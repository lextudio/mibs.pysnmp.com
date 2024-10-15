# SNMP MIB module (ASCEND-MIBSWANNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSWANNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:22 2024
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

_MibswanNetworkProfile_ObjectIdentity = ObjectIdentity
mibswanNetworkProfile = _MibswanNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 124)
)
_MibswanNetworkProfileTable_Object = MibTable
mibswanNetworkProfileTable = _MibswanNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1)
)
if mibBuilder.loadTexts:
    mibswanNetworkProfileTable.setStatus("mandatory")
_MibswanNetworkProfileEntry_Object = MibTableRow
mibswanNetworkProfileEntry = _MibswanNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1)
)
mibswanNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSWANNET-MIB", "swanNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBSWANNET-MIB", "swanNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBSWANNET-MIB", "swanNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibswanNetworkProfileEntry.setStatus("mandatory")
_SwanNetworkProfile_Shelf_o_Type = Integer32
_SwanNetworkProfile_Shelf_o_Object = MibScalar
swanNetworkProfile_Shelf_o = _SwanNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 1),
    _SwanNetworkProfile_Shelf_o_Type()
)
swanNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanNetworkProfile_Shelf_o.setStatus("mandatory")
_SwanNetworkProfile_Slot_o_Type = Integer32
_SwanNetworkProfile_Slot_o_Object = MibScalar
swanNetworkProfile_Slot_o = _SwanNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 2),
    _SwanNetworkProfile_Slot_o_Type()
)
swanNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanNetworkProfile_Slot_o.setStatus("mandatory")
_SwanNetworkProfile_Item_o_Type = Integer32
_SwanNetworkProfile_Item_o_Object = MibScalar
swanNetworkProfile_Item_o = _SwanNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 3),
    _SwanNetworkProfile_Item_o_Type()
)
swanNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanNetworkProfile_Item_o.setStatus("mandatory")
_SwanNetworkProfile_Name_Type = DisplayString
_SwanNetworkProfile_Name_Object = MibScalar
swanNetworkProfile_Name = _SwanNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 4),
    _SwanNetworkProfile_Name_Type()
)
swanNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_Name.setStatus("mandatory")


class _SwanNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type swanNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_SwanNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_SwanNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
swanNetworkProfile_PhysicalAddress_Shelf = _SwanNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 5),
    _SwanNetworkProfile_PhysicalAddress_Shelf_Type()
)
swanNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _SwanNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type swanNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_SwanNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_SwanNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
swanNetworkProfile_PhysicalAddress_Slot = _SwanNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 6),
    _SwanNetworkProfile_PhysicalAddress_Slot_Type()
)
swanNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_SwanNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_SwanNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
swanNetworkProfile_PhysicalAddress_ItemNumber = _SwanNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 7),
    _SwanNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
swanNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _SwanNetworkProfile_Enabled_Type(Integer32):
    """Custom type swanNetworkProfile_Enabled based on Integer32"""
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


_SwanNetworkProfile_Enabled_Type.__name__ = "Integer32"
_SwanNetworkProfile_Enabled_Object = MibScalar
swanNetworkProfile_Enabled = _SwanNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 8),
    _SwanNetworkProfile_Enabled_Type()
)
swanNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_Enabled.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_SwanNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
swanNetworkProfile_LineConfig_TrunkGroup = _SwanNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 9),
    _SwanNetworkProfile_LineConfig_TrunkGroup_Type()
)
swanNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_SwanNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
swanNetworkProfile_LineConfig_NailedGroup = _SwanNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 10),
    _SwanNetworkProfile_LineConfig_NailedGroup_Type()
)
swanNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
swanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 11),
    _SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
swanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
swanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 12),
    _SwanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
swanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_SwanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
swanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _SwanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 13),
    _SwanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
swanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _SwanNetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type swanNetworkProfile_LineConfig_Activation based on Integer32"""
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


_SwanNetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_SwanNetworkProfile_LineConfig_Activation_Object = MibScalar
swanNetworkProfile_LineConfig_Activation = _SwanNetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 14),
    _SwanNetworkProfile_LineConfig_Activation_Type()
)
swanNetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _SwanNetworkProfile_LineConfig_Clocking_ClockMode_Type(Integer32):
    """Custom type swanNetworkProfile_LineConfig_Clocking_ClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClock", 1),
          ("internalClock", 2))
    )


