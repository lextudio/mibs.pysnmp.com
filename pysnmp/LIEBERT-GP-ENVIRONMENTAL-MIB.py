# SNMP MIB module (LIEBERT-GP-ENVIRONMENTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIEBERT-GP-ENVIRONMENTAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:54 2024
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

(lgpEnvironmental,
 liebertEnvironmentalModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpEnvironmental",
    "liebertEnvironmentalModuleReg")

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

liebertGlobalProductsEnvironmentalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 5, 1)
)
liebertGlobalProductsEnvironmentalModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-08-15 00:00",
         "2006-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpEnvTemperature_ObjectIdentity = ObjectIdentity
lgpEnvTemperature = _LgpEnvTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lgpEnvTemperature.setStatus("current")
_LgpEnvTemperatureWellKnown_ObjectIdentity = ObjectIdentity
lgpEnvTemperatureWellKnown = _LgpEnvTemperatureWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureWellKnown.setStatus("current")
_LgpEnvControlTemperature_ObjectIdentity = ObjectIdentity
lgpEnvControlTemperature = _LgpEnvControlTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvControlTemperature.setStatus("current")
_LgpEnvReturnAirTemperature_ObjectIdentity = ObjectIdentity
lgpEnvReturnAirTemperature = _LgpEnvReturnAirTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvReturnAirTemperature.setStatus("current")
_LgpEnvSupplyAirTemperature_ObjectIdentity = ObjectIdentity
lgpEnvSupplyAirTemperature = _LgpEnvSupplyAirTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyAirTemperature.setStatus("current")
_LgpAmbientTemperature_ObjectIdentity = ObjectIdentity
lgpAmbientTemperature = _LgpAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lgpAmbientTemperature.setStatus("current")
_LgpInverterTemperature_ObjectIdentity = ObjectIdentity
lgpInverterTemperature = _LgpInverterTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lgpInverterTemperature.setStatus("current")
_LgpBatteryTempterature_ObjectIdentity = ObjectIdentity
lgpBatteryTempterature = _LgpBatteryTempterature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lgpBatteryTempterature.setStatus("current")
_LgpAcDcConverterTemperature_ObjectIdentity = ObjectIdentity
lgpAcDcConverterTemperature = _LgpAcDcConverterTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    lgpAcDcConverterTemperature.setStatus("current")
_LgpPfcTemperature_ObjectIdentity = ObjectIdentity
lgpPfcTemperature = _LgpPfcTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    lgpPfcTemperature.setStatus("current")
_LgpTransformerTemperature_ObjectIdentity = ObjectIdentity
lgpTransformerTemperature = _LgpTransformerTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    lgpTransformerTemperature.setStatus("current")
_LgpLocalTemperature_ObjectIdentity = ObjectIdentity
lgpLocalTemperature = _LgpLocalTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    lgpLocalTemperature.setStatus("current")
_LgpLocal1Temperature_ObjectIdentity = ObjectIdentity
lgpLocal1Temperature = _LgpLocal1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    lgpLocal1Temperature.setStatus("current")
_LgpLocal2Temperature_ObjectIdentity = ObjectIdentity
lgpLocal2Temperature = _LgpLocal2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    lgpLocal2Temperature.setStatus("current")
_LgpLocal3Temperature_ObjectIdentity = ObjectIdentity
lgpLocal3Temperature = _LgpLocal3Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    lgpLocal3Temperature.setStatus("current")
_LgpDigitalScrollCompressorTemperature_ObjectIdentity = ObjectIdentity
lgpDigitalScrollCompressorTemperature = _LgpDigitalScrollCompressorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    lgpDigitalScrollCompressorTemperature.setStatus("current")
_LgpDigitalScrollCompressor1Temperature_ObjectIdentity = ObjectIdentity
lgpDigitalScrollCompressor1Temperature = _LgpDigitalScrollCompressor1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    lgpDigitalScrollCompressor1Temperature.setStatus("current")
_LgpDigitalScrollCompressor2Temperature_ObjectIdentity = ObjectIdentity
lgpDigitalScrollCompressor2Temperature = _LgpDigitalScrollCompressor2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    lgpDigitalScrollCompressor2Temperature.setStatus("current")
_LgpChillWaterTemperature_ObjectIdentity = ObjectIdentity
lgpChillWaterTemperature = _LgpChillWaterTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    lgpChillWaterTemperature.setStatus("current")
_LgpCoolantTemperature_ObjectIdentity = ObjectIdentity
lgpCoolantTemperature = _LgpCoolantTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    lgpCoolantTemperature.setStatus("current")
_LgpEnvEnclosureTemperatureSensors_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensors = _LgpEnvEnclosureTemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensors.setStatus("current")
_LgpEnvEnclosureTemperatureSensor1_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor1 = _LgpEnvEnclosureTemperatureSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor1.setStatus("current")
_LgpEnvEnclosureTemperatureSensor2_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor2 = _LgpEnvEnclosureTemperatureSensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor2.setStatus("current")
_LgpEnvEnclosureTemperatureSensor3_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor3 = _LgpEnvEnclosureTemperatureSensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 3)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor3.setStatus("current")
_LgpEnvEnclosureTemperatureSensor4_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor4 = _LgpEnvEnclosureTemperatureSensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 4)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor4.setStatus("current")
_LgpEnvValueAmbientRoomTemperature_ObjectIdentity = ObjectIdentity
lgpEnvValueAmbientRoomTemperature = _LgpEnvValueAmbientRoomTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    lgpEnvValueAmbientRoomTemperature.setStatus("current")
_LgpEnvDewPointTemperature_ObjectIdentity = ObjectIdentity
lgpEnvDewPointTemperature = _LgpEnvDewPointTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    lgpEnvDewPointTemperature.setStatus("current")
_LgpEnvEnclosureTemperature_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperature = _LgpEnvEnclosureTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperature.setStatus("current")
_LgpEnvAdjustedTemperature_ObjectIdentity = ObjectIdentity
lgpEnvAdjustedTemperature = _LgpEnvAdjustedTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    lgpEnvAdjustedTemperature.setStatus("current")
_LgpEnvExternalSensors_ObjectIdentity = ObjectIdentity
lgpEnvExternalSensors = _LgpEnvExternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19)
)
if mibBuilder.loadTexts:
    lgpEnvExternalSensors.setStatus("current")
_LgpEnvExternalAirSensorA_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorA = _LgpEnvExternalAirSensorA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorA.setStatus("current")
_LgpEnvExternalAirSensorADewPoint_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorADewPoint = _LgpEnvExternalAirSensorADewPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorADewPoint.setStatus("current")
_LgpEnvExternalAirSensorB_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorB = _LgpEnvExternalAirSensorB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorB.setStatus("current")
_LgpEnvExternalAirSensorBDewPoint_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorBDewPoint = _LgpEnvExternalAirSensorBDewPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 4)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorBDewPoint.setStatus("current")
_LgpEnvSupplyFluidTemperature_ObjectIdentity = ObjectIdentity
lgpEnvSupplyFluidTemperature = _LgpEnvSupplyFluidTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 20)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyFluidTemperature.setStatus("current")
_LgpEnvSupplyRefrigerantTemperature_ObjectIdentity = ObjectIdentity
lgpEnvSupplyRefrigerantTemperature = _LgpEnvSupplyRefrigerantTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 21)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyRefrigerantTemperature.setStatus("current")
_LgpEnvMinDesiredRoomAirTemperature_ObjectIdentity = ObjectIdentity
lgpEnvMinDesiredRoomAirTemperature = _LgpEnvMinDesiredRoomAirTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 22)
)
if mibBuilder.loadTexts:
    lgpEnvMinDesiredRoomAirTemperature.setStatus("current")
_LgpEnvDewPointTemperatures_ObjectIdentity = ObjectIdentity
lgpEnvDewPointTemperatures = _LgpEnvDewPointTemperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 23)
)
if mibBuilder.loadTexts:
    lgpEnvDewPointTemperatures.setStatus("current")
_LgpEnvInletDewPointTemperature_ObjectIdentity = ObjectIdentity
lgpEnvInletDewPointTemperature = _LgpEnvInletDewPointTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    lgpEnvInletDewPointTemperature.setStatus("current")
_LgpEnvTemperatureFahrenheit_ObjectIdentity = ObjectIdentity
lgpEnvTemperatureFahrenheit = _LgpEnvTemperatureFahrenheit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureFahrenheit.setStatus("current")
_LgpEnvTemperatureSettingDegF_Type = Integer32
_LgpEnvTemperatureSettingDegF_Object = MibScalar
lgpEnvTemperatureSettingDegF = _LgpEnvTemperatureSettingDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 1),
    _LgpEnvTemperatureSettingDegF_Type()
)
lgpEnvTemperatureSettingDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureToleranceDegF_Type = Integer32
_LgpEnvTemperatureToleranceDegF_Object = MibScalar
lgpEnvTemperatureToleranceDegF = _LgpEnvTemperatureToleranceDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 2),
    _LgpEnvTemperatureToleranceDegF_Type()
)
lgpEnvTemperatureToleranceDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegF.setUnits("0.1 degrees Fahrenheit")
_LgpEnvTemperatureTableDegF_Object = MibTable
lgpEnvTemperatureTableDegF = _LgpEnvTemperatureTableDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureTableDegF.setStatus("current")
_LgpEnvTemperatureEntryDegF_Object = MibTableRow
lgpEnvTemperatureEntryDegF = _LgpEnvTemperatureEntryDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1)
)
lgpEnvTemperatureEntryDegF.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvTemperatureIdDegF"),
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureEntryDegF.setStatus("current")
_LgpEnvTemperatureIdDegF_Type = Unsigned32
_LgpEnvTemperatureIdDegF_Object = MibTableColumn
lgpEnvTemperatureIdDegF = _LgpEnvTemperatureIdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 1),
    _LgpEnvTemperatureIdDegF_Type()
)
lgpEnvTemperatureIdDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureIdDegF.setStatus("current")
_LgpEnvTemperatureDescrDegF_Type = ObjectIdentifier
_LgpEnvTemperatureDescrDegF_Object = MibTableColumn
lgpEnvTemperatureDescrDegF = _LgpEnvTemperatureDescrDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 2),
    _LgpEnvTemperatureDescrDegF_Type()
)
lgpEnvTemperatureDescrDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDescrDegF.setStatus("current")
_LgpEnvTemperatureMeasurementDegF_Type = Integer32
_LgpEnvTemperatureMeasurementDegF_Object = MibTableColumn
lgpEnvTemperatureMeasurementDegF = _LgpEnvTemperatureMeasurementDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 3),
    _LgpEnvTemperatureMeasurementDegF_Type()
)
lgpEnvTemperatureMeasurementDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureHighThresholdDegF_Type = Integer32
_LgpEnvTemperatureHighThresholdDegF_Object = MibTableColumn
lgpEnvTemperatureHighThresholdDegF = _LgpEnvTemperatureHighThresholdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 4),
    _LgpEnvTemperatureHighThresholdDegF_Type()
)
lgpEnvTemperatureHighThresholdDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureLowThresholdDegF_Type = Integer32
_LgpEnvTemperatureLowThresholdDegF_Object = MibTableColumn
lgpEnvTemperatureLowThresholdDegF = _LgpEnvTemperatureLowThresholdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 5),
    _LgpEnvTemperatureLowThresholdDegF_Type()
)
lgpEnvTemperatureLowThresholdDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureSetPointDegF_Type = Integer32
_LgpEnvTemperatureSetPointDegF_Object = MibTableColumn
lgpEnvTemperatureSetPointDegF = _LgpEnvTemperatureSetPointDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 6),
    _LgpEnvTemperatureSetPointDegF_Type()
)
lgpEnvTemperatureSetPointDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureDailyHighDegF_Type = Integer32
_LgpEnvTemperatureDailyHighDegF_Object = MibTableColumn
lgpEnvTemperatureDailyHighDegF = _LgpEnvTemperatureDailyHighDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 7),
    _LgpEnvTemperatureDailyHighDegF_Type()
)
lgpEnvTemperatureDailyHighDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureDailyLowDegF_Type = Integer32
_LgpEnvTemperatureDailyLowDegF_Object = MibTableColumn
lgpEnvTemperatureDailyLowDegF = _LgpEnvTemperatureDailyLowDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 8),
    _LgpEnvTemperatureDailyLowDegF_Type()
)
lgpEnvTemperatureDailyLowDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegF.setUnits("degrees Fahrenheit")


class _LgpEnvTempDailyHighTimeHourDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeHourDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyHighTimeHourDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeHourDegF_Object = MibTableColumn
lgpEnvTempDailyHighTimeHourDegF = _LgpEnvTempDailyHighTimeHourDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 9),
    _LgpEnvTempDailyHighTimeHourDegF_Type()
)
lgpEnvTempDailyHighTimeHourDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegF.setUnits("hours")


class _LgpEnvTempDailyHighTimeMinuteDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeMinuteDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeMinuteDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeMinuteDegF_Object = MibTableColumn
lgpEnvTempDailyHighTimeMinuteDegF = _LgpEnvTempDailyHighTimeMinuteDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 10),
    _LgpEnvTempDailyHighTimeMinuteDegF_Type()
)
lgpEnvTempDailyHighTimeMinuteDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegF.setUnits("minutes")


class _LgpEnvTempDailyHighTimeSecondDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeSecondDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeSecondDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeSecondDegF_Object = MibTableColumn
lgpEnvTempDailyHighTimeSecondDegF = _LgpEnvTempDailyHighTimeSecondDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 11),
    _LgpEnvTempDailyHighTimeSecondDegF_Type()
)
lgpEnvTempDailyHighTimeSecondDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegF.setUnits("seconds")


class _LgpEnvTempDailyLowTimeHourDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeHourDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyLowTimeHourDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeHourDegF_Object = MibTableColumn
lgpEnvTempDailyLowTimeHourDegF = _LgpEnvTempDailyLowTimeHourDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 12),
    _LgpEnvTempDailyLowTimeHourDegF_Type()
)
lgpEnvTempDailyLowTimeHourDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegF.setUnits("hours")


class _LgpEnvTempDailyLowTimeMinuteDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeMinuteDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeMinuteDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeMinuteDegF_Object = MibTableColumn
lgpEnvTempDailyLowTimeMinuteDegF = _LgpEnvTempDailyLowTimeMinuteDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 13),
    _LgpEnvTempDailyLowTimeMinuteDegF_Type()
)
lgpEnvTempDailyLowTimeMinuteDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegF.setUnits("minutes")


