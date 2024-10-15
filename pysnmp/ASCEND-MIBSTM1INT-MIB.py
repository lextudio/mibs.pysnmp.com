# SNMP MIB module (ASCEND-MIBSTM1INT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSTM1INT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:19 2024
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

_MibsTM1InterfaceProfile_ObjectIdentity = ObjectIdentity
mibsTM1InterfaceProfile = _MibsTM1InterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 154)
)
_MibsTM1InterfaceProfileTable_Object = MibTable
mibsTM1InterfaceProfileTable = _MibsTM1InterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1)
)
if mibBuilder.loadTexts:
    mibsTM1InterfaceProfileTable.setStatus("mandatory")
_MibsTM1InterfaceProfileEntry_Object = MibTableRow
mibsTM1InterfaceProfileEntry = _MibsTM1InterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1)
)
mibsTM1InterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibsTM1InterfaceProfileEntry.setStatus("mandatory")
_STM1InterfaceProfile_Shelf_o_Type = Integer32
_STM1InterfaceProfile_Shelf_o_Object = MibScalar
sTM1InterfaceProfile_Shelf_o = _STM1InterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 1),
    _STM1InterfaceProfile_Shelf_o_Type()
)
sTM1InterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_Shelf_o.setStatus("mandatory")
_STM1InterfaceProfile_Slot_o_Type = Integer32
_STM1InterfaceProfile_Slot_o_Object = MibScalar
sTM1InterfaceProfile_Slot_o = _STM1InterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 2),
    _STM1InterfaceProfile_Slot_o_Type()
)
sTM1InterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_Slot_o.setStatus("mandatory")
_STM1InterfaceProfile_Item_o_Type = Integer32
_STM1InterfaceProfile_Item_o_Object = MibScalar
sTM1InterfaceProfile_Item_o = _STM1InterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 3),
    _STM1InterfaceProfile_Item_o_Type()
)
sTM1InterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_Item_o.setStatus("mandatory")
_STM1InterfaceProfile_Name_Type = DisplayString
_STM1InterfaceProfile_Name_Object = MibScalar
sTM1InterfaceProfile_Name = _STM1InterfaceProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 4),
    _STM1InterfaceProfile_Name_Type()
)
sTM1InterfaceProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_Name.setStatus("mandatory")


class _STM1InterfaceProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PhysicalAddress_Shelf based on Integer32"""
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


_STM1InterfaceProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PhysicalAddress_Shelf_Object = MibScalar
sTM1InterfaceProfile_PhysicalAddress_Shelf = _STM1InterfaceProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 5),
    _STM1InterfaceProfile_PhysicalAddress_Shelf_Type()
)
sTM1InterfaceProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _STM1InterfaceProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PhysicalAddress_Slot based on Integer32"""
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


_STM1InterfaceProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PhysicalAddress_Slot_Object = MibScalar
sTM1InterfaceProfile_PhysicalAddress_Slot = _STM1InterfaceProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 6),
    _STM1InterfaceProfile_PhysicalAddress_Slot_Type()
)
sTM1InterfaceProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PhysicalAddress_Slot.setStatus("mandatory")
_STM1InterfaceProfile_PhysicalAddress_ItemNumber_Type = Integer32
_STM1InterfaceProfile_PhysicalAddress_ItemNumber_Object = MibScalar
sTM1InterfaceProfile_PhysicalAddress_ItemNumber = _STM1InterfaceProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 7),
    _STM1InterfaceProfile_PhysicalAddress_ItemNumber_Type()
)
sTM1InterfaceProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _STM1InterfaceProfile_LimControl_PrimaryLpm_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LimControl_PrimaryLpm based on Integer32"""
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


_STM1InterfaceProfile_LimControl_PrimaryLpm_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LimControl_PrimaryLpm_Object = MibScalar
sTM1InterfaceProfile_LimControl_PrimaryLpm = _STM1InterfaceProfile_LimControl_PrimaryLpm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 8),
    _STM1InterfaceProfile_LimControl_PrimaryLpm_Type()
)
sTM1InterfaceProfile_LimControl_PrimaryLpm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LimControl_PrimaryLpm.setStatus("mandatory")


class _STM1InterfaceProfile_LimControl_ActiveLine_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LimControl_ActiveLine based on Integer32"""
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


