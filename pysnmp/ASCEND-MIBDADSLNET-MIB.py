# SNMP MIB module (ASCEND-MIBDADSLNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDADSLNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:24 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibdadslNetworkProfile_ObjectIdentity = ObjectIdentity
mibdadslNetworkProfile = _MibdadslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 7)
)
_MibdadslNetworkProfileTable_Object = MibTable
mibdadslNetworkProfileTable = _MibdadslNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1)
)
if mibBuilder.loadTexts:
    mibdadslNetworkProfileTable.setStatus("mandatory")
_MibdadslNetworkProfileEntry_Object = MibTableRow
mibdadslNetworkProfileEntry = _MibdadslNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1)
)
mibdadslNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDADSLNET-MIB", "dadslNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBDADSLNET-MIB", "dadslNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBDADSLNET-MIB", "dadslNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibdadslNetworkProfileEntry.setStatus("mandatory")
_DadslNetworkProfile_Shelf_o_Type = Integer32
_DadslNetworkProfile_Shelf_o_Object = MibScalar
dadslNetworkProfile_Shelf_o = _DadslNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 1),
    _DadslNetworkProfile_Shelf_o_Type()
)
dadslNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadslNetworkProfile_Shelf_o.setStatus("mandatory")
_DadslNetworkProfile_Slot_o_Type = Integer32
_DadslNetworkProfile_Slot_o_Object = MibScalar
dadslNetworkProfile_Slot_o = _DadslNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 2),
    _DadslNetworkProfile_Slot_o_Type()
)
dadslNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadslNetworkProfile_Slot_o.setStatus("mandatory")
_DadslNetworkProfile_Item_o_Type = Integer32
_DadslNetworkProfile_Item_o_Object = MibScalar
dadslNetworkProfile_Item_o = _DadslNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 3),
    _DadslNetworkProfile_Item_o_Type()
)
dadslNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dadslNetworkProfile_Item_o.setStatus("mandatory")
_DadslNetworkProfile_Name_Type = DisplayString
_DadslNetworkProfile_Name_Object = MibScalar
dadslNetworkProfile_Name = _DadslNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 4),
    _DadslNetworkProfile_Name_Type()
)
dadslNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_Name.setStatus("mandatory")


class _DadslNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type dadslNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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
        *(("anyShelf", 1),
          ("shelf1", 2),
          ("shelf2", 3),
          ("shelf3", 4),
          ("shelf4", 5),
          ("shelf5", 6),
          ("shelf6", 7),
          ("shelf7", 8),
          ("shelf8", 9),
          ("shelf9", 10))
    )


_DadslNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DadslNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
dadslNetworkProfile_PhysicalAddress_Shelf = _DadslNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 5),
    _DadslNetworkProfile_PhysicalAddress_Shelf_Type()
)
dadslNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _DadslNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type dadslNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_DadslNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_DadslNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
dadslNetworkProfile_PhysicalAddress_Slot = _DadslNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 6),
    _DadslNetworkProfile_PhysicalAddress_Slot_Type()
)
dadslNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_DadslNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_DadslNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
dadslNetworkProfile_PhysicalAddress_ItemNumber = _DadslNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 7),
    _DadslNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
dadslNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _DadslNetworkProfile_Enabled_Type(Integer32):
    """Custom type dadslNetworkProfile_Enabled based on Integer32"""
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


