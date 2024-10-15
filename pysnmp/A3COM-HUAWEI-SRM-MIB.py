# SNMP MIB module (A3COM-HUAWEI-SRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-SRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:05 2024
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

(mlsr,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "mlsr")

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

aR46_E200 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hw8060DevObjects_ObjectIdentity = ObjectIdentity
hw8060DevObjects = _Hw8060DevObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1)
)
_Hw8060FrameTable_Object = MibTable
hw8060FrameTable = _Hw8060FrameTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 1)
)
if mibBuilder.loadTexts:
    hw8060FrameTable.setStatus("current")
_Hw8060FrameEntry_Object = MibTableRow
hw8060FrameEntry = _Hw8060FrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 1, 1)
)
hw8060FrameEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SRM-MIB", "hw8060FrameIndex"),
)
if mibBuilder.loadTexts:
    hw8060FrameEntry.setStatus("current")


class _Hw8060FrameIndex_Type(Integer32):
    """Custom type hw8060FrameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hw8060FrameIndex_Type.__name__ = "Integer32"
_Hw8060FrameIndex_Object = MibTableColumn
hw8060FrameIndex = _Hw8060FrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 1, 1, 1),
    _Hw8060FrameIndex_Type()
)
hw8060FrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060FrameIndex.setStatus("current")
_Hw8060FrameType_Type = Integer32
_Hw8060FrameType_Object = MibTableColumn
hw8060FrameType = _Hw8060FrameType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 1, 1, 2),
    _Hw8060FrameType_Type()
)
hw8060FrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060FrameType.setStatus("current")


class _Hw8060FrameDesc_Type(OctetString):
    """Custom type hw8060FrameDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hw8060FrameDesc_Type.__name__ = "OctetString"
_Hw8060FrameDesc_Object = MibTableColumn
hw8060FrameDesc = _Hw8060FrameDesc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 1, 1, 3),
    _Hw8060FrameDesc_Type()
)
hw8060FrameDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hw8060FrameDesc.setStatus("current")
_Hw8060FrameSlotNumber_Type = Integer32
_Hw8060FrameSlotNumber_Object = MibTableColumn
hw8060FrameSlotNumber = _Hw8060FrameSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 1, 1, 4),
    _Hw8060FrameSlotNumber_Type()
)
hw8060FrameSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060FrameSlotNumber.setStatus("current")
_Hw8060FrameAdminStatus_Type = Integer32
_Hw8060FrameAdminStatus_Object = MibTableColumn
hw8060FrameAdminStatus = _Hw8060FrameAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 1, 1, 5),
    _Hw8060FrameAdminStatus_Type()
)
hw8060FrameAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060FrameAdminStatus.setStatus("current")
_Hw8060SlotTable_Object = MibTable
hw8060SlotTable = _Hw8060SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2)
)
if mibBuilder.loadTexts:
    hw8060SlotTable.setStatus("current")
_Hw8060SlotEntry_Object = MibTableRow
hw8060SlotEntry = _Hw8060SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1)
)
hw8060SlotEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SRM-MIB", "hw8060SlotIndex"),
)
if mibBuilder.loadTexts:
    hw8060SlotEntry.setStatus("current")


