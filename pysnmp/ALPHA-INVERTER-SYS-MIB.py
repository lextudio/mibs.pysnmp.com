# SNMP MIB module (ALPHA-INVERTER-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALPHA-INVERTER-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:45 2024
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

(ScaledNumber,
 simple) = mibBuilder.importSymbols(
    "ALPHA-RESOURCE-MIB",
    "ScaledNumber",
    "simple")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

inverterSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3)
)
inverterSystem.setRevisions(
        ("2016-02-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InvTotalAcOutputPowerVa_Type = ScaledNumber
_InvTotalAcOutputPowerVa_Object = MibScalar
invTotalAcOutputPowerVa = _InvTotalAcOutputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 1),
    _InvTotalAcOutputPowerVa_Type()
)
invTotalAcOutputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invTotalAcOutputPowerVa.setStatus("current")
_InvSysAverageLoadingOfInstalledPowerVa_Type = ScaledNumber
_InvSysAverageLoadingOfInstalledPowerVa_Object = MibScalar
invSysAverageLoadingOfInstalledPowerVa = _InvSysAverageLoadingOfInstalledPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 2),
    _InvSysAverageLoadingOfInstalledPowerVa_Type()
)
invSysAverageLoadingOfInstalledPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAverageLoadingOfInstalledPowerVa.setStatus("current")
_InvSysAverageDcInputToOutputPowerRatio_Type = ScaledNumber
_InvSysAverageDcInputToOutputPowerRatio_Object = MibScalar
invSysAverageDcInputToOutputPowerRatio = _InvSysAverageDcInputToOutputPowerRatio_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 3),
    _InvSysAverageDcInputToOutputPowerRatio_Type()
)
invSysAverageDcInputToOutputPowerRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAverageDcInputToOutputPowerRatio.setStatus("current")
_InvSysSystemMode_Type = ScaledNumber
_InvSysSystemMode_Object = MibScalar
invSysSystemMode = _InvSysSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 4),
    _InvSysSystemMode_Type()
)
invSysSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysSystemMode.setStatus("current")
_InvSysPhase1OutputPowerVa_Type = ScaledNumber
_InvSysPhase1OutputPowerVa_Object = MibScalar
invSysPhase1OutputPowerVa = _InvSysPhase1OutputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 5),
    _InvSysPhase1OutputPowerVa_Type()
)
invSysPhase1OutputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysPhase1OutputPowerVa.setStatus("current")
_InvSysPhase2OutputPowerVa_Type = ScaledNumber
_InvSysPhase2OutputPowerVa_Object = MibScalar
invSysPhase2OutputPowerVa = _InvSysPhase2OutputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 6),
    _InvSysPhase2OutputPowerVa_Type()
)
invSysPhase2OutputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysPhase2OutputPowerVa.setStatus("current")
_InvSysPhase3OutputPowerVa_Type = ScaledNumber
_InvSysPhase3OutputPowerVa_Object = MibScalar
invSysPhase3OutputPowerVa = _InvSysPhase3OutputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 7),
    _InvSysPhase3OutputPowerVa_Type()
)
invSysPhase3OutputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysPhase3OutputPowerVa.setStatus("current")
_InvSysAverageOutputVoltageMeasured_Type = ScaledNumber
_InvSysAverageOutputVoltageMeasured_Object = MibScalar
invSysAverageOutputVoltageMeasured = _InvSysAverageOutputVoltageMeasured_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 8),
    _InvSysAverageOutputVoltageMeasured_Type()
)
invSysAverageOutputVoltageMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAverageOutputVoltageMeasured.setStatus("current")
_InvSysEnabledDisconnects_Type = ScaledNumber
_InvSysEnabledDisconnects_Object = MibScalar
invSysEnabledDisconnects = _InvSysEnabledDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 9),
    _InvSysEnabledDisconnects_Type()
)
invSysEnabledDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysEnabledDisconnects.setStatus("current")
_InvSysActivatedDisconnects_Type = ScaledNumber
_InvSysActivatedDisconnects_Object = MibScalar
invSysActivatedDisconnects = _InvSysActivatedDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 10),
    _InvSysActivatedDisconnects_Type()
)
invSysActivatedDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysActivatedDisconnects.setStatus("current")
_InvSysTotalDCInputCurrent_Type = ScaledNumber
_InvSysTotalDCInputCurrent_Object = MibScalar
invSysTotalDCInputCurrent = _InvSysTotalDCInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 11),
    _InvSysTotalDCInputCurrent_Type()
)
invSysTotalDCInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysTotalDCInputCurrent.setStatus("current")
_InvSysAverageDcInputVoltage_Type = ScaledNumber
_InvSysAverageDcInputVoltage_Object = MibScalar
invSysAverageDcInputVoltage = _InvSysAverageDcInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 12),
    _InvSysAverageDcInputVoltage_Type()
)
invSysAverageDcInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAverageDcInputVoltage.setStatus("current")
_InvSysTotalDcInputPower_Type = ScaledNumber
_InvSysTotalDcInputPower_Object = MibScalar
invSysTotalDcInputPower = _InvSysTotalDcInputPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 13),
    _InvSysTotalDcInputPower_Type()
)
invSysTotalDcInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysTotalDcInputPower.setStatus("current")
_InvSysSystemOnBypass_Type = ScaledNumber
_InvSysSystemOnBypass_Object = MibScalar
invSysSystemOnBypass = _InvSysSystemOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 14),
    _InvSysSystemOnBypass_Type()
)
invSysSystemOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysSystemOnBypass.setStatus("current")
_InvSysTotalAcInputPowerVa_Type = ScaledNumber
_InvSysTotalAcInputPowerVa_Object = MibScalar
invSysTotalAcInputPowerVa = _InvSysTotalAcInputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 18),
    _InvSysTotalAcInputPowerVa_Type()
)
invSysTotalAcInputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysTotalAcInputPowerVa.setStatus("current")
_PhaseGroup_ObjectIdentity = ObjectIdentity
phaseGroup = _PhaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80)
)
_InvSysAcPhaseCount_Type = Integer32
_InvSysAcPhaseCount_Object = MibScalar
invSysAcPhaseCount = _InvSysAcPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 1),
    _InvSysAcPhaseCount_Type()
)
invSysAcPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseCount.setStatus("current")
_InvSysAcPhaseTable_Object = MibTable
invSysAcPhaseTable = _InvSysAcPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2)
)
if mibBuilder.loadTexts:
    invSysAcPhaseTable.setStatus("current")
