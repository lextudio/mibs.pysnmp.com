# SNMP MIB module (ASCEND-MIBATMSVCROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMSVCROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:14 2024
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

_MibatmSvcRouteProfile_ObjectIdentity = ObjectIdentity
mibatmSvcRouteProfile = _MibatmSvcRouteProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 55)
)
_MibatmSvcRouteProfileTable_Object = MibTable
mibatmSvcRouteProfileTable = _MibatmSvcRouteProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1)
)
if mibBuilder.loadTexts:
    mibatmSvcRouteProfileTable.setStatus("mandatory")
_MibatmSvcRouteProfileEntry_Object = MibTableRow
mibatmSvcRouteProfileEntry = _MibatmSvcRouteProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1)
)
mibatmSvcRouteProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMSVCROUTE-MIB", "atmSvcRouteProfile-Name"),
)
if mibBuilder.loadTexts:
    mibatmSvcRouteProfileEntry.setStatus("mandatory")
_AtmSvcRouteProfile_Name_Type = DisplayString
_AtmSvcRouteProfile_Name_Object = MibScalar
atmSvcRouteProfile_Name = _AtmSvcRouteProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 1),
    _AtmSvcRouteProfile_Name_Type()
)
atmSvcRouteProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_Name.setStatus("mandatory")


class _AtmSvcRouteProfile_Active_Type(Integer32):
    """Custom type atmSvcRouteProfile_Active based on Integer32"""
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


_AtmSvcRouteProfile_Active_Type.__name__ = "Integer32"
_AtmSvcRouteProfile_Active_Object = MibScalar
atmSvcRouteProfile_Active = _AtmSvcRouteProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 2),
    _AtmSvcRouteProfile_Active_Type()
)
atmSvcRouteProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_Active.setStatus("mandatory")
_AtmSvcRouteProfile_AddressPrefix_Type = DisplayString
_AtmSvcRouteProfile_AddressPrefix_Object = MibScalar
atmSvcRouteProfile_AddressPrefix = _AtmSvcRouteProfile_AddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 3),
    _AtmSvcRouteProfile_AddressPrefix_Type()
)
atmSvcRouteProfile_AddressPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_AddressPrefix.setStatus("mandatory")


class _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf based on Integer32"""
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


_AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf_Object = MibScalar
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf = _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 4),
    _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf_Type()
)
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot based on Integer32"""
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


_AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot_Object = MibScalar
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot = _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 5),
    _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot_Type()
)
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus("mandatory")
_AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type = Integer32
_AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object = MibScalar
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber = _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 6),
    _AtmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type()
)
atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmSvcRouteProfile_InterfaceAddress_LogicalItem_Type = Integer32
_AtmSvcRouteProfile_InterfaceAddress_LogicalItem_Object = MibScalar
atmSvcRouteProfile_InterfaceAddress_LogicalItem = _AtmSvcRouteProfile_InterfaceAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 7),
    _AtmSvcRouteProfile_InterfaceAddress_LogicalItem_Type()
)
atmSvcRouteProfile_InterfaceAddress_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_InterfaceAddress_LogicalItem.setStatus("mandatory")


class _AtmSvcRouteProfile_Action_o_Type(Integer32):
    """Custom type atmSvcRouteProfile_Action_o based on Integer32"""
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


_AtmSvcRouteProfile_Action_o_Type.__name__ = "Integer32"
_AtmSvcRouteProfile_Action_o_Object = MibScalar
atmSvcRouteProfile_Action_o = _AtmSvcRouteProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 55, 1, 1, 8),
    _AtmSvcRouteProfile_Action_o_Type()
)
atmSvcRouteProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcRouteProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMSVCROUTE-MIB",
    **{"DisplayString": DisplayString,
       "mibatmSvcRouteProfile": mibatmSvcRouteProfile,
       "mibatmSvcRouteProfileTable": mibatmSvcRouteProfileTable,
       "mibatmSvcRouteProfileEntry": mibatmSvcRouteProfileEntry,
       "atmSvcRouteProfile-Name": atmSvcRouteProfile_Name,
       "atmSvcRouteProfile-Active": atmSvcRouteProfile_Active,
       "atmSvcRouteProfile-AddressPrefix": atmSvcRouteProfile_AddressPrefix,
       "atmSvcRouteProfile-InterfaceAddress-PhysicalAddress-Shelf": atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Shelf,
       "atmSvcRouteProfile-InterfaceAddress-PhysicalAddress-Slot": atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_Slot,
       "atmSvcRouteProfile-InterfaceAddress-PhysicalAddress-ItemNumber": atmSvcRouteProfile_InterfaceAddress_PhysicalAddress_ItemNumber,
       "atmSvcRouteProfile-InterfaceAddress-LogicalItem": atmSvcRouteProfile_InterfaceAddress_LogicalItem,
       "atmSvcRouteProfile-Action-o": atmSvcRouteProfile_Action_o}
)
