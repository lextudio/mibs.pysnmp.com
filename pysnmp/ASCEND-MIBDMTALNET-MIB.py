# SNMP MIB module (ASCEND-MIBDMTALNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDMTALNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:28 2024
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

_MibdmtAlDslNetworkProfile_ObjectIdentity = ObjectIdentity
mibdmtAlDslNetworkProfile = _MibdmtAlDslNetworkProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 10)
)
_MibdmtAlDslNetworkProfileTable_Object = MibTable
mibdmtAlDslNetworkProfileTable = _MibdmtAlDslNetworkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1)
)
if mibBuilder.loadTexts:
    mibdmtAlDslNetworkProfileTable.setStatus("mandatory")
_MibdmtAlDslNetworkProfileEntry_Object = MibTableRow
mibdmtAlDslNetworkProfileEntry = _MibdmtAlDslNetworkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1)
)
mibdmtAlDslNetworkProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDMTALNET-MIB", "dmtAlDslNetworkProfile-Shelf-o"),
    (0, "ASCEND-MIBDMTALNET-MIB", "dmtAlDslNetworkProfile-Slot-o"),
    (0, "ASCEND-MIBDMTALNET-MIB", "dmtAlDslNetworkProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibdmtAlDslNetworkProfileEntry.setStatus("mandatory")
_DmtAlDslNetworkProfile_Shelf_o_Type = Integer32
_DmtAlDslNetworkProfile_Shelf_o_Object = MibScalar
dmtAlDslNetworkProfile_Shelf_o = _DmtAlDslNetworkProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 1),
    _DmtAlDslNetworkProfile_Shelf_o_Type()
)
dmtAlDslNetworkProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_Shelf_o.setStatus("mandatory")
_DmtAlDslNetworkProfile_Slot_o_Type = Integer32
_DmtAlDslNetworkProfile_Slot_o_Object = MibScalar
dmtAlDslNetworkProfile_Slot_o = _DmtAlDslNetworkProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 2),
    _DmtAlDslNetworkProfile_Slot_o_Type()
)
dmtAlDslNetworkProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_Slot_o.setStatus("mandatory")
_DmtAlDslNetworkProfile_Item_o_Type = Integer32
_DmtAlDslNetworkProfile_Item_o_Object = MibScalar
dmtAlDslNetworkProfile_Item_o = _DmtAlDslNetworkProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 3),
    _DmtAlDslNetworkProfile_Item_o_Type()
)
dmtAlDslNetworkProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_Item_o.setStatus("mandatory")
_DmtAlDslNetworkProfile_Name_Type = DisplayString
_DmtAlDslNetworkProfile_Name_Object = MibScalar
dmtAlDslNetworkProfile_Name = _DmtAlDslNetworkProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 4),
    _DmtAlDslNetworkProfile_Name_Type()
)
dmtAlDslNetworkProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_Name.setStatus("mandatory")


class _DmtAlDslNetworkProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_PhysicalAddress_Shelf based on Integer32"""
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


_DmtAlDslNetworkProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_PhysicalAddress_Shelf_Object = MibScalar
dmtAlDslNetworkProfile_PhysicalAddress_Shelf = _DmtAlDslNetworkProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 5),
    _DmtAlDslNetworkProfile_PhysicalAddress_Shelf_Type()
)
dmtAlDslNetworkProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _DmtAlDslNetworkProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_PhysicalAddress_Slot based on Integer32"""
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


_DmtAlDslNetworkProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_PhysicalAddress_Slot_Object = MibScalar
dmtAlDslNetworkProfile_PhysicalAddress_Slot = _DmtAlDslNetworkProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 6),
    _DmtAlDslNetworkProfile_PhysicalAddress_Slot_Type()
)
dmtAlDslNetworkProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_PhysicalAddress_Slot.setStatus("mandatory")
_DmtAlDslNetworkProfile_PhysicalAddress_ItemNumber_Type = Integer32
_DmtAlDslNetworkProfile_PhysicalAddress_ItemNumber_Object = MibScalar
dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber = _DmtAlDslNetworkProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 7),
    _DmtAlDslNetworkProfile_PhysicalAddress_ItemNumber_Type()
)
dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _DmtAlDslNetworkProfile_Enabled_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_Enabled based on Integer32"""
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


_DmtAlDslNetworkProfile_Enabled_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_Enabled_Object = MibScalar
dmtAlDslNetworkProfile_Enabled = _DmtAlDslNetworkProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 8),
    _DmtAlDslNetworkProfile_Enabled_Type()
)
dmtAlDslNetworkProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_Enabled.setStatus("mandatory")
_DmtAlDslNetworkProfile_ProfileNumber_Type = Integer32
_DmtAlDslNetworkProfile_ProfileNumber_Object = MibScalar
dmtAlDslNetworkProfile_ProfileNumber = _DmtAlDslNetworkProfile_ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 9),
    _DmtAlDslNetworkProfile_ProfileNumber_Type()
)
dmtAlDslNetworkProfile_ProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_ProfileNumber.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_NailedGroup_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_NailedGroup_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_NailedGroup = _DmtAlDslNetworkProfile_LineConfig_NailedGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 11),
    _DmtAlDslNetworkProfile_LineConfig_NailedGroup_Type()
)
dmtAlDslNetworkProfile_LineConfig_NailedGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_NailedGroup.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automaticAtStartup", 2),
          ("dynamic", 3),
          ("operator", 1))
    )


_DmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp = _DmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 19),
    _DmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp_Type()
)
dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automaticAtStartup", 2),
          ("dynamic", 3),
          ("operator", 1))
    )


_DmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown = _DmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 20),
    _DmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown_Type()
)
dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp = _DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 21),
    _DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp_Type()
)
dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown = _DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 22),
    _DmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown_Type()
)
dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity = _DmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 25),
    _DmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity_Type()
)
dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity.setStatus("mandatory")
_DmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp_Type = Integer32
_DmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp_Object = MibScalar
dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp = _DmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 26),
    _DmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp_Type()
)
dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown_Type = Integer32
_DmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown_Object = MibScalar
dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown = _DmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 27),
    _DmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown_Type()
)
dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp_Type = Integer32
_DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp_Object = MibScalar
dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp = _DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 28),
    _DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp_Type()
)
dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown_Type = Integer32
_DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown_Object = MibScalar
dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown = _DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 29),
    _DmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown_Type()
)
dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp_Type = Integer32
_DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp_Object = MibScalar
dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp = _DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 30),
    _DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp_Type()
)
dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown_Type = Integer32
_DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown_Object = MibScalar
dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown = _DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 31),
    _DmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown_Type()
)
dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp = _DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 32),
    _DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown = _DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 33),
    _DmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp = _DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 34),
    _DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown = _DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 35),
    _DmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp = _DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 36),
    _DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown = _DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 37),
    _DmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp = _DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 38),
    _DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown_Type = Integer32
_DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown_Object = MibScalar
dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown = _DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 39),
    _DmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown_Type()
)
dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp = _DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 40),
    _DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp_Type()
)
dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown = _DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 41),
    _DmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown_Type()
)
dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp = _DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 42),
    _DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp_Type()
)
dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown = _DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 43),
    _DmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown_Type()
)
dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp = _DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 44),
    _DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp_Type()
)
dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown = _DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 45),
    _DmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown_Type()
)
dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp = _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 46),
    _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp = _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 47),
    _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown = _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 48),
    _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown = _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 49),
    _DmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp = _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 50),
    _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp = _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 51),
    _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown = _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 52),
    _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown.setStatus("mandatory")
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown_Type = Integer32
_DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown_Object = MibScalar
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown = _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 53),
    _DmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown_Type()
)
dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown.setStatus("mandatory")


class _DmtAlDslNetworkProfile_Action_o_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_Action_o based on Integer32"""
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


_DmtAlDslNetworkProfile_Action_o_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_Action_o_Object = MibScalar
dmtAlDslNetworkProfile_Action_o = _DmtAlDslNetworkProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 54),
    _DmtAlDslNetworkProfile_Action_o_Type()
)
dmtAlDslNetworkProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_Action_o.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi = _DmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 55),
    _DmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi_Type()
)
dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp = _DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 56),
    _DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp_Type()
)
dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown = _DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 57),
    _DmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown_Type()
)
dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_LineCode_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ansiDmt", 4),
          ("autoSelect", 3),
          ("etsiAnnexB", 7),
          ("gDmt", 5),
          ("gLite", 2),
          ("legacyMode", 6))
    )


