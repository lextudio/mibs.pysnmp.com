# SNMP MIB module (ASCEND-MIBDS3NET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDS3NET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:31 2024
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

_MibdS3NetworkProfile_ObjectIdentity = ObjectIdentity
mibdS3NetworkProfile = _MibdS3NetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 4)
)
_MibdS3NetworkProfileTable_Object = MibTable
mibdS3NetworkProfileTable = _MibdS3NetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1)
)
if mibBuilder.loadTexts:
    mibdS3NetworkProfileTable.setStatus("mandatory")
_MibdS3NetworkProfileEntry_Object = MibTableRow
mibdS3NetworkProfileEntry = _MibdS3NetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1)
)
mibdS3NetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDS3NET-MIB", "dS3NetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBDS3NET-MIB", "dS3NetworkProfile-Slot-o"),
    (0, "ASCEND-MIBDS3NET-MIB", "dS3NetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibdS3NetworkProfileEntry.setStatus("mandatory")
_DS3NetworkProfile_Shelf_o_Type = Integer32
_DS3NetworkProfile_Shelf_o_Object = MibScalar
dS3NetworkProfile_Shelf_o = _DS3NetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 1),
    _DS3NetworkProfile_Shelf_o_Type()
)
dS3NetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dS3NetworkProfile_Shelf_o.setStatus("mandatory")
_DS3NetworkProfile_Slot_o_Type = Integer32
_DS3NetworkProfile_Slot_o_Object = MibScalar
dS3NetworkProfile_Slot_o = _DS3NetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 2),
    _DS3NetworkProfile_Slot_o_Type()
)
dS3NetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dS3NetworkProfile_Slot_o.setStatus("mandatory")
_DS3NetworkProfile_Item_o_Type = Integer32
_DS3NetworkProfile_Item_o_Object = MibScalar
dS3NetworkProfile_Item_o = _DS3NetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 3),
    _DS3NetworkProfile_Item_o_Type()
)
dS3NetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dS3NetworkProfile_Item_o.setStatus("mandatory")
_DS3NetworkProfile_Name_Type = DisplayString
_DS3NetworkProfile_Name_Object = MibScalar
dS3NetworkProfile_Name = _DS3NetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 4),
    _DS3NetworkProfile_Name_Type()
)
dS3NetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_Name.setStatus("mandatory")


class _DS3NetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type dS3NetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_DS3NetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DS3NetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
dS3NetworkProfile_PhysicalAddress_Shelf = _DS3NetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 5),
    _DS3NetworkProfile_PhysicalAddress_Shelf_Type()
)
dS3NetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _DS3NetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type dS3NetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_DS3NetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_DS3NetworkProfile_PhysicalAddress_Slot_Object = MibScalar
dS3NetworkProfile_PhysicalAddress_Slot = _DS3NetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 6),
    _DS3NetworkProfile_PhysicalAddress_Slot_Type()
)
dS3NetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_DS3NetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_DS3NetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
dS3NetworkProfile_PhysicalAddress_ItemNumber = _DS3NetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 7),
    _DS3NetworkProfile_PhysicalAddress_ItemNumber_Type()
)
dS3NetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _DS3NetworkProfile_Enabled_Type(Integer32):
    """Custom type dS3NetworkProfile_Enabled based on Integer32"""
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


_DS3NetworkProfile_Enabled_Type.__name__ = "Integer32"
_DS3NetworkProfile_Enabled_Object = MibScalar
dS3NetworkProfile_Enabled = _DS3NetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 8),
    _DS3NetworkProfile_Enabled_Type()
)
dS3NetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_Enabled.setStatus("mandatory")


class _DS3NetworkProfile_FrameType_Type(Integer32):
    """Custom type dS3NetworkProfile_FrameType based on Integer32"""
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


