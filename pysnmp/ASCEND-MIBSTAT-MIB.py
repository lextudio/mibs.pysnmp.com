# SNMP MIB module (ASCEND-MIBSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:16 2024
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

_MibbRINetworkInterfaceState_ObjectIdentity = ObjectIdentity
mibbRINetworkInterfaceState = _MibbRINetworkInterfaceState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 28)
)
_MibbRINetworkInterfaceStateTable_Object = MibTable
mibbRINetworkInterfaceStateTable = _MibbRINetworkInterfaceStateTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1)
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceStateTable.setStatus("mandatory")
_MibbRINetworkInterfaceStateEntry_Object = MibTableRow
mibbRINetworkInterfaceStateEntry = _MibbRINetworkInterfaceStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1)
)
mibbRINetworkInterfaceStateEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-Item-o"),
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceStateEntry.setStatus("mandatory")
_BRINetworkInterfaceState_Shelf_o_Type = Integer32
_BRINetworkInterfaceState_Shelf_o_Object = MibScalar
bRINetworkInterfaceState_Shelf_o = _BRINetworkInterfaceState_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 1),
    _BRINetworkInterfaceState_Shelf_o_Type()
)
bRINetworkInterfaceState_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_Shelf_o.setStatus("mandatory")
_BRINetworkInterfaceState_Slot_o_Type = Integer32
_BRINetworkInterfaceState_Slot_o_Object = MibScalar
bRINetworkInterfaceState_Slot_o = _BRINetworkInterfaceState_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 2),
    _BRINetworkInterfaceState_Slot_o_Type()
)
bRINetworkInterfaceState_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_Slot_o.setStatus("mandatory")
_BRINetworkInterfaceState_Item_o_Type = Integer32
_BRINetworkInterfaceState_Item_o_Object = MibScalar
bRINetworkInterfaceState_Item_o = _BRINetworkInterfaceState_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 3),
    _BRINetworkInterfaceState_Item_o_Type()
)
bRINetworkInterfaceState_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_Item_o.setStatus("mandatory")


class _BRINetworkInterfaceState_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type bRINetworkInterfaceState_PhysicalAddress_Shelf based on Integer32"""
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


_BRINetworkInterfaceState_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_PhysicalAddress_Shelf_Object = MibScalar
bRINetworkInterfaceState_PhysicalAddress_Shelf = _BRINetworkInterfaceState_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 4),
    _BRINetworkInterfaceState_PhysicalAddress_Shelf_Type()
)
bRINetworkInterfaceState_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalAddress_Shelf.setStatus("mandatory")


class _BRINetworkInterfaceState_PhysicalAddress_Slot_Type(Integer32):
    """Custom type bRINetworkInterfaceState_PhysicalAddress_Slot based on Integer32"""
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


_BRINetworkInterfaceState_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_PhysicalAddress_Slot_Object = MibScalar
bRINetworkInterfaceState_PhysicalAddress_Slot = _BRINetworkInterfaceState_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 5),
    _BRINetworkInterfaceState_PhysicalAddress_Slot_Type()
)
bRINetworkInterfaceState_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalAddress_Slot.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalAddress_ItemNumber_Type = Integer32
_BRINetworkInterfaceState_PhysicalAddress_ItemNumber_Object = MibScalar
bRINetworkInterfaceState_PhysicalAddress_ItemNumber = _BRINetworkInterfaceState_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 6),
    _BRINetworkInterfaceState_PhysicalAddress_ItemNumber_Type()
)
bRINetworkInterfaceState_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _BRINetworkInterfaceState_LineState_Type(Integer32):
    """Custom type bRINetworkInterfaceState_LineState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("doesNotExist", 1),
          ("multipoint1", 7),
          ("multipoint2", 8),
          ("noLogical", 4),
          ("noMgmt", 5),
          ("noPhysical", 3),
          ("pointToPoint", 6))
    )


_BRINetworkInterfaceState_LineState_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_LineState_Object = MibScalar
bRINetworkInterfaceState_LineState = _BRINetworkInterfaceState_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 7),
    _BRINetworkInterfaceState_LineState_Type()
)
bRINetworkInterfaceState_LineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_LineState.setStatus("mandatory")


class _BRINetworkInterfaceState_Action_o_Type(Integer32):
    """Custom type bRINetworkInterfaceState_Action_o based on Integer32"""
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


_BRINetworkInterfaceState_Action_o_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_Action_o_Object = MibScalar
bRINetworkInterfaceState_Action_o = _BRINetworkInterfaceState_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 8),
    _BRINetworkInterfaceState_Action_o_Type()
)
bRINetworkInterfaceState_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_Action_o.setStatus("mandatory")


class _BRINetworkInterfaceState_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type bRINetworkInterfaceState_SparePhysicalAddress_Shelf based on Integer32"""
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


_BRINetworkInterfaceState_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_SparePhysicalAddress_Shelf_Object = MibScalar
bRINetworkInterfaceState_SparePhysicalAddress_Shelf = _BRINetworkInterfaceState_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 9),
    _BRINetworkInterfaceState_SparePhysicalAddress_Shelf_Type()
)
bRINetworkInterfaceState_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _BRINetworkInterfaceState_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type bRINetworkInterfaceState_SparePhysicalAddress_Slot based on Integer32"""
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


_BRINetworkInterfaceState_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_SparePhysicalAddress_Slot_Object = MibScalar
bRINetworkInterfaceState_SparePhysicalAddress_Slot = _BRINetworkInterfaceState_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 10),
    _BRINetworkInterfaceState_SparePhysicalAddress_Slot_Type()
)
bRINetworkInterfaceState_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_SparePhysicalAddress_Slot.setStatus("mandatory")
_BRINetworkInterfaceState_SparePhysicalAddress_ItemNumber_Type = Integer32
_BRINetworkInterfaceState_SparePhysicalAddress_ItemNumber_Object = MibScalar
bRINetworkInterfaceState_SparePhysicalAddress_ItemNumber = _BRINetworkInterfaceState_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 11),
    _BRINetworkInterfaceState_SparePhysicalAddress_ItemNumber_Type()
)
bRINetworkInterfaceState_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _BRINetworkInterfaceState_SparingState_Type(Integer32):
    """Custom type bRINetworkInterfaceState_SparingState based on Integer32"""
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


_BRINetworkInterfaceState_SparingState_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_SparingState_Object = MibScalar
bRINetworkInterfaceState_SparingState = _BRINetworkInterfaceState_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 12),
    _BRINetworkInterfaceState_SparingState_Type()
)
bRINetworkInterfaceState_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_SparingState.setStatus("mandatory")


class _BRINetworkInterfaceState_SparingChangeReason_Type(Integer32):
    """Custom type bRINetworkInterfaceState_SparingChangeReason based on Integer32"""
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


_BRINetworkInterfaceState_SparingChangeReason_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_SparingChangeReason_Object = MibScalar
bRINetworkInterfaceState_SparingChangeReason = _BRINetworkInterfaceState_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 13),
    _BRINetworkInterfaceState_SparingChangeReason_Type()
)
bRINetworkInterfaceState_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_SparingChangeReason.setStatus("mandatory")
_BRINetworkInterfaceState_SparingChangeTime_Type = Integer32
_BRINetworkInterfaceState_SparingChangeTime_Object = MibScalar
bRINetworkInterfaceState_SparingChangeTime = _BRINetworkInterfaceState_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 14),
    _BRINetworkInterfaceState_SparingChangeTime_Type()
)
bRINetworkInterfaceState_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_SparingChangeTime.setStatus("mandatory")
_BRINetworkInterfaceState_SparingChangeCounter_Type = Integer32
_BRINetworkInterfaceState_SparingChangeCounter_Object = MibScalar
bRINetworkInterfaceState_SparingChangeCounter = _BRINetworkInterfaceState_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 15),
    _BRINetworkInterfaceState_SparingChangeCounter_Type()
)
bRINetworkInterfaceState_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_SparingChangeCounter.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatus_IfGroupIndex_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatus_IfGroupIndex_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatus_IfGroupIndex = _BRINetworkInterfaceState_PhysicalStatus_IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 16),
    _BRINetworkInterfaceState_PhysicalStatus_IfGroupIndex_Type()
)
bRINetworkInterfaceState_PhysicalStatus_IfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatus_IfGroupIndex.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days = _BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 17),
    _BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours = _BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 18),
    _BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes = _BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 19),
    _BRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr = _BRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 1, 1, 20),
    _BRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr.setStatus("mandatory")
_MibbRINetworkInterfaceState_ErrorCountTable_Object = MibTable
mibbRINetworkInterfaceState_ErrorCountTable = _MibbRINetworkInterfaceState_ErrorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 2)
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceState_ErrorCountTable.setStatus("mandatory")
_MibbRINetworkInterfaceState_ErrorCountEntry_Object = MibTableRow
mibbRINetworkInterfaceState_ErrorCountEntry = _MibbRINetworkInterfaceState_ErrorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 2, 1)
)
mibbRINetworkInterfaceState_ErrorCountEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ErrorCount-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ErrorCount-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ErrorCount-Item-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ErrorCount-Index-o"),
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceState_ErrorCountEntry.setStatus("mandatory")
_BRINetworkInterfaceState_ErrorCount_Shelf_o_Type = Integer32
_BRINetworkInterfaceState_ErrorCount_Shelf_o_Object = MibScalar
bRINetworkInterfaceState_ErrorCount_Shelf_o = _BRINetworkInterfaceState_ErrorCount_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 2, 1, 1),
    _BRINetworkInterfaceState_ErrorCount_Shelf_o_Type()
)
bRINetworkInterfaceState_ErrorCount_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ErrorCount_Shelf_o.setStatus("mandatory")
_BRINetworkInterfaceState_ErrorCount_Slot_o_Type = Integer32
_BRINetworkInterfaceState_ErrorCount_Slot_o_Object = MibScalar
bRINetworkInterfaceState_ErrorCount_Slot_o = _BRINetworkInterfaceState_ErrorCount_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 2, 1, 2),
    _BRINetworkInterfaceState_ErrorCount_Slot_o_Type()
)
bRINetworkInterfaceState_ErrorCount_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ErrorCount_Slot_o.setStatus("mandatory")
_BRINetworkInterfaceState_ErrorCount_Item_o_Type = Integer32
_BRINetworkInterfaceState_ErrorCount_Item_o_Object = MibScalar
bRINetworkInterfaceState_ErrorCount_Item_o = _BRINetworkInterfaceState_ErrorCount_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 2, 1, 3),
    _BRINetworkInterfaceState_ErrorCount_Item_o_Type()
)
bRINetworkInterfaceState_ErrorCount_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ErrorCount_Item_o.setStatus("mandatory")
_BRINetworkInterfaceState_ErrorCount_Index_o_Type = Integer32
_BRINetworkInterfaceState_ErrorCount_Index_o_Object = MibScalar
bRINetworkInterfaceState_ErrorCount_Index_o = _BRINetworkInterfaceState_ErrorCount_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 2, 1, 4),
    _BRINetworkInterfaceState_ErrorCount_Index_o_Type()
)
bRINetworkInterfaceState_ErrorCount_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ErrorCount_Index_o.setStatus("mandatory")
_BRINetworkInterfaceState_ErrorCount_Type = Integer32
_BRINetworkInterfaceState_ErrorCount_Object = MibScalar
bRINetworkInterfaceState_ErrorCount = _BRINetworkInterfaceState_ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 2, 1, 5),
    _BRINetworkInterfaceState_ErrorCount_Type()
)
bRINetworkInterfaceState_ErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ErrorCount.setStatus("mandatory")
_MibbRINetworkInterfaceState_ChannelStateTable_Object = MibTable
mibbRINetworkInterfaceState_ChannelStateTable = _MibbRINetworkInterfaceState_ChannelStateTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 3)
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceState_ChannelStateTable.setStatus("mandatory")
_MibbRINetworkInterfaceState_ChannelStateEntry_Object = MibTableRow
mibbRINetworkInterfaceState_ChannelStateEntry = _MibbRINetworkInterfaceState_ChannelStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 3, 1)
)
mibbRINetworkInterfaceState_ChannelStateEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ChannelState-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ChannelState-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ChannelState-Item-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-ChannelState-Index-o"),
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceState_ChannelStateEntry.setStatus("mandatory")
_BRINetworkInterfaceState_ChannelState_Shelf_o_Type = Integer32
_BRINetworkInterfaceState_ChannelState_Shelf_o_Object = MibScalar
bRINetworkInterfaceState_ChannelState_Shelf_o = _BRINetworkInterfaceState_ChannelState_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 3, 1, 1),
    _BRINetworkInterfaceState_ChannelState_Shelf_o_Type()
)
bRINetworkInterfaceState_ChannelState_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ChannelState_Shelf_o.setStatus("mandatory")
_BRINetworkInterfaceState_ChannelState_Slot_o_Type = Integer32
_BRINetworkInterfaceState_ChannelState_Slot_o_Object = MibScalar
bRINetworkInterfaceState_ChannelState_Slot_o = _BRINetworkInterfaceState_ChannelState_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 3, 1, 2),
    _BRINetworkInterfaceState_ChannelState_Slot_o_Type()
)
bRINetworkInterfaceState_ChannelState_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ChannelState_Slot_o.setStatus("mandatory")
_BRINetworkInterfaceState_ChannelState_Item_o_Type = Integer32
_BRINetworkInterfaceState_ChannelState_Item_o_Object = MibScalar
bRINetworkInterfaceState_ChannelState_Item_o = _BRINetworkInterfaceState_ChannelState_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 3, 1, 3),
    _BRINetworkInterfaceState_ChannelState_Item_o_Type()
)
bRINetworkInterfaceState_ChannelState_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ChannelState_Item_o.setStatus("mandatory")
_BRINetworkInterfaceState_ChannelState_Index_o_Type = Integer32
_BRINetworkInterfaceState_ChannelState_Index_o_Object = MibScalar
bRINetworkInterfaceState_ChannelState_Index_o = _BRINetworkInterfaceState_ChannelState_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 3, 1, 4),
    _BRINetworkInterfaceState_ChannelState_Index_o_Type()
)
bRINetworkInterfaceState_ChannelState_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ChannelState_Index_o.setStatus("mandatory")


class _BRINetworkInterfaceState_ChannelState_Type(Integer32):
    """Custom type bRINetworkInterfaceState_ChannelState based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("backupD", 15),
          ("clearPending", 8),
          ("connected", 11),
          ("currentD", 14),
          ("cutThrough", 13),
          ("dialing", 9),
          ("disabled", 18),
          ("held", 5),
          ("idle", 7),
          ("maintainence", 16),
          ("nailedUp", 4),
          ("offHook", 6),
          ("outOfService", 3),
          ("ringing", 10),
          ("signaling", 12),
          ("spcUp", 17),
          ("unavailable", 1),
          ("unused", 2))
    )


_BRINetworkInterfaceState_ChannelState_Type.__name__ = "Integer32"
_BRINetworkInterfaceState_ChannelState_Object = MibScalar
bRINetworkInterfaceState_ChannelState = _BRINetworkInterfaceState_ChannelState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 3, 1, 5),
    _BRINetworkInterfaceState_ChannelState_Type()
)
bRINetworkInterfaceState_ChannelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_ChannelState.setStatus("mandatory")
_MibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountTable_Object = MibTable
mibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountTable = _MibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 4)
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountTable.setStatus("mandatory")
_MibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountEntry_Object = MibTableRow
mibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountEntry = _MibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 4, 1)
)
mibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Item-o"),
    (0, "ASCEND-MIBSTAT-MIB", "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Index-o"),
)
if mibBuilder.loadTexts:
    mibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountEntry.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o = _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 4, 1, 1),
    _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o = _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 4, 1, 2),
    _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o = _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 4, 1, 3),
    _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o = _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 4, 1, 4),
    _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o.setStatus("mandatory")
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Type = Integer32
_BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Object = MibScalar
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount = _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 28, 4, 1, 5),
    _BRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Type()
)
bRINetworkInterfaceState_PhysicalStatistic_ErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bRINetworkInterfaceState_PhysicalStatistic_ErrorCount.setStatus("mandatory")
_MibsdslLineStatus_ObjectIdentity = ObjectIdentity
mibsdslLineStatus = _MibsdslLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 180)
)
_MibsdslLineStatusTable_Object = MibTable
mibsdslLineStatusTable = _MibsdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1)
)
if mibBuilder.loadTexts:
    mibsdslLineStatusTable.setStatus("mandatory")
_MibsdslLineStatusEntry_Object = MibTableRow
mibsdslLineStatusEntry = _MibsdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1)
)
mibsdslLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "sdslLineStatus-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "sdslLineStatus-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "sdslLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibsdslLineStatusEntry.setStatus("mandatory")
_SdslLineStatus_Shelf_o_Type = Integer32
_SdslLineStatus_Shelf_o_Object = MibScalar
sdslLineStatus_Shelf_o = _SdslLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 1),
    _SdslLineStatus_Shelf_o_Type()
)
sdslLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_Shelf_o.setStatus("mandatory")
_SdslLineStatus_Slot_o_Type = Integer32
_SdslLineStatus_Slot_o_Object = MibScalar
sdslLineStatus_Slot_o = _SdslLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 2),
    _SdslLineStatus_Slot_o_Type()
)
sdslLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_Slot_o.setStatus("mandatory")
_SdslLineStatus_Item_o_Type = Integer32
_SdslLineStatus_Item_o_Object = MibScalar
sdslLineStatus_Item_o = _SdslLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 3),
    _SdslLineStatus_Item_o_Type()
)
sdslLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_Item_o.setStatus("mandatory")


class _SdslLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type sdslLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_SdslLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_SdslLineStatus_PhysicalAddress_Shelf_Object = MibScalar
sdslLineStatus_PhysicalAddress_Shelf = _SdslLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 4),
    _SdslLineStatus_PhysicalAddress_Shelf_Type()
)
sdslLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _SdslLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type sdslLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_SdslLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_SdslLineStatus_PhysicalAddress_Slot_Object = MibScalar
sdslLineStatus_PhysicalAddress_Slot = _SdslLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 5),
    _SdslLineStatus_PhysicalAddress_Slot_Type()
)
sdslLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_SdslLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_SdslLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
sdslLineStatus_PhysicalAddress_ItemNumber = _SdslLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 6),
    _SdslLineStatus_PhysicalAddress_ItemNumber_Type()
)
sdslLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _SdslLineStatus_LineState_Type(Integer32):
    """Custom type sdslLineStatus_LineState based on Integer32"""
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


_SdslLineStatus_LineState_Type.__name__ = "Integer32"
_SdslLineStatus_LineState_Object = MibScalar
sdslLineStatus_LineState = _SdslLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 7),
    _SdslLineStatus_LineState_Type()
)
sdslLineStatus_LineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_LineState.setStatus("mandatory")


class _SdslLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type sdslLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_SdslLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_SdslLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
sdslLineStatus_SparePhysicalAddress_Shelf = _SdslLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 8),
    _SdslLineStatus_SparePhysicalAddress_Shelf_Type()
)
sdslLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _SdslLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type sdslLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_SdslLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_SdslLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
sdslLineStatus_SparePhysicalAddress_Slot = _SdslLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 9),
    _SdslLineStatus_SparePhysicalAddress_Slot_Type()
)
sdslLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_SdslLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_SdslLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
sdslLineStatus_SparePhysicalAddress_ItemNumber = _SdslLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 10),
    _SdslLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
sdslLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _SdslLineStatus_SparingState_Type(Integer32):
    """Custom type sdslLineStatus_SparingState based on Integer32"""
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


_SdslLineStatus_SparingState_Type.__name__ = "Integer32"
_SdslLineStatus_SparingState_Object = MibScalar
sdslLineStatus_SparingState = _SdslLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 11),
    _SdslLineStatus_SparingState_Type()
)
sdslLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_SparingState.setStatus("mandatory")


class _SdslLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type sdslLineStatus_SparingChangeReason based on Integer32"""
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


_SdslLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_SdslLineStatus_SparingChangeReason_Object = MibScalar
sdslLineStatus_SparingChangeReason = _SdslLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 12),
    _SdslLineStatus_SparingChangeReason_Type()
)
sdslLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_SparingChangeReason.setStatus("mandatory")
_SdslLineStatus_SparingChangeTime_Type = Integer32
_SdslLineStatus_SparingChangeTime_Object = MibScalar
sdslLineStatus_SparingChangeTime = _SdslLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 13),
    _SdslLineStatus_SparingChangeTime_Type()
)
sdslLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_SparingChangeTime.setStatus("mandatory")
_SdslLineStatus_SparingChangeCounter_Type = Integer32
_SdslLineStatus_SparingChangeCounter_Object = MibScalar
sdslLineStatus_SparingChangeCounter = _SdslLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 14),
    _SdslLineStatus_SparingChangeCounter_Type()
)
sdslLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_SparingChangeCounter.setStatus("mandatory")


class _SdslLineStatus_VpiVciRange_Type(Integer32):
    """Custom type sdslLineStatus_VpiVciRange based on Integer32"""
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


_SdslLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_SdslLineStatus_VpiVciRange_Object = MibScalar
sdslLineStatus_VpiVciRange = _SdslLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 15),
    _SdslLineStatus_VpiVciRange_Type()
)
sdslLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_VpiVciRange.setStatus("mandatory")
_SdslLineStatus_VpSwitchingVpi_Type = Integer32
_SdslLineStatus_VpSwitchingVpi_Object = MibScalar
sdslLineStatus_VpSwitchingVpi = _SdslLineStatus_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 16),
    _SdslLineStatus_VpSwitchingVpi_Type()
)
sdslLineStatus_VpSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_VpSwitchingVpi.setStatus("mandatory")
_SdslLineStatus_ErrorCount_Type = Integer32
_SdslLineStatus_ErrorCount_Object = MibScalar
sdslLineStatus_ErrorCount = _SdslLineStatus_ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 17),
    _SdslLineStatus_ErrorCount_Type()
)
sdslLineStatus_ErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_ErrorCount.setStatus("mandatory")
_SdslLineStatus_PhysicalStatus_IfGroupIndex_Type = Integer32
_SdslLineStatus_PhysicalStatus_IfGroupIndex_Object = MibScalar
sdslLineStatus_PhysicalStatus_IfGroupIndex = _SdslLineStatus_PhysicalStatus_IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 18),
    _SdslLineStatus_PhysicalStatus_IfGroupIndex_Type()
)
sdslLineStatus_PhysicalStatus_IfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_IfGroupIndex.setStatus("mandatory")


class _SdslLineStatus_PhysicalStatus_UnitType_Type(Integer32):
    """Custom type sdslLineStatus_PhysicalStatus_UnitType based on Integer32"""
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


_SdslLineStatus_PhysicalStatus_UnitType_Type.__name__ = "Integer32"
_SdslLineStatus_PhysicalStatus_UnitType_Object = MibScalar
sdslLineStatus_PhysicalStatus_UnitType = _SdslLineStatus_PhysicalStatus_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 19),
    _SdslLineStatus_PhysicalStatus_UnitType_Type()
)
sdslLineStatus_PhysicalStatus_UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_UnitType.setStatus("mandatory")


class _SdslLineStatus_PhysicalStatus_DevLineState_Type(Integer32):
    """Custom type sdslLineStatus_PhysicalStatus_DevLineState based on Integer32"""
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
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("activating", 4),
          ("activeRx", 5),
          ("alteraTipHunt", 19),
          ("cellDelination", 16),
          ("config", 1),
          ("deactivate", 2),
          ("deactivateLost", 8),
          ("deactivateWait", 17),
          ("foreverBert", 12),
          ("hardwareTest", 9),
          ("inactive", 3),
          ("outOfService", 10),
          ("portUp", 6),
          ("portupPendingDeactivate", 7),
          ("preact", 20),
          ("preactWait", 21),
          ("tipHunt", 14),
          ("tipRingDetect", 11),
          ("tipWait1", 13),
          ("tipWait2", 15))
    )


_SdslLineStatus_PhysicalStatus_DevLineState_Type.__name__ = "Integer32"
_SdslLineStatus_PhysicalStatus_DevLineState_Object = MibScalar
sdslLineStatus_PhysicalStatus_DevLineState = _SdslLineStatus_PhysicalStatus_DevLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 20),
    _SdslLineStatus_PhysicalStatus_DevLineState_Type()
)
sdslLineStatus_PhysicalStatus_DevLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_DevLineState.setStatus("mandatory")
_SdslLineStatus_PhysicalStatus_UpStreamRate_Type = Integer32
_SdslLineStatus_PhysicalStatus_UpStreamRate_Object = MibScalar
sdslLineStatus_PhysicalStatus_UpStreamRate = _SdslLineStatus_PhysicalStatus_UpStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 21),
    _SdslLineStatus_PhysicalStatus_UpStreamRate_Type()
)
sdslLineStatus_PhysicalStatus_UpStreamRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_UpStreamRate.setStatus("mandatory")
_SdslLineStatus_PhysicalStatus_DownStreamRate_Type = Integer32
_SdslLineStatus_PhysicalStatus_DownStreamRate_Object = MibScalar
sdslLineStatus_PhysicalStatus_DownStreamRate = _SdslLineStatus_PhysicalStatus_DownStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 22),
    _SdslLineStatus_PhysicalStatus_DownStreamRate_Type()
)
sdslLineStatus_PhysicalStatus_DownStreamRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_DownStreamRate.setStatus("mandatory")
_SdslLineStatus_PhysicalStatus_MajorFirmwareVer_Type = Integer32
_SdslLineStatus_PhysicalStatus_MajorFirmwareVer_Object = MibScalar
sdslLineStatus_PhysicalStatus_MajorFirmwareVer = _SdslLineStatus_PhysicalStatus_MajorFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 23),
    _SdslLineStatus_PhysicalStatus_MajorFirmwareVer_Type()
)
sdslLineStatus_PhysicalStatus_MajorFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_MajorFirmwareVer.setStatus("mandatory")
_SdslLineStatus_PhysicalStatus_MinorFirmwareVer_Type = Integer32
_SdslLineStatus_PhysicalStatus_MinorFirmwareVer_Object = MibScalar
sdslLineStatus_PhysicalStatus_MinorFirmwareVer = _SdslLineStatus_PhysicalStatus_MinorFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 24),
    _SdslLineStatus_PhysicalStatus_MinorFirmwareVer_Type()
)
sdslLineStatus_PhysicalStatus_MinorFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_MinorFirmwareVer.setStatus("mandatory")
_SdslLineStatus_PhysicalStatus_HardwareVer_Type = Integer32
_SdslLineStatus_PhysicalStatus_HardwareVer_Object = MibScalar
sdslLineStatus_PhysicalStatus_HardwareVer = _SdslLineStatus_PhysicalStatus_HardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 25),
    _SdslLineStatus_PhysicalStatus_HardwareVer_Type()
)
sdslLineStatus_PhysicalStatus_HardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatus_HardwareVer.setStatus("mandatory")
_SdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type = Integer32
_SdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object = MibScalar
sdslLineStatus_PhysicalStatistic_LineUpTimer_Days = _SdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 26),
    _SdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type()
)
sdslLineStatus_PhysicalStatistic_LineUpTimer_Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_LineUpTimer_Days.setStatus("mandatory")
_SdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type = Integer32
_SdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object = MibScalar
sdslLineStatus_PhysicalStatistic_LineUpTimer_Hours = _SdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 27),
    _SdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type()
)
sdslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setStatus("mandatory")
_SdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type = Integer32
_SdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object = MibScalar
sdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes = _SdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 28),
    _SdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type()
)
sdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setStatus("mandatory")


class _SdslLineStatus_PhysicalStatistic_RxSignalPresent_Type(Integer32):
    """Custom type sdslLineStatus_PhysicalStatistic_RxSignalPresent based on Integer32"""
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


_SdslLineStatus_PhysicalStatistic_RxSignalPresent_Type.__name__ = "Integer32"
_SdslLineStatus_PhysicalStatistic_RxSignalPresent_Object = MibScalar
sdslLineStatus_PhysicalStatistic_RxSignalPresent = _SdslLineStatus_PhysicalStatistic_RxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 29),
    _SdslLineStatus_PhysicalStatistic_RxSignalPresent_Type()
)
sdslLineStatus_PhysicalStatistic_RxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_RxSignalPresent.setStatus("mandatory")
_SdslLineStatus_PhysicalStatistic_LineQuality_Type = Integer32
_SdslLineStatus_PhysicalStatistic_LineQuality_Object = MibScalar
sdslLineStatus_PhysicalStatistic_LineQuality = _SdslLineStatus_PhysicalStatistic_LineQuality_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 30),
    _SdslLineStatus_PhysicalStatistic_LineQuality_Type()
)
sdslLineStatus_PhysicalStatistic_LineQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_LineQuality.setStatus("mandatory")
_SdslLineStatus_PhysicalStatistic_UpDwnCntr_Type = Integer32
_SdslLineStatus_PhysicalStatistic_UpDwnCntr_Object = MibScalar
sdslLineStatus_PhysicalStatistic_UpDwnCntr = _SdslLineStatus_PhysicalStatistic_UpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 31),
    _SdslLineStatus_PhysicalStatistic_UpDwnCntr_Type()
)
sdslLineStatus_PhysicalStatistic_UpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_UpDwnCntr.setStatus("mandatory")


class _SdslLineStatus_PhysicalStatistic_SelfTest_Type(Integer32):
    """Custom type sdslLineStatus_PhysicalStatistic_SelfTest based on Integer32"""
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


_SdslLineStatus_PhysicalStatistic_SelfTest_Type.__name__ = "Integer32"
_SdslLineStatus_PhysicalStatistic_SelfTest_Object = MibScalar
sdslLineStatus_PhysicalStatistic_SelfTest = _SdslLineStatus_PhysicalStatistic_SelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 32),
    _SdslLineStatus_PhysicalStatistic_SelfTest_Type()
)
sdslLineStatus_PhysicalStatistic_SelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_SelfTest.setStatus("mandatory")
_SdslLineStatus_PhysicalStatistic_FarEndDbAttenuation_Type = Integer32
_SdslLineStatus_PhysicalStatistic_FarEndDbAttenuation_Object = MibScalar
sdslLineStatus_PhysicalStatistic_FarEndDbAttenuation = _SdslLineStatus_PhysicalStatistic_FarEndDbAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 33),
    _SdslLineStatus_PhysicalStatistic_FarEndDbAttenuation_Type()
)
sdslLineStatus_PhysicalStatistic_FarEndDbAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_FarEndDbAttenuation.setStatus("mandatory")


class _SdslLineStatus_PhysicalStatistic_FirmwareStartupStage_Type(Integer32):
    """Custom type sdslLineStatus_PhysicalStatistic_FirmwareStartupStage based on Integer32"""
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
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65)
        )
    )
    namedValues = NamedValues(
        *(("acquireFreq1", 46),
          ("acquireFreq2", 47),
          ("acquireFreq3", 48),
          ("acquireFreq4", 49),
          ("acquireFreq5", 50),
          ("activateSystem", 2),
          ("adaptAagc1", 16),
          ("adaptAagc2", 17),
          ("adaptAagc3", 18),
          ("adaptDagcAfterAagc", 54),
          ("adaptEc1", 12),
          ("adaptEc2", 13),
          ("adaptEc3", 14),
          ("adaptEcAfterAagc1", 8),
          ("adaptEcAfterAagc2", 9),
          ("adaptEcAfterAagc3", 10),
          ("adaptEcAfterAagc4", 11),
          ("adaptEcStage1", 5),
          ("adaptEcStage2", 6),
          ("adaptEcStage3", 7),
          ("adaptEq1", 55),
          ("adaptEq2", 56),
          ("adaptEq3", 57),
          ("adaptModules1", 61),
          ("adaptModules2", 62),
          ("dcCancellation", 3),
          ("deactivateMode", 65),
          ("idle", 1),
          ("initStartup", 4),
          ("normalOperation", 64),
          ("openEye1", 22),
          ("openEye2", 23),
          ("openEye3", 24),
          ("openEye4", 25),
          ("openEye5", 26),
          ("openEye6", 27),
          ("openEye7", 28),
          ("openEyeAtOptimalPhase1", 29),
          ("openEyeAtOptimalPhase10", 38),
          ("openEyeAtOptimalPhase11", 39),
          ("openEyeAtOptimalPhase12", 40),
          ("openEyeAtOptimalPhase13", 41),
          ("openEyeAtOptimalPhase2", 30),
          ("openEyeAtOptimalPhase3", 31),
          ("openEyeAtOptimalPhase4", 32),
          ("openEyeAtOptimalPhase5", 33),
          ("openEyeAtOptimalPhase6", 34),
          ("openEyeAtOptimalPhase7", 35),
          ("openEyeAtOptimalPhase8", 36),
          ("openEyeAtOptimalPhase9", 37),
          ("optimalPhase", 52),
          ("phaseAdaptEc1", 42),
          ("phaseAdaptEc2", 43),
          ("phaseAdaptEc3", 44),
          ("phaseAdaptEc4", 45),
          ("phaseLocked", 51),
          ("remotePhaseLock", 20),
          ("setNormalConditions", 63),
          ("startOpenEye", 21),
          ("transmit4Level", 59),
          ("tx2Level", 53),
          ("waitFor1Min", 58),
          ("waitFor4Level", 60),
          ("waitForRemotePhaseLock", 19),
          ("waitForSignal", 15))
    )


_SdslLineStatus_PhysicalStatistic_FirmwareStartupStage_Type.__name__ = "Integer32"
_SdslLineStatus_PhysicalStatistic_FirmwareStartupStage_Object = MibScalar
sdslLineStatus_PhysicalStatistic_FirmwareStartupStage = _SdslLineStatus_PhysicalStatistic_FirmwareStartupStage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 34),
    _SdslLineStatus_PhysicalStatistic_FirmwareStartupStage_Type()
)
sdslLineStatus_PhysicalStatistic_FirmwareStartupStage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_FirmwareStartupStage.setStatus("mandatory")
_SdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt_Type = Integer32
_SdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt_Object = MibScalar
sdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt = _SdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 35),
    _SdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt_Type()
)
sdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt.setStatus("mandatory")


class _SdslLineStatus_Action_o_Type(Integer32):
    """Custom type sdslLineStatus_Action_o based on Integer32"""
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


_SdslLineStatus_Action_o_Type.__name__ = "Integer32"
_SdslLineStatus_Action_o_Object = MibScalar
sdslLineStatus_Action_o = _SdslLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 180, 1, 1, 36),
    _SdslLineStatus_Action_o_Type()
)
sdslLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslLineStatus_Action_o.setStatus("mandatory")
_MibdmtAlDslLineStatus_ObjectIdentity = ObjectIdentity
mibdmtAlDslLineStatus = _MibdmtAlDslLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 181)
)
_MibdmtAlDslLineStatusTable_Object = MibTable
mibdmtAlDslLineStatusTable = _MibdmtAlDslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1)
)
if mibBuilder.loadTexts:
    mibdmtAlDslLineStatusTable.setStatus("mandatory")
