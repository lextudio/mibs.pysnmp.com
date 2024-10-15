# SNMP MIB module (ASCEND-MIBCONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:23 2024
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

_MibserialInterfaceProfile_ObjectIdentity = ObjectIdentity
mibserialInterfaceProfile = _MibserialInterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 69)
)
_MibserialInterfaceProfileTable_Object = MibTable
mibserialInterfaceProfileTable = _MibserialInterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1)
)
if mibBuilder.loadTexts:
    mibserialInterfaceProfileTable.setStatus("mandatory")
_MibserialInterfaceProfileEntry_Object = MibTableRow
mibserialInterfaceProfileEntry = _MibserialInterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1)
)
mibserialInterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBCONS-MIB", "serialInterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBCONS-MIB", "serialInterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBCONS-MIB", "serialInterfaceProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibserialInterfaceProfileEntry.setStatus("mandatory")
_SerialInterfaceProfile_Shelf_o_Type = Integer32
_SerialInterfaceProfile_Shelf_o_Object = MibScalar
serialInterfaceProfile_Shelf_o = _SerialInterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 1),
    _SerialInterfaceProfile_Shelf_o_Type()
)
serialInterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialInterfaceProfile_Shelf_o.setStatus("mandatory")
_SerialInterfaceProfile_Slot_o_Type = Integer32
_SerialInterfaceProfile_Slot_o_Object = MibScalar
serialInterfaceProfile_Slot_o = _SerialInterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 2),
    _SerialInterfaceProfile_Slot_o_Type()
)
serialInterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialInterfaceProfile_Slot_o.setStatus("mandatory")
_SerialInterfaceProfile_Item_o_Type = Integer32
_SerialInterfaceProfile_Item_o_Object = MibScalar
serialInterfaceProfile_Item_o = _SerialInterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 3),
    _SerialInterfaceProfile_Item_o_Type()
)
serialInterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialInterfaceProfile_Item_o.setStatus("mandatory")


class _SerialInterfaceProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type serialInterfaceProfile_PhysicalAddress_Shelf based on Integer32"""
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


_SerialInterfaceProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_SerialInterfaceProfile_PhysicalAddress_Shelf_Object = MibScalar
serialInterfaceProfile_PhysicalAddress_Shelf = _SerialInterfaceProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 4),
    _SerialInterfaceProfile_PhysicalAddress_Shelf_Type()
)
serialInterfaceProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _SerialInterfaceProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type serialInterfaceProfile_PhysicalAddress_Slot based on Integer32"""
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


_SerialInterfaceProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_SerialInterfaceProfile_PhysicalAddress_Slot_Object = MibScalar
serialInterfaceProfile_PhysicalAddress_Slot = _SerialInterfaceProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 5),
    _SerialInterfaceProfile_PhysicalAddress_Slot_Type()
)
serialInterfaceProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_PhysicalAddress_Slot.setStatus("mandatory")
_SerialInterfaceProfile_PhysicalAddress_ItemNumber_Type = Integer32
_SerialInterfaceProfile_PhysicalAddress_ItemNumber_Object = MibScalar
serialInterfaceProfile_PhysicalAddress_ItemNumber = _SerialInterfaceProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 6),
    _SerialInterfaceProfile_PhysicalAddress_ItemNumber_Type()
)
serialInterfaceProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _SerialInterfaceProfile_TermRate_Type(Integer32):
    """Custom type serialInterfaceProfile_TermRate based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("n-115200Bps", 9),
          ("n-1200Bps", 2),
          ("n-19200Bps", 6),
          ("n-2400Bps", 3),
          ("n-300Bps", 1),
          ("n-38400Bps", 7),
          ("n-4800Bps", 4),
          ("n-57600Bps", 8),
          ("n-9600Bps", 5))
    )


_SerialInterfaceProfile_TermRate_Type.__name__ = "Integer32"
_SerialInterfaceProfile_TermRate_Object = MibScalar
serialInterfaceProfile_TermRate = _SerialInterfaceProfile_TermRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 7),
    _SerialInterfaceProfile_TermRate_Type()
)
serialInterfaceProfile_TermRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_TermRate.setStatus("mandatory")


class _SerialInterfaceProfile_FlowControl_Type(Integer32):
    """Custom type serialInterfaceProfile_FlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardwareHandshake", 3),
          ("none", 1),
          ("xonXoff", 2))
    )


