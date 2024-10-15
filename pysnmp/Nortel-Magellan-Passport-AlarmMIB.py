# SNMP MIB module (Nortel-Magellan-Passport-AlarmMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AlarmMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:13 2024
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
 DisplayString,
 RowPointer,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "Unsigned32")

(AsciiString,
 DigitString,
 Hex,
 HexString) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "Hex",
    "HexString")

(passportMIBs,
 passportTraps) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs",
    "passportTraps")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlarmTrap_ObjectIdentity = ObjectIdentity
alarmTrap = _AlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2)
)
_MandatoryAlarmInfo_ObjectIdentity = ObjectIdentity
mandatoryAlarmInfo = _MandatoryAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7)
)
_ComponentRowPointer_Type = RowPointer
_ComponentRowPointer_Object = MibScalar
componentRowPointer = _ComponentRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 1),
    _ComponentRowPointer_Type()
)
componentRowPointer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentRowPointer.setStatus("mandatory")
_ComponentName_Type = DisplayString
_ComponentName_Object = MibScalar
componentName = _ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 2),
    _ComponentName_Type()
)
componentName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    componentName.setStatus("mandatory")
_EventTime_Type = DateAndTime
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 3),
    _EventTime_Type()
)
eventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTime.setStatus("mandatory")


class _ActiveListStatus_Type(Integer32):
    """Custom type activeListStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("message", 0),
          ("set", 1))
    )


_ActiveListStatus_Type.__name__ = "Integer32"
_ActiveListStatus_Object = MibScalar
activeListStatus = _ActiveListStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 4),
    _ActiveListStatus_Type()
)
activeListStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeListStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 5),
    _Severity_Type()
)
severity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    severity.setStatus("mandatory")


class _AlarmType_Type(Integer32):
    """Custom type alarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("communications", 0),
          ("debug", 7),
          ("environmental", 4),
          ("equipment", 3),
          ("operator", 6),
          ("processing", 2),
          ("qualityOfService", 1),
          ("security", 5),
          ("unknown", 8))
    )


_AlarmType_Type.__name__ = "Integer32"
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 6),
    _AlarmType_Type()
)
alarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmType.setStatus("mandatory")


class _ProbableCause_Type(Integer32):
    """Custom type probableCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              80,
              81,
              82,
              83,
              84,
              90,
              91,
              92,
              93,
              100,
              101,
              102,
              110,
              111,
              112,
              113,
              114,
              120,
              121,
              122,
              200,
              201,
              202,
              203,
              204)
        )
    )
    namedValues = NamedValues(
        *(("adapterError", 71),
          ("applicationSubsystemFailure", 50),
          ("atOrNearCapacity", 27),
          ("authenticationFailure", 110),
          ("bandwidthReduced", 22),
          ("breachOfConfidence", 111),
          ("cableTamper", 100),
          ("callEstablishmentError", 5),
          ("commProtocolError", 8),
          ("commSubsystemFailure", 7),
          ("configurationError", 51),
          ("congestion", 26),
          ("corruptData", 42),
          ("cpuCyclesLimitExceeded", 43),
          ("datasetModemError", 63),
          ("debugging", 201),
          ("degradedSignal", 6),
          ("delayedInfo", 120),
          ("denialOfService", 90),
          ("dteDceInterfaceError", 10),
          ("duplicateInfo", 80),
          ("equipmentFailure", 70),
          ("fileError", 47),
          ("framingError", 2),
          ("inactiveVirtualCircuit", 203),
          ("infoMissing", 81),
          ("infoModification", 82),
          ("infoOutOfSequence", 83),
          ("inputDeviceError", 68),
          ("intrusionDetection", 101),
          ("ioDeviceError", 69),
          ("keyExpired", 121),
          ("lanError", 9),
          ("localTransmissionError", 3),
          ("lossOfFrame", 1),
          ("lossOfSignal", 0),
          ("multiplexorProblem", 64),
          ("networkServerIntervention", 204),
          ("nonRepudiationFailure", 112),
          ("operationalCondition", 200),
          ("otherOperational", 93),
          ("otherPhysical", 102),
          ("otherSecurityService", 114),
          ("outOfHoursActivity", 122),
          ("outOfMemory", 48),
          ("outOfService", 91),
          ("outputDeviceError", 67),
          ("performanceDegraded", 25),
          ("powerProblem", 60),
          ("proceduralError", 92),
          ("processorProblem", 62),
          ("queueSizeExceeded", 21),
          ("receiverFailure", 65),
          ("remoteTransmissionError", 4),
          ("responseTimeExcessive", 20),
          ("retransmissionRateReduced", 23),
          ("softwareError", 44),
          ("softwareProgramError", 45),
          ("softwareProgramTermination", 46),
          ("storageCapacityProblem", 40),
          ("thresholdCrossed", 24),
          ("timingProblem", 61),
          ("transmitterFailure", 66),
          ("unauthorizedAccess", 113),
          ("underlyingResourceUnavail", 49),
          ("unexpectedInfo", 84),
          ("unknown", 202),
          ("versionMismatch", 41))
    )


_ProbableCause_Type.__name__ = "Integer32"
_ProbableCause_Object = MibScalar
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 7),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    probableCause.setStatus("mandatory")


class _NtpIndex_Type(DigitString):
    """Custom type ntpIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NtpIndex_Type.__name__ = "DigitString"
