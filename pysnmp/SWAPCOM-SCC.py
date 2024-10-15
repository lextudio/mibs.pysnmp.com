# SNMP MIB module (SWAPCOM-SCC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWAPCOM-SCC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:06 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

swapcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11308)
)
swapcom.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Scc_ObjectIdentity = ObjectIdentity
scc = _Scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 3)
)
_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 3, 1)
)
_PlatformPlatformId_Type = OctetString
_PlatformPlatformId_Object = MibScalar
platformPlatformId = _PlatformPlatformId_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 1, 1),
    _PlatformPlatformId_Type()
)
platformPlatformId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformPlatformId.setStatus("current")
_PlatformPlatformStatus_Type = Integer32
_PlatformPlatformStatus_Object = MibScalar
platformPlatformStatus = _PlatformPlatformStatus_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 1, 2),
    _PlatformPlatformStatus_Type()
)
platformPlatformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformPlatformStatus.setStatus("current")
_VersionTable_Object = MibTable
versionTable = _VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 2)
)
if mibBuilder.loadTexts:
    versionTable.setStatus("current")
_VersionEntry_Object = MibTableRow
versionEntry = _VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 2, 1)
)
versionEntry.setIndexNames(
    (0, "SWAPCOM-SCC", "versionProductName"),
)
if mibBuilder.loadTexts:
    versionEntry.setStatus("current")
