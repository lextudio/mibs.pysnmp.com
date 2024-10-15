# SNMP MIB module (ASCEND-MIBVDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBVDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:32 2024
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

_MibvdslLineStatus_ObjectIdentity = ObjectIdentity
mibvdslLineStatus = _MibvdslLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 161)
)
_MibvdslLineStatusTable_Object = MibTable
mibvdslLineStatusTable = _MibvdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1)
)
if mibBuilder.loadTexts:
    mibvdslLineStatusTable.setStatus("mandatory")
_MibvdslLineStatusEntry_Object = MibTableRow
mibvdslLineStatusEntry = _MibvdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1)
)
mibvdslLineStatusEntry.setIndexNames(
    (0, "ASCEND-MIBVDSL-MIB", "vdslLineStatus-Shelf-o"),
    (0, "ASCEND-MIBVDSL-MIB", "vdslLineStatus-Slot-o"),
    (0, "ASCEND-MIBVDSL-MIB", "vdslLineStatus-Item-o"),
)
if mibBuilder.loadTexts:
    mibvdslLineStatusEntry.setStatus("mandatory")
_VdslLineStatus_Shelf_o_Type = Integer32
_VdslLineStatus_Shelf_o_Object = MibScalar
vdslLineStatus_Shelf_o = _VdslLineStatus_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 1),
    _VdslLineStatus_Shelf_o_Type()
)
vdslLineStatus_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_Shelf_o.setStatus("mandatory")
_VdslLineStatus_Slot_o_Type = Integer32
_VdslLineStatus_Slot_o_Object = MibScalar
vdslLineStatus_Slot_o = _VdslLineStatus_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 2),
    _VdslLineStatus_Slot_o_Type()
)
vdslLineStatus_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_Slot_o.setStatus("mandatory")
_VdslLineStatus_Item_o_Type = Integer32
_VdslLineStatus_Item_o_Object = MibScalar
vdslLineStatus_Item_o = _VdslLineStatus_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 3),
    _VdslLineStatus_Item_o_Type()
)
vdslLineStatus_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_Item_o.setStatus("mandatory")


class _VdslLineStatus_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type vdslLineStatus_PhysicalAddress_Shelf based on Integer32"""
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


_VdslLineStatus_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_VdslLineStatus_PhysicalAddress_Shelf_Object = MibScalar
vdslLineStatus_PhysicalAddress_Shelf = _VdslLineStatus_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 4),
    _VdslLineStatus_PhysicalAddress_Shelf_Type()
)
vdslLineStatus_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalAddress_Shelf.setStatus("mandatory")


class _VdslLineStatus_PhysicalAddress_Slot_Type(Integer32):
    """Custom type vdslLineStatus_PhysicalAddress_Slot based on Integer32"""
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


_VdslLineStatus_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_VdslLineStatus_PhysicalAddress_Slot_Object = MibScalar
vdslLineStatus_PhysicalAddress_Slot = _VdslLineStatus_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 5),
    _VdslLineStatus_PhysicalAddress_Slot_Type()
)
vdslLineStatus_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalAddress_Slot.setStatus("mandatory")
_VdslLineStatus_PhysicalAddress_ItemNumber_Type = Integer32
_VdslLineStatus_PhysicalAddress_ItemNumber_Object = MibScalar
vdslLineStatus_PhysicalAddress_ItemNumber = _VdslLineStatus_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 6),
    _VdslLineStatus_PhysicalAddress_ItemNumber_Type()
)
vdslLineStatus_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _VdslLineStatus_LineState_Type(Integer32):
    """Custom type vdslLineStatus_LineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("disabled", 2),
          ("doesNotExist", 1))
    )


_VdslLineStatus_LineState_Type.__name__ = "Integer32"
_VdslLineStatus_LineState_Object = MibScalar
vdslLineStatus_LineState = _VdslLineStatus_LineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 7),
    _VdslLineStatus_LineState_Type()
)
vdslLineStatus_LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_LineState.setStatus("mandatory")


