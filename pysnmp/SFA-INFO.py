# SNMP MIB module (SFA-INFO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SFA-INFO
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:24 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Datadirect_ObjectIdentity = ObjectIdentity
datadirect = _Datadirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894)
)
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 2)
)
_TempNumber_Type = Integer32
_TempNumber_Object = MibScalar
tempNumber = _TempNumber_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 1),
    _TempNumber_Type()
)
tempNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNumber.setStatus("mandatory")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("mandatory")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 2, 1)
)
tempEntry.setIndexNames(
    (0, "SFA-INFO", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("mandatory")
_TempIndex_Type = Integer32
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("mandatory")


class _TempEncId_Type(OctetString):
    """Custom type tempEncId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TempEncId_Type.__name__ = "OctetString"
_TempEncId_Object = MibTableColumn
tempEncId = _TempEncId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 2),
    _TempEncId_Type()
)
tempEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempEncId.setStatus("mandatory")
_TempEncPos_Type = Integer32
_TempEncPos_Object = MibTableColumn
tempEncPos = _TempEncPos_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 3),
    _TempEncPos_Type()
)
tempEncPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempEncPos.setStatus("mandatory")


class _TempStatus_Type(Integer32):
    """Custom type tempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("normal", 1),
          ("warning", 2))
    )


_TempStatus_Type.__name__ = "Integer32"
_TempStatus_Object = MibTableColumn
tempStatus = _TempStatus_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 2, 1, 4),
    _TempStatus_Type()
)
tempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempStatus.setStatus("mandatory")
_FanNumber_Type = Integer32
_FanNumber_Object = MibScalar
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 3),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("mandatory")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 4)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("mandatory")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 4, 1)
)
fanEntry.setIndexNames(
    (0, "SFA-INFO", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("mandatory")
_FanIndex_Type = Integer32
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("mandatory")


class _FanEncId_Type(OctetString):
    """Custom type fanEncId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FanEncId_Type.__name__ = "OctetString"
_FanEncId_Object = MibTableColumn
fanEncId = _FanEncId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 2),
    _FanEncId_Type()
)
fanEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanEncId.setStatus("mandatory")
_FanEncPos_Type = Integer32
_FanEncPos_Object = MibTableColumn
fanEncPos = _FanEncPos_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 3),
    _FanEncPos_Type()
)
fanEncPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanEncPos.setStatus("mandatory")


class _FanStatus_Type(Integer32):
    """Custom type fanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("healthy", 1))
    )


_FanStatus_Type.__name__ = "Integer32"
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 4, 1, 4),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("mandatory")
_PowerNumber_Type = Integer32
_PowerNumber_Object = MibScalar
powerNumber = _PowerNumber_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 5),
    _PowerNumber_Type()
)
powerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerNumber.setStatus("mandatory")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 6)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("mandatory")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 6, 1)
)
powerEntry.setIndexNames(
    (0, "SFA-INFO", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("mandatory")
_PowerIndex_Type = Integer32
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerIndex.setStatus("mandatory")


class _PowerEncId_Type(OctetString):
    """Custom type powerEncId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PowerEncId_Type.__name__ = "OctetString"
_PowerEncId_Object = MibTableColumn
powerEncId = _PowerEncId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 2),
    _PowerEncId_Type()
)
powerEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerEncId.setStatus("mandatory")
_PowerEncPos_Type = Integer32
_PowerEncPos_Object = MibTableColumn
powerEncPos = _PowerEncPos_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 3),
    _PowerEncPos_Type()
)
powerEncPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerEncPos.setStatus("mandatory")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("healthy", 1))
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibTableColumn
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 6, 1, 4),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("mandatory")
_PoolNumber_Type = Integer32
_PoolNumber_Object = MibScalar
poolNumber = _PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 7),
    _PoolNumber_Type()
)
poolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumber.setStatus("mandatory")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 8)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("mandatory")
_PoolEntry_Object = MibTableRow
poolEntry = _PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 8, 1)
)
poolEntry.setIndexNames(
    (0, "SFA-INFO", "poolIndex"),
)
if mibBuilder.loadTexts:
    poolEntry.setStatus("mandatory")
_PoolIndex_Type = Integer32
_PoolIndex_Object = MibTableColumn
poolIndex = _PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 1),
    _PoolIndex_Type()
)
poolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolIndex.setStatus("mandatory")
_PoolId_Type = Integer32
_PoolId_Object = MibTableColumn
poolId = _PoolId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 2),
    _PoolId_Type()
)
poolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolId.setStatus("mandatory")


class _PoolType_Type(Integer32):
    """Custom type poolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("spare", 2),
          ("storage", 1),
          ("unassigned", 3))
    )


_PoolType_Type.__name__ = "Integer32"
_PoolType_Object = MibTableColumn
poolType = _PoolType_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 3),
    _PoolType_Type()
)
poolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolType.setStatus("mandatory")
_PoolNumDisks_Type = Integer32
_PoolNumDisks_Object = MibTableColumn
poolNumDisks = _PoolNumDisks_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 8, 1, 4),
    _PoolNumDisks_Type()
)
poolNumDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumDisks.setStatus("mandatory")
_PhysicalDiskTable_Object = MibTable
physicalDiskTable = _PhysicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9)
)
if mibBuilder.loadTexts:
    physicalDiskTable.setStatus("mandatory")
_PhysicalDiskEntry_Object = MibTableRow
physicalDiskEntry = _PhysicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1)
)
physicalDiskEntry.setIndexNames(
    (0, "SFA-INFO", "physDiskIndex"),
)
if mibBuilder.loadTexts:
    physicalDiskEntry.setStatus("mandatory")
