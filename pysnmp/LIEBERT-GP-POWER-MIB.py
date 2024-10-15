# SNMP MIB module (LIEBERT-GP-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-POWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:58 2024
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

(lgpPower,
 liebertPowerModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpPower",
    "liebertPowerModuleReg")

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

liebertGlobalProductsPowerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 6, 1)
)
liebertGlobalProductsPowerModule.setRevisions(
        ("2013-07-10 00:00",
         "2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpPwrBattery_ObjectIdentity = ObjectIdentity
lgpPwrBattery = _LgpPwrBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1)
)
if mibBuilder.loadTexts:
    lgpPwrBattery.setStatus("current")
_LgpPwrNumberInstalledBatteryModules_Type = Integer32
_LgpPwrNumberInstalledBatteryModules_Object = MibScalar
lgpPwrNumberInstalledBatteryModules = _LgpPwrNumberInstalledBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 1),
    _LgpPwrNumberInstalledBatteryModules_Type()
)
lgpPwrNumberInstalledBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberInstalledBatteryModules.setStatus("current")
_LgpPwrNumberFailedBatteryModules_Type = Integer32
_LgpPwrNumberFailedBatteryModules_Object = MibScalar
lgpPwrNumberFailedBatteryModules = _LgpPwrNumberFailedBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 2),
    _LgpPwrNumberFailedBatteryModules_Type()
)
lgpPwrNumberFailedBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberFailedBatteryModules.setStatus("current")
_LgpPwrNumberRedundantBatteryModules_Type = Integer32
_LgpPwrNumberRedundantBatteryModules_Object = MibScalar
lgpPwrNumberRedundantBatteryModules = _LgpPwrNumberRedundantBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 3),
    _LgpPwrNumberRedundantBatteryModules_Type()
)
lgpPwrNumberRedundantBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberRedundantBatteryModules.setStatus("current")
_LgpPwrNumberActiveBatteryModules_Type = Integer32
_LgpPwrNumberActiveBatteryModules_Object = MibScalar
lgpPwrNumberActiveBatteryModules = _LgpPwrNumberActiveBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 4),
    _LgpPwrNumberActiveBatteryModules_Type()
)
lgpPwrNumberActiveBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberActiveBatteryModules.setStatus("current")
_LgpPwrConfigLowBatteryWarningTime_Type = Integer32
_LgpPwrConfigLowBatteryWarningTime_Object = MibScalar
lgpPwrConfigLowBatteryWarningTime = _LgpPwrConfigLowBatteryWarningTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 5),
    _LgpPwrConfigLowBatteryWarningTime_Type()
)
lgpPwrConfigLowBatteryWarningTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrConfigLowBatteryWarningTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrConfigLowBatteryWarningTime.setUnits("minutes")
_LgpPwrNumberBatteryModuleWarnings_Type = Integer32
_LgpPwrNumberBatteryModuleWarnings_Object = MibScalar
lgpPwrNumberBatteryModuleWarnings = _LgpPwrNumberBatteryModuleWarnings_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 6),
    _LgpPwrNumberBatteryModuleWarnings_Type()
)
lgpPwrNumberBatteryModuleWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberBatteryModuleWarnings.setStatus("current")
_LgpPwrBatteryCount_Type = Integer32
_LgpPwrBatteryCount_Object = MibScalar
lgpPwrBatteryCount = _LgpPwrBatteryCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 7),
    _LgpPwrBatteryCount_Type()
)
lgpPwrBatteryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCount.setUnits("Count")


class _LgpPwrBatteryTestResult_Type(Integer32):
    """Custom type lgpPwrBatteryTestResult based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 4),
          ("inhibited", 6),
          ("passed", 2),
          ("systemFailure", 5),
          ("unknown", 1))
    )


_LgpPwrBatteryTestResult_Type.__name__ = "Integer32"
_LgpPwrBatteryTestResult_Object = MibScalar
lgpPwrBatteryTestResult = _LgpPwrBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 8),
    _LgpPwrBatteryTestResult_Type()
)
lgpPwrBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryTestResult.setStatus("current")
_LgpPwrNominalBatteryCapacity_Type = Integer32
_LgpPwrNominalBatteryCapacity_Object = MibScalar
lgpPwrNominalBatteryCapacity = _LgpPwrNominalBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 9),
    _LgpPwrNominalBatteryCapacity_Type()
)
lgpPwrNominalBatteryCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrNominalBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNominalBatteryCapacity.setUnits("minutes")
_LgpPwrBatteryFloatVoltage_Type = Integer32
_LgpPwrBatteryFloatVoltage_Object = MibScalar
lgpPwrBatteryFloatVoltage = _LgpPwrBatteryFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 10),
    _LgpPwrBatteryFloatVoltage_Type()
)
lgpPwrBatteryFloatVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryFloatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryFloatVoltage.setUnits("Volt")
_LgpPwrBatteryEndOfDischargeVoltage_Type = Integer32
_LgpPwrBatteryEndOfDischargeVoltage_Object = MibScalar
lgpPwrBatteryEndOfDischargeVoltage = _LgpPwrBatteryEndOfDischargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 11),
    _LgpPwrBatteryEndOfDischargeVoltage_Type()
)
lgpPwrBatteryEndOfDischargeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryEndOfDischargeVoltage.setStatus("current")
_LgpPwrAutomaticBatteryTestInterval_Type = Integer32
_LgpPwrAutomaticBatteryTestInterval_Object = MibScalar
lgpPwrAutomaticBatteryTestInterval = _LgpPwrAutomaticBatteryTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 12),
    _LgpPwrAutomaticBatteryTestInterval_Type()
)
lgpPwrAutomaticBatteryTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestInterval.setUnits("hours")
_LgpPwrAutomaticBatteryTestCountdown_Type = Integer32
_LgpPwrAutomaticBatteryTestCountdown_Object = MibScalar
lgpPwrAutomaticBatteryTestCountdown = _LgpPwrAutomaticBatteryTestCountdown_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 13),
    _LgpPwrAutomaticBatteryTestCountdown_Type()
)
lgpPwrAutomaticBatteryTestCountdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestCountdown.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestCountdown.setUnits("minutes")


class _LgpPwrBatteryChargeStatus_Type(Integer32):
    """Custom type lgpPwrBatteryChargeStatus based on Integer32"""
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
        *(("charging", 3),
          ("discharging", 4),
          ("fullycharged", 1),
          ("notfullycharged", 2))
    )


_LgpPwrBatteryChargeStatus_Type.__name__ = "Integer32"
_LgpPwrBatteryChargeStatus_Object = MibScalar
lgpPwrBatteryChargeStatus = _LgpPwrBatteryChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 14),
    _LgpPwrBatteryChargeStatus_Type()
)
lgpPwrBatteryChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryChargeStatus.setStatus("current")


class _LgpPwrBatteryLifeEnhancer_Type(Integer32):
    """Custom type lgpPwrBatteryLifeEnhancer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrBatteryLifeEnhancer_Type.__name__ = "Integer32"
_LgpPwrBatteryLifeEnhancer_Object = MibScalar
lgpPwrBatteryLifeEnhancer = _LgpPwrBatteryLifeEnhancer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 15),
    _LgpPwrBatteryLifeEnhancer_Type()
)
lgpPwrBatteryLifeEnhancer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryLifeEnhancer.setStatus("current")


class _LgpPwrBatteryCharger_Type(Integer32):
    """Custom type lgpPwrBatteryCharger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrBatteryCharger_Type.__name__ = "Integer32"
_LgpPwrBatteryCharger_Object = MibScalar
lgpPwrBatteryCharger = _LgpPwrBatteryCharger_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 16),
    _LgpPwrBatteryCharger_Type()
)
lgpPwrBatteryCharger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCharger.setStatus("current")


class _LgpPwrBatteryChargeMode_Type(Integer32):
    """Custom type lgpPwrBatteryChargeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equalize", 2),
          ("float", 1))
    )


_LgpPwrBatteryChargeMode_Type.__name__ = "Integer32"
_LgpPwrBatteryChargeMode_Object = MibScalar
lgpPwrBatteryChargeMode = _LgpPwrBatteryChargeMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 17),
    _LgpPwrBatteryChargeMode_Type()
)
lgpPwrBatteryChargeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryChargeMode.setStatus("current")
_LgpPwrBatteryTimeRemaining_Type = Integer32
_LgpPwrBatteryTimeRemaining_Object = MibScalar
lgpPwrBatteryTimeRemaining = _LgpPwrBatteryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 18),
    _LgpPwrBatteryTimeRemaining_Type()
)
lgpPwrBatteryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryTimeRemaining.setUnits("minutes")
_LgpPwrBatteryCapacity_Type = Integer32
_LgpPwrBatteryCapacity_Object = MibScalar
lgpPwrBatteryCapacity = _LgpPwrBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 19),
    _LgpPwrBatteryCapacity_Type()
)
lgpPwrBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCapacity.setUnits("percent")
_LgpPwrBatteryCabinet_ObjectIdentity = ObjectIdentity
lgpPwrBatteryCabinet = _LgpPwrBatteryCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20)
)
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinet.setStatus("current")
_LgpPwrBatteryCabinetCount_Type = Integer32
_LgpPwrBatteryCabinetCount_Object = MibScalar
lgpPwrBatteryCabinetCount = _LgpPwrBatteryCabinetCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 1),
    _LgpPwrBatteryCabinetCount_Type()
)
lgpPwrBatteryCabinetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetCount.setUnits("Count")


class _LgpPwrBatteryCabinetType_Type(Integer32):
    """Custom type lgpPwrBatteryCabinetType based on Integer32"""
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
        *(("external", 3),
          ("internal", 2),
          ("lrt", 4),
          ("notSpecified", 1))
    )


_LgpPwrBatteryCabinetType_Type.__name__ = "Integer32"
_LgpPwrBatteryCabinetType_Object = MibScalar
lgpPwrBatteryCabinetType = _LgpPwrBatteryCabinetType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 2),
    _LgpPwrBatteryCabinetType_Type()
)
lgpPwrBatteryCabinetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetType.setStatus("current")
_LgpPwrBatteryCabinetRatedCapacity_Type = Integer32
_LgpPwrBatteryCabinetRatedCapacity_Object = MibScalar
lgpPwrBatteryCabinetRatedCapacity = _LgpPwrBatteryCabinetRatedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 3),
    _LgpPwrBatteryCabinetRatedCapacity_Type()
)
lgpPwrBatteryCabinetRatedCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetRatedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetRatedCapacity.setUnits("0.1 Amp-hour")
_LgpPwrBatteryLeadAcidCellCount_Type = Integer32
_LgpPwrBatteryLeadAcidCellCount_Object = MibScalar
lgpPwrBatteryLeadAcidCellCount = _LgpPwrBatteryLeadAcidCellCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 4),
    _LgpPwrBatteryLeadAcidCellCount_Type()
)
lgpPwrBatteryLeadAcidCellCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryLeadAcidCellCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryLeadAcidCellCount.setUnits("Count")
_LgpPwrBatteryNiCadCellCount_Type = Integer32
_LgpPwrBatteryNiCadCellCount_Object = MibScalar
lgpPwrBatteryNiCadCellCount = _LgpPwrBatteryNiCadCellCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 5),
    _LgpPwrBatteryNiCadCellCount_Type()
)
lgpPwrBatteryNiCadCellCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryNiCadCellCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryNiCadCellCount.setUnits("Count")
_LgpPwrBatteryAmpHoursConsumed_Type = Integer32
_LgpPwrBatteryAmpHoursConsumed_Object = MibScalar
lgpPwrBatteryAmpHoursConsumed = _LgpPwrBatteryAmpHoursConsumed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 21),
    _LgpPwrBatteryAmpHoursConsumed_Type()
)
lgpPwrBatteryAmpHoursConsumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursConsumed.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursConsumed.setUnits("Amp-hour")
_LgpPwrBatteryAmpHoursDischargeConsumed_Type = Integer32
_LgpPwrBatteryAmpHoursDischargeConsumed_Object = MibScalar
lgpPwrBatteryAmpHoursDischargeConsumed = _LgpPwrBatteryAmpHoursDischargeConsumed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 22),
    _LgpPwrBatteryAmpHoursDischargeConsumed_Type()
)
lgpPwrBatteryAmpHoursDischargeConsumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursDischargeConsumed.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursDischargeConsumed.setUnits("Amp-hour")
_LgpPwrBatteryLastDischargeTime_Type = Unsigned32
_LgpPwrBatteryLastDischargeTime_Object = MibScalar
lgpPwrBatteryLastDischargeTime = _LgpPwrBatteryLastDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 23),
    _LgpPwrBatteryLastDischargeTime_Type()
)
lgpPwrBatteryLastDischargeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastDischargeTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastDischargeTime.setUnits("seconds")
_LgpPwrBatteryLastCommissionTime_Type = Unsigned32
_LgpPwrBatteryLastCommissionTime_Object = MibScalar
lgpPwrBatteryLastCommissionTime = _LgpPwrBatteryLastCommissionTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 24),
    _LgpPwrBatteryLastCommissionTime_Type()
)
lgpPwrBatteryLastCommissionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastCommissionTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastCommissionTime.setUnits("seconds")
_LgpPwrBatteryPresentDischargeTime_Type = Integer32
_LgpPwrBatteryPresentDischargeTime_Object = MibScalar
lgpPwrBatteryPresentDischargeTime = _LgpPwrBatteryPresentDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 25),
    _LgpPwrBatteryPresentDischargeTime_Type()
)
lgpPwrBatteryPresentDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryPresentDischargeTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryPresentDischargeTime.setUnits("seconds")


class _LgpPwrBatteryCapacityStatus_Type(Integer32):
    """Custom type lgpPwrBatteryCapacityStatus based on Integer32"""
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
        *(("batteryDepleted", 4),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_LgpPwrBatteryCapacityStatus_Type.__name__ = "Integer32"
_LgpPwrBatteryCapacityStatus_Object = MibScalar
lgpPwrBatteryCapacityStatus = _LgpPwrBatteryCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 26),
    _LgpPwrBatteryCapacityStatus_Type()
)
lgpPwrBatteryCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCapacityStatus.setStatus("current")


