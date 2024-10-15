# SNMP MIB module (ASCEND-MIBOC3ATMNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBOC3ATMNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:57 2024
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

_Miboc3AtmNetworkProfile_ObjectIdentity = ObjectIdentity
miboc3AtmNetworkProfile = _Miboc3AtmNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 11)
)
_Miboc3AtmNetworkProfileTable_Object = MibTable
miboc3AtmNetworkProfileTable = _Miboc3AtmNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1)
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfileTable.setStatus("mandatory")
_Miboc3AtmNetworkProfileEntry_Object = MibTableRow
miboc3AtmNetworkProfileEntry = _Miboc3AtmNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1)
)
miboc3AtmNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfileEntry.setStatus("mandatory")
_Oc3AtmNetworkProfile_Shelf_o_Type = Integer32
_Oc3AtmNetworkProfile_Shelf_o_Object = MibScalar
oc3AtmNetworkProfile_Shelf_o = _Oc3AtmNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 1),
    _Oc3AtmNetworkProfile_Shelf_o_Type()
)
oc3AtmNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_Shelf_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_Slot_o_Type = Integer32
_Oc3AtmNetworkProfile_Slot_o_Object = MibScalar
oc3AtmNetworkProfile_Slot_o = _Oc3AtmNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 2),
    _Oc3AtmNetworkProfile_Slot_o_Type()
)
oc3AtmNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_Slot_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_Item_o_Type = Integer32
_Oc3AtmNetworkProfile_Item_o_Object = MibScalar
oc3AtmNetworkProfile_Item_o = _Oc3AtmNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 3),
    _Oc3AtmNetworkProfile_Item_o_Type()
)
oc3AtmNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_Item_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_Name_Type = DisplayString
_Oc3AtmNetworkProfile_Name_Object = MibScalar
oc3AtmNetworkProfile_Name = _Oc3AtmNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 4),
    _Oc3AtmNetworkProfile_Name_Type()
)
oc3AtmNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_Name.setStatus("mandatory")


class _Oc3AtmNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_Oc3AtmNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
oc3AtmNetworkProfile_PhysicalAddress_Shelf = _Oc3AtmNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 5),
    _Oc3AtmNetworkProfile_PhysicalAddress_Shelf_Type()
)
oc3AtmNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _Oc3AtmNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_Oc3AtmNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
oc3AtmNetworkProfile_PhysicalAddress_Slot = _Oc3AtmNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 6),
    _Oc3AtmNetworkProfile_PhysicalAddress_Slot_Type()
)
oc3AtmNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_Oc3AtmNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_Oc3AtmNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
oc3AtmNetworkProfile_PhysicalAddress_ItemNumber = _Oc3AtmNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 7),
    _Oc3AtmNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
oc3AtmNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _Oc3AtmNetworkProfile_Enabled_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_Enabled based on Integer32"""
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


_Oc3AtmNetworkProfile_Enabled_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_Enabled_Object = MibScalar
oc3AtmNetworkProfile_Enabled = _Oc3AtmNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 8),
    _Oc3AtmNetworkProfile_Enabled_Type()
)
oc3AtmNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_Enabled.setStatus("mandatory")


class _Oc3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_SparePhysicalAddress_Shelf based on Integer32"""
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


_Oc3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_SparePhysicalAddress_Shelf_Object = MibScalar
oc3AtmNetworkProfile_SparePhysicalAddress_Shelf = _Oc3AtmNetworkProfile_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 9),
    _Oc3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type()
)
oc3AtmNetworkProfile_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _Oc3AtmNetworkProfile_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_SparePhysicalAddress_Slot based on Integer32"""
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


_Oc3AtmNetworkProfile_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_SparePhysicalAddress_Slot_Object = MibScalar
oc3AtmNetworkProfile_SparePhysicalAddress_Slot = _Oc3AtmNetworkProfile_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 10),
    _Oc3AtmNetworkProfile_SparePhysicalAddress_Slot_Type()
)
oc3AtmNetworkProfile_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_SparePhysicalAddress_Slot.setStatus("mandatory")
_Oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Type = Integer32
_Oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Object = MibScalar
oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber = _Oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 11),
    _Oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Type()
)
oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _Oc3AtmNetworkProfile_SparingMode_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_SparingMode based on Integer32"""
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


