# SNMP MIB module (ALTEON-ISD-PLATFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-ISD-PLATFORM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:54 2024
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

(platform,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "platform")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alteonPlatformISDModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 1)
)
alteonPlatformISDModule.setRevisions(
        ("1902-05-13 00:00",
         "1901-02-09 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 5),
          ("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("warning", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AlteonISDPlatformMIB_ObjectIdentity = ObjectIdentity
alteonISDPlatformMIB = _AlteonISDPlatformMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alteonISDPlatformMIB.setStatus("current")
_IsdObjects_ObjectIdentity = ObjectIdentity
isdObjects = _IsdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    isdObjects.setStatus("current")
_IsdCluster_ObjectIdentity = ObjectIdentity
isdCluster = _IsdCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    isdCluster.setStatus("current")
_IsdClusterTable_Object = MibTable
isdClusterTable = _IsdClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    isdClusterTable.setStatus("current")
_IsdClusterEntry_Object = MibTableRow
isdClusterEntry = _IsdClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1)
)
isdClusterEntry.setIndexNames(
    (0, "ALTEON-ISD-PLATFORM-MIB", "isdIndex"),
)
if mibBuilder.loadTexts:
    isdClusterEntry.setStatus("current")


class _IsdIndex_Type(Integer32):
    """Custom type isdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsdIndex_Type.__name__ = "Integer32"
_IsdIndex_Object = MibTableColumn
isdIndex = _IsdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 1),
    _IsdIndex_Type()
)
isdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdIndex.setStatus("current")
_IsdIP_Type = IpAddress
_IsdIP_Object = MibTableColumn
isdIP = _IsdIP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 2),
    _IsdIP_Type()
)
isdIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdIP.setStatus("current")


class _IsdType_Type(Integer32):
    """Custom type isdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_IsdType_Type.__name__ = "Integer32"
_IsdType_Object = MibTableColumn
isdType = _IsdType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 3),
    _IsdType_Type()
)
isdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdType.setStatus("current")