_DadslNetworkProfile_Enabled_Type.__name__ = "Integer32"
_DadslNetworkProfile_Enabled_Object = MibScalar
dadslNetworkProfile_Enabled = _DadslNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 8),
    _DadslNetworkProfile_Enabled_Type()
)
dadslNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_Enabled.setStatus("mandatory")
_DadslNetworkProfile_ProfileNumber_Type = Integer32
_DadslNetworkProfile_ProfileNumber_Object = MibScalar
dadslNetworkProfile_ProfileNumber = _DadslNetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 9),
    _DadslNetworkProfile_ProfileNumber_Type()
)
dadslNetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_ProfileNumber.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_DadslNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
dadslNetworkProfile_LineConfig_TrunkGroup = _DadslNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 10),
    _DadslNetworkProfile_LineConfig_TrunkGroup_Type()
)
dadslNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_DadslNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
dadslNetworkProfile_LineConfig_NailedGroup = _DadslNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 11),
    _DadslNetworkProfile_LineConfig_NailedGroup_Type()
)
dadslNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 12),
    _DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 13),
    _DadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_DadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
dadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _DadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 14),
    _DadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
dadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_Activation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dcdDsrActive", 3),
          ("dsrActive", 2),
          ("static", 1))
    )


_DadslNetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_Activation_Object = MibScalar
dadslNetworkProfile_LineConfig_Activation = _DadslNetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 15),
    _DadslNetworkProfile_LineConfig_Activation_Type()
)
dadslNetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_DataRateMode_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_DataRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 2),
          ("singlebaud", 3))
    )


_DadslNetworkProfile_LineConfig_DataRateMode_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_DataRateMode_Object = MibScalar
dadslNetworkProfile_LineConfig_DataRateMode = _DadslNetworkProfile_LineConfig_DataRateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 19),
    _DadslNetworkProfile_LineConfig_DataRateMode_Type()
)
dadslNetworkProfile_LineConfig_DataRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_DataRateMode.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_MaxUpStreamRate_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_MaxUpStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("n-1088000", 152),
          ("n-128000", 161),
          ("n-256000", 160),
          ("n-384000", 159),
          ("n-512000", 158),
          ("n-640000", 157),
          ("n-768000", 156),
          ("n-800000", 155),
          ("n-896000", 154),
          ("n-928000", 153),
          ("upstrmMegMax", 151))
    )


_DadslNetworkProfile_LineConfig_MaxUpStreamRate_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_MaxUpStreamRate_Object = MibScalar
dadslNetworkProfile_LineConfig_MaxUpStreamRate = _DadslNetworkProfile_LineConfig_MaxUpStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 20),
    _DadslNetworkProfile_LineConfig_MaxUpStreamRate_Type()
)
dadslNetworkProfile_LineConfig_MaxUpStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_MaxUpStreamRate.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_MaxDownStreamRate_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_MaxDownStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
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
              122)
        )
    )
    namedValues = NamedValues(
        *(("dwnstrmMegMax", 101),
          ("n-128000", 122),
          ("n-1280000", 115),
          ("n-1600000", 114),
          ("n-1920000", 113),
          ("n-2240000", 112),
          ("n-256000", 121),
          ("n-2560000", 111),
          ("n-2688000", 110),
          ("n-3200000", 109),
          ("n-384000", 120),
          ("n-4480000", 108),
          ("n-512000", 119),
          ("n-5120000", 107),
          ("n-6272000", 106),
          ("n-640000", 118),
          ("n-7168000", 105),
          ("n-768000", 117),
          ("n-8000000", 104),
          ("n-8960000", 103),
          ("n-9504000", 102),
          ("n-960000", 116))
    )


