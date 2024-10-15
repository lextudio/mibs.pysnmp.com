# SNMP MIB module (Wellfleet-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:19 2024
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

(wfHardwareConfig,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfHardwareConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfHwBase_ObjectIdentity = ObjectIdentity
wfHwBase = _WfHwBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1)
)


class _WfHwBpIdOpt_Type(Integer32):
    """Custom type wfHwBpIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              16,
              32,
              34,
              36,
              5000,
              16640,
              16896,
              17152,
              20480,
              20736,
              20992,
              24576,
              26368)
        )
    )
    namedValues = NamedValues(
        *(("acecn", 3),
          ("acefn", 1),
          ("aceln", 2),
          ("afn", 4),
          ("an", 16),
          ("arn", 32),
          ("asn", 20480),
          ("asnbcable", 20992),
          ("asnzcable", 20736),
          ("fbr4slot", 34),
          ("frecn", 16896),
          ("freln", 16640),
          ("frerbln", 17152),
          ("in", 5),
          ("lite", 36),
          ("sn", 24576),
          ("sys5000", 5000),
          ("v15k", 26368))
    )


_WfHwBpIdOpt_Type.__name__ = "Integer32"
_WfHwBpIdOpt_Object = MibScalar
wfHwBpIdOpt = _WfHwBpIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 1),
    _WfHwBpIdOpt_Type()
)
wfHwBpIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBpIdOpt.setStatus("mandatory")
_WfHwBpRev_Type = OctetString
_WfHwBpRev_Object = MibScalar
wfHwBpRev = _WfHwBpRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 2),
    _WfHwBpRev_Type()
)
wfHwBpRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBpRev.setStatus("mandatory")
_WfHwBpSerialNumber_Type = OctetString
_WfHwBpSerialNumber_Object = MibScalar
wfHwBpSerialNumber = _WfHwBpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 3),
    _WfHwBpSerialNumber_Type()
)
wfHwBpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBpSerialNumber.setStatus("mandatory")


class _WfBCNPwrSupply1_Type(Integer32):
    """Custom type wfBCNPwrSupply1 based on Integer32"""
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
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply1_Type.__name__ = "Integer32"
_WfBCNPwrSupply1_Object = MibScalar
wfBCNPwrSupply1 = _WfBCNPwrSupply1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 4),
    _WfBCNPwrSupply1_Type()
)
wfBCNPwrSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply1.setStatus("mandatory")


class _WfBCNPwrSupply2_Type(Integer32):
    """Custom type wfBCNPwrSupply2 based on Integer32"""
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
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply2_Type.__name__ = "Integer32"
_WfBCNPwrSupply2_Object = MibScalar
wfBCNPwrSupply2 = _WfBCNPwrSupply2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 5),
    _WfBCNPwrSupply2_Type()
)
wfBCNPwrSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply2.setStatus("mandatory")


class _WfBCNPwrSupply3_Type(Integer32):
    """Custom type wfBCNPwrSupply3 based on Integer32"""
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
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply3_Type.__name__ = "Integer32"
_WfBCNPwrSupply3_Object = MibScalar
wfBCNPwrSupply3 = _WfBCNPwrSupply3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 6),
    _WfBCNPwrSupply3_Type()
)
wfBCNPwrSupply3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply3.setStatus("mandatory")


class _WfBCNPwrSupply4_Type(Integer32):
    """Custom type wfBCNPwrSupply4 based on Integer32"""
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
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNPwrSupply4_Type.__name__ = "Integer32"
_WfBCNPwrSupply4_Object = MibScalar
wfBCNPwrSupply4 = _WfBCNPwrSupply4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 7),
    _WfBCNPwrSupply4_Type()
)
wfBCNPwrSupply4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNPwrSupply4.setStatus("mandatory")


class _WfBCNFanStatus_Type(Integer32):
    """Custom type wfBCNFanStatus based on Integer32"""
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
        *(("fail", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNFanStatus_Type.__name__ = "Integer32"
_WfBCNFanStatus_Object = MibScalar
wfBCNFanStatus = _WfBCNFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 8),
    _WfBCNFanStatus_Type()
)
wfBCNFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNFanStatus.setStatus("mandatory")


class _WfBCNTemperature_Type(Integer32):
    """Custom type wfBCNTemperature based on Integer32"""
    defaultValue = 3

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
        *(("caution", 2),
          ("fail", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNTemperature_Type.__name__ = "Integer32"
_WfBCNTemperature_Object = MibScalar
wfBCNTemperature = _WfBCNTemperature_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 9),
    _WfBCNTemperature_Type()
)
wfBCNTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNTemperature.setStatus("mandatory")


class _WfBCNTemperature2_Type(Integer32):
    """Custom type wfBCNTemperature2 based on Integer32"""
    defaultValue = 3

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
        *(("caution", 2),
          ("fail", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfBCNTemperature2_Type.__name__ = "Integer32"
_WfBCNTemperature2_Object = MibScalar
wfBCNTemperature2 = _WfBCNTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 10),
    _WfBCNTemperature2_Type()
)
wfBCNTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBCNTemperature2.setStatus("mandatory")


class _WfFanSpeed_Type(Integer32):
    """Custom type wfFanSpeed based on Integer32"""
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
        *(("high", 2),
          ("low", 1),
          ("notpresent", 3))
    )


_WfFanSpeed_Type.__name__ = "Integer32"
_WfFanSpeed_Object = MibScalar
wfFanSpeed = _WfFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 1, 11),
    _WfFanSpeed_Type()
)
wfFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFanSpeed.setStatus("mandatory")
_WfHwTable_Object = MibTable
wfHwTable = _WfHwTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wfHwTable.setStatus("mandatory")
_WfHwEntry_Object = MibTableRow
wfHwEntry = _WfHwEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1)
)
wfHwEntry.setIndexNames(
    (0, "Wellfleet-HARDWARE-MIB", "wfHwSlot"),
)
if mibBuilder.loadTexts:
    wfHwEntry.setStatus("mandatory")
_WfHwSlot_Type = Integer32
_WfHwSlot_Object = MibTableColumn
wfHwSlot = _WfHwSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 1),
    _WfHwSlot_Type()
)
wfHwSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSlot.setStatus("mandatory")


class _WfHwModIdOpt_Type(Integer32):
    """Custom type wfHwModIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              16,
              17,
              24,
              32,
              33,
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
              56,
              57,
              58,
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
              80,
              81,
              88,
              89,
              104,
              112,
              113,
              114,
              116,
              117,
              118,
              119,
              120,
              132,
              156,
              160,
              161,
              162,
              164,
              165,
              168,
              169,
              176,
              184,
              185,
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
              208,
              216,
              217,
              224,
              225,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              256,
              508,
              509,
              510,
              511,
              512,
              513,
              767,
              777,
              778,
              787,
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
              4096,
              4097,
              4098,
              4099,
              4352,
              4353,
              4354,
              4608,
              4609,
              4610,
              4864,
              5120,
              5121,
              5376,
              5377,
              5378,
              6144,
              6145,
              6400,
              6401,
              8448,
              8500,
              24848,
              24849,
              24864,
              24880,
              24896,
              24912,
              524288,
              524544,
              1048746,
              1048747,
              1048762,
              1048763,
              1048798,
              1048799,
              1048806,
              1048807,
              1048810,
              1048811,
              1048814,
              1048815,
              1048822,
              1048823,
              1048826,
              1048827,
              1048830,
              1048831,
              1048832,
              1048833,
              1048834,
              1048835,
              1048836,
              1048837,
              1048863,
              1048864,
              1048865,
              1048866,
              1048867,
              1048868,
              1048869,
              1048895,
              1048896,
              1048897,
              1048898,
              1048899,
              1048900,
              1048901,
              1048927,
              1048928,
              1048929,
              1048930,
              1048931,
              1048932,
              1048933,
              1048959,
              1048960,
              1048961,
              1048962,
              1048963,
              1048964,
              1048965,
              1048991,
              1049089,
              1049090,
              1049091,
              1049092,
              1049093,
              1049094,
              1049095,
              1049119,
              1049217,
              1049218,
              1049219,
              1049220,
              1049221,
              1049222,
              1049223,
              1049247,
              1049344,
              1049376)
        )
    )
    namedValues = NamedValues(
        *(("andeds", 1033),
          ("andedsg", 1050),
          ("andedsgx", 1053),
          ("andedsh", 1035),
          ("andedst", 1034),
          ("andedstx", 1060),
          ("andedsx", 1057),
          ("andst", 1037),
          ("andstc", 1091),
          ("andstcx", 1096),
          ("andstf", 1102),
          ("andstf2", 1103),
          ("andstf2x", 1110),
          ("andstfx", 1115),
          ("andsti", 1038),
          ("andsti2", 1046),
          ("andsti2x", 1061),
          ("andstj", 1121),
          ("andstj2", 1122),
          ("andstj2x", 1129),
          ("andstjx", 1134),
          ("andstu", 1068),
          ("andstu2", 1069),
          ("andstu2x", 1076),
          ("andstv", 1081),
          ("andstvx", 1086),
          ("andstx", 1036),
          ("ansdsedst", 1041),
          ("ansdsedstx", 1042),
          ("ansedi", 1064),
          ("anseds", 1024),
          ("ansedsc", 1090),
          ("ansedscx", 1095),
          ("ansedsf", 1100),
          ("ansedsf2", 1101),
          ("ansedsf2x", 1109),
          ("ansedsfx", 1114),
          ("ansedsg", 1047),
          ("ansedsgc", 1094),
          ("ansedsgcx", 1099),
          ("ansedsgf", 1108),
          ("ansedsgf2x", 1113),
          ("ansedsgfx", 1118),
          ("ansedsgi", 1051),
          ("ansedsgix", 1054),
          ("ansedsgj", 1127),
          ("ansedsgj2x", 1132),
          ("ansedsgjx", 1137),
          ("ansedsgu", 1074),
          ("ansedsgu2x", 1079),
          ("ansedsgv", 1084),
          ("ansedsgvx", 1089),
          ("ansedsgx", 1048),
          ("ansedsh", 1026),
          ("ansedshc", 1093),
          ("ansedshcx", 1098),
          ("ansedshf", 1106),
          ("ansedshf2", 1107),
          ("ansedshf2x", 1112),
          ("ansedshfx", 1117),
          ("ansedshi", 1029),
          ("ansedshi2", 1045),
          ("ansedshj", 1125),
          ("ansedshj2", 1126),
          ("ansedshj2x", 1131),
          ("ansedshjx", 1136),
          ("ansedshu", 1072),
          ("ansedshu2", 1073),
          ("ansedshu2x", 1078),
          ("ansedshv", 1083),
          ("ansedshvx", 1088),
          ("ansedsi", 1027),
          ("ansedsi2", 1043),
          ("ansedsi2x", 1062),
          ("ansedsj", 1119),
          ("ansedsj2", 1120),
          ("ansedsj2x", 1128),
          ("ansedsjx", 1133),
          ("ansedst", 1025),
          ("ansedstc", 1092),
          ("ansedstcx", 1097),
          ("ansedstf", 1104),
          ("ansedstf2", 1105),
          ("ansedstf2x", 1111),
          ("ansedstfx", 1116),
          ("ansedsti", 1028),
          ("ansedsti2", 1044),
          ("ansedsti2x", 1063),
          ("ansedstj", 1123),
          ("ansedstj2", 1124),
          ("ansedstj2x", 1130),
          ("ansedstjx", 1135),
          ("ansedstu", 1070),
          ("ansedstu2", 1071),
          ("ansedstu2x", 1077),
          ("ansedstv", 1082),
          ("ansedstvx", 1087),
          ("ansedstx", 1058),
          ("ansedsu", 1066),
          ("ansedsu2", 1067),
          ("ansedsu2x", 1075),
          ("ansedsv", 1080),
          ("ansedsvx", 1085),
          ("ansedsx", 1055),
          ("ansets", 1030),
          ("ansetsg", 1049),
          ("ansetsgx", 1052),
          ("ansetsh", 1032),
          ("ansetst", 1031),
          ("ansetstx", 1059),
          ("ansetsx", 1056),
          ("antst", 1039),
          ("antstx", 1040),
          ("arm", 24849),
          ("arn", 767),
          ("asn", 511),
          ("atm5000ah", 524288),
          ("atm5000bh", 524544),
          ("atmalc", 4096),
          ("atmalcsonetmm", 4098),
          ("atmalcsonetsm", 4099),
          ("atmalctaxi100", 4097),
          ("atmcds3", 5120),
          ("atmce3", 5121),
          ("atmcoc3mm", 4608),
          ("atmcoc3sm", 4609),
          ("atmcoc3utp5", 4610),
          ("atmoc12", 24880),
          ("chipcomdsync", 1049221),
          ("chipcomenet", 1049217),
          ("chipcomfddi", 1049218),
          ("chipcomfddis", 1049223),
          ("chipcomfdsync", 1049093),
          ("chipcomfenet", 1049089),
          ("chipcomffddi", 1049090),
          ("chipcomffddis", 1049095),
          ("chipcomfisdn", 1049094),
          ("chipcomfonly", 1049119),
          ("chipcomftok", 1049091),
          ("chipcomftokf", 1049092),
          ("chipcomisdn", 1049222),
          ("chipcomonly", 1049247),
          ("chipcomtok", 1049219),
          ("chipcomtokf", 1049220),
          ("cmcfddi", 88),
          ("comp", 4353),
          ("comp128", 4354),
          ("de100", 4864),
          ("def", 165),
          ("denf", 161),
          ("dhssi", 224),
          ("dmcoc3", 24864),
          ("dsde1", 112),
          ("dsde10bt", 120),
          ("dsde1a", 113),
          ("dsde2", 156),
          ("dse1", 32),
          ("dse1a", 33),
          ("dse2", 116),
          ("dse2a", 117),
          ("dst4", 42),
          ("dst416", 40),
          ("dt", 104),
          ("dtok", 176),
          ("e1", 61),
          ("e1n", 68),
          ("enet", 114),
          ("enet1", 1),
          ("enet2", 8),
          ("enet3", 132),
          ("enet3atm", 1048832),
          ("enet3datm", 1048960),
          ("enet3denet", 1048961),
          ("enet3dfddi", 1048962),
          ("enet3donly", 1048991),
          ("enet3dsync", 1048965),
          ("enet3dtok", 1048963),
          ("enet3dtokf", 1048964),
          ("enet3enet", 1048833),
          ("enet3fddi", 1048834),
          ("enet3only", 1048863),
          ("enet3sync", 1048837),
          ("enet3tok", 1048835),
          ("enet3tokf", 1048836),
          ("esaf", 236),
          ("esafde", 239),
          ("esafdenf", 235),
          ("esafdse", 237),
          ("esafdsenf", 233),
          ("esafnf", 232),
          ("esafsse", 238),
          ("esafssenf", 234),
          ("fbr2pmccarrier", 778),
          ("fbrcpu", 777),
          ("fddiatm", 1048864),
          ("fddienet", 1048865),
          ("fddifddi", 1048866),
          ("fddionly", 1048895),
          ("fddisync", 1048869),
          ("fdditok", 1048867),
          ("fdditokf", 1048868),
          ("floppy", 48),
          ("fmdse", 202),
          ("fmdset", 200),
          ("fmdst", 201),
          ("fmsse", 204),
          ("fmsst", 203),
          ("fnsdsdt", 216),
          ("fnsdse", 208),
          ("fnsdst", 217),
          ("fntsenet", 1049344),
          ("fntstok", 1049376),
          ("fvoip", 8500),
          ("gigenet", 6400),
          ("gigenetlx", 6401),
          ("hds3", 24848),
          ("iphfddi", 89),
          ("lite", 787),
          ("m5380", 508),
          ("m5580", 509),
          ("m5780", 510),
          ("m5782", 512),
          ("mce1", 184),
          ("mce1ii120", 190),
          ("mce1ii75", 188),
          ("mct1", 168),
          ("necfloppy", 49),
          ("oldqenf", 160),
          ("osync", 4352),
          ("qe", 1048799),
          ("qecddi1stp", 1048811),
          ("qecddi1stphwf", 1048810),
          ("qecddi1utp", 1048747),
          ("qecddi1utphwf", 1048746),
          ("qecddi2stp", 1048827),
          ("qecddi2stphwf", 1048826),
          ("qecddi2utp", 1048763),
          ("qecddi2utphwf", 1048762),
          ("qef", 164),
          ("qefddi1m", 1048815),
          ("qefddi1mhwf", 1048814),
          ("qefddi1s", 1048807),
          ("qefddi1shwf", 1048806),
          ("qefddi2m", 1048831),
          ("qefddi2mhwf", 1048830),
          ("qefddi2s", 1048823),
          ("qefddi2shwf", 1048822),
          ("qehwf", 1048798),
          ("qenf", 162),
          ("qmct1db15", 5377),
          ("qmct1ds0a", 5378),
          ("qmct1rj48", 5376),
          ("qtok", 256),
          ("se1", 63),
          ("se1n", 69),
          ("shssi", 225),
          ("smce1", 185),
          ("smce1ii120", 191),
          ("smce1ii75", 189),
          ("smct1", 169),
          ("sn", 513),
          ("sqe100", 6144),
          ("sqe100fx", 6145),
          ("srml", 8448),
          ("sse", 118),
          ("ssea", 119),
          ("sspcons", 24896),
          ("sspenet", 24912),
          ("sst4", 46),
          ("sst416", 44),
          ("sst416a", 41),
          ("sst4a", 43),
          ("st1", 58),
          ("st156k", 62),
          ("st156kn", 67),
          ("st1n", 65),
          ("stok4", 47),
          ("stok416", 45),
          ("sync", 80),
          ("sync1", 16),
          ("sync1a", 17),
          ("sync2a", 81),
          ("t11", 24),
          ("t12", 56),
          ("t12a", 57),
          ("t12n", 64),
          ("t156k", 60),
          ("t156kn", 66),
          ("tok3atm", 1048896),
          ("tok3enet", 1048897),
          ("tok3fddi", 1048898),
          ("tok3only", 1048927),
          ("tok3sync", 1048901),
          ("tok3tok", 1048899),
          ("tok3tokf", 1048900),
          ("tokf3atm", 1048928),
          ("tokf3enet", 1048929),
          ("tokf3fddi", 1048930),
          ("tokf3only", 1048959),
          ("tokf3sync", 1048933),
          ("tokf3tok", 1048931),
          ("tokf3tokf", 1048932),
          ("wffddi1m", 193),
          ("wffddi1mf", 197),
          ("wffddi1s", 195),
          ("wffddi1sf", 199),
          ("wffddi2m", 192),
          ("wffddi2mf", 196),
          ("wffddi2s", 194),
          ("wffddi2sf", 198))
    )