class _LgpPwrBatteryCircuitBreakerState_Type(Integer32):
    """Custom type lgpPwrBatteryCircuitBreakerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1),
          ("unknown", 0))
    )


_LgpPwrBatteryCircuitBreakerState_Type.__name__ = "Integer32"
_LgpPwrBatteryCircuitBreakerState_Object = MibScalar
lgpPwrBatteryCircuitBreakerState = _LgpPwrBatteryCircuitBreakerState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 27),
    _LgpPwrBatteryCircuitBreakerState_Type()
)
lgpPwrBatteryCircuitBreakerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCircuitBreakerState.setStatus("current")
_LgpPwrMeasurements_ObjectIdentity = ObjectIdentity
lgpPwrMeasurements = _LgpPwrMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2)
)
if mibBuilder.loadTexts:
    lgpPwrMeasurements.setStatus("current")
_LgpPwrWellKnownMeasurementPoints_ObjectIdentity = ObjectIdentity
lgpPwrWellKnownMeasurementPoints = _LgpPwrWellKnownMeasurementPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lgpPwrWellKnownMeasurementPoints.setStatus("current")
_LgpPwrSource1Input_ObjectIdentity = ObjectIdentity
lgpPwrSource1Input = _LgpPwrSource1Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lgpPwrSource1Input.setStatus("current")
_LgpPwrSource2Input_ObjectIdentity = ObjectIdentity
lgpPwrSource2Input = _LgpPwrSource2Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgpPwrSource2Input.setStatus("current")
_LgpPwrSourcePdu1Input_ObjectIdentity = ObjectIdentity
lgpPwrSourcePdu1Input = _LgpPwrSourcePdu1Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lgpPwrSourcePdu1Input.setStatus("current")
_LgpPwrSourcePdu2Input_ObjectIdentity = ObjectIdentity
lgpPwrSourcePdu2Input = _LgpPwrSourcePdu2Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lgpPwrSourcePdu2Input.setStatus("current")
_LgpPwrOutputToLoad_ObjectIdentity = ObjectIdentity
lgpPwrOutputToLoad = _LgpPwrOutputToLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lgpPwrOutputToLoad.setStatus("current")
_LgpPwrMeasBattery_ObjectIdentity = ObjectIdentity
lgpPwrMeasBattery = _LgpPwrMeasBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    lgpPwrMeasBattery.setStatus("current")
_LgpPwrMeasBypass_ObjectIdentity = ObjectIdentity
lgpPwrMeasBypass = _LgpPwrMeasBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    lgpPwrMeasBypass.setStatus("current")
_LgpPwrMeasDcBus_ObjectIdentity = ObjectIdentity
lgpPwrMeasDcBus = _LgpPwrMeasDcBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    lgpPwrMeasDcBus.setStatus("current")
_LgpPwrMeasSystemOutput_ObjectIdentity = ObjectIdentity
lgpPwrMeasSystemOutput = _LgpPwrMeasSystemOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    lgpPwrMeasSystemOutput.setStatus("current")
_LgpPwrMeasBatteryCabinet_ObjectIdentity = ObjectIdentity
lgpPwrMeasBatteryCabinet = _LgpPwrMeasBatteryCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    lgpPwrMeasBatteryCabinet.setStatus("current")
_LgpPwrMeasurementPointTable_Object = MibTable
lgpPwrMeasurementPointTable = _LgpPwrMeasurementPointTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointTable.setStatus("current")
_LgpPwrMeasurementPointEntry_Object = MibTableRow
lgpPwrMeasurementPointEntry = _LgpPwrMeasurementPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1)
)
lgpPwrMeasurementPointEntry.setIndexNames(
    (0, "LIEBERT-GP-POWER-MIB", "lgpPwrMeasurementPointIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointEntry.setStatus("current")
_LgpPwrMeasurementPointIndex_Type = Unsigned32
_LgpPwrMeasurementPointIndex_Object = MibTableColumn
lgpPwrMeasurementPointIndex = _LgpPwrMeasurementPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 1),
    _LgpPwrMeasurementPointIndex_Type()
)
lgpPwrMeasurementPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointIndex.setStatus("current")
_LgpPwrMeasurementPointId_Type = ObjectIdentifier
_LgpPwrMeasurementPointId_Object = MibTableColumn
lgpPwrMeasurementPointId = _LgpPwrMeasurementPointId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 2),
    _LgpPwrMeasurementPointId_Type()
)
lgpPwrMeasurementPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointId.setStatus("current")
_LgpPwrMeasurementPointNumLines_Type = Integer32
_LgpPwrMeasurementPointNumLines_Object = MibTableColumn
lgpPwrMeasurementPointNumLines = _LgpPwrMeasurementPointNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 3),
    _LgpPwrMeasurementPointNumLines_Type()
)
lgpPwrMeasurementPointNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNumLines.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNumLines.setUnits("Count")
_LgpPwrMeasurementPointNomVolts_Type = Integer32
_LgpPwrMeasurementPointNomVolts_Object = MibTableColumn
lgpPwrMeasurementPointNomVolts = _LgpPwrMeasurementPointNomVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 4),
    _LgpPwrMeasurementPointNomVolts_Type()
)
lgpPwrMeasurementPointNomVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVolts.setUnits("Volt")
_LgpPwrMeasurementPointNomFrequency_Type = Integer32
_LgpPwrMeasurementPointNomFrequency_Object = MibTableColumn
lgpPwrMeasurementPointNomFrequency = _LgpPwrMeasurementPointNomFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 5),
    _LgpPwrMeasurementPointNomFrequency_Type()
)
lgpPwrMeasurementPointNomFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomFrequency.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomFrequency.setUnits("Hertz")
_LgpPwrMeasurementPointFrequency_Type = Integer32
_LgpPwrMeasurementPointFrequency_Object = MibTableColumn
lgpPwrMeasurementPointFrequency = _LgpPwrMeasurementPointFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 6),
    _LgpPwrMeasurementPointFrequency_Type()
)
lgpPwrMeasurementPointFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointFrequency.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointFrequency.setUnits("Hertz")
_LgpPwrMeasurementPointApparentPower_Type = Integer32
_LgpPwrMeasurementPointApparentPower_Object = MibTableColumn
lgpPwrMeasurementPointApparentPower = _LgpPwrMeasurementPointApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 7),
    _LgpPwrMeasurementPointApparentPower_Type()
)
lgpPwrMeasurementPointApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointApparentPower.setUnits("Volt-Amp")
_LgpPwrMeasurementPointTruePower_Type = Integer32
_LgpPwrMeasurementPointTruePower_Object = MibTableColumn
lgpPwrMeasurementPointTruePower = _LgpPwrMeasurementPointTruePower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 8),
    _LgpPwrMeasurementPointTruePower_Type()
)
lgpPwrMeasurementPointTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointTruePower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointTruePower.setUnits("Watt")
_LgpPwrMeasurementPointPowerFactor_Type = Integer32
_LgpPwrMeasurementPointPowerFactor_Object = MibTableColumn
lgpPwrMeasurementPointPowerFactor = _LgpPwrMeasurementPointPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 9),
    _LgpPwrMeasurementPointPowerFactor_Type()
)
lgpPwrMeasurementPointPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointPowerFactor.setUnits(".01 Power Factor")
_LgpPwrMeasurementPointWattHours_Type = Integer32
_LgpPwrMeasurementPointWattHours_Object = MibTableColumn
lgpPwrMeasurementPointWattHours = _LgpPwrMeasurementPointWattHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 10),
    _LgpPwrMeasurementPointWattHours_Type()
)
lgpPwrMeasurementPointWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointWattHours.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointWattHours.setUnits("Watt-Hour")
_LgpPwrMeasurementPointVAPercent_Type = Integer32
_LgpPwrMeasurementPointVAPercent_Object = MibTableColumn
lgpPwrMeasurementPointVAPercent = _LgpPwrMeasurementPointVAPercent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 11),
    _LgpPwrMeasurementPointVAPercent_Type()
)
lgpPwrMeasurementPointVAPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointVAPercent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointVAPercent.setUnits("0.1 Percent")
_LgpPwrMeasurementPointNeutralCurrent_Type = Integer32
_LgpPwrMeasurementPointNeutralCurrent_Object = MibTableColumn
lgpPwrMeasurementPointNeutralCurrent = _LgpPwrMeasurementPointNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 12),
    _LgpPwrMeasurementPointNeutralCurrent_Type()
)
lgpPwrMeasurementPointNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNeutralCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNeutralCurrent.setUnits("Amp")
_LgpPwrMeasurementPointGroundCurrent_Type = Integer32
_LgpPwrMeasurementPointGroundCurrent_Object = MibTableColumn
lgpPwrMeasurementPointGroundCurrent = _LgpPwrMeasurementPointGroundCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 13),
    _LgpPwrMeasurementPointGroundCurrent_Type()
)
lgpPwrMeasurementPointGroundCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointGroundCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointGroundCurrent.setUnits("0.1 Amp")
_LgpPwrMeasurementPointNomCurrent_Type = Integer32
_LgpPwrMeasurementPointNomCurrent_Object = MibTableColumn
lgpPwrMeasurementPointNomCurrent = _LgpPwrMeasurementPointNomCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 14),
    _LgpPwrMeasurementPointNomCurrent_Type()
)
lgpPwrMeasurementPointNomCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomCurrent.setUnits("0.1 Amp")
_LgpPwrMeasurementPointNomPowerFactor_Type = Integer32
_LgpPwrMeasurementPointNomPowerFactor_Object = MibTableColumn
lgpPwrMeasurementPointNomPowerFactor = _LgpPwrMeasurementPointNomPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 15),
    _LgpPwrMeasurementPointNomPowerFactor_Type()
)
lgpPwrMeasurementPointNomPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomPowerFactor.setUnits(".01 Power Factor")
_LgpPwrMeasurementPointNomVA_Type = Integer32
_LgpPwrMeasurementPointNomVA_Object = MibTableColumn
lgpPwrMeasurementPointNomVA = _LgpPwrMeasurementPointNomVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 16),
    _LgpPwrMeasurementPointNomVA_Type()
)
lgpPwrMeasurementPointNomVA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVA.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVA.setUnits("Volt-Amp")
_LgpPwrMeasurementPointNomW_Type = Integer32
_LgpPwrMeasurementPointNomW_Object = MibTableColumn
lgpPwrMeasurementPointNomW = _LgpPwrMeasurementPointNomW_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 17),
    _LgpPwrMeasurementPointNomW_Type()
)
lgpPwrMeasurementPointNomW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomW.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomW.setUnits("Watt")


class _LgpPwrMeasurementPointPowerFactorTag_Type(Integer32):
    """Custom type lgpPwrMeasurementPointPowerFactorTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lagging", 2),
          ("leading", 1))
    )


_LgpPwrMeasurementPointPowerFactorTag_Type.__name__ = "Integer32"
_LgpPwrMeasurementPointPowerFactorTag_Object = MibTableColumn
lgpPwrMeasurementPointPowerFactorTag = _LgpPwrMeasurementPointPowerFactorTag_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 19),
    _LgpPwrMeasurementPointPowerFactorTag_Type()
)
lgpPwrMeasurementPointPowerFactorTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointPowerFactorTag.setStatus("current")
_LgpPwrLineMeasurementTable_Object = MibTable
lgpPwrLineMeasurementTable = _LgpPwrLineMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3)
)
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementTable.setStatus("current")
_LgpPwrLineMeasurementEntry_Object = MibTableRow
lgpPwrLineMeasurementEntry = _LgpPwrLineMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1)
)
lgpPwrLineMeasurementEntry.setIndexNames(
    (0, "LIEBERT-GP-POWER-MIB", "lgpPwrMeasurementPtIndex"),
    (0, "LIEBERT-GP-POWER-MIB", "lgpPwrLineMeasurementIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementEntry.setStatus("current")
_LgpPwrMeasurementPtIndex_Type = Unsigned32
_LgpPwrMeasurementPtIndex_Object = MibTableColumn
lgpPwrMeasurementPtIndex = _LgpPwrMeasurementPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 1),
    _LgpPwrMeasurementPtIndex_Type()
)
lgpPwrMeasurementPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPtIndex.setStatus("current")
_LgpPwrLineMeasurementIndex_Type = Unsigned32
_LgpPwrLineMeasurementIndex_Object = MibTableColumn
lgpPwrLineMeasurementIndex = _LgpPwrLineMeasurementIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 2),
    _LgpPwrLineMeasurementIndex_Type()
)
lgpPwrLineMeasurementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementIndex.setStatus("current")
_LgpPwrMeasurementPoint_Type = ObjectIdentifier
_LgpPwrMeasurementPoint_Object = MibTableColumn
lgpPwrMeasurementPoint = _LgpPwrMeasurementPoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 3),
    _LgpPwrMeasurementPoint_Type()
)
lgpPwrMeasurementPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPoint.setStatus("current")
_LgpPwrLineMeasurementVoltsLL_Type = Integer32
_LgpPwrLineMeasurementVoltsLL_Object = MibTableColumn
lgpPwrLineMeasurementVoltsLL = _LgpPwrLineMeasurementVoltsLL_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 4),
    _LgpPwrLineMeasurementVoltsLL_Type()
)
lgpPwrLineMeasurementVoltsLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLL.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLL.setUnits("Volt")
_LgpPwrLineMeasurementVoltsLN_Type = Integer32
_LgpPwrLineMeasurementVoltsLN_Object = MibTableColumn
lgpPwrLineMeasurementVoltsLN = _LgpPwrLineMeasurementVoltsLN_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 5),
    _LgpPwrLineMeasurementVoltsLN_Type()
)
lgpPwrLineMeasurementVoltsLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLN.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLN.setUnits("Volt")
_LgpPwrLineMeasurementCurrent_Type = Integer32
_LgpPwrLineMeasurementCurrent_Object = MibTableColumn
lgpPwrLineMeasurementCurrent = _LgpPwrLineMeasurementCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 6),
    _LgpPwrLineMeasurementCurrent_Type()
)
lgpPwrLineMeasurementCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrent.setUnits("Amp")
_LgpPwrLineMeasurementCapacity_Type = Integer32
_LgpPwrLineMeasurementCapacity_Object = MibTableColumn
lgpPwrLineMeasurementCapacity = _LgpPwrLineMeasurementCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 7),
    _LgpPwrLineMeasurementCapacity_Type()
)
lgpPwrLineMeasurementCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCapacity.setUnits("percent")
_LgpPwrLineMeasurementVA_Type = Integer32
_LgpPwrLineMeasurementVA_Object = MibTableColumn
lgpPwrLineMeasurementVA = _LgpPwrLineMeasurementVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 8),
    _LgpPwrLineMeasurementVA_Type()
)
lgpPwrLineMeasurementVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVA.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVA.setUnits("Volt-Amp")
_LgpPwrLineMeasurementTruePower_Type = Integer32
_LgpPwrLineMeasurementTruePower_Object = MibTableColumn
lgpPwrLineMeasurementTruePower = _LgpPwrLineMeasurementTruePower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 9),
    _LgpPwrLineMeasurementTruePower_Type()
)
lgpPwrLineMeasurementTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementTruePower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementTruePower.setUnits("Watt")
_LgpPwrLineMeasurementVoltageTHD_Type = Integer32
_LgpPwrLineMeasurementVoltageTHD_Object = MibTableColumn
lgpPwrLineMeasurementVoltageTHD = _LgpPwrLineMeasurementVoltageTHD_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 10),
    _LgpPwrLineMeasurementVoltageTHD_Type()
)
lgpPwrLineMeasurementVoltageTHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltageTHD.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltageTHD.setUnits("0.1 Percent")
_LgpPwrLineMeasurementCurrentTHD_Type = Integer32
_LgpPwrLineMeasurementCurrentTHD_Object = MibTableColumn
lgpPwrLineMeasurementCurrentTHD = _LgpPwrLineMeasurementCurrentTHD_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 11),
    _LgpPwrLineMeasurementCurrentTHD_Type()
)
lgpPwrLineMeasurementCurrentTHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrentTHD.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrentTHD.setUnits("0.1 Percent")
_LgpPwrLineMeasurementKFactorCurrent_Type = Integer32
_LgpPwrLineMeasurementKFactorCurrent_Object = MibTableColumn
lgpPwrLineMeasurementKFactorCurrent = _LgpPwrLineMeasurementKFactorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 12),
    _LgpPwrLineMeasurementKFactorCurrent_Type()
)
lgpPwrLineMeasurementKFactorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementKFactorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementKFactorCurrent.setUnits("0.1 K Factor")
_LgpPwrLineMeasurementCrestFactorCurrent_Type = Integer32
_LgpPwrLineMeasurementCrestFactorCurrent_Object = MibTableColumn
lgpPwrLineMeasurementCrestFactorCurrent = _LgpPwrLineMeasurementCrestFactorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 13),
    _LgpPwrLineMeasurementCrestFactorCurrent_Type()
)
lgpPwrLineMeasurementCrestFactorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCrestFactorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCrestFactorCurrent.setUnits("0.1 Crest Factor")
_LgpPwrLineMeasurementPowerFactor_Type = Integer32
_LgpPwrLineMeasurementPowerFactor_Object = MibTableColumn
lgpPwrLineMeasurementPowerFactor = _LgpPwrLineMeasurementPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 14),
    _LgpPwrLineMeasurementPowerFactor_Type()
)
lgpPwrLineMeasurementPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPowerFactor.setUnits("0.01 Power Factor")