_Oc3AtmNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_SparingMode_Object = MibScalar
oc3AtmNetworkProfile_SparingMode = _Oc3AtmNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 12),
    _Oc3AtmNetworkProfile_SparingMode_Type()
)
oc3AtmNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_SparingMode.setStatus("mandatory")
_Oc3AtmNetworkProfile_ProfileNumber_Type = Integer32
_Oc3AtmNetworkProfile_ProfileNumber_Object = MibScalar
oc3AtmNetworkProfile_ProfileNumber = _Oc3AtmNetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 13),
    _Oc3AtmNetworkProfile_ProfileNumber_Type()
)
oc3AtmNetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_ProfileNumber.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrunkGroup = _Oc3AtmNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 14),
    _Oc3AtmNetworkProfile_LineConfig_TrunkGroup_Type()
)
oc3AtmNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_NailedGroup = _Oc3AtmNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 15),
    _Oc3AtmNetworkProfile_LineConfig_NailedGroup_Type()
)
oc3AtmNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_Loopback_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_Loopback based on Integer32"""
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
        *(("atmLayerLoopback", 4),
          ("facilityLoopback", 2),
          ("localLoopback", 3),
          ("noLoopback", 1))
    )


_Oc3AtmNetworkProfile_LineConfig_Loopback_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_Loopback_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_Loopback = _Oc3AtmNetworkProfile_LineConfig_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 19),
    _Oc3AtmNetworkProfile_LineConfig_Loopback_Type()
)
oc3AtmNetworkProfile_LineConfig_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_Loopback.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_FramerRate_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_FramerRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sTS1", 2),
          ("sTS3c", 1))
    )


_Oc3AtmNetworkProfile_LineConfig_FramerRate_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_FramerRate_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_FramerRate = _Oc3AtmNetworkProfile_LineConfig_FramerRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 20),
    _Oc3AtmNetworkProfile_LineConfig_FramerRate_Type()
)
oc3AtmNetworkProfile_LineConfig_FramerRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_FramerRate.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled = _Oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 21),
    _Oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled_Type()
)
oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled = _Oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 22),
    _Oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled_Type()
)
oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled = _Oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 23),
    _Oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled_Type()
)
oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled = _Oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 24),
    _Oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled_Type()
)
oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_LoopTiming_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_LoopTiming based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_LoopTiming_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_LoopTiming_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_LoopTiming = _Oc3AtmNetworkProfile_LineConfig_LoopTiming_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 25),
    _Oc3AtmNetworkProfile_LineConfig_LoopTiming_Type()
)
oc3AtmNetworkProfile_LineConfig_LoopTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_LoopTiming.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_VpiVciRange_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_VpiVciRange based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n-01-3232767", 1),
          ("n-0127-32511", 7),
          ("n-015-324095", 4),
          ("n-0255-32255", 8),
          ("n-03-3216383", 2),
          ("n-031-322047", 5),
          ("n-063-321023", 6),
          ("n-07-328191", 3),
          ("vpi0255Vci321023", 11),
          ("vpi0255Vci3216383", 15),
          ("vpi0255Vci322047", 12),
          ("vpi0255Vci32255", 9),
          ("vpi0255Vci324095", 13),
          ("vpi0255Vci32511", 10),
          ("vpi0255Vci328191", 14))
    )


_Oc3AtmNetworkProfile_LineConfig_VpiVciRange_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_VpiVciRange_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_VpiVciRange = _Oc3AtmNetworkProfile_LineConfig_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 26),
    _Oc3AtmNetworkProfile_LineConfig_VpiVciRange_Type()
)
oc3AtmNetworkProfile_LineConfig_VpiVciRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_VpiVciRange.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_ClockSource_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_ClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("notEligible", 2))
    )


_Oc3AtmNetworkProfile_LineConfig_ClockSource_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_ClockSource_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_ClockSource = _Oc3AtmNetworkProfile_LineConfig_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 27),
    _Oc3AtmNetworkProfile_LineConfig_ClockSource_Type()
)
oc3AtmNetworkProfile_LineConfig_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_ClockSource.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_ClockPriority_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_ClockPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("lowPriority", 4),
          ("middlePriority", 3))
    )


_Oc3AtmNetworkProfile_LineConfig_ClockPriority_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_ClockPriority_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_ClockPriority = _Oc3AtmNetworkProfile_LineConfig_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 28),
    _Oc3AtmNetworkProfile_LineConfig_ClockPriority_Type()
)
oc3AtmNetworkProfile_LineConfig_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_ClockPriority.setStatus("mandatory")


class _Oc3AtmNetworkProfile_Action_o_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_Action_o based on Integer32"""
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


