# SNMP MIB module (RM-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RM-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:01 2024
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

(cpuUsage,
 curSize,
 disk,
 file,
 host,
 load,
 maxSize,
 memUsage,
 percentage,
 processID,
 processName,
 status) = mibBuilder.importSymbols(
    "AGGREGATED-EXT-MIB",
    "cpuUsage",
    "curSize",
    "disk",
    "file",
    "host",
    "load",
    "maxSize",
    "memUsage",
    "percentage",
    "processID",
    "processName",
    "status")

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
 ObjectName,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rmTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_SoftSwitch_ObjectIdentity = ObjectIdentity
softSwitch = _SoftSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)
_ResourceMonitor_ObjectIdentity = ObjectIdentity
resourceMonitor = _ResourceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4)
)

# Managed Objects groups


# Notification objects

cpuUtilWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 0)
)
cpuUtilWarning.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "percentage"))
)
if mibBuilder.loadTexts:
    cpuUtilWarning.setStatus(
        "current"
    )

cpuUtilAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 1)
)
cpuUtilAlarm.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "percentage"))
)
if mibBuilder.loadTexts:
    cpuUtilAlarm.setStatus(
        "current"
    )

cpuUtilInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 2)
)
cpuUtilInform.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "percentage"),
        ("AGGREGATED-EXT-MIB", "status"))
)
if mibBuilder.loadTexts:
    cpuUtilInform.setStatus(
        "current"
    )

cpuLoadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 3)
)
cpuLoadWarning.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "load"))
)
if mibBuilder.loadTexts:
    cpuLoadWarning.setStatus(
        "current"
    )

cpuLoadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 4)
)
cpuLoadAlarm.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "load"))
)
if mibBuilder.loadTexts:
    cpuLoadAlarm.setStatus(
        "current"
    )

cpuLoadInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 5)
)
cpuLoadInform.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "load"),
        ("AGGREGATED-EXT-MIB", "status"))
)
if mibBuilder.loadTexts:
    cpuLoadInform.setStatus(
        "current"
    )

diskUsageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 6)
)
diskUsageWarning.setObjects(
      *(("AGGREGATED-EXT-MIB", "disk"),
        ("AGGREGATED-EXT-MIB", "percentage"))
)
if mibBuilder.loadTexts:
    diskUsageWarning.setStatus(
        "current"
    )

diskUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 7)
)
diskUsageAlarm.setObjects(
      *(("AGGREGATED-EXT-MIB", "disk"),
        ("AGGREGATED-EXT-MIB", "percentage"))
)
if mibBuilder.loadTexts:
    diskUsageAlarm.setStatus(
        "current"
    )

diskUsageInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 8)
)
diskUsageInform.setObjects(
      *(("AGGREGATED-EXT-MIB", "disk"),
        ("AGGREGATED-EXT-MIB", "percentage"),
        ("AGGREGATED-EXT-MIB", "status"))
)
if mibBuilder.loadTexts:
    diskUsageInform.setStatus(
        "current"
    )

fileSizeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 9)
)
fileSizeEvent.setObjects(
      *(("AGGREGATED-EXT-MIB", "file"),
        ("AGGREGATED-EXT-MIB", "curSize"),
        ("AGGREGATED-EXT-MIB", "maxSize"))
)
if mibBuilder.loadTexts:
    fileSizeEvent.setStatus(
        "current"
    )

unixProcessDied = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 10)
)
unixProcessDied.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "processName"),
        ("AGGREGATED-EXT-MIB", "processID"))
)
if mibBuilder.loadTexts:
    unixProcessDied.setStatus(
        "current"
    )

procCpuAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 11)
)
procCpuAlarm.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "processName"),
        ("AGGREGATED-EXT-MIB", "processID"),
        ("AGGREGATED-EXT-MIB", "cpuUsage"))
)
if mibBuilder.loadTexts:
    procCpuAlarm.setStatus(
        "current"
    )

procCpuWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 12)
)
procCpuWarn.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "processName"),
        ("AGGREGATED-EXT-MIB", "processID"),
        ("AGGREGATED-EXT-MIB", "cpuUsage"))
)
if mibBuilder.loadTexts:
    procCpuWarn.setStatus(
        "current"
    )

procMemAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 13)
)
procMemAlarm.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "processName"),
        ("AGGREGATED-EXT-MIB", "processID"),
        ("AGGREGATED-EXT-MIB", "memUsage"))
)
if mibBuilder.loadTexts:
    procMemAlarm.setStatus(
        "current"
    )

procCpuInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 14)
)
procCpuInform.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "processName"),
        ("AGGREGATED-EXT-MIB", "processID"))
)
if mibBuilder.loadTexts:
    procCpuInform.setStatus(
        "current"
    )

procMemInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 15)
)
procMemInform.setObjects(
      *(("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "processName"),
        ("AGGREGATED-EXT-MIB", "processID"))
)
if mibBuilder.loadTexts:
    procMemInform.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RM-TRAP-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "resourceMonitor": resourceMonitor,
       "rmTraps": rmTraps,
       "cpuUtilWarning": cpuUtilWarning,
       "cpuUtilAlarm": cpuUtilAlarm,
       "cpuUtilInform": cpuUtilInform,
       "cpuLoadWarning": cpuLoadWarning,
       "cpuLoadAlarm": cpuLoadAlarm,
       "cpuLoadInform": cpuLoadInform,
       "diskUsageWarning": diskUsageWarning,
       "diskUsageAlarm": diskUsageAlarm,
       "diskUsageInform": diskUsageInform,
       "fileSizeEvent": fileSizeEvent,
       "unixProcessDied": unixProcessDied,
       "procCpuAlarm": procCpuAlarm,
       "procCpuWarn": procCpuWarn,
       "procMemAlarm": procMemAlarm,
       "procCpuInform": procCpuInform,
       "procMemInform": procMemInform}
)
