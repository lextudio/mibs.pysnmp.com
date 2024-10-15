# SNMP MIB module (ASCEND-MIBSTATICHSSLOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSTATICHSSLOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:18 2024
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

_MibmibProfHighSpeedSlotStatic_ObjectIdentity = ObjectIdentity
mibmibProfHighSpeedSlotStatic = _MibmibProfHighSpeedSlotStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 32)
)
_MibmibProfHighSpeedSlotStaticTable_Object = MibTable
mibmibProfHighSpeedSlotStaticTable = _MibmibProfHighSpeedSlotStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1)
)
if mibBuilder.loadTexts:
    mibmibProfHighSpeedSlotStaticTable.setStatus("mandatory")
_MibmibProfHighSpeedSlotStaticEntry_Object = MibTableRow
mibmibProfHighSpeedSlotStaticEntry = _MibmibProfHighSpeedSlotStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1)
)
mibmibProfHighSpeedSlotStaticEntry.setIndexNames(
    (0, "ASCEND-MIBSTATICHSSLOT-MIB", "mibProfHighSpeedSlotStatic-Shelf-o"),
    (0, "ASCEND-MIBSTATICHSSLOT-MIB", "mibProfHighSpeedSlotStatic-Slot-o"),
    (0, "ASCEND-MIBSTATICHSSLOT-MIB", "mibProfHighSpeedSlotStatic-Item-o"),
)
if mibBuilder.loadTexts:
    mibmibProfHighSpeedSlotStaticEntry.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_Shelf_o_Type = Integer32
_MibProfHighSpeedSlotStatic_Shelf_o_Object = MibScalar
mibProfHighSpeedSlotStatic_Shelf_o = _MibProfHighSpeedSlotStatic_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 1),
    _MibProfHighSpeedSlotStatic_Shelf_o_Type()
)
mibProfHighSpeedSlotStatic_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_Shelf_o.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_Slot_o_Type = Integer32
_MibProfHighSpeedSlotStatic_Slot_o_Object = MibScalar
mibProfHighSpeedSlotStatic_Slot_o = _MibProfHighSpeedSlotStatic_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 2),
    _MibProfHighSpeedSlotStatic_Slot_o_Type()
)
mibProfHighSpeedSlotStatic_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_Slot_o.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_Item_o_Type = Integer32
_MibProfHighSpeedSlotStatic_Item_o_Object = MibScalar
mibProfHighSpeedSlotStatic_Item_o = _MibProfHighSpeedSlotStatic_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 3),
    _MibProfHighSpeedSlotStatic_Item_o_Type()
)
mibProfHighSpeedSlotStatic_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_Item_o.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_Name_Type = DisplayString
_MibProfHighSpeedSlotStatic_Name_Object = MibScalar
mibProfHighSpeedSlotStatic_Name = _MibProfHighSpeedSlotStatic_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 4),
    _MibProfHighSpeedSlotStatic_Name_Type()
)
mibProfHighSpeedSlotStatic_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_Name.setStatus("mandatory")


class _MibProfHighSpeedSlotStatic_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf based on Integer32"""
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


_MibProfHighSpeedSlotStatic_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_MibProfHighSpeedSlotStatic_PhysicalAddress_Shelf_Object = MibScalar
mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf = _MibProfHighSpeedSlotStatic_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 5),
    _MibProfHighSpeedSlotStatic_PhysicalAddress_Shelf_Type()
)
mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf.setStatus("mandatory")


class _MibProfHighSpeedSlotStatic_PhysicalAddress_Slot_Type(Integer32):
    """Custom type mibProfHighSpeedSlotStatic_PhysicalAddress_Slot based on Integer32"""
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


_MibProfHighSpeedSlotStatic_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_MibProfHighSpeedSlotStatic_PhysicalAddress_Slot_Object = MibScalar
mibProfHighSpeedSlotStatic_PhysicalAddress_Slot = _MibProfHighSpeedSlotStatic_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 6),
    _MibProfHighSpeedSlotStatic_PhysicalAddress_Slot_Type()
)
mibProfHighSpeedSlotStatic_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_PhysicalAddress_Slot.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber_Type = Integer32
_MibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber_Object = MibScalar
mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber = _MibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 7),
    _MibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber_Type()
)
mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _MibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority_Type(Integer32):
    """Custom type mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("lowPriority", 1))
    )


_MibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority_Type.__name__ = "Integer32"
_MibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority_Object = MibScalar
mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority = _MibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 8),
    _MibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority_Type()
)
mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority.setStatus("mandatory")


class _MibProfHighSpeedSlotStatic_Action_o_Type(Integer32):
    """Custom type mibProfHighSpeedSlotStatic_Action_o based on Integer32"""
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


_MibProfHighSpeedSlotStatic_Action_o_Type.__name__ = "Integer32"
_MibProfHighSpeedSlotStatic_Action_o_Object = MibScalar
mibProfHighSpeedSlotStatic_Action_o = _MibProfHighSpeedSlotStatic_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 9),
    _MibProfHighSpeedSlotStatic_Action_o_Type()
)
mibProfHighSpeedSlotStatic_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_Action_o.setStatus("mandatory")


class _MibProfHighSpeedSlotStatic_TrunkCacConfig_Enable_Type(Integer32):
    """Custom type mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable based on Integer32"""
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


_MibProfHighSpeedSlotStatic_TrunkCacConfig_Enable_Type.__name__ = "Integer32"
_MibProfHighSpeedSlotStatic_TrunkCacConfig_Enable_Object = MibScalar
mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable = _MibProfHighSpeedSlotStatic_TrunkCacConfig_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 10),
    _MibProfHighSpeedSlotStatic_TrunkCacConfig_Enable_Type()
)
mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum_Type = DisplayString
_MibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum_Object = MibScalar
mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum = _MibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 11),
    _MibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum_Type()
)
mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate_Type = Integer32
_MibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate_Object = MibScalar
mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate = _MibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 12),
    _MibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate_Type()
)
mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate.setStatus("mandatory")
_MibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription_Type = Integer32
_MibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription_Object = MibScalar
mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription = _MibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 32, 1, 1, 13),
    _MibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription_Type()
)
mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSTATICHSSLOT-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfHighSpeedSlotStatic": mibmibProfHighSpeedSlotStatic,
       "mibmibProfHighSpeedSlotStaticTable": mibmibProfHighSpeedSlotStaticTable,
       "mibmibProfHighSpeedSlotStaticEntry": mibmibProfHighSpeedSlotStaticEntry,
       "mibProfHighSpeedSlotStatic-Shelf-o": mibProfHighSpeedSlotStatic_Shelf_o,
       "mibProfHighSpeedSlotStatic-Slot-o": mibProfHighSpeedSlotStatic_Slot_o,
       "mibProfHighSpeedSlotStatic-Item-o": mibProfHighSpeedSlotStatic_Item_o,
       "mibProfHighSpeedSlotStatic-Name": mibProfHighSpeedSlotStatic_Name,
       "mibProfHighSpeedSlotStatic-PhysicalAddress-Shelf": mibProfHighSpeedSlotStatic_PhysicalAddress_Shelf,
       "mibProfHighSpeedSlotStatic-PhysicalAddress-Slot": mibProfHighSpeedSlotStatic_PhysicalAddress_Slot,
       "mibProfHighSpeedSlotStatic-PhysicalAddress-ItemNumber": mibProfHighSpeedSlotStatic_PhysicalAddress_ItemNumber,
       "mibProfHighSpeedSlotStatic-AtmParameters-IncomingPriority": mibProfHighSpeedSlotStatic_AtmParameters_IncomingPriority,
       "mibProfHighSpeedSlotStatic-Action-o": mibProfHighSpeedSlotStatic_Action_o,
       "mibProfHighSpeedSlotStatic-TrunkCacConfig-Enable": mibProfHighSpeedSlotStatic_TrunkCacConfig_Enable,
       "mibProfHighSpeedSlotStatic-TrunkCacConfig-PortNum": mibProfHighSpeedSlotStatic_TrunkCacConfig_PortNum,
       "mibProfHighSpeedSlotStatic-TrunkCacConfig-LineRate": mibProfHighSpeedSlotStatic_TrunkCacConfig_LineRate,
       "mibProfHighSpeedSlotStatic-TrunkCacConfig-OverSubscription": mibProfHighSpeedSlotStatic_TrunkCacConfig_OverSubscription}
)
