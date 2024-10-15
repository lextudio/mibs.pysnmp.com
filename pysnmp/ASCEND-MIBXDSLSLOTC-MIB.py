# SNMP MIB module (ASCEND-MIBXDSLSLOTC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBXDSLSLOTC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:37 2024
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

_MibxdslSlotConfigProfile_ObjectIdentity = ObjectIdentity
mibxdslSlotConfigProfile = _MibxdslSlotConfigProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 20)
)
_MibxdslSlotConfigProfileTable_Object = MibTable
mibxdslSlotConfigProfileTable = _MibxdslSlotConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1)
)
if mibBuilder.loadTexts:
    mibxdslSlotConfigProfileTable.setStatus("mandatory")
_MibxdslSlotConfigProfileEntry_Object = MibTableRow
mibxdslSlotConfigProfileEntry = _MibxdslSlotConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1)
)
mibxdslSlotConfigProfileEntry.setIndexNames(
    (0, "ASCEND-MIBXDSLSLOTC-MIB", "xdslSlotConfigProfile-Shelf-o"),
    (0, "ASCEND-MIBXDSLSLOTC-MIB", "xdslSlotConfigProfile-Slot-o"),
    (0, "ASCEND-MIBXDSLSLOTC-MIB", "xdslSlotConfigProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibxdslSlotConfigProfileEntry.setStatus("mandatory")
_XdslSlotConfigProfile_Shelf_o_Type = Integer32
_XdslSlotConfigProfile_Shelf_o_Object = MibScalar
xdslSlotConfigProfile_Shelf_o = _XdslSlotConfigProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 1),
    _XdslSlotConfigProfile_Shelf_o_Type()
)
xdslSlotConfigProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_Shelf_o.setStatus("mandatory")
_XdslSlotConfigProfile_Slot_o_Type = Integer32
_XdslSlotConfigProfile_Slot_o_Object = MibScalar
xdslSlotConfigProfile_Slot_o = _XdslSlotConfigProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 2),
    _XdslSlotConfigProfile_Slot_o_Type()
)
xdslSlotConfigProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_Slot_o.setStatus("mandatory")
_XdslSlotConfigProfile_Item_o_Type = Integer32
_XdslSlotConfigProfile_Item_o_Object = MibScalar
xdslSlotConfigProfile_Item_o = _XdslSlotConfigProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 3),
    _XdslSlotConfigProfile_Item_o_Type()
)
xdslSlotConfigProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_Item_o.setStatus("mandatory")


class _XdslSlotConfigProfile_SlotAddress_Shelf_Type(Integer32):
    """Custom type xdslSlotConfigProfile_SlotAddress_Shelf based on Integer32"""
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


_XdslSlotConfigProfile_SlotAddress_Shelf_Type.__name__ = "Integer32"
_XdslSlotConfigProfile_SlotAddress_Shelf_Object = MibScalar
xdslSlotConfigProfile_SlotAddress_Shelf = _XdslSlotConfigProfile_SlotAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 4),
    _XdslSlotConfigProfile_SlotAddress_Shelf_Type()
)
xdslSlotConfigProfile_SlotAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_SlotAddress_Shelf.setStatus("mandatory")


class _XdslSlotConfigProfile_SlotAddress_Slot_Type(Integer32):
    """Custom type xdslSlotConfigProfile_SlotAddress_Slot based on Integer32"""
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


_XdslSlotConfigProfile_SlotAddress_Slot_Type.__name__ = "Integer32"
_XdslSlotConfigProfile_SlotAddress_Slot_Object = MibScalar
xdslSlotConfigProfile_SlotAddress_Slot = _XdslSlotConfigProfile_SlotAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 5),
    _XdslSlotConfigProfile_SlotAddress_Slot_Type()
)
xdslSlotConfigProfile_SlotAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_SlotAddress_Slot.setStatus("mandatory")
_XdslSlotConfigProfile_SlotAddress_ItemNumber_Type = Integer32
_XdslSlotConfigProfile_SlotAddress_ItemNumber_Object = MibScalar
xdslSlotConfigProfile_SlotAddress_ItemNumber = _XdslSlotConfigProfile_SlotAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 6),
    _XdslSlotConfigProfile_SlotAddress_ItemNumber_Type()
)
xdslSlotConfigProfile_SlotAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_SlotAddress_ItemNumber.setStatus("mandatory")


class _XdslSlotConfigProfile_SealingCurrentOn_Type(Integer32):
    """Custom type xdslSlotConfigProfile_SealingCurrentOn based on Integer32"""
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


_XdslSlotConfigProfile_SealingCurrentOn_Type.__name__ = "Integer32"
_XdslSlotConfigProfile_SealingCurrentOn_Object = MibScalar
xdslSlotConfigProfile_SealingCurrentOn = _XdslSlotConfigProfile_SealingCurrentOn_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 7),
    _XdslSlotConfigProfile_SealingCurrentOn_Type()
)
xdslSlotConfigProfile_SealingCurrentOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_SealingCurrentOn.setStatus("mandatory")


class _XdslSlotConfigProfile_Action_o_Type(Integer32):
    """Custom type xdslSlotConfigProfile_Action_o based on Integer32"""
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


_XdslSlotConfigProfile_Action_o_Type.__name__ = "Integer32"
_XdslSlotConfigProfile_Action_o_Object = MibScalar
xdslSlotConfigProfile_Action_o = _XdslSlotConfigProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 20, 1, 1, 8),
    _XdslSlotConfigProfile_Action_o_Type()
)
xdslSlotConfigProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslSlotConfigProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBXDSLSLOTC-MIB",
    **{"DisplayString": DisplayString,
       "mibxdslSlotConfigProfile": mibxdslSlotConfigProfile,
       "mibxdslSlotConfigProfileTable": mibxdslSlotConfigProfileTable,
       "mibxdslSlotConfigProfileEntry": mibxdslSlotConfigProfileEntry,
       "xdslSlotConfigProfile-Shelf-o": xdslSlotConfigProfile_Shelf_o,
       "xdslSlotConfigProfile-Slot-o": xdslSlotConfigProfile_Slot_o,
       "xdslSlotConfigProfile-Item-o": xdslSlotConfigProfile_Item_o,
       "xdslSlotConfigProfile-SlotAddress-Shelf": xdslSlotConfigProfile_SlotAddress_Shelf,
       "xdslSlotConfigProfile-SlotAddress-Slot": xdslSlotConfigProfile_SlotAddress_Slot,
       "xdslSlotConfigProfile-SlotAddress-ItemNumber": xdslSlotConfigProfile_SlotAddress_ItemNumber,
       "xdslSlotConfigProfile-SealingCurrentOn": xdslSlotConfigProfile_SealingCurrentOn,
       "xdslSlotConfigProfile-Action-o": xdslSlotConfigProfile_Action_o}
)
