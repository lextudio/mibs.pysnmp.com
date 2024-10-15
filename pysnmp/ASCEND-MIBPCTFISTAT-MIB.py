# SNMP MIB module (ASCEND-MIBPCTFISTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBPCTFISTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:01 2024
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

_MibpctfiLineStatus_ObjectIdentity = ObjectIdentity
mibpctfiLineStatus = _MibpctfiLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 19)
)
_MibpctfiLineStatusTable_Object = MibTable
mibpctfiLineStatusTable = _MibpctfiLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1)
)
if mibBuilder.loadTexts:
    mibpctfiLineStatusTable.setStatus("mandatory")
_MibpctfiLineStatusEntry_Object = MibTableRow
mibpctfiLineStatusEntry = _MibpctfiLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1)
)
mibpctfiLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-Shelf-o"),
    (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-Slot-o"),
    (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibpctfiLineStatusEntry.setStatus("mandatory")
_PctfiLineStatus_Shelf_o_Type = Integer32
_PctfiLineStatus_Shelf_o_Object = MibScalar
pctfiLineStatus_Shelf_o = _PctfiLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 1),
    _PctfiLineStatus_Shelf_o_Type()
)
pctfiLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiLineStatus_Shelf_o.setStatus("mandatory")
_PctfiLineStatus_Slot_o_Type = Integer32
_PctfiLineStatus_Slot_o_Object = MibScalar
pctfiLineStatus_Slot_o = _PctfiLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 2),
    _PctfiLineStatus_Slot_o_Type()
)
pctfiLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiLineStatus_Slot_o.setStatus("mandatory")
_PctfiLineStatus_Item_o_Type = Integer32
_PctfiLineStatus_Item_o_Object = MibScalar
pctfiLineStatus_Item_o = _PctfiLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 3),
    _PctfiLineStatus_Item_o_Type()
)
pctfiLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiLineStatus_Item_o.setStatus("mandatory")


class _PctfiLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type pctfiLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_PctfiLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_PctfiLineStatus_PhysicalAddress_Shelf_Object = MibScalar
pctfiLineStatus_PhysicalAddress_Shelf = _PctfiLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 4),
    _PctfiLineStatus_PhysicalAddress_Shelf_Type()
)
pctfiLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _PctfiLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type pctfiLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_PctfiLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_PctfiLineStatus_PhysicalAddress_Slot_Object = MibScalar
pctfiLineStatus_PhysicalAddress_Slot = _PctfiLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 5),
    _PctfiLineStatus_PhysicalAddress_Slot_Type()
)
pctfiLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_PctfiLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_PctfiLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
pctfiLineStatus_PhysicalAddress_ItemNumber = _PctfiLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 6),
    _PctfiLineStatus_PhysicalAddress_ItemNumber_Type()
)
pctfiLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _PctfiLineStatus_Link0Status_Type(Integer32):
    """Custom type pctfiLineStatus_Link0Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("disabled", 1),
          ("unavailable", 3))
    )


_PctfiLineStatus_Link0Status_Type.__name__ = "Integer32"
_PctfiLineStatus_Link0Status_Object = MibScalar
pctfiLineStatus_Link0Status = _PctfiLineStatus_Link0Status_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 7),
    _PctfiLineStatus_Link0Status_Type()
)
pctfiLineStatus_Link0Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_Link0Status.setStatus("mandatory")


class _PctfiLineStatus_Link1Status_Type(Integer32):
    """Custom type pctfiLineStatus_Link1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("disabled", 1),
          ("unavailable", 3))
    )


_PctfiLineStatus_Link1Status_Type.__name__ = "Integer32"
_PctfiLineStatus_Link1Status_Object = MibScalar
pctfiLineStatus_Link1Status = _PctfiLineStatus_Link1Status_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 8),
    _PctfiLineStatus_Link1Status_Type()
)
pctfiLineStatus_Link1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_Link1Status.setStatus("mandatory")


