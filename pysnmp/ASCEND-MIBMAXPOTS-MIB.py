# SNMP MIB module (ASCEND-MIBMAXPOTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBMAXPOTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:54 2024
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

_MibmaxpotsProfile_ObjectIdentity = ObjectIdentity
mibmaxpotsProfile = _MibmaxpotsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 94)
)
_MibmaxpotsProfileTable_Object = MibTable
mibmaxpotsProfileTable = _MibmaxpotsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1)
)
if mibBuilder.loadTexts:
    mibmaxpotsProfileTable.setStatus("mandatory")
_MibmaxpotsProfileEntry_Object = MibTableRow
mibmaxpotsProfileEntry = _MibmaxpotsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1)
)
mibmaxpotsProfileEntry.setIndexNames(
    (0, "ASCEND-MIBMAXPOTS-MIB", "maxpotsProfile-Shelf-o"),
    (0, "ASCEND-MIBMAXPOTS-MIB", "maxpotsProfile-Slot-o"),
    (0, "ASCEND-MIBMAXPOTS-MIB", "maxpotsProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibmaxpotsProfileEntry.setStatus("mandatory")
_MaxpotsProfile_Shelf_o_Type = Integer32
_MaxpotsProfile_Shelf_o_Object = MibScalar
maxpotsProfile_Shelf_o = _MaxpotsProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 1),
    _MaxpotsProfile_Shelf_o_Type()
)
maxpotsProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxpotsProfile_Shelf_o.setStatus("mandatory")
_MaxpotsProfile_Slot_o_Type = Integer32
_MaxpotsProfile_Slot_o_Object = MibScalar
maxpotsProfile_Slot_o = _MaxpotsProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 2),
    _MaxpotsProfile_Slot_o_Type()
)
maxpotsProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxpotsProfile_Slot_o.setStatus("mandatory")
_MaxpotsProfile_Item_o_Type = Integer32
_MaxpotsProfile_Item_o_Object = MibScalar
maxpotsProfile_Item_o = _MaxpotsProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 3),
    _MaxpotsProfile_Item_o_Type()
)
maxpotsProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxpotsProfile_Item_o.setStatus("mandatory")
_MaxpotsProfile_ProfileNumber_Type = Integer32
_MaxpotsProfile_ProfileNumber_Object = MibScalar
maxpotsProfile_ProfileNumber = _MaxpotsProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 4),
    _MaxpotsProfile_ProfileNumber_Type()
)
maxpotsProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_ProfileNumber.setStatus("mandatory")
_MaxpotsProfile_Name_Type = DisplayString
_MaxpotsProfile_Name_Object = MibScalar
maxpotsProfile_Name = _MaxpotsProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 5),
    _MaxpotsProfile_Name_Type()
)
maxpotsProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_Name.setStatus("mandatory")


class _MaxpotsProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type maxpotsProfile_PhysicalAddress_Shelf based on Integer32"""
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


_MaxpotsProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_MaxpotsProfile_PhysicalAddress_Shelf_Object = MibScalar
maxpotsProfile_PhysicalAddress_Shelf = _MaxpotsProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 6),
    _MaxpotsProfile_PhysicalAddress_Shelf_Type()
)
maxpotsProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _MaxpotsProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type maxpotsProfile_PhysicalAddress_Slot based on Integer32"""
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


_MaxpotsProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_MaxpotsProfile_PhysicalAddress_Slot_Object = MibScalar
maxpotsProfile_PhysicalAddress_Slot = _MaxpotsProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 7),
    _MaxpotsProfile_PhysicalAddress_Slot_Type()
)
maxpotsProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_PhysicalAddress_Slot.setStatus("mandatory")
_MaxpotsProfile_PhysicalAddress_ItemNumber_Type = Integer32
_MaxpotsProfile_PhysicalAddress_ItemNumber_Object = MibScalar
maxpotsProfile_PhysicalAddress_ItemNumber = _MaxpotsProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 8),
    _MaxpotsProfile_PhysicalAddress_ItemNumber_Type()
)
maxpotsProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _MaxpotsProfile_Action_o_Type(Integer32):
    """Custom type maxpotsProfile_Action_o based on Integer32"""
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


