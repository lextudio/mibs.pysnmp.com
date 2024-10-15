# SNMP MIB module (ASCEND-MIBMADDSLOTCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBMADDSLOTCONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:54 2024
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

_MibmaddSlotConfig_ObjectIdentity = ObjectIdentity
mibmaddSlotConfig = _MibmaddSlotConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 163)
)
_MibmaddSlotConfigTable_Object = MibTable
mibmaddSlotConfigTable = _MibmaddSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1)
)
if mibBuilder.loadTexts:
    mibmaddSlotConfigTable.setStatus("mandatory")
_MibmaddSlotConfigEntry_Object = MibTableRow
mibmaddSlotConfigEntry = _MibmaddSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1)
)
mibmaddSlotConfigEntry.setIndexNames(
    (0, "ASCEND-MIBMADDSLOTCONFIG-MIB", "maddSlotConfig-Shelf-o"),
    (0, "ASCEND-MIBMADDSLOTCONFIG-MIB", "maddSlotConfig-Slot-o"),
    (0, "ASCEND-MIBMADDSLOTCONFIG-MIB", "maddSlotConfig-Item-o"),
)
if mibBuilder.loadTexts:
    mibmaddSlotConfigEntry.setStatus("mandatory")
_MaddSlotConfig_Shelf_o_Type = Integer32
_MaddSlotConfig_Shelf_o_Object = MibScalar
maddSlotConfig_Shelf_o = _MaddSlotConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 1),
    _MaddSlotConfig_Shelf_o_Type()
)
maddSlotConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maddSlotConfig_Shelf_o.setStatus("mandatory")
_MaddSlotConfig_Slot_o_Type = Integer32
_MaddSlotConfig_Slot_o_Object = MibScalar
maddSlotConfig_Slot_o = _MaddSlotConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 2),
    _MaddSlotConfig_Slot_o_Type()
)
maddSlotConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maddSlotConfig_Slot_o.setStatus("mandatory")
_MaddSlotConfig_Item_o_Type = Integer32
_MaddSlotConfig_Item_o_Object = MibScalar
maddSlotConfig_Item_o = _MaddSlotConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 3),
    _MaddSlotConfig_Item_o_Type()
)
maddSlotConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maddSlotConfig_Item_o.setStatus("mandatory")


class _MaddSlotConfig_SlotAddress_Shelf_Type(Integer32):
    """Custom type maddSlotConfig_SlotAddress_Shelf based on Integer32"""
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


_MaddSlotConfig_SlotAddress_Shelf_Type.__name__ = "Integer32"
_MaddSlotConfig_SlotAddress_Shelf_Object = MibScalar
maddSlotConfig_SlotAddress_Shelf = _MaddSlotConfig_SlotAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 4),
    _MaddSlotConfig_SlotAddress_Shelf_Type()
)
maddSlotConfig_SlotAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maddSlotConfig_SlotAddress_Shelf.setStatus("mandatory")


class _MaddSlotConfig_SlotAddress_Slot_Type(Integer32):
    """Custom type maddSlotConfig_SlotAddress_Slot based on Integer32"""
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


_MaddSlotConfig_SlotAddress_Slot_Type.__name__ = "Integer32"
_MaddSlotConfig_SlotAddress_Slot_Object = MibScalar
maddSlotConfig_SlotAddress_Slot = _MaddSlotConfig_SlotAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 5),
    _MaddSlotConfig_SlotAddress_Slot_Type()
)
maddSlotConfig_SlotAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maddSlotConfig_SlotAddress_Slot.setStatus("mandatory")
_MaddSlotConfig_SlotAddress_ItemNumber_Type = Integer32
_MaddSlotConfig_SlotAddress_ItemNumber_Object = MibScalar
maddSlotConfig_SlotAddress_ItemNumber = _MaddSlotConfig_SlotAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 6),
    _MaddSlotConfig_SlotAddress_ItemNumber_Type()
)
maddSlotConfig_SlotAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maddSlotConfig_SlotAddress_ItemNumber.setStatus("mandatory")


class _MaddSlotConfig_Subtype_Type(Integer32):
    """Custom type maddSlotConfig_Subtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n-192Ip2ipPorts", 3),
          ("n-288UnivPorts", 1),
          ("n-480VoipPorts", 2))
    )


_MaddSlotConfig_Subtype_Type.__name__ = "Integer32"
_MaddSlotConfig_Subtype_Object = MibScalar
maddSlotConfig_Subtype = _MaddSlotConfig_Subtype_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 7),
    _MaddSlotConfig_Subtype_Type()
)
maddSlotConfig_Subtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maddSlotConfig_Subtype.setStatus("mandatory")


class _MaddSlotConfig_Action_o_Type(Integer32):
    """Custom type maddSlotConfig_Action_o based on Integer32"""
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


_MaddSlotConfig_Action_o_Type.__name__ = "Integer32"
_MaddSlotConfig_Action_o_Object = MibScalar
maddSlotConfig_Action_o = _MaddSlotConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 163, 1, 1, 8),
    _MaddSlotConfig_Action_o_Type()
)
maddSlotConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maddSlotConfig_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBMADDSLOTCONFIG-MIB",
    **{"DisplayString": DisplayString,
       "mibmaddSlotConfig": mibmaddSlotConfig,
       "mibmaddSlotConfigTable": mibmaddSlotConfigTable,
       "mibmaddSlotConfigEntry": mibmaddSlotConfigEntry,
       "maddSlotConfig-Shelf-o": maddSlotConfig_Shelf_o,
       "maddSlotConfig-Slot-o": maddSlotConfig_Slot_o,
       "maddSlotConfig-Item-o": maddSlotConfig_Item_o,
       "maddSlotConfig-SlotAddress-Shelf": maddSlotConfig_SlotAddress_Shelf,
       "maddSlotConfig-SlotAddress-Slot": maddSlotConfig_SlotAddress_Slot,
       "maddSlotConfig-SlotAddress-ItemNumber": maddSlotConfig_SlotAddress_ItemNumber,
       "maddSlotConfig-Subtype": maddSlotConfig_Subtype,
       "maddSlotConfig-Action-o": maddSlotConfig_Action_o}
)
