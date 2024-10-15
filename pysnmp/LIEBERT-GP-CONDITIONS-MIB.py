# SNMP MIB module (LIEBERT-GP-CONDITIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-CONDITIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:52 2024
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

(lgpConditions,
 liebertConditionsModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpConditions",
    "liebertConditionsModuleReg")

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

liebertGlobalProductsConditionsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 3, 1)
)
liebertGlobalProductsConditionsModule.setRevisions(
        ("2013-02-12 00:00",
         "2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-08-15 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpConditionsWellKnown_ObjectIdentity = ObjectIdentity
lgpConditionsWellKnown = _LgpConditionsWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1)
)
_LgpConditionHighTemperature_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperature = _LgpConditionHighTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperature.setStatus("current")
_LgpConditionLowTemperature_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperature = _LgpConditionLowTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperature.setStatus("current")
_LgpConditionHighHumidity_ObjectIdentity = ObjectIdentity
lgpConditionHighHumidity = _LgpConditionHighHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumidity.setStatus("current")
_LgpConditionLowHumidity_ObjectIdentity = ObjectIdentity
lgpConditionLowHumidity = _LgpConditionLowHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumidity.setStatus("current")
_LgpConditionLossOfAirflow_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflow = _LgpConditionLossOfAirflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflow.setStatus("current")
_LgpConditionLossOfAirflow1_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflow1 = _LgpConditionLossOfAirflow1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflow1.setStatus("current")
_LgpConditionLossOfAirflow2_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflow2 = _LgpConditionLossOfAirflow2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflow2.setStatus("current")
_LgpConditionLossOfAirflowBlower1_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflowBlower1 = _LgpConditionLossOfAirflowBlower1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflowBlower1.setStatus("current")
_LgpConditionLossOfAirflowAllBlowers_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflowAllBlowers = _LgpConditionLossOfAirflowAllBlowers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflowAllBlowers.setStatus("current")
_LgpConditionChangeFilter_ObjectIdentity = ObjectIdentity
lgpConditionChangeFilter = _LgpConditionChangeFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    lgpConditionChangeFilter.setStatus("current")
_LgpConditionCompressorHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorHighHeadPressure = _LgpConditionCompressorHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorHighHeadPressure.setStatus("current")
_LgpConditionCompressor1HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1HighHeadPressure = _LgpConditionCompressor1HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1HighHeadPressure.setStatus("current")
_LgpConditionCompressor1AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1AHighHeadPressure = _LgpConditionCompressor1AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1AHighHeadPressure.setStatus("current")
_LgpConditionCompressor1BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1BHighHeadPressure = _LgpConditionCompressor1BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1BHighHeadPressure.setStatus("current")
_LgpConditionCompressor2HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2HighHeadPressure = _LgpConditionCompressor2HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2HighHeadPressure.setStatus("current")
_LgpConditionCompressor2AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2AHighHeadPressure = _LgpConditionCompressor2AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2AHighHeadPressure.setStatus("current")
_LgpConditionCompressor2BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2BHighHeadPressure = _LgpConditionCompressor2BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2BHighHeadPressure.setStatus("current")
_LgpConditionCompressor3HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor3HighHeadPressure = _LgpConditionCompressor3HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor3HighHeadPressure.setStatus("current")
_LgpConditionCompressor4HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor4HighHeadPressure = _LgpConditionCompressor4HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor4HighHeadPressure.setStatus("current")
_LgpConditionCompressorOverload_ObjectIdentity = ObjectIdentity
lgpConditionCompressorOverload = _LgpConditionCompressorOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorOverload.setStatus("current")
_LgpConditionCompressor1Overload_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1Overload = _LgpConditionCompressor1Overload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1Overload.setStatus("current")
_LgpConditionCompressor2Overload_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2Overload = _LgpConditionCompressor2Overload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2Overload.setStatus("current")
_LgpConditionCompressorShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressorShortCycle = _LgpConditionCompressorShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorShortCycle.setStatus("current")
_LgpConditionCompressor1ShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1ShortCycle = _LgpConditionCompressor1ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1ShortCycle.setStatus("current")
_LgpConditionCompressor1AShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1AShortCycle = _LgpConditionCompressor1AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1AShortCycle.setStatus("current")
_LgpConditionCompressor1BShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1BShortCycle = _LgpConditionCompressor1BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1BShortCycle.setStatus("current")
_LgpConditionCompressor2ShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2ShortCycle = _LgpConditionCompressor2ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2ShortCycle.setStatus("current")
_LgpConditionCompressor2AShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2AShortCycle = _LgpConditionCompressor2AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2AShortCycle.setStatus("current")
_LgpConditionCompressor2BShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2BShortCycle = _LgpConditionCompressor2BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2BShortCycle.setStatus("current")
_LgpConditionCompressorLowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorLowSuctionPressure = _LgpConditionCompressorLowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 10)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorLowSuctionPressure.setStatus("current")
_LgpConditionCompressor1LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1LowSuctionPressure = _LgpConditionCompressor1LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1LowSuctionPressure.setStatus("current")
_LgpConditionCompressor2LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2LowSuctionPressure = _LgpConditionCompressor2LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2LowSuctionPressure.setStatus("current")
_LgpConditionMainFanOverLoad_ObjectIdentity = ObjectIdentity
lgpConditionMainFanOverLoad = _LgpConditionMainFanOverLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 11)
)
if mibBuilder.loadTexts:
    lgpConditionMainFanOverLoad.setStatus("current")
_LgpConditionManualOverride_ObjectIdentity = ObjectIdentity
lgpConditionManualOverride = _LgpConditionManualOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 12)
)
if mibBuilder.loadTexts:
    lgpConditionManualOverride.setStatus("current")
_LgpConditionStandbyGlycoolPumpOn_ObjectIdentity = ObjectIdentity
lgpConditionStandbyGlycoolPumpOn = _LgpConditionStandbyGlycoolPumpOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 13)
)
if mibBuilder.loadTexts:
    lgpConditionStandbyGlycoolPumpOn.setStatus("current")
_LgpConditionWaterUnderFloor_ObjectIdentity = ObjectIdentity
lgpConditionWaterUnderFloor = _LgpConditionWaterUnderFloor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 14)
)
if mibBuilder.loadTexts:
    lgpConditionWaterUnderFloor.setStatus("current")
_LgpConditionHumidifierProblem_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierProblem = _LgpConditionHumidifierProblem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 15)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierProblem.setStatus("current")
_LgpConditionLowWaterInHumidifier_ObjectIdentity = ObjectIdentity
lgpConditionLowWaterInHumidifier = _LgpConditionLowWaterInHumidifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 16)
)
if mibBuilder.loadTexts:
    lgpConditionLowWaterInHumidifier.setStatus("current")
_LgpConditionSmokeDetected_ObjectIdentity = ObjectIdentity
lgpConditionSmokeDetected = _LgpConditionSmokeDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 17)
)
if mibBuilder.loadTexts:
    lgpConditionSmokeDetected.setStatus("current")
_LgpConditionLowWaterFlow_ObjectIdentity = ObjectIdentity
lgpConditionLowWaterFlow = _LgpConditionLowWaterFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 18)
)
if mibBuilder.loadTexts:
    lgpConditionLowWaterFlow.setStatus("current")
_LgpConditionLostPower_ObjectIdentity = ObjectIdentity
lgpConditionLostPower = _LgpConditionLostPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 19)
)
if mibBuilder.loadTexts:
    lgpConditionLostPower.setStatus("current")
_LgpGeneralFault_ObjectIdentity = ObjectIdentity
lgpGeneralFault = _LgpGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 20)
)
if mibBuilder.loadTexts:
    lgpGeneralFault.setStatus("current")
_LgpConditionLocalAlarm_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm = _LgpConditionLocalAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm.setStatus("current")
_LgpConditionLocalAlarm1_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm1 = _LgpConditionLocalAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm1.setStatus("current")
_LgpConditionLocalAlarm2_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm2 = _LgpConditionLocalAlarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm2.setStatus("current")
_LgpConditionLocalAlarm3_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm3 = _LgpConditionLocalAlarm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 3)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm3.setStatus("current")
_LgpConditionLocalAlarm4_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm4 = _LgpConditionLocalAlarm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm4.setStatus("current")
_LgpConditionLocalAlarm5_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm5 = _LgpConditionLocalAlarm5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm5.setStatus("current")
_LgpConditionLocalAlarm6_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm6 = _LgpConditionLocalAlarm6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 6)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm6.setStatus("current")
_LgpConditionLocalAlarm7_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm7 = _LgpConditionLocalAlarm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 7)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm7.setStatus("current")
_LgpConditionLocalAlarm8_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm8 = _LgpConditionLocalAlarm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 8)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm8.setStatus("current")
_LgpConditionStandbyUnitOn_ObjectIdentity = ObjectIdentity
lgpConditionStandbyUnitOn = _LgpConditionStandbyUnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 22)
)
if mibBuilder.loadTexts:
    lgpConditionStandbyUnitOn.setStatus("current")
_LgpConditionCompressorLowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorLowPressure = _LgpConditionCompressorLowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorLowPressure.setStatus("current")
_LgpConditionCompressor1LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1LowPressure = _LgpConditionCompressor1LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1LowPressure.setStatus("current")
_LgpConditionTandemCompressorCircuit1LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionTandemCompressorCircuit1LowPressure = _LgpConditionTandemCompressorCircuit1LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionTandemCompressorCircuit1LowPressure.setStatus("current")
_LgpConditionCompressor2LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2LowPressure = _LgpConditionCompressor2LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2LowPressure.setStatus("current")
_LgpConditionTandemCompressorCircuit2LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionTandemCompressorCircuit2LowPressure = _LgpConditionTandemCompressorCircuit2LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    lgpConditionTandemCompressorCircuit2LowPressure.setStatus("current")
_LgpConditionCompressor3LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor3LowPressure = _LgpConditionCompressor3LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor3LowPressure.setStatus("current")
_LgpConditionCompressor4LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor4LowPressure = _LgpConditionCompressor4LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 4)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor4LowPressure.setStatus("current")
_LgpConditionHighWaterInPan_ObjectIdentity = ObjectIdentity
lgpConditionHighWaterInPan = _LgpConditionHighWaterInPan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 24)
)
if mibBuilder.loadTexts:
    lgpConditionHighWaterInPan.setStatus("current")
_LgpConditionFaultySensor_ObjectIdentity = ObjectIdentity
lgpConditionFaultySensor = _LgpConditionFaultySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 25)
)
if mibBuilder.loadTexts:
    lgpConditionFaultySensor.setStatus("current")
_LgpConditionServiceCooling_ObjectIdentity = ObjectIdentity
lgpConditionServiceCooling = _LgpConditionServiceCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 26)
)
if mibBuilder.loadTexts:
    lgpConditionServiceCooling.setStatus("current")
_LgpConditionServiceHumidifier_ObjectIdentity = ObjectIdentity
lgpConditionServiceHumidifier = _LgpConditionServiceHumidifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 27)
)
if mibBuilder.loadTexts:
    lgpConditionServiceHumidifier.setStatus("current")
_LgpConditionSystemControlBatteryLow_ObjectIdentity = ObjectIdentity
lgpConditionSystemControlBatteryLow = _LgpConditionSystemControlBatteryLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 28)
)
if mibBuilder.loadTexts:
    lgpConditionSystemControlBatteryLow.setStatus("current")
_LgpConditionGroundSystemFault_ObjectIdentity = ObjectIdentity
lgpConditionGroundSystemFault = _LgpConditionGroundSystemFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 29)
)
if mibBuilder.loadTexts:
    lgpConditionGroundSystemFault.setStatus("current")
_LgpConditionGroundFailure_ObjectIdentity = ObjectIdentity
lgpConditionGroundFailure = _LgpConditionGroundFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 30)
)
if mibBuilder.loadTexts:
    lgpConditionGroundFailure.setStatus("current")
_LgpConditionSecurityBreach_ObjectIdentity = ObjectIdentity
lgpConditionSecurityBreach = _LgpConditionSecurityBreach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 31)
)
if mibBuilder.loadTexts:
    lgpConditionSecurityBreach.setStatus("current")
_LgpConditionEmergencyShutdown_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyShutdown = _LgpConditionEmergencyShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 32)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyShutdown.setStatus("current")
_LgpConditionOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionOnBypass = _LgpConditionOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33)
)
if mibBuilder.loadTexts:
    lgpConditionOnBypass.setStatus("current")
_LgpConditionLoadOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnBypass = _LgpConditionLoadOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnBypass.setStatus("obsolete")
_LgpConditionLoadOnMaintenceBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnMaintenceBypass = _LgpConditionLoadOnMaintenceBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnMaintenceBypass.setStatus("current")
_LgpConditionParallelSysLoadOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysLoadOnBypass = _LgpConditionParallelSysLoadOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 3)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysLoadOnBypass.setStatus("current")
_LgpConditionLoadOnBypassByImpact_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnBypassByImpact = _LgpConditionLoadOnBypassByImpact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnBypassByImpact.setStatus("current")
_LgpConditionLoadTransferedToBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadTransferedToBypass = _LgpConditionLoadTransferedToBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLoadTransferedToBypass.setStatus("current")
_LgpConditionEmergencyTransferToBypass_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyTransferToBypass = _LgpConditionEmergencyTransferToBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 6)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyTransferToBypass.setStatus("current")
_LgpConditionOutputToLoadVoltTHD_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadVoltTHD = _LgpConditionOutputToLoadVoltTHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 34)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadVoltTHD.setStatus("current")
_LgpConditionLogicFailure_ObjectIdentity = ObjectIdentity
lgpConditionLogicFailure = _LgpConditionLogicFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 35)
)
if mibBuilder.loadTexts:
    lgpConditionLogicFailure.setStatus("current")
_LgpConditionPowerSupplyFault_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupplyFault = _LgpConditionPowerSupplyFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 36)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupplyFault.setStatus("current")
_LgpConditionPowerSupply1Fault_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply1Fault = _LgpConditionPowerSupply1Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 36, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply1Fault.setStatus("current")
_LgpConditionPowerSupply2Fault_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply2Fault = _LgpConditionPowerSupply2Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 36, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply2Fault.setStatus("current")
_LgpConditionPowerSupplyFailure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupplyFailure = _LgpConditionPowerSupplyFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupplyFailure.setStatus("current")
_LgpConditionPowerSupply1Failure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply1Failure = _LgpConditionPowerSupply1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply1Failure.setStatus("current")
_LgpConditionPowerSupply2Failure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply2Failure = _LgpConditionPowerSupply2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply2Failure.setStatus("current")
_LgpConditionSource1PowerSupplyInputFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1PowerSupplyInputFailure = _LgpConditionSource1PowerSupplyInputFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PowerSupplyInputFailure.setStatus("current")
_LgpConditionSource2PowerSupplyInputFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2PowerSupplyInputFailure = _LgpConditionSource2PowerSupplyInputFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PowerSupplyInputFailure.setStatus("current")
_LgpConditionPowerSupplyLogicFailure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupplyLogicFailure = _LgpConditionPowerSupplyLogicFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 5)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupplyLogicFailure.setStatus("current")
_LgpConditionCompressorPowerSupplyFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorPowerSupplyFailure = _LgpConditionCompressorPowerSupplyFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 6)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorPowerSupplyFailure.setStatus("current")
_LgpConditionOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionOverVoltage = _LgpConditionOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38)
)
if mibBuilder.loadTexts:
    lgpConditionOverVoltage.setStatus("current")
_LgpConditionSource1OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource1OverVoltage = _LgpConditionSource1OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1OverVoltage.setStatus("current")
_LgpConditionSource2OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource2OverVoltage = _LgpConditionSource2OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2OverVoltage.setStatus("current")
_LgpConditionOutputToLoadOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverVoltage = _LgpConditionOutputToLoadOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverVoltage.setStatus("current")
_LgpConditionInputOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionInputOverVoltage = _LgpConditionInputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInputOverVoltage.setStatus("current")
_LgpConditionBypassOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBypassOverVoltage = _LgpConditionBypassOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBypassOverVoltage.setStatus("current")
_LgpConditionBypassOverVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionBypassOverVoltageFailure = _LgpConditionBypassOverVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 6)
)
if mibBuilder.loadTexts:
    lgpConditionBypassOverVoltageFailure.setStatus("current")
_LgpConditionBatteryOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBatteryOverVoltage = _LgpConditionBatteryOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryOverVoltage.setStatus("current")
_LgpConditionDcBusOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBusOverVoltage = _LgpConditionDcBusOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8)
)
if mibBuilder.loadTexts:
    lgpConditionDcBusOverVoltage.setStatus("current")
_LgpConditionDcBus1OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1OverVoltage = _LgpConditionDcBus1OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 1)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1OverVoltage.setStatus("current")
_LgpConditionDcBus2OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2OverVoltage = _LgpConditionDcBus2OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 2)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2OverVoltage.setStatus("current")
_LgpConditionDcBus1OverVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1OverVoltageFailure = _LgpConditionDcBus1OverVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 3)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1OverVoltageFailure.setStatus("current")
_LgpConditionDcBus2OverVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2OverVoltageFailure = _LgpConditionDcBus2OverVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 4)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2OverVoltageFailure.setStatus("current")
_LgpConditionUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionUnderVoltage = _LgpConditionUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39)
)
if mibBuilder.loadTexts:
    lgpConditionUnderVoltage.setStatus("current")
_LgpConditionSource1UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource1UnderVoltage = _LgpConditionSource1UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1UnderVoltage.setStatus("current")
_LgpConditionSource2UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource2UnderVoltage = _LgpConditionSource2UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2UnderVoltage.setStatus("current")
_LgpConditionOutputToLoadUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadUnderVoltage = _LgpConditionOutputToLoadUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadUnderVoltage.setStatus("current")
_LgpConditionSource1UnderVoltageRMS_ObjectIdentity = ObjectIdentity
lgpConditionSource1UnderVoltageRMS = _LgpConditionSource1UnderVoltageRMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource1UnderVoltageRMS.setStatus("current")
_LgpConditionSource2UnderVoltageRMS_ObjectIdentity = ObjectIdentity
lgpConditionSource2UnderVoltageRMS = _LgpConditionSource2UnderVoltageRMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource2UnderVoltageRMS.setStatus("current")
_LgpConditionInputUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionInputUnderVoltage = _LgpConditionInputUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 6)
)
if mibBuilder.loadTexts:
    lgpConditionInputUnderVoltage.setStatus("current")
_LgpConditionBypassUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBypassUnderVoltage = _LgpConditionBypassUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBypassUnderVoltage.setStatus("current")
_LgpConditionBypassUnderVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionBypassUnderVoltageFailure = _LgpConditionBypassUnderVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBypassUnderVoltageFailure.setStatus("current")
_LgpConditionBatteryUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBatteryUnderVoltage = _LgpConditionBatteryUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 9)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryUnderVoltage.setStatus("current")
_LgpConditionDcBusUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBusUnderVoltage = _LgpConditionDcBusUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10)
)
if mibBuilder.loadTexts:
    lgpConditionDcBusUnderVoltage.setStatus("current")
_LgpConditionDcBus1UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1UnderVoltage = _LgpConditionDcBus1UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 1)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1UnderVoltage.setStatus("current")
_LgpConditionDcBus2UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2UnderVoltage = _LgpConditionDcBus2UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 2)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2UnderVoltage.setStatus("current")
_LgpConditionDcBus1UnderVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1UnderVoltageFailure = _LgpConditionDcBus1UnderVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 3)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1UnderVoltageFailure.setStatus("current")
_LgpConditionDcBus2UnderVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2UnderVoltageFailure = _LgpConditionDcBus2UnderVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 4)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2UnderVoltageFailure.setStatus("current")
_LgpConditionOverload_ObjectIdentity = ObjectIdentity
lgpConditionOverload = _LgpConditionOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40)
)
if mibBuilder.loadTexts:
    lgpConditionOverload.setStatus("current")
_LgpConditionSource1Overload_ObjectIdentity = ObjectIdentity
lgpConditionSource1Overload = _LgpConditionSource1Overload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1Overload.setStatus("current")
_LgpConditionSystemOverload_ObjectIdentity = ObjectIdentity
lgpConditionSystemOverload = _LgpConditionSystemOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOverload.setStatus("current")
_LgpConditionSource1PeakCurrentOverLoad_ObjectIdentity = ObjectIdentity
lgpConditionSource1PeakCurrentOverLoad = _LgpConditionSource1PeakCurrentOverLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PeakCurrentOverLoad.setStatus("current")
_LgpConditionSource2PeakCurrentOverLoad_ObjectIdentity = ObjectIdentity
lgpConditionSource2PeakCurrentOverLoad = _LgpConditionSource2PeakCurrentOverLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PeakCurrentOverLoad.setStatus("current")
_LgpConditionOutputToLoadOverLimit_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverLimit = _LgpConditionOutputToLoadOverLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 5)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverLimit.setStatus("current")
_LgpConditionOutputToLoadOverload_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverload = _LgpConditionOutputToLoadOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 6)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverload.setStatus("current")
_LgpConditionParallelSysOverload_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysOverload = _LgpConditionParallelSysOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 7)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysOverload.setStatus("current")
_LgpConditionBypassCurrentOverload_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverload = _LgpConditionBypassCurrentOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverload.setStatus("current")
_LgpConditionBypassCurrentOverloadPhsA_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverloadPhsA = _LgpConditionBypassCurrentOverloadPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverloadPhsA.setStatus("current")
_LgpConditionBypassCurrentOverloadPhsB_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverloadPhsB = _LgpConditionBypassCurrentOverloadPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8, 2)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverloadPhsB.setStatus("current")
_LgpConditionBypassCurrentOverloadPhsC_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverloadPhsC = _LgpConditionBypassCurrentOverloadPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverloadPhsC.setStatus("current")
_LgpConditionScrShort_ObjectIdentity = ObjectIdentity
lgpConditionScrShort = _LgpConditionScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41)
)
if mibBuilder.loadTexts:
    lgpConditionScrShort.setStatus("current")
_LgpConditionSource1ScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource1ScrShort = _LgpConditionSource1ScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1ScrShort.setStatus("current")
_LgpConditionSource2ScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource2ScrShort = _LgpConditionSource2ScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2ScrShort.setStatus("current")
_LgpConditionBypassScrShort_ObjectIdentity = ObjectIdentity
lgpConditionBypassScrShort = _LgpConditionBypassScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassScrShort.setStatus("current")
_LgpConditionInvStaticSwScrShort_ObjectIdentity = ObjectIdentity
lgpConditionInvStaticSwScrShort = _LgpConditionInvStaticSwScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInvStaticSwScrShort.setStatus("current")
_LgpConditionSource1NeutralScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource1NeutralScrShort = _LgpConditionSource1NeutralScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource1NeutralScrShort.setStatus("current")
_LgpConditionSource2NeutralScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource2NeutralScrShort = _LgpConditionSource2NeutralScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 6)
)
if mibBuilder.loadTexts:
    lgpConditionSource2NeutralScrShort.setStatus("current")
_LgpConditionScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionScrOpen = _LgpConditionScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42)
)
if mibBuilder.loadTexts:
    lgpConditionScrOpen.setStatus("current")