class _LgpEnvTempDailyLowTimeSecondDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeSecondDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeSecondDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeSecondDegF_Object = MibTableColumn
lgpEnvTempDailyLowTimeSecondDegF = _LgpEnvTempDailyLowTimeSecondDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 14),
    _LgpEnvTempDailyLowTimeSecondDegF_Type()
)
lgpEnvTempDailyLowTimeSecondDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegF.setUnits("seconds")
_LgpEnvTemperatureMeasurementTenthsDegF_Type = Integer32
_LgpEnvTemperatureMeasurementTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureMeasurementTenthsDegF = _LgpEnvTemperatureMeasurementTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 50),
    _LgpEnvTemperatureMeasurementTenthsDegF_Type()
)
lgpEnvTemperatureMeasurementTenthsDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureHighThresholdTenthsDegF_Type = Integer32
_LgpEnvTemperatureHighThresholdTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureHighThresholdTenthsDegF = _LgpEnvTemperatureHighThresholdTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 51),
    _LgpEnvTemperatureHighThresholdTenthsDegF_Type()
)
lgpEnvTemperatureHighThresholdTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureLowThresholdTenthsDegF_Type = Integer32
_LgpEnvTemperatureLowThresholdTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureLowThresholdTenthsDegF = _LgpEnvTemperatureLowThresholdTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 52),
    _LgpEnvTemperatureLowThresholdTenthsDegF_Type()
)
lgpEnvTemperatureLowThresholdTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureSetPointTenthsDegF_Type = Integer32
_LgpEnvTemperatureSetPointTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureSetPointTenthsDegF = _LgpEnvTemperatureSetPointTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 53),
    _LgpEnvTemperatureSetPointTenthsDegF_Type()
)
lgpEnvTemperatureSetPointTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureDeadBandTenthsDegF_Type = Integer32
_LgpEnvTemperatureDeadBandTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureDeadBandTenthsDegF = _LgpEnvTemperatureDeadBandTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 60),
    _LgpEnvTemperatureDeadBandTenthsDegF_Type()
)
lgpEnvTemperatureDeadBandTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTempHeatingPropBandTenthsDegF_Type = Integer32
_LgpEnvTempHeatingPropBandTenthsDegF_Object = MibTableColumn
lgpEnvTempHeatingPropBandTenthsDegF = _LgpEnvTempHeatingPropBandTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 61),
    _LgpEnvTempHeatingPropBandTenthsDegF_Type()
)
lgpEnvTempHeatingPropBandTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTempCoolingPropBandTenthsDegF_Type = Integer32
_LgpEnvTempCoolingPropBandTenthsDegF_Object = MibTableColumn
lgpEnvTempCoolingPropBandTenthsDegF = _LgpEnvTempCoolingPropBandTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 62),
    _LgpEnvTempCoolingPropBandTenthsDegF_Type()
)
lgpEnvTempCoolingPropBandTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureDeadbandRangeDegF_Type = Integer32
_LgpEnvTemperatureDeadbandRangeDegF_Object = MibScalar
lgpEnvTemperatureDeadbandRangeDegF = _LgpEnvTemperatureDeadbandRangeDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 4),
    _LgpEnvTemperatureDeadbandRangeDegF_Type()
)
lgpEnvTemperatureDeadbandRangeDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureCelsius_ObjectIdentity = ObjectIdentity
lgpEnvTemperatureCelsius = _LgpEnvTemperatureCelsius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureCelsius.setStatus("current")
_LgpEnvTemperatureSettingDegC_Type = Integer32
_LgpEnvTemperatureSettingDegC_Object = MibScalar
lgpEnvTemperatureSettingDegC = _LgpEnvTemperatureSettingDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 1),
    _LgpEnvTemperatureSettingDegC_Type()
)
lgpEnvTemperatureSettingDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureToleranceDegC_Type = Integer32
_LgpEnvTemperatureToleranceDegC_Object = MibScalar
lgpEnvTemperatureToleranceDegC = _LgpEnvTemperatureToleranceDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 2),
    _LgpEnvTemperatureToleranceDegC_Type()
)
lgpEnvTemperatureToleranceDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegC.setUnits("0.1 degrees Celsius")
_LgpEnvTemperatureTableDegC_Object = MibTable
lgpEnvTemperatureTableDegC = _LgpEnvTemperatureTableDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureTableDegC.setStatus("current")
_LgpEnvTemperatureEntryDegC_Object = MibTableRow
lgpEnvTemperatureEntryDegC = _LgpEnvTemperatureEntryDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1)
)
lgpEnvTemperatureEntryDegC.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvTemperatureIdDegC"),
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureEntryDegC.setStatus("current")
_LgpEnvTemperatureIdDegC_Type = Unsigned32
_LgpEnvTemperatureIdDegC_Object = MibTableColumn
lgpEnvTemperatureIdDegC = _LgpEnvTemperatureIdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 1),
    _LgpEnvTemperatureIdDegC_Type()
)
lgpEnvTemperatureIdDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureIdDegC.setStatus("current")
_LgpEnvTemperatureDescrDegC_Type = ObjectIdentifier
_LgpEnvTemperatureDescrDegC_Object = MibTableColumn
lgpEnvTemperatureDescrDegC = _LgpEnvTemperatureDescrDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 2),
    _LgpEnvTemperatureDescrDegC_Type()
)
lgpEnvTemperatureDescrDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDescrDegC.setStatus("current")
_LgpEnvTemperatureMeasurementDegC_Type = Integer32
_LgpEnvTemperatureMeasurementDegC_Object = MibTableColumn
lgpEnvTemperatureMeasurementDegC = _LgpEnvTemperatureMeasurementDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 3),
    _LgpEnvTemperatureMeasurementDegC_Type()
)
lgpEnvTemperatureMeasurementDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureHighThresholdDegC_Type = Integer32
_LgpEnvTemperatureHighThresholdDegC_Object = MibTableColumn
lgpEnvTemperatureHighThresholdDegC = _LgpEnvTemperatureHighThresholdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 4),
    _LgpEnvTemperatureHighThresholdDegC_Type()
)
lgpEnvTemperatureHighThresholdDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureLowThresholdDegC_Type = Integer32
_LgpEnvTemperatureLowThresholdDegC_Object = MibTableColumn
lgpEnvTemperatureLowThresholdDegC = _LgpEnvTemperatureLowThresholdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 5),
    _LgpEnvTemperatureLowThresholdDegC_Type()
)
lgpEnvTemperatureLowThresholdDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureSetPointDegC_Type = Integer32
_LgpEnvTemperatureSetPointDegC_Object = MibTableColumn
lgpEnvTemperatureSetPointDegC = _LgpEnvTemperatureSetPointDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 6),
    _LgpEnvTemperatureSetPointDegC_Type()
)
lgpEnvTemperatureSetPointDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureDailyHighDegC_Type = Integer32
_LgpEnvTemperatureDailyHighDegC_Object = MibTableColumn
lgpEnvTemperatureDailyHighDegC = _LgpEnvTemperatureDailyHighDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 7),
    _LgpEnvTemperatureDailyHighDegC_Type()
)
lgpEnvTemperatureDailyHighDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureDailyLowDegC_Type = Integer32
_LgpEnvTemperatureDailyLowDegC_Object = MibTableColumn
lgpEnvTemperatureDailyLowDegC = _LgpEnvTemperatureDailyLowDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 8),
    _LgpEnvTemperatureDailyLowDegC_Type()
)
lgpEnvTemperatureDailyLowDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegC.setUnits("degrees Celsius")


class _LgpEnvTempDailyHighTimeHourDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeHourDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyHighTimeHourDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeHourDegC_Object = MibTableColumn
lgpEnvTempDailyHighTimeHourDegC = _LgpEnvTempDailyHighTimeHourDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 9),
    _LgpEnvTempDailyHighTimeHourDegC_Type()
)
lgpEnvTempDailyHighTimeHourDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegC.setUnits("hours")


class _LgpEnvTempDailyHighTimeMinuteDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeMinuteDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeMinuteDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeMinuteDegC_Object = MibTableColumn
lgpEnvTempDailyHighTimeMinuteDegC = _LgpEnvTempDailyHighTimeMinuteDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 10),
    _LgpEnvTempDailyHighTimeMinuteDegC_Type()
)
lgpEnvTempDailyHighTimeMinuteDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegC.setUnits("minutes")


class _LgpEnvTempDailyHighTimeSecondDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeSecondDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeSecondDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeSecondDegC_Object = MibTableColumn
lgpEnvTempDailyHighTimeSecondDegC = _LgpEnvTempDailyHighTimeSecondDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 11),
    _LgpEnvTempDailyHighTimeSecondDegC_Type()
)
lgpEnvTempDailyHighTimeSecondDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegC.setUnits("seconds")


class _LgpEnvTempDailyLowTimeHourDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeHourDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyLowTimeHourDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeHourDegC_Object = MibTableColumn
lgpEnvTempDailyLowTimeHourDegC = _LgpEnvTempDailyLowTimeHourDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 12),
    _LgpEnvTempDailyLowTimeHourDegC_Type()
)
lgpEnvTempDailyLowTimeHourDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegC.setUnits("hours")


class _LgpEnvTempDailyLowTimeMinuteDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeMinuteDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeMinuteDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeMinuteDegC_Object = MibTableColumn
lgpEnvTempDailyLowTimeMinuteDegC = _LgpEnvTempDailyLowTimeMinuteDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 13),
    _LgpEnvTempDailyLowTimeMinuteDegC_Type()
)
lgpEnvTempDailyLowTimeMinuteDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegC.setUnits("minutes")


class _LgpEnvTempDailyLowTimeSecondDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeSecondDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeSecondDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeSecondDegC_Object = MibTableColumn
lgpEnvTempDailyLowTimeSecondDegC = _LgpEnvTempDailyLowTimeSecondDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 14),
    _LgpEnvTempDailyLowTimeSecondDegC_Type()
)
lgpEnvTempDailyLowTimeSecondDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegC.setUnits("seconds")
_LgpEnvTemperatureMeasurementTenthsDegC_Type = Integer32
_LgpEnvTemperatureMeasurementTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureMeasurementTenthsDegC = _LgpEnvTemperatureMeasurementTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 50),
    _LgpEnvTemperatureMeasurementTenthsDegC_Type()
)
lgpEnvTemperatureMeasurementTenthsDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureHighThresholdTenthsDegC_Type = Integer32
_LgpEnvTemperatureHighThresholdTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureHighThresholdTenthsDegC = _LgpEnvTemperatureHighThresholdTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 51),
    _LgpEnvTemperatureHighThresholdTenthsDegC_Type()
)
lgpEnvTemperatureHighThresholdTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureLowThresholdTenthsDegC_Type = Integer32
_LgpEnvTemperatureLowThresholdTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureLowThresholdTenthsDegC = _LgpEnvTemperatureLowThresholdTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 52),
    _LgpEnvTemperatureLowThresholdTenthsDegC_Type()
)
lgpEnvTemperatureLowThresholdTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureSetPointTenthsDegC_Type = Integer32
_LgpEnvTemperatureSetPointTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureSetPointTenthsDegC = _LgpEnvTemperatureSetPointTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 53),
    _LgpEnvTemperatureSetPointTenthsDegC_Type()
)
lgpEnvTemperatureSetPointTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureDeadBandTenthsDegC_Type = Integer32
_LgpEnvTemperatureDeadBandTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureDeadBandTenthsDegC = _LgpEnvTemperatureDeadBandTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 60),
    _LgpEnvTemperatureDeadBandTenthsDegC_Type()
)
lgpEnvTemperatureDeadBandTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTempHeatingPropBandTenthsDegC_Type = Integer32
_LgpEnvTempHeatingPropBandTenthsDegC_Object = MibTableColumn
lgpEnvTempHeatingPropBandTenthsDegC = _LgpEnvTempHeatingPropBandTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 61),
    _LgpEnvTempHeatingPropBandTenthsDegC_Type()
)
lgpEnvTempHeatingPropBandTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTempCoolingPropBandTenthsDegC_Type = Integer32
_LgpEnvTempCoolingPropBandTenthsDegC_Object = MibTableColumn
lgpEnvTempCoolingPropBandTenthsDegC = _LgpEnvTempCoolingPropBandTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 62),
    _LgpEnvTempCoolingPropBandTenthsDegC_Type()
)
lgpEnvTempCoolingPropBandTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureDeadbandRangeDegC_Type = Integer32
_LgpEnvTemperatureDeadbandRangeDegC_Object = MibScalar
lgpEnvTemperatureDeadbandRangeDegC = _LgpEnvTemperatureDeadbandRangeDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 4),
    _LgpEnvTemperatureDeadbandRangeDegC_Type()
)
lgpEnvTemperatureDeadbandRangeDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureControlMode_Type = ObjectIdentifier
_LgpEnvTemperatureControlMode_Object = MibScalar
lgpEnvTemperatureControlMode = _LgpEnvTemperatureControlMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 4),
    _LgpEnvTemperatureControlMode_Type()
)
lgpEnvTemperatureControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureControlMode.setStatus("current")
_LgpEnvHumidity_ObjectIdentity = ObjectIdentity
lgpEnvHumidity = _LgpEnvHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2)
)
if mibBuilder.loadTexts:
    lgpEnvHumidity.setStatus("current")
_LgpEnvHumidityWellKnown_ObjectIdentity = ObjectIdentity
lgpEnvHumidityWellKnown = _LgpEnvHumidityWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lgpEnvHumidityWellKnown.setStatus("current")
_LgpEnvControlHumidity_ObjectIdentity = ObjectIdentity
lgpEnvControlHumidity = _LgpEnvControlHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvControlHumidity.setStatus("current")
_LgpEnvReturnAirHumidity_ObjectIdentity = ObjectIdentity
lgpEnvReturnAirHumidity = _LgpEnvReturnAirHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvReturnAirHumidity.setStatus("current")
_LgpEnvSupplyAirHumidity_ObjectIdentity = ObjectIdentity
lgpEnvSupplyAirHumidity = _LgpEnvSupplyAirHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyAirHumidity.setStatus("current")
_LgpEnvValueAmbientHumidity_ObjectIdentity = ObjectIdentity
lgpEnvValueAmbientHumidity = _LgpEnvValueAmbientHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lgpEnvValueAmbientHumidity.setStatus("current")
_LgpEnvHumidityRelative_ObjectIdentity = ObjectIdentity
lgpEnvHumidityRelative = _LgpEnvHumidityRelative_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    lgpEnvHumidityRelative.setStatus("current")
_LgpEnvHumiditySettingRel_Type = Integer32
_LgpEnvHumiditySettingRel_Object = MibScalar
lgpEnvHumiditySettingRel = _LgpEnvHumiditySettingRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 1),
    _LgpEnvHumiditySettingRel_Type()
)
lgpEnvHumiditySettingRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumiditySettingRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumiditySettingRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityToleranceRel_Type = Integer32
_LgpEnvHumidityToleranceRel_Object = MibScalar
lgpEnvHumidityToleranceRel = _LgpEnvHumidityToleranceRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 2),
    _LgpEnvHumidityToleranceRel_Type()
)
lgpEnvHumidityToleranceRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityToleranceRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityToleranceRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityTableRel_Object = MibTable
lgpEnvHumidityTableRel = _LgpEnvHumidityTableRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    lgpEnvHumidityTableRel.setStatus("current")
_LgpEnvHumidityEntryRel_Object = MibTableRow
lgpEnvHumidityEntryRel = _LgpEnvHumidityEntryRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1)
)
lgpEnvHumidityEntryRel.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvHumidityIdRel"),
)
if mibBuilder.loadTexts:
    lgpEnvHumidityEntryRel.setStatus("current")
_LgpEnvHumidityIdRel_Type = Unsigned32
_LgpEnvHumidityIdRel_Object = MibTableColumn
lgpEnvHumidityIdRel = _LgpEnvHumidityIdRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 1),
    _LgpEnvHumidityIdRel_Type()
)
lgpEnvHumidityIdRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityIdRel.setStatus("current")
_LgpEnvHumidityDescrRel_Type = ObjectIdentifier
_LgpEnvHumidityDescrRel_Object = MibTableColumn
lgpEnvHumidityDescrRel = _LgpEnvHumidityDescrRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 2),
    _LgpEnvHumidityDescrRel_Type()
)
lgpEnvHumidityDescrRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDescrRel.setStatus("current")
_LgpEnvHumidityMeasurementRel_Type = Integer32
_LgpEnvHumidityMeasurementRel_Object = MibTableColumn
lgpEnvHumidityMeasurementRel = _LgpEnvHumidityMeasurementRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 3),
    _LgpEnvHumidityMeasurementRel_Type()
)
lgpEnvHumidityMeasurementRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityHighThresholdRel_Type = Integer32
_LgpEnvHumidityHighThresholdRel_Object = MibTableColumn
lgpEnvHumidityHighThresholdRel = _LgpEnvHumidityHighThresholdRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 4),
    _LgpEnvHumidityHighThresholdRel_Type()
)
lgpEnvHumidityHighThresholdRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityLowThresholdRel_Type = Integer32
_LgpEnvHumidityLowThresholdRel_Object = MibTableColumn
lgpEnvHumidityLowThresholdRel = _LgpEnvHumidityLowThresholdRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 5),
    _LgpEnvHumidityLowThresholdRel_Type()
)
lgpEnvHumidityLowThresholdRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRel.setUnits("percent Relative Humidity")
_LgpEnvHumiditySetPoint_Type = Integer32
_LgpEnvHumiditySetPoint_Object = MibTableColumn
lgpEnvHumiditySetPoint = _LgpEnvHumiditySetPoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 6),
    _LgpEnvHumiditySetPoint_Type()
)
lgpEnvHumiditySetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumiditySetPoint.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumiditySetPoint.setUnits("percent Relative Humidity")
_LgpEnvHumidityDailyHigh_Type = Integer32
_LgpEnvHumidityDailyHigh_Object = MibTableColumn
lgpEnvHumidityDailyHigh = _LgpEnvHumidityDailyHigh_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 7),
    _LgpEnvHumidityDailyHigh_Type()
)
lgpEnvHumidityDailyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHigh.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHigh.setUnits("percent Relative Humidity")
_LgpEnvHumidityDailyLow_Type = Integer32
_LgpEnvHumidityDailyLow_Object = MibTableColumn
lgpEnvHumidityDailyLow = _LgpEnvHumidityDailyLow_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 8),
    _LgpEnvHumidityDailyLow_Type()
)
lgpEnvHumidityDailyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLow.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLow.setUnits("percent Relative Humidity")


