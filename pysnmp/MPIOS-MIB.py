# SNMP MIB module (MPIOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPIOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:51 2024
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpios = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_IosSystem_ObjectIdentity = ObjectIdentity
iosSystem = _IosSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1)
)
_IosObjects_ObjectIdentity = ObjectIdentity
iosObjects = _IosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1)
)
_SysMemory_ObjectIdentity = ObjectIdentity
sysMemory = _SysMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1)
)
_NumBytesFree_Type = Integer32
_NumBytesFree_Object = MibScalar
numBytesFree = _NumBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 1),
    _NumBytesFree_Type()
)
numBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesFree.setStatus("current")
_NumBlocksFree_Type = Integer32
_NumBlocksFree_Object = MibScalar
numBlocksFree = _NumBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 2),
    _NumBlocksFree_Type()
)
numBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksFree.setStatus("current")
_AvgBlockSizeFree_Type = Integer32
_AvgBlockSizeFree_Object = MibScalar
avgBlockSizeFree = _AvgBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 3),
    _AvgBlockSizeFree_Type()
)
avgBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBlockSizeFree.setStatus("current")
_MaxBlockSizeFree_Type = Integer32
_MaxBlockSizeFree_Object = MibScalar
maxBlockSizeFree = _MaxBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 4),
    _MaxBlockSizeFree_Type()
)
maxBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBlockSizeFree.setStatus("current")
_NumBytesAlloc_Type = Integer32
_NumBytesAlloc_Object = MibScalar
numBytesAlloc = _NumBytesAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 5),
    _NumBytesAlloc_Type()
)
numBytesAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesAlloc.setStatus("current")
_NumBlocksAlloc_Type = Integer32
_NumBlocksAlloc_Object = MibScalar
numBlocksAlloc = _NumBlocksAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 6),
    _NumBlocksAlloc_Type()
)
numBlocksAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksAlloc.setStatus("current")
_AvgBlockSizeAlloc_Type = Integer32
_AvgBlockSizeAlloc_Object = MibScalar
avgBlockSizeAlloc = _AvgBlockSizeAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 7),
    _AvgBlockSizeAlloc_Type()
)
avgBlockSizeAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBlockSizeAlloc.setStatus("current")
_MemoryTotalBytes_Type = Integer32
_MemoryTotalBytes_Object = MibScalar
memoryTotalBytes = _MemoryTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 8),
    _MemoryTotalBytes_Type()
)
memoryTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotalBytes.setStatus("current")
_AllocBytesPercent_Type = Integer32
_AllocBytesPercent_Object = MibScalar
allocBytesPercent = _AllocBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 1, 9),
    _AllocBytesPercent_Type()
)
allocBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allocBytesPercent.setStatus("current")
_SysTask_ObjectIdentity = ObjectIdentity
sysTask = _SysTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2)
)
_TaskTable_Object = MibTable
taskTable = _TaskTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    taskTable.setStatus("current")
_TaskEntry_Object = MibTableRow
taskEntry = _TaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1)
)
taskEntry.setIndexNames(
    (0, "MPIOS-MIB", "taskId"),
)
if mibBuilder.loadTexts:
    taskEntry.setStatus("current")
_TaskId_Type = Unsigned32
_TaskId_Object = MibTableColumn
taskId = _TaskId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 1),
    _TaskId_Type()
)
taskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskId.setStatus("current")
_TaskName_Type = DisplayString
_TaskName_Object = MibTableColumn
taskName = _TaskName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 2),
    _TaskName_Type()
)
taskName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskName.setStatus("current")
_TaskPriority_Type = Integer32
_TaskPriority_Object = MibTableColumn
taskPriority = _TaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 3),
    _TaskPriority_Type()
)
taskPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskPriority.setStatus("current")


class _TaskStatus_Type(Integer32):
    """Custom type taskStatus based on Integer32"""
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
        *(("task-delay", 3),
          ("task-deleted", 4),
          ("task-ready", 1),
          ("task-suspended", 2))
    )


_TaskStatus_Type.__name__ = "Integer32"
_TaskStatus_Object = MibTableColumn
taskStatus = _TaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 4),
    _TaskStatus_Type()
)
taskStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskStatus.setStatus("current")
_TaskOptions_Type = Integer32
_TaskOptions_Object = MibTableColumn
taskOptions = _TaskOptions_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 5),
    _TaskOptions_Type()
)
taskOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskOptions.setStatus("current")
_TaskMain_Type = DisplayString
_TaskMain_Object = MibTableColumn
taskMain = _TaskMain_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 6),
    _TaskMain_Type()
)
taskMain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskMain.setStatus("current")
_TaskStackPtr_Type = Unsigned32
_TaskStackPtr_Object = MibTableColumn
taskStackPtr = _TaskStackPtr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 7),
    _TaskStackPtr_Type()
)
taskStackPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackPtr.setStatus("current")
_TaskStackBase_Type = Unsigned32
_TaskStackBase_Object = MibTableColumn
taskStackBase = _TaskStackBase_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 8),
    _TaskStackBase_Type()
)
taskStackBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackBase.setStatus("current")
_TaskStackPos_Type = Unsigned32
_TaskStackPos_Object = MibTableColumn
taskStackPos = _TaskStackPos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 9),
    _TaskStackPos_Type()
)
taskStackPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackPos.setStatus("current")
_TaskStackEnd_Type = Unsigned32
_TaskStackEnd_Object = MibTableColumn
taskStackEnd = _TaskStackEnd_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 10),
    _TaskStackEnd_Type()
)
taskStackEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackEnd.setStatus("current")
_TaskStackSize_Type = Unsigned32
_TaskStackSize_Object = MibTableColumn
taskStackSize = _TaskStackSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 11),
    _TaskStackSize_Type()
)
taskStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskStackSize.setStatus("current")
_TaskStackSizeUsage_Type = Unsigned32
_TaskStackSizeUsage_Object = MibTableColumn
taskStackSizeUsage = _TaskStackSizeUsage_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 12),
    _TaskStackSizeUsage_Type()
)
taskStackSizeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackSizeUsage.setStatus("current")
_TaskStackMaxUsed_Type = Unsigned32
_TaskStackMaxUsed_Object = MibTableColumn
taskStackMaxUsed = _TaskStackMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 13),
    _TaskStackMaxUsed_Type()
)
taskStackMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackMaxUsed.setStatus("current")
_TaskStackFree_Type = Unsigned32
_TaskStackFree_Object = MibTableColumn
taskStackFree = _TaskStackFree_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 14),
    _TaskStackFree_Type()
)
taskStackFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackFree.setStatus("current")
_TaskErrorStatus_Type = Integer32
_TaskErrorStatus_Object = MibTableColumn
taskErrorStatus = _TaskErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 1, 1, 15),
    _TaskErrorStatus_Type()
)
taskErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskErrorStatus.setStatus("current")
_TaskDescr_Type = DisplayString
_TaskDescr_Object = MibScalar
taskDescr = _TaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 2, 2),
    _TaskDescr_Type()
)
taskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskDescr.setStatus("current")
_SysCpu_ObjectIdentity = ObjectIdentity
sysCpu = _SysCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3)
)


class _SysCpuStatus_Type(Integer32):
    """Custom type sysCpuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSpyCpu", 1),
          ("spyCpu", 2))
    )


_SysCpuStatus_Type.__name__ = "Integer32"
_SysCpuStatus_Object = MibScalar
sysCpuStatus = _SysCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 1),
    _SysCpuStatus_Type()
)
sysCpuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCpuStatus.setStatus("current")


class _SysCpuTaskTabView_Type(Integer32):
    """Custom type sysCpuTaskTabView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detailed", 1),
          ("simple", 2))
    )


_SysCpuTaskTabView_Type.__name__ = "Integer32"
_SysCpuTaskTabView_Object = MibScalar
sysCpuTaskTabView = _SysCpuTaskTabView_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 2),
    _SysCpuTaskTabView_Type()
)
sysCpuTaskTabView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCpuTaskTabView.setStatus("current")