_DmtAlDslNetworkProfile_LineConfig_LineCode_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_LineCode_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_LineCode = _DmtAlDslNetworkProfile_LineConfig_LineCode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 58),
    _DmtAlDslNetworkProfile_LineConfig_LineCode_Type()
)
dmtAlDslNetworkProfile_LineConfig_LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_LineCode.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_LineLatencyDown_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_LineLatencyDown based on Integer32"""
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
        *(("both", 4),
          ("fast", 2),
          ("interleave", 3),
          ("none", 1))
    )


_DmtAlDslNetworkProfile_LineConfig_LineLatencyDown_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_LineLatencyDown_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_LineLatencyDown = _DmtAlDslNetworkProfile_LineConfig_LineLatencyDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 59),
    _DmtAlDslNetworkProfile_LineConfig_LineLatencyDown_Type()
)
dmtAlDslNetworkProfile_LineConfig_LineLatencyDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_LineLatencyDown.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_LineLatencyUp_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_LineLatencyUp based on Integer32"""
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
        *(("both", 4),
          ("fast", 2),
          ("interleave", 3),
          ("none", 1))
    )


_DmtAlDslNetworkProfile_LineConfig_LineLatencyUp_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_LineLatencyUp_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_LineLatencyUp = _DmtAlDslNetworkProfile_LineConfig_LineLatencyUp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 60),
    _DmtAlDslNetworkProfile_LineConfig_LineLatencyUp_Type()
)
dmtAlDslNetworkProfile_LineConfig_LineLatencyUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_LineLatencyUp.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_TrellisEncoding_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_TrellisEncoding based on Integer32"""
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


_DmtAlDslNetworkProfile_LineConfig_TrellisEncoding_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_TrellisEncoding_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_TrellisEncoding = _DmtAlDslNetworkProfile_LineConfig_TrellisEncoding_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 61),
    _DmtAlDslNetworkProfile_LineConfig_TrellisEncoding_Type()
)
dmtAlDslNetworkProfile_LineConfig_TrellisEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_TrellisEncoding.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_GainDefault_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_GainDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-16Db", 1),
          ("n-20Db", 2))
    )


_DmtAlDslNetworkProfile_LineConfig_GainDefault_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_GainDefault_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_GainDefault = _DmtAlDslNetworkProfile_LineConfig_GainDefault_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 62),
    _DmtAlDslNetworkProfile_LineConfig_GainDefault_Type()
)
dmtAlDslNetworkProfile_LineConfig_GainDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_GainDefault.setStatus("mandatory")


class _DmtAlDslNetworkProfile_SparingMode_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_SparingMode based on Integer32"""
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


_DmtAlDslNetworkProfile_SparingMode_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_SparingMode_Object = MibScalar
dmtAlDslNetworkProfile_SparingMode = _DmtAlDslNetworkProfile_SparingMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 63),
    _DmtAlDslNetworkProfile_SparingMode_Type()
)
dmtAlDslNetworkProfile_SparingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_SparingMode.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_UpstreamStartBin_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_UpstreamStartBin_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin = _DmtAlDslNetworkProfile_LineConfig_UpstreamStartBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 64),
    _DmtAlDslNetworkProfile_LineConfig_UpstreamStartBin_Type()
)
dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_UpstreamEndBin_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_UpstreamEndBin_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin = _DmtAlDslNetworkProfile_LineConfig_UpstreamEndBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 65),
    _DmtAlDslNetworkProfile_LineConfig_UpstreamEndBin_Type()
)
dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_DownstreamStartBin_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_DownstreamStartBin_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin = _DmtAlDslNetworkProfile_LineConfig_DownstreamStartBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 66),
    _DmtAlDslNetworkProfile_LineConfig_DownstreamStartBin_Type()
)
dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin.setStatus("mandatory")
_DmtAlDslNetworkProfile_LineConfig_DownstreamEndBin_Type = Integer32
_DmtAlDslNetworkProfile_LineConfig_DownstreamEndBin_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin = _DmtAlDslNetworkProfile_LineConfig_DownstreamEndBin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 67),
    _DmtAlDslNetworkProfile_LineConfig_DownstreamEndBin_Type()
)
dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_LoopBack_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_LoopBack based on Integer32"""
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


_DmtAlDslNetworkProfile_LineConfig_LoopBack_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_LoopBack_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_LoopBack = _DmtAlDslNetworkProfile_LineConfig_LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 69),
    _DmtAlDslNetworkProfile_LineConfig_LoopBack_Type()
)
dmtAlDslNetworkProfile_LineConfig_LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_LoopBack.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_BitSwapping_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_BitSwapping based on Integer32"""
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


