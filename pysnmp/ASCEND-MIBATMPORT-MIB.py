# SNMP MIB module (ASCEND-MIBATMPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMPORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:10 2024
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

_MibatmIntfConfProfile_ObjectIdentity = ObjectIdentity
mibatmIntfConfProfile = _MibatmIntfConfProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 51)
)
_MibatmIntfConfProfileTable_Object = MibTable
mibatmIntfConfProfileTable = _MibatmIntfConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1)
)
if mibBuilder.loadTexts:
    mibatmIntfConfProfileTable.setStatus("mandatory")
_MibatmIntfConfProfileEntry_Object = MibTableRow
mibatmIntfConfProfileEntry = _MibatmIntfConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1)
)
mibatmIntfConfProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMPORT-MIB", "atmIntfConfProfile-Shelf-o"),
    (0, "ASCEND-MIBATMPORT-MIB", "atmIntfConfProfile-Slot-o"),
    (0, "ASCEND-MIBATMPORT-MIB", "atmIntfConfProfile-Item-o"),
    (0, "ASCEND-MIBATMPORT-MIB", "atmIntfConfProfile-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibatmIntfConfProfileEntry.setStatus("mandatory")
_AtmIntfConfProfile_Shelf_o_Type = Integer32
_AtmIntfConfProfile_Shelf_o_Object = MibScalar
atmIntfConfProfile_Shelf_o = _AtmIntfConfProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 1),
    _AtmIntfConfProfile_Shelf_o_Type()
)
atmIntfConfProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Shelf_o.setStatus("mandatory")
_AtmIntfConfProfile_Slot_o_Type = Integer32
_AtmIntfConfProfile_Slot_o_Object = MibScalar
atmIntfConfProfile_Slot_o = _AtmIntfConfProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 2),
    _AtmIntfConfProfile_Slot_o_Type()
)
atmIntfConfProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Slot_o.setStatus("mandatory")
_AtmIntfConfProfile_Item_o_Type = Integer32
_AtmIntfConfProfile_Item_o_Object = MibScalar
atmIntfConfProfile_Item_o = _AtmIntfConfProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 3),
    _AtmIntfConfProfile_Item_o_Type()
)
atmIntfConfProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Item_o.setStatus("mandatory")
_AtmIntfConfProfile_LogicalItem_o_Type = Integer32
_AtmIntfConfProfile_LogicalItem_o_Object = MibScalar
atmIntfConfProfile_LogicalItem_o = _AtmIntfConfProfile_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 4),
    _AtmIntfConfProfile_LogicalItem_o_Type()
)
atmIntfConfProfile_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_LogicalItem_o.setStatus("mandatory")


class _AtmIntfConfProfile_Address_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atmIntfConfProfile_Address_PhysicalAddress_Shelf based on Integer32"""
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


_AtmIntfConfProfile_Address_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtmIntfConfProfile_Address_PhysicalAddress_Shelf_Object = MibScalar
atmIntfConfProfile_Address_PhysicalAddress_Shelf = _AtmIntfConfProfile_Address_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 5),
    _AtmIntfConfProfile_Address_PhysicalAddress_Shelf_Type()
)
atmIntfConfProfile_Address_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Address_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtmIntfConfProfile_Address_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atmIntfConfProfile_Address_PhysicalAddress_Slot based on Integer32"""
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


