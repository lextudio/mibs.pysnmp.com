# SNMP MIB module (ASCEND-MIBCADSLNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCADSLNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:19 2024
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

_MibcadslNetworkProfile_ObjectIdentity = ObjectIdentity
mibcadslNetworkProfile = _MibcadslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 6)
)
_MibcadslNetworkProfileTable_Object = MibTable
mibcadslNetworkProfileTable = _MibcadslNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1)
)
if mibBuilder.loadTexts:
    mibcadslNetworkProfileTable.setStatus("mandatory")
_MibcadslNetworkProfileEntry_Object = MibTableRow
mibcadslNetworkProfileEntry = _MibcadslNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1)
)
mibcadslNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBCADSLNET-MIB", "cadslNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBCADSLNET-MIB", "cadslNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBCADSLNET-MIB", "cadslNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibcadslNetworkProfileEntry.setStatus("mandatory")
_CadslNetworkProfile_Shelf_o_Type = Integer32
_CadslNetworkProfile_Shelf_o_Object = MibScalar
cadslNetworkProfile_Shelf_o = _CadslNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 1),
    _CadslNetworkProfile_Shelf_o_Type()
)
cadslNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadslNetworkProfile_Shelf_o.setStatus("mandatory")
_CadslNetworkProfile_Slot_o_Type = Integer32
_CadslNetworkProfile_Slot_o_Object = MibScalar
cadslNetworkProfile_Slot_o = _CadslNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 2),
    _CadslNetworkProfile_Slot_o_Type()
)
cadslNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadslNetworkProfile_Slot_o.setStatus("mandatory")
_CadslNetworkProfile_Item_o_Type = Integer32
_CadslNetworkProfile_Item_o_Object = MibScalar
cadslNetworkProfile_Item_o = _CadslNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 3),
    _CadslNetworkProfile_Item_o_Type()
)
cadslNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadslNetworkProfile_Item_o.setStatus("mandatory")
_CadslNetworkProfile_Name_Type = DisplayString
_CadslNetworkProfile_Name_Object = MibScalar
cadslNetworkProfile_Name = _CadslNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 4),
    _CadslNetworkProfile_Name_Type()
)
cadslNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_Name.setStatus("mandatory")


class _CadslNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type cadslNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_CadslNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_CadslNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
cadslNetworkProfile_PhysicalAddress_Shelf = _CadslNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 5),
    _CadslNetworkProfile_PhysicalAddress_Shelf_Type()
)
cadslNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _CadslNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type cadslNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_CadslNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_CadslNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
cadslNetworkProfile_PhysicalAddress_Slot = _CadslNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 6),
    _CadslNetworkProfile_PhysicalAddress_Slot_Type()
)
cadslNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_CadslNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_CadslNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
cadslNetworkProfile_PhysicalAddress_ItemNumber = _CadslNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 7),
    _CadslNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
cadslNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _CadslNetworkProfile_Enabled_Type(Integer32):
    """Custom type cadslNetworkProfile_Enabled based on Integer32"""
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


_CadslNetworkProfile_Enabled_Type.__name__ = "Integer32"
_CadslNetworkProfile_Enabled_Object = MibScalar
cadslNetworkProfile_Enabled = _CadslNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 8),
    _CadslNetworkProfile_Enabled_Type()
)
cadslNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_Enabled.setStatus("mandatory")
_CadslNetworkProfile_ProfileNumber_Type = Integer32
_CadslNetworkProfile_ProfileNumber_Object = MibScalar
cadslNetworkProfile_ProfileNumber = _CadslNetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 9),
    _CadslNetworkProfile_ProfileNumber_Type()
)
cadslNetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_ProfileNumber.setStatus("mandatory")
_CadslNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_CadslNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
cadslNetworkProfile_LineConfig_TrunkGroup = _CadslNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 10),
    _CadslNetworkProfile_LineConfig_TrunkGroup_Type()
)
cadslNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_CadslNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_CadslNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
cadslNetworkProfile_LineConfig_NailedGroup = _CadslNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 11),
    _CadslNetworkProfile_LineConfig_NailedGroup_Type()
)
cadslNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 12),
    _CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 13),
    _CadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_CadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_CadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
cadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _CadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 14),
    _CadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
cadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _CadslNetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type cadslNetworkProfile_LineConfig_Activation based on Integer32"""
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


_CadslNetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_CadslNetworkProfile_LineConfig_Activation_Object = MibScalar
cadslNetworkProfile_LineConfig_Activation = _CadslNetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 15),
    _CadslNetworkProfile_LineConfig_Activation_Type()
)
cadslNetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _CadslNetworkProfile_LineConfig_DataRateMode_Type(Integer32):
    """Custom type cadslNetworkProfile_LineConfig_DataRateMode based on Integer32"""
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


_CadslNetworkProfile_LineConfig_DataRateMode_Type.__name__ = "Integer32"
_CadslNetworkProfile_LineConfig_DataRateMode_Object = MibScalar
cadslNetworkProfile_LineConfig_DataRateMode = _CadslNetworkProfile_LineConfig_DataRateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 19),
    _CadslNetworkProfile_LineConfig_DataRateMode_Type()
)
cadslNetworkProfile_LineConfig_DataRateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_DataRateMode.setStatus("mandatory")


class _CadslNetworkProfile_LineConfig_MaxUpStreamRate_Type(Integer32):
    """Custom type cadslNetworkProfile_LineConfig_MaxUpStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("n-1088000", 51),
          ("n-272000", 57),
          ("n-408000", 56),
          ("n-544000", 55),
          ("n-680000", 54),
          ("n-816000", 53),
          ("n-952000", 52))
    )


