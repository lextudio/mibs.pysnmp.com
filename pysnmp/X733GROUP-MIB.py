# SNMP MIB module (X733GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/X733GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:39 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ewsdAlarms = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SiemensUnits_ObjectIdentity = ObjectIdentity
siemensUnits = _SiemensUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7)
)
_OenProductMibs_ObjectIdentity = ObjectIdentity
oenProductMibs = _OenProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1)
)
_Nms_ObjectIdentity = ObjectIdentity
nms = _Nms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3)
)
_NcProxy_ObjectIdentity = ObjectIdentity
ncProxy = _NcProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1)
)
_CommonGroup_ObjectIdentity = ObjectIdentity
commonGroup = _CommonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1)
)
_NeName_Type = DisplayString
_NeName_Object = MibScalar
neName = _NeName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 1),
    _NeName_Type()
)
neName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neName.setStatus("current")
_ManagedObjectClass_Type = DisplayString
_ManagedObjectClass_Object = MibScalar
managedObjectClass = _ManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 2),
    _ManagedObjectClass_Type()
)
managedObjectClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    managedObjectClass.setStatus("current")
_NotificationId_Type = DisplayString
_NotificationId_Object = MibScalar
notificationId = _NotificationId_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 3),
    _NotificationId_Type()
)
notificationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    notificationId.setStatus("current")


class _GlobalAlarmIds_Type(OctetString):
    """Custom type globalAlarmIds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_GlobalAlarmIds_Type.__name__ = "OctetString"
_GlobalAlarmIds_Object = MibScalar
globalAlarmIds = _GlobalAlarmIds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 1, 4),
    _GlobalAlarmIds_Type()
)
globalAlarmIds.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalAlarmIds.setStatus("current")
_ControlGroup_ObjectIdentity = ObjectIdentity
controlGroup = _ControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2)
)


class _SetPeriod_Type(Integer32):
    """Custom type setPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SetPeriod_Type.__name__ = "Integer32"
_SetPeriod_Object = MibScalar
setPeriod = _SetPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 1),
    _SetPeriod_Type()
)
setPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPeriod.setStatus("current")
_SendSummary_Type = DisplayString
_SendSummary_Object = MibScalar
sendSummary = _SendSummary_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 2),
    _SendSummary_Type()
)
sendSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendSummary.setStatus("current")
_ResendAlarm_Type = DisplayString
_ResendAlarm_Object = MibScalar
resendAlarm = _ResendAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 3),
    _ResendAlarm_Type()
)
resendAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resendAlarm.setStatus("current")


class _SendAllAlarms_Type(Integer32):
    """Custom type sendAllAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SendAllAlarms_Type.__name__ = "Integer32"
_SendAllAlarms_Object = MibScalar
sendAllAlarms = _SendAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 4),
    _SendAllAlarms_Type()
)
sendAllAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendAllAlarms.setStatus("current")


class _AlarmSpontan_Type(Integer32):
    """Custom type alarmSpontan based on Integer32"""
    defaultValue = 1

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


_AlarmSpontan_Type.__name__ = "Integer32"
_AlarmSpontan_Object = MibScalar
alarmSpontan = _AlarmSpontan_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 5),
    _AlarmSpontan_Type()
)
alarmSpontan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSpontan.setStatus("current")


class _CountAlarmPeriod_Type(Integer32):
    """Custom type countAlarmPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CountAlarmPeriod_Type.__name__ = "Integer32"
_CountAlarmPeriod_Object = MibScalar
countAlarmPeriod = _CountAlarmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 6),
    _CountAlarmPeriod_Type()
)
countAlarmPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countAlarmPeriod.setStatus("current")


class _CountAlarmSpontan_Type(Integer32):
    """Custom type countAlarmSpontan based on Integer32"""
    defaultValue = 2

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


