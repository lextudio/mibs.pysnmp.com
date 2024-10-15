# SNMP MIB module (ASCEND-MIBSHDSLNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSHDSLNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:11 2024
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

_MibshdslNetworkProfile_ObjectIdentity = ObjectIdentity
mibshdslNetworkProfile = _MibshdslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 147)
)
_MibshdslNetworkProfileTable_Object = MibTable
mibshdslNetworkProfileTable = _MibshdslNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1)
)
if mibBuilder.loadTexts:
    mibshdslNetworkProfileTable.setStatus("mandatory")
_MibshdslNetworkProfileEntry_Object = MibTableRow
mibshdslNetworkProfileEntry = _MibshdslNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1)
)
mibshdslNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSHDSLNET-MIB", "shdslNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBSHDSLNET-MIB", "shdslNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBSHDSLNET-MIB", "shdslNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibshdslNetworkProfileEntry.setStatus("mandatory")
_ShdslNetworkProfile_Shelf_o_Type = Integer32
_ShdslNetworkProfile_Shelf_o_Object = MibScalar
shdslNetworkProfile_Shelf_o = _ShdslNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 1),
    _ShdslNetworkProfile_Shelf_o_Type()
)
shdslNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslNetworkProfile_Shelf_o.setStatus("mandatory")
_ShdslNetworkProfile_Slot_o_Type = Integer32
_ShdslNetworkProfile_Slot_o_Object = MibScalar
shdslNetworkProfile_Slot_o = _ShdslNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 2),
    _ShdslNetworkProfile_Slot_o_Type()
)
shdslNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslNetworkProfile_Slot_o.setStatus("mandatory")
_ShdslNetworkProfile_Item_o_Type = Integer32
_ShdslNetworkProfile_Item_o_Object = MibScalar
shdslNetworkProfile_Item_o = _ShdslNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 3),
    _ShdslNetworkProfile_Item_o_Type()
)
shdslNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslNetworkProfile_Item_o.setStatus("mandatory")
_ShdslNetworkProfile_Name_Type = DisplayString
_ShdslNetworkProfile_Name_Object = MibScalar
shdslNetworkProfile_Name = _ShdslNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 4),
    _ShdslNetworkProfile_Name_Type()
)
shdslNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_Name.setStatus("mandatory")


class _ShdslNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type shdslNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_ShdslNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_ShdslNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
shdslNetworkProfile_PhysicalAddress_Shelf = _ShdslNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 5),
    _ShdslNetworkProfile_PhysicalAddress_Shelf_Type()
)
shdslNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _ShdslNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type shdslNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_ShdslNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_ShdslNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
shdslNetworkProfile_PhysicalAddress_Slot = _ShdslNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 6),
    _ShdslNetworkProfile_PhysicalAddress_Slot_Type()
)
shdslNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_ShdslNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_ShdslNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
shdslNetworkProfile_PhysicalAddress_ItemNumber = _ShdslNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 7),
    _ShdslNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
shdslNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _ShdslNetworkProfile_Enabled_Type(Integer32):
    """Custom type shdslNetworkProfile_Enabled based on Integer32"""
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


_ShdslNetworkProfile_Enabled_Type.__name__ = "Integer32"
_ShdslNetworkProfile_Enabled_Object = MibScalar
shdslNetworkProfile_Enabled = _ShdslNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 8),
    _ShdslNetworkProfile_Enabled_Type()
)
shdslNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_Enabled.setStatus("mandatory")


class _ShdslNetworkProfile_SparingMode_Type(Integer32):
    """Custom type shdslNetworkProfile_SparingMode based on Integer32"""
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


_ShdslNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_ShdslNetworkProfile_SparingMode_Object = MibScalar
shdslNetworkProfile_SparingMode = _ShdslNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 9),
    _ShdslNetworkProfile_SparingMode_Type()
)
shdslNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_SparingMode.setStatus("mandatory")


