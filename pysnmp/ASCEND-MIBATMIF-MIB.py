# SNMP MIB module (ASCEND-MIBATMIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:07 2024
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

_MibatmInterfaceProfile_ObjectIdentity = ObjectIdentity
mibatmInterfaceProfile = _MibatmInterfaceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 40)
)
_MibatmInterfaceProfileTable_Object = MibTable
mibatmInterfaceProfileTable = _MibatmInterfaceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1)
)
if mibBuilder.loadTexts:
    mibatmInterfaceProfileTable.setStatus("mandatory")
_MibatmInterfaceProfileEntry_Object = MibTableRow
mibatmInterfaceProfileEntry = _MibatmInterfaceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1)
)
mibatmInterfaceProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMIF-MIB", "atmInterfaceProfile-Shelf-o"),
    (0, "ASCEND-MIBATMIF-MIB", "atmInterfaceProfile-Slot-o"),
    (0, "ASCEND-MIBATMIF-MIB", "atmInterfaceProfile-Item-o"),
    (0, "ASCEND-MIBATMIF-MIB", "atmInterfaceProfile-LogicalItem-o"),
)
if mibBuilder.loadTexts:
    mibatmInterfaceProfileEntry.setStatus("mandatory")
_AtmInterfaceProfile_Shelf_o_Type = Integer32
_AtmInterfaceProfile_Shelf_o_Object = MibScalar
atmInterfaceProfile_Shelf_o = _AtmInterfaceProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 1),
    _AtmInterfaceProfile_Shelf_o_Type()
)
atmInterfaceProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceProfile_Shelf_o.setStatus("mandatory")
_AtmInterfaceProfile_Slot_o_Type = Integer32
_AtmInterfaceProfile_Slot_o_Object = MibScalar
atmInterfaceProfile_Slot_o = _AtmInterfaceProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 2),
    _AtmInterfaceProfile_Slot_o_Type()
)
atmInterfaceProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceProfile_Slot_o.setStatus("mandatory")
_AtmInterfaceProfile_Item_o_Type = Integer32
_AtmInterfaceProfile_Item_o_Object = MibScalar
atmInterfaceProfile_Item_o = _AtmInterfaceProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 3),
    _AtmInterfaceProfile_Item_o_Type()
)
atmInterfaceProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceProfile_Item_o.setStatus("mandatory")
_AtmInterfaceProfile_LogicalItem_o_Type = Integer32
_AtmInterfaceProfile_LogicalItem_o_Object = MibScalar
atmInterfaceProfile_LogicalItem_o = _AtmInterfaceProfile_LogicalItem_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 4),
    _AtmInterfaceProfile_LogicalItem_o_Type()
)
atmInterfaceProfile_LogicalItem_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceProfile_LogicalItem_o.setStatus("mandatory")


class _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf based on Integer32"""
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


_AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object = MibScalar
atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf = _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 5),
    _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf_Type()
)
atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf.setStatus("mandatory")


class _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type(Integer32):
    """Custom type atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot based on Integer32"""
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


_AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object = MibScalar
atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot = _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 6),
    _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot_Type()
)
atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot.setStatus("mandatory")
_AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type = Integer32
_AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object = MibScalar
atmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber = _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 7),
    _AtmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber_Type()
)
atmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber.setStatus("mandatory")
_AtmInterfaceProfile_InterfaceAddress_LogicalItem_Type = Integer32
_AtmInterfaceProfile_InterfaceAddress_LogicalItem_Object = MibScalar
atmInterfaceProfile_InterfaceAddress_LogicalItem = _AtmInterfaceProfile_InterfaceAddress_LogicalItem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 8),
    _AtmInterfaceProfile_InterfaceAddress_LogicalItem_Type()
)
atmInterfaceProfile_InterfaceAddress_LogicalItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_InterfaceAddress_LogicalItem.setStatus("mandatory")
_AtmInterfaceProfile_Name_Type = DisplayString
_AtmInterfaceProfile_Name_Object = MibScalar
atmInterfaceProfile_Name = _AtmInterfaceProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 9),
    _AtmInterfaceProfile_Name_Type()
)
atmInterfaceProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_Name.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_Enabled_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_Enabled based on Integer32"""
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


_AtmInterfaceProfile_SvcOptions_Enabled_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_Enabled_Object = MibScalar
atmInterfaceProfile_SvcOptions_Enabled = _AtmInterfaceProfile_SvcOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 10),
    _AtmInterfaceProfile_SvcOptions_Enabled_Type()
)
atmInterfaceProfile_SvcOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Enabled.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_AtmProtocol_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_AtmProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni30", 2),
          ("uni31", 3))
    )


