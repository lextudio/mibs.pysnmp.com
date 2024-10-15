# SNMP MIB module (ASCEND-MIBSWITCHCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSWITCHCONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:22 2024
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

_MibswitchConfig_ObjectIdentity = ObjectIdentity
mibswitchConfig = _MibswitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 151)
)
_MibswitchConfigTable_Object = MibTable
mibswitchConfigTable = _MibswitchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 1)
)
if mibBuilder.loadTexts:
    mibswitchConfigTable.setStatus("mandatory")
_MibswitchConfigEntry_Object = MibTableRow
mibswitchConfigEntry = _MibswitchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 1, 1)
)
mibswitchConfigEntry.setIndexNames(
    (0, "ASCEND-MIBSWITCHCONFIG-MIB", "switchConfig-SwitchName"),
)
if mibBuilder.loadTexts:
    mibswitchConfigEntry.setStatus("mandatory")
_SwitchConfig_SwitchName_Type = DisplayString
_SwitchConfig_SwitchName_Object = MibScalar
switchConfig_SwitchName = _SwitchConfig_SwitchName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 1, 1, 1),
    _SwitchConfig_SwitchName_Type()
)
switchConfig_SwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchConfig_SwitchName.setStatus("mandatory")


class _SwitchConfig_Action_o_Type(Integer32):
    """Custom type switchConfig_Action_o based on Integer32"""
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


_SwitchConfig_Action_o_Type.__name__ = "Integer32"
_SwitchConfig_Action_o_Object = MibScalar
switchConfig_Action_o = _SwitchConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 1, 1, 2),
    _SwitchConfig_Action_o_Type()
)
switchConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_Action_o.setStatus("mandatory")
_MibswitchConfig_AtmParameters_OutgoingShaperTable_Object = MibTable
mibswitchConfig_AtmParameters_OutgoingShaperTable = _MibswitchConfig_AtmParameters_OutgoingShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 2)
)
if mibBuilder.loadTexts:
    mibswitchConfig_AtmParameters_OutgoingShaperTable.setStatus("mandatory")
_MibswitchConfig_AtmParameters_OutgoingShaperEntry_Object = MibTableRow
mibswitchConfig_AtmParameters_OutgoingShaperEntry = _MibswitchConfig_AtmParameters_OutgoingShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 2, 1)
)
mibswitchConfig_AtmParameters_OutgoingShaperEntry.setIndexNames(
    (0, "ASCEND-MIBSWITCHCONFIG-MIB", "switchConfig-AtmParameters-OutgoingShaper-SwitchName"),
    (0, "ASCEND-MIBSWITCHCONFIG-MIB", "switchConfig-AtmParameters-OutgoingShaper-Index-o"),
)
if mibBuilder.loadTexts:
    mibswitchConfig_AtmParameters_OutgoingShaperEntry.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingShaper_SwitchName_Type = DisplayString
_SwitchConfig_AtmParameters_OutgoingShaper_SwitchName_Object = MibScalar
switchConfig_AtmParameters_OutgoingShaper_SwitchName = _SwitchConfig_AtmParameters_OutgoingShaper_SwitchName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 2, 1, 1),
    _SwitchConfig_AtmParameters_OutgoingShaper_SwitchName_Type()
)
switchConfig_AtmParameters_OutgoingShaper_SwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingShaper_SwitchName.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingShaper_Index_o_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingShaper_Index_o_Object = MibScalar
switchConfig_AtmParameters_OutgoingShaper_Index_o = _SwitchConfig_AtmParameters_OutgoingShaper_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 2, 1, 2),
    _SwitchConfig_AtmParameters_OutgoingShaper_Index_o_Type()
)
switchConfig_AtmParameters_OutgoingShaper_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingShaper_Index_o.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingShaper_QueueIndex_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingShaper_QueueIndex_Object = MibScalar
switchConfig_AtmParameters_OutgoingShaper_QueueIndex = _SwitchConfig_AtmParameters_OutgoingShaper_QueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 2, 1, 3),
    _SwitchConfig_AtmParameters_OutgoingShaper_QueueIndex_Type()
)
switchConfig_AtmParameters_OutgoingShaper_QueueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingShaper_QueueIndex.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingShaper_Vpi_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingShaper_Vpi_Object = MibScalar
switchConfig_AtmParameters_OutgoingShaper_Vpi = _SwitchConfig_AtmParameters_OutgoingShaper_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 2, 1, 4),
    _SwitchConfig_AtmParameters_OutgoingShaper_Vpi_Type()
)
switchConfig_AtmParameters_OutgoingShaper_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingShaper_Vpi.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingShaper_Bandwidth_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingShaper_Bandwidth_Object = MibScalar
switchConfig_AtmParameters_OutgoingShaper_Bandwidth = _SwitchConfig_AtmParameters_OutgoingShaper_Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 2, 1, 5),
    _SwitchConfig_AtmParameters_OutgoingShaper_Bandwidth_Type()
)
switchConfig_AtmParameters_OutgoingShaper_Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingShaper_Bandwidth.setStatus("mandatory")
_MibswitchConfig_AtmParameters_OutgoingQueueTable_Object = MibTable
mibswitchConfig_AtmParameters_OutgoingQueueTable = _MibswitchConfig_AtmParameters_OutgoingQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3)
)
if mibBuilder.loadTexts:
    mibswitchConfig_AtmParameters_OutgoingQueueTable.setStatus("mandatory")
