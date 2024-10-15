# SNMP MIB module (ASCEND-MIBSDSLNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSDSLNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:10 2024
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

_MibsdslNetworkProfile_ObjectIdentity = ObjectIdentity
mibsdslNetworkProfile = _MibsdslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 8)
)
_MibsdslNetworkProfileTable_Object = MibTable
mibsdslNetworkProfileTable = _MibsdslNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1)
)
if mibBuilder.loadTexts:
    mibsdslNetworkProfileTable.setStatus("mandatory")
_MibsdslNetworkProfileEntry_Object = MibTableRow
mibsdslNetworkProfileEntry = _MibsdslNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1)
)
mibsdslNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSDSLNET-MIB", "sdslNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBSDSLNET-MIB", "sdslNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBSDSLNET-MIB", "sdslNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibsdslNetworkProfileEntry.setStatus("mandatory")
_SdslNetworkProfile_Shelf_o_Type = Integer32
_SdslNetworkProfile_Shelf_o_Object = MibScalar
sdslNetworkProfile_Shelf_o = _SdslNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 1),
    _SdslNetworkProfile_Shelf_o_Type()
)
sdslNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslNetworkProfile_Shelf_o.setStatus("mandatory")
_SdslNetworkProfile_Slot_o_Type = Integer32
_SdslNetworkProfile_Slot_o_Object = MibScalar
sdslNetworkProfile_Slot_o = _SdslNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 2),
    _SdslNetworkProfile_Slot_o_Type()
)
sdslNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslNetworkProfile_Slot_o.setStatus("mandatory")
_SdslNetworkProfile_Item_o_Type = Integer32
_SdslNetworkProfile_Item_o_Object = MibScalar
sdslNetworkProfile_Item_o = _SdslNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 3),
    _SdslNetworkProfile_Item_o_Type()
)
sdslNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslNetworkProfile_Item_o.setStatus("mandatory")
_SdslNetworkProfile_Name_Type = DisplayString
_SdslNetworkProfile_Name_Object = MibScalar
sdslNetworkProfile_Name = _SdslNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 4),
    _SdslNetworkProfile_Name_Type()
)
sdslNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_Name.setStatus("mandatory")


class _SdslNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type sdslNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_SdslNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_SdslNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
sdslNetworkProfile_PhysicalAddress_Shelf = _SdslNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 5),
    _SdslNetworkProfile_PhysicalAddress_Shelf_Type()
)
sdslNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _SdslNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type sdslNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_SdslNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_SdslNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
sdslNetworkProfile_PhysicalAddress_Slot = _SdslNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 6),
    _SdslNetworkProfile_PhysicalAddress_Slot_Type()
)
sdslNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_SdslNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_SdslNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
sdslNetworkProfile_PhysicalAddress_ItemNumber = _SdslNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 7),
    _SdslNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
sdslNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _SdslNetworkProfile_Enabled_Type(Integer32):
    """Custom type sdslNetworkProfile_Enabled based on Integer32"""
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


_SdslNetworkProfile_Enabled_Type.__name__ = "Integer32"
_SdslNetworkProfile_Enabled_Object = MibScalar
sdslNetworkProfile_Enabled = _SdslNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 8),
    _SdslNetworkProfile_Enabled_Type()
)
sdslNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_Enabled.setStatus("mandatory")
_SdslNetworkProfile_ProfileNumber_Type = Integer32
_SdslNetworkProfile_ProfileNumber_Object = MibScalar
sdslNetworkProfile_ProfileNumber = _SdslNetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 9),
    _SdslNetworkProfile_ProfileNumber_Type()
)
sdslNetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_ProfileNumber.setStatus("mandatory")
_SdslNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_SdslNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
sdslNetworkProfile_LineConfig_TrunkGroup = _SdslNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 10),
    _SdslNetworkProfile_LineConfig_TrunkGroup_Type()
)
sdslNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_SdslNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_SdslNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
sdslNetworkProfile_LineConfig_NailedGroup = _SdslNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 11),
    _SdslNetworkProfile_LineConfig_NailedGroup_Type()
)
sdslNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")
_SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type = Integer32
_SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object = MibScalar
sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber = _SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 12),
    _SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber_Type()
)
sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber.setStatus("mandatory")
_SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type = Integer32
_SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object = MibScalar
sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber = _SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 13),
    _SdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber_Type()
)
sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber.setStatus("mandatory")
_SdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type = Integer32
_SdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object = MibScalar
sdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber = _SdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 14),
    _SdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber_Type()
)
sdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_Activation_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_Activation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dcdDsrActive", 3),
          ("dsrActive", 2),
          ("static", 1))
    )


