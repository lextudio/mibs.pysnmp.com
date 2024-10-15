# SNMP MIB module (InternetThruway-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/InternetThruway-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:33 2024
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



class TimeString(DisplayString):
    """Custom type TimeString based on DisplayString"""




class PartitionSpaceStatus(Integer32):
    """Custom type PartitionSpaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spaceAlarmOff", 1),
          ("spaceAlarmOn", 2))
    )





class ComponentIndex(Integer32):
    """Custom type ComponentIndex based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("arm", 3),
          ("climan", 2),
          ("hgm", 5),
          ("oolsproxy", 1),
          ("sem", 4),
          ("ss7cheni", 9),
          ("ss7opm", 8),
          ("ss7scm", 7),
          ("survman", 6))
    )





class ComponentSysmanState(Integer32):
    """Custom type ComponentSysmanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProvisionedState", 1),
          ("notInProvisionedState", 2),
          ("unknown", 3))
    )





class LinksetState(Integer32):
    """Custom type LinksetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unAvailable", 2))
    )





class LinkState(Integer32):
    """Custom type LinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unAvailable", 2))
    )





class LinkInhibitionState(Integer32):
    """Custom type LinkInhibitionState based on Integer32"""
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
        *(("localInhibited", 2),
          ("localRemoteInhibited", 4),
          ("remoteInhibited", 3),
          ("unInhibited", 1))
    )





class LinkCongestionState(Integer32):
    """Custom type LinkCongestionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congested", 2),
          ("notCongested", 1))
    )





class LinkAlignmentState(Integer32):
    """Custom type LinkAlignmentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aligned", 1),
          ("notAligned", 2))
    )





class RouteState(Integer32):
    """Custom type RouteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessible", 1),
          ("inaccessible", 2),
          ("restricted", 3))
    )





class DestinationState(Integer32):
    """Custom type DestinationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessible", 1),
          ("inaccessible", 2),
          ("restricted", 3))
    )





class UpgradeInProgress(Integer32):
    """Custom type UpgradeInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )





class MTP2AlarmConditionType(Integer32):
    """Custom type MTP2AlarmConditionType based on Integer32"""
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
        *(("aisRcv", 4),
          ("carrierLost", 2),
          ("fasError", 1),
          ("remoteAlarmRcv", 5),
          ("synchroLost", 3),
          ("tooHighBer", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nortel_ObjectIdentity = ObjectIdentity
nortel = _Nortel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562)
)
_Dialaccess_ObjectIdentity = ObjectIdentity
dialaccess = _Dialaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14)
)
_Csg_ObjectIdentity = ObjectIdentity
csg = _Csg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1)
)
_Disk_ObjectIdentity = ObjectIdentity
disk = _Disk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1)
)
_PartitionTable_Object = MibTable
partitionTable = _PartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    partitionTable.setStatus("mandatory")
_PartitionTableEntry_Object = MibTableRow
partitionTableEntry = _PartitionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1)
)
partitionTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "partitionIndex"),
)
if mibBuilder.loadTexts:
    partitionTableEntry.setStatus("mandatory")


class _PartitionIndex_Type(Integer32):
    """Custom type partitionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PartitionIndex_Type.__name__ = "Integer32"
_PartitionIndex_Object = MibTableColumn
partitionIndex = _PartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1, 1),
    _PartitionIndex_Type()
)
partitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    partitionIndex.setStatus("mandatory")
_PartitionName_Type = DisplayString
_PartitionName_Object = MibTableColumn
partitionName = _PartitionName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1, 2),
    _PartitionName_Type()
)
partitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionName.setStatus("mandatory")


class _PartitionPercentFull_Type(Integer32):
    """Custom type partitionPercentFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PartitionPercentFull_Type.__name__ = "Integer32"
_PartitionPercentFull_Object = MibTableColumn
partitionPercentFull = _PartitionPercentFull_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1, 3),
    _PartitionPercentFull_Type()
)
partitionPercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPercentFull.setStatus("mandatory")
_PartitionMegsFree_Type = Integer32
_PartitionMegsFree_Object = MibTableColumn
partitionMegsFree = _PartitionMegsFree_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1, 4),
    _PartitionMegsFree_Type()
)
partitionMegsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionMegsFree.setStatus("mandatory")
_PartitionSpaceStatus_Type = PartitionSpaceStatus
_PartitionSpaceStatus_Object = MibTableColumn
partitionSpaceStatus = _PartitionSpaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1, 5),
    _PartitionSpaceStatus_Type()
)
partitionSpaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSpaceStatus.setStatus("mandatory")
_PartitionSpaceKey_Type = Integer32
_PartitionSpaceKey_Object = MibTableColumn
partitionSpaceKey = _PartitionSpaceKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1, 6),
    _PartitionSpaceKey_Type()
)
partitionSpaceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSpaceKey.setStatus("mandatory")
_PartitionSpaceTimeStamp_Type = TimeString
_PartitionSpaceTimeStamp_Object = MibTableColumn
partitionSpaceTimeStamp = _PartitionSpaceTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 1, 1, 1, 1, 7),
    _PartitionSpaceTimeStamp_Type()
)
partitionSpaceTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSpaceTimeStamp.setStatus("mandatory")
_Components_ObjectIdentity = ObjectIdentity
components = _Components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2)
)
_ComponentTable_Object = MibTable
componentTable = _ComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10)
)
if mibBuilder.loadTexts:
    componentTable.setStatus("mandatory")
_ComponentTableEntry_Object = MibTableRow
componentTableEntry = _ComponentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1)
)
componentTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "componentIndex"),
)
if mibBuilder.loadTexts:
    componentTableEntry.setStatus("mandatory")
_ComponentIndex_Type = ComponentIndex
_ComponentIndex_Object = MibTableColumn
componentIndex = _ComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 1),
    _ComponentIndex_Type()
)
componentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentIndex.setStatus("mandatory")
_ComponentName_Type = DisplayString
_ComponentName_Object = MibTableColumn
componentName = _ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 2),
    _ComponentName_Type()
)
componentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentName.setStatus("mandatory")
_CompSecsInCurrentState_Type = Integer32
_CompSecsInCurrentState_Object = MibTableColumn
compSecsInCurrentState = _CompSecsInCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 3),
    _CompSecsInCurrentState_Type()
)
compSecsInCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compSecsInCurrentState.setStatus("mandatory")
_CompProvStateStatus_Type = ComponentSysmanState
_CompProvStateStatus_Object = MibTableColumn
compProvStateStatus = _CompProvStateStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 4),
    _CompProvStateStatus_Type()
)
compProvStateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compProvStateStatus.setStatus("mandatory")
_CompProvStateKey_Type = Integer32
_CompProvStateKey_Object = MibTableColumn
compProvStateKey = _CompProvStateKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 5),
    _CompProvStateKey_Type()
)
compProvStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compProvStateKey.setStatus("mandatory")
_CompProvStateTimeStamp_Type = TimeString
_CompProvStateTimeStamp_Object = MibTableColumn
compProvStateTimeStamp = _CompProvStateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 6),
    _CompProvStateTimeStamp_Type()
)
compProvStateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compProvStateTimeStamp.setStatus("mandatory")
_CompDebugStatus_Type = Integer32
_CompDebugStatus_Object = MibTableColumn
compDebugStatus = _CompDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 7),
    _CompDebugStatus_Type()
)
compDebugStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compDebugStatus.setStatus("mandatory")
_CompDebugKey_Type = Integer32
_CompDebugKey_Object = MibTableColumn
compDebugKey = _CompDebugKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 8),
    _CompDebugKey_Type()
)
compDebugKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compDebugKey.setStatus("mandatory")
_CompDebugTimeStamp_Type = TimeString
_CompDebugTimeStamp_Object = MibTableColumn
compDebugTimeStamp = _CompDebugTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 9),
    _CompDebugTimeStamp_Type()
)
compDebugTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compDebugTimeStamp.setStatus("mandatory")
_CompRestartStatus_Type = Integer32
_CompRestartStatus_Object = MibTableColumn
compRestartStatus = _CompRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 10),
    _CompRestartStatus_Type()
)
compRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compRestartStatus.setStatus("mandatory")
_CompRestartKey_Type = Integer32
_CompRestartKey_Object = MibTableColumn
compRestartKey = _CompRestartKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 11),
    _CompRestartKey_Type()
)
compRestartKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compRestartKey.setStatus("mandatory")
_CompRestartTimeStamp_Type = TimeString
_CompRestartTimeStamp_Object = MibTableColumn
compRestartTimeStamp = _CompRestartTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 2, 10, 1, 12),
    _CompRestartTimeStamp_Type()
)
compRestartTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compRestartTimeStamp.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3)
)
_TrapCompName_Type = DisplayString
_TrapCompName_Object = MibScalar
trapCompName = _TrapCompName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 1),
    _TrapCompName_Type()
)
trapCompName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapCompName.setStatus("mandatory")
_TrapFileName_Type = DisplayString
_TrapFileName_Object = MibScalar
trapFileName = _TrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 2),
    _TrapFileName_Type()
)
trapFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapFileName.setStatus("mandatory")
_TrapDate_Type = TimeString
_TrapDate_Object = MibScalar
trapDate = _TrapDate_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 3),
    _TrapDate_Type()
)
trapDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDate.setStatus("mandatory")
_TrapGenericStr1_Type = DisplayString
_TrapGenericStr1_Object = MibScalar
trapGenericStr1 = _TrapGenericStr1_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 4),
    _TrapGenericStr1_Type()
)
trapGenericStr1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapGenericStr1.setStatus("mandatory")
_TrapIdKey_Type = Integer32
_TrapIdKey_Object = MibScalar
trapIdKey = _TrapIdKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 5),
    _TrapIdKey_Type()
)
trapIdKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapIdKey.setStatus("mandatory")
_TrapIPAddress_Type = IpAddress
_TrapIPAddress_Object = MibScalar
trapIPAddress = _TrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 6),
    _TrapIPAddress_Type()
)
trapIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapIPAddress.setStatus("mandatory")
_TrapName_Type = DisplayString
_TrapName_Object = MibScalar
trapName = _TrapName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 7),
    _TrapName_Type()
)
trapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapName.setStatus("mandatory")
_TrapTimeStamp_Type = DisplayString
_TrapTimeStamp_Object = MibScalar
trapTimeStamp = _TrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 8),
    _TrapTimeStamp_Type()
)
trapTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapTimeStamp.setStatus("mandatory")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4)
)
_AlarmMaskInt1_Type = Gauge32
_AlarmMaskInt1_Object = MibScalar
alarmMaskInt1 = _AlarmMaskInt1_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 1),
    _AlarmMaskInt1_Type()
)
alarmMaskInt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaskInt1.setStatus("mandatory")
_AlarmStatusInt1_Type = Gauge32
_AlarmStatusInt1_Object = MibScalar
alarmStatusInt1 = _AlarmStatusInt1_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 2),
    _AlarmStatusInt1_Type()
)
alarmStatusInt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusInt1.setStatus("mandatory")
_AlarmStatusInt2_Type = Gauge32
_AlarmStatusInt2_Object = MibScalar
alarmStatusInt2 = _AlarmStatusInt2_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 3),
    _AlarmStatusInt2_Type()
)
alarmStatusInt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusInt2.setStatus("mandatory")
_AlarmStatusInt3_Type = Gauge32
_AlarmStatusInt3_Object = MibScalar
alarmStatusInt3 = _AlarmStatusInt3_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 4),
    _AlarmStatusInt3_Type()
)
alarmStatusInt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusInt3.setStatus("mandatory")
_AlarmMaskInt2_Type = Gauge32
_AlarmMaskInt2_Object = MibScalar
alarmMaskInt2 = _AlarmMaskInt2_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 5),
    _AlarmMaskInt2_Type()
)
alarmMaskInt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmMaskInt2.setStatus("mandatory")
_HgAlarmTable_Object = MibTable
hgAlarmTable = _HgAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 10)
)
if mibBuilder.loadTexts:
    hgAlarmTable.setStatus("mandatory")
_HgAlarmTableEntry_Object = MibTableRow
hgAlarmTableEntry = _HgAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 10, 1)
)
hgAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "hgIndex"),
)
if mibBuilder.loadTexts:
    hgAlarmTableEntry.setStatus("mandatory")
_HgIndex_Type = Integer32
_HgIndex_Object = MibTableColumn
hgIndex = _HgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 10, 1, 1),
    _HgIndex_Type()
)
hgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hgIndex.setStatus("mandatory")
_HgName_Type = DisplayString
_HgName_Object = MibTableColumn
hgName = _HgName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 10, 1, 2),
    _HgName_Type()
)
hgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgName.setStatus("mandatory")
_HgKey_Type = Integer32
_HgKey_Object = MibTableColumn
hgKey = _HgKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 10, 1, 3),
    _HgKey_Type()
)
hgKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgKey.setStatus("mandatory")
_HgAlarmTimeStamp_Type = TimeString
_HgAlarmTimeStamp_Object = MibTableColumn
hgAlarmTimeStamp = _HgAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 10, 1, 4),
    _HgAlarmTimeStamp_Type()
)
hgAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgAlarmTimeStamp.setStatus("mandatory")
_HgIPAddress_Type = IpAddress
_HgIPAddress_Object = MibTableColumn
hgIPAddress = _HgIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 10, 1, 5),
    _HgIPAddress_Type()
)
hgIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hgIPAddress.setStatus("mandatory")
_NasAlarmTable_Object = MibTable
nasAlarmTable = _NasAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11)
)
if mibBuilder.loadTexts:
    nasAlarmTable.setStatus("mandatory")
_NasAlarmTableEntry_Object = MibTableRow
nasAlarmTableEntry = _NasAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11, 1)
)
nasAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "nasIndex"),
)
if mibBuilder.loadTexts:
    nasAlarmTableEntry.setStatus("mandatory")
_NasIndex_Type = Integer32
_NasIndex_Object = MibTableColumn
nasIndex = _NasIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11, 1, 1),
    _NasIndex_Type()
)
nasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasIndex.setStatus("mandatory")
_NasName_Type = DisplayString
_NasName_Object = MibTableColumn
nasName = _NasName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11, 1, 2),
    _NasName_Type()
)
nasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasName.setStatus("mandatory")
_NasKey_Type = Integer32
_NasKey_Object = MibTableColumn
nasKey = _NasKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11, 1, 3),
    _NasKey_Type()
)
nasKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasKey.setStatus("mandatory")
_NasAlarmTimeStamp_Type = TimeString
_NasAlarmTimeStamp_Object = MibTableColumn
nasAlarmTimeStamp = _NasAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11, 1, 4),
    _NasAlarmTimeStamp_Type()
)
nasAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasAlarmTimeStamp.setStatus("mandatory")
_NasIPAddress_Type = IpAddress
_NasIPAddress_Object = MibTableColumn
nasIPAddress = _NasIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11, 1, 5),
    _NasIPAddress_Type()
)
nasIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasIPAddress.setStatus("mandatory")
_NasCmplxName_Type = DisplayString
_NasCmplxName_Object = MibTableColumn
nasCmplxName = _NasCmplxName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 11, 1, 6),
    _NasCmplxName_Type()
)
nasCmplxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCmplxName.setStatus("mandatory")
_Ss7LinkFailureAlarmTable_Object = MibTable
ss7LinkFailureAlarmTable = _Ss7LinkFailureAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12)
)
if mibBuilder.loadTexts:
    ss7LinkFailureAlarmTable.setStatus("mandatory")
_Ss7LinkFailureAlarmTableEntry_Object = MibTableRow
ss7LinkFailureAlarmTableEntry = _Ss7LinkFailureAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1)
)
ss7LinkFailureAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "lfIndex"),
)
if mibBuilder.loadTexts:
    ss7LinkFailureAlarmTableEntry.setStatus("mandatory")
_LfIndex_Type = Integer32
_LfIndex_Object = MibTableColumn
lfIndex = _LfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 1),
    _LfIndex_Type()
)
lfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lfIndex.setStatus("mandatory")
_LfKey_Type = Integer32
_LfKey_Object = MibTableColumn
lfKey = _LfKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 2),
    _LfKey_Type()
)
lfKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfKey.setStatus("mandatory")
_LfIPAddress_Type = IpAddress
_LfIPAddress_Object = MibTableColumn
lfIPAddress = _LfIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 3),
    _LfIPAddress_Type()
)
lfIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfIPAddress.setStatus("mandatory")
_LfLinkCode_Type = Integer32
_LfLinkCode_Object = MibTableColumn
lfLinkCode = _LfLinkCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 5),
    _LfLinkCode_Type()
)
lfLinkCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfLinkCode.setStatus("mandatory")
_LfTimeStamp_Type = TimeString
_LfTimeStamp_Object = MibTableColumn
lfTimeStamp = _LfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 6),
    _LfTimeStamp_Type()
)
lfTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfTimeStamp.setStatus("mandatory")
_LfName_Type = DisplayString
_LfName_Object = MibTableColumn
lfName = _LfName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 7),
    _LfName_Type()
)
lfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfName.setStatus("mandatory")
_LfCardId_Type = DisplayString
_LfCardId_Object = MibTableColumn
lfCardId = _LfCardId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 8),
    _LfCardId_Type()
)
lfCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfCardId.setStatus("mandatory")
_LfLinkSet_Type = DisplayString
_LfLinkSet_Object = MibTableColumn
lfLinkSet = _LfLinkSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 12, 1, 9),
    _LfLinkSet_Type()
)
lfLinkSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfLinkSet.setStatus("mandatory")
_Ss7LinkCongestionAlarmTable_Object = MibTable
ss7LinkCongestionAlarmTable = _Ss7LinkCongestionAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13)
)
if mibBuilder.loadTexts:
    ss7LinkCongestionAlarmTable.setStatus("mandatory")
_Ss7LinkCongestionAlarmTableEntry_Object = MibTableRow
ss7LinkCongestionAlarmTableEntry = _Ss7LinkCongestionAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1)
)
ss7LinkCongestionAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "lcIndex"),
)
if mibBuilder.loadTexts:
    ss7LinkCongestionAlarmTableEntry.setStatus("mandatory")
_LcIndex_Type = Integer32
_LcIndex_Object = MibTableColumn
lcIndex = _LcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 1),
    _LcIndex_Type()
)
lcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lcIndex.setStatus("mandatory")
_LcKey_Type = Integer32
_LcKey_Object = MibTableColumn
lcKey = _LcKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 2),
    _LcKey_Type()
)
lcKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcKey.setStatus("mandatory")
_LcIPAddress_Type = IpAddress
_LcIPAddress_Object = MibTableColumn
lcIPAddress = _LcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 3),
    _LcIPAddress_Type()
)
lcIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcIPAddress.setStatus("mandatory")
_LcLinkCode_Type = Integer32
_LcLinkCode_Object = MibTableColumn
lcLinkCode = _LcLinkCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 4),
    _LcLinkCode_Type()
)
lcLinkCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLinkCode.setStatus("mandatory")
_LcTimeStamp_Type = TimeString
_LcTimeStamp_Object = MibTableColumn
lcTimeStamp = _LcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 5),
    _LcTimeStamp_Type()
)
lcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcTimeStamp.setStatus("mandatory")
_LcName_Type = DisplayString
_LcName_Object = MibTableColumn
lcName = _LcName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 6),
    _LcName_Type()
)
lcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcName.setStatus("mandatory")
_LcCardId_Type = DisplayString
_LcCardId_Object = MibTableColumn
lcCardId = _LcCardId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 7),
    _LcCardId_Type()
)
lcCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcCardId.setStatus("mandatory")
_LcLinkSet_Type = DisplayString
_LcLinkSet_Object = MibTableColumn
lcLinkSet = _LcLinkSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 13, 1, 8),
    _LcLinkSet_Type()
)
lcLinkSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcLinkSet.setStatus("mandatory")
_Ss7ISUPFailureAlarmTable_Object = MibTable
ss7ISUPFailureAlarmTable = _Ss7ISUPFailureAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 14)
)
if mibBuilder.loadTexts:
    ss7ISUPFailureAlarmTable.setStatus("mandatory")
