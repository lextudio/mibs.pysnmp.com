# SNMP MIB module (ASCEND-MIBT3INT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBT3INT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:25 2024
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

_Mibt3InterfaceProfile_ObjectIdentity = ObjectIdentity
mibt3InterfaceProfile = _Mibt3InterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 156)
)
_Mibt3InterfaceProfileTable_Object = MibTable
mibt3InterfaceProfileTable = _Mibt3InterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1)
)
if mibBuilder.loadTexts:
    mibt3InterfaceProfileTable.setStatus("mandatory")
_Mibt3InterfaceProfileEntry_Object = MibTableRow
mibt3InterfaceProfileEntry = _Mibt3InterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1)
)
mibt3InterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBT3INT-MIB", "t3InterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBT3INT-MIB", "t3InterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBT3INT-MIB", "t3InterfaceProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibt3InterfaceProfileEntry.setStatus("mandatory")
_T3InterfaceProfile_Shelf_o_Type = Integer32
_T3InterfaceProfile_Shelf_o_Object = MibScalar
t3InterfaceProfile_Shelf_o = _T3InterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 1),
    _T3InterfaceProfile_Shelf_o_Type()
)
t3InterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Shelf_o.setStatus("mandatory")
_T3InterfaceProfile_Slot_o_Type = Integer32
_T3InterfaceProfile_Slot_o_Object = MibScalar
t3InterfaceProfile_Slot_o = _T3InterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 2),
    _T3InterfaceProfile_Slot_o_Type()
)
t3InterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Slot_o.setStatus("mandatory")
_T3InterfaceProfile_Item_o_Type = Integer32
_T3InterfaceProfile_Item_o_Object = MibScalar
t3InterfaceProfile_Item_o = _T3InterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 3),
    _T3InterfaceProfile_Item_o_Type()
)
t3InterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Item_o.setStatus("mandatory")
_T3InterfaceProfile_Name_Type = DisplayString
_T3InterfaceProfile_Name_Object = MibScalar
t3InterfaceProfile_Name = _T3InterfaceProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 4),
    _T3InterfaceProfile_Name_Type()
)
t3InterfaceProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Name.setStatus("mandatory")


class _T3InterfaceProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type t3InterfaceProfile_PhysicalAddress_Shelf based on Integer32"""
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


_T3InterfaceProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_T3InterfaceProfile_PhysicalAddress_Shelf_Object = MibScalar
t3InterfaceProfile_PhysicalAddress_Shelf = _T3InterfaceProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 5),
    _T3InterfaceProfile_PhysicalAddress_Shelf_Type()
)
t3InterfaceProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _T3InterfaceProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type t3InterfaceProfile_PhysicalAddress_Slot based on Integer32"""
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


_T3InterfaceProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_T3InterfaceProfile_PhysicalAddress_Slot_Object = MibScalar
t3InterfaceProfile_PhysicalAddress_Slot = _T3InterfaceProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 6),
    _T3InterfaceProfile_PhysicalAddress_Slot_Type()
)
t3InterfaceProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_PhysicalAddress_Slot.setStatus("mandatory")
_T3InterfaceProfile_PhysicalAddress_ItemNumber_Type = Integer32
_T3InterfaceProfile_PhysicalAddress_ItemNumber_Object = MibScalar
t3InterfaceProfile_PhysicalAddress_ItemNumber = _T3InterfaceProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 7),
    _T3InterfaceProfile_PhysicalAddress_ItemNumber_Type()
)
t3InterfaceProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _T3InterfaceProfile_LimControl_PrimaryLpm_Type(Integer32):
    """Custom type t3InterfaceProfile_LimControl_PrimaryLpm based on Integer32"""
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


_T3InterfaceProfile_LimControl_PrimaryLpm_Type.__name__ = "Integer32"
_T3InterfaceProfile_LimControl_PrimaryLpm_Object = MibScalar
t3InterfaceProfile_LimControl_PrimaryLpm = _T3InterfaceProfile_LimControl_PrimaryLpm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 8),
    _T3InterfaceProfile_LimControl_PrimaryLpm_Type()
)
t3InterfaceProfile_LimControl_PrimaryLpm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_LimControl_PrimaryLpm.setStatus("mandatory")


