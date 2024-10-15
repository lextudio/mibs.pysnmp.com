# SNMP MIB module (ASCEND-MIBIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:43 2024
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

_MibipInterfaceProfile_ObjectIdentity = ObjectIdentity
mibipInterfaceProfile = _MibipInterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 82)
)
_MibipInterfaceProfileTable_Object = MibTable
mibipInterfaceProfileTable = _MibipInterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1)
)
if mibBuilder.loadTexts:
    mibipInterfaceProfileTable.setStatus("mandatory")
_MibipInterfaceProfileEntry_Object = MibTableRow
mibipInterfaceProfileEntry = _MibipInterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1)
)
mibipInterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipInterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBIP-MIB", "ipInterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBIP-MIB", "ipInterfaceProfile-Item-o"),
    (0, "ASCEND-MIBIP-MIB", "ipInterfaceProfile-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibipInterfaceProfileEntry.setStatus("mandatory")
_IpInterfaceProfile_Shelf_o_Type = Integer32
_IpInterfaceProfile_Shelf_o_Object = MibScalar
ipInterfaceProfile_Shelf_o = _IpInterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 1),
    _IpInterfaceProfile_Shelf_o_Type()
)
ipInterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Shelf_o.setStatus("mandatory")
_IpInterfaceProfile_Slot_o_Type = Integer32
_IpInterfaceProfile_Slot_o_Object = MibScalar
ipInterfaceProfile_Slot_o = _IpInterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 2),
    _IpInterfaceProfile_Slot_o_Type()
)
ipInterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Slot_o.setStatus("mandatory")
_IpInterfaceProfile_Item_o_Type = Integer32
_IpInterfaceProfile_Item_o_Object = MibScalar
ipInterfaceProfile_Item_o = _IpInterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 3),
    _IpInterfaceProfile_Item_o_Type()
)
ipInterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Item_o.setStatus("mandatory")
_IpInterfaceProfile_LogicalItem_o_Type = Integer32
_IpInterfaceProfile_LogicalItem_o_Object = MibScalar
ipInterfaceProfile_LogicalItem_o = _IpInterfaceProfile_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 4),
    _IpInterfaceProfile_LogicalItem_o_Type()
)
ipInterfaceProfile_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceProfile_LogicalItem_o.setStatus("mandatory")


class _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf based on Integer32"""
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


_IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object = MibScalar
ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf = _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 5),
    _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type()
)
ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus("mandatory")


class _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot based on Integer32"""
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


_IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object = MibScalar
ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot = _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 6),
    _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type()
)
ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus("mandatory")
_IpInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type = Integer32
_IpInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object = MibScalar
ipInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber = _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 7),
    _IpInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type()
)
ipInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_IpInterfaceProfile_InterfaceAddress_LogicalItem_Type = Integer32
_IpInterfaceProfile_InterfaceAddress_LogicalItem_Object = MibScalar
ipInterfaceProfile_InterfaceAddress_LogicalItem = _IpInterfaceProfile_InterfaceAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 8),
    _IpInterfaceProfile_InterfaceAddress_LogicalItem_Type()
)
ipInterfaceProfile_InterfaceAddress_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_InterfaceAddress_LogicalItem.setStatus("mandatory")
_IpInterfaceProfile_IpAddress_Type = IpAddress
_IpInterfaceProfile_IpAddress_Object = MibScalar
ipInterfaceProfile_IpAddress = _IpInterfaceProfile_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 9),
    _IpInterfaceProfile_IpAddress_Type()
)
ipInterfaceProfile_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_IpAddress.setStatus("mandatory")
_IpInterfaceProfile_o2ndIpAddress_Type = IpAddress
_IpInterfaceProfile_o2ndIpAddress_Object = MibScalar
ipInterfaceProfile_o2ndIpAddress = _IpInterfaceProfile_o2ndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 10),
    _IpInterfaceProfile_o2ndIpAddress_Type()
)
ipInterfaceProfile_o2ndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_o2ndIpAddress.setStatus("mandatory")


class _IpInterfaceProfile_ProxyMode_Type(Integer32):
    """Custom type ipInterfaceProfile_ProxyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("always", 4),
          ("inactive", 3),
          ("off", 1))
    )


_IpInterfaceProfile_ProxyMode_Type.__name__ = "Integer32"
_IpInterfaceProfile_ProxyMode_Object = MibScalar
ipInterfaceProfile_ProxyMode = _IpInterfaceProfile_ProxyMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 11),
    _IpInterfaceProfile_ProxyMode_Type()
)
ipInterfaceProfile_ProxyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_ProxyMode.setStatus("mandatory")


class _IpInterfaceProfile_RipMode_Type(Integer32):
    """Custom type ipInterfaceProfile_RipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("routingOff", 1),
          ("routingRecvOnly", 3),
          ("routingRecvOnlyV2", 6),
          ("routingSendAndRecv", 4),
          ("routingSendAndRecvV2", 7),
          ("routingSendOnly", 2),
          ("routingSendOnlyV2", 5))
    )


_IpInterfaceProfile_RipMode_Type.__name__ = "Integer32"
_IpInterfaceProfile_RipMode_Object = MibScalar
ipInterfaceProfile_RipMode = _IpInterfaceProfile_RipMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 12),
    _IpInterfaceProfile_RipMode_Type()
)
ipInterfaceProfile_RipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_RipMode.setStatus("mandatory")


class _IpInterfaceProfile_o2ndRipMode_Type(Integer32):
    """Custom type ipInterfaceProfile_o2ndRipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("routingOff", 1),
          ("routingRecvOnly", 3),
          ("routingRecvOnlyV2", 6),
          ("routingSendAndRecv", 4),
          ("routingSendAndRecvV2", 7),
          ("routingSendOnly", 2),
          ("routingSendOnlyV2", 5))
    )


_IpInterfaceProfile_o2ndRipMode_Type.__name__ = "Integer32"
_IpInterfaceProfile_o2ndRipMode_Object = MibScalar
ipInterfaceProfile_o2ndRipMode = _IpInterfaceProfile_o2ndRipMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 13),
    _IpInterfaceProfile_o2ndRipMode_Type()
)
ipInterfaceProfile_o2ndRipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_o2ndRipMode.setStatus("mandatory")
_IpInterfaceProfile_RouteFilter_Type = DisplayString
_IpInterfaceProfile_RouteFilter_Object = MibScalar
ipInterfaceProfile_RouteFilter = _IpInterfaceProfile_RouteFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 14),
    _IpInterfaceProfile_RouteFilter_Type()
)
ipInterfaceProfile_RouteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_RouteFilter.setStatus("mandatory")


class _IpInterfaceProfile_Rip2UseMulticast_Type(Integer32):
    """Custom type ipInterfaceProfile_Rip2UseMulticast based on Integer32"""
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


_IpInterfaceProfile_Rip2UseMulticast_Type.__name__ = "Integer32"
_IpInterfaceProfile_Rip2UseMulticast_Object = MibScalar
ipInterfaceProfile_Rip2UseMulticast = _IpInterfaceProfile_Rip2UseMulticast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 15),
    _IpInterfaceProfile_Rip2UseMulticast_Type()
)
ipInterfaceProfile_Rip2UseMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Rip2UseMulticast.setStatus("mandatory")


class _IpInterfaceProfile_Ospf_Active_Type(Integer32):
    """Custom type ipInterfaceProfile_Ospf_Active based on Integer32"""
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


_IpInterfaceProfile_Ospf_Active_Type.__name__ = "Integer32"
_IpInterfaceProfile_Ospf_Active_Object = MibScalar
ipInterfaceProfile_Ospf_Active = _IpInterfaceProfile_Ospf_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 16),
    _IpInterfaceProfile_Ospf_Active_Type()
)
ipInterfaceProfile_Ospf_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_Active.setStatus("mandatory")
_IpInterfaceProfile_Ospf_Area_Type = IpAddress
_IpInterfaceProfile_Ospf_Area_Object = MibScalar
ipInterfaceProfile_Ospf_Area = _IpInterfaceProfile_Ospf_Area_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 17),
    _IpInterfaceProfile_Ospf_Area_Type()
)
ipInterfaceProfile_Ospf_Area.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_Area.setStatus("mandatory")


class _IpInterfaceProfile_Ospf_AreaType_Type(Integer32):
    """Custom type ipInterfaceProfile_Ospf_AreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nSSA", 3),
          ("normal", 1),
          ("stub", 2))
    )


_IpInterfaceProfile_Ospf_AreaType_Type.__name__ = "Integer32"
_IpInterfaceProfile_Ospf_AreaType_Object = MibScalar
ipInterfaceProfile_Ospf_AreaType = _IpInterfaceProfile_Ospf_AreaType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 18),
    _IpInterfaceProfile_Ospf_AreaType_Type()
)
ipInterfaceProfile_Ospf_AreaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_AreaType.setStatus("mandatory")
_IpInterfaceProfile_Ospf_HelloInterval_Type = Integer32
_IpInterfaceProfile_Ospf_HelloInterval_Object = MibScalar
ipInterfaceProfile_Ospf_HelloInterval = _IpInterfaceProfile_Ospf_HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 19),
    _IpInterfaceProfile_Ospf_HelloInterval_Type()
)
ipInterfaceProfile_Ospf_HelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_HelloInterval.setStatus("mandatory")
_IpInterfaceProfile_Ospf_DeadInterval_Type = Integer32
_IpInterfaceProfile_Ospf_DeadInterval_Object = MibScalar
ipInterfaceProfile_Ospf_DeadInterval = _IpInterfaceProfile_Ospf_DeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 20),
    _IpInterfaceProfile_Ospf_DeadInterval_Type()
)
ipInterfaceProfile_Ospf_DeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_DeadInterval.setStatus("mandatory")
_IpInterfaceProfile_Ospf_Priority_Type = Integer32
_IpInterfaceProfile_Ospf_Priority_Object = MibScalar
ipInterfaceProfile_Ospf_Priority = _IpInterfaceProfile_Ospf_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 21),
    _IpInterfaceProfile_Ospf_Priority_Type()
)
ipInterfaceProfile_Ospf_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_Priority.setStatus("mandatory")


class _IpInterfaceProfile_Ospf_AuthenType_Type(Integer32):
    """Custom type ipInterfaceProfile_Ospf_AuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("simple", 2))
    )


_IpInterfaceProfile_Ospf_AuthenType_Type.__name__ = "Integer32"
_IpInterfaceProfile_Ospf_AuthenType_Object = MibScalar
ipInterfaceProfile_Ospf_AuthenType = _IpInterfaceProfile_Ospf_AuthenType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 22),
    _IpInterfaceProfile_Ospf_AuthenType_Type()
)
ipInterfaceProfile_Ospf_AuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_AuthenType.setStatus("mandatory")
_IpInterfaceProfile_Ospf_AuthKey_Type = DisplayString
_IpInterfaceProfile_Ospf_AuthKey_Object = MibScalar
ipInterfaceProfile_Ospf_AuthKey = _IpInterfaceProfile_Ospf_AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 23),
    _IpInterfaceProfile_Ospf_AuthKey_Type()
)
ipInterfaceProfile_Ospf_AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_AuthKey.setStatus("mandatory")
_IpInterfaceProfile_Ospf_KeyId_Type = Integer32
_IpInterfaceProfile_Ospf_KeyId_Object = MibScalar
ipInterfaceProfile_Ospf_KeyId = _IpInterfaceProfile_Ospf_KeyId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 24),
    _IpInterfaceProfile_Ospf_KeyId_Type()
)
ipInterfaceProfile_Ospf_KeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_KeyId.setStatus("mandatory")
_IpInterfaceProfile_Ospf_Cost_Type = Integer32
_IpInterfaceProfile_Ospf_Cost_Object = MibScalar
ipInterfaceProfile_Ospf_Cost = _IpInterfaceProfile_Ospf_Cost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 25),
    _IpInterfaceProfile_Ospf_Cost_Type()
)
ipInterfaceProfile_Ospf_Cost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_Cost.setStatus("mandatory")
_IpInterfaceProfile_Ospf_DownCost_Type = Integer32
_IpInterfaceProfile_Ospf_DownCost_Object = MibScalar
ipInterfaceProfile_Ospf_DownCost = _IpInterfaceProfile_Ospf_DownCost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 26),
    _IpInterfaceProfile_Ospf_DownCost_Type()
)
ipInterfaceProfile_Ospf_DownCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_DownCost.setStatus("mandatory")


class _IpInterfaceProfile_Ospf_AseType_Type(Integer32):
    """Custom type ipInterfaceProfile_Ospf_AseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_IpInterfaceProfile_Ospf_AseType_Type.__name__ = "Integer32"
_IpInterfaceProfile_Ospf_AseType_Object = MibScalar
ipInterfaceProfile_Ospf_AseType = _IpInterfaceProfile_Ospf_AseType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 27),
    _IpInterfaceProfile_Ospf_AseType_Type()
)
ipInterfaceProfile_Ospf_AseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_AseType.setStatus("mandatory")
_IpInterfaceProfile_Ospf_AseTag_Type = DisplayString
_IpInterfaceProfile_Ospf_AseTag_Object = MibScalar
ipInterfaceProfile_Ospf_AseTag = _IpInterfaceProfile_Ospf_AseTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 28),
    _IpInterfaceProfile_Ospf_AseTag_Type()
)
ipInterfaceProfile_Ospf_AseTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_AseTag.setStatus("mandatory")
_IpInterfaceProfile_Ospf_TransitDelay_Type = Integer32
_IpInterfaceProfile_Ospf_TransitDelay_Object = MibScalar
ipInterfaceProfile_Ospf_TransitDelay = _IpInterfaceProfile_Ospf_TransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 29),
    _IpInterfaceProfile_Ospf_TransitDelay_Type()
)
ipInterfaceProfile_Ospf_TransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_TransitDelay.setStatus("mandatory")
_IpInterfaceProfile_Ospf_RetransmitInterval_Type = Integer32
_IpInterfaceProfile_Ospf_RetransmitInterval_Object = MibScalar
ipInterfaceProfile_Ospf_RetransmitInterval = _IpInterfaceProfile_Ospf_RetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 30),
    _IpInterfaceProfile_Ospf_RetransmitInterval_Type()
)
ipInterfaceProfile_Ospf_RetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_RetransmitInterval.setStatus("mandatory")