_Oc3AtmNetworkProfile_Action_o_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_Action_o_Object = MibScalar
oc3AtmNetworkProfile_Action_o = _Oc3AtmNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 29),
    _Oc3AtmNetworkProfile_Action_o_Type()
)
oc3AtmNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_Action_o.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_FramerMode_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_FramerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_Oc3AtmNetworkProfile_LineConfig_FramerMode_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_FramerMode_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_FramerMode = _Oc3AtmNetworkProfile_LineConfig_FramerMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 30),
    _Oc3AtmNetworkProfile_LineConfig_FramerMode_Type()
)
oc3AtmNetworkProfile_LineConfig_FramerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_FramerMode.setStatus("mandatory")


class _Oc3AtmNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_IgnoreLineup based on Integer32"""
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


_Oc3AtmNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_IgnoreLineup_Object = MibScalar
oc3AtmNetworkProfile_IgnoreLineup = _Oc3AtmNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 31),
    _Oc3AtmNetworkProfile_IgnoreLineup_Type()
)
oc3AtmNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_IgnoreLineup.setStatus("mandatory")
_Oc3AtmNetworkProfile_ApsConfigName_Type = DisplayString
_Oc3AtmNetworkProfile_ApsConfigName_Object = MibScalar
oc3AtmNetworkProfile_ApsConfigName = _Oc3AtmNetworkProfile_ApsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 1, 1, 32),
    _Oc3AtmNetworkProfile_ApsConfigName_Type()
)
oc3AtmNetworkProfile_ApsConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_ApsConfigName.setStatus("mandatory")
_Miboc3AtmNetworkProfile_LineConfig_IncomingVCCsTable_Object = MibTable
miboc3AtmNetworkProfile_LineConfig_IncomingVCCsTable = _Miboc3AtmNetworkProfile_LineConfig_IncomingVCCsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2)
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfile_LineConfig_IncomingVCCsTable.setStatus("mandatory")
_Miboc3AtmNetworkProfile_LineConfig_IncomingVCCsEntry_Object = MibTableRow
miboc3AtmNetworkProfile_LineConfig_IncomingVCCsEntry = _Miboc3AtmNetworkProfile_LineConfig_IncomingVCCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1)
)
miboc3AtmNetworkProfile_LineConfig_IncomingVCCsEntry.setIndexNames(
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o"),
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfile_LineConfig_IncomingVCCsEntry.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 1),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 2),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 3),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 4),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 5),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 6),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 7),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci = _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 2, 1, 8),
    _Oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Type()
)
oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci.setStatus("mandatory")
_Miboc3AtmNetworkProfile_LineConfig_TrafficShapersTable_Object = MibTable
miboc3AtmNetworkProfile_LineConfig_TrafficShapersTable = _Miboc3AtmNetworkProfile_LineConfig_TrafficShapersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3)
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfile_LineConfig_TrafficShapersTable.setStatus("mandatory")
_Miboc3AtmNetworkProfile_LineConfig_TrafficShapersEntry_Object = MibTableRow
miboc3AtmNetworkProfile_LineConfig_TrafficShapersEntry = _Miboc3AtmNetworkProfile_LineConfig_TrafficShapersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1)
)
miboc3AtmNetworkProfile_LineConfig_TrafficShapersEntry.setIndexNames(
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o"),
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfile_LineConfig_TrafficShapersEntry.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 1),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 2),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 3),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 4),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 5),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 6),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 7),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 8),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize.setStatus("mandatory")


class _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type(Integer32):
    """Custom type oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate based on Integer32"""
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


_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type.__name__ = "Integer32"
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 9),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority = _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 3, 1, 10),
    _Oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Type()
)
oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority.setStatus("mandatory")
_Miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable_Object = MibTable
miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable = _Miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 4)
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable.setStatus("mandatory")
_Miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry_Object = MibTableRow
miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry = _Miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 4, 1)
)
miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry.setIndexNames(
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o"),
    (0, "ASCEND-MIBOC3ATMNET-MIB", "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o"),
)
if mibBuilder.loadTexts:
    miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o = _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 4, 1, 1),
    _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Type()
)
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o = _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 4, 1, 2),
    _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Type()
)
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o = _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 4, 1, 3),
    _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Type()
)
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o = _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 4, 1, 4),
    _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Type()
)
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o.setStatus("mandatory")
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Type = Integer32
_Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Object = MibScalar
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi = _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 11, 4, 1, 5),
    _Oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Type()
)
oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBOC3ATMNET-MIB",
    **{"DisplayString": DisplayString,
       "miboc3AtmNetworkProfile": miboc3AtmNetworkProfile,
       "miboc3AtmNetworkProfileTable": miboc3AtmNetworkProfileTable,
       "miboc3AtmNetworkProfileEntry": miboc3AtmNetworkProfileEntry,
       "oc3AtmNetworkProfile-Shelf-o": oc3AtmNetworkProfile_Shelf_o,
       "oc3AtmNetworkProfile-Slot-o": oc3AtmNetworkProfile_Slot_o,
       "oc3AtmNetworkProfile-Item-o": oc3AtmNetworkProfile_Item_o,
       "oc3AtmNetworkProfile-Name": oc3AtmNetworkProfile_Name,
       "oc3AtmNetworkProfile-PhysicalAddress-Shelf": oc3AtmNetworkProfile_PhysicalAddress_Shelf,
       "oc3AtmNetworkProfile-PhysicalAddress-Slot": oc3AtmNetworkProfile_PhysicalAddress_Slot,
       "oc3AtmNetworkProfile-PhysicalAddress-ItemNumber": oc3AtmNetworkProfile_PhysicalAddress_ItemNumber,
       "oc3AtmNetworkProfile-Enabled": oc3AtmNetworkProfile_Enabled,
       "oc3AtmNetworkProfile-SparePhysicalAddress-Shelf": oc3AtmNetworkProfile_SparePhysicalAddress_Shelf,
       "oc3AtmNetworkProfile-SparePhysicalAddress-Slot": oc3AtmNetworkProfile_SparePhysicalAddress_Slot,
       "oc3AtmNetworkProfile-SparePhysicalAddress-ItemNumber": oc3AtmNetworkProfile_SparePhysicalAddress_ItemNumber,
       "oc3AtmNetworkProfile-SparingMode": oc3AtmNetworkProfile_SparingMode,
       "oc3AtmNetworkProfile-ProfileNumber": oc3AtmNetworkProfile_ProfileNumber,
       "oc3AtmNetworkProfile-LineConfig-TrunkGroup": oc3AtmNetworkProfile_LineConfig_TrunkGroup,
       "oc3AtmNetworkProfile-LineConfig-NailedGroup": oc3AtmNetworkProfile_LineConfig_NailedGroup,
       "oc3AtmNetworkProfile-LineConfig-Loopback": oc3AtmNetworkProfile_LineConfig_Loopback,
       "oc3AtmNetworkProfile-LineConfig-FramerRate": oc3AtmNetworkProfile_LineConfig_FramerRate,
       "oc3AtmNetworkProfile-LineConfig-RxDescrambleDisabled": oc3AtmNetworkProfile_LineConfig_RxDescrambleDisabled,
       "oc3AtmNetworkProfile-LineConfig-TxScrambleDisabled": oc3AtmNetworkProfile_LineConfig_TxScrambleDisabled,
       "oc3AtmNetworkProfile-LineConfig-RxCellPayloadDescrambleDisabled": oc3AtmNetworkProfile_LineConfig_RxCellPayloadDescrambleDisabled,
       "oc3AtmNetworkProfile-LineConfig-TxCellPayloadScrambleDisabled": oc3AtmNetworkProfile_LineConfig_TxCellPayloadScrambleDisabled,
       "oc3AtmNetworkProfile-LineConfig-LoopTiming": oc3AtmNetworkProfile_LineConfig_LoopTiming,
       "oc3AtmNetworkProfile-LineConfig-VpiVciRange": oc3AtmNetworkProfile_LineConfig_VpiVciRange,
       "oc3AtmNetworkProfile-LineConfig-ClockSource": oc3AtmNetworkProfile_LineConfig_ClockSource,
       "oc3AtmNetworkProfile-LineConfig-ClockPriority": oc3AtmNetworkProfile_LineConfig_ClockPriority,
       "oc3AtmNetworkProfile-Action-o": oc3AtmNetworkProfile_Action_o,
       "oc3AtmNetworkProfile-LineConfig-FramerMode": oc3AtmNetworkProfile_LineConfig_FramerMode,
       "oc3AtmNetworkProfile-IgnoreLineup": oc3AtmNetworkProfile_IgnoreLineup,
       "oc3AtmNetworkProfile-ApsConfigName": oc3AtmNetworkProfile_ApsConfigName,
       "miboc3AtmNetworkProfile-LineConfig-IncomingVCCsTable": miboc3AtmNetworkProfile_LineConfig_IncomingVCCsTable,
       "miboc3AtmNetworkProfile-LineConfig-IncomingVCCsEntry": miboc3AtmNetworkProfile_LineConfig_IncomingVCCsEntry,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Enabled": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-Vpi": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-StartVci": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci,
       "oc3AtmNetworkProfile-LineConfig-IncomingVCCs-EndVci": oc3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci,
       "miboc3AtmNetworkProfile-LineConfig-TrafficShapersTable": miboc3AtmNetworkProfile_LineConfig_TrafficShapersTable,
       "miboc3AtmNetworkProfile-LineConfig-TrafficShapersEntry": miboc3AtmNetworkProfile_LineConfig_TrafficShapersEntry,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o": oc3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o": oc3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o": oc3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o": oc3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Enabled": oc3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-BitRate": oc3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-PeakRate": oc3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-MaxBurstSize": oc3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Aggregate": oc3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate,
       "oc3AtmNetworkProfile-LineConfig-TrafficShapers-Priority": oc3AtmNetworkProfile_LineConfig_TrafficShapers_Priority,
       "miboc3AtmNetworkProfile-LineConfig-VcSwitchingVpiTable": miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable,
       "miboc3AtmNetworkProfile-LineConfig-VcSwitchingVpiEntry": miboc3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry,
       "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o": oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o,
       "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o": oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o,
       "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o": oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o,
       "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o": oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o,
       "oc3AtmNetworkProfile-LineConfig-VcSwitchingVpi": oc3AtmNetworkProfile_LineConfig_VcSwitchingVpi}
)
