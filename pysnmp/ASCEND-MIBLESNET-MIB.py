# SNMP MIB module (ASCEND-MIBLESNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBLESNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:50 2024
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

_MiblesNetworkProfile_ObjectIdentity = ObjectIdentity
miblesNetworkProfile = _MiblesNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 178)
)
_MiblesNetworkProfileTable_Object = MibTable
miblesNetworkProfileTable = _MiblesNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1)
)
if mibBuilder.loadTexts:
    miblesNetworkProfileTable.setStatus("mandatory")
_MiblesNetworkProfileEntry_Object = MibTableRow
miblesNetworkProfileEntry = _MiblesNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1)
)
miblesNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    miblesNetworkProfileEntry.setStatus("mandatory")
_LesNetworkProfile_Shelf_o_Type = Integer32
_LesNetworkProfile_Shelf_o_Object = MibScalar
lesNetworkProfile_Shelf_o = _LesNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 1),
    _LesNetworkProfile_Shelf_o_Type()
)
lesNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesNetworkProfile_Shelf_o.setStatus("mandatory")
_LesNetworkProfile_Slot_o_Type = Integer32
_LesNetworkProfile_Slot_o_Object = MibScalar
lesNetworkProfile_Slot_o = _LesNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 2),
    _LesNetworkProfile_Slot_o_Type()
)
lesNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesNetworkProfile_Slot_o.setStatus("mandatory")
_LesNetworkProfile_Item_o_Type = Integer32
_LesNetworkProfile_Item_o_Object = MibScalar
lesNetworkProfile_Item_o = _LesNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 3),
    _LesNetworkProfile_Item_o_Type()
)
lesNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesNetworkProfile_Item_o.setStatus("mandatory")
_LesNetworkProfile_Name_Type = DisplayString
_LesNetworkProfile_Name_Object = MibScalar
lesNetworkProfile_Name = _LesNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 4),
    _LesNetworkProfile_Name_Type()
)
lesNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_Name.setStatus("mandatory")


class _LesNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type lesNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_LesNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_LesNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
lesNetworkProfile_PhysicalAddress_Shelf = _LesNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 5),
    _LesNetworkProfile_PhysicalAddress_Shelf_Type()
)
lesNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _LesNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type lesNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_LesNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_LesNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
lesNetworkProfile_PhysicalAddress_Slot = _LesNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 6),
    _LesNetworkProfile_PhysicalAddress_Slot_Type()
)
lesNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_LesNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_LesNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
lesNetworkProfile_PhysicalAddress_ItemNumber = _LesNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 7),
    _LesNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
lesNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _LesNetworkProfile_Enabled_Type(Integer32):
    """Custom type lesNetworkProfile_Enabled based on Integer32"""
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


_LesNetworkProfile_Enabled_Type.__name__ = "Integer32"
_LesNetworkProfile_Enabled_Object = MibScalar
lesNetworkProfile_Enabled = _LesNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 8),
    _LesNetworkProfile_Enabled_Type()
)
lesNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_Enabled.setStatus("mandatory")
_LesNetworkProfile_NailedGroup_Type = Integer32
_LesNetworkProfile_NailedGroup_Object = MibScalar
lesNetworkProfile_NailedGroup = _LesNetworkProfile_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 9),
    _LesNetworkProfile_NailedGroup_Type()
)
lesNetworkProfile_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_NailedGroup.setStatus("mandatory")


class _LesNetworkProfile_Action_o_Type(Integer32):
    """Custom type lesNetworkProfile_Action_o based on Integer32"""
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


_LesNetworkProfile_Action_o_Type.__name__ = "Integer32"
_LesNetworkProfile_Action_o_Object = MibScalar
lesNetworkProfile_Action_o = _LesNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 1, 1, 10),
    _LesNetworkProfile_Action_o_Type()
)
lesNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_Action_o.setStatus("mandatory")
_MiblesNetworkProfile_PotsLineConfigTable_Object = MibTable
miblesNetworkProfile_PotsLineConfigTable = _MiblesNetworkProfile_PotsLineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2)
)
if mibBuilder.loadTexts:
    miblesNetworkProfile_PotsLineConfigTable.setStatus("mandatory")