_MaxpotsProfile_Action_o_Type.__name__ = "Integer32"
_MaxpotsProfile_Action_o_Object = MibScalar
maxpotsProfile_Action_o = _MaxpotsProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 1, 1, 9),
    _MaxpotsProfile_Action_o_Type()
)
maxpotsProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_Action_o.setStatus("mandatory")
_MibmaxpotsProfile_LineInterfaceTable_Object = MibTable
mibmaxpotsProfile_LineInterfaceTable = _MibmaxpotsProfile_LineInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2)
)
if mibBuilder.loadTexts:
    mibmaxpotsProfile_LineInterfaceTable.setStatus("mandatory")
_MibmaxpotsProfile_LineInterfaceEntry_Object = MibTableRow
mibmaxpotsProfile_LineInterfaceEntry = _MibmaxpotsProfile_LineInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1)
)
mibmaxpotsProfile_LineInterfaceEntry.setIndexNames(
    (0, "ASCEND-MIBMAXPOTS-MIB", "maxpotsProfile-LineInterface-Shelf-o"),
    (0, "ASCEND-MIBMAXPOTS-MIB", "maxpotsProfile-LineInterface-Slot-o"),
    (0, "ASCEND-MIBMAXPOTS-MIB", "maxpotsProfile-LineInterface-Item-o"),
    (0, "ASCEND-MIBMAXPOTS-MIB", "maxpotsProfile-LineInterface-Index-o"),
)
if mibBuilder.loadTexts:
    mibmaxpotsProfile_LineInterfaceEntry.setStatus("mandatory")
_MaxpotsProfile_LineInterface_Shelf_o_Type = Integer32
_MaxpotsProfile_LineInterface_Shelf_o_Object = MibScalar
maxpotsProfile_LineInterface_Shelf_o = _MaxpotsProfile_LineInterface_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 1),
    _MaxpotsProfile_LineInterface_Shelf_o_Type()
)
maxpotsProfile_LineInterface_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_Shelf_o.setStatus("mandatory")
_MaxpotsProfile_LineInterface_Slot_o_Type = Integer32
_MaxpotsProfile_LineInterface_Slot_o_Object = MibScalar
maxpotsProfile_LineInterface_Slot_o = _MaxpotsProfile_LineInterface_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 2),
    _MaxpotsProfile_LineInterface_Slot_o_Type()
)
maxpotsProfile_LineInterface_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_Slot_o.setStatus("mandatory")
_MaxpotsProfile_LineInterface_Item_o_Type = Integer32
_MaxpotsProfile_LineInterface_Item_o_Object = MibScalar
maxpotsProfile_LineInterface_Item_o = _MaxpotsProfile_LineInterface_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 3),
    _MaxpotsProfile_LineInterface_Item_o_Type()
)
maxpotsProfile_LineInterface_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_Item_o.setStatus("mandatory")
_MaxpotsProfile_LineInterface_Index_o_Type = Integer32
_MaxpotsProfile_LineInterface_Index_o_Object = MibScalar
maxpotsProfile_LineInterface_Index_o = _MaxpotsProfile_LineInterface_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 4),
    _MaxpotsProfile_LineInterface_Index_o_Type()
)
maxpotsProfile_LineInterface_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_Index_o.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_DialEnabled_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_DialEnabled based on Integer32"""
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


_MaxpotsProfile_LineInterface_DialEnabled_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_DialEnabled_Object = MibScalar
maxpotsProfile_LineInterface_DialEnabled = _MaxpotsProfile_LineInterface_DialEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 5),
    _MaxpotsProfile_LineInterface_DialEnabled_Type()
)
maxpotsProfile_LineInterface_DialEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_DialEnabled.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_NetClidEnabled_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_NetClidEnabled based on Integer32"""
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


