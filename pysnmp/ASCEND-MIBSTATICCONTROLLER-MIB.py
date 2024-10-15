# SNMP MIB module (ASCEND-MIBSTATICCONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSTATICCONTROLLER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:17 2024
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

_MibmibProfControllerStatic_ObjectIdentity = ObjectIdentity
mibmibProfControllerStatic = _MibmibProfControllerStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 30)
)
_MibmibProfControllerStaticTable_Object = MibTable
mibmibProfControllerStaticTable = _MibmibProfControllerStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 1)
)
if mibBuilder.loadTexts:
    mibmibProfControllerStaticTable.setStatus("mandatory")
_MibmibProfControllerStaticEntry_Object = MibTableRow
mibmibProfControllerStaticEntry = _MibmibProfControllerStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 1, 1)
)
mibmibProfControllerStaticEntry.setIndexNames(
    (0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-Index-o"),
)
if mibBuilder.loadTexts:
    mibmibProfControllerStaticEntry.setStatus("mandatory")
_MibProfControllerStatic_Index_o_Type = Integer32
_MibProfControllerStatic_Index_o_Object = MibScalar
mibProfControllerStatic_Index_o = _MibProfControllerStatic_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 1, 1, 1),
    _MibProfControllerStatic_Index_o_Type()
)
mibProfControllerStatic_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfControllerStatic_Index_o.setStatus("mandatory")


class _MibProfControllerStatic_Action_o_Type(Integer32):
    """Custom type mibProfControllerStatic_Action_o based on Integer32"""
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


_MibProfControllerStatic_Action_o_Type.__name__ = "Integer32"
_MibProfControllerStatic_Action_o_Object = MibScalar
mibProfControllerStatic_Action_o = _MibProfControllerStatic_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 1, 1, 2),
    _MibProfControllerStatic_Action_o_Type()
)
mibProfControllerStatic_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_Action_o.setStatus("mandatory")
_MibmibProfControllerStatic_AtmParameters_OutgoingShaperTable_Object = MibTable
mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable = _MibmibProfControllerStatic_AtmParameters_OutgoingShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 2)
)
if mibBuilder.loadTexts:
    mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable.setStatus("mandatory")
_MibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry_Object = MibTableRow
mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry = _MibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1)
)
mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry.setIndexNames(
    (0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingShaper-Index-o"),
    (0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingShaper-Index1-o"),
)
if mibBuilder.loadTexts:
    mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o = _MibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 1),
    _MibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o = _MibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 2),
    _MibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex = _MibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 3),
    _MibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi = _MibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 4),
    _MibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth = _MibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 2, 1, 5),
    _MibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth.setStatus("mandatory")
_MibmibProfControllerStatic_AtmParameters_OutgoingQueueTable_Object = MibTable
mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable = _MibmibProfControllerStatic_AtmParameters_OutgoingQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3)
)
if mibBuilder.loadTexts:
    mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable.setStatus("mandatory")
_MibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry_Object = MibTableRow
mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry = _MibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1)
)
mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry.setIndexNames(
    (0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingQueue-Index-o"),
    (0, "ASCEND-MIBSTATICCONTROLLER-MIB", "mibProfControllerStatic-AtmParameters-OutgoingQueue-Index1-o"),
)
if mibBuilder.loadTexts:
    mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o = _MibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 1),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o = _MibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 2),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o.setStatus("mandatory")


class _MibProfControllerStatic_AtmParameters_OutgoingQueue_Active_Type(Integer32):
    """Custom type mibProfControllerStatic_AtmParameters_OutgoingQueue_Active based on Integer32"""
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


_MibProfControllerStatic_AtmParameters_OutgoingQueue_Active_Type.__name__ = "Integer32"
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Active_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_Active = _MibProfControllerStatic_AtmParameters_OutgoingQueue_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 3),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_Active_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_Active.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Name_Type = DisplayString
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Name_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_Name = _MibProfControllerStatic_AtmParameters_OutgoingQueue_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 4),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_Name_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_Name.setStatus("mandatory")