class _VdslLineStatus_SparePhysicalAddress_Shelf_Type(Integer32):
    """Custom type vdslLineStatus_SparePhysicalAddress_Shelf based on Integer32"""
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


_VdslLineStatus_SparePhysicalAddress_Shelf_Type.__name__ = "Integer32"
_VdslLineStatus_SparePhysicalAddress_Shelf_Object = MibScalar
vdslLineStatus_SparePhysicalAddress_Shelf = _VdslLineStatus_SparePhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 8),
    _VdslLineStatus_SparePhysicalAddress_Shelf_Type()
)
vdslLineStatus_SparePhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineStatus_SparePhysicalAddress_Shelf.setStatus("mandatory")


class _VdslLineStatus_SparePhysicalAddress_Slot_Type(Integer32):
    """Custom type vdslLineStatus_SparePhysicalAddress_Slot based on Integer32"""
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


_VdslLineStatus_SparePhysicalAddress_Slot_Type.__name__ = "Integer32"
_VdslLineStatus_SparePhysicalAddress_Slot_Object = MibScalar
vdslLineStatus_SparePhysicalAddress_Slot = _VdslLineStatus_SparePhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 9),
    _VdslLineStatus_SparePhysicalAddress_Slot_Type()
)
vdslLineStatus_SparePhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineStatus_SparePhysicalAddress_Slot.setStatus("mandatory")
_VdslLineStatus_SparePhysicalAddress_ItemNumber_Type = Integer32
_VdslLineStatus_SparePhysicalAddress_ItemNumber_Object = MibScalar
vdslLineStatus_SparePhysicalAddress_ItemNumber = _VdslLineStatus_SparePhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 10),
    _VdslLineStatus_SparePhysicalAddress_ItemNumber_Type()
)
vdslLineStatus_SparePhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineStatus_SparePhysicalAddress_ItemNumber.setStatus("mandatory")


class _VdslLineStatus_SparingState_Type(Integer32):
    """Custom type vdslLineStatus_SparingState based on Integer32"""
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
        *(("primaryActive", 2),
          ("primaryInactive", 3),
          ("secondaryActive", 4),
          ("secondaryInactive", 5),
          ("sparingNone", 1))
    )


_VdslLineStatus_SparingState_Type.__name__ = "Integer32"
_VdslLineStatus_SparingState_Object = MibScalar
vdslLineStatus_SparingState = _VdslLineStatus_SparingState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 11),
    _VdslLineStatus_SparingState_Type()
)
vdslLineStatus_SparingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_SparingState.setStatus("mandatory")


class _VdslLineStatus_SparingChangeReason_Type(Integer32):
    """Custom type vdslLineStatus_SparingChangeReason based on Integer32"""
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
        *(("automatic", 3),
          ("manual", 2),
          ("test", 4),
          ("unknown", 1))
    )


_VdslLineStatus_SparingChangeReason_Type.__name__ = "Integer32"
_VdslLineStatus_SparingChangeReason_Object = MibScalar
vdslLineStatus_SparingChangeReason = _VdslLineStatus_SparingChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 12),
    _VdslLineStatus_SparingChangeReason_Type()
)
vdslLineStatus_SparingChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_SparingChangeReason.setStatus("mandatory")
_VdslLineStatus_SparingChangeTime_Type = Integer32
_VdslLineStatus_SparingChangeTime_Object = MibScalar
vdslLineStatus_SparingChangeTime = _VdslLineStatus_SparingChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 13),
    _VdslLineStatus_SparingChangeTime_Type()
)
vdslLineStatus_SparingChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_SparingChangeTime.setStatus("mandatory")
_VdslLineStatus_SparingChangeCounter_Type = Integer32
_VdslLineStatus_SparingChangeCounter_Object = MibScalar
vdslLineStatus_SparingChangeCounter = _VdslLineStatus_SparingChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 14),
    _VdslLineStatus_SparingChangeCounter_Type()
)
vdslLineStatus_SparingChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_SparingChangeCounter.setStatus("mandatory")