_CountAlarmSpontan_Type.__name__ = "Integer32"
_CountAlarmSpontan_Object = MibScalar
countAlarmSpontan = _CountAlarmSpontan_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 2, 7),
    _CountAlarmSpontan_Type()
)
countAlarmSpontan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    countAlarmSpontan.setStatus("current")
_SummaryGroup_ObjectIdentity = ObjectIdentity
summaryGroup = _SummaryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3)
)
_NumberOfAlarms_Type = Integer32
_NumberOfAlarms_Object = MibScalar
numberOfAlarms = _NumberOfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 1),
    _NumberOfAlarms_Type()
)
numberOfAlarms.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numberOfAlarms.setStatus("current")


class _ConnectionReliable_Type(Integer32):
    """Custom type connectionReliable based on Integer32"""
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


_ConnectionReliable_Type.__name__ = "Integer32"
_ConnectionReliable_Object = MibScalar
connectionReliable = _ConnectionReliable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 2),
    _ConnectionReliable_Type()
)
connectionReliable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionReliable.setStatus("current")
_Critical_Type = Integer32
_Critical_Object = MibScalar
critical = _Critical_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 3),
    _Critical_Type()
)
critical.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    critical.setStatus("current")
_Major_Type = Integer32
_Major_Object = MibScalar
major = _Major_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 4),
    _Major_Type()
)
major.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    major.setStatus("current")
_Minor_Type = Integer32
_Minor_Object = MibScalar
minor = _Minor_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 3, 5),
    _Minor_Type()
)
minor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    minor.setStatus("current")
_MiscGroup_ObjectIdentity = ObjectIdentity
miscGroup = _MiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 4)
)


class _TimePeriod_Type(Integer32):
    """Custom type timePeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TimePeriod_Type.__name__ = "Integer32"
_TimePeriod_Object = MibScalar
timePeriod = _TimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 4, 3),
    _TimePeriod_Type()
)
timePeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timePeriod.setStatus("current")


class _Q3AlarmNumber_Type(Integer32):
    """Custom type q3AlarmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Q3AlarmNumber_Type.__name__ = "Integer32"
_Q3AlarmNumber_Object = MibScalar
q3AlarmNumber = _Q3AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 4, 4),
    _Q3AlarmNumber_Type()
)
q3AlarmNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    q3AlarmNumber.setStatus("current")
_X733Group_ObjectIdentity = ObjectIdentity
x733Group = _X733Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5)
)


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("communicationsAlarm", 2),
          ("enviromentalAlarm", 3),
          ("equipmentAlarm", 4),
          ("indeterminate", 0),
          ("integrityViolation", 5),
          ("operationalViolation", 8),
          ("physicalViolation", 9),
          ("processingErrorAlarm", 10),
          ("qualityOfServiceAlarm", 11),
          ("securityServiceOrMechanismViolation", 13),
          ("timeDomainViolation", 15))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibScalar
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 1),
    _EventType_Type()
)
eventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventType.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
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


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 2),
    _Severity_Type()
)
severity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_ProbableCause_Type = DisplayString
_ProbableCause_Object = MibScalar
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 3),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probableCause.setStatus("current")


class _OriginalAlarm_Type(OctetString):
    """Custom type originalAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_OriginalAlarm_Type.__name__ = "OctetString"
_OriginalAlarm_Object = MibScalar
originalAlarm = _OriginalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 4),
    _OriginalAlarm_Type()
)
originalAlarm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    originalAlarm.setStatus("current")


class _ProcessingStatus_Type(Integer32):
    """Custom type processingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 4),
          ("deferred", 3),
          ("in-process", 1),
          ("not-processed", 0),
          ("under-repair", 2))
    )


_ProcessingStatus_Type.__name__ = "Integer32"
_ProcessingStatus_Object = MibScalar
processingStatus = _ProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 5),
    _ProcessingStatus_Type()
)
processingStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    processingStatus.setStatus("current")
_AlarmClass_Type = DisplayString
_AlarmClass_Object = MibScalar
alarmClass = _AlarmClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 6),
    _AlarmClass_Type()
)
alarmClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmClass.setStatus("current")
_ManagedObjectInstance_Type = DisplayString
_ManagedObjectInstance_Object = MibScalar
managedObjectInstance = _ManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 7),
    _ManagedObjectInstance_Type()
)
managedObjectInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    managedObjectInstance.setStatus("current")