class _LgpPwrLineMeasurementPowerFactorTag_Type(Integer32):
    """Custom type lgpPwrLineMeasurementPowerFactorTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lagging", 2),
          ("leading", 1))
    )


_LgpPwrLineMeasurementPowerFactorTag_Type.__name__ = "Integer32"
_LgpPwrLineMeasurementPowerFactorTag_Object = MibTableColumn
lgpPwrLineMeasurementPowerFactorTag = _LgpPwrLineMeasurementPowerFactorTag_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 15),
    _LgpPwrLineMeasurementPowerFactorTag_Type()
)
lgpPwrLineMeasurementPowerFactorTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPowerFactorTag.setStatus("current")
_LgpPwrLineMeasurementMaxVolts_Type = Integer32
_LgpPwrLineMeasurementMaxVolts_Object = MibTableColumn
lgpPwrLineMeasurementMaxVolts = _LgpPwrLineMeasurementMaxVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 16),
    _LgpPwrLineMeasurementMaxVolts_Type()
)
lgpPwrLineMeasurementMaxVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMaxVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMaxVolts.setUnits("Volt")
_LgpPwrLineMeasurementMinVolts_Type = Integer32
_LgpPwrLineMeasurementMinVolts_Object = MibTableColumn
lgpPwrLineMeasurementMinVolts = _LgpPwrLineMeasurementMinVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 17),
    _LgpPwrLineMeasurementMinVolts_Type()
)
lgpPwrLineMeasurementMinVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMinVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMinVolts.setUnits("Volt")
_LgpPwrLineMeasurementVAR_Type = Integer32
_LgpPwrLineMeasurementVAR_Object = MibTableColumn
lgpPwrLineMeasurementVAR = _LgpPwrLineMeasurementVAR_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 18),
    _LgpPwrLineMeasurementVAR_Type()
)
lgpPwrLineMeasurementVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVAR.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVAR.setUnits("Volt-Amp-Reactive")
_LgpPwrLineMeasurementPercentLoad_Type = Integer32
_LgpPwrLineMeasurementPercentLoad_Object = MibTableColumn
lgpPwrLineMeasurementPercentLoad = _LgpPwrLineMeasurementPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 19),
    _LgpPwrLineMeasurementPercentLoad_Type()
)
lgpPwrLineMeasurementPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPercentLoad.setUnits("percent")
_LgpPwrLineMeasurementVolts_Type = Integer32
_LgpPwrLineMeasurementVolts_Object = MibTableColumn
lgpPwrLineMeasurementVolts = _LgpPwrLineMeasurementVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 20),
    _LgpPwrLineMeasurementVolts_Type()
)
lgpPwrLineMeasurementVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVolts.setUnits("Volt")
_LgpPwrLineMeasurementVACapacity_Type = Integer32
_LgpPwrLineMeasurementVACapacity_Object = MibTableColumn
lgpPwrLineMeasurementVACapacity = _LgpPwrLineMeasurementVACapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 21),
    _LgpPwrLineMeasurementVACapacity_Type()
)
lgpPwrLineMeasurementVACapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVACapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVACapacity.setUnits("percent")
_LgpPwrDcMeasurementPointTable_Object = MibTable
lgpPwrDcMeasurementPointTable = _LgpPwrDcMeasurementPointTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointTable.setStatus("current")
_LgpPwrDcMeasurementPointEntry_Object = MibTableRow
lgpPwrDcMeasurementPointEntry = _LgpPwrDcMeasurementPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1)
)
lgpPwrDcMeasurementPointEntry.setIndexNames(
    (0, "LIEBERT-GP-POWER-MIB", "lgpPwrDcMeasurementPointIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointEntry.setStatus("current")
_LgpPwrDcMeasurementPointIndex_Type = Unsigned32
_LgpPwrDcMeasurementPointIndex_Object = MibTableColumn
lgpPwrDcMeasurementPointIndex = _LgpPwrDcMeasurementPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 1),
    _LgpPwrDcMeasurementPointIndex_Type()
)
lgpPwrDcMeasurementPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointIndex.setStatus("current")
_LgpPwrDcMeasurementPointId_Type = ObjectIdentifier
_LgpPwrDcMeasurementPointId_Object = MibTableColumn
lgpPwrDcMeasurementPointId = _LgpPwrDcMeasurementPointId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 2),
    _LgpPwrDcMeasurementPointId_Type()
)
lgpPwrDcMeasurementPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointId.setStatus("current")
_LgpPwrDcMeasurementPointSubID_Type = Integer32
_LgpPwrDcMeasurementPointSubID_Object = MibTableColumn
lgpPwrDcMeasurementPointSubID = _LgpPwrDcMeasurementPointSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 3),
    _LgpPwrDcMeasurementPointSubID_Type()
)
lgpPwrDcMeasurementPointSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointSubID.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointSubID.setUnits("Count")
_LgpPwrDcMeasurementPointVolts_Type = Integer32
_LgpPwrDcMeasurementPointVolts_Object = MibTableColumn
lgpPwrDcMeasurementPointVolts = _LgpPwrDcMeasurementPointVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 4),
    _LgpPwrDcMeasurementPointVolts_Type()
)
lgpPwrDcMeasurementPointVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointVolts.setUnits("Volt")
_LgpPwrDcMeasurementPointCurrent_Type = Integer32
_LgpPwrDcMeasurementPointCurrent_Object = MibTableColumn
lgpPwrDcMeasurementPointCurrent = _LgpPwrDcMeasurementPointCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 5),
    _LgpPwrDcMeasurementPointCurrent_Type()
)
lgpPwrDcMeasurementPointCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointCurrent.setUnits("Amp")
_LgpPwrDcMeasurementPointNomVolts_Type = Integer32
_LgpPwrDcMeasurementPointNomVolts_Object = MibTableColumn
lgpPwrDcMeasurementPointNomVolts = _LgpPwrDcMeasurementPointNomVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 6),
    _LgpPwrDcMeasurementPointNomVolts_Type()
)
lgpPwrDcMeasurementPointNomVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointNomVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointNomVolts.setUnits("Volt")
_LgpPwrDcMeasurementPointTruePower_Type = Integer32
_LgpPwrDcMeasurementPointTruePower_Object = MibTableColumn
lgpPwrDcMeasurementPointTruePower = _LgpPwrDcMeasurementPointTruePower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 7),
    _LgpPwrDcMeasurementPointTruePower_Type()
)
lgpPwrDcMeasurementPointTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointTruePower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointTruePower.setUnits("Watt")
_LgpPwrWellKnownMeasurementTypes_ObjectIdentity = ObjectIdentity
lgpPwrWellKnownMeasurementTypes = _LgpPwrWellKnownMeasurementTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5)
)
if mibBuilder.loadTexts:
    lgpPwrWellKnownMeasurementTypes.setStatus("current")
_LgpPwrVoltsAc_ObjectIdentity = ObjectIdentity
lgpPwrVoltsAc = _LgpPwrVoltsAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lgpPwrVoltsAc.setStatus("current")
_LgpPwrVoltsDc_ObjectIdentity = ObjectIdentity
lgpPwrVoltsDc = _LgpPwrVoltsDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    lgpPwrVoltsDc.setStatus("current")
_LgpPwrAmpsNeutral_ObjectIdentity = ObjectIdentity
lgpPwrAmpsNeutral = _LgpPwrAmpsNeutral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5, 3)
)
if mibBuilder.loadTexts:
    lgpPwrAmpsNeutral.setStatus("current")
_LgpPwrStatus_ObjectIdentity = ObjectIdentity
lgpPwrStatus = _LgpPwrStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3)
)
if mibBuilder.loadTexts:
    lgpPwrStatus.setStatus("current")
_LgpPwrTransferCount_Type = Integer32
_LgpPwrTransferCount_Object = MibScalar
lgpPwrTransferCount = _LgpPwrTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 1),
    _LgpPwrTransferCount_Type()
)
lgpPwrTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTransferCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrTransferCount.setUnits("Count")
_LgpPwrAutoTransferTimer_Type = Integer32
_LgpPwrAutoTransferTimer_Object = MibScalar
lgpPwrAutoTransferTimer = _LgpPwrAutoTransferTimer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 2),
    _LgpPwrAutoTransferTimer_Type()
)
lgpPwrAutoTransferTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrAutoTransferTimer.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutoTransferTimer.setUnits("seconds")


class _LgpPwrAutoReTransferEnabled_Type(Integer32):
    """Custom type lgpPwrAutoReTransferEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LgpPwrAutoReTransferEnabled_Type.__name__ = "Integer32"
_LgpPwrAutoReTransferEnabled_Object = MibScalar
lgpPwrAutoReTransferEnabled = _LgpPwrAutoReTransferEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 3),
    _LgpPwrAutoReTransferEnabled_Type()
)
lgpPwrAutoReTransferEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrAutoReTransferEnabled.setStatus("current")


class _LgpPwrSyncPhaseAngle_Type(Integer32):
    """Custom type lgpPwrSyncPhaseAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3600, 3600),
    )


_LgpPwrSyncPhaseAngle_Type.__name__ = "Integer32"
_LgpPwrSyncPhaseAngle_Object = MibScalar
lgpPwrSyncPhaseAngle = _LgpPwrSyncPhaseAngle_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 4),
    _LgpPwrSyncPhaseAngle_Type()
)
lgpPwrSyncPhaseAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrSyncPhaseAngle.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrSyncPhaseAngle.setUnits("0.1 Degrees")


class _LgpPwrParallelSystemOutputToLoadSource_Type(Integer32):
    """Custom type lgpPwrParallelSystemOutputToLoadSource based on Integer32"""
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
        *(("battery", 2),
          ("bypass", 3),
          ("none", 4),
          ("unknown", 0),
          ("utility", 1))
    )


_LgpPwrParallelSystemOutputToLoadSource_Type.__name__ = "Integer32"
_LgpPwrParallelSystemOutputToLoadSource_Object = MibScalar
lgpPwrParallelSystemOutputToLoadSource = _LgpPwrParallelSystemOutputToLoadSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 5),
    _LgpPwrParallelSystemOutputToLoadSource_Type()
)
lgpPwrParallelSystemOutputToLoadSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrParallelSystemOutputToLoadSource.setStatus("current")


class _LgpPwrDcToDcConverter_Type(Integer32):
    """Custom type lgpPwrDcToDcConverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrDcToDcConverter_Type.__name__ = "Integer32"
_LgpPwrDcToDcConverter_Object = MibScalar
lgpPwrDcToDcConverter = _LgpPwrDcToDcConverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 6),
    _LgpPwrDcToDcConverter_Type()
)
lgpPwrDcToDcConverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcToDcConverter.setStatus("current")


class _LgpPwrOutputToLoadOnInverter_Type(Integer32):
    """Custom type lgpPwrOutputToLoadOnInverter based on Integer32"""
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


_LgpPwrOutputToLoadOnInverter_Type.__name__ = "Integer32"
_LgpPwrOutputToLoadOnInverter_Object = MibScalar
lgpPwrOutputToLoadOnInverter = _LgpPwrOutputToLoadOnInverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 7),
    _LgpPwrOutputToLoadOnInverter_Type()
)
lgpPwrOutputToLoadOnInverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadOnInverter.setStatus("current")


class _LgpPwrBatteryChargeCompensating_Type(Integer32):
    """Custom type lgpPwrBatteryChargeCompensating based on Integer32"""
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


_LgpPwrBatteryChargeCompensating_Type.__name__ = "Integer32"
_LgpPwrBatteryChargeCompensating_Object = MibScalar
lgpPwrBatteryChargeCompensating = _LgpPwrBatteryChargeCompensating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 8),
    _LgpPwrBatteryChargeCompensating_Type()
)
lgpPwrBatteryChargeCompensating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryChargeCompensating.setStatus("current")


class _LgpPwrInverterReady_Type(Integer32):
    """Custom type lgpPwrInverterReady based on Integer32"""
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


_LgpPwrInverterReady_Type.__name__ = "Integer32"
_LgpPwrInverterReady_Object = MibScalar
lgpPwrInverterReady = _LgpPwrInverterReady_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 9),
    _LgpPwrInverterReady_Type()
)
lgpPwrInverterReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrInverterReady.setStatus("current")


class _LgpPwrOutputToLoadOnBypass_Type(Integer32):
    """Custom type lgpPwrOutputToLoadOnBypass based on Integer32"""
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


_LgpPwrOutputToLoadOnBypass_Type.__name__ = "Integer32"
_LgpPwrOutputToLoadOnBypass_Object = MibScalar
lgpPwrOutputToLoadOnBypass = _LgpPwrOutputToLoadOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 10),
    _LgpPwrOutputToLoadOnBypass_Type()
)
lgpPwrOutputToLoadOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadOnBypass.setStatus("current")


class _LgpPwrBoost_Type(Integer32):
    """Custom type lgpPwrBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrBoost_Type.__name__ = "Integer32"
_LgpPwrBoost_Object = MibScalar
lgpPwrBoost = _LgpPwrBoost_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 11),
    _LgpPwrBoost_Type()
)
lgpPwrBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBoost.setStatus("current")


class _LgpPwrBuck_Type(Integer32):
    """Custom type lgpPwrBuck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrBuck_Type.__name__ = "Integer32"
_LgpPwrBuck_Object = MibScalar
lgpPwrBuck = _LgpPwrBuck_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 12),
    _LgpPwrBuck_Type()
)
lgpPwrBuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBuck.setStatus("current")


class _LgpPwrShutdownOverTemperature_Type(Integer32):
    """Custom type lgpPwrShutdownOverTemperature based on Integer32"""
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


_LgpPwrShutdownOverTemperature_Type.__name__ = "Integer32"
_LgpPwrShutdownOverTemperature_Object = MibScalar
lgpPwrShutdownOverTemperature = _LgpPwrShutdownOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 13),
    _LgpPwrShutdownOverTemperature_Type()
)
lgpPwrShutdownOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownOverTemperature.setStatus("current")


class _LgpPwrShutdownOverload_Type(Integer32):
    """Custom type lgpPwrShutdownOverload based on Integer32"""
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


_LgpPwrShutdownOverload_Type.__name__ = "Integer32"
_LgpPwrShutdownOverload_Object = MibScalar
lgpPwrShutdownOverload = _LgpPwrShutdownOverload_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 14),
    _LgpPwrShutdownOverload_Type()
)
lgpPwrShutdownOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownOverload.setStatus("current")


class _LgpPwrShutdownDcBusOverload_Type(Integer32):
    """Custom type lgpPwrShutdownDcBusOverload based on Integer32"""
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


_LgpPwrShutdownDcBusOverload_Type.__name__ = "Integer32"
_LgpPwrShutdownDcBusOverload_Object = MibScalar
lgpPwrShutdownDcBusOverload = _LgpPwrShutdownDcBusOverload_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 15),
    _LgpPwrShutdownDcBusOverload_Type()
)
lgpPwrShutdownDcBusOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownDcBusOverload.setStatus("current")


class _LgpPwrShutdownOutputShort_Type(Integer32):
    """Custom type lgpPwrShutdownOutputShort based on Integer32"""
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


_LgpPwrShutdownOutputShort_Type.__name__ = "Integer32"
_LgpPwrShutdownOutputShort_Object = MibScalar
lgpPwrShutdownOutputShort = _LgpPwrShutdownOutputShort_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 16),
    _LgpPwrShutdownOutputShort_Type()
)
lgpPwrShutdownOutputShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownOutputShort.setStatus("current")


class _LgpPwrShutdownLineSwap_Type(Integer32):
    """Custom type lgpPwrShutdownLineSwap based on Integer32"""
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


_LgpPwrShutdownLineSwap_Type.__name__ = "Integer32"
_LgpPwrShutdownLineSwap_Object = MibScalar
lgpPwrShutdownLineSwap = _LgpPwrShutdownLineSwap_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 17),
    _LgpPwrShutdownLineSwap_Type()
)
lgpPwrShutdownLineSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownLineSwap.setStatus("current")


class _LgpPwrShutdownLowBattery_Type(Integer32):
    """Custom type lgpPwrShutdownLowBattery based on Integer32"""
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


_LgpPwrShutdownLowBattery_Type.__name__ = "Integer32"
_LgpPwrShutdownLowBattery_Object = MibScalar
lgpPwrShutdownLowBattery = _LgpPwrShutdownLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 18),
    _LgpPwrShutdownLowBattery_Type()
)
lgpPwrShutdownLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownLowBattery.setStatus("current")


class _LgpPwrShutdownRemote_Type(Integer32):
    """Custom type lgpPwrShutdownRemote based on Integer32"""
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


_LgpPwrShutdownRemote_Type.__name__ = "Integer32"
_LgpPwrShutdownRemote_Object = MibScalar
lgpPwrShutdownRemote = _LgpPwrShutdownRemote_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 19),
    _LgpPwrShutdownRemote_Type()
)
lgpPwrShutdownRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownRemote.setStatus("current")


class _LgpPwrShutdownInputUnderVoltage_Type(Integer32):
    """Custom type lgpPwrShutdownInputUnderVoltage based on Integer32"""
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


_LgpPwrShutdownInputUnderVoltage_Type.__name__ = "Integer32"
_LgpPwrShutdownInputUnderVoltage_Object = MibScalar
lgpPwrShutdownInputUnderVoltage = _LgpPwrShutdownInputUnderVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 20),
    _LgpPwrShutdownInputUnderVoltage_Type()
)
lgpPwrShutdownInputUnderVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownInputUnderVoltage.setStatus("current")