_AtmIntfConfProfile_Address_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtmIntfConfProfile_Address_PhysicalAddress_Slot_Object = MibScalar
atmIntfConfProfile_Address_PhysicalAddress_Slot = _AtmIntfConfProfile_Address_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 6),
    _AtmIntfConfProfile_Address_PhysicalAddress_Slot_Type()
)
atmIntfConfProfile_Address_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Address_PhysicalAddress_Slot.setStatus("mandatory")
_AtmIntfConfProfile_Address_PhysicalAddress_ItemNumber_Type = Integer32
_AtmIntfConfProfile_Address_PhysicalAddress_ItemNumber_Object = MibScalar
atmIntfConfProfile_Address_PhysicalAddress_ItemNumber = _AtmIntfConfProfile_Address_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 7),
    _AtmIntfConfProfile_Address_PhysicalAddress_ItemNumber_Type()
)
atmIntfConfProfile_Address_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Address_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmIntfConfProfile_Address_LogicalItem_Type = Integer32
_AtmIntfConfProfile_Address_LogicalItem_Object = MibScalar
atmIntfConfProfile_Address_LogicalItem = _AtmIntfConfProfile_Address_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 8),
    _AtmIntfConfProfile_Address_LogicalItem_Type()
)
atmIntfConfProfile_Address_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Address_LogicalItem.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_MaxVpcs_Type = Integer32
_AtmIntfConfProfile_BaseConfig_MaxVpcs_Object = MibScalar
atmIntfConfProfile_BaseConfig_MaxVpcs = _AtmIntfConfProfile_BaseConfig_MaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 9),
    _AtmIntfConfProfile_BaseConfig_MaxVpcs_Type()
)
atmIntfConfProfile_BaseConfig_MaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_MaxVpcs.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_MaxVccs_Type = Integer32
_AtmIntfConfProfile_BaseConfig_MaxVccs_Object = MibScalar
atmIntfConfProfile_BaseConfig_MaxVccs = _AtmIntfConfProfile_BaseConfig_MaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 10),
    _AtmIntfConfProfile_BaseConfig_MaxVccs_Type()
)
atmIntfConfProfile_BaseConfig_MaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_MaxVccs.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_MaxActiveVpiBits_Type = Integer32
_AtmIntfConfProfile_BaseConfig_MaxActiveVpiBits_Object = MibScalar
atmIntfConfProfile_BaseConfig_MaxActiveVpiBits = _AtmIntfConfProfile_BaseConfig_MaxActiveVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 11),
    _AtmIntfConfProfile_BaseConfig_MaxActiveVpiBits_Type()
)
atmIntfConfProfile_BaseConfig_MaxActiveVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_MaxActiveVpiBits.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_MaxActiveVciBits_Type = Integer32
_AtmIntfConfProfile_BaseConfig_MaxActiveVciBits_Object = MibScalar
atmIntfConfProfile_BaseConfig_MaxActiveVciBits = _AtmIntfConfProfile_BaseConfig_MaxActiveVciBits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 12),
    _AtmIntfConfProfile_BaseConfig_MaxActiveVciBits_Type()
)
atmIntfConfProfile_BaseConfig_MaxActiveVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_MaxActiveVciBits.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_IlmiVpi_Type = Integer32
_AtmIntfConfProfile_BaseConfig_IlmiVpi_Object = MibScalar
atmIntfConfProfile_BaseConfig_IlmiVpi = _AtmIntfConfProfile_BaseConfig_IlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 13),
    _AtmIntfConfProfile_BaseConfig_IlmiVpi_Type()
)
atmIntfConfProfile_BaseConfig_IlmiVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_IlmiVpi.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_IlmiVci_Type = Integer32
_AtmIntfConfProfile_BaseConfig_IlmiVci_Object = MibScalar
atmIntfConfProfile_BaseConfig_IlmiVci = _AtmIntfConfProfile_BaseConfig_IlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 14),
    _AtmIntfConfProfile_BaseConfig_IlmiVci_Type()
)
atmIntfConfProfile_BaseConfig_IlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_IlmiVci.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_NeighborIpAddress_Type = IpAddress
_AtmIntfConfProfile_BaseConfig_NeighborIpAddress_Object = MibScalar
atmIntfConfProfile_BaseConfig_NeighborIpAddress = _AtmIntfConfProfile_BaseConfig_NeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 15),
    _AtmIntfConfProfile_BaseConfig_NeighborIpAddress_Type()
)
atmIntfConfProfile_BaseConfig_NeighborIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_NeighborIpAddress.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_NeighborName_Type = DisplayString
_AtmIntfConfProfile_BaseConfig_NeighborName_Object = MibScalar
atmIntfConfProfile_BaseConfig_NeighborName = _AtmIntfConfProfile_BaseConfig_NeighborName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 16),
    _AtmIntfConfProfile_BaseConfig_NeighborName_Type()
)
atmIntfConfProfile_BaseConfig_NeighborName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_NeighborName.setStatus("mandatory")
_AtmIntfConfProfile_BaseConfig_SubscAtmAddress_Type = DisplayString
_AtmIntfConfProfile_BaseConfig_SubscAtmAddress_Object = MibScalar
atmIntfConfProfile_BaseConfig_SubscAtmAddress = _AtmIntfConfProfile_BaseConfig_SubscAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 17),
    _AtmIntfConfProfile_BaseConfig_SubscAtmAddress_Type()
)
atmIntfConfProfile_BaseConfig_SubscAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_BaseConfig_SubscAtmAddress.setStatus("mandatory")


