# SNMP MIB module (ASCEND-MIBAPSSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBAPSSTAT-MIB
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

_MibapsStat_ObjectIdentity = ObjectIdentity
mibapsStat = _MibapsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 149)
)
_MibapsStatTable_Object = MibTable
mibapsStatTable = _MibapsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1)
)
if mibBuilder.loadTexts:
    mibapsStatTable.setStatus("mandatory")
_MibapsStatEntry_Object = MibTableRow
mibapsStatEntry = _MibapsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1)
)
mibapsStatEntry.setIndexNames(
    (0, "ASCEND-MIBAPSSTAT-MIB", "apsStat-Name"),
)
if mibBuilder.loadTexts:
    mibapsStatEntry.setStatus("mandatory")
_ApsStat_Name_Type = DisplayString
_ApsStat_Name_Object = MibScalar
apsStat_Name = _ApsStat_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 1),
    _ApsStat_Name_Type()
)
apsStat_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_Name.setStatus("mandatory")


class _ApsStat_ProtectionChannel_Shelf_Type(Integer32):
    """Custom type apsStat_ProtectionChannel_Shelf based on Integer32"""
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


_ApsStat_ProtectionChannel_Shelf_Type.__name__ = "Integer32"
_ApsStat_ProtectionChannel_Shelf_Object = MibScalar
apsStat_ProtectionChannel_Shelf = _ApsStat_ProtectionChannel_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 2),
    _ApsStat_ProtectionChannel_Shelf_Type()
)
apsStat_ProtectionChannel_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsStat_ProtectionChannel_Shelf.setStatus("mandatory")


class _ApsStat_ProtectionChannel_Slot_Type(Integer32):
    """Custom type apsStat_ProtectionChannel_Slot based on Integer32"""
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


_ApsStat_ProtectionChannel_Slot_Type.__name__ = "Integer32"
_ApsStat_ProtectionChannel_Slot_Object = MibScalar
apsStat_ProtectionChannel_Slot = _ApsStat_ProtectionChannel_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 3),
    _ApsStat_ProtectionChannel_Slot_Type()
)
apsStat_ProtectionChannel_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsStat_ProtectionChannel_Slot.setStatus("mandatory")
_ApsStat_ProtectionChannel_ItemNumber_Type = Integer32
_ApsStat_ProtectionChannel_ItemNumber_Object = MibScalar
apsStat_ProtectionChannel_ItemNumber = _ApsStat_ProtectionChannel_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 4),
    _ApsStat_ProtectionChannel_ItemNumber_Type()
)
apsStat_ProtectionChannel_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsStat_ProtectionChannel_ItemNumber.setStatus("mandatory")


class _ApsStat_ProtectionMode_Type(Integer32):
    """Custom type apsStat_ProtectionMode based on Integer32"""
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


_ApsStat_ProtectionMode_Type.__name__ = "Integer32"
_ApsStat_ProtectionMode_Object = MibScalar
apsStat_ProtectionMode = _ApsStat_ProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 5),
    _ApsStat_ProtectionMode_Type()
)
apsStat_ProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_ProtectionMode.setStatus("mandatory")


class _ApsStat_DirectionMode_Type(Integer32):
    """Custom type apsStat_DirectionMode based on Integer32"""
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


_ApsStat_DirectionMode_Type.__name__ = "Integer32"
_ApsStat_DirectionMode_Object = MibScalar
apsStat_DirectionMode = _ApsStat_DirectionMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 6),
    _ApsStat_DirectionMode_Type()
)
apsStat_DirectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_DirectionMode.setStatus("mandatory")


class _ApsStat_RevertiveMode_Type(Integer32):
    """Custom type apsStat_RevertiveMode based on Integer32"""
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


_ApsStat_RevertiveMode_Type.__name__ = "Integer32"
_ApsStat_RevertiveMode_Object = MibScalar
apsStat_RevertiveMode = _ApsStat_RevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 7),
    _ApsStat_RevertiveMode_Type()
)
apsStat_RevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_RevertiveMode.setStatus("mandatory")


