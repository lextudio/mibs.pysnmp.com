# SNMP MIB module (ASCEND-MIBETHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBETHER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:34 2024
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

_MibethernetInterfaceProfile_ObjectIdentity = ObjectIdentity
mibethernetInterfaceProfile = _MibethernetInterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 76)
)
_MibethernetInterfaceProfileTable_Object = MibTable
mibethernetInterfaceProfileTable = _MibethernetInterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1)
)
if mibBuilder.loadTexts:
    mibethernetInterfaceProfileTable.setStatus("mandatory")
_MibethernetInterfaceProfileEntry_Object = MibTableRow
mibethernetInterfaceProfileEntry = _MibethernetInterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1)
)
mibethernetInterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBETHER-MIB", "ethernetInterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBETHER-MIB", "ethernetInterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBETHER-MIB", "ethernetInterfaceProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibethernetInterfaceProfileEntry.setStatus("mandatory")
_EthernetInterfaceProfile_Shelf_o_Type = Integer32
_EthernetInterfaceProfile_Shelf_o_Object = MibScalar
ethernetInterfaceProfile_Shelf_o = _EthernetInterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 1),
    _EthernetInterfaceProfile_Shelf_o_Type()
)
ethernetInterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_Shelf_o.setStatus("mandatory")
_EthernetInterfaceProfile_Slot_o_Type = Integer32
_EthernetInterfaceProfile_Slot_o_Object = MibScalar
ethernetInterfaceProfile_Slot_o = _EthernetInterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 2),
    _EthernetInterfaceProfile_Slot_o_Type()
)
ethernetInterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_Slot_o.setStatus("mandatory")
_EthernetInterfaceProfile_Item_o_Type = Integer32
_EthernetInterfaceProfile_Item_o_Object = MibScalar
ethernetInterfaceProfile_Item_o = _EthernetInterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 3),
    _EthernetInterfaceProfile_Item_o_Type()
)
ethernetInterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_Item_o.setStatus("mandatory")


class _EthernetInterfaceProfile_InterfaceAddress_Shelf_Type(Integer32):
    """Custom type ethernetInterfaceProfile_InterfaceAddress_Shelf based on Integer32"""
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


_EthernetInterfaceProfile_InterfaceAddress_Shelf_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_InterfaceAddress_Shelf_Object = MibScalar
ethernetInterfaceProfile_InterfaceAddress_Shelf = _EthernetInterfaceProfile_InterfaceAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 4),
    _EthernetInterfaceProfile_InterfaceAddress_Shelf_Type()
)
ethernetInterfaceProfile_InterfaceAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_InterfaceAddress_Shelf.setStatus("mandatory")


class _EthernetInterfaceProfile_InterfaceAddress_Slot_Type(Integer32):
    """Custom type ethernetInterfaceProfile_InterfaceAddress_Slot based on Integer32"""
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


_EthernetInterfaceProfile_InterfaceAddress_Slot_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_InterfaceAddress_Slot_Object = MibScalar
ethernetInterfaceProfile_InterfaceAddress_Slot = _EthernetInterfaceProfile_InterfaceAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 5),
    _EthernetInterfaceProfile_InterfaceAddress_Slot_Type()
)
ethernetInterfaceProfile_InterfaceAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_InterfaceAddress_Slot.setStatus("mandatory")
_EthernetInterfaceProfile_InterfaceAddress_ItemNumber_Type = Integer32
_EthernetInterfaceProfile_InterfaceAddress_ItemNumber_Object = MibScalar
ethernetInterfaceProfile_InterfaceAddress_ItemNumber = _EthernetInterfaceProfile_InterfaceAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 6),
    _EthernetInterfaceProfile_InterfaceAddress_ItemNumber_Type()
)
ethernetInterfaceProfile_InterfaceAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_InterfaceAddress_ItemNumber.setStatus("mandatory")


class _EthernetInterfaceProfile_LinkStateEnabled_Type(Integer32):
    """Custom type ethernetInterfaceProfile_LinkStateEnabled based on Integer32"""
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


_EthernetInterfaceProfile_LinkStateEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_LinkStateEnabled_Object = MibScalar
ethernetInterfaceProfile_LinkStateEnabled = _EthernetInterfaceProfile_LinkStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 7),
    _EthernetInterfaceProfile_LinkStateEnabled_Type()
)
ethernetInterfaceProfile_LinkStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_LinkStateEnabled.setStatus("mandatory")


class _EthernetInterfaceProfile_Enabled_Type(Integer32):
    """Custom type ethernetInterfaceProfile_Enabled based on Integer32"""
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


