# SNMP MIB module (TRIPPUPS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRIPPUPS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:49 2024
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

_Tripplite_ObjectIdentity = ObjectIdentity
tripplite = _Tripplite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850)
)
_TrippUPS1_ObjectIdentity = ObjectIdentity
trippUPS1 = _TrippUPS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1)
)


class _UpsIdentManufacturer_Type(DisplayString):
    """Custom type upsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentManufacturer_Type.__name__ = "DisplayString"
_UpsIdentManufacturer_Object = MibScalar
upsIdentManufacturer = _UpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 1),
    _UpsIdentManufacturer_Type()
)
upsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturer.setStatus("mandatory")


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 2),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("mandatory")


class _UpsIdentUPSSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentUPSSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentUPSSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentUPSSoftwareVersion_Object = MibScalar
upsIdentUPSSoftwareVersion = _UpsIdentUPSSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 3),
    _UpsIdentUPSSoftwareVersion_Type()
)
upsIdentUPSSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersion.setStatus("mandatory")


class _UpsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentAgentSoftwareVersion_Object = MibScalar
upsIdentAgentSoftwareVersion = _UpsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 4),
    _UpsIdentAgentSoftwareVersion_Type()
)
upsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersion.setStatus("mandatory")


class _UpsIdentName_Type(DisplayString):
    """Custom type upsIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentName_Type.__name__ = "DisplayString"
_UpsIdentName_Object = MibScalar
upsIdentName = _UpsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 5),
    _UpsIdentName_Type()
)
upsIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentName.setStatus("mandatory")


class _UpsIdentAttachedDevices_Type(DisplayString):
    """Custom type upsIdentAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentAttachedDevices_Type.__name__ = "DisplayString"
_UpsIdentAttachedDevices_Object = MibScalar
upsIdentAttachedDevices = _UpsIdentAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 1, 6),
    _UpsIdentAttachedDevices_Type()
)
upsIdentAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevices.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2)
)


class _UpsBatteryStatus_Type(Integer32):
    """Custom type upsBatteryStatus based on Integer32"""
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


_UpsBatteryStatus_Type.__name__ = "Integer32"
_UpsBatteryStatus_Object = MibScalar
upsBatteryStatus = _UpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("mandatory")
_UpsSecondsOnBattery_Type = Integer32
_UpsSecondsOnBattery_Object = MibScalar
upsSecondsOnBattery = _UpsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 2),
    _UpsSecondsOnBattery_Type()
)
upsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBattery.setStatus("mandatory")
_UpsEstimatedMinutesRemaining_Type = Integer32
_UpsEstimatedMinutesRemaining_Object = MibScalar
upsEstimatedMinutesRemaining = _UpsEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 3),
    _UpsEstimatedMinutesRemaining_Type()
)
upsEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemaining.setStatus("mandatory")


class _UpsBatteryChargeRemaining_Type(Integer32):
    """Custom type upsBatteryChargeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsBatteryChargeRemaining_Type.__name__ = "Integer32"
_UpsBatteryChargeRemaining_Object = MibScalar
upsBatteryChargeRemaining = _UpsBatteryChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 4),
    _UpsBatteryChargeRemaining_Type()
)
upsBatteryChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryChargeRemaining.setStatus("mandatory")
_UpsBatteryVoltage_Type = Integer32
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 5),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("mandatory")
_UpsBatteryTemperature_Type = Integer32
_UpsBatteryTemperature_Object = MibScalar
upsBatteryTemperature = _UpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 2, 7),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3)
)
_UpsInputFrequency_Type = Integer32
_UpsInputFrequency_Object = MibScalar
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 1),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
_UpsInputLineBads_Type = Counter32
_UpsInputLineBads_Object = MibScalar
upsInputLineBads = _UpsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 2),
    _UpsInputLineBads_Type()
)
upsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBads.setStatus("mandatory")
_UpsInputNumLines_Type = Integer32
_UpsInputNumLines_Object = MibScalar
upsInputNumLines = _UpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 3),
    _UpsInputNumLines_Type()
)
upsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLines.setStatus("mandatory")
_UpsInputVolt_Type = Integer32
_UpsInputVolt_Object = MibScalar
upsInputVolt = _UpsInputVolt_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 4),
    _UpsInputVolt_Type()
)
upsInputVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVolt.setStatus("mandatory")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("mandatory")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 1)
)
upsInputEntry.setIndexNames(
    (0, "TRIPPUPS1-MIB", "upsInputLineIndex"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("mandatory")
_UpsInputLineIndex_Type = Integer32
_UpsInputLineIndex_Object = MibTableColumn
upsInputLineIndex = _UpsInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 1, 1),
    _UpsInputLineIndex_Type()
)
upsInputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineIndex.setStatus("mandatory")
_UpsInputVoltage_Type = Integer32
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 3, 5, 1, 2),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4)
)


