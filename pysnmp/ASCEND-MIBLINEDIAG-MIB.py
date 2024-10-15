# SNMP MIB module (ASCEND-MIBLINEDIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBLINEDIAG-MIB
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

_MibmibProfLineDiag_ObjectIdentity = ObjectIdentity
mibmibProfLineDiag = _MibmibProfLineDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 145)
)
_MibmibProfLineDiagTable_Object = MibTable
mibmibProfLineDiagTable = _MibmibProfLineDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1)
)
if mibBuilder.loadTexts:
    mibmibProfLineDiagTable.setStatus("mandatory")
_MibmibProfLineDiagEntry_Object = MibTableRow
mibmibProfLineDiagEntry = _MibmibProfLineDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1)
)
mibmibProfLineDiagEntry.setIndexNames(
    (0, "ASCEND-MIBLINEDIAG-MIB", "mibProfLineDiag-Shelf-o"),
    (0, "ASCEND-MIBLINEDIAG-MIB", "mibProfLineDiag-Slot-o"),
    (0, "ASCEND-MIBLINEDIAG-MIB", "mibProfLineDiag-Item-o"),
)
if mibBuilder.loadTexts:
    mibmibProfLineDiagEntry.setStatus("mandatory")
_MibProfLineDiag_Shelf_o_Type = Integer32
_MibProfLineDiag_Shelf_o_Object = MibScalar
mibProfLineDiag_Shelf_o = _MibProfLineDiag_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 1),
    _MibProfLineDiag_Shelf_o_Type()
)
mibProfLineDiag_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiag_Shelf_o.setStatus("mandatory")
_MibProfLineDiag_Slot_o_Type = Integer32
_MibProfLineDiag_Slot_o_Object = MibScalar
mibProfLineDiag_Slot_o = _MibProfLineDiag_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 2),
    _MibProfLineDiag_Slot_o_Type()
)
mibProfLineDiag_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiag_Slot_o.setStatus("mandatory")
_MibProfLineDiag_Item_o_Type = Integer32
_MibProfLineDiag_Item_o_Object = MibScalar
mibProfLineDiag_Item_o = _MibProfLineDiag_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 3),
    _MibProfLineDiag_Item_o_Type()
)
mibProfLineDiag_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfLineDiag_Item_o.setStatus("mandatory")


class _MibProfLineDiag_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type mibProfLineDiag_PhysicalAddress_Shelf based on Integer32"""
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


_MibProfLineDiag_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_MibProfLineDiag_PhysicalAddress_Shelf_Object = MibScalar
mibProfLineDiag_PhysicalAddress_Shelf = _MibProfLineDiag_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 4),
    _MibProfLineDiag_PhysicalAddress_Shelf_Type()
)
mibProfLineDiag_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_PhysicalAddress_Shelf.setStatus("mandatory")


class _MibProfLineDiag_PhysicalAddress_Slot_Type(Integer32):
    """Custom type mibProfLineDiag_PhysicalAddress_Slot based on Integer32"""
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


_MibProfLineDiag_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_MibProfLineDiag_PhysicalAddress_Slot_Object = MibScalar
mibProfLineDiag_PhysicalAddress_Slot = _MibProfLineDiag_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 5),
    _MibProfLineDiag_PhysicalAddress_Slot_Type()
)
mibProfLineDiag_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_PhysicalAddress_Slot.setStatus("mandatory")
_MibProfLineDiag_PhysicalAddress_ItemNumber_Type = Integer32
_MibProfLineDiag_PhysicalAddress_ItemNumber_Object = MibScalar
mibProfLineDiag_PhysicalAddress_ItemNumber = _MibProfLineDiag_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 6),
    _MibProfLineDiag_PhysicalAddress_ItemNumber_Type()
)
mibProfLineDiag_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _MibProfLineDiag_BertTimer_Type(Integer32):
    """Custom type mibProfLineDiag_BertTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(60001,
              120001,
              180001,
              240001,
              300001,
              600001,
              900001,
              1200001,
              1800001)
        )
    )
    namedValues = NamedValues(
        *(("n-10Minutes", 600001),
          ("n-15Minutes", 900001),
          ("n-1Minute", 60001),
          ("n-20Minutes", 1200001),
          ("n-2Minutes", 120001),
          ("n-30Minutes", 1800001),
          ("n-3Minutes", 180001),
          ("n-4Minutes", 240001),
          ("n-5Minutes", 300001))
    )


