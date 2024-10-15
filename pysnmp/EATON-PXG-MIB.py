# SNMP MIB module (EATON-PXG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-PXG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:24 2024
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

(powerChain,) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "powerChain")

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

pxgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 1)
)
pxgMIB.setRevisions(
        ("2008-01-30 00:00",
         "2007-07-05 00:00",
         "2007-04-10 00:00",
         "2007-01-03 00:00",
         "2006-10-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxgNotifications_ObjectIdentity = ObjectIdentity
pxgNotifications = _PxgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0)
)
_PxgMIBObjects_ObjectIdentity = ObjectIdentity
pxgMIBObjects = _PxgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1)
)
_EventInfo_ObjectIdentity = ObjectIdentity
eventInfo = _EventInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 1)
)


class _EventID_Type(Integer32):
    """Custom type eventID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EventID_Type.__name__ = "Integer32"
_EventID_Object = MibScalar
eventID = _EventID_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 1, 1),
    _EventID_Type()
)
eventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventID.setStatus("current")


class _EventSequenceIndex_Type(Integer32):
    """Custom type eventSequenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EventSequenceIndex_Type.__name__ = "Integer32"
_EventSequenceIndex_Object = MibScalar
eventSequenceIndex = _EventSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 1, 2),
    _EventSequenceIndex_Type()
)
eventSequenceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSequenceIndex.setStatus("current")
_EventDescription_Type = SnmpAdminString
_EventDescription_Object = MibScalar
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 1, 3),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_EventValue_Type = SnmpAdminString
_EventValue_Object = MibScalar
eventValue = _EventValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 1, 4),
    _EventValue_Type()
)
eventValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventValue.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2)
)
_NumAlarmsPresent_Type = Gauge32
_NumAlarmsPresent_Object = MibScalar
numAlarmsPresent = _NumAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 1),
    _NumAlarmsPresent_Type()
)
numAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numAlarmsPresent.setStatus("current")
_ActiveAlarmsTable_Object = MibTable
activeAlarmsTable = _ActiveAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    activeAlarmsTable.setStatus("current")
_ActiveAlarmsEntry_Object = MibTableRow
activeAlarmsEntry = _ActiveAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2, 1)
)
activeAlarmsEntry.setIndexNames(
    (0, "EATON-PXG-MIB", "alarmID"),
)
if mibBuilder.loadTexts:
    activeAlarmsEntry.setStatus("current")


class _AlarmID_Type(Integer32):
    """Custom type alarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmID_Type.__name__ = "Integer32"
_AlarmID_Object = MibTableColumn
alarmID = _AlarmID_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2, 1, 1),
    _AlarmID_Type()
)
alarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmID.setStatus("current")


class _AlarmSequenceIndex_Type(Integer32):
    """Custom type alarmSequenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmSequenceIndex_Type.__name__ = "Integer32"
_AlarmSequenceIndex_Object = MibTableColumn
alarmSequenceIndex = _AlarmSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2, 1, 2),
    _AlarmSequenceIndex_Type()
)
alarmSequenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSequenceIndex.setStatus("current")
_AlarmDescription_Type = SnmpAdminString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2, 1, 3),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_AlarmValue_Type = SnmpAdminString
_AlarmValue_Object = MibTableColumn
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2, 1, 4),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("current")