class _LgpPwrShutdownPowerFactorCorrectionFailure_Type(Integer32):
    """Custom type lgpPwrShutdownPowerFactorCorrectionFailure based on Integer32"""
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


_LgpPwrShutdownPowerFactorCorrectionFailure_Type.__name__ = "Integer32"
_LgpPwrShutdownPowerFactorCorrectionFailure_Object = MibScalar
lgpPwrShutdownPowerFactorCorrectionFailure = _LgpPwrShutdownPowerFactorCorrectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 21),
    _LgpPwrShutdownPowerFactorCorrectionFailure_Type()
)
lgpPwrShutdownPowerFactorCorrectionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownPowerFactorCorrectionFailure.setStatus("current")


class _LgpPwrShutdownHardware_Type(Integer32):
    """Custom type lgpPwrShutdownHardware based on Integer32"""
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


_LgpPwrShutdownHardware_Type.__name__ = "Integer32"
_LgpPwrShutdownHardware_Object = MibScalar
lgpPwrShutdownHardware = _LgpPwrShutdownHardware_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 22),
    _LgpPwrShutdownHardware_Type()
)
lgpPwrShutdownHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownHardware.setStatus("current")


class _LgpPwrRedundantSubModule_Type(Integer32):
    """Custom type lgpPwrRedundantSubModule based on Integer32"""
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


_LgpPwrRedundantSubModule_Type.__name__ = "Integer32"
_LgpPwrRedundantSubModule_Object = MibScalar
lgpPwrRedundantSubModule = _LgpPwrRedundantSubModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 23),
    _LgpPwrRedundantSubModule_Type()
)
lgpPwrRedundantSubModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRedundantSubModule.setStatus("current")


class _LgpPwrBypassReady_Type(Integer32):
    """Custom type lgpPwrBypassReady based on Integer32"""
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


_LgpPwrBypassReady_Type.__name__ = "Integer32"
_LgpPwrBypassReady_Object = MibScalar
lgpPwrBypassReady = _LgpPwrBypassReady_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 24),
    _LgpPwrBypassReady_Type()
)
lgpPwrBypassReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassReady.setStatus("current")


class _LgpPwrGeneratorStatus_Type(Integer32):
    """Custom type lgpPwrGeneratorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_LgpPwrGeneratorStatus_Type.__name__ = "Integer32"
_LgpPwrGeneratorStatus_Object = MibScalar
lgpPwrGeneratorStatus = _LgpPwrGeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 25),
    _LgpPwrGeneratorStatus_Type()
)
lgpPwrGeneratorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrGeneratorStatus.setStatus("current")


class _LgpPwrRotaryBreakerStatus_Type(Integer32):
    """Custom type lgpPwrRotaryBreakerStatus based on Integer32"""
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
        *(("bypass", 5),
          ("closed", 2),
          ("maintenance", 6),
          ("normal", 4),
          ("test", 3),
          ("unknown", 1))
    )


_LgpPwrRotaryBreakerStatus_Type.__name__ = "Integer32"
_LgpPwrRotaryBreakerStatus_Object = MibScalar
lgpPwrRotaryBreakerStatus = _LgpPwrRotaryBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 26),
    _LgpPwrRotaryBreakerStatus_Type()
)
lgpPwrRotaryBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRotaryBreakerStatus.setStatus("current")


class _LgpPwrPowerFactorCorrection_Type(Integer32):
    """Custom type lgpPwrPowerFactorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrPowerFactorCorrection_Type.__name__ = "Integer32"
_LgpPwrPowerFactorCorrection_Object = MibScalar
lgpPwrPowerFactorCorrection = _LgpPwrPowerFactorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 27),
    _LgpPwrPowerFactorCorrection_Type()
)
lgpPwrPowerFactorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrPowerFactorCorrection.setStatus("current")
_LgpPwrBypassSyncDiff_Type = Integer32
_LgpPwrBypassSyncDiff_Object = MibScalar
lgpPwrBypassSyncDiff = _LgpPwrBypassSyncDiff_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 28),
    _LgpPwrBypassSyncDiff_Type()
)
lgpPwrBypassSyncDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassSyncDiff.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBypassSyncDiff.setUnits("0.1 Degrees")
_LgpPwrBypassOverloadShutdownTime_Type = Integer32
_LgpPwrBypassOverloadShutdownTime_Object = MibScalar
lgpPwrBypassOverloadShutdownTime = _LgpPwrBypassOverloadShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 29),
    _LgpPwrBypassOverloadShutdownTime_Type()
)
lgpPwrBypassOverloadShutdownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassOverloadShutdownTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBypassOverloadShutdownTime.setUnits("seconds")
_LgpPwrInverterOverloadShutdownTime_Type = Integer32
_LgpPwrInverterOverloadShutdownTime_Object = MibScalar
lgpPwrInverterOverloadShutdownTime = _LgpPwrInverterOverloadShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 30),
    _LgpPwrInverterOverloadShutdownTime_Type()
)
lgpPwrInverterOverloadShutdownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrInverterOverloadShutdownTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrInverterOverloadShutdownTime.setUnits("seconds")


class _LgpPwrStateOutputSource_Type(Integer32):
    """Custom type lgpPwrStateOutputSource based on Integer32"""
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
        *(("bypass", 3),
          ("inverter", 2),
          ("maintenanceBypass", 4),
          ("none", 1))
    )


_LgpPwrStateOutputSource_Type.__name__ = "Integer32"
_LgpPwrStateOutputSource_Object = MibScalar
lgpPwrStateOutputSource = _LgpPwrStateOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 31),
    _LgpPwrStateOutputSource_Type()
)
lgpPwrStateOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutputSource.setStatus("current")


class _LgpPwrStateInputSource_Type(Integer32):
    """Custom type lgpPwrStateInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generator", 3),
          ("none", 1),
          ("utility", 2))
    )


_LgpPwrStateInputSource_Type.__name__ = "Integer32"
_LgpPwrStateInputSource_Object = MibScalar
lgpPwrStateInputSource = _LgpPwrStateInputSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 32),
    _LgpPwrStateInputSource_Type()
)
lgpPwrStateInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInputSource.setStatus("current")


class _LgpPwrStateInputQualification_Type(Integer32):
    """Custom type lgpPwrStateInputQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalHigh", 4),
          ("marginalLow", 2),
          ("normal", 3))
    )


_LgpPwrStateInputQualification_Type.__name__ = "Integer32"
_LgpPwrStateInputQualification_Object = MibScalar
lgpPwrStateInputQualification = _LgpPwrStateInputQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 33),
    _LgpPwrStateInputQualification_Type()
)
lgpPwrStateInputQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInputQualification.setStatus("current")


class _LgpPwrStateBypassStaticSwitchState_Type(Integer32):
    """Custom type lgpPwrStateBypassStaticSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrStateBypassStaticSwitchState_Type.__name__ = "Integer32"
_LgpPwrStateBypassStaticSwitchState_Object = MibScalar
lgpPwrStateBypassStaticSwitchState = _LgpPwrStateBypassStaticSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 34),
    _LgpPwrStateBypassStaticSwitchState_Type()
)
lgpPwrStateBypassStaticSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassStaticSwitchState.setStatus("current")


class _LgpPwrStateBypassQualification_Type(Integer32):
    """Custom type lgpPwrStateBypassQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalHigh", 4),
          ("marginalLow", 2),
          ("normal", 3))
    )


_LgpPwrStateBypassQualification_Type.__name__ = "Integer32"
_LgpPwrStateBypassQualification_Object = MibScalar
lgpPwrStateBypassQualification = _LgpPwrStateBypassQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 35),
    _LgpPwrStateBypassQualification_Type()
)
lgpPwrStateBypassQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassQualification.setStatus("current")


class _LgpPwrStateDCBusQualification_Type(Integer32):
    """Custom type lgpPwrStateDCBusQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalHigh", 4),
          ("marginalLow", 2),
          ("normal", 3))
    )


_LgpPwrStateDCBusQualification_Type.__name__ = "Integer32"
_LgpPwrStateDCBusQualification_Object = MibScalar
lgpPwrStateDCBusQualification = _LgpPwrStateDCBusQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 36),
    _LgpPwrStateDCBusQualification_Type()
)
lgpPwrStateDCBusQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateDCBusQualification.setStatus("current")


class _LgpPwrStateOutQualification_Type(Integer32):
    """Custom type lgpPwrStateOutQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalHigh", 4),
          ("marginalLow", 2),
          ("normal", 3))
    )


_LgpPwrStateOutQualification_Type.__name__ = "Integer32"
_LgpPwrStateOutQualification_Object = MibScalar
lgpPwrStateOutQualification = _LgpPwrStateOutQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 37),
    _LgpPwrStateOutQualification_Type()
)
lgpPwrStateOutQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutQualification.setStatus("current")


class _LgpPwrStateInverterQualification_Type(Integer32):
    """Custom type lgpPwrStateInverterQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalHigh", 4),
          ("marginalLow", 2),
          ("normal", 3))
    )


_LgpPwrStateInverterQualification_Type.__name__ = "Integer32"
_LgpPwrStateInverterQualification_Object = MibScalar
lgpPwrStateInverterQualification = _LgpPwrStateInverterQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 38),
    _LgpPwrStateInverterQualification_Type()
)
lgpPwrStateInverterQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInverterQualification.setStatus("current")


class _LgpPwrStateInverterState_Type(Integer32):
    """Custom type lgpPwrStateInverterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrStateInverterState_Type.__name__ = "Integer32"
_LgpPwrStateInverterState_Object = MibScalar
lgpPwrStateInverterState = _LgpPwrStateInverterState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 39),
    _LgpPwrStateInverterState_Type()
)
lgpPwrStateInverterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInverterState.setStatus("current")


class _LgpPwrStateRectifierState_Type(Integer32):
    """Custom type lgpPwrStateRectifierState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrStateRectifierState_Type.__name__ = "Integer32"
_LgpPwrStateRectifierState_Object = MibScalar
lgpPwrStateRectifierState = _LgpPwrStateRectifierState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 40),
    _LgpPwrStateRectifierState_Type()
)
lgpPwrStateRectifierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateRectifierState.setStatus("current")
_LgpPwrStateModuleGroup_ObjectIdentity = ObjectIdentity
lgpPwrStateModuleGroup = _LgpPwrStateModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 41)
)
if mibBuilder.loadTexts:
    lgpPwrStateModuleGroup.setStatus("current")
_LgpPwrStateUpsModuleCount_Type = Integer32
_LgpPwrStateUpsModuleCount_Object = MibScalar
lgpPwrStateUpsModuleCount = _LgpPwrStateUpsModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 41, 1),
    _LgpPwrStateUpsModuleCount_Type()
)
lgpPwrStateUpsModuleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleCount.setUnits("Count")
_LgpPwrStateUpsModuleRedundantCount_Type = Integer32
_LgpPwrStateUpsModuleRedundantCount_Object = MibScalar
lgpPwrStateUpsModuleRedundantCount = _LgpPwrStateUpsModuleRedundantCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 41, 2),
    _LgpPwrStateUpsModuleRedundantCount_Type()
)
lgpPwrStateUpsModuleRedundantCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleRedundantCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleRedundantCount.setUnits("Count")


class _LgpPwrStateBackfeedBrkrState_Type(Integer32):
    """Custom type lgpPwrStateBackfeedBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateBackfeedBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateBackfeedBrkrState_Object = MibScalar
lgpPwrStateBackfeedBrkrState = _LgpPwrStateBackfeedBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 42),
    _LgpPwrStateBackfeedBrkrState_Type()
)
lgpPwrStateBackfeedBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBackfeedBrkrState.setStatus("current")


class _LgpPwrStateLoadDisconnectState_Type(Integer32):
    """Custom type lgpPwrStateLoadDisconnectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateLoadDisconnectState_Type.__name__ = "Integer32"
_LgpPwrStateLoadDisconnectState_Object = MibScalar
lgpPwrStateLoadDisconnectState = _LgpPwrStateLoadDisconnectState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 43),
    _LgpPwrStateLoadDisconnectState_Type()
)
lgpPwrStateLoadDisconnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateLoadDisconnectState.setStatus("current")


class _LgpPwrStateInputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateInputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateInputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateInputBrkrState_Object = MibScalar
lgpPwrStateInputBrkrState = _LgpPwrStateInputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 44),
    _LgpPwrStateInputBrkrState_Type()
)
lgpPwrStateInputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInputBrkrState.setStatus("current")


class _LgpPwrStateTrapFilterBrkrState_Type(Integer32):
    """Custom type lgpPwrStateTrapFilterBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateTrapFilterBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateTrapFilterBrkrState_Object = MibScalar
lgpPwrStateTrapFilterBrkrState = _LgpPwrStateTrapFilterBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 45),
    _LgpPwrStateTrapFilterBrkrState_Type()
)
lgpPwrStateTrapFilterBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateTrapFilterBrkrState.setStatus("current")


class _LgpPwrStateInvOutputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateInvOutputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateInvOutputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateInvOutputBrkrState_Object = MibScalar
lgpPwrStateInvOutputBrkrState = _LgpPwrStateInvOutputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 46),
    _LgpPwrStateInvOutputBrkrState_Type()
)
lgpPwrStateInvOutputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInvOutputBrkrState.setStatus("current")


class _LgpPwrStateIntBypassBrkrState_Type(Integer32):
    """Custom type lgpPwrStateIntBypassBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateIntBypassBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateIntBypassBrkrState_Object = MibScalar
lgpPwrStateIntBypassBrkrState = _LgpPwrStateIntBypassBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 47),
    _LgpPwrStateIntBypassBrkrState_Type()
)
lgpPwrStateIntBypassBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateIntBypassBrkrState.setStatus("current")


class _LgpPwrStateBypassIsolBrkrState_Type(Integer32):
    """Custom type lgpPwrStateBypassIsolBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateBypassIsolBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateBypassIsolBrkrState_Object = MibScalar
lgpPwrStateBypassIsolBrkrState = _LgpPwrStateBypassIsolBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 48),
    _LgpPwrStateBypassIsolBrkrState_Type()
)
lgpPwrStateBypassIsolBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassIsolBrkrState.setStatus("current")


class _LgpPwrStateRectifierIsolBrkrState_Type(Integer32):
    """Custom type lgpPwrStateRectifierIsolBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateRectifierIsolBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateRectifierIsolBrkrState_Object = MibScalar
lgpPwrStateRectifierIsolBrkrState = _LgpPwrStateRectifierIsolBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 49),
    _LgpPwrStateRectifierIsolBrkrState_Type()
)
lgpPwrStateRectifierIsolBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateRectifierIsolBrkrState.setStatus("current")


class _LgpPwrStateMaintBypassBrkrState_Type(Integer32):
    """Custom type lgpPwrStateMaintBypassBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateMaintBypassBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateMaintBypassBrkrState_Object = MibScalar
lgpPwrStateMaintBypassBrkrState = _LgpPwrStateMaintBypassBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 50),
    _LgpPwrStateMaintBypassBrkrState_Type()
)
lgpPwrStateMaintBypassBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateMaintBypassBrkrState.setStatus("current")


class _LgpPwrStateMaintIsolBrkrState_Type(Integer32):
    """Custom type lgpPwrStateMaintIsolBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateMaintIsolBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateMaintIsolBrkrState_Object = MibScalar
lgpPwrStateMaintIsolBrkrState = _LgpPwrStateMaintIsolBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 51),
    _LgpPwrStateMaintIsolBrkrState_Type()
)
lgpPwrStateMaintIsolBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateMaintIsolBrkrState.setStatus("current")


class _LgpPwrStateOutStaticSwState_Type(Integer32):
    """Custom type lgpPwrStateOutStaticSwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 3),
          ("off", 1),
          ("on", 2))
    )


_LgpPwrStateOutStaticSwState_Type.__name__ = "Integer32"
_LgpPwrStateOutStaticSwState_Object = MibScalar
lgpPwrStateOutStaticSwState = _LgpPwrStateOutStaticSwState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 52),
    _LgpPwrStateOutStaticSwState_Type()
)
lgpPwrStateOutStaticSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutStaticSwState.setStatus("current")


