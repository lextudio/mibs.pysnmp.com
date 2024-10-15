# SNMP MIB module (ASCEND-MIBDS3ATMNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDS3ATMNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:31 2024
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

_Mibds3AtmNetworkProfile_ObjectIdentity = ObjectIdentity
mibds3AtmNetworkProfile = _Mibds3AtmNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 13)
)
_Mibds3AtmNetworkProfileTable_Object = MibTable
mibds3AtmNetworkProfileTable = _Mibds3AtmNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1)
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfileTable.setStatus("mandatory")
_Mibds3AtmNetworkProfileEntry_Object = MibTableRow
mibds3AtmNetworkProfileEntry = _Mibds3AtmNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1)
)
mibds3AtmNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfileEntry.setStatus("mandatory")
_Ds3AtmNetworkProfile_Shelf_o_Type = Integer32
_Ds3AtmNetworkProfile_Shelf_o_Object = MibScalar
ds3AtmNetworkProfile_Shelf_o = _Ds3AtmNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 1),
    _Ds3AtmNetworkProfile_Shelf_o_Type()
)
ds3AtmNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_Shelf_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_Slot_o_Type = Integer32
_Ds3AtmNetworkProfile_Slot_o_Object = MibScalar
ds3AtmNetworkProfile_Slot_o = _Ds3AtmNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 2),
    _Ds3AtmNetworkProfile_Slot_o_Type()
)
ds3AtmNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_Slot_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_Item_o_Type = Integer32
_Ds3AtmNetworkProfile_Item_o_Object = MibScalar
ds3AtmNetworkProfile_Item_o = _Ds3AtmNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 3),
    _Ds3AtmNetworkProfile_Item_o_Type()
)
ds3AtmNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_Item_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_Name_Type = DisplayString
_Ds3AtmNetworkProfile_Name_Object = MibScalar
ds3AtmNetworkProfile_Name = _Ds3AtmNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 4),
    _Ds3AtmNetworkProfile_Name_Type()
)
ds3AtmNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_Name.setStatus("mandatory")


class _Ds3AtmNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_Ds3AtmNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
ds3AtmNetworkProfile_PhysicalAddress_Shelf = _Ds3AtmNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 5),
    _Ds3AtmNetworkProfile_PhysicalAddress_Shelf_Type()
)
ds3AtmNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _Ds3AtmNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_Ds3AtmNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
ds3AtmNetworkProfile_PhysicalAddress_Slot = _Ds3AtmNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 6),
    _Ds3AtmNetworkProfile_PhysicalAddress_Slot_Type()
)
ds3AtmNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_Ds3AtmNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_Ds3AtmNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
ds3AtmNetworkProfile_PhysicalAddress_ItemNumber = _Ds3AtmNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 7),
    _Ds3AtmNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
ds3AtmNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Ds3AtmNetworkProfile_Enabled_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_Enabled based on Integer32"""
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


_Ds3AtmNetworkProfile_Enabled_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_Enabled_Object = MibScalar
ds3AtmNetworkProfile_Enabled = _Ds3AtmNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 8),
    _Ds3AtmNetworkProfile_Enabled_Type()
)
ds3AtmNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_Enabled.setStatus("mandatory")


class _Ds3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_SparePhysicalAddress_Shelf based on Integer32"""
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


_Ds3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_SparePhysicalAddress_Shelf_Object = MibScalar
ds3AtmNetworkProfile_SparePhysicalAddress_Shelf = _Ds3AtmNetworkProfile_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 9),
    _Ds3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type()
)
ds3AtmNetworkProfile_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _Ds3AtmNetworkProfile_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_SparePhysicalAddress_Slot based on Integer32"""
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


_Ds3AtmNetworkProfile_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_SparePhysicalAddress_Slot_Object = MibScalar
ds3AtmNetworkProfile_SparePhysicalAddress_Slot = _Ds3AtmNetworkProfile_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 10),
    _Ds3AtmNetworkProfile_SparePhysicalAddress_Slot_Type()
)
ds3AtmNetworkProfile_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_SparePhysicalAddress_Slot.setStatus("mandatory")
_Ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Type = Integer32
_Ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Object = MibScalar
ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber = _Ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 11),
    _Ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Type()
)
ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _Ds3AtmNetworkProfile_SparingMode_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_SparingMode based on Integer32"""
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


