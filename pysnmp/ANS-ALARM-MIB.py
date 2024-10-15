# SNMP MIB module (ANS-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANS-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:56 2024
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

(DateAndTime,
 RowStatus,
 mlpmpR115) = mibBuilder.importSymbols(
    "ANS-COMMON-MIB",
    "DateAndTime",
    "RowStatus",
    "mlpmpR115")

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


# Types definitions



class AlarmSeverity(Integer32):
    """Custom type AlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 5),
          ("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )





class AlarmType(Integer32):
    """Custom type AlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("communications", 1),
          ("environmental", 5),
          ("equipment", 4),
          ("processing", 3),
          ("qos", 2),
          ("undefined", 0))
    )





class InstancePointer(ObjectIdentifier):
    """Custom type InstancePointer based on ObjectIdentifier"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EventAndAlarm_ObjectIdentity = ObjectIdentity
eventAndAlarm = _EventAndAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ANS-ALARM-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")


class _EventIndex_Type(Integer32):
    """Custom type eventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventIndex_Type.__name__ = "Integer32"
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("mandatory")


class _EventName_Type(DisplayString):
    """Custom type eventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventName_Type.__name__ = "DisplayString"
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1, 1, 2),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("mandatory")


class _EventTreatment_Type(Integer32):
    """Custom type eventTreatment based on Integer32"""
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
        *(("log", 2),
          ("log-and-trap", 4),
          ("none", 1),
          ("snmp-trap", 3))
    )


_EventTreatment_Type.__name__ = "Integer32"
_EventTreatment_Object = MibTableColumn
eventTreatment = _EventTreatment_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1, 1, 3),
    _EventTreatment_Type()
)
eventTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTreatment.setStatus("mandatory")


class _EventCommunity_Type(DisplayString):
    """Custom type eventCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventCommunity_Type.__name__ = "DisplayString"
_EventCommunity_Object = MibTableColumn
eventCommunity = _EventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1, 1, 4),
    _EventCommunity_Type()
)
eventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventCommunity.setStatus("mandatory")
_EventLastTimeSent_Type = DateAndTime
_EventLastTimeSent_Object = MibTableColumn
eventLastTimeSent = _EventLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1, 1, 5),
    _EventLastTimeSent_Type()
)
eventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLastTimeSent.setStatus("mandatory")


class _EventOwner_Type(DisplayString):
    """Custom type eventOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventOwner_Type.__name__ = "DisplayString"
_EventOwner_Object = MibTableColumn
eventOwner = _EventOwner_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 1, 1, 6),
    _EventOwner_Type()
)
eventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventOwner.setStatus("mandatory")


class _DiscriminateNtEvents_Type(Integer32):
    """Custom type discriminateNtEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_DiscriminateNtEvents_Type.__name__ = "Integer32"
_DiscriminateNtEvents_Object = MibScalar
discriminateNtEvents = _DiscriminateNtEvents_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 1, 2),
    _DiscriminateNtEvents_Type()
)
discriminateNtEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discriminateNtEvents.setStatus("mandatory")
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2)
)


class _LogAdminStatus_Type(Integer32):
    """Custom type logAdminStatus based on Integer32"""
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


_LogAdminStatus_Type.__name__ = "Integer32"
_LogAdminStatus_Object = MibScalar
logAdminStatus = _LogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 1),
    _LogAdminStatus_Type()
)
logAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logAdminStatus.setStatus("mandatory")
_LogSize_Type = Integer32
_LogSize_Object = MibScalar
logSize = _LogSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 2),
    _LogSize_Type()
)
logSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSize.setStatus("mandatory")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3)
)
if mibBuilder.loadTexts:
    logTable.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1)
)
logEntry.setIndexNames(
    (0, "ANS-ALARM-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")
_LogIndex_Type = Integer32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")


class _LogEventIndex_Type(Integer32):
    """Custom type logEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LogEventIndex_Type.__name__ = "Integer32"
_LogEventIndex_Object = MibTableColumn
logEventIndex = _LogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 2),
    _LogEventIndex_Type()
)
logEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventIndex.setStatus("mandatory")


class _LogEventName_Type(DisplayString):
    """Custom type logEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LogEventName_Type.__name__ = "DisplayString"
_LogEventName_Object = MibTableColumn
logEventName = _LogEventName_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 3),
    _LogEventName_Type()
)
logEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventName.setStatus("mandatory")
_LogEventGeneratingObject_Type = InstancePointer
_LogEventGeneratingObject_Object = MibTableColumn
logEventGeneratingObject = _LogEventGeneratingObject_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 4),
    _LogEventGeneratingObject_Type()
)
logEventGeneratingObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventGeneratingObject.setStatus("mandatory")
_LogTime_Type = DateAndTime
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 5),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("mandatory")


