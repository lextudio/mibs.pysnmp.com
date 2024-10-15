# SNMP MIB module (ANS-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANS-EQUIPMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:57 2024
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

(RowPointer,
 RowStatus,
 mlpmpR115) = mibBuilder.importSymbols(
    "ANS-COMMON-MIB",
    "RowPointer",
    "RowStatus",
    "mlpmpR115")

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



class AnsSubrackType(Integer32):
    """Custom type AnsSubrackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("badvalue", -1),
          ("concentrator", 7),
          ("wbas", 9))
    )





class ProtectedBoardType(Integer32):
    """Custom type ProtectedBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wbas-rn", 1)
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3)
)
_SystemNode_ObjectIdentity = ObjectIdentity
systemNode = _SystemNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1)
)
_AnsSystemNodeTable_Object = MibTable
ansSystemNodeTable = _AnsSystemNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ansSystemNodeTable.setStatus("mandatory")
_AnsSystemNodeEntry_Object = MibTableRow
ansSystemNodeEntry = _AnsSystemNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3, 1)
)
ansSystemNodeEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansSystemNodeIndex"),
)
if mibBuilder.loadTexts:
    ansSystemNodeEntry.setStatus("mandatory")
_AnsSystemNodeIndex_Type = Integer32
_AnsSystemNodeIndex_Object = MibTableColumn
ansSystemNodeIndex = _AnsSystemNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3, 1, 1),
    _AnsSystemNodeIndex_Type()
)
ansSystemNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSystemNodeIndex.setStatus("mandatory")
_AnsSystemNodeName_Type = DisplayString
_AnsSystemNodeName_Object = MibTableColumn
ansSystemNodeName = _AnsSystemNodeName_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3, 1, 2),
    _AnsSystemNodeName_Type()
)
ansSystemNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSystemNodeName.setStatus("mandatory")


class _AnsSystemNodeOrigin_Type(Integer32):
    """Custom type ansSystemNodeOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("native", 1)
    )


_AnsSystemNodeOrigin_Type.__name__ = "Integer32"
_AnsSystemNodeOrigin_Object = MibTableColumn
ansSystemNodeOrigin = _AnsSystemNodeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3, 1, 3),
    _AnsSystemNodeOrigin_Type()
)
ansSystemNodeOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSystemNodeOrigin.setStatus("mandatory")
_AnsSystemNodeLocation_Type = DisplayString
_AnsSystemNodeLocation_Object = MibTableColumn
ansSystemNodeLocation = _AnsSystemNodeLocation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3, 1, 4),
    _AnsSystemNodeLocation_Type()
)
ansSystemNodeLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSystemNodeLocation.setStatus("mandatory")


class _AnsSystemNodeClockSource_Type(Integer32):
    """Custom type ansSystemNodeClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("net-clock-source", 2),
          ("undefined", 1))
    )


_AnsSystemNodeClockSource_Type.__name__ = "Integer32"
_AnsSystemNodeClockSource_Object = MibTableColumn
ansSystemNodeClockSource = _AnsSystemNodeClockSource_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3, 1, 5),
    _AnsSystemNodeClockSource_Type()
)
ansSystemNodeClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSystemNodeClockSource.setStatus("mandatory")
_AnsSystemNodeRowStatus_Type = RowStatus
_AnsSystemNodeRowStatus_Object = MibTableColumn
ansSystemNodeRowStatus = _AnsSystemNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 1, 3, 1, 6),
    _AnsSystemNodeRowStatus_Type()
)
ansSystemNodeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSystemNodeRowStatus.setStatus("mandatory")
_Subrack_ObjectIdentity = ObjectIdentity
subrack = _Subrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2)
)
_AnsSubrackTable_Object = MibTable
ansSubrackTable = _AnsSubrackTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ansSubrackTable.setStatus("mandatory")
_AnsSubrackEntry_Object = MibTableRow
ansSubrackEntry = _AnsSubrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1)
)
ansSubrackEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansSubrackSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansSubrackIndex"),
)
if mibBuilder.loadTexts:
    ansSubrackEntry.setStatus("mandatory")
