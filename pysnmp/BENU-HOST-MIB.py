# SNMP MIB module (BENU-HOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-HOST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:53 2024
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

(benuPlatform,) = mibBuilder.importSymbols(
    "BENU-PLATFORM-MIB",
    "benuPlatform")

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

bHostMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5)
)
bHostMIB.setRevisions(
        ("2015-11-03 00:00",
         "2015-04-28 00:00",
         "2015-04-27 00:00",
         "2015-01-05 00:00",
         "2015-01-04 00:00",
         "2014-12-17 00:00",
         "2014-09-22 00:00",
         "2014-03-21 00:00",
         "2013-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BHostNotifObjects_ObjectIdentity = ObjectIdentity
bHostNotifObjects = _BHostNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 0)
)
if mibBuilder.loadTexts:
    bHostNotifObjects.setStatus("current")
_BHostMIBObjects_ObjectIdentity = ObjectIdentity
bHostMIBObjects = _BHostMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1)
)
if mibBuilder.loadTexts:
    bHostMIBObjects.setStatus("current")
_BSWTaskInfoTable_Object = MibTable
bSWTaskInfoTable = _BSWTaskInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    bSWTaskInfoTable.setStatus("current")
_BSWTaskInfoEntry_Object = MibTableRow
bSWTaskInfoEntry = _BSWTaskInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1)
)
bSWTaskInfoEntry.setIndexNames(
    (0, "BENU-HOST-MIB", "bSWTaskIndex"),
)
if mibBuilder.loadTexts:
    bSWTaskInfoEntry.setStatus("current")