class _LgpPwrStateModuleOutBrkrState_Type(Integer32):
    """Custom type lgpPwrStateModuleOutBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateModuleOutBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateModuleOutBrkrState_Object = MibScalar
lgpPwrStateModuleOutBrkrState = _LgpPwrStateModuleOutBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 53),
    _LgpPwrStateModuleOutBrkrState_Type()
)
lgpPwrStateModuleOutBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateModuleOutBrkrState.setStatus("current")
_LgpPwrBypassReXfrRemainTime_Type = Integer32
_LgpPwrBypassReXfrRemainTime_Object = MibScalar
lgpPwrBypassReXfrRemainTime = _LgpPwrBypassReXfrRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 54),
    _LgpPwrBypassReXfrRemainTime_Type()
)
lgpPwrBypassReXfrRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassReXfrRemainTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBypassReXfrRemainTime.setUnits("seconds")


class _LgpPwrStateUpsOutputSource_Type(Integer32):
    """Custom type lgpPwrStateUpsOutputSource based on Integer32"""
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
        *(("battery", 5),
          ("booster", 6),
          ("bypass", 4),
          ("none", 2),
          ("normal", 3),
          ("other", 1),
          ("reducer", 7))
    )


_LgpPwrStateUpsOutputSource_Type.__name__ = "Integer32"
_LgpPwrStateUpsOutputSource_Object = MibScalar
lgpPwrStateUpsOutputSource = _LgpPwrStateUpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 55),
    _LgpPwrStateUpsOutputSource_Type()
)
lgpPwrStateUpsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateUpsOutputSource.setStatus("current")


class _LgpPwrStateLoadBusSynchronization_Type(Integer32):
    """Custom type lgpPwrStateLoadBusSynchronization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("active", 1),
          ("unknown", 0))
    )


_LgpPwrStateLoadBusSynchronization_Type.__name__ = "Integer32"
_LgpPwrStateLoadBusSynchronization_Object = MibScalar
lgpPwrStateLoadBusSynchronization = _LgpPwrStateLoadBusSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 56),
    _LgpPwrStateLoadBusSynchronization_Type()
)
lgpPwrStateLoadBusSynchronization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateLoadBusSynchronization.setStatus("current")
_LgpPwrStateCircuitBrkrStateGroup_ObjectIdentity = ObjectIdentity
lgpPwrStateCircuitBrkrStateGroup = _LgpPwrStateCircuitBrkrStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57)
)
if mibBuilder.loadTexts:
    lgpPwrStateCircuitBrkrStateGroup.setStatus("current")


class _LgpPwrStateSource1InputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateSource1InputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateSource1InputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateSource1InputBrkrState_Object = MibScalar
lgpPwrStateSource1InputBrkrState = _LgpPwrStateSource1InputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 1),
    _LgpPwrStateSource1InputBrkrState_Type()
)
lgpPwrStateSource1InputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateSource1InputBrkrState.setStatus("current")


class _LgpPwrStateSource2InputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateSource2InputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateSource2InputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateSource2InputBrkrState_Object = MibScalar
lgpPwrStateSource2InputBrkrState = _LgpPwrStateSource2InputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 2),
    _LgpPwrStateSource2InputBrkrState_Type()
)
lgpPwrStateSource2InputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateSource2InputBrkrState.setStatus("current")


class _LgpPwrStateSource1BypassBrkrState_Type(Integer32):
    """Custom type lgpPwrStateSource1BypassBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateSource1BypassBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateSource1BypassBrkrState_Object = MibScalar
lgpPwrStateSource1BypassBrkrState = _LgpPwrStateSource1BypassBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 3),
    _LgpPwrStateSource1BypassBrkrState_Type()
)
lgpPwrStateSource1BypassBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateSource1BypassBrkrState.setStatus("current")


class _LgpPwrStateSource2BypassBrkrState_Type(Integer32):
    """Custom type lgpPwrStateSource2BypassBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateSource2BypassBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateSource2BypassBrkrState_Object = MibScalar
lgpPwrStateSource2BypassBrkrState = _LgpPwrStateSource2BypassBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 4),
    _LgpPwrStateSource2BypassBrkrState_Type()
)
lgpPwrStateSource2BypassBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateSource2BypassBrkrState.setStatus("current")


class _LgpPwrStateOutputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateOutputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateOutputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateOutputBrkrState_Object = MibScalar
lgpPwrStateOutputBrkrState = _LgpPwrStateOutputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 5),
    _LgpPwrStateOutputBrkrState_Type()
)
lgpPwrStateOutputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutputBrkrState.setStatus("current")


class _LgpPwrStateAuxOutputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateAuxOutputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateAuxOutputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateAuxOutputBrkrState_Object = MibScalar
lgpPwrStateAuxOutputBrkrState = _LgpPwrStateAuxOutputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 6),
    _LgpPwrStateAuxOutputBrkrState_Type()
)
lgpPwrStateAuxOutputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateAuxOutputBrkrState.setStatus("current")


class _LgpPwrStateSource1PduInputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateSource1PduInputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateSource1PduInputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateSource1PduInputBrkrState_Object = MibScalar
lgpPwrStateSource1PduInputBrkrState = _LgpPwrStateSource1PduInputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 7),
    _LgpPwrStateSource1PduInputBrkrState_Type()
)
lgpPwrStateSource1PduInputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateSource1PduInputBrkrState.setStatus("current")


class _LgpPwrStateSource2PduInputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateSource2PduInputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("notInstalled", 3),
          ("open", 1))
    )


_LgpPwrStateSource2PduInputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateSource2PduInputBrkrState_Object = MibScalar
lgpPwrStateSource2PduInputBrkrState = _LgpPwrStateSource2PduInputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 57, 8),
    _LgpPwrStateSource2PduInputBrkrState_Type()
)
lgpPwrStateSource2PduInputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateSource2PduInputBrkrState.setStatus("current")


class _LgpPwrEconomicOperation_Type(Integer32):
    """Custom type lgpPwrEconomicOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LgpPwrEconomicOperation_Type.__name__ = "Integer32"
_LgpPwrEconomicOperation_Object = MibScalar
lgpPwrEconomicOperation = _LgpPwrEconomicOperation_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 58),
    _LgpPwrEconomicOperation_Type()
)
lgpPwrEconomicOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrEconomicOperation.setStatus("current")
_LgpPwrSettings_ObjectIdentity = ObjectIdentity
lgpPwrSettings = _LgpPwrSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4)
)
if mibBuilder.loadTexts:
    lgpPwrSettings.setStatus("current")
_LgpPwrPreferredSource_Type = ObjectIdentifier
_LgpPwrPreferredSource_Object = MibScalar
lgpPwrPreferredSource = _LgpPwrPreferredSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 1),
    _LgpPwrPreferredSource_Type()
)
lgpPwrPreferredSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrPreferredSource.setStatus("current")
_LgpPwrLoadOnSource_Type = ObjectIdentifier
_LgpPwrLoadOnSource_Object = MibScalar
lgpPwrLoadOnSource = _LgpPwrLoadOnSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 2),
    _LgpPwrLoadOnSource_Type()
)
lgpPwrLoadOnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLoadOnSource.setStatus("current")
_LgpPwrNominalVoltageDeviation_Type = Integer32
_LgpPwrNominalVoltageDeviation_Object = MibScalar
lgpPwrNominalVoltageDeviation = _LgpPwrNominalVoltageDeviation_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 3),
    _LgpPwrNominalVoltageDeviation_Type()
)
lgpPwrNominalVoltageDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviation.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviation.setUnits("Volt")
_LgpPwrNominalVoltageDeviationPercent_Type = Integer32
_LgpPwrNominalVoltageDeviationPercent_Object = MibScalar
lgpPwrNominalVoltageDeviationPercent = _LgpPwrNominalVoltageDeviationPercent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 4),
    _LgpPwrNominalVoltageDeviationPercent_Type()
)
lgpPwrNominalVoltageDeviationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviationPercent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviationPercent.setUnits("percent")
_LgpPwrPhaseDifferenceLimit_Type = Integer32
_LgpPwrPhaseDifferenceLimit_Object = MibScalar
lgpPwrPhaseDifferenceLimit = _LgpPwrPhaseDifferenceLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 5),
    _LgpPwrPhaseDifferenceLimit_Type()
)
lgpPwrPhaseDifferenceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrPhaseDifferenceLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrPhaseDifferenceLimit.setUnits("0.1 Degrees")
_LgpPwrFrequencyDeviationLimit_Type = Integer32
_LgpPwrFrequencyDeviationLimit_Object = MibScalar
lgpPwrFrequencyDeviationLimit = _LgpPwrFrequencyDeviationLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 6),
    _LgpPwrFrequencyDeviationLimit_Type()
)
lgpPwrFrequencyDeviationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrFrequencyDeviationLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrFrequencyDeviationLimit.setUnits("0.1 Hertz")
_LgpPwrThresholdTable_Object = MibTable
lgpPwrThresholdTable = _LgpPwrThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7)
)
if mibBuilder.loadTexts:
    lgpPwrThresholdTable.setStatus("current")
_LgpPwrThresholdEntry_Object = MibTableRow
lgpPwrThresholdEntry = _LgpPwrThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1)
)
lgpPwrThresholdEntry.setIndexNames(
    (0, "LIEBERT-GP-POWER-MIB", "lgpPwrThresholdIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrThresholdEntry.setStatus("current")
_LgpPwrThresholdIndex_Type = Unsigned32
_LgpPwrThresholdIndex_Object = MibTableColumn
lgpPwrThresholdIndex = _LgpPwrThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 1),
    _LgpPwrThresholdIndex_Type()
)
lgpPwrThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrThresholdIndex.setStatus("current")
_LgpPwrThresholdPoint_Type = ObjectIdentifier
_LgpPwrThresholdPoint_Object = MibTableColumn
lgpPwrThresholdPoint = _LgpPwrThresholdPoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 2),
    _LgpPwrThresholdPoint_Type()
)
lgpPwrThresholdPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrThresholdPoint.setStatus("current")
_LgpPwrThresholdSubID_Type = Unsigned32
_LgpPwrThresholdSubID_Object = MibTableColumn
lgpPwrThresholdSubID = _LgpPwrThresholdSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 3),
    _LgpPwrThresholdSubID_Type()
)
lgpPwrThresholdSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrThresholdSubID.setStatus("current")
_LgpPwrThresholdType_Type = ObjectIdentifier
_LgpPwrThresholdType_Object = MibTableColumn
lgpPwrThresholdType = _LgpPwrThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 4),
    _LgpPwrThresholdType_Type()
)
lgpPwrThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrThresholdType.setStatus("current")
_LgpPwrThresholdHighWarning_Type = Integer32
_LgpPwrThresholdHighWarning_Object = MibTableColumn
lgpPwrThresholdHighWarning = _LgpPwrThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 5),
    _LgpPwrThresholdHighWarning_Type()
)
lgpPwrThresholdHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdHighWarning.setStatus("current")
_LgpPwrThresholdHighFailure_Type = Integer32
_LgpPwrThresholdHighFailure_Object = MibTableColumn
lgpPwrThresholdHighFailure = _LgpPwrThresholdHighFailure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 6),
    _LgpPwrThresholdHighFailure_Type()
)
lgpPwrThresholdHighFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdHighFailure.setStatus("current")
_LgpPwrThresholdLowWarning_Type = Integer32
_LgpPwrThresholdLowWarning_Object = MibTableColumn
lgpPwrThresholdLowWarning = _LgpPwrThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 7),
    _LgpPwrThresholdLowWarning_Type()
)
lgpPwrThresholdLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdLowWarning.setStatus("current")
_LgpPwrThresholdLowFailure_Type = Integer32
_LgpPwrThresholdLowFailure_Object = MibTableColumn
lgpPwrThresholdLowFailure = _LgpPwrThresholdLowFailure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 8),
    _LgpPwrThresholdLowFailure_Type()
)
lgpPwrThresholdLowFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdLowFailure.setStatus("current")


class _LgpPwrUpsAutoRestart_Type(Integer32):
    """Custom type lgpPwrUpsAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrUpsAutoRestart_Type.__name__ = "Integer32"
_LgpPwrUpsAutoRestart_Object = MibScalar
lgpPwrUpsAutoRestart = _LgpPwrUpsAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 8),
    _LgpPwrUpsAutoRestart_Type()
)
lgpPwrUpsAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsAutoRestart.setStatus("current")
_LgpPwrUpsAutoRestartDelay_Type = Integer32
_LgpPwrUpsAutoRestartDelay_Object = MibScalar
lgpPwrUpsAutoRestartDelay = _LgpPwrUpsAutoRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 9),
    _LgpPwrUpsAutoRestartDelay_Type()
)
lgpPwrUpsAutoRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsAutoRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrUpsAutoRestartDelay.setUnits("seconds")
_LgpPwrAutoRestartBatteryChargeThreshold_Type = Integer32
_LgpPwrAutoRestartBatteryChargeThreshold_Object = MibScalar
lgpPwrAutoRestartBatteryChargeThreshold = _LgpPwrAutoRestartBatteryChargeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 10),
    _LgpPwrAutoRestartBatteryChargeThreshold_Type()
)
lgpPwrAutoRestartBatteryChargeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutoRestartBatteryChargeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutoRestartBatteryChargeThreshold.setUnits("percent")
_LgpPwrParallelModuleCount_Type = Integer32
_LgpPwrParallelModuleCount_Object = MibScalar
lgpPwrParallelModuleCount = _LgpPwrParallelModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 11),
    _LgpPwrParallelModuleCount_Type()
)
lgpPwrParallelModuleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrParallelModuleCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrParallelModuleCount.setUnits("Count")
_LgpPwrParallelRedundancyCount_Type = Integer32
_LgpPwrParallelRedundancyCount_Object = MibScalar
lgpPwrParallelRedundancyCount = _LgpPwrParallelRedundancyCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 12),
    _LgpPwrParallelRedundancyCount_Type()
)
lgpPwrParallelRedundancyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrParallelRedundancyCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrParallelRedundancyCount.setUnits("Count")


class _LgpPwrLoadBusSyncMode_Type(Integer32):
    """Custom type lgpPwrLoadBusSyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("none", 3),
          ("slave", 2))
    )


_LgpPwrLoadBusSyncMode_Type.__name__ = "Integer32"
_LgpPwrLoadBusSyncMode_Object = MibScalar
lgpPwrLoadBusSyncMode = _LgpPwrLoadBusSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 13),
    _LgpPwrLoadBusSyncMode_Type()
)
lgpPwrLoadBusSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrLoadBusSyncMode.setStatus("current")


class _LgpPwrEconomicOperationMode_Type(Integer32):
    """Custom type lgpPwrEconomicOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrEconomicOperationMode_Type.__name__ = "Integer32"
_LgpPwrEconomicOperationMode_Object = MibScalar
lgpPwrEconomicOperationMode = _LgpPwrEconomicOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 14),
    _LgpPwrEconomicOperationMode_Type()
)
lgpPwrEconomicOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrEconomicOperationMode.setStatus("current")


class _LgpPwrAutomaticBatteryTest_Type(Integer32):
    """Custom type lgpPwrAutomaticBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrAutomaticBatteryTest_Type.__name__ = "Integer32"
_LgpPwrAutomaticBatteryTest_Object = MibScalar
lgpPwrAutomaticBatteryTest = _LgpPwrAutomaticBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 15),
    _LgpPwrAutomaticBatteryTest_Type()
)
lgpPwrAutomaticBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTest.setStatus("current")
_LgpPwrMinimumRedundantPowerModule_Type = Integer32
_LgpPwrMinimumRedundantPowerModule_Object = MibScalar
lgpPwrMinimumRedundantPowerModule = _LgpPwrMinimumRedundantPowerModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 16),
    _LgpPwrMinimumRedundantPowerModule_Type()
)
lgpPwrMinimumRedundantPowerModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantPowerModule.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantPowerModule.setUnits("Count")
_LgpPwrMinimumRedundantBatteryModule_Type = Integer32
_LgpPwrMinimumRedundantBatteryModule_Object = MibScalar
lgpPwrMinimumRedundantBatteryModule = _LgpPwrMinimumRedundantBatteryModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 17),
    _LgpPwrMinimumRedundantBatteryModule_Type()
)
lgpPwrMinimumRedundantBatteryModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantBatteryModule.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantBatteryModule.setUnits("Count")
_LgpPwrOutputToLoadUserOverloadLimit_Type = Integer32
_LgpPwrOutputToLoadUserOverloadLimit_Object = MibScalar
lgpPwrOutputToLoadUserOverloadLimit = _LgpPwrOutputToLoadUserOverloadLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 18),
    _LgpPwrOutputToLoadUserOverloadLimit_Type()
)
lgpPwrOutputToLoadUserOverloadLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadUserOverloadLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadUserOverloadLimit.setUnits("Volt-Amp")
_LgpPwrNoLoadWarningLimit_Type = Integer32
_LgpPwrNoLoadWarningLimit_Object = MibScalar
lgpPwrNoLoadWarningLimit = _LgpPwrNoLoadWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 19),
    _LgpPwrNoLoadWarningLimit_Type()
)
lgpPwrNoLoadWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningLimit.setUnits("Amp")


class _LgpPwrNoLoadWarningDelay_Type(Integer32):
    """Custom type lgpPwrNoLoadWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_LgpPwrNoLoadWarningDelay_Type.__name__ = "Integer32"