_AtmInterfaceProfile_SvcOptions_AtmProtocol_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_AtmProtocol_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmProtocol = _AtmInterfaceProfile_SvcOptions_AtmProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 11),
    _AtmInterfaceProfile_SvcOptions_AtmProtocol_Type()
)
atmInterfaceProfile_SvcOptions_AtmProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmProtocol.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aesa", 3),
          ("isdn", 2),
          ("undefined", 1),
          ("unknown", 5),
          ("x121", 9))
    )


_AtmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan = _AtmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 12),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress_Type = DisplayString
_AtmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress = _AtmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 13),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("customAesa", 5),
          ("dccAesa", 2),
          ("e164Aesa", 4),
          ("icdAesa", 6),
          ("undefined", 1))
    )


_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format = _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 14),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi_Type = DisplayString
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi = _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 15),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi_Type = DisplayString
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi = _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 16),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp_Type = DisplayString
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp = _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 17),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi_Type = DisplayString
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi = _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 18),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel_Type = DisplayString
_AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel_Object = MibScalar
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel = _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 19),
    _AtmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel_Type()
)
atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_InsertCallingPartyAddr_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_InsertCallingPartyAddr based on Integer32"""
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


_AtmInterfaceProfile_SvcOptions_InsertCallingPartyAddr_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_InsertCallingPartyAddr_Object = MibScalar
atmInterfaceProfile_SvcOptions_InsertCallingPartyAddr = _AtmInterfaceProfile_SvcOptions_InsertCallingPartyAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 20),
    _AtmInterfaceProfile_SvcOptions_InsertCallingPartyAddr_Type()
)
atmInterfaceProfile_SvcOptions_InsertCallingPartyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_InsertCallingPartyAddr.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart = _AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 21),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq = _AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 22),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 23),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 24),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 25),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 26),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 27),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 28),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 29),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 30),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 31),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 32),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 33),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 34),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 35),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 36),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 37),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs = _AtmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 38),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 39),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 40),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 41),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 42),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries_Type = Integer32
_AtmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries = _AtmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 43),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci based on Integer32"""
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


_AtmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci_Object = MibScalar
atmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci = _AtmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 44),
    _AtmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci_Type()
)
atmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize = _AtmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 45),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc = _AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 46),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd = _AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 47),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat = _AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 48),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TccMs_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TccMs_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_TccMs = _AtmInterfaceProfile_SvcOptions_QsaalOptions_TccMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 49),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_TccMs_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_TccMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_TccMs.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs = _AtmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 50),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs = _AtmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 51),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs = _AtmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 52),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs.setStatus("mandatory")
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs_Type = Integer32
_AtmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs = _AtmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 53),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission based on Integer32"""
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


_AtmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission = _AtmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 54),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat based on Integer32"""
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


_AtmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat = _AtmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 55),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat.setStatus("mandatory")


class _AtmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll_Type(Integer32):
    """Custom type atmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll based on Integer32"""
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


_AtmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll_Type.__name__ = "Integer32"
_AtmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll_Object = MibScalar
atmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll = _AtmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 56),
    _AtmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll_Type()
)
atmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll.setStatus("mandatory")


class _AtmInterfaceProfile_Action_o_Type(Integer32):
    """Custom type atmInterfaceProfile_Action_o based on Integer32"""
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