_BSWTaskIndex_Type = Integer32
_BSWTaskIndex_Object = MibTableColumn
bSWTaskIndex = _BSWTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 1),
    _BSWTaskIndex_Type()
)
bSWTaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bSWTaskIndex.setStatus("current")
_BSWTaskName_Type = DisplayString
_BSWTaskName_Object = MibTableColumn
bSWTaskName = _BSWTaskName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 2),
    _BSWTaskName_Type()
)
bSWTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskName.setStatus("current")
_BSWTaskProcessID_Type = Unsigned32
_BSWTaskProcessID_Object = MibTableColumn
bSWTaskProcessID = _BSWTaskProcessID_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 3),
    _BSWTaskProcessID_Type()
)
bSWTaskProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskProcessID.setStatus("current")
_BSWTaskLoadIntervalDuration_Type = Unsigned32
_BSWTaskLoadIntervalDuration_Object = MibTableColumn
bSWTaskLoadIntervalDuration = _BSWTaskLoadIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 4),
    _BSWTaskLoadIntervalDuration_Type()
)
bSWTaskLoadIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskLoadIntervalDuration.setStatus("current")
_BSWTaskRunStateTime_Type = TimeTicks
_BSWTaskRunStateTime_Object = MibTableColumn
bSWTaskRunStateTime = _BSWTaskRunStateTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 5),
    _BSWTaskRunStateTime_Type()
)
bSWTaskRunStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskRunStateTime.setStatus("current")
_BSWTaskCPUUsage_Type = Unsigned32
_BSWTaskCPUUsage_Object = MibTableColumn
bSWTaskCPUUsage = _BSWTaskCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 6),
    _BSWTaskCPUUsage_Type()
)
bSWTaskCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskCPUUsage.setStatus("current")
_BSWTaskAvgCPUUsage_Type = Unsigned32
_BSWTaskAvgCPUUsage_Object = MibTableColumn
bSWTaskAvgCPUUsage = _BSWTaskAvgCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 7),
    _BSWTaskAvgCPUUsage_Type()
)
bSWTaskAvgCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskAvgCPUUsage.setStatus("current")
_BSWTaskMaxCPUUsage_Type = Unsigned32
_BSWTaskMaxCPUUsage_Object = MibTableColumn
bSWTaskMaxCPUUsage = _BSWTaskMaxCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 8),
    _BSWTaskMaxCPUUsage_Type()
)
bSWTaskMaxCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskMaxCPUUsage.setStatus("current")
_BSWTaskCodeSegmentSize_Type = Unsigned32
_BSWTaskCodeSegmentSize_Object = MibTableColumn
bSWTaskCodeSegmentSize = _BSWTaskCodeSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 9),
    _BSWTaskCodeSegmentSize_Type()
)
bSWTaskCodeSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskCodeSegmentSize.setStatus("current")
_BSWTaskDataSegmentSize_Type = Unsigned32
_BSWTaskDataSegmentSize_Object = MibTableColumn
bSWTaskDataSegmentSize = _BSWTaskDataSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 10),
    _BSWTaskDataSegmentSize_Type()
)
bSWTaskDataSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskDataSegmentSize.setStatus("current")
_BSWTaskResidentPhyMem_Type = Unsigned32
_BSWTaskResidentPhyMem_Object = MibTableColumn
bSWTaskResidentPhyMem = _BSWTaskResidentPhyMem_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 11),
    _BSWTaskResidentPhyMem_Type()
)
bSWTaskResidentPhyMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskResidentPhyMem.setStatus("current")
_BSWTaskVirtMemUsage_Type = Unsigned32
_BSWTaskVirtMemUsage_Object = MibTableColumn
bSWTaskVirtMemUsage = _BSWTaskVirtMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 12),
    _BSWTaskVirtMemUsage_Type()
)
bSWTaskVirtMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskVirtMemUsage.setStatus("current")
_BSWTaskSharedMem_Type = Unsigned32
_BSWTaskSharedMem_Object = MibTableColumn
bSWTaskSharedMem = _BSWTaskSharedMem_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 13),
    _BSWTaskSharedMem_Type()
)
bSWTaskSharedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskSharedMem.setStatus("current")
_BSWTaskVirtMemPeakUsage_Type = Unsigned32
_BSWTaskVirtMemPeakUsage_Object = MibTableColumn
bSWTaskVirtMemPeakUsage = _BSWTaskVirtMemPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 14),
    _BSWTaskVirtMemPeakUsage_Type()
)
bSWTaskVirtMemPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskVirtMemPeakUsage.setStatus("current")
_BSWTaskAvgCPUUsageHighThreshold_Type = Unsigned32
_BSWTaskAvgCPUUsageHighThreshold_Object = MibTableColumn
bSWTaskAvgCPUUsageHighThreshold = _BSWTaskAvgCPUUsageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 15),
    _BSWTaskAvgCPUUsageHighThreshold_Type()
)
bSWTaskAvgCPUUsageHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskAvgCPUUsageHighThreshold.setStatus("current")
_BSWTaskAvgCPUUsageLowThreshold_Type = Unsigned32
_BSWTaskAvgCPUUsageLowThreshold_Object = MibTableColumn
bSWTaskAvgCPUUsageLowThreshold = _BSWTaskAvgCPUUsageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 16),
    _BSWTaskAvgCPUUsageLowThreshold_Type()
)
bSWTaskAvgCPUUsageLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskAvgCPUUsageLowThreshold.setStatus("current")
_BSWTaskCPUUsageLimit_Type = Unsigned32
_BSWTaskCPUUsageLimit_Object = MibTableColumn
bSWTaskCPUUsageLimit = _BSWTaskCPUUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 17),
    _BSWTaskCPUUsageLimit_Type()
)
bSWTaskCPUUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskCPUUsageLimit.setStatus("current")
_BSWTaskRestartLimit_Type = Unsigned32
_BSWTaskRestartLimit_Object = MibTableColumn
bSWTaskRestartLimit = _BSWTaskRestartLimit_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 18),
    _BSWTaskRestartLimit_Type()
)
bSWTaskRestartLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskRestartLimit.setStatus("current")