class _ShdslNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type shdslNetworkProfile_IgnoreLineup based on Integer32"""
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


_ShdslNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_ShdslNetworkProfile_IgnoreLineup_Object = MibScalar
shdslNetworkProfile_IgnoreLineup = _ShdslNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 10),
    _ShdslNetworkProfile_IgnoreLineup_Type()
)
shdslNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_IgnoreLineup.setStatus("mandatory")
_ShdslNetworkProfile_ProfileNumber_Type = Integer32
_ShdslNetworkProfile_ProfileNumber_Object = MibScalar
shdslNetworkProfile_ProfileNumber = _ShdslNetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 11),
    _ShdslNetworkProfile_ProfileNumber_Type()
)
shdslNetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_ProfileNumber.setStatus("mandatory")
_ShdslNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_ShdslNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
shdslNetworkProfile_LineConfig_TrunkGroup = _ShdslNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 12),
    _ShdslNetworkProfile_LineConfig_TrunkGroup_Type()
)
shdslNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_ShdslNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_ShdslNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
shdslNetworkProfile_LineConfig_NailedGroup = _ShdslNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 13),
    _ShdslNetworkProfile_LineConfig_NailedGroup_Type()
)
shdslNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_ShdslNetworkProfile_LineConfig_VpSwitchingVpi_Type = Integer32
_ShdslNetworkProfile_LineConfig_VpSwitchingVpi_Object = MibScalar
shdslNetworkProfile_LineConfig_VpSwitchingVpi = _ShdslNetworkProfile_LineConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 14),
    _ShdslNetworkProfile_LineConfig_VpSwitchingVpi_Type()
)
shdslNetworkProfile_LineConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus("mandatory")
_ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 15),
    _ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 16),
    _ShdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_ShdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_ShdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _ShdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 17),
    _ShdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_Activation based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_Activation_Object = MibScalar
shdslNetworkProfile_LineConfig_Activation = _ShdslNetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 18),
    _ShdslNetworkProfile_LineConfig_Activation_Type()
)
shdslNetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_CallRouteInfo_Shelf_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_CallRouteInfo_Shelf_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_CallRouteInfo_Shelf_Object = MibScalar
shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf = _ShdslNetworkProfile_LineConfig_CallRouteInfo_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 19),
    _ShdslNetworkProfile_LineConfig_CallRouteInfo_Shelf_Type()
)
shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_CallRouteInfo_Slot_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_CallRouteInfo_Slot based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_CallRouteInfo_Slot_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_CallRouteInfo_Slot_Object = MibScalar
shdslNetworkProfile_LineConfig_CallRouteInfo_Slot = _ShdslNetworkProfile_LineConfig_CallRouteInfo_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 20),
    _ShdslNetworkProfile_LineConfig_CallRouteInfo_Slot_Type()
)
shdslNetworkProfile_LineConfig_CallRouteInfo_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_CallRouteInfo_Slot.setStatus("mandatory")
_ShdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Type = Integer32
_ShdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Object = MibScalar
shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber = _ShdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 21),
    _ShdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber_Type()
)
shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_UnitType_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_UnitType based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_UnitType_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_UnitType_Object = MibScalar
shdslNetworkProfile_LineConfig_UnitType = _ShdslNetworkProfile_LineConfig_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 22),
    _ShdslNetworkProfile_LineConfig_UnitType_Type()
)
shdslNetworkProfile_LineConfig_UnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_UnitType.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_NtrEnabled_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_NtrEnabled based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_NtrEnabled_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_NtrEnabled_Object = MibScalar
shdslNetworkProfile_LineConfig_NtrEnabled = _ShdslNetworkProfile_LineConfig_NtrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 23),
    _ShdslNetworkProfile_LineConfig_NtrEnabled_Type()
)
shdslNetworkProfile_LineConfig_NtrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_NtrEnabled.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_ClockSource_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_ClockSource based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_ClockSource_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_ClockSource_Object = MibScalar
shdslNetworkProfile_LineConfig_ClockSource = _ShdslNetworkProfile_LineConfig_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 24),
    _ShdslNetworkProfile_LineConfig_ClockSource_Type()
)
shdslNetworkProfile_LineConfig_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_ClockSource.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_ClockPriority_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_ClockPriority based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_ClockPriority_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_ClockPriority_Object = MibScalar
shdslNetworkProfile_LineConfig_ClockPriority = _ShdslNetworkProfile_LineConfig_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 25),
    _ShdslNetworkProfile_LineConfig_ClockPriority_Type()
)
shdslNetworkProfile_LineConfig_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_ClockPriority.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_LoopBack_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_LoopBack based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_LoopBack_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_LoopBack_Object = MibScalar
shdslNetworkProfile_LineConfig_LoopBack = _ShdslNetworkProfile_LineConfig_LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 26),
    _ShdslNetworkProfile_LineConfig_LoopBack_Type()
)
shdslNetworkProfile_LineConfig_LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_LoopBack.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_Margin_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_Margin based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_Margin_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_Margin_Object = MibScalar
shdslNetworkProfile_LineConfig_Margin = _ShdslNetworkProfile_LineConfig_Margin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 27),
    _ShdslNetworkProfile_LineConfig_Margin_Type()
)
shdslNetworkProfile_LineConfig_Margin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_Margin.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_RateMode_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_RateMode based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_RateMode_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_RateMode_Object = MibScalar
shdslNetworkProfile_LineConfig_RateMode = _ShdslNetworkProfile_LineConfig_RateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 28),
    _ShdslNetworkProfile_LineConfig_RateMode_Type()
)
shdslNetworkProfile_LineConfig_RateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_RateMode.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_MinRate_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_MinRate based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_MinRate_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_MinRate_Object = MibScalar
shdslNetworkProfile_LineConfig_MinRate = _ShdslNetworkProfile_LineConfig_MinRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 29),
    _ShdslNetworkProfile_LineConfig_MinRate_Type()
)
shdslNetworkProfile_LineConfig_MinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_MinRate.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_MaxRate_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_MaxRate based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_MaxRate_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_MaxRate_Object = MibScalar
shdslNetworkProfile_LineConfig_MaxRate = _ShdslNetworkProfile_LineConfig_MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 30),
    _ShdslNetworkProfile_LineConfig_MaxRate_Type()
)
shdslNetworkProfile_LineConfig_MaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_MaxRate.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_GshdslStandardNetworkType_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_GshdslStandardNetworkType based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_GshdslStandardNetworkType_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_GshdslStandardNetworkType_Object = MibScalar
shdslNetworkProfile_LineConfig_GshdslStandardNetworkType = _ShdslNetworkProfile_LineConfig_GshdslStandardNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 31),
    _ShdslNetworkProfile_LineConfig_GshdslStandardNetworkType_Type()
)
shdslNetworkProfile_LineConfig_GshdslStandardNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_GshdslStandardNetworkType.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_GshdslPsdType_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_GshdslPsdType based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_GshdslPsdType_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_GshdslPsdType_Object = MibScalar
shdslNetworkProfile_LineConfig_GshdslPsdType = _ShdslNetworkProfile_LineConfig_GshdslPsdType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 32),
    _ShdslNetworkProfile_LineConfig_GshdslPsdType_Type()
)
shdslNetworkProfile_LineConfig_GshdslPsdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_GshdslPsdType.setStatus("mandatory")


class _ShdslNetworkProfile_Action_o_Type(Integer32):
    """Custom type shdslNetworkProfile_Action_o based on Integer32"""
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


_ShdslNetworkProfile_Action_o_Type.__name__ = "Integer32"
_ShdslNetworkProfile_Action_o_Object = MibScalar
shdslNetworkProfile_Action_o = _ShdslNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 33),
    _ShdslNetworkProfile_Action_o_Type()
)
shdslNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_Action_o.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_SnextMargin_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_SnextMargin based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_SnextMargin_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_SnextMargin_Object = MibScalar
shdslNetworkProfile_LineConfig_SnextMargin = _ShdslNetworkProfile_LineConfig_SnextMargin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 34),
    _ShdslNetworkProfile_LineConfig_SnextMargin_Type()
)
shdslNetworkProfile_LineConfig_SnextMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_SnextMargin.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_AnnexbAnfpEnabled_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_AnnexbAnfpEnabled_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_AnnexbAnfpEnabled_Object = MibScalar
shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled = _ShdslNetworkProfile_LineConfig_AnnexbAnfpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 35),
    _ShdslNetworkProfile_LineConfig_AnnexbAnfpEnabled_Type()
)
shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled.setStatus("mandatory")


class _ShdslNetworkProfile_LineConfig_MasterBindingPort_Type(Integer32):
    """Custom type shdslNetworkProfile_LineConfig_MasterBindingPort based on Integer32"""
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


_ShdslNetworkProfile_LineConfig_MasterBindingPort_Type.__name__ = "Integer32"
_ShdslNetworkProfile_LineConfig_MasterBindingPort_Object = MibScalar
shdslNetworkProfile_LineConfig_MasterBindingPort = _ShdslNetworkProfile_LineConfig_MasterBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 147, 1, 1, 36),
    _ShdslNetworkProfile_LineConfig_MasterBindingPort_Type()
)
shdslNetworkProfile_LineConfig_MasterBindingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslNetworkProfile_LineConfig_MasterBindingPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSHDSLNET-MIB",
    **{"DisplayString": DisplayString,
       "mibshdslNetworkProfile": mibshdslNetworkProfile,
       "mibshdslNetworkProfileTable": mibshdslNetworkProfileTable,
       "mibshdslNetworkProfileEntry": mibshdslNetworkProfileEntry,
       "shdslNetworkProfile-Shelf-o": shdslNetworkProfile_Shelf_o,
       "shdslNetworkProfile-Slot-o": shdslNetworkProfile_Slot_o,
       "shdslNetworkProfile-Item-o": shdslNetworkProfile_Item_o,
       "shdslNetworkProfile-Name": shdslNetworkProfile_Name,
       "shdslNetworkProfile-PhysicalAddress-Shelf": shdslNetworkProfile_PhysicalAddress_Shelf,
       "shdslNetworkProfile-PhysicalAddress-Slot": shdslNetworkProfile_PhysicalAddress_Slot,
       "shdslNetworkProfile-PhysicalAddress-ItemNumber": shdslNetworkProfile_PhysicalAddress_ItemNumber,
       "shdslNetworkProfile-Enabled": shdslNetworkProfile_Enabled,
       "shdslNetworkProfile-SparingMode": shdslNetworkProfile_SparingMode,
       "shdslNetworkProfile-IgnoreLineup": shdslNetworkProfile_IgnoreLineup,
       "shdslNetworkProfile-ProfileNumber": shdslNetworkProfile_ProfileNumber,
       "shdslNetworkProfile-LineConfig-TrunkGroup": shdslNetworkProfile_LineConfig_TrunkGroup,
       "shdslNetworkProfile-LineConfig-NailedGroup": shdslNetworkProfile_LineConfig_NailedGroup,
       "shdslNetworkProfile-LineConfig-VpSwitchingVpi": shdslNetworkProfile_LineConfig_VpSwitchingVpi,
       "shdslNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "shdslNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": shdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "shdslNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": shdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "shdslNetworkProfile-LineConfig-Activation": shdslNetworkProfile_LineConfig_Activation,
       "shdslNetworkProfile-LineConfig-CallRouteInfo-Shelf": shdslNetworkProfile_LineConfig_CallRouteInfo_Shelf,
       "shdslNetworkProfile-LineConfig-CallRouteInfo-Slot": shdslNetworkProfile_LineConfig_CallRouteInfo_Slot,
       "shdslNetworkProfile-LineConfig-CallRouteInfo-ItemNumber": shdslNetworkProfile_LineConfig_CallRouteInfo_ItemNumber,
       "shdslNetworkProfile-LineConfig-UnitType": shdslNetworkProfile_LineConfig_UnitType,
       "shdslNetworkProfile-LineConfig-NtrEnabled": shdslNetworkProfile_LineConfig_NtrEnabled,
       "shdslNetworkProfile-LineConfig-ClockSource": shdslNetworkProfile_LineConfig_ClockSource,
       "shdslNetworkProfile-LineConfig-ClockPriority": shdslNetworkProfile_LineConfig_ClockPriority,
       "shdslNetworkProfile-LineConfig-LoopBack": shdslNetworkProfile_LineConfig_LoopBack,
       "shdslNetworkProfile-LineConfig-Margin": shdslNetworkProfile_LineConfig_Margin,
       "shdslNetworkProfile-LineConfig-RateMode": shdslNetworkProfile_LineConfig_RateMode,
       "shdslNetworkProfile-LineConfig-MinRate": shdslNetworkProfile_LineConfig_MinRate,
       "shdslNetworkProfile-LineConfig-MaxRate": shdslNetworkProfile_LineConfig_MaxRate,
       "shdslNetworkProfile-LineConfig-GshdslStandardNetworkType": shdslNetworkProfile_LineConfig_GshdslStandardNetworkType,
       "shdslNetworkProfile-LineConfig-GshdslPsdType": shdslNetworkProfile_LineConfig_GshdslPsdType,
       "shdslNetworkProfile-Action-o": shdslNetworkProfile_Action_o,
       "shdslNetworkProfile-LineConfig-SnextMargin": shdslNetworkProfile_LineConfig_SnextMargin,
       "shdslNetworkProfile-LineConfig-AnnexbAnfpEnabled": shdslNetworkProfile_LineConfig_AnnexbAnfpEnabled,
       "shdslNetworkProfile-LineConfig-MasterBindingPort": shdslNetworkProfile_LineConfig_MasterBindingPort}
)