_CadslNetworkProfile_LineConfig_MaxUpStreamRate_Type.__name__ = "Integer32"
_CadslNetworkProfile_LineConfig_MaxUpStreamRate_Object = MibScalar
cadslNetworkProfile_LineConfig_MaxUpStreamRate = _CadslNetworkProfile_LineConfig_MaxUpStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 20),
    _CadslNetworkProfile_LineConfig_MaxUpStreamRate_Type()
)
cadslNetworkProfile_LineConfig_MaxUpStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_MaxUpStreamRate.setStatus("mandatory")


class _CadslNetworkProfile_LineConfig_MaxDownStreamRate_Type(Integer32):
    """Custom type cadslNetworkProfile_LineConfig_MaxDownStreamRate based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("n-1280000", 11),
          ("n-1600000", 10),
          ("n-1920000", 9),
          ("n-2240000", 8),
          ("n-2560000", 7),
          ("n-2688000", 6),
          ("n-3200000", 5),
          ("n-4480000", 4),
          ("n-5120000", 3),
          ("n-6272000", 2),
          ("n-640000", 13),
          ("n-7168000", 1),
          ("n-960000", 12))
    )


_CadslNetworkProfile_LineConfig_MaxDownStreamRate_Type.__name__ = "Integer32"
_CadslNetworkProfile_LineConfig_MaxDownStreamRate_Object = MibScalar
cadslNetworkProfile_LineConfig_MaxDownStreamRate = _CadslNetworkProfile_LineConfig_MaxDownStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 21),
    _CadslNetworkProfile_LineConfig_MaxDownStreamRate_Type()
)
cadslNetworkProfile_LineConfig_MaxDownStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_MaxDownStreamRate.setStatus("mandatory")


class _CadslNetworkProfile_Action_o_Type(Integer32):
    """Custom type cadslNetworkProfile_Action_o based on Integer32"""
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


_CadslNetworkProfile_Action_o_Type.__name__ = "Integer32"
_CadslNetworkProfile_Action_o_Object = MibScalar
cadslNetworkProfile_Action_o = _CadslNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 22),
    _CadslNetworkProfile_Action_o_Type()
)
cadslNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_Action_o.setStatus("mandatory")


class _CadslNetworkProfile_LineConfig_LoopBack_Type(Integer32):
    """Custom type cadslNetworkProfile_LineConfig_LoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 3),
          ("none", 1))
    )


_CadslNetworkProfile_LineConfig_LoopBack_Type.__name__ = "Integer32"
_CadslNetworkProfile_LineConfig_LoopBack_Object = MibScalar
cadslNetworkProfile_LineConfig_LoopBack = _CadslNetworkProfile_LineConfig_LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 6, 1, 1, 23),
    _CadslNetworkProfile_LineConfig_LoopBack_Type()
)
cadslNetworkProfile_LineConfig_LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadslNetworkProfile_LineConfig_LoopBack.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCADSLNET-MIB",
    **{"DisplayString": DisplayString,
       "mibcadslNetworkProfile": mibcadslNetworkProfile,
       "mibcadslNetworkProfileTable": mibcadslNetworkProfileTable,
       "mibcadslNetworkProfileEntry": mibcadslNetworkProfileEntry,
       "cadslNetworkProfile-Shelf-o": cadslNetworkProfile_Shelf_o,
       "cadslNetworkProfile-Slot-o": cadslNetworkProfile_Slot_o,
       "cadslNetworkProfile-Item-o": cadslNetworkProfile_Item_o,
       "cadslNetworkProfile-Name": cadslNetworkProfile_Name,
       "cadslNetworkProfile-PhysicalAddress-Shelf": cadslNetworkProfile_PhysicalAddress_Shelf,
       "cadslNetworkProfile-PhysicalAddress-Slot": cadslNetworkProfile_PhysicalAddress_Slot,
       "cadslNetworkProfile-PhysicalAddress-ItemNumber": cadslNetworkProfile_PhysicalAddress_ItemNumber,
       "cadslNetworkProfile-Enabled": cadslNetworkProfile_Enabled,
       "cadslNetworkProfile-ProfileNumber": cadslNetworkProfile_ProfileNumber,
       "cadslNetworkProfile-LineConfig-TrunkGroup": cadslNetworkProfile_LineConfig_TrunkGroup,
       "cadslNetworkProfile-LineConfig-NailedGroup": cadslNetworkProfile_LineConfig_NailedGroup,
       "cadslNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "cadslNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": cadslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "cadslNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": cadslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "cadslNetworkProfile-LineConfig-Activation": cadslNetworkProfile_LineConfig_Activation,
       "cadslNetworkProfile-LineConfig-DataRateMode": cadslNetworkProfile_LineConfig_DataRateMode,
       "cadslNetworkProfile-LineConfig-MaxUpStreamRate": cadslNetworkProfile_LineConfig_MaxUpStreamRate,
       "cadslNetworkProfile-LineConfig-MaxDownStreamRate": cadslNetworkProfile_LineConfig_MaxDownStreamRate,
       "cadslNetworkProfile-Action-o": cadslNetworkProfile_Action_o,
       "cadslNetworkProfile-LineConfig-LoopBack": cadslNetworkProfile_LineConfig_LoopBack}
)
