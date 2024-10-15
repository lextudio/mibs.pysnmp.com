# SNMP MIB module (ASCEND-MIBATMSIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMSIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:12 2024
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

_MibatmIntfSigParams_ObjectIdentity = ObjectIdentity
mibatmIntfSigParams = _MibatmIntfSigParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 52)
)
_MibatmIntfSigParamsTable_Object = MibTable
mibatmIntfSigParamsTable = _MibatmIntfSigParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1)
)
if mibBuilder.loadTexts:
    mibatmIntfSigParamsTable.setStatus("mandatory")
_MibatmIntfSigParamsEntry_Object = MibTableRow
mibatmIntfSigParamsEntry = _MibatmIntfSigParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1)
)
mibatmIntfSigParamsEntry.setIndexNames(
    (0, "ASCEND-MIBATMSIG-MIB", "atmIntfSigParams-Shelf-o"),
    (0, "ASCEND-MIBATMSIG-MIB", "atmIntfSigParams-Slot-o"),
    (0, "ASCEND-MIBATMSIG-MIB", "atmIntfSigParams-Item-o"),
    (0, "ASCEND-MIBATMSIG-MIB", "atmIntfSigParams-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibatmIntfSigParamsEntry.setStatus("mandatory")
_AtmIntfSigParams_Shelf_o_Type = Integer32
_AtmIntfSigParams_Shelf_o_Object = MibScalar
atmIntfSigParams_Shelf_o = _AtmIntfSigParams_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 1),
    _AtmIntfSigParams_Shelf_o_Type()
)
atmIntfSigParams_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfSigParams_Shelf_o.setStatus("mandatory")
_AtmIntfSigParams_Slot_o_Type = Integer32
_AtmIntfSigParams_Slot_o_Object = MibScalar
atmIntfSigParams_Slot_o = _AtmIntfSigParams_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 2),
    _AtmIntfSigParams_Slot_o_Type()
)
atmIntfSigParams_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfSigParams_Slot_o.setStatus("mandatory")
_AtmIntfSigParams_Item_o_Type = Integer32
_AtmIntfSigParams_Item_o_Object = MibScalar
atmIntfSigParams_Item_o = _AtmIntfSigParams_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 3),
    _AtmIntfSigParams_Item_o_Type()
)
atmIntfSigParams_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfSigParams_Item_o.setStatus("mandatory")
_AtmIntfSigParams_LogicalItem_o_Type = Integer32
_AtmIntfSigParams_LogicalItem_o_Object = MibScalar
atmIntfSigParams_LogicalItem_o = _AtmIntfSigParams_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 4),
    _AtmIntfSigParams_LogicalItem_o_Type()
)
atmIntfSigParams_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfSigParams_LogicalItem_o.setStatus("mandatory")


class _AtmIntfSigParams_Address_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atmIntfSigParams_Address_PhysicalAddress_Shelf based on Integer32"""
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


_AtmIntfSigParams_Address_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtmIntfSigParams_Address_PhysicalAddress_Shelf_Object = MibScalar
atmIntfSigParams_Address_PhysicalAddress_Shelf = _AtmIntfSigParams_Address_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 5),
    _AtmIntfSigParams_Address_PhysicalAddress_Shelf_Type()
)
atmIntfSigParams_Address_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Address_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtmIntfSigParams_Address_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atmIntfSigParams_Address_PhysicalAddress_Slot based on Integer32"""
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