_MiblesNetworkProfile_PotsLineConfigEntry_Object = MibTableRow
miblesNetworkProfile_PotsLineConfigEntry = _MiblesNetworkProfile_PotsLineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1)
)
miblesNetworkProfile_PotsLineConfigEntry.setIndexNames(
    (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Shelf-o"),
    (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Slot-o"),
    (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Item-o"),
    (0, "ASCEND-MIBLESNET-MIB", "lesNetworkProfile-PotsLineConfig-Index-o"),
)
if mibBuilder.loadTexts:
    miblesNetworkProfile_PotsLineConfigEntry.setStatus("mandatory")
_LesNetworkProfile_PotsLineConfig_Shelf_o_Type = Integer32
_LesNetworkProfile_PotsLineConfig_Shelf_o_Object = MibScalar
lesNetworkProfile_PotsLineConfig_Shelf_o = _LesNetworkProfile_PotsLineConfig_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 1),
    _LesNetworkProfile_PotsLineConfig_Shelf_o_Type()
)
lesNetworkProfile_PotsLineConfig_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_Shelf_o.setStatus("mandatory")
_LesNetworkProfile_PotsLineConfig_Slot_o_Type = Integer32
_LesNetworkProfile_PotsLineConfig_Slot_o_Object = MibScalar
lesNetworkProfile_PotsLineConfig_Slot_o = _LesNetworkProfile_PotsLineConfig_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 2),
    _LesNetworkProfile_PotsLineConfig_Slot_o_Type()
)
lesNetworkProfile_PotsLineConfig_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_Slot_o.setStatus("mandatory")
_LesNetworkProfile_PotsLineConfig_Item_o_Type = Integer32
_LesNetworkProfile_PotsLineConfig_Item_o_Object = MibScalar
lesNetworkProfile_PotsLineConfig_Item_o = _LesNetworkProfile_PotsLineConfig_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 3),
    _LesNetworkProfile_PotsLineConfig_Item_o_Type()
)
lesNetworkProfile_PotsLineConfig_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_Item_o.setStatus("mandatory")
_LesNetworkProfile_PotsLineConfig_Index_o_Type = Integer32
_LesNetworkProfile_PotsLineConfig_Index_o_Object = MibScalar
lesNetworkProfile_PotsLineConfig_Index_o = _LesNetworkProfile_PotsLineConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 4),
    _LesNetworkProfile_PotsLineConfig_Index_o_Type()
)
lesNetworkProfile_PotsLineConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_Index_o.setStatus("mandatory")


class _LesNetworkProfile_PotsLineConfig_Enabled_Type(Integer32):
    """Custom type lesNetworkProfile_PotsLineConfig_Enabled based on Integer32"""
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


_LesNetworkProfile_PotsLineConfig_Enabled_Type.__name__ = "Integer32"
_LesNetworkProfile_PotsLineConfig_Enabled_Object = MibScalar
lesNetworkProfile_PotsLineConfig_Enabled = _LesNetworkProfile_PotsLineConfig_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 5),
    _LesNetworkProfile_PotsLineConfig_Enabled_Type()
)
lesNetworkProfile_PotsLineConfig_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_Enabled.setStatus("mandatory")