_NtpIndex_Object = MibScalar
ntpIndex = _NtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 8),
    _NtpIndex_Type()
)
ntpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpIndex.setStatus("mandatory")


class _CommentData_Type(AsciiString):
    """Custom type commentData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_CommentData_Type.__name__ = "AsciiString"
_CommentData_Object = MibScalar
commentData = _CommentData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 7, 9),
    _CommentData_Type()
)
commentData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    commentData.setStatus("mandatory")
_OptionalAlarmInfo_ObjectIdentity = ObjectIdentity
optionalAlarmInfo = _OptionalAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8)
)
_NotificationID_Type = Hex
_NotificationID_Object = MibScalar
notificationID = _NotificationID_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 1),
    _NotificationID_Type()
)
notificationID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    notificationID.setStatus("mandatory")
_LpForHierClear_Type = RowPointer
_LpForHierClear_Object = MibScalar
lpForHierClear = _LpForHierClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 2),
    _LpForHierClear_Type()
)
lpForHierClear.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpForHierClear.setStatus("mandatory")


class _OperatorData_Type(HexString):
    """Custom type operatorData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_OperatorData_Type.__name__ = "HexString"
_OperatorData_Object = MibScalar
operatorData = _OperatorData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 3),
    _OperatorData_Type()
)
operatorData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    operatorData.setStatus("mandatory")


class _Pid_Type(DisplayString):
    """Custom type pid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_Pid_Type.__name__ = "DisplayString"
_Pid_Object = MibScalar
pid = _Pid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 4),
    _Pid_Type()
)
pid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pid.setStatus("mandatory")
_FileName_Type = DisplayString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 5),
    _FileName_Type()
)
fileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileName.setStatus("mandatory")
_FileLineNumber_Type = Unsigned32
_FileLineNumber_Object = MibScalar
fileLineNumber = _FileLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 6),
    _FileLineNumber_Type()
)
fileLineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileLineNumber.setStatus("mandatory")
_FileVersion_Type = DisplayString
_FileVersion_Object = MibScalar
fileVersion = _FileVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 7),
    _FileVersion_Type()
)
fileVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileVersion.setStatus("mandatory")


class _InternalData_Type(HexString):
    """Custom type internalData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_InternalData_Type.__name__ = "HexString"
