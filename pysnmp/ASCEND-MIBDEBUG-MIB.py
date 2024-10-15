# SNMP MIB module (ASCEND-MIBDEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDEBUG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:26 2024
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

_MibdebugProfile_ObjectIdentity = ObjectIdentity
mibdebugProfile = _MibdebugProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 72)
)
_MibdebugProfileTable_Object = MibTable
mibdebugProfileTable = _MibdebugProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1)
)
if mibBuilder.loadTexts:
    mibdebugProfileTable.setStatus("mandatory")
_MibdebugProfileEntry_Object = MibTableRow
mibdebugProfileEntry = _MibdebugProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1)
)
mibdebugProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDEBUG-MIB", "debugProfile-Shelf-o"),
    (0, "ASCEND-MIBDEBUG-MIB", "debugProfile-Slot-o"),
    (0, "ASCEND-MIBDEBUG-MIB", "debugProfile-Item-o"),
)
if mibBuilder.loadTexts:
    mibdebugProfileEntry.setStatus("mandatory")
_DebugProfile_Shelf_o_Type = Integer32
_DebugProfile_Shelf_o_Object = MibScalar
debugProfile_Shelf_o = _DebugProfile_Shelf_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 1),
    _DebugProfile_Shelf_o_Type()
)
debugProfile_Shelf_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugProfile_Shelf_o.setStatus("mandatory")
_DebugProfile_Slot_o_Type = Integer32
_DebugProfile_Slot_o_Object = MibScalar
debugProfile_Slot_o = _DebugProfile_Slot_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 2),
    _DebugProfile_Slot_o_Type()
)
debugProfile_Slot_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugProfile_Slot_o.setStatus("mandatory")
_DebugProfile_Item_o_Type = Integer32
_DebugProfile_Item_o_Object = MibScalar
debugProfile_Item_o = _DebugProfile_Item_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 3),
    _DebugProfile_Item_o_Type()
)
debugProfile_Item_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugProfile_Item_o.setStatus("mandatory")


class _DebugProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type debugProfile_PhysicalAddress_Shelf based on Integer32"""
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


_DebugProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_DebugProfile_PhysicalAddress_Shelf_Object = MibScalar
debugProfile_PhysicalAddress_Shelf = _DebugProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 4),
    _DebugProfile_PhysicalAddress_Shelf_Type()
)
debugProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _DebugProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type debugProfile_PhysicalAddress_Slot based on Integer32"""
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


_DebugProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_DebugProfile_PhysicalAddress_Slot_Object = MibScalar
debugProfile_PhysicalAddress_Slot = _DebugProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 5),
    _DebugProfile_PhysicalAddress_Slot_Type()
)
debugProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_PhysicalAddress_Slot.setStatus("mandatory")
_DebugProfile_PhysicalAddress_ItemNumber_Type = Integer32
_DebugProfile_PhysicalAddress_ItemNumber_Object = MibScalar
debugProfile_PhysicalAddress_ItemNumber = _DebugProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 6),
    _DebugProfile_PhysicalAddress_ItemNumber_Type()
)
debugProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _DebugProfile_Active_Type(Integer32):
    """Custom type debugProfile_Active based on Integer32"""
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


_DebugProfile_Active_Type.__name__ = "Integer32"
_DebugProfile_Active_Object = MibScalar
debugProfile_Active = _DebugProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 7),
    _DebugProfile_Active_Type()
)
debugProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_Active.setStatus("mandatory")


class _DebugProfile_EnableCoreDump_Type(Integer32):
    """Custom type debugProfile_EnableCoreDump based on Integer32"""
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


_DebugProfile_EnableCoreDump_Type.__name__ = "Integer32"
_DebugProfile_EnableCoreDump_Object = MibScalar
debugProfile_EnableCoreDump = _DebugProfile_EnableCoreDump_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 8),
    _DebugProfile_EnableCoreDump_Type()
)
debugProfile_EnableCoreDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_EnableCoreDump.setStatus("mandatory")
_DebugProfile_CoreDumpServer_Type = DisplayString
_DebugProfile_CoreDumpServer_Object = MibScalar
debugProfile_CoreDumpServer = _DebugProfile_CoreDumpServer_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 9),
    _DebugProfile_CoreDumpServer_Type()
)
debugProfile_CoreDumpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_CoreDumpServer.setStatus("mandatory")


class _DebugProfile_EnableGdb_Type(Integer32):
    """Custom type debugProfile_EnableGdb based on Integer32"""
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


_DebugProfile_EnableGdb_Type.__name__ = "Integer32"
_DebugProfile_EnableGdb_Object = MibScalar
debugProfile_EnableGdb = _DebugProfile_EnableGdb_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 10),
    _DebugProfile_EnableGdb_Type()
)
debugProfile_EnableGdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_EnableGdb.setStatus("mandatory")
_DebugProfile_GdbHost_Type = DisplayString
_DebugProfile_GdbHost_Object = MibScalar
debugProfile_GdbHost = _DebugProfile_GdbHost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 11),
    _DebugProfile_GdbHost_Type()
)
debugProfile_GdbHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_GdbHost.setStatus("mandatory")


class _DebugProfile_CsTracking_Type(Integer32):
    """Custom type debugProfile_CsTracking based on Integer32"""
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