_LgpConditionSource1ScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1ScrOpen = _LgpConditionSource1ScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1ScrOpen.setStatus("current")
_LgpConditionSource2ScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2ScrOpen = _LgpConditionSource2ScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2ScrOpen.setStatus("current")
_LgpConditionBypassScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionBypassScrOpen = _LgpConditionBypassScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassScrOpen.setStatus("current")
_LgpConditionSource1NeutralScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1NeutralScrOpen = _LgpConditionSource1NeutralScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource1NeutralScrOpen.setStatus("current")
_LgpConditionSource2NeutralScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2NeutralScrOpen = _LgpConditionSource2NeutralScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource2NeutralScrOpen.setStatus("current")
_LgpConditionFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionFanFailure = _LgpConditionFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43)
)
if mibBuilder.loadTexts:
    lgpConditionFanFailure.setStatus("current")
_LgpConditionFan1Failure_ObjectIdentity = ObjectIdentity
lgpConditionFan1Failure = _LgpConditionFan1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 1)
)
if mibBuilder.loadTexts:
    lgpConditionFan1Failure.setStatus("current")
_LgpConditionRedundantFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionRedundantFanFailure = _LgpConditionRedundantFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantFanFailure.setStatus("current")
_LgpConditionMultipleFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionMultipleFanFailure = _LgpConditionMultipleFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 3)
)
if mibBuilder.loadTexts:
    lgpConditionMultipleFanFailure.setStatus("current")
_LgpConditionBlowerFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionBlowerFanFailure = _LgpConditionBlowerFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 4)
)
if mibBuilder.loadTexts:
    lgpConditionBlowerFanFailure.setStatus("current")
_LgpConditionBottomBlowerFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionBottomBlowerFanFailure = _LgpConditionBottomBlowerFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 4, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBottomBlowerFanFailure.setStatus("current")
_LgpConditionTopBlowerFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionTopBlowerFanFailure = _LgpConditionTopBlowerFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 4, 2)
)
if mibBuilder.loadTexts:
    lgpConditionTopBlowerFanFailure.setStatus("current")
_LgpConditionCondenserFanVFDFailure_ObjectIdentity = ObjectIdentity
lgpConditionCondenserFanVFDFailure = _LgpConditionCondenserFanVFDFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 5)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserFanVFDFailure.setStatus("current")
_LgpConditionFanPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionFanPowerFailure = _LgpConditionFanPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 6)
)
if mibBuilder.loadTexts:
    lgpConditionFanPowerFailure.setStatus("current")
_LgpConditionTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionTransferInhibited = _LgpConditionTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 44)
)
if mibBuilder.loadTexts:
    lgpConditionTransferInhibited.setStatus("current")
_LgpConditionAutoReTransferPrimed_ObjectIdentity = ObjectIdentity
lgpConditionAutoReTransferPrimed = _LgpConditionAutoReTransferPrimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 45)
)
if mibBuilder.loadTexts:
    lgpConditionAutoReTransferPrimed.setStatus("current")
_LgpConditionSourcesOutOfSync_ObjectIdentity = ObjectIdentity
lgpConditionSourcesOutOfSync = _LgpConditionSourcesOutOfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 46)
)
if mibBuilder.loadTexts:
    lgpConditionSourcesOutOfSync.setStatus("current")
_LgpConditionSourceFailure_ObjectIdentity = ObjectIdentity
lgpConditionSourceFailure = _LgpConditionSourceFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 47)
)
if mibBuilder.loadTexts:
    lgpConditionSourceFailure.setStatus("current")
_LgpConditionSource1Failure_ObjectIdentity = ObjectIdentity
lgpConditionSource1Failure = _LgpConditionSource1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 47, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1Failure.setStatus("current")
_LgpConditionSource2Failure_ObjectIdentity = ObjectIdentity
lgpConditionSource2Failure = _LgpConditionSource2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 47, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2Failure.setStatus("current")
_LgpConditionAutoReTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionAutoReTransferInhibited = _LgpConditionAutoReTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 48)
)
if mibBuilder.loadTexts:
    lgpConditionAutoReTransferInhibited.setStatus("current")
_LgpConditionAutoReTransferFailed_ObjectIdentity = ObjectIdentity
lgpConditionAutoReTransferFailed = _LgpConditionAutoReTransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 49)
)
if mibBuilder.loadTexts:
    lgpConditionAutoReTransferFailed.setStatus("current")
_LgpConditionFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionFuseOpen = _LgpConditionFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50)
)
if mibBuilder.loadTexts:
    lgpConditionFuseOpen.setStatus("current")
_LgpConditionControlFuse1Open_ObjectIdentity = ObjectIdentity
lgpConditionControlFuse1Open = _LgpConditionControlFuse1Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    lgpConditionControlFuse1Open.setStatus("current")
_LgpConditionControlFuse2Open_ObjectIdentity = ObjectIdentity
lgpConditionControlFuse2Open = _LgpConditionControlFuse2Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 2)
)
if mibBuilder.loadTexts:
    lgpConditionControlFuse2Open.setStatus("current")
_LgpConditionRectifierFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionRectifierFuseOpen = _LgpConditionRectifierFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 3)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierFuseOpen.setStatus("current")
_LgpConditionInverterFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionInverterFuseOpen = _LgpConditionInverterFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInverterFuseOpen.setStatus("current")
_LgpConditionOutputToLoadFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadFuseOpen = _LgpConditionOutputToLoadFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 5)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadFuseOpen.setStatus("current")
_LgpConditionDcCapacitorFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionDcCapacitorFuseOpen = _LgpConditionDcCapacitorFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 6)
)
if mibBuilder.loadTexts:
    lgpConditionDcCapacitorFuseOpen.setStatus("current")
_LgpConditionDisconnect_ObjectIdentity = ObjectIdentity
lgpConditionDisconnect = _LgpConditionDisconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51)
)
if mibBuilder.loadTexts:
    lgpConditionDisconnect.setStatus("current")
_LgpConditionSource1DisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1DisconnectOpen = _LgpConditionSource1DisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1DisconnectOpen.setStatus("current")
_LgpConditionSource2DisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2DisconnectOpen = _LgpConditionSource2DisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2DisconnectOpen.setStatus("current")
_LgpConditionSource1PduDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1PduDisconnectOpen = _LgpConditionSource1PduDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PduDisconnectOpen.setStatus("current")
_LgpConditionSource2PduDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2PduDisconnectOpen = _LgpConditionSource2PduDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PduDisconnectOpen.setStatus("current")
_LgpConditionOutputToLoadDisconnect1Open_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadDisconnect1Open = _LgpConditionOutputToLoadDisconnect1Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 5)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadDisconnect1Open.setStatus("current")
_LgpConditionOutputToLoadDisconnect2Open_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadDisconnect2Open = _LgpConditionOutputToLoadDisconnect2Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 6)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadDisconnect2Open.setStatus("current")
_LgpConditionSource1BypassDisconnectClosed_ObjectIdentity = ObjectIdentity
lgpConditionSource1BypassDisconnectClosed = _LgpConditionSource1BypassDisconnectClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 7)
)
if mibBuilder.loadTexts:
    lgpConditionSource1BypassDisconnectClosed.setStatus("current")
_LgpConditionSource2BypassDisconnectClosed_ObjectIdentity = ObjectIdentity
lgpConditionSource2BypassDisconnectClosed = _LgpConditionSource2BypassDisconnectClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 8)
)
if mibBuilder.loadTexts:
    lgpConditionSource2BypassDisconnectClosed.setStatus("current")
_LgpConditionOutputToLoadNeutralDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadNeutralDisconnectOpen = _LgpConditionOutputToLoadNeutralDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 9)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadNeutralDisconnectOpen.setStatus("current")
_LgpConditionBatteryDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDisconnectOpen = _LgpConditionBatteryDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDisconnectOpen.setStatus("current")
_LgpConditionBatteryDiscOpenCab01_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab01 = _LgpConditionBatteryDiscOpenCab01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab01.setStatus("current")
_LgpConditionBatteryDiscOpenCab02_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab02 = _LgpConditionBatteryDiscOpenCab02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 2)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab02.setStatus("current")
_LgpConditionBatteryDiscOpenCab03_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab03 = _LgpConditionBatteryDiscOpenCab03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab03.setStatus("current")
_LgpConditionBatteryDiscOpenCab04_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab04 = _LgpConditionBatteryDiscOpenCab04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 4)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab04.setStatus("current")
_LgpConditionBatteryDiscOpenCab05_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab05 = _LgpConditionBatteryDiscOpenCab05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab05.setStatus("current")
_LgpConditionBatteryDiscOpenCab06_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab06 = _LgpConditionBatteryDiscOpenCab06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 6)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab06.setStatus("current")
_LgpConditionBatteryDiscOpenCab07_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab07 = _LgpConditionBatteryDiscOpenCab07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab07.setStatus("current")
_LgpConditionBatteryDiscOpenCab08_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab08 = _LgpConditionBatteryDiscOpenCab08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab08.setStatus("current")
_LgpConditionInputDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionInputDisconnectOpen = _LgpConditionInputDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 11)
)
if mibBuilder.loadTexts:
    lgpConditionInputDisconnectOpen.setStatus("current")
_LgpConditionOutputToLoadDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadDisconnectOpen = _LgpConditionOutputToLoadDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 12)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadDisconnectOpen.setStatus("current")
_LgpConditionBypassDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionBypassDisconnectOpen = _LgpConditionBypassDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 13)
)
if mibBuilder.loadTexts:
    lgpConditionBypassDisconnectOpen.setStatus("current")
_LgpConditionStaticSwitchDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionStaticSwitchDisconnectOpen = _LgpConditionStaticSwitchDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 14)
)
if mibBuilder.loadTexts:
    lgpConditionStaticSwitchDisconnectOpen.setStatus("current")
_LgpConditionBreakerOpenFailure_ObjectIdentity = ObjectIdentity
lgpConditionBreakerOpenFailure = _LgpConditionBreakerOpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 15)
)
if mibBuilder.loadTexts:
    lgpConditionBreakerOpenFailure.setStatus("current")
_LgpConditionBreakerCloseFailure_ObjectIdentity = ObjectIdentity
lgpConditionBreakerCloseFailure = _LgpConditionBreakerCloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 16)
)
if mibBuilder.loadTexts:
    lgpConditionBreakerCloseFailure.setStatus("current")
_LgpConditionFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionFrequencyDeviation = _LgpConditionFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52)
)
if mibBuilder.loadTexts:
    lgpConditionFrequencyDeviation.setStatus("current")
_LgpConditionSource1FrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionSource1FrequencyDeviation = _LgpConditionSource1FrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1FrequencyDeviation.setStatus("current")
_LgpConditionSource2FrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionSource2FrequencyDeviation = _LgpConditionSource2FrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2FrequencyDeviation.setStatus("current")
_LgpConditionInputFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionInputFrequencyDeviation = _LgpConditionInputFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 3)
)
if mibBuilder.loadTexts:
    lgpConditionInputFrequencyDeviation.setStatus("current")
_LgpConditionOutputToLoadFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadFrequencyDeviation = _LgpConditionOutputToLoadFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 4)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadFrequencyDeviation.setStatus("current")
_LgpConditionBypassFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionBypassFrequencyDeviation = _LgpConditionBypassFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBypassFrequencyDeviation.setStatus("current")
_LgpConditionOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionOverCurrent = _LgpConditionOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53)
)
if mibBuilder.loadTexts:
    lgpConditionOverCurrent.setStatus("current")
_LgpConditionSource1OverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource1OverCurrent = _LgpConditionSource1OverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1OverCurrent.setStatus("current")
_LgpConditionSource2OverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource2OverCurrent = _LgpConditionSource2OverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2OverCurrent.setStatus("current")
_LgpConditionOutputToLoadOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrent = _LgpConditionOutputToLoadOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrent.setStatus("current")
_LgpConditionOutputToLoadOverCurrentPhsA_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrentPhsA = _LgpConditionOutputToLoadOverCurrentPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3, 1)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrentPhsA.setStatus("current")
_LgpConditionOutputToLoadOverCurrentPhsB_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrentPhsB = _LgpConditionOutputToLoadOverCurrentPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3, 2)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrentPhsB.setStatus("current")
_LgpConditionOutputToLoadOverCurrentPhsC_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrentPhsC = _LgpConditionOutputToLoadOverCurrentPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrentPhsC.setStatus("current")
_LgpConditionGroundOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionGroundOverCurrent = _LgpConditionGroundOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 4)
)
if mibBuilder.loadTexts:
    lgpConditionGroundOverCurrent.setStatus("current")
_LgpConditionRectifierOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionRectifierOverCurrent = _LgpConditionRectifierOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 5)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierOverCurrent.setStatus("current")
_LgpConditionInverterOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrent = _LgpConditionInverterOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrent.setStatus("current")
_LgpConditionInverterOverCurrentPhsA_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrentPhsA = _LgpConditionInverterOverCurrentPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6, 1)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrentPhsA.setStatus("current")
_LgpConditionInverterOverCurrentPhsB_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrentPhsB = _LgpConditionInverterOverCurrentPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6, 2)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrentPhsB.setStatus("current")
_LgpConditionInverterOverCurrentPhsC_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrentPhsC = _LgpConditionInverterOverCurrentPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6, 3)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrentPhsC.setStatus("current")
_LgpConditionBatteryConverterOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionBatteryConverterOverCurrent = _LgpConditionBatteryConverterOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryConverterOverCurrent.setStatus("current")
_LgpConditionBatteryBalancerOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionBatteryBalancerOverCurrent = _LgpConditionBatteryBalancerOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryBalancerOverCurrent.setStatus("current")
_LgpConditionHumidifierOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierOverCurrent = _LgpConditionHumidifierOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 9)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierOverCurrent.setStatus("current")
_LgpConditionInputOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionInputOverCurrent = _LgpConditionInputOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 10)
)
if mibBuilder.loadTexts:
    lgpConditionInputOverCurrent.setStatus("current")
_LgpConditionSource1NeutralOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource1NeutralOverCurrent = _LgpConditionSource1NeutralOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 11)
)
if mibBuilder.loadTexts:
    lgpConditionSource1NeutralOverCurrent.setStatus("current")
_LgpConditionSource2NeutralOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource2NeutralOverCurrent = _LgpConditionSource2NeutralOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 12)
)
if mibBuilder.loadTexts:
    lgpConditionSource2NeutralOverCurrent.setStatus("current")
_LgpConditionSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSensorFailure = _LgpConditionSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54)
)
if mibBuilder.loadTexts:
    lgpConditionSensorFailure.setStatus("current")
_LgpConditionOutputToLoadVoltageSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadVoltageSensorFailure = _LgpConditionOutputToLoadVoltageSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 1)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadVoltageSensorFailure.setStatus("current")
_LgpConditionSource1VoltageSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1VoltageSensorFailure = _LgpConditionSource1VoltageSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource1VoltageSensorFailure.setStatus("current")
_LgpConditionSource2VoltageSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2VoltageSensorFailure = _LgpConditionSource2VoltageSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource2VoltageSensorFailure.setStatus("current")
_LgpConditionSource1ScrSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1ScrSensorFailure = _LgpConditionSource1ScrSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource1ScrSensorFailure.setStatus("current")
_LgpConditionSource2ScrSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2ScrSensorFailure = _LgpConditionSource2ScrSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource2ScrSensorFailure.setStatus("current")
_LgpConditionSource1CurrentSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1CurrentSensorFailure = _LgpConditionSource1CurrentSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 6)
)
if mibBuilder.loadTexts:
    lgpConditionSource1CurrentSensorFailure.setStatus("current")
_LgpConditionSource2CurrentSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2CurrentSensorFailure = _LgpConditionSource2CurrentSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 7)
)
if mibBuilder.loadTexts:
    lgpConditionSource2CurrentSensorFailure.setStatus("current")
_LgpConditionRoomTempHumiditySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRoomTempHumiditySensorFailure = _LgpConditionRoomTempHumiditySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 8)
)
if mibBuilder.loadTexts:
    lgpConditionRoomTempHumiditySensorFailure.setStatus("current")
_LgpConditionGlycolTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionGlycolTempSensorFailure = _LgpConditionGlycolTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 9)
)
if mibBuilder.loadTexts:
    lgpConditionGlycolTempSensorFailure.setStatus("current")
_LgpConditionLocal1SensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionLocal1SensorFailure = _LgpConditionLocal1SensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 10)
)
if mibBuilder.loadTexts:
    lgpConditionLocal1SensorFailure.setStatus("current")
_LgpConditionCompressor1SensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1SensorFailure = _LgpConditionCompressor1SensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 11)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1SensorFailure.setStatus("current")
_LgpConditionCompressor2SensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2SensorFailure = _LgpConditionCompressor2SensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 12)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2SensorFailure.setStatus("current")
_LgpConditionSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSupplySensorFailure = _LgpConditionSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 13)
)
if mibBuilder.loadTexts:
    lgpConditionSupplySensorFailure.setStatus("current")
_LgpConditionCabinetTemperatureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCabinetTemperatureSensorFailure = _LgpConditionCabinetTemperatureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 14)
)
if mibBuilder.loadTexts:
    lgpConditionCabinetTemperatureSensorFailure.setStatus("current")
_LgpConditionCabinetHumiditySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCabinetHumiditySensorFailure = _LgpConditionCabinetHumiditySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 15)
)
if mibBuilder.loadTexts:
    lgpConditionCabinetHumiditySensorFailure.setStatus("current")
_LgpConditionRoomTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRoomTempSensorFailure = _LgpConditionRoomTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 16)
)
if mibBuilder.loadTexts:
    lgpConditionRoomTempSensorFailure.setStatus("current")
_LgpConditionBatteryTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTempSensorFailure = _LgpConditionBatteryTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 17)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTempSensorFailure.setStatus("current")
_LgpConditionAirSensorAFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirSensorAFailure = _LgpConditionAirSensorAFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 18)
)
if mibBuilder.loadTexts:
    lgpConditionAirSensorAFailure.setStatus("current")
_LgpConditionAirSensorBFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirSensorBFailure = _LgpConditionAirSensorBFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 19)
)
if mibBuilder.loadTexts:
    lgpConditionAirSensorBFailure.setStatus("current")
_LgpConditionChilledWaterSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterSupplySensorFailure = _LgpConditionChilledWaterSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 20)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterSupplySensorFailure.setStatus("current")
_LgpConditionRefrigerantSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRefrigerantSupplySensorFailure = _LgpConditionRefrigerantSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 21)
)
if mibBuilder.loadTexts:
    lgpConditionRefrigerantSupplySensorFailure.setStatus("current")
_LgpConditionFluidSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionFluidSupplySensorFailure = _LgpConditionFluidSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 22)
)
if mibBuilder.loadTexts:
    lgpConditionFluidSupplySensorFailure.setStatus("current")
_LgpConditionCompressorLowPressureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorLowPressureSensorFailure = _LgpConditionCompressorLowPressureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 23)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorLowPressureSensorFailure.setStatus("current")
_LgpConditionCompressor1LowPressureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1LowPressureSensorFailure = _LgpConditionCompressor1LowPressureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 23, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1LowPressureSensorFailure.setStatus("current")
_LgpConditionRemoteSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRemoteSensorFailure = _LgpConditionRemoteSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 24)
)
if mibBuilder.loadTexts:
    lgpConditionRemoteSensorFailure.setStatus("current")
_LgpConditionAirSupplyTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirSupplyTempSensorFailure = _LgpConditionAirSupplyTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 25)
)
if mibBuilder.loadTexts:
    lgpConditionAirSupplyTempSensorFailure.setStatus("current")
_LgpConditionAirReturnTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirReturnTempSensorFailure = _LgpConditionAirReturnTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 26)
)
if mibBuilder.loadTexts:
    lgpConditionAirReturnTempSensorFailure.setStatus("current")
_LgpConditionCompressorHighPressureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorHighPressureSensorFailure = _LgpConditionCompressorHighPressureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 27)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorHighPressureSensorFailure.setStatus("current")
_LgpConditionInternalCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionInternalCommunicationFailure = _LgpConditionInternalCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 55)
)
if mibBuilder.loadTexts:
    lgpConditionInternalCommunicationFailure.setStatus("current")
_LgpConditionExternalCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionExternalCommunicationFailure = _LgpConditionExternalCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 56)
)
if mibBuilder.loadTexts:
    lgpConditionExternalCommunicationFailure.setStatus("current")
_LgpConditionSourceGateDriveFailure_ObjectIdentity = ObjectIdentity
lgpConditionSourceGateDriveFailure = _LgpConditionSourceGateDriveFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 57)
)
if mibBuilder.loadTexts:
    lgpConditionSourceGateDriveFailure.setStatus("current")
_LgpConditionSource1GateDriveFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1GateDriveFailure = _LgpConditionSource1GateDriveFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 57, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1GateDriveFailure.setStatus("current")
_LgpConditionSource2GateDriveFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2GateDriveFailure = _LgpConditionSource2GateDriveFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 57, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2GateDriveFailure.setStatus("current")
_LgpConditionDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionDisconnectFailure = _LgpConditionDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58)
)
if mibBuilder.loadTexts:
    lgpConditionDisconnectFailure.setStatus("current")
_LgpConditionOutputToLoadNeutralDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadNeutralDisconnectFailure = _LgpConditionOutputToLoadNeutralDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 1)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadNeutralDisconnectFailure.setStatus("current")
_LgpConditionSource1DisconnectShuntTripFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1DisconnectShuntTripFailure = _LgpConditionSource1DisconnectShuntTripFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource1DisconnectShuntTripFailure.setStatus("current")
_LgpConditionSource2DisconnectShuntTripFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2DisconnectShuntTripFailure = _LgpConditionSource2DisconnectShuntTripFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource2DisconnectShuntTripFailure.setStatus("current")
_LgpConditionInverterDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionInverterDisconnectFailure = _LgpConditionInverterDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInverterDisconnectFailure.setStatus("current")
_LgpConditionBatteryDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDisconnectFailure = _LgpConditionBatteryDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDisconnectFailure.setStatus("current")
_LgpConditionRectifierDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionRectifierDisconnectFailure = _LgpConditionRectifierDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 6)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierDisconnectFailure.setStatus("current")
_LgpConditionOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionOverTemperature = _LgpConditionOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59)
)
if mibBuilder.loadTexts:
    lgpConditionOverTemperature.setStatus("current")
_LgpConditionHeatSink1OverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionHeatSink1OverTemperature = _LgpConditionHeatSink1OverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHeatSink1OverTemperature.setStatus("current")
_LgpConditionAmbient1OverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionAmbient1OverTemperature = _LgpConditionAmbient1OverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 2)
)
if mibBuilder.loadTexts:
    lgpConditionAmbient1OverTemperature.setStatus("current")
_LgpConditionSystemOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionSystemOverTemperature = _LgpConditionSystemOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOverTemperature.setStatus("current")
_LgpConditionTransformerOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionTransformerOverTemperature = _LgpConditionTransformerOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 4)
)
if mibBuilder.loadTexts:
    lgpConditionTransformerOverTemperature.setStatus("current")
_LgpConditionBatteryOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionBatteryOverTemperature = _LgpConditionBatteryOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryOverTemperature.setStatus("current")
_LgpConditionRectifierOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionRectifierOverTemperature = _LgpConditionRectifierOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 6)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierOverTemperature.setStatus("current")
_LgpConditionInverterOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverTemperature = _LgpConditionInverterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 7)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverTemperature.setStatus("current")
_LgpConditionRectifierInductorOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionRectifierInductorOverTemperature = _LgpConditionRectifierInductorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 8)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierInductorOverTemperature.setStatus("current")
_LgpConditionInverterInductorOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionInverterInductorOverTemperature = _LgpConditionInverterInductorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 9)
)
if mibBuilder.loadTexts:
    lgpConditionInverterInductorOverTemperature.setStatus("current")
_LgpConditionBatteryConverterOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionBatteryConverterOverTemperature = _LgpConditionBatteryConverterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 10)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryConverterOverTemperature.setStatus("current")
_LgpConditionBatteryBalancerInductorOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionBatteryBalancerInductorOverTemperature = _LgpConditionBatteryBalancerInductorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 11)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryBalancerInductorOverTemperature.setStatus("current")
_LgpConditionChilledWaterOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterOverTemperature = _LgpConditionChilledWaterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 12)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterOverTemperature.setStatus("current")
_LgpConditionElectricHeatersOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionElectricHeatersOverTemperature = _LgpConditionElectricHeatersOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 13)
)
if mibBuilder.loadTexts:
    lgpConditionElectricHeatersOverTemperature.setStatus("current")
_LgpConditionInletAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionInletAirOverTemperature = _LgpConditionInletAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 14)
)
if mibBuilder.loadTexts:
    lgpConditionInletAirOverTemperature.setStatus("current")
_LgpConditionSystemOverTempWarning_ObjectIdentity = ObjectIdentity
lgpConditionSystemOverTempWarning = _LgpConditionSystemOverTempWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 15)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOverTempWarning.setStatus("current")
_LgpConditionHighTemperatureBattString_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureBattString = _LgpConditionHighTemperatureBattString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 16)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureBattString.setStatus("current")
_LgpConditionLoadOnAlternateSource_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnAlternateSource = _LgpConditionLoadOnAlternateSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 60)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnAlternateSource.setStatus("current")
_LgpConditionPhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionPhaseRotationError = _LgpConditionPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61)
)
if mibBuilder.loadTexts:
    lgpConditionPhaseRotationError.setStatus("current")
_LgpConditionSource1PhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionSource1PhaseRotationError = _LgpConditionSource1PhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PhaseRotationError.setStatus("current")
_LgpConditionSource2PhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionSource2PhaseRotationError = _LgpConditionSource2PhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PhaseRotationError.setStatus("current")
_LgpConditionBypassPhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionBypassPhaseRotationError = _LgpConditionBypassPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassPhaseRotationError.setStatus("current")
_LgpConditionInputPhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionInputPhaseRotationError = _LgpConditionInputPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInputPhaseRotationError.setStatus("current")
_LgpConditionControlModuleFailure_ObjectIdentity = ObjectIdentity
lgpConditionControlModuleFailure = _LgpConditionControlModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 62)
)
if mibBuilder.loadTexts:
    lgpConditionControlModuleFailure.setStatus("current")
_LgpConditionControlModule1Failure_ObjectIdentity = ObjectIdentity
lgpConditionControlModule1Failure = _LgpConditionControlModule1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 62, 1)
)
if mibBuilder.loadTexts:
    lgpConditionControlModule1Failure.setStatus("current")
_LgpConditionHistoryLogFull_ObjectIdentity = ObjectIdentity
lgpConditionHistoryLogFull = _LgpConditionHistoryLogFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 63)
)
if mibBuilder.loadTexts:
    lgpConditionHistoryLogFull.setStatus("current")
_LgpConditionConfigurationModified_ObjectIdentity = ObjectIdentity
lgpConditionConfigurationModified = _LgpConditionConfigurationModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 64)
)
if mibBuilder.loadTexts:
    lgpConditionConfigurationModified.setStatus("current")
_LgpConditionPasswordModified_ObjectIdentity = ObjectIdentity
lgpConditionPasswordModified = _LgpConditionPasswordModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 65)
)
if mibBuilder.loadTexts:
    lgpConditionPasswordModified.setStatus("current")
_LgpConditionTimeModified_ObjectIdentity = ObjectIdentity
lgpConditionTimeModified = _LgpConditionTimeModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 66)
)
if mibBuilder.loadTexts:
    lgpConditionTimeModified.setStatus("current")
_LgpConditionDateModified_ObjectIdentity = ObjectIdentity
lgpConditionDateModified = _LgpConditionDateModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 67)
)
if mibBuilder.loadTexts:
    lgpConditionDateModified.setStatus("current")
_LgpConditionEventLogCleared_ObjectIdentity = ObjectIdentity
lgpConditionEventLogCleared = _LgpConditionEventLogCleared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 68)
)
if mibBuilder.loadTexts:
    lgpConditionEventLogCleared.setStatus("current")
_LgpConditionHistoryLogCleared_ObjectIdentity = ObjectIdentity
lgpConditionHistoryLogCleared = _LgpConditionHistoryLogCleared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 69)
)
if mibBuilder.loadTexts:
    lgpConditionHistoryLogCleared.setStatus("current")
_LgpConditionUtilityFailure_ObjectIdentity = ObjectIdentity
lgpConditionUtilityFailure = _LgpConditionUtilityFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 70)
)
if mibBuilder.loadTexts:
    lgpConditionUtilityFailure.setStatus("current")
_LgpConditionBatteryTestInProgress_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTestInProgress = _LgpConditionBatteryTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 71)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTestInProgress.setStatus("current")
_LgpConditionLoadOnBattery_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnBattery = _LgpConditionLoadOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 72)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnBattery.setStatus("current")
_LgpConditionReplaceBattery_ObjectIdentity = ObjectIdentity
lgpConditionReplaceBattery = _LgpConditionReplaceBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 74)
)
if mibBuilder.loadTexts:
    lgpConditionReplaceBattery.setStatus("current")
_LgpConditionUpsShutdownPending_ObjectIdentity = ObjectIdentity
lgpConditionUpsShutdownPending = _LgpConditionUpsShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 75)
)
if mibBuilder.loadTexts:
    lgpConditionUpsShutdownPending.setStatus("current")
_LgpConditionBatteryChargerFailed_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargerFailed = _LgpConditionBatteryChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 76)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargerFailed.setStatus("current")
_LgpConditionBypassVoltageUnqualified_ObjectIdentity = ObjectIdentity
lgpConditionBypassVoltageUnqualified = _LgpConditionBypassVoltageUnqualified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 77)
)
if mibBuilder.loadTexts:
    lgpConditionBypassVoltageUnqualified.setStatus("current")
_LgpConditionCheckAirFilter_ObjectIdentity = ObjectIdentity
lgpConditionCheckAirFilter = _LgpConditionCheckAirFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 78)
)
if mibBuilder.loadTexts:
    lgpConditionCheckAirFilter.setStatus("current")
_LgpConditionBrownOut_ObjectIdentity = ObjectIdentity
lgpConditionBrownOut = _LgpConditionBrownOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 79)
)
if mibBuilder.loadTexts:
    lgpConditionBrownOut.setStatus("current")
_LgpConditionMultipleTransferLockout_ObjectIdentity = ObjectIdentity
lgpConditionMultipleTransferLockout = _LgpConditionMultipleTransferLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 80)
)
if mibBuilder.loadTexts:
    lgpConditionMultipleTransferLockout.setStatus("current")
_LgpConditionBypassPhaseLost_ObjectIdentity = ObjectIdentity
lgpConditionBypassPhaseLost = _LgpConditionBypassPhaseLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 81)
)
if mibBuilder.loadTexts:
    lgpConditionBypassPhaseLost.setStatus("current")
_LgpConditionMaintenceBypassInhibited_ObjectIdentity = ObjectIdentity
lgpConditionMaintenceBypassInhibited = _LgpConditionMaintenceBypassInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 82)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenceBypassInhibited.setStatus("current")
_LgpConditionLoadLockedOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadLockedOnBypass = _LgpConditionLoadLockedOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 83)
)
if mibBuilder.loadTexts:
    lgpConditionLoadLockedOnBypass.setStatus("current")
_LgpConditionOutputToLoadShort_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadShort = _LgpConditionOutputToLoadShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 84)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadShort.setStatus("current")
_LgpConditionEmergencyTransferToInverter_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyTransferToInverter = _LgpConditionEmergencyTransferToInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 85)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyTransferToInverter.setStatus("current")
_LgpConditonEmergencyPowerOff_ObjectIdentity = ObjectIdentity
lgpConditonEmergencyPowerOff = _LgpConditonEmergencyPowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 86)
)
if mibBuilder.loadTexts:
    lgpConditonEmergencyPowerOff.setStatus("current")
_LgpConditionInverterBackFeed_ObjectIdentity = ObjectIdentity
lgpConditionInverterBackFeed = _LgpConditionInverterBackFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 87)
)
if mibBuilder.loadTexts:
    lgpConditionInverterBackFeed.setStatus("current")
_LgpConditionDcGroundFault_ObjectIdentity = ObjectIdentity
lgpConditionDcGroundFault = _LgpConditionDcGroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 88)
)
if mibBuilder.loadTexts:
    lgpConditionDcGroundFault.setStatus("current")
_LgpConditionDcGroundFaultPos_ObjectIdentity = ObjectIdentity
lgpConditionDcGroundFaultPos = _LgpConditionDcGroundFaultPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 88, 1)
)
if mibBuilder.loadTexts:
    lgpConditionDcGroundFaultPos.setStatus("current")
_LgpConditionDcGroundFaultNeg_ObjectIdentity = ObjectIdentity
lgpConditionDcGroundFaultNeg = _LgpConditionDcGroundFaultNeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 88, 2)
)
if mibBuilder.loadTexts:
    lgpConditionDcGroundFaultNeg.setStatus("current")
_LgpConditionStaticTransferSwitchInhibited_ObjectIdentity = ObjectIdentity
lgpConditionStaticTransferSwitchInhibited = _LgpConditionStaticTransferSwitchInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 89)
)
if mibBuilder.loadTexts:
    lgpConditionStaticTransferSwitchInhibited.setStatus("current")
_LgpConditionBatteryLogFullWarning_ObjectIdentity = ObjectIdentity
lgpConditionBatteryLogFullWarning = _LgpConditionBatteryLogFullWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 90)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryLogFullWarning.setStatus("current")
_LgpConditionInputCurrentUnbalanced_ObjectIdentity = ObjectIdentity
lgpConditionInputCurrentUnbalanced = _LgpConditionInputCurrentUnbalanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 91)
)
if mibBuilder.loadTexts:
    lgpConditionInputCurrentUnbalanced.setStatus("current")
_LgpConditionSelfTestFailed_ObjectIdentity = ObjectIdentity
lgpConditionSelfTestFailed = _LgpConditionSelfTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 92)
)
if mibBuilder.loadTexts:
    lgpConditionSelfTestFailed.setStatus("current")
_LgpConditionInverterOutOfSynchronization_ObjectIdentity = ObjectIdentity
lgpConditionInverterOutOfSynchronization = _LgpConditionInverterOutOfSynchronization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 93)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOutOfSynchronization.setStatus("current")
_LgpConditionModuleAlarm_ObjectIdentity = ObjectIdentity
lgpConditionModuleAlarm = _LgpConditionModuleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94)
)
if mibBuilder.loadTexts:
    lgpConditionModuleAlarm.setStatus("current")
_LgpConditioniModuleUnit1Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit1Alarm = _LgpConditioniModuleUnit1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 1)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit1Alarm.setStatus("current")
_LgpConditioniModuleUnit2Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit2Alarm = _LgpConditioniModuleUnit2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 2)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit2Alarm.setStatus("current")
_LgpConditioniModuleUnit3Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit3Alarm = _LgpConditioniModuleUnit3Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 3)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit3Alarm.setStatus("current")
_LgpConditioniModuleUnit4Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit4Alarm = _LgpConditioniModuleUnit4Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 4)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit4Alarm.setStatus("current")
_LgpConditioniModuleUnit5Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit5Alarm = _LgpConditioniModuleUnit5Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 5)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit5Alarm.setStatus("current")
_LgpConditioniModuleUnit6Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit6Alarm = _LgpConditioniModuleUnit6Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 6)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit6Alarm.setStatus("current")
_LgpConditioniModuleUnit7Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit7Alarm = _LgpConditioniModuleUnit7Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 7)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit7Alarm.setStatus("current")
_LgpConditioniModuleUnit8Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit8Alarm = _LgpConditioniModuleUnit8Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 8)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit8Alarm.setStatus("current")
_LgpConditionActiveModuleAlarm_ObjectIdentity = ObjectIdentity
lgpConditionActiveModuleAlarm = _LgpConditionActiveModuleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 95)
)
if mibBuilder.loadTexts:
    lgpConditionActiveModuleAlarm.setStatus("current")
_LgpConditionControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionControlFailure = _LgpConditionControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96)
)
if mibBuilder.loadTexts:
    lgpConditionControlFailure.setStatus("current")
_LgpConditionMainControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionMainControlFailure = _LgpConditionMainControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMainControlFailure.setStatus("current")
_LgpConditionRedundantControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionRedundantControlFailure = _LgpConditionRedundantControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantControlFailure.setStatus("current")
_LgpConditionParallelSysControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysControlFailure = _LgpConditionParallelSysControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 3)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysControlFailure.setStatus("current")
_LgpConditionMainControlCommFailure_ObjectIdentity = ObjectIdentity
lgpConditionMainControlCommFailure = _LgpConditionMainControlCommFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 4)
)
if mibBuilder.loadTexts:
    lgpConditionMainControlCommFailure.setStatus("current")
_LgpConditionControlBoardFailure_ObjectIdentity = ObjectIdentity
lgpConditionControlBoardFailure = _LgpConditionControlBoardFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 5)
)
if mibBuilder.loadTexts:
    lgpConditionControlBoardFailure.setStatus("current")
_LgpConditionHumidifierControlBdFailure_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierControlBdFailure = _LgpConditionHumidifierControlBdFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 5, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierControlBdFailure.setStatus("current")
_LgpConditionControlWarning_ObjectIdentity = ObjectIdentity
lgpConditionControlWarning = _LgpConditionControlWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 97)
)
if mibBuilder.loadTexts:
    lgpConditionControlWarning.setStatus("current")
_LgpConditionMainControlWarning_ObjectIdentity = ObjectIdentity
lgpConditionMainControlWarning = _LgpConditionMainControlWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 97, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMainControlWarning.setStatus("current")
_LgpConditionRedundantControlWarning_ObjectIdentity = ObjectIdentity
lgpConditionRedundantControlWarning = _LgpConditionRedundantControlWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 97, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantControlWarning.setStatus("current")
_LgpConditionUserInterfaceFailure_ObjectIdentity = ObjectIdentity
lgpConditionUserInterfaceFailure = _LgpConditionUserInterfaceFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 98)
)
if mibBuilder.loadTexts:
    lgpConditionUserInterfaceFailure.setStatus("current")
_LgpConditionLostPowerRedundancy_ObjectIdentity = ObjectIdentity
lgpConditionLostPowerRedundancy = _LgpConditionLostPowerRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 99)
)
if mibBuilder.loadTexts:
    lgpConditionLostPowerRedundancy.setStatus("current")
_LgpConditionPowerModuleFailure_ObjectIdentity = ObjectIdentity
lgpConditionPowerModuleFailure = _LgpConditionPowerModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 100)
)
if mibBuilder.loadTexts:
    lgpConditionPowerModuleFailure.setStatus("current")
_LgpConditionBatteryModuleFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryModuleFailure = _LgpConditionBatteryModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 101)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryModuleFailure.setStatus("current")
_LgpConditionOutputToLoadOff_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOff = _LgpConditionOutputToLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 102)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOff.setStatus("current")
_LgpConditionSystemOff_ObjectIdentity = ObjectIdentity
lgpConditionSystemOff = _LgpConditionSystemOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 103)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOff.setStatus("current")
_LgpConditionRectifierStartupFailure_ObjectIdentity = ObjectIdentity
lgpConditionRectifierStartupFailure = _LgpConditionRectifierStartupFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 104)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierStartupFailure.setStatus("current")
_LgpConditionRectifierFault_ObjectIdentity = ObjectIdentity
lgpConditionRectifierFault = _LgpConditionRectifierFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 105)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierFault.setStatus("current")
_LgpConditionInverterShutdownLowDc_ObjectIdentity = ObjectIdentity
lgpConditionInverterShutdownLowDc = _LgpConditionInverterShutdownLowDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 106)
)
if mibBuilder.loadTexts:
    lgpConditionInverterShutdownLowDc.setStatus("current")
_LgpConditionInverterFault_ObjectIdentity = ObjectIdentity
lgpConditionInverterFault = _LgpConditionInverterFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 107)
)
if mibBuilder.loadTexts:
    lgpConditionInverterFault.setStatus("current")
_LgpConditionInverterDcOffsetOverrun_ObjectIdentity = ObjectIdentity
lgpConditionInverterDcOffsetOverrun = _LgpConditionInverterDcOffsetOverrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 108)
)
if mibBuilder.loadTexts:
    lgpConditionInverterDcOffsetOverrun.setStatus("current")
_LgpConditionParallelSysLowBatteryWarning_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysLowBatteryWarning = _LgpConditionParallelSysLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 109)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysLowBatteryWarning.setStatus("current")
_LgpConditionParallelSysLoadShareFault_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysLoadShareFault = _LgpConditionParallelSysLoadShareFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 110)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysLoadShareFault.setStatus("current")
_LgpConditionBatteryFault_ObjectIdentity = ObjectIdentity
lgpConditionBatteryFault = _LgpConditionBatteryFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 111)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryFault.setStatus("current")
_LgpConditionBatteryConverterFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryConverterFailure = _LgpConditionBatteryConverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 112)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryConverterFailure.setStatus("current")
_LgpConditionBatteryBalancerFault_ObjectIdentity = ObjectIdentity
lgpConditionBatteryBalancerFault = _LgpConditionBatteryBalancerFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 113)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryBalancerFault.setStatus("current")
_LgpConditionpsUpsOperationFault_ObjectIdentity = ObjectIdentity
lgpConditionpsUpsOperationFault = _LgpConditionpsUpsOperationFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 114)
)
if mibBuilder.loadTexts:
    lgpConditionpsUpsOperationFault.setStatus("deprecated")
_LgpConditionOutputToLoadOnJointMode_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOnJointMode = _LgpConditionOutputToLoadOnJointMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 115)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOnJointMode.setStatus("current")
_LgpConditionInputNeutralLost_ObjectIdentity = ObjectIdentity
lgpConditionInputNeutralLost = _LgpConditionInputNeutralLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 116)
)
if mibBuilder.loadTexts:
    lgpConditionInputNeutralLost.setStatus("current")
_LgpConditionLowBatteryWarning_ObjectIdentity = ObjectIdentity
lgpConditionLowBatteryWarning = _LgpConditionLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 117)
)
if mibBuilder.loadTexts:
    lgpConditionLowBatteryWarning.setStatus("current")
_LgpConditionInternalFault_ObjectIdentity = ObjectIdentity
lgpConditionInternalFault = _LgpConditionInternalFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 118)
)
if mibBuilder.loadTexts:
    lgpConditionInternalFault.setStatus("current")
_LgpConditionBatteryTestFailed_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTestFailed = _LgpConditionBatteryTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 119)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTestFailed.setStatus("current")
_LgpConditionPowerModuleWarning_ObjectIdentity = ObjectIdentity
lgpConditionPowerModuleWarning = _LgpConditionPowerModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 120)
)
if mibBuilder.loadTexts:
    lgpConditionPowerModuleWarning.setStatus("current")
_LgpConditionBatteryModuleWarning_ObjectIdentity = ObjectIdentity
lgpConditionBatteryModuleWarning = _LgpConditionBatteryModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 121)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryModuleWarning.setStatus("current")
_LgpConditionControlModuleWarning_ObjectIdentity = ObjectIdentity
lgpConditionControlModuleWarning = _LgpConditionControlModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 122)
)
if mibBuilder.loadTexts:
    lgpConditionControlModuleWarning.setStatus("current")
_LgpConditionUpsOperationFault_ObjectIdentity = ObjectIdentity
lgpConditionUpsOperationFault = _LgpConditionUpsOperationFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 123)
)
if mibBuilder.loadTexts:
    lgpConditionUpsOperationFault.setStatus("current")
_LgpConditionActiveAlarm_ObjectIdentity = ObjectIdentity
lgpConditionActiveAlarm = _LgpConditionActiveAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 124)
)
if mibBuilder.loadTexts:
    lgpConditionActiveAlarm.setStatus("current")
_LgpConditionRectifierCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionRectifierCommunicationFailure = _LgpConditionRectifierCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 125)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierCommunicationFailure.setStatus("current")
_LgpConditionInverterCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionInverterCommunicationFailure = _LgpConditionInverterCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 126)
)
if mibBuilder.loadTexts:
    lgpConditionInverterCommunicationFailure.setStatus("current")
_LgpConditionParallelSysConnectionFault_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysConnectionFault = _LgpConditionParallelSysConnectionFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 127)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysConnectionFault.setStatus("current")
_LgpConditionParallelSysCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysCommunicationFailure = _LgpConditionParallelSysCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 128)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysCommunicationFailure.setStatus("current")
_LgpConditionLostBatteryRedundancy_ObjectIdentity = ObjectIdentity
lgpConditionLostBatteryRedundancy = _LgpConditionLostBatteryRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 129)
)
if mibBuilder.loadTexts:
    lgpConditionLostBatteryRedundancy.setStatus("current")
_LgpConditionCompPumpDownFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompPumpDownFailure = _LgpConditionCompPumpDownFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 130)
)
if mibBuilder.loadTexts:
    lgpConditionCompPumpDownFailure.setStatus("current")
_LgpConditionComp1PumpDownFailure_ObjectIdentity = ObjectIdentity
lgpConditionComp1PumpDownFailure = _LgpConditionComp1PumpDownFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 130, 1)
)
if mibBuilder.loadTexts:
    lgpConditionComp1PumpDownFailure.setStatus("current")
_LgpConditionComp2PumpDownFailure_ObjectIdentity = ObjectIdentity
lgpConditionComp2PumpDownFailure = _LgpConditionComp2PumpDownFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 130, 2)
)
if mibBuilder.loadTexts:
    lgpConditionComp2PumpDownFailure.setStatus("current")
_LgpConditionChilledWaterLowWaterFlow_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterLowWaterFlow = _LgpConditionChilledWaterLowWaterFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 131)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterLowWaterFlow.setStatus("current")
_LgpConditionChilledWaterLowWaterFlowCircuit2_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterLowWaterFlowCircuit2 = _LgpConditionChilledWaterLowWaterFlowCircuit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 131, 2)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterLowWaterFlowCircuit2.setStatus("current")
_LgpConditionAirFilterClogged_ObjectIdentity = ObjectIdentity
lgpConditionAirFilterClogged = _LgpConditionAirFilterClogged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 132)
)
if mibBuilder.loadTexts:
    lgpConditionAirFilterClogged.setStatus("deprecated")
_LgpConditionHumidifierFailure_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierFailure = _LgpConditionHumidifierFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 133)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierFailure.setStatus("current")
_LgpConditionRunHoursExceeded_ObjectIdentity = ObjectIdentity
lgpConditionRunHoursExceeded = _LgpConditionRunHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134)
)
if mibBuilder.loadTexts:
    lgpConditionRunHoursExceeded.setStatus("current")
_LgpConditionUnitRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionUnitRunHrsExceeded = _LgpConditionUnitRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 1)
)
if mibBuilder.loadTexts:
    lgpConditionUnitRunHrsExceeded.setStatus("current")
