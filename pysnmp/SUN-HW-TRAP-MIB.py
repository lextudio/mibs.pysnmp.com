# SNMP MIB module (SUN-HW-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-HW-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:33 2024
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
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

sunHwTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103)
)
sunHwTrapMIB.setRevisions(
        ("2010-05-05 00:00",
         "2009-12-04 00:00",
         "2009-09-09 00:00",
         "2009-04-17 00:00",
         "2008-10-29 00:00",
         "2007-02-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SunHwTrapThresholdTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lower", 2),
          ("unknown", 3),
          ("upper", 1))
    )



class SunHwTrapSeverityTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("fatal", 2),
          ("nonCritical", 4),
          ("ok", 5),
          ("other", 1))
    )



class SunHwTrapHAStateTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 2),
          ("master", 5),
          ("other", 1),
          ("standalone", 3),
          ("standby", 4))
    )



class SunHwTrapHardDriveStatesTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("consistencyCheckInProgress", 6),
          ("fault", 3),
          ("hotSpare", 5),
          ("inCriticalArray", 7),
          ("inFailedArray", 8),
          ("other", 1),
          ("predictiveFailure", 4),
          ("present", 2),
          ("rebuildAborted", 10),
          ("rebuildInProgress", 9))
    )



class SunHwTrapDisableReasonsTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 3),
          ("faultOrError", 2),
          ("unknown", 1))
    )



class SunHwTrapFloatingPointValueTC(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SunHwTrapHardDriveProbableCauseTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("badblocklogalmostfull", 5),
          ("badblocklogfull", 4),
          ("globalsparecoverage", 7),
          ("nonmediumerror", 11),
          ("reassignwriteoperationfailed", 2),
          ("rebuildfailed", 6),
          ("selftestfailed", 12),
          ("smarthealthstatusfailed", 13),
          ("startstopmax", 14),
          ("uncorrectederror", 10),
          ("unknown", 1),
          ("unrecoverablemediumerrorduringrebuild", 3))
    )



class SunHwTrapDriveControllerProbableCauseTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("batterybackuperror", 3),
          ("controllerfailed", 6),
          ("fatalcacheerror", 4),
          ("fatalflasherror", 2),
          ("unknown", 1))
    )



class SunHwTrapStorageVolumeProbableCauseTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("badblocklogfull", 6),
          ("raiddegraded", 4),
          ("raiderror", 8),
          ("raidfailed", 2),
          ("raidmissing", 3),
          ("unknown", 1))
    )



class SunHwTrapDiagEntityTC(Integer32, TextualConvention):
    status = "current"
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
        *(("alomfm", 2),
          ("fdd", 1),
          ("other", 4),
          ("solarisfma", 3))
    )



class SunHwTrapSuspectFruStatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("acquitted", 6),
          ("faulted", 3),
          ("other", 1),
          ("repaired", 4),
          ("replaced", 5),
          ("suspected", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Ilom_ObjectIdentity = ObjectIdentity
ilom = _Ilom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175)
)
_SunHwTrapObjects_ObjectIdentity = ObjectIdentity
sunHwTrapObjects = _SunHwTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 1)
)
_SunHwTraps_ObjectIdentity = ObjectIdentity
sunHwTraps = _SunHwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2)
)
_SunHwTrapPrefix_ObjectIdentity = ObjectIdentity
sunHwTrapPrefix = _SunHwTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0)
)
_SunHwTrapData_ObjectIdentity = ObjectIdentity
sunHwTrapData = _SunHwTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1)
)
_SunHwTrapSystemIdentifier_Type = DisplayString
_SunHwTrapSystemIdentifier_Object = MibScalar
sunHwTrapSystemIdentifier = _SunHwTrapSystemIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 1),
    _SunHwTrapSystemIdentifier_Type()
)
sunHwTrapSystemIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSystemIdentifier.setStatus("current")
_SunHwTrapComponentName_Type = DisplayString
_SunHwTrapComponentName_Object = MibScalar
sunHwTrapComponentName = _SunHwTrapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 2),
    _SunHwTrapComponentName_Type()
)
sunHwTrapComponentName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapComponentName.setStatus("current")
_SunHwTrapThresholdType_Type = SunHwTrapThresholdTypeTC
_SunHwTrapThresholdType_Object = MibScalar
sunHwTrapThresholdType = _SunHwTrapThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 3),
    _SunHwTrapThresholdType_Type()
)
sunHwTrapThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapThresholdType.setStatus("current")
_SunHwTrapThresholdValue_Type = SunHwTrapFloatingPointValueTC
_SunHwTrapThresholdValue_Object = MibScalar
sunHwTrapThresholdValue = _SunHwTrapThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 4),
    _SunHwTrapThresholdValue_Type()
)
sunHwTrapThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapThresholdValue.setStatus("current")
_SunHwTrapSensorValue_Type = SunHwTrapFloatingPointValueTC
_SunHwTrapSensorValue_Object = MibScalar
sunHwTrapSensorValue = _SunHwTrapSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 5),
    _SunHwTrapSensorValue_Type()
)
sunHwTrapSensorValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSensorValue.setStatus("current")
_SunHwTrapSuspectComponentName_Type = DisplayString
_SunHwTrapSuspectComponentName_Object = MibScalar
sunHwTrapSuspectComponentName = _SunHwTrapSuspectComponentName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 6),
    _SunHwTrapSuspectComponentName_Type()
)
sunHwTrapSuspectComponentName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectComponentName.setStatus("current")
_SunHwTrapFaultClass_Type = DisplayString
_SunHwTrapFaultClass_Object = MibScalar
sunHwTrapFaultClass = _SunHwTrapFaultClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 7),
    _SunHwTrapFaultClass_Type()
)
sunHwTrapFaultClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapFaultClass.setStatus("current")