class _CheckCpuTimeInterval_Type(Integer32):
    """Custom type checkCpuTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CheckCpuTimeInterval_Type.__name__ = "Integer32"
_CheckCpuTimeInterval_Object = MibScalar
checkCpuTimeInterval = _CheckCpuTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 3),
    _CheckCpuTimeInterval_Type()
)
checkCpuTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    checkCpuTimeInterval.setStatus("current")
_CpuTaskTable_Object = MibTable
cpuTaskTable = _CpuTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cpuTaskTable.setStatus("current")
_CpuTaskEntry_Object = MibTableRow
cpuTaskEntry = _CpuTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1)
)
cpuTaskEntry.setIndexNames(
    (0, "MPIOS-MIB", "cpuTaskId"),
)
if mibBuilder.loadTexts:
    cpuTaskEntry.setStatus("current")
_CpuTaskId_Type = Integer32
_CpuTaskId_Object = MibTableColumn
cpuTaskId = _CpuTaskId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 1),
    _CpuTaskId_Type()
)
cpuTaskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskId.setStatus("current")
_CpuTaskName_Type = OctetString
_CpuTaskName_Object = MibTableColumn
cpuTaskName = _CpuTaskName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 2),
    _CpuTaskName_Type()
)
cpuTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskName.setStatus("current")
_CpuTaskPri_Type = Integer32
_CpuTaskPri_Object = MibTableColumn
cpuTaskPri = _CpuTaskPri_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 3),
    _CpuTaskPri_Type()
)
cpuTaskPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskPri.setStatus("current")
_CpuTaskDeltaUtil_Type = Integer32
_CpuTaskDeltaUtil_Object = MibTableColumn
cpuTaskDeltaUtil = _CpuTaskDeltaUtil_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 4),
    _CpuTaskDeltaUtil_Type()
)
cpuTaskDeltaUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskDeltaUtil.setStatus("current")
_CpuTaskDeltaTicks_Type = Integer32
_CpuTaskDeltaTicks_Object = MibTableColumn
cpuTaskDeltaTicks = _CpuTaskDeltaTicks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 5),
    _CpuTaskDeltaTicks_Type()
)
cpuTaskDeltaTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskDeltaTicks.setStatus("current")
_CpuTaskAverageUtil_Type = Integer32
_CpuTaskAverageUtil_Object = MibTableColumn
cpuTaskAverageUtil = _CpuTaskAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 6),
    _CpuTaskAverageUtil_Type()
)
cpuTaskAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskAverageUtil.setStatus("current")
_CpuTaskTotalTicks_Type = Integer32
_CpuTaskTotalTicks_Object = MibTableColumn
cpuTaskTotalTicks = _CpuTaskTotalTicks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 7),
    _CpuTaskTotalTicks_Type()
)
cpuTaskTotalTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskTotalTicks.setStatus("current")
_CpuTaskCurrentUtil_Type = Integer32
_CpuTaskCurrentUtil_Object = MibTableColumn
cpuTaskCurrentUtil = _CpuTaskCurrentUtil_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 4, 1, 8),
    _CpuTaskCurrentUtil_Type()
)
cpuTaskCurrentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTaskCurrentUtil.setStatus("current")
_CpuUtilTable_Object = MibTable
cpuUtilTable = _CpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cpuUtilTable.setStatus("current")
_CpuUtilEntry_Object = MibTableRow
cpuUtilEntry = _CpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1)
)
cpuUtilEntry.setIndexNames(
    (0, "MPIOS-MIB", "cpuUtilCpuId"),
)
if mibBuilder.loadTexts:
    cpuUtilEntry.setStatus("current")
_CpuUtilCpuId_Type = Integer32
_CpuUtilCpuId_Object = MibTableColumn
cpuUtilCpuId = _CpuUtilCpuId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 1),
    _CpuUtilCpuId_Type()
)
cpuUtilCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilCpuId.setStatus("current")
_CpuUtilDeltaUtil_Type = Integer32
_CpuUtilDeltaUtil_Object = MibTableColumn
cpuUtilDeltaUtil = _CpuUtilDeltaUtil_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 2),
    _CpuUtilDeltaUtil_Type()
)
cpuUtilDeltaUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilDeltaUtil.setStatus("current")
_CpuUtilDeltaUsedTicks_Type = Integer32
_CpuUtilDeltaUsedTicks_Object = MibTableColumn
cpuUtilDeltaUsedTicks = _CpuUtilDeltaUsedTicks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 3),
    _CpuUtilDeltaUsedTicks_Type()
)
cpuUtilDeltaUsedTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilDeltaUsedTicks.setStatus("current")
_CpuUtilDeltaTicks_Type = Integer32
_CpuUtilDeltaTicks_Object = MibTableColumn
cpuUtilDeltaTicks = _CpuUtilDeltaTicks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 4),
    _CpuUtilDeltaTicks_Type()
)
cpuUtilDeltaTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilDeltaTicks.setStatus("current")
_CpuUtilDeltaTimes_Type = Integer32
_CpuUtilDeltaTimes_Object = MibTableColumn
cpuUtilDeltaTimes = _CpuUtilDeltaTimes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 5),
    _CpuUtilDeltaTimes_Type()
)
cpuUtilDeltaTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilDeltaTimes.setStatus("current")
_CpuUtilAverageUtil_Type = Integer32
_CpuUtilAverageUtil_Object = MibTableColumn
cpuUtilAverageUtil = _CpuUtilAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 6),
    _CpuUtilAverageUtil_Type()
)
cpuUtilAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilAverageUtil.setStatus("current")
_CpuUtilTotalUsedTicks_Type = Integer32
_CpuUtilTotalUsedTicks_Object = MibTableColumn
cpuUtilTotalUsedTicks = _CpuUtilTotalUsedTicks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 7),
    _CpuUtilTotalUsedTicks_Type()
)
cpuUtilTotalUsedTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilTotalUsedTicks.setStatus("current")
_CpuUtilTotalTicks_Type = Integer32
_CpuUtilTotalTicks_Object = MibTableColumn
cpuUtilTotalTicks = _CpuUtilTotalTicks_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 8),
    _CpuUtilTotalTicks_Type()
)
cpuUtilTotalTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilTotalTicks.setStatus("current")
_CpuUtilTotalTimes_Type = Integer32
_CpuUtilTotalTimes_Object = MibTableColumn
cpuUtilTotalTimes = _CpuUtilTotalTimes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 9),
    _CpuUtilTotalTimes_Type()
)
cpuUtilTotalTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilTotalTimes.setStatus("current")
_CpuUtilCurrentUtil_Type = Integer32
_CpuUtilCurrentUtil_Object = MibTableColumn
cpuUtilCurrentUtil = _CpuUtilCurrentUtil_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 3, 5, 1, 10),
    _CpuUtilCurrentUtil_Type()
)
cpuUtilCurrentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilCurrentUtil.setStatus("current")
_SysTemperature_ObjectIdentity = ObjectIdentity
sysTemperature = _SysTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 4)
)
_SysCpuTemper_Type = Integer32
_SysCpuTemper_Object = MibScalar
sysCpuTemper = _SysCpuTemper_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 4, 1),
    _SysCpuTemper_Type()
)
sysCpuTemper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCpuTemper.setStatus("current")
_SysCpuAlertTemper_Type = Integer32
_SysCpuAlertTemper_Object = MibScalar
sysCpuAlertTemper = _SysCpuAlertTemper_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 4, 2),
    _SysCpuAlertTemper_Type()
)
sysCpuAlertTemper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCpuAlertTemper.setStatus("current")
_SysMainBoardTemper_Type = Integer32
_SysMainBoardTemper_Object = MibScalar
sysMainBoardTemper = _SysMainBoardTemper_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 4, 3),
    _SysMainBoardTemper_Type()
)
sysMainBoardTemper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMainBoardTemper.setStatus("current")
_SysMainBoardAlertTemper_Type = Integer32
_SysMainBoardAlertTemper_Object = MibScalar
sysMainBoardAlertTemper = _SysMainBoardAlertTemper_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 4, 4),
    _SysMainBoardAlertTemper_Type()
)
sysMainBoardAlertTemper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMainBoardAlertTemper.setStatus("current")
_SysAlertTrapInt_Type = Integer32
_SysAlertTrapInt_Object = MibScalar
sysAlertTrapInt = _SysAlertTrapInt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 4, 5),
    _SysAlertTrapInt_Type()
)
sysAlertTrapInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlertTrapInt.setStatus("current")
_SysNFI_ObjectIdentity = ObjectIdentity
sysNFI = _SysNFI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200)
)
_SysRtrGbl_ObjectIdentity = ObjectIdentity
sysRtrGbl = _SysRtrGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 1)
)
_SysRtrCtrl_Type = EnabledStatus
_SysRtrCtrl_Object = MibScalar
sysRtrCtrl = _SysRtrCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 1, 1),
    _SysRtrCtrl_Type()
)
sysRtrCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRtrCtrl.setStatus("current")
_SysRtrResponder_Type = TruthValue
_SysRtrResponder_Object = MibScalar
sysRtrResponder = _SysRtrResponder_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 1, 2),
    _SysRtrResponder_Type()
)
sysRtrResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRtrResponder.setStatus("current")
_SysRtrEntityMgt_ObjectIdentity = ObjectIdentity
sysRtrEntityMgt = _SysRtrEntityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2)
)
_SysRtrEntityTable_Object = MibTable
sysRtrEntityTable = _SysRtrEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100)
)
if mibBuilder.loadTexts:
    sysRtrEntityTable.setStatus("current")
_SysRtrEntityEntry_Object = MibTableRow
sysRtrEntityEntry = _SysRtrEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1)
)
sysRtrEntityEntry.setIndexNames(
    (0, "MPIOS-MIB", "rtrEntityId"),
)
if mibBuilder.loadTexts:
    sysRtrEntityEntry.setStatus("current")


class _RtrEntityId_Type(Integer32):
    """Custom type rtrEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RtrEntityId_Type.__name__ = "Integer32"
_RtrEntityId_Object = MibTableColumn
rtrEntityId = _RtrEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 1),
    _RtrEntityId_Type()
)
rtrEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrEntityId.setStatus("current")


class _RtrEntityName_Type(DisplayString):
    """Custom type rtrEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrEntityName_Type.__name__ = "DisplayString"
_RtrEntityName_Object = MibTableColumn
rtrEntityName = _RtrEntityName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 2),
    _RtrEntityName_Type()
)
rtrEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrEntityName.setStatus("current")


class _RtrEntityType_Type(Integer32):
    """Custom type rtrEntityType based on Integer32"""
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
        *(("flowStatistics", 3),
          ("icmpEcho", 1),
          ("jitter", 2),
          ("udpecho", 4))
    )


_RtrEntityType_Type.__name__ = "Integer32"
_RtrEntityType_Object = MibTableColumn
rtrEntityType = _RtrEntityType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 3),
    _RtrEntityType_Type()
)
rtrEntityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrEntityType.setStatus("current")


class _RtrEntityLogType_Type(Integer32):
    """Custom type rtrEntityLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_RtrEntityLogType_Type.__name__ = "Integer32"
_RtrEntityLogType_Object = MibTableColumn
rtrEntityLogType = _RtrEntityLogType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 4),
    _RtrEntityLogType_Type()
)
rtrEntityLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrEntityLogType.setStatus("current")


class _RtrEntityLogMaxSize_Type(Integer32):
    """Custom type rtrEntityLogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_RtrEntityLogMaxSize_Type.__name__ = "Integer32"
_RtrEntityLogMaxSize_Object = MibTableColumn
rtrEntityLogMaxSize = _RtrEntityLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 5),
    _RtrEntityLogMaxSize_Type()
)
rtrEntityLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrEntityLogMaxSize.setStatus("current")


class _RtrEntityLogFilter_Type(Integer32):
    """Custom type rtrEntityLogFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("error", 2),
          ("overThreshold", 3))
    )


_RtrEntityLogFilter_Type.__name__ = "Integer32"
_RtrEntityLogFilter_Object = MibTableColumn
rtrEntityLogFilter = _RtrEntityLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 6),
    _RtrEntityLogFilter_Type()
)
rtrEntityLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrEntityLogFilter.setStatus("current")


class _RtrEntityThreshold_Type(Integer32):
    """Custom type rtrEntityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtrEntityThreshold_Type.__name__ = "Integer32"
_RtrEntityThreshold_Object = MibTableColumn
rtrEntityThreshold = _RtrEntityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 7),
    _RtrEntityThreshold_Type()
)
rtrEntityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrEntityThreshold.setStatus("current")
_RtrEntityRowStatus_Type = RowStatus
_RtrEntityRowStatus_Object = MibTableColumn
rtrEntityRowStatus = _RtrEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 2, 100, 1, 8),
    _RtrEntityRowStatus_Type()
)
rtrEntityRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrEntityRowStatus.setStatus("current")
_SysRtrGroupMgt_ObjectIdentity = ObjectIdentity
sysRtrGroupMgt = _SysRtrGroupMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3)
)
_SysRtrGroupTable_Object = MibTable
sysRtrGroupTable = _SysRtrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3, 100)
)
if mibBuilder.loadTexts:
    sysRtrGroupTable.setStatus("current")
_SysRtrGroupEntry_Object = MibTableRow
sysRtrGroupEntry = _SysRtrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3, 100, 1)
)
sysRtrGroupEntry.setIndexNames(
    (0, "MPIOS-MIB", "rtrGroupId"),
)
if mibBuilder.loadTexts:
    sysRtrGroupEntry.setStatus("current")


class _RtrGroupId_Type(Integer32):
    """Custom type rtrGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RtrGroupId_Type.__name__ = "Integer32"
