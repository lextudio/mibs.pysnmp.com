# SNMP MIB module (ERI-DNX-SMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-SMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:21 2024
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

(eriMibs,
 eriProducts) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs",
    "eriProducts")

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


# MODULE-IDENTITY

eriDNXSmcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 1)
)
eriDNXSmcMIB.setRevisions(
        ("2003-05-19 00:00",
         "2003-05-06 00:00",
         "2003-03-21 00:00",
         "2003-02-25 00:00",
         "2003-01-28 00:00",
         "2003-01-10 00:00",
         "2003-01-03 00:00",
         "2002-11-18 00:00",
         "2002-10-30 00:00",
         "2002-09-19 00:00",
         "2002-08-20 00:00",
         "2002-07-22 00:00",
         "2002-07-03 00:00",
         "2002-05-31 00:00",
         "2002-05-13 00:00",
         "2002-05-06 00:00",
         "2002-04-22 00:00",
         "2002-04-18 00:00",
         "2002-04-12 00:00",
         "2002-03-11 00:00",
         "2001-11-13 00:00",
         "2001-09-10 00:00",
         "2001-08-13 00:00",
         "2001-07-19 00:00",
         "2001-07-05 00:00",
         "2001-06-23 00:00",
         "2001-06-01 00:00",
         "2001-05-21 00:00",
         "2001-03-23 00:00",
         "2001-03-01 00:00",
         "2001-01-02 00:00",
         "2000-12-01 00:00",
         "2000-10-26 00:00",
         "2000-10-02 00:00",
         "2000-07-26 00:00",
         "2000-05-31 00:00",
         "2000-05-15 00:00",
         "2000-02-25 00:00",
         "1999-12-15 00:00",
         "1999-11-09 00:00",
         "1998-12-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DnxResourceType(Integer32, TextualConvention):
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
              124,
              125,
              126,
              127,
              128,
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
              144)
        )
    )
    namedValues = NamedValues(
        *(("clockDs0DP", 126),
          ("deviceAsync", 34),
          ("deviceContact", 32),
          ("deviceDs0DP", 25),
          ("deviceE3", 28),
          ("deviceGr303", 19),
          ("deviceHybridDS3", 18),
          ("deviceNodeManager", 22),
          ("deviceOC3", 27),
          ("deviceOC3X", 31),
          ("deviceOctalE1T1", 1),
          ("deviceOctalHighSpeed", 3),
          ("deviceQuadHighSpeed", 2),
          ("deviceQuadOcu", 4),
          ("deviceQuadT1", 6),
          ("deviceRouterCard", 16),
          ("deviceSTM1", 26),
          ("deviceSTM1X", 30),
          ("deviceSts1", 17),
          ("deviceSync", 35),
          ("deviceSystemManager", 5),
          ("deviceT3", 7),
          ("deviceTempSensor", 38),
          ("deviceTestAccess", 8),
          ("deviceTranscoder", 41),
          ("deviceVoice", 9),
          ("deviceVoiceEM", 10),
          ("deviceVoiceFXO", 11),
          ("deviceVoiceFXS", 12),
          ("deviceVoltage", 33),
          ("deviceWan", 36),
          ("deviceXCC", 20),
          ("deviceXLC", 21),
          ("deviceXLC-T1E1", 29),
          ("dnx1UPowerSupply", 39),
          ("dnx1UQuadT1E1", 37),
          ("dnx1USysMgr", 40),
          ("linkE3-E1", 136),
          ("linkHds3-T1E1", 119),
          ("linkOC3-T1E1", 130),
          ("linkSTM1-T1E1", 128),
          ("linkSts1-T1E1", 117),
          ("linkT1E1", 141),
          ("linkT3-T1", 106),
          ("linkXlink", 124),
          ("nest", 23),
          ("node", 24),
          ("opticalXlink", 137),
          ("overheadOC3", 134),
          ("overheadSTM1", 132),
          ("payloadOC3", 133),
          ("payloadSTM1", 131),
          ("portAsync", 140),
          ("portContact", 138),
          ("portDs0DP", 125),
          ("portE3", 135),
          ("portGr303", 121),
          ("portHighSpeed", 142),
          ("portHybridDS3", 120),
          ("portOctal-T1E1", 100),
          ("portOctalHighSpeed", 102),
          ("portOctalT1", 105),
          ("portQuadHighSpeed", 101),
          ("portQuadOcu", 103),
          ("portQuadT1", 104),
          ("portRouter", 116),
          ("portSts1", 118),
          ("portT3", 107),
          ("portTestAccess", 108),
          ("portTranscoder", 144),
          ("portVirtualWan", 143),
          ("portVoiceEM", 109),
          ("portVoiceFXO", 110),
          ("portVoiceFXS", 111),
          ("portVoltage", 139),
          ("powerSupply", 14),
          ("protectionSwitch", 15),
          ("psxBroadband", 113),
          ("psxBroadbandSpare", 115),
          ("psxNarrowband", 112),
          ("psxNarrowbandSpare", 114),
          ("slot", 0),
          ("sysMgrClock", 127))
    )



class AlarmSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("informational", 1),
          ("major", 3),
          ("minor", 2),
          ("nominal", 0))
    )



class DecisionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class FunctionSwitch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class CurrentDevStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )



class PortStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-service", 1),
          ("out-service", 0))
    )



class DataSwitch(Integer32, TextualConvention):
    status = "current"
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



class TimeSlotAddress(IpAddress, TextualConvention):
    status = "current"


class LinkPortAddress(IpAddress, TextualConvention):
    status = "current"


class ClockSrcAddress(IpAddress, TextualConvention):
    status = "current"


class NestSlotAddress(IpAddress, TextualConvention):
    status = "current"


class UnsignedInt(Unsigned32, TextualConvention):
    status = "current"


class ConnectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("broadcastConnection", 1),
          ("broadcastMaster", 2),
          ("fullDuplex", 0),
          ("listenDest", 4),
          ("listenSrc", 3),
          ("listenerConnection", 7),
          ("subChannel", 9),
          ("subRate", 10),
          ("vcmp", 8))
    )



class CommunicationsType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("comp16kBitGrp1-2", 3),
          ("comp16kBitGrp3-4", 4),
          ("comp16kBitGrp5-6", 5),
          ("comp16kBitGrp7-8", 6),
          ("comp32kBitGrp1-4", 7),
          ("comp32kBitGrp5-8", 8),
          ("data", 0),
          ("voice", 1),
          ("voiceAuToMu", 2))
    )



class ConnectionState1(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inSrvc", 0),
          ("outOfSrvc", 1))
    )



class ConnectionState2(Integer32, TextualConvention):
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
        *(("cfgError", 3),
          ("ok", 1),
          ("underTest", 2))
    )



class MapNumber(Integer32, TextualConvention):
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
        *(("activeMap", 0),
          ("map01", 1),
          ("map02", 2),
          ("map03", 3),
          ("map04", 4),
          ("map05", 5))
    )



class TestAccess(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("monitorDest", 2),
          ("monitorSrc", 1),
          ("monitorSrcNDest", 3),
          ("none", 0),
          ("splitDest", 5),
          ("splitSrc", 4),
          ("splitSrcNDest", 6))
    )



class ConnectionSpeed(Integer32, TextualConvention):
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
              96,
              99)
        )
    )
    namedValues = NamedValues(
        *(("clearE1-32x64", 66),
          ("clearT1-25x64", 65),
          ("no-connection", 99),
          ("s1008k-18x56", 35),
          ("s1024k-16x64", 32),
          ("s1064k-19x56", 37),
          ("s1088k-17x64", 34),
          ("s1120k-20x56", 39),
          ("s112k-2x56", 3),
          ("s1152k-18x64", 36),
          ("s1176k-21x56", 41),
          ("s1216k-19x64", 38),
          ("s1232k-22x56", 43),
          ("s1280k-20x64", 40),
          ("s1288k-23x56", 45),
          ("s128k-2x64", 4),
          ("s1344k-21x64", 42),
          ("s1344k-24x56", 47),
          ("s1400k-25x56", 49),
          ("s1408k-22x64", 44),
          ("s1456k-26x56", 51),
          ("s1472k-23x64", 46),
          ("s1512k-27x56", 53),
          ("s1536k-24x64", 48),
          ("s1568k-28x56", 55),
          ("s1600k-25x64", 50),
          ("s1624k-29x56", 57),
          ("s1664k-26x64", 52),
          ("s1680k-30x56", 59),
          ("s168k-3x56", 5),
          ("s16k", 68),
          ("s1728k-27x64", 54),
          ("s1736k-31x56", 61),
          ("s1792k-28x64", 56),
          ("s1792k-32x56", 63),
          ("s1856k-29x64", 58),
          ("s1920k-30x64", 60),
          ("s192k-3x64", 6),
          ("s1984k-31x64", 62),
          ("s2048k-32x64", 64),
          ("s224k-4x56", 7),
          ("s256k-4x64", 8),
          ("s280k-5x56", 9),
          ("s320k-5x64", 10),
          ("s32k", 67),
          ("s336k-6x56", 11),
          ("s384k-6x64", 12),
          ("s392k-7x56", 13),
          ("s448k-7x64", 14),
          ("s448k-8x56", 15),
          ("s48k", 0),
          ("s504k-9x56", 17),
          ("s512k-8x64", 16),
          ("s560k-10x56", 19),
          ("s56k", 1),
          ("s576k-9x64", 18),
          ("s616k-11x56", 21),
          ("s640k-10x64", 20),
          ("s64k", 2),
          ("s672k-12x56", 23),
          ("s704k-11x64", 22),
          ("s728k-13x56", 25),
          ("s768k-12x64", 24),
          ("s784k-14x56", 27),
          ("s832k-13x64", 26),
          ("s840k-15x56", 29),
          ("s896k-14x64", 28),
          ("s896k-16x56", 31),
          ("s952k-17x56", 33),
          ("s9600-baud", 96),
          ("s960k-15x64", 30))
    )



class ConnCmdStatus(Integer32, TextualConvention):
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
              101,
              102,
              103,
              104,
              105,
              106,
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
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("add", 3),
          ("add-save-successful", 104),
          ("add-successful", 103),
          ("addNsave", 4),
          ("del-save-successful", 106),
          ("delete", 2),
          ("delete-successful", 102),
          ("deleteNsave", 6),
          ("err-cannot-chg-net-conn", 434),
          ("err-conn-max-channels-used", 430),
          ("err-conn-name-in-use", 404),
          ("err-conn-not-saved-to-map", 426),
          ("err-conn-test-in-progress", 424),
          ("err-connection-map-full", 427),
          ("err-data-locked-by-another-user", 450),
          ("err-dest-port-bandwidth-exceeded", 413),
          ("err-dest-port-cannot-be-voice", 417),
          ("err-dest-port-in-use", 403),
          ("err-dest-xlink-slot-not-assigned", 432),
          ("err-general-connection-error", 400),
          ("err-invalid-broadcast-id", 405),
          ("err-invalid-card-type", 428),
          ("err-invalid-command", 414),
          ("err-invalid-communications-dev", 418),
          ("err-invalid-communications-type", 419),
          ("err-invalid-conn-bit-group", 429),
          ("err-invalid-conn-id", 425),
          ("err-invalid-conn-name", 420),
          ("err-invalid-conn-record", 423),
          ("err-invalid-conn-speed", 422),
          ("err-invalid-conn-type", 421),
          ("err-invalid-dest-port", 411),
          ("err-invalid-dest-slot", 410),
          ("err-invalid-dest-timeslot", 412),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-src-port", 407),
          ("err-invalid-src-slot", 406),
          ("err-invalid-src-timeslot", 408),
          ("err-not-enough-bts-available", 415),
          ("err-protection-grp-conn-error", 433),
          ("err-snmp-parse-failed", 500),
          ("err-src-broadcast-id-not-found", 401),
          ("err-src-port-bandwidth-exceeded", 409),
          ("err-src-port-cannot-be-voice", 416),
          ("err-src-port-in-use", 402),
          ("err-src-xlink-slot-not-assigned", 431),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-save-successful", 105),
          ("update-successful", 101),
          ("updateNsave", 5))
    )



class LinkCmdStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              7,
              9,
              12,
              101,
              107,
              109,
              112,
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
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("copy-successful", 109),
          ("copyToAll", 9),
          ("err-cts-not-applicable", 425),
          ("err-data-locked-by-another-user", 450),
          ("err-dcd-dsr-not-applicable", 423),
          ("err-device-in-standby", 414),
          ("err-device-is-protection-module", 428),
          ("err-general-link-config-error", 400),
          ("err-gr303-not-applicable", 426),
          ("err-invalid-clock-timing", 421),
          ("err-invalid-control-signal", 422),
          ("err-invalid-esf-format", 405),
          ("err-invalid-idle-code", 413),
          ("err-invalid-interface", 419),
          ("err-invalid-link-ais", 409),
          ("err-invalid-link-bits", 427),
          ("err-invalid-link-command", 403),
          ("err-invalid-link-density", 406),
          ("err-invalid-link-framing", 402),
          ("err-invalid-link-lbo", 404),
          ("err-invalid-link-mapping", 415),
          ("err-invalid-link-name", 418),
          ("err-invalid-link-op-mode", 407),
          ("err-invalid-link-rem-loop", 408),
          ("err-invalid-link-status", 401),
          ("err-invalid-link-vt-group", 416),
          ("err-invalid-network-loop", 410),
          ("err-invalid-polarity", 420),
          ("err-invalid-rcv-clocksrc", 417),
          ("err-invalid-red-timeout", 412),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-yellow-alarm", 411),
          ("err-requires-special-mode", 424),
          ("err-snmp-parse-failed", 500),
          ("inServiceAll", 7),
          ("insvc-successful", 107),
          ("oos-successful", 112),
          ("outOfServiceAll", 12),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )



class OneByteField(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class DnxTsPortType(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("ds0dp", 11),
          ("e1", 1),
          ("e1-cas", 5),
          ("e1-clear-frm", 6),
          ("e1-clear-unfrm", 8),
          ("high-speed", 3),
          ("ocu", 12),
          ("t1", 2),
          ("t1-clear-frm", 7),
          ("t1-clear-unfrm", 9),
          ("tam", 13),
          ("unknown", 0),
          ("voice", 10),
          ("wan", 4))
    )



class DnxTrunkProfSelection(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("profile-1", 1),
          ("profile-10", 10),
          ("profile-11", 11),
          ("profile-12", 12),
          ("profile-13", 13),
          ("profile-14", 14),
          ("profile-15", 15),
          ("profile-16", 16),
          ("profile-2", 2),
          ("profile-3", 3),
          ("profile-4", 4),
          ("profile-5", 5),
          ("profile-6", 6),
          ("profile-7", 7),
          ("profile-8", 8),
          ("profile-9", 9))
    )



