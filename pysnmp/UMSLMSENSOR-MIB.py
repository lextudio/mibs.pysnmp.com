# SNMP MIB module (UMSLMSENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UMSLMSENSOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:33 2024
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

(Boolean,
 Datetime,
 Real32,
 Real64,
 Sint16,
 Sint32,
 Sint64,
 Sint8,
 String,
 Uint16,
 Uint32,
 Uint64,
 Uint8,
 ibmpsgLMSensor) = mibBuilder.importSymbols(
    "UMS-MIB",
    "Boolean",
    "Datetime",
    "Real32",
    "Real64",
    "Sint16",
    "Sint32",
    "Sint64",
    "Sint8",
    "String",
    "Uint16",
    "Uint32",
    "Uint64",
    "Uint8",
    "ibmpsgLMSensor")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IBMPSGTemperatureSensorTable_Object = MibTable
iBMPSGTemperatureSensorTable = _IBMPSGTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1)
)
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorTable.setStatus("mandatory")
_IBMPSGTemperatureSensorEntry_Object = MibTableRow
iBMPSGTemperatureSensorEntry = _IBMPSGTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1)
)
iBMPSGTemperatureSensorEntry.setIndexNames(
    (0, "UMSLMSENSOR-MIB", "iBMPSGTemperatureSensorKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorEntry.setStatus("mandatory")
_IBMPSGTemperatureSensorKeyIndex_Type = String
_IBMPSGTemperatureSensorKeyIndex_Object = MibTableColumn
iBMPSGTemperatureSensorKeyIndex = _IBMPSGTemperatureSensorKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 1),
    _IBMPSGTemperatureSensorKeyIndex_Type()
)
iBMPSGTemperatureSensorKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorKeyIndex.setStatus("mandatory")
_IBMPSGTemperatureSensorCurrentReading_Type = Sint32
_IBMPSGTemperatureSensorCurrentReading_Object = MibTableColumn
iBMPSGTemperatureSensorCurrentReading = _IBMPSGTemperatureSensorCurrentReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 2),
    _IBMPSGTemperatureSensorCurrentReading_Type()
)
iBMPSGTemperatureSensorCurrentReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorCurrentReading.setStatus("mandatory")
_IBMPSGTemperatureSensorNominalReading_Type = Sint32
_IBMPSGTemperatureSensorNominalReading_Object = MibTableColumn
iBMPSGTemperatureSensorNominalReading = _IBMPSGTemperatureSensorNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 3),
    _IBMPSGTemperatureSensorNominalReading_Type()
)
iBMPSGTemperatureSensorNominalReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorNominalReading.setStatus("mandatory")
_IBMPSGTemperatureSensorNormalMax_Type = Sint32
_IBMPSGTemperatureSensorNormalMax_Object = MibTableColumn
iBMPSGTemperatureSensorNormalMax = _IBMPSGTemperatureSensorNormalMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 4),
    _IBMPSGTemperatureSensorNormalMax_Type()
)
iBMPSGTemperatureSensorNormalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorNormalMax.setStatus("mandatory")
_IBMPSGTemperatureSensorNormalMin_Type = Sint32
_IBMPSGTemperatureSensorNormalMin_Object = MibTableColumn
iBMPSGTemperatureSensorNormalMin = _IBMPSGTemperatureSensorNormalMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 5),
    _IBMPSGTemperatureSensorNormalMin_Type()
)
iBMPSGTemperatureSensorNormalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorNormalMin.setStatus("mandatory")
_IBMPSGTemperatureSensorMaxReadable_Type = Sint32
_IBMPSGTemperatureSensorMaxReadable_Object = MibTableColumn
iBMPSGTemperatureSensorMaxReadable = _IBMPSGTemperatureSensorMaxReadable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 6),
    _IBMPSGTemperatureSensorMaxReadable_Type()
)
iBMPSGTemperatureSensorMaxReadable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorMaxReadable.setStatus("mandatory")
_IBMPSGTemperatureSensorMinReadable_Type = Sint32
_IBMPSGTemperatureSensorMinReadable_Object = MibTableColumn
iBMPSGTemperatureSensorMinReadable = _IBMPSGTemperatureSensorMinReadable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 7),
    _IBMPSGTemperatureSensorMinReadable_Type()
)
iBMPSGTemperatureSensorMinReadable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorMinReadable.setStatus("mandatory")
_IBMPSGTemperatureSensorResolution_Type = Uint32
_IBMPSGTemperatureSensorResolution_Object = MibTableColumn
iBMPSGTemperatureSensorResolution = _IBMPSGTemperatureSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 8),
    _IBMPSGTemperatureSensorResolution_Type()
)
iBMPSGTemperatureSensorResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorResolution.setStatus("mandatory")
_IBMPSGTemperatureSensorTolerance_Type = Sint32
_IBMPSGTemperatureSensorTolerance_Object = MibTableColumn
iBMPSGTemperatureSensorTolerance = _IBMPSGTemperatureSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 9),
    _IBMPSGTemperatureSensorTolerance_Type()
)
iBMPSGTemperatureSensorTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorTolerance.setStatus("mandatory")
_IBMPSGTemperatureSensorAccuracy_Type = Sint32
_IBMPSGTemperatureSensorAccuracy_Object = MibTableColumn
iBMPSGTemperatureSensorAccuracy = _IBMPSGTemperatureSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 10),
    _IBMPSGTemperatureSensorAccuracy_Type()
)
iBMPSGTemperatureSensorAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorAccuracy.setStatus("mandatory")
_IBMPSGTemperatureSensorLowerThresholdNonCritical_Type = Sint32
_IBMPSGTemperatureSensorLowerThresholdNonCritical_Object = MibTableColumn
iBMPSGTemperatureSensorLowerThresholdNonCritical = _IBMPSGTemperatureSensorLowerThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 11),
    _IBMPSGTemperatureSensorLowerThresholdNonCritical_Type()
)
iBMPSGTemperatureSensorLowerThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorLowerThresholdNonCritical.setStatus("mandatory")
_IBMPSGTemperatureSensorUpperThresholdNonCritical_Type = Sint32
_IBMPSGTemperatureSensorUpperThresholdNonCritical_Object = MibTableColumn
iBMPSGTemperatureSensorUpperThresholdNonCritical = _IBMPSGTemperatureSensorUpperThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 12),
    _IBMPSGTemperatureSensorUpperThresholdNonCritical_Type()
)
iBMPSGTemperatureSensorUpperThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorUpperThresholdNonCritical.setStatus("mandatory")
_IBMPSGTemperatureSensorLowerThresholdCritical_Type = Sint32
_IBMPSGTemperatureSensorLowerThresholdCritical_Object = MibTableColumn
iBMPSGTemperatureSensorLowerThresholdCritical = _IBMPSGTemperatureSensorLowerThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 13),
    _IBMPSGTemperatureSensorLowerThresholdCritical_Type()
)
iBMPSGTemperatureSensorLowerThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorLowerThresholdCritical.setStatus("mandatory")
_IBMPSGTemperatureSensorUpperThresholdCritical_Type = Sint32
_IBMPSGTemperatureSensorUpperThresholdCritical_Object = MibTableColumn
iBMPSGTemperatureSensorUpperThresholdCritical = _IBMPSGTemperatureSensorUpperThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 14),
    _IBMPSGTemperatureSensorUpperThresholdCritical_Type()
)
iBMPSGTemperatureSensorUpperThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorUpperThresholdCritical.setStatus("mandatory")
_IBMPSGTemperatureSensorLowerThresholdFatal_Type = Sint32
_IBMPSGTemperatureSensorLowerThresholdFatal_Object = MibTableColumn
iBMPSGTemperatureSensorLowerThresholdFatal = _IBMPSGTemperatureSensorLowerThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 15),
    _IBMPSGTemperatureSensorLowerThresholdFatal_Type()
)
iBMPSGTemperatureSensorLowerThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorLowerThresholdFatal.setStatus("mandatory")
_IBMPSGTemperatureSensorUpperThresholdFatal_Type = Sint32
_IBMPSGTemperatureSensorUpperThresholdFatal_Object = MibTableColumn
iBMPSGTemperatureSensorUpperThresholdFatal = _IBMPSGTemperatureSensorUpperThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 16),
    _IBMPSGTemperatureSensorUpperThresholdFatal_Type()
)
iBMPSGTemperatureSensorUpperThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorUpperThresholdFatal.setStatus("mandatory")
_IBMPSGTemperatureSensorTempLocation_Type = Uint32
_IBMPSGTemperatureSensorTempLocation_Object = MibTableColumn
iBMPSGTemperatureSensorTempLocation = _IBMPSGTemperatureSensorTempLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 17),
    _IBMPSGTemperatureSensorTempLocation_Type()
)
iBMPSGTemperatureSensorTempLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorTempLocation.setStatus("mandatory")
_IBMPSGTemperatureSensorEventsEnabled_Type = Boolean
_IBMPSGTemperatureSensorEventsEnabled_Object = MibTableColumn
iBMPSGTemperatureSensorEventsEnabled = _IBMPSGTemperatureSensorEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 18),
    _IBMPSGTemperatureSensorEventsEnabled_Type()
)
iBMPSGTemperatureSensorEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorEventsEnabled.setStatus("mandatory")
_IBMPSGTemperatureSensorPollingInterval_Type = Uint32
_IBMPSGTemperatureSensorPollingInterval_Object = MibTableColumn
iBMPSGTemperatureSensorPollingInterval = _IBMPSGTemperatureSensorPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 19),
    _IBMPSGTemperatureSensorPollingInterval_Type()
)
iBMPSGTemperatureSensorPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorPollingInterval.setStatus("mandatory")
_IBMPSGTemperatureSensorEventAutoClearEnabled_Type = Boolean
_IBMPSGTemperatureSensorEventAutoClearEnabled_Object = MibTableColumn
iBMPSGTemperatureSensorEventAutoClearEnabled = _IBMPSGTemperatureSensorEventAutoClearEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 20),
    _IBMPSGTemperatureSensorEventAutoClearEnabled_Type()
)
iBMPSGTemperatureSensorEventAutoClearEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorEventAutoClearEnabled.setStatus("mandatory")
_IBMPSGTemperatureSensorStatus_Type = String
_IBMPSGTemperatureSensorStatus_Object = MibTableColumn
iBMPSGTemperatureSensorStatus = _IBMPSGTemperatureSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 1, 1, 21),
    _IBMPSGTemperatureSensorStatus_Type()
)
iBMPSGTemperatureSensorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTemperatureSensorStatus.setStatus("mandatory")
_IBMPSGVoltageSensorTable_Object = MibTable
iBMPSGVoltageSensorTable = _IBMPSGVoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2)
)
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorTable.setStatus("mandatory")
_IBMPSGVoltageSensorEntry_Object = MibTableRow
iBMPSGVoltageSensorEntry = _IBMPSGVoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1)
)
iBMPSGVoltageSensorEntry.setIndexNames(
    (0, "UMSLMSENSOR-MIB", "iBMPSGVoltageSensorKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorEntry.setStatus("mandatory")
_IBMPSGVoltageSensorKeyIndex_Type = String
_IBMPSGVoltageSensorKeyIndex_Object = MibTableColumn
iBMPSGVoltageSensorKeyIndex = _IBMPSGVoltageSensorKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 1),
    _IBMPSGVoltageSensorKeyIndex_Type()
)
iBMPSGVoltageSensorKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorKeyIndex.setStatus("mandatory")
_IBMPSGVoltageSensorCurrentReading_Type = Sint32
_IBMPSGVoltageSensorCurrentReading_Object = MibTableColumn
iBMPSGVoltageSensorCurrentReading = _IBMPSGVoltageSensorCurrentReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 2),
    _IBMPSGVoltageSensorCurrentReading_Type()
)
iBMPSGVoltageSensorCurrentReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorCurrentReading.setStatus("mandatory")
_IBMPSGVoltageSensorNominalReading_Type = Sint32
_IBMPSGVoltageSensorNominalReading_Object = MibTableColumn
iBMPSGVoltageSensorNominalReading = _IBMPSGVoltageSensorNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 3),
    _IBMPSGVoltageSensorNominalReading_Type()
)
iBMPSGVoltageSensorNominalReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorNominalReading.setStatus("mandatory")
_IBMPSGVoltageSensorNormalMax_Type = Sint32
_IBMPSGVoltageSensorNormalMax_Object = MibTableColumn
iBMPSGVoltageSensorNormalMax = _IBMPSGVoltageSensorNormalMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 4),
    _IBMPSGVoltageSensorNormalMax_Type()
)
iBMPSGVoltageSensorNormalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorNormalMax.setStatus("mandatory")
_IBMPSGVoltageSensorNormalMin_Type = Sint32
_IBMPSGVoltageSensorNormalMin_Object = MibTableColumn
iBMPSGVoltageSensorNormalMin = _IBMPSGVoltageSensorNormalMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 5),
    _IBMPSGVoltageSensorNormalMin_Type()
)
iBMPSGVoltageSensorNormalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorNormalMin.setStatus("mandatory")
_IBMPSGVoltageSensorMaxReadable_Type = Sint32
_IBMPSGVoltageSensorMaxReadable_Object = MibTableColumn
iBMPSGVoltageSensorMaxReadable = _IBMPSGVoltageSensorMaxReadable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 6),
    _IBMPSGVoltageSensorMaxReadable_Type()
)
iBMPSGVoltageSensorMaxReadable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorMaxReadable.setStatus("mandatory")
_IBMPSGVoltageSensorMinReadable_Type = Sint32
_IBMPSGVoltageSensorMinReadable_Object = MibTableColumn
iBMPSGVoltageSensorMinReadable = _IBMPSGVoltageSensorMinReadable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 7),
    _IBMPSGVoltageSensorMinReadable_Type()
)
iBMPSGVoltageSensorMinReadable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorMinReadable.setStatus("mandatory")
_IBMPSGVoltageSensorResolution_Type = Uint32
_IBMPSGVoltageSensorResolution_Object = MibTableColumn
iBMPSGVoltageSensorResolution = _IBMPSGVoltageSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 8),
    _IBMPSGVoltageSensorResolution_Type()
)
iBMPSGVoltageSensorResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorResolution.setStatus("mandatory")
_IBMPSGVoltageSensorTolerance_Type = Sint32
_IBMPSGVoltageSensorTolerance_Object = MibTableColumn
iBMPSGVoltageSensorTolerance = _IBMPSGVoltageSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 9),
    _IBMPSGVoltageSensorTolerance_Type()
)
iBMPSGVoltageSensorTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorTolerance.setStatus("mandatory")
_IBMPSGVoltageSensorAccuracy_Type = Sint32
_IBMPSGVoltageSensorAccuracy_Object = MibTableColumn
iBMPSGVoltageSensorAccuracy = _IBMPSGVoltageSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 10),
    _IBMPSGVoltageSensorAccuracy_Type()
)
iBMPSGVoltageSensorAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorAccuracy.setStatus("mandatory")
_IBMPSGVoltageSensorLowerThresholdNonCritical_Type = Sint32
_IBMPSGVoltageSensorLowerThresholdNonCritical_Object = MibTableColumn
iBMPSGVoltageSensorLowerThresholdNonCritical = _IBMPSGVoltageSensorLowerThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 11),
    _IBMPSGVoltageSensorLowerThresholdNonCritical_Type()
)
iBMPSGVoltageSensorLowerThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorLowerThresholdNonCritical.setStatus("mandatory")
_IBMPSGVoltageSensorUpperThresholdNonCritical_Type = Sint32
_IBMPSGVoltageSensorUpperThresholdNonCritical_Object = MibTableColumn
iBMPSGVoltageSensorUpperThresholdNonCritical = _IBMPSGVoltageSensorUpperThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 12),
    _IBMPSGVoltageSensorUpperThresholdNonCritical_Type()
)
iBMPSGVoltageSensorUpperThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorUpperThresholdNonCritical.setStatus("mandatory")
_IBMPSGVoltageSensorLowerThresholdCritical_Type = Sint32
_IBMPSGVoltageSensorLowerThresholdCritical_Object = MibTableColumn
iBMPSGVoltageSensorLowerThresholdCritical = _IBMPSGVoltageSensorLowerThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 13),
    _IBMPSGVoltageSensorLowerThresholdCritical_Type()
)
iBMPSGVoltageSensorLowerThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorLowerThresholdCritical.setStatus("mandatory")
_IBMPSGVoltageSensorUpperThresholdCritical_Type = Sint32
_IBMPSGVoltageSensorUpperThresholdCritical_Object = MibTableColumn
iBMPSGVoltageSensorUpperThresholdCritical = _IBMPSGVoltageSensorUpperThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 14),
    _IBMPSGVoltageSensorUpperThresholdCritical_Type()
)
iBMPSGVoltageSensorUpperThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorUpperThresholdCritical.setStatus("mandatory")
_IBMPSGVoltageSensorLowerThresholdFatal_Type = Sint32
_IBMPSGVoltageSensorLowerThresholdFatal_Object = MibTableColumn
iBMPSGVoltageSensorLowerThresholdFatal = _IBMPSGVoltageSensorLowerThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 15),
    _IBMPSGVoltageSensorLowerThresholdFatal_Type()
)
iBMPSGVoltageSensorLowerThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorLowerThresholdFatal.setStatus("mandatory")
_IBMPSGVoltageSensorUpperThresholdFatal_Type = Sint32
_IBMPSGVoltageSensorUpperThresholdFatal_Object = MibTableColumn
iBMPSGVoltageSensorUpperThresholdFatal = _IBMPSGVoltageSensorUpperThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 16),
    _IBMPSGVoltageSensorUpperThresholdFatal_Type()
)
iBMPSGVoltageSensorUpperThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorUpperThresholdFatal.setStatus("mandatory")
_IBMPSGVoltageSensorVoltageType_Type = Uint32
_IBMPSGVoltageSensorVoltageType_Object = MibTableColumn
iBMPSGVoltageSensorVoltageType = _IBMPSGVoltageSensorVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 17),
    _IBMPSGVoltageSensorVoltageType_Type()
)
iBMPSGVoltageSensorVoltageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorVoltageType.setStatus("mandatory")
_IBMPSGVoltageSensorEventsEnabled_Type = Boolean
_IBMPSGVoltageSensorEventsEnabled_Object = MibTableColumn
iBMPSGVoltageSensorEventsEnabled = _IBMPSGVoltageSensorEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 18),
    _IBMPSGVoltageSensorEventsEnabled_Type()
)
iBMPSGVoltageSensorEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorEventsEnabled.setStatus("mandatory")
_IBMPSGVoltageSensorPollingInterval_Type = Uint32
_IBMPSGVoltageSensorPollingInterval_Object = MibTableColumn
iBMPSGVoltageSensorPollingInterval = _IBMPSGVoltageSensorPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 19),
    _IBMPSGVoltageSensorPollingInterval_Type()
)
iBMPSGVoltageSensorPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorPollingInterval.setStatus("mandatory")
_IBMPSGVoltageSensorEventAutoClearEnabled_Type = Boolean
_IBMPSGVoltageSensorEventAutoClearEnabled_Object = MibTableColumn
iBMPSGVoltageSensorEventAutoClearEnabled = _IBMPSGVoltageSensorEventAutoClearEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 20),
    _IBMPSGVoltageSensorEventAutoClearEnabled_Type()
)
iBMPSGVoltageSensorEventAutoClearEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorEventAutoClearEnabled.setStatus("mandatory")
_IBMPSGVoltageSensorStatus_Type = String
_IBMPSGVoltageSensorStatus_Object = MibTableColumn
iBMPSGVoltageSensorStatus = _IBMPSGVoltageSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 2, 1, 21),
    _IBMPSGVoltageSensorStatus_Type()
)
iBMPSGVoltageSensorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGVoltageSensorStatus.setStatus("mandatory")
_IBMPSGFanTable_Object = MibTable
iBMPSGFanTable = _IBMPSGFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3)
)
if mibBuilder.loadTexts:
    iBMPSGFanTable.setStatus("mandatory")
