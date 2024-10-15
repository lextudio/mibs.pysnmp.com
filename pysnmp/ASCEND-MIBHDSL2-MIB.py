# SNMP MIB module (ASCEND-MIBHDSL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBHDSL2-MIB
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

_Mibhdsl2DslLineStatus_ObjectIdentity = ObjectIdentity
mibhdsl2DslLineStatus = _Mibhdsl2DslLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 159)
)
_Mibhdsl2DslLineStatusTable_Object = MibTable
mibhdsl2DslLineStatusTable = _Mibhdsl2DslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1)
)
if mibBuilder.loadTexts:
    mibhdsl2DslLineStatusTable.setStatus("mandatory")
_Mibhdsl2DslLineStatusEntry_Object = MibTableRow
mibhdsl2DslLineStatusEntry = _Mibhdsl2DslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1)
)
mibhdsl2DslLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBHDSL2-MIB", "hdsl2DslLineStatus-Shelf-o"),
    (0, "ASCEND-MIBHDSL2-MIB", "hdsl2DslLineStatus-Slot-o"),
    (0, "ASCEND-MIBHDSL2-MIB", "hdsl2DslLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibhdsl2DslLineStatusEntry.setStatus("mandatory")
_Hdsl2DslLineStatus_Shelf_o_Type = Integer32
_Hdsl2DslLineStatus_Shelf_o_Object = MibScalar
hdsl2DslLineStatus_Shelf_o = _Hdsl2DslLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 1),
    _Hdsl2DslLineStatus_Shelf_o_Type()
)
hdsl2DslLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_Shelf_o.setStatus("mandatory")
_Hdsl2DslLineStatus_Slot_o_Type = Integer32
_Hdsl2DslLineStatus_Slot_o_Object = MibScalar
hdsl2DslLineStatus_Slot_o = _Hdsl2DslLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 2),
    _Hdsl2DslLineStatus_Slot_o_Type()
)
hdsl2DslLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_Slot_o.setStatus("mandatory")
_Hdsl2DslLineStatus_Item_o_Type = Integer32
_Hdsl2DslLineStatus_Item_o_Object = MibScalar
hdsl2DslLineStatus_Item_o = _Hdsl2DslLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 3),
    _Hdsl2DslLineStatus_Item_o_Type()
)
hdsl2DslLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_Item_o.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_Hdsl2DslLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalAddress_Shelf_Object = MibScalar
hdsl2DslLineStatus_PhysicalAddress_Shelf = _Hdsl2DslLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 4),
    _Hdsl2DslLineStatus_PhysicalAddress_Shelf_Type()
)
hdsl2DslLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_Hdsl2DslLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalAddress_Slot_Object = MibScalar
hdsl2DslLineStatus_PhysicalAddress_Slot = _Hdsl2DslLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 5),
    _Hdsl2DslLineStatus_PhysicalAddress_Slot_Type()
)
hdsl2DslLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_Hdsl2DslLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
hdsl2DslLineStatus_PhysicalAddress_ItemNumber = _Hdsl2DslLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 6),
    _Hdsl2DslLineStatus_PhysicalAddress_ItemNumber_Type()
)
hdsl2DslLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Hdsl2DslLineStatus_LineState_Type(Integer32):
    """Custom type hdsl2DslLineStatus_LineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("disabled", 2),
          ("doesNotExist", 1))
    )


_Hdsl2DslLineStatus_LineState_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_LineState_Object = MibScalar
hdsl2DslLineStatus_LineState = _Hdsl2DslLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 7),
    _Hdsl2DslLineStatus_LineState_Type()
)
hdsl2DslLineStatus_LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_LineState.setStatus("mandatory")


class _Hdsl2DslLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type hdsl2DslLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_Hdsl2DslLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
hdsl2DslLineStatus_SparePhysicalAddress_Shelf = _Hdsl2DslLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 8),
    _Hdsl2DslLineStatus_SparePhysicalAddress_Shelf_Type()
)
hdsl2DslLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _Hdsl2DslLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type hdsl2DslLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_Hdsl2DslLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
hdsl2DslLineStatus_SparePhysicalAddress_Slot = _Hdsl2DslLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 9),
    _Hdsl2DslLineStatus_SparePhysicalAddress_Slot_Type()
)
hdsl2DslLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_Hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_Hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber = _Hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 10),
    _Hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _Hdsl2DslLineStatus_SparingState_Type(Integer32):
    """Custom type hdsl2DslLineStatus_SparingState based on Integer32"""
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
        *(("primaryActive", 2),
          ("primaryInactive", 3),
          ("secondaryActive", 4),
          ("secondaryInactive", 5),
          ("sparingNone", 1))
    )


_Hdsl2DslLineStatus_SparingState_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_SparingState_Object = MibScalar
hdsl2DslLineStatus_SparingState = _Hdsl2DslLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 11),
    _Hdsl2DslLineStatus_SparingState_Type()
)
hdsl2DslLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_SparingState.setStatus("mandatory")


class _Hdsl2DslLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type hdsl2DslLineStatus_SparingChangeReason based on Integer32"""
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
        *(("automatic", 3),
          ("manual", 2),
          ("test", 4),
          ("unknown", 1))
    )