# MIB Managed Objects in the order of their OIDs

_EriTrapEnterprise_ObjectIdentity = ObjectIdentity
eriTrapEnterprise = _EriTrapEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 0)
)
if mibBuilder.loadTexts:
    eriTrapEnterprise.setStatus("current")
_Dnx_ObjectIdentity = ObjectIdentity
dnx = _Dnx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4)
)
_DnxTrapEnterprise_ObjectIdentity = ObjectIdentity
dnxTrapEnterprise = _DnxTrapEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0)
)
if mibBuilder.loadTexts:
    dnxTrapEnterprise.setStatus("current")
_SysMgr_ObjectIdentity = ObjectIdentity
sysMgr = _SysMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1)
)
_ResourceTable_Object = MibTable
resourceTable = _ResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    resourceTable.setStatus("current")
_ResourceEntry_Object = MibTableRow
resourceEntry = _ResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1)
)
resourceEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "resourceKey"),
)
if mibBuilder.loadTexts:
    resourceEntry.setStatus("current")
_ResourceKey_Type = UnsignedInt
_ResourceKey_Object = MibTableColumn
resourceKey = _ResourceKey_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 1),
    _ResourceKey_Type()
)
resourceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceKey.setStatus("current")
_ResourceAddr_Type = DisplayString
_ResourceAddr_Object = MibTableColumn
resourceAddr = _ResourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 2),
    _ResourceAddr_Type()
)
resourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAddr.setStatus("current")
_ResourceType_Type = DnxResourceType
_ResourceType_Object = MibTableColumn
resourceType = _ResourceType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 3),
    _ResourceType_Type()
)
resourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceType.setStatus("current")
_ResourceState_Type = UnsignedInt
_ResourceState_Object = MibTableColumn
resourceState = _ResourceState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 4),
    _ResourceState_Type()
)
resourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceState.setStatus("current")
_ResourceCriticalMask_Type = UnsignedInt
_ResourceCriticalMask_Object = MibTableColumn
resourceCriticalMask = _ResourceCriticalMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 5),
    _ResourceCriticalMask_Type()
)
resourceCriticalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceCriticalMask.setStatus("current")
_ResourceMajorMask_Type = UnsignedInt
_ResourceMajorMask_Object = MibTableColumn
resourceMajorMask = _ResourceMajorMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 6),
    _ResourceMajorMask_Type()
)
resourceMajorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceMajorMask.setStatus("current")
_ResourceMinorMask_Type = UnsignedInt
_ResourceMinorMask_Object = MibTableColumn
resourceMinorMask = _ResourceMinorMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 7),
    _ResourceMinorMask_Type()
)
resourceMinorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceMinorMask.setStatus("current")
_ResourceInfoMask_Type = UnsignedInt
_ResourceInfoMask_Object = MibTableColumn
resourceInfoMask = _ResourceInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 8),
    _ResourceInfoMask_Type()
)
resourceInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceInfoMask.setStatus("current")
_ResourceNominalMask_Type = UnsignedInt
_ResourceNominalMask_Object = MibTableColumn
resourceNominalMask = _ResourceNominalMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 9),
    _ResourceNominalMask_Type()
)
resourceNominalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceNominalMask.setStatus("current")
_ResourceTrapMask_Type = UnsignedInt
_ResourceTrapMask_Object = MibTableColumn
resourceTrapMask = _ResourceTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 1, 1, 10),
    _ResourceTrapMask_Type()
)
resourceTrapMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceTrapMask.setStatus("current")
_ResourceAlarmTable_Object = MibTable
resourceAlarmTable = _ResourceAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    resourceAlarmTable.setStatus("current")
_ResourceAlarmEntry_Object = MibTableRow
resourceAlarmEntry = _ResourceAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1)
)
resourceAlarmEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "resourceAlarmKey"),
)
if mibBuilder.loadTexts:
    resourceAlarmEntry.setStatus("current")
_ResourceAlarmKey_Type = UnsignedInt
_ResourceAlarmKey_Object = MibTableColumn
resourceAlarmKey = _ResourceAlarmKey_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 1),
    _ResourceAlarmKey_Type()
)
resourceAlarmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmKey.setStatus("current")
_ResourceAlarmAddr_Type = DisplayString
_ResourceAlarmAddr_Object = MibTableColumn
resourceAlarmAddr = _ResourceAlarmAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 2),
    _ResourceAlarmAddr_Type()
)
resourceAlarmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmAddr.setStatus("current")
_ResourceAlarmType_Type = DnxResourceType
_ResourceAlarmType_Object = MibTableColumn
resourceAlarmType = _ResourceAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 3),
    _ResourceAlarmType_Type()
)
resourceAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmType.setStatus("current")
_ResourceAlarmState_Type = UnsignedInt
_ResourceAlarmState_Object = MibTableColumn
resourceAlarmState = _ResourceAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 4),
    _ResourceAlarmState_Type()
)
resourceAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmState.setStatus("current")
_ResourceAlarmCriticalMask_Type = UnsignedInt
_ResourceAlarmCriticalMask_Object = MibTableColumn
resourceAlarmCriticalMask = _ResourceAlarmCriticalMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 5),
    _ResourceAlarmCriticalMask_Type()
)
resourceAlarmCriticalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmCriticalMask.setStatus("current")
_ResourceAlarmMajorMask_Type = UnsignedInt
_ResourceAlarmMajorMask_Object = MibTableColumn
resourceAlarmMajorMask = _ResourceAlarmMajorMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 6),
    _ResourceAlarmMajorMask_Type()
)
resourceAlarmMajorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmMajorMask.setStatus("current")
_ResourceAlarmMinorMask_Type = UnsignedInt
_ResourceAlarmMinorMask_Object = MibTableColumn
resourceAlarmMinorMask = _ResourceAlarmMinorMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 7),
    _ResourceAlarmMinorMask_Type()
)
resourceAlarmMinorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmMinorMask.setStatus("current")
_ResourceAlarmInfoMask_Type = UnsignedInt
_ResourceAlarmInfoMask_Object = MibTableColumn
resourceAlarmInfoMask = _ResourceAlarmInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 8),
    _ResourceAlarmInfoMask_Type()
)
resourceAlarmInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmInfoMask.setStatus("current")
_ResourceAlarmNominalMask_Type = UnsignedInt
_ResourceAlarmNominalMask_Object = MibTableColumn
resourceAlarmNominalMask = _ResourceAlarmNominalMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 9),
    _ResourceAlarmNominalMask_Type()
)
resourceAlarmNominalMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmNominalMask.setStatus("current")
_ResourceAlarmTrapMask_Type = UnsignedInt
_ResourceAlarmTrapMask_Object = MibTableColumn
resourceAlarmTrapMask = _ResourceAlarmTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 2, 1, 10),
    _ResourceAlarmTrapMask_Type()
)
resourceAlarmTrapMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceAlarmTrapMask.setStatus("current")
_SysProfile_ObjectIdentity = ObjectIdentity
sysProfile = _SysProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6)
)


class _UnitName_Type(DisplayString):
    """Custom type unitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_UnitName_Type.__name__ = "DisplayString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 1),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")


class _UnitType_Type(Integer32):
    """Custom type unitType based on Integer32"""
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
        *(("dnx11", 2),
          ("dnx11-psx", 3),
          ("dnx1U", 5),
          ("dnx4", 1),
          ("dnx88", 4))
    )


_UnitType_Type.__name__ = "Integer32"
_UnitType_Object = MibScalar
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 2),
    _UnitType_Type()
)
unitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitType.setStatus("current")


class _ActiveSMC_Type(Integer32):
    """Custom type activeSMC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("smc-A", 1),
          ("smc-B", 2))
    )


_ActiveSMC_Type.__name__ = "Integer32"
_ActiveSMC_Object = MibScalar
activeSMC = _ActiveSMC_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 3),
    _ActiveSMC_Type()
)
activeSMC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeSMC.setStatus("current")


class _SystemRelease_Type(DisplayString):
    """Custom type systemRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_SystemRelease_Type.__name__ = "DisplayString"
_SystemRelease_Object = MibScalar
systemRelease = _SystemRelease_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 4),
    _SystemRelease_Type()
)
systemRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemRelease.setStatus("current")


class _ReleaseDate_Type(DisplayString):
    """Custom type releaseDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ReleaseDate_Type.__name__ = "DisplayString"
_ReleaseDate_Object = MibScalar
releaseDate = _ReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 5),
    _ReleaseDate_Type()
)
releaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseDate.setStatus("current")


class _FlashChksum_Type(DisplayString):
    """Custom type flashChksum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FlashChksum_Type.__name__ = "DisplayString"
_FlashChksum_Object = MibScalar
flashChksum = _FlashChksum_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 6),
    _FlashChksum_Type()
)
flashChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashChksum.setStatus("current")


class _XilinxType_Type(DisplayString):
    """Custom type xilinxType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_XilinxType_Type.__name__ = "DisplayString"
_XilinxType_Object = MibScalar
xilinxType = _XilinxType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 7),
    _XilinxType_Type()
)
xilinxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xilinxType.setStatus("current")


class _XilinxVersion_Type(DisplayString):
    """Custom type xilinxVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_XilinxVersion_Type.__name__ = "DisplayString"
_XilinxVersion_Object = MibScalar
xilinxVersion = _XilinxVersion_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 8),
    _XilinxVersion_Type()
)
xilinxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xilinxVersion.setStatus("current")
_RearModem_Type = DecisionType
_RearModem_Object = MibScalar
rearModem = _RearModem_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 9),
    _RearModem_Type()
)
rearModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rearModem.setStatus("current")


class _MibProfile_Type(DisplayString):
    """Custom type mibProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_MibProfile_Type.__name__ = "DisplayString"
_MibProfile_Object = MibScalar
mibProfile = _MibProfile_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 10),
    _MibProfile_Type()
)
mibProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfile.setStatus("current")


class _SystemMgrType_Type(Integer32):
    """Custom type systemMgrType based on Integer32"""
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
        *(("dnx1u-sys", 4),
          ("smc-I", 1),
          ("smc-II", 2),
          ("xnm", 3))
    )


_SystemMgrType_Type.__name__ = "Integer32"
_SystemMgrType_Object = MibScalar
systemMgrType = _SystemMgrType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 11),
    _SystemMgrType_Type()
)
systemMgrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMgrType.setStatus("current")


class _SysAlarmCutOff_Type(Integer32):
    """Custom type sysAlarmCutOff based on Integer32"""
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


_SysAlarmCutOff_Type.__name__ = "Integer32"
_SysAlarmCutOff_Object = MibScalar
sysAlarmCutOff = _SysAlarmCutOff_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 12),
    _SysAlarmCutOff_Type()
)
sysAlarmCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmCutOff.setStatus("current")


class _SysMacAddress_Type(OctetString):
    """Custom type sysMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SysMacAddress_Type.__name__ = "OctetString"
_SysMacAddress_Object = MibScalar
sysMacAddress = _SysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 13),
    _SysMacAddress_Type()
)
sysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAddress.setStatus("current")


class _SysSa4RxTxTrap_Type(Integer32):
    """Custom type sysSa4RxTxTrap based on Integer32"""
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


_SysSa4RxTxTrap_Type.__name__ = "Integer32"
_SysSa4RxTxTrap_Object = MibScalar
sysSa4RxTxTrap = _SysSa4RxTxTrap_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 14),
    _SysSa4RxTxTrap_Type()
)
sysSa4RxTxTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSa4RxTxTrap.setStatus("current")


class _SysCustomerId_Type(Integer32):
    """Custom type sysCustomerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_SysCustomerId_Type.__name__ = "Integer32"
_SysCustomerId_Object = MibScalar
sysCustomerId = _SysCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 15),
    _SysCustomerId_Type()
)
sysCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCustomerId.setStatus("current")
_SysMgrOnlineTime_Type = TimeTicks
_SysMgrOnlineTime_Object = MibScalar
sysMgrOnlineTime = _SysMgrOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 16),
    _SysMgrOnlineTime_Type()
)
sysMgrOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgrOnlineTime.setStatus("current")
_FeatureKeys_ObjectIdentity = ObjectIdentity
featureKeys = _FeatureKeys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100)
)
_DnxFeatureKeyTable_Object = MibTable
dnxFeatureKeyTable = _DnxFeatureKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 1)
)
if mibBuilder.loadTexts:
    dnxFeatureKeyTable.setStatus("current")
_DnxFeatureKeyEntry_Object = MibTableRow
dnxFeatureKeyEntry = _DnxFeatureKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 1, 1)
)
dnxFeatureKeyEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "featureKeyId"),
)
if mibBuilder.loadTexts:
    dnxFeatureKeyEntry.setStatus("current")


class _FeatureKeyId_Type(Integer32):
    """Custom type featureKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FeatureKeyId_Type.__name__ = "Integer32"
_FeatureKeyId_Object = MibTableColumn
featureKeyId = _FeatureKeyId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 1, 1, 1),
    _FeatureKeyId_Type()
)
featureKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureKeyId.setStatus("current")
_FeatureKeyName_Type = DisplayString
_FeatureKeyName_Object = MibTableColumn
featureKeyName = _FeatureKeyName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 1, 1, 2),
    _FeatureKeyName_Type()
)
featureKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureKeyName.setStatus("current")


class _FeatureKeyState_Type(Integer32):
    """Custom type featureKeyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("noKey", 0))
    )


_FeatureKeyState_Type.__name__ = "Integer32"
_FeatureKeyState_Object = MibTableColumn
featureKeyState = _FeatureKeyState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 1, 1, 3),
    _FeatureKeyState_Type()
)
featureKeyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureKeyState.setStatus("current")