_LgpPwrNoLoadWarningDelay_Object = MibScalar
lgpPwrNoLoadWarningDelay = _LgpPwrNoLoadWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 20),
    _LgpPwrNoLoadWarningDelay_Type()
)
lgpPwrNoLoadWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningDelay.setUnits("minutes")


class _LgpPwrEconomicOperationModeControl_Type(Integer32):
    """Custom type lgpPwrEconomicOperationModeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("mode1", 1),
          ("mode2", 2))
    )


_LgpPwrEconomicOperationModeControl_Type.__name__ = "Integer32"
_LgpPwrEconomicOperationModeControl_Object = MibScalar
lgpPwrEconomicOperationModeControl = _LgpPwrEconomicOperationModeControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 21),
    _LgpPwrEconomicOperationModeControl_Type()
)
lgpPwrEconomicOperationModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrEconomicOperationModeControl.setStatus("current")
_LgpPwrConversion_ObjectIdentity = ObjectIdentity
lgpPwrConversion = _LgpPwrConversion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5)
)
if mibBuilder.loadTexts:
    lgpPwrConversion.setStatus("current")
_LgpPwrNumberInstalledPowerModules_Type = Integer32
_LgpPwrNumberInstalledPowerModules_Object = MibScalar
lgpPwrNumberInstalledPowerModules = _LgpPwrNumberInstalledPowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 1),
    _LgpPwrNumberInstalledPowerModules_Type()
)
lgpPwrNumberInstalledPowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberInstalledPowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberInstalledPowerModules.setUnits("Count")
_LgpPwrNumberFailedPowerModules_Type = Integer32
_LgpPwrNumberFailedPowerModules_Object = MibScalar
lgpPwrNumberFailedPowerModules = _LgpPwrNumberFailedPowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 2),
    _LgpPwrNumberFailedPowerModules_Type()
)
lgpPwrNumberFailedPowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberFailedPowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberFailedPowerModules.setUnits("Count")
_LgpPwrNumberRedundantPowerModules_Type = Integer32
_LgpPwrNumberRedundantPowerModules_Object = MibScalar
lgpPwrNumberRedundantPowerModules = _LgpPwrNumberRedundantPowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 3),
    _LgpPwrNumberRedundantPowerModules_Type()
)
lgpPwrNumberRedundantPowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberRedundantPowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberRedundantPowerModules.setUnits("Count")
_LgpPwrNumberActivePowerModules_Type = Integer32
_LgpPwrNumberActivePowerModules_Object = MibScalar
lgpPwrNumberActivePowerModules = _LgpPwrNumberActivePowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 4),
    _LgpPwrNumberActivePowerModules_Type()
)
lgpPwrNumberActivePowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberActivePowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberActivePowerModules.setUnits("Count")
_LgpPwrNumberPowerModuleWarnings_Type = Integer32
_LgpPwrNumberPowerModuleWarnings_Object = MibScalar
lgpPwrNumberPowerModuleWarnings = _LgpPwrNumberPowerModuleWarnings_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 6),
    _LgpPwrNumberPowerModuleWarnings_Type()
)
lgpPwrNumberPowerModuleWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberPowerModuleWarnings.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberPowerModuleWarnings.setUnits("Count")


class _LgpPwrUpsInverterStandby_Type(Integer32):
    """Custom type lgpPwrUpsInverterStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_LgpPwrUpsInverterStandby_Type.__name__ = "Integer32"
_LgpPwrUpsInverterStandby_Object = MibScalar
lgpPwrUpsInverterStandby = _LgpPwrUpsInverterStandby_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 7),
    _LgpPwrUpsInverterStandby_Type()
)
lgpPwrUpsInverterStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsInverterStandby.setStatus("current")
_LgpPwrControl_ObjectIdentity = ObjectIdentity
lgpPwrControl = _LgpPwrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6)
)
if mibBuilder.loadTexts:
    lgpPwrControl.setStatus("current")
_LgpPwrWellKnownControlPoints_ObjectIdentity = ObjectIdentity
lgpPwrWellKnownControlPoints = _LgpPwrWellKnownControlPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lgpPwrWellKnownControlPoints.setStatus("current")
_LgpPwrLoadCircuit_ObjectIdentity = ObjectIdentity
lgpPwrLoadCircuit = _LgpPwrLoadCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    lgpPwrLoadCircuit.setStatus("current")
_LgpPwrLoadCircuitTable_Object = MibTable
lgpPwrLoadCircuitTable = _LgpPwrLoadCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2)
)
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitTable.setStatus("current")
_LgpPwrLoadCircuitEntry_Object = MibTableRow
lgpPwrLoadCircuitEntry = _LgpPwrLoadCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1)
)
lgpPwrLoadCircuitEntry.setIndexNames(
    (0, "LIEBERT-GP-POWER-MIB", "lgpPwrLoadCircuitIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitEntry.setStatus("current")
_LgpPwrLoadCircuitIndex_Type = Unsigned32
_LgpPwrLoadCircuitIndex_Object = MibTableColumn
lgpPwrLoadCircuitIndex = _LgpPwrLoadCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 1),
    _LgpPwrLoadCircuitIndex_Type()
)
lgpPwrLoadCircuitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitIndex.setStatus("current")
_LgpPwrLoadCircuitId_Type = ObjectIdentifier
_LgpPwrLoadCircuitId_Object = MibTableColumn
lgpPwrLoadCircuitId = _LgpPwrLoadCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 2),
    _LgpPwrLoadCircuitId_Type()
)
lgpPwrLoadCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitId.setStatus("current")
_LgpPwrLoadCircuitSubID_Type = Unsigned32
_LgpPwrLoadCircuitSubID_Object = MibTableColumn
lgpPwrLoadCircuitSubID = _LgpPwrLoadCircuitSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 3),
    _LgpPwrLoadCircuitSubID_Type()
)
lgpPwrLoadCircuitSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitSubID.setStatus("current")


class _LgpPwrLoadCircuitState_Type(Integer32):
    """Custom type lgpPwrLoadCircuitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("off", 2),
          ("on", 1))
    )


_LgpPwrLoadCircuitState_Type.__name__ = "Integer32"
_LgpPwrLoadCircuitState_Object = MibTableColumn
lgpPwrLoadCircuitState = _LgpPwrLoadCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 4),
    _LgpPwrLoadCircuitState_Type()
)
lgpPwrLoadCircuitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitState.setStatus("current")


class _LgpPwrLoadCircuitStateAndControl_Type(Integer32):
    """Custom type lgpPwrLoadCircuitStateAndControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reboot", 2))
    )


_LgpPwrLoadCircuitStateAndControl_Type.__name__ = "Integer32"
_LgpPwrLoadCircuitStateAndControl_Object = MibTableColumn
lgpPwrLoadCircuitStateAndControl = _LgpPwrLoadCircuitStateAndControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 5),
    _LgpPwrLoadCircuitStateAndControl_Type()
)
lgpPwrLoadCircuitStateAndControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitStateAndControl.setStatus("current")
_LgpPwrAlarmSilence_Type = Integer32
_LgpPwrAlarmSilence_Object = MibScalar
lgpPwrAlarmSilence = _LgpPwrAlarmSilence_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 3),
    _LgpPwrAlarmSilence_Type()
)
lgpPwrAlarmSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAlarmSilence.setStatus("current")


class _LgpPwrBatteryTest_Type(Integer32):
    """Custom type lgpPwrBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 2),
          ("start", 1))
    )


_LgpPwrBatteryTest_Type.__name__ = "Integer32"
_LgpPwrBatteryTest_Object = MibScalar
lgpPwrBatteryTest = _LgpPwrBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 4),
    _LgpPwrBatteryTest_Type()
)
lgpPwrBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryTest.setStatus("current")
_LgpPwrUpsAbortCommand_Type = Integer32
_LgpPwrUpsAbortCommand_Object = MibScalar
lgpPwrUpsAbortCommand = _LgpPwrUpsAbortCommand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 5),
    _LgpPwrUpsAbortCommand_Type()
)
lgpPwrUpsAbortCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsAbortCommand.setStatus("current")
_LgpPwrTransferToBypass_Type = Integer32
_LgpPwrTransferToBypass_Object = MibScalar
lgpPwrTransferToBypass = _LgpPwrTransferToBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 6),
    _LgpPwrTransferToBypass_Type()
)
lgpPwrTransferToBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrTransferToBypass.setStatus("current")
_LgpPwrTransferToInverter_Type = Integer32
_LgpPwrTransferToInverter_Object = MibScalar
lgpPwrTransferToInverter = _LgpPwrTransferToInverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 7),
    _LgpPwrTransferToInverter_Type()
)
lgpPwrTransferToInverter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrTransferToInverter.setStatus("current")
_LgpPwrOutputOnDelay_Type = Integer32
_LgpPwrOutputOnDelay_Object = MibScalar
lgpPwrOutputOnDelay = _LgpPwrOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 8),
    _LgpPwrOutputOnDelay_Type()
)
lgpPwrOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputOnDelay.setUnits("seconds")
_LgpPwrOutputOffDelayWithRestart_Type = Integer32
_LgpPwrOutputOffDelayWithRestart_Object = MibScalar
lgpPwrOutputOffDelayWithRestart = _LgpPwrOutputOffDelayWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 9),
    _LgpPwrOutputOffDelayWithRestart_Type()
)
lgpPwrOutputOffDelayWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithRestart.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithRestart.setUnits("seconds")
_LgpPwrOutputOffDelayWithoutRestart_Type = Integer32
_LgpPwrOutputOffDelayWithoutRestart_Object = MibScalar
lgpPwrOutputOffDelayWithoutRestart = _LgpPwrOutputOffDelayWithoutRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 10),
    _LgpPwrOutputOffDelayWithoutRestart_Type()
)
lgpPwrOutputOffDelayWithoutRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithoutRestart.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithoutRestart.setUnits("seconds")
_LgpPwrTopology_ObjectIdentity = ObjectIdentity
lgpPwrTopology = _LgpPwrTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7)
)
if mibBuilder.loadTexts:
    lgpPwrTopology.setStatus("current")


class _LgpPwrUpsTopOffline_Type(Integer32):
    """Custom type lgpPwrUpsTopOffline based on Integer32"""
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


_LgpPwrUpsTopOffline_Type.__name__ = "Integer32"
_LgpPwrUpsTopOffline_Object = MibScalar
lgpPwrUpsTopOffline = _LgpPwrUpsTopOffline_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 1),
    _LgpPwrUpsTopOffline_Type()
)
lgpPwrUpsTopOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrUpsTopOffline.setStatus("current")


class _LgpPwrUpsTopLineInteractive_Type(Integer32):
    """Custom type lgpPwrUpsTopLineInteractive based on Integer32"""
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


_LgpPwrUpsTopLineInteractive_Type.__name__ = "Integer32"
_LgpPwrUpsTopLineInteractive_Object = MibScalar
lgpPwrUpsTopLineInteractive = _LgpPwrUpsTopLineInteractive_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 2),
    _LgpPwrUpsTopLineInteractive_Type()
)
lgpPwrUpsTopLineInteractive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrUpsTopLineInteractive.setStatus("current")


class _LgpPwrUPSTopDualInput_Type(Integer32):
    """Custom type lgpPwrUPSTopDualInput based on Integer32"""
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


_LgpPwrUPSTopDualInput_Type.__name__ = "Integer32"
_LgpPwrUPSTopDualInput_Object = MibScalar
lgpPwrUPSTopDualInput = _LgpPwrUPSTopDualInput_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 3),
    _LgpPwrUPSTopDualInput_Type()
)
lgpPwrUPSTopDualInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrUPSTopDualInput.setStatus("current")


class _LgpPwrTopFrequencyConverter_Type(Integer32):
    """Custom type lgpPwrTopFrequencyConverter based on Integer32"""
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


_LgpPwrTopFrequencyConverter_Type.__name__ = "Integer32"
_LgpPwrTopFrequencyConverter_Object = MibScalar
lgpPwrTopFrequencyConverter = _LgpPwrTopFrequencyConverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 4),
    _LgpPwrTopFrequencyConverter_Type()
)
lgpPwrTopFrequencyConverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTopFrequencyConverter.setStatus("current")


class _LgpPwrTopVoltageConverter_Type(Integer32):
    """Custom type lgpPwrTopVoltageConverter based on Integer32"""
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


_LgpPwrTopVoltageConverter_Type.__name__ = "Integer32"
_LgpPwrTopVoltageConverter_Object = MibScalar
lgpPwrTopVoltageConverter = _LgpPwrTopVoltageConverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 5),
    _LgpPwrTopVoltageConverter_Type()
)
lgpPwrTopVoltageConverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTopVoltageConverter.setStatus("current")
_LgpPwrTopMaximumFrameCapacity_Type = Integer32
_LgpPwrTopMaximumFrameCapacity_Object = MibScalar
lgpPwrTopMaximumFrameCapacity = _LgpPwrTopMaximumFrameCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 6),
    _LgpPwrTopMaximumFrameCapacity_Type()
)
lgpPwrTopMaximumFrameCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrTopMaximumFrameCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrTopMaximumFrameCapacity.setUnits("Volt-Amp")


class _LgpPwrTopRedundantControlModules_Type(Integer32):
    """Custom type lgpPwrTopRedundantControlModules based on Integer32"""
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


_LgpPwrTopRedundantControlModules_Type.__name__ = "Integer32"
_LgpPwrTopRedundantControlModules_Object = MibScalar
lgpPwrTopRedundantControlModules = _LgpPwrTopRedundantControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 7),
    _LgpPwrTopRedundantControlModules_Type()
)
lgpPwrTopRedundantControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTopRedundantControlModules.setStatus("current")


class _LgpPwrInputIsolationTransformerInstalled_Type(Integer32):
    """Custom type lgpPwrInputIsolationTransformerInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_LgpPwrInputIsolationTransformerInstalled_Type.__name__ = "Integer32"
_LgpPwrInputIsolationTransformerInstalled_Object = MibScalar
lgpPwrInputIsolationTransformerInstalled = _LgpPwrInputIsolationTransformerInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 8),
    _LgpPwrInputIsolationTransformerInstalled_Type()
)
lgpPwrInputIsolationTransformerInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrInputIsolationTransformerInstalled.setStatus("current")