_MibdmtAlDslLineStatusEntry_Object = MibTableRow
mibdmtAlDslLineStatusEntry = _MibdmtAlDslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1)
)
mibdmtAlDslLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "dmtAlDslLineStatus-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "dmtAlDslLineStatus-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "dmtAlDslLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibdmtAlDslLineStatusEntry.setStatus("mandatory")
_DmtAlDslLineStatus_Shelf_o_Type = Integer32
_DmtAlDslLineStatus_Shelf_o_Object = MibScalar
dmtAlDslLineStatus_Shelf_o = _DmtAlDslLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 1),
    _DmtAlDslLineStatus_Shelf_o_Type()
)
dmtAlDslLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_Shelf_o.setStatus("mandatory")
_DmtAlDslLineStatus_Slot_o_Type = Integer32
_DmtAlDslLineStatus_Slot_o_Object = MibScalar
dmtAlDslLineStatus_Slot_o = _DmtAlDslLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 2),
    _DmtAlDslLineStatus_Slot_o_Type()
)
dmtAlDslLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_Slot_o.setStatus("mandatory")
_DmtAlDslLineStatus_Item_o_Type = Integer32
_DmtAlDslLineStatus_Item_o_Object = MibScalar
dmtAlDslLineStatus_Item_o = _DmtAlDslLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 3),
    _DmtAlDslLineStatus_Item_o_Type()
)
dmtAlDslLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_Item_o.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_DmtAlDslLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalAddress_Shelf_Object = MibScalar
dmtAlDslLineStatus_PhysicalAddress_Shelf = _DmtAlDslLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 4),
    _DmtAlDslLineStatus_PhysicalAddress_Shelf_Type()
)
dmtAlDslLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_DmtAlDslLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalAddress_Slot_Object = MibScalar
dmtAlDslLineStatus_PhysicalAddress_Slot = _DmtAlDslLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 5),
    _DmtAlDslLineStatus_PhysicalAddress_Slot_Type()
)
dmtAlDslLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_DmtAlDslLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
dmtAlDslLineStatus_PhysicalAddress_ItemNumber = _DmtAlDslLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 6),
    _DmtAlDslLineStatus_PhysicalAddress_ItemNumber_Type()
)
dmtAlDslLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _DmtAlDslLineStatus_LineState_Type(Integer32):
    """Custom type dmtAlDslLineStatus_LineState based on Integer32"""
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


_DmtAlDslLineStatus_LineState_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_LineState_Object = MibScalar
dmtAlDslLineStatus_LineState = _DmtAlDslLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 7),
    _DmtAlDslLineStatus_LineState_Type()
)
dmtAlDslLineStatus_LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_LineState.setStatus("mandatory")


class _DmtAlDslLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type dmtAlDslLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_DmtAlDslLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
dmtAlDslLineStatus_SparePhysicalAddress_Shelf = _DmtAlDslLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 8),
    _DmtAlDslLineStatus_SparePhysicalAddress_Shelf_Type()
)
dmtAlDslLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _DmtAlDslLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type dmtAlDslLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_DmtAlDslLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
dmtAlDslLineStatus_SparePhysicalAddress_Slot = _DmtAlDslLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 9),
    _DmtAlDslLineStatus_SparePhysicalAddress_Slot_Type()
)
dmtAlDslLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_DmtAlDslLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_DmtAlDslLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
dmtAlDslLineStatus_SparePhysicalAddress_ItemNumber = _DmtAlDslLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 10),
    _DmtAlDslLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
dmtAlDslLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _DmtAlDslLineStatus_SparingState_Type(Integer32):
    """Custom type dmtAlDslLineStatus_SparingState based on Integer32"""
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


_DmtAlDslLineStatus_SparingState_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_SparingState_Object = MibScalar
dmtAlDslLineStatus_SparingState = _DmtAlDslLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 11),
    _DmtAlDslLineStatus_SparingState_Type()
)
dmtAlDslLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_SparingState.setStatus("mandatory")


class _DmtAlDslLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type dmtAlDslLineStatus_SparingChangeReason based on Integer32"""
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


_DmtAlDslLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_SparingChangeReason_Object = MibScalar
dmtAlDslLineStatus_SparingChangeReason = _DmtAlDslLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 12),
    _DmtAlDslLineStatus_SparingChangeReason_Type()
)
dmtAlDslLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_SparingChangeReason.setStatus("mandatory")
_DmtAlDslLineStatus_SparingChangeTime_Type = Integer32
_DmtAlDslLineStatus_SparingChangeTime_Object = MibScalar
dmtAlDslLineStatus_SparingChangeTime = _DmtAlDslLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 13),
    _DmtAlDslLineStatus_SparingChangeTime_Type()
)
dmtAlDslLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_SparingChangeTime.setStatus("mandatory")
_DmtAlDslLineStatus_SparingChangeCounter_Type = Integer32
_DmtAlDslLineStatus_SparingChangeCounter_Object = MibScalar
dmtAlDslLineStatus_SparingChangeCounter = _DmtAlDslLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 14),
    _DmtAlDslLineStatus_SparingChangeCounter_Type()
)
dmtAlDslLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_SparingChangeCounter.setStatus("mandatory")


class _DmtAlDslLineStatus_VpiVciRange_Type(Integer32):
    """Custom type dmtAlDslLineStatus_VpiVciRange based on Integer32"""
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


_DmtAlDslLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_VpiVciRange_Object = MibScalar
dmtAlDslLineStatus_VpiVciRange = _DmtAlDslLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 15),
    _DmtAlDslLineStatus_VpiVciRange_Type()
)
dmtAlDslLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_VpiVciRange.setStatus("mandatory")
_DmtAlDslLineStatus_VpSwitchingVpi_Type = Integer32
_DmtAlDslLineStatus_VpSwitchingVpi_Object = MibScalar
dmtAlDslLineStatus_VpSwitchingVpi = _DmtAlDslLineStatus_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 16),
    _DmtAlDslLineStatus_VpSwitchingVpi_Type()
)
dmtAlDslLineStatus_VpSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_VpSwitchingVpi.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_IfGroupIndex_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_IfGroupIndex_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_IfGroupIndex = _DmtAlDslLineStatus_PhysicalStatus_IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 17),
    _DmtAlDslLineStatus_PhysicalStatus_IfGroupIndex_Type()
)
dmtAlDslLineStatus_PhysicalStatus_IfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_IfGroupIndex.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatus_UnitType_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatus_UnitType based on Integer32"""
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


_DmtAlDslLineStatus_PhysicalStatus_UnitType_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatus_UnitType_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_UnitType = _DmtAlDslLineStatus_PhysicalStatus_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 18),
    _DmtAlDslLineStatus_PhysicalStatus_UnitType_Type()
)
dmtAlDslLineStatus_PhysicalStatus_UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_UnitType.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatus_DevLineState_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatus_DevLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9,
              17,
              33,
              86,
              106,
              122,
              138,
              154,
              256)
        )
    )
    namedValues = NamedValues(
        *(("activation", 9),
          ("down", 1),
          ("download", 138),
          ("dummy", 86),
          ("failed", 256),
          ("fastRetrain", 154),
          ("loopback", 106),
          ("portUp", 33),
          ("test", 122),
          ("training", 17))
    )


_DmtAlDslLineStatus_PhysicalStatus_DevLineState_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatus_DevLineState_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_DevLineState = _DmtAlDslLineStatus_PhysicalStatus_DevLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 19),
    _DmtAlDslLineStatus_PhysicalStatus_DevLineState_Type()
)
dmtAlDslLineStatus_PhysicalStatus_DevLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_DevLineState.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast = _DmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 20),
    _DmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast_Type()
)
dmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast = _DmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 21),
    _DmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast_Type()
)
dmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved = _DmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 22),
    _DmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved_Type()
)
dmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved = _DmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 23),
    _DmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved_Type()
)
dmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatus_UpStreamLatency_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatus_UpStreamLatency based on Integer32"""
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
        *(("both", 4),
          ("fast", 2),
          ("interleave", 3),
          ("none", 1))
    )


_DmtAlDslLineStatus_PhysicalStatus_UpStreamLatency_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatus_UpStreamLatency_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_UpStreamLatency = _DmtAlDslLineStatus_PhysicalStatus_UpStreamLatency_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 24),
    _DmtAlDslLineStatus_PhysicalStatus_UpStreamLatency_Type()
)
dmtAlDslLineStatus_PhysicalStatus_UpStreamLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_UpStreamLatency.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatus_DownStreamLatency_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatus_DownStreamLatency based on Integer32"""
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
        *(("both", 4),
          ("fast", 2),
          ("interleave", 3),
          ("none", 1))
    )


_DmtAlDslLineStatus_PhysicalStatus_DownStreamLatency_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatus_DownStreamLatency_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_DownStreamLatency = _DmtAlDslLineStatus_PhysicalStatus_DownStreamLatency_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 25),
    _DmtAlDslLineStatus_PhysicalStatus_DownStreamLatency_Type()
)
dmtAlDslLineStatus_PhysicalStatus_DownStreamLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_DownStreamLatency.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_FirmwareVer_Type = DisplayString
_DmtAlDslLineStatus_PhysicalStatus_FirmwareVer_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_FirmwareVer = _DmtAlDslLineStatus_PhysicalStatus_FirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 26),
    _DmtAlDslLineStatus_PhysicalStatus_FirmwareVer_Type()
)
dmtAlDslLineStatus_PhysicalStatus_FirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_FirmwareVer.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer = _DmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 27),
    _DmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer_Type()
)
dmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_InitialAdslVer_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_InitialAdslVer_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_InitialAdslVer = _DmtAlDslLineStatus_PhysicalStatus_InitialAdslVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 28),
    _DmtAlDslLineStatus_PhysicalStatus_InitialAdslVer_Type()
)
dmtAlDslLineStatus_PhysicalStatus_InitialAdslVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_InitialAdslVer.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_HardwareVer_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_HardwareVer_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_HardwareVer = _DmtAlDslLineStatus_PhysicalStatus_HardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 29),
    _DmtAlDslLineStatus_PhysicalStatus_HardwareVer_Type()
)
dmtAlDslLineStatus_PhysicalStatus_HardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_HardwareVer.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatus_ModemHwState_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatus_ModemHwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("badCache", 131),
          ("badCacheSdram", 132),
          ("badSdram", 130),
          ("down", 1),
          ("initOk", 129))
    )


_DmtAlDslLineStatus_PhysicalStatus_ModemHwState_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatus_ModemHwState_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_ModemHwState = _DmtAlDslLineStatus_PhysicalStatus_ModemHwState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 30),
    _DmtAlDslLineStatus_PhysicalStatus_ModemHwState_Type()
)
dmtAlDslLineStatus_PhysicalStatus_ModemHwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_ModemHwState.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_AccumBitErr_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_AccumBitErr_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_AccumBitErr = _DmtAlDslLineStatus_PhysicalStatus_AccumBitErr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 31),
    _DmtAlDslLineStatus_PhysicalStatus_AccumBitErr_Type()
)
dmtAlDslLineStatus_PhysicalStatus_AccumBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_AccumBitErr.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_NumSecValid_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_NumSecValid_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_NumSecValid = _DmtAlDslLineStatus_PhysicalStatus_NumSecValid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 32),
    _DmtAlDslLineStatus_PhysicalStatus_NumSecValid_Type()
)
dmtAlDslLineStatus_PhysicalStatus_NumSecValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_NumSecValid.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatus_NumSecInvalid_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatus_NumSecInvalid_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_NumSecInvalid = _DmtAlDslLineStatus_PhysicalStatus_NumSecInvalid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 33),
    _DmtAlDslLineStatus_PhysicalStatus_NumSecInvalid_Type()
)
dmtAlDslLineStatus_PhysicalStatus_NumSecInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_NumSecInvalid.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatus_OperationalMode_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatus_OperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              9,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266)
        )
    )
    namedValues = NamedValues(
        *(("annexB", 261),
          ("annexBEtsi", 266),
          ("annexCGdmtDbm", 265),
          ("annexCGdmtFbm", 263),
          ("annexCGliteDbm", 264),
          ("annexCGliteFbm", 262),
          ("ansiAdi", 258),
          ("ansiAlcatel141", 257),
          ("ansiAlcatelPost141", 259),
          ("ansiDmt", 2),
          ("gDmt", 3),
          ("gLite", 9),
          ("uawg", 260),
          ("unknown", 256))
    )


_DmtAlDslLineStatus_PhysicalStatus_OperationalMode_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatus_OperationalMode_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatus_OperationalMode = _DmtAlDslLineStatus_PhysicalStatus_OperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 34),
    _DmtAlDslLineStatus_PhysicalStatus_OperationalMode_Type()
)
dmtAlDslLineStatus_PhysicalStatus_OperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatus_OperationalMode.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days = _DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 35),
    _DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours = _DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 36),
    _DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes = _DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 37),
    _DmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent based on Integer32"""
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


_DmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent = _DmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 38),
    _DmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr = _DmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 39),
    _DmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr.setStatus("mandatory")


class _DmtAlDslLineStatus_PhysicalStatistic_SelfTest_Type(Integer32):
    """Custom type dmtAlDslLineStatus_PhysicalStatistic_SelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("notDone", 1),
          ("passed", 3))
    )


_DmtAlDslLineStatus_PhysicalStatistic_SelfTest_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_PhysicalStatistic_SelfTest_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_SelfTest = _DmtAlDslLineStatus_PhysicalStatistic_SelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 40),
    _DmtAlDslLineStatus_PhysicalStatistic_SelfTest_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_SelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_SelfTest.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown = _DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 41),
    _DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_AttenuationDown_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_AttenuationDown_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_AttenuationDown = _DmtAlDslLineStatus_PhysicalStatistic_AttenuationDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 42),
    _DmtAlDslLineStatus_PhysicalStatistic_AttenuationDown_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_AttenuationDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_AttenuationDown.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown = _DmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 43),
    _DmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp = _DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 44),
    _DmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_AttenuationUp_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_AttenuationUp_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_AttenuationUp = _DmtAlDslLineStatus_PhysicalStatistic_AttenuationUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 45),
    _DmtAlDslLineStatus_PhysicalStatistic_AttenuationUp_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_AttenuationUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_AttenuationUp.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp = _DmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 46),
    _DmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_NearEndFec_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_NearEndFec_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_NearEndFec = _DmtAlDslLineStatus_PhysicalStatistic_NearEndFec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 47),
    _DmtAlDslLineStatus_PhysicalStatistic_NearEndFec_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_NearEndFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_NearEndFec.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_NearEndCrc_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_NearEndCrc_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_NearEndCrc = _DmtAlDslLineStatus_PhysicalStatistic_NearEndCrc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 48),
    _DmtAlDslLineStatus_PhysicalStatistic_NearEndCrc_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_NearEndCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_NearEndCrc.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_NearEndHec_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_NearEndHec_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_NearEndHec = _DmtAlDslLineStatus_PhysicalStatistic_NearEndHec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 49),
    _DmtAlDslLineStatus_PhysicalStatistic_NearEndHec_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_NearEndHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_NearEndHec.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_FarEndFec_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_FarEndFec_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_FarEndFec = _DmtAlDslLineStatus_PhysicalStatistic_FarEndFec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 50),
    _DmtAlDslLineStatus_PhysicalStatistic_FarEndFec_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_FarEndFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_FarEndFec.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_FarEndCrc_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_FarEndCrc_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_FarEndCrc = _DmtAlDslLineStatus_PhysicalStatistic_FarEndCrc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 51),
    _DmtAlDslLineStatus_PhysicalStatistic_FarEndCrc_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_FarEndCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_FarEndCrc.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_FarEndHec_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_FarEndHec_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_FarEndHec = _DmtAlDslLineStatus_PhysicalStatistic_FarEndHec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 52),
    _DmtAlDslLineStatus_PhysicalStatistic_FarEndHec_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_FarEndHec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_FarEndHec.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks = _DmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 53),
    _DmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks = _DmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 54),
    _DmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_IncomingCells_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_IncomingCells_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_IncomingCells = _DmtAlDslLineStatus_PhysicalStatistic_IncomingCells_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 55),
    _DmtAlDslLineStatus_PhysicalStatistic_IncomingCells_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_IncomingCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_IncomingCells.setStatus("mandatory")
_DmtAlDslLineStatus_PhysicalStatistic_OutgoingCells_Type = Integer32
_DmtAlDslLineStatus_PhysicalStatistic_OutgoingCells_Object = MibScalar
dmtAlDslLineStatus_PhysicalStatistic_OutgoingCells = _DmtAlDslLineStatus_PhysicalStatistic_OutgoingCells_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 56),
    _DmtAlDslLineStatus_PhysicalStatistic_OutgoingCells_Type()
)
dmtAlDslLineStatus_PhysicalStatistic_OutgoingCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_PhysicalStatistic_OutgoingCells.setStatus("mandatory")


class _DmtAlDslLineStatus_Action_o_Type(Integer32):
    """Custom type dmtAlDslLineStatus_Action_o based on Integer32"""
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


_DmtAlDslLineStatus_Action_o_Type.__name__ = "Integer32"
_DmtAlDslLineStatus_Action_o_Object = MibScalar
dmtAlDslLineStatus_Action_o = _DmtAlDslLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 181, 1, 1, 57),
    _DmtAlDslLineStatus_Action_o_Type()
)
dmtAlDslLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslLineStatus_Action_o.setStatus("mandatory")
_Mibds3AtmLineStatus_ObjectIdentity = ObjectIdentity
mibds3AtmLineStatus = _Mibds3AtmLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 182)
)
_Mibds3AtmLineStatusTable_Object = MibTable
mibds3AtmLineStatusTable = _Mibds3AtmLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1)
)
if mibBuilder.loadTexts:
    mibds3AtmLineStatusTable.setStatus("mandatory")
