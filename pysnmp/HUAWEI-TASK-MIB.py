# SNMP MIB module (HUAWEI-TASK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TASK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:10 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hwTask = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27)
)
hwTask.setRevisions(
        ("2014-09-25 00:00",
         "2003-07-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwTaskStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              8,
              17,
              21,
              33,
              37,
              65,
              69,
              128,
              256,
              513,
              517)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("blockAndSuspend", 5),
          ("eventblock", 65),
          ("eventblockAndSuspend", 69),
          ("normalready", 0),
          ("preemptready", 256),
          ("prioblock", 128),
          ("queueblock", 17),
          ("queueblockAndSuspend", 21),
          ("running", 8),
          ("semaphoreblock", 33),
          ("semaphoreblockAandSuspend", 37),
          ("sleep", 2),
          ("sleptAndSuspend", 6),
          ("suspend", 4),
          ("writequeueblock", 513),
          ("writequeueblockAndSuspend", 517))
    )



# MIB Managed Objects in the order of their OIDs

_HwTaskObjects_ObjectIdentity = ObjectIdentity
hwTaskObjects = _HwTaskObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1)
)
_HwTaskTable_Object = MibTable
hwTaskTable = _HwTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1)
)
if mibBuilder.loadTexts:
    hwTaskTable.setStatus("current")
_HwTaskEntry_Object = MibTableRow
hwTaskEntry = _HwTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1)
)
hwTaskEntry.setIndexNames(
    (0, "HUAWEI-TASK-MIB", "hwTaskIndex"),
    (0, "HUAWEI-TASK-MIB", "hwTaskID"),
)
if mibBuilder.loadTexts:
    hwTaskEntry.setStatus("current")
_HwTaskIndex_Type = Gauge32
_HwTaskIndex_Object = MibTableColumn
hwTaskIndex = _HwTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 1),
    _HwTaskIndex_Type()
)
hwTaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTaskIndex.setStatus("current")
_HwTaskID_Type = Gauge32
_HwTaskID_Object = MibTableColumn
hwTaskID = _HwTaskID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 2),
    _HwTaskID_Type()
)
hwTaskID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTaskID.setStatus("current")


class _HwTaskName_Type(DisplayString):
    """Custom type hwTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwTaskName_Type.__name__ = "DisplayString"
_HwTaskName_Object = MibTableColumn
hwTaskName = _HwTaskName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 3),
    _HwTaskName_Type()
)
hwTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTaskName.setStatus("current")
_HwTaskStatus_Type = HwTaskStatusType
_HwTaskStatus_Object = MibTableColumn
hwTaskStatus = _HwTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 4),
    _HwTaskStatus_Type()
)
hwTaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTaskStatus.setStatus("current")
_HwTaskCpuUsage_Type = Gauge32
_HwTaskCpuUsage_Object = MibTableColumn
hwTaskCpuUsage = _HwTaskCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 5),
    _HwTaskCpuUsage_Type()
)
hwTaskCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTaskCpuUsage.setStatus("current")
_HwTaskuSecs_Type = Gauge32
_HwTaskuSecs_Object = MibTableColumn
hwTaskuSecs = _HwTaskuSecs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 1, 1, 6),
    _HwTaskuSecs_Type()
)
hwTaskuSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTaskuSecs.setStatus("current")
if mibBuilder.loadTexts:
    hwTaskuSecs.setUnits("millseconds")
_HwKeyTaskTable_Object = MibTable
hwKeyTaskTable = _HwKeyTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2)
)
if mibBuilder.loadTexts:
    hwKeyTaskTable.setStatus("current")
_HwKeyTaskEntry_Object = MibTableRow
hwKeyTaskEntry = _HwKeyTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1)
)
hwKeyTaskEntry.setIndexNames(
    (0, "HUAWEI-TASK-MIB", "hwKeyTaskIndex"),
    (0, "HUAWEI-TASK-MIB", "hwKeyTaskID"),
)
if mibBuilder.loadTexts:
    hwKeyTaskEntry.setStatus("current")
_HwKeyTaskIndex_Type = Integer32
_HwKeyTaskIndex_Object = MibTableColumn
hwKeyTaskIndex = _HwKeyTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 1),
    _HwKeyTaskIndex_Type()
)
hwKeyTaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKeyTaskIndex.setStatus("current")
_HwKeyTaskID_Type = Integer32
_HwKeyTaskID_Object = MibTableColumn
hwKeyTaskID = _HwKeyTaskID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 2),
    _HwKeyTaskID_Type()
)
hwKeyTaskID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKeyTaskID.setStatus("current")


class _HwKeyTaskName_Type(DisplayString):
    """Custom type hwKeyTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwKeyTaskName_Type.__name__ = "DisplayString"