_AnsSubrackSystemNodeIndex_Type = Integer32
_AnsSubrackSystemNodeIndex_Object = MibTableColumn
ansSubrackSystemNodeIndex = _AnsSubrackSystemNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 1),
    _AnsSubrackSystemNodeIndex_Type()
)
ansSubrackSystemNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSubrackSystemNodeIndex.setStatus("mandatory")
_AnsSubrackIndex_Type = Integer32
_AnsSubrackIndex_Object = MibTableColumn
ansSubrackIndex = _AnsSubrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 2),
    _AnsSubrackIndex_Type()
)
ansSubrackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSubrackIndex.setStatus("mandatory")
_AnsSubrackName_Type = DisplayString
_AnsSubrackName_Object = MibTableColumn
ansSubrackName = _AnsSubrackName_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 3),
    _AnsSubrackName_Type()
)
ansSubrackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSubrackName.setStatus("mandatory")


class _AnsSubrackHwId_Type(DisplayString):
    """Custom type ansSubrackHwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(46, 46),
    )


_AnsSubrackHwId_Type.__name__ = "DisplayString"
_AnsSubrackHwId_Object = MibTableColumn
ansSubrackHwId = _AnsSubrackHwId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 4),
    _AnsSubrackHwId_Type()
)
ansSubrackHwId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSubrackHwId.setStatus("mandatory")
_AnsSubrackLocation_Type = DisplayString
_AnsSubrackLocation_Object = MibTableColumn
ansSubrackLocation = _AnsSubrackLocation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 5),
    _AnsSubrackLocation_Type()
)
ansSubrackLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSubrackLocation.setStatus("mandatory")
_AnsSubrackType_Type = AnsSubrackType
_AnsSubrackType_Object = MibTableColumn
ansSubrackType = _AnsSubrackType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 6),
    _AnsSubrackType_Type()
)
ansSubrackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSubrackType.setStatus("mandatory")


class _AnsSubrackProtectionState_Type(Integer32):
    """Custom type ansSubrackProtectionState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-protected", 1),
          ("protected", 2))
    )


_AnsSubrackProtectionState_Type.__name__ = "Integer32"
_AnsSubrackProtectionState_Object = MibTableColumn
ansSubrackProtectionState = _AnsSubrackProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 7),
    _AnsSubrackProtectionState_Type()
)
ansSubrackProtectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSubrackProtectionState.setStatus("mandatory")
_AnsSubrackProtectionScheme_Type = DisplayString
_AnsSubrackProtectionScheme_Object = MibTableColumn
ansSubrackProtectionScheme = _AnsSubrackProtectionScheme_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 8),
    _AnsSubrackProtectionScheme_Type()
)
ansSubrackProtectionScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSubrackProtectionScheme.setStatus("mandatory")
_AnsSubrackNoOfSlots_Type = Integer32
_AnsSubrackNoOfSlots_Object = MibTableColumn
ansSubrackNoOfSlots = _AnsSubrackNoOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 9),
    _AnsSubrackNoOfSlots_Type()
)
ansSubrackNoOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSubrackNoOfSlots.setStatus("mandatory")


class _AnsSubrackAlarmStatus_Type(Integer32):
    """Custom type ansSubrackAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnsSubrackAlarmStatus_Type.__name__ = "Integer32"
_AnsSubrackAlarmStatus_Object = MibTableColumn
ansSubrackAlarmStatus = _AnsSubrackAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 10),
    _AnsSubrackAlarmStatus_Type()
)
ansSubrackAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSubrackAlarmStatus.setStatus("mandatory")
_AnsSubrackRowStatus_Type = RowStatus
_AnsSubrackRowStatus_Object = MibTableColumn
ansSubrackRowStatus = _AnsSubrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 2, 2, 1, 11),
    _AnsSubrackRowStatus_Type()
)
ansSubrackRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSubrackRowStatus.setStatus("mandatory")
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3)
)
_AnsSlotTable_Object = MibTable
ansSlotTable = _AnsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ansSlotTable.setStatus("mandatory")
_AnsSlotEntry_Object = MibTableRow
ansSlotEntry = _AnsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1)
)
ansSlotEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansSlotSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansSlotSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansSlotPosition"),
)
if mibBuilder.loadTexts:
    ansSlotEntry.setStatus("mandatory")
_AnsSlotSystemNodeIndex_Type = Integer32
_AnsSlotSystemNodeIndex_Object = MibTableColumn
ansSlotSystemNodeIndex = _AnsSlotSystemNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 1),
    _AnsSlotSystemNodeIndex_Type()
)
ansSlotSystemNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSlotSystemNodeIndex.setStatus("mandatory")
_AnsSlotSubrackIndex_Type = Integer32
_AnsSlotSubrackIndex_Object = MibTableColumn
ansSlotSubrackIndex = _AnsSlotSubrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 2),
    _AnsSlotSubrackIndex_Type()
)
ansSlotSubrackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSlotSubrackIndex.setStatus("mandatory")
_AnsSlotPosition_Type = Integer32
_AnsSlotPosition_Object = MibTableColumn
ansSlotPosition = _AnsSlotPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 3),
    _AnsSlotPosition_Type()
)
ansSlotPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSlotPosition.setStatus("mandatory")


class _AnsSlotConfiguredBoardId_Type(DisplayString):
    """Custom type ansSlotConfiguredBoardId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_AnsSlotConfiguredBoardId_Type.__name__ = "DisplayString"
