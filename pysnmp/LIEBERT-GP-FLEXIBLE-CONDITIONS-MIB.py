# SNMP MIB module (LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:55 2024
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

(lgpFlexConditions,) = mibBuilder.importSymbols(
    "LIEBERT-GP-CONDITIONS-MIB",
    "lgpFlexConditions")

(liebertFlexibleConditionsModuleReg,) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "liebertFlexibleConditionsModuleReg")

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

liebertGlobalProductsFlexibleConditionsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 11, 1)
)
liebertGlobalProductsFlexibleConditionsModule.setRevisions(
        ("2016-06-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpFlexConditionsWellKnown_ObjectIdentity = ObjectIdentity
lgpFlexConditionsWellKnown = _LgpFlexConditionsWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1)
)
_LgpCondId4122SystemInputPowerProblem_ObjectIdentity = ObjectIdentity
lgpCondId4122SystemInputPowerProblem = _LgpCondId4122SystemInputPowerProblem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4122)
)
if mibBuilder.loadTexts:
    lgpCondId4122SystemInputPowerProblem.setStatus("current")
_LgpCondId4132BypassOverloadPhaseA_ObjectIdentity = ObjectIdentity
lgpCondId4132BypassOverloadPhaseA = _LgpCondId4132BypassOverloadPhaseA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4132)
)
if mibBuilder.loadTexts:
    lgpCondId4132BypassOverloadPhaseA.setStatus("current")
_LgpCondId4133BypassOverloadPhaseB_ObjectIdentity = ObjectIdentity
lgpCondId4133BypassOverloadPhaseB = _LgpCondId4133BypassOverloadPhaseB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4133)
)
if mibBuilder.loadTexts:
    lgpCondId4133BypassOverloadPhaseB.setStatus("current")
_LgpCondId4134BypassOverloadPhaseC_ObjectIdentity = ObjectIdentity
lgpCondId4134BypassOverloadPhaseC = _LgpCondId4134BypassOverloadPhaseC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4134)
)
if mibBuilder.loadTexts:
    lgpCondId4134BypassOverloadPhaseC.setStatus("current")
_LgpCondId4135BypassNotAvailable_ObjectIdentity = ObjectIdentity
lgpCondId4135BypassNotAvailable = _LgpCondId4135BypassNotAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4135)
)
if mibBuilder.loadTexts:
    lgpCondId4135BypassNotAvailable.setStatus("current")
_LgpCondId4137BypassAutoRetransferPrimed_ObjectIdentity = ObjectIdentity
lgpCondId4137BypassAutoRetransferPrimed = _LgpCondId4137BypassAutoRetransferPrimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4137)
)
if mibBuilder.loadTexts:
    lgpCondId4137BypassAutoRetransferPrimed.setStatus("current")
_LgpCondId4138BypassAutoRetransferFailed_ObjectIdentity = ObjectIdentity
lgpCondId4138BypassAutoRetransferFailed = _LgpCondId4138BypassAutoRetransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4138)
)
if mibBuilder.loadTexts:
    lgpCondId4138BypassAutoRetransferFailed.setStatus("current")
_LgpCondId4139BypassExcessAutoRetransfers_ObjectIdentity = ObjectIdentity
lgpCondId4139BypassExcessAutoRetransfers = _LgpCondId4139BypassExcessAutoRetransfers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4139)
)
if mibBuilder.loadTexts:
    lgpCondId4139BypassExcessAutoRetransfers.setStatus("current")
_LgpCondId4140BypassRestartInhibitExternal_ObjectIdentity = ObjectIdentity
lgpCondId4140BypassRestartInhibitExternal = _LgpCondId4140BypassRestartInhibitExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4140)
)
if mibBuilder.loadTexts:
    lgpCondId4140BypassRestartInhibitExternal.setStatus("current")
_LgpCondId4141BypassBreakerClosed_ObjectIdentity = ObjectIdentity
lgpCondId4141BypassBreakerClosed = _LgpCondId4141BypassBreakerClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4141)
)
if mibBuilder.loadTexts:
    lgpCondId4141BypassBreakerClosed.setStatus("current")
_LgpCondId4142BypassStaticSwitchOverload_ObjectIdentity = ObjectIdentity
lgpCondId4142BypassStaticSwitchOverload = _LgpCondId4142BypassStaticSwitchOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4142)
)
if mibBuilder.loadTexts:
    lgpCondId4142BypassStaticSwitchOverload.setStatus("current")
_LgpCondId4143BypassStaticSwitchUnavailable_ObjectIdentity = ObjectIdentity
lgpCondId4143BypassStaticSwitchUnavailable = _LgpCondId4143BypassStaticSwitchUnavailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4143)
)
if mibBuilder.loadTexts:
    lgpCondId4143BypassStaticSwitchUnavailable.setStatus("current")
_LgpCondId4144BypassExcessivePulseParallel_ObjectIdentity = ObjectIdentity
lgpCondId4144BypassExcessivePulseParallel = _LgpCondId4144BypassExcessivePulseParallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4144)
)
if mibBuilder.loadTexts:
    lgpCondId4144BypassExcessivePulseParallel.setStatus("current")
_LgpCondId4145BypassAutoTransferFailed_ObjectIdentity = ObjectIdentity
lgpCondId4145BypassAutoTransferFailed = _LgpCondId4145BypassAutoTransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4145)
)
if mibBuilder.loadTexts:
    lgpCondId4145BypassAutoTransferFailed.setStatus("current")
_LgpCondId4146SystemInputPhsRotationError_ObjectIdentity = ObjectIdentity
lgpCondId4146SystemInputPhsRotationError = _LgpCondId4146SystemInputPhsRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4146)
)
if mibBuilder.loadTexts:
    lgpCondId4146SystemInputPhsRotationError.setStatus("current")
_LgpCondId4147SystemInputCurrentLimit_ObjectIdentity = ObjectIdentity
lgpCondId4147SystemInputCurrentLimit = _LgpCondId4147SystemInputCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4147)
)
if mibBuilder.loadTexts:
    lgpCondId4147SystemInputCurrentLimit.setStatus("current")
_LgpCondId4162BatteryLow_ObjectIdentity = ObjectIdentity
lgpCondId4162BatteryLow = _LgpCondId4162BatteryLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4162)
)
if mibBuilder.loadTexts:
    lgpCondId4162BatteryLow.setStatus("current")
_LgpCondId4163OutputOffEndofDischarge_ObjectIdentity = ObjectIdentity
lgpCondId4163OutputOffEndofDischarge = _LgpCondId4163OutputOffEndofDischarge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4163)
)
if mibBuilder.loadTexts:
    lgpCondId4163OutputOffEndofDischarge.setStatus("current")
_LgpCondId4164BatteryChargingError_ObjectIdentity = ObjectIdentity
lgpCondId4164BatteryChargingError = _LgpCondId4164BatteryChargingError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4164)
)
if mibBuilder.loadTexts:
    lgpCondId4164BatteryChargingError.setStatus("current")
_LgpCondId4165BatteryChargingReducedExtrnl_ObjectIdentity = ObjectIdentity
lgpCondId4165BatteryChargingReducedExtrnl = _LgpCondId4165BatteryChargingReducedExtrnl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4165)
)
if mibBuilder.loadTexts:
    lgpCondId4165BatteryChargingReducedExtrnl.setStatus("current")
_LgpCondId4166BatteryCapacityLow_ObjectIdentity = ObjectIdentity
lgpCondId4166BatteryCapacityLow = _LgpCondId4166BatteryCapacityLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4166)
)
if mibBuilder.loadTexts:
    lgpCondId4166BatteryCapacityLow.setStatus("current")
_LgpCondId4167OutputOff_ObjectIdentity = ObjectIdentity
lgpCondId4167OutputOff = _LgpCondId4167OutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4167)
)
if mibBuilder.loadTexts:
    lgpCondId4167OutputOff.setStatus("current")
_LgpCondId4168BatteryDischarging_ObjectIdentity = ObjectIdentity
lgpCondId4168BatteryDischarging = _LgpCondId4168BatteryDischarging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4168)
)
if mibBuilder.loadTexts:
    lgpCondId4168BatteryDischarging.setStatus("current")
_LgpCondId4169BatteryTemperatureImbalance_ObjectIdentity = ObjectIdentity
lgpCondId4169BatteryTemperatureImbalance = _LgpCondId4169BatteryTemperatureImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4169)
)
if mibBuilder.loadTexts:
    lgpCondId4169BatteryTemperatureImbalance.setStatus("current")
_LgpCondId4170BatteryEqualize_ObjectIdentity = ObjectIdentity
lgpCondId4170BatteryEqualize = _LgpCondId4170BatteryEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4170)
)
if mibBuilder.loadTexts:
    lgpCondId4170BatteryEqualize.setStatus("current")
_LgpCondId4171BatteryManualTestInProgress_ObjectIdentity = ObjectIdentity
lgpCondId4171BatteryManualTestInProgress = _LgpCondId4171BatteryManualTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4171)
)
if mibBuilder.loadTexts:
    lgpCondId4171BatteryManualTestInProgress.setStatus("current")
_LgpCondId4172BatteryAutoTestInProgress_ObjectIdentity = ObjectIdentity
lgpCondId4172BatteryAutoTestInProgress = _LgpCondId4172BatteryAutoTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4172)
)
if mibBuilder.loadTexts:
    lgpCondId4172BatteryAutoTestInProgress.setStatus("current")
_LgpCondId4173MainBatteryDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpCondId4173MainBatteryDisconnectOpen = _LgpCondId4173MainBatteryDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4173)
)
if mibBuilder.loadTexts:
    lgpCondId4173MainBatteryDisconnectOpen.setStatus("current")
_LgpCondId4174BatteryTemperatureSensorFault_ObjectIdentity = ObjectIdentity
lgpCondId4174BatteryTemperatureSensorFault = _LgpCondId4174BatteryTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4174)
)
if mibBuilder.loadTexts:
    lgpCondId4174BatteryTemperatureSensorFault.setStatus("current")
_LgpCondId4175BypassFrequencyError_ObjectIdentity = ObjectIdentity
lgpCondId4175BypassFrequencyError = _LgpCondId4175BypassFrequencyError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4175)
)
if mibBuilder.loadTexts:
    lgpCondId4175BypassFrequencyError.setStatus("current")
_LgpCondId4176BatteryCircuitBreaker1Open_ObjectIdentity = ObjectIdentity
lgpCondId4176BatteryCircuitBreaker1Open = _LgpCondId4176BatteryCircuitBreaker1Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4176)
)
if mibBuilder.loadTexts:
    lgpCondId4176BatteryCircuitBreaker1Open.setStatus("current")
_LgpCondId4177BatteryBreaker1OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4177BatteryBreaker1OpenFailure = _LgpCondId4177BatteryBreaker1OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4177)
)
if mibBuilder.loadTexts:
    lgpCondId4177BatteryBreaker1OpenFailure.setStatus("current")
_LgpCondId4178BatteryBreaker1CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4178BatteryBreaker1CloseFailure = _LgpCondId4178BatteryBreaker1CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4178)
)
if mibBuilder.loadTexts:
    lgpCondId4178BatteryBreaker1CloseFailure.setStatus("current")
_LgpCondId4179BatteryCircuitBreaker2Open_ObjectIdentity = ObjectIdentity
lgpCondId4179BatteryCircuitBreaker2Open = _LgpCondId4179BatteryCircuitBreaker2Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4179)
)
if mibBuilder.loadTexts:
    lgpCondId4179BatteryCircuitBreaker2Open.setStatus("current")
_LgpCondId4180BatteryBreaker2OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4180BatteryBreaker2OpenFailure = _LgpCondId4180BatteryBreaker2OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4180)
)
if mibBuilder.loadTexts:
    lgpCondId4180BatteryBreaker2OpenFailure.setStatus("current")
_LgpCondId4181BatteryBreaker2CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4181BatteryBreaker2CloseFailure = _LgpCondId4181BatteryBreaker2CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4181)
)
if mibBuilder.loadTexts:
    lgpCondId4181BatteryBreaker2CloseFailure.setStatus("current")
_LgpCondId4182BatteryCircuitBreaker3Open_ObjectIdentity = ObjectIdentity
lgpCondId4182BatteryCircuitBreaker3Open = _LgpCondId4182BatteryCircuitBreaker3Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4182)
)
if mibBuilder.loadTexts:
    lgpCondId4182BatteryCircuitBreaker3Open.setStatus("current")
_LgpCondId4183BatteryBreaker3OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4183BatteryBreaker3OpenFailure = _LgpCondId4183BatteryBreaker3OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4183)
)
if mibBuilder.loadTexts:
    lgpCondId4183BatteryBreaker3OpenFailure.setStatus("current")
_LgpCondId4184BatteryBreaker3CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4184BatteryBreaker3CloseFailure = _LgpCondId4184BatteryBreaker3CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4184)
)
if mibBuilder.loadTexts:
    lgpCondId4184BatteryBreaker3CloseFailure.setStatus("current")
_LgpCondId4185BatteryCircuitBreaker4Open_ObjectIdentity = ObjectIdentity
lgpCondId4185BatteryCircuitBreaker4Open = _LgpCondId4185BatteryCircuitBreaker4Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4185)
)
if mibBuilder.loadTexts:
    lgpCondId4185BatteryCircuitBreaker4Open.setStatus("current")
_LgpCondId4186BatteryBreaker4OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4186BatteryBreaker4OpenFailure = _LgpCondId4186BatteryBreaker4OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4186)
)
if mibBuilder.loadTexts:
    lgpCondId4186BatteryBreaker4OpenFailure.setStatus("current")
_LgpCondId4187BatteryBreaker4CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4187BatteryBreaker4CloseFailure = _LgpCondId4187BatteryBreaker4CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4187)
)
if mibBuilder.loadTexts:
    lgpCondId4187BatteryBreaker4CloseFailure.setStatus("current")
_LgpCondId4188BatteryCircuitBreaker5Open_ObjectIdentity = ObjectIdentity
lgpCondId4188BatteryCircuitBreaker5Open = _LgpCondId4188BatteryCircuitBreaker5Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4188)
)
if mibBuilder.loadTexts:
    lgpCondId4188BatteryCircuitBreaker5Open.setStatus("current")
_LgpCondId4189BatteryBreaker5OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4189BatteryBreaker5OpenFailure = _LgpCondId4189BatteryBreaker5OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4189)
)
if mibBuilder.loadTexts:
    lgpCondId4189BatteryBreaker5OpenFailure.setStatus("current")
_LgpCondId4190BatteryBreaker5CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4190BatteryBreaker5CloseFailure = _LgpCondId4190BatteryBreaker5CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4190)
)
if mibBuilder.loadTexts:
    lgpCondId4190BatteryBreaker5CloseFailure.setStatus("current")
_LgpCondId4191BatteryCircuitBreaker6Open_ObjectIdentity = ObjectIdentity
lgpCondId4191BatteryCircuitBreaker6Open = _LgpCondId4191BatteryCircuitBreaker6Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4191)
)
if mibBuilder.loadTexts:
    lgpCondId4191BatteryCircuitBreaker6Open.setStatus("current")
_LgpCondId4192BatteryBreaker6OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4192BatteryBreaker6OpenFailure = _LgpCondId4192BatteryBreaker6OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4192)
)
if mibBuilder.loadTexts:
    lgpCondId4192BatteryBreaker6OpenFailure.setStatus("current")
_LgpCondId4193BatteryBreaker6CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4193BatteryBreaker6CloseFailure = _LgpCondId4193BatteryBreaker6CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4193)
)
if mibBuilder.loadTexts:
    lgpCondId4193BatteryBreaker6CloseFailure.setStatus("current")
_LgpCondId4194BatteryCircuitBreaker7Open_ObjectIdentity = ObjectIdentity
lgpCondId4194BatteryCircuitBreaker7Open = _LgpCondId4194BatteryCircuitBreaker7Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4194)
)
if mibBuilder.loadTexts:
    lgpCondId4194BatteryCircuitBreaker7Open.setStatus("current")
_LgpCondId4195BatteryBreaker7OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4195BatteryBreaker7OpenFailure = _LgpCondId4195BatteryBreaker7OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4195)
)
if mibBuilder.loadTexts:
    lgpCondId4195BatteryBreaker7OpenFailure.setStatus("current")
_LgpCondId4196BatteryBreaker7CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4196BatteryBreaker7CloseFailure = _LgpCondId4196BatteryBreaker7CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4196)
)
if mibBuilder.loadTexts:
    lgpCondId4196BatteryBreaker7CloseFailure.setStatus("current")
_LgpCondId4197BatteryCircuitBreaker8Open_ObjectIdentity = ObjectIdentity
lgpCondId4197BatteryCircuitBreaker8Open = _LgpCondId4197BatteryCircuitBreaker8Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4197)
)
if mibBuilder.loadTexts:
    lgpCondId4197BatteryCircuitBreaker8Open.setStatus("current")
_LgpCondId4198BatteryBreaker8OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4198BatteryBreaker8OpenFailure = _LgpCondId4198BatteryBreaker8OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4198)
)
if mibBuilder.loadTexts:
    lgpCondId4198BatteryBreaker8OpenFailure.setStatus("current")
_LgpCondId4199BatteryBreaker8CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4199BatteryBreaker8CloseFailure = _LgpCondId4199BatteryBreaker8CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4199)
)
if mibBuilder.loadTexts:
    lgpCondId4199BatteryBreaker8CloseFailure.setStatus("current")
_LgpCondId4200BatteryChargingInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4200BatteryChargingInhibited = _LgpCondId4200BatteryChargingInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4200)
)
if mibBuilder.loadTexts:
    lgpCondId4200BatteryChargingInhibited.setStatus("current")
_LgpCondId4213SystemShutdownEPO_ObjectIdentity = ObjectIdentity
lgpCondId4213SystemShutdownEPO = _LgpCondId4213SystemShutdownEPO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4213)
)
if mibBuilder.loadTexts:
    lgpCondId4213SystemShutdownEPO.setStatus("current")
_LgpCondId4214SystemShutdownREPO_ObjectIdentity = ObjectIdentity
lgpCondId4214SystemShutdownREPO = _LgpCondId4214SystemShutdownREPO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4214)
)
if mibBuilder.loadTexts:
    lgpCondId4214SystemShutdownREPO.setStatus("current")
_LgpCondId4215SystemOutputOff_ObjectIdentity = ObjectIdentity
lgpCondId4215SystemOutputOff = _LgpCondId4215SystemOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4215)
)
if mibBuilder.loadTexts:
    lgpCondId4215SystemOutputOff.setStatus("current")
_LgpCondId4216BypassBackfeedDetected_ObjectIdentity = ObjectIdentity
lgpCondId4216BypassBackfeedDetected = _LgpCondId4216BypassBackfeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4216)
)
if mibBuilder.loadTexts:
    lgpCondId4216BypassBackfeedDetected.setStatus("current")
_LgpCondId4217BypassManualXfrInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4217BypassManualXfrInhibited = _LgpCondId4217BypassManualXfrInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4217)
)
if mibBuilder.loadTexts:
    lgpCondId4217BypassManualXfrInhibited.setStatus("current")
_LgpCondId4218BypassManualRexfrInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4218BypassManualRexfrInhibited = _LgpCondId4218BypassManualRexfrInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4218)
)
if mibBuilder.loadTexts:
    lgpCondId4218BypassManualRexfrInhibited.setStatus("current")
_LgpCondId4219BatteryOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4219BatteryOverTemperature = _LgpCondId4219BatteryOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4219)
)
if mibBuilder.loadTexts:
    lgpCondId4219BatteryOverTemperature.setStatus("current")
_LgpCondId4220BatteryExternalMonitor1_ObjectIdentity = ObjectIdentity
lgpCondId4220BatteryExternalMonitor1 = _LgpCondId4220BatteryExternalMonitor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4220)
)
if mibBuilder.loadTexts:
    lgpCondId4220BatteryExternalMonitor1.setStatus("current")
_LgpCondId4221BatteryExternalMonitor2_ObjectIdentity = ObjectIdentity
lgpCondId4221BatteryExternalMonitor2 = _LgpCondId4221BatteryExternalMonitor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4221)
)
if mibBuilder.loadTexts:
    lgpCondId4221BatteryExternalMonitor2.setStatus("current")
_LgpCondId4222BatteryGroundFault_ObjectIdentity = ObjectIdentity
lgpCondId4222BatteryGroundFault = _LgpCondId4222BatteryGroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4222)
)
if mibBuilder.loadTexts:
    lgpCondId4222BatteryGroundFault.setStatus("current")
_LgpCondId4229EmergencyPowerOffLatched_ObjectIdentity = ObjectIdentity
lgpCondId4229EmergencyPowerOffLatched = _LgpCondId4229EmergencyPowerOffLatched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4229)
)
if mibBuilder.loadTexts:
    lgpCondId4229EmergencyPowerOffLatched.setStatus("current")
_LgpCondId4230SystemOutputLowPowerFactor_ObjectIdentity = ObjectIdentity
lgpCondId4230SystemOutputLowPowerFactor = _LgpCondId4230SystemOutputLowPowerFactor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4230)
)
if mibBuilder.loadTexts:
    lgpCondId4230SystemOutputLowPowerFactor.setStatus("current")
_LgpCondId4231OutputCurrentExceedsThreshold_ObjectIdentity = ObjectIdentity
lgpCondId4231OutputCurrentExceedsThreshold = _LgpCondId4231OutputCurrentExceedsThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4231)
)
if mibBuilder.loadTexts:
    lgpCondId4231OutputCurrentExceedsThreshold.setStatus("current")
_LgpCondId4233InverterFailure_ObjectIdentity = ObjectIdentity
lgpCondId4233InverterFailure = _LgpCondId4233InverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4233)
)
if mibBuilder.loadTexts:
    lgpCondId4233InverterFailure.setStatus("current")
_LgpCondId4234InverterOverloadPhaseA_ObjectIdentity = ObjectIdentity
lgpCondId4234InverterOverloadPhaseA = _LgpCondId4234InverterOverloadPhaseA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4234)
)
if mibBuilder.loadTexts:
    lgpCondId4234InverterOverloadPhaseA.setStatus("current")
_LgpCondId4235InverterOverloadPhaseB_ObjectIdentity = ObjectIdentity
lgpCondId4235InverterOverloadPhaseB = _LgpCondId4235InverterOverloadPhaseB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4235)
)
if mibBuilder.loadTexts:
    lgpCondId4235InverterOverloadPhaseB.setStatus("current")
_LgpCondId4236InverterOverloadPhaseC_ObjectIdentity = ObjectIdentity
lgpCondId4236InverterOverloadPhaseC = _LgpCondId4236InverterOverloadPhaseC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4236)
)
if mibBuilder.loadTexts:
    lgpCondId4236InverterOverloadPhaseC.setStatus("current")
_LgpCondId4237InverterInhibitExternal_ObjectIdentity = ObjectIdentity
lgpCondId4237InverterInhibitExternal = _LgpCondId4237InverterInhibitExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4237)
)
if mibBuilder.loadTexts:
    lgpCondId4237InverterInhibitExternal.setStatus("current")
_LgpCondId4238InverterOutBreakerOpenFail_ObjectIdentity = ObjectIdentity
lgpCondId4238InverterOutBreakerOpenFail = _LgpCondId4238InverterOutBreakerOpenFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4238)
)
if mibBuilder.loadTexts:
    lgpCondId4238InverterOutBreakerOpenFail.setStatus("current")
_LgpCondId4239InverterOutBreakerCloseFail_ObjectIdentity = ObjectIdentity
lgpCondId4239InverterOutBreakerCloseFail = _LgpCondId4239InverterOutBreakerCloseFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4239)
)
if mibBuilder.loadTexts:
    lgpCondId4239InverterOutBreakerCloseFail.setStatus("current")
_LgpCondId4270InputContact01_ObjectIdentity = ObjectIdentity
lgpCondId4270InputContact01 = _LgpCondId4270InputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4270)
)
if mibBuilder.loadTexts:
    lgpCondId4270InputContact01.setStatus("current")
_LgpCondId4271InputContact02_ObjectIdentity = ObjectIdentity
lgpCondId4271InputContact02 = _LgpCondId4271InputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4271)
)
if mibBuilder.loadTexts:
    lgpCondId4271InputContact02.setStatus("current")
_LgpCondId4272InputContact03_ObjectIdentity = ObjectIdentity
lgpCondId4272InputContact03 = _LgpCondId4272InputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4272)
)
if mibBuilder.loadTexts:
    lgpCondId4272InputContact03.setStatus("current")
_LgpCondId4273InputContact04_ObjectIdentity = ObjectIdentity
lgpCondId4273InputContact04 = _LgpCondId4273InputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4273)
)
if mibBuilder.loadTexts:
    lgpCondId4273InputContact04.setStatus("current")
_LgpCondId4274InputContact05_ObjectIdentity = ObjectIdentity
lgpCondId4274InputContact05 = _LgpCondId4274InputContact05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4274)
)
if mibBuilder.loadTexts:
    lgpCondId4274InputContact05.setStatus("current")
_LgpCondId4275InputContact06_ObjectIdentity = ObjectIdentity
lgpCondId4275InputContact06 = _LgpCondId4275InputContact06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4275)
)
if mibBuilder.loadTexts:
    lgpCondId4275InputContact06.setStatus("current")
_LgpCondId4276InputContact07_ObjectIdentity = ObjectIdentity
lgpCondId4276InputContact07 = _LgpCondId4276InputContact07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4276)
)
if mibBuilder.loadTexts:
    lgpCondId4276InputContact07.setStatus("current")
_LgpCondId4277InputContact08_ObjectIdentity = ObjectIdentity
lgpCondId4277InputContact08 = _LgpCondId4277InputContact08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4277)
)
if mibBuilder.loadTexts:
    lgpCondId4277InputContact08.setStatus("current")
_LgpCondId4278InputContact09_ObjectIdentity = ObjectIdentity
lgpCondId4278InputContact09 = _LgpCondId4278InputContact09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4278)
)
if mibBuilder.loadTexts:
    lgpCondId4278InputContact09.setStatus("current")
_LgpCondId4279InputContact10_ObjectIdentity = ObjectIdentity
lgpCondId4279InputContact10 = _LgpCondId4279InputContact10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4279)
)
if mibBuilder.loadTexts:
    lgpCondId4279InputContact10.setStatus("current")
_LgpCondId4280InputContact11_ObjectIdentity = ObjectIdentity
lgpCondId4280InputContact11 = _LgpCondId4280InputContact11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4280)
)
if mibBuilder.loadTexts:
    lgpCondId4280InputContact11.setStatus("current")
_LgpCondId4281InputContact12_ObjectIdentity = ObjectIdentity
lgpCondId4281InputContact12 = _LgpCondId4281InputContact12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4281)
)
if mibBuilder.loadTexts:
    lgpCondId4281InputContact12.setStatus("current")
_LgpCondId4282InputContact13_ObjectIdentity = ObjectIdentity
lgpCondId4282InputContact13 = _LgpCondId4282InputContact13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4282)
)
if mibBuilder.loadTexts:
    lgpCondId4282InputContact13.setStatus("current")
_LgpCondId4283InputContact14_ObjectIdentity = ObjectIdentity
lgpCondId4283InputContact14 = _LgpCondId4283InputContact14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4283)
)
if mibBuilder.loadTexts:
    lgpCondId4283InputContact14.setStatus("current")
_LgpCondId4284InputContact15_ObjectIdentity = ObjectIdentity
lgpCondId4284InputContact15 = _LgpCondId4284InputContact15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4284)
)
if mibBuilder.loadTexts:
    lgpCondId4284InputContact15.setStatus("current")
_LgpCondId4285InputContact16_ObjectIdentity = ObjectIdentity
lgpCondId4285InputContact16 = _LgpCondId4285InputContact16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4285)
)
if mibBuilder.loadTexts:
    lgpCondId4285InputContact16.setStatus("current")
_LgpCondId4286OutputAmpOverUserLimitPhsA_ObjectIdentity = ObjectIdentity
lgpCondId4286OutputAmpOverUserLimitPhsA = _LgpCondId4286OutputAmpOverUserLimitPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4286)
)
if mibBuilder.loadTexts:
    lgpCondId4286OutputAmpOverUserLimitPhsA.setStatus("current")
_LgpCondId4287OutputAmpOverUserLimitPhsB_ObjectIdentity = ObjectIdentity
lgpCondId4287OutputAmpOverUserLimitPhsB = _LgpCondId4287OutputAmpOverUserLimitPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4287)
)
if mibBuilder.loadTexts:
    lgpCondId4287OutputAmpOverUserLimitPhsB.setStatus("current")
_LgpCondId4288OutputAmpOverUserLimitPhsC_ObjectIdentity = ObjectIdentity
lgpCondId4288OutputAmpOverUserLimitPhsC = _LgpCondId4288OutputAmpOverUserLimitPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4288)
)
if mibBuilder.loadTexts:
    lgpCondId4288OutputAmpOverUserLimitPhsC.setStatus("current")
_LgpCondId4289InverterTransferInhibitExt_ObjectIdentity = ObjectIdentity
lgpCondId4289InverterTransferInhibitExt = _LgpCondId4289InverterTransferInhibitExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4289)
)
if mibBuilder.loadTexts:
    lgpCondId4289InverterTransferInhibitExt.setStatus("current")
_LgpCondId4290InverterShutdownOverload_ObjectIdentity = ObjectIdentity
lgpCondId4290InverterShutdownOverload = _LgpCondId4290InverterShutdownOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4290)
)
if mibBuilder.loadTexts:
    lgpCondId4290InverterShutdownOverload.setStatus("current")
_LgpCondId4294InletAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4294InletAirOverTemperature = _LgpCondId4294InletAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4294)
)
if mibBuilder.loadTexts:
    lgpCondId4294InletAirOverTemperature.setStatus("current")
_LgpCondId4295RectifierFailure_ObjectIdentity = ObjectIdentity
lgpCondId4295RectifierFailure = _LgpCondId4295RectifierFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4295)
)
if mibBuilder.loadTexts:
    lgpCondId4295RectifierFailure.setStatus("current")
_LgpCondId4296RectifierOperationInhibitExt_ObjectIdentity = ObjectIdentity
lgpCondId4296RectifierOperationInhibitExt = _LgpCondId4296RectifierOperationInhibitExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4296)
)
if mibBuilder.loadTexts:
    lgpCondId4296RectifierOperationInhibitExt.setStatus("current")
_LgpCondId4297UPSOutputonInverter_ObjectIdentity = ObjectIdentity
lgpCondId4297UPSOutputonInverter = _LgpCondId4297UPSOutputonInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4297)
)
if mibBuilder.loadTexts:
    lgpCondId4297UPSOutputonInverter.setStatus("current")
_LgpCondId4298UPSOutputonBypass_ObjectIdentity = ObjectIdentity
lgpCondId4298UPSOutputonBypass = _LgpCondId4298UPSOutputonBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4298)
)
if mibBuilder.loadTexts:
    lgpCondId4298UPSOutputonBypass.setStatus("current")
_LgpCondId4299OutputLoadonMaintBypass_ObjectIdentity = ObjectIdentity
lgpCondId4299OutputLoadonMaintBypass = _LgpCondId4299OutputLoadonMaintBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4299)
)
if mibBuilder.loadTexts:
    lgpCondId4299OutputLoadonMaintBypass.setStatus("current")
_LgpCondId4300InternalCommunicationsFailure_ObjectIdentity = ObjectIdentity
lgpCondId4300InternalCommunicationsFailure = _LgpCondId4300InternalCommunicationsFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4300)
)
if mibBuilder.loadTexts:
    lgpCondId4300InternalCommunicationsFailure.setStatus("current")
_LgpCondId4308DCBusGroundFaultPositive_ObjectIdentity = ObjectIdentity
lgpCondId4308DCBusGroundFaultPositive = _LgpCondId4308DCBusGroundFaultPositive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4308)
)
if mibBuilder.loadTexts:
    lgpCondId4308DCBusGroundFaultPositive.setStatus("current")
_LgpCondId4309DCBusGroundFaultNegative_ObjectIdentity = ObjectIdentity
lgpCondId4309DCBusGroundFaultNegative = _LgpCondId4309DCBusGroundFaultNegative_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4309)
)
if mibBuilder.loadTexts:
    lgpCondId4309DCBusGroundFaultNegative.setStatus("current")
_LgpCondId4310EquipmentOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4310EquipmentOverTemperature = _LgpCondId4310EquipmentOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4310)
)
if mibBuilder.loadTexts:
    lgpCondId4310EquipmentOverTemperature.setStatus("current")
_LgpCondId4311SystemFanFailure_ObjectIdentity = ObjectIdentity
lgpCondId4311SystemFanFailure = _LgpCondId4311SystemFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4311)
)
if mibBuilder.loadTexts:
    lgpCondId4311SystemFanFailure.setStatus("current")
_LgpCondId4313PasswordChanged_ObjectIdentity = ObjectIdentity
lgpCondId4313PasswordChanged = _LgpCondId4313PasswordChanged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4313)
)
if mibBuilder.loadTexts:
    lgpCondId4313PasswordChanged.setStatus("current")
_LgpCondId4314PowerSupplyFailure_ObjectIdentity = ObjectIdentity
lgpCondId4314PowerSupplyFailure = _LgpCondId4314PowerSupplyFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4314)
)
if mibBuilder.loadTexts:
    lgpCondId4314PowerSupplyFailure.setStatus("current")
_LgpCondId4315OnGenerator_ObjectIdentity = ObjectIdentity
lgpCondId4315OnGenerator = _LgpCondId4315OnGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4315)
)
if mibBuilder.loadTexts:
    lgpCondId4315OnGenerator.setStatus("current")
_LgpCondId4316AutoRestartInProgress_ObjectIdentity = ObjectIdentity
lgpCondId4316AutoRestartInProgress = _LgpCondId4316AutoRestartInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4316)
)
if mibBuilder.loadTexts:
    lgpCondId4316AutoRestartInProgress.setStatus("current")
_LgpCondId4317AutoRestartInhibitedExt_ObjectIdentity = ObjectIdentity
lgpCondId4317AutoRestartInhibitedExt = _LgpCondId4317AutoRestartInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4317)
)
if mibBuilder.loadTexts:
    lgpCondId4317AutoRestartInhibitedExt.setStatus("current")
_LgpCondId4320InitiatedTransfertoBypass_ObjectIdentity = ObjectIdentity
lgpCondId4320InitiatedTransfertoBypass = _LgpCondId4320InitiatedTransfertoBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4320)
)
if mibBuilder.loadTexts:
    lgpCondId4320InitiatedTransfertoBypass.setStatus("current")
_LgpCondId4321InitiatedTransfertoInverter_ObjectIdentity = ObjectIdentity
lgpCondId4321InitiatedTransfertoInverter = _LgpCondId4321InitiatedTransfertoInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4321)
)
if mibBuilder.loadTexts:
    lgpCondId4321InitiatedTransfertoInverter.setStatus("current")
_LgpCondId4322BatteryTestPassed_ObjectIdentity = ObjectIdentity
lgpCondId4322BatteryTestPassed = _LgpCondId4322BatteryTestPassed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4322)
)
if mibBuilder.loadTexts:
    lgpCondId4322BatteryTestPassed.setStatus("current")
_LgpCondId4323BatteryTestFailed_ObjectIdentity = ObjectIdentity
lgpCondId4323BatteryTestFailed = _LgpCondId4323BatteryTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4323)
)
if mibBuilder.loadTexts:
    lgpCondId4323BatteryTestFailed.setStatus("current")
_LgpCondId4324BatteryTestManuallyStopped_ObjectIdentity = ObjectIdentity
lgpCondId4324BatteryTestManuallyStopped = _LgpCondId4324BatteryTestManuallyStopped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4324)
)
if mibBuilder.loadTexts:
    lgpCondId4324BatteryTestManuallyStopped.setStatus("current")
_LgpCondId4325BackfeedBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId4325BackfeedBreakerOpen = _LgpCondId4325BackfeedBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4325)
)
if mibBuilder.loadTexts:
    lgpCondId4325BackfeedBreakerOpen.setStatus("current")
