# SNMP MIB module (CPQDSCCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQDSCCS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:20 2024
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName")

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

_CpqDsccs_ObjectIdentity = ObjectIdentity
cpqDsccs = _CpqDsccs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 171)
)
_DsccsTrapInfo_ObjectIdentity = ObjectIdentity
dsccsTrapInfo = _DsccsTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 171, 1)
)


class _CsRoomName_Type(DisplayString):
    """Custom type csRoomName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CsRoomName_Type.__name__ = "DisplayString"
_CsRoomName_Object = MibScalar
csRoomName = _CsRoomName_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 1),
    _CsRoomName_Type()
)
csRoomName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csRoomName.setStatus("mandatory")


class _CsContactName_Type(DisplayString):
    """Custom type csContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CsContactName_Type.__name__ = "DisplayString"
_CsContactName_Object = MibScalar
csContactName = _CsContactName_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 2),
    _CsContactName_Type()
)
csContactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csContactName.setStatus("mandatory")


class _CsContactPhoneNumber_Type(DisplayString):
    """Custom type csContactPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CsContactPhoneNumber_Type.__name__ = "DisplayString"
_CsContactPhoneNumber_Object = MibScalar
csContactPhoneNumber = _CsContactPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 3),
    _CsContactPhoneNumber_Type()
)
csContactPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csContactPhoneNumber.setStatus("mandatory")


class _CsProductName_Type(DisplayString):
    """Custom type csProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CsProductName_Type.__name__ = "DisplayString"
_CsProductName_Object = MibScalar
csProductName = _CsProductName_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 4),
    _CsProductName_Type()
)
csProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csProductName.setStatus("mandatory")


class _CsProductId_Type(DisplayString):
    """Custom type csProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CsProductId_Type.__name__ = "DisplayString"
_CsProductId_Object = MibScalar
csProductId = _CsProductId_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 5),
    _CsProductId_Type()
)
csProductId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csProductId.setStatus("mandatory")


class _CsSerialNumber_Type(DisplayString):
    """Custom type csSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CsSerialNumber_Type.__name__ = "DisplayString"
_CsSerialNumber_Object = MibScalar
csSerialNumber = _CsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 6),
    _CsSerialNumber_Type()
)
csSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csSerialNumber.setStatus("mandatory")


class _CsSoftwareVersion_Type(DisplayString):
    """Custom type csSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CsSoftwareVersion_Type.__name__ = "DisplayString"
_CsSoftwareVersion_Object = MibScalar
csSoftwareVersion = _CsSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 7),
    _CsSoftwareVersion_Type()
)
csSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csSoftwareVersion.setStatus("mandatory")


class _TrapEventId_Type(Integer32):
    """Custom type trapEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3009,
              3010,
              3011,
              3012,
              3013,
              3014,
              3015,
              3016,
              3017,
              3018,
              3019,
              3020,
              3021,
              3022,
              3023,
              3024,
              3025,
              3026,
              3027,
              3028,
              3029,
              3030,
              3031,
              3032,
              3033,
              3034,
              3035,
              3036,
              4001,
              4002,
              4003,
              4004,
              4005,
              4006,
              4007,
              4008,
              4009,
              4010,
              4011,
              4012,
              4013,
              4014,
              6001,
              7001)
        )
    )
    namedValues = NamedValues(
        *(("commisAbortedByUseer", 3003),
          ("commisAhuPerturbationWithinConfig", 3032),
          ("commisAssertionFailedForAhuFeedbackOnTest", 3023),
          ("commisAttestSystemPerturbationForAhu", 3022),
          ("commisBeginExecutionCycleSettingAhuToConfiguredLevels", 3035),
          ("commisBeginInitCycle", 3016),
          ("commisCannotHaltCommissioningNoActiveInstanceRunning", 3034),
          ("commisCannotPerformMergeOpWhenRunningCommissioning", 3033),
          ("commisCannotPerformOperation", 3008),
          ("commisExecutionFailedForConfiguration", 3019),
          ("commisFailedCouldNotChangeAhuSetPoint", 3006),
          ("commisFailedDataCenterTempExceedThresholdLimit", 3007),
          ("commisFailedSupplyAirTempForAhuDidNotChange", 3005),
          ("commisFinishedSuccessfully", 3004),
          ("commisFullStartedByUser", 3001),
          ("commisHaltActiveCommmissioningExecution", 3018),
          ("commisInitDefaultConfigProfiles", 3031),
          ("commisInitSubsystemForCOnfigProfileAndInstance", 3014),
          ("commisInitSubsystemForConfigProfile", 3013),
          ("commisLoadingConfigParamForProfile", 3011),
          ("commisLoadingConfigProfile", 3009),
          ("commisLoadingPropertiesForConfigProfile", 3010),
          ("commisMergeDataForConfig", 3029),
          ("commisPartialStartedByUserForAhu", 3002),
          ("commisPerformCheckForAhusInConfigProfile", 3012),
          ("commisPerformPerturbationForAhu", 3021),
          ("commisPerformPerturbationForInitDistributionLevel", 3020),
          ("commisProcessCompletedSuccessfullyForConfiguration", 3017),
          ("commisRollbackAndCleanFromDatabaseChanges", 3030),
          ("commisSettingAhusToUniformDistributionLevel", 3036),
          ("commisStartingForConfigProfile", 3015),
          ("commisStoreBasecaseSensorTempAndData", 3027),
          ("commisStoreSensorNetworkStateAndDataForPerturbation", 3026),
          ("commisStoreSystemPerturbationSensorTempAndData", 3028),
          ("commisValidatingAhuSupplyAirTempHasChanged", 3025),
          ("commisWaitingForSystemSteadinessFromSensorNetwork", 3024),
          ("commuAhuFluidLeakDetected", 4012),
          ("commuAhuPoweredOff", 4011),
          ("commuAhuReturnAirTempReachedHighLimit", 4009),
          ("commuAhuReturnAirTempReachedLowLimit", 4010),
          ("commuAhuSupplyAirTempReachedHighLimit", 4007),
          ("commuAhuSupplyAirTempReachedLowLimit", 4008),
          ("commuAhuSwitchedToLocalControl", 4013),
          ("commuFailsafeDeviceHeartbeatNotPresent", 4005),
          ("commuMbcHostIsUnreachablePingFailed", 4002),
          ("commuOpcCommunicationsLost", 4001),
          ("commuOpcStatus", 4003),
          ("commuReverseAirFlowDetectedInRack", 4006),
          ("commuSensorTimestampOld", 4014),
          ("commuTempForSensorOutOfRange", 4004),
          ("ctrlAhuOff", 2008),
          ("ctrlMasterSensorTempAboveAcceptBand", 2001),
          ("ctrlNoTciDataForSensorAndAhu", 2005),
          ("ctrlOrphanSensorTempAboveAcceptBand", 2002),
          ("ctrlRegionInfluenceAhuNoSensors", 2004),
          ("ctrlSensorTimestampOld", 2007),
          ("ctrlStarted", 2009),
          ("ctrlStopped", 2010),
          ("ctrlTciDataExistsForSensorsRemovedFromDsc", 2006),
          ("ctrlTempSensorAboveAcceptBand", 2003),
          ("internalSoftwareUnhandledException", 6001),
          ("other", 7001),
          ("webGuiDscAutoMode", 1001),
          ("webGuiDscEmergencyOverrideMode", 1003),
          ("webGuiDscMonitoringMode", 1002),
          ("webGuiDscOff", 1004),
          ("webGuiUserLoggedIn", 1005),
          ("webGuiUserLoggedOut", 1006),
          ("webGuiUserSessionExpired", 1007))
    )