class _IpInterfaceProfile_Ospf_NonMulticast_Type(Integer32):
    """Custom type ipInterfaceProfile_Ospf_NonMulticast based on Integer32"""
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


_IpInterfaceProfile_Ospf_NonMulticast_Type.__name__ = "Integer32"
_IpInterfaceProfile_Ospf_NonMulticast_Object = MibScalar
ipInterfaceProfile_Ospf_NonMulticast = _IpInterfaceProfile_Ospf_NonMulticast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 31),
    _IpInterfaceProfile_Ospf_NonMulticast_Type()
)
ipInterfaceProfile_Ospf_NonMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_NonMulticast.setStatus("mandatory")


class _IpInterfaceProfile_Ospf_NetworkType_Type(Integer32):
    """Custom type ipInterfaceProfile_Ospf_NetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("nonBroadcast", 3),
          ("pointToPoint", 4))
    )


_IpInterfaceProfile_Ospf_NetworkType_Type.__name__ = "Integer32"
_IpInterfaceProfile_Ospf_NetworkType_Object = MibScalar
ipInterfaceProfile_Ospf_NetworkType = _IpInterfaceProfile_Ospf_NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 32),
    _IpInterfaceProfile_Ospf_NetworkType_Type()
)
ipInterfaceProfile_Ospf_NetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_NetworkType.setStatus("mandatory")
_IpInterfaceProfile_Ospf_PollInterval_Type = Integer32
_IpInterfaceProfile_Ospf_PollInterval_Object = MibScalar
ipInterfaceProfile_Ospf_PollInterval = _IpInterfaceProfile_Ospf_PollInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 33),
    _IpInterfaceProfile_Ospf_PollInterval_Type()
)
ipInterfaceProfile_Ospf_PollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_PollInterval.setStatus("mandatory")
_IpInterfaceProfile_Ospf_Md5AuthKey_Type = DisplayString
_IpInterfaceProfile_Ospf_Md5AuthKey_Object = MibScalar
ipInterfaceProfile_Ospf_Md5AuthKey = _IpInterfaceProfile_Ospf_Md5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 34),
    _IpInterfaceProfile_Ospf_Md5AuthKey_Type()
)
ipInterfaceProfile_Ospf_Md5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Ospf_Md5AuthKey.setStatus("mandatory")


class _IpInterfaceProfile_MulticastAllowed_Type(Integer32):
    """Custom type ipInterfaceProfile_MulticastAllowed based on Integer32"""
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


_IpInterfaceProfile_MulticastAllowed_Type.__name__ = "Integer32"
_IpInterfaceProfile_MulticastAllowed_Object = MibScalar
ipInterfaceProfile_MulticastAllowed = _IpInterfaceProfile_MulticastAllowed_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 35),
    _IpInterfaceProfile_MulticastAllowed_Type()
)
ipInterfaceProfile_MulticastAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_MulticastAllowed.setStatus("mandatory")
_IpInterfaceProfile_MulticastRateLimit_Type = Integer32
_IpInterfaceProfile_MulticastRateLimit_Object = MibScalar
ipInterfaceProfile_MulticastRateLimit = _IpInterfaceProfile_MulticastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 36),
    _IpInterfaceProfile_MulticastRateLimit_Type()
)
ipInterfaceProfile_MulticastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_MulticastRateLimit.setStatus("mandatory")
_IpInterfaceProfile_MulticastGroupLeaveDelay_Type = Integer32
_IpInterfaceProfile_MulticastGroupLeaveDelay_Object = MibScalar
ipInterfaceProfile_MulticastGroupLeaveDelay = _IpInterfaceProfile_MulticastGroupLeaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 37),
    _IpInterfaceProfile_MulticastGroupLeaveDelay_Type()
)
ipInterfaceProfile_MulticastGroupLeaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_MulticastGroupLeaveDelay.setStatus("mandatory")


class _IpInterfaceProfile_DirectedBroadcastAllowed_Type(Integer32):
    """Custom type ipInterfaceProfile_DirectedBroadcastAllowed based on Integer32"""
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


_IpInterfaceProfile_DirectedBroadcastAllowed_Type.__name__ = "Integer32"
_IpInterfaceProfile_DirectedBroadcastAllowed_Object = MibScalar
ipInterfaceProfile_DirectedBroadcastAllowed = _IpInterfaceProfile_DirectedBroadcastAllowed_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 38),
    _IpInterfaceProfile_DirectedBroadcastAllowed_Type()
)
ipInterfaceProfile_DirectedBroadcastAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_DirectedBroadcastAllowed.setStatus("mandatory")
_IpInterfaceProfile_Vrouter_Type = DisplayString
_IpInterfaceProfile_Vrouter_Object = MibScalar
ipInterfaceProfile_Vrouter = _IpInterfaceProfile_Vrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 39),
    _IpInterfaceProfile_Vrouter_Type()
)
ipInterfaceProfile_Vrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Vrouter.setStatus("mandatory")


class _IpInterfaceProfile_ManagementOnlyInterface_Type(Integer32):
    """Custom type ipInterfaceProfile_ManagementOnlyInterface based on Integer32"""
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


_IpInterfaceProfile_ManagementOnlyInterface_Type.__name__ = "Integer32"
_IpInterfaceProfile_ManagementOnlyInterface_Object = MibScalar
ipInterfaceProfile_ManagementOnlyInterface = _IpInterfaceProfile_ManagementOnlyInterface_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 40),
    _IpInterfaceProfile_ManagementOnlyInterface_Type()
)
ipInterfaceProfile_ManagementOnlyInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_ManagementOnlyInterface.setStatus("mandatory")


class _IpInterfaceProfile_DhcpClientEnabled_Type(Integer32):
    """Custom type ipInterfaceProfile_DhcpClientEnabled based on Integer32"""
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


_IpInterfaceProfile_DhcpClientEnabled_Type.__name__ = "Integer32"
_IpInterfaceProfile_DhcpClientEnabled_Object = MibScalar
ipInterfaceProfile_DhcpClientEnabled = _IpInterfaceProfile_DhcpClientEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 41),
    _IpInterfaceProfile_DhcpClientEnabled_Type()
)
ipInterfaceProfile_DhcpClientEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_DhcpClientEnabled.setStatus("mandatory")


class _IpInterfaceProfile_Action_o_Type(Integer32):
    """Custom type ipInterfaceProfile_Action_o based on Integer32"""
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


_IpInterfaceProfile_Action_o_Type.__name__ = "Integer32"
_IpInterfaceProfile_Action_o_Object = MibScalar
ipInterfaceProfile_Action_o = _IpInterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 42),
    _IpInterfaceProfile_Action_o_Type()
)
ipInterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Action_o.setStatus("mandatory")
_IpInterfaceProfile_Netmask_Type = IpAddress
_IpInterfaceProfile_Netmask_Object = MibScalar
ipInterfaceProfile_Netmask = _IpInterfaceProfile_Netmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 43),
    _IpInterfaceProfile_Netmask_Type()
)
ipInterfaceProfile_Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Netmask.setStatus("mandatory")
_IpInterfaceProfile_Netmask2_Type = IpAddress
_IpInterfaceProfile_Netmask2_Object = MibScalar
ipInterfaceProfile_Netmask2 = _IpInterfaceProfile_Netmask2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 44),
    _IpInterfaceProfile_Netmask2_Type()
)
ipInterfaceProfile_Netmask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_Netmask2.setStatus("mandatory")
_IpInterfaceProfile_NatProfileName_Type = DisplayString
_IpInterfaceProfile_NatProfileName_Object = MibScalar
ipInterfaceProfile_NatProfileName = _IpInterfaceProfile_NatProfileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 45),
    _IpInterfaceProfile_NatProfileName_Type()
)
ipInterfaceProfile_NatProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_NatProfileName.setStatus("mandatory")
_IpInterfaceProfile_AddressRealm_Type = Integer32
_IpInterfaceProfile_AddressRealm_Object = MibScalar
ipInterfaceProfile_AddressRealm = _IpInterfaceProfile_AddressRealm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 46),
    _IpInterfaceProfile_AddressRealm_Type()
)
ipInterfaceProfile_AddressRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_AddressRealm.setStatus("mandatory")


class _IpInterfaceProfile_VlanEnabled_Type(Integer32):
    """Custom type ipInterfaceProfile_VlanEnabled based on Integer32"""
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


_IpInterfaceProfile_VlanEnabled_Type.__name__ = "Integer32"
_IpInterfaceProfile_VlanEnabled_Object = MibScalar
ipInterfaceProfile_VlanEnabled = _IpInterfaceProfile_VlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 82, 1, 1, 47),
    _IpInterfaceProfile_VlanEnabled_Type()
)
ipInterfaceProfile_VlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProfile_VlanEnabled.setStatus("mandatory")
_MibipGlobalProfile_ObjectIdentity = ObjectIdentity
mibipGlobalProfile = _MibipGlobalProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 83)
)
_MibipGlobalProfileTable_Object = MibTable
mibipGlobalProfileTable = _MibipGlobalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1)
)
if mibBuilder.loadTexts:
    mibipGlobalProfileTable.setStatus("mandatory")
_MibipGlobalProfileEntry_Object = MibTableRow
mibipGlobalProfileEntry = _MibipGlobalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1)
)
mibipGlobalProfileEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfileEntry.setStatus("mandatory")
_IpGlobalProfile_Index_o_Type = Integer32
_IpGlobalProfile_Index_o_Object = MibScalar
ipGlobalProfile_Index_o = _IpGlobalProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 1),
    _IpGlobalProfile_Index_o_Type()
)
ipGlobalProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_Index_o.setStatus("mandatory")
_IpGlobalProfile_DomainName_Type = DisplayString
_IpGlobalProfile_DomainName_Object = MibScalar
ipGlobalProfile_DomainName = _IpGlobalProfile_DomainName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 2),
    _IpGlobalProfile_DomainName_Type()
)
ipGlobalProfile_DomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DomainName.setStatus("mandatory")
_IpGlobalProfile_DnsPrimaryServer_Type = IpAddress
_IpGlobalProfile_DnsPrimaryServer_Object = MibScalar
ipGlobalProfile_DnsPrimaryServer = _IpGlobalProfile_DnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 3),
    _IpGlobalProfile_DnsPrimaryServer_Type()
)
ipGlobalProfile_DnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsPrimaryServer.setStatus("mandatory")


class _IpGlobalProfile_DhcpServer_Active_Type(Integer32):
    """Custom type ipGlobalProfile_DhcpServer_Active based on Integer32"""
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


_IpGlobalProfile_DhcpServer_Active_Type.__name__ = "Integer32"
_IpGlobalProfile_DhcpServer_Active_Object = MibScalar
ipGlobalProfile_DhcpServer_Active = _IpGlobalProfile_DhcpServer_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 4),
    _IpGlobalProfile_DhcpServer_Active_Type()
)
ipGlobalProfile_DhcpServer_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_Active.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_LeaseDuration_Type = Integer32
_IpGlobalProfile_DhcpServer_LeaseDuration_Object = MibScalar
ipGlobalProfile_DhcpServer_LeaseDuration = _IpGlobalProfile_DhcpServer_LeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 5),
    _IpGlobalProfile_DhcpServer_LeaseDuration_Type()
)
ipGlobalProfile_DhcpServer_LeaseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_LeaseDuration.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_DefaultPool_Type = Integer32
_IpGlobalProfile_DhcpServer_DefaultPool_Object = MibScalar
ipGlobalProfile_DhcpServer_DefaultPool = _IpGlobalProfile_DhcpServer_DefaultPool_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 6),
    _IpGlobalProfile_DhcpServer_DefaultPool_Type()
)
ipGlobalProfile_DhcpServer_DefaultPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_DefaultPool.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_DefaultMaxLease_Type = Integer32
_IpGlobalProfile_DhcpServer_DefaultMaxLease_Object = MibScalar
ipGlobalProfile_DhcpServer_DefaultMaxLease = _IpGlobalProfile_DhcpServer_DefaultMaxLease_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 7),
    _IpGlobalProfile_DhcpServer_DefaultMaxLease_Type()
)
ipGlobalProfile_DhcpServer_DefaultMaxLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_DefaultMaxLease.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_DefaultLeaseDuration_Type = Integer32
_IpGlobalProfile_DhcpServer_DefaultLeaseDuration_Object = MibScalar
ipGlobalProfile_DhcpServer_DefaultLeaseDuration = _IpGlobalProfile_DhcpServer_DefaultLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 8),
    _IpGlobalProfile_DhcpServer_DefaultLeaseDuration_Type()
)
ipGlobalProfile_DhcpServer_DefaultLeaseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_DefaultLeaseDuration.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_TftpHostName_Type = DisplayString
_IpGlobalProfile_DhcpServer_TftpHostName_Object = MibScalar
ipGlobalProfile_DhcpServer_TftpHostName = _IpGlobalProfile_DhcpServer_TftpHostName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 9),
    _IpGlobalProfile_DhcpServer_TftpHostName_Type()
)
ipGlobalProfile_DhcpServer_TftpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_TftpHostName.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_BootFilePath_Type = DisplayString
_IpGlobalProfile_DhcpServer_BootFilePath_Object = MibScalar
ipGlobalProfile_DhcpServer_BootFilePath = _IpGlobalProfile_DhcpServer_BootFilePath_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 10),
    _IpGlobalProfile_DhcpServer_BootFilePath_Type()
)
ipGlobalProfile_DhcpServer_BootFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_BootFilePath.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_ServerAddress_Type = IpAddress
_IpGlobalProfile_DhcpServer_ServerAddress_Object = MibScalar
ipGlobalProfile_DhcpServer_ServerAddress = _IpGlobalProfile_DhcpServer_ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 11),
    _IpGlobalProfile_DhcpServer_ServerAddress_Type()
)
ipGlobalProfile_DhcpServer_ServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_ServerAddress.setStatus("mandatory")
_IpGlobalProfile_DnsSecondaryServer_Type = IpAddress
_IpGlobalProfile_DnsSecondaryServer_Object = MibScalar
ipGlobalProfile_DnsSecondaryServer = _IpGlobalProfile_DnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 12),
    _IpGlobalProfile_DnsSecondaryServer_Type()
)
ipGlobalProfile_DnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsSecondaryServer.setStatus("mandatory")


class _IpGlobalProfile_DnsServerQueryType_Type(Integer32):
    """Custom type ipGlobalProfile_DnsServerQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 3),
          ("tcpKeepOpen", 4),
          ("udp", 1),
          ("udpIgnoreTcBit", 2))
    )


