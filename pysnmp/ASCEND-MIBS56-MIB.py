# SNMP MIB module (ASCEND-MIBS56-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBS56-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:08 2024
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

_Mibs56NetworkProfile_ObjectIdentity = ObjectIdentity
mibs56NetworkProfile = _Mibs56NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 106)
)
_Mibs56NetworkProfileTable_Object = MibTable
mibs56NetworkProfileTable = _Mibs56NetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1)
)
if mibBuilder.loadTexts:
    mibs56NetworkProfileTable.setStatus("mandatory")
_Mibs56NetworkProfileEntry_Object = MibTableRow
mibs56NetworkProfileEntry = _Mibs56NetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1)
)
mibs56NetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-Slot-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibs56NetworkProfileEntry.setStatus("mandatory")
_S56NetworkProfile_Shelf_o_Type = Integer32
_S56NetworkProfile_Shelf_o_Object = MibScalar
s56NetworkProfile_Shelf_o = _S56NetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 1),
    _S56NetworkProfile_Shelf_o_Type()
)
s56NetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_Shelf_o.setStatus("mandatory")
_S56NetworkProfile_Slot_o_Type = Integer32
_S56NetworkProfile_Slot_o_Object = MibScalar
s56NetworkProfile_Slot_o = _S56NetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 2),
    _S56NetworkProfile_Slot_o_Type()
)
s56NetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_Slot_o.setStatus("mandatory")
_S56NetworkProfile_Item_o_Type = Integer32
_S56NetworkProfile_Item_o_Object = MibScalar
s56NetworkProfile_Item_o = _S56NetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 3),
    _S56NetworkProfile_Item_o_Type()
)
s56NetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_Item_o.setStatus("mandatory")
_S56NetworkProfile_ProfileNumber_Type = Integer32
_S56NetworkProfile_ProfileNumber_Object = MibScalar
s56NetworkProfile_ProfileNumber = _S56NetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 4),
    _S56NetworkProfile_ProfileNumber_Type()
)
s56NetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_ProfileNumber.setStatus("mandatory")
_S56NetworkProfile_Name_Type = DisplayString
_S56NetworkProfile_Name_Object = MibScalar
s56NetworkProfile_Name = _S56NetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 5),
    _S56NetworkProfile_Name_Type()
)
s56NetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_Name.setStatus("mandatory")


class _S56NetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type s56NetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_S56NetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_S56NetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
s56NetworkProfile_PhysicalAddress_Shelf = _S56NetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 6),
    _S56NetworkProfile_PhysicalAddress_Shelf_Type()
)
s56NetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _S56NetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type s56NetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_S56NetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_S56NetworkProfile_PhysicalAddress_Slot_Object = MibScalar
s56NetworkProfile_PhysicalAddress_Slot = _S56NetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 7),
    _S56NetworkProfile_PhysicalAddress_Slot_Type()
)
s56NetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_S56NetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_S56NetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
s56NetworkProfile_PhysicalAddress_ItemNumber = _S56NetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 8),
    _S56NetworkProfile_PhysicalAddress_ItemNumber_Type()
)
s56NetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _S56NetworkProfile_Action_o_Type(Integer32):
    """Custom type s56NetworkProfile_Action_o based on Integer32"""
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


_S56NetworkProfile_Action_o_Type.__name__ = "Integer32"
_S56NetworkProfile_Action_o_Object = MibScalar
s56NetworkProfile_Action_o = _S56NetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 1, 1, 9),
    _S56NetworkProfile_Action_o_Type()
)
s56NetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_Action_o.setStatus("mandatory")
_Mibs56NetworkProfile_LineInterfaceTable_Object = MibTable
mibs56NetworkProfile_LineInterfaceTable = _Mibs56NetworkProfile_LineInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 2)
)
if mibBuilder.loadTexts:
    mibs56NetworkProfile_LineInterfaceTable.setStatus("mandatory")
