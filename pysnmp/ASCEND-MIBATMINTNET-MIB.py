# SNMP MIB module (ASCEND-MIBATMINTNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMINTNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:08 2024
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

_MibatmInternalNetworkProfile_ObjectIdentity = ObjectIdentity
mibatmInternalNetworkProfile = _MibatmInternalNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 26)
)
_MibatmInternalNetworkProfileTable_Object = MibTable
mibatmInternalNetworkProfileTable = _MibatmInternalNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1)
)
if mibBuilder.loadTexts:
    mibatmInternalNetworkProfileTable.setStatus("mandatory")
_MibatmInternalNetworkProfileEntry_Object = MibTableRow
mibatmInternalNetworkProfileEntry = _MibatmInternalNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1)
)
mibatmInternalNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMINTNET-MIB", "atmInternalNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBATMINTNET-MIB", "atmInternalNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBATMINTNET-MIB", "atmInternalNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibatmInternalNetworkProfileEntry.setStatus("mandatory")
_AtmInternalNetworkProfile_Shelf_o_Type = Integer32
_AtmInternalNetworkProfile_Shelf_o_Object = MibScalar
atmInternalNetworkProfile_Shelf_o = _AtmInternalNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 1),
    _AtmInternalNetworkProfile_Shelf_o_Type()
)
atmInternalNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_Shelf_o.setStatus("mandatory")
_AtmInternalNetworkProfile_Slot_o_Type = Integer32
_AtmInternalNetworkProfile_Slot_o_Object = MibScalar
atmInternalNetworkProfile_Slot_o = _AtmInternalNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 2),
    _AtmInternalNetworkProfile_Slot_o_Type()
)
atmInternalNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_Slot_o.setStatus("mandatory")
_AtmInternalNetworkProfile_Item_o_Type = Integer32
_AtmInternalNetworkProfile_Item_o_Object = MibScalar
atmInternalNetworkProfile_Item_o = _AtmInternalNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 3),
    _AtmInternalNetworkProfile_Item_o_Type()
)
atmInternalNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_Item_o.setStatus("mandatory")
_AtmInternalNetworkProfile_Name_Type = DisplayString
_AtmInternalNetworkProfile_Name_Object = MibScalar
atmInternalNetworkProfile_Name = _AtmInternalNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 4),
    _AtmInternalNetworkProfile_Name_Type()
)
atmInternalNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_Name.setStatus("mandatory")


class _AtmInternalNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atmInternalNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_AtmInternalNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtmInternalNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
atmInternalNetworkProfile_PhysicalAddress_Shelf = _AtmInternalNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 5),
    _AtmInternalNetworkProfile_PhysicalAddress_Shelf_Type()
)
atmInternalNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtmInternalNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atmInternalNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_AtmInternalNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtmInternalNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
atmInternalNetworkProfile_PhysicalAddress_Slot = _AtmInternalNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 6),
    _AtmInternalNetworkProfile_PhysicalAddress_Slot_Type()
)
atmInternalNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_AtmInternalNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_AtmInternalNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
atmInternalNetworkProfile_PhysicalAddress_ItemNumber = _AtmInternalNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 7),
    _AtmInternalNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
atmInternalNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _AtmInternalNetworkProfile_Enabled_Type(Integer32):
    """Custom type atmInternalNetworkProfile_Enabled based on Integer32"""
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


_AtmInternalNetworkProfile_Enabled_Type.__name__ = "Integer32"
_AtmInternalNetworkProfile_Enabled_Object = MibScalar
atmInternalNetworkProfile_Enabled = _AtmInternalNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 8),
    _AtmInternalNetworkProfile_Enabled_Type()
)
atmInternalNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_Enabled.setStatus("mandatory")
_AtmInternalNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_AtmInternalNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
atmInternalNetworkProfile_LineConfig_NailedGroup = _AtmInternalNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 9),
    _AtmInternalNetworkProfile_LineConfig_NailedGroup_Type()
)
atmInternalNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")


class _AtmInternalNetworkProfile_Action_o_Type(Integer32):
    """Custom type atmInternalNetworkProfile_Action_o based on Integer32"""
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


_AtmInternalNetworkProfile_Action_o_Type.__name__ = "Integer32"
_AtmInternalNetworkProfile_Action_o_Object = MibScalar
atmInternalNetworkProfile_Action_o = _AtmInternalNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 10),
    _AtmInternalNetworkProfile_Action_o_Type()
)
atmInternalNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_Action_o.setStatus("mandatory")
_AtmInternalNetworkProfile_LineConfig_VpSwitchingVpi_Type = Integer32
_AtmInternalNetworkProfile_LineConfig_VpSwitchingVpi_Object = MibScalar
atmInternalNetworkProfile_LineConfig_VpSwitchingVpi = _AtmInternalNetworkProfile_LineConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 26, 1, 1, 11),
    _AtmInternalNetworkProfile_LineConfig_VpSwitchingVpi_Type()
)
atmInternalNetworkProfile_LineConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInternalNetworkProfile_LineConfig_VpSwitchingVpi.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMINTNET-MIB",
    **{"DisplayString": DisplayString,
       "mibatmInternalNetworkProfile": mibatmInternalNetworkProfile,
       "mibatmInternalNetworkProfileTable": mibatmInternalNetworkProfileTable,
       "mibatmInternalNetworkProfileEntry": mibatmInternalNetworkProfileEntry,
       "atmInternalNetworkProfile-Shelf-o": atmInternalNetworkProfile_Shelf_o,
       "atmInternalNetworkProfile-Slot-o": atmInternalNetworkProfile_Slot_o,
       "atmInternalNetworkProfile-Item-o": atmInternalNetworkProfile_Item_o,
       "atmInternalNetworkProfile-Name": atmInternalNetworkProfile_Name,
       "atmInternalNetworkProfile-PhysicalAddress-Shelf": atmInternalNetworkProfile_PhysicalAddress_Shelf,
       "atmInternalNetworkProfile-PhysicalAddress-Slot": atmInternalNetworkProfile_PhysicalAddress_Slot,
       "atmInternalNetworkProfile-PhysicalAddress-ItemNumber": atmInternalNetworkProfile_PhysicalAddress_ItemNumber,
       "atmInternalNetworkProfile-Enabled": atmInternalNetworkProfile_Enabled,
       "atmInternalNetworkProfile-LineConfig-NailedGroup": atmInternalNetworkProfile_LineConfig_NailedGroup,
       "atmInternalNetworkProfile-Action-o": atmInternalNetworkProfile_Action_o,
       "atmInternalNetworkProfile-LineConfig-VpSwitchingVpi": atmInternalNetworkProfile_LineConfig_VpSwitchingVpi}
)