_WfHwModIdOpt_Type.__name__ = "Integer32"
_WfHwModIdOpt_Object = MibTableColumn
wfHwModIdOpt = _WfHwModIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 2),
    _WfHwModIdOpt_Type()
)
wfHwModIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModIdOpt.setStatus("mandatory")
_WfHwModRev_Type = OctetString
_WfHwModRev_Object = MibTableColumn
wfHwModRev = _WfHwModRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 3),
    _WfHwModRev_Type()
)
wfHwModRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModRev.setStatus("mandatory")
_WfHwModSerialNumber_Type = OctetString
_WfHwModSerialNumber_Object = MibTableColumn
wfHwModSerialNumber = _WfHwModSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 4),
    _WfHwModSerialNumber_Type()
)
wfHwModSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModSerialNumber.setStatus("mandatory")


class _WfHwMotherBdIdOpt_Type(Integer32):
    """Custom type wfHwMotherBdIdOpt based on Integer32"""
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
              16,
              32,
              36,
              64,
              256,
              768,
              769,
              1024,
              1025,
              1280,
              1536,
              1792,
              2561,
              5632,
              5633,
              6656,
              8704,
              25088,
              25344,
              25600,
              25856)
        )
    )
    namedValues = NamedValues(
        *(("ace12", 2),
          ("ace25", 3),
          ("ace32", 4),
          ("afn", 5),
          ("an", 16),
          ("are", 1280),
          ("are5000", 1536),
          ("arn", 32),
          ("asn", 1024),
          ("asn2", 1025),
          ("asn5000", 1792),
          ("atp", 25600),
          ("cap", 25856),
          ("fbr", 64),
          ("fre", 256),
          ("fre2", 768),
          ("fre2060e", 5633),
          ("fre2060epci", 5632),
          ("fre4", 6656),
          ("ifp", 25344),
          ("in", 6),
          ("lite", 36),
          ("o60", 769),
          ("sn060", 2561),
          ("srmf", 8704),
          ("ssp", 25088),
          ("sysctrl", 1),
          ("sysctrl2", 7))
    )