class _FeatureKeyCmdStatus_Type(Integer32):
    """Custom type featureKeyCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              101,
              102,
              400,
              401,
              450,
              451,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("delete-successful", 102),
          ("deleteKey", 2),
          ("err-data-locked-by-another-user", 450),
          ("err-general-key-config-error", 400),
          ("err-invalid-cmd-status", 451),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-state", 401),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_FeatureKeyCmdStatus_Type.__name__ = "Integer32"
_FeatureKeyCmdStatus_Object = MibTableColumn
featureKeyCmdStatus = _FeatureKeyCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 1, 1, 4),
    _FeatureKeyCmdStatus_Type()
)
featureKeyCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featureKeyCmdStatus.setStatus("current")
_EnterNewFeatureKey_ObjectIdentity = ObjectIdentity
enterNewFeatureKey = _EnterNewFeatureKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 2)
)
_NewKeyCode_Type = DisplayString
_NewKeyCode_Object = MibScalar
newKeyCode = _NewKeyCode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 2, 1),
    _NewKeyCode_Type()
)
newKeyCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newKeyCode.setStatus("current")


class _NewKeyCodeCmdStatus_Type(Integer32):
    """Custom type newKeyCodeCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              402,
              450,
              451,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("enterKey", 1),
          ("err-data-locked-by-another-user", 450),
          ("err-invalid-cmd-status", 451),
          ("err-invalid-key", 402),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("key-successful", 101),
          ("ready-for-command", 0))
    )


_NewKeyCodeCmdStatus_Type.__name__ = "Integer32"
_NewKeyCodeCmdStatus_Object = MibScalar
newKeyCodeCmdStatus = _NewKeyCodeCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 6, 100, 2, 2),
    _NewKeyCodeCmdStatus_Type()
)
newKeyCodeCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newKeyCodeCmdStatus.setStatus("current")
_SysClock_ObjectIdentity = ObjectIdentity
sysClock = _SysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7)
)
_SysDateTime_ObjectIdentity = ObjectIdentity
sysDateTime = _SysDateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1)
)


class _SysMonth_Type(Integer32):
    """Custom type sysMonth based on Integer32"""
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_SysMonth_Type.__name__ = "Integer32"
_SysMonth_Object = MibScalar
sysMonth = _SysMonth_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 1),
    _SysMonth_Type()
)
sysMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonth.setStatus("current")


class _SysDay_Type(Integer32):
    """Custom type sysDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SysDay_Type.__name__ = "Integer32"
_SysDay_Object = MibScalar
sysDay = _SysDay_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 2),
    _SysDay_Type()
)
sysDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDay.setStatus("current")
_SysYear_Type = Integer32
_SysYear_Object = MibScalar
sysYear = _SysYear_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 3),
    _SysYear_Type()
)
sysYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysYear.setStatus("current")


class _SysHour_Type(Integer32):
    """Custom type sysHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SysHour_Type.__name__ = "Integer32"
_SysHour_Object = MibScalar
sysHour = _SysHour_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 4),
    _SysHour_Type()
)
sysHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHour.setStatus("current")


class _SysMin_Type(Integer32):
    """Custom type sysMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SysMin_Type.__name__ = "Integer32"
_SysMin_Object = MibScalar
sysMin = _SysMin_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 5),
    _SysMin_Type()
)
sysMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMin.setStatus("current")


class _SysSec_Type(Integer32):
    """Custom type sysSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SysSec_Type.__name__ = "Integer32"
_SysSec_Object = MibScalar
sysSec = _SysSec_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 6),
    _SysSec_Type()
)
sysSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSec.setStatus("current")


class _SysWeekday_Type(Integer32):
    """Custom type sysWeekday based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_SysWeekday_Type.__name__ = "Integer32"
_SysWeekday_Object = MibScalar
sysWeekday = _SysWeekday_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 7),
    _SysWeekday_Type()
)
sysWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysWeekday.setStatus("current")


class _SysTimeCmdStatus_Type(Integer32):
    """Custom type sysTimeCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
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
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-data-locked-by-another-user", 450),
          ("err-general-time-date-error", 200),
          ("err-invalid-calendar", 208),
          ("err-invalid-day", 201),
          ("err-invalid-hours", 204),
          ("err-invalid-minutes", 205),
          ("err-invalid-month", 202),
          ("err-invalid-seconds", 206),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-sys-time-cmd", 209),
          ("err-invalid-weekday", 207),
          ("err-invalid-year", 203),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update-successful", 101),
          ("update-sys-time", 1))
    )


_SysTimeCmdStatus_Type.__name__ = "Integer32"
_SysTimeCmdStatus_Object = MibScalar
sysTimeCmdStatus = _SysTimeCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 1, 8),
    _SysTimeCmdStatus_Type()
)
sysTimeCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeCmdStatus.setStatus("current")
_ClockSrcConfig_ObjectIdentity = ObjectIdentity
clockSrcConfig = _ClockSrcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 2)
)


class _ClockSrcActive_Type(Integer32):
    """Custom type clockSrcActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 0),
          ("holdover", 1),
          ("primary", 2),
          ("primary-protected", 6),
          ("secondary", 3),
          ("secondary-protected", 7),
          ("tertiary", 4),
          ("tertiary-protected", 8))
    )


_ClockSrcActive_Type.__name__ = "Integer32"
_ClockSrcActive_Object = MibScalar
clockSrcActive = _ClockSrcActive_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 2, 1),
    _ClockSrcActive_Type()
)
clockSrcActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockSrcActive.setStatus("current")
_PrimaryClockSrc_Type = ClockSrcAddress
_PrimaryClockSrc_Object = MibScalar
primaryClockSrc = _PrimaryClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 2, 2),
    _PrimaryClockSrc_Type()
)
primaryClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryClockSrc.setStatus("current")
_SecondaryClockSrc_Type = ClockSrcAddress
_SecondaryClockSrc_Object = MibScalar
secondaryClockSrc = _SecondaryClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 2, 3),
    _SecondaryClockSrc_Type()
)
secondaryClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryClockSrc.setStatus("current")
_TertiaryClockSrc_Type = ClockSrcAddress
_TertiaryClockSrc_Object = MibScalar
tertiaryClockSrc = _TertiaryClockSrc_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 2, 4),
    _TertiaryClockSrc_Type()
)
tertiaryClockSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tertiaryClockSrc.setStatus("current")


class _ClockSrcMode_Type(Integer32):
    """Custom type clockSrcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("freerun", 0),
          ("primary", 2),
          ("secondary", 3),
          ("tertiary", 4))
    )


_ClockSrcMode_Type.__name__ = "Integer32"
_ClockSrcMode_Object = MibScalar
clockSrcMode = _ClockSrcMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 2, 5),
    _ClockSrcMode_Type()
)
clockSrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockSrcMode.setStatus("current")


class _ClockSrcCmdStatus_Type(Integer32):
    """Custom type clockSrcCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              200,
              201,
              202,
              203,
              204,
              205,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-data-locked-by-another-user", 450),
          ("err-gen-clock-src-config-error", 200),
          ("err-invalid-clock-mode", 204),
          ("err-invalid-clock-src-command", 203),
          ("err-invalid-port", 202),
          ("err-invalid-slot", 201),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-station-clock", 205),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update-clock-src", 1),
          ("update-successful", 101))
    )


_ClockSrcCmdStatus_Type.__name__ = "Integer32"
_ClockSrcCmdStatus_Object = MibScalar
clockSrcCmdStatus = _ClockSrcCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 7, 2, 6),
    _ClockSrcCmdStatus_Type()
)
clockSrcCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockSrcCmdStatus.setStatus("current")
_Connections_ObjectIdentity = ObjectIdentity
connections = _Connections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8)
)
_ConnInfo_ObjectIdentity = ObjectIdentity
connInfo = _ConnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 1)
)


class _ActiveMapId_Type(Integer32):
    """Custom type activeMapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ActiveMapId_Type.__name__ = "Integer32"
_ActiveMapId_Object = MibScalar
activeMapId = _ActiveMapId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 1, 1),
    _ActiveMapId_Type()
)
activeMapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeMapId.setStatus("current")
_ConnDBChecksum_Type = UnsignedInt
_ConnDBChecksum_Object = MibScalar
connDBChecksum = _ConnDBChecksum_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 1, 2),
    _ConnDBChecksum_Type()
)
connDBChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connDBChecksum.setStatus("current")


class _LastMapCopied_Type(Integer32):
    """Custom type lastMapCopied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_LastMapCopied_Type.__name__ = "Integer32"
_LastMapCopied_Object = MibScalar
lastMapCopied = _LastMapCopied_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 1, 3),
    _LastMapCopied_Type()
)
lastMapCopied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastMapCopied.setStatus("current")
_ConnMapTable_Object = MibTable
connMapTable = _ConnMapTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2)
)
if mibBuilder.loadTexts:
    connMapTable.setStatus("current")
_ConnMapEntry_Object = MibTableRow
connMapEntry = _ConnMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1)
)
connMapEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "connMapID"),
)
if mibBuilder.loadTexts:
    connMapEntry.setStatus("current")


class _ConnMapID_Type(Integer32):
    """Custom type connMapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ConnMapID_Type.__name__ = "Integer32"
_ConnMapID_Object = MibTableColumn
connMapID = _ConnMapID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 1),
    _ConnMapID_Type()
)
connMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMapID.setStatus("current")


class _ConnMapName_Type(DisplayString):
    """Custom type connMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_ConnMapName_Type.__name__ = "DisplayString"
_ConnMapName_Object = MibTableColumn
connMapName = _ConnMapName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 2),
    _ConnMapName_Type()
)
connMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connMapName.setStatus("current")


class _ConnMapCurrStatus_Type(Integer32):
    """Custom type connMapCurrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("non-active", 2),
          ("non-active-tagged", 3))
    )


_ConnMapCurrStatus_Type.__name__ = "Integer32"
_ConnMapCurrStatus_Object = MibTableColumn
connMapCurrStatus = _ConnMapCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 3),
    _ConnMapCurrStatus_Type()
)
connMapCurrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connMapCurrStatus.setStatus("current")


class _ConnMapDescription_Type(DisplayString):
    """Custom type connMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConnMapDescription_Type.__name__ = "DisplayString"
_ConnMapDescription_Object = MibTableColumn
connMapDescription = _ConnMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 4),
    _ConnMapDescription_Type()
)
connMapDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connMapDescription.setStatus("current")
_ConnMapCounts_Type = Counter32
_ConnMapCounts_Object = MibTableColumn
connMapCounts = _ConnMapCounts_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 5),
    _ConnMapCounts_Type()
)
connMapCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMapCounts.setStatus("current")
_ConnMapVersions_Type = Counter32
_ConnMapVersions_Object = MibTableColumn
connMapVersions = _ConnMapVersions_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 6),
    _ConnMapVersions_Type()
)
connMapVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMapVersions.setStatus("current")
_ConnMapDate_Type = DisplayString
_ConnMapDate_Object = MibTableColumn
connMapDate = _ConnMapDate_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 7),
    _ConnMapDate_Type()
)
connMapDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMapDate.setStatus("current")


class _ConnMapCmdStatus_Type(Integer32):
    """Custom type connMapCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7,
              8,
              9,
              100,
              101,
              102,
              107,
              108,
              109,
              200,
              202,
              203,
              204,
              205,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("activate-map", 7),
          ("activate-successful", 107),
          ("command-in-progress", 100),
          ("copy-map-to-tagged-maps", 9),
          ("copy-successful", 109),
          ("delete-map", 2),
          ("delete-successful", 102),
          ("err-data-locked-by-another-user", 450),
          ("err-general-map-config-error", 200),
          ("err-invalid-map-command", 202),
          ("err-invalid-map-desc", 204),
          ("err-invalid-map-name", 203),
          ("err-invalid-map-status", 205),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("save-map", 8),
          ("save-successful", 108),
          ("update-map", 1),
          ("update-successful", 101))
    )


_ConnMapCmdStatus_Type.__name__ = "Integer32"
_ConnMapCmdStatus_Object = MibTableColumn
connMapCmdStatus = _ConnMapCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 8),
    _ConnMapCmdStatus_Type()
)
connMapCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connMapCmdStatus.setStatus("current")
_ConnMapChecksum_Type = UnsignedInt
_ConnMapChecksum_Object = MibTableColumn
connMapChecksum = _ConnMapChecksum_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 2, 1, 9),
    _ConnMapChecksum_Type()
)
connMapChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connMapChecksum.setStatus("current")
_SysConnTable_Object = MibTable
sysConnTable = _SysConnTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3)
)
if mibBuilder.loadTexts:
    sysConnTable.setStatus("current")
_SysConnEntry_Object = MibTableRow
sysConnEntry = _SysConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1)
)
sysConnEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "sysMapID"),
    (0, "ERI-DNX-SMC-MIB", "sysConnID"),
)
if mibBuilder.loadTexts:
    sysConnEntry.setStatus("current")
_SysMapID_Type = MapNumber
_SysMapID_Object = MibTableColumn
sysMapID = _SysMapID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 1),
    _SysMapID_Type()
)
sysMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMapID.setStatus("current")


class _SysConnID_Type(Integer32):
    """Custom type sysConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16224),
    )


_SysConnID_Type.__name__ = "Integer32"
_SysConnID_Object = MibTableColumn
sysConnID = _SysConnID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 2),
    _SysConnID_Type()
)
sysConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConnID.setStatus("current")


class _SysConnName_Type(DisplayString):
    """Custom type sysConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_SysConnName_Type.__name__ = "DisplayString"