_AnsSlotConfiguredBoardId_Object = MibTableColumn
ansSlotConfiguredBoardId = _AnsSlotConfiguredBoardId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 4),
    _AnsSlotConfiguredBoardId_Type()
)
ansSlotConfiguredBoardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSlotConfiguredBoardId.setStatus("mandatory")


class _AnsSlotInsertedBoardId_Type(DisplayString):
    """Custom type ansSlotInsertedBoardId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_AnsSlotInsertedBoardId_Type.__name__ = "DisplayString"
_AnsSlotInsertedBoardId_Object = MibTableColumn
ansSlotInsertedBoardId = _AnsSlotInsertedBoardId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 5),
    _AnsSlotInsertedBoardId_Type()
)
ansSlotInsertedBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSlotInsertedBoardId.setStatus("mandatory")


class _AnsSlotManagementStatus_Type(Integer32):
    """Custom type ansSlotManagementStatus based on Integer32"""
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
        *(("configBoard", 5),
          ("configEmpty", 4),
          ("managed", 1),
          ("unconfigEmpty", 3),
          ("unmanaged", 2))
    )


_AnsSlotManagementStatus_Type.__name__ = "Integer32"
_AnsSlotManagementStatus_Object = MibTableColumn
ansSlotManagementStatus = _AnsSlotManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 6),
    _AnsSlotManagementStatus_Type()
)
ansSlotManagementStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansSlotManagementStatus.setStatus("mandatory")


class _AnsSlotFallback_Type(Integer32):
    """Custom type ansSlotFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AnsSlotFallback_Type.__name__ = "Integer32"
_AnsSlotFallback_Object = MibTableColumn
ansSlotFallback = _AnsSlotFallback_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 7),
    _AnsSlotFallback_Type()
)
ansSlotFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSlotFallback.setStatus("mandatory")


class _AnsSlotAlarmStatus_Type(Integer32):
    """Custom type ansSlotAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnsSlotAlarmStatus_Type.__name__ = "Integer32"
_AnsSlotAlarmStatus_Object = MibTableColumn
ansSlotAlarmStatus = _AnsSlotAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 3, 1, 1, 8),
    _AnsSlotAlarmStatus_Type()
)
ansSlotAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansSlotAlarmStatus.setStatus("mandatory")
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4)
)
_AnsBoardTable_Object = MibTable
ansBoardTable = _AnsBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ansBoardTable.setStatus("mandatory")
_AnsBoardEntry_Object = MibTableRow
ansBoardEntry = _AnsBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1)
)
ansBoardEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
)
if mibBuilder.loadTexts:
    ansBoardEntry.setStatus("mandatory")
_AnsBoardSystemNodeIndex_Type = Integer32
_AnsBoardSystemNodeIndex_Object = MibTableColumn
ansBoardSystemNodeIndex = _AnsBoardSystemNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 1),
    _AnsBoardSystemNodeIndex_Type()
)
ansBoardSystemNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardSystemNodeIndex.setStatus("mandatory")
_AnsBoardSubrackIndex_Type = Integer32
_AnsBoardSubrackIndex_Object = MibTableColumn
ansBoardSubrackIndex = _AnsBoardSubrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 2),
    _AnsBoardSubrackIndex_Type()
)
ansBoardSubrackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardSubrackIndex.setStatus("mandatory")
_AnsBoardPosition_Type = Integer32
_AnsBoardPosition_Object = MibTableColumn
ansBoardPosition = _AnsBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 3),
    _AnsBoardPosition_Type()
)
ansBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardPosition.setStatus("mandatory")


class _AnsBoardType_Type(DisplayString):
    """Custom type ansBoardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AnsBoardType_Type.__name__ = "DisplayString"
