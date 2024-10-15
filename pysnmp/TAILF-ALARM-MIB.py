# SNMP MIB module (TAILF-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TAILF-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:53 2024
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

(IANAItuEventType,) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(TfAlarmIndex,
 TfAlarmOperatorState,
 TfProbableCause,
 TfUtf8String,
 TfYANGResource) = mibBuilder.importSymbols(
    "TAILF-ALARM-TC-MIB",
    "TfAlarmIndex",
    "TfAlarmOperatorState",
    "TfProbableCause",
    "TfUtf8String",
    "TfYANGResource")

(tfModules,) = mibBuilder.importSymbols(
    "TAILF-TOP-MIB",
    "tfModules")


# MODULE-IDENTITY

tfAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103)
)
tfAlarmMIB.setRevisions(
        ("2012-08-30 00:00",
         "2011-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TfAlarmObjects_ObjectIdentity = ObjectIdentity
tfAlarmObjects = _TfAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1)
)
_TfAlarms_ObjectIdentity = ObjectIdentity
tfAlarms = _TfAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1)
)
_TfAlarmNumber_Type = Unsigned32
_TfAlarmNumber_Object = MibScalar
tfAlarmNumber = _TfAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 1),
    _TfAlarmNumber_Type()
)
tfAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmNumber.setStatus("current")
_TfAlarmLastChanged_Type = DateAndTime
_TfAlarmLastChanged_Object = MibScalar
tfAlarmLastChanged = _TfAlarmLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 2),
    _TfAlarmLastChanged_Type()
)
tfAlarmLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmLastChanged.setStatus("current")
_TfAlarmTable_Object = MibTable
tfAlarmTable = _TfAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tfAlarmTable.setStatus("current")
_TfAlarmEntry_Object = MibTableRow
tfAlarmEntry = _TfAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1)
)
tfAlarmEntry.setIndexNames(
    (0, "TAILF-ALARM-MIB", "tfAlarmIndex"),
)
if mibBuilder.loadTexts:
    tfAlarmEntry.setStatus("current")