class _IsdOperStatus_Type(Integer32):
    """Custom type isdOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_IsdOperStatus_Type.__name__ = "Integer32"
_IsdOperStatus_Object = MibTableColumn
isdOperStatus = _IsdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 1, 1, 4),
    _IsdOperStatus_Type()
)
isdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdOperStatus.setStatus("current")
_IsdMIPOwner_Type = IpAddress
_IsdMIPOwner_Object = MibScalar
isdMIPOwner = _IsdMIPOwner_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 2),
    _IsdMIPOwner_Type()
)
isdMIPOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdMIPOwner.setStatus("current")
_IsdCurrentTime_Type = DateAndTime
_IsdCurrentTime_Object = MibScalar
isdCurrentTime = _IsdCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 3),
    _IsdCurrentTime_Type()
)
isdCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdCurrentTime.setStatus("current")
_IsdVersion_Type = DisplayString
_IsdVersion_Object = MibScalar
isdVersion = _IsdVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 4),
    _IsdVersion_Type()
)
isdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdVersion.setStatus("current")
_IsdImageTable_Object = MibTable
isdImageTable = _IsdImageTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    isdImageTable.setStatus("current")
_IsdImageEntry_Object = MibTableRow
isdImageEntry = _IsdImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1)
)
isdImageEntry.setIndexNames(
    (0, "ALTEON-ISD-PLATFORM-MIB", "isdImageIndex"),
)
if mibBuilder.loadTexts:
    isdImageEntry.setStatus("current")
_IsdImageIndex_Type = Integer32
_IsdImageIndex_Object = MibTableColumn
isdImageIndex = _IsdImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 1),
    _IsdImageIndex_Type()
)
isdImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdImageIndex.setStatus("current")
_IsdImageVersion_Type = DisplayString
_IsdImageVersion_Object = MibTableColumn
isdImageVersion = _IsdImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 2),
    _IsdImageVersion_Type()
)
isdImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdImageVersion.setStatus("current")
_IsdImageName_Type = DisplayString
_IsdImageName_Object = MibTableColumn
isdImageName = _IsdImageName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 3),
    _IsdImageName_Type()
)
isdImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdImageName.setStatus("current")


class _IsdImageStatus_Type(Integer32):
    """Custom type isdImageStatus based on Integer32"""
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
        *(("current", 2),
          ("old", 3),
          ("permanent", 1),
          ("unpacked", 4))
    )


_IsdImageStatus_Type.__name__ = "Integer32"
_IsdImageStatus_Object = MibTableColumn
isdImageStatus = _IsdImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 5, 1, 4),
    _IsdImageStatus_Type()
)
isdImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdImageStatus.setStatus("current")
_IsdClusterMIP_Type = IpAddress
_IsdClusterMIP_Object = MibScalar
isdClusterMIP = _IsdClusterMIP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 6),
    _IsdClusterMIP_Type()
)
isdClusterMIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdClusterMIP.setStatus("current")
_IsdClusterMask_Type = IpAddress
_IsdClusterMask_Object = MibScalar
isdClusterMask = _IsdClusterMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 1, 7),
    _IsdClusterMask_Type()
)
isdClusterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdClusterMask.setStatus("current")
_CurrentAlarm_ObjectIdentity = ObjectIdentity
currentAlarm = _CurrentAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    currentAlarm.setStatus("current")
_NumberOfCurrentAlarms_Type = Gauge32
_NumberOfCurrentAlarms_Object = MibScalar
numberOfCurrentAlarms = _NumberOfCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 1),
    _NumberOfCurrentAlarms_Type()
)
numberOfCurrentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfCurrentAlarms.setStatus("current")
_CurrentAlarmLastTimeChanged_Type = TimeTicks
_CurrentAlarmLastTimeChanged_Object = MibScalar
currentAlarmLastTimeChanged = _CurrentAlarmLastTimeChanged_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 2),
    _CurrentAlarmLastTimeChanged_Type()
)
currentAlarmLastTimeChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmLastTimeChanged.setStatus("current")
_CurrentAlarmTable_Object = MibTable
currentAlarmTable = _CurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    currentAlarmTable.setStatus("current")
_CurrentAlarmEntry_Object = MibTableRow
currentAlarmEntry = _CurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1)
)
currentAlarmEntry.setIndexNames(
    (0, "ALTEON-ISD-PLATFORM-MIB", "currentAlarmIndex"),
)
if mibBuilder.loadTexts:
    currentAlarmEntry.setStatus("current")


class _CurrentAlarmIndex_Type(Integer32):
    """Custom type currentAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurrentAlarmIndex_Type.__name__ = "Integer32"
_CurrentAlarmIndex_Object = MibTableColumn
currentAlarmIndex = _CurrentAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 1),
    _CurrentAlarmIndex_Type()
)
currentAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentAlarmIndex.setStatus("current")
_CurrentAlarmSeverity_Type = AlarmSeverity
_CurrentAlarmSeverity_Object = MibTableColumn
currentAlarmSeverity = _CurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 2),
    _CurrentAlarmSeverity_Type()
)
currentAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentAlarmSeverity.setStatus("current")
_CurrentAlarmOid_Type = ObjectIdentifier
_CurrentAlarmOid_Object = MibTableColumn
currentAlarmOid = _CurrentAlarmOid_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 3),
    _CurrentAlarmOid_Type()
)
currentAlarmOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmOid.setStatus("current")
_CurrentAlarmObject_Type = ObjectIdentifier
_CurrentAlarmObject_Object = MibTableColumn
currentAlarmObject = _CurrentAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 4),
    _CurrentAlarmObject_Type()
)
currentAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmObject.setStatus("current")
_CurrentAlarmCause_Type = DisplayString
_CurrentAlarmCause_Object = MibTableColumn
currentAlarmCause = _CurrentAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 5),
    _CurrentAlarmCause_Type()
)
currentAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmCause.setStatus("current")
_CurrentAlarmTime_Type = DateAndTime
_CurrentAlarmTime_Object = MibTableColumn
currentAlarmTime = _CurrentAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 3, 3, 1, 6),
    _CurrentAlarmTime_Type()
)
currentAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmTime.setStatus("current")
_IsdMonitor_ObjectIdentity = ObjectIdentity
isdMonitor = _IsdMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    isdMonitor.setStatus("current")
_IsdResourceTable_Object = MibTable
isdResourceTable = _IsdResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isdResourceTable.setStatus("current")
_IsdResourceEntry_Object = MibTableRow
isdResourceEntry = _IsdResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1)
)
isdResourceEntry.setIndexNames(
    (0, "ALTEON-ISD-PLATFORM-MIB", "isdIndex"),
)
if mibBuilder.loadTexts:
    isdResourceEntry.setStatus("current")