_RtrGroupId_Object = MibTableColumn
rtrGroupId = _RtrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3, 100, 1, 1),
    _RtrGroupId_Type()
)
rtrGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrGroupId.setStatus("current")


class _RtrGroupName_Type(DisplayString):
    """Custom type rtrGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrGroupName_Type.__name__ = "DisplayString"
_RtrGroupName_Object = MibTableColumn
rtrGroupName = _RtrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3, 100, 1, 2),
    _RtrGroupName_Type()
)
rtrGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrGroupName.setStatus("current")


class _RtrGroupInterval_Type(Integer32):
    """Custom type rtrGroupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RtrGroupInterval_Type.__name__ = "Integer32"
_RtrGroupInterval_Object = MibTableColumn
rtrGroupInterval = _RtrGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3, 100, 1, 3),
    _RtrGroupInterval_Type()
)
rtrGroupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrGroupInterval.setStatus("current")


class _RtrGroupEntityMembers_Type(DisplayString):
    """Custom type rtrGroupEntityMembers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RtrGroupEntityMembers_Type.__name__ = "DisplayString"
_RtrGroupEntityMembers_Object = MibTableColumn
rtrGroupEntityMembers = _RtrGroupEntityMembers_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3, 100, 1, 4),
    _RtrGroupEntityMembers_Type()
)
rtrGroupEntityMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrGroupEntityMembers.setStatus("current")
_RtrGroupRowStatus_Type = RowStatus
_RtrGroupRowStatus_Object = MibTableColumn
rtrGroupRowStatus = _RtrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 3, 100, 1, 5),
    _RtrGroupRowStatus_Type()
)
rtrGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrGroupRowStatus.setStatus("current")
_SysRtrScheduleMgt_ObjectIdentity = ObjectIdentity
sysRtrScheduleMgt = _SysRtrScheduleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4)
)
_SysRtrScheduleTable_Object = MibTable
sysRtrScheduleTable = _SysRtrScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100)
)
if mibBuilder.loadTexts:
    sysRtrScheduleTable.setStatus("current")
_SysRtrScheduleEntry_Object = MibTableRow
sysRtrScheduleEntry = _SysRtrScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1)
)
sysRtrScheduleEntry.setIndexNames(
    (0, "MPIOS-MIB", "rtrScheduleId"),
)
if mibBuilder.loadTexts:
    sysRtrScheduleEntry.setStatus("current")
_RtrScheduleId_Type = Unsigned32
_RtrScheduleId_Object = MibTableColumn
rtrScheduleId = _RtrScheduleId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 1),
    _RtrScheduleId_Type()
)
rtrScheduleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleId.setStatus("current")


class _RtrScheduleType_Type(Integer32):
    """Custom type rtrScheduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("entity", 1),
          ("group", 2))
    )


_RtrScheduleType_Type.__name__ = "Integer32"
_RtrScheduleType_Object = MibTableColumn
rtrScheduleType = _RtrScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 2),
    _RtrScheduleType_Type()
)
rtrScheduleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleType.setStatus("current")


class _RtrScheduleObjId_Type(Integer32):
    """Custom type rtrScheduleObjId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RtrScheduleObjId_Type.__name__ = "Integer32"
_RtrScheduleObjId_Object = MibTableColumn
rtrScheduleObjId = _RtrScheduleObjId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 3),
    _RtrScheduleObjId_Type()
)
rtrScheduleObjId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleObjId.setStatus("current")


class _RtrScheduleStartTimeFlag_Type(Integer32):
    """Custom type rtrScheduleStartTimeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("afterTime", 2),
          ("startNow", 1),
          ("startTime", 3))
    )


_RtrScheduleStartTimeFlag_Type.__name__ = "Integer32"
_RtrScheduleStartTimeFlag_Object = MibTableColumn
rtrScheduleStartTimeFlag = _RtrScheduleStartTimeFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 4),
    _RtrScheduleStartTimeFlag_Type()
)
rtrScheduleStartTimeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleStartTimeFlag.setStatus("current")


class _RtrScheduleAfterTime_Type(DisplayString):
    """Custom type rtrScheduleAfterTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RtrScheduleAfterTime_Type.__name__ = "DisplayString"
_RtrScheduleAfterTime_Object = MibTableColumn
rtrScheduleAfterTime = _RtrScheduleAfterTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 5),
    _RtrScheduleAfterTime_Type()
)
rtrScheduleAfterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleAfterTime.setStatus("current")


class _RtrScheduleStartTime_Type(DisplayString):
    """Custom type rtrScheduleStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrScheduleStartTime_Type.__name__ = "DisplayString"
_RtrScheduleStartTime_Object = MibTableColumn
rtrScheduleStartTime = _RtrScheduleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 6),
    _RtrScheduleStartTime_Type()
)
rtrScheduleStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleStartTime.setStatus("current")


class _RtrScheduleAgeOut_Type(Unsigned32):
    """Custom type rtrScheduleAgeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2073600),
    )


_RtrScheduleAgeOut_Type.__name__ = "Unsigned32"
_RtrScheduleAgeOut_Object = MibTableColumn
rtrScheduleAgeOut = _RtrScheduleAgeOut_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 7),
    _RtrScheduleAgeOut_Type()
)
rtrScheduleAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleAgeOut.setStatus("current")


class _RtrScheduleLifeFlag_Type(Integer32):
    """Custom type rtrScheduleLifeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forever", 1),
          ("repeatAndDie", 2))
    )


_RtrScheduleLifeFlag_Type.__name__ = "Integer32"
_RtrScheduleLifeFlag_Object = MibTableColumn
rtrScheduleLifeFlag = _RtrScheduleLifeFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 8),
    _RtrScheduleLifeFlag_Type()
)
rtrScheduleLifeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleLifeFlag.setStatus("current")


class _RtrScheduleLifeTime_Type(Unsigned32):
    """Custom type rtrScheduleLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtrScheduleLifeTime_Type.__name__ = "Unsigned32"
_RtrScheduleLifeTime_Object = MibTableColumn
rtrScheduleLifeTime = _RtrScheduleLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 9),
    _RtrScheduleLifeTime_Type()
)
rtrScheduleLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleLifeTime.setStatus("current")


class _RtrScheduleRepeat_Type(Unsigned32):
    """Custom type rtrScheduleRepeat based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtrScheduleRepeat_Type.__name__ = "Unsigned32"
_RtrScheduleRepeat_Object = MibTableColumn
rtrScheduleRepeat = _RtrScheduleRepeat_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 10),
    _RtrScheduleRepeat_Type()
)
rtrScheduleRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleRepeat.setStatus("current")


class _RtrScheduleInterval_Type(Unsigned32):
    """Custom type rtrScheduleInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtrScheduleInterval_Type.__name__ = "Unsigned32"
_RtrScheduleInterval_Object = MibTableColumn
rtrScheduleInterval = _RtrScheduleInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 11),
    _RtrScheduleInterval_Type()
)
rtrScheduleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrScheduleInterval.setStatus("current")
_RtrScheduleRowStatus_Type = RowStatus
_RtrScheduleRowStatus_Object = MibTableColumn
rtrScheduleRowStatus = _RtrScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 4, 100, 1, 12),
    _RtrScheduleRowStatus_Type()
)
rtrScheduleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrScheduleRowStatus.setStatus("current")
_SysRtrIcmpEchoMgt_ObjectIdentity = ObjectIdentity
sysRtrIcmpEchoMgt = _SysRtrIcmpEchoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5)
)
_SysRtrIcmpEchoTable_Object = MibTable
sysRtrIcmpEchoTable = _SysRtrIcmpEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100)
)
if mibBuilder.loadTexts:
    sysRtrIcmpEchoTable.setStatus("current")
_SysRtrIcmpEchoEntry_Object = MibTableRow
sysRtrIcmpEchoEntry = _SysRtrIcmpEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1)
)
sysRtrIcmpEchoEntry.setIndexNames(
    (0, "MPIOS-MIB", "rtrIcmpEchoEntityId"),
)
if mibBuilder.loadTexts:
    sysRtrIcmpEchoEntry.setStatus("current")


class _RtrIcmpEchoEntityId_Type(Integer32):
    """Custom type rtrIcmpEchoEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RtrIcmpEchoEntityId_Type.__name__ = "Integer32"
_RtrIcmpEchoEntityId_Object = MibTableColumn
rtrIcmpEchoEntityId = _RtrIcmpEchoEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 1),
    _RtrIcmpEchoEntityId_Type()
)
rtrIcmpEchoEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoEntityId.setStatus("current")
_RtrIcmpEchoTargetIp_Type = IpAddress
_RtrIcmpEchoTargetIp_Object = MibTableColumn
rtrIcmpEchoTargetIp = _RtrIcmpEchoTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 2),
    _RtrIcmpEchoTargetIp_Type()
)
rtrIcmpEchoTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoTargetIp.setStatus("current")


class _RtrIcmpEchoPktNum_Type(Unsigned32):
    """Custom type rtrIcmpEchoPktNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_RtrIcmpEchoPktNum_Type.__name__ = "Unsigned32"
_RtrIcmpEchoPktNum_Object = MibTableColumn
rtrIcmpEchoPktNum = _RtrIcmpEchoPktNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 3),
    _RtrIcmpEchoPktNum_Type()
)
rtrIcmpEchoPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoPktNum.setStatus("current")


class _RtrIcmpEchoPktLen_Type(Integer32):
    """Custom type rtrIcmpEchoPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36, 18024),
    )


_RtrIcmpEchoPktLen_Type.__name__ = "Integer32"
_RtrIcmpEchoPktLen_Object = MibTableColumn
rtrIcmpEchoPktLen = _RtrIcmpEchoPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 4),
    _RtrIcmpEchoPktLen_Type()
)
rtrIcmpEchoPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoPktLen.setStatus("current")