_PhysDiskIndex_Type = Integer32
_PhysDiskIndex_Object = MibTableColumn
physDiskIndex = _PhysDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 1),
    _PhysDiskIndex_Type()
)
physDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physDiskIndex.setStatus("mandatory")
_PhysDiskPoolId_Type = Integer32
_PhysDiskPoolId_Object = MibTableColumn
physDiskPoolId = _PhysDiskPoolId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 2),
    _PhysDiskPoolId_Type()
)
physDiskPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physDiskPoolId.setStatus("mandatory")
_PhysDiskId_Type = Integer32
_PhysDiskId_Object = MibTableColumn
physDiskId = _PhysDiskId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 3),
    _PhysDiskId_Type()
)
physDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physDiskId.setStatus("mandatory")


class _PhysDiskWWN_Type(OctetString):
    """Custom type physDiskWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PhysDiskWWN_Type.__name__ = "OctetString"
_PhysDiskWWN_Object = MibTableColumn
physDiskWWN = _PhysDiskWWN_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 4),
    _PhysDiskWWN_Type()
)
physDiskWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physDiskWWN.setStatus("mandatory")


class _PhysDiskEnc_Type(OctetString):
    """Custom type physDiskEnc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PhysDiskEnc_Type.__name__ = "OctetString"
_PhysDiskEnc_Object = MibTableColumn
physDiskEnc = _PhysDiskEnc_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 5),
    _PhysDiskEnc_Type()
)
physDiskEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physDiskEnc.setStatus("mandatory")
_PhysDiskSlot_Type = Integer32
_PhysDiskSlot_Object = MibTableColumn
physDiskSlot = _PhysDiskSlot_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 6),
    _PhysDiskSlot_Type()
)
physDiskSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physDiskSlot.setStatus("mandatory")


class _PhysDiskState_Type(Integer32):
    """Custom type physDiskState based on Integer32"""
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
        *(("failed", 2),
          ("normal", 1),
          ("predictedfailure", 3),
          ("unknown", 4))
    )


_PhysDiskState_Type.__name__ = "Integer32"
_PhysDiskState_Object = MibTableColumn
physDiskState = _PhysDiskState_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 9, 1, 7),
    _PhysDiskState_Type()
)
physDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physDiskState.setStatus("mandatory")
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10)
)


class _EventLogTrapLevel_Type(Integer32):
    """Custom type eventLogTrapLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("none", 0),
          ("notice", 6),
          ("warning", 5))
    )


_EventLogTrapLevel_Type.__name__ = "Integer32"
_EventLogTrapLevel_Object = MibScalar
eventLogTrapLevel = _EventLogTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10, 1),
    _EventLogTrapLevel_Type()
)
eventLogTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTrapLevel.setStatus("mandatory")


class _EventLogNumEntries_Type(Integer32):
    """Custom type eventLogNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_EventLogNumEntries_Type.__name__ = "Integer32"
_EventLogNumEntries_Object = MibScalar
eventLogNumEntries = _EventLogNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10, 2),
    _EventLogNumEntries_Type()
)
eventLogNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogNumEntries.setStatus("mandatory")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10, 3)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1)
)
eventLogEntry.setIndexNames(
    (0, "SFA-INFO", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("mandatory")


class _EventLogIndex_Type(Integer32):
    """Custom type eventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_EventLogIndex_Type.__name__ = "Integer32"
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("mandatory")


class _EventLogLevel_Type(Integer32):
    """Custom type eventLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("none", 0),
          ("notice", 6),
          ("warning", 5))
    )


_EventLogLevel_Type.__name__ = "Integer32"
_EventLogLevel_Object = MibTableColumn
eventLogLevel = _EventLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 2),
    _EventLogLevel_Type()
)
eventLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogLevel.setStatus("mandatory")
_EventLogDescr_Type = DisplayString
_EventLogDescr_Object = MibTableColumn
eventLogDescr = _EventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 10, 3, 1, 3),
    _EventLogDescr_Type()
)
eventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDescr.setStatus("mandatory")


class _SystemName_Type(OctetString):
    """Custom type systemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SystemName_Type.__name__ = "OctetString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 2, 30),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFA-INFO",
    **{"DisplayString": DisplayString,
       "datadirect": datadirect,
       "unit": unit,
       "tempNumber": tempNumber,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempEncId": tempEncId,
       "tempEncPos": tempEncPos,
       "tempStatus": tempStatus,
       "fanNumber": fanNumber,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanEncId": fanEncId,
       "fanEncPos": fanEncPos,
       "fanStatus": fanStatus,
       "powerNumber": powerNumber,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerIndex": powerIndex,
       "powerEncId": powerEncId,
       "powerEncPos": powerEncPos,
       "powerStatus": powerStatus,
       "poolNumber": poolNumber,
       "poolTable": poolTable,
       "poolEntry": poolEntry,
       "poolIndex": poolIndex,
       "poolId": poolId,
       "poolType": poolType,
       "poolNumDisks": poolNumDisks,
       "physicalDiskTable": physicalDiskTable,
       "physicalDiskEntry": physicalDiskEntry,
       "physDiskIndex": physDiskIndex,
       "physDiskPoolId": physDiskPoolId,
       "physDiskId": physDiskId,
       "physDiskWWN": physDiskWWN,
       "physDiskEnc": physDiskEnc,
       "physDiskSlot": physDiskSlot,
       "physDiskState": physDiskState,
       "eventLog": eventLog,
       "eventLogTrapLevel": eventLogTrapLevel,
       "eventLogNumEntries": eventLogNumEntries,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogLevel": eventLogLevel,
       "eventLogDescr": eventLogDescr,
       "systemName": systemName}
)