_AtmIntfSigParams_Address_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtmIntfSigParams_Address_PhysicalAddress_Slot_Object = MibScalar
atmIntfSigParams_Address_PhysicalAddress_Slot = _AtmIntfSigParams_Address_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 6),
    _AtmIntfSigParams_Address_PhysicalAddress_Slot_Type()
)
atmIntfSigParams_Address_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Address_PhysicalAddress_Slot.setStatus("mandatory")
_AtmIntfSigParams_Address_PhysicalAddress_ItemNumber_Type = Integer32
_AtmIntfSigParams_Address_PhysicalAddress_ItemNumber_Object = MibScalar
atmIntfSigParams_Address_PhysicalAddress_ItemNumber = _AtmIntfSigParams_Address_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 7),
    _AtmIntfSigParams_Address_PhysicalAddress_ItemNumber_Type()
)
atmIntfSigParams_Address_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Address_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmIntfSigParams_Address_LogicalItem_Type = Integer32
_AtmIntfSigParams_Address_LogicalItem_Object = MibScalar
atmIntfSigParams_Address_LogicalItem = _AtmIntfSigParams_Address_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 8),
    _AtmIntfSigParams_Address_LogicalItem_Type()
)
atmIntfSigParams_Address_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Address_LogicalItem.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_MaxRestart_Type = Integer32
_AtmIntfSigParams_Q2931Options_MaxRestart_Object = MibScalar
atmIntfSigParams_Q2931Options_MaxRestart = _AtmIntfSigParams_Q2931Options_MaxRestart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 9),
    _AtmIntfSigParams_Q2931Options_MaxRestart_Type()
)
atmIntfSigParams_Q2931Options_MaxRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_MaxRestart.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_MaxStatenq_Type = Integer32
_AtmIntfSigParams_Q2931Options_MaxStatenq_Object = MibScalar
atmIntfSigParams_Q2931Options_MaxStatenq = _AtmIntfSigParams_Q2931Options_MaxStatenq_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 10),
    _AtmIntfSigParams_Q2931Options_MaxStatenq_Type()
)
atmIntfSigParams_Q2931Options_MaxStatenq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_MaxStatenq.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T301Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T301Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T301Ms = _AtmIntfSigParams_Q2931Options_T301Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 11),
    _AtmIntfSigParams_Q2931Options_T301Ms_Type()
)
atmIntfSigParams_Q2931Options_T301Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T301Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T303Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T303Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T303Ms = _AtmIntfSigParams_Q2931Options_T303Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 12),
    _AtmIntfSigParams_Q2931Options_T303Ms_Type()
)
atmIntfSigParams_Q2931Options_T303Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T303Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T306Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T306Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T306Ms = _AtmIntfSigParams_Q2931Options_T306Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 13),
    _AtmIntfSigParams_Q2931Options_T306Ms_Type()
)
atmIntfSigParams_Q2931Options_T306Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T306Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T308Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T308Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T308Ms = _AtmIntfSigParams_Q2931Options_T308Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 14),
    _AtmIntfSigParams_Q2931Options_T308Ms_Type()
)
atmIntfSigParams_Q2931Options_T308Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T308Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T309Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T309Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T309Ms = _AtmIntfSigParams_Q2931Options_T309Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 15),
    _AtmIntfSigParams_Q2931Options_T309Ms_Type()
)
atmIntfSigParams_Q2931Options_T309Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T309Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T310Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T310Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T310Ms = _AtmIntfSigParams_Q2931Options_T310Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 16),
    _AtmIntfSigParams_Q2931Options_T310Ms_Type()
)
atmIntfSigParams_Q2931Options_T310Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T310Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T313Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T313Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T313Ms = _AtmIntfSigParams_Q2931Options_T313Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 17),
    _AtmIntfSigParams_Q2931Options_T313Ms_Type()
)
atmIntfSigParams_Q2931Options_T313Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T313Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T316Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T316Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T316Ms = _AtmIntfSigParams_Q2931Options_T316Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 18),
    _AtmIntfSigParams_Q2931Options_T316Ms_Type()
)
atmIntfSigParams_Q2931Options_T316Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T316Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T317Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T317Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T317Ms = _AtmIntfSigParams_Q2931Options_T317Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 19),
    _AtmIntfSigParams_Q2931Options_T317Ms_Type()
)
atmIntfSigParams_Q2931Options_T317Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T317Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T322Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T322Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T322Ms = _AtmIntfSigParams_Q2931Options_T322Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 20),
    _AtmIntfSigParams_Q2931Options_T322Ms_Type()
)
atmIntfSigParams_Q2931Options_T322Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T322Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T331Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T331Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T331Ms = _AtmIntfSigParams_Q2931Options_T331Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 21),
    _AtmIntfSigParams_Q2931Options_T331Ms_Type()
)
atmIntfSigParams_Q2931Options_T331Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T331Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T333Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T333Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T333Ms = _AtmIntfSigParams_Q2931Options_T333Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 22),
    _AtmIntfSigParams_Q2931Options_T333Ms_Type()
)
atmIntfSigParams_Q2931Options_T333Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T333Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T397Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T397Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T397Ms = _AtmIntfSigParams_Q2931Options_T397Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 23),
    _AtmIntfSigParams_Q2931Options_T397Ms_Type()
)
atmIntfSigParams_Q2931Options_T397Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T397Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T398Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T398Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T398Ms = _AtmIntfSigParams_Q2931Options_T398Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 24),
    _AtmIntfSigParams_Q2931Options_T398Ms_Type()
)
atmIntfSigParams_Q2931Options_T398Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T398Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T399Ms_Type = Integer32
_AtmIntfSigParams_Q2931Options_T399Ms_Object = MibScalar
atmIntfSigParams_Q2931Options_T399Ms = _AtmIntfSigParams_Q2931Options_T399Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 25),
    _AtmIntfSigParams_Q2931Options_T399Ms_Type()
)
atmIntfSigParams_Q2931Options_T399Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T399Ms.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_SaalRetryMs_Type = Integer32
_AtmIntfSigParams_Q2931Options_SaalRetryMs_Object = MibScalar
atmIntfSigParams_Q2931Options_SaalRetryMs = _AtmIntfSigParams_Q2931Options_SaalRetryMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 26),
    _AtmIntfSigParams_Q2931Options_SaalRetryMs_Type()
)
atmIntfSigParams_Q2931Options_SaalRetryMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_SaalRetryMs.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T303NumReties_Type = Integer32
_AtmIntfSigParams_Q2931Options_T303NumReties_Object = MibScalar
atmIntfSigParams_Q2931Options_T303NumReties = _AtmIntfSigParams_Q2931Options_T303NumReties_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 27),
    _AtmIntfSigParams_Q2931Options_T303NumReties_Type()
)
atmIntfSigParams_Q2931Options_T303NumReties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T303NumReties.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T308NumRetries_Type = Integer32
_AtmIntfSigParams_Q2931Options_T308NumRetries_Object = MibScalar
atmIntfSigParams_Q2931Options_T308NumRetries = _AtmIntfSigParams_Q2931Options_T308NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 28),
    _AtmIntfSigParams_Q2931Options_T308NumRetries_Type()
)
atmIntfSigParams_Q2931Options_T308NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T308NumRetries.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T316NumRetries_Type = Integer32
_AtmIntfSigParams_Q2931Options_T316NumRetries_Object = MibScalar
atmIntfSigParams_Q2931Options_T316NumRetries = _AtmIntfSigParams_Q2931Options_T316NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 29),
    _AtmIntfSigParams_Q2931Options_T316NumRetries_Type()
)
atmIntfSigParams_Q2931Options_T316NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T316NumRetries.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T322NumRetries_Type = Integer32
_AtmIntfSigParams_Q2931Options_T322NumRetries_Object = MibScalar
atmIntfSigParams_Q2931Options_T322NumRetries = _AtmIntfSigParams_Q2931Options_T322NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 30),
    _AtmIntfSigParams_Q2931Options_T322NumRetries_Type()
)
atmIntfSigParams_Q2931Options_T322NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T322NumRetries.setStatus("mandatory")
_AtmIntfSigParams_Q2931Options_T331NumRetries_Type = Integer32
_AtmIntfSigParams_Q2931Options_T331NumRetries_Object = MibScalar
atmIntfSigParams_Q2931Options_T331NumRetries = _AtmIntfSigParams_Q2931Options_T331NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 31),
    _AtmIntfSigParams_Q2931Options_T331NumRetries_Type()
)
atmIntfSigParams_Q2931Options_T331NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_T331NumRetries.setStatus("mandatory")