class _RtrIcmpEchoTimeout_Type(Integer32):
    """Custom type rtrIcmpEchoTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RtrIcmpEchoTimeout_Type.__name__ = "Integer32"
_RtrIcmpEchoTimeout_Object = MibTableColumn
rtrIcmpEchoTimeout = _RtrIcmpEchoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 5),
    _RtrIcmpEchoTimeout_Type()
)
rtrIcmpEchoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoTimeout.setStatus("current")


class _RtrIcmpEchoSchInterval_Type(Unsigned32):
    """Custom type rtrIcmpEchoSchInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtrIcmpEchoSchInterval_Type.__name__ = "Unsigned32"
_RtrIcmpEchoSchInterval_Object = MibTableColumn
rtrIcmpEchoSchInterval = _RtrIcmpEchoSchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 6),
    _RtrIcmpEchoSchInterval_Type()
)
rtrIcmpEchoSchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoSchInterval.setStatus("current")
_RtrIcmpEchoExtendFlag_Type = TruthValue
_RtrIcmpEchoExtendFlag_Object = MibTableColumn
rtrIcmpEchoExtendFlag = _RtrIcmpEchoExtendFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 7),
    _RtrIcmpEchoExtendFlag_Type()
)
rtrIcmpEchoExtendFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoExtendFlag.setStatus("current")


class _RtrIcmpEchoVrfName_Type(DisplayString):
    """Custom type rtrIcmpEchoVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrIcmpEchoVrfName_Type.__name__ = "DisplayString"
_RtrIcmpEchoVrfName_Object = MibTableColumn
rtrIcmpEchoVrfName = _RtrIcmpEchoVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 8),
    _RtrIcmpEchoVrfName_Type()
)
rtrIcmpEchoVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoVrfName.setStatus("current")
_RtrIcmpEchoSourceIp_Type = IpAddress
_RtrIcmpEchoSourceIp_Object = MibTableColumn
rtrIcmpEchoSourceIp = _RtrIcmpEchoSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 9),
    _RtrIcmpEchoSourceIp_Type()
)
rtrIcmpEchoSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoSourceIp.setStatus("current")


class _RtrIcmpEchoTos_Type(Integer32):
    """Custom type rtrIcmpEchoTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtrIcmpEchoTos_Type.__name__ = "Integer32"
_RtrIcmpEchoTos_Object = MibTableColumn
rtrIcmpEchoTos = _RtrIcmpEchoTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 10),
    _RtrIcmpEchoTos_Type()
)
rtrIcmpEchoTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoTos.setStatus("current")
_RtrIcmpEchoSetDf_Type = TruthValue
_RtrIcmpEchoSetDf_Object = MibTableColumn
rtrIcmpEchoSetDf = _RtrIcmpEchoSetDf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 11),
    _RtrIcmpEchoSetDf_Type()
)
rtrIcmpEchoSetDf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoSetDf.setStatus("current")
_RtrIcmpEchoVerifyData_Type = TruthValue
_RtrIcmpEchoVerifyData_Object = MibTableColumn
rtrIcmpEchoVerifyData = _RtrIcmpEchoVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 12),
    _RtrIcmpEchoVerifyData_Type()
)
rtrIcmpEchoVerifyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoVerifyData.setStatus("current")
_RtrIcmpEchoIsScheduling_Type = TruthValue
_RtrIcmpEchoIsScheduling_Object = MibTableColumn
rtrIcmpEchoIsScheduling = _RtrIcmpEchoIsScheduling_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 13),
    _RtrIcmpEchoIsScheduling_Type()
)
rtrIcmpEchoIsScheduling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIcmpEchoIsScheduling.setStatus("current")
_RtrIcmpEchoPktTotalSend_Type = Counter32
_RtrIcmpEchoPktTotalSend_Object = MibTableColumn
rtrIcmpEchoPktTotalSend = _RtrIcmpEchoPktTotalSend_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 14),
    _RtrIcmpEchoPktTotalSend_Type()
)
rtrIcmpEchoPktTotalSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIcmpEchoPktTotalSend.setStatus("current")
_RtrIcmpEchoPktTotalRcvd_Type = Counter32
_RtrIcmpEchoPktTotalRcvd_Object = MibTableColumn
rtrIcmpEchoPktTotalRcvd = _RtrIcmpEchoPktTotalRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 15),
    _RtrIcmpEchoPktTotalRcvd_Type()
)
rtrIcmpEchoPktTotalRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIcmpEchoPktTotalRcvd.setStatus("current")


class _RtrIcmpEchoSuccessRate_Type(Integer32):
    """Custom type rtrIcmpEchoSuccessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtrIcmpEchoSuccessRate_Type.__name__ = "Integer32"
_RtrIcmpEchoSuccessRate_Object = MibTableColumn
rtrIcmpEchoSuccessRate = _RtrIcmpEchoSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 16),
    _RtrIcmpEchoSuccessRate_Type()
)
rtrIcmpEchoSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrIcmpEchoSuccessRate.setStatus("current")
_RtrIcmpEchoRowStatus_Type = RowStatus
_RtrIcmpEchoRowStatus_Object = MibTableColumn
rtrIcmpEchoRowStatus = _RtrIcmpEchoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 5, 100, 1, 17),
    _RtrIcmpEchoRowStatus_Type()
)
rtrIcmpEchoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrIcmpEchoRowStatus.setStatus("current")
_SysRtrJitterMgt_ObjectIdentity = ObjectIdentity
sysRtrJitterMgt = _SysRtrJitterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6)
)
_SysRtrJitterTable_Object = MibTable
sysRtrJitterTable = _SysRtrJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100)
)
if mibBuilder.loadTexts:
    sysRtrJitterTable.setStatus("current")
_SysRtrJitterEntry_Object = MibTableRow
sysRtrJitterEntry = _SysRtrJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1)
)
sysRtrJitterEntry.setIndexNames(
    (0, "MPIOS-MIB", "rtrJitterEntityId"),
)
if mibBuilder.loadTexts:
    sysRtrJitterEntry.setStatus("current")


class _RtrJitterEntityId_Type(Integer32):
    """Custom type rtrJitterEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RtrJitterEntityId_Type.__name__ = "Integer32"
_RtrJitterEntityId_Object = MibTableColumn
rtrJitterEntityId = _RtrJitterEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 1),
    _RtrJitterEntityId_Type()
)
rtrJitterEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterEntityId.setStatus("current")


class _RtrJitterState_Type(Integer32):
    """Custom type rtrJitterState based on Integer32"""
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
        *(("closed", 2),
          ("finished", 5),
          ("init", 1),
          ("request", 3),
          ("transmit", 4))
    )


_RtrJitterState_Type.__name__ = "Integer32"
_RtrJitterState_Object = MibTableColumn
rtrJitterState = _RtrJitterState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 2),
    _RtrJitterState_Type()
)
rtrJitterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterState.setStatus("current")
_RtrJitterTargetIp_Type = IpAddress
_RtrJitterTargetIp_Object = MibTableColumn
rtrJitterTargetIp = _RtrJitterTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 3),
    _RtrJitterTargetIp_Type()
)
rtrJitterTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterTargetIp.setStatus("current")


class _RtrJitterTargetPort_Type(Unsigned32):
    """Custom type rtrJitterTargetPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtrJitterTargetPort_Type.__name__ = "Unsigned32"
_RtrJitterTargetPort_Object = MibTableColumn
rtrJitterTargetPort = _RtrJitterTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 4),
    _RtrJitterTargetPort_Type()
)
rtrJitterTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterTargetPort.setStatus("current")


class _RtrJitterCodec_Type(Integer32):
    """Custom type rtrJitterCodec based on Integer32"""
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
        *(("g711ALAW", 2),
          ("g711MULAW", 1),
          ("g729A", 3),
          ("invalid", 5),
          ("userDefined", 4))
    )


_RtrJitterCodec_Type.__name__ = "Integer32"
_RtrJitterCodec_Object = MibTableColumn
rtrJitterCodec = _RtrJitterCodec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 5),
    _RtrJitterCodec_Type()
)
rtrJitterCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterCodec.setStatus("current")


class _RtrJitterPktLen_Type(Integer32):
    """Custom type rtrJitterPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1500),
    )


_RtrJitterPktLen_Type.__name__ = "Integer32"
_RtrJitterPktLen_Object = MibTableColumn
rtrJitterPktLen = _RtrJitterPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 6),
    _RtrJitterPktLen_Type()
)
rtrJitterPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterPktLen.setStatus("current")


class _RtrJitterPktNum_Type(Integer32):
    """Custom type rtrJitterPktNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_RtrJitterPktNum_Type.__name__ = "Integer32"
_RtrJitterPktNum_Object = MibTableColumn
rtrJitterPktNum = _RtrJitterPktNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 7),
    _RtrJitterPktNum_Type()
)
rtrJitterPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterPktNum.setStatus("current")


class _RtrJitterPktInterval_Type(Integer32):
    """Custom type rtrJitterPktInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 6000),
    )


_RtrJitterPktInterval_Type.__name__ = "Integer32"
_RtrJitterPktInterval_Object = MibTableColumn
rtrJitterPktInterval = _RtrJitterPktInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 8),
    _RtrJitterPktInterval_Type()
)
rtrJitterPktInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterPktInterval.setStatus("current")


class _RtrJitterSchInterval_Type(Unsigned32):
    """Custom type rtrJitterSchInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtrJitterSchInterval_Type.__name__ = "Unsigned32"
_RtrJitterSchInterval_Object = MibTableColumn
rtrJitterSchInterval = _RtrJitterSchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 9),
    _RtrJitterSchInterval_Type()
)
rtrJitterSchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterSchInterval.setStatus("current")
_RtrJitterSourceIp_Type = IpAddress
_RtrJitterSourceIp_Object = MibTableColumn
rtrJitterSourceIp = _RtrJitterSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 10),
    _RtrJitterSourceIp_Type()
)
rtrJitterSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterSourceIp.setStatus("current")


class _RtrJitterSourcePort_Type(Unsigned32):
    """Custom type rtrJitterSourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtrJitterSourcePort_Type.__name__ = "Unsigned32"
_RtrJitterSourcePort_Object = MibTableColumn
rtrJitterSourcePort = _RtrJitterSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 11),
    _RtrJitterSourcePort_Type()
)
rtrJitterSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterSourcePort.setStatus("current")


class _RtrJitterTimeout_Type(Unsigned32):
    """Custom type rtrJitterTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_RtrJitterTimeout_Type.__name__ = "Unsigned32"
_RtrJitterTimeout_Object = MibTableColumn
rtrJitterTimeout = _RtrJitterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 12),
    _RtrJitterTimeout_Type()
)
rtrJitterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterTimeout.setStatus("current")


class _RtrJitterVrfName_Type(DisplayString):
    """Custom type rtrJitterVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrJitterVrfName_Type.__name__ = "DisplayString"