_TfAlarmIndex_Type = TfAlarmIndex
_TfAlarmIndex_Object = MibTableColumn
tfAlarmIndex = _TfAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 1),
    _TfAlarmIndex_Type()
)
tfAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tfAlarmIndex.setStatus("current")
_TfAlarmType_Type = SnmpAdminString
_TfAlarmType_Object = MibTableColumn
tfAlarmType = _TfAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 2),
    _TfAlarmType_Type()
)
tfAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmType.setStatus("current")
_TfAlarmDevice_Type = SnmpAdminString
_TfAlarmDevice_Object = MibTableColumn
tfAlarmDevice = _TfAlarmDevice_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 3),
    _TfAlarmDevice_Type()
)
tfAlarmDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmDevice.setStatus("current")
_TfAlarmObject_Type = TfYANGResource
_TfAlarmObject_Object = MibTableColumn
tfAlarmObject = _TfAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 4),
    _TfAlarmObject_Type()
)
tfAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmObject.setStatus("current")
_TfAlarmObjectOID_Type = ObjectIdentifier
_TfAlarmObjectOID_Object = MibTableColumn
tfAlarmObjectOID = _TfAlarmObjectOID_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 5),
    _TfAlarmObjectOID_Type()
)
tfAlarmObjectOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmObjectOID.setStatus("current")
_TfAlarmObjectStr_Type = TfUtf8String
_TfAlarmObjectStr_Object = MibTableColumn
tfAlarmObjectStr = _TfAlarmObjectStr_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 6),
    _TfAlarmObjectStr_Type()
)
tfAlarmObjectStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmObjectStr.setStatus("current")
_TfAlarmSpecificProblem_Type = TfUtf8String
_TfAlarmSpecificProblem_Object = MibTableColumn
tfAlarmSpecificProblem = _TfAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 7),
    _TfAlarmSpecificProblem_Type()
)
tfAlarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmSpecificProblem.setStatus("current")
_TfAlarmEventType_Type = IANAItuEventType
_TfAlarmEventType_Object = MibTableColumn
tfAlarmEventType = _TfAlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 8),
    _TfAlarmEventType_Type()
)
tfAlarmEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmEventType.setStatus("current")
_TfAlarmProbableCause_Type = TfProbableCause
_TfAlarmProbableCause_Object = MibTableColumn
tfAlarmProbableCause = _TfAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 9),
    _TfAlarmProbableCause_Type()
)
tfAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmProbableCause.setStatus("current")
_TfAlarmOrigTime_Type = DateAndTime
_TfAlarmOrigTime_Object = MibTableColumn
tfAlarmOrigTime = _TfAlarmOrigTime_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 10),
    _TfAlarmOrigTime_Type()
)
tfAlarmOrigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmOrigTime.setStatus("current")
_TfAlarmTime_Type = DateAndTime
_TfAlarmTime_Object = MibTableColumn
tfAlarmTime = _TfAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 11),
    _TfAlarmTime_Type()
)
tfAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmTime.setStatus("current")
_TfAlarmSeverity_Type = ItuPerceivedSeverity
_TfAlarmSeverity_Object = MibTableColumn
tfAlarmSeverity = _TfAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 12),
    _TfAlarmSeverity_Type()
)
tfAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmSeverity.setStatus("current")
_TfAlarmCleared_Type = TruthValue
_TfAlarmCleared_Object = MibTableColumn
tfAlarmCleared = _TfAlarmCleared_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 13),
    _TfAlarmCleared_Type()
)
tfAlarmCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmCleared.setStatus("current")
_TfAlarmText_Type = TfUtf8String
_TfAlarmText_Object = MibTableColumn
tfAlarmText = _TfAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 14),
    _TfAlarmText_Type()
)
tfAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmText.setStatus("current")
_TfAlarmOperatorState_Type = TfAlarmOperatorState
_TfAlarmOperatorState_Object = MibTableColumn
tfAlarmOperatorState = _TfAlarmOperatorState_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 15),
    _TfAlarmOperatorState_Type()
)
tfAlarmOperatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmOperatorState.setStatus("current")
_TfAlarmOperatorNote_Type = TfUtf8String
_TfAlarmOperatorNote_Object = MibTableColumn
tfAlarmOperatorNote = _TfAlarmOperatorNote_Object(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 1, 1, 5, 1, 16),
    _TfAlarmOperatorNote_Type()
)
tfAlarmOperatorNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tfAlarmOperatorNote.setStatus("current")
_TfAlarmNotifications_ObjectIdentity = ObjectIdentity
tfAlarmNotifications = _TfAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2)
)
_TfAlarmNotifsPrefix_ObjectIdentity = ObjectIdentity
tfAlarmNotifsPrefix = _TfAlarmNotifsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0)
)
_TfAlarmConformance_ObjectIdentity = ObjectIdentity
tfAlarmConformance = _TfAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 10)
)
_TfAlarmCompliances_ObjectIdentity = ObjectIdentity
tfAlarmCompliances = _TfAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 1)
)
_TfAlarmGroups_ObjectIdentity = ObjectIdentity
tfAlarmGroups = _TfAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 2)
)

# Managed Objects groups

tfAlarmObjs = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 2, 2)
)
tfAlarmObjs.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmType"),
        ("TAILF-ALARM-MIB", "tfAlarmNumber"),
        ("TAILF-ALARM-MIB", "tfAlarmLastChanged"),
        ("TAILF-ALARM-MIB", "tfAlarmEventType"),
        ("TAILF-ALARM-MIB", "tfAlarmProbableCause"),
        ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"),
        ("TAILF-ALARM-MIB", "tfAlarmCleared"),
        ("TAILF-ALARM-MIB", "tfAlarmOperatorState"),
        ("TAILF-ALARM-MIB", "tfAlarmOperatorNote"),
        ("TAILF-ALARM-MIB", "tfAlarmDevice"),
        ("TAILF-ALARM-MIB", "tfAlarmObject"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectOID"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectStr"),
        ("TAILF-ALARM-MIB", "tfAlarmOrigTime"),
        ("TAILF-ALARM-MIB", "tfAlarmTime"),
        ("TAILF-ALARM-MIB", "tfAlarmSeverity"),
        ("TAILF-ALARM-MIB", "tfAlarmText"))
)
if mibBuilder.loadTexts:
    tfAlarmObjs.setStatus("current")


