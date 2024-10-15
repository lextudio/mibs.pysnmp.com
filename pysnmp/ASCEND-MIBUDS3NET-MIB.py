# SNMP MIB module (ASCEND-MIBUDS3NET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBUDS3NET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:30 2024
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

_Mibuds3NetworkProfile_ObjectIdentity = ObjectIdentity
mibuds3NetworkProfile = _Mibuds3NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 5)
)
_Mibuds3NetworkProfileTable_Object = MibTable
mibuds3NetworkProfileTable = _Mibuds3NetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1)
)
if mibBuilder.loadTexts:
    mibuds3NetworkProfileTable.setStatus("mandatory")
_Mibuds3NetworkProfileEntry_Object = MibTableRow
mibuds3NetworkProfileEntry = _Mibuds3NetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1)
)
mibuds3NetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBUDS3NET-MIB", "uds3NetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBUDS3NET-MIB", "uds3NetworkProfile-Slot-o"),
    (0, "ASCEND-MIBUDS3NET-MIB", "uds3NetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibuds3NetworkProfileEntry.setStatus("mandatory")
_Uds3NetworkProfile_Shelf_o_Type = Integer32
_Uds3NetworkProfile_Shelf_o_Object = MibScalar
uds3NetworkProfile_Shelf_o = _Uds3NetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 1),
    _Uds3NetworkProfile_Shelf_o_Type()
)
uds3NetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds3NetworkProfile_Shelf_o.setStatus("mandatory")
_Uds3NetworkProfile_Slot_o_Type = Integer32
_Uds3NetworkProfile_Slot_o_Object = MibScalar
uds3NetworkProfile_Slot_o = _Uds3NetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 2),
    _Uds3NetworkProfile_Slot_o_Type()
)
uds3NetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds3NetworkProfile_Slot_o.setStatus("mandatory")
_Uds3NetworkProfile_Item_o_Type = Integer32
_Uds3NetworkProfile_Item_o_Object = MibScalar
uds3NetworkProfile_Item_o = _Uds3NetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 3),
    _Uds3NetworkProfile_Item_o_Type()
)
uds3NetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds3NetworkProfile_Item_o.setStatus("mandatory")
_Uds3NetworkProfile_Name_Type = DisplayString
_Uds3NetworkProfile_Name_Object = MibScalar
uds3NetworkProfile_Name = _Uds3NetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 4),
    _Uds3NetworkProfile_Name_Type()
)
uds3NetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_Name.setStatus("mandatory")


class _Uds3NetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type uds3NetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_Uds3NetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Uds3NetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
uds3NetworkProfile_PhysicalAddress_Shelf = _Uds3NetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 5),
    _Uds3NetworkProfile_PhysicalAddress_Shelf_Type()
)
uds3NetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _Uds3NetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type uds3NetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_Uds3NetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Uds3NetworkProfile_PhysicalAddress_Slot_Object = MibScalar
uds3NetworkProfile_PhysicalAddress_Slot = _Uds3NetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 6),
    _Uds3NetworkProfile_PhysicalAddress_Slot_Type()
)
uds3NetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_Uds3NetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_Uds3NetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
uds3NetworkProfile_PhysicalAddress_ItemNumber = _Uds3NetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 7),
    _Uds3NetworkProfile_PhysicalAddress_ItemNumber_Type()
)
uds3NetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Uds3NetworkProfile_Enabled_Type(Integer32):
    """Custom type uds3NetworkProfile_Enabled based on Integer32"""
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


