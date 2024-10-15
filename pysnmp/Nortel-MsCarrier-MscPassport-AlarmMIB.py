# SNMP MIB module (Nortel-MsCarrier-MscPassport-AlarmMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AlarmMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:43 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "Unsigned32")

(AsciiString,
 DigitString,
 Hex,
 HexString) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "Hex",
    "HexString")

(mscPassportMIBs,
 mscPassportTraps) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs",
    "mscPassportTraps")

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

_MscAlarmTrap_ObjectIdentity = ObjectIdentity
mscAlarmTrap = _MscAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2)
)
_MscMandatoryAlarmInfo_ObjectIdentity = ObjectIdentity
mscMandatoryAlarmInfo = _MscMandatoryAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7)
)
_MscComponentRowPointer_Type = RowPointer
_MscComponentRowPointer_Object = MibScalar
mscComponentRowPointer = _MscComponentRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 1),
    _MscComponentRowPointer_Type()
)
mscComponentRowPointer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscComponentRowPointer.setStatus("mandatory")
_MscComponentName_Type = DisplayString
_MscComponentName_Object = MibScalar
mscComponentName = _MscComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 2),
    _MscComponentName_Type()
)
mscComponentName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscComponentName.setStatus("mandatory")
_MscEventTime_Type = DateAndTime
_MscEventTime_Object = MibScalar
mscEventTime = _MscEventTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 3),
    _MscEventTime_Type()
)
mscEventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscEventTime.setStatus("mandatory")


class _MscActiveListStatus_Type(Integer32):
    """Custom type mscActiveListStatus based on Integer32"""
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


_MscActiveListStatus_Type.__name__ = "Integer32"
_MscActiveListStatus_Object = MibScalar
mscActiveListStatus = _MscActiveListStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 4),
    _MscActiveListStatus_Type()
)
mscActiveListStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscActiveListStatus.setStatus("mandatory")


class _MscSeverity_Type(Integer32):
    """Custom type mscSeverity based on Integer32"""
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


_MscSeverity_Type.__name__ = "Integer32"
_MscSeverity_Object = MibScalar
mscSeverity = _MscSeverity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 5),
    _MscSeverity_Type()
)
mscSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscSeverity.setStatus("mandatory")


class _MscAlarmType_Type(Integer32):
    """Custom type mscAlarmType based on Integer32"""
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


_MscAlarmType_Type.__name__ = "Integer32"
_MscAlarmType_Object = MibScalar
mscAlarmType = _MscAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 6),
    _MscAlarmType_Type()
)
mscAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAlarmType.setStatus("mandatory")


class _MscProbableCause_Type(Integer32):
    """Custom type mscProbableCause based on Integer32"""
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


_MscProbableCause_Type.__name__ = "Integer32"
_MscProbableCause_Object = MibScalar
mscProbableCause = _MscProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 7),
    _MscProbableCause_Type()
)
mscProbableCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscProbableCause.setStatus("mandatory")


class _MscNtpIndex_Type(DigitString):
    """Custom type mscNtpIndex based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscNtpIndex_Type.__name__ = "DigitString"
_MscNtpIndex_Object = MibScalar
mscNtpIndex = _MscNtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 8),
    _MscNtpIndex_Type()
)
mscNtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNtpIndex.setStatus("mandatory")


class _MscCommentData_Type(AsciiString):
    """Custom type mscCommentData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_MscCommentData_Type.__name__ = "AsciiString"
_MscCommentData_Object = MibScalar
mscCommentData = _MscCommentData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 7, 9),
    _MscCommentData_Type()
)
mscCommentData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCommentData.setStatus("mandatory")
_MscOptionalAlarmInfo_ObjectIdentity = ObjectIdentity
mscOptionalAlarmInfo = _MscOptionalAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8)
)
_MscNotificationID_Type = Hex
_MscNotificationID_Object = MibScalar
mscNotificationID = _MscNotificationID_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 1),
    _MscNotificationID_Type()
)
mscNotificationID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNotificationID.setStatus("mandatory")
_MscLpForHierClear_Type = RowPointer
_MscLpForHierClear_Object = MibScalar
mscLpForHierClear = _MscLpForHierClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 2),
    _MscLpForHierClear_Type()
)
mscLpForHierClear.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpForHierClear.setStatus("mandatory")


