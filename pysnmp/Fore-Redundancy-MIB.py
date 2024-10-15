# SNMP MIB module (Fore-Redundancy-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Redundancy-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:11 2024
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

(atmSwitch,
 hardware) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "atmSwitch",
    "hardware")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

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

asx4000RedundancyModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9)
)


# Types definitions



class Asx4000RedundancyState(Integer32):
    """Custom type Asx4000RedundancyState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("armed", 7),
          ("cloning", 2),
          ("errored-detected", 6),
          ("initializing", 1),
          ("passive", 5),
          ("requalifying", 8),
          ("testing", 3),
          ("unprotected", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asx4000RedFabricGroup_ObjectIdentity = ObjectIdentity
asx4000RedFabricGroup = _Asx4000RedFabricGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1)
)
_Asx4000RedFabricTable_Object = MibTable
asx4000RedFabricTable = _Asx4000RedFabricTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    asx4000RedFabricTable.setStatus("current")
_Asx4000RedFabricEntry_Object = MibTableRow
asx4000RedFabricEntry = _Asx4000RedFabricEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1)
)
asx4000RedFabricEntry.setIndexNames(
    (0, "Fore-Redundancy-MIB", "asx4000RedFabricIndex"),
)
if mibBuilder.loadTexts:
    asx4000RedFabricEntry.setStatus("current")
_Asx4000RedFabricIndex_Type = Integer32
_Asx4000RedFabricIndex_Object = MibTableColumn
asx4000RedFabricIndex = _Asx4000RedFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 1),
    _Asx4000RedFabricIndex_Type()
)
asx4000RedFabricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedFabricIndex.setStatus("current")


class _Asx4000RedFabricAdminMode_Type(Integer32):
    """Custom type asx4000RedFabricAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protection", 2),
          ("unprotected", 3),
          ("working", 1))
    )


_Asx4000RedFabricAdminMode_Type.__name__ = "Integer32"
_Asx4000RedFabricAdminMode_Object = MibTableColumn
asx4000RedFabricAdminMode = _Asx4000RedFabricAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 2),
    _Asx4000RedFabricAdminMode_Type()
)
asx4000RedFabricAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedFabricAdminMode.setStatus("current")


class _Asx4000RedFabricOperState_Type(Integer32):
    """Custom type asx4000RedFabricOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("unprotected", 3))
    )


_Asx4000RedFabricOperState_Type.__name__ = "Integer32"
_Asx4000RedFabricOperState_Object = MibTableColumn
asx4000RedFabricOperState = _Asx4000RedFabricOperState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 3),
    _Asx4000RedFabricOperState_Type()
)
asx4000RedFabricOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedFabricOperState.setStatus("current")


class _Asx4000RedFabricPendingAdminMode_Type(Integer32):
    """Custom type asx4000RedFabricPendingAdminMode based on Integer32"""
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
        *(("none", 4),
          ("protection", 2),
          ("unprotected", 3),
          ("working", 1))
    )


_Asx4000RedFabricPendingAdminMode_Type.__name__ = "Integer32"
_Asx4000RedFabricPendingAdminMode_Object = MibTableColumn
asx4000RedFabricPendingAdminMode = _Asx4000RedFabricPendingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 4),
    _Asx4000RedFabricPendingAdminMode_Type()
)
asx4000RedFabricPendingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asx4000RedFabricPendingAdminMode.setStatus("current")


class _Asx4000RedFabricCommittedState_Type(Integer32):
    """Custom type asx4000RedFabricCommittedState based on Integer32"""
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


_Asx4000RedFabricCommittedState_Type.__name__ = "Integer32"
_Asx4000RedFabricCommittedState_Object = MibTableColumn
asx4000RedFabricCommittedState = _Asx4000RedFabricCommittedState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 5),
    _Asx4000RedFabricCommittedState_Type()
)
asx4000RedFabricCommittedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedFabricCommittedState.setStatus("current")


class _Asx4000RedFabricCloningState_Type(Integer32):
    """Custom type asx4000RedFabricCloningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("inprogress", 2),
          ("notApplicable", 3))
    )


_Asx4000RedFabricCloningState_Type.__name__ = "Integer32"
_Asx4000RedFabricCloningState_Object = MibTableColumn
asx4000RedFabricCloningState = _Asx4000RedFabricCloningState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 6),
    _Asx4000RedFabricCloningState_Type()
)
asx4000RedFabricCloningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedFabricCloningState.setStatus("deprecated")


