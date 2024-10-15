# SNMP MIB module (SOCOMECUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SOCOMECUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:31 2024
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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SocomecSicon_ObjectIdentity = ObjectIdentity
socomecSicon = _SocomecSicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1)
)
_Netvision_ObjectIdentity = ObjectIdentity
netvision = _Netvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1)
)
_UpsObjects_ObjectIdentity = ObjectIdentity
upsObjects = _UpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 1)
)


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 1, 1),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("mandatory")


class _UpsIdentUPSFirmwareVersion_Type(DisplayString):
    """Custom type upsIdentUPSFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentUPSFirmwareVersion_Type.__name__ = "DisplayString"
_UpsIdentUPSFirmwareVersion_Object = MibScalar
upsIdentUPSFirmwareVersion = _UpsIdentUPSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 1, 2),
    _UpsIdentUPSFirmwareVersion_Type()
)
upsIdentUPSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSFirmwareVersion.setStatus("mandatory")


class _UpsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentAgentSoftwareVersion_Object = MibScalar
upsIdentAgentSoftwareVersion = _UpsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 1, 3),
    _UpsIdentAgentSoftwareVersion_Type()
)
upsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersion.setStatus("mandatory")


class _UpsIdentUpsSerialNumber_Type(DisplayString):
    """Custom type upsIdentUpsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsIdentUpsSerialNumber_Type.__name__ = "DisplayString"
_UpsIdentUpsSerialNumber_Object = MibScalar
upsIdentUpsSerialNumber = _UpsIdentUpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 1, 4),
    _UpsIdentUpsSerialNumber_Type()
)
upsIdentUpsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUpsSerialNumber.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 2)
)


class _UpsBatteryStatus_Type(Integer32):
    """Custom type upsBatteryStatus based on Integer32"""
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
        *(("batteryDepleted", 4),
          ("batteryDischarging", 5),
          ("batteryFailure", 6),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1),
          ("upsOff", 7))
    )


_UpsBatteryStatus_Type.__name__ = "Integer32"
_UpsBatteryStatus_Object = MibScalar
upsBatteryStatus = _UpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 2, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("mandatory")
_UpsSecondsOnBattery_Type = Integer32
_UpsSecondsOnBattery_Object = MibScalar
upsSecondsOnBattery = _UpsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 2, 2),
    _UpsSecondsOnBattery_Type()
)
upsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBattery.setStatus("mandatory")
_UpsEstimatedMinutesRemaining_Type = Integer32
_UpsEstimatedMinutesRemaining_Object = MibScalar
upsEstimatedMinutesRemaining = _UpsEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 2, 3),
    _UpsEstimatedMinutesRemaining_Type()
)
upsEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemaining.setStatus("mandatory")
_UpsEstimatedChargeRemaining_Type = Integer32
_UpsEstimatedChargeRemaining_Object = MibScalar
upsEstimatedChargeRemaining = _UpsEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 2, 4),
    _UpsEstimatedChargeRemaining_Type()
)
upsEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaining.setStatus("mandatory")
_UpsBatteryVoltage_Type = Integer32
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 2, 5),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("mandatory")
_UpsBatteryTemperature_Type = Integer32
_UpsBatteryTemperature_Object = MibScalar
upsBatteryTemperature = _UpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 2, 6),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3)
)
_UpsInputNumLines_Type = Integer32
_UpsInputNumLines_Object = MibScalar
upsInputNumLines = _UpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 1),
    _UpsInputNumLines_Type()
)
upsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLines.setStatus("mandatory")
_UpsInputFrequency_Type = Integer32
_UpsInputFrequency_Object = MibScalar
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 2),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("mandatory")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 3, 1)
)
upsInputEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsInputLineIndex"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("mandatory")


class _UpsInputLineIndex_Type(Integer32):
    """Custom type upsInputLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsInputLineIndex_Type.__name__ = "Integer32"
_UpsInputLineIndex_Object = MibTableColumn
upsInputLineIndex = _UpsInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 3, 1, 1),
    _UpsInputLineIndex_Type()
)
upsInputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineIndex.setStatus("mandatory")
_UpsInputVoltage_Type = Integer32
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 3, 1, 2),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("mandatory")
_UpsInputCurrent_Type = Integer32
_UpsInputCurrent_Object = MibTableColumn
upsInputCurrent = _UpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 3, 1, 3),
    _UpsInputCurrent_Type()
)
upsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent.setStatus("mandatory")
_UpsInputVoltageMax_Type = Integer32
_UpsInputVoltageMax_Object = MibTableColumn
upsInputVoltageMax = _UpsInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 3, 1, 4),
    _UpsInputVoltageMax_Type()
)
upsInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMax.setStatus("mandatory")
_UpsInputVoltageMin_Type = Integer32
_UpsInputVoltageMin_Object = MibTableColumn
upsInputVoltageMin = _UpsInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 3, 3, 1, 5),
    _UpsInputVoltageMin_Type()
)
upsInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMin.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4)
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ecoMode", 4),
          ("normalMode", 9),
          ("onBypass", 5),
          ("onInverter", 2),
          ("onMains", 3),
          ("onMaintenanceBypass", 7),
          ("standby", 6),
          ("unknown", 1),
          ("upsOff", 8))
    )


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 1),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("mandatory")
_UpsOutputFrequency_Type = Integer32
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("mandatory")
_UpsOutputNumLines_Type = Integer32
_UpsOutputNumLines_Object = MibScalar
upsOutputNumLines = _UpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 3),
    _UpsOutputNumLines_Type()
)
upsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLines.setStatus("mandatory")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("mandatory")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 4, 1)
)
upsOutputEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("mandatory")


class _UpsOutputLineIndex_Type(Integer32):
    """Custom type upsOutputLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsOutputLineIndex_Type.__name__ = "Integer32"
_UpsOutputLineIndex_Object = MibTableColumn
upsOutputLineIndex = _UpsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 4, 1, 1),
    _UpsOutputLineIndex_Type()
)
upsOutputLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLineIndex.setStatus("mandatory")
_UpsOutputVoltage_Type = Integer32
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 4, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("mandatory")
_UpsOutputCurrent_Type = Integer32
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 4, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("mandatory")
_UpsOutputPercentLoad_Type = Integer32
_UpsOutputPercentLoad_Object = MibTableColumn
upsOutputPercentLoad = _UpsOutputPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 4, 1, 4),
    _UpsOutputPercentLoad_Type()
)
upsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setStatus("mandatory")
_UpsOutputKva_Type = Integer32
_UpsOutputKva_Object = MibTableColumn
upsOutputKva = _UpsOutputKva_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 4, 4, 1, 5),
    _UpsOutputKva_Type()
)
upsOutputKva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputKva.setStatus("mandatory")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5)
)
_UpsBypassFrequency_Type = Integer32
_UpsBypassFrequency_Object = MibScalar
upsBypassFrequency = _UpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5, 1),
    _UpsBypassFrequency_Type()
)
upsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequency.setStatus("mandatory")
_UpsBypassNumLines_Type = Integer32
_UpsBypassNumLines_Object = MibScalar
upsBypassNumLines = _UpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5, 2),
    _UpsBypassNumLines_Type()
)
upsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLines.setStatus("mandatory")
_UpsBypassTable_Object = MibTable
upsBypassTable = _UpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassTable.setStatus("mandatory")
_UpsBypassEntry_Object = MibTableRow
upsBypassEntry = _UpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5, 3, 1)
)
upsBypassEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsBypassLineIndex"),
)
if mibBuilder.loadTexts:
    upsBypassEntry.setStatus("mandatory")