_VersionProductName_Type = OctetString
_VersionProductName_Object = MibTableColumn
versionProductName = _VersionProductName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 2, 1, 1),
    _VersionProductName_Type()
)
versionProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionProductName.setStatus("current")
_VersionProductVersion_Type = OctetString
_VersionProductVersion_Object = MibTableColumn
versionProductVersion = _VersionProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 2, 1, 2),
    _VersionProductVersion_Type()
)
versionProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionProductVersion.setStatus("current")
_VersionBuildNumber_Type = Integer32
_VersionBuildNumber_Object = MibTableColumn
versionBuildNumber = _VersionBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 2, 1, 3),
    _VersionBuildNumber_Type()
)
versionBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionBuildNumber.setStatus("current")
_VersionBuildDate_Type = DisplayString
_VersionBuildDate_Object = MibTableColumn
versionBuildDate = _VersionBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 2, 1, 4),
    _VersionBuildDate_Type()
)
versionBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionBuildDate.setStatus("current")
_TransactionManager_ObjectIdentity = ObjectIdentity
transactionManager = _TransactionManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3)
)
_TransactionManagerLongTransactionThreshold_Type = Unsigned32
_TransactionManagerLongTransactionThreshold_Object = MibScalar
transactionManagerLongTransactionThreshold = _TransactionManagerLongTransactionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 1),
    _TransactionManagerLongTransactionThreshold_Type()
)
transactionManagerLongTransactionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerLongTransactionThreshold.setStatus("current")
_TransactionManagerActiveTransactionCurrentCount_Type = Integer32
_TransactionManagerActiveTransactionCurrentCount_Object = MibScalar
transactionManagerActiveTransactionCurrentCount = _TransactionManagerActiveTransactionCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 2),
    _TransactionManagerActiveTransactionCurrentCount_Type()
)
transactionManagerActiveTransactionCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerActiveTransactionCurrentCount.setStatus("current")
_TransactionManagerActiveTransactionMinCount_Type = Integer32
_TransactionManagerActiveTransactionMinCount_Object = MibScalar
transactionManagerActiveTransactionMinCount = _TransactionManagerActiveTransactionMinCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 3),
    _TransactionManagerActiveTransactionMinCount_Type()
)
transactionManagerActiveTransactionMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerActiveTransactionMinCount.setStatus("current")
_TransactionManagerActiveTransactionMaxCount_Type = Integer32
_TransactionManagerActiveTransactionMaxCount_Object = MibScalar
transactionManagerActiveTransactionMaxCount = _TransactionManagerActiveTransactionMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 4),
    _TransactionManagerActiveTransactionMaxCount_Type()
)
transactionManagerActiveTransactionMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerActiveTransactionMaxCount.setStatus("current")
_TransactionManagerCommittedTransactionCumulativeCount_Type = Integer32
_TransactionManagerCommittedTransactionCumulativeCount_Object = MibScalar
transactionManagerCommittedTransactionCumulativeCount = _TransactionManagerCommittedTransactionCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 5),
    _TransactionManagerCommittedTransactionCumulativeCount_Type()
)
transactionManagerCommittedTransactionCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerCommittedTransactionCumulativeCount.setStatus("current")
_TransactionManagerRolledbackTransactionCumulativeCount_Type = Integer32
_TransactionManagerRolledbackTransactionCumulativeCount_Object = MibScalar
transactionManagerRolledbackTransactionCumulativeCount = _TransactionManagerRolledbackTransactionCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 6),
    _TransactionManagerRolledbackTransactionCumulativeCount_Type()
)
transactionManagerRolledbackTransactionCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerRolledbackTransactionCumulativeCount.setStatus("current")
_TransactionManagerTransactionCumulativeTime_Type = Unsigned32
_TransactionManagerTransactionCumulativeTime_Object = MibScalar
transactionManagerTransactionCumulativeTime = _TransactionManagerTransactionCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 7),
    _TransactionManagerTransactionCumulativeTime_Type()
)
transactionManagerTransactionCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerTransactionCumulativeTime.setStatus("current")
_TransactionManagerTransactionMinTime_Type = Unsigned32
_TransactionManagerTransactionMinTime_Object = MibScalar
transactionManagerTransactionMinTime = _TransactionManagerTransactionMinTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 8),
    _TransactionManagerTransactionMinTime_Type()
)
transactionManagerTransactionMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerTransactionMinTime.setStatus("current")
_TransactionManagerTransactionMaxTime_Type = Unsigned32
_TransactionManagerTransactionMaxTime_Object = MibScalar
transactionManagerTransactionMaxTime = _TransactionManagerTransactionMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 9),
    _TransactionManagerTransactionMaxTime_Type()
)
transactionManagerTransactionMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerTransactionMaxTime.setStatus("current")
_TransactionManagerTransactionManagerLastError_Type = DisplayString
_TransactionManagerTransactionManagerLastError_Object = MibScalar
transactionManagerTransactionManagerLastError = _TransactionManagerTransactionManagerLastError_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 3, 10),
    _TransactionManagerTransactionManagerLastError_Type()
)
transactionManagerTransactionManagerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionManagerTransactionManagerLastError.setStatus("current")
_LockManager_ObjectIdentity = ObjectIdentity
lockManager = _LockManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4)
)
_LockManagerLockedItemCumulativeCount_Type = Integer32
_LockManagerLockedItemCumulativeCount_Object = MibScalar
lockManagerLockedItemCumulativeCount = _LockManagerLockedItemCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 1),
    _LockManagerLockedItemCumulativeCount_Type()
)
lockManagerLockedItemCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerLockedItemCumulativeCount.setStatus("current")
_LockManagerLockedItemCurrentCount_Type = Integer32
_LockManagerLockedItemCurrentCount_Object = MibScalar
lockManagerLockedItemCurrentCount = _LockManagerLockedItemCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 2),
    _LockManagerLockedItemCurrentCount_Type()
)
lockManagerLockedItemCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerLockedItemCurrentCount.setStatus("current")
_LockManagerLockedItemMinCount_Type = Integer32
_LockManagerLockedItemMinCount_Object = MibScalar
lockManagerLockedItemMinCount = _LockManagerLockedItemMinCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 3),
    _LockManagerLockedItemMinCount_Type()
)
lockManagerLockedItemMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerLockedItemMinCount.setStatus("current")
_LockManagerLockedItemMaxCount_Type = Integer32
_LockManagerLockedItemMaxCount_Object = MibScalar
lockManagerLockedItemMaxCount = _LockManagerLockedItemMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 4),
    _LockManagerLockedItemMaxCount_Type()
)
lockManagerLockedItemMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerLockedItemMaxCount.setStatus("current")
_LockManagerLockRejectedOnDeadlockCumulativeCount_Type = Integer32
_LockManagerLockRejectedOnDeadlockCumulativeCount_Object = MibScalar
lockManagerLockRejectedOnDeadlockCumulativeCount = _LockManagerLockRejectedOnDeadlockCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 5),
    _LockManagerLockRejectedOnDeadlockCumulativeCount_Type()
)
lockManagerLockRejectedOnDeadlockCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerLockRejectedOnDeadlockCumulativeCount.setStatus("current")
_LockManagerLockRejectedOnTimeoutCumulativeCount_Type = Integer32
_LockManagerLockRejectedOnTimeoutCumulativeCount_Object = MibScalar
lockManagerLockRejectedOnTimeoutCumulativeCount = _LockManagerLockRejectedOnTimeoutCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 6),
    _LockManagerLockRejectedOnTimeoutCumulativeCount_Type()
)
lockManagerLockRejectedOnTimeoutCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerLockRejectedOnTimeoutCumulativeCount.setStatus("current")
_LockManagerBlockedTransactionCurrentCount_Type = Integer32
_LockManagerBlockedTransactionCurrentCount_Object = MibScalar
lockManagerBlockedTransactionCurrentCount = _LockManagerBlockedTransactionCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 7),
    _LockManagerBlockedTransactionCurrentCount_Type()
)
lockManagerBlockedTransactionCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerBlockedTransactionCurrentCount.setStatus("current")
_LockManagerBlockedTransactionMinCount_Type = Integer32
_LockManagerBlockedTransactionMinCount_Object = MibScalar
lockManagerBlockedTransactionMinCount = _LockManagerBlockedTransactionMinCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 8),
    _LockManagerBlockedTransactionMinCount_Type()
)
lockManagerBlockedTransactionMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerBlockedTransactionMinCount.setStatus("current")
_LockManagerBlockedTransactionMaxCount_Type = Integer32
_LockManagerBlockedTransactionMaxCount_Object = MibScalar
lockManagerBlockedTransactionMaxCount = _LockManagerBlockedTransactionMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 4, 9),
    _LockManagerBlockedTransactionMaxCount_Type()
)
lockManagerBlockedTransactionMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockManagerBlockedTransactionMaxCount.setStatus("current")
_SchedulerTaskTable_Object = MibTable
schedulerTaskTable = _SchedulerTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5)
)
if mibBuilder.loadTexts:
    schedulerTaskTable.setStatus("current")
_SchedulerTaskEntry_Object = MibTableRow
schedulerTaskEntry = _SchedulerTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1)
)
schedulerTaskEntry.setIndexNames(
    (0, "SWAPCOM-SCC", "schedulerTaskName"),
)
if mibBuilder.loadTexts:
    schedulerTaskEntry.setStatus("current")