class _LgpEnvHumidityDailyHighTimeHour_Type(Integer32):
    """Custom type lgpEnvHumidityDailyHighTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvHumidityDailyHighTimeHour_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyHighTimeHour_Object = MibTableColumn
lgpEnvHumidityDailyHighTimeHour = _LgpEnvHumidityDailyHighTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 9),
    _LgpEnvHumidityDailyHighTimeHour_Type()
)
lgpEnvHumidityDailyHighTimeHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeHour.setUnits("hours")


class _LgpEnvHumidityDailyHighTimeMinute_Type(Integer32):
    """Custom type lgpEnvHumidityDailyHighTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyHighTimeMinute_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyHighTimeMinute_Object = MibTableColumn
lgpEnvHumidityDailyHighTimeMinute = _LgpEnvHumidityDailyHighTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 10),
    _LgpEnvHumidityDailyHighTimeMinute_Type()
)
lgpEnvHumidityDailyHighTimeMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeMinute.setUnits("minutes")


class _LgpEnvHumidityDailyHighTimeSecond_Type(Integer32):
    """Custom type lgpEnvHumidityDailyHighTimeSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyHighTimeSecond_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyHighTimeSecond_Object = MibTableColumn
lgpEnvHumidityDailyHighTimeSecond = _LgpEnvHumidityDailyHighTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 11),
    _LgpEnvHumidityDailyHighTimeSecond_Type()
)
lgpEnvHumidityDailyHighTimeSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeSecond.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeSecond.setUnits("seconds")


class _LgpEnvHumidityDailyLowTimeHour_Type(Integer32):
    """Custom type lgpEnvHumidityDailyLowTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvHumidityDailyLowTimeHour_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyLowTimeHour_Object = MibTableColumn
lgpEnvHumidityDailyLowTimeHour = _LgpEnvHumidityDailyLowTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 12),
    _LgpEnvHumidityDailyLowTimeHour_Type()
)
lgpEnvHumidityDailyLowTimeHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeHour.setUnits("hours")


class _LgpEnvHumidityDailyLowTimeMinute_Type(Integer32):
    """Custom type lgpEnvHumidityDailyLowTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyLowTimeMinute_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyLowTimeMinute_Object = MibTableColumn
lgpEnvHumidityDailyLowTimeMinute = _LgpEnvHumidityDailyLowTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 13),
    _LgpEnvHumidityDailyLowTimeMinute_Type()
)
lgpEnvHumidityDailyLowTimeMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeMinute.setUnits("minutes")


class _LgpEnvHumidityDailyLowTimeSecond_Type(Integer32):
    """Custom type lgpEnvHumidityDailyLowTimeSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyLowTimeSecond_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyLowTimeSecond_Object = MibTableColumn
lgpEnvHumidityDailyLowTimeSecond = _LgpEnvHumidityDailyLowTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 14),
    _LgpEnvHumidityDailyLowTimeSecond_Type()
)
lgpEnvHumidityDailyLowTimeSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeSecond.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeSecond.setUnits("seconds")
_LgpEnvHumidityDeadBand_Type = Integer32
_LgpEnvHumidityDeadBand_Object = MibTableColumn
lgpEnvHumidityDeadBand = _LgpEnvHumidityDeadBand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 15),
    _LgpEnvHumidityDeadBand_Type()
)
lgpEnvHumidityDeadBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadBand.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadBand.setUnits("percent Relative Humidity")
_LgpEnvHumidifyPropBand_Type = Integer32
_LgpEnvHumidifyPropBand_Object = MibTableColumn
lgpEnvHumidifyPropBand = _LgpEnvHumidifyPropBand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 16),
    _LgpEnvHumidifyPropBand_Type()
)
lgpEnvHumidifyPropBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidifyPropBand.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidifyPropBand.setUnits("percent Relative Humidity")
_LgpEnvDehumidifyPropBand_Type = Integer32
_LgpEnvDehumidifyPropBand_Object = MibTableColumn
lgpEnvDehumidifyPropBand = _LgpEnvDehumidifyPropBand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 17),
    _LgpEnvDehumidifyPropBand_Type()
)
lgpEnvDehumidifyPropBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvDehumidifyPropBand.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvDehumidifyPropBand.setUnits("percent Relative Humidity")
_LgpEnvHumidityMeasurementRelTenths_Type = Integer32
_LgpEnvHumidityMeasurementRelTenths_Object = MibTableColumn
lgpEnvHumidityMeasurementRelTenths = _LgpEnvHumidityMeasurementRelTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 50),
    _LgpEnvHumidityMeasurementRelTenths_Type()
)
lgpEnvHumidityMeasurementRelTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRelTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRelTenths.setUnits(".1 percent Relative Humidity")
_LgpEnvHumidityHighThresholdRelTenths_Type = Integer32
_LgpEnvHumidityHighThresholdRelTenths_Object = MibTableColumn
lgpEnvHumidityHighThresholdRelTenths = _LgpEnvHumidityHighThresholdRelTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 51),
    _LgpEnvHumidityHighThresholdRelTenths_Type()
)
lgpEnvHumidityHighThresholdRelTenths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRelTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRelTenths.setUnits(".1 percent Relative Humidity")
_LgpEnvHumidityLowThresholdRelTenths_Type = Integer32
_LgpEnvHumidityLowThresholdRelTenths_Object = MibTableColumn
lgpEnvHumidityLowThresholdRelTenths = _LgpEnvHumidityLowThresholdRelTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 52),
    _LgpEnvHumidityLowThresholdRelTenths_Type()
)
lgpEnvHumidityLowThresholdRelTenths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRelTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRelTenths.setUnits(".1 percent Relative Humidity")
_LgpEnvHumidityDeadbandRange_Type = Integer32
_LgpEnvHumidityDeadbandRange_Object = MibScalar
lgpEnvHumidityDeadbandRange = _LgpEnvHumidityDeadbandRange_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 4),
    _LgpEnvHumidityDeadbandRange_Type()
)
lgpEnvHumidityDeadbandRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadbandRange.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadbandRange.setUnits(".1 percent RH")
_LgpEnvState_ObjectIdentity = ObjectIdentity
lgpEnvState = _LgpEnvState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3)
)
if mibBuilder.loadTexts:
    lgpEnvState.setStatus("current")


class _LgpEnvStateSystem_Type(Integer32):
    """Custom type lgpEnvStateSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("standby", 3))
    )


_LgpEnvStateSystem_Type.__name__ = "Integer32"
_LgpEnvStateSystem_Object = MibScalar
lgpEnvStateSystem = _LgpEnvStateSystem_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 1),
    _LgpEnvStateSystem_Type()
)
lgpEnvStateSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateSystem.setStatus("current")


class _LgpEnvStateCooling_Type(Integer32):
    """Custom type lgpEnvStateCooling based on Integer32"""
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


_LgpEnvStateCooling_Type.__name__ = "Integer32"
_LgpEnvStateCooling_Object = MibScalar
lgpEnvStateCooling = _LgpEnvStateCooling_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 2),
    _LgpEnvStateCooling_Type()
)
lgpEnvStateCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCooling.setStatus("current")


class _LgpEnvStateHeating_Type(Integer32):
    """Custom type lgpEnvStateHeating based on Integer32"""
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


_LgpEnvStateHeating_Type.__name__ = "Integer32"
_LgpEnvStateHeating_Object = MibScalar
lgpEnvStateHeating = _LgpEnvStateHeating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 3),
    _LgpEnvStateHeating_Type()
)
lgpEnvStateHeating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeating.setStatus("current")


class _LgpEnvStateHumidifying_Type(Integer32):
    """Custom type lgpEnvStateHumidifying based on Integer32"""
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


_LgpEnvStateHumidifying_Type.__name__ = "Integer32"
_LgpEnvStateHumidifying_Object = MibScalar
lgpEnvStateHumidifying = _LgpEnvStateHumidifying_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 4),
    _LgpEnvStateHumidifying_Type()
)
lgpEnvStateHumidifying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHumidifying.setStatus("current")


class _LgpEnvStateDehumidifying_Type(Integer32):
    """Custom type lgpEnvStateDehumidifying based on Integer32"""
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


_LgpEnvStateDehumidifying_Type.__name__ = "Integer32"
_LgpEnvStateDehumidifying_Object = MibScalar
lgpEnvStateDehumidifying = _LgpEnvStateDehumidifying_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 5),
    _LgpEnvStateDehumidifying_Type()
)
lgpEnvStateDehumidifying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateDehumidifying.setStatus("current")


class _LgpEnvStateEconoCycle_Type(Integer32):
    """Custom type lgpEnvStateEconoCycle based on Integer32"""
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


_LgpEnvStateEconoCycle_Type.__name__ = "Integer32"
_LgpEnvStateEconoCycle_Object = MibScalar
lgpEnvStateEconoCycle = _LgpEnvStateEconoCycle_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 6),
    _LgpEnvStateEconoCycle_Type()
)
lgpEnvStateEconoCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateEconoCycle.setStatus("current")


class _LgpEnvStateFan_Type(Integer32):
    """Custom type lgpEnvStateFan based on Integer32"""
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


_LgpEnvStateFan_Type.__name__ = "Integer32"
_LgpEnvStateFan_Object = MibScalar
lgpEnvStateFan = _LgpEnvStateFan_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 7),
    _LgpEnvStateFan_Type()
)
lgpEnvStateFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFan.setStatus("current")


class _LgpEnvStateGeneralAlarmOutput_Type(Integer32):
    """Custom type lgpEnvStateGeneralAlarmOutput based on Integer32"""
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


_LgpEnvStateGeneralAlarmOutput_Type.__name__ = "Integer32"
_LgpEnvStateGeneralAlarmOutput_Object = MibScalar
lgpEnvStateGeneralAlarmOutput = _LgpEnvStateGeneralAlarmOutput_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 8),
    _LgpEnvStateGeneralAlarmOutput_Type()
)
lgpEnvStateGeneralAlarmOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateGeneralAlarmOutput.setStatus("current")
_LgpEnvStateCoolingCapacity_Type = Unsigned32
_LgpEnvStateCoolingCapacity_Object = MibScalar
lgpEnvStateCoolingCapacity = _LgpEnvStateCoolingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 9),
    _LgpEnvStateCoolingCapacity_Type()
)
lgpEnvStateCoolingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingCapacity.setUnits("percent")
_LgpEnvStateHeatingCapacity_Type = Unsigned32
_LgpEnvStateHeatingCapacity_Object = MibScalar
lgpEnvStateHeatingCapacity = _LgpEnvStateHeatingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 10),
    _LgpEnvStateHeatingCapacity_Type()
)
lgpEnvStateHeatingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingCapacity.setUnits("percent")


class _LgpEnvStateAudibleAlarm_Type(Integer32):
    """Custom type lgpEnvStateAudibleAlarm based on Integer32"""
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


_LgpEnvStateAudibleAlarm_Type.__name__ = "Integer32"
_LgpEnvStateAudibleAlarm_Object = MibScalar
lgpEnvStateAudibleAlarm = _LgpEnvStateAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 11),
    _LgpEnvStateAudibleAlarm_Type()
)
lgpEnvStateAudibleAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateAudibleAlarm.setStatus("current")
_LgpEnvStateCoolingUnits_ObjectIdentity = ObjectIdentity
lgpEnvStateCoolingUnits = _LgpEnvStateCoolingUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12)
)
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnits.setStatus("current")


class _LgpEnvStateCoolingUnit1_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit1 based on Integer32"""
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


_LgpEnvStateCoolingUnit1_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit1_Object = MibScalar
lgpEnvStateCoolingUnit1 = _LgpEnvStateCoolingUnit1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 2),
    _LgpEnvStateCoolingUnit1_Type()
)
lgpEnvStateCoolingUnit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit1.setStatus("current")


class _LgpEnvStateCoolingUnit2_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit2 based on Integer32"""
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


_LgpEnvStateCoolingUnit2_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit2_Object = MibScalar
lgpEnvStateCoolingUnit2 = _LgpEnvStateCoolingUnit2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 3),
    _LgpEnvStateCoolingUnit2_Type()
)
lgpEnvStateCoolingUnit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit2.setStatus("current")


class _LgpEnvStateCoolingUnit3_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit3 based on Integer32"""
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


_LgpEnvStateCoolingUnit3_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit3_Object = MibScalar
lgpEnvStateCoolingUnit3 = _LgpEnvStateCoolingUnit3_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 4),
    _LgpEnvStateCoolingUnit3_Type()
)
lgpEnvStateCoolingUnit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit3.setStatus("current")


class _LgpEnvStateCoolingUnit4_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit4 based on Integer32"""
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


_LgpEnvStateCoolingUnit4_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit4_Object = MibScalar
lgpEnvStateCoolingUnit4 = _LgpEnvStateCoolingUnit4_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 5),
    _LgpEnvStateCoolingUnit4_Type()
)
lgpEnvStateCoolingUnit4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit4.setStatus("current")
_LgpEnvStateHeatingUnits_ObjectIdentity = ObjectIdentity
lgpEnvStateHeatingUnits = _LgpEnvStateHeatingUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13)
)
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnits.setStatus("current")


class _LgpEnvStateHeatingUnit1_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit1 based on Integer32"""
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


_LgpEnvStateHeatingUnit1_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit1_Object = MibScalar
lgpEnvStateHeatingUnit1 = _LgpEnvStateHeatingUnit1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 2),
    _LgpEnvStateHeatingUnit1_Type()
)
lgpEnvStateHeatingUnit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit1.setStatus("current")


class _LgpEnvStateHeatingUnit2_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit2 based on Integer32"""
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


_LgpEnvStateHeatingUnit2_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit2_Object = MibScalar
lgpEnvStateHeatingUnit2 = _LgpEnvStateHeatingUnit2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 3),
    _LgpEnvStateHeatingUnit2_Type()
)
lgpEnvStateHeatingUnit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit2.setStatus("current")


class _LgpEnvStateHeatingUnit3_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit3 based on Integer32"""
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


_LgpEnvStateHeatingUnit3_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit3_Object = MibScalar
lgpEnvStateHeatingUnit3 = _LgpEnvStateHeatingUnit3_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 4),
    _LgpEnvStateHeatingUnit3_Type()
)
lgpEnvStateHeatingUnit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit3.setStatus("current")


class _LgpEnvStateHeatingUnit4_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit4 based on Integer32"""
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


_LgpEnvStateHeatingUnit4_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit4_Object = MibScalar
lgpEnvStateHeatingUnit4 = _LgpEnvStateHeatingUnit4_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 5),
    _LgpEnvStateHeatingUnit4_Type()
)
lgpEnvStateHeatingUnit4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit4.setStatus("current")


class _LgpEnvStateOperatingReason_Type(Integer32):
    """Custom type lgpEnvStateOperatingReason based on Integer32"""
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
        *(("alarm", 3),
          ("externalDevice", 6),
          ("localDisplay", 7),
          ("localUser", 2),
          ("none", 1),
          ("remoteUser", 5),
          ("schedule", 4))
    )


_LgpEnvStateOperatingReason_Type.__name__ = "Integer32"
_LgpEnvStateOperatingReason_Object = MibScalar
lgpEnvStateOperatingReason = _LgpEnvStateOperatingReason_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 14),
    _LgpEnvStateOperatingReason_Type()
)
lgpEnvStateOperatingReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingReason.setStatus("current")


class _LgpEnvStateOperatingMode_Type(Integer32):
    """Custom type lgpEnvStateOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_LgpEnvStateOperatingMode_Type.__name__ = "Integer32"