class _UpsBypassLineIndex_Type(Integer32):
    """Custom type upsBypassLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsBypassLineIndex_Type.__name__ = "Integer32"
_UpsBypassLineIndex_Object = MibTableColumn
upsBypassLineIndex = _UpsBypassLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5, 3, 1, 1),
    _UpsBypassLineIndex_Type()
)
upsBypassLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassLineIndex.setStatus("mandatory")
_UpsBypassVoltage_Type = Integer32
_UpsBypassVoltage_Object = MibTableColumn
upsBypassVoltage = _UpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5, 3, 1, 2),
    _UpsBypassVoltage_Type()
)
upsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltage.setStatus("mandatory")
_UpsBypassCurrent_Type = Integer32
_UpsBypassCurrent_Object = MibTableColumn
upsBypassCurrent = _UpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 5, 3, 1, 3),
    _UpsBypassCurrent_Type()
)
upsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrent.setStatus("mandatory")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6)
)
_UpsAlarmsPresent_Type = Integer32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("mandatory")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("mandatory")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 2, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsAlarmId"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("mandatory")
_UpsAlarmId_Type = PositiveInteger
_UpsAlarmId_Object = MibTableColumn
upsAlarmId = _UpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 2, 1, 1),
    _UpsAlarmId_Type()
)
upsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmId.setStatus("mandatory")
_UpsAlarmDescr_Type = AutonomousType
_UpsAlarmDescr_Object = MibTableColumn
upsAlarmDescr = _UpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 2, 1, 2),
    _UpsAlarmDescr_Type()
)
upsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescr.setStatus("mandatory")
_UpsAlarmTime_Type = TimeStamp
_UpsAlarmTime_Object = MibTableColumn
upsAlarmTime = _UpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 2, 1, 3),
    _UpsAlarmTime_Type()
)
upsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTime.setStatus("mandatory")
_UpsAlarmExtDes_Type = DisplayString
_UpsAlarmExtDes_Object = MibTableColumn
upsAlarmExtDes = _UpsAlarmExtDes_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 2, 1, 4),
    _UpsAlarmExtDes_Type()
)
upsAlarmExtDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExtDes.setStatus("mandatory")
_UpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
upsWellKnownAlarms = _UpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3)
)
_UpsAlarmBatteryBad_Type = Integer32
_UpsAlarmBatteryBad_Object = MibScalar
upsAlarmBatteryBad = _UpsAlarmBatteryBad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 1),
    _UpsAlarmBatteryBad_Type()
)
upsAlarmBatteryBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryBad.setStatus("mandatory")
_UpsAlarmOnBattery_Type = Integer32
_UpsAlarmOnBattery_Object = MibScalar
upsAlarmOnBattery = _UpsAlarmOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 2),
    _UpsAlarmOnBattery_Type()
)
upsAlarmOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBattery.setStatus("mandatory")
_UpsAlarmLowBattery_Type = Integer32
_UpsAlarmLowBattery_Object = MibScalar
upsAlarmLowBattery = _UpsAlarmLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 3),
    _UpsAlarmLowBattery_Type()
)
upsAlarmLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmLowBattery.setStatus("mandatory")
_UpsAlarmDepletedBattery_Type = Integer32
_UpsAlarmDepletedBattery_Object = MibScalar
upsAlarmDepletedBattery = _UpsAlarmDepletedBattery_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 4),
    _UpsAlarmDepletedBattery_Type()
)
upsAlarmDepletedBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDepletedBattery.setStatus("mandatory")
_UpsAlarmTempBad_Type = Integer32
_UpsAlarmTempBad_Object = MibScalar
upsAlarmTempBad = _UpsAlarmTempBad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 5),
    _UpsAlarmTempBad_Type()
)
upsAlarmTempBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTempBad.setStatus("mandatory")
_UpsAlarmInputBad_Type = Integer32
_UpsAlarmInputBad_Object = MibScalar
upsAlarmInputBad = _UpsAlarmInputBad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 6),
    _UpsAlarmInputBad_Type()
)
upsAlarmInputBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInputBad.setStatus("mandatory")
_UpsAlarmOutputBad_Type = Integer32
_UpsAlarmOutputBad_Object = MibScalar
upsAlarmOutputBad = _UpsAlarmOutputBad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 7),
    _UpsAlarmOutputBad_Type()
)
upsAlarmOutputBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputBad.setStatus("mandatory")
_UpsAlarmOutputOverload_Type = Integer32
_UpsAlarmOutputOverload_Object = MibScalar
upsAlarmOutputOverload = _UpsAlarmOutputOverload_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 8),
    _UpsAlarmOutputOverload_Type()
)
upsAlarmOutputOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOverload.setStatus("mandatory")
_UpsAlarmOnBypass_Type = Integer32
_UpsAlarmOnBypass_Object = MibScalar
upsAlarmOnBypass = _UpsAlarmOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 9),
    _UpsAlarmOnBypass_Type()
)
upsAlarmOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBypass.setStatus("mandatory")
_UpsAlarmBypassBad_Type = Integer32
_UpsAlarmBypassBad_Object = MibScalar
upsAlarmBypassBad = _UpsAlarmBypassBad_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 10),
    _UpsAlarmBypassBad_Type()
)
upsAlarmBypassBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBypassBad.setStatus("mandatory")
_UpsAlarmOutputOffAsRequested_Type = Integer32
_UpsAlarmOutputOffAsRequested_Object = MibScalar
upsAlarmOutputOffAsRequested = _UpsAlarmOutputOffAsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 11),
    _UpsAlarmOutputOffAsRequested_Type()
)
upsAlarmOutputOffAsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequested.setStatus("mandatory")
_UpsAlarmUpsOffAsRequested_Type = Integer32
_UpsAlarmUpsOffAsRequested_Object = MibScalar
upsAlarmUpsOffAsRequested = _UpsAlarmUpsOffAsRequested_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 12),
    _UpsAlarmUpsOffAsRequested_Type()
)
upsAlarmUpsOffAsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequested.setStatus("mandatory")
_UpsAlarmChargerFailed_Type = Integer32
_UpsAlarmChargerFailed_Object = MibScalar
upsAlarmChargerFailed = _UpsAlarmChargerFailed_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 13),
    _UpsAlarmChargerFailed_Type()
)
upsAlarmChargerFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmChargerFailed.setStatus("mandatory")
_UpsAlarmUpsOutputOff_Type = Integer32
_UpsAlarmUpsOutputOff_Object = MibScalar
upsAlarmUpsOutputOff = _UpsAlarmUpsOutputOff_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 14),
    _UpsAlarmUpsOutputOff_Type()
)
upsAlarmUpsOutputOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOff.setStatus("mandatory")
_UpsAlarmUpsSystemOff_Type = Integer32
_UpsAlarmUpsSystemOff_Object = MibScalar
upsAlarmUpsSystemOff = _UpsAlarmUpsSystemOff_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 15),
    _UpsAlarmUpsSystemOff_Type()
)
upsAlarmUpsSystemOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOff.setStatus("mandatory")
_UpsAlarmFanFailure_Type = Integer32
_UpsAlarmFanFailure_Object = MibScalar
upsAlarmFanFailure = _UpsAlarmFanFailure_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 16),
    _UpsAlarmFanFailure_Type()
)
upsAlarmFanFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmFanFailure.setStatus("mandatory")
_UpsAlarmFuseFailure_Type = Integer32
_UpsAlarmFuseFailure_Object = MibScalar
upsAlarmFuseFailure = _UpsAlarmFuseFailure_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 17),
    _UpsAlarmFuseFailure_Type()
)
upsAlarmFuseFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmFuseFailure.setStatus("mandatory")
_UpsAlarmGeneralFault_Type = Integer32
_UpsAlarmGeneralFault_Object = MibScalar
upsAlarmGeneralFault = _UpsAlarmGeneralFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 18),
    _UpsAlarmGeneralFault_Type()
)
upsAlarmGeneralFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmGeneralFault.setStatus("mandatory")
_UpsAlarmDiagnosticTestFailed_Type = Integer32
_UpsAlarmDiagnosticTestFailed_Object = MibScalar
upsAlarmDiagnosticTestFailed = _UpsAlarmDiagnosticTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 19),
    _UpsAlarmDiagnosticTestFailed_Type()
)
upsAlarmDiagnosticTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailed.setStatus("mandatory")
_UpsAlarmCommunicationLost_Type = Integer32
_UpsAlarmCommunicationLost_Object = MibScalar
upsAlarmCommunicationLost = _UpsAlarmCommunicationLost_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 20),
    _UpsAlarmCommunicationLost_Type()
)
upsAlarmCommunicationLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCommunicationLost.setStatus("mandatory")
_UpsAlarmAwaitingPower_Type = Integer32
_UpsAlarmAwaitingPower_Object = MibScalar
upsAlarmAwaitingPower = _UpsAlarmAwaitingPower_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 21),
    _UpsAlarmAwaitingPower_Type()
)
upsAlarmAwaitingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAwaitingPower.setStatus("mandatory")
_UpsAlarmShutdownPending_Type = Integer32
_UpsAlarmShutdownPending_Object = MibScalar
upsAlarmShutdownPending = _UpsAlarmShutdownPending_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 22),
    _UpsAlarmShutdownPending_Type()
)
upsAlarmShutdownPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShutdownPending.setStatus("mandatory")
_UpsAlarmShutdownImminent_Type = Integer32
_UpsAlarmShutdownImminent_Object = MibScalar
upsAlarmShutdownImminent = _UpsAlarmShutdownImminent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 23),
    _UpsAlarmShutdownImminent_Type()
)
upsAlarmShutdownImminent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShutdownImminent.setStatus("mandatory")
_UpsAlarmTestInProgress_Type = Integer32
_UpsAlarmTestInProgress_Object = MibScalar
upsAlarmTestInProgress = _UpsAlarmTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 24),
    _UpsAlarmTestInProgress_Type()
)
upsAlarmTestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTestInProgress.setStatus("mandatory")
_UpsAlarmPowerSupplyFault_Type = Integer32
_UpsAlarmPowerSupplyFault_Object = MibScalar
upsAlarmPowerSupplyFault = _UpsAlarmPowerSupplyFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 25),
    _UpsAlarmPowerSupplyFault_Type()
)
upsAlarmPowerSupplyFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmPowerSupplyFault.setStatus("mandatory")
_UpsAlarmAuxMainFail_Type = Integer32
_UpsAlarmAuxMainFail_Object = MibScalar
upsAlarmAuxMainFail = _UpsAlarmAuxMainFail_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 26),
    _UpsAlarmAuxMainFail_Type()
)
upsAlarmAuxMainFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAuxMainFail.setStatus("mandatory")
_UpsAlarmManualBypassClose_Type = Integer32
_UpsAlarmManualBypassClose_Object = MibScalar
upsAlarmManualBypassClose = _UpsAlarmManualBypassClose_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 27),
    _UpsAlarmManualBypassClose_Type()
)
upsAlarmManualBypassClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmManualBypassClose.setStatus("mandatory")
_UpsAlarmShortCircuit_Type = Integer32
_UpsAlarmShortCircuit_Object = MibScalar
upsAlarmShortCircuit = _UpsAlarmShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 28),
    _UpsAlarmShortCircuit_Type()
)
upsAlarmShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmShortCircuit.setStatus("mandatory")
_UpsAlarmBatteryChargerFailure_Type = Integer32
_UpsAlarmBatteryChargerFailure_Object = MibScalar
upsAlarmBatteryChargerFailure = _UpsAlarmBatteryChargerFailure_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 29),
    _UpsAlarmBatteryChargerFailure_Type()
)
upsAlarmBatteryChargerFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryChargerFailure.setStatus("mandatory")
_UpsAlarmInverterOverCurrent_Type = Integer32
_UpsAlarmInverterOverCurrent_Object = MibScalar
upsAlarmInverterOverCurrent = _UpsAlarmInverterOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 30),
    _UpsAlarmInverterOverCurrent_Type()
)
upsAlarmInverterOverCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterOverCurrent.setStatus("mandatory")
_UpsAlarmInverterDistorsion_Type = Integer32
_UpsAlarmInverterDistorsion_Object = MibScalar
upsAlarmInverterDistorsion = _UpsAlarmInverterDistorsion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 31),
    _UpsAlarmInverterDistorsion_Type()
)
upsAlarmInverterDistorsion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterDistorsion.setStatus("mandatory")
_UpsAlarmPrechargeVoltageFail_Type = Integer32
_UpsAlarmPrechargeVoltageFail_Object = MibScalar
upsAlarmPrechargeVoltageFail = _UpsAlarmPrechargeVoltageFail_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 32),
    _UpsAlarmPrechargeVoltageFail_Type()
)
upsAlarmPrechargeVoltageFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmPrechargeVoltageFail.setStatus("mandatory")
_UpsAlarmBoostTooLow_Type = Integer32
_UpsAlarmBoostTooLow_Object = MibScalar
upsAlarmBoostTooLow = _UpsAlarmBoostTooLow_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 33),
    _UpsAlarmBoostTooLow_Type()
)
upsAlarmBoostTooLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBoostTooLow.setStatus("mandatory")
_UpsAlarmBoostTooHigh_Type = Integer32
_UpsAlarmBoostTooHigh_Object = MibScalar
upsAlarmBoostTooHigh = _UpsAlarmBoostTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 34),
    _UpsAlarmBoostTooHigh_Type()
)
upsAlarmBoostTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBoostTooHigh.setStatus("mandatory")
_UpsAlarmBatteryTooHigh_Type = Integer32
_UpsAlarmBatteryTooHigh_Object = MibScalar
upsAlarmBatteryTooHigh = _UpsAlarmBatteryTooHigh_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 35),
    _UpsAlarmBatteryTooHigh_Type()
)
upsAlarmBatteryTooHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryTooHigh.setStatus("mandatory")
_UpsAlarmImproperCondition_Type = Integer32
_UpsAlarmImproperCondition_Object = MibScalar
upsAlarmImproperCondition = _UpsAlarmImproperCondition_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 36),
    _UpsAlarmImproperCondition_Type()
)
upsAlarmImproperCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmImproperCondition.setStatus("mandatory")
_UpsAlarmOverloadTimeout_Type = Integer32
_UpsAlarmOverloadTimeout_Object = MibScalar
upsAlarmOverloadTimeout = _UpsAlarmOverloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 37),
    _UpsAlarmOverloadTimeout_Type()
)
upsAlarmOverloadTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOverloadTimeout.setStatus("mandatory")
_UpsAlarmControlSystemFailure_Type = Integer32
_UpsAlarmControlSystemFailure_Object = MibScalar
upsAlarmControlSystemFailure = _UpsAlarmControlSystemFailure_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 38),
    _UpsAlarmControlSystemFailure_Type()
)
upsAlarmControlSystemFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmControlSystemFailure.setStatus("mandatory")
_UpsAlarmDataCorrupted_Type = Integer32
_UpsAlarmDataCorrupted_Object = MibScalar
upsAlarmDataCorrupted = _UpsAlarmDataCorrupted_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 39),
    _UpsAlarmDataCorrupted_Type()
)
upsAlarmDataCorrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDataCorrupted.setStatus("mandatory")
_UpsAlarmPllFault_Type = Integer32
_UpsAlarmPllFault_Object = MibScalar
upsAlarmPllFault = _UpsAlarmPllFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 40),
    _UpsAlarmPllFault_Type()
)
upsAlarmPllFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmPllFault.setStatus("mandatory")
_UpsAlarmInputGeneralAlarm_Type = Integer32
_UpsAlarmInputGeneralAlarm_Object = MibScalar
upsAlarmInputGeneralAlarm = _UpsAlarmInputGeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 41),
    _UpsAlarmInputGeneralAlarm_Type()
)
upsAlarmInputGeneralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInputGeneralAlarm.setStatus("mandatory")
_UpsAlarmRectifierGeneralAlarm_Type = Integer32
_UpsAlarmRectifierGeneralAlarm_Object = MibScalar
upsAlarmRectifierGeneralAlarm = _UpsAlarmRectifierGeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 42),
    _UpsAlarmRectifierGeneralAlarm_Type()
)
upsAlarmRectifierGeneralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRectifierGeneralAlarm.setStatus("mandatory")
_UpsAlarmBoostGeneralAlarm_Type = Integer32
_UpsAlarmBoostGeneralAlarm_Object = MibScalar
upsAlarmBoostGeneralAlarm = _UpsAlarmBoostGeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 43),
    _UpsAlarmBoostGeneralAlarm_Type()
)
upsAlarmBoostGeneralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBoostGeneralAlarm.setStatus("mandatory")
_UpsAlarmInverterGeneralAlarm_Type = Integer32
_UpsAlarmInverterGeneralAlarm_Object = MibScalar
upsAlarmInverterGeneralAlarm = _UpsAlarmInverterGeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 44),
    _UpsAlarmInverterGeneralAlarm_Type()
)
upsAlarmInverterGeneralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterGeneralAlarm.setStatus("mandatory")
_UpsAlarmBatteryGeneralAlarm_Type = Integer32
_UpsAlarmBatteryGeneralAlarm_Object = MibScalar
upsAlarmBatteryGeneralAlarm = _UpsAlarmBatteryGeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 45),
    _UpsAlarmBatteryGeneralAlarm_Type()
)
upsAlarmBatteryGeneralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryGeneralAlarm.setStatus("mandatory")
_UpsAlarmOutputOver_Type = Integer32
_UpsAlarmOutputOver_Object = MibScalar
upsAlarmOutputOver = _UpsAlarmOutputOver_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 46),
    _UpsAlarmOutputOver_Type()
)
upsAlarmOutputOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOver.setStatus("mandatory")
_UpsAlarmOutputUnder_Type = Integer32
_UpsAlarmOutputUnder_Object = MibScalar
upsAlarmOutputUnder = _UpsAlarmOutputUnder_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 47),
    _UpsAlarmOutputUnder_Type()
)
upsAlarmOutputUnder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputUnder.setStatus("mandatory")
_UpsAlarmBypassGeneralAlarm_Type = Integer32
_UpsAlarmBypassGeneralAlarm_Object = MibScalar
upsAlarmBypassGeneralAlarm = _UpsAlarmBypassGeneralAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 48),
    _UpsAlarmBypassGeneralAlarm_Type()
)
upsAlarmBypassGeneralAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBypassGeneralAlarm.setStatus("mandatory")
_UpsAlarmStopForOverload_Type = Integer32
_UpsAlarmStopForOverload_Object = MibScalar
upsAlarmStopForOverload = _UpsAlarmStopForOverload_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 49),
    _UpsAlarmStopForOverload_Type()
)
upsAlarmStopForOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmStopForOverload.setStatus("mandatory")
_UpsAlarmImminentStop_Type = Integer32
_UpsAlarmImminentStop_Object = MibScalar
upsAlarmImminentStop = _UpsAlarmImminentStop_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 50),
    _UpsAlarmImminentStop_Type()
)
upsAlarmImminentStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmImminentStop.setStatus("mandatory")
_UpsAlarmModule1Alarm_Type = Integer32
_UpsAlarmModule1Alarm_Object = MibScalar
upsAlarmModule1Alarm = _UpsAlarmModule1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 51),
    _UpsAlarmModule1Alarm_Type()
)
upsAlarmModule1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule1Alarm.setStatus("mandatory")
_UpsAlarmModule2Alarm_Type = Integer32
_UpsAlarmModule2Alarm_Object = MibScalar
upsAlarmModule2Alarm = _UpsAlarmModule2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 52),
    _UpsAlarmModule2Alarm_Type()
)
upsAlarmModule2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule2Alarm.setStatus("mandatory")
_UpsAlarmModule3Alarm_Type = Integer32
_UpsAlarmModule3Alarm_Object = MibScalar
upsAlarmModule3Alarm = _UpsAlarmModule3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 53),
    _UpsAlarmModule3Alarm_Type()
)
upsAlarmModule3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule3Alarm.setStatus("mandatory")
_UpsAlarmModule4Alarm_Type = Integer32
_UpsAlarmModule4Alarm_Object = MibScalar
upsAlarmModule4Alarm = _UpsAlarmModule4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 54),
    _UpsAlarmModule4Alarm_Type()
)
upsAlarmModule4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule4Alarm.setStatus("mandatory")
_UpsAlarmModule5Alarm_Type = Integer32
_UpsAlarmModule5Alarm_Object = MibScalar
upsAlarmModule5Alarm = _UpsAlarmModule5Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 55),
    _UpsAlarmModule5Alarm_Type()
)
upsAlarmModule5Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule5Alarm.setStatus("mandatory")
_UpsAlarmModule6Alarm_Type = Integer32
_UpsAlarmModule6Alarm_Object = MibScalar
upsAlarmModule6Alarm = _UpsAlarmModule6Alarm_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 56),
    _UpsAlarmModule6Alarm_Type()
)
upsAlarmModule6Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmModule6Alarm.setStatus("mandatory")
_UpsAlarmExternalAlarm1_Type = Integer32
_UpsAlarmExternalAlarm1_Object = MibScalar
upsAlarmExternalAlarm1 = _UpsAlarmExternalAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 57),
    _UpsAlarmExternalAlarm1_Type()
)
upsAlarmExternalAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm1.setStatus("mandatory")
_UpsAlarmExternalAlarm2_Type = Integer32
_UpsAlarmExternalAlarm2_Object = MibScalar
upsAlarmExternalAlarm2 = _UpsAlarmExternalAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 58),
    _UpsAlarmExternalAlarm2_Type()
)
upsAlarmExternalAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm2.setStatus("mandatory")
_UpsAlarmExternalAlarm3_Type = Integer32
_UpsAlarmExternalAlarm3_Object = MibScalar
upsAlarmExternalAlarm3 = _UpsAlarmExternalAlarm3_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 59),
    _UpsAlarmExternalAlarm3_Type()
)
upsAlarmExternalAlarm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm3.setStatus("mandatory")
_UpsAlarmExternalAlarm4_Type = Integer32
_UpsAlarmExternalAlarm4_Object = MibScalar
upsAlarmExternalAlarm4 = _UpsAlarmExternalAlarm4_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 60),
    _UpsAlarmExternalAlarm4_Type()
)
upsAlarmExternalAlarm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmExternalAlarm4.setStatus("mandatory")
_UpsAlarmEService_Type = Integer32
_UpsAlarmEService_Object = MibScalar
upsAlarmEService = _UpsAlarmEService_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 61),
    _UpsAlarmEService_Type()
)
upsAlarmEService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmEService.setStatus("mandatory")
_UpsAlarmRedundancyLost_Type = Integer32
_UpsAlarmRedundancyLost_Object = MibScalar
upsAlarmRedundancyLost = _UpsAlarmRedundancyLost_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 62),
    _UpsAlarmRedundancyLost_Type()
)
upsAlarmRedundancyLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRedundancyLost.setStatus("mandatory")
_UpsAlarmPeriodicServiceCheck_Type = Integer32
_UpsAlarmPeriodicServiceCheck_Object = MibScalar
upsAlarmPeriodicServiceCheck = _UpsAlarmPeriodicServiceCheck_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 63),
    _UpsAlarmPeriodicServiceCheck_Type()
)
upsAlarmPeriodicServiceCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmPeriodicServiceCheck.setStatus("mandatory")
_UpsAlarmAllTransferDisabled_Type = Integer32
_UpsAlarmAllTransferDisabled_Object = MibScalar
upsAlarmAllTransferDisabled = _UpsAlarmAllTransferDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 64),
    _UpsAlarmAllTransferDisabled_Type()
)
upsAlarmAllTransferDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAllTransferDisabled.setStatus("mandatory")
_UpsAlarmAutoTransferDisabled_Type = Integer32
_UpsAlarmAutoTransferDisabled_Object = MibScalar
upsAlarmAutoTransferDisabled = _UpsAlarmAutoTransferDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 65),
    _UpsAlarmAutoTransferDisabled_Type()
)
upsAlarmAutoTransferDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAutoTransferDisabled.setStatus("mandatory")
_UpsAlarmBatteryRoom_Type = Integer32
_UpsAlarmBatteryRoom_Object = MibScalar
upsAlarmBatteryRoom = _UpsAlarmBatteryRoom_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 66),
    _UpsAlarmBatteryRoom_Type()
)
upsAlarmBatteryRoom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryRoom.setStatus("mandatory")
_UpsAlarmManualBypass_Type = Integer32
_UpsAlarmManualBypass_Object = MibScalar
upsAlarmManualBypass = _UpsAlarmManualBypass_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 67),
    _UpsAlarmManualBypass_Type()
)
upsAlarmManualBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmManualBypass.setStatus("mandatory")
_UpsAlarmBatteryDischarged_Type = Integer32
_UpsAlarmBatteryDischarged_Object = MibScalar
upsAlarmBatteryDischarged = _UpsAlarmBatteryDischarged_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 68),
    _UpsAlarmBatteryDischarged_Type()
)
upsAlarmBatteryDischarged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryDischarged.setStatus("mandatory")
_UpsAlarmInsufficientResources_Type = Integer32
_UpsAlarmInsufficientResources_Object = MibScalar
upsAlarmInsufficientResources = _UpsAlarmInsufficientResources_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 69),
    _UpsAlarmInsufficientResources_Type()
)
upsAlarmInsufficientResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInsufficientResources.setStatus("mandatory")
_UpsAlarmOptionalBoards_Type = Integer32
_UpsAlarmOptionalBoards_Object = MibScalar
upsAlarmOptionalBoards = _UpsAlarmOptionalBoards_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 70),
    _UpsAlarmOptionalBoards_Type()
)
upsAlarmOptionalBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOptionalBoards.setStatus("mandatory")
_UpsAlarmRectifierFault_Type = Integer32
_UpsAlarmRectifierFault_Object = MibScalar
upsAlarmRectifierFault = _UpsAlarmRectifierFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 71),
    _UpsAlarmRectifierFault_Type()
)
upsAlarmRectifierFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRectifierFault.setStatus("mandatory")
_UpsAlarmBoostFault_Type = Integer32
_UpsAlarmBoostFault_Object = MibScalar
upsAlarmBoostFault = _UpsAlarmBoostFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 72),
    _UpsAlarmBoostFault_Type()
)
upsAlarmBoostFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBoostFault.setStatus("mandatory")
_UpsAlarmInverterFault_Type = Integer32
_UpsAlarmInverterFault_Object = MibScalar
upsAlarmInverterFault = _UpsAlarmInverterFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 73),
    _UpsAlarmInverterFault_Type()
)
upsAlarmInverterFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterFault.setStatus("mandatory")
_UpsAlarmParallelModuleFault_Type = Integer32
_UpsAlarmParallelModuleFault_Object = MibScalar
upsAlarmParallelModuleFault = _UpsAlarmParallelModuleFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 74),
    _UpsAlarmParallelModuleFault_Type()
)
upsAlarmParallelModuleFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmParallelModuleFault.setStatus("mandatory")
_UpsAlarmGenSetGeneral_Type = Integer32
_UpsAlarmGenSetGeneral_Object = MibScalar
upsAlarmGenSetGeneral = _UpsAlarmGenSetGeneral_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 75),
    _UpsAlarmGenSetGeneral_Type()
)
upsAlarmGenSetGeneral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmGenSetGeneral.setStatus("mandatory")
_UpsAlarmGenSetFault_Type = Integer32
_UpsAlarmGenSetFault_Object = MibScalar
upsAlarmGenSetFault = _UpsAlarmGenSetFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 76),
    _UpsAlarmGenSetFault_Type()
)
upsAlarmGenSetFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmGenSetFault.setStatus("mandatory")
_UpsAlarmEmergencyStopActive_Type = Integer32
_UpsAlarmEmergencyStopActive_Object = MibScalar
upsAlarmEmergencyStopActive = _UpsAlarmEmergencyStopActive_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 77),
    _UpsAlarmEmergencyStopActive_Type()
)
upsAlarmEmergencyStopActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmEmergencyStopActive.setStatus("mandatory")
_UpsAlarmBatteryCircuitOpen_Type = Integer32
_UpsAlarmBatteryCircuitOpen_Object = MibScalar
upsAlarmBatteryCircuitOpen = _UpsAlarmBatteryCircuitOpen_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 78),
    _UpsAlarmBatteryCircuitOpen_Type()
)
upsAlarmBatteryCircuitOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryCircuitOpen.setStatus("mandatory")
_UpsAlarmFansFailure_Type = Integer32
_UpsAlarmFansFailure_Object = MibScalar
upsAlarmFansFailure = _UpsAlarmFansFailure_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 79),
    _UpsAlarmFansFailure_Type()
)
upsAlarmFansFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmFansFailure.setStatus("mandatory")
_UpsAlarmPhaseRotationFault_Type = Integer32
_UpsAlarmPhaseRotationFault_Object = MibScalar
upsAlarmPhaseRotationFault = _UpsAlarmPhaseRotationFault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 80),
    _UpsAlarmPhaseRotationFault_Type()
)
upsAlarmPhaseRotationFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmPhaseRotationFault.setStatus("mandatory")
_UpsAlarmA62_Type = Integer32
_UpsAlarmA62_Object = MibScalar
upsAlarmA62 = _UpsAlarmA62_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 81),
    _UpsAlarmA62_Type()
)
upsAlarmA62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmA62.setStatus("mandatory")
_UpsAlarmA63_Type = Integer32
_UpsAlarmA63_Object = MibScalar
upsAlarmA63 = _UpsAlarmA63_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 6, 3, 82),
    _UpsAlarmA63_Type()
)
upsAlarmA63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmA63.setStatus("mandatory")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7)
)
_UpsTestId_Type = ObjectIdentifier
_UpsTestId_Object = MibScalar
upsTestId = _UpsTestId_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 1),
    _UpsTestId_Type()
)
upsTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestId.setStatus("mandatory")
_UpsTestSpinLock_Type = TestAndIncr
_UpsTestSpinLock_Object = MibScalar
upsTestSpinLock = _UpsTestSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 2),
    _UpsTestSpinLock_Type()
)
upsTestSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLock.setStatus("mandatory")


class _UpsTestResultsSummary_Type(Integer32):
    """Custom type upsTestResultsSummary based on Integer32"""
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
        *(("byPass", 3),
          ("failed", 4),
          ("inProgress", 2),
          ("notActive", 1))
    )


_UpsTestResultsSummary_Type.__name__ = "Integer32"
_UpsTestResultsSummary_Object = MibScalar
upsTestResultsSummary = _UpsTestResultsSummary_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 3),
    _UpsTestResultsSummary_Type()
)
upsTestResultsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummary.setStatus("mandatory")
_UpsTestResultsDetail_Type = DisplayString
_UpsTestResultsDetail_Object = MibScalar
upsTestResultsDetail = _UpsTestResultsDetail_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 4),
    _UpsTestResultsDetail_Type()
)
upsTestResultsDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetail.setStatus("mandatory")
_UpsTestStartTime_Type = TimeStamp
_UpsTestStartTime_Object = MibScalar
upsTestStartTime = _UpsTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 5),
    _UpsTestStartTime_Type()
)
upsTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTime.setStatus("mandatory")
_UpsTestElapsedTime_Type = TimeInterval
_UpsTestElapsedTime_Object = MibScalar
upsTestElapsedTime = _UpsTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 6),
    _UpsTestElapsedTime_Type()
)
upsTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTime.setStatus("mandatory")
_UpsWellKnownTests_ObjectIdentity = ObjectIdentity
upsWellKnownTests = _UpsWellKnownTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 7)
)
_UpsTestNoTestsInitiated_Type = Integer32
_UpsTestNoTestsInitiated_Object = MibScalar
upsTestNoTestsInitiated = _UpsTestNoTestsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 7, 1),
    _UpsTestNoTestsInitiated_Type()
)
upsTestNoTestsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestNoTestsInitiated.setStatus("mandatory")
_UpsTestAbortTestInProgress_Type = Integer32
_UpsTestAbortTestInProgress_Object = MibScalar
upsTestAbortTestInProgress = _UpsTestAbortTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 7, 2),
    _UpsTestAbortTestInProgress_Type()
)
upsTestAbortTestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestAbortTestInProgress.setStatus("mandatory")
_UpsTestGeneralSystemsTest_Type = Integer32
_UpsTestGeneralSystemsTest_Object = MibScalar
upsTestGeneralSystemsTest = _UpsTestGeneralSystemsTest_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 7, 3),
    _UpsTestGeneralSystemsTest_Type()
)
upsTestGeneralSystemsTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTest.setStatus("mandatory")
_UpsTestQuickBatteryTest_Type = Integer32
_UpsTestQuickBatteryTest_Object = MibScalar
upsTestQuickBatteryTest = _UpsTestQuickBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 7, 4),
    _UpsTestQuickBatteryTest_Type()
)
upsTestQuickBatteryTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestQuickBatteryTest.setStatus("mandatory")
_UpsDeepBatteryCalibration_Type = Integer32
_UpsDeepBatteryCalibration_Object = MibScalar
upsDeepBatteryCalibration = _UpsDeepBatteryCalibration_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 7, 7, 5),
    _UpsDeepBatteryCalibration_Type()
)
upsDeepBatteryCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeepBatteryCalibration.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8)
)


class _UpsControlStatusControl_Type(Integer32):
    """Custom type upsControlStatusControl based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("upsAlarmReset", 5),
          ("upsBuzzerOff", 7),
          ("upsCommandReset", 6),
          ("upsEcoMode", 3),
          ("upsNormalMode", 4),
          ("upsOnBypass", 8),
          ("upsOnInverter", 9),
          ("upsStandbyOff", 2),
          ("upsStandbyOn", 1))
    )


