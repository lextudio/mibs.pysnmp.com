# SNMP MIB module (ASCEND-MIBE3ATMNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBE3ATMNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:33 2024
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

_Mibe3AtmNetworkProfile_ObjectIdentity = ObjectIdentity
mibe3AtmNetworkProfile = _Mibe3AtmNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 15)
)
_Mibe3AtmNetworkProfileTable_Object = MibTable
mibe3AtmNetworkProfileTable = _Mibe3AtmNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1)
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfileTable.setStatus("mandatory")
_Mibe3AtmNetworkProfileEntry_Object = MibTableRow
mibe3AtmNetworkProfileEntry = _Mibe3AtmNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1)
)
mibe3AtmNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfileEntry.setStatus("mandatory")
_E3AtmNetworkProfile_Shelf_o_Type = Integer32
_E3AtmNetworkProfile_Shelf_o_Object = MibScalar
e3AtmNetworkProfile_Shelf_o = _E3AtmNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 1),
    _E3AtmNetworkProfile_Shelf_o_Type()
)
e3AtmNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_Shelf_o.setStatus("mandatory")
_E3AtmNetworkProfile_Slot_o_Type = Integer32
_E3AtmNetworkProfile_Slot_o_Object = MibScalar
e3AtmNetworkProfile_Slot_o = _E3AtmNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 2),
    _E3AtmNetworkProfile_Slot_o_Type()
)
e3AtmNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_Slot_o.setStatus("mandatory")
_E3AtmNetworkProfile_Item_o_Type = Integer32
_E3AtmNetworkProfile_Item_o_Object = MibScalar
e3AtmNetworkProfile_Item_o = _E3AtmNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 3),
    _E3AtmNetworkProfile_Item_o_Type()
)
e3AtmNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_Item_o.setStatus("mandatory")
_E3AtmNetworkProfile_Name_Type = DisplayString
_E3AtmNetworkProfile_Name_Object = MibScalar
e3AtmNetworkProfile_Name = _E3AtmNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 4),
    _E3AtmNetworkProfile_Name_Type()
)
e3AtmNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_Name.setStatus("mandatory")


class _E3AtmNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type e3AtmNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_E3AtmNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
e3AtmNetworkProfile_PhysicalAddress_Shelf = _E3AtmNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 5),
    _E3AtmNetworkProfile_PhysicalAddress_Shelf_Type()
)
e3AtmNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _E3AtmNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type e3AtmNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_E3AtmNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
e3AtmNetworkProfile_PhysicalAddress_Slot = _E3AtmNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 6),
    _E3AtmNetworkProfile_PhysicalAddress_Slot_Type()
)
e3AtmNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_E3AtmNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_E3AtmNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
e3AtmNetworkProfile_PhysicalAddress_ItemNumber = _E3AtmNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 7),
    _E3AtmNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
e3AtmNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _E3AtmNetworkProfile_Enabled_Type(Integer32):
    """Custom type e3AtmNetworkProfile_Enabled based on Integer32"""
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


_E3AtmNetworkProfile_Enabled_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_Enabled_Object = MibScalar
e3AtmNetworkProfile_Enabled = _E3AtmNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 8),
    _E3AtmNetworkProfile_Enabled_Type()
)
e3AtmNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_Enabled.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrunkGroup_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrunkGroup_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrunkGroup = _E3AtmNetworkProfile_LineConfig_TrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 9),
    _E3AtmNetworkProfile_LineConfig_TrunkGroup_Type()
)
e3AtmNetworkProfile_LineConfig_TrunkGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrunkGroup.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_E3AtmNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
e3AtmNetworkProfile_LineConfig_NailedGroup = _E3AtmNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 10),
    _E3AtmNetworkProfile_LineConfig_NailedGroup_Type()
)
e3AtmNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_Loopback_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("facilityLoopback", 2),
          ("localLoopback", 3),
          ("noLoopback", 1))
    )