class _Hw8060SlotIndex_Type(Integer32):
    """Custom type hw8060SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hw8060SlotIndex_Type.__name__ = "Integer32"
_Hw8060SlotIndex_Object = MibTableColumn
hw8060SlotIndex = _Hw8060SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 1),
    _Hw8060SlotIndex_Type()
)
hw8060SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotIndex.setStatus("current")


class _Hw8060SlotType_Type(Integer32):
    """Custom type hw8060SlotType based on Integer32"""
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
              233)
        )
    )
    namedValues = NamedValues(
        *(("am12", 27),
          ("am6", 28),
          ("ame12", 61),
          ("ame6", 60),
          ("as", 2),
          ("as16", 16),
          ("ase16", 78),
          ("ase8", 77),
          ("atm155m", 76),
          ("atm155m-mm", 106),
          ("atm155m-sm", 107),
          ("atm155m-sml", 108),
          ("atm1ADSLI", 119),
          ("atm1shdsl4wire", 151),
          ("atm25m", 93),
          ("atm2ADSLI", 120),
          ("atmIma4shdsl", 152),
          ("atmadsl1", 74),
          ("atmadsl2", 75),
          ("atme3", 94),
          ("atmshdsl1", 90),
          ("atmshdsl2", 91),
          ("atmshdsl4", 92),
          ("atmt3", 95),
          ("aux", 31),
          ("bi", 4),
          ("bs4", 132),
          ("bsv2", 160),
          ("bsv2-v2", 224),
          ("bsv4", 161),
          ("cavium", 117),
          ("ce32", 159),
          ("cf-card", 223),
          ("console", 32),
          ("cpos", 103),
          ("cpos-t1", 111),
          ("dm-epri", 231),
          ("dm-tpri", 232),
          ("e1", 8),
          ("e11-f", 65),
          ("e11-f-17", 71),
          ("e12", 5),
          ("e12-f", 66),
          ("e14", 6),
          ("e14-f", 67),
          ("e18-120", 124),
          ("e18-75", 123),
          ("e1vi", 26),
          ("e1vi1-v2", 225),
          ("e1vi2", 226),
          ("em2", 21),
          ("em4", 24),
          ("erpu", 163),
          ("erpu-h", 233),
          ("fcm2", 58),
          ("fcm4", 57),
          ("fcm6", 51),
          ("fe1", 7),
          ("fe18-120", 221),
          ("fe18-75", 220),
          ("fe1op", 104),
          ("fe1op-mfx", 110),
          ("fe1op-sfx", 109),
          ("fe2", 9),
          ("fix-1sae", 116),
          ("fix-1wan", 115),
          ("fix-e11", 121),
          ("fix-t11", 122),
          ("ft18", 222),
          ("ft3", 158),
          ("fxo2", 20),
          ("fxo4", 23),
          ("fxs2", 19),
          ("fxs4", 22),
          ("ge1", 101),
          ("ge1-op", 112),
          ("ge2", 114),
          ("ge2-op", 113),
          ("ima-4e1120", 136),
          ("ima-4e175", 135),
          ("ima-4t1", 138),
          ("ima-8e1120", 134),
          ("ima-8e175", 133),
          ("ima-8t1", 137),
          ("ls16", 155),
          ("ls4", 153),
          ("ls8", 154),
          ("lsa", 18),
          ("ndec", 29),
          ("new8as", 17),
          ("newsa2", 30),
          ("osm", 229),
          ("pos155m", 102),
          ("rpu", 162),
          ("rtb21ce3", 59),
          ("rtb21ct3", 73),
          ("s1b", 14),
          ("sa2", 15),
          ("sa8", 52),
          ("sab", 25),
          ("sae2", 80),
          ("sae4", 79),
          ("sae8", 105),
          ("sd707", 230),
          ("sic-1Eth", 118),
          ("sic-1am", 43),
          ("sic-1bs", 41),
          ("sic-1bu", 39),
          ("sic-1e1", 37),
          ("sic-1e1f", 140),
          ("sic-1em", 45),
          ("sic-1fe", 34),
          ("sic-1fxo", 49),
          ("sic-1fxs", 47),
          ("sic-1sa", 35),
          ("sic-1t1", 38),
          ("sic-1t1f", 139),
          ("sic-1vifxo", 127),
          ("sic-1vifxs", 126),
          ("sic-2am", 44),
          ("sic-2bs", 42),
          ("sic-2bu", 40),
          ("sic-2em", 46),
          ("sic-2fxo", 50),
          ("sic-2fxs", 48),
          ("sic-2vifxo", 129),
          ("sic-2vifxs", 128),
          ("sic-3as", 36),
          ("sic-adls2plus-isdn", 156),
          ("sic-adls2plus-pots", 157),
          ("sic-wan", 33),
          ("ss", 3),
          ("t11", 53),
          ("t11-f", 68),
          ("t11-f-17", 72),
          ("t12", 54),
          ("t12-f", 69),
          ("t14", 55),
          ("t14-f", 70),
          ("t18", 125),
          ("t1vi", 56),
          ("t1vi1-v2", 227),
          ("t1vi2", 228),
          ("unavailable", 1),
          ("vi2", 11),
          ("vi30", 13),
          ("vi4", 12),
          ("xdsl-adsl", 97),
          ("xdsl-bri", 99),
          ("xdsl-fec", 96),
          ("xdsl-fec-new", 130),
          ("xdsl-gshdsl", 98),
          ("xdsl-sa", 131),
          ("xdsl-scc", 100))
    )


_Hw8060SlotType_Type.__name__ = "Integer32"
_Hw8060SlotType_Object = MibTableColumn
hw8060SlotType = _Hw8060SlotType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 2),
    _Hw8060SlotType_Type()
)
hw8060SlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotType.setStatus("current")


class _Hw8060SlotDesc_Type(OctetString):
    """Custom type hw8060SlotDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hw8060SlotDesc_Type.__name__ = "OctetString"