_SchedulerTaskName_Type = OctetString
_SchedulerTaskName_Object = MibTableColumn
schedulerTaskName = _SchedulerTaskName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 1),
    _SchedulerTaskName_Type()
)
schedulerTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskName.setStatus("current")
_SchedulerTaskRunning_Type = TruthValue
_SchedulerTaskRunning_Object = MibTableColumn
schedulerTaskRunning = _SchedulerTaskRunning_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 2),
    _SchedulerTaskRunning_Type()
)
schedulerTaskRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskRunning.setStatus("current")
_SchedulerTaskExecutionCumulativeCount_Type = Integer32
_SchedulerTaskExecutionCumulativeCount_Object = MibTableColumn
schedulerTaskExecutionCumulativeCount = _SchedulerTaskExecutionCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 3),
    _SchedulerTaskExecutionCumulativeCount_Type()
)
schedulerTaskExecutionCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskExecutionCumulativeCount.setStatus("current")
_SchedulerTaskExecutionCumulativeTime_Type = Unsigned32
_SchedulerTaskExecutionCumulativeTime_Object = MibTableColumn
schedulerTaskExecutionCumulativeTime = _SchedulerTaskExecutionCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 4),
    _SchedulerTaskExecutionCumulativeTime_Type()
)
schedulerTaskExecutionCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskExecutionCumulativeTime.setStatus("current")
_SchedulerTaskExecutionMinTime_Type = Unsigned32
_SchedulerTaskExecutionMinTime_Object = MibTableColumn
schedulerTaskExecutionMinTime = _SchedulerTaskExecutionMinTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 5),
    _SchedulerTaskExecutionMinTime_Type()
)
schedulerTaskExecutionMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskExecutionMinTime.setStatus("current")
_SchedulerTaskExecutionMaxTime_Type = Unsigned32
_SchedulerTaskExecutionMaxTime_Object = MibTableColumn
schedulerTaskExecutionMaxTime = _SchedulerTaskExecutionMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 6),
    _SchedulerTaskExecutionMaxTime_Type()
)
schedulerTaskExecutionMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskExecutionMaxTime.setStatus("current")
_SchedulerTaskExecutionRetryCurrentCount_Type = Integer32
_SchedulerTaskExecutionRetryCurrentCount_Object = MibTableColumn
schedulerTaskExecutionRetryCurrentCount = _SchedulerTaskExecutionRetryCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 7),
    _SchedulerTaskExecutionRetryCurrentCount_Type()
)
schedulerTaskExecutionRetryCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskExecutionRetryCurrentCount.setStatus("current")
_SchedulerTaskExecutionLastError_Type = DisplayString
_SchedulerTaskExecutionLastError_Object = MibTableColumn
schedulerTaskExecutionLastError = _SchedulerTaskExecutionLastError_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 5, 1, 8),
    _SchedulerTaskExecutionLastError_Type()
)
schedulerTaskExecutionLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerTaskExecutionLastError.setStatus("current")
_AlarmProbeTable_Object = MibTable
alarmProbeTable = _AlarmProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 12)
)
if mibBuilder.loadTexts:
    alarmProbeTable.setStatus("current")
_AlarmProbeEntry_Object = MibTableRow
alarmProbeEntry = _AlarmProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 12, 1)
)
alarmProbeEntry.setIndexNames(
    (0, "SWAPCOM-SCC", "alarmProbeAlertType"),
    (0, "SWAPCOM-SCC", "alarmProbeAlertSource"),
)
if mibBuilder.loadTexts:
    alarmProbeEntry.setStatus("current")
_AlarmProbeAlertType_Type = OctetString
_AlarmProbeAlertType_Object = MibTableColumn
alarmProbeAlertType = _AlarmProbeAlertType_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 12, 1, 1),
    _AlarmProbeAlertType_Type()
)
alarmProbeAlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProbeAlertType.setStatus("current")
_AlarmProbeAlertSource_Type = OctetString
_AlarmProbeAlertSource_Object = MibTableColumn
alarmProbeAlertSource = _AlarmProbeAlertSource_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 12, 1, 2),
    _AlarmProbeAlertSource_Type()
)
alarmProbeAlertSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProbeAlertSource.setStatus("current")
_AlarmProbeSeverity_Type = Integer32
_AlarmProbeSeverity_Object = MibTableColumn
alarmProbeSeverity = _AlarmProbeSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 12, 1, 3),
    _AlarmProbeSeverity_Type()
)
alarmProbeSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProbeSeverity.setStatus("current")
_AlarmProbeLastSeverityChange_Type = DisplayString
_AlarmProbeLastSeverityChange_Object = MibTableColumn
alarmProbeLastSeverityChange = _AlarmProbeLastSeverityChange_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 12, 1, 4),
    _AlarmProbeLastSeverityChange_Type()
)
alarmProbeLastSeverityChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProbeLastSeverityChange.setStatus("current")
_RemotePlatformTable_Object = MibTable
remotePlatformTable = _RemotePlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 21)
)
if mibBuilder.loadTexts:
    remotePlatformTable.setStatus("current")
_RemotePlatformEntry_Object = MibTableRow
remotePlatformEntry = _RemotePlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 21, 1)
)
remotePlatformEntry.setIndexNames(
    (0, "SWAPCOM-SCC", "remotePlatformPlatformId"),
)
if mibBuilder.loadTexts:
    remotePlatformEntry.setStatus("current")
