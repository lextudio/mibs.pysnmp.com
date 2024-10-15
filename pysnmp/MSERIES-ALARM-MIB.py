# SNMP MIB module (MSERIES-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSERIES-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:54 2024
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

(mseries,) = mibBuilder.importSymbols(
    "MSERIES-MIB",
    "mseries")

(AlarmNotificationType,
 AlarmPerceivedSeverity,
 AlarmProbableCause,
 PortType,
 UnitType) = mibBuilder.importSymbols(
    "MSERIES-TC",
    "AlarmNotificationType",
    "AlarmPerceivedSeverity",
    "AlarmProbableCause",
    "PortType",
    "UnitType")

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

smartAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1)
)
smartAlarm.setRevisions(
        ("2014-02-12 14:15",
         "2013-10-15 13:41",
         "2011-12-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlarmGeneral_ObjectIdentity = ObjectIdentity
alarmGeneral = _AlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 1)
)
_SmartAlarmGeneralLastSeqNumber_Type = Counter32
_SmartAlarmGeneralLastSeqNumber_Object = MibScalar
smartAlarmGeneralLastSeqNumber = _SmartAlarmGeneralLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 1),
    _SmartAlarmGeneralLastSeqNumber_Type()
)
smartAlarmGeneralLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmGeneralLastSeqNumber.setStatus("current")
_SmartAlarmGeneralHighestSeverity_Type = AlarmPerceivedSeverity
_SmartAlarmGeneralHighestSeverity_Object = MibScalar
smartAlarmGeneralHighestSeverity = _SmartAlarmGeneralHighestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 2),
    _SmartAlarmGeneralHighestSeverity_Type()
)
smartAlarmGeneralHighestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmGeneralHighestSeverity.setStatus("current")
_SmartAlarmGeneralNumberActiveList_Type = Unsigned32
_SmartAlarmGeneralNumberActiveList_Object = MibScalar
smartAlarmGeneralNumberActiveList = _SmartAlarmGeneralNumberActiveList_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 3),
    _SmartAlarmGeneralNumberActiveList_Type()
)
smartAlarmGeneralNumberActiveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmGeneralNumberActiveList.setStatus("current")
_SmartAlarmGeneralNumberLogList_Type = Unsigned32
_SmartAlarmGeneralNumberLogList_Object = MibScalar
smartAlarmGeneralNumberLogList = _SmartAlarmGeneralNumberLogList_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 1, 4),
    _SmartAlarmGeneralNumberLogList_Type()
)
smartAlarmGeneralNumberLogList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmGeneralNumberLogList.setStatus("current")
_AlarmActiveList_ObjectIdentity = ObjectIdentity
alarmActiveList = _AlarmActiveList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2)
)
_AlarmActiveTable_Object = MibTable
alarmActiveTable = _AlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alarmActiveTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "MSERIES-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmIndex_Type(Unsigned32):
    """Custom type alarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmIndex_Type.__name__ = "Unsigned32"
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmUnit_Type = UnitType
_AlarmUnit_Object = MibTableColumn
alarmUnit = _AlarmUnit_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 2),
    _AlarmUnit_Type()
)
alarmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnit.setStatus("current")
_AlarmPort_Type = Integer32
_AlarmPort_Object = MibTableColumn
alarmPort = _AlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 3),
    _AlarmPort_Type()
)
alarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPort.setStatus("current")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibTableColumn
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 4),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("current")
_AlarmSeverity_Type = AlarmPerceivedSeverity
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 5),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmActivationTime_Type = DateAndTime
_AlarmActivationTime_Object = MibTableColumn
alarmActivationTime = _AlarmActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 6),
    _AlarmActivationTime_Type()
)
alarmActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActivationTime.setStatus("current")
_AlarmCeaseTime_Type = DateAndTime
_AlarmCeaseTime_Object = MibTableColumn
alarmCeaseTime = _AlarmCeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 7),
    _AlarmCeaseTime_Type()
)
alarmCeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCeaseTime.setStatus("current")
_AlarmSeqNumber_Type = Counter32
_AlarmSeqNumber_Object = MibTableColumn
alarmSeqNumber = _AlarmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 8),
    _AlarmSeqNumber_Type()
)
alarmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeqNumber.setStatus("current")
_AlarmHostName_Type = DisplayString
_AlarmHostName_Object = MibTableColumn
alarmHostName = _AlarmHostName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 9),
    _AlarmHostName_Type()
)
alarmHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmHostName.setStatus("current")
_AlarmPortName_Type = DisplayString
_AlarmPortName_Object = MibTableColumn
alarmPortName = _AlarmPortName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 10),
    _AlarmPortName_Type()
)
alarmPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPortName.setStatus("current")
_AlarmPortType_Type = PortType
_AlarmPortType_Object = MibTableColumn
alarmPortType = _AlarmPortType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 11),
    _AlarmPortType_Type()
)
alarmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPortType.setStatus("current")
_AlarmType_Type = AlarmNotificationType
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 12),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmCause_Type = AlarmProbableCause
_AlarmCause_Object = MibTableColumn
alarmCause = _AlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 13),
    _AlarmCause_Type()
)
alarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCause.setStatus("current")
_AlarmPortAlias_Type = DisplayString
_AlarmPortAlias_Object = MibTableColumn
alarmPortAlias = _AlarmPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 2, 1, 1, 14),
    _AlarmPortAlias_Type()
)
alarmPortAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPortAlias.setStatus("current")
_AlarmLogList_ObjectIdentity = ObjectIdentity
alarmLogList = _AlarmLogList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3)
)
_AlarmLogTable_Object = MibTable
alarmLogTable = _AlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alarmLogTable.setStatus("current")
_AlarmLogEntry_Object = MibTableRow
alarmLogEntry = _AlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1)
)
alarmLogEntry.setIndexNames(
    (0, "MSERIES-ALARM-MIB", "alarmLogIndex"),
)
if mibBuilder.loadTexts:
    alarmLogEntry.setStatus("current")


class _AlarmLogIndex_Type(Unsigned32):
    """Custom type alarmLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmLogIndex_Type.__name__ = "Unsigned32"