_SysConnName_Object = MibTableColumn
sysConnName = _SysConnName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 3),
    _SysConnName_Type()
)
sysConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConnName.setStatus("current")
_SysConnType_Type = ConnectionType
_SysConnType_Object = MibTableColumn
sysConnType = _SysConnType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 4),
    _SysConnType_Type()
)
sysConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConnType.setStatus("current")
_SysSrcAddr_Type = TimeSlotAddress
_SysSrcAddr_Object = MibTableColumn
sysSrcAddr = _SysSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 5),
    _SysSrcAddr_Type()
)
sysSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSrcAddr.setStatus("current")
_SysDestAddr_Type = TimeSlotAddress
_SysDestAddr_Object = MibTableColumn
sysDestAddr = _SysDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 6),
    _SysDestAddr_Type()
)
sysDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDestAddr.setStatus("current")
_SysComm_Type = CommunicationsType
_SysComm_Object = MibTableColumn
sysComm = _SysComm_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 7),
    _SysComm_Type()
)
sysComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysComm.setStatus("current")
_SysConnSpeed_Type = ConnectionSpeed
_SysConnSpeed_Object = MibTableColumn
sysConnSpeed = _SysConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 8),
    _SysConnSpeed_Type()
)
sysConnSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConnSpeed.setStatus("current")
_SysSrcTsBitmap_Type = Integer32
_SysSrcTsBitmap_Object = MibTableColumn
sysSrcTsBitmap = _SysSrcTsBitmap_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 9),
    _SysSrcTsBitmap_Type()
)
sysSrcTsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSrcTsBitmap.setStatus("current")
_SysDestTsBitmap_Type = Integer32
_SysDestTsBitmap_Object = MibTableColumn
sysDestTsBitmap = _SysDestTsBitmap_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 10),
    _SysDestTsBitmap_Type()
)
sysDestTsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDestTsBitmap.setStatus("current")
_SysBroadSrcId_Type = Integer32
_SysBroadSrcId_Object = MibTableColumn
sysBroadSrcId = _SysBroadSrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 11),
    _SysBroadSrcId_Type()
)
sysBroadSrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBroadSrcId.setStatus("current")
_SysTestMode_Type = TestAccess
_SysTestMode_Object = MibTableColumn
sysTestMode = _SysTestMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 12),
    _SysTestMode_Type()
)
sysTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTestMode.setStatus("obsolete")
_SysCmdStatus_Type = ConnCmdStatus
_SysCmdStatus_Object = MibTableColumn
sysCmdStatus = _SysCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 13),
    _SysCmdStatus_Type()
)
sysCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCmdStatus.setStatus("current")
_SysPrimaryState_Type = ConnectionState1
_SysPrimaryState_Object = MibTableColumn
sysPrimaryState = _SysPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 14),
    _SysPrimaryState_Type()
)
sysPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPrimaryState.setStatus("current")
_SysSecondaryState_Type = ConnectionState2
_SysSecondaryState_Object = MibTableColumn
sysSecondaryState = _SysSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 15),
    _SysSecondaryState_Type()
)
sysSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecondaryState.setStatus("current")
_SysConnInstance_Type = Integer32
_SysConnInstance_Object = MibTableColumn
sysConnInstance = _SysConnInstance_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 16),
    _SysConnInstance_Type()
)
sysConnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConnInstance.setStatus("current")
_SysConnChecksum_Type = UnsignedInt
_SysConnChecksum_Object = MibTableColumn
sysConnChecksum = _SysConnChecksum_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 17),
    _SysConnChecksum_Type()
)
sysConnChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConnChecksum.setStatus("current")
_SysSrcTsLineType_Type = DnxTsPortType
_SysSrcTsLineType_Object = MibTableColumn
sysSrcTsLineType = _SysSrcTsLineType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 18),
    _SysSrcTsLineType_Type()
)
sysSrcTsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSrcTsLineType.setStatus("current")
_SysDestTsLineType_Type = DnxTsPortType
_SysDestTsLineType_Object = MibTableColumn
sysDestTsLineType = _SysDestTsLineType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 19),
    _SysDestTsLineType_Type()
)
sysDestTsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDestTsLineType.setStatus("current")
_SysSrcTrunkCProfile_Type = DnxTrunkProfSelection
_SysSrcTrunkCProfile_Object = MibTableColumn
sysSrcTrunkCProfile = _SysSrcTrunkCProfile_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 20),
    _SysSrcTrunkCProfile_Type()
)
sysSrcTrunkCProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSrcTrunkCProfile.setStatus("current")
_SysDestTrunkCProfile_Type = DnxTrunkProfSelection
_SysDestTrunkCProfile_Object = MibTableColumn
sysDestTrunkCProfile = _SysDestTrunkCProfile_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 3, 1, 21),
    _SysDestTrunkCProfile_Type()
)
sysDestTrunkCProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDestTrunkCProfile.setStatus("current")
_ActvConnTable_Object = MibTable
actvConnTable = _ActvConnTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4)
)
if mibBuilder.loadTexts:
    actvConnTable.setStatus("current")
_ActvConnEntry_Object = MibTableRow
actvConnEntry = _ActvConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1)
)
actvConnEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "actvMapID"),
    (0, "ERI-DNX-SMC-MIB", "actvConnID"),
)
if mibBuilder.loadTexts:
    actvConnEntry.setStatus("current")
_ActvMapID_Type = MapNumber
_ActvMapID_Object = MibTableColumn
actvMapID = _ActvMapID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 1),
    _ActvMapID_Type()
)
actvMapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvMapID.setStatus("current")


class _ActvConnID_Type(Integer32):
    """Custom type actvConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16224),
    )


_ActvConnID_Type.__name__ = "Integer32"
_ActvConnID_Object = MibTableColumn
actvConnID = _ActvConnID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 2),
    _ActvConnID_Type()
)
actvConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvConnID.setStatus("current")


class _ActvConnName_Type(DisplayString):
    """Custom type actvConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ActvConnName_Type.__name__ = "DisplayString"
_ActvConnName_Object = MibTableColumn
actvConnName = _ActvConnName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 3),
    _ActvConnName_Type()
)
actvConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvConnName.setStatus("current")
_ActvConnType_Type = ConnectionType
_ActvConnType_Object = MibTableColumn
actvConnType = _ActvConnType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 4),
    _ActvConnType_Type()
)
actvConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvConnType.setStatus("current")
_ActvSrcAddr_Type = TimeSlotAddress
_ActvSrcAddr_Object = MibTableColumn
actvSrcAddr = _ActvSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 5),
    _ActvSrcAddr_Type()
)
actvSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvSrcAddr.setStatus("current")
_ActvDestAddr_Type = TimeSlotAddress
_ActvDestAddr_Object = MibTableColumn
actvDestAddr = _ActvDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 6),
    _ActvDestAddr_Type()
)
actvDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvDestAddr.setStatus("current")
_ActvComm_Type = CommunicationsType
_ActvComm_Object = MibTableColumn
actvComm = _ActvComm_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 7),
    _ActvComm_Type()
)
actvComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvComm.setStatus("current")
_ActvConnSpeed_Type = ConnectionSpeed
_ActvConnSpeed_Object = MibTableColumn
actvConnSpeed = _ActvConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 8),
    _ActvConnSpeed_Type()
)
actvConnSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvConnSpeed.setStatus("current")
_ActvSrcTsBitmap_Type = Integer32
_ActvSrcTsBitmap_Object = MibTableColumn
actvSrcTsBitmap = _ActvSrcTsBitmap_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 9),
    _ActvSrcTsBitmap_Type()
)
actvSrcTsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvSrcTsBitmap.setStatus("current")
_ActvDestTsBitmap_Type = Integer32
_ActvDestTsBitmap_Object = MibTableColumn
actvDestTsBitmap = _ActvDestTsBitmap_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 10),
    _ActvDestTsBitmap_Type()
)
actvDestTsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvDestTsBitmap.setStatus("current")
_ActvBroadSrcId_Type = Integer32
_ActvBroadSrcId_Object = MibTableColumn
actvBroadSrcId = _ActvBroadSrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 11),
    _ActvBroadSrcId_Type()
)
actvBroadSrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvBroadSrcId.setStatus("current")
_ActvTestMode_Type = TestAccess
_ActvTestMode_Object = MibTableColumn
actvTestMode = _ActvTestMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 12),
    _ActvTestMode_Type()
)
actvTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvTestMode.setStatus("obsolete")
_ActvCmdStatus_Type = ConnCmdStatus
_ActvCmdStatus_Object = MibTableColumn
actvCmdStatus = _ActvCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 13),
    _ActvCmdStatus_Type()
)
actvCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvCmdStatus.setStatus("current")
_ActvPrimaryState_Type = ConnectionState1
_ActvPrimaryState_Object = MibTableColumn
actvPrimaryState = _ActvPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 14),
    _ActvPrimaryState_Type()
)
actvPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvPrimaryState.setStatus("current")
_ActvSecondaryState_Type = ConnectionState2
_ActvSecondaryState_Object = MibTableColumn
actvSecondaryState = _ActvSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 15),
    _ActvSecondaryState_Type()
)
actvSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvSecondaryState.setStatus("current")
_ActvConnInstance_Type = Integer32
_ActvConnInstance_Object = MibTableColumn
actvConnInstance = _ActvConnInstance_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 16),
    _ActvConnInstance_Type()
)
actvConnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvConnInstance.setStatus("current")
_ActvConnChecksum_Type = UnsignedInt
_ActvConnChecksum_Object = MibTableColumn
actvConnChecksum = _ActvConnChecksum_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 17),
    _ActvConnChecksum_Type()
)
actvConnChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvConnChecksum.setStatus("current")
_ActvSrcTsLineType_Type = DnxTsPortType
_ActvSrcTsLineType_Object = MibTableColumn
actvSrcTsLineType = _ActvSrcTsLineType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 18),
    _ActvSrcTsLineType_Type()
)
actvSrcTsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvSrcTsLineType.setStatus("current")
_ActvDestTsLineType_Type = DnxTsPortType
_ActvDestTsLineType_Object = MibTableColumn
actvDestTsLineType = _ActvDestTsLineType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 19),
    _ActvDestTsLineType_Type()
)
actvDestTsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvDestTsLineType.setStatus("current")
_ActvSrcTrunkCProfile_Type = DnxTrunkProfSelection
_ActvSrcTrunkCProfile_Object = MibTableColumn
actvSrcTrunkCProfile = _ActvSrcTrunkCProfile_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 20),
    _ActvSrcTrunkCProfile_Type()
)
actvSrcTrunkCProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvSrcTrunkCProfile.setStatus("current")
_ActvDestTrunkCProfile_Type = DnxTrunkProfSelection
_ActvDestTrunkCProfile_Object = MibTableColumn
actvDestTrunkCProfile = _ActvDestTrunkCProfile_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 4, 1, 21),
    _ActvDestTrunkCProfile_Type()
)
actvDestTrunkCProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actvDestTrunkCProfile.setStatus("current")
_AddConnRecord_ObjectIdentity = ObjectIdentity
addConnRecord = _AddConnRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5)
)
_AddMapID_Type = MapNumber
_AddMapID_Object = MibScalar
addMapID = _AddMapID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 1),
    _AddMapID_Type()
)
addMapID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addMapID.setStatus("current")


class _AddConnID_Type(Integer32):
    """Custom type addConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16224),
    )


_AddConnID_Type.__name__ = "Integer32"
_AddConnID_Object = MibScalar
addConnID = _AddConnID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 2),
    _AddConnID_Type()
)
addConnID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addConnID.setStatus("current")


class _AddConnName_Type(DisplayString):
    """Custom type addConnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_AddConnName_Type.__name__ = "DisplayString"
_AddConnName_Object = MibScalar
addConnName = _AddConnName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 3),
    _AddConnName_Type()
)
addConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addConnName.setStatus("current")
_AddConnType_Type = ConnectionType
_AddConnType_Object = MibScalar
addConnType = _AddConnType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 4),
    _AddConnType_Type()
)
addConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addConnType.setStatus("current")
_AddSrcAddr_Type = TimeSlotAddress
_AddSrcAddr_Object = MibScalar
addSrcAddr = _AddSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 5),
    _AddSrcAddr_Type()
)
addSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addSrcAddr.setStatus("current")
_AddDestAddr_Type = TimeSlotAddress
_AddDestAddr_Object = MibScalar
addDestAddr = _AddDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 6),
    _AddDestAddr_Type()
)
addDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addDestAddr.setStatus("current")
_AddComm_Type = CommunicationsType
_AddComm_Object = MibScalar
addComm = _AddComm_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 7),
    _AddComm_Type()
)
addComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addComm.setStatus("current")
_AddConnSpeed_Type = ConnectionSpeed
_AddConnSpeed_Object = MibScalar
addConnSpeed = _AddConnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 8),
    _AddConnSpeed_Type()
)
addConnSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addConnSpeed.setStatus("current")
_AddSrcTsBitmap_Type = Integer32
_AddSrcTsBitmap_Object = MibScalar
addSrcTsBitmap = _AddSrcTsBitmap_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 9),
    _AddSrcTsBitmap_Type()
)
addSrcTsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addSrcTsBitmap.setStatus("current")
_AddDestTsBitmap_Type = Integer32
_AddDestTsBitmap_Object = MibScalar
addDestTsBitmap = _AddDestTsBitmap_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 10),
    _AddDestTsBitmap_Type()
)
addDestTsBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addDestTsBitmap.setStatus("current")


class _AddBroadSrcId_Type(Integer32):
    """Custom type addBroadSrcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16224),
    )


_AddBroadSrcId_Type.__name__ = "Integer32"
_AddBroadSrcId_Object = MibScalar
addBroadSrcId = _AddBroadSrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 11),
    _AddBroadSrcId_Type()
)
addBroadSrcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addBroadSrcId.setStatus("current")
_AddTestMode_Type = TestAccess
_AddTestMode_Object = MibScalar
addTestMode = _AddTestMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 12),
    _AddTestMode_Type()
)
addTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addTestMode.setStatus("current")
_AddCmdStatus_Type = ConnCmdStatus
_AddCmdStatus_Object = MibScalar
addCmdStatus = _AddCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 13),
    _AddCmdStatus_Type()
)
addCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addCmdStatus.setStatus("current")
_AddSrcTrunkCProfile_Type = DnxTrunkProfSelection
_AddSrcTrunkCProfile_Object = MibScalar
addSrcTrunkCProfile = _AddSrcTrunkCProfile_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 14),
    _AddSrcTrunkCProfile_Type()
)
addSrcTrunkCProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addSrcTrunkCProfile.setStatus("current")
_AddDestTrunkCProfile_Type = DnxTrunkProfSelection
_AddDestTrunkCProfile_Object = MibScalar
addDestTrunkCProfile = _AddDestTrunkCProfile_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 5, 15),
    _AddDestTrunkCProfile_Type()
)
addDestTrunkCProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addDestTrunkCProfile.setStatus("current")
_TrunkCProfileTable_Object = MibTable
trunkCProfileTable = _TrunkCProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 6)
)
if mibBuilder.loadTexts:
    trunkCProfileTable.setStatus("current")
_TrunkCProfileEntry_Object = MibTableRow
trunkCProfileEntry = _TrunkCProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 6, 1)
)
trunkCProfileEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "trunkProfileID"),
)
if mibBuilder.loadTexts:
    trunkCProfileEntry.setStatus("current")


class _TrunkProfileID_Type(Integer32):
    """Custom type trunkProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TrunkProfileID_Type.__name__ = "Integer32"
_TrunkProfileID_Object = MibTableColumn
trunkProfileID = _TrunkProfileID_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 6, 1, 1),
    _TrunkProfileID_Type()
)
trunkProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkProfileID.setStatus("current")


class _TrunkSignalStart_Type(OctetString):
    """Custom type trunkSignalStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrunkSignalStart_Type.__name__ = "OctetString"
_TrunkSignalStart_Object = MibTableColumn
trunkSignalStart = _TrunkSignalStart_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 6, 1, 2),
    _TrunkSignalStart_Type()
)
trunkSignalStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkSignalStart.setStatus("current")


class _TrunkSignalEnd_Type(OctetString):
    """Custom type trunkSignalEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrunkSignalEnd_Type.__name__ = "OctetString"
