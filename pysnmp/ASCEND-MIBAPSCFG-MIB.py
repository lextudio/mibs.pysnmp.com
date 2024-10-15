# SNMP MIB module (ASCEND-MIBAPSCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBAPSCFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:04 2024
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

_MibapsConfig_ObjectIdentity = ObjectIdentity
mibapsConfig = _MibapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 148)
)
_MibapsConfigTable_Object = MibTable
mibapsConfigTable = _MibapsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1)
)
if mibBuilder.loadTexts:
    mibapsConfigTable.setStatus("mandatory")
_MibapsConfigEntry_Object = MibTableRow
mibapsConfigEntry = _MibapsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1)
)
mibapsConfigEntry.setIndexNames(
    (0, "ASCEND-MIBAPSCFG-MIB", "apsConfig-Name"),
)
if mibBuilder.loadTexts:
    mibapsConfigEntry.setStatus("mandatory")
_ApsConfig_Name_Type = DisplayString
_ApsConfig_Name_Object = MibScalar
apsConfig_Name = _ApsConfig_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 1),
    _ApsConfig_Name_Type()
)
apsConfig_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsConfig_Name.setStatus("mandatory")


class _ApsConfig_Active_Type(Integer32):
    """Custom type apsConfig_Active based on Integer32"""
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


_ApsConfig_Active_Type.__name__ = "Integer32"
_ApsConfig_Active_Object = MibScalar
apsConfig_Active = _ApsConfig_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 2),
    _ApsConfig_Active_Type()
)
apsConfig_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_Active.setStatus("mandatory")


class _ApsConfig_LinearProtectionChannel_Shelf_Type(Integer32):
    """Custom type apsConfig_LinearProtectionChannel_Shelf based on Integer32"""
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


_ApsConfig_LinearProtectionChannel_Shelf_Type.__name__ = "Integer32"
_ApsConfig_LinearProtectionChannel_Shelf_Object = MibScalar
apsConfig_LinearProtectionChannel_Shelf = _ApsConfig_LinearProtectionChannel_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 3),
    _ApsConfig_LinearProtectionChannel_Shelf_Type()
)
apsConfig_LinearProtectionChannel_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_LinearProtectionChannel_Shelf.setStatus("mandatory")


class _ApsConfig_LinearProtectionChannel_Slot_Type(Integer32):
    """Custom type apsConfig_LinearProtectionChannel_Slot based on Integer32"""
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


_ApsConfig_LinearProtectionChannel_Slot_Type.__name__ = "Integer32"
_ApsConfig_LinearProtectionChannel_Slot_Object = MibScalar
apsConfig_LinearProtectionChannel_Slot = _ApsConfig_LinearProtectionChannel_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 4),
    _ApsConfig_LinearProtectionChannel_Slot_Type()
)
apsConfig_LinearProtectionChannel_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_LinearProtectionChannel_Slot.setStatus("mandatory")
_ApsConfig_LinearProtectionChannel_ItemNumber_Type = Integer32
_ApsConfig_LinearProtectionChannel_ItemNumber_Object = MibScalar
apsConfig_LinearProtectionChannel_ItemNumber = _ApsConfig_LinearProtectionChannel_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 5),
    _ApsConfig_LinearProtectionChannel_ItemNumber_Type()
)
apsConfig_LinearProtectionChannel_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_LinearProtectionChannel_ItemNumber.setStatus("mandatory")


class _ApsConfig_ProtectionMode_Type(Integer32):
    """Custom type apsConfig_ProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n-1-divide-n", 2),
          ("n-1-plus-1", 1))
    )


_ApsConfig_ProtectionMode_Type.__name__ = "Integer32"
_ApsConfig_ProtectionMode_Object = MibScalar
apsConfig_ProtectionMode = _ApsConfig_ProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 6),
    _ApsConfig_ProtectionMode_Type()
)
apsConfig_ProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_ProtectionMode.setStatus("mandatory")


class _ApsConfig_DirectionMode_Type(Integer32):
    """Custom type apsConfig_DirectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_ApsConfig_DirectionMode_Type.__name__ = "Integer32"
_ApsConfig_DirectionMode_Object = MibScalar
apsConfig_DirectionMode = _ApsConfig_DirectionMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 7),
    _ApsConfig_DirectionMode_Type()
)
apsConfig_DirectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_DirectionMode.setStatus("mandatory")