_Ss7ISUPFailureAlarmTableEntry_Object = MibTableRow
ss7ISUPFailureAlarmTableEntry = _Ss7ISUPFailureAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 14, 1)
)
ss7ISUPFailureAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ss7ISUPFailureAlarmTableEntry.setStatus("mandatory")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 14, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIndex.setStatus("mandatory")
_IfKey_Type = Integer32
_IfKey_Object = MibTableColumn
ifKey = _IfKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 14, 1, 2),
    _IfKey_Type()
)
ifKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifKey.setStatus("mandatory")
_IfIPAddress_Type = IpAddress
_IfIPAddress_Object = MibTableColumn
ifIPAddress = _IfIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 14, 1, 3),
    _IfIPAddress_Type()
)
ifIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIPAddress.setStatus("mandatory")
_IfTimeStamp_Type = TimeString
_IfTimeStamp_Object = MibTableColumn
ifTimeStamp = _IfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 14, 1, 4),
    _IfTimeStamp_Type()
)
ifTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTimeStamp.setStatus("mandatory")
_IfName_Type = DisplayString
_IfName_Object = MibTableColumn
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 14, 1, 5),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("mandatory")
_Ss7ISUPCongestionAlarmTable_Object = MibTable
ss7ISUPCongestionAlarmTable = _Ss7ISUPCongestionAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15)
)
if mibBuilder.loadTexts:
    ss7ISUPCongestionAlarmTable.setStatus("mandatory")
_Ss7ISUPCongestionAlarmTableEntry_Object = MibTableRow
ss7ISUPCongestionAlarmTableEntry = _Ss7ISUPCongestionAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15, 1)
)
ss7ISUPCongestionAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "icIndex"),
)
if mibBuilder.loadTexts:
    ss7ISUPCongestionAlarmTableEntry.setStatus("mandatory")
_IcIndex_Type = Integer32
_IcIndex_Object = MibTableColumn
icIndex = _IcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15, 1, 1),
    _IcIndex_Type()
)
icIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icIndex.setStatus("mandatory")
_IcKey_Type = Integer32
_IcKey_Object = MibTableColumn
icKey = _IcKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15, 1, 2),
    _IcKey_Type()
)
icKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icKey.setStatus("mandatory")
_IcIPAddress_Type = IpAddress
_IcIPAddress_Object = MibTableColumn
icIPAddress = _IcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15, 1, 3),
    _IcIPAddress_Type()
)
icIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icIPAddress.setStatus("mandatory")
_IcCongestionLevel_Type = Integer32
_IcCongestionLevel_Object = MibTableColumn
icCongestionLevel = _IcCongestionLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15, 1, 4),
    _IcCongestionLevel_Type()
)
icCongestionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icCongestionLevel.setStatus("mandatory")
_IcTimeStamp_Type = TimeString
_IcTimeStamp_Object = MibTableColumn
icTimeStamp = _IcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15, 1, 5),
    _IcTimeStamp_Type()
)
icTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTimeStamp.setStatus("mandatory")
_IcName_Type = DisplayString
_IcName_Object = MibTableColumn
icName = _IcName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 15, 1, 6),
    _IcName_Type()
)
icName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icName.setStatus("mandatory")
_Ss7MTP3CongestionAlarmTable_Object = MibTable
ss7MTP3CongestionAlarmTable = _Ss7MTP3CongestionAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16)
)
if mibBuilder.loadTexts:
    ss7MTP3CongestionAlarmTable.setStatus("mandatory")
_Ss7MTP3CongestionAlarmTableEntry_Object = MibTableRow
ss7MTP3CongestionAlarmTableEntry = _Ss7MTP3CongestionAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16, 1)
)
ss7MTP3CongestionAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "mtp3Index"),
)
if mibBuilder.loadTexts:
    ss7MTP3CongestionAlarmTableEntry.setStatus("mandatory")
_Mtp3Index_Type = Integer32
_Mtp3Index_Object = MibTableColumn
mtp3Index = _Mtp3Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16, 1, 1),
    _Mtp3Index_Type()
)
mtp3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtp3Index.setStatus("mandatory")
_Mtp3Key_Type = Integer32
_Mtp3Key_Object = MibTableColumn
mtp3Key = _Mtp3Key_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16, 1, 2),
    _Mtp3Key_Type()
)
mtp3Key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3Key.setStatus("mandatory")
_Mtp3IPAddress_Type = IpAddress
_Mtp3IPAddress_Object = MibTableColumn
mtp3IPAddress = _Mtp3IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16, 1, 3),
    _Mtp3IPAddress_Type()
)
mtp3IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3IPAddress.setStatus("mandatory")
_Mtp3CongestionLevel_Type = Integer32
_Mtp3CongestionLevel_Object = MibTableColumn
mtp3CongestionLevel = _Mtp3CongestionLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16, 1, 4),
    _Mtp3CongestionLevel_Type()
)
mtp3CongestionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3CongestionLevel.setStatus("mandatory")
_Mtp3TimeStamp_Type = TimeString
_Mtp3TimeStamp_Object = MibTableColumn
mtp3TimeStamp = _Mtp3TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16, 1, 5),
    _Mtp3TimeStamp_Type()
)
mtp3TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3TimeStamp.setStatus("mandatory")
_Mtp3Name_Type = DisplayString
_Mtp3Name_Object = MibTableColumn
mtp3Name = _Mtp3Name_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 16, 1, 6),
    _Mtp3Name_Type()
)
mtp3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3Name.setStatus("mandatory")
_Ss7MTP2TrunkFailureAlarmTable_Object = MibTable
ss7MTP2TrunkFailureAlarmTable = _Ss7MTP2TrunkFailureAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17)
)
if mibBuilder.loadTexts:
    ss7MTP2TrunkFailureAlarmTable.setStatus("mandatory")
_Ss7MTP2TrunkFailureAlarmTableEntry_Object = MibTableRow
ss7MTP2TrunkFailureAlarmTableEntry = _Ss7MTP2TrunkFailureAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1)
)
ss7MTP2TrunkFailureAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "mtp2Index"),
)
if mibBuilder.loadTexts:
    ss7MTP2TrunkFailureAlarmTableEntry.setStatus("mandatory")
_Mtp2Index_Type = Integer32
_Mtp2Index_Object = MibTableColumn
mtp2Index = _Mtp2Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1, 1),
    _Mtp2Index_Type()
)
mtp2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtp2Index.setStatus("mandatory")
_Mtp2Key_Type = Integer32
_Mtp2Key_Object = MibTableColumn
mtp2Key = _Mtp2Key_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1, 2),
    _Mtp2Key_Type()
)
mtp2Key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp2Key.setStatus("mandatory")
_Mtp2IPAddress_Type = IpAddress
_Mtp2IPAddress_Object = MibTableColumn
mtp2IPAddress = _Mtp2IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1, 3),
    _Mtp2IPAddress_Type()
)
mtp2IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp2IPAddress.setStatus("mandatory")
_Mtp2Name_Type = DisplayString
_Mtp2Name_Object = MibTableColumn
mtp2Name = _Mtp2Name_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1, 4),
    _Mtp2Name_Type()
)
mtp2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp2Name.setStatus("mandatory")
_Mtp2CardId_Type = DisplayString
_Mtp2CardId_Object = MibTableColumn
mtp2CardId = _Mtp2CardId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1, 5),
    _Mtp2CardId_Type()
)
mtp2CardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp2CardId.setStatus("mandatory")
_Mtp2AlarmCondition_Type = MTP2AlarmConditionType
_Mtp2AlarmCondition_Object = MibTableColumn
mtp2AlarmCondition = _Mtp2AlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1, 6),
    _Mtp2AlarmCondition_Type()
)
mtp2AlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp2AlarmCondition.setStatus("mandatory")
_Mtp2TimeStamp_Type = TimeString
_Mtp2TimeStamp_Object = MibTableColumn
mtp2TimeStamp = _Mtp2TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 17, 1, 7),
    _Mtp2TimeStamp_Type()
)
mtp2TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp2TimeStamp.setStatus("mandatory")
_Ss7LinksetFailureAlarmTable_Object = MibTable
ss7LinksetFailureAlarmTable = _Ss7LinksetFailureAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18)
)
if mibBuilder.loadTexts:
    ss7LinksetFailureAlarmTable.setStatus("mandatory")
_Ss7LinksetFailureAlarmTableEntry_Object = MibTableRow
ss7LinksetFailureAlarmTableEntry = _Ss7LinksetFailureAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18, 1)
)
ss7LinksetFailureAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "lsFailureIndex"),
)
if mibBuilder.loadTexts:
    ss7LinksetFailureAlarmTableEntry.setStatus("mandatory")
_LsFailureIndex_Type = Integer32
_LsFailureIndex_Object = MibTableColumn
lsFailureIndex = _LsFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18, 1, 1),
    _LsFailureIndex_Type()
)
lsFailureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lsFailureIndex.setStatus("mandatory")
_LsFailureKey_Type = Integer32
_LsFailureKey_Object = MibTableColumn
lsFailureKey = _LsFailureKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18, 1, 2),
    _LsFailureKey_Type()
)
lsFailureKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFailureKey.setStatus("mandatory")
_LsFailureIPAddress_Type = IpAddress
_LsFailureIPAddress_Object = MibTableColumn
lsFailureIPAddress = _LsFailureIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18, 1, 3),
    _LsFailureIPAddress_Type()
)
lsFailureIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFailureIPAddress.setStatus("mandatory")
_LsFailureName_Type = DisplayString
_LsFailureName_Object = MibTableColumn
lsFailureName = _LsFailureName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18, 1, 4),
    _LsFailureName_Type()
)
lsFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFailureName.setStatus("mandatory")
_LsFailurePointcode_Type = DisplayString
_LsFailurePointcode_Object = MibTableColumn
lsFailurePointcode = _LsFailurePointcode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18, 1, 5),
    _LsFailurePointcode_Type()
)
lsFailurePointcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFailurePointcode.setStatus("mandatory")
_LsFailureTimeStamp_Type = TimeString
_LsFailureTimeStamp_Object = MibTableColumn
lsFailureTimeStamp = _LsFailureTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 18, 1, 6),
    _LsFailureTimeStamp_Type()
)
lsFailureTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFailureTimeStamp.setStatus("mandatory")
_Ss7DestinationInaccessibleAlarmTable_Object = MibTable
ss7DestinationInaccessibleAlarmTable = _Ss7DestinationInaccessibleAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19)
)
if mibBuilder.loadTexts:
    ss7DestinationInaccessibleAlarmTable.setStatus("mandatory")
_Ss7DestinationInaccessibleAlarmTableEntry_Object = MibTableRow
ss7DestinationInaccessibleAlarmTableEntry = _Ss7DestinationInaccessibleAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19, 1)
)
ss7DestinationInaccessibleAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "destInaccessIndex"),
)
if mibBuilder.loadTexts:
    ss7DestinationInaccessibleAlarmTableEntry.setStatus("mandatory")
_DestInaccessIndex_Type = Integer32
_DestInaccessIndex_Object = MibTableColumn
destInaccessIndex = _DestInaccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19, 1, 1),
    _DestInaccessIndex_Type()
)
destInaccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    destInaccessIndex.setStatus("mandatory")
_DestInaccessKey_Type = Integer32
_DestInaccessKey_Object = MibTableColumn
destInaccessKey = _DestInaccessKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19, 1, 2),
    _DestInaccessKey_Type()
)
destInaccessKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destInaccessKey.setStatus("mandatory")
_DestInaccessIPAddress_Type = IpAddress
_DestInaccessIPAddress_Object = MibTableColumn
destInaccessIPAddress = _DestInaccessIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19, 1, 3),
    _DestInaccessIPAddress_Type()
)
destInaccessIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destInaccessIPAddress.setStatus("mandatory")
_DestInaccessName_Type = DisplayString
_DestInaccessName_Object = MibTableColumn
destInaccessName = _DestInaccessName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19, 1, 4),
    _DestInaccessName_Type()
)
destInaccessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destInaccessName.setStatus("mandatory")
_DestInaccessPointcode_Type = DisplayString
_DestInaccessPointcode_Object = MibTableColumn
destInaccessPointcode = _DestInaccessPointcode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19, 1, 5),
    _DestInaccessPointcode_Type()
)
destInaccessPointcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destInaccessPointcode.setStatus("mandatory")
_DestInaccessTimeStamp_Type = TimeString
_DestInaccessTimeStamp_Object = MibTableColumn
destInaccessTimeStamp = _DestInaccessTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 19, 1, 6),
    _DestInaccessTimeStamp_Type()
)
destInaccessTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destInaccessTimeStamp.setStatus("mandatory")
_Ss7DestinationCongestedAlarmTable_Object = MibTable
ss7DestinationCongestedAlarmTable = _Ss7DestinationCongestedAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20)
)
if mibBuilder.loadTexts:
    ss7DestinationCongestedAlarmTable.setStatus("mandatory")
_Ss7DestinationCongestedAlarmTableEntry_Object = MibTableRow
ss7DestinationCongestedAlarmTableEntry = _Ss7DestinationCongestedAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1)
)
ss7DestinationCongestedAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "destCongestIndex"),
)
if mibBuilder.loadTexts:
    ss7DestinationCongestedAlarmTableEntry.setStatus("mandatory")
_DestCongestIndex_Type = Integer32
_DestCongestIndex_Object = MibTableColumn
destCongestIndex = _DestCongestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1, 1),
    _DestCongestIndex_Type()
)
destCongestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    destCongestIndex.setStatus("mandatory")
_DestCongestKey_Type = Integer32
_DestCongestKey_Object = MibTableColumn
destCongestKey = _DestCongestKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1, 2),
    _DestCongestKey_Type()
)
destCongestKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destCongestKey.setStatus("mandatory")
_DestCongestIPAddress_Type = IpAddress
_DestCongestIPAddress_Object = MibTableColumn
destCongestIPAddress = _DestCongestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1, 3),
    _DestCongestIPAddress_Type()
)
destCongestIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destCongestIPAddress.setStatus("mandatory")
_DestCongestName_Type = DisplayString
_DestCongestName_Object = MibTableColumn
destCongestName = _DestCongestName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1, 4),
    _DestCongestName_Type()
)
destCongestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destCongestName.setStatus("mandatory")
_DestCongestPointcode_Type = DisplayString
_DestCongestPointcode_Object = MibTableColumn
destCongestPointcode = _DestCongestPointcode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1, 5),
    _DestCongestPointcode_Type()
)
destCongestPointcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destCongestPointcode.setStatus("mandatory")
_DestCongestCongestionLevel_Type = Integer32
_DestCongestCongestionLevel_Object = MibTableColumn
destCongestCongestionLevel = _DestCongestCongestionLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1, 6),
    _DestCongestCongestionLevel_Type()
)
destCongestCongestionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destCongestCongestionLevel.setStatus("mandatory")
_DestCongestTimeStamp_Type = TimeString
_DestCongestTimeStamp_Object = MibTableColumn
destCongestTimeStamp = _DestCongestTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 20, 1, 7),
    _DestCongestTimeStamp_Type()
)
destCongestTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destCongestTimeStamp.setStatus("mandatory")
_Ss7LinkAlignmentAlarmTable_Object = MibTable
ss7LinkAlignmentAlarmTable = _Ss7LinkAlignmentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21)
)
if mibBuilder.loadTexts:
    ss7LinkAlignmentAlarmTable.setStatus("mandatory")
_Ss7LinkAlignmentAlarmTableEntry_Object = MibTableRow
ss7LinkAlignmentAlarmTableEntry = _Ss7LinkAlignmentAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1)
)
ss7LinkAlignmentAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "linkAlignIndex"),
)
if mibBuilder.loadTexts:
    ss7LinkAlignmentAlarmTableEntry.setStatus("mandatory")