_AnsBoardType_Object = MibTableColumn
ansBoardType = _AnsBoardType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 4),
    _AnsBoardType_Type()
)
ansBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardType.setStatus("mandatory")


class _AnsBoardHwId_Type(DisplayString):
    """Custom type ansBoardHwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(46, 46),
    )


_AnsBoardHwId_Type.__name__ = "DisplayString"
_AnsBoardHwId_Object = MibTableColumn
ansBoardHwId = _AnsBoardHwId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 5),
    _AnsBoardHwId_Type()
)
ansBoardHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardHwId.setStatus("mandatory")


class _AnsBoardSwIdActive_Type(DisplayString):
    """Custom type ansBoardSwIdActive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_AnsBoardSwIdActive_Type.__name__ = "DisplayString"
_AnsBoardSwIdActive_Object = MibTableColumn
ansBoardSwIdActive = _AnsBoardSwIdActive_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 6),
    _AnsBoardSwIdActive_Type()
)
ansBoardSwIdActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardSwIdActive.setStatus("mandatory")


class _AnsBoardSwIdPassive_Type(DisplayString):
    """Custom type ansBoardSwIdPassive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_AnsBoardSwIdPassive_Type.__name__ = "DisplayString"
_AnsBoardSwIdPassive_Object = MibTableColumn
ansBoardSwIdPassive = _AnsBoardSwIdPassive_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 7),
    _AnsBoardSwIdPassive_Type()
)
ansBoardSwIdPassive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardSwIdPassive.setStatus("mandatory")


class _AnsBoardOperStatus_Type(Integer32):
    """Custom type ansBoardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AnsBoardOperStatus_Type.__name__ = "Integer32"
_AnsBoardOperStatus_Object = MibTableColumn
ansBoardOperStatus = _AnsBoardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 8),
    _AnsBoardOperStatus_Type()
)
ansBoardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardOperStatus.setStatus("mandatory")


class _AnsBoardAdminStatus_Type(Integer32):
    """Custom type ansBoardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_AnsBoardAdminStatus_Type.__name__ = "Integer32"
_AnsBoardAdminStatus_Object = MibTableColumn
ansBoardAdminStatus = _AnsBoardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 9),
    _AnsBoardAdminStatus_Type()
)
ansBoardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansBoardAdminStatus.setStatus("mandatory")


class _AnsBoardRestart_Type(Integer32):
    """Custom type ansBoardRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("restart", 2))
    )


_AnsBoardRestart_Type.__name__ = "Integer32"
_AnsBoardRestart_Object = MibTableColumn
ansBoardRestart = _AnsBoardRestart_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 10),
    _AnsBoardRestart_Type()
)
ansBoardRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansBoardRestart.setStatus("mandatory")


class _AnsBoardLedStatus_Type(Integer32):
    """Custom type ansBoardLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("redOff", 1),
          ("redOn", 2))
    )


_AnsBoardLedStatus_Type.__name__ = "Integer32"
_AnsBoardLedStatus_Object = MibTableColumn
ansBoardLedStatus = _AnsBoardLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 11),
    _AnsBoardLedStatus_Type()
)
ansBoardLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardLedStatus.setStatus("mandatory")


class _AnsBoardStandbyStatus_Type(Integer32):
    """Custom type ansBoardStandbyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cold-standby", 2),
          ("null", 3),
          ("providing-service", 1))
    )


_AnsBoardStandbyStatus_Type.__name__ = "Integer32"
_AnsBoardStandbyStatus_Object = MibTableColumn
ansBoardStandbyStatus = _AnsBoardStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 12),
    _AnsBoardStandbyStatus_Type()
)
ansBoardStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardStandbyStatus.setStatus("mandatory")