_IpGlobalProfile_DnsServerQueryType_Type.__name__ = "Integer32"
_IpGlobalProfile_DnsServerQueryType_Object = MibScalar
ipGlobalProfile_DnsServerQueryType = _IpGlobalProfile_DnsServerQueryType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 13),
    _IpGlobalProfile_DnsServerQueryType_Type()
)
ipGlobalProfile_DnsServerQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsServerQueryType.setStatus("mandatory")
_IpGlobalProfile_SystemIpAddr_Type = IpAddress
_IpGlobalProfile_SystemIpAddr_Object = MibScalar
ipGlobalProfile_SystemIpAddr = _IpGlobalProfile_SystemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 14),
    _IpGlobalProfile_SystemIpAddr_Type()
)
ipGlobalProfile_SystemIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SystemIpAddr.setStatus("mandatory")
_IpGlobalProfile_NetbiosPrimaryNs_Type = IpAddress
_IpGlobalProfile_NetbiosPrimaryNs_Object = MibScalar
ipGlobalProfile_NetbiosPrimaryNs = _IpGlobalProfile_NetbiosPrimaryNs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 15),
    _IpGlobalProfile_NetbiosPrimaryNs_Type()
)
ipGlobalProfile_NetbiosPrimaryNs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_NetbiosPrimaryNs.setStatus("mandatory")
_IpGlobalProfile_NetbiosSecondaryNs_Type = IpAddress
_IpGlobalProfile_NetbiosSecondaryNs_Object = MibScalar
ipGlobalProfile_NetbiosSecondaryNs = _IpGlobalProfile_NetbiosSecondaryNs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 16),
    _IpGlobalProfile_NetbiosSecondaryNs_Type()
)
ipGlobalProfile_NetbiosSecondaryNs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_NetbiosSecondaryNs.setStatus("mandatory")


class _IpGlobalProfile_MustAcceptAddressAssign_Type(Integer32):
    """Custom type ipGlobalProfile_MustAcceptAddressAssign based on Integer32"""
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


_IpGlobalProfile_MustAcceptAddressAssign_Type.__name__ = "Integer32"
_IpGlobalProfile_MustAcceptAddressAssign_Object = MibScalar
ipGlobalProfile_MustAcceptAddressAssign = _IpGlobalProfile_MustAcceptAddressAssign_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 17),
    _IpGlobalProfile_MustAcceptAddressAssign_Type()
)
ipGlobalProfile_MustAcceptAddressAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MustAcceptAddressAssign.setStatus("mandatory")


class _IpGlobalProfile_PoolSummary_Type(Integer32):
    """Custom type ipGlobalProfile_PoolSummary based on Integer32"""
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


_IpGlobalProfile_PoolSummary_Type.__name__ = "Integer32"
_IpGlobalProfile_PoolSummary_Object = MibScalar
ipGlobalProfile_PoolSummary = _IpGlobalProfile_PoolSummary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 18),
    _IpGlobalProfile_PoolSummary_Type()
)
ipGlobalProfile_PoolSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolSummary.setStatus("mandatory")


class _IpGlobalProfile_PoolChaining_Type(Integer32):
    """Custom type ipGlobalProfile_PoolChaining based on Integer32"""
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


_IpGlobalProfile_PoolChaining_Type.__name__ = "Integer32"
_IpGlobalProfile_PoolChaining_Object = MibScalar
ipGlobalProfile_PoolChaining = _IpGlobalProfile_PoolChaining_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 19),
    _IpGlobalProfile_PoolChaining_Type()
)
ipGlobalProfile_PoolChaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolChaining.setStatus("mandatory")


class _IpGlobalProfile_PoolOspfAdvType_Type(Integer32):
    """Custom type ipGlobalProfile_PoolOspfAdvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 3),
          ("type1", 1),
          ("type2", 2))
    )


_IpGlobalProfile_PoolOspfAdvType_Type.__name__ = "Integer32"
_IpGlobalProfile_PoolOspfAdvType_Object = MibScalar
ipGlobalProfile_PoolOspfAdvType = _IpGlobalProfile_PoolOspfAdvType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 20),
    _IpGlobalProfile_PoolOspfAdvType_Type()
)
ipGlobalProfile_PoolOspfAdvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolOspfAdvType.setStatus("mandatory")


class _IpGlobalProfile_RipPolicy_Type(Integer32):
    """Custom type ipGlobalProfile_RipPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poisonRvrs", 2),
          ("splitHorzn", 1))
    )


_IpGlobalProfile_RipPolicy_Type.__name__ = "Integer32"
_IpGlobalProfile_RipPolicy_Object = MibScalar
ipGlobalProfile_RipPolicy = _IpGlobalProfile_RipPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 21),
    _IpGlobalProfile_RipPolicy_Type()
)
ipGlobalProfile_RipPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RipPolicy.setStatus("mandatory")


class _IpGlobalProfile_SummarizeRipRoutes_Type(Integer32):
    """Custom type ipGlobalProfile_SummarizeRipRoutes based on Integer32"""
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


_IpGlobalProfile_SummarizeRipRoutes_Type.__name__ = "Integer32"
_IpGlobalProfile_SummarizeRipRoutes_Object = MibScalar
ipGlobalProfile_SummarizeRipRoutes = _IpGlobalProfile_SummarizeRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 22),
    _IpGlobalProfile_SummarizeRipRoutes_Type()
)
ipGlobalProfile_SummarizeRipRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SummarizeRipRoutes.setStatus("mandatory")


class _IpGlobalProfile_RipTrigger_Type(Integer32):
    """Custom type ipGlobalProfile_RipTrigger based on Integer32"""
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


_IpGlobalProfile_RipTrigger_Type.__name__ = "Integer32"
_IpGlobalProfile_RipTrigger_Object = MibScalar
ipGlobalProfile_RipTrigger = _IpGlobalProfile_RipTrigger_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 23),
    _IpGlobalProfile_RipTrigger_Type()
)
ipGlobalProfile_RipTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RipTrigger.setStatus("mandatory")


class _IpGlobalProfile_BootpEnabled_Type(Integer32):
    """Custom type ipGlobalProfile_BootpEnabled based on Integer32"""
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


_IpGlobalProfile_BootpEnabled_Type.__name__ = "Integer32"
_IpGlobalProfile_BootpEnabled_Object = MibScalar
ipGlobalProfile_BootpEnabled = _IpGlobalProfile_BootpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 24),
    _IpGlobalProfile_BootpEnabled_Type()
)
ipGlobalProfile_BootpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_BootpEnabled.setStatus("mandatory")


class _IpGlobalProfile_BootpRelay_Active_Type(Integer32):
    """Custom type ipGlobalProfile_BootpRelay_Active based on Integer32"""
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


_IpGlobalProfile_BootpRelay_Active_Type.__name__ = "Integer32"
_IpGlobalProfile_BootpRelay_Active_Object = MibScalar
ipGlobalProfile_BootpRelay_Active = _IpGlobalProfile_BootpRelay_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 25),
    _IpGlobalProfile_BootpRelay_Active_Type()
)
ipGlobalProfile_BootpRelay_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_BootpRelay_Active.setStatus("mandatory")


class _IpGlobalProfile_DropSourceRoutedIpPackets_Type(Integer32):
    """Custom type ipGlobalProfile_DropSourceRoutedIpPackets based on Integer32"""
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


_IpGlobalProfile_DropSourceRoutedIpPackets_Type.__name__ = "Integer32"
_IpGlobalProfile_DropSourceRoutedIpPackets_Object = MibScalar
ipGlobalProfile_DropSourceRoutedIpPackets = _IpGlobalProfile_DropSourceRoutedIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 26),
    _IpGlobalProfile_DropSourceRoutedIpPackets_Type()
)
ipGlobalProfile_DropSourceRoutedIpPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DropSourceRoutedIpPackets.setStatus("mandatory")


class _IpGlobalProfile_IgnoreDefRoute_Type(Integer32):
    """Custom type ipGlobalProfile_IgnoreDefRoute based on Integer32"""
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


_IpGlobalProfile_IgnoreDefRoute_Type.__name__ = "Integer32"
_IpGlobalProfile_IgnoreDefRoute_Object = MibScalar
ipGlobalProfile_IgnoreDefRoute = _IpGlobalProfile_IgnoreDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 27),
    _IpGlobalProfile_IgnoreDefRoute_Type()
)
ipGlobalProfile_IgnoreDefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IgnoreDefRoute.setStatus("mandatory")


class _IpGlobalProfile_RarpEnabled_Type(Integer32):
    """Custom type ipGlobalProfile_RarpEnabled based on Integer32"""
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


_IpGlobalProfile_RarpEnabled_Type.__name__ = "Integer32"
_IpGlobalProfile_RarpEnabled_Object = MibScalar
ipGlobalProfile_RarpEnabled = _IpGlobalProfile_RarpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 28),
    _IpGlobalProfile_RarpEnabled_Type()
)
ipGlobalProfile_RarpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RarpEnabled.setStatus("mandatory")


class _IpGlobalProfile_UdpCksum_Type(Integer32):
    """Custom type ipGlobalProfile_UdpCksum based on Integer32"""
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


_IpGlobalProfile_UdpCksum_Type.__name__ = "Integer32"
_IpGlobalProfile_UdpCksum_Object = MibScalar
ipGlobalProfile_UdpCksum = _IpGlobalProfile_UdpCksum_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 29),
    _IpGlobalProfile_UdpCksum_Type()
)
ipGlobalProfile_UdpCksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_UdpCksum.setStatus("mandatory")
_IpGlobalProfile_TcpTimeout_Type = Integer32
_IpGlobalProfile_TcpTimeout_Object = MibScalar
ipGlobalProfile_TcpTimeout = _IpGlobalProfile_TcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 30),
    _IpGlobalProfile_TcpTimeout_Type()
)
ipGlobalProfile_TcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_TcpTimeout.setStatus("mandatory")


class _IpGlobalProfile_DialoutPoison_Type(Integer32):
    """Custom type ipGlobalProfile_DialoutPoison based on Integer32"""
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


_IpGlobalProfile_DialoutPoison_Type.__name__ = "Integer32"
_IpGlobalProfile_DialoutPoison_Object = MibScalar
ipGlobalProfile_DialoutPoison = _IpGlobalProfile_DialoutPoison_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 31),
    _IpGlobalProfile_DialoutPoison_Type()
)
ipGlobalProfile_DialoutPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DialoutPoison.setStatus("mandatory")
_IpGlobalProfile_TelnetPassword_Type = DisplayString
_IpGlobalProfile_TelnetPassword_Object = MibScalar
ipGlobalProfile_TelnetPassword = _IpGlobalProfile_TelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 32),
    _IpGlobalProfile_TelnetPassword_Type()
)
ipGlobalProfile_TelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_TelnetPassword.setStatus("mandatory")
_IpGlobalProfile_UserProfile_Type = DisplayString
_IpGlobalProfile_UserProfile_Object = MibScalar
ipGlobalProfile_UserProfile = _IpGlobalProfile_UserProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 33),
    _IpGlobalProfile_UserProfile_Type()
)
ipGlobalProfile_UserProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_UserProfile.setStatus("mandatory")


class _IpGlobalProfile_SharedProf_Type(Integer32):
    """Custom type ipGlobalProfile_SharedProf based on Integer32"""
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


_IpGlobalProfile_SharedProf_Type.__name__ = "Integer32"
_IpGlobalProfile_SharedProf_Object = MibScalar
ipGlobalProfile_SharedProf = _IpGlobalProfile_SharedProf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 34),
    _IpGlobalProfile_SharedProf_Type()
)
ipGlobalProfile_SharedProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SharedProf.setStatus("mandatory")


class _IpGlobalProfile_DnsListAttempt_Type(Integer32):
    """Custom type ipGlobalProfile_DnsListAttempt based on Integer32"""
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


_IpGlobalProfile_DnsListAttempt_Type.__name__ = "Integer32"
_IpGlobalProfile_DnsListAttempt_Object = MibScalar
ipGlobalProfile_DnsListAttempt = _IpGlobalProfile_DnsListAttempt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 35),
    _IpGlobalProfile_DnsListAttempt_Type()
)
ipGlobalProfile_DnsListAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsListAttempt.setStatus("mandatory")
_IpGlobalProfile_StaticPref_Type = Integer32
_IpGlobalProfile_StaticPref_Object = MibScalar
ipGlobalProfile_StaticPref = _IpGlobalProfile_StaticPref_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 36),
    _IpGlobalProfile_StaticPref_Type()
)
ipGlobalProfile_StaticPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_StaticPref.setStatus("mandatory")
_IpGlobalProfile_RipPref_Type = Integer32
_IpGlobalProfile_RipPref_Object = MibScalar
ipGlobalProfile_RipPref = _IpGlobalProfile_RipPref_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 37),
    _IpGlobalProfile_RipPref_Type()
)
ipGlobalProfile_RipPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RipPref.setStatus("mandatory")
_IpGlobalProfile_RipQueueDepth_Type = Integer32
_IpGlobalProfile_RipQueueDepth_Object = MibScalar
ipGlobalProfile_RipQueueDepth = _IpGlobalProfile_RipQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 38),
    _IpGlobalProfile_RipQueueDepth_Type()
)
ipGlobalProfile_RipQueueDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RipQueueDepth.setStatus("mandatory")
_IpGlobalProfile_OspfPref_Type = Integer32
_IpGlobalProfile_OspfPref_Object = MibScalar
ipGlobalProfile_OspfPref = _IpGlobalProfile_OspfPref_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 39),
    _IpGlobalProfile_OspfPref_Type()
)
ipGlobalProfile_OspfPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_OspfPref.setStatus("mandatory")
_IpGlobalProfile_OspfAsePref_Type = Integer32
_IpGlobalProfile_OspfAsePref_Object = MibScalar
ipGlobalProfile_OspfAsePref = _IpGlobalProfile_OspfAsePref_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 40),
    _IpGlobalProfile_OspfAsePref_Type()
)
ipGlobalProfile_OspfAsePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_OspfAsePref.setStatus("mandatory")


class _IpGlobalProfile_OspfGlobal_Enable_Type(Integer32):
    """Custom type ipGlobalProfile_OspfGlobal_Enable based on Integer32"""
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