_InvSysAcPhaseEntry_Object = MibTableRow
invSysAcPhaseEntry = _InvSysAcPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1)
)
invSysAcPhaseEntry.setIndexNames(
    (0, "ALPHA-INVERTER-SYS-MIB", "invSysAcPhaseCount"),
)
if mibBuilder.loadTexts:
    invSysAcPhaseEntry.setStatus("current")
_InvSysAcPhaseAcOutputPowerVa_Type = ScaledNumber
_InvSysAcPhaseAcOutputPowerVa_Object = MibTableColumn
invSysAcPhaseAcOutputPowerVa = _InvSysAcPhaseAcOutputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 1),
    _InvSysAcPhaseAcOutputPowerVa_Type()
)
invSysAcPhaseAcOutputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseAcOutputPowerVa.setStatus("current")
_InvSysAcPhaseOutputVoltageMeasured_Type = ScaledNumber
_InvSysAcPhaseOutputVoltageMeasured_Object = MibTableColumn
invSysAcPhaseOutputVoltageMeasured = _InvSysAcPhaseOutputVoltageMeasured_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 2),
    _InvSysAcPhaseOutputVoltageMeasured_Type()
)
invSysAcPhaseOutputVoltageMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseOutputVoltageMeasured.setStatus("current")
_InvSysAcPhaseOutputCurrent_Type = ScaledNumber
_InvSysAcPhaseOutputCurrent_Object = MibTableColumn
invSysAcPhaseOutputCurrent = _InvSysAcPhaseOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 3),
    _InvSysAcPhaseOutputCurrent_Type()
)
invSysAcPhaseOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseOutputCurrent.setStatus("current")
_InvSysAcPhaseFrequency_Type = ScaledNumber
_InvSysAcPhaseFrequency_Object = MibTableColumn
invSysAcPhaseFrequency = _InvSysAcPhaseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 4),
    _InvSysAcPhaseFrequency_Type()
)
invSysAcPhaseFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseFrequency.setStatus("current")
_InvSysAcPhaseLoadingOfInstalledPowerVa_Type = ScaledNumber
_InvSysAcPhaseLoadingOfInstalledPowerVa_Object = MibTableColumn
invSysAcPhaseLoadingOfInstalledPowerVa = _InvSysAcPhaseLoadingOfInstalledPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 5),
    _InvSysAcPhaseLoadingOfInstalledPowerVa_Type()
)
invSysAcPhaseLoadingOfInstalledPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseLoadingOfInstalledPowerVa.setStatus("current")
_InvSysAcPhaseNumberOfModulesOn_Type = ScaledNumber
_InvSysAcPhaseNumberOfModulesOn_Object = MibTableColumn
invSysAcPhaseNumberOfModulesOn = _InvSysAcPhaseNumberOfModulesOn_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 6),
    _InvSysAcPhaseNumberOfModulesOn_Type()
)
invSysAcPhaseNumberOfModulesOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseNumberOfModulesOn.setStatus("current")
_InvSysAcPhaseLoadingOfInstalledPowerWatts_Type = ScaledNumber
_InvSysAcPhaseLoadingOfInstalledPowerWatts_Object = MibTableColumn
invSysAcPhaseLoadingOfInstalledPowerWatts = _InvSysAcPhaseLoadingOfInstalledPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 7),
    _InvSysAcPhaseLoadingOfInstalledPowerWatts_Type()
)
invSysAcPhaseLoadingOfInstalledPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseLoadingOfInstalledPowerWatts.setStatus("current")
_InvSysAcPhaseDcInputToOutputPowerRatioMeasured_Type = ScaledNumber
_InvSysAcPhaseDcInputToOutputPowerRatioMeasured_Object = MibTableColumn
invSysAcPhaseDcInputToOutputPowerRatioMeasured = _InvSysAcPhaseDcInputToOutputPowerRatioMeasured_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 8),
    _InvSysAcPhaseDcInputToOutputPowerRatioMeasured_Type()
)
invSysAcPhaseDcInputToOutputPowerRatioMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseDcInputToOutputPowerRatioMeasured.setStatus("current")
_InvSysAcPhaseAcInputPowerWatts_Type = ScaledNumber
_InvSysAcPhaseAcInputPowerWatts_Object = MibTableColumn
invSysAcPhaseAcInputPowerWatts = _InvSysAcPhaseAcInputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 9),
    _InvSysAcPhaseAcInputPowerWatts_Type()
)
invSysAcPhaseAcInputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseAcInputPowerWatts.setStatus("current")
_InvSysAcPhaseAcInputPowerVa_Type = ScaledNumber
_InvSysAcPhaseAcInputPowerVa_Object = MibTableColumn
invSysAcPhaseAcInputPowerVa = _InvSysAcPhaseAcInputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 10),
    _InvSysAcPhaseAcInputPowerVa_Type()
)
invSysAcPhaseAcInputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseAcInputPowerVa.setStatus("current")
_InvSysAcPhaseAcOutputPowerWatts_Type = ScaledNumber
_InvSysAcPhaseAcOutputPowerWatts_Object = MibTableColumn
invSysAcPhaseAcOutputPowerWatts = _InvSysAcPhaseAcOutputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 11),
    _InvSysAcPhaseAcOutputPowerWatts_Type()
)
invSysAcPhaseAcOutputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseAcOutputPowerWatts.setStatus("current")
_InvSysAcPhaseDCInputPowerWatts_Type = ScaledNumber
_InvSysAcPhaseDCInputPowerWatts_Object = MibTableColumn
invSysAcPhaseDCInputPowerWatts = _InvSysAcPhaseDCInputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 12),
    _InvSysAcPhaseDCInputPowerWatts_Type()
)
invSysAcPhaseDCInputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseDCInputPowerWatts.setStatus("current")
_InvSysAcPhaseNumberOfRedundantModulesMeasured_Type = ScaledNumber
_InvSysAcPhaseNumberOfRedundantModulesMeasured_Object = MibTableColumn
invSysAcPhaseNumberOfRedundantModulesMeasured = _InvSysAcPhaseNumberOfRedundantModulesMeasured_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 13),
    _InvSysAcPhaseNumberOfRedundantModulesMeasured_Type()
)
invSysAcPhaseNumberOfRedundantModulesMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseNumberOfRedundantModulesMeasured.setStatus("current")
_InvSysAcPhaseNumberOfModulesDetected_Type = ScaledNumber
_InvSysAcPhaseNumberOfModulesDetected_Object = MibTableColumn
invSysAcPhaseNumberOfModulesDetected = _InvSysAcPhaseNumberOfModulesDetected_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 14),
    _InvSysAcPhaseNumberOfModulesDetected_Type()
)
invSysAcPhaseNumberOfModulesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseNumberOfModulesDetected.setStatus("current")
_InvSysAcPhaseNumberOfModulesOff_Type = ScaledNumber
_InvSysAcPhaseNumberOfModulesOff_Object = MibTableColumn
invSysAcPhaseNumberOfModulesOff = _InvSysAcPhaseNumberOfModulesOff_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 15),
    _InvSysAcPhaseNumberOfModulesOff_Type()
)
invSysAcPhaseNumberOfModulesOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseNumberOfModulesOff.setStatus("current")
_InvSysAcPhaseNumberOfModulesFailed_Type = ScaledNumber
_InvSysAcPhaseNumberOfModulesFailed_Object = MibTableColumn
invSysAcPhaseNumberOfModulesFailed = _InvSysAcPhaseNumberOfModulesFailed_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 80, 2, 1, 16),
    _InvSysAcPhaseNumberOfModulesFailed_Type()
)
invSysAcPhaseNumberOfModulesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcPhaseNumberOfModulesFailed.setStatus("current")
_AcInputGroup_ObjectIdentity = ObjectIdentity
acInputGroup = _AcInputGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81)
)
_InvSysAcInputCount_Type = Integer32
_InvSysAcInputCount_Object = MibScalar
invSysAcInputCount = _InvSysAcInputCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 1),
    _InvSysAcInputCount_Type()
)
invSysAcInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputCount.setStatus("current")
_InvSysAcInputTable_Object = MibTable
invSysAcInputTable = _InvSysAcInputTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2)
)
if mibBuilder.loadTexts:
    invSysAcInputTable.setStatus("current")