class _MscOperatorData_Type(HexString):
    """Custom type mscOperatorData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_MscOperatorData_Type.__name__ = "HexString"
_MscOperatorData_Object = MibScalar
mscOperatorData = _MscOperatorData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 3),
    _MscOperatorData_Type()
)
mscOperatorData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscOperatorData.setStatus("mandatory")


class _MscPid_Type(DisplayString):
    """Custom type mscPid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_MscPid_Type.__name__ = "DisplayString"
_MscPid_Object = MibScalar
mscPid = _MscPid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 4),
    _MscPid_Type()
)
mscPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPid.setStatus("mandatory")
_MscFileName_Type = DisplayString
_MscFileName_Object = MibScalar
mscFileName = _MscFileName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 5),
    _MscFileName_Type()
)
mscFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFileName.setStatus("mandatory")
_MscFileLineNumber_Type = Unsigned32
_MscFileLineNumber_Object = MibScalar
mscFileLineNumber = _MscFileLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 6),
    _MscFileLineNumber_Type()
)
mscFileLineNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFileLineNumber.setStatus("mandatory")
_MscFileVersion_Type = DisplayString
_MscFileVersion_Object = MibScalar
mscFileVersion = _MscFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 7),
    _MscFileVersion_Type()
)
mscFileVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFileVersion.setStatus("mandatory")


