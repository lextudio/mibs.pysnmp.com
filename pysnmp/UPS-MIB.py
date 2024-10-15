# SNMP MIB module (UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:54 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

upsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_UpsObjects_ObjectIdentity = ObjectIdentity
upsObjects = _UpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 1)
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
    (1, 3, 6, 1, 2, 1, 33, 1, 1, 1),
    _UpsIdentManufacturer_Type()
)
upsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturer.setStatus("current")


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 1, 2),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("current")


class _UpsIdentUPSSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentUPSSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentUPSSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentUPSSoftwareVersion_Object = MibScalar
upsIdentUPSSoftwareVersion = _UpsIdentUPSSoftwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 1, 3),
    _UpsIdentUPSSoftwareVersion_Type()
)
upsIdentUPSSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersion.setStatus("current")


class _UpsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentAgentSoftwareVersion_Object = MibScalar
upsIdentAgentSoftwareVersion = _UpsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 1, 4),
    _UpsIdentAgentSoftwareVersion_Type()
)
upsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersion.setStatus("current")


class _UpsIdentName_Type(DisplayString):
    """Custom type upsIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentName_Type.__name__ = "DisplayString"
_UpsIdentName_Object = MibScalar
upsIdentName = _UpsIdentName_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 1, 5),
    _UpsIdentName_Type()
)
upsIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentName.setStatus("current")


class _UpsIdentAttachedDevices_Type(DisplayString):
    """Custom type upsIdentAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentAttachedDevices_Type.__name__ = "DisplayString"
_UpsIdentAttachedDevices_Object = MibScalar
upsIdentAttachedDevices = _UpsIdentAttachedDevices_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 1, 6),
    _UpsIdentAttachedDevices_Type()
)
upsIdentAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevices.setStatus("current")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 2)
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
    (1, 3, 6, 1, 2, 1, 33, 1, 2, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("current")
_UpsSecondsOnBattery_Type = NonNegativeInteger
_UpsSecondsOnBattery_Object = MibScalar
upsSecondsOnBattery = _UpsSecondsOnBattery_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 2, 2),
    _UpsSecondsOnBattery_Type()
)
upsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBattery.setUnits("seconds")
_UpsEstimatedMinutesRemaining_Type = PositiveInteger
_UpsEstimatedMinutesRemaining_Object = MibScalar
upsEstimatedMinutesRemaining = _UpsEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 2, 3),
    _UpsEstimatedMinutesRemaining_Type()
)
upsEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemaining.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemaining.setUnits("minutes")


class _UpsEstimatedChargeRemaining_Type(Integer32):
    """Custom type upsEstimatedChargeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemaining_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemaining_Object = MibScalar
upsEstimatedChargeRemaining = _UpsEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 2, 4),
    _UpsEstimatedChargeRemaining_Type()
)
upsEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaining.setUnits("percent")
_UpsBatteryVoltage_Type = NonNegativeInteger
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 2, 5),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setUnits("0.1 Volt DC")
_UpsBatteryCurrent_Type = Integer32
_UpsBatteryCurrent_Object = MibScalar
upsBatteryCurrent = _UpsBatteryCurrent_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 2, 6),
    _UpsBatteryCurrent_Type()
)
upsBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrent.setUnits("0.1 Amp DC")
_UpsBatteryTemperature_Type = Integer32
_UpsBatteryTemperature_Object = MibScalar
upsBatteryTemperature = _UpsBatteryTemperature_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 2, 7),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setUnits("degrees Centigrade")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 3)
)
_UpsInputLineBads_Type = Counter32
_UpsInputLineBads_Object = MibScalar
upsInputLineBads = _UpsInputLineBads_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 1),
    _UpsInputLineBads_Type()
)
upsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBads.setStatus("current")
_UpsInputNumLines_Type = NonNegativeInteger
_UpsInputNumLines_Object = MibScalar
upsInputNumLines = _UpsInputNumLines_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 2),
    _UpsInputNumLines_Type()
)
upsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLines.setStatus("current")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("current")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1)
)
upsInputEntry.setIndexNames(
    (0, "UPS-MIB", "upsInputLineIndex"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("current")
_UpsInputLineIndex_Type = PositiveInteger
_UpsInputLineIndex_Object = MibTableColumn
upsInputLineIndex = _UpsInputLineIndex_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 1),
    _UpsInputLineIndex_Type()
)
upsInputLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndex.setStatus("current")
_UpsInputFrequency_Type = NonNegativeInteger
_UpsInputFrequency_Object = MibTableColumn
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 2),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequency.setUnits("0.1 Hertz")
_UpsInputVoltage_Type = NonNegativeInteger
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 3),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltage.setUnits("RMS Volts")
_UpsInputCurrent_Type = NonNegativeInteger
_UpsInputCurrent_Object = MibTableColumn
upsInputCurrent = _UpsInputCurrent_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 4),
    _UpsInputCurrent_Type()
)
upsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrent.setUnits("0.1 RMS Amp")
_UpsInputTruePower_Type = NonNegativeInteger
_UpsInputTruePower_Object = MibTableColumn
upsInputTruePower = _UpsInputTruePower_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 3, 3, 1, 5),
    _UpsInputTruePower_Type()
)
upsInputTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePower.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePower.setUnits("Watts")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 4)
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
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 1),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("current")
_UpsOutputFrequency_Type = NonNegativeInteger
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequency.setUnits("0.1 Hertz")
_UpsOutputNumLines_Type = NonNegativeInteger
_UpsOutputNumLines_Object = MibScalar
upsOutputNumLines = _UpsOutputNumLines_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 3),
    _UpsOutputNumLines_Type()
)
upsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLines.setStatus("current")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("current")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1)
)
upsOutputEntry.setIndexNames(
    (0, "UPS-MIB", "upsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("current")
_UpsOutputLineIndex_Type = PositiveInteger
_UpsOutputLineIndex_Object = MibTableColumn
upsOutputLineIndex = _UpsOutputLineIndex_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 1),
    _UpsOutputLineIndex_Type()
)
upsOutputLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndex.setStatus("current")
_UpsOutputVoltage_Type = NonNegativeInteger
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltage.setUnits("RMS Volts")
_UpsOutputCurrent_Type = NonNegativeInteger
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrent.setUnits("0.1 RMS Amp")
_UpsOutputPower_Type = NonNegativeInteger
_UpsOutputPower_Object = MibTableColumn
upsOutputPower = _UpsOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 4),
    _UpsOutputPower_Type()
)
upsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPower.setUnits("Watts")


class _UpsOutputPercentLoad_Type(Integer32):
    """Custom type upsOutputPercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoad_Type.__name__ = "Integer32"