_SdslNetworkProfile_LineConfig_Activation_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_Activation_Object = MibScalar
sdslNetworkProfile_LineConfig_Activation = _SdslNetworkProfile_LineConfig_Activation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 15),
    _SdslNetworkProfile_LineConfig_Activation_Type()
)
sdslNetworkProfile_LineConfig_Activation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_Activation.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_DataRateMode_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_DataRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 2),
          ("fastautobaud", 4),
          ("singlebaud", 3))
    )


_SdslNetworkProfile_LineConfig_DataRateMode_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_DataRateMode_Object = MibScalar
sdslNetworkProfile_LineConfig_DataRateMode = _SdslNetworkProfile_LineConfig_DataRateMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 19),
    _SdslNetworkProfile_LineConfig_DataRateMode_Type()
)
sdslNetworkProfile_LineConfig_DataRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_DataRateMode.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_MaxRate_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_MaxRate based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("n-1040000", 15),
          ("n-1152000", 16),
          ("n-1168000", 6),
          ("n-144000", 1),
          ("n-1536000", 17),
          ("n-1552000", 7),
          ("n-1568000", 18),
          ("n-160000", 9),
          ("n-1680000", 19),
          ("n-192000", 10),
          ("n-1920000", 20),
          ("n-208000", 11),
          ("n-2160000", 21),
          ("n-2320000", 8),
          ("n-272000", 2),
          ("n-384000", 12),
          ("n-400000", 3),
          ("n-416000", 13),
          ("n-528000", 4),
          ("n-768000", 14),
          ("n-784000", 5))
    )


_SdslNetworkProfile_LineConfig_MaxRate_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_MaxRate_Object = MibScalar
sdslNetworkProfile_LineConfig_MaxRate = _SdslNetworkProfile_LineConfig_MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 20),
    _SdslNetworkProfile_LineConfig_MaxRate_Type()
)
sdslNetworkProfile_LineConfig_MaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_MaxRate.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_UnitType_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_UnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coe", 1),
          ("cpe", 2))
    )


_SdslNetworkProfile_LineConfig_UnitType_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_UnitType_Object = MibScalar
sdslNetworkProfile_LineConfig_UnitType = _SdslNetworkProfile_LineConfig_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 21),
    _SdslNetworkProfile_LineConfig_UnitType_Type()
)
sdslNetworkProfile_LineConfig_UnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_UnitType.setStatus("mandatory")


class _SdslNetworkProfile_Action_o_Type(Integer32):
    """Custom type sdslNetworkProfile_Action_o based on Integer32"""
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