class _UpsOutputSource_Type(Integer32):
    """Custom type upsOutputSource based on Integer32"""
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


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 1),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("mandatory")
_UpsOutputFrequency_Type = Integer32
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("mandatory")
_UpsOutputNumLines_Type = Integer32
_UpsOutputNumLines_Object = MibScalar
upsOutputNumLines = _UpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 3),
    _UpsOutputNumLines_Type()
)
upsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLines.setStatus("mandatory")
_UpsOutputPercLoad_Type = Integer32
_UpsOutputPercLoad_Object = MibScalar
upsOutputPercLoad = _UpsOutputPercLoad_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 4),
    _UpsOutputPercLoad_Type()
)
upsOutputPercLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercLoad.setStatus("mandatory")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("mandatory")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 5, 1)
)
upsOutputEntry.setIndexNames(
    (0, "TRIPPUPS1-MIB", "upsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("mandatory")
_UpsOutputLineIndex_Type = Integer32
_UpsOutputLineIndex_Object = MibTableColumn
upsOutputLineIndex = _UpsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 5, 1, 1),
    _UpsOutputLineIndex_Type()
)
upsOutputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLineIndex.setStatus("mandatory")
_UpsOutputVoltage_Type = Integer32
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 5, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("mandatory")
_UpsOutputCurrent_Type = Integer32
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 5, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("mandatory")
_UpsOutputPower_Type = Integer32
_UpsOutputPower_Object = MibTableColumn
upsOutputPower = _UpsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 5, 1, 4),
    _UpsOutputPower_Type()
)
upsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPower.setStatus("mandatory")
_UpsOutputPercentLoad_Type = Integer32
_UpsOutputPercentLoad_Object = MibTableColumn
upsOutputPercentLoad = _UpsOutputPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 4, 5, 1, 5),
    _UpsOutputPercentLoad_Type()
)
upsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setStatus("mandatory")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6)
)
_UpsAlarmsPresent_Type = Gauge32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("mandatory")


class _UpsAlarmID_Type(Integer32):
    """Custom type upsAlarmID based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("upsAlarmBatteryBad", 1),
          ("upsAlarmCommunicationsLost", 10),
          ("upsAlarmDepletedBattery", 4),
          ("upsAlarmDiagnosticTestFailed", 9),
          ("upsAlarmLowBattery", 3),
          ("upsAlarmOnBattery", 2),
          ("upsAlarmOutputOff", 8),
          ("upsAlarmOutputOffAsRequested", 7),
          ("upsAlarmOutputOverload", 6),
          ("upsAlarmShutdownImminent", 12),
          ("upsAlarmShutdownPending", 11),
          ("upsAlarmTempBad", 5),
          ("upsAlarmTestInProgress", 13))
    )


_UpsAlarmID_Type.__name__ = "Integer32"
_UpsAlarmID_Object = MibScalar
upsAlarmID = _UpsAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 2),
    _UpsAlarmID_Type()
)
upsAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmID.setStatus("mandatory")


class _UpsAlarmDESCR_Type(DisplayString):
    """Custom type upsAlarmDESCR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsAlarmDESCR_Type.__name__ = "DisplayString"
_UpsAlarmDESCR_Object = MibScalar
upsAlarmDESCR = _UpsAlarmDESCR_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 3),
    _UpsAlarmDESCR_Type()
)
upsAlarmDESCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDESCR.setStatus("mandatory")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("mandatory")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 4, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "TRIPPUPS1-MIB", "upsAlarmId"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("mandatory")
_UpsAlarmId_Type = Integer32
_UpsAlarmId_Object = MibTableColumn
upsAlarmId = _UpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 4, 1, 1),
    _UpsAlarmId_Type()
)
upsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmId.setStatus("mandatory")