_STM1InterfaceProfile_LimControl_ActiveLine_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LimControl_ActiveLine_Object = MibScalar
sTM1InterfaceProfile_LimControl_ActiveLine = _STM1InterfaceProfile_LimControl_ActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 9),
    _STM1InterfaceProfile_LimControl_ActiveLine_Type()
)
sTM1InterfaceProfile_LimControl_ActiveLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LimControl_ActiveLine.setStatus("mandatory")
_STM1InterfaceProfile_LineParams_Name_Type = DisplayString
_STM1InterfaceProfile_LineParams_Name_Object = MibScalar
sTM1InterfaceProfile_LineParams_Name = _STM1InterfaceProfile_LineParams_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 10),
    _STM1InterfaceProfile_LineParams_Name_Type()
)
sTM1InterfaceProfile_LineParams_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_Name.setStatus("mandatory")


class _STM1InterfaceProfile_LineParams_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LineParams_PhysicalAddress_Shelf based on Integer32"""
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


_STM1InterfaceProfile_LineParams_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LineParams_PhysicalAddress_Shelf_Object = MibScalar
sTM1InterfaceProfile_LineParams_PhysicalAddress_Shelf = _STM1InterfaceProfile_LineParams_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 11),
    _STM1InterfaceProfile_LineParams_PhysicalAddress_Shelf_Type()
)
sTM1InterfaceProfile_LineParams_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_PhysicalAddress_Shelf.setStatus("mandatory")


class _STM1InterfaceProfile_LineParams_PhysicalAddress_Slot_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LineParams_PhysicalAddress_Slot based on Integer32"""
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


_STM1InterfaceProfile_LineParams_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LineParams_PhysicalAddress_Slot_Object = MibScalar
sTM1InterfaceProfile_LineParams_PhysicalAddress_Slot = _STM1InterfaceProfile_LineParams_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 12),
    _STM1InterfaceProfile_LineParams_PhysicalAddress_Slot_Type()
)
sTM1InterfaceProfile_LineParams_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_PhysicalAddress_Slot.setStatus("mandatory")
_STM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber_Type = Integer32
_STM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber_Object = MibScalar
sTM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber = _STM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 13),
    _STM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber_Type()
)
sTM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _STM1InterfaceProfile_LineParams_Enabled_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LineParams_Enabled based on Integer32"""
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


_STM1InterfaceProfile_LineParams_Enabled_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LineParams_Enabled_Object = MibScalar
sTM1InterfaceProfile_LineParams_Enabled = _STM1InterfaceProfile_LineParams_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 14),
    _STM1InterfaceProfile_LineParams_Enabled_Type()
)
sTM1InterfaceProfile_LineParams_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_Enabled.setStatus("mandatory")


class _STM1InterfaceProfile_LineParams_AuPointer_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LineParams_AuPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("au3Pointer", 2),
          ("au4Pointer", 3))
    )


_STM1InterfaceProfile_LineParams_AuPointer_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LineParams_AuPointer_Object = MibScalar
sTM1InterfaceProfile_LineParams_AuPointer = _STM1InterfaceProfile_LineParams_AuPointer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 15),
    _STM1InterfaceProfile_LineParams_AuPointer_Type()
)
sTM1InterfaceProfile_LineParams_AuPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_AuPointer.setStatus("mandatory")


class _STM1InterfaceProfile_LineParams_LoopTiming_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LineParams_LoopTiming based on Integer32"""
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


_STM1InterfaceProfile_LineParams_LoopTiming_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LineParams_LoopTiming_Object = MibScalar
sTM1InterfaceProfile_LineParams_LoopTiming = _STM1InterfaceProfile_LineParams_LoopTiming_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 16),
    _STM1InterfaceProfile_LineParams_LoopTiming_Type()
)
sTM1InterfaceProfile_LineParams_LoopTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_LoopTiming.setStatus("mandatory")