_LgpCondId4341VelocityAuthenticationFailure_ObjectIdentity = ObjectIdentity
lgpCondId4341VelocityAuthenticationFailure = _LgpCondId4341VelocityAuthenticationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4341)
)
if mibBuilder.loadTexts:
    lgpCondId4341VelocityAuthenticationFailure.setStatus("current")
_LgpCondId4360ReceptacleOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4360ReceptacleOverCurrent = _LgpCondId4360ReceptacleOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4360)
)
if mibBuilder.loadTexts:
    lgpCondId4360ReceptacleOverCurrent.setStatus("current")
_LgpCondId4361ReceptacleUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4361ReceptacleUnderCurrent = _LgpCondId4361ReceptacleUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4361)
)
if mibBuilder.loadTexts:
    lgpCondId4361ReceptacleUnderCurrent.setStatus("current")
_LgpCondId4382SystemInputCurrentImbalance_ObjectIdentity = ObjectIdentity
lgpCondId4382SystemInputCurrentImbalance = _LgpCondId4382SystemInputCurrentImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4382)
)
if mibBuilder.loadTexts:
    lgpCondId4382SystemInputCurrentImbalance.setStatus("current")
_LgpCondId4383BypassStaticSwitchOffExtrnl_ObjectIdentity = ObjectIdentity
lgpCondId4383BypassStaticSwitchOffExtrnl = _LgpCondId4383BypassStaticSwitchOffExtrnl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4383)
)
if mibBuilder.loadTexts:
    lgpCondId4383BypassStaticSwitchOffExtrnl.setStatus("current")
_LgpCondId4384BatteryEoDDisconnect_ObjectIdentity = ObjectIdentity
lgpCondId4384BatteryEoDDisconnect = _LgpCondId4384BatteryEoDDisconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4384)
)
if mibBuilder.loadTexts:
    lgpCondId4384BatteryEoDDisconnect.setStatus("current")
_LgpCondId4389SystemOutputFault_ObjectIdentity = ObjectIdentity
lgpCondId4389SystemOutputFault = _LgpCondId4389SystemOutputFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4389)
)
if mibBuilder.loadTexts:
    lgpCondId4389SystemOutputFault.setStatus("current")
_LgpCondId4390InverterOffExternal_ObjectIdentity = ObjectIdentity
lgpCondId4390InverterOffExternal = _LgpCondId4390InverterOffExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4390)
)
if mibBuilder.loadTexts:
    lgpCondId4390InverterOffExternal.setStatus("current")
_LgpCondId4391InverterStaticSwitchSCRShort_ObjectIdentity = ObjectIdentity
lgpCondId4391InverterStaticSwitchSCRShort = _LgpCondId4391InverterStaticSwitchSCRShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4391)
)
if mibBuilder.loadTexts:
    lgpCondId4391InverterStaticSwitchSCRShort.setStatus("current")
_LgpCondId4392TemperatureSensorError_ObjectIdentity = ObjectIdentity
lgpCondId4392TemperatureSensorError = _LgpCondId4392TemperatureSensorError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4392)
)
if mibBuilder.loadTexts:
    lgpCondId4392TemperatureSensorError.setStatus("current")
_LgpCondId4406BranchOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4406BranchOverCurrent = _LgpCondId4406BranchOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4406)
)
if mibBuilder.loadTexts:
    lgpCondId4406BranchOverCurrent.setStatus("current")
_LgpCondId4407BranchUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4407BranchUnderCurrent = _LgpCondId4407BranchUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4407)
)
if mibBuilder.loadTexts:
    lgpCondId4407BranchUnderCurrent.setStatus("current")
_LgpCondId4416BranchOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4416BranchOverCurrent = _LgpCondId4416BranchOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4416)
)
if mibBuilder.loadTexts:
    lgpCondId4416BranchOverCurrent.setStatus("current")
_LgpCondId4417BranchUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4417BranchUnderCurrent = _LgpCondId4417BranchUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4417)
)
if mibBuilder.loadTexts:
    lgpCondId4417BranchUnderCurrent.setStatus("current")
_LgpCondId4421BranchFailure_ObjectIdentity = ObjectIdentity
lgpCondId4421BranchFailure = _LgpCondId4421BranchFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4421)
)
if mibBuilder.loadTexts:
    lgpCondId4421BranchFailure.setStatus("current")
_LgpCondId4436PDUOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4436PDUOverCurrent = _LgpCondId4436PDUOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4436)
)
if mibBuilder.loadTexts:
    lgpCondId4436PDUOverCurrent.setStatus("current")
_LgpCondId4437PDUUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4437PDUUnderCurrent = _LgpCondId4437PDUUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4437)
)
if mibBuilder.loadTexts:
    lgpCondId4437PDUUnderCurrent.setStatus("current")
_LgpCondId4438SystemInternalTemperatureRise_ObjectIdentity = ObjectIdentity
lgpCondId4438SystemInternalTemperatureRise = _LgpCondId4438SystemInternalTemperatureRise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4438)
)
if mibBuilder.loadTexts:
    lgpCondId4438SystemInternalTemperatureRise.setStatus("current")
_LgpCondId4439AutomaticRestartFailed_ObjectIdentity = ObjectIdentity
lgpCondId4439AutomaticRestartFailed = _LgpCondId4439AutomaticRestartFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4439)
)
if mibBuilder.loadTexts:
    lgpCondId4439AutomaticRestartFailed.setStatus("current")
_LgpCondId4440FuseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4440FuseFailure = _LgpCondId4440FuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4440)
)
if mibBuilder.loadTexts:
    lgpCondId4440FuseFailure.setStatus("current")
_LgpCondId4441SystemControllerError_ObjectIdentity = ObjectIdentity
lgpCondId4441SystemControllerError = _LgpCondId4441SystemControllerError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4441)
)
if mibBuilder.loadTexts:
    lgpCondId4441SystemControllerError.setStatus("current")
_LgpCondId4442SystemBreakersOpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4442SystemBreakersOpenFailure = _LgpCondId4442SystemBreakersOpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4442)
)
if mibBuilder.loadTexts:
    lgpCondId4442SystemBreakersOpenFailure.setStatus("current")
_LgpCondId4448PDUOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4448PDUOverCurrent = _LgpCondId4448PDUOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4448)
)
if mibBuilder.loadTexts:
    lgpCondId4448PDUOverCurrent.setStatus("current")
_LgpCondId4449PDUUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4449PDUUnderCurrent = _LgpCondId4449PDUUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4449)
)
if mibBuilder.loadTexts:
    lgpCondId4449PDUUnderCurrent.setStatus("current")
_LgpCondId4468PDUOverCurrentL1_ObjectIdentity = ObjectIdentity
lgpCondId4468PDUOverCurrentL1 = _LgpCondId4468PDUOverCurrentL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4468)
)
if mibBuilder.loadTexts:
    lgpCondId4468PDUOverCurrentL1.setStatus("current")
_LgpCondId4469PDUOverCurrentL2_ObjectIdentity = ObjectIdentity
lgpCondId4469PDUOverCurrentL2 = _LgpCondId4469PDUOverCurrentL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4469)
)
if mibBuilder.loadTexts:
    lgpCondId4469PDUOverCurrentL2.setStatus("current")
_LgpCondId4470PDUOverCurrentL3_ObjectIdentity = ObjectIdentity
lgpCondId4470PDUOverCurrentL3 = _LgpCondId4470PDUOverCurrentL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4470)
)
if mibBuilder.loadTexts:
    lgpCondId4470PDUOverCurrentL3.setStatus("current")
_LgpCondId4471PDUUnderCurrentL1_ObjectIdentity = ObjectIdentity
lgpCondId4471PDUUnderCurrentL1 = _LgpCondId4471PDUUnderCurrentL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4471)
)
if mibBuilder.loadTexts:
    lgpCondId4471PDUUnderCurrentL1.setStatus("current")
_LgpCondId4472PDUUnderCurrentL2_ObjectIdentity = ObjectIdentity
lgpCondId4472PDUUnderCurrentL2 = _LgpCondId4472PDUUnderCurrentL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4472)
)
if mibBuilder.loadTexts:
    lgpCondId4472PDUUnderCurrentL2.setStatus("current")
_LgpCondId4473PDUUnderCurrentL3_ObjectIdentity = ObjectIdentity
lgpCondId4473PDUUnderCurrentL3 = _LgpCondId4473PDUUnderCurrentL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4473)
)
if mibBuilder.loadTexts:
    lgpCondId4473PDUUnderCurrentL3.setStatus("current")
_LgpCondId4492ReceptaclePowerStateOn_ObjectIdentity = ObjectIdentity
lgpCondId4492ReceptaclePowerStateOn = _LgpCondId4492ReceptaclePowerStateOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4492)
)
if mibBuilder.loadTexts:
    lgpCondId4492ReceptaclePowerStateOn.setStatus("current")
_LgpCondId4493ReceptaclePowerStateOff_ObjectIdentity = ObjectIdentity
lgpCondId4493ReceptaclePowerStateOff = _LgpCondId4493ReceptaclePowerStateOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4493)
)
if mibBuilder.loadTexts:
    lgpCondId4493ReceptaclePowerStateOff.setStatus("current")
_LgpCondId4494BranchBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId4494BranchBreakerOpen = _LgpCondId4494BranchBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4494)
)
if mibBuilder.loadTexts:
    lgpCondId4494BranchBreakerOpen.setStatus("current")
_LgpCondId4495DeviceConfigurationChange_ObjectIdentity = ObjectIdentity
lgpCondId4495DeviceConfigurationChange = _LgpCondId4495DeviceConfigurationChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4495)
)
if mibBuilder.loadTexts:
    lgpCondId4495DeviceConfigurationChange.setStatus("current")
_LgpCondId4496BasicDisplayModuleRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4496BasicDisplayModuleRemoved = _LgpCondId4496BasicDisplayModuleRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4496)
)
if mibBuilder.loadTexts:
    lgpCondId4496BasicDisplayModuleRemoved.setStatus("current")
_LgpCondId4497BasicDisplayModuleDiscovered_ObjectIdentity = ObjectIdentity
lgpCondId4497BasicDisplayModuleDiscovered = _LgpCondId4497BasicDisplayModuleDiscovered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4497)
)
if mibBuilder.loadTexts:
    lgpCondId4497BasicDisplayModuleDiscovered.setStatus("current")
_LgpCondId4500PDUOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4500PDUOverCurrent = _LgpCondId4500PDUOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4500)
)
if mibBuilder.loadTexts:
    lgpCondId4500PDUOverCurrent.setStatus("current")
_LgpCondId4501PDUUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4501PDUUnderCurrent = _LgpCondId4501PDUUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4501)
)
if mibBuilder.loadTexts:
    lgpCondId4501PDUUnderCurrent.setStatus("current")
_LgpCondId4502PDUFailure_ObjectIdentity = ObjectIdentity
lgpCondId4502PDUFailure = _LgpCondId4502PDUFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4502)
)
if mibBuilder.loadTexts:
    lgpCondId4502PDUFailure.setStatus("current")
_LgpCondId4503PDUCommunicationFail_ObjectIdentity = ObjectIdentity
lgpCondId4503PDUCommunicationFail = _LgpCondId4503PDUCommunicationFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4503)
)
if mibBuilder.loadTexts:
    lgpCondId4503PDUCommunicationFail.setStatus("current")
_LgpCondId4504BranchRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4504BranchRemoved = _LgpCondId4504BranchRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4504)
)
if mibBuilder.loadTexts:
    lgpCondId4504BranchRemoved.setStatus("current")
_LgpCondId4505BranchDiscovered_ObjectIdentity = ObjectIdentity
lgpCondId4505BranchDiscovered = _LgpCondId4505BranchDiscovered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4505)
)
if mibBuilder.loadTexts:
    lgpCondId4505BranchDiscovered.setStatus("current")
_LgpCondId4506BranchOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4506BranchOverCurrent = _LgpCondId4506BranchOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4506)
)
if mibBuilder.loadTexts:
    lgpCondId4506BranchOverCurrent.setStatus("current")
_LgpCondId4507BranchCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4507BranchCurrent = _LgpCondId4507BranchCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4507)
)
if mibBuilder.loadTexts:
    lgpCondId4507BranchCurrent.setStatus("current")
_LgpCondId4508ReceptacleLoadRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4508ReceptacleLoadRemoved = _LgpCondId4508ReceptacleLoadRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4508)
)
if mibBuilder.loadTexts:
    lgpCondId4508ReceptacleLoadRemoved.setStatus("current")
_LgpCondId4509ReceptacleLoadAdded_ObjectIdentity = ObjectIdentity
lgpCondId4509ReceptacleLoadAdded = _LgpCondId4509ReceptacleLoadAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4509)
)
if mibBuilder.loadTexts:
    lgpCondId4509ReceptacleLoadAdded.setStatus("current")
_LgpCondId4523ModuleRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4523ModuleRemoved = _LgpCondId4523ModuleRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4523)
)
if mibBuilder.loadTexts:
    lgpCondId4523ModuleRemoved.setStatus("current")
_LgpCondId4524ModuleAdded_ObjectIdentity = ObjectIdentity
lgpCondId4524ModuleAdded = _LgpCondId4524ModuleAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4524)
)
if mibBuilder.loadTexts:
    lgpCondId4524ModuleAdded.setStatus("current")
_LgpCondId4550FirmwareUpdateRequired_ObjectIdentity = ObjectIdentity
lgpCondId4550FirmwareUpdateRequired = _LgpCondId4550FirmwareUpdateRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4550)
)
if mibBuilder.loadTexts:
    lgpCondId4550FirmwareUpdateRequired.setStatus("current")
_LgpCondId4551GenericTestEvent_ObjectIdentity = ObjectIdentity
lgpCondId4551GenericTestEvent = _LgpCondId4551GenericTestEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4551)
)
if mibBuilder.loadTexts:
    lgpCondId4551GenericTestEvent.setStatus("current")
_LgpCondId4580OverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4580OverTemperature = _LgpCondId4580OverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4580)
)
if mibBuilder.loadTexts:
    lgpCondId4580OverTemperature.setStatus("current")
_LgpCondId4581UnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4581UnderTemperature = _LgpCondId4581UnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4581)
)
if mibBuilder.loadTexts:
    lgpCondId4581UnderTemperature.setStatus("current")
_LgpCondId4588OverRelativeHumidity_ObjectIdentity = ObjectIdentity
lgpCondId4588OverRelativeHumidity = _LgpCondId4588OverRelativeHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4588)
)
if mibBuilder.loadTexts:
    lgpCondId4588OverRelativeHumidity.setStatus("current")
_LgpCondId4589UnderRelativeHumidity_ObjectIdentity = ObjectIdentity
lgpCondId4589UnderRelativeHumidity = _LgpCondId4589UnderRelativeHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4589)
)
if mibBuilder.loadTexts:
    lgpCondId4589UnderRelativeHumidity.setStatus("current")
_LgpCondId4601ExternalAirSensorAOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4601ExternalAirSensorAOverTemperature = _LgpCondId4601ExternalAirSensorAOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4601)
)
if mibBuilder.loadTexts:
    lgpCondId4601ExternalAirSensorAOverTemperature.setStatus("current")
_LgpCondId4604ExternalAirSensorBOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4604ExternalAirSensorBOverTemperature = _LgpCondId4604ExternalAirSensorBOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4604)
)
if mibBuilder.loadTexts:
    lgpCondId4604ExternalAirSensorBOverTemperature.setStatus("current")
_LgpCondId4608ExtAirSensorAUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4608ExtAirSensorAUnderTemperature = _LgpCondId4608ExtAirSensorAUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4608)
)
if mibBuilder.loadTexts:
    lgpCondId4608ExtAirSensorAUnderTemperature.setStatus("current")
_LgpCondId4611ExtAirSensorBUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4611ExtAirSensorBUnderTemperature = _LgpCondId4611ExtAirSensorBUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4611)
)
if mibBuilder.loadTexts:
    lgpCondId4611ExtAirSensorBUnderTemperature.setStatus("current")
_LgpCondId4615ExtDewPointOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4615ExtDewPointOverTemperature = _LgpCondId4615ExtDewPointOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4615)
)
if mibBuilder.loadTexts:
    lgpCondId4615ExtDewPointOverTemperature.setStatus("current")
_LgpCondId4618ExternalAirSensorAIssue_ObjectIdentity = ObjectIdentity
lgpCondId4618ExternalAirSensorAIssue = _LgpCondId4618ExternalAirSensorAIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4618)
)
if mibBuilder.loadTexts:
    lgpCondId4618ExternalAirSensorAIssue.setStatus("current")
_LgpCondId4621ExternalAirSensorBIssue_ObjectIdentity = ObjectIdentity
lgpCondId4621ExternalAirSensorBIssue = _LgpCondId4621ExternalAirSensorBIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4621)
)
if mibBuilder.loadTexts:
    lgpCondId4621ExternalAirSensorBIssue.setStatus("current")
_LgpCondId4626SupplyChilledWaterOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId4626SupplyChilledWaterOverTemp = _LgpCondId4626SupplyChilledWaterOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4626)
)
if mibBuilder.loadTexts:
    lgpCondId4626SupplyChilledWaterOverTemp.setStatus("current")
_LgpCondId4629SupplyChilledWaterTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId4629SupplyChilledWaterTempSensorIssue = _LgpCondId4629SupplyChilledWaterTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4629)
)
if mibBuilder.loadTexts:
    lgpCondId4629SupplyChilledWaterTempSensorIssue.setStatus("current")
_LgpCondId4634SupplyRefrigerantOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId4634SupplyRefrigerantOverTemp = _LgpCondId4634SupplyRefrigerantOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4634)
)
if mibBuilder.loadTexts:
    lgpCondId4634SupplyRefrigerantOverTemp.setStatus("current")
_LgpCondId4637SupplyRefrigerantUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId4637SupplyRefrigerantUnderTemp = _LgpCondId4637SupplyRefrigerantUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4637)
)
if mibBuilder.loadTexts:
    lgpCondId4637SupplyRefrigerantUnderTemp.setStatus("current")
_LgpCondId4640SupplyRefrigerantTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId4640SupplyRefrigerantTempSensorIssue = _LgpCondId4640SupplyRefrigerantTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4640)
)
if mibBuilder.loadTexts:
    lgpCondId4640SupplyRefrigerantTempSensorIssue.setStatus("current")
_LgpCondId4645SupplyFluidOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId4645SupplyFluidOverTemp = _LgpCondId4645SupplyFluidOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4645)
)
if mibBuilder.loadTexts:
    lgpCondId4645SupplyFluidOverTemp.setStatus("current")
_LgpCondId4648SupplyFluidUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId4648SupplyFluidUnderTemp = _LgpCondId4648SupplyFluidUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4648)
)
if mibBuilder.loadTexts:
    lgpCondId4648SupplyFluidUnderTemp.setStatus("current")
_LgpCondId4651SupplyFluidTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId4651SupplyFluidTempSensorIssue = _LgpCondId4651SupplyFluidTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4651)
)
if mibBuilder.loadTexts:
    lgpCondId4651SupplyFluidTempSensorIssue.setStatus("current")
_LgpCondId4656Pump1LossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId4656Pump1LossofFlow = _LgpCondId4656Pump1LossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4656)
)
if mibBuilder.loadTexts:
    lgpCondId4656Pump1LossofFlow.setStatus("current")
_LgpCondId4659Pump2LossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId4659Pump2LossofFlow = _LgpCondId4659Pump2LossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4659)
)
if mibBuilder.loadTexts:
    lgpCondId4659Pump2LossofFlow.setStatus("current")
_LgpCondId4662PumpShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4662PumpShortCycle = _LgpCondId4662PumpShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4662)
)
if mibBuilder.loadTexts:
    lgpCondId4662PumpShortCycle.setStatus("current")
_LgpCondId4669Compressor1AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4669Compressor1AHighHeadPressure = _LgpCondId4669Compressor1AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4669)
)
if mibBuilder.loadTexts:
    lgpCondId4669Compressor1AHighHeadPressure.setStatus("current")
_LgpCondId4672Compressor1BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4672Compressor1BHighHeadPressure = _LgpCondId4672Compressor1BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4672)
)
if mibBuilder.loadTexts:
    lgpCondId4672Compressor1BHighHeadPressure.setStatus("current")
_LgpCondId4675Compressor2AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4675Compressor2AHighHeadPressure = _LgpCondId4675Compressor2AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4675)
)
if mibBuilder.loadTexts:
    lgpCondId4675Compressor2AHighHeadPressure.setStatus("current")
_LgpCondId4678Compressor2BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4678Compressor2BHighHeadPressure = _LgpCondId4678Compressor2BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4678)
)
if mibBuilder.loadTexts:
    lgpCondId4678Compressor2BHighHeadPressure.setStatus("current")
_LgpCondId4681Compressor1AShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4681Compressor1AShortCycle = _LgpCondId4681Compressor1AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4681)
)
if mibBuilder.loadTexts:
    lgpCondId4681Compressor1AShortCycle.setStatus("current")
_LgpCondId4684Compressor1BShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4684Compressor1BShortCycle = _LgpCondId4684Compressor1BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4684)
)
if mibBuilder.loadTexts:
    lgpCondId4684Compressor1BShortCycle.setStatus("current")
_LgpCondId4687Compressor2AShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4687Compressor2AShortCycle = _LgpCondId4687Compressor2AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4687)
)
if mibBuilder.loadTexts:
    lgpCondId4687Compressor2AShortCycle.setStatus("current")
_LgpCondId4690Compressor2BShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4690Compressor2BShortCycle = _LgpCondId4690Compressor2BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4690)
)
if mibBuilder.loadTexts:
    lgpCondId4690Compressor2BShortCycle.setStatus("current")
_LgpCondId4693Tandem1LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId4693Tandem1LowSuctionPressure = _LgpCondId4693Tandem1LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4693)
)
if mibBuilder.loadTexts:
    lgpCondId4693Tandem1LowSuctionPressure.setStatus("current")
_LgpCondId4696Tandem2LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId4696Tandem2LowSuctionPressure = _LgpCondId4696Tandem2LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4696)
)
if mibBuilder.loadTexts:
    lgpCondId4696Tandem2LowSuctionPressure.setStatus("current")
_LgpCondId4703ChilledWaterControlValvePosition_ObjectIdentity = ObjectIdentity
lgpCondId4703ChilledWaterControlValvePosition = _LgpCondId4703ChilledWaterControlValvePosition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4703)
)
if mibBuilder.loadTexts:
    lgpCondId4703ChilledWaterControlValvePosition.setStatus("current")
_LgpCondId4711SystemCondensationDetected_ObjectIdentity = ObjectIdentity
lgpCondId4711SystemCondensationDetected = _LgpCondId4711SystemCondensationDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4711)
)
if mibBuilder.loadTexts:
    lgpCondId4711SystemCondensationDetected.setStatus("current")
_LgpCondId4714ShutdownLossOfPower_ObjectIdentity = ObjectIdentity
lgpCondId4714ShutdownLossOfPower = _LgpCondId4714ShutdownLossOfPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4714)
)
if mibBuilder.loadTexts:
    lgpCondId4714ShutdownLossOfPower.setStatus("current")
_LgpCondId4720SmokeDetected_ObjectIdentity = ObjectIdentity
lgpCondId4720SmokeDetected = _LgpCondId4720SmokeDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4720)
)
if mibBuilder.loadTexts:
    lgpCondId4720SmokeDetected.setStatus("current")
_LgpCondId4723WaterUnderFloor_ObjectIdentity = ObjectIdentity
lgpCondId4723WaterUnderFloor = _LgpCondId4723WaterUnderFloor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4723)
)
if mibBuilder.loadTexts:
    lgpCondId4723WaterUnderFloor.setStatus("current")
_LgpCondId4726ServiceRequired_ObjectIdentity = ObjectIdentity
lgpCondId4726ServiceRequired = _LgpCondId4726ServiceRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4726)
)
if mibBuilder.loadTexts:
    lgpCondId4726ServiceRequired.setStatus("current")
_LgpCondId4729FanIssue_ObjectIdentity = ObjectIdentity
lgpCondId4729FanIssue = _LgpCondId4729FanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4729)
)
if mibBuilder.loadTexts:
    lgpCondId4729FanIssue.setStatus("current")
_LgpCondId4732ReceptacleLoadDropped_ObjectIdentity = ObjectIdentity
lgpCondId4732ReceptacleLoadDropped = _LgpCondId4732ReceptacleLoadDropped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4732)
)
if mibBuilder.loadTexts:
    lgpCondId4732ReceptacleLoadDropped.setStatus("current")
_LgpCondId4740BatteryAutomaticTestInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4740BatteryAutomaticTestInhibited = _LgpCondId4740BatteryAutomaticTestInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4740)
)
if mibBuilder.loadTexts:
    lgpCondId4740BatteryAutomaticTestInhibited.setStatus("current")
_LgpCondId4741BatterySelfTest_ObjectIdentity = ObjectIdentity
lgpCondId4741BatterySelfTest = _LgpCondId4741BatterySelfTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4741)
)
if mibBuilder.loadTexts:
    lgpCondId4741BatterySelfTest.setStatus("current")
_LgpCondId4742BatteryLowShutdown_ObjectIdentity = ObjectIdentity
lgpCondId4742BatteryLowShutdown = _LgpCondId4742BatteryLowShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4742)
)
if mibBuilder.loadTexts:
    lgpCondId4742BatteryLowShutdown.setStatus("current")
_LgpCondId4747EquipmentTemperatureSensorFail_ObjectIdentity = ObjectIdentity
lgpCondId4747EquipmentTemperatureSensorFail = _LgpCondId4747EquipmentTemperatureSensorFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4747)
)
if mibBuilder.loadTexts:
    lgpCondId4747EquipmentTemperatureSensorFail.setStatus("current")
_LgpCondId4749SystemFanFailureRedundant_ObjectIdentity = ObjectIdentity
lgpCondId4749SystemFanFailureRedundant = _LgpCondId4749SystemFanFailureRedundant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4749)
)
if mibBuilder.loadTexts:
    lgpCondId4749SystemFanFailureRedundant.setStatus("current")
_LgpCondId4750MultipleFanFailure_ObjectIdentity = ObjectIdentity
lgpCondId4750MultipleFanFailure = _LgpCondId4750MultipleFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4750)
)
if mibBuilder.loadTexts:
    lgpCondId4750MultipleFanFailure.setStatus("current")
_LgpCondId4753MainControllerFault_ObjectIdentity = ObjectIdentity
lgpCondId4753MainControllerFault = _LgpCondId4753MainControllerFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4753)
)
if mibBuilder.loadTexts:
    lgpCondId4753MainControllerFault.setStatus("current")
_LgpCondId4754SystemBreakersCloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4754SystemBreakersCloseFailure = _LgpCondId4754SystemBreakersCloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4754)
)
if mibBuilder.loadTexts:
    lgpCondId4754SystemBreakersCloseFailure.setStatus("current")
_LgpCondId4755InputFilterCycleLock_ObjectIdentity = ObjectIdentity
lgpCondId4755InputFilterCycleLock = _LgpCondId4755InputFilterCycleLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4755)
)
if mibBuilder.loadTexts:
    lgpCondId4755InputFilterCycleLock.setStatus("current")
_LgpCondId4756ServiceCodeActive_ObjectIdentity = ObjectIdentity
lgpCondId4756ServiceCodeActive = _LgpCondId4756ServiceCodeActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4756)
)
if mibBuilder.loadTexts:
    lgpCondId4756ServiceCodeActive.setStatus("current")
_LgpCondId4757LBSActive_ObjectIdentity = ObjectIdentity
lgpCondId4757LBSActive = _LgpCondId4757LBSActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4757)
)
if mibBuilder.loadTexts:
    lgpCondId4757LBSActive.setStatus("current")
_LgpCondId4758LBSInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4758LBSInhibited = _LgpCondId4758LBSInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4758)
)
if mibBuilder.loadTexts:
    lgpCondId4758LBSInhibited.setStatus("current")
_LgpCondId4759LeadingPowerFactor_ObjectIdentity = ObjectIdentity
lgpCondId4759LeadingPowerFactor = _LgpCondId4759LeadingPowerFactor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4759)
)
if mibBuilder.loadTexts:
    lgpCondId4759LeadingPowerFactor.setStatus("current")
_LgpCondId4760ControlsResetRequired_ObjectIdentity = ObjectIdentity
lgpCondId4760ControlsResetRequired = _LgpCondId4760ControlsResetRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4760)
)
if mibBuilder.loadTexts:
    lgpCondId4760ControlsResetRequired.setStatus("current")
_LgpCondId4823ParallelCommWarning_ObjectIdentity = ObjectIdentity
lgpCondId4823ParallelCommWarning = _LgpCondId4823ParallelCommWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4823)
)
if mibBuilder.loadTexts:
    lgpCondId4823ParallelCommWarning.setStatus("current")
_LgpCondId4824SystemCommFail_ObjectIdentity = ObjectIdentity
lgpCondId4824SystemCommFail = _LgpCondId4824SystemCommFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4824)
)
if mibBuilder.loadTexts:
    lgpCondId4824SystemCommFail.setStatus("current")
_LgpCondId4825LossofRedundancy_ObjectIdentity = ObjectIdentity
lgpCondId4825LossofRedundancy = _LgpCondId4825LossofRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4825)
)
if mibBuilder.loadTexts:
    lgpCondId4825LossofRedundancy.setStatus("current")
_LgpCondId4826BPSSStartupInhibit_ObjectIdentity = ObjectIdentity
lgpCondId4826BPSSStartupInhibit = _LgpCondId4826BPSSStartupInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4826)
)
if mibBuilder.loadTexts:
    lgpCondId4826BPSSStartupInhibit.setStatus("current")
_LgpCondId4827MMSTransferInhibit_ObjectIdentity = ObjectIdentity
lgpCondId4827MMSTransferInhibit = _LgpCondId4827MMSTransferInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4827)
)
if mibBuilder.loadTexts:
    lgpCondId4827MMSTransferInhibit.setStatus("current")
_LgpCondId4828MMSRetransferInhibit_ObjectIdentity = ObjectIdentity
lgpCondId4828MMSRetransferInhibit = _LgpCondId4828MMSRetransferInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4828)
)
if mibBuilder.loadTexts:
    lgpCondId4828MMSRetransferInhibit.setStatus("current")
_LgpCondId4830MMSLossofSyncPulse_ObjectIdentity = ObjectIdentity
lgpCondId4830MMSLossofSyncPulse = _LgpCondId4830MMSLossofSyncPulse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4830)
)
if mibBuilder.loadTexts:
    lgpCondId4830MMSLossofSyncPulse.setStatus("current")
_LgpCondId4831MMSOverload_ObjectIdentity = ObjectIdentity
lgpCondId4831MMSOverload = _LgpCondId4831MMSOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4831)
)
if mibBuilder.loadTexts:
    lgpCondId4831MMSOverload.setStatus("current")
_LgpCondId4834MMSOnBattery_ObjectIdentity = ObjectIdentity
lgpCondId4834MMSOnBattery = _LgpCondId4834MMSOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4834)
)
if mibBuilder.loadTexts:
    lgpCondId4834MMSOnBattery.setStatus("current")
_LgpCondId4835MMSLowBatteryWarning_ObjectIdentity = ObjectIdentity
lgpCondId4835MMSLowBatteryWarning = _LgpCondId4835MMSLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4835)
)
if mibBuilder.loadTexts:
    lgpCondId4835MMSLowBatteryWarning.setStatus("current")
_LgpCondId4906LowAmbientTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4906LowAmbientTemperature = _LgpCondId4906LowAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4906)
)
if mibBuilder.loadTexts:
    lgpCondId4906LowAmbientTemperature.setStatus("current")
_LgpCondId4907HighAmbientTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4907HighAmbientTemperature = _LgpCondId4907HighAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4907)
)
if mibBuilder.loadTexts:
    lgpCondId4907HighAmbientTemperature.setStatus("current")
_LgpCondId4908LowOverallVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4908LowOverallVoltage = _LgpCondId4908LowOverallVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4908)
)
if mibBuilder.loadTexts:
    lgpCondId4908LowOverallVoltage.setStatus("current")
_LgpCondId4909HighOverallVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4909HighOverallVoltage = _LgpCondId4909HighOverallVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4909)
)
if mibBuilder.loadTexts:
    lgpCondId4909HighOverallVoltage.setStatus("current")
_LgpCondId4910HighBatteryStringCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4910HighBatteryStringCurrent = _LgpCondId4910HighBatteryStringCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4910)
)
if mibBuilder.loadTexts:
    lgpCondId4910HighBatteryStringCurrent.setStatus("current")
_LgpCondId4911LowBatteryStringFloatCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4911LowBatteryStringFloatCurrent = _LgpCondId4911LowBatteryStringFloatCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4911)
)
if mibBuilder.loadTexts:
    lgpCondId4911LowBatteryStringFloatCurrent.setStatus("current")
_LgpCondId4912HighBatteryStringFloatCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4912HighBatteryStringFloatCurrent = _LgpCondId4912HighBatteryStringFloatCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4912)
)
if mibBuilder.loadTexts:
    lgpCondId4912HighBatteryStringFloatCurrent.setStatus("current")
_LgpCondId4913HighBatteryStringRippleCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4913HighBatteryStringRippleCurrent = _LgpCondId4913HighBatteryStringRippleCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4913)
)
if mibBuilder.loadTexts:
    lgpCondId4913HighBatteryStringRippleCurrent.setStatus("current")
_LgpCondId4914BatteryStringDischargeDetected_ObjectIdentity = ObjectIdentity
lgpCondId4914BatteryStringDischargeDetected = _LgpCondId4914BatteryStringDischargeDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4914)
)
if mibBuilder.loadTexts:
    lgpCondId4914BatteryStringDischargeDetected.setStatus("current")
_LgpCondId4915MaximumDischargeTimeExceeded_ObjectIdentity = ObjectIdentity
lgpCondId4915MaximumDischargeTimeExceeded = _LgpCondId4915MaximumDischargeTimeExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4915)
)
if mibBuilder.loadTexts:
    lgpCondId4915MaximumDischargeTimeExceeded.setStatus("current")
_LgpCondId4916DischargeLowOverallVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4916DischargeLowOverallVoltage = _LgpCondId4916DischargeLowOverallVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4916)
)
if mibBuilder.loadTexts:
    lgpCondId4916DischargeLowOverallVoltage.setStatus("current")
_LgpCondId4917DischargeLowCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4917DischargeLowCellVoltage = _LgpCondId4917DischargeLowCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4917)
)
if mibBuilder.loadTexts:
    lgpCondId4917DischargeLowCellVoltage.setStatus("current")
_LgpCondId4918DischargeHighBatteryStringCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4918DischargeHighBatteryStringCurrent = _LgpCondId4918DischargeHighBatteryStringCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4918)
)
if mibBuilder.loadTexts:
    lgpCondId4918DischargeHighBatteryStringCurrent.setStatus("current")
_LgpCondId4919ExcessiveCelltoCellTemperatureDeviation_ObjectIdentity = ObjectIdentity
lgpCondId4919ExcessiveCelltoCellTemperatureDeviation = _LgpCondId4919ExcessiveCelltoCellTemperatureDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4919)
)
if mibBuilder.loadTexts:
    lgpCondId4919ExcessiveCelltoCellTemperatureDeviation.setStatus("current")
_LgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation_ObjectIdentity = ObjectIdentity
lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation = _LgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4920)
)
if mibBuilder.loadTexts:
    lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation.setStatus("current")
_LgpCondId4964LowCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4964LowCellVoltage = _LgpCondId4964LowCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4964)
)
if mibBuilder.loadTexts:
    lgpCondId4964LowCellVoltage.setStatus("current")
_LgpCondId4965HighCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4965HighCellVoltage = _LgpCondId4965HighCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4965)
)
if mibBuilder.loadTexts:
    lgpCondId4965HighCellVoltage.setStatus("current")
_LgpCondId4966LowCellTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4966LowCellTemperature = _LgpCondId4966LowCellTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4966)
)
if mibBuilder.loadTexts:
    lgpCondId4966LowCellTemperature.setStatus("current")
