# SNMP MIB module (ASCEND-MIBSHDSLSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSHDSLSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:12 2024
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

_MibshdslDslLineStatus_ObjectIdentity = ObjectIdentity
mibshdslDslLineStatus = _MibshdslDslLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 157)
)
_MibshdslDslLineStatusTable_Object = MibTable
mibshdslDslLineStatusTable = _MibshdslDslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1)
)
if mibBuilder.loadTexts:
    mibshdslDslLineStatusTable.setStatus("mandatory")
_MibshdslDslLineStatusEntry_Object = MibTableRow
mibshdslDslLineStatusEntry = _MibshdslDslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1)
)
mibshdslDslLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSHDSLSTAT-MIB", "shdslDslLineStatus-Shelf-o"),
    (0, "ASCEND-MIBSHDSLSTAT-MIB", "shdslDslLineStatus-Slot-o"),
    (0, "ASCEND-MIBSHDSLSTAT-MIB", "shdslDslLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibshdslDslLineStatusEntry.setStatus("mandatory")
_ShdslDslLineStatus_Shelf_o_Type = Integer32
_ShdslDslLineStatus_Shelf_o_Object = MibScalar
shdslDslLineStatus_Shelf_o = _ShdslDslLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 1),
    _ShdslDslLineStatus_Shelf_o_Type()
)
shdslDslLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_Shelf_o.setStatus("mandatory")
_ShdslDslLineStatus_Slot_o_Type = Integer32
_ShdslDslLineStatus_Slot_o_Object = MibScalar
shdslDslLineStatus_Slot_o = _ShdslDslLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 2),
    _ShdslDslLineStatus_Slot_o_Type()
)
shdslDslLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_Slot_o.setStatus("mandatory")
_ShdslDslLineStatus_Item_o_Type = Integer32
_ShdslDslLineStatus_Item_o_Object = MibScalar
shdslDslLineStatus_Item_o = _ShdslDslLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 3),
    _ShdslDslLineStatus_Item_o_Type()
)
shdslDslLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_Item_o.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_ShdslDslLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalAddress_Shelf_Object = MibScalar
shdslDslLineStatus_PhysicalAddress_Shelf = _ShdslDslLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 4),
    _ShdslDslLineStatus_PhysicalAddress_Shelf_Type()
)
shdslDslLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_ShdslDslLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalAddress_Slot_Object = MibScalar
shdslDslLineStatus_PhysicalAddress_Slot = _ShdslDslLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 5),
    _ShdslDslLineStatus_PhysicalAddress_Slot_Type()
)
shdslDslLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_ShdslDslLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
shdslDslLineStatus_PhysicalAddress_ItemNumber = _ShdslDslLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 6),
    _ShdslDslLineStatus_PhysicalAddress_ItemNumber_Type()
)
shdslDslLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _ShdslDslLineStatus_LineState_Type(Integer32):
    """Custom type shdslDslLineStatus_LineState based on Integer32"""
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


_ShdslDslLineStatus_LineState_Type.__name__ = "Integer32"
_ShdslDslLineStatus_LineState_Object = MibScalar
shdslDslLineStatus_LineState = _ShdslDslLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 7),
    _ShdslDslLineStatus_LineState_Type()
)
shdslDslLineStatus_LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_LineState.setStatus("mandatory")


class _ShdslDslLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type shdslDslLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_ShdslDslLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_ShdslDslLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
shdslDslLineStatus_SparePhysicalAddress_Shelf = _ShdslDslLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 8),
    _ShdslDslLineStatus_SparePhysicalAddress_Shelf_Type()
)
shdslDslLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslDslLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _ShdslDslLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type shdslDslLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_ShdslDslLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_ShdslDslLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
shdslDslLineStatus_SparePhysicalAddress_Slot = _ShdslDslLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 9),
    _ShdslDslLineStatus_SparePhysicalAddress_Slot_Type()
)
shdslDslLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslDslLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_ShdslDslLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_ShdslDslLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
shdslDslLineStatus_SparePhysicalAddress_ItemNumber = _ShdslDslLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 10),
    _ShdslDslLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
shdslDslLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslDslLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _ShdslDslLineStatus_SparingState_Type(Integer32):
    """Custom type shdslDslLineStatus_SparingState based on Integer32"""
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


_ShdslDslLineStatus_SparingState_Type.__name__ = "Integer32"
_ShdslDslLineStatus_SparingState_Object = MibScalar
shdslDslLineStatus_SparingState = _ShdslDslLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 11),
    _ShdslDslLineStatus_SparingState_Type()
)
shdslDslLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_SparingState.setStatus("mandatory")


