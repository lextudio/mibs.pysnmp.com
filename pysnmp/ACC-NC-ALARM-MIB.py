# SNMP MIB module (ACC-NC-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-NC-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:39 2024
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

(accNetController,) = mibBuilder.importSymbols(
    "ANDOVER-CONTROLS-MIB",
    "accNetController")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

accAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1)
)
accAlarmMIB.setRevisions(
        ("2002-10-30 09:46",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlarmListMax_Type = Integer32
_AlarmListMax_Object = MibScalar
alarmListMax = _AlarmListMax_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 1),
    _AlarmListMax_Type()
)
alarmListMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmListMax.setStatus("current")
_AlarmList_ObjectIdentity = ObjectIdentity
alarmList = _AlarmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1)
)
alarmEntry.setIndexNames(
    (0, "ACC-NC-ALARM-MIB", "alarmIENAD"),
    (0, "ACC-NC-ALARM-MIB", "alarmLink"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_AlarmControllerName_Type = DisplayString
_AlarmControllerName_Object = MibTableColumn
alarmControllerName = _AlarmControllerName_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 1),
    _AlarmControllerName_Type()
)
alarmControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmControllerName.setStatus("current")
_AlarmInfinetControllerName_Type = DisplayString
_AlarmInfinetControllerName_Object = MibTableColumn
alarmInfinetControllerName = _AlarmInfinetControllerName_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 2),
    _AlarmInfinetControllerName_Type()
)
alarmInfinetControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInfinetControllerName.setStatus("current")
_AlarmPointName_Type = DisplayString
_AlarmPointName_Object = MibTableColumn
alarmPointName = _AlarmPointName_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 3),
    _AlarmPointName_Type()
)
alarmPointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPointName.setStatus("current")
_AlarmPointDescription_Type = DisplayString
_AlarmPointDescription_Object = MibTableColumn
alarmPointDescription = _AlarmPointDescription_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 4),
    _AlarmPointDescription_Type()
)
alarmPointDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPointDescription.setStatus("current")
_AlarmAlarmName_Type = DisplayString
_AlarmAlarmName_Object = MibTableColumn
alarmAlarmName = _AlarmAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 5),
    _AlarmAlarmName_Type()
)
alarmAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAlarmName.setStatus("current")


class _AlarmState_Type(Integer32):
    """Custom type alarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alm", 2),
          ("null", 0),
          ("rtn", 1))
    )


_AlarmState_Type.__name__ = "Integer32"
_AlarmState_Object = MibTableColumn
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 6),
    _AlarmState_Type()
)
alarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")
_AlarmAlmTime_Type = DateAndTime
_AlarmAlmTime_Object = MibTableColumn
alarmAlmTime = _AlarmAlmTime_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 7),
    _AlarmAlmTime_Type()
)
alarmAlmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAlmTime.setStatus("current")
_AlarmAlmValue_Type = DisplayString
_AlarmAlmValue_Object = MibTableColumn
alarmAlmValue = _AlarmAlmValue_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 8),
    _AlarmAlmValue_Type()
)
alarmAlmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAlmValue.setStatus("current")
_AlarmRtnTime_Type = DateAndTime
_AlarmRtnTime_Object = MibTableColumn
alarmRtnTime = _AlarmRtnTime_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 9),
    _AlarmRtnTime_Type()
)
alarmRtnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRtnTime.setStatus("current")
_AlarmRtnValue_Type = DisplayString
_AlarmRtnValue_Object = MibTableColumn
alarmRtnValue = _AlarmRtnValue_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 10),
    _AlarmRtnValue_Type()
)
alarmRtnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmRtnValue.setStatus("current")


class _AlarmIENAD_Type(OctetString):
    """Custom type alarmIENAD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AlarmIENAD_Type.__name__ = "OctetString"
_AlarmIENAD_Object = MibTableColumn
alarmIENAD = _AlarmIENAD_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 12),
    _AlarmIENAD_Type()
)
alarmIENAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIENAD.setStatus("current")