_RemotePlatformPlatformId_Type = OctetString
_RemotePlatformPlatformId_Object = MibTableColumn
remotePlatformPlatformId = _RemotePlatformPlatformId_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 21, 1, 1),
    _RemotePlatformPlatformId_Type()
)
remotePlatformPlatformId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePlatformPlatformId.setStatus("current")
_RemotePlatformPlatformProtocol_Type = OctetString
_RemotePlatformPlatformProtocol_Object = MibTableColumn
remotePlatformPlatformProtocol = _RemotePlatformPlatformProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 21, 1, 2),
    _RemotePlatformPlatformProtocol_Type()
)
remotePlatformPlatformProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePlatformPlatformProtocol.setStatus("current")
_RemotePlatformRemotePlatformStatus_Type = Integer32
_RemotePlatformRemotePlatformStatus_Object = MibTableColumn
remotePlatformRemotePlatformStatus = _RemotePlatformRemotePlatformStatus_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 21, 1, 3),
    _RemotePlatformRemotePlatformStatus_Type()
)
remotePlatformRemotePlatformStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotePlatformRemotePlatformStatus.setStatus("current")
_AsynchronousEventQueueTable_Object = MibTable
asynchronousEventQueueTable = _AsynchronousEventQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22)
)
if mibBuilder.loadTexts:
    asynchronousEventQueueTable.setStatus("current")
_AsynchronousEventQueueEntry_Object = MibTableRow
asynchronousEventQueueEntry = _AsynchronousEventQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1)
)
asynchronousEventQueueEntry.setIndexNames(
    (0, "SWAPCOM-SCC", "asynchronousEventQueuePlatformId"),
)
if mibBuilder.loadTexts:
    asynchronousEventQueueEntry.setStatus("current")
_AsynchronousEventQueuePlatformId_Type = OctetString
_AsynchronousEventQueuePlatformId_Object = MibTableColumn
asynchronousEventQueuePlatformId = _AsynchronousEventQueuePlatformId_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 1),
    _AsynchronousEventQueuePlatformId_Type()
)
asynchronousEventQueuePlatformId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueuePlatformId.setStatus("current")
_AsynchronousEventQueueInsertedEventCumulativeCount_Type = Integer32
_AsynchronousEventQueueInsertedEventCumulativeCount_Object = MibTableColumn
asynchronousEventQueueInsertedEventCumulativeCount = _AsynchronousEventQueueInsertedEventCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 2),
    _AsynchronousEventQueueInsertedEventCumulativeCount_Type()
)
asynchronousEventQueueInsertedEventCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueInsertedEventCumulativeCount.setStatus("current")
_AsynchronousEventQueueWaitingEventCurrentCount_Type = Integer32
_AsynchronousEventQueueWaitingEventCurrentCount_Object = MibTableColumn
asynchronousEventQueueWaitingEventCurrentCount = _AsynchronousEventQueueWaitingEventCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 3),
    _AsynchronousEventQueueWaitingEventCurrentCount_Type()
)
asynchronousEventQueueWaitingEventCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueWaitingEventCurrentCount.setStatus("current")
_AsynchronousEventQueueWaitingEventMinCount_Type = Integer32
_AsynchronousEventQueueWaitingEventMinCount_Object = MibTableColumn
asynchronousEventQueueWaitingEventMinCount = _AsynchronousEventQueueWaitingEventMinCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 4),
    _AsynchronousEventQueueWaitingEventMinCount_Type()
)
asynchronousEventQueueWaitingEventMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueWaitingEventMinCount.setStatus("current")
_AsynchronousEventQueueWaitingEventMaxCount_Type = Integer32
_AsynchronousEventQueueWaitingEventMaxCount_Object = MibTableColumn
asynchronousEventQueueWaitingEventMaxCount = _AsynchronousEventQueueWaitingEventMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 5),
    _AsynchronousEventQueueWaitingEventMaxCount_Type()
)
asynchronousEventQueueWaitingEventMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueWaitingEventMaxCount.setStatus("current")
_AsynchronousEventQueueProcessedEventCumulativeCount_Type = Integer32
_AsynchronousEventQueueProcessedEventCumulativeCount_Object = MibTableColumn
asynchronousEventQueueProcessedEventCumulativeCount = _AsynchronousEventQueueProcessedEventCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 6),
    _AsynchronousEventQueueProcessedEventCumulativeCount_Type()
)
asynchronousEventQueueProcessedEventCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueProcessedEventCumulativeCount.setStatus("current")
_AsynchronousEventQueueEventProcessingCumulativeTime_Type = Unsigned32
_AsynchronousEventQueueEventProcessingCumulativeTime_Object = MibTableColumn
asynchronousEventQueueEventProcessingCumulativeTime = _AsynchronousEventQueueEventProcessingCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 7),
    _AsynchronousEventQueueEventProcessingCumulativeTime_Type()
)
asynchronousEventQueueEventProcessingCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueEventProcessingCumulativeTime.setStatus("current")
_AsynchronousEventQueueEventProcessingMinTime_Type = Unsigned32
_AsynchronousEventQueueEventProcessingMinTime_Object = MibTableColumn
asynchronousEventQueueEventProcessingMinTime = _AsynchronousEventQueueEventProcessingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 8),
    _AsynchronousEventQueueEventProcessingMinTime_Type()
)
asynchronousEventQueueEventProcessingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueEventProcessingMinTime.setStatus("current")
_AsynchronousEventQueueEventProcessingMaxTime_Type = Unsigned32
_AsynchronousEventQueueEventProcessingMaxTime_Object = MibTableColumn
asynchronousEventQueueEventProcessingMaxTime = _AsynchronousEventQueueEventProcessingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 9),
    _AsynchronousEventQueueEventProcessingMaxTime_Type()
)
asynchronousEventQueueEventProcessingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueEventProcessingMaxTime.setStatus("current")
_AsynchronousEventQueueFailedEventCumulativeCount_Type = Integer32
_AsynchronousEventQueueFailedEventCumulativeCount_Object = MibTableColumn
asynchronousEventQueueFailedEventCumulativeCount = _AsynchronousEventQueueFailedEventCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 10),
    _AsynchronousEventQueueFailedEventCumulativeCount_Type()
)
asynchronousEventQueueFailedEventCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueFailedEventCumulativeCount.setStatus("current")
_AsynchronousEventQueueFailedEventLastError_Type = DisplayString
_AsynchronousEventQueueFailedEventLastError_Object = MibTableColumn
asynchronousEventQueueFailedEventLastError = _AsynchronousEventQueueFailedEventLastError_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 22, 1, 11),
    _AsynchronousEventQueueFailedEventLastError_Type()
)
asynchronousEventQueueFailedEventLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asynchronousEventQueueFailedEventLastError.setStatus("current")
_SlsConnection_ObjectIdentity = ObjectIdentity
slsConnection = _SlsConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11308, 3, 23)
)
_SlsConnectionConnected_Type = TruthValue
_SlsConnectionConnected_Object = MibScalar
slsConnectionConnected = _SlsConnectionConnected_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 23, 1),
    _SlsConnectionConnected_Type()
)
slsConnectionConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slsConnectionConnected.setStatus("current")
_SlsConnectionLicenseCheckSuccessCumulativeCount_Type = Integer32
_SlsConnectionLicenseCheckSuccessCumulativeCount_Object = MibScalar
slsConnectionLicenseCheckSuccessCumulativeCount = _SlsConnectionLicenseCheckSuccessCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 23, 2),
    _SlsConnectionLicenseCheckSuccessCumulativeCount_Type()
)
slsConnectionLicenseCheckSuccessCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slsConnectionLicenseCheckSuccessCumulativeCount.setStatus("current")
_SlsConnectionLicenseCheckFailedCumulativeCount_Type = Integer32
_SlsConnectionLicenseCheckFailedCumulativeCount_Object = MibScalar
slsConnectionLicenseCheckFailedCumulativeCount = _SlsConnectionLicenseCheckFailedCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 23, 3),
    _SlsConnectionLicenseCheckFailedCumulativeCount_Type()
)
slsConnectionLicenseCheckFailedCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slsConnectionLicenseCheckFailedCumulativeCount.setStatus("current")
_SlsConnectionLicenseCheckLastError_Type = DisplayString
_SlsConnectionLicenseCheckLastError_Object = MibScalar
slsConnectionLicenseCheckLastError = _SlsConnectionLicenseCheckLastError_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 23, 4),
    _SlsConnectionLicenseCheckLastError_Type()
)
slsConnectionLicenseCheckLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slsConnectionLicenseCheckLastError.setStatus("current")
_SqlPoolXATable_Object = MibTable
sqlPoolXATable = _SqlPoolXATable_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24)
)
if mibBuilder.loadTexts:
    sqlPoolXATable.setStatus("current")