_RtrJitterVrfName_Object = MibTableColumn
rtrJitterVrfName = _RtrJitterVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 13),
    _RtrJitterVrfName_Type()
)
rtrJitterVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterVrfName.setStatus("current")


class _RtrJitterTos_Type(Integer32):
    """Custom type rtrJitterTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtrJitterTos_Type.__name__ = "Integer32"
_RtrJitterTos_Object = MibTableColumn
rtrJitterTos = _RtrJitterTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 14),
    _RtrJitterTos_Type()
)
rtrJitterTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterTos.setStatus("current")
_RtrJitterMinRtt_Type = Integer32
_RtrJitterMinRtt_Object = MibTableColumn
rtrJitterMinRtt = _RtrJitterMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 15),
    _RtrJitterMinRtt_Type()
)
rtrJitterMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterMinRtt.setStatus("current")
_RtrJitterMaxRtt_Type = Integer32
_RtrJitterMaxRtt_Object = MibTableColumn
rtrJitterMaxRtt = _RtrJitterMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 16),
    _RtrJitterMaxRtt_Type()
)
rtrJitterMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterMaxRtt.setStatus("current")
_RtrJitterPktLossSd_Type = Integer32
_RtrJitterPktLossSd_Object = MibTableColumn
rtrJitterPktLossSd = _RtrJitterPktLossSd_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 17),
    _RtrJitterPktLossSd_Type()
)
rtrJitterPktLossSd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterPktLossSd.setStatus("current")
_RtrJitterPktLossDs_Type = Integer32
_RtrJitterPktLossDs_Object = MibTableColumn
rtrJitterPktLossDs = _RtrJitterPktLossDs_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 18),
    _RtrJitterPktLossDs_Type()
)
rtrJitterPktLossDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterPktLossDs.setStatus("current")
_RtrJitterDsMin_Type = Integer32
_RtrJitterDsMin_Object = MibTableColumn
rtrJitterDsMin = _RtrJitterDsMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 19),
    _RtrJitterDsMin_Type()
)
rtrJitterDsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterDsMin.setStatus("current")
_RtrJitterDsMax_Type = Integer32
_RtrJitterDsMax_Object = MibTableColumn
rtrJitterDsMax = _RtrJitterDsMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 20),
    _RtrJitterDsMax_Type()
)
rtrJitterDsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterDsMax.setStatus("current")
_RtrJitterSdMin_Type = Integer32
_RtrJitterSdMin_Object = MibTableColumn
rtrJitterSdMin = _RtrJitterSdMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 21),
    _RtrJitterSdMin_Type()
)
rtrJitterSdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterSdMin.setStatus("current")
_RtrJitterSdMax_Type = Integer32
_RtrJitterSdMax_Object = MibTableColumn
rtrJitterSdMax = _RtrJitterSdMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 22),
    _RtrJitterSdMax_Type()
)
rtrJitterSdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterSdMax.setStatus("current")
_RtrJitterDelayDsMin_Type = Integer32
_RtrJitterDelayDsMin_Object = MibTableColumn
rtrJitterDelayDsMin = _RtrJitterDelayDsMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 23),
    _RtrJitterDelayDsMin_Type()
)
rtrJitterDelayDsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterDelayDsMin.setStatus("current")
_RtrJitterDelayDsMax_Type = Integer32
_RtrJitterDelayDsMax_Object = MibTableColumn
rtrJitterDelayDsMax = _RtrJitterDelayDsMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 24),
    _RtrJitterDelayDsMax_Type()
)
rtrJitterDelayDsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterDelayDsMax.setStatus("current")
_RtrJitterDelaySdMin_Type = Integer32
_RtrJitterDelaySdMin_Object = MibTableColumn
rtrJitterDelaySdMin = _RtrJitterDelaySdMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 25),
    _RtrJitterDelaySdMin_Type()
)
rtrJitterDelaySdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterDelaySdMin.setStatus("current")
_RtrJitterDelaySdMax_Type = Integer32
_RtrJitterDelaySdMax_Object = MibTableColumn
rtrJitterDelaySdMax = _RtrJitterDelaySdMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 26),
    _RtrJitterDelaySdMax_Type()
)
rtrJitterDelaySdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterDelaySdMax.setStatus("current")


class _RtrJitterIcpifMin_Type(DisplayString):
    """Custom type rtrJitterIcpifMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrJitterIcpifMin_Type.__name__ = "DisplayString"
_RtrJitterIcpifMin_Object = MibTableColumn
rtrJitterIcpifMin = _RtrJitterIcpifMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 27),
    _RtrJitterIcpifMin_Type()
)
rtrJitterIcpifMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterIcpifMin.setStatus("current")


class _RtrJitterIcpifMax_Type(DisplayString):
    """Custom type rtrJitterIcpifMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrJitterIcpifMax_Type.__name__ = "DisplayString"
_RtrJitterIcpifMax_Object = MibTableColumn
rtrJitterIcpifMax = _RtrJitterIcpifMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 28),
    _RtrJitterIcpifMax_Type()
)
rtrJitterIcpifMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterIcpifMax.setStatus("current")


class _RtrJitterMosMin_Type(DisplayString):
    """Custom type rtrJitterMosMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrJitterMosMin_Type.__name__ = "DisplayString"
_RtrJitterMosMin_Object = MibTableColumn
rtrJitterMosMin = _RtrJitterMosMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 29),
    _RtrJitterMosMin_Type()
)
rtrJitterMosMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterMosMin.setStatus("current")


class _RtrJitterMosMax_Type(DisplayString):
    """Custom type rtrJitterMosMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrJitterMosMax_Type.__name__ = "DisplayString"
_RtrJitterMosMax_Object = MibTableColumn
rtrJitterMosMax = _RtrJitterMosMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 30),
    _RtrJitterMosMax_Type()
)
rtrJitterMosMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrJitterMosMax.setStatus("current")
_RtrJitterRowStatus_Type = RowStatus
_RtrJitterRowStatus_Object = MibTableColumn
rtrJitterRowStatus = _RtrJitterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 6, 100, 1, 31),
    _RtrJitterRowStatus_Type()
)
rtrJitterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrJitterRowStatus.setStatus("current")
_SysRtrFlowStatisticsMgt_ObjectIdentity = ObjectIdentity
sysRtrFlowStatisticsMgt = _SysRtrFlowStatisticsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7)
)
_SysRtrFlowStatisticsTable_Object = MibTable
sysRtrFlowStatisticsTable = _SysRtrFlowStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100)
)
if mibBuilder.loadTexts:
    sysRtrFlowStatisticsTable.setStatus("current")
_SysRtrFlowStatisticsEntry_Object = MibTableRow
sysRtrFlowStatisticsEntry = _SysRtrFlowStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1)
)
sysRtrFlowStatisticsEntry.setIndexNames(
    (0, "MPIOS-MIB", "rtrFlStatisticsEntityId"),
)
if mibBuilder.loadTexts:
    sysRtrFlowStatisticsEntry.setStatus("current")


class _RtrFlStatisticsEntityId_Type(Integer32):
    """Custom type rtrFlStatisticsEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RtrFlStatisticsEntityId_Type.__name__ = "Integer32"
_RtrFlStatisticsEntityId_Object = MibTableColumn
rtrFlStatisticsEntityId = _RtrFlStatisticsEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 1),
    _RtrFlStatisticsEntityId_Type()
)
rtrFlStatisticsEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFlStatisticsEntityId.setStatus("current")


class _RtrFlStatisticsIfName_Type(DisplayString):
    """Custom type rtrFlStatisticsIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStatisticsIfName_Type.__name__ = "DisplayString"
_RtrFlStatisticsIfName_Object = MibTableColumn
rtrFlStatisticsIfName = _RtrFlStatisticsIfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 2),
    _RtrFlStatisticsIfName_Type()
)
rtrFlStatisticsIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFlStatisticsIfName.setStatus("current")


class _RtrFlStatisticsInterval_Type(Integer32):
    """Custom type rtrFlStatisticsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_RtrFlStatisticsInterval_Type.__name__ = "Integer32"
_RtrFlStatisticsInterval_Object = MibTableColumn
rtrFlStatisticsInterval = _RtrFlStatisticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 3),
    _RtrFlStatisticsInterval_Type()
)
rtrFlStatisticsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFlStatisticsInterval.setStatus("current")
_RtrFlStaInputMaxPkts_Type = Counter64
_RtrFlStaInputMaxPkts_Object = MibTableColumn
rtrFlStaInputMaxPkts = _RtrFlStaInputMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 4),
    _RtrFlStaInputMaxPkts_Type()
)
rtrFlStaInputMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaInputMaxPkts.setStatus("current")


class _RtrFlStaTmInputMaxPkts_Type(DisplayString):
    """Custom type rtrFlStaTmInputMaxPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmInputMaxPkts_Type.__name__ = "DisplayString"
_RtrFlStaTmInputMaxPkts_Object = MibTableColumn
rtrFlStaTmInputMaxPkts = _RtrFlStaTmInputMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 5),
    _RtrFlStaTmInputMaxPkts_Type()
)
rtrFlStaTmInputMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmInputMaxPkts.setStatus("current")
_RtrFlStaInputMaxFlow_Type = Counter64
_RtrFlStaInputMaxFlow_Object = MibTableColumn
rtrFlStaInputMaxFlow = _RtrFlStaInputMaxFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 6),
    _RtrFlStaInputMaxFlow_Type()
)
rtrFlStaInputMaxFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaInputMaxFlow.setStatus("current")


class _RtrFlStaTmInputMaxFlow_Type(DisplayString):
    """Custom type rtrFlStaTmInputMaxFlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmInputMaxFlow_Type.__name__ = "DisplayString"
_RtrFlStaTmInputMaxFlow_Object = MibTableColumn
rtrFlStaTmInputMaxFlow = _RtrFlStaTmInputMaxFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 7),
    _RtrFlStaTmInputMaxFlow_Type()
)
rtrFlStaTmInputMaxFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmInputMaxFlow.setStatus("current")
_RtrFlStaInputMinPkts_Type = Counter64
_RtrFlStaInputMinPkts_Object = MibTableColumn
rtrFlStaInputMinPkts = _RtrFlStaInputMinPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 8),
    _RtrFlStaInputMinPkts_Type()
)
rtrFlStaInputMinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaInputMinPkts.setStatus("current")