_IBMPSGFanEntry_Object = MibTableRow
iBMPSGFanEntry = _IBMPSGFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1)
)
iBMPSGFanEntry.setIndexNames(
    (0, "UMSLMSENSOR-MIB", "iBMPSGFanKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGFanEntry.setStatus("mandatory")
_IBMPSGFanKeyIndex_Type = String
_IBMPSGFanKeyIndex_Object = MibTableColumn
iBMPSGFanKeyIndex = _IBMPSGFanKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 1),
    _IBMPSGFanKeyIndex_Type()
)
iBMPSGFanKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanKeyIndex.setStatus("mandatory")
_IBMPSGFanVariableSpeed_Type = Boolean
_IBMPSGFanVariableSpeed_Object = MibTableColumn
iBMPSGFanVariableSpeed = _IBMPSGFanVariableSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 2),
    _IBMPSGFanVariableSpeed_Type()
)
iBMPSGFanVariableSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanVariableSpeed.setStatus("mandatory")
_IBMPSGFanDesiredSpeed_Type = String
_IBMPSGFanDesiredSpeed_Object = MibTableColumn
iBMPSGFanDesiredSpeed = _IBMPSGFanDesiredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 3),
    _IBMPSGFanDesiredSpeed_Type()
)
iBMPSGFanDesiredSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanDesiredSpeed.setStatus("mandatory")
_IBMPSGFanActiveCooling_Type = Boolean
_IBMPSGFanActiveCooling_Object = MibTableColumn
iBMPSGFanActiveCooling = _IBMPSGFanActiveCooling_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 4),
    _IBMPSGFanActiveCooling_Type()
)
iBMPSGFanActiveCooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanActiveCooling.setStatus("mandatory")
_IBMPSGFanFanType_Type = Uint32
_IBMPSGFanFanType_Object = MibTableColumn
iBMPSGFanFanType = _IBMPSGFanFanType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 5),
    _IBMPSGFanFanType_Type()
)
iBMPSGFanFanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanFanType.setStatus("mandatory")
_IBMPSGFanEventsEnabled_Type = Boolean
_IBMPSGFanEventsEnabled_Object = MibTableColumn
iBMPSGFanEventsEnabled = _IBMPSGFanEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 6),
    _IBMPSGFanEventsEnabled_Type()
)
iBMPSGFanEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanEventsEnabled.setStatus("mandatory")
_IBMPSGFanPollingInterval_Type = Uint32
_IBMPSGFanPollingInterval_Object = MibTableColumn
iBMPSGFanPollingInterval = _IBMPSGFanPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 7),
    _IBMPSGFanPollingInterval_Type()
)
iBMPSGFanPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanPollingInterval.setStatus("mandatory")
_IBMPSGFanEventAutoClearEnabled_Type = Boolean
_IBMPSGFanEventAutoClearEnabled_Object = MibTableColumn
iBMPSGFanEventAutoClearEnabled = _IBMPSGFanEventAutoClearEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 8),
    _IBMPSGFanEventAutoClearEnabled_Type()
)
iBMPSGFanEventAutoClearEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanEventAutoClearEnabled.setStatus("mandatory")
_IBMPSGFanStatus_Type = String
_IBMPSGFanStatus_Object = MibTableColumn
iBMPSGFanStatus = _IBMPSGFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 3, 1, 9),
    _IBMPSGFanStatus_Type()
)
iBMPSGFanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGFanStatus.setStatus("mandatory")
_IBMPSGSystemEnclosureTable_Object = MibTable
iBMPSGSystemEnclosureTable = _IBMPSGSystemEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4)
)
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureTable.setStatus("mandatory")
_IBMPSGSystemEnclosureEntry_Object = MibTableRow
iBMPSGSystemEnclosureEntry = _IBMPSGSystemEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1)
)
iBMPSGSystemEnclosureEntry.setIndexNames(
    (0, "UMSLMSENSOR-MIB", "iBMPSGSystemEnclosureKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureEntry.setStatus("mandatory")
_IBMPSGSystemEnclosureKeyIndex_Type = String
_IBMPSGSystemEnclosureKeyIndex_Object = MibTableColumn
iBMPSGSystemEnclosureKeyIndex = _IBMPSGSystemEnclosureKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 1),
    _IBMPSGSystemEnclosureKeyIndex_Type()
)
iBMPSGSystemEnclosureKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureKeyIndex.setStatus("mandatory")
_IBMPSGSystemEnclosureIntrusionStatus_Type = Uint32
_IBMPSGSystemEnclosureIntrusionStatus_Object = MibTableColumn
iBMPSGSystemEnclosureIntrusionStatus = _IBMPSGSystemEnclosureIntrusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 2),
    _IBMPSGSystemEnclosureIntrusionStatus_Type()
)
iBMPSGSystemEnclosureIntrusionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureIntrusionStatus.setStatus("mandatory")
_IBMPSGSystemEnclosureIntrusionType_Type = Uint32
_IBMPSGSystemEnclosureIntrusionType_Object = MibTableColumn
iBMPSGSystemEnclosureIntrusionType = _IBMPSGSystemEnclosureIntrusionType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 3),
    _IBMPSGSystemEnclosureIntrusionType_Type()
)
iBMPSGSystemEnclosureIntrusionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureIntrusionType.setStatus("mandatory")
_IBMPSGSystemEnclosureEventsEnabled_Type = Boolean
_IBMPSGSystemEnclosureEventsEnabled_Object = MibTableColumn
iBMPSGSystemEnclosureEventsEnabled = _IBMPSGSystemEnclosureEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 4),
    _IBMPSGSystemEnclosureEventsEnabled_Type()
)
iBMPSGSystemEnclosureEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureEventsEnabled.setStatus("mandatory")
_IBMPSGSystemEnclosurePollingInterval_Type = Uint32
_IBMPSGSystemEnclosurePollingInterval_Object = MibTableColumn
iBMPSGSystemEnclosurePollingInterval = _IBMPSGSystemEnclosurePollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 5),
    _IBMPSGSystemEnclosurePollingInterval_Type()
)
iBMPSGSystemEnclosurePollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosurePollingInterval.setStatus("mandatory")
_IBMPSGSystemEnclosureDockingStatus_Type = Uint16
_IBMPSGSystemEnclosureDockingStatus_Object = MibTableColumn
iBMPSGSystemEnclosureDockingStatus = _IBMPSGSystemEnclosureDockingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 6),
    _IBMPSGSystemEnclosureDockingStatus_Type()
)
iBMPSGSystemEnclosureDockingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureDockingStatus.setStatus("mandatory")
_IBMPSGSystemEnclosureACLineStatus_Type = Uint16
_IBMPSGSystemEnclosureACLineStatus_Object = MibTableColumn
iBMPSGSystemEnclosureACLineStatus = _IBMPSGSystemEnclosureACLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 7),
    _IBMPSGSystemEnclosureACLineStatus_Type()
)
iBMPSGSystemEnclosureACLineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureACLineStatus.setStatus("mandatory")
_IBMPSGSystemEnclosureEventAutoClearEnabled_Type = Boolean
_IBMPSGSystemEnclosureEventAutoClearEnabled_Object = MibTableColumn
iBMPSGSystemEnclosureEventAutoClearEnabled = _IBMPSGSystemEnclosureEventAutoClearEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 8),
    _IBMPSGSystemEnclosureEventAutoClearEnabled_Type()
)
iBMPSGSystemEnclosureEventAutoClearEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureEventAutoClearEnabled.setStatus("mandatory")
_IBMPSGSystemEnclosureStatus_Type = String
_IBMPSGSystemEnclosureStatus_Object = MibTableColumn
iBMPSGSystemEnclosureStatus = _IBMPSGSystemEnclosureStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 4, 1, 9),
    _IBMPSGSystemEnclosureStatus_Type()
)
iBMPSGSystemEnclosureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGSystemEnclosureStatus.setStatus("mandatory")
_IBMPSGTachometerTable_Object = MibTable
iBMPSGTachometerTable = _IBMPSGTachometerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5)
)
if mibBuilder.loadTexts:
    iBMPSGTachometerTable.setStatus("mandatory")