_LgpEnvStateOperatingMode_Object = MibScalar
lgpEnvStateOperatingMode = _LgpEnvStateOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 15),
    _LgpEnvStateOperatingMode_Type()
)
lgpEnvStateOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingMode.setStatus("current")
_LgpEnvStateFanCapacity_Type = Unsigned32
_LgpEnvStateFanCapacity_Object = MibScalar
lgpEnvStateFanCapacity = _LgpEnvStateFanCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 16),
    _LgpEnvStateFanCapacity_Type()
)
lgpEnvStateFanCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFanCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateFanCapacity.setUnits("percent")
_LgpEnvStateFreeCoolingCapacity_Type = Unsigned32
_LgpEnvStateFreeCoolingCapacity_Object = MibScalar
lgpEnvStateFreeCoolingCapacity = _LgpEnvStateFreeCoolingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 17),
    _LgpEnvStateFreeCoolingCapacity_Type()
)
lgpEnvStateFreeCoolingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFreeCoolingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateFreeCoolingCapacity.setUnits("percent")
_LgpEnvStateDehumidifyingCapacity_Type = Unsigned32
_LgpEnvStateDehumidifyingCapacity_Object = MibScalar
lgpEnvStateDehumidifyingCapacity = _LgpEnvStateDehumidifyingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 18),
    _LgpEnvStateDehumidifyingCapacity_Type()
)
lgpEnvStateDehumidifyingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateDehumidifyingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateDehumidifyingCapacity.setUnits("percent")
_LgpEnvStateHumidifyingCapacity_Type = Unsigned32
_LgpEnvStateHumidifyingCapacity_Object = MibScalar
lgpEnvStateHumidifyingCapacity = _LgpEnvStateHumidifyingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 19),
    _LgpEnvStateHumidifyingCapacity_Type()
)
lgpEnvStateHumidifyingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHumidifyingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateHumidifyingCapacity.setUnits("percent")


class _LgpEnvStateFreeCooling_Type(Integer32):
    """Custom type lgpEnvStateFreeCooling based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("start", 3),
          ("unavailable", 4))
    )


_LgpEnvStateFreeCooling_Type.__name__ = "Integer32"
_LgpEnvStateFreeCooling_Object = MibScalar
lgpEnvStateFreeCooling = _LgpEnvStateFreeCooling_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 20),
    _LgpEnvStateFreeCooling_Type()
)
lgpEnvStateFreeCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFreeCooling.setStatus("current")


class _LgpEnvStateElectricHeater_Type(Integer32):
    """Custom type lgpEnvStateElectricHeater based on Integer32"""
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


_LgpEnvStateElectricHeater_Type.__name__ = "Integer32"
_LgpEnvStateElectricHeater_Object = MibScalar
lgpEnvStateElectricHeater = _LgpEnvStateElectricHeater_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 21),
    _LgpEnvStateElectricHeater_Type()
)
lgpEnvStateElectricHeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateElectricHeater.setStatus("current")


class _LgpEnvStateHotWater_Type(Integer32):
    """Custom type lgpEnvStateHotWater based on Integer32"""
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


_LgpEnvStateHotWater_Type.__name__ = "Integer32"
_LgpEnvStateHotWater_Object = MibScalar
lgpEnvStateHotWater = _LgpEnvStateHotWater_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 22),
    _LgpEnvStateHotWater_Type()
)
lgpEnvStateHotWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHotWater.setStatus("current")
_LgpEnvStateOperatingEfficiency_Type = Unsigned32
_LgpEnvStateOperatingEfficiency_Object = MibScalar
lgpEnvStateOperatingEfficiency = _LgpEnvStateOperatingEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 23),
    _LgpEnvStateOperatingEfficiency_Type()
)
lgpEnvStateOperatingEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingEfficiency.setUnits("percent")
_LgpEnvComponentStateTable_Object = MibTable
lgpEnvComponentStateTable = _LgpEnvComponentStateTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50)
)
if mibBuilder.loadTexts:
    lgpEnvComponentStateTable.setStatus("current")
_LgpEnvComponentStateEntry_Object = MibTableRow
lgpEnvComponentStateEntry = _LgpEnvComponentStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1)
)
lgpEnvComponentStateEntry.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvComponentStateIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvComponentStateEntry.setStatus("current")
_LgpEnvComponentStateIndex_Type = Unsigned32
_LgpEnvComponentStateIndex_Object = MibTableColumn
lgpEnvComponentStateIndex = _LgpEnvComponentStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1, 1),
    _LgpEnvComponentStateIndex_Type()
)
lgpEnvComponentStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvComponentStateIndex.setStatus("current")
_LgpEnvComponentStateDescr_Type = ObjectIdentifier
_LgpEnvComponentStateDescr_Object = MibTableColumn
lgpEnvComponentStateDescr = _LgpEnvComponentStateDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1, 2),
    _LgpEnvComponentStateDescr_Type()
)
lgpEnvComponentStateDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvComponentStateDescr.setStatus("current")


class _LgpEnvComponentState_Type(Integer32):
    """Custom type lgpEnvComponentState based on Integer32"""
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
          ("off", 2),
          ("on", 1))
    )


_LgpEnvComponentState_Type.__name__ = "Integer32"
_LgpEnvComponentState_Object = MibTableColumn
lgpEnvComponentState = _LgpEnvComponentState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1, 3),
    _LgpEnvComponentState_Type()
)
lgpEnvComponentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvComponentState.setStatus("current")
_LgpEnvValveTable_Object = MibTable
lgpEnvValveTable = _LgpEnvValveTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70)
)
if mibBuilder.loadTexts:
    lgpEnvValveTable.setStatus("current")
_LgpEnvValveEntry_Object = MibTableRow
lgpEnvValveEntry = _LgpEnvValveEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1)
)
lgpEnvValveEntry.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvValveIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvValveEntry.setStatus("current")
_LgpEnvValveIndex_Type = Unsigned32
_LgpEnvValveIndex_Object = MibTableColumn
lgpEnvValveIndex = _LgpEnvValveIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 1),
    _LgpEnvValveIndex_Type()
)
lgpEnvValveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvValveIndex.setStatus("current")
_LgpEnvValveDescr_Type = ObjectIdentifier
_LgpEnvValveDescr_Object = MibTableColumn
lgpEnvValveDescr = _LgpEnvValveDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 2),
    _LgpEnvValveDescr_Type()
)
lgpEnvValveDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvValveDescr.setStatus("current")


class _LgpEnvValveState_Type(Integer32):
    """Custom type lgpEnvValveState based on Integer32"""
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
          ("not-specified", 0),
          ("open", 1))
    )


_LgpEnvValveState_Type.__name__ = "Integer32"
_LgpEnvValveState_Object = MibTableColumn
lgpEnvValveState = _LgpEnvValveState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 3),
    _LgpEnvValveState_Type()
)
lgpEnvValveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvValveState.setStatus("current")
_LgpEnvValvePositionTenths_Type = Unsigned32
_LgpEnvValvePositionTenths_Object = MibTableColumn
lgpEnvValvePositionTenths = _LgpEnvValvePositionTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 20),
    _LgpEnvValvePositionTenths_Type()
)
lgpEnvValvePositionTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvValvePositionTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvValvePositionTenths.setUnits(".1 percent")
_LgpEnvConfig_ObjectIdentity = ObjectIdentity
lgpEnvConfig = _LgpEnvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4)
)
if mibBuilder.loadTexts:
    lgpEnvConfig.setStatus("current")


class _LgpEnvConfigReheatLockout_Type(Integer32):
    """Custom type lgpEnvConfigReheatLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigReheatLockout_Type.__name__ = "Integer32"
_LgpEnvConfigReheatLockout_Object = MibScalar
lgpEnvConfigReheatLockout = _LgpEnvConfigReheatLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 1),
    _LgpEnvConfigReheatLockout_Type()
)
lgpEnvConfigReheatLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigReheatLockout.setStatus("current")


class _LgpEnvConfigHumLockout_Type(Integer32):
    """Custom type lgpEnvConfigHumLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigHumLockout_Type.__name__ = "Integer32"
_LgpEnvConfigHumLockout_Object = MibScalar
lgpEnvConfigHumLockout = _LgpEnvConfigHumLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 2),
    _LgpEnvConfigHumLockout_Type()
)
lgpEnvConfigHumLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumLockout.setStatus("current")
_LgpEnvConfigRestartDelay_Type = Unsigned32
_LgpEnvConfigRestartDelay_Object = MibScalar
lgpEnvConfigRestartDelay = _LgpEnvConfigRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 4),
    _LgpEnvConfigRestartDelay_Type()
)
lgpEnvConfigRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigRestartDelay.setUnits("seconds")


class _LgpEnvConfigRemoteShutdown_Type(Integer32):
    """Custom type lgpEnvConfigRemoteShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigRemoteShutdown_Type.__name__ = "Integer32"
_LgpEnvConfigRemoteShutdown_Object = MibScalar
lgpEnvConfigRemoteShutdown = _LgpEnvConfigRemoteShutdown_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 7),
    _LgpEnvConfigRemoteShutdown_Type()
)
lgpEnvConfigRemoteShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigRemoteShutdown.setStatus("current")
_LgpEnvConfigCoolingServiceInterval_Type = Unsigned32
_LgpEnvConfigCoolingServiceInterval_Object = MibScalar
lgpEnvConfigCoolingServiceInterval = _LgpEnvConfigCoolingServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 8),
    _LgpEnvConfigCoolingServiceInterval_Type()
)
lgpEnvConfigCoolingServiceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigCoolingServiceInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigCoolingServiceInterval.setUnits("hours")
_LgpEnvConfigHumidifierServiceInterval_Type = Unsigned32
_LgpEnvConfigHumidifierServiceInterval_Object = MibScalar
lgpEnvConfigHumidifierServiceInterval = _LgpEnvConfigHumidifierServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 9),
    _LgpEnvConfigHumidifierServiceInterval_Type()
)
lgpEnvConfigHumidifierServiceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidifierServiceInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidifierServiceInterval.setUnits("hours")
_LgpEnvConfigFilterServiceInterval_Type = Unsigned32
_LgpEnvConfigFilterServiceInterval_Object = MibScalar
lgpEnvConfigFilterServiceInterval = _LgpEnvConfigFilterServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 10),
    _LgpEnvConfigFilterServiceInterval_Type()
)
lgpEnvConfigFilterServiceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFilterServiceInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFilterServiceInterval.setUnits("hours")
_LgpEnvConfigSleepModeDeadbandRangeDegC_Type = Integer32
_LgpEnvConfigSleepModeDeadbandRangeDegC_Object = MibScalar
lgpEnvConfigSleepModeDeadbandRangeDegC = _LgpEnvConfigSleepModeDeadbandRangeDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 11),
    _LgpEnvConfigSleepModeDeadbandRangeDegC_Type()
)
lgpEnvConfigSleepModeDeadbandRangeDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegC.setUnits(".1 degrees Celsius")
_LgpEnvConfigSleepModeDeadbandRangeDegF_Type = Integer32
_LgpEnvConfigSleepModeDeadbandRangeDegF_Object = MibScalar
lgpEnvConfigSleepModeDeadbandRangeDegF = _LgpEnvConfigSleepModeDeadbandRangeDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 12),
    _LgpEnvConfigSleepModeDeadbandRangeDegF_Type()
)
lgpEnvConfigSleepModeDeadbandRangeDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvConfigSupplyTempLowLimitDegF_Type = Integer32
_LgpEnvConfigSupplyTempLowLimitDegF_Object = MibScalar
lgpEnvConfigSupplyTempLowLimitDegF = _LgpEnvConfigSupplyTempLowLimitDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 13),
    _LgpEnvConfigSupplyTempLowLimitDegF_Type()
)
lgpEnvConfigSupplyTempLowLimitDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegF.setUnits("degrees Fahrenheit")
_LgpEnvConfigSupplyTempLowLimitDegC_Type = Integer32
_LgpEnvConfigSupplyTempLowLimitDegC_Object = MibScalar
lgpEnvConfigSupplyTempLowLimitDegC = _LgpEnvConfigSupplyTempLowLimitDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 14),
    _LgpEnvConfigSupplyTempLowLimitDegC_Type()
)
lgpEnvConfigSupplyTempLowLimitDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegC.setUnits("degrees Celsius")
_LgpEnvConfigTemperatureIntegTime_Type = Integer32
_LgpEnvConfigTemperatureIntegTime_Object = MibScalar
lgpEnvConfigTemperatureIntegTime = _LgpEnvConfigTemperatureIntegTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 15),
    _LgpEnvConfigTemperatureIntegTime_Type()
)
lgpEnvConfigTemperatureIntegTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigTemperatureIntegTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigTemperatureIntegTime.setUnits("minutes")


class _LgpEnvConfigLocalTemperatureUnit_Type(Integer32):
    """Custom type lgpEnvConfigLocalTemperatureUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("degC", 1),
          ("degF", 2))
    )


_LgpEnvConfigLocalTemperatureUnit_Type.__name__ = "Integer32"
_LgpEnvConfigLocalTemperatureUnit_Object = MibScalar
lgpEnvConfigLocalTemperatureUnit = _LgpEnvConfigLocalTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 16),
    _LgpEnvConfigLocalTemperatureUnit_Type()
)
lgpEnvConfigLocalTemperatureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigLocalTemperatureUnit.setStatus("current")


class _LgpEnvConfigSleepMode_Type(Integer32):
    """Custom type lgpEnvConfigSleepMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_LgpEnvConfigSleepMode_Type.__name__ = "Integer32"
_LgpEnvConfigSleepMode_Object = MibScalar
lgpEnvConfigSleepMode = _LgpEnvConfigSleepMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 17),
    _LgpEnvConfigSleepMode_Type()
)
lgpEnvConfigSleepMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepMode.setStatus("current")
_LgpEnvConfigHumidityIntegTime_Type = Integer32
_LgpEnvConfigHumidityIntegTime_Object = MibScalar
lgpEnvConfigHumidityIntegTime = _LgpEnvConfigHumidityIntegTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 18),
    _LgpEnvConfigHumidityIntegTime_Type()
)
lgpEnvConfigHumidityIntegTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidityIntegTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidityIntegTime.setUnits("minutes")
_LgpEnvConfigFreecoolingDeltaDegF_Type = Integer32
_LgpEnvConfigFreecoolingDeltaDegF_Object = MibScalar
lgpEnvConfigFreecoolingDeltaDegF = _LgpEnvConfigFreecoolingDeltaDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 19),
    _LgpEnvConfigFreecoolingDeltaDegF_Type()
)
lgpEnvConfigFreecoolingDeltaDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegF.setUnits("degrees Fahrenheit")
_LgpEnvConfigFreecoolingDeltaDegC_Type = Integer32
_LgpEnvConfigFreecoolingDeltaDegC_Object = MibScalar
lgpEnvConfigFreecoolingDeltaDegC = _LgpEnvConfigFreecoolingDeltaDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 20),
    _LgpEnvConfigFreecoolingDeltaDegC_Type()
)
lgpEnvConfigFreecoolingDeltaDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegC.setUnits("degrees Celsius")


class _LgpEnvConfigSupplyTempLowLimit_Type(Integer32):
    """Custom type lgpEnvConfigSupplyTempLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSupplyTempLowLimit_Type.__name__ = "Integer32"
_LgpEnvConfigSupplyTempLowLimit_Object = MibScalar
lgpEnvConfigSupplyTempLowLimit = _LgpEnvConfigSupplyTempLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 21),
    _LgpEnvConfigSupplyTempLowLimit_Type()
)
lgpEnvConfigSupplyTempLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimit.setStatus("current")


class _LgpEnvConfigSensorEventsStandard_Type(Integer32):
    """Custom type lgpEnvConfigSensorEventsStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSensorEventsStandard_Type.__name__ = "Integer32"
_LgpEnvConfigSensorEventsStandard_Object = MibScalar
lgpEnvConfigSensorEventsStandard = _LgpEnvConfigSensorEventsStandard_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 22),
    _LgpEnvConfigSensorEventsStandard_Type()
)
lgpEnvConfigSensorEventsStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSensorEventsStandard.setStatus("current")