_EthernetInterfaceProfile_Enabled_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_Enabled_Object = MibScalar
ethernetInterfaceProfile_Enabled = _EthernetInterfaceProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 8),
    _EthernetInterfaceProfile_Enabled_Type()
)
ethernetInterfaceProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_Enabled.setStatus("mandatory")


class _EthernetInterfaceProfile_EtherIfType_Type(Integer32):
    """Custom type ethernetInterfaceProfile_EtherIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aui", 1),
          ("coax", 2),
          ("utp", 3))
    )


_EthernetInterfaceProfile_EtherIfType_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_EtherIfType_Object = MibScalar
ethernetInterfaceProfile_EtherIfType = _EthernetInterfaceProfile_EtherIfType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 9),
    _EthernetInterfaceProfile_EtherIfType_Type()
)
ethernetInterfaceProfile_EtherIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_EtherIfType.setStatus("mandatory")
_EthernetInterfaceProfile_Filter_Type = Integer32
_EthernetInterfaceProfile_Filter_Object = MibScalar
ethernetInterfaceProfile_Filter = _EthernetInterfaceProfile_Filter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 10),
    _EthernetInterfaceProfile_Filter_Type()
)
ethernetInterfaceProfile_Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_Filter.setStatus("mandatory")


class _EthernetInterfaceProfile_BridgingEnabled_Type(Integer32):
    """Custom type ethernetInterfaceProfile_BridgingEnabled based on Integer32"""
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


_EthernetInterfaceProfile_BridgingEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_BridgingEnabled_Object = MibScalar
ethernetInterfaceProfile_BridgingEnabled = _EthernetInterfaceProfile_BridgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 11),
    _EthernetInterfaceProfile_BridgingEnabled_Type()
)
ethernetInterfaceProfile_BridgingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingEnabled.setStatus("mandatory")
_EthernetInterfaceProfile_FilterName_Type = DisplayString
_EthernetInterfaceProfile_FilterName_Object = MibScalar
ethernetInterfaceProfile_FilterName = _EthernetInterfaceProfile_FilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 12),
    _EthernetInterfaceProfile_FilterName_Type()
)
ethernetInterfaceProfile_FilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_FilterName.setStatus("mandatory")


class _EthernetInterfaceProfile_DuplexMode_Type(Integer32):
    """Custom type ethernetInterfaceProfile_DuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_EthernetInterfaceProfile_DuplexMode_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_DuplexMode_Object = MibScalar
ethernetInterfaceProfile_DuplexMode = _EthernetInterfaceProfile_DuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 13),
    _EthernetInterfaceProfile_DuplexMode_Type()
)
ethernetInterfaceProfile_DuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_DuplexMode.setStatus("mandatory")


class _EthernetInterfaceProfile_PppoeOptions_Pppoe_Type(Integer32):
    """Custom type ethernetInterfaceProfile_PppoeOptions_Pppoe based on Integer32"""
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


_EthernetInterfaceProfile_PppoeOptions_Pppoe_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_PppoeOptions_Pppoe_Object = MibScalar
ethernetInterfaceProfile_PppoeOptions_Pppoe = _EthernetInterfaceProfile_PppoeOptions_Pppoe_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 14),
    _EthernetInterfaceProfile_PppoeOptions_Pppoe_Type()
)
ethernetInterfaceProfile_PppoeOptions_Pppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_PppoeOptions_Pppoe.setStatus("mandatory")


class _EthernetInterfaceProfile_PppoeOptions_BridgeNonPppoe_Type(Integer32):
    """Custom type ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe based on Integer32"""
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


_EthernetInterfaceProfile_PppoeOptions_BridgeNonPppoe_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_PppoeOptions_BridgeNonPppoe_Object = MibScalar
ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe = _EthernetInterfaceProfile_PppoeOptions_BridgeNonPppoe_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 15),
    _EthernetInterfaceProfile_PppoeOptions_BridgeNonPppoe_Type()
)
ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe.setStatus("mandatory")
_EthernetInterfaceProfile_BridgingOptions_BridgingGroup_Type = Integer32
_EthernetInterfaceProfile_BridgingOptions_BridgingGroup_Object = MibScalar
ethernetInterfaceProfile_BridgingOptions_BridgingGroup = _EthernetInterfaceProfile_BridgingOptions_BridgingGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 16),
    _EthernetInterfaceProfile_BridgingOptions_BridgingGroup_Type()
)
ethernetInterfaceProfile_BridgingOptions_BridgingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingOptions_BridgingGroup.setStatus("mandatory")


