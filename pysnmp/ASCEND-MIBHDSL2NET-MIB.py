# SNMP MIB module (ASCEND-MIBHDSL2NET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBHDSL2NET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:37 2024
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

_Mibhdsl2NetworkProfile_ObjectIdentity = ObjectIdentity
mibhdsl2NetworkProfile = _Mibhdsl2NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 14)
)
_Mibhdsl2NetworkProfileTable_Object = MibTable
mibhdsl2NetworkProfileTable = _Mibhdsl2NetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1)
)
if mibBuilder.loadTexts:
    mibhdsl2NetworkProfileTable.setStatus("mandatory")
_Mibhdsl2NetworkProfileEntry_Object = MibTableRow
mibhdsl2NetworkProfileEntry = _Mibhdsl2NetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1)
)
mibhdsl2NetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-Slot-o"),
    (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibhdsl2NetworkProfileEntry.setStatus("mandatory")
_Hdsl2NetworkProfile_Shelf_o_Type = Integer32
_Hdsl2NetworkProfile_Shelf_o_Object = MibScalar
hdsl2NetworkProfile_Shelf_o = _Hdsl2NetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 1),
    _Hdsl2NetworkProfile_Shelf_o_Type()
)
hdsl2NetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_Shelf_o.setStatus("mandatory")
_Hdsl2NetworkProfile_Slot_o_Type = Integer32
_Hdsl2NetworkProfile_Slot_o_Object = MibScalar
hdsl2NetworkProfile_Slot_o = _Hdsl2NetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 2),
    _Hdsl2NetworkProfile_Slot_o_Type()
)
hdsl2NetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_Slot_o.setStatus("mandatory")
_Hdsl2NetworkProfile_Item_o_Type = Integer32
_Hdsl2NetworkProfile_Item_o_Object = MibScalar
hdsl2NetworkProfile_Item_o = _Hdsl2NetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 3),
    _Hdsl2NetworkProfile_Item_o_Type()
)
hdsl2NetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_Item_o.setStatus("mandatory")
_Hdsl2NetworkProfile_Name_Type = DisplayString
_Hdsl2NetworkProfile_Name_Object = MibScalar
hdsl2NetworkProfile_Name = _Hdsl2NetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 4),
    _Hdsl2NetworkProfile_Name_Type()
)
hdsl2NetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_Name.setStatus("mandatory")


class _Hdsl2NetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type hdsl2NetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_Hdsl2NetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
hdsl2NetworkProfile_PhysicalAddress_Shelf = _Hdsl2NetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 5),
    _Hdsl2NetworkProfile_PhysicalAddress_Shelf_Type()
)
hdsl2NetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _Hdsl2NetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type hdsl2NetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_Hdsl2NetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_PhysicalAddress_Slot_Object = MibScalar
hdsl2NetworkProfile_PhysicalAddress_Slot = _Hdsl2NetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 6),
    _Hdsl2NetworkProfile_PhysicalAddress_Slot_Type()
)
hdsl2NetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_Hdsl2NetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_Hdsl2NetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
hdsl2NetworkProfile_PhysicalAddress_ItemNumber = _Hdsl2NetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 7),
    _Hdsl2NetworkProfile_PhysicalAddress_ItemNumber_Type()
)
hdsl2NetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Hdsl2NetworkProfile_Enabled_Type(Integer32):
    """Custom type hdsl2NetworkProfile_Enabled based on Integer32"""
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