class _LogEventInformation_Type(DisplayString):
    """Custom type logEventInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogEventInformation_Type.__name__ = "DisplayString"
_LogEventInformation_Object = MibTableColumn
logEventInformation = _LogEventInformation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 6),
    _LogEventInformation_Type()
)
logEventInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventInformation.setStatus("mandatory")


class _LogEventType_Type(Integer32):
    """Custom type logEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("other", 2))
    )


_LogEventType_Type.__name__ = "Integer32"
_LogEventType_Object = MibTableColumn
logEventType = _LogEventType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 7),
    _LogEventType_Type()
)
logEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventType.setStatus("mandatory")
_LogAlarmType_Type = AlarmType
_LogAlarmType_Object = MibTableColumn
logAlarmType = _LogAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 8),
    _LogAlarmType_Type()
)
logAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAlarmType.setStatus("mandatory")
_LogAlarmSeverity_Type = AlarmSeverity
_LogAlarmSeverity_Object = MibTableColumn
logAlarmSeverity = _LogAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 2, 3, 1, 9),
    _LogAlarmSeverity_Type()
)
logAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAlarmSeverity.setStatus("mandatory")
_AlarmSeverityAssignment_ObjectIdentity = ObjectIdentity
alarmSeverityAssignment = _AlarmSeverityAssignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 3)
)
_AlarmSeverityAssignmentTable_Object = MibTable
alarmSeverityAssignmentTable = _AlarmSeverityAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 3, 1)
)
if mibBuilder.loadTexts:
    alarmSeverityAssignmentTable.setStatus("mandatory")
_AlarmSeverityAssignmentEntry_Object = MibTableRow
alarmSeverityAssignmentEntry = _AlarmSeverityAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 3, 1, 1)
)
alarmSeverityAssignmentEntry.setIndexNames(
    (0, "ANS-ALARM-MIB", "alarmSeverityIndex"),
)
if mibBuilder.loadTexts:
    alarmSeverityAssignmentEntry.setStatus("mandatory")


class _AlarmSeverityIndex_Type(Integer32):
    """Custom type alarmSeverityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlarmSeverityIndex_Type.__name__ = "Integer32"
_AlarmSeverityIndex_Object = MibTableColumn
alarmSeverityIndex = _AlarmSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 3, 1, 1, 1),
    _AlarmSeverityIndex_Type()
)
alarmSeverityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverityIndex.setStatus("mandatory")


class _AlarmSeverityAlarmName_Type(DisplayString):
    """Custom type alarmSeverityAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlarmSeverityAlarmName_Type.__name__ = "DisplayString"
_AlarmSeverityAlarmName_Object = MibTableColumn
alarmSeverityAlarmName = _AlarmSeverityAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 3, 1, 1, 2),
    _AlarmSeverityAlarmName_Type()
)
alarmSeverityAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverityAlarmName.setStatus("mandatory")
_AlarmSeverityPerceivedSeverity_Type = AlarmSeverity
_AlarmSeverityPerceivedSeverity_Object = MibTableColumn
alarmSeverityPerceivedSeverity = _AlarmSeverityPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 3, 1, 1, 3),
    _AlarmSeverityPerceivedSeverity_Type()
)
alarmSeverityPerceivedSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSeverityPerceivedSeverity.setStatus("mandatory")
_CurrentAlarm_ObjectIdentity = ObjectIdentity
currentAlarm = _CurrentAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4)
)
_NumberOfCurrentAlarms_Type = Integer32
_NumberOfCurrentAlarms_Object = MibScalar
numberOfCurrentAlarms = _NumberOfCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 1),
    _NumberOfCurrentAlarms_Type()
)
numberOfCurrentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfCurrentAlarms.setStatus("mandatory")
_CurrentAlarmTable_Object = MibTable
currentAlarmTable = _CurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2)
)
if mibBuilder.loadTexts:
    currentAlarmTable.setStatus("mandatory")