class _ShdslDslLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type shdslDslLineStatus_SparingChangeReason based on Integer32"""
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


_ShdslDslLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_ShdslDslLineStatus_SparingChangeReason_Object = MibScalar
shdslDslLineStatus_SparingChangeReason = _ShdslDslLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 12),
    _ShdslDslLineStatus_SparingChangeReason_Type()
)
shdslDslLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_SparingChangeReason.setStatus("mandatory")
_ShdslDslLineStatus_SparingChangeTime_Type = Integer32
_ShdslDslLineStatus_SparingChangeTime_Object = MibScalar
shdslDslLineStatus_SparingChangeTime = _ShdslDslLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 13),
    _ShdslDslLineStatus_SparingChangeTime_Type()
)
shdslDslLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_SparingChangeTime.setStatus("mandatory")
_ShdslDslLineStatus_SparingChangeCounter_Type = Integer32
_ShdslDslLineStatus_SparingChangeCounter_Object = MibScalar
shdslDslLineStatus_SparingChangeCounter = _ShdslDslLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 14),
    _ShdslDslLineStatus_SparingChangeCounter_Type()
)
shdslDslLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_SparingChangeCounter.setStatus("mandatory")


class _ShdslDslLineStatus_VpiVciRange_Type(Integer32):
    """Custom type shdslDslLineStatus_VpiVciRange based on Integer32"""
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


_ShdslDslLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_ShdslDslLineStatus_VpiVciRange_Object = MibScalar
shdslDslLineStatus_VpiVciRange = _ShdslDslLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 15),
    _ShdslDslLineStatus_VpiVciRange_Type()
)
shdslDslLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_VpiVciRange.setStatus("mandatory")
_ShdslDslLineStatus_VpSwitchingVpi_Type = Integer32
_ShdslDslLineStatus_VpSwitchingVpi_Object = MibScalar
shdslDslLineStatus_VpSwitchingVpi = _ShdslDslLineStatus_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 16),
    _ShdslDslLineStatus_VpSwitchingVpi_Type()
)
shdslDslLineStatus_VpSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_VpSwitchingVpi.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatus_IfGroupIndex_Type = Integer32
_ShdslDslLineStatus_PhysicalStatus_IfGroupIndex_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_IfGroupIndex = _ShdslDslLineStatus_PhysicalStatus_IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 17),
    _ShdslDslLineStatus_PhysicalStatus_IfGroupIndex_Type()
)
shdslDslLineStatus_PhysicalStatus_IfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_IfGroupIndex.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalStatus_UnitType_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalStatus_UnitType based on Integer32"""
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


_ShdslDslLineStatus_PhysicalStatus_UnitType_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalStatus_UnitType_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_UnitType = _ShdslDslLineStatus_PhysicalStatus_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 18),
    _ShdslDslLineStatus_PhysicalStatus_UnitType_Type()
)
shdslDslLineStatus_PhysicalStatus_UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_UnitType.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalStatus_InterfaceType_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalStatus_InterfaceType based on Integer32"""
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


_ShdslDslLineStatus_PhysicalStatus_InterfaceType_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalStatus_InterfaceType_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_InterfaceType = _ShdslDslLineStatus_PhysicalStatus_InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 19),
    _ShdslDslLineStatus_PhysicalStatus_InterfaceType_Type()
)
shdslDslLineStatus_PhysicalStatus_InterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_InterfaceType.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalStatus_DevLineState_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalStatus_DevLineState based on Integer32"""
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