class _AtmIntfSigParams_Q2931Options_AssignVpiVci_Type(Integer32):
    """Custom type atmIntfSigParams_Q2931Options_AssignVpiVci based on Integer32"""
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


_AtmIntfSigParams_Q2931Options_AssignVpiVci_Type.__name__ = "Integer32"
_AtmIntfSigParams_Q2931Options_AssignVpiVci_Object = MibScalar
atmIntfSigParams_Q2931Options_AssignVpiVci = _AtmIntfSigParams_Q2931Options_AssignVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 32),
    _AtmIntfSigParams_Q2931Options_AssignVpiVci_Type()
)
atmIntfSigParams_Q2931Options_AssignVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Q2931Options_AssignVpiVci.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_WindowSize_Type = Integer32
_AtmIntfSigParams_QsaalOptions_WindowSize_Object = MibScalar
atmIntfSigParams_QsaalOptions_WindowSize = _AtmIntfSigParams_QsaalOptions_WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 33),
    _AtmIntfSigParams_QsaalOptions_WindowSize_Type()
)
atmIntfSigParams_QsaalOptions_WindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_WindowSize.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_MaxCc_Type = Integer32
_AtmIntfSigParams_QsaalOptions_MaxCc_Object = MibScalar
atmIntfSigParams_QsaalOptions_MaxCc = _AtmIntfSigParams_QsaalOptions_MaxCc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 34),
    _AtmIntfSigParams_QsaalOptions_MaxCc_Type()
)
atmIntfSigParams_QsaalOptions_MaxCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_MaxCc.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_MaxPd_Type = Integer32
_AtmIntfSigParams_QsaalOptions_MaxPd_Object = MibScalar
atmIntfSigParams_QsaalOptions_MaxPd = _AtmIntfSigParams_QsaalOptions_MaxPd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 35),
    _AtmIntfSigParams_QsaalOptions_MaxPd_Type()
)
atmIntfSigParams_QsaalOptions_MaxPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_MaxPd.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_MaxStat_Type = Integer32
_AtmIntfSigParams_QsaalOptions_MaxStat_Object = MibScalar
atmIntfSigParams_QsaalOptions_MaxStat = _AtmIntfSigParams_QsaalOptions_MaxStat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 36),
    _AtmIntfSigParams_QsaalOptions_MaxStat_Type()
)
atmIntfSigParams_QsaalOptions_MaxStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_MaxStat.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_TccMs_Type = Integer32
_AtmIntfSigParams_QsaalOptions_TccMs_Object = MibScalar
atmIntfSigParams_QsaalOptions_TccMs = _AtmIntfSigParams_QsaalOptions_TccMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 37),
    _AtmIntfSigParams_QsaalOptions_TccMs_Type()
)
atmIntfSigParams_QsaalOptions_TccMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_TccMs.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_TpollMs_Type = Integer32
_AtmIntfSigParams_QsaalOptions_TpollMs_Object = MibScalar
atmIntfSigParams_QsaalOptions_TpollMs = _AtmIntfSigParams_QsaalOptions_TpollMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 38),
    _AtmIntfSigParams_QsaalOptions_TpollMs_Type()
)
atmIntfSigParams_QsaalOptions_TpollMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_TpollMs.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_TkeepaliveMs_Type = Integer32
_AtmIntfSigParams_QsaalOptions_TkeepaliveMs_Object = MibScalar
atmIntfSigParams_QsaalOptions_TkeepaliveMs = _AtmIntfSigParams_QsaalOptions_TkeepaliveMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 39),
    _AtmIntfSigParams_QsaalOptions_TkeepaliveMs_Type()
)
atmIntfSigParams_QsaalOptions_TkeepaliveMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_TkeepaliveMs.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_TnoresponseMs_Type = Integer32
_AtmIntfSigParams_QsaalOptions_TnoresponseMs_Object = MibScalar
atmIntfSigParams_QsaalOptions_TnoresponseMs = _AtmIntfSigParams_QsaalOptions_TnoresponseMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 40),
    _AtmIntfSigParams_QsaalOptions_TnoresponseMs_Type()
)
atmIntfSigParams_QsaalOptions_TnoresponseMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_TnoresponseMs.setStatus("mandatory")
_AtmIntfSigParams_QsaalOptions_TidleMs_Type = Integer32
_AtmIntfSigParams_QsaalOptions_TidleMs_Object = MibScalar
atmIntfSigParams_QsaalOptions_TidleMs = _AtmIntfSigParams_QsaalOptions_TidleMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 41),
    _AtmIntfSigParams_QsaalOptions_TidleMs_Type()
)
atmIntfSigParams_QsaalOptions_TidleMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_TidleMs.setStatus("mandatory")


