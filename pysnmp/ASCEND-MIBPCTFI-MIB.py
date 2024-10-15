# SNMP MIB module (ASCEND-MIBPCTFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBPCTFI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:00 2024
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

_MibpctfiNetworkProfile_ObjectIdentity = ObjectIdentity
mibpctfiNetworkProfile = _MibpctfiNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 18)
)
_MibpctfiNetworkProfileTable_Object = MibTable
mibpctfiNetworkProfileTable = _MibpctfiNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1)
)
if mibBuilder.loadTexts:
    mibpctfiNetworkProfileTable.setStatus("mandatory")
_MibpctfiNetworkProfileEntry_Object = MibTableRow
mibpctfiNetworkProfileEntry = _MibpctfiNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1)
)
mibpctfiNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBPCTFI-MIB", "pctfiNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBPCTFI-MIB", "pctfiNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBPCTFI-MIB", "pctfiNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibpctfiNetworkProfileEntry.setStatus("mandatory")
_PctfiNetworkProfile_Shelf_o_Type = Integer32
_PctfiNetworkProfile_Shelf_o_Object = MibScalar
pctfiNetworkProfile_Shelf_o = _PctfiNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 1),
    _PctfiNetworkProfile_Shelf_o_Type()
)
pctfiNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_Shelf_o.setStatus("mandatory")
_PctfiNetworkProfile_Slot_o_Type = Integer32
_PctfiNetworkProfile_Slot_o_Object = MibScalar
pctfiNetworkProfile_Slot_o = _PctfiNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 2),
    _PctfiNetworkProfile_Slot_o_Type()
)
pctfiNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_Slot_o.setStatus("mandatory")
_PctfiNetworkProfile_Item_o_Type = Integer32
_PctfiNetworkProfile_Item_o_Object = MibScalar
pctfiNetworkProfile_Item_o = _PctfiNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 3),
    _PctfiNetworkProfile_Item_o_Type()
)
pctfiNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_Item_o.setStatus("mandatory")
_PctfiNetworkProfile_Name_Type = DisplayString
_PctfiNetworkProfile_Name_Object = MibScalar
pctfiNetworkProfile_Name = _PctfiNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 4),
    _PctfiNetworkProfile_Name_Type()
)
pctfiNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_Name.setStatus("mandatory")


class _PctfiNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type pctfiNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_PctfiNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_PctfiNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
pctfiNetworkProfile_PhysicalAddress_Shelf = _PctfiNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 5),
    _PctfiNetworkProfile_PhysicalAddress_Shelf_Type()
)
pctfiNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _PctfiNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type pctfiNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_PctfiNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_PctfiNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
pctfiNetworkProfile_PhysicalAddress_Slot = _PctfiNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 6),
    _PctfiNetworkProfile_PhysicalAddress_Slot_Type()
)
pctfiNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_PctfiNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_PctfiNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
pctfiNetworkProfile_PhysicalAddress_ItemNumber = _PctfiNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 7),
    _PctfiNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
pctfiNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _PctfiNetworkProfile_Enabled_Type(Integer32):
    """Custom type pctfiNetworkProfile_Enabled based on Integer32"""
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


_PctfiNetworkProfile_Enabled_Type.__name__ = "Integer32"
_PctfiNetworkProfile_Enabled_Object = MibScalar
pctfiNetworkProfile_Enabled = _PctfiNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 8),
    _PctfiNetworkProfile_Enabled_Type()
)
pctfiNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_Enabled.setStatus("mandatory")


class _PctfiNetworkProfile_InterfaceVersion_Type(Integer32):
    """Custom type pctfiNetworkProfile_InterfaceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("firstOffice", 2),
          ("pelts", 16))
    )


_PctfiNetworkProfile_InterfaceVersion_Type.__name__ = "Integer32"
_PctfiNetworkProfile_InterfaceVersion_Object = MibScalar
pctfiNetworkProfile_InterfaceVersion = _PctfiNetworkProfile_InterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 9),
    _PctfiNetworkProfile_InterfaceVersion_Type()
)
pctfiNetworkProfile_InterfaceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_InterfaceVersion.setStatus("mandatory")
_PctfiNetworkProfile_TraceId0_Type = Integer32
_PctfiNetworkProfile_TraceId0_Object = MibScalar
pctfiNetworkProfile_TraceId0 = _PctfiNetworkProfile_TraceId0_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 10),
    _PctfiNetworkProfile_TraceId0_Type()
)
pctfiNetworkProfile_TraceId0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_TraceId0.setStatus("mandatory")
_PctfiNetworkProfile_TraceId1_Type = Integer32
_PctfiNetworkProfile_TraceId1_Object = MibScalar
pctfiNetworkProfile_TraceId1 = _PctfiNetworkProfile_TraceId1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 11),
    _PctfiNetworkProfile_TraceId1_Type()
)
pctfiNetworkProfile_TraceId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_TraceId1.setStatus("mandatory")


class _PctfiNetworkProfile_Mode_Type(Integer32):
    """Custom type pctfiNetworkProfile_Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_PctfiNetworkProfile_Mode_Type.__name__ = "Integer32"
_PctfiNetworkProfile_Mode_Object = MibScalar
pctfiNetworkProfile_Mode = _PctfiNetworkProfile_Mode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 12),
    _PctfiNetworkProfile_Mode_Type()
)
pctfiNetworkProfile_Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_Mode.setStatus("mandatory")


class _PctfiNetworkProfile_Action_o_Type(Integer32):
    """Custom type pctfiNetworkProfile_Action_o based on Integer32"""
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


_PctfiNetworkProfile_Action_o_Type.__name__ = "Integer32"
_PctfiNetworkProfile_Action_o_Object = MibScalar
pctfiNetworkProfile_Action_o = _PctfiNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 18, 1, 1, 13),
    _PctfiNetworkProfile_Action_o_Type()
)
pctfiNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pctfiNetworkProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBPCTFI-MIB",
    **{"DisplayString": DisplayString,
       "mibpctfiNetworkProfile": mibpctfiNetworkProfile,
       "mibpctfiNetworkProfileTable": mibpctfiNetworkProfileTable,
       "mibpctfiNetworkProfileEntry": mibpctfiNetworkProfileEntry,
       "pctfiNetworkProfile-Shelf-o": pctfiNetworkProfile_Shelf_o,
       "pctfiNetworkProfile-Slot-o": pctfiNetworkProfile_Slot_o,
       "pctfiNetworkProfile-Item-o": pctfiNetworkProfile_Item_o,
       "pctfiNetworkProfile-Name": pctfiNetworkProfile_Name,
       "pctfiNetworkProfile-PhysicalAddress-Shelf": pctfiNetworkProfile_PhysicalAddress_Shelf,
       "pctfiNetworkProfile-PhysicalAddress-Slot": pctfiNetworkProfile_PhysicalAddress_Slot,
       "pctfiNetworkProfile-PhysicalAddress-ItemNumber": pctfiNetworkProfile_PhysicalAddress_ItemNumber,
       "pctfiNetworkProfile-Enabled": pctfiNetworkProfile_Enabled,
       "pctfiNetworkProfile-InterfaceVersion": pctfiNetworkProfile_InterfaceVersion,
       "pctfiNetworkProfile-TraceId0": pctfiNetworkProfile_TraceId0,
       "pctfiNetworkProfile-TraceId1": pctfiNetworkProfile_TraceId1,
       "pctfiNetworkProfile-Mode": pctfiNetworkProfile_Mode,
       "pctfiNetworkProfile-Action-o": pctfiNetworkProfile_Action_o}
)