_IBMPSGTachometerEntry_Object = MibTableRow
iBMPSGTachometerEntry = _IBMPSGTachometerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1)
)
iBMPSGTachometerEntry.setIndexNames(
    (0, "UMSLMSENSOR-MIB", "iBMPSGTachometerKeyIndex"),
)
if mibBuilder.loadTexts:
    iBMPSGTachometerEntry.setStatus("mandatory")
_IBMPSGTachometerKeyIndex_Type = String
_IBMPSGTachometerKeyIndex_Object = MibTableColumn
iBMPSGTachometerKeyIndex = _IBMPSGTachometerKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 1),
    _IBMPSGTachometerKeyIndex_Type()
)
iBMPSGTachometerKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerKeyIndex.setStatus("mandatory")
_IBMPSGTachometerCurrentReading_Type = Sint32
_IBMPSGTachometerCurrentReading_Object = MibTableColumn
iBMPSGTachometerCurrentReading = _IBMPSGTachometerCurrentReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 2),
    _IBMPSGTachometerCurrentReading_Type()
)
iBMPSGTachometerCurrentReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerCurrentReading.setStatus("mandatory")
_IBMPSGTachometerNominalReading_Type = Sint32
_IBMPSGTachometerNominalReading_Object = MibTableColumn
iBMPSGTachometerNominalReading = _IBMPSGTachometerNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 3),
    _IBMPSGTachometerNominalReading_Type()
)
iBMPSGTachometerNominalReading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerNominalReading.setStatus("mandatory")
_IBMPSGTachometerNormalMax_Type = Sint32
_IBMPSGTachometerNormalMax_Object = MibTableColumn
iBMPSGTachometerNormalMax = _IBMPSGTachometerNormalMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 4),
    _IBMPSGTachometerNormalMax_Type()
)
iBMPSGTachometerNormalMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerNormalMax.setStatus("mandatory")
_IBMPSGTachometerNormalMin_Type = Sint32
_IBMPSGTachometerNormalMin_Object = MibTableColumn
iBMPSGTachometerNormalMin = _IBMPSGTachometerNormalMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 5),
    _IBMPSGTachometerNormalMin_Type()
)
iBMPSGTachometerNormalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerNormalMin.setStatus("mandatory")
_IBMPSGTachometerMaxReadable_Type = Sint32
_IBMPSGTachometerMaxReadable_Object = MibTableColumn
iBMPSGTachometerMaxReadable = _IBMPSGTachometerMaxReadable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 6),
    _IBMPSGTachometerMaxReadable_Type()
)
iBMPSGTachometerMaxReadable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerMaxReadable.setStatus("mandatory")
_IBMPSGTachometerMinReadable_Type = Sint32
_IBMPSGTachometerMinReadable_Object = MibTableColumn
iBMPSGTachometerMinReadable = _IBMPSGTachometerMinReadable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 7),
    _IBMPSGTachometerMinReadable_Type()
)
iBMPSGTachometerMinReadable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerMinReadable.setStatus("mandatory")
_IBMPSGTachometerResolution_Type = Uint32
_IBMPSGTachometerResolution_Object = MibTableColumn
iBMPSGTachometerResolution = _IBMPSGTachometerResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 8),
    _IBMPSGTachometerResolution_Type()
)
iBMPSGTachometerResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerResolution.setStatus("mandatory")
_IBMPSGTachometerTolerance_Type = Sint32
_IBMPSGTachometerTolerance_Object = MibTableColumn
iBMPSGTachometerTolerance = _IBMPSGTachometerTolerance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 9),
    _IBMPSGTachometerTolerance_Type()
)
iBMPSGTachometerTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerTolerance.setStatus("mandatory")
_IBMPSGTachometerLowerThresholdNonCritical_Type = Sint32
_IBMPSGTachometerLowerThresholdNonCritical_Object = MibTableColumn
iBMPSGTachometerLowerThresholdNonCritical = _IBMPSGTachometerLowerThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 10),
    _IBMPSGTachometerLowerThresholdNonCritical_Type()
)
iBMPSGTachometerLowerThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerLowerThresholdNonCritical.setStatus("mandatory")
_IBMPSGTachometerUpperThresholdNonCritical_Type = Sint32
_IBMPSGTachometerUpperThresholdNonCritical_Object = MibTableColumn
iBMPSGTachometerUpperThresholdNonCritical = _IBMPSGTachometerUpperThresholdNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 11),
    _IBMPSGTachometerUpperThresholdNonCritical_Type()
)
iBMPSGTachometerUpperThresholdNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerUpperThresholdNonCritical.setStatus("mandatory")
_IBMPSGTachometerLowerThresholdCritical_Type = Sint32
_IBMPSGTachometerLowerThresholdCritical_Object = MibTableColumn
iBMPSGTachometerLowerThresholdCritical = _IBMPSGTachometerLowerThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 12),
    _IBMPSGTachometerLowerThresholdCritical_Type()
)
iBMPSGTachometerLowerThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerLowerThresholdCritical.setStatus("mandatory")
_IBMPSGTachometerUpperThresholdCritical_Type = Sint32
_IBMPSGTachometerUpperThresholdCritical_Object = MibTableColumn
iBMPSGTachometerUpperThresholdCritical = _IBMPSGTachometerUpperThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 13),
    _IBMPSGTachometerUpperThresholdCritical_Type()
)
iBMPSGTachometerUpperThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerUpperThresholdCritical.setStatus("mandatory")
_IBMPSGTachometerLowerThresholdFatal_Type = Sint32
_IBMPSGTachometerLowerThresholdFatal_Object = MibTableColumn
iBMPSGTachometerLowerThresholdFatal = _IBMPSGTachometerLowerThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 14),
    _IBMPSGTachometerLowerThresholdFatal_Type()
)
iBMPSGTachometerLowerThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerLowerThresholdFatal.setStatus("mandatory")
_IBMPSGTachometerUpperThresholdFatal_Type = Sint32
_IBMPSGTachometerUpperThresholdFatal_Object = MibTableColumn
iBMPSGTachometerUpperThresholdFatal = _IBMPSGTachometerUpperThresholdFatal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 15),
    _IBMPSGTachometerUpperThresholdFatal_Type()
)
iBMPSGTachometerUpperThresholdFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerUpperThresholdFatal.setStatus("mandatory")
_IBMPSGTachometerFanDescrip_Type = Uint32
_IBMPSGTachometerFanDescrip_Object = MibTableColumn
iBMPSGTachometerFanDescrip = _IBMPSGTachometerFanDescrip_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 16),
    _IBMPSGTachometerFanDescrip_Type()
)
iBMPSGTachometerFanDescrip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerFanDescrip.setStatus("mandatory")
_IBMPSGTachometerFanType_Type = Uint32
_IBMPSGTachometerFanType_Object = MibTableColumn
iBMPSGTachometerFanType = _IBMPSGTachometerFanType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 17),
    _IBMPSGTachometerFanType_Type()
)
iBMPSGTachometerFanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerFanType.setStatus("mandatory")
_IBMPSGTachometerEventsEnabled_Type = Boolean
_IBMPSGTachometerEventsEnabled_Object = MibTableColumn
iBMPSGTachometerEventsEnabled = _IBMPSGTachometerEventsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 18),
    _IBMPSGTachometerEventsEnabled_Type()
)
iBMPSGTachometerEventsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerEventsEnabled.setStatus("mandatory")
_IBMPSGTachometerEventAutoClearEnabled_Type = Boolean
_IBMPSGTachometerEventAutoClearEnabled_Object = MibTableColumn
iBMPSGTachometerEventAutoClearEnabled = _IBMPSGTachometerEventAutoClearEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 19),
    _IBMPSGTachometerEventAutoClearEnabled_Type()
)
iBMPSGTachometerEventAutoClearEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerEventAutoClearEnabled.setStatus("mandatory")
_IBMPSGTachometerStatus_Type = String
_IBMPSGTachometerStatus_Object = MibTableColumn
iBMPSGTachometerStatus = _IBMPSGTachometerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 159, 1, 1, 80, 5, 1, 20),
    _IBMPSGTachometerStatus_Type()
)
iBMPSGTachometerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iBMPSGTachometerStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UMSLMSENSOR-MIB",
    **{"iBMPSGTemperatureSensorTable": iBMPSGTemperatureSensorTable,
       "iBMPSGTemperatureSensorEntry": iBMPSGTemperatureSensorEntry,
       "iBMPSGTemperatureSensorKeyIndex": iBMPSGTemperatureSensorKeyIndex,
       "iBMPSGTemperatureSensorCurrentReading": iBMPSGTemperatureSensorCurrentReading,
       "iBMPSGTemperatureSensorNominalReading": iBMPSGTemperatureSensorNominalReading,
       "iBMPSGTemperatureSensorNormalMax": iBMPSGTemperatureSensorNormalMax,
       "iBMPSGTemperatureSensorNormalMin": iBMPSGTemperatureSensorNormalMin,
       "iBMPSGTemperatureSensorMaxReadable": iBMPSGTemperatureSensorMaxReadable,
       "iBMPSGTemperatureSensorMinReadable": iBMPSGTemperatureSensorMinReadable,
       "iBMPSGTemperatureSensorResolution": iBMPSGTemperatureSensorResolution,
       "iBMPSGTemperatureSensorTolerance": iBMPSGTemperatureSensorTolerance,
       "iBMPSGTemperatureSensorAccuracy": iBMPSGTemperatureSensorAccuracy,
       "iBMPSGTemperatureSensorLowerThresholdNonCritical": iBMPSGTemperatureSensorLowerThresholdNonCritical,
       "iBMPSGTemperatureSensorUpperThresholdNonCritical": iBMPSGTemperatureSensorUpperThresholdNonCritical,
       "iBMPSGTemperatureSensorLowerThresholdCritical": iBMPSGTemperatureSensorLowerThresholdCritical,
       "iBMPSGTemperatureSensorUpperThresholdCritical": iBMPSGTemperatureSensorUpperThresholdCritical,
       "iBMPSGTemperatureSensorLowerThresholdFatal": iBMPSGTemperatureSensorLowerThresholdFatal,
       "iBMPSGTemperatureSensorUpperThresholdFatal": iBMPSGTemperatureSensorUpperThresholdFatal,
       "iBMPSGTemperatureSensorTempLocation": iBMPSGTemperatureSensorTempLocation,
       "iBMPSGTemperatureSensorEventsEnabled": iBMPSGTemperatureSensorEventsEnabled,
       "iBMPSGTemperatureSensorPollingInterval": iBMPSGTemperatureSensorPollingInterval,
       "iBMPSGTemperatureSensorEventAutoClearEnabled": iBMPSGTemperatureSensorEventAutoClearEnabled,
       "iBMPSGTemperatureSensorStatus": iBMPSGTemperatureSensorStatus,
       "iBMPSGVoltageSensorTable": iBMPSGVoltageSensorTable,
       "iBMPSGVoltageSensorEntry": iBMPSGVoltageSensorEntry,
       "iBMPSGVoltageSensorKeyIndex": iBMPSGVoltageSensorKeyIndex,
       "iBMPSGVoltageSensorCurrentReading": iBMPSGVoltageSensorCurrentReading,
       "iBMPSGVoltageSensorNominalReading": iBMPSGVoltageSensorNominalReading,
       "iBMPSGVoltageSensorNormalMax": iBMPSGVoltageSensorNormalMax,
       "iBMPSGVoltageSensorNormalMin": iBMPSGVoltageSensorNormalMin,
       "iBMPSGVoltageSensorMaxReadable": iBMPSGVoltageSensorMaxReadable,
       "iBMPSGVoltageSensorMinReadable": iBMPSGVoltageSensorMinReadable,
       "iBMPSGVoltageSensorResolution": iBMPSGVoltageSensorResolution,
       "iBMPSGVoltageSensorTolerance": iBMPSGVoltageSensorTolerance,
       "iBMPSGVoltageSensorAccuracy": iBMPSGVoltageSensorAccuracy,
       "iBMPSGVoltageSensorLowerThresholdNonCritical": iBMPSGVoltageSensorLowerThresholdNonCritical,
       "iBMPSGVoltageSensorUpperThresholdNonCritical": iBMPSGVoltageSensorUpperThresholdNonCritical,
       "iBMPSGVoltageSensorLowerThresholdCritical": iBMPSGVoltageSensorLowerThresholdCritical,
       "iBMPSGVoltageSensorUpperThresholdCritical": iBMPSGVoltageSensorUpperThresholdCritical,
       "iBMPSGVoltageSensorLowerThresholdFatal": iBMPSGVoltageSensorLowerThresholdFatal,
       "iBMPSGVoltageSensorUpperThresholdFatal": iBMPSGVoltageSensorUpperThresholdFatal,
       "iBMPSGVoltageSensorVoltageType": iBMPSGVoltageSensorVoltageType,
       "iBMPSGVoltageSensorEventsEnabled": iBMPSGVoltageSensorEventsEnabled,
       "iBMPSGVoltageSensorPollingInterval": iBMPSGVoltageSensorPollingInterval,
       "iBMPSGVoltageSensorEventAutoClearEnabled": iBMPSGVoltageSensorEventAutoClearEnabled,
       "iBMPSGVoltageSensorStatus": iBMPSGVoltageSensorStatus,
       "iBMPSGFanTable": iBMPSGFanTable,
       "iBMPSGFanEntry": iBMPSGFanEntry,
       "iBMPSGFanKeyIndex": iBMPSGFanKeyIndex,
       "iBMPSGFanVariableSpeed": iBMPSGFanVariableSpeed,
       "iBMPSGFanDesiredSpeed": iBMPSGFanDesiredSpeed,
       "iBMPSGFanActiveCooling": iBMPSGFanActiveCooling,
       "iBMPSGFanFanType": iBMPSGFanFanType,
       "iBMPSGFanEventsEnabled": iBMPSGFanEventsEnabled,
       "iBMPSGFanPollingInterval": iBMPSGFanPollingInterval,
       "iBMPSGFanEventAutoClearEnabled": iBMPSGFanEventAutoClearEnabled,
       "iBMPSGFanStatus": iBMPSGFanStatus,
       "iBMPSGSystemEnclosureTable": iBMPSGSystemEnclosureTable,
       "iBMPSGSystemEnclosureEntry": iBMPSGSystemEnclosureEntry,
       "iBMPSGSystemEnclosureKeyIndex": iBMPSGSystemEnclosureKeyIndex,
       "iBMPSGSystemEnclosureIntrusionStatus": iBMPSGSystemEnclosureIntrusionStatus,
       "iBMPSGSystemEnclosureIntrusionType": iBMPSGSystemEnclosureIntrusionType,
       "iBMPSGSystemEnclosureEventsEnabled": iBMPSGSystemEnclosureEventsEnabled,
       "iBMPSGSystemEnclosurePollingInterval": iBMPSGSystemEnclosurePollingInterval,
       "iBMPSGSystemEnclosureDockingStatus": iBMPSGSystemEnclosureDockingStatus,
       "iBMPSGSystemEnclosureACLineStatus": iBMPSGSystemEnclosureACLineStatus,
       "iBMPSGSystemEnclosureEventAutoClearEnabled": iBMPSGSystemEnclosureEventAutoClearEnabled,
       "iBMPSGSystemEnclosureStatus": iBMPSGSystemEnclosureStatus,
       "iBMPSGTachometerTable": iBMPSGTachometerTable,
       "iBMPSGTachometerEntry": iBMPSGTachometerEntry,
       "iBMPSGTachometerKeyIndex": iBMPSGTachometerKeyIndex,
       "iBMPSGTachometerCurrentReading": iBMPSGTachometerCurrentReading,
       "iBMPSGTachometerNominalReading": iBMPSGTachometerNominalReading,
       "iBMPSGTachometerNormalMax": iBMPSGTachometerNormalMax,
       "iBMPSGTachometerNormalMin": iBMPSGTachometerNormalMin,
       "iBMPSGTachometerMaxReadable": iBMPSGTachometerMaxReadable,
       "iBMPSGTachometerMinReadable": iBMPSGTachometerMinReadable,
       "iBMPSGTachometerResolution": iBMPSGTachometerResolution,
       "iBMPSGTachometerTolerance": iBMPSGTachometerTolerance,
       "iBMPSGTachometerLowerThresholdNonCritical": iBMPSGTachometerLowerThresholdNonCritical,
       "iBMPSGTachometerUpperThresholdNonCritical": iBMPSGTachometerUpperThresholdNonCritical,
       "iBMPSGTachometerLowerThresholdCritical": iBMPSGTachometerLowerThresholdCritical,
       "iBMPSGTachometerUpperThresholdCritical": iBMPSGTachometerUpperThresholdCritical,
       "iBMPSGTachometerLowerThresholdFatal": iBMPSGTachometerLowerThresholdFatal,
       "iBMPSGTachometerUpperThresholdFatal": iBMPSGTachometerUpperThresholdFatal,
       "iBMPSGTachometerFanDescrip": iBMPSGTachometerFanDescrip,
       "iBMPSGTachometerFanType": iBMPSGTachometerFanType,
       "iBMPSGTachometerEventsEnabled": iBMPSGTachometerEventsEnabled,
       "iBMPSGTachometerEventAutoClearEnabled": iBMPSGTachometerEventAutoClearEnabled,
       "iBMPSGTachometerStatus": iBMPSGTachometerStatus}
)