_MaxpotsProfile_LineInterface_NetClidEnabled_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_NetClidEnabled_Object = MibScalar
maxpotsProfile_LineInterface_NetClidEnabled = _MaxpotsProfile_LineInterface_NetClidEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 6),
    _MaxpotsProfile_LineInterface_NetClidEnabled_Type()
)
maxpotsProfile_LineInterface_NetClidEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_NetClidEnabled.setStatus("mandatory")
_MaxpotsProfile_LineInterface_ClidNumber_Type = DisplayString
_MaxpotsProfile_LineInterface_ClidNumber_Object = MibScalar
maxpotsProfile_LineInterface_ClidNumber = _MaxpotsProfile_LineInterface_ClidNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 7),
    _MaxpotsProfile_LineInterface_ClidNumber_Type()
)
maxpotsProfile_LineInterface_ClidNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_ClidNumber.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_AnswerEnabled_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_AnswerEnabled based on Integer32"""
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


_MaxpotsProfile_LineInterface_AnswerEnabled_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_AnswerEnabled_Object = MibScalar
maxpotsProfile_LineInterface_AnswerEnabled = _MaxpotsProfile_LineInterface_AnswerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 8),
    _MaxpotsProfile_LineInterface_AnswerEnabled_Type()
)
maxpotsProfile_LineInterface_AnswerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_AnswerEnabled.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_CallerIdEnabled_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_CallerIdEnabled based on Integer32"""
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