class _LgpEnvConfigSensorEvents1_Type(Integer32):
    """Custom type lgpEnvConfigSensorEvents1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSensorEvents1_Type.__name__ = "Integer32"
_LgpEnvConfigSensorEvents1_Object = MibScalar
lgpEnvConfigSensorEvents1 = _LgpEnvConfigSensorEvents1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 23),
    _LgpEnvConfigSensorEvents1_Type()
)
lgpEnvConfigSensorEvents1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSensorEvents1.setStatus("current")


class _LgpEnvConfigSleepModeDeadbandRange_Type(Integer32):
    """Custom type lgpEnvConfigSleepModeDeadbandRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSleepModeDeadbandRange_Type.__name__ = "Integer32"
_LgpEnvConfigSleepModeDeadbandRange_Object = MibScalar
lgpEnvConfigSleepModeDeadbandRange = _LgpEnvConfigSleepModeDeadbandRange_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 24),
    _LgpEnvConfigSleepModeDeadbandRange_Type()
)
lgpEnvConfigSleepModeDeadbandRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRange.setStatus("current")


class _LgpEnvConfigAutoConfiguration_Type(Integer32):
    """Custom type lgpEnvConfigAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigAutoConfiguration_Type.__name__ = "Integer32"
_LgpEnvConfigAutoConfiguration_Object = MibScalar
lgpEnvConfigAutoConfiguration = _LgpEnvConfigAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 25),
    _LgpEnvConfigAutoConfiguration_Type()
)
lgpEnvConfigAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigAutoConfiguration.setStatus("current")


class _LgpEnvConfigDeltaGlycolType_Type(Integer32):
    """Custom type lgpEnvConfigDeltaGlycolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("contact", 2),
          ("disabled", 1),
          ("value", 3))
    )


_LgpEnvConfigDeltaGlycolType_Type.__name__ = "Integer32"
_LgpEnvConfigDeltaGlycolType_Object = MibScalar
lgpEnvConfigDeltaGlycolType = _LgpEnvConfigDeltaGlycolType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 26),
    _LgpEnvConfigDeltaGlycolType_Type()
)
lgpEnvConfigDeltaGlycolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigDeltaGlycolType.setStatus("current")


class _LgpEnvConfigChillWaterControl_Type(Integer32):
    """Custom type lgpEnvConfigChillWaterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigChillWaterControl_Type.__name__ = "Integer32"
_LgpEnvConfigChillWaterControl_Object = MibScalar
lgpEnvConfigChillWaterControl = _LgpEnvConfigChillWaterControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 27),
    _LgpEnvConfigChillWaterControl_Type()
)
lgpEnvConfigChillWaterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigChillWaterControl.setStatus("current")
_LgpEnvConfigInfaredFlushRate_Type = Unsigned32
_LgpEnvConfigInfaredFlushRate_Object = MibScalar
lgpEnvConfigInfaredFlushRate = _LgpEnvConfigInfaredFlushRate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 28),
    _LgpEnvConfigInfaredFlushRate_Type()
)
lgpEnvConfigInfaredFlushRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigInfaredFlushRate.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigInfaredFlushRate.setUnits("percent")


class _LgpEnvConfigHumidityControl_Type(Integer32):
    """Custom type lgpEnvConfigHumidityControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compensated", 2),
          ("predictive", 3),
          ("relative", 1))
    )


_LgpEnvConfigHumidityControl_Type.__name__ = "Integer32"
_LgpEnvConfigHumidityControl_Object = MibScalar
lgpEnvConfigHumidityControl = _LgpEnvConfigHumidityControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 29),
    _LgpEnvConfigHumidityControl_Type()
)
lgpEnvConfigHumidityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidityControl.setStatus("current")


class _LgpEnvConfigCompressorLockout_Type(Integer32):
    """Custom type lgpEnvConfigCompressorLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigCompressorLockout_Type.__name__ = "Integer32"
_LgpEnvConfigCompressorLockout_Object = MibScalar
lgpEnvConfigCompressorLockout = _LgpEnvConfigCompressorLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 30),
    _LgpEnvConfigCompressorLockout_Type()
)
lgpEnvConfigCompressorLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigCompressorLockout.setStatus("current")


class _LgpEnvConfigReheatAndHumidifierLockout_Type(Integer32):
    """Custom type lgpEnvConfigReheatAndHumidifierLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigReheatAndHumidifierLockout_Type.__name__ = "Integer32"
_LgpEnvConfigReheatAndHumidifierLockout_Object = MibScalar
lgpEnvConfigReheatAndHumidifierLockout = _LgpEnvConfigReheatAndHumidifierLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 31),
    _LgpEnvConfigReheatAndHumidifierLockout_Type()
)
lgpEnvConfigReheatAndHumidifierLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigReheatAndHumidifierLockout.setStatus("current")
_LgpEnvOperationalTimeTable_Object = MibTable
lgpEnvOperationalTimeTable = _LgpEnvOperationalTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32)
)
if mibBuilder.loadTexts:
    lgpEnvOperationalTimeTable.setStatus("current")
_LgpEnvOperationalTimeEntry_Object = MibTableRow
lgpEnvOperationalTimeEntry = _LgpEnvOperationalTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1)
)
lgpEnvOperationalTimeEntry.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvOperationTimeIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvOperationalTimeEntry.setStatus("current")
_LgpEnvOperationTimeIndex_Type = Unsigned32
_LgpEnvOperationTimeIndex_Object = MibTableColumn
lgpEnvOperationTimeIndex = _LgpEnvOperationTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 1),
    _LgpEnvOperationTimeIndex_Type()
)
lgpEnvOperationTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeIndex.setStatus("current")
_LgpEnvOperationTimePoint_Type = ObjectIdentifier
_LgpEnvOperationTimePoint_Object = MibTableColumn
lgpEnvOperationTimePoint = _LgpEnvOperationTimePoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 2),
    _LgpEnvOperationTimePoint_Type()
)
lgpEnvOperationTimePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvOperationTimePoint.setStatus("current")
_LgpEnvOperationTimeSubID_Type = Integer32
_LgpEnvOperationTimeSubID_Object = MibTableColumn
lgpEnvOperationTimeSubID = _LgpEnvOperationTimeSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 3),
    _LgpEnvOperationTimeSubID_Type()
)
lgpEnvOperationTimeSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeSubID.setStatus("current")
_LgpEnvOperationTimeUnit_Type = ObjectIdentifier
_LgpEnvOperationTimeUnit_Object = MibTableColumn
lgpEnvOperationTimeUnit = _LgpEnvOperationTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 4),
    _LgpEnvOperationTimeUnit_Type()
)
lgpEnvOperationTimeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeUnit.setStatus("current")
_LgpEnvOperationTimeValue_Type = Integer32
_LgpEnvOperationTimeValue_Object = MibTableColumn
lgpEnvOperationTimeValue = _LgpEnvOperationTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 5),
    _LgpEnvOperationTimeValue_Type()
)
lgpEnvOperationTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeValue.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeValue.setUnits("hours")
_LgpEnvOperationTimeHighWarning_Type = Integer32
_LgpEnvOperationTimeHighWarning_Object = MibTableColumn
lgpEnvOperationTimeHighWarning = _LgpEnvOperationTimeHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 6),
    _LgpEnvOperationTimeHighWarning_Type()
)
lgpEnvOperationTimeHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeHighWarning.setUnits("hours")


class _LgpEnvConfigTempControlAlgorithm_Type(Integer32):
    """Custom type lgpEnvConfigTempControlAlgorithm based on Integer32"""
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
        *(("intelligent", 3),
          ("pi", 1),
          ("pid", 2),
          ("proportional", 4))
    )


_LgpEnvConfigTempControlAlgorithm_Type.__name__ = "Integer32"
_LgpEnvConfigTempControlAlgorithm_Object = MibScalar
lgpEnvConfigTempControlAlgorithm = _LgpEnvConfigTempControlAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 33),
    _LgpEnvConfigTempControlAlgorithm_Type()
)
lgpEnvConfigTempControlAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigTempControlAlgorithm.setStatus("current")


class _LgpEnvConfigFanSpeedMode_Type(Integer32):
    """Custom type lgpEnvConfigFanSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1))
    )


_LgpEnvConfigFanSpeedMode_Type.__name__ = "Integer32"
_LgpEnvConfigFanSpeedMode_Object = MibScalar
lgpEnvConfigFanSpeedMode = _LgpEnvConfigFanSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 34),
    _LgpEnvConfigFanSpeedMode_Type()
)
lgpEnvConfigFanSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedMode.setStatus("current")
_LgpEnvConfigFanSpeedCapacity_Type = Unsigned32
_LgpEnvConfigFanSpeedCapacity_Object = MibScalar
lgpEnvConfigFanSpeedCapacity = _LgpEnvConfigFanSpeedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 35),
    _LgpEnvConfigFanSpeedCapacity_Type()
)
lgpEnvConfigFanSpeedCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedCapacity.setUnits("percent")
_LgpEnvConfigBmsResetTimer_Type = Unsigned32
_LgpEnvConfigBmsResetTimer_Object = MibScalar
lgpEnvConfigBmsResetTimer = _LgpEnvConfigBmsResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 36),
    _LgpEnvConfigBmsResetTimer_Type()
)
lgpEnvConfigBmsResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigBmsResetTimer.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigBmsResetTimer.setUnits("minutes")
_LgpEnvConfigDisableSensorOffsetDegC_Type = Integer32
_LgpEnvConfigDisableSensorOffsetDegC_Object = MibScalar
lgpEnvConfigDisableSensorOffsetDegC = _LgpEnvConfigDisableSensorOffsetDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 37),
    _LgpEnvConfigDisableSensorOffsetDegC_Type()
)
lgpEnvConfigDisableSensorOffsetDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegC.setUnits("degrees Celsius")
_LgpEnvConfigDisableSensorOffsetDegF_Type = Integer32
_LgpEnvConfigDisableSensorOffsetDegF_Object = MibScalar
lgpEnvConfigDisableSensorOffsetDegF = _LgpEnvConfigDisableSensorOffsetDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 38),
    _LgpEnvConfigDisableSensorOffsetDegF_Type()
)
lgpEnvConfigDisableSensorOffsetDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegF.setUnits("degrees Fahrenheit")


class _LgpEnvConfigCabinetSensorAlarms_Type(Integer32):
    """Custom type lgpEnvConfigCabinetSensorAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LgpEnvConfigCabinetSensorAlarms_Type.__name__ = "Integer32"
_LgpEnvConfigCabinetSensorAlarms_Object = MibScalar
lgpEnvConfigCabinetSensorAlarms = _LgpEnvConfigCabinetSensorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 39),
    _LgpEnvConfigCabinetSensorAlarms_Type()
)
lgpEnvConfigCabinetSensorAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigCabinetSensorAlarms.setStatus("current")


class _LgpEnvConfigAirTemperatureControlSensor_Type(Integer32):
    """Custom type lgpEnvConfigAirTemperatureControlSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remote", 2),
          ("return", 3),
          ("supply", 1))
    )


_LgpEnvConfigAirTemperatureControlSensor_Type.__name__ = "Integer32"
_LgpEnvConfigAirTemperatureControlSensor_Object = MibScalar
lgpEnvConfigAirTemperatureControlSensor = _LgpEnvConfigAirTemperatureControlSensor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 42),
    _LgpEnvConfigAirTemperatureControlSensor_Type()
)
lgpEnvConfigAirTemperatureControlSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigAirTemperatureControlSensor.setStatus("current")


class _LgpEnvConfigFanSpeedControlSensor_Type(Integer32):
    """Custom type lgpEnvConfigFanSpeedControlSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remote", 2),
          ("return", 3),
          ("supply", 1))
    )


_LgpEnvConfigFanSpeedControlSensor_Type.__name__ = "Integer32"
_LgpEnvConfigFanSpeedControlSensor_Object = MibScalar
lgpEnvConfigFanSpeedControlSensor = _LgpEnvConfigFanSpeedControlSensor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 43),
    _LgpEnvConfigFanSpeedControlSensor_Type()
)
lgpEnvConfigFanSpeedControlSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedControlSensor.setStatus("current")
_LgpEnvConfigMinFanSpeed_Type = Unsigned32
_LgpEnvConfigMinFanSpeed_Object = MibScalar
lgpEnvConfigMinFanSpeed = _LgpEnvConfigMinFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 44),
    _LgpEnvConfigMinFanSpeed_Type()
)
lgpEnvConfigMinFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigMinFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigMinFanSpeed.setUnits("percent")
_LgpEnvConfigMaxFanSpeed_Type = Unsigned32
_LgpEnvConfigMaxFanSpeed_Object = MibScalar
lgpEnvConfigMaxFanSpeed = _LgpEnvConfigMaxFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 45),
    _LgpEnvConfigMaxFanSpeed_Type()
)
lgpEnvConfigMaxFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigMaxFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigMaxFanSpeed.setUnits("percent")
_LgpEnvConfigFanSpeedPropBandDegC_Type = Integer32
_LgpEnvConfigFanSpeedPropBandDegC_Object = MibScalar
lgpEnvConfigFanSpeedPropBandDegC = _LgpEnvConfigFanSpeedPropBandDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 46),
    _LgpEnvConfigFanSpeedPropBandDegC_Type()
)
lgpEnvConfigFanSpeedPropBandDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegC.setUnits("degrees Celsius")
_LgpEnvConfigFanSpeedPropBandDegF_Type = Integer32
_LgpEnvConfigFanSpeedPropBandDegF_Object = MibScalar
lgpEnvConfigFanSpeedPropBandDegF = _LgpEnvConfigFanSpeedPropBandDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 47),
    _LgpEnvConfigFanSpeedPropBandDegF_Type()
)
lgpEnvConfigFanSpeedPropBandDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegF.setUnits("degrees Fahrenheit")
_LgpEnvControl_ObjectIdentity = ObjectIdentity
lgpEnvControl = _LgpEnvControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5)
)
if mibBuilder.loadTexts:
    lgpEnvControl.setStatus("current")


class _LgpEnvControlShutdownAfterDelay_Type(Integer32):
    """Custom type lgpEnvControlShutdownAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LgpEnvControlShutdownAfterDelay_Type.__name__ = "Integer32"
_LgpEnvControlShutdownAfterDelay_Object = MibScalar
lgpEnvControlShutdownAfterDelay = _LgpEnvControlShutdownAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 1),
    _LgpEnvControlShutdownAfterDelay_Type()
)
lgpEnvControlShutdownAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvControlShutdownAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvControlShutdownAfterDelay.setUnits("seconds")


class _LgpEnvControlStartupAfterDelay_Type(Integer32):
    """Custom type lgpEnvControlStartupAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LgpEnvControlStartupAfterDelay_Type.__name__ = "Integer32"
_LgpEnvControlStartupAfterDelay_Object = MibScalar
lgpEnvControlStartupAfterDelay = _LgpEnvControlStartupAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 2),
    _LgpEnvControlStartupAfterDelay_Type()
)
lgpEnvControlStartupAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvControlStartupAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvControlStartupAfterDelay.setUnits("seconds")
_LgpEnvSleepIntervalTimeTable_Object = MibTable
lgpEnvSleepIntervalTimeTable = _LgpEnvSleepIntervalTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3)
)
if mibBuilder.loadTexts:
    lgpEnvSleepIntervalTimeTable.setStatus("current")
_LgpEnvSleepIntervalTimeEntry_Object = MibTableRow
lgpEnvSleepIntervalTimeEntry = _LgpEnvSleepIntervalTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1)
)
lgpEnvSleepIntervalTimeEntry.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvSleepTimeIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvSleepIntervalTimeEntry.setStatus("current")
_LgpEnvSleepTimeIndex_Type = Unsigned32
_LgpEnvSleepTimeIndex_Object = MibTableColumn
lgpEnvSleepTimeIndex = _LgpEnvSleepTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 1),
    _LgpEnvSleepTimeIndex_Type()
)
lgpEnvSleepTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeIndex.setStatus("current")
_LgpEnvSleepTimeSubID_Type = Integer32
_LgpEnvSleepTimeSubID_Object = MibTableColumn
lgpEnvSleepTimeSubID = _LgpEnvSleepTimeSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 2),
    _LgpEnvSleepTimeSubID_Type()
)
lgpEnvSleepTimeSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeSubID.setStatus("current")