_Mibds3AtmLineStatusEntry_Object = MibTableRow
mibds3AtmLineStatusEntry = _Mibds3AtmLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1)
)
mibds3AtmLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "ds3AtmLineStatus-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "ds3AtmLineStatus-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "ds3AtmLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibds3AtmLineStatusEntry.setStatus("mandatory")
_Ds3AtmLineStatus_Shelf_o_Type = Integer32
_Ds3AtmLineStatus_Shelf_o_Object = MibScalar
ds3AtmLineStatus_Shelf_o = _Ds3AtmLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 1),
    _Ds3AtmLineStatus_Shelf_o_Type()
)
ds3AtmLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_Shelf_o.setStatus("mandatory")
_Ds3AtmLineStatus_Slot_o_Type = Integer32
_Ds3AtmLineStatus_Slot_o_Object = MibScalar
ds3AtmLineStatus_Slot_o = _Ds3AtmLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 2),
    _Ds3AtmLineStatus_Slot_o_Type()
)
ds3AtmLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_Slot_o.setStatus("mandatory")
_Ds3AtmLineStatus_Item_o_Type = Integer32
_Ds3AtmLineStatus_Item_o_Object = MibScalar
ds3AtmLineStatus_Item_o = _Ds3AtmLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 3),
    _Ds3AtmLineStatus_Item_o_Type()
)
ds3AtmLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_Item_o.setStatus("mandatory")


class _Ds3AtmLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ds3AtmLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_Ds3AtmLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_PhysicalAddress_Shelf_Object = MibScalar
ds3AtmLineStatus_PhysicalAddress_Shelf = _Ds3AtmLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 4),
    _Ds3AtmLineStatus_PhysicalAddress_Shelf_Type()
)
ds3AtmLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _Ds3AtmLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ds3AtmLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_Ds3AtmLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_PhysicalAddress_Slot_Object = MibScalar
ds3AtmLineStatus_PhysicalAddress_Slot = _Ds3AtmLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 5),
    _Ds3AtmLineStatus_PhysicalAddress_Slot_Type()
)
ds3AtmLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_Ds3AtmLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_Ds3AtmLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
ds3AtmLineStatus_PhysicalAddress_ItemNumber = _Ds3AtmLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 6),
    _Ds3AtmLineStatus_PhysicalAddress_ItemNumber_Type()
)
ds3AtmLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Ds3AtmLineStatus_LineState_Type(Integer32):
    """Custom type ds3AtmLineStatus_LineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 7),
          ("aisReceive", 6),
          ("disabled", 2),
          ("doesNotExist", 1),
          ("lossOfFrame", 4),
          ("lossOfSignal", 3),
          ("yellowReceive", 5))
    )


_Ds3AtmLineStatus_LineState_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_LineState_Object = MibScalar
ds3AtmLineStatus_LineState = _Ds3AtmLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 7),
    _Ds3AtmLineStatus_LineState_Type()
)
ds3AtmLineStatus_LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_LineState.setStatus("mandatory")


class _Ds3AtmLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type ds3AtmLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_Ds3AtmLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
ds3AtmLineStatus_SparePhysicalAddress_Shelf = _Ds3AtmLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 8),
    _Ds3AtmLineStatus_SparePhysicalAddress_Shelf_Type()
)
ds3AtmLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _Ds3AtmLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type ds3AtmLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_Ds3AtmLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
ds3AtmLineStatus_SparePhysicalAddress_Slot = _Ds3AtmLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 9),
    _Ds3AtmLineStatus_SparePhysicalAddress_Slot_Type()
)
ds3AtmLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_Ds3AtmLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_Ds3AtmLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
ds3AtmLineStatus_SparePhysicalAddress_ItemNumber = _Ds3AtmLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 10),
    _Ds3AtmLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
ds3AtmLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _Ds3AtmLineStatus_SparingState_Type(Integer32):
    """Custom type ds3AtmLineStatus_SparingState based on Integer32"""
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


_Ds3AtmLineStatus_SparingState_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_SparingState_Object = MibScalar
ds3AtmLineStatus_SparingState = _Ds3AtmLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 11),
    _Ds3AtmLineStatus_SparingState_Type()
)
ds3AtmLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_SparingState.setStatus("mandatory")


class _Ds3AtmLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type ds3AtmLineStatus_SparingChangeReason based on Integer32"""
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


_Ds3AtmLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_SparingChangeReason_Object = MibScalar
ds3AtmLineStatus_SparingChangeReason = _Ds3AtmLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 12),
    _Ds3AtmLineStatus_SparingChangeReason_Type()
)
ds3AtmLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_SparingChangeReason.setStatus("mandatory")
_Ds3AtmLineStatus_SparingChangeTime_Type = Integer32
_Ds3AtmLineStatus_SparingChangeTime_Object = MibScalar
ds3AtmLineStatus_SparingChangeTime = _Ds3AtmLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 13),
    _Ds3AtmLineStatus_SparingChangeTime_Type()
)
ds3AtmLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_SparingChangeTime.setStatus("mandatory")
_Ds3AtmLineStatus_SparingChangeCounter_Type = Integer32
_Ds3AtmLineStatus_SparingChangeCounter_Object = MibScalar
ds3AtmLineStatus_SparingChangeCounter = _Ds3AtmLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 14),
    _Ds3AtmLineStatus_SparingChangeCounter_Type()
)
ds3AtmLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_SparingChangeCounter.setStatus("mandatory")


class _Ds3AtmLineStatus_VpiVciRange_Type(Integer32):
    """Custom type ds3AtmLineStatus_VpiVciRange based on Integer32"""
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


_Ds3AtmLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_VpiVciRange_Object = MibScalar
ds3AtmLineStatus_VpiVciRange = _Ds3AtmLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 15),
    _Ds3AtmLineStatus_VpiVciRange_Type()
)
ds3AtmLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_VpiVciRange.setStatus("mandatory")
_Ds3AtmLineStatus_VcSwitchingVpi_Type = DisplayString
_Ds3AtmLineStatus_VcSwitchingVpi_Object = MibScalar
ds3AtmLineStatus_VcSwitchingVpi = _Ds3AtmLineStatus_VcSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 16),
    _Ds3AtmLineStatus_VcSwitchingVpi_Type()
)
ds3AtmLineStatus_VcSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_VcSwitchingVpi.setStatus("mandatory")
_Ds3AtmLineStatus_FBitErrorCount_Type = Integer32
_Ds3AtmLineStatus_FBitErrorCount_Object = MibScalar
ds3AtmLineStatus_FBitErrorCount = _Ds3AtmLineStatus_FBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 17),
    _Ds3AtmLineStatus_FBitErrorCount_Type()
)
ds3AtmLineStatus_FBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_FBitErrorCount.setStatus("mandatory")
_Ds3AtmLineStatus_PBitErrorCount_Type = Integer32
_Ds3AtmLineStatus_PBitErrorCount_Object = MibScalar
ds3AtmLineStatus_PBitErrorCount = _Ds3AtmLineStatus_PBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 18),
    _Ds3AtmLineStatus_PBitErrorCount_Type()
)
ds3AtmLineStatus_PBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_PBitErrorCount.setStatus("mandatory")
_Ds3AtmLineStatus_CpBitErrorCount_Type = Integer32
_Ds3AtmLineStatus_CpBitErrorCount_Object = MibScalar
ds3AtmLineStatus_CpBitErrorCount = _Ds3AtmLineStatus_CpBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 19),
    _Ds3AtmLineStatus_CpBitErrorCount_Type()
)
ds3AtmLineStatus_CpBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_CpBitErrorCount.setStatus("mandatory")
_Ds3AtmLineStatus_FebErrorCount_Type = Integer32
_Ds3AtmLineStatus_FebErrorCount_Object = MibScalar
ds3AtmLineStatus_FebErrorCount = _Ds3AtmLineStatus_FebErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 20),
    _Ds3AtmLineStatus_FebErrorCount_Type()
)
ds3AtmLineStatus_FebErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_FebErrorCount.setStatus("mandatory")
_Ds3AtmLineStatus_BpvErrorCount_Type = Integer32
_Ds3AtmLineStatus_BpvErrorCount_Object = MibScalar
ds3AtmLineStatus_BpvErrorCount = _Ds3AtmLineStatus_BpvErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 21),
    _Ds3AtmLineStatus_BpvErrorCount_Type()
)
ds3AtmLineStatus_BpvErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_BpvErrorCount.setStatus("mandatory")


class _Ds3AtmLineStatus_LossOfSignal_Type(Integer32):
    """Custom type ds3AtmLineStatus_LossOfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Ds3AtmLineStatus_LossOfSignal_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_LossOfSignal_Object = MibScalar
ds3AtmLineStatus_LossOfSignal = _Ds3AtmLineStatus_LossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 22),
    _Ds3AtmLineStatus_LossOfSignal_Type()
)
ds3AtmLineStatus_LossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_LossOfSignal.setStatus("mandatory")


class _Ds3AtmLineStatus_LossOfFrame_Type(Integer32):
    """Custom type ds3AtmLineStatus_LossOfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Ds3AtmLineStatus_LossOfFrame_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_LossOfFrame_Object = MibScalar
ds3AtmLineStatus_LossOfFrame = _Ds3AtmLineStatus_LossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 23),
    _Ds3AtmLineStatus_LossOfFrame_Type()
)
ds3AtmLineStatus_LossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_LossOfFrame.setStatus("mandatory")


class _Ds3AtmLineStatus_YellowReceive_Type(Integer32):
    """Custom type ds3AtmLineStatus_YellowReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Ds3AtmLineStatus_YellowReceive_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_YellowReceive_Object = MibScalar
ds3AtmLineStatus_YellowReceive = _Ds3AtmLineStatus_YellowReceive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 24),
    _Ds3AtmLineStatus_YellowReceive_Type()
)
ds3AtmLineStatus_YellowReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_YellowReceive.setStatus("mandatory")


class _Ds3AtmLineStatus_AisReceive_Type(Integer32):
    """Custom type ds3AtmLineStatus_AisReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Ds3AtmLineStatus_AisReceive_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_AisReceive_Object = MibScalar
ds3AtmLineStatus_AisReceive = _Ds3AtmLineStatus_AisReceive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 25),
    _Ds3AtmLineStatus_AisReceive_Type()
)
ds3AtmLineStatus_AisReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_AisReceive.setStatus("mandatory")


class _Ds3AtmLineStatus_Action_o_Type(Integer32):
    """Custom type ds3AtmLineStatus_Action_o based on Integer32"""
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


_Ds3AtmLineStatus_Action_o_Type.__name__ = "Integer32"
_Ds3AtmLineStatus_Action_o_Object = MibScalar
ds3AtmLineStatus_Action_o = _Ds3AtmLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 182, 1, 1, 26),
    _Ds3AtmLineStatus_Action_o_Type()
)
ds3AtmLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3AtmLineStatus_Action_o.setStatus("mandatory")
_Miboc3AtmLineStatus_ObjectIdentity = ObjectIdentity
miboc3AtmLineStatus = _Miboc3AtmLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 183)
)
_Miboc3AtmLineStatusTable_Object = MibTable
miboc3AtmLineStatusTable = _Miboc3AtmLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1)
)
if mibBuilder.loadTexts:
    miboc3AtmLineStatusTable.setStatus("mandatory")
_Miboc3AtmLineStatusEntry_Object = MibTableRow
miboc3AtmLineStatusEntry = _Miboc3AtmLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1)
)
miboc3AtmLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "oc3AtmLineStatus-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "oc3AtmLineStatus-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "oc3AtmLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    miboc3AtmLineStatusEntry.setStatus("mandatory")
_Oc3AtmLineStatus_Shelf_o_Type = Integer32
_Oc3AtmLineStatus_Shelf_o_Object = MibScalar
oc3AtmLineStatus_Shelf_o = _Oc3AtmLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 1),
    _Oc3AtmLineStatus_Shelf_o_Type()
)
oc3AtmLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_Shelf_o.setStatus("mandatory")
_Oc3AtmLineStatus_Slot_o_Type = Integer32
_Oc3AtmLineStatus_Slot_o_Object = MibScalar
oc3AtmLineStatus_Slot_o = _Oc3AtmLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 2),
    _Oc3AtmLineStatus_Slot_o_Type()
)
oc3AtmLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_Slot_o.setStatus("mandatory")
_Oc3AtmLineStatus_Item_o_Type = Integer32
_Oc3AtmLineStatus_Item_o_Object = MibScalar
oc3AtmLineStatus_Item_o = _Oc3AtmLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 3),
    _Oc3AtmLineStatus_Item_o_Type()
)
oc3AtmLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_Item_o.setStatus("mandatory")


class _Oc3AtmLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type oc3AtmLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_Oc3AtmLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_PhysicalAddress_Shelf_Object = MibScalar
oc3AtmLineStatus_PhysicalAddress_Shelf = _Oc3AtmLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 4),
    _Oc3AtmLineStatus_PhysicalAddress_Shelf_Type()
)
oc3AtmLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _Oc3AtmLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type oc3AtmLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_Oc3AtmLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_PhysicalAddress_Slot_Object = MibScalar
oc3AtmLineStatus_PhysicalAddress_Slot = _Oc3AtmLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 5),
    _Oc3AtmLineStatus_PhysicalAddress_Slot_Type()
)
oc3AtmLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_Oc3AtmLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_Oc3AtmLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
oc3AtmLineStatus_PhysicalAddress_ItemNumber = _Oc3AtmLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 6),
    _Oc3AtmLineStatus_PhysicalAddress_ItemNumber_Type()
)
oc3AtmLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Oc3AtmLineStatus_LineState_Type(Integer32):
    """Custom type oc3AtmLineStatus_LineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 7),
          ("aisReceive", 6),
          ("disabled", 2),
          ("doesNotExist", 1),
          ("lossOfFrame", 4),
          ("lossOfSignal", 3),
          ("yellowReceive", 5))
    )


_Oc3AtmLineStatus_LineState_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_LineState_Object = MibScalar
oc3AtmLineStatus_LineState = _Oc3AtmLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 7),
    _Oc3AtmLineStatus_LineState_Type()
)
oc3AtmLineStatus_LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_LineState.setStatus("mandatory")


class _Oc3AtmLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type oc3AtmLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_Oc3AtmLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
oc3AtmLineStatus_SparePhysicalAddress_Shelf = _Oc3AtmLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 8),
    _Oc3AtmLineStatus_SparePhysicalAddress_Shelf_Type()
)
oc3AtmLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _Oc3AtmLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type oc3AtmLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_Oc3AtmLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
oc3AtmLineStatus_SparePhysicalAddress_Slot = _Oc3AtmLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 9),
    _Oc3AtmLineStatus_SparePhysicalAddress_Slot_Type()
)
oc3AtmLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_Oc3AtmLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_Oc3AtmLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
oc3AtmLineStatus_SparePhysicalAddress_ItemNumber = _Oc3AtmLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 10),
    _Oc3AtmLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
oc3AtmLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _Oc3AtmLineStatus_SparingState_Type(Integer32):
    """Custom type oc3AtmLineStatus_SparingState based on Integer32"""
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


_Oc3AtmLineStatus_SparingState_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_SparingState_Object = MibScalar
oc3AtmLineStatus_SparingState = _Oc3AtmLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 11),
    _Oc3AtmLineStatus_SparingState_Type()
)
oc3AtmLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SparingState.setStatus("mandatory")


class _Oc3AtmLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type oc3AtmLineStatus_SparingChangeReason based on Integer32"""
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


_Oc3AtmLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_SparingChangeReason_Object = MibScalar
oc3AtmLineStatus_SparingChangeReason = _Oc3AtmLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 12),
    _Oc3AtmLineStatus_SparingChangeReason_Type()
)
oc3AtmLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SparingChangeReason.setStatus("mandatory")
_Oc3AtmLineStatus_SparingChangeTime_Type = Integer32
_Oc3AtmLineStatus_SparingChangeTime_Object = MibScalar
oc3AtmLineStatus_SparingChangeTime = _Oc3AtmLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 13),
    _Oc3AtmLineStatus_SparingChangeTime_Type()
)
oc3AtmLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SparingChangeTime.setStatus("mandatory")
_Oc3AtmLineStatus_SparingChangeCounter_Type = Integer32
_Oc3AtmLineStatus_SparingChangeCounter_Object = MibScalar
oc3AtmLineStatus_SparingChangeCounter = _Oc3AtmLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 14),
    _Oc3AtmLineStatus_SparingChangeCounter_Type()
)
oc3AtmLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SparingChangeCounter.setStatus("mandatory")


class _Oc3AtmLineStatus_VpiVciRange_Type(Integer32):
    """Custom type oc3AtmLineStatus_VpiVciRange based on Integer32"""
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


_Oc3AtmLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_VpiVciRange_Object = MibScalar
oc3AtmLineStatus_VpiVciRange = _Oc3AtmLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 15),
    _Oc3AtmLineStatus_VpiVciRange_Type()
)
oc3AtmLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_VpiVciRange.setStatus("mandatory")
_Oc3AtmLineStatus_VcSwitchingVpi_Type = DisplayString
_Oc3AtmLineStatus_VcSwitchingVpi_Object = MibScalar
oc3AtmLineStatus_VcSwitchingVpi = _Oc3AtmLineStatus_VcSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 16),
    _Oc3AtmLineStatus_VcSwitchingVpi_Type()
)
oc3AtmLineStatus_VcSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_VcSwitchingVpi.setStatus("mandatory")
_Oc3AtmLineStatus_ApsConfigName_Type = DisplayString
_Oc3AtmLineStatus_ApsConfigName_Object = MibScalar
oc3AtmLineStatus_ApsConfigName = _Oc3AtmLineStatus_ApsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 17),
    _Oc3AtmLineStatus_ApsConfigName_Type()
)
oc3AtmLineStatus_ApsConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsConfigName.setStatus("mandatory")


class _Oc3AtmLineStatus_ApsChannelStatus_Type(Integer32):
    """Custom type oc3AtmLineStatus_ApsChannelStatus based on Integer32"""
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
        *(("lockedOutWorking", 4),
          ("onProtection", 2),
          ("onWorking", 3),
          ("unknown", 1))
    )