_LgpConditionComp1RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionComp1RunHrsExceeded = _LgpConditionComp1RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 2)
)
if mibBuilder.loadTexts:
    lgpConditionComp1RunHrsExceeded.setStatus("current")
_LgpConditionComp2RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionComp2RunHrsExceeded = _LgpConditionComp2RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 3)
)
if mibBuilder.loadTexts:
    lgpConditionComp2RunHrsExceeded.setStatus("current")
_LgpConditionFreeCoolRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionFreeCoolRunHrsExceeded = _LgpConditionFreeCoolRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 4)
)
if mibBuilder.loadTexts:
    lgpConditionFreeCoolRunHrsExceeded.setStatus("current")
_LgpConditionElectricalHeater1RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionElectricalHeater1RunHrsExceeded = _LgpConditionElectricalHeater1RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 5)
)
if mibBuilder.loadTexts:
    lgpConditionElectricalHeater1RunHrsExceeded.setStatus("current")
_LgpConditionElectricalHeater2RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionElectricalHeater2RunHrsExceeded = _LgpConditionElectricalHeater2RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 6)
)
if mibBuilder.loadTexts:
    lgpConditionElectricalHeater2RunHrsExceeded.setStatus("current")
_LgpConditionElectricalHeater3RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionElectricalHeater3RunHrsExceeded = _LgpConditionElectricalHeater3RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 7)
)
if mibBuilder.loadTexts:
    lgpConditionElectricalHeater3RunHrsExceeded.setStatus("current")
_LgpConditionHotWaterRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionHotWaterRunHrsExceeded = _LgpConditionHotWaterRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 8)
)
if mibBuilder.loadTexts:
    lgpConditionHotWaterRunHrsExceeded.setStatus("current")
_LgpConditionHotGasRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionHotGasRunHrsExceeded = _LgpConditionHotGasRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 9)
)
if mibBuilder.loadTexts:
    lgpConditionHotGasRunHrsExceeded.setStatus("current")
_LgpConditionHumidifierRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierRunHrsExceeded = _LgpConditionHumidifierRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 10)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierRunHrsExceeded.setStatus("current")
_LgpConditionDehumidiferRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionDehumidiferRunHrsExceeded = _LgpConditionDehumidiferRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 11)
)
if mibBuilder.loadTexts:
    lgpConditionDehumidiferRunHrsExceeded.setStatus("current")
_LgpConditionFanRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionFanRunHrsExceeded = _LgpConditionFanRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 12)
)
if mibBuilder.loadTexts:
    lgpConditionFanRunHrsExceeded.setStatus("current")
_LgpConditionCommWarning_ObjectIdentity = ObjectIdentity
lgpConditionCommWarning = _LgpConditionCommWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarning.setStatus("current")
_LgpConditionCommWarningUnit1_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit1 = _LgpConditionCommWarningUnit1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit1.setStatus("current")
_LgpConditionCommWarningUnit2_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit2 = _LgpConditionCommWarningUnit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit2.setStatus("current")
_LgpConditionCommWarningUnit3_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit3 = _LgpConditionCommWarningUnit3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit3.setStatus("current")
_LgpConditionCommWarningUnit4_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit4 = _LgpConditionCommWarningUnit4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 4)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit4.setStatus("current")
_LgpConditionCommWarningUnit5_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit5 = _LgpConditionCommWarningUnit5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 5)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit5.setStatus("current")
_LgpConditionCommWarningUnit6_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit6 = _LgpConditionCommWarningUnit6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 6)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit6.setStatus("current")
_LgpConditionCommWarningUnit7_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit7 = _LgpConditionCommWarningUnit7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 7)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit7.setStatus("current")
_LgpConditionCommWarningUnit8_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit8 = _LgpConditionCommWarningUnit8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 8)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit8.setStatus("current")
_LgpConditionCommWarningUnit9_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit9 = _LgpConditionCommWarningUnit9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 9)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit9.setStatus("current")
_LgpConditionCommWarningUnit10_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit10 = _LgpConditionCommWarningUnit10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 10)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit10.setStatus("current")
_LgpConditionCommWarningUnit11_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit11 = _LgpConditionCommWarningUnit11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 11)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit11.setStatus("current")
_LgpConditionCommWarningUnit12_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit12 = _LgpConditionCommWarningUnit12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 12)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit12.setStatus("current")
_LgpConditionCommWarningUnit13_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit13 = _LgpConditionCommWarningUnit13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 13)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit13.setStatus("current")
_LgpConditionCommWarningUnit14_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit14 = _LgpConditionCommWarningUnit14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 14)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit14.setStatus("current")
_LgpConditionCommWarningUnit15_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit15 = _LgpConditionCommWarningUnit15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 15)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit15.setStatus("current")
_LgpConditionCommWarningUnit16_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit16 = _LgpConditionCommWarningUnit16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 16)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit16.setStatus("current")
_LgpConditionUnitOn_ObjectIdentity = ObjectIdentity
lgpConditionUnitOn = _LgpConditionUnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 136)
)
if mibBuilder.loadTexts:
    lgpConditionUnitOn.setStatus("current")
_LgpConditionUnitOff_ObjectIdentity = ObjectIdentity
lgpConditionUnitOff = _LgpConditionUnitOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 137)
)
if mibBuilder.loadTexts:
    lgpConditionUnitOff.setStatus("current")
_LgpConditionSleepModeOff_ObjectIdentity = ObjectIdentity
lgpConditionSleepModeOff = _LgpConditionSleepModeOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 138)
)
if mibBuilder.loadTexts:
    lgpConditionSleepModeOff.setStatus("current")
_LgpConditionPowerOn_ObjectIdentity = ObjectIdentity
lgpConditionPowerOn = _LgpConditionPowerOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 139)
)
if mibBuilder.loadTexts:
    lgpConditionPowerOn.setStatus("current")
_LgpConditionSystemOnStanby_ObjectIdentity = ObjectIdentity
lgpConditionSystemOnStanby = _LgpConditionSystemOnStanby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 140)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOnStanby.setStatus("current")
_LgpConditionPowerOff_ObjectIdentity = ObjectIdentity
lgpConditionPowerOff = _LgpConditionPowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 141)
)
if mibBuilder.loadTexts:
    lgpConditionPowerOff.setStatus("current")
_LgpConditionHighTemperatureGroup_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureGroup = _LgpConditionHighTemperatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureGroup.setStatus("current")
_LgpConditionHighTemperatureSensor1_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureSensor1 = _LgpConditionHighTemperatureSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureSensor1.setStatus("current")
_LgpConditionHighTemperatureDigitalScroll1_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureDigitalScroll1 = _LgpConditionHighTemperatureDigitalScroll1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 2)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureDigitalScroll1.setStatus("current")
_LgpConditionHighTemperatureDigitalScroll2_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureDigitalScroll2 = _LgpConditionHighTemperatureDigitalScroll2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 3)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureDigitalScroll2.setStatus("current")
_LgpConditionHighTemperatureUser1_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureUser1 = _LgpConditionHighTemperatureUser1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 4)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureUser1.setStatus("current")
_LgpConditionHighTemperatureInternal_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureInternal = _LgpConditionHighTemperatureInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 5)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureInternal.setStatus("current")
_LgpConditionHighTemperatureExternalAirSensorA_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureExternalAirSensorA = _LgpConditionHighTemperatureExternalAirSensorA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 6)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureExternalAirSensorA.setStatus("current")
_LgpConditionHighTemperatureExternalAirSensorB_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureExternalAirSensorB = _LgpConditionHighTemperatureExternalAirSensorB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 7)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureExternalAirSensorB.setStatus("current")
_LgpConditionHighTemperatureRefrigerantSupply_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureRefrigerantSupply = _LgpConditionHighTemperatureRefrigerantSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 8)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureRefrigerantSupply.setStatus("current")
_LgpConditionHighTemperatureFluidSupply_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureFluidSupply = _LgpConditionHighTemperatureFluidSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 9)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureFluidSupply.setStatus("current")
_LgpConditionHighTemperatureSupplyAir_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureSupplyAir = _LgpConditionHighTemperatureSupplyAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 10)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureSupplyAir.setStatus("current")
_LgpConditionHighTemperatureReturnAir_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureReturnAir = _LgpConditionHighTemperatureReturnAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 11)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureReturnAir.setStatus("current")
_LgpConditionLowTemperatureGroup_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureGroup = _LgpConditionLowTemperatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureGroup.setStatus("current")
_LgpConditionLowTemperatureSensor1_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureSensor1 = _LgpConditionLowTemperatureSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureSensor1.setStatus("current")
_LgpConditionLowTemperatureInternal_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureInternal = _LgpConditionLowTemperatureInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureInternal.setStatus("current")
_LgpConditionLowTemperatureExternalAirSensorA_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureExternalAirSensorA = _LgpConditionLowTemperatureExternalAirSensorA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 3)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureExternalAirSensorA.setStatus("current")
_LgpConditionLowTemperatureExternalAirSensorB_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureExternalAirSensorB = _LgpConditionLowTemperatureExternalAirSensorB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureExternalAirSensorB.setStatus("current")
_LgpConditionLowTemperatureRefrigerantSupply_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureRefrigerantSupply = _LgpConditionLowTemperatureRefrigerantSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureRefrigerantSupply.setStatus("current")
_LgpConditionLowTemperatureFluidSupply_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureFluidSupply = _LgpConditionLowTemperatureFluidSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 6)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureFluidSupply.setStatus("current")
_LgpConditionLowTemperatureSupplyAir_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureSupplyAir = _LgpConditionLowTemperatureSupplyAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 7)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureSupplyAir.setStatus("current")
_LgpConditionHighHumidityGroup_ObjectIdentity = ObjectIdentity
lgpConditionHighHumidityGroup = _LgpConditionHighHumidityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 144)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumidityGroup.setStatus("current")
_LgpConditionHighHumiditySensor1_ObjectIdentity = ObjectIdentity
lgpConditionHighHumiditySensor1 = _LgpConditionHighHumiditySensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 144, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumiditySensor1.setStatus("current")
_LgpConditionHighHumidityReturnAir_ObjectIdentity = ObjectIdentity
lgpConditionHighHumidityReturnAir = _LgpConditionHighHumidityReturnAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 144, 2)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumidityReturnAir.setStatus("current")
_LgpConditionLowHumidityGroup_ObjectIdentity = ObjectIdentity
lgpConditionLowHumidityGroup = _LgpConditionLowHumidityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 145)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumidityGroup.setStatus("current")
_LgpConditionLowHumiditySensor1_ObjectIdentity = ObjectIdentity
lgpConditionLowHumiditySensor1 = _LgpConditionLowHumiditySensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 145, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumiditySensor1.setStatus("current")
_LgpConditionLowHumidityReturnAir_ObjectIdentity = ObjectIdentity
lgpConditionLowHumidityReturnAir = _LgpConditionLowHumidityReturnAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 145, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumidityReturnAir.setStatus("current")
_LgpConditionPeerNetworkNoMaster_ObjectIdentity = ObjectIdentity
lgpConditionPeerNetworkNoMaster = _LgpConditionPeerNetworkNoMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 146)
)
if mibBuilder.loadTexts:
    lgpConditionPeerNetworkNoMaster.setStatus("current")
_LgpConditionNoOnOffPermissions_ObjectIdentity = ObjectIdentity
lgpConditionNoOnOffPermissions = _LgpConditionNoOnOffPermissions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 147)
)
if mibBuilder.loadTexts:
    lgpConditionNoOnOffPermissions.setStatus("current")
_LgpConditionPeerNetworkFailure_ObjectIdentity = ObjectIdentity
lgpConditionPeerNetworkFailure = _LgpConditionPeerNetworkFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 148)
)
if mibBuilder.loadTexts:
    lgpConditionPeerNetworkFailure.setStatus("current")
_LgpConditionUnitDisabled_ObjectIdentity = ObjectIdentity
lgpConditionUnitDisabled = _LgpConditionUnitDisabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 149)
)
if mibBuilder.loadTexts:
    lgpConditionUnitDisabled.setStatus("current")
_LgpConditionUnitShutdown_ObjectIdentity = ObjectIdentity
lgpConditionUnitShutdown = _LgpConditionUnitShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 150)
)
if mibBuilder.loadTexts:
    lgpConditionUnitShutdown.setStatus("current")
_LgpConditionPeerNetworkDiscovered_ObjectIdentity = ObjectIdentity
lgpConditionPeerNetworkDiscovered = _LgpConditionPeerNetworkDiscovered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 151)
)
if mibBuilder.loadTexts:
    lgpConditionPeerNetworkDiscovered.setStatus("current")
_LgpConditionLossOfWaterFlow_ObjectIdentity = ObjectIdentity
lgpConditionLossOfWaterFlow = _LgpConditionLossOfWaterFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 152)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfWaterFlow.setStatus("current")
_LgpConditionCondensatePumpHighWater_ObjectIdentity = ObjectIdentity
lgpConditionCondensatePumpHighWater = _LgpConditionCondensatePumpHighWater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 153)
)
if mibBuilder.loadTexts:
    lgpConditionCondensatePumpHighWater.setStatus("current")
_LgpConditionGeneralAlarm_ObjectIdentity = ObjectIdentity
lgpConditionGeneralAlarm = _LgpConditionGeneralAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 154)
)
if mibBuilder.loadTexts:
    lgpConditionGeneralAlarm.setStatus("current")
_LgpConditionProductSpecific_ObjectIdentity = ObjectIdentity
lgpConditionProductSpecific = _LgpConditionProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 155)
)
if mibBuilder.loadTexts:
    lgpConditionProductSpecific.setStatus("current")
_LgpConditionReheatLockout_ObjectIdentity = ObjectIdentity
lgpConditionReheatLockout = _LgpConditionReheatLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 156)
)
if mibBuilder.loadTexts:
    lgpConditionReheatLockout.setStatus("current")
_LgpConditionHumidifierLockout_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierLockout = _LgpConditionHumidifierLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 157)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierLockout.setStatus("current")
_LgpConditionCompressorsLockout_ObjectIdentity = ObjectIdentity
lgpConditionCompressorsLockout = _LgpConditionCompressorsLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 158)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorsLockout.setStatus("current")
_LgpConditionCallService_ObjectIdentity = ObjectIdentity
lgpConditionCallService = _LgpConditionCallService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 159)
)
if mibBuilder.loadTexts:
    lgpConditionCallService.setStatus("current")
_LgpConditionLowMemoryGroup_ObjectIdentity = ObjectIdentity
lgpConditionLowMemoryGroup = _LgpConditionLowMemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 160)
)
if mibBuilder.loadTexts:
    lgpConditionLowMemoryGroup.setStatus("current")
_LgpConditionLowMemory1_ObjectIdentity = ObjectIdentity
lgpConditionLowMemory1 = _LgpConditionLowMemory1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 160, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLowMemory1.setStatus("current")
_LgpConditionMemoryFailureGroup_ObjectIdentity = ObjectIdentity
lgpConditionMemoryFailureGroup = _LgpConditionMemoryFailureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 161)
)
if mibBuilder.loadTexts:
    lgpConditionMemoryFailureGroup.setStatus("current")
_LgpConditionMemory1Failure_ObjectIdentity = ObjectIdentity
lgpConditionMemory1Failure = _LgpConditionMemory1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 161, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMemory1Failure.setStatus("current")
_LgpConditionMemory2Failure_ObjectIdentity = ObjectIdentity
lgpConditionMemory2Failure = _LgpConditionMemory2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 161, 2)
)
if mibBuilder.loadTexts:
    lgpConditionMemory2Failure.setStatus("current")
_LgpConditionUnitCodeErrorGroup_ObjectIdentity = ObjectIdentity
lgpConditionUnitCodeErrorGroup = _LgpConditionUnitCodeErrorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCodeErrorGroup.setStatus("current")
_LgpConditionUnitCodeNotConfigured_ObjectIdentity = ObjectIdentity
lgpConditionUnitCodeNotConfigured = _LgpConditionUnitCodeNotConfigured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 1)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCodeNotConfigured.setStatus("current")
_LgpConditionUnitCode01OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode01OutOfRange = _LgpConditionUnitCode01OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 2)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode01OutOfRange.setStatus("current")
_LgpConditionUnitCode02OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode02OutOfRange = _LgpConditionUnitCode02OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 3)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode02OutOfRange.setStatus("current")
_LgpConditionUnitCode03OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode03OutOfRange = _LgpConditionUnitCode03OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 4)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode03OutOfRange.setStatus("current")
_LgpConditionUnitCode04OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode04OutOfRange = _LgpConditionUnitCode04OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 5)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode04OutOfRange.setStatus("current")
_LgpConditionUnitCode05OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode05OutOfRange = _LgpConditionUnitCode05OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 6)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode05OutOfRange.setStatus("current")
_LgpConditionUnitCode06OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode06OutOfRange = _LgpConditionUnitCode06OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 7)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode06OutOfRange.setStatus("current")
_LgpConditionUnitCode07OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode07OutOfRange = _LgpConditionUnitCode07OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 8)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode07OutOfRange.setStatus("current")
_LgpConditionUnitCode08OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode08OutOfRange = _LgpConditionUnitCode08OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 9)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode08OutOfRange.setStatus("current")
_LgpConditionUnitCode09OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode09OutOfRange = _LgpConditionUnitCode09OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 10)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode09OutOfRange.setStatus("current")
_LgpConditionUnitCode10OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode10OutOfRange = _LgpConditionUnitCode10OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 11)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode10OutOfRange.setStatus("current")
_LgpConditionUnitCode11OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode11OutOfRange = _LgpConditionUnitCode11OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 12)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode11OutOfRange.setStatus("current")
_LgpConditionUnitCode12OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode12OutOfRange = _LgpConditionUnitCode12OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 13)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode12OutOfRange.setStatus("current")
_LgpConditionUnitCode13OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode13OutOfRange = _LgpConditionUnitCode13OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 14)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode13OutOfRange.setStatus("current")
_LgpConditionUnitCode14OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode14OutOfRange = _LgpConditionUnitCode14OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 15)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode14OutOfRange.setStatus("current")
_LgpConditionUnitCode15OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode15OutOfRange = _LgpConditionUnitCode15OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 16)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode15OutOfRange.setStatus("current")
_LgpConditionUnitCode16OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode16OutOfRange = _LgpConditionUnitCode16OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 17)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode16OutOfRange.setStatus("current")
_LgpConditionUnitCode17OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode17OutOfRange = _LgpConditionUnitCode17OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 18)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode17OutOfRange.setStatus("current")
_LgpConditionUnitCode18OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode18OutOfRange = _LgpConditionUnitCode18OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 19)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode18OutOfRange.setStatus("current")
_LgpConditionHighExternalDewPoint_ObjectIdentity = ObjectIdentity
lgpConditionHighExternalDewPoint = _LgpConditionHighExternalDewPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 163)
)
if mibBuilder.loadTexts:
    lgpConditionHighExternalDewPoint.setStatus("current")
_LgpConditionHcbDisconnected_ObjectIdentity = ObjectIdentity
lgpConditionHcbDisconnected = _LgpConditionHcbDisconnected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 164)
)
if mibBuilder.loadTexts:
    lgpConditionHcbDisconnected.setStatus("current")
_LgpConditionBmsResetTimerExpired_ObjectIdentity = ObjectIdentity
lgpConditionBmsResetTimerExpired = _LgpConditionBmsResetTimerExpired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 165)
)
if mibBuilder.loadTexts:
    lgpConditionBmsResetTimerExpired.setStatus("current")
_LgpConditionAgentFirmwareCorrupt_ObjectIdentity = ObjectIdentity
lgpConditionAgentFirmwareCorrupt = _LgpConditionAgentFirmwareCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 166)
)
if mibBuilder.loadTexts:
    lgpConditionAgentFirmwareCorrupt.setStatus("current")
_LgpConditionSystemAccessGroup_ObjectIdentity = ObjectIdentity
lgpConditionSystemAccessGroup = _LgpConditionSystemAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 175)
)
if mibBuilder.loadTexts:
    lgpConditionSystemAccessGroup.setStatus("current")
_LgpConditionFrontAccessOpen_ObjectIdentity = ObjectIdentity
lgpConditionFrontAccessOpen = _LgpConditionFrontAccessOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 175, 1)
)
if mibBuilder.loadTexts:
    lgpConditionFrontAccessOpen.setStatus("current")
_LgpConditionRearAccessOpen_ObjectIdentity = ObjectIdentity
lgpConditionRearAccessOpen = _LgpConditionRearAccessOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 175, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRearAccessOpen.setStatus("current")
_LgpConditionsDamperFailure_ObjectIdentity = ObjectIdentity
lgpConditionsDamperFailure = _LgpConditionsDamperFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 176)
)
if mibBuilder.loadTexts:
    lgpConditionsDamperFailure.setStatus("current")
_LgpConditionEmergencyDamperFailure_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyDamperFailure = _LgpConditionEmergencyDamperFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 176, 1)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyDamperFailure.setStatus("current")
_LgpConditionRemoteShutdown_ObjectIdentity = ObjectIdentity
lgpConditionRemoteShutdown = _LgpConditionRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 177)
)
if mibBuilder.loadTexts:
    lgpConditionRemoteShutdown.setStatus("current")
_LgpConditionFireAlarm_ObjectIdentity = ObjectIdentity
lgpConditionFireAlarm = _LgpConditionFireAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 178)
)
if mibBuilder.loadTexts:
    lgpConditionFireAlarm.setStatus("current")
_LgpConditionHeatersOverheated_ObjectIdentity = ObjectIdentity
lgpConditionHeatersOverheated = _LgpConditionHeatersOverheated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 179)
)
if mibBuilder.loadTexts:
    lgpConditionHeatersOverheated.setStatus("current")
_LgpConditionCondenserFailureGroup_ObjectIdentity = ObjectIdentity
lgpConditionCondenserFailureGroup = _LgpConditionCondenserFailureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserFailureGroup.setStatus("current")
_LgpConditionCondenser1Failure_ObjectIdentity = ObjectIdentity
lgpConditionCondenser1Failure = _LgpConditionCondenser1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCondenser1Failure.setStatus("current")
_LgpConditionCondenser2Failure_ObjectIdentity = ObjectIdentity
lgpConditionCondenser2Failure = _LgpConditionCondenser2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCondenser2Failure.setStatus("current")
_LgpConditionCondenserTVSSFailure_ObjectIdentity = ObjectIdentity
lgpConditionCondenserTVSSFailure = _LgpConditionCondenserTVSSFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserTVSSFailure.setStatus("current")
_LgpConditionHumidifierCyclinderWorn_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierCyclinderWorn = _LgpConditionHumidifierCyclinderWorn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 181)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierCyclinderWorn.setStatus("current")
_LgpConditionUnderCurrent_ObjectIdentity = ObjectIdentity
lgpConditionUnderCurrent = _LgpConditionUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 182)
)
if mibBuilder.loadTexts:
    lgpConditionUnderCurrent.setStatus("current")
_LgpConditionHumidifierUnderCurrent_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierUnderCurrent = _LgpConditionHumidifierUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 182, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierUnderCurrent.setStatus("current")
_LgpConditionInputUnderCurrent_ObjectIdentity = ObjectIdentity
lgpConditionInputUnderCurrent = _LgpConditionInputUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 182, 2)
)
if mibBuilder.loadTexts:
    lgpConditionInputUnderCurrent.setStatus("current")
