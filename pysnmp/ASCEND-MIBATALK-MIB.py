# SNMP MIB module (ASCEND-MIBATALK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATALK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:05 2024
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

_MibatalkInterfaceProfile_ObjectIdentity = ObjectIdentity
mibatalkInterfaceProfile = _MibatalkInterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 35)
)
_MibatalkInterfaceProfileTable_Object = MibTable
mibatalkInterfaceProfileTable = _MibatalkInterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1)
)
if mibBuilder.loadTexts:
    mibatalkInterfaceProfileTable.setStatus("mandatory")
_MibatalkInterfaceProfileEntry_Object = MibTableRow
mibatalkInterfaceProfileEntry = _MibatalkInterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1)
)
mibatalkInterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-Item-o"),
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibatalkInterfaceProfileEntry.setStatus("mandatory")
_AtalkInterfaceProfile_Shelf_o_Type = Integer32
_AtalkInterfaceProfile_Shelf_o_Object = MibScalar
atalkInterfaceProfile_Shelf_o = _AtalkInterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 1),
    _AtalkInterfaceProfile_Shelf_o_Type()
)
atalkInterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_Shelf_o.setStatus("mandatory")
_AtalkInterfaceProfile_Slot_o_Type = Integer32
_AtalkInterfaceProfile_Slot_o_Object = MibScalar
atalkInterfaceProfile_Slot_o = _AtalkInterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 2),
    _AtalkInterfaceProfile_Slot_o_Type()
)
atalkInterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_Slot_o.setStatus("mandatory")
_AtalkInterfaceProfile_Item_o_Type = Integer32
_AtalkInterfaceProfile_Item_o_Object = MibScalar
atalkInterfaceProfile_Item_o = _AtalkInterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 3),
    _AtalkInterfaceProfile_Item_o_Type()
)
atalkInterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_Item_o.setStatus("mandatory")
_AtalkInterfaceProfile_LogicalItem_o_Type = Integer32
_AtalkInterfaceProfile_LogicalItem_o_Object = MibScalar
atalkInterfaceProfile_LogicalItem_o = _AtalkInterfaceProfile_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 4),
    _AtalkInterfaceProfile_LogicalItem_o_Type()
)
atalkInterfaceProfile_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_LogicalItem_o.setStatus("mandatory")


class _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf based on Integer32"""
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


_AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object = MibScalar
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf = _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 5),
    _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type()
)
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot based on Integer32"""
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


_AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object = MibScalar
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot = _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 6),
    _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type()
)
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus("mandatory")
_AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type = Integer32
_AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object = MibScalar
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber = _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 7),
    _AtalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type()
)
atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtalkInterfaceProfile_InterfaceAddress_LogicalItem_Type = Integer32
_AtalkInterfaceProfile_InterfaceAddress_LogicalItem_Object = MibScalar
atalkInterfaceProfile_InterfaceAddress_LogicalItem = _AtalkInterfaceProfile_InterfaceAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 8),
    _AtalkInterfaceProfile_InterfaceAddress_LogicalItem_Type()
)
atalkInterfaceProfile_InterfaceAddress_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_InterfaceAddress_LogicalItem.setStatus("mandatory")


class _AtalkInterfaceProfile_AtalkRoutingEnabled_Type(Integer32):
    """Custom type atalkInterfaceProfile_AtalkRoutingEnabled based on Integer32"""
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


_AtalkInterfaceProfile_AtalkRoutingEnabled_Type.__name__ = "Integer32"
_AtalkInterfaceProfile_AtalkRoutingEnabled_Object = MibScalar
atalkInterfaceProfile_AtalkRoutingEnabled = _AtalkInterfaceProfile_AtalkRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 9),
    _AtalkInterfaceProfile_AtalkRoutingEnabled_Type()
)
atalkInterfaceProfile_AtalkRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkRoutingEnabled.setStatus("mandatory")
_AtalkInterfaceProfile_HintZone_Type = DisplayString
_AtalkInterfaceProfile_HintZone_Object = MibScalar
atalkInterfaceProfile_HintZone = _AtalkInterfaceProfile_HintZone_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 10),
    _AtalkInterfaceProfile_HintZone_Type()
)
atalkInterfaceProfile_HintZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_HintZone.setStatus("mandatory")