class _ApsStat_ApsState_Type(Integer32):
    """Custom type apsStat_ApsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onProtection", 2),
          ("onWorking", 3),
          ("unknown", 1))
    )


_ApsStat_ApsState_Type.__name__ = "Integer32"
_ApsStat_ApsState_Object = MibScalar
apsStat_ApsState = _ApsStat_ApsState_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 8),
    _ApsStat_ApsState_Type()
)
apsStat_ApsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_ApsState.setStatus("mandatory")
_ApsStat_RecvPsbfCount_Type = Integer32
_ApsStat_RecvPsbfCount_Object = MibScalar
apsStat_RecvPsbfCount = _ApsStat_RecvPsbfCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 29),
    _ApsStat_RecvPsbfCount_Type()
)
apsStat_RecvPsbfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_RecvPsbfCount.setStatus("mandatory")
_ApsStat_RecvModeMismatchCount_Type = Integer32
_ApsStat_RecvModeMismatchCount_Object = MibScalar
apsStat_RecvModeMismatchCount = _ApsStat_RecvModeMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 30),
    _ApsStat_RecvModeMismatchCount_Type()
)
apsStat_RecvModeMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_RecvModeMismatchCount.setStatus("mandatory")
_ApsStat_RecvChannelMismatchCount_Type = Integer32
_ApsStat_RecvChannelMismatchCount_Object = MibScalar
apsStat_RecvChannelMismatchCount = _ApsStat_RecvChannelMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 31),
    _ApsStat_RecvChannelMismatchCount_Type()
)
apsStat_RecvChannelMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_RecvChannelMismatchCount.setStatus("mandatory")
_ApsStat_RecvFeplCount_Type = Integer32
_ApsStat_RecvFeplCount_Object = MibScalar
apsStat_RecvFeplCount = _ApsStat_RecvFeplCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 32),
    _ApsStat_RecvFeplCount_Type()
)
apsStat_RecvFeplCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_RecvFeplCount.setStatus("mandatory")


class _ApsStat_ExtraTrafficFlag_Type(Integer32):
    """Custom type apsStat_ExtraTrafficFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ApsStat_ExtraTrafficFlag_Type.__name__ = "Integer32"
_ApsStat_ExtraTrafficFlag_Object = MibScalar
apsStat_ExtraTrafficFlag = _ApsStat_ExtraTrafficFlag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 33),
    _ApsStat_ExtraTrafficFlag_Type()
)
apsStat_ExtraTrafficFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_ExtraTrafficFlag.setStatus("mandatory")
_ApsStat_RxK1ByteValue_Type = DisplayString
_ApsStat_RxK1ByteValue_Object = MibScalar
apsStat_RxK1ByteValue = _ApsStat_RxK1ByteValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 34),
    _ApsStat_RxK1ByteValue_Type()
)
apsStat_RxK1ByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_RxK1ByteValue.setStatus("mandatory")
_ApsStat_RxK2ByteValue_Type = DisplayString
_ApsStat_RxK2ByteValue_Object = MibScalar
apsStat_RxK2ByteValue = _ApsStat_RxK2ByteValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 35),
    _ApsStat_RxK2ByteValue_Type()
)
apsStat_RxK2ByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_RxK2ByteValue.setStatus("mandatory")
_ApsStat_TxK1ByteValue_Type = DisplayString
_ApsStat_TxK1ByteValue_Object = MibScalar
apsStat_TxK1ByteValue = _ApsStat_TxK1ByteValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 36),
    _ApsStat_TxK1ByteValue_Type()
)
apsStat_TxK1ByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_TxK1ByteValue.setStatus("mandatory")
_ApsStat_TxK2ByteValue_Type = DisplayString
_ApsStat_TxK2ByteValue_Object = MibScalar
apsStat_TxK2ByteValue = _ApsStat_TxK2ByteValue_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 37),
    _ApsStat_TxK2ByteValue_Type()
)
apsStat_TxK2ByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_TxK2ByteValue.setStatus("mandatory")


class _ApsStat_Action_o_Type(Integer32):
    """Custom type apsStat_Action_o based on Integer32"""
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