_DadslNetworkProfile_LineConfig_MaxDownStreamRate_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_MaxDownStreamRate_Object = MibScalar
dadslNetworkProfile_LineConfig_MaxDownStreamRate = _DadslNetworkProfile_LineConfig_MaxDownStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 21),
    _DadslNetworkProfile_LineConfig_MaxDownStreamRate_Type()
)
dadslNetworkProfile_LineConfig_MaxDownStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_MaxDownStreamRate.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_UpStreamMargin_Type = Integer32
_DadslNetworkProfile_LineConfig_UpStreamMargin_Object = MibScalar
dadslNetworkProfile_LineConfig_UpStreamMargin = _DadslNetworkProfile_LineConfig_UpStreamMargin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 22),
    _DadslNetworkProfile_LineConfig_UpStreamMargin_Type()
)
dadslNetworkProfile_LineConfig_UpStreamMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_UpStreamMargin.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_DownStreamMargin_Type = Integer32
_DadslNetworkProfile_LineConfig_DownStreamMargin_Object = MibScalar
dadslNetworkProfile_LineConfig_DownStreamMargin = _DadslNetworkProfile_LineConfig_DownStreamMargin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 23),
    _DadslNetworkProfile_LineConfig_DownStreamMargin_Type()
)
dadslNetworkProfile_LineConfig_DownStreamMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_DownStreamMargin.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_UpStreamInterleave_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_UpStreamInterleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17,
              33,
              65)
        )
    )
    namedValues = NamedValues(
        *(("dmt0", 1),
          ("dmt16", 17),
          ("dmt2", 3),
          ("dmt32", 33),
          ("dmt4", 5),
          ("dmt64", 65),
          ("dmt8", 9))
    )


_DadslNetworkProfile_LineConfig_UpStreamInterleave_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_UpStreamInterleave_Object = MibScalar
dadslNetworkProfile_LineConfig_UpStreamInterleave = _DadslNetworkProfile_LineConfig_UpStreamInterleave_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 24),
    _DadslNetworkProfile_LineConfig_UpStreamInterleave_Type()
)
dadslNetworkProfile_LineConfig_UpStreamInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_UpStreamInterleave.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_DownStreamInterleave_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_DownStreamInterleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17,
              33,
              65)
        )
    )
    namedValues = NamedValues(
        *(("dmt0", 1),
          ("dmt16", 17),
          ("dmt2", 3),
          ("dmt32", 33),
          ("dmt4", 5),
          ("dmt64", 65),
          ("dmt8", 9))
    )


_DadslNetworkProfile_LineConfig_DownStreamInterleave_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_DownStreamInterleave_Object = MibScalar
dadslNetworkProfile_LineConfig_DownStreamInterleave = _DadslNetworkProfile_LineConfig_DownStreamInterleave_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 25),
    _DadslNetworkProfile_LineConfig_DownStreamInterleave_Type()
)
dadslNetworkProfile_LineConfig_DownStreamInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_DownStreamInterleave.setStatus("mandatory")
_DadslNetworkProfile_LineConfig_TxPowerLevel_Type = Integer32
_DadslNetworkProfile_LineConfig_TxPowerLevel_Object = MibScalar
dadslNetworkProfile_LineConfig_TxPowerLevel = _DadslNetworkProfile_LineConfig_TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 26),
    _DadslNetworkProfile_LineConfig_TxPowerLevel_Type()
)
dadslNetworkProfile_LineConfig_TxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_TxPowerLevel.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_TxPowerAutoState_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_TxPowerAutoState based on Integer32"""
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
        *(("adjusting", 2),
          ("disabled", 1),
          ("locked", 4),
          ("tracking", 3))
    )


_DadslNetworkProfile_LineConfig_TxPowerAutoState_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_TxPowerAutoState_Object = MibScalar
dadslNetworkProfile_LineConfig_TxPowerAutoState = _DadslNetworkProfile_LineConfig_TxPowerAutoState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 27),
    _DadslNetworkProfile_LineConfig_TxPowerAutoState_Type()
)
dadslNetworkProfile_LineConfig_TxPowerAutoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_TxPowerAutoState.setStatus("mandatory")


class _DadslNetworkProfile_LineConfig_MaintainLanUp_Type(Integer32):
    """Custom type dadslNetworkProfile_LineConfig_MaintainLanUp based on Integer32"""
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


_DadslNetworkProfile_LineConfig_MaintainLanUp_Type.__name__ = "Integer32"
_DadslNetworkProfile_LineConfig_MaintainLanUp_Object = MibScalar
dadslNetworkProfile_LineConfig_MaintainLanUp = _DadslNetworkProfile_LineConfig_MaintainLanUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 28),
    _DadslNetworkProfile_LineConfig_MaintainLanUp_Type()
)
dadslNetworkProfile_LineConfig_MaintainLanUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_LineConfig_MaintainLanUp.setStatus("mandatory")


class _DadslNetworkProfile_Action_o_Type(Integer32):
    """Custom type dadslNetworkProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_DadslNetworkProfile_Action_o_Type.__name__ = "Integer32"