_LinkAlignIndex_Type = Integer32
_LinkAlignIndex_Object = MibTableColumn
linkAlignIndex = _LinkAlignIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 1),
    _LinkAlignIndex_Type()
)
linkAlignIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkAlignIndex.setStatus("mandatory")
_LinkAlignKey_Type = Integer32
_LinkAlignKey_Object = MibTableColumn
linkAlignKey = _LinkAlignKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 2),
    _LinkAlignKey_Type()
)
linkAlignKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignKey.setStatus("mandatory")
_LinkAlignIPAddress_Type = IpAddress
_LinkAlignIPAddress_Object = MibTableColumn
linkAlignIPAddress = _LinkAlignIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 3),
    _LinkAlignIPAddress_Type()
)
linkAlignIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignIPAddress.setStatus("mandatory")
_LinkAlignName_Type = DisplayString
_LinkAlignName_Object = MibTableColumn
linkAlignName = _LinkAlignName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 4),
    _LinkAlignName_Type()
)
linkAlignName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignName.setStatus("mandatory")
_LinkAlignLinkCode_Type = Integer32
_LinkAlignLinkCode_Object = MibTableColumn
linkAlignLinkCode = _LinkAlignLinkCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 5),
    _LinkAlignLinkCode_Type()
)
linkAlignLinkCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignLinkCode.setStatus("mandatory")
_LinkAlignTimeStamp_Type = TimeString
_LinkAlignTimeStamp_Object = MibTableColumn
linkAlignTimeStamp = _LinkAlignTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 6),
    _LinkAlignTimeStamp_Type()
)
linkAlignTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignTimeStamp.setStatus("mandatory")
_LinkAlignCardId_Type = DisplayString
_LinkAlignCardId_Object = MibTableColumn
linkAlignCardId = _LinkAlignCardId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 7),
    _LinkAlignCardId_Type()
)
linkAlignCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignCardId.setStatus("mandatory")
_LinkAlignLinkSet_Type = DisplayString
_LinkAlignLinkSet_Object = MibTableColumn
linkAlignLinkSet = _LinkAlignLinkSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 21, 1, 8),
    _LinkAlignLinkSet_Type()
)
linkAlignLinkSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignLinkSet.setStatus("mandatory")
_CsgComplexStateTrapInfo_ObjectIdentity = ObjectIdentity
csgComplexStateTrapInfo = _CsgComplexStateTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22)
)
_CplxName_Type = DisplayString
_CplxName_Object = MibScalar
cplxName = _CplxName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 1),
    _CplxName_Type()
)
cplxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxName.setStatus("mandatory")
_CplxLocEthernetName_Type = DisplayString
_CplxLocEthernetName_Object = MibScalar
cplxLocEthernetName = _CplxLocEthernetName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 2),
    _CplxLocEthernetName_Type()
)
cplxLocEthernetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxLocEthernetName.setStatus("mandatory")
_CplxLocEthernetIP_Type = IpAddress
_CplxLocEthernetIP_Object = MibScalar
cplxLocEthernetIP = _CplxLocEthernetIP_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 3),
    _CplxLocEthernetIP_Type()
)
cplxLocEthernetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxLocEthernetIP.setStatus("mandatory")
_CplxLocOperationalState_Type = DisplayString
_CplxLocOperationalState_Object = MibScalar
cplxLocOperationalState = _CplxLocOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 4),
    _CplxLocOperationalState_Type()
)
cplxLocOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxLocOperationalState.setStatus("mandatory")
_CplxLocStandbyState_Type = DisplayString
_CplxLocStandbyState_Object = MibScalar
cplxLocStandbyState = _CplxLocStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 5),
    _CplxLocStandbyState_Type()
)
cplxLocStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxLocStandbyState.setStatus("mandatory")
_CplxLocAvailabilityState_Type = DisplayString
_CplxLocAvailabilityState_Object = MibScalar
cplxLocAvailabilityState = _CplxLocAvailabilityState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 6),
    _CplxLocAvailabilityState_Type()
)
cplxLocAvailabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxLocAvailabilityState.setStatus("mandatory")
_CplxMateEthernetName_Type = DisplayString
_CplxMateEthernetName_Object = MibScalar
cplxMateEthernetName = _CplxMateEthernetName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 7),
    _CplxMateEthernetName_Type()
)
cplxMateEthernetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxMateEthernetName.setStatus("mandatory")
_CplxMateEthernetIP_Type = IpAddress
_CplxMateEthernetIP_Object = MibScalar
cplxMateEthernetIP = _CplxMateEthernetIP_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 8),
    _CplxMateEthernetIP_Type()
)
cplxMateEthernetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxMateEthernetIP.setStatus("mandatory")
_CplxMateOperationalState_Type = DisplayString
_CplxMateOperationalState_Object = MibScalar
cplxMateOperationalState = _CplxMateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 9),
    _CplxMateOperationalState_Type()
)
cplxMateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxMateOperationalState.setStatus("mandatory")
_CplxMateStandbyState_Type = DisplayString
_CplxMateStandbyState_Object = MibScalar
cplxMateStandbyState = _CplxMateStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 10),
    _CplxMateStandbyState_Type()
)
cplxMateStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxMateStandbyState.setStatus("mandatory")
_CplxMateAvailabilityState_Type = DisplayString
_CplxMateAvailabilityState_Object = MibScalar
cplxMateAvailabilityState = _CplxMateAvailabilityState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 11),
    _CplxMateAvailabilityState_Type()
)
cplxMateAvailabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxMateAvailabilityState.setStatus("mandatory")
_CplxAlarmStatus_Type = DisplayString
_CplxAlarmStatus_Object = MibScalar
cplxAlarmStatus = _CplxAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 4, 22, 12),
    _CplxAlarmStatus_Type()
)
cplxAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cplxAlarmStatus.setStatus("mandatory")
_NcServer_ObjectIdentity = ObjectIdentity
ncServer = _NcServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5)
)
_LostServerAlarmTable_Object = MibTable
lostServerAlarmTable = _LostServerAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lostServerAlarmTable.setStatus("mandatory")
_LostServerAlarmTableEntry_Object = MibTableRow
lostServerAlarmTableEntry = _LostServerAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 1, 1)
)
lostServerAlarmTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "lsIndex"),
)
if mibBuilder.loadTexts:
    lostServerAlarmTableEntry.setStatus("mandatory")
_LsIndex_Type = Integer32
_LsIndex_Object = MibTableColumn
lsIndex = _LsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 1, 1, 1),
    _LsIndex_Type()
)
lsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lsIndex.setStatus("mandatory")
_LsKey_Type = Integer32
_LsKey_Object = MibTableColumn
lsKey = _LsKey_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 1, 1, 2),
    _LsKey_Type()
)
lsKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsKey.setStatus("mandatory")
_LsIPAddress_Type = IpAddress
_LsIPAddress_Object = MibTableColumn
lsIPAddress = _LsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 1, 1, 3),
    _LsIPAddress_Type()
)
lsIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsIPAddress.setStatus("mandatory")
_LsName_Type = DisplayString
_LsName_Object = MibTableColumn
lsName = _LsName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 1, 1, 4),
    _LsName_Type()
)
lsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsName.setStatus("mandatory")
_LsTimeStamp_Type = TimeString
_LsTimeStamp_Object = MibTableColumn
lsTimeStamp = _LsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 1, 1, 5),
    _LsTimeStamp_Type()
)
lsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsTimeStamp.setStatus("mandatory")
_NcServerId_Type = Integer32
_NcServerId_Object = MibScalar
ncServerId = _NcServerId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 2),
    _NcServerId_Type()
)
ncServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncServerId.setStatus("mandatory")
_NcServerName_Type = DisplayString
_NcServerName_Object = MibScalar
ncServerName = _NcServerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 3),
    _NcServerName_Type()
)
ncServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncServerName.setStatus("mandatory")
_NcHostName_Type = DisplayString
_NcHostName_Object = MibScalar
ncHostName = _NcHostName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 4),
    _NcHostName_Type()
)
ncHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncHostName.setStatus("mandatory")
_NcEthernetName_Type = DisplayString
_NcEthernetName_Object = MibScalar
ncEthernetName = _NcEthernetName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 5),
    _NcEthernetName_Type()
)
ncEthernetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncEthernetName.setStatus("mandatory")
_NcEthernetIP_Type = IpAddress
_NcEthernetIP_Object = MibScalar
ncEthernetIP = _NcEthernetIP_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 6),
    _NcEthernetIP_Type()
)
ncEthernetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncEthernetIP.setStatus("mandatory")
_NcClusterName_Type = DisplayString
_NcClusterName_Object = MibScalar
ncClusterName = _NcClusterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 7),
    _NcClusterName_Type()
)
ncClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncClusterName.setStatus("mandatory")
_NcClusterIP_Type = IpAddress
_NcClusterIP_Object = MibScalar
ncClusterIP = _NcClusterIP_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 8),
    _NcClusterIP_Type()
)
ncClusterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncClusterIP.setStatus("mandatory")
_NcOperationalState_Type = DisplayString
_NcOperationalState_Object = MibScalar
ncOperationalState = _NcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 9),
    _NcOperationalState_Type()
)
ncOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncOperationalState.setStatus("mandatory")
_NcStandbyState_Type = DisplayString
_NcStandbyState_Object = MibScalar
ncStandbyState = _NcStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 10),
    _NcStandbyState_Type()
)
ncStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStandbyState.setStatus("mandatory")
_NcAvailabilityState_Type = DisplayString
_NcAvailabilityState_Object = MibScalar
ncAvailabilityState = _NcAvailabilityState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 11),
    _NcAvailabilityState_Type()
)
ncAvailabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncAvailabilityState.setStatus("mandatory")
_NcSoftwareVersion_Type = DisplayString
_NcSoftwareVersion_Object = MibScalar
ncSoftwareVersion = _NcSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 12),
    _NcSoftwareVersion_Type()
)
ncSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncSoftwareVersion.setStatus("mandatory")
_NcUpgradeInProgress_Type = UpgradeInProgress
_NcUpgradeInProgress_Object = MibScalar
ncUpgradeInProgress = _NcUpgradeInProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 5, 13),
    _NcUpgradeInProgress_Type()
)
ncUpgradeInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncUpgradeInProgress.setStatus("mandatory")
_Ss7_ObjectIdentity = ObjectIdentity
ss7 = _Ss7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6)
)
_LinksetTable_Object = MibTable
linksetTable = _LinksetTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 1)
)
if mibBuilder.loadTexts:
    linksetTable.setStatus("mandatory")
_LinksetTableEntry_Object = MibTableRow
linksetTableEntry = _LinksetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 1, 1)
)
linksetTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "linksetIndex"),
)
if mibBuilder.loadTexts:
    linksetTableEntry.setStatus("mandatory")
_LinksetIndex_Type = Integer32
_LinksetIndex_Object = MibTableColumn
linksetIndex = _LinksetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 1, 1, 1),
    _LinksetIndex_Type()
)
linksetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linksetIndex.setStatus("mandatory")
_LinksetId_Type = Integer32
_LinksetId_Object = MibTableColumn
linksetId = _LinksetId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 1, 1, 2),
    _LinksetId_Type()
)
linksetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linksetId.setStatus("mandatory")
_LinksetAdjPointcode_Type = Integer32
_LinksetAdjPointcode_Object = MibTableColumn
linksetAdjPointcode = _LinksetAdjPointcode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 1, 1, 3),
    _LinksetAdjPointcode_Type()
)
linksetAdjPointcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linksetAdjPointcode.setStatus("mandatory")
_LinksetState_Type = LinksetState
_LinksetState_Object = MibTableColumn
linksetState = _LinksetState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 1, 1, 4),
    _LinksetState_Type()
)
linksetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linksetState.setStatus("mandatory")
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("mandatory")
_LinkTableEntry_Object = MibTableRow
linkTableEntry = _LinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1)
)
linkTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "linksetIndex"),
    (0, "InternetThruway-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkTableEntry.setStatus("mandatory")
_LinkIndex_Type = Integer32
_LinkIndex_Object = MibTableColumn
linkIndex = _LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 1),
    _LinkIndex_Type()
)
linkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkIndex.setStatus("mandatory")
_LinkId_Type = Integer32
_LinkId_Object = MibTableColumn
linkId = _LinkId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 2),
    _LinkId_Type()
)
linkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkId.setStatus("mandatory")
_LinkHostname_Type = DisplayString
_LinkHostname_Object = MibTableColumn
linkHostname = _LinkHostname_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 3),
    _LinkHostname_Type()
)
linkHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkHostname.setStatus("mandatory")
_LinkCardDeviceName_Type = DisplayString
_LinkCardDeviceName_Object = MibTableColumn
linkCardDeviceName = _LinkCardDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 4),
    _LinkCardDeviceName_Type()
)
linkCardDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCardDeviceName.setStatus("mandatory")
_LinkState_Type = LinkState
_LinkState_Object = MibTableColumn
linkState = _LinkState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 5),
    _LinkState_Type()
)
linkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkState.setStatus("mandatory")
_LinkInhibitionState_Type = LinkInhibitionState
_LinkInhibitionState_Object = MibTableColumn
linkInhibitionState = _LinkInhibitionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 6),
    _LinkInhibitionState_Type()
)
linkInhibitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInhibitionState.setStatus("mandatory")
_LinkCongestionState_Type = LinkCongestionState
_LinkCongestionState_Object = MibTableColumn
linkCongestionState = _LinkCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 7),
    _LinkCongestionState_Type()
)
linkCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCongestionState.setStatus("mandatory")
_LinkAlignmentState_Type = LinkAlignmentState
_LinkAlignmentState_Object = MibTableColumn
linkAlignmentState = _LinkAlignmentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 8),
    _LinkAlignmentState_Type()
)
linkAlignmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAlignmentState.setStatus("mandatory")
_LinkNumMSUReceived_Type = Integer32
_LinkNumMSUReceived_Object = MibTableColumn
linkNumMSUReceived = _LinkNumMSUReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 9),
    _LinkNumMSUReceived_Type()
)
linkNumMSUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumMSUReceived.setStatus("mandatory")
_LinkNumMSUDiscarded_Type = Integer32
_LinkNumMSUDiscarded_Object = MibTableColumn
linkNumMSUDiscarded = _LinkNumMSUDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 10),
    _LinkNumMSUDiscarded_Type()
)
linkNumMSUDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumMSUDiscarded.setStatus("mandatory")
_LinkNumMSUTransmitted_Type = Integer32
_LinkNumMSUTransmitted_Object = MibTableColumn
linkNumMSUTransmitted = _LinkNumMSUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 11),
    _LinkNumMSUTransmitted_Type()
)
linkNumMSUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumMSUTransmitted.setStatus("mandatory")
_LinkNumSIFReceived_Type = Integer32
_LinkNumSIFReceived_Object = MibTableColumn
linkNumSIFReceived = _LinkNumSIFReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 12),
    _LinkNumSIFReceived_Type()
)
linkNumSIFReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumSIFReceived.setStatus("mandatory")
_LinkNumSIFTransmitted_Type = Integer32
_LinkNumSIFTransmitted_Object = MibTableColumn
linkNumSIFTransmitted = _LinkNumSIFTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 13),
    _LinkNumSIFTransmitted_Type()
)
linkNumSIFTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumSIFTransmitted.setStatus("mandatory")
_LinkNumAutoChangeovers_Type = Integer32
_LinkNumAutoChangeovers_Object = MibTableColumn
linkNumAutoChangeovers = _LinkNumAutoChangeovers_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 14),
    _LinkNumAutoChangeovers_Type()
)
linkNumAutoChangeovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumAutoChangeovers.setStatus("mandatory")
_LinkNumUnexpectedMsgs_Type = Integer32
_LinkNumUnexpectedMsgs_Object = MibTableColumn
linkNumUnexpectedMsgs = _LinkNumUnexpectedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 2, 1, 15),
    _LinkNumUnexpectedMsgs_Type()
)
linkNumUnexpectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumUnexpectedMsgs.setStatus("mandatory")
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("mandatory")
_RouteTableEntry_Object = MibTableRow
routeTableEntry = _RouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3, 1)
)
routeTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "routeIndex"),
)
if mibBuilder.loadTexts:
    routeTableEntry.setStatus("mandatory")
_RouteIndex_Type = Integer32
_RouteIndex_Object = MibTableColumn
routeIndex = _RouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3, 1, 1),
    _RouteIndex_Type()
)
routeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    routeIndex.setStatus("mandatory")
_RouteId_Type = DisplayString
_RouteId_Object = MibTableColumn
routeId = _RouteId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3, 1, 2),
    _RouteId_Type()
)
routeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeId.setStatus("mandatory")
_RouteDestPointCode_Type = DisplayString
_RouteDestPointCode_Object = MibTableColumn
routeDestPointCode = _RouteDestPointCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3, 1, 3),
    _RouteDestPointCode_Type()
)
routeDestPointCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeDestPointCode.setStatus("mandatory")
_RouteState_Type = RouteState
_RouteState_Object = MibTableColumn
routeState = _RouteState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3, 1, 4),
    _RouteState_Type()
)
routeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeState.setStatus("mandatory")
_RouteRank_Type = Integer32
_RouteRank_Object = MibTableColumn
routeRank = _RouteRank_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3, 1, 5),
    _RouteRank_Type()
)
routeRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeRank.setStatus("mandatory")
_RouteLinksetId_Type = DisplayString
_RouteLinksetId_Object = MibTableColumn
routeLinksetId = _RouteLinksetId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 3, 1, 6),
    _RouteLinksetId_Type()
)
routeLinksetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeLinksetId.setStatus("mandatory")
_DestinationTable_Object = MibTable
destinationTable = _DestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 4)
)
if mibBuilder.loadTexts:
    destinationTable.setStatus("mandatory")
_DestinationTableEntry_Object = MibTableRow
destinationTableEntry = _DestinationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 4, 1)
)
destinationTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "destIndex"),
)
if mibBuilder.loadTexts:
    destinationTableEntry.setStatus("mandatory")