class _AtmIntfSigParams_QsaalOptions_PollAfterRetransmission_Type(Integer32):
    """Custom type atmIntfSigParams_QsaalOptions_PollAfterRetransmission based on Integer32"""
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


_AtmIntfSigParams_QsaalOptions_PollAfterRetransmission_Type.__name__ = "Integer32"
_AtmIntfSigParams_QsaalOptions_PollAfterRetransmission_Object = MibScalar
atmIntfSigParams_QsaalOptions_PollAfterRetransmission = _AtmIntfSigParams_QsaalOptions_PollAfterRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 42),
    _AtmIntfSigParams_QsaalOptions_PollAfterRetransmission_Type()
)
atmIntfSigParams_QsaalOptions_PollAfterRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_PollAfterRetransmission.setStatus("mandatory")


class _AtmIntfSigParams_QsaalOptions_RepeatUstat_Type(Integer32):
    """Custom type atmIntfSigParams_QsaalOptions_RepeatUstat based on Integer32"""
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


_AtmIntfSigParams_QsaalOptions_RepeatUstat_Type.__name__ = "Integer32"
_AtmIntfSigParams_QsaalOptions_RepeatUstat_Object = MibScalar
atmIntfSigParams_QsaalOptions_RepeatUstat = _AtmIntfSigParams_QsaalOptions_RepeatUstat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 43),
    _AtmIntfSigParams_QsaalOptions_RepeatUstat_Type()
)
atmIntfSigParams_QsaalOptions_RepeatUstat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_RepeatUstat.setStatus("mandatory")