class _AnsBoardAlarmStatus_Type(Integer32):
    """Custom type ansBoardAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AnsBoardAlarmStatus_Type.__name__ = "Integer32"
_AnsBoardAlarmStatus_Object = MibTableColumn
ansBoardAlarmStatus = _AnsBoardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 13),
    _AnsBoardAlarmStatus_Type()
)
ansBoardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardAlarmStatus.setStatus("mandatory")


class _AnsBoardUsageState_Type(Integer32):
    """Custom type ansBoardUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )


_AnsBoardUsageState_Type.__name__ = "Integer32"
_AnsBoardUsageState_Object = MibTableColumn
ansBoardUsageState = _AnsBoardUsageState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 14),
    _AnsBoardUsageState_Type()
)
ansBoardUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansBoardUsageState.setStatus("mandatory")


class _AnsBoardSyncMode_Type(Integer32):
    """Custom type ansBoardSyncMode based on Integer32"""
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
        *(("master", 1),
          ("netMaster", 3),
          ("notUsed", 4),
          ("slave", 2))
    )


_AnsBoardSyncMode_Type.__name__ = "Integer32"
_AnsBoardSyncMode_Object = MibTableColumn
ansBoardSyncMode = _AnsBoardSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 4, 2, 1, 15),
    _AnsBoardSyncMode_Type()
)
ansBoardSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansBoardSyncMode.setStatus("mandatory")
_PhysicalPoint_ObjectIdentity = ObjectIdentity
physicalPoint = _PhysicalPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5)
)
_AnsPhysicalPointTable_Object = MibTable
ansPhysicalPointTable = _AnsPhysicalPointTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1)
)
if mibBuilder.loadTexts:
    ansPhysicalPointTable.setStatus("mandatory")
_AnsPhysicalPointEntry_Object = MibTableRow
ansPhysicalPointEntry = _AnsPhysicalPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1)
)
ansPhysicalPointEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansPhysicalPointSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansPhysicalPointSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansPhysicalPointPosition"),
    (0, "ANS-EQUIPMENT-MIB", "ansPhysicalPointIndex"),
)
if mibBuilder.loadTexts:
    ansPhysicalPointEntry.setStatus("mandatory")
_AnsPhysicalPointSystemNodeIndex_Type = Integer32
_AnsPhysicalPointSystemNodeIndex_Object = MibTableColumn
ansPhysicalPointSystemNodeIndex = _AnsPhysicalPointSystemNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 1),
    _AnsPhysicalPointSystemNodeIndex_Type()
)
ansPhysicalPointSystemNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansPhysicalPointSystemNodeIndex.setStatus("mandatory")
_AnsPhysicalPointSubrackIndex_Type = Integer32
_AnsPhysicalPointSubrackIndex_Object = MibTableColumn
ansPhysicalPointSubrackIndex = _AnsPhysicalPointSubrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 2),
    _AnsPhysicalPointSubrackIndex_Type()
)
ansPhysicalPointSubrackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansPhysicalPointSubrackIndex.setStatus("mandatory")
_AnsPhysicalPointPosition_Type = Integer32
_AnsPhysicalPointPosition_Object = MibTableColumn
ansPhysicalPointPosition = _AnsPhysicalPointPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 3),
    _AnsPhysicalPointPosition_Type()
)
ansPhysicalPointPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansPhysicalPointPosition.setStatus("mandatory")
_AnsPhysicalPointIndex_Type = Integer32
_AnsPhysicalPointIndex_Object = MibTableColumn
ansPhysicalPointIndex = _AnsPhysicalPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 4),
    _AnsPhysicalPointIndex_Type()
)
ansPhysicalPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansPhysicalPointIndex.setStatus("mandatory")
_AnsDsPhysicalPointSystemNodeIndex_Type = Integer32
_AnsDsPhysicalPointSystemNodeIndex_Object = MibTableColumn
ansDsPhysicalPointSystemNodeIndex = _AnsDsPhysicalPointSystemNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 5),
    _AnsDsPhysicalPointSystemNodeIndex_Type()
)
ansDsPhysicalPointSystemNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansDsPhysicalPointSystemNodeIndex.setStatus("mandatory")
_AnsDsPhysicalPointSubrackIndex_Type = Integer32
_AnsDsPhysicalPointSubrackIndex_Object = MibTableColumn
ansDsPhysicalPointSubrackIndex = _AnsDsPhysicalPointSubrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 6),
    _AnsDsPhysicalPointSubrackIndex_Type()
)
ansDsPhysicalPointSubrackIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansDsPhysicalPointSubrackIndex.setStatus("mandatory")
_AnsDsPhysicalPointPosition_Type = Integer32
_AnsDsPhysicalPointPosition_Object = MibTableColumn
ansDsPhysicalPointPosition = _AnsDsPhysicalPointPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 7),
    _AnsDsPhysicalPointPosition_Type()
)
ansDsPhysicalPointPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansDsPhysicalPointPosition.setStatus("mandatory")
_AnsDsPhysicalPointIndex_Type = Integer32
_AnsDsPhysicalPointIndex_Object = MibTableColumn
ansDsPhysicalPointIndex = _AnsDsPhysicalPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 8),
    _AnsDsPhysicalPointIndex_Type()
)
ansDsPhysicalPointIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansDsPhysicalPointIndex.setStatus("mandatory")