_SdslNetworkProfile_Action_o_Type.__name__ = "Integer32"
_SdslNetworkProfile_Action_o_Object = MibScalar
sdslNetworkProfile_Action_o = _SdslNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 22),
    _SdslNetworkProfile_Action_o_Type()
)
sdslNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_Action_o.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_Enabled_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_Enabled based on Integer32"""
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


_SdslNetworkProfile_LineConfig_Enabled_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_Enabled_Object = MibScalar
sdslNetworkProfile_LineConfig_Enabled = _SdslNetworkProfile_LineConfig_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 24),
    _SdslNetworkProfile_LineConfig_Enabled_Type()
)
sdslNetworkProfile_LineConfig_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_Enabled.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_AutoBaseRate_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_AutoBaseRate based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("n-1040000", 15),
          ("n-1152000", 16),
          ("n-1168000", 6),
          ("n-144000", 1),
          ("n-1536000", 17),
          ("n-1552000", 7),
          ("n-1568000", 18),
          ("n-160000", 9),
          ("n-1680000", 19),
          ("n-192000", 10),
          ("n-1920000", 20),
          ("n-208000", 11),
          ("n-2160000", 21),
          ("n-2320000", 8),
          ("n-272000", 2),
          ("n-384000", 12),
          ("n-400000", 3),
          ("n-416000", 13),
          ("n-528000", 4),
          ("n-768000", 14),
          ("n-784000", 5))
    )


_SdslNetworkProfile_LineConfig_AutoBaseRate_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_AutoBaseRate_Object = MibScalar
sdslNetworkProfile_LineConfig_AutoBaseRate = _SdslNetworkProfile_LineConfig_AutoBaseRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 25),
    _SdslNetworkProfile_LineConfig_AutoBaseRate_Type()
)
sdslNetworkProfile_LineConfig_AutoBaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_AutoBaseRate.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_DataSense_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_DataSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inv", 2),
          ("normal", 1))
    )


_SdslNetworkProfile_LineConfig_DataSense_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_DataSense_Object = MibScalar
sdslNetworkProfile_LineConfig_DataSense = _SdslNetworkProfile_LineConfig_DataSense_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 26),
    _SdslNetworkProfile_LineConfig_DataSense_Type()
)
sdslNetworkProfile_LineConfig_DataSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_DataSense.setStatus("mandatory")
_SdslNetworkProfile_LineConfig_VpSwitchingVpi_Type = Integer32
_SdslNetworkProfile_LineConfig_VpSwitchingVpi_Object = MibScalar
sdslNetworkProfile_LineConfig_VpSwitchingVpi = _SdslNetworkProfile_LineConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 27),
    _SdslNetworkProfile_LineConfig_VpSwitchingVpi_Type()
)
sdslNetworkProfile_LineConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus("mandatory")
_SdslNetworkProfile_DhcpConfig_IpAddress_Type = IpAddress
_SdslNetworkProfile_DhcpConfig_IpAddress_Object = MibScalar
sdslNetworkProfile_DhcpConfig_IpAddress = _SdslNetworkProfile_DhcpConfig_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 28),
    _SdslNetworkProfile_DhcpConfig_IpAddress_Type()
)
sdslNetworkProfile_DhcpConfig_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_DhcpConfig_IpAddress.setStatus("mandatory")
_SdslNetworkProfile_DhcpConfig_MaxLease_Type = Integer32
_SdslNetworkProfile_DhcpConfig_MaxLease_Object = MibScalar
sdslNetworkProfile_DhcpConfig_MaxLease = _SdslNetworkProfile_DhcpConfig_MaxLease_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 29),
    _SdslNetworkProfile_DhcpConfig_MaxLease_Type()
)
sdslNetworkProfile_DhcpConfig_MaxLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_DhcpConfig_MaxLease.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_SdslDataFormat_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_SdslDataFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("serial", 1)
    )


_SdslNetworkProfile_LineConfig_SdslDataFormat_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_SdslDataFormat_Object = MibScalar
sdslNetworkProfile_LineConfig_SdslDataFormat = _SdslNetworkProfile_LineConfig_SdslDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 30),
    _SdslNetworkProfile_LineConfig_SdslDataFormat_Type()
)
sdslNetworkProfile_LineConfig_SdslDataFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_SdslDataFormat.setStatus("mandatory")


class _SdslNetworkProfile_SparingMode_Type(Integer32):
    """Custom type sdslNetworkProfile_SparingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("inactive", 1),
          ("manual", 2))
    )


_SdslNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_SdslNetworkProfile_SparingMode_Object = MibScalar
sdslNetworkProfile_SparingMode = _SdslNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 31),
    _SdslNetworkProfile_SparingMode_Type()
)
sdslNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_SparingMode.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_LineMode_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_LineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("hdlc", 2))
    )


_SdslNetworkProfile_LineConfig_LineMode_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_LineMode_Object = MibScalar
sdslNetworkProfile_LineConfig_LineMode = _SdslNetworkProfile_LineConfig_LineMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 32),
    _SdslNetworkProfile_LineConfig_LineMode_Type()
)
sdslNetworkProfile_LineConfig_LineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_LineMode.setStatus("mandatory")


