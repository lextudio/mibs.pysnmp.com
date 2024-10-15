# SNMP MIB module (ASCEND-MIBIPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBIPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:47 2024
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

_MibipxInterfaceProfile_ObjectIdentity = ObjectIdentity
mibipxInterfaceProfile = _MibipxInterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 86)
)
_MibipxInterfaceProfileTable_Object = MibTable
mibipxInterfaceProfileTable = _MibipxInterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1)
)
if mibBuilder.loadTexts:
    mibipxInterfaceProfileTable.setStatus("mandatory")
_MibipxInterfaceProfileEntry_Object = MibTableRow
mibipxInterfaceProfileEntry = _MibipxInterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1)
)
mibipxInterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-Item-o"),
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibipxInterfaceProfileEntry.setStatus("mandatory")
_IpxInterfaceProfile_Shelf_o_Type = Integer32
_IpxInterfaceProfile_Shelf_o_Object = MibScalar
ipxInterfaceProfile_Shelf_o = _IpxInterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 1),
    _IpxInterfaceProfile_Shelf_o_Type()
)
ipxInterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_Shelf_o.setStatus("mandatory")
_IpxInterfaceProfile_Slot_o_Type = Integer32
_IpxInterfaceProfile_Slot_o_Object = MibScalar
ipxInterfaceProfile_Slot_o = _IpxInterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 2),
    _IpxInterfaceProfile_Slot_o_Type()
)
ipxInterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_Slot_o.setStatus("mandatory")
_IpxInterfaceProfile_Item_o_Type = Integer32
_IpxInterfaceProfile_Item_o_Object = MibScalar
ipxInterfaceProfile_Item_o = _IpxInterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 3),
    _IpxInterfaceProfile_Item_o_Type()
)
ipxInterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_Item_o.setStatus("mandatory")
_IpxInterfaceProfile_LogicalItem_o_Type = Integer32
_IpxInterfaceProfile_LogicalItem_o_Object = MibScalar
ipxInterfaceProfile_LogicalItem_o = _IpxInterfaceProfile_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 4),
    _IpxInterfaceProfile_LogicalItem_o_Type()
)
ipxInterfaceProfile_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_LogicalItem_o.setStatus("mandatory")


class _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf based on Integer32"""
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


_IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object = MibScalar
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf = _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 5),
    _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type()
)
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus("mandatory")


class _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot based on Integer32"""
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


_IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object = MibScalar
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot = _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 6),
    _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type()
)
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus("mandatory")
_IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type = Integer32
_IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object = MibScalar
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber = _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 7),
    _IpxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type()
)
ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_IpxInterfaceProfile_InterfaceAddress_LogicalItem_Type = Integer32
_IpxInterfaceProfile_InterfaceAddress_LogicalItem_Object = MibScalar
ipxInterfaceProfile_InterfaceAddress_LogicalItem = _IpxInterfaceProfile_InterfaceAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 8),
    _IpxInterfaceProfile_InterfaceAddress_LogicalItem_Type()
)
ipxInterfaceProfile_InterfaceAddress_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_InterfaceAddress_LogicalItem.setStatus("mandatory")


class _IpxInterfaceProfile_IpxRoutingEnabled_Type(Integer32):
    """Custom type ipxInterfaceProfile_IpxRoutingEnabled based on Integer32"""
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


_IpxInterfaceProfile_IpxRoutingEnabled_Type.__name__ = "Integer32"
_IpxInterfaceProfile_IpxRoutingEnabled_Object = MibScalar
ipxInterfaceProfile_IpxRoutingEnabled = _IpxInterfaceProfile_IpxRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 9),
    _IpxInterfaceProfile_IpxRoutingEnabled_Type()
)
ipxInterfaceProfile_IpxRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxRoutingEnabled.setStatus("mandatory")