_Hdsl2DslLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_SparingChangeReason_Object = MibScalar
hdsl2DslLineStatus_SparingChangeReason = _Hdsl2DslLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 12),
    _Hdsl2DslLineStatus_SparingChangeReason_Type()
)
hdsl2DslLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_SparingChangeReason.setStatus("mandatory")
_Hdsl2DslLineStatus_SparingChangeTime_Type = Integer32
_Hdsl2DslLineStatus_SparingChangeTime_Object = MibScalar
hdsl2DslLineStatus_SparingChangeTime = _Hdsl2DslLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 13),
    _Hdsl2DslLineStatus_SparingChangeTime_Type()
)
hdsl2DslLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_SparingChangeTime.setStatus("mandatory")
_Hdsl2DslLineStatus_SparingChangeCounter_Type = Integer32
_Hdsl2DslLineStatus_SparingChangeCounter_Object = MibScalar
hdsl2DslLineStatus_SparingChangeCounter = _Hdsl2DslLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 14),
    _Hdsl2DslLineStatus_SparingChangeCounter_Type()
)
hdsl2DslLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_SparingChangeCounter.setStatus("mandatory")


class _Hdsl2DslLineStatus_VpiVciRange_Type(Integer32):
    """Custom type hdsl2DslLineStatus_VpiVciRange based on Integer32"""
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
        *(("notApplicable", 5),
          ("vpi015Vci32127", 3),
          ("vpi01Vci321023", 6),
          ("vpi031Vci3263", 4),
          ("vpi03Vci32511", 1),
          ("vpi07Vci32255", 2))
    )