_MaxpotsProfile_LineInterface_CallerIdEnabled_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_CallerIdEnabled_Object = MibScalar
maxpotsProfile_LineInterface_CallerIdEnabled = _MaxpotsProfile_LineInterface_CallerIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 9),
    _MaxpotsProfile_LineInterface_CallerIdEnabled_Type()
)
maxpotsProfile_LineInterface_CallerIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_CallerIdEnabled.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_FwdDiscEnabled_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_FwdDiscEnabled based on Integer32"""
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


_MaxpotsProfile_LineInterface_FwdDiscEnabled_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_FwdDiscEnabled_Object = MibScalar
maxpotsProfile_LineInterface_FwdDiscEnabled = _MaxpotsProfile_LineInterface_FwdDiscEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 10),
    _MaxpotsProfile_LineInterface_FwdDiscEnabled_Type()
)
maxpotsProfile_LineInterface_FwdDiscEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_FwdDiscEnabled.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_RxGain_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_RxGain based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("n-0db", 1),
          ("n-10db", 23),
          ("n-11db", 24),
          ("n-12db", 25),
          ("n-1db", 14),
          ("n-2db", 15),
          ("n-3db", 16),
          ("n-4db", 17),
          ("n-5db", 18),
          ("n-6db", 19),
          ("n-7db", 20),
          ("n-8db", 21),
          ("n-9db", 22),
          ("n-plus-10db", 11),
          ("n-plus-11db", 12),
          ("n-plus-12db", 13),
          ("n-plus-1db", 2),
          ("n-plus-2db", 3),
          ("n-plus-3db", 4),
          ("n-plus-4db", 5),
          ("n-plus-5db", 6),
          ("n-plus-6db", 7),
          ("n-plus-7db", 8),
          ("n-plus-8db", 9),
          ("n-plus-9db", 10))
    )


_MaxpotsProfile_LineInterface_RxGain_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_RxGain_Object = MibScalar
maxpotsProfile_LineInterface_RxGain = _MaxpotsProfile_LineInterface_RxGain_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 11),
    _MaxpotsProfile_LineInterface_RxGain_Type()
)
maxpotsProfile_LineInterface_RxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_RxGain.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_TxGain_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_TxGain based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("n-0db", 1),
          ("n-10db", 23),
          ("n-11db", 24),
          ("n-12db", 25),
          ("n-1db", 14),
          ("n-2db", 15),
          ("n-3db", 16),
          ("n-4db", 17),
          ("n-5db", 18),
          ("n-6db", 19),
          ("n-7db", 20),
          ("n-8db", 21),
          ("n-9db", 22),
          ("n-plus-10db", 11),
          ("n-plus-11db", 12),
          ("n-plus-12db", 13),
          ("n-plus-1db", 2),
          ("n-plus-2db", 3),
          ("n-plus-3db", 4),
          ("n-plus-4db", 5),
          ("n-plus-5db", 6),
          ("n-plus-6db", 7),
          ("n-plus-7db", 8),
          ("n-plus-8db", 9),
          ("n-plus-9db", 10))
    )


_MaxpotsProfile_LineInterface_TxGain_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_TxGain_Object = MibScalar
maxpotsProfile_LineInterface_TxGain = _MaxpotsProfile_LineInterface_TxGain_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 12),
    _MaxpotsProfile_LineInterface_TxGain_Type()
)
maxpotsProfile_LineInterface_TxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_TxGain.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_Signaling_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_Signaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groundStart", 2),
          ("loopStart", 1))
    )


_MaxpotsProfile_LineInterface_Signaling_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_Signaling_Object = MibScalar
maxpotsProfile_LineInterface_Signaling = _MaxpotsProfile_LineInterface_Signaling_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 13),
    _MaxpotsProfile_LineInterface_Signaling_Type()
)
maxpotsProfile_LineInterface_Signaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_Signaling.setStatus("mandatory")


class _MaxpotsProfile_LineInterface_GndStartRing_Type(Integer32):
    """Custom type maxpotsProfile_LineInterface_GndStartRing based on Integer32"""
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


_MaxpotsProfile_LineInterface_GndStartRing_Type.__name__ = "Integer32"
_MaxpotsProfile_LineInterface_GndStartRing_Object = MibScalar
maxpotsProfile_LineInterface_GndStartRing = _MaxpotsProfile_LineInterface_GndStartRing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 94, 2, 1, 14),
    _MaxpotsProfile_LineInterface_GndStartRing_Type()
)
maxpotsProfile_LineInterface_GndStartRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxpotsProfile_LineInterface_GndStartRing.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBMAXPOTS-MIB",
    **{"DisplayString": DisplayString,
       "mibmaxpotsProfile": mibmaxpotsProfile,
       "mibmaxpotsProfileTable": mibmaxpotsProfileTable,
       "mibmaxpotsProfileEntry": mibmaxpotsProfileEntry,
       "maxpotsProfile-Shelf-o": maxpotsProfile_Shelf_o,
       "maxpotsProfile-Slot-o": maxpotsProfile_Slot_o,
       "maxpotsProfile-Item-o": maxpotsProfile_Item_o,
       "maxpotsProfile-ProfileNumber": maxpotsProfile_ProfileNumber,
       "maxpotsProfile-Name": maxpotsProfile_Name,
       "maxpotsProfile-PhysicalAddress-Shelf": maxpotsProfile_PhysicalAddress_Shelf,
       "maxpotsProfile-PhysicalAddress-Slot": maxpotsProfile_PhysicalAddress_Slot,
       "maxpotsProfile-PhysicalAddress-ItemNumber": maxpotsProfile_PhysicalAddress_ItemNumber,
       "maxpotsProfile-Action-o": maxpotsProfile_Action_o,
       "mibmaxpotsProfile-LineInterfaceTable": mibmaxpotsProfile_LineInterfaceTable,
       "mibmaxpotsProfile-LineInterfaceEntry": mibmaxpotsProfile_LineInterfaceEntry,
       "maxpotsProfile-LineInterface-Shelf-o": maxpotsProfile_LineInterface_Shelf_o,
       "maxpotsProfile-LineInterface-Slot-o": maxpotsProfile_LineInterface_Slot_o,
       "maxpotsProfile-LineInterface-Item-o": maxpotsProfile_LineInterface_Item_o,
       "maxpotsProfile-LineInterface-Index-o": maxpotsProfile_LineInterface_Index_o,
       "maxpotsProfile-LineInterface-DialEnabled": maxpotsProfile_LineInterface_DialEnabled,
       "maxpotsProfile-LineInterface-NetClidEnabled": maxpotsProfile_LineInterface_NetClidEnabled,
       "maxpotsProfile-LineInterface-ClidNumber": maxpotsProfile_LineInterface_ClidNumber,
       "maxpotsProfile-LineInterface-AnswerEnabled": maxpotsProfile_LineInterface_AnswerEnabled,
       "maxpotsProfile-LineInterface-CallerIdEnabled": maxpotsProfile_LineInterface_CallerIdEnabled,
       "maxpotsProfile-LineInterface-FwdDiscEnabled": maxpotsProfile_LineInterface_FwdDiscEnabled,
       "maxpotsProfile-LineInterface-RxGain": maxpotsProfile_LineInterface_RxGain,
       "maxpotsProfile-LineInterface-TxGain": maxpotsProfile_LineInterface_TxGain,
       "maxpotsProfile-LineInterface-Signaling": maxpotsProfile_LineInterface_Signaling,
       "maxpotsProfile-LineInterface-GndStartRing": maxpotsProfile_LineInterface_GndStartRing}
)
