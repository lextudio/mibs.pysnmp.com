# SNMP MIB module (A3COM0304-RESILIENTLINKS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM0304-RESILIENTLINKS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:12 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_MrmResilience_ObjectIdentity = ObjectIdentity
mrmResilience = _MrmResilience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 15)
)
_ResTable_Object = MibTable
resTable = _ResTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1)
)
if mibBuilder.loadTexts:
    resTable.setStatus("mandatory")
_ResTableEntry_Object = MibTableRow
resTableEntry = _ResTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1)
)
resTableEntry.setIndexNames(
    (0, "A3COM0304-RESILIENTLINKS", "resRepeater"),
    (0, "A3COM0304-RESILIENTLINKS", "resMainSlot"),
    (0, "A3COM0304-RESILIENTLINKS", "resMainPort"),
)
if mibBuilder.loadTexts:
    resTableEntry.setStatus("mandatory")
_ResRepeater_Type = Integer32
_ResRepeater_Object = MibTableColumn
resRepeater = _ResRepeater_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 1),
    _ResRepeater_Type()
)
resRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resRepeater.setStatus("mandatory")
_ResMainSlot_Type = Integer32
_ResMainSlot_Object = MibTableColumn
resMainSlot = _ResMainSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 2),
    _ResMainSlot_Type()
)
resMainSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainSlot.setStatus("mandatory")
_ResMainPort_Type = Integer32
_ResMainPort_Object = MibTableColumn
resMainPort = _ResMainPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 3),
    _ResMainPort_Type()
)
resMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainPort.setStatus("mandatory")


class _ResMainState_Type(Integer32):
    """Custom type resMainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2),
          ("ok-and-active", 3))
    )


_ResMainState_Type.__name__ = "Integer32"
_ResMainState_Object = MibTableColumn
resMainState = _ResMainState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 4),
    _ResMainState_Type()
)
resMainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainState.setStatus("mandatory")
_ResStandbySlot_Type = Integer32
_ResStandbySlot_Object = MibTableColumn
resStandbySlot = _ResStandbySlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 5),
    _ResStandbySlot_Type()
)
resStandbySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resStandbySlot.setStatus("mandatory")
_ResStandbyPort_Type = Integer32
_ResStandbyPort_Object = MibTableColumn
resStandbyPort = _ResStandbyPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 6),
    _ResStandbyPort_Type()
)
resStandbyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resStandbyPort.setStatus("mandatory")


class _ResStandbyState_Type(Integer32):
    """Custom type resStandbyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2),
          ("ok-and-active", 3))
    )


_ResStandbyState_Type.__name__ = "Integer32"
_ResStandbyState_Object = MibTableColumn
resStandbyState = _ResStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 7),
    _ResStandbyState_Type()
)
resStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resStandbyState.setStatus("mandatory")


class _ResPairState_Type(Integer32):
    """Custom type resPairState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("operational", 2))
    )


_ResPairState_Type.__name__ = "Integer32"
_ResPairState_Object = MibTableColumn
resPairState = _ResPairState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 8),
    _ResPairState_Type()
)
resPairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resPairState.setStatus("mandatory")


class _ResPairModificationStatus_Type(Integer32):
    """Custom type resPairModificationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stable", 2),
          ("under-modification", 1))
    )


_ResPairModificationStatus_Type.__name__ = "Integer32"
_ResPairModificationStatus_Object = MibTableColumn
resPairModificationStatus = _ResPairModificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 9),
    _ResPairModificationStatus_Type()
)
resPairModificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairModificationStatus.setStatus("mandatory")


class _ResPairAction_Type(Integer32):
    """Custom type resPairAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2),
          ("togglePort", 3))
    )


_ResPairAction_Type.__name__ = "Integer32"
_ResPairAction_Object = MibTableColumn
resPairAction = _ResPairAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 10),
    _ResPairAction_Type()
)
resPairAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairAction.setStatus("mandatory")


class _ResPairEnable_Type(Integer32):
    """Custom type resPairEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ResPairEnable_Type.__name__ = "Integer32"
_ResPairEnable_Object = MibTableColumn
resPairEnable = _ResPairEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 11),
    _ResPairEnable_Type()
)
resPairEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairEnable.setStatus("mandatory")


class _ResPairMode_Type(Integer32):
    """Custom type resPairMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-switch-back", 1),
          ("switch-back-to-main", 2))
    )


_ResPairMode_Type.__name__ = "Integer32"
_ResPairMode_Object = MibTableColumn
resPairMode = _ResPairMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 12),
    _ResPairMode_Type()
)
resPairMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairMode.setStatus("mandatory")


class _ResPairName_Type(DisplayString):
    """Custom type resPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ResPairName_Type.__name__ = "DisplayString"