class _AtmIntfSigParams_QsaalOptions_UstatRspToPoll_Type(Integer32):
    """Custom type atmIntfSigParams_QsaalOptions_UstatRspToPoll based on Integer32"""
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


_AtmIntfSigParams_QsaalOptions_UstatRspToPoll_Type.__name__ = "Integer32"
_AtmIntfSigParams_QsaalOptions_UstatRspToPoll_Object = MibScalar
atmIntfSigParams_QsaalOptions_UstatRspToPoll = _AtmIntfSigParams_QsaalOptions_UstatRspToPoll_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 44),
    _AtmIntfSigParams_QsaalOptions_UstatRspToPoll_Type()
)
atmIntfSigParams_QsaalOptions_UstatRspToPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_QsaalOptions_UstatRspToPoll.setStatus("mandatory")


class _AtmIntfSigParams_Action_o_Type(Integer32):
    """Custom type atmIntfSigParams_Action_o based on Integer32"""
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


_AtmIntfSigParams_Action_o_Type.__name__ = "Integer32"
_AtmIntfSigParams_Action_o_Object = MibScalar
atmIntfSigParams_Action_o = _AtmIntfSigParams_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 52, 1, 1, 45),
    _AtmIntfSigParams_Action_o_Type()
)
atmIntfSigParams_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigParams_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMSIG-MIB",
    **{"DisplayString": DisplayString,
       "mibatmIntfSigParams": mibatmIntfSigParams,
       "mibatmIntfSigParamsTable": mibatmIntfSigParamsTable,
       "mibatmIntfSigParamsEntry": mibatmIntfSigParamsEntry,
       "atmIntfSigParams-Shelf-o": atmIntfSigParams_Shelf_o,
       "atmIntfSigParams-Slot-o": atmIntfSigParams_Slot_o,
       "atmIntfSigParams-Item-o": atmIntfSigParams_Item_o,
       "atmIntfSigParams-LogicalItem-o": atmIntfSigParams_LogicalItem_o,
       "atmIntfSigParams-Address-PhysicalAddress-Shelf": atmIntfSigParams_Address_PhysicalAddress_Shelf,
       "atmIntfSigParams-Address-PhysicalAddress-Slot": atmIntfSigParams_Address_PhysicalAddress_Slot,
       "atmIntfSigParams-Address-PhysicalAddress-ItemNumber": atmIntfSigParams_Address_PhysicalAddress_ItemNumber,
       "atmIntfSigParams-Address-LogicalItem": atmIntfSigParams_Address_LogicalItem,
       "atmIntfSigParams-Q2931Options-MaxRestart": atmIntfSigParams_Q2931Options_MaxRestart,
       "atmIntfSigParams-Q2931Options-MaxStatenq": atmIntfSigParams_Q2931Options_MaxStatenq,
       "atmIntfSigParams-Q2931Options-T301Ms": atmIntfSigParams_Q2931Options_T301Ms,
       "atmIntfSigParams-Q2931Options-T303Ms": atmIntfSigParams_Q2931Options_T303Ms,
       "atmIntfSigParams-Q2931Options-T306Ms": atmIntfSigParams_Q2931Options_T306Ms,
       "atmIntfSigParams-Q2931Options-T308Ms": atmIntfSigParams_Q2931Options_T308Ms,
       "atmIntfSigParams-Q2931Options-T309Ms": atmIntfSigParams_Q2931Options_T309Ms,
       "atmIntfSigParams-Q2931Options-T310Ms": atmIntfSigParams_Q2931Options_T310Ms,
       "atmIntfSigParams-Q2931Options-T313Ms": atmIntfSigParams_Q2931Options_T313Ms,
       "atmIntfSigParams-Q2931Options-T316Ms": atmIntfSigParams_Q2931Options_T316Ms,
       "atmIntfSigParams-Q2931Options-T317Ms": atmIntfSigParams_Q2931Options_T317Ms,
       "atmIntfSigParams-Q2931Options-T322Ms": atmIntfSigParams_Q2931Options_T322Ms,
       "atmIntfSigParams-Q2931Options-T331Ms": atmIntfSigParams_Q2931Options_T331Ms,
       "atmIntfSigParams-Q2931Options-T333Ms": atmIntfSigParams_Q2931Options_T333Ms,
       "atmIntfSigParams-Q2931Options-T397Ms": atmIntfSigParams_Q2931Options_T397Ms,
       "atmIntfSigParams-Q2931Options-T398Ms": atmIntfSigParams_Q2931Options_T398Ms,
       "atmIntfSigParams-Q2931Options-T399Ms": atmIntfSigParams_Q2931Options_T399Ms,
       "atmIntfSigParams-Q2931Options-SaalRetryMs": atmIntfSigParams_Q2931Options_SaalRetryMs,
       "atmIntfSigParams-Q2931Options-T303NumReties": atmIntfSigParams_Q2931Options_T303NumReties,
       "atmIntfSigParams-Q2931Options-T308NumRetries": atmIntfSigParams_Q2931Options_T308NumRetries,
       "atmIntfSigParams-Q2931Options-T316NumRetries": atmIntfSigParams_Q2931Options_T316NumRetries,
       "atmIntfSigParams-Q2931Options-T322NumRetries": atmIntfSigParams_Q2931Options_T322NumRetries,
       "atmIntfSigParams-Q2931Options-T331NumRetries": atmIntfSigParams_Q2931Options_T331NumRetries,
       "atmIntfSigParams-Q2931Options-AssignVpiVci": atmIntfSigParams_Q2931Options_AssignVpiVci,
       "atmIntfSigParams-QsaalOptions-WindowSize": atmIntfSigParams_QsaalOptions_WindowSize,
       "atmIntfSigParams-QsaalOptions-MaxCc": atmIntfSigParams_QsaalOptions_MaxCc,
       "atmIntfSigParams-QsaalOptions-MaxPd": atmIntfSigParams_QsaalOptions_MaxPd,
       "atmIntfSigParams-QsaalOptions-MaxStat": atmIntfSigParams_QsaalOptions_MaxStat,
       "atmIntfSigParams-QsaalOptions-TccMs": atmIntfSigParams_QsaalOptions_TccMs,
       "atmIntfSigParams-QsaalOptions-TpollMs": atmIntfSigParams_QsaalOptions_TpollMs,
       "atmIntfSigParams-QsaalOptions-TkeepaliveMs": atmIntfSigParams_QsaalOptions_TkeepaliveMs,
       "atmIntfSigParams-QsaalOptions-TnoresponseMs": atmIntfSigParams_QsaalOptions_TnoresponseMs,
       "atmIntfSigParams-QsaalOptions-TidleMs": atmIntfSigParams_QsaalOptions_TidleMs,
       "atmIntfSigParams-QsaalOptions-PollAfterRetransmission": atmIntfSigParams_QsaalOptions_PollAfterRetransmission,
       "atmIntfSigParams-QsaalOptions-RepeatUstat": atmIntfSigParams_QsaalOptions_RepeatUstat,
       "atmIntfSigParams-QsaalOptions-UstatRspToPoll": atmIntfSigParams_QsaalOptions_UstatRspToPoll,
       "atmIntfSigParams-Action-o": atmIntfSigParams_Action_o}
)