class _LgpEnvSleepTimeStartHour_Type(Integer32):
    """Custom type lgpEnvSleepTimeStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvSleepTimeStartHour_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStartHour_Object = MibTableColumn
lgpEnvSleepTimeStartHour = _LgpEnvSleepTimeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 3),
    _LgpEnvSleepTimeStartHour_Type()
)
lgpEnvSleepTimeStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartHour.setUnits("hour")


class _LgpEnvSleepTimeStartMinute_Type(Integer32):
    """Custom type lgpEnvSleepTimeStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvSleepTimeStartMinute_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStartMinute_Object = MibTableColumn
lgpEnvSleepTimeStartMinute = _LgpEnvSleepTimeStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 4),
    _LgpEnvSleepTimeStartMinute_Type()
)
lgpEnvSleepTimeStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartMinute.setUnits("minute")


class _LgpEnvSleepTimeStopHour_Type(Integer32):
    """Custom type lgpEnvSleepTimeStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvSleepTimeStopHour_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStopHour_Object = MibTableColumn
lgpEnvSleepTimeStopHour = _LgpEnvSleepTimeStopHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 5),
    _LgpEnvSleepTimeStopHour_Type()
)
lgpEnvSleepTimeStopHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopHour.setUnits("hour")


class _LgpEnvSleepTimeStopMinute_Type(Integer32):
    """Custom type lgpEnvSleepTimeStopMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvSleepTimeStopMinute_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStopMinute_Object = MibTableColumn
lgpEnvSleepTimeStopMinute = _LgpEnvSleepTimeStopMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 6),
    _LgpEnvSleepTimeStopMinute_Type()
)
lgpEnvSleepTimeStopMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopMinute.setUnits("minute")
_LgpEnvSleepDayTable_Object = MibTable
lgpEnvSleepDayTable = _LgpEnvSleepDayTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4)
)
if mibBuilder.loadTexts:
    lgpEnvSleepDayTable.setStatus("current")
_LgpEnvSleepDayEntry_Object = MibTableRow
lgpEnvSleepDayEntry = _LgpEnvSleepDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1)
)
lgpEnvSleepDayEntry.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvSleepDayIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvSleepDayEntry.setStatus("current")
_LgpEnvSleepDayIndex_Type = Unsigned32
_LgpEnvSleepDayIndex_Object = MibTableColumn
lgpEnvSleepDayIndex = _LgpEnvSleepDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1, 1),
    _LgpEnvSleepDayIndex_Type()
)
lgpEnvSleepDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvSleepDayIndex.setStatus("current")


class _LgpEnvSleepDay_Type(Integer32):
    """Custom type lgpEnvSleepDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_LgpEnvSleepDay_Type.__name__ = "Integer32"
_LgpEnvSleepDay_Object = MibTableColumn
lgpEnvSleepDay = _LgpEnvSleepDay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1, 2),
    _LgpEnvSleepDay_Type()
)
lgpEnvSleepDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvSleepDay.setStatus("current")


class _LgpEnvSleepAllDayEnabled_Type(Integer32):
    """Custom type lgpEnvSleepAllDayEnabled based on Integer32"""
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


_LgpEnvSleepAllDayEnabled_Type.__name__ = "Integer32"
_LgpEnvSleepAllDayEnabled_Object = MibTableColumn
lgpEnvSleepAllDayEnabled = _LgpEnvSleepAllDayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1, 3),
    _LgpEnvSleepAllDayEnabled_Type()
)
lgpEnvSleepAllDayEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepAllDayEnabled.setStatus("current")
_LgpEnvStatistics_ObjectIdentity = ObjectIdentity
lgpEnvStatistics = _LgpEnvStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6)
)
if mibBuilder.loadTexts:
    lgpEnvStatistics.setStatus("current")
_LgpEnvStatisticsComp1RunHr_Type = Unsigned32
_LgpEnvStatisticsComp1RunHr_Object = MibScalar
lgpEnvStatisticsComp1RunHr = _LgpEnvStatisticsComp1RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 1),
    _LgpEnvStatisticsComp1RunHr_Type()
)
lgpEnvStatisticsComp1RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp1RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp1RunHr.setUnits("hours")
_LgpEnvStatisticsComp2RunHr_Type = Unsigned32
_LgpEnvStatisticsComp2RunHr_Object = MibScalar
lgpEnvStatisticsComp2RunHr = _LgpEnvStatisticsComp2RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 2),
    _LgpEnvStatisticsComp2RunHr_Type()
)
lgpEnvStatisticsComp2RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp2RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp2RunHr.setUnits("hours")
_LgpEnvStatisticsFanRunHr_Type = Unsigned32
_LgpEnvStatisticsFanRunHr_Object = MibScalar
lgpEnvStatisticsFanRunHr = _LgpEnvStatisticsFanRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 3),
    _LgpEnvStatisticsFanRunHr_Type()
)
lgpEnvStatisticsFanRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsFanRunHr.setStatus("current")
_LgpEnvStatisticsHumRunHr_Type = Unsigned32
_LgpEnvStatisticsHumRunHr_Object = MibScalar
lgpEnvStatisticsHumRunHr = _LgpEnvStatisticsHumRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 4),
    _LgpEnvStatisticsHumRunHr_Type()
)
lgpEnvStatisticsHumRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHumRunHr.setStatus("current")
_LgpEnvStatisticsReheat1RunHr_Type = Unsigned32
_LgpEnvStatisticsReheat1RunHr_Object = MibScalar
lgpEnvStatisticsReheat1RunHr = _LgpEnvStatisticsReheat1RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 7),
    _LgpEnvStatisticsReheat1RunHr_Type()
)
lgpEnvStatisticsReheat1RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat1RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat1RunHr.setUnits("hours")
_LgpEnvStatisticsReheat2RunHr_Type = Unsigned32
_LgpEnvStatisticsReheat2RunHr_Object = MibScalar
lgpEnvStatisticsReheat2RunHr = _LgpEnvStatisticsReheat2RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 8),
    _LgpEnvStatisticsReheat2RunHr_Type()
)
lgpEnvStatisticsReheat2RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat2RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat2RunHr.setUnits("hours")
_LgpEnvStatisticsReheat3RunHr_Type = Unsigned32
_LgpEnvStatisticsReheat3RunHr_Object = MibScalar
lgpEnvStatisticsReheat3RunHr = _LgpEnvStatisticsReheat3RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 9),
    _LgpEnvStatisticsReheat3RunHr_Type()
)
lgpEnvStatisticsReheat3RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat3RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat3RunHr.setUnits("hours")
_LgpEnvStatisticsCoolingModeHrs_Type = Unsigned32
_LgpEnvStatisticsCoolingModeHrs_Object = MibScalar
lgpEnvStatisticsCoolingModeHrs = _LgpEnvStatisticsCoolingModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 10),
    _LgpEnvStatisticsCoolingModeHrs_Type()
)
lgpEnvStatisticsCoolingModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsCoolingModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsCoolingModeHrs.setUnits("hours")
_LgpEnvStatisticsHeatingModeHrs_Type = Unsigned32
_LgpEnvStatisticsHeatingModeHrs_Object = MibScalar
lgpEnvStatisticsHeatingModeHrs = _LgpEnvStatisticsHeatingModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 11),
    _LgpEnvStatisticsHeatingModeHrs_Type()
)
lgpEnvStatisticsHeatingModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHeatingModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHeatingModeHrs.setUnits("hours")
_LgpEnvStatisticsHumidifyModeHrs_Type = Unsigned32
_LgpEnvStatisticsHumidifyModeHrs_Object = MibScalar
lgpEnvStatisticsHumidifyModeHrs = _LgpEnvStatisticsHumidifyModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 12),
    _LgpEnvStatisticsHumidifyModeHrs_Type()
)
lgpEnvStatisticsHumidifyModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHumidifyModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHumidifyModeHrs.setUnits("hours")
_LgpEnvStatisticsDehumidifyModeHrs_Type = Unsigned32
_LgpEnvStatisticsDehumidifyModeHrs_Object = MibScalar
lgpEnvStatisticsDehumidifyModeHrs = _LgpEnvStatisticsDehumidifyModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 13),
    _LgpEnvStatisticsDehumidifyModeHrs_Type()
)
lgpEnvStatisticsDehumidifyModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsDehumidifyModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsDehumidifyModeHrs.setUnits("hours")
_LgpEnvStatisticsHotGasRunHr_Type = Unsigned32
_LgpEnvStatisticsHotGasRunHr_Object = MibScalar
lgpEnvStatisticsHotGasRunHr = _LgpEnvStatisticsHotGasRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 14),
    _LgpEnvStatisticsHotGasRunHr_Type()
)
lgpEnvStatisticsHotGasRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotGasRunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotGasRunHr.setUnits("hours")
_LgpEnvStatisticsHotWaterRunHr_Type = Unsigned32
_LgpEnvStatisticsHotWaterRunHr_Object = MibScalar
lgpEnvStatisticsHotWaterRunHr = _LgpEnvStatisticsHotWaterRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 15),
    _LgpEnvStatisticsHotWaterRunHr_Type()
)
lgpEnvStatisticsHotWaterRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotWaterRunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotWaterRunHr.setUnits("hours")
_LgpEnvStatisticsFreeCoolRunHr_Type = Unsigned32
_LgpEnvStatisticsFreeCoolRunHr_Object = MibScalar
lgpEnvStatisticsFreeCoolRunHr = _LgpEnvStatisticsFreeCoolRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 16),
    _LgpEnvStatisticsFreeCoolRunHr_Type()
)
lgpEnvStatisticsFreeCoolRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsFreeCoolRunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsFreeCoolRunHr.setUnits("hours")
_LgpEnvStatisticsComp3RunHr_Type = Unsigned32
_LgpEnvStatisticsComp3RunHr_Object = MibScalar
lgpEnvStatisticsComp3RunHr = _LgpEnvStatisticsComp3RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 17),
    _LgpEnvStatisticsComp3RunHr_Type()
)
lgpEnvStatisticsComp3RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp3RunHr.setStatus("current")
_LgpEnvStatisticsComp4RunHr_Type = Unsigned32
_LgpEnvStatisticsComp4RunHr_Object = MibScalar
lgpEnvStatisticsComp4RunHr = _LgpEnvStatisticsComp4RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 18),
    _LgpEnvStatisticsComp4RunHr_Type()
)
lgpEnvStatisticsComp4RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp4RunHr.setStatus("current")
_LgpEnvPoints_ObjectIdentity = ObjectIdentity
lgpEnvPoints = _LgpEnvPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7)
)
if mibBuilder.loadTexts:
    lgpEnvPoints.setStatus("current")
_LgpEnvWellKnownPoints_ObjectIdentity = ObjectIdentity
lgpEnvWellKnownPoints = _LgpEnvWellKnownPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1)
)
if mibBuilder.loadTexts:
    lgpEnvWellKnownPoints.setStatus("current")
_LgpEnvFanPoint_ObjectIdentity = ObjectIdentity
lgpEnvFanPoint = _LgpEnvFanPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvFanPoint.setStatus("current")
_LgpEnvCompressorPoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressorPoint = _LgpEnvCompressorPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressorPoint.setStatus("current")
_LgpEnvElectricHeaterPoint_ObjectIdentity = ObjectIdentity
lgpEnvElectricHeaterPoint = _LgpEnvElectricHeaterPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvElectricHeaterPoint.setStatus("current")
_LgpEnvChilledWaterPoint_ObjectIdentity = ObjectIdentity
lgpEnvChilledWaterPoint = _LgpEnvChilledWaterPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 4)
)
if mibBuilder.loadTexts:
    lgpEnvChilledWaterPoint.setStatus("current")
_LgpEnvHumidifierPoint_ObjectIdentity = ObjectIdentity
lgpEnvHumidifierPoint = _LgpEnvHumidifierPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 5)
)
if mibBuilder.loadTexts:
    lgpEnvHumidifierPoint.setStatus("current")
_LgpEnvDehumidifierPoint_ObjectIdentity = ObjectIdentity
lgpEnvDehumidifierPoint = _LgpEnvDehumidifierPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 6)
)
if mibBuilder.loadTexts:
    lgpEnvDehumidifierPoint.setStatus("current")
_LgpEnvFreeCoolingPoint_ObjectIdentity = ObjectIdentity
lgpEnvFreeCoolingPoint = _LgpEnvFreeCoolingPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 7)
)
if mibBuilder.loadTexts:
    lgpEnvFreeCoolingPoint.setStatus("current")
_LgpEnvHotWaterPoint_ObjectIdentity = ObjectIdentity
lgpEnvHotWaterPoint = _LgpEnvHotWaterPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 8)
)
if mibBuilder.loadTexts:
    lgpEnvHotWaterPoint.setStatus("current")
_LgpEnvHotGasPoint_ObjectIdentity = ObjectIdentity
lgpEnvHotGasPoint = _LgpEnvHotGasPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 9)
)
if mibBuilder.loadTexts:
    lgpEnvHotGasPoint.setStatus("current")
_LgpEnvBatteryCabinetPoint_ObjectIdentity = ObjectIdentity
lgpEnvBatteryCabinetPoint = _LgpEnvBatteryCabinetPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 10)
)
if mibBuilder.loadTexts:
    lgpEnvBatteryCabinetPoint.setStatus("current")
_LgpEnvPumpPoints_ObjectIdentity = ObjectIdentity
lgpEnvPumpPoints = _LgpEnvPumpPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 11)
)
if mibBuilder.loadTexts:
    lgpEnvPumpPoints.setStatus("current")
_LgpEnvPump1Point_ObjectIdentity = ObjectIdentity
lgpEnvPump1Point = _LgpEnvPump1Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 11, 1)
)
if mibBuilder.loadTexts:
    lgpEnvPump1Point.setStatus("current")
_LgpEnvPump2Point_ObjectIdentity = ObjectIdentity
lgpEnvPump2Point = _LgpEnvPump2Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 11, 2)
)
if mibBuilder.loadTexts:
    lgpEnvPump2Point.setStatus("current")
_LgpEnvCompressorPoints_ObjectIdentity = ObjectIdentity
lgpEnvCompressorPoints = _LgpEnvCompressorPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12)
)
if mibBuilder.loadTexts:
    lgpEnvCompressorPoints.setStatus("current")
_LgpEnvCompressor1Point_ObjectIdentity = ObjectIdentity
lgpEnvCompressor1Point = _LgpEnvCompressor1Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor1Point.setStatus("current")
_LgpEnvCompressor1APoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor1APoint = _LgpEnvCompressor1APoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor1APoint.setStatus("current")
_LgpEnvCompressor1BPoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor1BPoint = _LgpEnvCompressor1BPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor1BPoint.setStatus("current")
_LgpEnvCompressor2Point_ObjectIdentity = ObjectIdentity
lgpEnvCompressor2Point = _LgpEnvCompressor2Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor2Point.setStatus("current")
_LgpEnvCompressor2APoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor2APoint = _LgpEnvCompressor2APoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor2APoint.setStatus("current")
_LgpEnvCompressor2BPoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor2BPoint = _LgpEnvCompressor2BPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 2, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor2BPoint.setStatus("current")
_LgpEnvValvePoints_ObjectIdentity = ObjectIdentity
lgpEnvValvePoints = _LgpEnvValvePoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 13)
)
if mibBuilder.loadTexts:
    lgpEnvValvePoints.setStatus("current")
_LgpEnvHotGasValve1Point_ObjectIdentity = ObjectIdentity
lgpEnvHotGasValve1Point = _LgpEnvHotGasValve1Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 13, 1)
)
if mibBuilder.loadTexts:
    lgpEnvHotGasValve1Point.setStatus("current")
_LgpEnvHotGasValve2Point_ObjectIdentity = ObjectIdentity
lgpEnvHotGasValve2Point = _LgpEnvHotGasValve2Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 13, 2)
)
if mibBuilder.loadTexts:
    lgpEnvHotGasValve2Point.setStatus("current")
_LgpEnvRemoteSensorStatisticPoints_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorStatisticPoints = _LgpEnvRemoteSensorStatisticPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorStatisticPoints.setStatus("current")
_LgpEnvRemoteSensorMinimumPoint_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorMinimumPoint = _LgpEnvRemoteSensorMinimumPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14, 1)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorMinimumPoint.setStatus("current")
_LgpEnvRemoteSensorMaximumPoint_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorMaximumPoint = _LgpEnvRemoteSensorMaximumPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14, 2)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorMaximumPoint.setStatus("current")
_LgpEnvRemoteSensorAveragePoint_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorAveragePoint = _LgpEnvRemoteSensorAveragePoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14, 3)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorAveragePoint.setStatus("current")
_LgpEnvUnits_ObjectIdentity = ObjectIdentity
lgpEnvUnits = _LgpEnvUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 8)
)
if mibBuilder.loadTexts:
    lgpEnvUnits.setStatus("current")
_LgpEnvWellKnownUnits_ObjectIdentity = ObjectIdentity
lgpEnvWellKnownUnits = _LgpEnvWellKnownUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    lgpEnvWellKnownUnits.setStatus("current")
_LgpEnvHours_ObjectIdentity = ObjectIdentity
lgpEnvHours = _LgpEnvHours_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 8, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvHours.setStatus("current")
_LgpEnvRemoteSensors_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensors = _LgpEnvRemoteSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensors.setStatus("current")


class _LgpEnvRemoteSensorCalc_Type(Integer32):
    """Custom type lgpEnvRemoteSensorCalc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("maximum", 2))
    )