_WfHwMotherBdIdOpt_Type.__name__ = "Integer32"
_WfHwMotherBdIdOpt_Object = MibTableColumn
wfHwMotherBdIdOpt = _WfHwMotherBdIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 5),
    _WfHwMotherBdIdOpt_Type()
)
wfHwMotherBdIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwMotherBdIdOpt.setStatus("mandatory")
_WfHwMotherBdRev_Type = OctetString
_WfHwMotherBdRev_Object = MibTableColumn
wfHwMotherBdRev = _WfHwMotherBdRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 6),
    _WfHwMotherBdRev_Type()
)
wfHwMotherBdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwMotherBdRev.setStatus("mandatory")
_WfHwMotherBdSerialNumber_Type = OctetString
_WfHwMotherBdSerialNumber_Object = MibTableColumn
wfHwMotherBdSerialNumber = _WfHwMotherBdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 7),
    _WfHwMotherBdSerialNumber_Type()
)
wfHwMotherBdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwMotherBdSerialNumber.setStatus("mandatory")


class _WfHwDaughterBdIdOpt_Type(Integer32):
    """Custom type wfHwDaughterBdIdOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              4352,
              4608,
              5888,
              5889,
              5890,
              5891,
              8752,
              25345,
              25857)
        )
    )
    namedValues = NamedValues(
        *(("ace68020mhz12", 2),
          ("ace68020mhz25", 3),
          ("ace68030mhz32", 4),
          ("arnv34", 8752),
          ("cap3m13dtr", 25857),
          ("fre68040mhz25", 4352),
          ("fre68040mhz33", 4608),
          ("hwcomp128", 5889),
          ("hwcomp128pci", 5888),
          ("hwcomp256", 5891),
          ("hwcomp256pci", 5890),
          ("ifprspdtr", 25345),
          ("sysctrl", 1))
    )


_WfHwDaughterBdIdOpt_Type.__name__ = "Integer32"
_WfHwDaughterBdIdOpt_Object = MibTableColumn
wfHwDaughterBdIdOpt = _WfHwDaughterBdIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 8),
    _WfHwDaughterBdIdOpt_Type()
)
wfHwDaughterBdIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDaughterBdIdOpt.setStatus("mandatory")
_WfHwDaughterBdRev_Type = OctetString
_WfHwDaughterBdRev_Object = MibTableColumn
wfHwDaughterBdRev = _WfHwDaughterBdRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 9),
    _WfHwDaughterBdRev_Type()
)
wfHwDaughterBdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDaughterBdRev.setStatus("mandatory")
_WfHwDaughterBdSerialNumber_Type = OctetString
_WfHwDaughterBdSerialNumber_Object = MibTableColumn
wfHwDaughterBdSerialNumber = _WfHwDaughterBdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 10),
    _WfHwDaughterBdSerialNumber_Type()
)
wfHwDaughterBdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDaughterBdSerialNumber.setStatus("mandatory")
_WfHwBabyBdIdOpt_Type = Integer32
_WfHwBabyBdIdOpt_Object = MibTableColumn
wfHwBabyBdIdOpt = _WfHwBabyBdIdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 11),
    _WfHwBabyBdIdOpt_Type()
)
wfHwBabyBdIdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBabyBdIdOpt.setStatus("mandatory")
_WfHwBabyBdRev_Type = OctetString
_WfHwBabyBdRev_Object = MibTableColumn
wfHwBabyBdRev = _WfHwBabyBdRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 12),
    _WfHwBabyBdRev_Type()
)
wfHwBabyBdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBabyBdRev.setStatus("mandatory")
_WfHwBabyBdSerialNumber_Type = OctetString
_WfHwBabyBdSerialNumber_Object = MibTableColumn
wfHwBabyBdSerialNumber = _WfHwBabyBdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 13),
    _WfHwBabyBdSerialNumber_Type()
)
wfHwBabyBdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBabyBdSerialNumber.setStatus("mandatory")
_WfHwDiagPromRev_Type = OctetString
_WfHwDiagPromRev_Object = MibTableColumn
wfHwDiagPromRev = _WfHwDiagPromRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 14),
    _WfHwDiagPromRev_Type()
)
wfHwDiagPromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDiagPromRev.setStatus("mandatory")
_WfHwDiagPromDate_Type = DisplayString
_WfHwDiagPromDate_Object = MibTableColumn
wfHwDiagPromDate = _WfHwDiagPromDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 15),
    _WfHwDiagPromDate_Type()
)
wfHwDiagPromDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDiagPromDate.setStatus("mandatory")
_WfHwDiagPromSource_Type = DisplayString
_WfHwDiagPromSource_Object = MibTableColumn
wfHwDiagPromSource = _WfHwDiagPromSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 16),
    _WfHwDiagPromSource_Type()
)
wfHwDiagPromSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwDiagPromSource.setStatus("mandatory")
_WfHwBootPromRev_Type = OctetString
_WfHwBootPromRev_Object = MibTableColumn
wfHwBootPromRev = _WfHwBootPromRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 17),
    _WfHwBootPromRev_Type()
)
wfHwBootPromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBootPromRev.setStatus("mandatory")
_WfHwBootPromDate_Type = DisplayString
_WfHwBootPromDate_Object = MibTableColumn
wfHwBootPromDate = _WfHwBootPromDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 18),
    _WfHwBootPromDate_Type()
)
wfHwBootPromDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBootPromDate.setStatus("mandatory")
_WfHwBootPromSource_Type = DisplayString
_WfHwBootPromSource_Object = MibTableColumn
wfHwBootPromSource = _WfHwBootPromSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 19),
    _WfHwBootPromSource_Type()
)
wfHwBootPromSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwBootPromSource.setStatus("mandatory")
_WfHwSparePromRev_Type = OctetString
_WfHwSparePromRev_Object = MibTableColumn
wfHwSparePromRev = _WfHwSparePromRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 20),
    _WfHwSparePromRev_Type()
)
wfHwSparePromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSparePromRev.setStatus("mandatory")
_WfHwSparePromDate_Type = DisplayString
_WfHwSparePromDate_Object = MibTableColumn
wfHwSparePromDate = _WfHwSparePromDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 21),
    _WfHwSparePromDate_Type()
)
wfHwSparePromDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSparePromDate.setStatus("mandatory")
_WfHwSparePromSource_Type = DisplayString
_WfHwSparePromSource_Object = MibTableColumn
wfHwSparePromSource = _WfHwSparePromSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 22),
    _WfHwSparePromSource_Type()
)
wfHwSparePromSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwSparePromSource.setStatus("mandatory")


class _WfHwFileSysPresent_Type(Integer32):
    """Custom type wfHwFileSysPresent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filesys", 1),
          ("nofilesys", 2))
    )