_SqlPoolXAEntry_Object = MibTableRow
sqlPoolXAEntry = _SqlPoolXAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1)
)
sqlPoolXAEntry.setIndexNames(
    (0, "SWAPCOM-SCC", "sqlPoolXAName"),
)
if mibBuilder.loadTexts:
    sqlPoolXAEntry.setStatus("current")
_SqlPoolXAName_Type = OctetString
_SqlPoolXAName_Object = MibTableColumn
sqlPoolXAName = _SqlPoolXAName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 1),
    _SqlPoolXAName_Type()
)
sqlPoolXAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXAName.setStatus("current")
_SqlPoolXASqlPlatformName_Type = OctetString
_SqlPoolXASqlPlatformName_Object = MibTableColumn
sqlPoolXASqlPlatformName = _SqlPoolXASqlPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 2),
    _SqlPoolXASqlPlatformName_Type()
)
sqlPoolXASqlPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXASqlPlatformName.setStatus("current")
_SqlPoolXADatabaseName_Type = OctetString
_SqlPoolXADatabaseName_Object = MibTableColumn
sqlPoolXADatabaseName = _SqlPoolXADatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 3),
    _SqlPoolXADatabaseName_Type()
)
sqlPoolXADatabaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXADatabaseName.setStatus("current")
_SqlPoolXADriverName_Type = OctetString
_SqlPoolXADriverName_Object = MibTableColumn
sqlPoolXADriverName = _SqlPoolXADriverName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 4),
    _SqlPoolXADriverName_Type()
)
sqlPoolXADriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXADriverName.setStatus("current")
_SqlPoolXADriverClassName_Type = OctetString
_SqlPoolXADriverClassName_Object = MibTableColumn
sqlPoolXADriverClassName = _SqlPoolXADriverClassName_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 5),
    _SqlPoolXADriverClassName_Type()
)
sqlPoolXADriverClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXADriverClassName.setStatus("current")
_SqlPoolXAMaximumSize_Type = Integer32
_SqlPoolXAMaximumSize_Object = MibTableColumn
sqlPoolXAMaximumSize = _SqlPoolXAMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 6),
    _SqlPoolXAMaximumSize_Type()
)
sqlPoolXAMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXAMaximumSize.setStatus("current")
_SqlPoolXAMaximumIdleTime_Type = Unsigned32
_SqlPoolXAMaximumIdleTime_Object = MibTableColumn
sqlPoolXAMaximumIdleTime = _SqlPoolXAMaximumIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 7),
    _SqlPoolXAMaximumIdleTime_Type()
)
sqlPoolXAMaximumIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXAMaximumIdleTime.setStatus("current")
_SqlPoolXAMaximumWaitTime_Type = Unsigned32
_SqlPoolXAMaximumWaitTime_Object = MibTableColumn
sqlPoolXAMaximumWaitTime = _SqlPoolXAMaximumWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 8),
    _SqlPoolXAMaximumWaitTime_Type()
)
sqlPoolXAMaximumWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXAMaximumWaitTime.setStatus("current")
_SqlPoolXACheckIsClosedInterval_Type = Unsigned32
_SqlPoolXACheckIsClosedInterval_Object = MibTableColumn
sqlPoolXACheckIsClosedInterval = _SqlPoolXACheckIsClosedInterval_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 9),
    _SqlPoolXACheckIsClosedInterval_Type()
)
sqlPoolXACheckIsClosedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckIsClosedInterval.setStatus("current")
_SqlPoolXACreateConnectionSuccessCumulativeCount_Type = Integer32
_SqlPoolXACreateConnectionSuccessCumulativeCount_Object = MibTableColumn
sqlPoolXACreateConnectionSuccessCumulativeCount = _SqlPoolXACreateConnectionSuccessCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 10),
    _SqlPoolXACreateConnectionSuccessCumulativeCount_Type()
)
sqlPoolXACreateConnectionSuccessCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACreateConnectionSuccessCumulativeCount.setStatus("current")
_SqlPoolXACreateConnectionFailureCumulativeCount_Type = Integer32
_SqlPoolXACreateConnectionFailureCumulativeCount_Object = MibTableColumn
sqlPoolXACreateConnectionFailureCumulativeCount = _SqlPoolXACreateConnectionFailureCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 11),
    _SqlPoolXACreateConnectionFailureCumulativeCount_Type()
)
sqlPoolXACreateConnectionFailureCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACreateConnectionFailureCumulativeCount.setStatus("current")
_SqlPoolXACreateConnectionLastError_Type = DisplayString
_SqlPoolXACreateConnectionLastError_Object = MibTableColumn
sqlPoolXACreateConnectionLastError = _SqlPoolXACreateConnectionLastError_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 12),
    _SqlPoolXACreateConnectionLastError_Type()
)
sqlPoolXACreateConnectionLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACreateConnectionLastError.setStatus("current")
_SqlPoolXAConnectionCurrentCount_Type = Integer32
_SqlPoolXAConnectionCurrentCount_Object = MibTableColumn
sqlPoolXAConnectionCurrentCount = _SqlPoolXAConnectionCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 13),
    _SqlPoolXAConnectionCurrentCount_Type()
)
sqlPoolXAConnectionCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXAConnectionCurrentCount.setStatus("current")
_SqlPoolXAConnectionMinCount_Type = Integer32
_SqlPoolXAConnectionMinCount_Object = MibTableColumn
sqlPoolXAConnectionMinCount = _SqlPoolXAConnectionMinCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 14),
    _SqlPoolXAConnectionMinCount_Type()
)
sqlPoolXAConnectionMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXAConnectionMinCount.setStatus("current")
_SqlPoolXAConnectionMaxCount_Type = Integer32
_SqlPoolXAConnectionMaxCount_Object = MibTableColumn
sqlPoolXAConnectionMaxCount = _SqlPoolXAConnectionMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 15),
    _SqlPoolXAConnectionMaxCount_Type()
)
sqlPoolXAConnectionMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXAConnectionMaxCount.setStatus("current")
_SqlPoolXACheckedOutConnectionCurrentCount_Type = Integer32
_SqlPoolXACheckedOutConnectionCurrentCount_Object = MibTableColumn
sqlPoolXACheckedOutConnectionCurrentCount = _SqlPoolXACheckedOutConnectionCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 16),
    _SqlPoolXACheckedOutConnectionCurrentCount_Type()
)
sqlPoolXACheckedOutConnectionCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionCurrentCount.setStatus("current")
_SqlPoolXACheckedOutConnectionMinCount_Type = Integer32
_SqlPoolXACheckedOutConnectionMinCount_Object = MibTableColumn
sqlPoolXACheckedOutConnectionMinCount = _SqlPoolXACheckedOutConnectionMinCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 17),
    _SqlPoolXACheckedOutConnectionMinCount_Type()
)
sqlPoolXACheckedOutConnectionMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionMinCount.setStatus("current")
_SqlPoolXACheckedOutConnectionMaxCount_Type = Integer32
_SqlPoolXACheckedOutConnectionMaxCount_Object = MibTableColumn
sqlPoolXACheckedOutConnectionMaxCount = _SqlPoolXACheckedOutConnectionMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 18),
    _SqlPoolXACheckedOutConnectionMaxCount_Type()
)
sqlPoolXACheckedOutConnectionMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionMaxCount.setStatus("current")
_SqlPoolXACheckedOutConnectionCumulativeCount_Type = Integer32
_SqlPoolXACheckedOutConnectionCumulativeCount_Object = MibTableColumn
sqlPoolXACheckedOutConnectionCumulativeCount = _SqlPoolXACheckedOutConnectionCumulativeCount_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 19),
    _SqlPoolXACheckedOutConnectionCumulativeCount_Type()
)
sqlPoolXACheckedOutConnectionCumulativeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionCumulativeCount.setStatus("current")
_SqlPoolXACheckedOutConnectionCumulativeTime_Type = Unsigned32
_SqlPoolXACheckedOutConnectionCumulativeTime_Object = MibTableColumn
sqlPoolXACheckedOutConnectionCumulativeTime = _SqlPoolXACheckedOutConnectionCumulativeTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 20),
    _SqlPoolXACheckedOutConnectionCumulativeTime_Type()
)
sqlPoolXACheckedOutConnectionCumulativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionCumulativeTime.setStatus("current")
_SqlPoolXACheckedOutConnectionMinTime_Type = Unsigned32
_SqlPoolXACheckedOutConnectionMinTime_Object = MibTableColumn
sqlPoolXACheckedOutConnectionMinTime = _SqlPoolXACheckedOutConnectionMinTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 21),
    _SqlPoolXACheckedOutConnectionMinTime_Type()
)
sqlPoolXACheckedOutConnectionMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionMinTime.setStatus("current")
_SqlPoolXACheckedOutConnectionMaxTime_Type = Unsigned32
_SqlPoolXACheckedOutConnectionMaxTime_Object = MibTableColumn
sqlPoolXACheckedOutConnectionMaxTime = _SqlPoolXACheckedOutConnectionMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 22),
    _SqlPoolXACheckedOutConnectionMaxTime_Type()
)
sqlPoolXACheckedOutConnectionMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionMaxTime.setStatus("current")
_SqlPoolXACheckedOutConnectionAverageTime_Type = DisplayString
_SqlPoolXACheckedOutConnectionAverageTime_Object = MibTableColumn
sqlPoolXACheckedOutConnectionAverageTime = _SqlPoolXACheckedOutConnectionAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 11308, 3, 24, 1, 23),
    _SqlPoolXACheckedOutConnectionAverageTime_Type()
)
sqlPoolXACheckedOutConnectionAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sqlPoolXACheckedOutConnectionAverageTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWAPCOM-SCC",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "swapcom": swapcom,
       "scc": scc,
       "platform": platform,
       "platformPlatformId": platformPlatformId,
       "platformPlatformStatus": platformPlatformStatus,
       "versionTable": versionTable,
       "versionEntry": versionEntry,
       "versionProductName": versionProductName,
       "versionProductVersion": versionProductVersion,
       "versionBuildNumber": versionBuildNumber,
       "versionBuildDate": versionBuildDate,
       "transactionManager": transactionManager,
       "transactionManagerLongTransactionThreshold": transactionManagerLongTransactionThreshold,
       "transactionManagerActiveTransactionCurrentCount": transactionManagerActiveTransactionCurrentCount,
       "transactionManagerActiveTransactionMinCount": transactionManagerActiveTransactionMinCount,
       "transactionManagerActiveTransactionMaxCount": transactionManagerActiveTransactionMaxCount,
       "transactionManagerCommittedTransactionCumulativeCount": transactionManagerCommittedTransactionCumulativeCount,
       "transactionManagerRolledbackTransactionCumulativeCount": transactionManagerRolledbackTransactionCumulativeCount,
       "transactionManagerTransactionCumulativeTime": transactionManagerTransactionCumulativeTime,
       "transactionManagerTransactionMinTime": transactionManagerTransactionMinTime,
       "transactionManagerTransactionMaxTime": transactionManagerTransactionMaxTime,
       "transactionManagerTransactionManagerLastError": transactionManagerTransactionManagerLastError,
       "lockManager": lockManager,
       "lockManagerLockedItemCumulativeCount": lockManagerLockedItemCumulativeCount,
       "lockManagerLockedItemCurrentCount": lockManagerLockedItemCurrentCount,
       "lockManagerLockedItemMinCount": lockManagerLockedItemMinCount,
       "lockManagerLockedItemMaxCount": lockManagerLockedItemMaxCount,
       "lockManagerLockRejectedOnDeadlockCumulativeCount": lockManagerLockRejectedOnDeadlockCumulativeCount,
       "lockManagerLockRejectedOnTimeoutCumulativeCount": lockManagerLockRejectedOnTimeoutCumulativeCount,
       "lockManagerBlockedTransactionCurrentCount": lockManagerBlockedTransactionCurrentCount,
       "lockManagerBlockedTransactionMinCount": lockManagerBlockedTransactionMinCount,
       "lockManagerBlockedTransactionMaxCount": lockManagerBlockedTransactionMaxCount,
       "schedulerTaskTable": schedulerTaskTable,
       "schedulerTaskEntry": schedulerTaskEntry,
       "schedulerTaskName": schedulerTaskName,
       "schedulerTaskRunning": schedulerTaskRunning,
       "schedulerTaskExecutionCumulativeCount": schedulerTaskExecutionCumulativeCount,
       "schedulerTaskExecutionCumulativeTime": schedulerTaskExecutionCumulativeTime,
       "schedulerTaskExecutionMinTime": schedulerTaskExecutionMinTime,
       "schedulerTaskExecutionMaxTime": schedulerTaskExecutionMaxTime,
       "schedulerTaskExecutionRetryCurrentCount": schedulerTaskExecutionRetryCurrentCount,
       "schedulerTaskExecutionLastError": schedulerTaskExecutionLastError,
       "alarmProbeTable": alarmProbeTable,
       "alarmProbeEntry": alarmProbeEntry,
       "alarmProbeAlertType": alarmProbeAlertType,
       "alarmProbeAlertSource": alarmProbeAlertSource,
       "alarmProbeSeverity": alarmProbeSeverity,
       "alarmProbeLastSeverityChange": alarmProbeLastSeverityChange,
       "remotePlatformTable": remotePlatformTable,
       "remotePlatformEntry": remotePlatformEntry,
       "remotePlatformPlatformId": remotePlatformPlatformId,
       "remotePlatformPlatformProtocol": remotePlatformPlatformProtocol,
       "remotePlatformRemotePlatformStatus": remotePlatformRemotePlatformStatus,
       "asynchronousEventQueueTable": asynchronousEventQueueTable,
       "asynchronousEventQueueEntry": asynchronousEventQueueEntry,
       "asynchronousEventQueuePlatformId": asynchronousEventQueuePlatformId,
       "asynchronousEventQueueInsertedEventCumulativeCount": asynchronousEventQueueInsertedEventCumulativeCount,
       "asynchronousEventQueueWaitingEventCurrentCount": asynchronousEventQueueWaitingEventCurrentCount,
       "asynchronousEventQueueWaitingEventMinCount": asynchronousEventQueueWaitingEventMinCount,
       "asynchronousEventQueueWaitingEventMaxCount": asynchronousEventQueueWaitingEventMaxCount,
       "asynchronousEventQueueProcessedEventCumulativeCount": asynchronousEventQueueProcessedEventCumulativeCount,
       "asynchronousEventQueueEventProcessingCumulativeTime": asynchronousEventQueueEventProcessingCumulativeTime,
       "asynchronousEventQueueEventProcessingMinTime": asynchronousEventQueueEventProcessingMinTime,
       "asynchronousEventQueueEventProcessingMaxTime": asynchronousEventQueueEventProcessingMaxTime,
       "asynchronousEventQueueFailedEventCumulativeCount": asynchronousEventQueueFailedEventCumulativeCount,
       "asynchronousEventQueueFailedEventLastError": asynchronousEventQueueFailedEventLastError,
       "slsConnection": slsConnection,
       "slsConnectionConnected": slsConnectionConnected,
       "slsConnectionLicenseCheckSuccessCumulativeCount": slsConnectionLicenseCheckSuccessCumulativeCount,
       "slsConnectionLicenseCheckFailedCumulativeCount": slsConnectionLicenseCheckFailedCumulativeCount,
       "slsConnectionLicenseCheckLastError": slsConnectionLicenseCheckLastError,
       "sqlPoolXATable": sqlPoolXATable,
       "sqlPoolXAEntry": sqlPoolXAEntry,
       "sqlPoolXAName": sqlPoolXAName,
       "sqlPoolXASqlPlatformName": sqlPoolXASqlPlatformName,
       "sqlPoolXADatabaseName": sqlPoolXADatabaseName,
       "sqlPoolXADriverName": sqlPoolXADriverName,
       "sqlPoolXADriverClassName": sqlPoolXADriverClassName,
       "sqlPoolXAMaximumSize": sqlPoolXAMaximumSize,
       "sqlPoolXAMaximumIdleTime": sqlPoolXAMaximumIdleTime,
       "sqlPoolXAMaximumWaitTime": sqlPoolXAMaximumWaitTime,
       "sqlPoolXACheckIsClosedInterval": sqlPoolXACheckIsClosedInterval,
       "sqlPoolXACreateConnectionSuccessCumulativeCount": sqlPoolXACreateConnectionSuccessCumulativeCount,
       "sqlPoolXACreateConnectionFailureCumulativeCount": sqlPoolXACreateConnectionFailureCumulativeCount,
       "sqlPoolXACreateConnectionLastError": sqlPoolXACreateConnectionLastError,
       "sqlPoolXAConnectionCurrentCount": sqlPoolXAConnectionCurrentCount,
       "sqlPoolXAConnectionMinCount": sqlPoolXAConnectionMinCount,
       "sqlPoolXAConnectionMaxCount": sqlPoolXAConnectionMaxCount,
       "sqlPoolXACheckedOutConnectionCurrentCount": sqlPoolXACheckedOutConnectionCurrentCount,
       "sqlPoolXACheckedOutConnectionMinCount": sqlPoolXACheckedOutConnectionMinCount,
       "sqlPoolXACheckedOutConnectionMaxCount": sqlPoolXACheckedOutConnectionMaxCount,
       "sqlPoolXACheckedOutConnectionCumulativeCount": sqlPoolXACheckedOutConnectionCumulativeCount,
       "sqlPoolXACheckedOutConnectionCumulativeTime": sqlPoolXACheckedOutConnectionCumulativeTime,
       "sqlPoolXACheckedOutConnectionMinTime": sqlPoolXACheckedOutConnectionMinTime,
       "sqlPoolXACheckedOutConnectionMaxTime": sqlPoolXACheckedOutConnectionMaxTime,
       "sqlPoolXACheckedOutConnectionAverageTime": sqlPoolXACheckedOutConnectionAverageTime}
)