_DestIndex_Type = Integer32
_DestIndex_Object = MibTableColumn
destIndex = _DestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 4, 1, 1),
    _DestIndex_Type()
)
destIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    destIndex.setStatus("mandatory")
_DestPointCode_Type = DisplayString
_DestPointCode_Object = MibTableColumn
destPointCode = _DestPointCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 4, 1, 2),
    _DestPointCode_Type()
)
destPointCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destPointCode.setStatus("mandatory")
_DestState_Type = DestinationState
_DestState_Object = MibTableColumn
destState = _DestState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 4, 1, 3),
    _DestState_Type()
)
destState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destState.setStatus("mandatory")
_DestRuleId_Type = Integer32
_DestRuleId_Object = MibTableColumn
destRuleId = _DestRuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 6, 4, 1, 4),
    _DestRuleId_Type()
)
destRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destRuleId.setStatus("mandatory")
_OmData_ObjectIdentity = ObjectIdentity
omData = _OmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7)
)
_LinkOMs_ObjectIdentity = ObjectIdentity
linkOMs = _LinkOMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1)
)
_LinkOMTable_Object = MibTable
linkOMTable = _LinkOMTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    linkOMTable.setStatus("mandatory")
_LinkOMTableEntry_Object = MibTableRow
linkOMTableEntry = _LinkOMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1)
)
linkOMTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "linksetIndex"),
    (0, "InternetThruway-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkOMTableEntry.setStatus("mandatory")
_LinkOMId_Type = Integer32
_LinkOMId_Object = MibTableColumn
linkOMId = _LinkOMId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 1),
    _LinkOMId_Type()
)
linkOMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOMId.setStatus("mandatory")
_LinkOMSetId_Type = Integer32
_LinkOMSetId_Object = MibTableColumn
linkOMSetId = _LinkOMSetId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 2),
    _LinkOMSetId_Type()
)
linkOMSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOMSetId.setStatus("mandatory")
_LinkFailures_Type = Counter32
_LinkFailures_Object = MibTableColumn
linkFailures = _LinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 3),
    _LinkFailures_Type()
)
linkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFailures.setStatus("mandatory")
_LinkCongestions_Type = Counter32
_LinkCongestions_Object = MibTableColumn
linkCongestions = _LinkCongestions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 4),
    _LinkCongestions_Type()
)
linkCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCongestions.setStatus("mandatory")
_LinkInhibits_Type = Counter32
_LinkInhibits_Object = MibTableColumn
linkInhibits = _LinkInhibits_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 5),
    _LinkInhibits_Type()
)
linkInhibits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInhibits.setStatus("mandatory")
_LinkTransmittedMSUs_Type = Counter32
_LinkTransmittedMSUs_Object = MibTableColumn
linkTransmittedMSUs = _LinkTransmittedMSUs_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 6),
    _LinkTransmittedMSUs_Type()
)
linkTransmittedMSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTransmittedMSUs.setStatus("mandatory")
_LinkReceivedMSUs_Type = Counter32
_LinkReceivedMSUs_Object = MibTableColumn
linkReceivedMSUs = _LinkReceivedMSUs_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 7),
    _LinkReceivedMSUs_Type()
)
linkReceivedMSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReceivedMSUs.setStatus("mandatory")
_LinkRemoteProcOutages_Type = Counter32
_LinkRemoteProcOutages_Object = MibTableColumn
linkRemoteProcOutages = _LinkRemoteProcOutages_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 1, 1, 1, 8),
    _LinkRemoteProcOutages_Type()
)
linkRemoteProcOutages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRemoteProcOutages.setStatus("mandatory")
_MaintenanceOMs_ObjectIdentity = ObjectIdentity
maintenanceOMs = _MaintenanceOMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 2)
)
_BLATimerExpiries_Type = Counter32
_BLATimerExpiries_Object = MibScalar
bLATimerExpiries = _BLATimerExpiries_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 2, 1),
    _BLATimerExpiries_Type()
)
bLATimerExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bLATimerExpiries.setStatus("mandatory")
_RLCTimerExpiries_Type = Counter32
_RLCTimerExpiries_Object = MibScalar
rLCTimerExpiries = _RLCTimerExpiries_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 2, 2),
    _RLCTimerExpiries_Type()
)
rLCTimerExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rLCTimerExpiries.setStatus("mandatory")
_UBATimerExpiries_Type = Counter32
_UBATimerExpiries_Object = MibScalar
uBATimerExpiries = _UBATimerExpiries_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 2, 3),
    _UBATimerExpiries_Type()
)
uBATimerExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uBATimerExpiries.setStatus("mandatory")
_RSATimerExpiries_Type = Counter32
_RSATimerExpiries_Object = MibScalar
rSATimerExpiries = _RSATimerExpiries_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 2, 4),
    _RSATimerExpiries_Type()
)
rSATimerExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSATimerExpiries.setStatus("mandatory")
_CallOMs_ObjectIdentity = ObjectIdentity
callOMs = _CallOMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3)
)
_OutCallAttempts_Type = Counter32
_OutCallAttempts_Object = MibScalar
outCallAttempts = _OutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 1),
    _OutCallAttempts_Type()
)
outCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outCallAttempts.setStatus("mandatory")
_OutCallNormalCompletions_Type = Counter32
_OutCallNormalCompletions_Object = MibScalar
outCallNormalCompletions = _OutCallNormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 2),
    _OutCallNormalCompletions_Type()
)
outCallNormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outCallNormalCompletions.setStatus("mandatory")
_OutCallAbnormalCompletions_Type = Counter32
_OutCallAbnormalCompletions_Object = MibScalar
outCallAbnormalCompletions = _OutCallAbnormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 3),
    _OutCallAbnormalCompletions_Type()
)
outCallAbnormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outCallAbnormalCompletions.setStatus("mandatory")
_UserBusyOutCallRejects_Type = Counter32
_UserBusyOutCallRejects_Object = MibScalar
userBusyOutCallRejects = _UserBusyOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 4),
    _UserBusyOutCallRejects_Type()
)
userBusyOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userBusyOutCallRejects.setStatus("mandatory")
_TempFailOutCallRejects_Type = Counter32
_TempFailOutCallRejects_Object = MibScalar
tempFailOutCallRejects = _TempFailOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 5),
    _TempFailOutCallRejects_Type()
)
tempFailOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFailOutCallRejects.setStatus("mandatory")
_UserUnavailableOutCallRejects_Type = Counter32
_UserUnavailableOutCallRejects_Object = MibScalar
userUnavailableOutCallRejects = _UserUnavailableOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 6),
    _UserUnavailableOutCallRejects_Type()
)
userUnavailableOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userUnavailableOutCallRejects.setStatus("mandatory")
_AbnormalReleaseOutCallRejects_Type = Counter32
_AbnormalReleaseOutCallRejects_Object = MibScalar
abnormalReleaseOutCallRejects = _AbnormalReleaseOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 7),
    _AbnormalReleaseOutCallRejects_Type()
)
abnormalReleaseOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abnormalReleaseOutCallRejects.setStatus("mandatory")
_OtherOutCallRejects_Type = Counter32
_OtherOutCallRejects_Object = MibScalar
otherOutCallRejects = _OtherOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 8),
    _OtherOutCallRejects_Type()
)
otherOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherOutCallRejects.setStatus("mandatory")
_CumulativeActiveOutCalls_Type = Counter32
_CumulativeActiveOutCalls_Object = MibScalar
cumulativeActiveOutCalls = _CumulativeActiveOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 9),
    _CumulativeActiveOutCalls_Type()
)
cumulativeActiveOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumulativeActiveOutCalls.setStatus("mandatory")
_CurrentlyActiveOutCalls_Type = Counter32
_CurrentlyActiveOutCalls_Object = MibScalar
currentlyActiveOutCalls = _CurrentlyActiveOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 10),
    _CurrentlyActiveOutCalls_Type()
)
currentlyActiveOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyActiveOutCalls.setStatus("mandatory")
_CurrentlyActiveDigitalOutCalls_Type = Counter32
_CurrentlyActiveDigitalOutCalls_Object = MibScalar
currentlyActiveDigitalOutCalls = _CurrentlyActiveDigitalOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 11),
    _CurrentlyActiveDigitalOutCalls_Type()
)
currentlyActiveDigitalOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyActiveDigitalOutCalls.setStatus("mandatory")
_CurrentlyActiveAnalogOutCalls_Type = Counter32
_CurrentlyActiveAnalogOutCalls_Object = MibScalar
currentlyActiveAnalogOutCalls = _CurrentlyActiveAnalogOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 12),
    _CurrentlyActiveAnalogOutCalls_Type()
)
currentlyActiveAnalogOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyActiveAnalogOutCalls.setStatus("mandatory")
_InCallAttempts_Type = Counter32
_InCallAttempts_Object = MibScalar
inCallAttempts = _InCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 13),
    _InCallAttempts_Type()
)
inCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inCallAttempts.setStatus("mandatory")
_InCallNormalCompletions_Type = Counter32
_InCallNormalCompletions_Object = MibScalar
inCallNormalCompletions = _InCallNormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 14),
    _InCallNormalCompletions_Type()
)
inCallNormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inCallNormalCompletions.setStatus("mandatory")
_InCallAbnormalCompletions_Type = Counter32
_InCallAbnormalCompletions_Object = MibScalar
inCallAbnormalCompletions = _InCallAbnormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 15),
    _InCallAbnormalCompletions_Type()
)
inCallAbnormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inCallAbnormalCompletions.setStatus("mandatory")
_UserBusyInCallRejects_Type = Counter32
_UserBusyInCallRejects_Object = MibScalar
userBusyInCallRejects = _UserBusyInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 16),
    _UserBusyInCallRejects_Type()
)
userBusyInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userBusyInCallRejects.setStatus("mandatory")
_TempFailInCallRejects_Type = Counter32
_TempFailInCallRejects_Object = MibScalar
tempFailInCallRejects = _TempFailInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 17),
    _TempFailInCallRejects_Type()
)
tempFailInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempFailInCallRejects.setStatus("mandatory")
_UserUnavailableInCallRejects_Type = Counter32
_UserUnavailableInCallRejects_Object = MibScalar
userUnavailableInCallRejects = _UserUnavailableInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 18),
    _UserUnavailableInCallRejects_Type()
)
userUnavailableInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userUnavailableInCallRejects.setStatus("mandatory")
_AbnormalReleaseInCallRejects_Type = Counter32
_AbnormalReleaseInCallRejects_Object = MibScalar
abnormalReleaseInCallRejects = _AbnormalReleaseInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 19),
    _AbnormalReleaseInCallRejects_Type()
)
abnormalReleaseInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abnormalReleaseInCallRejects.setStatus("mandatory")
_OtherInCallRejects_Type = Counter32
_OtherInCallRejects_Object = MibScalar
otherInCallRejects = _OtherInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 20),
    _OtherInCallRejects_Type()
)
otherInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherInCallRejects.setStatus("mandatory")
_CumulativeActiveInCalls_Type = Counter32
_CumulativeActiveInCalls_Object = MibScalar
cumulativeActiveInCalls = _CumulativeActiveInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 21),
    _CumulativeActiveInCalls_Type()
)
cumulativeActiveInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumulativeActiveInCalls.setStatus("mandatory")
_CurrentlyActiveInCalls_Type = Counter32
_CurrentlyActiveInCalls_Object = MibScalar
currentlyActiveInCalls = _CurrentlyActiveInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 22),
    _CurrentlyActiveInCalls_Type()
)
currentlyActiveInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyActiveInCalls.setStatus("mandatory")
_CurrentlyActiveDigitalInCalls_Type = Counter32
_CurrentlyActiveDigitalInCalls_Object = MibScalar
currentlyActiveDigitalInCalls = _CurrentlyActiveDigitalInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 23),
    _CurrentlyActiveDigitalInCalls_Type()
)
currentlyActiveDigitalInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyActiveDigitalInCalls.setStatus("mandatory")
_CurrentlyActiveAnalogInCalls_Type = Counter32
_CurrentlyActiveAnalogInCalls_Object = MibScalar
currentlyActiveAnalogInCalls = _CurrentlyActiveAnalogInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 3, 24),
    _CurrentlyActiveAnalogInCalls_Type()
)
currentlyActiveAnalogInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyActiveAnalogInCalls.setStatus("mandatory")
_TrunkGroupOMs_ObjectIdentity = ObjectIdentity
trunkGroupOMs = _TrunkGroupOMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4)
)
_TrunkCallOMTable_Object = MibTable
trunkCallOMTable = _TrunkCallOMTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    trunkCallOMTable.setStatus("mandatory")
_TrunkCallOMTableEntry_Object = MibTableRow
trunkCallOMTableEntry = _TrunkCallOMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1)
)
trunkCallOMTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "trunkCallOMIndex"),
)
if mibBuilder.loadTexts:
    trunkCallOMTableEntry.setStatus("mandatory")
_TrunkCallOMIndex_Type = Integer32
_TrunkCallOMIndex_Object = MibTableColumn
trunkCallOMIndex = _TrunkCallOMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 1),
    _TrunkCallOMIndex_Type()
)
trunkCallOMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkCallOMIndex.setStatus("mandatory")
_TrunkGroupCLLI_Type = DisplayString
_TrunkGroupCLLI_Object = MibTableColumn
trunkGroupCLLI = _TrunkGroupCLLI_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 2),
    _TrunkGroupCLLI_Type()
)
trunkGroupCLLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupCLLI.setStatus("mandatory")
_NumberOfCircuits_Type = Integer32
_NumberOfCircuits_Object = MibTableColumn
numberOfCircuits = _NumberOfCircuits_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 3),
    _NumberOfCircuits_Type()
)
numberOfCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfCircuits.setStatus("mandatory")
_TrunkOutCallAttempts_Type = Counter32
_TrunkOutCallAttempts_Object = MibTableColumn
trunkOutCallAttempts = _TrunkOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 4),
    _TrunkOutCallAttempts_Type()
)
trunkOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkOutCallAttempts.setStatus("mandatory")
_TrunkOutCallNormalCompletions_Type = Counter32
_TrunkOutCallNormalCompletions_Object = MibTableColumn
trunkOutCallNormalCompletions = _TrunkOutCallNormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 5),
    _TrunkOutCallNormalCompletions_Type()
)
trunkOutCallNormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkOutCallNormalCompletions.setStatus("mandatory")
_TrunkOutCallAbnormalCompletions_Type = Counter32
_TrunkOutCallAbnormalCompletions_Object = MibTableColumn
trunkOutCallAbnormalCompletions = _TrunkOutCallAbnormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 6),
    _TrunkOutCallAbnormalCompletions_Type()
)
trunkOutCallAbnormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkOutCallAbnormalCompletions.setStatus("mandatory")
_TrunkUserBusyOutCallRejects_Type = Counter32
_TrunkUserBusyOutCallRejects_Object = MibTableColumn
trunkUserBusyOutCallRejects = _TrunkUserBusyOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 7),
    _TrunkUserBusyOutCallRejects_Type()
)
trunkUserBusyOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkUserBusyOutCallRejects.setStatus("mandatory")
_TrunkTempFailOutCallRejects_Type = Counter32
_TrunkTempFailOutCallRejects_Object = MibTableColumn
trunkTempFailOutCallRejects = _TrunkTempFailOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 8),
    _TrunkTempFailOutCallRejects_Type()
)
trunkTempFailOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkTempFailOutCallRejects.setStatus("mandatory")
_TrunkUserUnavailableOutCallRejects_Type = Counter32
_TrunkUserUnavailableOutCallRejects_Object = MibTableColumn
trunkUserUnavailableOutCallRejects = _TrunkUserUnavailableOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 9),
    _TrunkUserUnavailableOutCallRejects_Type()
)
trunkUserUnavailableOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkUserUnavailableOutCallRejects.setStatus("mandatory")
_TrunkAbnormalReleaseOutCallRejects_Type = Counter32
_TrunkAbnormalReleaseOutCallRejects_Object = MibTableColumn
trunkAbnormalReleaseOutCallRejects = _TrunkAbnormalReleaseOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 10),
    _TrunkAbnormalReleaseOutCallRejects_Type()
)
trunkAbnormalReleaseOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkAbnormalReleaseOutCallRejects.setStatus("mandatory")
_TrunkOtherOutCallRejects_Type = Counter32
_TrunkOtherOutCallRejects_Object = MibTableColumn
trunkOtherOutCallRejects = _TrunkOtherOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 11),
    _TrunkOtherOutCallRejects_Type()
)
trunkOtherOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkOtherOutCallRejects.setStatus("mandatory")
_TrunkCumulativeActiveOutCalls_Type = Counter32
_TrunkCumulativeActiveOutCalls_Object = MibTableColumn
trunkCumulativeActiveOutCalls = _TrunkCumulativeActiveOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 12),
    _TrunkCumulativeActiveOutCalls_Type()
)
trunkCumulativeActiveOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCumulativeActiveOutCalls.setStatus("mandatory")
_TrunkCurrentlyActiveOutCalls_Type = Counter32
_TrunkCurrentlyActiveOutCalls_Object = MibTableColumn
trunkCurrentlyActiveOutCalls = _TrunkCurrentlyActiveOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 13),
    _TrunkCurrentlyActiveOutCalls_Type()
)
trunkCurrentlyActiveOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCurrentlyActiveOutCalls.setStatus("mandatory")
_TrunkCurrentlyActiveDigitalOutCalls_Type = Counter32
_TrunkCurrentlyActiveDigitalOutCalls_Object = MibTableColumn
trunkCurrentlyActiveDigitalOutCalls = _TrunkCurrentlyActiveDigitalOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 14),
    _TrunkCurrentlyActiveDigitalOutCalls_Type()
)
trunkCurrentlyActiveDigitalOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCurrentlyActiveDigitalOutCalls.setStatus("mandatory")
_TrunkCurrentlyActiveAnalogOutCalls_Type = Counter32
_TrunkCurrentlyActiveAnalogOutCalls_Object = MibTableColumn
trunkCurrentlyActiveAnalogOutCalls = _TrunkCurrentlyActiveAnalogOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 15),
    _TrunkCurrentlyActiveAnalogOutCalls_Type()
)
trunkCurrentlyActiveAnalogOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCurrentlyActiveAnalogOutCalls.setStatus("mandatory")
_TrunkInCallAttempts_Type = Counter32
_TrunkInCallAttempts_Object = MibTableColumn
trunkInCallAttempts = _TrunkInCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 16),
    _TrunkInCallAttempts_Type()
)
trunkInCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkInCallAttempts.setStatus("mandatory")
_TrunkInCallNormalCompletions_Type = Counter32
_TrunkInCallNormalCompletions_Object = MibTableColumn
trunkInCallNormalCompletions = _TrunkInCallNormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 17),
    _TrunkInCallNormalCompletions_Type()
)
trunkInCallNormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkInCallNormalCompletions.setStatus("mandatory")
_TrunkInCallAbnormalCompletions_Type = Counter32
_TrunkInCallAbnormalCompletions_Object = MibTableColumn
trunkInCallAbnormalCompletions = _TrunkInCallAbnormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 18),
    _TrunkInCallAbnormalCompletions_Type()
)
trunkInCallAbnormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkInCallAbnormalCompletions.setStatus("mandatory")
_TrunkUserBusyInCallRejects_Type = Counter32
_TrunkUserBusyInCallRejects_Object = MibTableColumn
trunkUserBusyInCallRejects = _TrunkUserBusyInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 19),
    _TrunkUserBusyInCallRejects_Type()
)
trunkUserBusyInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkUserBusyInCallRejects.setStatus("mandatory")
_TrunkTempFailInCallRejects_Type = Counter32
_TrunkTempFailInCallRejects_Object = MibTableColumn
trunkTempFailInCallRejects = _TrunkTempFailInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 20),
    _TrunkTempFailInCallRejects_Type()
)
trunkTempFailInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkTempFailInCallRejects.setStatus("mandatory")
_TrunkUserUnavailableInCallRejects_Type = Counter32
_TrunkUserUnavailableInCallRejects_Object = MibTableColumn
trunkUserUnavailableInCallRejects = _TrunkUserUnavailableInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 21),
    _TrunkUserUnavailableInCallRejects_Type()
)
trunkUserUnavailableInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkUserUnavailableInCallRejects.setStatus("mandatory")
_TrunkAbnormalReleaseInCallRejects_Type = Counter32
_TrunkAbnormalReleaseInCallRejects_Object = MibTableColumn
trunkAbnormalReleaseInCallRejects = _TrunkAbnormalReleaseInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 22),
    _TrunkAbnormalReleaseInCallRejects_Type()
)
trunkAbnormalReleaseInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkAbnormalReleaseInCallRejects.setStatus("mandatory")
_TrunkOtherInCallRejects_Type = Counter32
_TrunkOtherInCallRejects_Object = MibTableColumn
trunkOtherInCallRejects = _TrunkOtherInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 23),
    _TrunkOtherInCallRejects_Type()
)
trunkOtherInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkOtherInCallRejects.setStatus("mandatory")
_TrunkCumulativeActiveInCalls_Type = Counter32
_TrunkCumulativeActiveInCalls_Object = MibTableColumn
trunkCumulativeActiveInCalls = _TrunkCumulativeActiveInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 24),
    _TrunkCumulativeActiveInCalls_Type()
)
trunkCumulativeActiveInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCumulativeActiveInCalls.setStatus("mandatory")
_TrunkCurrentlyActiveInCalls_Type = Counter32
_TrunkCurrentlyActiveInCalls_Object = MibTableColumn
trunkCurrentlyActiveInCalls = _TrunkCurrentlyActiveInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 25),
    _TrunkCurrentlyActiveInCalls_Type()
)
trunkCurrentlyActiveInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCurrentlyActiveInCalls.setStatus("mandatory")
_TrunkCurrentlyActiveDigitalInCalls_Type = Counter32
_TrunkCurrentlyActiveDigitalInCalls_Object = MibTableColumn
trunkCurrentlyActiveDigitalInCalls = _TrunkCurrentlyActiveDigitalInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 26),
    _TrunkCurrentlyActiveDigitalInCalls_Type()
)
trunkCurrentlyActiveDigitalInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCurrentlyActiveDigitalInCalls.setStatus("mandatory")
_TrunkCurrentlyActiveAnalogInCalls_Type = Counter32
_TrunkCurrentlyActiveAnalogInCalls_Object = MibTableColumn
trunkCurrentlyActiveAnalogInCalls = _TrunkCurrentlyActiveAnalogInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 27),
    _TrunkCurrentlyActiveAnalogInCalls_Type()
)
trunkCurrentlyActiveAnalogInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCurrentlyActiveAnalogInCalls.setStatus("mandatory")
_TrunkAllActiveCalls_Type = Integer32
_TrunkAllActiveCalls_Object = MibTableColumn
trunkAllActiveCalls = _TrunkAllActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 28),
    _TrunkAllActiveCalls_Type()
)
trunkAllActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkAllActiveCalls.setStatus("mandatory")
_TrunkOccupancyPerCCS_Type = Integer32
_TrunkOccupancyPerCCS_Object = MibTableColumn
trunkOccupancyPerCCS = _TrunkOccupancyPerCCS_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 29),
    _TrunkOccupancyPerCCS_Type()
)
trunkOccupancyPerCCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkOccupancyPerCCS.setStatus("mandatory")
_TrafficInCCSs_Type = Counter32
_TrafficInCCSs_Object = MibTableColumn
trafficInCCSs = _TrafficInCCSs_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 30),
    _TrafficInCCSs_Type()
)
trafficInCCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficInCCSs.setStatus("mandatory")
_TrafficInCCSIncomings_Type = Counter32
_TrafficInCCSIncomings_Object = MibTableColumn
trafficInCCSIncomings = _TrafficInCCSIncomings_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 31),
    _TrafficInCCSIncomings_Type()
)
trafficInCCSIncomings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficInCCSIncomings.setStatus("mandatory")
_LocalBusyInCCSs_Type = Counter32
_LocalBusyInCCSs_Object = MibTableColumn
localBusyInCCSs = _LocalBusyInCCSs_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 32),
    _LocalBusyInCCSs_Type()
)
localBusyInCCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localBusyInCCSs.setStatus("mandatory")
_RemoteBusyInCCSs_Type = Counter32
_RemoteBusyInCCSs_Object = MibTableColumn
remoteBusyInCCSs = _RemoteBusyInCCSs_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 4, 1, 1, 33),
    _RemoteBusyInCCSs_Type()
)
remoteBusyInCCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteBusyInCCSs.setStatus("mandatory")
_PhoneNumberOMs_ObjectIdentity = ObjectIdentity
phoneNumberOMs = _PhoneNumberOMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5)
)
_PhoneCallOMTable_Object = MibTable
phoneCallOMTable = _PhoneCallOMTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1)
)
if mibBuilder.loadTexts:
    phoneCallOMTable.setStatus("mandatory")