class _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf based on Integer32"""
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


_MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf = _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 5),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf.setStatus("mandatory")


class _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Type(Integer32):
    """Custom type mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot based on Integer32"""
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


_MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot = _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 6),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber = _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 7),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _MibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr_Type(Integer32):
    """Custom type mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr based on Integer32"""
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


_MibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr_Type.__name__ = "Integer32"
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr = _MibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 8),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr.setStatus("mandatory")


class _MibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr_Type(Integer32):
    """Custom type mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr based on Integer32"""
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


_MibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr_Type.__name__ = "Integer32"
_MibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr = _MibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 9),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr.setStatus("mandatory")


class _MibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr_Type(Integer32):
    """Custom type mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr based on Integer32"""
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


_MibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr_Type.__name__ = "Integer32"
_MibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr = _MibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 10),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr.setStatus("mandatory")


class _MibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr_Type(Integer32):
    """Custom type mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr based on Integer32"""
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


_MibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr_Type.__name__ = "Integer32"
_MibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr = _MibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 11),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight = _MibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 12),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight.setStatus("mandatory")
_MibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight_Type = Integer32
_MibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight_Object = MibScalar
mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight = _MibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 30, 3, 1, 13),
    _MibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight_Type()
)
mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSTATICCONTROLLER-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfControllerStatic": mibmibProfControllerStatic,
       "mibmibProfControllerStaticTable": mibmibProfControllerStaticTable,
       "mibmibProfControllerStaticEntry": mibmibProfControllerStaticEntry,
       "mibProfControllerStatic-Index-o": mibProfControllerStatic_Index_o,
       "mibProfControllerStatic-Action-o": mibProfControllerStatic_Action_o,
       "mibmibProfControllerStatic-AtmParameters-OutgoingShaperTable": mibmibProfControllerStatic_AtmParameters_OutgoingShaperTable,
       "mibmibProfControllerStatic-AtmParameters-OutgoingShaperEntry": mibmibProfControllerStatic_AtmParameters_OutgoingShaperEntry,
       "mibProfControllerStatic-AtmParameters-OutgoingShaper-Index-o": mibProfControllerStatic_AtmParameters_OutgoingShaper_Index_o,
       "mibProfControllerStatic-AtmParameters-OutgoingShaper-Index1-o": mibProfControllerStatic_AtmParameters_OutgoingShaper_Index1_o,
       "mibProfControllerStatic-AtmParameters-OutgoingShaper-QueueIndex": mibProfControllerStatic_AtmParameters_OutgoingShaper_QueueIndex,
       "mibProfControllerStatic-AtmParameters-OutgoingShaper-Vpi": mibProfControllerStatic_AtmParameters_OutgoingShaper_Vpi,
       "mibProfControllerStatic-AtmParameters-OutgoingShaper-Bandwidth": mibProfControllerStatic_AtmParameters_OutgoingShaper_Bandwidth,
       "mibmibProfControllerStatic-AtmParameters-OutgoingQueueTable": mibmibProfControllerStatic_AtmParameters_OutgoingQueueTable,
       "mibmibProfControllerStatic-AtmParameters-OutgoingQueueEntry": mibmibProfControllerStatic_AtmParameters_OutgoingQueueEntry,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-Index-o": mibProfControllerStatic_AtmParameters_OutgoingQueue_Index_o,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-Index1-o": mibProfControllerStatic_AtmParameters_OutgoingQueue_Index1_o,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-Active": mibProfControllerStatic_AtmParameters_OutgoingQueue_Active,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-Name": mibProfControllerStatic_AtmParameters_OutgoingQueue_Name,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-PhysicalAddress-Shelf": mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Shelf,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-PhysicalAddress-Slot": mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_Slot,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-PhysicalAddress-ItemNumber": mibProfControllerStatic_AtmParameters_OutgoingQueue_PhysicalAddress_ItemNumber,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-Cbr": mibProfControllerStatic_AtmParameters_OutgoingQueue_Cbr,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-RealTimeVbr": mibProfControllerStatic_AtmParameters_OutgoingQueue_RealTimeVbr,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-NonRealTimeVbr": mibProfControllerStatic_AtmParameters_OutgoingQueue_NonRealTimeVbr,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-Ubr": mibProfControllerStatic_AtmParameters_OutgoingQueue_Ubr,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-HighPriorityWeight": mibProfControllerStatic_AtmParameters_OutgoingQueue_HighPriorityWeight,
       "mibProfControllerStatic-AtmParameters-OutgoingQueue-LowPriorityWeight": mibProfControllerStatic_AtmParameters_OutgoingQueue_LowPriorityWeight}
)