_LgpEnvRemoteSensorCalc_Type.__name__ = "Integer32"
_LgpEnvRemoteSensorCalc_Object = MibScalar
lgpEnvRemoteSensorCalc = _LgpEnvRemoteSensorCalc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 1),
    _LgpEnvRemoteSensorCalc_Type()
)
lgpEnvRemoteSensorCalc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorCalc.setStatus("current")
_LgpEnvRemoteSensorTable_Object = MibTable
lgpEnvRemoteSensorTable = _LgpEnvRemoteSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTable.setStatus("current")
_LgpEnvRemoteSensorEntry_Object = MibTableRow
lgpEnvRemoteSensorEntry = _LgpEnvRemoteSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1)
)
lgpEnvRemoteSensorEntry.setIndexNames(
    (0, "LIEBERT-GP-ENVIRONMENTAL-MIB", "lgpEnvRemoteSensorIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorEntry.setStatus("current")
_LgpEnvRemoteSensorIndex_Type = Unsigned32
_LgpEnvRemoteSensorIndex_Object = MibTableColumn
lgpEnvRemoteSensorIndex = _LgpEnvRemoteSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 1),
    _LgpEnvRemoteSensorIndex_Type()
)
lgpEnvRemoteSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorIndex.setStatus("current")
_LgpEnvRemoteSensorId_Type = Unsigned32
_LgpEnvRemoteSensorId_Object = MibTableColumn
lgpEnvRemoteSensorId = _LgpEnvRemoteSensorId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 2),
    _LgpEnvRemoteSensorId_Type()
)
lgpEnvRemoteSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorId.setStatus("current")