_PhoneCallOMTableEntry_Object = MibTableRow
phoneCallOMTableEntry = _PhoneCallOMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1)
)
phoneCallOMTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "phoneCallOMIndex"),
)
if mibBuilder.loadTexts:
    phoneCallOMTableEntry.setStatus("mandatory")
_PhoneCallOMIndex_Type = Integer32
_PhoneCallOMIndex_Object = MibTableColumn
phoneCallOMIndex = _PhoneCallOMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 1),
    _PhoneCallOMIndex_Type()
)
phoneCallOMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phoneCallOMIndex.setStatus("mandatory")
_PhoneNumber_Type = DisplayString
_PhoneNumber_Object = MibTableColumn
phoneNumber = _PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 2),
    _PhoneNumber_Type()
)
phoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneNumber.setStatus("mandatory")
_PhoneDialCallAttempts_Type = Counter32
_PhoneDialCallAttempts_Object = MibTableColumn
phoneDialCallAttempts = _PhoneDialCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 3),
    _PhoneDialCallAttempts_Type()
)
phoneDialCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneDialCallAttempts.setStatus("mandatory")
_PhoneDialCallNormalCompletions_Type = Counter32
_PhoneDialCallNormalCompletions_Object = MibTableColumn
phoneDialCallNormalCompletions = _PhoneDialCallNormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 4),
    _PhoneDialCallNormalCompletions_Type()
)
phoneDialCallNormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneDialCallNormalCompletions.setStatus("mandatory")
_PhoneDialCallAbnormalCompletions_Type = Counter32
_PhoneDialCallAbnormalCompletions_Object = MibTableColumn
phoneDialCallAbnormalCompletions = _PhoneDialCallAbnormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 5),
    _PhoneDialCallAbnormalCompletions_Type()
)
phoneDialCallAbnormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneDialCallAbnormalCompletions.setStatus("mandatory")
_PhoneUserBusyDialCallRejects_Type = Counter32
_PhoneUserBusyDialCallRejects_Object = MibTableColumn
phoneUserBusyDialCallRejects = _PhoneUserBusyDialCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 6),
    _PhoneUserBusyDialCallRejects_Type()
)
phoneUserBusyDialCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneUserBusyDialCallRejects.setStatus("mandatory")
_PhoneTempFailDialCallRejects_Type = Counter32
_PhoneTempFailDialCallRejects_Object = MibTableColumn
phoneTempFailDialCallRejects = _PhoneTempFailDialCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 7),
    _PhoneTempFailDialCallRejects_Type()
)
phoneTempFailDialCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneTempFailDialCallRejects.setStatus("mandatory")
_PhoneUserUnavailableDialCallRejects_Type = Counter32
_PhoneUserUnavailableDialCallRejects_Object = MibTableColumn
phoneUserUnavailableDialCallRejects = _PhoneUserUnavailableDialCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 8),
    _PhoneUserUnavailableDialCallRejects_Type()
)
phoneUserUnavailableDialCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneUserUnavailableDialCallRejects.setStatus("mandatory")
_PhoneAbnormalReleaseDialCallRejects_Type = Counter32
_PhoneAbnormalReleaseDialCallRejects_Object = MibTableColumn
phoneAbnormalReleaseDialCallRejects = _PhoneAbnormalReleaseDialCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 9),
    _PhoneAbnormalReleaseDialCallRejects_Type()
)
phoneAbnormalReleaseDialCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneAbnormalReleaseDialCallRejects.setStatus("mandatory")
_PhoneOtherDialCallRejects_Type = Counter32
_PhoneOtherDialCallRejects_Object = MibTableColumn
phoneOtherDialCallRejects = _PhoneOtherDialCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 10),
    _PhoneOtherDialCallRejects_Type()
)
phoneOtherDialCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneOtherDialCallRejects.setStatus("mandatory")
_PhoneCumulativeActiveDialCalls_Type = Counter32
_PhoneCumulativeActiveDialCalls_Object = MibTableColumn
phoneCumulativeActiveDialCalls = _PhoneCumulativeActiveDialCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 11),
    _PhoneCumulativeActiveDialCalls_Type()
)
phoneCumulativeActiveDialCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneCumulativeActiveDialCalls.setStatus("mandatory")
_PhoneCurrentlyActiveDialCalls_Type = Counter32
_PhoneCurrentlyActiveDialCalls_Object = MibTableColumn
phoneCurrentlyActiveDialCalls = _PhoneCurrentlyActiveDialCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 12),
    _PhoneCurrentlyActiveDialCalls_Type()
)
phoneCurrentlyActiveDialCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneCurrentlyActiveDialCalls.setStatus("mandatory")
_PhoneCurrentlyActiveDigitalDialCalls_Type = Counter32
_PhoneCurrentlyActiveDigitalDialCalls_Object = MibTableColumn
phoneCurrentlyActiveDigitalDialCalls = _PhoneCurrentlyActiveDigitalDialCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 13),
    _PhoneCurrentlyActiveDigitalDialCalls_Type()
)
phoneCurrentlyActiveDigitalDialCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneCurrentlyActiveDigitalDialCalls.setStatus("mandatory")
_PhoneCurrentlyActiveAnalogDialCalls_Type = Counter32
_PhoneCurrentlyActiveAnalogDialCalls_Object = MibTableColumn
phoneCurrentlyActiveAnalogDialCalls = _PhoneCurrentlyActiveAnalogDialCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 5, 1, 1, 14),
    _PhoneCurrentlyActiveAnalogDialCalls_Type()
)
phoneCurrentlyActiveAnalogDialCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneCurrentlyActiveAnalogDialCalls.setStatus("mandatory")
_SystemOMs_ObjectIdentity = ObjectIdentity
systemOMs = _SystemOMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6)
)
_CsgComplexCLLI_Type = DisplayString
_CsgComplexCLLI_Object = MibScalar
csgComplexCLLI = _CsgComplexCLLI_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 1),
    _CsgComplexCLLI_Type()
)
csgComplexCLLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csgComplexCLLI.setStatus("mandatory")
_ServerHostName_Type = DisplayString
_ServerHostName_Object = MibScalar
serverHostName = _ServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 2),
    _ServerHostName_Type()
)
serverHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverHostName.setStatus("mandatory")
_ServerIpAddress_Type = IpAddress
_ServerIpAddress_Object = MibScalar
serverIpAddress = _ServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 3),
    _ServerIpAddress_Type()
)
serverIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIpAddress.setStatus("mandatory")
_ServerCLLI_Type = DisplayString
_ServerCLLI_Object = MibScalar
serverCLLI = _ServerCLLI_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 4),
    _ServerCLLI_Type()
)
serverCLLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCLLI.setStatus("mandatory")
_MateServerHostName_Type = DisplayString
_MateServerHostName_Object = MibScalar
mateServerHostName = _MateServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 5),
    _MateServerHostName_Type()
)
mateServerHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mateServerHostName.setStatus("mandatory")
_MateServerIpAddress_Type = IpAddress
_MateServerIpAddress_Object = MibScalar
mateServerIpAddress = _MateServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 6),
    _MateServerIpAddress_Type()
)
mateServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mateServerIpAddress.setStatus("mandatory")
_ServerMemSize_Type = Integer32
_ServerMemSize_Object = MibScalar
serverMemSize = _ServerMemSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 8),
    _ServerMemSize_Type()
)
serverMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverMemSize.setStatus("mandatory")
_ProvisionedDPCs_Type = Integer32
_ProvisionedDPCs_Object = MibScalar
provisionedDPCs = _ProvisionedDPCs_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 9),
    _ProvisionedDPCs_Type()
)
provisionedDPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provisionedDPCs.setStatus("mandatory")
_ProvisionedCircuits_Type = Integer32
_ProvisionedCircuits_Object = MibScalar
provisionedCircuits = _ProvisionedCircuits_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 10),
    _ProvisionedCircuits_Type()
)
provisionedCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provisionedCircuits.setStatus("mandatory")
_InserviceCircuits_Type = Integer32
_InserviceCircuits_Object = MibScalar
inserviceCircuits = _InserviceCircuits_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 11),
    _InserviceCircuits_Type()
)
inserviceCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inserviceCircuits.setStatus("mandatory")
_ProvisionedNASes_Type = Integer32
_ProvisionedNASes_Object = MibScalar
provisionedNASes = _ProvisionedNASes_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 12),
    _ProvisionedNASes_Type()
)
provisionedNASes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provisionedNASes.setStatus("mandatory")
_AliveNASes_Type = Integer32
_AliveNASes_Object = MibScalar
aliveNASes = _AliveNASes_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 13),
    _AliveNASes_Type()
)
aliveNASes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aliveNASes.setStatus("mandatory")
_InserviceNASes_Type = Integer32
_InserviceNASes_Object = MibScalar
inserviceNASes = _InserviceNASes_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 14),
    _InserviceNASes_Type()
)
inserviceNASes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inserviceNASes.setStatus("mandatory")
_ProvsionedCards_Type = Integer32
_ProvsionedCards_Object = MibScalar
provsionedCards = _ProvsionedCards_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 15),
    _ProvsionedCards_Type()
)
provsionedCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provsionedCards.setStatus("mandatory")
_InserviceCards_Type = Integer32
_InserviceCards_Object = MibScalar
inserviceCards = _InserviceCards_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 16),
    _InserviceCards_Type()
)
inserviceCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inserviceCards.setStatus("mandatory")
_ProvisionedPorts_Type = Integer32
_ProvisionedPorts_Object = MibScalar
provisionedPorts = _ProvisionedPorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 17),
    _ProvisionedPorts_Type()
)
provisionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provisionedPorts.setStatus("mandatory")
_InservicePorts_Type = Integer32
_InservicePorts_Object = MibScalar
inservicePorts = _InservicePorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 18),
    _InservicePorts_Type()
)
inservicePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inservicePorts.setStatus("mandatory")
_UserCPUUsage_Type = Integer32
_UserCPUUsage_Object = MibScalar
userCPUUsage = _UserCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 19),
    _UserCPUUsage_Type()
)
userCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userCPUUsage.setStatus("mandatory")
_SystemCPUUsage_Type = Integer32
_SystemCPUUsage_Object = MibScalar
systemCPUUsage = _SystemCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 20),
    _SystemCPUUsage_Type()
)
systemCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPUUsage.setStatus("mandatory")
_TotalCPUUsage_Type = Integer32
_TotalCPUUsage_Object = MibScalar
totalCPUUsage = _TotalCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 21),
    _TotalCPUUsage_Type()
)
totalCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCPUUsage.setStatus("mandatory")
_MaxCPUUsage_Type = Integer32
_MaxCPUUsage_Object = MibScalar
maxCPUUsage = _MaxCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 22),
    _MaxCPUUsage_Type()
)
maxCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCPUUsage.setStatus("mandatory")
_AvgLoad_Type = Integer32
_AvgLoad_Object = MibScalar
avgLoad = _AvgLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 23),
    _AvgLoad_Type()
)
avgLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgLoad.setStatus("mandatory")
_SystemCallRate_Type = Integer32
_SystemCallRate_Object = MibScalar
systemCallRate = _SystemCallRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 24),
    _SystemCallRate_Type()
)
systemCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCallRate.setStatus("mandatory")
_ContextSwitchRate_Type = Integer32
_ContextSwitchRate_Object = MibScalar
contextSwitchRate = _ContextSwitchRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 25),
    _ContextSwitchRate_Type()
)
contextSwitchRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contextSwitchRate.setStatus("mandatory")
_LastUpdateOMFile_Type = DisplayString
_LastUpdateOMFile_Object = MibScalar
lastUpdateOMFile = _LastUpdateOMFile_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 6, 26),
    _LastUpdateOMFile_Type()
)
lastUpdateOMFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastUpdateOMFile.setStatus("mandatory")
_NasOMs_ObjectIdentity = ObjectIdentity
nasOMs = _NasOMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7)
)
_NasCallOMTable_Object = MibTable
nasCallOMTable = _NasCallOMTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1)
)
if mibBuilder.loadTexts:
    nasCallOMTable.setStatus("mandatory")
_NasCallOMTableEntry_Object = MibTableRow
nasCallOMTableEntry = _NasCallOMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1)
)
nasCallOMTableEntry.setIndexNames(
    (0, "InternetThruway-MIB", "nasCallOMIndex"),
)
if mibBuilder.loadTexts:
    nasCallOMTableEntry.setStatus("mandatory")