_UpsControlStatusControl_Type.__name__ = "Integer32"
_UpsControlStatusControl_Object = MibScalar
upsControlStatusControl = _UpsControlStatusControl_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 1),
    _UpsControlStatusControl_Type()
)
upsControlStatusControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlStatusControl.setStatus("mandatory")
_UpsShutdownDelay_Type = Integer32
_UpsShutdownDelay_Object = MibScalar
upsShutdownDelay = _UpsShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 2),
    _UpsShutdownDelay_Type()
)
upsShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownDelay.setStatus("mandatory")


class _UpsTurnOffAfterShutdown_Type(Integer32):
    """Custom type upsTurnOffAfterShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsTurnOffAfterShutdown_Type.__name__ = "Integer32"
_UpsTurnOffAfterShutdown_Object = MibScalar
upsTurnOffAfterShutdown = _UpsTurnOffAfterShutdown_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 3),
    _UpsTurnOffAfterShutdown_Type()
)
upsTurnOffAfterShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTurnOffAfterShutdown.setStatus("mandatory")
_UpsControlShutdownParametersTable_Object = MibTable
upsControlShutdownParametersTable = _UpsControlShutdownParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    upsControlShutdownParametersTable.setStatus("mandatory")
_ShutdownParametersEntry_Object = MibTableRow
shutdownParametersEntry = _ShutdownParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4, 1)
)
shutdownParametersEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlEventDescr"),
)
if mibBuilder.loadTexts:
    shutdownParametersEntry.setStatus("mandatory")
_UpsControlEventDescr_Type = DisplayString
_UpsControlEventDescr_Object = MibTableColumn
upsControlEventDescr = _UpsControlEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4, 1, 1),
    _UpsControlEventDescr_Type()
)
upsControlEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlEventDescr.setStatus("mandatory")


class _UpsControlEventStatus_Type(Integer32):
    """Custom type upsControlEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsControlEventStatus_Type.__name__ = "Integer32"