_WfHwFileSysPresent_Type.__name__ = "Integer32"
_WfHwFileSysPresent_Object = MibTableColumn
wfHwFileSysPresent = _WfHwFileSysPresent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 23),
    _WfHwFileSysPresent_Type()
)
wfHwFileSysPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwFileSysPresent.setStatus("mandatory")


class _WfHwFileSysPresent2_Type(Integer32):
    """Custom type wfHwFileSysPresent2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filesys", 1),
          ("nofilesys", 2))
    )


_WfHwFileSysPresent2_Type.__name__ = "Integer32"
_WfHwFileSysPresent2_Object = MibTableColumn
wfHwFileSysPresent2 = _WfHwFileSysPresent2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 24),
    _WfHwFileSysPresent2_Type()
)
wfHwFileSysPresent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwFileSysPresent2.setStatus("mandatory")
_WfHwConfigServer_Type = Integer32
_WfHwConfigServer_Object = MibTableColumn
wfHwConfigServer = _WfHwConfigServer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 25),
    _WfHwConfigServer_Type()
)
wfHwConfigServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwConfigServer.setStatus("mandatory")
_WfHwConfigFile_Type = DisplayString
_WfHwConfigFile_Object = MibTableColumn
wfHwConfigFile = _WfHwConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 26),
    _WfHwConfigFile_Type()
)
wfHwConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwConfigFile.setStatus("mandatory")
_WfHwConfigDateAndTime_Type = OctetString
_WfHwConfigDateAndTime_Object = MibTableColumn
wfHwConfigDateAndTime = _WfHwConfigDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 27),
    _WfHwConfigDateAndTime_Type()
)
wfHwConfigDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwConfigDateAndTime.setStatus("mandatory")
_WfHwActiveImageName_Type = DisplayString
_WfHwActiveImageName_Object = MibTableColumn
wfHwActiveImageName = _WfHwActiveImageName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 28),
    _WfHwActiveImageName_Type()
)
wfHwActiveImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwActiveImageName.setStatus("mandatory")
_WfHwActiveImageSource_Type = DisplayString
_WfHwActiveImageSource_Object = MibTableColumn
wfHwActiveImageSource = _WfHwActiveImageSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 29),
    _WfHwActiveImageSource_Type()
)
wfHwActiveImageSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwActiveImageSource.setStatus("mandatory")
_WfHwActiveImageDate_Type = DisplayString
_WfHwActiveImageDate_Object = MibTableColumn
wfHwActiveImageDate = _WfHwActiveImageDate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 30),
    _WfHwActiveImageDate_Type()
)
wfHwActiveImageDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwActiveImageDate.setStatus("mandatory")
_WfHwMotherBdMemorySize_Type = Integer32
_WfHwMotherBdMemorySize_Object = MibTableColumn
wfHwMotherBdMemorySize = _WfHwMotherBdMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 31),
    _WfHwMotherBdMemorySize_Type()
)
wfHwMotherBdMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwMotherBdMemorySize.setStatus("mandatory")
_WfHwFastPacketCacheSize_Type = Integer32
_WfHwFastPacketCacheSize_Object = MibTableColumn
wfHwFastPacketCacheSize = _WfHwFastPacketCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 32),
    _WfHwFastPacketCacheSize_Type()
)
wfHwFastPacketCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwFastPacketCacheSize.setStatus("mandatory")
_WfHwModDaughterBd1IdOpt_Type = Integer32
_WfHwModDaughterBd1IdOpt_Object = MibTableColumn
wfHwModDaughterBd1IdOpt = _WfHwModDaughterBd1IdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 33),
    _WfHwModDaughterBd1IdOpt_Type()
)
wfHwModDaughterBd1IdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd1IdOpt.setStatus("mandatory")
_WfHwModDaughterBd1AwRev_Type = OctetString
_WfHwModDaughterBd1AwRev_Object = MibTableColumn
wfHwModDaughterBd1AwRev = _WfHwModDaughterBd1AwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 34),
    _WfHwModDaughterBd1AwRev_Type()
)
wfHwModDaughterBd1AwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd1AwRev.setStatus("mandatory")
_WfHwModDaughterBd1Rev_Type = OctetString
_WfHwModDaughterBd1Rev_Object = MibTableColumn
wfHwModDaughterBd1Rev = _WfHwModDaughterBd1Rev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 35),
    _WfHwModDaughterBd1Rev_Type()
)
wfHwModDaughterBd1Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd1Rev.setStatus("mandatory")
_WfHwModDaughterBd1SerialNumber_Type = OctetString
_WfHwModDaughterBd1SerialNumber_Object = MibTableColumn
wfHwModDaughterBd1SerialNumber = _WfHwModDaughterBd1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 36),
    _WfHwModDaughterBd1SerialNumber_Type()
)
wfHwModDaughterBd1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd1SerialNumber.setStatus("mandatory")
_WfHwModDaughterBd2IdOpt_Type = Integer32
_WfHwModDaughterBd2IdOpt_Object = MibTableColumn
wfHwModDaughterBd2IdOpt = _WfHwModDaughterBd2IdOpt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 37),
    _WfHwModDaughterBd2IdOpt_Type()
)
wfHwModDaughterBd2IdOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd2IdOpt.setStatus("mandatory")
_WfHwModDaughterBd2AwRev_Type = OctetString
_WfHwModDaughterBd2AwRev_Object = MibTableColumn
wfHwModDaughterBd2AwRev = _WfHwModDaughterBd2AwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 38),
    _WfHwModDaughterBd2AwRev_Type()
)
wfHwModDaughterBd2AwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd2AwRev.setStatus("mandatory")
_WfHwModDaughterBd2Rev_Type = OctetString
_WfHwModDaughterBd2Rev_Object = MibTableColumn
wfHwModDaughterBd2Rev = _WfHwModDaughterBd2Rev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 39),
    _WfHwModDaughterBd2Rev_Type()
)
wfHwModDaughterBd2Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd2Rev.setStatus("mandatory")
_WfHwModDaughterBd2SerialNumber_Type = OctetString
_WfHwModDaughterBd2SerialNumber_Object = MibTableColumn
wfHwModDaughterBd2SerialNumber = _WfHwModDaughterBd2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 40),
    _WfHwModDaughterBd2SerialNumber_Type()
)
wfHwModDaughterBd2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwModDaughterBd2SerialNumber.setStatus("mandatory")


class _WfRASNPwrSupply1_Type(Integer32):
    """Custom type wfRASNPwrSupply1 based on Integer32"""
    defaultValue = 4

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
        *(("fail", 2),
          ("notapplicable", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfRASNPwrSupply1_Type.__name__ = "Integer32"
_WfRASNPwrSupply1_Object = MibTableColumn
wfRASNPwrSupply1 = _WfRASNPwrSupply1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 41),
    _WfRASNPwrSupply1_Type()
)
wfRASNPwrSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRASNPwrSupply1.setStatus("mandatory")


class _WfRASNPwrSupply2_Type(Integer32):
    """Custom type wfRASNPwrSupply2 based on Integer32"""
    defaultValue = 4

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
        *(("fail", 2),
          ("notapplicable", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfRASNPwrSupply2_Type.__name__ = "Integer32"
_WfRASNPwrSupply2_Object = MibTableColumn
wfRASNPwrSupply2 = _WfRASNPwrSupply2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 42),
    _WfRASNPwrSupply2_Type()
)
wfRASNPwrSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRASNPwrSupply2.setStatus("mandatory")


class _WfPowerSupply1_Type(Integer32):
    """Custom type wfPowerSupply1 based on Integer32"""
    defaultValue = 4

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
        *(("fail", 2),
          ("notapplicable", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfPowerSupply1_Type.__name__ = "Integer32"
_WfPowerSupply1_Object = MibTableColumn
wfPowerSupply1 = _WfPowerSupply1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 43),
    _WfPowerSupply1_Type()
)
wfPowerSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPowerSupply1.setStatus("mandatory")


class _WfPowerSupply2_Type(Integer32):
    """Custom type wfPowerSupply2 based on Integer32"""
    defaultValue = 4

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
        *(("fail", 2),
          ("notapplicable", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfPowerSupply2_Type.__name__ = "Integer32"
_WfPowerSupply2_Object = MibTableColumn
wfPowerSupply2 = _WfPowerSupply2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 44),
    _WfPowerSupply2_Type()
)
wfPowerSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPowerSupply2.setStatus("mandatory")


class _WfFanStatus1_Type(Integer32):
    """Custom type wfFanStatus1 based on Integer32"""
    defaultValue = 4

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
        *(("fail", 2),
          ("notapplicable", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfFanStatus1_Type.__name__ = "Integer32"
_WfFanStatus1_Object = MibTableColumn
wfFanStatus1 = _WfFanStatus1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 45),
    _WfFanStatus1_Type()
)
wfFanStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFanStatus1.setStatus("mandatory")


class _WfFanStatus2_Type(Integer32):
    """Custom type wfFanStatus2 based on Integer32"""
    defaultValue = 4

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
        *(("fail", 2),
          ("notapplicable", 4),
          ("notpresent", 3),
          ("ok", 1))
    )


_WfFanStatus2_Type.__name__ = "Integer32"
_WfFanStatus2_Object = MibTableColumn
wfFanStatus2 = _WfFanStatus2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 46),
    _WfFanStatus2_Type()
)
wfFanStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFanStatus2.setStatus("mandatory")


class _WfRASNRPSUPresent_Type(Integer32):
    """Custom type wfRASNRPSUPresent based on Integer32"""
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
        *(("notapplicable", 3),
          ("notpresent", 2),
          ("present", 1))
    )


_WfRASNRPSUPresent_Type.__name__ = "Integer32"
_WfRASNRPSUPresent_Object = MibTableColumn
wfRASNRPSUPresent = _WfRASNRPSUPresent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 47),
    _WfRASNRPSUPresent_Type()
)
wfRASNRPSUPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRASNRPSUPresent.setStatus("obsolete")


class _WfModDiagStatus_Type(Integer32):
    """Custom type wfModDiagStatus based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              20)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notapplicable", 20),
          ("notpresent", 4),
          ("notrun", 3),
          ("passed", 1))
    )