class _AnsPhysicalPointType_Type(Integer32):
    """Custom type ansPhysicalPointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sdhUni", 5),
          ("sdhUniTelia", 6),
          ("sonetUni", 7),
          ("undefined", 4))
    )


_AnsPhysicalPointType_Type.__name__ = "Integer32"
_AnsPhysicalPointType_Object = MibTableColumn
ansPhysicalPointType = _AnsPhysicalPointType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 9),
    _AnsPhysicalPointType_Type()
)
ansPhysicalPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansPhysicalPointType.setStatus("mandatory")


class _AnsPhysicalPointCategory_Type(Integer32):
    """Custom type ansPhysicalPointCategory based on Integer32"""
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
        *(("internal", 4),
          ("service", 1),
          ("serviceUser", 3),
          ("user", 2))
    )


_AnsPhysicalPointCategory_Type.__name__ = "Integer32"
_AnsPhysicalPointCategory_Object = MibTableColumn
ansPhysicalPointCategory = _AnsPhysicalPointCategory_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 10),
    _AnsPhysicalPointCategory_Type()
)
ansPhysicalPointCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansPhysicalPointCategory.setStatus("mandatory")


class _AnsPhysicalPointOperStatus_Type(Integer32):
    """Custom type ansPhysicalPointOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AnsPhysicalPointOperStatus_Type.__name__ = "Integer32"
_AnsPhysicalPointOperStatus_Object = MibTableColumn
ansPhysicalPointOperStatus = _AnsPhysicalPointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 11),
    _AnsPhysicalPointOperStatus_Type()
)
ansPhysicalPointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansPhysicalPointOperStatus.setStatus("mandatory")


class _AnsPhysicalPointAdminStatus_Type(Integer32):
    """Custom type ansPhysicalPointAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_AnsPhysicalPointAdminStatus_Type.__name__ = "Integer32"
_AnsPhysicalPointAdminStatus_Object = MibTableColumn
ansPhysicalPointAdminStatus = _AnsPhysicalPointAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 12),
    _AnsPhysicalPointAdminStatus_Type()
)
ansPhysicalPointAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ansPhysicalPointAdminStatus.setStatus("mandatory")


class _AnsPhysicalPointUsageState_Type(Integer32):
    """Custom type ansPhysicalPointUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )


_AnsPhysicalPointUsageState_Type.__name__ = "Integer32"
_AnsPhysicalPointUsageState_Object = MibTableColumn
ansPhysicalPointUsageState = _AnsPhysicalPointUsageState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 5, 1, 1, 13),
    _AnsPhysicalPointUsageState_Type()
)
ansPhysicalPointUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ansPhysicalPointUsageState.setStatus("mandatory")
_NetClockSource_ObjectIdentity = ObjectIdentity
netClockSource = _NetClockSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6)
)
_NetClockSourceTable_Object = MibTable
netClockSourceTable = _NetClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1)
)
if mibBuilder.loadTexts:
    netClockSourceTable.setStatus("mandatory")
_NetClockSourceEntry_Object = MibTableRow
netClockSourceEntry = _NetClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1)
)
netClockSourceEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "netClockSourceSystemNodeIndex"),
)
if mibBuilder.loadTexts:
    netClockSourceEntry.setStatus("mandatory")