_Uds3NetworkProfile_Enabled_Type.__name__ = "Integer32"
_Uds3NetworkProfile_Enabled_Object = MibScalar
uds3NetworkProfile_Enabled = _Uds3NetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 8),
    _Uds3NetworkProfile_Enabled_Type()
)
uds3NetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_Enabled.setStatus("mandatory")
_Uds3NetworkProfile_ProfileNumber_Type = Integer32
_Uds3NetworkProfile_ProfileNumber_Object = MibScalar
uds3NetworkProfile_ProfileNumber = _Uds3NetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 9),
    _Uds3NetworkProfile_ProfileNumber_Type()
)
uds3NetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_ProfileNumber.setStatus("mandatory")
_Uds3NetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_Uds3NetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
uds3NetworkProfile_LineConfig_TrunkGroup = _Uds3NetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 10),
    _Uds3NetworkProfile_LineConfig_TrunkGroup_Type()
)
uds3NetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_Uds3NetworkProfile_LineConfig_NailedGroup_Type = Integer32
_Uds3NetworkProfile_LineConfig_NailedGroup_Object = MibScalar
uds3NetworkProfile_LineConfig_NailedGroup = _Uds3NetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 11),
    _Uds3NetworkProfile_LineConfig_NailedGroup_Type()
)
uds3NetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 12),
    _Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 13),
    _Uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_Uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_Uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _Uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 14),
    _Uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _Uds3NetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type uds3NetworkProfile_LineConfig_Activation based on Integer32"""
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


_Uds3NetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_Uds3NetworkProfile_LineConfig_Activation_Object = MibScalar
uds3NetworkProfile_LineConfig_Activation = _Uds3NetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 15),
    _Uds3NetworkProfile_LineConfig_Activation_Type()
)
uds3NetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _Uds3NetworkProfile_LineConfig_LineType_Type(Integer32):
    """Custom type uds3NetworkProfile_LineConfig_LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cBitParity", 1)
    )


_Uds3NetworkProfile_LineConfig_LineType_Type.__name__ = "Integer32"
_Uds3NetworkProfile_LineConfig_LineType_Object = MibScalar
uds3NetworkProfile_LineConfig_LineType = _Uds3NetworkProfile_LineConfig_LineType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 19),
    _Uds3NetworkProfile_LineConfig_LineType_Type()
)
uds3NetworkProfile_LineConfig_LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_LineType.setStatus("mandatory")


class _Uds3NetworkProfile_LineConfig_LineCoding_Type(Integer32):
    """Custom type uds3NetworkProfile_LineConfig_LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("b3zs", 1)
    )


_Uds3NetworkProfile_LineConfig_LineCoding_Type.__name__ = "Integer32"
_Uds3NetworkProfile_LineConfig_LineCoding_Object = MibScalar
uds3NetworkProfile_LineConfig_LineCoding = _Uds3NetworkProfile_LineConfig_LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 20),
    _Uds3NetworkProfile_LineConfig_LineCoding_Type()
)
uds3NetworkProfile_LineConfig_LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_LineCoding.setStatus("mandatory")


class _Uds3NetworkProfile_LineConfig_Loopback_Type(Integer32):
    """Custom type uds3NetworkProfile_LineConfig_Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("facilityLoopback", 2),
          ("localLoopback", 3),
          ("noLoopback", 1))
    )


_Uds3NetworkProfile_LineConfig_Loopback_Type.__name__ = "Integer32"
_Uds3NetworkProfile_LineConfig_Loopback_Object = MibScalar
uds3NetworkProfile_LineConfig_Loopback = _Uds3NetworkProfile_LineConfig_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 21),
    _Uds3NetworkProfile_LineConfig_Loopback_Type()
)
uds3NetworkProfile_LineConfig_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_Loopback.setStatus("mandatory")


class _Uds3NetworkProfile_Action_o_Type(Integer32):
    """Custom type uds3NetworkProfile_Action_o based on Integer32"""
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


_Uds3NetworkProfile_Action_o_Type.__name__ = "Integer32"
_Uds3NetworkProfile_Action_o_Object = MibScalar
uds3NetworkProfile_Action_o = _Uds3NetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 22),
    _Uds3NetworkProfile_Action_o_Type()
)
uds3NetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_Action_o.setStatus("mandatory")


class _Uds3NetworkProfile_LineConfig_ClockSource_Type(Integer32):
    """Custom type uds3NetworkProfile_LineConfig_ClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("notEligible", 2))
    )


_Uds3NetworkProfile_LineConfig_ClockSource_Type.__name__ = "Integer32"
_Uds3NetworkProfile_LineConfig_ClockSource_Object = MibScalar
uds3NetworkProfile_LineConfig_ClockSource = _Uds3NetworkProfile_LineConfig_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 23),
    _Uds3NetworkProfile_LineConfig_ClockSource_Type()
)
uds3NetworkProfile_LineConfig_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_ClockSource.setStatus("mandatory")


class _Uds3NetworkProfile_LineConfig_ClockPriority_Type(Integer32):
    """Custom type uds3NetworkProfile_LineConfig_ClockPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("lowPriority", 4),
          ("middlePriority", 3))
    )