_AlarmLogIndex_Object = MibTableColumn
alarmLogIndex = _AlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 1),
    _AlarmLogIndex_Type()
)
alarmLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogIndex.setStatus("current")
_AlarmLogUnit_Type = UnitType
_AlarmLogUnit_Object = MibTableColumn
alarmLogUnit = _AlarmLogUnit_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 2),
    _AlarmLogUnit_Type()
)
alarmLogUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogUnit.setStatus("current")
_AlarmLogPort_Type = Integer32
_AlarmLogPort_Object = MibTableColumn
alarmLogPort = _AlarmLogPort_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 3),
    _AlarmLogPort_Type()
)
alarmLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogPort.setStatus("current")
_AlarmLogText_Type = DisplayString
_AlarmLogText_Object = MibTableColumn
alarmLogText = _AlarmLogText_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 4),
    _AlarmLogText_Type()
)
alarmLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogText.setStatus("current")
_AlarmLogSeverity_Type = AlarmPerceivedSeverity
_AlarmLogSeverity_Object = MibTableColumn
alarmLogSeverity = _AlarmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 5),
    _AlarmLogSeverity_Type()
)
alarmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogSeverity.setStatus("current")
_AlarmLogActivationTime_Type = DateAndTime
_AlarmLogActivationTime_Object = MibTableColumn
alarmLogActivationTime = _AlarmLogActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 6),
    _AlarmLogActivationTime_Type()
)
alarmLogActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogActivationTime.setStatus("current")
_AlarmLogCeaseTime_Type = DateAndTime
_AlarmLogCeaseTime_Object = MibTableColumn
alarmLogCeaseTime = _AlarmLogCeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 7),
    _AlarmLogCeaseTime_Type()
)
alarmLogCeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogCeaseTime.setStatus("current")
_AlarmLogSeqNumber_Type = Counter32
_AlarmLogSeqNumber_Object = MibTableColumn
alarmLogSeqNumber = _AlarmLogSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 8),
    _AlarmLogSeqNumber_Type()
)
alarmLogSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogSeqNumber.setStatus("current")
_AlarmLogHostName_Type = DisplayString
_AlarmLogHostName_Object = MibTableColumn
alarmLogHostName = _AlarmLogHostName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 9),
    _AlarmLogHostName_Type()
)
alarmLogHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogHostName.setStatus("current")
_AlarmLogPortName_Type = DisplayString
_AlarmLogPortName_Object = MibTableColumn
alarmLogPortName = _AlarmLogPortName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 10),
    _AlarmLogPortName_Type()
)
alarmLogPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogPortName.setStatus("current")
_AlarmLogPortType_Type = PortType
_AlarmLogPortType_Object = MibTableColumn
alarmLogPortType = _AlarmLogPortType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 11),
    _AlarmLogPortType_Type()
)
alarmLogPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogPortType.setStatus("current")
_AlarmLogType_Type = AlarmNotificationType
_AlarmLogType_Object = MibTableColumn
alarmLogType = _AlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 12),
    _AlarmLogType_Type()
)
alarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogType.setStatus("current")
_AlarmLogCause_Type = AlarmProbableCause
_AlarmLogCause_Object = MibTableColumn
alarmLogCause = _AlarmLogCause_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 3, 1, 1, 13),
    _AlarmLogCause_Type()
)
alarmLogCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLogCause.setStatus("current")
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 4)
)
_AlarmNotifyPrefix_ObjectIdentity = ObjectIdentity
alarmNotifyPrefix = _AlarmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0)
)
_SmartAlarmMIBConformance_ObjectIdentity = ObjectIdentity
smartAlarmMIBConformance = _SmartAlarmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5)
)
_SmartAlarmGroups_ObjectIdentity = ObjectIdentity
smartAlarmGroups = _SmartAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1)
)
_SmartAlarmCompliances_ObjectIdentity = ObjectIdentity
smartAlarmCompliances = _SmartAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 2)
)