class _Asx4000RedFabricSwitchCommand_Type(Integer32):
    """Custom type asx4000RedFabricSwitchCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Asx4000RedFabricSwitchCommand_Type.__name__ = "Integer32"
_Asx4000RedFabricSwitchCommand_Object = MibTableColumn
asx4000RedFabricSwitchCommand = _Asx4000RedFabricSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 7),
    _Asx4000RedFabricSwitchCommand_Type()
)
asx4000RedFabricSwitchCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asx4000RedFabricSwitchCommand.setStatus("current")
_Asx4000RedFabricRedundancyState_Type = Asx4000RedundancyState
_Asx4000RedFabricRedundancyState_Object = MibTableColumn
asx4000RedFabricRedundancyState = _Asx4000RedFabricRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 1, 1, 8),
    _Asx4000RedFabricRedundancyState_Type()
)
asx4000RedFabricRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedFabricRedundancyState.setStatus("current")


class _Asx4000RedFabricGroupCommit_Type(Integer32):
    """Custom type asx4000RedFabricGroupCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_Asx4000RedFabricGroupCommit_Type.__name__ = "Integer32"
_Asx4000RedFabricGroupCommit_Object = MibScalar
asx4000RedFabricGroupCommit = _Asx4000RedFabricGroupCommit_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 1, 3),
    _Asx4000RedFabricGroupCommit_Type()
)
asx4000RedFabricGroupCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asx4000RedFabricGroupCommit.setStatus("current")
_Asx4000RedPortCardGroup_ObjectIdentity = ObjectIdentity
asx4000RedPortCardGroup = _Asx4000RedPortCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2)
)
_Asx4000RedPortCardTable_Object = MibTable
asx4000RedPortCardTable = _Asx4000RedPortCardTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    asx4000RedPortCardTable.setStatus("current")
_Asx4000RedPortCardEntry_Object = MibTableRow
asx4000RedPortCardEntry = _Asx4000RedPortCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1)
)
asx4000RedPortCardEntry.setIndexNames(
    (0, "Fore-Redundancy-MIB", "asx4000RedPortCardFabIndex"),
    (0, "Fore-Redundancy-MIB", "asx4000RedPortCardIndex"),
)
if mibBuilder.loadTexts:
    asx4000RedPortCardEntry.setStatus("current")
_Asx4000RedPortCardFabIndex_Type = Integer32
_Asx4000RedPortCardFabIndex_Object = MibTableColumn
asx4000RedPortCardFabIndex = _Asx4000RedPortCardFabIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1, 1),
    _Asx4000RedPortCardFabIndex_Type()
)
asx4000RedPortCardFabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedPortCardFabIndex.setStatus("current")


class _Asx4000RedPortCardIndex_Type(Integer32):
    """Custom type asx4000RedPortCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ab", 1),
          ("cd", 2))
    )


_Asx4000RedPortCardIndex_Type.__name__ = "Integer32"
_Asx4000RedPortCardIndex_Object = MibTableColumn
asx4000RedPortCardIndex = _Asx4000RedPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1, 2),
    _Asx4000RedPortCardIndex_Type()
)
asx4000RedPortCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedPortCardIndex.setStatus("current")


class _Asx4000RedPortCardCloningState_Type(Integer32):
    """Custom type asx4000RedPortCardCloningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("inprogress", 2),
          ("notApplicable", 3))
    )


_Asx4000RedPortCardCloningState_Type.__name__ = "Integer32"
_Asx4000RedPortCardCloningState_Object = MibTableColumn
asx4000RedPortCardCloningState = _Asx4000RedPortCardCloningState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 2, 1, 1, 3),
    _Asx4000RedPortCardCloningState_Type()
)
asx4000RedPortCardCloningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedPortCardCloningState.setStatus("current")
_Asx4000RedundancyGroup_ObjectIdentity = ObjectIdentity
asx4000RedundancyGroup = _Asx4000RedundancyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3)
)
_Asx4000RedundancyGroupTable_Object = MibTable
asx4000RedundancyGroupTable = _Asx4000RedundancyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    asx4000RedundancyGroupTable.setStatus("current")
_Asx4000RedundancyGroupEntry_Object = MibTableRow
asx4000RedundancyGroupEntry = _Asx4000RedundancyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1)
)
asx4000RedundancyGroupEntry.setIndexNames(
    (0, "Fore-Redundancy-MIB", "asx4000RedGroupName"),
)
if mibBuilder.loadTexts:
    asx4000RedundancyGroupEntry.setStatus("current")