class _MscInternalData_Type(HexString):
    """Custom type mscInternalData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_MscInternalData_Type.__name__ = "HexString"
_MscInternalData_Object = MibScalar
mscInternalData = _MscInternalData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 8, 8),
    _MscInternalData_Type()
)
mscInternalData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscInternalData.setStatus("mandatory")
_MscProvisionalAlarmInfo_ObjectIdentity = ObjectIdentity
mscProvisionalAlarmInfo = _MscProvisionalAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 9)
)
_MscCid_Type = Unsigned32
_MscCid_Object = MibScalar
mscCid = _MscCid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 9, 1),
    _MscCid_Type()
)
mscCid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscCid.setStatus("mandatory")
_AlarmMIB_ObjectIdentity = ObjectIdentity
alarmMIB = _AlarmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 1)
)
_AlarmGroupCA_ObjectIdentity = ObjectIdentity
alarmGroupCA = _AlarmGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 1, 1)
)
_AlarmGroupCA01_ObjectIdentity = ObjectIdentity
alarmGroupCA01 = _AlarmGroupCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 1, 1, 2)
)
_AlarmGroupCA01A_ObjectIdentity = ObjectIdentity
alarmGroupCA01A = _AlarmGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 1, 1, 2, 2)
)
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 2)
)
_AlarmNotificationsGroupCA01A_ObjectIdentity = ObjectIdentity
alarmNotificationsGroupCA01A = _AlarmNotificationsGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 2, 1)
)
_AlarmCapabilities_ObjectIdentity = ObjectIdentity
alarmCapabilities = _AlarmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 3)
)
_AlarmCapabilitiesCA_ObjectIdentity = ObjectIdentity
alarmCapabilitiesCA = _AlarmCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 3, 1)
)
_AlarmCapabilitiesCA01_ObjectIdentity = ObjectIdentity
alarmCapabilitiesCA01 = _AlarmCapabilitiesCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 3, 1, 2)
)
_AlarmCapabilitiesCA01A_ObjectIdentity = ObjectIdentity
alarmCapabilitiesCA01A = _AlarmCapabilitiesCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 4, 3, 1, 2, 2)
)

# Managed Objects groups


# Notification objects

mscCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 0, 1)
)
mscCriticalAlarm.setObjects(
      *(("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentRowPointer"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentName"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscEventTime"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscActiveListStatus"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscSeverity"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscAlarmType"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscProbableCause"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscNtpIndex"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscCommentData"))
)
if mibBuilder.loadTexts:
    mscCriticalAlarm.setStatus(
        ""
    )

mscMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 0, 2)
)
mscMajorAlarm.setObjects(
      *(("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentRowPointer"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentName"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscEventTime"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscActiveListStatus"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscSeverity"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscAlarmType"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscProbableCause"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscNtpIndex"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscCommentData"))
)
if mibBuilder.loadTexts:
    mscMajorAlarm.setStatus(
        ""
    )

mscMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 0, 3)
)
mscMinorAlarm.setObjects(
      *(("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentRowPointer"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentName"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscEventTime"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscActiveListStatus"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscSeverity"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscAlarmType"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscProbableCause"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscNtpIndex"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscCommentData"))
)
if mibBuilder.loadTexts:
    mscMinorAlarm.setStatus(
        ""
    )

mscWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 0, 4)
)
mscWarningAlarm.setObjects(
      *(("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentRowPointer"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentName"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscEventTime"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscActiveListStatus"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscSeverity"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscAlarmType"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscProbableCause"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscNtpIndex"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscCommentData"))
)
if mibBuilder.loadTexts:
    mscWarningAlarm.setStatus(
        ""
    )

mscClearedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 0, 5)
)
mscClearedAlarm.setObjects(
      *(("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentRowPointer"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentName"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscEventTime"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscActiveListStatus"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscSeverity"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscAlarmType"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscProbableCause"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscNtpIndex"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscCommentData"))
)
if mibBuilder.loadTexts:
    mscClearedAlarm.setStatus(
        ""
    )

mscIndeterminateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 3, 2, 0, 6)
)
mscIndeterminateAlarm.setObjects(
      *(("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentRowPointer"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscComponentName"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscEventTime"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscActiveListStatus"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscSeverity"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscAlarmType"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscProbableCause"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscNtpIndex"),
        ("Nortel-MsCarrier-MscPassport-AlarmMIB", "mscCommentData"))
)
if mibBuilder.loadTexts:
    mscIndeterminateAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AlarmMIB",
    **{"mscAlarmTrap": mscAlarmTrap,
       "mscCriticalAlarm": mscCriticalAlarm,
       "mscMajorAlarm": mscMajorAlarm,
       "mscMinorAlarm": mscMinorAlarm,
       "mscWarningAlarm": mscWarningAlarm,
       "mscClearedAlarm": mscClearedAlarm,
       "mscIndeterminateAlarm": mscIndeterminateAlarm,
       "mscMandatoryAlarmInfo": mscMandatoryAlarmInfo,
       "mscComponentRowPointer": mscComponentRowPointer,
       "mscComponentName": mscComponentName,
       "mscEventTime": mscEventTime,
       "mscActiveListStatus": mscActiveListStatus,
       "mscSeverity": mscSeverity,
       "mscAlarmType": mscAlarmType,
       "mscProbableCause": mscProbableCause,
       "mscNtpIndex": mscNtpIndex,
       "mscCommentData": mscCommentData,
       "mscOptionalAlarmInfo": mscOptionalAlarmInfo,
       "mscNotificationID": mscNotificationID,
       "mscLpForHierClear": mscLpForHierClear,
       "mscOperatorData": mscOperatorData,
       "mscPid": mscPid,
       "mscFileName": mscFileName,
       "mscFileLineNumber": mscFileLineNumber,
       "mscFileVersion": mscFileVersion,
       "mscInternalData": mscInternalData,
       "mscProvisionalAlarmInfo": mscProvisionalAlarmInfo,
       "mscCid": mscCid,
       "alarmMIB": alarmMIB,
       "alarmGroup": alarmGroup,
       "alarmGroupCA": alarmGroupCA,
       "alarmGroupCA01": alarmGroupCA01,
       "alarmGroupCA01A": alarmGroupCA01A,
       "alarmNotifications": alarmNotifications,
       "alarmNotificationsGroupCA01A": alarmNotificationsGroupCA01A,
       "alarmCapabilities": alarmCapabilities,
       "alarmCapabilitiesCA": alarmCapabilitiesCA,
       "alarmCapabilitiesCA01": alarmCapabilitiesCA01,
       "alarmCapabilitiesCA01A": alarmCapabilitiesCA01A}
)