_Oc3AtmLineStatus_ApsChannelStatus_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_ApsChannelStatus_Object = MibScalar
oc3AtmLineStatus_ApsChannelStatus = _Oc3AtmLineStatus_ApsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 18),
    _Oc3AtmLineStatus_ApsChannelStatus_Type()
)
oc3AtmLineStatus_ApsChannelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelStatus.setStatus("mandatory")


class _Oc3AtmLineStatus_ApsChannelSdCondition_Type(Integer32):
    """Custom type oc3AtmLineStatus_ApsChannelSdCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_ApsChannelSdCondition_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_ApsChannelSdCondition_Object = MibScalar
oc3AtmLineStatus_ApsChannelSdCondition = _Oc3AtmLineStatus_ApsChannelSdCondition_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 19),
    _Oc3AtmLineStatus_ApsChannelSdCondition_Type()
)
oc3AtmLineStatus_ApsChannelSdCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelSdCondition.setStatus("mandatory")


class _Oc3AtmLineStatus_ApsChannelSfCondition_Type(Integer32):
    """Custom type oc3AtmLineStatus_ApsChannelSfCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_ApsChannelSfCondition_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_ApsChannelSfCondition_Object = MibScalar
oc3AtmLineStatus_ApsChannelSfCondition = _Oc3AtmLineStatus_ApsChannelSfCondition_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 20),
    _Oc3AtmLineStatus_ApsChannelSfCondition_Type()
)
oc3AtmLineStatus_ApsChannelSfCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelSfCondition.setStatus("mandatory")


class _Oc3AtmLineStatus_ApsChannelLowDirection_Type(Integer32):
    """Custom type oc3AtmLineStatus_ApsChannelLowDirection based on Integer32"""
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
        *(("lowBoth", 4),
          ("lowNone", 1),
          ("lowRecv", 2),
          ("lowSend", 3))
    )


_Oc3AtmLineStatus_ApsChannelLowDirection_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_ApsChannelLowDirection_Object = MibScalar
oc3AtmLineStatus_ApsChannelLowDirection = _Oc3AtmLineStatus_ApsChannelLowDirection_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 21),
    _Oc3AtmLineStatus_ApsChannelLowDirection_Type()
)
oc3AtmLineStatus_ApsChannelLowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelLowDirection.setStatus("mandatory")
_Oc3AtmLineStatus_ApsChannelRecvSdCount_Type = Integer32
_Oc3AtmLineStatus_ApsChannelRecvSdCount_Object = MibScalar
oc3AtmLineStatus_ApsChannelRecvSdCount = _Oc3AtmLineStatus_ApsChannelRecvSdCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 22),
    _Oc3AtmLineStatus_ApsChannelRecvSdCount_Type()
)
oc3AtmLineStatus_ApsChannelRecvSdCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelRecvSdCount.setStatus("mandatory")
_Oc3AtmLineStatus_ApsChannelRecvSfCount_Type = Integer32
_Oc3AtmLineStatus_ApsChannelRecvSfCount_Object = MibScalar
oc3AtmLineStatus_ApsChannelRecvSfCount = _Oc3AtmLineStatus_ApsChannelRecvSfCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 23),
    _Oc3AtmLineStatus_ApsChannelRecvSfCount_Type()
)
oc3AtmLineStatus_ApsChannelRecvSfCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelRecvSfCount.setStatus("mandatory")
_Oc3AtmLineStatus_ApsChannelRecvAisCount_Type = Integer32
_Oc3AtmLineStatus_ApsChannelRecvAisCount_Object = MibScalar
oc3AtmLineStatus_ApsChannelRecvAisCount = _Oc3AtmLineStatus_ApsChannelRecvAisCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 24),
    _Oc3AtmLineStatus_ApsChannelRecvAisCount_Type()
)
oc3AtmLineStatus_ApsChannelRecvAisCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelRecvAisCount.setStatus("mandatory")
_Oc3AtmLineStatus_ApsChannelRecvRdiCount_Type = Integer32
_Oc3AtmLineStatus_ApsChannelRecvRdiCount_Object = MibScalar
oc3AtmLineStatus_ApsChannelRecvRdiCount = _Oc3AtmLineStatus_ApsChannelRecvRdiCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 25),
    _Oc3AtmLineStatus_ApsChannelRecvRdiCount_Type()
)
oc3AtmLineStatus_ApsChannelRecvRdiCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsChannelRecvRdiCount.setStatus("mandatory")


class _Oc3AtmLineStatus_LossOfSignal_Type(Integer32):
    """Custom type oc3AtmLineStatus_LossOfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_LossOfSignal_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_LossOfSignal_Object = MibScalar
oc3AtmLineStatus_LossOfSignal = _Oc3AtmLineStatus_LossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 26),
    _Oc3AtmLineStatus_LossOfSignal_Type()
)
oc3AtmLineStatus_LossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_LossOfSignal.setStatus("mandatory")


class _Oc3AtmLineStatus_LossOfFrame_Type(Integer32):
    """Custom type oc3AtmLineStatus_LossOfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_LossOfFrame_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_LossOfFrame_Object = MibScalar
oc3AtmLineStatus_LossOfFrame = _Oc3AtmLineStatus_LossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 27),
    _Oc3AtmLineStatus_LossOfFrame_Type()
)
oc3AtmLineStatus_LossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_LossOfFrame.setStatus("mandatory")


class _Oc3AtmLineStatus_OutOfFrame_Type(Integer32):
    """Custom type oc3AtmLineStatus_OutOfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_OutOfFrame_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_OutOfFrame_Object = MibScalar
oc3AtmLineStatus_OutOfFrame = _Oc3AtmLineStatus_OutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 28),
    _Oc3AtmLineStatus_OutOfFrame_Type()
)
oc3AtmLineStatus_OutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_OutOfFrame.setStatus("mandatory")


class _Oc3AtmLineStatus_SectionState_Type(Integer32):
    """Custom type oc3AtmLineStatus_SectionState based on Integer32"""
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
        *(("sonetDisabled", 1),
          ("sonetSectionActiveNoDefect", 2),
          ("sonetSectionLossOfFrame", 4),
          ("sonetSectionLossOfSignal", 3))
    )


_Oc3AtmLineStatus_SectionState_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_SectionState_Object = MibScalar
oc3AtmLineStatus_SectionState = _Oc3AtmLineStatus_SectionState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 29),
    _Oc3AtmLineStatus_SectionState_Type()
)
oc3AtmLineStatus_SectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_SectionState.setStatus("mandatory")


class _Oc3AtmLineStatus_PathState_Type(Integer32):
    """Custom type oc3AtmLineStatus_PathState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sonetDisabled", 1),
          ("sonetPathActiveNoDefect", 2),
          ("sonetPathAlarmIndicationSignal", 4),
          ("sonetPathLossOfPointer", 3),
          ("sonetPathRdi", 5),
          ("sonetPathSignalLabelMismatch", 7),
          ("sonetPathUnquipped", 6))
    )


_Oc3AtmLineStatus_PathState_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_PathState_Object = MibScalar
oc3AtmLineStatus_PathState = _Oc3AtmLineStatus_PathState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 30),
    _Oc3AtmLineStatus_PathState_Type()
)
oc3AtmLineStatus_PathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PathState.setStatus("mandatory")


class _Oc3AtmLineStatus_AisReceive_Type(Integer32):
    """Custom type oc3AtmLineStatus_AisReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_AisReceive_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_AisReceive_Object = MibScalar
oc3AtmLineStatus_AisReceive = _Oc3AtmLineStatus_AisReceive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 31),
    _Oc3AtmLineStatus_AisReceive_Type()
)
oc3AtmLineStatus_AisReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_AisReceive.setStatus("mandatory")


class _Oc3AtmLineStatus_YellowReceive_Type(Integer32):
    """Custom type oc3AtmLineStatus_YellowReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_YellowReceive_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_YellowReceive_Object = MibScalar
oc3AtmLineStatus_YellowReceive = _Oc3AtmLineStatus_YellowReceive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 32),
    _Oc3AtmLineStatus_YellowReceive_Type()
)
oc3AtmLineStatus_YellowReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_YellowReceive.setStatus("mandatory")


class _Oc3AtmLineStatus_OutOfCellDelineation_Type(Integer32):
    """Custom type oc3AtmLineStatus_OutOfCellDelineation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_OutOfCellDelineation_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_OutOfCellDelineation_Object = MibScalar
oc3AtmLineStatus_OutOfCellDelineation = _Oc3AtmLineStatus_OutOfCellDelineation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 33),
    _Oc3AtmLineStatus_OutOfCellDelineation_Type()
)
oc3AtmLineStatus_OutOfCellDelineation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_OutOfCellDelineation.setStatus("mandatory")


class _Oc3AtmLineStatus_LossOfCellDelineation_Type(Integer32):
    """Custom type oc3AtmLineStatus_LossOfCellDelineation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_LossOfCellDelineation_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_LossOfCellDelineation_Object = MibScalar
oc3AtmLineStatus_LossOfCellDelineation = _Oc3AtmLineStatus_LossOfCellDelineation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 34),
    _Oc3AtmLineStatus_LossOfCellDelineation_Type()
)
oc3AtmLineStatus_LossOfCellDelineation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_LossOfCellDelineation.setStatus("mandatory")


class _Oc3AtmLineStatus_ApsReceive_Type(Integer32):
    """Custom type oc3AtmLineStatus_ApsReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Oc3AtmLineStatus_ApsReceive_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_ApsReceive_Object = MibScalar
oc3AtmLineStatus_ApsReceive = _Oc3AtmLineStatus_ApsReceive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 35),
    _Oc3AtmLineStatus_ApsReceive_Type()
)
oc3AtmLineStatus_ApsReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ApsReceive.setStatus("mandatory")
_Oc3AtmLineStatus_RsopBipErrorCount_Type = Integer32
_Oc3AtmLineStatus_RsopBipErrorCount_Object = MibScalar
oc3AtmLineStatus_RsopBipErrorCount = _Oc3AtmLineStatus_RsopBipErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 36),
    _Oc3AtmLineStatus_RsopBipErrorCount_Type()
)
oc3AtmLineStatus_RsopBipErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RsopBipErrorCount.setStatus("mandatory")
_Oc3AtmLineStatus_RlopBipErrorCount_Type = Integer32
_Oc3AtmLineStatus_RlopBipErrorCount_Object = MibScalar
oc3AtmLineStatus_RlopBipErrorCount = _Oc3AtmLineStatus_RlopBipErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 37),
    _Oc3AtmLineStatus_RlopBipErrorCount_Type()
)
oc3AtmLineStatus_RlopBipErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RlopBipErrorCount.setStatus("mandatory")
_Oc3AtmLineStatus_RlopFebeErrorCount_Type = Integer32
_Oc3AtmLineStatus_RlopFebeErrorCount_Object = MibScalar
oc3AtmLineStatus_RlopFebeErrorCount = _Oc3AtmLineStatus_RlopFebeErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 38),
    _Oc3AtmLineStatus_RlopFebeErrorCount_Type()
)
oc3AtmLineStatus_RlopFebeErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RlopFebeErrorCount.setStatus("mandatory")
_Oc3AtmLineStatus_RpopBipErrorCount_Type = Integer32
_Oc3AtmLineStatus_RpopBipErrorCount_Object = MibScalar
oc3AtmLineStatus_RpopBipErrorCount = _Oc3AtmLineStatus_RpopBipErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 39),
    _Oc3AtmLineStatus_RpopBipErrorCount_Type()
)
oc3AtmLineStatus_RpopBipErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RpopBipErrorCount.setStatus("mandatory")
_Oc3AtmLineStatus_RpopFebeErrorCount_Type = Integer32
_Oc3AtmLineStatus_RpopFebeErrorCount_Object = MibScalar
oc3AtmLineStatus_RpopFebeErrorCount = _Oc3AtmLineStatus_RpopFebeErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 40),
    _Oc3AtmLineStatus_RpopFebeErrorCount_Type()
)
oc3AtmLineStatus_RpopFebeErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RpopFebeErrorCount.setStatus("mandatory")
_Oc3AtmLineStatus_RacpChcsErrorCount_Type = Integer32
_Oc3AtmLineStatus_RacpChcsErrorCount_Object = MibScalar
oc3AtmLineStatus_RacpChcsErrorCount = _Oc3AtmLineStatus_RacpChcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 41),
    _Oc3AtmLineStatus_RacpChcsErrorCount_Type()
)
oc3AtmLineStatus_RacpChcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RacpChcsErrorCount.setStatus("mandatory")
_Oc3AtmLineStatus_RacpUchcsErrorCount_Type = Integer32
_Oc3AtmLineStatus_RacpUchcsErrorCount_Object = MibScalar
oc3AtmLineStatus_RacpUchcsErrorCount = _Oc3AtmLineStatus_RacpUchcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 42),
    _Oc3AtmLineStatus_RacpUchcsErrorCount_Type()
)
oc3AtmLineStatus_RacpUchcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RacpUchcsErrorCount.setStatus("mandatory")
_Oc3AtmLineStatus_RacpRxCellCount_Type = Integer32
_Oc3AtmLineStatus_RacpRxCellCount_Object = MibScalar
oc3AtmLineStatus_RacpRxCellCount = _Oc3AtmLineStatus_RacpRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 43),
    _Oc3AtmLineStatus_RacpRxCellCount_Type()
)
oc3AtmLineStatus_RacpRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_RacpRxCellCount.setStatus("mandatory")
_Oc3AtmLineStatus_TacpTxCellCount_Type = Integer32
_Oc3AtmLineStatus_TacpTxCellCount_Object = MibScalar
oc3AtmLineStatus_TacpTxCellCount = _Oc3AtmLineStatus_TacpTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 44),
    _Oc3AtmLineStatus_TacpTxCellCount_Type()
)
oc3AtmLineStatus_TacpTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_TacpTxCellCount.setStatus("mandatory")
_Oc3AtmLineStatus_FrequencyJustificationCount_Type = Integer32
_Oc3AtmLineStatus_FrequencyJustificationCount_Object = MibScalar
oc3AtmLineStatus_FrequencyJustificationCount = _Oc3AtmLineStatus_FrequencyJustificationCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 45),
    _Oc3AtmLineStatus_FrequencyJustificationCount_Type()
)
oc3AtmLineStatus_FrequencyJustificationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_FrequencyJustificationCount.setStatus("mandatory")
_Oc3AtmLineStatus_oHECCellDropCounter_Type = Integer32
_Oc3AtmLineStatus_oHECCellDropCounter_Object = MibScalar
oc3AtmLineStatus_oHECCellDropCounter = _Oc3AtmLineStatus_oHECCellDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 46),
    _Oc3AtmLineStatus_oHECCellDropCounter_Type()
)
oc3AtmLineStatus_oHECCellDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_oHECCellDropCounter.setStatus("mandatory")
_Oc3AtmLineStatus_oFIFOOverflowCounter_Type = Integer32
_Oc3AtmLineStatus_oFIFOOverflowCounter_Object = MibScalar
oc3AtmLineStatus_oFIFOOverflowCounter = _Oc3AtmLineStatus_oFIFOOverflowCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 47),
    _Oc3AtmLineStatus_oFIFOOverflowCounter_Type()
)
oc3AtmLineStatus_oFIFOOverflowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_oFIFOOverflowCounter.setStatus("mandatory")
_Oc3AtmLineStatus_IdleCellCounter_Type = Integer32
_Oc3AtmLineStatus_IdleCellCounter_Object = MibScalar
oc3AtmLineStatus_IdleCellCounter = _Oc3AtmLineStatus_IdleCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 48),
    _Oc3AtmLineStatus_IdleCellCounter_Type()
)
oc3AtmLineStatus_IdleCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IdleCellCounter.setStatus("mandatory")
_Oc3AtmLineStatus_ValidCellCounter_Type = Integer32
_Oc3AtmLineStatus_ValidCellCounter_Object = MibScalar
oc3AtmLineStatus_ValidCellCounter = _Oc3AtmLineStatus_ValidCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 49),
    _Oc3AtmLineStatus_ValidCellCounter_Type()
)
oc3AtmLineStatus_ValidCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_ValidCellCounter.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 50),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 51),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 52),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations = _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 53),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 54),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 55),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations = _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 56),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 57),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 58),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 59),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 60),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 61),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 62),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 63),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations = _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 64),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 65),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 66),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 67),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 68),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds = _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 69),
    _Oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Type()
)
oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds.setStatus("mandatory")


class _Oc3AtmLineStatus_Action_o_Type(Integer32):
    """Custom type oc3AtmLineStatus_Action_o based on Integer32"""
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


_Oc3AtmLineStatus_Action_o_Type.__name__ = "Integer32"
_Oc3AtmLineStatus_Action_o_Object = MibScalar
oc3AtmLineStatus_Action_o = _Oc3AtmLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 1, 1, 70),
    _Oc3AtmLineStatus_Action_o_Type()
)
oc3AtmLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_Action_o.setStatus("mandatory")
_Miboc3AtmLineStatus_IntervalPerformanceMonitoringTable_Object = MibTable
miboc3AtmLineStatus_IntervalPerformanceMonitoringTable = _Miboc3AtmLineStatus_IntervalPerformanceMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2)
)
if mibBuilder.loadTexts:
    miboc3AtmLineStatus_IntervalPerformanceMonitoringTable.setStatus("mandatory")
_Miboc3AtmLineStatus_IntervalPerformanceMonitoringEntry_Object = MibTableRow
miboc3AtmLineStatus_IntervalPerformanceMonitoringEntry = _Miboc3AtmLineStatus_IntervalPerformanceMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1)
)
miboc3AtmLineStatus_IntervalPerformanceMonitoringEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "oc3AtmLineStatus-IntervalPerformanceMonitoring-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "oc3AtmLineStatus-IntervalPerformanceMonitoring-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "oc3AtmLineStatus-IntervalPerformanceMonitoring-Item-o"),
    (0, "ASCEND-MIBSTAT-MIB", "oc3AtmLineStatus-IntervalPerformanceMonitoring-Index-o"),
)
if mibBuilder.loadTexts:
    miboc3AtmLineStatus_IntervalPerformanceMonitoringEntry.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 1),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 2),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 3),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 4),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 5),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 6),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 7),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 8),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 9),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 10),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 11),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 12),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 13),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 14),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 15),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 16),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 17),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 18),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 19),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 20),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 21),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 22),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 23),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations.setStatus("mandatory")
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Type = Integer32
_Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Object = MibScalar
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds = _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 183, 2, 1, 24),
    _Oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds_Type()
)
oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds.setStatus("mandatory")
_Mibe3AtmLineStatus_ObjectIdentity = ObjectIdentity
mibe3AtmLineStatus = _Mibe3AtmLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 184)
)
_Mibe3AtmLineStatusTable_Object = MibTable
mibe3AtmLineStatusTable = _Mibe3AtmLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1)
)
if mibBuilder.loadTexts:
    mibe3AtmLineStatusTable.setStatus("mandatory")
_Mibe3AtmLineStatusEntry_Object = MibTableRow
mibe3AtmLineStatusEntry = _Mibe3AtmLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1)
)
mibe3AtmLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "e3AtmLineStatus-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "e3AtmLineStatus-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "e3AtmLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibe3AtmLineStatusEntry.setStatus("mandatory")
_E3AtmLineStatus_Shelf_o_Type = Integer32
_E3AtmLineStatus_Shelf_o_Object = MibScalar
e3AtmLineStatus_Shelf_o = _E3AtmLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 1),
    _E3AtmLineStatus_Shelf_o_Type()
)
e3AtmLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_Shelf_o.setStatus("mandatory")
_E3AtmLineStatus_Slot_o_Type = Integer32
_E3AtmLineStatus_Slot_o_Object = MibScalar
e3AtmLineStatus_Slot_o = _E3AtmLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 2),
    _E3AtmLineStatus_Slot_o_Type()
)
e3AtmLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_Slot_o.setStatus("mandatory")
_E3AtmLineStatus_Item_o_Type = Integer32
_E3AtmLineStatus_Item_o_Object = MibScalar
e3AtmLineStatus_Item_o = _E3AtmLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 3),
    _E3AtmLineStatus_Item_o_Type()
)
e3AtmLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_Item_o.setStatus("mandatory")


class _E3AtmLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type e3AtmLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_E3AtmLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_E3AtmLineStatus_PhysicalAddress_Shelf_Object = MibScalar
e3AtmLineStatus_PhysicalAddress_Shelf = _E3AtmLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 4),
    _E3AtmLineStatus_PhysicalAddress_Shelf_Type()
)
e3AtmLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _E3AtmLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type e3AtmLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_E3AtmLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_E3AtmLineStatus_PhysicalAddress_Slot_Object = MibScalar
e3AtmLineStatus_PhysicalAddress_Slot = _E3AtmLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 5),
    _E3AtmLineStatus_PhysicalAddress_Slot_Type()
)
e3AtmLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_E3AtmLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_E3AtmLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
e3AtmLineStatus_PhysicalAddress_ItemNumber = _E3AtmLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 6),
    _E3AtmLineStatus_PhysicalAddress_ItemNumber_Type()
)
e3AtmLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _E3AtmLineStatus_LineState_Type(Integer32):
    """Custom type e3AtmLineStatus_LineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 7),
          ("aisReceive", 6),
          ("disabled", 2),
          ("doesNotExist", 1),
          ("lossOfFrame", 4),
          ("lossOfSignal", 3),
          ("yellowReceive", 5))
    )