_Uds3NetworkProfile_LineConfig_ClockPriority_Type.__name__ = "Integer32"
_Uds3NetworkProfile_LineConfig_ClockPriority_Object = MibScalar
uds3NetworkProfile_LineConfig_ClockPriority = _Uds3NetworkProfile_LineConfig_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 24),
    _Uds3NetworkProfile_LineConfig_ClockPriority_Type()
)
uds3NetworkProfile_LineConfig_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_ClockPriority.setStatus("mandatory")


class _Uds3NetworkProfile_LineConfig_StatusChangeTrapEnable_Type(Integer32):
    """Custom type uds3NetworkProfile_LineConfig_StatusChangeTrapEnable based on Integer32"""
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


_Uds3NetworkProfile_LineConfig_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_Uds3NetworkProfile_LineConfig_StatusChangeTrapEnable_Object = MibScalar
uds3NetworkProfile_LineConfig_StatusChangeTrapEnable = _Uds3NetworkProfile_LineConfig_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 5, 1, 1, 25),
    _Uds3NetworkProfile_LineConfig_StatusChangeTrapEnable_Type()
)
uds3NetworkProfile_LineConfig_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds3NetworkProfile_LineConfig_StatusChangeTrapEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBUDS3NET-MIB",
    **{"DisplayString": DisplayString,
       "mibuds3NetworkProfile": mibuds3NetworkProfile,
       "mibuds3NetworkProfileTable": mibuds3NetworkProfileTable,
       "mibuds3NetworkProfileEntry": mibuds3NetworkProfileEntry,
       "uds3NetworkProfile-Shelf-o": uds3NetworkProfile_Shelf_o,
       "uds3NetworkProfile-Slot-o": uds3NetworkProfile_Slot_o,
       "uds3NetworkProfile-Item-o": uds3NetworkProfile_Item_o,
       "uds3NetworkProfile-Name": uds3NetworkProfile_Name,
       "uds3NetworkProfile-PhysicalAddress-Shelf": uds3NetworkProfile_PhysicalAddress_Shelf,
       "uds3NetworkProfile-PhysicalAddress-Slot": uds3NetworkProfile_PhysicalAddress_Slot,
       "uds3NetworkProfile-PhysicalAddress-ItemNumber": uds3NetworkProfile_PhysicalAddress_ItemNumber,
       "uds3NetworkProfile-Enabled": uds3NetworkProfile_Enabled,
       "uds3NetworkProfile-ProfileNumber": uds3NetworkProfile_ProfileNumber,
       "uds3NetworkProfile-LineConfig-TrunkGroup": uds3NetworkProfile_LineConfig_TrunkGroup,
       "uds3NetworkProfile-LineConfig-NailedGroup": uds3NetworkProfile_LineConfig_NailedGroup,
       "uds3NetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "uds3NetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": uds3NetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "uds3NetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": uds3NetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "uds3NetworkProfile-LineConfig-Activation": uds3NetworkProfile_LineConfig_Activation,
       "uds3NetworkProfile-LineConfig-LineType": uds3NetworkProfile_LineConfig_LineType,
       "uds3NetworkProfile-LineConfig-LineCoding": uds3NetworkProfile_LineConfig_LineCoding,
       "uds3NetworkProfile-LineConfig-Loopback": uds3NetworkProfile_LineConfig_Loopback,
       "uds3NetworkProfile-Action-o": uds3NetworkProfile_Action_o,
       "uds3NetworkProfile-LineConfig-ClockSource": uds3NetworkProfile_LineConfig_ClockSource,
       "uds3NetworkProfile-LineConfig-ClockPriority": uds3NetworkProfile_LineConfig_ClockPriority,
       "uds3NetworkProfile-LineConfig-StatusChangeTrapEnable": uds3NetworkProfile_LineConfig_StatusChangeTrapEnable}
)