class _T3InterfaceProfile_LimControl_ActiveLine_Type(Integer32):
    """Custom type t3InterfaceProfile_LimControl_ActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupLine", 3),
          ("protectionLine", 2),
          ("workingLine", 1))
    )


_T3InterfaceProfile_LimControl_ActiveLine_Type.__name__ = "Integer32"
_T3InterfaceProfile_LimControl_ActiveLine_Object = MibScalar
t3InterfaceProfile_LimControl_ActiveLine = _T3InterfaceProfile_LimControl_ActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 9),
    _T3InterfaceProfile_LimControl_ActiveLine_Type()
)
t3InterfaceProfile_LimControl_ActiveLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_LimControl_ActiveLine.setStatus("mandatory")
_T3InterfaceProfile_Ds3Profile_Name_Type = DisplayString
_T3InterfaceProfile_Ds3Profile_Name_Object = MibScalar
t3InterfaceProfile_Ds3Profile_Name = _T3InterfaceProfile_Ds3Profile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 10),
    _T3InterfaceProfile_Ds3Profile_Name_Type()
)
t3InterfaceProfile_Ds3Profile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_Name.setStatus("mandatory")


class _T3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type t3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf based on Integer32"""
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


_T3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_T3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf_Object = MibScalar
t3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf = _T3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 11),
    _T3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf_Type()
)
t3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf.setStatus("mandatory")


class _T3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type t3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot based on Integer32"""
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


_T3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_T3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot_Object = MibScalar
t3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot = _T3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 12),
    _T3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot_Type()
)
t3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot.setStatus("mandatory")
_T3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber_Type = Integer32
_T3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber_Object = MibScalar
t3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber = _T3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 13),
    _T3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber_Type()
)
t3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _T3InterfaceProfile_Ds3Profile_Enabled_Type(Integer32):
    """Custom type t3InterfaceProfile_Ds3Profile_Enabled based on Integer32"""
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


_T3InterfaceProfile_Ds3Profile_Enabled_Type.__name__ = "Integer32"
_T3InterfaceProfile_Ds3Profile_Enabled_Object = MibScalar
t3InterfaceProfile_Ds3Profile_Enabled = _T3InterfaceProfile_Ds3Profile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 14),
    _T3InterfaceProfile_Ds3Profile_Enabled_Type()
)
t3InterfaceProfile_Ds3Profile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_Enabled.setStatus("mandatory")


class _T3InterfaceProfile_Ds3Profile_FrameType_Type(Integer32):
    """Custom type t3InterfaceProfile_Ds3Profile_FrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cBitParity", 2),
          ("m13", 1))
    )


_T3InterfaceProfile_Ds3Profile_FrameType_Type.__name__ = "Integer32"
_T3InterfaceProfile_Ds3Profile_FrameType_Object = MibScalar
t3InterfaceProfile_Ds3Profile_FrameType = _T3InterfaceProfile_Ds3Profile_FrameType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 15),
    _T3InterfaceProfile_Ds3Profile_FrameType_Type()
)
t3InterfaceProfile_Ds3Profile_FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_FrameType.setStatus("mandatory")


class _T3InterfaceProfile_Ds3Profile_LineLength_Type(Integer32):
    """Custom type t3InterfaceProfile_Ds3Profile_LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-0225", 1),
          ("n-226450", 2))
    )


_T3InterfaceProfile_Ds3Profile_LineLength_Type.__name__ = "Integer32"
_T3InterfaceProfile_Ds3Profile_LineLength_Object = MibScalar
t3InterfaceProfile_Ds3Profile_LineLength = _T3InterfaceProfile_Ds3Profile_LineLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 16),
    _T3InterfaceProfile_Ds3Profile_LineLength_Type()
)
t3InterfaceProfile_Ds3Profile_LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_LineLength.setStatus("mandatory")


class _T3InterfaceProfile_Ds3Profile_Loopback_Type(Integer32):
    """Custom type t3InterfaceProfile_Ds3Profile_Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineLoopback", 2),
          ("localLoopback", 3),
          ("noLoopback", 1))
    )


_T3InterfaceProfile_Ds3Profile_Loopback_Type.__name__ = "Integer32"
_T3InterfaceProfile_Ds3Profile_Loopback_Object = MibScalar
t3InterfaceProfile_Ds3Profile_Loopback = _T3InterfaceProfile_Ds3Profile_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 17),
    _T3InterfaceProfile_Ds3Profile_Loopback_Type()
)
t3InterfaceProfile_Ds3Profile_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_Loopback.setStatus("mandatory")