_ShdslDslLineStatus_PhysicalStatus_DevLineState_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalStatus_DevLineState_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_DevLineState = _ShdslDslLineStatus_PhysicalStatus_DevLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 20),
    _ShdslDslLineStatus_PhysicalStatus_DevLineState_Type()
)
shdslDslLineStatus_PhysicalStatus_DevLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_DevLineState.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatus_OperationalRate_Type = Integer32
_ShdslDslLineStatus_PhysicalStatus_OperationalRate_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_OperationalRate = _ShdslDslLineStatus_PhysicalStatus_OperationalRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 21),
    _ShdslDslLineStatus_PhysicalStatus_OperationalRate_Type()
)
shdslDslLineStatus_PhysicalStatus_OperationalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_OperationalRate.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatus_FirmwareVer_Type = DisplayString
_ShdslDslLineStatus_PhysicalStatus_FirmwareVer_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_FirmwareVer = _ShdslDslLineStatus_PhysicalStatus_FirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 22),
    _ShdslDslLineStatus_PhysicalStatus_FirmwareVer_Type()
)
shdslDslLineStatus_PhysicalStatus_FirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_FirmwareVer.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatus_HardwareVer_Type = Integer32
_ShdslDslLineStatus_PhysicalStatus_HardwareVer_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_HardwareVer = _ShdslDslLineStatus_PhysicalStatus_HardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 23),
    _ShdslDslLineStatus_PhysicalStatus_HardwareVer_Type()
)
shdslDslLineStatus_PhysicalStatus_HardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_HardwareVer.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days = _ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 24),
    _ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type()
)
shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours = _ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 25),
    _ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type()
)
shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes = _ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 26),
    _ShdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type()
)
shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalStatistic_RxSignalPresent_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalStatistic_RxSignalPresent based on Integer32"""
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


_ShdslDslLineStatus_PhysicalStatistic_RxSignalPresent_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalStatistic_RxSignalPresent_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_RxSignalPresent = _ShdslDslLineStatus_PhysicalStatistic_RxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 27),
    _ShdslDslLineStatus_PhysicalStatistic_RxSignalPresent_Type()
)
shdslDslLineStatus_PhysicalStatistic_RxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_RxSignalPresent.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_LineQuality_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_LineQuality_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_LineQuality = _ShdslDslLineStatus_PhysicalStatistic_LineQuality_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 28),
    _ShdslDslLineStatus_PhysicalStatistic_LineQuality_Type()
)
shdslDslLineStatus_PhysicalStatistic_LineQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_LineQuality.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_UpDwnCntr_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_UpDwnCntr_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_UpDwnCntr = _ShdslDslLineStatus_PhysicalStatistic_UpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 29),
    _ShdslDslLineStatus_PhysicalStatistic_UpDwnCntr_Type()
)
shdslDslLineStatus_PhysicalStatistic_UpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_UpDwnCntr.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalStatistic_SelfTest_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalStatistic_SelfTest based on Integer32"""
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