class _SunHwTrapFaultCertainty_Type(Integer32):
    """Custom type sunHwTrapFaultCertainty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SunHwTrapFaultCertainty_Type.__name__ = "Integer32"
_SunHwTrapFaultCertainty_Object = MibScalar
sunHwTrapFaultCertainty = _SunHwTrapFaultCertainty_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 8),
    _SunHwTrapFaultCertainty_Type()
)
sunHwTrapFaultCertainty.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapFaultCertainty.setStatus("current")
_SunHwTrapAdditionalInfo_Type = DisplayString
_SunHwTrapAdditionalInfo_Object = MibScalar
sunHwTrapAdditionalInfo = _SunHwTrapAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 9),
    _SunHwTrapAdditionalInfo_Type()
)
sunHwTrapAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapAdditionalInfo.setStatus("current")
_SunHwTrapAssocObjectId_Type = RowPointer
_SunHwTrapAssocObjectId_Object = MibScalar
sunHwTrapAssocObjectId = _SunHwTrapAssocObjectId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 10),
    _SunHwTrapAssocObjectId_Type()
)
sunHwTrapAssocObjectId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapAssocObjectId.setStatus("current")
_SunHwTrapNewHAState_Type = SunHwTrapHAStateTC
_SunHwTrapNewHAState_Object = MibScalar
sunHwTrapNewHAState = _SunHwTrapNewHAState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 11),
    _SunHwTrapNewHAState_Type()
)
sunHwTrapNewHAState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapNewHAState.setStatus("current")
_SunHwTrapOldHAState_Type = SunHwTrapHAStateTC
_SunHwTrapOldHAState_Object = MibScalar
sunHwTrapOldHAState = _SunHwTrapOldHAState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 12),
    _SunHwTrapOldHAState_Type()
)
sunHwTrapOldHAState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapOldHAState.setStatus("current")
_SunHwTrapSeverity_Type = SunHwTrapSeverityTC
_SunHwTrapSeverity_Object = MibScalar
sunHwTrapSeverity = _SunHwTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 13),
    _SunHwTrapSeverity_Type()
)
sunHwTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSeverity.setStatus("current")
_SunHwTrapChassisId_Type = DisplayString
_SunHwTrapChassisId_Object = MibScalar
sunHwTrapChassisId = _SunHwTrapChassisId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 14),
    _SunHwTrapChassisId_Type()
)
sunHwTrapChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapChassisId.setStatus("current")
_SunHwTrapProductName_Type = DisplayString
_SunHwTrapProductName_Object = MibScalar
sunHwTrapProductName = _SunHwTrapProductName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 15),
    _SunHwTrapProductName_Type()
)
sunHwTrapProductName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapProductName.setStatus("current")
_SunHwTrapHardDriveState_Type = SunHwTrapHardDriveStatesTC
_SunHwTrapHardDriveState_Object = MibScalar
sunHwTrapHardDriveState = _SunHwTrapHardDriveState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 16),
    _SunHwTrapHardDriveState_Type()
)
sunHwTrapHardDriveState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapHardDriveState.setStatus("current")
_SunHwTrapFaultMessageID_Type = DisplayString
_SunHwTrapFaultMessageID_Object = MibScalar
sunHwTrapFaultMessageID = _SunHwTrapFaultMessageID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 17),
    _SunHwTrapFaultMessageID_Type()
)
sunHwTrapFaultMessageID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapFaultMessageID.setStatus("current")
_SunHwTrapFaultUUID_Type = DisplayString
_SunHwTrapFaultUUID_Object = MibScalar
sunHwTrapFaultUUID = _SunHwTrapFaultUUID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 18),
    _SunHwTrapFaultUUID_Type()
)
sunHwTrapFaultUUID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapFaultUUID.setStatus("current")
_SunHwTrapDisableReason_Type = SunHwTrapDisableReasonsTC
_SunHwTrapDisableReason_Object = MibScalar
sunHwTrapDisableReason = _SunHwTrapDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 19),
    _SunHwTrapDisableReason_Type()
)
sunHwTrapDisableReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapDisableReason.setStatus("current")
_SunHwTrapTestMessage_Type = DisplayString
_SunHwTrapTestMessage_Object = MibScalar
sunHwTrapTestMessage = _SunHwTrapTestMessage_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 20),
    _SunHwTrapTestMessage_Type()
)
sunHwTrapTestMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapTestMessage.setStatus("current")
_SunHwTrapHardDriveProbableCause_Type = SunHwTrapHardDriveProbableCauseTC
_SunHwTrapHardDriveProbableCause_Object = MibScalar
sunHwTrapHardDriveProbableCause = _SunHwTrapHardDriveProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 21),
    _SunHwTrapHardDriveProbableCause_Type()
)
sunHwTrapHardDriveProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapHardDriveProbableCause.setStatus("current")
_SunHwTrapDriveControllerProbableCause_Type = SunHwTrapDriveControllerProbableCauseTC
_SunHwTrapDriveControllerProbableCause_Object = MibScalar
sunHwTrapDriveControllerProbableCause = _SunHwTrapDriveControllerProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 22),
    _SunHwTrapDriveControllerProbableCause_Type()
)
sunHwTrapDriveControllerProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapDriveControllerProbableCause.setStatus("current")
_SunHwTrapStorageVolumeProbableCause_Type = SunHwTrapStorageVolumeProbableCauseTC
_SunHwTrapStorageVolumeProbableCause_Object = MibScalar
sunHwTrapStorageVolumeProbableCause = _SunHwTrapStorageVolumeProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 23),
    _SunHwTrapStorageVolumeProbableCause_Type()
)
sunHwTrapStorageVolumeProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapStorageVolumeProbableCause.setStatus("current")
_SunHwTrapEventTime_Type = DisplayString
_SunHwTrapEventTime_Object = MibScalar
sunHwTrapEventTime = _SunHwTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 24),
    _SunHwTrapEventTime_Type()
)
sunHwTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapEventTime.setStatus("current")
_SunHwTrapDiagEntity_Type = SunHwTrapDiagEntityTC
_SunHwTrapDiagEntity_Object = MibScalar
sunHwTrapDiagEntity = _SunHwTrapDiagEntity_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 25),
    _SunHwTrapDiagEntity_Type()
)
sunHwTrapDiagEntity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapDiagEntity.setStatus("current")
_SunHwTrapFaultDescription_Type = DisplayString
_SunHwTrapFaultDescription_Object = MibScalar
sunHwTrapFaultDescription = _SunHwTrapFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 26),
    _SunHwTrapFaultDescription_Type()
)
sunHwTrapFaultDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapFaultDescription.setStatus("current")
_SunHwTrapKaUrl_Type = DisplayString
_SunHwTrapKaUrl_Object = MibScalar
sunHwTrapKaUrl = _SunHwTrapKaUrl_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 27),
    _SunHwTrapKaUrl_Type()
)
sunHwTrapKaUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapKaUrl.setStatus("current")
_SunHwTrapSuspectCnt_Type = Integer32
_SunHwTrapSuspectCnt_Object = MibScalar
sunHwTrapSuspectCnt = _SunHwTrapSuspectCnt_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 28),
    _SunHwTrapSuspectCnt_Type()
)
sunHwTrapSuspectCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectCnt.setStatus("current")
_SunHwTrapHostname_Type = DisplayString
_SunHwTrapHostname_Object = MibScalar
sunHwTrapHostname = _SunHwTrapHostname_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 29),
    _SunHwTrapHostname_Type()
)
sunHwTrapHostname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapHostname.setStatus("current")
_SunHwTrapProductManufacturer_Type = DisplayString
_SunHwTrapProductManufacturer_Object = MibScalar
sunHwTrapProductManufacturer = _SunHwTrapProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 30),
    _SunHwTrapProductManufacturer_Type()
)
sunHwTrapProductManufacturer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapProductManufacturer.setStatus("current")
_SunHwTrapProductSn_Type = DisplayString
_SunHwTrapProductSn_Object = MibScalar
sunHwTrapProductSn = _SunHwTrapProductSn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 1, 31),
    _SunHwTrapProductSn_Type()
)
sunHwTrapProductSn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapProductSn.setStatus("current")
_SunHwTrapDataTables_ObjectIdentity = ObjectIdentity
sunHwTrapDataTables = _SunHwTrapDataTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2)
)
_SunHwTrapSuspectTable_Object = MibTable
sunHwTrapSuspectTable = _SunHwTrapSuspectTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sunHwTrapSuspectTable.setStatus("current")
_SunHwTrapSuspectEntry_Object = MibTableRow
sunHwTrapSuspectEntry = _SunHwTrapSuspectEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1)
)
sunHwTrapSuspectEntry.setIndexNames(
    (0, "SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruIndex"),
)
if mibBuilder.loadTexts:
    sunHwTrapSuspectEntry.setStatus("current")


class _SunHwTrapSuspectFruIndex_Type(Integer32):
    """Custom type sunHwTrapSuspectFruIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SunHwTrapSuspectFruIndex_Type.__name__ = "Integer32"