class _RtrFlStaTmInputMinPkts_Type(DisplayString):
    """Custom type rtrFlStaTmInputMinPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmInputMinPkts_Type.__name__ = "DisplayString"
_RtrFlStaTmInputMinPkts_Object = MibTableColumn
rtrFlStaTmInputMinPkts = _RtrFlStaTmInputMinPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 9),
    _RtrFlStaTmInputMinPkts_Type()
)
rtrFlStaTmInputMinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmInputMinPkts.setStatus("current")
_RtrFlStaInputMinFlow_Type = Counter64
_RtrFlStaInputMinFlow_Object = MibTableColumn
rtrFlStaInputMinFlow = _RtrFlStaInputMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 10),
    _RtrFlStaInputMinFlow_Type()
)
rtrFlStaInputMinFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaInputMinFlow.setStatus("current")


class _RtrFlStaTmInputMinFlow_Type(DisplayString):
    """Custom type rtrFlStaTmInputMinFlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmInputMinFlow_Type.__name__ = "DisplayString"
_RtrFlStaTmInputMinFlow_Object = MibTableColumn
rtrFlStaTmInputMinFlow = _RtrFlStaTmInputMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 11),
    _RtrFlStaTmInputMinFlow_Type()
)
rtrFlStaTmInputMinFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmInputMinFlow.setStatus("current")
_RtrFlStaOutputMaxPkts_Type = Counter64
_RtrFlStaOutputMaxPkts_Object = MibTableColumn
rtrFlStaOutputMaxPkts = _RtrFlStaOutputMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 12),
    _RtrFlStaOutputMaxPkts_Type()
)
rtrFlStaOutputMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaOutputMaxPkts.setStatus("current")


class _RtrFlStaTmOutputMaxPkts_Type(DisplayString):
    """Custom type rtrFlStaTmOutputMaxPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmOutputMaxPkts_Type.__name__ = "DisplayString"
_RtrFlStaTmOutputMaxPkts_Object = MibTableColumn
rtrFlStaTmOutputMaxPkts = _RtrFlStaTmOutputMaxPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 13),
    _RtrFlStaTmOutputMaxPkts_Type()
)
rtrFlStaTmOutputMaxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmOutputMaxPkts.setStatus("current")
_RtrFlStaOutputMaxFlow_Type = Counter64
_RtrFlStaOutputMaxFlow_Object = MibTableColumn
rtrFlStaOutputMaxFlow = _RtrFlStaOutputMaxFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 14),
    _RtrFlStaOutputMaxFlow_Type()
)
rtrFlStaOutputMaxFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaOutputMaxFlow.setStatus("current")


class _RtrFlStaTmOutputMaxFlow_Type(DisplayString):
    """Custom type rtrFlStaTmOutputMaxFlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmOutputMaxFlow_Type.__name__ = "DisplayString"
_RtrFlStaTmOutputMaxFlow_Object = MibTableColumn
rtrFlStaTmOutputMaxFlow = _RtrFlStaTmOutputMaxFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 15),
    _RtrFlStaTmOutputMaxFlow_Type()
)
rtrFlStaTmOutputMaxFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmOutputMaxFlow.setStatus("current")
_RtrFlStaOutputMinPkts_Type = Counter64
_RtrFlStaOutputMinPkts_Object = MibTableColumn
rtrFlStaOutputMinPkts = _RtrFlStaOutputMinPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 16),
    _RtrFlStaOutputMinPkts_Type()
)
rtrFlStaOutputMinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaOutputMinPkts.setStatus("current")


class _RtrFlStaTmOutputMinPkts_Type(DisplayString):
    """Custom type rtrFlStaTmOutputMinPkts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmOutputMinPkts_Type.__name__ = "DisplayString"
_RtrFlStaTmOutputMinPkts_Object = MibTableColumn
rtrFlStaTmOutputMinPkts = _RtrFlStaTmOutputMinPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 17),
    _RtrFlStaTmOutputMinPkts_Type()
)
rtrFlStaTmOutputMinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmOutputMinPkts.setStatus("current")
_RtrFlStaOutputMinFlow_Type = Counter64
_RtrFlStaOutputMinFlow_Object = MibTableColumn
rtrFlStaOutputMinFlow = _RtrFlStaOutputMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 18),
    _RtrFlStaOutputMinFlow_Type()
)
rtrFlStaOutputMinFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaOutputMinFlow.setStatus("current")


class _RtrFlStaTmOutputMinFlow_Type(DisplayString):
    """Custom type rtrFlStaTmOutputMinFlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrFlStaTmOutputMinFlow_Type.__name__ = "DisplayString"
_RtrFlStaTmOutputMinFlow_Object = MibTableColumn
rtrFlStaTmOutputMinFlow = _RtrFlStaTmOutputMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 19),
    _RtrFlStaTmOutputMinFlow_Type()
)
rtrFlStaTmOutputMinFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrFlStaTmOutputMinFlow.setStatus("current")
_RtrFlowStatisticsRowStatus_Type = RowStatus
_RtrFlowStatisticsRowStatus_Object = MibTableColumn
rtrFlowStatisticsRowStatus = _RtrFlowStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 7, 100, 1, 20),
    _RtrFlowStatisticsRowStatus_Type()
)
rtrFlowStatisticsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrFlowStatisticsRowStatus.setStatus("current")
_SysRtrUdpechoMgt_ObjectIdentity = ObjectIdentity
sysRtrUdpechoMgt = _SysRtrUdpechoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8)
)
_SysRtrUdpechoTable_Object = MibTable
sysRtrUdpechoTable = _SysRtrUdpechoTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100)
)
if mibBuilder.loadTexts:
    sysRtrUdpechoTable.setStatus("current")
_SysRtrUdpechoEntry_Object = MibTableRow
sysRtrUdpechoEntry = _SysRtrUdpechoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1)
)
sysRtrUdpechoEntry.setIndexNames(
    (0, "MPIOS-MIB", "rtrUdpechoEntityId"),
)
if mibBuilder.loadTexts:
    sysRtrUdpechoEntry.setStatus("current")


class _RtrUdpechoEntityId_Type(Integer32):
    """Custom type rtrUdpechoEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_RtrUdpechoEntityId_Type.__name__ = "Integer32"
_RtrUdpechoEntityId_Object = MibTableColumn
rtrUdpechoEntityId = _RtrUdpechoEntityId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 1),
    _RtrUdpechoEntityId_Type()
)
rtrUdpechoEntityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoEntityId.setStatus("current")


class _RtrUdpechoState_Type(Integer32):
    """Custom type rtrUdpechoState based on Integer32"""
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
        *(("closed", 2),
          ("finished", 5),
          ("init", 1),
          ("request", 3),
          ("transmit", 4))
    )


_RtrUdpechoState_Type.__name__ = "Integer32"
_RtrUdpechoState_Object = MibTableColumn
rtrUdpechoState = _RtrUdpechoState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 2),
    _RtrUdpechoState_Type()
)
rtrUdpechoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrUdpechoState.setStatus("current")
_RtrUdpechoTargetIp_Type = IpAddress
_RtrUdpechoTargetIp_Object = MibTableColumn
rtrUdpechoTargetIp = _RtrUdpechoTargetIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 3),
    _RtrUdpechoTargetIp_Type()
)
rtrUdpechoTargetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoTargetIp.setStatus("current")


class _RtrUdpechoTargetPort_Type(Unsigned32):
    """Custom type rtrUdpechoTargetPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtrUdpechoTargetPort_Type.__name__ = "Unsigned32"
_RtrUdpechoTargetPort_Object = MibTableColumn
rtrUdpechoTargetPort = _RtrUdpechoTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 4),
    _RtrUdpechoTargetPort_Type()
)
rtrUdpechoTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoTargetPort.setStatus("current")


class _RtrUdpechoPktLen_Type(Integer32):
    """Custom type rtrUdpechoPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1500),
    )


_RtrUdpechoPktLen_Type.__name__ = "Integer32"
_RtrUdpechoPktLen_Object = MibTableColumn
rtrUdpechoPktLen = _RtrUdpechoPktLen_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 5),
    _RtrUdpechoPktLen_Type()
)
rtrUdpechoPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoPktLen.setStatus("current")


class _RtrUdpechoSchInterval_Type(Unsigned32):
    """Custom type rtrUdpechoSchInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtrUdpechoSchInterval_Type.__name__ = "Unsigned32"
_RtrUdpechoSchInterval_Object = MibTableColumn
rtrUdpechoSchInterval = _RtrUdpechoSchInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 6),
    _RtrUdpechoSchInterval_Type()
)
rtrUdpechoSchInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoSchInterval.setStatus("current")
_RtrUdpechoSourceIp_Type = IpAddress
_RtrUdpechoSourceIp_Object = MibTableColumn
rtrUdpechoSourceIp = _RtrUdpechoSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 7),
    _RtrUdpechoSourceIp_Type()
)
rtrUdpechoSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoSourceIp.setStatus("current")


class _RtrUdpechoSourcePort_Type(Unsigned32):
    """Custom type rtrUdpechoSourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtrUdpechoSourcePort_Type.__name__ = "Unsigned32"
_RtrUdpechoSourcePort_Object = MibTableColumn
rtrUdpechoSourcePort = _RtrUdpechoSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 8),
    _RtrUdpechoSourcePort_Type()
)
rtrUdpechoSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoSourcePort.setStatus("current")


class _RtrUdpechoTimeout_Type(Unsigned32):
    """Custom type rtrUdpechoTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_RtrUdpechoTimeout_Type.__name__ = "Unsigned32"
_RtrUdpechoTimeout_Object = MibTableColumn
rtrUdpechoTimeout = _RtrUdpechoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 9),
    _RtrUdpechoTimeout_Type()
)
rtrUdpechoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoTimeout.setStatus("current")


class _RtrUdpechoVrfName_Type(DisplayString):
    """Custom type rtrUdpechoVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RtrUdpechoVrfName_Type.__name__ = "DisplayString"
_RtrUdpechoVrfName_Object = MibTableColumn
rtrUdpechoVrfName = _RtrUdpechoVrfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 10),
    _RtrUdpechoVrfName_Type()
)
rtrUdpechoVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoVrfName.setStatus("current")


class _RtrUdpechoTos_Type(Integer32):
    """Custom type rtrUdpechoTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RtrUdpechoTos_Type.__name__ = "Integer32"