# Notification objects

tfAlarmIndeterminate = NotificationType(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 1)
)
tfAlarmIndeterminate.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmType"),
        ("TAILF-ALARM-MIB", "tfAlarmDevice"),
        ("TAILF-ALARM-MIB", "tfAlarmObject"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectOID"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectStr"),
        ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"),
        ("TAILF-ALARM-MIB", "tfAlarmEventType"),
        ("TAILF-ALARM-MIB", "tfAlarmProbableCause"),
        ("TAILF-ALARM-MIB", "tfAlarmTime"),
        ("TAILF-ALARM-MIB", "tfAlarmText"))
)
if mibBuilder.loadTexts:
    tfAlarmIndeterminate.setStatus(
        "current"
    )

tfAlarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 2)
)
tfAlarmWarning.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmType"),
        ("TAILF-ALARM-MIB", "tfAlarmDevice"),
        ("TAILF-ALARM-MIB", "tfAlarmObject"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectOID"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectStr"),
        ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"),
        ("TAILF-ALARM-MIB", "tfAlarmEventType"),
        ("TAILF-ALARM-MIB", "tfAlarmProbableCause"),
        ("TAILF-ALARM-MIB", "tfAlarmTime"),
        ("TAILF-ALARM-MIB", "tfAlarmText"))
)
if mibBuilder.loadTexts:
    tfAlarmWarning.setStatus(
        "current"
    )

tfAlarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 3)
)
tfAlarmMinor.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmType"),
        ("TAILF-ALARM-MIB", "tfAlarmDevice"),
        ("TAILF-ALARM-MIB", "tfAlarmObject"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectOID"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectStr"),
        ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"),
        ("TAILF-ALARM-MIB", "tfAlarmEventType"),
        ("TAILF-ALARM-MIB", "tfAlarmProbableCause"),
        ("TAILF-ALARM-MIB", "tfAlarmTime"),
        ("TAILF-ALARM-MIB", "tfAlarmText"))
)
if mibBuilder.loadTexts:
    tfAlarmMinor.setStatus(
        "current"
    )

tfAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 4)
)
tfAlarmMajor.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmType"),
        ("TAILF-ALARM-MIB", "tfAlarmDevice"),
        ("TAILF-ALARM-MIB", "tfAlarmObject"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectOID"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectStr"),
        ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"),
        ("TAILF-ALARM-MIB", "tfAlarmEventType"),
        ("TAILF-ALARM-MIB", "tfAlarmProbableCause"),
        ("TAILF-ALARM-MIB", "tfAlarmTime"),
        ("TAILF-ALARM-MIB", "tfAlarmText"))
)
if mibBuilder.loadTexts:
    tfAlarmMajor.setStatus(
        "current"
    )

tfAlarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 5)
)
tfAlarmCritical.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmType"),
        ("TAILF-ALARM-MIB", "tfAlarmDevice"),
        ("TAILF-ALARM-MIB", "tfAlarmObject"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectOID"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectStr"),
        ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"),
        ("TAILF-ALARM-MIB", "tfAlarmEventType"),
        ("TAILF-ALARM-MIB", "tfAlarmProbableCause"),
        ("TAILF-ALARM-MIB", "tfAlarmTime"),
        ("TAILF-ALARM-MIB", "tfAlarmText"))
)
if mibBuilder.loadTexts:
    tfAlarmCritical.setStatus(
        "current"
    )

tfAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 2, 0, 6)
)
tfAlarmClear.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmType"),
        ("TAILF-ALARM-MIB", "tfAlarmDevice"),
        ("TAILF-ALARM-MIB", "tfAlarmObject"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectOID"),
        ("TAILF-ALARM-MIB", "tfAlarmObjectStr"),
        ("TAILF-ALARM-MIB", "tfAlarmSpecificProblem"),
        ("TAILF-ALARM-MIB", "tfAlarmEventType"),
        ("TAILF-ALARM-MIB", "tfAlarmProbableCause"),
        ("TAILF-ALARM-MIB", "tfAlarmTime"),
        ("TAILF-ALARM-MIB", "tfAlarmText"))
)
if mibBuilder.loadTexts:
    tfAlarmClear.setStatus(
        "current"
    )


# Notifications groups

tfAlarmNotifs = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 2, 1)
)
tfAlarmNotifs.setObjects(
      *(("TAILF-ALARM-MIB", "tfAlarmIndeterminate"),
        ("TAILF-ALARM-MIB", "tfAlarmWarning"),
        ("TAILF-ALARM-MIB", "tfAlarmMinor"),
        ("TAILF-ALARM-MIB", "tfAlarmMajor"),
        ("TAILF-ALARM-MIB", "tfAlarmCritical"),
        ("TAILF-ALARM-MIB", "tfAlarmClear"))
)
if mibBuilder.loadTexts:
    tfAlarmNotifs.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tfAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 24961, 2, 103, 10, 1, 1)
)
if mibBuilder.loadTexts:
    tfAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAILF-ALARM-MIB",
    **{"tfAlarmMIB": tfAlarmMIB,
       "tfAlarmObjects": tfAlarmObjects,
       "tfAlarms": tfAlarms,
       "tfAlarmNumber": tfAlarmNumber,
       "tfAlarmLastChanged": tfAlarmLastChanged,
       "tfAlarmTable": tfAlarmTable,
       "tfAlarmEntry": tfAlarmEntry,
       "tfAlarmIndex": tfAlarmIndex,
       "tfAlarmType": tfAlarmType,
       "tfAlarmDevice": tfAlarmDevice,
       "tfAlarmObject": tfAlarmObject,
       "tfAlarmObjectOID": tfAlarmObjectOID,
       "tfAlarmObjectStr": tfAlarmObjectStr,
       "tfAlarmSpecificProblem": tfAlarmSpecificProblem,
       "tfAlarmEventType": tfAlarmEventType,
       "tfAlarmProbableCause": tfAlarmProbableCause,
       "tfAlarmOrigTime": tfAlarmOrigTime,
       "tfAlarmTime": tfAlarmTime,
       "tfAlarmSeverity": tfAlarmSeverity,
       "tfAlarmCleared": tfAlarmCleared,
       "tfAlarmText": tfAlarmText,
       "tfAlarmOperatorState": tfAlarmOperatorState,
       "tfAlarmOperatorNote": tfAlarmOperatorNote,
       "tfAlarmNotifications": tfAlarmNotifications,
       "tfAlarmNotifsPrefix": tfAlarmNotifsPrefix,
       "tfAlarmIndeterminate": tfAlarmIndeterminate,
       "tfAlarmWarning": tfAlarmWarning,
       "tfAlarmMinor": tfAlarmMinor,
       "tfAlarmMajor": tfAlarmMajor,
       "tfAlarmCritical": tfAlarmCritical,
       "tfAlarmClear": tfAlarmClear,
       "tfAlarmConformance": tfAlarmConformance,
       "tfAlarmCompliances": tfAlarmCompliances,
       "tfAlarmCompliance": tfAlarmCompliance,
       "tfAlarmGroups": tfAlarmGroups,
       "tfAlarmNotifs": tfAlarmNotifs,
       "tfAlarmObjs": tfAlarmObjs}
)