_ApsStat_Action_o_Type.__name__ = "Integer32"
_ApsStat_Action_o_Object = MibScalar
apsStat_Action_o = _ApsStat_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 42),
    _ApsStat_Action_o_Type()
)
apsStat_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsStat_Action_o.setStatus("mandatory")


class _ApsStat_WorkingChannel_Shelf_Type(Integer32):
    """Custom type apsStat_WorkingChannel_Shelf based on Integer32"""
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


_ApsStat_WorkingChannel_Shelf_Type.__name__ = "Integer32"
_ApsStat_WorkingChannel_Shelf_Object = MibScalar
apsStat_WorkingChannel_Shelf = _ApsStat_WorkingChannel_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 43),
    _ApsStat_WorkingChannel_Shelf_Type()
)
apsStat_WorkingChannel_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsStat_WorkingChannel_Shelf.setStatus("mandatory")


class _ApsStat_WorkingChannel_Slot_Type(Integer32):
    """Custom type apsStat_WorkingChannel_Slot based on Integer32"""
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


_ApsStat_WorkingChannel_Slot_Type.__name__ = "Integer32"
_ApsStat_WorkingChannel_Slot_Object = MibScalar
apsStat_WorkingChannel_Slot = _ApsStat_WorkingChannel_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 44),
    _ApsStat_WorkingChannel_Slot_Type()
)
apsStat_WorkingChannel_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsStat_WorkingChannel_Slot.setStatus("mandatory")
_ApsStat_WorkingChannel_ItemNumber_Type = Integer32
_ApsStat_WorkingChannel_ItemNumber_Object = MibScalar
apsStat_WorkingChannel_ItemNumber = _ApsStat_WorkingChannel_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 45),
    _ApsStat_WorkingChannel_ItemNumber_Type()
)
apsStat_WorkingChannel_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsStat_WorkingChannel_ItemNumber.setStatus("mandatory")


class _ApsStat_BridgeStatus_Type(Integer32):
    """Custom type apsStat_BridgeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ApsStat_BridgeStatus_Type.__name__ = "Integer32"
_ApsStat_BridgeStatus_Object = MibScalar
apsStat_BridgeStatus = _ApsStat_BridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 47),
    _ApsStat_BridgeStatus_Type()
)
apsStat_BridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_BridgeStatus.setStatus("mandatory")
_ApsStat_LastSwitchTime_Type = Integer32
_ApsStat_LastSwitchTime_Object = MibScalar
apsStat_LastSwitchTime = _ApsStat_LastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 48),
    _ApsStat_LastSwitchTime_Type()
)
apsStat_LastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_LastSwitchTime.setStatus("mandatory")
_ApsStat_SwitchCount_Type = Integer32
_ApsStat_SwitchCount_Object = MibScalar
apsStat_SwitchCount = _ApsStat_SwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 49),
    _ApsStat_SwitchCount_Type()
)
apsStat_SwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_SwitchCount.setStatus("mandatory")
_ApsStat_ApsCfgCreationTime_Type = Integer32
_ApsStat_ApsCfgCreationTime_Object = MibScalar
apsStat_ApsCfgCreationTime = _ApsStat_ApsCfgCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 50),
    _ApsStat_ApsCfgCreationTime_Type()
)
apsStat_ApsCfgCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_ApsCfgCreationTime.setStatus("mandatory")
_ApsStat_NumberOfChannels_Type = Integer32
_ApsStat_NumberOfChannels_Object = MibScalar
apsStat_NumberOfChannels = _ApsStat_NumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 51),
    _ApsStat_NumberOfChannels_Type()
)
apsStat_NumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_NumberOfChannels.setStatus("mandatory")


class _ApsStat_PsbfFailure_Type(Integer32):
    """Custom type apsStat_PsbfFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ApsStat_PsbfFailure_Type.__name__ = "Integer32"
_ApsStat_PsbfFailure_Object = MibScalar
apsStat_PsbfFailure = _ApsStat_PsbfFailure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 52),
    _ApsStat_PsbfFailure_Type()
)
apsStat_PsbfFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_PsbfFailure.setStatus("mandatory")