_SerialInterfaceProfile_FlowControl_Type.__name__ = "Integer32"
_SerialInterfaceProfile_FlowControl_Object = MibScalar
serialInterfaceProfile_FlowControl = _SerialInterfaceProfile_FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 8),
    _SerialInterfaceProfile_FlowControl_Type()
)
serialInterfaceProfile_FlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_FlowControl.setStatus("mandatory")
_SerialInterfaceProfile_UserProfile_Type = DisplayString
_SerialInterfaceProfile_UserProfile_Object = MibScalar
serialInterfaceProfile_UserProfile = _SerialInterfaceProfile_UserProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 9),
    _SerialInterfaceProfile_UserProfile_Type()
)
serialInterfaceProfile_UserProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_UserProfile.setStatus("mandatory")


class _SerialInterfaceProfile_AutoLogout_Type(Integer32):
    """Custom type serialInterfaceProfile_AutoLogout based on Integer32"""
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


_SerialInterfaceProfile_AutoLogout_Type.__name__ = "Integer32"
_SerialInterfaceProfile_AutoLogout_Object = MibScalar
serialInterfaceProfile_AutoLogout = _SerialInterfaceProfile_AutoLogout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 10),
    _SerialInterfaceProfile_AutoLogout_Type()
)
serialInterfaceProfile_AutoLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_AutoLogout.setStatus("mandatory")


class _SerialInterfaceProfile_Action_o_Type(Integer32):
    """Custom type serialInterfaceProfile_Action_o based on Integer32"""
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


_SerialInterfaceProfile_Action_o_Type.__name__ = "Integer32"
_SerialInterfaceProfile_Action_o_Object = MibScalar
serialInterfaceProfile_Action_o = _SerialInterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 11),
    _SerialInterfaceProfile_Action_o_Type()
)
serialInterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_Action_o.setStatus("mandatory")


class _SerialInterfaceProfile_ConsoleMode_Type(Integer32):
    """Custom type serialInterfaceProfile_ConsoleMode based on Integer32"""
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
          ("yCable", 3))
    )


_SerialInterfaceProfile_ConsoleMode_Type.__name__ = "Integer32"
_SerialInterfaceProfile_ConsoleMode_Object = MibScalar
serialInterfaceProfile_ConsoleMode = _SerialInterfaceProfile_ConsoleMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 69, 1, 1, 12),
    _SerialInterfaceProfile_ConsoleMode_Type()
)
serialInterfaceProfile_ConsoleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialInterfaceProfile_ConsoleMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCONS-MIB",
    **{"DisplayString": DisplayString,
       "mibserialInterfaceProfile": mibserialInterfaceProfile,
       "mibserialInterfaceProfileTable": mibserialInterfaceProfileTable,
       "mibserialInterfaceProfileEntry": mibserialInterfaceProfileEntry,
       "serialInterfaceProfile-Shelf-o": serialInterfaceProfile_Shelf_o,
       "serialInterfaceProfile-Slot-o": serialInterfaceProfile_Slot_o,
       "serialInterfaceProfile-Item-o": serialInterfaceProfile_Item_o,
       "serialInterfaceProfile-PhysicalAddress-Shelf": serialInterfaceProfile_PhysicalAddress_Shelf,
       "serialInterfaceProfile-PhysicalAddress-Slot": serialInterfaceProfile_PhysicalAddress_Slot,
       "serialInterfaceProfile-PhysicalAddress-ItemNumber": serialInterfaceProfile_PhysicalAddress_ItemNumber,
       "serialInterfaceProfile-TermRate": serialInterfaceProfile_TermRate,
       "serialInterfaceProfile-FlowControl": serialInterfaceProfile_FlowControl,
       "serialInterfaceProfile-UserProfile": serialInterfaceProfile_UserProfile,
       "serialInterfaceProfile-AutoLogout": serialInterfaceProfile_AutoLogout,
       "serialInterfaceProfile-Action-o": serialInterfaceProfile_Action_o,
       "serialInterfaceProfile-ConsoleMode": serialInterfaceProfile_ConsoleMode}
)