_UpsOutputPercentLoad_Object = MibTableColumn
upsOutputPercentLoad = _UpsOutputPercentLoad_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 4, 4, 1, 5),
    _UpsOutputPercentLoad_Type()
)
upsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setUnits("percent")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 5)
)
_UpsBypassFrequency_Type = NonNegativeInteger
_UpsBypassFrequency_Object = MibScalar
upsBypassFrequency = _UpsBypassFrequency_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 1),
    _UpsBypassFrequency_Type()
)
upsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequency.setUnits("0.1 Hertz")
_UpsBypassNumLines_Type = NonNegativeInteger
_UpsBypassNumLines_Object = MibScalar
upsBypassNumLines = _UpsBypassNumLines_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 2),
    _UpsBypassNumLines_Type()
)
upsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLines.setStatus("current")
_UpsBypassTable_Object = MibTable
upsBypassTable = _UpsBypassTable_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassTable.setStatus("current")
_UpsBypassEntry_Object = MibTableRow
upsBypassEntry = _UpsBypassEntry_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1)
)
upsBypassEntry.setIndexNames(
    (0, "UPS-MIB", "upsBypassLineIndex"),
)
if mibBuilder.loadTexts:
    upsBypassEntry.setStatus("current")
_UpsBypassLineIndex_Type = PositiveInteger
_UpsBypassLineIndex_Object = MibTableColumn
upsBypassLineIndex = _UpsBypassLineIndex_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 1),
    _UpsBypassLineIndex_Type()
)
upsBypassLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndex.setStatus("current")
_UpsBypassVoltage_Type = NonNegativeInteger
_UpsBypassVoltage_Object = MibTableColumn
upsBypassVoltage = _UpsBypassVoltage_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 2),
    _UpsBypassVoltage_Type()
)
upsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltage.setUnits("RMS Volts")
_UpsBypassCurrent_Type = NonNegativeInteger
_UpsBypassCurrent_Object = MibTableColumn
upsBypassCurrent = _UpsBypassCurrent_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 3),
    _UpsBypassCurrent_Type()
)
upsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrent.setUnits("0.1 RMS Amp")
_UpsBypassPower_Type = NonNegativeInteger
_UpsBypassPower_Object = MibTableColumn
upsBypassPower = _UpsBypassPower_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 5, 3, 1, 4),
    _UpsBypassPower_Type()
)
upsBypassPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPower.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPower.setUnits("Watts")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6)
)
_UpsAlarmsPresent_Type = Gauge32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("current")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("current")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "UPS-MIB", "upsAlarmId"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("current")
_UpsAlarmId_Type = PositiveInteger
_UpsAlarmId_Object = MibTableColumn
upsAlarmId = _UpsAlarmId_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 1),
    _UpsAlarmId_Type()
)
upsAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmId.setStatus("current")
_UpsAlarmDescr_Type = AutonomousType
_UpsAlarmDescr_Object = MibTableColumn
upsAlarmDescr = _UpsAlarmDescr_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 2),
    _UpsAlarmDescr_Type()
)
upsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescr.setStatus("current")
_UpsAlarmTime_Type = TimeStamp
_UpsAlarmTime_Object = MibTableColumn
upsAlarmTime = _UpsAlarmTime_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 2, 1, 3),
    _UpsAlarmTime_Type()
)
upsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTime.setStatus("current")
_UpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
upsWellKnownAlarms = _UpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3)
)
_UpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBad = _UpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBad.setStatus("current")
_UpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
upsAlarmOnBattery = _UpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBattery.setStatus("current")
_UpsAlarmLowBattery_ObjectIdentity = ObjectIdentity
upsAlarmLowBattery = _UpsAlarmLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBattery.setStatus("current")
_UpsAlarmDepletedBattery_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBattery = _UpsAlarmDepletedBattery_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBattery.setStatus("current")
_UpsAlarmTempBad_ObjectIdentity = ObjectIdentity
upsAlarmTempBad = _UpsAlarmTempBad_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBad.setStatus("current")
_UpsAlarmInputBad_ObjectIdentity = ObjectIdentity
upsAlarmInputBad = _UpsAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBad.setStatus("current")
_UpsAlarmOutputBad_ObjectIdentity = ObjectIdentity
upsAlarmOutputBad = _UpsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBad.setStatus("current")
_UpsAlarmOutputOverload_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverload = _UpsAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverload.setStatus("current")
_UpsAlarmOnBypass_ObjectIdentity = ObjectIdentity
upsAlarmOnBypass = _UpsAlarmOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypass.setStatus("current")
_UpsAlarmBypassBad_ObjectIdentity = ObjectIdentity
upsAlarmBypassBad = _UpsAlarmBypassBad_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBad.setStatus("current")
_UpsAlarmOutputOffAsRequested_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequested = _UpsAlarmOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequested.setStatus("current")
_UpsAlarmUpsOffAsRequested_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequested = _UpsAlarmUpsOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequested.setStatus("current")
_UpsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailed = _UpsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailed.setStatus("current")
_UpsAlarmUpsOutputOff_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOff = _UpsAlarmUpsOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOff.setStatus("current")
_UpsAlarmUpsSystemOff_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOff = _UpsAlarmUpsSystemOff_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOff.setStatus("current")
_UpsAlarmFanFailure_ObjectIdentity = ObjectIdentity
upsAlarmFanFailure = _UpsAlarmFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailure.setStatus("current")
_UpsAlarmFuseFailure_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailure = _UpsAlarmFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailure.setStatus("current")
_UpsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFault = _UpsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFault.setStatus("current")
_UpsAlarmDiagnosticTestFailed_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailed = _UpsAlarmDiagnosticTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailed.setStatus("current")
_UpsAlarmCommunicationsLost_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLost = _UpsAlarmCommunicationsLost_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLost.setStatus("current")
_UpsAlarmAwaitingPower_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPower = _UpsAlarmAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPower.setStatus("current")
_UpsAlarmShutdownPending_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPending = _UpsAlarmShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPending.setStatus("current")
_UpsAlarmShutdownImminent_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminent = _UpsAlarmShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminent.setStatus("current")
_UpsAlarmTestInProgress_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgress = _UpsAlarmTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgress.setStatus("current")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 7)
)
_UpsTestId_Type = ObjectIdentifier
_UpsTestId_Object = MibScalar
upsTestId = _UpsTestId_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 1),
    _UpsTestId_Type()
)
upsTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestId.setStatus("current")
_UpsTestSpinLock_Type = TestAndIncr
_UpsTestSpinLock_Object = MibScalar
upsTestSpinLock = _UpsTestSpinLock_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 2),
    _UpsTestSpinLock_Type()
)
upsTestSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLock.setStatus("current")


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
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 3),
    _UpsTestResultsSummary_Type()
)
upsTestResultsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummary.setStatus("current")