class _LgpPwrStateStaticSwitchType_Type(Integer32):
    """Custom type lgpPwrStateStaticSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continuousDuty", 2),
          ("momentaryDuty", 3),
          ("notApplicable", 1))
    )


_LgpPwrStateStaticSwitchType_Type.__name__ = "Integer32"
_LgpPwrStateStaticSwitchType_Object = MibScalar
lgpPwrStateStaticSwitchType = _LgpPwrStateStaticSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 9),
    _LgpPwrStateStaticSwitchType_Type()
)
lgpPwrStateStaticSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateStaticSwitchType.setStatus("current")


class _LgpPwrStateModuleType_Type(Integer32):
    """Custom type lgpPwrStateModuleType based on Integer32"""
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
        *(("mainStaticSwitch", 6),
          ("module1plus1", 2),
          ("module1plusN", 3),
          ("moduleNplus1", 4),
          ("singleModuleSystem", 1),
          ("systemControlCabinet", 5))
    )


_LgpPwrStateModuleType_Type.__name__ = "Integer32"
_LgpPwrStateModuleType_Object = MibScalar
lgpPwrStateModuleType = _LgpPwrStateModuleType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 10),
    _LgpPwrStateModuleType_Type()
)
lgpPwrStateModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateModuleType.setStatus("current")


class _LgpPwrStateBypassInputConfig_Type(Integer32):
    """Custom type lgpPwrStateBypassInputConfig based on Integer32"""
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
        *(("singlePhase2WireL1WithReturn", 1),
          ("threePhase3WireL1L2L3", 4),
          ("threePhase4WireL1L2L3WithNeutral", 5),
          ("twoPhase2WireL1L2", 2),
          ("twoPhase3WireL1L2WithNeutral", 3))
    )


_LgpPwrStateBypassInputConfig_Type.__name__ = "Integer32"
_LgpPwrStateBypassInputConfig_Object = MibScalar
lgpPwrStateBypassInputConfig = _LgpPwrStateBypassInputConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 11),
    _LgpPwrStateBypassInputConfig_Type()
)
lgpPwrStateBypassInputConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassInputConfig.setStatus("current")


class _LgpPwrStateOutputConfig_Type(Integer32):
    """Custom type lgpPwrStateOutputConfig based on Integer32"""
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
        *(("singlePhase2WireL1WithReturn", 1),
          ("threePhase3WireL1L2L3", 4),
          ("threePhase4WireL1L2L3WithNeutral", 5),
          ("twoPhase2WireL1L2", 2),
          ("twoPhase3WireL1L2WithNeutral", 3))
    )


_LgpPwrStateOutputConfig_Type.__name__ = "Integer32"
_LgpPwrStateOutputConfig_Object = MibScalar
lgpPwrStateOutputConfig = _LgpPwrStateOutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 12),
    _LgpPwrStateOutputConfig_Type()
)
lgpPwrStateOutputConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutputConfig.setStatus("current")


class _LgpPwrRectifierPassiveFilterInstalled_Type(Integer32):
    """Custom type lgpPwrRectifierPassiveFilterInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_LgpPwrRectifierPassiveFilterInstalled_Type.__name__ = "Integer32"
_LgpPwrRectifierPassiveFilterInstalled_Object = MibScalar
lgpPwrRectifierPassiveFilterInstalled = _LgpPwrRectifierPassiveFilterInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 13),
    _LgpPwrRectifierPassiveFilterInstalled_Type()
)
lgpPwrRectifierPassiveFilterInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierPassiveFilterInstalled.setStatus("current")


class _LgpPwrRectifierTrapInstalled_Type(Integer32):
    """Custom type lgpPwrRectifierTrapInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_LgpPwrRectifierTrapInstalled_Type.__name__ = "Integer32"
_LgpPwrRectifierTrapInstalled_Object = MibScalar
lgpPwrRectifierTrapInstalled = _LgpPwrRectifierTrapInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 14),
    _LgpPwrRectifierTrapInstalled_Type()
)
lgpPwrRectifierTrapInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierTrapInstalled.setStatus("current")


class _LgpPwrRectifierActiveFilterInstalled_Type(Integer32):
    """Custom type lgpPwrRectifierActiveFilterInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_LgpPwrRectifierActiveFilterInstalled_Type.__name__ = "Integer32"
_LgpPwrRectifierActiveFilterInstalled_Object = MibScalar
lgpPwrRectifierActiveFilterInstalled = _LgpPwrRectifierActiveFilterInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 15),
    _LgpPwrRectifierActiveFilterInstalled_Type()
)
lgpPwrRectifierActiveFilterInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierActiveFilterInstalled.setStatus("current")
_LgpPwrStatistic_ObjectIdentity = ObjectIdentity
lgpPwrStatistic = _LgpPwrStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8)
)
if mibBuilder.loadTexts:
    lgpPwrStatistic.setStatus("current")
_LgpPwrBrownOutCount_Type = Integer32
_LgpPwrBrownOutCount_Object = MibScalar
lgpPwrBrownOutCount = _LgpPwrBrownOutCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 1),
    _LgpPwrBrownOutCount_Type()
)
lgpPwrBrownOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBrownOutCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBrownOutCount.setUnits("Count")
_LgpPwrBlackOutCount_Type = Integer32
_LgpPwrBlackOutCount_Object = MibScalar
lgpPwrBlackOutCount = _LgpPwrBlackOutCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 2),
    _LgpPwrBlackOutCount_Type()
)
lgpPwrBlackOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBlackOutCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBlackOutCount.setUnits("Count")
_LgpPwrTransientCount_Type = Integer32
_LgpPwrTransientCount_Object = MibScalar
lgpPwrTransientCount = _LgpPwrTransientCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 3),
    _LgpPwrTransientCount_Type()
)
lgpPwrTransientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTransientCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrTransientCount.setUnits("Count")
_LgpPwrBatteryDischargeCount_Type = Integer32
_LgpPwrBatteryDischargeCount_Object = MibScalar
lgpPwrBatteryDischargeCount = _LgpPwrBatteryDischargeCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 4),
    _LgpPwrBatteryDischargeCount_Type()
)
lgpPwrBatteryDischargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeCount.setUnits("Count")
_LgpPwrBatteryDischargeTime_Type = Integer32
_LgpPwrBatteryDischargeTime_Object = MibScalar
lgpPwrBatteryDischargeTime = _LgpPwrBatteryDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 5),
    _LgpPwrBatteryDischargeTime_Type()
)
lgpPwrBatteryDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeTime.setUnits("minutes")
_LgpPwrBatteryAmpHours_Type = Integer32
_LgpPwrBatteryAmpHours_Object = MibScalar
lgpPwrBatteryAmpHours = _LgpPwrBatteryAmpHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 6),
    _LgpPwrBatteryAmpHours_Type()
)
lgpPwrBatteryAmpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHours.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHours.setUnits("Amp-hour")
_LgpPwrBatteryWattHours_Type = Integer32
_LgpPwrBatteryWattHours_Object = MibScalar
lgpPwrBatteryWattHours = _LgpPwrBatteryWattHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 7),
    _LgpPwrBatteryWattHours_Type()
)
lgpPwrBatteryWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryWattHours.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryWattHours.setUnits("Watt-Hour")
_LgpPwrBatteryStatisticsReset_Type = Integer32
_LgpPwrBatteryStatisticsReset_Object = MibScalar
lgpPwrBatteryStatisticsReset = _LgpPwrBatteryStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 8),
    _LgpPwrBatteryStatisticsReset_Type()
)
lgpPwrBatteryStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryStatisticsReset.setStatus("current")
_LgpPwrStatisticsReset_Type = Integer32
_LgpPwrStatisticsReset_Object = MibScalar
lgpPwrStatisticsReset = _LgpPwrStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 9),
    _LgpPwrStatisticsReset_Type()
)
lgpPwrStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrStatisticsReset.setStatus("current")
_LgpPwrConfig_ObjectIdentity = ObjectIdentity
lgpPwrConfig = _LgpPwrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9)
)
if mibBuilder.loadTexts:
    lgpPwrConfig.setStatus("current")
_LgpPwrSysCapacity_Type = Integer32
_LgpPwrSysCapacity_Object = MibScalar
lgpPwrSysCapacity = _LgpPwrSysCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 1),
    _LgpPwrSysCapacity_Type()
)
lgpPwrSysCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrSysCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrSysCapacity.setUnits("Volt-Amp")


class _LgpPwrUPSModuleMode_Type(Integer32):
    """Custom type lgpPwrUPSModuleMode based on Integer32"""
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
        *(("hotmaster", 3),
          ("hotslave", 4),
          ("parallel", 2),
          ("single", 1))
    )


_LgpPwrUPSModuleMode_Type.__name__ = "Integer32"
_LgpPwrUPSModuleMode_Object = MibScalar
lgpPwrUPSModuleMode = _LgpPwrUPSModuleMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 2),
    _LgpPwrUPSModuleMode_Type()
)
lgpPwrUPSModuleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUPSModuleMode.setStatus("current")
_LgpPwrMaxRatedCurrent_Type = Integer32
_LgpPwrMaxRatedCurrent_Object = MibScalar
lgpPwrMaxRatedCurrent = _LgpPwrMaxRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 3),
    _LgpPwrMaxRatedCurrent_Type()
)
lgpPwrMaxRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMaxRatedCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMaxRatedCurrent.setUnits("Amp")


class _LgpPwrRectifierPulseCount_Type(Integer32):
    """Custom type lgpPwrRectifierPulseCount based on Integer32"""
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
        *(("eighteenPulse", 3),
          ("sixPulse", 1),
          ("twelvePulse", 2),
          ("twentyFourPulse", 4))
    )