_LgpCondId4967HighCellTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4967HighCellTemperature = _LgpCondId4967HighCellTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4967)
)
if mibBuilder.loadTexts:
    lgpCondId4967HighCellTemperature.setStatus("current")
_LgpCondId4968LowInternalResistance_ObjectIdentity = ObjectIdentity
lgpCondId4968LowInternalResistance = _LgpCondId4968LowInternalResistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4968)
)
if mibBuilder.loadTexts:
    lgpCondId4968LowInternalResistance.setStatus("current")
_LgpCondId4969HighInternalResistance_ObjectIdentity = ObjectIdentity
lgpCondId4969HighInternalResistance = _LgpCondId4969HighInternalResistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4969)
)
if mibBuilder.loadTexts:
    lgpCondId4969HighInternalResistance.setStatus("current")
_LgpCondId4970HighIntercellResistance_ObjectIdentity = ObjectIdentity
lgpCondId4970HighIntercellResistance = _LgpCondId4970HighIntercellResistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4970)
)
if mibBuilder.loadTexts:
    lgpCondId4970HighIntercellResistance.setStatus("current")
_LgpCondId4978IntertierResistanceHigh_ObjectIdentity = ObjectIdentity
lgpCondId4978IntertierResistanceHigh = _LgpCondId4978IntertierResistanceHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4978)
)
if mibBuilder.loadTexts:
    lgpCondId4978IntertierResistanceHigh.setStatus("current")
_LgpCondId4980SupplyChilledWaterLossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId4980SupplyChilledWaterLossofFlow = _LgpCondId4980SupplyChilledWaterLossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4980)
)
if mibBuilder.loadTexts:
    lgpCondId4980SupplyChilledWaterLossofFlow.setStatus("current")
_LgpCondId4983SupplyRefrigOverTempBand1_ObjectIdentity = ObjectIdentity
lgpCondId4983SupplyRefrigOverTempBand1 = _LgpCondId4983SupplyRefrigOverTempBand1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4983)
)
if mibBuilder.loadTexts:
    lgpCondId4983SupplyRefrigOverTempBand1.setStatus("current")
_LgpCondId4986SupplyRefrigUnderTempBand1_ObjectIdentity = ObjectIdentity
lgpCondId4986SupplyRefrigUnderTempBand1 = _LgpCondId4986SupplyRefrigUnderTempBand1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4986)
)
if mibBuilder.loadTexts:
    lgpCondId4986SupplyRefrigUnderTempBand1.setStatus("current")
_LgpCondId4990SupplyRefrigOverTempBand2_ObjectIdentity = ObjectIdentity
lgpCondId4990SupplyRefrigOverTempBand2 = _LgpCondId4990SupplyRefrigOverTempBand2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4990)
)
if mibBuilder.loadTexts:
    lgpCondId4990SupplyRefrigOverTempBand2.setStatus("current")
_LgpCondId4993SupplyRefrigUnderTempBand2_ObjectIdentity = ObjectIdentity
lgpCondId4993SupplyRefrigUnderTempBand2 = _LgpCondId4993SupplyRefrigUnderTempBand2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4993)
)
if mibBuilder.loadTexts:
    lgpCondId4993SupplyRefrigUnderTempBand2.setStatus("current")
_LgpCondId4996Inverter1ShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4996Inverter1ShortCycle = _LgpCondId4996Inverter1ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4996)
)
if mibBuilder.loadTexts:
    lgpCondId4996Inverter1ShortCycle.setStatus("current")
_LgpCondId4999Inverter2ShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4999Inverter2ShortCycle = _LgpCondId4999Inverter2ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4999)
)
if mibBuilder.loadTexts:
    lgpCondId4999Inverter2ShortCycle.setStatus("current")
_LgpCondId5015SupplyAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5015SupplyAirOverTemperature = _LgpCondId5015SupplyAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5015)
)
if mibBuilder.loadTexts:
    lgpCondId5015SupplyAirOverTemperature.setStatus("current")
_LgpCondId5019SupplyAirUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5019SupplyAirUnderTemperature = _LgpCondId5019SupplyAirUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5019)
)
if mibBuilder.loadTexts:
    lgpCondId5019SupplyAirUnderTemperature.setStatus("current")
_LgpCondId5023ReturnAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5023ReturnAirOverTemperature = _LgpCondId5023ReturnAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5023)
)
if mibBuilder.loadTexts:
    lgpCondId5023ReturnAirOverTemperature.setStatus("current")
_LgpCondId5026SupplyAirSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5026SupplyAirSensorIssue = _LgpCondId5026SupplyAirSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5026)
)
if mibBuilder.loadTexts:
    lgpCondId5026SupplyAirSensorIssue.setStatus("current")
_LgpCondId5034HighReturnHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5034HighReturnHumidity = _LgpCondId5034HighReturnHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5034)
)
if mibBuilder.loadTexts:
    lgpCondId5034HighReturnHumidity.setStatus("current")
_LgpCondId5036LowReturnHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5036LowReturnHumidity = _LgpCondId5036LowReturnHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5036)
)
if mibBuilder.loadTexts:
    lgpCondId5036LowReturnHumidity.setStatus("current")
_LgpCondId5037HumidifierHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5037HumidifierHoursExceeded = _LgpCondId5037HumidifierHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5037)
)
if mibBuilder.loadTexts:
    lgpCondId5037HumidifierHoursExceeded.setStatus("current")
_LgpCondId5038DehumidifierHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5038DehumidifierHoursExceeded = _LgpCondId5038DehumidifierHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5038)
)
if mibBuilder.loadTexts:
    lgpCondId5038DehumidifierHoursExceeded.setStatus("current")
_LgpCondId5039HumidifierUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId5039HumidifierUnderCurrent = _LgpCondId5039HumidifierUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5039)
)
if mibBuilder.loadTexts:
    lgpCondId5039HumidifierUnderCurrent.setStatus("current")
_LgpCondId5040HumidifierOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId5040HumidifierOverCurrent = _LgpCondId5040HumidifierOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5040)
)
if mibBuilder.loadTexts:
    lgpCondId5040HumidifierOverCurrent.setStatus("current")
_LgpCondId5041HumidifierLowWater_ObjectIdentity = ObjectIdentity
lgpCondId5041HumidifierLowWater = _LgpCondId5041HumidifierLowWater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5041)
)
if mibBuilder.loadTexts:
    lgpCondId5041HumidifierLowWater.setStatus("current")
_LgpCondId5042HumidifierCylinderWorn_ObjectIdentity = ObjectIdentity
lgpCondId5042HumidifierCylinderWorn = _LgpCondId5042HumidifierCylinderWorn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5042)
)
if mibBuilder.loadTexts:
    lgpCondId5042HumidifierCylinderWorn.setStatus("current")
_LgpCondId5043HumidifierIssue_ObjectIdentity = ObjectIdentity
lgpCondId5043HumidifierIssue = _LgpCondId5043HumidifierIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5043)
)
if mibBuilder.loadTexts:
    lgpCondId5043HumidifierIssue.setStatus("current")
_LgpCondId5044ExtHumidifierLockout_ObjectIdentity = ObjectIdentity
lgpCondId5044ExtHumidifierLockout = _LgpCondId5044ExtHumidifierLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5044)
)
if mibBuilder.loadTexts:
    lgpCondId5044ExtHumidifierLockout.setStatus("current")
_LgpCondId5045HumidifierControlBoardNotDetected_ObjectIdentity = ObjectIdentity
lgpCondId5045HumidifierControlBoardNotDetected = _LgpCondId5045HumidifierControlBoardNotDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5045)
)
if mibBuilder.loadTexts:
    lgpCondId5045HumidifierControlBoardNotDetected.setStatus("current")
_LgpCondId5046ReturnHumidityOutOfProportionalBand_ObjectIdentity = ObjectIdentity
lgpCondId5046ReturnHumidityOutOfProportionalBand = _LgpCondId5046ReturnHumidityOutOfProportionalBand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5046)
)
if mibBuilder.loadTexts:
    lgpCondId5046ReturnHumidityOutOfProportionalBand.setStatus("current")
_LgpCondId5053LossofAirFlow_ObjectIdentity = ObjectIdentity
lgpCondId5053LossofAirFlow = _LgpCondId5053LossofAirFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5053)
)
if mibBuilder.loadTexts:
    lgpCondId5053LossofAirFlow.setStatus("current")
_LgpCondId5054FanHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5054FanHoursExceeded = _LgpCondId5054FanHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5054)
)
if mibBuilder.loadTexts:
    lgpCondId5054FanHoursExceeded.setStatus("current")
_LgpCondId5055TopFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5055TopFanIssue = _LgpCondId5055TopFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5055)
)
if mibBuilder.loadTexts:
    lgpCondId5055TopFanIssue.setStatus("current")
_LgpCondId5056BottomFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5056BottomFanIssue = _LgpCondId5056BottomFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5056)
)
if mibBuilder.loadTexts:
    lgpCondId5056BottomFanIssue.setStatus("current")
_LgpCondId5060RemoteSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5060RemoteSensorIssue = _LgpCondId5060RemoteSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5060)
)
if mibBuilder.loadTexts:
    lgpCondId5060RemoteSensorIssue.setStatus("current")
_LgpCondId5062Compressor1LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId5062Compressor1LowSuctionPressure = _LgpCondId5062Compressor1LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5062)
)
if mibBuilder.loadTexts:
    lgpCondId5062Compressor1LowSuctionPressure.setStatus("current")
_LgpCondId5063Compressor1HoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5063Compressor1HoursExceeded = _LgpCondId5063Compressor1HoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5063)
)
if mibBuilder.loadTexts:
    lgpCondId5063Compressor1HoursExceeded.setStatus("current")
_LgpCondId5064DigScrollComp1TempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5064DigScrollComp1TempSensorIssue = _LgpCondId5064DigScrollComp1TempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5064)
)
if mibBuilder.loadTexts:
    lgpCondId5064DigScrollComp1TempSensorIssue.setStatus("current")
_LgpCondId5065DigScrollComp1OverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5065DigScrollComp1OverTemp = _LgpCondId5065DigScrollComp1OverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5065)
)
if mibBuilder.loadTexts:
    lgpCondId5065DigScrollComp1OverTemp.setStatus("current")
_LgpCondId5066Compressor1LowPressureTransducerIssue_ObjectIdentity = ObjectIdentity
lgpCondId5066Compressor1LowPressureTransducerIssue = _LgpCondId5066Compressor1LowPressureTransducerIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5066)
)
if mibBuilder.loadTexts:
    lgpCondId5066Compressor1LowPressureTransducerIssue.setStatus("current")
_LgpCondId5067ExtCompressorLockout_ObjectIdentity = ObjectIdentity
lgpCondId5067ExtCompressorLockout = _LgpCondId5067ExtCompressorLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5067)
)
if mibBuilder.loadTexts:
    lgpCondId5067ExtCompressorLockout.setStatus("current")
_LgpCondId5068ReheaterOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5068ReheaterOverTemperature = _LgpCondId5068ReheaterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5068)
)
if mibBuilder.loadTexts:
    lgpCondId5068ReheaterOverTemperature.setStatus("current")
_LgpCondId5069ElectricReheater1HoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5069ElectricReheater1HoursExceeded = _LgpCondId5069ElectricReheater1HoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5069)
)
if mibBuilder.loadTexts:
    lgpCondId5069ElectricReheater1HoursExceeded.setStatus("current")
_LgpCondId5070ExtReheatLockout_ObjectIdentity = ObjectIdentity
lgpCondId5070ExtReheatLockout = _LgpCondId5070ExtReheatLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5070)
)
if mibBuilder.loadTexts:
    lgpCondId5070ExtReheatLockout.setStatus("current")
_LgpCondId5071Condenser1Issue_ObjectIdentity = ObjectIdentity
lgpCondId5071Condenser1Issue = _LgpCondId5071Condenser1Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5071)
)
if mibBuilder.loadTexts:
    lgpCondId5071Condenser1Issue.setStatus("current")
_LgpCondId5072CondenserVFDIssue_ObjectIdentity = ObjectIdentity
lgpCondId5072CondenserVFDIssue = _LgpCondId5072CondenserVFDIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5072)
)
if mibBuilder.loadTexts:
    lgpCondId5072CondenserVFDIssue.setStatus("current")
_LgpCondId5073CondenserTVSSIssue_ObjectIdentity = ObjectIdentity
lgpCondId5073CondenserTVSSIssue = _LgpCondId5073CondenserTVSSIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5073)
)
if mibBuilder.loadTexts:
    lgpCondId5073CondenserTVSSIssue.setStatus("current")
_LgpCondId5104ExtOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5104ExtOverTemperature = _LgpCondId5104ExtOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5104)
)
if mibBuilder.loadTexts:
    lgpCondId5104ExtOverTemperature.setStatus("current")
_LgpCondId5105ExtLossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId5105ExtLossofFlow = _LgpCondId5105ExtLossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5105)
)
if mibBuilder.loadTexts:
    lgpCondId5105ExtLossofFlow.setStatus("current")
_LgpCondId5106ExtCondenserPumpHighWater_ObjectIdentity = ObjectIdentity
lgpCondId5106ExtCondenserPumpHighWater = _LgpCondId5106ExtCondenserPumpHighWater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5106)
)
if mibBuilder.loadTexts:
    lgpCondId5106ExtCondenserPumpHighWater.setStatus("current")
_LgpCondId5107ExtStandbyGlycolPumpOn_ObjectIdentity = ObjectIdentity
lgpCondId5107ExtStandbyGlycolPumpOn = _LgpCondId5107ExtStandbyGlycolPumpOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5107)
)
if mibBuilder.loadTexts:
    lgpCondId5107ExtStandbyGlycolPumpOn.setStatus("current")
_LgpCondId5108ExternalFireDetected_ObjectIdentity = ObjectIdentity
lgpCondId5108ExternalFireDetected = _LgpCondId5108ExternalFireDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5108)
)
if mibBuilder.loadTexts:
    lgpCondId5108ExternalFireDetected.setStatus("current")
_LgpCondId5109UnitOn_ObjectIdentity = ObjectIdentity
lgpCondId5109UnitOn = _LgpCondId5109UnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5109)
)
if mibBuilder.loadTexts:
    lgpCondId5109UnitOn.setStatus("current")
_LgpCondId5110UnitOff_ObjectIdentity = ObjectIdentity
lgpCondId5110UnitOff = _LgpCondId5110UnitOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5110)
)
if mibBuilder.loadTexts:
    lgpCondId5110UnitOff.setStatus("current")
_LgpCondId5111UnitStandby_ObjectIdentity = ObjectIdentity
lgpCondId5111UnitStandby = _LgpCondId5111UnitStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5111)
)
if mibBuilder.loadTexts:
    lgpCondId5111UnitStandby.setStatus("current")
_LgpCondId5112UnitPartialShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5112UnitPartialShutdown = _LgpCondId5112UnitPartialShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5112)
)
if mibBuilder.loadTexts:
    lgpCondId5112UnitPartialShutdown.setStatus("current")
_LgpCondId5113UnitShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5113UnitShutdown = _LgpCondId5113UnitShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5113)
)
if mibBuilder.loadTexts:
    lgpCondId5113UnitShutdown.setStatus("current")
_LgpCondId5114WaterLeakageDetectorSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5114WaterLeakageDetectorSensorIssue = _LgpCondId5114WaterLeakageDetectorSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5114)
)
if mibBuilder.loadTexts:
    lgpCondId5114WaterLeakageDetectorSensorIssue.setStatus("current")
_LgpCondId5115BMSCommunicationsTimeout_ObjectIdentity = ObjectIdentity
lgpCondId5115BMSCommunicationsTimeout = _LgpCondId5115BMSCommunicationsTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5115)
)
if mibBuilder.loadTexts:
    lgpCondId5115BMSCommunicationsTimeout.setStatus("current")
_LgpCondId5116MaintenanceDue_ObjectIdentity = ObjectIdentity
lgpCondId5116MaintenanceDue = _LgpCondId5116MaintenanceDue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5116)
)
if mibBuilder.loadTexts:
    lgpCondId5116MaintenanceDue.setStatus("current")
_LgpCondId5117MaintenanceCompleted_ObjectIdentity = ObjectIdentity
lgpCondId5117MaintenanceCompleted = _LgpCondId5117MaintenanceCompleted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5117)
)
if mibBuilder.loadTexts:
    lgpCondId5117MaintenanceCompleted.setStatus("current")
_LgpCondId5118CloggedAirFilter_ObjectIdentity = ObjectIdentity
lgpCondId5118CloggedAirFilter = _LgpCondId5118CloggedAirFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5118)
)
if mibBuilder.loadTexts:
    lgpCondId5118CloggedAirFilter.setStatus("current")
_LgpCondId5119RAMBatteryIssue_ObjectIdentity = ObjectIdentity
lgpCondId5119RAMBatteryIssue = _LgpCondId5119RAMBatteryIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5119)
)
if mibBuilder.loadTexts:
    lgpCondId5119RAMBatteryIssue.setStatus("current")
_LgpCondId5120MasterUnitCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5120MasterUnitCommunicationLost = _LgpCondId5120MasterUnitCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5120)
)
if mibBuilder.loadTexts:
    lgpCondId5120MasterUnitCommunicationLost.setStatus("current")
_LgpCondId5121HighPowerShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5121HighPowerShutdown = _LgpCondId5121HighPowerShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5121)
)
if mibBuilder.loadTexts:
    lgpCondId5121HighPowerShutdown.setStatus("current")
_LgpCondId5126DigScrollComp2OverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5126DigScrollComp2OverTemp = _LgpCondId5126DigScrollComp2OverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5126)
)
if mibBuilder.loadTexts:
    lgpCondId5126DigScrollComp2OverTemp.setStatus("current")
_LgpCondId5144OutputOfUf_ObjectIdentity = ObjectIdentity
lgpCondId5144OutputOfUf = _LgpCondId5144OutputOfUf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5144)
)
if mibBuilder.loadTexts:
    lgpCondId5144OutputOfUf.setStatus("current")
_LgpCondId5145MMSModuleAlarmActive_ObjectIdentity = ObjectIdentity
lgpCondId5145MMSModuleAlarmActive = _LgpCondId5145MMSModuleAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5145)
)
if mibBuilder.loadTexts:
    lgpCondId5145MMSModuleAlarmActive.setStatus("current")
_LgpCondId5146CompressorPumpDownIssue_ObjectIdentity = ObjectIdentity
lgpCondId5146CompressorPumpDownIssue = _LgpCondId5146CompressorPumpDownIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5146)
)
if mibBuilder.loadTexts:
    lgpCondId5146CompressorPumpDownIssue.setStatus("current")
_LgpCondId5147ReturnAirSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5147ReturnAirSensorIssue = _LgpCondId5147ReturnAirSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5147)
)
if mibBuilder.loadTexts:
    lgpCondId5147ReturnAirSensorIssue.setStatus("current")
_LgpCondId5148CompressorHighPressureTransducerIssue_ObjectIdentity = ObjectIdentity
lgpCondId5148CompressorHighPressureTransducerIssue = _LgpCondId5148CompressorHighPressureTransducerIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5148)
)
if mibBuilder.loadTexts:
    lgpCondId5148CompressorHighPressureTransducerIssue.setStatus("current")
_LgpCondId5149BatteryNotQualified_ObjectIdentity = ObjectIdentity
lgpCondId5149BatteryNotQualified = _LgpCondId5149BatteryNotQualified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5149)
)
if mibBuilder.loadTexts:
    lgpCondId5149BatteryNotQualified.setStatus("current")
_LgpCondId5150BatteryTerminalsReversed_ObjectIdentity = ObjectIdentity
lgpCondId5150BatteryTerminalsReversed = _LgpCondId5150BatteryTerminalsReversed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5150)
)
if mibBuilder.loadTexts:
    lgpCondId5150BatteryTerminalsReversed.setStatus("current")
_LgpCondId5151BatteryConverterFailure_ObjectIdentity = ObjectIdentity
lgpCondId5151BatteryConverterFailure = _LgpCondId5151BatteryConverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5151)
)
if mibBuilder.loadTexts:
    lgpCondId5151BatteryConverterFailure.setStatus("current")
_LgpCondId5152InverterSCROpen_ObjectIdentity = ObjectIdentity
lgpCondId5152InverterSCROpen = _LgpCondId5152InverterSCROpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5152)
)
if mibBuilder.loadTexts:
    lgpCondId5152InverterSCROpen.setStatus("current")
_LgpCondId5153LoadSharingFault_ObjectIdentity = ObjectIdentity
lgpCondId5153LoadSharingFault = _LgpCondId5153LoadSharingFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5153)
)
if mibBuilder.loadTexts:
    lgpCondId5153LoadSharingFault.setStatus("current")
_LgpCondId5154DCBusAbnormal_ObjectIdentity = ObjectIdentity
lgpCondId5154DCBusAbnormal = _LgpCondId5154DCBusAbnormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5154)
)
if mibBuilder.loadTexts:
    lgpCondId5154DCBusAbnormal.setStatus("current")
_LgpCondId5155MainsInputNeutralLost_ObjectIdentity = ObjectIdentity
lgpCondId5155MainsInputNeutralLost = _LgpCondId5155MainsInputNeutralLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5155)
)
if mibBuilder.loadTexts:
    lgpCondId5155MainsInputNeutralLost.setStatus("current")
_LgpCondId5156LoadImpactTransfer_ObjectIdentity = ObjectIdentity
lgpCondId5156LoadImpactTransfer = _LgpCondId5156LoadImpactTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5156)
)
if mibBuilder.loadTexts:
    lgpCondId5156LoadImpactTransfer.setStatus("current")
_LgpCondId5157UserOperationInvalid_ObjectIdentity = ObjectIdentity
lgpCondId5157UserOperationInvalid = _LgpCondId5157UserOperationInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5157)
)
if mibBuilder.loadTexts:
    lgpCondId5157UserOperationInvalid.setStatus("current")
_LgpCondId5158PowerSubModuleFault_ObjectIdentity = ObjectIdentity
lgpCondId5158PowerSubModuleFault = _LgpCondId5158PowerSubModuleFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5158)
)
if mibBuilder.loadTexts:
    lgpCondId5158PowerSubModuleFault.setStatus("current")
_LgpCondId5178OutputOvervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5178OutputOvervoltage = _LgpCondId5178OutputOvervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5178)
)
if mibBuilder.loadTexts:
    lgpCondId5178OutputOvervoltage.setStatus("current")
_LgpCondId5179OutputUndervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5179OutputUndervoltage = _LgpCondId5179OutputUndervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5179)
)
if mibBuilder.loadTexts:
    lgpCondId5179OutputUndervoltage.setStatus("current")
_LgpCondId5180OutputOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5180OutputOvercurrent = _LgpCondId5180OutputOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5180)
)
if mibBuilder.loadTexts:
    lgpCondId5180OutputOvercurrent.setStatus("current")
_LgpCondId5181NeutralOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5181NeutralOvercurrent = _LgpCondId5181NeutralOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5181)
)
if mibBuilder.loadTexts:
    lgpCondId5181NeutralOvercurrent.setStatus("current")
_LgpCondId5182GroundOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5182GroundOvercurrent = _LgpCondId5182GroundOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5182)
)
if mibBuilder.loadTexts:
    lgpCondId5182GroundOvercurrent.setStatus("current")
_LgpCondId5183OutputVoltageTHD_ObjectIdentity = ObjectIdentity
lgpCondId5183OutputVoltageTHD = _LgpCondId5183OutputVoltageTHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5183)
)
if mibBuilder.loadTexts:
    lgpCondId5183OutputVoltageTHD.setStatus("current")
_LgpCondId5184OutputFrequencyError_ObjectIdentity = ObjectIdentity
lgpCondId5184OutputFrequencyError = _LgpCondId5184OutputFrequencyError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5184)
)
if mibBuilder.loadTexts:
    lgpCondId5184OutputFrequencyError.setStatus("current")
_LgpCondId5185TransformerOvertemperature_ObjectIdentity = ObjectIdentity
lgpCondId5185TransformerOvertemperature = _LgpCondId5185TransformerOvertemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5185)
)
if mibBuilder.loadTexts:
    lgpCondId5185TransformerOvertemperature.setStatus("current")
_LgpCondId5212PanelSummaryStatus_ObjectIdentity = ObjectIdentity
lgpCondId5212PanelSummaryStatus = _LgpCondId5212PanelSummaryStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5212)
)
if mibBuilder.loadTexts:
    lgpCondId5212PanelSummaryStatus.setStatus("current")
_LgpCondId5213PanelOvervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5213PanelOvervoltage = _LgpCondId5213PanelOvervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5213)
)
if mibBuilder.loadTexts:
    lgpCondId5213PanelOvervoltage.setStatus("current")
_LgpCondId5214PanelUndervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5214PanelUndervoltage = _LgpCondId5214PanelUndervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5214)
)
if mibBuilder.loadTexts:
    lgpCondId5214PanelUndervoltage.setStatus("current")
_LgpCondId5215PanelOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5215PanelOvercurrent = _LgpCondId5215PanelOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5215)
)
if mibBuilder.loadTexts:
    lgpCondId5215PanelOvercurrent.setStatus("current")
_LgpCondId5216PanelNeutralOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5216PanelNeutralOvercurrent = _LgpCondId5216PanelNeutralOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5216)
)
if mibBuilder.loadTexts:
    lgpCondId5216PanelNeutralOvercurrent.setStatus("current")
_LgpCondId5217PanelGroundOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5217PanelGroundOvercurrent = _LgpCondId5217PanelGroundOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5217)
)
if mibBuilder.loadTexts:
    lgpCondId5217PanelGroundOvercurrent.setStatus("current")
_LgpCondId5226BranchOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5226BranchOvercurrent = _LgpCondId5226BranchOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5226)
)
if mibBuilder.loadTexts:
    lgpCondId5226BranchOvercurrent.setStatus("current")
_LgpCondId5227BranchUndercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5227BranchUndercurrent = _LgpCondId5227BranchUndercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5227)
)
if mibBuilder.loadTexts:
    lgpCondId5227BranchUndercurrent.setStatus("current")
_LgpCondId5245SubfeedPhaseOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5245SubfeedPhaseOvercurrent = _LgpCondId5245SubfeedPhaseOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5245)
)
if mibBuilder.loadTexts:
    lgpCondId5245SubfeedPhaseOvercurrent.setStatus("current")
_LgpCondId5246SubfeedNeutralOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5246SubfeedNeutralOvercurrent = _LgpCondId5246SubfeedNeutralOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5246)
)
if mibBuilder.loadTexts:
    lgpCondId5246SubfeedNeutralOvercurrent.setStatus("current")
_LgpCondId5247SubfeedGroundOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5247SubfeedGroundOvercurrent = _LgpCondId5247SubfeedGroundOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5247)
)
if mibBuilder.loadTexts:
    lgpCondId5247SubfeedGroundOvercurrent.setStatus("current")
_LgpCondId5249EventState_ObjectIdentity = ObjectIdentity
lgpCondId5249EventState = _LgpCondId5249EventState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5249)
)
if mibBuilder.loadTexts:
    lgpCondId5249EventState.setStatus("current")
_LgpCondId5263CompressorNotStopping_ObjectIdentity = ObjectIdentity
lgpCondId5263CompressorNotStopping = _LgpCondId5263CompressorNotStopping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5263)
)
if mibBuilder.loadTexts:
    lgpCondId5263CompressorNotStopping.setStatus("current")
_LgpCondId5269CompressorHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5269CompressorHoursExceeded = _LgpCondId5269CompressorHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5269)
)
if mibBuilder.loadTexts:
    lgpCondId5269CompressorHoursExceeded.setStatus("current")
_LgpCondId5270CompressorHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId5270CompressorHighHeadPressure = _LgpCondId5270CompressorHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5270)
)
if mibBuilder.loadTexts:
    lgpCondId5270CompressorHighHeadPressure.setStatus("current")
_LgpCondId5271CompressorLowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId5271CompressorLowSuctionPressure = _LgpCondId5271CompressorLowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5271)
)
if mibBuilder.loadTexts:
    lgpCondId5271CompressorLowSuctionPressure.setStatus("current")
_LgpCondId5272CompressorThermalOverload_ObjectIdentity = ObjectIdentity
lgpCondId5272CompressorThermalOverload = _LgpCondId5272CompressorThermalOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5272)
)
if mibBuilder.loadTexts:
    lgpCondId5272CompressorThermalOverload.setStatus("current")
_LgpCondId5273CompressorLowOilPressure_ObjectIdentity = ObjectIdentity
lgpCondId5273CompressorLowOilPressure = _LgpCondId5273CompressorLowOilPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5273)
)
if mibBuilder.loadTexts:
    lgpCondId5273CompressorLowOilPressure.setStatus("current")
_LgpCondId5274CompressorHeadPressureOverThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5274CompressorHeadPressureOverThreshold = _LgpCondId5274CompressorHeadPressureOverThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5274)
)
if mibBuilder.loadTexts:
    lgpCondId5274CompressorHeadPressureOverThreshold.setStatus("current")
_LgpCondId5275CompressorLossofDifferentialPressure_ObjectIdentity = ObjectIdentity
lgpCondId5275CompressorLossofDifferentialPressure = _LgpCondId5275CompressorLossofDifferentialPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5275)
)
if mibBuilder.loadTexts:
    lgpCondId5275CompressorLossofDifferentialPressure.setStatus("current")
_LgpCondId5277CondenserFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5277CondenserFanIssue = _LgpCondId5277CondenserFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5277)
)
if mibBuilder.loadTexts:
    lgpCondId5277CondenserFanIssue.setStatus("current")
_LgpCondId5278LowCondenserRefrigerantPressure_ObjectIdentity = ObjectIdentity
lgpCondId5278LowCondenserRefrigerantPressure = _LgpCondId5278LowCondenserRefrigerantPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5278)
)
if mibBuilder.loadTexts:
    lgpCondId5278LowCondenserRefrigerantPressure.setStatus("current")
_LgpCondId5280LowFluidPressure_ObjectIdentity = ObjectIdentity
lgpCondId5280LowFluidPressure = _LgpCondId5280LowFluidPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5280)
)
if mibBuilder.loadTexts:
    lgpCondId5280LowFluidPressure.setStatus("current")
_LgpCondId5293ReturnFluidOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5293ReturnFluidOverTemp = _LgpCondId5293ReturnFluidOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5293)
)
if mibBuilder.loadTexts:
    lgpCondId5293ReturnFluidOverTemp.setStatus("current")
_LgpCondId5294ReturnFluidUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId5294ReturnFluidUnderTemp = _LgpCondId5294ReturnFluidUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5294)
)
if mibBuilder.loadTexts:
    lgpCondId5294ReturnFluidUnderTemp.setStatus("current")
_LgpCondId5295ReturnFluidTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5295ReturnFluidTempSensorIssue = _LgpCondId5295ReturnFluidTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5295)
)
if mibBuilder.loadTexts:
    lgpCondId5295ReturnFluidTempSensorIssue.setStatus("current")
_LgpCondId5296TeamworkReturnFluidTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5296TeamworkReturnFluidTempSensorIssue = _LgpCondId5296TeamworkReturnFluidTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5296)
)
if mibBuilder.loadTexts:
    lgpCondId5296TeamworkReturnFluidTempSensorIssue.setStatus("current")
_LgpCondId5297AllPumpsLossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId5297AllPumpsLossofFlow = _LgpCondId5297AllPumpsLossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5297)
)
if mibBuilder.loadTexts:
    lgpCondId5297AllPumpsLossofFlow.setStatus("current")
_LgpCondId5300PumpHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5300PumpHoursExceeded = _LgpCondId5300PumpHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5300)
)
if mibBuilder.loadTexts:
    lgpCondId5300PumpHoursExceeded.setStatus("current")
_LgpCondId5306FreeCoolingValveHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5306FreeCoolingValveHoursExceeded = _LgpCondId5306FreeCoolingValveHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5306)
)
if mibBuilder.loadTexts:
    lgpCondId5306FreeCoolingValveHoursExceeded.setStatus("current")
_LgpCondId5308EvaporatorInletTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5308EvaporatorInletTempSensorIssue = _LgpCondId5308EvaporatorInletTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5308)
)
if mibBuilder.loadTexts:
    lgpCondId5308EvaporatorInletTempSensorIssue.setStatus("current")
_LgpCondId5309TeamworkEvaporatorInletTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5309TeamworkEvaporatorInletTempSensorIssue = _LgpCondId5309TeamworkEvaporatorInletTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5309)
)
if mibBuilder.loadTexts:
    lgpCondId5309TeamworkEvaporatorInletTempSensorIssue.setStatus("current")
_LgpCondId5310EvaporatorFluidFreezeAutoReset_ObjectIdentity = ObjectIdentity
lgpCondId5310EvaporatorFluidFreezeAutoReset = _LgpCondId5310EvaporatorFluidFreezeAutoReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5310)
)
if mibBuilder.loadTexts:
    lgpCondId5310EvaporatorFluidFreezeAutoReset.setStatus("current")
_LgpCondId5311EvaporatorFluidFreezeManualResetRequired_ObjectIdentity = ObjectIdentity
lgpCondId5311EvaporatorFluidFreezeManualResetRequired = _LgpCondId5311EvaporatorFluidFreezeManualResetRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5311)
)
if mibBuilder.loadTexts:
    lgpCondId5311EvaporatorFluidFreezeManualResetRequired.setStatus("current")
_LgpCondId5315SubgroupEventOccurredDuringCommunicationLoss_ObjectIdentity = ObjectIdentity
lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss = _LgpCondId5315SubgroupEventOccurredDuringCommunicationLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5315)
)
if mibBuilder.loadTexts:
    lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss.setStatus("current")
_LgpCondId5335ReturnAirUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5335ReturnAirUnderTemperature = _LgpCondId5335ReturnAirUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5335)
)
if mibBuilder.loadTexts:
    lgpCondId5335ReturnAirUnderTemperature.setStatus("current")
_LgpCondId5349ExtAirSensorAHighHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5349ExtAirSensorAHighHumidity = _LgpCondId5349ExtAirSensorAHighHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5349)
)
if mibBuilder.loadTexts:
    lgpCondId5349ExtAirSensorAHighHumidity.setStatus("current")
_LgpCondId5351ExtAirSensorALowHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5351ExtAirSensorALowHumidity = _LgpCondId5351ExtAirSensorALowHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5351)
)
if mibBuilder.loadTexts:
    lgpCondId5351ExtAirSensorALowHumidity.setStatus("current")
_LgpCondId5352CompressorShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId5352CompressorShortCycle = _LgpCondId5352CompressorShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5352)
)
if mibBuilder.loadTexts:
    lgpCondId5352CompressorShortCycle.setStatus("current")
_LgpCondId5354DigScrollCompDischargeTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5354DigScrollCompDischargeTempSensorIssue = _LgpCondId5354DigScrollCompDischargeTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5354)
)
if mibBuilder.loadTexts:
    lgpCondId5354DigScrollCompDischargeTempSensorIssue.setStatus("current")
_LgpCondId5355DigScrollCompOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5355DigScrollCompOverTemp = _LgpCondId5355DigScrollCompOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5355)
)
if mibBuilder.loadTexts:
    lgpCondId5355DigScrollCompOverTemp.setStatus("current")
_LgpCondId5361ExtFreeCoolingLockout_ObjectIdentity = ObjectIdentity
lgpCondId5361ExtFreeCoolingLockout = _LgpCondId5361ExtFreeCoolingLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5361)
)
if mibBuilder.loadTexts:
    lgpCondId5361ExtFreeCoolingLockout.setStatus("current")
_LgpCondId5362FreeCoolingTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5362FreeCoolingTempSensorIssue = _LgpCondId5362FreeCoolingTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5362)
)
if mibBuilder.loadTexts:
    lgpCondId5362FreeCoolingTempSensorIssue.setStatus("current")
_LgpCondId5365HotWaterHotGasValveHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5365HotWaterHotGasValveHoursExceeded = _LgpCondId5365HotWaterHotGasValveHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5365)
)
if mibBuilder.loadTexts:
    lgpCondId5365HotWaterHotGasValveHoursExceeded.setStatus("current")
