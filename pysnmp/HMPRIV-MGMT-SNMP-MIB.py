# SNMP MIB module (HMPRIV-MGMT-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HMPRIV-MGMT-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:35 2024
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

(dot1dStaticAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStaticAddress")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmConfiguration = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14)
)
hmConfiguration.setRevisions(
        ("2008-06-03 12:00",
         "2007-12-11 12:00",
         "2007-09-13 12:00",
         "2010-01-29 12:00",
         "2012-09-04 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HmAgentLogSeverity(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("informational", 6),
          ("notice", 5),
          ("warning", 4))
    )



class LEDState(Integer32, TextualConvention):
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
        *(("green", 2),
          ("off", 1),
          ("red", 4),
          ("yellow", 3))
    )



class DIPSwitchState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )



class PTPTimeInterval(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class PTPPortIdentity(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )



class PTPClockIdentity(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class PTPClockQuality(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class BridgeIdOrNull(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_HmChassis_ObjectIdentity = ObjectIdentity
hmChassis = _HmChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1)
)
_HmChassisEvent_ObjectIdentity = ObjectIdentity
hmChassisEvent = _HmChassisEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0)
)
if mibBuilder.loadTexts:
    hmChassisEvent.setStatus("current")
_HmSystemTable_ObjectIdentity = ObjectIdentity
hmSystemTable = _HmSystemTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1)
)


class _HmSysProduct_Type(Integer32):
    """Custom type hmSysProduct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              12,
              20,
              21,
              100,
              101,
              102,
              110,
              111,
              112,
              120,
              121,
              122,
              130,
              131,
              132,
              140,
              141,
              142,
              200,
              201,
              202,
              210,
              211,
              212,
              220,
              221,
              222,
              230,
              231,
              232,
              240,
              241,
              242,
              300,
              301,
              302,
              303,
              304,
              311,
              312,
              313,
              401,
              410,
              420,
              421,
              425,
              426,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              530,
              531,
              532,
              533,
              534,
              535,
              536,
              537,
              540,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              550,
              551,
              600,
              601,
              620,
              621,
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
              720,
              721,
              722,
              723,
              724,
              725,
              730,
              731,
              732,
              733,
              734,
              740,
              780,
              800,
              801,
              802,
              803,
              804,
              810,
              811,
              812,
              820,
              821,
              822,
              823,
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
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
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
              1200)
        )
    )
    namedValues = NamedValues(
        *(("cs30-0202", 780),
          ("eagle-fw-mm-sc-lh-sc", 527),
          ("eagle-fw-mm-sc-mm-sc", 525),
          ("eagle-fw-mm-sc-sm-sc", 526),
          ("eagle-fw-mm-sc-tx", 524),
          ("eagle-fw-tx-lh-sc", 523),
          ("eagle-fw-tx-mm-sc", 521),
          ("eagle-fw-tx-sm-sc", 522),
          ("eagle-fw-tx-tx", 520),
          ("eagle-mguard-mm-sc-lh-sc", 537),
          ("eagle-mguard-mm-sc-mm-sc", 535),
          ("eagle-mguard-mm-sc-sm-sc", 536),
          ("eagle-mguard-mm-sc-tx", 534),
          ("eagle-mguard-tx-lh-sc", 533),
          ("eagle-mguard-tx-mm-sc", 531),
          ("eagle-mguard-tx-sm-sc", 532),
          ("eagle-mguard-tx-tx", 530),
          ("eagle-mm-sc-lh-sc", 507),
          ("eagle-mm-sc-mm-sc", 505),
          ("eagle-mm-sc-sm-sc", 506),
          ("eagle-mm-sc-tx", 504),
          ("eagle-tx-lh-sc", 503),
          ("eagle-tx-mm-sc", 501),
          ("eagle-tx-sm-sc", 502),
          ("eagle-tx-tx", 500),
          ("eagle20-mm-sc-lh-sc", 547),
          ("eagle20-mm-sc-mm-sc", 545),
          ("eagle20-mm-sc-sm-sc", 546),
          ("eagle20-mm-sc-tx", 544),
          ("eagle20-tx-lh-sc", 543),
          ("eagle20-tx-mm-sc", 541),
          ("eagle20-tx-sm-sc", 542),
          ("eagle20-tx-tx", 540),
          ("eem1", 1200),
          ("mach100", 1100),
          ("mach104-16tx-poep", 1104),
          ("mach104-16tx-poep-2x", 1107),
          ("mach104-16tx-poep-2x-e", 1109),
          ("mach104-16tx-poep-2x-r", 1108),
          ("mach104-16tx-poep-e", 1106),
          ("mach104-16tx-poep-r", 1105),
          ("mach104-20tx-f", 1101),
          ("mach104-20tx-f-4poe", 1103),
          ("mach104-20tx-fr", 1102),
          ("mach3001", 12),
          ("mach3002", 10),
          ("mach3005", 11),
          ("mach4002-24G", 420),
          ("mach4002-24G-3X", 421),
          ("mach4002-48-4G", 410),
          ("mach4002-48G", 425),
          ("mach4002-48G-3X", 426),
          ("mar1020", 900),
          ("mar1022", 903),
          ("mar1030", 901),
          ("mar1030-4g", 902),
          ("mar1032", 904),
          ("mar1032-4g", 905),
          ("mar1040", 912),
          ("mar1042", 913),
          ("mar1120", 906),
          ("mar1122", 909),
          ("mar1130", 907),
          ("mar1130-4g", 908),
          ("mar1132", 910),
          ("mar1132-4g", 911),
          ("mar1140", 914),
          ("mar1142", 915),
          ("ms20-0800", 600),
          ("ms20-2400", 601),
          ("ms2108-2", 20),
          ("ms30-0802", 620),
          ("ms30-2402", 621),
          ("ms3124-4", 21),
          ("ms4128-5", 401),
          ("octopus-16m", 801),
          ("octopus-16m-2g", 804),
          ("octopus-24m", 802),
          ("octopus-8m", 800),
          ("octopus-8m-2g", 803),
          ("os-000800", 810),
          ("os-000802", 811),
          ("os-001000", 812),
          ("osb20-10tx", 822),
          ("osb20-9tx", 820),
          ("osb24-10tx-8poe", 823),
          ("osb24-9tx-8poe", 821),
          ("rr-epl-tx-mm-sc", 551),
          ("rr-epl-tx-tx", 550),
          ("rs2-14m", 102),
          ("rs2-15m", 101),
          ("rs2-15m-1lh-sc", 122),
          ("rs2-15m-1mm-sc", 120),
          ("rs2-15m-1sm-sc", 121),
          ("rs2-16m", 100),
          ("rs2-16m-1lh-sc", 112),
          ("rs2-16m-1mm-sc", 110),
          ("rs2-16m-1mm-sc-1lh-sc", 141),
          ("rs2-16m-1mm-sc-1sm-sc", 140),
          ("rs2-16m-1sm-sc", 111),
          ("rs2-16m-1sm-sc-1lh-sc", 142),
          ("rs2-16m-2lh-sc", 132),
          ("rs2-16m-2mm-sc", 130),
          ("rs2-16m-2sm-sc", 131),
          ("rs2-4r", 300),
          ("rs2-4r-1fl-st", 304),
          ("rs2-4r-1lh-sc", 303),
          ("rs2-4r-1mm-sc", 301),
          ("rs2-4r-1sm-sc", 302),
          ("rs2-4r-2lh-sc", 313),
          ("rs2-4r-2mm-sc", 311),
          ("rs2-4r-2sm-sc", 312),
          ("rs2-6m", 202),
          ("rs2-7m", 201),
          ("rs2-7m-1lh-sc", 222),
          ("rs2-7m-1mm-sc", 220),
          ("rs2-7m-1sm-sc", 221),
          ("rs2-8m", 200),
          ("rs2-8m-1lh-sc", 212),
          ("rs2-8m-1mm-sc", 210),
          ("rs2-8m-1mm-sc-1lh-sc", 241),
          ("rs2-8m-1mm-sc-1sm-sc", 240),
          ("rs2-8m-1sm-sc", 211),
          ("rs2-8m-1sm-sc-1lh-sc", 242),
          ("rs2-8m-2lh-sc", 232),
          ("rs2-8m-2mm-sc", 230),
          ("rs2-8m-2sm-sc", 231),
          ("rs2-fx-fx", 2),
          ("rs2-fxsm-fxsm", 3),
          ("rs2-tx-tx", 1),
          ("rs20-0400", 700),
          ("rs20-0400m1", 701),
          ("rs20-0400m2", 702),
          ("rs20-0800", 703),
          ("rs20-0800m2", 704),
          ("rs20-0900m3", 709),
          ("rs20-1600", 705),
          ("rs20-1600m2", 706),
          ("rs20-1700m3", 710),
          ("rs20-2400", 707),
          ("rs20-2400m2", 708),
          ("rs20-2500m3", 711),
          ("rs30-0802", 720),
          ("rs30-0802m4", 723),
          ("rs30-1602", 721),
          ("rs30-1602m4", 724),
          ("rs30-2402", 722),
          ("rs30-2402m4", 725),
          ("rs40-0009", 740),
          ("rsb20-6tx-2fx", 732),
          ("rsb20-6tx-3fx", 733),
          ("rsb20-6tx-3sfp", 734),
          ("rsb20-8tx", 730),
          ("rsb20-8tx-1fx", 731),
          ("rsr20-06tp-02fx", 1007),
          ("rsr20-06tp-03fx", 1006),
          ("rsr20-08tp", 1008),
          ("rsr30-06tp-02sfp-02combo", 1002),
          ("rsr30-06tp-02sfp-02sfp", 1003),
          ("rsr30-06tp-03combo", 1001),
          ("rsr30-07sfp-03sfp", 1000),
          ("rsr30-08tp-02combo", 1004),
          ("rsr30-08tp-02sfp", 1005))
    )


_HmSysProduct_Type.__name__ = "Integer32"
_HmSysProduct_Object = MibScalar
hmSysProduct = _HmSysProduct_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 1),
    _HmSysProduct_Type()
)
hmSysProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysProduct.setStatus("current")
_HmSysVersion_Type = DisplayString
_HmSysVersion_Object = MibScalar
hmSysVersion = _HmSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 2),
    _HmSysVersion_Type()
)
hmSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysVersion.setStatus("current")
_HmSysGroupCapacity_Type = Integer32
_HmSysGroupCapacity_Object = MibScalar
hmSysGroupCapacity = _HmSysGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 3),
    _HmSysGroupCapacity_Type()
)
hmSysGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupCapacity.setStatus("current")
_HmSysGroupMap_Type = DisplayString
_HmSysGroupMap_Object = MibScalar
hmSysGroupMap = _HmSysGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 4),
    _HmSysGroupMap_Type()
)
hmSysGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupMap.setStatus("current")
_HmSysMaxPowerSupply_Type = Integer32
_HmSysMaxPowerSupply_Object = MibScalar
hmSysMaxPowerSupply = _HmSysMaxPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 5),
    _HmSysMaxPowerSupply_Type()
)
hmSysMaxPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysMaxPowerSupply.setStatus("current")
_HmSysMaxFan_Type = Integer32
_HmSysMaxFan_Object = MibScalar
hmSysMaxFan = _HmSysMaxFan_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 6),
    _HmSysMaxFan_Type()
)
hmSysMaxFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysMaxFan.setStatus("current")
_HmSysGroupModuleCapacity_Type = Integer32
_HmSysGroupModuleCapacity_Object = MibScalar
hmSysGroupModuleCapacity = _HmSysGroupModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 7),
    _HmSysGroupModuleCapacity_Type()
)
hmSysGroupModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupModuleCapacity.setStatus("current")
_HmSysModulePortCapacity_Type = Integer32
_HmSysModulePortCapacity_Object = MibScalar
hmSysModulePortCapacity = _HmSysModulePortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 8),
    _HmSysModulePortCapacity_Type()
)
hmSysModulePortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModulePortCapacity.setStatus("current")
_HmSysGroupTable_Object = MibTable
hmSysGroupTable = _HmSysGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hmSysGroupTable.setStatus("current")
_HmSysGroupEntry_Object = MibTableRow
hmSysGroupEntry = _HmSysGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1)
)
hmSysGroupEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSysGroupID"),
)
if mibBuilder.loadTexts:
    hmSysGroupEntry.setStatus("current")


class _HmSysGroupID_Type(Integer32):
    """Custom type hmSysGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmSysGroupID_Type.__name__ = "Integer32"
_HmSysGroupID_Object = MibTableColumn
hmSysGroupID = _HmSysGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 1),
    _HmSysGroupID_Type()
)
hmSysGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupID.setStatus("current")


class _HmSysGroupType_Type(Integer32):
    """Custom type hmSysGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              21,
              22,
              23,
              30,
              31,
              40,
              41,
              42,
              44,
              45,
              50,
              60,
              70,
              71,
              75,
              76,
              90,
              100,
              110,
              130,
              131,
              200)
        )
    )
    namedValues = NamedValues(
        *(("eem1", 200),
          ("m-basic4", 10),
          ("mach100", 110),
          ("mach1000ge", 131),
          ("mach100ge", 130),
          ("mach4002-24G", 70),
          ("mach4002-24G-3X", 71),
          ("mach4002-48-4G", 50),
          ("mach4002-48G", 75),
          ("mach4002-48G-3X", 76),
          ("ms20", 30),
          ("ms2108-2", 20),
          ("ms30", 31),
          ("ms3124-4", 21),
          ("ms4128-5", 23),
          ("octopus", 60),
          ("osb2x", 45),
          ("railswitchrugged", 100),
          ("rs2", 22),
          ("rs20", 40),
          ("rs30", 41),
          ("rs40", 42),
          ("rsb20", 44),
          ("ruggedswitch", 90),
          ("unknown", 1))
    )


_HmSysGroupType_Type.__name__ = "Integer32"
_HmSysGroupType_Object = MibTableColumn
hmSysGroupType = _HmSysGroupType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 2),
    _HmSysGroupType_Type()
)
hmSysGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupType.setStatus("current")
_HmSysGroupDescription_Type = DisplayString
_HmSysGroupDescription_Object = MibTableColumn
hmSysGroupDescription = _HmSysGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 3),
    _HmSysGroupDescription_Type()
)
hmSysGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupDescription.setStatus("current")
_HmSysGroupHwVersion_Type = DisplayString
_HmSysGroupHwVersion_Object = MibTableColumn
hmSysGroupHwVersion = _HmSysGroupHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 4),
    _HmSysGroupHwVersion_Type()
)
hmSysGroupHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupHwVersion.setStatus("current")
_HmSysGroupSwVersion_Type = DisplayString
_HmSysGroupSwVersion_Object = MibTableColumn
hmSysGroupSwVersion = _HmSysGroupSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 5),
    _HmSysGroupSwVersion_Type()
)
hmSysGroupSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupSwVersion.setStatus("current")
_HmSysGroupModuleMap_Type = DisplayString
_HmSysGroupModuleMap_Object = MibTableColumn
hmSysGroupModuleMap = _HmSysGroupModuleMap_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 6),
    _HmSysGroupModuleMap_Type()
)
hmSysGroupModuleMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupModuleMap.setStatus("current")


class _HmSysGroupAction_Type(Integer32):
    """Custom type hmSysGroupAction based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("hotRestart", 10),
          ("other", 1),
          ("reset", 2),
          ("resetARP", 5),
          ("resetFDB", 4),
          ("resetL3Stats", 6),
          ("resetL4-7Stats", 7),
          ("resetStats", 3))
    )


_HmSysGroupAction_Type.__name__ = "Integer32"
_HmSysGroupAction_Object = MibTableColumn
hmSysGroupAction = _HmSysGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 7),
    _HmSysGroupAction_Type()
)
hmSysGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysGroupAction.setStatus("current")
_HmSysGroupActionResult_Type = Integer32
_HmSysGroupActionResult_Object = MibTableColumn
hmSysGroupActionResult = _HmSysGroupActionResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 8),
    _HmSysGroupActionResult_Type()
)
hmSysGroupActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupActionResult.setStatus("current")


class _HmSysGroupIsolateMode_Type(Integer32):
    """Custom type hmSysGroupIsolateMode based on Integer32"""
    defaultValue = 2

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


_HmSysGroupIsolateMode_Type.__name__ = "Integer32"
_HmSysGroupIsolateMode_Object = MibTableColumn
hmSysGroupIsolateMode = _HmSysGroupIsolateMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 9),
    _HmSysGroupIsolateMode_Type()
)
hmSysGroupIsolateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysGroupIsolateMode.setStatus("current")
_HmSysGroupSerialNum_Type = DisplayString
_HmSysGroupSerialNum_Object = MibTableColumn
hmSysGroupSerialNum = _HmSysGroupSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 10),
    _HmSysGroupSerialNum_Type()
)
hmSysGroupSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupSerialNum.setStatus("current")


class _HmSysGroupActionDelayPreset_Type(Integer32):
    """Custom type hmSysGroupActionDelayPreset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483),
    )


_HmSysGroupActionDelayPreset_Type.__name__ = "Integer32"
_HmSysGroupActionDelayPreset_Object = MibTableColumn
hmSysGroupActionDelayPreset = _HmSysGroupActionDelayPreset_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 11),
    _HmSysGroupActionDelayPreset_Type()
)
hmSysGroupActionDelayPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysGroupActionDelayPreset.setStatus("current")


class _HmSysGroupActionDelayCurrent_Type(Integer32):
    """Custom type hmSysGroupActionDelayCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483),
    )


_HmSysGroupActionDelayCurrent_Type.__name__ = "Integer32"
_HmSysGroupActionDelayCurrent_Object = MibTableColumn
hmSysGroupActionDelayCurrent = _HmSysGroupActionDelayCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 9, 1, 12),
    _HmSysGroupActionDelayCurrent_Type()
)
hmSysGroupActionDelayCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysGroupActionDelayCurrent.setStatus("current")
_HmSysModuleTable_Object = MibTable
hmSysModuleTable = _HmSysModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hmSysModuleTable.setStatus("current")
_HmSysModuleEntry_Object = MibTableRow
hmSysModuleEntry = _HmSysModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1)
)
hmSysModuleEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSysModGroupID"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSysModID"),
)
if mibBuilder.loadTexts:
    hmSysModuleEntry.setStatus("current")


class _HmSysModGroupID_Type(Integer32):
    """Custom type hmSysModGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmSysModGroupID_Type.__name__ = "Integer32"
_HmSysModGroupID_Object = MibTableColumn
hmSysModGroupID = _HmSysModGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 1),
    _HmSysModGroupID_Type()
)
hmSysModGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModGroupID.setStatus("current")


class _HmSysModID_Type(Integer32):
    """Custom type hmSysModID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmSysModID_Type.__name__ = "Integer32"
_HmSysModID_Object = MibTableColumn
hmSysModID = _HmSysModID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 2),
    _HmSysModID_Type()
)
hmSysModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModID.setStatus("current")


class _HmSysModType_Type(Integer32):
    """Custom type hmSysModType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100,
              101,
              102,
              103,
              104,
              200,
              201,
              300,
              400,
              401,
              402,
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1100,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1107,
              1201,
              1202,
              1203,
              1204,
              1205,
              1206,
              1207,
              1208,
              1209,
              1299,
              1300,
              1301,
              1302,
              1303,
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
              1501,
              1502,
              1503,
              1550,
              1600,
              1601,
              1610,
              1611,
              1612,
              1613,
              1614,
              1615,
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
              1750,
              1751,
              1752,
              1753,
              1850)
        )
    )
    namedValues = NamedValues(
        *(("m-eth-4mm-st", 104),
          ("m-fast-2mm-sc", 102),
          ("m-fast-2sm-sc", 103),
          ("m-fast-8mm-mt", 101),
          ("m-fast-8tp-rj", 100),
          ("m-giga-1lx-sc", 201),
          ("m-giga-1lx-sc-2", 401),
          ("m-giga-2sx-sc", 200),
          ("m-giga-2sx-sc-2", 400),
          ("m-giga-2tp-rj", 402),
          ("m-router", 300),
          ("m1-8mm-sc", 1703),
          ("m1-8sfp", 1705),
          ("m1-8sm-sc", 1704),
          ("m1-8tp-rj45", 1702),
          ("m1-8tp-rj45-poe", 1709),
          ("m4-8tp-rj45", 1501),
          ("m4-base-24g-3xfp", 1615),
          ("m4-base-24g-8tp", 1613),
          ("m4-base-24g-8tp-sfp", 1614),
          ("m4-base-48g-16tp", 1610),
          ("m4-base-48g-3xfp", 1612),
          ("m4-base-48g-8tp-sfp-8tp", 1611),
          ("m4-base-fast-16tp", 1601),
          ("m4-base-giga-4tp-sfp", 1600),
          ("m4-fast-8sfp", 1502),
          ("m4-fast-8tp-rj45-poe", 1503),
          ("m4-giga-8sfp", 1550),
          ("mach102-8tp", 1701),
          ("mach104-16tx-poep", 1710),
          ("mach104-16tx-poep-2x", 1713),
          ("mach104-16tx-poep-2x-e", 1715),
          ("mach104-16tx-poep-2x-r", 1714),
          ("mach104-16tx-poep-e", 1712),
          ("mach104-16tx-poep-r", 1711),
          ("mach104-20tx-f", 1706),
          ("mach104-20tx-f-4poe", 1708),
          ("mach104-20tx-fr", 1707),
          ("mar1040", 1750),
          ("mar1042", 1751),
          ("mar1140", 1752),
          ("mar1142", 1753),
          ("mm2-2flm4", 1001),
          ("mm2-2fls4", 1002),
          ("mm2-2fxm2", 1101),
          ("mm2-2fxm3-2tx1", 1201),
          ("mm2-2fxp4", 1106),
          ("mm2-2fxs2", 1102),
          ("mm2-4fxm3", 1100),
          ("mm2-4tx1", 1000),
          ("mm20-ioioioio", 1850),
          ("mm23-f4f4t1t1", 1410),
          ("mm23-m2m2t1t1", 1408),
          ("mm23-s2s2t1t1", 1409),
          ("mm23-t1t1t1t1", 1407),
          ("mm3-1fxl2-3tx1", 1204),
          ("mm3-1fxm2-3tx1", 1206),
          ("mm3-1fxs2-3tx1", 1205),
          ("mm3-2aui", 1005),
          ("mm3-2flm3-2tx1-rt", 1303),
          ("mm3-2fxm2-2tx1", 1202),
          ("mm3-2fxm2-2tx1-rt", 1301),
          ("mm3-2fxm4-2tx1", 1207),
          ("mm3-2fxs2-2tx1", 1203),
          ("mm3-2fxs2-2tx1-rt", 1302),
          ("mm3-3fxxx-1tx1", 1299),
          ("mm3-3tx1-1fxm2", 1208),
          ("mm3-3tx5-poe-1tx5", 1406),
          ("mm3-4flm4", 1003),
          ("mm3-4fls4", 1004),
          ("mm3-4fxm2", 1103),
          ("mm3-4fxm4", 1105),
          ("mm3-4fxp4", 1107),
          ("mm3-4fxs2", 1104),
          ("mm3-4sfp", 1404),
          ("mm3-4tx1-poe", 1403),
          ("mm3-4tx1-rt", 1300),
          ("mm3-4tx5", 1006),
          ("mm3-4tx5-poe", 1405),
          ("mm3-4tx5-relay", 1209),
          ("mm33-07079999", 1411),
          ("mm4-2tx-giga", 1413),
          ("mm4-2tx-sfp", 1402),
          ("mm4-2tx-sfp-giga", 1412),
          ("mm4-4tx-sfp", 1401),
          ("unknown", 1))
    )


_HmSysModType_Type.__name__ = "Integer32"
_HmSysModType_Object = MibTableColumn
hmSysModType = _HmSysModType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 3),
    _HmSysModType_Type()
)
hmSysModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModType.setStatus("current")
_HmSysModDescription_Type = DisplayString
_HmSysModDescription_Object = MibTableColumn
hmSysModDescription = _HmSysModDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 4),
    _HmSysModDescription_Type()
)
hmSysModDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModDescription.setStatus("current")
_HmSysModVersion_Type = DisplayString
_HmSysModVersion_Object = MibTableColumn
hmSysModVersion = _HmSysModVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 5),
    _HmSysModVersion_Type()
)
hmSysModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModVersion.setStatus("current")
_HmSysModNumOfPorts_Type = Integer32
_HmSysModNumOfPorts_Object = MibTableColumn
hmSysModNumOfPorts = _HmSysModNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 6),
    _HmSysModNumOfPorts_Type()
)
hmSysModNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModNumOfPorts.setStatus("current")
_HmSysModFirstMauIndex_Type = Integer32
_HmSysModFirstMauIndex_Object = MibTableColumn
hmSysModFirstMauIndex = _HmSysModFirstMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 7),
    _HmSysModFirstMauIndex_Type()
)
hmSysModFirstMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModFirstMauIndex.setStatus("current")


class _HmSysModStatus_Type(Integer32):
    """Custom type hmSysModStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurable", 2),
          ("physical", 1),
          ("remove", 3))
    )


_HmSysModStatus_Type.__name__ = "Integer32"
_HmSysModStatus_Object = MibTableColumn
hmSysModStatus = _HmSysModStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 8),
    _HmSysModStatus_Type()
)
hmSysModStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysModStatus.setStatus("current")
_HmSysModSerialNum_Type = DisplayString
_HmSysModSerialNum_Object = MibTableColumn
hmSysModSerialNum = _HmSysModSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 10, 1, 9),
    _HmSysModSerialNum_Type()
)
hmSysModSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysModSerialNum.setStatus("current")
_HmInterfaceTable_Object = MibTable
hmInterfaceTable = _HmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hmInterfaceTable.setStatus("current")
_HmInterfaceEntry_Object = MibTableRow
hmInterfaceEntry = _HmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1)
)
hmInterfaceEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmIfaceGroupID"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmIfaceID"),
)
if mibBuilder.loadTexts:
    hmInterfaceEntry.setStatus("current")


class _HmIfaceGroupID_Type(Integer32):
    """Custom type hmIfaceGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmIfaceGroupID_Type.__name__ = "Integer32"
_HmIfaceGroupID_Object = MibTableColumn
hmIfaceGroupID = _HmIfaceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 1),
    _HmIfaceGroupID_Type()
)
hmIfaceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceGroupID.setStatus("current")


class _HmIfaceID_Type(Integer32):
    """Custom type hmIfaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmIfaceID_Type.__name__ = "Integer32"
_HmIfaceID_Object = MibTableColumn
hmIfaceID = _HmIfaceID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 2),
    _HmIfaceID_Type()
)
hmIfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceID.setStatus("current")


class _HmIfaceStpEnable_Type(Integer32):
    """Custom type hmIfaceStpEnable based on Integer32"""
    defaultValue = 1

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


_HmIfaceStpEnable_Type.__name__ = "Integer32"
_HmIfaceStpEnable_Object = MibTableColumn
hmIfaceStpEnable = _HmIfaceStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 3),
    _HmIfaceStpEnable_Type()
)
hmIfaceStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceStpEnable.setStatus("current")


class _HmIfaceLinkType_Type(Integer32):
    """Custom type hmIfaceLinkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uplink", 2),
          ("user", 1))
    )


_HmIfaceLinkType_Type.__name__ = "Integer32"
_HmIfaceLinkType_Object = MibTableColumn
hmIfaceLinkType = _HmIfaceLinkType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 4),
    _HmIfaceLinkType_Type()
)
hmIfaceLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceLinkType.setStatus("current")


class _HmIfaceAction_Type(Integer32):
    """Custom type hmIfaceAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetStats", 2))
    )


_HmIfaceAction_Type.__name__ = "Integer32"
_HmIfaceAction_Object = MibTableColumn
hmIfaceAction = _HmIfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 5),
    _HmIfaceAction_Type()
)
hmIfaceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceAction.setStatus("current")
_HmIfaceNextHopMacAddress_Type = MacAddress
_HmIfaceNextHopMacAddress_Object = MibTableColumn
hmIfaceNextHopMacAddress = _HmIfaceNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 6),
    _HmIfaceNextHopMacAddress_Type()
)
hmIfaceNextHopMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceNextHopMacAddress.setStatus("current")


class _HmIfaceFlowControl_Type(Integer32):
    """Custom type hmIfaceFlowControl based on Integer32"""
    defaultValue = 1

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


_HmIfaceFlowControl_Type.__name__ = "Integer32"
_HmIfaceFlowControl_Object = MibTableColumn
hmIfaceFlowControl = _HmIfaceFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 7),
    _HmIfaceFlowControl_Type()
)
hmIfaceFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceFlowControl.setStatus("current")


class _HmIfacePriorityThreshold_Type(Integer32):
    """Custom type hmIfacePriorityThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmIfacePriorityThreshold_Type.__name__ = "Integer32"
_HmIfacePriorityThreshold_Object = MibTableColumn
hmIfacePriorityThreshold = _HmIfacePriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 8),
    _HmIfacePriorityThreshold_Type()
)
hmIfacePriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfacePriorityThreshold.setStatus("current")


class _HmIfaceName_Type(DisplayString):
    """Custom type hmIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmIfaceName_Type.__name__ = "DisplayString"
_HmIfaceName_Object = MibTableColumn
hmIfaceName = _HmIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 9),
    _HmIfaceName_Type()
)
hmIfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceName.setStatus("current")


class _HmIfaceTrunkID_Type(Integer32):
    """Custom type hmIfaceTrunkID based on Integer32"""
    defaultValue = 0


_HmIfaceTrunkID_Object = MibTableColumn
hmIfaceTrunkID = _HmIfaceTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 10),
    _HmIfaceTrunkID_Type()
)
hmIfaceTrunkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceTrunkID.setStatus("current")


class _HmIfacePrioTOSEnable_Type(Integer32):
    """Custom type hmIfacePrioTOSEnable based on Integer32"""
    defaultValue = 2

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


_HmIfacePrioTOSEnable_Type.__name__ = "Integer32"
_HmIfacePrioTOSEnable_Object = MibTableColumn
hmIfacePrioTOSEnable = _HmIfacePrioTOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 11),
    _HmIfacePrioTOSEnable_Type()
)
hmIfacePrioTOSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfacePrioTOSEnable.setStatus("current")


class _HmIfaceBcastLimit_Type(Integer32):
    """Custom type hmIfaceBcastLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_HmIfaceBcastLimit_Type.__name__ = "Integer32"
_HmIfaceBcastLimit_Object = MibTableColumn
hmIfaceBcastLimit = _HmIfaceBcastLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 12),
    _HmIfaceBcastLimit_Type()
)
hmIfaceBcastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceBcastLimit.setStatus("current")


class _HmIfaceUtilization_Type(Integer32):
    """Custom type hmIfaceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HmIfaceUtilization_Type.__name__ = "Integer32"
_HmIfaceUtilization_Object = MibTableColumn
hmIfaceUtilization = _HmIfaceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 13),
    _HmIfaceUtilization_Type()
)
hmIfaceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceUtilization.setStatus("current")


class _HmIfaceUtilizationControlInterval_Type(Integer32):
    """Custom type hmIfaceUtilizationControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HmIfaceUtilizationControlInterval_Type.__name__ = "Integer32"
_HmIfaceUtilizationControlInterval_Object = MibTableColumn
hmIfaceUtilizationControlInterval = _HmIfaceUtilizationControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 14),
    _HmIfaceUtilizationControlInterval_Type()
)
hmIfaceUtilizationControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceUtilizationControlInterval.setStatus("current")


class _HmIfaceStpBpduGuardEnable_Type(Integer32):
    """Custom type hmIfaceStpBpduGuardEnable based on Integer32"""
    defaultValue = 1

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


_HmIfaceStpBpduGuardEnable_Type.__name__ = "Integer32"
_HmIfaceStpBpduGuardEnable_Object = MibTableColumn
hmIfaceStpBpduGuardEnable = _HmIfaceStpBpduGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 15),
    _HmIfaceStpBpduGuardEnable_Type()
)
hmIfaceStpBpduGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceStpBpduGuardEnable.setStatus("current")


class _HmIfaceStpBpduGuardStatus_Type(Integer32):
    """Custom type hmIfaceStpBpduGuardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmIfaceStpBpduGuardStatus_Type.__name__ = "Integer32"
_HmIfaceStpBpduGuardStatus_Object = MibTableColumn
hmIfaceStpBpduGuardStatus = _HmIfaceStpBpduGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 16),
    _HmIfaceStpBpduGuardStatus_Type()
)
hmIfaceStpBpduGuardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceStpBpduGuardStatus.setStatus("current")
_HmIfaceCapability_Type = Integer32
_HmIfaceCapability_Object = MibTableColumn
hmIfaceCapability = _HmIfaceCapability_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 17),
    _HmIfaceCapability_Type()
)
hmIfaceCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceCapability.setStatus("current")


class _HmIfaceIngressLimiterMode_Type(Integer32):
    """Custom type hmIfaceIngressLimiterMode based on Integer32"""
    defaultValue = 2

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
        *(("all", 1),
          ("bc", 2),
          ("bc-mc", 3),
          ("bc-mc-uuc", 4))
    )


_HmIfaceIngressLimiterMode_Type.__name__ = "Integer32"
_HmIfaceIngressLimiterMode_Object = MibTableColumn
hmIfaceIngressLimiterMode = _HmIfaceIngressLimiterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 18),
    _HmIfaceIngressLimiterMode_Type()
)
hmIfaceIngressLimiterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceIngressLimiterMode.setStatus("current")


class _HmIfaceIngressLimiterCalculationMode_Type(Integer32):
    """Custom type hmIfaceIngressLimiterCalculationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytebased", 1),
          ("packetbased", 2))
    )


_HmIfaceIngressLimiterCalculationMode_Type.__name__ = "Integer32"
_HmIfaceIngressLimiterCalculationMode_Object = MibTableColumn
hmIfaceIngressLimiterCalculationMode = _HmIfaceIngressLimiterCalculationMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 19),
    _HmIfaceIngressLimiterCalculationMode_Type()
)
hmIfaceIngressLimiterCalculationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceIngressLimiterCalculationMode.setStatus("current")


class _HmIfaceIngressLimiterRate_Type(Integer32):
    """Custom type hmIfaceIngressLimiterRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_HmIfaceIngressLimiterRate_Type.__name__ = "Integer32"
_HmIfaceIngressLimiterRate_Object = MibTableColumn
hmIfaceIngressLimiterRate = _HmIfaceIngressLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 20),
    _HmIfaceIngressLimiterRate_Type()
)
hmIfaceIngressLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceIngressLimiterRate.setStatus("current")


class _HmIfaceEgressLimiterMode_Type(Integer32):
    """Custom type hmIfaceEgressLimiterMode based on Integer32"""
    defaultValue = 1

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
        *(("all", 1),
          ("bc", 2),
          ("bc-mc", 3),
          ("bc-mc-uuc", 4))
    )


_HmIfaceEgressLimiterMode_Type.__name__ = "Integer32"
_HmIfaceEgressLimiterMode_Object = MibTableColumn
hmIfaceEgressLimiterMode = _HmIfaceEgressLimiterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 21),
    _HmIfaceEgressLimiterMode_Type()
)
hmIfaceEgressLimiterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceEgressLimiterMode.setStatus("current")


class _HmIfaceEgressLimiterCalculationMode_Type(Integer32):
    """Custom type hmIfaceEgressLimiterCalculationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytebased", 1),
          ("packetbased", 2))
    )


_HmIfaceEgressLimiterCalculationMode_Type.__name__ = "Integer32"
_HmIfaceEgressLimiterCalculationMode_Object = MibTableColumn
hmIfaceEgressLimiterCalculationMode = _HmIfaceEgressLimiterCalculationMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 22),
    _HmIfaceEgressLimiterCalculationMode_Type()
)
hmIfaceEgressLimiterCalculationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceEgressLimiterCalculationMode.setStatus("current")


class _HmIfaceEgressLimiterRate_Type(Integer32):
    """Custom type hmIfaceEgressLimiterRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_HmIfaceEgressLimiterRate_Type.__name__ = "Integer32"
_HmIfaceEgressLimiterRate_Object = MibTableColumn
hmIfaceEgressLimiterRate = _HmIfaceEgressLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 23),
    _HmIfaceEgressLimiterRate_Type()
)
hmIfaceEgressLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceEgressLimiterRate.setStatus("current")


class _HmIfaceUtilizationAlarmUpperThreshold_Type(Integer32):
    """Custom type hmIfaceUtilizationAlarmUpperThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HmIfaceUtilizationAlarmUpperThreshold_Type.__name__ = "Integer32"
_HmIfaceUtilizationAlarmUpperThreshold_Object = MibTableColumn
hmIfaceUtilizationAlarmUpperThreshold = _HmIfaceUtilizationAlarmUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 24),
    _HmIfaceUtilizationAlarmUpperThreshold_Type()
)
hmIfaceUtilizationAlarmUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceUtilizationAlarmUpperThreshold.setStatus("current")


class _HmIfaceUtilizationAlarmLowerThreshold_Type(Integer32):
    """Custom type hmIfaceUtilizationAlarmLowerThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HmIfaceUtilizationAlarmLowerThreshold_Type.__name__ = "Integer32"
_HmIfaceUtilizationAlarmLowerThreshold_Object = MibTableColumn
hmIfaceUtilizationAlarmLowerThreshold = _HmIfaceUtilizationAlarmLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 25),
    _HmIfaceUtilizationAlarmLowerThreshold_Type()
)
hmIfaceUtilizationAlarmLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceUtilizationAlarmLowerThreshold.setStatus("current")
_HmIfaceUtilizationAlarmCondition_Type = TruthValue
_HmIfaceUtilizationAlarmCondition_Object = MibTableColumn
hmIfaceUtilizationAlarmCondition = _HmIfaceUtilizationAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 26),
    _HmIfaceUtilizationAlarmCondition_Type()
)
hmIfaceUtilizationAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIfaceUtilizationAlarmCondition.setStatus("current")


class _HmIfaceCableCrossing_Type(Integer32):
    """Custom type hmIfaceCableCrossing based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("unsupported", 3))
    )


_HmIfaceCableCrossing_Type.__name__ = "Integer32"
_HmIfaceCableCrossing_Object = MibTableColumn
hmIfaceCableCrossing = _HmIfaceCableCrossing_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 27),
    _HmIfaceCableCrossing_Type()
)
hmIfaceCableCrossing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfaceCableCrossing.setStatus("current")


class _HmIfacePhyFastLinkDetection_Type(Integer32):
    """Custom type hmIfacePhyFastLinkDetection based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("unsupported", 3))
    )


_HmIfacePhyFastLinkDetection_Type.__name__ = "Integer32"
_HmIfacePhyFastLinkDetection_Object = MibTableColumn
hmIfacePhyFastLinkDetection = _HmIfacePhyFastLinkDetection_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 11, 1, 28),
    _HmIfacePhyFastLinkDetection_Type()
)
hmIfacePhyFastLinkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIfacePhyFastLinkDetection.setStatus("current")
_HmTrunkTable_Object = MibTable
hmTrunkTable = _HmTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hmTrunkTable.setStatus("current")
_HmTrunkEntry_Object = MibTableRow
hmTrunkEntry = _HmTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1)
)
hmTrunkEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmTrunkID"),
)
if mibBuilder.loadTexts:
    hmTrunkEntry.setStatus("current")


class _HmTrunkID_Type(Integer32):
    """Custom type hmTrunkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmTrunkID_Type.__name__ = "Integer32"
_HmTrunkID_Object = MibTableColumn
hmTrunkID = _HmTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1, 1),
    _HmTrunkID_Type()
)
hmTrunkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrunkID.setStatus("current")
_HmTrunkInterfaces_Type = OctetString
_HmTrunkInterfaces_Object = MibTableColumn
hmTrunkInterfaces = _HmTrunkInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1, 2),
    _HmTrunkInterfaces_Type()
)
hmTrunkInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrunkInterfaces.setStatus("current")
_HmTrunkName_Type = DisplayString
_HmTrunkName_Object = MibTableColumn
hmTrunkName = _HmTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1, 3),
    _HmTrunkName_Type()
)
hmTrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrunkName.setStatus("current")


class _HmTrunkAction_Type(Integer32):
    """Custom type hmTrunkAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetStats", 2))
    )


_HmTrunkAction_Type.__name__ = "Integer32"
_HmTrunkAction_Object = MibTableColumn
hmTrunkAction = _HmTrunkAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1, 4),
    _HmTrunkAction_Type()
)
hmTrunkAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrunkAction.setStatus("current")


class _HmTrunkAdminStatus_Type(Integer32):
    """Custom type hmTrunkAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HmTrunkAdminStatus_Type.__name__ = "Integer32"
_HmTrunkAdminStatus_Object = MibTableColumn
hmTrunkAdminStatus = _HmTrunkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1, 5),
    _HmTrunkAdminStatus_Type()
)
hmTrunkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrunkAdminStatus.setStatus("current")


class _HmTrunkOperStatus_Type(Integer32):
    """Custom type hmTrunkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HmTrunkOperStatus_Type.__name__ = "Integer32"
_HmTrunkOperStatus_Object = MibTableColumn
hmTrunkOperStatus = _HmTrunkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1, 6),
    _HmTrunkOperStatus_Type()
)
hmTrunkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrunkOperStatus.setStatus("current")
_HmTrunkLastChange_Type = TimeTicks
_HmTrunkLastChange_Object = MibTableColumn
hmTrunkLastChange = _HmTrunkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 12, 1, 7),
    _HmTrunkLastChange_Type()
)
hmTrunkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrunkLastChange.setStatus("current")
_HmSFPTable_Object = MibTable
hmSFPTable = _HmSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13)
)
if mibBuilder.loadTexts:
    hmSFPTable.setStatus("current")
_HmSFPEntry_Object = MibTableRow
hmSFPEntry = _HmSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1)
)
hmSFPEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSfpGroupID"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSfpID"),
)
if mibBuilder.loadTexts:
    hmSFPEntry.setStatus("current")


class _HmSfpGroupID_Type(Integer32):
    """Custom type hmSfpGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmSfpGroupID_Type.__name__ = "Integer32"
_HmSfpGroupID_Object = MibTableColumn
hmSfpGroupID = _HmSfpGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 1),
    _HmSfpGroupID_Type()
)
hmSfpGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSfpGroupID.setStatus("current")


class _HmSfpID_Type(Integer32):
    """Custom type hmSfpID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmSfpID_Type.__name__ = "Integer32"
_HmSfpID_Object = MibTableColumn
hmSfpID = _HmSfpID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 2),
    _HmSfpID_Type()
)
hmSfpID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSfpID.setStatus("current")


class _HmSfpConnector_Type(Integer32):
    """Custom type hmSfpConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              8,
              11,
              33)
        )
    )
    namedValues = NamedValues(
        *(("copper-pigtail", 33),
          ("fiberjack", 6),
          ("lc", 7),
          ("mt-rj", 8),
          ("non-sfp", 1),
          ("optical-pigtail", 11))
    )


_HmSfpConnector_Type.__name__ = "Integer32"
_HmSfpConnector_Object = MibTableColumn
hmSfpConnector = _HmSfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 3),
    _HmSfpConnector_Type()
)
hmSfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpConnector.setStatus("current")


class _HmSfpTransceiver_Type(Integer32):
    """Custom type hmSfpTransceiver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
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
              30,
              31,
              32,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("ge-1000-base-cx", 4),
          ("ge-1000-base-lx", 2),
          ("ge-1000-base-sx", 1),
          ("ge-1000-base-t", 8),
          ("microfx", 40),
          ("oc12-mm-sr", 13),
          ("oc12-sm-ir", 14),
          ("oc12-sm-lr", 15),
          ("oc3-mm-sr", 10),
          ("oc3-sm-ir", 11),
          ("oc3-sm-lr", 12),
          ("oc48-ir", 17),
          ("oc48-lr", 18),
          ("oc48-sr", 16),
          ("pof", 41),
          ("unsupported", 9),
          ("xfp-10gbase-er", 32),
          ("xfp-10gbase-lr", 31),
          ("xfp-10gbase-sr", 30))
    )


_HmSfpTransceiver_Type.__name__ = "Integer32"
_HmSfpTransceiver_Object = MibTableColumn
hmSfpTransceiver = _HmSfpTransceiver_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 4),
    _HmSfpTransceiver_Type()
)
hmSfpTransceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpTransceiver.setStatus("current")
_HmSfpVendorOUI_Type = OctetString
_HmSfpVendorOUI_Object = MibTableColumn
hmSfpVendorOUI = _HmSfpVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 5),
    _HmSfpVendorOUI_Type()
)
hmSfpVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpVendorOUI.setStatus("current")
_HmSfpVendorName_Type = DisplayString
_HmSfpVendorName_Object = MibTableColumn
hmSfpVendorName = _HmSfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 6),
    _HmSfpVendorName_Type()
)
hmSfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpVendorName.setStatus("current")
_HmSfpPartNumber_Type = DisplayString
_HmSfpPartNumber_Object = MibTableColumn
hmSfpPartNumber = _HmSfpPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 7),
    _HmSfpPartNumber_Type()
)
hmSfpPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpPartNumber.setStatus("current")
_HmSfpPartRev_Type = DisplayString
_HmSfpPartRev_Object = MibTableColumn
hmSfpPartRev = _HmSfpPartRev_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 8),
    _HmSfpPartRev_Type()
)
hmSfpPartRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpPartRev.setStatus("current")
_HmSfpSerialNum_Type = DisplayString
_HmSfpSerialNum_Object = MibTableColumn
hmSfpSerialNum = _HmSfpSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 9),
    _HmSfpSerialNum_Type()
)
hmSfpSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpSerialNum.setStatus("current")
_HmSfpDateCode_Type = DisplayString
_HmSfpDateCode_Object = MibTableColumn
hmSfpDateCode = _HmSfpDateCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 10),
    _HmSfpDateCode_Type()
)
hmSfpDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpDateCode.setStatus("current")
_HmSfpBitRate_Type = Integer32
_HmSfpBitRate_Object = MibTableColumn
hmSfpBitRate = _HmSfpBitRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 11),
    _HmSfpBitRate_Type()
)
hmSfpBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpBitRate.setStatus("current")
_HmSfpTemperature_Type = Integer32
_HmSfpTemperature_Object = MibTableColumn
hmSfpTemperature = _HmSfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 12),
    _HmSfpTemperature_Type()
)
hmSfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpTemperature.setStatus("current")
_HmSfpTxPower_Type = DisplayString
_HmSfpTxPower_Object = MibTableColumn
hmSfpTxPower = _HmSfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 13),
    _HmSfpTxPower_Type()
)
hmSfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpTxPower.setStatus("current")
_HmSfpRxPower_Type = DisplayString
_HmSfpRxPower_Object = MibTableColumn
hmSfpRxPower = _HmSfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 14),
    _HmSfpRxPower_Type()
)
hmSfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpRxPower.setStatus("current")
_HmSfpTxPowerInt_Type = Integer32
_HmSfpTxPowerInt_Object = MibTableColumn
hmSfpTxPowerInt = _HmSfpTxPowerInt_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 15),
    _HmSfpTxPowerInt_Type()
)
hmSfpTxPowerInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpTxPowerInt.setStatus("current")
_HmSfpRxPowerInt_Type = Integer32
_HmSfpRxPowerInt_Object = MibTableColumn
hmSfpRxPowerInt = _HmSfpRxPowerInt_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 16),
    _HmSfpRxPowerInt_Type()
)
hmSfpRxPowerInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpRxPowerInt.setStatus("current")


class _HmSfpRxPowerState_Type(Integer32):
    """Custom type hmSfpRxPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("ok", 1),
          ("warning", 2))
    )


_HmSfpRxPowerState_Type.__name__ = "Integer32"
_HmSfpRxPowerState_Object = MibTableColumn
hmSfpRxPowerState = _HmSfpRxPowerState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 17),
    _HmSfpRxPowerState_Type()
)
hmSfpRxPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpRxPowerState.setStatus("current")
_HmSfpInfoVersion_Type = Integer32
_HmSfpInfoVersion_Object = MibTableColumn
hmSfpInfoVersion = _HmSfpInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 20),
    _HmSfpInfoVersion_Type()
)
hmSfpInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpInfoVersion.setStatus("current")


class _HmSfpInfoPartNumber_Type(DisplayString):
    """Custom type hmSfpInfoPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_HmSfpInfoPartNumber_Type.__name__ = "DisplayString"
_HmSfpInfoPartNumber_Object = MibTableColumn
hmSfpInfoPartNumber = _HmSfpInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 21),
    _HmSfpInfoPartNumber_Type()
)
hmSfpInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpInfoPartNumber.setStatus("current")


class _HmSfpInfoPartId_Type(DisplayString):
    """Custom type hmSfpInfoPartId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmSfpInfoPartId_Type.__name__ = "DisplayString"
_HmSfpInfoPartId_Object = MibTableColumn
hmSfpInfoPartId = _HmSfpInfoPartId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 22),
    _HmSfpInfoPartId_Type()
)
hmSfpInfoPartId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpInfoPartId.setStatus("current")
_HmSfpInfoMagic_Type = Integer32
_HmSfpInfoMagic_Object = MibTableColumn
hmSfpInfoMagic = _HmSfpInfoMagic_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 23),
    _HmSfpInfoMagic_Type()
)
hmSfpInfoMagic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpInfoMagic.setStatus("current")
_HmSfpSupported_Type = TruthValue
_HmSfpSupported_Object = MibTableColumn
hmSfpSupported = _HmSfpSupported_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 24),
    _HmSfpSupported_Type()
)
hmSfpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpSupported.setStatus("current")
_HmSfpMaxLength_fiber_9_Type = Integer32
_HmSfpMaxLength_fiber_9_Object = MibScalar
hmSfpMaxLength_fiber_9 = _HmSfpMaxLength_fiber_9_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 30),
    _HmSfpMaxLength_fiber_9_Type()
)
hmSfpMaxLength_fiber_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpMaxLength_fiber_9.setStatus("current")
_HmSfpMaxLength_fiber_50_Type = Integer32
_HmSfpMaxLength_fiber_50_Object = MibScalar
hmSfpMaxLength_fiber_50 = _HmSfpMaxLength_fiber_50_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 31),
    _HmSfpMaxLength_fiber_50_Type()
)
hmSfpMaxLength_fiber_50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpMaxLength_fiber_50.setStatus("current")
_HmSfpMaxLength_fiber_62_5_Type = Integer32
_HmSfpMaxLength_fiber_62_5_Object = MibScalar
hmSfpMaxLength_fiber_62_5 = _HmSfpMaxLength_fiber_62_5_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 32),
    _HmSfpMaxLength_fiber_62_5_Type()
)
hmSfpMaxLength_fiber_62_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpMaxLength_fiber_62_5.setStatus("current")
_HmSfpMaxLength_copper_Type = Integer32
_HmSfpMaxLength_copper_Object = MibScalar
hmSfpMaxLength_copper = _HmSfpMaxLength_copper_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 33),
    _HmSfpMaxLength_copper_Type()
)
hmSfpMaxLength_copper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpMaxLength_copper.setStatus("current")
_HmSfpTxPowerdBm_Type = DisplayString
_HmSfpTxPowerdBm_Object = MibTableColumn
hmSfpTxPowerdBm = _HmSfpTxPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 34),
    _HmSfpTxPowerdBm_Type()
)
hmSfpTxPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpTxPowerdBm.setStatus("current")
_HmSfpRxPowerdBm_Type = DisplayString
_HmSfpRxPowerdBm_Object = MibTableColumn
hmSfpRxPowerdBm = _HmSfpRxPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 13, 1, 35),
    _HmSfpRxPowerdBm_Type()
)
hmSfpRxPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSfpRxPowerdBm.setStatus("current")
_HmSysChassisName_Type = DisplayString
_HmSysChassisName_Object = MibScalar
hmSysChassisName = _HmSysChassisName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 20),
    _HmSysChassisName_Type()
)
hmSysChassisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysChassisName.setStatus("current")


class _HmSysStpEnable_Type(Integer32):
    """Custom type hmSysStpEnable based on Integer32"""
    defaultValue = 1

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


_HmSysStpEnable_Type.__name__ = "Integer32"
_HmSysStpEnable_Object = MibScalar
hmSysStpEnable = _HmSysStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 21),
    _HmSysStpEnable_Type()
)
hmSysStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysStpEnable.setStatus("current")


class _HmSysFlowControl_Type(Integer32):
    """Custom type hmSysFlowControl based on Integer32"""
    defaultValue = 2

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


_HmSysFlowControl_Type.__name__ = "Integer32"
_HmSysFlowControl_Object = MibScalar
hmSysFlowControl = _HmSysFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 22),
    _HmSysFlowControl_Type()
)
hmSysFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysFlowControl.setStatus("current")


class _HmSysBOOTPEnable_Type(Integer32):
    """Custom type hmSysBOOTPEnable based on Integer32"""
    defaultValue = 2

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


_HmSysBOOTPEnable_Type.__name__ = "Integer32"
_HmSysBOOTPEnable_Object = MibScalar
hmSysBOOTPEnable = _HmSysBOOTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 23),
    _HmSysBOOTPEnable_Type()
)
hmSysBOOTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysBOOTPEnable.setStatus("current")


class _HmSysDHCPEnable_Type(Integer32):
    """Custom type hmSysDHCPEnable based on Integer32"""
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


_HmSysDHCPEnable_Type.__name__ = "Integer32"
_HmSysDHCPEnable_Object = MibScalar
hmSysDHCPEnable = _HmSysDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 24),
    _HmSysDHCPEnable_Type()
)
hmSysDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysDHCPEnable.setStatus("current")


class _HmSysTelnetEnable_Type(Integer32):
    """Custom type hmSysTelnetEnable based on Integer32"""
    defaultValue = 1

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


_HmSysTelnetEnable_Type.__name__ = "Integer32"
_HmSysTelnetEnable_Object = MibScalar
hmSysTelnetEnable = _HmSysTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 25),
    _HmSysTelnetEnable_Type()
)
hmSysTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysTelnetEnable.setStatus("current")


class _HmSysHTTPEnable_Type(Integer32):
    """Custom type hmSysHTTPEnable based on Integer32"""
    defaultValue = 1

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


_HmSysHTTPEnable_Type.__name__ = "Integer32"
_HmSysHTTPEnable_Object = MibScalar
hmSysHTTPEnable = _HmSysHTTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 26),
    _HmSysHTTPEnable_Type()
)
hmSysHTTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysHTTPEnable.setStatus("current")


class _HmSysPlugAndPlay_Type(Integer32):
    """Custom type hmSysPlugAndPlay based on Integer32"""
    defaultValue = 2

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


_HmSysPlugAndPlay_Type.__name__ = "Integer32"
_HmSysPlugAndPlay_Object = MibScalar
hmSysPlugAndPlay = _HmSysPlugAndPlay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 27),
    _HmSysPlugAndPlay_Type()
)
hmSysPlugAndPlay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysPlugAndPlay.setStatus("current")


class _HmBcastLimiterMode_Type(Integer32):
    """Custom type hmBcastLimiterMode based on Integer32"""
    defaultValue = 2

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


_HmBcastLimiterMode_Type.__name__ = "Integer32"
_HmBcastLimiterMode_Object = MibScalar
hmBcastLimiterMode = _HmBcastLimiterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 29),
    _HmBcastLimiterMode_Type()
)
hmBcastLimiterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmBcastLimiterMode.setStatus("current")
_HmSystemTime_Type = TimeTicks
_HmSystemTime_Object = MibScalar
hmSystemTime = _HmSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 30),
    _HmSystemTime_Type()
)
hmSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSystemTime.setStatus("current")


class _HmSystemTimeSource_Type(Integer32):
    """Custom type hmSystemTimeSource based on Integer32"""
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
        *(("gps", 4),
          ("local", 1),
          ("ntp", 5),
          ("ptp", 3),
          ("sntp", 2))
    )


_HmSystemTimeSource_Type.__name__ = "Integer32"
_HmSystemTimeSource_Object = MibScalar
hmSystemTimeSource = _HmSystemTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 31),
    _HmSystemTimeSource_Type()
)
hmSystemTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSystemTimeSource.setStatus("current")


class _HmSysStpBPDUGuardEnable_Type(Integer32):
    """Custom type hmSysStpBPDUGuardEnable based on Integer32"""
    defaultValue = 2

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


_HmSysStpBPDUGuardEnable_Type.__name__ = "Integer32"
_HmSysStpBPDUGuardEnable_Object = MibScalar
hmSysStpBPDUGuardEnable = _HmSysStpBPDUGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 32),
    _HmSysStpBPDUGuardEnable_Type()
)
hmSysStpBPDUGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysStpBPDUGuardEnable.setStatus("current")


class _HmSysSTPErrorNumber_Type(Integer32):
    """Custom type hmSysSTPErrorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HmSysSTPErrorNumber_Type.__name__ = "Integer32"
_HmSysSTPErrorNumber_Object = MibScalar
hmSysSTPErrorNumber = _HmSysSTPErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 33),
    _HmSysSTPErrorNumber_Type()
)
hmSysSTPErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSTPErrorNumber.setStatus("current")
_HmSysSoftwareCapability_Type = DisplayString
_HmSysSoftwareCapability_Object = MibScalar
hmSysSoftwareCapability = _HmSysSoftwareCapability_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 34),
    _HmSysSoftwareCapability_Type()
)
hmSysSoftwareCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSoftwareCapability.setStatus("current")
_HmLEDGroup_ObjectIdentity = ObjectIdentity
hmLEDGroup = _HmLEDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35)
)
_HmLEDRSGroup_ObjectIdentity = ObjectIdentity
hmLEDRSGroup = _HmLEDRSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 1)
)
_HmLEDRSPowerSupply_Type = LEDState
_HmLEDRSPowerSupply_Object = MibScalar
hmLEDRSPowerSupply = _HmLEDRSPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 1, 1),
    _HmLEDRSPowerSupply_Type()
)
hmLEDRSPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSPowerSupply.setStatus("current")
_HmLEDRStandby_Type = LEDState
_HmLEDRStandby_Object = MibScalar
hmLEDRStandby = _HmLEDRStandby_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 1, 2),
    _HmLEDRStandby_Type()
)
hmLEDRStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRStandby.setStatus("current")
_HmLEDRSRedundancyManager_Type = LEDState
_HmLEDRSRedundancyManager_Object = MibScalar
hmLEDRSRedundancyManager = _HmLEDRSRedundancyManager_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 1, 3),
    _HmLEDRSRedundancyManager_Type()
)
hmLEDRSRedundancyManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSRedundancyManager.setStatus("current")
_HmLEDRSFault_Type = LEDState
_HmLEDRSFault_Object = MibScalar
hmLEDRSFault = _HmLEDRSFault_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 1, 4),
    _HmLEDRSFault_Type()
)
hmLEDRSFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSFault.setStatus("current")
_HmLEDOctGroup_ObjectIdentity = ObjectIdentity
hmLEDOctGroup = _HmLEDOctGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 2)
)
_HmLEDOctPowerSupply1_Type = LEDState
_HmLEDOctPowerSupply1_Object = MibScalar
hmLEDOctPowerSupply1 = _HmLEDOctPowerSupply1_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 2, 1),
    _HmLEDOctPowerSupply1_Type()
)
hmLEDOctPowerSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDOctPowerSupply1.setStatus("current")
_HmLEDOctPowerSupply2_Type = LEDState
_HmLEDOctPowerSupply2_Object = MibScalar
hmLEDOctPowerSupply2 = _HmLEDOctPowerSupply2_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 2, 2),
    _HmLEDOctPowerSupply2_Type()
)
hmLEDOctPowerSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDOctPowerSupply2.setStatus("current")
_HmLEDOctRedundancyManager_Type = LEDState
_HmLEDOctRedundancyManager_Object = MibScalar
hmLEDOctRedundancyManager = _HmLEDOctRedundancyManager_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 2, 3),
    _HmLEDOctRedundancyManager_Type()
)
hmLEDOctRedundancyManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDOctRedundancyManager.setStatus("current")
_HmLEDOctFault_Type = LEDState
_HmLEDOctFault_Object = MibScalar
hmLEDOctFault = _HmLEDOctFault_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 2, 4),
    _HmLEDOctFault_Type()
)
hmLEDOctFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDOctFault.setStatus("current")
_HmLEDRSRGroup_ObjectIdentity = ObjectIdentity
hmLEDRSRGroup = _HmLEDRSRGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 3)
)
_HmLEDRSRPowerSupply_Type = LEDState
_HmLEDRSRPowerSupply_Object = MibScalar
hmLEDRSRPowerSupply = _HmLEDRSRPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 3, 1),
    _HmLEDRSRPowerSupply_Type()
)
hmLEDRSRPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSRPowerSupply.setStatus("current")
_HmLEDRSRStandby_Type = LEDState
_HmLEDRSRStandby_Object = MibScalar
hmLEDRSRStandby = _HmLEDRSRStandby_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 3, 2),
    _HmLEDRSRStandby_Type()
)
hmLEDRSRStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSRStandby.setStatus("current")
_HmLEDRSRRedundancyManager_Type = LEDState
_HmLEDRSRRedundancyManager_Object = MibScalar
hmLEDRSRRedundancyManager = _HmLEDRSRRedundancyManager_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 3, 3),
    _HmLEDRSRRedundancyManager_Type()
)
hmLEDRSRRedundancyManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSRRedundancyManager.setStatus("current")
_HmLEDRSRFault_Type = LEDState
_HmLEDRSRFault_Object = MibScalar
hmLEDRSRFault = _HmLEDRSRFault_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 3, 4),
    _HmLEDRSRFault_Type()
)
hmLEDRSRFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSRFault.setStatus("current")
_HmLEDRSRRelay1_Type = LEDState
_HmLEDRSRRelay1_Object = MibScalar
hmLEDRSRRelay1 = _HmLEDRSRRelay1_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 3, 5),
    _HmLEDRSRRelay1_Type()
)
hmLEDRSRRelay1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSRRelay1.setStatus("current")
_HmLEDRSRRelay2_Type = LEDState
_HmLEDRSRRelay2_Object = MibScalar
hmLEDRSRRelay2 = _HmLEDRSRRelay2_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 35, 3, 6),
    _HmLEDRSRRelay2_Type()
)
hmLEDRSRRelay2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLEDRSRRelay2.setStatus("current")
_HmDIPSwitchGroup_ObjectIdentity = ObjectIdentity
hmDIPSwitchGroup = _HmDIPSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36)
)
_HmDIPSwitchRSGroup_ObjectIdentity = ObjectIdentity
hmDIPSwitchRSGroup = _HmDIPSwitchRSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 1)
)
_HmDIPSwitchRSRedundancyManager_Type = DIPSwitchState
_HmDIPSwitchRSRedundancyManager_Object = MibScalar
hmDIPSwitchRSRedundancyManager = _HmDIPSwitchRSRedundancyManager_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 1, 1),
    _HmDIPSwitchRSRedundancyManager_Type()
)
hmDIPSwitchRSRedundancyManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDIPSwitchRSRedundancyManager.setStatus("current")
_HmDIPSwitchRSStandby_Type = DIPSwitchState
_HmDIPSwitchRSStandby_Object = MibScalar
hmDIPSwitchRSStandby = _HmDIPSwitchRSStandby_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 1, 2),
    _HmDIPSwitchRSStandby_Type()
)
hmDIPSwitchRSStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDIPSwitchRSStandby.setStatus("current")
_HmDIPSwitchMICEGroup_ObjectIdentity = ObjectIdentity
hmDIPSwitchMICEGroup = _HmDIPSwitchMICEGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 2)
)
_HmDIPSwitchMICERedundancyManager_Type = DIPSwitchState
_HmDIPSwitchMICERedundancyManager_Object = MibScalar
hmDIPSwitchMICERedundancyManager = _HmDIPSwitchMICERedundancyManager_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 2, 1),
    _HmDIPSwitchMICERedundancyManager_Type()
)
hmDIPSwitchMICERedundancyManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDIPSwitchMICERedundancyManager.setStatus("current")
_HmDIPSwitchMICERingPort_Type = DIPSwitchState
_HmDIPSwitchMICERingPort_Object = MibScalar
hmDIPSwitchMICERingPort = _HmDIPSwitchMICERingPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 2, 2),
    _HmDIPSwitchMICERingPort_Type()
)
hmDIPSwitchMICERingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDIPSwitchMICERingPort.setStatus("current")
_HmDIPSwitchMICEStandby_Type = DIPSwitchState
_HmDIPSwitchMICEStandby_Object = MibScalar
hmDIPSwitchMICEStandby = _HmDIPSwitchMICEStandby_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 2, 3),
    _HmDIPSwitchMICEStandby_Type()
)
hmDIPSwitchMICEStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDIPSwitchMICEStandby.setStatus("current")
_HmDIPSwitchMICEConfig_Type = DIPSwitchState
_HmDIPSwitchMICEConfig_Object = MibScalar
hmDIPSwitchMICEConfig = _HmDIPSwitchMICEConfig_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 36, 2, 4),
    _HmDIPSwitchMICEConfig_Type()
)
hmDIPSwitchMICEConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDIPSwitchMICEConfig.setStatus("current")
_HmSysMaxTrunks_Type = Integer32
_HmSysMaxTrunks_Object = MibScalar
hmSysMaxTrunks = _HmSysMaxTrunks_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 37),
    _HmSysMaxTrunks_Type()
)
hmSysMaxTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysMaxTrunks.setStatus("current")
_HmLimiterGroup_ObjectIdentity = ObjectIdentity
hmLimiterGroup = _HmLimiterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38)
)
_HmIngressLimiterGroup_ObjectIdentity = ObjectIdentity
hmIngressLimiterGroup = _HmIngressLimiterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 1)
)


class _HmIngressLimiterEnable_Type(Integer32):
    """Custom type hmIngressLimiterEnable based on Integer32"""
    defaultValue = 2

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


_HmIngressLimiterEnable_Type.__name__ = "Integer32"
_HmIngressLimiterEnable_Object = MibScalar
hmIngressLimiterEnable = _HmIngressLimiterEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 1, 1),
    _HmIngressLimiterEnable_Type()
)
hmIngressLimiterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIngressLimiterEnable.setStatus("current")


class _HmIngressLimiterMode_Type(Integer32):
    """Custom type hmIngressLimiterMode based on Integer32"""
    defaultValue = 2

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
        *(("all", 1),
          ("bc", 2),
          ("bc-mc", 3),
          ("bc-mc-uuc", 4))
    )


_HmIngressLimiterMode_Type.__name__ = "Integer32"
_HmIngressLimiterMode_Object = MibScalar
hmIngressLimiterMode = _HmIngressLimiterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 1, 2),
    _HmIngressLimiterMode_Type()
)
hmIngressLimiterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIngressLimiterMode.setStatus("current")
_HmIngressUnknUcLimiterGroup_ObjectIdentity = ObjectIdentity
hmIngressUnknUcLimiterGroup = _HmIngressUnknUcLimiterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 1, 3)
)


class _HmIngressUnknUcLimiterMode_Type(Integer32):
    """Custom type hmIngressUnknUcLimiterMode based on Integer32"""
    defaultValue = 2

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


_HmIngressUnknUcLimiterMode_Type.__name__ = "Integer32"
_HmIngressUnknUcLimiterMode_Object = MibScalar
hmIngressUnknUcLimiterMode = _HmIngressUnknUcLimiterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 1, 3, 1),
    _HmIngressUnknUcLimiterMode_Type()
)
hmIngressUnknUcLimiterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIngressUnknUcLimiterMode.setStatus("current")


class _HmIngressUnknUcLimiterCalculationMode_Type(Integer32):
    """Custom type hmIngressUnknUcLimiterCalculationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytebased", 1),
          ("packetbased", 2))
    )


_HmIngressUnknUcLimiterCalculationMode_Type.__name__ = "Integer32"
_HmIngressUnknUcLimiterCalculationMode_Object = MibScalar
hmIngressUnknUcLimiterCalculationMode = _HmIngressUnknUcLimiterCalculationMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 1, 3, 2),
    _HmIngressUnknUcLimiterCalculationMode_Type()
)
hmIngressUnknUcLimiterCalculationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIngressUnknUcLimiterCalculationMode.setStatus("current")


class _HmIngressUnknUcLimiterRate_Type(Integer32):
    """Custom type hmIngressUnknUcLimiterRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_HmIngressUnknUcLimiterRate_Type.__name__ = "Integer32"
_HmIngressUnknUcLimiterRate_Object = MibScalar
hmIngressUnknUcLimiterRate = _HmIngressUnknUcLimiterRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 1, 3, 3),
    _HmIngressUnknUcLimiterRate_Type()
)
hmIngressUnknUcLimiterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIngressUnknUcLimiterRate.setStatus("current")
_HmEgressLimiterGroup_ObjectIdentity = ObjectIdentity
hmEgressLimiterGroup = _HmEgressLimiterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 2)
)


class _HmEgressLimiterEnable_Type(Integer32):
    """Custom type hmEgressLimiterEnable based on Integer32"""
    defaultValue = 2

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


_HmEgressLimiterEnable_Type.__name__ = "Integer32"
_HmEgressLimiterEnable_Object = MibScalar
hmEgressLimiterEnable = _HmEgressLimiterEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 38, 2, 1),
    _HmEgressLimiterEnable_Type()
)
hmEgressLimiterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmEgressLimiterEnable.setStatus("current")
_HmSysUSBGroup_ObjectIdentity = ObjectIdentity
hmSysUSBGroup = _HmSysUSBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 39)
)
_HmSysMaxUSBPorts_Type = Integer32
_HmSysMaxUSBPorts_Object = MibScalar
hmSysMaxUSBPorts = _HmSysMaxUSBPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 39, 1),
    _HmSysMaxUSBPorts_Type()
)
hmSysMaxUSBPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysMaxUSBPorts.setStatus("current")
_HmSysSwitchGroup_ObjectIdentity = ObjectIdentity
hmSysSwitchGroup = _HmSysSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40)
)


class _HmSysSwitchLearning_Type(Integer32):
    """Custom type hmSysSwitchLearning based on Integer32"""
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


_HmSysSwitchLearning_Type.__name__ = "Integer32"
_HmSysSwitchLearning_Object = MibScalar
hmSysSwitchLearning = _HmSysSwitchLearning_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 1),
    _HmSysSwitchLearning_Type()
)
hmSysSwitchLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchLearning.setStatus("current")


class _HmSysSwitchMRU_Type(Integer32):
    """Custom type hmSysSwitchMRU based on Integer32"""
    defaultValue = 1522

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1522,
              1552,
              1632)
        )
    )
    namedValues = NamedValues(
        *(("size1522", 1522),
          ("size1552", 1552),
          ("size1632", 1632))
    )


_HmSysSwitchMRU_Type.__name__ = "Integer32"
_HmSysSwitchMRU_Object = MibScalar
hmSysSwitchMRU = _HmSysSwitchMRU_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 2),
    _HmSysSwitchMRU_Type()
)
hmSysSwitchMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchMRU.setStatus("current")


class _HmSysSwitchFastLinkDetection_Type(Integer32):
    """Custom type hmSysSwitchFastLinkDetection based on Integer32"""
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


_HmSysSwitchFastLinkDetection_Type.__name__ = "Integer32"
_HmSysSwitchFastLinkDetection_Object = MibScalar
hmSysSwitchFastLinkDetection = _HmSysSwitchFastLinkDetection_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 3),
    _HmSysSwitchFastLinkDetection_Type()
)
hmSysSwitchFastLinkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchFastLinkDetection.setStatus("current")


class _HmSysSwitchAddressRelearnDetection_Type(Integer32):
    """Custom type hmSysSwitchAddressRelearnDetection based on Integer32"""
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


_HmSysSwitchAddressRelearnDetection_Type.__name__ = "Integer32"
_HmSysSwitchAddressRelearnDetection_Object = MibScalar
hmSysSwitchAddressRelearnDetection = _HmSysSwitchAddressRelearnDetection_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 4),
    _HmSysSwitchAddressRelearnDetection_Type()
)
hmSysSwitchAddressRelearnDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchAddressRelearnDetection.setStatus("current")


class _HmSysSwitchAddressRelearnThreshold_Type(Integer32):
    """Custom type hmSysSwitchAddressRelearnThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HmSysSwitchAddressRelearnThreshold_Type.__name__ = "Integer32"
_HmSysSwitchAddressRelearnThreshold_Object = MibScalar
hmSysSwitchAddressRelearnThreshold = _HmSysSwitchAddressRelearnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 5),
    _HmSysSwitchAddressRelearnThreshold_Type()
)
hmSysSwitchAddressRelearnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchAddressRelearnThreshold.setStatus("current")


class _HmSysSwitchDuplexMismatchDetection_Type(Integer32):
    """Custom type hmSysSwitchDuplexMismatchDetection based on Integer32"""
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


_HmSysSwitchDuplexMismatchDetection_Type.__name__ = "Integer32"
_HmSysSwitchDuplexMismatchDetection_Object = MibScalar
hmSysSwitchDuplexMismatchDetection = _HmSysSwitchDuplexMismatchDetection_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 6),
    _HmSysSwitchDuplexMismatchDetection_Type()
)
hmSysSwitchDuplexMismatchDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchDuplexMismatchDetection.setStatus("current")
_HmSysSwitchFDBFullCounter_Type = Counter32
_HmSysSwitchFDBFullCounter_Object = MibScalar
hmSysSwitchFDBFullCounter = _HmSysSwitchFDBFullCounter_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 7),
    _HmSysSwitchFDBFullCounter_Type()
)
hmSysSwitchFDBFullCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSwitchFDBFullCounter.setStatus("current")
_HmSysSwitchFDBHashOptimizingMode_Type = Integer32
_HmSysSwitchFDBHashOptimizingMode_Object = MibScalar
hmSysSwitchFDBHashOptimizingMode = _HmSysSwitchFDBHashOptimizingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 8),
    _HmSysSwitchFDBHashOptimizingMode_Type()
)
hmSysSwitchFDBHashOptimizingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchFDBHashOptimizingMode.setStatus("current")
_HmSysSwitchFDBHashOptimizingStatus_Type = Integer32
_HmSysSwitchFDBHashOptimizingStatus_Object = MibScalar
hmSysSwitchFDBHashOptimizingStatus = _HmSysSwitchFDBHashOptimizingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 9),
    _HmSysSwitchFDBHashOptimizingStatus_Type()
)
hmSysSwitchFDBHashOptimizingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSwitchFDBHashOptimizingStatus.setStatus("current")
_HmSysSwitchVLANGroup_ObjectIdentity = ObjectIdentity
hmSysSwitchVLANGroup = _HmSysSwitchVLANGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 10)
)


class _HmSysSwitchVLANLearningMode_Type(Integer32):
    """Custom type hmSysSwitchVLANLearningMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ivl", 1),
          ("svl", 2))
    )


_HmSysSwitchVLANLearningMode_Type.__name__ = "Integer32"
_HmSysSwitchVLANLearningMode_Object = MibScalar
hmSysSwitchVLANLearningMode = _HmSysSwitchVLANLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 10, 1),
    _HmSysSwitchVLANLearningMode_Type()
)
hmSysSwitchVLANLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchVLANLearningMode.setStatus("current")


class _HmSysSwitchVLANLearningStatus_Type(Integer32):
    """Custom type hmSysSwitchVLANLearningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ivl", 1),
          ("svl", 2))
    )


_HmSysSwitchVLANLearningStatus_Type.__name__ = "Integer32"
_HmSysSwitchVLANLearningStatus_Object = MibScalar
hmSysSwitchVLANLearningStatus = _HmSysSwitchVLANLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 10, 2),
    _HmSysSwitchVLANLearningStatus_Type()
)
hmSysSwitchVLANLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSwitchVLANLearningStatus.setStatus("current")
_HmSysSwitchServiceModeGroup_ObjectIdentity = ObjectIdentity
hmSysSwitchServiceModeGroup = _HmSysSwitchServiceModeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 11)
)


class _HmSysSwitchServiceMode_Type(Integer32):
    """Custom type hmSysSwitchServiceMode based on Integer32"""
    defaultValue = 2

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


_HmSysSwitchServiceMode_Type.__name__ = "Integer32"
_HmSysSwitchServiceMode_Object = MibScalar
hmSysSwitchServiceMode = _HmSysSwitchServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 11, 1),
    _HmSysSwitchServiceMode_Type()
)
hmSysSwitchServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchServiceMode.setStatus("current")
_HmSysSwitchServiceVlan_Type = Integer32
_HmSysSwitchServiceVlan_Object = MibScalar
hmSysSwitchServiceVlan = _HmSysSwitchServiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 11, 2),
    _HmSysSwitchServiceVlan_Type()
)
hmSysSwitchServiceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchServiceVlan.setStatus("current")


class _HmSysSwitchServiceModeOperState_Type(Integer32):
    """Custom type hmSysSwitchServiceModeOperState based on Integer32"""
    defaultValue = 2

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


_HmSysSwitchServiceModeOperState_Type.__name__ = "Integer32"
_HmSysSwitchServiceModeOperState_Object = MibScalar
hmSysSwitchServiceModeOperState = _HmSysSwitchServiceModeOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 11, 3),
    _HmSysSwitchServiceModeOperState_Type()
)
hmSysSwitchServiceModeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSwitchServiceModeOperState.setStatus("current")
_HmSysSwitchRedundancyGroup_ObjectIdentity = ObjectIdentity
hmSysSwitchRedundancyGroup = _HmSysSwitchRedundancyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 20)
)


class _HmSysSwitchRedundancyRstpMrpMode_Type(Integer32):
    """Custom type hmSysSwitchRedundancyRstpMrpMode based on Integer32"""
    defaultValue = 2

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


_HmSysSwitchRedundancyRstpMrpMode_Type.__name__ = "Integer32"
_HmSysSwitchRedundancyRstpMrpMode_Object = MibScalar
hmSysSwitchRedundancyRstpMrpMode = _HmSysSwitchRedundancyRstpMrpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 20, 1),
    _HmSysSwitchRedundancyRstpMrpMode_Type()
)
hmSysSwitchRedundancyRstpMrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSwitchRedundancyRstpMrpMode.setStatus("current")


class _HmSysSwitchRedundancyRstpMrpConfigError_Type(TruthValue):
    """Custom type hmSysSwitchRedundancyRstpMrpConfigError based on TruthValue"""


_HmSysSwitchRedundancyRstpMrpConfigError_Object = MibScalar
hmSysSwitchRedundancyRstpMrpConfigError = _HmSysSwitchRedundancyRstpMrpConfigError_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 20, 2),
    _HmSysSwitchRedundancyRstpMrpConfigError_Type()
)
hmSysSwitchRedundancyRstpMrpConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSwitchRedundancyRstpMrpConfigError.setStatus("current")
_HmSysSwitchRedundancyRstpMrpConfigErrorBridge_Type = BridgeIdOrNull
_HmSysSwitchRedundancyRstpMrpConfigErrorBridge_Object = MibScalar
hmSysSwitchRedundancyRstpMrpConfigErrorBridge = _HmSysSwitchRedundancyRstpMrpConfigErrorBridge_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 40, 20, 3),
    _HmSysSwitchRedundancyRstpMrpConfigErrorBridge_Type()
)
hmSysSwitchRedundancyRstpMrpConfigErrorBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSwitchRedundancyRstpMrpConfigErrorBridge.setStatus("current")
_HmSysSelftestGroup_ObjectIdentity = ObjectIdentity
hmSysSelftestGroup = _HmSysSelftestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 41)
)


class _HmSysSelftestRAM_Type(Integer32):
    """Custom type hmSysSelftestRAM based on Integer32"""
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


_HmSysSelftestRAM_Type.__name__ = "Integer32"
_HmSysSelftestRAM_Object = MibScalar
hmSysSelftestRAM = _HmSysSelftestRAM_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 41, 1),
    _HmSysSelftestRAM_Type()
)
hmSysSelftestRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSelftestRAM.setStatus("current")


class _HmSysSelftestRebootOnError_Type(Integer32):
    """Custom type hmSysSelftestRebootOnError based on Integer32"""
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


_HmSysSelftestRebootOnError_Type.__name__ = "Integer32"
_HmSysSelftestRebootOnError_Object = MibScalar
hmSysSelftestRebootOnError = _HmSysSelftestRebootOnError_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 41, 2),
    _HmSysSelftestRebootOnError_Type()
)
hmSysSelftestRebootOnError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSelftestRebootOnError.setStatus("current")


class _HmSysSelftestMMUStatus_Type(Integer32):
    """Custom type hmSysSelftestMMUStatus based on Integer32"""
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


_HmSysSelftestMMUStatus_Type.__name__ = "Integer32"
_HmSysSelftestMMUStatus_Object = MibScalar
hmSysSelftestMMUStatus = _HmSysSelftestMMUStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 41, 3),
    _HmSysSelftestMMUStatus_Type()
)
hmSysSelftestMMUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysSelftestMMUStatus.setStatus("current")


class _HmSysSelftestRebootOnHdxError_Type(Integer32):
    """Custom type hmSysSelftestRebootOnHdxError based on Integer32"""
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


_HmSysSelftestRebootOnHdxError_Type.__name__ = "Integer32"
_HmSysSelftestRebootOnHdxError_Object = MibScalar
hmSysSelftestRebootOnHdxError = _HmSysSelftestRebootOnHdxError_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 41, 4),
    _HmSysSelftestRebootOnHdxError_Type()
)
hmSysSelftestRebootOnHdxError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSelftestRebootOnHdxError.setStatus("current")
_HmSysOEMGroup_ObjectIdentity = ObjectIdentity
hmSysOEMGroup = _HmSysOEMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 42)
)
_HmSysOEMID_Type = Integer32
_HmSysOEMID_Object = MibScalar
hmSysOEMID = _HmSysOEMID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 42, 1),
    _HmSysOEMID_Type()
)
hmSysOEMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysOEMID.setStatus("current")
_HmSysMaxSignalContacts_Type = Integer32
_HmSysMaxSignalContacts_Object = MibScalar
hmSysMaxSignalContacts = _HmSysMaxSignalContacts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 43),
    _HmSysMaxSignalContacts_Type()
)
hmSysMaxSignalContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSysMaxSignalContacts.setStatus("current")


class _HmSysHttpsEnable_Type(Integer32):
    """Custom type hmSysHttpsEnable based on Integer32"""
    defaultValue = 2

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


_HmSysHttpsEnable_Type.__name__ = "Integer32"
_HmSysHttpsEnable_Object = MibScalar
hmSysHttpsEnable = _HmSysHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 44),
    _HmSysHttpsEnable_Type()
)
hmSysHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysHttpsEnable.setStatus("current")


class _HmSysHttpsPortNumber_Type(Integer32):
    """Custom type hmSysHttpsPortNumber based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmSysHttpsPortNumber_Type.__name__ = "Integer32"
_HmSysHttpsPortNumber_Object = MibScalar
hmSysHttpsPortNumber = _HmSysHttpsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 45),
    _HmSysHttpsPortNumber_Type()
)
hmSysHttpsPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysHttpsPortNumber.setStatus("current")


class _HmSysSkipAcaOnBoot_Type(Integer32):
    """Custom type hmSysSkipAcaOnBoot based on Integer32"""
    defaultValue = 2

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


_HmSysSkipAcaOnBoot_Type.__name__ = "Integer32"
_HmSysSkipAcaOnBoot_Object = MibScalar
hmSysSkipAcaOnBoot = _HmSysSkipAcaOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 1, 46),
    _HmSysSkipAcaOnBoot_Type()
)
hmSysSkipAcaOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSysSkipAcaOnBoot.setStatus("current")
_HmPSTable_Object = MibTable
hmPSTable = _HmPSTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2)
)
if mibBuilder.loadTexts:
    hmPSTable.setStatus("current")
_HmPSEntry_Object = MibTableRow
hmPSEntry = _HmPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1)
)
hmPSEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPSSysID"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPSID"),
)
if mibBuilder.loadTexts:
    hmPSEntry.setStatus("current")


class _HmPSSysID_Type(Integer32):
    """Custom type hmPSSysID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HmPSSysID_Type.__name__ = "Integer32"
_HmPSSysID_Object = MibTableColumn
hmPSSysID = _HmPSSysID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 1),
    _HmPSSysID_Type()
)
hmPSSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSSysID.setStatus("current")


class _HmPSID_Type(Integer32):
    """Custom type hmPSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmPSID_Type.__name__ = "Integer32"
_HmPSID_Object = MibTableColumn
hmPSID = _HmPSID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 2),
    _HmPSID_Type()
)
hmPSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSID.setStatus("current")


class _HmPSState_Type(Integer32):
    """Custom type hmPSState based on Integer32"""
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
        *(("failed", 2),
          ("notInstalled", 3),
          ("ok", 1),
          ("unknown", 4))
    )


_HmPSState_Type.__name__ = "Integer32"
_HmPSState_Object = MibTableColumn
hmPSState = _HmPSState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 3),
    _HmPSState_Type()
)
hmPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSState.setStatus("current")


class _HmPSType_Type(Integer32):
    """Custom type hmPSType based on Integer32"""
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
        *(("ac-dc", 2),
          ("dc-dc-24v-1", 3),
          ("dc-dc-24v-2", 5),
          ("dc-dc-48v-1", 4),
          ("dc-dc-48v-2", 6),
          ("unknown", 1))
    )


_HmPSType_Type.__name__ = "Integer32"
_HmPSType_Object = MibTableColumn
hmPSType = _HmPSType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 4),
    _HmPSType_Type()
)
hmPSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSType.setStatus("current")
_HmPSVersion_Type = Integer32
_HmPSVersion_Object = MibTableColumn
hmPSVersion = _HmPSVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 5),
    _HmPSVersion_Type()
)
hmPSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSVersion.setStatus("current")
_HmPSDescription_Type = DisplayString
_HmPSDescription_Object = MibTableColumn
hmPSDescription = _HmPSDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 6),
    _HmPSDescription_Type()
)
hmPSDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSDescription.setStatus("current")
_HmPSSerialNumber_Type = DisplayString
_HmPSSerialNumber_Object = MibTableColumn
hmPSSerialNumber = _HmPSSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 7),
    _HmPSSerialNumber_Type()
)
hmPSSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSSerialNumber.setStatus("current")
_HmPSProductCode_Type = DisplayString
_HmPSProductCode_Object = MibTableColumn
hmPSProductCode = _HmPSProductCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 8),
    _HmPSProductCode_Type()
)
hmPSProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSProductCode.setStatus("current")
_HmPSPowerBudget_Type = Integer32
_HmPSPowerBudget_Object = MibTableColumn
hmPSPowerBudget = _HmPSPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 2, 1, 9),
    _HmPSPowerBudget_Type()
)
hmPSPowerBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPSPowerBudget.setStatus("current")
_HmFanTable_Object = MibTable
hmFanTable = _HmFanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 3)
)
if mibBuilder.loadTexts:
    hmFanTable.setStatus("current")
_HmFanEntry_Object = MibTableRow
hmFanEntry = _HmFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 3, 1)
)
hmFanEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmFanSysID"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmFanID"),
)
if mibBuilder.loadTexts:
    hmFanEntry.setStatus("current")


class _HmFanSysID_Type(Integer32):
    """Custom type hmFanSysID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HmFanSysID_Type.__name__ = "Integer32"
_HmFanSysID_Object = MibTableColumn
hmFanSysID = _HmFanSysID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 3, 1, 1),
    _HmFanSysID_Type()
)
hmFanSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFanSysID.setStatus("current")


class _HmFanID_Type(Integer32):
    """Custom type hmFanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HmFanID_Type.__name__ = "Integer32"
_HmFanID_Object = MibTableColumn
hmFanID = _HmFanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 3, 1, 2),
    _HmFanID_Type()
)
hmFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFanID.setStatus("current")


class _HmFanState_Type(Integer32):
    """Custom type hmFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_HmFanState_Type.__name__ = "Integer32"
_HmFanState_Object = MibTableColumn
hmFanState = _HmFanState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 3, 1, 3),
    _HmFanState_Type()
)
hmFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFanState.setStatus("current")
_HmFwdPriorityConfiguration_ObjectIdentity = ObjectIdentity
hmFwdPriorityConfiguration = _HmFwdPriorityConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4)
)


class _HmPrioTOSEnable_Type(Integer32):
    """Custom type hmPrioTOSEnable based on Integer32"""
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


_HmPrioTOSEnable_Type.__name__ = "Integer32"
_HmPrioTOSEnable_Object = MibScalar
hmPrioTOSEnable = _HmPrioTOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 1),
    _HmPrioTOSEnable_Type()
)
hmPrioTOSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPrioTOSEnable.setStatus("current")


class _HmPrioMACAddressEnable_Type(Integer32):
    """Custom type hmPrioMACAddressEnable based on Integer32"""
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


_HmPrioMACAddressEnable_Type.__name__ = "Integer32"
_HmPrioMACAddressEnable_Object = MibScalar
hmPrioMACAddressEnable = _HmPrioMACAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 2),
    _HmPrioMACAddressEnable_Type()
)
hmPrioMACAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPrioMACAddressEnable.setStatus("current")


class _HmPrioVlan0TagTransparentMode_Type(Integer32):
    """Custom type hmPrioVlan0TagTransparentMode based on Integer32"""
    defaultValue = 2

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


_HmPrioVlan0TagTransparentMode_Type.__name__ = "Integer32"
_HmPrioVlan0TagTransparentMode_Object = MibScalar
hmPrioVlan0TagTransparentMode = _HmPrioVlan0TagTransparentMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 3),
    _HmPrioVlan0TagTransparentMode_Type()
)
hmPrioVlan0TagTransparentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPrioVlan0TagTransparentMode.setStatus("current")
_HmPrioMACAddressTable_Object = MibTable
hmPrioMACAddressTable = _HmPrioMACAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 10)
)
if mibBuilder.loadTexts:
    hmPrioMACAddressTable.setStatus("current")
_HmPrioMACAddressEntry_Object = MibTableRow
hmPrioMACAddressEntry = _HmPrioMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 10, 1)
)
hmPrioMACAddressEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPrioMACAddress"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPrioMACReceivePort"),
)
if mibBuilder.loadTexts:
    hmPrioMACAddressEntry.setStatus("current")
_HmPrioMACAddress_Type = MacAddress
_HmPrioMACAddress_Object = MibTableColumn
hmPrioMACAddress = _HmPrioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 10, 1, 1),
    _HmPrioMACAddress_Type()
)
hmPrioMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPrioMACAddress.setStatus("current")


class _HmPrioMACReceivePort_Type(Integer32):
    """Custom type hmPrioMACReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmPrioMACReceivePort_Type.__name__ = "Integer32"
_HmPrioMACReceivePort_Object = MibTableColumn
hmPrioMACReceivePort = _HmPrioMACReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 10, 1, 2),
    _HmPrioMACReceivePort_Type()
)
hmPrioMACReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPrioMACReceivePort.setStatus("current")


class _HmPrioMACPriority_Type(Integer32):
    """Custom type hmPrioMACPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_HmPrioMACPriority_Type.__name__ = "Integer32"
_HmPrioMACPriority_Object = MibTableColumn
hmPrioMACPriority = _HmPrioMACPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 10, 1, 3),
    _HmPrioMACPriority_Type()
)
hmPrioMACPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPrioMACPriority.setStatus("current")


class _HmPrioMACStatus_Type(Integer32):
    """Custom type hmPrioMACStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_HmPrioMACStatus_Type.__name__ = "Integer32"
_HmPrioMACStatus_Object = MibTableColumn
hmPrioMACStatus = _HmPrioMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 10, 1, 4),
    _HmPrioMACStatus_Type()
)
hmPrioMACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPrioMACStatus.setStatus("current")
_HmPrioTrafficClassTable_Object = MibTable
hmPrioTrafficClassTable = _HmPrioTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 11)
)
if mibBuilder.loadTexts:
    hmPrioTrafficClassTable.setStatus("current")
_HmPrioTrafficClassEntry_Object = MibTableRow
hmPrioTrafficClassEntry = _HmPrioTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 11, 1)
)
hmPrioTrafficClassEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPrioTrafficClassID"),
)
if mibBuilder.loadTexts:
    hmPrioTrafficClassEntry.setStatus("current")


class _HmPrioTrafficClassID_Type(Integer32):
    """Custom type hmPrioTrafficClassID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HmPrioTrafficClassID_Type.__name__ = "Integer32"
_HmPrioTrafficClassID_Object = MibTableColumn
hmPrioTrafficClassID = _HmPrioTrafficClassID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 11, 1, 1),
    _HmPrioTrafficClassID_Type()
)
hmPrioTrafficClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPrioTrafficClassID.setStatus("current")


class _HmPrioTrafficClassWeight_Type(Integer32):
    """Custom type hmPrioTrafficClassWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_HmPrioTrafficClassWeight_Type.__name__ = "Integer32"
_HmPrioTrafficClassWeight_Object = MibTableColumn
hmPrioTrafficClassWeight = _HmPrioTrafficClassWeight_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 11, 1, 2),
    _HmPrioTrafficClassWeight_Type()
)
hmPrioTrafficClassWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPrioTrafficClassWeight.setStatus("current")
_HmPrioTosToPrioTable_Object = MibTable
hmPrioTosToPrioTable = _HmPrioTosToPrioTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 12)
)
if mibBuilder.loadTexts:
    hmPrioTosToPrioTable.setStatus("current")
_HmPrioTosToPrioEntry_Object = MibTableRow
hmPrioTosToPrioEntry = _HmPrioTosToPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 12, 1)
)
hmPrioTosToPrioEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPrioTTPTos"),
)
if mibBuilder.loadTexts:
    hmPrioTosToPrioEntry.setStatus("current")


class _HmPrioTTPTos_Type(Integer32):
    """Custom type hmPrioTTPTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmPrioTTPTos_Type.__name__ = "Integer32"
_HmPrioTTPTos_Object = MibTableColumn
hmPrioTTPTos = _HmPrioTTPTos_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 12, 1, 1),
    _HmPrioTTPTos_Type()
)
hmPrioTTPTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPrioTTPTos.setStatus("current")


class _HmPrioTTPPrio_Type(Integer32):
    """Custom type hmPrioTTPPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmPrioTTPPrio_Type.__name__ = "Integer32"
_HmPrioTTPPrio_Object = MibTableColumn
hmPrioTTPPrio = _HmPrioTTPPrio_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 4, 12, 1, 2),
    _HmPrioTTPPrio_Type()
)
hmPrioTTPPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPrioTTPPrio.setStatus("current")
_HmCurrentAddressTable_Object = MibTable
hmCurrentAddressTable = _HmCurrentAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 5)
)
if mibBuilder.loadTexts:
    hmCurrentAddressTable.setStatus("current")
_HmCurrentAddressEntry_Object = MibTableRow
hmCurrentAddressEntry = _HmCurrentAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 5, 1)
)
hmCurrentAddressEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmCurrentAddress"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmCurrentAddressReceivePort"),
)
if mibBuilder.loadTexts:
    hmCurrentAddressEntry.setStatus("current")
_HmCurrentAddress_Type = MacAddress
_HmCurrentAddress_Object = MibTableColumn
hmCurrentAddress = _HmCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 5, 1, 1),
    _HmCurrentAddress_Type()
)
hmCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCurrentAddress.setStatus("current")


class _HmCurrentAddressReceivePort_Type(Integer32):
    """Custom type hmCurrentAddressReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmCurrentAddressReceivePort_Type.__name__ = "Integer32"
_HmCurrentAddressReceivePort_Object = MibTableColumn
hmCurrentAddressReceivePort = _HmCurrentAddressReceivePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 5, 1, 2),
    _HmCurrentAddressReceivePort_Type()
)
hmCurrentAddressReceivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCurrentAddressReceivePort.setStatus("current")
_HmCurrentAddressStaticEgressPorts_Type = OctetString
_HmCurrentAddressStaticEgressPorts_Object = MibTableColumn
hmCurrentAddressStaticEgressPorts = _HmCurrentAddressStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 5, 1, 3),
    _HmCurrentAddressStaticEgressPorts_Type()
)
hmCurrentAddressStaticEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCurrentAddressStaticEgressPorts.setStatus("current")
_HmCurrentAddressEgressPorts_Type = OctetString
_HmCurrentAddressEgressPorts_Object = MibTableColumn
hmCurrentAddressEgressPorts = _HmCurrentAddressEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 5, 1, 4),
    _HmCurrentAddressEgressPorts_Type()
)
hmCurrentAddressEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCurrentAddressEgressPorts.setStatus("current")


class _HmCurrentAddressStatus_Type(Integer32):
    """Custom type hmCurrentAddressStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_HmCurrentAddressStatus_Type.__name__ = "Integer32"
_HmCurrentAddressStatus_Object = MibTableColumn
hmCurrentAddressStatus = _HmCurrentAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 5, 1, 5),
    _HmCurrentAddressStatus_Type()
)
hmCurrentAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCurrentAddressStatus.setStatus("current")
_HmRS2ext_ObjectIdentity = ObjectIdentity
hmRS2ext = _HmRS2ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10)
)


class _HmRS2OperMode_Type(Integer32):
    """Custom type hmRS2OperMode based on Integer32"""
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
        *(("normal", 1),
          ("redundancy-manager-active", 4),
          ("redundancy-manager-inactive", 5),
          ("standby-active", 2),
          ("standby-inactive", 3))
    )


_HmRS2OperMode_Type.__name__ = "Integer32"
_HmRS2OperMode_Object = MibScalar
hmRS2OperMode = _HmRS2OperMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 1),
    _HmRS2OperMode_Type()
)
hmRS2OperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRS2OperMode.setStatus("current")


class _HmRS2ConfigError_Type(Integer32):
    """Custom type hmRS2ConfigError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("no-error", 1))
    )


_HmRS2ConfigError_Type.__name__ = "Integer32"
_HmRS2ConfigError_Object = MibScalar
hmRS2ConfigError = _HmRS2ConfigError_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 2),
    _HmRS2ConfigError_Type()
)
hmRS2ConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRS2ConfigError.setStatus("current")


class _HmRS2SigRelayState_Type(Integer32):
    """Custom type hmRS2SigRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HmRS2SigRelayState_Type.__name__ = "Integer32"
_HmRS2SigRelayState_Object = MibScalar
hmRS2SigRelayState = _HmRS2SigRelayState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 3),
    _HmRS2SigRelayState_Type()
)
hmRS2SigRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRS2SigRelayState.setStatus("current")
_HmSigLinkTable_Object = MibTable
hmSigLinkTable = _HmSigLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 4)
)
if mibBuilder.loadTexts:
    hmSigLinkTable.setStatus("current")
_HmSigLinkEntry_Object = MibTableRow
hmSigLinkEntry = _HmSigLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 4, 1)
)
hmSigLinkEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSigLinkID"),
)
if mibBuilder.loadTexts:
    hmSigLinkEntry.setStatus("current")


class _HmSigLinkID_Type(Integer32):
    """Custom type hmSigLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmSigLinkID_Type.__name__ = "Integer32"
_HmSigLinkID_Object = MibTableColumn
hmSigLinkID = _HmSigLinkID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 4, 1, 1),
    _HmSigLinkID_Type()
)
hmSigLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigLinkID.setStatus("current")


class _HmSigLinkAlarm_Type(Integer32):
    """Custom type hmSigLinkAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HmSigLinkAlarm_Type.__name__ = "Integer32"
_HmSigLinkAlarm_Object = MibTableColumn
hmSigLinkAlarm = _HmSigLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 4, 1, 2),
    _HmSigLinkAlarm_Type()
)
hmSigLinkAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigLinkAlarm.setStatus("current")
_HmSigTrapReason_Type = ObjectIdentifier
_HmSigTrapReason_Object = MibScalar
hmSigTrapReason = _HmSigTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 5),
    _HmSigTrapReason_Type()
)
hmSigTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigTrapReason.setStatus("current")
_HmSigReasonIndex_Type = Integer32
_HmSigReasonIndex_Object = MibScalar
hmSigReasonIndex = _HmSigReasonIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 6),
    _HmSigReasonIndex_Type()
)
hmSigReasonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigReasonIndex.setStatus("current")
_HmRS2TopologyGroup_ObjectIdentity = ObjectIdentity
hmRS2TopologyGroup = _HmRS2TopologyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 7)
)
_HmRS2PartnerIpAddress_Type = IpAddress
_HmRS2PartnerIpAddress_Object = MibScalar
hmRS2PartnerIpAddress = _HmRS2PartnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 7, 1),
    _HmRS2PartnerIpAddress_Type()
)
hmRS2PartnerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2PartnerIpAddress.setStatus("current")
_HmRS2TopologyTable_Object = MibTable
hmRS2TopologyTable = _HmRS2TopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    hmRS2TopologyTable.setStatus("current")
_HmRS2TopologyEntry_Object = MibTableRow
hmRS2TopologyEntry = _HmRS2TopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 7, 2, 1)
)
hmRS2TopologyEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmRS2TopologyLinkID"),
)
if mibBuilder.loadTexts:
    hmRS2TopologyEntry.setStatus("current")


class _HmRS2TopologyLinkID_Type(Integer32):
    """Custom type hmRS2TopologyLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmRS2TopologyLinkID_Type.__name__ = "Integer32"
_HmRS2TopologyLinkID_Object = MibTableColumn
hmRS2TopologyLinkID = _HmRS2TopologyLinkID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 7, 2, 1, 1),
    _HmRS2TopologyLinkID_Type()
)
hmRS2TopologyLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRS2TopologyLinkID.setStatus("current")
_HmRS2TopologyIpAddress_Type = IpAddress
_HmRS2TopologyIpAddress_Object = MibTableColumn
hmRS2TopologyIpAddress = _HmRS2TopologyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 7, 2, 1, 2),
    _HmRS2TopologyIpAddress_Type()
)
hmRS2TopologyIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2TopologyIpAddress.setStatus("current")
_HmRS2ConnectionMirroringGroup_ObjectIdentity = ObjectIdentity
hmRS2ConnectionMirroringGroup = _HmRS2ConnectionMirroringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 8)
)


class _HmRS2ConnectionMirroringStatus_Type(Integer32):
    """Custom type hmRS2ConnectionMirroringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HmRS2ConnectionMirroringStatus_Type.__name__ = "Integer32"
_HmRS2ConnectionMirroringStatus_Object = MibScalar
hmRS2ConnectionMirroringStatus = _HmRS2ConnectionMirroringStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 8, 1),
    _HmRS2ConnectionMirroringStatus_Type()
)
hmRS2ConnectionMirroringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2ConnectionMirroringStatus.setStatus("current")
_HmRS2ConnectionMirroringPortOne_Type = Integer32
_HmRS2ConnectionMirroringPortOne_Object = MibScalar
hmRS2ConnectionMirroringPortOne = _HmRS2ConnectionMirroringPortOne_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 8, 2),
    _HmRS2ConnectionMirroringPortOne_Type()
)
hmRS2ConnectionMirroringPortOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2ConnectionMirroringPortOne.setStatus("current")
_HmRS2ConnectionMirroringPortTwo_Type = Integer32
_HmRS2ConnectionMirroringPortTwo_Object = MibScalar
hmRS2ConnectionMirroringPortTwo = _HmRS2ConnectionMirroringPortTwo_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 8, 3),
    _HmRS2ConnectionMirroringPortTwo_Type()
)
hmRS2ConnectionMirroringPortTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2ConnectionMirroringPortTwo.setStatus("current")
_HmRS2DisableLearningGroup_ObjectIdentity = ObjectIdentity
hmRS2DisableLearningGroup = _HmRS2DisableLearningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 9)
)


class _HmRS2DisableLearningStatus_Type(Integer32):
    """Custom type hmRS2DisableLearningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HmRS2DisableLearningStatus_Type.__name__ = "Integer32"
_HmRS2DisableLearningStatus_Object = MibScalar
hmRS2DisableLearningStatus = _HmRS2DisableLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 9, 1),
    _HmRS2DisableLearningStatus_Type()
)
hmRS2DisableLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2DisableLearningStatus.setStatus("current")
_HmRS2SigRelayGroup_ObjectIdentity = ObjectIdentity
hmRS2SigRelayGroup = _HmRS2SigRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 10)
)


class _HmRS2SigRelayMode_Type(Integer32):
    """Custom type hmRS2SigRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("standard", 1))
    )


_HmRS2SigRelayMode_Type.__name__ = "Integer32"
_HmRS2SigRelayMode_Object = MibScalar
hmRS2SigRelayMode = _HmRS2SigRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 10, 1),
    _HmRS2SigRelayMode_Type()
)
hmRS2SigRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2SigRelayMode.setStatus("current")


class _HmRS2SigRelayManualState_Type(Integer32):
    """Custom type hmRS2SigRelayManualState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HmRS2SigRelayManualState_Type.__name__ = "Integer32"
_HmRS2SigRelayManualState_Object = MibScalar
hmRS2SigRelayManualState = _HmRS2SigRelayManualState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 10, 2),
    _HmRS2SigRelayManualState_Type()
)
hmRS2SigRelayManualState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2SigRelayManualState.setStatus("current")
_HmRS2VlanGroup_ObjectIdentity = ObjectIdentity
hmRS2VlanGroup = _HmRS2VlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 11)
)


class _HmRS2VlanMode_Type(Integer32):
    """Custom type hmRS2VlanMode based on Integer32"""
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


_HmRS2VlanMode_Type.__name__ = "Integer32"
_HmRS2VlanMode_Object = MibScalar
hmRS2VlanMode = _HmRS2VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 11, 1),
    _HmRS2VlanMode_Type()
)
hmRS2VlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2VlanMode.setStatus("current")


class _HmRS2VlanStatus_Type(Integer32):
    """Custom type hmRS2VlanStatus based on Integer32"""
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


_HmRS2VlanStatus_Type.__name__ = "Integer32"
_HmRS2VlanStatus_Object = MibScalar
hmRS2VlanStatus = _HmRS2VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 11, 2),
    _HmRS2VlanStatus_Type()
)
hmRS2VlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRS2VlanStatus.setStatus("current")
_HmRS2SelftestGroup_ObjectIdentity = ObjectIdentity
hmRS2SelftestGroup = _HmRS2SelftestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 12)
)
_HmRS2SelftestResult_Type = Integer32
_HmRS2SelftestResult_Object = MibScalar
hmRS2SelftestResult = _HmRS2SelftestResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 12, 1),
    _HmRS2SelftestResult_Type()
)
hmRS2SelftestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRS2SelftestResult.setStatus("current")
_HmRS2SelftestMode_Type = Integer32
_HmRS2SelftestMode_Object = MibScalar
hmRS2SelftestMode = _HmRS2SelftestMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 12, 2),
    _HmRS2SelftestMode_Type()
)
hmRS2SelftestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2SelftestMode.setStatus("current")
_HmRS2PSGroup_ObjectIdentity = ObjectIdentity
hmRS2PSGroup = _HmRS2PSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 13)
)


class _HmRS2PSAlarm_Type(Integer32):
    """Custom type hmRS2PSAlarm based on Integer32"""
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


_HmRS2PSAlarm_Type.__name__ = "Integer32"
_HmRS2PSAlarm_Object = MibScalar
hmRS2PSAlarm = _HmRS2PSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 13, 1),
    _HmRS2PSAlarm_Type()
)
hmRS2PSAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2PSAlarm.setStatus("current")
_HmRS2RedundancyGroup_ObjectIdentity = ObjectIdentity
hmRS2RedundancyGroup = _HmRS2RedundancyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 14)
)


class _HmRS2RedNotGuaranteedAlarm_Type(Integer32):
    """Custom type hmRS2RedNotGuaranteedAlarm based on Integer32"""
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


_HmRS2RedNotGuaranteedAlarm_Type.__name__ = "Integer32"
_HmRS2RedNotGuaranteedAlarm_Object = MibScalar
hmRS2RedNotGuaranteedAlarm = _HmRS2RedNotGuaranteedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 14, 1),
    _HmRS2RedNotGuaranteedAlarm_Type()
)
hmRS2RedNotGuaranteedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2RedNotGuaranteedAlarm.setStatus("current")
_HmRS4RGroup_ObjectIdentity = ObjectIdentity
hmRS4RGroup = _HmRS4RGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 15)
)
_HmRS4RVlanGroup_ObjectIdentity = ObjectIdentity
hmRS4RVlanGroup = _HmRS4RVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 15, 1)
)
_HmRS4RVlanPortTable_Object = MibTable
hmRS4RVlanPortTable = _HmRS4RVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 15, 1, 1)
)
if mibBuilder.loadTexts:
    hmRS4RVlanPortTable.setStatus("current")
_HmRS4RVlanPortEntry_Object = MibTableRow
hmRS4RVlanPortEntry = _HmRS4RVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 15, 1, 1, 1)
)
hmRS4RVlanPortEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmRS4RVlanPortID"),
)
if mibBuilder.loadTexts:
    hmRS4RVlanPortEntry.setStatus("current")


class _HmRS4RVlanPortID_Type(Integer32):
    """Custom type hmRS4RVlanPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HmRS4RVlanPortID_Type.__name__ = "Integer32"
_HmRS4RVlanPortID_Object = MibTableColumn
hmRS4RVlanPortID = _HmRS4RVlanPortID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 15, 1, 1, 1, 1),
    _HmRS4RVlanPortID_Type()
)
hmRS4RVlanPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmRS4RVlanPortID.setStatus("current")


class _HmRS4RVlanPortTagFormatRstp_Type(Integer32):
    """Custom type hmRS4RVlanPortTagFormatRstp based on Integer32"""
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


_HmRS4RVlanPortTagFormatRstp_Type.__name__ = "Integer32"
_HmRS4RVlanPortTagFormatRstp_Object = MibTableColumn
hmRS4RVlanPortTagFormatRstp = _HmRS4RVlanPortTagFormatRstp_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 15, 1, 1, 1, 2),
    _HmRS4RVlanPortTagFormatRstp_Type()
)
hmRS4RVlanPortTagFormatRstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS4RVlanPortTagFormatRstp.setStatus("current")
_HmRS2FDBGroup_ObjectIdentity = ObjectIdentity
hmRS2FDBGroup = _HmRS2FDBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 16)
)
_HmRS2FDBHashGroup_ObjectIdentity = ObjectIdentity
hmRS2FDBHashGroup = _HmRS2FDBHashGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 16, 1)
)


class _HmRS2FDBHashOptimizingMode_Type(Integer32):
    """Custom type hmRS2FDBHashOptimizingMode based on Integer32"""
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


_HmRS2FDBHashOptimizingMode_Type.__name__ = "Integer32"
_HmRS2FDBHashOptimizingMode_Object = MibScalar
hmRS2FDBHashOptimizingMode = _HmRS2FDBHashOptimizingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 16, 1, 1),
    _HmRS2FDBHashOptimizingMode_Type()
)
hmRS2FDBHashOptimizingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRS2FDBHashOptimizingMode.setStatus("current")


class _HmRS2FDBHashOptimizingStatus_Type(Integer32):
    """Custom type hmRS2FDBHashOptimizingStatus based on Integer32"""
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


_HmRS2FDBHashOptimizingStatus_Type.__name__ = "Integer32"
_HmRS2FDBHashOptimizingStatus_Object = MibScalar
hmRS2FDBHashOptimizingStatus = _HmRS2FDBHashOptimizingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 10, 16, 1, 2),
    _HmRS2FDBHashOptimizingStatus_Type()
)
hmRS2FDBHashOptimizingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRS2FDBHashOptimizingStatus.setStatus("current")
_HmMACH3ChassisExt_ObjectIdentity = ObjectIdentity
hmMACH3ChassisExt = _HmMACH3ChassisExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11)
)
_HmSelfTestResults_ObjectIdentity = ObjectIdentity
hmSelfTestResults = _HmSelfTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1)
)
_HmSelfTestCpuResult_Type = Integer32
_HmSelfTestCpuResult_Object = MibScalar
hmSelfTestCpuResult = _HmSelfTestCpuResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 1),
    _HmSelfTestCpuResult_Type()
)
hmSelfTestCpuResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSelfTestCpuResult.setStatus("current")
_HmSelfTestBBResult_Type = Integer32
_HmSelfTestBBResult_Object = MibScalar
hmSelfTestBBResult = _HmSelfTestBBResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 2),
    _HmSelfTestBBResult_Type()
)
hmSelfTestBBResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSelfTestBBResult.setStatus("current")
_HmSelfTestBPResult_Type = Integer32
_HmSelfTestBPResult_Object = MibScalar
hmSelfTestBPResult = _HmSelfTestBPResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 3),
    _HmSelfTestBPResult_Type()
)
hmSelfTestBPResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSelfTestBPResult.setStatus("current")
_HmSelfTestM1Result_Type = Integer32
_HmSelfTestM1Result_Object = MibScalar
hmSelfTestM1Result = _HmSelfTestM1Result_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 4),
    _HmSelfTestM1Result_Type()
)
hmSelfTestM1Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSelfTestM1Result.setStatus("current")
_HmSelfTestM2Result_Type = Integer32
_HmSelfTestM2Result_Object = MibScalar
hmSelfTestM2Result = _HmSelfTestM2Result_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 5),
    _HmSelfTestM2Result_Type()
)
hmSelfTestM2Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSelfTestM2Result.setStatus("current")
_HmSelfTestM3Result_Type = Integer32
_HmSelfTestM3Result_Object = MibScalar
hmSelfTestM3Result = _HmSelfTestM3Result_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 6),
    _HmSelfTestM3Result_Type()
)
hmSelfTestM3Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSelfTestM3Result.setStatus("current")
_HmSelfTestM4Result_Type = Integer32
_HmSelfTestM4Result_Object = MibScalar
hmSelfTestM4Result = _HmSelfTestM4Result_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 7),
    _HmSelfTestM4Result_Type()
)
hmSelfTestM4Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSelfTestM4Result.setStatus("current")


class _HmSelfTestMode_Type(Integer32):
    """Custom type hmSelfTestMode based on Integer32"""
    defaultValue = 2

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


_HmSelfTestMode_Type.__name__ = "Integer32"
_HmSelfTestMode_Object = MibScalar
hmSelfTestMode = _HmSelfTestMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 1, 8),
    _HmSelfTestMode_Type()
)
hmSelfTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSelfTestMode.setStatus("current")


class _HmMgmtBusSelected_Type(Integer32):
    """Custom type hmMgmtBusSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("redundant", 2))
    )


_HmMgmtBusSelected_Type.__name__ = "Integer32"
_HmMgmtBusSelected_Object = MibScalar
hmMgmtBusSelected = _HmMgmtBusSelected_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 2),
    _HmMgmtBusSelected_Type()
)
hmMgmtBusSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtBusSelected.setStatus("current")
_HmSerialNumbers_ObjectIdentity = ObjectIdentity
hmSerialNumbers = _HmSerialNumbers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3)
)
_HmSerialNumCpu_Type = DisplayString
_HmSerialNumCpu_Object = MibScalar
hmSerialNumCpu = _HmSerialNumCpu_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3, 1),
    _HmSerialNumCpu_Type()
)
hmSerialNumCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSerialNumCpu.setStatus("current")
_HmSerialNumBB_Type = DisplayString
_HmSerialNumBB_Object = MibScalar
hmSerialNumBB = _HmSerialNumBB_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3, 2),
    _HmSerialNumBB_Type()
)
hmSerialNumBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSerialNumBB.setStatus("current")
_HmSerialNumBP_Type = DisplayString
_HmSerialNumBP_Object = MibScalar
hmSerialNumBP = _HmSerialNumBP_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3, 3),
    _HmSerialNumBP_Type()
)
hmSerialNumBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSerialNumBP.setStatus("current")
_HmSerialNumM1_Type = DisplayString
_HmSerialNumM1_Object = MibScalar
hmSerialNumM1 = _HmSerialNumM1_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3, 4),
    _HmSerialNumM1_Type()
)
hmSerialNumM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSerialNumM1.setStatus("current")
_HmSerialNumM2_Type = DisplayString
_HmSerialNumM2_Object = MibScalar
hmSerialNumM2 = _HmSerialNumM2_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3, 5),
    _HmSerialNumM2_Type()
)
hmSerialNumM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSerialNumM2.setStatus("current")
_HmSerialNumM3_Type = DisplayString
_HmSerialNumM3_Object = MibScalar
hmSerialNumM3 = _HmSerialNumM3_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3, 6),
    _HmSerialNumM3_Type()
)
hmSerialNumM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSerialNumM3.setStatus("current")
_HmSerialNumM4_Type = DisplayString
_HmSerialNumM4_Object = MibScalar
hmSerialNumM4 = _HmSerialNumM4_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 3, 7),
    _HmSerialNumM4_Type()
)
hmSerialNumM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSerialNumM4.setStatus("current")
_HmPlugAndPlay_ObjectIdentity = ObjectIdentity
hmPlugAndPlay = _HmPlugAndPlay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 4)
)


class _HmAutoConfigState_Type(Integer32):
    """Custom type hmAutoConfigState based on Integer32"""
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
        *(("disabled", 1),
          ("failed", 4),
          ("inProgess", 2),
          ("ready", 3))
    )


_HmAutoConfigState_Type.__name__ = "Integer32"
_HmAutoConfigState_Object = MibScalar
hmAutoConfigState = _HmAutoConfigState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 4, 1),
    _HmAutoConfigState_Type()
)
hmAutoConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAutoConfigState.setStatus("current")
_HmMACH3Misc_ObjectIdentity = ObjectIdentity
hmMACH3Misc = _HmMACH3Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 5)
)


class _HmUserGroupStatus_Type(Integer32):
    """Custom type hmUserGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HmUserGroupStatus_Type.__name__ = "Integer32"
_HmUserGroupStatus_Object = MibScalar
hmUserGroupStatus = _HmUserGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 11, 5, 1),
    _HmUserGroupStatus_Type()
)
hmUserGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmUserGroupStatus.setStatus("current")
_HmAUIGroup_ObjectIdentity = ObjectIdentity
hmAUIGroup = _HmAUIGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12)
)
_HmAUIModuleTable_Object = MibTable
hmAUIModuleTable = _HmAUIModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 10)
)
if mibBuilder.loadTexts:
    hmAUIModuleTable.setStatus("current")
_HmAUIModuleEntry_Object = MibTableRow
hmAUIModuleEntry = _HmAUIModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 10, 1)
)
hmAUIModuleEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmAUIModuleID"),
)
if mibBuilder.loadTexts:
    hmAUIModuleEntry.setStatus("current")


class _HmAUIModuleID_Type(Integer32):
    """Custom type hmAUIModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmAUIModuleID_Type.__name__ = "Integer32"
_HmAUIModuleID_Object = MibTableColumn
hmAUIModuleID = _HmAUIModuleID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 10, 1, 1),
    _HmAUIModuleID_Type()
)
hmAUIModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAUIModuleID.setStatus("current")


class _HmAUIModuleDTEPowerMonitor_Type(Integer32):
    """Custom type hmAUIModuleDTEPowerMonitor based on Integer32"""
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


_HmAUIModuleDTEPowerMonitor_Type.__name__ = "Integer32"
_HmAUIModuleDTEPowerMonitor_Object = MibTableColumn
hmAUIModuleDTEPowerMonitor = _HmAUIModuleDTEPowerMonitor_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 10, 1, 2),
    _HmAUIModuleDTEPowerMonitor_Type()
)
hmAUIModuleDTEPowerMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAUIModuleDTEPowerMonitor.setStatus("current")
_HmAUIPortTable_Object = MibTable
hmAUIPortTable = _HmAUIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 11)
)
if mibBuilder.loadTexts:
    hmAUIPortTable.setStatus("current")
_HmAUIPortEntry_Object = MibTableRow
hmAUIPortEntry = _HmAUIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 11, 1)
)
hmAUIPortEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmAUIPortID"),
)
if mibBuilder.loadTexts:
    hmAUIPortEntry.setStatus("current")


class _HmAUIPortID_Type(Integer32):
    """Custom type hmAUIPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmAUIPortID_Type.__name__ = "Integer32"
_HmAUIPortID_Object = MibTableColumn
hmAUIPortID = _HmAUIPortID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 11, 1, 1),
    _HmAUIPortID_Type()
)
hmAUIPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAUIPortID.setStatus("current")


class _HmAUIPortDTEPower_Type(Integer32):
    """Custom type hmAUIPortDTEPower based on Integer32"""
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


_HmAUIPortDTEPower_Type.__name__ = "Integer32"
_HmAUIPortDTEPower_Object = MibTableColumn
hmAUIPortDTEPower = _HmAUIPortDTEPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 11, 1, 2),
    _HmAUIPortDTEPower_Type()
)
hmAUIPortDTEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAUIPortDTEPower.setStatus("current")


class _HmAUIPortSQETest_Type(Integer32):
    """Custom type hmAUIPortSQETest based on Integer32"""
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


_HmAUIPortSQETest_Type.__name__ = "Integer32"
_HmAUIPortSQETest_Object = MibTableColumn
hmAUIPortSQETest = _HmAUIPortSQETest_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 12, 11, 1, 3),
    _HmAUIPortSQETest_Type()
)
hmAUIPortSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAUIPortSQETest.setStatus("current")
_HmAgent_ObjectIdentity = ObjectIdentity
hmAgent = _HmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2)
)
_HmAgentEvent_ObjectIdentity = ObjectIdentity
hmAgentEvent = _HmAgentEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0)
)
if mibBuilder.loadTexts:
    hmAgentEvent.setStatus("current")


class _HmAction_Type(Integer32):
    """Custom type hmAction based on Integer32"""
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
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("gbl-reset", 12),
          ("hotRestart", 10),
          ("other", 1),
          ("reset", 2),
          ("resetARP", 5),
          ("resetFDB", 4),
          ("resetL3Stats", 6),
          ("resetL4-7Stats", 7),
          ("resetStats", 3))
    )


_HmAction_Type.__name__ = "Integer32"
_HmAction_Object = MibScalar
hmAction = _HmAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 1),
    _HmAction_Type()
)
hmAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAction.setStatus("current")
_HmActionResult_Type = Integer32
_HmActionResult_Object = MibScalar
hmActionResult = _HmActionResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 2),
    _HmActionResult_Type()
)
hmActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmActionResult.setStatus("current")
_HmNetwork_ObjectIdentity = ObjectIdentity
hmNetwork = _HmNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3)
)
_HmNetLocalIPAddr_Type = IpAddress
_HmNetLocalIPAddr_Object = MibScalar
hmNetLocalIPAddr = _HmNetLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 1),
    _HmNetLocalIPAddr_Type()
)
hmNetLocalIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetLocalIPAddr.setStatus("current")
_HmNetLocalPhysAddr_Type = MacAddress
_HmNetLocalPhysAddr_Object = MibScalar
hmNetLocalPhysAddr = _HmNetLocalPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 2),
    _HmNetLocalPhysAddr_Type()
)
hmNetLocalPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetLocalPhysAddr.setStatus("current")
_HmNetGatewayIPAddr_Type = IpAddress
_HmNetGatewayIPAddr_Object = MibScalar
hmNetGatewayIPAddr = _HmNetGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 3),
    _HmNetGatewayIPAddr_Type()
)
hmNetGatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetGatewayIPAddr.setStatus("current")
_HmNetMask_Type = IpAddress
_HmNetMask_Object = MibScalar
hmNetMask = _HmNetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 4),
    _HmNetMask_Type()
)
hmNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetMask.setStatus("current")
_HmNetPPPBaseIPAddr_Type = IpAddress
_HmNetPPPBaseIPAddr_Object = MibScalar
hmNetPPPBaseIPAddr = _HmNetPPPBaseIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 5),
    _HmNetPPPBaseIPAddr_Type()
)
hmNetPPPBaseIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPPPBaseIPAddr.setStatus("current")
_HmNetPPPNetMask_Type = IpAddress
_HmNetPPPNetMask_Object = MibScalar
hmNetPPPNetMask = _HmNetPPPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 6),
    _HmNetPPPNetMask_Type()
)
hmNetPPPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPPPNetMask.setStatus("current")


class _HmNetAction_Type(Integer32):
    """Custom type hmNetAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("other", 1))
    )


_HmNetAction_Type.__name__ = "Integer32"
_HmNetAction_Object = MibScalar
hmNetAction = _HmNetAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 7),
    _HmNetAction_Type()
)
hmNetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetAction.setStatus("current")
_HmNetVlanID_Type = Integer32
_HmNetVlanID_Object = MibScalar
hmNetVlanID = _HmNetVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 8),
    _HmNetVlanID_Type()
)
hmNetVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetVlanID.setStatus("current")
_HmNetLocalPhysAddrRange_Type = Integer32
_HmNetLocalPhysAddrRange_Object = MibScalar
hmNetLocalPhysAddrRange = _HmNetLocalPhysAddrRange_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 9),
    _HmNetLocalPhysAddrRange_Type()
)
hmNetLocalPhysAddrRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetLocalPhysAddrRange.setStatus("current")


class _HmNetVlanPriority_Type(Integer32):
    """Custom type hmNetVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmNetVlanPriority_Type.__name__ = "Integer32"
_HmNetVlanPriority_Object = MibScalar
hmNetVlanPriority = _HmNetVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 10),
    _HmNetVlanPriority_Type()
)
hmNetVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetVlanPriority.setStatus("current")


class _HmNetIpDscpPriority_Type(Integer32):
    """Custom type hmNetIpDscpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HmNetIpDscpPriority_Type.__name__ = "Integer32"
_HmNetIpDscpPriority_Object = MibScalar
hmNetIpDscpPriority = _HmNetIpDscpPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 11),
    _HmNetIpDscpPriority_Type()
)
hmNetIpDscpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetIpDscpPriority.setStatus("current")
_HmNetACDGroup_ObjectIdentity = ObjectIdentity
hmNetACDGroup = _HmNetACDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12)
)


class _HmNetACDStatus_Type(Integer32):
    """Custom type hmNetACDStatus based on Integer32"""
    defaultValue = 2

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
        *(("activeDetectionOnly", 3),
          ("disable", 2),
          ("enable", 1),
          ("passiveDetectionOnly", 4))
    )


_HmNetACDStatus_Type.__name__ = "Integer32"
_HmNetACDStatus_Object = MibScalar
hmNetACDStatus = _HmNetACDStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 1),
    _HmNetACDStatus_Type()
)
hmNetACDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetACDStatus.setStatus("current")


class _HmNetACDOngoingProbeStatus_Type(Integer32):
    """Custom type hmNetACDOngoingProbeStatus based on Integer32"""
    defaultValue = 1

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


_HmNetACDOngoingProbeStatus_Type.__name__ = "Integer32"
_HmNetACDOngoingProbeStatus_Object = MibScalar
hmNetACDOngoingProbeStatus = _HmNetACDOngoingProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 3),
    _HmNetACDOngoingProbeStatus_Type()
)
hmNetACDOngoingProbeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetACDOngoingProbeStatus.setStatus("current")


class _HmNetACDDelay_Type(Integer32):
    """Custom type hmNetACDDelay based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_HmNetACDDelay_Type.__name__ = "Integer32"
_HmNetACDDelay_Object = MibScalar
hmNetACDDelay = _HmNetACDDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 5),
    _HmNetACDDelay_Type()
)
hmNetACDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetACDDelay.setStatus("current")


class _HmNetACDReleaseDelay_Type(Integer32):
    """Custom type hmNetACDReleaseDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HmNetACDReleaseDelay_Type.__name__ = "Integer32"
_HmNetACDReleaseDelay_Object = MibScalar
hmNetACDReleaseDelay = _HmNetACDReleaseDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 7),
    _HmNetACDReleaseDelay_Type()
)
hmNetACDReleaseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetACDReleaseDelay.setStatus("current")


class _HmNetACDMaxProtection_Type(Integer32):
    """Custom type hmNetACDMaxProtection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmNetACDMaxProtection_Type.__name__ = "Integer32"
_HmNetACDMaxProtection_Object = MibScalar
hmNetACDMaxProtection = _HmNetACDMaxProtection_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 9),
    _HmNetACDMaxProtection_Type()
)
hmNetACDMaxProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetACDMaxProtection.setStatus("current")


class _HmNetACDProtectInterval_Type(Integer32):
    """Custom type hmNetACDProtectInterval based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_HmNetACDProtectInterval_Type.__name__ = "Integer32"
_HmNetACDProtectInterval_Object = MibScalar
hmNetACDProtectInterval = _HmNetACDProtectInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 11),
    _HmNetACDProtectInterval_Type()
)
hmNetACDProtectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetACDProtectInterval.setStatus("current")


class _HmNetACDFaultState_Type(Integer32):
    """Custom type hmNetACDFaultState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmNetACDFaultState_Type.__name__ = "Integer32"
_HmNetACDFaultState_Object = MibScalar
hmNetACDFaultState = _HmNetACDFaultState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 13),
    _HmNetACDFaultState_Type()
)
hmNetACDFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetACDFaultState.setStatus("current")
_HmNetACDAddrTable_Object = MibTable
hmNetACDAddrTable = _HmNetACDAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 20)
)
if mibBuilder.loadTexts:
    hmNetACDAddrTable.setStatus("current")
_HmNetACDAddrEntry_Object = MibTableRow
hmNetACDAddrEntry = _HmNetACDAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 20, 1)
)
hmNetACDAddrEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmNetACDTimeMark"),
)
if mibBuilder.loadTexts:
    hmNetACDAddrEntry.setStatus("current")
_HmNetACDTimeMark_Type = TimeFilter
_HmNetACDTimeMark_Object = MibTableColumn
hmNetACDTimeMark = _HmNetACDTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 20, 1, 1),
    _HmNetACDTimeMark_Type()
)
hmNetACDTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetACDTimeMark.setStatus("current")
_HmNetACDAddrSubtype_Type = AddressFamilyNumbers
_HmNetACDAddrSubtype_Object = MibTableColumn
hmNetACDAddrSubtype = _HmNetACDAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 20, 1, 3),
    _HmNetACDAddrSubtype_Type()
)
hmNetACDAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetACDAddrSubtype.setStatus("current")


class _HmNetACDAddr_Type(OctetString):
    """Custom type hmNetACDAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HmNetACDAddr_Type.__name__ = "OctetString"
_HmNetACDAddr_Object = MibTableColumn
hmNetACDAddr = _HmNetACDAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 20, 1, 5),
    _HmNetACDAddr_Type()
)
hmNetACDAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetACDAddr.setStatus("current")
_HmNetACDMAC_Type = MacAddress
_HmNetACDMAC_Object = MibTableColumn
hmNetACDMAC = _HmNetACDMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 20, 1, 7),
    _HmNetACDMAC_Type()
)
hmNetACDMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetACDMAC.setStatus("current")
_HmNetACDIfId_Type = Integer32
_HmNetACDIfId_Object = MibTableColumn
hmNetACDIfId = _HmNetACDIfId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 12, 20, 1, 9),
    _HmNetACDIfId_Type()
)
hmNetACDIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetACDIfId.setStatus("current")
_HmNetHiDiscoveryGroup_ObjectIdentity = ObjectIdentity
hmNetHiDiscoveryGroup = _HmNetHiDiscoveryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 20)
)


class _HmNetHiDiscoveryStatus_Type(Integer32):
    """Custom type hmNetHiDiscoveryStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("readOnly", 3))
    )


_HmNetHiDiscoveryStatus_Type.__name__ = "Integer32"
_HmNetHiDiscoveryStatus_Object = MibScalar
hmNetHiDiscoveryStatus = _HmNetHiDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 20, 1),
    _HmNetHiDiscoveryStatus_Type()
)
hmNetHiDiscoveryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetHiDiscoveryStatus.setStatus("current")


class _HmNetHiDiscoveryRelay_Type(Integer32):
    """Custom type hmNetHiDiscoveryRelay based on Integer32"""
    defaultValue = 2

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


_HmNetHiDiscoveryRelay_Type.__name__ = "Integer32"
_HmNetHiDiscoveryRelay_Object = MibScalar
hmNetHiDiscoveryRelay = _HmNetHiDiscoveryRelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 20, 2),
    _HmNetHiDiscoveryRelay_Type()
)
hmNetHiDiscoveryRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetHiDiscoveryRelay.setStatus("current")
_HmNetSNTPGroup_ObjectIdentity = ObjectIdentity
hmNetSNTPGroup = _HmNetSNTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30)
)


class _HmNetSNTPStatus_Type(Integer32):
    """Custom type hmNetSNTPStatus based on Integer32"""
    defaultValue = 2

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


_HmNetSNTPStatus_Type.__name__ = "Integer32"
_HmNetSNTPStatus_Object = MibScalar
hmNetSNTPStatus = _HmNetSNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 1),
    _HmNetSNTPStatus_Type()
)
hmNetSNTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPStatus.setStatus("current")
_HmNetSNTPServer_Type = IpAddress
_HmNetSNTPServer_Object = MibScalar
hmNetSNTPServer = _HmNetSNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 2),
    _HmNetSNTPServer_Type()
)
hmNetSNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPServer.setStatus("current")
_HmNetSNTPTime_Type = TimeTicks
_HmNetSNTPTime_Object = MibScalar
hmNetSNTPTime = _HmNetSNTPTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 3),
    _HmNetSNTPTime_Type()
)
hmNetSNTPTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPTime.setStatus("current")


class _HmNetSNTPLocalOffset_Type(Integer32):
    """Custom type hmNetSNTPLocalOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_HmNetSNTPLocalOffset_Type.__name__ = "Integer32"
_HmNetSNTPLocalOffset_Object = MibScalar
hmNetSNTPLocalOffset = _HmNetSNTPLocalOffset_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 4),
    _HmNetSNTPLocalOffset_Type()
)
hmNetSNTPLocalOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPLocalOffset.setStatus("current")
_HmNetSNTPServer2_Type = IpAddress
_HmNetSNTPServer2_Object = MibScalar
hmNetSNTPServer2 = _HmNetSNTPServer2_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 5),
    _HmNetSNTPServer2_Type()
)
hmNetSNTPServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPServer2.setStatus("current")


class _HmNetSNTPSyncInterval_Type(Integer32):
    """Custom type hmNetSNTPSyncInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HmNetSNTPSyncInterval_Type.__name__ = "Integer32"
_HmNetSNTPSyncInterval_Object = MibScalar
hmNetSNTPSyncInterval = _HmNetSNTPSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 6),
    _HmNetSNTPSyncInterval_Type()
)
hmNetSNTPSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPSyncInterval.setStatus("current")


class _HmNetSNTPAcceptBroadcasts_Type(Integer32):
    """Custom type hmNetSNTPAcceptBroadcasts based on Integer32"""
    defaultValue = 1

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


_HmNetSNTPAcceptBroadcasts_Type.__name__ = "Integer32"
_HmNetSNTPAcceptBroadcasts_Object = MibScalar
hmNetSNTPAcceptBroadcasts = _HmNetSNTPAcceptBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 7),
    _HmNetSNTPAcceptBroadcasts_Type()
)
hmNetSNTPAcceptBroadcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPAcceptBroadcasts.setStatus("current")
_HmNetSNTPAnycastAddr_Type = IpAddress
_HmNetSNTPAnycastAddr_Object = MibScalar
hmNetSNTPAnycastAddr = _HmNetSNTPAnycastAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 8),
    _HmNetSNTPAnycastAddr_Type()
)
hmNetSNTPAnycastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPAnycastAddr.setStatus("current")


class _HmNetSNTPAnycastVlan_Type(Integer32):
    """Custom type hmNetSNTPAnycastVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4042),
    )


_HmNetSNTPAnycastVlan_Type.__name__ = "Integer32"
_HmNetSNTPAnycastVlan_Object = MibScalar
hmNetSNTPAnycastVlan = _HmNetSNTPAnycastVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 9),
    _HmNetSNTPAnycastVlan_Type()
)
hmNetSNTPAnycastVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPAnycastVlan.setStatus("current")


class _HmNetSNTPAnycastInterval_Type(Integer32):
    """Custom type hmNetSNTPAnycastInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HmNetSNTPAnycastInterval_Type.__name__ = "Integer32"
_HmNetSNTPAnycastInterval_Object = MibScalar
hmNetSNTPAnycastInterval = _HmNetSNTPAnycastInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 10),
    _HmNetSNTPAnycastInterval_Type()
)
hmNetSNTPAnycastInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPAnycastInterval.setStatus("current")
_HmNetSNTPOperStatus_Type = Integer32
_HmNetSNTPOperStatus_Object = MibScalar
hmNetSNTPOperStatus = _HmNetSNTPOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 11),
    _HmNetSNTPOperStatus_Type()
)
hmNetSNTPOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetSNTPOperStatus.setStatus("current")


class _HmNetSNTPTimeAdjustThreshold_Type(Integer32):
    """Custom type hmNetSNTPTimeAdjustThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmNetSNTPTimeAdjustThreshold_Type.__name__ = "Integer32"
_HmNetSNTPTimeAdjustThreshold_Object = MibScalar
hmNetSNTPTimeAdjustThreshold = _HmNetSNTPTimeAdjustThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 12),
    _HmNetSNTPTimeAdjustThreshold_Type()
)
hmNetSNTPTimeAdjustThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPTimeAdjustThreshold.setStatus("current")


class _HmNetSNTPOnceAtStartup_Type(Integer32):
    """Custom type hmNetSNTPOnceAtStartup based on Integer32"""
    defaultValue = 2

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


_HmNetSNTPOnceAtStartup_Type.__name__ = "Integer32"
_HmNetSNTPOnceAtStartup_Object = MibScalar
hmNetSNTPOnceAtStartup = _HmNetSNTPOnceAtStartup_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 13),
    _HmNetSNTPOnceAtStartup_Type()
)
hmNetSNTPOnceAtStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPOnceAtStartup.setStatus("current")


class _HmNetSNTPServerOnlyIfSync_Type(Integer32):
    """Custom type hmNetSNTPServerOnlyIfSync based on Integer32"""
    defaultValue = 2

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


_HmNetSNTPServerOnlyIfSync_Type.__name__ = "Integer32"
_HmNetSNTPServerOnlyIfSync_Object = MibScalar
hmNetSNTPServerOnlyIfSync = _HmNetSNTPServerOnlyIfSync_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 14),
    _HmNetSNTPServerOnlyIfSync_Type()
)
hmNetSNTPServerOnlyIfSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPServerOnlyIfSync.setStatus("current")


class _HmNetSNTPServerStatus_Type(Integer32):
    """Custom type hmNetSNTPServerStatus based on Integer32"""
    defaultValue = 1

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


_HmNetSNTPServerStatus_Type.__name__ = "Integer32"
_HmNetSNTPServerStatus_Object = MibScalar
hmNetSNTPServerStatus = _HmNetSNTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 15),
    _HmNetSNTPServerStatus_Type()
)
hmNetSNTPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPServerStatus.setStatus("current")


class _HmNetSNTPClientStatus_Type(Integer32):
    """Custom type hmNetSNTPClientStatus based on Integer32"""
    defaultValue = 1

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


_HmNetSNTPClientStatus_Type.__name__ = "Integer32"
_HmNetSNTPClientStatus_Object = MibScalar
hmNetSNTPClientStatus = _HmNetSNTPClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 30, 16),
    _HmNetSNTPClientStatus_Type()
)
hmNetSNTPClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNTPClientStatus.setStatus("current")
_HmNetNTPGroup_ObjectIdentity = ObjectIdentity
hmNetNTPGroup = _HmNetNTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31)
)


class _HmNetNTPOperation_Type(Integer32):
    """Custom type hmNetNTPOperation based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("broadcast-client", 7),
          ("client", 4),
          ("client-server", 6),
          ("off", 1),
          ("server", 5),
          ("symmetric-active", 2),
          ("symmetric-passive", 3))
    )


_HmNetNTPOperation_Type.__name__ = "Integer32"
_HmNetNTPOperation_Object = MibScalar
hmNetNTPOperation = _HmNetNTPOperation_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 1),
    _HmNetNTPOperation_Type()
)
hmNetNTPOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPOperation.setStatus("current")


class _HmNetNTPServer1AddrType_Type(InetAddressType):
    """Custom type hmNetNTPServer1AddrType based on InetAddressType"""


_HmNetNTPServer1AddrType_Object = MibScalar
hmNetNTPServer1AddrType = _HmNetNTPServer1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 2),
    _HmNetNTPServer1AddrType_Type()
)
hmNetNTPServer1AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPServer1AddrType.setStatus("current")
_HmNetNTPServer1Address_Type = InetAddress
_HmNetNTPServer1Address_Object = MibScalar
hmNetNTPServer1Address = _HmNetNTPServer1Address_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 3),
    _HmNetNTPServer1Address_Type()
)
hmNetNTPServer1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPServer1Address.setStatus("current")


class _HmNetNTPServer2AddrType_Type(InetAddressType):
    """Custom type hmNetNTPServer2AddrType based on InetAddressType"""


_HmNetNTPServer2AddrType_Object = MibScalar
hmNetNTPServer2AddrType = _HmNetNTPServer2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 4),
    _HmNetNTPServer2AddrType_Type()
)
hmNetNTPServer2AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPServer2AddrType.setStatus("current")
_HmNetNTPServer2Address_Type = InetAddress
_HmNetNTPServer2Address_Object = MibScalar
hmNetNTPServer2Address = _HmNetNTPServer2Address_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 5),
    _HmNetNTPServer2Address_Type()
)
hmNetNTPServer2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPServer2Address.setStatus("current")


class _HmNetNTPSyncInterval_Type(Integer32):
    """Custom type hmNetNTPSyncInterval based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_HmNetNTPSyncInterval_Type.__name__ = "Integer32"
_HmNetNTPSyncInterval_Object = MibScalar
hmNetNTPSyncInterval = _HmNetNTPSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 6),
    _HmNetNTPSyncInterval_Type()
)
hmNetNTPSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPSyncInterval.setStatus("current")


class _HmNetNTPAnycastAddrType_Type(InetAddressType):
    """Custom type hmNetNTPAnycastAddrType based on InetAddressType"""


_HmNetNTPAnycastAddrType_Object = MibScalar
hmNetNTPAnycastAddrType = _HmNetNTPAnycastAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 7),
    _HmNetNTPAnycastAddrType_Type()
)
hmNetNTPAnycastAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPAnycastAddrType.setStatus("current")
_HmNetNTPAnycastAddress_Type = InetAddress
_HmNetNTPAnycastAddress_Object = MibScalar
hmNetNTPAnycastAddress = _HmNetNTPAnycastAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 8),
    _HmNetNTPAnycastAddress_Type()
)
hmNetNTPAnycastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPAnycastAddress.setStatus("current")


class _HmNetNTPAnycastInterval_Type(Integer32):
    """Custom type hmNetNTPAnycastInterval based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4096),
    )


_HmNetNTPAnycastInterval_Type.__name__ = "Integer32"
_HmNetNTPAnycastInterval_Object = MibScalar
hmNetNTPAnycastInterval = _HmNetNTPAnycastInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 9),
    _HmNetNTPAnycastInterval_Type()
)
hmNetNTPAnycastInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetNTPAnycastInterval.setStatus("current")
_HmNetNTPStatusText_Type = DisplayString
_HmNetNTPStatusText_Object = MibScalar
hmNetNTPStatusText = _HmNetNTPStatusText_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 10),
    _HmNetNTPStatusText_Type()
)
hmNetNTPStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetNTPStatusText.setStatus("current")
_HmNetNTPStatusCode_Type = Integer32
_HmNetNTPStatusCode_Object = MibScalar
hmNetNTPStatusCode = _HmNetNTPStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 31, 11),
    _HmNetNTPStatusCode_Type()
)
hmNetNTPStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetNTPStatusCode.setStatus("current")
_HmNetPTPGroup_ObjectIdentity = ObjectIdentity
hmNetPTPGroup = _HmNetPTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40)
)
_HmNetPTPConfiguration_ObjectIdentity = ObjectIdentity
hmNetPTPConfiguration = _HmNetPTPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1)
)


class _HmNetPTPEnable_Type(Integer32):
    """Custom type hmNetPTPEnable based on Integer32"""
    defaultValue = 2

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


_HmNetPTPEnable_Type.__name__ = "Integer32"
_HmNetPTPEnable_Object = MibScalar
hmNetPTPEnable = _HmNetPTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 1),
    _HmNetPTPEnable_Type()
)
hmNetPTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPEnable.setStatus("current")


class _HmNetPTPAction_Type(Integer32):
    """Custom type hmNetPTPAction based on Integer32"""
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
        *(("init-with-default", 2),
          ("init-with-nvm", 3),
          ("other", 1))
    )


_HmNetPTPAction_Type.__name__ = "Integer32"
_HmNetPTPAction_Object = MibScalar
hmNetPTPAction = _HmNetPTPAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 2),
    _HmNetPTPAction_Type()
)
hmNetPTPAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPAction.setStatus("current")


class _HmNetPTPClockMode_Type(Integer32):
    """Custom type hmNetPTPClockMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("v1-boundary-clock", 1),
          ("v1-simple-mode", 4),
          ("v2-boundary-clock-onestep", 5),
          ("v2-boundary-clock-twostep", 6),
          ("v2-simple-mode", 9),
          ("v2-transparent-clock", 7))
    )


_HmNetPTPClockMode_Type.__name__ = "Integer32"
_HmNetPTPClockMode_Object = MibScalar
hmNetPTPClockMode = _HmNetPTPClockMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 3),
    _HmNetPTPClockMode_Type()
)
hmNetPTPClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPClockMode.setStatus("current")


class _HmNetPTPSlavePort_Type(Integer32):
    """Custom type hmNetPTPSlavePort based on Integer32"""
    defaultValue = 0


_HmNetPTPSlavePort_Object = MibScalar
hmNetPTPSlavePort = _HmNetPTPSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 4),
    _HmNetPTPSlavePort_Type()
)
hmNetPTPSlavePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPSlavePort.setStatus("current")


class _HmNetPTPIsSynchronized_Type(Integer32):
    """Custom type hmNetPTPIsSynchronized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmNetPTPIsSynchronized_Type.__name__ = "Integer32"
_HmNetPTPIsSynchronized_Object = MibScalar
hmNetPTPIsSynchronized = _HmNetPTPIsSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 5),
    _HmNetPTPIsSynchronized_Type()
)
hmNetPTPIsSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPIsSynchronized.setStatus("current")


class _HmNetPTPSyncLowerBound_Type(Integer32):
    """Custom type hmNetPTPSyncLowerBound based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_HmNetPTPSyncLowerBound_Type.__name__ = "Integer32"
_HmNetPTPSyncLowerBound_Object = MibScalar
hmNetPTPSyncLowerBound = _HmNetPTPSyncLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 6),
    _HmNetPTPSyncLowerBound_Type()
)
hmNetPTPSyncLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPSyncLowerBound.setStatus("current")


class _HmNetPTPSyncUpperBound_Type(Integer32):
    """Custom type hmNetPTPSyncUpperBound based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(31, 1000000000),
    )


_HmNetPTPSyncUpperBound_Type.__name__ = "Integer32"
_HmNetPTPSyncUpperBound_Object = MibScalar
hmNetPTPSyncUpperBound = _HmNetPTPSyncUpperBound_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 7),
    _HmNetPTPSyncUpperBound_Type()
)
hmNetPTPSyncUpperBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPSyncUpperBound.setStatus("current")


class _HmNetPTPClockStratum_Type(Integer32):
    """Custom type hmNetPTPClockStratum based on Integer32"""
    defaultValue = 255


_HmNetPTPClockStratum_Object = MibScalar
hmNetPTPClockStratum = _HmNetPTPClockStratum_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 8),
    _HmNetPTPClockStratum_Type()
)
hmNetPTPClockStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPClockStratum.setStatus("current")


class _HmNetPTPClockIdentifier_Type(OctetString):
    """Custom type hmNetPTPClockIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HmNetPTPClockIdentifier_Type.__name__ = "OctetString"
_HmNetPTPClockIdentifier_Object = MibScalar
hmNetPTPClockIdentifier = _HmNetPTPClockIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 9),
    _HmNetPTPClockIdentifier_Type()
)
hmNetPTPClockIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPClockIdentifier.setStatus("current")


class _HmNetPTPClockVariance_Type(Integer32):
    """Custom type hmNetPTPClockVariance based on Integer32"""
    defaultValue = -16256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_HmNetPTPClockVariance_Type.__name__ = "Integer32"
_HmNetPTPClockVariance_Object = MibScalar
hmNetPTPClockVariance = _HmNetPTPClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 10),
    _HmNetPTPClockVariance_Type()
)
hmNetPTPClockVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPClockVariance.setStatus("current")


class _HmNetPTPPreferredMaster_Type(Integer32):
    """Custom type hmNetPTPPreferredMaster based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmNetPTPPreferredMaster_Type.__name__ = "Integer32"
_HmNetPTPPreferredMaster_Object = MibScalar
hmNetPTPPreferredMaster = _HmNetPTPPreferredMaster_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 11),
    _HmNetPTPPreferredMaster_Type()
)
hmNetPTPPreferredMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPPreferredMaster.setStatus("current")


class _HmNetPTPSyncInterval_Type(Integer32):
    """Custom type hmNetPTPSyncInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              16,
              64)
        )
    )
    namedValues = NamedValues(
        *(("sec-1", 1),
          ("sec-16", 16),
          ("sec-2", 2),
          ("sec-64", 64),
          ("sec-8", 8))
    )


_HmNetPTPSyncInterval_Type.__name__ = "Integer32"
_HmNetPTPSyncInterval_Object = MibScalar
hmNetPTPSyncInterval = _HmNetPTPSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 12),
    _HmNetPTPSyncInterval_Type()
)
hmNetPTPSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPSyncInterval.setStatus("current")


class _HmNetPTPSubdomainName_Type(OctetString):
    """Custom type hmNetPTPSubdomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HmNetPTPSubdomainName_Type.__name__ = "OctetString"
_HmNetPTPSubdomainName_Object = MibScalar
hmNetPTPSubdomainName = _HmNetPTPSubdomainName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 13),
    _HmNetPTPSubdomainName_Type()
)
hmNetPTPSubdomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPSubdomainName.setStatus("current")
_HmNetPTPOffsetFromMasterNanoSecs_Type = Integer32
_HmNetPTPOffsetFromMasterNanoSecs_Object = MibScalar
hmNetPTPOffsetFromMasterNanoSecs = _HmNetPTPOffsetFromMasterNanoSecs_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 14),
    _HmNetPTPOffsetFromMasterNanoSecs_Type()
)
hmNetPTPOffsetFromMasterNanoSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPOffsetFromMasterNanoSecs.setStatus("current")
_HmNetPTPAbsMaxOffset_Type = Integer32
_HmNetPTPAbsMaxOffset_Object = MibScalar
hmNetPTPAbsMaxOffset = _HmNetPTPAbsMaxOffset_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 15),
    _HmNetPTPAbsMaxOffset_Type()
)
hmNetPTPAbsMaxOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPAbsMaxOffset.setStatus("current")
_HmNetPTPOneWayDelayNanoSecs_Type = Integer32
_HmNetPTPOneWayDelayNanoSecs_Object = MibScalar
hmNetPTPOneWayDelayNanoSecs = _HmNetPTPOneWayDelayNanoSecs_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 16),
    _HmNetPTPOneWayDelayNanoSecs_Type()
)
hmNetPTPOneWayDelayNanoSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPOneWayDelayNanoSecs.setStatus("current")
_HmNetPTPTimeSeconds_Type = Integer32
_HmNetPTPTimeSeconds_Object = MibScalar
hmNetPTPTimeSeconds = _HmNetPTPTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 17),
    _HmNetPTPTimeSeconds_Type()
)
hmNetPTPTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPTimeSeconds.setStatus("current")
_HmNetPTPObservedDrift_Type = Integer32
_HmNetPTPObservedDrift_Object = MibScalar
hmNetPTPObservedDrift = _HmNetPTPObservedDrift_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 18),
    _HmNetPTPObservedDrift_Type()
)
hmNetPTPObservedDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPObservedDrift.setStatus("current")


class _HmNetPTPPiIntegral_Type(Integer32):
    """Custom type hmNetPTPPiIntegral based on Integer32"""
    defaultValue = 6250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_HmNetPTPPiIntegral_Type.__name__ = "Integer32"
_HmNetPTPPiIntegral_Object = MibScalar
hmNetPTPPiIntegral = _HmNetPTPPiIntegral_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 19),
    _HmNetPTPPiIntegral_Type()
)
hmNetPTPPiIntegral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPPiIntegral.setStatus("current")
_HmNetPTPParentUUID_Type = MacAddress
_HmNetPTPParentUUID_Object = MibScalar
hmNetPTPParentUUID = _HmNetPTPParentUUID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 20),
    _HmNetPTPParentUUID_Type()
)
hmNetPTPParentUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPParentUUID.setStatus("current")
_HmNetPTPGrandmasterUUID_Type = MacAddress
_HmNetPTPGrandmasterUUID_Object = MibScalar
hmNetPTPGrandmasterUUID = _HmNetPTPGrandmasterUUID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 21),
    _HmNetPTPGrandmasterUUID_Type()
)
hmNetPTPGrandmasterUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPGrandmasterUUID.setStatus("current")
_HmNetPTPCurrentUTCOffset_Type = Integer32
_HmNetPTPCurrentUTCOffset_Object = MibScalar
hmNetPTPCurrentUTCOffset = _HmNetPTPCurrentUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 22),
    _HmNetPTPCurrentUTCOffset_Type()
)
hmNetPTPCurrentUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPCurrentUTCOffset.setStatus("current")


class _HmNetPTPleap59_Type(Integer32):
    """Custom type hmNetPTPleap59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmNetPTPleap59_Type.__name__ = "Integer32"
_HmNetPTPleap59_Object = MibScalar
hmNetPTPleap59 = _HmNetPTPleap59_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 23),
    _HmNetPTPleap59_Type()
)
hmNetPTPleap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPleap59.setStatus("current")


class _HmNetPTPleap61_Type(Integer32):
    """Custom type hmNetPTPleap61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmNetPTPleap61_Type.__name__ = "Integer32"
_HmNetPTPleap61_Object = MibScalar
hmNetPTPleap61 = _HmNetPTPleap61_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 24),
    _HmNetPTPleap61_Type()
)
hmNetPTPleap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPleap61.setStatus("current")
_HmNetPTPStepsRemoved_Type = Integer32
_HmNetPTPStepsRemoved_Object = MibScalar
hmNetPTPStepsRemoved = _HmNetPTPStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 25),
    _HmNetPTPStepsRemoved_Type()
)
hmNetPTPStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPStepsRemoved.setStatus("current")
_HmNetPTPEpochNumber_Type = Integer32
_HmNetPTPEpochNumber_Object = MibScalar
hmNetPTPEpochNumber = _HmNetPTPEpochNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 26),
    _HmNetPTPEpochNumber_Type()
)
hmNetPTPEpochNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPEpochNumber.setStatus("current")


class _HmNetPTPStaticDrift_Type(Integer32):
    """Custom type hmNetPTPStaticDrift based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500000000, 500000000),
    )


_HmNetPTPStaticDrift_Type.__name__ = "Integer32"
_HmNetPTPStaticDrift_Object = MibScalar
hmNetPTPStaticDrift = _HmNetPTPStaticDrift_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 1, 27),
    _HmNetPTPStaticDrift_Type()
)
hmNetPTPStaticDrift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPStaticDrift.setStatus("current")
_HmNetPTPPortTable_Object = MibTable
hmNetPTPPortTable = _HmNetPTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 2)
)
if mibBuilder.loadTexts:
    hmNetPTPPortTable.setStatus("current")
_HmNetPTPPortEntry_Object = MibTableRow
hmNetPTPPortEntry = _HmNetPTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 2, 1)
)
hmNetPTPPortEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmNetPTPPortID"),
)
if mibBuilder.loadTexts:
    hmNetPTPPortEntry.setStatus("current")


class _HmNetPTPPortID_Type(Integer32):
    """Custom type hmNetPTPPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmNetPTPPortID_Type.__name__ = "Integer32"
_HmNetPTPPortID_Object = MibTableColumn
hmNetPTPPortID = _HmNetPTPPortID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 2, 1, 1),
    _HmNetPTPPortID_Type()
)
hmNetPTPPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPPortID.setStatus("current")


class _HmNetPTPPortState_Type(Integer32):
    """Custom type hmNetPTPPortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("faulty", 2),
          ("initializing", 1),
          ("listening", 4),
          ("master", 6),
          ("passive", 7),
          ("pre-master", 5),
          ("slave", 9),
          ("uncalibrated", 8))
    )


_HmNetPTPPortState_Type.__name__ = "Integer32"
_HmNetPTPPortState_Object = MibTableColumn
hmNetPTPPortState = _HmNetPTPPortState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 2, 1, 2),
    _HmNetPTPPortState_Type()
)
hmNetPTPPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTPPortState.setStatus("current")


class _HmNetPTPPortBurstEnable_Type(Integer32):
    """Custom type hmNetPTPPortBurstEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmNetPTPPortBurstEnable_Type.__name__ = "Integer32"
_HmNetPTPPortBurstEnable_Object = MibTableColumn
hmNetPTPPortBurstEnable = _HmNetPTPPortBurstEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 2, 1, 3),
    _HmNetPTPPortBurstEnable_Type()
)
hmNetPTPPortBurstEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPPortBurstEnable.setStatus("current")


class _HmNetPTPPortEnable_Type(Integer32):
    """Custom type hmNetPTPPortEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HmNetPTPPortEnable_Type.__name__ = "Integer32"
_HmNetPTPPortEnable_Object = MibTableColumn
hmNetPTPPortEnable = _HmNetPTPPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 40, 2, 1, 4),
    _HmNetPTPPortEnable_Type()
)
hmNetPTPPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTPPortEnable.setStatus("current")
_HmNetPTP2Group_ObjectIdentity = ObjectIdentity
hmNetPTP2Group = _HmNetPTP2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41)
)
_HmNetPTP2Configuration_ObjectIdentity = ObjectIdentity
hmNetPTP2Configuration = _HmNetPTP2Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1)
)
_HmNetPTP2TwoStepClock_Type = TruthValue
_HmNetPTP2TwoStepClock_Object = MibScalar
hmNetPTP2TwoStepClock = _HmNetPTP2TwoStepClock_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 1),
    _HmNetPTP2TwoStepClock_Type()
)
hmNetPTP2TwoStepClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2TwoStepClock.setStatus("current")
_HmNetPTP2ClockIdentity_Type = PTPClockIdentity
_HmNetPTP2ClockIdentity_Object = MibScalar
hmNetPTP2ClockIdentity = _HmNetPTP2ClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 2),
    _HmNetPTP2ClockIdentity_Type()
)
hmNetPTP2ClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2ClockIdentity.setStatus("current")


class _HmNetPTP2Priority1_Type(Integer32):
    """Custom type hmNetPTP2Priority1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmNetPTP2Priority1_Type.__name__ = "Integer32"
_HmNetPTP2Priority1_Object = MibScalar
hmNetPTP2Priority1 = _HmNetPTP2Priority1_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 3),
    _HmNetPTP2Priority1_Type()
)
hmNetPTP2Priority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2Priority1.setStatus("current")


class _HmNetPTP2Priority2_Type(Integer32):
    """Custom type hmNetPTP2Priority2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmNetPTP2Priority2_Type.__name__ = "Integer32"
_HmNetPTP2Priority2_Object = MibScalar
hmNetPTP2Priority2 = _HmNetPTP2Priority2_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 4),
    _HmNetPTP2Priority2_Type()
)
hmNetPTP2Priority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2Priority2.setStatus("current")


class _HmNetPTP2DomainNumber_Type(Integer32):
    """Custom type hmNetPTP2DomainNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmNetPTP2DomainNumber_Type.__name__ = "Integer32"
_HmNetPTP2DomainNumber_Object = MibScalar
hmNetPTP2DomainNumber = _HmNetPTP2DomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 5),
    _HmNetPTP2DomainNumber_Type()
)
hmNetPTP2DomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2DomainNumber.setStatus("current")
_HmNetPTP2StepsRemoved_Type = Integer32
_HmNetPTP2StepsRemoved_Object = MibScalar
hmNetPTP2StepsRemoved = _HmNetPTP2StepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 6),
    _HmNetPTP2StepsRemoved_Type()
)
hmNetPTP2StepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2StepsRemoved.setStatus("current")
_HmNetPTP2OffsetFromMaster_Type = PTPTimeInterval
_HmNetPTP2OffsetFromMaster_Object = MibScalar
hmNetPTP2OffsetFromMaster = _HmNetPTP2OffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 7),
    _HmNetPTP2OffsetFromMaster_Type()
)
hmNetPTP2OffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2OffsetFromMaster.setStatus("current")
_HmNetPTP2MeanPathDelay_Type = PTPTimeInterval
_HmNetPTP2MeanPathDelay_Object = MibScalar
hmNetPTP2MeanPathDelay = _HmNetPTP2MeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 8),
    _HmNetPTP2MeanPathDelay_Type()
)
hmNetPTP2MeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2MeanPathDelay.setStatus("current")
_HmNetPTP2ParentPortIdentity_Type = PTPPortIdentity
_HmNetPTP2ParentPortIdentity_Object = MibScalar
hmNetPTP2ParentPortIdentity = _HmNetPTP2ParentPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 9),
    _HmNetPTP2ParentPortIdentity_Type()
)
hmNetPTP2ParentPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2ParentPortIdentity.setStatus("current")
_HmNetPTP2ParentStats_Type = TruthValue
_HmNetPTP2ParentStats_Object = MibScalar
hmNetPTP2ParentStats = _HmNetPTP2ParentStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 10),
    _HmNetPTP2ParentStats_Type()
)
hmNetPTP2ParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2ParentStats.setStatus("current")
_HmNetPTP2ObservedParentOffsetScaledLogVariance_Type = Integer32
_HmNetPTP2ObservedParentOffsetScaledLogVariance_Object = MibScalar
hmNetPTP2ObservedParentOffsetScaledLogVariance = _HmNetPTP2ObservedParentOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 11),
    _HmNetPTP2ObservedParentOffsetScaledLogVariance_Type()
)
hmNetPTP2ObservedParentOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2ObservedParentOffsetScaledLogVariance.setStatus("current")
_HmNetPTP2ObservedParentClockPhaseChangeRate_Type = Integer32
_HmNetPTP2ObservedParentClockPhaseChangeRate_Object = MibScalar
hmNetPTP2ObservedParentClockPhaseChangeRate = _HmNetPTP2ObservedParentClockPhaseChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 12),
    _HmNetPTP2ObservedParentClockPhaseChangeRate_Type()
)
hmNetPTP2ObservedParentClockPhaseChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2ObservedParentClockPhaseChangeRate.setStatus("current")
_HmNetPTP2GrandmasterIdentity_Type = PTPClockIdentity
_HmNetPTP2GrandmasterIdentity_Object = MibScalar
hmNetPTP2GrandmasterIdentity = _HmNetPTP2GrandmasterIdentity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 13),
    _HmNetPTP2GrandmasterIdentity_Type()
)
hmNetPTP2GrandmasterIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2GrandmasterIdentity.setStatus("current")
_HmNetPTP2GrandmasterClockQuality_Type = PTPClockQuality
_HmNetPTP2GrandmasterClockQuality_Object = MibScalar
hmNetPTP2GrandmasterClockQuality = _HmNetPTP2GrandmasterClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 14),
    _HmNetPTP2GrandmasterClockQuality_Type()
)
hmNetPTP2GrandmasterClockQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2GrandmasterClockQuality.setStatus("current")
_HmNetPTP2GrandmasterPriority1_Type = Integer32
_HmNetPTP2GrandmasterPriority1_Object = MibScalar
hmNetPTP2GrandmasterPriority1 = _HmNetPTP2GrandmasterPriority1_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 15),
    _HmNetPTP2GrandmasterPriority1_Type()
)
hmNetPTP2GrandmasterPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2GrandmasterPriority1.setStatus("current")
_HmNetPTP2GrandmasterPriority2_Type = Integer32
_HmNetPTP2GrandmasterPriority2_Object = MibScalar
hmNetPTP2GrandmasterPriority2 = _HmNetPTP2GrandmasterPriority2_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 16),
    _HmNetPTP2GrandmasterPriority2_Type()
)
hmNetPTP2GrandmasterPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2GrandmasterPriority2.setStatus("current")
_HmNetPTP2CurrentUtcOffset_Type = Integer32
_HmNetPTP2CurrentUtcOffset_Object = MibScalar
hmNetPTP2CurrentUtcOffset = _HmNetPTP2CurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 17),
    _HmNetPTP2CurrentUtcOffset_Type()
)
hmNetPTP2CurrentUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2CurrentUtcOffset.setStatus("current")
_HmNetPTP2CurrentUtcOffsetValid_Type = TruthValue
_HmNetPTP2CurrentUtcOffsetValid_Object = MibScalar
hmNetPTP2CurrentUtcOffsetValid = _HmNetPTP2CurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 18),
    _HmNetPTP2CurrentUtcOffsetValid_Type()
)
hmNetPTP2CurrentUtcOffsetValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2CurrentUtcOffsetValid.setStatus("current")
_HmNetPTP2Leap59_Type = TruthValue
_HmNetPTP2Leap59_Object = MibScalar
hmNetPTP2Leap59 = _HmNetPTP2Leap59_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 19),
    _HmNetPTP2Leap59_Type()
)
hmNetPTP2Leap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2Leap59.setStatus("current")
_HmNetPTP2Leap61_Type = TruthValue
_HmNetPTP2Leap61_Object = MibScalar
hmNetPTP2Leap61 = _HmNetPTP2Leap61_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 20),
    _HmNetPTP2Leap61_Type()
)
hmNetPTP2Leap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2Leap61.setStatus("current")
_HmNetPTP2TimeTraceable_Type = TruthValue
_HmNetPTP2TimeTraceable_Object = MibScalar
hmNetPTP2TimeTraceable = _HmNetPTP2TimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 21),
    _HmNetPTP2TimeTraceable_Type()
)
hmNetPTP2TimeTraceable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TimeTraceable.setStatus("current")
_HmNetPTP2FrequencyTraceable_Type = TruthValue
_HmNetPTP2FrequencyTraceable_Object = MibScalar
hmNetPTP2FrequencyTraceable = _HmNetPTP2FrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 22),
    _HmNetPTP2FrequencyTraceable_Type()
)
hmNetPTP2FrequencyTraceable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2FrequencyTraceable.setStatus("current")
_HmNetPTP2PtpTimescale_Type = TruthValue
_HmNetPTP2PtpTimescale_Object = MibScalar
hmNetPTP2PtpTimescale = _HmNetPTP2PtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 23),
    _HmNetPTP2PtpTimescale_Type()
)
hmNetPTP2PtpTimescale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2PtpTimescale.setStatus("current")


class _HmNetPTP2TimeSource_Type(Integer32):
    """Custom type hmNetPTP2TimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("handSet", 96),
          ("internalOscillator", 160),
          ("ntp", 80),
          ("other", 144),
          ("ptp", 64),
          ("terrestrialRadio", 48))
    )


_HmNetPTP2TimeSource_Type.__name__ = "Integer32"
_HmNetPTP2TimeSource_Object = MibScalar
hmNetPTP2TimeSource = _HmNetPTP2TimeSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 24),
    _HmNetPTP2TimeSource_Type()
)
hmNetPTP2TimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TimeSource.setStatus("current")


class _HmNetPTP2GrandmasterClockClass_Type(Integer32):
    """Custom type hmNetPTP2GrandmasterClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmNetPTP2GrandmasterClockClass_Type.__name__ = "Integer32"
_HmNetPTP2GrandmasterClockClass_Object = MibScalar
hmNetPTP2GrandmasterClockClass = _HmNetPTP2GrandmasterClockClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 25),
    _HmNetPTP2GrandmasterClockClass_Type()
)
hmNetPTP2GrandmasterClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2GrandmasterClockClass.setStatus("current")


class _HmNetPTP2GrandmasterClockAccuracy_Type(Integer32):
    """Custom type hmNetPTP2GrandmasterClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
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
              254)
        )
    )
    namedValues = NamedValues(
        *(("beyond10s", 49),
          ("unknown", 254),
          ("within1000ns", 35),
          ("within1000us", 41),
          ("within100ms", 45),
          ("within100ns", 33),
          ("within100us", 39),
          ("within10ms", 43),
          ("within10s", 48),
          ("within10us", 37),
          ("within1s", 47),
          ("within2500ns", 36),
          ("within2500us", 42),
          ("within250ms", 46),
          ("within250ns", 34),
          ("within250us", 40),
          ("within25ms", 44),
          ("within25ns", 32),
          ("within25us", 38))
    )


_HmNetPTP2GrandmasterClockAccuracy_Type.__name__ = "Integer32"
_HmNetPTP2GrandmasterClockAccuracy_Object = MibScalar
hmNetPTP2GrandmasterClockAccuracy = _HmNetPTP2GrandmasterClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 26),
    _HmNetPTP2GrandmasterClockAccuracy_Type()
)
hmNetPTP2GrandmasterClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2GrandmasterClockAccuracy.setStatus("current")
_HmNetPTP2GrandmasterClockVariance_Type = Integer32
_HmNetPTP2GrandmasterClockVariance_Object = MibScalar
hmNetPTP2GrandmasterClockVariance = _HmNetPTP2GrandmasterClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 1, 27),
    _HmNetPTP2GrandmasterClockVariance_Type()
)
hmNetPTP2GrandmasterClockVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2GrandmasterClockVariance.setStatus("current")
_HmNetPTP2PortTable_Object = MibTable
hmNetPTP2PortTable = _HmNetPTP2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2)
)
if mibBuilder.loadTexts:
    hmNetPTP2PortTable.setStatus("current")
_HmNetPTP2PortEntry_Object = MibTableRow
hmNetPTP2PortEntry = _HmNetPTP2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1)
)
hmNetPTP2PortEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmNetPTPPortID"),
)
if mibBuilder.loadTexts:
    hmNetPTP2PortEntry.setStatus("current")


class _HmNetPTP2PortEnable_Type(TruthValue):
    """Custom type hmNetPTP2PortEnable based on TruthValue"""


_HmNetPTP2PortEnable_Object = MibTableColumn
hmNetPTP2PortEnable = _HmNetPTP2PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 1),
    _HmNetPTP2PortEnable_Type()
)
hmNetPTP2PortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2PortEnable.setStatus("current")


class _HmNetPTP2PortState_Type(Integer32):
    """Custom type hmNetPTP2PortState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("faulty", 2),
          ("initializing", 1),
          ("listening", 4),
          ("master", 6),
          ("passive", 7),
          ("pre-master", 5),
          ("slave", 9),
          ("uncalibrated", 8))
    )


_HmNetPTP2PortState_Type.__name__ = "Integer32"
_HmNetPTP2PortState_Object = MibTableColumn
hmNetPTP2PortState = _HmNetPTP2PortState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 2),
    _HmNetPTP2PortState_Type()
)
hmNetPTP2PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2PortState.setStatus("current")
_HmNetPTP2LogDelayReqInterval_Type = Integer32
_HmNetPTP2LogDelayReqInterval_Object = MibTableColumn
hmNetPTP2LogDelayReqInterval = _HmNetPTP2LogDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 3),
    _HmNetPTP2LogDelayReqInterval_Type()
)
hmNetPTP2LogDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2LogDelayReqInterval.setStatus("current")
_HmNetPTP2PeerMeanPathDelay_Type = PTPTimeInterval
_HmNetPTP2PeerMeanPathDelay_Object = MibTableColumn
hmNetPTP2PeerMeanPathDelay = _HmNetPTP2PeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 4),
    _HmNetPTP2PeerMeanPathDelay_Type()
)
hmNetPTP2PeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2PeerMeanPathDelay.setStatus("current")


class _HmNetPTP2LogAnnounceInterval_Type(Integer32):
    """Custom type hmNetPTP2LogAnnounceInterval based on Integer32"""
    defaultValue = 1

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
        *(("sec-1", 0),
          ("sec-16", 4),
          ("sec-2", 1),
          ("sec-4", 2),
          ("sec-8", 3))
    )


_HmNetPTP2LogAnnounceInterval_Type.__name__ = "Integer32"
_HmNetPTP2LogAnnounceInterval_Object = MibTableColumn
hmNetPTP2LogAnnounceInterval = _HmNetPTP2LogAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 5),
    _HmNetPTP2LogAnnounceInterval_Type()
)
hmNetPTP2LogAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2LogAnnounceInterval.setStatus("current")


class _HmNetPTP2AnnounceReceiptTimeout_Type(Integer32):
    """Custom type hmNetPTP2AnnounceReceiptTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_HmNetPTP2AnnounceReceiptTimeout_Type.__name__ = "Integer32"
_HmNetPTP2AnnounceReceiptTimeout_Object = MibTableColumn
hmNetPTP2AnnounceReceiptTimeout = _HmNetPTP2AnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 6),
    _HmNetPTP2AnnounceReceiptTimeout_Type()
)
hmNetPTP2AnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2AnnounceReceiptTimeout.setStatus("current")


class _HmNetPTP2LogSyncInterval_Type(Integer32):
    """Custom type hmNetPTP2LogSyncInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("msec-250", -2),
          ("msec-500", -1),
          ("sec-1", 0),
          ("sec-2", 1))
    )


_HmNetPTP2LogSyncInterval_Type.__name__ = "Integer32"
_HmNetPTP2LogSyncInterval_Object = MibTableColumn
hmNetPTP2LogSyncInterval = _HmNetPTP2LogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 7),
    _HmNetPTP2LogSyncInterval_Type()
)
hmNetPTP2LogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2LogSyncInterval.setStatus("current")


class _HmNetPTP2DelayMechanism_Type(Integer32):
    """Custom type hmNetPTP2DelayMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 254),
          ("e2e", 1),
          ("p2p", 2))
    )


_HmNetPTP2DelayMechanism_Type.__name__ = "Integer32"
_HmNetPTP2DelayMechanism_Object = MibTableColumn
hmNetPTP2DelayMechanism = _HmNetPTP2DelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 8),
    _HmNetPTP2DelayMechanism_Type()
)
hmNetPTP2DelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2DelayMechanism.setStatus("current")


class _HmNetPTP2LogPdelayReqInterval_Type(Integer32):
    """Custom type hmNetPTP2LogPdelayReqInterval based on Integer32"""
    defaultValue = 0

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
        *(("sec-1", 0),
          ("sec-16", 4),
          ("sec-2", 1),
          ("sec-32", 5),
          ("sec-4", 2),
          ("sec-8", 3))
    )


_HmNetPTP2LogPdelayReqInterval_Type.__name__ = "Integer32"
_HmNetPTP2LogPdelayReqInterval_Object = MibTableColumn
hmNetPTP2LogPdelayReqInterval = _HmNetPTP2LogPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 9),
    _HmNetPTP2LogPdelayReqInterval_Type()
)
hmNetPTP2LogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2LogPdelayReqInterval.setStatus("current")


class _HmNetPTP2VersionNumber_Type(Integer32):
    """Custom type hmNetPTP2VersionNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptpVersion1", 1),
          ("ptpVersion2", 2))
    )


_HmNetPTP2VersionNumber_Type.__name__ = "Integer32"
_HmNetPTP2VersionNumber_Object = MibTableColumn
hmNetPTP2VersionNumber = _HmNetPTP2VersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 10),
    _HmNetPTP2VersionNumber_Type()
)
hmNetPTP2VersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2VersionNumber.setStatus("current")


class _HmNetPTP2NetworkProtocol_Type(Integer32):
    """Custom type hmNetPTP2NetworkProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023", 3),
          ("udpIpv4", 1))
    )


_HmNetPTP2NetworkProtocol_Type.__name__ = "Integer32"
_HmNetPTP2NetworkProtocol_Object = MibTableColumn
hmNetPTP2NetworkProtocol = _HmNetPTP2NetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 11),
    _HmNetPTP2NetworkProtocol_Type()
)
hmNetPTP2NetworkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2NetworkProtocol.setStatus("current")


class _HmNetPTP2V1Compatibility_Type(Integer32):
    """Custom type hmNetPTP2V1Compatibility based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("off", 2),
          ("on", 1))
    )


_HmNetPTP2V1Compatibility_Type.__name__ = "Integer32"
_HmNetPTP2V1Compatibility_Object = MibTableColumn
hmNetPTP2V1Compatibility = _HmNetPTP2V1Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 12),
    _HmNetPTP2V1Compatibility_Type()
)
hmNetPTP2V1Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2V1Compatibility.setStatus("current")


class _HmNetPTP2DelayAsymmetry_Type(PTPTimeInterval):
    """Custom type hmNetPTP2DelayAsymmetry based on PTPTimeInterval"""
    defaultHexValue = "0000000000000000"


_HmNetPTP2DelayAsymmetry_Object = MibTableColumn
hmNetPTP2DelayAsymmetry = _HmNetPTP2DelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 13),
    _HmNetPTP2DelayAsymmetry_Type()
)
hmNetPTP2DelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2DelayAsymmetry.setStatus("current")


class _HmNetPTP2PortCapability_Type(Bits):
    """Custom type hmNetPTP2PortCapability based on Bits"""
    namedValues = NamedValues(
        *(("asymmCorrection", 7),
          ("e2e-delay", 2),
          ("one-step", 1),
          ("p2p-delay", 3),
          ("ptp2Ieee8023", 4),
          ("ptp2UdpIpv4", 5),
          ("ptp2UdpIpv6", 6),
          ("reserved", 0))
    )

_HmNetPTP2PortCapability_Type.__name__ = "Bits"
_HmNetPTP2PortCapability_Object = MibTableColumn
hmNetPTP2PortCapability = _HmNetPTP2PortCapability_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 14),
    _HmNetPTP2PortCapability_Type()
)
hmNetPTP2PortCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2PortCapability.setStatus("current")


class _HmNetPTP2VlanID_Type(Integer32):
    """Custom type hmNetPTP2VlanID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4042),
    )


_HmNetPTP2VlanID_Type.__name__ = "Integer32"
_HmNetPTP2VlanID_Object = MibTableColumn
hmNetPTP2VlanID = _HmNetPTP2VlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 15),
    _HmNetPTP2VlanID_Type()
)
hmNetPTP2VlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2VlanID.setStatus("current")


class _HmNetPTP2VlanPriority_Type(Integer32):
    """Custom type hmNetPTP2VlanPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmNetPTP2VlanPriority_Type.__name__ = "Integer32"
_HmNetPTP2VlanPriority_Object = MibTableColumn
hmNetPTP2VlanPriority = _HmNetPTP2VlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 41, 2, 1, 16),
    _HmNetPTP2VlanPriority_Type()
)
hmNetPTP2VlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2VlanPriority.setStatus("current")
_HmNetPTP2TCGroup_ObjectIdentity = ObjectIdentity
hmNetPTP2TCGroup = _HmNetPTP2TCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42)
)
_HmNetPTP2TCConfiguration_ObjectIdentity = ObjectIdentity
hmNetPTP2TCConfiguration = _HmNetPTP2TCConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1)
)
_HmNetPTP2TCClockIdentity_Type = PTPClockIdentity
_HmNetPTP2TCClockIdentity_Object = MibScalar
hmNetPTP2TCClockIdentity = _HmNetPTP2TCClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 1),
    _HmNetPTP2TCClockIdentity_Type()
)
hmNetPTP2TCClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2TCClockIdentity.setStatus("current")


class _HmNetPTP2TCDelayMechanism_Type(Integer32):
    """Custom type hmNetPTP2TCDelayMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 254),
          ("e2e", 1),
          ("e2e-optimized", 3),
          ("p2p", 2))
    )


_HmNetPTP2TCDelayMechanism_Type.__name__ = "Integer32"
_HmNetPTP2TCDelayMechanism_Object = MibScalar
hmNetPTP2TCDelayMechanism = _HmNetPTP2TCDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 2),
    _HmNetPTP2TCDelayMechanism_Type()
)
hmNetPTP2TCDelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCDelayMechanism.setStatus("current")


class _HmNetPTP2TCPrimaryDomain_Type(Integer32):
    """Custom type hmNetPTP2TCPrimaryDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmNetPTP2TCPrimaryDomain_Type.__name__ = "Integer32"
_HmNetPTP2TCPrimaryDomain_Object = MibScalar
hmNetPTP2TCPrimaryDomain = _HmNetPTP2TCPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 3),
    _HmNetPTP2TCPrimaryDomain_Type()
)
hmNetPTP2TCPrimaryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCPrimaryDomain.setStatus("current")
_HmNetPTP2TCSyntonized_Type = TruthValue
_HmNetPTP2TCSyntonized_Object = MibScalar
hmNetPTP2TCSyntonized = _HmNetPTP2TCSyntonized_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 4),
    _HmNetPTP2TCSyntonized_Type()
)
hmNetPTP2TCSyntonized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCSyntonized.setStatus("current")


class _HmNetPTP2TCNetworkProtocol_Type(Integer32):
    """Custom type hmNetPTP2TCNetworkProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023", 3),
          ("udpIpv4", 1))
    )


_HmNetPTP2TCNetworkProtocol_Type.__name__ = "Integer32"
_HmNetPTP2TCNetworkProtocol_Object = MibScalar
hmNetPTP2TCNetworkProtocol = _HmNetPTP2TCNetworkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 5),
    _HmNetPTP2TCNetworkProtocol_Type()
)
hmNetPTP2TCNetworkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCNetworkProtocol.setStatus("current")
_HmNetPTP2TCCurrentMaster_Type = PTPPortIdentity
_HmNetPTP2TCCurrentMaster_Object = MibScalar
hmNetPTP2TCCurrentMaster = _HmNetPTP2TCCurrentMaster_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 6),
    _HmNetPTP2TCCurrentMaster_Type()
)
hmNetPTP2TCCurrentMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2TCCurrentMaster.setStatus("current")


class _HmNetPTP2TCManagement_Type(TruthValue):
    """Custom type hmNetPTP2TCManagement based on TruthValue"""


_HmNetPTP2TCManagement_Object = MibScalar
hmNetPTP2TCManagement = _HmNetPTP2TCManagement_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 7),
    _HmNetPTP2TCManagement_Type()
)
hmNetPTP2TCManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCManagement.setStatus("current")


class _HmNetPTP2TCMultiDomainMode_Type(TruthValue):
    """Custom type hmNetPTP2TCMultiDomainMode based on TruthValue"""


_HmNetPTP2TCMultiDomainMode_Object = MibScalar
hmNetPTP2TCMultiDomainMode = _HmNetPTP2TCMultiDomainMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 8),
    _HmNetPTP2TCMultiDomainMode_Type()
)
hmNetPTP2TCMultiDomainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCMultiDomainMode.setStatus("current")


class _HmNetPTP2TCSyncLocalClock_Type(TruthValue):
    """Custom type hmNetPTP2TCSyncLocalClock based on TruthValue"""


_HmNetPTP2TCSyncLocalClock_Object = MibScalar
hmNetPTP2TCSyncLocalClock = _HmNetPTP2TCSyncLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 9),
    _HmNetPTP2TCSyncLocalClock_Type()
)
hmNetPTP2TCSyncLocalClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCSyncLocalClock.setStatus("current")


class _HmNetPTP2TCVlanID_Type(Integer32):
    """Custom type hmNetPTP2TCVlanID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4042),
    )


_HmNetPTP2TCVlanID_Type.__name__ = "Integer32"
_HmNetPTP2TCVlanID_Object = MibScalar
hmNetPTP2TCVlanID = _HmNetPTP2TCVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 10),
    _HmNetPTP2TCVlanID_Type()
)
hmNetPTP2TCVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCVlanID.setStatus("current")


class _HmNetPTP2TCVlanPriority_Type(Integer32):
    """Custom type hmNetPTP2TCVlanPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HmNetPTP2TCVlanPriority_Type.__name__ = "Integer32"
_HmNetPTP2TCVlanPriority_Object = MibScalar
hmNetPTP2TCVlanPriority = _HmNetPTP2TCVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 1, 11),
    _HmNetPTP2TCVlanPriority_Type()
)
hmNetPTP2TCVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCVlanPriority.setStatus("current")
_HmNetPTP2TCPortTable_Object = MibTable
hmNetPTP2TCPortTable = _HmNetPTP2TCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 2)
)
if mibBuilder.loadTexts:
    hmNetPTP2TCPortTable.setStatus("current")
_HmNetPTP2TCPortEntry_Object = MibTableRow
hmNetPTP2TCPortEntry = _HmNetPTP2TCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 2, 1)
)
hmNetPTP2TCPortEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmNetPTPPortID"),
)
if mibBuilder.loadTexts:
    hmNetPTP2TCPortEntry.setStatus("current")


class _HmNetPTP2TCPortEnable_Type(TruthValue):
    """Custom type hmNetPTP2TCPortEnable based on TruthValue"""


_HmNetPTP2TCPortEnable_Object = MibTableColumn
hmNetPTP2TCPortEnable = _HmNetPTP2TCPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 2, 1, 1),
    _HmNetPTP2TCPortEnable_Type()
)
hmNetPTP2TCPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCPortEnable.setStatus("current")


class _HmNetPTP2TCLogPdelayReqInterval_Type(Integer32):
    """Custom type hmNetPTP2TCLogPdelayReqInterval based on Integer32"""
    defaultValue = 0

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
        *(("sec-1", 0),
          ("sec-16", 4),
          ("sec-2", 1),
          ("sec-32", 5),
          ("sec-4", 2),
          ("sec-8", 3))
    )


_HmNetPTP2TCLogPdelayReqInterval_Type.__name__ = "Integer32"
_HmNetPTP2TCLogPdelayReqInterval_Object = MibTableColumn
hmNetPTP2TCLogPdelayReqInterval = _HmNetPTP2TCLogPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 2, 1, 2),
    _HmNetPTP2TCLogPdelayReqInterval_Type()
)
hmNetPTP2TCLogPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCLogPdelayReqInterval.setStatus("current")
_HmNetPTP2TCFaulty_Type = TruthValue
_HmNetPTP2TCFaulty_Object = MibTableColumn
hmNetPTP2TCFaulty = _HmNetPTP2TCFaulty_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 2, 1, 3),
    _HmNetPTP2TCFaulty_Type()
)
hmNetPTP2TCFaulty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2TCFaulty.setStatus("current")
_HmNetPTP2TCPeerMeanPathDelay_Type = PTPTimeInterval
_HmNetPTP2TCPeerMeanPathDelay_Object = MibTableColumn
hmNetPTP2TCPeerMeanPathDelay = _HmNetPTP2TCPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 2, 1, 4),
    _HmNetPTP2TCPeerMeanPathDelay_Type()
)
hmNetPTP2TCPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPTP2TCPeerMeanPathDelay.setStatus("current")


class _HmNetPTP2TCDelayAsymmetry_Type(PTPTimeInterval):
    """Custom type hmNetPTP2TCDelayAsymmetry based on PTPTimeInterval"""
    defaultHexValue = "0000000000000000"


_HmNetPTP2TCDelayAsymmetry_Object = MibTableColumn
hmNetPTP2TCDelayAsymmetry = _HmNetPTP2TCDelayAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 42, 2, 1, 5),
    _HmNetPTP2TCDelayAsymmetry_Type()
)
hmNetPTP2TCDelayAsymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetPTP2TCDelayAsymmetry.setStatus("current")
_HmNetSNMPGroup_ObjectIdentity = ObjectIdentity
hmNetSNMPGroup = _HmNetSNMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50)
)


class _HmNetSNMPv1Status_Type(Integer32):
    """Custom type hmNetSNMPv1Status based on Integer32"""
    defaultValue = 1

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


_HmNetSNMPv1Status_Type.__name__ = "Integer32"
_HmNetSNMPv1Status_Object = MibScalar
hmNetSNMPv1Status = _HmNetSNMPv1Status_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 1),
    _HmNetSNMPv1Status_Type()
)
hmNetSNMPv1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPv1Status.setStatus("current")


class _HmNetSNMPv2Status_Type(Integer32):
    """Custom type hmNetSNMPv2Status based on Integer32"""
    defaultValue = 1

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


_HmNetSNMPv2Status_Type.__name__ = "Integer32"
_HmNetSNMPv2Status_Object = MibScalar
hmNetSNMPv2Status = _HmNetSNMPv2Status_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 2),
    _HmNetSNMPv2Status_Type()
)
hmNetSNMPv2Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPv2Status.setStatus("current")


class _HmNetSNMPv3Status_Type(Integer32):
    """Custom type hmNetSNMPv3Status based on Integer32"""
    defaultValue = 1

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


_HmNetSNMPv3Status_Type.__name__ = "Integer32"
_HmNetSNMPv3Status_Object = MibScalar
hmNetSNMPv3Status = _HmNetSNMPv3Status_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 3),
    _HmNetSNMPv3Status_Type()
)
hmNetSNMPv3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPv3Status.setStatus("current")


class _HmNetSNMPAccessStatus_Type(Integer32):
    """Custom type hmNetSNMPAccessStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("readOnly", 3))
    )


_HmNetSNMPAccessStatus_Type.__name__ = "Integer32"
_HmNetSNMPAccessStatus_Object = MibScalar
hmNetSNMPAccessStatus = _HmNetSNMPAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 4),
    _HmNetSNMPAccessStatus_Type()
)
hmNetSNMPAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPAccessStatus.setStatus("current")


class _HmNetSNMPSynchronizeV1V3Status_Type(Integer32):
    """Custom type hmNetSNMPSynchronizeV1V3Status based on Integer32"""
    defaultValue = 1

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


_HmNetSNMPSynchronizeV1V3Status_Type.__name__ = "Integer32"
_HmNetSNMPSynchronizeV1V3Status_Object = MibScalar
hmNetSNMPSynchronizeV1V3Status = _HmNetSNMPSynchronizeV1V3Status_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 5),
    _HmNetSNMPSynchronizeV1V3Status_Type()
)
hmNetSNMPSynchronizeV1V3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPSynchronizeV1V3Status.setStatus("current")


class _HmNetSNMPPortNumber_Type(Integer32):
    """Custom type hmNetSNMPPortNumber based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmNetSNMPPortNumber_Type.__name__ = "Integer32"
_HmNetSNMPPortNumber_Object = MibScalar
hmNetSNMPPortNumber = _HmNetSNMPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 6),
    _HmNetSNMPPortNumber_Type()
)
hmNetSNMPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPPortNumber.setStatus("current")


class _HmNetSNMPRadiusAuthenticate_Type(Integer32):
    """Custom type hmNetSNMPRadiusAuthenticate based on Integer32"""
    defaultValue = 2

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


_HmNetSNMPRadiusAuthenticate_Type.__name__ = "Integer32"
_HmNetSNMPRadiusAuthenticate_Object = MibScalar
hmNetSNMPRadiusAuthenticate = _HmNetSNMPRadiusAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 7),
    _HmNetSNMPRadiusAuthenticate_Type()
)
hmNetSNMPRadiusAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPRadiusAuthenticate.setStatus("current")


class _HmNetSNMPv3EncryptionReadWriteStatus_Type(Integer32):
    """Custom type hmNetSNMPv3EncryptionReadWriteStatus based on Integer32"""
    defaultValue = 2

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


_HmNetSNMPv3EncryptionReadWriteStatus_Type.__name__ = "Integer32"
_HmNetSNMPv3EncryptionReadWriteStatus_Object = MibScalar
hmNetSNMPv3EncryptionReadWriteStatus = _HmNetSNMPv3EncryptionReadWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 8),
    _HmNetSNMPv3EncryptionReadWriteStatus_Type()
)
hmNetSNMPv3EncryptionReadWriteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPv3EncryptionReadWriteStatus.setStatus("current")


class _HmNetSNMPv3EncryptionReadOnlyStatus_Type(Integer32):
    """Custom type hmNetSNMPv3EncryptionReadOnlyStatus based on Integer32"""
    defaultValue = 2

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


_HmNetSNMPv3EncryptionReadOnlyStatus_Type.__name__ = "Integer32"
_HmNetSNMPv3EncryptionReadOnlyStatus_Object = MibScalar
hmNetSNMPv3EncryptionReadOnlyStatus = _HmNetSNMPv3EncryptionReadOnlyStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 50, 9),
    _HmNetSNMPv3EncryptionReadOnlyStatus_Type()
)
hmNetSNMPv3EncryptionReadOnlyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSNMPv3EncryptionReadOnlyStatus.setStatus("current")
_HmNetGPSGroup_ObjectIdentity = ObjectIdentity
hmNetGPSGroup = _HmNetGPSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 60)
)
_HmNetGPSIsAvailable_Type = TruthValue
_HmNetGPSIsAvailable_Object = MibScalar
hmNetGPSIsAvailable = _HmNetGPSIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 60, 1),
    _HmNetGPSIsAvailable_Type()
)
hmNetGPSIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetGPSIsAvailable.setStatus("current")
_HmNetGPSIsSynchronized_Type = TruthValue
_HmNetGPSIsSynchronized_Object = MibScalar
hmNetGPSIsSynchronized = _HmNetGPSIsSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 60, 2),
    _HmNetGPSIsSynchronized_Type()
)
hmNetGPSIsSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetGPSIsSynchronized.setStatus("current")


class _HmNetGPSMode_Type(Integer32):
    """Custom type hmNetGPSMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gpsIn", 1),
          ("gpsOut", 2))
    )


_HmNetGPSMode_Type.__name__ = "Integer32"
_HmNetGPSMode_Object = MibScalar
hmNetGPSMode = _HmNetGPSMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 60, 3),
    _HmNetGPSMode_Type()
)
hmNetGPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetGPSMode.setStatus("current")


class _HmNetGPSTimeStringFormat_Type(Integer32):
    """Custom type hmNetGPSTimeStringFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("meinberg", 1)
    )


_HmNetGPSTimeStringFormat_Type.__name__ = "Integer32"
_HmNetGPSTimeStringFormat_Object = MibScalar
hmNetGPSTimeStringFormat = _HmNetGPSTimeStringFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 60, 4),
    _HmNetGPSTimeStringFormat_Type()
)
hmNetGPSTimeStringFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetGPSTimeStringFormat.setStatus("current")
_HmRestrictedMgtAccessGroup_ObjectIdentity = ObjectIdentity
hmRestrictedMgtAccessGroup = _HmRestrictedMgtAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70)
)


class _HmRMAOperation_Type(Integer32):
    """Custom type hmRMAOperation based on Integer32"""
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


_HmRMAOperation_Type.__name__ = "Integer32"
_HmRMAOperation_Object = MibScalar
hmRMAOperation = _HmRMAOperation_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 1),
    _HmRMAOperation_Type()
)
hmRMAOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRMAOperation.setStatus("current")
_HmRMATable_Object = MibTable
hmRMATable = _HmRMATable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2)
)
if mibBuilder.loadTexts:
    hmRMATable.setStatus("current")
_HmRMAEntry_Object = MibTableRow
hmRMAEntry = _HmRMAEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1)
)
hmRMAEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmRMAIndex"),
)
if mibBuilder.loadTexts:
    hmRMAEntry.setStatus("current")


class _HmRMAIndex_Type(Integer32):
    """Custom type hmRMAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HmRMAIndex_Type.__name__ = "Integer32"
_HmRMAIndex_Object = MibTableColumn
hmRMAIndex = _HmRMAIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 1),
    _HmRMAIndex_Type()
)
hmRMAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRMAIndex.setStatus("current")
_HmRMARowStatus_Type = RowStatus
_HmRMARowStatus_Object = MibTableColumn
hmRMARowStatus = _HmRMARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 2),
    _HmRMARowStatus_Type()
)
hmRMARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmRMARowStatus.setStatus("current")


class _HmRMAIpAddr_Type(IpAddress):
    """Custom type hmRMAIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_HmRMAIpAddr_Object = MibTableColumn
hmRMAIpAddr = _HmRMAIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 3),
    _HmRMAIpAddr_Type()
)
hmRMAIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRMAIpAddr.setStatus("current")


class _HmRMANetMask_Type(IpAddress):
    """Custom type hmRMANetMask based on IpAddress"""
    defaultHexValue = "00000000"


_HmRMANetMask_Object = MibTableColumn
hmRMANetMask = _HmRMANetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 4),
    _HmRMANetMask_Type()
)
hmRMANetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRMANetMask.setStatus("current")


class _HmRMASrvHttp_Type(Integer32):
    """Custom type hmRMASrvHttp based on Integer32"""
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


_HmRMASrvHttp_Type.__name__ = "Integer32"
_HmRMASrvHttp_Object = MibTableColumn
hmRMASrvHttp = _HmRMASrvHttp_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 5),
    _HmRMASrvHttp_Type()
)
hmRMASrvHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRMASrvHttp.setStatus("current")


class _HmRMASrvSnmp_Type(Integer32):
    """Custom type hmRMASrvSnmp based on Integer32"""
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


_HmRMASrvSnmp_Type.__name__ = "Integer32"
_HmRMASrvSnmp_Object = MibTableColumn
hmRMASrvSnmp = _HmRMASrvSnmp_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 6),
    _HmRMASrvSnmp_Type()
)
hmRMASrvSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRMASrvSnmp.setStatus("current")


class _HmRMASrvTelnet_Type(Integer32):
    """Custom type hmRMASrvTelnet based on Integer32"""
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


_HmRMASrvTelnet_Type.__name__ = "Integer32"
_HmRMASrvTelnet_Object = MibTableColumn
hmRMASrvTelnet = _HmRMASrvTelnet_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 7),
    _HmRMASrvTelnet_Type()
)
hmRMASrvTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRMASrvTelnet.setStatus("current")


class _HmRMASrvSsh_Type(Integer32):
    """Custom type hmRMASrvSsh based on Integer32"""
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


_HmRMASrvSsh_Type.__name__ = "Integer32"
_HmRMASrvSsh_Object = MibTableColumn
hmRMASrvSsh = _HmRMASrvSsh_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 3, 70, 2, 1, 8),
    _HmRMASrvSsh_Type()
)
hmRMASrvSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRMASrvSsh.setStatus("current")
_HmFSTable_ObjectIdentity = ObjectIdentity
hmFSTable = _HmFSTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4)
)


class _HmFSUpdFileName_Type(DisplayString):
    """Custom type hmFSUpdFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_HmFSUpdFileName_Type.__name__ = "DisplayString"
_HmFSUpdFileName_Object = MibScalar
hmFSUpdFileName = _HmFSUpdFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 1),
    _HmFSUpdFileName_Type()
)
hmFSUpdFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSUpdFileName.setStatus("current")


class _HmFSConfFileName_Type(DisplayString):
    """Custom type hmFSConfFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_HmFSConfFileName_Type.__name__ = "DisplayString"
_HmFSConfFileName_Object = MibScalar
hmFSConfFileName = _HmFSConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 2),
    _HmFSConfFileName_Type()
)
hmFSConfFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSConfFileName.setStatus("current")


class _HmFSLogFileName_Type(DisplayString):
    """Custom type hmFSLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_HmFSLogFileName_Type.__name__ = "DisplayString"
_HmFSLogFileName_Object = MibScalar
hmFSLogFileName = _HmFSLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 3),
    _HmFSLogFileName_Type()
)
hmFSLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSLogFileName.setStatus("current")


class _HmFSUserName_Type(DisplayString):
    """Custom type hmFSUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmFSUserName_Type.__name__ = "DisplayString"
_HmFSUserName_Object = MibScalar
hmFSUserName = _HmFSUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 4),
    _HmFSUserName_Type()
)
hmFSUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSUserName.setStatus("current")


class _HmFSTPPassword_Type(DisplayString):
    """Custom type hmFSTPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmFSTPPassword_Type.__name__ = "DisplayString"
_HmFSTPPassword_Object = MibScalar
hmFSTPPassword = _HmFSTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 5),
    _HmFSTPPassword_Type()
)
hmFSTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSTPPassword.setStatus("current")


class _HmFSAction_Type(Integer32):
    """Custom type hmFSAction based on Integer32"""
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
              12,
              13,
              15,
              16,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("config-load", 3),
          ("config-load-backup", 13),
          ("config-load-default", 8),
          ("config-load-remote", 5),
          ("config-remote-and-save", 15),
          ("config-save", 4),
          ("config-save-remote", 6),
          ("config-save-remote-script", 21),
          ("gbl-update", 12),
          ("log-clear", 10),
          ("log-save", 7),
          ("other", 1),
          ("set-to-factory", 9),
          ("toggleImage", 20),
          ("update", 2),
          ("updateBootcode", 16))
    )


_HmFSAction_Type.__name__ = "Integer32"
_HmFSAction_Object = MibScalar
hmFSAction = _HmFSAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 6),
    _HmFSAction_Type()
)
hmFSAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSAction.setStatus("current")


class _HmFSActionResult_Type(Integer32):
    """Custom type hmFSActionResult based on Integer32"""
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
          ("ok", 3),
          ("other", 1),
          ("pending", 2))
    )


_HmFSActionResult_Type.__name__ = "Integer32"
_HmFSActionResult_Object = MibScalar
hmFSActionResult = _HmFSActionResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 8),
    _HmFSActionResult_Type()
)
hmFSActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFSActionResult.setStatus("current")


class _HmFSBootConfiguration_Type(Integer32):
    """Custom type hmFSBootConfiguration based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("local", 2))
    )


_HmFSBootConfiguration_Type.__name__ = "Integer32"
_HmFSBootConfiguration_Object = MibScalar
hmFSBootConfiguration = _HmFSBootConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 9),
    _HmFSBootConfiguration_Type()
)
hmFSBootConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSBootConfiguration.setStatus("current")


class _HmFSRunningConfiguration_Type(Integer32):
    """Custom type hmFSRunningConfiguration based on Integer32"""
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
        *(("boot", 1),
          ("local", 2),
          ("remote", 3))
    )


_HmFSRunningConfiguration_Type.__name__ = "Integer32"
_HmFSRunningConfiguration_Object = MibScalar
hmFSRunningConfiguration = _HmFSRunningConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 10),
    _HmFSRunningConfiguration_Type()
)
hmFSRunningConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmFSRunningConfiguration.setStatus("current")
_HmFSLastMessage_Type = DisplayString
_HmFSLastMessage_Object = MibScalar
hmFSLastMessage = _HmFSLastMessage_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 11),
    _HmFSLastMessage_Type()
)
hmFSLastMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFSLastMessage.setStatus("current")


class _HmConfigurationStatus_Type(Integer32):
    """Custom type hmConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInSync", 2),
          ("ok", 1))
    )


_HmConfigurationStatus_Type.__name__ = "Integer32"
_HmConfigurationStatus_Object = MibScalar
hmConfigurationStatus = _HmConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 12),
    _HmConfigurationStatus_Type()
)
hmConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmConfigurationStatus.setStatus("current")
_HmFSFileTable_Object = MibTable
hmFSFileTable = _HmFSFileTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 100)
)
if mibBuilder.loadTexts:
    hmFSFileTable.setStatus("current")
_HmFSFileEntry_Object = MibTableRow
hmFSFileEntry = _HmFSFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 100, 1)
)
hmFSFileEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmFSFileID"),
)
if mibBuilder.loadTexts:
    hmFSFileEntry.setStatus("current")


class _HmFSFileID_Type(Integer32):
    """Custom type hmFSFileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmFSFileID_Type.__name__ = "Integer32"
_HmFSFileID_Object = MibTableColumn
hmFSFileID = _HmFSFileID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 100, 1, 1),
    _HmFSFileID_Type()
)
hmFSFileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFSFileID.setStatus("current")
_HmFSFileName_Type = DisplayString
_HmFSFileName_Object = MibTableColumn
hmFSFileName = _HmFSFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 100, 1, 2),
    _HmFSFileName_Type()
)
hmFSFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFSFileName.setStatus("current")
_HmFSFileSize_Type = Integer32
_HmFSFileSize_Object = MibTableColumn
hmFSFileSize = _HmFSFileSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 100, 1, 3),
    _HmFSFileSize_Type()
)
hmFSFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFSFileSize.setStatus("current")
_HmFSFileDate_Type = TimeTicks
_HmFSFileDate_Object = MibTableColumn
hmFSFileDate = _HmFSFileDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 100, 1, 4),
    _HmFSFileDate_Type()
)
hmFSFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFSFileDate.setStatus("current")
_HmAutoconfigGroup_ObjectIdentity = ObjectIdentity
hmAutoconfigGroup = _HmAutoconfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 200)
)


class _HmAutoconfigAdapterStatus_Type(Integer32):
    """Custom type hmAutoconfigAdapterStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("autodisabled", 9),
          ("checksumErr", 7),
          ("genericErr", 8),
          ("notInSync", 4),
          ("notPresent", 1),
          ("ok", 3),
          ("outOfMemory", 5),
          ("removed", 2),
          ("wrongMachine", 6))
    )


_HmAutoconfigAdapterStatus_Type.__name__ = "Integer32"
_HmAutoconfigAdapterStatus_Object = MibScalar
hmAutoconfigAdapterStatus = _HmAutoconfigAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 200, 1),
    _HmAutoconfigAdapterStatus_Type()
)
hmAutoconfigAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAutoconfigAdapterStatus.setStatus("current")
_HmAutoconfigAdapterSerialNum_Type = DisplayString
_HmAutoconfigAdapterSerialNum_Object = MibScalar
hmAutoconfigAdapterSerialNum = _HmAutoconfigAdapterSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 200, 2),
    _HmAutoconfigAdapterSerialNum_Type()
)
hmAutoconfigAdapterSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAutoconfigAdapterSerialNum.setStatus("current")
_HmConfigWatchdogGroup_ObjectIdentity = ObjectIdentity
hmConfigWatchdogGroup = _HmConfigWatchdogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 201)
)


class _HmConfigWatchdogAdminStatus_Type(Integer32):
    """Custom type hmConfigWatchdogAdminStatus based on Integer32"""
    defaultValue = 2

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


_HmConfigWatchdogAdminStatus_Type.__name__ = "Integer32"
_HmConfigWatchdogAdminStatus_Object = MibScalar
hmConfigWatchdogAdminStatus = _HmConfigWatchdogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 201, 1),
    _HmConfigWatchdogAdminStatus_Type()
)
hmConfigWatchdogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmConfigWatchdogAdminStatus.setStatus("current")


class _HmConfigWatchdogOperStatus_Type(Integer32):
    """Custom type hmConfigWatchdogOperStatus based on Integer32"""
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


_HmConfigWatchdogOperStatus_Type.__name__ = "Integer32"
_HmConfigWatchdogOperStatus_Object = MibScalar
hmConfigWatchdogOperStatus = _HmConfigWatchdogOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 201, 2),
    _HmConfigWatchdogOperStatus_Type()
)
hmConfigWatchdogOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmConfigWatchdogOperStatus.setStatus("current")


class _HmConfigWatchdogTimeInterval_Type(Integer32):
    """Custom type hmConfigWatchdogTimeInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_HmConfigWatchdogTimeInterval_Type.__name__ = "Integer32"
_HmConfigWatchdogTimeInterval_Object = MibScalar
hmConfigWatchdogTimeInterval = _HmConfigWatchdogTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 201, 3),
    _HmConfigWatchdogTimeInterval_Type()
)
hmConfigWatchdogTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmConfigWatchdogTimeInterval.setStatus("current")
_HmConfigWatchdogTimerValue_Type = Integer32
_HmConfigWatchdogTimerValue_Object = MibScalar
hmConfigWatchdogTimerValue = _HmConfigWatchdogTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 201, 4),
    _HmConfigWatchdogTimerValue_Type()
)
hmConfigWatchdogTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmConfigWatchdogTimerValue.setStatus("current")
_HmConfigWatchdogIPAddress_Type = IpAddress
_HmConfigWatchdogIPAddress_Object = MibScalar
hmConfigWatchdogIPAddress = _HmConfigWatchdogIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 4, 201, 5),
    _HmConfigWatchdogIPAddress_Type()
)
hmConfigWatchdogIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmConfigWatchdogIPAddress.setStatus("current")
_HmTempTable_ObjectIdentity = ObjectIdentity
hmTempTable = _HmTempTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 5)
)
_HmTemperature_Type = Integer32
_HmTemperature_Object = MibScalar
hmTemperature = _HmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 5, 1),
    _HmTemperature_Type()
)
hmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTemperature.setStatus("current")


class _HmTempUprLimit_Type(Integer32):
    """Custom type hmTempUprLimit based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 99),
    )


_HmTempUprLimit_Type.__name__ = "Integer32"
_HmTempUprLimit_Object = MibScalar
hmTempUprLimit = _HmTempUprLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 5, 2),
    _HmTempUprLimit_Type()
)
hmTempUprLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTempUprLimit.setStatus("current")


class _HmTempLwrLimit_Type(Integer32):
    """Custom type hmTempLwrLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 99),
    )


_HmTempLwrLimit_Type.__name__ = "Integer32"
_HmTempLwrLimit_Object = MibScalar
hmTempLwrLimit = _HmTempLwrLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 5, 3),
    _HmTempLwrLimit_Type()
)
hmTempLwrLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTempLwrLimit.setStatus("current")
_HmNeighbourAgentTable_Object = MibTable
hmNeighbourAgentTable = _HmNeighbourAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 6)
)
if mibBuilder.loadTexts:
    hmNeighbourAgentTable.setStatus("current")
_HmNeighbourAgentEntry_Object = MibTableRow
hmNeighbourAgentEntry = _HmNeighbourAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 6, 1)
)
hmNeighbourAgentEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmNeighbourSlot"),
)
if mibBuilder.loadTexts:
    hmNeighbourAgentEntry.setStatus("current")


class _HmNeighbourSlot_Type(Integer32):
    """Custom type hmNeighbourSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_HmNeighbourSlot_Type.__name__ = "Integer32"
_HmNeighbourSlot_Object = MibTableColumn
hmNeighbourSlot = _HmNeighbourSlot_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 6, 1, 1),
    _HmNeighbourSlot_Type()
)
hmNeighbourSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNeighbourSlot.setStatus("current")
_HmNeighbourIpAddress_Type = IpAddress
_HmNeighbourIpAddress_Object = MibTableColumn
hmNeighbourIpAddress = _HmNeighbourIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 6, 1, 2),
    _HmNeighbourIpAddress_Type()
)
hmNeighbourIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNeighbourIpAddress.setStatus("current")
_HmAuthGroup_ObjectIdentity = ObjectIdentity
hmAuthGroup = _HmAuthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7)
)


class _HmAuthHostTableEntriesMax_Type(Integer32):
    """Custom type hmAuthHostTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmAuthHostTableEntriesMax_Type.__name__ = "Integer32"
_HmAuthHostTableEntriesMax_Object = MibScalar
hmAuthHostTableEntriesMax = _HmAuthHostTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 1),
    _HmAuthHostTableEntriesMax_Type()
)
hmAuthHostTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAuthHostTableEntriesMax.setStatus("current")


class _HmAuthCommTableEntriesMax_Type(Integer32):
    """Custom type hmAuthCommTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmAuthCommTableEntriesMax_Type.__name__ = "Integer32"
_HmAuthCommTableEntriesMax_Object = MibScalar
hmAuthCommTableEntriesMax = _HmAuthCommTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 2),
    _HmAuthCommTableEntriesMax_Type()
)
hmAuthCommTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAuthCommTableEntriesMax.setStatus("current")
_HmAuthCommTable_Object = MibTable
hmAuthCommTable = _HmAuthCommTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 3)
)
if mibBuilder.loadTexts:
    hmAuthCommTable.setStatus("current")
_HmAuthCommEntry_Object = MibTableRow
hmAuthCommEntry = _HmAuthCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 3, 1)
)
hmAuthCommEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmAuthCommIndex"),
)
if mibBuilder.loadTexts:
    hmAuthCommEntry.setStatus("current")


class _HmAuthCommIndex_Type(Integer32):
    """Custom type hmAuthCommIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmAuthCommIndex_Type.__name__ = "Integer32"
_HmAuthCommIndex_Object = MibTableColumn
hmAuthCommIndex = _HmAuthCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 3, 1, 1),
    _HmAuthCommIndex_Type()
)
hmAuthCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAuthCommIndex.setStatus("current")


class _HmAuthCommName_Type(DisplayString):
    """Custom type hmAuthCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmAuthCommName_Type.__name__ = "DisplayString"
_HmAuthCommName_Object = MibTableColumn
hmAuthCommName = _HmAuthCommName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 3, 1, 2),
    _HmAuthCommName_Type()
)
hmAuthCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthCommName.setStatus("current")


class _HmAuthCommPerm_Type(Integer32):
    """Custom type hmAuthCommPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perm-ro", 1),
          ("perm-rw", 2))
    )


_HmAuthCommPerm_Type.__name__ = "Integer32"
_HmAuthCommPerm_Object = MibTableColumn
hmAuthCommPerm = _HmAuthCommPerm_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 3, 1, 3),
    _HmAuthCommPerm_Type()
)
hmAuthCommPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthCommPerm.setStatus("current")


class _HmAuthCommState_Type(Integer32):
    """Custom type hmAuthCommState based on Integer32"""
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
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1),
          ("invalid", 4))
    )


_HmAuthCommState_Type.__name__ = "Integer32"
_HmAuthCommState_Object = MibTableColumn
hmAuthCommState = _HmAuthCommState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 3, 1, 4),
    _HmAuthCommState_Type()
)
hmAuthCommState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthCommState.setStatus("current")
_HmAuthHostTable_Object = MibTable
hmAuthHostTable = _HmAuthHostTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4)
)
if mibBuilder.loadTexts:
    hmAuthHostTable.setStatus("current")
_HmAuthHostEntry_Object = MibTableRow
hmAuthHostEntry = _HmAuthHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4, 1)
)
hmAuthHostEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmAuthHostIndex"),
)
if mibBuilder.loadTexts:
    hmAuthHostEntry.setStatus("current")


class _HmAuthHostIndex_Type(Integer32):
    """Custom type hmAuthHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmAuthHostIndex_Type.__name__ = "Integer32"
_HmAuthHostIndex_Object = MibTableColumn
hmAuthHostIndex = _HmAuthHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4, 1, 1),
    _HmAuthHostIndex_Type()
)
hmAuthHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAuthHostIndex.setStatus("current")


class _HmAuthHostName_Type(DisplayString):
    """Custom type hmAuthHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmAuthHostName_Type.__name__ = "DisplayString"
_HmAuthHostName_Object = MibTableColumn
hmAuthHostName = _HmAuthHostName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4, 1, 2),
    _HmAuthHostName_Type()
)
hmAuthHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthHostName.setStatus("current")
_HmAuthHostCommIndex_Type = Integer32
_HmAuthHostCommIndex_Object = MibTableColumn
hmAuthHostCommIndex = _HmAuthHostCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4, 1, 3),
    _HmAuthHostCommIndex_Type()
)
hmAuthHostCommIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthHostCommIndex.setStatus("current")
_HmAuthHostIpAddress_Type = IpAddress
_HmAuthHostIpAddress_Object = MibTableColumn
hmAuthHostIpAddress = _HmAuthHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4, 1, 4),
    _HmAuthHostIpAddress_Type()
)
hmAuthHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthHostIpAddress.setStatus("current")
_HmAuthHostIpMask_Type = IpAddress
_HmAuthHostIpMask_Object = MibTableColumn
hmAuthHostIpMask = _HmAuthHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4, 1, 5),
    _HmAuthHostIpMask_Type()
)
hmAuthHostIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthHostIpMask.setStatus("current")


class _HmAuthHostState_Type(Integer32):
    """Custom type hmAuthHostState based on Integer32"""
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
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1),
          ("invalid", 4))
    )


_HmAuthHostState_Type.__name__ = "Integer32"
_HmAuthHostState_Object = MibTableColumn
hmAuthHostState = _HmAuthHostState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 7, 4, 1, 6),
    _HmAuthHostState_Type()
)
hmAuthHostState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAuthHostState.setStatus("current")
_HmTrapGroup_ObjectIdentity = ObjectIdentity
hmTrapGroup = _HmTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8)
)


class _HmTrapCommTableEntriesMax_Type(Integer32):
    """Custom type hmTrapCommTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmTrapCommTableEntriesMax_Type.__name__ = "Integer32"
_HmTrapCommTableEntriesMax_Object = MibScalar
hmTrapCommTableEntriesMax = _HmTrapCommTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 1),
    _HmTrapCommTableEntriesMax_Type()
)
hmTrapCommTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrapCommTableEntriesMax.setStatus("current")


class _HmTrapDestTableEntriesMax_Type(Integer32):
    """Custom type hmTrapDestTableEntriesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmTrapDestTableEntriesMax_Type.__name__ = "Integer32"
_HmTrapDestTableEntriesMax_Object = MibScalar
hmTrapDestTableEntriesMax = _HmTrapDestTableEntriesMax_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 2),
    _HmTrapDestTableEntriesMax_Type()
)
hmTrapDestTableEntriesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrapDestTableEntriesMax.setStatus("current")
_HmTrapCommTable_Object = MibTable
hmTrapCommTable = _HmTrapCommTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3)
)
if mibBuilder.loadTexts:
    hmTrapCommTable.setStatus("current")
_HmTrapCommEntry_Object = MibTableRow
hmTrapCommEntry = _HmTrapCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1)
)
hmTrapCommEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmTrapCommIndex"),
)
if mibBuilder.loadTexts:
    hmTrapCommEntry.setStatus("current")


class _HmTrapCommIndex_Type(Integer32):
    """Custom type hmTrapCommIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmTrapCommIndex_Type.__name__ = "Integer32"
_HmTrapCommIndex_Object = MibTableColumn
hmTrapCommIndex = _HmTrapCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 1),
    _HmTrapCommIndex_Type()
)
hmTrapCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrapCommIndex.setStatus("current")
_HmTrapCommCommIndex_Type = Integer32
_HmTrapCommCommIndex_Object = MibTableColumn
hmTrapCommCommIndex = _HmTrapCommCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 2),
    _HmTrapCommCommIndex_Type()
)
hmTrapCommCommIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommCommIndex.setStatus("current")


class _HmTrapCommColdStart_Type(Integer32):
    """Custom type hmTrapCommColdStart based on Integer32"""
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


_HmTrapCommColdStart_Type.__name__ = "Integer32"
_HmTrapCommColdStart_Object = MibTableColumn
hmTrapCommColdStart = _HmTrapCommColdStart_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 3),
    _HmTrapCommColdStart_Type()
)
hmTrapCommColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommColdStart.setStatus("current")


class _HmTrapCommLinkDown_Type(Integer32):
    """Custom type hmTrapCommLinkDown based on Integer32"""
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


_HmTrapCommLinkDown_Type.__name__ = "Integer32"
_HmTrapCommLinkDown_Object = MibTableColumn
hmTrapCommLinkDown = _HmTrapCommLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 4),
    _HmTrapCommLinkDown_Type()
)
hmTrapCommLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommLinkDown.setStatus("current")


class _HmTrapCommLinkUp_Type(Integer32):
    """Custom type hmTrapCommLinkUp based on Integer32"""
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


_HmTrapCommLinkUp_Type.__name__ = "Integer32"
_HmTrapCommLinkUp_Object = MibTableColumn
hmTrapCommLinkUp = _HmTrapCommLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 5),
    _HmTrapCommLinkUp_Type()
)
hmTrapCommLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommLinkUp.setStatus("current")


class _HmTrapCommAuthentication_Type(Integer32):
    """Custom type hmTrapCommAuthentication based on Integer32"""
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


_HmTrapCommAuthentication_Type.__name__ = "Integer32"
_HmTrapCommAuthentication_Object = MibTableColumn
hmTrapCommAuthentication = _HmTrapCommAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 6),
    _HmTrapCommAuthentication_Type()
)
hmTrapCommAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommAuthentication.setStatus("current")


class _HmTrapCommBridge_Type(Integer32):
    """Custom type hmTrapCommBridge based on Integer32"""
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


_HmTrapCommBridge_Type.__name__ = "Integer32"
_HmTrapCommBridge_Object = MibTableColumn
hmTrapCommBridge = _HmTrapCommBridge_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 7),
    _HmTrapCommBridge_Type()
)
hmTrapCommBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommBridge.setStatus("current")


class _HmTrapCommRMON_Type(Integer32):
    """Custom type hmTrapCommRMON based on Integer32"""
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


_HmTrapCommRMON_Type.__name__ = "Integer32"
_HmTrapCommRMON_Object = MibTableColumn
hmTrapCommRMON = _HmTrapCommRMON_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 8),
    _HmTrapCommRMON_Type()
)
hmTrapCommRMON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommRMON.setStatus("current")


class _HmTrapCommUsergroup_Type(Integer32):
    """Custom type hmTrapCommUsergroup based on Integer32"""
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


_HmTrapCommUsergroup_Type.__name__ = "Integer32"
_HmTrapCommUsergroup_Object = MibTableColumn
hmTrapCommUsergroup = _HmTrapCommUsergroup_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 9),
    _HmTrapCommUsergroup_Type()
)
hmTrapCommUsergroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommUsergroup.setStatus("current")


class _HmTrapCommDualHoming_Type(Integer32):
    """Custom type hmTrapCommDualHoming based on Integer32"""
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


_HmTrapCommDualHoming_Type.__name__ = "Integer32"
_HmTrapCommDualHoming_Object = MibTableColumn
hmTrapCommDualHoming = _HmTrapCommDualHoming_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 10),
    _HmTrapCommDualHoming_Type()
)
hmTrapCommDualHoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommDualHoming.setStatus("current")


class _HmTrapCommChassis_Type(Integer32):
    """Custom type hmTrapCommChassis based on Integer32"""
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


_HmTrapCommChassis_Type.__name__ = "Integer32"
_HmTrapCommChassis_Object = MibTableColumn
hmTrapCommChassis = _HmTrapCommChassis_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 11),
    _HmTrapCommChassis_Type()
)
hmTrapCommChassis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommChassis.setStatus("current")


class _HmTrapCommState_Type(Integer32):
    """Custom type hmTrapCommState based on Integer32"""
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
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1),
          ("invalid", 4))
    )


_HmTrapCommState_Type.__name__ = "Integer32"
_HmTrapCommState_Object = MibTableColumn
hmTrapCommState = _HmTrapCommState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 3, 1, 12),
    _HmTrapCommState_Type()
)
hmTrapCommState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapCommState.setStatus("current")
_HmTrapDestTable_Object = MibTable
hmTrapDestTable = _HmTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4)
)
if mibBuilder.loadTexts:
    hmTrapDestTable.setStatus("current")
_HmTrapDestEntry_Object = MibTableRow
hmTrapDestEntry = _HmTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4, 1)
)
hmTrapDestEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmTrapDestIndex"),
)
if mibBuilder.loadTexts:
    hmTrapDestEntry.setStatus("current")


class _HmTrapDestIndex_Type(Integer32):
    """Custom type hmTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HmTrapDestIndex_Type.__name__ = "Integer32"
_HmTrapDestIndex_Object = MibTableColumn
hmTrapDestIndex = _HmTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4, 1, 1),
    _HmTrapDestIndex_Type()
)
hmTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmTrapDestIndex.setStatus("current")


class _HmTrapDestName_Type(DisplayString):
    """Custom type hmTrapDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HmTrapDestName_Type.__name__ = "DisplayString"
_HmTrapDestName_Object = MibTableColumn
hmTrapDestName = _HmTrapDestName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4, 1, 2),
    _HmTrapDestName_Type()
)
hmTrapDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapDestName.setStatus("current")
_HmTrapDestCommIndex_Type = Integer32
_HmTrapDestCommIndex_Object = MibTableColumn
hmTrapDestCommIndex = _HmTrapDestCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4, 1, 3),
    _HmTrapDestCommIndex_Type()
)
hmTrapDestCommIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapDestCommIndex.setStatus("current")
_HmTrapDestIpAddress_Type = IpAddress
_HmTrapDestIpAddress_Object = MibTableColumn
hmTrapDestIpAddress = _HmTrapDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4, 1, 4),
    _HmTrapDestIpAddress_Type()
)
hmTrapDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapDestIpAddress.setStatus("current")
_HmTrapDestIpMask_Type = IpAddress
_HmTrapDestIpMask_Object = MibTableColumn
hmTrapDestIpMask = _HmTrapDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4, 1, 5),
    _HmTrapDestIpMask_Type()
)
hmTrapDestIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapDestIpMask.setStatus("obsolete")


class _HmTrapDestState_Type(Integer32):
    """Custom type hmTrapDestState based on Integer32"""
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
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1),
          ("invalid", 4))
    )


_HmTrapDestState_Type.__name__ = "Integer32"
_HmTrapDestState_Object = MibTableColumn
hmTrapDestState = _HmTrapDestState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 8, 4, 1, 6),
    _HmTrapDestState_Type()
)
hmTrapDestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmTrapDestState.setStatus("current")
_HmLastAccessGroup_ObjectIdentity = ObjectIdentity
hmLastAccessGroup = _HmLastAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 9)
)
_HmLastIpAddr_Type = IpAddress
_HmLastIpAddr_Object = MibScalar
hmLastIpAddr = _HmLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 9, 1),
    _HmLastIpAddr_Type()
)
hmLastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLastIpAddr.setStatus("current")
_HmLastPort_Type = Integer32
_HmLastPort_Object = MibScalar
hmLastPort = _HmLastPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 9, 2),
    _HmLastPort_Type()
)
hmLastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLastPort.setStatus("current")
_HmLastCommunity_Type = DisplayString
_HmLastCommunity_Object = MibScalar
hmLastCommunity = _HmLastCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 9, 3),
    _HmLastCommunity_Type()
)
hmLastCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLastCommunity.setStatus("current")
_HmLastLoginUserName_Type = DisplayString
_HmLastLoginUserName_Object = MibScalar
hmLastLoginUserName = _HmLastLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 9, 4),
    _HmLastLoginUserName_Type()
)
hmLastLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLastLoginUserName.setStatus("current")
_HmMulticast_ObjectIdentity = ObjectIdentity
hmMulticast = _HmMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10)
)
_HmIGMPGroup_ObjectIdentity = ObjectIdentity
hmIGMPGroup = _HmIGMPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1)
)
_HmIGMPSnoop_ObjectIdentity = ObjectIdentity
hmIGMPSnoop = _HmIGMPSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2)
)


class _HmIGMPSnoopStatus_Type(Integer32):
    """Custom type hmIGMPSnoopStatus based on Integer32"""
    defaultValue = 2

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


_HmIGMPSnoopStatus_Type.__name__ = "Integer32"
_HmIGMPSnoopStatus_Object = MibScalar
hmIGMPSnoopStatus = _HmIGMPSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 1),
    _HmIGMPSnoopStatus_Type()
)
hmIGMPSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopStatus.setStatus("current")


class _HmIGMPSnoopAgingTime_Type(Integer32):
    """Custom type hmIGMPSnoopAgingTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_HmIGMPSnoopAgingTime_Type.__name__ = "Integer32"
_HmIGMPSnoopAgingTime_Object = MibScalar
hmIGMPSnoopAgingTime = _HmIGMPSnoopAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 2),
    _HmIGMPSnoopAgingTime_Type()
)
hmIGMPSnoopAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopAgingTime.setStatus("current")


class _HmIGMPSnoopUnknownMode_Type(Integer32):
    """Custom type hmIGMPSnoopUnknownMode based on Integer32"""
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
        *(("discard", 1),
          ("flood", 2),
          ("query-ports", 3))
    )


_HmIGMPSnoopUnknownMode_Type.__name__ = "Integer32"
_HmIGMPSnoopUnknownMode_Object = MibScalar
hmIGMPSnoopUnknownMode = _HmIGMPSnoopUnknownMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 3),
    _HmIGMPSnoopUnknownMode_Type()
)
hmIGMPSnoopUnknownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopUnknownMode.setStatus("current")


class _HmIGMPSnoopUnknownAgingTime_Type(Integer32):
    """Custom type hmIGMPSnoopUnknownAgingTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_HmIGMPSnoopUnknownAgingTime_Type.__name__ = "Integer32"
_HmIGMPSnoopUnknownAgingTime_Object = MibScalar
hmIGMPSnoopUnknownAgingTime = _HmIGMPSnoopUnknownAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 4),
    _HmIGMPSnoopUnknownAgingTime_Type()
)
hmIGMPSnoopUnknownAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopUnknownAgingTime.setStatus("current")


class _HmIGMPSnoopUnknownLookupInterval_Type(Integer32):
    """Custom type hmIGMPSnoopUnknownLookupInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3599),
    )


_HmIGMPSnoopUnknownLookupInterval_Type.__name__ = "Integer32"
_HmIGMPSnoopUnknownLookupInterval_Object = MibScalar
hmIGMPSnoopUnknownLookupInterval = _HmIGMPSnoopUnknownLookupInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 5),
    _HmIGMPSnoopUnknownLookupInterval_Type()
)
hmIGMPSnoopUnknownLookupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopUnknownLookupInterval.setStatus("current")


class _HmIGMPSnoopUnknownLookupResponseTime_Type(Integer32):
    """Custom type hmIGMPSnoopUnknownLookupResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3598),
    )


_HmIGMPSnoopUnknownLookupResponseTime_Type.__name__ = "Integer32"
_HmIGMPSnoopUnknownLookupResponseTime_Object = MibScalar
hmIGMPSnoopUnknownLookupResponseTime = _HmIGMPSnoopUnknownLookupResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 6),
    _HmIGMPSnoopUnknownLookupResponseTime_Type()
)
hmIGMPSnoopUnknownLookupResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopUnknownLookupResponseTime.setStatus("current")


class _HmIGMPSnoopQuerierToPortmask_Type(Integer32):
    """Custom type hmIGMPSnoopQuerierToPortmask based on Integer32"""
    defaultValue = 2

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


_HmIGMPSnoopQuerierToPortmask_Type.__name__ = "Integer32"
_HmIGMPSnoopQuerierToPortmask_Object = MibScalar
hmIGMPSnoopQuerierToPortmask = _HmIGMPSnoopQuerierToPortmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 7),
    _HmIGMPSnoopQuerierToPortmask_Type()
)
hmIGMPSnoopQuerierToPortmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopQuerierToPortmask.setStatus("current")
_HmIGMPSnoopQuerierIPAddress_Type = IpAddress
_HmIGMPSnoopQuerierIPAddress_Object = MibScalar
hmIGMPSnoopQuerierIPAddress = _HmIGMPSnoopQuerierIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 8),
    _HmIGMPSnoopQuerierIPAddress_Type()
)
hmIGMPSnoopQuerierIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIGMPSnoopQuerierIPAddress.setStatus("current")
_HmIGMPSnoopQueryTable_Object = MibTable
hmIGMPSnoopQueryTable = _HmIGMPSnoopQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryTable.setStatus("current")
_HmIGMPSnoopQueryEntry_Object = MibTableRow
hmIGMPSnoopQueryEntry = _HmIGMPSnoopQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 10, 1)
)
hmIGMPSnoopQueryEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmIGMPSnoopQueryVlanIndex"),
)
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryEntry.setStatus("current")


class _HmIGMPSnoopQueryVlanIndex_Type(Integer32):
    """Custom type hmIGMPSnoopQueryVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HmIGMPSnoopQueryVlanIndex_Type.__name__ = "Integer32"
_HmIGMPSnoopQueryVlanIndex_Object = MibTableColumn
hmIGMPSnoopQueryVlanIndex = _HmIGMPSnoopQueryVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 10, 1, 1),
    _HmIGMPSnoopQueryVlanIndex_Type()
)
hmIGMPSnoopQueryVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryVlanIndex.setStatus("current")
_HmIGMPSnoopQueryPorts_Type = OctetString
_HmIGMPSnoopQueryPorts_Object = MibTableColumn
hmIGMPSnoopQueryPorts = _HmIGMPSnoopQueryPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 10, 1, 2),
    _HmIGMPSnoopQueryPorts_Type()
)
hmIGMPSnoopQueryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryPorts.setStatus("current")
_HmIGMPSnoopFilterTable_Object = MibTable
hmIGMPSnoopFilterTable = _HmIGMPSnoopFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hmIGMPSnoopFilterTable.setStatus("current")
_HmIGMPSnoopFilterEntry_Object = MibTableRow
hmIGMPSnoopFilterEntry = _HmIGMPSnoopFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 11, 1)
)
hmIGMPSnoopFilterEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmIGMPSnoopFilterVlanIndex"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmIGMPSnoopFilterAddress"),
)
if mibBuilder.loadTexts:
    hmIGMPSnoopFilterEntry.setStatus("current")


class _HmIGMPSnoopFilterVlanIndex_Type(Integer32):
    """Custom type hmIGMPSnoopFilterVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HmIGMPSnoopFilterVlanIndex_Type.__name__ = "Integer32"
_HmIGMPSnoopFilterVlanIndex_Object = MibTableColumn
hmIGMPSnoopFilterVlanIndex = _HmIGMPSnoopFilterVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 11, 1, 1),
    _HmIGMPSnoopFilterVlanIndex_Type()
)
hmIGMPSnoopFilterVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIGMPSnoopFilterVlanIndex.setStatus("current")
_HmIGMPSnoopFilterAddress_Type = MacAddress
_HmIGMPSnoopFilterAddress_Object = MibTableColumn
hmIGMPSnoopFilterAddress = _HmIGMPSnoopFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 11, 1, 2),
    _HmIGMPSnoopFilterAddress_Type()
)
hmIGMPSnoopFilterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIGMPSnoopFilterAddress.setStatus("current")
_HmIGMPSnoopFilterLearntPorts_Type = OctetString
_HmIGMPSnoopFilterLearntPorts_Object = MibTableColumn
hmIGMPSnoopFilterLearntPorts = _HmIGMPSnoopFilterLearntPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 11, 1, 3),
    _HmIGMPSnoopFilterLearntPorts_Type()
)
hmIGMPSnoopFilterLearntPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIGMPSnoopFilterLearntPorts.setStatus("current")
_HmIGMPSnoopForwardAllTable_Object = MibTable
hmIGMPSnoopForwardAllTable = _HmIGMPSnoopForwardAllTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hmIGMPSnoopForwardAllTable.setStatus("current")
_HmIGMPSnoopForwardAllEntry_Object = MibTableRow
hmIGMPSnoopForwardAllEntry = _HmIGMPSnoopForwardAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 12, 1)
)
hmIGMPSnoopForwardAllEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmIGMPSnoopForwardAllVlanIndex"),
)
if mibBuilder.loadTexts:
    hmIGMPSnoopForwardAllEntry.setStatus("current")


class _HmIGMPSnoopForwardAllVlanIndex_Type(Integer32):
    """Custom type hmIGMPSnoopForwardAllVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HmIGMPSnoopForwardAllVlanIndex_Type.__name__ = "Integer32"
_HmIGMPSnoopForwardAllVlanIndex_Object = MibTableColumn
hmIGMPSnoopForwardAllVlanIndex = _HmIGMPSnoopForwardAllVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 12, 1, 1),
    _HmIGMPSnoopForwardAllVlanIndex_Type()
)
hmIGMPSnoopForwardAllVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIGMPSnoopForwardAllVlanIndex.setStatus("current")
_HmIGMPSnoopForwardAllStaticPorts_Type = OctetString
_HmIGMPSnoopForwardAllStaticPorts_Object = MibTableColumn
hmIGMPSnoopForwardAllStaticPorts = _HmIGMPSnoopForwardAllStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 12, 1, 2),
    _HmIGMPSnoopForwardAllStaticPorts_Type()
)
hmIGMPSnoopForwardAllStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopForwardAllStaticPorts.setStatus("current")
_HmIGMPSnoopQueryStaticTable_Object = MibTable
hmIGMPSnoopQueryStaticTable = _HmIGMPSnoopQueryStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryStaticTable.setStatus("current")
_HmIGMPSnoopQueryStaticEntry_Object = MibTableRow
hmIGMPSnoopQueryStaticEntry = _HmIGMPSnoopQueryStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 13, 1)
)
hmIGMPSnoopQueryStaticEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmIGMPSnoopQueryStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryStaticEntry.setStatus("current")


class _HmIGMPSnoopQueryStaticVlanIndex_Type(Integer32):
    """Custom type hmIGMPSnoopQueryStaticVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HmIGMPSnoopQueryStaticVlanIndex_Type.__name__ = "Integer32"
_HmIGMPSnoopQueryStaticVlanIndex_Object = MibTableColumn
hmIGMPSnoopQueryStaticVlanIndex = _HmIGMPSnoopQueryStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 13, 1, 1),
    _HmIGMPSnoopQueryStaticVlanIndex_Type()
)
hmIGMPSnoopQueryStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryStaticVlanIndex.setStatus("current")
_HmIGMPSnoopQueryStaticPorts_Type = OctetString
_HmIGMPSnoopQueryStaticPorts_Object = MibTableColumn
hmIGMPSnoopQueryStaticPorts = _HmIGMPSnoopQueryStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 13, 1, 2),
    _HmIGMPSnoopQueryStaticPorts_Type()
)
hmIGMPSnoopQueryStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryStaticPorts.setStatus("current")
_HmIGMPSnoopQueryStaticAutomaticPorts_Type = OctetString
_HmIGMPSnoopQueryStaticAutomaticPorts_Object = MibTableColumn
hmIGMPSnoopQueryStaticAutomaticPorts = _HmIGMPSnoopQueryStaticAutomaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 13, 1, 3),
    _HmIGMPSnoopQueryStaticAutomaticPorts_Type()
)
hmIGMPSnoopQueryStaticAutomaticPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryStaticAutomaticPorts.setStatus("current")
_HmIGMPSnoopQueryStaticAutomaticPortsEnable_Type = OctetString
_HmIGMPSnoopQueryStaticAutomaticPortsEnable_Object = MibTableColumn
hmIGMPSnoopQueryStaticAutomaticPortsEnable = _HmIGMPSnoopQueryStaticAutomaticPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 13, 1, 4),
    _HmIGMPSnoopQueryStaticAutomaticPortsEnable_Type()
)
hmIGMPSnoopQueryStaticAutomaticPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPSnoopQueryStaticAutomaticPortsEnable.setStatus("current")
_HmIGMPQuerierGroup_ObjectIdentity = ObjectIdentity
hmIGMPQuerierGroup = _HmIGMPQuerierGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 100)
)


class _HmIGMPQuerierStatus_Type(Integer32):
    """Custom type hmIGMPQuerierStatus based on Integer32"""
    defaultValue = 2

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


_HmIGMPQuerierStatus_Type.__name__ = "Integer32"
_HmIGMPQuerierStatus_Object = MibScalar
hmIGMPQuerierStatus = _HmIGMPQuerierStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 100, 1),
    _HmIGMPQuerierStatus_Type()
)
hmIGMPQuerierStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPQuerierStatus.setStatus("current")


class _HmIGMPQuerierMode_Type(Integer32):
    """Custom type hmIGMPQuerierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-querier", 2),
          ("querier", 1))
    )


_HmIGMPQuerierMode_Type.__name__ = "Integer32"
_HmIGMPQuerierMode_Object = MibScalar
hmIGMPQuerierMode = _HmIGMPQuerierMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 100, 2),
    _HmIGMPQuerierMode_Type()
)
hmIGMPQuerierMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmIGMPQuerierMode.setStatus("current")


class _HmIGMPQuerierTransmitInterval_Type(Integer32):
    """Custom type hmIGMPQuerierTransmitInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3599),
    )


_HmIGMPQuerierTransmitInterval_Type.__name__ = "Integer32"
_HmIGMPQuerierTransmitInterval_Object = MibScalar
hmIGMPQuerierTransmitInterval = _HmIGMPQuerierTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 100, 3),
    _HmIGMPQuerierTransmitInterval_Type()
)
hmIGMPQuerierTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPQuerierTransmitInterval.setStatus("current")


class _HmIGMPQuerierMaxResponseTime_Type(Integer32):
    """Custom type hmIGMPQuerierMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3598),
    )


_HmIGMPQuerierMaxResponseTime_Type.__name__ = "Integer32"
_HmIGMPQuerierMaxResponseTime_Object = MibScalar
hmIGMPQuerierMaxResponseTime = _HmIGMPQuerierMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 100, 4),
    _HmIGMPQuerierMaxResponseTime_Type()
)
hmIGMPQuerierMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPQuerierMaxResponseTime.setStatus("current")


class _HmIGMPQuerierProtocolVersion_Type(Integer32):
    """Custom type hmIGMPQuerierProtocolVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HmIGMPQuerierProtocolVersion_Type.__name__ = "Integer32"
_HmIGMPQuerierProtocolVersion_Object = MibScalar
hmIGMPQuerierProtocolVersion = _HmIGMPQuerierProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 1, 2, 100, 5),
    _HmIGMPQuerierProtocolVersion_Type()
)
hmIGMPQuerierProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmIGMPQuerierProtocolVersion.setStatus("current")
_HmGMRPGroup_ObjectIdentity = ObjectIdentity
hmGMRPGroup = _HmGMRPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 2)
)
_HmGMRP_ObjectIdentity = ObjectIdentity
hmGMRP = _HmGMRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 2, 1)
)


class _HmGmrpUnknownMode_Type(Integer32):
    """Custom type hmGmrpUnknownMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("flood", 2))
    )


_HmGmrpUnknownMode_Type.__name__ = "Integer32"
_HmGmrpUnknownMode_Object = MibScalar
hmGmrpUnknownMode = _HmGmrpUnknownMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 10, 2, 1, 1),
    _HmGmrpUnknownMode_Type()
)
hmGmrpUnknownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmGmrpUnknownMode.setStatus("current")
_HmRelayGroup_ObjectIdentity = ObjectIdentity
hmRelayGroup = _HmRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11)
)


class _HmRelayOption82Status_Type(Integer32):
    """Custom type hmRelayOption82Status based on Integer32"""
    defaultValue = 2

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


_HmRelayOption82Status_Type.__name__ = "Integer32"
_HmRelayOption82Status_Object = MibScalar
hmRelayOption82Status = _HmRelayOption82Status_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 1),
    _HmRelayOption82Status_Type()
)
hmRelayOption82Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayOption82Status.setStatus("current")


class _HmRelayOptionRemoteIDType_Type(Integer32):
    """Custom type hmRelayOptionRemoteIDType based on Integer32"""
    defaultValue = 2

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
        *(("client-id", 3),
          ("ip", 1),
          ("mac", 2),
          ("other", 4))
    )


_HmRelayOptionRemoteIDType_Type.__name__ = "Integer32"
_HmRelayOptionRemoteIDType_Object = MibScalar
hmRelayOptionRemoteIDType = _HmRelayOptionRemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 2),
    _HmRelayOptionRemoteIDType_Type()
)
hmRelayOptionRemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayOptionRemoteIDType.setStatus("current")
_HmRelayOptionRemoteID_Type = OctetString
_HmRelayOptionRemoteID_Object = MibScalar
hmRelayOptionRemoteID = _HmRelayOptionRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 3),
    _HmRelayOptionRemoteID_Type()
)
hmRelayOptionRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayOptionRemoteID.setStatus("current")
_HmRelayOptionRemoteIDValue_Type = OctetString
_HmRelayOptionRemoteIDValue_Object = MibScalar
hmRelayOptionRemoteIDValue = _HmRelayOptionRemoteIDValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 4),
    _HmRelayOptionRemoteIDValue_Type()
)
hmRelayOptionRemoteIDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayOptionRemoteIDValue.setStatus("current")
_HmRelayServerGroup_ObjectIdentity = ObjectIdentity
hmRelayServerGroup = _HmRelayServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 10)
)
_HmRelayDHCPServerIpAddr_Type = IpAddress
_HmRelayDHCPServerIpAddr_Object = MibScalar
hmRelayDHCPServerIpAddr = _HmRelayDHCPServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 10, 1),
    _HmRelayDHCPServerIpAddr_Type()
)
hmRelayDHCPServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayDHCPServerIpAddr.setStatus("current")
_HmRelayDHCPServer2IpAddr_Type = IpAddress
_HmRelayDHCPServer2IpAddr_Object = MibScalar
hmRelayDHCPServer2IpAddr = _HmRelayDHCPServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 10, 2),
    _HmRelayDHCPServer2IpAddr_Type()
)
hmRelayDHCPServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayDHCPServer2IpAddr.setStatus("current")
_HmRelayDHCPServer3IpAddr_Type = IpAddress
_HmRelayDHCPServer3IpAddr_Object = MibScalar
hmRelayDHCPServer3IpAddr = _HmRelayDHCPServer3IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 10, 3),
    _HmRelayDHCPServer3IpAddr_Type()
)
hmRelayDHCPServer3IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayDHCPServer3IpAddr.setStatus("current")
_HmRelayDHCPServer4IpAddr_Type = IpAddress
_HmRelayDHCPServer4IpAddr_Object = MibScalar
hmRelayDHCPServer4IpAddr = _HmRelayDHCPServer4IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 10, 4),
    _HmRelayDHCPServer4IpAddr_Type()
)
hmRelayDHCPServer4IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayDHCPServer4IpAddr.setStatus("current")
_HmRelayInterfaceTable_Object = MibTable
hmRelayInterfaceTable = _HmRelayInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 11)
)
if mibBuilder.loadTexts:
    hmRelayInterfaceTable.setStatus("current")
_HmRelayInterfaceEntry_Object = MibTableRow
hmRelayInterfaceEntry = _HmRelayInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 11, 1)
)
hmRelayInterfaceEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmRelayIfaceGroupID"),
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmRelayIfaceID"),
)
if mibBuilder.loadTexts:
    hmRelayInterfaceEntry.setStatus("current")


class _HmRelayIfaceGroupID_Type(Integer32):
    """Custom type hmRelayIfaceGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmRelayIfaceGroupID_Type.__name__ = "Integer32"
_HmRelayIfaceGroupID_Object = MibTableColumn
hmRelayIfaceGroupID = _HmRelayIfaceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 11, 1, 1),
    _HmRelayIfaceGroupID_Type()
)
hmRelayIfaceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayIfaceGroupID.setStatus("current")


class _HmRelayIfaceID_Type(Integer32):
    """Custom type hmRelayIfaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmRelayIfaceID_Type.__name__ = "Integer32"
_HmRelayIfaceID_Object = MibTableColumn
hmRelayIfaceID = _HmRelayIfaceID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 11, 1, 2),
    _HmRelayIfaceID_Type()
)
hmRelayIfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayIfaceID.setStatus("current")


class _HmRelayIfaceOption82Enable_Type(Integer32):
    """Custom type hmRelayIfaceOption82Enable based on Integer32"""
    defaultValue = 1

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


_HmRelayIfaceOption82Enable_Type.__name__ = "Integer32"
_HmRelayIfaceOption82Enable_Object = MibTableColumn
hmRelayIfaceOption82Enable = _HmRelayIfaceOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 11, 1, 3),
    _HmRelayIfaceOption82Enable_Type()
)
hmRelayIfaceOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayIfaceOption82Enable.setStatus("current")


class _HmRelayIfaceBCRequestFwd_Type(Integer32):
    """Custom type hmRelayIfaceBCRequestFwd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HmRelayIfaceBCRequestFwd_Type.__name__ = "Integer32"
_HmRelayIfaceBCRequestFwd_Object = MibTableColumn
hmRelayIfaceBCRequestFwd = _HmRelayIfaceBCRequestFwd_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 11, 1, 4),
    _HmRelayIfaceBCRequestFwd_Type()
)
hmRelayIfaceBCRequestFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmRelayIfaceBCRequestFwd.setStatus("current")
_HmRelayIfaceCircuitID_Type = OctetString
_HmRelayIfaceCircuitID_Object = MibTableColumn
hmRelayIfaceCircuitID = _HmRelayIfaceCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 11, 1, 5),
    _HmRelayIfaceCircuitID_Type()
)
hmRelayIfaceCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayIfaceCircuitID.setStatus("current")
_HmRelayBCPktInCnt_Type = Counter32
_HmRelayBCPktInCnt_Object = MibScalar
hmRelayBCPktInCnt = _HmRelayBCPktInCnt_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 20),
    _HmRelayBCPktInCnt_Type()
)
hmRelayBCPktInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayBCPktInCnt.setStatus("current")
_HmRelayMCPktInCnt_Type = Counter32
_HmRelayMCPktInCnt_Object = MibScalar
hmRelayMCPktInCnt = _HmRelayMCPktInCnt_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 21),
    _HmRelayMCPktInCnt_Type()
)
hmRelayMCPktInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayMCPktInCnt.setStatus("current")
_HmRelayPktServerRelayCnt_Type = Counter32
_HmRelayPktServerRelayCnt_Object = MibScalar
hmRelayPktServerRelayCnt = _HmRelayPktServerRelayCnt_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 22),
    _HmRelayPktServerRelayCnt_Type()
)
hmRelayPktServerRelayCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayPktServerRelayCnt.setStatus("current")
_HmRelayPktClientRelayCnt_Type = Counter32
_HmRelayPktClientRelayCnt_Object = MibScalar
hmRelayPktClientRelayCnt = _HmRelayPktClientRelayCnt_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 23),
    _HmRelayPktClientRelayCnt_Type()
)
hmRelayPktClientRelayCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayPktClientRelayCnt.setStatus("current")
_HmRelayErrCnt_Type = Counter32
_HmRelayErrCnt_Object = MibScalar
hmRelayErrCnt = _HmRelayErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 24),
    _HmRelayErrCnt_Type()
)
hmRelayErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayErrCnt.setStatus("current")
_HmRelayLastDuplicateIP_Type = IpAddress
_HmRelayLastDuplicateIP_Object = MibScalar
hmRelayLastDuplicateIP = _HmRelayLastDuplicateIP_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 11, 25),
    _HmRelayLastDuplicateIP_Type()
)
hmRelayLastDuplicateIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmRelayLastDuplicateIP.setStatus("current")
_HmDeviceMonitoringGroup_ObjectIdentity = ObjectIdentity
hmDeviceMonitoringGroup = _HmDeviceMonitoringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12)
)
_HmSigConConfigTable_Object = MibTable
hmSigConConfigTable = _HmSigConConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1)
)
if mibBuilder.loadTexts:
    hmSigConConfigTable.setStatus("current")
_HmSigConConfigEntry_Object = MibTableRow
hmSigConConfigEntry = _HmSigConConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1)
)
hmSigConConfigEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSigConID"),
)
if mibBuilder.loadTexts:
    hmSigConConfigEntry.setStatus("current")


class _HmSigConID_Type(Integer32):
    """Custom type hmSigConID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HmSigConID_Type.__name__ = "Integer32"
_HmSigConID_Object = MibTableColumn
hmSigConID = _HmSigConID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 1),
    _HmSigConID_Type()
)
hmSigConID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigConID.setStatus("current")


class _HmSigConTrapEnable_Type(Integer32):
    """Custom type hmSigConTrapEnable based on Integer32"""
    defaultValue = 2

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


_HmSigConTrapEnable_Type.__name__ = "Integer32"
_HmSigConTrapEnable_Object = MibTableColumn
hmSigConTrapEnable = _HmSigConTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 2),
    _HmSigConTrapEnable_Type()
)
hmSigConTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConTrapEnable.setStatus("current")


class _HmSigConTrapCause_Type(Integer32):
    """Custom type hmSigConTrapCause based on Integer32"""
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
        *(("acaNotInSync", 10),
          ("acaRemoval", 8),
          ("controlLine", 3),
          ("fanFailure", 9),
          ("linkFailure", 2),
          ("moduleRemoval", 7),
          ("other", 1),
          ("psState", 5),
          ("redNotGuaranteed", 4),
          ("temperature", 6))
    )


_HmSigConTrapCause_Type.__name__ = "Integer32"
_HmSigConTrapCause_Object = MibTableColumn
hmSigConTrapCause = _HmSigConTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 3),
    _HmSigConTrapCause_Type()
)
hmSigConTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigConTrapCause.setStatus("current")
_HmSigConTrapCauseIndex_Type = Integer32
_HmSigConTrapCauseIndex_Object = MibTableColumn
hmSigConTrapCauseIndex = _HmSigConTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 4),
    _HmSigConTrapCauseIndex_Type()
)
hmSigConTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigConTrapCauseIndex.setStatus("current")


class _HmSigConMode_Type(Integer32):
    """Custom type hmSigConMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("devicestate", 3),
          ("manual", 1),
          ("monitor", 2))
    )


_HmSigConMode_Type.__name__ = "Integer32"
_HmSigConMode_Object = MibTableColumn
hmSigConMode = _HmSigConMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 5),
    _HmSigConMode_Type()
)
hmSigConMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConMode.setStatus("current")


class _HmSigConManualActivate_Type(Integer32):
    """Custom type hmSigConManualActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("open", 2))
    )


_HmSigConManualActivate_Type.__name__ = "Integer32"
_HmSigConManualActivate_Object = MibTableColumn
hmSigConManualActivate = _HmSigConManualActivate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 6),
    _HmSigConManualActivate_Type()
)
hmSigConManualActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConManualActivate.setStatus("current")


class _HmSigConOperState_Type(Integer32):
    """Custom type hmSigConOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_HmSigConOperState_Type.__name__ = "Integer32"
_HmSigConOperState_Object = MibTableColumn
hmSigConOperState = _HmSigConOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 7),
    _HmSigConOperState_Type()
)
hmSigConOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigConOperState.setStatus("current")


class _HmSigConSenseLinkFailure_Type(Integer32):
    """Custom type hmSigConSenseLinkFailure based on Integer32"""
    defaultValue = 2

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


_HmSigConSenseLinkFailure_Type.__name__ = "Integer32"
_HmSigConSenseLinkFailure_Object = MibTableColumn
hmSigConSenseLinkFailure = _HmSigConSenseLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 8),
    _HmSigConSenseLinkFailure_Type()
)
hmSigConSenseLinkFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseLinkFailure.setStatus("current")


class _HmSigConSenseControlLine_Type(Integer32):
    """Custom type hmSigConSenseControlLine based on Integer32"""
    defaultValue = 2

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


_HmSigConSenseControlLine_Type.__name__ = "Integer32"
_HmSigConSenseControlLine_Object = MibTableColumn
hmSigConSenseControlLine = _HmSigConSenseControlLine_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 9),
    _HmSigConSenseControlLine_Type()
)
hmSigConSenseControlLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseControlLine.setStatus("current")


class _HmSigConSenseRedNotGuaranteed_Type(Integer32):
    """Custom type hmSigConSenseRedNotGuaranteed based on Integer32"""
    defaultValue = 2

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


_HmSigConSenseRedNotGuaranteed_Type.__name__ = "Integer32"
_HmSigConSenseRedNotGuaranteed_Object = MibTableColumn
hmSigConSenseRedNotGuaranteed = _HmSigConSenseRedNotGuaranteed_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 10),
    _HmSigConSenseRedNotGuaranteed_Type()
)
hmSigConSenseRedNotGuaranteed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseRedNotGuaranteed.setStatus("current")


class _HmSigConSensePS1State_Type(Integer32):
    """Custom type hmSigConSensePS1State based on Integer32"""
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


_HmSigConSensePS1State_Type.__name__ = "Integer32"
_HmSigConSensePS1State_Object = MibTableColumn
hmSigConSensePS1State = _HmSigConSensePS1State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 11),
    _HmSigConSensePS1State_Type()
)
hmSigConSensePS1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS1State.setStatus("current")


class _HmSigConSensePS2State_Type(Integer32):
    """Custom type hmSigConSensePS2State based on Integer32"""
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


_HmSigConSensePS2State_Type.__name__ = "Integer32"
_HmSigConSensePS2State_Object = MibTableColumn
hmSigConSensePS2State = _HmSigConSensePS2State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 12),
    _HmSigConSensePS2State_Type()
)
hmSigConSensePS2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS2State.setStatus("current")


class _HmSigConSenseTemperature_Type(Integer32):
    """Custom type hmSigConSenseTemperature based on Integer32"""
    defaultValue = 2

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


_HmSigConSenseTemperature_Type.__name__ = "Integer32"
_HmSigConSenseTemperature_Object = MibTableColumn
hmSigConSenseTemperature = _HmSigConSenseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 13),
    _HmSigConSenseTemperature_Type()
)
hmSigConSenseTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseTemperature.setStatus("current")


class _HmSigConSenseModuleRemoval_Type(Integer32):
    """Custom type hmSigConSenseModuleRemoval based on Integer32"""
    defaultValue = 2

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


_HmSigConSenseModuleRemoval_Type.__name__ = "Integer32"
_HmSigConSenseModuleRemoval_Object = MibTableColumn
hmSigConSenseModuleRemoval = _HmSigConSenseModuleRemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 14),
    _HmSigConSenseModuleRemoval_Type()
)
hmSigConSenseModuleRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseModuleRemoval.setStatus("current")


class _HmSigConSenseACARemoval_Type(Integer32):
    """Custom type hmSigConSenseACARemoval based on Integer32"""
    defaultValue = 2

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


_HmSigConSenseACARemoval_Type.__name__ = "Integer32"
_HmSigConSenseACARemoval_Object = MibTableColumn
hmSigConSenseACARemoval = _HmSigConSenseACARemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 15),
    _HmSigConSenseACARemoval_Type()
)
hmSigConSenseACARemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseACARemoval.setStatus("current")


class _HmSigConSensePS3State_Type(Integer32):
    """Custom type hmSigConSensePS3State based on Integer32"""
    defaultValue = 2

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


_HmSigConSensePS3State_Type.__name__ = "Integer32"
_HmSigConSensePS3State_Object = MibTableColumn
hmSigConSensePS3State = _HmSigConSensePS3State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 16),
    _HmSigConSensePS3State_Type()
)
hmSigConSensePS3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS3State.setStatus("current")


class _HmSigConSensePS4State_Type(Integer32):
    """Custom type hmSigConSensePS4State based on Integer32"""
    defaultValue = 2

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


_HmSigConSensePS4State_Type.__name__ = "Integer32"
_HmSigConSensePS4State_Object = MibTableColumn
hmSigConSensePS4State = _HmSigConSensePS4State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 17),
    _HmSigConSensePS4State_Type()
)
hmSigConSensePS4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS4State.setStatus("current")


class _HmSigConSenseFan1State_Type(Integer32):
    """Custom type hmSigConSenseFan1State based on Integer32"""
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


_HmSigConSenseFan1State_Type.__name__ = "Integer32"
_HmSigConSenseFan1State_Object = MibTableColumn
hmSigConSenseFan1State = _HmSigConSenseFan1State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 18),
    _HmSigConSenseFan1State_Type()
)
hmSigConSenseFan1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseFan1State.setStatus("current")


class _HmSigConSensePS5State_Type(Integer32):
    """Custom type hmSigConSensePS5State based on Integer32"""
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


_HmSigConSensePS5State_Type.__name__ = "Integer32"
_HmSigConSensePS5State_Object = MibTableColumn
hmSigConSensePS5State = _HmSigConSensePS5State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 19),
    _HmSigConSensePS5State_Type()
)
hmSigConSensePS5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS5State.setStatus("current")


class _HmSigConSensePS6State_Type(Integer32):
    """Custom type hmSigConSensePS6State based on Integer32"""
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


_HmSigConSensePS6State_Type.__name__ = "Integer32"
_HmSigConSensePS6State_Object = MibTableColumn
hmSigConSensePS6State = _HmSigConSensePS6State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 20),
    _HmSigConSensePS6State_Type()
)
hmSigConSensePS6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS6State.setStatus("current")


class _HmSigConSensePS7State_Type(Integer32):
    """Custom type hmSigConSensePS7State based on Integer32"""
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


_HmSigConSensePS7State_Type.__name__ = "Integer32"
_HmSigConSensePS7State_Object = MibTableColumn
hmSigConSensePS7State = _HmSigConSensePS7State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 21),
    _HmSigConSensePS7State_Type()
)
hmSigConSensePS7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS7State.setStatus("current")


class _HmSigConSensePS8State_Type(Integer32):
    """Custom type hmSigConSensePS8State based on Integer32"""
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


_HmSigConSensePS8State_Type.__name__ = "Integer32"
_HmSigConSensePS8State_Object = MibTableColumn
hmSigConSensePS8State = _HmSigConSensePS8State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 22),
    _HmSigConSensePS8State_Type()
)
hmSigConSensePS8State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSensePS8State.setStatus("current")


class _HmSigConSenseACANotInSync_Type(Integer32):
    """Custom type hmSigConSenseACANotInSync based on Integer32"""
    defaultValue = 2

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


_HmSigConSenseACANotInSync_Type.__name__ = "Integer32"
_HmSigConSenseACANotInSync_Object = MibTableColumn
hmSigConSenseACANotInSync = _HmSigConSenseACANotInSync_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 1, 1, 23),
    _HmSigConSenseACANotInSync_Type()
)
hmSigConSenseACANotInSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConSenseACANotInSync.setStatus("current")
_HmSigConLinkTable_Object = MibTable
hmSigConLinkTable = _HmSigConLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 2)
)
if mibBuilder.loadTexts:
    hmSigConLinkTable.setStatus("current")
_HmSigConLinkEntry_Object = MibTableRow
hmSigConLinkEntry = _HmSigConLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 2, 1)
)
hmSigConLinkEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmSigConLinkID"),
)
if mibBuilder.loadTexts:
    hmSigConLinkEntry.setStatus("current")


class _HmSigConLinkID_Type(Integer32):
    """Custom type hmSigConLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmSigConLinkID_Type.__name__ = "Integer32"
_HmSigConLinkID_Object = MibTableColumn
hmSigConLinkID = _HmSigConLinkID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 2, 1, 1),
    _HmSigConLinkID_Type()
)
hmSigConLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSigConLinkID.setStatus("current")


class _HmSigConLinkAlarm_Type(Integer32):
    """Custom type hmSigConLinkAlarm based on Integer32"""
    defaultValue = 2

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


_HmSigConLinkAlarm_Type.__name__ = "Integer32"
_HmSigConLinkAlarm_Object = MibTableColumn
hmSigConLinkAlarm = _HmSigConLinkAlarm_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 2, 1, 2),
    _HmSigConLinkAlarm_Type()
)
hmSigConLinkAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSigConLinkAlarm.setStatus("current")
_HmDevMonConfigTable_Object = MibTable
hmDevMonConfigTable = _HmDevMonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3)
)
if mibBuilder.loadTexts:
    hmDevMonConfigTable.setStatus("current")
_HmDevMonConfigEntry_Object = MibTableRow
hmDevMonConfigEntry = _HmDevMonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1)
)
hmDevMonConfigEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmDevMonID"),
)
if mibBuilder.loadTexts:
    hmDevMonConfigEntry.setStatus("current")


class _HmDevMonID_Type(Integer32):
    """Custom type hmDevMonID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HmDevMonID_Type.__name__ = "Integer32"
_HmDevMonID_Object = MibTableColumn
hmDevMonID = _HmDevMonID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 1),
    _HmDevMonID_Type()
)
hmDevMonID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDevMonID.setStatus("current")


class _HmDevMonTrapEnable_Type(Integer32):
    """Custom type hmDevMonTrapEnable based on Integer32"""
    defaultValue = 2

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


_HmDevMonTrapEnable_Type.__name__ = "Integer32"
_HmDevMonTrapEnable_Object = MibTableColumn
hmDevMonTrapEnable = _HmDevMonTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 2),
    _HmDevMonTrapEnable_Type()
)
hmDevMonTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonTrapEnable.setStatus("current")


class _HmDevMonTrapCause_Type(Integer32):
    """Custom type hmDevMonTrapCause based on Integer32"""
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
        *(("acaNotInSync", 10),
          ("acaRemoval", 8),
          ("controlLine", 3),
          ("fanFailure", 9),
          ("linkFailure", 2),
          ("moduleRemoval", 7),
          ("other", 1),
          ("psState", 5),
          ("redNotGuaranteed", 4),
          ("temperature", 6))
    )


_HmDevMonTrapCause_Type.__name__ = "Integer32"
_HmDevMonTrapCause_Object = MibTableColumn
hmDevMonTrapCause = _HmDevMonTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 3),
    _HmDevMonTrapCause_Type()
)
hmDevMonTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDevMonTrapCause.setStatus("current")
_HmDevMonTrapCauseIndex_Type = Integer32
_HmDevMonTrapCauseIndex_Object = MibTableColumn
hmDevMonTrapCauseIndex = _HmDevMonTrapCauseIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 4),
    _HmDevMonTrapCauseIndex_Type()
)
hmDevMonTrapCauseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDevMonTrapCauseIndex.setStatus("current")


class _HmDevMonSwitchState_Type(Integer32):
    """Custom type hmDevMonSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noerror", 2))
    )


_HmDevMonSwitchState_Type.__name__ = "Integer32"
_HmDevMonSwitchState_Object = MibTableColumn
hmDevMonSwitchState = _HmDevMonSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 5),
    _HmDevMonSwitchState_Type()
)
hmDevMonSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDevMonSwitchState.setStatus("current")


class _HmDevMonSenseLinkFailure_Type(Integer32):
    """Custom type hmDevMonSenseLinkFailure based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseLinkFailure_Type.__name__ = "Integer32"
_HmDevMonSenseLinkFailure_Object = MibTableColumn
hmDevMonSenseLinkFailure = _HmDevMonSenseLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 6),
    _HmDevMonSenseLinkFailure_Type()
)
hmDevMonSenseLinkFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseLinkFailure.setStatus("current")


class _HmDevMonSenseControlLine_Type(Integer32):
    """Custom type hmDevMonSenseControlLine based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseControlLine_Type.__name__ = "Integer32"
_HmDevMonSenseControlLine_Object = MibTableColumn
hmDevMonSenseControlLine = _HmDevMonSenseControlLine_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 7),
    _HmDevMonSenseControlLine_Type()
)
hmDevMonSenseControlLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseControlLine.setStatus("current")


class _HmDevMonSenseRedNotGuaranteed_Type(Integer32):
    """Custom type hmDevMonSenseRedNotGuaranteed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseRedNotGuaranteed_Type.__name__ = "Integer32"
_HmDevMonSenseRedNotGuaranteed_Object = MibTableColumn
hmDevMonSenseRedNotGuaranteed = _HmDevMonSenseRedNotGuaranteed_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 8),
    _HmDevMonSenseRedNotGuaranteed_Type()
)
hmDevMonSenseRedNotGuaranteed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseRedNotGuaranteed.setStatus("current")


class _HmDevMonSensePS1State_Type(Integer32):
    """Custom type hmDevMonSensePS1State based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS1State_Type.__name__ = "Integer32"
_HmDevMonSensePS1State_Object = MibTableColumn
hmDevMonSensePS1State = _HmDevMonSensePS1State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 9),
    _HmDevMonSensePS1State_Type()
)
hmDevMonSensePS1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS1State.setStatus("current")


class _HmDevMonSensePS2State_Type(Integer32):
    """Custom type hmDevMonSensePS2State based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS2State_Type.__name__ = "Integer32"
_HmDevMonSensePS2State_Object = MibTableColumn
hmDevMonSensePS2State = _HmDevMonSensePS2State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 10),
    _HmDevMonSensePS2State_Type()
)
hmDevMonSensePS2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS2State.setStatus("current")


class _HmDevMonSenseTemperature_Type(Integer32):
    """Custom type hmDevMonSenseTemperature based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseTemperature_Type.__name__ = "Integer32"
_HmDevMonSenseTemperature_Object = MibTableColumn
hmDevMonSenseTemperature = _HmDevMonSenseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 11),
    _HmDevMonSenseTemperature_Type()
)
hmDevMonSenseTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseTemperature.setStatus("current")


class _HmDevMonSenseModuleRemoval_Type(Integer32):
    """Custom type hmDevMonSenseModuleRemoval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseModuleRemoval_Type.__name__ = "Integer32"
_HmDevMonSenseModuleRemoval_Object = MibTableColumn
hmDevMonSenseModuleRemoval = _HmDevMonSenseModuleRemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 12),
    _HmDevMonSenseModuleRemoval_Type()
)
hmDevMonSenseModuleRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseModuleRemoval.setStatus("current")


class _HmDevMonSenseACARemoval_Type(Integer32):
    """Custom type hmDevMonSenseACARemoval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseACARemoval_Type.__name__ = "Integer32"
_HmDevMonSenseACARemoval_Object = MibTableColumn
hmDevMonSenseACARemoval = _HmDevMonSenseACARemoval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 13),
    _HmDevMonSenseACARemoval_Type()
)
hmDevMonSenseACARemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseACARemoval.setStatus("current")


class _HmDevMonSensePS3State_Type(Integer32):
    """Custom type hmDevMonSensePS3State based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS3State_Type.__name__ = "Integer32"
_HmDevMonSensePS3State_Object = MibTableColumn
hmDevMonSensePS3State = _HmDevMonSensePS3State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 14),
    _HmDevMonSensePS3State_Type()
)
hmDevMonSensePS3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS3State.setStatus("current")


class _HmDevMonSensePS4State_Type(Integer32):
    """Custom type hmDevMonSensePS4State based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS4State_Type.__name__ = "Integer32"
_HmDevMonSensePS4State_Object = MibTableColumn
hmDevMonSensePS4State = _HmDevMonSensePS4State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 15),
    _HmDevMonSensePS4State_Type()
)
hmDevMonSensePS4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS4State.setStatus("current")


class _HmDevMonSenseFan1State_Type(Integer32):
    """Custom type hmDevMonSenseFan1State based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseFan1State_Type.__name__ = "Integer32"
_HmDevMonSenseFan1State_Object = MibTableColumn
hmDevMonSenseFan1State = _HmDevMonSenseFan1State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 16),
    _HmDevMonSenseFan1State_Type()
)
hmDevMonSenseFan1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseFan1State.setStatus("current")


class _HmDevMonSensePS5State_Type(Integer32):
    """Custom type hmDevMonSensePS5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS5State_Type.__name__ = "Integer32"
_HmDevMonSensePS5State_Object = MibTableColumn
hmDevMonSensePS5State = _HmDevMonSensePS5State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 17),
    _HmDevMonSensePS5State_Type()
)
hmDevMonSensePS5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS5State.setStatus("current")


class _HmDevMonSensePS6State_Type(Integer32):
    """Custom type hmDevMonSensePS6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS6State_Type.__name__ = "Integer32"
_HmDevMonSensePS6State_Object = MibTableColumn
hmDevMonSensePS6State = _HmDevMonSensePS6State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 18),
    _HmDevMonSensePS6State_Type()
)
hmDevMonSensePS6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS6State.setStatus("current")


class _HmDevMonSensePS7State_Type(Integer32):
    """Custom type hmDevMonSensePS7State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS7State_Type.__name__ = "Integer32"
_HmDevMonSensePS7State_Object = MibTableColumn
hmDevMonSensePS7State = _HmDevMonSensePS7State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 19),
    _HmDevMonSensePS7State_Type()
)
hmDevMonSensePS7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS7State.setStatus("current")


class _HmDevMonSensePS8State_Type(Integer32):
    """Custom type hmDevMonSensePS8State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSensePS8State_Type.__name__ = "Integer32"
_HmDevMonSensePS8State_Object = MibTableColumn
hmDevMonSensePS8State = _HmDevMonSensePS8State_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 20),
    _HmDevMonSensePS8State_Type()
)
hmDevMonSensePS8State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSensePS8State.setStatus("current")


class _HmDevMonSenseACANotInSync_Type(Integer32):
    """Custom type hmDevMonSenseACANotInSync based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("ignore", 2))
    )


_HmDevMonSenseACANotInSync_Type.__name__ = "Integer32"
_HmDevMonSenseACANotInSync_Object = MibTableColumn
hmDevMonSenseACANotInSync = _HmDevMonSenseACANotInSync_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 12, 3, 1, 21),
    _HmDevMonSenseACANotInSync_Type()
)
hmDevMonSenseACANotInSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDevMonSenseACANotInSync.setStatus("current")
_HmAgentSnmpConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentSnmpConfigGroup = _HmAgentSnmpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13)
)


class _HmAgentSnmpCommunityCreate_Type(DisplayString):
    """Custom type hmAgentSnmpCommunityCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HmAgentSnmpCommunityCreate_Type.__name__ = "DisplayString"
_HmAgentSnmpCommunityCreate_Object = MibScalar
hmAgentSnmpCommunityCreate = _HmAgentSnmpCommunityCreate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 1),
    _HmAgentSnmpCommunityCreate_Type()
)
hmAgentSnmpCommunityCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityCreate.setStatus("current")
_HmAgentSnmpCommunityConfigTable_Object = MibTable
hmAgentSnmpCommunityConfigTable = _HmAgentSnmpCommunityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2)
)
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityConfigTable.setStatus("current")
_HmAgentSnmpCommunityConfigEntry_Object = MibTableRow
hmAgentSnmpCommunityConfigEntry = _HmAgentSnmpCommunityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2, 1)
)
hmAgentSnmpCommunityConfigEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmAgentSnmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityConfigEntry.setStatus("current")


class _HmAgentSnmpCommunityIndex_Type(Integer32):
    """Custom type hmAgentSnmpCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_HmAgentSnmpCommunityIndex_Type.__name__ = "Integer32"
_HmAgentSnmpCommunityIndex_Object = MibTableColumn
hmAgentSnmpCommunityIndex = _HmAgentSnmpCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2, 1, 1),
    _HmAgentSnmpCommunityIndex_Type()
)
hmAgentSnmpCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityIndex.setStatus("current")


class _HmAgentSnmpCommunityName_Type(DisplayString):
    """Custom type hmAgentSnmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HmAgentSnmpCommunityName_Type.__name__ = "DisplayString"
_HmAgentSnmpCommunityName_Object = MibTableColumn
hmAgentSnmpCommunityName = _HmAgentSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2, 1, 2),
    _HmAgentSnmpCommunityName_Type()
)
hmAgentSnmpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityName.setStatus("current")
_HmAgentSnmpCommunityIPAddress_Type = IpAddress
_HmAgentSnmpCommunityIPAddress_Object = MibTableColumn
hmAgentSnmpCommunityIPAddress = _HmAgentSnmpCommunityIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2, 1, 3),
    _HmAgentSnmpCommunityIPAddress_Type()
)
hmAgentSnmpCommunityIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityIPAddress.setStatus("current")
_HmAgentSnmpCommunityIPMask_Type = IpAddress
_HmAgentSnmpCommunityIPMask_Object = MibTableColumn
hmAgentSnmpCommunityIPMask = _HmAgentSnmpCommunityIPMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2, 1, 4),
    _HmAgentSnmpCommunityIPMask_Type()
)
hmAgentSnmpCommunityIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityIPMask.setStatus("current")


class _HmAgentSnmpCommunityAccessMode_Type(Integer32):
    """Custom type hmAgentSnmpCommunityAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_HmAgentSnmpCommunityAccessMode_Type.__name__ = "Integer32"
_HmAgentSnmpCommunityAccessMode_Object = MibTableColumn
hmAgentSnmpCommunityAccessMode = _HmAgentSnmpCommunityAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2, 1, 5),
    _HmAgentSnmpCommunityAccessMode_Type()
)
hmAgentSnmpCommunityAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityAccessMode.setStatus("current")


class _HmAgentSnmpCommunityStatus_Type(Integer32):
    """Custom type hmAgentSnmpCommunityStatus based on Integer32"""
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
        *(("active", 1),
          ("config", 3),
          ("destroy", 4),
          ("notInService", 2))
    )


_HmAgentSnmpCommunityStatus_Type.__name__ = "Integer32"
_HmAgentSnmpCommunityStatus_Object = MibTableColumn
hmAgentSnmpCommunityStatus = _HmAgentSnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 2, 1, 6),
    _HmAgentSnmpCommunityStatus_Type()
)
hmAgentSnmpCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityStatus.setStatus("current")


class _HmAgentSnmpTrapReceiverCreate_Type(DisplayString):
    """Custom type hmAgentSnmpTrapReceiverCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HmAgentSnmpTrapReceiverCreate_Type.__name__ = "DisplayString"
_HmAgentSnmpTrapReceiverCreate_Object = MibScalar
hmAgentSnmpTrapReceiverCreate = _HmAgentSnmpTrapReceiverCreate_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 3),
    _HmAgentSnmpTrapReceiverCreate_Type()
)
hmAgentSnmpTrapReceiverCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverCreate.setStatus("current")
_HmAgentSnmpTrapReceiverConfigTable_Object = MibTable
hmAgentSnmpTrapReceiverConfigTable = _HmAgentSnmpTrapReceiverConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 4)
)
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverConfigTable.setStatus("current")
_HmAgentSnmpTrapReceiverConfigEntry_Object = MibTableRow
hmAgentSnmpTrapReceiverConfigEntry = _HmAgentSnmpTrapReceiverConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 4, 1)
)
hmAgentSnmpTrapReceiverConfigEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmAgentSnmpTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverConfigEntry.setStatus("current")


class _HmAgentSnmpTrapReceiverIndex_Type(Integer32):
    """Custom type hmAgentSnmpTrapReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_HmAgentSnmpTrapReceiverIndex_Type.__name__ = "Integer32"
_HmAgentSnmpTrapReceiverIndex_Object = MibTableColumn
hmAgentSnmpTrapReceiverIndex = _HmAgentSnmpTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 4, 1, 1),
    _HmAgentSnmpTrapReceiverIndex_Type()
)
hmAgentSnmpTrapReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverIndex.setStatus("current")


class _HmAgentSnmpTrapReceiverCommunityName_Type(DisplayString):
    """Custom type hmAgentSnmpTrapReceiverCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HmAgentSnmpTrapReceiverCommunityName_Type.__name__ = "DisplayString"
_HmAgentSnmpTrapReceiverCommunityName_Object = MibTableColumn
hmAgentSnmpTrapReceiverCommunityName = _HmAgentSnmpTrapReceiverCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 4, 1, 2),
    _HmAgentSnmpTrapReceiverCommunityName_Type()
)
hmAgentSnmpTrapReceiverCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverCommunityName.setStatus("current")
_HmAgentSnmpTrapReceiverIPAddress_Type = IpAddress
_HmAgentSnmpTrapReceiverIPAddress_Object = MibTableColumn
hmAgentSnmpTrapReceiverIPAddress = _HmAgentSnmpTrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 4, 1, 3),
    _HmAgentSnmpTrapReceiverIPAddress_Type()
)
hmAgentSnmpTrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverIPAddress.setStatus("current")


class _HmAgentSnmpTrapReceiverStatus_Type(Integer32):
    """Custom type hmAgentSnmpTrapReceiverStatus based on Integer32"""
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
        *(("active", 1),
          ("config", 3),
          ("destroy", 4),
          ("notInService", 2))
    )


_HmAgentSnmpTrapReceiverStatus_Type.__name__ = "Integer32"
_HmAgentSnmpTrapReceiverStatus_Object = MibTableColumn
hmAgentSnmpTrapReceiverStatus = _HmAgentSnmpTrapReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 4, 1, 4),
    _HmAgentSnmpTrapReceiverStatus_Type()
)
hmAgentSnmpTrapReceiverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverStatus.setStatus("current")
_HmAgentSnmpTrapFlagsConfigGroup_ObjectIdentity = ObjectIdentity
hmAgentSnmpTrapFlagsConfigGroup = _HmAgentSnmpTrapFlagsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5)
)


class _HmAgentSnmpAuthenticationTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpAuthenticationTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpAuthenticationTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpAuthenticationTrapFlag_Object = MibScalar
hmAgentSnmpAuthenticationTrapFlag = _HmAgentSnmpAuthenticationTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 1),
    _HmAgentSnmpAuthenticationTrapFlag_Type()
)
hmAgentSnmpAuthenticationTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpAuthenticationTrapFlag.setStatus("current")


class _HmAgentSnmpLinkUpDownTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpLinkUpDownTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpLinkUpDownTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpLinkUpDownTrapFlag_Object = MibScalar
hmAgentSnmpLinkUpDownTrapFlag = _HmAgentSnmpLinkUpDownTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 2),
    _HmAgentSnmpLinkUpDownTrapFlag_Type()
)
hmAgentSnmpLinkUpDownTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpLinkUpDownTrapFlag.setStatus("current")


class _HmAgentSnmpMultipleUsersTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpMultipleUsersTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpMultipleUsersTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpMultipleUsersTrapFlag_Object = MibScalar
hmAgentSnmpMultipleUsersTrapFlag = _HmAgentSnmpMultipleUsersTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 3),
    _HmAgentSnmpMultipleUsersTrapFlag_Type()
)
hmAgentSnmpMultipleUsersTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpMultipleUsersTrapFlag.setStatus("current")


class _HmAgentSnmpSpanningTreeTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpSpanningTreeTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpSpanningTreeTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpSpanningTreeTrapFlag_Object = MibScalar
hmAgentSnmpSpanningTreeTrapFlag = _HmAgentSnmpSpanningTreeTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 4),
    _HmAgentSnmpSpanningTreeTrapFlag_Type()
)
hmAgentSnmpSpanningTreeTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpSpanningTreeTrapFlag.setStatus("current")


class _HmAgentSnmpBroadcastStormTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpBroadcastStormTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpBroadcastStormTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpBroadcastStormTrapFlag_Object = MibScalar
hmAgentSnmpBroadcastStormTrapFlag = _HmAgentSnmpBroadcastStormTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 5),
    _HmAgentSnmpBroadcastStormTrapFlag_Type()
)
hmAgentSnmpBroadcastStormTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpBroadcastStormTrapFlag.setStatus("current")


class _HmAgentSnmpChassisTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpChassisTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpChassisTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpChassisTrapFlag_Object = MibScalar
hmAgentSnmpChassisTrapFlag = _HmAgentSnmpChassisTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 6),
    _HmAgentSnmpChassisTrapFlag_Type()
)
hmAgentSnmpChassisTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpChassisTrapFlag.setStatus("current")


class _HmAgentSnmpL2RedundancyTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpL2RedundancyTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpL2RedundancyTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpL2RedundancyTrapFlag_Object = MibScalar
hmAgentSnmpL2RedundancyTrapFlag = _HmAgentSnmpL2RedundancyTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 7),
    _HmAgentSnmpL2RedundancyTrapFlag_Type()
)
hmAgentSnmpL2RedundancyTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpL2RedundancyTrapFlag.setStatus("current")


class _HmAgentSnmpPortSecurityTrapFlag_Type(Integer32):
    """Custom type hmAgentSnmpPortSecurityTrapFlag based on Integer32"""
    defaultValue = 1

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


_HmAgentSnmpPortSecurityTrapFlag_Type.__name__ = "Integer32"
_HmAgentSnmpPortSecurityTrapFlag_Object = MibScalar
hmAgentSnmpPortSecurityTrapFlag = _HmAgentSnmpPortSecurityTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 5, 8),
    _HmAgentSnmpPortSecurityTrapFlag_Type()
)
hmAgentSnmpPortSecurityTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpPortSecurityTrapFlag.setStatus("current")
_HmAgentSnmpCommunityMaxEntries_Type = Integer32
_HmAgentSnmpCommunityMaxEntries_Object = MibScalar
hmAgentSnmpCommunityMaxEntries = _HmAgentSnmpCommunityMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 6),
    _HmAgentSnmpCommunityMaxEntries_Type()
)
hmAgentSnmpCommunityMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSnmpCommunityMaxEntries.setStatus("current")
_HmAgentSnmpTrapReceiverMaxEntries_Type = Integer32
_HmAgentSnmpTrapReceiverMaxEntries_Object = MibScalar
hmAgentSnmpTrapReceiverMaxEntries = _HmAgentSnmpTrapReceiverMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 7),
    _HmAgentSnmpTrapReceiverMaxEntries_Type()
)
hmAgentSnmpTrapReceiverMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmAgentSnmpTrapReceiverMaxEntries.setStatus("current")
_HmAgentSnmpLoggingGroup_ObjectIdentity = ObjectIdentity
hmAgentSnmpLoggingGroup = _HmAgentSnmpLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 8)
)


class _HmAgentSnmpLogGetRequest_Type(Integer32):
    """Custom type hmAgentSnmpLogGetRequest based on Integer32"""
    defaultValue = 2

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


_HmAgentSnmpLogGetRequest_Type.__name__ = "Integer32"
_HmAgentSnmpLogGetRequest_Object = MibScalar
hmAgentSnmpLogGetRequest = _HmAgentSnmpLogGetRequest_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 8, 1),
    _HmAgentSnmpLogGetRequest_Type()
)
hmAgentSnmpLogGetRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpLogGetRequest.setStatus("current")


class _HmAgentSnmpLogSetRequest_Type(Integer32):
    """Custom type hmAgentSnmpLogSetRequest based on Integer32"""
    defaultValue = 2

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


_HmAgentSnmpLogSetRequest_Type.__name__ = "Integer32"
_HmAgentSnmpLogSetRequest_Object = MibScalar
hmAgentSnmpLogSetRequest = _HmAgentSnmpLogSetRequest_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 8, 2),
    _HmAgentSnmpLogSetRequest_Type()
)
hmAgentSnmpLogSetRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpLogSetRequest.setStatus("current")


class _HmAgentSnmpLogGetSeverity_Type(HmAgentLogSeverity):
    """Custom type hmAgentSnmpLogGetSeverity based on HmAgentLogSeverity"""


_HmAgentSnmpLogGetSeverity_Object = MibScalar
hmAgentSnmpLogGetSeverity = _HmAgentSnmpLogGetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 8, 3),
    _HmAgentSnmpLogGetSeverity_Type()
)
hmAgentSnmpLogGetSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpLogGetSeverity.setStatus("current")


class _HmAgentSnmpLogSetSeverity_Type(HmAgentLogSeverity):
    """Custom type hmAgentSnmpLogSetSeverity based on HmAgentLogSeverity"""


_HmAgentSnmpLogSetSeverity_Object = MibScalar
hmAgentSnmpLogSetSeverity = _HmAgentSnmpLogSetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 13, 8, 4),
    _HmAgentSnmpLogSetSeverity_Type()
)
hmAgentSnmpLogSetSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentSnmpLogSetSeverity.setStatus("current")
_HmPOEGroup_ObjectIdentity = ObjectIdentity
hmPOEGroup = _HmPOEGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14)
)
_HmPOEGlobalGroup_ObjectIdentity = ObjectIdentity
hmPOEGlobalGroup = _HmPOEGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 1)
)


class _HmPOEStatus_Type(Integer32):
    """Custom type hmPOEStatus based on Integer32"""
    defaultValue = 1

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


_HmPOEStatus_Type.__name__ = "Integer32"
_HmPOEStatus_Object = MibScalar
hmPOEStatus = _HmPOEStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 1, 1),
    _HmPOEStatus_Type()
)
hmPOEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPOEStatus.setStatus("current")


class _HmPOEScanning_Type(Integer32):
    """Custom type hmPOEScanning based on Integer32"""
    defaultValue = 1

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


_HmPOEScanning_Type.__name__ = "Integer32"
_HmPOEScanning_Object = MibScalar
hmPOEScanning = _HmPOEScanning_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 1, 2),
    _HmPOEScanning_Type()
)
hmPOEScanning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPOEScanning.setStatus("current")
_HmPOEReservedPower_Type = Integer32
_HmPOEReservedPower_Object = MibScalar
hmPOEReservedPower = _HmPOEReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 1, 3),
    _HmPOEReservedPower_Type()
)
hmPOEReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPOEReservedPower.setStatus("current")


class _HmPOEFastStartup_Type(Integer32):
    """Custom type hmPOEFastStartup based on Integer32"""
    defaultValue = 2

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


_HmPOEFastStartup_Type.__name__ = "Integer32"
_HmPOEFastStartup_Object = MibScalar
hmPOEFastStartup = _HmPOEFastStartup_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 1, 4),
    _HmPOEFastStartup_Type()
)
hmPOEFastStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPOEFastStartup.setStatus("current")
_HmPOEPortTable_Object = MibTable
hmPOEPortTable = _HmPOEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 2)
)
if mibBuilder.loadTexts:
    hmPOEPortTable.setStatus("current")
_HmPOEPortEntry_Object = MibTableRow
hmPOEPortEntry = _HmPOEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 2, 1)
)
hmPOEPortEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPOEPortIndex"),
)
if mibBuilder.loadTexts:
    hmPOEPortEntry.setStatus("current")


class _HmPOEPortIndex_Type(Integer32):
    """Custom type hmPOEPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmPOEPortIndex_Type.__name__ = "Integer32"
_HmPOEPortIndex_Object = MibTableColumn
hmPOEPortIndex = _HmPOEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 2, 1, 1),
    _HmPOEPortIndex_Type()
)
hmPOEPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPOEPortIndex.setStatus("current")
_HmPOEPortConsumptionPower_Type = Integer32
_HmPOEPortConsumptionPower_Object = MibTableColumn
hmPOEPortConsumptionPower = _HmPOEPortConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 2, 1, 2),
    _HmPOEPortConsumptionPower_Type()
)
hmPOEPortConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPOEPortConsumptionPower.setStatus("current")
_HmPOEModuleTable_Object = MibTable
hmPOEModuleTable = _HmPOEModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3)
)
if mibBuilder.loadTexts:
    hmPOEModuleTable.setStatus("current")
_HmPOEModuleEntry_Object = MibTableRow
hmPOEModuleEntry = _HmPOEModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1)
)
hmPOEModuleEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPOEModuleIndex"),
)
if mibBuilder.loadTexts:
    hmPOEModuleEntry.setStatus("current")


class _HmPOEModuleIndex_Type(Integer32):
    """Custom type hmPOEModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmPOEModuleIndex_Type.__name__ = "Integer32"
_HmPOEModuleIndex_Object = MibTableColumn
hmPOEModuleIndex = _HmPOEModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1, 1),
    _HmPOEModuleIndex_Type()
)
hmPOEModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPOEModuleIndex.setStatus("current")


class _HmPOEModulePower_Type(Integer32):
    """Custom type hmPOEModulePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HmPOEModulePower_Type.__name__ = "Integer32"
_HmPOEModulePower_Object = MibTableColumn
hmPOEModulePower = _HmPOEModulePower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1, 2),
    _HmPOEModulePower_Type()
)
hmPOEModulePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPOEModulePower.setStatus("current")


class _HmPOEModuleMaximumPower_Type(Integer32):
    """Custom type hmPOEModuleMaximumPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HmPOEModuleMaximumPower_Type.__name__ = "Integer32"
_HmPOEModuleMaximumPower_Object = MibTableColumn
hmPOEModuleMaximumPower = _HmPOEModuleMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1, 3),
    _HmPOEModuleMaximumPower_Type()
)
hmPOEModuleMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPOEModuleMaximumPower.setStatus("current")
_HmPOEModuleReservedPower_Type = Integer32
_HmPOEModuleReservedPower_Object = MibTableColumn
hmPOEModuleReservedPower = _HmPOEModuleReservedPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1, 4),
    _HmPOEModuleReservedPower_Type()
)
hmPOEModuleReservedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPOEModuleReservedPower.setStatus("current")
_HmPOEModuleDeliveredPower_Type = Integer32
_HmPOEModuleDeliveredPower_Object = MibTableColumn
hmPOEModuleDeliveredPower = _HmPOEModuleDeliveredPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1, 5),
    _HmPOEModuleDeliveredPower_Type()
)
hmPOEModuleDeliveredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPOEModuleDeliveredPower.setStatus("current")


class _HmPOEModuleUsageThreshold_Type(Integer32):
    """Custom type hmPOEModuleUsageThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_HmPOEModuleUsageThreshold_Type.__name__ = "Integer32"
_HmPOEModuleUsageThreshold_Object = MibTableColumn
hmPOEModuleUsageThreshold = _HmPOEModuleUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1, 6),
    _HmPOEModuleUsageThreshold_Type()
)
hmPOEModuleUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPOEModuleUsageThreshold.setStatus("current")


class _HmPOEModuleNotificationControlEnable_Type(TruthValue):
    """Custom type hmPOEModuleNotificationControlEnable based on TruthValue"""


_HmPOEModuleNotificationControlEnable_Object = MibTableColumn
hmPOEModuleNotificationControlEnable = _HmPOEModuleNotificationControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 14, 3, 1, 7),
    _HmPOEModuleNotificationControlEnable_Type()
)
hmPOEModuleNotificationControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPOEModuleNotificationControlEnable.setStatus("current")
_HmSwitchResources_ObjectIdentity = ObjectIdentity
hmSwitchResources = _HmSwitchResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15)
)


class _HmEnableMeasurement_Type(Integer32):
    """Custom type hmEnableMeasurement based on Integer32"""
    defaultValue = 1

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


_HmEnableMeasurement_Type.__name__ = "Integer32"
_HmEnableMeasurement_Object = MibScalar
hmEnableMeasurement = _HmEnableMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 1),
    _HmEnableMeasurement_Type()
)
hmEnableMeasurement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmEnableMeasurement.setStatus("current")
_HmCpuResources_ObjectIdentity = ObjectIdentity
hmCpuResources = _HmCpuResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 2)
)


class _HmCpuUtilization_Type(Integer32):
    """Custom type hmCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmCpuUtilization_Type.__name__ = "Integer32"
_HmCpuUtilization_Object = MibScalar
hmCpuUtilization = _HmCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 2, 1),
    _HmCpuUtilization_Type()
)
hmCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hmCpuUtilization.setUnits("percent")


class _HmCpuAverageUtilization_Type(Integer32):
    """Custom type hmCpuAverageUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmCpuAverageUtilization_Type.__name__ = "Integer32"
_HmCpuAverageUtilization_Object = MibScalar
hmCpuAverageUtilization = _HmCpuAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 2, 2),
    _HmCpuAverageUtilization_Type()
)
hmCpuAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCpuAverageUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hmCpuAverageUtilization.setUnits("percent")


class _HmCpuRunningProcesses_Type(Integer32):
    """Custom type hmCpuRunningProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_HmCpuRunningProcesses_Type.__name__ = "Integer32"
_HmCpuRunningProcesses_Object = MibScalar
hmCpuRunningProcesses = _HmCpuRunningProcesses_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 2, 3),
    _HmCpuRunningProcesses_Type()
)
hmCpuRunningProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCpuRunningProcesses.setStatus("current")


class _HmCpuMaxRunningProcesses_Type(Integer32):
    """Custom type hmCpuMaxRunningProcesses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_HmCpuMaxRunningProcesses_Type.__name__ = "Integer32"
_HmCpuMaxRunningProcesses_Object = MibScalar
hmCpuMaxRunningProcesses = _HmCpuMaxRunningProcesses_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 2, 4),
    _HmCpuMaxRunningProcesses_Type()
)
hmCpuMaxRunningProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmCpuMaxRunningProcesses.setStatus("current")
_HmMemoryResources_ObjectIdentity = ObjectIdentity
hmMemoryResources = _HmMemoryResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 3)
)


class _HmMemoryAllocated_Type(Integer32):
    """Custom type hmMemoryAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmMemoryAllocated_Type.__name__ = "Integer32"
_HmMemoryAllocated_Object = MibScalar
hmMemoryAllocated = _HmMemoryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 3, 1),
    _HmMemoryAllocated_Type()
)
hmMemoryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMemoryAllocated.setStatus("current")
if mibBuilder.loadTexts:
    hmMemoryAllocated.setUnits("kBytes")


class _HmMemoryFree_Type(Integer32):
    """Custom type hmMemoryFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmMemoryFree_Type.__name__ = "Integer32"
_HmMemoryFree_Object = MibScalar
hmMemoryFree = _HmMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 3, 2),
    _HmMemoryFree_Type()
)
hmMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMemoryFree.setStatus("current")
if mibBuilder.loadTexts:
    hmMemoryFree.setUnits("kBytes")


class _HmMemoryAllocatedAverage_Type(Integer32):
    """Custom type hmMemoryAllocatedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmMemoryAllocatedAverage_Type.__name__ = "Integer32"
_HmMemoryAllocatedAverage_Object = MibScalar
hmMemoryAllocatedAverage = _HmMemoryAllocatedAverage_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 3, 3),
    _HmMemoryAllocatedAverage_Type()
)
hmMemoryAllocatedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMemoryAllocatedAverage.setStatus("current")
if mibBuilder.loadTexts:
    hmMemoryAllocatedAverage.setUnits("kBytes")


class _HmMemoryFreeAverage_Type(Integer32):
    """Custom type hmMemoryFreeAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmMemoryFreeAverage_Type.__name__ = "Integer32"
_HmMemoryFreeAverage_Object = MibScalar
hmMemoryFreeAverage = _HmMemoryFreeAverage_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 3, 4),
    _HmMemoryFreeAverage_Type()
)
hmMemoryFreeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMemoryFreeAverage.setStatus("current")
if mibBuilder.loadTexts:
    hmMemoryFreeAverage.setUnits("kBytes")
_HmNetworkResources_ObjectIdentity = ObjectIdentity
hmNetworkResources = _HmNetworkResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 4)
)


class _HmNetworkCpuIfUtilization_Type(Integer32):
    """Custom type hmNetworkCpuIfUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmNetworkCpuIfUtilization_Type.__name__ = "Integer32"
_HmNetworkCpuIfUtilization_Object = MibScalar
hmNetworkCpuIfUtilization = _HmNetworkCpuIfUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 4, 1),
    _HmNetworkCpuIfUtilization_Type()
)
hmNetworkCpuIfUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetworkCpuIfUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hmNetworkCpuIfUtilization.setUnits("precent")


class _HmNetworkCpuIfAverageUtilization_Type(Integer32):
    """Custom type hmNetworkCpuIfAverageUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmNetworkCpuIfAverageUtilization_Type.__name__ = "Integer32"
_HmNetworkCpuIfAverageUtilization_Object = MibScalar
hmNetworkCpuIfAverageUtilization = _HmNetworkCpuIfAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 15, 4, 2),
    _HmNetworkCpuIfAverageUtilization_Type()
)
hmNetworkCpuIfAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetworkCpuIfAverageUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hmNetworkCpuIfAverageUtilization.setUnits("precent")
_HmIndustrialEthernetProtocols_ObjectIdentity = ObjectIdentity
hmIndustrialEthernetProtocols = _HmIndustrialEthernetProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16)
)
_HmProfinetIOConfigGroup_ObjectIdentity = ObjectIdentity
hmProfinetIOConfigGroup = _HmProfinetIOConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1)
)


class _HmPNIOAdminStatus_Type(Integer32):
    """Custom type hmPNIOAdminStatus based on Integer32"""
    defaultValue = 2

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


_HmPNIOAdminStatus_Type.__name__ = "Integer32"
_HmPNIOAdminStatus_Object = MibScalar
hmPNIOAdminStatus = _HmPNIOAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 1),
    _HmPNIOAdminStatus_Type()
)
hmPNIOAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPNIOAdminStatus.setStatus("current")


class _HmPNIODeviceID_Type(Integer32):
    """Custom type hmPNIODeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmPNIODeviceID_Type.__name__ = "Integer32"
_HmPNIODeviceID_Object = MibScalar
hmPNIODeviceID = _HmPNIODeviceID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 2),
    _HmPNIODeviceID_Type()
)
hmPNIODeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIODeviceID.setStatus("current")
_HmPNIOModuleIdentNumber_Type = Integer32
_HmPNIOModuleIdentNumber_Object = MibScalar
hmPNIOModuleIdentNumber = _HmPNIOModuleIdentNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 3),
    _HmPNIOModuleIdentNumber_Type()
)
hmPNIOModuleIdentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIOModuleIdentNumber.setStatus("current")


class _HmPNIOOrderID_Type(DisplayString):
    """Custom type hmPNIOOrderID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HmPNIOOrderID_Type.__name__ = "DisplayString"
_HmPNIOOrderID_Object = MibScalar
hmPNIOOrderID = _HmPNIOOrderID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 4),
    _HmPNIOOrderID_Type()
)
hmPNIOOrderID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIOOrderID.setStatus("current")
_HmPNIODeviceTypeDetails_Type = DisplayString
_HmPNIODeviceTypeDetails_Object = MibScalar
hmPNIODeviceTypeDetails = _HmPNIODeviceTypeDetails_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 5),
    _HmPNIODeviceTypeDetails_Type()
)
hmPNIODeviceTypeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIODeviceTypeDetails.setStatus("current")
_HmPNIOSoftwareRelease_Type = DisplayString
_HmPNIOSoftwareRelease_Object = MibScalar
hmPNIOSoftwareRelease = _HmPNIOSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 6),
    _HmPNIOSoftwareRelease_Type()
)
hmPNIOSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIOSoftwareRelease.setStatus("current")
_HmPNIOHardwareRelease_Type = Integer32
_HmPNIOHardwareRelease_Object = MibScalar
hmPNIOHardwareRelease = _HmPNIOHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 7),
    _HmPNIOHardwareRelease_Type()
)
hmPNIOHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIOHardwareRelease.setStatus("current")


class _HmPNIOOrderID9th_Type(DisplayString):
    """Custom type hmPNIOOrderID9th based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmPNIOOrderID9th_Type.__name__ = "DisplayString"
_HmPNIOOrderID9th_Object = MibScalar
hmPNIOOrderID9th = _HmPNIOOrderID9th_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 8),
    _HmPNIOOrderID9th_Type()
)
hmPNIOOrderID9th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIOOrderID9th.setStatus("current")
_HmPNIODcpModeTable_Object = MibTable
hmPNIODcpModeTable = _HmPNIODcpModeTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 10)
)
if mibBuilder.loadTexts:
    hmPNIODcpModeTable.setStatus("current")
_HmPNIODcpModeEntry_Object = MibTableRow
hmPNIODcpModeEntry = _HmPNIODcpModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 10, 1)
)
hmPNIODcpModeEntry.setIndexNames(
    (0, "HMPRIV-MGMT-SNMP-MIB", "hmPNIODcpModePortID"),
)
if mibBuilder.loadTexts:
    hmPNIODcpModeEntry.setStatus("current")


class _HmPNIODcpModePortID_Type(Integer32):
    """Custom type hmPNIODcpModePortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmPNIODcpModePortID_Type.__name__ = "Integer32"
_HmPNIODcpModePortID_Object = MibTableColumn
hmPNIODcpModePortID = _HmPNIODcpModePortID_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 10, 1, 1),
    _HmPNIODcpModePortID_Type()
)
hmPNIODcpModePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPNIODcpModePortID.setStatus("current")


class _HmPNIODcpMode_Type(Integer32):
    """Custom type hmPNIODcpMode based on Integer32"""
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
        *(("both", 3),
          ("egress", 2),
          ("ingress", 1),
          ("none", 0))
    )


_HmPNIODcpMode_Type.__name__ = "Integer32"
_HmPNIODcpMode_Object = MibTableColumn
hmPNIODcpMode = _HmPNIODcpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 10, 1, 2),
    _HmPNIODcpMode_Type()
)
hmPNIODcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPNIODcpMode.setStatus("current")


class _HmPNIONameOfStation_Type(DisplayString):
    """Custom type hmPNIONameOfStation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_HmPNIONameOfStation_Type.__name__ = "DisplayString"
_HmPNIONameOfStation_Object = MibScalar
hmPNIONameOfStation = _HmPNIONameOfStation_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 1, 11),
    _HmPNIONameOfStation_Type()
)
hmPNIONameOfStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPNIONameOfStation.setStatus("current")
_HmProfinetIOStatisticsGroup_ObjectIdentity = ObjectIdentity
hmProfinetIOStatisticsGroup = _HmProfinetIOStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 2)
)
_HmEthernetIPConfigGroup_ObjectIdentity = ObjectIdentity
hmEthernetIPConfigGroup = _HmEthernetIPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3)
)


class _HmEtherNetIPAdminStatus_Type(Integer32):
    """Custom type hmEtherNetIPAdminStatus based on Integer32"""
    defaultValue = 2

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


_HmEtherNetIPAdminStatus_Type.__name__ = "Integer32"
_HmEtherNetIPAdminStatus_Object = MibScalar
hmEtherNetIPAdminStatus = _HmEtherNetIPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3, 1),
    _HmEtherNetIPAdminStatus_Type()
)
hmEtherNetIPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmEtherNetIPAdminStatus.setStatus("current")


class _HmEtherNetIPErrorCode_Type(Integer32):
    """Custom type hmEtherNetIPErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmEtherNetIPErrorCode_Type.__name__ = "Integer32"
_HmEtherNetIPErrorCode_Object = MibScalar
hmEtherNetIPErrorCode = _HmEtherNetIPErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3, 2),
    _HmEtherNetIPErrorCode_Type()
)
hmEtherNetIPErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPErrorCode.setStatus("current")


class _HmEtherNetIPProductCode_Type(Integer32):
    """Custom type hmEtherNetIPProductCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HmEtherNetIPProductCode_Type.__name__ = "Integer32"
_HmEtherNetIPProductCode_Object = MibScalar
hmEtherNetIPProductCode = _HmEtherNetIPProductCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3, 3),
    _HmEtherNetIPProductCode_Type()
)
hmEtherNetIPProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPProductCode.setStatus("current")


class _HmEtherNetIPRevisionMajor_Type(Integer32):
    """Custom type hmEtherNetIPRevisionMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmEtherNetIPRevisionMajor_Type.__name__ = "Integer32"
_HmEtherNetIPRevisionMajor_Object = MibScalar
hmEtherNetIPRevisionMajor = _HmEtherNetIPRevisionMajor_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3, 4),
    _HmEtherNetIPRevisionMajor_Type()
)
hmEtherNetIPRevisionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPRevisionMajor.setStatus("current")


class _HmEtherNetIPRevisionMinor_Type(Integer32):
    """Custom type hmEtherNetIPRevisionMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmEtherNetIPRevisionMinor_Type.__name__ = "Integer32"
_HmEtherNetIPRevisionMinor_Object = MibScalar
hmEtherNetIPRevisionMinor = _HmEtherNetIPRevisionMinor_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3, 5),
    _HmEtherNetIPRevisionMinor_Type()
)
hmEtherNetIPRevisionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPRevisionMinor.setStatus("current")


class _HmEtherNetIPProductName_Type(DisplayString):
    """Custom type hmEtherNetIPProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmEtherNetIPProductName_Type.__name__ = "DisplayString"
_HmEtherNetIPProductName_Object = MibScalar
hmEtherNetIPProductName = _HmEtherNetIPProductName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3, 6),
    _HmEtherNetIPProductName_Type()
)
hmEtherNetIPProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPProductName.setStatus("current")
_HmEtherNetIPCatalogName_Type = DisplayString
_HmEtherNetIPCatalogName_Object = MibScalar
hmEtherNetIPCatalogName = _HmEtherNetIPCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 3, 7),
    _HmEtherNetIPCatalogName_Type()
)
hmEtherNetIPCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPCatalogName.setStatus("current")
_HmEthernetIPStatisticsGroup_ObjectIdentity = ObjectIdentity
hmEthernetIPStatisticsGroup = _HmEthernetIPStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 4)
)
_HmEtherNetIPConnEstablished_Type = Integer32
_HmEtherNetIPConnEstablished_Object = MibScalar
hmEtherNetIPConnEstablished = _HmEtherNetIPConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 4, 1),
    _HmEtherNetIPConnEstablished_Type()
)
hmEtherNetIPConnEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPConnEstablished.setStatus("current")
_HmEtherNetIPConnTimeouts_Type = Integer32
_HmEtherNetIPConnTimeouts_Object = MibScalar
hmEtherNetIPConnTimeouts = _HmEtherNetIPConnTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 4, 2),
    _HmEtherNetIPConnTimeouts_Type()
)
hmEtherNetIPConnTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPConnTimeouts.setStatus("current")
_HmEtherNetIPVendorObjRequests_Type = Integer32
_HmEtherNetIPVendorObjRequests_Object = MibScalar
hmEtherNetIPVendorObjRequests = _HmEtherNetIPVendorObjRequests_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 16, 4, 3),
    _HmEtherNetIPVendorObjRequests_Type()
)
hmEtherNetIPVendorObjRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmEtherNetIPVendorObjRequests.setStatus("current")
_HmAgentLoginGroup_ObjectIdentity = ObjectIdentity
hmAgentLoginGroup = _HmAgentLoginGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 17)
)


class _HmAgentLoginBanner_Type(OctetString):
    """Custom type hmAgentLoginBanner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmAgentLoginBanner_Type.__name__ = "OctetString"
_HmAgentLoginBanner_Object = MibScalar
hmAgentLoginBanner = _HmAgentLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 17, 1),
    _HmAgentLoginBanner_Type()
)
hmAgentLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmAgentLoginBanner.setStatus("current")
_HmPortMonitorGroup_ObjectIdentity = ObjectIdentity
hmPortMonitorGroup = _HmPortMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18)
)


class _HmPortMonitorAdminMode_Type(TruthValue):
    """Custom type hmPortMonitorAdminMode based on TruthValue"""


_HmPortMonitorAdminMode_Object = MibScalar
hmPortMonitorAdminMode = _HmPortMonitorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 1),
    _HmPortMonitorAdminMode_Type()
)
hmPortMonitorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorAdminMode.setStatus("current")
_HmPortMonitorIntfTable_Object = MibTable
hmPortMonitorIntfTable = _HmPortMonitorIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 2)
)
if mibBuilder.loadTexts:
    hmPortMonitorIntfTable.setStatus("current")
_HmPortMonitorIntfEntry_Object = MibTableRow
hmPortMonitorIntfEntry = _HmPortMonitorIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 2, 1)
)
hmPortMonitorIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hmPortMonitorIntfEntry.setStatus("current")


class _HmPortMonitorIntfMode_Type(TruthValue):
    """Custom type hmPortMonitorIntfMode based on TruthValue"""


_HmPortMonitorIntfMode_Object = MibTableColumn
hmPortMonitorIntfMode = _HmPortMonitorIntfMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 2, 1, 1),
    _HmPortMonitorIntfMode_Type()
)
hmPortMonitorIntfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorIntfMode.setStatus("current")


class _HmPortMonitorIntfReset_Type(TruthValue):
    """Custom type hmPortMonitorIntfReset based on TruthValue"""


_HmPortMonitorIntfReset_Object = MibTableColumn
hmPortMonitorIntfReset = _HmPortMonitorIntfReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 2, 1, 2),
    _HmPortMonitorIntfReset_Type()
)
hmPortMonitorIntfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorIntfReset.setStatus("current")


class _HmPortMonitorIntfAction_Type(Integer32):
    """Custom type hmPortMonitorIntfAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-disable", 1),
          ("trap-only", 2))
    )


_HmPortMonitorIntfAction_Type.__name__ = "Integer32"
_HmPortMonitorIntfAction_Object = MibTableColumn
hmPortMonitorIntfAction = _HmPortMonitorIntfAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 2, 1, 3),
    _HmPortMonitorIntfAction_Type()
)
hmPortMonitorIntfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorIntfAction.setStatus("current")
_HmPortMonitorConditionGroup_ObjectIdentity = ObjectIdentity
hmPortMonitorConditionGroup = _HmPortMonitorConditionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3)
)
_HmPortMonitorConditionTable_Object = MibTable
hmPortMonitorConditionTable = _HmPortMonitorConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 1)
)
if mibBuilder.loadTexts:
    hmPortMonitorConditionTable.setStatus("current")
_HmPortMonitorConditionIntfEntry_Object = MibTableRow
hmPortMonitorConditionIntfEntry = _HmPortMonitorConditionIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 1, 1)
)
hmPortMonitorConditionIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hmPortMonitorConditionIntfEntry.setStatus("current")


class _HmPortMonitorConditionLinkFlapMode_Type(TruthValue):
    """Custom type hmPortMonitorConditionLinkFlapMode based on TruthValue"""


_HmPortMonitorConditionLinkFlapMode_Object = MibTableColumn
hmPortMonitorConditionLinkFlapMode = _HmPortMonitorConditionLinkFlapMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 1, 1, 1),
    _HmPortMonitorConditionLinkFlapMode_Type()
)
hmPortMonitorConditionLinkFlapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorConditionLinkFlapMode.setStatus("current")


class _HmPortMonitorConditionCrcFragmentsMode_Type(TruthValue):
    """Custom type hmPortMonitorConditionCrcFragmentsMode based on TruthValue"""


_HmPortMonitorConditionCrcFragmentsMode_Object = MibTableColumn
hmPortMonitorConditionCrcFragmentsMode = _HmPortMonitorConditionCrcFragmentsMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 1, 1, 2),
    _HmPortMonitorConditionCrcFragmentsMode_Type()
)
hmPortMonitorConditionCrcFragmentsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorConditionCrcFragmentsMode.setStatus("current")


class _HmPortMonitorConditionField_Type(Bits):
    """Custom type hmPortMonitorConditionField based on Bits"""
    namedValues = NamedValues(
        *(("crcFragments", 2),
          ("link-flap", 1),
          ("none", 0))
    )

_HmPortMonitorConditionField_Type.__name__ = "Bits"
_HmPortMonitorConditionField_Object = MibTableColumn
hmPortMonitorConditionField = _HmPortMonitorConditionField_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 1, 1, 3),
    _HmPortMonitorConditionField_Type()
)
hmPortMonitorConditionField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortMonitorConditionField.setStatus("current")
_HmPortMonitorConditionLinkFlapGroup_ObjectIdentity = ObjectIdentity
hmPortMonitorConditionLinkFlapGroup = _HmPortMonitorConditionLinkFlapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 2)
)


class _HmPortMonitorConditionLinkFlapInterval_Type(Integer32):
    """Custom type hmPortMonitorConditionLinkFlapInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_HmPortMonitorConditionLinkFlapInterval_Type.__name__ = "Integer32"
_HmPortMonitorConditionLinkFlapInterval_Object = MibScalar
hmPortMonitorConditionLinkFlapInterval = _HmPortMonitorConditionLinkFlapInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 2, 1),
    _HmPortMonitorConditionLinkFlapInterval_Type()
)
hmPortMonitorConditionLinkFlapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorConditionLinkFlapInterval.setStatus("current")


class _HmPortMonitorConditionLinkFlapCount_Type(Integer32):
    """Custom type hmPortMonitorConditionLinkFlapCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmPortMonitorConditionLinkFlapCount_Type.__name__ = "Integer32"
_HmPortMonitorConditionLinkFlapCount_Object = MibScalar
hmPortMonitorConditionLinkFlapCount = _HmPortMonitorConditionLinkFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 2, 2),
    _HmPortMonitorConditionLinkFlapCount_Type()
)
hmPortMonitorConditionLinkFlapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorConditionLinkFlapCount.setStatus("current")
_HmPortMonitorConditionLinkFlapIntfTable_Object = MibTable
hmPortMonitorConditionLinkFlapIntfTable = _HmPortMonitorConditionLinkFlapIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hmPortMonitorConditionLinkFlapIntfTable.setStatus("current")
_HmPortMonitorConditionLinkFlapIntfEntry_Object = MibTableRow
hmPortMonitorConditionLinkFlapIntfEntry = _HmPortMonitorConditionLinkFlapIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 2, 3, 1)
)
hmPortMonitorConditionLinkFlapIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hmPortMonitorConditionLinkFlapIntfEntry.setStatus("current")
_HmPortMonitorConditionLinkFlapCountInterval_Type = Integer32
_HmPortMonitorConditionLinkFlapCountInterval_Object = MibTableColumn
hmPortMonitorConditionLinkFlapCountInterval = _HmPortMonitorConditionLinkFlapCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 2, 3, 1, 1),
    _HmPortMonitorConditionLinkFlapCountInterval_Type()
)
hmPortMonitorConditionLinkFlapCountInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortMonitorConditionLinkFlapCountInterval.setStatus("current")
_HmPortMonitorConditionLinkFlapCountTotal_Type = Integer32
_HmPortMonitorConditionLinkFlapCountTotal_Object = MibTableColumn
hmPortMonitorConditionLinkFlapCountTotal = _HmPortMonitorConditionLinkFlapCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 2, 3, 1, 2),
    _HmPortMonitorConditionLinkFlapCountTotal_Type()
)
hmPortMonitorConditionLinkFlapCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortMonitorConditionLinkFlapCountTotal.setStatus("current")
_HmPortMonitorConditionCrcFragmentsGroup_ObjectIdentity = ObjectIdentity
hmPortMonitorConditionCrcFragmentsGroup = _HmPortMonitorConditionCrcFragmentsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 3)
)


class _HmPortMonitorConditionCrcFragmentsInterval_Type(Integer32):
    """Custom type hmPortMonitorConditionCrcFragmentsInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 180),
    )


_HmPortMonitorConditionCrcFragmentsInterval_Type.__name__ = "Integer32"
_HmPortMonitorConditionCrcFragmentsInterval_Object = MibScalar
hmPortMonitorConditionCrcFragmentsInterval = _HmPortMonitorConditionCrcFragmentsInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 3, 1),
    _HmPortMonitorConditionCrcFragmentsInterval_Type()
)
hmPortMonitorConditionCrcFragmentsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorConditionCrcFragmentsInterval.setStatus("current")


class _HmPortMonitorConditionCrcFragmentsCount_Type(Integer32):
    """Custom type hmPortMonitorConditionCrcFragmentsCount based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_HmPortMonitorConditionCrcFragmentsCount_Type.__name__ = "Integer32"
_HmPortMonitorConditionCrcFragmentsCount_Object = MibScalar
hmPortMonitorConditionCrcFragmentsCount = _HmPortMonitorConditionCrcFragmentsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 3, 2),
    _HmPortMonitorConditionCrcFragmentsCount_Type()
)
hmPortMonitorConditionCrcFragmentsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmPortMonitorConditionCrcFragmentsCount.setStatus("current")
_HmPortMonitorConditionCrcFragmentsIntfTable_Object = MibTable
hmPortMonitorConditionCrcFragmentsIntfTable = _HmPortMonitorConditionCrcFragmentsIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hmPortMonitorConditionCrcFragmentsIntfTable.setStatus("current")
_HmPortMonitorConditionCrcFragmentsIntfEntry_Object = MibTableRow
hmPortMonitorConditionCrcFragmentsIntfEntry = _HmPortMonitorConditionCrcFragmentsIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 3, 3, 1)
)
hmPortMonitorConditionCrcFragmentsIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hmPortMonitorConditionCrcFragmentsIntfEntry.setStatus("current")
_HmPortMonitorConditionCrcFragmentsCountInterval_Type = Integer32
_HmPortMonitorConditionCrcFragmentsCountInterval_Object = MibTableColumn
hmPortMonitorConditionCrcFragmentsCountInterval = _HmPortMonitorConditionCrcFragmentsCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 3, 3, 1, 1),
    _HmPortMonitorConditionCrcFragmentsCountInterval_Type()
)
hmPortMonitorConditionCrcFragmentsCountInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortMonitorConditionCrcFragmentsCountInterval.setStatus("current")
_HmPortMonitorConditionCrcFragmentsCountTotal_Type = Integer32
_HmPortMonitorConditionCrcFragmentsCountTotal_Object = MibTableColumn
hmPortMonitorConditionCrcFragmentsCountTotal = _HmPortMonitorConditionCrcFragmentsCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 18, 3, 3, 3, 1, 2),
    _HmPortMonitorConditionCrcFragmentsCountTotal_Type()
)
hmPortMonitorConditionCrcFragmentsCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmPortMonitorConditionCrcFragmentsCountTotal.setStatus("current")
_HmProducts_ObjectIdentity = ObjectIdentity
hmProducts = _HmProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10)
)
_Rs2_ObjectIdentity = ObjectIdentity
rs2 = _Rs2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 2)
)
_Mach3000_ObjectIdentity = ObjectIdentity
mach3000 = _Mach3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 3)
)
_Ms2108_2_ObjectIdentity = ObjectIdentity
ms2108_2 = _Ms2108_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 4)
)
_Ms3124_4_ObjectIdentity = ObjectIdentity
ms3124_4 = _Ms3124_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 5)
)
_Rs2_16_ObjectIdentity = ObjectIdentity
rs2_16 = _Rs2_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 6)
)
_Rs2_4r_ObjectIdentity = ObjectIdentity
rs2_4r = _Rs2_4r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 7)
)
_Ms4128_5_ObjectIdentity = ObjectIdentity
ms4128_5 = _Ms4128_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 10)
)
_Eagle_ObjectIdentity = ObjectIdentity
eagle = _Eagle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 20)
)
_Rr_epl_ObjectIdentity = ObjectIdentity
rr_epl = _Rr_epl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 21)
)
_Eagle_mguard_ObjectIdentity = ObjectIdentity
eagle_mguard = _Eagle_mguard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 22)
)
_Eagle20_ObjectIdentity = ObjectIdentity
eagle20 = _Eagle20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 23)
)
_Ms20_ObjectIdentity = ObjectIdentity
ms20 = _Ms20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 30)
)
_Ms30_ObjectIdentity = ObjectIdentity
ms30 = _Ms30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 31)
)
_Rs20_ObjectIdentity = ObjectIdentity
rs20 = _Rs20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 40)
)
_Rs30_ObjectIdentity = ObjectIdentity
rs30 = _Rs30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 41)
)
_Rsb20_ObjectIdentity = ObjectIdentity
rsb20 = _Rsb20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 44)
)
_Osb20_ObjectIdentity = ObjectIdentity
osb20 = _Osb20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 45)
)
_Mach4002_48_4G_ObjectIdentity = ObjectIdentity
mach4002_48_4G = _Mach4002_48_4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 50)
)
_Octopus_ObjectIdentity = ObjectIdentity
octopus = _Octopus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 60)
)
_Mach4002_24G_ObjectIdentity = ObjectIdentity
mach4002_24G = _Mach4002_24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 70)
)
_Mach4002_24G_3X_ObjectIdentity = ObjectIdentity
mach4002_24G_3X = _Mach4002_24G_3X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 71)
)
_Mach4002_48G_ObjectIdentity = ObjectIdentity
mach4002_48G = _Mach4002_48G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 75)
)
_Mach4002_48G_3X_ObjectIdentity = ObjectIdentity
mach4002_48G_3X = _Mach4002_48G_3X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 76)
)
_Ruggedswitch_ObjectIdentity = ObjectIdentity
ruggedswitch = _Ruggedswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 90)
)
_Railswitchrugged_ObjectIdentity = ObjectIdentity
railswitchrugged = _Railswitchrugged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 100)
)
_Mach100_ObjectIdentity = ObjectIdentity
mach100 = _Mach100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 110)
)
_Octopus_os_ObjectIdentity = ObjectIdentity
octopus_os = _Octopus_os_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 120)
)
_Mach100ge_ObjectIdentity = ObjectIdentity
mach100ge = _Mach100ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 130)
)
_Mach1000ge_ObjectIdentity = ObjectIdentity
mach1000ge = _Mach1000ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 131)
)
_Eem1_ObjectIdentity = ObjectIdentity
eem1 = _Eem1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 10, 200)
)

# Managed Objects groups


# Notification objects

hmGroupMapChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 1)
)
hmGroupMapChange.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmSysGroupMap"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmNeighbourSlot"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmNeighbourIpAddress"))
)
if mibBuilder.loadTexts:
    hmGroupMapChange.setStatus(
        "current"
    )

hmPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 2)
)
hmPowerSupply.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmPSState")
)
if mibBuilder.loadTexts:
    hmPowerSupply.setStatus(
        "current"
    )

hmFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 3)
)
hmFan.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmFanState")
)
if mibBuilder.loadTexts:
    hmFan.setStatus(
        "current"
    )

hmSignallingRelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 4)
)
hmSignallingRelay.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmRS2SigRelayState"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSigTrapReason"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSigReasonIndex"))
)
if mibBuilder.loadTexts:
    hmSignallingRelay.setStatus(
        "current"
    )

hmStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 5)
)
hmStandby.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmRS2OperMode")
)
if mibBuilder.loadTexts:
    hmStandby.setStatus(
        "current"
    )

hmSelftestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 6)
)
hmSelftestError.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmSelfTestCpuResult"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSelfTestBBResult"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSelfTestBPResult"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSelfTestM1Result"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSelfTestM2Result"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSelfTestM3Result"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSelfTestM4Result"))
)
if mibBuilder.loadTexts:
    hmSelftestError.setStatus(
        "current"
    )

hmModuleMapChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 7)
)
hmModuleMapChange.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmSysGroupModuleMap")
)
if mibBuilder.loadTexts:
    hmModuleMapChange.setStatus(
        "current"
    )

hmBPDUGuardTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 8)
)
hmBPDUGuardTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmIfaceStpBpduGuardStatus")
)
if mibBuilder.loadTexts:
    hmBPDUGuardTrap.setStatus(
        "current"
    )

hmSigConRelayChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 10)
)
hmSigConRelayChange.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmSigConOperState"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSigConTrapCause"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmSigConTrapCauseIndex"))
)
if mibBuilder.loadTexts:
    hmSigConRelayChange.setStatus(
        "current"
    )

hmSFPChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 11)
)
hmSFPChangeTrap.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmIfaceGroupID"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmIfaceID"))
)
if mibBuilder.loadTexts:
    hmSFPChangeTrap.setStatus(
        "current"
    )

hmIfaceUtilizationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 12)
)
hmIfaceUtilizationTrap.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmIfaceUtilizationAlarmCondition"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmIfaceUtilization"))
)
if mibBuilder.loadTexts:
    hmIfaceUtilizationTrap.setStatus(
        "current"
    )

hmDevMonStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 13)
)
hmDevMonStateChange.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmDevMonSwitchState"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmDevMonTrapCause"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmDevMonTrapCauseIndex"))
)
if mibBuilder.loadTexts:
    hmDevMonStateChange.setStatus(
        "current"
    )

hmSFPRxPowerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 14)
)
hmSFPRxPowerChangeTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmSfpRxPowerState")
)
if mibBuilder.loadTexts:
    hmSFPRxPowerChangeTrap.setStatus(
        "current"
    )

hmSysSelftestRebootOnErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 1, 0, 15)
)
hmSysSelftestRebootOnErrorTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmSysSelftestRebootOnError")
)
if mibBuilder.loadTexts:
    hmSysSelftestRebootOnErrorTrap.setStatus(
        "current"
    )

hmTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 1)
)
hmTemperatureTrap.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmTemperature"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmTempUprLimit"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmTempLwrLimit"))
)
if mibBuilder.loadTexts:
    hmTemperatureTrap.setStatus(
        "current"
    )

hmLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 2)
)
hmLoginTrap.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmLastIpAddr"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmLastCommunity"))
)
if mibBuilder.loadTexts:
    hmLoginTrap.setStatus(
        "current"
    )

hmDuplicateStaticAddressTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 3)
)
hmDuplicateStaticAddressTrap.setObjects(
    ("BRIDGE-MIB", "dot1dStaticAddress")
)
if mibBuilder.loadTexts:
    hmDuplicateStaticAddressTrap.setStatus(
        "current"
    )

hmAutoconfigAdapterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 4)
)
hmAutoconfigAdapterTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmAutoconfigAdapterStatus")
)
if mibBuilder.loadTexts:
    hmAutoconfigAdapterTrap.setStatus(
        "current"
    )

hmRelayDuplicateIPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 5)
)
hmRelayDuplicateIPTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmRelayLastDuplicateIP")
)
if mibBuilder.loadTexts:
    hmRelayDuplicateIPTrap.setStatus(
        "current"
    )

hmSNTPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 6)
)
hmSNTPTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmNetSNTPOperStatus")
)
if mibBuilder.loadTexts:
    hmSNTPTrap.setStatus(
        "current"
    )

hmNetACDNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 7)
)
hmNetACDNotification.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmNetACDTimeMark"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmNetACDAddrSubtype"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmNetACDAddr"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmNetACDMAC"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmNetACDIfId"))
)
if mibBuilder.loadTexts:
    hmNetACDNotification.setStatus(
        "current"
    )

hmConfigurationSavedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 8)
)
hmConfigurationSavedTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmAutoconfigAdapterStatus")
)
if mibBuilder.loadTexts:
    hmConfigurationSavedTrap.setStatus(
        "current"
    )

hmConfigurationChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 9)
)
hmConfigurationChangedTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmConfigurationStatus")
)
if mibBuilder.loadTexts:
    hmConfigurationChangedTrap.setStatus(
        "current"
    )

hmAddressRelearnDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 10)
)
hmAddressRelearnDetectTrap.setObjects(
    ("HMPRIV-MGMT-SNMP-MIB", "hmSysSwitchAddressRelearnThreshold")
)
if mibBuilder.loadTexts:
    hmAddressRelearnDetectTrap.setStatus(
        "current"
    )

hmDuplexMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 11)
)
hmDuplexMismatchTrap.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmIfaceGroupID"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmIfaceID"))
)
if mibBuilder.loadTexts:
    hmDuplexMismatchTrap.setStatus(
        "current"
    )

hmNTPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 12)
)
hmNTPTrap.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmNetNTPStatusCode"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmNetNTPStatusText"))
)
if mibBuilder.loadTexts:
    hmNTPTrap.setStatus(
        "current"
    )

hmPortMonitorPortDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 13)
)
hmPortMonitorPortDisabledTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmPortMonitorConditionField"))
)
if mibBuilder.loadTexts:
    hmPortMonitorPortDisabledTrap.setStatus(
        "current"
    )

hmPOEModulePowerUsageOnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 14)
)
hmPOEModulePowerUsageOnNotification.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmPOEModuleIndex"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmPOEModuleDeliveredPower"))
)
if mibBuilder.loadTexts:
    hmPOEModulePowerUsageOnNotification.setStatus(
        "current"
    )

hmPOEModulePowerUsageOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 15)
)
hmPOEModulePowerUsageOffNotification.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmPOEModuleIndex"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmPOEModuleDeliveredPower"))
)
if mibBuilder.loadTexts:
    hmPOEModulePowerUsageOffNotification.setStatus(
        "current"
    )

hmSysSelftestPortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 14, 2, 0, 16)
)
hmSysSelftestPortError.setObjects(
      *(("HMPRIV-MGMT-SNMP-MIB", "hmIfaceGroupID"),
        ("HMPRIV-MGMT-SNMP-MIB", "hmIfaceID"))
)
if mibBuilder.loadTexts:
    hmSysSelftestPortError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    **{"HmAgentLogSeverity": HmAgentLogSeverity,
       "LEDState": LEDState,
       "DIPSwitchState": DIPSwitchState,
       "PTPTimeInterval": PTPTimeInterval,
       "PTPPortIdentity": PTPPortIdentity,
       "PTPClockIdentity": PTPClockIdentity,
       "PTPClockQuality": PTPClockQuality,
       "BridgeIdOrNull": BridgeIdOrNull,
       "hirschmann": hirschmann,
       "hmConfiguration": hmConfiguration,
       "hmChassis": hmChassis,
       "hmChassisEvent": hmChassisEvent,
       "hmGroupMapChange": hmGroupMapChange,
       "hmPowerSupply": hmPowerSupply,
       "hmFan": hmFan,
       "hmSignallingRelay": hmSignallingRelay,
       "hmStandby": hmStandby,
       "hmSelftestError": hmSelftestError,
       "hmModuleMapChange": hmModuleMapChange,
       "hmBPDUGuardTrap": hmBPDUGuardTrap,
       "hmSigConRelayChange": hmSigConRelayChange,
       "hmSFPChangeTrap": hmSFPChangeTrap,
       "hmIfaceUtilizationTrap": hmIfaceUtilizationTrap,
       "hmDevMonStateChange": hmDevMonStateChange,
       "hmSFPRxPowerChangeTrap": hmSFPRxPowerChangeTrap,
       "hmSysSelftestRebootOnErrorTrap": hmSysSelftestRebootOnErrorTrap,
       "hmSystemTable": hmSystemTable,
       "hmSysProduct": hmSysProduct,
       "hmSysVersion": hmSysVersion,
       "hmSysGroupCapacity": hmSysGroupCapacity,
       "hmSysGroupMap": hmSysGroupMap,
       "hmSysMaxPowerSupply": hmSysMaxPowerSupply,
       "hmSysMaxFan": hmSysMaxFan,
       "hmSysGroupModuleCapacity": hmSysGroupModuleCapacity,
       "hmSysModulePortCapacity": hmSysModulePortCapacity,
       "hmSysGroupTable": hmSysGroupTable,
       "hmSysGroupEntry": hmSysGroupEntry,
       "hmSysGroupID": hmSysGroupID,
       "hmSysGroupType": hmSysGroupType,
       "hmSysGroupDescription": hmSysGroupDescription,
       "hmSysGroupHwVersion": hmSysGroupHwVersion,
       "hmSysGroupSwVersion": hmSysGroupSwVersion,
       "hmSysGroupModuleMap": hmSysGroupModuleMap,
       "hmSysGroupAction": hmSysGroupAction,
       "hmSysGroupActionResult": hmSysGroupActionResult,
       "hmSysGroupIsolateMode": hmSysGroupIsolateMode,
       "hmSysGroupSerialNum": hmSysGroupSerialNum,
       "hmSysGroupActionDelayPreset": hmSysGroupActionDelayPreset,
       "hmSysGroupActionDelayCurrent": hmSysGroupActionDelayCurrent,
       "hmSysModuleTable": hmSysModuleTable,
       "hmSysModuleEntry": hmSysModuleEntry,
       "hmSysModGroupID": hmSysModGroupID,
       "hmSysModID": hmSysModID,
       "hmSysModType": hmSysModType,
       "hmSysModDescription": hmSysModDescription,
       "hmSysModVersion": hmSysModVersion,
       "hmSysModNumOfPorts": hmSysModNumOfPorts,
       "hmSysModFirstMauIndex": hmSysModFirstMauIndex,
       "hmSysModStatus": hmSysModStatus,
       "hmSysModSerialNum": hmSysModSerialNum,
       "hmInterfaceTable": hmInterfaceTable,
       "hmInterfaceEntry": hmInterfaceEntry,
       "hmIfaceGroupID": hmIfaceGroupID,
       "hmIfaceID": hmIfaceID,
       "hmIfaceStpEnable": hmIfaceStpEnable,
       "hmIfaceLinkType": hmIfaceLinkType,
       "hmIfaceAction": hmIfaceAction,
       "hmIfaceNextHopMacAddress": hmIfaceNextHopMacAddress,
       "hmIfaceFlowControl": hmIfaceFlowControl,
       "hmIfacePriorityThreshold": hmIfacePriorityThreshold,
       "hmIfaceName": hmIfaceName,
       "hmIfaceTrunkID": hmIfaceTrunkID,
       "hmIfacePrioTOSEnable": hmIfacePrioTOSEnable,
       "hmIfaceBcastLimit": hmIfaceBcastLimit,
       "hmIfaceUtilization": hmIfaceUtilization,
       "hmIfaceUtilizationControlInterval": hmIfaceUtilizationControlInterval,
       "hmIfaceStpBpduGuardEnable": hmIfaceStpBpduGuardEnable,
       "hmIfaceStpBpduGuardStatus": hmIfaceStpBpduGuardStatus,
       "hmIfaceCapability": hmIfaceCapability,
       "hmIfaceIngressLimiterMode": hmIfaceIngressLimiterMode,
       "hmIfaceIngressLimiterCalculationMode": hmIfaceIngressLimiterCalculationMode,
       "hmIfaceIngressLimiterRate": hmIfaceIngressLimiterRate,
       "hmIfaceEgressLimiterMode": hmIfaceEgressLimiterMode,
       "hmIfaceEgressLimiterCalculationMode": hmIfaceEgressLimiterCalculationMode,
       "hmIfaceEgressLimiterRate": hmIfaceEgressLimiterRate,
       "hmIfaceUtilizationAlarmUpperThreshold": hmIfaceUtilizationAlarmUpperThreshold,
       "hmIfaceUtilizationAlarmLowerThreshold": hmIfaceUtilizationAlarmLowerThreshold,
       "hmIfaceUtilizationAlarmCondition": hmIfaceUtilizationAlarmCondition,
       "hmIfaceCableCrossing": hmIfaceCableCrossing,
       "hmIfacePhyFastLinkDetection": hmIfacePhyFastLinkDetection,
       "hmTrunkTable": hmTrunkTable,
       "hmTrunkEntry": hmTrunkEntry,
       "hmTrunkID": hmTrunkID,
       "hmTrunkInterfaces": hmTrunkInterfaces,
       "hmTrunkName": hmTrunkName,
       "hmTrunkAction": hmTrunkAction,
       "hmTrunkAdminStatus": hmTrunkAdminStatus,
       "hmTrunkOperStatus": hmTrunkOperStatus,
       "hmTrunkLastChange": hmTrunkLastChange,
       "hmSFPTable": hmSFPTable,
       "hmSFPEntry": hmSFPEntry,
       "hmSfpGroupID": hmSfpGroupID,
       "hmSfpID": hmSfpID,
       "hmSfpConnector": hmSfpConnector,
       "hmSfpTransceiver": hmSfpTransceiver,
       "hmSfpVendorOUI": hmSfpVendorOUI,
       "hmSfpVendorName": hmSfpVendorName,
       "hmSfpPartNumber": hmSfpPartNumber,
       "hmSfpPartRev": hmSfpPartRev,
       "hmSfpSerialNum": hmSfpSerialNum,
       "hmSfpDateCode": hmSfpDateCode,
       "hmSfpBitRate": hmSfpBitRate,
       "hmSfpTemperature": hmSfpTemperature,
       "hmSfpTxPower": hmSfpTxPower,
       "hmSfpRxPower": hmSfpRxPower,
       "hmSfpTxPowerInt": hmSfpTxPowerInt,
       "hmSfpRxPowerInt": hmSfpRxPowerInt,
       "hmSfpRxPowerState": hmSfpRxPowerState,
       "hmSfpInfoVersion": hmSfpInfoVersion,
       "hmSfpInfoPartNumber": hmSfpInfoPartNumber,
       "hmSfpInfoPartId": hmSfpInfoPartId,
       "hmSfpInfoMagic": hmSfpInfoMagic,
       "hmSfpSupported": hmSfpSupported,
       "hmSfpMaxLength-fiber-9": hmSfpMaxLength_fiber_9,
       "hmSfpMaxLength-fiber-50": hmSfpMaxLength_fiber_50,
       "hmSfpMaxLength-fiber-62-5": hmSfpMaxLength_fiber_62_5,
       "hmSfpMaxLength-copper": hmSfpMaxLength_copper,
       "hmSfpTxPowerdBm": hmSfpTxPowerdBm,
       "hmSfpRxPowerdBm": hmSfpRxPowerdBm,
       "hmSysChassisName": hmSysChassisName,
       "hmSysStpEnable": hmSysStpEnable,
       "hmSysFlowControl": hmSysFlowControl,
       "hmSysBOOTPEnable": hmSysBOOTPEnable,
       "hmSysDHCPEnable": hmSysDHCPEnable,
       "hmSysTelnetEnable": hmSysTelnetEnable,
       "hmSysHTTPEnable": hmSysHTTPEnable,
       "hmSysPlugAndPlay": hmSysPlugAndPlay,
       "hmBcastLimiterMode": hmBcastLimiterMode,
       "hmSystemTime": hmSystemTime,
       "hmSystemTimeSource": hmSystemTimeSource,
       "hmSysStpBPDUGuardEnable": hmSysStpBPDUGuardEnable,
       "hmSysSTPErrorNumber": hmSysSTPErrorNumber,
       "hmSysSoftwareCapability": hmSysSoftwareCapability,
       "hmLEDGroup": hmLEDGroup,
       "hmLEDRSGroup": hmLEDRSGroup,
       "hmLEDRSPowerSupply": hmLEDRSPowerSupply,
       "hmLEDRStandby": hmLEDRStandby,
       "hmLEDRSRedundancyManager": hmLEDRSRedundancyManager,
       "hmLEDRSFault": hmLEDRSFault,
       "hmLEDOctGroup": hmLEDOctGroup,
       "hmLEDOctPowerSupply1": hmLEDOctPowerSupply1,
       "hmLEDOctPowerSupply2": hmLEDOctPowerSupply2,
       "hmLEDOctRedundancyManager": hmLEDOctRedundancyManager,
       "hmLEDOctFault": hmLEDOctFault,
       "hmLEDRSRGroup": hmLEDRSRGroup,
       "hmLEDRSRPowerSupply": hmLEDRSRPowerSupply,
       "hmLEDRSRStandby": hmLEDRSRStandby,
       "hmLEDRSRRedundancyManager": hmLEDRSRRedundancyManager,
       "hmLEDRSRFault": hmLEDRSRFault,
       "hmLEDRSRRelay1": hmLEDRSRRelay1,
       "hmLEDRSRRelay2": hmLEDRSRRelay2,
       "hmDIPSwitchGroup": hmDIPSwitchGroup,
       "hmDIPSwitchRSGroup": hmDIPSwitchRSGroup,
       "hmDIPSwitchRSRedundancyManager": hmDIPSwitchRSRedundancyManager,
       "hmDIPSwitchRSStandby": hmDIPSwitchRSStandby,
       "hmDIPSwitchMICEGroup": hmDIPSwitchMICEGroup,
       "hmDIPSwitchMICERedundancyManager": hmDIPSwitchMICERedundancyManager,
       "hmDIPSwitchMICERingPort": hmDIPSwitchMICERingPort,
       "hmDIPSwitchMICEStandby": hmDIPSwitchMICEStandby,
       "hmDIPSwitchMICEConfig": hmDIPSwitchMICEConfig,
       "hmSysMaxTrunks": hmSysMaxTrunks,
       "hmLimiterGroup": hmLimiterGroup,
       "hmIngressLimiterGroup": hmIngressLimiterGroup,
       "hmIngressLimiterEnable": hmIngressLimiterEnable,
       "hmIngressLimiterMode": hmIngressLimiterMode,
       "hmIngressUnknUcLimiterGroup": hmIngressUnknUcLimiterGroup,
       "hmIngressUnknUcLimiterMode": hmIngressUnknUcLimiterMode,
       "hmIngressUnknUcLimiterCalculationMode": hmIngressUnknUcLimiterCalculationMode,
       "hmIngressUnknUcLimiterRate": hmIngressUnknUcLimiterRate,
       "hmEgressLimiterGroup": hmEgressLimiterGroup,
       "hmEgressLimiterEnable": hmEgressLimiterEnable,
       "hmSysUSBGroup": hmSysUSBGroup,
       "hmSysMaxUSBPorts": hmSysMaxUSBPorts,
       "hmSysSwitchGroup": hmSysSwitchGroup,
       "hmSysSwitchLearning": hmSysSwitchLearning,
       "hmSysSwitchMRU": hmSysSwitchMRU,
       "hmSysSwitchFastLinkDetection": hmSysSwitchFastLinkDetection,
       "hmSysSwitchAddressRelearnDetection": hmSysSwitchAddressRelearnDetection,
       "hmSysSwitchAddressRelearnThreshold": hmSysSwitchAddressRelearnThreshold,
       "hmSysSwitchDuplexMismatchDetection": hmSysSwitchDuplexMismatchDetection,
       "hmSysSwitchFDBFullCounter": hmSysSwitchFDBFullCounter,
       "hmSysSwitchFDBHashOptimizingMode": hmSysSwitchFDBHashOptimizingMode,
       "hmSysSwitchFDBHashOptimizingStatus": hmSysSwitchFDBHashOptimizingStatus,
       "hmSysSwitchVLANGroup": hmSysSwitchVLANGroup,
       "hmSysSwitchVLANLearningMode": hmSysSwitchVLANLearningMode,
       "hmSysSwitchVLANLearningStatus": hmSysSwitchVLANLearningStatus,
       "hmSysSwitchServiceModeGroup": hmSysSwitchServiceModeGroup,
       "hmSysSwitchServiceMode": hmSysSwitchServiceMode,
       "hmSysSwitchServiceVlan": hmSysSwitchServiceVlan,
       "hmSysSwitchServiceModeOperState": hmSysSwitchServiceModeOperState,
       "hmSysSwitchRedundancyGroup": hmSysSwitchRedundancyGroup,
       "hmSysSwitchRedundancyRstpMrpMode": hmSysSwitchRedundancyRstpMrpMode,
       "hmSysSwitchRedundancyRstpMrpConfigError": hmSysSwitchRedundancyRstpMrpConfigError,
       "hmSysSwitchRedundancyRstpMrpConfigErrorBridge": hmSysSwitchRedundancyRstpMrpConfigErrorBridge,
       "hmSysSelftestGroup": hmSysSelftestGroup,
       "hmSysSelftestRAM": hmSysSelftestRAM,
       "hmSysSelftestRebootOnError": hmSysSelftestRebootOnError,
       "hmSysSelftestMMUStatus": hmSysSelftestMMUStatus,
       "hmSysSelftestRebootOnHdxError": hmSysSelftestRebootOnHdxError,
       "hmSysOEMGroup": hmSysOEMGroup,
       "hmSysOEMID": hmSysOEMID,
       "hmSysMaxSignalContacts": hmSysMaxSignalContacts,
       "hmSysHttpsEnable": hmSysHttpsEnable,
       "hmSysHttpsPortNumber": hmSysHttpsPortNumber,
       "hmSysSkipAcaOnBoot": hmSysSkipAcaOnBoot,
       "hmPSTable": hmPSTable,
       "hmPSEntry": hmPSEntry,
       "hmPSSysID": hmPSSysID,
       "hmPSID": hmPSID,
       "hmPSState": hmPSState,
       "hmPSType": hmPSType,
       "hmPSVersion": hmPSVersion,
       "hmPSDescription": hmPSDescription,
       "hmPSSerialNumber": hmPSSerialNumber,
       "hmPSProductCode": hmPSProductCode,
       "hmPSPowerBudget": hmPSPowerBudget,
       "hmFanTable": hmFanTable,
       "hmFanEntry": hmFanEntry,
       "hmFanSysID": hmFanSysID,
       "hmFanID": hmFanID,
       "hmFanState": hmFanState,
       "hmFwdPriorityConfiguration": hmFwdPriorityConfiguration,
       "hmPrioTOSEnable": hmPrioTOSEnable,
       "hmPrioMACAddressEnable": hmPrioMACAddressEnable,
       "hmPrioVlan0TagTransparentMode": hmPrioVlan0TagTransparentMode,
       "hmPrioMACAddressTable": hmPrioMACAddressTable,
       "hmPrioMACAddressEntry": hmPrioMACAddressEntry,
       "hmPrioMACAddress": hmPrioMACAddress,
       "hmPrioMACReceivePort": hmPrioMACReceivePort,
       "hmPrioMACPriority": hmPrioMACPriority,
       "hmPrioMACStatus": hmPrioMACStatus,
       "hmPrioTrafficClassTable": hmPrioTrafficClassTable,
       "hmPrioTrafficClassEntry": hmPrioTrafficClassEntry,
       "hmPrioTrafficClassID": hmPrioTrafficClassID,
       "hmPrioTrafficClassWeight": hmPrioTrafficClassWeight,
       "hmPrioTosToPrioTable": hmPrioTosToPrioTable,
       "hmPrioTosToPrioEntry": hmPrioTosToPrioEntry,
       "hmPrioTTPTos": hmPrioTTPTos,
       "hmPrioTTPPrio": hmPrioTTPPrio,
       "hmCurrentAddressTable": hmCurrentAddressTable,
       "hmCurrentAddressEntry": hmCurrentAddressEntry,
       "hmCurrentAddress": hmCurrentAddress,
       "hmCurrentAddressReceivePort": hmCurrentAddressReceivePort,
       "hmCurrentAddressStaticEgressPorts": hmCurrentAddressStaticEgressPorts,
       "hmCurrentAddressEgressPorts": hmCurrentAddressEgressPorts,
       "hmCurrentAddressStatus": hmCurrentAddressStatus,
       "hmRS2ext": hmRS2ext,
       "hmRS2OperMode": hmRS2OperMode,
       "hmRS2ConfigError": hmRS2ConfigError,
       "hmRS2SigRelayState": hmRS2SigRelayState,
       "hmSigLinkTable": hmSigLinkTable,
       "hmSigLinkEntry": hmSigLinkEntry,
       "hmSigLinkID": hmSigLinkID,
       "hmSigLinkAlarm": hmSigLinkAlarm,
       "hmSigTrapReason": hmSigTrapReason,
       "hmSigReasonIndex": hmSigReasonIndex,
       "hmRS2TopologyGroup": hmRS2TopologyGroup,
       "hmRS2PartnerIpAddress": hmRS2PartnerIpAddress,
       "hmRS2TopologyTable": hmRS2TopologyTable,
       "hmRS2TopologyEntry": hmRS2TopologyEntry,
       "hmRS2TopologyLinkID": hmRS2TopologyLinkID,
       "hmRS2TopologyIpAddress": hmRS2TopologyIpAddress,
       "hmRS2ConnectionMirroringGroup": hmRS2ConnectionMirroringGroup,
       "hmRS2ConnectionMirroringStatus": hmRS2ConnectionMirroringStatus,
       "hmRS2ConnectionMirroringPortOne": hmRS2ConnectionMirroringPortOne,
       "hmRS2ConnectionMirroringPortTwo": hmRS2ConnectionMirroringPortTwo,
       "hmRS2DisableLearningGroup": hmRS2DisableLearningGroup,
       "hmRS2DisableLearningStatus": hmRS2DisableLearningStatus,
       "hmRS2SigRelayGroup": hmRS2SigRelayGroup,
       "hmRS2SigRelayMode": hmRS2SigRelayMode,
       "hmRS2SigRelayManualState": hmRS2SigRelayManualState,
       "hmRS2VlanGroup": hmRS2VlanGroup,
       "hmRS2VlanMode": hmRS2VlanMode,
       "hmRS2VlanStatus": hmRS2VlanStatus,
       "hmRS2SelftestGroup": hmRS2SelftestGroup,
       "hmRS2SelftestResult": hmRS2SelftestResult,
       "hmRS2SelftestMode": hmRS2SelftestMode,
       "hmRS2PSGroup": hmRS2PSGroup,
       "hmRS2PSAlarm": hmRS2PSAlarm,
       "hmRS2RedundancyGroup": hmRS2RedundancyGroup,
       "hmRS2RedNotGuaranteedAlarm": hmRS2RedNotGuaranteedAlarm,
       "hmRS4RGroup": hmRS4RGroup,
       "hmRS4RVlanGroup": hmRS4RVlanGroup,
       "hmRS4RVlanPortTable": hmRS4RVlanPortTable,
       "hmRS4RVlanPortEntry": hmRS4RVlanPortEntry,
       "hmRS4RVlanPortID": hmRS4RVlanPortID,
       "hmRS4RVlanPortTagFormatRstp": hmRS4RVlanPortTagFormatRstp,
       "hmRS2FDBGroup": hmRS2FDBGroup,
       "hmRS2FDBHashGroup": hmRS2FDBHashGroup,
       "hmRS2FDBHashOptimizingMode": hmRS2FDBHashOptimizingMode,
       "hmRS2FDBHashOptimizingStatus": hmRS2FDBHashOptimizingStatus,
       "hmMACH3ChassisExt": hmMACH3ChassisExt,
       "hmSelfTestResults": hmSelfTestResults,
       "hmSelfTestCpuResult": hmSelfTestCpuResult,
       "hmSelfTestBBResult": hmSelfTestBBResult,
       "hmSelfTestBPResult": hmSelfTestBPResult,
       "hmSelfTestM1Result": hmSelfTestM1Result,
       "hmSelfTestM2Result": hmSelfTestM2Result,
       "hmSelfTestM3Result": hmSelfTestM3Result,
       "hmSelfTestM4Result": hmSelfTestM4Result,
       "hmSelfTestMode": hmSelfTestMode,
       "hmMgmtBusSelected": hmMgmtBusSelected,
       "hmSerialNumbers": hmSerialNumbers,
       "hmSerialNumCpu": hmSerialNumCpu,
       "hmSerialNumBB": hmSerialNumBB,
       "hmSerialNumBP": hmSerialNumBP,
       "hmSerialNumM1": hmSerialNumM1,
       "hmSerialNumM2": hmSerialNumM2,
       "hmSerialNumM3": hmSerialNumM3,
       "hmSerialNumM4": hmSerialNumM4,
       "hmPlugAndPlay": hmPlugAndPlay,
       "hmAutoConfigState": hmAutoConfigState,
       "hmMACH3Misc": hmMACH3Misc,
       "hmUserGroupStatus": hmUserGroupStatus,
       "hmAUIGroup": hmAUIGroup,
       "hmAUIModuleTable": hmAUIModuleTable,
       "hmAUIModuleEntry": hmAUIModuleEntry,
       "hmAUIModuleID": hmAUIModuleID,
       "hmAUIModuleDTEPowerMonitor": hmAUIModuleDTEPowerMonitor,
       "hmAUIPortTable": hmAUIPortTable,
       "hmAUIPortEntry": hmAUIPortEntry,
       "hmAUIPortID": hmAUIPortID,
       "hmAUIPortDTEPower": hmAUIPortDTEPower,
       "hmAUIPortSQETest": hmAUIPortSQETest,
       "hmAgent": hmAgent,
       "hmAgentEvent": hmAgentEvent,
       "hmTemperatureTrap": hmTemperatureTrap,
       "hmLoginTrap": hmLoginTrap,
       "hmDuplicateStaticAddressTrap": hmDuplicateStaticAddressTrap,
       "hmAutoconfigAdapterTrap": hmAutoconfigAdapterTrap,
       "hmRelayDuplicateIPTrap": hmRelayDuplicateIPTrap,
       "hmSNTPTrap": hmSNTPTrap,
       "hmNetACDNotification": hmNetACDNotification,
       "hmConfigurationSavedTrap": hmConfigurationSavedTrap,
       "hmConfigurationChangedTrap": hmConfigurationChangedTrap,
       "hmAddressRelearnDetectTrap": hmAddressRelearnDetectTrap,
       "hmDuplexMismatchTrap": hmDuplexMismatchTrap,
       "hmNTPTrap": hmNTPTrap,
       "hmPortMonitorPortDisabledTrap": hmPortMonitorPortDisabledTrap,
       "hmPOEModulePowerUsageOnNotification": hmPOEModulePowerUsageOnNotification,
       "hmPOEModulePowerUsageOffNotification": hmPOEModulePowerUsageOffNotification,
       "hmSysSelftestPortError": hmSysSelftestPortError,
       "hmAction": hmAction,
       "hmActionResult": hmActionResult,
       "hmNetwork": hmNetwork,
       "hmNetLocalIPAddr": hmNetLocalIPAddr,
       "hmNetLocalPhysAddr": hmNetLocalPhysAddr,
       "hmNetGatewayIPAddr": hmNetGatewayIPAddr,
       "hmNetMask": hmNetMask,
       "hmNetPPPBaseIPAddr": hmNetPPPBaseIPAddr,
       "hmNetPPPNetMask": hmNetPPPNetMask,
       "hmNetAction": hmNetAction,
       "hmNetVlanID": hmNetVlanID,
       "hmNetLocalPhysAddrRange": hmNetLocalPhysAddrRange,
       "hmNetVlanPriority": hmNetVlanPriority,
       "hmNetIpDscpPriority": hmNetIpDscpPriority,
       "hmNetACDGroup": hmNetACDGroup,
       "hmNetACDStatus": hmNetACDStatus,
       "hmNetACDOngoingProbeStatus": hmNetACDOngoingProbeStatus,
       "hmNetACDDelay": hmNetACDDelay,
       "hmNetACDReleaseDelay": hmNetACDReleaseDelay,
       "hmNetACDMaxProtection": hmNetACDMaxProtection,
       "hmNetACDProtectInterval": hmNetACDProtectInterval,
       "hmNetACDFaultState": hmNetACDFaultState,
       "hmNetACDAddrTable": hmNetACDAddrTable,
       "hmNetACDAddrEntry": hmNetACDAddrEntry,
       "hmNetACDTimeMark": hmNetACDTimeMark,
       "hmNetACDAddrSubtype": hmNetACDAddrSubtype,
       "hmNetACDAddr": hmNetACDAddr,
       "hmNetACDMAC": hmNetACDMAC,
       "hmNetACDIfId": hmNetACDIfId,
       "hmNetHiDiscoveryGroup": hmNetHiDiscoveryGroup,
       "hmNetHiDiscoveryStatus": hmNetHiDiscoveryStatus,
       "hmNetHiDiscoveryRelay": hmNetHiDiscoveryRelay,
       "hmNetSNTPGroup": hmNetSNTPGroup,
       "hmNetSNTPStatus": hmNetSNTPStatus,
       "hmNetSNTPServer": hmNetSNTPServer,
       "hmNetSNTPTime": hmNetSNTPTime,
       "hmNetSNTPLocalOffset": hmNetSNTPLocalOffset,
       "hmNetSNTPServer2": hmNetSNTPServer2,
       "hmNetSNTPSyncInterval": hmNetSNTPSyncInterval,
       "hmNetSNTPAcceptBroadcasts": hmNetSNTPAcceptBroadcasts,
       "hmNetSNTPAnycastAddr": hmNetSNTPAnycastAddr,
       "hmNetSNTPAnycastVlan": hmNetSNTPAnycastVlan,
       "hmNetSNTPAnycastInterval": hmNetSNTPAnycastInterval,
       "hmNetSNTPOperStatus": hmNetSNTPOperStatus,
       "hmNetSNTPTimeAdjustThreshold": hmNetSNTPTimeAdjustThreshold,
       "hmNetSNTPOnceAtStartup": hmNetSNTPOnceAtStartup,
       "hmNetSNTPServerOnlyIfSync": hmNetSNTPServerOnlyIfSync,
       "hmNetSNTPServerStatus": hmNetSNTPServerStatus,
       "hmNetSNTPClientStatus": hmNetSNTPClientStatus,
       "hmNetNTPGroup": hmNetNTPGroup,
       "hmNetNTPOperation": hmNetNTPOperation,
       "hmNetNTPServer1AddrType": hmNetNTPServer1AddrType,
       "hmNetNTPServer1Address": hmNetNTPServer1Address,
       "hmNetNTPServer2AddrType": hmNetNTPServer2AddrType,
       "hmNetNTPServer2Address": hmNetNTPServer2Address,
       "hmNetNTPSyncInterval": hmNetNTPSyncInterval,
       "hmNetNTPAnycastAddrType": hmNetNTPAnycastAddrType,
       "hmNetNTPAnycastAddress": hmNetNTPAnycastAddress,
       "hmNetNTPAnycastInterval": hmNetNTPAnycastInterval,
       "hmNetNTPStatusText": hmNetNTPStatusText,
       "hmNetNTPStatusCode": hmNetNTPStatusCode,
       "hmNetPTPGroup": hmNetPTPGroup,
       "hmNetPTPConfiguration": hmNetPTPConfiguration,
       "hmNetPTPEnable": hmNetPTPEnable,
       "hmNetPTPAction": hmNetPTPAction,
       "hmNetPTPClockMode": hmNetPTPClockMode,
       "hmNetPTPSlavePort": hmNetPTPSlavePort,
       "hmNetPTPIsSynchronized": hmNetPTPIsSynchronized,
       "hmNetPTPSyncLowerBound": hmNetPTPSyncLowerBound,
       "hmNetPTPSyncUpperBound": hmNetPTPSyncUpperBound,
       "hmNetPTPClockStratum": hmNetPTPClockStratum,
       "hmNetPTPClockIdentifier": hmNetPTPClockIdentifier,
       "hmNetPTPClockVariance": hmNetPTPClockVariance,
       "hmNetPTPPreferredMaster": hmNetPTPPreferredMaster,
       "hmNetPTPSyncInterval": hmNetPTPSyncInterval,
       "hmNetPTPSubdomainName": hmNetPTPSubdomainName,
       "hmNetPTPOffsetFromMasterNanoSecs": hmNetPTPOffsetFromMasterNanoSecs,
       "hmNetPTPAbsMaxOffset": hmNetPTPAbsMaxOffset,
       "hmNetPTPOneWayDelayNanoSecs": hmNetPTPOneWayDelayNanoSecs,
       "hmNetPTPTimeSeconds": hmNetPTPTimeSeconds,
       "hmNetPTPObservedDrift": hmNetPTPObservedDrift,
       "hmNetPTPPiIntegral": hmNetPTPPiIntegral,
       "hmNetPTPParentUUID": hmNetPTPParentUUID,
       "hmNetPTPGrandmasterUUID": hmNetPTPGrandmasterUUID,
       "hmNetPTPCurrentUTCOffset": hmNetPTPCurrentUTCOffset,
       "hmNetPTPleap59": hmNetPTPleap59,
       "hmNetPTPleap61": hmNetPTPleap61,
       "hmNetPTPStepsRemoved": hmNetPTPStepsRemoved,
       "hmNetPTPEpochNumber": hmNetPTPEpochNumber,
       "hmNetPTPStaticDrift": hmNetPTPStaticDrift,
       "hmNetPTPPortTable": hmNetPTPPortTable,
       "hmNetPTPPortEntry": hmNetPTPPortEntry,
       "hmNetPTPPortID": hmNetPTPPortID,
       "hmNetPTPPortState": hmNetPTPPortState,
       "hmNetPTPPortBurstEnable": hmNetPTPPortBurstEnable,
       "hmNetPTPPortEnable": hmNetPTPPortEnable,
       "hmNetPTP2Group": hmNetPTP2Group,
       "hmNetPTP2Configuration": hmNetPTP2Configuration,
       "hmNetPTP2TwoStepClock": hmNetPTP2TwoStepClock,
       "hmNetPTP2ClockIdentity": hmNetPTP2ClockIdentity,
       "hmNetPTP2Priority1": hmNetPTP2Priority1,
       "hmNetPTP2Priority2": hmNetPTP2Priority2,
       "hmNetPTP2DomainNumber": hmNetPTP2DomainNumber,
       "hmNetPTP2StepsRemoved": hmNetPTP2StepsRemoved,
       "hmNetPTP2OffsetFromMaster": hmNetPTP2OffsetFromMaster,
       "hmNetPTP2MeanPathDelay": hmNetPTP2MeanPathDelay,
       "hmNetPTP2ParentPortIdentity": hmNetPTP2ParentPortIdentity,
       "hmNetPTP2ParentStats": hmNetPTP2ParentStats,
       "hmNetPTP2ObservedParentOffsetScaledLogVariance": hmNetPTP2ObservedParentOffsetScaledLogVariance,
       "hmNetPTP2ObservedParentClockPhaseChangeRate": hmNetPTP2ObservedParentClockPhaseChangeRate,
       "hmNetPTP2GrandmasterIdentity": hmNetPTP2GrandmasterIdentity,
       "hmNetPTP2GrandmasterClockQuality": hmNetPTP2GrandmasterClockQuality,
       "hmNetPTP2GrandmasterPriority1": hmNetPTP2GrandmasterPriority1,
       "hmNetPTP2GrandmasterPriority2": hmNetPTP2GrandmasterPriority2,
       "hmNetPTP2CurrentUtcOffset": hmNetPTP2CurrentUtcOffset,
       "hmNetPTP2CurrentUtcOffsetValid": hmNetPTP2CurrentUtcOffsetValid,
       "hmNetPTP2Leap59": hmNetPTP2Leap59,
       "hmNetPTP2Leap61": hmNetPTP2Leap61,
       "hmNetPTP2TimeTraceable": hmNetPTP2TimeTraceable,
       "hmNetPTP2FrequencyTraceable": hmNetPTP2FrequencyTraceable,
       "hmNetPTP2PtpTimescale": hmNetPTP2PtpTimescale,
       "hmNetPTP2TimeSource": hmNetPTP2TimeSource,
       "hmNetPTP2GrandmasterClockClass": hmNetPTP2GrandmasterClockClass,
       "hmNetPTP2GrandmasterClockAccuracy": hmNetPTP2GrandmasterClockAccuracy,
       "hmNetPTP2GrandmasterClockVariance": hmNetPTP2GrandmasterClockVariance,
       "hmNetPTP2PortTable": hmNetPTP2PortTable,
       "hmNetPTP2PortEntry": hmNetPTP2PortEntry,
       "hmNetPTP2PortEnable": hmNetPTP2PortEnable,
       "hmNetPTP2PortState": hmNetPTP2PortState,
       "hmNetPTP2LogDelayReqInterval": hmNetPTP2LogDelayReqInterval,
       "hmNetPTP2PeerMeanPathDelay": hmNetPTP2PeerMeanPathDelay,
       "hmNetPTP2LogAnnounceInterval": hmNetPTP2LogAnnounceInterval,
       "hmNetPTP2AnnounceReceiptTimeout": hmNetPTP2AnnounceReceiptTimeout,
       "hmNetPTP2LogSyncInterval": hmNetPTP2LogSyncInterval,
       "hmNetPTP2DelayMechanism": hmNetPTP2DelayMechanism,
       "hmNetPTP2LogPdelayReqInterval": hmNetPTP2LogPdelayReqInterval,
       "hmNetPTP2VersionNumber": hmNetPTP2VersionNumber,
       "hmNetPTP2NetworkProtocol": hmNetPTP2NetworkProtocol,
       "hmNetPTP2V1Compatibility": hmNetPTP2V1Compatibility,
       "hmNetPTP2DelayAsymmetry": hmNetPTP2DelayAsymmetry,
       "hmNetPTP2PortCapability": hmNetPTP2PortCapability,
       "hmNetPTP2VlanID": hmNetPTP2VlanID,
       "hmNetPTP2VlanPriority": hmNetPTP2VlanPriority,
       "hmNetPTP2TCGroup": hmNetPTP2TCGroup,
       "hmNetPTP2TCConfiguration": hmNetPTP2TCConfiguration,
       "hmNetPTP2TCClockIdentity": hmNetPTP2TCClockIdentity,
       "hmNetPTP2TCDelayMechanism": hmNetPTP2TCDelayMechanism,
       "hmNetPTP2TCPrimaryDomain": hmNetPTP2TCPrimaryDomain,
       "hmNetPTP2TCSyntonized": hmNetPTP2TCSyntonized,
       "hmNetPTP2TCNetworkProtocol": hmNetPTP2TCNetworkProtocol,
       "hmNetPTP2TCCurrentMaster": hmNetPTP2TCCurrentMaster,
       "hmNetPTP2TCManagement": hmNetPTP2TCManagement,
       "hmNetPTP2TCMultiDomainMode": hmNetPTP2TCMultiDomainMode,
       "hmNetPTP2TCSyncLocalClock": hmNetPTP2TCSyncLocalClock,
       "hmNetPTP2TCVlanID": hmNetPTP2TCVlanID,
       "hmNetPTP2TCVlanPriority": hmNetPTP2TCVlanPriority,
       "hmNetPTP2TCPortTable": hmNetPTP2TCPortTable,
       "hmNetPTP2TCPortEntry": hmNetPTP2TCPortEntry,
       "hmNetPTP2TCPortEnable": hmNetPTP2TCPortEnable,
       "hmNetPTP2TCLogPdelayReqInterval": hmNetPTP2TCLogPdelayReqInterval,
       "hmNetPTP2TCFaulty": hmNetPTP2TCFaulty,
       "hmNetPTP2TCPeerMeanPathDelay": hmNetPTP2TCPeerMeanPathDelay,
       "hmNetPTP2TCDelayAsymmetry": hmNetPTP2TCDelayAsymmetry,
       "hmNetSNMPGroup": hmNetSNMPGroup,
       "hmNetSNMPv1Status": hmNetSNMPv1Status,
       "hmNetSNMPv2Status": hmNetSNMPv2Status,
       "hmNetSNMPv3Status": hmNetSNMPv3Status,
       "hmNetSNMPAccessStatus": hmNetSNMPAccessStatus,
       "hmNetSNMPSynchronizeV1V3Status": hmNetSNMPSynchronizeV1V3Status,
       "hmNetSNMPPortNumber": hmNetSNMPPortNumber,
       "hmNetSNMPRadiusAuthenticate": hmNetSNMPRadiusAuthenticate,
       "hmNetSNMPv3EncryptionReadWriteStatus": hmNetSNMPv3EncryptionReadWriteStatus,
       "hmNetSNMPv3EncryptionReadOnlyStatus": hmNetSNMPv3EncryptionReadOnlyStatus,
       "hmNetGPSGroup": hmNetGPSGroup,
       "hmNetGPSIsAvailable": hmNetGPSIsAvailable,
       "hmNetGPSIsSynchronized": hmNetGPSIsSynchronized,
       "hmNetGPSMode": hmNetGPSMode,
       "hmNetGPSTimeStringFormat": hmNetGPSTimeStringFormat,
       "hmRestrictedMgtAccessGroup": hmRestrictedMgtAccessGroup,
       "hmRMAOperation": hmRMAOperation,
       "hmRMATable": hmRMATable,
       "hmRMAEntry": hmRMAEntry,
       "hmRMAIndex": hmRMAIndex,
       "hmRMARowStatus": hmRMARowStatus,
       "hmRMAIpAddr": hmRMAIpAddr,
       "hmRMANetMask": hmRMANetMask,
       "hmRMASrvHttp": hmRMASrvHttp,
       "hmRMASrvSnmp": hmRMASrvSnmp,
       "hmRMASrvTelnet": hmRMASrvTelnet,
       "hmRMASrvSsh": hmRMASrvSsh,
       "hmFSTable": hmFSTable,
       "hmFSUpdFileName": hmFSUpdFileName,
       "hmFSConfFileName": hmFSConfFileName,
       "hmFSLogFileName": hmFSLogFileName,
       "hmFSUserName": hmFSUserName,
       "hmFSTPPassword": hmFSTPPassword,
       "hmFSAction": hmFSAction,
       "hmFSActionResult": hmFSActionResult,
       "hmFSBootConfiguration": hmFSBootConfiguration,
       "hmFSRunningConfiguration": hmFSRunningConfiguration,
       "hmFSLastMessage": hmFSLastMessage,
       "hmConfigurationStatus": hmConfigurationStatus,
       "hmFSFileTable": hmFSFileTable,
       "hmFSFileEntry": hmFSFileEntry,
       "hmFSFileID": hmFSFileID,
       "hmFSFileName": hmFSFileName,
       "hmFSFileSize": hmFSFileSize,
       "hmFSFileDate": hmFSFileDate,
       "hmAutoconfigGroup": hmAutoconfigGroup,
       "hmAutoconfigAdapterStatus": hmAutoconfigAdapterStatus,
       "hmAutoconfigAdapterSerialNum": hmAutoconfigAdapterSerialNum,
       "hmConfigWatchdogGroup": hmConfigWatchdogGroup,
       "hmConfigWatchdogAdminStatus": hmConfigWatchdogAdminStatus,
       "hmConfigWatchdogOperStatus": hmConfigWatchdogOperStatus,
       "hmConfigWatchdogTimeInterval": hmConfigWatchdogTimeInterval,
       "hmConfigWatchdogTimerValue": hmConfigWatchdogTimerValue,
       "hmConfigWatchdogIPAddress": hmConfigWatchdogIPAddress,
       "hmTempTable": hmTempTable,
       "hmTemperature": hmTemperature,
       "hmTempUprLimit": hmTempUprLimit,
       "hmTempLwrLimit": hmTempLwrLimit,
       "hmNeighbourAgentTable": hmNeighbourAgentTable,
       "hmNeighbourAgentEntry": hmNeighbourAgentEntry,
       "hmNeighbourSlot": hmNeighbourSlot,
       "hmNeighbourIpAddress": hmNeighbourIpAddress,
       "hmAuthGroup": hmAuthGroup,
       "hmAuthHostTableEntriesMax": hmAuthHostTableEntriesMax,
       "hmAuthCommTableEntriesMax": hmAuthCommTableEntriesMax,
       "hmAuthCommTable": hmAuthCommTable,
       "hmAuthCommEntry": hmAuthCommEntry,
       "hmAuthCommIndex": hmAuthCommIndex,
       "hmAuthCommName": hmAuthCommName,
       "hmAuthCommPerm": hmAuthCommPerm,
       "hmAuthCommState": hmAuthCommState,
       "hmAuthHostTable": hmAuthHostTable,
       "hmAuthHostEntry": hmAuthHostEntry,
       "hmAuthHostIndex": hmAuthHostIndex,
       "hmAuthHostName": hmAuthHostName,
       "hmAuthHostCommIndex": hmAuthHostCommIndex,
       "hmAuthHostIpAddress": hmAuthHostIpAddress,
       "hmAuthHostIpMask": hmAuthHostIpMask,
       "hmAuthHostState": hmAuthHostState,
       "hmTrapGroup": hmTrapGroup,
       "hmTrapCommTableEntriesMax": hmTrapCommTableEntriesMax,
       "hmTrapDestTableEntriesMax": hmTrapDestTableEntriesMax,
       "hmTrapCommTable": hmTrapCommTable,
       "hmTrapCommEntry": hmTrapCommEntry,
       "hmTrapCommIndex": hmTrapCommIndex,
       "hmTrapCommCommIndex": hmTrapCommCommIndex,
       "hmTrapCommColdStart": hmTrapCommColdStart,
       "hmTrapCommLinkDown": hmTrapCommLinkDown,
       "hmTrapCommLinkUp": hmTrapCommLinkUp,
       "hmTrapCommAuthentication": hmTrapCommAuthentication,
       "hmTrapCommBridge": hmTrapCommBridge,
       "hmTrapCommRMON": hmTrapCommRMON,
       "hmTrapCommUsergroup": hmTrapCommUsergroup,
       "hmTrapCommDualHoming": hmTrapCommDualHoming,
       "hmTrapCommChassis": hmTrapCommChassis,
       "hmTrapCommState": hmTrapCommState,
       "hmTrapDestTable": hmTrapDestTable,
       "hmTrapDestEntry": hmTrapDestEntry,
       "hmTrapDestIndex": hmTrapDestIndex,
       "hmTrapDestName": hmTrapDestName,
       "hmTrapDestCommIndex": hmTrapDestCommIndex,
       "hmTrapDestIpAddress": hmTrapDestIpAddress,
       "hmTrapDestIpMask": hmTrapDestIpMask,
       "hmTrapDestState": hmTrapDestState,
       "hmLastAccessGroup": hmLastAccessGroup,
       "hmLastIpAddr": hmLastIpAddr,
       "hmLastPort": hmLastPort,
       "hmLastCommunity": hmLastCommunity,
       "hmLastLoginUserName": hmLastLoginUserName,
       "hmMulticast": hmMulticast,
       "hmIGMPGroup": hmIGMPGroup,
       "hmIGMPSnoop": hmIGMPSnoop,
       "hmIGMPSnoopStatus": hmIGMPSnoopStatus,
       "hmIGMPSnoopAgingTime": hmIGMPSnoopAgingTime,
       "hmIGMPSnoopUnknownMode": hmIGMPSnoopUnknownMode,
       "hmIGMPSnoopUnknownAgingTime": hmIGMPSnoopUnknownAgingTime,
       "hmIGMPSnoopUnknownLookupInterval": hmIGMPSnoopUnknownLookupInterval,
       "hmIGMPSnoopUnknownLookupResponseTime": hmIGMPSnoopUnknownLookupResponseTime,
       "hmIGMPSnoopQuerierToPortmask": hmIGMPSnoopQuerierToPortmask,
       "hmIGMPSnoopQuerierIPAddress": hmIGMPSnoopQuerierIPAddress,
       "hmIGMPSnoopQueryTable": hmIGMPSnoopQueryTable,
       "hmIGMPSnoopQueryEntry": hmIGMPSnoopQueryEntry,
       "hmIGMPSnoopQueryVlanIndex": hmIGMPSnoopQueryVlanIndex,
       "hmIGMPSnoopQueryPorts": hmIGMPSnoopQueryPorts,
       "hmIGMPSnoopFilterTable": hmIGMPSnoopFilterTable,
       "hmIGMPSnoopFilterEntry": hmIGMPSnoopFilterEntry,
       "hmIGMPSnoopFilterVlanIndex": hmIGMPSnoopFilterVlanIndex,
       "hmIGMPSnoopFilterAddress": hmIGMPSnoopFilterAddress,
       "hmIGMPSnoopFilterLearntPorts": hmIGMPSnoopFilterLearntPorts,
       "hmIGMPSnoopForwardAllTable": hmIGMPSnoopForwardAllTable,
       "hmIGMPSnoopForwardAllEntry": hmIGMPSnoopForwardAllEntry,
       "hmIGMPSnoopForwardAllVlanIndex": hmIGMPSnoopForwardAllVlanIndex,
       "hmIGMPSnoopForwardAllStaticPorts": hmIGMPSnoopForwardAllStaticPorts,
       "hmIGMPSnoopQueryStaticTable": hmIGMPSnoopQueryStaticTable,
       "hmIGMPSnoopQueryStaticEntry": hmIGMPSnoopQueryStaticEntry,
       "hmIGMPSnoopQueryStaticVlanIndex": hmIGMPSnoopQueryStaticVlanIndex,
       "hmIGMPSnoopQueryStaticPorts": hmIGMPSnoopQueryStaticPorts,
       "hmIGMPSnoopQueryStaticAutomaticPorts": hmIGMPSnoopQueryStaticAutomaticPorts,
       "hmIGMPSnoopQueryStaticAutomaticPortsEnable": hmIGMPSnoopQueryStaticAutomaticPortsEnable,
       "hmIGMPQuerierGroup": hmIGMPQuerierGroup,
       "hmIGMPQuerierStatus": hmIGMPQuerierStatus,
       "hmIGMPQuerierMode": hmIGMPQuerierMode,
       "hmIGMPQuerierTransmitInterval": hmIGMPQuerierTransmitInterval,
       "hmIGMPQuerierMaxResponseTime": hmIGMPQuerierMaxResponseTime,
       "hmIGMPQuerierProtocolVersion": hmIGMPQuerierProtocolVersion,
       "hmGMRPGroup": hmGMRPGroup,
       "hmGMRP": hmGMRP,
       "hmGmrpUnknownMode": hmGmrpUnknownMode,
       "hmRelayGroup": hmRelayGroup,
       "hmRelayOption82Status": hmRelayOption82Status,
       "hmRelayOptionRemoteIDType": hmRelayOptionRemoteIDType,
       "hmRelayOptionRemoteID": hmRelayOptionRemoteID,
       "hmRelayOptionRemoteIDValue": hmRelayOptionRemoteIDValue,
       "hmRelayServerGroup": hmRelayServerGroup,
       "hmRelayDHCPServerIpAddr": hmRelayDHCPServerIpAddr,
       "hmRelayDHCPServer2IpAddr": hmRelayDHCPServer2IpAddr,
       "hmRelayDHCPServer3IpAddr": hmRelayDHCPServer3IpAddr,
       "hmRelayDHCPServer4IpAddr": hmRelayDHCPServer4IpAddr,
       "hmRelayInterfaceTable": hmRelayInterfaceTable,
       "hmRelayInterfaceEntry": hmRelayInterfaceEntry,
       "hmRelayIfaceGroupID": hmRelayIfaceGroupID,
       "hmRelayIfaceID": hmRelayIfaceID,
       "hmRelayIfaceOption82Enable": hmRelayIfaceOption82Enable,
       "hmRelayIfaceBCRequestFwd": hmRelayIfaceBCRequestFwd,
       "hmRelayIfaceCircuitID": hmRelayIfaceCircuitID,
       "hmRelayBCPktInCnt": hmRelayBCPktInCnt,
       "hmRelayMCPktInCnt": hmRelayMCPktInCnt,
       "hmRelayPktServerRelayCnt": hmRelayPktServerRelayCnt,
       "hmRelayPktClientRelayCnt": hmRelayPktClientRelayCnt,
       "hmRelayErrCnt": hmRelayErrCnt,
       "hmRelayLastDuplicateIP": hmRelayLastDuplicateIP,
       "hmDeviceMonitoringGroup": hmDeviceMonitoringGroup,
       "hmSigConConfigTable": hmSigConConfigTable,
       "hmSigConConfigEntry": hmSigConConfigEntry,
       "hmSigConID": hmSigConID,
       "hmSigConTrapEnable": hmSigConTrapEnable,
       "hmSigConTrapCause": hmSigConTrapCause,
       "hmSigConTrapCauseIndex": hmSigConTrapCauseIndex,
       "hmSigConMode": hmSigConMode,
       "hmSigConManualActivate": hmSigConManualActivate,
       "hmSigConOperState": hmSigConOperState,
       "hmSigConSenseLinkFailure": hmSigConSenseLinkFailure,
       "hmSigConSenseControlLine": hmSigConSenseControlLine,
       "hmSigConSenseRedNotGuaranteed": hmSigConSenseRedNotGuaranteed,
       "hmSigConSensePS1State": hmSigConSensePS1State,
       "hmSigConSensePS2State": hmSigConSensePS2State,
       "hmSigConSenseTemperature": hmSigConSenseTemperature,
       "hmSigConSenseModuleRemoval": hmSigConSenseModuleRemoval,
       "hmSigConSenseACARemoval": hmSigConSenseACARemoval,
       "hmSigConSensePS3State": hmSigConSensePS3State,
       "hmSigConSensePS4State": hmSigConSensePS4State,
       "hmSigConSenseFan1State": hmSigConSenseFan1State,
       "hmSigConSensePS5State": hmSigConSensePS5State,
       "hmSigConSensePS6State": hmSigConSensePS6State,
       "hmSigConSensePS7State": hmSigConSensePS7State,
       "hmSigConSensePS8State": hmSigConSensePS8State,
       "hmSigConSenseACANotInSync": hmSigConSenseACANotInSync,
       "hmSigConLinkTable": hmSigConLinkTable,
       "hmSigConLinkEntry": hmSigConLinkEntry,
       "hmSigConLinkID": hmSigConLinkID,
       "hmSigConLinkAlarm": hmSigConLinkAlarm,
       "hmDevMonConfigTable": hmDevMonConfigTable,
       "hmDevMonConfigEntry": hmDevMonConfigEntry,
       "hmDevMonID": hmDevMonID,
       "hmDevMonTrapEnable": hmDevMonTrapEnable,
       "hmDevMonTrapCause": hmDevMonTrapCause,
       "hmDevMonTrapCauseIndex": hmDevMonTrapCauseIndex,
       "hmDevMonSwitchState": hmDevMonSwitchState,
       "hmDevMonSenseLinkFailure": hmDevMonSenseLinkFailure,
       "hmDevMonSenseControlLine": hmDevMonSenseControlLine,
       "hmDevMonSenseRedNotGuaranteed": hmDevMonSenseRedNotGuaranteed,
       "hmDevMonSensePS1State": hmDevMonSensePS1State,
       "hmDevMonSensePS2State": hmDevMonSensePS2State,
       "hmDevMonSenseTemperature": hmDevMonSenseTemperature,
       "hmDevMonSenseModuleRemoval": hmDevMonSenseModuleRemoval,
       "hmDevMonSenseACARemoval": hmDevMonSenseACARemoval,
       "hmDevMonSensePS3State": hmDevMonSensePS3State,
       "hmDevMonSensePS4State": hmDevMonSensePS4State,
       "hmDevMonSenseFan1State": hmDevMonSenseFan1State,
       "hmDevMonSensePS5State": hmDevMonSensePS5State,
       "hmDevMonSensePS6State": hmDevMonSensePS6State,
       "hmDevMonSensePS7State": hmDevMonSensePS7State,
       "hmDevMonSensePS8State": hmDevMonSensePS8State,
       "hmDevMonSenseACANotInSync": hmDevMonSenseACANotInSync,
       "hmAgentSnmpConfigGroup": hmAgentSnmpConfigGroup,
       "hmAgentSnmpCommunityCreate": hmAgentSnmpCommunityCreate,
       "hmAgentSnmpCommunityConfigTable": hmAgentSnmpCommunityConfigTable,
       "hmAgentSnmpCommunityConfigEntry": hmAgentSnmpCommunityConfigEntry,
       "hmAgentSnmpCommunityIndex": hmAgentSnmpCommunityIndex,
       "hmAgentSnmpCommunityName": hmAgentSnmpCommunityName,
       "hmAgentSnmpCommunityIPAddress": hmAgentSnmpCommunityIPAddress,
       "hmAgentSnmpCommunityIPMask": hmAgentSnmpCommunityIPMask,
       "hmAgentSnmpCommunityAccessMode": hmAgentSnmpCommunityAccessMode,
       "hmAgentSnmpCommunityStatus": hmAgentSnmpCommunityStatus,
       "hmAgentSnmpTrapReceiverCreate": hmAgentSnmpTrapReceiverCreate,
       "hmAgentSnmpTrapReceiverConfigTable": hmAgentSnmpTrapReceiverConfigTable,
       "hmAgentSnmpTrapReceiverConfigEntry": hmAgentSnmpTrapReceiverConfigEntry,
       "hmAgentSnmpTrapReceiverIndex": hmAgentSnmpTrapReceiverIndex,
       "hmAgentSnmpTrapReceiverCommunityName": hmAgentSnmpTrapReceiverCommunityName,
       "hmAgentSnmpTrapReceiverIPAddress": hmAgentSnmpTrapReceiverIPAddress,
       "hmAgentSnmpTrapReceiverStatus": hmAgentSnmpTrapReceiverStatus,
       "hmAgentSnmpTrapFlagsConfigGroup": hmAgentSnmpTrapFlagsConfigGroup,
       "hmAgentSnmpAuthenticationTrapFlag": hmAgentSnmpAuthenticationTrapFlag,
       "hmAgentSnmpLinkUpDownTrapFlag": hmAgentSnmpLinkUpDownTrapFlag,
       "hmAgentSnmpMultipleUsersTrapFlag": hmAgentSnmpMultipleUsersTrapFlag,
       "hmAgentSnmpSpanningTreeTrapFlag": hmAgentSnmpSpanningTreeTrapFlag,
       "hmAgentSnmpBroadcastStormTrapFlag": hmAgentSnmpBroadcastStormTrapFlag,
       "hmAgentSnmpChassisTrapFlag": hmAgentSnmpChassisTrapFlag,
       "hmAgentSnmpL2RedundancyTrapFlag": hmAgentSnmpL2RedundancyTrapFlag,
       "hmAgentSnmpPortSecurityTrapFlag": hmAgentSnmpPortSecurityTrapFlag,
       "hmAgentSnmpCommunityMaxEntries": hmAgentSnmpCommunityMaxEntries,
       "hmAgentSnmpTrapReceiverMaxEntries": hmAgentSnmpTrapReceiverMaxEntries,
       "hmAgentSnmpLoggingGroup": hmAgentSnmpLoggingGroup,
       "hmAgentSnmpLogGetRequest": hmAgentSnmpLogGetRequest,
       "hmAgentSnmpLogSetRequest": hmAgentSnmpLogSetRequest,
       "hmAgentSnmpLogGetSeverity": hmAgentSnmpLogGetSeverity,
       "hmAgentSnmpLogSetSeverity": hmAgentSnmpLogSetSeverity,
       "hmPOEGroup": hmPOEGroup,
       "hmPOEGlobalGroup": hmPOEGlobalGroup,
       "hmPOEStatus": hmPOEStatus,
       "hmPOEScanning": hmPOEScanning,
       "hmPOEReservedPower": hmPOEReservedPower,
       "hmPOEFastStartup": hmPOEFastStartup,
       "hmPOEPortTable": hmPOEPortTable,
       "hmPOEPortEntry": hmPOEPortEntry,
       "hmPOEPortIndex": hmPOEPortIndex,
       "hmPOEPortConsumptionPower": hmPOEPortConsumptionPower,
       "hmPOEModuleTable": hmPOEModuleTable,
       "hmPOEModuleEntry": hmPOEModuleEntry,
       "hmPOEModuleIndex": hmPOEModuleIndex,
       "hmPOEModulePower": hmPOEModulePower,
       "hmPOEModuleMaximumPower": hmPOEModuleMaximumPower,
       "hmPOEModuleReservedPower": hmPOEModuleReservedPower,
       "hmPOEModuleDeliveredPower": hmPOEModuleDeliveredPower,
       "hmPOEModuleUsageThreshold": hmPOEModuleUsageThreshold,
       "hmPOEModuleNotificationControlEnable": hmPOEModuleNotificationControlEnable,
       "hmSwitchResources": hmSwitchResources,
       "hmEnableMeasurement": hmEnableMeasurement,
       "hmCpuResources": hmCpuResources,
       "hmCpuUtilization": hmCpuUtilization,
       "hmCpuAverageUtilization": hmCpuAverageUtilization,
       "hmCpuRunningProcesses": hmCpuRunningProcesses,
       "hmCpuMaxRunningProcesses": hmCpuMaxRunningProcesses,
       "hmMemoryResources": hmMemoryResources,
       "hmMemoryAllocated": hmMemoryAllocated,
       "hmMemoryFree": hmMemoryFree,
       "hmMemoryAllocatedAverage": hmMemoryAllocatedAverage,
       "hmMemoryFreeAverage": hmMemoryFreeAverage,
       "hmNetworkResources": hmNetworkResources,
       "hmNetworkCpuIfUtilization": hmNetworkCpuIfUtilization,
       "hmNetworkCpuIfAverageUtilization": hmNetworkCpuIfAverageUtilization,
       "hmIndustrialEthernetProtocols": hmIndustrialEthernetProtocols,
       "hmProfinetIOConfigGroup": hmProfinetIOConfigGroup,
       "hmPNIOAdminStatus": hmPNIOAdminStatus,
       "hmPNIODeviceID": hmPNIODeviceID,
       "hmPNIOModuleIdentNumber": hmPNIOModuleIdentNumber,
       "hmPNIOOrderID": hmPNIOOrderID,
       "hmPNIODeviceTypeDetails": hmPNIODeviceTypeDetails,
       "hmPNIOSoftwareRelease": hmPNIOSoftwareRelease,
       "hmPNIOHardwareRelease": hmPNIOHardwareRelease,
       "hmPNIOOrderID9th": hmPNIOOrderID9th,
       "hmPNIODcpModeTable": hmPNIODcpModeTable,
       "hmPNIODcpModeEntry": hmPNIODcpModeEntry,
       "hmPNIODcpModePortID": hmPNIODcpModePortID,
       "hmPNIODcpMode": hmPNIODcpMode,
       "hmPNIONameOfStation": hmPNIONameOfStation,
       "hmProfinetIOStatisticsGroup": hmProfinetIOStatisticsGroup,
       "hmEthernetIPConfigGroup": hmEthernetIPConfigGroup,
       "hmEtherNetIPAdminStatus": hmEtherNetIPAdminStatus,
       "hmEtherNetIPErrorCode": hmEtherNetIPErrorCode,
       "hmEtherNetIPProductCode": hmEtherNetIPProductCode,
       "hmEtherNetIPRevisionMajor": hmEtherNetIPRevisionMajor,
       "hmEtherNetIPRevisionMinor": hmEtherNetIPRevisionMinor,
       "hmEtherNetIPProductName": hmEtherNetIPProductName,
       "hmEtherNetIPCatalogName": hmEtherNetIPCatalogName,
       "hmEthernetIPStatisticsGroup": hmEthernetIPStatisticsGroup,
       "hmEtherNetIPConnEstablished": hmEtherNetIPConnEstablished,
       "hmEtherNetIPConnTimeouts": hmEtherNetIPConnTimeouts,
       "hmEtherNetIPVendorObjRequests": hmEtherNetIPVendorObjRequests,
       "hmAgentLoginGroup": hmAgentLoginGroup,
       "hmAgentLoginBanner": hmAgentLoginBanner,
       "hmPortMonitorGroup": hmPortMonitorGroup,
       "hmPortMonitorAdminMode": hmPortMonitorAdminMode,
       "hmPortMonitorIntfTable": hmPortMonitorIntfTable,
       "hmPortMonitorIntfEntry": hmPortMonitorIntfEntry,
       "hmPortMonitorIntfMode": hmPortMonitorIntfMode,
       "hmPortMonitorIntfReset": hmPortMonitorIntfReset,
       "hmPortMonitorIntfAction": hmPortMonitorIntfAction,
       "hmPortMonitorConditionGroup": hmPortMonitorConditionGroup,
       "hmPortMonitorConditionTable": hmPortMonitorConditionTable,
       "hmPortMonitorConditionIntfEntry": hmPortMonitorConditionIntfEntry,
       "hmPortMonitorConditionLinkFlapMode": hmPortMonitorConditionLinkFlapMode,
       "hmPortMonitorConditionCrcFragmentsMode": hmPortMonitorConditionCrcFragmentsMode,
       "hmPortMonitorConditionField": hmPortMonitorConditionField,
       "hmPortMonitorConditionLinkFlapGroup": hmPortMonitorConditionLinkFlapGroup,
       "hmPortMonitorConditionLinkFlapInterval": hmPortMonitorConditionLinkFlapInterval,
       "hmPortMonitorConditionLinkFlapCount": hmPortMonitorConditionLinkFlapCount,
       "hmPortMonitorConditionLinkFlapIntfTable": hmPortMonitorConditionLinkFlapIntfTable,
       "hmPortMonitorConditionLinkFlapIntfEntry": hmPortMonitorConditionLinkFlapIntfEntry,
       "hmPortMonitorConditionLinkFlapCountInterval": hmPortMonitorConditionLinkFlapCountInterval,
       "hmPortMonitorConditionLinkFlapCountTotal": hmPortMonitorConditionLinkFlapCountTotal,
       "hmPortMonitorConditionCrcFragmentsGroup": hmPortMonitorConditionCrcFragmentsGroup,
       "hmPortMonitorConditionCrcFragmentsInterval": hmPortMonitorConditionCrcFragmentsInterval,
       "hmPortMonitorConditionCrcFragmentsCount": hmPortMonitorConditionCrcFragmentsCount,
       "hmPortMonitorConditionCrcFragmentsIntfTable": hmPortMonitorConditionCrcFragmentsIntfTable,
       "hmPortMonitorConditionCrcFragmentsIntfEntry": hmPortMonitorConditionCrcFragmentsIntfEntry,
       "hmPortMonitorConditionCrcFragmentsCountInterval": hmPortMonitorConditionCrcFragmentsCountInterval,
       "hmPortMonitorConditionCrcFragmentsCountTotal": hmPortMonitorConditionCrcFragmentsCountTotal,
       "hmProducts": hmProducts,
       "rs2": rs2,
       "mach3000": mach3000,
       "ms2108-2": ms2108_2,
       "ms3124-4": ms3124_4,
       "rs2-16": rs2_16,
       "rs2-4r": rs2_4r,
       "ms4128-5": ms4128_5,
       "eagle": eagle,
       "rr-epl": rr_epl,
       "eagle-mguard": eagle_mguard,
       "eagle20": eagle20,
       "ms20": ms20,
       "ms30": ms30,
       "rs20": rs20,
       "rs30": rs30,
       "rsb20": rsb20,
       "osb20": osb20,
       "mach4002-48-4G": mach4002_48_4G,
       "octopus": octopus,
       "mach4002-24G": mach4002_24G,
       "mach4002-24G-3X": mach4002_24G_3X,
       "mach4002-48G": mach4002_48G,
       "mach4002-48G-3X": mach4002_48G_3X,
       "ruggedswitch": ruggedswitch,
       "railswitchrugged": railswitchrugged,
       "mach100": mach100,
       "octopus-os": octopus_os,
       "mach100ge": mach100ge,
       "mach1000ge": mach1000ge,
       "eem1": eem1}
)