class _EthernetInterfaceProfile_BridgingOptions_DialOnBroadcast_Type(Integer32):
    """Custom type ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast based on Integer32"""
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


_EthernetInterfaceProfile_BridgingOptions_DialOnBroadcast_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_BridgingOptions_DialOnBroadcast_Object = MibScalar
ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast = _EthernetInterfaceProfile_BridgingOptions_DialOnBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 17),
    _EthernetInterfaceProfile_BridgingOptions_DialOnBroadcast_Type()
)
ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast.setStatus("mandatory")


class _EthernetInterfaceProfile_BridgingOptions_IpxSpoofing_Type(Integer32):
    """Custom type ethernetInterfaceProfile_BridgingOptions_IpxSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientSpoofing", 2),
          ("none", 1),
          ("serverSpoofing", 3))
    )


_EthernetInterfaceProfile_BridgingOptions_IpxSpoofing_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_BridgingOptions_IpxSpoofing_Object = MibScalar
ethernetInterfaceProfile_BridgingOptions_IpxSpoofing = _EthernetInterfaceProfile_BridgingOptions_IpxSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 18),
    _EthernetInterfaceProfile_BridgingOptions_IpxSpoofing_Type()
)
ethernetInterfaceProfile_BridgingOptions_IpxSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingOptions_IpxSpoofing.setStatus("mandatory")
_EthernetInterfaceProfile_BridgingOptions_SpoofingTimeout_Type = Integer32
_EthernetInterfaceProfile_BridgingOptions_SpoofingTimeout_Object = MibScalar
ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout = _EthernetInterfaceProfile_BridgingOptions_SpoofingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 19),
    _EthernetInterfaceProfile_BridgingOptions_SpoofingTimeout_Type()
)
ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout.setStatus("mandatory")
_EthernetInterfaceProfile_BridgingOptions_Fill2_Type = Integer32
_EthernetInterfaceProfile_BridgingOptions_Fill2_Object = MibScalar
ethernetInterfaceProfile_BridgingOptions_Fill2 = _EthernetInterfaceProfile_BridgingOptions_Fill2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 20),
    _EthernetInterfaceProfile_BridgingOptions_Fill2_Type()
)
ethernetInterfaceProfile_BridgingOptions_Fill2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingOptions_Fill2.setStatus("mandatory")


class _EthernetInterfaceProfile_BridgingOptions_BridgeType_Type(Integer32):
    """Custom type ethernetInterfaceProfile_BridgingOptions_BridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipxClientBridging", 2),
          ("noBridging", 3),
          ("transparentBridging", 1))
    )


_EthernetInterfaceProfile_BridgingOptions_BridgeType_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_BridgingOptions_BridgeType_Object = MibScalar
ethernetInterfaceProfile_BridgingOptions_BridgeType = _EthernetInterfaceProfile_BridgingOptions_BridgeType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 21),
    _EthernetInterfaceProfile_BridgingOptions_BridgeType_Type()
)
ethernetInterfaceProfile_BridgingOptions_BridgeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingOptions_BridgeType.setStatus("mandatory")


class _EthernetInterfaceProfile_BridgingOptions_Egress_Type(Integer32):
    """Custom type ethernetInterfaceProfile_BridgingOptions_Egress based on Integer32"""
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


_EthernetInterfaceProfile_BridgingOptions_Egress_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_BridgingOptions_Egress_Object = MibScalar
ethernetInterfaceProfile_BridgingOptions_Egress = _EthernetInterfaceProfile_BridgingOptions_Egress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 22),
    _EthernetInterfaceProfile_BridgingOptions_Egress_Type()
)
ethernetInterfaceProfile_BridgingOptions_Egress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_BridgingOptions_Egress.setStatus("mandatory")