_LgpPwrRectifierPulseCount_Type.__name__ = "Integer32"
_LgpPwrRectifierPulseCount_Object = MibScalar
lgpPwrRectifierPulseCount = _LgpPwrRectifierPulseCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 4),
    _LgpPwrRectifierPulseCount_Type()
)
lgpPwrRectifierPulseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierPulseCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-POWER-MIB",
    **{"liebertGlobalProductsPowerModule": liebertGlobalProductsPowerModule,
       "lgpPwrBattery": lgpPwrBattery,
       "lgpPwrNumberInstalledBatteryModules": lgpPwrNumberInstalledBatteryModules,
       "lgpPwrNumberFailedBatteryModules": lgpPwrNumberFailedBatteryModules,
       "lgpPwrNumberRedundantBatteryModules": lgpPwrNumberRedundantBatteryModules,
       "lgpPwrNumberActiveBatteryModules": lgpPwrNumberActiveBatteryModules,
       "lgpPwrConfigLowBatteryWarningTime": lgpPwrConfigLowBatteryWarningTime,
       "lgpPwrNumberBatteryModuleWarnings": lgpPwrNumberBatteryModuleWarnings,
       "lgpPwrBatteryCount": lgpPwrBatteryCount,
       "lgpPwrBatteryTestResult": lgpPwrBatteryTestResult,
       "lgpPwrNominalBatteryCapacity": lgpPwrNominalBatteryCapacity,
       "lgpPwrBatteryFloatVoltage": lgpPwrBatteryFloatVoltage,
       "lgpPwrBatteryEndOfDischargeVoltage": lgpPwrBatteryEndOfDischargeVoltage,
       "lgpPwrAutomaticBatteryTestInterval": lgpPwrAutomaticBatteryTestInterval,
       "lgpPwrAutomaticBatteryTestCountdown": lgpPwrAutomaticBatteryTestCountdown,
       "lgpPwrBatteryChargeStatus": lgpPwrBatteryChargeStatus,
       "lgpPwrBatteryLifeEnhancer": lgpPwrBatteryLifeEnhancer,
       "lgpPwrBatteryCharger": lgpPwrBatteryCharger,
       "lgpPwrBatteryChargeMode": lgpPwrBatteryChargeMode,
       "lgpPwrBatteryTimeRemaining": lgpPwrBatteryTimeRemaining,
       "lgpPwrBatteryCapacity": lgpPwrBatteryCapacity,
       "lgpPwrBatteryCabinet": lgpPwrBatteryCabinet,
       "lgpPwrBatteryCabinetCount": lgpPwrBatteryCabinetCount,
       "lgpPwrBatteryCabinetType": lgpPwrBatteryCabinetType,
       "lgpPwrBatteryCabinetRatedCapacity": lgpPwrBatteryCabinetRatedCapacity,
       "lgpPwrBatteryLeadAcidCellCount": lgpPwrBatteryLeadAcidCellCount,
       "lgpPwrBatteryNiCadCellCount": lgpPwrBatteryNiCadCellCount,
       "lgpPwrBatteryAmpHoursConsumed": lgpPwrBatteryAmpHoursConsumed,
       "lgpPwrBatteryAmpHoursDischargeConsumed": lgpPwrBatteryAmpHoursDischargeConsumed,
       "lgpPwrBatteryLastDischargeTime": lgpPwrBatteryLastDischargeTime,
       "lgpPwrBatteryLastCommissionTime": lgpPwrBatteryLastCommissionTime,
       "lgpPwrBatteryPresentDischargeTime": lgpPwrBatteryPresentDischargeTime,
       "lgpPwrBatteryCapacityStatus": lgpPwrBatteryCapacityStatus,
       "lgpPwrBatteryCircuitBreakerState": lgpPwrBatteryCircuitBreakerState,
       "lgpPwrMeasurements": lgpPwrMeasurements,
       "lgpPwrWellKnownMeasurementPoints": lgpPwrWellKnownMeasurementPoints,
       "lgpPwrSource1Input": lgpPwrSource1Input,
       "lgpPwrSource2Input": lgpPwrSource2Input,
       "lgpPwrSourcePdu1Input": lgpPwrSourcePdu1Input,
       "lgpPwrSourcePdu2Input": lgpPwrSourcePdu2Input,
       "lgpPwrOutputToLoad": lgpPwrOutputToLoad,
       "lgpPwrMeasBattery": lgpPwrMeasBattery,
       "lgpPwrMeasBypass": lgpPwrMeasBypass,
       "lgpPwrMeasDcBus": lgpPwrMeasDcBus,
       "lgpPwrMeasSystemOutput": lgpPwrMeasSystemOutput,
       "lgpPwrMeasBatteryCabinet": lgpPwrMeasBatteryCabinet,
       "lgpPwrMeasurementPointTable": lgpPwrMeasurementPointTable,
       "lgpPwrMeasurementPointEntry": lgpPwrMeasurementPointEntry,
       "lgpPwrMeasurementPointIndex": lgpPwrMeasurementPointIndex,
       "lgpPwrMeasurementPointId": lgpPwrMeasurementPointId,
       "lgpPwrMeasurementPointNumLines": lgpPwrMeasurementPointNumLines,
       "lgpPwrMeasurementPointNomVolts": lgpPwrMeasurementPointNomVolts,
       "lgpPwrMeasurementPointNomFrequency": lgpPwrMeasurementPointNomFrequency,
       "lgpPwrMeasurementPointFrequency": lgpPwrMeasurementPointFrequency,
       "lgpPwrMeasurementPointApparentPower": lgpPwrMeasurementPointApparentPower,
       "lgpPwrMeasurementPointTruePower": lgpPwrMeasurementPointTruePower,
       "lgpPwrMeasurementPointPowerFactor": lgpPwrMeasurementPointPowerFactor,
       "lgpPwrMeasurementPointWattHours": lgpPwrMeasurementPointWattHours,
       "lgpPwrMeasurementPointVAPercent": lgpPwrMeasurementPointVAPercent,
       "lgpPwrMeasurementPointNeutralCurrent": lgpPwrMeasurementPointNeutralCurrent,
       "lgpPwrMeasurementPointGroundCurrent": lgpPwrMeasurementPointGroundCurrent,
       "lgpPwrMeasurementPointNomCurrent": lgpPwrMeasurementPointNomCurrent,
       "lgpPwrMeasurementPointNomPowerFactor": lgpPwrMeasurementPointNomPowerFactor,
       "lgpPwrMeasurementPointNomVA": lgpPwrMeasurementPointNomVA,
       "lgpPwrMeasurementPointNomW": lgpPwrMeasurementPointNomW,
       "lgpPwrMeasurementPointPowerFactorTag": lgpPwrMeasurementPointPowerFactorTag,
       "lgpPwrLineMeasurementTable": lgpPwrLineMeasurementTable,
       "lgpPwrLineMeasurementEntry": lgpPwrLineMeasurementEntry,
       "lgpPwrMeasurementPtIndex": lgpPwrMeasurementPtIndex,
       "lgpPwrLineMeasurementIndex": lgpPwrLineMeasurementIndex,
       "lgpPwrMeasurementPoint": lgpPwrMeasurementPoint,
       "lgpPwrLineMeasurementVoltsLL": lgpPwrLineMeasurementVoltsLL,
       "lgpPwrLineMeasurementVoltsLN": lgpPwrLineMeasurementVoltsLN,
       "lgpPwrLineMeasurementCurrent": lgpPwrLineMeasurementCurrent,
       "lgpPwrLineMeasurementCapacity": lgpPwrLineMeasurementCapacity,
       "lgpPwrLineMeasurementVA": lgpPwrLineMeasurementVA,
       "lgpPwrLineMeasurementTruePower": lgpPwrLineMeasurementTruePower,
       "lgpPwrLineMeasurementVoltageTHD": lgpPwrLineMeasurementVoltageTHD,
       "lgpPwrLineMeasurementCurrentTHD": lgpPwrLineMeasurementCurrentTHD,
       "lgpPwrLineMeasurementKFactorCurrent": lgpPwrLineMeasurementKFactorCurrent,
       "lgpPwrLineMeasurementCrestFactorCurrent": lgpPwrLineMeasurementCrestFactorCurrent,
       "lgpPwrLineMeasurementPowerFactor": lgpPwrLineMeasurementPowerFactor,
       "lgpPwrLineMeasurementPowerFactorTag": lgpPwrLineMeasurementPowerFactorTag,
       "lgpPwrLineMeasurementMaxVolts": lgpPwrLineMeasurementMaxVolts,
       "lgpPwrLineMeasurementMinVolts": lgpPwrLineMeasurementMinVolts,
       "lgpPwrLineMeasurementVAR": lgpPwrLineMeasurementVAR,
       "lgpPwrLineMeasurementPercentLoad": lgpPwrLineMeasurementPercentLoad,
       "lgpPwrLineMeasurementVolts": lgpPwrLineMeasurementVolts,
       "lgpPwrLineMeasurementVACapacity": lgpPwrLineMeasurementVACapacity,
       "lgpPwrDcMeasurementPointTable": lgpPwrDcMeasurementPointTable,
       "lgpPwrDcMeasurementPointEntry": lgpPwrDcMeasurementPointEntry,
       "lgpPwrDcMeasurementPointIndex": lgpPwrDcMeasurementPointIndex,
       "lgpPwrDcMeasurementPointId": lgpPwrDcMeasurementPointId,
       "lgpPwrDcMeasurementPointSubID": lgpPwrDcMeasurementPointSubID,
       "lgpPwrDcMeasurementPointVolts": lgpPwrDcMeasurementPointVolts,
       "lgpPwrDcMeasurementPointCurrent": lgpPwrDcMeasurementPointCurrent,
       "lgpPwrDcMeasurementPointNomVolts": lgpPwrDcMeasurementPointNomVolts,
       "lgpPwrDcMeasurementPointTruePower": lgpPwrDcMeasurementPointTruePower,
       "lgpPwrWellKnownMeasurementTypes": lgpPwrWellKnownMeasurementTypes,
       "lgpPwrVoltsAc": lgpPwrVoltsAc,
       "lgpPwrVoltsDc": lgpPwrVoltsDc,
       "lgpPwrAmpsNeutral": lgpPwrAmpsNeutral,
       "lgpPwrStatus": lgpPwrStatus,
       "lgpPwrTransferCount": lgpPwrTransferCount,
       "lgpPwrAutoTransferTimer": lgpPwrAutoTransferTimer,
       "lgpPwrAutoReTransferEnabled": lgpPwrAutoReTransferEnabled,
       "lgpPwrSyncPhaseAngle": lgpPwrSyncPhaseAngle,
       "lgpPwrParallelSystemOutputToLoadSource": lgpPwrParallelSystemOutputToLoadSource,
       "lgpPwrDcToDcConverter": lgpPwrDcToDcConverter,
       "lgpPwrOutputToLoadOnInverter": lgpPwrOutputToLoadOnInverter,
       "lgpPwrBatteryChargeCompensating": lgpPwrBatteryChargeCompensating,
       "lgpPwrInverterReady": lgpPwrInverterReady,
       "lgpPwrOutputToLoadOnBypass": lgpPwrOutputToLoadOnBypass,
       "lgpPwrBoost": lgpPwrBoost,
       "lgpPwrBuck": lgpPwrBuck,
       "lgpPwrShutdownOverTemperature": lgpPwrShutdownOverTemperature,
       "lgpPwrShutdownOverload": lgpPwrShutdownOverload,
       "lgpPwrShutdownDcBusOverload": lgpPwrShutdownDcBusOverload,
       "lgpPwrShutdownOutputShort": lgpPwrShutdownOutputShort,
       "lgpPwrShutdownLineSwap": lgpPwrShutdownLineSwap,
       "lgpPwrShutdownLowBattery": lgpPwrShutdownLowBattery,
       "lgpPwrShutdownRemote": lgpPwrShutdownRemote,
       "lgpPwrShutdownInputUnderVoltage": lgpPwrShutdownInputUnderVoltage,
       "lgpPwrShutdownPowerFactorCorrectionFailure": lgpPwrShutdownPowerFactorCorrectionFailure,
       "lgpPwrShutdownHardware": lgpPwrShutdownHardware,
       "lgpPwrRedundantSubModule": lgpPwrRedundantSubModule,
       "lgpPwrBypassReady": lgpPwrBypassReady,
       "lgpPwrGeneratorStatus": lgpPwrGeneratorStatus,
       "lgpPwrRotaryBreakerStatus": lgpPwrRotaryBreakerStatus,
       "lgpPwrPowerFactorCorrection": lgpPwrPowerFactorCorrection,
       "lgpPwrBypassSyncDiff": lgpPwrBypassSyncDiff,
       "lgpPwrBypassOverloadShutdownTime": lgpPwrBypassOverloadShutdownTime,
       "lgpPwrInverterOverloadShutdownTime": lgpPwrInverterOverloadShutdownTime,
       "lgpPwrStateOutputSource": lgpPwrStateOutputSource,
       "lgpPwrStateInputSource": lgpPwrStateInputSource,
       "lgpPwrStateInputQualification": lgpPwrStateInputQualification,
       "lgpPwrStateBypassStaticSwitchState": lgpPwrStateBypassStaticSwitchState,
       "lgpPwrStateBypassQualification": lgpPwrStateBypassQualification,
       "lgpPwrStateDCBusQualification": lgpPwrStateDCBusQualification,
       "lgpPwrStateOutQualification": lgpPwrStateOutQualification,
       "lgpPwrStateInverterQualification": lgpPwrStateInverterQualification,
       "lgpPwrStateInverterState": lgpPwrStateInverterState,
       "lgpPwrStateRectifierState": lgpPwrStateRectifierState,
       "lgpPwrStateModuleGroup": lgpPwrStateModuleGroup,
       "lgpPwrStateUpsModuleCount": lgpPwrStateUpsModuleCount,
       "lgpPwrStateUpsModuleRedundantCount": lgpPwrStateUpsModuleRedundantCount,
       "lgpPwrStateBackfeedBrkrState": lgpPwrStateBackfeedBrkrState,
       "lgpPwrStateLoadDisconnectState": lgpPwrStateLoadDisconnectState,
       "lgpPwrStateInputBrkrState": lgpPwrStateInputBrkrState,
       "lgpPwrStateTrapFilterBrkrState": lgpPwrStateTrapFilterBrkrState,
       "lgpPwrStateInvOutputBrkrState": lgpPwrStateInvOutputBrkrState,
       "lgpPwrStateIntBypassBrkrState": lgpPwrStateIntBypassBrkrState,
       "lgpPwrStateBypassIsolBrkrState": lgpPwrStateBypassIsolBrkrState,
       "lgpPwrStateRectifierIsolBrkrState": lgpPwrStateRectifierIsolBrkrState,
       "lgpPwrStateMaintBypassBrkrState": lgpPwrStateMaintBypassBrkrState,
       "lgpPwrStateMaintIsolBrkrState": lgpPwrStateMaintIsolBrkrState,
       "lgpPwrStateOutStaticSwState": lgpPwrStateOutStaticSwState,
       "lgpPwrStateModuleOutBrkrState": lgpPwrStateModuleOutBrkrState,
       "lgpPwrBypassReXfrRemainTime": lgpPwrBypassReXfrRemainTime,
       "lgpPwrStateUpsOutputSource": lgpPwrStateUpsOutputSource,
       "lgpPwrStateLoadBusSynchronization": lgpPwrStateLoadBusSynchronization,
       "lgpPwrStateCircuitBrkrStateGroup": lgpPwrStateCircuitBrkrStateGroup,
       "lgpPwrStateSource1InputBrkrState": lgpPwrStateSource1InputBrkrState,
       "lgpPwrStateSource2InputBrkrState": lgpPwrStateSource2InputBrkrState,
       "lgpPwrStateSource1BypassBrkrState": lgpPwrStateSource1BypassBrkrState,
       "lgpPwrStateSource2BypassBrkrState": lgpPwrStateSource2BypassBrkrState,
       "lgpPwrStateOutputBrkrState": lgpPwrStateOutputBrkrState,
       "lgpPwrStateAuxOutputBrkrState": lgpPwrStateAuxOutputBrkrState,
       "lgpPwrStateSource1PduInputBrkrState": lgpPwrStateSource1PduInputBrkrState,
       "lgpPwrStateSource2PduInputBrkrState": lgpPwrStateSource2PduInputBrkrState,
       "lgpPwrEconomicOperation": lgpPwrEconomicOperation,
       "lgpPwrSettings": lgpPwrSettings,
       "lgpPwrPreferredSource": lgpPwrPreferredSource,
       "lgpPwrLoadOnSource": lgpPwrLoadOnSource,
       "lgpPwrNominalVoltageDeviation": lgpPwrNominalVoltageDeviation,
       "lgpPwrNominalVoltageDeviationPercent": lgpPwrNominalVoltageDeviationPercent,
       "lgpPwrPhaseDifferenceLimit": lgpPwrPhaseDifferenceLimit,
       "lgpPwrFrequencyDeviationLimit": lgpPwrFrequencyDeviationLimit,
       "lgpPwrThresholdTable": lgpPwrThresholdTable,
       "lgpPwrThresholdEntry": lgpPwrThresholdEntry,
       "lgpPwrThresholdIndex": lgpPwrThresholdIndex,
       "lgpPwrThresholdPoint": lgpPwrThresholdPoint,
       "lgpPwrThresholdSubID": lgpPwrThresholdSubID,
       "lgpPwrThresholdType": lgpPwrThresholdType,
       "lgpPwrThresholdHighWarning": lgpPwrThresholdHighWarning,
       "lgpPwrThresholdHighFailure": lgpPwrThresholdHighFailure,
       "lgpPwrThresholdLowWarning": lgpPwrThresholdLowWarning,
       "lgpPwrThresholdLowFailure": lgpPwrThresholdLowFailure,
       "lgpPwrUpsAutoRestart": lgpPwrUpsAutoRestart,
       "lgpPwrUpsAutoRestartDelay": lgpPwrUpsAutoRestartDelay,
       "lgpPwrAutoRestartBatteryChargeThreshold": lgpPwrAutoRestartBatteryChargeThreshold,
       "lgpPwrParallelModuleCount": lgpPwrParallelModuleCount,
       "lgpPwrParallelRedundancyCount": lgpPwrParallelRedundancyCount,
       "lgpPwrLoadBusSyncMode": lgpPwrLoadBusSyncMode,
       "lgpPwrEconomicOperationMode": lgpPwrEconomicOperationMode,
       "lgpPwrAutomaticBatteryTest": lgpPwrAutomaticBatteryTest,
       "lgpPwrMinimumRedundantPowerModule": lgpPwrMinimumRedundantPowerModule,
       "lgpPwrMinimumRedundantBatteryModule": lgpPwrMinimumRedundantBatteryModule,
       "lgpPwrOutputToLoadUserOverloadLimit": lgpPwrOutputToLoadUserOverloadLimit,
       "lgpPwrNoLoadWarningLimit": lgpPwrNoLoadWarningLimit,
       "lgpPwrNoLoadWarningDelay": lgpPwrNoLoadWarningDelay,
       "lgpPwrEconomicOperationModeControl": lgpPwrEconomicOperationModeControl,
       "lgpPwrConversion": lgpPwrConversion,
       "lgpPwrNumberInstalledPowerModules": lgpPwrNumberInstalledPowerModules,
       "lgpPwrNumberFailedPowerModules": lgpPwrNumberFailedPowerModules,
       "lgpPwrNumberRedundantPowerModules": lgpPwrNumberRedundantPowerModules,
       "lgpPwrNumberActivePowerModules": lgpPwrNumberActivePowerModules,
       "lgpPwrNumberPowerModuleWarnings": lgpPwrNumberPowerModuleWarnings,
       "lgpPwrUpsInverterStandby": lgpPwrUpsInverterStandby,
       "lgpPwrControl": lgpPwrControl,
       "lgpPwrWellKnownControlPoints": lgpPwrWellKnownControlPoints,
       "lgpPwrLoadCircuit": lgpPwrLoadCircuit,
       "lgpPwrLoadCircuitTable": lgpPwrLoadCircuitTable,
       "lgpPwrLoadCircuitEntry": lgpPwrLoadCircuitEntry,
       "lgpPwrLoadCircuitIndex": lgpPwrLoadCircuitIndex,
       "lgpPwrLoadCircuitId": lgpPwrLoadCircuitId,
       "lgpPwrLoadCircuitSubID": lgpPwrLoadCircuitSubID,
       "lgpPwrLoadCircuitState": lgpPwrLoadCircuitState,
       "lgpPwrLoadCircuitStateAndControl": lgpPwrLoadCircuitStateAndControl,
       "lgpPwrAlarmSilence": lgpPwrAlarmSilence,
       "lgpPwrBatteryTest": lgpPwrBatteryTest,
       "lgpPwrUpsAbortCommand": lgpPwrUpsAbortCommand,
       "lgpPwrTransferToBypass": lgpPwrTransferToBypass,
       "lgpPwrTransferToInverter": lgpPwrTransferToInverter,
       "lgpPwrOutputOnDelay": lgpPwrOutputOnDelay,
       "lgpPwrOutputOffDelayWithRestart": lgpPwrOutputOffDelayWithRestart,
       "lgpPwrOutputOffDelayWithoutRestart": lgpPwrOutputOffDelayWithoutRestart,
       "lgpPwrTopology": lgpPwrTopology,
       "lgpPwrUpsTopOffline": lgpPwrUpsTopOffline,
       "lgpPwrUpsTopLineInteractive": lgpPwrUpsTopLineInteractive,
       "lgpPwrUPSTopDualInput": lgpPwrUPSTopDualInput,
       "lgpPwrTopFrequencyConverter": lgpPwrTopFrequencyConverter,
       "lgpPwrTopVoltageConverter": lgpPwrTopVoltageConverter,
       "lgpPwrTopMaximumFrameCapacity": lgpPwrTopMaximumFrameCapacity,
       "lgpPwrTopRedundantControlModules": lgpPwrTopRedundantControlModules,
       "lgpPwrInputIsolationTransformerInstalled": lgpPwrInputIsolationTransformerInstalled,
       "lgpPwrStateStaticSwitchType": lgpPwrStateStaticSwitchType,
       "lgpPwrStateModuleType": lgpPwrStateModuleType,
       "lgpPwrStateBypassInputConfig": lgpPwrStateBypassInputConfig,
       "lgpPwrStateOutputConfig": lgpPwrStateOutputConfig,
       "lgpPwrRectifierPassiveFilterInstalled": lgpPwrRectifierPassiveFilterInstalled,
       "lgpPwrRectifierTrapInstalled": lgpPwrRectifierTrapInstalled,
       "lgpPwrRectifierActiveFilterInstalled": lgpPwrRectifierActiveFilterInstalled,
       "lgpPwrStatistic": lgpPwrStatistic,
       "lgpPwrBrownOutCount": lgpPwrBrownOutCount,
       "lgpPwrBlackOutCount": lgpPwrBlackOutCount,
       "lgpPwrTransientCount": lgpPwrTransientCount,
       "lgpPwrBatteryDischargeCount": lgpPwrBatteryDischargeCount,
       "lgpPwrBatteryDischargeTime": lgpPwrBatteryDischargeTime,
       "lgpPwrBatteryAmpHours": lgpPwrBatteryAmpHours,
       "lgpPwrBatteryWattHours": lgpPwrBatteryWattHours,
       "lgpPwrBatteryStatisticsReset": lgpPwrBatteryStatisticsReset,
       "lgpPwrStatisticsReset": lgpPwrStatisticsReset,
       "lgpPwrConfig": lgpPwrConfig,
       "lgpPwrSysCapacity": lgpPwrSysCapacity,
       "lgpPwrUPSModuleMode": lgpPwrUPSModuleMode,
       "lgpPwrMaxRatedCurrent": lgpPwrMaxRatedCurrent,
       "lgpPwrRectifierPulseCount": lgpPwrRectifierPulseCount}
)