class _VdslLineStatus_VpiVciRange_Type(Integer32):
    """Custom type vdslLineStatus_VpiVciRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 5),
          ("vpi015Vci32127", 3),
          ("vpi01Vci321023", 6),
          ("vpi031Vci3263", 4),
          ("vpi03Vci32511", 1),
          ("vpi07Vci32255", 2))
    )


_VdslLineStatus_VpiVciRange_Type.__name__ = "Integer32"
_VdslLineStatus_VpiVciRange_Object = MibScalar
vdslLineStatus_VpiVciRange = _VdslLineStatus_VpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 15),
    _VdslLineStatus_VpiVciRange_Type()
)
vdslLineStatus_VpiVciRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_VpiVciRange.setStatus("mandatory")
_VdslLineStatus_VpSwitchingVpi_Type = Integer32
_VdslLineStatus_VpSwitchingVpi_Object = MibScalar
vdslLineStatus_VpSwitchingVpi = _VdslLineStatus_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 16),
    _VdslLineStatus_VpSwitchingVpi_Type()
)
vdslLineStatus_VpSwitchingVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_VpSwitchingVpi.setStatus("mandatory")
_VdslLineStatus_PhysicalStatus_IfGroupIndex_Type = Integer32
_VdslLineStatus_PhysicalStatus_IfGroupIndex_Object = MibScalar
vdslLineStatus_PhysicalStatus_IfGroupIndex = _VdslLineStatus_PhysicalStatus_IfGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 17),
    _VdslLineStatus_PhysicalStatus_IfGroupIndex_Type()
)
vdslLineStatus_PhysicalStatus_IfGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatus_IfGroupIndex.setStatus("mandatory")


class _VdslLineStatus_PhysicalStatus_UnitType_Type(Integer32):
    """Custom type vdslLineStatus_PhysicalStatus_UnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dslCoe", 2),
          ("dslCpe", 3))
    )


_VdslLineStatus_PhysicalStatus_UnitType_Type.__name__ = "Integer32"
_VdslLineStatus_PhysicalStatus_UnitType_Object = MibScalar
vdslLineStatus_PhysicalStatus_UnitType = _VdslLineStatus_PhysicalStatus_UnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 18),
    _VdslLineStatus_PhysicalStatus_UnitType_Type()
)
vdslLineStatus_PhysicalStatus_UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatus_UnitType.setStatus("mandatory")


class _VdslLineStatus_PhysicalStatus_DevLineState_Type(Integer32):
    """Custom type vdslLineStatus_PhysicalStatus_DevLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("dslStatDownload", 9),
          ("dslStatDwnInd", 2),
          ("dslStatFailInd", 6),
          ("dslStatInit", 4),
          ("dslStatLback", 7),
          ("dslStatNumberStates", 10),
          ("dslStatTest", 8),
          ("dslStatUpInd", 5),
          ("dslStatWaitInit", 3))
    )


_VdslLineStatus_PhysicalStatus_DevLineState_Type.__name__ = "Integer32"
_VdslLineStatus_PhysicalStatus_DevLineState_Object = MibScalar
vdslLineStatus_PhysicalStatus_DevLineState = _VdslLineStatus_PhysicalStatus_DevLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 19),
    _VdslLineStatus_PhysicalStatus_DevLineState_Type()
)
vdslLineStatus_PhysicalStatus_DevLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatus_DevLineState.setStatus("mandatory")
_VdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type = Integer32
_VdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object = MibScalar
vdslLineStatus_PhysicalStatistic_LineUpTimer_Days = _VdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 20),
    _VdslLineStatus_PhysicalStatistic_LineUpTimer_Days_Type()
)
vdslLineStatus_PhysicalStatistic_LineUpTimer_Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatistic_LineUpTimer_Days.setStatus("mandatory")
_VdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type = Integer32
_VdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object = MibScalar
vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours = _VdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 21),
    _VdslLineStatus_PhysicalStatistic_LineUpTimer_Hours_Type()
)
vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours.setStatus("mandatory")
_VdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type = Integer32
_VdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object = MibScalar
vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes = _VdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 22),
    _VdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes_Type()
)
vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes.setStatus("mandatory")


class _VdslLineStatus_PhysicalStatistic_RxSignalPresent_Type(Integer32):
    """Custom type vdslLineStatus_PhysicalStatistic_RxSignalPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_VdslLineStatus_PhysicalStatistic_RxSignalPresent_Type.__name__ = "Integer32"