_AtmInterfaceProfile_Action_o_Type.__name__ = "Integer32"
_AtmInterfaceProfile_Action_o_Object = MibScalar
atmInterfaceProfile_Action_o = _AtmInterfaceProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 40, 1, 1, 57),
    _AtmInterfaceProfile_Action_o_Type()
)
atmInterfaceProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMIF-MIB",
    **{"DisplayString": DisplayString,
       "mibatmInterfaceProfile": mibatmInterfaceProfile,
       "mibatmInterfaceProfileTable": mibatmInterfaceProfileTable,
       "mibatmInterfaceProfileEntry": mibatmInterfaceProfileEntry,
       "atmInterfaceProfile-Shelf-o": atmInterfaceProfile_Shelf_o,
       "atmInterfaceProfile-Slot-o": atmInterfaceProfile_Slot_o,
       "atmInterfaceProfile-Item-o": atmInterfaceProfile_Item_o,
       "atmInterfaceProfile-LogicalItem-o": atmInterfaceProfile_LogicalItem_o,
       "atmInterfaceProfile-InterfaceAddress-PhysicalAddress-Shelf": atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Shelf,
       "atmInterfaceProfile-InterfaceAddress-PhysicalAddress-Slot": atmInterfaceProfile_InterfaceAddress_PhysicalAddress_Slot,
       "atmInterfaceProfile-InterfaceAddress-PhysicalAddress-ItemNumber": atmInterfaceProfile_InterfaceAddress_PhysicalAddress_ItemNumber,
       "atmInterfaceProfile-InterfaceAddress-LogicalItem": atmInterfaceProfile_InterfaceAddress_LogicalItem,
       "atmInterfaceProfile-Name": atmInterfaceProfile_Name,
       "atmInterfaceProfile-SvcOptions-Enabled": atmInterfaceProfile_SvcOptions_Enabled,
       "atmInterfaceProfile-SvcOptions-AtmProtocol": atmInterfaceProfile_SvcOptions_AtmProtocol,
       "atmInterfaceProfile-SvcOptions-AtmAddress-NumberingPlan": atmInterfaceProfile_SvcOptions_AtmAddress_NumberingPlan,
       "atmInterfaceProfile-SvcOptions-AtmAddress-E164NativeAddress": atmInterfaceProfile_SvcOptions_AtmAddress_E164NativeAddress,
       "atmInterfaceProfile-SvcOptions-AtmAddress-AesaAddress-Format": atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_Format,
       "atmInterfaceProfile-SvcOptions-AtmAddress-AesaAddress-IdpPortion-Afi": atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Afi,
       "atmInterfaceProfile-SvcOptions-AtmAddress-AesaAddress-IdpPortion-Idi": atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_IdpPortion_Idi,
       "atmInterfaceProfile-SvcOptions-AtmAddress-AesaAddress-DspPortion-HoDsp": atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_HoDsp,
       "atmInterfaceProfile-SvcOptions-AtmAddress-AesaAddress-DspPortion-Esi": atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Esi,
       "atmInterfaceProfile-SvcOptions-AtmAddress-AesaAddress-DspPortion-Sel": atmInterfaceProfile_SvcOptions_AtmAddress_AesaAddress_DspPortion_Sel,
       "atmInterfaceProfile-SvcOptions-InsertCallingPartyAddr": atmInterfaceProfile_SvcOptions_InsertCallingPartyAddr,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-MaxRestart": atmInterfaceProfile_SvcOptions_Q93bOptions_MaxRestart,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-MaxStatenq": atmInterfaceProfile_SvcOptions_Q93bOptions_MaxStatenq,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T301Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T301Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T303Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T303Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T306Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T306Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T308Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T308Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T309Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T309Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T310Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T310Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T313Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T313Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T316Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T316Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T317Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T317Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T322Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T322Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T331Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T331Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T333Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T333Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T397Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T397Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T398Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T398Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T399Ms": atmInterfaceProfile_SvcOptions_Q93bOptions_T399Ms,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-SaalRetryMs": atmInterfaceProfile_SvcOptions_Q93bOptions_SaalRetryMs,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T303NumReties": atmInterfaceProfile_SvcOptions_Q93bOptions_T303NumReties,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T308NumRetries": atmInterfaceProfile_SvcOptions_Q93bOptions_T308NumRetries,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T316NumRetries": atmInterfaceProfile_SvcOptions_Q93bOptions_T316NumRetries,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T322NumRetries": atmInterfaceProfile_SvcOptions_Q93bOptions_T322NumRetries,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-T331NumRetries": atmInterfaceProfile_SvcOptions_Q93bOptions_T331NumRetries,
       "atmInterfaceProfile-SvcOptions-Q93bOptions-AssignVpiVci": atmInterfaceProfile_SvcOptions_Q93bOptions_AssignVpiVci,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-WindowSize": atmInterfaceProfile_SvcOptions_QsaalOptions_WindowSize,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-MaxCc": atmInterfaceProfile_SvcOptions_QsaalOptions_MaxCc,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-MaxPd": atmInterfaceProfile_SvcOptions_QsaalOptions_MaxPd,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-MaxStat": atmInterfaceProfile_SvcOptions_QsaalOptions_MaxStat,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-TccMs": atmInterfaceProfile_SvcOptions_QsaalOptions_TccMs,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-TpollMs": atmInterfaceProfile_SvcOptions_QsaalOptions_TpollMs,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-TkeepaliveMs": atmInterfaceProfile_SvcOptions_QsaalOptions_TkeepaliveMs,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-TnoresponseMs": atmInterfaceProfile_SvcOptions_QsaalOptions_TnoresponseMs,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-TidleMs": atmInterfaceProfile_SvcOptions_QsaalOptions_TidleMs,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-PollAfterRetransmission": atmInterfaceProfile_SvcOptions_QsaalOptions_PollAfterRetransmission,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-RepeatUstat": atmInterfaceProfile_SvcOptions_QsaalOptions_RepeatUstat,
       "atmInterfaceProfile-SvcOptions-QsaalOptions-UstatRspToPoll": atmInterfaceProfile_SvcOptions_QsaalOptions_UstatRspToPoll,
       "atmInterfaceProfile-Action-o": atmInterfaceProfile_Action_o}
)