class _BSWTaskRestartability_Type(Integer32):
    """Custom type bSWTaskRestartability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_BSWTaskRestartability_Type.__name__ = "Integer32"
_BSWTaskRestartability_Object = MibTableColumn
bSWTaskRestartability = _BSWTaskRestartability_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 19),
    _BSWTaskRestartability_Type()
)
bSWTaskRestartability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskRestartability.setStatus("current")
_BSWTaskRestartCount_Type = Unsigned32
_BSWTaskRestartCount_Object = MibTableColumn
bSWTaskRestartCount = _BSWTaskRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 1, 1, 20),
    _BSWTaskRestartCount_Type()
)
bSWTaskRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSWTaskRestartCount.setStatus("current")
_BSysTotalMem_Type = Unsigned32
_BSysTotalMem_Object = MibScalar
bSysTotalMem = _BSysTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 2),
    _BSysTotalMem_Type()
)
bSysTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSysTotalMem.setStatus("current")
_BSysMemUsed_Type = Unsigned32
_BSysMemUsed_Object = MibScalar
bSysMemUsed = _BSysMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 3),
    _BSysMemUsed_Type()
)
bSysMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSysMemUsed.setStatus("current")
_BSysMemFree_Type = Unsigned32
_BSysMemFree_Object = MibScalar
bSysMemFree = _BSysMemFree_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 4),
    _BSysMemFree_Type()
)
bSysMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSysMemFree.setStatus("current")
_BSysTotalCPUUtilAvailable_Type = Unsigned32
_BSysTotalCPUUtilAvailable_Object = MibScalar
bSysTotalCPUUtilAvailable = _BSysTotalCPUUtilAvailable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 5),
    _BSysTotalCPUUtilAvailable_Type()
)
bSysTotalCPUUtilAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSysTotalCPUUtilAvailable.setStatus("current")
_BSysAvgCPUUtil15Sec_Type = Unsigned32
_BSysAvgCPUUtil15Sec_Object = MibScalar
bSysAvgCPUUtil15Sec = _BSysAvgCPUUtil15Sec_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 6),
    _BSysAvgCPUUtil15Sec_Type()
)
bSysAvgCPUUtil15Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSysAvgCPUUtil15Sec.setStatus("current")
_BSysAvgCPUUtil1Min_Type = Unsigned32
_BSysAvgCPUUtil1Min_Object = MibScalar
bSysAvgCPUUtil1Min = _BSysAvgCPUUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 7),
    _BSysAvgCPUUtil1Min_Type()
)
bSysAvgCPUUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSysAvgCPUUtil1Min.setStatus("current")
_BSysAvgCPUUtil5Min_Type = Unsigned32
_BSysAvgCPUUtil5Min_Object = MibScalar
bSysAvgCPUUtil5Min = _BSysAvgCPUUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 8),
    _BSysAvgCPUUtil5Min_Type()
)
bSysAvgCPUUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSysAvgCPUUtil5Min.setStatus("current")
_BCPUMonInterval_Type = Unsigned32
_BCPUMonInterval_Object = MibScalar
bCPUMonInterval = _BCPUMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 1, 9),
    _BCPUMonInterval_Type()
)
bCPUMonInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bCPUMonInterval.setStatus("current")
if mibBuilder.loadTexts:
    bCPUMonInterval.setUnits("seconds")
_BHostNotifVariables_ObjectIdentity = ObjectIdentity
bHostNotifVariables = _BHostNotifVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 2)
)
if mibBuilder.loadTexts:
    bHostNotifVariables.setStatus("current")


class _BSWTaskDiedReason_Type(Integer32):
    """Custom type bSWTaskDiedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpuUsageLimitReached", 1),
          ("unKnown", 2))
    )


_BSWTaskDiedReason_Type.__name__ = "Integer32"
_BSWTaskDiedReason_Object = MibScalar
bSWTaskDiedReason = _BSWTaskDiedReason_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 1),
    _BSWTaskDiedReason_Type()
)
bSWTaskDiedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bSWTaskDiedReason.setStatus("current")
_BSWProcessName_Type = DisplayString
_BSWProcessName_Object = MibScalar
bSWProcessName = _BSWProcessName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 2),
    _BSWProcessName_Type()
)
bSWProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bSWProcessName.setStatus("current")
_BSWProcessID_Type = Unsigned32
_BSWProcessID_Object = MibScalar
bSWProcessID = _BSWProcessID_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 3),
    _BSWProcessID_Type()
)
bSWProcessID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bSWProcessID.setStatus("current")
_BSWProcessAvgCPUUsageLowThreshold_Type = Unsigned32
_BSWProcessAvgCPUUsageLowThreshold_Object = MibScalar
bSWProcessAvgCPUUsageLowThreshold = _BSWProcessAvgCPUUsageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 4),
    _BSWProcessAvgCPUUsageLowThreshold_Type()
)
bSWProcessAvgCPUUsageLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bSWProcessAvgCPUUsageLowThreshold.setStatus("current")
_BSWProcessAvgCPUUsageHighThreshold_Type = Unsigned32
_BSWProcessAvgCPUUsageHighThreshold_Object = MibScalar
bSWProcessAvgCPUUsageHighThreshold = _BSWProcessAvgCPUUsageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 2, 5),
    _BSWProcessAvgCPUUsageHighThreshold_Type()
)
bSWProcessAvgCPUUsageHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bSWProcessAvgCPUUsageHighThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

bSWTaskAvgCPUUsageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 1)
)
bSWTaskAvgCPUUsageLow.setObjects(
      *(("BENU-HOST-MIB", "bSWProcessName"),
        ("BENU-HOST-MIB", "bSWProcessID"),
        ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageLowThreshold"))
)
if mibBuilder.loadTexts:
    bSWTaskAvgCPUUsageLow.setStatus(
        "current"
    )

bSWTaskAvgCPUUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 2)
)
bSWTaskAvgCPUUsageHigh.setObjects(
      *(("BENU-HOST-MIB", "bSWProcessName"),
        ("BENU-HOST-MIB", "bSWProcessID"),
        ("BENU-HOST-MIB", "bSWProcessAvgCPUUsageHighThreshold"))
)
if mibBuilder.loadTexts:
    bSWTaskAvgCPUUsageHigh.setStatus(
        "current"
    )

bSWTaskDied = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 3)
)
bSWTaskDied.setObjects(
      *(("BENU-HOST-MIB", "bSWProcessName"),
        ("BENU-HOST-MIB", "bSWProcessID"),
        ("BENU-HOST-MIB", "bSWTaskDiedReason"))
)
if mibBuilder.loadTexts:
    bSWTaskDied.setStatus(
        "current"
    )

bSWTaskRestartLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 1, 5, 0, 4)
)
bSWTaskRestartLimitReached.setObjects(
      *(("BENU-HOST-MIB", "bSWProcessName"),
        ("BENU-HOST-MIB", "bSWProcessID"))
)
if mibBuilder.loadTexts:
    bSWTaskRestartLimitReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-HOST-MIB",
    **{"bHostMIB": bHostMIB,
       "bHostNotifObjects": bHostNotifObjects,
       "bSWTaskAvgCPUUsageLow": bSWTaskAvgCPUUsageLow,
       "bSWTaskAvgCPUUsageHigh": bSWTaskAvgCPUUsageHigh,
       "bSWTaskDied": bSWTaskDied,
       "bSWTaskRestartLimitReached": bSWTaskRestartLimitReached,
       "bHostMIBObjects": bHostMIBObjects,
       "bSWTaskInfoTable": bSWTaskInfoTable,
       "bSWTaskInfoEntry": bSWTaskInfoEntry,
       "bSWTaskIndex": bSWTaskIndex,
       "bSWTaskName": bSWTaskName,
       "bSWTaskProcessID": bSWTaskProcessID,
       "bSWTaskLoadIntervalDuration": bSWTaskLoadIntervalDuration,
       "bSWTaskRunStateTime": bSWTaskRunStateTime,
       "bSWTaskCPUUsage": bSWTaskCPUUsage,
       "bSWTaskAvgCPUUsage": bSWTaskAvgCPUUsage,
       "bSWTaskMaxCPUUsage": bSWTaskMaxCPUUsage,
       "bSWTaskCodeSegmentSize": bSWTaskCodeSegmentSize,
       "bSWTaskDataSegmentSize": bSWTaskDataSegmentSize,
       "bSWTaskResidentPhyMem": bSWTaskResidentPhyMem,
       "bSWTaskVirtMemUsage": bSWTaskVirtMemUsage,
       "bSWTaskSharedMem": bSWTaskSharedMem,
       "bSWTaskVirtMemPeakUsage": bSWTaskVirtMemPeakUsage,
       "bSWTaskAvgCPUUsageHighThreshold": bSWTaskAvgCPUUsageHighThreshold,
       "bSWTaskAvgCPUUsageLowThreshold": bSWTaskAvgCPUUsageLowThreshold,
       "bSWTaskCPUUsageLimit": bSWTaskCPUUsageLimit,
       "bSWTaskRestartLimit": bSWTaskRestartLimit,
       "bSWTaskRestartability": bSWTaskRestartability,
       "bSWTaskRestartCount": bSWTaskRestartCount,
       "bSysTotalMem": bSysTotalMem,
       "bSysMemUsed": bSysMemUsed,
       "bSysMemFree": bSysMemFree,
       "bSysTotalCPUUtilAvailable": bSysTotalCPUUtilAvailable,
       "bSysAvgCPUUtil15Sec": bSysAvgCPUUtil15Sec,
       "bSysAvgCPUUtil1Min": bSysAvgCPUUtil1Min,
       "bSysAvgCPUUtil5Min": bSysAvgCPUUtil5Min,
       "bCPUMonInterval": bCPUMonInterval,
       "bHostNotifVariables": bHostNotifVariables,
       "bSWTaskDiedReason": bSWTaskDiedReason,
       "bSWProcessName": bSWProcessName,
       "bSWProcessID": bSWProcessID,
       "bSWProcessAvgCPUUsageLowThreshold": bSWProcessAvgCPUUsageLowThreshold,
       "bSWProcessAvgCPUUsageHighThreshold": bSWProcessAvgCPUUsageHighThreshold}
)