_Mibs56NetworkProfile_LineInterfaceEntry_Object = MibTableRow
mibs56NetworkProfile_LineInterfaceEntry = _Mibs56NetworkProfile_LineInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 2, 1)
)
mibs56NetworkProfile_LineInterfaceEntry.setIndexNames(
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-Shelf-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-Slot-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-Item-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-Index-o"),
)
if mibBuilder.loadTexts:
    mibs56NetworkProfile_LineInterfaceEntry.setStatus("mandatory")
_S56NetworkProfile_LineInterface_Shelf_o_Type = Integer32
_S56NetworkProfile_LineInterface_Shelf_o_Object = MibScalar
s56NetworkProfile_LineInterface_Shelf_o = _S56NetworkProfile_LineInterface_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 2, 1, 1),
    _S56NetworkProfile_LineInterface_Shelf_o_Type()
)
s56NetworkProfile_LineInterface_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_Shelf_o.setStatus("mandatory")
_S56NetworkProfile_LineInterface_Slot_o_Type = Integer32
_S56NetworkProfile_LineInterface_Slot_o_Object = MibScalar
s56NetworkProfile_LineInterface_Slot_o = _S56NetworkProfile_LineInterface_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 2, 1, 2),
    _S56NetworkProfile_LineInterface_Slot_o_Type()
)
s56NetworkProfile_LineInterface_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_Slot_o.setStatus("mandatory")
_S56NetworkProfile_LineInterface_Item_o_Type = Integer32
_S56NetworkProfile_LineInterface_Item_o_Object = MibScalar
s56NetworkProfile_LineInterface_Item_o = _S56NetworkProfile_LineInterface_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 2, 1, 3),
    _S56NetworkProfile_LineInterface_Item_o_Type()
)
s56NetworkProfile_LineInterface_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_Item_o.setStatus("mandatory")
_S56NetworkProfile_LineInterface_Index_o_Type = Integer32
_S56NetworkProfile_LineInterface_Index_o_Object = MibScalar
s56NetworkProfile_LineInterface_Index_o = _S56NetworkProfile_LineInterface_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 2, 1, 4),
    _S56NetworkProfile_LineInterface_Index_o_Type()
)
s56NetworkProfile_LineInterface_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_Index_o.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_LineEnabled_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_LineEnabled based on Integer32"""
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


_S56NetworkProfile_LineInterface_LineEnabled_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_LineEnabled_Object = MibScalar
s56NetworkProfile_LineInterface_LineEnabled = _S56NetworkProfile_LineInterface_LineEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 2, 1, 5),
    _S56NetworkProfile_LineInterface_LineEnabled_Type()
)
s56NetworkProfile_LineInterface_LineEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_LineEnabled.setStatus("mandatory")
_Mibs56NetworkProfile_LineInterface_ChannelConfigTable_Object = MibTable
mibs56NetworkProfile_LineInterface_ChannelConfigTable = _Mibs56NetworkProfile_LineInterface_ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3)
)
if mibBuilder.loadTexts:
    mibs56NetworkProfile_LineInterface_ChannelConfigTable.setStatus("mandatory")
_Mibs56NetworkProfile_LineInterface_ChannelConfigEntry_Object = MibTableRow
mibs56NetworkProfile_LineInterface_ChannelConfigEntry = _Mibs56NetworkProfile_LineInterface_ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1)
)
mibs56NetworkProfile_LineInterface_ChannelConfigEntry.setIndexNames(
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-ChannelConfig-Shelf-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-ChannelConfig-Slot-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-ChannelConfig-Item-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-ChannelConfig-Index-o"),
    (0, "ASCEND-MIBS56-MIB", "s56NetworkProfile-LineInterface-ChannelConfig-Index1-o"),
)
if mibBuilder.loadTexts:
    mibs56NetworkProfile_LineInterface_ChannelConfigEntry.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_Shelf_o = _S56NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 1),
    _S56NetworkProfile_LineInterface_ChannelConfig_Shelf_o_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_Shelf_o.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_Slot_o_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_Slot_o_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_Slot_o = _S56NetworkProfile_LineInterface_ChannelConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 2),
    _S56NetworkProfile_LineInterface_ChannelConfig_Slot_o_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_Slot_o.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_Item_o_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_Item_o_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_Item_o = _S56NetworkProfile_LineInterface_ChannelConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 3),
    _S56NetworkProfile_LineInterface_ChannelConfig_Item_o_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_Item_o.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_Index_o_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_Index_o_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_Index_o = _S56NetworkProfile_LineInterface_ChannelConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 4),
    _S56NetworkProfile_LineInterface_ChannelConfig_Index_o_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_Index_o.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_Index1_o_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_Index1_o_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_Index1_o = _S56NetworkProfile_LineInterface_ChannelConfig_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 5),
    _S56NetworkProfile_LineInterface_ChannelConfig_Index1_o_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_Index1_o.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage based on Integer32"""
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
        *(("dChannel", 4),
          ("nailed64Channel", 3),
          ("nfasPrimaryDChannel", 5),
          ("nfasSecondaryDChannel", 6),
          ("semiPermChannel", 7),
          ("ss7SignalingChannel", 8),
          ("switchedChannel", 2),
          ("unusedChannel", 1))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage = _S56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 6),
    _S56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable = _S56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 7),
    _S56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Type = DisplayString