class _AlarmLevel_Type(Integer32):
    """Custom type alarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 3),
          ("active", 4),
          ("cautionary", 2),
          ("cleared", 5),
          ("closed", 6),
          ("critical", 1),
          ("unknown", 7))
    )


_AlarmLevel_Type.__name__ = "Integer32"
_AlarmLevel_Object = MibTableColumn
alarmLevel = _AlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2, 1, 5),
    _AlarmLevel_Type()
)
alarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLevel.setStatus("current")
_AlarmTime_Type = TimeStamp
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 1, 2, 2, 1, 6),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_PxgConformance_ObjectIdentity = ObjectIdentity
pxgConformance = _PxgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 2)
)

# Managed Objects groups

tkEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 2, 1)
)
tkEventGroup.setObjects(
      *(("EATON-PXG-MIB", "eventID"),
        ("EATON-PXG-MIB", "eventSequenceIndex"),
        ("EATON-PXG-MIB", "eventDescription"),
        ("EATON-PXG-MIB", "eventValue"))
)
if mibBuilder.loadTexts:
    tkEventGroup.setStatus("current")

tkAlarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 2, 2)
)
tkAlarmTableGroup.setObjects(
      *(("EATON-PXG-MIB", "alarmID"),
        ("EATON-PXG-MIB", "alarmSequenceIndex"),
        ("EATON-PXG-MIB", "alarmDescription"),
        ("EATON-PXG-MIB", "alarmValue"),
        ("EATON-PXG-MIB", "alarmLevel"),
        ("EATON-PXG-MIB", "alarmTime"),
        ("EATON-PXG-MIB", "numAlarmsPresent"))
)
if mibBuilder.loadTexts:
    tkAlarmTableGroup.setStatus("current")


# Notification objects

powerChainCriticalAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 1)
)
powerChainCriticalAlarmEvent.setObjects(
      *(("EATON-PXG-MIB", "eventID"),
        ("EATON-PXG-MIB", "eventSequenceIndex"),
        ("EATON-PXG-MIB", "eventDescription"),
        ("EATON-PXG-MIB", "eventValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainCriticalAlarmEvent.setStatus(
        "current"
    )

powerChainCautionaryAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 2)
)
powerChainCautionaryAlarmEvent.setObjects(
      *(("EATON-PXG-MIB", "eventID"),
        ("EATON-PXG-MIB", "eventSequenceIndex"),
        ("EATON-PXG-MIB", "eventDescription"),
        ("EATON-PXG-MIB", "eventValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainCautionaryAlarmEvent.setStatus(
        "current"
    )

powerChainAlarmEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 3)
)
powerChainAlarmEventAcknowledged.setObjects(
      *(("EATON-PXG-MIB", "eventID"),
        ("EATON-PXG-MIB", "eventSequenceIndex"),
        ("EATON-PXG-MIB", "eventDescription"),
        ("EATON-PXG-MIB", "eventValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainAlarmEventAcknowledged.setStatus(
        "current"
    )

powerChainEventCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 4)
)
powerChainEventCleared.setObjects(
      *(("EATON-PXG-MIB", "eventID"),
        ("EATON-PXG-MIB", "eventSequenceIndex"),
        ("EATON-PXG-MIB", "eventDescription"),
        ("EATON-PXG-MIB", "eventValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainEventCleared.setStatus(
        "current"
    )

powerChainEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 5)
)
powerChainEvent.setObjects(
      *(("EATON-PXG-MIB", "eventID"),
        ("EATON-PXG-MIB", "eventSequenceIndex"),
        ("EATON-PXG-MIB", "eventDescription"),
        ("EATON-PXG-MIB", "eventValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainEvent.setStatus(
        "current"
    )

powerChainAlarmEventClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 6)
)
powerChainAlarmEventClosed.setObjects(
      *(("EATON-PXG-MIB", "eventID"),
        ("EATON-PXG-MIB", "eventSequenceIndex"),
        ("EATON-PXG-MIB", "eventDescription"),
        ("EATON-PXG-MIB", "eventValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainAlarmEventClosed.setStatus(
        "current"
    )

powerChainCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 7)
)
powerChainCriticalAlarm.setObjects(
      *(("EATON-PXG-MIB", "alarmID"),
        ("EATON-PXG-MIB", "alarmSequenceIndex"),
        ("EATON-PXG-MIB", "alarmDescription"),
        ("EATON-PXG-MIB", "alarmValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainCriticalAlarm.setStatus(
        "current"
    )

powerChainCautionaryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 8)
)
powerChainCautionaryAlarm.setObjects(
      *(("EATON-PXG-MIB", "alarmID"),
        ("EATON-PXG-MIB", "alarmSequenceIndex"),
        ("EATON-PXG-MIB", "alarmDescription"),
        ("EATON-PXG-MIB", "alarmValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainCautionaryAlarm.setStatus(
        "current"
    )

powerChainAlarmAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 9)
)
powerChainAlarmAcknowledged.setObjects(
      *(("EATON-PXG-MIB", "alarmID"),
        ("EATON-PXG-MIB", "alarmSequenceIndex"),
        ("EATON-PXG-MIB", "alarmDescription"),
        ("EATON-PXG-MIB", "alarmValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainAlarmAcknowledged.setStatus(
        "current"
    )

powerChainAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 10)
)
powerChainAlarmCleared.setObjects(
      *(("EATON-PXG-MIB", "alarmID"),
        ("EATON-PXG-MIB", "alarmSequenceIndex"),
        ("EATON-PXG-MIB", "alarmDescription"),
        ("EATON-PXG-MIB", "alarmValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainAlarmCleared.setStatus(
        "current"
    )

powerChainAlarmClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 11)
)
powerChainAlarmClosed.setObjects(
      *(("EATON-PXG-MIB", "alarmID"),
        ("EATON-PXG-MIB", "alarmSequenceIndex"),
        ("EATON-PXG-MIB", "alarmDescription"),
        ("EATON-PXG-MIB", "alarmValue"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainAlarmClosed.setStatus(
        "current"
    )

powerChainAlarmUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 0, 12)
)
powerChainAlarmUpdated.setObjects(
      *(("EATON-PXG-MIB", "alarmID"),
        ("EATON-PXG-MIB", "alarmSequenceIndex"),
        ("EATON-PXG-MIB", "alarmDescription"),
        ("EATON-PXG-MIB", "alarmValue"),
        ("EATON-PXG-MIB", "alarmLevel"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    powerChainAlarmUpdated.setStatus(
        "current"
    )


# Notifications groups

tkEventNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 2, 3)
)
tkEventNotifyGroup.setObjects(
      *(("EATON-PXG-MIB", "powerChainCriticalAlarmEvent"),
        ("EATON-PXG-MIB", "powerChainCautionaryAlarmEvent"),
        ("EATON-PXG-MIB", "powerChainAlarmEventAcknowledged"),
        ("EATON-PXG-MIB", "powerChainEventCleared"),
        ("EATON-PXG-MIB", "powerChainEvent"),
        ("EATON-PXG-MIB", "powerChainAlarmEventClosed"))
)
if mibBuilder.loadTexts:
    tkEventNotifyGroup.setStatus(
        "current"
    )

tkAlarmNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 2, 4)
)
tkAlarmNotifyGroup.setObjects(
      *(("EATON-PXG-MIB", "powerChainCriticalAlarm"),
        ("EATON-PXG-MIB", "powerChainCautionaryAlarm"),
        ("EATON-PXG-MIB", "powerChainAlarmAcknowledged"),
        ("EATON-PXG-MIB", "powerChainAlarmCleared"),
        ("EATON-PXG-MIB", "powerChainAlarmClosed"),
        ("EATON-PXG-MIB", "powerChainAlarmUpdated"))
)
if mibBuilder.loadTexts:
    tkAlarmNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tkSimpleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tkSimpleCompliance.setStatus(
        "current"
    )

tkAlarmsTableCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tkAlarmsTableCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-PXG-MIB",
    **{"pxgMIB": pxgMIB,
       "pxgNotifications": pxgNotifications,
       "powerChainCriticalAlarmEvent": powerChainCriticalAlarmEvent,
       "powerChainCautionaryAlarmEvent": powerChainCautionaryAlarmEvent,
       "powerChainAlarmEventAcknowledged": powerChainAlarmEventAcknowledged,
       "powerChainEventCleared": powerChainEventCleared,
       "powerChainEvent": powerChainEvent,
       "powerChainAlarmEventClosed": powerChainAlarmEventClosed,
       "powerChainCriticalAlarm": powerChainCriticalAlarm,
       "powerChainCautionaryAlarm": powerChainCautionaryAlarm,
       "powerChainAlarmAcknowledged": powerChainAlarmAcknowledged,
       "powerChainAlarmCleared": powerChainAlarmCleared,
       "powerChainAlarmClosed": powerChainAlarmClosed,
       "powerChainAlarmUpdated": powerChainAlarmUpdated,
       "pxgMIBObjects": pxgMIBObjects,
       "eventInfo": eventInfo,
       "eventID": eventID,
       "eventSequenceIndex": eventSequenceIndex,
       "eventDescription": eventDescription,
       "eventValue": eventValue,
       "alarms": alarms,
       "numAlarmsPresent": numAlarmsPresent,
       "activeAlarmsTable": activeAlarmsTable,
       "activeAlarmsEntry": activeAlarmsEntry,
       "alarmID": alarmID,
       "alarmSequenceIndex": alarmSequenceIndex,
       "alarmDescription": alarmDescription,
       "alarmValue": alarmValue,
       "alarmLevel": alarmLevel,
       "alarmTime": alarmTime,
       "pxgConformance": pxgConformance,
       "tkEventGroup": tkEventGroup,
       "tkAlarmTableGroup": tkAlarmTableGroup,
       "tkEventNotifyGroup": tkEventNotifyGroup,
       "tkAlarmNotifyGroup": tkAlarmNotifyGroup,
       "tkSimpleCompliance": tkSimpleCompliance,
       "tkAlarmsTableCompliance": tkAlarmsTableCompliance}
)