class _ApsStat_ChannelMismatchFailure_Type(Integer32):
    """Custom type apsStat_ChannelMismatchFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ApsStat_ChannelMismatchFailure_Type.__name__ = "Integer32"
_ApsStat_ChannelMismatchFailure_Object = MibScalar
apsStat_ChannelMismatchFailure = _ApsStat_ChannelMismatchFailure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 53),
    _ApsStat_ChannelMismatchFailure_Type()
)
apsStat_ChannelMismatchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_ChannelMismatchFailure.setStatus("mandatory")


class _ApsStat_ModeMismatchFailure_Type(Integer32):
    """Custom type apsStat_ModeMismatchFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ApsStat_ModeMismatchFailure_Type.__name__ = "Integer32"
_ApsStat_ModeMismatchFailure_Object = MibScalar
apsStat_ModeMismatchFailure = _ApsStat_ModeMismatchFailure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 54),
    _ApsStat_ModeMismatchFailure_Type()
)
apsStat_ModeMismatchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_ModeMismatchFailure.setStatus("mandatory")


class _ApsStat_FeplFailure_Type(Integer32):
    """Custom type apsStat_FeplFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ApsStat_FeplFailure_Type.__name__ = "Integer32"
_ApsStat_FeplFailure_Object = MibScalar
apsStat_FeplFailure = _ApsStat_FeplFailure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 55),
    _ApsStat_FeplFailure_Type()
)
apsStat_FeplFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStat_FeplFailure.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBAPSSTAT-MIB",
    **{"DisplayString": DisplayString,
       "mibapsStat": mibapsStat,
       "mibapsStatTable": mibapsStatTable,
       "mibapsStatEntry": mibapsStatEntry,
       "apsStat-Name": apsStat_Name,
       "apsStat-ProtectionChannel-Shelf": apsStat_ProtectionChannel_Shelf,
       "apsStat-ProtectionChannel-Slot": apsStat_ProtectionChannel_Slot,
       "apsStat-ProtectionChannel-ItemNumber": apsStat_ProtectionChannel_ItemNumber,
       "apsStat-ProtectionMode": apsStat_ProtectionMode,
       "apsStat-DirectionMode": apsStat_DirectionMode,
       "apsStat-RevertiveMode": apsStat_RevertiveMode,
       "apsStat-ApsState": apsStat_ApsState,
       "apsStat-RecvPsbfCount": apsStat_RecvPsbfCount,
       "apsStat-RecvModeMismatchCount": apsStat_RecvModeMismatchCount,
       "apsStat-RecvChannelMismatchCount": apsStat_RecvChannelMismatchCount,
       "apsStat-RecvFeplCount": apsStat_RecvFeplCount,
       "apsStat-ExtraTrafficFlag": apsStat_ExtraTrafficFlag,
       "apsStat-RxK1ByteValue": apsStat_RxK1ByteValue,
       "apsStat-RxK2ByteValue": apsStat_RxK2ByteValue,
       "apsStat-TxK1ByteValue": apsStat_TxK1ByteValue,
       "apsStat-TxK2ByteValue": apsStat_TxK2ByteValue,
       "apsStat-Action-o": apsStat_Action_o,
       "apsStat-WorkingChannel-Shelf": apsStat_WorkingChannel_Shelf,
       "apsStat-WorkingChannel-Slot": apsStat_WorkingChannel_Slot,
       "apsStat-WorkingChannel-ItemNumber": apsStat_WorkingChannel_ItemNumber,
       "apsStat-BridgeStatus": apsStat_BridgeStatus,
       "apsStat-LastSwitchTime": apsStat_LastSwitchTime,
       "apsStat-SwitchCount": apsStat_SwitchCount,
       "apsStat-ApsCfgCreationTime": apsStat_ApsCfgCreationTime,
       "apsStat-NumberOfChannels": apsStat_NumberOfChannels,
       "apsStat-PsbfFailure": apsStat_PsbfFailure,
       "apsStat-ChannelMismatchFailure": apsStat_ChannelMismatchFailure,
       "apsStat-ModeMismatchFailure": apsStat_ModeMismatchFailure,
       "apsStat-FeplFailure": apsStat_FeplFailure}
)