_DmtAlDslNetworkProfile_LineConfig_BitSwapping_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_BitSwapping_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_BitSwapping = _DmtAlDslNetworkProfile_LineConfig_BitSwapping_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 70),
    _DmtAlDslNetworkProfile_LineConfig_BitSwapping_Type()
)
dmtAlDslNetworkProfile_LineConfig_BitSwapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_BitSwapping.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_FbmDbmMode_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_FbmDbmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dbm", 2),
          ("fbm", 1))
    )


_DmtAlDslNetworkProfile_LineConfig_FbmDbmMode_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_FbmDbmMode_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_FbmDbmMode = _DmtAlDslNetworkProfile_LineConfig_FbmDbmMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 71),
    _DmtAlDslNetworkProfile_LineConfig_FbmDbmMode_Type()
)
dmtAlDslNetworkProfile_LineConfig_FbmDbmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_FbmDbmMode.setStatus("mandatory")
_DmtAlDslNetworkProfile_ThreshProfile_Type = DisplayString
_DmtAlDslNetworkProfile_ThreshProfile_Object = MibScalar
dmtAlDslNetworkProfile_ThreshProfile = _DmtAlDslNetworkProfile_ThreshProfile_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 72),
    _DmtAlDslNetworkProfile_ThreshProfile_Type()
)
dmtAlDslNetworkProfile_ThreshProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_ThreshProfile.setStatus("mandatory")


class _DmtAlDslNetworkProfile_IgnoreLineup_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_IgnoreLineup based on Integer32"""
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


_DmtAlDslNetworkProfile_IgnoreLineup_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_IgnoreLineup_Object = MibScalar
dmtAlDslNetworkProfile_IgnoreLineup = _DmtAlDslNetworkProfile_IgnoreLineup_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 73),
    _DmtAlDslNetworkProfile_IgnoreLineup_Type()
)
dmtAlDslNetworkProfile_IgnoreLineup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_IgnoreLineup.setStatus("mandatory")


class _DmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost_Type(Integer32):
    """Custom type dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("old", 2),
          ("unknown", 3))
    )


_DmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost_Type.__name__ = "Integer32"
_DmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost_Object = MibScalar
dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost = _DmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 10, 1, 1, 74),
    _DmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost_Type()
)
dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDMTALNET-MIB",
    **{"DisplayString": DisplayString,
       "mibdmtAlDslNetworkProfile": mibdmtAlDslNetworkProfile,
       "mibdmtAlDslNetworkProfileTable": mibdmtAlDslNetworkProfileTable,
       "mibdmtAlDslNetworkProfileEntry": mibdmtAlDslNetworkProfileEntry,
       "dmtAlDslNetworkProfile-Shelf-o": dmtAlDslNetworkProfile_Shelf_o,
       "dmtAlDslNetworkProfile-Slot-o": dmtAlDslNetworkProfile_Slot_o,
       "dmtAlDslNetworkProfile-Item-o": dmtAlDslNetworkProfile_Item_o,
       "dmtAlDslNetworkProfile-Name": dmtAlDslNetworkProfile_Name,
       "dmtAlDslNetworkProfile-PhysicalAddress-Shelf": dmtAlDslNetworkProfile_PhysicalAddress_Shelf,
       "dmtAlDslNetworkProfile-PhysicalAddress-Slot": dmtAlDslNetworkProfile_PhysicalAddress_Slot,
       "dmtAlDslNetworkProfile-PhysicalAddress-ItemNumber": dmtAlDslNetworkProfile_PhysicalAddress_ItemNumber,
       "dmtAlDslNetworkProfile-Enabled": dmtAlDslNetworkProfile_Enabled,
       "dmtAlDslNetworkProfile-ProfileNumber": dmtAlDslNetworkProfile_ProfileNumber,
       "dmtAlDslNetworkProfile-LineConfig-NailedGroup": dmtAlDslNetworkProfile_LineConfig_NailedGroup,
       "dmtAlDslNetworkProfile-LineConfig-RateAdaptModeUp": dmtAlDslNetworkProfile_LineConfig_RateAdaptModeUp,
       "dmtAlDslNetworkProfile-LineConfig-RateAdaptModeDown": dmtAlDslNetworkProfile_LineConfig_RateAdaptModeDown,
       "dmtAlDslNetworkProfile-LineConfig-RateAdaptRatioUp": dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioUp,
       "dmtAlDslNetworkProfile-LineConfig-RateAdaptRatioDown": dmtAlDslNetworkProfile_LineConfig_RateAdaptRatioDown,
       "dmtAlDslNetworkProfile-LineConfig-MaxPowerSpectralDensity": dmtAlDslNetworkProfile_LineConfig_MaxPowerSpectralDensity,
       "dmtAlDslNetworkProfile-FastPathConfig-MinBitrateUp": dmtAlDslNetworkProfile_FastPathConfig_MinBitrateUp,
       "dmtAlDslNetworkProfile-FastPathConfig-MinBitrateDown": dmtAlDslNetworkProfile_FastPathConfig_MinBitrateDown,
       "dmtAlDslNetworkProfile-FastPathConfig-MaxBitrateUp": dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateUp,
       "dmtAlDslNetworkProfile-FastPathConfig-MaxBitrateDown": dmtAlDslNetworkProfile_FastPathConfig_MaxBitrateDown,
       "dmtAlDslNetworkProfile-FastPathConfig-PlannedBitrateUp": dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateUp,
       "dmtAlDslNetworkProfile-FastPathConfig-PlannedBitrateDown": dmtAlDslNetworkProfile_FastPathConfig_PlannedBitrateDown,
       "dmtAlDslNetworkProfile-InterleavePathConfig-MinBitrateUp": dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateUp,
       "dmtAlDslNetworkProfile-InterleavePathConfig-MinBitrateDown": dmtAlDslNetworkProfile_InterleavePathConfig_MinBitrateDown,
       "dmtAlDslNetworkProfile-InterleavePathConfig-MaxBitrateUp": dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateUp,
       "dmtAlDslNetworkProfile-InterleavePathConfig-MaxBitrateDown": dmtAlDslNetworkProfile_InterleavePathConfig_MaxBitrateDown,
       "dmtAlDslNetworkProfile-InterleavePathConfig-PlannedBitrateUp": dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateUp,
       "dmtAlDslNetworkProfile-InterleavePathConfig-PlannedBitrateDown": dmtAlDslNetworkProfile_InterleavePathConfig_PlannedBitrateDown,
       "dmtAlDslNetworkProfile-InterleavePathConfig-MaxDelayUp": dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayUp,
       "dmtAlDslNetworkProfile-InterleavePathConfig-MaxDelayDown": dmtAlDslNetworkProfile_InterleavePathConfig_MaxDelayDown,
       "dmtAlDslNetworkProfile-MarginConfig-TargetNoiseMarginUp": dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginUp,
       "dmtAlDslNetworkProfile-MarginConfig-TargetNoiseMarginDown": dmtAlDslNetworkProfile_MarginConfig_TargetNoiseMarginDown,
       "dmtAlDslNetworkProfile-MarginConfig-MinNoiseMarginUp": dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginUp,
       "dmtAlDslNetworkProfile-MarginConfig-MinNoiseMarginDown": dmtAlDslNetworkProfile_MarginConfig_MinNoiseMarginDown,
       "dmtAlDslNetworkProfile-MarginConfig-MaxAddNoiseMarginUp": dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginUp,
       "dmtAlDslNetworkProfile-MarginConfig-MaxAddNoiseMarginDown": dmtAlDslNetworkProfile_MarginConfig_MaxAddNoiseMarginDown,
       "dmtAlDslNetworkProfile-MarginConfig-RaDownshiftMarginUp": dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginUp,
       "dmtAlDslNetworkProfile-MarginConfig-RaDownshiftIntUp": dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntUp,
       "dmtAlDslNetworkProfile-MarginConfig-RaDownshiftMarginDown": dmtAlDslNetworkProfile_MarginConfig_RaDownshiftMarginDown,
       "dmtAlDslNetworkProfile-MarginConfig-RaDownshiftIntDown": dmtAlDslNetworkProfile_MarginConfig_RaDownshiftIntDown,
       "dmtAlDslNetworkProfile-MarginConfig-RaUpshiftMarginUp": dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginUp,
       "dmtAlDslNetworkProfile-MarginConfig-RaUpshiftIntUp": dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntUp,
       "dmtAlDslNetworkProfile-MarginConfig-RaUpshiftMarginDown": dmtAlDslNetworkProfile_MarginConfig_RaUpshiftMarginDown,
       "dmtAlDslNetworkProfile-MarginConfig-RaUpshiftIntDown": dmtAlDslNetworkProfile_MarginConfig_RaUpshiftIntDown,
       "dmtAlDslNetworkProfile-Action-o": dmtAlDslNetworkProfile_Action_o,
       "dmtAlDslNetworkProfile-LineConfig-VpSwitchingVpi": dmtAlDslNetworkProfile_LineConfig_VpSwitchingVpi,
       "dmtAlDslNetworkProfile-LineConfig-MaxAggrPowerLevelUp": dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelUp,
       "dmtAlDslNetworkProfile-LineConfig-MaxAggrPowerLevelDown": dmtAlDslNetworkProfile_LineConfig_MaxAggrPowerLevelDown,
       "dmtAlDslNetworkProfile-LineConfig-LineCode": dmtAlDslNetworkProfile_LineConfig_LineCode,
       "dmtAlDslNetworkProfile-LineConfig-LineLatencyDown": dmtAlDslNetworkProfile_LineConfig_LineLatencyDown,
       "dmtAlDslNetworkProfile-LineConfig-LineLatencyUp": dmtAlDslNetworkProfile_LineConfig_LineLatencyUp,
       "dmtAlDslNetworkProfile-LineConfig-TrellisEncoding": dmtAlDslNetworkProfile_LineConfig_TrellisEncoding,
       "dmtAlDslNetworkProfile-LineConfig-GainDefault": dmtAlDslNetworkProfile_LineConfig_GainDefault,
       "dmtAlDslNetworkProfile-SparingMode": dmtAlDslNetworkProfile_SparingMode,
       "dmtAlDslNetworkProfile-LineConfig-UpstreamStartBin": dmtAlDslNetworkProfile_LineConfig_UpstreamStartBin,
       "dmtAlDslNetworkProfile-LineConfig-UpstreamEndBin": dmtAlDslNetworkProfile_LineConfig_UpstreamEndBin,
       "dmtAlDslNetworkProfile-LineConfig-DownstreamStartBin": dmtAlDslNetworkProfile_LineConfig_DownstreamStartBin,
       "dmtAlDslNetworkProfile-LineConfig-DownstreamEndBin": dmtAlDslNetworkProfile_LineConfig_DownstreamEndBin,
       "dmtAlDslNetworkProfile-LineConfig-LoopBack": dmtAlDslNetworkProfile_LineConfig_LoopBack,
       "dmtAlDslNetworkProfile-LineConfig-BitSwapping": dmtAlDslNetworkProfile_LineConfig_BitSwapping,
       "dmtAlDslNetworkProfile-LineConfig-FbmDbmMode": dmtAlDslNetworkProfile_LineConfig_FbmDbmMode,
       "dmtAlDslNetworkProfile-ThreshProfile": dmtAlDslNetworkProfile_ThreshProfile,
       "dmtAlDslNetworkProfile-IgnoreLineup": dmtAlDslNetworkProfile_IgnoreLineup,
       "dmtAlDslNetworkProfile-LineConfig-AlcatelUs413Boost": dmtAlDslNetworkProfile_LineConfig_AlcatelUs413Boost}
)