_LgpCondId5368ElectricReheaterHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5368ElectricReheaterHoursExceeded = _LgpCondId5368ElectricReheaterHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5368)
)
if mibBuilder.loadTexts:
    lgpCondId5368ElectricReheaterHoursExceeded.setStatus("current")
_LgpCondId5376MainFanOverload_ObjectIdentity = ObjectIdentity
lgpCondId5376MainFanOverload = _LgpCondId5376MainFanOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5376)
)
if mibBuilder.loadTexts:
    lgpCondId5376MainFanOverload.setStatus("current")
_LgpCondId5377Condenser_ObjectIdentity = ObjectIdentity
lgpCondId5377Condenser = _LgpCondId5377Condenser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5377)
)
if mibBuilder.loadTexts:
    lgpCondId5377Condenser.setStatus("current")
_LgpCondId5415ExtLossofAirBlower_ObjectIdentity = ObjectIdentity
lgpCondId5415ExtLossofAirBlower = _LgpCondId5415ExtLossofAirBlower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5415)
)
if mibBuilder.loadTexts:
    lgpCondId5415ExtLossofAirBlower.setStatus("current")
_LgpCondId5416ExtStandbyUnitOn_ObjectIdentity = ObjectIdentity
lgpCondId5416ExtStandbyUnitOn = _LgpCondId5416ExtStandbyUnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5416)
)
if mibBuilder.loadTexts:
    lgpCondId5416ExtStandbyUnitOn.setStatus("current")
_LgpCondId5417DigitalOutputBoardNotDetected_ObjectIdentity = ObjectIdentity
lgpCondId5417DigitalOutputBoardNotDetected = _LgpCondId5417DigitalOutputBoardNotDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5417)
)
if mibBuilder.loadTexts:
    lgpCondId5417DigitalOutputBoardNotDetected.setStatus("current")
_LgpCondId5418UnitCodeMissing_ObjectIdentity = ObjectIdentity
lgpCondId5418UnitCodeMissing = _LgpCondId5418UnitCodeMissing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5418)
)
if mibBuilder.loadTexts:
    lgpCondId5418UnitCodeMissing.setStatus("current")
_LgpCondId5419UnitCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5419UnitCommunicationLost = _LgpCondId5419UnitCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5419)
)
if mibBuilder.loadTexts:
    lgpCondId5419UnitCommunicationLost.setStatus("current")
_LgpCondId5422OvertemperaturePowerOff_ObjectIdentity = ObjectIdentity
lgpCondId5422OvertemperaturePowerOff = _LgpCondId5422OvertemperaturePowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5422)
)
if mibBuilder.loadTexts:
    lgpCondId5422OvertemperaturePowerOff.setStatus("current")
_LgpCondId5423TooManySensors_ObjectIdentity = ObjectIdentity
lgpCondId5423TooManySensors = _LgpCondId5423TooManySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5423)
)
if mibBuilder.loadTexts:
    lgpCondId5423TooManySensors.setStatus("current")
_LgpCondId5432TransformerOvertemperaturePowerOff_ObjectIdentity = ObjectIdentity
lgpCondId5432TransformerOvertemperaturePowerOff = _LgpCondId5432TransformerOvertemperaturePowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5432)
)
if mibBuilder.loadTexts:
    lgpCondId5432TransformerOvertemperaturePowerOff.setStatus("current")
_LgpCondId5433TransformerOvertemperature_ObjectIdentity = ObjectIdentity
lgpCondId5433TransformerOvertemperature = _LgpCondId5433TransformerOvertemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5433)
)
if mibBuilder.loadTexts:
    lgpCondId5433TransformerOvertemperature.setStatus("current")
_LgpCondId5434TransformerTemperatureSensorFail_ObjectIdentity = ObjectIdentity
lgpCondId5434TransformerTemperatureSensorFail = _LgpCondId5434TransformerTemperatureSensorFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5434)
)
if mibBuilder.loadTexts:
    lgpCondId5434TransformerTemperatureSensorFail.setStatus("current")
_LgpCondId5436LowAmbientTemperatureProbeTwo_ObjectIdentity = ObjectIdentity
lgpCondId5436LowAmbientTemperatureProbeTwo = _LgpCondId5436LowAmbientTemperatureProbeTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5436)
)
if mibBuilder.loadTexts:
    lgpCondId5436LowAmbientTemperatureProbeTwo.setStatus("current")
_LgpCondId5437HighAmbientTemperatureProbeTwo_ObjectIdentity = ObjectIdentity
lgpCondId5437HighAmbientTemperatureProbeTwo = _LgpCondId5437HighAmbientTemperatureProbeTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5437)
)
if mibBuilder.loadTexts:
    lgpCondId5437HighAmbientTemperatureProbeTwo.setStatus("current")
_LgpCondId5438ThermalRunawayDetected_ObjectIdentity = ObjectIdentity
lgpCondId5438ThermalRunawayDetected = _LgpCondId5438ThermalRunawayDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5438)
)
if mibBuilder.loadTexts:
    lgpCondId5438ThermalRunawayDetected.setStatus("current")
_LgpCondId5439BatteryStringEqualize_ObjectIdentity = ObjectIdentity
lgpCondId5439BatteryStringEqualize = _LgpCondId5439BatteryStringEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5439)
)
if mibBuilder.loadTexts:
    lgpCondId5439BatteryStringEqualize.setStatus("current")
_LgpCondId5440BatteryStringOffline_ObjectIdentity = ObjectIdentity
lgpCondId5440BatteryStringOffline = _LgpCondId5440BatteryStringOffline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5440)
)
if mibBuilder.loadTexts:
    lgpCondId5440BatteryStringOffline.setStatus("current")
_LgpCondId5442DischargeLowCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId5442DischargeLowCellVoltage = _LgpCondId5442DischargeLowCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5442)
)
if mibBuilder.loadTexts:
    lgpCondId5442DischargeLowCellVoltage.setStatus("current")
_LgpCondId5447MMSPowerSharing_ObjectIdentity = ObjectIdentity
lgpCondId5447MMSPowerSharing = _LgpCondId5447MMSPowerSharing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5447)
)
if mibBuilder.loadTexts:
    lgpCondId5447MMSPowerSharing.setStatus("current")
_LgpCondId5453ModuleInStandbyIntelligentParalleling_ObjectIdentity = ObjectIdentity
lgpCondId5453ModuleInStandbyIntelligentParalleling = _LgpCondId5453ModuleInStandbyIntelligentParalleling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5453)
)
if mibBuilder.loadTexts:
    lgpCondId5453ModuleInStandbyIntelligentParalleling.setStatus("current")
_LgpCondId5456ECOModeActive_ObjectIdentity = ObjectIdentity
lgpCondId5456ECOModeActive = _LgpCondId5456ECOModeActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5456)
)
if mibBuilder.loadTexts:
    lgpCondId5456ECOModeActive.setStatus("current")
_LgpCondId5457ECOModeSuspended_ObjectIdentity = ObjectIdentity
lgpCondId5457ECOModeSuspended = _LgpCondId5457ECOModeSuspended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5457)
)
if mibBuilder.loadTexts:
    lgpCondId5457ECOModeSuspended.setStatus("current")
_LgpCondId5458ExcessECOSuspends_ObjectIdentity = ObjectIdentity
lgpCondId5458ExcessECOSuspends = _LgpCondId5458ExcessECOSuspends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5458)
)
if mibBuilder.loadTexts:
    lgpCondId5458ExcessECOSuspends.setStatus("current")
_LgpCondId5471DoorOpen_ObjectIdentity = ObjectIdentity
lgpCondId5471DoorOpen = _LgpCondId5471DoorOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5471)
)
if mibBuilder.loadTexts:
    lgpCondId5471DoorOpen.setStatus("current")
_LgpCondId5472DoorSensorDisconnected_ObjectIdentity = ObjectIdentity
lgpCondId5472DoorSensorDisconnected = _LgpCondId5472DoorSensorDisconnected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5472)
)
if mibBuilder.loadTexts:
    lgpCondId5472DoorSensorDisconnected.setStatus("current")
_LgpCondId5479ContactClosureOpen_ObjectIdentity = ObjectIdentity
lgpCondId5479ContactClosureOpen = _LgpCondId5479ContactClosureOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5479)
)
if mibBuilder.loadTexts:
    lgpCondId5479ContactClosureOpen.setStatus("current")
_LgpCondId5480ContactClosureClosed_ObjectIdentity = ObjectIdentity
lgpCondId5480ContactClosureClosed = _LgpCondId5480ContactClosureClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5480)
)
if mibBuilder.loadTexts:
    lgpCondId5480ContactClosureClosed.setStatus("current")
_LgpCondId5492ExtSystemCondensationDetected_ObjectIdentity = ObjectIdentity
lgpCondId5492ExtSystemCondensationDetected = _LgpCondId5492ExtSystemCondensationDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5492)
)
if mibBuilder.loadTexts:
    lgpCondId5492ExtSystemCondensationDetected.setStatus("current")
_LgpCondId5495ExtFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5495ExtFanIssue = _LgpCondId5495ExtFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5495)
)
if mibBuilder.loadTexts:
    lgpCondId5495ExtFanIssue.setStatus("current")
_LgpCondId5500ExtRemoteShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5500ExtRemoteShutdown = _LgpCondId5500ExtRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5500)
)
if mibBuilder.loadTexts:
    lgpCondId5500ExtRemoteShutdown.setStatus("current")
_LgpCondId5505HotAisleTempOutofRange_ObjectIdentity = ObjectIdentity
lgpCondId5505HotAisleTempOutofRange = _LgpCondId5505HotAisleTempOutofRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5505)
)
if mibBuilder.loadTexts:
    lgpCondId5505HotAisleTempOutofRange.setStatus("current")
_LgpCondId5508ColdAisleTempOutofRange_ObjectIdentity = ObjectIdentity
lgpCondId5508ColdAisleTempOutofRange = _LgpCondId5508ColdAisleTempOutofRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5508)
)
if mibBuilder.loadTexts:
    lgpCondId5508ColdAisleTempOutofRange.setStatus("current")
_LgpCondId5512RemoteShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5512RemoteShutdown = _LgpCondId5512RemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5512)
)
if mibBuilder.loadTexts:
    lgpCondId5512RemoteShutdown.setStatus("current")
_LgpCondId5513CompressorCapacityReduced_ObjectIdentity = ObjectIdentity
lgpCondId5513CompressorCapacityReduced = _LgpCondId5513CompressorCapacityReduced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5513)
)
if mibBuilder.loadTexts:
    lgpCondId5513CompressorCapacityReduced.setStatus("current")
_LgpCondId5514CompressorLowPressureTransducerIssue_ObjectIdentity = ObjectIdentity
lgpCondId5514CompressorLowPressureTransducerIssue = _LgpCondId5514CompressorLowPressureTransducerIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5514)
)
if mibBuilder.loadTexts:
    lgpCondId5514CompressorLowPressureTransducerIssue.setStatus("current")
_LgpCondId5524PDUNeutralOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId5524PDUNeutralOverCurrent = _LgpCondId5524PDUNeutralOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5524)
)
if mibBuilder.loadTexts:
    lgpCondId5524PDUNeutralOverCurrent.setStatus("current")
_LgpCondId5531CondenserCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5531CondenserCommunicationLost = _LgpCondId5531CondenserCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5531)
)
if mibBuilder.loadTexts:
    lgpCondId5531CondenserCommunicationLost.setStatus("current")
_LgpCondId5535CondenserOutsideAirTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5535CondenserOutsideAirTempSensorIssue = _LgpCondId5535CondenserOutsideAirTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5535)
)
if mibBuilder.loadTexts:
    lgpCondId5535CondenserOutsideAirTempSensorIssue.setStatus("current")
_LgpCondId5536CondenserOutsideAirTempOutofOperatingRange_ObjectIdentity = ObjectIdentity
lgpCondId5536CondenserOutsideAirTempOutofOperatingRange = _LgpCondId5536CondenserOutsideAirTempOutofOperatingRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5536)
)
if mibBuilder.loadTexts:
    lgpCondId5536CondenserOutsideAirTempOutofOperatingRange.setStatus("current")
_LgpCondId5537CondenserControlBoardIssue_ObjectIdentity = ObjectIdentity
lgpCondId5537CondenserControlBoardIssue = _LgpCondId5537CondenserControlBoardIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5537)
)
if mibBuilder.loadTexts:
    lgpCondId5537CondenserControlBoardIssue.setStatus("current")
_LgpCondId5539CondenserRefrigerantPressureOverThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5539CondenserRefrigerantPressureOverThreshold = _LgpCondId5539CondenserRefrigerantPressureOverThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5539)
)
if mibBuilder.loadTexts:
    lgpCondId5539CondenserRefrigerantPressureOverThreshold.setStatus("current")
_LgpCondId5540CondenserRefrigerantPressureUnderThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5540CondenserRefrigerantPressureUnderThreshold = _LgpCondId5540CondenserRefrigerantPressureUnderThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5540)
)
if mibBuilder.loadTexts:
    lgpCondId5540CondenserRefrigerantPressureUnderThreshold.setStatus("current")
_LgpCondId5541CondenserRefrigerantPressureSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5541CondenserRefrigerantPressureSensorIssue = _LgpCondId5541CondenserRefrigerantPressureSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5541)
)
if mibBuilder.loadTexts:
    lgpCondId5541CondenserRefrigerantPressureSensorIssue.setStatus("current")
_LgpCondId5542CondenserSupplyRefrigerantOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5542CondenserSupplyRefrigerantOverTemp = _LgpCondId5542CondenserSupplyRefrigerantOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5542)
)
if mibBuilder.loadTexts:
    lgpCondId5542CondenserSupplyRefrigerantOverTemp.setStatus("current")
_LgpCondId5543CondenserSupplyRefrigerantUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId5543CondenserSupplyRefrigerantUnderTemp = _LgpCondId5543CondenserSupplyRefrigerantUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5543)
)
if mibBuilder.loadTexts:
    lgpCondId5543CondenserSupplyRefrigerantUnderTemp.setStatus("current")
_LgpCondId5544CondenserSupplyRefrigerantTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue = _LgpCondId5544CondenserSupplyRefrigerantTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5544)
)
if mibBuilder.loadTexts:
    lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue.setStatus("current")
_LgpCondId5545CondenserMaxFanSpeedOverride_ObjectIdentity = ObjectIdentity
lgpCondId5545CondenserMaxFanSpeedOverride = _LgpCondId5545CondenserMaxFanSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5545)
)
if mibBuilder.loadTexts:
    lgpCondId5545CondenserMaxFanSpeedOverride.setStatus("current")
_LgpCondId5559EvaporatorReturnFluidOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5559EvaporatorReturnFluidOverTemp = _LgpCondId5559EvaporatorReturnFluidOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5559)
)
if mibBuilder.loadTexts:
    lgpCondId5559EvaporatorReturnFluidOverTemp.setStatus("current")
_LgpCondId5560EvaporatorReturnFluidUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId5560EvaporatorReturnFluidUnderTemp = _LgpCondId5560EvaporatorReturnFluidUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5560)
)
if mibBuilder.loadTexts:
    lgpCondId5560EvaporatorReturnFluidUnderTemp.setStatus("current")
_LgpCondId5561LBSActiveMaster_ObjectIdentity = ObjectIdentity
lgpCondId5561LBSActiveMaster = _LgpCondId5561LBSActiveMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5561)
)
if mibBuilder.loadTexts:
    lgpCondId5561LBSActiveMaster.setStatus("current")
_LgpCondId5562LBSActiveSlave_ObjectIdentity = ObjectIdentity
lgpCondId5562LBSActiveSlave = _LgpCondId5562LBSActiveSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5562)
)
if mibBuilder.loadTexts:
    lgpCondId5562LBSActiveSlave.setStatus("current")
_LgpCondId5563DCBusLowFault_ObjectIdentity = ObjectIdentity
lgpCondId5563DCBusLowFault = _LgpCondId5563DCBusLowFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5563)
)
if mibBuilder.loadTexts:
    lgpCondId5563DCBusLowFault.setStatus("current")
_LgpCondId5564FanContactorOpen_ObjectIdentity = ObjectIdentity
lgpCondId5564FanContactorOpen = _LgpCondId5564FanContactorOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5564)
)
if mibBuilder.loadTexts:
    lgpCondId5564FanContactorOpen.setStatus("current")
_LgpCondId5565FanContactorOpenFail_ObjectIdentity = ObjectIdentity
lgpCondId5565FanContactorOpenFail = _LgpCondId5565FanContactorOpenFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5565)
)
if mibBuilder.loadTexts:
    lgpCondId5565FanContactorOpenFail.setStatus("current")
_LgpCondId5566FanContactorCloseFail_ObjectIdentity = ObjectIdentity
lgpCondId5566FanContactorCloseFail = _LgpCondId5566FanContactorCloseFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5566)
)
if mibBuilder.loadTexts:
    lgpCondId5566FanContactorCloseFail.setStatus("current")
_LgpCondId5567IPInhibit_ObjectIdentity = ObjectIdentity
lgpCondId5567IPInhibit = _LgpCondId5567IPInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5567)
)
if mibBuilder.loadTexts:
    lgpCondId5567IPInhibit.setStatus("current")
_LgpCondId5568InputUndervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5568InputUndervoltage = _LgpCondId5568InputUndervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5568)
)
if mibBuilder.loadTexts:
    lgpCondId5568InputUndervoltage.setStatus("current")
_LgpCondId5569InputOvervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5569InputOvervoltage = _LgpCondId5569InputOvervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5569)
)
if mibBuilder.loadTexts:
    lgpCondId5569InputOvervoltage.setStatus("current")
_LgpCondId5573AmbientAirSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5573AmbientAirSensorIssue = _LgpCondId5573AmbientAirSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5573)
)
if mibBuilder.loadTexts:
    lgpCondId5573AmbientAirSensorIssue.setStatus("current")
_LgpCondId5577ExtDewPointUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5577ExtDewPointUnderTemperature = _LgpCondId5577ExtDewPointUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5577)
)
if mibBuilder.loadTexts:
    lgpCondId5577ExtDewPointUnderTemperature.setStatus("current")
_LgpCondId5578DewPointOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5578DewPointOverTemperature = _LgpCondId5578DewPointOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5578)
)
if mibBuilder.loadTexts:
    lgpCondId5578DewPointOverTemperature.setStatus("current")
_LgpCondId5579DewPointUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5579DewPointUnderTemperature = _LgpCondId5579DewPointUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5579)
)
if mibBuilder.loadTexts:
    lgpCondId5579DewPointUnderTemperature.setStatus("current")
_LgpCondId5588UnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId5588UnspecifiedGeneralEvent = _LgpCondId5588UnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5588)
)
if mibBuilder.loadTexts:
    lgpCondId5588UnspecifiedGeneralEvent.setStatus("current")
_LgpCondId5593RemoteSensorAverageOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5593RemoteSensorAverageOverTemperature = _LgpCondId5593RemoteSensorAverageOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5593)
)
if mibBuilder.loadTexts:
    lgpCondId5593RemoteSensorAverageOverTemperature.setStatus("current")
_LgpCondId5594RemoteSensorAverageUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5594RemoteSensorAverageUnderTemperature = _LgpCondId5594RemoteSensorAverageUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5594)
)
if mibBuilder.loadTexts:
    lgpCondId5594RemoteSensorAverageUnderTemperature.setStatus("current")
_LgpCondId5595RemoteSensorSystemAverageOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5595RemoteSensorSystemAverageOverTemperature = _LgpCondId5595RemoteSensorSystemAverageOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5595)
)
if mibBuilder.loadTexts:
    lgpCondId5595RemoteSensorSystemAverageOverTemperature.setStatus("current")
_LgpCondId5596RemoteSensorSystemAverageUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5596RemoteSensorSystemAverageUnderTemperature = _LgpCondId5596RemoteSensorSystemAverageUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5596)
)
if mibBuilder.loadTexts:
    lgpCondId5596RemoteSensorSystemAverageUnderTemperature.setStatus("current")
_LgpCondId5597RemoteSensorOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5597RemoteSensorOverTemperature = _LgpCondId5597RemoteSensorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5597)
)
if mibBuilder.loadTexts:
    lgpCondId5597RemoteSensorOverTemperature.setStatus("current")
_LgpCondId5598RemoteSensorUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5598RemoteSensorUnderTemperature = _LgpCondId5598RemoteSensorUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5598)
)
if mibBuilder.loadTexts:
    lgpCondId5598RemoteSensorUnderTemperature.setStatus("current")
_LgpCondId5600AirEconomizerEmergencyOverride_ObjectIdentity = ObjectIdentity
lgpCondId5600AirEconomizerEmergencyOverride = _LgpCondId5600AirEconomizerEmergencyOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5600)
)
if mibBuilder.loadTexts:
    lgpCondId5600AirEconomizerEmergencyOverride.setStatus("current")
_LgpCondId5601AirEconomizerReducedAirflow_ObjectIdentity = ObjectIdentity
lgpCondId5601AirEconomizerReducedAirflow = _LgpCondId5601AirEconomizerReducedAirflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5601)
)
if mibBuilder.loadTexts:
    lgpCondId5601AirEconomizerReducedAirflow.setStatus("current")
_LgpCondId5604CompressorSuperheatOverThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5604CompressorSuperheatOverThreshold = _LgpCondId5604CompressorSuperheatOverThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5604)
)
if mibBuilder.loadTexts:
    lgpCondId5604CompressorSuperheatOverThreshold.setStatus("current")
_LgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent_ObjectIdentity = ObjectIdentity
lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent = _LgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5609)
)
if mibBuilder.loadTexts:
    lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent.setStatus("current")
_LgpCondId5610ThermalRunawayCelltoCellTemperatureEvent_ObjectIdentity = ObjectIdentity
lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent = _LgpCondId5610ThermalRunawayCelltoCellTemperatureEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5610)
)
if mibBuilder.loadTexts:
    lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent.setStatus("current")
_LgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent_ObjectIdentity = ObjectIdentity
lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent = _LgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5611)
)
if mibBuilder.loadTexts:
    lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent.setStatus("current")
_LgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent_ObjectIdentity = ObjectIdentity
lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent = _LgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5612)
)
if mibBuilder.loadTexts:
    lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent.setStatus("current")
_LgpCondId5617TemperatureControlSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5617TemperatureControlSensorIssue = _LgpCondId5617TemperatureControlSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5617)
)
if mibBuilder.loadTexts:
    lgpCondId5617TemperatureControlSensorIssue.setStatus("current")
_LgpCondId5621EEVSuperheatBelowThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5621EEVSuperheatBelowThreshold = _LgpCondId5621EEVSuperheatBelowThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5621)
)
if mibBuilder.loadTexts:
    lgpCondId5621EEVSuperheatBelowThreshold.setStatus("current")
_LgpCondId5622EEVDischargeTempAboveThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5622EEVDischargeTempAboveThreshold = _LgpCondId5622EEVDischargeTempAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5622)
)
if mibBuilder.loadTexts:
    lgpCondId5622EEVDischargeTempAboveThreshold.setStatus("current")
_LgpCondId5623EEVBatteryIssue_ObjectIdentity = ObjectIdentity
lgpCondId5623EEVBatteryIssue = _LgpCondId5623EEVBatteryIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5623)
)
if mibBuilder.loadTexts:
    lgpCondId5623EEVBatteryIssue.setStatus("current")
_LgpCondId5624EEVPowerIssue_ObjectIdentity = ObjectIdentity
lgpCondId5624EEVPowerIssue = _LgpCondId5624EEVPowerIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5624)
)
if mibBuilder.loadTexts:
    lgpCondId5624EEVPowerIssue.setStatus("current")
_LgpCondId5625EEVUnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId5625EEVUnspecifiedGeneralEvent = _LgpCondId5625EEVUnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5625)
)
if mibBuilder.loadTexts:
    lgpCondId5625EEVUnspecifiedGeneralEvent.setStatus("current")
_LgpCondId5629StaticPressureSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5629StaticPressureSensorIssue = _LgpCondId5629StaticPressureSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5629)
)
if mibBuilder.loadTexts:
    lgpCondId5629StaticPressureSensorIssue.setStatus("current")
_LgpCondId5630HighStaticPressure_ObjectIdentity = ObjectIdentity
lgpCondId5630HighStaticPressure = _LgpCondId5630HighStaticPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5630)
)
if mibBuilder.loadTexts:
    lgpCondId5630HighStaticPressure.setStatus("current")
_LgpCondId5631LowStaticPressure_ObjectIdentity = ObjectIdentity
lgpCondId5631LowStaticPressure = _LgpCondId5631LowStaticPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5631)
)
if mibBuilder.loadTexts:
    lgpCondId5631LowStaticPressure.setStatus("current")
_LgpCondId5636PumpUnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId5636PumpUnspecifiedGeneralEvent = _LgpCondId5636PumpUnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5636)
)
if mibBuilder.loadTexts:
    lgpCondId5636PumpUnspecifiedGeneralEvent.setStatus("current")
_LgpCondId5637CondenserUnitUnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId5637CondenserUnitUnspecifiedGeneralEvent = _LgpCondId5637CondenserUnitUnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5637)
)
if mibBuilder.loadTexts:
    lgpCondId5637CondenserUnitUnspecifiedGeneralEvent.setStatus("current")
_LgpCondId5638CondenserCircuitUnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId5638CondenserCircuitUnspecifiedGeneralEvent = _LgpCondId5638CondenserCircuitUnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5638)
)
if mibBuilder.loadTexts:
    lgpCondId5638CondenserCircuitUnspecifiedGeneralEvent.setStatus("current")
_LgpCondId5642SFAReservedEvent1_ObjectIdentity = ObjectIdentity
lgpCondId5642SFAReservedEvent1 = _LgpCondId5642SFAReservedEvent1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5642)
)
if mibBuilder.loadTexts:
    lgpCondId5642SFAReservedEvent1.setStatus("current")
_LgpCondId5643SFAReservedEvent2_ObjectIdentity = ObjectIdentity
lgpCondId5643SFAReservedEvent2 = _LgpCondId5643SFAReservedEvent2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5643)
)
if mibBuilder.loadTexts:
    lgpCondId5643SFAReservedEvent2.setStatus("current")
_LgpCondId5644SFAReservedEvent3_ObjectIdentity = ObjectIdentity
lgpCondId5644SFAReservedEvent3 = _LgpCondId5644SFAReservedEvent3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5644)
)
if mibBuilder.loadTexts:
    lgpCondId5644SFAReservedEvent3.setStatus("current")
_LgpCondId5645SFAReservedEvent4_ObjectIdentity = ObjectIdentity
lgpCondId5645SFAReservedEvent4 = _LgpCondId5645SFAReservedEvent4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5645)
)
if mibBuilder.loadTexts:
    lgpCondId5645SFAReservedEvent4.setStatus("current")
_LgpCondId5646SFAReservedEvent5_ObjectIdentity = ObjectIdentity
lgpCondId5646SFAReservedEvent5 = _LgpCondId5646SFAReservedEvent5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5646)
)
if mibBuilder.loadTexts:
    lgpCondId5646SFAReservedEvent5.setStatus("current")
_LgpCondId5647SFAReservedEvent6_ObjectIdentity = ObjectIdentity
lgpCondId5647SFAReservedEvent6 = _LgpCondId5647SFAReservedEvent6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5647)
)
if mibBuilder.loadTexts:
    lgpCondId5647SFAReservedEvent6.setStatus("current")
_LgpCondId5648SFAReservedEvent7_ObjectIdentity = ObjectIdentity
lgpCondId5648SFAReservedEvent7 = _LgpCondId5648SFAReservedEvent7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5648)
)
if mibBuilder.loadTexts:
    lgpCondId5648SFAReservedEvent7.setStatus("current")
_LgpCondId5649SFAReservedEvent8_ObjectIdentity = ObjectIdentity
lgpCondId5649SFAReservedEvent8 = _LgpCondId5649SFAReservedEvent8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5649)
)
if mibBuilder.loadTexts:
    lgpCondId5649SFAReservedEvent8.setStatus("current")
_LgpCondId5650SFAReservedEvent9_ObjectIdentity = ObjectIdentity
lgpCondId5650SFAReservedEvent9 = _LgpCondId5650SFAReservedEvent9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5650)
)
if mibBuilder.loadTexts:
    lgpCondId5650SFAReservedEvent9.setStatus("current")
_LgpCondId5651SFAReservedEvent10_ObjectIdentity = ObjectIdentity
lgpCondId5651SFAReservedEvent10 = _LgpCondId5651SFAReservedEvent10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5651)
)
if mibBuilder.loadTexts:
    lgpCondId5651SFAReservedEvent10.setStatus("current")
_LgpCondId5652SFAReservedEvent11_ObjectIdentity = ObjectIdentity
lgpCondId5652SFAReservedEvent11 = _LgpCondId5652SFAReservedEvent11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5652)
)
if mibBuilder.loadTexts:
    lgpCondId5652SFAReservedEvent11.setStatus("current")
_LgpCondId5653SFAReservedEvent12_ObjectIdentity = ObjectIdentity
lgpCondId5653SFAReservedEvent12 = _LgpCondId5653SFAReservedEvent12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5653)
)
if mibBuilder.loadTexts:
    lgpCondId5653SFAReservedEvent12.setStatus("current")
_LgpCondId5654SFAReservedEvent13_ObjectIdentity = ObjectIdentity
lgpCondId5654SFAReservedEvent13 = _LgpCondId5654SFAReservedEvent13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5654)
)
if mibBuilder.loadTexts:
    lgpCondId5654SFAReservedEvent13.setStatus("current")
_LgpCondId5655SFAReservedEvent14_ObjectIdentity = ObjectIdentity
lgpCondId5655SFAReservedEvent14 = _LgpCondId5655SFAReservedEvent14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5655)
)
if mibBuilder.loadTexts:
    lgpCondId5655SFAReservedEvent14.setStatus("current")
_LgpCondId5656SFAReservedEvent15_ObjectIdentity = ObjectIdentity
lgpCondId5656SFAReservedEvent15 = _LgpCondId5656SFAReservedEvent15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5656)
)
if mibBuilder.loadTexts:
    lgpCondId5656SFAReservedEvent15.setStatus("current")
_LgpCondId5657SFAReservedEvent16_ObjectIdentity = ObjectIdentity
lgpCondId5657SFAReservedEvent16 = _LgpCondId5657SFAReservedEvent16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5657)
)
if mibBuilder.loadTexts:
    lgpCondId5657SFAReservedEvent16.setStatus("current")
_LgpCondId5658SFAReservedEvent17_ObjectIdentity = ObjectIdentity
lgpCondId5658SFAReservedEvent17 = _LgpCondId5658SFAReservedEvent17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5658)
)
if mibBuilder.loadTexts:
    lgpCondId5658SFAReservedEvent17.setStatus("current")
_LgpCondId5659SFAReservedEvent18_ObjectIdentity = ObjectIdentity
lgpCondId5659SFAReservedEvent18 = _LgpCondId5659SFAReservedEvent18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5659)
)
if mibBuilder.loadTexts:
    lgpCondId5659SFAReservedEvent18.setStatus("current")
_LgpCondId5660SFAReservedEvent19_ObjectIdentity = ObjectIdentity
lgpCondId5660SFAReservedEvent19 = _LgpCondId5660SFAReservedEvent19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5660)
)
if mibBuilder.loadTexts:
    lgpCondId5660SFAReservedEvent19.setStatus("current")
_LgpCondId5661SFAReservedEvent20_ObjectIdentity = ObjectIdentity
lgpCondId5661SFAReservedEvent20 = _LgpCondId5661SFAReservedEvent20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5661)
)
if mibBuilder.loadTexts:
    lgpCondId5661SFAReservedEvent20.setStatus("current")
_LgpCondId5662SFAReservedEvent21_ObjectIdentity = ObjectIdentity
lgpCondId5662SFAReservedEvent21 = _LgpCondId5662SFAReservedEvent21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5662)
)
if mibBuilder.loadTexts:
    lgpCondId5662SFAReservedEvent21.setStatus("current")
_LgpCondId5663SFAReservedEvent22_ObjectIdentity = ObjectIdentity
lgpCondId5663SFAReservedEvent22 = _LgpCondId5663SFAReservedEvent22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5663)
)
if mibBuilder.loadTexts:
    lgpCondId5663SFAReservedEvent22.setStatus("current")
_LgpCondId5664SFAReservedEvent23_ObjectIdentity = ObjectIdentity
lgpCondId5664SFAReservedEvent23 = _LgpCondId5664SFAReservedEvent23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5664)
)
if mibBuilder.loadTexts:
    lgpCondId5664SFAReservedEvent23.setStatus("current")
_LgpCondId5665SFAReservedEvent24_ObjectIdentity = ObjectIdentity
lgpCondId5665SFAReservedEvent24 = _LgpCondId5665SFAReservedEvent24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5665)
)
if mibBuilder.loadTexts:
    lgpCondId5665SFAReservedEvent24.setStatus("current")
_LgpCondId5666SFAReservedEvent25_ObjectIdentity = ObjectIdentity
lgpCondId5666SFAReservedEvent25 = _LgpCondId5666SFAReservedEvent25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5666)
)
if mibBuilder.loadTexts:
    lgpCondId5666SFAReservedEvent25.setStatus("current")
_LgpCondId5768OutletAirOvertemperatureLimit_ObjectIdentity = ObjectIdentity
lgpCondId5768OutletAirOvertemperatureLimit = _LgpCondId5768OutletAirOvertemperatureLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5768)
)
if mibBuilder.loadTexts:
    lgpCondId5768OutletAirOvertemperatureLimit.setStatus("current")
_LgpCondId5769EMOShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5769EMOShutdown = _LgpCondId5769EMOShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5769)
)
if mibBuilder.loadTexts:
    lgpCondId5769EMOShutdown.setStatus("current")
_LgpCondId5770TopOutletFanFault_ObjectIdentity = ObjectIdentity
lgpCondId5770TopOutletFanFault = _LgpCondId5770TopOutletFanFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5770)
)
if mibBuilder.loadTexts:
    lgpCondId5770TopOutletFanFault.setStatus("current")
_LgpCondId5771MMSOverCapacity_ObjectIdentity = ObjectIdentity
lgpCondId5771MMSOverCapacity = _LgpCondId5771MMSOverCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5771)
)
if mibBuilder.loadTexts:
    lgpCondId5771MMSOverCapacity.setStatus("current")
_LgpCondId5773CompressorCapacityNormal_ObjectIdentity = ObjectIdentity
lgpCondId5773CompressorCapacityNormal = _LgpCondId5773CompressorCapacityNormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5773)
)
if mibBuilder.loadTexts:
    lgpCondId5773CompressorCapacityNormal.setStatus("current")
_LgpCondId5774CompressorContactorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5774CompressorContactorIssue = _LgpCondId5774CompressorContactorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5774)
)
if mibBuilder.loadTexts:
    lgpCondId5774CompressorContactorIssue.setStatus("current")
_LgpCondId5775UnitShutdownUnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId5775UnitShutdownUnspecifiedGeneralEvent = _LgpCondId5775UnitShutdownUnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5775)
)
if mibBuilder.loadTexts:
    lgpCondId5775UnitShutdownUnspecifiedGeneralEvent.setStatus("current")
_LgpCondId5776PDULowVoltageLN_ObjectIdentity = ObjectIdentity
lgpCondId5776PDULowVoltageLN = _LgpCondId5776PDULowVoltageLN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5776)
)
if mibBuilder.loadTexts:
    lgpCondId5776PDULowVoltageLN.setStatus("current")
_LgpCondId5777PDULowVoltageLL_ObjectIdentity = ObjectIdentity
lgpCondId5777PDULowVoltageLL = _LgpCondId5777PDULowVoltageLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5777)
)
if mibBuilder.loadTexts:
    lgpCondId5777PDULowVoltageLL.setStatus("current")
_LgpCondId5778PDULowVoltageL1L2_ObjectIdentity = ObjectIdentity
lgpCondId5778PDULowVoltageL1L2 = _LgpCondId5778PDULowVoltageL1L2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5778)
)
if mibBuilder.loadTexts:
    lgpCondId5778PDULowVoltageL1L2.setStatus("current")