_Hdsl2NetworkProfile_Enabled_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_Enabled_Object = MibScalar
hdsl2NetworkProfile_Enabled = _Hdsl2NetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 8),
    _Hdsl2NetworkProfile_Enabled_Type()
)
hdsl2NetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_Enabled.setStatus("mandatory")
_Hdsl2NetworkProfile_ProfileNumber_Type = Integer32
_Hdsl2NetworkProfile_ProfileNumber_Object = MibScalar
hdsl2NetworkProfile_ProfileNumber = _Hdsl2NetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 9),
    _Hdsl2NetworkProfile_ProfileNumber_Type()
)
hdsl2NetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ProfileNumber.setStatus("mandatory")
_Hdsl2NetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_Hdsl2NetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
hdsl2NetworkProfile_LineConfig_TrunkGroup = _Hdsl2NetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 10),
    _Hdsl2NetworkProfile_LineConfig_TrunkGroup_Type()
)
hdsl2NetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_Hdsl2NetworkProfile_LineConfig_NailedGroup_Type = Integer32
_Hdsl2NetworkProfile_LineConfig_NailedGroup_Object = MibScalar
hdsl2NetworkProfile_LineConfig_NailedGroup = _Hdsl2NetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 11),
    _Hdsl2NetworkProfile_LineConfig_NailedGroup_Type()
)
hdsl2NetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_Hdsl2NetworkProfile_LineConfig_VpSwitchingVpi_Type = Integer32
_Hdsl2NetworkProfile_LineConfig_VpSwitchingVpi_Object = MibScalar
hdsl2NetworkProfile_LineConfig_VpSwitchingVpi = _Hdsl2NetworkProfile_LineConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 12),
    _Hdsl2NetworkProfile_LineConfig_VpSwitchingVpi_Type()
)
hdsl2NetworkProfile_LineConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_VpSwitchingVpi.setStatus("mandatory")
_Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 13),
    _Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 14),
    _Hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_Hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_Hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _Hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 15),
    _Hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_Activation based on Integer32"""
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


_Hdsl2NetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_Activation_Object = MibScalar
hdsl2NetworkProfile_LineConfig_Activation = _Hdsl2NetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 16),
    _Hdsl2NetworkProfile_LineConfig_Activation_Type()
)
hdsl2NetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf based on Integer32"""
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


_Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf_Object = MibScalar
hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf = _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 17),
    _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf_Type()
)
hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot based on Integer32"""
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


_Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot_Object = MibScalar
hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot = _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 18),
    _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot_Type()
)
hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot.setStatus("mandatory")
_Hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Type = Integer32
_Hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Object = MibScalar
hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber = _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 19),
    _Hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Type()
)
hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_UnitType_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_UnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coe", 1),
          ("cpe", 2))
    )


_Hdsl2NetworkProfile_LineConfig_UnitType_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_UnitType_Object = MibScalar
hdsl2NetworkProfile_LineConfig_UnitType = _Hdsl2NetworkProfile_LineConfig_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 20),
    _Hdsl2NetworkProfile_LineConfig_UnitType_Type()
)
hdsl2NetworkProfile_LineConfig_UnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_UnitType.setStatus("mandatory")


class _Hdsl2NetworkProfile_Action_o_Type(Integer32):
    """Custom type hdsl2NetworkProfile_Action_o based on Integer32"""
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


_Hdsl2NetworkProfile_Action_o_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_Action_o_Object = MibScalar
hdsl2NetworkProfile_Action_o = _Hdsl2NetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 23),
    _Hdsl2NetworkProfile_Action_o_Type()
)
hdsl2NetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_Action_o.setStatus("mandatory")


class _Hdsl2NetworkProfile_SparingMode_Type(Integer32):
    """Custom type hdsl2NetworkProfile_SparingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("inactive", 1),
          ("manual", 2))
    )