_SwanNetworkProfile_LineConfig_Clocking_ClockMode_Type.__name__ = "Integer32"
_SwanNetworkProfile_LineConfig_Clocking_ClockMode_Object = MibScalar
swanNetworkProfile_LineConfig_Clocking_ClockMode = _SwanNetworkProfile_LineConfig_Clocking_ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 18),
    _SwanNetworkProfile_LineConfig_Clocking_ClockMode_Type()
)
swanNetworkProfile_LineConfig_Clocking_ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_Clocking_ClockMode.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_Clocking_Divider_Type = Integer32
_SwanNetworkProfile_LineConfig_Clocking_Divider_Object = MibScalar
swanNetworkProfile_LineConfig_Clocking_Divider = _SwanNetworkProfile_LineConfig_Clocking_Divider_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 19),
    _SwanNetworkProfile_LineConfig_Clocking_Divider_Type()
)
swanNetworkProfile_LineConfig_Clocking_Divider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_Clocking_Divider.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_Clocking_Exp_Type = Integer32
_SwanNetworkProfile_LineConfig_Clocking_Exp_Object = MibScalar
swanNetworkProfile_LineConfig_Clocking_Exp = _SwanNetworkProfile_LineConfig_Clocking_Exp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 20),
    _SwanNetworkProfile_LineConfig_Clocking_Exp_Type()
)
swanNetworkProfile_LineConfig_Clocking_Exp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_Clocking_Exp.setStatus("mandatory")
_SwanNetworkProfile_LineConfig_Clocking_LineRate_Type = Integer32
_SwanNetworkProfile_LineConfig_Clocking_LineRate_Object = MibScalar
swanNetworkProfile_LineConfig_Clocking_LineRate = _SwanNetworkProfile_LineConfig_Clocking_LineRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 21),
    _SwanNetworkProfile_LineConfig_Clocking_LineRate_Type()
)
swanNetworkProfile_LineConfig_Clocking_LineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_LineConfig_Clocking_LineRate.setStatus("mandatory")


class _SwanNetworkProfile_Action_o_Type(Integer32):
    """Custom type swanNetworkProfile_Action_o based on Integer32"""
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


_SwanNetworkProfile_Action_o_Type.__name__ = "Integer32"
_SwanNetworkProfile_Action_o_Object = MibScalar
swanNetworkProfile_Action_o = _SwanNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 124, 1, 1, 22),
    _SwanNetworkProfile_Action_o_Type()
)
swanNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNetworkProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSWANNET-MIB",
    **{"DisplayString": DisplayString,
       "mibswanNetworkProfile": mibswanNetworkProfile,
       "mibswanNetworkProfileTable": mibswanNetworkProfileTable,
       "mibswanNetworkProfileEntry": mibswanNetworkProfileEntry,
       "swanNetworkProfile-Shelf-o": swanNetworkProfile_Shelf_o,
       "swanNetworkProfile-Slot-o": swanNetworkProfile_Slot_o,
       "swanNetworkProfile-Item-o": swanNetworkProfile_Item_o,
       "swanNetworkProfile-Name": swanNetworkProfile_Name,
       "swanNetworkProfile-PhysicalAddress-Shelf": swanNetworkProfile_PhysicalAddress_Shelf,
       "swanNetworkProfile-PhysicalAddress-Slot": swanNetworkProfile_PhysicalAddress_Slot,
       "swanNetworkProfile-PhysicalAddress-ItemNumber": swanNetworkProfile_PhysicalAddress_ItemNumber,
       "swanNetworkProfile-Enabled": swanNetworkProfile_Enabled,
       "swanNetworkProfile-LineConfig-TrunkGroup": swanNetworkProfile_LineConfig_TrunkGroup,
       "swanNetworkProfile-LineConfig-NailedGroup": swanNetworkProfile_LineConfig_NailedGroup,
       "swanNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": swanNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "swanNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": swanNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "swanNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": swanNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "swanNetworkProfile-LineConfig-Activation": swanNetworkProfile_LineConfig_Activation,
       "swanNetworkProfile-LineConfig-Clocking-ClockMode": swanNetworkProfile_LineConfig_Clocking_ClockMode,
       "swanNetworkProfile-LineConfig-Clocking-Divider": swanNetworkProfile_LineConfig_Clocking_Divider,
       "swanNetworkProfile-LineConfig-Clocking-Exp": swanNetworkProfile_LineConfig_Clocking_Exp,
       "swanNetworkProfile-LineConfig-Clocking-LineRate": swanNetworkProfile_LineConfig_Clocking_LineRate,
       "swanNetworkProfile-Action-o": swanNetworkProfile_Action_o}
)