class _Asx4000RedGroupName_Type(Integer32):
    """Custom type asx4000RedGroupName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("r12", 1),
          ("r34", 2))
    )


_Asx4000RedGroupName_Type.__name__ = "Integer32"
_Asx4000RedGroupName_Object = MibTableColumn
asx4000RedGroupName = _Asx4000RedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 1),
    _Asx4000RedGroupName_Type()
)
asx4000RedGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedGroupName.setStatus("current")


class _Asx4000RedGroupRevertMode_Type(Integer32):
    """Custom type asx4000RedGroupRevertMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_Asx4000RedGroupRevertMode_Type.__name__ = "Integer32"
_Asx4000RedGroupRevertMode_Object = MibTableColumn
asx4000RedGroupRevertMode = _Asx4000RedGroupRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 2),
    _Asx4000RedGroupRevertMode_Type()
)
asx4000RedGroupRevertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asx4000RedGroupRevertMode.setStatus("current")


class _Asx4000RedGroupQualifyTimer_Type(Integer32):
    """Custom type asx4000RedGroupQualifyTimer based on Integer32"""
    defaultValue = 5


_Asx4000RedGroupQualifyTimer_Object = MibTableColumn
asx4000RedGroupQualifyTimer = _Asx4000RedGroupQualifyTimer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 3),
    _Asx4000RedGroupQualifyTimer_Type()
)
asx4000RedGroupQualifyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asx4000RedGroupQualifyTimer.setStatus("current")


class _Asx4000RedGroupErrorThreshold_Type(Integer32):
    """Custom type asx4000RedGroupErrorThreshold based on Integer32"""
    defaultValue = 2


_Asx4000RedGroupErrorThreshold_Object = MibTableColumn
asx4000RedGroupErrorThreshold = _Asx4000RedGroupErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 4),
    _Asx4000RedGroupErrorThreshold_Type()
)
asx4000RedGroupErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asx4000RedGroupErrorThreshold.setStatus("current")
_Asx4000RedGroupErrorBlockSize_Type = Integer32
_Asx4000RedGroupErrorBlockSize_Object = MibTableColumn
asx4000RedGroupErrorBlockSize = _Asx4000RedGroupErrorBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 3, 1, 1, 5),
    _Asx4000RedGroupErrorBlockSize_Type()
)
asx4000RedGroupErrorBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedGroupErrorBlockSize.setStatus("current")
_Asx4000RedNetmodGroup_ObjectIdentity = ObjectIdentity
asx4000RedNetmodGroup = _Asx4000RedNetmodGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4)
)
_Asx4000RedNetmodTable_Object = MibTable
asx4000RedNetmodTable = _Asx4000RedNetmodTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    asx4000RedNetmodTable.setStatus("current")
_Asx4000RedNetmodEntry_Object = MibTableRow
asx4000RedNetmodEntry = _Asx4000RedNetmodEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1)
)
asx4000RedNetmodEntry.setIndexNames(
    (0, "Fore-Redundancy-MIB", "asx4000RedNetmodFabIndex"),
    (0, "Fore-Redundancy-MIB", "asx4000RedNetmodIndex"),
)
if mibBuilder.loadTexts:
    asx4000RedNetmodEntry.setStatus("current")
_Asx4000RedNetmodFabIndex_Type = Integer32
_Asx4000RedNetmodFabIndex_Object = MibTableColumn
asx4000RedNetmodFabIndex = _Asx4000RedNetmodFabIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1, 1),
    _Asx4000RedNetmodFabIndex_Type()
)
asx4000RedNetmodFabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedNetmodFabIndex.setStatus("current")
_Asx4000RedNetmodIndex_Type = Integer32
_Asx4000RedNetmodIndex_Object = MibTableColumn
asx4000RedNetmodIndex = _Asx4000RedNetmodIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1, 2),
    _Asx4000RedNetmodIndex_Type()
)
asx4000RedNetmodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedNetmodIndex.setStatus("current")
_Asx4000RedNetmodRedundancyState_Type = Asx4000RedundancyState
_Asx4000RedNetmodRedundancyState_Object = MibTableColumn
asx4000RedNetmodRedundancyState = _Asx4000RedNetmodRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 4, 1, 1, 3),
    _Asx4000RedNetmodRedundancyState_Type()
)
asx4000RedNetmodRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asx4000RedNetmodRedundancyState.setStatus("current")

# Managed Objects groups


# Notification objects

redundancyFabricSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2018)
)
redundancyFabricSwitchover.setObjects(
      *(("Fore-Redundancy-MIB", "asx4000RedFabricIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    redundancyFabricSwitchover.setStatus(
        "current"
    )

redundancyFabricErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 2)
)
redundancyFabricErrorCleared.setObjects(
      *(("Fore-Redundancy-MIB", "asx4000RedFabricIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    redundancyFabricErrorCleared.setStatus(
        "current"
    )

redundancyFabricErrorDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 3)
)
redundancyFabricErrorDetected.setObjects(
      *(("Fore-Redundancy-MIB", "asx4000RedFabricIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    redundancyFabricErrorDetected.setStatus(
        "current"
    )

redundancyNetmodErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 4)
)
redundancyNetmodErrorCleared.setObjects(
      *(("Fore-Redundancy-MIB", "asx4000RedNetmodFabIndex"),
        ("Fore-Redundancy-MIB", "asx4000RedNetmodIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    redundancyNetmodErrorCleared.setStatus(
        "current"
    )

redundancyNetmodErrorDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 9, 0, 5)
)
redundancyNetmodErrorDetected.setObjects(
      *(("Fore-Redundancy-MIB", "asx4000RedNetmodFabIndex"),
        ("Fore-Redundancy-MIB", "asx4000RedNetmodIndex"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    redundancyNetmodErrorDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Redundancy-MIB",
    **{"Asx4000RedundancyState": Asx4000RedundancyState,
       "redundancyFabricSwitchover": redundancyFabricSwitchover,
       "asx4000RedundancyModule": asx4000RedundancyModule,
       "redundancyFabricErrorCleared": redundancyFabricErrorCleared,
       "redundancyFabricErrorDetected": redundancyFabricErrorDetected,
       "redundancyNetmodErrorCleared": redundancyNetmodErrorCleared,
       "redundancyNetmodErrorDetected": redundancyNetmodErrorDetected,
       "asx4000RedFabricGroup": asx4000RedFabricGroup,
       "asx4000RedFabricTable": asx4000RedFabricTable,
       "asx4000RedFabricEntry": asx4000RedFabricEntry,
       "asx4000RedFabricIndex": asx4000RedFabricIndex,
       "asx4000RedFabricAdminMode": asx4000RedFabricAdminMode,
       "asx4000RedFabricOperState": asx4000RedFabricOperState,
       "asx4000RedFabricPendingAdminMode": asx4000RedFabricPendingAdminMode,
       "asx4000RedFabricCommittedState": asx4000RedFabricCommittedState,
       "asx4000RedFabricCloningState": asx4000RedFabricCloningState,
       "asx4000RedFabricSwitchCommand": asx4000RedFabricSwitchCommand,
       "asx4000RedFabricRedundancyState": asx4000RedFabricRedundancyState,
       "asx4000RedFabricGroupCommit": asx4000RedFabricGroupCommit,
       "asx4000RedPortCardGroup": asx4000RedPortCardGroup,
       "asx4000RedPortCardTable": asx4000RedPortCardTable,
       "asx4000RedPortCardEntry": asx4000RedPortCardEntry,
       "asx4000RedPortCardFabIndex": asx4000RedPortCardFabIndex,
       "asx4000RedPortCardIndex": asx4000RedPortCardIndex,
       "asx4000RedPortCardCloningState": asx4000RedPortCardCloningState,
       "asx4000RedundancyGroup": asx4000RedundancyGroup,
       "asx4000RedundancyGroupTable": asx4000RedundancyGroupTable,
       "asx4000RedundancyGroupEntry": asx4000RedundancyGroupEntry,
       "asx4000RedGroupName": asx4000RedGroupName,
       "asx4000RedGroupRevertMode": asx4000RedGroupRevertMode,
       "asx4000RedGroupQualifyTimer": asx4000RedGroupQualifyTimer,
       "asx4000RedGroupErrorThreshold": asx4000RedGroupErrorThreshold,
       "asx4000RedGroupErrorBlockSize": asx4000RedGroupErrorBlockSize,
       "asx4000RedNetmodGroup": asx4000RedNetmodGroup,
       "asx4000RedNetmodTable": asx4000RedNetmodTable,
       "asx4000RedNetmodEntry": asx4000RedNetmodEntry,
       "asx4000RedNetmodFabIndex": asx4000RedNetmodFabIndex,
       "asx4000RedNetmodIndex": asx4000RedNetmodIndex,
       "asx4000RedNetmodRedundancyState": asx4000RedNetmodRedundancyState}
)
