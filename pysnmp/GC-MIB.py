# SNMP MIB module (GC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:07 2024
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

(products,) = mibBuilder.importSymbols(
    "RBT-MIB",
    "products")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

gc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100)
)
gc.setRevisions(
        ("2014-12-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 1)
)
_Model_Type = OctetString
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 1, 1),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_SystemVersion_Type = OctetString
_SystemVersion_Object = MibScalar
systemVersion = _SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 1, 3),
    _SystemVersion_Type()
)
systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVersion.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2)
)
_SystemClock_Type = DateAndTime
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 1),
    _SystemClock_Type()
)
systemClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemClock.setStatus("current")
_Health_Type = OctetString
_Health_Object = MibScalar
health = _Health_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 2),
    _Health_Type()
)
health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health.setStatus("current")


class _SystemHealth_Type(Integer32):
    """Custom type systemHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10000,
              30000,
              50000)
        )
    )
    namedValues = NamedValues(
        *(("critical", 50000),
          ("degraded", 30000),
          ("healthy", 10000))
    )


_SystemHealth_Type.__name__ = "Integer32"
_SystemHealth_Object = MibScalar
systemHealth = _SystemHealth_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 3),
    _SystemHealth_Type()
)
systemHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealth.setStatus("current")
_SystemTemperature_Type = Unsigned32
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 4),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")
_ProcTable_Object = MibTable
procTable = _ProcTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 11)
)
if mibBuilder.loadTexts:
    procTable.setStatus("current")
_ProcEntry_Object = MibTableRow
procEntry = _ProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 11, 1)
)
procEntry.setIndexNames(
    (0, "GC-MIB", "procIndex"),
)
if mibBuilder.loadTexts:
    procEntry.setStatus("current")
_ProcIndex_Type = Unsigned32
_ProcIndex_Object = MibTableColumn
procIndex = _ProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 11, 1, 1),
    _ProcIndex_Type()
)
procIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    procIndex.setStatus("current")
_ProcName_Type = OctetString
_ProcName_Object = MibTableColumn
procName = _ProcName_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 11, 1, 2),
    _ProcName_Type()
)
procName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procName.setStatus("current")
_ProcStatus_Type = OctetString
_ProcStatus_Object = MibTableColumn
procStatus = _ProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 11, 1, 3),
    _ProcStatus_Type()
)
procStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procStatus.setStatus("current")
_ProcNumFailures_Type = Unsigned32
_ProcNumFailures_Object = MibTableColumn
procNumFailures = _ProcNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 2, 11, 1, 4),
    _ProcNumFailures_Type()
)
procNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procNumFailures.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 3)
)
_ActiveConfig_Type = OctetString
_ActiveConfig_Object = MibScalar
activeConfig = _ActiveConfig_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 3, 1),
    _ActiveConfig_Type()
)
activeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeConfig.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4)
)
_AlarmsPrefix_ObjectIdentity = ObjectIdentity
alarmsPrefix = _AlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5)
)
_CpuLoad_ObjectIdentity = ObjectIdentity
cpuLoad = _CpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1)
)
_CpuLoad1_Type = Unsigned32
_CpuLoad1_Object = MibScalar
cpuLoad1 = _CpuLoad1_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 1),
    _CpuLoad1_Type()
)
cpuLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad1.setStatus("current")
_CpuLoad5_Type = Unsigned32
_CpuLoad5_Object = MibScalar
cpuLoad5 = _CpuLoad5_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 2),
    _CpuLoad5_Type()
)
cpuLoad5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad5.setStatus("current")
_CpuLoad15_Type = Unsigned32
_CpuLoad15_Object = MibScalar
cpuLoad15 = _CpuLoad15_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 3),
    _CpuLoad15_Type()
)
cpuLoad15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad15.setStatus("current")
_CpuUtil1_Type = Unsigned32
_CpuUtil1_Object = MibScalar
cpuUtil1 = _CpuUtil1_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 4),
    _CpuUtil1_Type()
)
cpuUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtil1.setStatus("current")
_CpuIndivUtilTable_Object = MibTable
cpuIndivUtilTable = _CpuIndivUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 5)
)
if mibBuilder.loadTexts:
    cpuIndivUtilTable.setStatus("current")
_CpuIndivUtilEntry_Object = MibTableRow
cpuIndivUtilEntry = _CpuIndivUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 5, 1)
)
cpuIndivUtilEntry.setIndexNames(
    (0, "GC-MIB", "cpuIndivIndex"),
)
if mibBuilder.loadTexts:
    cpuIndivUtilEntry.setStatus("current")
_CpuIndivIndex_Type = Unsigned32
_CpuIndivIndex_Object = MibTableColumn
cpuIndivIndex = _CpuIndivIndex_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 5, 1, 1),
    _CpuIndivIndex_Type()
)
cpuIndivIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuIndivIndex.setStatus("current")
_CpuIndivId_Type = Unsigned32
_CpuIndivId_Object = MibTableColumn
cpuIndivId = _CpuIndivId_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 5, 1, 2),
    _CpuIndivId_Type()
)
cpuIndivId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivId.setStatus("current")
_CpuIndivIdleTime_Type = Unsigned32
_CpuIndivIdleTime_Object = MibTableColumn
cpuIndivIdleTime = _CpuIndivIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 5, 1, 3),
    _CpuIndivIdleTime_Type()
)
cpuIndivIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivIdleTime.setStatus("current")
_CpuIndivSystemTime_Type = Unsigned32
_CpuIndivSystemTime_Object = MibTableColumn
cpuIndivSystemTime = _CpuIndivSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 5, 1, 4),
    _CpuIndivSystemTime_Type()
)
cpuIndivSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivSystemTime.setStatus("current")
_CpuIndivUserTime_Type = Unsigned32
_CpuIndivUserTime_Object = MibTableColumn
cpuIndivUserTime = _CpuIndivUserTime_Object(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 5, 1, 5, 1, 5),
    _CpuIndivUserTime_Type()
)
cpuIndivUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndivUserTime.setStatus("current")

# Managed Objects groups


# Notification objects

procCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1)
)
procCrash.setObjects(
    ("GC-MIB", "procName")
)
if mibBuilder.loadTexts:
    procCrash.setStatus(
        "current"
    )

procExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 2)
)
procExit.setObjects(
    ("GC-MIB", "procName")
)
if mibBuilder.loadTexts:
    procExit.setStatus(
        "current"
    )

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 3)
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        "current"
    )

cpuUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 4)
)
if mibBuilder.loadTexts:
    cpuUtil.setStatus(
        "current"
    )

pagingActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 5)
)
if mibBuilder.loadTexts:
    pagingActivity.setStatus(
        "current"
    )

linkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 6)
)
if mibBuilder.loadTexts:
    linkError.setStatus(
        "current"
    )

powerSupplyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 7)
)
if mibBuilder.loadTexts:
    powerSupplyError.setStatus(
        "current"
    )

fanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 8)
)
if mibBuilder.loadTexts:
    fanError.setStatus(
        "current"
    )

memoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 9)
)
if mibBuilder.loadTexts:
    memoryError.setStatus(
        "current"
    )

ipmi = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10)
)
if mibBuilder.loadTexts:
    ipmi.setStatus(
        "current"
    )

localFSFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11)
)
if mibBuilder.loadTexts:
    localFSFull.setStatus(
        "current"
    )

temperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 12)
)
if mibBuilder.loadTexts:
    temperatureCritical.setStatus(
        "current"
    )

temperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 13)
)
if mibBuilder.loadTexts:
    temperatureWarning.setStatus(
        "current"
    )

scheduledJobError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 14)
)
if mibBuilder.loadTexts:
    scheduledJobError.setStatus(
        "current"
    )

confModeEnter = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 15)
)
if mibBuilder.loadTexts:
    confModeEnter.setStatus(
        "current"
    )

confModeExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 16)
)
if mibBuilder.loadTexts:
    confModeExit.setStatus(
        "current"
    )

secureVaultLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 17)
)
if mibBuilder.loadTexts:
    secureVaultLocked.setStatus(
        "current"
    )

procRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 18)
)
procRestart.setObjects(
    ("GC-MIB", "procName")
)
if mibBuilder.loadTexts:
    procRestart.setStatus(
        "current"
    )

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 19)
)
testTrap.setObjects(
    ("GC-MIB", "procName")
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        "current"
    )

cpuUtilClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1004)
)
if mibBuilder.loadTexts:
    cpuUtilClear.setStatus(
        "current"
    )

pagingActivityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1005)
)
if mibBuilder.loadTexts:
    pagingActivityClear.setStatus(
        "current"
    )

linkErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1006)
)
if mibBuilder.loadTexts:
    linkErrorClear.setStatus(
        "current"
    )

powerSupplyErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1007)
)
if mibBuilder.loadTexts:
    powerSupplyErrorClear.setStatus(
        "current"
    )

fanErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1008)
)
if mibBuilder.loadTexts:
    fanErrorClear.setStatus(
        "current"
    )

memoryErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1009)
)
if mibBuilder.loadTexts:
    memoryErrorClear.setStatus(
        "current"
    )

ipmiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1010)
)
if mibBuilder.loadTexts:
    ipmiClear.setStatus(
        "current"
    )

localFSFullClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1011)
)
if mibBuilder.loadTexts:
    localFSFullClear.setStatus(
        "current"
    )

temperatureNonCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1012)
)
if mibBuilder.loadTexts:
    temperatureNonCritical.setStatus(
        "current"
    )

temperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1013)
)
if mibBuilder.loadTexts:
    temperatureNormal.setStatus(
        "current"
    )

secureVaultUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 1017)
)
if mibBuilder.loadTexts:
    secureVaultUnlocked.setStatus(
        "current"
    )

edgeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10500)
)
if mibBuilder.loadTexts:
    edgeError.setStatus(
        "current"
    )

highAvailabilityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10501)
)
if mibBuilder.loadTexts:
    highAvailabilityError.setStatus(
        "current"
    )

lunError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10502)
)
if mibBuilder.loadTexts:
    lunError.setStatus(
        "current"
    )

iscsiError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10503)
)
if mibBuilder.loadTexts:
    iscsiError.setStatus(
        "current"
    )

snapshotError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10505)
)
if mibBuilder.loadTexts:
    snapshotError.setStatus(
        "current"
    )

applianceUnlicensedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10506)
)
if mibBuilder.loadTexts:
    applianceUnlicensedError.setStatus(
        "current"
    )

modelUnlicensedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10507)
)
if mibBuilder.loadTexts:
    modelUnlicensedError.setStatus(
        "current"
    )

blkdiskError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10508)
)
if mibBuilder.loadTexts:
    blkdiskError.setStatus(
        "current"
    )

backupIntegrationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10509)
)
if mibBuilder.loadTexts:
    backupIntegrationError.setStatus(
        "current"
    )

otherHardwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 10510)
)
if mibBuilder.loadTexts:
    otherHardwareError.setStatus(
        "current"
    )

edgeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11500)
)
if mibBuilder.loadTexts:
    edgeClear.setStatus(
        "current"
    )

highAvailabilityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11501)
)
if mibBuilder.loadTexts:
    highAvailabilityClear.setStatus(
        "current"
    )

lunClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11502)
)
if mibBuilder.loadTexts:
    lunClear.setStatus(
        "current"
    )

iscsiClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11503)
)
if mibBuilder.loadTexts:
    iscsiClear.setStatus(
        "current"
    )

snapshotClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11505)
)
if mibBuilder.loadTexts:
    snapshotClear.setStatus(
        "current"
    )

applianceUnlicensedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11506)
)
if mibBuilder.loadTexts:
    applianceUnlicensedClear.setStatus(
        "current"
    )

modelUnlicensedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11507)
)
if mibBuilder.loadTexts:
    modelUnlicensedClear.setStatus(
        "current"
    )

blkdiskClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11508)
)
if mibBuilder.loadTexts:
    blkdiskClear.setStatus(
        "current"
    )

backupIntegrationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11509)
)
if mibBuilder.loadTexts:
    backupIntegrationClear.setStatus(
        "current"
    )

otherHardwareClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 17163, 1, 100, 4, 0, 11510)
)
if mibBuilder.loadTexts:
    otherHardwareClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GC-MIB",
    **{"gc": gc,
       "system": system,
       "model": model,
       "serialNumber": serialNumber,
       "systemVersion": systemVersion,
       "status": status,
       "systemClock": systemClock,
       "health": health,
       "systemHealth": systemHealth,
       "systemTemperature": systemTemperature,
       "procTable": procTable,
       "procEntry": procEntry,
       "procIndex": procIndex,
       "procName": procName,
       "procStatus": procStatus,
       "procNumFailures": procNumFailures,
       "config": config,
       "activeConfig": activeConfig,
       "alarms": alarms,
       "alarmsPrefix": alarmsPrefix,
       "procCrash": procCrash,
       "procExit": procExit,
       "configChange": configChange,
       "cpuUtil": cpuUtil,
       "pagingActivity": pagingActivity,
       "linkError": linkError,
       "powerSupplyError": powerSupplyError,
       "fanError": fanError,
       "memoryError": memoryError,
       "ipmi": ipmi,
       "localFSFull": localFSFull,
       "temperatureCritical": temperatureCritical,
       "temperatureWarning": temperatureWarning,
       "scheduledJobError": scheduledJobError,
       "confModeEnter": confModeEnter,
       "confModeExit": confModeExit,
       "secureVaultLocked": secureVaultLocked,
       "procRestart": procRestart,
       "testTrap": testTrap,
       "cpuUtilClear": cpuUtilClear,
       "pagingActivityClear": pagingActivityClear,
       "linkErrorClear": linkErrorClear,
       "powerSupplyErrorClear": powerSupplyErrorClear,
       "fanErrorClear": fanErrorClear,
       "memoryErrorClear": memoryErrorClear,
       "ipmiClear": ipmiClear,
       "localFSFullClear": localFSFullClear,
       "temperatureNonCritical": temperatureNonCritical,
       "temperatureNormal": temperatureNormal,
       "secureVaultUnlocked": secureVaultUnlocked,
       "edgeError": edgeError,
       "highAvailabilityError": highAvailabilityError,
       "lunError": lunError,
       "iscsiError": iscsiError,
       "snapshotError": snapshotError,
       "applianceUnlicensedError": applianceUnlicensedError,
       "modelUnlicensedError": modelUnlicensedError,
       "blkdiskError": blkdiskError,
       "backupIntegrationError": backupIntegrationError,
       "otherHardwareError": otherHardwareError,
       "edgeClear": edgeClear,
       "highAvailabilityClear": highAvailabilityClear,
       "lunClear": lunClear,
       "iscsiClear": iscsiClear,
       "snapshotClear": snapshotClear,
       "applianceUnlicensedClear": applianceUnlicensedClear,
       "modelUnlicensedClear": modelUnlicensedClear,
       "blkdiskClear": blkdiskClear,
       "backupIntegrationClear": backupIntegrationClear,
       "otherHardwareClear": otherHardwareClear,
       "statistics": statistics,
       "cpuLoad": cpuLoad,
       "cpuLoad1": cpuLoad1,
       "cpuLoad5": cpuLoad5,
       "cpuLoad15": cpuLoad15,
       "cpuUtil1": cpuUtil1,
       "cpuIndivUtilTable": cpuIndivUtilTable,
       "cpuIndivUtilEntry": cpuIndivUtilEntry,
       "cpuIndivIndex": cpuIndivIndex,
       "cpuIndivId": cpuIndivId,
       "cpuIndivIdleTime": cpuIndivIdleTime,
       "cpuIndivSystemTime": cpuIndivSystemTime,
       "cpuIndivUserTime": cpuIndivUserTime}
)