class _PctfiLineStatus_SideSelect_Type(Integer32):
    """Custom type pctfiLineStatus_SideSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("side0", 1),
          ("side1", 2))
    )


_PctfiLineStatus_SideSelect_Type.__name__ = "Integer32"
_PctfiLineStatus_SideSelect_Object = MibScalar
pctfiLineStatus_SideSelect = _PctfiLineStatus_SideSelect_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 9),
    _PctfiLineStatus_SideSelect_Type()
)
pctfiLineStatus_SideSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_SideSelect.setStatus("mandatory")


class _PctfiLineStatus_Action_o_Type(Integer32):
    """Custom type pctfiLineStatus_Action_o based on Integer32"""
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


_PctfiLineStatus_Action_o_Type.__name__ = "Integer32"
_PctfiLineStatus_Action_o_Object = MibScalar
pctfiLineStatus_Action_o = _PctfiLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 10),
    _PctfiLineStatus_Action_o_Type()
)
pctfiLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_Action_o.setStatus("mandatory")
_MibpctfiLineStatus_VirtualDs1LineStatusTable_Object = MibTable
mibpctfiLineStatus_VirtualDs1LineStatusTable = _MibpctfiLineStatus_VirtualDs1LineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2)
)
if mibBuilder.loadTexts:
    mibpctfiLineStatus_VirtualDs1LineStatusTable.setStatus("mandatory")
_MibpctfiLineStatus_VirtualDs1LineStatusEntry_Object = MibTableRow
mibpctfiLineStatus_VirtualDs1LineStatusEntry = _MibpctfiLineStatus_VirtualDs1LineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1)
)
mibpctfiLineStatus_VirtualDs1LineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Shelf-o"),
    (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Slot-o"),
    (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Item-o"),
    (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Index-o"),
)
if mibBuilder.loadTexts:
    mibpctfiLineStatus_VirtualDs1LineStatusEntry.setStatus("mandatory")
_PctfiLineStatus_VirtualDs1LineStatus_Shelf_o_Type = Integer32
_PctfiLineStatus_VirtualDs1LineStatus_Shelf_o_Object = MibScalar
pctfiLineStatus_VirtualDs1LineStatus_Shelf_o = _PctfiLineStatus_VirtualDs1LineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 1),
    _PctfiLineStatus_VirtualDs1LineStatus_Shelf_o_Type()
)
pctfiLineStatus_VirtualDs1LineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiLineStatus_VirtualDs1LineStatus_Shelf_o.setStatus("mandatory")
_PctfiLineStatus_VirtualDs1LineStatus_Slot_o_Type = Integer32
_PctfiLineStatus_VirtualDs1LineStatus_Slot_o_Object = MibScalar
pctfiLineStatus_VirtualDs1LineStatus_Slot_o = _PctfiLineStatus_VirtualDs1LineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 2),
    _PctfiLineStatus_VirtualDs1LineStatus_Slot_o_Type()
)
pctfiLineStatus_VirtualDs1LineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiLineStatus_VirtualDs1LineStatus_Slot_o.setStatus("mandatory")
_PctfiLineStatus_VirtualDs1LineStatus_Item_o_Type = Integer32
_PctfiLineStatus_VirtualDs1LineStatus_Item_o_Object = MibScalar
pctfiLineStatus_VirtualDs1LineStatus_Item_o = _PctfiLineStatus_VirtualDs1LineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 3),
    _PctfiLineStatus_VirtualDs1LineStatus_Item_o_Type()
)
pctfiLineStatus_VirtualDs1LineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiLineStatus_VirtualDs1LineStatus_Item_o.setStatus("mandatory")
_PctfiLineStatus_VirtualDs1LineStatus_Index_o_Type = Integer32
_PctfiLineStatus_VirtualDs1LineStatus_Index_o_Object = MibScalar
pctfiLineStatus_VirtualDs1LineStatus_Index_o = _PctfiLineStatus_VirtualDs1LineStatus_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 4),
    _PctfiLineStatus_VirtualDs1LineStatus_Index_o_Type()
)
pctfiLineStatus_VirtualDs1LineStatus_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiLineStatus_VirtualDs1LineStatus_Index_o.setStatus("mandatory")


class _PctfiLineStatus_VirtualDs1LineStatus_TrunkState_Type(Integer32):
    """Custom type pctfiLineStatus_VirtualDs1LineStatus_TrunkState based on Integer32"""
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
        *(("nonOperational", 2),
          ("operational", 3),
          ("unequipped", 4),
          ("unused", 1))
    )


_PctfiLineStatus_VirtualDs1LineStatus_TrunkState_Type.__name__ = "Integer32"
_PctfiLineStatus_VirtualDs1LineStatus_TrunkState_Object = MibScalar
pctfiLineStatus_VirtualDs1LineStatus_TrunkState = _PctfiLineStatus_VirtualDs1LineStatus_TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 5),
    _PctfiLineStatus_VirtualDs1LineStatus_TrunkState_Type()
)
pctfiLineStatus_VirtualDs1LineStatus_TrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_VirtualDs1LineStatus_TrunkState.setStatus("mandatory")


class _PctfiLineStatus_VirtualDs1LineStatus_F4BitState_Type(Integer32):
    """Custom type pctfiLineStatus_VirtualDs1LineStatus_F4BitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cas", 2),
          ("nonCas", 1))
    )