_NetClockSourceSystemNodeIndex_Type = Integer32
_NetClockSourceSystemNodeIndex_Object = MibTableColumn
netClockSourceSystemNodeIndex = _NetClockSourceSystemNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 1),
    _NetClockSourceSystemNodeIndex_Type()
)
netClockSourceSystemNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netClockSourceSystemNodeIndex.setStatus("mandatory")
_NetClockSourceSubrack_Type = Integer32
_NetClockSourceSubrack_Object = MibTableColumn
netClockSourceSubrack = _NetClockSourceSubrack_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 2),
    _NetClockSourceSubrack_Type()
)
netClockSourceSubrack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClockSourceSubrack.setStatus("mandatory")
_NetClockSourceSlot_Type = Integer32
_NetClockSourceSlot_Object = MibTableColumn
netClockSourceSlot = _NetClockSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 3),
    _NetClockSourceSlot_Type()
)
netClockSourceSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClockSourceSlot.setStatus("mandatory")
_NetClockSourcePort_Type = Integer32
_NetClockSourcePort_Object = MibTableColumn
netClockSourcePort = _NetClockSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 4),
    _NetClockSourcePort_Type()
)
netClockSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netClockSourcePort.setStatus("mandatory")


class _NetClockSourceStatus_Type(Integer32):
    """Custom type netClockSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("idle", 2))
    )


_NetClockSourceStatus_Type.__name__ = "Integer32"
_NetClockSourceStatus_Object = MibTableColumn
netClockSourceStatus = _NetClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 5),
    _NetClockSourceStatus_Type()
)
netClockSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netClockSourceStatus.setStatus("mandatory")
_NetClockSourcePriorityList_Type = DisplayString
_NetClockSourcePriorityList_Object = MibTableColumn
netClockSourcePriorityList = _NetClockSourcePriorityList_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 6),
    _NetClockSourcePriorityList_Type()
)
netClockSourcePriorityList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClockSourcePriorityList.setStatus("mandatory")


class _NetClockSourceRevertiveMode_Type(Integer32):
    """Custom type netClockSourceRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-revertive", 2),
          ("not-used", 3),
          ("revertive", 1))
    )


_NetClockSourceRevertiveMode_Type.__name__ = "Integer32"
_NetClockSourceRevertiveMode_Object = MibTableColumn
netClockSourceRevertiveMode = _NetClockSourceRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 7),
    _NetClockSourceRevertiveMode_Type()
)
netClockSourceRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClockSourceRevertiveMode.setStatus("mandatory")