_Hw8060SlotDesc_Object = MibTableColumn
hw8060SlotDesc = _Hw8060SlotDesc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 3),
    _Hw8060SlotDesc_Type()
)
hw8060SlotDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hw8060SlotDesc.setStatus("current")
_Hw8060SlotCpuRatio_Type = Integer32
_Hw8060SlotCpuRatio_Object = MibTableColumn
hw8060SlotCpuRatio = _Hw8060SlotCpuRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 4),
    _Hw8060SlotCpuRatio_Type()
)
hw8060SlotCpuRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotCpuRatio.setStatus("current")
_Hw8060SlotPcbVersion_Type = OctetString
_Hw8060SlotPcbVersion_Object = MibTableColumn
hw8060SlotPcbVersion = _Hw8060SlotPcbVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 5),
    _Hw8060SlotPcbVersion_Type()
)
hw8060SlotPcbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotPcbVersion.setStatus("current")
_Hw8060SlotSoftwareVersion_Type = OctetString
_Hw8060SlotSoftwareVersion_Object = MibTableColumn
hw8060SlotSoftwareVersion = _Hw8060SlotSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 6),
    _Hw8060SlotSoftwareVersion_Type()
)
hw8060SlotSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotSoftwareVersion.setStatus("current")
_Hw8060SlotSubslotNumber_Type = Integer32
_Hw8060SlotSubslotNumber_Object = MibTableColumn
hw8060SlotSubslotNumber = _Hw8060SlotSubslotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 7),
    _Hw8060SlotSubslotNumber_Type()
)
hw8060SlotSubslotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotSubslotNumber.setStatus("current")
_Hw8060SlotAdminStatus_Type = Integer32
_Hw8060SlotAdminStatus_Object = MibTableColumn
hw8060SlotAdminStatus = _Hw8060SlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 8),
    _Hw8060SlotAdminStatus_Type()
)
hw8060SlotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotAdminStatus.setStatus("current")
_Hw8060SlotOperStatus_Type = Integer32
_Hw8060SlotOperStatus_Object = MibTableColumn
hw8060SlotOperStatus = _Hw8060SlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 2, 1, 9),
    _Hw8060SlotOperStatus_Type()
)
hw8060SlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SlotOperStatus.setStatus("current")
_Hw8060SubslotTable_Object = MibTable
hw8060SubslotTable = _Hw8060SubslotTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 3)
)
if mibBuilder.loadTexts:
    hw8060SubslotTable.setStatus("current")
_Hw8060SubslotEntry_Object = MibTableRow
hw8060SubslotEntry = _Hw8060SubslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 3, 1)
)
hw8060SubslotEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SRM-MIB", "hw8060SlotIndex"),
    (0, "A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex"),
)
if mibBuilder.loadTexts:
    hw8060SubslotEntry.setStatus("current")