_LgpCondId5779PDULowVoltageL2L3_ObjectIdentity = ObjectIdentity
lgpCondId5779PDULowVoltageL2L3 = _LgpCondId5779PDULowVoltageL2L3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5779)
)
if mibBuilder.loadTexts:
    lgpCondId5779PDULowVoltageL2L3.setStatus("current")
_LgpCondId5780PDULowVoltageL3L1_ObjectIdentity = ObjectIdentity
lgpCondId5780PDULowVoltageL3L1 = _LgpCondId5780PDULowVoltageL3L1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5780)
)
if mibBuilder.loadTexts:
    lgpCondId5780PDULowVoltageL3L1.setStatus("current")
_LgpCondId5781PDULowVoltageL1N_ObjectIdentity = ObjectIdentity
lgpCondId5781PDULowVoltageL1N = _LgpCondId5781PDULowVoltageL1N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5781)
)
if mibBuilder.loadTexts:
    lgpCondId5781PDULowVoltageL1N.setStatus("current")
_LgpCondId5782PDULowVoltageL2N_ObjectIdentity = ObjectIdentity
lgpCondId5782PDULowVoltageL2N = _LgpCondId5782PDULowVoltageL2N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5782)
)
if mibBuilder.loadTexts:
    lgpCondId5782PDULowVoltageL2N.setStatus("current")
_LgpCondId5783PDULowVoltageL3N_ObjectIdentity = ObjectIdentity
lgpCondId5783PDULowVoltageL3N = _LgpCondId5783PDULowVoltageL3N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5783)
)
if mibBuilder.loadTexts:
    lgpCondId5783PDULowVoltageL3N.setStatus("current")
_LgpCondId5784BranchLowVoltageLN_ObjectIdentity = ObjectIdentity
lgpCondId5784BranchLowVoltageLN = _LgpCondId5784BranchLowVoltageLN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5784)
)
if mibBuilder.loadTexts:
    lgpCondId5784BranchLowVoltageLN.setStatus("current")
_LgpCondId5785BranchLowVoltageLL_ObjectIdentity = ObjectIdentity
lgpCondId5785BranchLowVoltageLL = _LgpCondId5785BranchLowVoltageLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5785)
)
if mibBuilder.loadTexts:
    lgpCondId5785BranchLowVoltageLL.setStatus("current")
_LgpCondId5786BranchLowVoltage_ObjectIdentity = ObjectIdentity
lgpCondId5786BranchLowVoltage = _LgpCondId5786BranchLowVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5786)
)
if mibBuilder.loadTexts:
    lgpCondId5786BranchLowVoltage.setStatus("current")
_LgpCondId5788ContTieActive_ObjectIdentity = ObjectIdentity
lgpCondId5788ContTieActive = _LgpCondId5788ContTieActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5788)
)
if mibBuilder.loadTexts:
    lgpCondId5788ContTieActive.setStatus("current")
_LgpCondId5792UserkWhReset_ObjectIdentity = ObjectIdentity
lgpCondId5792UserkWhReset = _LgpCondId5792UserkWhReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5792)
)
if mibBuilder.loadTexts:
    lgpCondId5792UserkWhReset.setStatus("current")
_LgpCondId5796PeakkWReset_ObjectIdentity = ObjectIdentity
lgpCondId5796PeakkWReset = _LgpCondId5796PeakkWReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5796)
)
if mibBuilder.loadTexts:
    lgpCondId5796PeakkWReset.setStatus("current")
_LgpCondId5798BypassOverload_ObjectIdentity = ObjectIdentity
lgpCondId5798BypassOverload = _LgpCondId5798BypassOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5798)
)
if mibBuilder.loadTexts:
    lgpCondId5798BypassOverload.setStatus("current")
_LgpCondId5801LowBatteryShutdownImminent_ObjectIdentity = ObjectIdentity
lgpCondId5801LowBatteryShutdownImminent = _LgpCondId5801LowBatteryShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5801)
)
if mibBuilder.loadTexts:
    lgpCondId5801LowBatteryShutdownImminent.setStatus("current")
_LgpCondId5806OutputOverload_ObjectIdentity = ObjectIdentity
lgpCondId5806OutputOverload = _LgpCondId5806OutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5806)
)
if mibBuilder.loadTexts:
    lgpCondId5806OutputOverload.setStatus("current")
_LgpCondId5807OutputOffPending_ObjectIdentity = ObjectIdentity
lgpCondId5807OutputOffPending = _LgpCondId5807OutputOffPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5807)
)
if mibBuilder.loadTexts:
    lgpCondId5807OutputOffPending.setStatus("current")
_LgpCondId5808SystemShutdownOutputShort_ObjectIdentity = ObjectIdentity
lgpCondId5808SystemShutdownOutputShort = _LgpCondId5808SystemShutdownOutputShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5808)
)
if mibBuilder.loadTexts:
    lgpCondId5808SystemShutdownOutputShort.setStatus("current")
_LgpCondId5809SystemShutdownLowBattery_ObjectIdentity = ObjectIdentity
lgpCondId5809SystemShutdownLowBattery = _LgpCondId5809SystemShutdownLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5809)
)
if mibBuilder.loadTexts:
    lgpCondId5809SystemShutdownLowBattery.setStatus("current")
_LgpCondId5810SystemShutdownRemoteShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5810SystemShutdownRemoteShutdown = _LgpCondId5810SystemShutdownRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5810)
)
if mibBuilder.loadTexts:
    lgpCondId5810SystemShutdownRemoteShutdown.setStatus("current")
_LgpCondId5811SystemShutdownHardwareFault_ObjectIdentity = ObjectIdentity
lgpCondId5811SystemShutdownHardwareFault = _LgpCondId5811SystemShutdownHardwareFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5811)
)
if mibBuilder.loadTexts:
    lgpCondId5811SystemShutdownHardwareFault.setStatus("current")
_LgpCondId5817LossofRedundancy_ObjectIdentity = ObjectIdentity
lgpCondId5817LossofRedundancy = _LgpCondId5817LossofRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5817)
)
if mibBuilder.loadTexts:
    lgpCondId5817LossofRedundancy.setStatus("current")
_LgpCondId5818PowerModuleFailure_ObjectIdentity = ObjectIdentity
lgpCondId5818PowerModuleFailure = _LgpCondId5818PowerModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5818)
)
if mibBuilder.loadTexts:
    lgpCondId5818PowerModuleFailure.setStatus("current")
_LgpCondId5819PowerModuleWarning_ObjectIdentity = ObjectIdentity
lgpCondId5819PowerModuleWarning = _LgpCondId5819PowerModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5819)
)
if mibBuilder.loadTexts:
    lgpCondId5819PowerModuleWarning.setStatus("current")
_LgpCondId5838PowerModuleFanFault_ObjectIdentity = ObjectIdentity
lgpCondId5838PowerModuleFanFault = _LgpCondId5838PowerModuleFanFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5838)
)
if mibBuilder.loadTexts:
    lgpCondId5838PowerModuleFanFault.setStatus("current")
_LgpCondId5839PowerModuleOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5839PowerModuleOverTemperature = _LgpCondId5839PowerModuleOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5839)
)
if mibBuilder.loadTexts:
    lgpCondId5839PowerModuleOverTemperature.setStatus("current")
_LgpCondId5840PowerModuleShutdownOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5840PowerModuleShutdownOverTemperature = _LgpCondId5840PowerModuleShutdownOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5840)
)
if mibBuilder.loadTexts:
    lgpCondId5840PowerModuleShutdownOverTemperature.setStatus("current")
_LgpCondId5842ChargerModuleFanFault_ObjectIdentity = ObjectIdentity
lgpCondId5842ChargerModuleFanFault = _LgpCondId5842ChargerModuleFanFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5842)
)
if mibBuilder.loadTexts:
    lgpCondId5842ChargerModuleFanFault.setStatus("current")
_LgpCondId5847BatteryModuleTemperatureSensorFault_ObjectIdentity = ObjectIdentity
lgpCondId5847BatteryModuleTemperatureSensorFault = _LgpCondId5847BatteryModuleTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5847)
)
if mibBuilder.loadTexts:
    lgpCondId5847BatteryModuleTemperatureSensorFault.setStatus("current")
_LgpCondId5848BatteryModuleOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5848BatteryModuleOverTemperature = _LgpCondId5848BatteryModuleOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5848)
)
if mibBuilder.loadTexts:
    lgpCondId5848BatteryModuleOverTemperature.setStatus("current")
_LgpCondId5849ReplaceBatteryModule_ObjectIdentity = ObjectIdentity
lgpCondId5849ReplaceBatteryModule = _LgpCondId5849ReplaceBatteryModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5849)
)
if mibBuilder.loadTexts:
    lgpCondId5849ReplaceBatteryModule.setStatus("current")
_LgpCondId5850SystemShutdownTransformerOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5850SystemShutdownTransformerOverTemperature = _LgpCondId5850SystemShutdownTransformerOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5850)
)
if mibBuilder.loadTexts:
    lgpCondId5850SystemShutdownTransformerOverTemperature.setStatus("current")
_LgpCondId5851MaximumLoadAlarm_ObjectIdentity = ObjectIdentity
lgpCondId5851MaximumLoadAlarm = _LgpCondId5851MaximumLoadAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5851)
)
if mibBuilder.loadTexts:
    lgpCondId5851MaximumLoadAlarm.setStatus("current")
_LgpCondId5856BatteryModuleFault_ObjectIdentity = ObjectIdentity
lgpCondId5856BatteryModuleFault = _LgpCondId5856BatteryModuleFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5856)
)
if mibBuilder.loadTexts:
    lgpCondId5856BatteryModuleFault.setStatus("current")
_LgpCondId5857BatteryModuleWarning_ObjectIdentity = ObjectIdentity
lgpCondId5857BatteryModuleWarning = _LgpCondId5857BatteryModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5857)
)
if mibBuilder.loadTexts:
    lgpCondId5857BatteryModuleWarning.setStatus("current")
_LgpCondId5862CheckAirFilter_ObjectIdentity = ObjectIdentity
lgpCondId5862CheckAirFilter = _LgpCondId5862CheckAirFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5862)
)
if mibBuilder.loadTexts:
    lgpCondId5862CheckAirFilter.setStatus("current")
_LgpCondId5863TransformerFanFault_ObjectIdentity = ObjectIdentity
lgpCondId5863TransformerFanFault = _LgpCondId5863TransformerFanFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5863)
)
if mibBuilder.loadTexts:
    lgpCondId5863TransformerFanFault.setStatus("current")
_LgpCondId5865NoLoadWarning_ObjectIdentity = ObjectIdentity
lgpCondId5865NoLoadWarning = _LgpCondId5865NoLoadWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5865)
)
if mibBuilder.loadTexts:
    lgpCondId5865NoLoadWarning.setStatus("current")
_LgpCondId5871BatteryOverTemperatureLimit_ObjectIdentity = ObjectIdentity
lgpCondId5871BatteryOverTemperatureLimit = _LgpCondId5871BatteryOverTemperatureLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5871)
)
if mibBuilder.loadTexts:
    lgpCondId5871BatteryOverTemperatureLimit.setStatus("current")
_LgpCondId5873UnexpectedMainBatteryDisconnectClosure_ObjectIdentity = ObjectIdentity
lgpCondId5873UnexpectedMainBatteryDisconnectClosure = _LgpCondId5873UnexpectedMainBatteryDisconnectClosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5873)
)
if mibBuilder.loadTexts:
    lgpCondId5873UnexpectedMainBatteryDisconnectClosure.setStatus("current")
_LgpCondId5874BatteryOverVoltage_ObjectIdentity = ObjectIdentity
lgpCondId5874BatteryOverVoltage = _LgpCondId5874BatteryOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5874)
)
if mibBuilder.loadTexts:
    lgpCondId5874BatteryOverVoltage.setStatus("current")
_LgpCondId5875BatteryFuseFault_ObjectIdentity = ObjectIdentity
lgpCondId5875BatteryFuseFault = _LgpCondId5875BatteryFuseFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5875)
)
if mibBuilder.loadTexts:
    lgpCondId5875BatteryFuseFault.setStatus("current")
_LgpCondId5878MainBatteryDisconnectForcedToUnlock_ObjectIdentity = ObjectIdentity
lgpCondId5878MainBatteryDisconnectForcedToUnlock = _LgpCondId5878MainBatteryDisconnectForcedToUnlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5878)
)
if mibBuilder.loadTexts:
    lgpCondId5878MainBatteryDisconnectForcedToUnlock.setStatus("current")
_LgpCondId5879VdcBackfeed_ObjectIdentity = ObjectIdentity
lgpCondId5879VdcBackfeed = _LgpCondId5879VdcBackfeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5879)
)
if mibBuilder.loadTexts:
    lgpCondId5879VdcBackfeed.setStatus("current")
_LgpCondId5880RectifierConfigurationChangeRequest_ObjectIdentity = ObjectIdentity
lgpCondId5880RectifierConfigurationChangeRequest = _LgpCondId5880RectifierConfigurationChangeRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5880)
)
if mibBuilder.loadTexts:
    lgpCondId5880RectifierConfigurationChangeRequest.setStatus("current")
_LgpCondId5881RegenerationActive_ObjectIdentity = ObjectIdentity
lgpCondId5881RegenerationActive = _LgpCondId5881RegenerationActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5881)
)
if mibBuilder.loadTexts:
    lgpCondId5881RegenerationActive.setStatus("current")
_LgpCondId5882RegenerationOperationTerminated_ObjectIdentity = ObjectIdentity
lgpCondId5882RegenerationOperationTerminated = _LgpCondId5882RegenerationOperationTerminated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5882)
)
if mibBuilder.loadTexts:
    lgpCondId5882RegenerationOperationTerminated.setStatus("current")
_LgpCondId5883RegenerationOperationFailure_ObjectIdentity = ObjectIdentity
lgpCondId5883RegenerationOperationFailure = _LgpCondId5883RegenerationOperationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5883)
)
if mibBuilder.loadTexts:
    lgpCondId5883RegenerationOperationFailure.setStatus("current")
_LgpCondId5884ProgramInputContact01_ObjectIdentity = ObjectIdentity
lgpCondId5884ProgramInputContact01 = _LgpCondId5884ProgramInputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5884)
)
if mibBuilder.loadTexts:
    lgpCondId5884ProgramInputContact01.setStatus("current")
_LgpCondId5885ProgramInputContact02_ObjectIdentity = ObjectIdentity
lgpCondId5885ProgramInputContact02 = _LgpCondId5885ProgramInputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5885)
)
if mibBuilder.loadTexts:
    lgpCondId5885ProgramInputContact02.setStatus("current")
_LgpCondId5886ProgramInputContact03_ObjectIdentity = ObjectIdentity
lgpCondId5886ProgramInputContact03 = _LgpCondId5886ProgramInputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5886)
)
if mibBuilder.loadTexts:
    lgpCondId5886ProgramInputContact03.setStatus("current")
_LgpCondId5887ProgramInputContact04_ObjectIdentity = ObjectIdentity
lgpCondId5887ProgramInputContact04 = _LgpCondId5887ProgramInputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5887)
)
if mibBuilder.loadTexts:
    lgpCondId5887ProgramInputContact04.setStatus("current")
_LgpCondId5888ProgramInputContact05_ObjectIdentity = ObjectIdentity
lgpCondId5888ProgramInputContact05 = _LgpCondId5888ProgramInputContact05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5888)
)
if mibBuilder.loadTexts:
    lgpCondId5888ProgramInputContact05.setStatus("current")
_LgpCondId5889ProgramInputContact06_ObjectIdentity = ObjectIdentity
lgpCondId5889ProgramInputContact06 = _LgpCondId5889ProgramInputContact06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5889)
)
if mibBuilder.loadTexts:
    lgpCondId5889ProgramInputContact06.setStatus("current")
_LgpCondId5890ProgramInputContact07_ObjectIdentity = ObjectIdentity
lgpCondId5890ProgramInputContact07 = _LgpCondId5890ProgramInputContact07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5890)
)
if mibBuilder.loadTexts:
    lgpCondId5890ProgramInputContact07.setStatus("current")
_LgpCondId5891ProgramInputContact08_ObjectIdentity = ObjectIdentity
lgpCondId5891ProgramInputContact08 = _LgpCondId5891ProgramInputContact08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5891)
)
if mibBuilder.loadTexts:
    lgpCondId5891ProgramInputContact08.setStatus("current")
_LgpCondId5892ProgramInputContact09_ObjectIdentity = ObjectIdentity
lgpCondId5892ProgramInputContact09 = _LgpCondId5892ProgramInputContact09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5892)
)
if mibBuilder.loadTexts:
    lgpCondId5892ProgramInputContact09.setStatus("current")
_LgpCondId5893ProgramInputContact10_ObjectIdentity = ObjectIdentity
lgpCondId5893ProgramInputContact10 = _LgpCondId5893ProgramInputContact10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5893)
)
if mibBuilder.loadTexts:
    lgpCondId5893ProgramInputContact10.setStatus("current")
_LgpCondId5894ProgramInputContact11_ObjectIdentity = ObjectIdentity
lgpCondId5894ProgramInputContact11 = _LgpCondId5894ProgramInputContact11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5894)
)
if mibBuilder.loadTexts:
    lgpCondId5894ProgramInputContact11.setStatus("current")
_LgpCondId5895ProgramInputContact12_ObjectIdentity = ObjectIdentity
lgpCondId5895ProgramInputContact12 = _LgpCondId5895ProgramInputContact12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5895)
)
if mibBuilder.loadTexts:
    lgpCondId5895ProgramInputContact12.setStatus("current")
_LgpCondId5896GroundFaultDetected_ObjectIdentity = ObjectIdentity
lgpCondId5896GroundFaultDetected = _LgpCondId5896GroundFaultDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5896)
)
if mibBuilder.loadTexts:
    lgpCondId5896GroundFaultDetected.setStatus("current")
_LgpCondId5902ReturnHumiditySensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5902ReturnHumiditySensorIssue = _LgpCondId5902ReturnHumiditySensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5902)
)
if mibBuilder.loadTexts:
    lgpCondId5902ReturnHumiditySensorIssue.setStatus("current")
_LgpCondId5903CompressorLowDifferentialPressureLockout_ObjectIdentity = ObjectIdentity
lgpCondId5903CompressorLowDifferentialPressureLockout = _LgpCondId5903CompressorLowDifferentialPressureLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5903)
)
if mibBuilder.loadTexts:
    lgpCondId5903CompressorLowDifferentialPressureLockout.setStatus("current")
_LgpCondId5906AirflowSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5906AirflowSensorIssue = _LgpCondId5906AirflowSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5906)
)
if mibBuilder.loadTexts:
    lgpCondId5906AirflowSensorIssue.setStatus("current")
_LgpCondId5907ExtAirDamperPositionIssue_ObjectIdentity = ObjectIdentity
lgpCondId5907ExtAirDamperPositionIssue = _LgpCondId5907ExtAirDamperPositionIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5907)
)
if mibBuilder.loadTexts:
    lgpCondId5907ExtAirDamperPositionIssue.setStatus("current")
_LgpCondId5908ExtPowerSourceAFailure_ObjectIdentity = ObjectIdentity
lgpCondId5908ExtPowerSourceAFailure = _LgpCondId5908ExtPowerSourceAFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5908)
)
if mibBuilder.loadTexts:
    lgpCondId5908ExtPowerSourceAFailure.setStatus("current")
_LgpCondId5909ExtPowerSourceBFailure_ObjectIdentity = ObjectIdentity
lgpCondId5909ExtPowerSourceBFailure = _LgpCondId5909ExtPowerSourceBFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5909)
)
if mibBuilder.loadTexts:
    lgpCondId5909ExtPowerSourceBFailure.setStatus("current")
_LgpCondId5910StaticPressureSensorOutofRange_ObjectIdentity = ObjectIdentity
lgpCondId5910StaticPressureSensorOutofRange = _LgpCondId5910StaticPressureSensorOutofRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5910)
)
if mibBuilder.loadTexts:
    lgpCondId5910StaticPressureSensorOutofRange.setStatus("current")
_LgpCondId5911FluidTemperatureSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5911FluidTemperatureSensorIssue = _LgpCondId5911FluidTemperatureSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5911)
)
if mibBuilder.loadTexts:
    lgpCondId5911FluidTemperatureSensorIssue.setStatus("current")
_LgpCondId5912FluidFlowSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5912FluidFlowSensorIssue = _LgpCondId5912FluidFlowSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5912)
)
if mibBuilder.loadTexts:
    lgpCondId5912FluidFlowSensorIssue.setStatus("current")
_LgpCondId5914OverDifferentialPressure_ObjectIdentity = ObjectIdentity
lgpCondId5914OverDifferentialPressure = _LgpCondId5914OverDifferentialPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5914)
)
if mibBuilder.loadTexts:
    lgpCondId5914OverDifferentialPressure.setStatus("current")
_LgpCondId5915UnderDifferentialPressure_ObjectIdentity = ObjectIdentity
lgpCondId5915UnderDifferentialPressure = _LgpCondId5915UnderDifferentialPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5915)
)
if mibBuilder.loadTexts:
    lgpCondId5915UnderDifferentialPressure.setStatus("current")
_LgpCondId5924MixedModeLockout_ObjectIdentity = ObjectIdentity
lgpCondId5924MixedModeLockout = _LgpCondId5924MixedModeLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5924)
)
if mibBuilder.loadTexts:
    lgpCondId5924MixedModeLockout.setStatus("current")
_LgpCondId5928UnbalancedLoadCondition_ObjectIdentity = ObjectIdentity
lgpCondId5928UnbalancedLoadCondition = _LgpCondId5928UnbalancedLoadCondition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5928)
)
if mibBuilder.loadTexts:
    lgpCondId5928UnbalancedLoadCondition.setStatus("current")
_LgpCondId5939BranchOverCurrentProtection_ObjectIdentity = ObjectIdentity
lgpCondId5939BranchOverCurrentProtection = _LgpCondId5939BranchOverCurrentProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5939)
)
if mibBuilder.loadTexts:
    lgpCondId5939BranchOverCurrentProtection.setStatus("current")
_LgpCondId5948BranchLowVoltageLL_ObjectIdentity = ObjectIdentity
lgpCondId5948BranchLowVoltageLL = _LgpCondId5948BranchLowVoltageLL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5948)
)
if mibBuilder.loadTexts:
    lgpCondId5948BranchLowVoltageLL.setStatus("current")
_LgpCondId5957BypassInputVoltageFault_ObjectIdentity = ObjectIdentity
lgpCondId5957BypassInputVoltageFault = _LgpCondId5957BypassInputVoltageFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5957)
)
if mibBuilder.loadTexts:
    lgpCondId5957BypassInputVoltageFault.setStatus("current")
_LgpCondId5958BatteryTemperatureOutofRange_ObjectIdentity = ObjectIdentity
lgpCondId5958BatteryTemperatureOutofRange = _LgpCondId5958BatteryTemperatureOutofRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5958)
)
if mibBuilder.loadTexts:
    lgpCondId5958BatteryTemperatureOutofRange.setStatus("current")
_LgpCondId5960InverterOverload_ObjectIdentity = ObjectIdentity
lgpCondId5960InverterOverload = _LgpCondId5960InverterOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5960)
)
if mibBuilder.loadTexts:
    lgpCondId5960InverterOverload.setStatus("current")
_LgpCondId5966AuxAirTempDeviceCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5966AuxAirTempDeviceCommunicationLost = _LgpCondId5966AuxAirTempDeviceCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5966)
)
if mibBuilder.loadTexts:
    lgpCondId5966AuxAirTempDeviceCommunicationLost.setStatus("current")
_LgpCondId5967ModbusPowerMeterCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5967ModbusPowerMeterCommunicationLost = _LgpCondId5967ModbusPowerMeterCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5967)
)
if mibBuilder.loadTexts:
    lgpCondId5967ModbusPowerMeterCommunicationLost.setStatus("current")
_LgpCondId5968InverterDesaturation_ObjectIdentity = ObjectIdentity
lgpCondId5968InverterDesaturation = _LgpCondId5968InverterDesaturation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5968)
)
if mibBuilder.loadTexts:
    lgpCondId5968InverterDesaturation.setStatus("current")
_LgpCondId5969GenericDICFault_ObjectIdentity = ObjectIdentity
lgpCondId5969GenericDICFault = _LgpCondId5969GenericDICFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5969)
)
if mibBuilder.loadTexts:
    lgpCondId5969GenericDICFault.setStatus("current")
_LgpCondId5970GroundFault_ObjectIdentity = ObjectIdentity
lgpCondId5970GroundFault = _LgpCondId5970GroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5970)
)
if mibBuilder.loadTexts:
    lgpCondId5970GroundFault.setStatus("current")
_LgpCondId5973InputBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId5973InputBreakerOpen = _LgpCondId5973InputBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5973)
)
if mibBuilder.loadTexts:
    lgpCondId5973InputBreakerOpen.setStatus("current")
_LgpCondId5974NeutralBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId5974NeutralBreakerOpen = _LgpCondId5974NeutralBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5974)
)
if mibBuilder.loadTexts:
    lgpCondId5974NeutralBreakerOpen.setStatus("current")
_LgpCondId5975OutputBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId5975OutputBreakerOpen = _LgpCondId5975OutputBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5975)
)
if mibBuilder.loadTexts:
    lgpCondId5975OutputBreakerOpen.setStatus("current")
_LgpCondId5976MaintenanceBypassBreakerClosed_ObjectIdentity = ObjectIdentity
lgpCondId5976MaintenanceBypassBreakerClosed = _LgpCondId5976MaintenanceBypassBreakerClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5976)
)
if mibBuilder.loadTexts:
    lgpCondId5976MaintenanceBypassBreakerClosed.setStatus("current")
_LgpCondId5977BatteryBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId5977BatteryBreakerOpen = _LgpCondId5977BatteryBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5977)
)
if mibBuilder.loadTexts:
    lgpCondId5977BatteryBreakerOpen.setStatus("current")
_LgpCondId5978RectifierIsolationBreakerRFBOpen_ObjectIdentity = ObjectIdentity
lgpCondId5978RectifierIsolationBreakerRFBOpen = _LgpCondId5978RectifierIsolationBreakerRFBOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5978)
)
if mibBuilder.loadTexts:
    lgpCondId5978RectifierIsolationBreakerRFBOpen.setStatus("current")
_LgpCondId5982BypassBreakerSBBOpen_ObjectIdentity = ObjectIdentity
lgpCondId5982BypassBreakerSBBOpen = _LgpCondId5982BypassBreakerSBBOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5982)
)
if mibBuilder.loadTexts:
    lgpCondId5982BypassBreakerSBBOpen.setStatus("current")
_LgpCondId5983BypassIsolationBreakerBIBOpen_ObjectIdentity = ObjectIdentity
lgpCondId5983BypassIsolationBreakerBIBOpen = _LgpCondId5983BypassIsolationBreakerBIBOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5983)
)
if mibBuilder.loadTexts:
    lgpCondId5983BypassIsolationBreakerBIBOpen.setStatus("current")
_LgpCondId5984BypassUndervoltageWarning_ObjectIdentity = ObjectIdentity
lgpCondId5984BypassUndervoltageWarning = _LgpCondId5984BypassUndervoltageWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5984)
)
if mibBuilder.loadTexts:
    lgpCondId5984BypassUndervoltageWarning.setStatus("current")
_LgpCondId5985BypassStaticSwitchBPSSOn_ObjectIdentity = ObjectIdentity
lgpCondId5985BypassStaticSwitchBPSSOn = _LgpCondId5985BypassStaticSwitchBPSSOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5985)
)
if mibBuilder.loadTexts:
    lgpCondId5985BypassStaticSwitchBPSSOn.setStatus("current")
_LgpCondId5998BattOvtempWarning_ObjectIdentity = ObjectIdentity
lgpCondId5998BattOvtempWarning = _LgpCondId5998BattOvtempWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5998)
)
if mibBuilder.loadTexts:
    lgpCondId5998BattOvtempWarning.setStatus("current")
_LgpCondId6009InverterOutputBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId6009InverterOutputBreakerOpen = _LgpCondId6009InverterOutputBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6009)
)
if mibBuilder.loadTexts:
    lgpCondId6009InverterOutputBreakerOpen.setStatus("current")
_LgpCondId6011EquipmentOverTempWarning_ObjectIdentity = ObjectIdentity
lgpCondId6011EquipmentOverTempWarning = _LgpCondId6011EquipmentOverTempWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6011)
)
if mibBuilder.loadTexts:
    lgpCondId6011EquipmentOverTempWarning.setStatus("current")
_LgpCondId6012EquipmentOvertemperatureLimit_ObjectIdentity = ObjectIdentity
lgpCondId6012EquipmentOvertemperatureLimit = _LgpCondId6012EquipmentOvertemperatureLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6012)
)
if mibBuilder.loadTexts:
    lgpCondId6012EquipmentOvertemperatureLimit.setStatus("current")
_LgpCondId6045RectifierInputBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId6045RectifierInputBreakerOpen = _LgpCondId6045RectifierInputBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6045)
)
if mibBuilder.loadTexts:
    lgpCondId6045RectifierInputBreakerOpen.setStatus("current")
_LgpCondId6046LoadonUPS_ObjectIdentity = ObjectIdentity
lgpCondId6046LoadonUPS = _LgpCondId6046LoadonUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6046)
)
if mibBuilder.loadTexts:
    lgpCondId6046LoadonUPS.setStatus("current")
_LgpCondId6047Core2CoreFuseFailure_ObjectIdentity = ObjectIdentity
lgpCondId6047Core2CoreFuseFailure = _LgpCondId6047Core2CoreFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6047)
)
if mibBuilder.loadTexts:
    lgpCondId6047Core2CoreFuseFailure.setStatus("current")
_LgpCondId6052SystemOutputBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId6052SystemOutputBreakerOpen = _LgpCondId6052SystemOutputBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6052)
)
if mibBuilder.loadTexts:
    lgpCondId6052SystemOutputBreakerOpen.setStatus("current")
_LgpCondId6059InverterRelayFault_ObjectIdentity = ObjectIdentity
lgpCondId6059InverterRelayFault = _LgpCondId6059InverterRelayFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6059)
)
if mibBuilder.loadTexts:
    lgpCondId6059InverterRelayFault.setStatus("current")
_LgpCondId6060TransfertoBypassSystemOverload_ObjectIdentity = ObjectIdentity
lgpCondId6060TransfertoBypassSystemOverload = _LgpCondId6060TransfertoBypassSystemOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6060)
)
if mibBuilder.loadTexts:
    lgpCondId6060TransfertoBypassSystemOverload.setStatus("current")
_LgpCondId6061InputSourceBackfeed_ObjectIdentity = ObjectIdentity
lgpCondId6061InputSourceBackfeed = _LgpCondId6061InputSourceBackfeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6061)
)
if mibBuilder.loadTexts:
    lgpCondId6061InputSourceBackfeed.setStatus("current")
_LgpCondId6062LossofSynchronization_ObjectIdentity = ObjectIdentity
lgpCondId6062LossofSynchronization = _LgpCondId6062LossofSynchronization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6062)
)
if mibBuilder.loadTexts:
    lgpCondId6062LossofSynchronization.setStatus("current")
_LgpCondId6063BatteryConverterCurrentLimit_ObjectIdentity = ObjectIdentity
lgpCondId6063BatteryConverterCurrentLimit = _LgpCondId6063BatteryConverterCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6063)
)
if mibBuilder.loadTexts:
    lgpCondId6063BatteryConverterCurrentLimit.setStatus("current")
_LgpCondId6064LBSCableFailure_ObjectIdentity = ObjectIdentity
lgpCondId6064LBSCableFailure = _LgpCondId6064LBSCableFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6064)
)
if mibBuilder.loadTexts:
    lgpCondId6064LBSCableFailure.setStatus("current")
_LgpCondId6065BatteryChargeEqualizationTimeout_ObjectIdentity = ObjectIdentity
lgpCondId6065BatteryChargeEqualizationTimeout = _LgpCondId6065BatteryChargeEqualizationTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6065)
)
if mibBuilder.loadTexts:
    lgpCondId6065BatteryChargeEqualizationTimeout.setStatus("current")
_LgpCondId6066ParallelCableFailure_ObjectIdentity = ObjectIdentity
lgpCondId6066ParallelCableFailure = _LgpCondId6066ParallelCableFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6066)
)
if mibBuilder.loadTexts:
    lgpCondId6066ParallelCableFailure.setStatus("current")
_LgpCondId6067BatteryFault_ObjectIdentity = ObjectIdentity
lgpCondId6067BatteryFault = _LgpCondId6067BatteryFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6067)
)
if mibBuilder.loadTexts:
    lgpCondId6067BatteryFault.setStatus("current")
_LgpCondId6068BatteryRoomAlarm_ObjectIdentity = ObjectIdentity
lgpCondId6068BatteryRoomAlarm = _LgpCondId6068BatteryRoomAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6068)
)
if mibBuilder.loadTexts:
    lgpCondId6068BatteryRoomAlarm.setStatus("current")
_LgpCondId6080UPSCCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpCondId6080UPSCCommunicationFailure = _LgpCondId6080UPSCCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6080)
)
if mibBuilder.loadTexts:
    lgpCondId6080UPSCCommunicationFailure.setStatus("current")
_LgpCondId6092Compressor1BThermalOverload_ObjectIdentity = ObjectIdentity
lgpCondId6092Compressor1BThermalOverload = _LgpCondId6092Compressor1BThermalOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6092)
)
if mibBuilder.loadTexts:
    lgpCondId6092Compressor1BThermalOverload.setStatus("current")
_LgpCondId6093Compressor2BThermalOverload_ObjectIdentity = ObjectIdentity
lgpCondId6093Compressor2BThermalOverload = _LgpCondId6093Compressor2BThermalOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6093)
)
if mibBuilder.loadTexts:
    lgpCondId6093Compressor2BThermalOverload.setStatus("current")
_LgpCondId6094Compressor1BHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId6094Compressor1BHoursExceeded = _LgpCondId6094Compressor1BHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6094)
)
if mibBuilder.loadTexts:
    lgpCondId6094Compressor1BHoursExceeded.setStatus("current")
_LgpCondId6095Compressor2BHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId6095Compressor2BHoursExceeded = _LgpCondId6095Compressor2BHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6095)
)
if mibBuilder.loadTexts:
    lgpCondId6095Compressor2BHoursExceeded.setStatus("current")
_LgpCondId6100CondenserRemoteShutdown_ObjectIdentity = ObjectIdentity
lgpCondId6100CondenserRemoteShutdown = _LgpCondId6100CondenserRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6100)
)
if mibBuilder.loadTexts:
    lgpCondId6100CondenserRemoteShutdown.setStatus("current")
_LgpCondId6105ExternalCondenserTVSSIssue_ObjectIdentity = ObjectIdentity
lgpCondId6105ExternalCondenserTVSSIssue = _LgpCondId6105ExternalCondenserTVSSIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6105)
)
if mibBuilder.loadTexts:
    lgpCondId6105ExternalCondenserTVSSIssue.setStatus("current")
_LgpCondId6106ExternalCondenserVFDIssue_ObjectIdentity = ObjectIdentity
lgpCondId6106ExternalCondenserVFDIssue = _LgpCondId6106ExternalCondenserVFDIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6106)
)
if mibBuilder.loadTexts:
    lgpCondId6106ExternalCondenserVFDIssue.setStatus("current")
_LgpCondId6107ExternalCondenserIssue_ObjectIdentity = ObjectIdentity
lgpCondId6107ExternalCondenserIssue = _LgpCondId6107ExternalCondenserIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6107)
)
if mibBuilder.loadTexts:
    lgpCondId6107ExternalCondenserIssue.setStatus("current")
_LgpCondId6119Slotsnotavailable_ObjectIdentity = ObjectIdentity
lgpCondId6119Slotsnotavailable = _LgpCondId6119Slotsnotavailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6119)
)
if mibBuilder.loadTexts:
    lgpCondId6119Slotsnotavailable.setStatus("current")