_E3AtmNetworkProfile_LineConfig_Loopback_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_Loopback_Object = MibScalar
e3AtmNetworkProfile_LineConfig_Loopback = _E3AtmNetworkProfile_LineConfig_Loopback_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 14),
    _E3AtmNetworkProfile_LineConfig_Loopback_Type()
)
e3AtmNetworkProfile_LineConfig_Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_Loopback.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_HighTxOutput_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_HighTxOutput based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_HighTxOutput_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_HighTxOutput_Object = MibScalar
e3AtmNetworkProfile_LineConfig_HighTxOutput = _E3AtmNetworkProfile_LineConfig_HighTxOutput_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 15),
    _E3AtmNetworkProfile_LineConfig_HighTxOutput_Type()
)
e3AtmNetworkProfile_LineConfig_HighTxOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_HighTxOutput.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_FramerMode_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_FramerMode based on Integer32"""
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
        *(("g751Adm", 1),
          ("g751Plcp", 2),
          ("g832Adm", 3),
          ("g832AdmFrameLocked", 4),
          ("g832AdmLoopTimed", 5))
    )


_E3AtmNetworkProfile_LineConfig_FramerMode_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_FramerMode_Object = MibScalar
e3AtmNetworkProfile_LineConfig_FramerMode = _E3AtmNetworkProfile_LineConfig_FramerMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 16),
    _E3AtmNetworkProfile_LineConfig_FramerMode_Type()
)
e3AtmNetworkProfile_LineConfig_FramerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_FramerMode.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_VpiVciRange_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_VpiVciRange based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_VpiVciRange_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_VpiVciRange_Object = MibScalar
e3AtmNetworkProfile_LineConfig_VpiVciRange = _E3AtmNetworkProfile_LineConfig_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 17),
    _E3AtmNetworkProfile_LineConfig_VpiVciRange_Type()
)
e3AtmNetworkProfile_LineConfig_VpiVciRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_VpiVciRange.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_CellPayloadScramble_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_CellPayloadScramble based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_CellPayloadScramble_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_CellPayloadScramble_Object = MibScalar
e3AtmNetworkProfile_LineConfig_CellPayloadScramble = _E3AtmNetworkProfile_LineConfig_CellPayloadScramble_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 18),
    _E3AtmNetworkProfile_LineConfig_CellPayloadScramble_Type()
)
e3AtmNetworkProfile_LineConfig_CellPayloadScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_CellPayloadScramble.setStatus("mandatory")


class _E3AtmNetworkProfile_Action_o_Type(Integer32):
    """Custom type e3AtmNetworkProfile_Action_o based on Integer32"""
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


_E3AtmNetworkProfile_Action_o_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_Action_o_Object = MibScalar
e3AtmNetworkProfile_Action_o = _E3AtmNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 19),
    _E3AtmNetworkProfile_Action_o_Type()
)
e3AtmNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_Action_o.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_ReceiveEqualization_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_ReceiveEqualization based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_ReceiveEqualization_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_ReceiveEqualization_Object = MibScalar
e3AtmNetworkProfile_LineConfig_ReceiveEqualization = _E3AtmNetworkProfile_LineConfig_ReceiveEqualization_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 20),
    _E3AtmNetworkProfile_LineConfig_ReceiveEqualization_Type()
)
e3AtmNetworkProfile_LineConfig_ReceiveEqualization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_ReceiveEqualization.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_ClockSource_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_ClockSource based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_ClockSource_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_ClockSource_Object = MibScalar
e3AtmNetworkProfile_LineConfig_ClockSource = _E3AtmNetworkProfile_LineConfig_ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 21),
    _E3AtmNetworkProfile_LineConfig_ClockSource_Type()
)
e3AtmNetworkProfile_LineConfig_ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_ClockSource.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_ClockPriority_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_ClockPriority based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_ClockPriority_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_ClockPriority_Object = MibScalar
e3AtmNetworkProfile_LineConfig_ClockPriority = _E3AtmNetworkProfile_LineConfig_ClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 22),
    _E3AtmNetworkProfile_LineConfig_ClockPriority_Type()
)
e3AtmNetworkProfile_LineConfig_ClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_ClockPriority.setStatus("mandatory")


class _E3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type e3AtmNetworkProfile_SparePhysicalAddress_Shelf based on Integer32"""
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