_ResPairName_Object = MibTableColumn
resPairName = _ResPairName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 13),
    _ResPairName_Type()
)
resPairName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairName.setStatus("mandatory")
_ResStandbyMapTable_Object = MibTable
resStandbyMapTable = _ResStandbyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2)
)
if mibBuilder.loadTexts:
    resStandbyMapTable.setStatus("mandatory")
_ResStandbyMapTableEntry_Object = MibTableRow
resStandbyMapTableEntry = _ResStandbyMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1)
)
resStandbyMapTableEntry.setIndexNames(
    (0, "A3COM0304-RESILIENTLINKS", "resSbRepeater"),
    (0, "A3COM0304-RESILIENTLINKS", "resSbSlot"),
    (0, "A3COM0304-RESILIENTLINKS", "resSbPort"),
)
if mibBuilder.loadTexts:
    resStandbyMapTableEntry.setStatus("mandatory")
_ResSbRepeater_Type = Integer32
_ResSbRepeater_Object = MibTableColumn
resSbRepeater = _ResSbRepeater_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 1),
    _ResSbRepeater_Type()
)
resSbRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbRepeater.setStatus("mandatory")
_ResSbSlot_Type = Integer32
_ResSbSlot_Object = MibTableColumn
resSbSlot = _ResSbSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 2),
    _ResSbSlot_Type()
)
resSbSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbSlot.setStatus("mandatory")
_ResSbPort_Type = Integer32
_ResSbPort_Object = MibTableColumn
resSbPort = _ResSbPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 3),
    _ResSbPort_Type()
)
resSbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbPort.setStatus("mandatory")


class _ResSbType_Type(Integer32):
    """Custom type resSbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("standby", 2))
    )


_ResSbType_Type.__name__ = "Integer32"
_ResSbType_Object = MibTableColumn
resSbType = _ResSbType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 4),
    _ResSbType_Type()
)
resSbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbType.setStatus("mandatory")
_ResSbMainSlot_Type = Integer32
_ResSbMainSlot_Object = MibTableColumn
resSbMainSlot = _ResSbMainSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 5),
    _ResSbMainSlot_Type()
)
resSbMainSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbMainSlot.setStatus("mandatory")
_ResSbMainPort_Type = Integer32
_ResSbMainPort_Object = MibTableColumn
resSbMainPort = _ResSbMainPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 6),
    _ResSbMainPort_Type()
)
resSbMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbMainPort.setStatus("mandatory")
_ResFlushTable_Type = Integer32
_ResFlushTable_Object = MibScalar
resFlushTable = _ResFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 3),
    _ResFlushTable_Type()
)
resFlushTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resFlushTable.setStatus("mandatory")

# Managed Objects groups


# Notification objects

resResilienceSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 43)
)
resResilienceSwitch.setObjects(
      *(("A3COM0304-RESILIENTLINKS", "resMainState"),
        ("A3COM0304-RESILIENTLINKS", "resStandbyState"))
)
if mibBuilder.loadTexts:
    resResilienceSwitch.setStatus(
        ""
    )

resStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 44)
)
resStateChange.setObjects(
      *(("A3COM0304-RESILIENTLINKS", "resMainState"),
        ("A3COM0304-RESILIENTLINKS", "resStandbyState"))
)
if mibBuilder.loadTexts:
    resStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM0304-RESILIENTLINKS",
    **{"a3Com": a3Com,
       "resResilienceSwitch": resResilienceSwitch,
       "resStateChange": resStateChange,
       "generic": generic,
       "mrmResilience": mrmResilience,
       "resTable": resTable,
       "resTableEntry": resTableEntry,
       "resRepeater": resRepeater,
       "resMainSlot": resMainSlot,
       "resMainPort": resMainPort,
       "resMainState": resMainState,
       "resStandbySlot": resStandbySlot,
       "resStandbyPort": resStandbyPort,
       "resStandbyState": resStandbyState,
       "resPairState": resPairState,
       "resPairModificationStatus": resPairModificationStatus,
       "resPairAction": resPairAction,
       "resPairEnable": resPairEnable,
       "resPairMode": resPairMode,
       "resPairName": resPairName,
       "resStandbyMapTable": resStandbyMapTable,
       "resStandbyMapTableEntry": resStandbyMapTableEntry,
       "resSbRepeater": resSbRepeater,
       "resSbSlot": resSbSlot,
       "resSbPort": resSbPort,
       "resSbType": resSbType,
       "resSbMainSlot": resSbMainSlot,
       "resSbMainPort": resSbMainPort,
       "resFlushTable": resFlushTable}
)