_VdslLineStatus_PhysicalStatistic_RxSignalPresent_Object = MibScalar
vdslLineStatus_PhysicalStatistic_RxSignalPresent = _VdslLineStatus_PhysicalStatistic_RxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 23),
    _VdslLineStatus_PhysicalStatistic_RxSignalPresent_Type()
)
vdslLineStatus_PhysicalStatistic_RxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatistic_RxSignalPresent.setStatus("mandatory")
_VdslLineStatus_PhysicalStatistic_UpDwnCntr_Type = Integer32
_VdslLineStatus_PhysicalStatistic_UpDwnCntr_Object = MibScalar
vdslLineStatus_PhysicalStatistic_UpDwnCntr = _VdslLineStatus_PhysicalStatistic_UpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 24),
    _VdslLineStatus_PhysicalStatistic_UpDwnCntr_Type()
)
vdslLineStatus_PhysicalStatistic_UpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatistic_UpDwnCntr.setStatus("mandatory")


class _VdslLineStatus_PhysicalStatistic_SelfTest_Type(Integer32):
    """Custom type vdslLineStatus_PhysicalStatistic_SelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dslSelfTestFailed", 3),
          ("dslSelfTestNone", 2),
          ("dslSelfTestPassed", 4))
    )


_VdslLineStatus_PhysicalStatistic_SelfTest_Type.__name__ = "Integer32"
_VdslLineStatus_PhysicalStatistic_SelfTest_Object = MibScalar
vdslLineStatus_PhysicalStatistic_SelfTest = _VdslLineStatus_PhysicalStatistic_SelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 25),
    _VdslLineStatus_PhysicalStatistic_SelfTest_Type()
)
vdslLineStatus_PhysicalStatistic_SelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatistic_SelfTest.setStatus("mandatory")


class _VdslLineStatus_Action_o_Type(Integer32):
    """Custom type vdslLineStatus_Action_o based on Integer32"""
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


_VdslLineStatus_Action_o_Type.__name__ = "Integer32"
_VdslLineStatus_Action_o_Object = MibScalar
vdslLineStatus_Action_o = _VdslLineStatus_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 26),
    _VdslLineStatus_Action_o_Type()
)
vdslLineStatus_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vdslLineStatus_Action_o.setStatus("mandatory")
_VdslLineStatus_PhysicalStatus_OpUpRates_Type = Integer32
_VdslLineStatus_PhysicalStatus_OpUpRates_Object = MibScalar
vdslLineStatus_PhysicalStatus_OpUpRates = _VdslLineStatus_PhysicalStatus_OpUpRates_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 27),
    _VdslLineStatus_PhysicalStatus_OpUpRates_Type()
)
vdslLineStatus_PhysicalStatus_OpUpRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatus_OpUpRates.setStatus("mandatory")
_VdslLineStatus_PhysicalStatus_OpDownRates_Type = Integer32
_VdslLineStatus_PhysicalStatus_OpDownRates_Object = MibScalar
vdslLineStatus_PhysicalStatus_OpDownRates = _VdslLineStatus_PhysicalStatus_OpDownRates_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 28),
    _VdslLineStatus_PhysicalStatus_OpDownRates_Type()
)
vdslLineStatus_PhysicalStatus_OpDownRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatus_OpDownRates.setStatus("mandatory")
_VdslLineStatus_PhysicalStatus_FirmwareVer_Type = DisplayString
_VdslLineStatus_PhysicalStatus_FirmwareVer_Object = MibScalar
vdslLineStatus_PhysicalStatus_FirmwareVer = _VdslLineStatus_PhysicalStatus_FirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 161, 1, 1, 29),
    _VdslLineStatus_PhysicalStatus_FirmwareVer_Type()
)
vdslLineStatus_PhysicalStatus_FirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineStatus_PhysicalStatus_FirmwareVer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBVDSL-MIB",
    **{"DisplayString": DisplayString,
       "mibvdslLineStatus": mibvdslLineStatus,
       "mibvdslLineStatusTable": mibvdslLineStatusTable,
       "mibvdslLineStatusEntry": mibvdslLineStatusEntry,
       "vdslLineStatus-Shelf-o": vdslLineStatus_Shelf_o,
       "vdslLineStatus-Slot-o": vdslLineStatus_Slot_o,
       "vdslLineStatus-Item-o": vdslLineStatus_Item_o,
       "vdslLineStatus-PhysicalAddress-Shelf": vdslLineStatus_PhysicalAddress_Shelf,
       "vdslLineStatus-PhysicalAddress-Slot": vdslLineStatus_PhysicalAddress_Slot,
       "vdslLineStatus-PhysicalAddress-ItemNumber": vdslLineStatus_PhysicalAddress_ItemNumber,
       "vdslLineStatus-LineState": vdslLineStatus_LineState,
       "vdslLineStatus-SparePhysicalAddress-Shelf": vdslLineStatus_SparePhysicalAddress_Shelf,
       "vdslLineStatus-SparePhysicalAddress-Slot": vdslLineStatus_SparePhysicalAddress_Slot,
       "vdslLineStatus-SparePhysicalAddress-ItemNumber": vdslLineStatus_SparePhysicalAddress_ItemNumber,
       "vdslLineStatus-SparingState": vdslLineStatus_SparingState,
       "vdslLineStatus-SparingChangeReason": vdslLineStatus_SparingChangeReason,
       "vdslLineStatus-SparingChangeTime": vdslLineStatus_SparingChangeTime,
       "vdslLineStatus-SparingChangeCounter": vdslLineStatus_SparingChangeCounter,
       "vdslLineStatus-VpiVciRange": vdslLineStatus_VpiVciRange,
       "vdslLineStatus-VpSwitchingVpi": vdslLineStatus_VpSwitchingVpi,
       "vdslLineStatus-PhysicalStatus-IfGroupIndex": vdslLineStatus_PhysicalStatus_IfGroupIndex,
       "vdslLineStatus-PhysicalStatus-UnitType": vdslLineStatus_PhysicalStatus_UnitType,
       "vdslLineStatus-PhysicalStatus-DevLineState": vdslLineStatus_PhysicalStatus_DevLineState,
       "vdslLineStatus-PhysicalStatistic-LineUpTimer-Days": vdslLineStatus_PhysicalStatistic_LineUpTimer_Days,
       "vdslLineStatus-PhysicalStatistic-LineUpTimer-Hours": vdslLineStatus_PhysicalStatistic_LineUpTimer_Hours,
       "vdslLineStatus-PhysicalStatistic-LineUpTimer-Minutes": vdslLineStatus_PhysicalStatistic_LineUpTimer_Minutes,
       "vdslLineStatus-PhysicalStatistic-RxSignalPresent": vdslLineStatus_PhysicalStatistic_RxSignalPresent,
       "vdslLineStatus-PhysicalStatistic-UpDwnCntr": vdslLineStatus_PhysicalStatistic_UpDwnCntr,
       "vdslLineStatus-PhysicalStatistic-SelfTest": vdslLineStatus_PhysicalStatistic_SelfTest,
       "vdslLineStatus-Action-o": vdslLineStatus_Action_o,
       "vdslLineStatus-PhysicalStatus-OpUpRates": vdslLineStatus_PhysicalStatus_OpUpRates,
       "vdslLineStatus-PhysicalStatus-OpDownRates": vdslLineStatus_PhysicalStatus_OpDownRates,
       "vdslLineStatus-PhysicalStatus-FirmwareVer": vdslLineStatus_PhysicalStatus_FirmwareVer}
)