class _Hw8060SubslotIndex_Type(Integer32):
    """Custom type hw8060SubslotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hw8060SubslotIndex_Type.__name__ = "Integer32"
_Hw8060SubslotIndex_Object = MibTableColumn
hw8060SubslotIndex = _Hw8060SubslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 3, 1, 1),
    _Hw8060SubslotIndex_Type()
)
hw8060SubslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SubslotIndex.setStatus("current")
_Hw8060SubslotType_Type = Integer32
_Hw8060SubslotType_Object = MibTableColumn
hw8060SubslotType = _Hw8060SubslotType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 3, 1, 2),
    _Hw8060SubslotType_Type()
)
hw8060SubslotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SubslotType.setStatus("current")
_Hw8060SubslotPortNum_Type = Integer32
_Hw8060SubslotPortNum_Object = MibTableColumn
hw8060SubslotPortNum = _Hw8060SubslotPortNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 3, 1, 3),
    _Hw8060SubslotPortNum_Type()
)
hw8060SubslotPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SubslotPortNum.setStatus("current")
_Hw8060SubslotAdminStatus_Type = Integer32
_Hw8060SubslotAdminStatus_Object = MibTableColumn
hw8060SubslotAdminStatus = _Hw8060SubslotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 3, 1, 4),
    _Hw8060SubslotAdminStatus_Type()
)
hw8060SubslotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SubslotAdminStatus.setStatus("current")
_Hw8060PortTable_Object = MibTable
hw8060PortTable = _Hw8060PortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4)
)
if mibBuilder.loadTexts:
    hw8060PortTable.setStatus("current")
_Hw8060PortEntry_Object = MibTableRow
hw8060PortEntry = _Hw8060PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4, 1)
)
hw8060PortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SRM-MIB", "hw8060SlotIndex"),
    (0, "A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex"),
    (0, "A3COM-HUAWEI-SRM-MIB", "hw8060PortIndex"),
)
if mibBuilder.loadTexts:
    hw8060PortEntry.setStatus("current")


class _Hw8060PortIndex_Type(Integer32):
    """Custom type hw8060PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hw8060PortIndex_Type.__name__ = "Integer32"
_Hw8060PortIndex_Object = MibTableColumn
hw8060PortIndex = _Hw8060PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4, 1, 1),
    _Hw8060PortIndex_Type()
)
hw8060PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060PortIndex.setStatus("current")
_Hw8060PortType_Type = Integer32
_Hw8060PortType_Object = MibTableColumn
hw8060PortType = _Hw8060PortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4, 1, 2),
    _Hw8060PortType_Type()
)
hw8060PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060PortType.setStatus("current")


class _Hw8060PortDesc_Type(OctetString):
    """Custom type hw8060PortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hw8060PortDesc_Type.__name__ = "OctetString"
_Hw8060PortDesc_Object = MibTableColumn
hw8060PortDesc = _Hw8060PortDesc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4, 1, 3),
    _Hw8060PortDesc_Type()
)
hw8060PortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060PortDesc.setStatus("current")
_Hw8060PortSpeed_Type = Integer32
_Hw8060PortSpeed_Object = MibTableColumn
hw8060PortSpeed = _Hw8060PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4, 1, 4),
    _Hw8060PortSpeed_Type()
)
hw8060PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060PortSpeed.setStatus("current")
_Hw8060PortAdminStatus_Type = Integer32
_Hw8060PortAdminStatus_Object = MibTableColumn
hw8060PortAdminStatus = _Hw8060PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4, 1, 5),
    _Hw8060PortAdminStatus_Type()
)
hw8060PortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060PortAdminStatus.setStatus("current")
_Hw8060PortOperateStatus_Type = Integer32
_Hw8060PortOperateStatus_Object = MibTableColumn
hw8060PortOperateStatus = _Hw8060PortOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 4, 1, 6),
    _Hw8060PortOperateStatus_Type()
)
hw8060PortOperateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060PortOperateStatus.setStatus("current")
_Dev8060MPowerStatusTable_Object = MibTable
dev8060MPowerStatusTable = _Dev8060MPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 5)
)
if mibBuilder.loadTexts:
    dev8060MPowerStatusTable.setStatus("current")
_Dev8060MPowerStatusEntry_Object = MibTableRow
dev8060MPowerStatusEntry = _Dev8060MPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 5, 1)
)
dev8060MPowerStatusEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SRM-MIB", "dev8060MPowerNum"),
)
if mibBuilder.loadTexts:
    dev8060MPowerStatusEntry.setStatus("current")


class _Dev8060MPowerNum_Type(Integer32):
    """Custom type dev8060MPowerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dev8060MPowerNum_Type.__name__ = "Integer32"