_WfModDiagStatus_Type.__name__ = "Integer32"
_WfModDiagStatus_Object = MibTableColumn
wfModDiagStatus = _WfModDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 2, 1, 48),
    _WfModDiagStatus_Type()
)
wfModDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModDiagStatus.setStatus("mandatory")
_WfHwCfgTable_Object = MibTable
wfHwCfgTable = _WfHwCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 7)
)
if mibBuilder.loadTexts:
    wfHwCfgTable.setStatus("mandatory")
_WfHwCfgEntry_Object = MibTableRow
wfHwCfgEntry = _WfHwCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 7, 1)
)
wfHwCfgEntry.setIndexNames(
    (0, "Wellfleet-HARDWARE-MIB", "wfHwCfgSlot"),
)
if mibBuilder.loadTexts:
    wfHwCfgEntry.setStatus("mandatory")
_WfHwCfgSlot_Type = Integer32
_WfHwCfgSlot_Object = MibTableColumn
wfHwCfgSlot = _WfHwCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 7, 1, 1),
    _WfHwCfgSlot_Type()
)
wfHwCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHwCfgSlot.setStatus("mandatory")


class _WfRPSUPresent_Type(Integer32):
    """Custom type wfRPSUPresent based on Integer32"""
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
        *(("notapplicable", 3),
          ("notpresent", 2),
          ("present", 1))
    )