_IpGlobalProfile_OspfGlobal_Enable_Type.__name__ = "Integer32"
_IpGlobalProfile_OspfGlobal_Enable_Object = MibScalar
ipGlobalProfile_OspfGlobal_Enable = _IpGlobalProfile_OspfGlobal_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 41),
    _IpGlobalProfile_OspfGlobal_Enable_Type()
)
ipGlobalProfile_OspfGlobal_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_OspfGlobal_Enable.setStatus("mandatory")


class _IpGlobalProfile_OspfGlobal_AsBoundaryRouter_Type(Integer32):
    """Custom type ipGlobalProfile_OspfGlobal_AsBoundaryRouter based on Integer32"""
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


_IpGlobalProfile_OspfGlobal_AsBoundaryRouter_Type.__name__ = "Integer32"
_IpGlobalProfile_OspfGlobal_AsBoundaryRouter_Object = MibScalar
ipGlobalProfile_OspfGlobal_AsBoundaryRouter = _IpGlobalProfile_OspfGlobal_AsBoundaryRouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 42),
    _IpGlobalProfile_OspfGlobal_AsBoundaryRouter_Type()
)
ipGlobalProfile_OspfGlobal_AsBoundaryRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_OspfGlobal_AsBoundaryRouter.setStatus("mandatory")
_IpGlobalProfile_OspfGlobal_OspfMaxLsa_Type = Integer32
_IpGlobalProfile_OspfGlobal_OspfMaxLsa_Object = MibScalar
ipGlobalProfile_OspfGlobal_OspfMaxLsa = _IpGlobalProfile_OspfGlobal_OspfMaxLsa_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 43),
    _IpGlobalProfile_OspfGlobal_OspfMaxLsa_Type()
)
ipGlobalProfile_OspfGlobal_OspfMaxLsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_OspfGlobal_OspfMaxLsa.setStatus("mandatory")
_IpGlobalProfile_RipTag_Type = DisplayString
_IpGlobalProfile_RipTag_Object = MibScalar
ipGlobalProfile_RipTag = _IpGlobalProfile_RipTag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 44),
    _IpGlobalProfile_RipTag_Type()
)
ipGlobalProfile_RipTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RipTag.setStatus("mandatory")
_IpGlobalProfile_RipAseType_Type = Integer32
_IpGlobalProfile_RipAseType_Object = MibScalar
ipGlobalProfile_RipAseType = _IpGlobalProfile_RipAseType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 45),
    _IpGlobalProfile_RipAseType_Type()
)
ipGlobalProfile_RipAseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RipAseType.setStatus("mandatory")


class _IpGlobalProfile_IprouteCacheEnable_Type(Integer32):
    """Custom type ipGlobalProfile_IprouteCacheEnable based on Integer32"""
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


_IpGlobalProfile_IprouteCacheEnable_Type.__name__ = "Integer32"
_IpGlobalProfile_IprouteCacheEnable_Object = MibScalar
ipGlobalProfile_IprouteCacheEnable = _IpGlobalProfile_IprouteCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 46),
    _IpGlobalProfile_IprouteCacheEnable_Type()
)
ipGlobalProfile_IprouteCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IprouteCacheEnable.setStatus("mandatory")
_IpGlobalProfile_IprouteCacheSize_Type = Integer32
_IpGlobalProfile_IprouteCacheSize_Object = MibScalar
ipGlobalProfile_IprouteCacheSize = _IpGlobalProfile_IprouteCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 47),
    _IpGlobalProfile_IprouteCacheSize_Type()
)
ipGlobalProfile_IprouteCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IprouteCacheSize.setStatus("mandatory")


class _IpGlobalProfile_IpportCacheEnable_Type(Integer32):
    """Custom type ipGlobalProfile_IpportCacheEnable based on Integer32"""
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


_IpGlobalProfile_IpportCacheEnable_Type.__name__ = "Integer32"
_IpGlobalProfile_IpportCacheEnable_Object = MibScalar
ipGlobalProfile_IpportCacheEnable = _IpGlobalProfile_IpportCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 48),
    _IpGlobalProfile_IpportCacheEnable_Type()
)
ipGlobalProfile_IpportCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IpportCacheEnable.setStatus("mandatory")


class _IpGlobalProfile_SuppressHostRoutes_Type(Integer32):
    """Custom type ipGlobalProfile_SuppressHostRoutes based on Integer32"""
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


_IpGlobalProfile_SuppressHostRoutes_Type.__name__ = "Integer32"
_IpGlobalProfile_SuppressHostRoutes_Object = MibScalar
ipGlobalProfile_SuppressHostRoutes = _IpGlobalProfile_SuppressHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 49),
    _IpGlobalProfile_SuppressHostRoutes_Type()
)
ipGlobalProfile_SuppressHostRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SuppressHostRoutes.setStatus("mandatory")


class _IpGlobalProfile_SntpInfo_Enabled_Type(Integer32):
    """Custom type ipGlobalProfile_SntpInfo_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sntpDisabled", 1),
          ("sntpEnabled", 2),
          ("sntpPassive", 3))
    )


_IpGlobalProfile_SntpInfo_Enabled_Type.__name__ = "Integer32"
_IpGlobalProfile_SntpInfo_Enabled_Object = MibScalar
ipGlobalProfile_SntpInfo_Enabled = _IpGlobalProfile_SntpInfo_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 50),
    _IpGlobalProfile_SntpInfo_Enabled_Type()
)
ipGlobalProfile_SntpInfo_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SntpInfo_Enabled.setStatus("mandatory")


class _IpGlobalProfile_SntpInfo_oGMTOffset_Type(Integer32):
    """Custom type ipGlobalProfile_SntpInfo_oGMTOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-41399,
              -39599,
              -37799,
              -35999,
              -34199,
              -32399,
              -30599,
              -28799,
              -26999,
              -25199,
              -23399,
              -21599,
              -19799,
              -17999,
              -16199,
              -14399,
              -12599,
              -10799,
              -8999,
              -7199,
              -5399,
              -3599,
              -1799,
              1,
              1801,
              3601,
              5401,
              7201,
              9001,
              10801,
              12601,
              14401,
              16201,
              18001,
              19801,
              21601,
              23401,
              25201,
              27001,
              28801,
              30601,
              32401,
              34201,
              36001,
              37801,
              39601,
              41401,
              43201,
              45001,
              46801)
        )
    )
    namedValues = NamedValues(
        *(("utc-plus-0000", 1),
          ("utc-plus-0030", 1801),
          ("utc-plus-0100", 3601),
          ("utc-plus-0130", 5401),
          ("utc-plus-0200", 7201),
          ("utc-plus-0230", 9001),
          ("utc-plus-0300", 10801),
          ("utc-plus-0330", 12601),
          ("utc-plus-0400", 14401),
          ("utc-plus-0430", 16201),
          ("utc-plus-0500", 18001),
          ("utc-plus-0530", 19801),
          ("utc-plus-0600", 21601),
          ("utc-plus-0630", 23401),
          ("utc-plus-0700", 25201),
          ("utc-plus-0730", 27001),
          ("utc-plus-0800", 28801),
          ("utc-plus-0830", 30601),
          ("utc-plus-0900", 32401),
          ("utc-plus-0930", 34201),
          ("utc-plus-1000", 36001),
          ("utc-plus-1030", 37801),
          ("utc-plus-1100", 39601),
          ("utc-plus-1130", 41401),
          ("utc-plus-1200", 43201),
          ("utc-plus-1230", 45001),
          ("utc-plus-1300", 46801),
          ("utc0030", -1799),
          ("utc0100", -3599),
          ("utc0130", -5399),
          ("utc0200", -7199),
          ("utc0230", -8999),
          ("utc0300", -10799),
          ("utc0330", -12599),
          ("utc0400", -14399),
          ("utc0430", -16199),
          ("utc0500", -17999),
          ("utc0530", -19799),
          ("utc0600", -21599),
          ("utc0630", -23399),
          ("utc0700", -25199),
          ("utc0730", -26999),
          ("utc0800", -28799),
          ("utc0830", -30599),
          ("utc0900", -32399),
          ("utc0930", -34199),
          ("utc1000", -35999),
          ("utc1030", -37799),
          ("utc1100", -39599),
          ("utc1130", -41399))
    )


_IpGlobalProfile_SntpInfo_oGMTOffset_Type.__name__ = "Integer32"
_IpGlobalProfile_SntpInfo_oGMTOffset_Object = MibScalar
ipGlobalProfile_SntpInfo_oGMTOffset = _IpGlobalProfile_SntpInfo_oGMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 51),
    _IpGlobalProfile_SntpInfo_oGMTOffset_Type()
)
ipGlobalProfile_SntpInfo_oGMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SntpInfo_oGMTOffset.setStatus("mandatory")
_IpGlobalProfile_SntpInfo_UpdateThreshold_Type = Integer32
_IpGlobalProfile_SntpInfo_UpdateThreshold_Object = MibScalar
ipGlobalProfile_SntpInfo_UpdateThreshold = _IpGlobalProfile_SntpInfo_UpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 52),
    _IpGlobalProfile_SntpInfo_UpdateThreshold_Type()
)
ipGlobalProfile_SntpInfo_UpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SntpInfo_UpdateThreshold.setStatus("mandatory")
_IpGlobalProfile_DnsListSize_Type = Integer32
_IpGlobalProfile_DnsListSize_Object = MibScalar
ipGlobalProfile_DnsListSize = _IpGlobalProfile_DnsListSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 53),
    _IpGlobalProfile_DnsListSize_Type()
)
ipGlobalProfile_DnsListSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsListSize.setStatus("mandatory")
_IpGlobalProfile_ClientPrimaryDnsServer_Type = IpAddress
_IpGlobalProfile_ClientPrimaryDnsServer_Object = MibScalar
ipGlobalProfile_ClientPrimaryDnsServer = _IpGlobalProfile_ClientPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 54),
    _IpGlobalProfile_ClientPrimaryDnsServer_Type()
)
ipGlobalProfile_ClientPrimaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_ClientPrimaryDnsServer.setStatus("mandatory")
_IpGlobalProfile_ClientSecondaryDnsServer_Type = IpAddress
_IpGlobalProfile_ClientSecondaryDnsServer_Object = MibScalar
ipGlobalProfile_ClientSecondaryDnsServer = _IpGlobalProfile_ClientSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 55),
    _IpGlobalProfile_ClientSecondaryDnsServer_Type()
)
ipGlobalProfile_ClientSecondaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_ClientSecondaryDnsServer.setStatus("mandatory")


class _IpGlobalProfile_AllowAsClientDnsInfo_Type(Integer32):
    """Custom type ipGlobalProfile_AllowAsClientDnsInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_IpGlobalProfile_AllowAsClientDnsInfo_Type.__name__ = "Integer32"
_IpGlobalProfile_AllowAsClientDnsInfo_Object = MibScalar
ipGlobalProfile_AllowAsClientDnsInfo = _IpGlobalProfile_AllowAsClientDnsInfo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 56),
    _IpGlobalProfile_AllowAsClientDnsInfo_Type()
)
ipGlobalProfile_AllowAsClientDnsInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_AllowAsClientDnsInfo.setStatus("mandatory")


class _IpGlobalProfile_DnsLocalTable_Enabled_Type(Integer32):
    """Custom type ipGlobalProfile_DnsLocalTable_Enabled based on Integer32"""
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


_IpGlobalProfile_DnsLocalTable_Enabled_Type.__name__ = "Integer32"
_IpGlobalProfile_DnsLocalTable_Enabled_Object = MibScalar
ipGlobalProfile_DnsLocalTable_Enabled = _IpGlobalProfile_DnsLocalTable_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 57),
    _IpGlobalProfile_DnsLocalTable_Enabled_Type()
)
ipGlobalProfile_DnsLocalTable_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsLocalTable_Enabled.setStatus("mandatory")


class _IpGlobalProfile_DnsLocalTable_AutoUpdate_Type(Integer32):
    """Custom type ipGlobalProfile_DnsLocalTable_AutoUpdate based on Integer32"""
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


_IpGlobalProfile_DnsLocalTable_AutoUpdate_Type.__name__ = "Integer32"
_IpGlobalProfile_DnsLocalTable_AutoUpdate_Object = MibScalar
ipGlobalProfile_DnsLocalTable_AutoUpdate = _IpGlobalProfile_DnsLocalTable_AutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 58),
    _IpGlobalProfile_DnsLocalTable_AutoUpdate_Type()
)
ipGlobalProfile_DnsLocalTable_AutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsLocalTable_AutoUpdate.setStatus("mandatory")


class _IpGlobalProfile_MulticastForwarding_Type(Integer32):
    """Custom type ipGlobalProfile_MulticastForwarding based on Integer32"""
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


_IpGlobalProfile_MulticastForwarding_Type.__name__ = "Integer32"
_IpGlobalProfile_MulticastForwarding_Object = MibScalar
ipGlobalProfile_MulticastForwarding = _IpGlobalProfile_MulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 59),
    _IpGlobalProfile_MulticastForwarding_Type()
)
ipGlobalProfile_MulticastForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastForwarding.setStatus("mandatory")
_IpGlobalProfile_MboneProfile_Type = DisplayString
_IpGlobalProfile_MboneProfile_Object = MibScalar
ipGlobalProfile_MboneProfile = _IpGlobalProfile_MboneProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 60),
    _IpGlobalProfile_MboneProfile_Type()
)
ipGlobalProfile_MboneProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneProfile.setStatus("mandatory")


class _IpGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ipGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf based on Integer32"""
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


_IpGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_IpGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf_Object = MibScalar
ipGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf = _IpGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 61),
    _IpGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf_Type()
)
ipGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf.setStatus("mandatory")