class _UpsTestResultsDetail_Type(DisplayString):
    """Custom type upsTestResultsDetail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsTestResultsDetail_Type.__name__ = "DisplayString"
_UpsTestResultsDetail_Object = MibScalar
upsTestResultsDetail = _UpsTestResultsDetail_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 4),
    _UpsTestResultsDetail_Type()
)
upsTestResultsDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetail.setStatus("current")
_UpsTestStartTime_Type = TimeStamp
_UpsTestStartTime_Object = MibScalar
upsTestStartTime = _UpsTestStartTime_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 5),
    _UpsTestStartTime_Type()
)
upsTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTime.setStatus("current")
_UpsTestElapsedTime_Type = TimeInterval
_UpsTestElapsedTime_Object = MibScalar
upsTestElapsedTime = _UpsTestElapsedTime_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 6),
    _UpsTestElapsedTime_Type()
)
upsTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTime.setStatus("current")
_UpsWellKnownTests_ObjectIdentity = ObjectIdentity
upsWellKnownTests = _UpsWellKnownTests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 7)
)
_UpsTestNoTestsInitiated_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiated = _UpsTestNoTestsInitiated_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiated.setStatus("current")
_UpsTestAbortTestInProgress_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgress = _UpsTestAbortTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgress.setStatus("current")
_UpsTestGeneralSystemsTest_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTest = _UpsTestGeneralSystemsTest_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTest.setStatus("current")
_UpsTestQuickBatteryTest_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTest = _UpsTestQuickBatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTest.setStatus("current")
_UpsTestDeepBatteryCalibration_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibration = _UpsTestDeepBatteryCalibration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibration.setStatus("current")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 8)
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
    (1, 3, 6, 1, 2, 1, 33, 1, 8, 1),
    _UpsShutdownType_Type()
)
upsShutdownType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownType.setStatus("current")


class _UpsShutdownAfterDelay_Type(Integer32):
    """Custom type upsShutdownAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483648),
    )