_Hdsl2NetworkProfile_SparingMode_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_SparingMode_Object = MibScalar
hdsl2NetworkProfile_SparingMode = _Hdsl2NetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 24),
    _Hdsl2NetworkProfile_SparingMode_Type()
)
hdsl2NetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_SparingMode.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_NtrEnabled_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_NtrEnabled based on Integer32"""
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


_Hdsl2NetworkProfile_LineConfig_NtrEnabled_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_NtrEnabled_Object = MibScalar
hdsl2NetworkProfile_LineConfig_NtrEnabled = _Hdsl2NetworkProfile_LineConfig_NtrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 25),
    _Hdsl2NetworkProfile_LineConfig_NtrEnabled_Type()
)
hdsl2NetworkProfile_LineConfig_NtrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_NtrEnabled.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_ClockSource_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_ClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("notEligible", 2))
    )


_Hdsl2NetworkProfile_LineConfig_ClockSource_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_ClockSource_Object = MibScalar
hdsl2NetworkProfile_LineConfig_ClockSource = _Hdsl2NetworkProfile_LineConfig_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 26),
    _Hdsl2NetworkProfile_LineConfig_ClockSource_Type()
)
hdsl2NetworkProfile_LineConfig_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_ClockSource.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_ClockPriority_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_ClockPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("lowPriority", 4),
          ("middlePriority", 3))
    )


_Hdsl2NetworkProfile_LineConfig_ClockPriority_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_ClockPriority_Object = MibScalar
hdsl2NetworkProfile_LineConfig_ClockPriority = _Hdsl2NetworkProfile_LineConfig_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 27),
    _Hdsl2NetworkProfile_LineConfig_ClockPriority_Type()
)
hdsl2NetworkProfile_LineConfig_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_ClockPriority.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_LoopBack_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_LoopBack based on Integer32"""
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


_Hdsl2NetworkProfile_LineConfig_LoopBack_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_LoopBack_Object = MibScalar
hdsl2NetworkProfile_LineConfig_LoopBack = _Hdsl2NetworkProfile_LineConfig_LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 28),
    _Hdsl2NetworkProfile_LineConfig_LoopBack_Type()
)
hdsl2NetworkProfile_LineConfig_LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_LoopBack.setStatus("mandatory")


class _Hdsl2NetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type hdsl2NetworkProfile_IgnoreLineup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("systemDefined", 1),
          ("yes", 3))
    )


_Hdsl2NetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_IgnoreLineup_Object = MibScalar
hdsl2NetworkProfile_IgnoreLineup = _Hdsl2NetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 29),
    _Hdsl2NetworkProfile_IgnoreLineup_Type()
)
hdsl2NetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_IgnoreLineup.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_Margin_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_Margin based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("disable", 17),
          ("n-0db", 1),
          ("n-10db", 11),
          ("n-1db", 2),
          ("n-2db", 3),
          ("n-3db", 4),
          ("n-4db", 5),
          ("n-5db", 6),
          ("n-6db", 7),
          ("n-7db", 8),
          ("n-8db", 9),
          ("n-9db", 10))
    )


_Hdsl2NetworkProfile_LineConfig_Margin_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_Margin_Object = MibScalar
hdsl2NetworkProfile_LineConfig_Margin = _Hdsl2NetworkProfile_LineConfig_Margin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 30),
    _Hdsl2NetworkProfile_LineConfig_Margin_Type()
)
hdsl2NetworkProfile_LineConfig_Margin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_Margin.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_RateMode_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_RateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("fixed", 1))
    )


_Hdsl2NetworkProfile_LineConfig_RateMode_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_RateMode_Object = MibScalar
hdsl2NetworkProfile_LineConfig_RateMode = _Hdsl2NetworkProfile_LineConfig_RateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 31),
    _Hdsl2NetworkProfile_LineConfig_RateMode_Type()
)
hdsl2NetworkProfile_LineConfig_RateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_RateMode.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_MinRate_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_MinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(72001,
              136001,
              200001,
              264001,
              328001,
              392001,
              520001,
              776001,
              1032001,
              1160001,
              1288001,
              1544001,
              2056001,
              2312001)
        )
    )
    namedValues = NamedValues(
        *(("n-1032000", 1032001),
          ("n-1160000", 1160001),
          ("n-1288000", 1288001),
          ("n-136000", 136001),
          ("n-1544000", 1544001),
          ("n-200000", 200001),
          ("n-2056000", 2056001),
          ("n-2312000", 2312001),
          ("n-264000", 264001),
          ("n-328000", 328001),
          ("n-392000", 392001),
          ("n-520000", 520001),
          ("n-72000", 72001),
          ("n-776000", 776001))
    )