class _Rack_Type(Integer32):
    """Custom type rack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Rack_Type.__name__ = "Integer32"
_Rack_Object = MibScalar
rack = _Rack_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 8),
    _Rack_Type()
)
rack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rack.setStatus("current")


class _Shelf_Type(Integer32):
    """Custom type shelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Shelf_Type.__name__ = "Integer32"
_Shelf_Object = MibScalar
shelf = _Shelf_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 9),
    _Shelf_Type()
)
shelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shelf.setStatus("current")


class _FromCard_Type(Integer32):
    """Custom type fromCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_FromCard_Type.__name__ = "Integer32"
_FromCard_Object = MibScalar
fromCard = _FromCard_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 10),
    _FromCard_Type()
)
fromCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fromCard.setStatus("current")


class _ToCard_Type(Integer32):
    """Custom type toCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_ToCard_Type.__name__ = "Integer32"
_ToCard_Object = MibScalar
toCard = _ToCard_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 11),
    _ToCard_Type()
)
toCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    toCard.setStatus("current")


class _FromPort_Type(Integer32):
    """Custom type fromPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_FromPort_Type.__name__ = "Integer32"
_FromPort_Object = MibScalar
fromPort = _FromPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 12),
    _FromPort_Type()
)
fromPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fromPort.setStatus("current")


class _ToPort_Type(Integer32):
    """Custom type toPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_ToPort_Type.__name__ = "Integer32"
_ToPort_Object = MibScalar
toPort = _ToPort_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 13),
    _ToPort_Type()
)
toPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    toPort.setStatus("current")
_EventTime_Type = DisplayString
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 14),
    _EventTime_Type()
)
eventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_IpAddress_Type = DisplayString
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 15),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_TrapName_Type = DisplayString
_TrapName_Object = MibScalar
trapName = _TrapName_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 16),
    _TrapName_Type()
)
trapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapName.setStatus("current")
_SpecificProblems_Type = DisplayString
_SpecificProblems_Object = MibScalar
specificProblems = _SpecificProblems_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 17),
    _SpecificProblems_Type()
)
specificProblems.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    specificProblems.setStatus("current")


class _AdditionalText_Type(OctetString):
    """Custom type additionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_AdditionalText_Type.__name__ = "OctetString"
_AdditionalText_Object = MibScalar
additionalText = _AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 18),
    _AdditionalText_Type()
)
additionalText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    additionalText.setStatus("current")


class _AdditionalInformation_Type(OctetString):
    """Custom type additionalInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_AdditionalInformation_Type.__name__ = "OctetString"
_AdditionalInformation_Object = MibScalar
additionalInformation = _AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 19),
    _AdditionalInformation_Type()
)
additionalInformation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    additionalInformation.setStatus("current")
_Q3Group_ObjectIdentity = ObjectIdentity
q3Group = _Q3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6)
)


class _BackupStatus_Type(Integer32):
    """Custom type backupStatus based on Integer32"""
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


_BackupStatus_Type.__name__ = "Integer32"
_BackupStatus_Object = MibScalar
backupStatus = _BackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 1),
    _BackupStatus_Type()
)
backupStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    backupStatus.setStatus("current")
_BackupObject_Type = DisplayString
_BackupObject_Object = MibScalar
backupObject = _BackupObject_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 2),
    _BackupObject_Type()
)
backupObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    backupObject.setStatus("current")


class _TrendIndication_Type(Integer32):
    """Custom type trendIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lesssevere", 3),
          ("moresevere", 1),
          ("nochange", 2))
    )


_TrendIndication_Type.__name__ = "Integer32"
_TrendIndication_Object = MibScalar
trendIndication = _TrendIndication_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 3),
    _TrendIndication_Type()
)
trendIndication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trendIndication.setStatus("current")
_ThresholdInformation_Type = DisplayString
_ThresholdInformation_Object = MibScalar
thresholdInformation = _ThresholdInformation_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 4),
    _ThresholdInformation_Type()
)
thresholdInformation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdInformation.setStatus("current")


class _CorrelatedEvents_Type(OctetString):
    """Custom type correlatedEvents based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_CorrelatedEvents_Type.__name__ = "OctetString"