class _AtmIntfConfProfile_ExtensionConfig_ConfigType_Type(Integer32):
    """Custom type atmIntfConfProfile_ExtensionConfig_ConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("atmfAutoConfig", 3),
          ("atmfPnni1dot0", 11),
          ("atmfUniPvcOnly", 13))
    )


_AtmIntfConfProfile_ExtensionConfig_ConfigType_Type.__name__ = "Integer32"
_AtmIntfConfProfile_ExtensionConfig_ConfigType_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_ConfigType = _AtmIntfConfProfile_ExtensionConfig_ConfigType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 18),
    _AtmIntfConfProfile_ExtensionConfig_ConfigType_Type()
)
atmIntfConfProfile_ExtensionConfig_ConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_ConfigType.setStatus("mandatory")


class _AtmIntfConfProfile_ExtensionConfig_ConfigSide_Type(Integer32):
    """Custom type atmIntfConfProfile_ExtensionConfig_ConfigSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("network", 4),
          ("other", 2),
          ("user", 3))
    )


_AtmIntfConfProfile_ExtensionConfig_ConfigSide_Type.__name__ = "Integer32"
_AtmIntfConfProfile_ExtensionConfig_ConfigSide_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_ConfigSide = _AtmIntfConfProfile_ExtensionConfig_ConfigSide_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 19),
    _AtmIntfConfProfile_ExtensionConfig_ConfigSide_Type()
)
atmIntfConfProfile_ExtensionConfig_ConfigSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_ConfigSide.setStatus("mandatory")


class _AtmIntfConfProfile_ExtensionConfig_IlmiAdminStatus_Type(Integer32):
    """Custom type atmIntfConfProfile_ExtensionConfig_IlmiAdminStatus based on Integer32"""
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


_AtmIntfConfProfile_ExtensionConfig_IlmiAdminStatus_Type.__name__ = "Integer32"
_AtmIntfConfProfile_ExtensionConfig_IlmiAdminStatus_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_IlmiAdminStatus = _AtmIntfConfProfile_ExtensionConfig_IlmiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 20),
    _AtmIntfConfProfile_ExtensionConfig_IlmiAdminStatus_Type()
)
atmIntfConfProfile_ExtensionConfig_IlmiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_IlmiAdminStatus.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_ConnEstabInterval_Type = Integer32
_AtmIntfConfProfile_ExtensionConfig_ConnEstabInterval_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_ConnEstabInterval = _AtmIntfConfProfile_ExtensionConfig_ConnEstabInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 21),
    _AtmIntfConfProfile_ExtensionConfig_ConnEstabInterval_Type()
)
atmIntfConfProfile_ExtensionConfig_ConnEstabInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_ConnEstabInterval.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_LossDetectInterval_Type = Integer32
_AtmIntfConfProfile_ExtensionConfig_LossDetectInterval_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_LossDetectInterval = _AtmIntfConfProfile_ExtensionConfig_LossDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 22),
    _AtmIntfConfProfile_ExtensionConfig_LossDetectInterval_Type()
)
atmIntfConfProfile_ExtensionConfig_LossDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_LossDetectInterval.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_PollInactFactor_Type = Integer32
_AtmIntfConfProfile_ExtensionConfig_PollInactFactor_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_PollInactFactor = _AtmIntfConfProfile_ExtensionConfig_PollInactFactor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 23),
    _AtmIntfConfProfile_ExtensionConfig_PollInactFactor_Type()
)
atmIntfConfProfile_ExtensionConfig_PollInactFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_PollInactFactor.setStatus("mandatory")