_E3AtmLineStatus_LineState_Type.__name__ = "Integer32"
_E3AtmLineStatus_LineState_Object = MibScalar
e3AtmLineStatus_LineState = _E3AtmLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 7),
    _E3AtmLineStatus_LineState_Type()
)
e3AtmLineStatus_LineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_LineState.setStatus("mandatory")


class _E3AtmLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type e3AtmLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_E3AtmLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_E3AtmLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
e3AtmLineStatus_SparePhysicalAddress_Shelf = _E3AtmLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 8),
    _E3AtmLineStatus_SparePhysicalAddress_Shelf_Type()
)
e3AtmLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _E3AtmLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type e3AtmLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_E3AtmLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_E3AtmLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
e3AtmLineStatus_SparePhysicalAddress_Slot = _E3AtmLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 9),
    _E3AtmLineStatus_SparePhysicalAddress_Slot_Type()
)
e3AtmLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_E3AtmLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_E3AtmLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
e3AtmLineStatus_SparePhysicalAddress_ItemNumber = _E3AtmLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 10),
    _E3AtmLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
e3AtmLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _E3AtmLineStatus_SparingState_Type(Integer32):
    """Custom type e3AtmLineStatus_SparingState based on Integer32"""
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


_E3AtmLineStatus_SparingState_Type.__name__ = "Integer32"
_E3AtmLineStatus_SparingState_Object = MibScalar
e3AtmLineStatus_SparingState = _E3AtmLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 11),
    _E3AtmLineStatus_SparingState_Type()
)
e3AtmLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_SparingState.setStatus("mandatory")


class _E3AtmLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type e3AtmLineStatus_SparingChangeReason based on Integer32"""
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


_E3AtmLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_E3AtmLineStatus_SparingChangeReason_Object = MibScalar
e3AtmLineStatus_SparingChangeReason = _E3AtmLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 12),
    _E3AtmLineStatus_SparingChangeReason_Type()
)
e3AtmLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_SparingChangeReason.setStatus("mandatory")
_E3AtmLineStatus_SparingChangeTime_Type = Integer32
_E3AtmLineStatus_SparingChangeTime_Object = MibScalar
e3AtmLineStatus_SparingChangeTime = _E3AtmLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 13),
    _E3AtmLineStatus_SparingChangeTime_Type()
)
e3AtmLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_SparingChangeTime.setStatus("mandatory")
_E3AtmLineStatus_SparingChangeCounter_Type = Integer32
_E3AtmLineStatus_SparingChangeCounter_Object = MibScalar
e3AtmLineStatus_SparingChangeCounter = _E3AtmLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 14),
    _E3AtmLineStatus_SparingChangeCounter_Type()
)
e3AtmLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_SparingChangeCounter.setStatus("mandatory")


class _E3AtmLineStatus_VpiVciRange_Type(Integer32):
    """Custom type e3AtmLineStatus_VpiVciRange based on Integer32"""
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


_E3AtmLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_E3AtmLineStatus_VpiVciRange_Object = MibScalar
e3AtmLineStatus_VpiVciRange = _E3AtmLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 15),
    _E3AtmLineStatus_VpiVciRange_Type()
)
e3AtmLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_VpiVciRange.setStatus("mandatory")
_E3AtmLineStatus_VcSwitchingVpi_Type = DisplayString
_E3AtmLineStatus_VcSwitchingVpi_Object = MibScalar
e3AtmLineStatus_VcSwitchingVpi = _E3AtmLineStatus_VcSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 16),
    _E3AtmLineStatus_VcSwitchingVpi_Type()
)
e3AtmLineStatus_VcSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmLineStatus_VcSwitchingVpi.setStatus("mandatory")
_E3AtmLineStatus_FBitErrorCount_Type = Integer32
_E3AtmLineStatus_FBitErrorCount_Object = MibScalar
e3AtmLineStatus_FBitErrorCount = _E3AtmLineStatus_FBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 17),
    _E3AtmLineStatus_FBitErrorCount_Type()
)
e3AtmLineStatus_FBitErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_FBitErrorCount.setStatus("mandatory")
_E3AtmLineStatus_PBitErrorCount_Type = Integer32
_E3AtmLineStatus_PBitErrorCount_Object = MibScalar
e3AtmLineStatus_PBitErrorCount = _E3AtmLineStatus_PBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 18),
    _E3AtmLineStatus_PBitErrorCount_Type()
)
e3AtmLineStatus_PBitErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_PBitErrorCount.setStatus("mandatory")
_E3AtmLineStatus_CpBitErrorCount_Type = Integer32
_E3AtmLineStatus_CpBitErrorCount_Object = MibScalar
e3AtmLineStatus_CpBitErrorCount = _E3AtmLineStatus_CpBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 19),
    _E3AtmLineStatus_CpBitErrorCount_Type()
)
e3AtmLineStatus_CpBitErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_CpBitErrorCount.setStatus("mandatory")
_E3AtmLineStatus_FebErrorCount_Type = Integer32
_E3AtmLineStatus_FebErrorCount_Object = MibScalar
e3AtmLineStatus_FebErrorCount = _E3AtmLineStatus_FebErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 20),
    _E3AtmLineStatus_FebErrorCount_Type()
)
e3AtmLineStatus_FebErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_FebErrorCount.setStatus("mandatory")
_E3AtmLineStatus_BpvErrorCount_Type = Integer32
_E3AtmLineStatus_BpvErrorCount_Object = MibScalar
e3AtmLineStatus_BpvErrorCount = _E3AtmLineStatus_BpvErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 21),
    _E3AtmLineStatus_BpvErrorCount_Type()
)
e3AtmLineStatus_BpvErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_BpvErrorCount.setStatus("mandatory")


class _E3AtmLineStatus_LossOfSignal_Type(Integer32):
    """Custom type e3AtmLineStatus_LossOfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_E3AtmLineStatus_LossOfSignal_Type.__name__ = "Integer32"
_E3AtmLineStatus_LossOfSignal_Object = MibScalar
e3AtmLineStatus_LossOfSignal = _E3AtmLineStatus_LossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 22),
    _E3AtmLineStatus_LossOfSignal_Type()
)
e3AtmLineStatus_LossOfSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_LossOfSignal.setStatus("mandatory")


class _E3AtmLineStatus_LossOfFrame_Type(Integer32):
    """Custom type e3AtmLineStatus_LossOfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_E3AtmLineStatus_LossOfFrame_Type.__name__ = "Integer32"
_E3AtmLineStatus_LossOfFrame_Object = MibScalar
e3AtmLineStatus_LossOfFrame = _E3AtmLineStatus_LossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 23),
    _E3AtmLineStatus_LossOfFrame_Type()
)
e3AtmLineStatus_LossOfFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_LossOfFrame.setStatus("mandatory")


class _E3AtmLineStatus_YellowReceive_Type(Integer32):
    """Custom type e3AtmLineStatus_YellowReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_E3AtmLineStatus_YellowReceive_Type.__name__ = "Integer32"
_E3AtmLineStatus_YellowReceive_Object = MibScalar
e3AtmLineStatus_YellowReceive = _E3AtmLineStatus_YellowReceive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 24),
    _E3AtmLineStatus_YellowReceive_Type()
)
e3AtmLineStatus_YellowReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_YellowReceive.setStatus("mandatory")


class _E3AtmLineStatus_AisReceive_Type(Integer32):
    """Custom type e3AtmLineStatus_AisReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_E3AtmLineStatus_AisReceive_Type.__name__ = "Integer32"
_E3AtmLineStatus_AisReceive_Object = MibScalar
e3AtmLineStatus_AisReceive = _E3AtmLineStatus_AisReceive_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 25),
    _E3AtmLineStatus_AisReceive_Type()
)
e3AtmLineStatus_AisReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_AisReceive.setStatus("mandatory")


class _E3AtmLineStatus_Action_o_Type(Integer32):
    """Custom type e3AtmLineStatus_Action_o based on Integer32"""
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


_E3AtmLineStatus_Action_o_Type.__name__ = "Integer32"
_E3AtmLineStatus_Action_o_Object = MibScalar
e3AtmLineStatus_Action_o = _E3AtmLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 184, 1, 1, 26),
    _E3AtmLineStatus_Action_o_Type()
)
e3AtmLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmLineStatus_Action_o.setStatus("mandatory")
_MibatmIfStatus_ObjectIdentity = ObjectIdentity
mibatmIfStatus = _MibatmIfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 185)
)
_MibatmIfStatusTable_Object = MibTable
mibatmIfStatusTable = _MibatmIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1)
)
if mibBuilder.loadTexts:
    mibatmIfStatusTable.setStatus("mandatory")
_MibatmIfStatusEntry_Object = MibTableRow
mibatmIfStatusEntry = _MibatmIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1)
)
mibatmIfStatusEntry.setIndexNames(
    (0, "ASCEND-MIBSTAT-MIB", "atmIfStatus-Shelf-o"),
    (0, "ASCEND-MIBSTAT-MIB", "atmIfStatus-Slot-o"),
    (0, "ASCEND-MIBSTAT-MIB", "atmIfStatus-Item-o"),
    (0, "ASCEND-MIBSTAT-MIB", "atmIfStatus-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibatmIfStatusEntry.setStatus("mandatory")
_AtmIfStatus_Shelf_o_Type = Integer32
_AtmIfStatus_Shelf_o_Object = MibScalar
atmIfStatus_Shelf_o = _AtmIfStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 1),
    _AtmIfStatus_Shelf_o_Type()
)
atmIfStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_Shelf_o.setStatus("mandatory")
_AtmIfStatus_Slot_o_Type = Integer32
_AtmIfStatus_Slot_o_Object = MibScalar
atmIfStatus_Slot_o = _AtmIfStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 2),
    _AtmIfStatus_Slot_o_Type()
)
atmIfStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_Slot_o.setStatus("mandatory")
_AtmIfStatus_Item_o_Type = Integer32
_AtmIfStatus_Item_o_Object = MibScalar
atmIfStatus_Item_o = _AtmIfStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 3),
    _AtmIfStatus_Item_o_Type()
)
atmIfStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_Item_o.setStatus("mandatory")
_AtmIfStatus_LogicalItem_o_Type = Integer32
_AtmIfStatus_LogicalItem_o_Object = MibScalar
atmIfStatus_LogicalItem_o = _AtmIfStatus_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 4),
    _AtmIfStatus_LogicalItem_o_Type()
)
atmIfStatus_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_LogicalItem_o.setStatus("mandatory")


class _AtmIfStatus_Address_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atmIfStatus_Address_PhysicalAddress_Shelf based on Integer32"""
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


_AtmIfStatus_Address_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtmIfStatus_Address_PhysicalAddress_Shelf_Object = MibScalar
atmIfStatus_Address_PhysicalAddress_Shelf = _AtmIfStatus_Address_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 5),
    _AtmIfStatus_Address_PhysicalAddress_Shelf_Type()
)
atmIfStatus_Address_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfStatus_Address_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtmIfStatus_Address_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atmIfStatus_Address_PhysicalAddress_Slot based on Integer32"""
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


_AtmIfStatus_Address_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtmIfStatus_Address_PhysicalAddress_Slot_Object = MibScalar
atmIfStatus_Address_PhysicalAddress_Slot = _AtmIfStatus_Address_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 6),
    _AtmIfStatus_Address_PhysicalAddress_Slot_Type()
)
atmIfStatus_Address_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfStatus_Address_PhysicalAddress_Slot.setStatus("mandatory")
_AtmIfStatus_Address_PhysicalAddress_ItemNumber_Type = Integer32
_AtmIfStatus_Address_PhysicalAddress_ItemNumber_Object = MibScalar
atmIfStatus_Address_PhysicalAddress_ItemNumber = _AtmIfStatus_Address_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 7),
    _AtmIfStatus_Address_PhysicalAddress_ItemNumber_Type()
)
atmIfStatus_Address_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfStatus_Address_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmIfStatus_Address_LogicalItem_Type = Integer32
_AtmIfStatus_Address_LogicalItem_Object = MibScalar
atmIfStatus_Address_LogicalItem = _AtmIfStatus_Address_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 8),
    _AtmIfStatus_Address_LogicalItem_Type()
)
atmIfStatus_Address_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfStatus_Address_LogicalItem.setStatus("mandatory")
_AtmIfStatus_IfNumber_Type = Integer32
_AtmIfStatus_IfNumber_Object = MibScalar
atmIfStatus_IfNumber = _AtmIfStatus_IfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 9),
    _AtmIfStatus_IfNumber_Type()
)
atmIfStatus_IfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_IfNumber.setStatus("mandatory")
_AtmIfStatus_NailedGroup_Type = Integer32
_AtmIfStatus_NailedGroup_Object = MibScalar
atmIfStatus_NailedGroup = _AtmIfStatus_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 10),
    _AtmIfStatus_NailedGroup_Type()
)
atmIfStatus_NailedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_NailedGroup.setStatus("mandatory")


class _AtmIfStatus_PortState_Type(Integer32):
    """Custom type atmIfStatus_PortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notConfigured", 1),
          ("up", 2))
    )


_AtmIfStatus_PortState_Type.__name__ = "Integer32"
_AtmIfStatus_PortState_Object = MibScalar
atmIfStatus_PortState = _AtmIfStatus_PortState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 11),
    _AtmIfStatus_PortState_Type()
)
atmIfStatus_PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_PortState.setStatus("mandatory")


class _AtmIfStatus_SignallingState_Type(Integer32):
    """Custom type atmIfStatus_SignallingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notConfigured", 1),
          ("up", 2))
    )


_AtmIfStatus_SignallingState_Type.__name__ = "Integer32"
_AtmIfStatus_SignallingState_Object = MibScalar
atmIfStatus_SignallingState = _AtmIfStatus_SignallingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 12),
    _AtmIfStatus_SignallingState_Type()
)
atmIfStatus_SignallingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_SignallingState.setStatus("mandatory")


class _AtmIfStatus_PnniLinkState_Type(Integer32):
    """Custom type atmIfStatus_PnniLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notConfigured", 1),
          ("up", 2))
    )