class _IpxInterfaceProfile_IpxFrame_Type(Integer32):
    """Custom type ipxInterfaceProfile_IpxFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("enetII", 5),
          ("n-8022", 3),
          ("n-8023", 2),
          ("none", 1),
          ("sNAP", 4))
    )


_IpxInterfaceProfile_IpxFrame_Type.__name__ = "Integer32"
_IpxInterfaceProfile_IpxFrame_Object = MibScalar
ipxInterfaceProfile_IpxFrame = _IpxInterfaceProfile_IpxFrame_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 10),
    _IpxInterfaceProfile_IpxFrame_Type()
)
ipxInterfaceProfile_IpxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxFrame.setStatus("mandatory")
_IpxInterfaceProfile_IpxNetNumber_Type = DisplayString
_IpxInterfaceProfile_IpxNetNumber_Object = MibScalar
ipxInterfaceProfile_IpxNetNumber = _IpxInterfaceProfile_IpxNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 11),
    _IpxInterfaceProfile_IpxNetNumber_Type()
)
ipxInterfaceProfile_IpxNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxNetNumber.setStatus("mandatory")


class _IpxInterfaceProfile_IpxType20_Type(Integer32):
    """Custom type ipxInterfaceProfile_IpxType20 based on Integer32"""
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


_IpxInterfaceProfile_IpxType20_Type.__name__ = "Integer32"
_IpxInterfaceProfile_IpxType20_Object = MibScalar
ipxInterfaceProfile_IpxType20 = _IpxInterfaceProfile_IpxType20_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 12),
    _IpxInterfaceProfile_IpxType20_Type()
)
ipxInterfaceProfile_IpxType20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxType20.setStatus("mandatory")
_IpxInterfaceProfile_IpxSapFilterName_Type = DisplayString
_IpxInterfaceProfile_IpxSapFilterName_Object = MibScalar
ipxInterfaceProfile_IpxSapFilterName = _IpxInterfaceProfile_IpxSapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 13),
    _IpxInterfaceProfile_IpxSapFilterName_Type()
)
ipxInterfaceProfile_IpxSapFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapFilterName.setStatus("mandatory")
_IpxInterfaceProfile_oIPXSAPFilter_Type = Integer32
_IpxInterfaceProfile_oIPXSAPFilter_Object = MibScalar
ipxInterfaceProfile_oIPXSAPFilter = _IpxInterfaceProfile_oIPXSAPFilter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 14),
    _IpxInterfaceProfile_oIPXSAPFilter_Type()
)
ipxInterfaceProfile_oIPXSAPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_oIPXSAPFilter.setStatus("mandatory")


class _IpxInterfaceProfile_IpxSapProxy_Type(Integer32):
    """Custom type ipxInterfaceProfile_IpxSapProxy based on Integer32"""
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


_IpxInterfaceProfile_IpxSapProxy_Type.__name__ = "Integer32"
_IpxInterfaceProfile_IpxSapProxy_Object = MibScalar
ipxInterfaceProfile_IpxSapProxy = _IpxInterfaceProfile_IpxSapProxy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 15),
    _IpxInterfaceProfile_IpxSapProxy_Type()
)
ipxInterfaceProfile_IpxSapProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapProxy.setStatus("mandatory")
_IpxInterfaceProfile_Vrouter_Type = DisplayString
_IpxInterfaceProfile_Vrouter_Object = MibScalar
ipxInterfaceProfile_Vrouter = _IpxInterfaceProfile_Vrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 16),
    _IpxInterfaceProfile_Vrouter_Type()
)
ipxInterfaceProfile_Vrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_Vrouter.setStatus("mandatory")


class _IpxInterfaceProfile_Action_o_Type(Integer32):
    """Custom type ipxInterfaceProfile_Action_o based on Integer32"""
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


_IpxInterfaceProfile_Action_o_Type.__name__ = "Integer32"
_IpxInterfaceProfile_Action_o_Object = MibScalar
ipxInterfaceProfile_Action_o = _IpxInterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 1, 1, 17),
    _IpxInterfaceProfile_Action_o_Type()
)
ipxInterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_Action_o.setStatus("mandatory")
_MibipxInterfaceProfile_IpxSapProxyNetTable_Object = MibTable
mibipxInterfaceProfile_IpxSapProxyNetTable = _MibipxInterfaceProfile_IpxSapProxyNetTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2)
)
if mibBuilder.loadTexts:
    mibipxInterfaceProfile_IpxSapProxyNetTable.setStatus("mandatory")
_MibipxInterfaceProfile_IpxSapProxyNetEntry_Object = MibTableRow
mibipxInterfaceProfile_IpxSapProxyNetEntry = _MibipxInterfaceProfile_IpxSapProxyNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1)
)
mibipxInterfaceProfile_IpxSapProxyNetEntry.setIndexNames(
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Shelf-o"),
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Slot-o"),
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Item-o"),
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-LogicalItem-o"),
    (0, "ASCEND-MIBIPX-MIB", "ipxInterfaceProfile-IpxSapProxyNet-Index-o"),
)
if mibBuilder.loadTexts:
    mibipxInterfaceProfile_IpxSapProxyNetEntry.setStatus("mandatory")
_IpxInterfaceProfile_IpxSapProxyNet_Shelf_o_Type = Integer32
_IpxInterfaceProfile_IpxSapProxyNet_Shelf_o_Object = MibScalar
ipxInterfaceProfile_IpxSapProxyNet_Shelf_o = _IpxInterfaceProfile_IpxSapProxyNet_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 1),
    _IpxInterfaceProfile_IpxSapProxyNet_Shelf_o_Type()
)
ipxInterfaceProfile_IpxSapProxyNet_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapProxyNet_Shelf_o.setStatus("mandatory")
_IpxInterfaceProfile_IpxSapProxyNet_Slot_o_Type = Integer32
_IpxInterfaceProfile_IpxSapProxyNet_Slot_o_Object = MibScalar
ipxInterfaceProfile_IpxSapProxyNet_Slot_o = _IpxInterfaceProfile_IpxSapProxyNet_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 2),
    _IpxInterfaceProfile_IpxSapProxyNet_Slot_o_Type()
)
ipxInterfaceProfile_IpxSapProxyNet_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapProxyNet_Slot_o.setStatus("mandatory")
_IpxInterfaceProfile_IpxSapProxyNet_Item_o_Type = Integer32
_IpxInterfaceProfile_IpxSapProxyNet_Item_o_Object = MibScalar
ipxInterfaceProfile_IpxSapProxyNet_Item_o = _IpxInterfaceProfile_IpxSapProxyNet_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 3),
    _IpxInterfaceProfile_IpxSapProxyNet_Item_o_Type()
)
ipxInterfaceProfile_IpxSapProxyNet_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapProxyNet_Item_o.setStatus("mandatory")
_IpxInterfaceProfile_IpxSapProxyNet_LogicalItem_o_Type = Integer32
_IpxInterfaceProfile_IpxSapProxyNet_LogicalItem_o_Object = MibScalar
ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o = _IpxInterfaceProfile_IpxSapProxyNet_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 4),
    _IpxInterfaceProfile_IpxSapProxyNet_LogicalItem_o_Type()
)
ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o.setStatus("mandatory")
_IpxInterfaceProfile_IpxSapProxyNet_Index_o_Type = Integer32
_IpxInterfaceProfile_IpxSapProxyNet_Index_o_Object = MibScalar
ipxInterfaceProfile_IpxSapProxyNet_Index_o = _IpxInterfaceProfile_IpxSapProxyNet_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 5),
    _IpxInterfaceProfile_IpxSapProxyNet_Index_o_Type()
)
ipxInterfaceProfile_IpxSapProxyNet_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapProxyNet_Index_o.setStatus("mandatory")
_IpxInterfaceProfile_IpxSapProxyNet_Type = Integer32
_IpxInterfaceProfile_IpxSapProxyNet_Object = MibScalar
ipxInterfaceProfile_IpxSapProxyNet = _IpxInterfaceProfile_IpxSapProxyNet_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 86, 2, 1, 6),
    _IpxInterfaceProfile_IpxSapProxyNet_Type()
)
ipxInterfaceProfile_IpxSapProxyNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInterfaceProfile_IpxSapProxyNet.setStatus("mandatory")
_MibipxGlobalProfile_ObjectIdentity = ObjectIdentity
mibipxGlobalProfile = _MibipxGlobalProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 87)
)
_MibipxGlobalProfileTable_Object = MibTable
mibipxGlobalProfileTable = _MibipxGlobalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1)
)
if mibBuilder.loadTexts:
    mibipxGlobalProfileTable.setStatus("mandatory")
_MibipxGlobalProfileEntry_Object = MibTableRow
mibipxGlobalProfileEntry = _MibipxGlobalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1)
)
mibipxGlobalProfileEntry.setIndexNames(
    (0, "ASCEND-MIBIPX-MIB", "ipxGlobalProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibipxGlobalProfileEntry.setStatus("mandatory")
_IpxGlobalProfile_Index_o_Type = Integer32
_IpxGlobalProfile_Index_o_Object = MibScalar
ipxGlobalProfile_Index_o = _IpxGlobalProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 1),
    _IpxGlobalProfile_Index_o_Type()
)
ipxGlobalProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxGlobalProfile_Index_o.setStatus("mandatory")


class _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf based on Integer32"""
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


_IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf_Object = MibScalar
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf = _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 2),
    _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf_Type()
)
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus("mandatory")


class _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot_Type(Integer32):
    """Custom type ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot based on Integer32"""
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


_IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot_Object = MibScalar
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot = _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 3),
    _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot_Type()
)
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus("mandatory")
_IpxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type = Integer32
_IpxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object = MibScalar
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber = _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 4),
    _IpxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type()
)
ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_IpxGlobalProfile_InterfaceAddress_LogicalItem_Type = Integer32
_IpxGlobalProfile_InterfaceAddress_LogicalItem_Object = MibScalar
ipxGlobalProfile_InterfaceAddress_LogicalItem = _IpxGlobalProfile_InterfaceAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 5),
    _IpxGlobalProfile_InterfaceAddress_LogicalItem_Type()
)
ipxGlobalProfile_InterfaceAddress_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_InterfaceAddress_LogicalItem.setStatus("mandatory")


class _IpxGlobalProfile_IpxRoutingEnabled_Type(Integer32):
    """Custom type ipxGlobalProfile_IpxRoutingEnabled based on Integer32"""
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


_IpxGlobalProfile_IpxRoutingEnabled_Type.__name__ = "Integer32"
_IpxGlobalProfile_IpxRoutingEnabled_Object = MibScalar
ipxGlobalProfile_IpxRoutingEnabled = _IpxGlobalProfile_IpxRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 6),
    _IpxGlobalProfile_IpxRoutingEnabled_Type()
)
ipxGlobalProfile_IpxRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_IpxRoutingEnabled.setStatus("mandatory")
_IpxGlobalProfile_IpxDialinPool_Type = DisplayString
_IpxGlobalProfile_IpxDialinPool_Object = MibScalar
ipxGlobalProfile_IpxDialinPool = _IpxGlobalProfile_IpxDialinPool_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 7),
    _IpxGlobalProfile_IpxDialinPool_Type()
)
ipxGlobalProfile_IpxDialinPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_IpxDialinPool.setStatus("mandatory")
_IpxGlobalProfile_GlobalVrouter_Type = DisplayString
_IpxGlobalProfile_GlobalVrouter_Object = MibScalar
ipxGlobalProfile_GlobalVrouter = _IpxGlobalProfile_GlobalVrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 8),
    _IpxGlobalProfile_GlobalVrouter_Type()
)
ipxGlobalProfile_GlobalVrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_GlobalVrouter.setStatus("mandatory")