_SunHwTrapSuspectFruIndex_Object = MibTableColumn
sunHwTrapSuspectFruIndex = _SunHwTrapSuspectFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 1),
    _SunHwTrapSuspectFruIndex_Type()
)
sunHwTrapSuspectFruIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruIndex.setStatus("current")


class _SunHwTrapSuspectFruFaultCertainty_Type(Integer32):
    """Custom type sunHwTrapSuspectFruFaultCertainty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SunHwTrapSuspectFruFaultCertainty_Type.__name__ = "Integer32"
_SunHwTrapSuspectFruFaultCertainty_Object = MibTableColumn
sunHwTrapSuspectFruFaultCertainty = _SunHwTrapSuspectFruFaultCertainty_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 2),
    _SunHwTrapSuspectFruFaultCertainty_Type()
)
sunHwTrapSuspectFruFaultCertainty.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruFaultCertainty.setStatus("current")
_SunHwTrapSuspectFruFaultClass_Type = DisplayString
_SunHwTrapSuspectFruFaultClass_Object = MibTableColumn
sunHwTrapSuspectFruFaultClass = _SunHwTrapSuspectFruFaultClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 3),
    _SunHwTrapSuspectFruFaultClass_Type()
)
sunHwTrapSuspectFruFaultClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruFaultClass.setStatus("current")
_SunHwTrapSuspectFruName_Type = DisplayString
_SunHwTrapSuspectFruName_Object = MibTableColumn
sunHwTrapSuspectFruName = _SunHwTrapSuspectFruName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 4),
    _SunHwTrapSuspectFruName_Type()
)
sunHwTrapSuspectFruName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruName.setStatus("current")
_SunHwTrapSuspectFruLocation_Type = DisplayString
_SunHwTrapSuspectFruLocation_Object = MibTableColumn
sunHwTrapSuspectFruLocation = _SunHwTrapSuspectFruLocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 5),
    _SunHwTrapSuspectFruLocation_Type()
)
sunHwTrapSuspectFruLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruLocation.setStatus("current")
_SunHwTrapSuspectFruChassisId_Type = DisplayString
_SunHwTrapSuspectFruChassisId_Object = MibTableColumn
sunHwTrapSuspectFruChassisId = _SunHwTrapSuspectFruChassisId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 6),
    _SunHwTrapSuspectFruChassisId_Type()
)
sunHwTrapSuspectFruChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruChassisId.setStatus("current")
_SunHwTrapSuspectFruManufacturer_Type = DisplayString
_SunHwTrapSuspectFruManufacturer_Object = MibTableColumn
sunHwTrapSuspectFruManufacturer = _SunHwTrapSuspectFruManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 7),
    _SunHwTrapSuspectFruManufacturer_Type()
)
sunHwTrapSuspectFruManufacturer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruManufacturer.setStatus("current")
_SunHwTrapSuspectFruPn_Type = DisplayString
_SunHwTrapSuspectFruPn_Object = MibTableColumn
sunHwTrapSuspectFruPn = _SunHwTrapSuspectFruPn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 8),
    _SunHwTrapSuspectFruPn_Type()
)
sunHwTrapSuspectFruPn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruPn.setStatus("current")
_SunHwTrapSuspectFruSn_Type = DisplayString
_SunHwTrapSuspectFruSn_Object = MibTableColumn
sunHwTrapSuspectFruSn = _SunHwTrapSuspectFruSn_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 9),
    _SunHwTrapSuspectFruSn_Type()
)
sunHwTrapSuspectFruSn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruSn.setStatus("current")
_SunHwTrapSuspectFruRevision_Type = DisplayString
_SunHwTrapSuspectFruRevision_Object = MibTableColumn
sunHwTrapSuspectFruRevision = _SunHwTrapSuspectFruRevision_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 10),
    _SunHwTrapSuspectFruRevision_Type()
)
sunHwTrapSuspectFruRevision.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruRevision.setStatus("current")
_SunHwTrapSuspectFruStatus_Type = SunHwTrapSuspectFruStatusTC
_SunHwTrapSuspectFruStatus_Object = MibTableColumn
sunHwTrapSuspectFruStatus = _SunHwTrapSuspectFruStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 2, 1, 1, 11),
    _SunHwTrapSuspectFruStatus_Type()
)
sunHwTrapSuspectFruStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sunHwTrapSuspectFruStatus.setStatus("current")
_SunHwTrapConformances_ObjectIdentity = ObjectIdentity
sunHwTrapConformances = _SunHwTrapConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 3)
)
_SunHwTrapCompliances_ObjectIdentity = ObjectIdentity
sunHwTrapCompliances = _SunHwTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 3, 1)
)
_SunHwTrapGroups_ObjectIdentity = ObjectIdentity
sunHwTrapGroups = _SunHwTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 3, 2)
)
_SunHwTrapObjectGroups_ObjectIdentity = ObjectIdentity
sunHwTrapObjectGroups = _SunHwTrapObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 3, 2, 1)
)
_SunHwTrapNotifGroups_ObjectIdentity = ObjectIdentity
sunHwTrapNotifGroups = _SunHwTrapNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 3, 2, 2)
)

# Managed Objects groups

sunHwTrapNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 3, 2, 1, 2)
)
sunHwTrapNotificationObjectGroup.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapNewHAState"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapOldHAState"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveState"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDisableReason"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTestMessage"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveProbableCause"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDriveControllerProbableCause"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapStorageVolumeProbableCause"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapEventTime"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDiagEntity"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapKaUrl"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultDescription"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHostname"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectCnt"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruLocation"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruPn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruRevision"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruStatus"))
)
if mibBuilder.loadTexts:
    sunHwTrapNotificationObjectGroup.setStatus("current")


# Notification objects

sunHwTrapVoltageFatalThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 1)
)
sunHwTrapVoltageFatalThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapVoltageFatalThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapVoltageFatalThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 2)
)
sunHwTrapVoltageFatalThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapVoltageFatalThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapVoltageCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 3)
)
sunHwTrapVoltageCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapVoltageCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapVoltageCritThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 4)
)
sunHwTrapVoltageCritThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapVoltageCritThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapVoltageNonCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 5)
)
sunHwTrapVoltageNonCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapVoltageNonCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 6)
)
sunHwTrapVoltageOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapVoltageOk.setStatus(
        "current"
    )

sunHwTrapTempFatalThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 7)
)
sunHwTrapTempFatalThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapTempFatalThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapTempFatalThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 8)
)
sunHwTrapTempFatalThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapTempFatalThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapTempCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 9)
)
sunHwTrapTempCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapTempCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapTempCritThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 10)
)
sunHwTrapTempCritThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapTempCritThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapTempNonCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 11)
)
sunHwTrapTempNonCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapTempNonCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 12)
)
sunHwTrapTempOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapTempOk.setStatus(
        "current"
    )

sunHwTrapElectricalCurrentFatalThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 13)
)
sunHwTrapElectricalCurrentFatalThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapElectricalCurrentFatalThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapElectricalCurrentFatalThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 14)
)
sunHwTrapElectricalCurrentFatalThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapElectricalCurrentFatalThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapElectricalCurrentCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 15)
)
sunHwTrapElectricalCurrentCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapElectricalCurrentCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapElectricalCurrentCritThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 16)
)
sunHwTrapElectricalCurrentCritThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapElectricalCurrentCritThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapElectricalCurrentNonCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 17)
)
sunHwTrapElectricalCurrentNonCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapElectricalCurrentNonCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapElectricalCurrentOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 18)
)
sunHwTrapElectricalCurrentOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapElectricalCurrentOk.setStatus(
        "current"
    )

sunHwTrapFanSpeedFatalThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 19)
)
sunHwTrapFanSpeedFatalThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanSpeedFatalThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapFanSpeedFatalThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 20)
)
sunHwTrapFanSpeedFatalThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanSpeedFatalThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapFanSpeedCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 21)
)
sunHwTrapFanSpeedCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanSpeedCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapFanSpeedCritThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 22)
)
sunHwTrapFanSpeedCritThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanSpeedCritThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapFanSpeedNonCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 23)
)
sunHwTrapFanSpeedNonCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanSpeedNonCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapFanSpeedOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 24)
)
sunHwTrapFanSpeedOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanSpeedOk.setStatus(
        "current"
    )

sunHwTrapSensorFatalThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 25)
)
sunHwTrapSensorFatalThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapSensorFatalThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapSensorFatalThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 26)
)
sunHwTrapSensorFatalThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapSensorFatalThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapSensorCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 27)
)
sunHwTrapSensorCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapSensorCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapSensorCritThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 28)
)
sunHwTrapSensorCritThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapSensorCritThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapSensorNonCritThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 29)
)
sunHwTrapSensorNonCritThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapSensorNonCritThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapSensorThresholdOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 30)
)
sunHwTrapSensorThresholdOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapSensorThresholdOk.setStatus(
        "current"
    )

sunHwTrapPowerSupplyFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 31)
)
sunHwTrapPowerSupplyFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapPowerSupplyFault.setStatus(
        "current"
    )

sunHwTrapPowerSupplyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 32)
)
sunHwTrapPowerSupplyError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapPowerSupplyError.setStatus(
        "current"
    )

sunHwTrapPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 33)
)
sunHwTrapPowerSupplyOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapPowerSupplyOk.setStatus(
        "current"
    )

sunHwTrapFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 34)
)
sunHwTrapFanFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanFault.setStatus(
        "current"
    )

sunHwTrapFanError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 35)
)
sunHwTrapFanError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanError.setStatus(
        "current"
    )

sunHwTrapFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 36)
)
sunHwTrapFanOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanOk.setStatus(
        "current"
    )

sunHwTrapProcessorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 37)
)
sunHwTrapProcessorFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapProcessorFault.setStatus(
        "current"
    )

sunHwTrapProcessorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 38)
)
sunHwTrapProcessorError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapProcessorError.setStatus(
        "current"
    )

sunHwTrapProcessorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 39)
)
sunHwTrapProcessorOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapProcessorOk.setStatus(
        "current"
    )

sunHwTrapMemoryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 40)
)
sunHwTrapMemoryFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapMemoryFault.setStatus(
        "current"
    )

sunHwTrapMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 41)
)
sunHwTrapMemoryError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapMemoryError.setStatus(
        "current"
    )

sunHwTrapMemoryOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 42)
)
sunHwTrapMemoryOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapMemoryOk.setStatus(
        "current"
    )

sunHwTrapHardDriveFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 43)
)
sunHwTrapHardDriveFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveProbableCause"))
)
if mibBuilder.loadTexts:
    sunHwTrapHardDriveFault.setStatus(
        "current"
    )

sunHwTrapHardDriveError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 44)
)
sunHwTrapHardDriveError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveProbableCause"))
)
if mibBuilder.loadTexts:
    sunHwTrapHardDriveError.setStatus(
        "current"
    )

sunHwTrapHardDriveOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 45)
)
sunHwTrapHardDriveOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapHardDriveOk.setStatus(
        "current"
    )

sunHwTrapIOFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 46)
)
sunHwTrapIOFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapIOFault.setStatus(
        "current"
    )

sunHwTrapIOError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 47)
)
sunHwTrapIOError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapIOError.setStatus(
        "current"
    )

sunHwTrapIOOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 48)
)
sunHwTrapIOOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapIOOk.setStatus(
        "current"
    )

sunHwTrapSlotOrConnectorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 49)
)
sunHwTrapSlotOrConnectorFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapSlotOrConnectorFault.setStatus(
        "current"
    )

sunHwTrapSlotOrConnectorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 50)
)
sunHwTrapSlotOrConnectorError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapSlotOrConnectorError.setStatus(
        "current"
    )

sunHwTrapSlotOrConnectorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 51)
)
sunHwTrapSlotOrConnectorOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapSlotOrConnectorOk.setStatus(
        "current"
    )

sunHwTrapComponentFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 52)
)
sunHwTrapComponentFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapComponentFault.setStatus(
        "current"
    )

sunHwTrapComponentError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 53)
)
sunHwTrapComponentError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapComponentError.setStatus(
        "current"
    )

sunHwTrapComponentOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 54)
)
sunHwTrapComponentOk.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapComponentOk.setStatus(
        "current"
    )

sunHwTrapFruInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 55)
)
sunHwTrapFruInserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapFruInserted.setStatus(
        "current"
    )

sunHwTrapFruRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 56)
)
sunHwTrapFruRemoved.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapFruRemoved.setStatus(
        "current"
    )

sunHwTrapComponentDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 57)
)
sunHwTrapComponentDisabled.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDisableReason"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapComponentDisabled.setStatus(
        "current"
    )

sunHwTrapComponentEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 58)
)
sunHwTrapComponentEnabled.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"))
)
if mibBuilder.loadTexts:
    sunHwTrapComponentEnabled.setStatus(
        "current"
    )

sunHwTrapPreOSError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 59)
)
sunHwTrapPreOSError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapPreOSError.setStatus(
        "current"
    )

sunHwTrapHAStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 60)
)
sunHwTrapHAStateChange.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapNewHAState"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapOldHAState"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapHAStateChange.setStatus(
        "current"
    )

sunHwTrapSecurityIntrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 61)
)
sunHwTrapSecurityIntrusion.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapSecurityIntrusion.setStatus(
        "current"
    )

sunHwTrapHardDriveStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 62)
)
sunHwTrapHardDriveStatus.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveState"))
)
if mibBuilder.loadTexts:
    sunHwTrapHardDriveStatus.setStatus(
        "current"
    )

sunHwTrapTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 63)
)
sunHwTrapTestTrap.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTestMessage"))
)
if mibBuilder.loadTexts:
    sunHwTrapTestTrap.setStatus(
        "current"
    )

sunHwTrapPowerSupplyFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 64)
)
sunHwTrapPowerSupplyFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapPowerSupplyFaultCleared.setStatus(
        "current"
    )

sunHwTrapFanFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 65)
)
sunHwTrapFanFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapFanFaultCleared.setStatus(
        "current"
    )

sunHwTrapProcessorFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 66)
)
sunHwTrapProcessorFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapProcessorFaultCleared.setStatus(
        "current"
    )

sunHwTrapMemoryFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 67)
)
sunHwTrapMemoryFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapMemoryFaultCleared.setStatus(
        "current"
    )

sunHwTrapHardDriveFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 68)
)
sunHwTrapHardDriveFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapHardDriveFaultCleared.setStatus(
        "current"
    )

sunHwTrapIOFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 69)
)
sunHwTrapIOFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapIOFaultCleared.setStatus(
        "current"
    )

sunHwTrapSlotOrConnectorFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 70)
)
sunHwTrapSlotOrConnectorFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapSlotOrConnectorFaultCleared.setStatus(
        "current"
    )

sunHwTrapComponentFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 71)
)
sunHwTrapComponentFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapComponentFaultCleared.setStatus(
        "current"
    )

sunHwTrapPowerConsumptionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 72)
)
sunHwTrapPowerConsumptionThresholdExceeded.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapPowerConsumptionThresholdExceeded.setStatus(
        "current"
    )

sunHwTrapPowerConsumptionThresholdDeasserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 73)
)
sunHwTrapPowerConsumptionThresholdDeasserted.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdType"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapThresholdValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorValue"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"))
)
if mibBuilder.loadTexts:
    sunHwTrapPowerConsumptionThresholdDeasserted.setStatus(
        "current"
    )

sunHwTrapDriveControllerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 74)
)
sunHwTrapDriveControllerFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDriveControllerProbableCause"))
)
if mibBuilder.loadTexts:
    sunHwTrapDriveControllerFault.setStatus(
        "current"
    )

sunHwTrapDriveControllerFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 75)
)
sunHwTrapDriveControllerFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapDriveControllerFaultCleared.setStatus(
        "current"
    )

sunHwTrapDriveControllerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 76)
)
sunHwTrapDriveControllerError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDriveControllerProbableCause"))
)
if mibBuilder.loadTexts:
    sunHwTrapDriveControllerError.setStatus(
        "current"
    )

sunHwTrapStorageVolumeFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 77)
)
sunHwTrapStorageVolumeFault.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapStorageVolumeProbableCause"))
)
if mibBuilder.loadTexts:
    sunHwTrapStorageVolumeFault.setStatus(
        "current"
    )

sunHwTrapStorageVolumeFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 78)
)
sunHwTrapStorageVolumeFaultCleared.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"))
)
if mibBuilder.loadTexts:
    sunHwTrapStorageVolumeFaultCleared.setStatus(
        "current"
    )

sunHwTrapStorageVolumeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 79)
)
sunHwTrapStorageVolumeError.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAdditionalInfo"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapAssocObjectId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapStorageVolumeProbableCause"))
)
if mibBuilder.loadTexts:
    sunHwTrapStorageVolumeError.setStatus(
        "current"
    )

sunHwTrapFaultDiagnosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 2, 0, 80)
)
sunHwTrapFaultDiagnosed.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapEventTime"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultMessageID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultUUID"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapKaUrl"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultDescription"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSeverity"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProductSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDiagEntity"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSystemIdentifier"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHostname"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectCnt"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruLocation"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruPn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruRevision"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruStatus"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruLocation"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruPn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruRevision"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruStatus"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruLocation"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruPn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruRevision"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruStatus"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruLocation"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruPn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruRevision"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruStatus"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultCertainty"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruFaultClass"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruName"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruLocation"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruChassisId"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruManufacturer"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruPn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruSn"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruRevision"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSuspectFruStatus"))
)
if mibBuilder.loadTexts:
    sunHwTrapFaultDiagnosed.setStatus(
        "current"
    )


# Notifications groups

sunHwTrapNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 103, 3, 2, 2, 1)
)
sunHwTrapNotificationsGroup.setObjects(
      *(("SUN-HW-TRAP-MIB", "sunHwTrapVoltageFatalThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapVoltageFatalThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapVoltageCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapVoltageCritThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapVoltageNonCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapVoltageOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTempFatalThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTempFatalThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTempCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTempCritThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTempNonCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTempOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapElectricalCurrentFatalThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapElectricalCurrentFatalThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapElectricalCurrentCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapElectricalCurrentCritThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapElectricalCurrentNonCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapElectricalCurrentOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanSpeedFatalThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanSpeedFatalThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanSpeedCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanSpeedCritThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanSpeedNonCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanSpeedOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorFatalThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorFatalThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorCritThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorNonCritThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSensorThresholdOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapPowerSupplyFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapPowerSupplyFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapPowerSupplyError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapPowerSupplyOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFanOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProcessorFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProcessorFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProcessorError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapProcessorOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapMemoryFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapMemoryFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapMemoryError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapMemoryOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapIOFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapIOFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapIOError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapIOOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSlotOrConnectorFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSlotOrConnectorFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSlotOrConnectorError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSlotOrConnectorOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentOk"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFruInserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFruRemoved"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentDisabled"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapComponentEnabled"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapPreOSError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHAStateChange"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapSecurityIntrusion"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapHardDriveStatus"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapTestTrap"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapPowerConsumptionThresholdExceeded"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapPowerConsumptionThresholdDeasserted"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDriveControllerFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDriveControllerFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapDriveControllerError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapStorageVolumeFault"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapStorageVolumeFaultCleared"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapStorageVolumeError"),
        ("SUN-HW-TRAP-MIB", "sunHwTrapFaultDiagnosed"))
)
if mibBuilder.loadTexts:
    sunHwTrapNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-HW-TRAP-MIB",
    **{"SunHwTrapThresholdTypeTC": SunHwTrapThresholdTypeTC,
       "SunHwTrapSeverityTC": SunHwTrapSeverityTC,
       "SunHwTrapHAStateTC": SunHwTrapHAStateTC,
       "SunHwTrapHardDriveStatesTC": SunHwTrapHardDriveStatesTC,
       "SunHwTrapDisableReasonsTC": SunHwTrapDisableReasonsTC,
       "SunHwTrapFloatingPointValueTC": SunHwTrapFloatingPointValueTC,
       "SunHwTrapHardDriveProbableCauseTC": SunHwTrapHardDriveProbableCauseTC,
       "SunHwTrapDriveControllerProbableCauseTC": SunHwTrapDriveControllerProbableCauseTC,
       "SunHwTrapStorageVolumeProbableCauseTC": SunHwTrapStorageVolumeProbableCauseTC,
       "SunHwTrapDiagEntityTC": SunHwTrapDiagEntityTC,
       "SunHwTrapSuspectFruStatusTC": SunHwTrapSuspectFruStatusTC,
       "sun": sun,
       "products": products,
       "ilom": ilom,
       "sunHwTrapMIB": sunHwTrapMIB,
       "sunHwTrapObjects": sunHwTrapObjects,
       "sunHwTraps": sunHwTraps,
       "sunHwTrapPrefix": sunHwTrapPrefix,
       "sunHwTrapVoltageFatalThresholdExceeded": sunHwTrapVoltageFatalThresholdExceeded,
       "sunHwTrapVoltageFatalThresholdDeasserted": sunHwTrapVoltageFatalThresholdDeasserted,
       "sunHwTrapVoltageCritThresholdExceeded": sunHwTrapVoltageCritThresholdExceeded,
       "sunHwTrapVoltageCritThresholdDeasserted": sunHwTrapVoltageCritThresholdDeasserted,
       "sunHwTrapVoltageNonCritThresholdExceeded": sunHwTrapVoltageNonCritThresholdExceeded,
       "sunHwTrapVoltageOk": sunHwTrapVoltageOk,
       "sunHwTrapTempFatalThresholdExceeded": sunHwTrapTempFatalThresholdExceeded,
       "sunHwTrapTempFatalThresholdDeasserted": sunHwTrapTempFatalThresholdDeasserted,
       "sunHwTrapTempCritThresholdExceeded": sunHwTrapTempCritThresholdExceeded,
       "sunHwTrapTempCritThresholdDeasserted": sunHwTrapTempCritThresholdDeasserted,
       "sunHwTrapTempNonCritThresholdExceeded": sunHwTrapTempNonCritThresholdExceeded,
       "sunHwTrapTempOk": sunHwTrapTempOk,
       "sunHwTrapElectricalCurrentFatalThresholdExceeded": sunHwTrapElectricalCurrentFatalThresholdExceeded,
       "sunHwTrapElectricalCurrentFatalThresholdDeasserted": sunHwTrapElectricalCurrentFatalThresholdDeasserted,
       "sunHwTrapElectricalCurrentCritThresholdExceeded": sunHwTrapElectricalCurrentCritThresholdExceeded,
       "sunHwTrapElectricalCurrentCritThresholdDeasserted": sunHwTrapElectricalCurrentCritThresholdDeasserted,
       "sunHwTrapElectricalCurrentNonCritThresholdExceeded": sunHwTrapElectricalCurrentNonCritThresholdExceeded,
       "sunHwTrapElectricalCurrentOk": sunHwTrapElectricalCurrentOk,
       "sunHwTrapFanSpeedFatalThresholdExceeded": sunHwTrapFanSpeedFatalThresholdExceeded,
       "sunHwTrapFanSpeedFatalThresholdDeasserted": sunHwTrapFanSpeedFatalThresholdDeasserted,
       "sunHwTrapFanSpeedCritThresholdExceeded": sunHwTrapFanSpeedCritThresholdExceeded,
       "sunHwTrapFanSpeedCritThresholdDeasserted": sunHwTrapFanSpeedCritThresholdDeasserted,
       "sunHwTrapFanSpeedNonCritThresholdExceeded": sunHwTrapFanSpeedNonCritThresholdExceeded,
       "sunHwTrapFanSpeedOk": sunHwTrapFanSpeedOk,
       "sunHwTrapSensorFatalThresholdExceeded": sunHwTrapSensorFatalThresholdExceeded,
       "sunHwTrapSensorFatalThresholdDeasserted": sunHwTrapSensorFatalThresholdDeasserted,
       "sunHwTrapSensorCritThresholdExceeded": sunHwTrapSensorCritThresholdExceeded,
       "sunHwTrapSensorCritThresholdDeasserted": sunHwTrapSensorCritThresholdDeasserted,
       "sunHwTrapSensorNonCritThresholdExceeded": sunHwTrapSensorNonCritThresholdExceeded,
       "sunHwTrapSensorThresholdOk": sunHwTrapSensorThresholdOk,
       "sunHwTrapPowerSupplyFault": sunHwTrapPowerSupplyFault,
       "sunHwTrapPowerSupplyError": sunHwTrapPowerSupplyError,
       "sunHwTrapPowerSupplyOk": sunHwTrapPowerSupplyOk,
       "sunHwTrapFanFault": sunHwTrapFanFault,
       "sunHwTrapFanError": sunHwTrapFanError,
       "sunHwTrapFanOk": sunHwTrapFanOk,
       "sunHwTrapProcessorFault": sunHwTrapProcessorFault,
       "sunHwTrapProcessorError": sunHwTrapProcessorError,
       "sunHwTrapProcessorOk": sunHwTrapProcessorOk,
       "sunHwTrapMemoryFault": sunHwTrapMemoryFault,
       "sunHwTrapMemoryError": sunHwTrapMemoryError,
       "sunHwTrapMemoryOk": sunHwTrapMemoryOk,
       "sunHwTrapHardDriveFault": sunHwTrapHardDriveFault,
       "sunHwTrapHardDriveError": sunHwTrapHardDriveError,
       "sunHwTrapHardDriveOk": sunHwTrapHardDriveOk,
       "sunHwTrapIOFault": sunHwTrapIOFault,
       "sunHwTrapIOError": sunHwTrapIOError,
       "sunHwTrapIOOk": sunHwTrapIOOk,
       "sunHwTrapSlotOrConnectorFault": sunHwTrapSlotOrConnectorFault,
       "sunHwTrapSlotOrConnectorError": sunHwTrapSlotOrConnectorError,
       "sunHwTrapSlotOrConnectorOk": sunHwTrapSlotOrConnectorOk,
       "sunHwTrapComponentFault": sunHwTrapComponentFault,
       "sunHwTrapComponentError": sunHwTrapComponentError,
       "sunHwTrapComponentOk": sunHwTrapComponentOk,
       "sunHwTrapFruInserted": sunHwTrapFruInserted,
       "sunHwTrapFruRemoved": sunHwTrapFruRemoved,
       "sunHwTrapComponentDisabled": sunHwTrapComponentDisabled,
       "sunHwTrapComponentEnabled": sunHwTrapComponentEnabled,
       "sunHwTrapPreOSError": sunHwTrapPreOSError,
       "sunHwTrapHAStateChange": sunHwTrapHAStateChange,
       "sunHwTrapSecurityIntrusion": sunHwTrapSecurityIntrusion,
       "sunHwTrapHardDriveStatus": sunHwTrapHardDriveStatus,
       "sunHwTrapTestTrap": sunHwTrapTestTrap,
       "sunHwTrapPowerSupplyFaultCleared": sunHwTrapPowerSupplyFaultCleared,
       "sunHwTrapFanFaultCleared": sunHwTrapFanFaultCleared,
       "sunHwTrapProcessorFaultCleared": sunHwTrapProcessorFaultCleared,
       "sunHwTrapMemoryFaultCleared": sunHwTrapMemoryFaultCleared,
       "sunHwTrapHardDriveFaultCleared": sunHwTrapHardDriveFaultCleared,
       "sunHwTrapIOFaultCleared": sunHwTrapIOFaultCleared,
       "sunHwTrapSlotOrConnectorFaultCleared": sunHwTrapSlotOrConnectorFaultCleared,
       "sunHwTrapComponentFaultCleared": sunHwTrapComponentFaultCleared,
       "sunHwTrapPowerConsumptionThresholdExceeded": sunHwTrapPowerConsumptionThresholdExceeded,
       "sunHwTrapPowerConsumptionThresholdDeasserted": sunHwTrapPowerConsumptionThresholdDeasserted,
       "sunHwTrapDriveControllerFault": sunHwTrapDriveControllerFault,
       "sunHwTrapDriveControllerFaultCleared": sunHwTrapDriveControllerFaultCleared,
       "sunHwTrapDriveControllerError": sunHwTrapDriveControllerError,
       "sunHwTrapStorageVolumeFault": sunHwTrapStorageVolumeFault,
       "sunHwTrapStorageVolumeFaultCleared": sunHwTrapStorageVolumeFaultCleared,
       "sunHwTrapStorageVolumeError": sunHwTrapStorageVolumeError,
       "sunHwTrapFaultDiagnosed": sunHwTrapFaultDiagnosed,
       "sunHwTrapData": sunHwTrapData,
       "sunHwTrapSystemIdentifier": sunHwTrapSystemIdentifier,
       "sunHwTrapComponentName": sunHwTrapComponentName,
       "sunHwTrapThresholdType": sunHwTrapThresholdType,
       "sunHwTrapThresholdValue": sunHwTrapThresholdValue,
       "sunHwTrapSensorValue": sunHwTrapSensorValue,
       "sunHwTrapSuspectComponentName": sunHwTrapSuspectComponentName,
       "sunHwTrapFaultClass": sunHwTrapFaultClass,
       "sunHwTrapFaultCertainty": sunHwTrapFaultCertainty,
       "sunHwTrapAdditionalInfo": sunHwTrapAdditionalInfo,
       "sunHwTrapAssocObjectId": sunHwTrapAssocObjectId,
       "sunHwTrapNewHAState": sunHwTrapNewHAState,
       "sunHwTrapOldHAState": sunHwTrapOldHAState,
       "sunHwTrapSeverity": sunHwTrapSeverity,
       "sunHwTrapChassisId": sunHwTrapChassisId,
       "sunHwTrapProductName": sunHwTrapProductName,
       "sunHwTrapHardDriveState": sunHwTrapHardDriveState,
       "sunHwTrapFaultMessageID": sunHwTrapFaultMessageID,
       "sunHwTrapFaultUUID": sunHwTrapFaultUUID,
       "sunHwTrapDisableReason": sunHwTrapDisableReason,
       "sunHwTrapTestMessage": sunHwTrapTestMessage,
       "sunHwTrapHardDriveProbableCause": sunHwTrapHardDriveProbableCause,
       "sunHwTrapDriveControllerProbableCause": sunHwTrapDriveControllerProbableCause,
       "sunHwTrapStorageVolumeProbableCause": sunHwTrapStorageVolumeProbableCause,
       "sunHwTrapEventTime": sunHwTrapEventTime,
       "sunHwTrapDiagEntity": sunHwTrapDiagEntity,
       "sunHwTrapFaultDescription": sunHwTrapFaultDescription,
       "sunHwTrapKaUrl": sunHwTrapKaUrl,
       "sunHwTrapSuspectCnt": sunHwTrapSuspectCnt,
       "sunHwTrapHostname": sunHwTrapHostname,
       "sunHwTrapProductManufacturer": sunHwTrapProductManufacturer,
       "sunHwTrapProductSn": sunHwTrapProductSn,
       "sunHwTrapDataTables": sunHwTrapDataTables,
       "sunHwTrapSuspectTable": sunHwTrapSuspectTable,
       "sunHwTrapSuspectEntry": sunHwTrapSuspectEntry,
       "sunHwTrapSuspectFruIndex": sunHwTrapSuspectFruIndex,
       "sunHwTrapSuspectFruFaultCertainty": sunHwTrapSuspectFruFaultCertainty,
       "sunHwTrapSuspectFruFaultClass": sunHwTrapSuspectFruFaultClass,
       "sunHwTrapSuspectFruName": sunHwTrapSuspectFruName,
       "sunHwTrapSuspectFruLocation": sunHwTrapSuspectFruLocation,
       "sunHwTrapSuspectFruChassisId": sunHwTrapSuspectFruChassisId,
       "sunHwTrapSuspectFruManufacturer": sunHwTrapSuspectFruManufacturer,
       "sunHwTrapSuspectFruPn": sunHwTrapSuspectFruPn,
       "sunHwTrapSuspectFruSn": sunHwTrapSuspectFruSn,
       "sunHwTrapSuspectFruRevision": sunHwTrapSuspectFruRevision,
       "sunHwTrapSuspectFruStatus": sunHwTrapSuspectFruStatus,
       "sunHwTrapConformances": sunHwTrapConformances,
       "sunHwTrapCompliances": sunHwTrapCompliances,
       "sunHwTrapGroups": sunHwTrapGroups,
       "sunHwTrapObjectGroups": sunHwTrapObjectGroups,
       "sunHwTrapNotificationObjectGroup": sunHwTrapNotificationObjectGroup,
       "sunHwTrapNotifGroups": sunHwTrapNotifGroups,
       "sunHwTrapNotificationsGroup": sunHwTrapNotificationsGroup}
)