class _T3InterfaceProfile_Action_o_Type(Integer32):
    """Custom type t3InterfaceProfile_Action_o based on Integer32"""
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


_T3InterfaceProfile_Action_o_Type.__name__ = "Integer32"
_T3InterfaceProfile_Action_o_Object = MibScalar
t3InterfaceProfile_Action_o = _T3InterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 19),
    _T3InterfaceProfile_Action_o_Type()
)
t3InterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Action_o.setStatus("mandatory")


class _T3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable_Type(Integer32):
    """Custom type t3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable based on Integer32"""
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


_T3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_T3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable_Object = MibScalar
t3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable = _T3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 1, 1, 20),
    _T3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable_Type()
)
t3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable.setStatus("mandatory")
_Mibt3InterfaceProfile_MasterDs1IndexTable_Object = MibTable
mibt3InterfaceProfile_MasterDs1IndexTable = _Mibt3InterfaceProfile_MasterDs1IndexTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 18)
)
if mibBuilder.loadTexts:
    mibt3InterfaceProfile_MasterDs1IndexTable.setStatus("mandatory")
_Mibt3InterfaceProfile_MasterDs1IndexEntry_Object = MibTableRow
mibt3InterfaceProfile_MasterDs1IndexEntry = _Mibt3InterfaceProfile_MasterDs1IndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 18, 1)
)
mibt3InterfaceProfile_MasterDs1IndexEntry.setIndexNames(
    (0, "ASCEND-MIBT3INT-MIB", "t3InterfaceProfile-MasterDs1Index-Shelf-o"),
    (0, "ASCEND-MIBT3INT-MIB", "t3InterfaceProfile-MasterDs1Index-Slot-o"),
    (0, "ASCEND-MIBT3INT-MIB", "t3InterfaceProfile-MasterDs1Index-Item-o"),
    (0, "ASCEND-MIBT3INT-MIB", "t3InterfaceProfile-MasterDs1Index-Index-o"),
)
if mibBuilder.loadTexts:
    mibt3InterfaceProfile_MasterDs1IndexEntry.setStatus("mandatory")