class _EthernetInterfaceProfile_MediaSpeedMbit_Type(Integer32):
    """Custom type ethernetInterfaceProfile_MediaSpeedMbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-100mb", 2),
          ("n-10mb", 1))
    )


_EthernetInterfaceProfile_MediaSpeedMbit_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_MediaSpeedMbit_Object = MibScalar
ethernetInterfaceProfile_MediaSpeedMbit = _EthernetInterfaceProfile_MediaSpeedMbit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 23),
    _EthernetInterfaceProfile_MediaSpeedMbit_Type()
)
ethernetInterfaceProfile_MediaSpeedMbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_MediaSpeedMbit.setStatus("mandatory")


class _EthernetInterfaceProfile_AutoNegotiate_Type(Integer32):
    """Custom type ethernetInterfaceProfile_AutoNegotiate based on Integer32"""
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


_EthernetInterfaceProfile_AutoNegotiate_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_AutoNegotiate_Object = MibScalar
ethernetInterfaceProfile_AutoNegotiate = _EthernetInterfaceProfile_AutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 24),
    _EthernetInterfaceProfile_AutoNegotiate_Type()
)
ethernetInterfaceProfile_AutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_AutoNegotiate.setStatus("mandatory")


class _EthernetInterfaceProfile_Action_o_Type(Integer32):
    """Custom type ethernetInterfaceProfile_Action_o based on Integer32"""
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


_EthernetInterfaceProfile_Action_o_Type.__name__ = "Integer32"
_EthernetInterfaceProfile_Action_o_Object = MibScalar
ethernetInterfaceProfile_Action_o = _EthernetInterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 76, 1, 1, 25),
    _EthernetInterfaceProfile_Action_o_Type()
)
ethernetInterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBETHER-MIB",
    **{"DisplayString": DisplayString,
       "mibethernetInterfaceProfile": mibethernetInterfaceProfile,
       "mibethernetInterfaceProfileTable": mibethernetInterfaceProfileTable,
       "mibethernetInterfaceProfileEntry": mibethernetInterfaceProfileEntry,
       "ethernetInterfaceProfile-Shelf-o": ethernetInterfaceProfile_Shelf_o,
       "ethernetInterfaceProfile-Slot-o": ethernetInterfaceProfile_Slot_o,
       "ethernetInterfaceProfile-Item-o": ethernetInterfaceProfile_Item_o,
       "ethernetInterfaceProfile-InterfaceAddress-Shelf": ethernetInterfaceProfile_InterfaceAddress_Shelf,
       "ethernetInterfaceProfile-InterfaceAddress-Slot": ethernetInterfaceProfile_InterfaceAddress_Slot,
       "ethernetInterfaceProfile-InterfaceAddress-ItemNumber": ethernetInterfaceProfile_InterfaceAddress_ItemNumber,
       "ethernetInterfaceProfile-LinkStateEnabled": ethernetInterfaceProfile_LinkStateEnabled,
       "ethernetInterfaceProfile-Enabled": ethernetInterfaceProfile_Enabled,
       "ethernetInterfaceProfile-EtherIfType": ethernetInterfaceProfile_EtherIfType,
       "ethernetInterfaceProfile-Filter": ethernetInterfaceProfile_Filter,
       "ethernetInterfaceProfile-BridgingEnabled": ethernetInterfaceProfile_BridgingEnabled,
       "ethernetInterfaceProfile-FilterName": ethernetInterfaceProfile_FilterName,
       "ethernetInterfaceProfile-DuplexMode": ethernetInterfaceProfile_DuplexMode,
       "ethernetInterfaceProfile-PppoeOptions-Pppoe": ethernetInterfaceProfile_PppoeOptions_Pppoe,
       "ethernetInterfaceProfile-PppoeOptions-BridgeNonPppoe": ethernetInterfaceProfile_PppoeOptions_BridgeNonPppoe,
       "ethernetInterfaceProfile-BridgingOptions-BridgingGroup": ethernetInterfaceProfile_BridgingOptions_BridgingGroup,
       "ethernetInterfaceProfile-BridgingOptions-DialOnBroadcast": ethernetInterfaceProfile_BridgingOptions_DialOnBroadcast,
       "ethernetInterfaceProfile-BridgingOptions-IpxSpoofing": ethernetInterfaceProfile_BridgingOptions_IpxSpoofing,
       "ethernetInterfaceProfile-BridgingOptions-SpoofingTimeout": ethernetInterfaceProfile_BridgingOptions_SpoofingTimeout,
       "ethernetInterfaceProfile-BridgingOptions-Fill2": ethernetInterfaceProfile_BridgingOptions_Fill2,
       "ethernetInterfaceProfile-BridgingOptions-BridgeType": ethernetInterfaceProfile_BridgingOptions_BridgeType,
       "ethernetInterfaceProfile-BridgingOptions-Egress": ethernetInterfaceProfile_BridgingOptions_Egress,
       "ethernetInterfaceProfile-MediaSpeedMbit": ethernetInterfaceProfile_MediaSpeedMbit,
       "ethernetInterfaceProfile-AutoNegotiate": ethernetInterfaceProfile_AutoNegotiate,
       "ethernetInterfaceProfile-Action-o": ethernetInterfaceProfile_Action_o}
)