_Dev8060MPowerNum_Object = MibTableColumn
dev8060MPowerNum = _Dev8060MPowerNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 5, 1, 1),
    _Dev8060MPowerNum_Type()
)
dev8060MPowerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dev8060MPowerNum.setStatus("current")


class _Dev8060MPowerStatus_Type(Integer32):
    """Custom type dev8060MPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_Dev8060MPowerStatus_Type.__name__ = "Integer32"
_Dev8060MPowerStatus_Object = MibTableColumn
dev8060MPowerStatus = _Dev8060MPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 5, 1, 2),
    _Dev8060MPowerStatus_Type()
)
dev8060MPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dev8060MPowerStatus.setStatus("current")
_Dev8060MFanStatusTable_Object = MibTable
dev8060MFanStatusTable = _Dev8060MFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 6)
)
if mibBuilder.loadTexts:
    dev8060MFanStatusTable.setStatus("current")
_Dev8060MFanStatusEntry_Object = MibTableRow
dev8060MFanStatusEntry = _Dev8060MFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 6, 1)
)
dev8060MFanStatusEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SRM-MIB", "dev8060MFanNum"),
)
if mibBuilder.loadTexts:
    dev8060MFanStatusEntry.setStatus("current")


class _Dev8060MFanNum_Type(Integer32):
    """Custom type dev8060MFanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Dev8060MFanNum_Type.__name__ = "Integer32"
_Dev8060MFanNum_Object = MibTableColumn
dev8060MFanNum = _Dev8060MFanNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 6, 1, 1),
    _Dev8060MFanNum_Type()
)
dev8060MFanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dev8060MFanNum.setStatus("current")