class _NetClockSourceTimeToRestore_Type(Integer32):
    """Custom type netClockSourceTimeToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 900),
    )


_NetClockSourceTimeToRestore_Type.__name__ = "Integer32"
_NetClockSourceTimeToRestore_Object = MibTableColumn
netClockSourceTimeToRestore = _NetClockSourceTimeToRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 8),
    _NetClockSourceTimeToRestore_Type()
)
netClockSourceTimeToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClockSourceTimeToRestore.setStatus("mandatory")
_NetClockSourceRowStatus_Type = RowStatus
_NetClockSourceRowStatus_Object = MibTableColumn
netClockSourceRowStatus = _NetClockSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 3, 6, 1, 1, 9),
    _NetClockSourceRowStatus_Type()
)
netClockSourceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netClockSourceRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANS-EQUIPMENT-MIB",
    **{"AnsSubrackType": AnsSubrackType,
       "ProtectedBoardType": ProtectedBoardType,
       "equipment": equipment,
       "systemNode": systemNode,
       "ansSystemNodeTable": ansSystemNodeTable,
       "ansSystemNodeEntry": ansSystemNodeEntry,
       "ansSystemNodeIndex": ansSystemNodeIndex,
       "ansSystemNodeName": ansSystemNodeName,
       "ansSystemNodeOrigin": ansSystemNodeOrigin,
       "ansSystemNodeLocation": ansSystemNodeLocation,
       "ansSystemNodeClockSource": ansSystemNodeClockSource,
       "ansSystemNodeRowStatus": ansSystemNodeRowStatus,
       "subrack": subrack,
       "ansSubrackTable": ansSubrackTable,
       "ansSubrackEntry": ansSubrackEntry,
       "ansSubrackSystemNodeIndex": ansSubrackSystemNodeIndex,
       "ansSubrackIndex": ansSubrackIndex,
       "ansSubrackName": ansSubrackName,
       "ansSubrackHwId": ansSubrackHwId,
       "ansSubrackLocation": ansSubrackLocation,
       "ansSubrackType": ansSubrackType,
       "ansSubrackProtectionState": ansSubrackProtectionState,
       "ansSubrackProtectionScheme": ansSubrackProtectionScheme,
       "ansSubrackNoOfSlots": ansSubrackNoOfSlots,
       "ansSubrackAlarmStatus": ansSubrackAlarmStatus,
       "ansSubrackRowStatus": ansSubrackRowStatus,
       "slot": slot,
       "ansSlotTable": ansSlotTable,
       "ansSlotEntry": ansSlotEntry,
       "ansSlotSystemNodeIndex": ansSlotSystemNodeIndex,
       "ansSlotSubrackIndex": ansSlotSubrackIndex,
       "ansSlotPosition": ansSlotPosition,
       "ansSlotConfiguredBoardId": ansSlotConfiguredBoardId,
       "ansSlotInsertedBoardId": ansSlotInsertedBoardId,
       "ansSlotManagementStatus": ansSlotManagementStatus,
       "ansSlotFallback": ansSlotFallback,
       "ansSlotAlarmStatus": ansSlotAlarmStatus,
       "board": board,
       "ansBoardTable": ansBoardTable,
       "ansBoardEntry": ansBoardEntry,
       "ansBoardSystemNodeIndex": ansBoardSystemNodeIndex,
       "ansBoardSubrackIndex": ansBoardSubrackIndex,
       "ansBoardPosition": ansBoardPosition,
       "ansBoardType": ansBoardType,
       "ansBoardHwId": ansBoardHwId,
       "ansBoardSwIdActive": ansBoardSwIdActive,
       "ansBoardSwIdPassive": ansBoardSwIdPassive,
       "ansBoardOperStatus": ansBoardOperStatus,
       "ansBoardAdminStatus": ansBoardAdminStatus,
       "ansBoardRestart": ansBoardRestart,
       "ansBoardLedStatus": ansBoardLedStatus,
       "ansBoardStandbyStatus": ansBoardStandbyStatus,
       "ansBoardAlarmStatus": ansBoardAlarmStatus,
       "ansBoardUsageState": ansBoardUsageState,
       "ansBoardSyncMode": ansBoardSyncMode,
       "physicalPoint": physicalPoint,
       "ansPhysicalPointTable": ansPhysicalPointTable,
       "ansPhysicalPointEntry": ansPhysicalPointEntry,
       "ansPhysicalPointSystemNodeIndex": ansPhysicalPointSystemNodeIndex,
       "ansPhysicalPointSubrackIndex": ansPhysicalPointSubrackIndex,
       "ansPhysicalPointPosition": ansPhysicalPointPosition,
       "ansPhysicalPointIndex": ansPhysicalPointIndex,
       "ansDsPhysicalPointSystemNodeIndex": ansDsPhysicalPointSystemNodeIndex,
       "ansDsPhysicalPointSubrackIndex": ansDsPhysicalPointSubrackIndex,
       "ansDsPhysicalPointPosition": ansDsPhysicalPointPosition,
       "ansDsPhysicalPointIndex": ansDsPhysicalPointIndex,
       "ansPhysicalPointType": ansPhysicalPointType,
       "ansPhysicalPointCategory": ansPhysicalPointCategory,
       "ansPhysicalPointOperStatus": ansPhysicalPointOperStatus,
       "ansPhysicalPointAdminStatus": ansPhysicalPointAdminStatus,
       "ansPhysicalPointUsageState": ansPhysicalPointUsageState,
       "netClockSource": netClockSource,
       "netClockSourceTable": netClockSourceTable,
       "netClockSourceEntry": netClockSourceEntry,
       "netClockSourceSystemNodeIndex": netClockSourceSystemNodeIndex,
       "netClockSourceSubrack": netClockSourceSubrack,
       "netClockSourceSlot": netClockSourceSlot,
       "netClockSourcePort": netClockSourcePort,
       "netClockSourceStatus": netClockSourceStatus,
       "netClockSourcePriorityList": netClockSourcePriorityList,
       "netClockSourceRevertiveMode": netClockSourceRevertiveMode,
       "netClockSourceTimeToRestore": netClockSourceTimeToRestore,
       "netClockSourceRowStatus": netClockSourceRowStatus}
)