_Hdsl2NetworkProfile_LineConfig_MinRate_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_MinRate_Object = MibScalar
hdsl2NetworkProfile_LineConfig_MinRate = _Hdsl2NetworkProfile_LineConfig_MinRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 32),
    _Hdsl2NetworkProfile_LineConfig_MinRate_Type()
)
hdsl2NetworkProfile_LineConfig_MinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_MinRate.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_MaxRate_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(72001,
              136001,
              200001,
              264001,
              328001,
              392001,
              520001,
              776001,
              1032001,
              1160001,
              1288001,
              1544001,
              2056001,
              2312001)
        )
    )
    namedValues = NamedValues(
        *(("n-1032000", 1032001),
          ("n-1160000", 1160001),
          ("n-1288000", 1288001),
          ("n-136000", 136001),
          ("n-1544000", 1544001),
          ("n-200000", 200001),
          ("n-2056000", 2056001),
          ("n-2312000", 2312001),
          ("n-264000", 264001),
          ("n-328000", 328001),
          ("n-392000", 392001),
          ("n-520000", 520001),
          ("n-72000", 72001),
          ("n-776000", 776001))
    )


_Hdsl2NetworkProfile_LineConfig_MaxRate_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_MaxRate_Object = MibScalar
hdsl2NetworkProfile_LineConfig_MaxRate = _Hdsl2NetworkProfile_LineConfig_MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 33),
    _Hdsl2NetworkProfile_LineConfig_MaxRate_Type()
)
hdsl2NetworkProfile_LineConfig_MaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_MaxRate.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 3),
          ("europeanAnnexB", 2),
          ("northAmericanAnnexA", 1))
    )


_Hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType_Object = MibScalar
hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType = _Hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 34),
    _Hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType_Type()
)
hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_GshdslPsdType_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_GshdslPsdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric1544kPsdAnnexA", 5),
          ("asymmetric2056kPsdAnnexB", 6),
          ("asymmetric2312kPsdAnnexB", 7),
          ("asymmetric776kPsdAnnexA", 4),
          ("autoDetect", 8),
          ("symmetric", 1))
    )


_Hdsl2NetworkProfile_LineConfig_GshdslPsdType_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_GshdslPsdType_Object = MibScalar
hdsl2NetworkProfile_LineConfig_GshdslPsdType = _Hdsl2NetworkProfile_LineConfig_GshdslPsdType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 35),
    _Hdsl2NetworkProfile_LineConfig_GshdslPsdType_Type()
)
hdsl2NetworkProfile_LineConfig_GshdslPsdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_GshdslPsdType.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile_Type = DisplayString
_Hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile = _Hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 36),
    _Hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile_Type()
)
hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile_Type = DisplayString
_Hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile = _Hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 37),
    _Hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile_Type()
)
hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile_Type = DisplayString
_Hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile = _Hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 38),
    _Hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile_Type()
)
hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_SnextMargin_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_SnextMargin based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("disable", 22),
          ("n-0db", 1),
          ("n-10db", 11),
          ("n-1db", 2),
          ("n-2db", 3),
          ("n-3db", 4),
          ("n-4db", 5),
          ("n-5db", 6),
          ("n-6db", 7),
          ("n-7db", 8),
          ("n-8db", 9),
          ("n-9db", 10),
          ("n-plus-10db", 12),
          ("n-plus-1db", 21),
          ("n-plus-2db", 20),
          ("n-plus-3db", 19),
          ("n-plus-4db", 18),
          ("n-plus-5db", 17),
          ("n-plus-6db", 16),
          ("n-plus-7db", 15),
          ("n-plus-8db", 14),
          ("n-plus-9db", 13))
    )