class _AtalkInterfaceProfile_AtalkRouter_Type(Integer32):
    """Custom type atalkInterfaceProfile_AtalkRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atalkRouterNonSeed", 3),
          ("atalkRouterOff", 1),
          ("atalkRouterSeed", 2))
    )


_AtalkInterfaceProfile_AtalkRouter_Type.__name__ = "Integer32"
_AtalkInterfaceProfile_AtalkRouter_Object = MibScalar
atalkInterfaceProfile_AtalkRouter = _AtalkInterfaceProfile_AtalkRouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 11),
    _AtalkInterfaceProfile_AtalkRouter_Type()
)
atalkInterfaceProfile_AtalkRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkRouter.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkNetStart_Type = Integer32
_AtalkInterfaceProfile_AtalkNetStart_Object = MibScalar
atalkInterfaceProfile_AtalkNetStart = _AtalkInterfaceProfile_AtalkNetStart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 12),
    _AtalkInterfaceProfile_AtalkNetStart_Type()
)
atalkInterfaceProfile_AtalkNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkNetStart.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkNetEnd_Type = Integer32
_AtalkInterfaceProfile_AtalkNetEnd_Object = MibScalar
atalkInterfaceProfile_AtalkNetEnd = _AtalkInterfaceProfile_AtalkNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 13),
    _AtalkInterfaceProfile_AtalkNetEnd_Type()
)
atalkInterfaceProfile_AtalkNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkNetEnd.setStatus("mandatory")


class _AtalkInterfaceProfile_Action_o_Type(Integer32):
    """Custom type atalkInterfaceProfile_Action_o based on Integer32"""
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


_AtalkInterfaceProfile_Action_o_Type.__name__ = "Integer32"
_AtalkInterfaceProfile_Action_o_Object = MibScalar
atalkInterfaceProfile_Action_o = _AtalkInterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 1, 1, 14),
    _AtalkInterfaceProfile_Action_o_Type()
)
atalkInterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_Action_o.setStatus("mandatory")
_MibatalkInterfaceProfile_AtalkZoneListTable_Object = MibTable
mibatalkInterfaceProfile_AtalkZoneListTable = _MibatalkInterfaceProfile_AtalkZoneListTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2)
)
if mibBuilder.loadTexts:
    mibatalkInterfaceProfile_AtalkZoneListTable.setStatus("mandatory")
_MibatalkInterfaceProfile_AtalkZoneListEntry_Object = MibTableRow
mibatalkInterfaceProfile_AtalkZoneListEntry = _MibatalkInterfaceProfile_AtalkZoneListEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1)
)
mibatalkInterfaceProfile_AtalkZoneListEntry.setIndexNames(
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Shelf-o"),
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Slot-o"),
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Item-o"),
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-LogicalItem-o"),
    (0, "ASCEND-MIBATALK-MIB", "atalkInterfaceProfile-AtalkZoneList-Index-o"),
)
if mibBuilder.loadTexts:
    mibatalkInterfaceProfile_AtalkZoneListEntry.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkZoneList_Shelf_o_Type = Integer32
_AtalkInterfaceProfile_AtalkZoneList_Shelf_o_Object = MibScalar
atalkInterfaceProfile_AtalkZoneList_Shelf_o = _AtalkInterfaceProfile_AtalkZoneList_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 1),
    _AtalkInterfaceProfile_AtalkZoneList_Shelf_o_Type()
)
atalkInterfaceProfile_AtalkZoneList_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkZoneList_Shelf_o.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkZoneList_Slot_o_Type = Integer32
_AtalkInterfaceProfile_AtalkZoneList_Slot_o_Object = MibScalar
atalkInterfaceProfile_AtalkZoneList_Slot_o = _AtalkInterfaceProfile_AtalkZoneList_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 2),
    _AtalkInterfaceProfile_AtalkZoneList_Slot_o_Type()
)
atalkInterfaceProfile_AtalkZoneList_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkZoneList_Slot_o.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkZoneList_Item_o_Type = Integer32
_AtalkInterfaceProfile_AtalkZoneList_Item_o_Object = MibScalar
atalkInterfaceProfile_AtalkZoneList_Item_o = _AtalkInterfaceProfile_AtalkZoneList_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 3),
    _AtalkInterfaceProfile_AtalkZoneList_Item_o_Type()
)
atalkInterfaceProfile_AtalkZoneList_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkZoneList_Item_o.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkZoneList_LogicalItem_o_Type = Integer32
_AtalkInterfaceProfile_AtalkZoneList_LogicalItem_o_Object = MibScalar
atalkInterfaceProfile_AtalkZoneList_LogicalItem_o = _AtalkInterfaceProfile_AtalkZoneList_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 4),
    _AtalkInterfaceProfile_AtalkZoneList_LogicalItem_o_Type()
)
atalkInterfaceProfile_AtalkZoneList_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkZoneList_LogicalItem_o.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkZoneList_Index_o_Type = Integer32
_AtalkInterfaceProfile_AtalkZoneList_Index_o_Object = MibScalar
atalkInterfaceProfile_AtalkZoneList_Index_o = _AtalkInterfaceProfile_AtalkZoneList_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 5),
    _AtalkInterfaceProfile_AtalkZoneList_Index_o_Type()
)
atalkInterfaceProfile_AtalkZoneList_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkZoneList_Index_o.setStatus("mandatory")
_AtalkInterfaceProfile_AtalkZoneList_Type = DisplayString
_AtalkInterfaceProfile_AtalkZoneList_Object = MibScalar
atalkInterfaceProfile_AtalkZoneList = _AtalkInterfaceProfile_AtalkZoneList_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 35, 2, 1, 6),
    _AtalkInterfaceProfile_AtalkZoneList_Type()
)
atalkInterfaceProfile_AtalkZoneList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkInterfaceProfile_AtalkZoneList.setStatus("mandatory")
_MibatalkGlobalProfile_ObjectIdentity = ObjectIdentity
mibatalkGlobalProfile = _MibatalkGlobalProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 36)
)
_MibatalkGlobalProfileTable_Object = MibTable
mibatalkGlobalProfileTable = _MibatalkGlobalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 36, 1)
)
if mibBuilder.loadTexts:
    mibatalkGlobalProfileTable.setStatus("mandatory")
_MibatalkGlobalProfileEntry_Object = MibTableRow
mibatalkGlobalProfileEntry = _MibatalkGlobalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1)
)
mibatalkGlobalProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATALK-MIB", "atalkGlobalProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibatalkGlobalProfileEntry.setStatus("mandatory")
_AtalkGlobalProfile_Index_o_Type = Integer32
_AtalkGlobalProfile_Index_o_Object = MibScalar
atalkGlobalProfile_Index_o = _AtalkGlobalProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 1),
    _AtalkGlobalProfile_Index_o_Type()
)
atalkGlobalProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atalkGlobalProfile_Index_o.setStatus("mandatory")
_AtalkGlobalProfile_AtalkDialinPoolStart_Type = Integer32
_AtalkGlobalProfile_AtalkDialinPoolStart_Object = MibScalar
atalkGlobalProfile_AtalkDialinPoolStart = _AtalkGlobalProfile_AtalkDialinPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 2),
    _AtalkGlobalProfile_AtalkDialinPoolStart_Type()
)
atalkGlobalProfile_AtalkDialinPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkGlobalProfile_AtalkDialinPoolStart.setStatus("mandatory")
_AtalkGlobalProfile_AtalkDialinPoolEnd_Type = Integer32
_AtalkGlobalProfile_AtalkDialinPoolEnd_Object = MibScalar
atalkGlobalProfile_AtalkDialinPoolEnd = _AtalkGlobalProfile_AtalkDialinPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 3),
    _AtalkGlobalProfile_AtalkDialinPoolEnd_Type()
)
atalkGlobalProfile_AtalkDialinPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkGlobalProfile_AtalkDialinPoolEnd.setStatus("mandatory")


class _AtalkGlobalProfile_Action_o_Type(Integer32):
    """Custom type atalkGlobalProfile_Action_o based on Integer32"""
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


_AtalkGlobalProfile_Action_o_Type.__name__ = "Integer32"
_AtalkGlobalProfile_Action_o_Object = MibScalar
atalkGlobalProfile_Action_o = _AtalkGlobalProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 36, 1, 1, 4),
    _AtalkGlobalProfile_Action_o_Type()
)
atalkGlobalProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atalkGlobalProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATALK-MIB",
    **{"DisplayString": DisplayString,
       "mibatalkInterfaceProfile": mibatalkInterfaceProfile,
       "mibatalkInterfaceProfileTable": mibatalkInterfaceProfileTable,
       "mibatalkInterfaceProfileEntry": mibatalkInterfaceProfileEntry,
       "atalkInterfaceProfile-Shelf-o": atalkInterfaceProfile_Shelf_o,
       "atalkInterfaceProfile-Slot-o": atalkInterfaceProfile_Slot_o,
       "atalkInterfaceProfile-Item-o": atalkInterfaceProfile_Item_o,
       "atalkInterfaceProfile-LogicalItem-o": atalkInterfaceProfile_LogicalItem_o,
       "atalkInterfaceProfile-InterfaceAddress-PhysicalAddress-Shelf": atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf,
       "atalkInterfaceProfile-InterfaceAddress-PhysicalAddress-Slot": atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot,
       "atalkInterfaceProfile-InterfaceAddress-PhysicalAddress-ItemNumber": atalkInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber,
       "atalkInterfaceProfile-InterfaceAddress-LogicalItem": atalkInterfaceProfile_InterfaceAddress_LogicalItem,
       "atalkInterfaceProfile-AtalkRoutingEnabled": atalkInterfaceProfile_AtalkRoutingEnabled,
       "atalkInterfaceProfile-HintZone": atalkInterfaceProfile_HintZone,
       "atalkInterfaceProfile-AtalkRouter": atalkInterfaceProfile_AtalkRouter,
       "atalkInterfaceProfile-AtalkNetStart": atalkInterfaceProfile_AtalkNetStart,
       "atalkInterfaceProfile-AtalkNetEnd": atalkInterfaceProfile_AtalkNetEnd,
       "atalkInterfaceProfile-Action-o": atalkInterfaceProfile_Action_o,
       "mibatalkInterfaceProfile-AtalkZoneListTable": mibatalkInterfaceProfile_AtalkZoneListTable,
       "mibatalkInterfaceProfile-AtalkZoneListEntry": mibatalkInterfaceProfile_AtalkZoneListEntry,
       "atalkInterfaceProfile-AtalkZoneList-Shelf-o": atalkInterfaceProfile_AtalkZoneList_Shelf_o,
       "atalkInterfaceProfile-AtalkZoneList-Slot-o": atalkInterfaceProfile_AtalkZoneList_Slot_o,
       "atalkInterfaceProfile-AtalkZoneList-Item-o": atalkInterfaceProfile_AtalkZoneList_Item_o,
       "atalkInterfaceProfile-AtalkZoneList-LogicalItem-o": atalkInterfaceProfile_AtalkZoneList_LogicalItem_o,
       "atalkInterfaceProfile-AtalkZoneList-Index-o": atalkInterfaceProfile_AtalkZoneList_Index_o,
       "atalkInterfaceProfile-AtalkZoneList": atalkInterfaceProfile_AtalkZoneList,
       "mibatalkGlobalProfile": mibatalkGlobalProfile,
       "mibatalkGlobalProfileTable": mibatalkGlobalProfileTable,
       "mibatalkGlobalProfileEntry": mibatalkGlobalProfileEntry,
       "atalkGlobalProfile-Index-o": atalkGlobalProfile_Index_o,
       "atalkGlobalProfile-AtalkDialinPoolStart": atalkGlobalProfile_AtalkDialinPoolStart,
       "atalkGlobalProfile-AtalkDialinPoolEnd": atalkGlobalProfile_AtalkDialinPoolEnd,
       "atalkGlobalProfile-Action-o": atalkGlobalProfile_Action_o}
)