_UpsControlEventStatus_Object = MibTableColumn
upsControlEventStatus = _UpsControlEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4, 1, 2),
    _UpsControlEventStatus_Type()
)
upsControlEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEventStatus.setStatus("mandatory")


class _UpsControlDelay_Type(Integer32):
    """Custom type upsControlDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UpsControlDelay_Type.__name__ = "Integer32"
_UpsControlDelay_Object = MibTableColumn
upsControlDelay = _UpsControlDelay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4, 1, 3),
    _UpsControlDelay_Type()
)
upsControlDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlDelay.setStatus("mandatory")


class _UpsControlFirstWarning_Type(Integer32):
    """Custom type upsControlFirstWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UpsControlFirstWarning_Type.__name__ = "Integer32"
_UpsControlFirstWarning_Object = MibTableColumn
upsControlFirstWarning = _UpsControlFirstWarning_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4, 1, 4),
    _UpsControlFirstWarning_Type()
)
upsControlFirstWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlFirstWarning.setStatus("mandatory")


class _UpsControlWarningInterval_Type(Integer32):
    """Custom type upsControlWarningInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UpsControlWarningInterval_Type.__name__ = "Integer32"
_UpsControlWarningInterval_Object = MibTableColumn
upsControlWarningInterval = _UpsControlWarningInterval_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4, 1, 5),
    _UpsControlWarningInterval_Type()
)
upsControlWarningInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWarningInterval.setStatus("mandatory")


class _UpsControlSeverity_Type(Integer32):
    """Custom type upsControlSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_UpsControlSeverity_Type.__name__ = "Integer32"
_UpsControlSeverity_Object = MibTableColumn
upsControlSeverity = _UpsControlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 4, 1, 6),
    _UpsControlSeverity_Type()
)
upsControlSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSeverity.setStatus("mandatory")
_UpsControlWeeklyScheduleTable_Object = MibTable
upsControlWeeklyScheduleTable = _UpsControlWeeklyScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    upsControlWeeklyScheduleTable.setStatus("mandatory")
_UpsControlWeeklyScheduleEntry_Object = MibTableRow
upsControlWeeklyScheduleEntry = _UpsControlWeeklyScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 5, 1)
)
upsControlWeeklyScheduleEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlWeeklyIndex"),
)
if mibBuilder.loadTexts:
    upsControlWeeklyScheduleEntry.setStatus("mandatory")


class _UpsControlWeeklyIndex_Type(Integer32):
    """Custom type upsControlWeeklyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_UpsControlWeeklyIndex_Type.__name__ = "Integer32"
_UpsControlWeeklyIndex_Object = MibTableColumn
upsControlWeeklyIndex = _UpsControlWeeklyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 5, 1, 1),
    _UpsControlWeeklyIndex_Type()
)
upsControlWeeklyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlWeeklyIndex.setStatus("mandatory")


class _UpsControlWeeklyShutdownDay_Type(Integer32):
    """Custom type upsControlWeeklyShutdownDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsControlWeeklyShutdownDay_Type.__name__ = "Integer32"
_UpsControlWeeklyShutdownDay_Object = MibTableColumn
upsControlWeeklyShutdownDay = _UpsControlWeeklyShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 5, 1, 2),
    _UpsControlWeeklyShutdownDay_Type()
)
upsControlWeeklyShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyShutdownDay.setStatus("mandatory")