_PctfiLineStatus_VirtualDs1LineStatus_F4BitState_Type.__name__ = "Integer32"
_PctfiLineStatus_VirtualDs1LineStatus_F4BitState_Object = MibScalar
pctfiLineStatus_VirtualDs1LineStatus_F4BitState = _PctfiLineStatus_VirtualDs1LineStatus_F4BitState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 6),
    _PctfiLineStatus_VirtualDs1LineStatus_F4BitState_Type()
)
pctfiLineStatus_VirtualDs1LineStatus_F4BitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiLineStatus_VirtualDs1LineStatus_F4BitState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBPCTFISTAT-MIB",
    **{"DisplayString": DisplayString,
       "mibpctfiLineStatus": mibpctfiLineStatus,
       "mibpctfiLineStatusTable": mibpctfiLineStatusTable,
       "mibpctfiLineStatusEntry": mibpctfiLineStatusEntry,
       "pctfiLineStatus-Shelf-o": pctfiLineStatus_Shelf_o,
       "pctfiLineStatus-Slot-o": pctfiLineStatus_Slot_o,
       "pctfiLineStatus-Item-o": pctfiLineStatus_Item_o,
       "pctfiLineStatus-PhysicalAddress-Shelf": pctfiLineStatus_PhysicalAddress_Shelf,
       "pctfiLineStatus-PhysicalAddress-Slot": pctfiLineStatus_PhysicalAddress_Slot,
       "pctfiLineStatus-PhysicalAddress-ItemNumber": pctfiLineStatus_PhysicalAddress_ItemNumber,
       "pctfiLineStatus-Link0Status": pctfiLineStatus_Link0Status,
       "pctfiLineStatus-Link1Status": pctfiLineStatus_Link1Status,
       "pctfiLineStatus-SideSelect": pctfiLineStatus_SideSelect,
       "pctfiLineStatus-Action-o": pctfiLineStatus_Action_o,
       "mibpctfiLineStatus-VirtualDs1LineStatusTable": mibpctfiLineStatus_VirtualDs1LineStatusTable,
       "mibpctfiLineStatus-VirtualDs1LineStatusEntry": mibpctfiLineStatus_VirtualDs1LineStatusEntry,
       "pctfiLineStatus-VirtualDs1LineStatus-Shelf-o": pctfiLineStatus_VirtualDs1LineStatus_Shelf_o,
       "pctfiLineStatus-VirtualDs1LineStatus-Slot-o": pctfiLineStatus_VirtualDs1LineStatus_Slot_o,
       "pctfiLineStatus-VirtualDs1LineStatus-Item-o": pctfiLineStatus_VirtualDs1LineStatus_Item_o,
       "pctfiLineStatus-VirtualDs1LineStatus-Index-o": pctfiLineStatus_VirtualDs1LineStatus_Index_o,
       "pctfiLineStatus-VirtualDs1LineStatus-TrunkState": pctfiLineStatus_VirtualDs1LineStatus_TrunkState,
       "pctfiLineStatus-VirtualDs1LineStatus-F4BitState": pctfiLineStatus_VirtualDs1LineStatus_F4BitState}
)