class _STM1InterfaceProfile_LineParams_Loopback_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LineParams_Loopback based on Integer32"""
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


_STM1InterfaceProfile_LineParams_Loopback_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LineParams_Loopback_Object = MibScalar
sTM1InterfaceProfile_LineParams_Loopback = _STM1InterfaceProfile_LineParams_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 17),
    _STM1InterfaceProfile_LineParams_Loopback_Type()
)
sTM1InterfaceProfile_LineParams_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_Loopback.setStatus("mandatory")


class _STM1InterfaceProfile_Action_o_Type(Integer32):
    """Custom type sTM1InterfaceProfile_Action_o based on Integer32"""
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


_STM1InterfaceProfile_Action_o_Type.__name__ = "Integer32"
_STM1InterfaceProfile_Action_o_Object = MibScalar
sTM1InterfaceProfile_Action_o = _STM1InterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 18),
    _STM1InterfaceProfile_Action_o_Type()
)
sTM1InterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_Action_o.setStatus("mandatory")
_STM1InterfaceProfile_LineParams_ApsConfigName_Type = DisplayString
_STM1InterfaceProfile_LineParams_ApsConfigName_Object = MibScalar
sTM1InterfaceProfile_LineParams_ApsConfigName = _STM1InterfaceProfile_LineParams_ApsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 19),
    _STM1InterfaceProfile_LineParams_ApsConfigName_Type()
)
sTM1InterfaceProfile_LineParams_ApsConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_ApsConfigName.setStatus("mandatory")


class _STM1InterfaceProfile_LineParams_Signaling_Type(Integer32):
    """Custom type sTM1InterfaceProfile_LineParams_Signaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("japan", 4),
          ("sdh", 3),
          ("sonet", 2))
    )


_STM1InterfaceProfile_LineParams_Signaling_Type.__name__ = "Integer32"
_STM1InterfaceProfile_LineParams_Signaling_Object = MibScalar
sTM1InterfaceProfile_LineParams_Signaling = _STM1InterfaceProfile_LineParams_Signaling_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 1, 1, 20),
    _STM1InterfaceProfile_LineParams_Signaling_Type()
)
sTM1InterfaceProfile_LineParams_Signaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_LineParams_Signaling.setStatus("mandatory")
_MibsTM1InterfaceProfile_PathParamsTable_Object = MibTable
mibsTM1InterfaceProfile_PathParamsTable = _MibsTM1InterfaceProfile_PathParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2)
)
if mibBuilder.loadTexts:
    mibsTM1InterfaceProfile_PathParamsTable.setStatus("mandatory")
_MibsTM1InterfaceProfile_PathParamsEntry_Object = MibTableRow
mibsTM1InterfaceProfile_PathParamsEntry = _MibsTM1InterfaceProfile_PathParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1)
)
mibsTM1InterfaceProfile_PathParamsEntry.setIndexNames(
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-Shelf-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-Slot-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-Item-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-Index-o"),
)
if mibBuilder.loadTexts:
    mibsTM1InterfaceProfile_PathParamsEntry.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Shelf_o_Type = Integer32
_STM1InterfaceProfile_PathParams_Shelf_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_Shelf_o = _STM1InterfaceProfile_PathParams_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 1),
    _STM1InterfaceProfile_PathParams_Shelf_o_Type()
)
sTM1InterfaceProfile_PathParams_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Shelf_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Slot_o_Type = Integer32
_STM1InterfaceProfile_PathParams_Slot_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_Slot_o = _STM1InterfaceProfile_PathParams_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 2),
    _STM1InterfaceProfile_PathParams_Slot_o_Type()
)
sTM1InterfaceProfile_PathParams_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Slot_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Item_o_Type = Integer32
_STM1InterfaceProfile_PathParams_Item_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_Item_o = _STM1InterfaceProfile_PathParams_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 3),
    _STM1InterfaceProfile_PathParams_Item_o_Type()
)
sTM1InterfaceProfile_PathParams_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Item_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Index_o_Type = Integer32
_STM1InterfaceProfile_PathParams_Index_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_Index_o = _STM1InterfaceProfile_PathParams_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 4),
    _STM1InterfaceProfile_PathParams_Index_o_Type()
)
sTM1InterfaceProfile_PathParams_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Index_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Name_Type = DisplayString
_STM1InterfaceProfile_PathParams_Name_Object = MibScalar
sTM1InterfaceProfile_PathParams_Name = _STM1InterfaceProfile_PathParams_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 5),
    _STM1InterfaceProfile_PathParams_Name_Type()
)
sTM1InterfaceProfile_PathParams_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Name.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Stm0Profile_Name_Type = DisplayString
_STM1InterfaceProfile_PathParams_Stm0Profile_Name_Object = MibScalar
sTM1InterfaceProfile_PathParams_Stm0Profile_Name = _STM1InterfaceProfile_PathParams_Stm0Profile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 6),
    _STM1InterfaceProfile_PathParams_Stm0Profile_Name_Type()
)
sTM1InterfaceProfile_PathParams_Stm0Profile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Stm0Profile_Name.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf_Object = MibScalar
sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf = _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 7),
    _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf_Type()
)
sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot_Object = MibScalar
sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot = _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 8),
    _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot_Type()
)
sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber_Type = Integer32
_STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber_Object = MibScalar
sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber = _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 9),
    _STM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber_Type()
)
sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Stm0Profile_Enabled_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Stm0Profile_Enabled based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Stm0Profile_Enabled_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Stm0Profile_Enabled_Object = MibScalar
sTM1InterfaceProfile_PathParams_Stm0Profile_Enabled = _STM1InterfaceProfile_PathParams_Stm0Profile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 10),
    _STM1InterfaceProfile_PathParams_Stm0Profile_Enabled_Type()
)
sTM1InterfaceProfile_PathParams_Stm0Profile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Stm0Profile_Enabled.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("vc11AsyncMapping", 2),
          ("vc11ByteSyncMapping", 3),
          ("vc12AsyncMapping", 5),
          ("vc12ByteSyncMapping", 6),
          ("vc3AsyncMapping", 8))
    )