_TrunkSignalEnd_Object = MibTableColumn
trunkSignalEnd = _TrunkSignalEnd_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 6, 1, 3),
    _TrunkSignalEnd_Type()
)
trunkSignalEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkSignalEnd.setStatus("current")


class _TrunkData_Type(OctetString):
    """Custom type trunkData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TrunkData_Type.__name__ = "OctetString"
_TrunkData_Object = MibTableColumn
trunkData = _TrunkData_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 6, 1, 4),
    _TrunkData_Type()
)
trunkData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkData.setStatus("current")


class _TrunkCmdStatus_Type(Integer32):
    """Custom type trunkCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              200,
              208,
              400,
              404,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-data-locked-by-another-user", 450),
          ("err-general-config-error", 400),
          ("err-general-trunk-error", 200),
          ("err-invalid-command", 208),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-trunk-value", 404),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_TrunkCmdStatus_Type.__name__ = "Integer32"
_TrunkCmdStatus_Object = MibTableColumn
trunkCmdStatus = _TrunkCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 8, 6, 1, 5),
    _TrunkCmdStatus_Type()
)
trunkCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkCmdStatus.setStatus("current")
_Utilities_ObjectIdentity = ObjectIdentity
utilities = _Utilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12)
)
_Database_ObjectIdentity = ObjectIdentity
database = _Database_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1)
)
_DbBackup_ObjectIdentity = ObjectIdentity
dbBackup = _DbBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1)
)
_DbAutoBackup_Type = DecisionType
_DbAutoBackup_Object = MibScalar
dbAutoBackup = _DbAutoBackup_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 1),
    _DbAutoBackup_Type()
)
dbAutoBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbAutoBackup.setStatus("current")


class _DbBackupOccurrence_Type(Integer32):
    """Custom type dbBackupOccurrence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("weekly", 0))
    )


_DbBackupOccurrence_Type.__name__ = "Integer32"
_DbBackupOccurrence_Object = MibScalar
dbBackupOccurrence = _DbBackupOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 2),
    _DbBackupOccurrence_Type()
)
dbBackupOccurrence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbBackupOccurrence.setStatus("current")


class _DbBackupDayOfWeek_Type(Integer32):
    """Custom type dbBackupDayOfWeek based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_DbBackupDayOfWeek_Type.__name__ = "Integer32"
_DbBackupDayOfWeek_Object = MibScalar
dbBackupDayOfWeek = _DbBackupDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 3),
    _DbBackupDayOfWeek_Type()
)
dbBackupDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbBackupDayOfWeek.setStatus("current")


class _DbBackupHour_Type(Integer32):
    """Custom type dbBackupHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DbBackupHour_Type.__name__ = "Integer32"
_DbBackupHour_Object = MibScalar
dbBackupHour = _DbBackupHour_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 4),
    _DbBackupHour_Type()
)
dbBackupHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbBackupHour.setStatus("current")


class _DbBackupMin_Type(Integer32):
    """Custom type dbBackupMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DbBackupMin_Type.__name__ = "Integer32"
_DbBackupMin_Object = MibScalar
dbBackupMin = _DbBackupMin_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 5),
    _DbBackupMin_Type()
)
dbBackupMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbBackupMin.setStatus("current")
_DbRemoteHostTable_Object = MibTable
dbRemoteHostTable = _DbRemoteHostTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 10)
)
if mibBuilder.loadTexts:
    dbRemoteHostTable.setStatus("current")
_DbRemoteHostTableEntry_Object = MibTableRow
dbRemoteHostTableEntry = _DbRemoteHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 10, 1)
)
dbRemoteHostTableEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "dbHostIndex"),
)
if mibBuilder.loadTexts:
    dbRemoteHostTableEntry.setStatus("current")


class _DbHostIndex_Type(Integer32):
    """Custom type dbHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DbHostIndex_Type.__name__ = "Integer32"
_DbHostIndex_Object = MibTableColumn
dbHostIndex = _DbHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 10, 1, 1),
    _DbHostIndex_Type()
)
dbHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbHostIndex.setStatus("current")
_DbHostIp_Type = IpAddress
_DbHostIp_Object = MibTableColumn
dbHostIp = _DbHostIp_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 10, 1, 2),
    _DbHostIp_Type()
)
dbHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbHostIp.setStatus("current")


class _DbHostDirectory_Type(DisplayString):
    """Custom type dbHostDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_DbHostDirectory_Type.__name__ = "DisplayString"
_DbHostDirectory_Object = MibTableColumn
dbHostDirectory = _DbHostDirectory_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 10, 1, 3),
    _DbHostDirectory_Type()
)
dbHostDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbHostDirectory.setStatus("current")


class _DbHostFilename_Type(DisplayString):
    """Custom type dbHostFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DbHostFilename_Type.__name__ = "DisplayString"
_DbHostFilename_Object = MibTableColumn
dbHostFilename = _DbHostFilename_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 10, 1, 4),
    _DbHostFilename_Type()
)
dbHostFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbHostFilename.setStatus("current")


class _DbHostCmdStatus_Type(Integer32):
    """Custom type dbHostCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              8,
              9,
              11,
              100,
              101,
              102,
              108,
              109,
              111,
              200,
              201,
              202,
              203,
              204,
              210,
              211,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-host", 2),
          ("clear-successful", 102),
          ("command-in-progress", 100),
          ("err-backup-file-creation-failed", 210),
          ("err-backup-file-transfer-failed", 211),
          ("err-data-locked-by-another-user", 450),
          ("err-general-host-config-error", 200),
          ("err-invalid-host-addr", 202),
          ("err-invalid-host-command", 201),
          ("err-invalid-host-dir", 204),
          ("err-invalid-host-name", 203),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("restore-successful", 111),
          ("restoreDB", 11),
          ("save-all-successful", 109),
          ("save-successful", 108),
          ("saveDB", 8),
          ("saveDBToAll", 9),
          ("update-host", 1),
          ("update-successful", 101))
    )


_DbHostCmdStatus_Type.__name__ = "Integer32"
_DbHostCmdStatus_Object = MibTableColumn
dbHostCmdStatus = _DbHostCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 1, 1, 10, 1, 5),
    _DbHostCmdStatus_Type()
)
dbHostCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbHostCmdStatus.setStatus("current")
_Devices_ObjectIdentity = ObjectIdentity
devices = _Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3)
)
_TrapSequence_Type = Counter32
_TrapSequence_Object = MibScalar
trapSequence = _TrapSequence_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 1),
    _TrapSequence_Type()
)
trapSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequence.setStatus("current")
_TrapResourceKey_Type = Integer32
_TrapResourceKey_Object = MibScalar
trapResourceKey = _TrapResourceKey_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 2),
    _TrapResourceKey_Type()
)
trapResourceKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapResourceKey.setStatus("current")
_TrapTime_Type = DisplayString
_TrapTime_Object = MibScalar
trapTime = _TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 3),
    _TrapTime_Type()
)
trapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapTime.setStatus("current")
_TrapResourceAddress_Type = DisplayString
_TrapResourceAddress_Object = MibScalar
trapResourceAddress = _TrapResourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 4),
    _TrapResourceAddress_Type()
)
trapResourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapResourceAddress.setStatus("current")
_TrapResourceType_Type = DnxResourceType
_TrapResourceType_Object = MibScalar
trapResourceType = _TrapResourceType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 5),
    _TrapResourceType_Type()
)
trapResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapResourceType.setStatus("current")