_DebugProfile_CsTracking_Type.__name__ = "Integer32"
_DebugProfile_CsTracking_Object = MibScalar
debugProfile_CsTracking = _DebugProfile_CsTracking_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 12),
    _DebugProfile_CsTracking_Type()
)
debugProfile_CsTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_CsTracking.setStatus("mandatory")
_DebugProfile_GenericField_Type = Integer32
_DebugProfile_GenericField_Object = MibScalar
debugProfile_GenericField = _DebugProfile_GenericField_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 13),
    _DebugProfile_GenericField_Type()
)
debugProfile_GenericField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_GenericField.setStatus("mandatory")
_DebugProfile_MinWarningCoreDump_Type = Integer32
_DebugProfile_MinWarningCoreDump_Object = MibScalar
debugProfile_MinWarningCoreDump = _DebugProfile_MinWarningCoreDump_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 14),
    _DebugProfile_MinWarningCoreDump_Type()
)
debugProfile_MinWarningCoreDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_MinWarningCoreDump.setStatus("mandatory")
_DebugProfile_MaxWarningCoreDump_Type = Integer32
_DebugProfile_MaxWarningCoreDump_Object = MibScalar
debugProfile_MaxWarningCoreDump = _DebugProfile_MaxWarningCoreDump_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 15),
    _DebugProfile_MaxWarningCoreDump_Type()
)
debugProfile_MaxWarningCoreDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_MaxWarningCoreDump.setStatus("mandatory")


class _DebugProfile_CoreDumpLocation_Type(Integer32):
    """Custom type debugProfile_CoreDumpLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("firstFlashThenNetwork", 4),
          ("flashOnly", 3),
          ("networkOnly", 2))
    )


_DebugProfile_CoreDumpLocation_Type.__name__ = "Integer32"
_DebugProfile_CoreDumpLocation_Object = MibScalar
debugProfile_CoreDumpLocation = _DebugProfile_CoreDumpLocation_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 16),
    _DebugProfile_CoreDumpLocation_Type()
)
debugProfile_CoreDumpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_CoreDumpLocation.setStatus("mandatory")


class _DebugProfile_FlashCoreOverwrite_Type(Integer32):
    """Custom type debugProfile_FlashCoreOverwrite based on Integer32"""
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


_DebugProfile_FlashCoreOverwrite_Type.__name__ = "Integer32"
_DebugProfile_FlashCoreOverwrite_Object = MibScalar
debugProfile_FlashCoreOverwrite = _DebugProfile_FlashCoreOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 17),
    _DebugProfile_FlashCoreOverwrite_Type()
)
debugProfile_FlashCoreOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_FlashCoreOverwrite.setStatus("mandatory")


class _DebugProfile_Action_o_Type(Integer32):
    """Custom type debugProfile_Action_o based on Integer32"""
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


_DebugProfile_Action_o_Type.__name__ = "Integer32"
_DebugProfile_Action_o_Object = MibScalar
debugProfile_Action_o = _DebugProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 18),
    _DebugProfile_Action_o_Type()
)
debugProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_Action_o.setStatus("mandatory")


class _DebugProfile_CoreDumpRipUpdate_Type(Integer32):
    """Custom type debugProfile_CoreDumpRipUpdate based on Integer32"""
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
        *(("updateHighFreq", 2),
          ("updateHigherFreq", 1),
          ("updateLowFreq", 4),
          ("updateLowerFreq", 5),
          ("updateMedFreq", 3),
          ("updateOff", 6))
    )


_DebugProfile_CoreDumpRipUpdate_Type.__name__ = "Integer32"
_DebugProfile_CoreDumpRipUpdate_Object = MibScalar
debugProfile_CoreDumpRipUpdate = _DebugProfile_CoreDumpRipUpdate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 19),
    _DebugProfile_CoreDumpRipUpdate_Type()
)
debugProfile_CoreDumpRipUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_CoreDumpRipUpdate.setStatus("mandatory")
_DebugProfile_CoredumpSourceAddress_Type = IpAddress
_DebugProfile_CoredumpSourceAddress_Object = MibScalar
debugProfile_CoredumpSourceAddress = _DebugProfile_CoredumpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 72, 1, 1, 20),
    _DebugProfile_CoredumpSourceAddress_Type()
)
debugProfile_CoredumpSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugProfile_CoredumpSourceAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDEBUG-MIB",
    **{"DisplayString": DisplayString,
       "mibdebugProfile": mibdebugProfile,
       "mibdebugProfileTable": mibdebugProfileTable,
       "mibdebugProfileEntry": mibdebugProfileEntry,
       "debugProfile-Shelf-o": debugProfile_Shelf_o,
       "debugProfile-Slot-o": debugProfile_Slot_o,
       "debugProfile-Item-o": debugProfile_Item_o,
       "debugProfile-PhysicalAddress-Shelf": debugProfile_PhysicalAddress_Shelf,
       "debugProfile-PhysicalAddress-Slot": debugProfile_PhysicalAddress_Slot,
       "debugProfile-PhysicalAddress-ItemNumber": debugProfile_PhysicalAddress_ItemNumber,
       "debugProfile-Active": debugProfile_Active,
       "debugProfile-EnableCoreDump": debugProfile_EnableCoreDump,
       "debugProfile-CoreDumpServer": debugProfile_CoreDumpServer,
       "debugProfile-EnableGdb": debugProfile_EnableGdb,
       "debugProfile-GdbHost": debugProfile_GdbHost,
       "debugProfile-CsTracking": debugProfile_CsTracking,
       "debugProfile-GenericField": debugProfile_GenericField,
       "debugProfile-MinWarningCoreDump": debugProfile_MinWarningCoreDump,
       "debugProfile-MaxWarningCoreDump": debugProfile_MaxWarningCoreDump,
       "debugProfile-CoreDumpLocation": debugProfile_CoreDumpLocation,
       "debugProfile-FlashCoreOverwrite": debugProfile_FlashCoreOverwrite,
       "debugProfile-Action-o": debugProfile_Action_o,
       "debugProfile-CoreDumpRipUpdate": debugProfile_CoreDumpRipUpdate,
       "debugProfile-CoredumpSourceAddress": debugProfile_CoredumpSourceAddress}
)