class _IpGlobalProfile_MboneLanInterface_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ipGlobalProfile_MboneLanInterface_PhysicalAddress_Slot based on Integer32"""
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


_IpGlobalProfile_MboneLanInterface_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_IpGlobalProfile_MboneLanInterface_PhysicalAddress_Slot_Object = MibScalar
ipGlobalProfile_MboneLanInterface_PhysicalAddress_Slot = _IpGlobalProfile_MboneLanInterface_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 62),
    _IpGlobalProfile_MboneLanInterface_PhysicalAddress_Slot_Type()
)
ipGlobalProfile_MboneLanInterface_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneLanInterface_PhysicalAddress_Slot.setStatus("mandatory")
_IpGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber_Type = Integer32
_IpGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber_Object = MibScalar
ipGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber = _IpGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 63),
    _IpGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber_Type()
)
ipGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber.setStatus("mandatory")
_IpGlobalProfile_MboneLanInterface_LogicalItem_Type = Integer32
_IpGlobalProfile_MboneLanInterface_LogicalItem_Object = MibScalar
ipGlobalProfile_MboneLanInterface_LogicalItem = _IpGlobalProfile_MboneLanInterface_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 64),
    _IpGlobalProfile_MboneLanInterface_LogicalItem_Type()
)
ipGlobalProfile_MboneLanInterface_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneLanInterface_LogicalItem.setStatus("mandatory")
_IpGlobalProfile_MulticastHbeatAddr_Type = IpAddress
_IpGlobalProfile_MulticastHbeatAddr_Object = MibScalar
ipGlobalProfile_MulticastHbeatAddr = _IpGlobalProfile_MulticastHbeatAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 65),
    _IpGlobalProfile_MulticastHbeatAddr_Type()
)
ipGlobalProfile_MulticastHbeatAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastHbeatAddr.setStatus("mandatory")
_IpGlobalProfile_MulticastHbeatPort_Type = Integer32
_IpGlobalProfile_MulticastHbeatPort_Object = MibScalar
ipGlobalProfile_MulticastHbeatPort = _IpGlobalProfile_MulticastHbeatPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 66),
    _IpGlobalProfile_MulticastHbeatPort_Type()
)
ipGlobalProfile_MulticastHbeatPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastHbeatPort.setStatus("mandatory")
_IpGlobalProfile_MulticastHbeatSlotTime_Type = Integer32
_IpGlobalProfile_MulticastHbeatSlotTime_Object = MibScalar
ipGlobalProfile_MulticastHbeatSlotTime = _IpGlobalProfile_MulticastHbeatSlotTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 67),
    _IpGlobalProfile_MulticastHbeatSlotTime_Type()
)
ipGlobalProfile_MulticastHbeatSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastHbeatSlotTime.setStatus("mandatory")
_IpGlobalProfile_MulticastHbeatNumberSlot_Type = Integer32
_IpGlobalProfile_MulticastHbeatNumberSlot_Object = MibScalar
ipGlobalProfile_MulticastHbeatNumberSlot = _IpGlobalProfile_MulticastHbeatNumberSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 68),
    _IpGlobalProfile_MulticastHbeatNumberSlot_Type()
)
ipGlobalProfile_MulticastHbeatNumberSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastHbeatNumberSlot.setStatus("mandatory")
_IpGlobalProfile_MulticastHbeatAlarmThreshold_Type = Integer32
_IpGlobalProfile_MulticastHbeatAlarmThreshold_Object = MibScalar
ipGlobalProfile_MulticastHbeatAlarmThreshold = _IpGlobalProfile_MulticastHbeatAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 69),
    _IpGlobalProfile_MulticastHbeatAlarmThreshold_Type()
)
ipGlobalProfile_MulticastHbeatAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastHbeatAlarmThreshold.setStatus("mandatory")
_IpGlobalProfile_MulticastHbeatSrcAddr_Type = IpAddress
_IpGlobalProfile_MulticastHbeatSrcAddr_Object = MibScalar
ipGlobalProfile_MulticastHbeatSrcAddr = _IpGlobalProfile_MulticastHbeatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 70),
    _IpGlobalProfile_MulticastHbeatSrcAddr_Type()
)
ipGlobalProfile_MulticastHbeatSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastHbeatSrcAddr.setStatus("mandatory")
_IpGlobalProfile_MulticastHbeatSrcAddrMask_Type = IpAddress
_IpGlobalProfile_MulticastHbeatSrcAddrMask_Object = MibScalar
ipGlobalProfile_MulticastHbeatSrcAddrMask = _IpGlobalProfile_MulticastHbeatSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 71),
    _IpGlobalProfile_MulticastHbeatSrcAddrMask_Type()
)
ipGlobalProfile_MulticastHbeatSrcAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastHbeatSrcAddrMask.setStatus("mandatory")
_IpGlobalProfile_SecDomainName_Type = DisplayString
_IpGlobalProfile_SecDomainName_Object = MibScalar
ipGlobalProfile_SecDomainName = _IpGlobalProfile_SecDomainName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 72),
    _IpGlobalProfile_SecDomainName_Type()
)
ipGlobalProfile_SecDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SecDomainName.setStatus("mandatory")
_IpGlobalProfile_MulticastMemberTimeout_Type = Integer32
_IpGlobalProfile_MulticastMemberTimeout_Object = MibScalar
ipGlobalProfile_MulticastMemberTimeout = _IpGlobalProfile_MulticastMemberTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 73),
    _IpGlobalProfile_MulticastMemberTimeout_Type()
)
ipGlobalProfile_MulticastMemberTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MulticastMemberTimeout.setStatus("mandatory")


class _IpGlobalProfile_Finger_Type(Integer32):
    """Custom type ipGlobalProfile_Finger based on Integer32"""
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


_IpGlobalProfile_Finger_Type.__name__ = "Integer32"
_IpGlobalProfile_Finger_Object = MibScalar
ipGlobalProfile_Finger = _IpGlobalProfile_Finger_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 74),
    _IpGlobalProfile_Finger_Type()
)
ipGlobalProfile_Finger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_Finger.setStatus("mandatory")


class _IpGlobalProfile_IgnoreIcmpRedirects_Type(Integer32):
    """Custom type ipGlobalProfile_IgnoreIcmpRedirects based on Integer32"""
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


_IpGlobalProfile_IgnoreIcmpRedirects_Type.__name__ = "Integer32"
_IpGlobalProfile_IgnoreIcmpRedirects_Object = MibScalar
ipGlobalProfile_IgnoreIcmpRedirects = _IpGlobalProfile_IgnoreIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 75),
    _IpGlobalProfile_IgnoreIcmpRedirects_Type()
)
ipGlobalProfile_IgnoreIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IgnoreIcmpRedirects.setStatus("mandatory")


class _IpGlobalProfile_IcmpReplyDirectedBcast_Type(Integer32):
    """Custom type ipGlobalProfile_IcmpReplyDirectedBcast based on Integer32"""
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


_IpGlobalProfile_IcmpReplyDirectedBcast_Type.__name__ = "Integer32"
_IpGlobalProfile_IcmpReplyDirectedBcast_Object = MibScalar
ipGlobalProfile_IcmpReplyDirectedBcast = _IpGlobalProfile_IcmpReplyDirectedBcast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 76),
    _IpGlobalProfile_IcmpReplyDirectedBcast_Type()
)
ipGlobalProfile_IcmpReplyDirectedBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IcmpReplyDirectedBcast.setStatus("mandatory")


class _IpGlobalProfile_SendIcmpDestUnreachable_Type(Integer32):
    """Custom type ipGlobalProfile_SendIcmpDestUnreachable based on Integer32"""
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


_IpGlobalProfile_SendIcmpDestUnreachable_Type.__name__ = "Integer32"
_IpGlobalProfile_SendIcmpDestUnreachable_Object = MibScalar
ipGlobalProfile_SendIcmpDestUnreachable = _IpGlobalProfile_SendIcmpDestUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 77),
    _IpGlobalProfile_SendIcmpDestUnreachable_Type()
)
ipGlobalProfile_SendIcmpDestUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SendIcmpDestUnreachable.setStatus("mandatory")
_IpGlobalProfile_GlobalVrouter_Type = DisplayString
_IpGlobalProfile_GlobalVrouter_Object = MibScalar
ipGlobalProfile_GlobalVrouter = _IpGlobalProfile_GlobalVrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 78),
    _IpGlobalProfile_GlobalVrouter_Type()
)
ipGlobalProfile_GlobalVrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_GlobalVrouter.setStatus("mandatory")
_IpGlobalProfile_RouterId_Type = IpAddress
_IpGlobalProfile_RouterId_Object = MibScalar
ipGlobalProfile_RouterId = _IpGlobalProfile_RouterId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 79),
    _IpGlobalProfile_RouterId_Type()
)
ipGlobalProfile_RouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RouterId.setStatus("mandatory")
_IpGlobalProfile_DefaultFilterCacheTime_Type = Integer32
_IpGlobalProfile_DefaultFilterCacheTime_Object = MibScalar
ipGlobalProfile_DefaultFilterCacheTime = _IpGlobalProfile_DefaultFilterCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 80),
    _IpGlobalProfile_DefaultFilterCacheTime_Type()
)
ipGlobalProfile_DefaultFilterCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DefaultFilterCacheTime.setStatus("mandatory")
_IpGlobalProfile_DefaultPrtCacheTime_Type = Integer32
_IpGlobalProfile_DefaultPrtCacheTime_Object = MibScalar
ipGlobalProfile_DefaultPrtCacheTime = _IpGlobalProfile_DefaultPrtCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 81),
    _IpGlobalProfile_DefaultPrtCacheTime_Type()
)
ipGlobalProfile_DefaultPrtCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DefaultPrtCacheTime.setStatus("mandatory")


class _IpGlobalProfile_TcpSynFloodProtect_Type(Integer32):
    """Custom type ipGlobalProfile_TcpSynFloodProtect based on Integer32"""
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


_IpGlobalProfile_TcpSynFloodProtect_Type.__name__ = "Integer32"
_IpGlobalProfile_TcpSynFloodProtect_Object = MibScalar
ipGlobalProfile_TcpSynFloodProtect = _IpGlobalProfile_TcpSynFloodProtect_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 82),
    _IpGlobalProfile_TcpSynFloodProtect_Type()
)
ipGlobalProfile_TcpSynFloodProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_TcpSynFloodProtect.setStatus("mandatory")


class _IpGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot_Type(Integer32):
    """Custom type ipGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot based on Integer32"""
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


_IpGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot_Type.__name__ = "Integer32"
_IpGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot_Object = MibScalar
ipGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot = _IpGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 83),
    _IpGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot_Type()
)
ipGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot.setStatus("mandatory")


class _IpGlobalProfile_Action_o_Type(Integer32):
    """Custom type ipGlobalProfile_Action_o based on Integer32"""
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


_IpGlobalProfile_Action_o_Type.__name__ = "Integer32"
_IpGlobalProfile_Action_o_Object = MibScalar
ipGlobalProfile_Action_o = _IpGlobalProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 84),
    _IpGlobalProfile_Action_o_Type()
)
ipGlobalProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_Action_o.setStatus("mandatory")
_IpGlobalProfile_MinRipTriggerDelay_Type = Integer32
_IpGlobalProfile_MinRipTriggerDelay_Object = MibScalar
ipGlobalProfile_MinRipTriggerDelay = _IpGlobalProfile_MinRipTriggerDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 85),
    _IpGlobalProfile_MinRipTriggerDelay_Type()
)
ipGlobalProfile_MinRipTriggerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MinRipTriggerDelay.setStatus("mandatory")
_IpGlobalProfile_MaxRipTriggerDelay_Type = Integer32
_IpGlobalProfile_MaxRipTriggerDelay_Object = MibScalar
ipGlobalProfile_MaxRipTriggerDelay = _IpGlobalProfile_MaxRipTriggerDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 86),
    _IpGlobalProfile_MaxRipTriggerDelay_Type()
)
ipGlobalProfile_MaxRipTriggerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MaxRipTriggerDelay.setStatus("mandatory")
_IpGlobalProfile_SntpInfo_UpdateInterval_Type = Integer32
_IpGlobalProfile_SntpInfo_UpdateInterval_Object = MibScalar
ipGlobalProfile_SntpInfo_UpdateInterval = _IpGlobalProfile_SntpInfo_UpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 87),
    _IpGlobalProfile_SntpInfo_UpdateInterval_Type()
)
ipGlobalProfile_SntpInfo_UpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SntpInfo_UpdateInterval.setStatus("mandatory")


class _IpGlobalProfile_IpsecOptions_Enabled_Type(Integer32):
    """Custom type ipGlobalProfile_IpsecOptions_Enabled based on Integer32"""
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


_IpGlobalProfile_IpsecOptions_Enabled_Type.__name__ = "Integer32"
_IpGlobalProfile_IpsecOptions_Enabled_Object = MibScalar
ipGlobalProfile_IpsecOptions_Enabled = _IpGlobalProfile_IpsecOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 88),
    _IpGlobalProfile_IpsecOptions_Enabled_Type()
)
ipGlobalProfile_IpsecOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IpsecOptions_Enabled.setStatus("mandatory")
_IpGlobalProfile_IpsecOptions_SecurityPolicyDatabase_Type = DisplayString
_IpGlobalProfile_IpsecOptions_SecurityPolicyDatabase_Object = MibScalar
ipGlobalProfile_IpsecOptions_SecurityPolicyDatabase = _IpGlobalProfile_IpsecOptions_SecurityPolicyDatabase_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 89),
    _IpGlobalProfile_IpsecOptions_SecurityPolicyDatabase_Type()
)
ipGlobalProfile_IpsecOptions_SecurityPolicyDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_IpsecOptions_SecurityPolicyDatabase.setStatus("mandatory")


class _IpGlobalProfile_DnsCacheEnable_Type(Integer32):
    """Custom type ipGlobalProfile_DnsCacheEnable based on Integer32"""
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


_IpGlobalProfile_DnsCacheEnable_Type.__name__ = "Integer32"
_IpGlobalProfile_DnsCacheEnable_Object = MibScalar
ipGlobalProfile_DnsCacheEnable = _IpGlobalProfile_DnsCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 90),
    _IpGlobalProfile_DnsCacheEnable_Type()
)
ipGlobalProfile_DnsCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsCacheEnable.setStatus("mandatory")
_IpGlobalProfile_DnsAutoUpdateInterval_Type = Integer32
_IpGlobalProfile_DnsAutoUpdateInterval_Object = MibScalar
ipGlobalProfile_DnsAutoUpdateInterval = _IpGlobalProfile_DnsAutoUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 91),
    _IpGlobalProfile_DnsAutoUpdateInterval_Type()
)
ipGlobalProfile_DnsAutoUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsAutoUpdateInterval.setStatus("mandatory")
_IpGlobalProfile_MboneTimeout_Type = Integer32
_IpGlobalProfile_MboneTimeout_Object = MibScalar
ipGlobalProfile_MboneTimeout = _IpGlobalProfile_MboneTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 92),
    _IpGlobalProfile_MboneTimeout_Type()
)
ipGlobalProfile_MboneTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneTimeout.setStatus("mandatory")
_IpGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes_Type = Integer32
_IpGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes_Object = MibScalar
ipGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes = _IpGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 1, 1, 93),
    _IpGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes_Type()
)
ipGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes.setStatus("mandatory")
_MibipGlobalProfile_DnsLocalTable_TableConfigTable_Object = MibTable
mibipGlobalProfile_DnsLocalTable_TableConfigTable = _MibipGlobalProfile_DnsLocalTable_TableConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 2)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_DnsLocalTable_TableConfigTable.setStatus("mandatory")
_MibipGlobalProfile_DnsLocalTable_TableConfigEntry_Object = MibTableRow
mibipGlobalProfile_DnsLocalTable_TableConfigEntry = _MibipGlobalProfile_DnsLocalTable_TableConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 2, 1)
)
mibipGlobalProfile_DnsLocalTable_TableConfigEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-DnsLocalTable-TableConfig-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-DnsLocalTable-TableConfig-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_DnsLocalTable_TableConfigEntry.setStatus("mandatory")
_IpGlobalProfile_DnsLocalTable_TableConfig_Index_o_Type = Integer32
_IpGlobalProfile_DnsLocalTable_TableConfig_Index_o_Object = MibScalar
ipGlobalProfile_DnsLocalTable_TableConfig_Index_o = _IpGlobalProfile_DnsLocalTable_TableConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 2, 1, 1),
    _IpGlobalProfile_DnsLocalTable_TableConfig_Index_o_Type()
)
ipGlobalProfile_DnsLocalTable_TableConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsLocalTable_TableConfig_Index_o.setStatus("mandatory")
_IpGlobalProfile_DnsLocalTable_TableConfig_Index1_o_Type = Integer32
_IpGlobalProfile_DnsLocalTable_TableConfig_Index1_o_Object = MibScalar
ipGlobalProfile_DnsLocalTable_TableConfig_Index1_o = _IpGlobalProfile_DnsLocalTable_TableConfig_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 2, 1, 2),
    _IpGlobalProfile_DnsLocalTable_TableConfig_Index1_o_Type()
)
ipGlobalProfile_DnsLocalTable_TableConfig_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsLocalTable_TableConfig_Index1_o.setStatus("mandatory")
_IpGlobalProfile_DnsLocalTable_TableConfig_HostName_Type = DisplayString
_IpGlobalProfile_DnsLocalTable_TableConfig_HostName_Object = MibScalar
ipGlobalProfile_DnsLocalTable_TableConfig_HostName = _IpGlobalProfile_DnsLocalTable_TableConfig_HostName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 2, 1, 3),
    _IpGlobalProfile_DnsLocalTable_TableConfig_HostName_Type()
)
ipGlobalProfile_DnsLocalTable_TableConfig_HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsLocalTable_TableConfig_HostName.setStatus("mandatory")
_IpGlobalProfile_DnsLocalTable_TableConfig_IpAddress_Type = IpAddress
_IpGlobalProfile_DnsLocalTable_TableConfig_IpAddress_Object = MibScalar
ipGlobalProfile_DnsLocalTable_TableConfig_IpAddress = _IpGlobalProfile_DnsLocalTable_TableConfig_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 2, 1, 4),
    _IpGlobalProfile_DnsLocalTable_TableConfig_IpAddress_Type()
)
ipGlobalProfile_DnsLocalTable_TableConfig_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DnsLocalTable_TableConfig_IpAddress.setStatus("mandatory")
_MibipGlobalProfile_SntpInfo_HostTable_Object = MibTable
mibipGlobalProfile_SntpInfo_HostTable = _MibipGlobalProfile_SntpInfo_HostTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 3)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_SntpInfo_HostTable.setStatus("mandatory")
_MibipGlobalProfile_SntpInfo_HostEntry_Object = MibTableRow
mibipGlobalProfile_SntpInfo_HostEntry = _MibipGlobalProfile_SntpInfo_HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 3, 1)
)
mibipGlobalProfile_SntpInfo_HostEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-SntpInfo-Host-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-SntpInfo-Host-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_SntpInfo_HostEntry.setStatus("mandatory")
_IpGlobalProfile_SntpInfo_Host_Index_o_Type = Integer32
_IpGlobalProfile_SntpInfo_Host_Index_o_Object = MibScalar
ipGlobalProfile_SntpInfo_Host_Index_o = _IpGlobalProfile_SntpInfo_Host_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 3, 1, 1),
    _IpGlobalProfile_SntpInfo_Host_Index_o_Type()
)
ipGlobalProfile_SntpInfo_Host_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_SntpInfo_Host_Index_o.setStatus("mandatory")
_IpGlobalProfile_SntpInfo_Host_Index1_o_Type = Integer32
_IpGlobalProfile_SntpInfo_Host_Index1_o_Object = MibScalar
ipGlobalProfile_SntpInfo_Host_Index1_o = _IpGlobalProfile_SntpInfo_Host_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 3, 1, 2),
    _IpGlobalProfile_SntpInfo_Host_Index1_o_Type()
)
ipGlobalProfile_SntpInfo_Host_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_SntpInfo_Host_Index1_o.setStatus("mandatory")
_IpGlobalProfile_SntpInfo_Host_Type = IpAddress
_IpGlobalProfile_SntpInfo_Host_Object = MibScalar
ipGlobalProfile_SntpInfo_Host = _IpGlobalProfile_SntpInfo_Host_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 3, 1, 3),
    _IpGlobalProfile_SntpInfo_Host_Type()
)
ipGlobalProfile_SntpInfo_Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_SntpInfo_Host.setStatus("mandatory")
_MibipGlobalProfile_BootpRelay_BootpServersTable_Object = MibTable
mibipGlobalProfile_BootpRelay_BootpServersTable = _MibipGlobalProfile_BootpRelay_BootpServersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 4)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_BootpRelay_BootpServersTable.setStatus("mandatory")
_MibipGlobalProfile_BootpRelay_BootpServersEntry_Object = MibTableRow
mibipGlobalProfile_BootpRelay_BootpServersEntry = _MibipGlobalProfile_BootpRelay_BootpServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 4, 1)
)
mibipGlobalProfile_BootpRelay_BootpServersEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-BootpRelay-BootpServers-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-BootpRelay-BootpServers-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_BootpRelay_BootpServersEntry.setStatus("mandatory")
_IpGlobalProfile_BootpRelay_BootpServers_Index_o_Type = Integer32
_IpGlobalProfile_BootpRelay_BootpServers_Index_o_Object = MibScalar
ipGlobalProfile_BootpRelay_BootpServers_Index_o = _IpGlobalProfile_BootpRelay_BootpServers_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 4, 1, 1),
    _IpGlobalProfile_BootpRelay_BootpServers_Index_o_Type()
)
ipGlobalProfile_BootpRelay_BootpServers_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_BootpRelay_BootpServers_Index_o.setStatus("mandatory")
_IpGlobalProfile_BootpRelay_BootpServers_Index1_o_Type = Integer32
_IpGlobalProfile_BootpRelay_BootpServers_Index1_o_Object = MibScalar
ipGlobalProfile_BootpRelay_BootpServers_Index1_o = _IpGlobalProfile_BootpRelay_BootpServers_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 4, 1, 2),
    _IpGlobalProfile_BootpRelay_BootpServers_Index1_o_Type()
)
ipGlobalProfile_BootpRelay_BootpServers_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_BootpRelay_BootpServers_Index1_o.setStatus("mandatory")
_IpGlobalProfile_BootpRelay_BootpServers_Type = IpAddress
_IpGlobalProfile_BootpRelay_BootpServers_Object = MibScalar
ipGlobalProfile_BootpRelay_BootpServers = _IpGlobalProfile_BootpRelay_BootpServers_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 4, 1, 3),
    _IpGlobalProfile_BootpRelay_BootpServers_Type()
)
ipGlobalProfile_BootpRelay_BootpServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_BootpRelay_BootpServers.setStatus("mandatory")
_MibipGlobalProfile_PoolNameTable_Object = MibTable
mibipGlobalProfile_PoolNameTable = _MibipGlobalProfile_PoolNameTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 5)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_PoolNameTable.setStatus("mandatory")
_MibipGlobalProfile_PoolNameEntry_Object = MibTableRow
mibipGlobalProfile_PoolNameEntry = _MibipGlobalProfile_PoolNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 5, 1)
)
mibipGlobalProfile_PoolNameEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-PoolName-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-PoolName-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_PoolNameEntry.setStatus("mandatory")
_IpGlobalProfile_PoolName_Index_o_Type = Integer32
_IpGlobalProfile_PoolName_Index_o_Object = MibScalar
ipGlobalProfile_PoolName_Index_o = _IpGlobalProfile_PoolName_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 5, 1, 1),
    _IpGlobalProfile_PoolName_Index_o_Type()
)
ipGlobalProfile_PoolName_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolName_Index_o.setStatus("mandatory")
_IpGlobalProfile_PoolName_Index1_o_Type = Integer32
_IpGlobalProfile_PoolName_Index1_o_Object = MibScalar
ipGlobalProfile_PoolName_Index1_o = _IpGlobalProfile_PoolName_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 5, 1, 2),
    _IpGlobalProfile_PoolName_Index1_o_Type()
)
ipGlobalProfile_PoolName_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolName_Index1_o.setStatus("mandatory")
_IpGlobalProfile_PoolName_Type = DisplayString
_IpGlobalProfile_PoolName_Object = MibScalar
ipGlobalProfile_PoolName = _IpGlobalProfile_PoolName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 5, 1, 3),
    _IpGlobalProfile_PoolName_Type()
)
ipGlobalProfile_PoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolName.setStatus("mandatory")
_MibipGlobalProfile_AssignCountTable_Object = MibTable
mibipGlobalProfile_AssignCountTable = _MibipGlobalProfile_AssignCountTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 6)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_AssignCountTable.setStatus("mandatory")
_MibipGlobalProfile_AssignCountEntry_Object = MibTableRow
mibipGlobalProfile_AssignCountEntry = _MibipGlobalProfile_AssignCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 6, 1)
)
mibipGlobalProfile_AssignCountEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-AssignCount-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-AssignCount-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_AssignCountEntry.setStatus("mandatory")
_IpGlobalProfile_AssignCount_Index_o_Type = Integer32
_IpGlobalProfile_AssignCount_Index_o_Object = MibScalar
ipGlobalProfile_AssignCount_Index_o = _IpGlobalProfile_AssignCount_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 6, 1, 1),
    _IpGlobalProfile_AssignCount_Index_o_Type()
)
ipGlobalProfile_AssignCount_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_AssignCount_Index_o.setStatus("mandatory")
_IpGlobalProfile_AssignCount_Index1_o_Type = Integer32
_IpGlobalProfile_AssignCount_Index1_o_Object = MibScalar
ipGlobalProfile_AssignCount_Index1_o = _IpGlobalProfile_AssignCount_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 6, 1, 2),
    _IpGlobalProfile_AssignCount_Index1_o_Type()
)
ipGlobalProfile_AssignCount_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_AssignCount_Index1_o.setStatus("mandatory")
_IpGlobalProfile_AssignCount_Type = Integer32
_IpGlobalProfile_AssignCount_Object = MibScalar
ipGlobalProfile_AssignCount = _IpGlobalProfile_AssignCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 6, 1, 3),
    _IpGlobalProfile_AssignCount_Type()
)
ipGlobalProfile_AssignCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_AssignCount.setStatus("mandatory")
_MibipGlobalProfile_PoolBaseAddressTable_Object = MibTable
mibipGlobalProfile_PoolBaseAddressTable = _MibipGlobalProfile_PoolBaseAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 7)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_PoolBaseAddressTable.setStatus("mandatory")
_MibipGlobalProfile_PoolBaseAddressEntry_Object = MibTableRow
mibipGlobalProfile_PoolBaseAddressEntry = _MibipGlobalProfile_PoolBaseAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 7, 1)
)
mibipGlobalProfile_PoolBaseAddressEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-PoolBaseAddress-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-PoolBaseAddress-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_PoolBaseAddressEntry.setStatus("mandatory")
_IpGlobalProfile_PoolBaseAddress_Index_o_Type = Integer32
_IpGlobalProfile_PoolBaseAddress_Index_o_Object = MibScalar
ipGlobalProfile_PoolBaseAddress_Index_o = _IpGlobalProfile_PoolBaseAddress_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 7, 1, 1),
    _IpGlobalProfile_PoolBaseAddress_Index_o_Type()
)
ipGlobalProfile_PoolBaseAddress_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolBaseAddress_Index_o.setStatus("mandatory")
_IpGlobalProfile_PoolBaseAddress_Index1_o_Type = Integer32
_IpGlobalProfile_PoolBaseAddress_Index1_o_Object = MibScalar
ipGlobalProfile_PoolBaseAddress_Index1_o = _IpGlobalProfile_PoolBaseAddress_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 7, 1, 2),
    _IpGlobalProfile_PoolBaseAddress_Index1_o_Type()
)
ipGlobalProfile_PoolBaseAddress_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolBaseAddress_Index1_o.setStatus("mandatory")
_IpGlobalProfile_PoolBaseAddress_Type = IpAddress
_IpGlobalProfile_PoolBaseAddress_Object = MibScalar
ipGlobalProfile_PoolBaseAddress = _IpGlobalProfile_PoolBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 7, 1, 3),
    _IpGlobalProfile_PoolBaseAddress_Type()
)
ipGlobalProfile_PoolBaseAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_PoolBaseAddress.setStatus("mandatory")
_MibipGlobalProfile_DhcpServer_StaticAddressTable_Object = MibTable
mibipGlobalProfile_DhcpServer_StaticAddressTable = _MibipGlobalProfile_DhcpServer_StaticAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 8)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_DhcpServer_StaticAddressTable.setStatus("mandatory")
_MibipGlobalProfile_DhcpServer_StaticAddressEntry_Object = MibTableRow
mibipGlobalProfile_DhcpServer_StaticAddressEntry = _MibipGlobalProfile_DhcpServer_StaticAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 8, 1)
)
mibipGlobalProfile_DhcpServer_StaticAddressEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-DhcpServer-StaticAddress-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-DhcpServer-StaticAddress-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_DhcpServer_StaticAddressEntry.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_StaticAddress_Index_o_Type = Integer32
_IpGlobalProfile_DhcpServer_StaticAddress_Index_o_Object = MibScalar
ipGlobalProfile_DhcpServer_StaticAddress_Index_o = _IpGlobalProfile_DhcpServer_StaticAddress_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 8, 1, 1),
    _IpGlobalProfile_DhcpServer_StaticAddress_Index_o_Type()
)
ipGlobalProfile_DhcpServer_StaticAddress_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_StaticAddress_Index_o.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_StaticAddress_Index1_o_Type = Integer32
_IpGlobalProfile_DhcpServer_StaticAddress_Index1_o_Object = MibScalar
ipGlobalProfile_DhcpServer_StaticAddress_Index1_o = _IpGlobalProfile_DhcpServer_StaticAddress_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 8, 1, 2),
    _IpGlobalProfile_DhcpServer_StaticAddress_Index1_o_Type()
)
ipGlobalProfile_DhcpServer_StaticAddress_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_StaticAddress_Index1_o.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_StaticAddress_IpAddress_Type = IpAddress
_IpGlobalProfile_DhcpServer_StaticAddress_IpAddress_Object = MibScalar
ipGlobalProfile_DhcpServer_StaticAddress_IpAddress = _IpGlobalProfile_DhcpServer_StaticAddress_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 8, 1, 3),
    _IpGlobalProfile_DhcpServer_StaticAddress_IpAddress_Type()
)
ipGlobalProfile_DhcpServer_StaticAddress_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_StaticAddress_IpAddress.setStatus("mandatory")
_IpGlobalProfile_DhcpServer_StaticAddress_EthernetAddress_Type = DisplayString
_IpGlobalProfile_DhcpServer_StaticAddress_EthernetAddress_Object = MibScalar
ipGlobalProfile_DhcpServer_StaticAddress_EthernetAddress = _IpGlobalProfile_DhcpServer_StaticAddress_EthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 8, 1, 4),
    _IpGlobalProfile_DhcpServer_StaticAddress_EthernetAddress_Type()
)
ipGlobalProfile_DhcpServer_StaticAddress_EthernetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_DhcpServer_StaticAddress_EthernetAddress.setStatus("mandatory")
_MibipGlobalProfile_MboneBackupTable_Object = MibTable
mibipGlobalProfile_MboneBackupTable = _MibipGlobalProfile_MboneBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9)
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_MboneBackupTable.setStatus("mandatory")
_MibipGlobalProfile_MboneBackupEntry_Object = MibTableRow
mibipGlobalProfile_MboneBackupEntry = _MibipGlobalProfile_MboneBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1)
)
mibipGlobalProfile_MboneBackupEntry.setIndexNames(
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-MboneBackup-Index-o"),
    (0, "ASCEND-MIBIP-MIB", "ipGlobalProfile-MboneBackup-Index1-o"),
)
if mibBuilder.loadTexts:
    mibipGlobalProfile_MboneBackupEntry.setStatus("mandatory")
_IpGlobalProfile_MboneBackup_Index_o_Type = Integer32
_IpGlobalProfile_MboneBackup_Index_o_Object = MibScalar
ipGlobalProfile_MboneBackup_Index_o = _IpGlobalProfile_MboneBackup_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 1),
    _IpGlobalProfile_MboneBackup_Index_o_Type()
)
ipGlobalProfile_MboneBackup_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_Index_o.setStatus("mandatory")
_IpGlobalProfile_MboneBackup_Index1_o_Type = Integer32
_IpGlobalProfile_MboneBackup_Index1_o_Object = MibScalar
ipGlobalProfile_MboneBackup_Index1_o = _IpGlobalProfile_MboneBackup_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 2),
    _IpGlobalProfile_MboneBackup_Index1_o_Type()
)
ipGlobalProfile_MboneBackup_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_Index1_o.setStatus("mandatory")


class _IpGlobalProfile_MboneBackup_Enabled_Type(Integer32):
    """Custom type ipGlobalProfile_MboneBackup_Enabled based on Integer32"""
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


_IpGlobalProfile_MboneBackup_Enabled_Type.__name__ = "Integer32"
_IpGlobalProfile_MboneBackup_Enabled_Object = MibScalar
ipGlobalProfile_MboneBackup_Enabled = _IpGlobalProfile_MboneBackup_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 3),
    _IpGlobalProfile_MboneBackup_Enabled_Type()
)
ipGlobalProfile_MboneBackup_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_Enabled.setStatus("mandatory")
_IpGlobalProfile_MboneBackup_MboneProfile_Type = DisplayString
_IpGlobalProfile_MboneBackup_MboneProfile_Object = MibScalar
ipGlobalProfile_MboneBackup_MboneProfile = _IpGlobalProfile_MboneBackup_MboneProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 4),
    _IpGlobalProfile_MboneBackup_MboneProfile_Type()
)
ipGlobalProfile_MboneBackup_MboneProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_MboneProfile.setStatus("mandatory")


class _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf based on Integer32"""
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


_IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf_Object = MibScalar
ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf = _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 5),
    _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf_Type()
)
ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf.setStatus("mandatory")


class _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot based on Integer32"""
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


_IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot_Object = MibScalar
ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot = _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 6),
    _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot_Type()
)
ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot.setStatus("mandatory")
_IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber_Type = Integer32
_IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber_Object = MibScalar
ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber = _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 7),
    _IpGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber_Type()
)
ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber.setStatus("mandatory")
_IpGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem_Type = Integer32
_IpGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem_Object = MibScalar
ipGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem = _IpGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 8),
    _IpGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem_Type()
)
ipGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem.setStatus("mandatory")
_IpGlobalProfile_MboneBackup_MboneTimeout_Type = Integer32
_IpGlobalProfile_MboneBackup_MboneTimeout_Object = MibScalar
ipGlobalProfile_MboneBackup_MboneTimeout = _IpGlobalProfile_MboneBackup_MboneTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 83, 9, 1, 9),
    _IpGlobalProfile_MboneBackup_MboneTimeout_Type()
)
ipGlobalProfile_MboneBackup_MboneTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalProfile_MboneBackup_MboneTimeout.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIP-MIB",
    **{"DisplayString": DisplayString,
       "mibipInterfaceProfile": mibipInterfaceProfile,
       "mibipInterfaceProfileTable": mibipInterfaceProfileTable,
       "mibipInterfaceProfileEntry": mibipInterfaceProfileEntry,
       "ipInterfaceProfile-Shelf-o": ipInterfaceProfile_Shelf_o,
       "ipInterfaceProfile-Slot-o": ipInterfaceProfile_Slot_o,
       "ipInterfaceProfile-Item-o": ipInterfaceProfile_Item_o,
       "ipInterfaceProfile-LogicalItem-o": ipInterfaceProfile_LogicalItem_o,
       "ipInterfaceProfile-InterfaceAddress-PhysicalAddress-Shelf": ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf,
       "ipInterfaceProfile-InterfaceAddress-PhysicalAddress-Slot": ipInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot,
       "ipInterfaceProfile-InterfaceAddress-PhysicalAddress-ItemNumber": ipInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber,
       "ipInterfaceProfile-InterfaceAddress-LogicalItem": ipInterfaceProfile_InterfaceAddress_LogicalItem,
       "ipInterfaceProfile-IpAddress": ipInterfaceProfile_IpAddress,
       "ipInterfaceProfile-o2ndIpAddress": ipInterfaceProfile_o2ndIpAddress,
       "ipInterfaceProfile-ProxyMode": ipInterfaceProfile_ProxyMode,
       "ipInterfaceProfile-RipMode": ipInterfaceProfile_RipMode,
       "ipInterfaceProfile-o2ndRipMode": ipInterfaceProfile_o2ndRipMode,
       "ipInterfaceProfile-RouteFilter": ipInterfaceProfile_RouteFilter,
       "ipInterfaceProfile-Rip2UseMulticast": ipInterfaceProfile_Rip2UseMulticast,
       "ipInterfaceProfile-Ospf-Active": ipInterfaceProfile_Ospf_Active,
       "ipInterfaceProfile-Ospf-Area": ipInterfaceProfile_Ospf_Area,
       "ipInterfaceProfile-Ospf-AreaType": ipInterfaceProfile_Ospf_AreaType,
       "ipInterfaceProfile-Ospf-HelloInterval": ipInterfaceProfile_Ospf_HelloInterval,
       "ipInterfaceProfile-Ospf-DeadInterval": ipInterfaceProfile_Ospf_DeadInterval,
       "ipInterfaceProfile-Ospf-Priority": ipInterfaceProfile_Ospf_Priority,
       "ipInterfaceProfile-Ospf-AuthenType": ipInterfaceProfile_Ospf_AuthenType,
       "ipInterfaceProfile-Ospf-AuthKey": ipInterfaceProfile_Ospf_AuthKey,
       "ipInterfaceProfile-Ospf-KeyId": ipInterfaceProfile_Ospf_KeyId,
       "ipInterfaceProfile-Ospf-Cost": ipInterfaceProfile_Ospf_Cost,
       "ipInterfaceProfile-Ospf-DownCost": ipInterfaceProfile_Ospf_DownCost,
       "ipInterfaceProfile-Ospf-AseType": ipInterfaceProfile_Ospf_AseType,
       "ipInterfaceProfile-Ospf-AseTag": ipInterfaceProfile_Ospf_AseTag,
       "ipInterfaceProfile-Ospf-TransitDelay": ipInterfaceProfile_Ospf_TransitDelay,
       "ipInterfaceProfile-Ospf-RetransmitInterval": ipInterfaceProfile_Ospf_RetransmitInterval,
       "ipInterfaceProfile-Ospf-NonMulticast": ipInterfaceProfile_Ospf_NonMulticast,
       "ipInterfaceProfile-Ospf-NetworkType": ipInterfaceProfile_Ospf_NetworkType,
       "ipInterfaceProfile-Ospf-PollInterval": ipInterfaceProfile_Ospf_PollInterval,
       "ipInterfaceProfile-Ospf-Md5AuthKey": ipInterfaceProfile_Ospf_Md5AuthKey,
       "ipInterfaceProfile-MulticastAllowed": ipInterfaceProfile_MulticastAllowed,
       "ipInterfaceProfile-MulticastRateLimit": ipInterfaceProfile_MulticastRateLimit,
       "ipInterfaceProfile-MulticastGroupLeaveDelay": ipInterfaceProfile_MulticastGroupLeaveDelay,
       "ipInterfaceProfile-DirectedBroadcastAllowed": ipInterfaceProfile_DirectedBroadcastAllowed,
       "ipInterfaceProfile-Vrouter": ipInterfaceProfile_Vrouter,
       "ipInterfaceProfile-ManagementOnlyInterface": ipInterfaceProfile_ManagementOnlyInterface,
       "ipInterfaceProfile-DhcpClientEnabled": ipInterfaceProfile_DhcpClientEnabled,
       "ipInterfaceProfile-Action-o": ipInterfaceProfile_Action_o,
       "ipInterfaceProfile-Netmask": ipInterfaceProfile_Netmask,
       "ipInterfaceProfile-Netmask2": ipInterfaceProfile_Netmask2,
       "ipInterfaceProfile-NatProfileName": ipInterfaceProfile_NatProfileName,
       "ipInterfaceProfile-AddressRealm": ipInterfaceProfile_AddressRealm,
       "ipInterfaceProfile-VlanEnabled": ipInterfaceProfile_VlanEnabled,
       "mibipGlobalProfile": mibipGlobalProfile,
       "mibipGlobalProfileTable": mibipGlobalProfileTable,
       "mibipGlobalProfileEntry": mibipGlobalProfileEntry,
       "ipGlobalProfile-Index-o": ipGlobalProfile_Index_o,
       "ipGlobalProfile-DomainName": ipGlobalProfile_DomainName,
       "ipGlobalProfile-DnsPrimaryServer": ipGlobalProfile_DnsPrimaryServer,
       "ipGlobalProfile-DhcpServer-Active": ipGlobalProfile_DhcpServer_Active,
       "ipGlobalProfile-DhcpServer-LeaseDuration": ipGlobalProfile_DhcpServer_LeaseDuration,
       "ipGlobalProfile-DhcpServer-DefaultPool": ipGlobalProfile_DhcpServer_DefaultPool,
       "ipGlobalProfile-DhcpServer-DefaultMaxLease": ipGlobalProfile_DhcpServer_DefaultMaxLease,
       "ipGlobalProfile-DhcpServer-DefaultLeaseDuration": ipGlobalProfile_DhcpServer_DefaultLeaseDuration,
       "ipGlobalProfile-DhcpServer-TftpHostName": ipGlobalProfile_DhcpServer_TftpHostName,
       "ipGlobalProfile-DhcpServer-BootFilePath": ipGlobalProfile_DhcpServer_BootFilePath,
       "ipGlobalProfile-DhcpServer-ServerAddress": ipGlobalProfile_DhcpServer_ServerAddress,
       "ipGlobalProfile-DnsSecondaryServer": ipGlobalProfile_DnsSecondaryServer,
       "ipGlobalProfile-DnsServerQueryType": ipGlobalProfile_DnsServerQueryType,
       "ipGlobalProfile-SystemIpAddr": ipGlobalProfile_SystemIpAddr,
       "ipGlobalProfile-NetbiosPrimaryNs": ipGlobalProfile_NetbiosPrimaryNs,
       "ipGlobalProfile-NetbiosSecondaryNs": ipGlobalProfile_NetbiosSecondaryNs,
       "ipGlobalProfile-MustAcceptAddressAssign": ipGlobalProfile_MustAcceptAddressAssign,
       "ipGlobalProfile-PoolSummary": ipGlobalProfile_PoolSummary,
       "ipGlobalProfile-PoolChaining": ipGlobalProfile_PoolChaining,
       "ipGlobalProfile-PoolOspfAdvType": ipGlobalProfile_PoolOspfAdvType,
       "ipGlobalProfile-RipPolicy": ipGlobalProfile_RipPolicy,
       "ipGlobalProfile-SummarizeRipRoutes": ipGlobalProfile_SummarizeRipRoutes,
       "ipGlobalProfile-RipTrigger": ipGlobalProfile_RipTrigger,
       "ipGlobalProfile-BootpEnabled": ipGlobalProfile_BootpEnabled,
       "ipGlobalProfile-BootpRelay-Active": ipGlobalProfile_BootpRelay_Active,
       "ipGlobalProfile-DropSourceRoutedIpPackets": ipGlobalProfile_DropSourceRoutedIpPackets,
       "ipGlobalProfile-IgnoreDefRoute": ipGlobalProfile_IgnoreDefRoute,
       "ipGlobalProfile-RarpEnabled": ipGlobalProfile_RarpEnabled,
       "ipGlobalProfile-UdpCksum": ipGlobalProfile_UdpCksum,
       "ipGlobalProfile-TcpTimeout": ipGlobalProfile_TcpTimeout,
       "ipGlobalProfile-DialoutPoison": ipGlobalProfile_DialoutPoison,
       "ipGlobalProfile-TelnetPassword": ipGlobalProfile_TelnetPassword,
       "ipGlobalProfile-UserProfile": ipGlobalProfile_UserProfile,
       "ipGlobalProfile-SharedProf": ipGlobalProfile_SharedProf,
       "ipGlobalProfile-DnsListAttempt": ipGlobalProfile_DnsListAttempt,
       "ipGlobalProfile-StaticPref": ipGlobalProfile_StaticPref,
       "ipGlobalProfile-RipPref": ipGlobalProfile_RipPref,
       "ipGlobalProfile-RipQueueDepth": ipGlobalProfile_RipQueueDepth,
       "ipGlobalProfile-OspfPref": ipGlobalProfile_OspfPref,
       "ipGlobalProfile-OspfAsePref": ipGlobalProfile_OspfAsePref,
       "ipGlobalProfile-OspfGlobal-Enable": ipGlobalProfile_OspfGlobal_Enable,
       "ipGlobalProfile-OspfGlobal-AsBoundaryRouter": ipGlobalProfile_OspfGlobal_AsBoundaryRouter,
       "ipGlobalProfile-OspfGlobal-OspfMaxLsa": ipGlobalProfile_OspfGlobal_OspfMaxLsa,
       "ipGlobalProfile-RipTag": ipGlobalProfile_RipTag,
       "ipGlobalProfile-RipAseType": ipGlobalProfile_RipAseType,
       "ipGlobalProfile-IprouteCacheEnable": ipGlobalProfile_IprouteCacheEnable,
       "ipGlobalProfile-IprouteCacheSize": ipGlobalProfile_IprouteCacheSize,
       "ipGlobalProfile-IpportCacheEnable": ipGlobalProfile_IpportCacheEnable,
       "ipGlobalProfile-SuppressHostRoutes": ipGlobalProfile_SuppressHostRoutes,
       "ipGlobalProfile-SntpInfo-Enabled": ipGlobalProfile_SntpInfo_Enabled,
       "ipGlobalProfile-SntpInfo-oGMTOffset": ipGlobalProfile_SntpInfo_oGMTOffset,
       "ipGlobalProfile-SntpInfo-UpdateThreshold": ipGlobalProfile_SntpInfo_UpdateThreshold,
       "ipGlobalProfile-DnsListSize": ipGlobalProfile_DnsListSize,
       "ipGlobalProfile-ClientPrimaryDnsServer": ipGlobalProfile_ClientPrimaryDnsServer,
       "ipGlobalProfile-ClientSecondaryDnsServer": ipGlobalProfile_ClientSecondaryDnsServer,
       "ipGlobalProfile-AllowAsClientDnsInfo": ipGlobalProfile_AllowAsClientDnsInfo,
       "ipGlobalProfile-DnsLocalTable-Enabled": ipGlobalProfile_DnsLocalTable_Enabled,
       "ipGlobalProfile-DnsLocalTable-AutoUpdate": ipGlobalProfile_DnsLocalTable_AutoUpdate,
       "ipGlobalProfile-MulticastForwarding": ipGlobalProfile_MulticastForwarding,
       "ipGlobalProfile-MboneProfile": ipGlobalProfile_MboneProfile,
       "ipGlobalProfile-MboneLanInterface-PhysicalAddress-Shelf": ipGlobalProfile_MboneLanInterface_PhysicalAddress_Shelf,
       "ipGlobalProfile-MboneLanInterface-PhysicalAddress-Slot": ipGlobalProfile_MboneLanInterface_PhysicalAddress_Slot,
       "ipGlobalProfile-MboneLanInterface-PhysicalAddress-ItemNumber": ipGlobalProfile_MboneLanInterface_PhysicalAddress_ItemNumber,
       "ipGlobalProfile-MboneLanInterface-LogicalItem": ipGlobalProfile_MboneLanInterface_LogicalItem,
       "ipGlobalProfile-MulticastHbeatAddr": ipGlobalProfile_MulticastHbeatAddr,
       "ipGlobalProfile-MulticastHbeatPort": ipGlobalProfile_MulticastHbeatPort,
       "ipGlobalProfile-MulticastHbeatSlotTime": ipGlobalProfile_MulticastHbeatSlotTime,
       "ipGlobalProfile-MulticastHbeatNumberSlot": ipGlobalProfile_MulticastHbeatNumberSlot,
       "ipGlobalProfile-MulticastHbeatAlarmThreshold": ipGlobalProfile_MulticastHbeatAlarmThreshold,
       "ipGlobalProfile-MulticastHbeatSrcAddr": ipGlobalProfile_MulticastHbeatSrcAddr,
       "ipGlobalProfile-MulticastHbeatSrcAddrMask": ipGlobalProfile_MulticastHbeatSrcAddrMask,
       "ipGlobalProfile-SecDomainName": ipGlobalProfile_SecDomainName,
       "ipGlobalProfile-MulticastMemberTimeout": ipGlobalProfile_MulticastMemberTimeout,
       "ipGlobalProfile-Finger": ipGlobalProfile_Finger,
       "ipGlobalProfile-IgnoreIcmpRedirects": ipGlobalProfile_IgnoreIcmpRedirects,
       "ipGlobalProfile-IcmpReplyDirectedBcast": ipGlobalProfile_IcmpReplyDirectedBcast,
       "ipGlobalProfile-SendIcmpDestUnreachable": ipGlobalProfile_SendIcmpDestUnreachable,
       "ipGlobalProfile-GlobalVrouter": ipGlobalProfile_GlobalVrouter,
       "ipGlobalProfile-RouterId": ipGlobalProfile_RouterId,
       "ipGlobalProfile-DefaultFilterCacheTime": ipGlobalProfile_DefaultFilterCacheTime,
       "ipGlobalProfile-DefaultPrtCacheTime": ipGlobalProfile_DefaultPrtCacheTime,
       "ipGlobalProfile-TcpSynFloodProtect": ipGlobalProfile_TcpSynFloodProtect,
       "ipGlobalProfile-ThrottleNoPortMatchUdpTrafficOnSlot": ipGlobalProfile_ThrottleNoPortMatchUdpTrafficOnSlot,
       "ipGlobalProfile-Action-o": ipGlobalProfile_Action_o,
       "ipGlobalProfile-MinRipTriggerDelay": ipGlobalProfile_MinRipTriggerDelay,
       "ipGlobalProfile-MaxRipTriggerDelay": ipGlobalProfile_MaxRipTriggerDelay,
       "ipGlobalProfile-SntpInfo-UpdateInterval": ipGlobalProfile_SntpInfo_UpdateInterval,
       "ipGlobalProfile-IpsecOptions-Enabled": ipGlobalProfile_IpsecOptions_Enabled,
       "ipGlobalProfile-IpsecOptions-SecurityPolicyDatabase": ipGlobalProfile_IpsecOptions_SecurityPolicyDatabase,
       "ipGlobalProfile-DnsCacheEnable": ipGlobalProfile_DnsCacheEnable,
       "ipGlobalProfile-DnsAutoUpdateInterval": ipGlobalProfile_DnsAutoUpdateInterval,
       "ipGlobalProfile-MboneTimeout": ipGlobalProfile_MboneTimeout,
       "ipGlobalProfile-RipOptions-MaxMultipathOrBackupRoutes": ipGlobalProfile_RipOptions_MaxMultipathOrBackupRoutes,
       "mibipGlobalProfile-DnsLocalTable-TableConfigTable": mibipGlobalProfile_DnsLocalTable_TableConfigTable,
       "mibipGlobalProfile-DnsLocalTable-TableConfigEntry": mibipGlobalProfile_DnsLocalTable_TableConfigEntry,
       "ipGlobalProfile-DnsLocalTable-TableConfig-Index-o": ipGlobalProfile_DnsLocalTable_TableConfig_Index_o,
       "ipGlobalProfile-DnsLocalTable-TableConfig-Index1-o": ipGlobalProfile_DnsLocalTable_TableConfig_Index1_o,
       "ipGlobalProfile-DnsLocalTable-TableConfig-HostName": ipGlobalProfile_DnsLocalTable_TableConfig_HostName,
       "ipGlobalProfile-DnsLocalTable-TableConfig-IpAddress": ipGlobalProfile_DnsLocalTable_TableConfig_IpAddress,
       "mibipGlobalProfile-SntpInfo-HostTable": mibipGlobalProfile_SntpInfo_HostTable,
       "mibipGlobalProfile-SntpInfo-HostEntry": mibipGlobalProfile_SntpInfo_HostEntry,
       "ipGlobalProfile-SntpInfo-Host-Index-o": ipGlobalProfile_SntpInfo_Host_Index_o,
       "ipGlobalProfile-SntpInfo-Host-Index1-o": ipGlobalProfile_SntpInfo_Host_Index1_o,
       "ipGlobalProfile-SntpInfo-Host": ipGlobalProfile_SntpInfo_Host,
       "mibipGlobalProfile-BootpRelay-BootpServersTable": mibipGlobalProfile_BootpRelay_BootpServersTable,
       "mibipGlobalProfile-BootpRelay-BootpServersEntry": mibipGlobalProfile_BootpRelay_BootpServersEntry,
       "ipGlobalProfile-BootpRelay-BootpServers-Index-o": ipGlobalProfile_BootpRelay_BootpServers_Index_o,
       "ipGlobalProfile-BootpRelay-BootpServers-Index1-o": ipGlobalProfile_BootpRelay_BootpServers_Index1_o,
       "ipGlobalProfile-BootpRelay-BootpServers": ipGlobalProfile_BootpRelay_BootpServers,
       "mibipGlobalProfile-PoolNameTable": mibipGlobalProfile_PoolNameTable,
       "mibipGlobalProfile-PoolNameEntry": mibipGlobalProfile_PoolNameEntry,
       "ipGlobalProfile-PoolName-Index-o": ipGlobalProfile_PoolName_Index_o,
       "ipGlobalProfile-PoolName-Index1-o": ipGlobalProfile_PoolName_Index1_o,
       "ipGlobalProfile-PoolName": ipGlobalProfile_PoolName,
       "mibipGlobalProfile-AssignCountTable": mibipGlobalProfile_AssignCountTable,
       "mibipGlobalProfile-AssignCountEntry": mibipGlobalProfile_AssignCountEntry,
       "ipGlobalProfile-AssignCount-Index-o": ipGlobalProfile_AssignCount_Index_o,
       "ipGlobalProfile-AssignCount-Index1-o": ipGlobalProfile_AssignCount_Index1_o,
       "ipGlobalProfile-AssignCount": ipGlobalProfile_AssignCount,
       "mibipGlobalProfile-PoolBaseAddressTable": mibipGlobalProfile_PoolBaseAddressTable,
       "mibipGlobalProfile-PoolBaseAddressEntry": mibipGlobalProfile_PoolBaseAddressEntry,
       "ipGlobalProfile-PoolBaseAddress-Index-o": ipGlobalProfile_PoolBaseAddress_Index_o,
       "ipGlobalProfile-PoolBaseAddress-Index1-o": ipGlobalProfile_PoolBaseAddress_Index1_o,
       "ipGlobalProfile-PoolBaseAddress": ipGlobalProfile_PoolBaseAddress,
       "mibipGlobalProfile-DhcpServer-StaticAddressTable": mibipGlobalProfile_DhcpServer_StaticAddressTable,
       "mibipGlobalProfile-DhcpServer-StaticAddressEntry": mibipGlobalProfile_DhcpServer_StaticAddressEntry,
       "ipGlobalProfile-DhcpServer-StaticAddress-Index-o": ipGlobalProfile_DhcpServer_StaticAddress_Index_o,
       "ipGlobalProfile-DhcpServer-StaticAddress-Index1-o": ipGlobalProfile_DhcpServer_StaticAddress_Index1_o,
       "ipGlobalProfile-DhcpServer-StaticAddress-IpAddress": ipGlobalProfile_DhcpServer_StaticAddress_IpAddress,
       "ipGlobalProfile-DhcpServer-StaticAddress-EthernetAddress": ipGlobalProfile_DhcpServer_StaticAddress_EthernetAddress,
       "mibipGlobalProfile-MboneBackupTable": mibipGlobalProfile_MboneBackupTable,
       "mibipGlobalProfile-MboneBackupEntry": mibipGlobalProfile_MboneBackupEntry,
       "ipGlobalProfile-MboneBackup-Index-o": ipGlobalProfile_MboneBackup_Index_o,
       "ipGlobalProfile-MboneBackup-Index1-o": ipGlobalProfile_MboneBackup_Index1_o,
       "ipGlobalProfile-MboneBackup-Enabled": ipGlobalProfile_MboneBackup_Enabled,
       "ipGlobalProfile-MboneBackup-MboneProfile": ipGlobalProfile_MboneBackup_MboneProfile,
       "ipGlobalProfile-MboneBackup-MboneLanInterface-PhysicalAddress-Shelf": ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Shelf,
       "ipGlobalProfile-MboneBackup-MboneLanInterface-PhysicalAddress-Slot": ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_Slot,
       "ipGlobalProfile-MboneBackup-MboneLanInterface-PhysicalAddress-ItemNumber": ipGlobalProfile_MboneBackup_MboneLanInterface_PhysicalAddress_ItemNumber,
       "ipGlobalProfile-MboneBackup-MboneLanInterface-LogicalItem": ipGlobalProfile_MboneBackup_MboneLanInterface_LogicalItem,
       "ipGlobalProfile-MboneBackup-MboneTimeout": ipGlobalProfile_MboneBackup_MboneTimeout}
)