class _TrapType_Type(Integer32):
    """Custom type trapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              101,
              102,
              141,
              142,
              201,
              202,
              203,
              204,
              206,
              207,
              208,
              209,
              210,
              216,
              219,
              225,
              228,
              231,
              241,
              242,
              243,
              244,
              246,
              247,
              248,
              249,
              250,
              256,
              259,
              265,
              268,
              271,
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
              312,
              313,
              314,
              316,
              321,
              322,
              323,
              324,
              325,
              330,
              331,
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
              352,
              353,
              354,
              356,
              361,
              362,
              363,
              364,
              365,
              370,
              371,
              401,
              402,
              403,
              404,
              407,
              424,
              425,
              430,
              431,
              441,
              442,
              443,
              444,
              447,
              464,
              465,
              470,
              471,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              522,
              523,
              524,
              525,
              530,
              531,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              552,
              553,
              554,
              555,
              556,
              557,
              558,
              559,
              560,
              562,
              563,
              564,
              565,
              570,
              571,
              601,
              602,
              641,
              642,
              706,
              712,
              723,
              725,
              731,
              746,
              752,
              763,
              765,
              771,
              825,
              831,
              865,
              871,
              925,
              931,
              965,
              971,
              1001,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
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
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
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
              1102,
              1103,
              1106,
              1107,
              1108,
              1142,
              1143,
              1146,
              1147,
              1148,
              1201,
              1202,
              1203,
              1225,
              1231,
              1241,
              1242,
              1243,
              1265,
              1271,
              1301,
              1302,
              1303,
              1304,
              1305,
              1307,
              1308,
              1309,
              1310,
              1312,
              1313,
              1314,
              1316,
              1317,
              1318,
              1320,
              1321,
              1322,
              1323,
              1324,
              1325,
              1330,
              1331,
              1341,
              1342,
              1343,
              1344,
              1345,
              1347,
              1348,
              1349,
              1350,
              1352,
              1353,
              1354,
              1356,
              1357,
              1358,
              1360,
              1361,
              1362,
              1363,
              1364,
              1365,
              1370,
              1371,
              1403,
              1404,
              1405,
              1406,
              1407,
              1408,
              1409,
              1411,
              1412,
              1413,
              1414,
              1417,
              1418,
              1419,
              1420,
              1421,
              1422,
              1423,
              1424,
              1425,
              1430,
              1431,
              1443,
              1444,
              1445,
              1446,
              1447,
              1448,
              1449,
              1451,
              1452,
              1453,
              1454,
              1457,
              1458,
              1459,
              1460,
              1461,
              1462,
              1463,
              1464,
              1465,
              1470,
              1471,
              1531,
              1571,
              1606,
              1615,
              1616,
              1617,
              1618,
              1620,
              1621,
              1646,
              1655,
              1656,
              1657,
              1658,
              1660,
              1661,
              1701,
              1702,
              1705,
              1706,
              1707,
              1708,
              1709,
              1741,
              1742,
              1745,
              1746,
              1747,
              1748,
              1749,
              1801,
              1802,
              1803,
              1841,
              1842,
              1843,
              1901,
              1902,
              1925,
              1930,
              1931,
              1941,
              1942,
              1965,
              1970,
              1971,
              2001,
              2002,
              2041,
              2042,
              2201,
              2202,
              2203,
              2204,
              2205,
              2207,
              2208,
              2209,
              2210,
              2213,
              2216,
              2217,
              2218,
              2219,
              2220,
              2221,
              2222,
              2223,
              2224,
              2225,
              2230,
              2231,
              2241,
              2242,
              2243,
              2244,
              2245,
              2247,
              2248,
              2249,
              2250,
              2253,
              2256,
              2257,
              2258,
              2259,
              2260,
              2261,
              2262,
              2263,
              2264,
              2265,
              2270,
              2271,
              2301,
              2302,
              2303,
              2304,
              2305,
              2307,
              2308,
              2330,
              2341,
              2342,
              2343,
              2344,
              2345,
              2347,
              2348,
              2370,
              2401,
              2402,
              2403,
              2404,
              2405,
              2407,
              2408,
              2409,
              2413,
              2414,
              2415,
              2430,
              2441,
              2442,
              2443,
              2444,
              2445,
              2447,
              2448,
              2449,
              2453,
              2454,
              2455,
              2470,
              2501,
              2502,
              2503,
              2504,
              2505,
              2506,
              2507,
              2512,
              2513,
              2514,
              2515,
              2516,
              2517,
              2519,
              2520,
              2523,
              2525,
              2530,
              2531,
              2541,
              2542,
              2543,
              2544,
              2545,
              2546,
              2547,
              2552,
              2553,
              2554,
              2555,
              2556,
              2557,
              2559,
              2560,
              2563,
              2565,
              2570,
              2571,
              2601,
              2625,
              2641,
              2665,
              2701,
              2725,
              2741,
              2765,
              2801,
              2802,
              2803,
              2804,
              2805,
              2841,
              2842,
              2843,
              2844,
              2845,
              2901,
              2941,
              3001,
              3025,
              3041,
              3065,
              3108,
              3109,
              3110,
              3116,
              3119,
              3125,
              3148,
              3149,
              3150,
              3156,
              3159,
              3165)
        )
    )
    namedValues = NamedValues(
        *(("clear1uPowerSupplyCfgMismatch", 3165),
          ("clear1uPowerSupplyCircuitMissing", 3159),
          ("clear1uPowerSupplyDefective", 3149),
          ("clear1uPowerSupplyFanFailure", 3150),
          ("clear1uPowerSupplyOffline", 3148),
          ("clearAsyncFramingError", 2845),
          ("clearAsyncOverrunError", 2843),
          ("clearAsyncParityError", 2844),
          ("clearAsyncRxFifoError", 2841),
          ("clearAsyncTxFifoError", 2842),
          ("clearContactClosureCfgError", 2665),
          ("clearContactClosureInputAlarm", 2641),
          ("clearDevBusError", 250),
          ("clearDevCircuitCardMissing", 259),
          ("clearDevConfigError", 265),
          ("clearDevDataBaseNotInsync", 246),
          ("clearDevDefective", 249),
          ("clearDevFrameSyncNotPresent", 243),
          ("clearDevFreeRunError", 247),
          ("clearDevNoRearCard", 268),
          ("clearDevOffline", 248),
          ("clearDevStratum3ClkFailure", 256),
          ("clearDevSystemClockNotPresent", 244),
          ("clearDs0DpClockBPV", 2042),
          ("clearDs0DpClockLossOfSignal", 2041),
          ("clearDs0DpPortBPV", 1942),
          ("clearDs0DpPortConfigError", 1965),
          ("clearDs0DpPortLossOfSignal", 1941),
          ("clearE3ConfigError", 2565),
          ("clearE3FarEndBlockError", 2557),
          ("clearE3LIUCodingViolation", 2563),
          ("clearE3LIUOtherStatus", 2560),
          ("clearE3MbitsInError", 2559),
          ("clearE3NearEndLOF", 2545),
          ("clearE3NearEndLossOfSignal", 2546),
          ("clearE3NearEndSendLOF", 2542),
          ("clearE3NearEndSendingAIS", 2544),
          ("clearE3NearEndSeverErroredFrame", 2555),
          ("clearE3NearEndUnavailableSig", 2553),
          ("clearE3OtherLineStatus", 2552),
          ("clearE3RcvFarEndLOF", 2541),
          ("clearE3TxRxClockFailure", 2556),
          ("clearHsCarrierFailure", 444),
          ("clearHsClockEdgeError", 443),
          ("clearHsConfigError", 465),
          ("clearHsRcvFIFOError", 441),
          ("clearHsXmtFIFOError", 442),
          ("clearHt3ChangeInFrameAlignment", 1459),
          ("clearHt3ConfigError", 1465),
          ("clearHt3FarEndBlockError", 1457),
          ("clearHt3FarEndRcvFailure", 1449),
          ("clearHt3LIUAnalogLOS", 1461),
          ("clearHt3LIUCodingViolation", 1463),
          ("clearHt3LIUDigitalLOS", 1460),
          ("clearHt3LIUExcessZeros", 1462),
          ("clearHt3LIUPrbsError", 1464),
          ("clearHt3NearEndExcessZeros", 1453),
          ("clearHt3NearEndFERRError", 1452),
          ("clearHt3NearEndLCVError", 1451),
          ("clearHt3NearEndLOF", 1448),
          ("clearHt3NearEndLossOfSignal", 1446),
          ("clearHt3NearEndOOF", 1445),
          ("clearHt3NearEndSendingAIS", 1444),
          ("clearHt3PbitCbitParityError", 1458),
          ("clearNestCriticalAlarm", 1746),
          ("clearNestMajorAlarm", 1747),
          ("clearNestMinorAlarm", 1748),
          ("clearNestMismatch", 1741),
          ("clearNestMissing", 1742),
          ("clearNestOffline", 1745),
          ("clearNestSwMismatch", 1749),
          ("clearNodeCriticalAlarm", 1841),
          ("clearNodeMajorAlarm", 1842),
          ("clearNodeMinorAlarm", 1843),
          ("clearOcuConfigError", 765),
          ("clearOcuNearEndLOS", 746),
          ("clearOcuNearEndSeverErroredFrame", 763),
          ("clearOcuOtherLineStatus", 752),
          ("clearOpticalT1E1ConfigError", 2265),
          ("clearOpticalT1E1DetectedAIS", 2250),
          ("clearOpticalT1E1LossOfPointer", 2248),
          ("clearOpticalT1E1NearEndLOF", 2245),
          ("clearOpticalT1E1NearEndLOS", 2253),
          ("clearOpticalT1E1NearEndSEF", 2258),
          ("clearOpticalT1E1NearEndSendLOF", 2242),
          ("clearOpticalT1E1NearEndSendingAIS", 2244),
          ("clearOpticalT1E1OutOfFrame", 2249),
          ("clearOpticalT1E1RcvFarEndYellow", 2257),
          ("clearOpticalT1E1RedAlarm", 2241),
          ("clearOpticalT1E1Tug2AIS", 2262),
          ("clearOpticalT1E1Tug2LOP", 2259),
          ("clearOpticalT1E1Tug2PSLM", 2263),
          ("clearOpticalT1E1Tug2PSLU", 2264),
          ("clearOpticalT1E1Tug2RDI", 2260),
          ("clearOpticalT1E1Tug2RFI", 2261),
          ("clearPayloadPathAIS", 2344),
          ("clearPayloadPathLOP", 2343),
          ("clearPayloadPathRDI", 2345),
          ("clearPowerSupplyNotPresent", 641),
          ("clearPowerSupplyProblem", 642),
          ("clearPsxDualBroadbandNotSupported", 1048),
          ("clearPsxFan01NotOk", 1045),
          ("clearPsxFan02NotOk", 1046),
          ("clearPsxFan03NotOk", 1047),
          ("clearPsxLineCardCableMissing", 1143),
          ("clearPsxLineCardMismatch", 1147),
          ("clearPsxLineCardMissing", 1146),
          ("clearPsxLineCardRelayMalfunction", 1148),
          ("clearPsxLineCardRelaySwitchToSpare", 1142),
          ("clearPsxPowerSupplyANotOk", 1043),
          ("clearPsxPowerSupplyBNotOk", 1044),
          ("clearRtrConfigError", 1265),
          ("clearRtrUserAlarm1", 1241),
          ("clearRtrUserAlarm2", 1242),
          ("clearRtrUserAlarm3", 1243),
          ("clearSlotMismatch", 141),
          ("clearSlotMissing", 142),
          ("clearSts1ConfigError", 1365),
          ("clearSts1LIUAnalogLOS", 1361),
          ("clearSts1LIUCodingViolation", 1363),
          ("clearSts1LIUDigitalLOS", 1360),
          ("clearSts1LIUExcessZeros", 1362),
          ("clearSts1LIUPrbsError", 1364),
          ("clearSts1NearEndAIS", 1350),
          ("clearSts1NearEndLOF", 1345),
          ("clearSts1NearEndLOMF", 1357),
          ("clearSts1NearEndLOP", 1348),
          ("clearSts1NearEndOOF", 1349),
          ("clearSts1NearEndSendLOF", 1342),
          ("clearSts1NearEndSendingAIS", 1344),
          ("clearSts1NearEndTraceError", 1358),
          ("clearSts1NearEndUnavailableSig", 1353),
          ("clearSts1OtherLineStatus", 1352),
          ("clearSts1RcvFarEndLOF", 1341),
          ("clearSts1TxRxClockFailure", 1356),
          ("clearT1E1ChangeFrameAlignment", 364),
          ("clearT1E1ConfigError", 365),
          ("clearT1E1FarEndSendingTs16LOMF", 349),
          ("clearT1E1NearEndLOF", 345),
          ("clearT1E1NearEndLossOfSignal", 346),
          ("clearT1E1NearEndRxSlip", 362),
          ("clearT1E1NearEndSendLOF", 342),
          ("clearT1E1NearEndSendingAIS", 344),
          ("clearT1E1NearEndSendingTs16LOMF", 350),
          ("clearT1E1NearEndSeverErroredFrame", 363),
          ("clearT1E1NearEndTxSlip", 361),
          ("clearT1E1NearEndUnavailableSig", 353),
          ("clearT1E1OtherLineStatus", 352),
          ("clearT1E1RcvFarEndLOF", 341),
          ("clearT1E1Ts16AIS", 348),
          ("clearT3ConfigError", 565),
          ("clearT3FarEndBlockError", 557),
          ("clearT3FarEndSendingAIS", 543),
          ("clearT3LIUCodingViolation", 563),
          ("clearT3LIUExcessZeros", 562),
          ("clearT3LIUOtherStatus", 560),
          ("clearT3LIUPrbsError", 564),
          ("clearT3MbitsInError", 559),
          ("clearT3NearEndLOF", 545),
          ("clearT3NearEndLossOfSignal", 546),
          ("clearT3NearEndSendLOF", 542),
          ("clearT3NearEndSendingAIS", 544),
          ("clearT3NearEndSeverErroredFrame", 555),
          ("clearT3NearEndUnavailableSig", 553),
          ("clearT3OtherLineStatus", 552),
          ("clearT3PbitCbitParityError", 558),
          ("clearT3RcvFarEndLOF", 541),
          ("clearT3TxRxClockFailure", 556),
          ("clearTamConfigError", 865),
          ("clearTempSensorOutOfRange", 2941),
          ("clearTransOverheadAIS", 2441),
          ("clearTransOverheadLOF", 2444),
          ("clearTransOverheadLOS", 2445),
          ("clearTransOverheadLaserOffDetect", 2455),
          ("clearTransOverheadOOF", 2443),
          ("clearTransOverheadRDI", 2442),
          ("clearTransOverheadSdDetect", 2454),
          ("clearTransOverheadSfDetect", 2453),
          ("clearVWanCfgError", 3065),
          ("clearVWanError", 3041),
          ("clearVoiceConfigError", 965),
          ("clearVoltMeasureAlarm", 2741),
          ("clearVoltMeasureCfgError", 2765),
          ("clearVtNearEndAIS", 2342),
          ("clearVtNearEndLOP", 2341),
          ("clearXlinkBertError", 1657),
          ("clearXlinkCableMismatch", 1646),
          ("clearXlinkClockError", 1658),
          ("clearXlinkCrcError", 1661),
          ("clearXlinkFramerError", 1656),
          ("clearXlinkInUseError", 1660),
          ("clearXlinkSerializerError", 1655),
          ("evnt1uPowerSupplyFanOff", 3156),
          ("evnt1uPowerSupplyFanOn", 3116),
          ("evntDevColdStart", 1),
          ("evntDevInService", 271),
          ("evntDevNotOnline", 241),
          ("evntDevNotStandby", 242),
          ("evntDevOnline", 201),
          ("evntDevOutOfService", 231),
          ("evntDevStandby", 202),
          ("evntDevWarmStart", 2),
          ("evntDs0DpPortInService", 1971),
          ("evntDs0DpPortInTest", 1930),
          ("evntDs0DpPortOutOfService", 1931),
          ("evntDs0DpPortTestOff", 1970),
          ("evntE1NationalSa4TxRxDiff", 356),
          ("evntE1NationalSa4TxRxSame", 316),
          ("evntE3CarrierEquipInService", 2554),
          ("evntE3CarrierEquipOutOfService", 2514),
          ("evntE3InService", 2571),
          ("evntE3InTest", 2530),
          ("evntE3NearEndLoopOff", 2547),
          ("evntE3NearEndLooped", 2507),
          ("evntE3OutOfService", 2531),
          ("evntE3RcvingAIS", 2503),
          ("evntE3StoppedRcvingAIS", 2543),
          ("evntE3TestOff", 2570),
          ("evntGr303InService", 1571),
          ("evntGr303OutOfService", 1531),
          ("evntHsBtsAssigned", 464),
          ("evntHsInService", 471),
          ("evntHsInTest", 430),
          ("evntHsNearEndLoopOff", 447),
          ("evntHsNearEndLooped", 407),
          ("evntHsNoBtsAssigned", 424),
          ("evntHsOutOfService", 431),
          ("evntHsTestOff", 470),
          ("evntHt3CarrierEquipInService", 1454),
          ("evntHt3CarrierEquipOutOfService", 1414),
          ("evntHt3InService", 1471),
          ("evntHt3InTest", 1430),
          ("evntHt3NearEndLoopOff", 1447),
          ("evntHt3NearEndLooped", 1407),
          ("evntHt3OutOfService", 1431),
          ("evntHt3RcvingAIS", 1403),
          ("evntHt3StoppedRcvingAIS", 1443),
          ("evntHt3TestOff", 1470),
          ("evntOcuInService", 771),
          ("evntOcuOutOfService", 731),
          ("evntOpticalE1NationalSa4TxRxDiff", 2256),
          ("evntOpticalE1NationalSa4TxRxSame", 2216),
          ("evntOpticalT1E1InService", 2271),
          ("evntOpticalT1E1InTest", 2230),
          ("evntOpticalT1E1NearEndLoopOff", 2247),
          ("evntOpticalT1E1NearEndLooped", 2207),
          ("evntOpticalT1E1OutOfService", 2231),
          ("evntOpticalT1E1RcvingAIS", 2203),
          ("evntOpticalT1E1StoppedRcvingAIS", 2243),
          ("evntOpticalT1E1TestOff", 2270),
          ("evntPayloadInTest", 2330),
          ("evntPayloadNearEndLineLoopOff", 2347),
          ("evntPayloadNearEndLineLooped", 2307),
          ("evntPayloadNearEndLocalLoopOff", 2348),
          ("evntPayloadNearEndLocalLooped", 2308),
          ("evntPayloadTestOff", 2370),
          ("evntPsxDevOnline", 1001),
          ("evntPsxLineCard01Missing", 1014),
          ("evntPsxLineCard01Present", 1054),
          ("evntPsxLineCard02Missing", 1015),
          ("evntPsxLineCard02Present", 1055),
          ("evntPsxLineCard03Missing", 1016),
          ("evntPsxLineCard03Present", 1056),
          ("evntPsxLineCard04Missing", 1017),
          ("evntPsxLineCard04Present", 1057),
          ("evntPsxLineCard05Missing", 1018),
          ("evntPsxLineCard05Present", 1058),
          ("evntPsxLineCard06Missing", 1019),
          ("evntPsxLineCard06Present", 1059),
          ("evntPsxLineCard07Missing", 1020),
          ("evntPsxLineCard07Present", 1060),
          ("evntPsxLineCard08Missing", 1021),
          ("evntPsxLineCard08Present", 1061),
          ("evntPsxLineCard09Missing", 1022),
          ("evntPsxLineCard09Present", 1062),
          ("evntPsxLineCard10Missing", 1023),
          ("evntPsxLineCard10Present", 1063),
          ("evntPsxLineCard11Missing", 1024),
          ("evntPsxLineCard11Present", 1064),
          ("evntPsxNewControllerRev", 1009),
          ("evntRtrInService", 1271),
          ("evntRtrOutOfService", 1231),
          ("evntSts1CarrierEquipInService", 1354),
          ("evntSts1CarrierEquipOutOfService", 1314),
          ("evntSts1InService", 1371),
          ("evntSts1InTest", 1330),
          ("evntSts1NearEndLoopOff", 1347),
          ("evntSts1NearEndLooped", 1307),
          ("evntSts1OutOfService", 1331),
          ("evntSts1RcvingAIS", 1303),
          ("evntSts1StoppedRcvingAIS", 1343),
          ("evntSts1TestOff", 1370),
          ("evntT1E1CarrierEquipInService", 354),
          ("evntT1E1CarrierEquipOutOfService", 314),
          ("evntT1E1InService", 371),
          ("evntT1E1InTest", 330),
          ("evntT1E1NearEndLoopOff", 347),
          ("evntT1E1NearEndLooped", 307),
          ("evntT1E1OutOfService", 331),
          ("evntT1E1RcvingAIS", 303),
          ("evntT1E1StoppedRcvingAIS", 343),
          ("evntT1E1TestOff", 370),
          ("evntT3CarrierEquipInService", 554),
          ("evntT3CarrierEquipOutOfService", 514),
          ("evntT3InService", 571),
          ("evntT3InTest", 530),
          ("evntT3NearEndLoopOff", 547),
          ("evntT3NearEndLooped", 507),
          ("evntT3OutOfService", 531),
          ("evntT3TestOff", 570),
          ("evntTamInService", 871),
          ("evntTamOutOfService", 831),
          ("evntTransOverheadInTest", 2430),
          ("evntTransOverheadNearEndLocalLoopOff", 2449),
          ("evntTransOverheadNearEndLocalLooped", 2409),
          ("evntTransOverheadNearEndPathLineLoopOff", 2448),
          ("evntTransOverheadNearEndPathLineLooped", 2408),
          ("evntTransOverheadNearEndSysLineLoopOff", 2447),
          ("evntTransOverheadNearEndSysLineLooped", 2407),
          ("evntTransOverheadTestOff", 2470),
          ("evntVoiceInService", 971),
          ("evntVoiceOutOfService", 931),
          ("set1uPowerSupplyCfgMismatch", 3125),
          ("set1uPowerSupplyCircuitMissing", 3119),
          ("set1uPowerSupplyDefective", 3109),
          ("set1uPowerSupplyFanFailure", 3110),
          ("set1uPowerSupplyOffline", 3108),
          ("setAsyncFramingError", 2805),
          ("setAsyncOverrunError", 2803),
          ("setAsyncParityError", 2804),
          ("setAsyncRxFifoError", 2801),
          ("setAsyncTxFifoError", 2802),
          ("setContactClosureCfgError", 2625),
          ("setContactClosureInputAlarm", 2601),
          ("setDevBusError", 210),
          ("setDevCircuitCardMissing", 219),
          ("setDevConfigError", 225),
          ("setDevDataBaseNotInsync", 206),
          ("setDevDefective", 209),
          ("setDevFrameSyncNotPresent", 203),
          ("setDevFreeRunError", 207),
          ("setDevNoRearCard", 228),
          ("setDevOffline", 208),
          ("setDevStratum3ClkFailure", 216),
          ("setDevSystemClockNotPresent", 204),
          ("setDs0DpClockBPV", 2002),
          ("setDs0DpClockLossOfSignal", 2001),
          ("setDs0DpPortBPV", 1902),
          ("setDs0DpPortConfigError", 1925),
          ("setDs0DpPortLossOfSignal", 1901),
          ("setE3ConfigError", 2525),
          ("setE3FarEndBlockError", 2517),
          ("setE3LIUCodingViolation", 2523),
          ("setE3LIUOtherStatus", 2520),
          ("setE3MbitsInError", 2519),
          ("setE3NearEndLOF", 2505),
          ("setE3NearEndLossOfSignal", 2506),
          ("setE3NearEndSendLOF", 2502),
          ("setE3NearEndSendingAIS", 2504),
          ("setE3NearEndSeverErroredFrame", 2515),
          ("setE3NearEndUnavailableSig", 2513),
          ("setE3OtherLineStatus", 2512),
          ("setE3RcvFarEndLOF", 2501),
          ("setE3TxRxClockFailure", 2516),
          ("setHsCarrierFailure", 404),
          ("setHsClockEdgeError", 403),
          ("setHsConfigError", 425),
          ("setHsRcvFIFOError", 401),
          ("setHsXmtFIFOError", 402),
          ("setHt3ChangeInFrameAlignment", 1419),
          ("setHt3ConfigError", 1425),
          ("setHt3FarEndBlockError", 1417),
          ("setHt3FarEndRcvFailure", 1409),
          ("setHt3LIUAnalogLOS", 1421),
          ("setHt3LIUCodingViolation", 1423),
          ("setHt3LIUDigitalLOS", 1420),
          ("setHt3LIUExcessZeros", 1422),
          ("setHt3LIUPrbsError", 1424),
          ("setHt3NearEndExcessZeros", 1413),
          ("setHt3NearEndFERRError", 1412),
          ("setHt3NearEndLCVError", 1411),
          ("setHt3NearEndLOF", 1408),
          ("setHt3NearEndLossOfSignal", 1406),
          ("setHt3NearEndOOF", 1405),
          ("setHt3NearEndSendingAIS", 1404),
          ("setHt3PbitCbitParityError", 1418),
          ("setNestCriticalAlarm", 1706),
          ("setNestMajorAlarm", 1707),
          ("setNestMinorAlarm", 1708),
          ("setNestMismatch", 1701),
          ("setNestMissing", 1702),
          ("setNestOffline", 1705),
          ("setNestSwMismatch", 1709),
          ("setNodeCriticalAlarm", 1801),
          ("setNodeMajorAlarm", 1802),
          ("setNodeMinorAlarm", 1803),
          ("setOcuConfigError", 725),
          ("setOcuNearEndLOS", 706),
          ("setOcuNearEndSeverErroredFrame", 723),
          ("setOcuOtherLineStatus", 712),
          ("setOpticalT1E1ConfigError", 2225),
          ("setOpticalT1E1DetectedAIS", 2210),
          ("setOpticalT1E1LossOfPointer", 2208),
          ("setOpticalT1E1NearEndLOF", 2205),
          ("setOpticalT1E1NearEndLOS", 2213),
          ("setOpticalT1E1NearEndSEF", 2218),
          ("setOpticalT1E1NearEndSendLOF", 2202),
          ("setOpticalT1E1NearEndSendingAIS", 2204),
          ("setOpticalT1E1OutOfFrame", 2209),
          ("setOpticalT1E1RcvFarEndYellow", 2217),
          ("setOpticalT1E1RedAlarm", 2201),
          ("setOpticalT1E1Tug2AIS", 2222),
          ("setOpticalT1E1Tug2LOP", 2219),
          ("setOpticalT1E1Tug2PSLM", 2223),
          ("setOpticalT1E1Tug2PSLU", 2224),
          ("setOpticalT1E1Tug2RDI", 2220),
          ("setOpticalT1E1Tug2RFI", 2221),
          ("setPayloadPathAIS", 2304),
          ("setPayloadPathLOP", 2303),
          ("setPayloadPathRDI", 2305),
          ("setPowerSupplyNotPresent", 601),
          ("setPowerSupplyProblem", 602),
          ("setPsxDualBroadbandNotSupported", 1008),
          ("setPsxFan01NotOk", 1005),
          ("setPsxFan02NotOk", 1006),
          ("setPsxFan03NotOk", 1007),
          ("setPsxLineCardCableMissing", 1103),
          ("setPsxLineCardMismatch", 1107),
          ("setPsxLineCardMissing", 1106),
          ("setPsxLineCardRelayMalfunction", 1108),
          ("setPsxLineCardRelaySwitchToSpare", 1102),
          ("setPsxPowerSupplyANotOk", 1003),
          ("setPsxPowerSupplyBNotOk", 1004),
          ("setRtrConfigError", 1225),
          ("setRtrUserAlarm1", 1201),
          ("setRtrUserAlarm2", 1202),
          ("setRtrUserAlarm3", 1203),
          ("setSlotMismatch", 101),
          ("setSlotMissing", 102),
          ("setSts1ConfigError", 1325),
          ("setSts1LIUAnalogLOS", 1321),
          ("setSts1LIUCodingViolation", 1323),
          ("setSts1LIUDigitalLOS", 1320),
          ("setSts1LIUExcessZeros", 1322),
          ("setSts1LIUPrbsError", 1324),
          ("setSts1NearEndAIS", 1310),
          ("setSts1NearEndLOF", 1305),
          ("setSts1NearEndLOMF", 1317),
          ("setSts1NearEndLOP", 1308),
          ("setSts1NearEndOOF", 1309),
          ("setSts1NearEndSendLOF", 1302),
          ("setSts1NearEndSendingAIS", 1304),
          ("setSts1NearEndTraceError", 1318),
          ("setSts1NearEndUnavailableSig", 1313),
          ("setSts1OtherLineStatus", 1312),
          ("setSts1RcvFarEndLOF", 1301),
          ("setSts1TxRxClockFailure", 1316),
          ("setT1E1ChangeFrameAlignment", 324),
          ("setT1E1ConfigError", 325),
          ("setT1E1FarEndSendingTs16LOMF", 309),
          ("setT1E1NearEndLOF", 305),
          ("setT1E1NearEndLossOfSignal", 306),
          ("setT1E1NearEndRxSlip", 322),
          ("setT1E1NearEndSendLOF", 302),
          ("setT1E1NearEndSendingAIS", 304),
          ("setT1E1NearEndSendingTs16LOMF", 310),
          ("setT1E1NearEndSeverErroredFrame", 323),
          ("setT1E1NearEndTxSlip", 321),
          ("setT1E1NearEndUnavailableSig", 313),
          ("setT1E1OtherLineStatus", 312),
          ("setT1E1RcvFarEndLOF", 301),
          ("setT1E1Ts16AIS", 308),
          ("setT3ConfigError", 525),
          ("setT3FarEndBlockError", 517),
          ("setT3FarEndSendingAIS", 503),
          ("setT3LIUCodingViolation", 523),
          ("setT3LIUExcessZeros", 522),
          ("setT3LIUOtherStatus", 520),
          ("setT3LIUPrbsError", 524),
          ("setT3MbitsInError", 519),
          ("setT3NearEndLOF", 505),
          ("setT3NearEndLossOfSignal", 506),
          ("setT3NearEndSendLOF", 502),
          ("setT3NearEndSendingAIS", 504),
          ("setT3NearEndSeverErroredFrame", 515),
          ("setT3NearEndUnavailableSig", 513),
          ("setT3OtherLineStatus", 512),
          ("setT3PbitCbitParityError", 518),
          ("setT3RcvFarEndLOF", 501),
          ("setT3TxRxClockFailure", 516),
          ("setTamConfigError", 825),
          ("setTempSensorOutOfRange", 2901),
          ("setTransOverheadAIS", 2401),
          ("setTransOverheadLOF", 2404),
          ("setTransOverheadLOS", 2405),
          ("setTransOverheadLaserOffDetect", 2415),
          ("setTransOverheadOOF", 2403),
          ("setTransOverheadRDI", 2402),
          ("setTransOverheadSdDetect", 2414),
          ("setTransOverheadSfDetect", 2413),
          ("setVWanCfgError", 3025),
          ("setVWanError", 3001),
          ("setVoiceConfigError", 925),
          ("setVoltMeasureAlarm", 2701),
          ("setVoltMeasureCfgError", 2725),
          ("setVtNearEndAIS", 2302),
          ("setVtNearEndLOP", 2301),
          ("setXlinkBertError", 1617),
          ("setXlinkCableMismatch", 1606),
          ("setXlinkClockError", 1618),
          ("setXlinkCrcError", 1621),
          ("setXlinkFramerError", 1616),
          ("setXlinkInUseError", 1620),
          ("setXlinkSerializerError", 1615))
    )


_TrapType_Type.__name__ = "Integer32"
_TrapType_Object = MibScalar
trapType = _TrapType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 6),
    _TrapType_Type()
)
trapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapType.setStatus("current")
_TrapState_Type = Integer32
_TrapState_Object = MibScalar
trapState = _TrapState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 7),
    _TrapState_Type()
)
trapState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapState.setStatus("current")
_TrapSeverity_Type = AlarmSeverity
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 8),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_TrapSysEvent_Type = DisplayString
_TrapSysEvent_Object = MibScalar
trapSysEvent = _TrapSysEvent_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 9),
    _TrapSysEvent_Type()
)
trapSysEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSysEvent.setStatus("current")
_TrapCfg_ObjectIdentity = ObjectIdentity
trapCfg = _TrapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20)
)
_TrapDestinationTable_Object = MibTable
trapDestinationTable = _TrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1)
)
if mibBuilder.loadTexts:
    trapDestinationTable.setStatus("current")
_TrapDestinationEntry_Object = MibTableRow
trapDestinationEntry = _TrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1, 1)
)
trapDestinationEntry.setIndexNames(
    (0, "ERI-DNX-SMC-MIB", "trapDestAddr"),
)
if mibBuilder.loadTexts:
    trapDestinationEntry.setStatus("current")
_TrapDestAddr_Type = IpAddress
_TrapDestAddr_Object = MibTableColumn
trapDestAddr = _TrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1, 1, 1),
    _TrapDestAddr_Type()
)
trapDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestAddr.setStatus("current")


class _TrapDestName_Type(DisplayString):
    """Custom type trapDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_TrapDestName_Type.__name__ = "DisplayString"