_LgpCondId6180BatteryUnderVoltage_ObjectIdentity = ObjectIdentity
lgpCondId6180BatteryUnderVoltage = _LgpCondId6180BatteryUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6180)
)
if mibBuilder.loadTexts:
    lgpCondId6180BatteryUnderVoltage.setStatus("current")
_LgpCondId6182ReplaceBattery_ObjectIdentity = ObjectIdentity
lgpCondId6182ReplaceBattery = _LgpCondId6182ReplaceBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6182)
)
if mibBuilder.loadTexts:
    lgpCondId6182ReplaceBattery.setStatus("current")
_LgpCondId6186InputFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpCondId6186InputFrequencyDeviation = _LgpCondId6186InputFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6186)
)
if mibBuilder.loadTexts:
    lgpCondId6186InputFrequencyDeviation.setStatus("current")
_LgpCondId6187ShutdownPending_ObjectIdentity = ObjectIdentity
lgpCondId6187ShutdownPending = _LgpCondId6187ShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6187)
)
if mibBuilder.loadTexts:
    lgpCondId6187ShutdownPending.setStatus("current")
_LgpCondId6194SystemRebootCommandIssued_ObjectIdentity = ObjectIdentity
lgpCondId6194SystemRebootCommandIssued = _LgpCondId6194SystemRebootCommandIssued_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6194)
)
if mibBuilder.loadTexts:
    lgpCondId6194SystemRebootCommandIssued.setStatus("current")
_LgpCondId6203SensorAdded_ObjectIdentity = ObjectIdentity
lgpCondId6203SensorAdded = _LgpCondId6203SensorAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6203)
)
if mibBuilder.loadTexts:
    lgpCondId6203SensorAdded.setStatus("current")
_LgpCondId6204SensorRemoved_ObjectIdentity = ObjectIdentity
lgpCondId6204SensorRemoved = _LgpCondId6204SensorRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6204)
)
if mibBuilder.loadTexts:
    lgpCondId6204SensorRemoved.setStatus("current")
_LgpCondId6205WaterLeakDetected_ObjectIdentity = ObjectIdentity
lgpCondId6205WaterLeakDetected = _LgpCondId6205WaterLeakDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6205)
)
if mibBuilder.loadTexts:
    lgpCondId6205WaterLeakDetected.setStatus("current")
_LgpCondId6210FirmwareUpdateInProgress_ObjectIdentity = ObjectIdentity
lgpCondId6210FirmwareUpdateInProgress = _LgpCondId6210FirmwareUpdateInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6210)
)
if mibBuilder.loadTexts:
    lgpCondId6210FirmwareUpdateInProgress.setStatus("current")
_LgpCondId6211FirmwareUpdateCompletedSuccessfully_ObjectIdentity = ObjectIdentity
lgpCondId6211FirmwareUpdateCompletedSuccessfully = _LgpCondId6211FirmwareUpdateCompletedSuccessfully_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6211)
)
if mibBuilder.loadTexts:
    lgpCondId6211FirmwareUpdateCompletedSuccessfully.setStatus("current")
_LgpCondId6212FirmwareUpdateCompletedUnsuccessfully_ObjectIdentity = ObjectIdentity
lgpCondId6212FirmwareUpdateCompletedUnsuccessfully = _LgpCondId6212FirmwareUpdateCompletedUnsuccessfully_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6212)
)
if mibBuilder.loadTexts:
    lgpCondId6212FirmwareUpdateCompletedUnsuccessfully.setStatus("current")
_LgpCondId6216PrechargeCircuitFailed_ObjectIdentity = ObjectIdentity
lgpCondId6216PrechargeCircuitFailed = _LgpCondId6216PrechargeCircuitFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6216)
)
if mibBuilder.loadTexts:
    lgpCondId6216PrechargeCircuitFailed.setStatus("current")
_LgpCondId6217MemoryCardRemoved_ObjectIdentity = ObjectIdentity
lgpCondId6217MemoryCardRemoved = _LgpCondId6217MemoryCardRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6217)
)
if mibBuilder.loadTexts:
    lgpCondId6217MemoryCardRemoved.setStatus("current")
_LgpCondId6218AutoCalibrationActive_ObjectIdentity = ObjectIdentity
lgpCondId6218AutoCalibrationActive = _LgpCondId6218AutoCalibrationActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6218)
)
if mibBuilder.loadTexts:
    lgpCondId6218AutoCalibrationActive.setStatus("current")
_LgpCondId6219AutoCalibrationFailed_ObjectIdentity = ObjectIdentity
lgpCondId6219AutoCalibrationFailed = _LgpCondId6219AutoCalibrationFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6219)
)
if mibBuilder.loadTexts:
    lgpCondId6219AutoCalibrationFailed.setStatus("current")
_LgpCondId6220ModuleOutputBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId6220ModuleOutputBreakerOpen = _LgpCondId6220ModuleOutputBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6220)
)
if mibBuilder.loadTexts:
    lgpCondId6220ModuleOutputBreakerOpen.setStatus("current")
_LgpCondId6221NeutralVoltageFault_ObjectIdentity = ObjectIdentity
lgpCondId6221NeutralVoltageFault = _LgpCondId6221NeutralVoltageFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6221)
)
if mibBuilder.loadTexts:
    lgpCondId6221NeutralVoltageFault.setStatus("current")
_LgpCondId6222BranchLoadLoss_ObjectIdentity = ObjectIdentity
lgpCondId6222BranchLoadLoss = _LgpCondId6222BranchLoadLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6222)
)
if mibBuilder.loadTexts:
    lgpCondId6222BranchLoadLoss.setStatus("current")
_LgpCondId6225RemoteSensorLowHumidity_ObjectIdentity = ObjectIdentity
lgpCondId6225RemoteSensorLowHumidity = _LgpCondId6225RemoteSensorLowHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6225)
)
if mibBuilder.loadTexts:
    lgpCondId6225RemoteSensorLowHumidity.setStatus("current")
_LgpCondId6226RemoteSensorHighHumidity_ObjectIdentity = ObjectIdentity
lgpCondId6226RemoteSensorHighHumidity = _LgpCondId6226RemoteSensorHighHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6226)
)
if mibBuilder.loadTexts:
    lgpCondId6226RemoteSensorHighHumidity.setStatus("current")
_LgpCondId6227RemoteSensorAverageLowHumidity_ObjectIdentity = ObjectIdentity
lgpCondId6227RemoteSensorAverageLowHumidity = _LgpCondId6227RemoteSensorAverageLowHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6227)
)
if mibBuilder.loadTexts:
    lgpCondId6227RemoteSensorAverageLowHumidity.setStatus("current")
_LgpCondId6228RemoteSensorAverageHighHumidity_ObjectIdentity = ObjectIdentity
lgpCondId6228RemoteSensorAverageHighHumidity = _LgpCondId6228RemoteSensorAverageHighHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6228)
)
if mibBuilder.loadTexts:
    lgpCondId6228RemoteSensorAverageHighHumidity.setStatus("current")
_LgpCondId6229RemoteSensorSystemAverageLowHumidity_ObjectIdentity = ObjectIdentity
lgpCondId6229RemoteSensorSystemAverageLowHumidity = _LgpCondId6229RemoteSensorSystemAverageLowHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6229)
)
if mibBuilder.loadTexts:
    lgpCondId6229RemoteSensorSystemAverageLowHumidity.setStatus("current")
_LgpCondId6230RemoteSensorSystemAverageHighHumidity_ObjectIdentity = ObjectIdentity
lgpCondId6230RemoteSensorSystemAverageHighHumidity = _LgpCondId6230RemoteSensorSystemAverageHighHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6230)
)
if mibBuilder.loadTexts:
    lgpCondId6230RemoteSensorSystemAverageHighHumidity.setStatus("current")
_LgpCondId6231LowCompressorSuperheat_ObjectIdentity = ObjectIdentity
lgpCondId6231LowCompressorSuperheat = _LgpCondId6231LowCompressorSuperheat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6231)
)
if mibBuilder.loadTexts:
    lgpCondId6231LowCompressorSuperheat.setStatus("current")
_LgpCondId6232SECUnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId6232SECUnspecifiedGeneralEvent = _LgpCondId6232SECUnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6232)
)
if mibBuilder.loadTexts:
    lgpCondId6232SECUnspecifiedGeneralEvent.setStatus("current")
_LgpCondId6233SECCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId6233SECCommunicationLost = _LgpCondId6233SECCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6233)
)
if mibBuilder.loadTexts:
    lgpCondId6233SECCommunicationLost.setStatus("current")
_LgpCondId6236PowerSourceAIssue_ObjectIdentity = ObjectIdentity
lgpCondId6236PowerSourceAIssue = _LgpCondId6236PowerSourceAIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6236)
)
if mibBuilder.loadTexts:
    lgpCondId6236PowerSourceAIssue.setStatus("current")
_LgpCondId6237PowerSourceBIssue_ObjectIdentity = ObjectIdentity
lgpCondId6237PowerSourceBIssue = _LgpCondId6237PowerSourceBIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6237)
)
if mibBuilder.loadTexts:
    lgpCondId6237PowerSourceBIssue.setStatus("current")
_LgpCondId6239FluidValveHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId6239FluidValveHoursExceeded = _LgpCondId6239FluidValveHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6239)
)
if mibBuilder.loadTexts:
    lgpCondId6239FluidValveHoursExceeded.setStatus("current")
_LgpCondId6253BoosterFailure_ObjectIdentity = ObjectIdentity
lgpCondId6253BoosterFailure = _LgpCondId6253BoosterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6253)
)
if mibBuilder.loadTexts:
    lgpCondId6253BoosterFailure.setStatus("current")
_LgpCondId6254ChargerFailure_ObjectIdentity = ObjectIdentity
lgpCondId6254ChargerFailure = _LgpCondId6254ChargerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6254)
)
if mibBuilder.loadTexts:
    lgpCondId6254ChargerFailure.setStatus("current")
_LgpCondId6274UnitTopReturnAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6274UnitTopReturnAirSensorFailure = _LgpCondId6274UnitTopReturnAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6274)
)
if mibBuilder.loadTexts:
    lgpCondId6274UnitTopReturnAirSensorFailure.setStatus("current")
_LgpCondId6275UnitMiddleReturnAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6275UnitMiddleReturnAirSensorFailure = _LgpCondId6275UnitMiddleReturnAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6275)
)
if mibBuilder.loadTexts:
    lgpCondId6275UnitMiddleReturnAirSensorFailure.setStatus("current")
_LgpCondId6276UnitBottomReturnAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6276UnitBottomReturnAirSensorFailure = _LgpCondId6276UnitBottomReturnAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6276)
)
if mibBuilder.loadTexts:
    lgpCondId6276UnitBottomReturnAirSensorFailure.setStatus("current")
_LgpCondId6277UnitTopSupplyAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6277UnitTopSupplyAirSensorFailure = _LgpCondId6277UnitTopSupplyAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6277)
)
if mibBuilder.loadTexts:
    lgpCondId6277UnitTopSupplyAirSensorFailure.setStatus("current")
_LgpCondId6278UnitMiddleFirstSupplyAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6278UnitMiddleFirstSupplyAirSensorFailure = _LgpCondId6278UnitMiddleFirstSupplyAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6278)
)
if mibBuilder.loadTexts:
    lgpCondId6278UnitMiddleFirstSupplyAirSensorFailure.setStatus("current")
_LgpCondId6279UnitBottomSupplyAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6279UnitBottomSupplyAirSensorFailure = _LgpCondId6279UnitBottomSupplyAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6279)
)
if mibBuilder.loadTexts:
    lgpCondId6279UnitBottomSupplyAirSensorFailure.setStatus("current")
_LgpCondId6284UnitMiddleSecondSupplyAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6284UnitMiddleSecondSupplyAirSensorFailure = _LgpCondId6284UnitMiddleSecondSupplyAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6284)
)
if mibBuilder.loadTexts:
    lgpCondId6284UnitMiddleSecondSupplyAirSensorFailure.setStatus("current")
_LgpCondId6293ChilledWaterControlActive_ObjectIdentity = ObjectIdentity
lgpCondId6293ChilledWaterControlActive = _LgpCondId6293ChilledWaterControlActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6293)
)
if mibBuilder.loadTexts:
    lgpCondId6293ChilledWaterControlActive.setStatus("current")
_LgpCondId6294ChilledWaterFlowTransducerFailure_ObjectIdentity = ObjectIdentity
lgpCondId6294ChilledWaterFlowTransducerFailure = _LgpCondId6294ChilledWaterFlowTransducerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6294)
)
if mibBuilder.loadTexts:
    lgpCondId6294ChilledWaterFlowTransducerFailure.setStatus("current")
_LgpCondId6295ChilledWaterInletTemperatureSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6295ChilledWaterInletTemperatureSensorFailure = _LgpCondId6295ChilledWaterInletTemperatureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6295)
)
if mibBuilder.loadTexts:
    lgpCondId6295ChilledWaterInletTemperatureSensorFailure.setStatus("current")
_LgpCondId6296ChilledWaterHighInletTemperature_ObjectIdentity = ObjectIdentity
lgpCondId6296ChilledWaterHighInletTemperature = _LgpCondId6296ChilledWaterHighInletTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6296)
)
if mibBuilder.loadTexts:
    lgpCondId6296ChilledWaterHighInletTemperature.setStatus("current")
_LgpCondId6297Modbus010VModuleCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpCondId6297Modbus010VModuleCommunicationFailure = _LgpCondId6297Modbus010VModuleCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6297)
)
if mibBuilder.loadTexts:
    lgpCondId6297Modbus010VModuleCommunicationFailure.setStatus("current")
_LgpCondId6299RackDoorsOpen_ObjectIdentity = ObjectIdentity
lgpCondId6299RackDoorsOpen = _LgpCondId6299RackDoorsOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6299)
)
if mibBuilder.loadTexts:
    lgpCondId6299RackDoorsOpen.setStatus("current")
_LgpCondId6303TeamStaticPressureSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6303TeamStaticPressureSensorFailure = _LgpCondId6303TeamStaticPressureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6303)
)
if mibBuilder.loadTexts:
    lgpCondId6303TeamStaticPressureSensorFailure.setStatus("current")
_LgpCondId6304HeatingLockout_ObjectIdentity = ObjectIdentity
lgpCondId6304HeatingLockout = _LgpCondId6304HeatingLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6304)
)
if mibBuilder.loadTexts:
    lgpCondId6304HeatingLockout.setStatus("current")
_LgpCondId6305FreeCoolingStoppedHighRoomTemp_ObjectIdentity = ObjectIdentity
lgpCondId6305FreeCoolingStoppedHighRoomTemp = _LgpCondId6305FreeCoolingStoppedHighRoomTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6305)
)
if mibBuilder.loadTexts:
    lgpCondId6305FreeCoolingStoppedHighRoomTemp.setStatus("current")
_LgpCondId6306ColdAisleTemperatureHumidityTeamSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6306ColdAisleTemperatureHumidityTeamSensorFailure = _LgpCondId6306ColdAisleTemperatureHumidityTeamSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6306)
)
if mibBuilder.loadTexts:
    lgpCondId6306ColdAisleTemperatureHumidityTeamSensorFailure.setStatus("current")
_LgpCondId6309ColdAisleAirSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6309ColdAisleAirSensorFailure = _LgpCondId6309ColdAisleAirSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6309)
)
if mibBuilder.loadTexts:
    lgpCondId6309ColdAisleAirSensorFailure.setStatus("current")
_LgpCondId6310ChilledWaterInletTemperatureControlActive_ObjectIdentity = ObjectIdentity
lgpCondId6310ChilledWaterInletTemperatureControlActive = _LgpCondId6310ChilledWaterInletTemperatureControlActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6310)
)
if mibBuilder.loadTexts:
    lgpCondId6310ChilledWaterInletTemperatureControlActive.setStatus("current")
_LgpCondId6313ChilledWaterInletTemperatureSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6313ChilledWaterInletTemperatureSensorFailure = _LgpCondId6313ChilledWaterInletTemperatureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6313)
)
if mibBuilder.loadTexts:
    lgpCondId6313ChilledWaterInletTemperatureSensorFailure.setStatus("current")
_LgpCondId6314ChilledWaterOutletTemperatureSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6314ChilledWaterOutletTemperatureSensorFailure = _LgpCondId6314ChilledWaterOutletTemperatureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6314)
)
if mibBuilder.loadTexts:
    lgpCondId6314ChilledWaterOutletTemperatureSensorFailure.setStatus("current")
_LgpCondId6315ChilledWaterFlowMeterSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6315ChilledWaterFlowMeterSensorFailure = _LgpCondId6315ChilledWaterFlowMeterSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6315)
)
if mibBuilder.loadTexts:
    lgpCondId6315ChilledWaterFlowMeterSensorFailure.setStatus("current")
_LgpCondId6333Bypassoutofsync_ObjectIdentity = ObjectIdentity
lgpCondId6333Bypassoutofsync = _LgpCondId6333Bypassoutofsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6333)
)
if mibBuilder.loadTexts:
    lgpCondId6333Bypassoutofsync.setStatus("current")
_LgpCondId6348SystemOutputoffasrequested_ObjectIdentity = ObjectIdentity
lgpCondId6348SystemOutputoffasrequested = _LgpCondId6348SystemOutputoffasrequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6348)
)
if mibBuilder.loadTexts:
    lgpCondId6348SystemOutputoffasrequested.setStatus("current")
_LgpCondId6349SystemOffasrequested_ObjectIdentity = ObjectIdentity
lgpCondId6349SystemOffasrequested = _LgpCondId6349SystemOffasrequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6349)
)
if mibBuilder.loadTexts:
    lgpCondId6349SystemOffasrequested.setStatus("current")
_LgpCondId6350GeneralFault_ObjectIdentity = ObjectIdentity
lgpCondId6350GeneralFault = _LgpCondId6350GeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6350)
)
if mibBuilder.loadTexts:
    lgpCondId6350GeneralFault.setStatus("current")
_LgpCondId6351UPSAwaitingPower_ObjectIdentity = ObjectIdentity
lgpCondId6351UPSAwaitingPower = _LgpCondId6351UPSAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6351)
)
if mibBuilder.loadTexts:
    lgpCondId6351UPSAwaitingPower.setStatus("current")
_LgpCondId6352AutonomyCalibration_ObjectIdentity = ObjectIdentity
lgpCondId6352AutonomyCalibration = _LgpCondId6352AutonomyCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6352)
)
if mibBuilder.loadTexts:
    lgpCondId6352AutonomyCalibration.setStatus("current")
_LgpCondId6353GeneralWarning_ObjectIdentity = ObjectIdentity
lgpCondId6353GeneralWarning = _LgpCondId6353GeneralWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6353)
)
if mibBuilder.loadTexts:
    lgpCondId6353GeneralWarning.setStatus("current")
_LgpCondId6354BatteryCharging_ObjectIdentity = ObjectIdentity
lgpCondId6354BatteryCharging = _LgpCondId6354BatteryCharging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6354)
)
if mibBuilder.loadTexts:
    lgpCondId6354BatteryCharging.setStatus("current")
_LgpCondId6355BackfeedRelayFailure_ObjectIdentity = ObjectIdentity
lgpCondId6355BackfeedRelayFailure = _LgpCondId6355BackfeedRelayFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6355)
)
if mibBuilder.loadTexts:
    lgpCondId6355BackfeedRelayFailure.setStatus("current")
_LgpCondId6356BatteryCircuitOpen_ObjectIdentity = ObjectIdentity
lgpCondId6356BatteryCircuitOpen = _LgpCondId6356BatteryCircuitOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6356)
)
if mibBuilder.loadTexts:
    lgpCondId6356BatteryCircuitOpen.setStatus("current")
_LgpCondId6357SystemRestartPending_ObjectIdentity = ObjectIdentity
lgpCondId6357SystemRestartPending = _LgpCondId6357SystemRestartPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6357)
)
if mibBuilder.loadTexts:
    lgpCondId6357SystemRestartPending.setStatus("current")
_LgpCondId6358PipeTemperatureSensorFailure_ObjectIdentity = ObjectIdentity
lgpCondId6358PipeTemperatureSensorFailure = _LgpCondId6358PipeTemperatureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6358)
)
if mibBuilder.loadTexts:
    lgpCondId6358PipeTemperatureSensorFailure.setStatus("current")
_LgpCondId6362SFAReservedEvent26_ObjectIdentity = ObjectIdentity
lgpCondId6362SFAReservedEvent26 = _LgpCondId6362SFAReservedEvent26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6362)
)
if mibBuilder.loadTexts:
    lgpCondId6362SFAReservedEvent26.setStatus("current")
_LgpCondId6363SFAReservedEvent27_ObjectIdentity = ObjectIdentity
lgpCondId6363SFAReservedEvent27 = _LgpCondId6363SFAReservedEvent27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6363)
)
if mibBuilder.loadTexts:
    lgpCondId6363SFAReservedEvent27.setStatus("current")
_LgpCondId6364SFAReservedEvent28_ObjectIdentity = ObjectIdentity
lgpCondId6364SFAReservedEvent28 = _LgpCondId6364SFAReservedEvent28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6364)
)
if mibBuilder.loadTexts:
    lgpCondId6364SFAReservedEvent28.setStatus("current")
_LgpCondId6365SFAReservedEvent29_ObjectIdentity = ObjectIdentity
lgpCondId6365SFAReservedEvent29 = _LgpCondId6365SFAReservedEvent29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6365)
)
if mibBuilder.loadTexts:
    lgpCondId6365SFAReservedEvent29.setStatus("current")
_LgpCondId6366SFAReservedEvent30_ObjectIdentity = ObjectIdentity
lgpCondId6366SFAReservedEvent30 = _LgpCondId6366SFAReservedEvent30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6366)
)
if mibBuilder.loadTexts:
    lgpCondId6366SFAReservedEvent30.setStatus("current")
_LgpCondId6367SFAReservedEvent31_ObjectIdentity = ObjectIdentity
lgpCondId6367SFAReservedEvent31 = _LgpCondId6367SFAReservedEvent31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6367)
)
if mibBuilder.loadTexts:
    lgpCondId6367SFAReservedEvent31.setStatus("current")
_LgpCondId6368SFAReservedEvent32_ObjectIdentity = ObjectIdentity
lgpCondId6368SFAReservedEvent32 = _LgpCondId6368SFAReservedEvent32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6368)
)
if mibBuilder.loadTexts:
    lgpCondId6368SFAReservedEvent32.setStatus("current")
_LgpCondId6369SFAReservedEvent33_ObjectIdentity = ObjectIdentity
lgpCondId6369SFAReservedEvent33 = _LgpCondId6369SFAReservedEvent33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6369)
)
if mibBuilder.loadTexts:
    lgpCondId6369SFAReservedEvent33.setStatus("current")
_LgpCondId6370SFAReservedEvent34_ObjectIdentity = ObjectIdentity
lgpCondId6370SFAReservedEvent34 = _LgpCondId6370SFAReservedEvent34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6370)
)
if mibBuilder.loadTexts:
    lgpCondId6370SFAReservedEvent34.setStatus("current")
_LgpCondId6371SFAReservedEvent35_ObjectIdentity = ObjectIdentity
lgpCondId6371SFAReservedEvent35 = _LgpCondId6371SFAReservedEvent35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6371)
)
if mibBuilder.loadTexts:
    lgpCondId6371SFAReservedEvent35.setStatus("current")
_LgpCondId6372SFAReservedEvent36_ObjectIdentity = ObjectIdentity
lgpCondId6372SFAReservedEvent36 = _LgpCondId6372SFAReservedEvent36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6372)
)
if mibBuilder.loadTexts:
    lgpCondId6372SFAReservedEvent36.setStatus("current")
_LgpCondId6373SFAReservedEvent37_ObjectIdentity = ObjectIdentity
lgpCondId6373SFAReservedEvent37 = _LgpCondId6373SFAReservedEvent37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6373)
)
if mibBuilder.loadTexts:
    lgpCondId6373SFAReservedEvent37.setStatus("current")
_LgpCondId6374SFAReservedEvent38_ObjectIdentity = ObjectIdentity
lgpCondId6374SFAReservedEvent38 = _LgpCondId6374SFAReservedEvent38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6374)
)
if mibBuilder.loadTexts:
    lgpCondId6374SFAReservedEvent38.setStatus("current")
_LgpCondId6375SFAReservedEvent39_ObjectIdentity = ObjectIdentity
lgpCondId6375SFAReservedEvent39 = _LgpCondId6375SFAReservedEvent39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6375)
)
if mibBuilder.loadTexts:
    lgpCondId6375SFAReservedEvent39.setStatus("current")
_LgpCondId6376SFAReservedEvent40_ObjectIdentity = ObjectIdentity
lgpCondId6376SFAReservedEvent40 = _LgpCondId6376SFAReservedEvent40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6376)
)
if mibBuilder.loadTexts:
    lgpCondId6376SFAReservedEvent40.setStatus("current")
_LgpCondId6377SFAReservedEvent41_ObjectIdentity = ObjectIdentity
lgpCondId6377SFAReservedEvent41 = _LgpCondId6377SFAReservedEvent41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6377)
)
if mibBuilder.loadTexts:
    lgpCondId6377SFAReservedEvent41.setStatus("current")
_LgpCondId6378SFAReservedEvent42_ObjectIdentity = ObjectIdentity
lgpCondId6378SFAReservedEvent42 = _LgpCondId6378SFAReservedEvent42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6378)
)
if mibBuilder.loadTexts:
    lgpCondId6378SFAReservedEvent42.setStatus("current")
_LgpCondId6379SFAReservedEvent43_ObjectIdentity = ObjectIdentity
lgpCondId6379SFAReservedEvent43 = _LgpCondId6379SFAReservedEvent43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6379)
)
if mibBuilder.loadTexts:
    lgpCondId6379SFAReservedEvent43.setStatus("current")
_LgpCondId6380SFAReservedEvent44_ObjectIdentity = ObjectIdentity
lgpCondId6380SFAReservedEvent44 = _LgpCondId6380SFAReservedEvent44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6380)
)
if mibBuilder.loadTexts:
    lgpCondId6380SFAReservedEvent44.setStatus("current")
_LgpCondId6381SFAReservedEvent45_ObjectIdentity = ObjectIdentity
lgpCondId6381SFAReservedEvent45 = _LgpCondId6381SFAReservedEvent45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6381)
)
if mibBuilder.loadTexts:
    lgpCondId6381SFAReservedEvent45.setStatus("current")
_LgpCondId6382SFAReservedEvent46_ObjectIdentity = ObjectIdentity
lgpCondId6382SFAReservedEvent46 = _LgpCondId6382SFAReservedEvent46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6382)
)
if mibBuilder.loadTexts:
    lgpCondId6382SFAReservedEvent46.setStatus("current")
_LgpCondId6383SFAReservedEvent47_ObjectIdentity = ObjectIdentity
lgpCondId6383SFAReservedEvent47 = _LgpCondId6383SFAReservedEvent47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6383)
)
if mibBuilder.loadTexts:
    lgpCondId6383SFAReservedEvent47.setStatus("current")
_LgpCondId6384SFAReservedEvent48_ObjectIdentity = ObjectIdentity
lgpCondId6384SFAReservedEvent48 = _LgpCondId6384SFAReservedEvent48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6384)
)
if mibBuilder.loadTexts:
    lgpCondId6384SFAReservedEvent48.setStatus("current")
_LgpCondId6385SFAReservedEvent49_ObjectIdentity = ObjectIdentity
lgpCondId6385SFAReservedEvent49 = _LgpCondId6385SFAReservedEvent49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6385)
)
if mibBuilder.loadTexts:
    lgpCondId6385SFAReservedEvent49.setStatus("current")
_LgpCondId6386SFAReservedEvent50_ObjectIdentity = ObjectIdentity
lgpCondId6386SFAReservedEvent50 = _LgpCondId6386SFAReservedEvent50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6386)
)
if mibBuilder.loadTexts:
    lgpCondId6386SFAReservedEvent50.setStatus("current")
_LgpCondId6438PowerModuleInputCurrentAbnormal_ObjectIdentity = ObjectIdentity
lgpCondId6438PowerModuleInputCurrentAbnormal = _LgpCondId6438PowerModuleInputCurrentAbnormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6438)
)
if mibBuilder.loadTexts:
    lgpCondId6438PowerModuleInputCurrentAbnormal.setStatus("current")
_LgpCondId6439PowerModuleBalancerofDCBusFailure_ObjectIdentity = ObjectIdentity
lgpCondId6439PowerModuleBalancerofDCBusFailure = _LgpCondId6439PowerModuleBalancerofDCBusFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6439)
)
if mibBuilder.loadTexts:
    lgpCondId6439PowerModuleBalancerofDCBusFailure.setStatus("current")
_LgpCondId6440PowerModuleFuseFailure_ObjectIdentity = ObjectIdentity
lgpCondId6440PowerModuleFuseFailure = _LgpCondId6440PowerModuleFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6440)
)
if mibBuilder.loadTexts:
    lgpCondId6440PowerModuleFuseFailure.setStatus("current")
_LgpCondId6441PowerModulePowerSupplyFailure_ObjectIdentity = ObjectIdentity
lgpCondId6441PowerModulePowerSupplyFailure = _LgpCondId6441PowerModulePowerSupplyFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6441)
)
if mibBuilder.loadTexts:
    lgpCondId6441PowerModulePowerSupplyFailure.setStatus("current")
_LgpCondId6450PDUPoweredOn_ObjectIdentity = ObjectIdentity
lgpCondId6450PDUPoweredOn = _LgpCondId6450PDUPoweredOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6450)
)
if mibBuilder.loadTexts:
    lgpCondId6450PDUPoweredOn.setStatus("current")
_LgpCondId6453InputWiringFault_ObjectIdentity = ObjectIdentity
lgpCondId6453InputWiringFault = _LgpCondId6453InputWiringFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6453)
)
if mibBuilder.loadTexts:
    lgpCondId6453InputWiringFault.setStatus("current")
_LgpCondId6454DCtoDCConverterFault_ObjectIdentity = ObjectIdentity
lgpCondId6454DCtoDCConverterFault = _LgpCondId6454DCtoDCConverterFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6454)
)
if mibBuilder.loadTexts:
    lgpCondId6454DCtoDCConverterFault.setStatus("current")
_LgpCondId6455LeakSensorCableFault_ObjectIdentity = ObjectIdentity
lgpCondId6455LeakSensorCableFault = _LgpCondId6455LeakSensorCableFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6455)
)
if mibBuilder.loadTexts:
    lgpCondId6455LeakSensorCableFault.setStatus("current")