class _UpsControlWeeklyShutdownTime_Type(DisplayString):
    """Custom type upsControlWeeklyShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlWeeklyShutdownTime_Type.__name__ = "DisplayString"
_UpsControlWeeklyShutdownTime_Object = MibTableColumn
upsControlWeeklyShutdownTime = _UpsControlWeeklyShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 5, 1, 3),
    _UpsControlWeeklyShutdownTime_Type()
)
upsControlWeeklyShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyShutdownTime.setStatus("mandatory")


class _UpsControlWeeklyRestartDay_Type(Integer32):
    """Custom type upsControlWeeklyRestartDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsControlWeeklyRestartDay_Type.__name__ = "Integer32"
_UpsControlWeeklyRestartDay_Object = MibTableColumn
upsControlWeeklyRestartDay = _UpsControlWeeklyRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 5, 1, 4),
    _UpsControlWeeklyRestartDay_Type()
)
upsControlWeeklyRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyRestartDay.setStatus("mandatory")


class _UpsControlWeeklyRestartTime_Type(DisplayString):
    """Custom type upsControlWeeklyRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlWeeklyRestartTime_Type.__name__ = "DisplayString"
_UpsControlWeeklyRestartTime_Object = MibTableColumn
upsControlWeeklyRestartTime = _UpsControlWeeklyRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 5, 1, 5),
    _UpsControlWeeklyRestartTime_Type()
)
upsControlWeeklyRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyRestartTime.setStatus("mandatory")
_UpsControlSpecialScheduleTable_Object = MibTable
upsControlSpecialScheduleTable = _UpsControlSpecialScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    upsControlSpecialScheduleTable.setStatus("mandatory")
_UpsControlSpecialScheduleEntry_Object = MibTableRow
upsControlSpecialScheduleEntry = _UpsControlSpecialScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 6, 1)
)
upsControlSpecialScheduleEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlSpecialIndex"),
)
if mibBuilder.loadTexts:
    upsControlSpecialScheduleEntry.setStatus("mandatory")


class _UpsControlSpecialIndex_Type(Integer32):
    """Custom type upsControlSpecialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_UpsControlSpecialIndex_Type.__name__ = "Integer32"
_UpsControlSpecialIndex_Object = MibTableColumn
upsControlSpecialIndex = _UpsControlSpecialIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 6, 1, 1),
    _UpsControlSpecialIndex_Type()
)
upsControlSpecialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlSpecialIndex.setStatus("mandatory")


class _UpsControlSpecialShutdownDay_Type(DisplayString):
    """Custom type upsControlSpecialShutdownDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsControlSpecialShutdownDay_Type.__name__ = "DisplayString"
_UpsControlSpecialShutdownDay_Object = MibTableColumn
upsControlSpecialShutdownDay = _UpsControlSpecialShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 6, 1, 2),
    _UpsControlSpecialShutdownDay_Type()
)
upsControlSpecialShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialShutdownDay.setStatus("mandatory")


class _UpsControlSpecialShutdownTime_Type(DisplayString):
    """Custom type upsControlSpecialShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlSpecialShutdownTime_Type.__name__ = "DisplayString"
_UpsControlSpecialShutdownTime_Object = MibTableColumn
upsControlSpecialShutdownTime = _UpsControlSpecialShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 6, 1, 3),
    _UpsControlSpecialShutdownTime_Type()
)
upsControlSpecialShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialShutdownTime.setStatus("mandatory")


class _UpsControlSpecialRestartDay_Type(DisplayString):
    """Custom type upsControlSpecialRestartDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsControlSpecialRestartDay_Type.__name__ = "DisplayString"
_UpsControlSpecialRestartDay_Object = MibTableColumn
upsControlSpecialRestartDay = _UpsControlSpecialRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 6, 1, 4),
    _UpsControlSpecialRestartDay_Type()
)
upsControlSpecialRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialRestartDay.setStatus("mandatory")


class _UpsControlSpecialRestartTime_Type(DisplayString):
    """Custom type upsControlSpecialRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlSpecialRestartTime_Type.__name__ = "DisplayString"
_UpsControlSpecialRestartTime_Object = MibTableColumn
upsControlSpecialRestartTime = _UpsControlSpecialRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 6, 1, 5),
    _UpsControlSpecialRestartTime_Type()
)
upsControlSpecialRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialRestartTime.setStatus("mandatory")
_UpsControlEcoModeScheduleTable_Object = MibTable
upsControlEcoModeScheduleTable = _UpsControlEcoModeScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 7)
)
if mibBuilder.loadTexts:
    upsControlEcoModeScheduleTable.setStatus("mandatory")
_UpsControlEcoModeScheduleEntry_Object = MibTableRow
upsControlEcoModeScheduleEntry = _UpsControlEcoModeScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 7, 1)
)
upsControlEcoModeScheduleEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "upsControlEcoModeIndex"),
)
if mibBuilder.loadTexts:
    upsControlEcoModeScheduleEntry.setStatus("mandatory")


class _UpsControlEcoModeIndex_Type(Integer32):
    """Custom type upsControlEcoModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_UpsControlEcoModeIndex_Type.__name__ = "Integer32"
_UpsControlEcoModeIndex_Object = MibTableColumn
upsControlEcoModeIndex = _UpsControlEcoModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 7, 1, 1),
    _UpsControlEcoModeIndex_Type()
)
upsControlEcoModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlEcoModeIndex.setStatus("mandatory")


class _UpsControlEcoModeStartDay_Type(Integer32):
    """Custom type upsControlEcoModeStartDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsControlEcoModeStartDay_Type.__name__ = "Integer32"
_UpsControlEcoModeStartDay_Object = MibTableColumn
upsControlEcoModeStartDay = _UpsControlEcoModeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 7, 1, 2),
    _UpsControlEcoModeStartDay_Type()
)
upsControlEcoModeStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeStartDay.setStatus("mandatory")


class _UpsControlEcoModeStartTime_Type(DisplayString):
    """Custom type upsControlEcoModeStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlEcoModeStartTime_Type.__name__ = "DisplayString"
_UpsControlEcoModeStartTime_Object = MibTableColumn
upsControlEcoModeStartTime = _UpsControlEcoModeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 7, 1, 3),
    _UpsControlEcoModeStartTime_Type()
)
upsControlEcoModeStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeStartTime.setStatus("mandatory")


class _UpsControlEcoModeEndDay_Type(Integer32):
    """Custom type upsControlEcoModeEndDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsControlEcoModeEndDay_Type.__name__ = "Integer32"
_UpsControlEcoModeEndDay_Object = MibTableColumn
upsControlEcoModeEndDay = _UpsControlEcoModeEndDay_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 7, 1, 4),
    _UpsControlEcoModeEndDay_Type()
)
upsControlEcoModeEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeEndDay.setStatus("mandatory")


class _UpsControlEcoModeEndTime_Type(DisplayString):
    """Custom type upsControlEcoModeEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlEcoModeEndTime_Type.__name__ = "DisplayString"
_UpsControlEcoModeEndTime_Object = MibTableColumn
upsControlEcoModeEndTime = _UpsControlEcoModeEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 8, 7, 1, 5),
    _UpsControlEcoModeEndTime_Type()
)
upsControlEcoModeEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEcoModeEndTime.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9)
)
_UpsConfigInputVoltage_Type = Integer32
_UpsConfigInputVoltage_Object = MibScalar
upsConfigInputVoltage = _UpsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 1),
    _UpsConfigInputVoltage_Type()
)
upsConfigInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigInputVoltage.setStatus("mandatory")
_UpsConfigInputFreq_Type = Integer32
_UpsConfigInputFreq_Object = MibScalar
upsConfigInputFreq = _UpsConfigInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 2),
    _UpsConfigInputFreq_Type()
)
upsConfigInputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigInputFreq.setStatus("mandatory")
_UpsConfigOutputVoltage_Type = Integer32
_UpsConfigOutputVoltage_Object = MibScalar
upsConfigOutputVoltage = _UpsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 3),
    _UpsConfigOutputVoltage_Type()
)
upsConfigOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVoltage.setStatus("mandatory")
_UpsConfigOutputFreq_Type = Integer32
_UpsConfigOutputFreq_Object = MibScalar
upsConfigOutputFreq = _UpsConfigOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 4),
    _UpsConfigOutputFreq_Type()
)
upsConfigOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputFreq.setStatus("mandatory")
_UpsDevicesTable_Object = MibTable
upsDevicesTable = _UpsDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5)
)
if mibBuilder.loadTexts:
    upsDevicesTable.setStatus("mandatory")
_UpsDevicesEntry_Object = MibTableRow
upsDevicesEntry = _UpsDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5, 1)
)
upsDevicesEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "indexOfDevice"),
)
if mibBuilder.loadTexts:
    upsDevicesEntry.setStatus("mandatory")


class _IndexOfDevice_Type(Integer32):
    """Custom type indexOfDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IndexOfDevice_Type.__name__ = "Integer32"
_IndexOfDevice_Object = MibTableColumn
indexOfDevice = _IndexOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5, 1, 1),
    _IndexOfDevice_Type()
)
indexOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexOfDevice.setStatus("mandatory")
_AddrOfDevice_Type = IpAddress
_AddrOfDevice_Object = MibTableColumn
addrOfDevice = _AddrOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5, 1, 2),
    _AddrOfDevice_Type()
)
addrOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrOfDevice.setStatus("mandatory")


class _NameOfDevice_Type(DisplayString):
    """Custom type nameOfDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NameOfDevice_Type.__name__ = "DisplayString"
_NameOfDevice_Object = MibTableColumn
nameOfDevice = _NameOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5, 1, 3),
    _NameOfDevice_Type()
)
nameOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameOfDevice.setStatus("mandatory")
_TimeOfConnection_Type = DisplayString
_TimeOfConnection_Object = MibTableColumn
timeOfConnection = _TimeOfConnection_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5, 1, 4),
    _TimeOfConnection_Type()
)
timeOfConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfConnection.setStatus("mandatory")
_StatusOfConnection_Type = Integer32
_StatusOfConnection_Object = MibTableColumn
statusOfConnection = _StatusOfConnection_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5, 1, 5),
    _StatusOfConnection_Type()
)
statusOfConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusOfConnection.setStatus("mandatory")
_SeverityOfConnection_Type = Integer32
_SeverityOfConnection_Object = MibTableColumn
severityOfConnection = _SeverityOfConnection_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 9, 5, 1, 6),
    _SeverityOfConnection_Type()
)
severityOfConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityOfConnection.setStatus("mandatory")
_UpsAgent_ObjectIdentity = ObjectIdentity
upsAgent = _UpsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10)
)
_UpsAgentIpaddress_Type = IpAddress
_UpsAgentIpaddress_Object = MibScalar
upsAgentIpaddress = _UpsAgentIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 1),
    _UpsAgentIpaddress_Type()
)
upsAgentIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentIpaddress.setStatus("mandatory")
_UpsAgentGateway_Type = IpAddress
_UpsAgentGateway_Object = MibScalar
upsAgentGateway = _UpsAgentGateway_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 2),
    _UpsAgentGateway_Type()
)
upsAgentGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentGateway.setStatus("mandatory")
_UpsAgentSubnetMask_Type = IpAddress
_UpsAgentSubnetMask_Object = MibScalar
upsAgentSubnetMask = _UpsAgentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 3),
    _UpsAgentSubnetMask_Type()
)
upsAgentSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentSubnetMask.setStatus("mandatory")


class _UpsAgentDate_Type(DisplayString):
    """Custom type upsAgentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsAgentDate_Type.__name__ = "DisplayString"