_NasCallOMIndex_Type = Integer32
_NasCallOMIndex_Object = MibTableColumn
nasCallOMIndex = _NasCallOMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 1),
    _NasCallOMIndex_Type()
)
nasCallOMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasCallOMIndex.setStatus("mandatory")
_NasName1_Type = DisplayString
_NasName1_Object = MibTableColumn
nasName1 = _NasName1_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 2),
    _NasName1_Type()
)
nasName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasName1.setStatus("mandatory")
_NumberOfPorts_Type = Integer32
_NumberOfPorts_Object = MibTableColumn
numberOfPorts = _NumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 3),
    _NumberOfPorts_Type()
)
numberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPorts.setStatus("mandatory")
_NasOutCallAttempts_Type = Counter32
_NasOutCallAttempts_Object = MibTableColumn
nasOutCallAttempts = _NasOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 4),
    _NasOutCallAttempts_Type()
)
nasOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOutCallAttempts.setStatus("mandatory")
_NasOutCallNormalCompletions_Type = Counter32
_NasOutCallNormalCompletions_Object = MibTableColumn
nasOutCallNormalCompletions = _NasOutCallNormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 5),
    _NasOutCallNormalCompletions_Type()
)
nasOutCallNormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOutCallNormalCompletions.setStatus("mandatory")
_NasOutCallAbnormalCompletions_Type = Counter32
_NasOutCallAbnormalCompletions_Object = MibTableColumn
nasOutCallAbnormalCompletions = _NasOutCallAbnormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 6),
    _NasOutCallAbnormalCompletions_Type()
)
nasOutCallAbnormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOutCallAbnormalCompletions.setStatus("mandatory")
_NasUserBusyOutCallRejects_Type = Counter32
_NasUserBusyOutCallRejects_Object = MibTableColumn
nasUserBusyOutCallRejects = _NasUserBusyOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 7),
    _NasUserBusyOutCallRejects_Type()
)
nasUserBusyOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasUserBusyOutCallRejects.setStatus("mandatory")
_NasTempFailOutCallRejects_Type = Counter32
_NasTempFailOutCallRejects_Object = MibTableColumn
nasTempFailOutCallRejects = _NasTempFailOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 8),
    _NasTempFailOutCallRejects_Type()
)
nasTempFailOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasTempFailOutCallRejects.setStatus("mandatory")
_NasUserUnavailableOutCallRejects_Type = Counter32
_NasUserUnavailableOutCallRejects_Object = MibTableColumn
nasUserUnavailableOutCallRejects = _NasUserUnavailableOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 9),
    _NasUserUnavailableOutCallRejects_Type()
)
nasUserUnavailableOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasUserUnavailableOutCallRejects.setStatus("mandatory")
_NasAbnormalReleaseOutCallRejects_Type = Counter32
_NasAbnormalReleaseOutCallRejects_Object = MibTableColumn
nasAbnormalReleaseOutCallRejects = _NasAbnormalReleaseOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 10),
    _NasAbnormalReleaseOutCallRejects_Type()
)
nasAbnormalReleaseOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasAbnormalReleaseOutCallRejects.setStatus("mandatory")
_NasOtherOutCallRejects_Type = Counter32
_NasOtherOutCallRejects_Object = MibTableColumn
nasOtherOutCallRejects = _NasOtherOutCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 11),
    _NasOtherOutCallRejects_Type()
)
nasOtherOutCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOtherOutCallRejects.setStatus("mandatory")
_NasCumulativeActiveOutCalls_Type = Counter32
_NasCumulativeActiveOutCalls_Object = MibTableColumn
nasCumulativeActiveOutCalls = _NasCumulativeActiveOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 12),
    _NasCumulativeActiveOutCalls_Type()
)
nasCumulativeActiveOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCumulativeActiveOutCalls.setStatus("mandatory")
_NasCurrentlyActiveOutCalls_Type = Counter32
_NasCurrentlyActiveOutCalls_Object = MibTableColumn
nasCurrentlyActiveOutCalls = _NasCurrentlyActiveOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 13),
    _NasCurrentlyActiveOutCalls_Type()
)
nasCurrentlyActiveOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCurrentlyActiveOutCalls.setStatus("mandatory")
_NasCurrentlyActiveDigitalOutCalls_Type = Counter32
_NasCurrentlyActiveDigitalOutCalls_Object = MibTableColumn
nasCurrentlyActiveDigitalOutCalls = _NasCurrentlyActiveDigitalOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 14),
    _NasCurrentlyActiveDigitalOutCalls_Type()
)
nasCurrentlyActiveDigitalOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCurrentlyActiveDigitalOutCalls.setStatus("mandatory")
_NasCurrentlyActiveAnalogOutCalls_Type = Counter32
_NasCurrentlyActiveAnalogOutCalls_Object = MibTableColumn
nasCurrentlyActiveAnalogOutCalls = _NasCurrentlyActiveAnalogOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 15),
    _NasCurrentlyActiveAnalogOutCalls_Type()
)
nasCurrentlyActiveAnalogOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCurrentlyActiveAnalogOutCalls.setStatus("mandatory")
_NasInCallAttempts_Type = Counter32
_NasInCallAttempts_Object = MibTableColumn
nasInCallAttempts = _NasInCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 16),
    _NasInCallAttempts_Type()
)
nasInCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInCallAttempts.setStatus("mandatory")
_NasInCallNormalCompletions_Type = Counter32
_NasInCallNormalCompletions_Object = MibTableColumn
nasInCallNormalCompletions = _NasInCallNormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 17),
    _NasInCallNormalCompletions_Type()
)
nasInCallNormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInCallNormalCompletions.setStatus("mandatory")
_NasInCallAbnormalCompletions_Type = Counter32
_NasInCallAbnormalCompletions_Object = MibTableColumn
nasInCallAbnormalCompletions = _NasInCallAbnormalCompletions_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 18),
    _NasInCallAbnormalCompletions_Type()
)
nasInCallAbnormalCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInCallAbnormalCompletions.setStatus("mandatory")
_NasUserBusyInCallRejects_Type = Counter32
_NasUserBusyInCallRejects_Object = MibTableColumn
nasUserBusyInCallRejects = _NasUserBusyInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 19),
    _NasUserBusyInCallRejects_Type()
)
nasUserBusyInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasUserBusyInCallRejects.setStatus("mandatory")
_NasTempFailInCallRejects_Type = Counter32
_NasTempFailInCallRejects_Object = MibTableColumn
nasTempFailInCallRejects = _NasTempFailInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 20),
    _NasTempFailInCallRejects_Type()
)
nasTempFailInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasTempFailInCallRejects.setStatus("mandatory")
_NasUserUnavailableInCallRejects_Type = Counter32
_NasUserUnavailableInCallRejects_Object = MibTableColumn
nasUserUnavailableInCallRejects = _NasUserUnavailableInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 21),
    _NasUserUnavailableInCallRejects_Type()
)
nasUserUnavailableInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasUserUnavailableInCallRejects.setStatus("mandatory")
_NasAbnormalReleaseInCallRejects_Type = Counter32
_NasAbnormalReleaseInCallRejects_Object = MibTableColumn
nasAbnormalReleaseInCallRejects = _NasAbnormalReleaseInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 22),
    _NasAbnormalReleaseInCallRejects_Type()
)
nasAbnormalReleaseInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasAbnormalReleaseInCallRejects.setStatus("mandatory")
_NasOtherInCallRejects_Type = Counter32
_NasOtherInCallRejects_Object = MibTableColumn
nasOtherInCallRejects = _NasOtherInCallRejects_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 23),
    _NasOtherInCallRejects_Type()
)
nasOtherInCallRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOtherInCallRejects.setStatus("mandatory")
_NasCumulativeActiveInCalls_Type = Counter32
_NasCumulativeActiveInCalls_Object = MibTableColumn
nasCumulativeActiveInCalls = _NasCumulativeActiveInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 24),
    _NasCumulativeActiveInCalls_Type()
)
nasCumulativeActiveInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCumulativeActiveInCalls.setStatus("mandatory")
_NasCurrentlyActiveInCalls_Type = Counter32
_NasCurrentlyActiveInCalls_Object = MibTableColumn
nasCurrentlyActiveInCalls = _NasCurrentlyActiveInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 25),
    _NasCurrentlyActiveInCalls_Type()
)
nasCurrentlyActiveInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCurrentlyActiveInCalls.setStatus("mandatory")
_NasCurrentlyActiveDigitalInCalls_Type = Counter32
_NasCurrentlyActiveDigitalInCalls_Object = MibTableColumn
nasCurrentlyActiveDigitalInCalls = _NasCurrentlyActiveDigitalInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 26),
    _NasCurrentlyActiveDigitalInCalls_Type()
)
nasCurrentlyActiveDigitalInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCurrentlyActiveDigitalInCalls.setStatus("mandatory")
_NasCurrentlyActiveAnalogInCalls_Type = Counter32
_NasCurrentlyActiveAnalogInCalls_Object = MibTableColumn
nasCurrentlyActiveAnalogInCalls = _NasCurrentlyActiveAnalogInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 27),
    _NasCurrentlyActiveAnalogInCalls_Type()
)
nasCurrentlyActiveAnalogInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCurrentlyActiveAnalogInCalls.setStatus("mandatory")
_NasAllActiveCalls_Type = Integer32
_NasAllActiveCalls_Object = MibTableColumn
nasAllActiveCalls = _NasAllActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 28),
    _NasAllActiveCalls_Type()
)
nasAllActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasAllActiveCalls.setStatus("mandatory")
_NasMaxPortsUsed_Type = Integer32
_NasMaxPortsUsed_Object = MibTableColumn
nasMaxPortsUsed = _NasMaxPortsUsed_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 29),
    _NasMaxPortsUsed_Type()
)
nasMaxPortsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasMaxPortsUsed.setStatus("mandatory")
_NasMinPortsUsed_Type = Integer32
_NasMinPortsUsed_Object = MibTableColumn
nasMinPortsUsed = _NasMinPortsUsed_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 30),
    _NasMinPortsUsed_Type()
)
nasMinPortsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasMinPortsUsed.setStatus("mandatory")
_NasCurrentlyInUsePorts_Type = Integer32
_NasCurrentlyInUsePorts_Object = MibTableColumn
nasCurrentlyInUsePorts = _NasCurrentlyInUsePorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 7, 7, 1, 1, 31),
    _NasCurrentlyInUsePorts_Type()
)
nasCurrentlyInUsePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasCurrentlyInUsePorts.setStatus("mandatory")

# Managed Objects groups


# Notification objects

diskSpaceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 1001)
)
diskSpaceClear.setObjects(
      *(("InternetThruway-MIB", "partitionSpaceKey"),
        ("InternetThruway-MIB", "partitionIndex"),
        ("InternetThruway-MIB", "partitionName"),
        ("InternetThruway-MIB", "partitionPercentFull"),
        ("InternetThruway-MIB", "partitionSpaceTimeStamp"))
)
if mibBuilder.loadTexts:
    diskSpaceClear.setStatus(
        ""
    )

diskSpaceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 1004)
)
diskSpaceAlarm.setObjects(
      *(("InternetThruway-MIB", "partitionSpaceKey"),
        ("InternetThruway-MIB", "partitionIndex"),
        ("InternetThruway-MIB", "partitionName"),
        ("InternetThruway-MIB", "partitionPercentFull"),
        ("InternetThruway-MIB", "partitionSpaceTimeStamp"))
)
if mibBuilder.loadTexts:
    diskSpaceAlarm.setStatus(
        ""
    )

etherCardTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 1011)
)
if mibBuilder.loadTexts:
    etherCardTrapClear.setStatus(
        ""
    )

etherCardTrapMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 1014)
)
if mibBuilder.loadTexts:
    etherCardTrapMajor.setStatus(
        ""
    )

etherCardTrapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 1015)
)
if mibBuilder.loadTexts:
    etherCardTrapCritical.setStatus(
        ""
    )

compDebugOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 2001)
)
compDebugOff.setObjects(
      *(("InternetThruway-MIB", "compDebugKey"),
        ("InternetThruway-MIB", "componentIndex"),
        ("InternetThruway-MIB", "componentName"),
        ("InternetThruway-MIB", "compDebugTimeStamp"))
)
if mibBuilder.loadTexts:
    compDebugOff.setStatus(
        ""
    )

compDebugOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 2002)
)
compDebugOn.setObjects(
      *(("InternetThruway-MIB", "compDebugKey"),
        ("InternetThruway-MIB", "componentIndex"),
        ("InternetThruway-MIB", "componentName"),
        ("InternetThruway-MIB", "compDebugTimeStamp"))
)
if mibBuilder.loadTexts:
    compDebugOn.setStatus(
        ""
    )

compStateClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 2011)
)
compStateClear.setObjects(
      *(("InternetThruway-MIB", "compProvStateKey"),
        ("InternetThruway-MIB", "componentIndex"),
        ("InternetThruway-MIB", "componentName"),
        ("InternetThruway-MIB", "compProvStateStatus"),
        ("InternetThruway-MIB", "compSecsInCurrentState"),
        ("InternetThruway-MIB", "compProvStateTimeStamp"))
)
if mibBuilder.loadTexts:
    compStateClear.setStatus(
        ""
    )

compStateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 2014)
)
compStateAlarm.setObjects(
      *(("InternetThruway-MIB", "compProvStateKey"),
        ("InternetThruway-MIB", "componentIndex"),
        ("InternetThruway-MIB", "componentName"),
        ("InternetThruway-MIB", "compProvStateStatus"),
        ("InternetThruway-MIB", "compSecsInCurrentState"),
        ("InternetThruway-MIB", "compProvStateTimeStamp"))
)
if mibBuilder.loadTexts:
    compStateAlarm.setStatus(
        ""
    )

restartStateClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 2021)
)
restartStateClear.setObjects(
      *(("InternetThruway-MIB", "compRestartKey"),
        ("InternetThruway-MIB", "componentIndex"),
        ("InternetThruway-MIB", "componentName"),
        ("InternetThruway-MIB", "compRestartStatus"),
        ("InternetThruway-MIB", "compRestartTimeStamp"))
)
if mibBuilder.loadTexts:
    restartStateClear.setStatus(
        ""
    )

restartStateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 2024)
)
restartStateAlarm.setObjects(
      *(("InternetThruway-MIB", "compRestartKey"),
        ("InternetThruway-MIB", "componentIndex"),
        ("InternetThruway-MIB", "componentName"),
        ("InternetThruway-MIB", "compRestartStatus"),
        ("InternetThruway-MIB", "compRestartTimeStamp"))
)
if mibBuilder.loadTexts:
    restartStateAlarm.setStatus(
        ""
    )

ss7LinkFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3001)
)
ss7LinkFailureClear.setObjects(
      *(("InternetThruway-MIB", "lfIndex"),
        ("InternetThruway-MIB", "lfKey"),
        ("InternetThruway-MIB", "lfIPAddress"),
        ("InternetThruway-MIB", "lfLinkCode"),
        ("InternetThruway-MIB", "lfName"),
        ("InternetThruway-MIB", "lfCardId"),
        ("InternetThruway-MIB", "lfLinkSet"),
        ("InternetThruway-MIB", "lfTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinkFailureClear.setStatus(
        ""
    )

ss7LinkFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3004)
)
ss7LinkFailureAlarm.setObjects(
      *(("InternetThruway-MIB", "lfIndex"),
        ("InternetThruway-MIB", "lfKey"),
        ("InternetThruway-MIB", "lfIPAddress"),
        ("InternetThruway-MIB", "lfLinkCode"),
        ("InternetThruway-MIB", "lfName"),
        ("InternetThruway-MIB", "lfCardId"),
        ("InternetThruway-MIB", "lfLinkSet"),
        ("InternetThruway-MIB", "lfTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinkFailureAlarm.setStatus(
        ""
    )

ss7LinkCongestionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3011)
)
ss7LinkCongestionClear.setObjects(
      *(("InternetThruway-MIB", "lcIndex"),
        ("InternetThruway-MIB", "lcKey"),
        ("InternetThruway-MIB", "lcIPAddress"),
        ("InternetThruway-MIB", "lcLinkCode"),
        ("InternetThruway-MIB", "lcName"),
        ("InternetThruway-MIB", "lcCardId"),
        ("InternetThruway-MIB", "lcLinkSet"),
        ("InternetThruway-MIB", "lcTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinkCongestionClear.setStatus(
        ""
    )

ss7LinkCongestionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3012)
)
ss7LinkCongestionAlarm.setObjects(
      *(("InternetThruway-MIB", "lcIndex"),
        ("InternetThruway-MIB", "lcKey"),
        ("InternetThruway-MIB", "lcIPAddress"),
        ("InternetThruway-MIB", "lcLinkCode"),
        ("InternetThruway-MIB", "lcName"),
        ("InternetThruway-MIB", "lcCardId"),
        ("InternetThruway-MIB", "lcLinkSet"),
        ("InternetThruway-MIB", "lcTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinkCongestionAlarm.setStatus(
        ""
    )

ss7ISUPFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3021)
)
ss7ISUPFailureClear.setObjects(
      *(("InternetThruway-MIB", "ifIndex"),
        ("InternetThruway-MIB", "ifKey"),
        ("InternetThruway-MIB", "ifIPAddress"),
        ("InternetThruway-MIB", "ifName"),
        ("InternetThruway-MIB", "ifTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7ISUPFailureClear.setStatus(
        ""
    )

ss7ISUPFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3025)
)
ss7ISUPFailureAlarm.setObjects(
      *(("InternetThruway-MIB", "ifIndex"),
        ("InternetThruway-MIB", "ifKey"),
        ("InternetThruway-MIB", "ifIPAddress"),
        ("InternetThruway-MIB", "ifName"),
        ("InternetThruway-MIB", "ifTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7ISUPFailureAlarm.setStatus(
        ""
    )

ss7ISUPCongestionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3031)
)
ss7ISUPCongestionClear.setObjects(
      *(("InternetThruway-MIB", "icIndex"),
        ("InternetThruway-MIB", "icKey"),
        ("InternetThruway-MIB", "icIPAddress"),
        ("InternetThruway-MIB", "icCongestionLevel"),
        ("InternetThruway-MIB", "icName"),
        ("InternetThruway-MIB", "icTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7ISUPCongestionClear.setStatus(
        ""
    )

ss7ISUPCongestionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3033)
)
ss7ISUPCongestionAlarm.setObjects(
      *(("InternetThruway-MIB", "icIndex"),
        ("InternetThruway-MIB", "icKey"),
        ("InternetThruway-MIB", "icIPAddress"),
        ("InternetThruway-MIB", "icCongestionLevel"),
        ("InternetThruway-MIB", "icName"),
        ("InternetThruway-MIB", "icTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7ISUPCongestionAlarm.setStatus(
        ""
    )

ss7FEPCongestionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3042)
)
ss7FEPCongestionWarning.setObjects(
      *(("InternetThruway-MIB", "trapIdKey"),
        ("InternetThruway-MIB", "trapIPAddress"),
        ("InternetThruway-MIB", "trapName"),
        ("InternetThruway-MIB", "trapTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7FEPCongestionWarning.setStatus(
        ""
    )

ss7BEPCongestionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3052)
)
ss7BEPCongestionWarning.setObjects(
      *(("InternetThruway-MIB", "trapIdKey"),
        ("InternetThruway-MIB", "trapIPAddress"),
        ("InternetThruway-MIB", "trapName"),
        ("InternetThruway-MIB", "trapTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7BEPCongestionWarning.setStatus(
        ""
    )

ss7MTP3CongestionClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3061)
)
ss7MTP3CongestionClear.setObjects(
      *(("InternetThruway-MIB", "mtp3Index"),
        ("InternetThruway-MIB", "mtp3Key"),
        ("InternetThruway-MIB", "mtp3IPAddress"),
        ("InternetThruway-MIB", "mtp3Name"),
        ("InternetThruway-MIB", "mtp3TimeStamp"))
)
if mibBuilder.loadTexts:
    ss7MTP3CongestionClear.setStatus(
        ""
    )

ss7MTP3CongestionMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3063)
)
ss7MTP3CongestionMinor.setObjects(
      *(("InternetThruway-MIB", "mtp3Index"),
        ("InternetThruway-MIB", "mtp3Key"),
        ("InternetThruway-MIB", "mtp3IPAddress"),
        ("InternetThruway-MIB", "mtp3Name"),
        ("InternetThruway-MIB", "mtp3TimeStamp"))
)
if mibBuilder.loadTexts:
    ss7MTP3CongestionMinor.setStatus(
        ""
    )

ss7MTP3CongestionMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3064)
)
ss7MTP3CongestionMajor.setObjects(
      *(("InternetThruway-MIB", "mtp3Index"),
        ("InternetThruway-MIB", "mtp3Key"),
        ("InternetThruway-MIB", "mtp3IPAddress"),
        ("InternetThruway-MIB", "mtp3Name"),
        ("InternetThruway-MIB", "mtp3TimeStamp"))
)
if mibBuilder.loadTexts:
    ss7MTP3CongestionMajor.setStatus(
        ""
    )

ss7MTP3CongestionCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3065)
)
ss7MTP3CongestionCritical.setObjects(
      *(("InternetThruway-MIB", "mtp3Index"),
        ("InternetThruway-MIB", "mtp3Key"),
        ("InternetThruway-MIB", "mtp3IPAddress"),
        ("InternetThruway-MIB", "mtp3Name"),
        ("InternetThruway-MIB", "mtp3TimeStamp"))
)
if mibBuilder.loadTexts:
    ss7MTP3CongestionCritical.setStatus(
        ""
    )

ss7MTP2TrunkFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3071)
)
ss7MTP2TrunkFailureClear.setObjects(
      *(("InternetThruway-MIB", "mtp2Index"),
        ("InternetThruway-MIB", "mtp2Key"),
        ("InternetThruway-MIB", "mtp2IPAddress"),
        ("InternetThruway-MIB", "mtp2Name"),
        ("InternetThruway-MIB", "mtp2CardId"),
        ("InternetThruway-MIB", "mtp2TimeStamp"))
)
if mibBuilder.loadTexts:
    ss7MTP2TrunkFailureClear.setStatus(
        ""
    )

ss7MTP2TrunkFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3075)
)
ss7MTP2TrunkFailureAlarm.setObjects(
      *(("InternetThruway-MIB", "mtp2Index"),
        ("InternetThruway-MIB", "mtp2Key"),
        ("InternetThruway-MIB", "mtp2IPAddress"),
        ("InternetThruway-MIB", "mtp2Name"),
        ("InternetThruway-MIB", "mtp2CardId"),
        ("InternetThruway-MIB", "mtp2AlarmCondition"),
        ("InternetThruway-MIB", "mtp2TimeStamp"))
)
if mibBuilder.loadTexts:
    ss7MTP2TrunkFailureAlarm.setStatus(
        ""
    )