_WfRPSUPresent_Type.__name__ = "Integer32"
_WfRPSUPresent_Object = MibTableColumn
wfRPSUPresent = _WfRPSUPresent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 1, 7, 1, 2),
    _WfRPSUPresent_Type()
)
wfRPSUPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRPSUPresent.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-HARDWARE-MIB",
    **{"wfHwBase": wfHwBase,
       "wfHwBpIdOpt": wfHwBpIdOpt,
       "wfHwBpRev": wfHwBpRev,
       "wfHwBpSerialNumber": wfHwBpSerialNumber,
       "wfBCNPwrSupply1": wfBCNPwrSupply1,
       "wfBCNPwrSupply2": wfBCNPwrSupply2,
       "wfBCNPwrSupply3": wfBCNPwrSupply3,
       "wfBCNPwrSupply4": wfBCNPwrSupply4,
       "wfBCNFanStatus": wfBCNFanStatus,
       "wfBCNTemperature": wfBCNTemperature,
       "wfBCNTemperature2": wfBCNTemperature2,
       "wfFanSpeed": wfFanSpeed,
       "wfHwTable": wfHwTable,
       "wfHwEntry": wfHwEntry,
       "wfHwSlot": wfHwSlot,
       "wfHwModIdOpt": wfHwModIdOpt,
       "wfHwModRev": wfHwModRev,
       "wfHwModSerialNumber": wfHwModSerialNumber,
       "wfHwMotherBdIdOpt": wfHwMotherBdIdOpt,
       "wfHwMotherBdRev": wfHwMotherBdRev,
       "wfHwMotherBdSerialNumber": wfHwMotherBdSerialNumber,
       "wfHwDaughterBdIdOpt": wfHwDaughterBdIdOpt,
       "wfHwDaughterBdRev": wfHwDaughterBdRev,
       "wfHwDaughterBdSerialNumber": wfHwDaughterBdSerialNumber,
       "wfHwBabyBdIdOpt": wfHwBabyBdIdOpt,
       "wfHwBabyBdRev": wfHwBabyBdRev,
       "wfHwBabyBdSerialNumber": wfHwBabyBdSerialNumber,
       "wfHwDiagPromRev": wfHwDiagPromRev,
       "wfHwDiagPromDate": wfHwDiagPromDate,
       "wfHwDiagPromSource": wfHwDiagPromSource,
       "wfHwBootPromRev": wfHwBootPromRev,
       "wfHwBootPromDate": wfHwBootPromDate,
       "wfHwBootPromSource": wfHwBootPromSource,
       "wfHwSparePromRev": wfHwSparePromRev,
       "wfHwSparePromDate": wfHwSparePromDate,
       "wfHwSparePromSource": wfHwSparePromSource,
       "wfHwFileSysPresent": wfHwFileSysPresent,
       "wfHwFileSysPresent2": wfHwFileSysPresent2,
       "wfHwConfigServer": wfHwConfigServer,
       "wfHwConfigFile": wfHwConfigFile,
       "wfHwConfigDateAndTime": wfHwConfigDateAndTime,
       "wfHwActiveImageName": wfHwActiveImageName,
       "wfHwActiveImageSource": wfHwActiveImageSource,
       "wfHwActiveImageDate": wfHwActiveImageDate,
       "wfHwMotherBdMemorySize": wfHwMotherBdMemorySize,
       "wfHwFastPacketCacheSize": wfHwFastPacketCacheSize,
       "wfHwModDaughterBd1IdOpt": wfHwModDaughterBd1IdOpt,
       "wfHwModDaughterBd1AwRev": wfHwModDaughterBd1AwRev,
       "wfHwModDaughterBd1Rev": wfHwModDaughterBd1Rev,
       "wfHwModDaughterBd1SerialNumber": wfHwModDaughterBd1SerialNumber,
       "wfHwModDaughterBd2IdOpt": wfHwModDaughterBd2IdOpt,
       "wfHwModDaughterBd2AwRev": wfHwModDaughterBd2AwRev,
       "wfHwModDaughterBd2Rev": wfHwModDaughterBd2Rev,
       "wfHwModDaughterBd2SerialNumber": wfHwModDaughterBd2SerialNumber,
       "wfRASNPwrSupply1": wfRASNPwrSupply1,
       "wfRASNPwrSupply2": wfRASNPwrSupply2,
       "wfPowerSupply1": wfPowerSupply1,
       "wfPowerSupply2": wfPowerSupply2,
       "wfFanStatus1": wfFanStatus1,
       "wfFanStatus2": wfFanStatus2,
       "wfRASNRPSUPresent": wfRASNRPSUPresent,
       "wfModDiagStatus": wfModDiagStatus,
       "wfHwCfgTable": wfHwCfgTable,
       "wfHwCfgEntry": wfHwCfgEntry,
       "wfHwCfgSlot": wfHwCfgSlot,
       "wfRPSUPresent": wfRPSUPresent}
)