class _LgpEnvRemoteSensorMode_Type(Integer32):
    """Custom type lgpEnvRemoteSensorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("disable", 0),
          ("reference", 1))
    )


_LgpEnvRemoteSensorMode_Type.__name__ = "Integer32"
_LgpEnvRemoteSensorMode_Object = MibTableColumn
lgpEnvRemoteSensorMode = _LgpEnvRemoteSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 3),
    _LgpEnvRemoteSensorMode_Type()
)
lgpEnvRemoteSensorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorMode.setStatus("current")
_LgpEnvRemoteSensorUsrLabel_Type = DisplayString
_LgpEnvRemoteSensorUsrLabel_Object = MibTableColumn
lgpEnvRemoteSensorUsrLabel = _LgpEnvRemoteSensorUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 4),
    _LgpEnvRemoteSensorUsrLabel_Type()
)
lgpEnvRemoteSensorUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorUsrLabel.setStatus("current")
_LgpEnvRemoteSensorTempMeasurementDegF_Type = Integer32
_LgpEnvRemoteSensorTempMeasurementDegF_Object = MibTableColumn
lgpEnvRemoteSensorTempMeasurementDegF = _LgpEnvRemoteSensorTempMeasurementDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 5),
    _LgpEnvRemoteSensorTempMeasurementDegF_Type()
)
lgpEnvRemoteSensorTempMeasurementDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegF.setUnits("degrees Fahrenheit")
_LgpEnvRemoteSensorTempMeasurementDegC_Type = Integer32
_LgpEnvRemoteSensorTempMeasurementDegC_Object = MibTableColumn
lgpEnvRemoteSensorTempMeasurementDegC = _LgpEnvRemoteSensorTempMeasurementDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 6),
    _LgpEnvRemoteSensorTempMeasurementDegC_Type()
)
lgpEnvRemoteSensorTempMeasurementDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegC.setUnits("degrees Celsius")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-ENVIRONMENTAL-MIB",
    **{"liebertGlobalProductsEnvironmentalModule": liebertGlobalProductsEnvironmentalModule,
       "lgpEnvTemperature": lgpEnvTemperature,
       "lgpEnvTemperatureWellKnown": lgpEnvTemperatureWellKnown,
       "lgpEnvControlTemperature": lgpEnvControlTemperature,
       "lgpEnvReturnAirTemperature": lgpEnvReturnAirTemperature,
       "lgpEnvSupplyAirTemperature": lgpEnvSupplyAirTemperature,
       "lgpAmbientTemperature": lgpAmbientTemperature,
       "lgpInverterTemperature": lgpInverterTemperature,
       "lgpBatteryTempterature": lgpBatteryTempterature,
       "lgpAcDcConverterTemperature": lgpAcDcConverterTemperature,
       "lgpPfcTemperature": lgpPfcTemperature,
       "lgpTransformerTemperature": lgpTransformerTemperature,
       "lgpLocalTemperature": lgpLocalTemperature,
       "lgpLocal1Temperature": lgpLocal1Temperature,
       "lgpLocal2Temperature": lgpLocal2Temperature,
       "lgpLocal3Temperature": lgpLocal3Temperature,
       "lgpDigitalScrollCompressorTemperature": lgpDigitalScrollCompressorTemperature,
       "lgpDigitalScrollCompressor1Temperature": lgpDigitalScrollCompressor1Temperature,
       "lgpDigitalScrollCompressor2Temperature": lgpDigitalScrollCompressor2Temperature,
       "lgpChillWaterTemperature": lgpChillWaterTemperature,
       "lgpCoolantTemperature": lgpCoolantTemperature,
       "lgpEnvEnclosureTemperatureSensors": lgpEnvEnclosureTemperatureSensors,
       "lgpEnvEnclosureTemperatureSensor1": lgpEnvEnclosureTemperatureSensor1,
       "lgpEnvEnclosureTemperatureSensor2": lgpEnvEnclosureTemperatureSensor2,
       "lgpEnvEnclosureTemperatureSensor3": lgpEnvEnclosureTemperatureSensor3,
       "lgpEnvEnclosureTemperatureSensor4": lgpEnvEnclosureTemperatureSensor4,
       "lgpEnvValueAmbientRoomTemperature": lgpEnvValueAmbientRoomTemperature,
       "lgpEnvDewPointTemperature": lgpEnvDewPointTemperature,
       "lgpEnvEnclosureTemperature": lgpEnvEnclosureTemperature,
       "lgpEnvAdjustedTemperature": lgpEnvAdjustedTemperature,
       "lgpEnvExternalSensors": lgpEnvExternalSensors,
       "lgpEnvExternalAirSensorA": lgpEnvExternalAirSensorA,
       "lgpEnvExternalAirSensorADewPoint": lgpEnvExternalAirSensorADewPoint,
       "lgpEnvExternalAirSensorB": lgpEnvExternalAirSensorB,
       "lgpEnvExternalAirSensorBDewPoint": lgpEnvExternalAirSensorBDewPoint,
       "lgpEnvSupplyFluidTemperature": lgpEnvSupplyFluidTemperature,
       "lgpEnvSupplyRefrigerantTemperature": lgpEnvSupplyRefrigerantTemperature,
       "lgpEnvMinDesiredRoomAirTemperature": lgpEnvMinDesiredRoomAirTemperature,
       "lgpEnvDewPointTemperatures": lgpEnvDewPointTemperatures,
       "lgpEnvInletDewPointTemperature": lgpEnvInletDewPointTemperature,
       "lgpEnvTemperatureFahrenheit": lgpEnvTemperatureFahrenheit,
       "lgpEnvTemperatureSettingDegF": lgpEnvTemperatureSettingDegF,
       "lgpEnvTemperatureToleranceDegF": lgpEnvTemperatureToleranceDegF,
       "lgpEnvTemperatureTableDegF": lgpEnvTemperatureTableDegF,
       "lgpEnvTemperatureEntryDegF": lgpEnvTemperatureEntryDegF,
       "lgpEnvTemperatureIdDegF": lgpEnvTemperatureIdDegF,
       "lgpEnvTemperatureDescrDegF": lgpEnvTemperatureDescrDegF,
       "lgpEnvTemperatureMeasurementDegF": lgpEnvTemperatureMeasurementDegF,
       "lgpEnvTemperatureHighThresholdDegF": lgpEnvTemperatureHighThresholdDegF,
       "lgpEnvTemperatureLowThresholdDegF": lgpEnvTemperatureLowThresholdDegF,
       "lgpEnvTemperatureSetPointDegF": lgpEnvTemperatureSetPointDegF,
       "lgpEnvTemperatureDailyHighDegF": lgpEnvTemperatureDailyHighDegF,
       "lgpEnvTemperatureDailyLowDegF": lgpEnvTemperatureDailyLowDegF,
       "lgpEnvTempDailyHighTimeHourDegF": lgpEnvTempDailyHighTimeHourDegF,
       "lgpEnvTempDailyHighTimeMinuteDegF": lgpEnvTempDailyHighTimeMinuteDegF,
       "lgpEnvTempDailyHighTimeSecondDegF": lgpEnvTempDailyHighTimeSecondDegF,
       "lgpEnvTempDailyLowTimeHourDegF": lgpEnvTempDailyLowTimeHourDegF,
       "lgpEnvTempDailyLowTimeMinuteDegF": lgpEnvTempDailyLowTimeMinuteDegF,
       "lgpEnvTempDailyLowTimeSecondDegF": lgpEnvTempDailyLowTimeSecondDegF,
       "lgpEnvTemperatureMeasurementTenthsDegF": lgpEnvTemperatureMeasurementTenthsDegF,
       "lgpEnvTemperatureHighThresholdTenthsDegF": lgpEnvTemperatureHighThresholdTenthsDegF,
       "lgpEnvTemperatureLowThresholdTenthsDegF": lgpEnvTemperatureLowThresholdTenthsDegF,
       "lgpEnvTemperatureSetPointTenthsDegF": lgpEnvTemperatureSetPointTenthsDegF,
       "lgpEnvTemperatureDeadBandTenthsDegF": lgpEnvTemperatureDeadBandTenthsDegF,
       "lgpEnvTempHeatingPropBandTenthsDegF": lgpEnvTempHeatingPropBandTenthsDegF,
       "lgpEnvTempCoolingPropBandTenthsDegF": lgpEnvTempCoolingPropBandTenthsDegF,
       "lgpEnvTemperatureDeadbandRangeDegF": lgpEnvTemperatureDeadbandRangeDegF,
       "lgpEnvTemperatureCelsius": lgpEnvTemperatureCelsius,
       "lgpEnvTemperatureSettingDegC": lgpEnvTemperatureSettingDegC,
       "lgpEnvTemperatureToleranceDegC": lgpEnvTemperatureToleranceDegC,
       "lgpEnvTemperatureTableDegC": lgpEnvTemperatureTableDegC,
       "lgpEnvTemperatureEntryDegC": lgpEnvTemperatureEntryDegC,
       "lgpEnvTemperatureIdDegC": lgpEnvTemperatureIdDegC,
       "lgpEnvTemperatureDescrDegC": lgpEnvTemperatureDescrDegC,
       "lgpEnvTemperatureMeasurementDegC": lgpEnvTemperatureMeasurementDegC,
       "lgpEnvTemperatureHighThresholdDegC": lgpEnvTemperatureHighThresholdDegC,
       "lgpEnvTemperatureLowThresholdDegC": lgpEnvTemperatureLowThresholdDegC,
       "lgpEnvTemperatureSetPointDegC": lgpEnvTemperatureSetPointDegC,
       "lgpEnvTemperatureDailyHighDegC": lgpEnvTemperatureDailyHighDegC,
       "lgpEnvTemperatureDailyLowDegC": lgpEnvTemperatureDailyLowDegC,
       "lgpEnvTempDailyHighTimeHourDegC": lgpEnvTempDailyHighTimeHourDegC,
       "lgpEnvTempDailyHighTimeMinuteDegC": lgpEnvTempDailyHighTimeMinuteDegC,
       "lgpEnvTempDailyHighTimeSecondDegC": lgpEnvTempDailyHighTimeSecondDegC,
       "lgpEnvTempDailyLowTimeHourDegC": lgpEnvTempDailyLowTimeHourDegC,
       "lgpEnvTempDailyLowTimeMinuteDegC": lgpEnvTempDailyLowTimeMinuteDegC,
       "lgpEnvTempDailyLowTimeSecondDegC": lgpEnvTempDailyLowTimeSecondDegC,
       "lgpEnvTemperatureMeasurementTenthsDegC": lgpEnvTemperatureMeasurementTenthsDegC,
       "lgpEnvTemperatureHighThresholdTenthsDegC": lgpEnvTemperatureHighThresholdTenthsDegC,
       "lgpEnvTemperatureLowThresholdTenthsDegC": lgpEnvTemperatureLowThresholdTenthsDegC,
       "lgpEnvTemperatureSetPointTenthsDegC": lgpEnvTemperatureSetPointTenthsDegC,
       "lgpEnvTemperatureDeadBandTenthsDegC": lgpEnvTemperatureDeadBandTenthsDegC,
       "lgpEnvTempHeatingPropBandTenthsDegC": lgpEnvTempHeatingPropBandTenthsDegC,
       "lgpEnvTempCoolingPropBandTenthsDegC": lgpEnvTempCoolingPropBandTenthsDegC,
       "lgpEnvTemperatureDeadbandRangeDegC": lgpEnvTemperatureDeadbandRangeDegC,
       "lgpEnvTemperatureControlMode": lgpEnvTemperatureControlMode,
       "lgpEnvHumidity": lgpEnvHumidity,
       "lgpEnvHumidityWellKnown": lgpEnvHumidityWellKnown,
       "lgpEnvControlHumidity": lgpEnvControlHumidity,
       "lgpEnvReturnAirHumidity": lgpEnvReturnAirHumidity,
       "lgpEnvSupplyAirHumidity": lgpEnvSupplyAirHumidity,
       "lgpEnvValueAmbientHumidity": lgpEnvValueAmbientHumidity,
       "lgpEnvHumidityRelative": lgpEnvHumidityRelative,
       "lgpEnvHumiditySettingRel": lgpEnvHumiditySettingRel,
       "lgpEnvHumidityToleranceRel": lgpEnvHumidityToleranceRel,
       "lgpEnvHumidityTableRel": lgpEnvHumidityTableRel,
       "lgpEnvHumidityEntryRel": lgpEnvHumidityEntryRel,
       "lgpEnvHumidityIdRel": lgpEnvHumidityIdRel,
       "lgpEnvHumidityDescrRel": lgpEnvHumidityDescrRel,
       "lgpEnvHumidityMeasurementRel": lgpEnvHumidityMeasurementRel,
       "lgpEnvHumidityHighThresholdRel": lgpEnvHumidityHighThresholdRel,
       "lgpEnvHumidityLowThresholdRel": lgpEnvHumidityLowThresholdRel,
       "lgpEnvHumiditySetPoint": lgpEnvHumiditySetPoint,
       "lgpEnvHumidityDailyHigh": lgpEnvHumidityDailyHigh,
       "lgpEnvHumidityDailyLow": lgpEnvHumidityDailyLow,
       "lgpEnvHumidityDailyHighTimeHour": lgpEnvHumidityDailyHighTimeHour,
       "lgpEnvHumidityDailyHighTimeMinute": lgpEnvHumidityDailyHighTimeMinute,
       "lgpEnvHumidityDailyHighTimeSecond": lgpEnvHumidityDailyHighTimeSecond,
       "lgpEnvHumidityDailyLowTimeHour": lgpEnvHumidityDailyLowTimeHour,
       "lgpEnvHumidityDailyLowTimeMinute": lgpEnvHumidityDailyLowTimeMinute,
       "lgpEnvHumidityDailyLowTimeSecond": lgpEnvHumidityDailyLowTimeSecond,
       "lgpEnvHumidityDeadBand": lgpEnvHumidityDeadBand,
       "lgpEnvHumidifyPropBand": lgpEnvHumidifyPropBand,
       "lgpEnvDehumidifyPropBand": lgpEnvDehumidifyPropBand,
       "lgpEnvHumidityMeasurementRelTenths": lgpEnvHumidityMeasurementRelTenths,
       "lgpEnvHumidityHighThresholdRelTenths": lgpEnvHumidityHighThresholdRelTenths,
       "lgpEnvHumidityLowThresholdRelTenths": lgpEnvHumidityLowThresholdRelTenths,
       "lgpEnvHumidityDeadbandRange": lgpEnvHumidityDeadbandRange,
       "lgpEnvState": lgpEnvState,
       "lgpEnvStateSystem": lgpEnvStateSystem,
       "lgpEnvStateCooling": lgpEnvStateCooling,
       "lgpEnvStateHeating": lgpEnvStateHeating,
       "lgpEnvStateHumidifying": lgpEnvStateHumidifying,
       "lgpEnvStateDehumidifying": lgpEnvStateDehumidifying,
       "lgpEnvStateEconoCycle": lgpEnvStateEconoCycle,
       "lgpEnvStateFan": lgpEnvStateFan,
       "lgpEnvStateGeneralAlarmOutput": lgpEnvStateGeneralAlarmOutput,
       "lgpEnvStateCoolingCapacity": lgpEnvStateCoolingCapacity,
       "lgpEnvStateHeatingCapacity": lgpEnvStateHeatingCapacity,
       "lgpEnvStateAudibleAlarm": lgpEnvStateAudibleAlarm,
       "lgpEnvStateCoolingUnits": lgpEnvStateCoolingUnits,
       "lgpEnvStateCoolingUnit1": lgpEnvStateCoolingUnit1,
       "lgpEnvStateCoolingUnit2": lgpEnvStateCoolingUnit2,
       "lgpEnvStateCoolingUnit3": lgpEnvStateCoolingUnit3,
       "lgpEnvStateCoolingUnit4": lgpEnvStateCoolingUnit4,
       "lgpEnvStateHeatingUnits": lgpEnvStateHeatingUnits,
       "lgpEnvStateHeatingUnit1": lgpEnvStateHeatingUnit1,
       "lgpEnvStateHeatingUnit2": lgpEnvStateHeatingUnit2,
       "lgpEnvStateHeatingUnit3": lgpEnvStateHeatingUnit3,
       "lgpEnvStateHeatingUnit4": lgpEnvStateHeatingUnit4,
       "lgpEnvStateOperatingReason": lgpEnvStateOperatingReason,
       "lgpEnvStateOperatingMode": lgpEnvStateOperatingMode,
       "lgpEnvStateFanCapacity": lgpEnvStateFanCapacity,
       "lgpEnvStateFreeCoolingCapacity": lgpEnvStateFreeCoolingCapacity,
       "lgpEnvStateDehumidifyingCapacity": lgpEnvStateDehumidifyingCapacity,
       "lgpEnvStateHumidifyingCapacity": lgpEnvStateHumidifyingCapacity,
       "lgpEnvStateFreeCooling": lgpEnvStateFreeCooling,
       "lgpEnvStateElectricHeater": lgpEnvStateElectricHeater,
       "lgpEnvStateHotWater": lgpEnvStateHotWater,
       "lgpEnvStateOperatingEfficiency": lgpEnvStateOperatingEfficiency,
       "lgpEnvComponentStateTable": lgpEnvComponentStateTable,
       "lgpEnvComponentStateEntry": lgpEnvComponentStateEntry,
       "lgpEnvComponentStateIndex": lgpEnvComponentStateIndex,
       "lgpEnvComponentStateDescr": lgpEnvComponentStateDescr,
       "lgpEnvComponentState": lgpEnvComponentState,
       "lgpEnvValveTable": lgpEnvValveTable,
       "lgpEnvValveEntry": lgpEnvValveEntry,
       "lgpEnvValveIndex": lgpEnvValveIndex,
       "lgpEnvValveDescr": lgpEnvValveDescr,
       "lgpEnvValveState": lgpEnvValveState,
       "lgpEnvValvePositionTenths": lgpEnvValvePositionTenths,
       "lgpEnvConfig": lgpEnvConfig,
       "lgpEnvConfigReheatLockout": lgpEnvConfigReheatLockout,
       "lgpEnvConfigHumLockout": lgpEnvConfigHumLockout,
       "lgpEnvConfigRestartDelay": lgpEnvConfigRestartDelay,
       "lgpEnvConfigRemoteShutdown": lgpEnvConfigRemoteShutdown,
       "lgpEnvConfigCoolingServiceInterval": lgpEnvConfigCoolingServiceInterval,
       "lgpEnvConfigHumidifierServiceInterval": lgpEnvConfigHumidifierServiceInterval,
       "lgpEnvConfigFilterServiceInterval": lgpEnvConfigFilterServiceInterval,
       "lgpEnvConfigSleepModeDeadbandRangeDegC": lgpEnvConfigSleepModeDeadbandRangeDegC,
       "lgpEnvConfigSleepModeDeadbandRangeDegF": lgpEnvConfigSleepModeDeadbandRangeDegF,
       "lgpEnvConfigSupplyTempLowLimitDegF": lgpEnvConfigSupplyTempLowLimitDegF,
       "lgpEnvConfigSupplyTempLowLimitDegC": lgpEnvConfigSupplyTempLowLimitDegC,
       "lgpEnvConfigTemperatureIntegTime": lgpEnvConfigTemperatureIntegTime,
       "lgpEnvConfigLocalTemperatureUnit": lgpEnvConfigLocalTemperatureUnit,
       "lgpEnvConfigSleepMode": lgpEnvConfigSleepMode,
       "lgpEnvConfigHumidityIntegTime": lgpEnvConfigHumidityIntegTime,
       "lgpEnvConfigFreecoolingDeltaDegF": lgpEnvConfigFreecoolingDeltaDegF,
       "lgpEnvConfigFreecoolingDeltaDegC": lgpEnvConfigFreecoolingDeltaDegC,
       "lgpEnvConfigSupplyTempLowLimit": lgpEnvConfigSupplyTempLowLimit,
       "lgpEnvConfigSensorEventsStandard": lgpEnvConfigSensorEventsStandard,
       "lgpEnvConfigSensorEvents1": lgpEnvConfigSensorEvents1,
       "lgpEnvConfigSleepModeDeadbandRange": lgpEnvConfigSleepModeDeadbandRange,
       "lgpEnvConfigAutoConfiguration": lgpEnvConfigAutoConfiguration,
       "lgpEnvConfigDeltaGlycolType": lgpEnvConfigDeltaGlycolType,
       "lgpEnvConfigChillWaterControl": lgpEnvConfigChillWaterControl,
       "lgpEnvConfigInfaredFlushRate": lgpEnvConfigInfaredFlushRate,
       "lgpEnvConfigHumidityControl": lgpEnvConfigHumidityControl,
       "lgpEnvConfigCompressorLockout": lgpEnvConfigCompressorLockout,
       "lgpEnvConfigReheatAndHumidifierLockout": lgpEnvConfigReheatAndHumidifierLockout,
       "lgpEnvOperationalTimeTable": lgpEnvOperationalTimeTable,
       "lgpEnvOperationalTimeEntry": lgpEnvOperationalTimeEntry,
       "lgpEnvOperationTimeIndex": lgpEnvOperationTimeIndex,
       "lgpEnvOperationTimePoint": lgpEnvOperationTimePoint,
       "lgpEnvOperationTimeSubID": lgpEnvOperationTimeSubID,
       "lgpEnvOperationTimeUnit": lgpEnvOperationTimeUnit,
       "lgpEnvOperationTimeValue": lgpEnvOperationTimeValue,
       "lgpEnvOperationTimeHighWarning": lgpEnvOperationTimeHighWarning,
       "lgpEnvConfigTempControlAlgorithm": lgpEnvConfigTempControlAlgorithm,
       "lgpEnvConfigFanSpeedMode": lgpEnvConfigFanSpeedMode,
       "lgpEnvConfigFanSpeedCapacity": lgpEnvConfigFanSpeedCapacity,
       "lgpEnvConfigBmsResetTimer": lgpEnvConfigBmsResetTimer,
       "lgpEnvConfigDisableSensorOffsetDegC": lgpEnvConfigDisableSensorOffsetDegC,
       "lgpEnvConfigDisableSensorOffsetDegF": lgpEnvConfigDisableSensorOffsetDegF,
       "lgpEnvConfigCabinetSensorAlarms": lgpEnvConfigCabinetSensorAlarms,
       "lgpEnvConfigAirTemperatureControlSensor": lgpEnvConfigAirTemperatureControlSensor,
       "lgpEnvConfigFanSpeedControlSensor": lgpEnvConfigFanSpeedControlSensor,
       "lgpEnvConfigMinFanSpeed": lgpEnvConfigMinFanSpeed,
       "lgpEnvConfigMaxFanSpeed": lgpEnvConfigMaxFanSpeed,
       "lgpEnvConfigFanSpeedPropBandDegC": lgpEnvConfigFanSpeedPropBandDegC,
       "lgpEnvConfigFanSpeedPropBandDegF": lgpEnvConfigFanSpeedPropBandDegF,
       "lgpEnvControl": lgpEnvControl,
       "lgpEnvControlShutdownAfterDelay": lgpEnvControlShutdownAfterDelay,
       "lgpEnvControlStartupAfterDelay": lgpEnvControlStartupAfterDelay,
       "lgpEnvSleepIntervalTimeTable": lgpEnvSleepIntervalTimeTable,
       "lgpEnvSleepIntervalTimeEntry": lgpEnvSleepIntervalTimeEntry,
       "lgpEnvSleepTimeIndex": lgpEnvSleepTimeIndex,
       "lgpEnvSleepTimeSubID": lgpEnvSleepTimeSubID,
       "lgpEnvSleepTimeStartHour": lgpEnvSleepTimeStartHour,
       "lgpEnvSleepTimeStartMinute": lgpEnvSleepTimeStartMinute,
       "lgpEnvSleepTimeStopHour": lgpEnvSleepTimeStopHour,
       "lgpEnvSleepTimeStopMinute": lgpEnvSleepTimeStopMinute,
       "lgpEnvSleepDayTable": lgpEnvSleepDayTable,
       "lgpEnvSleepDayEntry": lgpEnvSleepDayEntry,
       "lgpEnvSleepDayIndex": lgpEnvSleepDayIndex,
       "lgpEnvSleepDay": lgpEnvSleepDay,
       "lgpEnvSleepAllDayEnabled": lgpEnvSleepAllDayEnabled,
       "lgpEnvStatistics": lgpEnvStatistics,
       "lgpEnvStatisticsComp1RunHr": lgpEnvStatisticsComp1RunHr,
       "lgpEnvStatisticsComp2RunHr": lgpEnvStatisticsComp2RunHr,
       "lgpEnvStatisticsFanRunHr": lgpEnvStatisticsFanRunHr,
       "lgpEnvStatisticsHumRunHr": lgpEnvStatisticsHumRunHr,
       "lgpEnvStatisticsReheat1RunHr": lgpEnvStatisticsReheat1RunHr,
       "lgpEnvStatisticsReheat2RunHr": lgpEnvStatisticsReheat2RunHr,
       "lgpEnvStatisticsReheat3RunHr": lgpEnvStatisticsReheat3RunHr,
       "lgpEnvStatisticsCoolingModeHrs": lgpEnvStatisticsCoolingModeHrs,
       "lgpEnvStatisticsHeatingModeHrs": lgpEnvStatisticsHeatingModeHrs,
       "lgpEnvStatisticsHumidifyModeHrs": lgpEnvStatisticsHumidifyModeHrs,
       "lgpEnvStatisticsDehumidifyModeHrs": lgpEnvStatisticsDehumidifyModeHrs,
       "lgpEnvStatisticsHotGasRunHr": lgpEnvStatisticsHotGasRunHr,
       "lgpEnvStatisticsHotWaterRunHr": lgpEnvStatisticsHotWaterRunHr,
       "lgpEnvStatisticsFreeCoolRunHr": lgpEnvStatisticsFreeCoolRunHr,
       "lgpEnvStatisticsComp3RunHr": lgpEnvStatisticsComp3RunHr,
       "lgpEnvStatisticsComp4RunHr": lgpEnvStatisticsComp4RunHr,
       "lgpEnvPoints": lgpEnvPoints,
       "lgpEnvWellKnownPoints": lgpEnvWellKnownPoints,
       "lgpEnvFanPoint": lgpEnvFanPoint,
       "lgpEnvCompressorPoint": lgpEnvCompressorPoint,
       "lgpEnvElectricHeaterPoint": lgpEnvElectricHeaterPoint,
       "lgpEnvChilledWaterPoint": lgpEnvChilledWaterPoint,
       "lgpEnvHumidifierPoint": lgpEnvHumidifierPoint,
       "lgpEnvDehumidifierPoint": lgpEnvDehumidifierPoint,
       "lgpEnvFreeCoolingPoint": lgpEnvFreeCoolingPoint,
       "lgpEnvHotWaterPoint": lgpEnvHotWaterPoint,
       "lgpEnvHotGasPoint": lgpEnvHotGasPoint,
       "lgpEnvBatteryCabinetPoint": lgpEnvBatteryCabinetPoint,
       "lgpEnvPumpPoints": lgpEnvPumpPoints,
       "lgpEnvPump1Point": lgpEnvPump1Point,
       "lgpEnvPump2Point": lgpEnvPump2Point,
       "lgpEnvCompressorPoints": lgpEnvCompressorPoints,
       "lgpEnvCompressor1Point": lgpEnvCompressor1Point,
       "lgpEnvCompressor1APoint": lgpEnvCompressor1APoint,
       "lgpEnvCompressor1BPoint": lgpEnvCompressor1BPoint,
       "lgpEnvCompressor2Point": lgpEnvCompressor2Point,
       "lgpEnvCompressor2APoint": lgpEnvCompressor2APoint,
       "lgpEnvCompressor2BPoint": lgpEnvCompressor2BPoint,
       "lgpEnvValvePoints": lgpEnvValvePoints,
       "lgpEnvHotGasValve1Point": lgpEnvHotGasValve1Point,
       "lgpEnvHotGasValve2Point": lgpEnvHotGasValve2Point,
       "lgpEnvRemoteSensorStatisticPoints": lgpEnvRemoteSensorStatisticPoints,
       "lgpEnvRemoteSensorMinimumPoint": lgpEnvRemoteSensorMinimumPoint,
       "lgpEnvRemoteSensorMaximumPoint": lgpEnvRemoteSensorMaximumPoint,
       "lgpEnvRemoteSensorAveragePoint": lgpEnvRemoteSensorAveragePoint,
       "lgpEnvUnits": lgpEnvUnits,
       "lgpEnvWellKnownUnits": lgpEnvWellKnownUnits,
       "lgpEnvHours": lgpEnvHours,
       "lgpEnvRemoteSensors": lgpEnvRemoteSensors,
       "lgpEnvRemoteSensorCalc": lgpEnvRemoteSensorCalc,
       "lgpEnvRemoteSensorTable": lgpEnvRemoteSensorTable,
       "lgpEnvRemoteSensorEntry": lgpEnvRemoteSensorEntry,
       "lgpEnvRemoteSensorIndex": lgpEnvRemoteSensorIndex,
       "lgpEnvRemoteSensorId": lgpEnvRemoteSensorId,
       "lgpEnvRemoteSensorMode": lgpEnvRemoteSensorMode,
       "lgpEnvRemoteSensorUsrLabel": lgpEnvRemoteSensorUsrLabel,
       "lgpEnvRemoteSensorTempMeasurementDegF": lgpEnvRemoteSensorTempMeasurementDegF,
       "lgpEnvRemoteSensorTempMeasurementDegC": lgpEnvRemoteSensorTempMeasurementDegC}
)