_Ds3AtmNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_SparingMode_Object = MibScalar
ds3AtmNetworkProfile_SparingMode = _Ds3AtmNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 12),
    _Ds3AtmNetworkProfile_SparingMode_Type()
)
ds3AtmNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_SparingMode.setStatus("mandatory")
_Ds3AtmNetworkProfile_ProfileNumber_Type = Integer32
_Ds3AtmNetworkProfile_ProfileNumber_Object = MibScalar
ds3AtmNetworkProfile_ProfileNumber = _Ds3AtmNetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 13),
    _Ds3AtmNetworkProfile_ProfileNumber_Type()
)
ds3AtmNetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_ProfileNumber.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrunkGroup = _Ds3AtmNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 14),
    _Ds3AtmNetworkProfile_LineConfig_TrunkGroup_Type()
)
ds3AtmNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_NailedGroup = _Ds3AtmNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 15),
    _Ds3AtmNetworkProfile_LineConfig_NailedGroup_Type()
)
ds3AtmNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 16),
    _Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 17),
    _Ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _Ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 18),
    _Ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_Activation based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_Activation_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_Activation = _Ds3AtmNetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 19),
    _Ds3AtmNetworkProfile_LineConfig_Activation_Type()
)
ds3AtmNetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_Loopback_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("facilityLoopback", 2),
          ("localLoopback", 3),
          ("noLoopback", 1))
    )


_Ds3AtmNetworkProfile_LineConfig_Loopback_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_Loopback_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_Loopback = _Ds3AtmNetworkProfile_LineConfig_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 23),
    _Ds3AtmNetworkProfile_LineConfig_Loopback_Type()
)
ds3AtmNetworkProfile_LineConfig_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_Loopback.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_HighTxOutput_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_HighTxOutput based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_HighTxOutput_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_HighTxOutput_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_HighTxOutput = _Ds3AtmNetworkProfile_LineConfig_HighTxOutput_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 24),
    _Ds3AtmNetworkProfile_LineConfig_HighTxOutput_Type()
)
ds3AtmNetworkProfile_LineConfig_HighTxOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_HighTxOutput.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_FramerMode_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_FramerMode based on Integer32"""
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
        *(("cBITPLCP", 2),
          ("cBitADM", 1),
          ("cBitAdmFrameLocked", 5),
          ("cBitAdmLoopTimed", 3),
          ("cBitPlcpFrameLocked", 6),
          ("cBitPlcpLoopTimed", 4))
    )


_Ds3AtmNetworkProfile_LineConfig_FramerMode_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_FramerMode_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_FramerMode = _Ds3AtmNetworkProfile_LineConfig_FramerMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 25),
    _Ds3AtmNetworkProfile_LineConfig_FramerMode_Type()
)
ds3AtmNetworkProfile_LineConfig_FramerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_FramerMode.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_VpiVciRange_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_VpiVciRange based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n-01-3232767", 1),
          ("n-0127-32511", 7),
          ("n-015-324095", 4),
          ("n-0255-32255", 8),
          ("n-03-3216383", 2),
          ("n-031-322047", 5),
          ("n-063-321023", 6),
          ("n-07-328191", 3),
          ("vpi0255Vci321023", 11),
          ("vpi0255Vci3216383", 15),
          ("vpi0255Vci322047", 12),
          ("vpi0255Vci32255", 9),
          ("vpi0255Vci324095", 13),
          ("vpi0255Vci32511", 10),
          ("vpi0255Vci328191", 14))
    )


_Ds3AtmNetworkProfile_LineConfig_VpiVciRange_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_VpiVciRange_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_VpiVciRange = _Ds3AtmNetworkProfile_LineConfig_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 26),
    _Ds3AtmNetworkProfile_LineConfig_VpiVciRange_Type()
)
ds3AtmNetworkProfile_LineConfig_VpiVciRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_VpiVciRange.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_ClockSource_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_ClockSource based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_ClockSource_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_ClockSource_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_ClockSource = _Ds3AtmNetworkProfile_LineConfig_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 27),
    _Ds3AtmNetworkProfile_LineConfig_ClockSource_Type()
)
ds3AtmNetworkProfile_LineConfig_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_ClockSource.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_ClockPriority_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_ClockPriority based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_ClockPriority_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_ClockPriority_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_ClockPriority = _Ds3AtmNetworkProfile_LineConfig_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 28),
    _Ds3AtmNetworkProfile_LineConfig_ClockPriority_Type()
)
ds3AtmNetworkProfile_LineConfig_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_ClockPriority.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_CellPayloadScramble_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_CellPayloadScramble based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_CellPayloadScramble_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_CellPayloadScramble_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_CellPayloadScramble = _Ds3AtmNetworkProfile_LineConfig_CellPayloadScramble_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 29),
    _Ds3AtmNetworkProfile_LineConfig_CellPayloadScramble_Type()
)
ds3AtmNetworkProfile_LineConfig_CellPayloadScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_CellPayloadScramble.setStatus("mandatory")


class _Ds3AtmNetworkProfile_Action_o_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_Action_o based on Integer32"""
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


