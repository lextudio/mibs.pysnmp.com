# SNMP MIB module (ASCEND-MIBCMMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCMMODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:22 2024
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

_MibmodemProfile_ObjectIdentity = ObjectIdentity
mibmodemProfile = _MibmodemProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 144)
)
_MibmodemProfileTable_Object = MibTable
mibmodemProfileTable = _MibmodemProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1)
)
if mibBuilder.loadTexts:
    mibmodemProfileTable.setStatus("mandatory")
_MibmodemProfileEntry_Object = MibTableRow
mibmodemProfileEntry = _MibmodemProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1)
)
mibmodemProfileEntry.setIndexNames(
    (0, "ASCEND-MIBCMMODEM-MIB", "modemProfile-Shelf-o"),
    (0, "ASCEND-MIBCMMODEM-MIB", "modemProfile-Slot-o"),
    (0, "ASCEND-MIBCMMODEM-MIB", "modemProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibmodemProfileEntry.setStatus("mandatory")
_ModemProfile_Shelf_o_Type = Integer32
_ModemProfile_Shelf_o_Object = MibScalar
modemProfile_Shelf_o = _ModemProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 1),
    _ModemProfile_Shelf_o_Type()
)
modemProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProfile_Shelf_o.setStatus("mandatory")
_ModemProfile_Slot_o_Type = Integer32
_ModemProfile_Slot_o_Object = MibScalar
modemProfile_Slot_o = _ModemProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 2),
    _ModemProfile_Slot_o_Type()
)
modemProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProfile_Slot_o.setStatus("mandatory")
_ModemProfile_Item_o_Type = Integer32
_ModemProfile_Item_o_Object = MibScalar
modemProfile_Item_o = _ModemProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 3),
    _ModemProfile_Item_o_Type()
)
modemProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemProfile_Item_o.setStatus("mandatory")


class _ModemProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type modemProfile_PhysicalAddress_Shelf based on Integer32"""
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


_ModemProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_ModemProfile_PhysicalAddress_Shelf_Object = MibScalar
modemProfile_PhysicalAddress_Shelf = _ModemProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 4),
    _ModemProfile_PhysicalAddress_Shelf_Type()
)
modemProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _ModemProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type modemProfile_PhysicalAddress_Slot based on Integer32"""
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


_ModemProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_ModemProfile_PhysicalAddress_Slot_Object = MibScalar
modemProfile_PhysicalAddress_Slot = _ModemProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 5),
    _ModemProfile_PhysicalAddress_Slot_Type()
)
modemProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProfile_PhysicalAddress_Slot.setStatus("mandatory")
_ModemProfile_PhysicalAddress_ItemNumber_Type = Integer32
_ModemProfile_PhysicalAddress_ItemNumber_Object = MibScalar
modemProfile_PhysicalAddress_ItemNumber = _ModemProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 6),
    _ModemProfile_PhysicalAddress_ItemNumber_Type()
)
modemProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _ModemProfile_AutoAnswer_Type(Integer32):
    """Custom type modemProfile_AutoAnswer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("primaryOnly", 3))
    )


_ModemProfile_AutoAnswer_Type.__name__ = "Integer32"
_ModemProfile_AutoAnswer_Object = MibScalar
modemProfile_AutoAnswer = _ModemProfile_AutoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 7),
    _ModemProfile_AutoAnswer_Type()
)
modemProfile_AutoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProfile_AutoAnswer.setStatus("mandatory")


class _ModemProfile_Action_o_Type(Integer32):
    """Custom type modemProfile_Action_o based on Integer32"""
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


_ModemProfile_Action_o_Type.__name__ = "Integer32"
_ModemProfile_Action_o_Object = MibScalar
modemProfile_Action_o = _ModemProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 8),
    _ModemProfile_Action_o_Type()
)
modemProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProfile_Action_o.setStatus("mandatory")


class _ModemProfile_CountryCode_Type(Integer32):
    """Custom type modemProfile_CountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              11,
              16,
              23,
              28,
              33,
              39,
              47,
              50,
              61,
              62,
              67,
              71,
              81,
              82,
              84,
              88,
              89,
              90,
              98,
              106,
              109,
              116,
              124,
              127,
              131,
              138,
              139,
              140,
              157,
              160,
              161,
              166,
              167,
              181,
              182,
              185,
              255)
        )
    )
    namedValues = NamedValues(
        *(("australia", 10),
          ("austria", 11),
          ("belgium", 16),
          ("brazil", 23),
          ("bulgaria", 28),
          ("canada", 33),
          ("china", 39),
          ("czechslovak", 47),
          ("denmark", 50),
          ("finland", 61),
          ("france", 62),
          ("germany", 67),
          ("greece", 71),
          ("hongkong", 81),
          ("hungary", 82),
          ("india", 84),
          ("ireland", 88),
          ("israel", 89),
          ("italy", 90),
          ("japan", 1),
          ("korea", 98),
          ("luxembourg", 106),
          ("malaysia", 109),
          ("mexico", 116),
          ("netherlands", 124),
          ("newzealand", 127),
          ("norway", 131),
          ("philippines", 138),
          ("poland", 139),
          ("portugal", 140),
          ("russia", 185),
          ("singapore", 157),
          ("southafrica", 160),
          ("spain", 161),
          ("sweden", 166),
          ("switzerland", 167),
          ("taiwan", 255),
          ("unitedkingdom", 181),
          ("unitedstates", 182))
    )


_ModemProfile_CountryCode_Type.__name__ = "Integer32"
_ModemProfile_CountryCode_Object = MibScalar
modemProfile_CountryCode = _ModemProfile_CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 144, 1, 1, 9),
    _ModemProfile_CountryCode_Type()
)
modemProfile_CountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemProfile_CountryCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCMMODEM-MIB",
    **{"DisplayString": DisplayString,
       "mibmodemProfile": mibmodemProfile,
       "mibmodemProfileTable": mibmodemProfileTable,
       "mibmodemProfileEntry": mibmodemProfileEntry,
       "modemProfile-Shelf-o": modemProfile_Shelf_o,
       "modemProfile-Slot-o": modemProfile_Slot_o,
       "modemProfile-Item-o": modemProfile_Item_o,
       "modemProfile-PhysicalAddress-Shelf": modemProfile_PhysicalAddress_Shelf,
       "modemProfile-PhysicalAddress-Slot": modemProfile_PhysicalAddress_Slot,
       "modemProfile-PhysicalAddress-ItemNumber": modemProfile_PhysicalAddress_ItemNumber,
       "modemProfile-AutoAnswer": modemProfile_AutoAnswer,
       "modemProfile-Action-o": modemProfile_Action_o,
       "modemProfile-CountryCode": modemProfile_CountryCode}
)