_LgpConditionHeatRejectorGroup_ObjectIdentity = ObjectIdentity
lgpConditionHeatRejectorGroup = _LgpConditionHeatRejectorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 183)
)
if mibBuilder.loadTexts:
    lgpConditionHeatRejectorGroup.setStatus("current")
_LgpConditionHeatRejectorFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionHeatRejectorFanFailure = _LgpConditionHeatRejectorFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 183, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHeatRejectorFanFailure.setStatus("current")
_LgpConditionHeatRejectorVoltageSuppressionFailure_ObjectIdentity = ObjectIdentity
lgpConditionHeatRejectorVoltageSuppressionFailure = _LgpConditionHeatRejectorVoltageSuppressionFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 183, 2)
)
if mibBuilder.loadTexts:
    lgpConditionHeatRejectorVoltageSuppressionFailure.setStatus("current")
_LgpConditionFreeCoolLockout_ObjectIdentity = ObjectIdentity
lgpConditionFreeCoolLockout = _LgpConditionFreeCoolLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 184)
)
if mibBuilder.loadTexts:
    lgpConditionFreeCoolLockout.setStatus("current")
_LgpConditionWaterLeakSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionWaterLeakSensorFailure = _LgpConditionWaterLeakSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 185)
)
if mibBuilder.loadTexts:
    lgpConditionWaterLeakSensorFailure.setStatus("current")
_LgpConditionNoLoadDetectedWarning_ObjectIdentity = ObjectIdentity
lgpConditionNoLoadDetectedWarning = _LgpConditionNoLoadDetectedWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 186)
)
if mibBuilder.loadTexts:
    lgpConditionNoLoadDetectedWarning.setStatus("current")
_LgpConditionFirmwareGroup_ObjectIdentity = ObjectIdentity
lgpConditionFirmwareGroup = _LgpConditionFirmwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 187)
)
if mibBuilder.loadTexts:
    lgpConditionFirmwareGroup.setStatus("current")
_LgpConditionFirmwareUpdateRequired_ObjectIdentity = ObjectIdentity
lgpConditionFirmwareUpdateRequired = _LgpConditionFirmwareUpdateRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 187, 3)
)
if mibBuilder.loadTexts:
    lgpConditionFirmwareUpdateRequired.setStatus("current")
_LgpConditionTestGroup_ObjectIdentity = ObjectIdentity
lgpConditionTestGroup = _LgpConditionTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 188)
)
if mibBuilder.loadTexts:
    lgpConditionTestGroup.setStatus("current")
_LgpConditionTest01_ObjectIdentity = ObjectIdentity
lgpConditionTest01 = _LgpConditionTest01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 188, 5)
)
if mibBuilder.loadTexts:
    lgpConditionTest01.setStatus("current")
_LgpConditionReceptacleBranchGroup_ObjectIdentity = ObjectIdentity
lgpConditionReceptacleBranchGroup = _LgpConditionReceptacleBranchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 190)
)
if mibBuilder.loadTexts:
    lgpConditionReceptacleBranchGroup.setStatus("current")
_LgpConditionRcpBranchFailure_ObjectIdentity = ObjectIdentity
lgpConditionRcpBranchFailure = _LgpConditionRcpBranchFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 190, 5)
)
if mibBuilder.loadTexts:
    lgpConditionRcpBranchFailure.setStatus("current")
_LgpConditionRcpBranchBreakerOpen_ObjectIdentity = ObjectIdentity
lgpConditionRcpBranchBreakerOpen = _LgpConditionRcpBranchBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 190, 10)
)
if mibBuilder.loadTexts:
    lgpConditionRcpBranchBreakerOpen.setStatus("current")
_LgpConditionInputUnqualified_ObjectIdentity = ObjectIdentity
lgpConditionInputUnqualified = _LgpConditionInputUnqualified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 192)
)
if mibBuilder.loadTexts:
    lgpConditionInputUnqualified.setStatus("current")
_LgpConditionBypassUnavailable_ObjectIdentity = ObjectIdentity
lgpConditionBypassUnavailable = _LgpConditionBypassUnavailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 193)
)
if mibBuilder.loadTexts:
    lgpConditionBypassUnavailable.setStatus("current")
_LgpConditionAutoTransferFailed_ObjectIdentity = ObjectIdentity
lgpConditionAutoTransferFailed = _LgpConditionAutoTransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 194)
)
if mibBuilder.loadTexts:
    lgpConditionAutoTransferFailed.setStatus("current")
_LgpConditionSBSUnavailable_ObjectIdentity = ObjectIdentity
lgpConditionSBSUnavailable = _LgpConditionSBSUnavailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 195)
)
if mibBuilder.loadTexts:
    lgpConditionSBSUnavailable.setStatus("current")
_LgpConditionSBSOverload_ObjectIdentity = ObjectIdentity
lgpConditionSBSOverload = _LgpConditionSBSOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 196)
)
if mibBuilder.loadTexts:
    lgpConditionSBSOverload.setStatus("current")
_LgpConditionExcessPulseParallel_ObjectIdentity = ObjectIdentity
lgpConditionExcessPulseParallel = _LgpConditionExcessPulseParallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 197)
)
if mibBuilder.loadTexts:
    lgpConditionExcessPulseParallel.setStatus("current")
_LgpConditionRemoteBypassSwitchOffExt_ObjectIdentity = ObjectIdentity
lgpConditionRemoteBypassSwitchOffExt = _LgpConditionRemoteBypassSwitchOffExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 198)
)
if mibBuilder.loadTexts:
    lgpConditionRemoteBypassSwitchOffExt.setStatus("current")
_LgpConditionManTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionManTransferInhibited = _LgpConditionManTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 199)
)
if mibBuilder.loadTexts:
    lgpConditionManTransferInhibited.setStatus("current")
_LgpConditionManReTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionManReTransferInhibited = _LgpConditionManReTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 200)
)
if mibBuilder.loadTexts:
    lgpConditionManReTransferInhibited.setStatus("current")
_LgpConditionBatteryChargeError_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargeError = _LgpConditionBatteryChargeError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 201)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargeError.setStatus("current")
_LgpConditionBatteryAutoTestInhibited_ObjectIdentity = ObjectIdentity
lgpConditionBatteryAutoTestInhibited = _LgpConditionBatteryAutoTestInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 202)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryAutoTestInhibited.setStatus("current")
_LgpConditionBatteryChargeReducedExt_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargeReducedExt = _LgpConditionBatteryChargeReducedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 203)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargeReducedExt.setStatus("current")
_LgpConditionBatteryCapacityLow_ObjectIdentity = ObjectIdentity
lgpConditionBatteryCapacityLow = _LgpConditionBatteryCapacityLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 204)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryCapacityLow.setStatus("current")
_LgpConditionBatteryTempImbalance_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTempImbalance = _LgpConditionBatteryTempImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 205)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTempImbalance.setStatus("current")
_LgpConditionBatteryEqualize_ObjectIdentity = ObjectIdentity
lgpConditionBatteryEqualize = _LgpConditionBatteryEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 206)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryEqualize.setStatus("current")
_LgpConditionBatteryChargeInhibitedExt_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargeInhibitedExt = _LgpConditionBatteryChargeInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 207)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargeInhibitedExt.setStatus("current")
_LgpConditionServiceExtBatteryMonitorGroup_ObjectIdentity = ObjectIdentity
lgpConditionServiceExtBatteryMonitorGroup = _LgpConditionServiceExtBatteryMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 208)
)
if mibBuilder.loadTexts:
    lgpConditionServiceExtBatteryMonitorGroup.setStatus("current")
_LgpConditionServiceExtBatteryMonitor1_ObjectIdentity = ObjectIdentity
lgpConditionServiceExtBatteryMonitor1 = _LgpConditionServiceExtBatteryMonitor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 208, 1)
)
if mibBuilder.loadTexts:
    lgpConditionServiceExtBatteryMonitor1.setStatus("current")
_LgpConditionServiceExtBatteryMonitor2_ObjectIdentity = ObjectIdentity
lgpConditionServiceExtBatteryMonitor2 = _LgpConditionServiceExtBatteryMonitor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 208, 2)
)
if mibBuilder.loadTexts:
    lgpConditionServiceExtBatteryMonitor2.setStatus("current")
_LgpConditionBatteryGroundFault_ObjectIdentity = ObjectIdentity
lgpConditionBatteryGroundFault = _LgpConditionBatteryGroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 209)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryGroundFault.setStatus("current")
_LgpConditionBatteryLowShutdown_ObjectIdentity = ObjectIdentity
lgpConditionBatteryLowShutdown = _LgpConditionBatteryLowShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 210)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryLowShutdown.setStatus("current")
_LgpConditionEmergencyPowerOffLocal_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyPowerOffLocal = _LgpConditionEmergencyPowerOffLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 211)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyPowerOffLocal.setStatus("current")
_LgpConditionOutputLowPFLagging_ObjectIdentity = ObjectIdentity
lgpConditionOutputLowPFLagging = _LgpConditionOutputLowPFLagging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 212)
)
if mibBuilder.loadTexts:
    lgpConditionOutputLowPFLagging.setStatus("current")
_LgpConditionOutputLowPFLeading_ObjectIdentity = ObjectIdentity
lgpConditionOutputLowPFLeading = _LgpConditionOutputLowPFLeading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 213)
)
if mibBuilder.loadTexts:
    lgpConditionOutputLowPFLeading.setStatus("current")
_LgpConditionOutputToLoadFault_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadFault = _LgpConditionOutputToLoadFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 214)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadFault.setStatus("current")
_LgpConditionInvRestartInhibitedExt_ObjectIdentity = ObjectIdentity
lgpConditionInvRestartInhibitedExt = _LgpConditionInvRestartInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 215)
)
if mibBuilder.loadTexts:
    lgpConditionInvRestartInhibitedExt.setStatus("current")
_LgpConditionInverterShutdownOverload_ObjectIdentity = ObjectIdentity
lgpConditionInverterShutdownOverload = _LgpConditionInverterShutdownOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 216)
)
if mibBuilder.loadTexts:
    lgpConditionInverterShutdownOverload.setStatus("current")
_LgpConditionInverterOffExt_ObjectIdentity = ObjectIdentity
lgpConditionInverterOffExt = _LgpConditionInverterOffExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 217)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOffExt.setStatus("current")
_LgpConditionInputContactGroup_ObjectIdentity = ObjectIdentity
lgpConditionInputContactGroup = _LgpConditionInputContactGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218)
)
if mibBuilder.loadTexts:
    lgpConditionInputContactGroup.setStatus("current")
_LgpConditionInputContact01_ObjectIdentity = ObjectIdentity
lgpConditionInputContact01 = _LgpConditionInputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 1)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact01.setStatus("current")
_LgpConditionInputContact02_ObjectIdentity = ObjectIdentity
lgpConditionInputContact02 = _LgpConditionInputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 2)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact02.setStatus("current")
_LgpConditionInputContact03_ObjectIdentity = ObjectIdentity
lgpConditionInputContact03 = _LgpConditionInputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 3)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact03.setStatus("current")
_LgpConditionInputContact04_ObjectIdentity = ObjectIdentity
lgpConditionInputContact04 = _LgpConditionInputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact04.setStatus("current")
_LgpConditionInputContact05_ObjectIdentity = ObjectIdentity
lgpConditionInputContact05 = _LgpConditionInputContact05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 5)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact05.setStatus("current")
_LgpConditionInputContact06_ObjectIdentity = ObjectIdentity
lgpConditionInputContact06 = _LgpConditionInputContact06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 6)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact06.setStatus("current")
_LgpConditionInputContact07_ObjectIdentity = ObjectIdentity
lgpConditionInputContact07 = _LgpConditionInputContact07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 7)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact07.setStatus("current")
_LgpConditionInputContact08_ObjectIdentity = ObjectIdentity
lgpConditionInputContact08 = _LgpConditionInputContact08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 8)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact08.setStatus("current")
_LgpConditionInputContact09_ObjectIdentity = ObjectIdentity
lgpConditionInputContact09 = _LgpConditionInputContact09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 9)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact09.setStatus("current")
_LgpConditionInputContact10_ObjectIdentity = ObjectIdentity
lgpConditionInputContact10 = _LgpConditionInputContact10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 10)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact10.setStatus("current")
_LgpConditionInputContact11_ObjectIdentity = ObjectIdentity
lgpConditionInputContact11 = _LgpConditionInputContact11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 11)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact11.setStatus("current")
_LgpConditionInputContact12_ObjectIdentity = ObjectIdentity
lgpConditionInputContact12 = _LgpConditionInputContact12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 12)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact12.setStatus("current")
_LgpConditionInputContact13_ObjectIdentity = ObjectIdentity
lgpConditionInputContact13 = _LgpConditionInputContact13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 13)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact13.setStatus("current")
_LgpConditionInputContact14_ObjectIdentity = ObjectIdentity
lgpConditionInputContact14 = _LgpConditionInputContact14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 14)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact14.setStatus("current")
_LgpConditionInputContact15_ObjectIdentity = ObjectIdentity
lgpConditionInputContact15 = _LgpConditionInputContact15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 15)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact15.setStatus("current")
_LgpConditionInputContact16_ObjectIdentity = ObjectIdentity
lgpConditionInputContact16 = _LgpConditionInputContact16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 16)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact16.setStatus("current")
_LgpConditionRectifierOperInhibited_ObjectIdentity = ObjectIdentity
lgpConditionRectifierOperInhibited = _LgpConditionRectifierOperInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 219)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierOperInhibited.setStatus("current")
_LgpConditionBypassBackFeedBrkrOpen_ObjectIdentity = ObjectIdentity
lgpConditionBypassBackFeedBrkrOpen = _LgpConditionBypassBackFeedBrkrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 220)
)
if mibBuilder.loadTexts:
    lgpConditionBypassBackFeedBrkrOpen.setStatus("current")
_LgpConditionAutoRestartInProgress_ObjectIdentity = ObjectIdentity
lgpConditionAutoRestartInProgress = _LgpConditionAutoRestartInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 221)
)
if mibBuilder.loadTexts:
    lgpConditionAutoRestartInProgress.setStatus("current")
_LgpConditionAutoRestartInhibitedExt_ObjectIdentity = ObjectIdentity
lgpConditionAutoRestartInhibitedExt = _LgpConditionAutoRestartInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 222)
)
if mibBuilder.loadTexts:
    lgpConditionAutoRestartInhibitedExt.setStatus("current")
_LgpConditionAutoRestartFailed_ObjectIdentity = ObjectIdentity
lgpConditionAutoRestartFailed = _LgpConditionAutoRestartFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 223)
)
if mibBuilder.loadTexts:
    lgpConditionAutoRestartFailed.setStatus("current")
_LgpConditionInputOnGenerator_ObjectIdentity = ObjectIdentity
lgpConditionInputOnGenerator = _LgpConditionInputOnGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 224)
)
if mibBuilder.loadTexts:
    lgpConditionInputOnGenerator.setStatus("current")
_LgpConditionInputFilterCycleLock_ObjectIdentity = ObjectIdentity
lgpConditionInputFilterCycleLock = _LgpConditionInputFilterCycleLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 225)
)
if mibBuilder.loadTexts:
    lgpConditionInputFilterCycleLock.setStatus("current")
_LgpConditionServiceCodeActive_ObjectIdentity = ObjectIdentity
lgpConditionServiceCodeActive = _LgpConditionServiceCodeActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 226)
)
if mibBuilder.loadTexts:
    lgpConditionServiceCodeActive.setStatus("current")
_LgpConditionLoadBusSyncActive_ObjectIdentity = ObjectIdentity
lgpConditionLoadBusSyncActive = _LgpConditionLoadBusSyncActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 227)
)
if mibBuilder.loadTexts:
    lgpConditionLoadBusSyncActive.setStatus("current")
_LgpConditionLoadBusSyncInhibited_ObjectIdentity = ObjectIdentity
lgpConditionLoadBusSyncInhibited = _LgpConditionLoadBusSyncInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 228)
)
if mibBuilder.loadTexts:
    lgpConditionLoadBusSyncInhibited.setStatus("current")
_LgpConditionControlsResetRequired_ObjectIdentity = ObjectIdentity
lgpConditionControlsResetRequired = _LgpConditionControlsResetRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 229)
)
if mibBuilder.loadTexts:
    lgpConditionControlsResetRequired.setStatus("current")
_LgpConditionEquipTempSensorFailed_ObjectIdentity = ObjectIdentity
lgpConditionEquipTempSensorFailed = _LgpConditionEquipTempSensorFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 230)
)
if mibBuilder.loadTexts:
    lgpConditionEquipTempSensorFailed.setStatus("current")
_LgpConditionInputCurrentImbalance_ObjectIdentity = ObjectIdentity
lgpConditionInputCurrentImbalance = _LgpConditionInputCurrentImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 231)
)
if mibBuilder.loadTexts:
    lgpConditionInputCurrentImbalance.setStatus("current")
_LgpConditionPumpGroup_ObjectIdentity = ObjectIdentity
lgpConditionPumpGroup = _LgpConditionPumpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232)
)
if mibBuilder.loadTexts:
    lgpConditionPumpGroup.setStatus("current")
_LgpConditionPumpFlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionPumpFlowLoss = _LgpConditionPumpFlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPumpFlowLoss.setStatus("current")
_LgpConditionPump1FlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionPump1FlowLoss = _LgpConditionPump1FlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPump1FlowLoss.setStatus("current")
_LgpConditionPump2FlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionPump2FlowLoss = _LgpConditionPump2FlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPump2FlowLoss.setStatus("current")
_LgpConditionPumpShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPumpShortCycle = _LgpConditionPumpShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPumpShortCycle.setStatus("current")
_LgpConditionPumpInverterShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPumpInverterShortCycle = _LgpConditionPumpInverterShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 3)
)
if mibBuilder.loadTexts:
    lgpConditionPumpInverterShortCycle.setStatus("current")
_LgpConditionPump1InverterShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPump1InverterShortCycle = _LgpConditionPump1InverterShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 3, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPump1InverterShortCycle.setStatus("current")
_LgpConditionPump2InverterShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPump2InverterShortCycle = _LgpConditionPump2InverterShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 3, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPump2InverterShortCycle.setStatus("current")
_LgpConditionValveGroup_ObjectIdentity = ObjectIdentity
lgpConditionValveGroup = _LgpConditionValveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 233)
)
if mibBuilder.loadTexts:
    lgpConditionValveGroup.setStatus("current")
_LgpConditionChilledWaterValvePosition_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterValvePosition = _LgpConditionChilledWaterValvePosition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 233, 1)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterValvePosition.setStatus("current")
_LgpConditionCondensationDetected_ObjectIdentity = ObjectIdentity
lgpConditionCondensationDetected = _LgpConditionCondensationDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 234)
)
if mibBuilder.loadTexts:
    lgpConditionCondensationDetected.setStatus("current")
_LgpConditionMaintenanceGroup_ObjectIdentity = ObjectIdentity
lgpConditionMaintenanceGroup = _LgpConditionMaintenanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 235)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenanceGroup.setStatus("current")
_LgpConditionMaintenanceDue_ObjectIdentity = ObjectIdentity
lgpConditionMaintenanceDue = _LgpConditionMaintenanceDue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 235, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenanceDue.setStatus("current")
_LgpConditionMaintenanceComplete_ObjectIdentity = ObjectIdentity
lgpConditionMaintenanceComplete = _LgpConditionMaintenanceComplete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 235, 2)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenanceComplete.setStatus("current")
_LgpConditionExternalEventSignalGroup_ObjectIdentity = ObjectIdentity
lgpConditionExternalEventSignalGroup = _LgpConditionExternalEventSignalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236)
)
if mibBuilder.loadTexts:
    lgpConditionExternalEventSignalGroup.setStatus("current")
_LgpConditionExternalFireDetect_ObjectIdentity = ObjectIdentity
lgpConditionExternalFireDetect = _LgpConditionExternalFireDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 1)
)
if mibBuilder.loadTexts:
    lgpConditionExternalFireDetect.setStatus("current")
_LgpConditionExternalFlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionExternalFlowLoss = _LgpConditionExternalFlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 2)
)
if mibBuilder.loadTexts:
    lgpConditionExternalFlowLoss.setStatus("current")
_LgpConditionExternalReheatLockout_ObjectIdentity = ObjectIdentity
lgpConditionExternalReheatLockout = _LgpConditionExternalReheatLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 3)
)
if mibBuilder.loadTexts:
    lgpConditionExternalReheatLockout.setStatus("current")
_LgpConditionExternalOverTemp_ObjectIdentity = ObjectIdentity
lgpConditionExternalOverTemp = _LgpConditionExternalOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 4)
)
if mibBuilder.loadTexts:
    lgpConditionExternalOverTemp.setStatus("current")
_LgpConditionExternalCompLockout_ObjectIdentity = ObjectIdentity
lgpConditionExternalCompLockout = _LgpConditionExternalCompLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 5)
)
if mibBuilder.loadTexts:
    lgpConditionExternalCompLockout.setStatus("current")
_LgpConditionExternalHumidifierLockout_ObjectIdentity = ObjectIdentity
lgpConditionExternalHumidifierLockout = _LgpConditionExternalHumidifierLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 6)
)
if mibBuilder.loadTexts:
    lgpConditionExternalHumidifierLockout.setStatus("current")
_LgpConditionComponentShutdownGroup_ObjectIdentity = ObjectIdentity
lgpConditionComponentShutdownGroup = _LgpConditionComponentShutdownGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 237)
)
if mibBuilder.loadTexts:
    lgpConditionComponentShutdownGroup.setStatus("current")
_LgpConditionComponentShutdownPartial_ObjectIdentity = ObjectIdentity
lgpConditionComponentShutdownPartial = _LgpConditionComponentShutdownPartial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 237, 1)
)
if mibBuilder.loadTexts:
    lgpConditionComponentShutdownPartial.setStatus("current")
_LgpConditionComponentShutdownHighPower_ObjectIdentity = ObjectIdentity
lgpConditionComponentShutdownHighPower = _LgpConditionComponentShutdownHighPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 237, 2)
)
if mibBuilder.loadTexts:
    lgpConditionComponentShutdownHighPower.setStatus("current")
_LgpConditionCondenserProblemGroup_ObjectIdentity = ObjectIdentity
lgpConditionCondenserProblemGroup = _LgpConditionCondenserProblemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 238)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserProblemGroup.setStatus("current")
_LgpConditionCondenser1Problem_ObjectIdentity = ObjectIdentity
lgpConditionCondenser1Problem = _LgpConditionCondenser1Problem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 238, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCondenser1Problem.setStatus("current")
_LgpConditionHumidityOutOfPropBand_ObjectIdentity = ObjectIdentity
lgpConditionHumidityOutOfPropBand = _LgpConditionHumidityOutOfPropBand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 239)
)
if mibBuilder.loadTexts:
    lgpConditionHumidityOutOfPropBand.setStatus("current")
