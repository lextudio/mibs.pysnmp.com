# SNMP MIB module (ASCEND-MIBATMSPVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMSPVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:13 2024
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

_MibatmSpvcConfigProfile_ObjectIdentity = ObjectIdentity
mibatmSpvcConfigProfile = _MibatmSpvcConfigProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 53)
)
_MibatmSpvcConfigProfileTable_Object = MibTable
mibatmSpvcConfigProfileTable = _MibatmSpvcConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 53, 1)
)
if mibBuilder.loadTexts:
    mibatmSpvcConfigProfileTable.setStatus("mandatory")
_MibatmSpvcConfigProfileEntry_Object = MibTableRow
mibatmSpvcConfigProfileEntry = _MibatmSpvcConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 53, 1, 1)
)
mibatmSpvcConfigProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMSPVC-MIB", "atmSpvcConfigProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibatmSpvcConfigProfileEntry.setStatus("mandatory")
_AtmSpvcConfigProfile_Index_o_Type = Integer32
_AtmSpvcConfigProfile_Index_o_Object = MibScalar
atmSpvcConfigProfile_Index_o = _AtmSpvcConfigProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 53, 1, 1, 1),
    _AtmSpvcConfigProfile_Index_o_Type()
)
atmSpvcConfigProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSpvcConfigProfile_Index_o.setStatus("mandatory")


class _AtmSpvcConfigProfile_FailureTrapEnable_Type(Integer32):
    """Custom type atmSpvcConfigProfile_FailureTrapEnable based on Integer32"""
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


_AtmSpvcConfigProfile_FailureTrapEnable_Type.__name__ = "Integer32"
_AtmSpvcConfigProfile_FailureTrapEnable_Object = MibScalar
atmSpvcConfigProfile_FailureTrapEnable = _AtmSpvcConfigProfile_FailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 53, 1, 1, 2),
    _AtmSpvcConfigProfile_FailureTrapEnable_Type()
)
atmSpvcConfigProfile_FailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSpvcConfigProfile_FailureTrapEnable.setStatus("mandatory")
_AtmSpvcConfigProfile_FailureNotificationInterval_Type = Integer32
_AtmSpvcConfigProfile_FailureNotificationInterval_Object = MibScalar
atmSpvcConfigProfile_FailureNotificationInterval = _AtmSpvcConfigProfile_FailureNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 53, 1, 1, 3),
    _AtmSpvcConfigProfile_FailureNotificationInterval_Type()
)
atmSpvcConfigProfile_FailureNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSpvcConfigProfile_FailureNotificationInterval.setStatus("mandatory")


class _AtmSpvcConfigProfile_Action_o_Type(Integer32):
    """Custom type atmSpvcConfigProfile_Action_o based on Integer32"""
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


_AtmSpvcConfigProfile_Action_o_Type.__name__ = "Integer32"
_AtmSpvcConfigProfile_Action_o_Object = MibScalar
atmSpvcConfigProfile_Action_o = _AtmSpvcConfigProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 53, 1, 1, 4),
    _AtmSpvcConfigProfile_Action_o_Type()
)
atmSpvcConfigProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSpvcConfigProfile_Action_o.setStatus("mandatory")
_MibatmSoftPVcAddrProfile_ObjectIdentity = ObjectIdentity
mibatmSoftPVcAddrProfile = _MibatmSoftPVcAddrProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 54)
)
_MibatmSoftPVcAddrProfileTable_Object = MibTable
mibatmSoftPVcAddrProfileTable = _MibatmSoftPVcAddrProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1)
)
if mibBuilder.loadTexts:
    mibatmSoftPVcAddrProfileTable.setStatus("mandatory")
_MibatmSoftPVcAddrProfileEntry_Object = MibTableRow
mibatmSoftPVcAddrProfileEntry = _MibatmSoftPVcAddrProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1)
)
mibatmSoftPVcAddrProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMSPVC-MIB", "atmSoftPVcAddrProfile-Shelf-o"),
    (0, "ASCEND-MIBATMSPVC-MIB", "atmSoftPVcAddrProfile-Slot-o"),
    (0, "ASCEND-MIBATMSPVC-MIB", "atmSoftPVcAddrProfile-Item-o"),
    (0, "ASCEND-MIBATMSPVC-MIB", "atmSoftPVcAddrProfile-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibatmSoftPVcAddrProfileEntry.setStatus("mandatory")
_AtmSoftPVcAddrProfile_Shelf_o_Type = Integer32
_AtmSoftPVcAddrProfile_Shelf_o_Object = MibScalar
atmSoftPVcAddrProfile_Shelf_o = _AtmSoftPVcAddrProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 1),
    _AtmSoftPVcAddrProfile_Shelf_o_Type()
)
atmSoftPVcAddrProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Shelf_o.setStatus("mandatory")
_AtmSoftPVcAddrProfile_Slot_o_Type = Integer32
_AtmSoftPVcAddrProfile_Slot_o_Object = MibScalar
atmSoftPVcAddrProfile_Slot_o = _AtmSoftPVcAddrProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 2),
    _AtmSoftPVcAddrProfile_Slot_o_Type()
)
atmSoftPVcAddrProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Slot_o.setStatus("mandatory")
_AtmSoftPVcAddrProfile_Item_o_Type = Integer32
_AtmSoftPVcAddrProfile_Item_o_Object = MibScalar
atmSoftPVcAddrProfile_Item_o = _AtmSoftPVcAddrProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 3),
    _AtmSoftPVcAddrProfile_Item_o_Type()
)
atmSoftPVcAddrProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Item_o.setStatus("mandatory")
_AtmSoftPVcAddrProfile_LogicalItem_o_Type = Integer32
_AtmSoftPVcAddrProfile_LogicalItem_o_Object = MibScalar
atmSoftPVcAddrProfile_LogicalItem_o = _AtmSoftPVcAddrProfile_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 4),
    _AtmSoftPVcAddrProfile_LogicalItem_o_Type()
)
atmSoftPVcAddrProfile_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_LogicalItem_o.setStatus("mandatory")