_RtrUdpechoTos_Object = MibTableColumn
rtrUdpechoTos = _RtrUdpechoTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 11),
    _RtrUdpechoTos_Type()
)
rtrUdpechoTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoTos.setStatus("current")
_RtrUdpechoPktLoss_Type = Integer32
_RtrUdpechoPktLoss_Object = MibTableColumn
rtrUdpechoPktLoss = _RtrUdpechoPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 12),
    _RtrUdpechoPktLoss_Type()
)
rtrUdpechoPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrUdpechoPktLoss.setStatus("current")
_RtrUdpechoPktSucc_Type = Integer32
_RtrUdpechoPktSucc_Object = MibTableColumn
rtrUdpechoPktSucc = _RtrUdpechoPktSucc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 13),
    _RtrUdpechoPktSucc_Type()
)
rtrUdpechoPktSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrUdpechoPktSucc.setStatus("current")
_RtrUdpechoDelay_Type = Integer32
_RtrUdpechoDelay_Object = MibTableColumn
rtrUdpechoDelay = _RtrUdpechoDelay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 14),
    _RtrUdpechoDelay_Type()
)
rtrUdpechoDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrUdpechoDelay.setStatus("current")
_RtrUdpechoDelayMin_Type = Integer32
_RtrUdpechoDelayMin_Object = MibTableColumn
rtrUdpechoDelayMin = _RtrUdpechoDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 15),
    _RtrUdpechoDelayMin_Type()
)
rtrUdpechoDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrUdpechoDelayMin.setStatus("current")
_RtrUdpechoDelayMax_Type = Integer32
_RtrUdpechoDelayMax_Object = MibTableColumn
rtrUdpechoDelayMax = _RtrUdpechoDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 16),
    _RtrUdpechoDelayMax_Type()
)
rtrUdpechoDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtrUdpechoDelayMax.setStatus("current")
_RtrUdpechoRowStatus_Type = RowStatus
_RtrUdpechoRowStatus_Object = MibTableColumn
rtrUdpechoRowStatus = _RtrUdpechoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 200, 8, 100, 1, 17),
    _RtrUdpechoRowStatus_Type()
)
rtrUdpechoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtrUdpechoRowStatus.setStatus("current")
_SysIfStatistic_ObjectIdentity = ObjectIdentity
sysIfStatistic = _SysIfStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300)
)
_SysIfPktPriStatistics_ObjectIdentity = ObjectIdentity
sysIfPktPriStatistics = _SysIfPktPriStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1)
)
_SysIfPktPriStaTable_Object = MibTable
sysIfPktPriStaTable = _SysIfPktPriStaTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100)
)
if mibBuilder.loadTexts:
    sysIfPktPriStaTable.setStatus("current")
_SysIfPktPriStaEntry_Object = MibTableRow
sysIfPktPriStaEntry = _SysIfPktPriStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1)
)
sysIfPktPriStaEntry.setIndexNames(
    (0, "MPIOS-MIB", "sysIfPktPriority"),
    (0, "MPIOS-MIB", "sysIfIndex"),
)
if mibBuilder.loadTexts:
    sysIfPktPriStaEntry.setStatus("current")


class _SysIfPktPriority_Type(Integer32):
    """Custom type sysIfPktPriority based on Integer32"""
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
        *(("other", 9),
          ("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8))
    )


_SysIfPktPriority_Type.__name__ = "Integer32"
_SysIfPktPriority_Object = MibTableColumn
sysIfPktPriority = _SysIfPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 1),
    _SysIfPktPriority_Type()
)
sysIfPktPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfPktPriority.setStatus("current")
_SysIfIndex_Type = Integer32
_SysIfIndex_Object = MibTableColumn
sysIfIndex = _SysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 2),
    _SysIfIndex_Type()
)
sysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfIndex.setStatus("current")