_UpsAgentDate_Object = MibScalar
upsAgentDate = _UpsAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 4),
    _UpsAgentDate_Type()
)
upsAgentDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentDate.setStatus("mandatory")


class _UpsAgentTime_Type(DisplayString):
    """Custom type upsAgentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UpsAgentTime_Type.__name__ = "DisplayString"
_UpsAgentTime_Object = MibScalar
upsAgentTime = _UpsAgentTime_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 5),
    _UpsAgentTime_Type()
)
upsAgentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentTime.setStatus("mandatory")
_UpsAgentNtpTimeServer_Type = DisplayString
_UpsAgentNtpTimeServer_Object = MibScalar
upsAgentNtpTimeServer = _UpsAgentNtpTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 6),
    _UpsAgentNtpTimeServer_Type()
)
upsAgentNtpTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentNtpTimeServer.setStatus("mandatory")


class _UpsAgentNtpTimeZone_Type(Integer32):
    """Custom type upsAgentNtpTimeZone based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("gmt0000london", 28),
          ("gmt0000monrovia", 27),
          ("gmt0100azores", 25),
          ("gmt0100cvi", 26),
          ("gmt0100paris", 31),
          ("gmt0100prague", 30),
          ("gmt0100vienna", 29),
          ("gmt0100wcafrica", 33),
          ("gmt0100zagreb", 32),
          ("gmt0200atlantic", 24),
          ("gmt0200bucharest", 35),
          ("gmt0200cairo", 36),
          ("gmt0200jerusalem", 39),
          ("gmt0200minsk", 34),
          ("gmt0200pretoria", 37),
          ("gmt0200vilnius", 38),
          ("gmt0300brasilia", 21),
          ("gmt0300georgetown", 22),
          ("gmt0300greenland", 23),
          ("gmt0300maghdad", 40),
          ("gmt0300nairobi", 43),
          ("gmt0300newfoundland", 20),
          ("gmt0300riyadh", 41),
          ("gmt0300tehran", 44),
          ("gmt0300volgograd", 42),
          ("gmt0400atime", 17),
          ("gmt0400caracas", 18),
          ("gmt0400kabul", 47),
          ("gmt0400muscat", 45),
          ("gmt0400santiago", 19),
          ("gmt0400yerevan", 46),
          ("gmt0500calcutta", 50),
          ("gmt0500ekaterinburg", 48),
          ("gmt0500etime", 15),
          ("gmt0500indiana", 16),
          ("gmt0500kathmandu", 52),
          ("gmt0500mumbai", 51),
          ("gmt0500quito", 14),
          ("gmt0500tashkent", 49),
          ("gmt0600camerica", 10),
          ("gmt0600ctime", 11),
          ("gmt0600dhaka", 54),
          ("gmt0600guadalajara", 12),
          ("gmt0600jayawardenepura", 55),
          ("gmt0600novosibirsk", 53),
          ("gmt0600rangoon", 56),
          ("gmt0600saskatchewan", 13),
          ("gmt0700arizona", 7),
          ("gmt0700bangkok", 57),
          ("gmt0700chihuahua", 8),
          ("gmt0700krasnoyarsk", 58),
          ("gmt0700mountain", 9),
          ("gmt0800beijing", 59),
          ("gmt0800irkutsk", 60),
          ("gmt0800perth", 62),
          ("gmt0800singapore", 61),
          ("gmt0800taipei", 63),
          ("gmt0800tijuana", 6),
          ("gmt0900adelaide", 67),
          ("gmt0900alaska", 5),
          ("gmt0900darwin", 68),
          ("gmt0900seoul", 65),
          ("gmt0900tokyo", 64),
          ("gmt0900yakutsk", 66),
          ("gmt1000brisbane", 69),
          ("gmt1000canberra", 70),
          ("gmt1000guam", 71),
          ("gmt1000hawaii", 4),
          ("gmt1000hobart", 72),
          ("gmt1000vladivostok", 73),
          ("gmt1100magadan", 74),
          ("gmt1100samoa", 3),
          ("gmt1200auckland", 75),
          ("gmt1200dateLineWest", 1),
          ("gmt1200fiji", 76),
          ("gmt1200kwajalein", 2),
          ("gmt1300alofa", 77))
    )


_UpsAgentNtpTimeZone_Type.__name__ = "Integer32"
_UpsAgentNtpTimeZone_Object = MibScalar
upsAgentNtpTimeZone = _UpsAgentNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 7),
    _UpsAgentNtpTimeZone_Type()
)
upsAgentNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentNtpTimeZone.setStatus("mandatory")


class _UpsAgentHistoryLogFrequency_Type(Integer32):
    """Custom type upsAgentHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 21600),
    )


_UpsAgentHistoryLogFrequency_Type.__name__ = "Integer32"
_UpsAgentHistoryLogFrequency_Object = MibScalar
upsAgentHistoryLogFrequency = _UpsAgentHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 8),
    _UpsAgentHistoryLogFrequency_Type()
)
upsAgentHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentHistoryLogFrequency.setStatus("mandatory")


class _UpsAgentExtHistoryLogFrequency_Type(Integer32):
    """Custom type upsAgentExtHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10080),
    )


_UpsAgentExtHistoryLogFrequency_Type.__name__ = "Integer32"
_UpsAgentExtHistoryLogFrequency_Object = MibScalar
upsAgentExtHistoryLogFrequency = _UpsAgentExtHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 9),
    _UpsAgentExtHistoryLogFrequency_Type()
)
upsAgentExtHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentExtHistoryLogFrequency.setStatus("mandatory")


class _UpsAgentPollRate_Type(Integer32):
    """Custom type upsAgentPollRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_UpsAgentPollRate_Type.__name__ = "Integer32"
_UpsAgentPollRate_Object = MibScalar
upsAgentPollRate = _UpsAgentPollRate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 10),
    _UpsAgentPollRate_Type()
)
upsAgentPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentPollRate.setStatus("mandatory")


class _UpsAgentBaudRate_Type(Integer32):
    """Custom type upsAgentBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("br19200", 3),
          ("br2400", 1),
          ("br9600", 2))
    )


_UpsAgentBaudRate_Type.__name__ = "Integer32"
_UpsAgentBaudRate_Object = MibScalar
upsAgentBaudRate = _UpsAgentBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 11),
    _UpsAgentBaudRate_Type()
)
upsAgentBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentBaudRate.setStatus("mandatory")


class _UpsAgentDhcpStatus_Type(Integer32):
    """Custom type upsAgentDhcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_UpsAgentDhcpStatus_Type.__name__ = "Integer32"
_UpsAgentDhcpStatus_Object = MibScalar
upsAgentDhcpStatus = _UpsAgentDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 12),
    _UpsAgentDhcpStatus_Type()
)
upsAgentDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentDhcpStatus.setStatus("mandatory")


class _UpsAgentTelnetStatus_Type(Integer32):
    """Custom type upsAgentTelnetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_UpsAgentTelnetStatus_Type.__name__ = "Integer32"
_UpsAgentTelnetStatus_Object = MibScalar
upsAgentTelnetStatus = _UpsAgentTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 13),
    _UpsAgentTelnetStatus_Type()
)
upsAgentTelnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentTelnetStatus.setStatus("mandatory")


class _UpsAgentTftpStatus_Type(Integer32):
    """Custom type upsAgentTftpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_UpsAgentTftpStatus_Type.__name__ = "Integer32"
_UpsAgentTftpStatus_Object = MibScalar
upsAgentTftpStatus = _UpsAgentTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 14),
    _UpsAgentTftpStatus_Type()
)
upsAgentTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentTftpStatus.setStatus("mandatory")


class _UpsAgentResetToDefault_Type(Integer32):
    """Custom type upsAgentResetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("reset", 1))
    )


_UpsAgentResetToDefault_Type.__name__ = "Integer32"
_UpsAgentResetToDefault_Object = MibScalar
upsAgentResetToDefault = _UpsAgentResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 15),
    _UpsAgentResetToDefault_Type()
)
upsAgentResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentResetToDefault.setStatus("mandatory")


class _UpsAgentRestart_Type(Integer32):
    """Custom type upsAgentRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("restart", 1))
    )


_UpsAgentRestart_Type.__name__ = "Integer32"
_UpsAgentRestart_Object = MibScalar
upsAgentRestart = _UpsAgentRestart_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 16),
    _UpsAgentRestart_Type()
)
upsAgentRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentRestart.setStatus("mandatory")


class _UpsAgentClearAgentLog_Type(Integer32):
    """Custom type upsAgentClearAgentLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_UpsAgentClearAgentLog_Type.__name__ = "Integer32"
_UpsAgentClearAgentLog_Object = MibScalar
upsAgentClearAgentLog = _UpsAgentClearAgentLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 17),
    _UpsAgentClearAgentLog_Type()
)
upsAgentClearAgentLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearAgentLog.setStatus("mandatory")


class _UpsAgentClearEventLog_Type(Integer32):
    """Custom type upsAgentClearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_UpsAgentClearEventLog_Type.__name__ = "Integer32"
_UpsAgentClearEventLog_Object = MibScalar
upsAgentClearEventLog = _UpsAgentClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 18),
    _UpsAgentClearEventLog_Type()
)
upsAgentClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearEventLog.setStatus("mandatory")


class _UpsAgentClearExtHistoryLog_Type(Integer32):
    """Custom type upsAgentClearExtHistoryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_UpsAgentClearExtHistoryLog_Type.__name__ = "Integer32"
_UpsAgentClearExtHistoryLog_Object = MibScalar
upsAgentClearExtHistoryLog = _UpsAgentClearExtHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 19),
    _UpsAgentClearExtHistoryLog_Type()
)
upsAgentClearExtHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearExtHistoryLog.setStatus("mandatory")


class _UpsAgentClearHistoryLog_Type(Integer32):
    """Custom type upsAgentClearHistoryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_UpsAgentClearHistoryLog_Type.__name__ = "Integer32"
_UpsAgentClearHistoryLog_Object = MibScalar
upsAgentClearHistoryLog = _UpsAgentClearHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 20),
    _UpsAgentClearHistoryLog_Type()
)
upsAgentClearHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAgentClearHistoryLog.setStatus("mandatory")
_UpsAgentTrapsReceiversTable_Object = MibTable
upsAgentTrapsReceiversTable = _UpsAgentTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 21)
)
if mibBuilder.loadTexts:
    upsAgentTrapsReceiversTable.setStatus("mandatory")
_UpsAgentTrapsReceiversEntry_Object = MibTableRow
upsAgentTrapsReceiversEntry = _UpsAgentTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 21, 1)
)
upsAgentTrapsReceiversEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    upsAgentTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 21, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = DisplayString
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 21, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverCommunityString_Type(DisplayString):
    """Custom type receiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ReceiverCommunityString_Type.__name__ = "DisplayString"
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 21, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("mandatory")


class _ReceiverDescription_Type(DisplayString):
    """Custom type receiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReceiverDescription_Type.__name__ = "DisplayString"
_ReceiverDescription_Object = MibTableColumn
receiverDescription = _ReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 21, 1, 4),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_UpsAgentAccessControlTable_Object = MibTable
upsAgentAccessControlTable = _UpsAgentAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 22)
)
if mibBuilder.loadTexts:
    upsAgentAccessControlTable.setStatus("mandatory")
_UpsAgentAccessControlEntry_Object = MibTableRow
upsAgentAccessControlEntry = _UpsAgentAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 22, 1)
)
upsAgentAccessControlEntry.setIndexNames(
    (0, "SOCOMECUPS-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    upsAgentAccessControlEntry.setStatus("mandatory")
_AccessIndex_Type = Integer32
_AccessIndex_Object = MibTableColumn
accessIndex = _AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 22, 1, 1),
    _AccessIndex_Type()
)
accessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessIndex.setStatus("mandatory")
_AccessControlAddr_Type = DisplayString
_AccessControlAddr_Object = MibTableColumn
accessControlAddr = _AccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 22, 1, 2),
    _AccessControlAddr_Type()
)
accessControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlAddr.setStatus("mandatory")


class _AccessCommunityString_Type(DisplayString):
    """Custom type accessCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AccessCommunityString_Type.__name__ = "DisplayString"