class _UpsAlarmDescr_Type(DisplayString):
    """Custom type upsAlarmDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsAlarmDescr_Type.__name__ = "DisplayString"
_UpsAlarmDescr_Object = MibTableColumn
upsAlarmDescr = _UpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 4, 1, 2),
    _UpsAlarmDescr_Type()
)
upsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescr.setStatus("mandatory")
_UpsAlarmTime_Type = TimeTicks
_UpsAlarmTime_Object = MibTableColumn
upsAlarmTime = _UpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 6, 4, 1, 3),
    _UpsAlarmTime_Type()
)
upsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTime.setStatus("mandatory")
_UpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
upsWellKnownAlarms = _UpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7)
)
_UpsAlarmBatteryBad_Type = Integer32
_UpsAlarmBatteryBad_Object = MibScalar
upsAlarmBatteryBad = _UpsAlarmBatteryBad_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 1),
    _UpsAlarmBatteryBad_Type()
)
upsAlarmBatteryBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryBad.setStatus("mandatory")
_UpsAlarmOnBattery_Type = Integer32
_UpsAlarmOnBattery_Object = MibScalar
upsAlarmOnBattery = _UpsAlarmOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 2),
    _UpsAlarmOnBattery_Type()
)
upsAlarmOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBattery.setStatus("mandatory")
_UpsAlarmLowBattery_Type = Integer32
_UpsAlarmLowBattery_Object = MibScalar
upsAlarmLowBattery = _UpsAlarmLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 3),
    _UpsAlarmLowBattery_Type()
)
upsAlarmLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmLowBattery.setStatus("mandatory")
_UpsAlarmDepletedBattery_Type = Integer32
_UpsAlarmDepletedBattery_Object = MibScalar
upsAlarmDepletedBattery = _UpsAlarmDepletedBattery_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 4),
    _UpsAlarmDepletedBattery_Type()
)
upsAlarmDepletedBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDepletedBattery.setStatus("mandatory")
_UpsAlarmTempBad_Type = Integer32
_UpsAlarmTempBad_Object = MibScalar
upsAlarmTempBad = _UpsAlarmTempBad_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 5),
    _UpsAlarmTempBad_Type()
)
upsAlarmTempBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTempBad.setStatus("mandatory")
_UpsAlarmOutputOverload_Type = Integer32
_UpsAlarmOutputOverload_Object = MibScalar
upsAlarmOutputOverload = _UpsAlarmOutputOverload_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 6),
    _UpsAlarmOutputOverload_Type()
)
upsAlarmOutputOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOverload.setStatus("mandatory")
_UpsAlarmOutputOffAsRequested_Type = Integer32
_UpsAlarmOutputOffAsRequested_Object = MibScalar
upsAlarmOutputOffAsRequested = _UpsAlarmOutputOffAsRequested_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 7),
    _UpsAlarmOutputOffAsRequested_Type()
)
upsAlarmOutputOffAsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequested.setStatus("mandatory")
_UpsAlarmUpsOutputOff_Type = Integer32
_UpsAlarmUpsOutputOff_Object = MibScalar
upsAlarmUpsOutputOff = _UpsAlarmUpsOutputOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 8),
    _UpsAlarmUpsOutputOff_Type()
)
upsAlarmUpsOutputOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOff.setStatus("mandatory")
_UpsAlarmDiagnosticTestFailed_Type = Integer32
_UpsAlarmDiagnosticTestFailed_Object = MibScalar
upsAlarmDiagnosticTestFailed = _UpsAlarmDiagnosticTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 9),
    _UpsAlarmDiagnosticTestFailed_Type()
)
upsAlarmDiagnosticTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailed.setStatus("mandatory")
_UpsAlarmCommunicationsLost_Type = Integer32
_UpsAlarmCommunicationsLost_Object = MibScalar
upsAlarmCommunicationsLost = _UpsAlarmCommunicationsLost_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 10),
    _UpsAlarmCommunicationsLost_Type()
)
upsAlarmCommunicationsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLost.setStatus("mandatory")
_UpsAlarmShutdownPending_Type = Integer32
_UpsAlarmShutdownPending_Object = MibScalar
upsAlarmShutdownPending = _UpsAlarmShutdownPending_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 11),
    _UpsAlarmShutdownPending_Type()
)
upsAlarmShutdownPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShutdownPending.setStatus("mandatory")
_UpsAlarmShutdownImminent_Type = Integer32
_UpsAlarmShutdownImminent_Object = MibScalar
upsAlarmShutdownImminent = _UpsAlarmShutdownImminent_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 12),
    _UpsAlarmShutdownImminent_Type()
)
upsAlarmShutdownImminent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShutdownImminent.setStatus("mandatory")
_UpsAlarmTestInProgress_Type = Integer32
_UpsAlarmTestInProgress_Object = MibScalar
upsAlarmTestInProgress = _UpsAlarmTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 7, 13),
    _UpsAlarmTestInProgress_Type()
)
upsAlarmTestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTestInProgress.setStatus("mandatory")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 8)
)


class _UpsTestId_Type(Integer32):
    """Custom type upsTestId based on Integer32"""
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
        *(("abortTestInProgress", 2),
          ("checkBatteryTest", 4),
          ("deepBatteryCalibration", 5),
          ("generalSystemsTest", 3),
          ("noTestsInitiated", 1))
    )


_UpsTestId_Type.__name__ = "Integer32"
_UpsTestId_Object = MibScalar
upsTestId = _UpsTestId_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 8, 1),
    _UpsTestId_Type()
)
upsTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestId.setStatus("mandatory")


class _UpsTestResultsSummary_Type(Integer32):
    """Custom type upsTestResultsSummary based on Integer32"""
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
        *(("aborted", 4),
          ("doneError", 3),
          ("donePass", 1),
          ("doneWarning", 2),
          ("inProgress", 5),
          ("noTestsInitiated", 6))
    )


_UpsTestResultsSummary_Type.__name__ = "Integer32"
_UpsTestResultsSummary_Object = MibScalar
upsTestResultsSummary = _UpsTestResultsSummary_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 8, 2),
    _UpsTestResultsSummary_Type()
)
upsTestResultsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummary.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 9)
)


class _UpsShutdownType_Type(Integer32):
    """Custom type upsShutdownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("output", 1),
          ("system", 2))
    )