_TrapDestName_Object = MibTableColumn
trapDestName = _TrapDestName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1, 1, 2),
    _TrapDestName_Type()
)
trapDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestName.setStatus("current")


class _TrapDestCmdStatus_Type(Integer32):
    """Custom type trapDestCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              101,
              102,
              103,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("create-successful", 103),
          ("create-trap-dest", 3),
          ("delete-successful", 102),
          ("delete-trap-dest", 2),
          ("err-data-locked-by-another-user", 450),
          ("err-general-trap-dest-cfg-error", 200),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-trap-dest-addr", 201),
          ("err-invalid-trap-dest-cmd", 202),
          ("err-invalid-trap-dest-name", 203),
          ("err-invalid-trap-dest-pdu", 204),
          ("err-invalid-trap-dest-retry", 205),
          ("err-invalid-trap-dest-tmout", 206),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update-successful", 101),
          ("update-trap-dest", 1))
    )


_TrapDestCmdStatus_Type.__name__ = "Integer32"
_TrapDestCmdStatus_Object = MibTableColumn
trapDestCmdStatus = _TrapDestCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1, 1, 3),
    _TrapDestCmdStatus_Type()
)
trapDestCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestCmdStatus.setStatus("current")


class _TrapDestPduType_Type(Integer32):
    """Custom type trapDestPduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inform", 2),
          ("v1Trap", 0),
          ("v2Trap", 1))
    )


_TrapDestPduType_Type.__name__ = "Integer32"
_TrapDestPduType_Object = MibTableColumn
trapDestPduType = _TrapDestPduType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1, 1, 4),
    _TrapDestPduType_Type()
)
trapDestPduType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestPduType.setStatus("current")


class _TrapDestMaxRetry_Type(Integer32):
    """Custom type trapDestMaxRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TrapDestMaxRetry_Type.__name__ = "Integer32"
_TrapDestMaxRetry_Object = MibTableColumn
trapDestMaxRetry = _TrapDestMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1, 1, 5),
    _TrapDestMaxRetry_Type()
)
trapDestMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestMaxRetry.setStatus("current")


class _TrapDestTimeout_Type(Integer32):
    """Custom type trapDestTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              20)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("secs-10", 10),
          ("secs-15", 15),
          ("secs-20", 20),
          ("secs-5", 5))
    )