class _Dev8060MFanStatus_Type(Integer32):
    """Custom type dev8060MFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_Dev8060MFanStatus_Type.__name__ = "Integer32"
_Dev8060MFanStatus_Object = MibTableColumn
dev8060MFanStatus = _Dev8060MFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 6, 1, 2),
    _Dev8060MFanStatus_Type()
)
dev8060MFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dev8060MFanStatus.setStatus("current")
_Dev8060MGlobalTable_ObjectIdentity = ObjectIdentity
dev8060MGlobalTable = _Dev8060MGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 7)
)
_Hw8060DevMRpuTemperature_Type = Integer32
_Hw8060DevMRpuTemperature_Object = MibScalar
hw8060DevMRpuTemperature = _Hw8060DevMRpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 7, 1),
    _Hw8060DevMRpuTemperature_Type()
)
hw8060DevMRpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060DevMRpuTemperature.setStatus("current")
_Hw8060DevMTemperatureMax_Type = Integer32
_Hw8060DevMTemperatureMax_Object = MibScalar
hw8060DevMTemperatureMax = _Hw8060DevMTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 7, 2),
    _Hw8060DevMTemperatureMax_Type()
)
hw8060DevMTemperatureMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hw8060DevMTemperatureMax.setStatus("current")
_Hw8060DevMTemperatureMin_Type = Integer32
_Hw8060DevMTemperatureMin_Object = MibScalar
hw8060DevMTemperatureMin = _Hw8060DevMTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 7, 3),
    _Hw8060DevMTemperatureMin_Type()
)
hw8060DevMTemperatureMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hw8060DevMTemperatureMin.setStatus("current")
_Hw8060SysVersion_Type = OctetString
_Hw8060SysVersion_Object = MibScalar
hw8060SysVersion = _Hw8060SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 7, 4),
    _Hw8060SysVersion_Type()
)
hw8060SysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SysVersion.setStatus("current")
_Hw8060SysTime_Type = Integer32
_Hw8060SysTime_Object = MibScalar
hw8060SysTime = _Hw8060SysTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 7, 5),
    _Hw8060SysTime_Type()
)
hw8060SysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060SysTime.setStatus("current")
_Hw8060DevMVentTemperature_Type = Integer32
_Hw8060DevMVentTemperature_Object = MibScalar
hw8060DevMVentTemperature = _Hw8060DevMVentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 1, 7, 6),
    _Hw8060DevMVentTemperature_Type()
)
hw8060DevMVentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8060DevMVentTemperature.setStatus("current")
_Hw8060DevNotifications_ObjectIdentity = ObjectIdentity
hw8060DevNotifications = _Hw8060DevNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2)
)
_Hw8060DevConformance_ObjectIdentity = ObjectIdentity
hw8060DevConformance = _Hw8060DevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 3)
)

# Managed Objects groups


# Notification objects

hwRpuTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 1)
)
if mibBuilder.loadTexts:
    hwRpuTempTooHigh.setStatus(
        "current"
    )

hwRpuTempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 2)
)
if mibBuilder.loadTexts:
    hwRpuTempOK.setStatus(
        "current"
    )

hwNpTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 3)
)
if mibBuilder.loadTexts:
    hwNpTempTooHigh.setStatus(
        "current"
    )

hwNpTempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 4)
)
if mibBuilder.loadTexts:
    hwNpTempOK.setStatus(
        "current"
    )

hwRpuTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 5)
)
if mibBuilder.loadTexts:
    hwRpuTempTooLow.setStatus(
        "current"
    )

hwNpTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 6)
)
if mibBuilder.loadTexts:
    hwNpTempTooLow.setStatus(
        "current"
    )

hwVentTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 7)
)
if mibBuilder.loadTexts:
    hwVentTempTooHigh.setStatus(
        "current"
    )

hwVentTempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 9)
)
if mibBuilder.loadTexts:
    hwVentTempOK.setStatus(
        "current"
    )

hwRpuReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 10)
)
if mibBuilder.loadTexts:
    hwRpuReset.setStatus(
        "current"
    )

hwRpuResetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 11)
)
if mibBuilder.loadTexts:
    hwRpuResetOK.setStatus(
        "current"
    )

hwNpReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 12)
)
if mibBuilder.loadTexts:
    hwNpReset.setStatus(
        "current"
    )

hwNpResetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 13)
)
if mibBuilder.loadTexts:
    hwNpResetOK.setStatus(
        "current"
    )

hwSlotReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 14)
)
hwSlotReset.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SlotIndex")
)
if mibBuilder.loadTexts:
    hwSlotReset.setStatus(
        "current"
    )

hwSlotResetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 15)
)
hwSlotResetOK.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SlotIndex")
)
if mibBuilder.loadTexts:
    hwSlotResetOK.setStatus(
        "current"
    )

hwPciAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 16)
)
if mibBuilder.loadTexts:
    hwPciAlarm.setStatus(
        "current"
    )

hwPciNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 17)
)
if mibBuilder.loadTexts:
    hwPciNormal.setStatus(
        "current"
    )

hwRpuIntReportErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 18)
)
if mibBuilder.loadTexts:
    hwRpuIntReportErr.setStatus(
        "current"
    )

hwNpIntReportErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 19)
)
if mibBuilder.loadTexts:
    hwNpIntReportErr.setStatus(
        "current"
    )

hwSlotIntReportErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 20)
)
hwSlotIntReportErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwSlotIntReportErr.setStatus(
        "current"
    )

hwWriteFlashErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 21)
)
if mibBuilder.loadTexts:
    hwWriteFlashErr.setStatus(
        "current"
    )

hwPowerUnitFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 22)
)
hwPowerUnitFail.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "dev8060MPowerNum")
)
if mibBuilder.loadTexts:
    hwPowerUnitFail.setStatus(
        "current"
    )

hwPowerUnitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 23)
)
hwPowerUnitNormal.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "dev8060MPowerNum")
)
if mibBuilder.loadTexts:
    hwPowerUnitNormal.setStatus(
        "current"
    )

hwFanUnitFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 24)
)
hwFanUnitFail.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "dev8060MFanNum")
)
if mibBuilder.loadTexts:
    hwFanUnitFail.setStatus(
        "current"
    )

hwFanUnitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 25)
)
hwFanUnitNormal.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "dev8060MFanNum")
)
if mibBuilder.loadTexts:
    hwFanUnitNormal.setStatus(
        "current"
    )

hwFtpLoadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 26)
)
if mibBuilder.loadTexts:
    hwFtpLoadFail.setStatus(
        "current"
    )

hwTftpLoadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 27)
)
if mibBuilder.loadTexts:
    hwTftpLoadFail.setStatus(
        "current"
    )

hwXmodemLoadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 28)
)
if mibBuilder.loadTexts:
    hwXmodemLoadFail.setStatus(
        "current"
    )

hwNpConfPathErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 29)
)
if mibBuilder.loadTexts:
    hwNpConfPathErr.setStatus(
        "current"
    )

hwHSCardConfPathErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 30)
)
hwHSCardConfPathErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwHSCardConfPathErr.setStatus(
        "current"
    )

hwLSCardJtagErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 31)
)
hwLSCardJtagErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwLSCardJtagErr.setStatus(
        "current"
    )

hwHSCardJtagErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 32)
)
hwHSCardJtagErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwHSCardJtagErr.setStatus(
        "current"
    )

hwNpuJtagErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 33)
)
if mibBuilder.loadTexts:
    hwNpuJtagErr.setStatus(
        "current"
    )

hwNpRpuDmuErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 34)
)
if mibBuilder.loadTexts:
    hwNpRpuDmuErr.setStatus(
        "current"
    )

hwLSCardHealthyErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 35)
)
hwLSCardHealthyErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwLSCardHealthyErr.setStatus(
        "current"
    )

hwHSCardHealthyErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 36)
)
hwHSCardHealthyErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwHSCardHealthyErr.setStatus(
        "current"
    )

hwCardPciHealthyErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 37)
)
hwCardPciHealthyErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwCardPciHealthyErr.setStatus(
        "current"
    )

hwHSCardPowerErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 38)
)
hwHSCardPowerErr.setObjects(
    ("A3COM-HUAWEI-SRM-MIB", "hw8060SubslotIndex")
)
if mibBuilder.loadTexts:
    hwHSCardPowerErr.setStatus(
        "current"
    )

hwVentTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 20, 2, 39)
)
if mibBuilder.loadTexts:
    hwVentTempTooLow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-SRM-MIB",
    **{"aR46-E200": aR46_E200,
       "hw8060DevObjects": hw8060DevObjects,
       "hw8060FrameTable": hw8060FrameTable,
       "hw8060FrameEntry": hw8060FrameEntry,
       "hw8060FrameIndex": hw8060FrameIndex,
       "hw8060FrameType": hw8060FrameType,
       "hw8060FrameDesc": hw8060FrameDesc,
       "hw8060FrameSlotNumber": hw8060FrameSlotNumber,
       "hw8060FrameAdminStatus": hw8060FrameAdminStatus,
       "hw8060SlotTable": hw8060SlotTable,
       "hw8060SlotEntry": hw8060SlotEntry,
       "hw8060SlotIndex": hw8060SlotIndex,
       "hw8060SlotType": hw8060SlotType,
       "hw8060SlotDesc": hw8060SlotDesc,
       "hw8060SlotCpuRatio": hw8060SlotCpuRatio,
       "hw8060SlotPcbVersion": hw8060SlotPcbVersion,
       "hw8060SlotSoftwareVersion": hw8060SlotSoftwareVersion,
       "hw8060SlotSubslotNumber": hw8060SlotSubslotNumber,
       "hw8060SlotAdminStatus": hw8060SlotAdminStatus,
       "hw8060SlotOperStatus": hw8060SlotOperStatus,
       "hw8060SubslotTable": hw8060SubslotTable,
       "hw8060SubslotEntry": hw8060SubslotEntry,
       "hw8060SubslotIndex": hw8060SubslotIndex,
       "hw8060SubslotType": hw8060SubslotType,
       "hw8060SubslotPortNum": hw8060SubslotPortNum,
       "hw8060SubslotAdminStatus": hw8060SubslotAdminStatus,
       "hw8060PortTable": hw8060PortTable,
       "hw8060PortEntry": hw8060PortEntry,
       "hw8060PortIndex": hw8060PortIndex,
       "hw8060PortType": hw8060PortType,
       "hw8060PortDesc": hw8060PortDesc,
       "hw8060PortSpeed": hw8060PortSpeed,
       "hw8060PortAdminStatus": hw8060PortAdminStatus,
       "hw8060PortOperateStatus": hw8060PortOperateStatus,
       "dev8060MPowerStatusTable": dev8060MPowerStatusTable,
       "dev8060MPowerStatusEntry": dev8060MPowerStatusEntry,
       "dev8060MPowerNum": dev8060MPowerNum,
       "dev8060MPowerStatus": dev8060MPowerStatus,
       "dev8060MFanStatusTable": dev8060MFanStatusTable,
       "dev8060MFanStatusEntry": dev8060MFanStatusEntry,
       "dev8060MFanNum": dev8060MFanNum,
       "dev8060MFanStatus": dev8060MFanStatus,
       "dev8060MGlobalTable": dev8060MGlobalTable,
       "hw8060DevMRpuTemperature": hw8060DevMRpuTemperature,
       "hw8060DevMTemperatureMax": hw8060DevMTemperatureMax,
       "hw8060DevMTemperatureMin": hw8060DevMTemperatureMin,
       "hw8060SysVersion": hw8060SysVersion,
       "hw8060SysTime": hw8060SysTime,
       "hw8060DevMVentTemperature": hw8060DevMVentTemperature,
       "hw8060DevNotifications": hw8060DevNotifications,
       "hwRpuTempTooHigh": hwRpuTempTooHigh,
       "hwRpuTempOK": hwRpuTempOK,
       "hwNpTempTooHigh": hwNpTempTooHigh,
       "hwNpTempOK": hwNpTempOK,
       "hwRpuTempTooLow": hwRpuTempTooLow,
       "hwNpTempTooLow": hwNpTempTooLow,
       "hwVentTempTooHigh": hwVentTempTooHigh,
       "hwVentTempOK": hwVentTempOK,
       "hwRpuReset": hwRpuReset,
       "hwRpuResetOK": hwRpuResetOK,
       "hwNpReset": hwNpReset,
       "hwNpResetOK": hwNpResetOK,
       "hwSlotReset": hwSlotReset,
       "hwSlotResetOK": hwSlotResetOK,
       "hwPciAlarm": hwPciAlarm,
       "hwPciNormal": hwPciNormal,
       "hwRpuIntReportErr": hwRpuIntReportErr,
       "hwNpIntReportErr": hwNpIntReportErr,
       "hwSlotIntReportErr": hwSlotIntReportErr,
       "hwWriteFlashErr": hwWriteFlashErr,
       "hwPowerUnitFail": hwPowerUnitFail,
       "hwPowerUnitNormal": hwPowerUnitNormal,
       "hwFanUnitFail": hwFanUnitFail,
       "hwFanUnitNormal": hwFanUnitNormal,
       "hwFtpLoadFail": hwFtpLoadFail,
       "hwTftpLoadFail": hwTftpLoadFail,
       "hwXmodemLoadFail": hwXmodemLoadFail,
       "hwNpConfPathErr": hwNpConfPathErr,
       "hwHSCardConfPathErr": hwHSCardConfPathErr,
       "hwLSCardJtagErr": hwLSCardJtagErr,
       "hwHSCardJtagErr": hwHSCardJtagErr,
       "hwNpuJtagErr": hwNpuJtagErr,
       "hwNpRpuDmuErr": hwNpRpuDmuErr,
       "hwLSCardHealthyErr": hwLSCardHealthyErr,
       "hwHSCardHealthyErr": hwHSCardHealthyErr,
       "hwCardPciHealthyErr": hwCardPciHealthyErr,
       "hwHSCardPowerErr": hwHSCardPowerErr,
       "hwVentTempTooLow": hwVentTempTooLow,
       "hw8060DevConformance": hw8060DevConformance}
)