_UpsShutdownType_Type.__name__ = "Integer32"
_UpsShutdownType_Object = MibScalar
upsShutdownType = _UpsShutdownType_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 9, 1),
    _UpsShutdownType_Type()
)
upsShutdownType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownType.setStatus("mandatory")


class _UpsShutdownAfterDelay_Type(Integer32):
    """Custom type upsShutdownAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_UpsShutdownAfterDelay_Type.__name__ = "Integer32"
_UpsShutdownAfterDelay_Object = MibScalar
upsShutdownAfterDelay = _UpsShutdownAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 9, 2),
    _UpsShutdownAfterDelay_Type()
)
upsShutdownAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelay.setStatus("mandatory")


class _UpsStartupAfterDelay_Type(Integer32):
    """Custom type upsStartupAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_UpsStartupAfterDelay_Type.__name__ = "Integer32"
_UpsStartupAfterDelay_Object = MibScalar
upsStartupAfterDelay = _UpsStartupAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 9, 3),
    _UpsStartupAfterDelay_Type()
)
upsStartupAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelay.setStatus("mandatory")


class _UpsRebootDuration_Type(Integer32):
    """Custom type upsRebootDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_UpsRebootDuration_Type.__name__ = "Integer32"
_UpsRebootDuration_Object = MibScalar
upsRebootDuration = _UpsRebootDuration_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 9, 4),
    _UpsRebootDuration_Type()
)
upsRebootDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootDuration.setStatus("mandatory")


class _UpsAutoRestart_Type(Integer32):
    """Custom type upsAutoRestart based on Integer32"""
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


_UpsAutoRestart_Type.__name__ = "Integer32"
_UpsAutoRestart_Object = MibScalar
upsAutoRestart = _UpsAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 9, 5),
    _UpsAutoRestart_Type()
)
upsAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestart.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 10)
)
_UpsConfigInputVoltageHigh_Type = Integer32
_UpsConfigInputVoltageHigh_Object = MibScalar
upsConfigInputVoltageHigh = _UpsConfigInputVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 10, 11),
    _UpsConfigInputVoltageHigh_Type()
)
upsConfigInputVoltageHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltageHigh.setStatus("mandatory")
_UpsConfigInputVoltageLow_Type = Integer32
_UpsConfigInputVoltageLow_Object = MibScalar
upsConfigInputVoltageLow = _UpsConfigInputVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 10, 12),
    _UpsConfigInputVoltageLow_Type()
)
upsConfigInputVoltageLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltageLow.setStatus("mandatory")
_UpsConfigOutputPercLoadHigh_Type = Integer32
_UpsConfigOutputPercLoadHigh_Object = MibScalar
upsConfigOutputPercLoadHigh = _UpsConfigOutputPercLoadHigh_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 10, 13),
    _UpsConfigOutputPercLoadHigh_Type()
)
upsConfigOutputPercLoadHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputPercLoadHigh.setStatus("mandatory")
_UpsConfigBatteryPercLow_Type = Integer32
_UpsConfigBatteryPercLow_Object = MibScalar
upsConfigBatteryPercLow = _UpsConfigBatteryPercLow_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 10, 14),
    _UpsConfigBatteryPercLow_Type()
)
upsConfigBatteryPercLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryPercLow.setStatus("mandatory")
_UpsConfigBatteryTemperatureHigh_Type = Integer32
_UpsConfigBatteryTemperatureHigh_Object = MibScalar
upsConfigBatteryTemperatureHigh = _UpsConfigBatteryTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 850, 1, 1, 10, 15),
    _UpsConfigBatteryTemperatureHigh_Type()
)
upsConfigBatteryTemperatureHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryTemperatureHigh.setStatus("mandatory")

# Managed Objects groups


# Notification objects

upsOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 5)
)
upsOnBattery.setObjects(
      *(("TRIPPUPS1-MIB", "upsIdentAttachedDevices"),
        ("TRIPPUPS1-MIB", "upsEstimatedMinutesRemaining"))
)
if mibBuilder.loadTexts:
    upsOnBattery.setStatus(
        ""
    )

powerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 6)
)
if mibBuilder.loadTexts:
    powerRestored.setStatus(
        ""
    )

lowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 7)
)
if mibBuilder.loadTexts:
    lowBattery.setStatus(
        ""
    )

returnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 8)
)
if mibBuilder.loadTexts:
    returnFromLowBattery.setStatus(
        ""
    )

communicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 9)
)
if mibBuilder.loadTexts:
    communicationEstablished.setStatus(
        ""
    )

communicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 10)
)
if mibBuilder.loadTexts:
    communicationLost.setStatus(
        ""
    )

upsOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 11)
)
if mibBuilder.loadTexts:
    upsOverload.setStatus(
        ""
    )

upsDiagnosticsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 12)
)
if mibBuilder.loadTexts:
    upsDiagnosticsFailed.setStatus(
        ""
    )

upsDiagnosticsPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 13)
)
if mibBuilder.loadTexts:
    upsDiagnosticsPassed.setStatus(
        ""
    )

utilityVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 14)
)
if mibBuilder.loadTexts:
    utilityVoltageHigh.setStatus(
        ""
    )

utilityVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 15)
)
if mibBuilder.loadTexts:
    utilityVoltageLow.setStatus(
        ""
    )

utilityVoltageReturnToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 16)
)
if mibBuilder.loadTexts:
    utilityVoltageReturnToNormal.setStatus(
        ""
    )

batteryTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 17)
)
if mibBuilder.loadTexts:
    batteryTemperatureHigh.setStatus(
        ""
    )

shutdownPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 18)
)
if mibBuilder.loadTexts:
    shutdownPending.setStatus(
        ""
    )

upsSleeping = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 19)
)
if mibBuilder.loadTexts:
    upsSleeping.setStatus(
        ""
    )

upsWokeup = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 20)
)
if mibBuilder.loadTexts:
    upsWokeup.setStatus(
        ""
    )

upsBatteryNeedsReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 0, 21)
)
if mibBuilder.loadTexts:
    upsBatteryNeedsReplacement.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRIPPUPS1-MIB",
    **{"tripplite": tripplite,
       "upsOnBattery": upsOnBattery,
       "powerRestored": powerRestored,
       "lowBattery": lowBattery,
       "returnFromLowBattery": returnFromLowBattery,
       "communicationEstablished": communicationEstablished,
       "communicationLost": communicationLost,
       "upsOverload": upsOverload,
       "upsDiagnosticsFailed": upsDiagnosticsFailed,
       "upsDiagnosticsPassed": upsDiagnosticsPassed,
       "utilityVoltageHigh": utilityVoltageHigh,
       "utilityVoltageLow": utilityVoltageLow,
       "utilityVoltageReturnToNormal": utilityVoltageReturnToNormal,
       "batteryTemperatureHigh": batteryTemperatureHigh,
       "shutdownPending": shutdownPending,
       "upsSleeping": upsSleeping,
       "upsWokeup": upsWokeup,
       "upsBatteryNeedsReplacement": upsBatteryNeedsReplacement,
       "trippUPS1": trippUPS1,
       "ups": ups,
       "upsIdent": upsIdent,
       "upsIdentManufacturer": upsIdentManufacturer,
       "upsIdentModel": upsIdentModel,
       "upsIdentUPSSoftwareVersion": upsIdentUPSSoftwareVersion,
       "upsIdentAgentSoftwareVersion": upsIdentAgentSoftwareVersion,
       "upsIdentName": upsIdentName,
       "upsIdentAttachedDevices": upsIdentAttachedDevices,
       "upsBattery": upsBattery,
       "upsBatteryStatus": upsBatteryStatus,
       "upsSecondsOnBattery": upsSecondsOnBattery,
       "upsEstimatedMinutesRemaining": upsEstimatedMinutesRemaining,
       "upsBatteryChargeRemaining": upsBatteryChargeRemaining,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsInput": upsInput,
       "upsInputFrequency": upsInputFrequency,
       "upsInputLineBads": upsInputLineBads,
       "upsInputNumLines": upsInputNumLines,
       "upsInputVolt": upsInputVolt,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputLineIndex": upsInputLineIndex,
       "upsInputVoltage": upsInputVoltage,
       "upsOutput": upsOutput,
       "upsOutputSource": upsOutputSource,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputNumLines": upsOutputNumLines,
       "upsOutputPercLoad": upsOutputPercLoad,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputLineIndex": upsOutputLineIndex,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputPower": upsOutputPower,
       "upsOutputPercentLoad": upsOutputPercentLoad,
       "upsAlarm": upsAlarm,
       "upsAlarmsPresent": upsAlarmsPresent,
       "upsAlarmID": upsAlarmID,
       "upsAlarmDESCR": upsAlarmDESCR,
       "upsAlarmTable": upsAlarmTable,
       "upsAlarmEntry": upsAlarmEntry,
       "upsAlarmId": upsAlarmId,
       "upsAlarmDescr": upsAlarmDescr,
       "upsAlarmTime": upsAlarmTime,
       "upsWellKnownAlarms": upsWellKnownAlarms,
       "upsAlarmBatteryBad": upsAlarmBatteryBad,
       "upsAlarmOnBattery": upsAlarmOnBattery,
       "upsAlarmLowBattery": upsAlarmLowBattery,
       "upsAlarmDepletedBattery": upsAlarmDepletedBattery,
       "upsAlarmTempBad": upsAlarmTempBad,
       "upsAlarmOutputOverload": upsAlarmOutputOverload,
       "upsAlarmOutputOffAsRequested": upsAlarmOutputOffAsRequested,
       "upsAlarmUpsOutputOff": upsAlarmUpsOutputOff,
       "upsAlarmDiagnosticTestFailed": upsAlarmDiagnosticTestFailed,
       "upsAlarmCommunicationsLost": upsAlarmCommunicationsLost,
       "upsAlarmShutdownPending": upsAlarmShutdownPending,
       "upsAlarmShutdownImminent": upsAlarmShutdownImminent,
       "upsAlarmTestInProgress": upsAlarmTestInProgress,
       "upsTest": upsTest,
       "upsTestId": upsTestId,
       "upsTestResultsSummary": upsTestResultsSummary,
       "upsControl": upsControl,
       "upsShutdownType": upsShutdownType,
       "upsShutdownAfterDelay": upsShutdownAfterDelay,
       "upsStartupAfterDelay": upsStartupAfterDelay,
       "upsRebootDuration": upsRebootDuration,
       "upsAutoRestart": upsAutoRestart,
       "upsConfig": upsConfig,
       "upsConfigInputVoltageHigh": upsConfigInputVoltageHigh,
       "upsConfigInputVoltageLow": upsConfigInputVoltageLow,
       "upsConfigOutputPercLoadHigh": upsConfigOutputPercLoadHigh,
       "upsConfigBatteryPercLow": upsConfigBatteryPercLow,
       "upsConfigBatteryTemperatureHigh": upsConfigBatteryTemperatureHigh}
)