_InternalData_Object = MibScalar
internalData = _InternalData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 8, 8),
    _InternalData_Type()
)
internalData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    internalData.setStatus("mandatory")
_ProvisionalAlarmInfo_ObjectIdentity = ObjectIdentity
provisionalAlarmInfo = _ProvisionalAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 9)
)
_Cid_Type = Unsigned32
_Cid_Object = MibScalar
cid = _Cid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 9, 1),
    _Cid_Type()
)
cid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cid.setStatus("mandatory")
_AlarmMIB_ObjectIdentity = ObjectIdentity
alarmMIB = _AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 1)
)
_AlarmGroupBC_ObjectIdentity = ObjectIdentity
alarmGroupBC = _AlarmGroupBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 1, 3)
)
_AlarmGroupBC02_ObjectIdentity = ObjectIdentity
alarmGroupBC02 = _AlarmGroupBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 1, 3, 2)
)
_AlarmGroupBC02A_ObjectIdentity = ObjectIdentity
alarmGroupBC02A = _AlarmGroupBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 1, 3, 2, 2)
)
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 2)
)
_AlarmNotificationsGroupBC02A_ObjectIdentity = ObjectIdentity
alarmNotificationsGroupBC02A = _AlarmNotificationsGroupBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 2, 1)
)
_AlarmCapabilities_ObjectIdentity = ObjectIdentity
alarmCapabilities = _AlarmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 3)
)
_AlarmCapabilitiesBC_ObjectIdentity = ObjectIdentity
alarmCapabilitiesBC = _AlarmCapabilitiesBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 3, 3)
)
_AlarmCapabilitiesBC02_ObjectIdentity = ObjectIdentity
alarmCapabilitiesBC02 = _AlarmCapabilitiesBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 3, 3, 2)
)
_AlarmCapabilitiesBC02A_ObjectIdentity = ObjectIdentity
alarmCapabilitiesBC02A = _AlarmCapabilitiesBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 4, 3, 3, 2, 2)
)

# Managed Objects groups


# Notification objects

criticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 0, 1)
)
criticalAlarm.setObjects(
      *(("Nortel-Magellan-Passport-AlarmMIB", "componentRowPointer"),
        ("Nortel-Magellan-Passport-AlarmMIB", "componentName"),
        ("Nortel-Magellan-Passport-AlarmMIB", "eventTime"),
        ("Nortel-Magellan-Passport-AlarmMIB", "activeListStatus"),
        ("Nortel-Magellan-Passport-AlarmMIB", "severity"),
        ("Nortel-Magellan-Passport-AlarmMIB", "alarmType"),
        ("Nortel-Magellan-Passport-AlarmMIB", "probableCause"),
        ("Nortel-Magellan-Passport-AlarmMIB", "ntpIndex"),
        ("Nortel-Magellan-Passport-AlarmMIB", "commentData"))
)
if mibBuilder.loadTexts:
    criticalAlarm.setStatus(
        ""
    )

majorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 0, 2)
)
majorAlarm.setObjects(
      *(("Nortel-Magellan-Passport-AlarmMIB", "componentRowPointer"),
        ("Nortel-Magellan-Passport-AlarmMIB", "componentName"),
        ("Nortel-Magellan-Passport-AlarmMIB", "eventTime"),
        ("Nortel-Magellan-Passport-AlarmMIB", "activeListStatus"),
        ("Nortel-Magellan-Passport-AlarmMIB", "severity"),
        ("Nortel-Magellan-Passport-AlarmMIB", "alarmType"),
        ("Nortel-Magellan-Passport-AlarmMIB", "probableCause"),
        ("Nortel-Magellan-Passport-AlarmMIB", "ntpIndex"),
        ("Nortel-Magellan-Passport-AlarmMIB", "commentData"))
)
if mibBuilder.loadTexts:
    majorAlarm.setStatus(
        ""
    )

minorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 0, 3)
)
minorAlarm.setObjects(
      *(("Nortel-Magellan-Passport-AlarmMIB", "componentRowPointer"),
        ("Nortel-Magellan-Passport-AlarmMIB", "componentName"),
        ("Nortel-Magellan-Passport-AlarmMIB", "eventTime"),
        ("Nortel-Magellan-Passport-AlarmMIB", "activeListStatus"),
        ("Nortel-Magellan-Passport-AlarmMIB", "severity"),
        ("Nortel-Magellan-Passport-AlarmMIB", "alarmType"),
        ("Nortel-Magellan-Passport-AlarmMIB", "probableCause"),
        ("Nortel-Magellan-Passport-AlarmMIB", "ntpIndex"),
        ("Nortel-Magellan-Passport-AlarmMIB", "commentData"))
)
if mibBuilder.loadTexts:
    minorAlarm.setStatus(
        ""
    )

warningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 0, 4)
)
warningAlarm.setObjects(
      *(("Nortel-Magellan-Passport-AlarmMIB", "componentRowPointer"),
        ("Nortel-Magellan-Passport-AlarmMIB", "componentName"),
        ("Nortel-Magellan-Passport-AlarmMIB", "eventTime"),
        ("Nortel-Magellan-Passport-AlarmMIB", "activeListStatus"),
        ("Nortel-Magellan-Passport-AlarmMIB", "severity"),
        ("Nortel-Magellan-Passport-AlarmMIB", "alarmType"),
        ("Nortel-Magellan-Passport-AlarmMIB", "probableCause"),
        ("Nortel-Magellan-Passport-AlarmMIB", "ntpIndex"),
        ("Nortel-Magellan-Passport-AlarmMIB", "commentData"))
)
if mibBuilder.loadTexts:
    warningAlarm.setStatus(
        ""
    )

clearedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 0, 5)
)
clearedAlarm.setObjects(
      *(("Nortel-Magellan-Passport-AlarmMIB", "componentRowPointer"),
        ("Nortel-Magellan-Passport-AlarmMIB", "componentName"),
        ("Nortel-Magellan-Passport-AlarmMIB", "eventTime"),
        ("Nortel-Magellan-Passport-AlarmMIB", "activeListStatus"),
        ("Nortel-Magellan-Passport-AlarmMIB", "severity"),
        ("Nortel-Magellan-Passport-AlarmMIB", "alarmType"),
        ("Nortel-Magellan-Passport-AlarmMIB", "probableCause"),
        ("Nortel-Magellan-Passport-AlarmMIB", "ntpIndex"),
        ("Nortel-Magellan-Passport-AlarmMIB", "commentData"))
)
if mibBuilder.loadTexts:
    clearedAlarm.setStatus(
        ""
    )

indeterminateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 3, 2, 0, 6)
)
indeterminateAlarm.setObjects(
      *(("Nortel-Magellan-Passport-AlarmMIB", "componentRowPointer"),
        ("Nortel-Magellan-Passport-AlarmMIB", "componentName"),
        ("Nortel-Magellan-Passport-AlarmMIB", "eventTime"),
        ("Nortel-Magellan-Passport-AlarmMIB", "activeListStatus"),
        ("Nortel-Magellan-Passport-AlarmMIB", "severity"),
        ("Nortel-Magellan-Passport-AlarmMIB", "alarmType"),
        ("Nortel-Magellan-Passport-AlarmMIB", "probableCause"),
        ("Nortel-Magellan-Passport-AlarmMIB", "ntpIndex"),
        ("Nortel-Magellan-Passport-AlarmMIB", "commentData"))
)
if mibBuilder.loadTexts:
    indeterminateAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AlarmMIB",
    **{"alarmTrap": alarmTrap,
       "criticalAlarm": criticalAlarm,
       "majorAlarm": majorAlarm,
       "minorAlarm": minorAlarm,
       "warningAlarm": warningAlarm,
       "clearedAlarm": clearedAlarm,
       "indeterminateAlarm": indeterminateAlarm,
       "mandatoryAlarmInfo": mandatoryAlarmInfo,
       "componentRowPointer": componentRowPointer,
       "componentName": componentName,
       "eventTime": eventTime,
       "activeListStatus": activeListStatus,
       "severity": severity,
       "alarmType": alarmType,
       "probableCause": probableCause,
       "ntpIndex": ntpIndex,
       "commentData": commentData,
       "optionalAlarmInfo": optionalAlarmInfo,
       "notificationID": notificationID,
       "lpForHierClear": lpForHierClear,
       "operatorData": operatorData,
       "pid": pid,
       "fileName": fileName,
       "fileLineNumber": fileLineNumber,
       "fileVersion": fileVersion,
       "internalData": internalData,
       "provisionalAlarmInfo": provisionalAlarmInfo,
       "cid": cid,
       "alarmMIB": alarmMIB,
       "alarmGroup": alarmGroup,
       "alarmGroupBC": alarmGroupBC,
       "alarmGroupBC02": alarmGroupBC02,
       "alarmGroupBC02A": alarmGroupBC02A,
       "alarmNotifications": alarmNotifications,
       "alarmNotificationsGroupBC02A": alarmNotificationsGroupBC02A,
       "alarmCapabilities": alarmCapabilities,
       "alarmCapabilitiesBC": alarmCapabilitiesBC,
       "alarmCapabilitiesBC02": alarmCapabilitiesBC02,
       "alarmCapabilitiesBC02A": alarmCapabilitiesBC02A}
)