class _IpxGlobalProfile_Action_o_Type(Integer32):
    """Custom type ipxGlobalProfile_Action_o based on Integer32"""
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


_IpxGlobalProfile_Action_o_Type.__name__ = "Integer32"
_IpxGlobalProfile_Action_o_Object = MibScalar
ipxGlobalProfile_Action_o = _IpxGlobalProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 87, 1, 1, 9),
    _IpxGlobalProfile_Action_o_Type()
)
ipxGlobalProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxGlobalProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBIPX-MIB",
    **{"DisplayString": DisplayString,
       "mibipxInterfaceProfile": mibipxInterfaceProfile,
       "mibipxInterfaceProfileTable": mibipxInterfaceProfileTable,
       "mibipxInterfaceProfileEntry": mibipxInterfaceProfileEntry,
       "ipxInterfaceProfile-Shelf-o": ipxInterfaceProfile_Shelf_o,
       "ipxInterfaceProfile-Slot-o": ipxInterfaceProfile_Slot_o,
       "ipxInterfaceProfile-Item-o": ipxInterfaceProfile_Item_o,
       "ipxInterfaceProfile-LogicalItem-o": ipxInterfaceProfile_LogicalItem_o,
       "ipxInterfaceProfile-InterfaceAddress-PhysicalAddress-Shelf": ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf,
       "ipxInterfaceProfile-InterfaceAddress-PhysicalAddress-Slot": ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot,
       "ipxInterfaceProfile-InterfaceAddress-PhysicalAddress-ItemNumber": ipxInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber,
       "ipxInterfaceProfile-InterfaceAddress-LogicalItem": ipxInterfaceProfile_InterfaceAddress_LogicalItem,
       "ipxInterfaceProfile-IpxRoutingEnabled": ipxInterfaceProfile_IpxRoutingEnabled,
       "ipxInterfaceProfile-IpxFrame": ipxInterfaceProfile_IpxFrame,
       "ipxInterfaceProfile-IpxNetNumber": ipxInterfaceProfile_IpxNetNumber,
       "ipxInterfaceProfile-IpxType20": ipxInterfaceProfile_IpxType20,
       "ipxInterfaceProfile-IpxSapFilterName": ipxInterfaceProfile_IpxSapFilterName,
       "ipxInterfaceProfile-oIPXSAPFilter": ipxInterfaceProfile_oIPXSAPFilter,
       "ipxInterfaceProfile-IpxSapProxy": ipxInterfaceProfile_IpxSapProxy,
       "ipxInterfaceProfile-Vrouter": ipxInterfaceProfile_Vrouter,
       "ipxInterfaceProfile-Action-o": ipxInterfaceProfile_Action_o,
       "mibipxInterfaceProfile-IpxSapProxyNetTable": mibipxInterfaceProfile_IpxSapProxyNetTable,
       "mibipxInterfaceProfile-IpxSapProxyNetEntry": mibipxInterfaceProfile_IpxSapProxyNetEntry,
       "ipxInterfaceProfile-IpxSapProxyNet-Shelf-o": ipxInterfaceProfile_IpxSapProxyNet_Shelf_o,
       "ipxInterfaceProfile-IpxSapProxyNet-Slot-o": ipxInterfaceProfile_IpxSapProxyNet_Slot_o,
       "ipxInterfaceProfile-IpxSapProxyNet-Item-o": ipxInterfaceProfile_IpxSapProxyNet_Item_o,
       "ipxInterfaceProfile-IpxSapProxyNet-LogicalItem-o": ipxInterfaceProfile_IpxSapProxyNet_LogicalItem_o,
       "ipxInterfaceProfile-IpxSapProxyNet-Index-o": ipxInterfaceProfile_IpxSapProxyNet_Index_o,
       "ipxInterfaceProfile-IpxSapProxyNet": ipxInterfaceProfile_IpxSapProxyNet,
       "mibipxGlobalProfile": mibipxGlobalProfile,
       "mibipxGlobalProfileTable": mibipxGlobalProfileTable,
       "mibipxGlobalProfileEntry": mibipxGlobalProfileEntry,
       "ipxGlobalProfile-Index-o": ipxGlobalProfile_Index_o,
       "ipxGlobalProfile-InterfaceAddress-PhysicalAddress-Shelf": ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Shelf,
       "ipxGlobalProfile-InterfaceAddress-PhysicalAddress-Slot": ipxGlobalProfile_InterfaceAddress_PhysicalAddress_Slot,
       "ipxGlobalProfile-InterfaceAddress-PhysicalAddress-ItemNumber": ipxGlobalProfile_InterfaceAddress_PhysicalAddress_ItemNumber,
       "ipxGlobalProfile-InterfaceAddress-LogicalItem": ipxGlobalProfile_InterfaceAddress_LogicalItem,
       "ipxGlobalProfile-IpxRoutingEnabled": ipxGlobalProfile_IpxRoutingEnabled,
       "ipxGlobalProfile-IpxDialinPool": ipxGlobalProfile_IpxDialinPool,
       "ipxGlobalProfile-GlobalVrouter": ipxGlobalProfile_GlobalVrouter,
       "ipxGlobalProfile-Action-o": ipxGlobalProfile_Action_o}
)