_AccessCommunityString_Object = MibTableColumn
accessCommunityString = _AccessCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 22, 1, 3),
    _AccessCommunityString_Type()
)
accessCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCommunityString.setStatus("mandatory")


class _AccessControlMode_Type(Integer32):
    """Custom type accessControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAccess", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_AccessControlMode_Type.__name__ = "Integer32"
_AccessControlMode_Object = MibTableColumn
accessControlMode = _AccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 22, 1, 4),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("mandatory")
_UpsAgentMibVersion_Type = Integer32
_UpsAgentMibVersion_Object = MibScalar
upsAgentMibVersion = _UpsAgentMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 23),
    _UpsAgentMibVersion_Type()
)
upsAgentMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAgentMibVersion.setStatus("mandatory")
_UpsAgentTrapString_Type = DisplayString
_UpsAgentTrapString_Object = MibScalar
upsAgentTrapString = _UpsAgentTrapString_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 10, 50),
    _UpsAgentTrapString_Type()
)
upsAgentTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAgentTrapString.setStatus("mandatory")
_EmdStatus_ObjectIdentity = ObjectIdentity
emdStatus = _EmdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 11)
)
_EmdSatatusTemperature_Type = Integer32
_EmdSatatusTemperature_Object = MibScalar
emdSatatusTemperature = _EmdSatatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 11, 1),
    _EmdSatatusTemperature_Type()
)
emdSatatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusTemperature.setStatus("mandatory")
_EmdSatatusHumidity_Type = Integer32
_EmdSatatusHumidity_Object = MibScalar
emdSatatusHumidity = _EmdSatatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 1, 11, 2),
    _EmdSatatusHumidity_Type()
)
emdSatatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusHumidity.setStatus("mandatory")
_UpsTraps_ObjectIdentity = ObjectIdentity
upsTraps = _UpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2)
)

# Managed Objects groups


# Notification objects

upsTrapOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 1)
)
upsTrapOnBattery.setObjects(
      *(("SOCOMECUPS-MIB", "upsEstimatedMinutesRemaining"),
        ("SOCOMECUPS-MIB", "upsSecondsOnBattery"))
)
if mibBuilder.loadTexts:
    upsTrapOnBattery.setStatus(
        ""
    )

upsTrapTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 2)
)
upsTrapTestCompleted.setObjects(
      *(("SOCOMECUPS-MIB", "upsTestId"),
        ("SOCOMECUPS-MIB", "upsTestSpinLock"),
        ("SOCOMECUPS-MIB", "upsTestResultsSummary"),
        ("SOCOMECUPS-MIB", "upsTestResultsDetail"),
        ("SOCOMECUPS-MIB", "upsTestStartTime"),
        ("SOCOMECUPS-MIB", "upsTestElapsedTime"))
)
if mibBuilder.loadTexts:
    upsTrapTestCompleted.setStatus(
        ""
    )

upsTrapAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 3)
)
upsTrapAlarmEntryAdded.setObjects(
      *(("SOCOMECUPS-MIB", "upsAlarmId"),
        ("SOCOMECUPS-MIB", "upsAlarmDescr"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmEntryAdded.setStatus(
        ""
    )

upsTrapAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 4)
)
upsTrapAlarmEntryRemoved.setObjects(
      *(("SOCOMECUPS-MIB", "upsAlarmId"),
        ("SOCOMECUPS-MIB", "upsAlarmDescr"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmEntryRemoved.setStatus(
        ""
    )

upsTrapUpsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 5)
)
upsTrapUpsNormal.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapUpsNormal.setStatus(
        ""
    )

upsTrapUpsBattTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 6)
)
upsTrapUpsBattTestFailed.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapUpsBattTestFailed.setStatus(
        ""
    )

upsTrapOnBatteryPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 7)
)
upsTrapOnBatteryPower.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapOnBatteryPower.setStatus(
        ""
    )

upsTrapBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 8)
)
upsTrapBatteryLow.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapBatteryLow.setStatus(
        ""
    )

upsTrapPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 9)
)
upsTrapPowerRestored.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapPowerRestored.setStatus(
        ""
    )

upsTrapImminentStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 10)
)
upsTrapImminentStop.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapImminentStop.setStatus(
        ""
    )

upsTrapTurnedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 11)
)
upsTrapTurnedOff.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapTurnedOff.setStatus(
        ""
    )

upsTrapOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 12)
)
upsTrapOverTemperature.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapOverTemperature.setStatus(
        ""
    )

upsTrapOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 13)
)
upsTrapOverload.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapOverload.setStatus(
        ""
    )

upsTrapOnMains = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 14)
)
upsTrapOnMains.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapOnMains.setStatus(
        ""
    )

upsTrapRedoundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 15)
)
upsTrapRedoundancyLost.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapRedoundancyLost.setStatus(
        ""
    )

upsTrapEmdTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 16)
)
upsTrapEmdTempLow.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdTempLow.setStatus(
        ""
    )

upsTrapEmdTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 17)
)
upsTrapEmdTempHigh.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdTempHigh.setStatus(
        ""
    )

upsTrapEmdHumidityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 18)
)
upsTrapEmdHumidityLow.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdHumidityLow.setStatus(
        ""
    )

upsTrapEmdHumidityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 19)
)
upsTrapEmdHumidityHigh.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdHumidityHigh.setStatus(
        ""
    )

upsTrapEmdFirstInputActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 20)
)
upsTrapEmdFirstInputActive.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdFirstInputActive.setStatus(
        ""
    )

upsTrapEmdFirstInputRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 21)
)
upsTrapEmdFirstInputRestored.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdFirstInputRestored.setStatus(
        ""
    )

upsTrapEmdSecondInputActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 22)
)
upsTrapEmdSecondInputActive.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdSecondInputActive.setStatus(
        ""
    )

upsTrapEmdSecondInputRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 4555, 1, 1, 1, 2, 0, 23)
)
upsTrapEmdSecondInputRestored.setObjects(
    ("SOCOMECUPS-MIB", "upsAgentTrapString")
)
if mibBuilder.loadTexts:
    upsTrapEmdSecondInputRestored.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SOCOMECUPS-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "socomecSicon": socomecSicon,
       "software": software,
       "network": network,
       "netvision": netvision,
       "upsObjects": upsObjects,
       "upsIdent": upsIdent,
       "upsIdentModel": upsIdentModel,
       "upsIdentUPSFirmwareVersion": upsIdentUPSFirmwareVersion,
       "upsIdentAgentSoftwareVersion": upsIdentAgentSoftwareVersion,
       "upsIdentUpsSerialNumber": upsIdentUpsSerialNumber,
       "upsBattery": upsBattery,
       "upsBatteryStatus": upsBatteryStatus,
       "upsSecondsOnBattery": upsSecondsOnBattery,
       "upsEstimatedMinutesRemaining": upsEstimatedMinutesRemaining,
       "upsEstimatedChargeRemaining": upsEstimatedChargeRemaining,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsInput": upsInput,
       "upsInputNumLines": upsInputNumLines,
       "upsInputFrequency": upsInputFrequency,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputLineIndex": upsInputLineIndex,
       "upsInputVoltage": upsInputVoltage,
       "upsInputCurrent": upsInputCurrent,
       "upsInputVoltageMax": upsInputVoltageMax,
       "upsInputVoltageMin": upsInputVoltageMin,
       "upsOutput": upsOutput,
       "upsOutputSource": upsOutputSource,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputNumLines": upsOutputNumLines,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputLineIndex": upsOutputLineIndex,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputPercentLoad": upsOutputPercentLoad,
       "upsOutputKva": upsOutputKva,
       "upsBypass": upsBypass,
       "upsBypassFrequency": upsBypassFrequency,
       "upsBypassNumLines": upsBypassNumLines,
       "upsBypassTable": upsBypassTable,
       "upsBypassEntry": upsBypassEntry,
       "upsBypassLineIndex": upsBypassLineIndex,
       "upsBypassVoltage": upsBypassVoltage,
       "upsBypassCurrent": upsBypassCurrent,
       "upsAlarm": upsAlarm,
       "upsAlarmsPresent": upsAlarmsPresent,
       "upsAlarmTable": upsAlarmTable,
       "upsAlarmEntry": upsAlarmEntry,
       "upsAlarmId": upsAlarmId,
       "upsAlarmDescr": upsAlarmDescr,
       "upsAlarmTime": upsAlarmTime,
       "upsAlarmExtDes": upsAlarmExtDes,
       "upsWellKnownAlarms": upsWellKnownAlarms,
       "upsAlarmBatteryBad": upsAlarmBatteryBad,
       "upsAlarmOnBattery": upsAlarmOnBattery,
       "upsAlarmLowBattery": upsAlarmLowBattery,
       "upsAlarmDepletedBattery": upsAlarmDepletedBattery,
       "upsAlarmTempBad": upsAlarmTempBad,
       "upsAlarmInputBad": upsAlarmInputBad,
       "upsAlarmOutputBad": upsAlarmOutputBad,
       "upsAlarmOutputOverload": upsAlarmOutputOverload,
       "upsAlarmOnBypass": upsAlarmOnBypass,
       "upsAlarmBypassBad": upsAlarmBypassBad,
       "upsAlarmOutputOffAsRequested": upsAlarmOutputOffAsRequested,
       "upsAlarmUpsOffAsRequested": upsAlarmUpsOffAsRequested,
       "upsAlarmChargerFailed": upsAlarmChargerFailed,
       "upsAlarmUpsOutputOff": upsAlarmUpsOutputOff,
       "upsAlarmUpsSystemOff": upsAlarmUpsSystemOff,
       "upsAlarmFanFailure": upsAlarmFanFailure,
       "upsAlarmFuseFailure": upsAlarmFuseFailure,
       "upsAlarmGeneralFault": upsAlarmGeneralFault,
       "upsAlarmDiagnosticTestFailed": upsAlarmDiagnosticTestFailed,
       "upsAlarmCommunicationLost": upsAlarmCommunicationLost,
       "upsAlarmAwaitingPower": upsAlarmAwaitingPower,
       "upsAlarmShutdownPending": upsAlarmShutdownPending,
       "upsAlarmShutdownImminent": upsAlarmShutdownImminent,
       "upsAlarmTestInProgress": upsAlarmTestInProgress,
       "upsAlarmPowerSupplyFault": upsAlarmPowerSupplyFault,
       "upsAlarmAuxMainFail": upsAlarmAuxMainFail,
       "upsAlarmManualBypassClose": upsAlarmManualBypassClose,
       "upsAlarmShortCircuit": upsAlarmShortCircuit,
       "upsAlarmBatteryChargerFailure": upsAlarmBatteryChargerFailure,
       "upsAlarmInverterOverCurrent": upsAlarmInverterOverCurrent,
       "upsAlarmInverterDistorsion": upsAlarmInverterDistorsion,
       "upsAlarmPrechargeVoltageFail": upsAlarmPrechargeVoltageFail,
       "upsAlarmBoostTooLow": upsAlarmBoostTooLow,
       "upsAlarmBoostTooHigh": upsAlarmBoostTooHigh,
       "upsAlarmBatteryTooHigh": upsAlarmBatteryTooHigh,
       "upsAlarmImproperCondition": upsAlarmImproperCondition,
       "upsAlarmOverloadTimeout": upsAlarmOverloadTimeout,
       "upsAlarmControlSystemFailure": upsAlarmControlSystemFailure,
       "upsAlarmDataCorrupted": upsAlarmDataCorrupted,
       "upsAlarmPllFault": upsAlarmPllFault,
       "upsAlarmInputGeneralAlarm": upsAlarmInputGeneralAlarm,
       "upsAlarmRectifierGeneralAlarm": upsAlarmRectifierGeneralAlarm,
       "upsAlarmBoostGeneralAlarm": upsAlarmBoostGeneralAlarm,
       "upsAlarmInverterGeneralAlarm": upsAlarmInverterGeneralAlarm,
       "upsAlarmBatteryGeneralAlarm": upsAlarmBatteryGeneralAlarm,
       "upsAlarmOutputOver": upsAlarmOutputOver,
       "upsAlarmOutputUnder": upsAlarmOutputUnder,
       "upsAlarmBypassGeneralAlarm": upsAlarmBypassGeneralAlarm,
       "upsAlarmStopForOverload": upsAlarmStopForOverload,
       "upsAlarmImminentStop": upsAlarmImminentStop,
       "upsAlarmModule1Alarm": upsAlarmModule1Alarm,
       "upsAlarmModule2Alarm": upsAlarmModule2Alarm,
       "upsAlarmModule3Alarm": upsAlarmModule3Alarm,
       "upsAlarmModule4Alarm": upsAlarmModule4Alarm,
       "upsAlarmModule5Alarm": upsAlarmModule5Alarm,
       "upsAlarmModule6Alarm": upsAlarmModule6Alarm,
       "upsAlarmExternalAlarm1": upsAlarmExternalAlarm1,
       "upsAlarmExternalAlarm2": upsAlarmExternalAlarm2,
       "upsAlarmExternalAlarm3": upsAlarmExternalAlarm3,
       "upsAlarmExternalAlarm4": upsAlarmExternalAlarm4,
       "upsAlarmEService": upsAlarmEService,
       "upsAlarmRedundancyLost": upsAlarmRedundancyLost,
       "upsAlarmPeriodicServiceCheck": upsAlarmPeriodicServiceCheck,
       "upsAlarmAllTransferDisabled": upsAlarmAllTransferDisabled,
       "upsAlarmAutoTransferDisabled": upsAlarmAutoTransferDisabled,
       "upsAlarmBatteryRoom": upsAlarmBatteryRoom,
       "upsAlarmManualBypass": upsAlarmManualBypass,
       "upsAlarmBatteryDischarged": upsAlarmBatteryDischarged,
       "upsAlarmInsufficientResources": upsAlarmInsufficientResources,
       "upsAlarmOptionalBoards": upsAlarmOptionalBoards,
       "upsAlarmRectifierFault": upsAlarmRectifierFault,
       "upsAlarmBoostFault": upsAlarmBoostFault,
       "upsAlarmInverterFault": upsAlarmInverterFault,
       "upsAlarmParallelModuleFault": upsAlarmParallelModuleFault,
       "upsAlarmGenSetGeneral": upsAlarmGenSetGeneral,
       "upsAlarmGenSetFault": upsAlarmGenSetFault,
       "upsAlarmEmergencyStopActive": upsAlarmEmergencyStopActive,
       "upsAlarmBatteryCircuitOpen": upsAlarmBatteryCircuitOpen,
       "upsAlarmFansFailure": upsAlarmFansFailure,
       "upsAlarmPhaseRotationFault": upsAlarmPhaseRotationFault,
       "upsAlarmA62": upsAlarmA62,
       "upsAlarmA63": upsAlarmA63,
       "upsTest": upsTest,
       "upsTestId": upsTestId,
       "upsTestSpinLock": upsTestSpinLock,
       "upsTestResultsSummary": upsTestResultsSummary,
       "upsTestResultsDetail": upsTestResultsDetail,
       "upsTestStartTime": upsTestStartTime,
       "upsTestElapsedTime": upsTestElapsedTime,
       "upsWellKnownTests": upsWellKnownTests,
       "upsTestNoTestsInitiated": upsTestNoTestsInitiated,
       "upsTestAbortTestInProgress": upsTestAbortTestInProgress,
       "upsTestGeneralSystemsTest": upsTestGeneralSystemsTest,
       "upsTestQuickBatteryTest": upsTestQuickBatteryTest,
       "upsDeepBatteryCalibration": upsDeepBatteryCalibration,
       "upsControl": upsControl,
       "upsControlStatusControl": upsControlStatusControl,
       "upsShutdownDelay": upsShutdownDelay,
       "upsTurnOffAfterShutdown": upsTurnOffAfterShutdown,
       "upsControlShutdownParametersTable": upsControlShutdownParametersTable,
       "shutdownParametersEntry": shutdownParametersEntry,
       "upsControlEventDescr": upsControlEventDescr,
       "upsControlEventStatus": upsControlEventStatus,
       "upsControlDelay": upsControlDelay,
       "upsControlFirstWarning": upsControlFirstWarning,
       "upsControlWarningInterval": upsControlWarningInterval,
       "upsControlSeverity": upsControlSeverity,
       "upsControlWeeklyScheduleTable": upsControlWeeklyScheduleTable,
       "upsControlWeeklyScheduleEntry": upsControlWeeklyScheduleEntry,
       "upsControlWeeklyIndex": upsControlWeeklyIndex,
       "upsControlWeeklyShutdownDay": upsControlWeeklyShutdownDay,
       "upsControlWeeklyShutdownTime": upsControlWeeklyShutdownTime,
       "upsControlWeeklyRestartDay": upsControlWeeklyRestartDay,
       "upsControlWeeklyRestartTime": upsControlWeeklyRestartTime,
       "upsControlSpecialScheduleTable": upsControlSpecialScheduleTable,
       "upsControlSpecialScheduleEntry": upsControlSpecialScheduleEntry,
       "upsControlSpecialIndex": upsControlSpecialIndex,
       "upsControlSpecialShutdownDay": upsControlSpecialShutdownDay,
       "upsControlSpecialShutdownTime": upsControlSpecialShutdownTime,
       "upsControlSpecialRestartDay": upsControlSpecialRestartDay,
       "upsControlSpecialRestartTime": upsControlSpecialRestartTime,
       "upsControlEcoModeScheduleTable": upsControlEcoModeScheduleTable,
       "upsControlEcoModeScheduleEntry": upsControlEcoModeScheduleEntry,
       "upsControlEcoModeIndex": upsControlEcoModeIndex,
       "upsControlEcoModeStartDay": upsControlEcoModeStartDay,
       "upsControlEcoModeStartTime": upsControlEcoModeStartTime,
       "upsControlEcoModeEndDay": upsControlEcoModeEndDay,
       "upsControlEcoModeEndTime": upsControlEcoModeEndTime,
       "upsConfig": upsConfig,
       "upsConfigInputVoltage": upsConfigInputVoltage,
       "upsConfigInputFreq": upsConfigInputFreq,
       "upsConfigOutputVoltage": upsConfigOutputVoltage,
       "upsConfigOutputFreq": upsConfigOutputFreq,
       "upsDevicesTable": upsDevicesTable,
       "upsDevicesEntry": upsDevicesEntry,
       "indexOfDevice": indexOfDevice,
       "addrOfDevice": addrOfDevice,
       "nameOfDevice": nameOfDevice,
       "timeOfConnection": timeOfConnection,
       "statusOfConnection": statusOfConnection,
       "severityOfConnection": severityOfConnection,
       "upsAgent": upsAgent,
       "upsAgentIpaddress": upsAgentIpaddress,
       "upsAgentGateway": upsAgentGateway,
       "upsAgentSubnetMask": upsAgentSubnetMask,
       "upsAgentDate": upsAgentDate,
       "upsAgentTime": upsAgentTime,
       "upsAgentNtpTimeServer": upsAgentNtpTimeServer,
       "upsAgentNtpTimeZone": upsAgentNtpTimeZone,
       "upsAgentHistoryLogFrequency": upsAgentHistoryLogFrequency,
       "upsAgentExtHistoryLogFrequency": upsAgentExtHistoryLogFrequency,
       "upsAgentPollRate": upsAgentPollRate,
       "upsAgentBaudRate": upsAgentBaudRate,
       "upsAgentDhcpStatus": upsAgentDhcpStatus,
       "upsAgentTelnetStatus": upsAgentTelnetStatus,
       "upsAgentTftpStatus": upsAgentTftpStatus,
       "upsAgentResetToDefault": upsAgentResetToDefault,
       "upsAgentRestart": upsAgentRestart,
       "upsAgentClearAgentLog": upsAgentClearAgentLog,
       "upsAgentClearEventLog": upsAgentClearEventLog,
       "upsAgentClearExtHistoryLog": upsAgentClearExtHistoryLog,
       "upsAgentClearHistoryLog": upsAgentClearHistoryLog,
       "upsAgentTrapsReceiversTable": upsAgentTrapsReceiversTable,
       "upsAgentTrapsReceiversEntry": upsAgentTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "receiverDescription": receiverDescription,
       "upsAgentAccessControlTable": upsAgentAccessControlTable,
       "upsAgentAccessControlEntry": upsAgentAccessControlEntry,
       "accessIndex": accessIndex,
       "accessControlAddr": accessControlAddr,
       "accessCommunityString": accessCommunityString,
       "accessControlMode": accessControlMode,
       "upsAgentMibVersion": upsAgentMibVersion,
       "upsAgentTrapString": upsAgentTrapString,
       "emdStatus": emdStatus,
       "emdSatatusTemperature": emdSatatusTemperature,
       "emdSatatusHumidity": emdSatatusHumidity,
       "upsTraps": upsTraps,
       "upsTrapOnBattery": upsTrapOnBattery,
       "upsTrapTestCompleted": upsTrapTestCompleted,
       "upsTrapAlarmEntryAdded": upsTrapAlarmEntryAdded,
       "upsTrapAlarmEntryRemoved": upsTrapAlarmEntryRemoved,
       "upsTrapUpsNormal": upsTrapUpsNormal,
       "upsTrapUpsBattTestFailed": upsTrapUpsBattTestFailed,
       "upsTrapOnBatteryPower": upsTrapOnBatteryPower,
       "upsTrapBatteryLow": upsTrapBatteryLow,
       "upsTrapPowerRestored": upsTrapPowerRestored,
       "upsTrapImminentStop": upsTrapImminentStop,
       "upsTrapTurnedOff": upsTrapTurnedOff,
       "upsTrapOverTemperature": upsTrapOverTemperature,
       "upsTrapOverload": upsTrapOverload,
       "upsTrapOnMains": upsTrapOnMains,
       "upsTrapRedoundancyLost": upsTrapRedoundancyLost,
       "upsTrapEmdTempLow": upsTrapEmdTempLow,
       "upsTrapEmdTempHigh": upsTrapEmdTempHigh,
       "upsTrapEmdHumidityLow": upsTrapEmdHumidityLow,
       "upsTrapEmdHumidityHigh": upsTrapEmdHumidityHigh,
       "upsTrapEmdFirstInputActive": upsTrapEmdFirstInputActive,
       "upsTrapEmdFirstInputRestored": upsTrapEmdFirstInputRestored,
       "upsTrapEmdSecondInputActive": upsTrapEmdSecondInputActive,
       "upsTrapEmdSecondInputRestored": upsTrapEmdSecondInputRestored}
)