_UpsShutdownAfterDelay_Type.__name__ = "Integer32"
_UpsShutdownAfterDelay_Object = MibScalar
upsShutdownAfterDelay = _UpsShutdownAfterDelay_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 8, 2),
    _UpsShutdownAfterDelay_Type()
)
upsShutdownAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelay.setUnits("seconds")


class _UpsStartupAfterDelay_Type(Integer32):
    """Custom type upsStartupAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483648),
    )


_UpsStartupAfterDelay_Type.__name__ = "Integer32"
_UpsStartupAfterDelay_Object = MibScalar
upsStartupAfterDelay = _UpsStartupAfterDelay_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 8, 3),
    _UpsStartupAfterDelay_Type()
)
upsStartupAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelay.setUnits("seconds")


class _UpsRebootWithDuration_Type(Integer32):
    """Custom type upsRebootWithDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDuration_Type.__name__ = "Integer32"
_UpsRebootWithDuration_Object = MibScalar
upsRebootWithDuration = _UpsRebootWithDuration_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 8, 4),
    _UpsRebootWithDuration_Type()
)
upsRebootWithDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDuration.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDuration.setUnits("seconds")


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
    (1, 3, 6, 1, 2, 1, 33, 1, 8, 5),
    _UpsAutoRestart_Type()
)
upsAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestart.setStatus("current")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 1, 9)
)
_UpsConfigInputVoltage_Type = NonNegativeInteger
_UpsConfigInputVoltage_Object = MibScalar
upsConfigInputVoltage = _UpsConfigInputVoltage_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 1),
    _UpsConfigInputVoltage_Type()
)
upsConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltage.setUnits("RMS Volts")
_UpsConfigInputFreq_Type = NonNegativeInteger
_UpsConfigInputFreq_Object = MibScalar
upsConfigInputFreq = _UpsConfigInputFreq_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 2),
    _UpsConfigInputFreq_Type()
)
upsConfigInputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreq.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreq.setUnits("0.1 Hertz")
_UpsConfigOutputVoltage_Type = NonNegativeInteger
_UpsConfigOutputVoltage_Object = MibScalar
upsConfigOutputVoltage = _UpsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 3),
    _UpsConfigOutputVoltage_Type()
)
upsConfigOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltage.setUnits("RMS Volts")
_UpsConfigOutputFreq_Type = NonNegativeInteger
_UpsConfigOutputFreq_Object = MibScalar
upsConfigOutputFreq = _UpsConfigOutputFreq_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 4),
    _UpsConfigOutputFreq_Type()
)
upsConfigOutputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreq.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreq.setUnits("0.1 Hertz")
_UpsConfigOutputVA_Type = NonNegativeInteger
_UpsConfigOutputVA_Object = MibScalar
upsConfigOutputVA = _UpsConfigOutputVA_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 5),
    _UpsConfigOutputVA_Type()
)
upsConfigOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVA.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVA.setUnits("Volt-Amps")
_UpsConfigOutputPower_Type = NonNegativeInteger
_UpsConfigOutputPower_Object = MibScalar
upsConfigOutputPower = _UpsConfigOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 6),
    _UpsConfigOutputPower_Type()
)
upsConfigOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPower.setUnits("Watts")
_UpsConfigLowBattTime_Type = NonNegativeInteger
_UpsConfigLowBattTime_Object = MibScalar
upsConfigLowBattTime = _UpsConfigLowBattTime_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 7),
    _UpsConfigLowBattTime_Type()
)
upsConfigLowBattTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTime.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTime.setUnits("minutes")