_CorrelatedEvents_Object = MibScalar
correlatedEvents = _CorrelatedEvents_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 5),
    _CorrelatedEvents_Type()
)
correlatedEvents.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    correlatedEvents.setStatus("current")
_StateChanges_Type = DisplayString
_StateChanges_Object = MibScalar
stateChanges = _StateChanges_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 6),
    _StateChanges_Type()
)
stateChanges.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stateChanges.setStatus("current")


class _MonitoredAttributes_Type(OctetString):
    """Custom type monitoredAttributes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_MonitoredAttributes_Type.__name__ = "OctetString"
_MonitoredAttributes_Object = MibScalar
monitoredAttributes = _MonitoredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 7),
    _MonitoredAttributes_Type()
)
monitoredAttributes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    monitoredAttributes.setStatus("current")
_SecurityAlarmDetector_Type = DisplayString
_SecurityAlarmDetector_Object = MibScalar
securityAlarmDetector = _SecurityAlarmDetector_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 8),
    _SecurityAlarmDetector_Type()
)
securityAlarmDetector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    securityAlarmDetector.setStatus("current")
_ServiceUser_Type = DisplayString
_ServiceUser_Object = MibScalar
serviceUser = _ServiceUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 9),
    _ServiceUser_Type()
)
serviceUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceUser.setStatus("current")
_ServiceProvider_Type = DisplayString
_ServiceProvider_Object = MibScalar
serviceProvider = _ServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 10),
    _ServiceProvider_Type()
)
serviceProvider.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceProvider.setStatus("current")


class _ListOfFaultyBoards_Type(OctetString):
    """Custom type listOfFaultyBoards based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_ListOfFaultyBoards_Type.__name__ = "OctetString"
_ListOfFaultyBoards_Object = MibScalar
listOfFaultyBoards = _ListOfFaultyBoards_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 6, 11),
    _ListOfFaultyBoards_Type()
)
listOfFaultyBoards.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    listOfFaultyBoards.setStatus("current")
_OsGroup_ObjectIdentity = ObjectIdentity
osGroup = _OsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7)
)
_MmnKey_Type = DisplayString
_MmnKey_Object = MibScalar
mmnKey = _MmnKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7, 1),
    _MmnKey_Type()
)
mmnKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mmnKey.setStatus("current")


class _ThresholdValue_Type(Integer32):
    """Custom type thresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ThresholdValue_Type.__name__ = "Integer32"
_ThresholdValue_Object = MibScalar
thresholdValue = _ThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7, 2),
    _ThresholdValue_Type()
)
thresholdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdValue.setStatus("current")


class _CurrentValue_Type(Integer32):
    """Custom type currentValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CurrentValue_Type.__name__ = "Integer32"
_CurrentValue_Object = MibScalar
currentValue = _CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 7, 3),
    _CurrentValue_Type()
)
currentValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentValue.setStatus("current")

# Managed Objects groups


# Notification objects

summaryAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 201)
)
summaryAlarms.setObjects(
      *(("X733GROUP-MIB", "neName"),
        ("X733GROUP-MIB", "numberOfAlarms"),
        ("X733GROUP-MIB", "connectionReliable"),
        ("X733GROUP-MIB", "globalAlarmIds"))
)
if mibBuilder.loadTexts:
    summaryAlarms.setStatus(
        "current"
    )

spontaneousAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 202)
)
spontaneousAlarms.setObjects(
      *(("X733GROUP-MIB", "neName"),
        ("X733GROUP-MIB", "managedObjectClass"),
        ("X733GROUP-MIB", "notificationId"),
        ("X733GROUP-MIB", "severity"),
        ("X733GROUP-MIB", "eventType"),
        ("X733GROUP-MIB", "eventTime"),
        ("X733GROUP-MIB", "probableCause"),
        ("X733GROUP-MIB", "processingStatus"),
        ("X733GROUP-MIB", "alarmClass"),
        ("X733GROUP-MIB", "managedObjectInstance"),
        ("X733GROUP-MIB", "rack"),
        ("X733GROUP-MIB", "shelf"),
        ("X733GROUP-MIB", "fromCard"),
        ("X733GROUP-MIB", "toCard"),
        ("X733GROUP-MIB", "fromPort"),
        ("X733GROUP-MIB", "toPort"),
        ("X733GROUP-MIB", "originalAlarm"))
)
if mibBuilder.loadTexts:
    spontaneousAlarms.setStatus(
        "current"
    )

snmpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 203)
)
snmpAlarm.setObjects(
      *(("X733GROUP-MIB", "neName"),
        ("X733GROUP-MIB", "notificationId"),
        ("X733GROUP-MIB", "severity"),
        ("X733GROUP-MIB", "eventType"),
        ("X733GROUP-MIB", "eventTime"),
        ("X733GROUP-MIB", "probableCause"),
        ("X733GROUP-MIB", "specificProblems"),
        ("X733GROUP-MIB", "managedObjectClass"),
        ("X733GROUP-MIB", "managedObjectInstance"),
        ("X733GROUP-MIB", "ipAddress"),
        ("X733GROUP-MIB", "trapName"),
        ("X733GROUP-MIB", "originalAlarm"))
)
if mibBuilder.loadTexts:
    snmpAlarm.setStatus(
        "current"
    )

q3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 204)
)
q3Alarm.setObjects(
      *(("X733GROUP-MIB", "neName"),
        ("X733GROUP-MIB", "notificationId"),
        ("X733GROUP-MIB", "q3AlarmNumber"),
        ("X733GROUP-MIB", "severity"),
        ("X733GROUP-MIB", "eventType"),
        ("X733GROUP-MIB", "eventTime"),
        ("X733GROUP-MIB", "probableCause"),
        ("X733GROUP-MIB", "specificProblems"),
        ("X733GROUP-MIB", "managedObjectClass"),
        ("X733GROUP-MIB", "managedObjectInstance"),
        ("X733GROUP-MIB", "additionalText"),
        ("X733GROUP-MIB", "additionalInformation"),
        ("X733GROUP-MIB", "backupStatus"),
        ("X733GROUP-MIB", "backupObject"),
        ("X733GROUP-MIB", "trendIndication"),
        ("X733GROUP-MIB", "thresholdInformation"),
        ("X733GROUP-MIB", "correlatedEvents"),
        ("X733GROUP-MIB", "stateChanges"),
        ("X733GROUP-MIB", "monitoredAttributes"),
        ("X733GROUP-MIB", "securityAlarmDetector"),
        ("X733GROUP-MIB", "serviceUser"),
        ("X733GROUP-MIB", "serviceProvider"),
        ("X733GROUP-MIB", "listOfFaultyBoards"),
        ("X733GROUP-MIB", "originalAlarm"))
)
if mibBuilder.loadTexts:
    q3Alarm.setStatus(
        "current"
    )

q3contAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 205)
)
q3contAlarm.setObjects(
      *(("X733GROUP-MIB", "neName"),
        ("X733GROUP-MIB", "notificationId"),
        ("X733GROUP-MIB", "q3AlarmNumber"),
        ("X733GROUP-MIB", "correlatedEvents"),
        ("X733GROUP-MIB", "monitoredAttributes"),
        ("X733GROUP-MIB", "listOfFaultyBoards"),
        ("X733GROUP-MIB", "originalAlarm"))
)
if mibBuilder.loadTexts:
    q3contAlarm.setStatus(
        "current"
    )

timeAckAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 206)
)
timeAckAlarms.setObjects(
    ("X733GROUP-MIB", "timePeriod")
)
if mibBuilder.loadTexts:
    timeAckAlarms.setStatus(
        "current"
    )

proxyStartUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 207)
)
if mibBuilder.loadTexts:
    proxyStartUp.setStatus(
        "current"
    )

countAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 208)
)
countAlarm.setObjects(
      *(("X733GROUP-MIB", "neName"),
        ("X733GROUP-MIB", "critical"),
        ("X733GROUP-MIB", "major"),
        ("X733GROUP-MIB", "minor"))
)
if mibBuilder.loadTexts:
    countAlarm.setStatus(
        "current"
    )

osAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 3, 1, 1, 5, 209)
)
osAlarm.setObjects(
      *(("X733GROUP-MIB", "neName"),
        ("X733GROUP-MIB", "notificationId"),
        ("X733GROUP-MIB", "severity"),
        ("X733GROUP-MIB", "eventType"),
        ("X733GROUP-MIB", "eventTime"),
        ("X733GROUP-MIB", "probableCause"),
        ("X733GROUP-MIB", "managedObjectClass"),
        ("X733GROUP-MIB", "managedObjectInstance"),
        ("X733GROUP-MIB", "mmnKey"),
        ("X733GROUP-MIB", "additionalText"),
        ("X733GROUP-MIB", "thresholdValue"),
        ("X733GROUP-MIB", "currentValue"),
        ("X733GROUP-MIB", "securityAlarmDetector"),
        ("X733GROUP-MIB", "serviceUser"),
        ("X733GROUP-MIB", "serviceProvider"))
)
if mibBuilder.loadTexts:
    osAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "X733GROUP-MIB",
    **{"sni": sni,
       "siemensUnits": siemensUnits,
       "oenProductMibs": oenProductMibs,
       "nms": nms,
       "ncProxy": ncProxy,
       "ewsdAlarms": ewsdAlarms,
       "commonGroup": commonGroup,
       "neName": neName,
       "managedObjectClass": managedObjectClass,
       "notificationId": notificationId,
       "globalAlarmIds": globalAlarmIds,
       "controlGroup": controlGroup,
       "setPeriod": setPeriod,
       "sendSummary": sendSummary,
       "resendAlarm": resendAlarm,
       "sendAllAlarms": sendAllAlarms,
       "alarmSpontan": alarmSpontan,
       "countAlarmPeriod": countAlarmPeriod,
       "countAlarmSpontan": countAlarmSpontan,
       "summaryGroup": summaryGroup,
       "numberOfAlarms": numberOfAlarms,
       "connectionReliable": connectionReliable,
       "critical": critical,
       "major": major,
       "minor": minor,
       "miscGroup": miscGroup,
       "timePeriod": timePeriod,
       "q3AlarmNumber": q3AlarmNumber,
       "x733Group": x733Group,
       "eventType": eventType,
       "severity": severity,
       "probableCause": probableCause,
       "originalAlarm": originalAlarm,
       "processingStatus": processingStatus,
       "alarmClass": alarmClass,
       "managedObjectInstance": managedObjectInstance,
       "rack": rack,
       "shelf": shelf,
       "fromCard": fromCard,
       "toCard": toCard,
       "fromPort": fromPort,
       "toPort": toPort,
       "eventTime": eventTime,
       "ipAddress": ipAddress,
       "trapName": trapName,
       "specificProblems": specificProblems,
       "additionalText": additionalText,
       "additionalInformation": additionalInformation,
       "summaryAlarms": summaryAlarms,
       "spontaneousAlarms": spontaneousAlarms,
       "snmpAlarm": snmpAlarm,
       "q3Alarm": q3Alarm,
       "q3contAlarm": q3contAlarm,
       "timeAckAlarms": timeAckAlarms,
       "proxyStartUp": proxyStartUp,
       "countAlarm": countAlarm,
       "osAlarm": osAlarm,
       "q3Group": q3Group,
       "backupStatus": backupStatus,
       "backupObject": backupObject,
       "trendIndication": trendIndication,
       "thresholdInformation": thresholdInformation,
       "correlatedEvents": correlatedEvents,
       "stateChanges": stateChanges,
       "monitoredAttributes": monitoredAttributes,
       "securityAlarmDetector": securityAlarmDetector,
       "serviceUser": serviceUser,
       "serviceProvider": serviceProvider,
       "listOfFaultyBoards": listOfFaultyBoards,
       "osGroup": osGroup,
       "mmnKey": mmnKey,
       "thresholdValue": thresholdValue,
       "currentValue": currentValue}
)