_InvSysAcInputEntry_Object = MibTableRow
invSysAcInputEntry = _InvSysAcInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1)
)
invSysAcInputEntry.setIndexNames(
    (0, "ALPHA-INVERTER-SYS-MIB", "invSysAcInputCount"),
)
if mibBuilder.loadTexts:
    invSysAcInputEntry.setStatus("current")
_InvSysAcInputInputVoltage_Type = ScaledNumber
_InvSysAcInputInputVoltage_Object = MibTableColumn
invSysAcInputInputVoltage = _InvSysAcInputInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 1),
    _InvSysAcInputInputVoltage_Type()
)
invSysAcInputInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputInputVoltage.setStatus("current")
_InvSysAcInputInputCurrent_Type = ScaledNumber
_InvSysAcInputInputCurrent_Object = MibTableColumn
invSysAcInputInputCurrent = _InvSysAcInputInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 2),
    _InvSysAcInputInputCurrent_Type()
)
invSysAcInputInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputInputCurrent.setStatus("current")
_InvSysAcInputFrequency_Type = ScaledNumber
_InvSysAcInputFrequency_Object = MibTableColumn
invSysAcInputFrequency = _InvSysAcInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 3),
    _InvSysAcInputFrequency_Type()
)
invSysAcInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputFrequency.setStatus("current")
_InvSysAcInputAcInputPowerVa_Type = ScaledNumber
_InvSysAcInputAcInputPowerVa_Object = MibTableColumn
invSysAcInputAcInputPowerVa = _InvSysAcInputAcInputPowerVa_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 4),
    _InvSysAcInputAcInputPowerVa_Type()
)
invSysAcInputAcInputPowerVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputAcInputPowerVa.setStatus("current")
_InvSysAcInputNumberOfModulesOn_Type = ScaledNumber
_InvSysAcInputNumberOfModulesOn_Object = MibTableColumn
invSysAcInputNumberOfModulesOn = _InvSysAcInputNumberOfModulesOn_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 5),
    _InvSysAcInputNumberOfModulesOn_Type()
)
invSysAcInputNumberOfModulesOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputNumberOfModulesOn.setStatus("current")
_InvSysAcInputAcInputPowerWatts_Type = ScaledNumber
_InvSysAcInputAcInputPowerWatts_Object = MibTableColumn
invSysAcInputAcInputPowerWatts = _InvSysAcInputAcInputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 6),
    _InvSysAcInputAcInputPowerWatts_Type()
)
invSysAcInputAcInputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputAcInputPowerWatts.setStatus("current")
_InvSysAcInputNumberOfModulesDetected_Type = ScaledNumber
_InvSysAcInputNumberOfModulesDetected_Object = MibTableColumn
invSysAcInputNumberOfModulesDetected = _InvSysAcInputNumberOfModulesDetected_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 7),
    _InvSysAcInputNumberOfModulesDetected_Type()
)
invSysAcInputNumberOfModulesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputNumberOfModulesDetected.setStatus("current")
_InvSysAcInputNumberOfModulesOff_Type = ScaledNumber
_InvSysAcInputNumberOfModulesOff_Object = MibTableColumn
invSysAcInputNumberOfModulesOff = _InvSysAcInputNumberOfModulesOff_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 8),
    _InvSysAcInputNumberOfModulesOff_Type()
)
invSysAcInputNumberOfModulesOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputNumberOfModulesOff.setStatus("current")
_InvSysAcInputNumberOfModulesFailed_Type = ScaledNumber
_InvSysAcInputNumberOfModulesFailed_Object = MibTableColumn
invSysAcInputNumberOfModulesFailed = _InvSysAcInputNumberOfModulesFailed_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 81, 2, 1, 9),
    _InvSysAcInputNumberOfModulesFailed_Type()
)
invSysAcInputNumberOfModulesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysAcInputNumberOfModulesFailed.setStatus("current")
_DcInputGroup_ObjectIdentity = ObjectIdentity
dcInputGroup = _DcInputGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82)
)
_InvSysDcInputCount_Type = Integer32
_InvSysDcInputCount_Object = MibScalar
invSysDcInputCount = _InvSysDcInputCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 1),
    _InvSysDcInputCount_Type()
)
invSysDcInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputCount.setStatus("current")
_InvSysDcInputTable_Object = MibTable
invSysDcInputTable = _InvSysDcInputTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2)
)
if mibBuilder.loadTexts:
    invSysDcInputTable.setStatus("current")