_T3InterfaceProfile_MasterDs1Index_Shelf_o_Type = Integer32
_T3InterfaceProfile_MasterDs1Index_Shelf_o_Object = MibScalar
t3InterfaceProfile_MasterDs1Index_Shelf_o = _T3InterfaceProfile_MasterDs1Index_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 18, 1, 1),
    _T3InterfaceProfile_MasterDs1Index_Shelf_o_Type()
)
t3InterfaceProfile_MasterDs1Index_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3InterfaceProfile_MasterDs1Index_Shelf_o.setStatus("mandatory")
_T3InterfaceProfile_MasterDs1Index_Slot_o_Type = Integer32
_T3InterfaceProfile_MasterDs1Index_Slot_o_Object = MibScalar
t3InterfaceProfile_MasterDs1Index_Slot_o = _T3InterfaceProfile_MasterDs1Index_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 18, 1, 2),
    _T3InterfaceProfile_MasterDs1Index_Slot_o_Type()
)
t3InterfaceProfile_MasterDs1Index_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3InterfaceProfile_MasterDs1Index_Slot_o.setStatus("mandatory")
_T3InterfaceProfile_MasterDs1Index_Item_o_Type = Integer32
_T3InterfaceProfile_MasterDs1Index_Item_o_Object = MibScalar
t3InterfaceProfile_MasterDs1Index_Item_o = _T3InterfaceProfile_MasterDs1Index_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 18, 1, 3),
    _T3InterfaceProfile_MasterDs1Index_Item_o_Type()
)
t3InterfaceProfile_MasterDs1Index_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3InterfaceProfile_MasterDs1Index_Item_o.setStatus("mandatory")
_T3InterfaceProfile_MasterDs1Index_Index_o_Type = Integer32
_T3InterfaceProfile_MasterDs1Index_Index_o_Object = MibScalar
t3InterfaceProfile_MasterDs1Index_Index_o = _T3InterfaceProfile_MasterDs1Index_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 18, 1, 4),
    _T3InterfaceProfile_MasterDs1Index_Index_o_Type()
)
t3InterfaceProfile_MasterDs1Index_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3InterfaceProfile_MasterDs1Index_Index_o.setStatus("mandatory")
_T3InterfaceProfile_MasterDs1Index_Type = Integer32
_T3InterfaceProfile_MasterDs1Index_Object = MibScalar
t3InterfaceProfile_MasterDs1Index = _T3InterfaceProfile_MasterDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 156, 18, 1, 5),
    _T3InterfaceProfile_MasterDs1Index_Type()
)
t3InterfaceProfile_MasterDs1Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3InterfaceProfile_MasterDs1Index.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBT3INT-MIB",
    **{"DisplayString": DisplayString,
       "mibt3InterfaceProfile": mibt3InterfaceProfile,
       "mibt3InterfaceProfileTable": mibt3InterfaceProfileTable,
       "mibt3InterfaceProfileEntry": mibt3InterfaceProfileEntry,
       "t3InterfaceProfile-Shelf-o": t3InterfaceProfile_Shelf_o,
       "t3InterfaceProfile-Slot-o": t3InterfaceProfile_Slot_o,
       "t3InterfaceProfile-Item-o": t3InterfaceProfile_Item_o,
       "t3InterfaceProfile-Name": t3InterfaceProfile_Name,
       "t3InterfaceProfile-PhysicalAddress-Shelf": t3InterfaceProfile_PhysicalAddress_Shelf,
       "t3InterfaceProfile-PhysicalAddress-Slot": t3InterfaceProfile_PhysicalAddress_Slot,
       "t3InterfaceProfile-PhysicalAddress-ItemNumber": t3InterfaceProfile_PhysicalAddress_ItemNumber,
       "t3InterfaceProfile-LimControl-PrimaryLpm": t3InterfaceProfile_LimControl_PrimaryLpm,
       "t3InterfaceProfile-LimControl-ActiveLine": t3InterfaceProfile_LimControl_ActiveLine,
       "t3InterfaceProfile-Ds3Profile-Name": t3InterfaceProfile_Ds3Profile_Name,
       "t3InterfaceProfile-Ds3Profile-PhysicalAddress-Shelf": t3InterfaceProfile_Ds3Profile_PhysicalAddress_Shelf,
       "t3InterfaceProfile-Ds3Profile-PhysicalAddress-Slot": t3InterfaceProfile_Ds3Profile_PhysicalAddress_Slot,
       "t3InterfaceProfile-Ds3Profile-PhysicalAddress-ItemNumber": t3InterfaceProfile_Ds3Profile_PhysicalAddress_ItemNumber,
       "t3InterfaceProfile-Ds3Profile-Enabled": t3InterfaceProfile_Ds3Profile_Enabled,
       "t3InterfaceProfile-Ds3Profile-FrameType": t3InterfaceProfile_Ds3Profile_FrameType,
       "t3InterfaceProfile-Ds3Profile-LineLength": t3InterfaceProfile_Ds3Profile_LineLength,
       "t3InterfaceProfile-Ds3Profile-Loopback": t3InterfaceProfile_Ds3Profile_Loopback,
       "t3InterfaceProfile-Action-o": t3InterfaceProfile_Action_o,
       "t3InterfaceProfile-Ds3Profile-StatusChangeTrapEnable": t3InterfaceProfile_Ds3Profile_StatusChangeTrapEnable,
       "mibt3InterfaceProfile-MasterDs1IndexTable": mibt3InterfaceProfile_MasterDs1IndexTable,
       "mibt3InterfaceProfile-MasterDs1IndexEntry": mibt3InterfaceProfile_MasterDs1IndexEntry,
       "t3InterfaceProfile-MasterDs1Index-Shelf-o": t3InterfaceProfile_MasterDs1Index_Shelf_o,
       "t3InterfaceProfile-MasterDs1Index-Slot-o": t3InterfaceProfile_MasterDs1Index_Slot_o,
       "t3InterfaceProfile-MasterDs1Index-Item-o": t3InterfaceProfile_MasterDs1Index_Item_o,
       "t3InterfaceProfile-MasterDs1Index-Index-o": t3InterfaceProfile_MasterDs1Index_Index_o,
       "t3InterfaceProfile-MasterDs1Index": t3InterfaceProfile_MasterDs1Index}
)