ss7LinksetFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3081)
)
ss7LinksetFailureClear.setObjects(
      *(("InternetThruway-MIB", "lsFailureIndex"),
        ("InternetThruway-MIB", "lsFailureKey"),
        ("InternetThruway-MIB", "lsFailureIPAddress"),
        ("InternetThruway-MIB", "lsFailureName"),
        ("InternetThruway-MIB", "lsFailurePointcode"),
        ("InternetThruway-MIB", "lsFailureTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinksetFailureClear.setStatus(
        ""
    )

ss7LinksetFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3085)
)
ss7LinksetFailureAlarm.setObjects(
      *(("InternetThruway-MIB", "lsFailureIndex"),
        ("InternetThruway-MIB", "lsFailureKey"),
        ("InternetThruway-MIB", "lsFailureIPAddress"),
        ("InternetThruway-MIB", "lsFailureName"),
        ("InternetThruway-MIB", "lsFailurePointcode"),
        ("InternetThruway-MIB", "lsFailureTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinksetFailureAlarm.setStatus(
        ""
    )

ss7DestinationAccessible = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3091)
)
ss7DestinationAccessible.setObjects(
      *(("InternetThruway-MIB", "destInaccessIndex"),
        ("InternetThruway-MIB", "destInaccessKey"),
        ("InternetThruway-MIB", "destInaccessIPAddress"),
        ("InternetThruway-MIB", "destInaccessName"),
        ("InternetThruway-MIB", "destInaccessPointcode"),
        ("InternetThruway-MIB", "destInaccessTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7DestinationAccessible.setStatus(
        ""
    )

ss7DestinationInaccessible = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3092)
)
ss7DestinationInaccessible.setObjects(
      *(("InternetThruway-MIB", "destInaccessIndex"),
        ("InternetThruway-MIB", "destInaccessKey"),
        ("InternetThruway-MIB", "destInaccessIPAddress"),
        ("InternetThruway-MIB", "destInaccessName"),
        ("InternetThruway-MIB", "destInaccessPointcode"),
        ("InternetThruway-MIB", "destInaccessTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7DestinationInaccessible.setStatus(
        ""
    )

ss7DestinationCongestedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3101)
)
ss7DestinationCongestedClear.setObjects(
      *(("InternetThruway-MIB", "destCongestIndex"),
        ("InternetThruway-MIB", "destCongestKey"),
        ("InternetThruway-MIB", "destCongestIPAddress"),
        ("InternetThruway-MIB", "destCongestName"),
        ("InternetThruway-MIB", "destCongestPointcode"),
        ("InternetThruway-MIB", "destCongestCongestionLevel"),
        ("InternetThruway-MIB", "destCongestTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7DestinationCongestedClear.setStatus(
        ""
    )

ss7DestinationCongestedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3103)
)
ss7DestinationCongestedAlarm.setObjects(
      *(("InternetThruway-MIB", "destCongestIndex"),
        ("InternetThruway-MIB", "destCongestKey"),
        ("InternetThruway-MIB", "destCongestIPAddress"),
        ("InternetThruway-MIB", "destCongestName"),
        ("InternetThruway-MIB", "destCongestPointcode"),
        ("InternetThruway-MIB", "destCongestCongestionLevel"),
        ("InternetThruway-MIB", "destCongestTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7DestinationCongestedAlarm.setStatus(
        ""
    )

ss7LinkAlignmentFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3111)
)
ss7LinkAlignmentFailureClear.setObjects(
      *(("InternetThruway-MIB", "linkAlignIndex"),
        ("InternetThruway-MIB", "linkAlignKey"),
        ("InternetThruway-MIB", "linkAlignIPAddress"),
        ("InternetThruway-MIB", "linkAlignName"),
        ("InternetThruway-MIB", "linkAlignLinkCode"),
        ("InternetThruway-MIB", "linkAlignCardId"),
        ("InternetThruway-MIB", "linkAlignLinkSet"),
        ("InternetThruway-MIB", "linkAlignTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinkAlignmentFailureClear.setStatus(
        ""
    )

ss7LinkAlignmentFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 3114)
)
ss7LinkAlignmentFailureAlarm.setObjects(
      *(("InternetThruway-MIB", "linkAlignIndex"),
        ("InternetThruway-MIB", "linkAlignKey"),
        ("InternetThruway-MIB", "linkAlignIPAddress"),
        ("InternetThruway-MIB", "linkAlignName"),
        ("InternetThruway-MIB", "linkAlignLinkCode"),
        ("InternetThruway-MIB", "linkAlignCardId"),
        ("InternetThruway-MIB", "linkAlignLinkSet"),
        ("InternetThruway-MIB", "linkAlignTimeStamp"))
)
if mibBuilder.loadTexts:
    ss7LinkAlignmentFailureAlarm.setStatus(
        ""
    )

ncFoundServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 4011)
)
ncFoundServerTrap.setObjects(
      *(("InternetThruway-MIB", "lsIndex"),
        ("InternetThruway-MIB", "lsKey"),
        ("InternetThruway-MIB", "lsName"),
        ("InternetThruway-MIB", "lsIPAddress"),
        ("InternetThruway-MIB", "lsTimeStamp"))
)
if mibBuilder.loadTexts:
    ncFoundServerTrap.setStatus(
        ""
    )

ncLostServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 4014)
)
ncLostServerTrap.setObjects(
      *(("InternetThruway-MIB", "lsIndex"),
        ("InternetThruway-MIB", "lsKey"),
        ("InternetThruway-MIB", "lsName"),
        ("InternetThruway-MIB", "lsIPAddress"),
        ("InternetThruway-MIB", "lsTimeStamp"))
)
if mibBuilder.loadTexts:
    ncLostServerTrap.setStatus(
        ""
    )

ncStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 4022)
)
ncStateChangeTrap.setObjects(
      *(("InternetThruway-MIB", "ncEthernetName"),
        ("InternetThruway-MIB", "ncEthernetIP"),
        ("InternetThruway-MIB", "ncOperationalState"),
        ("InternetThruway-MIB", "ncStandbyState"),
        ("InternetThruway-MIB", "ncAvailabilityState"))
)
if mibBuilder.loadTexts:
    ncStateChangeTrap.setStatus(
        ""
    )

csgComplexStateTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 4031)
)
csgComplexStateTrapClear.setObjects(
      *(("InternetThruway-MIB", "cplxName"),
        ("InternetThruway-MIB", "cplxLocEthernetName"),
        ("InternetThruway-MIB", "cplxLocEthernetIP"),
        ("InternetThruway-MIB", "cplxLocOperationalState"),
        ("InternetThruway-MIB", "cplxLocStandbyState"),
        ("InternetThruway-MIB", "cplxLocAvailabilityState"),
        ("InternetThruway-MIB", "cplxMateEthernetName"),
        ("InternetThruway-MIB", "cplxMateEthernetIP"),
        ("InternetThruway-MIB", "cplxMateOperationalState"),
        ("InternetThruway-MIB", "cplxMateStandbyState"),
        ("InternetThruway-MIB", "cplxMateAvailabilityState"),
        ("InternetThruway-MIB", "cplxAlarmStatus"))
)
if mibBuilder.loadTexts:
    csgComplexStateTrapClear.setStatus(
        ""
    )

csgComplexStateTrapMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 4034)
)
csgComplexStateTrapMajor.setObjects(
      *(("InternetThruway-MIB", "cplxName"),
        ("InternetThruway-MIB", "cplxLocEthernetName"),
        ("InternetThruway-MIB", "cplxLocEthernetIP"),
        ("InternetThruway-MIB", "cplxLocOperationalState"),
        ("InternetThruway-MIB", "cplxLocStandbyState"),
        ("InternetThruway-MIB", "cplxLocAvailabilityState"),
        ("InternetThruway-MIB", "cplxMateEthernetName"),
        ("InternetThruway-MIB", "cplxMateEthernetIP"),
        ("InternetThruway-MIB", "cplxMateOperationalState"),
        ("InternetThruway-MIB", "cplxMateStandbyState"),
        ("InternetThruway-MIB", "cplxMateAvailabilityState"),
        ("InternetThruway-MIB", "cplxAlarmStatus"))
)
if mibBuilder.loadTexts:
    csgComplexStateTrapMajor.setStatus(
        ""
    )

csgComplexStateTrapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 4035)
)
csgComplexStateTrapCritical.setObjects(
      *(("InternetThruway-MIB", "cplxName"),
        ("InternetThruway-MIB", "cplxLocEthernetName"),
        ("InternetThruway-MIB", "cplxLocEthernetIP"),
        ("InternetThruway-MIB", "cplxLocOperationalState"),
        ("InternetThruway-MIB", "cplxLocStandbyState"),
        ("InternetThruway-MIB", "cplxLocAvailabilityState"),
        ("InternetThruway-MIB", "cplxMateEthernetName"),
        ("InternetThruway-MIB", "cplxMateEthernetIP"),
        ("InternetThruway-MIB", "cplxMateOperationalState"),
        ("InternetThruway-MIB", "cplxMateStandbyState"),
        ("InternetThruway-MIB", "cplxMateAvailabilityState"),
        ("InternetThruway-MIB", "cplxAlarmStatus"))
)
if mibBuilder.loadTexts:
    csgComplexStateTrapCritical.setStatus(
        ""
    )

cisRetrievalFailureTrapMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 4044)
)
if mibBuilder.loadTexts:
    cisRetrievalFailureTrapMajor.setStatus(
        ""
    )

genericNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9001)
)
genericNormal.setObjects(
      *(("InternetThruway-MIB", "trapIdKey"),
        ("InternetThruway-MIB", "trapGenericStr1"),
        ("InternetThruway-MIB", "trapTimeStamp"))
)
if mibBuilder.loadTexts:
    genericNormal.setStatus(
        ""
    )

genericWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9002)
)
genericWarning.setObjects(
      *(("InternetThruway-MIB", "trapIdKey"),
        ("InternetThruway-MIB", "trapGenericStr1"),
        ("InternetThruway-MIB", "trapTimeStamp"))
)
if mibBuilder.loadTexts:
    genericWarning.setStatus(
        ""
    )

genericMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9003)
)
genericMinor.setObjects(
      *(("InternetThruway-MIB", "trapIdKey"),
        ("InternetThruway-MIB", "trapGenericStr1"),
        ("InternetThruway-MIB", "trapTimeStamp"))
)
if mibBuilder.loadTexts:
    genericMinor.setStatus(
        ""
    )

genericMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9004)
)
genericMajor.setObjects(
      *(("InternetThruway-MIB", "trapIdKey"),
        ("InternetThruway-MIB", "trapGenericStr1"),
        ("InternetThruway-MIB", "trapTimeStamp"))
)
if mibBuilder.loadTexts:
    genericMajor.setStatus(
        ""
    )

genericCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9005)
)
genericCritical.setObjects(
      *(("InternetThruway-MIB", "trapIdKey"),
        ("InternetThruway-MIB", "trapGenericStr1"),
        ("InternetThruway-MIB", "trapTimeStamp"))
)
if mibBuilder.loadTexts:
    genericCritical.setStatus(
        ""
    )

hgStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9011)
)
hgStatusClear.setObjects(
      *(("InternetThruway-MIB", "hgKey"),
        ("InternetThruway-MIB", "hgIndex"),
        ("InternetThruway-MIB", "hgName"),
        ("InternetThruway-MIB", "hgIPAddress"),
        ("InternetThruway-MIB", "hgAlarmTimeStamp"))
)
if mibBuilder.loadTexts:
    hgStatusClear.setStatus(
        ""
    )

hgStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9014)
)
hgStatusAlarm.setObjects(
      *(("InternetThruway-MIB", "hgKey"),
        ("InternetThruway-MIB", "hgIndex"),
        ("InternetThruway-MIB", "hgName"),
        ("InternetThruway-MIB", "hgIPAddress"),
        ("InternetThruway-MIB", "hgAlarmTimeStamp"))
)
if mibBuilder.loadTexts:
    hgStatusAlarm.setStatus(
        ""
    )

nasStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9021)
)
nasStatusClear.setObjects(
      *(("InternetThruway-MIB", "nasKey"),
        ("InternetThruway-MIB", "nasIndex"),
        ("InternetThruway-MIB", "nasName"),
        ("InternetThruway-MIB", "nasIPAddress"),
        ("InternetThruway-MIB", "nasAlarmTimeStamp"),
        ("InternetThruway-MIB", "nasCmplxName"))
)
if mibBuilder.loadTexts:
    nasStatusClear.setStatus(
        ""
    )

nasStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 2, 3, 0, 9024)
)
nasStatusAlarm.setObjects(
      *(("InternetThruway-MIB", "nasKey"),
        ("InternetThruway-MIB", "nasIndex"),
        ("InternetThruway-MIB", "nasName"),
        ("InternetThruway-MIB", "nasIPAddress"),
        ("InternetThruway-MIB", "nasAlarmTimeStamp"),
        ("InternetThruway-MIB", "nasCmplxName"))
)
if mibBuilder.loadTexts:
    nasStatusAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "InternetThruway-MIB",
    **{"TimeString": TimeString,
       "PartitionSpaceStatus": PartitionSpaceStatus,
       "ComponentIndex": ComponentIndex,
       "ComponentSysmanState": ComponentSysmanState,
       "LinksetState": LinksetState,
       "LinkState": LinkState,
       "LinkInhibitionState": LinkInhibitionState,
       "LinkCongestionState": LinkCongestionState,
       "LinkAlignmentState": LinkAlignmentState,
       "RouteState": RouteState,
       "DestinationState": DestinationState,
       "UpgradeInProgress": UpgradeInProgress,
       "MTP2AlarmConditionType": MTP2AlarmConditionType,
       "nortel": nortel,
       "dialaccess": dialaccess,
       "csg": csg,
       "system": system,
       "disk": disk,
       "partitionTable": partitionTable,
       "partitionTableEntry": partitionTableEntry,
       "partitionIndex": partitionIndex,
       "partitionName": partitionName,
       "partitionPercentFull": partitionPercentFull,
       "partitionMegsFree": partitionMegsFree,
       "partitionSpaceStatus": partitionSpaceStatus,
       "partitionSpaceKey": partitionSpaceKey,
       "partitionSpaceTimeStamp": partitionSpaceTimeStamp,
       "components": components,
       "componentTable": componentTable,
       "componentTableEntry": componentTableEntry,
       "componentIndex": componentIndex,
       "componentName": componentName,
       "compSecsInCurrentState": compSecsInCurrentState,
       "compProvStateStatus": compProvStateStatus,
       "compProvStateKey": compProvStateKey,
       "compProvStateTimeStamp": compProvStateTimeStamp,
       "compDebugStatus": compDebugStatus,
       "compDebugKey": compDebugKey,
       "compDebugTimeStamp": compDebugTimeStamp,
       "compRestartStatus": compRestartStatus,
       "compRestartKey": compRestartKey,
       "compRestartTimeStamp": compRestartTimeStamp,
       "traps": traps,
       "diskSpaceClear": diskSpaceClear,
       "diskSpaceAlarm": diskSpaceAlarm,
       "etherCardTrapClear": etherCardTrapClear,
       "etherCardTrapMajor": etherCardTrapMajor,
       "etherCardTrapCritical": etherCardTrapCritical,
       "compDebugOff": compDebugOff,
       "compDebugOn": compDebugOn,
       "compStateClear": compStateClear,
       "compStateAlarm": compStateAlarm,
       "restartStateClear": restartStateClear,
       "restartStateAlarm": restartStateAlarm,
       "ss7LinkFailureClear": ss7LinkFailureClear,
       "ss7LinkFailureAlarm": ss7LinkFailureAlarm,
       "ss7LinkCongestionClear": ss7LinkCongestionClear,
       "ss7LinkCongestionAlarm": ss7LinkCongestionAlarm,
       "ss7ISUPFailureClear": ss7ISUPFailureClear,
       "ss7ISUPFailureAlarm": ss7ISUPFailureAlarm,
       "ss7ISUPCongestionClear": ss7ISUPCongestionClear,
       "ss7ISUPCongestionAlarm": ss7ISUPCongestionAlarm,
       "ss7FEPCongestionWarning": ss7FEPCongestionWarning,
       "ss7BEPCongestionWarning": ss7BEPCongestionWarning,
       "ss7MTP3CongestionClear": ss7MTP3CongestionClear,
       "ss7MTP3CongestionMinor": ss7MTP3CongestionMinor,
       "ss7MTP3CongestionMajor": ss7MTP3CongestionMajor,
       "ss7MTP3CongestionCritical": ss7MTP3CongestionCritical,
       "ss7MTP2TrunkFailureClear": ss7MTP2TrunkFailureClear,
       "ss7MTP2TrunkFailureAlarm": ss7MTP2TrunkFailureAlarm,
       "ss7LinksetFailureClear": ss7LinksetFailureClear,
       "ss7LinksetFailureAlarm": ss7LinksetFailureAlarm,
       "ss7DestinationAccessible": ss7DestinationAccessible,
       "ss7DestinationInaccessible": ss7DestinationInaccessible,
       "ss7DestinationCongestedClear": ss7DestinationCongestedClear,
       "ss7DestinationCongestedAlarm": ss7DestinationCongestedAlarm,
       "ss7LinkAlignmentFailureClear": ss7LinkAlignmentFailureClear,
       "ss7LinkAlignmentFailureAlarm": ss7LinkAlignmentFailureAlarm,
       "ncFoundServerTrap": ncFoundServerTrap,
       "ncLostServerTrap": ncLostServerTrap,
       "ncStateChangeTrap": ncStateChangeTrap,
       "csgComplexStateTrapClear": csgComplexStateTrapClear,
       "csgComplexStateTrapMajor": csgComplexStateTrapMajor,
       "csgComplexStateTrapCritical": csgComplexStateTrapCritical,
       "cisRetrievalFailureTrapMajor": cisRetrievalFailureTrapMajor,
       "genericNormal": genericNormal,
       "genericWarning": genericWarning,
       "genericMinor": genericMinor,
       "genericMajor": genericMajor,
       "genericCritical": genericCritical,
       "hgStatusClear": hgStatusClear,
       "hgStatusAlarm": hgStatusAlarm,
       "nasStatusClear": nasStatusClear,
       "nasStatusAlarm": nasStatusAlarm,
       "trapCompName": trapCompName,
       "trapFileName": trapFileName,
       "trapDate": trapDate,
       "trapGenericStr1": trapGenericStr1,
       "trapIdKey": trapIdKey,
       "trapIPAddress": trapIPAddress,
       "trapName": trapName,
       "trapTimeStamp": trapTimeStamp,
       "alarms": alarms,
       "alarmMaskInt1": alarmMaskInt1,
       "alarmStatusInt1": alarmStatusInt1,
       "alarmStatusInt2": alarmStatusInt2,
       "alarmStatusInt3": alarmStatusInt3,
       "alarmMaskInt2": alarmMaskInt2,
       "hgAlarmTable": hgAlarmTable,
       "hgAlarmTableEntry": hgAlarmTableEntry,
       "hgIndex": hgIndex,
       "hgName": hgName,
       "hgKey": hgKey,
       "hgAlarmTimeStamp": hgAlarmTimeStamp,
       "hgIPAddress": hgIPAddress,
       "nasAlarmTable": nasAlarmTable,
       "nasAlarmTableEntry": nasAlarmTableEntry,
       "nasIndex": nasIndex,
       "nasName": nasName,
       "nasKey": nasKey,
       "nasAlarmTimeStamp": nasAlarmTimeStamp,
       "nasIPAddress": nasIPAddress,
       "nasCmplxName": nasCmplxName,
       "ss7LinkFailureAlarmTable": ss7LinkFailureAlarmTable,
       "ss7LinkFailureAlarmTableEntry": ss7LinkFailureAlarmTableEntry,
       "lfIndex": lfIndex,
       "lfKey": lfKey,
       "lfIPAddress": lfIPAddress,
       "lfLinkCode": lfLinkCode,
       "lfTimeStamp": lfTimeStamp,
       "lfName": lfName,
       "lfCardId": lfCardId,
       "lfLinkSet": lfLinkSet,
       "ss7LinkCongestionAlarmTable": ss7LinkCongestionAlarmTable,
       "ss7LinkCongestionAlarmTableEntry": ss7LinkCongestionAlarmTableEntry,
       "lcIndex": lcIndex,
       "lcKey": lcKey,
       "lcIPAddress": lcIPAddress,
       "lcLinkCode": lcLinkCode,
       "lcTimeStamp": lcTimeStamp,
       "lcName": lcName,
       "lcCardId": lcCardId,
       "lcLinkSet": lcLinkSet,
       "ss7ISUPFailureAlarmTable": ss7ISUPFailureAlarmTable,
       "ss7ISUPFailureAlarmTableEntry": ss7ISUPFailureAlarmTableEntry,
       "ifIndex": ifIndex,
       "ifKey": ifKey,
       "ifIPAddress": ifIPAddress,
       "ifTimeStamp": ifTimeStamp,
       "ifName": ifName,
       "ss7ISUPCongestionAlarmTable": ss7ISUPCongestionAlarmTable,
       "ss7ISUPCongestionAlarmTableEntry": ss7ISUPCongestionAlarmTableEntry,
       "icIndex": icIndex,
       "icKey": icKey,
       "icIPAddress": icIPAddress,
       "icCongestionLevel": icCongestionLevel,
       "icTimeStamp": icTimeStamp,
       "icName": icName,
       "ss7MTP3CongestionAlarmTable": ss7MTP3CongestionAlarmTable,
       "ss7MTP3CongestionAlarmTableEntry": ss7MTP3CongestionAlarmTableEntry,
       "mtp3Index": mtp3Index,
       "mtp3Key": mtp3Key,
       "mtp3IPAddress": mtp3IPAddress,
       "mtp3CongestionLevel": mtp3CongestionLevel,
       "mtp3TimeStamp": mtp3TimeStamp,
       "mtp3Name": mtp3Name,
       "ss7MTP2TrunkFailureAlarmTable": ss7MTP2TrunkFailureAlarmTable,
       "ss7MTP2TrunkFailureAlarmTableEntry": ss7MTP2TrunkFailureAlarmTableEntry,
       "mtp2Index": mtp2Index,
       "mtp2Key": mtp2Key,
       "mtp2IPAddress": mtp2IPAddress,
       "mtp2Name": mtp2Name,
       "mtp2CardId": mtp2CardId,
       "mtp2AlarmCondition": mtp2AlarmCondition,
       "mtp2TimeStamp": mtp2TimeStamp,
       "ss7LinksetFailureAlarmTable": ss7LinksetFailureAlarmTable,
       "ss7LinksetFailureAlarmTableEntry": ss7LinksetFailureAlarmTableEntry,
       "lsFailureIndex": lsFailureIndex,
       "lsFailureKey": lsFailureKey,
       "lsFailureIPAddress": lsFailureIPAddress,
       "lsFailureName": lsFailureName,
       "lsFailurePointcode": lsFailurePointcode,
       "lsFailureTimeStamp": lsFailureTimeStamp,
       "ss7DestinationInaccessibleAlarmTable": ss7DestinationInaccessibleAlarmTable,
       "ss7DestinationInaccessibleAlarmTableEntry": ss7DestinationInaccessibleAlarmTableEntry,
       "destInaccessIndex": destInaccessIndex,
       "destInaccessKey": destInaccessKey,
       "destInaccessIPAddress": destInaccessIPAddress,
       "destInaccessName": destInaccessName,
       "destInaccessPointcode": destInaccessPointcode,
       "destInaccessTimeStamp": destInaccessTimeStamp,
       "ss7DestinationCongestedAlarmTable": ss7DestinationCongestedAlarmTable,
       "ss7DestinationCongestedAlarmTableEntry": ss7DestinationCongestedAlarmTableEntry,
       "destCongestIndex": destCongestIndex,
       "destCongestKey": destCongestKey,
       "destCongestIPAddress": destCongestIPAddress,
       "destCongestName": destCongestName,
       "destCongestPointcode": destCongestPointcode,
       "destCongestCongestionLevel": destCongestCongestionLevel,
       "destCongestTimeStamp": destCongestTimeStamp,
       "ss7LinkAlignmentAlarmTable": ss7LinkAlignmentAlarmTable,
       "ss7LinkAlignmentAlarmTableEntry": ss7LinkAlignmentAlarmTableEntry,
       "linkAlignIndex": linkAlignIndex,
       "linkAlignKey": linkAlignKey,
       "linkAlignIPAddress": linkAlignIPAddress,
       "linkAlignName": linkAlignName,
       "linkAlignLinkCode": linkAlignLinkCode,
       "linkAlignTimeStamp": linkAlignTimeStamp,
       "linkAlignCardId": linkAlignCardId,
       "linkAlignLinkSet": linkAlignLinkSet,
       "csgComplexStateTrapInfo": csgComplexStateTrapInfo,
       "cplxName": cplxName,
       "cplxLocEthernetName": cplxLocEthernetName,
       "cplxLocEthernetIP": cplxLocEthernetIP,
       "cplxLocOperationalState": cplxLocOperationalState,
       "cplxLocStandbyState": cplxLocStandbyState,
       "cplxLocAvailabilityState": cplxLocAvailabilityState,
       "cplxMateEthernetName": cplxMateEthernetName,
       "cplxMateEthernetIP": cplxMateEthernetIP,
       "cplxMateOperationalState": cplxMateOperationalState,
       "cplxMateStandbyState": cplxMateStandbyState,
       "cplxMateAvailabilityState": cplxMateAvailabilityState,
       "cplxAlarmStatus": cplxAlarmStatus,
       "ncServer": ncServer,
       "lostServerAlarmTable": lostServerAlarmTable,
       "lostServerAlarmTableEntry": lostServerAlarmTableEntry,
       "lsIndex": lsIndex,
       "lsKey": lsKey,
       "lsIPAddress": lsIPAddress,
       "lsName": lsName,
       "lsTimeStamp": lsTimeStamp,
       "ncServerId": ncServerId,
       "ncServerName": ncServerName,
       "ncHostName": ncHostName,
       "ncEthernetName": ncEthernetName,
       "ncEthernetIP": ncEthernetIP,
       "ncClusterName": ncClusterName,
       "ncClusterIP": ncClusterIP,
       "ncOperationalState": ncOperationalState,
       "ncStandbyState": ncStandbyState,
       "ncAvailabilityState": ncAvailabilityState,
       "ncSoftwareVersion": ncSoftwareVersion,
       "ncUpgradeInProgress": ncUpgradeInProgress,
       "ss7": ss7,
       "linksetTable": linksetTable,
       "linksetTableEntry": linksetTableEntry,
       "linksetIndex": linksetIndex,
       "linksetId": linksetId,
       "linksetAdjPointcode": linksetAdjPointcode,
       "linksetState": linksetState,
       "linkTable": linkTable,
       "linkTableEntry": linkTableEntry,
       "linkIndex": linkIndex,
       "linkId": linkId,
       "linkHostname": linkHostname,
       "linkCardDeviceName": linkCardDeviceName,
       "linkState": linkState,
       "linkInhibitionState": linkInhibitionState,
       "linkCongestionState": linkCongestionState,
       "linkAlignmentState": linkAlignmentState,
       "linkNumMSUReceived": linkNumMSUReceived,
       "linkNumMSUDiscarded": linkNumMSUDiscarded,
       "linkNumMSUTransmitted": linkNumMSUTransmitted,
       "linkNumSIFReceived": linkNumSIFReceived,
       "linkNumSIFTransmitted": linkNumSIFTransmitted,
       "linkNumAutoChangeovers": linkNumAutoChangeovers,
       "linkNumUnexpectedMsgs": linkNumUnexpectedMsgs,
       "routeTable": routeTable,
       "routeTableEntry": routeTableEntry,
       "routeIndex": routeIndex,
       "routeId": routeId,
       "routeDestPointCode": routeDestPointCode,
       "routeState": routeState,
       "routeRank": routeRank,
       "routeLinksetId": routeLinksetId,
       "destinationTable": destinationTable,
       "destinationTableEntry": destinationTableEntry,
       "destIndex": destIndex,
       "destPointCode": destPointCode,
       "destState": destState,
       "destRuleId": destRuleId,
       "omData": omData,
       "linkOMs": linkOMs,
       "linkOMTable": linkOMTable,
       "linkOMTableEntry": linkOMTableEntry,
       "linkOMId": linkOMId,
       "linkOMSetId": linkOMSetId,
       "linkFailures": linkFailures,
       "linkCongestions": linkCongestions,
       "linkInhibits": linkInhibits,
       "linkTransmittedMSUs": linkTransmittedMSUs,
       "linkReceivedMSUs": linkReceivedMSUs,
       "linkRemoteProcOutages": linkRemoteProcOutages,
       "maintenanceOMs": maintenanceOMs,
       "bLATimerExpiries": bLATimerExpiries,
       "rLCTimerExpiries": rLCTimerExpiries,
       "uBATimerExpiries": uBATimerExpiries,
       "rSATimerExpiries": rSATimerExpiries,
       "callOMs": callOMs,
       "outCallAttempts": outCallAttempts,
       "outCallNormalCompletions": outCallNormalCompletions,
       "outCallAbnormalCompletions": outCallAbnormalCompletions,
       "userBusyOutCallRejects": userBusyOutCallRejects,
       "tempFailOutCallRejects": tempFailOutCallRejects,
       "userUnavailableOutCallRejects": userUnavailableOutCallRejects,
       "abnormalReleaseOutCallRejects": abnormalReleaseOutCallRejects,
       "otherOutCallRejects": otherOutCallRejects,
       "cumulativeActiveOutCalls": cumulativeActiveOutCalls,
       "currentlyActiveOutCalls": currentlyActiveOutCalls,
       "currentlyActiveDigitalOutCalls": currentlyActiveDigitalOutCalls,
       "currentlyActiveAnalogOutCalls": currentlyActiveAnalogOutCalls,
       "inCallAttempts": inCallAttempts,
       "inCallNormalCompletions": inCallNormalCompletions,
       "inCallAbnormalCompletions": inCallAbnormalCompletions,
       "userBusyInCallRejects": userBusyInCallRejects,
       "tempFailInCallRejects": tempFailInCallRejects,
       "userUnavailableInCallRejects": userUnavailableInCallRejects,
       "abnormalReleaseInCallRejects": abnormalReleaseInCallRejects,
       "otherInCallRejects": otherInCallRejects,
       "cumulativeActiveInCalls": cumulativeActiveInCalls,
       "currentlyActiveInCalls": currentlyActiveInCalls,
       "currentlyActiveDigitalInCalls": currentlyActiveDigitalInCalls,
       "currentlyActiveAnalogInCalls": currentlyActiveAnalogInCalls,
       "trunkGroupOMs": trunkGroupOMs,
       "trunkCallOMTable": trunkCallOMTable,
       "trunkCallOMTableEntry": trunkCallOMTableEntry,
       "trunkCallOMIndex": trunkCallOMIndex,
       "trunkGroupCLLI": trunkGroupCLLI,
       "numberOfCircuits": numberOfCircuits,
       "trunkOutCallAttempts": trunkOutCallAttempts,
       "trunkOutCallNormalCompletions": trunkOutCallNormalCompletions,
       "trunkOutCallAbnormalCompletions": trunkOutCallAbnormalCompletions,
       "trunkUserBusyOutCallRejects": trunkUserBusyOutCallRejects,
       "trunkTempFailOutCallRejects": trunkTempFailOutCallRejects,
       "trunkUserUnavailableOutCallRejects": trunkUserUnavailableOutCallRejects,
       "trunkAbnormalReleaseOutCallRejects": trunkAbnormalReleaseOutCallRejects,
       "trunkOtherOutCallRejects": trunkOtherOutCallRejects,
       "trunkCumulativeActiveOutCalls": trunkCumulativeActiveOutCalls,
       "trunkCurrentlyActiveOutCalls": trunkCurrentlyActiveOutCalls,
       "trunkCurrentlyActiveDigitalOutCalls": trunkCurrentlyActiveDigitalOutCalls,
       "trunkCurrentlyActiveAnalogOutCalls": trunkCurrentlyActiveAnalogOutCalls,
       "trunkInCallAttempts": trunkInCallAttempts,
       "trunkInCallNormalCompletions": trunkInCallNormalCompletions,
       "trunkInCallAbnormalCompletions": trunkInCallAbnormalCompletions,
       "trunkUserBusyInCallRejects": trunkUserBusyInCallRejects,
       "trunkTempFailInCallRejects": trunkTempFailInCallRejects,
       "trunkUserUnavailableInCallRejects": trunkUserUnavailableInCallRejects,
       "trunkAbnormalReleaseInCallRejects": trunkAbnormalReleaseInCallRejects,
       "trunkOtherInCallRejects": trunkOtherInCallRejects,
       "trunkCumulativeActiveInCalls": trunkCumulativeActiveInCalls,
       "trunkCurrentlyActiveInCalls": trunkCurrentlyActiveInCalls,
       "trunkCurrentlyActiveDigitalInCalls": trunkCurrentlyActiveDigitalInCalls,
       "trunkCurrentlyActiveAnalogInCalls": trunkCurrentlyActiveAnalogInCalls,
       "trunkAllActiveCalls": trunkAllActiveCalls,
       "trunkOccupancyPerCCS": trunkOccupancyPerCCS,
       "trafficInCCSs": trafficInCCSs,
       "trafficInCCSIncomings": trafficInCCSIncomings,
       "localBusyInCCSs": localBusyInCCSs,
       "remoteBusyInCCSs": remoteBusyInCCSs,
       "phoneNumberOMs": phoneNumberOMs,
       "phoneCallOMTable": phoneCallOMTable,
       "phoneCallOMTableEntry": phoneCallOMTableEntry,
       "phoneCallOMIndex": phoneCallOMIndex,
       "phoneNumber": phoneNumber,
       "phoneDialCallAttempts": phoneDialCallAttempts,
       "phoneDialCallNormalCompletions": phoneDialCallNormalCompletions,
       "phoneDialCallAbnormalCompletions": phoneDialCallAbnormalCompletions,
       "phoneUserBusyDialCallRejects": phoneUserBusyDialCallRejects,
       "phoneTempFailDialCallRejects": phoneTempFailDialCallRejects,
       "phoneUserUnavailableDialCallRejects": phoneUserUnavailableDialCallRejects,
       "phoneAbnormalReleaseDialCallRejects": phoneAbnormalReleaseDialCallRejects,
       "phoneOtherDialCallRejects": phoneOtherDialCallRejects,
       "phoneCumulativeActiveDialCalls": phoneCumulativeActiveDialCalls,
       "phoneCurrentlyActiveDialCalls": phoneCurrentlyActiveDialCalls,
       "phoneCurrentlyActiveDigitalDialCalls": phoneCurrentlyActiveDigitalDialCalls,
       "phoneCurrentlyActiveAnalogDialCalls": phoneCurrentlyActiveAnalogDialCalls,
       "systemOMs": systemOMs,
       "csgComplexCLLI": csgComplexCLLI,
       "serverHostName": serverHostName,
       "serverIpAddress": serverIpAddress,
       "serverCLLI": serverCLLI,
       "mateServerHostName": mateServerHostName,
       "mateServerIpAddress": mateServerIpAddress,
       "serverMemSize": serverMemSize,
       "provisionedDPCs": provisionedDPCs,
       "provisionedCircuits": provisionedCircuits,
       "inserviceCircuits": inserviceCircuits,
       "provisionedNASes": provisionedNASes,
       "aliveNASes": aliveNASes,
       "inserviceNASes": inserviceNASes,
       "provsionedCards": provsionedCards,
       "inserviceCards": inserviceCards,
       "provisionedPorts": provisionedPorts,
       "inservicePorts": inservicePorts,
       "userCPUUsage": userCPUUsage,
       "systemCPUUsage": systemCPUUsage,
       "totalCPUUsage": totalCPUUsage,
       "maxCPUUsage": maxCPUUsage,
       "avgLoad": avgLoad,
       "systemCallRate": systemCallRate,
       "contextSwitchRate": contextSwitchRate,
       "lastUpdateOMFile": lastUpdateOMFile,
       "nasOMs": nasOMs,
       "nasCallOMTable": nasCallOMTable,
       "nasCallOMTableEntry": nasCallOMTableEntry,
       "nasCallOMIndex": nasCallOMIndex,
       "nasName1": nasName1,
       "numberOfPorts": numberOfPorts,
       "nasOutCallAttempts": nasOutCallAttempts,
       "nasOutCallNormalCompletions": nasOutCallNormalCompletions,
       "nasOutCallAbnormalCompletions": nasOutCallAbnormalCompletions,
       "nasUserBusyOutCallRejects": nasUserBusyOutCallRejects,
       "nasTempFailOutCallRejects": nasTempFailOutCallRejects,
       "nasUserUnavailableOutCallRejects": nasUserUnavailableOutCallRejects,
       "nasAbnormalReleaseOutCallRejects": nasAbnormalReleaseOutCallRejects,
       "nasOtherOutCallRejects": nasOtherOutCallRejects,
       "nasCumulativeActiveOutCalls": nasCumulativeActiveOutCalls,
       "nasCurrentlyActiveOutCalls": nasCurrentlyActiveOutCalls,
       "nasCurrentlyActiveDigitalOutCalls": nasCurrentlyActiveDigitalOutCalls,
       "nasCurrentlyActiveAnalogOutCalls": nasCurrentlyActiveAnalogOutCalls,
       "nasInCallAttempts": nasInCallAttempts,
       "nasInCallNormalCompletions": nasInCallNormalCompletions,
       "nasInCallAbnormalCompletions": nasInCallAbnormalCompletions,
       "nasUserBusyInCallRejects": nasUserBusyInCallRejects,
       "nasTempFailInCallRejects": nasTempFailInCallRejects,
       "nasUserUnavailableInCallRejects": nasUserUnavailableInCallRejects,
       "nasAbnormalReleaseInCallRejects": nasAbnormalReleaseInCallRejects,
       "nasOtherInCallRejects": nasOtherInCallRejects,
       "nasCumulativeActiveInCalls": nasCumulativeActiveInCalls,
       "nasCurrentlyActiveInCalls": nasCurrentlyActiveInCalls,
       "nasCurrentlyActiveDigitalInCalls": nasCurrentlyActiveDigitalInCalls,
       "nasCurrentlyActiveAnalogInCalls": nasCurrentlyActiveAnalogInCalls,
       "nasAllActiveCalls": nasAllActiveCalls,
       "nasMaxPortsUsed": nasMaxPortsUsed,
       "nasMinPortsUsed": nasMinPortsUsed,
       "nasCurrentlyInUsePorts": nasCurrentlyInUsePorts}
)