_MibProfLineDiag_BertTimer_Type.__name__ = "Integer32"
_MibProfLineDiag_BertTimer_Object = MibScalar
mibProfLineDiag_BertTimer = _MibProfLineDiag_BertTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 7),
    _MibProfLineDiag_BertTimer_Type()
)
mibProfLineDiag_BertTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_BertTimer.setStatus("mandatory")


class _MibProfLineDiag_BertEnable_Type(Integer32):
    """Custom type mibProfLineDiag_BertEnable based on Integer32"""
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


_MibProfLineDiag_BertEnable_Type.__name__ = "Integer32"
_MibProfLineDiag_BertEnable_Object = MibScalar
mibProfLineDiag_BertEnable = _MibProfLineDiag_BertEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 8),
    _MibProfLineDiag_BertEnable_Type()
)
mibProfLineDiag_BertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_BertEnable.setStatus("mandatory")


class _MibProfLineDiag_IdtEnable_Type(Integer32):
    """Custom type mibProfLineDiag_IdtEnable based on Integer32"""
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


_MibProfLineDiag_IdtEnable_Type.__name__ = "Integer32"
_MibProfLineDiag_IdtEnable_Object = MibScalar
mibProfLineDiag_IdtEnable = _MibProfLineDiag_IdtEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 9),
    _MibProfLineDiag_IdtEnable_Type()
)
mibProfLineDiag_IdtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_IdtEnable.setStatus("mandatory")
_MibProfLineDiag_IdtNumOfMsg_Type = Integer32
_MibProfLineDiag_IdtNumOfMsg_Object = MibScalar
mibProfLineDiag_IdtNumOfMsg = _MibProfLineDiag_IdtNumOfMsg_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 10),
    _MibProfLineDiag_IdtNumOfMsg_Type()
)
mibProfLineDiag_IdtNumOfMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_IdtNumOfMsg.setStatus("mandatory")


class _MibProfLineDiag_Action_o_Type(Integer32):
    """Custom type mibProfLineDiag_Action_o based on Integer32"""
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


_MibProfLineDiag_Action_o_Type.__name__ = "Integer32"
_MibProfLineDiag_Action_o_Object = MibScalar
mibProfLineDiag_Action_o = _MibProfLineDiag_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 145, 1, 1, 11),
    _MibProfLineDiag_Action_o_Type()
)
mibProfLineDiag_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfLineDiag_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBLINEDIAG-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfLineDiag": mibmibProfLineDiag,
       "mibmibProfLineDiagTable": mibmibProfLineDiagTable,
       "mibmibProfLineDiagEntry": mibmibProfLineDiagEntry,
       "mibProfLineDiag-Shelf-o": mibProfLineDiag_Shelf_o,
       "mibProfLineDiag-Slot-o": mibProfLineDiag_Slot_o,
       "mibProfLineDiag-Item-o": mibProfLineDiag_Item_o,
       "mibProfLineDiag-PhysicalAddress-Shelf": mibProfLineDiag_PhysicalAddress_Shelf,
       "mibProfLineDiag-PhysicalAddress-Slot": mibProfLineDiag_PhysicalAddress_Slot,
       "mibProfLineDiag-PhysicalAddress-ItemNumber": mibProfLineDiag_PhysicalAddress_ItemNumber,
       "mibProfLineDiag-BertTimer": mibProfLineDiag_BertTimer,
       "mibProfLineDiag-BertEnable": mibProfLineDiag_BertEnable,
       "mibProfLineDiag-IdtEnable": mibProfLineDiag_IdtEnable,
       "mibProfLineDiag-IdtNumOfMsg": mibProfLineDiag_IdtNumOfMsg,
       "mibProfLineDiag-Action-o": mibProfLineDiag_Action_o}
)