class _AtmIntfConfProfile_ExtensionConfig_DeviceType_Type(Integer32):
    """Custom type atmIntfConfProfile_ExtensionConfig_DeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("private", 4),
          ("public", 3))
    )


_AtmIntfConfProfile_ExtensionConfig_DeviceType_Type.__name__ = "Integer32"
_AtmIntfConfProfile_ExtensionConfig_DeviceType_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_DeviceType = _AtmIntfConfProfile_ExtensionConfig_DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 24),
    _AtmIntfConfProfile_ExtensionConfig_DeviceType_Type()
)
atmIntfConfProfile_ExtensionConfig_DeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_DeviceType.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi_Type = Integer32
_AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi = _AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 25),
    _AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi_Type()
)
atmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi_Type = Integer32
_AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi = _AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 26),
    _AtmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi_Type()
)
atmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci_Type = Integer32
_AtmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci = _AtmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 27),
    _AtmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci_Type()
)
atmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_SigVccRxQosName_Type = DisplayString
_AtmIntfConfProfile_ExtensionConfig_SigVccRxQosName_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_SigVccRxQosName = _AtmIntfConfProfile_ExtensionConfig_SigVccRxQosName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 28),
    _AtmIntfConfProfile_ExtensionConfig_SigVccRxQosName_Type()
)
atmIntfConfProfile_ExtensionConfig_SigVccRxQosName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_SigVccRxQosName.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_SigVccTxQosName_Type = DisplayString
_AtmIntfConfProfile_ExtensionConfig_SigVccTxQosName_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_SigVccTxQosName = _AtmIntfConfProfile_ExtensionConfig_SigVccTxQosName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 29),
    _AtmIntfConfProfile_ExtensionConfig_SigVccTxQosName_Type()
)
atmIntfConfProfile_ExtensionConfig_SigVccTxQosName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_SigVccTxQosName.setStatus("mandatory")


class _AtmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled_Type(Integer32):
    """Custom type atmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled based on Integer32"""
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


_AtmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled_Type.__name__ = "Integer32"
_AtmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled = _AtmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 30),
    _AtmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled_Type()
)
atmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled.setStatus("mandatory")
_AtmIntfConfProfile_ExtensionConfig_PvcFailureIntvl_Type = Integer32
_AtmIntfConfProfile_ExtensionConfig_PvcFailureIntvl_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_PvcFailureIntvl = _AtmIntfConfProfile_ExtensionConfig_PvcFailureIntvl_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 31),
    _AtmIntfConfProfile_ExtensionConfig_PvcFailureIntvl_Type()
)
atmIntfConfProfile_ExtensionConfig_PvcFailureIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_PvcFailureIntvl.setStatus("mandatory")


class _AtmIntfConfProfile_Action_o_Type(Integer32):
    """Custom type atmIntfConfProfile_Action_o based on Integer32"""
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


_AtmIntfConfProfile_Action_o_Type.__name__ = "Integer32"
_AtmIntfConfProfile_Action_o_Object = MibScalar
atmIntfConfProfile_Action_o = _AtmIntfConfProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 32),
    _AtmIntfConfProfile_Action_o_Type()
)
atmIntfConfProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_Action_o.setStatus("mandatory")


class _AtmIntfConfProfile_ExtensionConfig_IlmiConnectivity_Type(Integer32):
    """Custom type atmIntfConfProfile_ExtensionConfig_IlmiConnectivity based on Integer32"""
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


_AtmIntfConfProfile_ExtensionConfig_IlmiConnectivity_Type.__name__ = "Integer32"
_AtmIntfConfProfile_ExtensionConfig_IlmiConnectivity_Object = MibScalar
atmIntfConfProfile_ExtensionConfig_IlmiConnectivity = _AtmIntfConfProfile_ExtensionConfig_IlmiConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 51, 1, 1, 33),
    _AtmIntfConfProfile_ExtensionConfig_IlmiConnectivity_Type()
)
atmIntfConfProfile_ExtensionConfig_IlmiConnectivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfProfile_ExtensionConfig_IlmiConnectivity.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMPORT-MIB",
    **{"DisplayString": DisplayString,
       "mibatmIntfConfProfile": mibatmIntfConfProfile,
       "mibatmIntfConfProfileTable": mibatmIntfConfProfileTable,
       "mibatmIntfConfProfileEntry": mibatmIntfConfProfileEntry,
       "atmIntfConfProfile-Shelf-o": atmIntfConfProfile_Shelf_o,
       "atmIntfConfProfile-Slot-o": atmIntfConfProfile_Slot_o,
       "atmIntfConfProfile-Item-o": atmIntfConfProfile_Item_o,
       "atmIntfConfProfile-LogicalItem-o": atmIntfConfProfile_LogicalItem_o,
       "atmIntfConfProfile-Address-PhysicalAddress-Shelf": atmIntfConfProfile_Address_PhysicalAddress_Shelf,
       "atmIntfConfProfile-Address-PhysicalAddress-Slot": atmIntfConfProfile_Address_PhysicalAddress_Slot,
       "atmIntfConfProfile-Address-PhysicalAddress-ItemNumber": atmIntfConfProfile_Address_PhysicalAddress_ItemNumber,
       "atmIntfConfProfile-Address-LogicalItem": atmIntfConfProfile_Address_LogicalItem,
       "atmIntfConfProfile-BaseConfig-MaxVpcs": atmIntfConfProfile_BaseConfig_MaxVpcs,
       "atmIntfConfProfile-BaseConfig-MaxVccs": atmIntfConfProfile_BaseConfig_MaxVccs,
       "atmIntfConfProfile-BaseConfig-MaxActiveVpiBits": atmIntfConfProfile_BaseConfig_MaxActiveVpiBits,
       "atmIntfConfProfile-BaseConfig-MaxActiveVciBits": atmIntfConfProfile_BaseConfig_MaxActiveVciBits,
       "atmIntfConfProfile-BaseConfig-IlmiVpi": atmIntfConfProfile_BaseConfig_IlmiVpi,
       "atmIntfConfProfile-BaseConfig-IlmiVci": atmIntfConfProfile_BaseConfig_IlmiVci,
       "atmIntfConfProfile-BaseConfig-NeighborIpAddress": atmIntfConfProfile_BaseConfig_NeighborIpAddress,
       "atmIntfConfProfile-BaseConfig-NeighborName": atmIntfConfProfile_BaseConfig_NeighborName,
       "atmIntfConfProfile-BaseConfig-SubscAtmAddress": atmIntfConfProfile_BaseConfig_SubscAtmAddress,
       "atmIntfConfProfile-ExtensionConfig-ConfigType": atmIntfConfProfile_ExtensionConfig_ConfigType,
       "atmIntfConfProfile-ExtensionConfig-ConfigSide": atmIntfConfProfile_ExtensionConfig_ConfigSide,
       "atmIntfConfProfile-ExtensionConfig-IlmiAdminStatus": atmIntfConfProfile_ExtensionConfig_IlmiAdminStatus,
       "atmIntfConfProfile-ExtensionConfig-ConnEstabInterval": atmIntfConfProfile_ExtensionConfig_ConnEstabInterval,
       "atmIntfConfProfile-ExtensionConfig-LossDetectInterval": atmIntfConfProfile_ExtensionConfig_LossDetectInterval,
       "atmIntfConfProfile-ExtensionConfig-PollInactFactor": atmIntfConfProfile_ExtensionConfig_PollInactFactor,
       "atmIntfConfProfile-ExtensionConfig-DeviceType": atmIntfConfProfile_ExtensionConfig_DeviceType,
       "atmIntfConfProfile-ExtensionConfig-MaxSwitchedVpcVpi": atmIntfConfProfile_ExtensionConfig_MaxSwitchedVpcVpi,
       "atmIntfConfProfile-ExtensionConfig-MaxSwitchedVccVpi": atmIntfConfProfile_ExtensionConfig_MaxSwitchedVccVpi,
       "atmIntfConfProfile-ExtensionConfig-MinSwitchedVccVci": atmIntfConfProfile_ExtensionConfig_MinSwitchedVccVci,
       "atmIntfConfProfile-ExtensionConfig-SigVccRxQosName": atmIntfConfProfile_ExtensionConfig_SigVccRxQosName,
       "atmIntfConfProfile-ExtensionConfig-SigVccTxQosName": atmIntfConfProfile_ExtensionConfig_SigVccTxQosName,
       "atmIntfConfProfile-ExtensionConfig-PvcFailureTrapEnabled": atmIntfConfProfile_ExtensionConfig_PvcFailureTrapEnabled,
       "atmIntfConfProfile-ExtensionConfig-PvcFailureIntvl": atmIntfConfProfile_ExtensionConfig_PvcFailureIntvl,
       "atmIntfConfProfile-Action-o": atmIntfConfProfile_Action_o,
       "atmIntfConfProfile-ExtensionConfig-IlmiConnectivity": atmIntfConfProfile_ExtensionConfig_IlmiConnectivity}
)