_MibswitchConfig_AtmParameters_OutgoingQueueEntry_Object = MibTableRow
mibswitchConfig_AtmParameters_OutgoingQueueEntry = _MibswitchConfig_AtmParameters_OutgoingQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1)
)
mibswitchConfig_AtmParameters_OutgoingQueueEntry.setIndexNames(
    (0, "ASCEND-MIBSWITCHCONFIG-MIB", "switchConfig-AtmParameters-OutgoingQueue-SwitchName"),
    (0, "ASCEND-MIBSWITCHCONFIG-MIB", "switchConfig-AtmParameters-OutgoingQueue-Index-o"),
)
if mibBuilder.loadTexts:
    mibswitchConfig_AtmParameters_OutgoingQueueEntry.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingQueue_SwitchName_Type = DisplayString
_SwitchConfig_AtmParameters_OutgoingQueue_SwitchName_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_SwitchName = _SwitchConfig_AtmParameters_OutgoingQueue_SwitchName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 1),
    _SwitchConfig_AtmParameters_OutgoingQueue_SwitchName_Type()
)
switchConfig_AtmParameters_OutgoingQueue_SwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_SwitchName.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingQueue_Index_o_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingQueue_Index_o_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_Index_o = _SwitchConfig_AtmParameters_OutgoingQueue_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 2),
    _SwitchConfig_AtmParameters_OutgoingQueue_Index_o_Type()
)
switchConfig_AtmParameters_OutgoingQueue_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_Index_o.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_Active_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_Active based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_Active_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_Active_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_Active = _SwitchConfig_AtmParameters_OutgoingQueue_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 3),
    _SwitchConfig_AtmParameters_OutgoingQueue_Active_Type()
)
switchConfig_AtmParameters_OutgoingQueue_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_Active.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingQueue_Name_Type = DisplayString
_SwitchConfig_AtmParameters_OutgoingQueue_Name_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_Name = _SwitchConfig_AtmParameters_OutgoingQueue_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 4),
    _SwitchConfig_AtmParameters_OutgoingQueue_Name_Type()
)
switchConfig_AtmParameters_OutgoingQueue_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_Name.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf = _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 5),
    _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Type()
)
switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot = _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 6),
    _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Type()
)
switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber = _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 7),
    _SwitchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Type()
)
switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_Cbr_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_Cbr based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_Cbr_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_Cbr_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_Cbr = _SwitchConfig_AtmParameters_OutgoingQueue_Cbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 8),
    _SwitchConfig_AtmParameters_OutgoingQueue_Cbr_Type()
)
switchConfig_AtmParameters_OutgoingQueue_Cbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_Cbr.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_RealTimeVbr_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_RealTimeVbr based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_RealTimeVbr_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_RealTimeVbr_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_RealTimeVbr = _SwitchConfig_AtmParameters_OutgoingQueue_RealTimeVbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 9),
    _SwitchConfig_AtmParameters_OutgoingQueue_RealTimeVbr_Type()
)
switchConfig_AtmParameters_OutgoingQueue_RealTimeVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_RealTimeVbr.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr = _SwitchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 10),
    _SwitchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr_Type()
)
switchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_Ubr_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_Ubr based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_Ubr_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_Ubr_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_Ubr = _SwitchConfig_AtmParameters_OutgoingQueue_Ubr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 11),
    _SwitchConfig_AtmParameters_OutgoingQueue_Ubr_Type()
)
switchConfig_AtmParameters_OutgoingQueue_Ubr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_Ubr.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight = _SwitchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 12),
    _SwitchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight_Type()
)
switchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight = _SwitchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 13),
    _SwitchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight_Type()
)
switchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf = _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 14),
    _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf_Type()
)
switchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot based on Integer32"""
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


_SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot = _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 15),
    _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot_Type()
)
switchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot.setStatus("mandatory")
_SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber_Type = Integer32
_SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber = _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 16),
    _SwitchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber_Type()
)
switchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber.setStatus("mandatory")


class _SwitchConfig_AtmParameters_OutgoingQueue_HopLevel_Type(Integer32):
    """Custom type switchConfig_AtmParameters_OutgoingQueue_HopLevel based on Integer32"""
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
        *(("anyLevel", 5),
          ("n-0Level", 1),
          ("n-1Level", 2),
          ("n-2Level", 3),
          ("n-3Level", 4))
    )


_SwitchConfig_AtmParameters_OutgoingQueue_HopLevel_Type.__name__ = "Integer32"
_SwitchConfig_AtmParameters_OutgoingQueue_HopLevel_Object = MibScalar
switchConfig_AtmParameters_OutgoingQueue_HopLevel = _SwitchConfig_AtmParameters_OutgoingQueue_HopLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 151, 3, 1, 17),
    _SwitchConfig_AtmParameters_OutgoingQueue_HopLevel_Type()
)
switchConfig_AtmParameters_OutgoingQueue_HopLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchConfig_AtmParameters_OutgoingQueue_HopLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSWITCHCONFIG-MIB",
    **{"DisplayString": DisplayString,
       "mibswitchConfig": mibswitchConfig,
       "mibswitchConfigTable": mibswitchConfigTable,
       "mibswitchConfigEntry": mibswitchConfigEntry,
       "switchConfig-SwitchName": switchConfig_SwitchName,
       "switchConfig-Action-o": switchConfig_Action_o,
       "mibswitchConfig-AtmParameters-OutgoingShaperTable": mibswitchConfig_AtmParameters_OutgoingShaperTable,
       "mibswitchConfig-AtmParameters-OutgoingShaperEntry": mibswitchConfig_AtmParameters_OutgoingShaperEntry,
       "switchConfig-AtmParameters-OutgoingShaper-SwitchName": switchConfig_AtmParameters_OutgoingShaper_SwitchName,
       "switchConfig-AtmParameters-OutgoingShaper-Index-o": switchConfig_AtmParameters_OutgoingShaper_Index_o,
       "switchConfig-AtmParameters-OutgoingShaper-QueueIndex": switchConfig_AtmParameters_OutgoingShaper_QueueIndex,
       "switchConfig-AtmParameters-OutgoingShaper-Vpi": switchConfig_AtmParameters_OutgoingShaper_Vpi,
       "switchConfig-AtmParameters-OutgoingShaper-Bandwidth": switchConfig_AtmParameters_OutgoingShaper_Bandwidth,
       "mibswitchConfig-AtmParameters-OutgoingQueueTable": mibswitchConfig_AtmParameters_OutgoingQueueTable,
       "mibswitchConfig-AtmParameters-OutgoingQueueEntry": mibswitchConfig_AtmParameters_OutgoingQueueEntry,
       "switchConfig-AtmParameters-OutgoingQueue-SwitchName": switchConfig_AtmParameters_OutgoingQueue_SwitchName,
       "switchConfig-AtmParameters-OutgoingQueue-Index-o": switchConfig_AtmParameters_OutgoingQueue_Index_o,
       "switchConfig-AtmParameters-OutgoingQueue-Active": switchConfig_AtmParameters_OutgoingQueue_Active,
       "switchConfig-AtmParameters-OutgoingQueue-Name": switchConfig_AtmParameters_OutgoingQueue_Name,
       "switchConfig-AtmParameters-OutgoingQueue-PhysicalAddress-Shelf": switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf,
       "switchConfig-AtmParameters-OutgoingQueue-PhysicalAddress-Slot": switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_Slot,
       "switchConfig-AtmParameters-OutgoingQueue-PhysicalAddress-ItemNumber": switchConfig_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber,
       "switchConfig-AtmParameters-OutgoingQueue-Cbr": switchConfig_AtmParameters_OutgoingQueue_Cbr,
       "switchConfig-AtmParameters-OutgoingQueue-RealTimeVbr": switchConfig_AtmParameters_OutgoingQueue_RealTimeVbr,
       "switchConfig-AtmParameters-OutgoingQueue-NonRealTimeVbr": switchConfig_AtmParameters_OutgoingQueue_NonRealTimeVbr,
       "switchConfig-AtmParameters-OutgoingQueue-Ubr": switchConfig_AtmParameters_OutgoingQueue_Ubr,
       "switchConfig-AtmParameters-OutgoingQueue-HighPriorityWeight": switchConfig_AtmParameters_OutgoingQueue_HighPriorityWeight,
       "switchConfig-AtmParameters-OutgoingQueue-LowPriorityWeight": switchConfig_AtmParameters_OutgoingQueue_LowPriorityWeight,
       "switchConfig-AtmParameters-OutgoingQueue-SourcePort-Shelf": switchConfig_AtmParameters_OutgoingQueue_SourcePort_Shelf,
       "switchConfig-AtmParameters-OutgoingQueue-SourcePort-Slot": switchConfig_AtmParameters_OutgoingQueue_SourcePort_Slot,
       "switchConfig-AtmParameters-OutgoingQueue-SourcePort-ItemNumber": switchConfig_AtmParameters_OutgoingQueue_SourcePort_ItemNumber,
       "switchConfig-AtmParameters-OutgoingQueue-HopLevel": switchConfig_AtmParameters_OutgoingQueue_HopLevel}
)