_E3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_SparePhysicalAddress_Shelf_Object = MibScalar
e3AtmNetworkProfile_SparePhysicalAddress_Shelf = _E3AtmNetworkProfile_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 23),
    _E3AtmNetworkProfile_SparePhysicalAddress_Shelf_Type()
)
e3AtmNetworkProfile_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _E3AtmNetworkProfile_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type e3AtmNetworkProfile_SparePhysicalAddress_Slot based on Integer32"""
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


_E3AtmNetworkProfile_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_SparePhysicalAddress_Slot_Object = MibScalar
e3AtmNetworkProfile_SparePhysicalAddress_Slot = _E3AtmNetworkProfile_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 24),
    _E3AtmNetworkProfile_SparePhysicalAddress_Slot_Type()
)
e3AtmNetworkProfile_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_SparePhysicalAddress_Slot.setStatus("mandatory")
_E3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Type = Integer32
_E3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Object = MibScalar
e3AtmNetworkProfile_SparePhysicalAddress_ItemNumber = _E3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 25),
    _E3AtmNetworkProfile_SparePhysicalAddress_ItemNumber_Type()
)
e3AtmNetworkProfile_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _E3AtmNetworkProfile_SparingMode_Type(Integer32):
    """Custom type e3AtmNetworkProfile_SparingMode based on Integer32"""
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


_E3AtmNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_SparingMode_Object = MibScalar
e3AtmNetworkProfile_SparingMode = _E3AtmNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 26),
    _E3AtmNetworkProfile_SparingMode_Type()
)
e3AtmNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_SparingMode.setStatus("mandatory")


class _E3AtmNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type e3AtmNetworkProfile_IgnoreLineup based on Integer32"""
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


_E3AtmNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_IgnoreLineup_Object = MibScalar
e3AtmNetworkProfile_IgnoreLineup = _E3AtmNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 27),
    _E3AtmNetworkProfile_IgnoreLineup_Type()
)
e3AtmNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_IgnoreLineup.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Object = MibScalar
e3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable = _E3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 1, 1, 28),
    _E3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable_Type()
)
e3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable.setStatus("mandatory")
_Mibe3AtmNetworkProfile_LineConfig_TrafficShapersTable_Object = MibTable
mibe3AtmNetworkProfile_LineConfig_TrafficShapersTable = _Mibe3AtmNetworkProfile_LineConfig_TrafficShapersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2)
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfile_LineConfig_TrafficShapersTable.setStatus("mandatory")
_Mibe3AtmNetworkProfile_LineConfig_TrafficShapersEntry_Object = MibTableRow
mibe3AtmNetworkProfile_LineConfig_TrafficShapersEntry = _Mibe3AtmNetworkProfile_LineConfig_TrafficShapersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1)
)
mibe3AtmNetworkProfile_LineConfig_TrafficShapersEntry.setIndexNames(
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o"),
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfile_LineConfig_TrafficShapersEntry.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o = _E3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 1),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o = _E3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 2),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o = _E3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 3),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o = _E3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 4),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled = _E3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 5),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate = _E3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 6),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate = _E3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 7),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize = _E3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 8),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate = _E3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 9),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Type = Integer32
_E3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Object = MibScalar
e3AtmNetworkProfile_LineConfig_TrafficShapers_Priority = _E3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 2, 1, 10),
    _E3AtmNetworkProfile_LineConfig_TrafficShapers_Priority_Type()
)
e3AtmNetworkProfile_LineConfig_TrafficShapers_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_TrafficShapers_Priority.setStatus("mandatory")
_Mibe3AtmNetworkProfile_LineConfig_IncomingVCCsTable_Object = MibTable
mibe3AtmNetworkProfile_LineConfig_IncomingVCCsTable = _Mibe3AtmNetworkProfile_LineConfig_IncomingVCCsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3)
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfile_LineConfig_IncomingVCCsTable.setStatus("mandatory")
_Mibe3AtmNetworkProfile_LineConfig_IncomingVCCsEntry_Object = MibTableRow
mibe3AtmNetworkProfile_LineConfig_IncomingVCCsEntry = _Mibe3AtmNetworkProfile_LineConfig_IncomingVCCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1)
)
mibe3AtmNetworkProfile_LineConfig_IncomingVCCsEntry.setIndexNames(
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o"),
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfile_LineConfig_IncomingVCCsEntry.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 1),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 2),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 3),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 4),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o.setStatus("mandatory")