_AtmIfStatus_PnniLinkState_Type.__name__ = "Integer32"
_AtmIfStatus_PnniLinkState_Object = MibScalar
atmIfStatus_PnniLinkState = _AtmIfStatus_PnniLinkState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 13),
    _AtmIfStatus_PnniLinkState_Type()
)
atmIfStatus_PnniLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfStatus_PnniLinkState.setStatus("mandatory")


class _AtmIfStatus_Action_o_Type(Integer32):
    """Custom type atmIfStatus_Action_o based on Integer32"""
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


_AtmIfStatus_Action_o_Type.__name__ = "Integer32"
_AtmIfStatus_Action_o_Object = MibScalar
atmIfStatus_Action_o = _AtmIfStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 185, 1, 1, 14),
    _AtmIfStatus_Action_o_Type()
)
atmIfStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfStatus_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSTAT-MIB",
    **{"DisplayString": DisplayString,
       "mibbRINetworkInterfaceState": mibbRINetworkInterfaceState,
       "mibbRINetworkInterfaceStateTable": mibbRINetworkInterfaceStateTable,
       "mibbRINetworkInterfaceStateEntry": mibbRINetworkInterfaceStateEntry,
       "bRINetworkInterfaceState-Shelf-o": bRINetworkInterfaceState_Shelf_o,
       "bRINetworkInterfaceState-Slot-o": bRINetworkInterfaceState_Slot_o,
       "bRINetworkInterfaceState-Item-o": bRINetworkInterfaceState_Item_o,
       "bRINetworkInterfaceState-PhysicalAddress-Shelf": bRINetworkInterfaceState_PhysicalAddress_Shelf,
       "bRINetworkInterfaceState-PhysicalAddress-Slot": bRINetworkInterfaceState_PhysicalAddress_Slot,
       "bRINetworkInterfaceState-PhysicalAddress-ItemNumber": bRINetworkInterfaceState_PhysicalAddress_ItemNumber,
       "bRINetworkInterfaceState-LineState": bRINetworkInterfaceState_LineState,
       "bRINetworkInterfaceState-Action-o": bRINetworkInterfaceState_Action_o,
       "bRINetworkInterfaceState-SparePhysicalAddress-Shelf": bRINetworkInterfaceState_SparePhysicalAddress_Shelf,
       "bRINetworkInterfaceState-SparePhysicalAddress-Slot": bRINetworkInterfaceState_SparePhysicalAddress_Slot,
       "bRINetworkInterfaceState-SparePhysicalAddress-ItemNumber": bRINetworkInterfaceState_SparePhysicalAddress_ItemNumber,
       "bRINetworkInterfaceState-SparingState": bRINetworkInterfaceState_SparingState,
       "bRINetworkInterfaceState-SparingChangeReason": bRINetworkInterfaceState_SparingChangeReason,
       "bRINetworkInterfaceState-SparingChangeTime": bRINetworkInterfaceState_SparingChangeTime,
       "bRINetworkInterfaceState-SparingChangeCounter": bRINetworkInterfaceState_SparingChangeCounter,
       "bRINetworkInterfaceState-PhysicalStatus-IfGroupIndex": bRINetworkInterfaceState_PhysicalStatus_IfGroupIndex,
       "bRINetworkInterfaceState-PhysicalStatistic-LineUpTimer-Days": bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Days,
       "bRINetworkInterfaceState-PhysicalStatistic-LineUpTimer-Hours": bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Hours,
       "bRINetworkInterfaceState-PhysicalStatistic-LineUpTimer-Minutes": bRINetworkInterfaceState_PhysicalStatistic_LineUpTimer_Minutes,
       "bRINetworkInterfaceState-PhysicalStatistic-UpDwnCntr": bRINetworkInterfaceState_PhysicalStatistic_UpDwnCntr,
       "mibbRINetworkInterfaceState-ErrorCountTable": mibbRINetworkInterfaceState_ErrorCountTable,
       "mibbRINetworkInterfaceState-ErrorCountEntry": mibbRINetworkInterfaceState_ErrorCountEntry,
       "bRINetworkInterfaceState-ErrorCount-Shelf-o": bRINetworkInterfaceState_ErrorCount_Shelf_o,
       "bRINetworkInterfaceState-ErrorCount-Slot-o": bRINetworkInterfaceState_ErrorCount_Slot_o,
       "bRINetworkInterfaceState-ErrorCount-Item-o": bRINetworkInterfaceState_ErrorCount_Item_o,
       "bRINetworkInterfaceState-ErrorCount-Index-o": bRINetworkInterfaceState_ErrorCount_Index_o,
       "bRINetworkInterfaceState-ErrorCount": bRINetworkInterfaceState_ErrorCount,
       "mibbRINetworkInterfaceState-ChannelStateTable": mibbRINetworkInterfaceState_ChannelStateTable,
       "mibbRINetworkInterfaceState-ChannelStateEntry": mibbRINetworkInterfaceState_ChannelStateEntry,
       "bRINetworkInterfaceState-ChannelState-Shelf-o": bRINetworkInterfaceState_ChannelState_Shelf_o,
       "bRINetworkInterfaceState-ChannelState-Slot-o": bRINetworkInterfaceState_ChannelState_Slot_o,
       "bRINetworkInterfaceState-ChannelState-Item-o": bRINetworkInterfaceState_ChannelState_Item_o,
       "bRINetworkInterfaceState-ChannelState-Index-o": bRINetworkInterfaceState_ChannelState_Index_o,
       "bRINetworkInterfaceState-ChannelState": bRINetworkInterfaceState_ChannelState,
       "mibbRINetworkInterfaceState-PhysicalStatistic-ErrorCountTable": mibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountTable,
       "mibbRINetworkInterfaceState-PhysicalStatistic-ErrorCountEntry": mibbRINetworkInterfaceState_PhysicalStatistic_ErrorCountEntry,
       "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Shelf-o": bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Shelf_o,
       "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Slot-o": bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Slot_o,
       "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Item-o": bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Item_o,
       "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount-Index-o": bRINetworkInterfaceState_PhysicalStatistic_ErrorCount_Index_o,
       "bRINetworkInterfaceState-PhysicalStatistic-ErrorCount": bRINetworkInterfaceState_PhysicalStatistic_ErrorCount,
       "mibsdslLineStatus": mibsdslLineStatus,
       "mibsdslLineStatusTable": mibsdslLineStatusTable,
       "mibsdslLineStatusEntry": mibsdslLineStatusEntry,
       "sdslLineStatus-Shelf-o": sdslLineStatus_Shelf_o,
       "sdslLineStatus-Slot-o": sdslLineStatus_Slot_o,
       "sdslLineStatus-Item-o": sdslLineStatus_Item_o,
       "sdslLineStatus-PhysicalAddress-Shelf": sdslLineStatus_PhysicalAddress_Shelf,
       "sdslLineStatus-PhysicalAddress-Slot": sdslLineStatus_PhysicalAddress_Slot,
       "sdslLineStatus-PhysicalAddress-ItemNumber": sdslLineStatus_PhysicalAddress_ItemNumber,
       "sdslLineStatus-LineState": sdslLineStatus_LineState,
       "sdslLineStatus-SparePhysicalAddress-Shelf": sdslLineStatus_SparePhysicalAddress_Shelf,
       "sdslLineStatus-SparePhysicalAddress-Slot": sdslLineStatus_SparePhysicalAddress_Slot,
       "sdslLineStatus-SparePhysicalAddress-ItemNumber": sdslLineStatus_SparePhysicalAddress_ItemNumber,
       "sdslLineStatus-SparingState": sdslLineStatus_SparingState,
       "sdslLineStatus-SparingChangeReason": sdslLineStatus_SparingChangeReason,
       "sdslLineStatus-SparingChangeTime": sdslLineStatus_SparingChangeTime,
       "sdslLineStatus-SparingChangeCounter": sdslLineStatus_SparingChangeCounter,
       "sdslLineStatus-VpiVciRange": sdslLineStatus_VpiVciRange,
       "sdslLineStatus-VpSwitchingVpi": sdslLineStatus_VpSwitchingVpi,
       "sdslLineStatus-ErrorCount": sdslLineStatus_ErrorCount,
       "sdslLineStatus-PhysicalStatus-IfGroupIndex": sdslLineStatus_PhysicalStatus_IfGroupIndex,
       "sdslLineStatus-PhysicalStatus-UnitType": sdslLineStatus_PhysicalStatus_UnitType,
       "sdslLineStatus-PhysicalStatus-DevLineState": sdslLineStatus_PhysicalStatus_DevLineState,
       "sdslLineStatus-PhysicalStatus-UpStreamRate": sdslLineStatus_PhysicalStatus_UpStreamRate,
       "sdslLineStatus-PhysicalStatus-DownStreamRate": sdslLineStatus_PhysicalStatus_DownStreamRate,
       "sdslLineStatus-PhysicalStatus-MajorFirmwareVer": sdslLineStatus_PhysicalStatus_MajorFirmwareVer,
       "sdslLineStatus-PhysicalStatus-MinorFirmwareVer": sdslLineStatus_PhysicalStatus_MinorFirmwareVer,
       "sdslLineStatus-PhysicalStatus-HardwareVer": sdslLineStatus_PhysicalStatus_HardwareVer,
       "sdslLineStatus-PhysicalStatistic-LineUpTimer-Days": sdslLineStatus_PhysicalStatistic_LineUpTimer_Days,
       "sdslLineStatus-PhysicalStatistic-LineUpTimer-Hours": sdslLineStatus_PhysicalStatistic_LineUpTimer_Hours,
       "sdslLineStatus-PhysicalStatistic-LineUpTimer-Minutes": sdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes,
       "sdslLineStatus-PhysicalStatistic-RxSignalPresent": sdslLineStatus_PhysicalStatistic_RxSignalPresent,
       "sdslLineStatus-PhysicalStatistic-LineQuality": sdslLineStatus_PhysicalStatistic_LineQuality,
       "sdslLineStatus-PhysicalStatistic-UpDwnCntr": sdslLineStatus_PhysicalStatistic_UpDwnCntr,
       "sdslLineStatus-PhysicalStatistic-SelfTest": sdslLineStatus_PhysicalStatistic_SelfTest,
       "sdslLineStatus-PhysicalStatistic-FarEndDbAttenuation": sdslLineStatus_PhysicalStatistic_FarEndDbAttenuation,
       "sdslLineStatus-PhysicalStatistic-FirmwareStartupStage": sdslLineStatus_PhysicalStatistic_FirmwareStartupStage,
       "sdslLineStatus-PhysicalStatistic-HdlcRxCrcErrorCnt": sdslLineStatus_PhysicalStatistic_HdlcRxCrcErrorCnt,
       "sdslLineStatus-Action-o": sdslLineStatus_Action_o,
       "mibdmtAlDslLineStatus": mibdmtAlDslLineStatus,
       "mibdmtAlDslLineStatusTable": mibdmtAlDslLineStatusTable,
       "mibdmtAlDslLineStatusEntry": mibdmtAlDslLineStatusEntry,
       "dmtAlDslLineStatus-Shelf-o": dmtAlDslLineStatus_Shelf_o,
       "dmtAlDslLineStatus-Slot-o": dmtAlDslLineStatus_Slot_o,
       "dmtAlDslLineStatus-Item-o": dmtAlDslLineStatus_Item_o,
       "dmtAlDslLineStatus-PhysicalAddress-Shelf": dmtAlDslLineStatus_PhysicalAddress_Shelf,
       "dmtAlDslLineStatus-PhysicalAddress-Slot": dmtAlDslLineStatus_PhysicalAddress_Slot,
       "dmtAlDslLineStatus-PhysicalAddress-ItemNumber": dmtAlDslLineStatus_PhysicalAddress_ItemNumber,
       "dmtAlDslLineStatus-LineState": dmtAlDslLineStatus_LineState,
       "dmtAlDslLineStatus-SparePhysicalAddress-Shelf": dmtAlDslLineStatus_SparePhysicalAddress_Shelf,
       "dmtAlDslLineStatus-SparePhysicalAddress-Slot": dmtAlDslLineStatus_SparePhysicalAddress_Slot,
       "dmtAlDslLineStatus-SparePhysicalAddress-ItemNumber": dmtAlDslLineStatus_SparePhysicalAddress_ItemNumber,
       "dmtAlDslLineStatus-SparingState": dmtAlDslLineStatus_SparingState,
       "dmtAlDslLineStatus-SparingChangeReason": dmtAlDslLineStatus_SparingChangeReason,
       "dmtAlDslLineStatus-SparingChangeTime": dmtAlDslLineStatus_SparingChangeTime,
       "dmtAlDslLineStatus-SparingChangeCounter": dmtAlDslLineStatus_SparingChangeCounter,
       "dmtAlDslLineStatus-VpiVciRange": dmtAlDslLineStatus_VpiVciRange,
       "dmtAlDslLineStatus-VpSwitchingVpi": dmtAlDslLineStatus_VpSwitchingVpi,
       "dmtAlDslLineStatus-PhysicalStatus-IfGroupIndex": dmtAlDslLineStatus_PhysicalStatus_IfGroupIndex,
       "dmtAlDslLineStatus-PhysicalStatus-UnitType": dmtAlDslLineStatus_PhysicalStatus_UnitType,
       "dmtAlDslLineStatus-PhysicalStatus-DevLineState": dmtAlDslLineStatus_PhysicalStatus_DevLineState,
       "dmtAlDslLineStatus-PhysicalStatus-UpStreamRateFast": dmtAlDslLineStatus_PhysicalStatus_UpStreamRateFast,
       "dmtAlDslLineStatus-PhysicalStatus-DownStreamRateFast": dmtAlDslLineStatus_PhysicalStatus_DownStreamRateFast,
       "dmtAlDslLineStatus-PhysicalStatus-UpStreamRateInterleaved": dmtAlDslLineStatus_PhysicalStatus_UpStreamRateInterleaved,
       "dmtAlDslLineStatus-PhysicalStatus-DownStreamRateInterleaved": dmtAlDslLineStatus_PhysicalStatus_DownStreamRateInterleaved,
       "dmtAlDslLineStatus-PhysicalStatus-UpStreamLatency": dmtAlDslLineStatus_PhysicalStatus_UpStreamLatency,
       "dmtAlDslLineStatus-PhysicalStatus-DownStreamLatency": dmtAlDslLineStatus_PhysicalStatus_DownStreamLatency,
       "dmtAlDslLineStatus-PhysicalStatus-FirmwareVer": dmtAlDslLineStatus_PhysicalStatus_FirmwareVer,
       "dmtAlDslLineStatus-PhysicalStatus-AnsiAdslVer": dmtAlDslLineStatus_PhysicalStatus_AnsiAdslVer,
       "dmtAlDslLineStatus-PhysicalStatus-InitialAdslVer": dmtAlDslLineStatus_PhysicalStatus_InitialAdslVer,
       "dmtAlDslLineStatus-PhysicalStatus-HardwareVer": dmtAlDslLineStatus_PhysicalStatus_HardwareVer,
       "dmtAlDslLineStatus-PhysicalStatus-ModemHwState": dmtAlDslLineStatus_PhysicalStatus_ModemHwState,
       "dmtAlDslLineStatus-PhysicalStatus-AccumBitErr": dmtAlDslLineStatus_PhysicalStatus_AccumBitErr,
       "dmtAlDslLineStatus-PhysicalStatus-NumSecValid": dmtAlDslLineStatus_PhysicalStatus_NumSecValid,
       "dmtAlDslLineStatus-PhysicalStatus-NumSecInvalid": dmtAlDslLineStatus_PhysicalStatus_NumSecInvalid,
       "dmtAlDslLineStatus-PhysicalStatus-OperationalMode": dmtAlDslLineStatus_PhysicalStatus_OperationalMode,
       "dmtAlDslLineStatus-PhysicalStatistic-LineUpTimer-Days": dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Days,
       "dmtAlDslLineStatus-PhysicalStatistic-LineUpTimer-Hours": dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Hours,
       "dmtAlDslLineStatus-PhysicalStatistic-LineUpTimer-Minutes": dmtAlDslLineStatus_PhysicalStatistic_LineUpTimer_Minutes,
       "dmtAlDslLineStatus-PhysicalStatistic-RxSignalPresent": dmtAlDslLineStatus_PhysicalStatistic_RxSignalPresent,
       "dmtAlDslLineStatus-PhysicalStatistic-UpDwnCntr": dmtAlDslLineStatus_PhysicalStatistic_UpDwnCntr,
       "dmtAlDslLineStatus-PhysicalStatistic-SelfTest": dmtAlDslLineStatus_PhysicalStatistic_SelfTest,
       "dmtAlDslLineStatus-PhysicalStatistic-NoiseMarginDown": dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginDown,
       "dmtAlDslLineStatus-PhysicalStatistic-AttenuationDown": dmtAlDslLineStatus_PhysicalStatistic_AttenuationDown,
       "dmtAlDslLineStatus-PhysicalStatistic-OutputPowerDown": dmtAlDslLineStatus_PhysicalStatistic_OutputPowerDown,
       "dmtAlDslLineStatus-PhysicalStatistic-NoiseMarginUp": dmtAlDslLineStatus_PhysicalStatistic_NoiseMarginUp,
       "dmtAlDslLineStatus-PhysicalStatistic-AttenuationUp": dmtAlDslLineStatus_PhysicalStatistic_AttenuationUp,
       "dmtAlDslLineStatus-PhysicalStatistic-OutputPowerUp": dmtAlDslLineStatus_PhysicalStatistic_OutputPowerUp,
       "dmtAlDslLineStatus-PhysicalStatistic-NearEndFec": dmtAlDslLineStatus_PhysicalStatistic_NearEndFec,
       "dmtAlDslLineStatus-PhysicalStatistic-NearEndCrc": dmtAlDslLineStatus_PhysicalStatistic_NearEndCrc,
       "dmtAlDslLineStatus-PhysicalStatistic-NearEndHec": dmtAlDslLineStatus_PhysicalStatistic_NearEndHec,
       "dmtAlDslLineStatus-PhysicalStatistic-FarEndFec": dmtAlDslLineStatus_PhysicalStatistic_FarEndFec,
       "dmtAlDslLineStatus-PhysicalStatistic-FarEndCrc": dmtAlDslLineStatus_PhysicalStatistic_FarEndCrc,
       "dmtAlDslLineStatus-PhysicalStatistic-FarEndHec": dmtAlDslLineStatus_PhysicalStatistic_FarEndHec,
       "dmtAlDslLineStatus-PhysicalStatistic-ReceivedRsBlocks": dmtAlDslLineStatus_PhysicalStatistic_ReceivedRsBlocks,
       "dmtAlDslLineStatus-PhysicalStatistic-TransmittedRsBlocks": dmtAlDslLineStatus_PhysicalStatistic_TransmittedRsBlocks,
       "dmtAlDslLineStatus-PhysicalStatistic-IncomingCells": dmtAlDslLineStatus_PhysicalStatistic_IncomingCells,
       "dmtAlDslLineStatus-PhysicalStatistic-OutgoingCells": dmtAlDslLineStatus_PhysicalStatistic_OutgoingCells,
       "dmtAlDslLineStatus-Action-o": dmtAlDslLineStatus_Action_o,
       "mibds3AtmLineStatus": mibds3AtmLineStatus,
       "mibds3AtmLineStatusTable": mibds3AtmLineStatusTable,
       "mibds3AtmLineStatusEntry": mibds3AtmLineStatusEntry,
       "ds3AtmLineStatus-Shelf-o": ds3AtmLineStatus_Shelf_o,
       "ds3AtmLineStatus-Slot-o": ds3AtmLineStatus_Slot_o,
       "ds3AtmLineStatus-Item-o": ds3AtmLineStatus_Item_o,
       "ds3AtmLineStatus-PhysicalAddress-Shelf": ds3AtmLineStatus_PhysicalAddress_Shelf,
       "ds3AtmLineStatus-PhysicalAddress-Slot": ds3AtmLineStatus_PhysicalAddress_Slot,
       "ds3AtmLineStatus-PhysicalAddress-ItemNumber": ds3AtmLineStatus_PhysicalAddress_ItemNumber,
       "ds3AtmLineStatus-LineState": ds3AtmLineStatus_LineState,
       "ds3AtmLineStatus-SparePhysicalAddress-Shelf": ds3AtmLineStatus_SparePhysicalAddress_Shelf,
       "ds3AtmLineStatus-SparePhysicalAddress-Slot": ds3AtmLineStatus_SparePhysicalAddress_Slot,
       "ds3AtmLineStatus-SparePhysicalAddress-ItemNumber": ds3AtmLineStatus_SparePhysicalAddress_ItemNumber,
       "ds3AtmLineStatus-SparingState": ds3AtmLineStatus_SparingState,
       "ds3AtmLineStatus-SparingChangeReason": ds3AtmLineStatus_SparingChangeReason,
       "ds3AtmLineStatus-SparingChangeTime": ds3AtmLineStatus_SparingChangeTime,
       "ds3AtmLineStatus-SparingChangeCounter": ds3AtmLineStatus_SparingChangeCounter,
       "ds3AtmLineStatus-VpiVciRange": ds3AtmLineStatus_VpiVciRange,
       "ds3AtmLineStatus-VcSwitchingVpi": ds3AtmLineStatus_VcSwitchingVpi,
       "ds3AtmLineStatus-FBitErrorCount": ds3AtmLineStatus_FBitErrorCount,
       "ds3AtmLineStatus-PBitErrorCount": ds3AtmLineStatus_PBitErrorCount,
       "ds3AtmLineStatus-CpBitErrorCount": ds3AtmLineStatus_CpBitErrorCount,
       "ds3AtmLineStatus-FebErrorCount": ds3AtmLineStatus_FebErrorCount,
       "ds3AtmLineStatus-BpvErrorCount": ds3AtmLineStatus_BpvErrorCount,
       "ds3AtmLineStatus-LossOfSignal": ds3AtmLineStatus_LossOfSignal,
       "ds3AtmLineStatus-LossOfFrame": ds3AtmLineStatus_LossOfFrame,
       "ds3AtmLineStatus-YellowReceive": ds3AtmLineStatus_YellowReceive,
       "ds3AtmLineStatus-AisReceive": ds3AtmLineStatus_AisReceive,
       "ds3AtmLineStatus-Action-o": ds3AtmLineStatus_Action_o,
       "miboc3AtmLineStatus": miboc3AtmLineStatus,
       "miboc3AtmLineStatusTable": miboc3AtmLineStatusTable,
       "miboc3AtmLineStatusEntry": miboc3AtmLineStatusEntry,
       "oc3AtmLineStatus-Shelf-o": oc3AtmLineStatus_Shelf_o,
       "oc3AtmLineStatus-Slot-o": oc3AtmLineStatus_Slot_o,
       "oc3AtmLineStatus-Item-o": oc3AtmLineStatus_Item_o,
       "oc3AtmLineStatus-PhysicalAddress-Shelf": oc3AtmLineStatus_PhysicalAddress_Shelf,
       "oc3AtmLineStatus-PhysicalAddress-Slot": oc3AtmLineStatus_PhysicalAddress_Slot,
       "oc3AtmLineStatus-PhysicalAddress-ItemNumber": oc3AtmLineStatus_PhysicalAddress_ItemNumber,
       "oc3AtmLineStatus-LineState": oc3AtmLineStatus_LineState,
       "oc3AtmLineStatus-SparePhysicalAddress-Shelf": oc3AtmLineStatus_SparePhysicalAddress_Shelf,
       "oc3AtmLineStatus-SparePhysicalAddress-Slot": oc3AtmLineStatus_SparePhysicalAddress_Slot,
       "oc3AtmLineStatus-SparePhysicalAddress-ItemNumber": oc3AtmLineStatus_SparePhysicalAddress_ItemNumber,
       "oc3AtmLineStatus-SparingState": oc3AtmLineStatus_SparingState,
       "oc3AtmLineStatus-SparingChangeReason": oc3AtmLineStatus_SparingChangeReason,
       "oc3AtmLineStatus-SparingChangeTime": oc3AtmLineStatus_SparingChangeTime,
       "oc3AtmLineStatus-SparingChangeCounter": oc3AtmLineStatus_SparingChangeCounter,
       "oc3AtmLineStatus-VpiVciRange": oc3AtmLineStatus_VpiVciRange,
       "oc3AtmLineStatus-VcSwitchingVpi": oc3AtmLineStatus_VcSwitchingVpi,
       "oc3AtmLineStatus-ApsConfigName": oc3AtmLineStatus_ApsConfigName,
       "oc3AtmLineStatus-ApsChannelStatus": oc3AtmLineStatus_ApsChannelStatus,
       "oc3AtmLineStatus-ApsChannelSdCondition": oc3AtmLineStatus_ApsChannelSdCondition,
       "oc3AtmLineStatus-ApsChannelSfCondition": oc3AtmLineStatus_ApsChannelSfCondition,
       "oc3AtmLineStatus-ApsChannelLowDirection": oc3AtmLineStatus_ApsChannelLowDirection,
       "oc3AtmLineStatus-ApsChannelRecvSdCount": oc3AtmLineStatus_ApsChannelRecvSdCount,
       "oc3AtmLineStatus-ApsChannelRecvSfCount": oc3AtmLineStatus_ApsChannelRecvSfCount,
       "oc3AtmLineStatus-ApsChannelRecvAisCount": oc3AtmLineStatus_ApsChannelRecvAisCount,
       "oc3AtmLineStatus-ApsChannelRecvRdiCount": oc3AtmLineStatus_ApsChannelRecvRdiCount,
       "oc3AtmLineStatus-LossOfSignal": oc3AtmLineStatus_LossOfSignal,
       "oc3AtmLineStatus-LossOfFrame": oc3AtmLineStatus_LossOfFrame,
       "oc3AtmLineStatus-OutOfFrame": oc3AtmLineStatus_OutOfFrame,
       "oc3AtmLineStatus-SectionState": oc3AtmLineStatus_SectionState,
       "oc3AtmLineStatus-PathState": oc3AtmLineStatus_PathState,
       "oc3AtmLineStatus-AisReceive": oc3AtmLineStatus_AisReceive,
       "oc3AtmLineStatus-YellowReceive": oc3AtmLineStatus_YellowReceive,
       "oc3AtmLineStatus-OutOfCellDelineation": oc3AtmLineStatus_OutOfCellDelineation,
       "oc3AtmLineStatus-LossOfCellDelineation": oc3AtmLineStatus_LossOfCellDelineation,
       "oc3AtmLineStatus-ApsReceive": oc3AtmLineStatus_ApsReceive,
       "oc3AtmLineStatus-RsopBipErrorCount": oc3AtmLineStatus_RsopBipErrorCount,
       "oc3AtmLineStatus-RlopBipErrorCount": oc3AtmLineStatus_RlopBipErrorCount,
       "oc3AtmLineStatus-RlopFebeErrorCount": oc3AtmLineStatus_RlopFebeErrorCount,
       "oc3AtmLineStatus-RpopBipErrorCount": oc3AtmLineStatus_RpopBipErrorCount,
       "oc3AtmLineStatus-RpopFebeErrorCount": oc3AtmLineStatus_RpopFebeErrorCount,
       "oc3AtmLineStatus-RacpChcsErrorCount": oc3AtmLineStatus_RacpChcsErrorCount,
       "oc3AtmLineStatus-RacpUchcsErrorCount": oc3AtmLineStatus_RacpUchcsErrorCount,
       "oc3AtmLineStatus-RacpRxCellCount": oc3AtmLineStatus_RacpRxCellCount,
       "oc3AtmLineStatus-TacpTxCellCount": oc3AtmLineStatus_TacpTxCellCount,
       "oc3AtmLineStatus-FrequencyJustificationCount": oc3AtmLineStatus_FrequencyJustificationCount,
       "oc3AtmLineStatus-oHECCellDropCounter": oc3AtmLineStatus_oHECCellDropCounter,
       "oc3AtmLineStatus-oFIFOOverflowCounter": oc3AtmLineStatus_oFIFOOverflowCounter,
       "oc3AtmLineStatus-IdleCellCounter": oc3AtmLineStatus_IdleCellCounter,
       "oc3AtmLineStatus-ValidCellCounter": oc3AtmLineStatus_ValidCellCounter,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetSectionErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetSectionErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetSectionSeverelyErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetSectionSeverelyErroredFramingSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetSectionCodingViolations": oc3AtmLineStatus_PerformanceMonitoring_SonetSectionCodingViolations,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetLineErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetLineErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetLineSeverelyErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetLineSeverelyErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetLineCodingViolations": oc3AtmLineStatus_PerformanceMonitoring_SonetLineCodingViolations,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetLineUnavailableSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetLineUnavailableSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndLineErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndLineSeverelyErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndLineCodingViolations": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineCodingViolations,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndLineUnavailableSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndLineUnavailableSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetPathErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetPathErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetPathSeverelyErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetPathSeverelyErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetPathCodingViolations": oc3AtmLineStatus_PerformanceMonitoring_SonetPathCodingViolations,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetPathUnavailableSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetPathUnavailableSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndPathErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndPathSeverelyErroredSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndPathCodingViolations": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathCodingViolations,
       "oc3AtmLineStatus-PerformanceMonitoring-SonetFarEndPathUnavailableSeconds": oc3AtmLineStatus_PerformanceMonitoring_SonetFarEndPathUnavailableSeconds,
       "oc3AtmLineStatus-Action-o": oc3AtmLineStatus_Action_o,
       "miboc3AtmLineStatus-IntervalPerformanceMonitoringTable": miboc3AtmLineStatus_IntervalPerformanceMonitoringTable,
       "miboc3AtmLineStatus-IntervalPerformanceMonitoringEntry": miboc3AtmLineStatus_IntervalPerformanceMonitoringEntry,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-Shelf-o": oc3AtmLineStatus_IntervalPerformanceMonitoring_Shelf_o,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-Slot-o": oc3AtmLineStatus_IntervalPerformanceMonitoring_Slot_o,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-Item-o": oc3AtmLineStatus_IntervalPerformanceMonitoring_Item_o,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-Index-o": oc3AtmLineStatus_IntervalPerformanceMonitoring_Index_o,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetSectionErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetSectionSeverelyErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetSectionSeverelyErroredFramingSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionSeverelyErroredFramingSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetSectionCodingViolations": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetSectionCodingViolations,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetLineErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetLineSeverelyErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineSeverelyErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetLineCodingViolations": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineCodingViolations,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetLineUnavailableSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetLineUnavailableSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndLineErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndLineSeverelyErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineSeverelyErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndLineCodingViolations": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineCodingViolations,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndLineUnavailableSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndLineUnavailableSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetPathErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetPathSeverelyErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathSeverelyErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetPathCodingViolations": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathCodingViolations,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetPathUnavailableSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetPathUnavailableSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndPathErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndPathSeverelyErroredSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathSeverelyErroredSeconds,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndPathCodingViolations": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathCodingViolations,
       "oc3AtmLineStatus-IntervalPerformanceMonitoring-SonetFarEndPathUnavailableSeconds": oc3AtmLineStatus_IntervalPerformanceMonitoring_SonetFarEndPathUnavailableSeconds,
       "mibe3AtmLineStatus": mibe3AtmLineStatus,
       "mibe3AtmLineStatusTable": mibe3AtmLineStatusTable,
       "mibe3AtmLineStatusEntry": mibe3AtmLineStatusEntry,
       "e3AtmLineStatus-Shelf-o": e3AtmLineStatus_Shelf_o,
       "e3AtmLineStatus-Slot-o": e3AtmLineStatus_Slot_o,
       "e3AtmLineStatus-Item-o": e3AtmLineStatus_Item_o,
       "e3AtmLineStatus-PhysicalAddress-Shelf": e3AtmLineStatus_PhysicalAddress_Shelf,
       "e3AtmLineStatus-PhysicalAddress-Slot": e3AtmLineStatus_PhysicalAddress_Slot,
       "e3AtmLineStatus-PhysicalAddress-ItemNumber": e3AtmLineStatus_PhysicalAddress_ItemNumber,
       "e3AtmLineStatus-LineState": e3AtmLineStatus_LineState,
       "e3AtmLineStatus-SparePhysicalAddress-Shelf": e3AtmLineStatus_SparePhysicalAddress_Shelf,
       "e3AtmLineStatus-SparePhysicalAddress-Slot": e3AtmLineStatus_SparePhysicalAddress_Slot,
       "e3AtmLineStatus-SparePhysicalAddress-ItemNumber": e3AtmLineStatus_SparePhysicalAddress_ItemNumber,
       "e3AtmLineStatus-SparingState": e3AtmLineStatus_SparingState,
       "e3AtmLineStatus-SparingChangeReason": e3AtmLineStatus_SparingChangeReason,
       "e3AtmLineStatus-SparingChangeTime": e3AtmLineStatus_SparingChangeTime,
       "e3AtmLineStatus-SparingChangeCounter": e3AtmLineStatus_SparingChangeCounter,
       "e3AtmLineStatus-VpiVciRange": e3AtmLineStatus_VpiVciRange,
       "e3AtmLineStatus-VcSwitchingVpi": e3AtmLineStatus_VcSwitchingVpi,
       "e3AtmLineStatus-FBitErrorCount": e3AtmLineStatus_FBitErrorCount,
       "e3AtmLineStatus-PBitErrorCount": e3AtmLineStatus_PBitErrorCount,
       "e3AtmLineStatus-CpBitErrorCount": e3AtmLineStatus_CpBitErrorCount,
       "e3AtmLineStatus-FebErrorCount": e3AtmLineStatus_FebErrorCount,
       "e3AtmLineStatus-BpvErrorCount": e3AtmLineStatus_BpvErrorCount,
       "e3AtmLineStatus-LossOfSignal": e3AtmLineStatus_LossOfSignal,
       "e3AtmLineStatus-LossOfFrame": e3AtmLineStatus_LossOfFrame,
       "e3AtmLineStatus-YellowReceive": e3AtmLineStatus_YellowReceive,
       "e3AtmLineStatus-AisReceive": e3AtmLineStatus_AisReceive,
       "e3AtmLineStatus-Action-o": e3AtmLineStatus_Action_o,
       "mibatmIfStatus": mibatmIfStatus,
       "mibatmIfStatusTable": mibatmIfStatusTable,
       "mibatmIfStatusEntry": mibatmIfStatusEntry,
       "atmIfStatus-Shelf-o": atmIfStatus_Shelf_o,
       "atmIfStatus-Slot-o": atmIfStatus_Slot_o,
       "atmIfStatus-Item-o": atmIfStatus_Item_o,
       "atmIfStatus-LogicalItem-o": atmIfStatus_LogicalItem_o,
       "atmIfStatus-Address-PhysicalAddress-Shelf": atmIfStatus_Address_PhysicalAddress_Shelf,
       "atmIfStatus-Address-PhysicalAddress-Slot": atmIfStatus_Address_PhysicalAddress_Slot,
       "atmIfStatus-Address-PhysicalAddress-ItemNumber": atmIfStatus_Address_PhysicalAddress_ItemNumber,
       "atmIfStatus-Address-LogicalItem": atmIfStatus_Address_LogicalItem,
       "atmIfStatus-IfNumber": atmIfStatus_IfNumber,
       "atmIfStatus-NailedGroup": atmIfStatus_NailedGroup,
       "atmIfStatus-PortState": atmIfStatus_PortState,
       "atmIfStatus-SignallingState": atmIfStatus_SignallingState,
       "atmIfStatus-PnniLinkState": atmIfStatus_PnniLinkState,
       "atmIfStatus-Action-o": atmIfStatus_Action_o}
)