class _ApsConfig_RevertiveMode_Type(Integer32):
    """Custom type apsConfig_RevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 2),
          ("revertive", 1))
    )


_ApsConfig_RevertiveMode_Type.__name__ = "Integer32"
_ApsConfig_RevertiveMode_Object = MibScalar
apsConfig_RevertiveMode = _ApsConfig_RevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 8),
    _ApsConfig_RevertiveMode_Type()
)
apsConfig_RevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_RevertiveMode.setStatus("mandatory")
_ApsConfig_WtrTimerDuration_Type = Integer32
_ApsConfig_WtrTimerDuration_Object = MibScalar
apsConfig_WtrTimerDuration = _ApsConfig_WtrTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 9),
    _ApsConfig_WtrTimerDuration_Type()
)
apsConfig_WtrTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_WtrTimerDuration.setStatus("mandatory")
_ApsConfig_PsbfFailureTimerDuration_Type = Integer32
_ApsConfig_PsbfFailureTimerDuration_Object = MibScalar
apsConfig_PsbfFailureTimerDuration = _ApsConfig_PsbfFailureTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 10),
    _ApsConfig_PsbfFailureTimerDuration_Type()
)
apsConfig_PsbfFailureTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_PsbfFailureTimerDuration.setStatus("mandatory")
_ApsConfig_PsbfClearTimerDuration_Type = Integer32
_ApsConfig_PsbfClearTimerDuration_Object = MibScalar
apsConfig_PsbfClearTimerDuration = _ApsConfig_PsbfClearTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 11),
    _ApsConfig_PsbfClearTimerDuration_Type()
)
apsConfig_PsbfClearTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_PsbfClearTimerDuration.setStatus("mandatory")
_ApsConfig_ModeMismatchFailureTimerDuration_Type = Integer32
_ApsConfig_ModeMismatchFailureTimerDuration_Object = MibScalar
apsConfig_ModeMismatchFailureTimerDuration = _ApsConfig_ModeMismatchFailureTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 12),
    _ApsConfig_ModeMismatchFailureTimerDuration_Type()
)
apsConfig_ModeMismatchFailureTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_ModeMismatchFailureTimerDuration.setStatus("mandatory")
_ApsConfig_ModeMismatchClearTimerDuration_Type = Integer32
_ApsConfig_ModeMismatchClearTimerDuration_Object = MibScalar
apsConfig_ModeMismatchClearTimerDuration = _ApsConfig_ModeMismatchClearTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 13),
    _ApsConfig_ModeMismatchClearTimerDuration_Type()
)
apsConfig_ModeMismatchClearTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_ModeMismatchClearTimerDuration.setStatus("mandatory")
_ApsConfig_ChannelMismatchFailureTimerDuration_Type = Integer32
_ApsConfig_ChannelMismatchFailureTimerDuration_Object = MibScalar
apsConfig_ChannelMismatchFailureTimerDuration = _ApsConfig_ChannelMismatchFailureTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 14),
    _ApsConfig_ChannelMismatchFailureTimerDuration_Type()
)
apsConfig_ChannelMismatchFailureTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_ChannelMismatchFailureTimerDuration.setStatus("mandatory")
_ApsConfig_ChannelMismatchClearTimerDuration_Type = Integer32
_ApsConfig_ChannelMismatchClearTimerDuration_Object = MibScalar
apsConfig_ChannelMismatchClearTimerDuration = _ApsConfig_ChannelMismatchClearTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 15),
    _ApsConfig_ChannelMismatchClearTimerDuration_Type()
)
apsConfig_ChannelMismatchClearTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_ChannelMismatchClearTimerDuration.setStatus("mandatory")
_ApsConfig_FeplMismatchFailureTimerDuration_Type = Integer32
_ApsConfig_FeplMismatchFailureTimerDuration_Object = MibScalar
apsConfig_FeplMismatchFailureTimerDuration = _ApsConfig_FeplMismatchFailureTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 16),
    _ApsConfig_FeplMismatchFailureTimerDuration_Type()
)
apsConfig_FeplMismatchFailureTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_FeplMismatchFailureTimerDuration.setStatus("mandatory")
_ApsConfig_FeplMismatchClearTimerDuration_Type = Integer32
_ApsConfig_FeplMismatchClearTimerDuration_Object = MibScalar
apsConfig_FeplMismatchClearTimerDuration = _ApsConfig_FeplMismatchClearTimerDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 17),
    _ApsConfig_FeplMismatchClearTimerDuration_Type()
)
apsConfig_FeplMismatchClearTimerDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_FeplMismatchClearTimerDuration.setStatus("mandatory")
_ApsConfig_ProtectionChannelSignalDegradeExponent_Type = Integer32
_ApsConfig_ProtectionChannelSignalDegradeExponent_Object = MibScalar
apsConfig_ProtectionChannelSignalDegradeExponent = _ApsConfig_ProtectionChannelSignalDegradeExponent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 18),
    _ApsConfig_ProtectionChannelSignalDegradeExponent_Type()
)
apsConfig_ProtectionChannelSignalDegradeExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_ProtectionChannelSignalDegradeExponent.setStatus("mandatory")
_ApsConfig_ProtectionChannelSignalFailureExponent_Type = Integer32
_ApsConfig_ProtectionChannelSignalFailureExponent_Object = MibScalar
apsConfig_ProtectionChannelSignalFailureExponent = _ApsConfig_ProtectionChannelSignalFailureExponent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 19),
    _ApsConfig_ProtectionChannelSignalFailureExponent_Type()
)
apsConfig_ProtectionChannelSignalFailureExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_ProtectionChannelSignalFailureExponent.setStatus("mandatory")
_ApsConfig_WorkingChannelSignalDegradeExponent_Type = Integer32
_ApsConfig_WorkingChannelSignalDegradeExponent_Object = MibScalar
apsConfig_WorkingChannelSignalDegradeExponent = _ApsConfig_WorkingChannelSignalDegradeExponent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 20),
    _ApsConfig_WorkingChannelSignalDegradeExponent_Type()
)
apsConfig_WorkingChannelSignalDegradeExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_WorkingChannelSignalDegradeExponent.setStatus("mandatory")
_ApsConfig_WorkingChannelSignalFailureExponent_Type = Integer32
_ApsConfig_WorkingChannelSignalFailureExponent_Object = MibScalar
apsConfig_WorkingChannelSignalFailureExponent = _ApsConfig_WorkingChannelSignalFailureExponent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 21),
    _ApsConfig_WorkingChannelSignalFailureExponent_Type()
)
apsConfig_WorkingChannelSignalFailureExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_WorkingChannelSignalFailureExponent.setStatus("mandatory")


class _ApsConfig_Action_o_Type(Integer32):
    """Custom type apsConfig_Action_o based on Integer32"""
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


_ApsConfig_Action_o_Type.__name__ = "Integer32"
_ApsConfig_Action_o_Object = MibScalar
apsConfig_Action_o = _ApsConfig_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 148, 1, 1, 22),
    _ApsConfig_Action_o_Type()
)
apsConfig_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsConfig_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBAPSCFG-MIB",
    **{"DisplayString": DisplayString,
       "mibapsConfig": mibapsConfig,
       "mibapsConfigTable": mibapsConfigTable,
       "mibapsConfigEntry": mibapsConfigEntry,
       "apsConfig-Name": apsConfig_Name,
       "apsConfig-Active": apsConfig_Active,
       "apsConfig-LinearProtectionChannel-Shelf": apsConfig_LinearProtectionChannel_Shelf,
       "apsConfig-LinearProtectionChannel-Slot": apsConfig_LinearProtectionChannel_Slot,
       "apsConfig-LinearProtectionChannel-ItemNumber": apsConfig_LinearProtectionChannel_ItemNumber,
       "apsConfig-ProtectionMode": apsConfig_ProtectionMode,
       "apsConfig-DirectionMode": apsConfig_DirectionMode,
       "apsConfig-RevertiveMode": apsConfig_RevertiveMode,
       "apsConfig-WtrTimerDuration": apsConfig_WtrTimerDuration,
       "apsConfig-PsbfFailureTimerDuration": apsConfig_PsbfFailureTimerDuration,
       "apsConfig-PsbfClearTimerDuration": apsConfig_PsbfClearTimerDuration,
       "apsConfig-ModeMismatchFailureTimerDuration": apsConfig_ModeMismatchFailureTimerDuration,
       "apsConfig-ModeMismatchClearTimerDuration": apsConfig_ModeMismatchClearTimerDuration,
       "apsConfig-ChannelMismatchFailureTimerDuration": apsConfig_ChannelMismatchFailureTimerDuration,
       "apsConfig-ChannelMismatchClearTimerDuration": apsConfig_ChannelMismatchClearTimerDuration,
       "apsConfig-FeplMismatchFailureTimerDuration": apsConfig_FeplMismatchFailureTimerDuration,
       "apsConfig-FeplMismatchClearTimerDuration": apsConfig_FeplMismatchClearTimerDuration,
       "apsConfig-ProtectionChannelSignalDegradeExponent": apsConfig_ProtectionChannelSignalDegradeExponent,
       "apsConfig-ProtectionChannelSignalFailureExponent": apsConfig_ProtectionChannelSignalFailureExponent,
       "apsConfig-WorkingChannelSignalDegradeExponent": apsConfig_WorkingChannelSignalDegradeExponent,
       "apsConfig-WorkingChannelSignalFailureExponent": apsConfig_WorkingChannelSignalFailureExponent,
       "apsConfig-Action-o": apsConfig_Action_o}
)