class _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type(Integer32):
    """Custom type e3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled based on Integer32"""
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


_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type.__name__ = "Integer32"
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 5),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Type = Integer32
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 6),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Type = Integer32
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 7),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Type = Integer32
_E3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Object = MibScalar
e3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci = _E3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 3, 1, 8),
    _E3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci_Type()
)
e3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci.setStatus("mandatory")
_Mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable_Object = MibTable
mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable = _Mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 4)
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable.setStatus("mandatory")
_Mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry_Object = MibTableRow
mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry = _Mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 4, 1)
)
mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry.setIndexNames(
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o"),
    (0, "ASCEND-MIBE3ATMNET-MIB", "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o"),
)
if mibBuilder.loadTexts:
    mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o = _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 4, 1, 1),
    _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o_Type()
)
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o = _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 4, 1, 2),
    _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o_Type()
)
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o = _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 4, 1, 3),
    _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o_Type()
)
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Type = Integer32
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Object = MibScalar
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o = _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 4, 1, 4),
    _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o_Type()
)
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o.setStatus("mandatory")
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Type = Integer32
_E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Object = MibScalar
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi = _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 15, 4, 1, 5),
    _E3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Type()
)
e3AtmNetworkProfile_LineConfig_VcSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3AtmNetworkProfile_LineConfig_VcSwitchingVpi.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBE3ATMNET-MIB",
    **{"DisplayString": DisplayString,
       "mibe3AtmNetworkProfile": mibe3AtmNetworkProfile,
       "mibe3AtmNetworkProfileTable": mibe3AtmNetworkProfileTable,
       "mibe3AtmNetworkProfileEntry": mibe3AtmNetworkProfileEntry,
       "e3AtmNetworkProfile-Shelf-o": e3AtmNetworkProfile_Shelf_o,
       "e3AtmNetworkProfile-Slot-o": e3AtmNetworkProfile_Slot_o,
       "e3AtmNetworkProfile-Item-o": e3AtmNetworkProfile_Item_o,
       "e3AtmNetworkProfile-Name": e3AtmNetworkProfile_Name,
       "e3AtmNetworkProfile-PhysicalAddress-Shelf": e3AtmNetworkProfile_PhysicalAddress_Shelf,
       "e3AtmNetworkProfile-PhysicalAddress-Slot": e3AtmNetworkProfile_PhysicalAddress_Slot,
       "e3AtmNetworkProfile-PhysicalAddress-ItemNumber": e3AtmNetworkProfile_PhysicalAddress_ItemNumber,
       "e3AtmNetworkProfile-Enabled": e3AtmNetworkProfile_Enabled,
       "e3AtmNetworkProfile-LineConfig-TrunkGroup": e3AtmNetworkProfile_LineConfig_TrunkGroup,
       "e3AtmNetworkProfile-LineConfig-NailedGroup": e3AtmNetworkProfile_LineConfig_NailedGroup,
       "e3AtmNetworkProfile-LineConfig-Loopback": e3AtmNetworkProfile_LineConfig_Loopback,
       "e3AtmNetworkProfile-LineConfig-HighTxOutput": e3AtmNetworkProfile_LineConfig_HighTxOutput,
       "e3AtmNetworkProfile-LineConfig-FramerMode": e3AtmNetworkProfile_LineConfig_FramerMode,
       "e3AtmNetworkProfile-LineConfig-VpiVciRange": e3AtmNetworkProfile_LineConfig_VpiVciRange,
       "e3AtmNetworkProfile-LineConfig-CellPayloadScramble": e3AtmNetworkProfile_LineConfig_CellPayloadScramble,
       "e3AtmNetworkProfile-Action-o": e3AtmNetworkProfile_Action_o,
       "e3AtmNetworkProfile-LineConfig-ReceiveEqualization": e3AtmNetworkProfile_LineConfig_ReceiveEqualization,
       "e3AtmNetworkProfile-LineConfig-ClockSource": e3AtmNetworkProfile_LineConfig_ClockSource,
       "e3AtmNetworkProfile-LineConfig-ClockPriority": e3AtmNetworkProfile_LineConfig_ClockPriority,
       "e3AtmNetworkProfile-SparePhysicalAddress-Shelf": e3AtmNetworkProfile_SparePhysicalAddress_Shelf,
       "e3AtmNetworkProfile-SparePhysicalAddress-Slot": e3AtmNetworkProfile_SparePhysicalAddress_Slot,
       "e3AtmNetworkProfile-SparePhysicalAddress-ItemNumber": e3AtmNetworkProfile_SparePhysicalAddress_ItemNumber,
       "e3AtmNetworkProfile-SparingMode": e3AtmNetworkProfile_SparingMode,
       "e3AtmNetworkProfile-IgnoreLineup": e3AtmNetworkProfile_IgnoreLineup,
       "e3AtmNetworkProfile-LineConfig-StatusChangeTrapEnable": e3AtmNetworkProfile_LineConfig_StatusChangeTrapEnable,
       "mibe3AtmNetworkProfile-LineConfig-TrafficShapersTable": mibe3AtmNetworkProfile_LineConfig_TrafficShapersTable,
       "mibe3AtmNetworkProfile-LineConfig-TrafficShapersEntry": mibe3AtmNetworkProfile_LineConfig_TrafficShapersEntry,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-Shelf-o": e3AtmNetworkProfile_LineConfig_TrafficShapers_Shelf_o,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-Slot-o": e3AtmNetworkProfile_LineConfig_TrafficShapers_Slot_o,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-Item-o": e3AtmNetworkProfile_LineConfig_TrafficShapers_Item_o,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-Index-o": e3AtmNetworkProfile_LineConfig_TrafficShapers_Index_o,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-Enabled": e3AtmNetworkProfile_LineConfig_TrafficShapers_Enabled,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-BitRate": e3AtmNetworkProfile_LineConfig_TrafficShapers_BitRate,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-PeakRate": e3AtmNetworkProfile_LineConfig_TrafficShapers_PeakRate,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-MaxBurstSize": e3AtmNetworkProfile_LineConfig_TrafficShapers_MaxBurstSize,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-Aggregate": e3AtmNetworkProfile_LineConfig_TrafficShapers_Aggregate,
       "e3AtmNetworkProfile-LineConfig-TrafficShapers-Priority": e3AtmNetworkProfile_LineConfig_TrafficShapers_Priority,
       "mibe3AtmNetworkProfile-LineConfig-IncomingVCCsTable": mibe3AtmNetworkProfile_LineConfig_IncomingVCCsTable,
       "mibe3AtmNetworkProfile-LineConfig-IncomingVCCsEntry": mibe3AtmNetworkProfile_LineConfig_IncomingVCCsEntry,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Shelf-o": e3AtmNetworkProfile_LineConfig_IncomingVCCs_Shelf_o,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Slot-o": e3AtmNetworkProfile_LineConfig_IncomingVCCs_Slot_o,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Item-o": e3AtmNetworkProfile_LineConfig_IncomingVCCs_Item_o,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Index-o": e3AtmNetworkProfile_LineConfig_IncomingVCCs_Index_o,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Enabled": e3AtmNetworkProfile_LineConfig_IncomingVCCs_Enabled,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-Vpi": e3AtmNetworkProfile_LineConfig_IncomingVCCs_Vpi,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-StartVci": e3AtmNetworkProfile_LineConfig_IncomingVCCs_StartVci,
       "e3AtmNetworkProfile-LineConfig-IncomingVCCs-EndVci": e3AtmNetworkProfile_LineConfig_IncomingVCCs_EndVci,
       "mibe3AtmNetworkProfile-LineConfig-VcSwitchingVpiTable": mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiTable,
       "mibe3AtmNetworkProfile-LineConfig-VcSwitchingVpiEntry": mibe3AtmNetworkProfile_LineConfig_VcSwitchingVpiEntry,
       "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Shelf-o": e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Shelf_o,
       "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Slot-o": e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Slot_o,
       "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Item-o": e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Item_o,
       "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi-Index-o": e3AtmNetworkProfile_LineConfig_VcSwitchingVpi_Index_o,
       "e3AtmNetworkProfile-LineConfig-VcSwitchingVpi": e3AtmNetworkProfile_LineConfig_VcSwitchingVpi}
)