_LgpConditionEnvRemoteSensorGroup_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensorGroup = _LgpConditionEnvRemoteSensorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensorGroup.setStatus("current")
_LgpConditionEnvRemoteSensor1Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor1Issue = _LgpConditionEnvRemoteSensor1Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 1)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor1Issue.setStatus("current")
_LgpConditionEnvRemoteSensor2Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor2Issue = _LgpConditionEnvRemoteSensor2Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 2)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor2Issue.setStatus("current")
_LgpConditionEnvRemoteSensor3Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor3Issue = _LgpConditionEnvRemoteSensor3Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 3)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor3Issue.setStatus("current")
_LgpConditionEnvRemoteSensor4Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor4Issue = _LgpConditionEnvRemoteSensor4Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 4)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor4Issue.setStatus("current")
_LgpConditionEnvRemoteSensor5Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor5Issue = _LgpConditionEnvRemoteSensor5Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 5)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor5Issue.setStatus("current")
_LgpConditionEnvRemoteSensor6Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor6Issue = _LgpConditionEnvRemoteSensor6Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 6)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor6Issue.setStatus("current")
_LgpConditionEnvRemoteSensor7Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor7Issue = _LgpConditionEnvRemoteSensor7Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 7)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor7Issue.setStatus("current")
_LgpConditionEnvRemoteSensor8Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor8Issue = _LgpConditionEnvRemoteSensor8Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 8)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor8Issue.setStatus("current")
_LgpConditionEnvRemoteSensor9Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor9Issue = _LgpConditionEnvRemoteSensor9Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 9)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor9Issue.setStatus("current")
_LgpConditionEnvRemoteSensor10Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor10Issue = _LgpConditionEnvRemoteSensor10Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 10)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor10Issue.setStatus("current")
_LgpConditionNeutralSnubberBoardCommFailure_ObjectIdentity = ObjectIdentity
lgpConditionNeutralSnubberBoardCommFailure = _LgpConditionNeutralSnubberBoardCommFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 241)
)
if mibBuilder.loadTexts:
    lgpConditionNeutralSnubberBoardCommFailure.setStatus("current")
_LgpConditionRedundantChargerFailure_ObjectIdentity = ObjectIdentity
lgpConditionRedundantChargerFailure = _LgpConditionRedundantChargerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 242)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantChargerFailure.setStatus("current")
_LgpConditionBoardInputContactorPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionBoardInputContactorPowerFailure = _LgpConditionBoardInputContactorPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 243)
)
if mibBuilder.loadTexts:
    lgpConditionBoardInputContactorPowerFailure.setStatus("current")
_LgpConditionBoard1InputContactorPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionBoard1InputContactorPowerFailure = _LgpConditionBoard1InputContactorPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 243, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBoard1InputContactorPowerFailure.setStatus("current")
_LgpConditionBoard2InputContactorPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionBoard2InputContactorPowerFailure = _LgpConditionBoard2InputContactorPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 243, 2)
)
if mibBuilder.loadTexts:
    lgpConditionBoard2InputContactorPowerFailure.setStatus("current")
_LgpConditionTooManySensors_ObjectIdentity = ObjectIdentity
lgpConditionTooManySensors = _LgpConditionTooManySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5423)
)
if mibBuilder.loadTexts:
    lgpConditionTooManySensors.setStatus("current")
_LgpConditionDoorSwitchOpen_ObjectIdentity = ObjectIdentity
lgpConditionDoorSwitchOpen = _LgpConditionDoorSwitchOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5471)
)
if mibBuilder.loadTexts:
    lgpConditionDoorSwitchOpen.setStatus("current")
_LgpConditionContactClosureOpen_ObjectIdentity = ObjectIdentity
lgpConditionContactClosureOpen = _LgpConditionContactClosureOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5479)
)
if mibBuilder.loadTexts:
    lgpConditionContactClosureOpen.setStatus("current")
_LgpConditionContactClosureClosed_ObjectIdentity = ObjectIdentity
lgpConditionContactClosureClosed = _LgpConditionContactClosureClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5480)
)
if mibBuilder.loadTexts:
    lgpConditionContactClosureClosed.setStatus("current")
_LgpConditionSensorsNotDisplayed_ObjectIdentity = ObjectIdentity
lgpConditionSensorsNotDisplayed = _LgpConditionSensorsNotDisplayed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 6119)
)
if mibBuilder.loadTexts:
    lgpConditionSensorsNotDisplayed.setStatus("current")
_LgpConditionsPresent_Type = Gauge32
_LgpConditionsPresent_Object = MibScalar
lgpConditionsPresent = _LgpConditionsPresent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 2),
    _LgpConditionsPresent_Type()
)
lgpConditionsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionsPresent.setStatus("current")
_LgpConditionsTable_Object = MibTable
lgpConditionsTable = _LgpConditionsTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3)
)
if mibBuilder.loadTexts:
    lgpConditionsTable.setStatus("current")
_LgpConditionEntry_Object = MibTableRow
lgpConditionEntry = _LgpConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1)
)
lgpConditionEntry.setIndexNames(
    (0, "LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"),
)
if mibBuilder.loadTexts:
    lgpConditionEntry.setStatus("current")
_LgpConditionId_Type = Unsigned32
_LgpConditionId_Object = MibTableColumn
lgpConditionId = _LgpConditionId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 1),
    _LgpConditionId_Type()
)
lgpConditionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionId.setStatus("current")
_LgpConditionDescr_Type = ObjectIdentifier
_LgpConditionDescr_Object = MibTableColumn
lgpConditionDescr = _LgpConditionDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 2),
    _LgpConditionDescr_Type()
)
lgpConditionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionDescr.setStatus("current")
_LgpConditionTime_Type = TimeTicks
_LgpConditionTime_Object = MibTableColumn
lgpConditionTime = _LgpConditionTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 3),
    _LgpConditionTime_Type()
)
lgpConditionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionTime.setStatus("current")
_LgpConditionTableRef_Type = ObjectIdentifier
_LgpConditionTableRef_Object = MibTableColumn
lgpConditionTableRef = _LgpConditionTableRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 5),
    _LgpConditionTableRef_Type()
)
lgpConditionTableRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionTableRef.setStatus("current")
_LgpConditionTableRowRef_Type = ObjectIdentifier
_LgpConditionTableRowRef_Object = MibTableColumn
lgpConditionTableRowRef = _LgpConditionTableRowRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 6),
    _LgpConditionTableRowRef_Type()
)
lgpConditionTableRowRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionTableRowRef.setStatus("current")


class _LgpConditionType_Type(Integer32):
    """Custom type lgpConditionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 6),
          ("fault", 8),
          ("message", 2),
          ("not-specified", 0),
          ("warning", 4))
    )


_LgpConditionType_Type.__name__ = "Integer32"
_LgpConditionType_Object = MibTableColumn
lgpConditionType = _LgpConditionType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 10),
    _LgpConditionType_Type()
)
lgpConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionType.setStatus("current")


class _LgpConditionCurrentState_Type(Integer32):
    """Custom type lgpConditionCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LgpConditionCurrentState_Type.__name__ = "Integer32"
_LgpConditionCurrentState_Object = MibTableColumn
lgpConditionCurrentState = _LgpConditionCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 12),
    _LgpConditionCurrentState_Type()
)
lgpConditionCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionCurrentState.setStatus("current")


class _LgpConditionSeverity_Type(Integer32):
    """Custom type lgpConditionSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("critical", 9),
          ("major", 6),
          ("minor", 3),
          ("not-applicable", 0))
    )


_LgpConditionSeverity_Type.__name__ = "Integer32"
_LgpConditionSeverity_Object = MibTableColumn
lgpConditionSeverity = _LgpConditionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 14),
    _LgpConditionSeverity_Type()
)
lgpConditionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionSeverity.setStatus("current")


class _LgpConditionAcknowledged_Type(Integer32):
    """Custom type lgpConditionAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 2),
          ("notAcknowledged", 1))
    )


_LgpConditionAcknowledged_Type.__name__ = "Integer32"
_LgpConditionAcknowledged_Object = MibTableColumn
lgpConditionAcknowledged = _LgpConditionAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 18),
    _LgpConditionAcknowledged_Type()
)
lgpConditionAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionAcknowledged.setStatus("current")


class _LgpConditionAckReq_Type(Integer32):
    """Custom type lgpConditionAckReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRequired", 2),
          ("required", 1))
    )


_LgpConditionAckReq_Type.__name__ = "Integer32"
_LgpConditionAckReq_Object = MibTableColumn
lgpConditionAckReq = _LgpConditionAckReq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 19),
    _LgpConditionAckReq_Type()
)
lgpConditionAckReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionAckReq.setStatus("current")
_LgpConditionControl_ObjectIdentity = ObjectIdentity
lgpConditionControl = _LgpConditionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4)
)


class _LgpConditionControlEventReset_Type(Integer32):
    """Custom type lgpConditionControlEventReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetAll", 2))
    )


_LgpConditionControlEventReset_Type.__name__ = "Integer32"
_LgpConditionControlEventReset_Object = MibScalar
lgpConditionControlEventReset = _LgpConditionControlEventReset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 1),
    _LgpConditionControlEventReset_Type()
)
lgpConditionControlEventReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlEventReset.setStatus("current")


class _LgpConditionControlEventAck_Type(Integer32):
    """Custom type lgpConditionControlEventAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ackAll", 2),
          ("noAction", 1))
    )


_LgpConditionControlEventAck_Type.__name__ = "Integer32"
_LgpConditionControlEventAck_Object = MibScalar
lgpConditionControlEventAck = _LgpConditionControlEventAck_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 2),
    _LgpConditionControlEventAck_Type()
)
lgpConditionControlEventAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlEventAck.setStatus("current")
_LgpConditionControlTable_Object = MibTable
lgpConditionControlTable = _LgpConditionControlTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20)
)
if mibBuilder.loadTexts:
    lgpConditionControlTable.setStatus("current")
_LgpConditionControlEntry_Object = MibTableRow
lgpConditionControlEntry = _LgpConditionControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1)
)
lgpConditionControlEntry.setIndexNames(
    (0, "LIEBERT-GP-CONDITIONS-MIB", "lgpConditionControlIndex"),
)
if mibBuilder.loadTexts:
    lgpConditionControlEntry.setStatus("current")
_LgpConditionControlIndex_Type = Unsigned32
_LgpConditionControlIndex_Object = MibTableColumn
lgpConditionControlIndex = _LgpConditionControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 1),
    _LgpConditionControlIndex_Type()
)
lgpConditionControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpConditionControlIndex.setStatus("current")
_LgpConditionControlDescr_Type = ObjectIdentifier
_LgpConditionControlDescr_Object = MibTableColumn
lgpConditionControlDescr = _LgpConditionControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 2),
    _LgpConditionControlDescr_Type()
)
lgpConditionControlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionControlDescr.setStatus("current")


class _LgpConditionControlEnableStatus_Type(Integer32):
    """Custom type lgpConditionControlEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-specified", 0))
    )


_LgpConditionControlEnableStatus_Type.__name__ = "Integer32"
_LgpConditionControlEnableStatus_Object = MibTableColumn
lgpConditionControlEnableStatus = _LgpConditionControlEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 3),
    _LgpConditionControlEnableStatus_Type()
)
lgpConditionControlEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlEnableStatus.setStatus("current")


class _LgpConditionControlType_Type(Integer32):
    """Custom type lgpConditionControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 6),
          ("fault", 8),
          ("message", 2),
          ("not-specified", 0),
          ("warning", 4))
    )


_LgpConditionControlType_Type.__name__ = "Integer32"
_LgpConditionControlType_Object = MibTableColumn
lgpConditionControlType = _LgpConditionControlType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 4),
    _LgpConditionControlType_Type()
)
lgpConditionControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlType.setStatus("current")


class _LgpConditionControlEnableCapability_Type(Integer32):
    """Custom type lgpConditionControlEnableCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("readonly", 1),
          ("readwrite", 2))
    )


_LgpConditionControlEnableCapability_Type.__name__ = "Integer32"
_LgpConditionControlEnableCapability_Object = MibTableColumn
lgpConditionControlEnableCapability = _LgpConditionControlEnableCapability_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 5),
    _LgpConditionControlEnableCapability_Type()
)
lgpConditionControlEnableCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionControlEnableCapability.setStatus("current")


class _LgpConditionDescription_Type(DisplayString):
    """Custom type lgpConditionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpConditionDescription_Type.__name__ = "DisplayString"
_LgpConditionDescription_Object = MibScalar
lgpConditionDescription = _LgpConditionDescription_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 5),
    _LgpConditionDescription_Type()
)
lgpConditionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionDescription.setStatus("current")


class _LgpNetworkName_Type(DisplayString):
    """Custom type lgpNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_LgpNetworkName_Type.__name__ = "DisplayString"