_LgpCondId6518StandbyUnitActivatedDuetoChillerFailure_ObjectIdentity = ObjectIdentity
lgpCondId6518StandbyUnitActivatedDuetoChillerFailure = _LgpCondId6518StandbyUnitActivatedDuetoChillerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 6518)
)
if mibBuilder.loadTexts:
    lgpCondId6518StandbyUnitActivatedDuetoChillerFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-FLEXIBLE-CONDITIONS-MIB",
    **{"liebertGlobalProductsFlexibleConditionsModule": liebertGlobalProductsFlexibleConditionsModule,
       "lgpFlexConditionsWellKnown": lgpFlexConditionsWellKnown,
       "lgpCondId4122SystemInputPowerProblem": lgpCondId4122SystemInputPowerProblem,
       "lgpCondId4132BypassOverloadPhaseA": lgpCondId4132BypassOverloadPhaseA,
       "lgpCondId4133BypassOverloadPhaseB": lgpCondId4133BypassOverloadPhaseB,
       "lgpCondId4134BypassOverloadPhaseC": lgpCondId4134BypassOverloadPhaseC,
       "lgpCondId4135BypassNotAvailable": lgpCondId4135BypassNotAvailable,
       "lgpCondId4137BypassAutoRetransferPrimed": lgpCondId4137BypassAutoRetransferPrimed,
       "lgpCondId4138BypassAutoRetransferFailed": lgpCondId4138BypassAutoRetransferFailed,
       "lgpCondId4139BypassExcessAutoRetransfers": lgpCondId4139BypassExcessAutoRetransfers,
       "lgpCondId4140BypassRestartInhibitExternal": lgpCondId4140BypassRestartInhibitExternal,
       "lgpCondId4141BypassBreakerClosed": lgpCondId4141BypassBreakerClosed,
       "lgpCondId4142BypassStaticSwitchOverload": lgpCondId4142BypassStaticSwitchOverload,
       "lgpCondId4143BypassStaticSwitchUnavailable": lgpCondId4143BypassStaticSwitchUnavailable,
       "lgpCondId4144BypassExcessivePulseParallel": lgpCondId4144BypassExcessivePulseParallel,
       "lgpCondId4145BypassAutoTransferFailed": lgpCondId4145BypassAutoTransferFailed,
       "lgpCondId4146SystemInputPhsRotationError": lgpCondId4146SystemInputPhsRotationError,
       "lgpCondId4147SystemInputCurrentLimit": lgpCondId4147SystemInputCurrentLimit,
       "lgpCondId4162BatteryLow": lgpCondId4162BatteryLow,
       "lgpCondId4163OutputOffEndofDischarge": lgpCondId4163OutputOffEndofDischarge,
       "lgpCondId4164BatteryChargingError": lgpCondId4164BatteryChargingError,
       "lgpCondId4165BatteryChargingReducedExtrnl": lgpCondId4165BatteryChargingReducedExtrnl,
       "lgpCondId4166BatteryCapacityLow": lgpCondId4166BatteryCapacityLow,
       "lgpCondId4167OutputOff": lgpCondId4167OutputOff,
       "lgpCondId4168BatteryDischarging": lgpCondId4168BatteryDischarging,
       "lgpCondId4169BatteryTemperatureImbalance": lgpCondId4169BatteryTemperatureImbalance,
       "lgpCondId4170BatteryEqualize": lgpCondId4170BatteryEqualize,
       "lgpCondId4171BatteryManualTestInProgress": lgpCondId4171BatteryManualTestInProgress,
       "lgpCondId4172BatteryAutoTestInProgress": lgpCondId4172BatteryAutoTestInProgress,
       "lgpCondId4173MainBatteryDisconnectOpen": lgpCondId4173MainBatteryDisconnectOpen,
       "lgpCondId4174BatteryTemperatureSensorFault": lgpCondId4174BatteryTemperatureSensorFault,
       "lgpCondId4175BypassFrequencyError": lgpCondId4175BypassFrequencyError,
       "lgpCondId4176BatteryCircuitBreaker1Open": lgpCondId4176BatteryCircuitBreaker1Open,
       "lgpCondId4177BatteryBreaker1OpenFailure": lgpCondId4177BatteryBreaker1OpenFailure,
       "lgpCondId4178BatteryBreaker1CloseFailure": lgpCondId4178BatteryBreaker1CloseFailure,
       "lgpCondId4179BatteryCircuitBreaker2Open": lgpCondId4179BatteryCircuitBreaker2Open,
       "lgpCondId4180BatteryBreaker2OpenFailure": lgpCondId4180BatteryBreaker2OpenFailure,
       "lgpCondId4181BatteryBreaker2CloseFailure": lgpCondId4181BatteryBreaker2CloseFailure,
       "lgpCondId4182BatteryCircuitBreaker3Open": lgpCondId4182BatteryCircuitBreaker3Open,
       "lgpCondId4183BatteryBreaker3OpenFailure": lgpCondId4183BatteryBreaker3OpenFailure,
       "lgpCondId4184BatteryBreaker3CloseFailure": lgpCondId4184BatteryBreaker3CloseFailure,
       "lgpCondId4185BatteryCircuitBreaker4Open": lgpCondId4185BatteryCircuitBreaker4Open,
       "lgpCondId4186BatteryBreaker4OpenFailure": lgpCondId4186BatteryBreaker4OpenFailure,
       "lgpCondId4187BatteryBreaker4CloseFailure": lgpCondId4187BatteryBreaker4CloseFailure,
       "lgpCondId4188BatteryCircuitBreaker5Open": lgpCondId4188BatteryCircuitBreaker5Open,
       "lgpCondId4189BatteryBreaker5OpenFailure": lgpCondId4189BatteryBreaker5OpenFailure,
       "lgpCondId4190BatteryBreaker5CloseFailure": lgpCondId4190BatteryBreaker5CloseFailure,
       "lgpCondId4191BatteryCircuitBreaker6Open": lgpCondId4191BatteryCircuitBreaker6Open,
       "lgpCondId4192BatteryBreaker6OpenFailure": lgpCondId4192BatteryBreaker6OpenFailure,
       "lgpCondId4193BatteryBreaker6CloseFailure": lgpCondId4193BatteryBreaker6CloseFailure,
       "lgpCondId4194BatteryCircuitBreaker7Open": lgpCondId4194BatteryCircuitBreaker7Open,
       "lgpCondId4195BatteryBreaker7OpenFailure": lgpCondId4195BatteryBreaker7OpenFailure,
       "lgpCondId4196BatteryBreaker7CloseFailure": lgpCondId4196BatteryBreaker7CloseFailure,
       "lgpCondId4197BatteryCircuitBreaker8Open": lgpCondId4197BatteryCircuitBreaker8Open,
       "lgpCondId4198BatteryBreaker8OpenFailure": lgpCondId4198BatteryBreaker8OpenFailure,
       "lgpCondId4199BatteryBreaker8CloseFailure": lgpCondId4199BatteryBreaker8CloseFailure,
       "lgpCondId4200BatteryChargingInhibited": lgpCondId4200BatteryChargingInhibited,
       "lgpCondId4213SystemShutdownEPO": lgpCondId4213SystemShutdownEPO,
       "lgpCondId4214SystemShutdownREPO": lgpCondId4214SystemShutdownREPO,
       "lgpCondId4215SystemOutputOff": lgpCondId4215SystemOutputOff,
       "lgpCondId4216BypassBackfeedDetected": lgpCondId4216BypassBackfeedDetected,
       "lgpCondId4217BypassManualXfrInhibited": lgpCondId4217BypassManualXfrInhibited,
       "lgpCondId4218BypassManualRexfrInhibited": lgpCondId4218BypassManualRexfrInhibited,
       "lgpCondId4219BatteryOverTemperature": lgpCondId4219BatteryOverTemperature,
       "lgpCondId4220BatteryExternalMonitor1": lgpCondId4220BatteryExternalMonitor1,
       "lgpCondId4221BatteryExternalMonitor2": lgpCondId4221BatteryExternalMonitor2,
       "lgpCondId4222BatteryGroundFault": lgpCondId4222BatteryGroundFault,
       "lgpCondId4229EmergencyPowerOffLatched": lgpCondId4229EmergencyPowerOffLatched,
       "lgpCondId4230SystemOutputLowPowerFactor": lgpCondId4230SystemOutputLowPowerFactor,
       "lgpCondId4231OutputCurrentExceedsThreshold": lgpCondId4231OutputCurrentExceedsThreshold,
       "lgpCondId4233InverterFailure": lgpCondId4233InverterFailure,
       "lgpCondId4234InverterOverloadPhaseA": lgpCondId4234InverterOverloadPhaseA,
       "lgpCondId4235InverterOverloadPhaseB": lgpCondId4235InverterOverloadPhaseB,
       "lgpCondId4236InverterOverloadPhaseC": lgpCondId4236InverterOverloadPhaseC,
       "lgpCondId4237InverterInhibitExternal": lgpCondId4237InverterInhibitExternal,
       "lgpCondId4238InverterOutBreakerOpenFail": lgpCondId4238InverterOutBreakerOpenFail,
       "lgpCondId4239InverterOutBreakerCloseFail": lgpCondId4239InverterOutBreakerCloseFail,
       "lgpCondId4270InputContact01": lgpCondId4270InputContact01,
       "lgpCondId4271InputContact02": lgpCondId4271InputContact02,
       "lgpCondId4272InputContact03": lgpCondId4272InputContact03,
       "lgpCondId4273InputContact04": lgpCondId4273InputContact04,
       "lgpCondId4274InputContact05": lgpCondId4274InputContact05,
       "lgpCondId4275InputContact06": lgpCondId4275InputContact06,
       "lgpCondId4276InputContact07": lgpCondId4276InputContact07,
       "lgpCondId4277InputContact08": lgpCondId4277InputContact08,
       "lgpCondId4278InputContact09": lgpCondId4278InputContact09,
       "lgpCondId4279InputContact10": lgpCondId4279InputContact10,
       "lgpCondId4280InputContact11": lgpCondId4280InputContact11,
       "lgpCondId4281InputContact12": lgpCondId4281InputContact12,
       "lgpCondId4282InputContact13": lgpCondId4282InputContact13,
       "lgpCondId4283InputContact14": lgpCondId4283InputContact14,
       "lgpCondId4284InputContact15": lgpCondId4284InputContact15,
       "lgpCondId4285InputContact16": lgpCondId4285InputContact16,
       "lgpCondId4286OutputAmpOverUserLimitPhsA": lgpCondId4286OutputAmpOverUserLimitPhsA,
       "lgpCondId4287OutputAmpOverUserLimitPhsB": lgpCondId4287OutputAmpOverUserLimitPhsB,
       "lgpCondId4288OutputAmpOverUserLimitPhsC": lgpCondId4288OutputAmpOverUserLimitPhsC,
       "lgpCondId4289InverterTransferInhibitExt": lgpCondId4289InverterTransferInhibitExt,
       "lgpCondId4290InverterShutdownOverload": lgpCondId4290InverterShutdownOverload,
       "lgpCondId4294InletAirOverTemperature": lgpCondId4294InletAirOverTemperature,
       "lgpCondId4295RectifierFailure": lgpCondId4295RectifierFailure,
       "lgpCondId4296RectifierOperationInhibitExt": lgpCondId4296RectifierOperationInhibitExt,
       "lgpCondId4297UPSOutputonInverter": lgpCondId4297UPSOutputonInverter,
       "lgpCondId4298UPSOutputonBypass": lgpCondId4298UPSOutputonBypass,
       "lgpCondId4299OutputLoadonMaintBypass": lgpCondId4299OutputLoadonMaintBypass,
       "lgpCondId4300InternalCommunicationsFailure": lgpCondId4300InternalCommunicationsFailure,
       "lgpCondId4308DCBusGroundFaultPositive": lgpCondId4308DCBusGroundFaultPositive,
       "lgpCondId4309DCBusGroundFaultNegative": lgpCondId4309DCBusGroundFaultNegative,
       "lgpCondId4310EquipmentOverTemperature": lgpCondId4310EquipmentOverTemperature,
       "lgpCondId4311SystemFanFailure": lgpCondId4311SystemFanFailure,
       "lgpCondId4313PasswordChanged": lgpCondId4313PasswordChanged,
       "lgpCondId4314PowerSupplyFailure": lgpCondId4314PowerSupplyFailure,
       "lgpCondId4315OnGenerator": lgpCondId4315OnGenerator,
       "lgpCondId4316AutoRestartInProgress": lgpCondId4316AutoRestartInProgress,
       "lgpCondId4317AutoRestartInhibitedExt": lgpCondId4317AutoRestartInhibitedExt,
       "lgpCondId4320InitiatedTransfertoBypass": lgpCondId4320InitiatedTransfertoBypass,
       "lgpCondId4321InitiatedTransfertoInverter": lgpCondId4321InitiatedTransfertoInverter,
       "lgpCondId4322BatteryTestPassed": lgpCondId4322BatteryTestPassed,
       "lgpCondId4323BatteryTestFailed": lgpCondId4323BatteryTestFailed,
       "lgpCondId4324BatteryTestManuallyStopped": lgpCondId4324BatteryTestManuallyStopped,
       "lgpCondId4325BackfeedBreakerOpen": lgpCondId4325BackfeedBreakerOpen,
       "lgpCondId4341VelocityAuthenticationFailure": lgpCondId4341VelocityAuthenticationFailure,
       "lgpCondId4360ReceptacleOverCurrent": lgpCondId4360ReceptacleOverCurrent,
       "lgpCondId4361ReceptacleUnderCurrent": lgpCondId4361ReceptacleUnderCurrent,
       "lgpCondId4382SystemInputCurrentImbalance": lgpCondId4382SystemInputCurrentImbalance,
       "lgpCondId4383BypassStaticSwitchOffExtrnl": lgpCondId4383BypassStaticSwitchOffExtrnl,
       "lgpCondId4384BatteryEoDDisconnect": lgpCondId4384BatteryEoDDisconnect,
       "lgpCondId4389SystemOutputFault": lgpCondId4389SystemOutputFault,
       "lgpCondId4390InverterOffExternal": lgpCondId4390InverterOffExternal,
       "lgpCondId4391InverterStaticSwitchSCRShort": lgpCondId4391InverterStaticSwitchSCRShort,
       "lgpCondId4392TemperatureSensorError": lgpCondId4392TemperatureSensorError,
       "lgpCondId4406BranchOverCurrent": lgpCondId4406BranchOverCurrent,
       "lgpCondId4407BranchUnderCurrent": lgpCondId4407BranchUnderCurrent,
       "lgpCondId4416BranchOverCurrent": lgpCondId4416BranchOverCurrent,
       "lgpCondId4417BranchUnderCurrent": lgpCondId4417BranchUnderCurrent,
       "lgpCondId4421BranchFailure": lgpCondId4421BranchFailure,
       "lgpCondId4436PDUOverCurrent": lgpCondId4436PDUOverCurrent,
       "lgpCondId4437PDUUnderCurrent": lgpCondId4437PDUUnderCurrent,
       "lgpCondId4438SystemInternalTemperatureRise": lgpCondId4438SystemInternalTemperatureRise,
       "lgpCondId4439AutomaticRestartFailed": lgpCondId4439AutomaticRestartFailed,
       "lgpCondId4440FuseFailure": lgpCondId4440FuseFailure,
       "lgpCondId4441SystemControllerError": lgpCondId4441SystemControllerError,
       "lgpCondId4442SystemBreakersOpenFailure": lgpCondId4442SystemBreakersOpenFailure,
       "lgpCondId4448PDUOverCurrent": lgpCondId4448PDUOverCurrent,
       "lgpCondId4449PDUUnderCurrent": lgpCondId4449PDUUnderCurrent,
       "lgpCondId4468PDUOverCurrentL1": lgpCondId4468PDUOverCurrentL1,
       "lgpCondId4469PDUOverCurrentL2": lgpCondId4469PDUOverCurrentL2,
       "lgpCondId4470PDUOverCurrentL3": lgpCondId4470PDUOverCurrentL3,
       "lgpCondId4471PDUUnderCurrentL1": lgpCondId4471PDUUnderCurrentL1,
       "lgpCondId4472PDUUnderCurrentL2": lgpCondId4472PDUUnderCurrentL2,
       "lgpCondId4473PDUUnderCurrentL3": lgpCondId4473PDUUnderCurrentL3,
       "lgpCondId4492ReceptaclePowerStateOn": lgpCondId4492ReceptaclePowerStateOn,
       "lgpCondId4493ReceptaclePowerStateOff": lgpCondId4493ReceptaclePowerStateOff,
       "lgpCondId4494BranchBreakerOpen": lgpCondId4494BranchBreakerOpen,
       "lgpCondId4495DeviceConfigurationChange": lgpCondId4495DeviceConfigurationChange,
       "lgpCondId4496BasicDisplayModuleRemoved": lgpCondId4496BasicDisplayModuleRemoved,
       "lgpCondId4497BasicDisplayModuleDiscovered": lgpCondId4497BasicDisplayModuleDiscovered,
       "lgpCondId4500PDUOverCurrent": lgpCondId4500PDUOverCurrent,
       "lgpCondId4501PDUUnderCurrent": lgpCondId4501PDUUnderCurrent,
       "lgpCondId4502PDUFailure": lgpCondId4502PDUFailure,
       "lgpCondId4503PDUCommunicationFail": lgpCondId4503PDUCommunicationFail,
       "lgpCondId4504BranchRemoved": lgpCondId4504BranchRemoved,
       "lgpCondId4505BranchDiscovered": lgpCondId4505BranchDiscovered,
       "lgpCondId4506BranchOverCurrent": lgpCondId4506BranchOverCurrent,
       "lgpCondId4507BranchCurrent": lgpCondId4507BranchCurrent,
       "lgpCondId4508ReceptacleLoadRemoved": lgpCondId4508ReceptacleLoadRemoved,
       "lgpCondId4509ReceptacleLoadAdded": lgpCondId4509ReceptacleLoadAdded,
       "lgpCondId4523ModuleRemoved": lgpCondId4523ModuleRemoved,
       "lgpCondId4524ModuleAdded": lgpCondId4524ModuleAdded,
       "lgpCondId4550FirmwareUpdateRequired": lgpCondId4550FirmwareUpdateRequired,
       "lgpCondId4551GenericTestEvent": lgpCondId4551GenericTestEvent,
       "lgpCondId4580OverTemperature": lgpCondId4580OverTemperature,
       "lgpCondId4581UnderTemperature": lgpCondId4581UnderTemperature,
       "lgpCondId4588OverRelativeHumidity": lgpCondId4588OverRelativeHumidity,
       "lgpCondId4589UnderRelativeHumidity": lgpCondId4589UnderRelativeHumidity,
       "lgpCondId4601ExternalAirSensorAOverTemperature": lgpCondId4601ExternalAirSensorAOverTemperature,
       "lgpCondId4604ExternalAirSensorBOverTemperature": lgpCondId4604ExternalAirSensorBOverTemperature,
       "lgpCondId4608ExtAirSensorAUnderTemperature": lgpCondId4608ExtAirSensorAUnderTemperature,
       "lgpCondId4611ExtAirSensorBUnderTemperature": lgpCondId4611ExtAirSensorBUnderTemperature,
       "lgpCondId4615ExtDewPointOverTemperature": lgpCondId4615ExtDewPointOverTemperature,
       "lgpCondId4618ExternalAirSensorAIssue": lgpCondId4618ExternalAirSensorAIssue,
       "lgpCondId4621ExternalAirSensorBIssue": lgpCondId4621ExternalAirSensorBIssue,
       "lgpCondId4626SupplyChilledWaterOverTemp": lgpCondId4626SupplyChilledWaterOverTemp,
       "lgpCondId4629SupplyChilledWaterTempSensorIssue": lgpCondId4629SupplyChilledWaterTempSensorIssue,
       "lgpCondId4634SupplyRefrigerantOverTemp": lgpCondId4634SupplyRefrigerantOverTemp,
       "lgpCondId4637SupplyRefrigerantUnderTemp": lgpCondId4637SupplyRefrigerantUnderTemp,
       "lgpCondId4640SupplyRefrigerantTempSensorIssue": lgpCondId4640SupplyRefrigerantTempSensorIssue,
       "lgpCondId4645SupplyFluidOverTemp": lgpCondId4645SupplyFluidOverTemp,
       "lgpCondId4648SupplyFluidUnderTemp": lgpCondId4648SupplyFluidUnderTemp,
       "lgpCondId4651SupplyFluidTempSensorIssue": lgpCondId4651SupplyFluidTempSensorIssue,
       "lgpCondId4656Pump1LossofFlow": lgpCondId4656Pump1LossofFlow,
       "lgpCondId4659Pump2LossofFlow": lgpCondId4659Pump2LossofFlow,
       "lgpCondId4662PumpShortCycle": lgpCondId4662PumpShortCycle,
       "lgpCondId4669Compressor1AHighHeadPressure": lgpCondId4669Compressor1AHighHeadPressure,
       "lgpCondId4672Compressor1BHighHeadPressure": lgpCondId4672Compressor1BHighHeadPressure,
       "lgpCondId4675Compressor2AHighHeadPressure": lgpCondId4675Compressor2AHighHeadPressure,
       "lgpCondId4678Compressor2BHighHeadPressure": lgpCondId4678Compressor2BHighHeadPressure,
       "lgpCondId4681Compressor1AShortCycle": lgpCondId4681Compressor1AShortCycle,
       "lgpCondId4684Compressor1BShortCycle": lgpCondId4684Compressor1BShortCycle,
       "lgpCondId4687Compressor2AShortCycle": lgpCondId4687Compressor2AShortCycle,
       "lgpCondId4690Compressor2BShortCycle": lgpCondId4690Compressor2BShortCycle,
       "lgpCondId4693Tandem1LowSuctionPressure": lgpCondId4693Tandem1LowSuctionPressure,
       "lgpCondId4696Tandem2LowSuctionPressure": lgpCondId4696Tandem2LowSuctionPressure,
       "lgpCondId4703ChilledWaterControlValvePosition": lgpCondId4703ChilledWaterControlValvePosition,
       "lgpCondId4711SystemCondensationDetected": lgpCondId4711SystemCondensationDetected,
       "lgpCondId4714ShutdownLossOfPower": lgpCondId4714ShutdownLossOfPower,
       "lgpCondId4720SmokeDetected": lgpCondId4720SmokeDetected,
       "lgpCondId4723WaterUnderFloor": lgpCondId4723WaterUnderFloor,
       "lgpCondId4726ServiceRequired": lgpCondId4726ServiceRequired,
       "lgpCondId4729FanIssue": lgpCondId4729FanIssue,
       "lgpCondId4732ReceptacleLoadDropped": lgpCondId4732ReceptacleLoadDropped,
       "lgpCondId4740BatteryAutomaticTestInhibited": lgpCondId4740BatteryAutomaticTestInhibited,
       "lgpCondId4741BatterySelfTest": lgpCondId4741BatterySelfTest,
       "lgpCondId4742BatteryLowShutdown": lgpCondId4742BatteryLowShutdown,
       "lgpCondId4747EquipmentTemperatureSensorFail": lgpCondId4747EquipmentTemperatureSensorFail,
       "lgpCondId4749SystemFanFailureRedundant": lgpCondId4749SystemFanFailureRedundant,
       "lgpCondId4750MultipleFanFailure": lgpCondId4750MultipleFanFailure,
       "lgpCondId4753MainControllerFault": lgpCondId4753MainControllerFault,
       "lgpCondId4754SystemBreakersCloseFailure": lgpCondId4754SystemBreakersCloseFailure,
       "lgpCondId4755InputFilterCycleLock": lgpCondId4755InputFilterCycleLock,
       "lgpCondId4756ServiceCodeActive": lgpCondId4756ServiceCodeActive,
       "lgpCondId4757LBSActive": lgpCondId4757LBSActive,
       "lgpCondId4758LBSInhibited": lgpCondId4758LBSInhibited,
       "lgpCondId4759LeadingPowerFactor": lgpCondId4759LeadingPowerFactor,
       "lgpCondId4760ControlsResetRequired": lgpCondId4760ControlsResetRequired,
       "lgpCondId4823ParallelCommWarning": lgpCondId4823ParallelCommWarning,
       "lgpCondId4824SystemCommFail": lgpCondId4824SystemCommFail,
       "lgpCondId4825LossofRedundancy": lgpCondId4825LossofRedundancy,
       "lgpCondId4826BPSSStartupInhibit": lgpCondId4826BPSSStartupInhibit,
       "lgpCondId4827MMSTransferInhibit": lgpCondId4827MMSTransferInhibit,
       "lgpCondId4828MMSRetransferInhibit": lgpCondId4828MMSRetransferInhibit,
       "lgpCondId4830MMSLossofSyncPulse": lgpCondId4830MMSLossofSyncPulse,
       "lgpCondId4831MMSOverload": lgpCondId4831MMSOverload,
       "lgpCondId4834MMSOnBattery": lgpCondId4834MMSOnBattery,
       "lgpCondId4835MMSLowBatteryWarning": lgpCondId4835MMSLowBatteryWarning,
       "lgpCondId4906LowAmbientTemperature": lgpCondId4906LowAmbientTemperature,
       "lgpCondId4907HighAmbientTemperature": lgpCondId4907HighAmbientTemperature,
       "lgpCondId4908LowOverallVoltage": lgpCondId4908LowOverallVoltage,
       "lgpCondId4909HighOverallVoltage": lgpCondId4909HighOverallVoltage,
       "lgpCondId4910HighBatteryStringCurrent": lgpCondId4910HighBatteryStringCurrent,
       "lgpCondId4911LowBatteryStringFloatCurrent": lgpCondId4911LowBatteryStringFloatCurrent,
       "lgpCondId4912HighBatteryStringFloatCurrent": lgpCondId4912HighBatteryStringFloatCurrent,
       "lgpCondId4913HighBatteryStringRippleCurrent": lgpCondId4913HighBatteryStringRippleCurrent,
       "lgpCondId4914BatteryStringDischargeDetected": lgpCondId4914BatteryStringDischargeDetected,
       "lgpCondId4915MaximumDischargeTimeExceeded": lgpCondId4915MaximumDischargeTimeExceeded,
       "lgpCondId4916DischargeLowOverallVoltage": lgpCondId4916DischargeLowOverallVoltage,
       "lgpCondId4917DischargeLowCellVoltage": lgpCondId4917DischargeLowCellVoltage,
       "lgpCondId4918DischargeHighBatteryStringCurrent": lgpCondId4918DischargeHighBatteryStringCurrent,
       "lgpCondId4919ExcessiveCelltoCellTemperatureDeviation": lgpCondId4919ExcessiveCelltoCellTemperatureDeviation,
       "lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation": lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation,
       "lgpCondId4964LowCellVoltage": lgpCondId4964LowCellVoltage,
       "lgpCondId4965HighCellVoltage": lgpCondId4965HighCellVoltage,
       "lgpCondId4966LowCellTemperature": lgpCondId4966LowCellTemperature,
       "lgpCondId4967HighCellTemperature": lgpCondId4967HighCellTemperature,
       "lgpCondId4968LowInternalResistance": lgpCondId4968LowInternalResistance,
       "lgpCondId4969HighInternalResistance": lgpCondId4969HighInternalResistance,
       "lgpCondId4970HighIntercellResistance": lgpCondId4970HighIntercellResistance,
       "lgpCondId4978IntertierResistanceHigh": lgpCondId4978IntertierResistanceHigh,
       "lgpCondId4980SupplyChilledWaterLossofFlow": lgpCondId4980SupplyChilledWaterLossofFlow,
       "lgpCondId4983SupplyRefrigOverTempBand1": lgpCondId4983SupplyRefrigOverTempBand1,
       "lgpCondId4986SupplyRefrigUnderTempBand1": lgpCondId4986SupplyRefrigUnderTempBand1,
       "lgpCondId4990SupplyRefrigOverTempBand2": lgpCondId4990SupplyRefrigOverTempBand2,
       "lgpCondId4993SupplyRefrigUnderTempBand2": lgpCondId4993SupplyRefrigUnderTempBand2,
       "lgpCondId4996Inverter1ShortCycle": lgpCondId4996Inverter1ShortCycle,
       "lgpCondId4999Inverter2ShortCycle": lgpCondId4999Inverter2ShortCycle,
       "lgpCondId5015SupplyAirOverTemperature": lgpCondId5015SupplyAirOverTemperature,
       "lgpCondId5019SupplyAirUnderTemperature": lgpCondId5019SupplyAirUnderTemperature,
       "lgpCondId5023ReturnAirOverTemperature": lgpCondId5023ReturnAirOverTemperature,
       "lgpCondId5026SupplyAirSensorIssue": lgpCondId5026SupplyAirSensorIssue,
       "lgpCondId5034HighReturnHumidity": lgpCondId5034HighReturnHumidity,
       "lgpCondId5036LowReturnHumidity": lgpCondId5036LowReturnHumidity,
       "lgpCondId5037HumidifierHoursExceeded": lgpCondId5037HumidifierHoursExceeded,
       "lgpCondId5038DehumidifierHoursExceeded": lgpCondId5038DehumidifierHoursExceeded,
       "lgpCondId5039HumidifierUnderCurrent": lgpCondId5039HumidifierUnderCurrent,
       "lgpCondId5040HumidifierOverCurrent": lgpCondId5040HumidifierOverCurrent,
       "lgpCondId5041HumidifierLowWater": lgpCondId5041HumidifierLowWater,
       "lgpCondId5042HumidifierCylinderWorn": lgpCondId5042HumidifierCylinderWorn,
       "lgpCondId5043HumidifierIssue": lgpCondId5043HumidifierIssue,
       "lgpCondId5044ExtHumidifierLockout": lgpCondId5044ExtHumidifierLockout,
       "lgpCondId5045HumidifierControlBoardNotDetected": lgpCondId5045HumidifierControlBoardNotDetected,
       "lgpCondId5046ReturnHumidityOutOfProportionalBand": lgpCondId5046ReturnHumidityOutOfProportionalBand,
       "lgpCondId5053LossofAirFlow": lgpCondId5053LossofAirFlow,
       "lgpCondId5054FanHoursExceeded": lgpCondId5054FanHoursExceeded,
       "lgpCondId5055TopFanIssue": lgpCondId5055TopFanIssue,
       "lgpCondId5056BottomFanIssue": lgpCondId5056BottomFanIssue,
       "lgpCondId5060RemoteSensorIssue": lgpCondId5060RemoteSensorIssue,
       "lgpCondId5062Compressor1LowSuctionPressure": lgpCondId5062Compressor1LowSuctionPressure,
       "lgpCondId5063Compressor1HoursExceeded": lgpCondId5063Compressor1HoursExceeded,
       "lgpCondId5064DigScrollComp1TempSensorIssue": lgpCondId5064DigScrollComp1TempSensorIssue,
       "lgpCondId5065DigScrollComp1OverTemp": lgpCondId5065DigScrollComp1OverTemp,
       "lgpCondId5066Compressor1LowPressureTransducerIssue": lgpCondId5066Compressor1LowPressureTransducerIssue,
       "lgpCondId5067ExtCompressorLockout": lgpCondId5067ExtCompressorLockout,
       "lgpCondId5068ReheaterOverTemperature": lgpCondId5068ReheaterOverTemperature,
       "lgpCondId5069ElectricReheater1HoursExceeded": lgpCondId5069ElectricReheater1HoursExceeded,
       "lgpCondId5070ExtReheatLockout": lgpCondId5070ExtReheatLockout,
       "lgpCondId5071Condenser1Issue": lgpCondId5071Condenser1Issue,
       "lgpCondId5072CondenserVFDIssue": lgpCondId5072CondenserVFDIssue,
       "lgpCondId5073CondenserTVSSIssue": lgpCondId5073CondenserTVSSIssue,
       "lgpCondId5104ExtOverTemperature": lgpCondId5104ExtOverTemperature,
       "lgpCondId5105ExtLossofFlow": lgpCondId5105ExtLossofFlow,
       "lgpCondId5106ExtCondenserPumpHighWater": lgpCondId5106ExtCondenserPumpHighWater,
       "lgpCondId5107ExtStandbyGlycolPumpOn": lgpCondId5107ExtStandbyGlycolPumpOn,
       "lgpCondId5108ExternalFireDetected": lgpCondId5108ExternalFireDetected,
       "lgpCondId5109UnitOn": lgpCondId5109UnitOn,
       "lgpCondId5110UnitOff": lgpCondId5110UnitOff,
       "lgpCondId5111UnitStandby": lgpCondId5111UnitStandby,
       "lgpCondId5112UnitPartialShutdown": lgpCondId5112UnitPartialShutdown,
       "lgpCondId5113UnitShutdown": lgpCondId5113UnitShutdown,
       "lgpCondId5114WaterLeakageDetectorSensorIssue": lgpCondId5114WaterLeakageDetectorSensorIssue,
       "lgpCondId5115BMSCommunicationsTimeout": lgpCondId5115BMSCommunicationsTimeout,
       "lgpCondId5116MaintenanceDue": lgpCondId5116MaintenanceDue,
       "lgpCondId5117MaintenanceCompleted": lgpCondId5117MaintenanceCompleted,
       "lgpCondId5118CloggedAirFilter": lgpCondId5118CloggedAirFilter,
       "lgpCondId5119RAMBatteryIssue": lgpCondId5119RAMBatteryIssue,
       "lgpCondId5120MasterUnitCommunicationLost": lgpCondId5120MasterUnitCommunicationLost,
       "lgpCondId5121HighPowerShutdown": lgpCondId5121HighPowerShutdown,
       "lgpCondId5126DigScrollComp2OverTemp": lgpCondId5126DigScrollComp2OverTemp,
       "lgpCondId5144OutputOfUf": lgpCondId5144OutputOfUf,
       "lgpCondId5145MMSModuleAlarmActive": lgpCondId5145MMSModuleAlarmActive,
       "lgpCondId5146CompressorPumpDownIssue": lgpCondId5146CompressorPumpDownIssue,
       "lgpCondId5147ReturnAirSensorIssue": lgpCondId5147ReturnAirSensorIssue,
       "lgpCondId5148CompressorHighPressureTransducerIssue": lgpCondId5148CompressorHighPressureTransducerIssue,
       "lgpCondId5149BatteryNotQualified": lgpCondId5149BatteryNotQualified,
       "lgpCondId5150BatteryTerminalsReversed": lgpCondId5150BatteryTerminalsReversed,
       "lgpCondId5151BatteryConverterFailure": lgpCondId5151BatteryConverterFailure,
       "lgpCondId5152InverterSCROpen": lgpCondId5152InverterSCROpen,
       "lgpCondId5153LoadSharingFault": lgpCondId5153LoadSharingFault,
       "lgpCondId5154DCBusAbnormal": lgpCondId5154DCBusAbnormal,
       "lgpCondId5155MainsInputNeutralLost": lgpCondId5155MainsInputNeutralLost,
       "lgpCondId5156LoadImpactTransfer": lgpCondId5156LoadImpactTransfer,
       "lgpCondId5157UserOperationInvalid": lgpCondId5157UserOperationInvalid,
       "lgpCondId5158PowerSubModuleFault": lgpCondId5158PowerSubModuleFault,
       "lgpCondId5178OutputOvervoltage": lgpCondId5178OutputOvervoltage,
       "lgpCondId5179OutputUndervoltage": lgpCondId5179OutputUndervoltage,
       "lgpCondId5180OutputOvercurrent": lgpCondId5180OutputOvercurrent,
       "lgpCondId5181NeutralOvercurrent": lgpCondId5181NeutralOvercurrent,
       "lgpCondId5182GroundOvercurrent": lgpCondId5182GroundOvercurrent,
       "lgpCondId5183OutputVoltageTHD": lgpCondId5183OutputVoltageTHD,
       "lgpCondId5184OutputFrequencyError": lgpCondId5184OutputFrequencyError,
       "lgpCondId5185TransformerOvertemperature": lgpCondId5185TransformerOvertemperature,
       "lgpCondId5212PanelSummaryStatus": lgpCondId5212PanelSummaryStatus,
       "lgpCondId5213PanelOvervoltage": lgpCondId5213PanelOvervoltage,
       "lgpCondId5214PanelUndervoltage": lgpCondId5214PanelUndervoltage,
       "lgpCondId5215PanelOvercurrent": lgpCondId5215PanelOvercurrent,
       "lgpCondId5216PanelNeutralOvercurrent": lgpCondId5216PanelNeutralOvercurrent,
       "lgpCondId5217PanelGroundOvercurrent": lgpCondId5217PanelGroundOvercurrent,
       "lgpCondId5226BranchOvercurrent": lgpCondId5226BranchOvercurrent,
       "lgpCondId5227BranchUndercurrent": lgpCondId5227BranchUndercurrent,
       "lgpCondId5245SubfeedPhaseOvercurrent": lgpCondId5245SubfeedPhaseOvercurrent,
       "lgpCondId5246SubfeedNeutralOvercurrent": lgpCondId5246SubfeedNeutralOvercurrent,
       "lgpCondId5247SubfeedGroundOvercurrent": lgpCondId5247SubfeedGroundOvercurrent,
       "lgpCondId5249EventState": lgpCondId5249EventState,
       "lgpCondId5263CompressorNotStopping": lgpCondId5263CompressorNotStopping,
       "lgpCondId5269CompressorHoursExceeded": lgpCondId5269CompressorHoursExceeded,
       "lgpCondId5270CompressorHighHeadPressure": lgpCondId5270CompressorHighHeadPressure,
       "lgpCondId5271CompressorLowSuctionPressure": lgpCondId5271CompressorLowSuctionPressure,
       "lgpCondId5272CompressorThermalOverload": lgpCondId5272CompressorThermalOverload,
       "lgpCondId5273CompressorLowOilPressure": lgpCondId5273CompressorLowOilPressure,
       "lgpCondId5274CompressorHeadPressureOverThreshold": lgpCondId5274CompressorHeadPressureOverThreshold,
       "lgpCondId5275CompressorLossofDifferentialPressure": lgpCondId5275CompressorLossofDifferentialPressure,
       "lgpCondId5277CondenserFanIssue": lgpCondId5277CondenserFanIssue,
       "lgpCondId5278LowCondenserRefrigerantPressure": lgpCondId5278LowCondenserRefrigerantPressure,
       "lgpCondId5280LowFluidPressure": lgpCondId5280LowFluidPressure,
       "lgpCondId5293ReturnFluidOverTemp": lgpCondId5293ReturnFluidOverTemp,
       "lgpCondId5294ReturnFluidUnderTemp": lgpCondId5294ReturnFluidUnderTemp,
       "lgpCondId5295ReturnFluidTempSensorIssue": lgpCondId5295ReturnFluidTempSensorIssue,
       "lgpCondId5296TeamworkReturnFluidTempSensorIssue": lgpCondId5296TeamworkReturnFluidTempSensorIssue,
       "lgpCondId5297AllPumpsLossofFlow": lgpCondId5297AllPumpsLossofFlow,
       "lgpCondId5300PumpHoursExceeded": lgpCondId5300PumpHoursExceeded,
       "lgpCondId5306FreeCoolingValveHoursExceeded": lgpCondId5306FreeCoolingValveHoursExceeded,
       "lgpCondId5308EvaporatorInletTempSensorIssue": lgpCondId5308EvaporatorInletTempSensorIssue,
       "lgpCondId5309TeamworkEvaporatorInletTempSensorIssue": lgpCondId5309TeamworkEvaporatorInletTempSensorIssue,
       "lgpCondId5310EvaporatorFluidFreezeAutoReset": lgpCondId5310EvaporatorFluidFreezeAutoReset,
       "lgpCondId5311EvaporatorFluidFreezeManualResetRequired": lgpCondId5311EvaporatorFluidFreezeManualResetRequired,
       "lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss": lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss,
       "lgpCondId5335ReturnAirUnderTemperature": lgpCondId5335ReturnAirUnderTemperature,
       "lgpCondId5349ExtAirSensorAHighHumidity": lgpCondId5349ExtAirSensorAHighHumidity,
       "lgpCondId5351ExtAirSensorALowHumidity": lgpCondId5351ExtAirSensorALowHumidity,
       "lgpCondId5352CompressorShortCycle": lgpCondId5352CompressorShortCycle,
       "lgpCondId5354DigScrollCompDischargeTempSensorIssue": lgpCondId5354DigScrollCompDischargeTempSensorIssue,
       "lgpCondId5355DigScrollCompOverTemp": lgpCondId5355DigScrollCompOverTemp,
       "lgpCondId5361ExtFreeCoolingLockout": lgpCondId5361ExtFreeCoolingLockout,
       "lgpCondId5362FreeCoolingTempSensorIssue": lgpCondId5362FreeCoolingTempSensorIssue,
       "lgpCondId5365HotWaterHotGasValveHoursExceeded": lgpCondId5365HotWaterHotGasValveHoursExceeded,
       "lgpCondId5368ElectricReheaterHoursExceeded": lgpCondId5368ElectricReheaterHoursExceeded,
       "lgpCondId5376MainFanOverload": lgpCondId5376MainFanOverload,
       "lgpCondId5377Condenser": lgpCondId5377Condenser,
       "lgpCondId5415ExtLossofAirBlower": lgpCondId5415ExtLossofAirBlower,
       "lgpCondId5416ExtStandbyUnitOn": lgpCondId5416ExtStandbyUnitOn,
       "lgpCondId5417DigitalOutputBoardNotDetected": lgpCondId5417DigitalOutputBoardNotDetected,
       "lgpCondId5418UnitCodeMissing": lgpCondId5418UnitCodeMissing,
       "lgpCondId5419UnitCommunicationLost": lgpCondId5419UnitCommunicationLost,
       "lgpCondId5422OvertemperaturePowerOff": lgpCondId5422OvertemperaturePowerOff,
       "lgpCondId5423TooManySensors": lgpCondId5423TooManySensors,
       "lgpCondId5432TransformerOvertemperaturePowerOff": lgpCondId5432TransformerOvertemperaturePowerOff,
       "lgpCondId5433TransformerOvertemperature": lgpCondId5433TransformerOvertemperature,
       "lgpCondId5434TransformerTemperatureSensorFail": lgpCondId5434TransformerTemperatureSensorFail,
       "lgpCondId5436LowAmbientTemperatureProbeTwo": lgpCondId5436LowAmbientTemperatureProbeTwo,
       "lgpCondId5437HighAmbientTemperatureProbeTwo": lgpCondId5437HighAmbientTemperatureProbeTwo,
       "lgpCondId5438ThermalRunawayDetected": lgpCondId5438ThermalRunawayDetected,
       "lgpCondId5439BatteryStringEqualize": lgpCondId5439BatteryStringEqualize,
       "lgpCondId5440BatteryStringOffline": lgpCondId5440BatteryStringOffline,
       "lgpCondId5442DischargeLowCellVoltage": lgpCondId5442DischargeLowCellVoltage,
       "lgpCondId5447MMSPowerSharing": lgpCondId5447MMSPowerSharing,
       "lgpCondId5453ModuleInStandbyIntelligentParalleling": lgpCondId5453ModuleInStandbyIntelligentParalleling,
       "lgpCondId5456ECOModeActive": lgpCondId5456ECOModeActive,
       "lgpCondId5457ECOModeSuspended": lgpCondId5457ECOModeSuspended,
       "lgpCondId5458ExcessECOSuspends": lgpCondId5458ExcessECOSuspends,
       "lgpCondId5471DoorOpen": lgpCondId5471DoorOpen,
       "lgpCondId5472DoorSensorDisconnected": lgpCondId5472DoorSensorDisconnected,
       "lgpCondId5479ContactClosureOpen": lgpCondId5479ContactClosureOpen,
       "lgpCondId5480ContactClosureClosed": lgpCondId5480ContactClosureClosed,
       "lgpCondId5492ExtSystemCondensationDetected": lgpCondId5492ExtSystemCondensationDetected,
       "lgpCondId5495ExtFanIssue": lgpCondId5495ExtFanIssue,
       "lgpCondId5500ExtRemoteShutdown": lgpCondId5500ExtRemoteShutdown,
       "lgpCondId5505HotAisleTempOutofRange": lgpCondId5505HotAisleTempOutofRange,
       "lgpCondId5508ColdAisleTempOutofRange": lgpCondId5508ColdAisleTempOutofRange,
       "lgpCondId5512RemoteShutdown": lgpCondId5512RemoteShutdown,
       "lgpCondId5513CompressorCapacityReduced": lgpCondId5513CompressorCapacityReduced,
       "lgpCondId5514CompressorLowPressureTransducerIssue": lgpCondId5514CompressorLowPressureTransducerIssue,
       "lgpCondId5524PDUNeutralOverCurrent": lgpCondId5524PDUNeutralOverCurrent,
       "lgpCondId5531CondenserCommunicationLost": lgpCondId5531CondenserCommunicationLost,
       "lgpCondId5535CondenserOutsideAirTempSensorIssue": lgpCondId5535CondenserOutsideAirTempSensorIssue,
       "lgpCondId5536CondenserOutsideAirTempOutofOperatingRange": lgpCondId5536CondenserOutsideAirTempOutofOperatingRange,
       "lgpCondId5537CondenserControlBoardIssue": lgpCondId5537CondenserControlBoardIssue,
       "lgpCondId5539CondenserRefrigerantPressureOverThreshold": lgpCondId5539CondenserRefrigerantPressureOverThreshold,
       "lgpCondId5540CondenserRefrigerantPressureUnderThreshold": lgpCondId5540CondenserRefrigerantPressureUnderThreshold,
       "lgpCondId5541CondenserRefrigerantPressureSensorIssue": lgpCondId5541CondenserRefrigerantPressureSensorIssue,
       "lgpCondId5542CondenserSupplyRefrigerantOverTemp": lgpCondId5542CondenserSupplyRefrigerantOverTemp,
       "lgpCondId5543CondenserSupplyRefrigerantUnderTemp": lgpCondId5543CondenserSupplyRefrigerantUnderTemp,
       "lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue": lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue,
       "lgpCondId5545CondenserMaxFanSpeedOverride": lgpCondId5545CondenserMaxFanSpeedOverride,
       "lgpCondId5559EvaporatorReturnFluidOverTemp": lgpCondId5559EvaporatorReturnFluidOverTemp,
       "lgpCondId5560EvaporatorReturnFluidUnderTemp": lgpCondId5560EvaporatorReturnFluidUnderTemp,
       "lgpCondId5561LBSActiveMaster": lgpCondId5561LBSActiveMaster,
       "lgpCondId5562LBSActiveSlave": lgpCondId5562LBSActiveSlave,
       "lgpCondId5563DCBusLowFault": lgpCondId5563DCBusLowFault,
       "lgpCondId5564FanContactorOpen": lgpCondId5564FanContactorOpen,
       "lgpCondId5565FanContactorOpenFail": lgpCondId5565FanContactorOpenFail,
       "lgpCondId5566FanContactorCloseFail": lgpCondId5566FanContactorCloseFail,
       "lgpCondId5567IPInhibit": lgpCondId5567IPInhibit,
       "lgpCondId5568InputUndervoltage": lgpCondId5568InputUndervoltage,
       "lgpCondId5569InputOvervoltage": lgpCondId5569InputOvervoltage,
       "lgpCondId5573AmbientAirSensorIssue": lgpCondId5573AmbientAirSensorIssue,
       "lgpCondId5577ExtDewPointUnderTemperature": lgpCondId5577ExtDewPointUnderTemperature,
       "lgpCondId5578DewPointOverTemperature": lgpCondId5578DewPointOverTemperature,
       "lgpCondId5579DewPointUnderTemperature": lgpCondId5579DewPointUnderTemperature,
       "lgpCondId5588UnspecifiedGeneralEvent": lgpCondId5588UnspecifiedGeneralEvent,
       "lgpCondId5593RemoteSensorAverageOverTemperature": lgpCondId5593RemoteSensorAverageOverTemperature,
       "lgpCondId5594RemoteSensorAverageUnderTemperature": lgpCondId5594RemoteSensorAverageUnderTemperature,
       "lgpCondId5595RemoteSensorSystemAverageOverTemperature": lgpCondId5595RemoteSensorSystemAverageOverTemperature,
       "lgpCondId5596RemoteSensorSystemAverageUnderTemperature": lgpCondId5596RemoteSensorSystemAverageUnderTemperature,
       "lgpCondId5597RemoteSensorOverTemperature": lgpCondId5597RemoteSensorOverTemperature,
       "lgpCondId5598RemoteSensorUnderTemperature": lgpCondId5598RemoteSensorUnderTemperature,
       "lgpCondId5600AirEconomizerEmergencyOverride": lgpCondId5600AirEconomizerEmergencyOverride,
       "lgpCondId5601AirEconomizerReducedAirflow": lgpCondId5601AirEconomizerReducedAirflow,
       "lgpCondId5604CompressorSuperheatOverThreshold": lgpCondId5604CompressorSuperheatOverThreshold,
       "lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent": lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent,
       "lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent": lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent,
       "lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent": lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent,
       "lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent": lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent,
       "lgpCondId5617TemperatureControlSensorIssue": lgpCondId5617TemperatureControlSensorIssue,
       "lgpCondId5621EEVSuperheatBelowThreshold": lgpCondId5621EEVSuperheatBelowThreshold,
       "lgpCondId5622EEVDischargeTempAboveThreshold": lgpCondId5622EEVDischargeTempAboveThreshold,
       "lgpCondId5623EEVBatteryIssue": lgpCondId5623EEVBatteryIssue,
       "lgpCondId5624EEVPowerIssue": lgpCondId5624EEVPowerIssue,
       "lgpCondId5625EEVUnspecifiedGeneralEvent": lgpCondId5625EEVUnspecifiedGeneralEvent,
       "lgpCondId5629StaticPressureSensorIssue": lgpCondId5629StaticPressureSensorIssue,
       "lgpCondId5630HighStaticPressure": lgpCondId5630HighStaticPressure,
       "lgpCondId5631LowStaticPressure": lgpCondId5631LowStaticPressure,
       "lgpCondId5636PumpUnspecifiedGeneralEvent": lgpCondId5636PumpUnspecifiedGeneralEvent,
       "lgpCondId5637CondenserUnitUnspecifiedGeneralEvent": lgpCondId5637CondenserUnitUnspecifiedGeneralEvent,
       "lgpCondId5638CondenserCircuitUnspecifiedGeneralEvent": lgpCondId5638CondenserCircuitUnspecifiedGeneralEvent,
       "lgpCondId5642SFAReservedEvent1": lgpCondId5642SFAReservedEvent1,
       "lgpCondId5643SFAReservedEvent2": lgpCondId5643SFAReservedEvent2,
       "lgpCondId5644SFAReservedEvent3": lgpCondId5644SFAReservedEvent3,
       "lgpCondId5645SFAReservedEvent4": lgpCondId5645SFAReservedEvent4,
       "lgpCondId5646SFAReservedEvent5": lgpCondId5646SFAReservedEvent5,
       "lgpCondId5647SFAReservedEvent6": lgpCondId5647SFAReservedEvent6,
       "lgpCondId5648SFAReservedEvent7": lgpCondId5648SFAReservedEvent7,
       "lgpCondId5649SFAReservedEvent8": lgpCondId5649SFAReservedEvent8,
       "lgpCondId5650SFAReservedEvent9": lgpCondId5650SFAReservedEvent9,
       "lgpCondId5651SFAReservedEvent10": lgpCondId5651SFAReservedEvent10,
       "lgpCondId5652SFAReservedEvent11": lgpCondId5652SFAReservedEvent11,
       "lgpCondId5653SFAReservedEvent12": lgpCondId5653SFAReservedEvent12,
       "lgpCondId5654SFAReservedEvent13": lgpCondId5654SFAReservedEvent13,
       "lgpCondId5655SFAReservedEvent14": lgpCondId5655SFAReservedEvent14,
       "lgpCondId5656SFAReservedEvent15": lgpCondId5656SFAReservedEvent15,
       "lgpCondId5657SFAReservedEvent16": lgpCondId5657SFAReservedEvent16,
       "lgpCondId5658SFAReservedEvent17": lgpCondId5658SFAReservedEvent17,
       "lgpCondId5659SFAReservedEvent18": lgpCondId5659SFAReservedEvent18,
       "lgpCondId5660SFAReservedEvent19": lgpCondId5660SFAReservedEvent19,
       "lgpCondId5661SFAReservedEvent20": lgpCondId5661SFAReservedEvent20,
       "lgpCondId5662SFAReservedEvent21": lgpCondId5662SFAReservedEvent21,
       "lgpCondId5663SFAReservedEvent22": lgpCondId5663SFAReservedEvent22,
       "lgpCondId5664SFAReservedEvent23": lgpCondId5664SFAReservedEvent23,
       "lgpCondId5665SFAReservedEvent24": lgpCondId5665SFAReservedEvent24,
       "lgpCondId5666SFAReservedEvent25": lgpCondId5666SFAReservedEvent25,
       "lgpCondId5768OutletAirOvertemperatureLimit": lgpCondId5768OutletAirOvertemperatureLimit,
       "lgpCondId5769EMOShutdown": lgpCondId5769EMOShutdown,
       "lgpCondId5770TopOutletFanFault": lgpCondId5770TopOutletFanFault,
       "lgpCondId5771MMSOverCapacity": lgpCondId5771MMSOverCapacity,
       "lgpCondId5773CompressorCapacityNormal": lgpCondId5773CompressorCapacityNormal,
       "lgpCondId5774CompressorContactorIssue": lgpCondId5774CompressorContactorIssue,
       "lgpCondId5775UnitShutdownUnspecifiedGeneralEvent": lgpCondId5775UnitShutdownUnspecifiedGeneralEvent,
       "lgpCondId5776PDULowVoltageLN": lgpCondId5776PDULowVoltageLN,
       "lgpCondId5777PDULowVoltageLL": lgpCondId5777PDULowVoltageLL,
       "lgpCondId5778PDULowVoltageL1L2": lgpCondId5778PDULowVoltageL1L2,
       "lgpCondId5779PDULowVoltageL2L3": lgpCondId5779PDULowVoltageL2L3,
       "lgpCondId5780PDULowVoltageL3L1": lgpCondId5780PDULowVoltageL3L1,
       "lgpCondId5781PDULowVoltageL1N": lgpCondId5781PDULowVoltageL1N,
       "lgpCondId5782PDULowVoltageL2N": lgpCondId5782PDULowVoltageL2N,
       "lgpCondId5783PDULowVoltageL3N": lgpCondId5783PDULowVoltageL3N,
       "lgpCondId5784BranchLowVoltageLN": lgpCondId5784BranchLowVoltageLN,
       "lgpCondId5785BranchLowVoltageLL": lgpCondId5785BranchLowVoltageLL,
       "lgpCondId5786BranchLowVoltage": lgpCondId5786BranchLowVoltage,
       "lgpCondId5788ContTieActive": lgpCondId5788ContTieActive,
       "lgpCondId5792UserkWhReset": lgpCondId5792UserkWhReset,
       "lgpCondId5796PeakkWReset": lgpCondId5796PeakkWReset,
       "lgpCondId5798BypassOverload": lgpCondId5798BypassOverload,
       "lgpCondId5801LowBatteryShutdownImminent": lgpCondId5801LowBatteryShutdownImminent,
       "lgpCondId5806OutputOverload": lgpCondId5806OutputOverload,
       "lgpCondId5807OutputOffPending": lgpCondId5807OutputOffPending,
       "lgpCondId5808SystemShutdownOutputShort": lgpCondId5808SystemShutdownOutputShort,
       "lgpCondId5809SystemShutdownLowBattery": lgpCondId5809SystemShutdownLowBattery,
       "lgpCondId5810SystemShutdownRemoteShutdown": lgpCondId5810SystemShutdownRemoteShutdown,
       "lgpCondId5811SystemShutdownHardwareFault": lgpCondId5811SystemShutdownHardwareFault,
       "lgpCondId5817LossofRedundancy": lgpCondId5817LossofRedundancy,
       "lgpCondId5818PowerModuleFailure": lgpCondId5818PowerModuleFailure,
       "lgpCondId5819PowerModuleWarning": lgpCondId5819PowerModuleWarning,
       "lgpCondId5838PowerModuleFanFault": lgpCondId5838PowerModuleFanFault,
       "lgpCondId5839PowerModuleOverTemperature": lgpCondId5839PowerModuleOverTemperature,
       "lgpCondId5840PowerModuleShutdownOverTemperature": lgpCondId5840PowerModuleShutdownOverTemperature,
       "lgpCondId5842ChargerModuleFanFault": lgpCondId5842ChargerModuleFanFault,
       "lgpCondId5847BatteryModuleTemperatureSensorFault": lgpCondId5847BatteryModuleTemperatureSensorFault,
       "lgpCondId5848BatteryModuleOverTemperature": lgpCondId5848BatteryModuleOverTemperature,
       "lgpCondId5849ReplaceBatteryModule": lgpCondId5849ReplaceBatteryModule,
       "lgpCondId5850SystemShutdownTransformerOverTemperature": lgpCondId5850SystemShutdownTransformerOverTemperature,
       "lgpCondId5851MaximumLoadAlarm": lgpCondId5851MaximumLoadAlarm,
       "lgpCondId5856BatteryModuleFault": lgpCondId5856BatteryModuleFault,
       "lgpCondId5857BatteryModuleWarning": lgpCondId5857BatteryModuleWarning,
       "lgpCondId5862CheckAirFilter": lgpCondId5862CheckAirFilter,
       "lgpCondId5863TransformerFanFault": lgpCondId5863TransformerFanFault,
       "lgpCondId5865NoLoadWarning": lgpCondId5865NoLoadWarning,
       "lgpCondId5871BatteryOverTemperatureLimit": lgpCondId5871BatteryOverTemperatureLimit,
       "lgpCondId5873UnexpectedMainBatteryDisconnectClosure": lgpCondId5873UnexpectedMainBatteryDisconnectClosure,
       "lgpCondId5874BatteryOverVoltage": lgpCondId5874BatteryOverVoltage,
       "lgpCondId5875BatteryFuseFault": lgpCondId5875BatteryFuseFault,
       "lgpCondId5878MainBatteryDisconnectForcedToUnlock": lgpCondId5878MainBatteryDisconnectForcedToUnlock,
       "lgpCondId5879VdcBackfeed": lgpCondId5879VdcBackfeed,
       "lgpCondId5880RectifierConfigurationChangeRequest": lgpCondId5880RectifierConfigurationChangeRequest,
       "lgpCondId5881RegenerationActive": lgpCondId5881RegenerationActive,
       "lgpCondId5882RegenerationOperationTerminated": lgpCondId5882RegenerationOperationTerminated,
       "lgpCondId5883RegenerationOperationFailure": lgpCondId5883RegenerationOperationFailure,
       "lgpCondId5884ProgramInputContact01": lgpCondId5884ProgramInputContact01,
       "lgpCondId5885ProgramInputContact02": lgpCondId5885ProgramInputContact02,
       "lgpCondId5886ProgramInputContact03": lgpCondId5886ProgramInputContact03,
       "lgpCondId5887ProgramInputContact04": lgpCondId5887ProgramInputContact04,
       "lgpCondId5888ProgramInputContact05": lgpCondId5888ProgramInputContact05,
       "lgpCondId5889ProgramInputContact06": lgpCondId5889ProgramInputContact06,
       "lgpCondId5890ProgramInputContact07": lgpCondId5890ProgramInputContact07,
       "lgpCondId5891ProgramInputContact08": lgpCondId5891ProgramInputContact08,
       "lgpCondId5892ProgramInputContact09": lgpCondId5892ProgramInputContact09,
       "lgpCondId5893ProgramInputContact10": lgpCondId5893ProgramInputContact10,
       "lgpCondId5894ProgramInputContact11": lgpCondId5894ProgramInputContact11,
       "lgpCondId5895ProgramInputContact12": lgpCondId5895ProgramInputContact12,
       "lgpCondId5896GroundFaultDetected": lgpCondId5896GroundFaultDetected,
       "lgpCondId5902ReturnHumiditySensorIssue": lgpCondId5902ReturnHumiditySensorIssue,
       "lgpCondId5903CompressorLowDifferentialPressureLockout": lgpCondId5903CompressorLowDifferentialPressureLockout,
       "lgpCondId5906AirflowSensorIssue": lgpCondId5906AirflowSensorIssue,
       "lgpCondId5907ExtAirDamperPositionIssue": lgpCondId5907ExtAirDamperPositionIssue,
       "lgpCondId5908ExtPowerSourceAFailure": lgpCondId5908ExtPowerSourceAFailure,
       "lgpCondId5909ExtPowerSourceBFailure": lgpCondId5909ExtPowerSourceBFailure,
       "lgpCondId5910StaticPressureSensorOutofRange": lgpCondId5910StaticPressureSensorOutofRange,
       "lgpCondId5911FluidTemperatureSensorIssue": lgpCondId5911FluidTemperatureSensorIssue,
       "lgpCondId5912FluidFlowSensorIssue": lgpCondId5912FluidFlowSensorIssue,
       "lgpCondId5914OverDifferentialPressure": lgpCondId5914OverDifferentialPressure,
       "lgpCondId5915UnderDifferentialPressure": lgpCondId5915UnderDifferentialPressure,
       "lgpCondId5924MixedModeLockout": lgpCondId5924MixedModeLockout,
       "lgpCondId5928UnbalancedLoadCondition": lgpCondId5928UnbalancedLoadCondition,
       "lgpCondId5939BranchOverCurrentProtection": lgpCondId5939BranchOverCurrentProtection,
       "lgpCondId5948BranchLowVoltageLL": lgpCondId5948BranchLowVoltageLL,
       "lgpCondId5957BypassInputVoltageFault": lgpCondId5957BypassInputVoltageFault,
       "lgpCondId5958BatteryTemperatureOutofRange": lgpCondId5958BatteryTemperatureOutofRange,
       "lgpCondId5960InverterOverload": lgpCondId5960InverterOverload,
       "lgpCondId5966AuxAirTempDeviceCommunicationLost": lgpCondId5966AuxAirTempDeviceCommunicationLost,
       "lgpCondId5967ModbusPowerMeterCommunicationLost": lgpCondId5967ModbusPowerMeterCommunicationLost,
       "lgpCondId5968InverterDesaturation": lgpCondId5968InverterDesaturation,
       "lgpCondId5969GenericDICFault": lgpCondId5969GenericDICFault,
       "lgpCondId5970GroundFault": lgpCondId5970GroundFault,
       "lgpCondId5973InputBreakerOpen": lgpCondId5973InputBreakerOpen,
       "lgpCondId5974NeutralBreakerOpen": lgpCondId5974NeutralBreakerOpen,
       "lgpCondId5975OutputBreakerOpen": lgpCondId5975OutputBreakerOpen,
       "lgpCondId5976MaintenanceBypassBreakerClosed": lgpCondId5976MaintenanceBypassBreakerClosed,
       "lgpCondId5977BatteryBreakerOpen": lgpCondId5977BatteryBreakerOpen,
       "lgpCondId5978RectifierIsolationBreakerRFBOpen": lgpCondId5978RectifierIsolationBreakerRFBOpen,
       "lgpCondId5982BypassBreakerSBBOpen": lgpCondId5982BypassBreakerSBBOpen,
       "lgpCondId5983BypassIsolationBreakerBIBOpen": lgpCondId5983BypassIsolationBreakerBIBOpen,
       "lgpCondId5984BypassUndervoltageWarning": lgpCondId5984BypassUndervoltageWarning,
       "lgpCondId5985BypassStaticSwitchBPSSOn": lgpCondId5985BypassStaticSwitchBPSSOn,
       "lgpCondId5998BattOvtempWarning": lgpCondId5998BattOvtempWarning,
       "lgpCondId6009InverterOutputBreakerOpen": lgpCondId6009InverterOutputBreakerOpen,
       "lgpCondId6011EquipmentOverTempWarning": lgpCondId6011EquipmentOverTempWarning,
       "lgpCondId6012EquipmentOvertemperatureLimit": lgpCondId6012EquipmentOvertemperatureLimit,
       "lgpCondId6045RectifierInputBreakerOpen": lgpCondId6045RectifierInputBreakerOpen,
       "lgpCondId6046LoadonUPS": lgpCondId6046LoadonUPS,
       "lgpCondId6047Core2CoreFuseFailure": lgpCondId6047Core2CoreFuseFailure,
       "lgpCondId6052SystemOutputBreakerOpen": lgpCondId6052SystemOutputBreakerOpen,
       "lgpCondId6059InverterRelayFault": lgpCondId6059InverterRelayFault,
       "lgpCondId6060TransfertoBypassSystemOverload": lgpCondId6060TransfertoBypassSystemOverload,
       "lgpCondId6061InputSourceBackfeed": lgpCondId6061InputSourceBackfeed,
       "lgpCondId6062LossofSynchronization": lgpCondId6062LossofSynchronization,
       "lgpCondId6063BatteryConverterCurrentLimit": lgpCondId6063BatteryConverterCurrentLimit,
       "lgpCondId6064LBSCableFailure": lgpCondId6064LBSCableFailure,
       "lgpCondId6065BatteryChargeEqualizationTimeout": lgpCondId6065BatteryChargeEqualizationTimeout,
       "lgpCondId6066ParallelCableFailure": lgpCondId6066ParallelCableFailure,
       "lgpCondId6067BatteryFault": lgpCondId6067BatteryFault,
       "lgpCondId6068BatteryRoomAlarm": lgpCondId6068BatteryRoomAlarm,
       "lgpCondId6080UPSCCommunicationFailure": lgpCondId6080UPSCCommunicationFailure,
       "lgpCondId6092Compressor1BThermalOverload": lgpCondId6092Compressor1BThermalOverload,
       "lgpCondId6093Compressor2BThermalOverload": lgpCondId6093Compressor2BThermalOverload,
       "lgpCondId6094Compressor1BHoursExceeded": lgpCondId6094Compressor1BHoursExceeded,
       "lgpCondId6095Compressor2BHoursExceeded": lgpCondId6095Compressor2BHoursExceeded,
       "lgpCondId6100CondenserRemoteShutdown": lgpCondId6100CondenserRemoteShutdown,
       "lgpCondId6105ExternalCondenserTVSSIssue": lgpCondId6105ExternalCondenserTVSSIssue,
       "lgpCondId6106ExternalCondenserVFDIssue": lgpCondId6106ExternalCondenserVFDIssue,
       "lgpCondId6107ExternalCondenserIssue": lgpCondId6107ExternalCondenserIssue,
       "lgpCondId6119Slotsnotavailable": lgpCondId6119Slotsnotavailable,
       "lgpCondId6180BatteryUnderVoltage": lgpCondId6180BatteryUnderVoltage,
       "lgpCondId6182ReplaceBattery": lgpCondId6182ReplaceBattery,
       "lgpCondId6186InputFrequencyDeviation": lgpCondId6186InputFrequencyDeviation,
       "lgpCondId6187ShutdownPending": lgpCondId6187ShutdownPending,
       "lgpCondId6194SystemRebootCommandIssued": lgpCondId6194SystemRebootCommandIssued,
       "lgpCondId6203SensorAdded": lgpCondId6203SensorAdded,
       "lgpCondId6204SensorRemoved": lgpCondId6204SensorRemoved,
       "lgpCondId6205WaterLeakDetected": lgpCondId6205WaterLeakDetected,
       "lgpCondId6210FirmwareUpdateInProgress": lgpCondId6210FirmwareUpdateInProgress,
       "lgpCondId6211FirmwareUpdateCompletedSuccessfully": lgpCondId6211FirmwareUpdateCompletedSuccessfully,
       "lgpCondId6212FirmwareUpdateCompletedUnsuccessfully": lgpCondId6212FirmwareUpdateCompletedUnsuccessfully,
       "lgpCondId6216PrechargeCircuitFailed": lgpCondId6216PrechargeCircuitFailed,
       "lgpCondId6217MemoryCardRemoved": lgpCondId6217MemoryCardRemoved,
       "lgpCondId6218AutoCalibrationActive": lgpCondId6218AutoCalibrationActive,
       "lgpCondId6219AutoCalibrationFailed": lgpCondId6219AutoCalibrationFailed,
       "lgpCondId6220ModuleOutputBreakerOpen": lgpCondId6220ModuleOutputBreakerOpen,
       "lgpCondId6221NeutralVoltageFault": lgpCondId6221NeutralVoltageFault,
       "lgpCondId6222BranchLoadLoss": lgpCondId6222BranchLoadLoss,
       "lgpCondId6225RemoteSensorLowHumidity": lgpCondId6225RemoteSensorLowHumidity,
       "lgpCondId6226RemoteSensorHighHumidity": lgpCondId6226RemoteSensorHighHumidity,
       "lgpCondId6227RemoteSensorAverageLowHumidity": lgpCondId6227RemoteSensorAverageLowHumidity,
       "lgpCondId6228RemoteSensorAverageHighHumidity": lgpCondId6228RemoteSensorAverageHighHumidity,
       "lgpCondId6229RemoteSensorSystemAverageLowHumidity": lgpCondId6229RemoteSensorSystemAverageLowHumidity,
       "lgpCondId6230RemoteSensorSystemAverageHighHumidity": lgpCondId6230RemoteSensorSystemAverageHighHumidity,
       "lgpCondId6231LowCompressorSuperheat": lgpCondId6231LowCompressorSuperheat,
       "lgpCondId6232SECUnspecifiedGeneralEvent": lgpCondId6232SECUnspecifiedGeneralEvent,
       "lgpCondId6233SECCommunicationLost": lgpCondId6233SECCommunicationLost,
       "lgpCondId6236PowerSourceAIssue": lgpCondId6236PowerSourceAIssue,
       "lgpCondId6237PowerSourceBIssue": lgpCondId6237PowerSourceBIssue,
       "lgpCondId6239FluidValveHoursExceeded": lgpCondId6239FluidValveHoursExceeded,
       "lgpCondId6253BoosterFailure": lgpCondId6253BoosterFailure,
       "lgpCondId6254ChargerFailure": lgpCondId6254ChargerFailure,
       "lgpCondId6274UnitTopReturnAirSensorFailure": lgpCondId6274UnitTopReturnAirSensorFailure,
       "lgpCondId6275UnitMiddleReturnAirSensorFailure": lgpCondId6275UnitMiddleReturnAirSensorFailure,
       "lgpCondId6276UnitBottomReturnAirSensorFailure": lgpCondId6276UnitBottomReturnAirSensorFailure,
       "lgpCondId6277UnitTopSupplyAirSensorFailure": lgpCondId6277UnitTopSupplyAirSensorFailure,
       "lgpCondId6278UnitMiddleFirstSupplyAirSensorFailure": lgpCondId6278UnitMiddleFirstSupplyAirSensorFailure,
       "lgpCondId6279UnitBottomSupplyAirSensorFailure": lgpCondId6279UnitBottomSupplyAirSensorFailure,
       "lgpCondId6284UnitMiddleSecondSupplyAirSensorFailure": lgpCondId6284UnitMiddleSecondSupplyAirSensorFailure,
       "lgpCondId6293ChilledWaterControlActive": lgpCondId6293ChilledWaterControlActive,
       "lgpCondId6294ChilledWaterFlowTransducerFailure": lgpCondId6294ChilledWaterFlowTransducerFailure,
       "lgpCondId6295ChilledWaterInletTemperatureSensorFailure": lgpCondId6295ChilledWaterInletTemperatureSensorFailure,
       "lgpCondId6296ChilledWaterHighInletTemperature": lgpCondId6296ChilledWaterHighInletTemperature,
       "lgpCondId6297Modbus010VModuleCommunicationFailure": lgpCondId6297Modbus010VModuleCommunicationFailure,
       "lgpCondId6299RackDoorsOpen": lgpCondId6299RackDoorsOpen,
       "lgpCondId6303TeamStaticPressureSensorFailure": lgpCondId6303TeamStaticPressureSensorFailure,
       "lgpCondId6304HeatingLockout": lgpCondId6304HeatingLockout,
       "lgpCondId6305FreeCoolingStoppedHighRoomTemp": lgpCondId6305FreeCoolingStoppedHighRoomTemp,
       "lgpCondId6306ColdAisleTemperatureHumidityTeamSensorFailure": lgpCondId6306ColdAisleTemperatureHumidityTeamSensorFailure,
       "lgpCondId6309ColdAisleAirSensorFailure": lgpCondId6309ColdAisleAirSensorFailure,
       "lgpCondId6310ChilledWaterInletTemperatureControlActive": lgpCondId6310ChilledWaterInletTemperatureControlActive,
       "lgpCondId6313ChilledWaterInletTemperatureSensorFailure": lgpCondId6313ChilledWaterInletTemperatureSensorFailure,
       "lgpCondId6314ChilledWaterOutletTemperatureSensorFailure": lgpCondId6314ChilledWaterOutletTemperatureSensorFailure,
       "lgpCondId6315ChilledWaterFlowMeterSensorFailure": lgpCondId6315ChilledWaterFlowMeterSensorFailure,
       "lgpCondId6333Bypassoutofsync": lgpCondId6333Bypassoutofsync,
       "lgpCondId6348SystemOutputoffasrequested": lgpCondId6348SystemOutputoffasrequested,
       "lgpCondId6349SystemOffasrequested": lgpCondId6349SystemOffasrequested,
       "lgpCondId6350GeneralFault": lgpCondId6350GeneralFault,
       "lgpCondId6351UPSAwaitingPower": lgpCondId6351UPSAwaitingPower,
       "lgpCondId6352AutonomyCalibration": lgpCondId6352AutonomyCalibration,
       "lgpCondId6353GeneralWarning": lgpCondId6353GeneralWarning,
       "lgpCondId6354BatteryCharging": lgpCondId6354BatteryCharging,
       "lgpCondId6355BackfeedRelayFailure": lgpCondId6355BackfeedRelayFailure,
       "lgpCondId6356BatteryCircuitOpen": lgpCondId6356BatteryCircuitOpen,
       "lgpCondId6357SystemRestartPending": lgpCondId6357SystemRestartPending,
       "lgpCondId6358PipeTemperatureSensorFailure": lgpCondId6358PipeTemperatureSensorFailure,
       "lgpCondId6362SFAReservedEvent26": lgpCondId6362SFAReservedEvent26,
       "lgpCondId6363SFAReservedEvent27": lgpCondId6363SFAReservedEvent27,
       "lgpCondId6364SFAReservedEvent28": lgpCondId6364SFAReservedEvent28,
       "lgpCondId6365SFAReservedEvent29": lgpCondId6365SFAReservedEvent29,
       "lgpCondId6366SFAReservedEvent30": lgpCondId6366SFAReservedEvent30,
       "lgpCondId6367SFAReservedEvent31": lgpCondId6367SFAReservedEvent31,
       "lgpCondId6368SFAReservedEvent32": lgpCondId6368SFAReservedEvent32,
       "lgpCondId6369SFAReservedEvent33": lgpCondId6369SFAReservedEvent33,
       "lgpCondId6370SFAReservedEvent34": lgpCondId6370SFAReservedEvent34,
       "lgpCondId6371SFAReservedEvent35": lgpCondId6371SFAReservedEvent35,
       "lgpCondId6372SFAReservedEvent36": lgpCondId6372SFAReservedEvent36,
       "lgpCondId6373SFAReservedEvent37": lgpCondId6373SFAReservedEvent37,
       "lgpCondId6374SFAReservedEvent38": lgpCondId6374SFAReservedEvent38,
       "lgpCondId6375SFAReservedEvent39": lgpCondId6375SFAReservedEvent39,
       "lgpCondId6376SFAReservedEvent40": lgpCondId6376SFAReservedEvent40,
       "lgpCondId6377SFAReservedEvent41": lgpCondId6377SFAReservedEvent41,
       "lgpCondId6378SFAReservedEvent42": lgpCondId6378SFAReservedEvent42,
       "lgpCondId6379SFAReservedEvent43": lgpCondId6379SFAReservedEvent43,
       "lgpCondId6380SFAReservedEvent44": lgpCondId6380SFAReservedEvent44,
       "lgpCondId6381SFAReservedEvent45": lgpCondId6381SFAReservedEvent45,
       "lgpCondId6382SFAReservedEvent46": lgpCondId6382SFAReservedEvent46,
       "lgpCondId6383SFAReservedEvent47": lgpCondId6383SFAReservedEvent47,
       "lgpCondId6384SFAReservedEvent48": lgpCondId6384SFAReservedEvent48,
       "lgpCondId6385SFAReservedEvent49": lgpCondId6385SFAReservedEvent49,
       "lgpCondId6386SFAReservedEvent50": lgpCondId6386SFAReservedEvent50,
       "lgpCondId6438PowerModuleInputCurrentAbnormal": lgpCondId6438PowerModuleInputCurrentAbnormal,
       "lgpCondId6439PowerModuleBalancerofDCBusFailure": lgpCondId6439PowerModuleBalancerofDCBusFailure,
       "lgpCondId6440PowerModuleFuseFailure": lgpCondId6440PowerModuleFuseFailure,
       "lgpCondId6441PowerModulePowerSupplyFailure": lgpCondId6441PowerModulePowerSupplyFailure,
       "lgpCondId6450PDUPoweredOn": lgpCondId6450PDUPoweredOn,
       "lgpCondId6453InputWiringFault": lgpCondId6453InputWiringFault,
       "lgpCondId6454DCtoDCConverterFault": lgpCondId6454DCtoDCConverterFault,
       "lgpCondId6455LeakSensorCableFault": lgpCondId6455LeakSensorCableFault,
       "lgpCondId6518StandbyUnitActivatedDuetoChillerFailure": lgpCondId6518StandbyUnitActivatedDuetoChillerFailure}
)