class _AtmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf based on Integer32"""
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


_AtmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf_Object = MibScalar
atmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf = _AtmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 5),
    _AtmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf_Type()
)
atmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtmSoftPVcAddrProfile_Index_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atmSoftPVcAddrProfile_Index_PhysicalAddress_Slot based on Integer32"""
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


_AtmSoftPVcAddrProfile_Index_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtmSoftPVcAddrProfile_Index_PhysicalAddress_Slot_Object = MibScalar
atmSoftPVcAddrProfile_Index_PhysicalAddress_Slot = _AtmSoftPVcAddrProfile_Index_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 6),
    _AtmSoftPVcAddrProfile_Index_PhysicalAddress_Slot_Type()
)
atmSoftPVcAddrProfile_Index_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Index_PhysicalAddress_Slot.setStatus("mandatory")
_AtmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber_Type = Integer32
_AtmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber_Object = MibScalar
atmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber = _AtmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 7),
    _AtmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber_Type()
)
atmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmSoftPVcAddrProfile_Index_LogicalItem_Type = Integer32
_AtmSoftPVcAddrProfile_Index_LogicalItem_Object = MibScalar
atmSoftPVcAddrProfile_Index_LogicalItem = _AtmSoftPVcAddrProfile_Index_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 8),
    _AtmSoftPVcAddrProfile_Index_LogicalItem_Type()
)
atmSoftPVcAddrProfile_Index_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Index_LogicalItem.setStatus("mandatory")
_AtmSoftPVcAddrProfile_SpvcAtmAddress_Type = DisplayString
_AtmSoftPVcAddrProfile_SpvcAtmAddress_Object = MibScalar
atmSoftPVcAddrProfile_SpvcAtmAddress = _AtmSoftPVcAddrProfile_SpvcAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 9),
    _AtmSoftPVcAddrProfile_SpvcAtmAddress_Type()
)
atmSoftPVcAddrProfile_SpvcAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_SpvcAtmAddress.setStatus("mandatory")


class _AtmSoftPVcAddrProfile_Action_o_Type(Integer32):
    """Custom type atmSoftPVcAddrProfile_Action_o based on Integer32"""
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


_AtmSoftPVcAddrProfile_Action_o_Type.__name__ = "Integer32"
_AtmSoftPVcAddrProfile_Action_o_Object = MibScalar
atmSoftPVcAddrProfile_Action_o = _AtmSoftPVcAddrProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 54, 1, 1, 10),
    _AtmSoftPVcAddrProfile_Action_o_Type()
)
atmSoftPVcAddrProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSoftPVcAddrProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMSPVC-MIB",
    **{"DisplayString": DisplayString,
       "mibatmSpvcConfigProfile": mibatmSpvcConfigProfile,
       "mibatmSpvcConfigProfileTable": mibatmSpvcConfigProfileTable,
       "mibatmSpvcConfigProfileEntry": mibatmSpvcConfigProfileEntry,
       "atmSpvcConfigProfile-Index-o": atmSpvcConfigProfile_Index_o,
       "atmSpvcConfigProfile-FailureTrapEnable": atmSpvcConfigProfile_FailureTrapEnable,
       "atmSpvcConfigProfile-FailureNotificationInterval": atmSpvcConfigProfile_FailureNotificationInterval,
       "atmSpvcConfigProfile-Action-o": atmSpvcConfigProfile_Action_o,
       "mibatmSoftPVcAddrProfile": mibatmSoftPVcAddrProfile,
       "mibatmSoftPVcAddrProfileTable": mibatmSoftPVcAddrProfileTable,
       "mibatmSoftPVcAddrProfileEntry": mibatmSoftPVcAddrProfileEntry,
       "atmSoftPVcAddrProfile-Shelf-o": atmSoftPVcAddrProfile_Shelf_o,
       "atmSoftPVcAddrProfile-Slot-o": atmSoftPVcAddrProfile_Slot_o,
       "atmSoftPVcAddrProfile-Item-o": atmSoftPVcAddrProfile_Item_o,
       "atmSoftPVcAddrProfile-LogicalItem-o": atmSoftPVcAddrProfile_LogicalItem_o,
       "atmSoftPVcAddrProfile-Index-PhysicalAddress-Shelf": atmSoftPVcAddrProfile_Index_PhysicalAddress_Shelf,
       "atmSoftPVcAddrProfile-Index-PhysicalAddress-Slot": atmSoftPVcAddrProfile_Index_PhysicalAddress_Slot,
       "atmSoftPVcAddrProfile-Index-PhysicalAddress-ItemNumber": atmSoftPVcAddrProfile_Index_PhysicalAddress_ItemNumber,
       "atmSoftPVcAddrProfile-Index-LogicalItem": atmSoftPVcAddrProfile_Index_LogicalItem,
       "atmSoftPVcAddrProfile-SpvcAtmAddress": atmSoftPVcAddrProfile_SpvcAtmAddress,
       "atmSoftPVcAddrProfile-Action-o": atmSoftPVcAddrProfile_Action_o}
)