class _UpsConfigAudibleStatus_Type(Integer32):
    """Custom type upsConfigAudibleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("muted", 3))
    )


_UpsConfigAudibleStatus_Type.__name__ = "Integer32"
_UpsConfigAudibleStatus_Object = MibScalar
upsConfigAudibleStatus = _UpsConfigAudibleStatus_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 8),
    _UpsConfigAudibleStatus_Type()
)
upsConfigAudibleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatus.setStatus("current")
_UpsConfigLowVoltageTransferPoint_Type = NonNegativeInteger
_UpsConfigLowVoltageTransferPoint_Object = MibScalar
upsConfigLowVoltageTransferPoint = _UpsConfigLowVoltageTransferPoint_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 9),
    _UpsConfigLowVoltageTransferPoint_Type()
)
upsConfigLowVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPoint.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPoint.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPoint_Type = NonNegativeInteger
_UpsConfigHighVoltageTransferPoint_Object = MibScalar
upsConfigHighVoltageTransferPoint = _UpsConfigHighVoltageTransferPoint_Object(
    (1, 3, 6, 1, 2, 1, 33, 1, 9, 10),
    _UpsConfigHighVoltageTransferPoint_Type()
)
upsConfigHighVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPoint.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPoint.setUnits("RMS Volts")
_UpsTraps_ObjectIdentity = ObjectIdentity
upsTraps = _UpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 2)
)
_UpsConformance_ObjectIdentity = ObjectIdentity
upsConformance = _UpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 3)
)
_UpsCompliances_ObjectIdentity = ObjectIdentity
upsCompliances = _UpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 3, 1)
)
_UpsGroups_ObjectIdentity = ObjectIdentity
upsGroups = _UpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 3, 2)
)
_UpsSubsetGroups_ObjectIdentity = ObjectIdentity
upsSubsetGroups = _UpsSubsetGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1)
)
_UpsBasicGroups_ObjectIdentity = ObjectIdentity
upsBasicGroups = _UpsBasicGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2)
)
_UpsFullGroups_ObjectIdentity = ObjectIdentity
upsFullGroups = _UpsFullGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3)
)

# Managed Objects groups

upsSubsetIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 1)
)
upsSubsetIdentGroup.setObjects(
      *(("UPS-MIB", "upsIdentManufacturer"),
        ("UPS-MIB", "upsIdentModel"),
        ("UPS-MIB", "upsIdentAgentSoftwareVersion"),
        ("UPS-MIB", "upsIdentName"),
        ("UPS-MIB", "upsIdentAttachedDevices"))
)
if mibBuilder.loadTexts:
    upsSubsetIdentGroup.setStatus("current")

upsSubsetBatteryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 2)
)
upsSubsetBatteryGroup.setObjects(
      *(("UPS-MIB", "upsBatteryStatus"),
        ("UPS-MIB", "upsSecondsOnBattery"))
)
if mibBuilder.loadTexts:
    upsSubsetBatteryGroup.setStatus("current")

upsSubsetInputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 3)
)
upsSubsetInputGroup.setObjects(
    ("UPS-MIB", "upsInputLineBads")
)
if mibBuilder.loadTexts:
    upsSubsetInputGroup.setStatus("current")

upsSubsetOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 4)
)
upsSubsetOutputGroup.setObjects(
    ("UPS-MIB", "upsOutputSource")
)
if mibBuilder.loadTexts:
    upsSubsetOutputGroup.setStatus("current")

upsSubsetAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 6)
)
upsSubsetAlarmGroup.setObjects(
      *(("UPS-MIB", "upsAlarmsPresent"),
        ("UPS-MIB", "upsAlarmDescr"),
        ("UPS-MIB", "upsAlarmTime"))
)
if mibBuilder.loadTexts:
    upsSubsetAlarmGroup.setStatus("current")

upsSubsetControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 8)
)
upsSubsetControlGroup.setObjects(
      *(("UPS-MIB", "upsShutdownType"),
        ("UPS-MIB", "upsShutdownAfterDelay"),
        ("UPS-MIB", "upsAutoRestart"))
)
if mibBuilder.loadTexts:
    upsSubsetControlGroup.setStatus("current")

upsSubsetConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 1, 9)
)
upsSubsetConfigGroup.setObjects(
      *(("UPS-MIB", "upsConfigInputVoltage"),
        ("UPS-MIB", "upsConfigInputFreq"),
        ("UPS-MIB", "upsConfigOutputVoltage"),
        ("UPS-MIB", "upsConfigOutputFreq"),
        ("UPS-MIB", "upsConfigOutputVA"),
        ("UPS-MIB", "upsConfigOutputPower"))
)
if mibBuilder.loadTexts:
    upsSubsetConfigGroup.setStatus("current")

upsBasicIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 1)
)
upsBasicIdentGroup.setObjects(
      *(("UPS-MIB", "upsIdentManufacturer"),
        ("UPS-MIB", "upsIdentModel"),
        ("UPS-MIB", "upsIdentUPSSoftwareVersion"),
        ("UPS-MIB", "upsIdentAgentSoftwareVersion"),
        ("UPS-MIB", "upsIdentName"))
)
if mibBuilder.loadTexts:
    upsBasicIdentGroup.setStatus("current")

upsBasicBatteryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 2)
)
upsBasicBatteryGroup.setObjects(
      *(("UPS-MIB", "upsBatteryStatus"),
        ("UPS-MIB", "upsSecondsOnBattery"))
)
if mibBuilder.loadTexts:
    upsBasicBatteryGroup.setStatus("current")

upsBasicInputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 3)
)
upsBasicInputGroup.setObjects(
      *(("UPS-MIB", "upsInputLineBads"),
        ("UPS-MIB", "upsInputNumLines"),
        ("UPS-MIB", "upsInputFrequency"),
        ("UPS-MIB", "upsInputVoltage"))
)
if mibBuilder.loadTexts:
    upsBasicInputGroup.setStatus("current")

upsBasicOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 4)
)
upsBasicOutputGroup.setObjects(
      *(("UPS-MIB", "upsOutputSource"),
        ("UPS-MIB", "upsOutputFrequency"),
        ("UPS-MIB", "upsOutputNumLines"),
        ("UPS-MIB", "upsOutputVoltage"))
)
if mibBuilder.loadTexts:
    upsBasicOutputGroup.setStatus("current")

upsBasicBypassGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 5)
)
upsBasicBypassGroup.setObjects(
      *(("UPS-MIB", "upsBypassFrequency"),
        ("UPS-MIB", "upsBypassNumLines"),
        ("UPS-MIB", "upsBypassVoltage"))
)
if mibBuilder.loadTexts:
    upsBasicBypassGroup.setStatus("current")

upsBasicAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 6)
)
upsBasicAlarmGroup.setObjects(
      *(("UPS-MIB", "upsAlarmsPresent"),
        ("UPS-MIB", "upsAlarmDescr"),
        ("UPS-MIB", "upsAlarmTime"))
)
if mibBuilder.loadTexts:
    upsBasicAlarmGroup.setStatus("current")

upsBasicTestGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 7)
)
upsBasicTestGroup.setObjects(
      *(("UPS-MIB", "upsTestId"),
        ("UPS-MIB", "upsTestSpinLock"),
        ("UPS-MIB", "upsTestResultsSummary"),
        ("UPS-MIB", "upsTestResultsDetail"),
        ("UPS-MIB", "upsTestStartTime"),
        ("UPS-MIB", "upsTestElapsedTime"))
)
if mibBuilder.loadTexts:
    upsBasicTestGroup.setStatus("current")

upsBasicControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 8)
)
upsBasicControlGroup.setObjects(
      *(("UPS-MIB", "upsShutdownType"),
        ("UPS-MIB", "upsShutdownAfterDelay"),
        ("UPS-MIB", "upsStartupAfterDelay"),
        ("UPS-MIB", "upsRebootWithDuration"),
        ("UPS-MIB", "upsAutoRestart"))
)
if mibBuilder.loadTexts:
    upsBasicControlGroup.setStatus("current")

upsBasicConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 2, 9)
)
upsBasicConfigGroup.setObjects(
      *(("UPS-MIB", "upsConfigInputVoltage"),
        ("UPS-MIB", "upsConfigInputFreq"),
        ("UPS-MIB", "upsConfigOutputVoltage"),
        ("UPS-MIB", "upsConfigOutputFreq"),
        ("UPS-MIB", "upsConfigOutputVA"),
        ("UPS-MIB", "upsConfigOutputPower"),
        ("UPS-MIB", "upsConfigLowBattTime"),
        ("UPS-MIB", "upsConfigAudibleStatus"))
)
if mibBuilder.loadTexts:
    upsBasicConfigGroup.setStatus("current")

upsFullIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 1)
)
upsFullIdentGroup.setObjects(
      *(("UPS-MIB", "upsIdentManufacturer"),
        ("UPS-MIB", "upsIdentModel"),
        ("UPS-MIB", "upsIdentUPSSoftwareVersion"),
        ("UPS-MIB", "upsIdentAgentSoftwareVersion"),
        ("UPS-MIB", "upsIdentName"),
        ("UPS-MIB", "upsIdentAttachedDevices"))
)
if mibBuilder.loadTexts:
    upsFullIdentGroup.setStatus("current")

upsFullBatteryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 2)
)
upsFullBatteryGroup.setObjects(
      *(("UPS-MIB", "upsBatteryStatus"),
        ("UPS-MIB", "upsSecondsOnBattery"),
        ("UPS-MIB", "upsEstimatedMinutesRemaining"),
        ("UPS-MIB", "upsEstimatedChargeRemaining"))
)
if mibBuilder.loadTexts:
    upsFullBatteryGroup.setStatus("current")

upsFullInputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 3)
)
upsFullInputGroup.setObjects(
      *(("UPS-MIB", "upsInputLineBads"),
        ("UPS-MIB", "upsInputNumLines"),
        ("UPS-MIB", "upsInputFrequency"),
        ("UPS-MIB", "upsInputVoltage"))
)
if mibBuilder.loadTexts:
    upsFullInputGroup.setStatus("current")

upsFullOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 4)
)
upsFullOutputGroup.setObjects(
      *(("UPS-MIB", "upsOutputSource"),
        ("UPS-MIB", "upsOutputFrequency"),
        ("UPS-MIB", "upsOutputNumLines"),
        ("UPS-MIB", "upsOutputVoltage"),
        ("UPS-MIB", "upsOutputCurrent"),
        ("UPS-MIB", "upsOutputPower"),
        ("UPS-MIB", "upsOutputPercentLoad"))
)
if mibBuilder.loadTexts:
    upsFullOutputGroup.setStatus("current")

upsFullBypassGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 5)
)
upsFullBypassGroup.setObjects(
      *(("UPS-MIB", "upsBypassFrequency"),
        ("UPS-MIB", "upsBypassNumLines"),
        ("UPS-MIB", "upsBypassVoltage"))
)
if mibBuilder.loadTexts:
    upsFullBypassGroup.setStatus("current")

upsFullAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 6)
)
upsFullAlarmGroup.setObjects(
      *(("UPS-MIB", "upsAlarmsPresent"),
        ("UPS-MIB", "upsAlarmDescr"),
        ("UPS-MIB", "upsAlarmTime"))
)
if mibBuilder.loadTexts:
    upsFullAlarmGroup.setStatus("current")

upsFullTestGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 7)
)
upsFullTestGroup.setObjects(
      *(("UPS-MIB", "upsTestId"),
        ("UPS-MIB", "upsTestSpinLock"),
        ("UPS-MIB", "upsTestResultsSummary"),
        ("UPS-MIB", "upsTestResultsDetail"),
        ("UPS-MIB", "upsTestStartTime"),
        ("UPS-MIB", "upsTestElapsedTime"))
)
if mibBuilder.loadTexts:
    upsFullTestGroup.setStatus("current")

upsFullControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 8)
)
upsFullControlGroup.setObjects(
      *(("UPS-MIB", "upsShutdownType"),
        ("UPS-MIB", "upsShutdownAfterDelay"),
        ("UPS-MIB", "upsStartupAfterDelay"),
        ("UPS-MIB", "upsRebootWithDuration"),
        ("UPS-MIB", "upsAutoRestart"))
)
if mibBuilder.loadTexts:
    upsFullControlGroup.setStatus("current")

upsFullConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 33, 3, 2, 3, 9)
)
upsFullConfigGroup.setObjects(
      *(("UPS-MIB", "upsConfigInputVoltage"),
        ("UPS-MIB", "upsConfigInputFreq"),
        ("UPS-MIB", "upsConfigOutputVoltage"),
        ("UPS-MIB", "upsConfigOutputFreq"),
        ("UPS-MIB", "upsConfigOutputVA"),
        ("UPS-MIB", "upsConfigOutputPower"),
        ("UPS-MIB", "upsConfigLowBattTime"),
        ("UPS-MIB", "upsConfigAudibleStatus"))
)
if mibBuilder.loadTexts:
    upsFullConfigGroup.setStatus("current")


# Notification objects

upsTrapOnBattery = NotificationType(
    (1, 3, 6, 1, 2, 1, 33, 2, 1)
)
upsTrapOnBattery.setObjects(
      *(("UPS-MIB", "upsEstimatedMinutesRemaining"),
        ("UPS-MIB", "upsSecondsOnBattery"),
        ("UPS-MIB", "upsConfigLowBattTime"))
)
if mibBuilder.loadTexts:
    upsTrapOnBattery.setStatus(
        "current"
    )

upsTrapTestCompleted = NotificationType(
    (1, 3, 6, 1, 2, 1, 33, 2, 2)
)
upsTrapTestCompleted.setObjects(
      *(("UPS-MIB", "upsTestId"),
        ("UPS-MIB", "upsTestSpinLock"),
        ("UPS-MIB", "upsTestResultsSummary"),
        ("UPS-MIB", "upsTestResultsDetail"),
        ("UPS-MIB", "upsTestStartTime"),
        ("UPS-MIB", "upsTestElapsedTime"))
)
if mibBuilder.loadTexts:
    upsTrapTestCompleted.setStatus(
        "current"
    )

upsTrapAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 2, 1, 33, 2, 3)
)
upsTrapAlarmEntryAdded.setObjects(
      *(("UPS-MIB", "upsAlarmId"),
        ("UPS-MIB", "upsAlarmDescr"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmEntryAdded.setStatus(
        "current"
    )

upsTrapAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 2, 1, 33, 2, 4)
)
upsTrapAlarmEntryRemoved.setObjects(
      *(("UPS-MIB", "upsAlarmId"),
        ("UPS-MIB", "upsAlarmDescr"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmEntryRemoved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

upsSubsetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 33, 3, 1, 1)
)
if mibBuilder.loadTexts:
    upsSubsetCompliance.setStatus(
        "current"
    )

upsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 33, 3, 1, 2)
)
if mibBuilder.loadTexts:
    upsBasicCompliance.setStatus(
        "current"
    )

upsFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 33, 3, 1, 3)
)
if mibBuilder.loadTexts:
    upsFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UPS-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "upsMIB": upsMIB,
       "upsObjects": upsObjects,
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
       "upsEstimatedChargeRemaining": upsEstimatedChargeRemaining,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryCurrent": upsBatteryCurrent,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsInput": upsInput,
       "upsInputLineBads": upsInputLineBads,
       "upsInputNumLines": upsInputNumLines,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputLineIndex": upsInputLineIndex,
       "upsInputFrequency": upsInputFrequency,
       "upsInputVoltage": upsInputVoltage,
       "upsInputCurrent": upsInputCurrent,
       "upsInputTruePower": upsInputTruePower,
       "upsOutput": upsOutput,
       "upsOutputSource": upsOutputSource,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputNumLines": upsOutputNumLines,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputLineIndex": upsOutputLineIndex,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputPower": upsOutputPower,
       "upsOutputPercentLoad": upsOutputPercentLoad,
       "upsBypass": upsBypass,
       "upsBypassFrequency": upsBypassFrequency,
       "upsBypassNumLines": upsBypassNumLines,
       "upsBypassTable": upsBypassTable,
       "upsBypassEntry": upsBypassEntry,
       "upsBypassLineIndex": upsBypassLineIndex,
       "upsBypassVoltage": upsBypassVoltage,
       "upsBypassCurrent": upsBypassCurrent,
       "upsBypassPower": upsBypassPower,
       "upsAlarm": upsAlarm,
       "upsAlarmsPresent": upsAlarmsPresent,
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
       "upsAlarmCommunicationsLost": upsAlarmCommunicationsLost,
       "upsAlarmAwaitingPower": upsAlarmAwaitingPower,
       "upsAlarmShutdownPending": upsAlarmShutdownPending,
       "upsAlarmShutdownImminent": upsAlarmShutdownImminent,
       "upsAlarmTestInProgress": upsAlarmTestInProgress,
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
       "upsTestDeepBatteryCalibration": upsTestDeepBatteryCalibration,
       "upsControl": upsControl,
       "upsShutdownType": upsShutdownType,
       "upsShutdownAfterDelay": upsShutdownAfterDelay,
       "upsStartupAfterDelay": upsStartupAfterDelay,
       "upsRebootWithDuration": upsRebootWithDuration,
       "upsAutoRestart": upsAutoRestart,
       "upsConfig": upsConfig,
       "upsConfigInputVoltage": upsConfigInputVoltage,
       "upsConfigInputFreq": upsConfigInputFreq,
       "upsConfigOutputVoltage": upsConfigOutputVoltage,
       "upsConfigOutputFreq": upsConfigOutputFreq,
       "upsConfigOutputVA": upsConfigOutputVA,
       "upsConfigOutputPower": upsConfigOutputPower,
       "upsConfigLowBattTime": upsConfigLowBattTime,
       "upsConfigAudibleStatus": upsConfigAudibleStatus,
       "upsConfigLowVoltageTransferPoint": upsConfigLowVoltageTransferPoint,
       "upsConfigHighVoltageTransferPoint": upsConfigHighVoltageTransferPoint,
       "upsTraps": upsTraps,
       "upsTrapOnBattery": upsTrapOnBattery,
       "upsTrapTestCompleted": upsTrapTestCompleted,
       "upsTrapAlarmEntryAdded": upsTrapAlarmEntryAdded,
       "upsTrapAlarmEntryRemoved": upsTrapAlarmEntryRemoved,
       "upsConformance": upsConformance,
       "upsCompliances": upsCompliances,
       "upsSubsetCompliance": upsSubsetCompliance,
       "upsBasicCompliance": upsBasicCompliance,
       "upsFullCompliance": upsFullCompliance,
       "upsGroups": upsGroups,
       "upsSubsetGroups": upsSubsetGroups,
       "upsSubsetIdentGroup": upsSubsetIdentGroup,
       "upsSubsetBatteryGroup": upsSubsetBatteryGroup,
       "upsSubsetInputGroup": upsSubsetInputGroup,
       "upsSubsetOutputGroup": upsSubsetOutputGroup,
       "upsSubsetAlarmGroup": upsSubsetAlarmGroup,
       "upsSubsetControlGroup": upsSubsetControlGroup,
       "upsSubsetConfigGroup": upsSubsetConfigGroup,
       "upsBasicGroups": upsBasicGroups,
       "upsBasicIdentGroup": upsBasicIdentGroup,
       "upsBasicBatteryGroup": upsBasicBatteryGroup,
       "upsBasicInputGroup": upsBasicInputGroup,
       "upsBasicOutputGroup": upsBasicOutputGroup,
       "upsBasicBypassGroup": upsBasicBypassGroup,
       "upsBasicAlarmGroup": upsBasicAlarmGroup,
       "upsBasicTestGroup": upsBasicTestGroup,
       "upsBasicControlGroup": upsBasicControlGroup,
       "upsBasicConfigGroup": upsBasicConfigGroup,
       "upsFullGroups": upsFullGroups,
       "upsFullIdentGroup": upsFullIdentGroup,
       "upsFullBatteryGroup": upsFullBatteryGroup,
       "upsFullInputGroup": upsFullInputGroup,
       "upsFullOutputGroup": upsFullOutputGroup,
       "upsFullBypassGroup": upsFullBypassGroup,
       "upsFullAlarmGroup": upsFullAlarmGroup,
       "upsFullTestGroup": upsFullTestGroup,
       "upsFullControlGroup": upsFullControlGroup,
       "upsFullConfigGroup": upsFullConfigGroup}
)