_TrapDestTimeout_Type.__name__ = "Integer32"
_TrapDestTimeout_Object = MibTableColumn
trapDestTimeout = _TrapDestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 3, 20, 1, 1, 6),
    _TrapDestTimeout_Type()
)
trapDestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestTimeout.setStatus("current")

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 0, 1)
)
alarmTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapResourceKey"),
        ("ERI-DNX-SMC-MIB", "trapTime"),
        ("ERI-DNX-SMC-MIB", "trapResourceAddress"),
        ("ERI-DNX-SMC-MIB", "trapResourceType"),
        ("ERI-DNX-SMC-MIB", "trapType"),
        ("ERI-DNX-SMC-MIB", "trapState"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        "current"
    )

deleteResourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 0, 2)
)
deleteResourceTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "resourceKey"),
        ("ERI-DNX-SMC-MIB", "trapSequence"))
)
if mibBuilder.loadTexts:
    deleteResourceTrap.setStatus(
        "current"
    )

connectionEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 3)
)
connectionEventTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "sysMapID"),
        ("ERI-DNX-SMC-MIB", "sysConnID"),
        ("ERI-DNX-SMC-MIB", "sysCmdStatus"))
)
if mibBuilder.loadTexts:
    connectionEventTrap.setStatus(
        "current"
    )

connMapMgrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 4)
)
connMapMgrTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "connMapID"),
        ("ERI-DNX-SMC-MIB", "connMapCmdStatus"))
)
if mibBuilder.loadTexts:
    connMapMgrTrap.setStatus(
        "current"
    )

connMapCopyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 6)
)
connMapCopyTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "lastMapCopied"),
        ("ERI-DNX-SMC-MIB", "connMapID"))
)
if mibBuilder.loadTexts:
    connMapCopyTrap.setStatus(
        "current"
    )

bulkConnPurgeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 7)
)
bulkConnPurgeTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "resourceKey"),
        ("ERI-DNX-SMC-MIB", "connMapID"),
        ("ERI-DNX-SMC-MIB", "connMapCounts"))
)
if mibBuilder.loadTexts:
    bulkConnPurgeTrap.setStatus(
        "current"
    )

clockSrcChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 10)
)
clockSrcChgTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "clockSrcActive"),
        ("ERI-DNX-SMC-MIB", "primaryClockSrc"),
        ("ERI-DNX-SMC-MIB", "secondaryClockSrc"),
        ("ERI-DNX-SMC-MIB", "tertiaryClockSrc"),
        ("ERI-DNX-SMC-MIB", "clockSrcCmdStatus"))
)
if mibBuilder.loadTexts:
    clockSrcChgTrap.setStatus(
        "current"
    )

trunkCondProfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 13)
)
trunkCondProfTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trunkProfileID"),
        ("ERI-DNX-SMC-MIB", "trunkCmdStatus"))
)
if mibBuilder.loadTexts:
    trunkCondProfTrap.setStatus(
        "current"
    )

systemEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 14)
)
systemEventTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapSysEvent"),
        ("ERI-DNX-SMC-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    systemEventTrap.setStatus(
        "current"
    )

trapDestCfgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 15)
)
trapDestCfgTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "trapDestAddr"),
        ("ERI-DNX-SMC-MIB", "trapDestCmdStatus"))
)
if mibBuilder.loadTexts:
    trapDestCfgTrap.setStatus(
        "current"
    )

featureKeyCfgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 16)
)
featureKeyCfgTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-SMC-MIB", "featureKeyName"),
        ("ERI-DNX-SMC-MIB", "featureKeyState"),
        ("ERI-DNX-SMC-MIB", "featureKeyCmdStatus"))
)
if mibBuilder.loadTexts:
    featureKeyCfgTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-SMC-MIB",
    **{"DnxResourceType": DnxResourceType,
       "AlarmSeverity": AlarmSeverity,
       "DecisionType": DecisionType,
       "FunctionSwitch": FunctionSwitch,
       "CurrentDevStatus": CurrentDevStatus,
       "PortStatus": PortStatus,
       "DataSwitch": DataSwitch,
       "TimeSlotAddress": TimeSlotAddress,
       "LinkPortAddress": LinkPortAddress,
       "ClockSrcAddress": ClockSrcAddress,
       "NestSlotAddress": NestSlotAddress,
       "UnsignedInt": UnsignedInt,
       "ConnectionType": ConnectionType,
       "CommunicationsType": CommunicationsType,
       "ConnectionState1": ConnectionState1,
       "ConnectionState2": ConnectionState2,
       "MapNumber": MapNumber,
       "TestAccess": TestAccess,
       "ConnectionSpeed": ConnectionSpeed,
       "ConnCmdStatus": ConnCmdStatus,
       "LinkCmdStatus": LinkCmdStatus,
       "OneByteField": OneByteField,
       "DnxTsPortType": DnxTsPortType,
       "DnxTrunkProfSelection": DnxTrunkProfSelection,
       "eriTrapEnterprise": eriTrapEnterprise,
       "alarmTrap": alarmTrap,
       "deleteResourceTrap": deleteResourceTrap,
       "dnx": dnx,
       "dnxTrapEnterprise": dnxTrapEnterprise,
       "connectionEventTrap": connectionEventTrap,
       "connMapMgrTrap": connMapMgrTrap,
       "connMapCopyTrap": connMapCopyTrap,
       "bulkConnPurgeTrap": bulkConnPurgeTrap,
       "clockSrcChgTrap": clockSrcChgTrap,
       "trunkCondProfTrap": trunkCondProfTrap,
       "systemEventTrap": systemEventTrap,
       "trapDestCfgTrap": trapDestCfgTrap,
       "featureKeyCfgTrap": featureKeyCfgTrap,
       "sysMgr": sysMgr,
       "resourceTable": resourceTable,
       "resourceEntry": resourceEntry,
       "resourceKey": resourceKey,
       "resourceAddr": resourceAddr,
       "resourceType": resourceType,
       "resourceState": resourceState,
       "resourceCriticalMask": resourceCriticalMask,
       "resourceMajorMask": resourceMajorMask,
       "resourceMinorMask": resourceMinorMask,
       "resourceInfoMask": resourceInfoMask,
       "resourceNominalMask": resourceNominalMask,
       "resourceTrapMask": resourceTrapMask,
       "resourceAlarmTable": resourceAlarmTable,
       "resourceAlarmEntry": resourceAlarmEntry,
       "resourceAlarmKey": resourceAlarmKey,
       "resourceAlarmAddr": resourceAlarmAddr,
       "resourceAlarmType": resourceAlarmType,
       "resourceAlarmState": resourceAlarmState,
       "resourceAlarmCriticalMask": resourceAlarmCriticalMask,
       "resourceAlarmMajorMask": resourceAlarmMajorMask,
       "resourceAlarmMinorMask": resourceAlarmMinorMask,
       "resourceAlarmInfoMask": resourceAlarmInfoMask,
       "resourceAlarmNominalMask": resourceAlarmNominalMask,
       "resourceAlarmTrapMask": resourceAlarmTrapMask,
       "sysProfile": sysProfile,
       "unitName": unitName,
       "unitType": unitType,
       "activeSMC": activeSMC,
       "systemRelease": systemRelease,
       "releaseDate": releaseDate,
       "flashChksum": flashChksum,
       "xilinxType": xilinxType,
       "xilinxVersion": xilinxVersion,
       "rearModem": rearModem,
       "mibProfile": mibProfile,
       "systemMgrType": systemMgrType,
       "sysAlarmCutOff": sysAlarmCutOff,
       "sysMacAddress": sysMacAddress,
       "sysSa4RxTxTrap": sysSa4RxTxTrap,
       "sysCustomerId": sysCustomerId,
       "sysMgrOnlineTime": sysMgrOnlineTime,
       "featureKeys": featureKeys,
       "dnxFeatureKeyTable": dnxFeatureKeyTable,
       "dnxFeatureKeyEntry": dnxFeatureKeyEntry,
       "featureKeyId": featureKeyId,
       "featureKeyName": featureKeyName,
       "featureKeyState": featureKeyState,
       "featureKeyCmdStatus": featureKeyCmdStatus,
       "enterNewFeatureKey": enterNewFeatureKey,
       "newKeyCode": newKeyCode,
       "newKeyCodeCmdStatus": newKeyCodeCmdStatus,
       "sysClock": sysClock,
       "sysDateTime": sysDateTime,
       "sysMonth": sysMonth,
       "sysDay": sysDay,
       "sysYear": sysYear,
       "sysHour": sysHour,
       "sysMin": sysMin,
       "sysSec": sysSec,
       "sysWeekday": sysWeekday,
       "sysTimeCmdStatus": sysTimeCmdStatus,
       "clockSrcConfig": clockSrcConfig,
       "clockSrcActive": clockSrcActive,
       "primaryClockSrc": primaryClockSrc,
       "secondaryClockSrc": secondaryClockSrc,
       "tertiaryClockSrc": tertiaryClockSrc,
       "clockSrcMode": clockSrcMode,
       "clockSrcCmdStatus": clockSrcCmdStatus,
       "connections": connections,
       "connInfo": connInfo,
       "activeMapId": activeMapId,
       "connDBChecksum": connDBChecksum,
       "lastMapCopied": lastMapCopied,
       "connMapTable": connMapTable,
       "connMapEntry": connMapEntry,
       "connMapID": connMapID,
       "connMapName": connMapName,
       "connMapCurrStatus": connMapCurrStatus,
       "connMapDescription": connMapDescription,
       "connMapCounts": connMapCounts,
       "connMapVersions": connMapVersions,
       "connMapDate": connMapDate,
       "connMapCmdStatus": connMapCmdStatus,
       "connMapChecksum": connMapChecksum,
       "sysConnTable": sysConnTable,
       "sysConnEntry": sysConnEntry,
       "sysMapID": sysMapID,
       "sysConnID": sysConnID,
       "sysConnName": sysConnName,
       "sysConnType": sysConnType,
       "sysSrcAddr": sysSrcAddr,
       "sysDestAddr": sysDestAddr,
       "sysComm": sysComm,
       "sysConnSpeed": sysConnSpeed,
       "sysSrcTsBitmap": sysSrcTsBitmap,
       "sysDestTsBitmap": sysDestTsBitmap,
       "sysBroadSrcId": sysBroadSrcId,
       "sysTestMode": sysTestMode,
       "sysCmdStatus": sysCmdStatus,
       "sysPrimaryState": sysPrimaryState,
       "sysSecondaryState": sysSecondaryState,
       "sysConnInstance": sysConnInstance,
       "sysConnChecksum": sysConnChecksum,
       "sysSrcTsLineType": sysSrcTsLineType,
       "sysDestTsLineType": sysDestTsLineType,
       "sysSrcTrunkCProfile": sysSrcTrunkCProfile,
       "sysDestTrunkCProfile": sysDestTrunkCProfile,
       "actvConnTable": actvConnTable,
       "actvConnEntry": actvConnEntry,
       "actvMapID": actvMapID,
       "actvConnID": actvConnID,
       "actvConnName": actvConnName,
       "actvConnType": actvConnType,
       "actvSrcAddr": actvSrcAddr,
       "actvDestAddr": actvDestAddr,
       "actvComm": actvComm,
       "actvConnSpeed": actvConnSpeed,
       "actvSrcTsBitmap": actvSrcTsBitmap,
       "actvDestTsBitmap": actvDestTsBitmap,
       "actvBroadSrcId": actvBroadSrcId,
       "actvTestMode": actvTestMode,
       "actvCmdStatus": actvCmdStatus,
       "actvPrimaryState": actvPrimaryState,
       "actvSecondaryState": actvSecondaryState,
       "actvConnInstance": actvConnInstance,
       "actvConnChecksum": actvConnChecksum,
       "actvSrcTsLineType": actvSrcTsLineType,
       "actvDestTsLineType": actvDestTsLineType,
       "actvSrcTrunkCProfile": actvSrcTrunkCProfile,
       "actvDestTrunkCProfile": actvDestTrunkCProfile,
       "addConnRecord": addConnRecord,
       "addMapID": addMapID,
       "addConnID": addConnID,
       "addConnName": addConnName,
       "addConnType": addConnType,
       "addSrcAddr": addSrcAddr,
       "addDestAddr": addDestAddr,
       "addComm": addComm,
       "addConnSpeed": addConnSpeed,
       "addSrcTsBitmap": addSrcTsBitmap,
       "addDestTsBitmap": addDestTsBitmap,
       "addBroadSrcId": addBroadSrcId,
       "addTestMode": addTestMode,
       "addCmdStatus": addCmdStatus,
       "addSrcTrunkCProfile": addSrcTrunkCProfile,
       "addDestTrunkCProfile": addDestTrunkCProfile,
       "trunkCProfileTable": trunkCProfileTable,
       "trunkCProfileEntry": trunkCProfileEntry,
       "trunkProfileID": trunkProfileID,
       "trunkSignalStart": trunkSignalStart,
       "trunkSignalEnd": trunkSignalEnd,
       "trunkData": trunkData,
       "trunkCmdStatus": trunkCmdStatus,
       "utilities": utilities,
       "database": database,
       "dbBackup": dbBackup,
       "dbAutoBackup": dbAutoBackup,
       "dbBackupOccurrence": dbBackupOccurrence,
       "dbBackupDayOfWeek": dbBackupDayOfWeek,
       "dbBackupHour": dbBackupHour,
       "dbBackupMin": dbBackupMin,
       "dbRemoteHostTable": dbRemoteHostTable,
       "dbRemoteHostTableEntry": dbRemoteHostTableEntry,
       "dbHostIndex": dbHostIndex,
       "dbHostIp": dbHostIp,
       "dbHostDirectory": dbHostDirectory,
       "dbHostFilename": dbHostFilename,
       "dbHostCmdStatus": dbHostCmdStatus,
       "devices": devices,
       "traps": traps,
       "trapSequence": trapSequence,
       "trapResourceKey": trapResourceKey,
       "trapTime": trapTime,
       "trapResourceAddress": trapResourceAddress,
       "trapResourceType": trapResourceType,
       "trapType": trapType,
       "trapState": trapState,
       "trapSeverity": trapSeverity,
       "trapSysEvent": trapSysEvent,
       "trapCfg": trapCfg,
       "trapDestinationTable": trapDestinationTable,
       "trapDestinationEntry": trapDestinationEntry,
       "trapDestAddr": trapDestAddr,
       "trapDestName": trapDestName,
       "trapDestCmdStatus": trapDestCmdStatus,
       "trapDestPduType": trapDestPduType,
       "trapDestMaxRetry": trapDestMaxRetry,
       "trapDestTimeout": trapDestTimeout,
       "eriDNXSmcMIB": eriDNXSmcMIB}
)