_HwKeyTaskName_Object = MibTableColumn
hwKeyTaskName = _HwKeyTaskName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 3),
    _HwKeyTaskName_Type()
)
hwKeyTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKeyTaskName.setStatus("current")
_HwKeyTaskCpuUsage_Type = Integer32
_HwKeyTaskCpuUsage_Object = MibTableColumn
hwKeyTaskCpuUsage = _HwKeyTaskCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 1, 2, 1, 4),
    _HwKeyTaskCpuUsage_Type()
)
hwKeyTaskCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKeyTaskCpuUsage.setStatus("current")
_HwTaskNotifications_ObjectIdentity = ObjectIdentity
hwTaskNotifications = _HwTaskNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 2)
)
_HwTaskConformance_ObjectIdentity = ObjectIdentity
hwTaskConformance = _HwTaskConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3)
)
_HwTaskCompliances_ObjectIdentity = ObjectIdentity
hwTaskCompliances = _HwTaskCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 1)
)
_HwTaskGroups_ObjectIdentity = ObjectIdentity
hwTaskGroups = _HwTaskGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 2)
)

# Managed Objects groups

hwTaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 2, 1)
)
hwTaskGroup.setObjects(
      *(("HUAWEI-TASK-MIB", "hwTaskName"),
        ("HUAWEI-TASK-MIB", "hwTaskStatus"),
        ("HUAWEI-TASK-MIB", "hwTaskCpuUsage"),
        ("HUAWEI-TASK-MIB", "hwTaskuSecs"))
)
if mibBuilder.loadTexts:
    hwTaskGroup.setStatus("current")

hwKeyTaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 2, 2)
)
hwKeyTaskGroup.setObjects(
      *(("HUAWEI-TASK-MIB", "hwKeyTaskName"),
        ("HUAWEI-TASK-MIB", "hwKeyTaskCpuUsage"))
)
if mibBuilder.loadTexts:
    hwKeyTaskGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwTaskCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 27, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwTaskCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TASK-MIB",
    **{"HwTaskStatusType": HwTaskStatusType,
       "hwTask": hwTask,
       "hwTaskObjects": hwTaskObjects,
       "hwTaskTable": hwTaskTable,
       "hwTaskEntry": hwTaskEntry,
       "hwTaskIndex": hwTaskIndex,
       "hwTaskID": hwTaskID,
       "hwTaskName": hwTaskName,
       "hwTaskStatus": hwTaskStatus,
       "hwTaskCpuUsage": hwTaskCpuUsage,
       "hwTaskuSecs": hwTaskuSecs,
       "hwKeyTaskTable": hwKeyTaskTable,
       "hwKeyTaskEntry": hwKeyTaskEntry,
       "hwKeyTaskIndex": hwKeyTaskIndex,
       "hwKeyTaskID": hwKeyTaskID,
       "hwKeyTaskName": hwKeyTaskName,
       "hwKeyTaskCpuUsage": hwKeyTaskCpuUsage,
       "hwTaskNotifications": hwTaskNotifications,
       "hwTaskConformance": hwTaskConformance,
       "hwTaskCompliances": hwTaskCompliances,
       "hwTaskCompliance": hwTaskCompliance,
       "hwTaskGroups": hwTaskGroups,
       "hwTaskGroup": hwTaskGroup,
       "hwKeyTaskGroup": hwKeyTaskGroup}
)