_CurrentAlarmEntry_Object = MibTableRow
currentAlarmEntry = _CurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1)
)
currentAlarmEntry.setIndexNames(
    (0, "ANS-ALARM-MIB", "currentAlarmIndex"),
)
if mibBuilder.loadTexts:
    currentAlarmEntry.setStatus("mandatory")
_CurrentAlarmIndex_Type = Integer32
_CurrentAlarmIndex_Object = MibTableColumn
currentAlarmIndex = _CurrentAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1, 1),
    _CurrentAlarmIndex_Type()
)
currentAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmIndex.setStatus("mandatory")


class _CurrentAlarmName_Type(DisplayString):
    """Custom type currentAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CurrentAlarmName_Type.__name__ = "DisplayString"
_CurrentAlarmName_Object = MibTableColumn
currentAlarmName = _CurrentAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1, 2),
    _CurrentAlarmName_Type()
)
currentAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmName.setStatus("mandatory")
_CurrentAlarmObject_Type = InstancePointer
_CurrentAlarmObject_Object = MibTableColumn
currentAlarmObject = _CurrentAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1, 3),
    _CurrentAlarmObject_Type()
)
currentAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmObject.setStatus("mandatory")
_CurrentAlarmType_Type = AlarmType
_CurrentAlarmType_Object = MibTableColumn
currentAlarmType = _CurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1, 4),
    _CurrentAlarmType_Type()
)
currentAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmType.setStatus("mandatory")
_CurrentAlarmSeverity_Type = AlarmSeverity
_CurrentAlarmSeverity_Object = MibTableColumn
currentAlarmSeverity = _CurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1, 5),
    _CurrentAlarmSeverity_Type()
)
currentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmSeverity.setStatus("mandatory")
_CurrentAlarmTime_Type = DateAndTime
_CurrentAlarmTime_Object = MibTableColumn
currentAlarmTime = _CurrentAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1, 6),
    _CurrentAlarmTime_Type()
)
currentAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmTime.setStatus("mandatory")


class _CurrentAlarmInformation_Type(DisplayString):
    """Custom type currentAlarmInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentAlarmInformation_Type.__name__ = "DisplayString"
_CurrentAlarmInformation_Object = MibTableColumn
currentAlarmInformation = _CurrentAlarmInformation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 2, 4, 2, 1, 7),
    _CurrentAlarmInformation_Type()
)
currentAlarmInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmInformation.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANS-ALARM-MIB",
    **{"AlarmSeverity": AlarmSeverity,
       "AlarmType": AlarmType,
       "InstancePointer": InstancePointer,
       "eventAndAlarm": eventAndAlarm,
       "event": event,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventName": eventName,
       "eventTreatment": eventTreatment,
       "eventCommunity": eventCommunity,
       "eventLastTimeSent": eventLastTimeSent,
       "eventOwner": eventOwner,
       "discriminateNtEvents": discriminateNtEvents,
       "log": log,
       "logAdminStatus": logAdminStatus,
       "logSize": logSize,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logEventIndex": logEventIndex,
       "logEventName": logEventName,
       "logEventGeneratingObject": logEventGeneratingObject,
       "logTime": logTime,
       "logEventInformation": logEventInformation,
       "logEventType": logEventType,
       "logAlarmType": logAlarmType,
       "logAlarmSeverity": logAlarmSeverity,
       "alarmSeverityAssignment": alarmSeverityAssignment,
       "alarmSeverityAssignmentTable": alarmSeverityAssignmentTable,
       "alarmSeverityAssignmentEntry": alarmSeverityAssignmentEntry,
       "alarmSeverityIndex": alarmSeverityIndex,
       "alarmSeverityAlarmName": alarmSeverityAlarmName,
       "alarmSeverityPerceivedSeverity": alarmSeverityPerceivedSeverity,
       "currentAlarm": currentAlarm,
       "numberOfCurrentAlarms": numberOfCurrentAlarms,
       "currentAlarmTable": currentAlarmTable,
       "currentAlarmEntry": currentAlarmEntry,
       "currentAlarmIndex": currentAlarmIndex,
       "currentAlarmName": currentAlarmName,
       "currentAlarmObject": currentAlarmObject,
       "currentAlarmType": currentAlarmType,
       "currentAlarmSeverity": currentAlarmSeverity,
       "currentAlarmTime": currentAlarmTime,
       "currentAlarmInformation": currentAlarmInformation}
)
