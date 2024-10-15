# SNMP MIB module (DELL-ASF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-ASF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:46 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wiredformgmt_ObjectIdentity = ObjectIdentity
wiredformgmt = _Wiredformgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183)
)
_Pet_ObjectIdentity = ObjectIdentity
pet = _Pet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1)
)
_AsfPetEvts_ObjectIdentity = ObjectIdentity
asfPetEvts = _AsfPetEvts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1)
)

# Managed Objects groups


# Notification objects

asfTrapIPMIAlertTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1001)
)
if mibBuilder.loadTexts:
    asfTrapIPMIAlertTest.setStatus(
        ""
    )

asfTrapUnderTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65792)
)
if mibBuilder.loadTexts:
    asfTrapUnderTemperatureWarning.setStatus(
        ""
    )

asfTrapUnderTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65794)
)
if mibBuilder.loadTexts:
    asfTrapUnderTemperature.setStatus(
        ""
    )

asfTrapOverTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65799)
)
if mibBuilder.loadTexts:
    asfTrapOverTemperatureWarning.setStatus(
        ""
    )

asfTrapOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65801)
)
if mibBuilder.loadTexts:
    asfTrapOverTemperature.setStatus(
        ""
    )

asfTrapUnderTemperatureWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65920)
)
if mibBuilder.loadTexts:
    asfTrapUnderTemperatureWarningCleared.setStatus(
        ""
    )

asfTrapUnderTemperatureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65922)
)
if mibBuilder.loadTexts:
    asfTrapUnderTemperatureCleared.setStatus(
        ""
    )

asfTrapOverTemperatureWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65927)
)
if mibBuilder.loadTexts:
    asfTrapOverTemperatureWarningCleared.setStatus(
        ""
    )

asfTrapOverTemperatureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 65929)
)
if mibBuilder.loadTexts:
    asfTrapOverTemperatureCleared.setStatus(
        ""
    )

asfTrapUnderVoltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131328)
)
if mibBuilder.loadTexts:
    asfTrapUnderVoltageWarning.setStatus(
        ""
    )

asfTrapUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131330)
)
if mibBuilder.loadTexts:
    asfTrapUnderVoltage.setStatus(
        ""
    )

asfTrapOverVoltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131335)
)
if mibBuilder.loadTexts:
    asfTrapOverVoltageWarning.setStatus(
        ""
    )

asfTrapOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131337)
)
if mibBuilder.loadTexts:
    asfTrapOverVoltage.setStatus(
        ""
    )

asfTrapUnderVoltageWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131456)
)
if mibBuilder.loadTexts:
    asfTrapUnderVoltageWarningCleared.setStatus(
        ""
    )

asfTrapUnderVoltageCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131458)
)
if mibBuilder.loadTexts:
    asfTrapUnderVoltageCleared.setStatus(
        ""
    )

asfTrapOverVoltageWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131463)
)
if mibBuilder.loadTexts:
    asfTrapOverVoltageWarningCleared.setStatus(
        ""
    )

asfTrapVoltageCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131465)
)
if mibBuilder.loadTexts:
    asfTrapVoltageCleared.setStatus(
        ""
    )

asfTrapCriticalDiscreteVoltageCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131840)
)
if mibBuilder.loadTexts:
    asfTrapCriticalDiscreteVoltageCleared.setStatus(
        ""
    )

asfTrapCriticalDiscreteVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 131841)
)
if mibBuilder.loadTexts:
    asfTrapCriticalDiscreteVoltage.setStatus(
        ""
    )

asfTrapFanSpeedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262400)
)
if mibBuilder.loadTexts:
    asfTrapFanSpeedWarning.setStatus(
        ""
    )

asfTrapFanSpeedProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262402)
)
if mibBuilder.loadTexts:
    asfTrapFanSpeedProblem.setStatus(
        ""
    )

asfTrapFanSPeedWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262528)
)
if mibBuilder.loadTexts:
    asfTrapFanSPeedWarningCleared.setStatus(
        ""
    )

asfTrapFanSPeedProblemCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 262530)
)
if mibBuilder.loadTexts:
    asfTrapFanSPeedProblemCleared.setStatus(
        ""
    )

asfTrapFanFullRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 264960)
)
if mibBuilder.loadTexts:
    asfTrapFanFullRedundancy.setStatus(
        ""
    )

asfTrapFanRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 264961)
)
if mibBuilder.loadTexts:
    asfTrapFanRedundancyLost.setStatus(
        ""
    )

asfTrapFanRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 264962)
)
if mibBuilder.loadTexts:
    asfTrapFanRedundancyDegraded.setStatus(
        ""
    )

asfTrapCaseIntrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356096)
)
if mibBuilder.loadTexts:
    asfTrapCaseIntrusion.setStatus(
        ""
    )

asfTrapCaseIntrusionCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 356224)
)
if mibBuilder.loadTexts:
    asfTrapCaseIntrusionCleared.setStatus(
        ""
    )

asfTrapCpuIErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487168)
)
if mibBuilder.loadTexts:
    asfTrapCpuIErr.setStatus(
        ""
    )

asfTrapCpuThermalTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487169)
)
if mibBuilder.loadTexts:
    asfTrapCpuThermalTrip.setStatus(
        ""
    )

asfTrapCpuBistError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487170)
)
if mibBuilder.loadTexts:
    asfTrapCpuBistError.setStatus(
        ""
    )

asfTrapCpuConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487173)
)
if mibBuilder.loadTexts:
    asfTrapCpuConfigError.setStatus(
        ""
    )

asfTrapCpuPresence = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487175)
)
if mibBuilder.loadTexts:
    asfTrapCpuPresence.setStatus(
        ""
    )

asfTrapCpuDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487176)
)
if mibBuilder.loadTexts:
    asfTrapCpuDisabled.setStatus(
        ""
    )

asfTrapCpuThrottle = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487178)
)
if mibBuilder.loadTexts:
    asfTrapCpuThrottle.setStatus(
        ""
    )

asfTrapCpuIErrCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487296)
)
if mibBuilder.loadTexts:
    asfTrapCpuIErrCleared.setStatus(
        ""
    )

asfTrapCpuThermalTripCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487297)
)
if mibBuilder.loadTexts:
    asfTrapCpuThermalTripCleared.setStatus(
        ""
    )

asfTrapCpuBistErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487298)
)
if mibBuilder.loadTexts:
    asfTrapCpuBistErrorCleared.setStatus(
        ""
    )

asfTrapCpuConfigErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487301)
)
if mibBuilder.loadTexts:
    asfTrapCpuConfigErrorCleared.setStatus(
        ""
    )

asfTrapCpuNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487303)
)
if mibBuilder.loadTexts:
    asfTrapCpuNotPresent.setStatus(
        ""
    )

asfTrapCpuEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487304)
)
if mibBuilder.loadTexts:
    asfTrapCpuEnabled.setStatus(
        ""
    )

asfTrapCpuThrottleCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 487306)
)
if mibBuilder.loadTexts:
    asfTrapCpuThrottleCleared.setStatus(
        ""
    )

asfTrapPSFullRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 527104)
)
if mibBuilder.loadTexts:
    asfTrapPSFullRedundancy.setStatus(
        ""
    )

asfTrapPSRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 527105)
)
if mibBuilder.loadTexts:
    asfTrapPSRedundancyLost.setStatus(
        ""
    )

asfTrapPSRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 527106)
)
if mibBuilder.loadTexts:
    asfTrapPSRedundancyDegraded.setStatus(
        ""
    )

asfTrapPsPresenceDeteced = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552704)
)
if mibBuilder.loadTexts:
    asfTrapPsPresenceDeteced.setStatus(
        ""
    )

asfTrapPsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552705)
)
if mibBuilder.loadTexts:
    asfTrapPsFailure.setStatus(
        ""
    )

asfTrapPsPredictiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552706)
)
if mibBuilder.loadTexts:
    asfTrapPsPredictiveFailure.setStatus(
        ""
    )

asfTrapPsAcLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552707)
)
if mibBuilder.loadTexts:
    asfTrapPsAcLost.setStatus(
        ""
    )

asfTrapPSUMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552710)
)
if mibBuilder.loadTexts:
    asfTrapPSUMismatch.setStatus(
        ""
    )

asfTrapSystemPowerExceedsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552711)
)
if mibBuilder.loadTexts:
    asfTrapSystemPowerExceedsWarning.setStatus(
        ""
    )

asfTrapPsPresenceRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552832)
)
if mibBuilder.loadTexts:
    asfTrapPsPresenceRemoved.setStatus(
        ""
    )

asfTrapPsFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552833)
)
if mibBuilder.loadTexts:
    asfTrapPsFailureCleared.setStatus(
        ""
    )

asfTrapPsPredictiveFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552834)
)
if mibBuilder.loadTexts:
    asfTrapPsPredictiveFailureCleared.setStatus(
        ""
    )

asfTrapPsAcBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552835)
)
if mibBuilder.loadTexts:
    asfTrapPsAcBack.setStatus(
        ""
    )

asfTrapPSUMismatchNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552838)
)
if mibBuilder.loadTexts:
    asfTrapPSUMismatchNormal.setStatus(
        ""
    )

asfTrapSystemPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 552839)
)
if mibBuilder.loadTexts:
    asfTrapSystemPowerNormal.setStatus(
        ""
    )

asfTrapSelCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1076994)
)
if mibBuilder.loadTexts:
    asfTrapSelCleared.setStatus(
        ""
    )

asfTrapSelFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1076996)
)
if mibBuilder.loadTexts:
    asfTrapSelFull.setStatus(
        ""
    )

asfTrapSDFullRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1379072)
)
if mibBuilder.loadTexts:
    asfTrapSDFullRedundancy.setStatus(
        ""
    )

asfTrapSDRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1379073)
)
if mibBuilder.loadTexts:
    asfTrapSDRedundancyLost.setStatus(
        ""
    )

asfTrapSDRedundancyDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1379074)
)
if mibBuilder.loadTexts:
    asfTrapSDRedundancyDegraded.setStatus(
        ""
    )

asfTrapModuleSDCardNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1404928)
)
if mibBuilder.loadTexts:
    asfTrapModuleSDCardNotPresent.setStatus(
        ""
    )

asfTrapModuleSDCardFailedError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1404932)
)
if mibBuilder.loadTexts:
    asfTrapModuleSDCardFailedError.setStatus(
        ""
    )

asfTrapModuleSDWriteProtectWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1404935)
)
if mibBuilder.loadTexts:
    asfTrapModuleSDWriteProtectWarning.setStatus(
        ""
    )

asfTrapModuleSDCardPresence = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 1405056)
)
if mibBuilder.loadTexts:
    asfTrapModuleSDCardPresence.setStatus(
        ""
    )

asfTrapASRTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322176)
)
if mibBuilder.loadTexts:
    asfTrapASRTimeout.setStatus(
        ""
    )

asfTrapASROsReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322177)
)
if mibBuilder.loadTexts:
    asfTrapASROsReset.setStatus(
        ""
    )

asfTrapASRPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322178)
)
if mibBuilder.loadTexts:
    asfTrapASRPowerDown.setStatus(
        ""
    )

asfTrapASRPowerCycle = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322179)
)
if mibBuilder.loadTexts:
    asfTrapASRPowerCycle.setStatus(
        ""
    )

asfTrapOverSystemPowerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322180)
)
if mibBuilder.loadTexts:
    asfTrapOverSystemPowerWarning.setStatus(
        ""
    )

asfTrapOverSystemPowerWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322181)
)
if mibBuilder.loadTexts:
    asfTrapOverSystemPowerWarningCleared.setStatus(
        ""
    )

asfTrapOverSystemPowerCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322182)
)
if mibBuilder.loadTexts:
    asfTrapOverSystemPowerCritical.setStatus(
        ""
    )

asfTrapOverSystemPowerCriticalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2322183)
)
if mibBuilder.loadTexts:
    asfTrapOverSystemPowerCriticalCleared.setStatus(
        ""
    )

asfTrapBatteryLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2715392)
)
if mibBuilder.loadTexts:
    asfTrapBatteryLowWarning.setStatus(
        ""
    )

asfTrapBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2715393)
)
if mibBuilder.loadTexts:
    asfTrapBatteryFailure.setStatus(
        ""
    )

asfTrapBatteryLowWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2715520)
)
if mibBuilder.loadTexts:
    asfTrapBatteryLowWarningCleared.setStatus(
        ""
    )

asfTrapBatteryFailCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 2715521)
)
if mibBuilder.loadTexts:
    asfTrapBatteryFailCleared.setStatus(
        ""
    )

asfTrapSystemPowerExceedsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 12611334)
)
if mibBuilder.loadTexts:
    asfTrapSystemPowerExceedsError.setStatus(
        ""
    )

asfTrapSystemPowerExceedsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 12611462)
)
if mibBuilder.loadTexts:
    asfTrapSystemPowerExceedsCleared.setStatus(
        ""
    )

asfTrapInternalDualSDModuleRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13175552)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleRedundant.setStatus(
        ""
    )

asfTrapInternalDualSDModuleRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13175553)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleRedundancyLost.setStatus(
        ""
    )

asfTrapInternalDualSDModuleNotRedundant = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13175555)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleNotRedundant.setStatus(
        ""
    )

asfTrapInternalDualSDModulePresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201152)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModulePresent.setStatus(
        ""
    )

asfTrapInternalDualSDModuleOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201153)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleOffline.setStatus(
        ""
    )

asfTrapInternalDualSDModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201154)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleFailure.setStatus(
        ""
    )

asfTrapInternalDualSDModuleWriteProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201155)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleWriteProtected.setStatus(
        ""
    )

asfTrapInternalDualSDModuleAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201280)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleAbsent.setStatus(
        ""
    )

asfTrapInternalDualSDModuleOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201281)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleOnline.setStatus(
        ""
    )

asfTrapInternalDualSDModuleNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201282)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleNormal.setStatus(
        ""
    )

asfTrapInternalDualSDModuleWriteable = NotificationType(
    (1, 3, 6, 1, 4, 1, 3183, 1, 1, 0, 13201283)
)
if mibBuilder.loadTexts:
    asfTrapInternalDualSDModuleWriteable.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-ASF-MIB",
    **{"wiredformgmt": wiredformgmt,
       "pet": pet,
       "asfPetEvts": asfPetEvts,
       "asfTrapIPMIAlertTest": asfTrapIPMIAlertTest,
       "asfTrapUnderTemperatureWarning": asfTrapUnderTemperatureWarning,
       "asfTrapUnderTemperature": asfTrapUnderTemperature,
       "asfTrapOverTemperatureWarning": asfTrapOverTemperatureWarning,
       "asfTrapOverTemperature": asfTrapOverTemperature,
       "asfTrapUnderTemperatureWarningCleared": asfTrapUnderTemperatureWarningCleared,
       "asfTrapUnderTemperatureCleared": asfTrapUnderTemperatureCleared,
       "asfTrapOverTemperatureWarningCleared": asfTrapOverTemperatureWarningCleared,
       "asfTrapOverTemperatureCleared": asfTrapOverTemperatureCleared,
       "asfTrapUnderVoltageWarning": asfTrapUnderVoltageWarning,
       "asfTrapUnderVoltage": asfTrapUnderVoltage,
       "asfTrapOverVoltageWarning": asfTrapOverVoltageWarning,
       "asfTrapOverVoltage": asfTrapOverVoltage,
       "asfTrapUnderVoltageWarningCleared": asfTrapUnderVoltageWarningCleared,
       "asfTrapUnderVoltageCleared": asfTrapUnderVoltageCleared,
       "asfTrapOverVoltageWarningCleared": asfTrapOverVoltageWarningCleared,
       "asfTrapVoltageCleared": asfTrapVoltageCleared,
       "asfTrapCriticalDiscreteVoltageCleared": asfTrapCriticalDiscreteVoltageCleared,
       "asfTrapCriticalDiscreteVoltage": asfTrapCriticalDiscreteVoltage,
       "asfTrapFanSpeedWarning": asfTrapFanSpeedWarning,
       "asfTrapFanSpeedProblem": asfTrapFanSpeedProblem,
       "asfTrapFanSPeedWarningCleared": asfTrapFanSPeedWarningCleared,
       "asfTrapFanSPeedProblemCleared": asfTrapFanSPeedProblemCleared,
       "asfTrapFanFullRedundancy": asfTrapFanFullRedundancy,
       "asfTrapFanRedundancyLost": asfTrapFanRedundancyLost,
       "asfTrapFanRedundancyDegraded": asfTrapFanRedundancyDegraded,
       "asfTrapCaseIntrusion": asfTrapCaseIntrusion,
       "asfTrapCaseIntrusionCleared": asfTrapCaseIntrusionCleared,
       "asfTrapCpuIErr": asfTrapCpuIErr,
       "asfTrapCpuThermalTrip": asfTrapCpuThermalTrip,
       "asfTrapCpuBistError": asfTrapCpuBistError,
       "asfTrapCpuConfigError": asfTrapCpuConfigError,
       "asfTrapCpuPresence": asfTrapCpuPresence,
       "asfTrapCpuDisabled": asfTrapCpuDisabled,
       "asfTrapCpuThrottle": asfTrapCpuThrottle,
       "asfTrapCpuIErrCleared": asfTrapCpuIErrCleared,
       "asfTrapCpuThermalTripCleared": asfTrapCpuThermalTripCleared,
       "asfTrapCpuBistErrorCleared": asfTrapCpuBistErrorCleared,
       "asfTrapCpuConfigErrorCleared": asfTrapCpuConfigErrorCleared,
       "asfTrapCpuNotPresent": asfTrapCpuNotPresent,
       "asfTrapCpuEnabled": asfTrapCpuEnabled,
       "asfTrapCpuThrottleCleared": asfTrapCpuThrottleCleared,
       "asfTrapPSFullRedundancy": asfTrapPSFullRedundancy,
       "asfTrapPSRedundancyLost": asfTrapPSRedundancyLost,
       "asfTrapPSRedundancyDegraded": asfTrapPSRedundancyDegraded,
       "asfTrapPsPresenceDeteced": asfTrapPsPresenceDeteced,
       "asfTrapPsFailure": asfTrapPsFailure,
       "asfTrapPsPredictiveFailure": asfTrapPsPredictiveFailure,
       "asfTrapPsAcLost": asfTrapPsAcLost,
       "asfTrapPSUMismatch": asfTrapPSUMismatch,
       "asfTrapSystemPowerExceedsWarning": asfTrapSystemPowerExceedsWarning,
       "asfTrapPsPresenceRemoved": asfTrapPsPresenceRemoved,
       "asfTrapPsFailureCleared": asfTrapPsFailureCleared,
       "asfTrapPsPredictiveFailureCleared": asfTrapPsPredictiveFailureCleared,
       "asfTrapPsAcBack": asfTrapPsAcBack,
       "asfTrapPSUMismatchNormal": asfTrapPSUMismatchNormal,
       "asfTrapSystemPowerNormal": asfTrapSystemPowerNormal,
       "asfTrapSelCleared": asfTrapSelCleared,
       "asfTrapSelFull": asfTrapSelFull,
       "asfTrapSDFullRedundancy": asfTrapSDFullRedundancy,
       "asfTrapSDRedundancyLost": asfTrapSDRedundancyLost,
       "asfTrapSDRedundancyDegraded": asfTrapSDRedundancyDegraded,
       "asfTrapModuleSDCardNotPresent": asfTrapModuleSDCardNotPresent,
       "asfTrapModuleSDCardFailedError": asfTrapModuleSDCardFailedError,
       "asfTrapModuleSDWriteProtectWarning": asfTrapModuleSDWriteProtectWarning,
       "asfTrapModuleSDCardPresence": asfTrapModuleSDCardPresence,
       "asfTrapASRTimeout": asfTrapASRTimeout,
       "asfTrapASROsReset": asfTrapASROsReset,
       "asfTrapASRPowerDown": asfTrapASRPowerDown,
       "asfTrapASRPowerCycle": asfTrapASRPowerCycle,
       "asfTrapOverSystemPowerWarning": asfTrapOverSystemPowerWarning,
       "asfTrapOverSystemPowerWarningCleared": asfTrapOverSystemPowerWarningCleared,
       "asfTrapOverSystemPowerCritical": asfTrapOverSystemPowerCritical,
       "asfTrapOverSystemPowerCriticalCleared": asfTrapOverSystemPowerCriticalCleared,
       "asfTrapBatteryLowWarning": asfTrapBatteryLowWarning,
       "asfTrapBatteryFailure": asfTrapBatteryFailure,
       "asfTrapBatteryLowWarningCleared": asfTrapBatteryLowWarningCleared,
       "asfTrapBatteryFailCleared": asfTrapBatteryFailCleared,
       "asfTrapSystemPowerExceedsError": asfTrapSystemPowerExceedsError,
       "asfTrapSystemPowerExceedsCleared": asfTrapSystemPowerExceedsCleared,
       "asfTrapInternalDualSDModuleRedundant": asfTrapInternalDualSDModuleRedundant,
       "asfTrapInternalDualSDModuleRedundancyLost": asfTrapInternalDualSDModuleRedundancyLost,
       "asfTrapInternalDualSDModuleNotRedundant": asfTrapInternalDualSDModuleNotRedundant,
       "asfTrapInternalDualSDModulePresent": asfTrapInternalDualSDModulePresent,
       "asfTrapInternalDualSDModuleOffline": asfTrapInternalDualSDModuleOffline,
       "asfTrapInternalDualSDModuleFailure": asfTrapInternalDualSDModuleFailure,
       "asfTrapInternalDualSDModuleWriteProtected": asfTrapInternalDualSDModuleWriteProtected,
       "asfTrapInternalDualSDModuleAbsent": asfTrapInternalDualSDModuleAbsent,
       "asfTrapInternalDualSDModuleOnline": asfTrapInternalDualSDModuleOnline,
       "asfTrapInternalDualSDModuleNormal": asfTrapInternalDualSDModuleNormal,
       "asfTrapInternalDualSDModuleWriteable": asfTrapInternalDualSDModuleWriteable}
)