_ShdslDslLineStatus_PhysicalStatistic_SelfTest_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalStatistic_SelfTest_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_SelfTest = _ShdslDslLineStatus_PhysicalStatistic_SelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 30),
    _ShdslDslLineStatus_PhysicalStatistic_SelfTest_Type()
)
shdslDslLineStatus_PhysicalStatistic_SelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_SelfTest.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_TransmitPower_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_TransmitPower_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_TransmitPower = _ShdslDslLineStatus_PhysicalStatistic_TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 31),
    _ShdslDslLineStatus_PhysicalStatistic_TransmitPower_Type()
)
shdslDslLineStatus_PhysicalStatistic_TransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_TransmitPower.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalStatistic_FramerSyncStatus_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalStatistic_FramerSyncStatus based on Integer32"""
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


_ShdslDslLineStatus_PhysicalStatistic_FramerSyncStatus_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalStatistic_FramerSyncStatus_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_FramerSyncStatus = _ShdslDslLineStatus_PhysicalStatistic_FramerSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 32),
    _ShdslDslLineStatus_PhysicalStatistic_FramerSyncStatus_Type()
)
shdslDslLineStatus_PhysicalStatistic_FramerSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_FramerSyncStatus.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_CodeViolations_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_CodeViolations_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_CodeViolations = _ShdslDslLineStatus_PhysicalStatistic_CodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 33),
    _ShdslDslLineStatus_PhysicalStatistic_CodeViolations_Type()
)
shdslDslLineStatus_PhysicalStatistic_CodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_CodeViolations.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_ErroredSecond_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_ErroredSecond_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_ErroredSecond = _ShdslDslLineStatus_PhysicalStatistic_ErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 34),
    _ShdslDslLineStatus_PhysicalStatistic_ErroredSecond_Type()
)
shdslDslLineStatus_PhysicalStatistic_ErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_ErroredSecond.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond = _ShdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 35),
    _ShdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond_Type()
)
shdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_LoswSecond_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_LoswSecond_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_LoswSecond = _ShdslDslLineStatus_PhysicalStatistic_LoswSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 36),
    _ShdslDslLineStatus_PhysicalStatistic_LoswSecond_Type()
)
shdslDslLineStatus_PhysicalStatistic_LoswSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_LoswSecond.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_UnavailableSecond_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_UnavailableSecond_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_UnavailableSecond = _ShdslDslLineStatus_PhysicalStatistic_UnavailableSecond_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 37),
    _ShdslDslLineStatus_PhysicalStatistic_UnavailableSecond_Type()
)
shdslDslLineStatus_PhysicalStatistic_UnavailableSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_UnavailableSecond.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_LoopAttenuation_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_LoopAttenuation_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_LoopAttenuation = _ShdslDslLineStatus_PhysicalStatistic_LoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 38),
    _ShdslDslLineStatus_PhysicalStatistic_LoopAttenuation_Type()
)
shdslDslLineStatus_PhysicalStatistic_LoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_LoopAttenuation.setStatus("mandatory")


class _ShdslDslLineStatus_Action_o_Type(Integer32):
    """Custom type shdslDslLineStatus_Action_o based on Integer32"""
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


_ShdslDslLineStatus_Action_o_Type.__name__ = "Integer32"
_ShdslDslLineStatus_Action_o_Object = MibScalar
shdslDslLineStatus_Action_o = _ShdslDslLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 39),
    _ShdslDslLineStatus_Action_o_Type()
)
shdslDslLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslDslLineStatus_Action_o.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_Snr_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_Snr_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_Snr = _ShdslDslLineStatus_PhysicalStatistic_Snr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 40),
    _ShdslDslLineStatus_PhysicalStatistic_Snr_Type()
)
shdslDslLineStatus_PhysicalStatistic_Snr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_Snr.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation = _ShdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 41),
    _ShdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation_Type()
)
shdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation.setStatus("mandatory")
_ShdslDslLineStatus_PhysicalStatistic_SturSnr_Type = Integer32
_ShdslDslLineStatus_PhysicalStatistic_SturSnr_Object = MibScalar
shdslDslLineStatus_PhysicalStatistic_SturSnr = _ShdslDslLineStatus_PhysicalStatistic_SturSnr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 42),
    _ShdslDslLineStatus_PhysicalStatistic_SturSnr_Type()
)
shdslDslLineStatus_PhysicalStatistic_SturSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatistic_SturSnr.setStatus("mandatory")


class _ShdslDslLineStatus_PhysicalStatus_NetworkType_Type(Integer32):
    """Custom type shdslDslLineStatus_PhysicalStatus_NetworkType based on Integer32"""
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


_ShdslDslLineStatus_PhysicalStatus_NetworkType_Type.__name__ = "Integer32"
_ShdslDslLineStatus_PhysicalStatus_NetworkType_Object = MibScalar
shdslDslLineStatus_PhysicalStatus_NetworkType = _ShdslDslLineStatus_PhysicalStatus_NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 157, 1, 1, 43),
    _ShdslDslLineStatus_PhysicalStatus_NetworkType_Type()
)
shdslDslLineStatus_PhysicalStatus_NetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslDslLineStatus_PhysicalStatus_NetworkType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSHDSLSTAT-MIB",
    **{"DisplayString": DisplayString,
       "mibshdslDslLineStatus": mibshdslDslLineStatus,
       "mibshdslDslLineStatusTable": mibshdslDslLineStatusTable,
       "mibshdslDslLineStatusEntry": mibshdslDslLineStatusEntry,
       "shdslDslLineStatus-Shelf-o": shdslDslLineStatus_Shelf_o,
       "shdslDslLineStatus-Slot-o": shdslDslLineStatus_Slot_o,
       "shdslDslLineStatus-Item-o": shdslDslLineStatus_Item_o,
       "shdslDslLineStatus-PhysicalAddress-Shelf": shdslDslLineStatus_PhysicalAddress_Shelf,
       "shdslDslLineStatus-PhysicalAddress-Slot": shdslDslLineStatus_PhysicalAddress_Slot,
       "shdslDslLineStatus-PhysicalAddress-ItemNumber": shdslDslLineStatus_PhysicalAddress_ItemNumber,
       "shdslDslLineStatus-LineState": shdslDslLineStatus_LineState,
       "shdslDslLineStatus-SparePhysicalAddress-Shelf": shdslDslLineStatus_SparePhysicalAddress_Shelf,
       "shdslDslLineStatus-SparePhysicalAddress-Slot": shdslDslLineStatus_SparePhysicalAddress_Slot,
       "shdslDslLineStatus-SparePhysicalAddress-ItemNumber": shdslDslLineStatus_SparePhysicalAddress_ItemNumber,
       "shdslDslLineStatus-SparingState": shdslDslLineStatus_SparingState,
       "shdslDslLineStatus-SparingChangeReason": shdslDslLineStatus_SparingChangeReason,
       "shdslDslLineStatus-SparingChangeTime": shdslDslLineStatus_SparingChangeTime,
       "shdslDslLineStatus-SparingChangeCounter": shdslDslLineStatus_SparingChangeCounter,
       "shdslDslLineStatus-VpiVciRange": shdslDslLineStatus_VpiVciRange,
       "shdslDslLineStatus-VpSwitchingVpi": shdslDslLineStatus_VpSwitchingVpi,
       "shdslDslLineStatus-PhysicalStatus-IfGroupIndex": shdslDslLineStatus_PhysicalStatus_IfGroupIndex,
       "shdslDslLineStatus-PhysicalStatus-UnitType": shdslDslLineStatus_PhysicalStatus_UnitType,
       "shdslDslLineStatus-PhysicalStatus-InterfaceType": shdslDslLineStatus_PhysicalStatus_InterfaceType,
       "shdslDslLineStatus-PhysicalStatus-DevLineState": shdslDslLineStatus_PhysicalStatus_DevLineState,
       "shdslDslLineStatus-PhysicalStatus-OperationalRate": shdslDslLineStatus_PhysicalStatus_OperationalRate,
       "shdslDslLineStatus-PhysicalStatus-FirmwareVer": shdslDslLineStatus_PhysicalStatus_FirmwareVer,
       "shdslDslLineStatus-PhysicalStatus-HardwareVer": shdslDslLineStatus_PhysicalStatus_HardwareVer,
       "shdslDslLineStatus-PhysicalStatistic-LineUpTimer-Days": shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Days,
       "shdslDslLineStatus-PhysicalStatistic-LineUpTimer-Hours": shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Hours,
       "shdslDslLineStatus-PhysicalStatistic-LineUpTimer-Minutes": shdslDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes,
       "shdslDslLineStatus-PhysicalStatistic-RxSignalPresent": shdslDslLineStatus_PhysicalStatistic_RxSignalPresent,
       "shdslDslLineStatus-PhysicalStatistic-LineQuality": shdslDslLineStatus_PhysicalStatistic_LineQuality,
       "shdslDslLineStatus-PhysicalStatistic-UpDwnCntr": shdslDslLineStatus_PhysicalStatistic_UpDwnCntr,
       "shdslDslLineStatus-PhysicalStatistic-SelfTest": shdslDslLineStatus_PhysicalStatistic_SelfTest,
       "shdslDslLineStatus-PhysicalStatistic-TransmitPower": shdslDslLineStatus_PhysicalStatistic_TransmitPower,
       "shdslDslLineStatus-PhysicalStatistic-FramerSyncStatus": shdslDslLineStatus_PhysicalStatistic_FramerSyncStatus,
       "shdslDslLineStatus-PhysicalStatistic-CodeViolations": shdslDslLineStatus_PhysicalStatistic_CodeViolations,
       "shdslDslLineStatus-PhysicalStatistic-ErroredSecond": shdslDslLineStatus_PhysicalStatistic_ErroredSecond,
       "shdslDslLineStatus-PhysicalStatistic-SeverelyErroredSecond": shdslDslLineStatus_PhysicalStatistic_SeverelyErroredSecond,
       "shdslDslLineStatus-PhysicalStatistic-LoswSecond": shdslDslLineStatus_PhysicalStatistic_LoswSecond,
       "shdslDslLineStatus-PhysicalStatistic-UnavailableSecond": shdslDslLineStatus_PhysicalStatistic_UnavailableSecond,
       "shdslDslLineStatus-PhysicalStatistic-LoopAttenuation": shdslDslLineStatus_PhysicalStatistic_LoopAttenuation,
       "shdslDslLineStatus-Action-o": shdslDslLineStatus_Action_o,
       "shdslDslLineStatus-PhysicalStatistic-Snr": shdslDslLineStatus_PhysicalStatistic_Snr,
       "shdslDslLineStatus-PhysicalStatistic-SturLoopAttenuation": shdslDslLineStatus_PhysicalStatistic_SturLoopAttenuation,
       "shdslDslLineStatus-PhysicalStatistic-SturSnr": shdslDslLineStatus_PhysicalStatistic_SturSnr,
       "shdslDslLineStatus-PhysicalStatus-NetworkType": shdslDslLineStatus_PhysicalStatus_NetworkType}
)