_STM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping_Object = MibScalar
sTM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping = _STM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 11),
    _STM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping_Type()
)
sTM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Ds3Profile_Name_Type = DisplayString
_STM1InterfaceProfile_PathParams_Ds3Profile_Name_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_Name = _STM1InterfaceProfile_PathParams_Ds3Profile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 12),
    _STM1InterfaceProfile_PathParams_Ds3Profile_Name_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_Name.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf = _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 13),
    _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot = _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 14),
    _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber_Type = Integer32
_STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber = _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 15),
    _STM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Ds3Profile_Enabled_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Ds3Profile_Enabled based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Ds3Profile_Enabled_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Ds3Profile_Enabled_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_Enabled = _STM1InterfaceProfile_PathParams_Ds3Profile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 16),
    _STM1InterfaceProfile_PathParams_Ds3Profile_Enabled_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_Enabled.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Ds3Profile_FrameType_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Ds3Profile_FrameType based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Ds3Profile_FrameType_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Ds3Profile_FrameType_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_FrameType = _STM1InterfaceProfile_PathParams_Ds3Profile_FrameType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 17),
    _STM1InterfaceProfile_PathParams_Ds3Profile_FrameType_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_FrameType.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Ds3Profile_LineLength_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Ds3Profile_LineLength based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Ds3Profile_LineLength_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Ds3Profile_LineLength_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_LineLength = _STM1InterfaceProfile_PathParams_Ds3Profile_LineLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 18),
    _STM1InterfaceProfile_PathParams_Ds3Profile_LineLength_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_LineLength.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Ds3Profile_Loopback_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Ds3Profile_Loopback based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Ds3Profile_Loopback_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Ds3Profile_Loopback_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_Loopback = _STM1InterfaceProfile_PathParams_Ds3Profile_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 19),
    _STM1InterfaceProfile_PathParams_Ds3Profile_Loopback_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_Loopback.setStatus("mandatory")


class _STM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable_Type(Integer32):
    """Custom type sTM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable based on Integer32"""
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


_STM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_STM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable_Object = MibScalar
sTM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable = _STM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 2, 1, 21),
    _STM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable_Type()
)
sTM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable.setStatus("mandatory")
_MibsTM1InterfaceProfile_PathParams_MasterDs1IndexTable_Object = MibTable
mibsTM1InterfaceProfile_PathParams_MasterDs1IndexTable = _MibsTM1InterfaceProfile_PathParams_MasterDs1IndexTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20)
)
if mibBuilder.loadTexts:
    mibsTM1InterfaceProfile_PathParams_MasterDs1IndexTable.setStatus("mandatory")
_MibsTM1InterfaceProfile_PathParams_MasterDs1IndexEntry_Object = MibTableRow
mibsTM1InterfaceProfile_PathParams_MasterDs1IndexEntry = _MibsTM1InterfaceProfile_PathParams_MasterDs1IndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20, 1)
)
mibsTM1InterfaceProfile_PathParams_MasterDs1IndexEntry.setIndexNames(
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-MasterDs1Index-Shelf-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-MasterDs1Index-Slot-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-MasterDs1Index-Item-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-MasterDs1Index-Index-o"),
    (0, "ASCEND-MIBSTM1INT-MIB", "sTM1InterfaceProfile-PathParams-MasterDs1Index-Index1-o"),
)
if mibBuilder.loadTexts:
    mibsTM1InterfaceProfile_PathParams_MasterDs1IndexEntry.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o_Type = Integer32