_DadslNetworkProfile_Action_o_Object = MibScalar
dadslNetworkProfile_Action_o = _DadslNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 7, 1, 1, 29),
    _DadslNetworkProfile_Action_o_Type()
)
dadslNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dadslNetworkProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDADSLNET-MIB",
    **{"DisplayString": DisplayString,
       "mibdadslNetworkProfile": mibdadslNetworkProfile,
       "mibdadslNetworkProfileTable": mibdadslNetworkProfileTable,
       "mibdadslNetworkProfileEntry": mibdadslNetworkProfileEntry,
       "dadslNetworkProfile-Shelf-o": dadslNetworkProfile_Shelf_o,
       "dadslNetworkProfile-Slot-o": dadslNetworkProfile_Slot_o,
       "dadslNetworkProfile-Item-o": dadslNetworkProfile_Item_o,
       "dadslNetworkProfile-Name": dadslNetworkProfile_Name,
       "dadslNetworkProfile-PhysicalAddress-Shelf": dadslNetworkProfile_PhysicalAddress_Shelf,
       "dadslNetworkProfile-PhysicalAddress-Slot": dadslNetworkProfile_PhysicalAddress_Slot,
       "dadslNetworkProfile-PhysicalAddress-ItemNumber": dadslNetworkProfile_PhysicalAddress_ItemNumber,
       "dadslNetworkProfile-Enabled": dadslNetworkProfile_Enabled,
       "dadslNetworkProfile-ProfileNumber": dadslNetworkProfile_ProfileNumber,
       "dadslNetworkProfile-LineConfig-TrunkGroup": dadslNetworkProfile_LineConfig_TrunkGroup,
       "dadslNetworkProfile-LineConfig-NailedGroup": dadslNetworkProfile_LineConfig_NailedGroup,
       "dadslNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "dadslNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": dadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "dadslNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": dadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "dadslNetworkProfile-LineConfig-Activation": dadslNetworkProfile_LineConfig_Activation,
       "dadslNetworkProfile-LineConfig-DataRateMode": dadslNetworkProfile_LineConfig_DataRateMode,
       "dadslNetworkProfile-LineConfig-MaxUpStreamRate": dadslNetworkProfile_LineConfig_MaxUpStreamRate,
       "dadslNetworkProfile-LineConfig-MaxDownStreamRate": dadslNetworkProfile_LineConfig_MaxDownStreamRate,
       "dadslNetworkProfile-LineConfig-UpStreamMargin": dadslNetworkProfile_LineConfig_UpStreamMargin,
       "dadslNetworkProfile-LineConfig-DownStreamMargin": dadslNetworkProfile_LineConfig_DownStreamMargin,
       "dadslNetworkProfile-LineConfig-UpStreamInterleave": dadslNetworkProfile_LineConfig_UpStreamInterleave,
       "dadslNetworkProfile-LineConfig-DownStreamInterleave": dadslNetworkProfile_LineConfig_DownStreamInterleave,
       "dadslNetworkProfile-LineConfig-TxPowerLevel": dadslNetworkProfile_LineConfig_TxPowerLevel,
       "dadslNetworkProfile-LineConfig-TxPowerAutoState": dadslNetworkProfile_LineConfig_TxPowerAutoState,
       "dadslNetworkProfile-LineConfig-MaintainLanUp": dadslNetworkProfile_LineConfig_MaintainLanUp,
       "dadslNetworkProfile-Action-o": dadslNetworkProfile_Action_o}
)