class _LesNetworkProfile_PotsLineConfig_Mode_Type(Integer32):
    """Custom type lesNetworkProfile_PotsLineConfig_Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groundStart", 1),
          ("loopStart", 2))
    )


_LesNetworkProfile_PotsLineConfig_Mode_Type.__name__ = "Integer32"
_LesNetworkProfile_PotsLineConfig_Mode_Object = MibScalar
lesNetworkProfile_PotsLineConfig_Mode = _LesNetworkProfile_PotsLineConfig_Mode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 6),
    _LesNetworkProfile_PotsLineConfig_Mode_Type()
)
lesNetworkProfile_PotsLineConfig_Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_Mode.setStatus("mandatory")
_LesNetworkProfile_PotsLineConfig_EncodingFormatProfile_Type = Integer32
_LesNetworkProfile_PotsLineConfig_EncodingFormatProfile_Object = MibScalar
lesNetworkProfile_PotsLineConfig_EncodingFormatProfile = _LesNetworkProfile_PotsLineConfig_EncodingFormatProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 7),
    _LesNetworkProfile_PotsLineConfig_EncodingFormatProfile_Type()
)
lesNetworkProfile_PotsLineConfig_EncodingFormatProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_EncodingFormatProfile.setStatus("mandatory")


class _LesNetworkProfile_PotsLineConfig_FwdDisc_Type(Integer32):
    """Custom type lesNetworkProfile_PotsLineConfig_FwdDisc based on Integer32"""
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


_LesNetworkProfile_PotsLineConfig_FwdDisc_Type.__name__ = "Integer32"
_LesNetworkProfile_PotsLineConfig_FwdDisc_Object = MibScalar
lesNetworkProfile_PotsLineConfig_FwdDisc = _LesNetworkProfile_PotsLineConfig_FwdDisc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 8),
    _LesNetworkProfile_PotsLineConfig_FwdDisc_Type()
)
lesNetworkProfile_PotsLineConfig_FwdDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_FwdDisc.setStatus("mandatory")
_LesNetworkProfile_PotsLineConfig_OverRideCid_Type = Integer32
_LesNetworkProfile_PotsLineConfig_OverRideCid_Object = MibScalar
lesNetworkProfile_PotsLineConfig_OverRideCid = _LesNetworkProfile_PotsLineConfig_OverRideCid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 178, 2, 1, 9),
    _LesNetworkProfile_PotsLineConfig_OverRideCid_Type()
)
lesNetworkProfile_PotsLineConfig_OverRideCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lesNetworkProfile_PotsLineConfig_OverRideCid.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBLESNET-MIB",
    **{"DisplayString": DisplayString,
       "miblesNetworkProfile": miblesNetworkProfile,
       "miblesNetworkProfileTable": miblesNetworkProfileTable,
       "miblesNetworkProfileEntry": miblesNetworkProfileEntry,
       "lesNetworkProfile-Shelf-o": lesNetworkProfile_Shelf_o,
       "lesNetworkProfile-Slot-o": lesNetworkProfile_Slot_o,
       "lesNetworkProfile-Item-o": lesNetworkProfile_Item_o,
       "lesNetworkProfile-Name": lesNetworkProfile_Name,
       "lesNetworkProfile-PhysicalAddress-Shelf": lesNetworkProfile_PhysicalAddress_Shelf,
       "lesNetworkProfile-PhysicalAddress-Slot": lesNetworkProfile_PhysicalAddress_Slot,
       "lesNetworkProfile-PhysicalAddress-ItemNumber": lesNetworkProfile_PhysicalAddress_ItemNumber,
       "lesNetworkProfile-Enabled": lesNetworkProfile_Enabled,
       "lesNetworkProfile-NailedGroup": lesNetworkProfile_NailedGroup,
       "lesNetworkProfile-Action-o": lesNetworkProfile_Action_o,
       "miblesNetworkProfile-PotsLineConfigTable": miblesNetworkProfile_PotsLineConfigTable,
       "miblesNetworkProfile-PotsLineConfigEntry": miblesNetworkProfile_PotsLineConfigEntry,
       "lesNetworkProfile-PotsLineConfig-Shelf-o": lesNetworkProfile_PotsLineConfig_Shelf_o,
       "lesNetworkProfile-PotsLineConfig-Slot-o": lesNetworkProfile_PotsLineConfig_Slot_o,
       "lesNetworkProfile-PotsLineConfig-Item-o": lesNetworkProfile_PotsLineConfig_Item_o,
       "lesNetworkProfile-PotsLineConfig-Index-o": lesNetworkProfile_PotsLineConfig_Index_o,
       "lesNetworkProfile-PotsLineConfig-Enabled": lesNetworkProfile_PotsLineConfig_Enabled,
       "lesNetworkProfile-PotsLineConfig-Mode": lesNetworkProfile_PotsLineConfig_Mode,
       "lesNetworkProfile-PotsLineConfig-EncodingFormatProfile": lesNetworkProfile_PotsLineConfig_EncodingFormatProfile,
       "lesNetworkProfile-PotsLineConfig-FwdDisc": lesNetworkProfile_PotsLineConfig_FwdDisc,
       "lesNetworkProfile-PotsLineConfig-OverRideCid": lesNetworkProfile_PotsLineConfig_OverRideCid}
)