_STM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o = _STM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20, 1, 1),
    _STM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o_Type()
)
sTM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o_Type = Integer32
_STM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o = _STM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20, 1, 2),
    _STM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o_Type()
)
sTM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_MasterDs1Index_Item_o_Type = Integer32
_STM1InterfaceProfile_PathParams_MasterDs1Index_Item_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_MasterDs1Index_Item_o = _STM1InterfaceProfile_PathParams_MasterDs1Index_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20, 1, 3),
    _STM1InterfaceProfile_PathParams_MasterDs1Index_Item_o_Type()
)
sTM1InterfaceProfile_PathParams_MasterDs1Index_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_MasterDs1Index_Item_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_MasterDs1Index_Index_o_Type = Integer32
_STM1InterfaceProfile_PathParams_MasterDs1Index_Index_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_MasterDs1Index_Index_o = _STM1InterfaceProfile_PathParams_MasterDs1Index_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20, 1, 4),
    _STM1InterfaceProfile_PathParams_MasterDs1Index_Index_o_Type()
)
sTM1InterfaceProfile_PathParams_MasterDs1Index_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_MasterDs1Index_Index_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o_Type = Integer32
_STM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o_Object = MibScalar
sTM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o = _STM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20, 1, 5),
    _STM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o_Type()
)
sTM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o.setStatus("mandatory")
_STM1InterfaceProfile_PathParams_MasterDs1Index_Type = Integer32
_STM1InterfaceProfile_PathParams_MasterDs1Index_Object = MibScalar
sTM1InterfaceProfile_PathParams_MasterDs1Index = _STM1InterfaceProfile_PathParams_MasterDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 154, 20, 1, 6),
    _STM1InterfaceProfile_PathParams_MasterDs1Index_Type()
)
sTM1InterfaceProfile_PathParams_MasterDs1Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sTM1InterfaceProfile_PathParams_MasterDs1Index.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSTM1INT-MIB",
    **{"DisplayString": DisplayString,
       "mibsTM1InterfaceProfile": mibsTM1InterfaceProfile,
       "mibsTM1InterfaceProfileTable": mibsTM1InterfaceProfileTable,
       "mibsTM1InterfaceProfileEntry": mibsTM1InterfaceProfileEntry,
       "sTM1InterfaceProfile-Shelf-o": sTM1InterfaceProfile_Shelf_o,
       "sTM1InterfaceProfile-Slot-o": sTM1InterfaceProfile_Slot_o,
       "sTM1InterfaceProfile-Item-o": sTM1InterfaceProfile_Item_o,
       "sTM1InterfaceProfile-Name": sTM1InterfaceProfile_Name,
       "sTM1InterfaceProfile-PhysicalAddress-Shelf": sTM1InterfaceProfile_PhysicalAddress_Shelf,
       "sTM1InterfaceProfile-PhysicalAddress-Slot": sTM1InterfaceProfile_PhysicalAddress_Slot,
       "sTM1InterfaceProfile-PhysicalAddress-ItemNumber": sTM1InterfaceProfile_PhysicalAddress_ItemNumber,
       "sTM1InterfaceProfile-LimControl-PrimaryLpm": sTM1InterfaceProfile_LimControl_PrimaryLpm,
       "sTM1InterfaceProfile-LimControl-ActiveLine": sTM1InterfaceProfile_LimControl_ActiveLine,
       "sTM1InterfaceProfile-LineParams-Name": sTM1InterfaceProfile_LineParams_Name,
       "sTM1InterfaceProfile-LineParams-PhysicalAddress-Shelf": sTM1InterfaceProfile_LineParams_PhysicalAddress_Shelf,
       "sTM1InterfaceProfile-LineParams-PhysicalAddress-Slot": sTM1InterfaceProfile_LineParams_PhysicalAddress_Slot,
       "sTM1InterfaceProfile-LineParams-PhysicalAddress-ItemNumber": sTM1InterfaceProfile_LineParams_PhysicalAddress_ItemNumber,
       "sTM1InterfaceProfile-LineParams-Enabled": sTM1InterfaceProfile_LineParams_Enabled,
       "sTM1InterfaceProfile-LineParams-AuPointer": sTM1InterfaceProfile_LineParams_AuPointer,
       "sTM1InterfaceProfile-LineParams-LoopTiming": sTM1InterfaceProfile_LineParams_LoopTiming,
       "sTM1InterfaceProfile-LineParams-Loopback": sTM1InterfaceProfile_LineParams_Loopback,
       "sTM1InterfaceProfile-Action-o": sTM1InterfaceProfile_Action_o,
       "sTM1InterfaceProfile-LineParams-ApsConfigName": sTM1InterfaceProfile_LineParams_ApsConfigName,
       "sTM1InterfaceProfile-LineParams-Signaling": sTM1InterfaceProfile_LineParams_Signaling,
       "mibsTM1InterfaceProfile-PathParamsTable": mibsTM1InterfaceProfile_PathParamsTable,
       "mibsTM1InterfaceProfile-PathParamsEntry": mibsTM1InterfaceProfile_PathParamsEntry,
       "sTM1InterfaceProfile-PathParams-Shelf-o": sTM1InterfaceProfile_PathParams_Shelf_o,
       "sTM1InterfaceProfile-PathParams-Slot-o": sTM1InterfaceProfile_PathParams_Slot_o,
       "sTM1InterfaceProfile-PathParams-Item-o": sTM1InterfaceProfile_PathParams_Item_o,
       "sTM1InterfaceProfile-PathParams-Index-o": sTM1InterfaceProfile_PathParams_Index_o,
       "sTM1InterfaceProfile-PathParams-Name": sTM1InterfaceProfile_PathParams_Name,
       "sTM1InterfaceProfile-PathParams-Stm0Profile-Name": sTM1InterfaceProfile_PathParams_Stm0Profile_Name,
       "sTM1InterfaceProfile-PathParams-Stm0Profile-PhysicalAddress-Shelf": sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Shelf,
       "sTM1InterfaceProfile-PathParams-Stm0Profile-PhysicalAddress-Slot": sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_Slot,
       "sTM1InterfaceProfile-PathParams-Stm0Profile-PhysicalAddress-ItemNumber": sTM1InterfaceProfile_PathParams_Stm0Profile_PhysicalAddress_ItemNumber,
       "sTM1InterfaceProfile-PathParams-Stm0Profile-Enabled": sTM1InterfaceProfile_PathParams_Stm0Profile_Enabled,
       "sTM1InterfaceProfile-PathParams-Stm0Profile-TributaryMapping": sTM1InterfaceProfile_PathParams_Stm0Profile_TributaryMapping,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-Name": sTM1InterfaceProfile_PathParams_Ds3Profile_Name,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-PhysicalAddress-Shelf": sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Shelf,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-PhysicalAddress-Slot": sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_Slot,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-PhysicalAddress-ItemNumber": sTM1InterfaceProfile_PathParams_Ds3Profile_PhysicalAddress_ItemNumber,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-Enabled": sTM1InterfaceProfile_PathParams_Ds3Profile_Enabled,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-FrameType": sTM1InterfaceProfile_PathParams_Ds3Profile_FrameType,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-LineLength": sTM1InterfaceProfile_PathParams_Ds3Profile_LineLength,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-Loopback": sTM1InterfaceProfile_PathParams_Ds3Profile_Loopback,
       "sTM1InterfaceProfile-PathParams-Ds3Profile-StatusChangeTrapEnable": sTM1InterfaceProfile_PathParams_Ds3Profile_StatusChangeTrapEnable,
       "mibsTM1InterfaceProfile-PathParams-MasterDs1IndexTable": mibsTM1InterfaceProfile_PathParams_MasterDs1IndexTable,
       "mibsTM1InterfaceProfile-PathParams-MasterDs1IndexEntry": mibsTM1InterfaceProfile_PathParams_MasterDs1IndexEntry,
       "sTM1InterfaceProfile-PathParams-MasterDs1Index-Shelf-o": sTM1InterfaceProfile_PathParams_MasterDs1Index_Shelf_o,
       "sTM1InterfaceProfile-PathParams-MasterDs1Index-Slot-o": sTM1InterfaceProfile_PathParams_MasterDs1Index_Slot_o,
       "sTM1InterfaceProfile-PathParams-MasterDs1Index-Item-o": sTM1InterfaceProfile_PathParams_MasterDs1Index_Item_o,
       "sTM1InterfaceProfile-PathParams-MasterDs1Index-Index-o": sTM1InterfaceProfile_PathParams_MasterDs1Index_Index_o,
       "sTM1InterfaceProfile-PathParams-MasterDs1Index-Index1-o": sTM1InterfaceProfile_PathParams_MasterDs1Index_Index1_o,
       "sTM1InterfaceProfile-PathParams-MasterDs1Index": sTM1InterfaceProfile_PathParams_MasterDs1Index}
)