_DS3NetworkProfile_FrameType_Type.__name__ = "Integer32"
_DS3NetworkProfile_FrameType_Object = MibScalar
dS3NetworkProfile_FrameType = _DS3NetworkProfile_FrameType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 9),
    _DS3NetworkProfile_FrameType_Type()
)
dS3NetworkProfile_FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_FrameType.setStatus("mandatory")


class _DS3NetworkProfile_LineLength_Type(Integer32):
    """Custom type dS3NetworkProfile_LineLength based on Integer32"""
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


_DS3NetworkProfile_LineLength_Type.__name__ = "Integer32"
_DS3NetworkProfile_LineLength_Object = MibScalar
dS3NetworkProfile_LineLength = _DS3NetworkProfile_LineLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 10),
    _DS3NetworkProfile_LineLength_Type()
)
dS3NetworkProfile_LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_LineLength.setStatus("mandatory")


class _DS3NetworkProfile_Action_o_Type(Integer32):
    """Custom type dS3NetworkProfile_Action_o based on Integer32"""
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


_DS3NetworkProfile_Action_o_Type.__name__ = "Integer32"
_DS3NetworkProfile_Action_o_Object = MibScalar
dS3NetworkProfile_Action_o = _DS3NetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 11),
    _DS3NetworkProfile_Action_o_Type()
)
dS3NetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_Action_o.setStatus("mandatory")


class _DS3NetworkProfile_Loopback_Type(Integer32):
    """Custom type dS3NetworkProfile_Loopback based on Integer32"""
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


_DS3NetworkProfile_Loopback_Type.__name__ = "Integer32"
_DS3NetworkProfile_Loopback_Object = MibScalar
dS3NetworkProfile_Loopback = _DS3NetworkProfile_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 12),
    _DS3NetworkProfile_Loopback_Type()
)
dS3NetworkProfile_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_Loopback.setStatus("mandatory")


class _DS3NetworkProfile_StatusChangeTrapEnable_Type(Integer32):
    """Custom type dS3NetworkProfile_StatusChangeTrapEnable based on Integer32"""
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


_DS3NetworkProfile_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_DS3NetworkProfile_StatusChangeTrapEnable_Object = MibScalar
dS3NetworkProfile_StatusChangeTrapEnable = _DS3NetworkProfile_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 4, 1, 1, 13),
    _DS3NetworkProfile_StatusChangeTrapEnable_Type()
)
dS3NetworkProfile_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dS3NetworkProfile_StatusChangeTrapEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDS3NET-MIB",
    **{"DisplayString": DisplayString,
       "mibdS3NetworkProfile": mibdS3NetworkProfile,
       "mibdS3NetworkProfileTable": mibdS3NetworkProfileTable,
       "mibdS3NetworkProfileEntry": mibdS3NetworkProfileEntry,
       "dS3NetworkProfile-Shelf-o": dS3NetworkProfile_Shelf_o,
       "dS3NetworkProfile-Slot-o": dS3NetworkProfile_Slot_o,
       "dS3NetworkProfile-Item-o": dS3NetworkProfile_Item_o,
       "dS3NetworkProfile-Name": dS3NetworkProfile_Name,
       "dS3NetworkProfile-PhysicalAddress-Shelf": dS3NetworkProfile_PhysicalAddress_Shelf,
       "dS3NetworkProfile-PhysicalAddress-Slot": dS3NetworkProfile_PhysicalAddress_Slot,
       "dS3NetworkProfile-PhysicalAddress-ItemNumber": dS3NetworkProfile_PhysicalAddress_ItemNumber,
       "dS3NetworkProfile-Enabled": dS3NetworkProfile_Enabled,
       "dS3NetworkProfile-FrameType": dS3NetworkProfile_FrameType,
       "dS3NetworkProfile-LineLength": dS3NetworkProfile_LineLength,
       "dS3NetworkProfile-Action-o": dS3NetworkProfile_Action_o,
       "dS3NetworkProfile-Loopback": dS3NetworkProfile_Loopback,
       "dS3NetworkProfile-StatusChangeTrapEnable": dS3NetworkProfile_StatusChangeTrapEnable}
)