# Managed Objects groups

smartAlarmGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 1)
)
smartAlarmGeneralGroupV1.setObjects(
      *(("MSERIES-ALARM-MIB", "smartAlarmGeneralLastSeqNumber"),
        ("MSERIES-ALARM-MIB", "smartAlarmGeneralHighestSeverity"),
        ("MSERIES-ALARM-MIB", "smartAlarmGeneralNumberActiveList"),
        ("MSERIES-ALARM-MIB", "smartAlarmGeneralNumberLogList"))
)
if mibBuilder.loadTexts:
    smartAlarmGeneralGroupV1.setStatus("current")

smartAlarmActiveTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 3)
)
smartAlarmActiveTableGroupV1.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmIndex"),
        ("MSERIES-ALARM-MIB", "alarmUnit"),
        ("MSERIES-ALARM-MIB", "alarmPort"),
        ("MSERIES-ALARM-MIB", "alarmText"),
        ("MSERIES-ALARM-MIB", "alarmSeverity"),
        ("MSERIES-ALARM-MIB", "alarmActivationTime"),
        ("MSERIES-ALARM-MIB", "alarmCeaseTime"),
        ("MSERIES-ALARM-MIB", "alarmSeqNumber"),
        ("MSERIES-ALARM-MIB", "alarmHostName"),
        ("MSERIES-ALARM-MIB", "alarmPortName"),
        ("MSERIES-ALARM-MIB", "alarmPortType"),
        ("MSERIES-ALARM-MIB", "alarmType"),
        ("MSERIES-ALARM-MIB", "alarmCause"))
)
if mibBuilder.loadTexts:
    smartAlarmActiveTableGroupV1.setStatus("current")

smartAlarmLogTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 4)
)
smartAlarmLogTableGroupV1.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmLogIndex"),
        ("MSERIES-ALARM-MIB", "alarmLogUnit"),
        ("MSERIES-ALARM-MIB", "alarmLogPort"),
        ("MSERIES-ALARM-MIB", "alarmLogText"),
        ("MSERIES-ALARM-MIB", "alarmLogSeverity"),
        ("MSERIES-ALARM-MIB", "alarmLogActivationTime"),
        ("MSERIES-ALARM-MIB", "alarmLogCeaseTime"),
        ("MSERIES-ALARM-MIB", "alarmLogSeqNumber"),
        ("MSERIES-ALARM-MIB", "alarmLogHostName"),
        ("MSERIES-ALARM-MIB", "alarmLogPortName"),
        ("MSERIES-ALARM-MIB", "alarmLogPortType"),
        ("MSERIES-ALARM-MIB", "alarmLogType"),
        ("MSERIES-ALARM-MIB", "alarmLogCause"))
)
if mibBuilder.loadTexts:
    smartAlarmLogTableGroupV1.setStatus("current")


# Notification objects

alarmNotificationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 1)
)
alarmNotificationCleared.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmIndex"),
        ("MSERIES-ALARM-MIB", "alarmUnit"),
        ("MSERIES-ALARM-MIB", "alarmPort"),
        ("MSERIES-ALARM-MIB", "alarmText"),
        ("MSERIES-ALARM-MIB", "alarmSeverity"),
        ("MSERIES-ALARM-MIB", "alarmActivationTime"),
        ("MSERIES-ALARM-MIB", "alarmCeaseTime"),
        ("MSERIES-ALARM-MIB", "alarmSeqNumber"),
        ("MSERIES-ALARM-MIB", "alarmHostName"),
        ("MSERIES-ALARM-MIB", "alarmPortName"),
        ("MSERIES-ALARM-MIB", "alarmPortType"),
        ("MSERIES-ALARM-MIB", "alarmPortAlias"))
)
if mibBuilder.loadTexts:
    alarmNotificationCleared.setStatus(
        "current"
    )

alarmNotificationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 2)
)
alarmNotificationWarning.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmIndex"),
        ("MSERIES-ALARM-MIB", "alarmUnit"),
        ("MSERIES-ALARM-MIB", "alarmPort"),
        ("MSERIES-ALARM-MIB", "alarmText"),
        ("MSERIES-ALARM-MIB", "alarmSeverity"),
        ("MSERIES-ALARM-MIB", "alarmActivationTime"),
        ("MSERIES-ALARM-MIB", "alarmCeaseTime"),
        ("MSERIES-ALARM-MIB", "alarmSeqNumber"),
        ("MSERIES-ALARM-MIB", "alarmHostName"),
        ("MSERIES-ALARM-MIB", "alarmPortName"),
        ("MSERIES-ALARM-MIB", "alarmPortType"),
        ("MSERIES-ALARM-MIB", "alarmPortAlias"))
)
if mibBuilder.loadTexts:
    alarmNotificationWarning.setStatus(
        "current"
    )

alarmNotificationMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 3)
)
alarmNotificationMinor.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmIndex"),
        ("MSERIES-ALARM-MIB", "alarmUnit"),
        ("MSERIES-ALARM-MIB", "alarmPort"),
        ("MSERIES-ALARM-MIB", "alarmText"),
        ("MSERIES-ALARM-MIB", "alarmSeverity"),
        ("MSERIES-ALARM-MIB", "alarmActivationTime"),
        ("MSERIES-ALARM-MIB", "alarmCeaseTime"),
        ("MSERIES-ALARM-MIB", "alarmSeqNumber"),
        ("MSERIES-ALARM-MIB", "alarmHostName"),
        ("MSERIES-ALARM-MIB", "alarmPortName"),
        ("MSERIES-ALARM-MIB", "alarmPortType"),
        ("MSERIES-ALARM-MIB", "alarmPortAlias"))
)
if mibBuilder.loadTexts:
    alarmNotificationMinor.setStatus(
        "current"
    )

alarmNotificationMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 4)
)
alarmNotificationMajor.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmIndex"),
        ("MSERIES-ALARM-MIB", "alarmUnit"),
        ("MSERIES-ALARM-MIB", "alarmPort"),
        ("MSERIES-ALARM-MIB", "alarmText"),
        ("MSERIES-ALARM-MIB", "alarmSeverity"),
        ("MSERIES-ALARM-MIB", "alarmActivationTime"),
        ("MSERIES-ALARM-MIB", "alarmCeaseTime"),
        ("MSERIES-ALARM-MIB", "alarmSeqNumber"),
        ("MSERIES-ALARM-MIB", "alarmHostName"),
        ("MSERIES-ALARM-MIB", "alarmPortName"),
        ("MSERIES-ALARM-MIB", "alarmPortType"),
        ("MSERIES-ALARM-MIB", "alarmPortAlias"))
)
if mibBuilder.loadTexts:
    alarmNotificationMajor.setStatus(
        "current"
    )

alarmNotificationCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 4, 0, 5)
)
alarmNotificationCritical.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmIndex"),
        ("MSERIES-ALARM-MIB", "alarmUnit"),
        ("MSERIES-ALARM-MIB", "alarmPort"),
        ("MSERIES-ALARM-MIB", "alarmText"),
        ("MSERIES-ALARM-MIB", "alarmSeverity"),
        ("MSERIES-ALARM-MIB", "alarmActivationTime"),
        ("MSERIES-ALARM-MIB", "alarmCeaseTime"),
        ("MSERIES-ALARM-MIB", "alarmSeqNumber"),
        ("MSERIES-ALARM-MIB", "alarmHostName"),
        ("MSERIES-ALARM-MIB", "alarmPortName"),
        ("MSERIES-ALARM-MIB", "alarmPortType"),
        ("MSERIES-ALARM-MIB", "alarmPortAlias"))
)
if mibBuilder.loadTexts:
    alarmNotificationCritical.setStatus(
        "current"
    )


# Notifications groups

smartAlarmNotificationGroupV1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 1, 2)
)
smartAlarmNotificationGroupV1.setObjects(
      *(("MSERIES-ALARM-MIB", "alarmNotificationCleared"),
        ("MSERIES-ALARM-MIB", "alarmNotificationCritical"),
        ("MSERIES-ALARM-MIB", "alarmNotificationMajor"),
        ("MSERIES-ALARM-MIB", "alarmNotificationMinor"),
        ("MSERIES-ALARM-MIB", "alarmNotificationWarning"))
)
if mibBuilder.loadTexts:
    smartAlarmNotificationGroupV1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

smartAlarmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    smartAlarmBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSERIES-ALARM-MIB",
    **{"smartAlarm": smartAlarm,
       "alarmGeneral": alarmGeneral,
       "smartAlarmGeneralLastSeqNumber": smartAlarmGeneralLastSeqNumber,
       "smartAlarmGeneralHighestSeverity": smartAlarmGeneralHighestSeverity,
       "smartAlarmGeneralNumberActiveList": smartAlarmGeneralNumberActiveList,
       "smartAlarmGeneralNumberLogList": smartAlarmGeneralNumberLogList,
       "alarmActiveList": alarmActiveList,
       "alarmActiveTable": alarmActiveTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmUnit": alarmUnit,
       "alarmPort": alarmPort,
       "alarmText": alarmText,
       "alarmSeverity": alarmSeverity,
       "alarmActivationTime": alarmActivationTime,
       "alarmCeaseTime": alarmCeaseTime,
       "alarmSeqNumber": alarmSeqNumber,
       "alarmHostName": alarmHostName,
       "alarmPortName": alarmPortName,
       "alarmPortType": alarmPortType,
       "alarmType": alarmType,
       "alarmCause": alarmCause,
       "alarmPortAlias": alarmPortAlias,
       "alarmLogList": alarmLogList,
       "alarmLogTable": alarmLogTable,
       "alarmLogEntry": alarmLogEntry,
       "alarmLogIndex": alarmLogIndex,
       "alarmLogUnit": alarmLogUnit,
       "alarmLogPort": alarmLogPort,
       "alarmLogText": alarmLogText,
       "alarmLogSeverity": alarmLogSeverity,
       "alarmLogActivationTime": alarmLogActivationTime,
       "alarmLogCeaseTime": alarmLogCeaseTime,
       "alarmLogSeqNumber": alarmLogSeqNumber,
       "alarmLogHostName": alarmLogHostName,
       "alarmLogPortName": alarmLogPortName,
       "alarmLogPortType": alarmLogPortType,
       "alarmLogType": alarmLogType,
       "alarmLogCause": alarmLogCause,
       "alarmNotifications": alarmNotifications,
       "alarmNotifyPrefix": alarmNotifyPrefix,
       "alarmNotificationCleared": alarmNotificationCleared,
       "alarmNotificationWarning": alarmNotificationWarning,
       "alarmNotificationMinor": alarmNotificationMinor,
       "alarmNotificationMajor": alarmNotificationMajor,
       "alarmNotificationCritical": alarmNotificationCritical,
       "smartAlarmMIBConformance": smartAlarmMIBConformance,
       "smartAlarmGroups": smartAlarmGroups,
       "smartAlarmGeneralGroupV1": smartAlarmGeneralGroupV1,
       "smartAlarmNotificationGroupV1": smartAlarmNotificationGroupV1,
       "smartAlarmActiveTableGroupV1": smartAlarmActiveTableGroupV1,
       "smartAlarmLogTableGroupV1": smartAlarmLogTableGroupV1,
       "smartAlarmCompliances": smartAlarmCompliances,
       "smartAlarmBasicComplV1": smartAlarmBasicComplV1}
)