_Hdsl2DslLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_VpiVciRange_Object = MibScalar
hdsl2DslLineStatus_VpiVciRange = _Hdsl2DslLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 15),
    _Hdsl2DslLineStatus_VpiVciRange_Type()
)
hdsl2DslLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_VpiVciRange.setStatus("mandatory")
_Hdsl2DslLineStatus_VpSwitchingVpi_Type = Integer32
_Hdsl2DslLineStatus_VpSwitchingVpi_Object = MibScalar
hdsl2DslLineStatus_VpSwitchingVpi = _Hdsl2DslLineStatus_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 16),
    _Hdsl2DslLineStatus_VpSwitchingVpi_Type()
)
hdsl2DslLineStatus_VpSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_VpSwitchingVpi.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex = _Hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 17),
    _Hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex_Type()
)
hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalStatus_UnitType_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalStatus_UnitType based on Integer32"""
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


_Hdsl2DslLineStatus_PhysicalStatus_UnitType_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalStatus_UnitType_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_UnitType = _Hdsl2DslLineStatus_PhysicalStatus_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 18),
    _Hdsl2DslLineStatus_PhysicalStatus_UnitType_Type()
)
hdsl2DslLineStatus_PhysicalStatus_UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_UnitType.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalStatus_InterfaceType_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalStatus_InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("gShdsl", 2),
          ("hdsl2", 3))
    )


_Hdsl2DslLineStatus_PhysicalStatus_InterfaceType_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalStatus_InterfaceType_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_InterfaceType = _Hdsl2DslLineStatus_PhysicalStatus_InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 19),
    _Hdsl2DslLineStatus_PhysicalStatus_InterfaceType_Type()
)
hdsl2DslLineStatus_PhysicalStatus_InterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_InterfaceType.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalStatus_DevLineState_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalStatus_DevLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("analogLoopback", 11),
          ("digitalLoopback", 12),
          ("down", 8),
          ("idle", 7),
          ("outOfService", 9),
          ("portUp", 2),
          ("startupDownload", 6),
          ("startupHandshake", 4),
          ("startupTraining", 5),
          ("test", 3),
          ("unknown", 10))
    )


_Hdsl2DslLineStatus_PhysicalStatus_DevLineState_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalStatus_DevLineState_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_DevLineState = _Hdsl2DslLineStatus_PhysicalStatus_DevLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 20),
    _Hdsl2DslLineStatus_PhysicalStatus_DevLineState_Type()
)
hdsl2DslLineStatus_PhysicalStatus_DevLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_DevLineState.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatus_OperationalRate_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatus_OperationalRate_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_OperationalRate = _Hdsl2DslLineStatus_PhysicalStatus_OperationalRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 21),
    _Hdsl2DslLineStatus_PhysicalStatus_OperationalRate_Type()
)
hdsl2DslLineStatus_PhysicalStatus_OperationalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_OperationalRate.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatus_FirmwareVer_Type = DisplayString
_Hdsl2DslLineStatus_PhysicalStatus_FirmwareVer_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_FirmwareVer = _Hdsl2DslLineStatus_PhysicalStatus_FirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 22),
    _Hdsl2DslLineStatus_PhysicalStatus_FirmwareVer_Type()
)
hdsl2DslLineStatus_PhysicalStatus_FirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_FirmwareVer.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatus_HardwareVer_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatus_HardwareVer_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_HardwareVer = _Hdsl2DslLineStatus_PhysicalStatus_HardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 23),
    _Hdsl2DslLineStatus_PhysicalStatus_HardwareVer_Type()
)
hdsl2DslLineStatus_PhysicalStatus_HardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_HardwareVer.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days = _Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 24),
    _Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours = _Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 25),
    _Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes = _Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 26),
    _Hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_Hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent = _Hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 27),
    _Hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_LineQuality_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_LineQuality_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_LineQuality = _Hdsl2DslLineStatus_PhysicalStatistic_LineQuality_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 28),
    _Hdsl2DslLineStatus_PhysicalStatistic_LineQuality_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_LineQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_LineQuality.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr = _Hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 29),
    _Hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalStatistic_SelfTest_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalStatistic_SelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localLoopBackFailed", 3),
          ("passed", 1),
          ("selfTestFailed", 2))
    )


_Hdsl2DslLineStatus_PhysicalStatistic_SelfTest_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalStatistic_SelfTest_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_SelfTest = _Hdsl2DslLineStatus_PhysicalStatistic_SelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 30),
    _Hdsl2DslLineStatus_PhysicalStatistic_SelfTest_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_SelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_SelfTest.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_TransmitPower_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_TransmitPower_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_TransmitPower = _Hdsl2DslLineStatus_PhysicalStatistic_TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 31),
    _Hdsl2DslLineStatus_PhysicalStatistic_TransmitPower_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_TransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_TransmitPower.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 2),
          ("outOfSync", 1))
    )


_Hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus = _Hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 32),
    _Hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_CodeViolations_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_CodeViolations_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_CodeViolations = _Hdsl2DslLineStatus_PhysicalStatistic_CodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 33),
    _Hdsl2DslLineStatus_PhysicalStatistic_CodeViolations_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_CodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_CodeViolations.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond = _Hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 34),
    _Hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond = _Hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 35),
    _Hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_LoswSecond_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_LoswSecond_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_LoswSecond = _Hdsl2DslLineStatus_PhysicalStatistic_LoswSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 36),
    _Hdsl2DslLineStatus_PhysicalStatistic_LoswSecond_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_LoswSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_LoswSecond.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond = _Hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 37),
    _Hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation = _Hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 38),
    _Hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation.setStatus("mandatory")


class _Hdsl2DslLineStatus_Action_o_Type(Integer32):
    """Custom type hdsl2DslLineStatus_Action_o based on Integer32"""
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


_Hdsl2DslLineStatus_Action_o_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_Action_o_Object = MibScalar
hdsl2DslLineStatus_Action_o = _Hdsl2DslLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 39),
    _Hdsl2DslLineStatus_Action_o_Type()
)
hdsl2DslLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_Action_o.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_Snr_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_Snr_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_Snr = _Hdsl2DslLineStatus_PhysicalStatistic_Snr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 40),
    _Hdsl2DslLineStatus_PhysicalStatistic_Snr_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_Snr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_Snr.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation = _Hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 41),
    _Hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation.setStatus("mandatory")
_Hdsl2DslLineStatus_PhysicalStatistic_SturSnr_Type = Integer32
_Hdsl2DslLineStatus_PhysicalStatistic_SturSnr_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatistic_SturSnr = _Hdsl2DslLineStatus_PhysicalStatistic_SturSnr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 42),
    _Hdsl2DslLineStatus_PhysicalStatistic_SturSnr_Type()
)
hdsl2DslLineStatus_PhysicalStatistic_SturSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatistic_SturSnr.setStatus("mandatory")


class _Hdsl2DslLineStatus_PhysicalStatus_NetworkType_Type(Integer32):
    """Custom type hdsl2DslLineStatus_PhysicalStatus_NetworkType based on Integer32"""
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


_Hdsl2DslLineStatus_PhysicalStatus_NetworkType_Type.__name__ = "Integer32"
_Hdsl2DslLineStatus_PhysicalStatus_NetworkType_Object = MibScalar
hdsl2DslLineStatus_PhysicalStatus_NetworkType = _Hdsl2DslLineStatus_PhysicalStatus_NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 159, 1, 1, 43),
    _Hdsl2DslLineStatus_PhysicalStatus_NetworkType_Type()
)
hdsl2DslLineStatus_PhysicalStatus_NetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2DslLineStatus_PhysicalStatus_NetworkType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBHDSL2-MIB",
    **{"DisplayString": DisplayString,
       "mibhdsl2DslLineStatus": mibhdsl2DslLineStatus,
       "mibhdsl2DslLineStatusTable": mibhdsl2DslLineStatusTable,
       "mibhdsl2DslLineStatusEntry": mibhdsl2DslLineStatusEntry,
       "hdsl2DslLineStatus-Shelf-o": hdsl2DslLineStatus_Shelf_o,
       "hdsl2DslLineStatus-Slot-o": hdsl2DslLineStatus_Slot_o,
       "hdsl2DslLineStatus-Item-o": hdsl2DslLineStatus_Item_o,
       "hdsl2DslLineStatus-PhysicalAddress-Shelf": hdsl2DslLineStatus_PhysicalAddress_Shelf,
       "hdsl2DslLineStatus-PhysicalAddress-Slot": hdsl2DslLineStatus_PhysicalAddress_Slot,
       "hdsl2DslLineStatus-PhysicalAddress-ItemNumber": hdsl2DslLineStatus_PhysicalAddress_ItemNumber,
       "hdsl2DslLineStatus-LineState": hdsl2DslLineStatus_LineState,
       "hdsl2DslLineStatus-SparePhysicalAddress-Shelf": hdsl2DslLineStatus_SparePhysicalAddress_Shelf,
       "hdsl2DslLineStatus-SparePhysicalAddress-Slot": hdsl2DslLineStatus_SparePhysicalAddress_Slot,
       "hdsl2DslLineStatus-SparePhysicalAddress-ItemNumber": hdsl2DslLineStatus_SparePhysicalAddress_ItemNumber,
       "hdsl2DslLineStatus-SparingState": hdsl2DslLineStatus_SparingState,
       "hdsl2DslLineStatus-SparingChangeReason": hdsl2DslLineStatus_SparingChangeReason,
       "hdsl2DslLineStatus-SparingChangeTime": hdsl2DslLineStatus_SparingChangeTime,
       "hdsl2DslLineStatus-SparingChangeCounter": hdsl2DslLineStatus_SparingChangeCounter,
       "hdsl2DslLineStatus-VpiVciRange": hdsl2DslLineStatus_VpiVciRange,
       "hdsl2DslLineStatus-VpSwitchingVpi": hdsl2DslLineStatus_VpSwitchingVpi,
       "hdsl2DslLineStatus-PhysicalStatus-IfGroupIndex": hdsl2DslLineStatus_PhysicalStatus_IfGroupIndex,
       "hdsl2DslLineStatus-PhysicalStatus-UnitType": hdsl2DslLineStatus_PhysicalStatus_UnitType,
       "hdsl2DslLineStatus-PhysicalStatus-InterfaceType": hdsl2DslLineStatus_PhysicalStatus_InterfaceType,
       "hdsl2DslLineStatus-PhysicalStatus-DevLineState": hdsl2DslLineStatus_PhysicalStatus_DevLineState,
       "hdsl2DslLineStatus-PhysicalStatus-OperationalRate": hdsl2DslLineStatus_PhysicalStatus_OperationalRate,
       "hdsl2DslLineStatus-PhysicalStatus-FirmwareVer": hdsl2DslLineStatus_PhysicalStatus_FirmwareVer,
       "hdsl2DslLineStatus-PhysicalStatus-HardwareVer": hdsl2DslLineStatus_PhysicalStatus_HardwareVer,
       "hdsl2DslLineStatus-PhysicalStatistic-LineUpTimer-Days": hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Days,
       "hdsl2DslLineStatus-PhysicalStatistic-LineUpTimer-Hours": hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Hours,
       "hdsl2DslLineStatus-PhysicalStatistic-LineUpTimer-Minutes": hdsl2DslLineStatus_PhysicalStatistic_LineUpTimer_Minutes,
       "hdsl2DslLineStatus-PhysicalStatistic-RxSignalPresent": hdsl2DslLineStatus_PhysicalStatistic_RxSignalPresent,
       "hdsl2DslLineStatus-PhysicalStatistic-LineQuality": hdsl2DslLineStatus_PhysicalStatistic_LineQuality,
       "hdsl2DslLineStatus-PhysicalStatistic-UpDwnCntr": hdsl2DslLineStatus_PhysicalStatistic_UpDwnCntr,
       "hdsl2DslLineStatus-PhysicalStatistic-SelfTest": hdsl2DslLineStatus_PhysicalStatistic_SelfTest,
       "hdsl2DslLineStatus-PhysicalStatistic-TransmitPower": hdsl2DslLineStatus_PhysicalStatistic_TransmitPower,
       "hdsl2DslLineStatus-PhysicalStatistic-FramerSyncStatus": hdsl2DslLineStatus_PhysicalStatistic_FramerSyncStatus,
       "hdsl2DslLineStatus-PhysicalStatistic-CodeViolations": hdsl2DslLineStatus_PhysicalStatistic_CodeViolations,
       "hdsl2DslLineStatus-PhysicalStatistic-ErroredSecond": hdsl2DslLineStatus_PhysicalStatistic_ErroredSecond,
       "hdsl2DslLineStatus-PhysicalStatistic-SeverelyErroredSecond": hdsl2DslLineStatus_PhysicalStatistic_SeverelyErroredSecond,
       "hdsl2DslLineStatus-PhysicalStatistic-LoswSecond": hdsl2DslLineStatus_PhysicalStatistic_LoswSecond,
       "hdsl2DslLineStatus-PhysicalStatistic-UnavailableSecond": hdsl2DslLineStatus_PhysicalStatistic_UnavailableSecond,
       "hdsl2DslLineStatus-PhysicalStatistic-LoopAttenuation": hdsl2DslLineStatus_PhysicalStatistic_LoopAttenuation,
       "hdsl2DslLineStatus-Action-o": hdsl2DslLineStatus_Action_o,
       "hdsl2DslLineStatus-PhysicalStatistic-Snr": hdsl2DslLineStatus_PhysicalStatistic_Snr,
       "hdsl2DslLineStatus-PhysicalStatistic-SturLoopAttenuation": hdsl2DslLineStatus_PhysicalStatistic_SturLoopAttenuation,
       "hdsl2DslLineStatus-PhysicalStatistic-SturSnr": hdsl2DslLineStatus_PhysicalStatistic_SturSnr,
       "hdsl2DslLineStatus-PhysicalStatus-NetworkType": hdsl2DslLineStatus_PhysicalStatus_NetworkType}
)