class _SdslNetworkProfile_LineConfig_LoopBack_Type(Integer32):
    """Custom type sdslNetworkProfile_LineConfig_LoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 3),
          ("none", 1))
    )


_SdslNetworkProfile_LineConfig_LoopBack_Type.__name__ = "Integer32"
_SdslNetworkProfile_LineConfig_LoopBack_Object = MibScalar
sdslNetworkProfile_LineConfig_LoopBack = _SdslNetworkProfile_LineConfig_LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 33),
    _SdslNetworkProfile_LineConfig_LoopBack_Type()
)
sdslNetworkProfile_LineConfig_LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_LineConfig_LoopBack.setStatus("mandatory")


class _SdslNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type sdslNetworkProfile_IgnoreLineup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("systemDefined", 1),
          ("yes", 3))
    )


_SdslNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_SdslNetworkProfile_IgnoreLineup_Object = MibScalar
sdslNetworkProfile_IgnoreLineup = _SdslNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 8, 1, 1, 34),
    _SdslNetworkProfile_IgnoreLineup_Type()
)
sdslNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslNetworkProfile_IgnoreLineup.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSDSLNET-MIB",
    **{"DisplayString": DisplayString,
       "mibsdslNetworkProfile": mibsdslNetworkProfile,
       "mibsdslNetworkProfileTable": mibsdslNetworkProfileTable,
       "mibsdslNetworkProfileEntry": mibsdslNetworkProfileEntry,
       "sdslNetworkProfile-Shelf-o": sdslNetworkProfile_Shelf_o,
       "sdslNetworkProfile-Slot-o": sdslNetworkProfile_Slot_o,
       "sdslNetworkProfile-Item-o": sdslNetworkProfile_Item_o,
       "sdslNetworkProfile-Name": sdslNetworkProfile_Name,
       "sdslNetworkProfile-PhysicalAddress-Shelf": sdslNetworkProfile_PhysicalAddress_Shelf,
       "sdslNetworkProfile-PhysicalAddress-Slot": sdslNetworkProfile_PhysicalAddress_Slot,
       "sdslNetworkProfile-PhysicalAddress-ItemNumber": sdslNetworkProfile_PhysicalAddress_ItemNumber,
       "sdslNetworkProfile-Enabled": sdslNetworkProfile_Enabled,
       "sdslNetworkProfile-ProfileNumber": sdslNetworkProfile_ProfileNumber,
       "sdslNetworkProfile-LineConfig-TrunkGroup": sdslNetworkProfile_LineConfig_TrunkGroup,
       "sdslNetworkProfile-LineConfig-NailedGroup": sdslNetworkProfile_LineConfig_NailedGroup,
       "sdslNetworkProfile-LineConfig-RoutePort-SlotNumber-SlotNumber": sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_SlotNumber,
       "sdslNetworkProfile-LineConfig-RoutePort-SlotNumber-ShelfNumber": sdslNetworkProfile_LineConfig_RoutePort_SlotNumber_ShelfNumber,
       "sdslNetworkProfile-LineConfig-RoutePort-RelativePortNumber-RelativePortNumber": sdslNetworkProfile_LineConfig_RoutePort_RelativePortNumber_RelativePortNumber,
       "sdslNetworkProfile-LineConfig-Activation": sdslNetworkProfile_LineConfig_Activation,
       "sdslNetworkProfile-LineConfig-DataRateMode": sdslNetworkProfile_LineConfig_DataRateMode,
       "sdslNetworkProfile-LineConfig-MaxRate": sdslNetworkProfile_LineConfig_MaxRate,
       "sdslNetworkProfile-LineConfig-UnitType": sdslNetworkProfile_LineConfig_UnitType,
       "sdslNetworkProfile-Action-o": sdslNetworkProfile_Action_o,
       "sdslNetworkProfile-LineConfig-Enabled": sdslNetworkProfile_LineConfig_Enabled,
       "sdslNetworkProfile-LineConfig-AutoBaseRate": sdslNetworkProfile_LineConfig_AutoBaseRate,
       "sdslNetworkProfile-LineConfig-DataSense": sdslNetworkProfile_LineConfig_DataSense,
       "sdslNetworkProfile-LineConfig-VpSwitchingVpi": sdslNetworkProfile_LineConfig_VpSwitchingVpi,
       "sdslNetworkProfile-DhcpConfig-IpAddress": sdslNetworkProfile_DhcpConfig_IpAddress,
       "sdslNetworkProfile-DhcpConfig-MaxLease": sdslNetworkProfile_DhcpConfig_MaxLease,
       "sdslNetworkProfile-LineConfig-SdslDataFormat": sdslNetworkProfile_LineConfig_SdslDataFormat,
       "sdslNetworkProfile-SparingMode": sdslNetworkProfile_SparingMode,
       "sdslNetworkProfile-LineConfig-LineMode": sdslNetworkProfile_LineConfig_LineMode,
       "sdslNetworkProfile-LineConfig-LoopBack": sdslNetworkProfile_LineConfig_LoopBack,
       "sdslNetworkProfile-IgnoreLineup": sdslNetworkProfile_IgnoreLineup}
)