class _AlarmLink_Type(Integer32):
    """Custom type alarmLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlarmLink_Type.__name__ = "Integer32"
_AlarmLink_Object = MibTableColumn
alarmLink = _AlarmLink_Object(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 2, 2, 1, 13),
    _AlarmLink_Type()
)
alarmLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLink.setStatus("current")
_AlarmConformance_ObjectIdentity = ObjectIdentity
alarmConformance = _AlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 4)
)
_AlarmCompliances_ObjectIdentity = ObjectIdentity
alarmCompliances = _AlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 4, 1)
)
_AlarmGroups_ObjectIdentity = ObjectIdentity
alarmGroups = _AlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 4, 2)
)

# Managed Objects groups

alarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 4, 2, 1)
)
alarmGroup.setObjects(
      *(("ACC-NC-ALARM-MIB", "alarmListMax"),
        ("ACC-NC-ALARM-MIB", "alarmControllerName"),
        ("ACC-NC-ALARM-MIB", "alarmInfinetControllerName"),
        ("ACC-NC-ALARM-MIB", "alarmPointName"),
        ("ACC-NC-ALARM-MIB", "alarmPointDescription"),
        ("ACC-NC-ALARM-MIB", "alarmAlarmName"),
        ("ACC-NC-ALARM-MIB", "alarmState"),
        ("ACC-NC-ALARM-MIB", "alarmAlmTime"),
        ("ACC-NC-ALARM-MIB", "alarmAlmValue"),
        ("ACC-NC-ALARM-MIB", "alarmRtnTime"),
        ("ACC-NC-ALARM-MIB", "alarmRtnValue"),
        ("ACC-NC-ALARM-MIB", "alarmIENAD"),
        ("ACC-NC-ALARM-MIB", "alarmLink"))
)
if mibBuilder.loadTexts:
    alarmGroup.setStatus("current")


# Notification objects

alarmTransitionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 3)
)
alarmTransitionEvent.setObjects(
      *(("ACC-NC-ALARM-MIB", "alarmControllerName"),
        ("ACC-NC-ALARM-MIB", "alarmInfinetControllerName"),
        ("ACC-NC-ALARM-MIB", "alarmPointName"),
        ("ACC-NC-ALARM-MIB", "alarmPointDescription"),
        ("ACC-NC-ALARM-MIB", "alarmAlarmName"),
        ("ACC-NC-ALARM-MIB", "alarmState"),
        ("ACC-NC-ALARM-MIB", "alarmAlmTime"),
        ("ACC-NC-ALARM-MIB", "alarmAlmValue"),
        ("ACC-NC-ALARM-MIB", "alarmRtnTime"),
        ("ACC-NC-ALARM-MIB", "alarmRtnValue"))
)
if mibBuilder.loadTexts:
    alarmTransitionEvent.setStatus(
        "current"
    )


# Notifications groups

alarmEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 4, 2, 2)
)
alarmEvents.setObjects(
    ("ACC-NC-ALARM-MIB", "alarmTransitionEvent")
)
if mibBuilder.loadTexts:
    alarmEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alarmBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    alarmBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-NC-ALARM-MIB",
    **{"accAlarmMIB": accAlarmMIB,
       "alarmListMax": alarmListMax,
       "alarmList": alarmList,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmControllerName": alarmControllerName,
       "alarmInfinetControllerName": alarmInfinetControllerName,
       "alarmPointName": alarmPointName,
       "alarmPointDescription": alarmPointDescription,
       "alarmAlarmName": alarmAlarmName,
       "alarmState": alarmState,
       "alarmAlmTime": alarmAlmTime,
       "alarmAlmValue": alarmAlmValue,
       "alarmRtnTime": alarmRtnTime,
       "alarmRtnValue": alarmRtnValue,
       "alarmIENAD": alarmIENAD,
       "alarmLink": alarmLink,
       "alarmTransitionEvent": alarmTransitionEvent,
       "alarmConformance": alarmConformance,
       "alarmCompliances": alarmCompliances,
       "alarmBasicCompliance": alarmBasicCompliance,
       "alarmGroups": alarmGroups,
       "alarmGroup": alarmGroup,
       "alarmEvents": alarmEvents}
)