_Hdsl2NetworkProfile_LineConfig_SnextMargin_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_SnextMargin_Object = MibScalar
hdsl2NetworkProfile_LineConfig_SnextMargin = _Hdsl2NetworkProfile_LineConfig_SnextMargin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 39),
    _Hdsl2NetworkProfile_LineConfig_SnextMargin_Type()
)
hdsl2NetworkProfile_LineConfig_SnextMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_SnextMargin.setStatus("mandatory")


class _Hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled_Type(Integer32):
    """Custom type hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled based on Integer32"""
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


_Hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled_Type.__name__ = "Integer32"
_Hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled_Object = MibScalar
hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled = _Hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 1, 1, 40),
    _Hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled_Type()
)
hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled.setStatus("mandatory")
_Mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable_Object = MibTable
mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable = _Mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2)
)
if mibBuilder.loadTexts:
    mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable.setStatus("mandatory")
_Mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry_Object = MibTableRow
mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry = _Mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1)
)
mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry.setIndexNames(
    (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Shelf-o"),
    (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Slot-o"),
    (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Item-o"),
    (0, "ASCEND-MIBHDSL2NET-MIB", "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Index-o"),
)
if mibBuilder.loadTexts:
    mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o_Type = Integer32
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o = _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 1),
    _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o_Type()
)
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o_Type = Integer32
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o = _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 2),
    _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o_Type()
)
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o_Type = Integer32
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o = _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 3),
    _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o_Type()
)
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o_Type = Integer32
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o = _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 4),
    _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o_Type()
)
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile_Type = DisplayString
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile = _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 5),
    _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile_Type()
)
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile.setStatus("mandatory")
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile_Type = DisplayString
_Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile_Object = MibScalar
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile = _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 14, 2, 1, 6),
    _Hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile_Type()
)
hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBHDSL2NET-MIB",
    **{"DisplayString": DisplayString,
       "mibhdsl2NetworkProfile": mibhdsl2NetworkProfile,
       "mibhdsl2NetworkProfileTable": mibhdsl2NetworkProfileTable,
       "mibhdsl2NetworkProfileEntry": mibhdsl2NetworkProfileEntry,
       "hdsl2NetworkProfile-Shelf-o": hdsl2NetworkProfile_Shelf_o,
       "hdsl2NetworkProfile-Slot-o": hdsl2NetworkProfile_Slot_o,
       "hdsl2NetworkProfile-Item-o": hdsl2NetworkProfile_Item_o,
       "hdsl2NetworkProfile-Name": hdsl2NetworkProfile_Name,
       "hdsl2NetworkProfile-PhysicalAddress-Shelf": hdsl2NetworkProfile_PhysicalAddress_Shelf,
       "hdsl2NetworkProfile-PhysicalAddress-Slot": hdsl2NetworkProfile_PhysicalAddress_Slot,
       "hdsl2NetworkProfile-PhysicalAddress-ItemNumber": hdsl2NetworkProfile_PhysicalAddress_ItemNumber,
       "hdsl2NetworkProfile-Enabled": hdsl2NetworkProfile_Enabled,
       "hdsl2NetworkProfile-ProfileNumber": hdsl2NetworkProfile_ProfileNumber,
       "hdsl2NetworkProfile-LineConfig-TrunkGroup": hdsl2NetworkProfile_LineConfig_TrunkGroup,
       "hdsl2NetworkProfile-LineConfig-NailedGroup": hdsl2NetworkProfile_LineConfig_NailedGroup,
       "hdsl2NetworkProfile-LineConfig-VpSwitchingVpi": hdsl2NetworkProfile_LineConfig_VpSwitchingVpi,
       "hdsl2NetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "hdsl2NetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": hdsl2NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "hdsl2NetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": hdsl2NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "hdsl2NetworkProfile-LineConfig-Activation": hdsl2NetworkProfile_LineConfig_Activation,
       "hdsl2NetworkProfile-LineConfig-CallRouteInfo-Shelf": hdsl2NetworkProfile_LineConfig_CallRouteInfo_Shelf,
       "hdsl2NetworkProfile-LineConfig-CallRouteInfo-Slot": hdsl2NetworkProfile_LineConfig_CallRouteInfo_Slot,
       "hdsl2NetworkProfile-LineConfig-CallRouteInfo-ItemNumber": hdsl2NetworkProfile_LineConfig_CallRouteInfo_ItemNumber,
       "hdsl2NetworkProfile-LineConfig-UnitType": hdsl2NetworkProfile_LineConfig_UnitType,
       "hdsl2NetworkProfile-Action-o": hdsl2NetworkProfile_Action_o,
       "hdsl2NetworkProfile-SparingMode": hdsl2NetworkProfile_SparingMode,
       "hdsl2NetworkProfile-LineConfig-NtrEnabled": hdsl2NetworkProfile_LineConfig_NtrEnabled,
       "hdsl2NetworkProfile-LineConfig-ClockSource": hdsl2NetworkProfile_LineConfig_ClockSource,
       "hdsl2NetworkProfile-LineConfig-ClockPriority": hdsl2NetworkProfile_LineConfig_ClockPriority,
       "hdsl2NetworkProfile-LineConfig-LoopBack": hdsl2NetworkProfile_LineConfig_LoopBack,
       "hdsl2NetworkProfile-IgnoreLineup": hdsl2NetworkProfile_IgnoreLineup,
       "hdsl2NetworkProfile-LineConfig-Margin": hdsl2NetworkProfile_LineConfig_Margin,
       "hdsl2NetworkProfile-LineConfig-RateMode": hdsl2NetworkProfile_LineConfig_RateMode,
       "hdsl2NetworkProfile-LineConfig-MinRate": hdsl2NetworkProfile_LineConfig_MinRate,
       "hdsl2NetworkProfile-LineConfig-MaxRate": hdsl2NetworkProfile_LineConfig_MaxRate,
       "hdsl2NetworkProfile-LineConfig-GshdslStandardNetworkType": hdsl2NetworkProfile_LineConfig_GshdslStandardNetworkType,
       "hdsl2NetworkProfile-LineConfig-GshdslPsdType": hdsl2NetworkProfile_LineConfig_GshdslPsdType,
       "hdsl2NetworkProfile-ThreshProfiles-SpanThreshProfile": hdsl2NetworkProfile_ThreshProfiles_SpanThreshProfile,
       "hdsl2NetworkProfile-ThreshProfiles-XtucThreshProfile": hdsl2NetworkProfile_ThreshProfiles_XtucThreshProfile,
       "hdsl2NetworkProfile-ThreshProfiles-XturThreshProfile": hdsl2NetworkProfile_ThreshProfiles_XturThreshProfile,
       "hdsl2NetworkProfile-LineConfig-SnextMargin": hdsl2NetworkProfile_LineConfig_SnextMargin,
       "hdsl2NetworkProfile-LineConfig-AnnexbAnfpEnabled": hdsl2NetworkProfile_LineConfig_AnnexbAnfpEnabled,
       "mibhdsl2NetworkProfile-ThreshProfiles-UnitThreshProfilesTable": mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesTable,
       "mibhdsl2NetworkProfile-ThreshProfiles-UnitThreshProfilesEntry": mibhdsl2NetworkProfile_ThreshProfiles_UnitThreshProfilesEntry,
       "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Shelf-o": hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Shelf_o,
       "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Slot-o": hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Slot_o,
       "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Item-o": hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Item_o,
       "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-Index-o": hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_Index_o,
       "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-XruNetThreshProfile": hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruNetThreshProfile,
       "hdsl2NetworkProfile-ThreshProfiles-UnitThreshProfiles-XruCustThreshProfile": hdsl2NetworkProfile_ThreshProfiles_UnitThreshProfiles_XruCustThreshProfile}
)