_LgpNetworkName_Object = MibScalar
lgpNetworkName = _LgpNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 6),
    _LgpNetworkName_Type()
)
lgpNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpNetworkName.setStatus("current")
_LgpFlexConditions_ObjectIdentity = ObjectIdentity
lgpFlexConditions = _LgpFlexConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-CONDITIONS-MIB",
    **{"liebertGlobalProductsConditionsModule": liebertGlobalProductsConditionsModule,
       "lgpConditionsWellKnown": lgpConditionsWellKnown,
       "lgpConditionHighTemperature": lgpConditionHighTemperature,
       "lgpConditionLowTemperature": lgpConditionLowTemperature,
       "lgpConditionHighHumidity": lgpConditionHighHumidity,
       "lgpConditionLowHumidity": lgpConditionLowHumidity,
       "lgpConditionLossOfAirflow": lgpConditionLossOfAirflow,
       "lgpConditionLossOfAirflow1": lgpConditionLossOfAirflow1,
       "lgpConditionLossOfAirflow2": lgpConditionLossOfAirflow2,
       "lgpConditionLossOfAirflowBlower1": lgpConditionLossOfAirflowBlower1,
       "lgpConditionLossOfAirflowAllBlowers": lgpConditionLossOfAirflowAllBlowers,
       "lgpConditionChangeFilter": lgpConditionChangeFilter,
       "lgpConditionCompressorHighHeadPressure": lgpConditionCompressorHighHeadPressure,
       "lgpConditionCompressor1HighHeadPressure": lgpConditionCompressor1HighHeadPressure,
       "lgpConditionCompressor1AHighHeadPressure": lgpConditionCompressor1AHighHeadPressure,
       "lgpConditionCompressor1BHighHeadPressure": lgpConditionCompressor1BHighHeadPressure,
       "lgpConditionCompressor2HighHeadPressure": lgpConditionCompressor2HighHeadPressure,
       "lgpConditionCompressor2AHighHeadPressure": lgpConditionCompressor2AHighHeadPressure,
       "lgpConditionCompressor2BHighHeadPressure": lgpConditionCompressor2BHighHeadPressure,
       "lgpConditionCompressor3HighHeadPressure": lgpConditionCompressor3HighHeadPressure,
       "lgpConditionCompressor4HighHeadPressure": lgpConditionCompressor4HighHeadPressure,
       "lgpConditionCompressorOverload": lgpConditionCompressorOverload,
       "lgpConditionCompressor1Overload": lgpConditionCompressor1Overload,
       "lgpConditionCompressor2Overload": lgpConditionCompressor2Overload,
       "lgpConditionCompressorShortCycle": lgpConditionCompressorShortCycle,
       "lgpConditionCompressor1ShortCycle": lgpConditionCompressor1ShortCycle,
       "lgpConditionCompressor1AShortCycle": lgpConditionCompressor1AShortCycle,
       "lgpConditionCompressor1BShortCycle": lgpConditionCompressor1BShortCycle,
       "lgpConditionCompressor2ShortCycle": lgpConditionCompressor2ShortCycle,
       "lgpConditionCompressor2AShortCycle": lgpConditionCompressor2AShortCycle,
       "lgpConditionCompressor2BShortCycle": lgpConditionCompressor2BShortCycle,
       "lgpConditionCompressorLowSuctionPressure": lgpConditionCompressorLowSuctionPressure,
       "lgpConditionCompressor1LowSuctionPressure": lgpConditionCompressor1LowSuctionPressure,
       "lgpConditionCompressor2LowSuctionPressure": lgpConditionCompressor2LowSuctionPressure,
       "lgpConditionMainFanOverLoad": lgpConditionMainFanOverLoad,
       "lgpConditionManualOverride": lgpConditionManualOverride,
       "lgpConditionStandbyGlycoolPumpOn": lgpConditionStandbyGlycoolPumpOn,
       "lgpConditionWaterUnderFloor": lgpConditionWaterUnderFloor,
       "lgpConditionHumidifierProblem": lgpConditionHumidifierProblem,
       "lgpConditionLowWaterInHumidifier": lgpConditionLowWaterInHumidifier,
       "lgpConditionSmokeDetected": lgpConditionSmokeDetected,
       "lgpConditionLowWaterFlow": lgpConditionLowWaterFlow,
       "lgpConditionLostPower": lgpConditionLostPower,
       "lgpGeneralFault": lgpGeneralFault,
       "lgpConditionLocalAlarm": lgpConditionLocalAlarm,
       "lgpConditionLocalAlarm1": lgpConditionLocalAlarm1,
       "lgpConditionLocalAlarm2": lgpConditionLocalAlarm2,
       "lgpConditionLocalAlarm3": lgpConditionLocalAlarm3,
       "lgpConditionLocalAlarm4": lgpConditionLocalAlarm4,
       "lgpConditionLocalAlarm5": lgpConditionLocalAlarm5,
       "lgpConditionLocalAlarm6": lgpConditionLocalAlarm6,
       "lgpConditionLocalAlarm7": lgpConditionLocalAlarm7,
       "lgpConditionLocalAlarm8": lgpConditionLocalAlarm8,
       "lgpConditionStandbyUnitOn": lgpConditionStandbyUnitOn,
       "lgpConditionCompressorLowPressure": lgpConditionCompressorLowPressure,
       "lgpConditionCompressor1LowPressure": lgpConditionCompressor1LowPressure,
       "lgpConditionTandemCompressorCircuit1LowPressure": lgpConditionTandemCompressorCircuit1LowPressure,
       "lgpConditionCompressor2LowPressure": lgpConditionCompressor2LowPressure,
       "lgpConditionTandemCompressorCircuit2LowPressure": lgpConditionTandemCompressorCircuit2LowPressure,
       "lgpConditionCompressor3LowPressure": lgpConditionCompressor3LowPressure,
       "lgpConditionCompressor4LowPressure": lgpConditionCompressor4LowPressure,
       "lgpConditionHighWaterInPan": lgpConditionHighWaterInPan,
       "lgpConditionFaultySensor": lgpConditionFaultySensor,
       "lgpConditionServiceCooling": lgpConditionServiceCooling,
       "lgpConditionServiceHumidifier": lgpConditionServiceHumidifier,
       "lgpConditionSystemControlBatteryLow": lgpConditionSystemControlBatteryLow,
       "lgpConditionGroundSystemFault": lgpConditionGroundSystemFault,
       "lgpConditionGroundFailure": lgpConditionGroundFailure,
       "lgpConditionSecurityBreach": lgpConditionSecurityBreach,
       "lgpConditionEmergencyShutdown": lgpConditionEmergencyShutdown,
       "lgpConditionOnBypass": lgpConditionOnBypass,
       "lgpConditionLoadOnBypass": lgpConditionLoadOnBypass,
       "lgpConditionLoadOnMaintenceBypass": lgpConditionLoadOnMaintenceBypass,
       "lgpConditionParallelSysLoadOnBypass": lgpConditionParallelSysLoadOnBypass,
       "lgpConditionLoadOnBypassByImpact": lgpConditionLoadOnBypassByImpact,
       "lgpConditionLoadTransferedToBypass": lgpConditionLoadTransferedToBypass,
       "lgpConditionEmergencyTransferToBypass": lgpConditionEmergencyTransferToBypass,
       "lgpConditionOutputToLoadVoltTHD": lgpConditionOutputToLoadVoltTHD,
       "lgpConditionLogicFailure": lgpConditionLogicFailure,
       "lgpConditionPowerSupplyFault": lgpConditionPowerSupplyFault,
       "lgpConditionPowerSupply1Fault": lgpConditionPowerSupply1Fault,
       "lgpConditionPowerSupply2Fault": lgpConditionPowerSupply2Fault,
       "lgpConditionPowerSupplyFailure": lgpConditionPowerSupplyFailure,
       "lgpConditionPowerSupply1Failure": lgpConditionPowerSupply1Failure,
       "lgpConditionPowerSupply2Failure": lgpConditionPowerSupply2Failure,
       "lgpConditionSource1PowerSupplyInputFailure": lgpConditionSource1PowerSupplyInputFailure,
       "lgpConditionSource2PowerSupplyInputFailure": lgpConditionSource2PowerSupplyInputFailure,
       "lgpConditionPowerSupplyLogicFailure": lgpConditionPowerSupplyLogicFailure,
       "lgpConditionCompressorPowerSupplyFailure": lgpConditionCompressorPowerSupplyFailure,
       "lgpConditionOverVoltage": lgpConditionOverVoltage,
       "lgpConditionSource1OverVoltage": lgpConditionSource1OverVoltage,
       "lgpConditionSource2OverVoltage": lgpConditionSource2OverVoltage,
       "lgpConditionOutputToLoadOverVoltage": lgpConditionOutputToLoadOverVoltage,
       "lgpConditionInputOverVoltage": lgpConditionInputOverVoltage,
       "lgpConditionBypassOverVoltage": lgpConditionBypassOverVoltage,
       "lgpConditionBypassOverVoltageFailure": lgpConditionBypassOverVoltageFailure,
       "lgpConditionBatteryOverVoltage": lgpConditionBatteryOverVoltage,
       "lgpConditionDcBusOverVoltage": lgpConditionDcBusOverVoltage,
       "lgpConditionDcBus1OverVoltage": lgpConditionDcBus1OverVoltage,
       "lgpConditionDcBus2OverVoltage": lgpConditionDcBus2OverVoltage,
       "lgpConditionDcBus1OverVoltageFailure": lgpConditionDcBus1OverVoltageFailure,
       "lgpConditionDcBus2OverVoltageFailure": lgpConditionDcBus2OverVoltageFailure,
       "lgpConditionUnderVoltage": lgpConditionUnderVoltage,
       "lgpConditionSource1UnderVoltage": lgpConditionSource1UnderVoltage,
       "lgpConditionSource2UnderVoltage": lgpConditionSource2UnderVoltage,
       "lgpConditionOutputToLoadUnderVoltage": lgpConditionOutputToLoadUnderVoltage,
       "lgpConditionSource1UnderVoltageRMS": lgpConditionSource1UnderVoltageRMS,
       "lgpConditionSource2UnderVoltageRMS": lgpConditionSource2UnderVoltageRMS,
       "lgpConditionInputUnderVoltage": lgpConditionInputUnderVoltage,
       "lgpConditionBypassUnderVoltage": lgpConditionBypassUnderVoltage,
       "lgpConditionBypassUnderVoltageFailure": lgpConditionBypassUnderVoltageFailure,
       "lgpConditionBatteryUnderVoltage": lgpConditionBatteryUnderVoltage,
       "lgpConditionDcBusUnderVoltage": lgpConditionDcBusUnderVoltage,
       "lgpConditionDcBus1UnderVoltage": lgpConditionDcBus1UnderVoltage,
       "lgpConditionDcBus2UnderVoltage": lgpConditionDcBus2UnderVoltage,
       "lgpConditionDcBus1UnderVoltageFailure": lgpConditionDcBus1UnderVoltageFailure,
       "lgpConditionDcBus2UnderVoltageFailure": lgpConditionDcBus2UnderVoltageFailure,
       "lgpConditionOverload": lgpConditionOverload,
       "lgpConditionSource1Overload": lgpConditionSource1Overload,
       "lgpConditionSystemOverload": lgpConditionSystemOverload,
       "lgpConditionSource1PeakCurrentOverLoad": lgpConditionSource1PeakCurrentOverLoad,
       "lgpConditionSource2PeakCurrentOverLoad": lgpConditionSource2PeakCurrentOverLoad,
       "lgpConditionOutputToLoadOverLimit": lgpConditionOutputToLoadOverLimit,
       "lgpConditionOutputToLoadOverload": lgpConditionOutputToLoadOverload,
       "lgpConditionParallelSysOverload": lgpConditionParallelSysOverload,
       "lgpConditionBypassCurrentOverload": lgpConditionBypassCurrentOverload,
       "lgpConditionBypassCurrentOverloadPhsA": lgpConditionBypassCurrentOverloadPhsA,
       "lgpConditionBypassCurrentOverloadPhsB": lgpConditionBypassCurrentOverloadPhsB,
       "lgpConditionBypassCurrentOverloadPhsC": lgpConditionBypassCurrentOverloadPhsC,
       "lgpConditionScrShort": lgpConditionScrShort,
       "lgpConditionSource1ScrShort": lgpConditionSource1ScrShort,
       "lgpConditionSource2ScrShort": lgpConditionSource2ScrShort,
       "lgpConditionBypassScrShort": lgpConditionBypassScrShort,
       "lgpConditionInvStaticSwScrShort": lgpConditionInvStaticSwScrShort,
       "lgpConditionSource1NeutralScrShort": lgpConditionSource1NeutralScrShort,
       "lgpConditionSource2NeutralScrShort": lgpConditionSource2NeutralScrShort,
       "lgpConditionScrOpen": lgpConditionScrOpen,
       "lgpConditionSource1ScrOpen": lgpConditionSource1ScrOpen,
       "lgpConditionSource2ScrOpen": lgpConditionSource2ScrOpen,
       "lgpConditionBypassScrOpen": lgpConditionBypassScrOpen,
       "lgpConditionSource1NeutralScrOpen": lgpConditionSource1NeutralScrOpen,
       "lgpConditionSource2NeutralScrOpen": lgpConditionSource2NeutralScrOpen,
       "lgpConditionFanFailure": lgpConditionFanFailure,
       "lgpConditionFan1Failure": lgpConditionFan1Failure,
       "lgpConditionRedundantFanFailure": lgpConditionRedundantFanFailure,
       "lgpConditionMultipleFanFailure": lgpConditionMultipleFanFailure,
       "lgpConditionBlowerFanFailure": lgpConditionBlowerFanFailure,
       "lgpConditionBottomBlowerFanFailure": lgpConditionBottomBlowerFanFailure,
       "lgpConditionTopBlowerFanFailure": lgpConditionTopBlowerFanFailure,
       "lgpConditionCondenserFanVFDFailure": lgpConditionCondenserFanVFDFailure,
       "lgpConditionFanPowerFailure": lgpConditionFanPowerFailure,
       "lgpConditionTransferInhibited": lgpConditionTransferInhibited,
       "lgpConditionAutoReTransferPrimed": lgpConditionAutoReTransferPrimed,
       "lgpConditionSourcesOutOfSync": lgpConditionSourcesOutOfSync,
       "lgpConditionSourceFailure": lgpConditionSourceFailure,
       "lgpConditionSource1Failure": lgpConditionSource1Failure,
       "lgpConditionSource2Failure": lgpConditionSource2Failure,
       "lgpConditionAutoReTransferInhibited": lgpConditionAutoReTransferInhibited,
       "lgpConditionAutoReTransferFailed": lgpConditionAutoReTransferFailed,
       "lgpConditionFuseOpen": lgpConditionFuseOpen,
       "lgpConditionControlFuse1Open": lgpConditionControlFuse1Open,
       "lgpConditionControlFuse2Open": lgpConditionControlFuse2Open,
       "lgpConditionRectifierFuseOpen": lgpConditionRectifierFuseOpen,
       "lgpConditionInverterFuseOpen": lgpConditionInverterFuseOpen,
       "lgpConditionOutputToLoadFuseOpen": lgpConditionOutputToLoadFuseOpen,
       "lgpConditionDcCapacitorFuseOpen": lgpConditionDcCapacitorFuseOpen,
       "lgpConditionDisconnect": lgpConditionDisconnect,
       "lgpConditionSource1DisconnectOpen": lgpConditionSource1DisconnectOpen,
       "lgpConditionSource2DisconnectOpen": lgpConditionSource2DisconnectOpen,
       "lgpConditionSource1PduDisconnectOpen": lgpConditionSource1PduDisconnectOpen,
       "lgpConditionSource2PduDisconnectOpen": lgpConditionSource2PduDisconnectOpen,
       "lgpConditionOutputToLoadDisconnect1Open": lgpConditionOutputToLoadDisconnect1Open,
       "lgpConditionOutputToLoadDisconnect2Open": lgpConditionOutputToLoadDisconnect2Open,
       "lgpConditionSource1BypassDisconnectClosed": lgpConditionSource1BypassDisconnectClosed,
       "lgpConditionSource2BypassDisconnectClosed": lgpConditionSource2BypassDisconnectClosed,
       "lgpConditionOutputToLoadNeutralDisconnectOpen": lgpConditionOutputToLoadNeutralDisconnectOpen,
       "lgpConditionBatteryDisconnectOpen": lgpConditionBatteryDisconnectOpen,
       "lgpConditionBatteryDiscOpenCab01": lgpConditionBatteryDiscOpenCab01,
       "lgpConditionBatteryDiscOpenCab02": lgpConditionBatteryDiscOpenCab02,
       "lgpConditionBatteryDiscOpenCab03": lgpConditionBatteryDiscOpenCab03,
       "lgpConditionBatteryDiscOpenCab04": lgpConditionBatteryDiscOpenCab04,
       "lgpConditionBatteryDiscOpenCab05": lgpConditionBatteryDiscOpenCab05,
       "lgpConditionBatteryDiscOpenCab06": lgpConditionBatteryDiscOpenCab06,
       "lgpConditionBatteryDiscOpenCab07": lgpConditionBatteryDiscOpenCab07,
       "lgpConditionBatteryDiscOpenCab08": lgpConditionBatteryDiscOpenCab08,
       "lgpConditionInputDisconnectOpen": lgpConditionInputDisconnectOpen,
       "lgpConditionOutputToLoadDisconnectOpen": lgpConditionOutputToLoadDisconnectOpen,
       "lgpConditionBypassDisconnectOpen": lgpConditionBypassDisconnectOpen,
       "lgpConditionStaticSwitchDisconnectOpen": lgpConditionStaticSwitchDisconnectOpen,
       "lgpConditionBreakerOpenFailure": lgpConditionBreakerOpenFailure,
       "lgpConditionBreakerCloseFailure": lgpConditionBreakerCloseFailure,
       "lgpConditionFrequencyDeviation": lgpConditionFrequencyDeviation,
       "lgpConditionSource1FrequencyDeviation": lgpConditionSource1FrequencyDeviation,
       "lgpConditionSource2FrequencyDeviation": lgpConditionSource2FrequencyDeviation,
       "lgpConditionInputFrequencyDeviation": lgpConditionInputFrequencyDeviation,
       "lgpConditionOutputToLoadFrequencyDeviation": lgpConditionOutputToLoadFrequencyDeviation,
       "lgpConditionBypassFrequencyDeviation": lgpConditionBypassFrequencyDeviation,
       "lgpConditionOverCurrent": lgpConditionOverCurrent,
       "lgpConditionSource1OverCurrent": lgpConditionSource1OverCurrent,
       "lgpConditionSource2OverCurrent": lgpConditionSource2OverCurrent,
       "lgpConditionOutputToLoadOverCurrent": lgpConditionOutputToLoadOverCurrent,
       "lgpConditionOutputToLoadOverCurrentPhsA": lgpConditionOutputToLoadOverCurrentPhsA,
       "lgpConditionOutputToLoadOverCurrentPhsB": lgpConditionOutputToLoadOverCurrentPhsB,
       "lgpConditionOutputToLoadOverCurrentPhsC": lgpConditionOutputToLoadOverCurrentPhsC,
       "lgpConditionGroundOverCurrent": lgpConditionGroundOverCurrent,
       "lgpConditionRectifierOverCurrent": lgpConditionRectifierOverCurrent,
       "lgpConditionInverterOverCurrent": lgpConditionInverterOverCurrent,
       "lgpConditionInverterOverCurrentPhsA": lgpConditionInverterOverCurrentPhsA,
       "lgpConditionInverterOverCurrentPhsB": lgpConditionInverterOverCurrentPhsB,
       "lgpConditionInverterOverCurrentPhsC": lgpConditionInverterOverCurrentPhsC,
       "lgpConditionBatteryConverterOverCurrent": lgpConditionBatteryConverterOverCurrent,
       "lgpConditionBatteryBalancerOverCurrent": lgpConditionBatteryBalancerOverCurrent,
       "lgpConditionHumidifierOverCurrent": lgpConditionHumidifierOverCurrent,
       "lgpConditionInputOverCurrent": lgpConditionInputOverCurrent,
       "lgpConditionSource1NeutralOverCurrent": lgpConditionSource1NeutralOverCurrent,
       "lgpConditionSource2NeutralOverCurrent": lgpConditionSource2NeutralOverCurrent,
       "lgpConditionSensorFailure": lgpConditionSensorFailure,
       "lgpConditionOutputToLoadVoltageSensorFailure": lgpConditionOutputToLoadVoltageSensorFailure,
       "lgpConditionSource1VoltageSensorFailure": lgpConditionSource1VoltageSensorFailure,
       "lgpConditionSource2VoltageSensorFailure": lgpConditionSource2VoltageSensorFailure,
       "lgpConditionSource1ScrSensorFailure": lgpConditionSource1ScrSensorFailure,
       "lgpConditionSource2ScrSensorFailure": lgpConditionSource2ScrSensorFailure,
       "lgpConditionSource1CurrentSensorFailure": lgpConditionSource1CurrentSensorFailure,
       "lgpConditionSource2CurrentSensorFailure": lgpConditionSource2CurrentSensorFailure,
       "lgpConditionRoomTempHumiditySensorFailure": lgpConditionRoomTempHumiditySensorFailure,
       "lgpConditionGlycolTempSensorFailure": lgpConditionGlycolTempSensorFailure,
       "lgpConditionLocal1SensorFailure": lgpConditionLocal1SensorFailure,
       "lgpConditionCompressor1SensorFailure": lgpConditionCompressor1SensorFailure,
       "lgpConditionCompressor2SensorFailure": lgpConditionCompressor2SensorFailure,
       "lgpConditionSupplySensorFailure": lgpConditionSupplySensorFailure,
       "lgpConditionCabinetTemperatureSensorFailure": lgpConditionCabinetTemperatureSensorFailure,
       "lgpConditionCabinetHumiditySensorFailure": lgpConditionCabinetHumiditySensorFailure,
       "lgpConditionRoomTempSensorFailure": lgpConditionRoomTempSensorFailure,
       "lgpConditionBatteryTempSensorFailure": lgpConditionBatteryTempSensorFailure,
       "lgpConditionAirSensorAFailure": lgpConditionAirSensorAFailure,
       "lgpConditionAirSensorBFailure": lgpConditionAirSensorBFailure,
       "lgpConditionChilledWaterSupplySensorFailure": lgpConditionChilledWaterSupplySensorFailure,
       "lgpConditionRefrigerantSupplySensorFailure": lgpConditionRefrigerantSupplySensorFailure,
       "lgpConditionFluidSupplySensorFailure": lgpConditionFluidSupplySensorFailure,
       "lgpConditionCompressorLowPressureSensorFailure": lgpConditionCompressorLowPressureSensorFailure,
       "lgpConditionCompressor1LowPressureSensorFailure": lgpConditionCompressor1LowPressureSensorFailure,
       "lgpConditionRemoteSensorFailure": lgpConditionRemoteSensorFailure,
       "lgpConditionAirSupplyTempSensorFailure": lgpConditionAirSupplyTempSensorFailure,
       "lgpConditionAirReturnTempSensorFailure": lgpConditionAirReturnTempSensorFailure,
       "lgpConditionCompressorHighPressureSensorFailure": lgpConditionCompressorHighPressureSensorFailure,
       "lgpConditionInternalCommunicationFailure": lgpConditionInternalCommunicationFailure,
       "lgpConditionExternalCommunicationFailure": lgpConditionExternalCommunicationFailure,
       "lgpConditionSourceGateDriveFailure": lgpConditionSourceGateDriveFailure,
       "lgpConditionSource1GateDriveFailure": lgpConditionSource1GateDriveFailure,
       "lgpConditionSource2GateDriveFailure": lgpConditionSource2GateDriveFailure,
       "lgpConditionDisconnectFailure": lgpConditionDisconnectFailure,
       "lgpConditionOutputToLoadNeutralDisconnectFailure": lgpConditionOutputToLoadNeutralDisconnectFailure,
       "lgpConditionSource1DisconnectShuntTripFailure": lgpConditionSource1DisconnectShuntTripFailure,
       "lgpConditionSource2DisconnectShuntTripFailure": lgpConditionSource2DisconnectShuntTripFailure,
       "lgpConditionInverterDisconnectFailure": lgpConditionInverterDisconnectFailure,
       "lgpConditionBatteryDisconnectFailure": lgpConditionBatteryDisconnectFailure,
       "lgpConditionRectifierDisconnectFailure": lgpConditionRectifierDisconnectFailure,
       "lgpConditionOverTemperature": lgpConditionOverTemperature,
       "lgpConditionHeatSink1OverTemperature": lgpConditionHeatSink1OverTemperature,
       "lgpConditionAmbient1OverTemperature": lgpConditionAmbient1OverTemperature,
       "lgpConditionSystemOverTemperature": lgpConditionSystemOverTemperature,
       "lgpConditionTransformerOverTemperature": lgpConditionTransformerOverTemperature,
       "lgpConditionBatteryOverTemperature": lgpConditionBatteryOverTemperature,
       "lgpConditionRectifierOverTemperature": lgpConditionRectifierOverTemperature,
       "lgpConditionInverterOverTemperature": lgpConditionInverterOverTemperature,
       "lgpConditionRectifierInductorOverTemperature": lgpConditionRectifierInductorOverTemperature,
       "lgpConditionInverterInductorOverTemperature": lgpConditionInverterInductorOverTemperature,
       "lgpConditionBatteryConverterOverTemperature": lgpConditionBatteryConverterOverTemperature,
       "lgpConditionBatteryBalancerInductorOverTemperature": lgpConditionBatteryBalancerInductorOverTemperature,
       "lgpConditionChilledWaterOverTemperature": lgpConditionChilledWaterOverTemperature,
       "lgpConditionElectricHeatersOverTemperature": lgpConditionElectricHeatersOverTemperature,
       "lgpConditionInletAirOverTemperature": lgpConditionInletAirOverTemperature,
       "lgpConditionSystemOverTempWarning": lgpConditionSystemOverTempWarning,
       "lgpConditionHighTemperatureBattString": lgpConditionHighTemperatureBattString,
       "lgpConditionLoadOnAlternateSource": lgpConditionLoadOnAlternateSource,
       "lgpConditionPhaseRotationError": lgpConditionPhaseRotationError,
       "lgpConditionSource1PhaseRotationError": lgpConditionSource1PhaseRotationError,
       "lgpConditionSource2PhaseRotationError": lgpConditionSource2PhaseRotationError,
       "lgpConditionBypassPhaseRotationError": lgpConditionBypassPhaseRotationError,
       "lgpConditionInputPhaseRotationError": lgpConditionInputPhaseRotationError,
       "lgpConditionControlModuleFailure": lgpConditionControlModuleFailure,
       "lgpConditionControlModule1Failure": lgpConditionControlModule1Failure,
       "lgpConditionHistoryLogFull": lgpConditionHistoryLogFull,
       "lgpConditionConfigurationModified": lgpConditionConfigurationModified,
       "lgpConditionPasswordModified": lgpConditionPasswordModified,
       "lgpConditionTimeModified": lgpConditionTimeModified,
       "lgpConditionDateModified": lgpConditionDateModified,
       "lgpConditionEventLogCleared": lgpConditionEventLogCleared,
       "lgpConditionHistoryLogCleared": lgpConditionHistoryLogCleared,
       "lgpConditionUtilityFailure": lgpConditionUtilityFailure,
       "lgpConditionBatteryTestInProgress": lgpConditionBatteryTestInProgress,
       "lgpConditionLoadOnBattery": lgpConditionLoadOnBattery,
       "lgpConditionReplaceBattery": lgpConditionReplaceBattery,
       "lgpConditionUpsShutdownPending": lgpConditionUpsShutdownPending,
       "lgpConditionBatteryChargerFailed": lgpConditionBatteryChargerFailed,
       "lgpConditionBypassVoltageUnqualified": lgpConditionBypassVoltageUnqualified,
       "lgpConditionCheckAirFilter": lgpConditionCheckAirFilter,
       "lgpConditionBrownOut": lgpConditionBrownOut,
       "lgpConditionMultipleTransferLockout": lgpConditionMultipleTransferLockout,
       "lgpConditionBypassPhaseLost": lgpConditionBypassPhaseLost,
       "lgpConditionMaintenceBypassInhibited": lgpConditionMaintenceBypassInhibited,
       "lgpConditionLoadLockedOnBypass": lgpConditionLoadLockedOnBypass,
       "lgpConditionOutputToLoadShort": lgpConditionOutputToLoadShort,
       "lgpConditionEmergencyTransferToInverter": lgpConditionEmergencyTransferToInverter,
       "lgpConditonEmergencyPowerOff": lgpConditonEmergencyPowerOff,
       "lgpConditionInverterBackFeed": lgpConditionInverterBackFeed,
       "lgpConditionDcGroundFault": lgpConditionDcGroundFault,
       "lgpConditionDcGroundFaultPos": lgpConditionDcGroundFaultPos,
       "lgpConditionDcGroundFaultNeg": lgpConditionDcGroundFaultNeg,
       "lgpConditionStaticTransferSwitchInhibited": lgpConditionStaticTransferSwitchInhibited,
       "lgpConditionBatteryLogFullWarning": lgpConditionBatteryLogFullWarning,
       "lgpConditionInputCurrentUnbalanced": lgpConditionInputCurrentUnbalanced,
       "lgpConditionSelfTestFailed": lgpConditionSelfTestFailed,
       "lgpConditionInverterOutOfSynchronization": lgpConditionInverterOutOfSynchronization,
       "lgpConditionModuleAlarm": lgpConditionModuleAlarm,
       "lgpConditioniModuleUnit1Alarm": lgpConditioniModuleUnit1Alarm,
       "lgpConditioniModuleUnit2Alarm": lgpConditioniModuleUnit2Alarm,
       "lgpConditioniModuleUnit3Alarm": lgpConditioniModuleUnit3Alarm,
       "lgpConditioniModuleUnit4Alarm": lgpConditioniModuleUnit4Alarm,
       "lgpConditioniModuleUnit5Alarm": lgpConditioniModuleUnit5Alarm,
       "lgpConditioniModuleUnit6Alarm": lgpConditioniModuleUnit6Alarm,
       "lgpConditioniModuleUnit7Alarm": lgpConditioniModuleUnit7Alarm,
       "lgpConditioniModuleUnit8Alarm": lgpConditioniModuleUnit8Alarm,
       "lgpConditionActiveModuleAlarm": lgpConditionActiveModuleAlarm,
       "lgpConditionControlFailure": lgpConditionControlFailure,
       "lgpConditionMainControlFailure": lgpConditionMainControlFailure,
       "lgpConditionRedundantControlFailure": lgpConditionRedundantControlFailure,
       "lgpConditionParallelSysControlFailure": lgpConditionParallelSysControlFailure,
       "lgpConditionMainControlCommFailure": lgpConditionMainControlCommFailure,
       "lgpConditionControlBoardFailure": lgpConditionControlBoardFailure,
       "lgpConditionHumidifierControlBdFailure": lgpConditionHumidifierControlBdFailure,
       "lgpConditionControlWarning": lgpConditionControlWarning,
       "lgpConditionMainControlWarning": lgpConditionMainControlWarning,
       "lgpConditionRedundantControlWarning": lgpConditionRedundantControlWarning,
       "lgpConditionUserInterfaceFailure": lgpConditionUserInterfaceFailure,
       "lgpConditionLostPowerRedundancy": lgpConditionLostPowerRedundancy,
       "lgpConditionPowerModuleFailure": lgpConditionPowerModuleFailure,
       "lgpConditionBatteryModuleFailure": lgpConditionBatteryModuleFailure,
       "lgpConditionOutputToLoadOff": lgpConditionOutputToLoadOff,
       "lgpConditionSystemOff": lgpConditionSystemOff,
       "lgpConditionRectifierStartupFailure": lgpConditionRectifierStartupFailure,
       "lgpConditionRectifierFault": lgpConditionRectifierFault,
       "lgpConditionInverterShutdownLowDc": lgpConditionInverterShutdownLowDc,
       "lgpConditionInverterFault": lgpConditionInverterFault,
       "lgpConditionInverterDcOffsetOverrun": lgpConditionInverterDcOffsetOverrun,
       "lgpConditionParallelSysLowBatteryWarning": lgpConditionParallelSysLowBatteryWarning,
       "lgpConditionParallelSysLoadShareFault": lgpConditionParallelSysLoadShareFault,
       "lgpConditionBatteryFault": lgpConditionBatteryFault,
       "lgpConditionBatteryConverterFailure": lgpConditionBatteryConverterFailure,
       "lgpConditionBatteryBalancerFault": lgpConditionBatteryBalancerFault,
       "lgpConditionpsUpsOperationFault": lgpConditionpsUpsOperationFault,
       "lgpConditionOutputToLoadOnJointMode": lgpConditionOutputToLoadOnJointMode,
       "lgpConditionInputNeutralLost": lgpConditionInputNeutralLost,
       "lgpConditionLowBatteryWarning": lgpConditionLowBatteryWarning,
       "lgpConditionInternalFault": lgpConditionInternalFault,
       "lgpConditionBatteryTestFailed": lgpConditionBatteryTestFailed,
       "lgpConditionPowerModuleWarning": lgpConditionPowerModuleWarning,
       "lgpConditionBatteryModuleWarning": lgpConditionBatteryModuleWarning,
       "lgpConditionControlModuleWarning": lgpConditionControlModuleWarning,
       "lgpConditionUpsOperationFault": lgpConditionUpsOperationFault,
       "lgpConditionActiveAlarm": lgpConditionActiveAlarm,
       "lgpConditionRectifierCommunicationFailure": lgpConditionRectifierCommunicationFailure,
       "lgpConditionInverterCommunicationFailure": lgpConditionInverterCommunicationFailure,
       "lgpConditionParallelSysConnectionFault": lgpConditionParallelSysConnectionFault,
       "lgpConditionParallelSysCommunicationFailure": lgpConditionParallelSysCommunicationFailure,
       "lgpConditionLostBatteryRedundancy": lgpConditionLostBatteryRedundancy,
       "lgpConditionCompPumpDownFailure": lgpConditionCompPumpDownFailure,
       "lgpConditionComp1PumpDownFailure": lgpConditionComp1PumpDownFailure,
       "lgpConditionComp2PumpDownFailure": lgpConditionComp2PumpDownFailure,
       "lgpConditionChilledWaterLowWaterFlow": lgpConditionChilledWaterLowWaterFlow,
       "lgpConditionChilledWaterLowWaterFlowCircuit2": lgpConditionChilledWaterLowWaterFlowCircuit2,
       "lgpConditionAirFilterClogged": lgpConditionAirFilterClogged,
       "lgpConditionHumidifierFailure": lgpConditionHumidifierFailure,
       "lgpConditionRunHoursExceeded": lgpConditionRunHoursExceeded,
       "lgpConditionUnitRunHrsExceeded": lgpConditionUnitRunHrsExceeded,
       "lgpConditionComp1RunHrsExceeded": lgpConditionComp1RunHrsExceeded,
       "lgpConditionComp2RunHrsExceeded": lgpConditionComp2RunHrsExceeded,
       "lgpConditionFreeCoolRunHrsExceeded": lgpConditionFreeCoolRunHrsExceeded,
       "lgpConditionElectricalHeater1RunHrsExceeded": lgpConditionElectricalHeater1RunHrsExceeded,
       "lgpConditionElectricalHeater2RunHrsExceeded": lgpConditionElectricalHeater2RunHrsExceeded,
       "lgpConditionElectricalHeater3RunHrsExceeded": lgpConditionElectricalHeater3RunHrsExceeded,
       "lgpConditionHotWaterRunHrsExceeded": lgpConditionHotWaterRunHrsExceeded,
       "lgpConditionHotGasRunHrsExceeded": lgpConditionHotGasRunHrsExceeded,
       "lgpConditionHumidifierRunHrsExceeded": lgpConditionHumidifierRunHrsExceeded,
       "lgpConditionDehumidiferRunHrsExceeded": lgpConditionDehumidiferRunHrsExceeded,
       "lgpConditionFanRunHrsExceeded": lgpConditionFanRunHrsExceeded,
       "lgpConditionCommWarning": lgpConditionCommWarning,
       "lgpConditionCommWarningUnit1": lgpConditionCommWarningUnit1,
       "lgpConditionCommWarningUnit2": lgpConditionCommWarningUnit2,
       "lgpConditionCommWarningUnit3": lgpConditionCommWarningUnit3,
       "lgpConditionCommWarningUnit4": lgpConditionCommWarningUnit4,
       "lgpConditionCommWarningUnit5": lgpConditionCommWarningUnit5,
       "lgpConditionCommWarningUnit6": lgpConditionCommWarningUnit6,
       "lgpConditionCommWarningUnit7": lgpConditionCommWarningUnit7,
       "lgpConditionCommWarningUnit8": lgpConditionCommWarningUnit8,
       "lgpConditionCommWarningUnit9": lgpConditionCommWarningUnit9,
       "lgpConditionCommWarningUnit10": lgpConditionCommWarningUnit10,
       "lgpConditionCommWarningUnit11": lgpConditionCommWarningUnit11,
       "lgpConditionCommWarningUnit12": lgpConditionCommWarningUnit12,
       "lgpConditionCommWarningUnit13": lgpConditionCommWarningUnit13,
       "lgpConditionCommWarningUnit14": lgpConditionCommWarningUnit14,
       "lgpConditionCommWarningUnit15": lgpConditionCommWarningUnit15,
       "lgpConditionCommWarningUnit16": lgpConditionCommWarningUnit16,
       "lgpConditionUnitOn": lgpConditionUnitOn,
       "lgpConditionUnitOff": lgpConditionUnitOff,
       "lgpConditionSleepModeOff": lgpConditionSleepModeOff,
       "lgpConditionPowerOn": lgpConditionPowerOn,
       "lgpConditionSystemOnStanby": lgpConditionSystemOnStanby,
       "lgpConditionPowerOff": lgpConditionPowerOff,
       "lgpConditionHighTemperatureGroup": lgpConditionHighTemperatureGroup,
       "lgpConditionHighTemperatureSensor1": lgpConditionHighTemperatureSensor1,
       "lgpConditionHighTemperatureDigitalScroll1": lgpConditionHighTemperatureDigitalScroll1,
       "lgpConditionHighTemperatureDigitalScroll2": lgpConditionHighTemperatureDigitalScroll2,
       "lgpConditionHighTemperatureUser1": lgpConditionHighTemperatureUser1,
       "lgpConditionHighTemperatureInternal": lgpConditionHighTemperatureInternal,
       "lgpConditionHighTemperatureExternalAirSensorA": lgpConditionHighTemperatureExternalAirSensorA,
       "lgpConditionHighTemperatureExternalAirSensorB": lgpConditionHighTemperatureExternalAirSensorB,
       "lgpConditionHighTemperatureRefrigerantSupply": lgpConditionHighTemperatureRefrigerantSupply,
       "lgpConditionHighTemperatureFluidSupply": lgpConditionHighTemperatureFluidSupply,
       "lgpConditionHighTemperatureSupplyAir": lgpConditionHighTemperatureSupplyAir,
       "lgpConditionHighTemperatureReturnAir": lgpConditionHighTemperatureReturnAir,
       "lgpConditionLowTemperatureGroup": lgpConditionLowTemperatureGroup,
       "lgpConditionLowTemperatureSensor1": lgpConditionLowTemperatureSensor1,
       "lgpConditionLowTemperatureInternal": lgpConditionLowTemperatureInternal,
       "lgpConditionLowTemperatureExternalAirSensorA": lgpConditionLowTemperatureExternalAirSensorA,
       "lgpConditionLowTemperatureExternalAirSensorB": lgpConditionLowTemperatureExternalAirSensorB,
       "lgpConditionLowTemperatureRefrigerantSupply": lgpConditionLowTemperatureRefrigerantSupply,
       "lgpConditionLowTemperatureFluidSupply": lgpConditionLowTemperatureFluidSupply,
       "lgpConditionLowTemperatureSupplyAir": lgpConditionLowTemperatureSupplyAir,
       "lgpConditionHighHumidityGroup": lgpConditionHighHumidityGroup,
       "lgpConditionHighHumiditySensor1": lgpConditionHighHumiditySensor1,
       "lgpConditionHighHumidityReturnAir": lgpConditionHighHumidityReturnAir,
       "lgpConditionLowHumidityGroup": lgpConditionLowHumidityGroup,
       "lgpConditionLowHumiditySensor1": lgpConditionLowHumiditySensor1,
       "lgpConditionLowHumidityReturnAir": lgpConditionLowHumidityReturnAir,
       "lgpConditionPeerNetworkNoMaster": lgpConditionPeerNetworkNoMaster,
       "lgpConditionNoOnOffPermissions": lgpConditionNoOnOffPermissions,
       "lgpConditionPeerNetworkFailure": lgpConditionPeerNetworkFailure,
       "lgpConditionUnitDisabled": lgpConditionUnitDisabled,
       "lgpConditionUnitShutdown": lgpConditionUnitShutdown,
       "lgpConditionPeerNetworkDiscovered": lgpConditionPeerNetworkDiscovered,
       "lgpConditionLossOfWaterFlow": lgpConditionLossOfWaterFlow,
       "lgpConditionCondensatePumpHighWater": lgpConditionCondensatePumpHighWater,
       "lgpConditionGeneralAlarm": lgpConditionGeneralAlarm,
       "lgpConditionProductSpecific": lgpConditionProductSpecific,
       "lgpConditionReheatLockout": lgpConditionReheatLockout,
       "lgpConditionHumidifierLockout": lgpConditionHumidifierLockout,
       "lgpConditionCompressorsLockout": lgpConditionCompressorsLockout,
       "lgpConditionCallService": lgpConditionCallService,
       "lgpConditionLowMemoryGroup": lgpConditionLowMemoryGroup,
       "lgpConditionLowMemory1": lgpConditionLowMemory1,
       "lgpConditionMemoryFailureGroup": lgpConditionMemoryFailureGroup,
       "lgpConditionMemory1Failure": lgpConditionMemory1Failure,
       "lgpConditionMemory2Failure": lgpConditionMemory2Failure,
       "lgpConditionUnitCodeErrorGroup": lgpConditionUnitCodeErrorGroup,
       "lgpConditionUnitCodeNotConfigured": lgpConditionUnitCodeNotConfigured,
       "lgpConditionUnitCode01OutOfRange": lgpConditionUnitCode01OutOfRange,
       "lgpConditionUnitCode02OutOfRange": lgpConditionUnitCode02OutOfRange,
       "lgpConditionUnitCode03OutOfRange": lgpConditionUnitCode03OutOfRange,
       "lgpConditionUnitCode04OutOfRange": lgpConditionUnitCode04OutOfRange,
       "lgpConditionUnitCode05OutOfRange": lgpConditionUnitCode05OutOfRange,
       "lgpConditionUnitCode06OutOfRange": lgpConditionUnitCode06OutOfRange,
       "lgpConditionUnitCode07OutOfRange": lgpConditionUnitCode07OutOfRange,
       "lgpConditionUnitCode08OutOfRange": lgpConditionUnitCode08OutOfRange,
       "lgpConditionUnitCode09OutOfRange": lgpConditionUnitCode09OutOfRange,
       "lgpConditionUnitCode10OutOfRange": lgpConditionUnitCode10OutOfRange,
       "lgpConditionUnitCode11OutOfRange": lgpConditionUnitCode11OutOfRange,
       "lgpConditionUnitCode12OutOfRange": lgpConditionUnitCode12OutOfRange,
       "lgpConditionUnitCode13OutOfRange": lgpConditionUnitCode13OutOfRange,
       "lgpConditionUnitCode14OutOfRange": lgpConditionUnitCode14OutOfRange,
       "lgpConditionUnitCode15OutOfRange": lgpConditionUnitCode15OutOfRange,
       "lgpConditionUnitCode16OutOfRange": lgpConditionUnitCode16OutOfRange,
       "lgpConditionUnitCode17OutOfRange": lgpConditionUnitCode17OutOfRange,
       "lgpConditionUnitCode18OutOfRange": lgpConditionUnitCode18OutOfRange,
       "lgpConditionHighExternalDewPoint": lgpConditionHighExternalDewPoint,
       "lgpConditionHcbDisconnected": lgpConditionHcbDisconnected,
       "lgpConditionBmsResetTimerExpired": lgpConditionBmsResetTimerExpired,
       "lgpConditionAgentFirmwareCorrupt": lgpConditionAgentFirmwareCorrupt,
       "lgpConditionSystemAccessGroup": lgpConditionSystemAccessGroup,
       "lgpConditionFrontAccessOpen": lgpConditionFrontAccessOpen,
       "lgpConditionRearAccessOpen": lgpConditionRearAccessOpen,
       "lgpConditionsDamperFailure": lgpConditionsDamperFailure,
       "lgpConditionEmergencyDamperFailure": lgpConditionEmergencyDamperFailure,
       "lgpConditionRemoteShutdown": lgpConditionRemoteShutdown,
       "lgpConditionFireAlarm": lgpConditionFireAlarm,
       "lgpConditionHeatersOverheated": lgpConditionHeatersOverheated,
       "lgpConditionCondenserFailureGroup": lgpConditionCondenserFailureGroup,
       "lgpConditionCondenser1Failure": lgpConditionCondenser1Failure,
       "lgpConditionCondenser2Failure": lgpConditionCondenser2Failure,
       "lgpConditionCondenserTVSSFailure": lgpConditionCondenserTVSSFailure,
       "lgpConditionHumidifierCyclinderWorn": lgpConditionHumidifierCyclinderWorn,
       "lgpConditionUnderCurrent": lgpConditionUnderCurrent,
       "lgpConditionHumidifierUnderCurrent": lgpConditionHumidifierUnderCurrent,
       "lgpConditionInputUnderCurrent": lgpConditionInputUnderCurrent,
       "lgpConditionHeatRejectorGroup": lgpConditionHeatRejectorGroup,
       "lgpConditionHeatRejectorFanFailure": lgpConditionHeatRejectorFanFailure,
       "lgpConditionHeatRejectorVoltageSuppressionFailure": lgpConditionHeatRejectorVoltageSuppressionFailure,
       "lgpConditionFreeCoolLockout": lgpConditionFreeCoolLockout,
       "lgpConditionWaterLeakSensorFailure": lgpConditionWaterLeakSensorFailure,
       "lgpConditionNoLoadDetectedWarning": lgpConditionNoLoadDetectedWarning,
       "lgpConditionFirmwareGroup": lgpConditionFirmwareGroup,
       "lgpConditionFirmwareUpdateRequired": lgpConditionFirmwareUpdateRequired,
       "lgpConditionTestGroup": lgpConditionTestGroup,
       "lgpConditionTest01": lgpConditionTest01,
       "lgpConditionReceptacleBranchGroup": lgpConditionReceptacleBranchGroup,
       "lgpConditionRcpBranchFailure": lgpConditionRcpBranchFailure,
       "lgpConditionRcpBranchBreakerOpen": lgpConditionRcpBranchBreakerOpen,
       "lgpConditionInputUnqualified": lgpConditionInputUnqualified,
       "lgpConditionBypassUnavailable": lgpConditionBypassUnavailable,
       "lgpConditionAutoTransferFailed": lgpConditionAutoTransferFailed,
       "lgpConditionSBSUnavailable": lgpConditionSBSUnavailable,
       "lgpConditionSBSOverload": lgpConditionSBSOverload,
       "lgpConditionExcessPulseParallel": lgpConditionExcessPulseParallel,
       "lgpConditionRemoteBypassSwitchOffExt": lgpConditionRemoteBypassSwitchOffExt,
       "lgpConditionManTransferInhibited": lgpConditionManTransferInhibited,
       "lgpConditionManReTransferInhibited": lgpConditionManReTransferInhibited,
       "lgpConditionBatteryChargeError": lgpConditionBatteryChargeError,
       "lgpConditionBatteryAutoTestInhibited": lgpConditionBatteryAutoTestInhibited,
       "lgpConditionBatteryChargeReducedExt": lgpConditionBatteryChargeReducedExt,
       "lgpConditionBatteryCapacityLow": lgpConditionBatteryCapacityLow,
       "lgpConditionBatteryTempImbalance": lgpConditionBatteryTempImbalance,
       "lgpConditionBatteryEqualize": lgpConditionBatteryEqualize,
       "lgpConditionBatteryChargeInhibitedExt": lgpConditionBatteryChargeInhibitedExt,
       "lgpConditionServiceExtBatteryMonitorGroup": lgpConditionServiceExtBatteryMonitorGroup,
       "lgpConditionServiceExtBatteryMonitor1": lgpConditionServiceExtBatteryMonitor1,
       "lgpConditionServiceExtBatteryMonitor2": lgpConditionServiceExtBatteryMonitor2,
       "lgpConditionBatteryGroundFault": lgpConditionBatteryGroundFault,
       "lgpConditionBatteryLowShutdown": lgpConditionBatteryLowShutdown,
       "lgpConditionEmergencyPowerOffLocal": lgpConditionEmergencyPowerOffLocal,
       "lgpConditionOutputLowPFLagging": lgpConditionOutputLowPFLagging,
       "lgpConditionOutputLowPFLeading": lgpConditionOutputLowPFLeading,
       "lgpConditionOutputToLoadFault": lgpConditionOutputToLoadFault,
       "lgpConditionInvRestartInhibitedExt": lgpConditionInvRestartInhibitedExt,
       "lgpConditionInverterShutdownOverload": lgpConditionInverterShutdownOverload,
       "lgpConditionInverterOffExt": lgpConditionInverterOffExt,
       "lgpConditionInputContactGroup": lgpConditionInputContactGroup,
       "lgpConditionInputContact01": lgpConditionInputContact01,
       "lgpConditionInputContact02": lgpConditionInputContact02,
       "lgpConditionInputContact03": lgpConditionInputContact03,
       "lgpConditionInputContact04": lgpConditionInputContact04,
       "lgpConditionInputContact05": lgpConditionInputContact05,
       "lgpConditionInputContact06": lgpConditionInputContact06,
       "lgpConditionInputContact07": lgpConditionInputContact07,
       "lgpConditionInputContact08": lgpConditionInputContact08,
       "lgpConditionInputContact09": lgpConditionInputContact09,
       "lgpConditionInputContact10": lgpConditionInputContact10,
       "lgpConditionInputContact11": lgpConditionInputContact11,
       "lgpConditionInputContact12": lgpConditionInputContact12,
       "lgpConditionInputContact13": lgpConditionInputContact13,
       "lgpConditionInputContact14": lgpConditionInputContact14,
       "lgpConditionInputContact15": lgpConditionInputContact15,
       "lgpConditionInputContact16": lgpConditionInputContact16,
       "lgpConditionRectifierOperInhibited": lgpConditionRectifierOperInhibited,
       "lgpConditionBypassBackFeedBrkrOpen": lgpConditionBypassBackFeedBrkrOpen,
       "lgpConditionAutoRestartInProgress": lgpConditionAutoRestartInProgress,
       "lgpConditionAutoRestartInhibitedExt": lgpConditionAutoRestartInhibitedExt,
       "lgpConditionAutoRestartFailed": lgpConditionAutoRestartFailed,
       "lgpConditionInputOnGenerator": lgpConditionInputOnGenerator,
       "lgpConditionInputFilterCycleLock": lgpConditionInputFilterCycleLock,
       "lgpConditionServiceCodeActive": lgpConditionServiceCodeActive,
       "lgpConditionLoadBusSyncActive": lgpConditionLoadBusSyncActive,
       "lgpConditionLoadBusSyncInhibited": lgpConditionLoadBusSyncInhibited,
       "lgpConditionControlsResetRequired": lgpConditionControlsResetRequired,
       "lgpConditionEquipTempSensorFailed": lgpConditionEquipTempSensorFailed,
       "lgpConditionInputCurrentImbalance": lgpConditionInputCurrentImbalance,
       "lgpConditionPumpGroup": lgpConditionPumpGroup,
       "lgpConditionPumpFlowLoss": lgpConditionPumpFlowLoss,
       "lgpConditionPump1FlowLoss": lgpConditionPump1FlowLoss,
       "lgpConditionPump2FlowLoss": lgpConditionPump2FlowLoss,
       "lgpConditionPumpShortCycle": lgpConditionPumpShortCycle,
       "lgpConditionPumpInverterShortCycle": lgpConditionPumpInverterShortCycle,
       "lgpConditionPump1InverterShortCycle": lgpConditionPump1InverterShortCycle,
       "lgpConditionPump2InverterShortCycle": lgpConditionPump2InverterShortCycle,
       "lgpConditionValveGroup": lgpConditionValveGroup,
       "lgpConditionChilledWaterValvePosition": lgpConditionChilledWaterValvePosition,
       "lgpConditionCondensationDetected": lgpConditionCondensationDetected,
       "lgpConditionMaintenanceGroup": lgpConditionMaintenanceGroup,
       "lgpConditionMaintenanceDue": lgpConditionMaintenanceDue,
       "lgpConditionMaintenanceComplete": lgpConditionMaintenanceComplete,
       "lgpConditionExternalEventSignalGroup": lgpConditionExternalEventSignalGroup,
       "lgpConditionExternalFireDetect": lgpConditionExternalFireDetect,
       "lgpConditionExternalFlowLoss": lgpConditionExternalFlowLoss,
       "lgpConditionExternalReheatLockout": lgpConditionExternalReheatLockout,
       "lgpConditionExternalOverTemp": lgpConditionExternalOverTemp,
       "lgpConditionExternalCompLockout": lgpConditionExternalCompLockout,
       "lgpConditionExternalHumidifierLockout": lgpConditionExternalHumidifierLockout,
       "lgpConditionComponentShutdownGroup": lgpConditionComponentShutdownGroup,
       "lgpConditionComponentShutdownPartial": lgpConditionComponentShutdownPartial,
       "lgpConditionComponentShutdownHighPower": lgpConditionComponentShutdownHighPower,
       "lgpConditionCondenserProblemGroup": lgpConditionCondenserProblemGroup,
       "lgpConditionCondenser1Problem": lgpConditionCondenser1Problem,
       "lgpConditionHumidityOutOfPropBand": lgpConditionHumidityOutOfPropBand,
       "lgpConditionEnvRemoteSensorGroup": lgpConditionEnvRemoteSensorGroup,
       "lgpConditionEnvRemoteSensor1Issue": lgpConditionEnvRemoteSensor1Issue,
       "lgpConditionEnvRemoteSensor2Issue": lgpConditionEnvRemoteSensor2Issue,
       "lgpConditionEnvRemoteSensor3Issue": lgpConditionEnvRemoteSensor3Issue,
       "lgpConditionEnvRemoteSensor4Issue": lgpConditionEnvRemoteSensor4Issue,
       "lgpConditionEnvRemoteSensor5Issue": lgpConditionEnvRemoteSensor5Issue,
       "lgpConditionEnvRemoteSensor6Issue": lgpConditionEnvRemoteSensor6Issue,
       "lgpConditionEnvRemoteSensor7Issue": lgpConditionEnvRemoteSensor7Issue,
       "lgpConditionEnvRemoteSensor8Issue": lgpConditionEnvRemoteSensor8Issue,
       "lgpConditionEnvRemoteSensor9Issue": lgpConditionEnvRemoteSensor9Issue,
       "lgpConditionEnvRemoteSensor10Issue": lgpConditionEnvRemoteSensor10Issue,
       "lgpConditionNeutralSnubberBoardCommFailure": lgpConditionNeutralSnubberBoardCommFailure,
       "lgpConditionRedundantChargerFailure": lgpConditionRedundantChargerFailure,
       "lgpConditionBoardInputContactorPowerFailure": lgpConditionBoardInputContactorPowerFailure,
       "lgpConditionBoard1InputContactorPowerFailure": lgpConditionBoard1InputContactorPowerFailure,
       "lgpConditionBoard2InputContactorPowerFailure": lgpConditionBoard2InputContactorPowerFailure,
       "lgpConditionTooManySensors": lgpConditionTooManySensors,
       "lgpConditionDoorSwitchOpen": lgpConditionDoorSwitchOpen,
       "lgpConditionContactClosureOpen": lgpConditionContactClosureOpen,
       "lgpConditionContactClosureClosed": lgpConditionContactClosureClosed,
       "lgpConditionSensorsNotDisplayed": lgpConditionSensorsNotDisplayed,
       "lgpConditionsPresent": lgpConditionsPresent,
       "lgpConditionsTable": lgpConditionsTable,
       "lgpConditionEntry": lgpConditionEntry,
       "lgpConditionId": lgpConditionId,
       "lgpConditionDescr": lgpConditionDescr,
       "lgpConditionTime": lgpConditionTime,
       "lgpConditionTableRef": lgpConditionTableRef,
       "lgpConditionTableRowRef": lgpConditionTableRowRef,
       "lgpConditionType": lgpConditionType,
       "lgpConditionCurrentState": lgpConditionCurrentState,
       "lgpConditionSeverity": lgpConditionSeverity,
       "lgpConditionAcknowledged": lgpConditionAcknowledged,
       "lgpConditionAckReq": lgpConditionAckReq,
       "lgpConditionControl": lgpConditionControl,
       "lgpConditionControlEventReset": lgpConditionControlEventReset,
       "lgpConditionControlEventAck": lgpConditionControlEventAck,
       "lgpConditionControlTable": lgpConditionControlTable,
       "lgpConditionControlEntry": lgpConditionControlEntry,
       "lgpConditionControlIndex": lgpConditionControlIndex,
       "lgpConditionControlDescr": lgpConditionControlDescr,
       "lgpConditionControlEnableStatus": lgpConditionControlEnableStatus,
       "lgpConditionControlType": lgpConditionControlType,
       "lgpConditionControlEnableCapability": lgpConditionControlEnableCapability,
       "lgpConditionDescription": lgpConditionDescription,
       "lgpNetworkName": lgpNetworkName,
       "lgpFlexConditions": lgpFlexConditions}
)