_Ds3AtmNetworkProfile_Action_o_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_Action_o_Object = MibScalar
ds3AtmNetworkProfile_Action_o = _Ds3AtmNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 30),
    _Ds3AtmNetworkProfile_Action_o_Type()
)
ds3AtmNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_Action_o.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_ReceiveEqualization_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_ReceiveEqualization based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_ReceiveEqualization_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_ReceiveEqualization_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_ReceiveEqualization = _Ds3AtmNetworkProfile_LineConfig_ReceiveEqualization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 31),
    _Ds3AtmNetworkProfile_LineConfig_ReceiveEqualization_Type()
)
ds3AtmNetworkProfile_LineConfig_ReceiveEqualization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_ReceiveEqualization.setStatus("mandatory")


class _Ds3AtmNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_IgnoreLineup based on Integer32"""
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


_Ds3AtmNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_IgnoreLineup_Object = MibScalar
ds3AtmNetworkProfile_IgnoreLineup = _Ds3AtmNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 32),
    _Ds3AtmNetworkProfile_IgnoreLineup_Type()
)
ds3AtmNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_IgnoreLineup.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable = _Ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 1, 1, 33),
    _Ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type()
)
ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable.setStatus("mandatory")
_Mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable_Object = MibTable
mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable = _Mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2)
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable.setStatus("mandatory")
_Mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry_Object = MibTableRow
mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry = _Mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1)
)
mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry.setIndexNames(
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o"),
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 1),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 2),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 3),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 4),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 5),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 6),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 7),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 8),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 9),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority = _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 2, 1, 10),
    _Ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Type()
)
ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority.setStatus("mandatory")
_Mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable_Object = MibTable
mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable = _Mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3)
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable.setStatus("mandatory")
_Mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry_Object = MibTableRow
mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry = _Mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1)
)
mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry.setIndexNames(
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o"),
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 1),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 2),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 3),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 4),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o.setStatus("mandatory")


class _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type(Integer32):
    """Custom type ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled based on Integer32"""
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


_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type.__name__ = "Integer32"
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 5),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 6),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 7),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci = _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 3, 1, 8),
    _Ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Type()
)
ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci.setStatus("mandatory")
_Mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable_Object = MibTable
mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable = _Mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 4)
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable.setStatus("mandatory")
_Mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry_Object = MibTableRow
mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry = _Mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1)
)
mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry.setIndexNames(
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o"),
    (0, "ASCEND-MIBDS3ATMNET-MIB", "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o"),
)
if mibBuilder.loadTexts:
    mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o = _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 1),
    _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Type()
)
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o = _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 2),
    _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Type()
)
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o = _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 3),
    _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Type()
)
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o = _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 4),
    _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Type()
)
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o.setStatus("mandatory")
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Type = Integer32
_Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Object = MibScalar
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi = _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 13, 4, 1, 5),
    _Ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Type()
)
ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDS3ATMNET-MIB",
    **{"DisplayString": DisplayString,
       "mibds3AtmNetworkProfile": mibds3AtmNetworkProfile,
       "mibds3AtmNetworkProfileTable": mibds3AtmNetworkProfileTable,
       "mibds3AtmNetworkProfileEntry": mibds3AtmNetworkProfileEntry,
       "ds3AtmNetworkProfile-Shelf-o": ds3AtmNetworkProfile_Shelf_o,
       "ds3AtmNetworkProfile-Slot-o": ds3AtmNetworkProfile_Slot_o,
       "ds3AtmNetworkProfile-Item-o": ds3AtmNetworkProfile_Item_o,
       "ds3AtmNetworkProfile-Name": ds3AtmNetworkProfile_Name,
       "ds3AtmNetworkProfile-PhysicalAddress-Shelf": ds3AtmNetworkProfile_PhysicalAddress_Shelf,
       "ds3AtmNetworkProfile-PhysicalAddress-Slot": ds3AtmNetworkProfile_PhysicalAddress_Slot,
       "ds3AtmNetworkProfile-PhysicalAddress-ItemNumber": ds3AtmNetworkProfile_PhysicalAddress_ItemNumber,
       "ds3AtmNetworkProfile-Enabled": ds3AtmNetworkProfile_Enabled,
       "ds3AtmNetworkProfile-SparePhysicalAddress-Shelf": ds3AtmNetworkProfile_SparePhysicalAddress_Shelf,
       "ds3AtmNetworkProfile-SparePhysicalAddress-Slot": ds3AtmNetworkProfile_SparePhysicalAddress_Slot,
       "ds3AtmNetworkProfile-SparePhysicalAddress-ItemNumber": ds3AtmNetworkProfile_SparePhysicalAddress_ItemNumber,
       "ds3AtmNetworkProfile-SparingMode": ds3AtmNetworkProfile_SparingMode,
       "ds3AtmNetworkProfile-ProfileNumber": ds3AtmNetworkProfile_ProfileNumber,
       "ds3AtmNetworkProfile-LineConfig-TrunkGroup": ds3AtmNetworkProfile_LineConfig_TrunkGroup,
       "ds3AtmNetworkProfile-LineConfig-NailedGroup": ds3AtmNetworkProfile_LineConfig_NailedGroup,
       "ds3AtmNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "ds3AtmNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": ds3AtmNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "ds3AtmNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": ds3AtmNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "ds3AtmNetworkProfile-LineConfig-Activation": ds3AtmNetworkProfile_LineConfig_Activation,
       "ds3AtmNetworkProfile-LineConfig-Loopback": ds3AtmNetworkProfile_LineConfig_Loopback,
       "ds3AtmNetworkProfile-LineConfig-HighTxOutput": ds3AtmNetworkProfile_LineConfig_HighTxOutput,
       "ds3AtmNetworkProfile-LineConfig-FramerMode": ds3AtmNetworkProfile_LineConfig_FramerMode,
       "ds3AtmNetworkProfile-LineConfig-VpiVciRange": ds3AtmNetworkProfile_LineConfig_VpiVciRange,
       "ds3AtmNetworkProfile-LineConfig-ClockSource": ds3AtmNetworkProfile_LineConfig_ClockSource,
       "ds3AtmNetworkProfile-LineConfig-ClockPriority": ds3AtmNetworkProfile_LineConfig_ClockPriority,
       "ds3AtmNetworkProfile-LineConfig-CellPayloadScramble": ds3AtmNetworkProfile_LineConfig_CellPayloadScramble,
       "ds3AtmNetworkProfile-Action-o": ds3AtmNetworkProfile_Action_o,
       "ds3AtmNetworkProfile-LineConfig-ReceiveEqualization": ds3AtmNetworkProfile_LineConfig_ReceiveEqualization,
       "ds3AtmNetworkProfile-IgnoreLineup": ds3AtmNetworkProfile_IgnoreLineup,
       "ds3AtmNetworkProfile-LineConfig-StatusChangeTrapEnable": ds3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable,
       "mibds3AtmNetworkProfile-LineConfig-TrafficShapersTable": mibds3AtmNetworkProfile_LineConfig_TrafficShapersTable,
       "mibds3AtmNetworkProfile-LineConfig-TrafficShapersEntry": mibds3AtmNetworkProfile_LineConfig_TrafficShapersEntry,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o": ds3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o": ds3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o": ds3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o": ds3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Enabled": ds3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-BitRate": ds3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-PeakRate": ds3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-MaxBurstSize": ds3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Aggregate": ds3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate,
       "ds3AtmNetworkProfile-LineConfig-TrafficShapers-Priority": ds3AtmNetworkProfile_LineConfig_TrafficShapers_Priority,
       "mibds3AtmNetworkProfile-LineConfig-IncomingVCCsTable": mibds3AtmNetworkProfile_LineConfig_IncomingVCCsTable,
       "mibds3AtmNetworkProfile-LineConfig-IncomingVCCsEntry": mibds3AtmNetworkProfile_LineConfig_IncomingVCCsEntry,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Enabled": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-Vpi": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-StartVci": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci,
       "ds3AtmNetworkProfile-LineConfig-IncomingVCCs-EndVci": ds3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci,
       "mibds3AtmNetworkProfile-LineConfig-VcSwitchingVpiTable": mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable,
       "mibds3AtmNetworkProfile-LineConfig-VcSwitchingVpiEntry": mibds3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry,
       "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o": ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o,
       "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o": ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o,
       "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o": ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o,
       "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o": ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o,
       "ds3AtmNetworkProfile-LineConfig-VcSwitchingVpi": ds3AtmNetworkProfile_LineConfig_VcSwitchingVpi}
)