_S56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber = _S56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 8),
    _S56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber = _S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 9),
    _S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber = _S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 10),
    _S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber = _S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 11),
    _S56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup = _S56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 12),
    _S56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 2),
          ("singlebaud", 3))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode = _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 13),
    _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("n-1088000", 51),
          ("n-272000", 57),
          ("n-408000", 56),
          ("n-544000", 55),
          ("n-680000", 54),
          ("n-816000", 53),
          ("n-952000", 52))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate = _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 14),
    _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("n-1280000", 11),
          ("n-1600000", 10),
          ("n-1920000", 9),
          ("n-2240000", 8),
          ("n-2560000", 7),
          ("n-2688000", 6),
          ("n-3200000", 5),
          ("n-4480000", 4),
          ("n-5120000", 3),
          ("n-6272000", 2),
          ("n-640000", 13),
          ("n-7168000", 1),
          ("n-960000", 12))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate = _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 15),
    _S56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("n-1088000", 152),
          ("n-128000", 161),
          ("n-256000", 160),
          ("n-384000", 159),
          ("n-512000", 158),
          ("n-640000", 157),
          ("n-768000", 156),
          ("n-800000", 155),
          ("n-896000", 154),
          ("n-928000", 153),
          ("upstrmMegMax", 151))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate = _S56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 16),
    _S56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122)
        )
    )
    namedValues = NamedValues(
        *(("dwnstrmMegMax", 101),
          ("n-128000", 122),
          ("n-1280000", 115),
          ("n-1600000", 114),
          ("n-1920000", 113),
          ("n-2240000", 112),
          ("n-256000", 121),
          ("n-2560000", 111),
          ("n-2688000", 110),
          ("n-3200000", 109),
          ("n-384000", 120),
          ("n-4480000", 108),
          ("n-512000", 119),
          ("n-5120000", 107),
          ("n-6272000", 106),
          ("n-640000", 118),
          ("n-7168000", 105),
          ("n-768000", 117),
          ("n-8000000", 104),
          ("n-8960000", 103),
          ("n-9504000", 102),
          ("n-960000", 116))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate = _S56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 17),
    _S56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 2),
          ("singlebaud", 3))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode = _S56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 18),
    _S56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin = _S56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 19),
    _S56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin = _S56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 20),
    _S56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17,
              33,
              65)
        )
    )
    namedValues = NamedValues(
        *(("dmt0", 1),
          ("dmt16", 17),
          ("dmt2", 3),
          ("dmt32", 33),
          ("dmt4", 5),
          ("dmt64", 65),
          ("dmt8", 9))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave = _S56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 21),
    _S56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17,
              33,
              65)
        )
    )
    namedValues = NamedValues(
        *(("dmt0", 1),
          ("dmt16", 17),
          ("dmt2", 3),
          ("dmt32", 33),
          ("dmt4", 5),
          ("dmt64", 65),
          ("dmt8", 9))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave = _S56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 22),
    _S56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel = _S56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 23),
    _S56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState based on Integer32"""
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
        *(("adjusting", 2),
          ("disabled", 1),
          ("locked", 4),
          ("tracking", 3))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState = _S56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 24),
    _S56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp = _S56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 25),
    _S56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inv", 2),
          ("normal", 1))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense = _S56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 26),
    _S56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("serial", 1)
    )


_S56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat = _S56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 27),
    _S56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 2),
          ("singlebaud", 3))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode = _S56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 28),
    _S56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("n-1040000", 15),
          ("n-1152000", 16),
          ("n-1168000", 6),
          ("n-144000", 1),
          ("n-1536000", 17),
          ("n-1552000", 7),
          ("n-1568000", 18),
          ("n-160000", 9),
          ("n-1680000", 19),
          ("n-192000", 10),
          ("n-1920000", 20),
          ("n-208000", 11),
          ("n-2160000", 21),
          ("n-2320000", 8),
          ("n-272000", 2),
          ("n-384000", 12),
          ("n-400000", 3),
          ("n-416000", 13),
          ("n-528000", 4),
          ("n-768000", 14),
          ("n-784000", 5))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate = _S56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 29),
    _S56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType = _S56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 30),
    _S56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("n-1040000", 15),
          ("n-1152000", 16),
          ("n-1168000", 6),
          ("n-144000", 1),
          ("n-1536000", 17),
          ("n-1552000", 7),
          ("n-1568000", 18),
          ("n-160000", 9),
          ("n-1680000", 19),
          ("n-192000", 10),
          ("n-1920000", 20),
          ("n-208000", 11),
          ("n-2160000", 21),
          ("n-2320000", 8),
          ("n-272000", 2),
          ("n-384000", 12),
          ("n-400000", 3),
          ("n-416000", 13),
          ("n-528000", 4),
          ("n-768000", 14),
          ("n-784000", 5))
    )


_S56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate = _S56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 31),
    _S56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType = _S56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 32),
    _S56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("upstrmBoost", 1)
    )


_S56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance = _S56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 33),
    _S56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_Trellis_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_Trellis based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_Trellis_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_Trellis_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_Trellis = _S56NetworkProfile_LineInterface_ChannelConfig_Trellis_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 34),
    _S56NetworkProfile_LineInterface_ChannelConfig_Trellis_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_Trellis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_Trellis.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode = _S56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 35),
    _S56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_FastRetrain_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_FastRetrain based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_FastRetrain_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_FastRetrain_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_FastRetrain = _S56NetworkProfile_LineInterface_ChannelConfig_FastRetrain_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 36),
    _S56NetworkProfile_LineInterface_ChannelConfig_FastRetrain_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_FastRetrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_FastRetrain.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_BitSwapping_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_BitSwapping based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_BitSwapping_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_BitSwapping_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_BitSwapping = _S56NetworkProfile_LineInterface_ChannelConfig_BitSwapping_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 37),
    _S56NetworkProfile_LineInterface_ChannelConfig_BitSwapping_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_BitSwapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_BitSwapping.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_FramingMode_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_FramingMode_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_FramingMode = _S56NetworkProfile_LineInterface_ChannelConfig_FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 38),
    _S56NetworkProfile_LineInterface_ChannelConfig_FramingMode_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_FramingMode.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_TxPower_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_TxPower_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_TxPower = _S56NetworkProfile_LineInterface_ChannelConfig_TxPower_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 39),
    _S56NetworkProfile_LineInterface_ChannelConfig_TxPower_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_TxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_TxPower.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate = _S56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 40),
    _S56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin = _S56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 41),
    _S56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin = _S56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 42),
    _S56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin = _S56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 43),
    _S56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin.setStatus("mandatory")
_S56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin_Type = Integer32
_S56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin = _S56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 44),
    _S56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType = _S56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 45),
    _S56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_RateMode_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_RateMode based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_RateMode_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_RateMode_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_RateMode = _S56NetworkProfile_LineInterface_ChannelConfig_RateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 46),
    _S56NetworkProfile_LineInterface_ChannelConfig_RateMode_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_RateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_RateMode.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_MaxRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_MaxRate based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_MaxRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_MaxRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_MaxRate = _S56NetworkProfile_LineInterface_ChannelConfig_MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 47),
    _S56NetworkProfile_LineInterface_ChannelConfig_MaxRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_MaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_MaxRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_MinRate_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_MinRate based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_MinRate_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_MinRate_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_MinRate = _S56NetworkProfile_LineInterface_ChannelConfig_MinRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 48),
    _S56NetworkProfile_LineInterface_ChannelConfig_MinRate_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_MinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_MinRate.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType = _S56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 49),
    _S56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType = _S56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 50),
    _S56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType.setStatus("mandatory")


class _S56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled_Type(Integer32):
    """Custom type s56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled based on Integer32"""
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


_S56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled_Type.__name__ = "Integer32"
_S56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled_Object = MibScalar
s56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled = _S56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 106, 3, 1, 52),
    _S56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled_Type()
)
s56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBS56-MIB",
    **{"DisplayString": DisplayString,
       "mibs56NetworkProfile": mibs56NetworkProfile,
       "mibs56NetworkProfileTable": mibs56NetworkProfileTable,
       "mibs56NetworkProfileEntry": mibs56NetworkProfileEntry,
       "s56NetworkProfile-Shelf-o": s56NetworkProfile_Shelf_o,
       "s56NetworkProfile-Slot-o": s56NetworkProfile_Slot_o,
       "s56NetworkProfile-Item-o": s56NetworkProfile_Item_o,
       "s56NetworkProfile-ProfileNumber": s56NetworkProfile_ProfileNumber,
       "s56NetworkProfile-Name": s56NetworkProfile_Name,
       "s56NetworkProfile-PhysicalAddress-Shelf": s56NetworkProfile_PhysicalAddress_Shelf,
       "s56NetworkProfile-PhysicalAddress-Slot": s56NetworkProfile_PhysicalAddress_Slot,
       "s56NetworkProfile-PhysicalAddress-ItemNumber": s56NetworkProfile_PhysicalAddress_ItemNumber,
       "s56NetworkProfile-Action-o": s56NetworkProfile_Action_o,
       "mibs56NetworkProfile-LineInterfaceTable": mibs56NetworkProfile_LineInterfaceTable,
       "mibs56NetworkProfile-LineInterfaceEntry": mibs56NetworkProfile_LineInterfaceEntry,
       "s56NetworkProfile-LineInterface-Shelf-o": s56NetworkProfile_LineInterface_Shelf_o,
       "s56NetworkProfile-LineInterface-Slot-o": s56NetworkProfile_LineInterface_Slot_o,
       "s56NetworkProfile-LineInterface-Item-o": s56NetworkProfile_LineInterface_Item_o,
       "s56NetworkProfile-LineInterface-Index-o": s56NetworkProfile_LineInterface_Index_o,
       "s56NetworkProfile-LineInterface-LineEnabled": s56NetworkProfile_LineInterface_LineEnabled,
       "mibs56NetworkProfile-LineInterface-ChannelConfigTable": mibs56NetworkProfile_LineInterface_ChannelConfigTable,
       "mibs56NetworkProfile-LineInterface-ChannelConfigEntry": mibs56NetworkProfile_LineInterface_ChannelConfigEntry,
       "s56NetworkProfile-LineInterface-ChannelConfig-Shelf-o": s56NetworkProfile_LineInterface_ChannelConfig_Shelf_o,
       "s56NetworkProfile-LineInterface-ChannelConfig-Slot-o": s56NetworkProfile_LineInterface_ChannelConfig_Slot_o,
       "s56NetworkProfile-LineInterface-ChannelConfig-Item-o": s56NetworkProfile_LineInterface_ChannelConfig_Item_o,
       "s56NetworkProfile-LineInterface-ChannelConfig-Index-o": s56NetworkProfile_LineInterface_ChannelConfig_Index_o,
       "s56NetworkProfile-LineInterface-ChannelConfig-Index1-o": s56NetworkProfile_LineInterface_ChannelConfig_Index1_o,
       "s56NetworkProfile-LineInterface-ChannelConfig-ChannelUsage": s56NetworkProfile_LineInterface_ChannelConfig_ChannelUsage,
       "s56NetworkProfile-LineInterface-ChannelConfig-LoopbackEnable": s56NetworkProfile_LineInterface_ChannelConfig_LoopbackEnable,
       "s56NetworkProfile-LineInterface-ChannelConfig-PhoneNumber": s56NetworkProfile_LineInterface_ChannelConfig_PhoneNumber,
       "s56NetworkProfile-LineInterface-ChannelConfig-RoutePort-SlotNumber-SlotNumber": s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_SlotNumber,
       "s56NetworkProfile-LineInterface-ChannelConfig-RoutePort-SlotNumber-ShelfNumber": s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_SlotNumber_ShelfNumber,
       "s56NetworkProfile-LineInterface-ChannelConfig-RoutePort-RelativePortNumber-RelativePortNumber": s56NetworkProfile_LineInterface_ChannelConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "s56NetworkProfile-LineInterface-ChannelConfig-TrunkGroup": s56NetworkProfile_LineInterface_ChannelConfig_TrunkGroup,
       "s56NetworkProfile-LineInterface-ChannelConfig-AdslCapRateMode": s56NetworkProfile_LineInterface_ChannelConfig_AdslCapRateMode,
       "s56NetworkProfile-LineInterface-ChannelConfig-AdslCapUpStreamRate": s56NetworkProfile_LineInterface_ChannelConfig_AdslCapUpStreamRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-AdslCapDownStreamRate": s56NetworkProfile_LineInterface_ChannelConfig_AdslCapDownStreamRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-MaxUpStreamRate": s56NetworkProfile_LineInterface_ChannelConfig_MaxUpStreamRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-MaxDownStreamRate": s56NetworkProfile_LineInterface_ChannelConfig_MaxDownStreamRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-AdslDmtRateMode": s56NetworkProfile_LineInterface_ChannelConfig_AdslDmtRateMode,
       "s56NetworkProfile-LineInterface-ChannelConfig-UpStreamMargin": s56NetworkProfile_LineInterface_ChannelConfig_UpStreamMargin,
       "s56NetworkProfile-LineInterface-ChannelConfig-DownStreamMargin": s56NetworkProfile_LineInterface_ChannelConfig_DownStreamMargin,
       "s56NetworkProfile-LineInterface-ChannelConfig-UpStreamInterleave": s56NetworkProfile_LineInterface_ChannelConfig_UpStreamInterleave,
       "s56NetworkProfile-LineInterface-ChannelConfig-DownStreamInterleave": s56NetworkProfile_LineInterface_ChannelConfig_DownStreamInterleave,
       "s56NetworkProfile-LineInterface-ChannelConfig-TxPowerLevel": s56NetworkProfile_LineInterface_ChannelConfig_TxPowerLevel,
       "s56NetworkProfile-LineInterface-ChannelConfig-TxPowerAutoState": s56NetworkProfile_LineInterface_ChannelConfig_TxPowerAutoState,
       "s56NetworkProfile-LineInterface-ChannelConfig-MaintainLanUp": s56NetworkProfile_LineInterface_ChannelConfig_MaintainLanUp,
       "s56NetworkProfile-LineInterface-ChannelConfig-HdlcDataSense": s56NetworkProfile_LineInterface_ChannelConfig_HdlcDataSense,
       "s56NetworkProfile-LineInterface-ChannelConfig-SdslDataFormat": s56NetworkProfile_LineInterface_ChannelConfig_SdslDataFormat,
       "s56NetworkProfile-LineInterface-ChannelConfig-SdslRateMode": s56NetworkProfile_LineInterface_ChannelConfig_SdslRateMode,
       "s56NetworkProfile-LineInterface-ChannelConfig-SdslLineRate": s56NetworkProfile_LineInterface_ChannelConfig_SdslLineRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-SdslUnitType": s56NetworkProfile_LineInterface_ChannelConfig_SdslUnitType,
       "s56NetworkProfile-LineInterface-ChannelConfig-SdslAutoBaseRate": s56NetworkProfile_LineInterface_ChannelConfig_SdslAutoBaseRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-Hdsl2UnitType": s56NetworkProfile_LineInterface_ChannelConfig_Hdsl2UnitType,
       "s56NetworkProfile-LineInterface-ChannelConfig-FrontEndBalance": s56NetworkProfile_LineInterface_ChannelConfig_FrontEndBalance,
       "s56NetworkProfile-LineInterface-ChannelConfig-Trellis": s56NetworkProfile_LineInterface_ChannelConfig_Trellis,
       "s56NetworkProfile-LineInterface-ChannelConfig-AdslLineCode": s56NetworkProfile_LineInterface_ChannelConfig_AdslLineCode,
       "s56NetworkProfile-LineInterface-ChannelConfig-FastRetrain": s56NetworkProfile_LineInterface_ChannelConfig_FastRetrain,
       "s56NetworkProfile-LineInterface-ChannelConfig-BitSwapping": s56NetworkProfile_LineInterface_ChannelConfig_BitSwapping,
       "s56NetworkProfile-LineInterface-ChannelConfig-FramingMode": s56NetworkProfile_LineInterface_ChannelConfig_FramingMode,
       "s56NetworkProfile-LineInterface-ChannelConfig-TxPower": s56NetworkProfile_LineInterface_ChannelConfig_TxPower,
       "s56NetworkProfile-LineInterface-ChannelConfig-MaxDownRate": s56NetworkProfile_LineInterface_ChannelConfig_MaxDownRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-DnstreamStartBin": s56NetworkProfile_LineInterface_ChannelConfig_DnstreamStartBin,
       "s56NetworkProfile-LineInterface-ChannelConfig-DnstreamEndBin": s56NetworkProfile_LineInterface_ChannelConfig_DnstreamEndBin,
       "s56NetworkProfile-LineInterface-ChannelConfig-UpstreamStartBin": s56NetworkProfile_LineInterface_ChannelConfig_UpstreamStartBin,
       "s56NetworkProfile-LineInterface-ChannelConfig-UpstreamEndBin": s56NetworkProfile_LineInterface_ChannelConfig_UpstreamEndBin,
       "s56NetworkProfile-LineInterface-ChannelConfig-HdslInterfaceType": s56NetworkProfile_LineInterface_ChannelConfig_HdslInterfaceType,
       "s56NetworkProfile-LineInterface-ChannelConfig-RateMode": s56NetworkProfile_LineInterface_ChannelConfig_RateMode,
       "s56NetworkProfile-LineInterface-ChannelConfig-MaxRate": s56NetworkProfile_LineInterface_ChannelConfig_MaxRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-MinRate": s56NetworkProfile_LineInterface_ChannelConfig_MinRate,
       "s56NetworkProfile-LineInterface-ChannelConfig-GshdslStandardNetworkType": s56NetworkProfile_LineInterface_ChannelConfig_GshdslStandardNetworkType,
       "s56NetworkProfile-LineInterface-ChannelConfig-GshdslPsdType": s56NetworkProfile_LineInterface_ChannelConfig_GshdslPsdType,
       "s56NetworkProfile-LineInterface-ChannelConfig-AnnexbAnfpEnabled": s56NetworkProfile_LineInterface_ChannelConfig_AnnexbAnfpEnabled}
)