_IsdResourceUptime_Type = TimeTicks
_IsdResourceUptime_Object = MibTableColumn
isdResourceUptime = _IsdResourceUptime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 1),
    _IsdResourceUptime_Type()
)
isdResourceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdResourceUptime.setStatus("current")


class _IsdResourceCpu_Type(Gauge32):
    """Custom type isdResourceCpu based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IsdResourceCpu_Type.__name__ = "Gauge32"
_IsdResourceCpu_Object = MibTableColumn
isdResourceCpu = _IsdResourceCpu_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 2),
    _IsdResourceCpu_Type()
)
isdResourceCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdResourceCpu.setStatus("current")


class _IsdResourceMemory_Type(Gauge32):
    """Custom type isdResourceMemory based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IsdResourceMemory_Type.__name__ = "Gauge32"
_IsdResourceMemory_Object = MibTableColumn
isdResourceMemory = _IsdResourceMemory_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 3),
    _IsdResourceMemory_Type()
)
isdResourceMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdResourceMemory.setStatus("current")


class _IsdResourceDisk_Type(Gauge32):
    """Custom type isdResourceDisk based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IsdResourceDisk_Type.__name__ = "Gauge32"
_IsdResourceDisk_Object = MibTableColumn
isdResourceDisk = _IsdResourceDisk_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 1, 5, 1, 1, 4),
    _IsdResourceDisk_Type()
)
isdResourceDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdResourceDisk.setStatus("current")
_IsdNotifications_ObjectIdentity = ObjectIdentity
isdNotifications = _IsdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    isdNotifications.setStatus("current")
_IsdEvents_ObjectIdentity = ObjectIdentity
isdEvents = _IsdEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    isdEvents.setStatus("current")
_IsdAlarms_ObjectIdentity = ObjectIdentity
isdAlarms = _IsdAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    isdAlarms.setStatus("current")
_IsdNotificationObjects_ObjectIdentity = ObjectIdentity
isdNotificationObjects = _IsdNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    isdNotificationObjects.setStatus("current")
_IsdEventTime_Type = DateAndTime
_IsdEventTime_Object = MibScalar
isdEventTime = _IsdEventTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 1),
    _IsdEventTime_Type()
)
isdEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isdEventTime.setStatus("current")
_IsdEventDescription_Type = DisplayString
_IsdEventDescription_Object = MibScalar
isdEventDescription = _IsdEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 2),
    _IsdEventDescription_Type()
)
isdEventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isdEventDescription.setStatus("current")


class _IsdUtilization_Type(Gauge32):
    """Custom type isdUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IsdUtilization_Type.__name__ = "Gauge32"
_IsdUtilization_Object = MibScalar
isdUtilization = _IsdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 3),
    _IsdUtilization_Type()
)
isdUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isdUtilization.setStatus("current")
_IsdLoad_Type = Gauge32
_IsdLoad_Object = MibScalar
isdLoad = _IsdLoad_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 4, 4),
    _IsdLoad_Type()
)
isdLoad.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    isdLoad.setStatus("current")

# Managed Objects groups


# Notification objects

isdAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 1)
)
isdAlarmCleared.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmOid"))
)
if mibBuilder.loadTexts:
    isdAlarmCleared.setStatus(
        "current"
    )

isdTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 2)
)
isdTopologyChange.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdEventDescription"))
)
if mibBuilder.loadTexts:
    isdTopologyChange.setStatus(
        "current"
    )

isdAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 4)
)
isdAuthenticationFailure.setObjects(
    ("ALTEON-ISD-PLATFORM-MIB", "isdEventTime")
)
if mibBuilder.loadTexts:
    isdAuthenticationFailure.setStatus(
        "current"
    )

isdMipMigration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 1, 5)
)
isdMipMigration.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "isdEventTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
)
if mibBuilder.loadTexts:
    isdMipMigration.setStatus(
        "current"
    )

isdDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 1)
)
isdDown.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
)
if mibBuilder.loadTexts:
    isdDown.setStatus(
        "current"
    )

isdUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 2)
)
isdUp.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdIP"))
)
if mibBuilder.loadTexts:
    isdUp.setStatus(
        "current"
    )

isdSingleMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 3)
)
isdSingleMaster.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"))
)
if mibBuilder.loadTexts:
    isdSingleMaster.setStatus(
        "current"
    )

isdMemoryStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 4)
)
isdMemoryStateChange.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdIP"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdUtilization"))
)
if mibBuilder.loadTexts:
    isdMemoryStateChange.setStatus(
        "current"
    )

isdCpuStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 5)
)
isdCpuStateChange.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdIP"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdLoad"))
)
if mibBuilder.loadTexts:
    isdCpuStateChange.setStatus(
        "current"
    )

isdDiskStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 1, 2, 3, 2, 6)
)
isdDiskStateChange.setObjects(
      *(("ALTEON-ISD-PLATFORM-MIB", "currentAlarmSeverity"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmTime"),
        ("ALTEON-ISD-PLATFORM-MIB", "currentAlarmCause"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdIP"),
        ("ALTEON-ISD-PLATFORM-MIB", "isdUtilization"))
)
if mibBuilder.loadTexts:
    isdDiskStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-ISD-PLATFORM-MIB",
    **{"AlarmSeverity": AlarmSeverity,
       "alteonPlatformISDModule": alteonPlatformISDModule,
       "alteonISDPlatformMIB": alteonISDPlatformMIB,
       "isdObjects": isdObjects,
       "isdCluster": isdCluster,
       "isdClusterTable": isdClusterTable,
       "isdClusterEntry": isdClusterEntry,
       "isdIndex": isdIndex,
       "isdIP": isdIP,
       "isdType": isdType,
       "isdOperStatus": isdOperStatus,
       "isdMIPOwner": isdMIPOwner,
       "isdCurrentTime": isdCurrentTime,
       "isdVersion": isdVersion,
       "isdImageTable": isdImageTable,
       "isdImageEntry": isdImageEntry,
       "isdImageIndex": isdImageIndex,
       "isdImageVersion": isdImageVersion,
       "isdImageName": isdImageName,
       "isdImageStatus": isdImageStatus,
       "isdClusterMIP": isdClusterMIP,
       "isdClusterMask": isdClusterMask,
       "currentAlarm": currentAlarm,
       "numberOfCurrentAlarms": numberOfCurrentAlarms,
       "currentAlarmLastTimeChanged": currentAlarmLastTimeChanged,
       "currentAlarmTable": currentAlarmTable,
       "currentAlarmEntry": currentAlarmEntry,
       "currentAlarmIndex": currentAlarmIndex,
       "currentAlarmSeverity": currentAlarmSeverity,
       "currentAlarmOid": currentAlarmOid,
       "currentAlarmObject": currentAlarmObject,
       "currentAlarmCause": currentAlarmCause,
       "currentAlarmTime": currentAlarmTime,
       "isdMonitor": isdMonitor,
       "isdResourceTable": isdResourceTable,
       "isdResourceEntry": isdResourceEntry,
       "isdResourceUptime": isdResourceUptime,
       "isdResourceCpu": isdResourceCpu,
       "isdResourceMemory": isdResourceMemory,
       "isdResourceDisk": isdResourceDisk,
       "isdNotifications": isdNotifications,
       "isdEvents": isdEvents,
       "isdAlarmCleared": isdAlarmCleared,
       "isdTopologyChange": isdTopologyChange,
       "isdAuthenticationFailure": isdAuthenticationFailure,
       "isdMipMigration": isdMipMigration,
       "isdAlarms": isdAlarms,
       "isdDown": isdDown,
       "isdUp": isdUp,
       "isdSingleMaster": isdSingleMaster,
       "isdMemoryStateChange": isdMemoryStateChange,
       "isdCpuStateChange": isdCpuStateChange,
       "isdDiskStateChange": isdDiskStateChange,
       "isdNotificationObjects": isdNotificationObjects,
       "isdEventTime": isdEventTime,
       "isdEventDescription": isdEventDescription,
       "isdUtilization": isdUtilization,
       "isdLoad": isdLoad}
)