_TrapEventId_Type.__name__ = "Integer32"
_TrapEventId_Object = MibScalar
trapEventId = _TrapEventId_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 8),
    _TrapEventId_Type()
)
trapEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventId.setStatus("mandatory")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 171, 1, 9),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapDscTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 171, 0, 1)
)
trapDscTest.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQDSCCS-MIB", "csRoomName"),
        ("CPQDSCCS-MIB", "csContactName"),
        ("CPQDSCCS-MIB", "csContactPhoneNumber"),
        ("CPQDSCCS-MIB", "csProductName"),
        ("CPQDSCCS-MIB", "csProductId"),
        ("CPQDSCCS-MIB", "csSerialNumber"),
        ("CPQDSCCS-MIB", "csSoftwareVersion"),
        ("CPQDSCCS-MIB", "trapEventId"),
        ("CPQDSCCS-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    trapDscTest.setStatus(
        ""
    )

trapDscCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 171, 0, 2)
)
trapDscCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQDSCCS-MIB", "csRoomName"),
        ("CPQDSCCS-MIB", "csContactName"),
        ("CPQDSCCS-MIB", "csContactPhoneNumber"),
        ("CPQDSCCS-MIB", "csProductName"),
        ("CPQDSCCS-MIB", "csProductId"),
        ("CPQDSCCS-MIB", "csSerialNumber"),
        ("CPQDSCCS-MIB", "csSoftwareVersion"),
        ("CPQDSCCS-MIB", "trapEventId"),
        ("CPQDSCCS-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    trapDscCritical.setStatus(
        ""
    )

trapDscWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 171, 0, 3)
)
trapDscWarning.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQDSCCS-MIB", "csRoomName"),
        ("CPQDSCCS-MIB", "csContactName"),
        ("CPQDSCCS-MIB", "csContactPhoneNumber"),
        ("CPQDSCCS-MIB", "csProductName"),
        ("CPQDSCCS-MIB", "csProductId"),
        ("CPQDSCCS-MIB", "csSerialNumber"),
        ("CPQDSCCS-MIB", "csSoftwareVersion"),
        ("CPQDSCCS-MIB", "trapEventId"),
        ("CPQDSCCS-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    trapDscWarning.setStatus(
        ""
    )

trapDscInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 171, 0, 4)
)
trapDscInformation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQDSCCS-MIB", "csRoomName"),
        ("CPQDSCCS-MIB", "csContactName"),
        ("CPQDSCCS-MIB", "csContactPhoneNumber"),
        ("CPQDSCCS-MIB", "csProductName"),
        ("CPQDSCCS-MIB", "csProductId"),
        ("CPQDSCCS-MIB", "csSerialNumber"),
        ("CPQDSCCS-MIB", "csSoftwareVersion"),
        ("CPQDSCCS-MIB", "trapEventId"),
        ("CPQDSCCS-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    trapDscInformation.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQDSCCS-MIB",
    **{"cpqDsccs": cpqDsccs,
       "trapDscTest": trapDscTest,
       "trapDscCritical": trapDscCritical,
       "trapDscWarning": trapDscWarning,
       "trapDscInformation": trapDscInformation,
       "dsccsTrapInfo": dsccsTrapInfo,
       "csRoomName": csRoomName,
       "csContactName": csContactName,
       "csContactPhoneNumber": csContactPhoneNumber,
       "csProductName": csProductName,
       "csProductId": csProductId,
       "csSerialNumber": csSerialNumber,
       "csSoftwareVersion": csSoftwareVersion,
       "trapEventId": trapEventId,
       "trapDescription": trapDescription}
)