_InvSysDcInputEntry_Object = MibTableRow
invSysDcInputEntry = _InvSysDcInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1)
)
invSysDcInputEntry.setIndexNames(
    (0, "ALPHA-INVERTER-SYS-MIB", "invSysDcInputCount"),
)
if mibBuilder.loadTexts:
    invSysDcInputEntry.setStatus("current")
_InvSysDcInputInputVoltage_Type = ScaledNumber
_InvSysDcInputInputVoltage_Object = MibTableColumn
invSysDcInputInputVoltage = _InvSysDcInputInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1, 1),
    _InvSysDcInputInputVoltage_Type()
)
invSysDcInputInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputInputVoltage.setStatus("current")
_InvSysDcInputInputCurrent_Type = ScaledNumber
_InvSysDcInputInputCurrent_Object = MibTableColumn
invSysDcInputInputCurrent = _InvSysDcInputInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1, 2),
    _InvSysDcInputInputCurrent_Type()
)
invSysDcInputInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputInputCurrent.setStatus("current")
_InvSysDcInputDcInputPowerWatts_Type = ScaledNumber
_InvSysDcInputDcInputPowerWatts_Object = MibTableColumn
invSysDcInputDcInputPowerWatts = _InvSysDcInputDcInputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1, 3),
    _InvSysDcInputDcInputPowerWatts_Type()
)
invSysDcInputDcInputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputDcInputPowerWatts.setStatus("current")
_InvSysDcInputNumberOfModulesOn_Type = ScaledNumber
_InvSysDcInputNumberOfModulesOn_Object = MibTableColumn
invSysDcInputNumberOfModulesOn = _InvSysDcInputNumberOfModulesOn_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1, 4),
    _InvSysDcInputNumberOfModulesOn_Type()
)
invSysDcInputNumberOfModulesOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputNumberOfModulesOn.setStatus("current")
_InvSysDcInputNumberOfModulesOff_Type = ScaledNumber
_InvSysDcInputNumberOfModulesOff_Object = MibTableColumn
invSysDcInputNumberOfModulesOff = _InvSysDcInputNumberOfModulesOff_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1, 5),
    _InvSysDcInputNumberOfModulesOff_Type()
)
invSysDcInputNumberOfModulesOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputNumberOfModulesOff.setStatus("current")
_InvSysDcInputNumberOfModulesFailed_Type = ScaledNumber
_InvSysDcInputNumberOfModulesFailed_Object = MibTableColumn
invSysDcInputNumberOfModulesFailed = _InvSysDcInputNumberOfModulesFailed_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1, 6),
    _InvSysDcInputNumberOfModulesFailed_Type()
)
invSysDcInputNumberOfModulesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputNumberOfModulesFailed.setStatus("current")
_InvSysDcInputNumberOfModulesDetected_Type = ScaledNumber
_InvSysDcInputNumberOfModulesDetected_Object = MibTableColumn
invSysDcInputNumberOfModulesDetected = _InvSysDcInputNumberOfModulesDetected_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 3, 82, 2, 1, 7),
    _InvSysDcInputNumberOfModulesDetected_Type()
)
invSysDcInputNumberOfModulesDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invSysDcInputNumberOfModulesDetected.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHA-INVERTER-SYS-MIB",
    **{"inverterSystem": inverterSystem,
       "invTotalAcOutputPowerVa": invTotalAcOutputPowerVa,
       "invSysAverageLoadingOfInstalledPowerVa": invSysAverageLoadingOfInstalledPowerVa,
       "invSysAverageDcInputToOutputPowerRatio": invSysAverageDcInputToOutputPowerRatio,
       "invSysSystemMode": invSysSystemMode,
       "invSysPhase1OutputPowerVa": invSysPhase1OutputPowerVa,
       "invSysPhase2OutputPowerVa": invSysPhase2OutputPowerVa,
       "invSysPhase3OutputPowerVa": invSysPhase3OutputPowerVa,
       "invSysAverageOutputVoltageMeasured": invSysAverageOutputVoltageMeasured,
       "invSysEnabledDisconnects": invSysEnabledDisconnects,
       "invSysActivatedDisconnects": invSysActivatedDisconnects,
       "invSysTotalDCInputCurrent": invSysTotalDCInputCurrent,
       "invSysAverageDcInputVoltage": invSysAverageDcInputVoltage,
       "invSysTotalDcInputPower": invSysTotalDcInputPower,
       "invSysSystemOnBypass": invSysSystemOnBypass,
       "invSysTotalAcInputPowerVa": invSysTotalAcInputPowerVa,
       "phaseGroup": phaseGroup,
       "invSysAcPhaseCount": invSysAcPhaseCount,
       "invSysAcPhaseTable": invSysAcPhaseTable,
       "invSysAcPhaseEntry": invSysAcPhaseEntry,
       "invSysAcPhaseAcOutputPowerVa": invSysAcPhaseAcOutputPowerVa,
       "invSysAcPhaseOutputVoltageMeasured": invSysAcPhaseOutputVoltageMeasured,
       "invSysAcPhaseOutputCurrent": invSysAcPhaseOutputCurrent,
       "invSysAcPhaseFrequency": invSysAcPhaseFrequency,
       "invSysAcPhaseLoadingOfInstalledPowerVa": invSysAcPhaseLoadingOfInstalledPowerVa,
       "invSysAcPhaseNumberOfModulesOn": invSysAcPhaseNumberOfModulesOn,
       "invSysAcPhaseLoadingOfInstalledPowerWatts": invSysAcPhaseLoadingOfInstalledPowerWatts,
       "invSysAcPhaseDcInputToOutputPowerRatioMeasured": invSysAcPhaseDcInputToOutputPowerRatioMeasured,
       "invSysAcPhaseAcInputPowerWatts": invSysAcPhaseAcInputPowerWatts,
       "invSysAcPhaseAcInputPowerVa": invSysAcPhaseAcInputPowerVa,
       "invSysAcPhaseAcOutputPowerWatts": invSysAcPhaseAcOutputPowerWatts,
       "invSysAcPhaseDCInputPowerWatts": invSysAcPhaseDCInputPowerWatts,
       "invSysAcPhaseNumberOfRedundantModulesMeasured": invSysAcPhaseNumberOfRedundantModulesMeasured,
       "invSysAcPhaseNumberOfModulesDetected": invSysAcPhaseNumberOfModulesDetected,
       "invSysAcPhaseNumberOfModulesOff": invSysAcPhaseNumberOfModulesOff,
       "invSysAcPhaseNumberOfModulesFailed": invSysAcPhaseNumberOfModulesFailed,
       "acInputGroup": acInputGroup,
       "invSysAcInputCount": invSysAcInputCount,
       "invSysAcInputTable": invSysAcInputTable,
       "invSysAcInputEntry": invSysAcInputEntry,
       "invSysAcInputInputVoltage": invSysAcInputInputVoltage,
       "invSysAcInputInputCurrent": invSysAcInputInputCurrent,
       "invSysAcInputFrequency": invSysAcInputFrequency,
       "invSysAcInputAcInputPowerVa": invSysAcInputAcInputPowerVa,
       "invSysAcInputNumberOfModulesOn": invSysAcInputNumberOfModulesOn,
       "invSysAcInputAcInputPowerWatts": invSysAcInputAcInputPowerWatts,
       "invSysAcInputNumberOfModulesDetected": invSysAcInputNumberOfModulesDetected,
       "invSysAcInputNumberOfModulesOff": invSysAcInputNumberOfModulesOff,
       "invSysAcInputNumberOfModulesFailed": invSysAcInputNumberOfModulesFailed,
       "dcInputGroup": dcInputGroup,
       "invSysDcInputCount": invSysDcInputCount,
       "invSysDcInputTable": invSysDcInputTable,
       "invSysDcInputEntry": invSysDcInputEntry,
       "invSysDcInputInputVoltage": invSysDcInputInputVoltage,
       "invSysDcInputInputCurrent": invSysDcInputInputCurrent,
       "invSysDcInputDcInputPowerWatts": invSysDcInputDcInputPowerWatts,
       "invSysDcInputNumberOfModulesOn": invSysDcInputNumberOfModulesOn,
       "invSysDcInputNumberOfModulesOff": invSysDcInputNumberOfModulesOff,
       "invSysDcInputNumberOfModulesFailed": invSysDcInputNumberOfModulesFailed,
       "invSysDcInputNumberOfModulesDetected": invSysDcInputNumberOfModulesDetected}
)