class _SysIfDesc_Type(DisplayString):
    """Custom type sysIfDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysIfDesc_Type.__name__ = "DisplayString"
_SysIfDesc_Object = MibTableColumn
sysIfDesc = _SysIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 3),
    _SysIfDesc_Type()
)
sysIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfDesc.setStatus("current")
_SysIfInOctets_Type = Counter32
_SysIfInOctets_Object = MibTableColumn
sysIfInOctets = _SysIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 4),
    _SysIfInOctets_Type()
)
sysIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfInOctets.setStatus("current")
_SysIfInUcastPkts_Type = Counter32
_SysIfInUcastPkts_Object = MibTableColumn
sysIfInUcastPkts = _SysIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 5),
    _SysIfInUcastPkts_Type()
)
sysIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfInUcastPkts.setStatus("current")
_SysIfInNUcastPkts_Type = Counter32
_SysIfInNUcastPkts_Object = MibTableColumn
sysIfInNUcastPkts = _SysIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 6),
    _SysIfInNUcastPkts_Type()
)
sysIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfInNUcastPkts.setStatus("current")
_SysIfInDiscards_Type = Counter32
_SysIfInDiscards_Object = MibTableColumn
sysIfInDiscards = _SysIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 7),
    _SysIfInDiscards_Type()
)
sysIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfInDiscards.setStatus("current")
_SysIfInErrors_Type = Counter32
_SysIfInErrors_Object = MibTableColumn
sysIfInErrors = _SysIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 8),
    _SysIfInErrors_Type()
)
sysIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfInErrors.setStatus("current")
_SysIfInUnkownProtos_Type = Counter32
_SysIfInUnkownProtos_Object = MibTableColumn
sysIfInUnkownProtos = _SysIfInUnkownProtos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 9),
    _SysIfInUnkownProtos_Type()
)
sysIfInUnkownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfInUnkownProtos.setStatus("current")
_SysIfOutOctets_Type = Counter32
_SysIfOutOctets_Object = MibTableColumn
sysIfOutOctets = _SysIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 10),
    _SysIfOutOctets_Type()
)
sysIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfOutOctets.setStatus("current")
_SysIfOutUcastPkts_Type = Counter32
_SysIfOutUcastPkts_Object = MibTableColumn
sysIfOutUcastPkts = _SysIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 11),
    _SysIfOutUcastPkts_Type()
)
sysIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfOutUcastPkts.setStatus("current")
_SysIfOutNUcastPkts_Type = Counter32
_SysIfOutNUcastPkts_Object = MibTableColumn
sysIfOutNUcastPkts = _SysIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 12),
    _SysIfOutNUcastPkts_Type()
)
sysIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfOutNUcastPkts.setStatus("current")
_SysIfOutDiscards_Type = Counter32
_SysIfOutDiscards_Object = MibTableColumn
sysIfOutDiscards = _SysIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 13),
    _SysIfOutDiscards_Type()
)
sysIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfOutDiscards.setStatus("current")
_SysIfOutErrors_Type = Counter32
_SysIfOutErrors_Object = MibTableColumn
sysIfOutErrors = _SysIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 20, 1, 1, 300, 1, 100, 1, 14),
    _SysIfOutErrors_Type()
)
sysIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIfOutErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPIOS-MIB",
    **{"EnabledStatus": EnabledStatus,
       "mpios": mpios,
       "iosSystem": iosSystem,
       "iosObjects": iosObjects,
       "sysMemory": sysMemory,
       "numBytesFree": numBytesFree,
       "numBlocksFree": numBlocksFree,
       "avgBlockSizeFree": avgBlockSizeFree,
       "maxBlockSizeFree": maxBlockSizeFree,
       "numBytesAlloc": numBytesAlloc,
       "numBlocksAlloc": numBlocksAlloc,
       "avgBlockSizeAlloc": avgBlockSizeAlloc,
       "memoryTotalBytes": memoryTotalBytes,
       "allocBytesPercent": allocBytesPercent,
       "sysTask": sysTask,
       "taskTable": taskTable,
       "taskEntry": taskEntry,
       "taskId": taskId,
       "taskName": taskName,
       "taskPriority": taskPriority,
       "taskStatus": taskStatus,
       "taskOptions": taskOptions,
       "taskMain": taskMain,
       "taskStackPtr": taskStackPtr,
       "taskStackBase": taskStackBase,
       "taskStackPos": taskStackPos,
       "taskStackEnd": taskStackEnd,
       "taskStackSize": taskStackSize,
       "taskStackSizeUsage": taskStackSizeUsage,
       "taskStackMaxUsed": taskStackMaxUsed,
       "taskStackFree": taskStackFree,
       "taskErrorStatus": taskErrorStatus,
       "taskDescr": taskDescr,
       "sysCpu": sysCpu,
       "sysCpuStatus": sysCpuStatus,
       "sysCpuTaskTabView": sysCpuTaskTabView,
       "checkCpuTimeInterval": checkCpuTimeInterval,
       "cpuTaskTable": cpuTaskTable,
       "cpuTaskEntry": cpuTaskEntry,
       "cpuTaskId": cpuTaskId,
       "cpuTaskName": cpuTaskName,
       "cpuTaskPri": cpuTaskPri,
       "cpuTaskDeltaUtil": cpuTaskDeltaUtil,
       "cpuTaskDeltaTicks": cpuTaskDeltaTicks,
       "cpuTaskAverageUtil": cpuTaskAverageUtil,
       "cpuTaskTotalTicks": cpuTaskTotalTicks,
       "cpuTaskCurrentUtil": cpuTaskCurrentUtil,
       "cpuUtilTable": cpuUtilTable,
       "cpuUtilEntry": cpuUtilEntry,
       "cpuUtilCpuId": cpuUtilCpuId,
       "cpuUtilDeltaUtil": cpuUtilDeltaUtil,
       "cpuUtilDeltaUsedTicks": cpuUtilDeltaUsedTicks,
       "cpuUtilDeltaTicks": cpuUtilDeltaTicks,
       "cpuUtilDeltaTimes": cpuUtilDeltaTimes,
       "cpuUtilAverageUtil": cpuUtilAverageUtil,
       "cpuUtilTotalUsedTicks": cpuUtilTotalUsedTicks,
       "cpuUtilTotalTicks": cpuUtilTotalTicks,
       "cpuUtilTotalTimes": cpuUtilTotalTimes,
       "cpuUtilCurrentUtil": cpuUtilCurrentUtil,
       "sysTemperature": sysTemperature,
       "sysCpuTemper": sysCpuTemper,
       "sysCpuAlertTemper": sysCpuAlertTemper,
       "sysMainBoardTemper": sysMainBoardTemper,
       "sysMainBoardAlertTemper": sysMainBoardAlertTemper,
       "sysAlertTrapInt": sysAlertTrapInt,
       "sysNFI": sysNFI,
       "sysRtrGbl": sysRtrGbl,
       "sysRtrCtrl": sysRtrCtrl,
       "sysRtrResponder": sysRtrResponder,
       "sysRtrEntityMgt": sysRtrEntityMgt,
       "sysRtrEntityTable": sysRtrEntityTable,
       "sysRtrEntityEntry": sysRtrEntityEntry,
       "rtrEntityId": rtrEntityId,
       "rtrEntityName": rtrEntityName,
       "rtrEntityType": rtrEntityType,
       "rtrEntityLogType": rtrEntityLogType,
       "rtrEntityLogMaxSize": rtrEntityLogMaxSize,
       "rtrEntityLogFilter": rtrEntityLogFilter,
       "rtrEntityThreshold": rtrEntityThreshold,
       "rtrEntityRowStatus": rtrEntityRowStatus,
       "sysRtrGroupMgt": sysRtrGroupMgt,
       "sysRtrGroupTable": sysRtrGroupTable,
       "sysRtrGroupEntry": sysRtrGroupEntry,
       "rtrGroupId": rtrGroupId,
       "rtrGroupName": rtrGroupName,
       "rtrGroupInterval": rtrGroupInterval,
       "rtrGroupEntityMembers": rtrGroupEntityMembers,
       "rtrGroupRowStatus": rtrGroupRowStatus,
       "sysRtrScheduleMgt": sysRtrScheduleMgt,
       "sysRtrScheduleTable": sysRtrScheduleTable,
       "sysRtrScheduleEntry": sysRtrScheduleEntry,
       "rtrScheduleId": rtrScheduleId,
       "rtrScheduleType": rtrScheduleType,
       "rtrScheduleObjId": rtrScheduleObjId,
       "rtrScheduleStartTimeFlag": rtrScheduleStartTimeFlag,
       "rtrScheduleAfterTime": rtrScheduleAfterTime,
       "rtrScheduleStartTime": rtrScheduleStartTime,
       "rtrScheduleAgeOut": rtrScheduleAgeOut,
       "rtrScheduleLifeFlag": rtrScheduleLifeFlag,
       "rtrScheduleLifeTime": rtrScheduleLifeTime,
       "rtrScheduleRepeat": rtrScheduleRepeat,
       "rtrScheduleInterval": rtrScheduleInterval,
       "rtrScheduleRowStatus": rtrScheduleRowStatus,
       "sysRtrIcmpEchoMgt": sysRtrIcmpEchoMgt,
       "sysRtrIcmpEchoTable": sysRtrIcmpEchoTable,
       "sysRtrIcmpEchoEntry": sysRtrIcmpEchoEntry,
       "rtrIcmpEchoEntityId": rtrIcmpEchoEntityId,
       "rtrIcmpEchoTargetIp": rtrIcmpEchoTargetIp,
       "rtrIcmpEchoPktNum": rtrIcmpEchoPktNum,
       "rtrIcmpEchoPktLen": rtrIcmpEchoPktLen,
       "rtrIcmpEchoTimeout": rtrIcmpEchoTimeout,
       "rtrIcmpEchoSchInterval": rtrIcmpEchoSchInterval,
       "rtrIcmpEchoExtendFlag": rtrIcmpEchoExtendFlag,
       "rtrIcmpEchoVrfName": rtrIcmpEchoVrfName,
       "rtrIcmpEchoSourceIp": rtrIcmpEchoSourceIp,
       "rtrIcmpEchoTos": rtrIcmpEchoTos,
       "rtrIcmpEchoSetDf": rtrIcmpEchoSetDf,
       "rtrIcmpEchoVerifyData": rtrIcmpEchoVerifyData,
       "rtrIcmpEchoIsScheduling": rtrIcmpEchoIsScheduling,
       "rtrIcmpEchoPktTotalSend": rtrIcmpEchoPktTotalSend,
       "rtrIcmpEchoPktTotalRcvd": rtrIcmpEchoPktTotalRcvd,
       "rtrIcmpEchoSuccessRate": rtrIcmpEchoSuccessRate,
       "rtrIcmpEchoRowStatus": rtrIcmpEchoRowStatus,
       "sysRtrJitterMgt": sysRtrJitterMgt,
       "sysRtrJitterTable": sysRtrJitterTable,
       "sysRtrJitterEntry": sysRtrJitterEntry,
       "rtrJitterEntityId": rtrJitterEntityId,
       "rtrJitterState": rtrJitterState,
       "rtrJitterTargetIp": rtrJitterTargetIp,
       "rtrJitterTargetPort": rtrJitterTargetPort,
       "rtrJitterCodec": rtrJitterCodec,
       "rtrJitterPktLen": rtrJitterPktLen,
       "rtrJitterPktNum": rtrJitterPktNum,
       "rtrJitterPktInterval": rtrJitterPktInterval,
       "rtrJitterSchInterval": rtrJitterSchInterval,
       "rtrJitterSourceIp": rtrJitterSourceIp,
       "rtrJitterSourcePort": rtrJitterSourcePort,
       "rtrJitterTimeout": rtrJitterTimeout,
       "rtrJitterVrfName": rtrJitterVrfName,
       "rtrJitterTos": rtrJitterTos,
       "rtrJitterMinRtt": rtrJitterMinRtt,
       "rtrJitterMaxRtt": rtrJitterMaxRtt,
       "rtrJitterPktLossSd": rtrJitterPktLossSd,
       "rtrJitterPktLossDs": rtrJitterPktLossDs,
       "rtrJitterDsMin": rtrJitterDsMin,
       "rtrJitterDsMax": rtrJitterDsMax,
       "rtrJitterSdMin": rtrJitterSdMin,
       "rtrJitterSdMax": rtrJitterSdMax,
       "rtrJitterDelayDsMin": rtrJitterDelayDsMin,
       "rtrJitterDelayDsMax": rtrJitterDelayDsMax,
       "rtrJitterDelaySdMin": rtrJitterDelaySdMin,
       "rtrJitterDelaySdMax": rtrJitterDelaySdMax,
       "rtrJitterIcpifMin": rtrJitterIcpifMin,
       "rtrJitterIcpifMax": rtrJitterIcpifMax,
       "rtrJitterMosMin": rtrJitterMosMin,
       "rtrJitterMosMax": rtrJitterMosMax,
       "rtrJitterRowStatus": rtrJitterRowStatus,
       "sysRtrFlowStatisticsMgt": sysRtrFlowStatisticsMgt,
       "sysRtrFlowStatisticsTable": sysRtrFlowStatisticsTable,
       "sysRtrFlowStatisticsEntry": sysRtrFlowStatisticsEntry,
       "rtrFlStatisticsEntityId": rtrFlStatisticsEntityId,
       "rtrFlStatisticsIfName": rtrFlStatisticsIfName,
       "rtrFlStatisticsInterval": rtrFlStatisticsInterval,
       "rtrFlStaInputMaxPkts": rtrFlStaInputMaxPkts,
       "rtrFlStaTmInputMaxPkts": rtrFlStaTmInputMaxPkts,
       "rtrFlStaInputMaxFlow": rtrFlStaInputMaxFlow,
       "rtrFlStaTmInputMaxFlow": rtrFlStaTmInputMaxFlow,
       "rtrFlStaInputMinPkts": rtrFlStaInputMinPkts,
       "rtrFlStaTmInputMinPkts": rtrFlStaTmInputMinPkts,
       "rtrFlStaInputMinFlow": rtrFlStaInputMinFlow,
       "rtrFlStaTmInputMinFlow": rtrFlStaTmInputMinFlow,
       "rtrFlStaOutputMaxPkts": rtrFlStaOutputMaxPkts,
       "rtrFlStaTmOutputMaxPkts": rtrFlStaTmOutputMaxPkts,
       "rtrFlStaOutputMaxFlow": rtrFlStaOutputMaxFlow,
       "rtrFlStaTmOutputMaxFlow": rtrFlStaTmOutputMaxFlow,
       "rtrFlStaOutputMinPkts": rtrFlStaOutputMinPkts,
       "rtrFlStaTmOutputMinPkts": rtrFlStaTmOutputMinPkts,
       "rtrFlStaOutputMinFlow": rtrFlStaOutputMinFlow,
       "rtrFlStaTmOutputMinFlow": rtrFlStaTmOutputMinFlow,
       "rtrFlowStatisticsRowStatus": rtrFlowStatisticsRowStatus,
       "sysRtrUdpechoMgt": sysRtrUdpechoMgt,
       "sysRtrUdpechoTable": sysRtrUdpechoTable,
       "sysRtrUdpechoEntry": sysRtrUdpechoEntry,
       "rtrUdpechoEntityId": rtrUdpechoEntityId,
       "rtrUdpechoState": rtrUdpechoState,
       "rtrUdpechoTargetIp": rtrUdpechoTargetIp,
       "rtrUdpechoTargetPort": rtrUdpechoTargetPort,
       "rtrUdpechoPktLen": rtrUdpechoPktLen,
       "rtrUdpechoSchInterval": rtrUdpechoSchInterval,
       "rtrUdpechoSourceIp": rtrUdpechoSourceIp,
       "rtrUdpechoSourcePort": rtrUdpechoSourcePort,
       "rtrUdpechoTimeout": rtrUdpechoTimeout,
       "rtrUdpechoVrfName": rtrUdpechoVrfName,
       "rtrUdpechoTos": rtrUdpechoTos,
       "rtrUdpechoPktLoss": rtrUdpechoPktLoss,
       "rtrUdpechoPktSucc": rtrUdpechoPktSucc,
       "rtrUdpechoDelay": rtrUdpechoDelay,
       "rtrUdpechoDelayMin": rtrUdpechoDelayMin,
       "rtrUdpechoDelayMax": rtrUdpechoDelayMax,
       "rtrUdpechoRowStatus": rtrUdpechoRowStatus,
       "sysIfStatistic": sysIfStatistic,
       "sysIfPktPriStatistics": sysIfPktPriStatistics,
       "sysIfPktPriStaTable": sysIfPktPriStaTable,
       "sysIfPktPriStaEntry": sysIfPktPriStaEntry,
       "sysIfPktPriority": sysIfPktPriority,
       "sysIfIndex": sysIfIndex,
       "sysIfDesc": sysIfDesc,
       "sysIfInOctets": sysIfInOctets,
       "sysIfInUcastPkts": sysIfInUcastPkts,
       "sysIfInNUcastPkts": sysIfInNUcastPkts,
       "sysIfInDiscards": sysIfInDiscards,
       "sysIfInErrors": sysIfInErrors,
       "sysIfInUnkownProtos": sysIfInUnkownProtos,
       "sysIfOutOctets": sysIfOutOctets,
       "sysIfOutUcastPkts": sysIfOutUcastPkts,
       "sysIfOutNUcastPkts": sysIfOutNUcastPkts,
       "sysIfOutDiscards": sysIfOutDiscards,
       "sysIfOutErrors": sysIfOutErrors}
)
