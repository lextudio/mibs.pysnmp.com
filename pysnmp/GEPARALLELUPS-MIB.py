# SNMP MIB module (GEPARALLELUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GEPARALLELUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:34 2024
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

imv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 818)
)
imv.setRevisions(
        ("2010-07-05 00:00",
         "2008-01-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_GeHardware_ObjectIdentity = ObjectIdentity
geHardware = _GeHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1)
)
_GeUPS_ObjectIdentity = ObjectIdentity
geUPS = _GeUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1)
)
_GeDiscoveredUPSsMask_Type = Integer32
_GeDiscoveredUPSsMask_Object = MibScalar
geDiscoveredUPSsMask = _GeDiscoveredUPSsMask_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 1),
    _GeDiscoveredUPSsMask_Type()
)
geDiscoveredUPSsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDiscoveredUPSsMask.setStatus("current")
_GeRequestPacket_Type = DisplayString
_GeRequestPacket_Object = MibScalar
geRequestPacket = _GeRequestPacket_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 2),
    _GeRequestPacket_Type()
)
geRequestPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geRequestPacket.setStatus("current")
_GeReplyPacket_Type = DisplayString
_GeReplyPacket_Object = MibScalar
geReplyPacket = _GeReplyPacket_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 3),
    _GeReplyPacket_Type()
)
geReplyPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geReplyPacket.setStatus("current")
_GeGenericUPS_ObjectIdentity = ObjectIdentity
geGenericUPS = _GeGenericUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1)
)
_UpsIdentManufacturer_Type = DisplayString
_UpsIdentManufacturer_Object = MibScalar
upsIdentManufacturer = _UpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 1),
    _UpsIdentManufacturer_Type()
)
upsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturer.setStatus("current")
_UpsIdentModel_Type = DisplayString
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 2),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("current")
_UpsIdentUPSSoftwareVersion_Type = DisplayString
_UpsIdentUPSSoftwareVersion_Object = MibScalar
upsIdentUPSSoftwareVersion = _UpsIdentUPSSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 3),
    _UpsIdentUPSSoftwareVersion_Type()
)
upsIdentUPSSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersion.setStatus("current")
_UpsIdentAgentSoftwareVersion_Type = DisplayString
_UpsIdentAgentSoftwareVersion_Object = MibScalar
upsIdentAgentSoftwareVersion = _UpsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 4),
    _UpsIdentAgentSoftwareVersion_Type()
)
upsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersion.setStatus("current")
_UpsIdentName_Type = DisplayString
_UpsIdentName_Object = MibScalar
upsIdentName = _UpsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 5),
    _UpsIdentName_Type()
)
upsIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentName.setStatus("current")
_UpsIdentAttachedDevices_Type = DisplayString
_UpsIdentAttachedDevices_Object = MibScalar
upsIdentAttachedDevices = _UpsIdentAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 6),
    _UpsIdentAttachedDevices_Type()
)
upsIdentAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevices.setStatus("current")
_UpsIdentUPSSerialNumber_Type = DisplayString
_UpsIdentUPSSerialNumber_Object = MibScalar
upsIdentUPSSerialNumber = _UpsIdentUPSSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 7),
    _UpsIdentUPSSerialNumber_Type()
)
upsIdentUPSSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumber.setStatus("current")
_UpsIdentComProtVersion_Type = DisplayString
_UpsIdentComProtVersion_Object = MibScalar
upsIdentComProtVersion = _UpsIdentComProtVersion_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 8),
    _UpsIdentComProtVersion_Type()
)
upsIdentComProtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersion.setStatus("current")
_UpsIdentOperatingTime_Type = NonNegativeInteger32
_UpsIdentOperatingTime_Object = MibScalar
upsIdentOperatingTime = _UpsIdentOperatingTime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 9),
    _UpsIdentOperatingTime_Type()
)
upsIdentOperatingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTime.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTime.setUnits("seconds")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2)
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("current")
_UpsSecondsOnBattery_Type = Integer32
_UpsSecondsOnBattery_Object = MibScalar
upsSecondsOnBattery = _UpsSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 2),
    _UpsSecondsOnBattery_Type()
)
upsSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBattery.setUnits("seconds")
_UpsEstimatedMinutesRemaining_Type = PositiveInteger32
_UpsEstimatedMinutesRemaining_Object = MibScalar
upsEstimatedMinutesRemaining = _UpsEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 4),
    _UpsEstimatedChargeRemaining_Type()
)
upsEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaining.setUnits("percent")
_UpsBatteryVoltage_Type = NonNegativeInteger32
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 7),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setUnits("degrees Centigrade")
_UpsBatteryRipple_Type = Integer32
_UpsBatteryRipple_Object = MibScalar
upsBatteryRipple = _UpsBatteryRipple_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 8),
    _UpsBatteryRipple_Type()
)
upsBatteryRipple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipple.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipple.setUnits("0.1 Volt RMS")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3)
)
_UpsInputLineBads_Type = Counter32
_UpsInputLineBads_Object = MibScalar
upsInputLineBads = _UpsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 1),
    _UpsInputLineBads_Type()
)
upsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBads.setStatus("current")
_UpsInputNumLines_Type = NonNegativeInteger32
_UpsInputNumLines_Object = MibScalar
upsInputNumLines = _UpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 2),
    _UpsInputNumLines_Type()
)
upsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLines.setStatus("current")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("current")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1)
)
upsInputEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndex"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("current")
_UpsInputLineIndex_Type = PositiveInteger32
_UpsInputLineIndex_Object = MibTableColumn
upsInputLineIndex = _UpsInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 1),
    _UpsInputLineIndex_Type()
)
upsInputLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndex.setStatus("current")
_UpsInputFrequency_Type = NonNegativeInteger32
_UpsInputFrequency_Object = MibTableColumn
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 2),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequency.setUnits("0.1 Hertz")
_UpsInputVoltage_Type = NonNegativeInteger32
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 3),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltage.setUnits("RMS Volts")
_UpsInputCurrent_Type = NonNegativeInteger32
_UpsInputCurrent_Object = MibTableColumn
upsInputCurrent = _UpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 4),
    _UpsInputCurrent_Type()
)
upsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrent.setUnits("0.1 RMS Amp")
_UpsInputTruePower_Type = NonNegativeInteger32
_UpsInputTruePower_Object = MibTableColumn
upsInputTruePower = _UpsInputTruePower_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 5),
    _UpsInputTruePower_Type()
)
upsInputTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePower.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePower.setUnits("Watts")
_UpsInputVoltageMin_Type = NonNegativeInteger32
_UpsInputVoltageMin_Object = MibTableColumn
upsInputVoltageMin = _UpsInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 6),
    _UpsInputVoltageMin_Type()
)
upsInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMin.setUnits("RMS Volts")
_UpsInputVoltageMax_Type = NonNegativeInteger32
_UpsInputVoltageMax_Object = MibTableColumn
upsInputVoltageMax = _UpsInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 7),
    _UpsInputVoltageMax_Type()
)
upsInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMax.setUnits("RMS Volts")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4)
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 1),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("current")
_UpsOutputFrequency_Type = NonNegativeInteger32
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequency.setUnits("0.1 Hertz")
_UpsOutputNumLines_Type = NonNegativeInteger32
_UpsOutputNumLines_Object = MibScalar
upsOutputNumLines = _UpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 3),
    _UpsOutputNumLines_Type()
)
upsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLines.setStatus("current")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("current")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1)
)
upsOutputEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("current")
_UpsOutputLineIndex_Type = PositiveInteger32
_UpsOutputLineIndex_Object = MibTableColumn
upsOutputLineIndex = _UpsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 1),
    _UpsOutputLineIndex_Type()
)
upsOutputLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndex.setStatus("current")
_UpsOutputVoltage_Type = NonNegativeInteger32
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltage.setUnits("RMS Volts")
_UpsOutputCurrent_Type = NonNegativeInteger32
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrent.setUnits("0.1 RMS Amp")
_UpsOutputPower_Type = NonNegativeInteger32
_UpsOutputPower_Object = MibTableColumn
upsOutputPower = _UpsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 5),
    _UpsOutputPercentLoad_Type()
)
upsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setUnits("percent")


class _UpsOutputPowerFactor_Type(Integer32):
    """Custom type upsOutputPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactor_Type.__name__ = "Integer32"
_UpsOutputPowerFactor_Object = MibTableColumn
upsOutputPowerFactor = _UpsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 6),
    _UpsOutputPowerFactor_Type()
)
upsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactor.setUnits("0.01 cos phi")
_UpsOutputPeakCurrent_Type = Integer32
_UpsOutputPeakCurrent_Object = MibTableColumn
upsOutputPeakCurrent = _UpsOutputPeakCurrent_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 7),
    _UpsOutputPeakCurrent_Type()
)
upsOutputPeakCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrent.setUnits("Amps")
_UpsOutputShareCurrent_Type = Integer32
_UpsOutputShareCurrent_Object = MibTableColumn
upsOutputShareCurrent = _UpsOutputShareCurrent_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 8),
    _UpsOutputShareCurrent_Type()
)
upsOutputShareCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrent.setUnits("Amps")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5)
)
_UpsBypassFrequency_Type = NonNegativeInteger32
_UpsBypassFrequency_Object = MibScalar
upsBypassFrequency = _UpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 1),
    _UpsBypassFrequency_Type()
)
upsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequency.setUnits("0.1 Hertz")
_UpsBypassNumLines_Type = NonNegativeInteger32
_UpsBypassNumLines_Object = MibScalar
upsBypassNumLines = _UpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 2),
    _UpsBypassNumLines_Type()
)
upsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLines.setStatus("current")
_UpsBypassTable_Object = MibTable
upsBypassTable = _UpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassTable.setStatus("current")
_UpsBypassEntry_Object = MibTableRow
upsBypassEntry = _UpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1)
)
upsBypassEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndex"),
)
if mibBuilder.loadTexts:
    upsBypassEntry.setStatus("current")
_UpsBypassLineIndex_Type = PositiveInteger32
_UpsBypassLineIndex_Object = MibTableColumn
upsBypassLineIndex = _UpsBypassLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 1),
    _UpsBypassLineIndex_Type()
)
upsBypassLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndex.setStatus("current")
_UpsBypassVoltage_Type = NonNegativeInteger32
_UpsBypassVoltage_Object = MibTableColumn
upsBypassVoltage = _UpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 2),
    _UpsBypassVoltage_Type()
)
upsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltage.setUnits("RMS Volts")
_UpsBypassCurrent_Type = NonNegativeInteger32
_UpsBypassCurrent_Object = MibTableColumn
upsBypassCurrent = _UpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 3),
    _UpsBypassCurrent_Type()
)
upsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrent.setUnits("0.1 RMS Amp")
_UpsBypassPower_Type = NonNegativeInteger32
_UpsBypassPower_Object = MibTableColumn
upsBypassPower = _UpsBypassPower_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 4),
    _UpsBypassPower_Type()
)
upsBypassPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPower.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPower.setUnits("Watts")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6)
)
_UpsAlarmsPresent_Type = Gauge32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("current")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("current")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmId"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("current")
_UpsAlarmId_Type = PositiveInteger32
_UpsAlarmId_Object = MibTableColumn
upsAlarmId = _UpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1, 1),
    _UpsAlarmId_Type()
)
upsAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmId.setStatus("current")
_UpsAlarmDescr_Type = AutonomousType
_UpsAlarmDescr_Object = MibTableColumn
upsAlarmDescr = _UpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1, 2),
    _UpsAlarmDescr_Type()
)
upsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescr.setStatus("current")
_UpsAlarmTime_Type = TimeStamp
_UpsAlarmTime_Object = MibTableColumn
upsAlarmTime = _UpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1, 3),
    _UpsAlarmTime_Type()
)
upsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTime.setStatus("current")
_UpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
upsWellKnownAlarms = _UpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3)
)
_UpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBad = _UpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBad.setStatus("current")
_UpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
upsAlarmOnBattery = _UpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBattery.setStatus("current")
_UpsAlarmLowBattery_ObjectIdentity = ObjectIdentity
upsAlarmLowBattery = _UpsAlarmLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBattery.setStatus("current")
_UpsAlarmDepletedBattery_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBattery = _UpsAlarmDepletedBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBattery.setStatus("current")
_UpsAlarmTempBad_ObjectIdentity = ObjectIdentity
upsAlarmTempBad = _UpsAlarmTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBad.setStatus("current")
_UpsAlarmInputBad_ObjectIdentity = ObjectIdentity
upsAlarmInputBad = _UpsAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBad.setStatus("current")
_UpsAlarmOutputBad_ObjectIdentity = ObjectIdentity
upsAlarmOutputBad = _UpsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBad.setStatus("current")
_UpsAlarmOutputOverload_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverload = _UpsAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverload.setStatus("current")
_UpsAlarmOnBypass_ObjectIdentity = ObjectIdentity
upsAlarmOnBypass = _UpsAlarmOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypass.setStatus("current")
_UpsAlarmBypassBad_ObjectIdentity = ObjectIdentity
upsAlarmBypassBad = _UpsAlarmBypassBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBad.setStatus("current")
_UpsAlarmOutputOffAsRequested_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequested = _UpsAlarmOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequested.setStatus("current")
_UpsAlarmUpsOffAsRequested_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequested = _UpsAlarmUpsOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequested.setStatus("current")
_UpsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailed = _UpsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailed.setStatus("current")
_UpsAlarmUpsOutputOff_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOff = _UpsAlarmUpsOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOff.setStatus("current")
_UpsAlarmUpsSystemOff_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOff = _UpsAlarmUpsSystemOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOff.setStatus("current")
_UpsAlarmFanFailure_ObjectIdentity = ObjectIdentity
upsAlarmFanFailure = _UpsAlarmFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailure.setStatus("current")
_UpsAlarmFuseFailure_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailure = _UpsAlarmFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailure.setStatus("current")
_UpsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFault = _UpsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFault.setStatus("current")
_UpsAlarmDiagnosticTestFailed_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailed = _UpsAlarmDiagnosticTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailed.setStatus("current")
_UpsAlarmCommunicationsLost_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLost = _UpsAlarmCommunicationsLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLost.setStatus("current")
_UpsAlarmAwaitingPower_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPower = _UpsAlarmAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPower.setStatus("current")
_UpsAlarmShutdownPending_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPending = _UpsAlarmShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPending.setStatus("current")
_UpsAlarmShutdownImminent_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminent = _UpsAlarmShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminent.setStatus("current")
_UpsAlarmTestInProgress_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgress = _UpsAlarmTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgress.setStatus("current")
_UpsAlarmReceptacleOff_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOff = _UpsAlarmReceptacleOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOff.setStatus("current")
_UpsAlarmHighSpeedBusFailure_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailure = _UpsAlarmHighSpeedBusFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailure.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailure_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailure = _UpsAlarmHighSpeedBusJACRCFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailure.setStatus("current")
_UpsAlarmConnectivityBusFailure_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailure = _UpsAlarmConnectivityBusFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailure.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailure_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailure = _UpsAlarmHighSpeedBusJBCRCFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailure.setStatus("current")
_UpsAlarmCurrentSharing_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharing = _UpsAlarmCurrentSharing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharing.setStatus("current")
_UpsAlarmDCRipple_ObjectIdentity = ObjectIdentity
upsAlarmDCRipple = _UpsAlarmDCRipple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipple.setStatus("current")
_UpsAlarmMaskA_Type = Unsigned32
_UpsAlarmMaskA_Object = MibScalar
upsAlarmMaskA = _UpsAlarmMaskA_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 4),
    _UpsAlarmMaskA_Type()
)
upsAlarmMaskA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskA.setStatus("current")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7)
)
_UpsTestId_Type = ObjectIdentifier
_UpsTestId_Object = MibScalar
upsTestId = _UpsTestId_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 1),
    _UpsTestId_Type()
)
upsTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestId.setStatus("current")
_UpsTestSpinLock_Type = TestAndIncr
_UpsTestSpinLock_Object = MibScalar
upsTestSpinLock = _UpsTestSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 3),
    _UpsTestResultsSummary_Type()
)
upsTestResultsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummary.setStatus("current")
_UpsTestResultsDetail_Type = DisplayString
_UpsTestResultsDetail_Object = MibScalar
upsTestResultsDetail = _UpsTestResultsDetail_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 4),
    _UpsTestResultsDetail_Type()
)
upsTestResultsDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetail.setStatus("current")
_UpsTestStartTime_Type = TimeStamp
_UpsTestStartTime_Object = MibScalar
upsTestStartTime = _UpsTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 5),
    _UpsTestStartTime_Type()
)
upsTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTime.setStatus("current")
_UpsTestElapsedTime_Type = TimeInterval
_UpsTestElapsedTime_Object = MibScalar
upsTestElapsedTime = _UpsTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 6),
    _UpsTestElapsedTime_Type()
)
upsTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTime.setStatus("current")
_UpsWellKnownTests_ObjectIdentity = ObjectIdentity
upsWellKnownTests = _UpsWellKnownTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7)
)
_UpsTestNoTestsInitiated_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiated = _UpsTestNoTestsInitiated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiated.setStatus("current")
_UpsTestAbortTestInProgress_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgress = _UpsTestAbortTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgress.setStatus("current")
_UpsTestGeneralSystemsTest_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTest = _UpsTestGeneralSystemsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTest.setStatus("current")
_UpsTestQuickBatteryTest_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTest = _UpsTestQuickBatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTest.setStatus("current")
_UpsTestDeepBatteryCalibration_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibration = _UpsTestDeepBatteryCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibration.setStatus("current")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8)
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 1),
    _UpsShutdownType_Type()
)
upsShutdownType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownType.setStatus("current")


class _UpsShutdownAfterDelay_Type(Integer32):
    """Custom type upsShutdownAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelay_Type.__name__ = "Integer32"
_UpsShutdownAfterDelay_Object = MibScalar
upsShutdownAfterDelay = _UpsShutdownAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 2),
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
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelay_Type.__name__ = "Integer32"
_UpsStartupAfterDelay_Object = MibScalar
upsStartupAfterDelay = _UpsStartupAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 3),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 5),
    _UpsAutoRestart_Type()
)
upsAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestart.setStatus("current")
_UpsReceptaclesNum_Type = NonNegativeInteger32
_UpsReceptaclesNum_Object = MibScalar
upsReceptaclesNum = _UpsReceptaclesNum_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 6),
    _UpsReceptaclesNum_Type()
)
upsReceptaclesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNum.setStatus("current")
_UpsReceptacleTable_Object = MibTable
upsReceptacleTable = _UpsReceptacleTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleTable.setStatus("current")
_UpsReceptacleEntry_Object = MibTableRow
upsReceptacleEntry = _UpsReceptacleEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7, 1)
)
upsReceptacleEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndex"),
)
if mibBuilder.loadTexts:
    upsReceptacleEntry.setStatus("current")
_UpsReceptacleLineIndex_Type = PositiveInteger32
_UpsReceptacleLineIndex_Object = MibTableColumn
upsReceptacleLineIndex = _UpsReceptacleLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7, 1, 1),
    _UpsReceptacleLineIndex_Type()
)
upsReceptacleLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndex.setStatus("current")


class _UpsReceptacleOnOff_Type(Integer32):
    """Custom type upsReceptacleOnOff based on Integer32"""
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


_UpsReceptacleOnOff_Type.__name__ = "Integer32"
_UpsReceptacleOnOff_Object = MibTableColumn
upsReceptacleOnOff = _UpsReceptacleOnOff_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7, 1, 2),
    _UpsReceptacleOnOff_Type()
)
upsReceptacleOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOff.setStatus("current")


class _UpsUPSMode_Type(Integer32):
    """Custom type upsUPSMode based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSMode_Type.__name__ = "Integer32"
_UpsUPSMode_Object = MibScalar
upsUPSMode = _UpsUPSMode_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 8),
    _UpsUPSMode_Type()
)
upsUPSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSMode.setStatus("current")


class _UpsRectifierOnOff_Type(Integer32):
    """Custom type upsRectifierOnOff based on Integer32"""
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


_UpsRectifierOnOff_Type.__name__ = "Integer32"
_UpsRectifierOnOff_Object = MibScalar
upsRectifierOnOff = _UpsRectifierOnOff_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 9),
    _UpsRectifierOnOff_Type()
)
upsRectifierOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOff.setStatus("current")


class _UpsBatteryChargeMethod_Type(Integer32):
    """Custom type upsBatteryChargeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethod_Type.__name__ = "Integer32"
_UpsBatteryChargeMethod_Object = MibScalar
upsBatteryChargeMethod = _UpsBatteryChargeMethod_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 10),
    _UpsBatteryChargeMethod_Type()
)
upsBatteryChargeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethod.setStatus("current")


class _UpsInverterOnOff_Type(Integer32):
    """Custom type upsInverterOnOff based on Integer32"""
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


_UpsInverterOnOff_Type.__name__ = "Integer32"
_UpsInverterOnOff_Object = MibScalar
upsInverterOnOff = _UpsInverterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 11),
    _UpsInverterOnOff_Type()
)
upsInverterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOff.setStatus("current")


class _UpsBypassOnOff_Type(Integer32):
    """Custom type upsBypassOnOff based on Integer32"""
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


_UpsBypassOnOff_Type.__name__ = "Integer32"
_UpsBypassOnOff_Object = MibScalar
upsBypassOnOff = _UpsBypassOnOff_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 12),
    _UpsBypassOnOff_Type()
)
upsBypassOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOff.setStatus("current")


class _UpsLoadSource_Type(Integer32):
    """Custom type upsLoadSource based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSource_Type.__name__ = "Integer32"
_UpsLoadSource_Object = MibScalar
upsLoadSource = _UpsLoadSource_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 13),
    _UpsLoadSource_Type()
)
upsLoadSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSource.setStatus("current")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9)
)
_UpsConfigInputVoltage_Type = NonNegativeInteger32
_UpsConfigInputVoltage_Object = MibScalar
upsConfigInputVoltage = _UpsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 1),
    _UpsConfigInputVoltage_Type()
)
upsConfigInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltage.setUnits("RMS Volts")
_UpsConfigInputFreq_Type = NonNegativeInteger32
_UpsConfigInputFreq_Object = MibScalar
upsConfigInputFreq = _UpsConfigInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 2),
    _UpsConfigInputFreq_Type()
)
upsConfigInputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreq.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreq.setUnits("0.1 Hertz")
_UpsConfigOutputVoltage_Type = NonNegativeInteger32
_UpsConfigOutputVoltage_Object = MibScalar
upsConfigOutputVoltage = _UpsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 3),
    _UpsConfigOutputVoltage_Type()
)
upsConfigOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltage.setUnits("RMS Volts")
_UpsConfigOutputFreq_Type = NonNegativeInteger32
_UpsConfigOutputFreq_Object = MibScalar
upsConfigOutputFreq = _UpsConfigOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 4),
    _UpsConfigOutputFreq_Type()
)
upsConfigOutputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreq.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreq.setUnits("0.1 Hertz")
_UpsConfigOutputVA_Type = NonNegativeInteger32
_UpsConfigOutputVA_Object = MibScalar
upsConfigOutputVA = _UpsConfigOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 5),
    _UpsConfigOutputVA_Type()
)
upsConfigOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVA.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVA.setUnits("Volt-Amps")
_UpsConfigOutputPower_Type = NonNegativeInteger32
_UpsConfigOutputPower_Object = MibScalar
upsConfigOutputPower = _UpsConfigOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 6),
    _UpsConfigOutputPower_Type()
)
upsConfigOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPower.setUnits("Watts")
_UpsConfigLowBattTime_Type = NonNegativeInteger32
_UpsConfigLowBattTime_Object = MibScalar
upsConfigLowBattTime = _UpsConfigLowBattTime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 7),
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
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 8),
    _UpsConfigAudibleStatus_Type()
)
upsConfigAudibleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatus.setStatus("current")
_UpsConfigLowVoltageTransferPoint_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPoint_Object = MibScalar
upsConfigLowVoltageTransferPoint = _UpsConfigLowVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 9),
    _UpsConfigLowVoltageTransferPoint_Type()
)
upsConfigLowVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPoint.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPoint.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPoint_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPoint_Object = MibScalar
upsConfigHighVoltageTransferPoint = _UpsConfigHighVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 10),
    _UpsConfigHighVoltageTransferPoint_Type()
)
upsConfigHighVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPoint.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPoint.setUnits("RMS Volts")
_UpsConfigBatteryCapacity_Type = NonNegativeInteger32
_UpsConfigBatteryCapacity_Object = MibScalar
upsConfigBatteryCapacity = _UpsConfigBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 11),
    _UpsConfigBatteryCapacity_Type()
)
upsConfigBatteryCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacity.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrent_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrent_Object = MibScalar
upsConfigBatteryChargeCurrent = _UpsConfigBatteryChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 12),
    _UpsConfigBatteryChargeCurrent_Type()
)
upsConfigBatteryChargeCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrent.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdown_Type(Integer32):
    """Custom type upsConfigNoLoadShutdown based on Integer32"""
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


_UpsConfigNoLoadShutdown_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdown_Object = MibScalar
upsConfigNoLoadShutdown = _UpsConfigNoLoadShutdown_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 13),
    _UpsConfigNoLoadShutdown_Type()
)
upsConfigNoLoadShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdown.setStatus("current")
_UpsConfigStartDelay_Type = PositiveInteger32
_UpsConfigStartDelay_Object = MibScalar
upsConfigStartDelay = _UpsConfigStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 14),
    _UpsConfigStartDelay_Type()
)
upsConfigStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelay.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelay.setUnits("minutes")
_UpsGetSet_ObjectIdentity = ObjectIdentity
upsGetSet = _UpsGetSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10)
)
_UpsEventGetNext_Type = PositiveInteger32
_UpsEventGetNext_Object = MibScalar
upsEventGetNext = _UpsEventGetNext_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 1),
    _UpsEventGetNext_Type()
)
upsEventGetNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNext.setStatus("current")
_UpsEventGetPrevious_Type = PositiveInteger32
_UpsEventGetPrevious_Object = MibScalar
upsEventGetPrevious = _UpsEventGetPrevious_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 2),
    _UpsEventGetPrevious_Type()
)
upsEventGetPrevious.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPrevious.setStatus("current")
_UpsEventSetStartingTimeStamp_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStamp_Object = MibScalar
upsEventSetStartingTimeStamp = _UpsEventSetStartingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 3),
    _UpsEventSetStartingTimeStamp_Type()
)
upsEventSetStartingTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStamp.setStatus("current")
_UpsEventRetreiveCurrentTimeStamp_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStamp_Object = MibScalar
upsEventRetreiveCurrentTimeStamp = _UpsEventRetreiveCurrentTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 4),
    _UpsEventRetreiveCurrentTimeStamp_Type()
)
upsEventRetreiveCurrentTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStamp.setStatus("current")
_UpsEventTableSize_Type = NonNegativeInteger32
_UpsEventTableSize_Object = MibScalar
upsEventTableSize = _UpsEventTableSize_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 5),
    _UpsEventTableSize_Type()
)
upsEventTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSize.setStatus("current")
_UpsEventTable_Object = MibTable
upsEventTable = _UpsEventTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventTable.setStatus("current")
_UpsEventEntry_Object = MibTableRow
upsEventEntry = _UpsEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1)
)
upsEventEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndex"),
)
if mibBuilder.loadTexts:
    upsEventEntry.setStatus("current")
_UpsEventLineIndex_Type = PositiveInteger32
_UpsEventLineIndex_Object = MibTableColumn
upsEventLineIndex = _UpsEventLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 1),
    _UpsEventLineIndex_Type()
)
upsEventLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndex.setStatus("current")
_UpsEventCode_Type = Integer32
_UpsEventCode_Object = MibTableColumn
upsEventCode = _UpsEventCode_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 2),
    _UpsEventCode_Type()
)
upsEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCode.setStatus("current")
_UpsEventStatus_Type = NonNegativeInteger32
_UpsEventStatus_Object = MibTableColumn
upsEventStatus = _UpsEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 3),
    _UpsEventStatus_Type()
)
upsEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatus.setStatus("current")
_UpsEventTime_Type = NonNegativeInteger32
_UpsEventTime_Object = MibTableColumn
upsEventTime = _UpsEventTime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 4),
    _UpsEventTime_Type()
)
upsEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTime.setStatus("current")
_UpsParametersRead_Type = PositiveInteger32
_UpsParametersRead_Object = MibScalar
upsParametersRead = _UpsParametersRead_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 7),
    _UpsParametersRead_Type()
)
upsParametersRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersRead.setStatus("current")
_UpsParametersWrite_Type = PositiveInteger32
_UpsParametersWrite_Object = MibScalar
upsParametersWrite = _UpsParametersWrite_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 8),
    _UpsParametersWrite_Type()
)
upsParametersWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWrite.setStatus("current")
_UpsParametersStartAddress_Type = NonNegativeInteger32
_UpsParametersStartAddress_Object = MibScalar
upsParametersStartAddress = _UpsParametersStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 9),
    _UpsParametersStartAddress_Type()
)
upsParametersStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddress.setStatus("current")
_UpsParameterTableSize_Type = NonNegativeInteger32
_UpsParameterTableSize_Object = MibScalar
upsParameterTableSize = _UpsParameterTableSize_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 10),
    _UpsParameterTableSize_Type()
)
upsParameterTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSize.setStatus("current")
_UpsParameterTable_Object = MibTable
upsParameterTable = _UpsParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterTable.setStatus("current")
_UpsParameterEntry_Object = MibTableRow
upsParameterEntry = _UpsParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11, 1)
)
upsParameterEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndex"),
)
if mibBuilder.loadTexts:
    upsParameterEntry.setStatus("current")
_UpsParameterLineIndex_Type = PositiveInteger32
_UpsParameterLineIndex_Object = MibTableColumn
upsParameterLineIndex = _UpsParameterLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11, 1, 1),
    _UpsParameterLineIndex_Type()
)
upsParameterLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndex.setStatus("current")
_UpsParameterValue_Type = Integer32
_UpsParameterValue_Object = MibTableColumn
upsParameterValue = _UpsParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11, 1, 2),
    _UpsParameterValue_Type()
)
upsParameterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValue.setStatus("current")
_UpsStatus_Type = NonNegativeInteger32
_UpsStatus_Object = MibScalar
upsStatus = _UpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 12),
    _UpsStatus_Type()
)
upsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatus.setStatus("current")
_UpsMainsStatisticsMBfail_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfail_Object = MibScalar
upsMainsStatisticsMBfail = _UpsMainsStatisticsMBfail_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 13),
    _UpsMainsStatisticsMBfail_Type()
)
upsMainsStatisticsMBfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfail.setStatus("current")
_UpsMainsStatisticsMRfail_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfail_Object = MibScalar
upsMainsStatisticsMRfail = _UpsMainsStatisticsMRfail_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 14),
    _UpsMainsStatisticsMRfail_Type()
)
upsMainsStatisticsMRfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfail.setStatus("current")
_UpsMainsStatisticsB2_Type = NonNegativeInteger32
_UpsMainsStatisticsB2_Object = MibScalar
upsMainsStatisticsB2 = _UpsMainsStatisticsB2_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 15),
    _UpsMainsStatisticsB2_Type()
)
upsMainsStatisticsB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2.setStatus("current")
_UpsMainsStatisticsB5_Type = NonNegativeInteger32
_UpsMainsStatisticsB5_Object = MibScalar
upsMainsStatisticsB5 = _UpsMainsStatisticsB5_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 16),
    _UpsMainsStatisticsB5_Type()
)
upsMainsStatisticsB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5.setStatus("current")
_UpsMainsStatisticsB10_Type = NonNegativeInteger32
_UpsMainsStatisticsB10_Object = MibScalar
upsMainsStatisticsB10 = _UpsMainsStatisticsB10_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 17),
    _UpsMainsStatisticsB10_Type()
)
upsMainsStatisticsB10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10.setStatus("current")
_UpsMainsStatisticsB200_Type = NonNegativeInteger32
_UpsMainsStatisticsB200_Object = MibScalar
upsMainsStatisticsB200 = _UpsMainsStatisticsB200_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 18),
    _UpsMainsStatisticsB200_Type()
)
upsMainsStatisticsB200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200.setStatus("current")
_UpsMainsStatisticsBypRel_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRel_Object = MibScalar
upsMainsStatisticsBypRel = _UpsMainsStatisticsBypRel_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 19),
    _UpsMainsStatisticsBypRel_Type()
)
upsMainsStatisticsBypRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRel.setStatus("current")
_UpsTimegen_Type = NonNegativeInteger32
_UpsTimegen_Object = MibScalar
upsTimegen = _UpsTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 20),
    _UpsTimegen_Type()
)
upsTimegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimegen.setStatus("current")
_UpsRequestPermission_Type = DisplayString
_UpsRequestPermission_Object = MibScalar
upsRequestPermission = _UpsRequestPermission_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 21),
    _UpsRequestPermission_Type()
)
upsRequestPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermission.setStatus("current")
_UpsEventGetCode_Type = Integer32
_UpsEventGetCode_Object = MibScalar
upsEventGetCode = _UpsEventGetCode_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 22),
    _UpsEventGetCode_Type()
)
upsEventGetCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCode.setStatus("current")
_UpsEventSpinLock_Type = TestAndIncr
_UpsEventSpinLock_Object = MibScalar
upsEventSpinLock = _UpsEventSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 23),
    _UpsEventSpinLock_Type()
)
upsEventSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLock.setStatus("current")
_UpsParameterSpinLock_Type = TestAndIncr
_UpsParameterSpinLock_Object = MibScalar
upsParameterSpinLock = _UpsParameterSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 24),
    _UpsParameterSpinLock_Type()
)
upsParameterSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLock.setStatus("current")
_GeUPSTraps_ObjectIdentity = ObjectIdentity
geUPSTraps = _GeUPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11)
)
_UpsDiagnostic_ObjectIdentity = ObjectIdentity
upsDiagnostic = _UpsDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12)
)
_UpsDiagnosticBusJACommunicationStatus_Type = Integer32
_UpsDiagnosticBusJACommunicationStatus_Object = MibScalar
upsDiagnosticBusJACommunicationStatus = _UpsDiagnosticBusJACommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 1),
    _UpsDiagnosticBusJACommunicationStatus_Type()
)
upsDiagnosticBusJACommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatus.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatus_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatus_Object = MibScalar
upsDiagnosticBusJBCommunicationStatus = _UpsDiagnosticBusJBCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatus_Type()
)
upsDiagnosticBusJBCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatus.setStatus("current")
_UpsDiagnosticBatteryLifetime_Type = Integer32
_UpsDiagnosticBatteryLifetime_Object = MibScalar
upsDiagnosticBatteryLifetime = _UpsDiagnosticBatteryLifetime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 3),
    _UpsDiagnosticBatteryLifetime_Type()
)
upsDiagnosticBatteryLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetime.setStatus("current")
_UpsDiagnosticFansLifetime_Type = Integer32
_UpsDiagnosticFansLifetime_Object = MibScalar
upsDiagnosticFansLifetime = _UpsDiagnosticFansLifetime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 4),
    _UpsDiagnosticFansLifetime_Type()
)
upsDiagnosticFansLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetime.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetime_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetime_Object = MibScalar
upsDiagnosticDCcapacitorsLifetime = _UpsDiagnosticDCcapacitorsLifetime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetime_Type()
)
upsDiagnosticDCcapacitorsLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetime.setStatus("current")
_UpsDiagnosticACcapacitorsLifetime_Type = Integer32
_UpsDiagnosticACcapacitorsLifetime_Object = MibScalar
upsDiagnosticACcapacitorsLifetime = _UpsDiagnosticACcapacitorsLifetime_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 6),
    _UpsDiagnosticACcapacitorsLifetime_Type()
)
upsDiagnosticACcapacitorsLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetime.setStatus("current")
_UpsDiagnosticGlobalServiceCheck_Type = Integer32
_UpsDiagnosticGlobalServiceCheck_Object = MibScalar
upsDiagnosticGlobalServiceCheck = _UpsDiagnosticGlobalServiceCheck_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 7),
    _UpsDiagnosticGlobalServiceCheck_Type()
)
upsDiagnosticGlobalServiceCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheck.setStatus("current")
_GeFirstUPS_ObjectIdentity = ObjectIdentity
geFirstUPS = _GeFirstUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11)
)
_UpsIdentfirst_ObjectIdentity = ObjectIdentity
upsIdentfirst = _UpsIdentfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1)
)
_UpsIdentManufacturerfirst_Type = DisplayString
_UpsIdentManufacturerfirst_Object = MibScalar
upsIdentManufacturerfirst = _UpsIdentManufacturerfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 1),
    _UpsIdentManufacturerfirst_Type()
)
upsIdentManufacturerfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturerfirst.setStatus("current")
_UpsIdentModelfirst_Type = DisplayString
_UpsIdentModelfirst_Object = MibScalar
upsIdentModelfirst = _UpsIdentModelfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 2),
    _UpsIdentModelfirst_Type()
)
upsIdentModelfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelfirst.setStatus("current")
_UpsIdentUPSSoftwareVersionfirst_Type = DisplayString
_UpsIdentUPSSoftwareVersionfirst_Object = MibScalar
upsIdentUPSSoftwareVersionfirst = _UpsIdentUPSSoftwareVersionfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 3),
    _UpsIdentUPSSoftwareVersionfirst_Type()
)
upsIdentUPSSoftwareVersionfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersionfirst.setStatus("current")
_UpsIdentAgentSoftwareVersionfirst_Type = DisplayString
_UpsIdentAgentSoftwareVersionfirst_Object = MibScalar
upsIdentAgentSoftwareVersionfirst = _UpsIdentAgentSoftwareVersionfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 4),
    _UpsIdentAgentSoftwareVersionfirst_Type()
)
upsIdentAgentSoftwareVersionfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersionfirst.setStatus("current")
_UpsIdentNamefirst_Type = DisplayString
_UpsIdentNamefirst_Object = MibScalar
upsIdentNamefirst = _UpsIdentNamefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 5),
    _UpsIdentNamefirst_Type()
)
upsIdentNamefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNamefirst.setStatus("current")
_UpsIdentAttachedDevicesfirst_Type = DisplayString
_UpsIdentAttachedDevicesfirst_Object = MibScalar
upsIdentAttachedDevicesfirst = _UpsIdentAttachedDevicesfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 6),
    _UpsIdentAttachedDevicesfirst_Type()
)
upsIdentAttachedDevicesfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicesfirst.setStatus("current")
_UpsIdentUPSSerialNumberfirst_Type = DisplayString
_UpsIdentUPSSerialNumberfirst_Object = MibScalar
upsIdentUPSSerialNumberfirst = _UpsIdentUPSSerialNumberfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 7),
    _UpsIdentUPSSerialNumberfirst_Type()
)
upsIdentUPSSerialNumberfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumberfirst.setStatus("current")
_UpsIdentComProtVersionfirst_Type = DisplayString
_UpsIdentComProtVersionfirst_Object = MibScalar
upsIdentComProtVersionfirst = _UpsIdentComProtVersionfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 8),
    _UpsIdentComProtVersionfirst_Type()
)
upsIdentComProtVersionfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersionfirst.setStatus("current")
_UpsIdentOperatingTimefirst_Type = NonNegativeInteger32
_UpsIdentOperatingTimefirst_Object = MibScalar
upsIdentOperatingTimefirst = _UpsIdentOperatingTimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 1, 9),
    _UpsIdentOperatingTimefirst_Type()
)
upsIdentOperatingTimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimefirst.setUnits("seconds")
_UpsBatteryfirst_ObjectIdentity = ObjectIdentity
upsBatteryfirst = _UpsBatteryfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2)
)


class _UpsBatteryStatusfirst_Type(Integer32):
    """Custom type upsBatteryStatusfirst based on Integer32"""
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


_UpsBatteryStatusfirst_Type.__name__ = "Integer32"
_UpsBatteryStatusfirst_Object = MibScalar
upsBatteryStatusfirst = _UpsBatteryStatusfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 1),
    _UpsBatteryStatusfirst_Type()
)
upsBatteryStatusfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatusfirst.setStatus("current")
_UpsSecondsOnBatteryfirst_Type = Integer32
_UpsSecondsOnBatteryfirst_Object = MibScalar
upsSecondsOnBatteryfirst = _UpsSecondsOnBatteryfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 2),
    _UpsSecondsOnBatteryfirst_Type()
)
upsSecondsOnBatteryfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryfirst.setUnits("seconds")
_UpsEstimatedMinutesRemainingfirst_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingfirst_Object = MibScalar
upsEstimatedMinutesRemainingfirst = _UpsEstimatedMinutesRemainingfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 3),
    _UpsEstimatedMinutesRemainingfirst_Type()
)
upsEstimatedMinutesRemainingfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingfirst.setUnits("minutes")


class _UpsEstimatedChargeRemainingfirst_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingfirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingfirst_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingfirst_Object = MibScalar
upsEstimatedChargeRemainingfirst = _UpsEstimatedChargeRemainingfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 4),
    _UpsEstimatedChargeRemainingfirst_Type()
)
upsEstimatedChargeRemainingfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingfirst.setUnits("percent")
_UpsBatteryVoltagefirst_Type = NonNegativeInteger32
_UpsBatteryVoltagefirst_Object = MibScalar
upsBatteryVoltagefirst = _UpsBatteryVoltagefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 5),
    _UpsBatteryVoltagefirst_Type()
)
upsBatteryVoltagefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltagefirst.setUnits("0.1 Volt DC")
_UpsBatteryCurrentfirst_Type = Integer32
_UpsBatteryCurrentfirst_Object = MibScalar
upsBatteryCurrentfirst = _UpsBatteryCurrentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 6),
    _UpsBatteryCurrentfirst_Type()
)
upsBatteryCurrentfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentfirst.setUnits("0.1 Amp DC")
_UpsBatteryTemperaturefirst_Type = Integer32
_UpsBatteryTemperaturefirst_Object = MibScalar
upsBatteryTemperaturefirst = _UpsBatteryTemperaturefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 7),
    _UpsBatteryTemperaturefirst_Type()
)
upsBatteryTemperaturefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperaturefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperaturefirst.setUnits("degrees Centigrade")
_UpsBatteryRipplefirst_Type = Integer32
_UpsBatteryRipplefirst_Object = MibScalar
upsBatteryRipplefirst = _UpsBatteryRipplefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 2, 8),
    _UpsBatteryRipplefirst_Type()
)
upsBatteryRipplefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipplefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipplefirst.setUnits("0.1 Volt RMS")
_UpsInputfirst_ObjectIdentity = ObjectIdentity
upsInputfirst = _UpsInputfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3)
)
_UpsInputLineBadsfirst_Type = Counter32
_UpsInputLineBadsfirst_Object = MibScalar
upsInputLineBadsfirst = _UpsInputLineBadsfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 1),
    _UpsInputLineBadsfirst_Type()
)
upsInputLineBadsfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadsfirst.setStatus("current")
_UpsInputNumLinesfirst_Type = NonNegativeInteger32
_UpsInputNumLinesfirst_Object = MibScalar
upsInputNumLinesfirst = _UpsInputNumLinesfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 2),
    _UpsInputNumLinesfirst_Type()
)
upsInputNumLinesfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinesfirst.setStatus("current")
_UpsInputFirstTable_Object = MibTable
upsInputFirstTable = _UpsInputFirstTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputFirstTable.setStatus("current")
_UpsInputFirstEntry_Object = MibTableRow
upsInputFirstEntry = _UpsInputFirstEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1)
)
upsInputFirstEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexfirst"),
)
if mibBuilder.loadTexts:
    upsInputFirstEntry.setStatus("current")
_UpsInputLineIndexfirst_Type = PositiveInteger32
_UpsInputLineIndexfirst_Object = MibTableColumn
upsInputLineIndexfirst = _UpsInputLineIndexfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1, 1),
    _UpsInputLineIndexfirst_Type()
)
upsInputLineIndexfirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexfirst.setStatus("current")
_UpsInputFrequencyfirst_Type = NonNegativeInteger32
_UpsInputFrequencyfirst_Object = MibTableColumn
upsInputFrequencyfirst = _UpsInputFrequencyfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1, 2),
    _UpsInputFrequencyfirst_Type()
)
upsInputFrequencyfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyfirst.setUnits("0.1 Hertz")
_UpsInputVoltagefirst_Type = NonNegativeInteger32
_UpsInputVoltagefirst_Object = MibTableColumn
upsInputVoltagefirst = _UpsInputVoltagefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1, 3),
    _UpsInputVoltagefirst_Type()
)
upsInputVoltagefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltagefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltagefirst.setUnits("RMS Volts")
_UpsInputCurrentfirst_Type = NonNegativeInteger32
_UpsInputCurrentfirst_Object = MibTableColumn
upsInputCurrentfirst = _UpsInputCurrentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1, 4),
    _UpsInputCurrentfirst_Type()
)
upsInputCurrentfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentfirst.setUnits("0.1 RMS Amp")
_UpsInputTruePowerfirst_Type = NonNegativeInteger32
_UpsInputTruePowerfirst_Object = MibTableColumn
upsInputTruePowerfirst = _UpsInputTruePowerfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1, 5),
    _UpsInputTruePowerfirst_Type()
)
upsInputTruePowerfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowerfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowerfirst.setUnits("Watts")
_UpsInputVoltageMinfirst_Type = NonNegativeInteger32
_UpsInputVoltageMinfirst_Object = MibTableColumn
upsInputVoltageMinfirst = _UpsInputVoltageMinfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1, 6),
    _UpsInputVoltageMinfirst_Type()
)
upsInputVoltageMinfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMinfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMinfirst.setUnits("RMS Volts")
_UpsInputVoltageMaxfirst_Type = NonNegativeInteger32
_UpsInputVoltageMaxfirst_Object = MibTableColumn
upsInputVoltageMaxfirst = _UpsInputVoltageMaxfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 3, 3, 1, 7),
    _UpsInputVoltageMaxfirst_Type()
)
upsInputVoltageMaxfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxfirst.setUnits("RMS Volts")
_UpsOutputfirst_ObjectIdentity = ObjectIdentity
upsOutputfirst = _UpsOutputfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4)
)


class _UpsOutputSourcefirst_Type(Integer32):
    """Custom type upsOutputSourcefirst based on Integer32"""
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


_UpsOutputSourcefirst_Type.__name__ = "Integer32"
_UpsOutputSourcefirst_Object = MibScalar
upsOutputSourcefirst = _UpsOutputSourcefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 1),
    _UpsOutputSourcefirst_Type()
)
upsOutputSourcefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourcefirst.setStatus("current")
_UpsOutputFrequencyfirst_Type = NonNegativeInteger32
_UpsOutputFrequencyfirst_Object = MibScalar
upsOutputFrequencyfirst = _UpsOutputFrequencyfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 2),
    _UpsOutputFrequencyfirst_Type()
)
upsOutputFrequencyfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencyfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencyfirst.setUnits("0.1 Hertz")
_UpsOutputNumLinesfirst_Type = NonNegativeInteger32
_UpsOutputNumLinesfirst_Object = MibScalar
upsOutputNumLinesfirst = _UpsOutputNumLinesfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 3),
    _UpsOutputNumLinesfirst_Type()
)
upsOutputNumLinesfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinesfirst.setStatus("current")
_UpsOutputFirstTable_Object = MibTable
upsOutputFirstTable = _UpsOutputFirstTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputFirstTable.setStatus("current")
_UpsOutputFirstEntry_Object = MibTableRow
upsOutputFirstEntry = _UpsOutputFirstEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1)
)
upsOutputFirstEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexfirst"),
)
if mibBuilder.loadTexts:
    upsOutputFirstEntry.setStatus("current")
_UpsOutputLineIndexfirst_Type = PositiveInteger32
_UpsOutputLineIndexfirst_Object = MibTableColumn
upsOutputLineIndexfirst = _UpsOutputLineIndexfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 1),
    _UpsOutputLineIndexfirst_Type()
)
upsOutputLineIndexfirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexfirst.setStatus("current")
_UpsOutputVoltagefirst_Type = NonNegativeInteger32
_UpsOutputVoltagefirst_Object = MibTableColumn
upsOutputVoltagefirst = _UpsOutputVoltagefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 2),
    _UpsOutputVoltagefirst_Type()
)
upsOutputVoltagefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltagefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltagefirst.setUnits("RMS Volts")
_UpsOutputCurrentfirst_Type = NonNegativeInteger32
_UpsOutputCurrentfirst_Object = MibTableColumn
upsOutputCurrentfirst = _UpsOutputCurrentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 3),
    _UpsOutputCurrentfirst_Type()
)
upsOutputCurrentfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentfirst.setUnits("0.1 RMS Amp")
_UpsOutputPowerfirst_Type = NonNegativeInteger32
_UpsOutputPowerfirst_Object = MibTableColumn
upsOutputPowerfirst = _UpsOutputPowerfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 4),
    _UpsOutputPowerfirst_Type()
)
upsOutputPowerfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerfirst.setUnits("Watts")


class _UpsOutputPercentLoadfirst_Type(Integer32):
    """Custom type upsOutputPercentLoadfirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadfirst_Type.__name__ = "Integer32"
_UpsOutputPercentLoadfirst_Object = MibTableColumn
upsOutputPercentLoadfirst = _UpsOutputPercentLoadfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 5),
    _UpsOutputPercentLoadfirst_Type()
)
upsOutputPercentLoadfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadfirst.setUnits("percent")


class _UpsOutputPowerFactorfirst_Type(Integer32):
    """Custom type upsOutputPowerFactorfirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorfirst_Type.__name__ = "Integer32"
_UpsOutputPowerFactorfirst_Object = MibTableColumn
upsOutputPowerFactorfirst = _UpsOutputPowerFactorfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 6),
    _UpsOutputPowerFactorfirst_Type()
)
upsOutputPowerFactorfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorfirst.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentfirst_Type = Integer32
_UpsOutputPeakCurrentfirst_Object = MibTableColumn
upsOutputPeakCurrentfirst = _UpsOutputPeakCurrentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 7),
    _UpsOutputPeakCurrentfirst_Type()
)
upsOutputPeakCurrentfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentfirst.setUnits("Amps")
_UpsOutputShareCurrentfirst_Type = Integer32
_UpsOutputShareCurrentfirst_Object = MibTableColumn
upsOutputShareCurrentfirst = _UpsOutputShareCurrentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 4, 4, 1, 8),
    _UpsOutputShareCurrentfirst_Type()
)
upsOutputShareCurrentfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentfirst.setUnits("Amps")
_UpsBypassfirst_ObjectIdentity = ObjectIdentity
upsBypassfirst = _UpsBypassfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5)
)
_UpsBypassFrequencyfirst_Type = NonNegativeInteger32
_UpsBypassFrequencyfirst_Object = MibScalar
upsBypassFrequencyfirst = _UpsBypassFrequencyfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 1),
    _UpsBypassFrequencyfirst_Type()
)
upsBypassFrequencyfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencyfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencyfirst.setUnits("0.1 Hertz")
_UpsBypassNumLinesfirst_Type = NonNegativeInteger32
_UpsBypassNumLinesfirst_Object = MibScalar
upsBypassNumLinesfirst = _UpsBypassNumLinesfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 2),
    _UpsBypassNumLinesfirst_Type()
)
upsBypassNumLinesfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinesfirst.setStatus("current")
_UpsBypassFirstTable_Object = MibTable
upsBypassFirstTable = _UpsBypassFirstTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassFirstTable.setStatus("current")
_UpsBypassFirstEntry_Object = MibTableRow
upsBypassFirstEntry = _UpsBypassFirstEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 3, 1)
)
upsBypassFirstEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexfirst"),
)
if mibBuilder.loadTexts:
    upsBypassFirstEntry.setStatus("current")
_UpsBypassLineIndexfirst_Type = PositiveInteger32
_UpsBypassLineIndexfirst_Object = MibTableColumn
upsBypassLineIndexfirst = _UpsBypassLineIndexfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 3, 1, 1),
    _UpsBypassLineIndexfirst_Type()
)
upsBypassLineIndexfirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexfirst.setStatus("current")
_UpsBypassVoltagefirst_Type = NonNegativeInteger32
_UpsBypassVoltagefirst_Object = MibTableColumn
upsBypassVoltagefirst = _UpsBypassVoltagefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 3, 1, 2),
    _UpsBypassVoltagefirst_Type()
)
upsBypassVoltagefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltagefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltagefirst.setUnits("RMS Volts")
_UpsBypassCurrentfirst_Type = NonNegativeInteger32
_UpsBypassCurrentfirst_Object = MibTableColumn
upsBypassCurrentfirst = _UpsBypassCurrentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 3, 1, 3),
    _UpsBypassCurrentfirst_Type()
)
upsBypassCurrentfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentfirst.setUnits("0.1 RMS Amp")
_UpsBypassPowerfirst_Type = NonNegativeInteger32
_UpsBypassPowerfirst_Object = MibTableColumn
upsBypassPowerfirst = _UpsBypassPowerfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 5, 3, 1, 4),
    _UpsBypassPowerfirst_Type()
)
upsBypassPowerfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowerfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowerfirst.setUnits("Watts")
_UpsAlarmfirst_ObjectIdentity = ObjectIdentity
upsAlarmfirst = _UpsAlarmfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6)
)
_UpsAlarmsPresentfirst_Type = Gauge32
_UpsAlarmsPresentfirst_Object = MibScalar
upsAlarmsPresentfirst = _UpsAlarmsPresentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 1),
    _UpsAlarmsPresentfirst_Type()
)
upsAlarmsPresentfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentfirst.setStatus("current")
_UpsAlarmFirstTable_Object = MibTable
upsAlarmFirstTable = _UpsAlarmFirstTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmFirstTable.setStatus("current")
_UpsAlarmFirstEntry_Object = MibTableRow
upsAlarmFirstEntry = _UpsAlarmFirstEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 2, 1)
)
upsAlarmFirstEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdfirst"),
)
if mibBuilder.loadTexts:
    upsAlarmFirstEntry.setStatus("current")
_UpsAlarmIdfirst_Type = PositiveInteger32
_UpsAlarmIdfirst_Object = MibTableColumn
upsAlarmIdfirst = _UpsAlarmIdfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 2, 1, 1),
    _UpsAlarmIdfirst_Type()
)
upsAlarmIdfirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdfirst.setStatus("current")
_UpsAlarmDescrfirst_Type = AutonomousType
_UpsAlarmDescrfirst_Object = MibTableColumn
upsAlarmDescrfirst = _UpsAlarmDescrfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 2, 1, 2),
    _UpsAlarmDescrfirst_Type()
)
upsAlarmDescrfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrfirst.setStatus("current")
_UpsAlarmTimefirst_Type = TimeStamp
_UpsAlarmTimefirst_Object = MibTableColumn
upsAlarmTimefirst = _UpsAlarmTimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 2, 1, 3),
    _UpsAlarmTimefirst_Type()
)
upsAlarmTimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimefirst.setStatus("current")
_UpsWellKnownAlarmsfirst_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmsfirst = _UpsWellKnownAlarmsfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3)
)
_UpsAlarmBatteryBadfirst_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadfirst = _UpsAlarmBatteryBadfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadfirst.setStatus("current")
_UpsAlarmOnBatteryfirst_ObjectIdentity = ObjectIdentity
upsAlarmOnBatteryfirst = _UpsAlarmOnBatteryfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatteryfirst.setStatus("current")
_UpsAlarmLowBatteryfirst_ObjectIdentity = ObjectIdentity
upsAlarmLowBatteryfirst = _UpsAlarmLowBatteryfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatteryfirst.setStatus("current")
_UpsAlarmDepletedBatteryfirst_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatteryfirst = _UpsAlarmDepletedBatteryfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatteryfirst.setStatus("current")
_UpsAlarmTempBadfirst_ObjectIdentity = ObjectIdentity
upsAlarmTempBadfirst = _UpsAlarmTempBadfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadfirst.setStatus("current")
_UpsAlarmInputBadfirst_ObjectIdentity = ObjectIdentity
upsAlarmInputBadfirst = _UpsAlarmInputBadfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadfirst.setStatus("current")
_UpsAlarmOutputBadfirst_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadfirst = _UpsAlarmOutputBadfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadfirst.setStatus("current")
_UpsAlarmOutputOverloadfirst_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadfirst = _UpsAlarmOutputOverloadfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadfirst.setStatus("current")
_UpsAlarmOnBypassfirst_ObjectIdentity = ObjectIdentity
upsAlarmOnBypassfirst = _UpsAlarmOnBypassfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypassfirst.setStatus("current")
_UpsAlarmBypassBadfirst_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadfirst = _UpsAlarmBypassBadfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadfirst.setStatus("current")
_UpsAlarmOutputOffAsRequestedfirst_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedfirst = _UpsAlarmOutputOffAsRequestedfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedfirst.setStatus("current")
_UpsAlarmUpsOffAsRequestedfirst_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedfirst = _UpsAlarmUpsOffAsRequestedfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedfirst.setStatus("current")
_UpsAlarmChargerFailedfirst_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedfirst = _UpsAlarmChargerFailedfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedfirst.setStatus("current")
_UpsAlarmUpsOutputOfffirst_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOfffirst = _UpsAlarmUpsOutputOfffirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOfffirst.setStatus("current")
_UpsAlarmUpsSystemOfffirst_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOfffirst = _UpsAlarmUpsSystemOfffirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOfffirst.setStatus("current")
_UpsAlarmFanFailurefirst_ObjectIdentity = ObjectIdentity
upsAlarmFanFailurefirst = _UpsAlarmFanFailurefirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailurefirst.setStatus("current")
_UpsAlarmFuseFailurefirst_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailurefirst = _UpsAlarmFuseFailurefirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailurefirst.setStatus("current")
_UpsAlarmGeneralFaultfirst_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultfirst = _UpsAlarmGeneralFaultfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultfirst.setStatus("current")
_UpsAlarmDiagnosticTestFailedfirst_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedfirst = _UpsAlarmDiagnosticTestFailedfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedfirst.setStatus("current")
_UpsAlarmCommunicationsLostfirst_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostfirst = _UpsAlarmCommunicationsLostfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostfirst.setStatus("current")
_UpsAlarmAwaitingPowerfirst_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowerfirst = _UpsAlarmAwaitingPowerfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowerfirst.setStatus("current")
_UpsAlarmShutdownPendingfirst_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingfirst = _UpsAlarmShutdownPendingfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingfirst.setStatus("current")
_UpsAlarmShutdownImminentfirst_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentfirst = _UpsAlarmShutdownImminentfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentfirst.setStatus("current")
_UpsAlarmTestInProgressfirst_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgressfirst = _UpsAlarmTestInProgressfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgressfirst.setStatus("current")
_UpsAlarmReceptacleOfffirst_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOfffirst = _UpsAlarmReceptacleOfffirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOfffirst.setStatus("current")
_UpsAlarmHighSpeedBusFailurefirst_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailurefirst = _UpsAlarmHighSpeedBusFailurefirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailurefirst.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailurefirst_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailurefirst = _UpsAlarmHighSpeedBusJACRCFailurefirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailurefirst.setStatus("current")
_UpsAlarmConnectivityBusFailurefirst_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailurefirst = _UpsAlarmConnectivityBusFailurefirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailurefirst.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailurefirst_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailurefirst = _UpsAlarmHighSpeedBusJBCRCFailurefirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailurefirst.setStatus("current")
_UpsAlarmCurrentSharingfirst_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingfirst = _UpsAlarmCurrentSharingfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingfirst.setStatus("current")
_UpsAlarmDCRipplefirst_ObjectIdentity = ObjectIdentity
upsAlarmDCRipplefirst = _UpsAlarmDCRipplefirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipplefirst.setStatus("current")
_UpsAlarmMaskAfirst_Type = Unsigned32
_UpsAlarmMaskAfirst_Object = MibScalar
upsAlarmMaskAfirst = _UpsAlarmMaskAfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 6, 4),
    _UpsAlarmMaskAfirst_Type()
)
upsAlarmMaskAfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAfirst.setStatus("current")
_UpsTestfirst_ObjectIdentity = ObjectIdentity
upsTestfirst = _UpsTestfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7)
)
_UpsTestIdfirst_Type = ObjectIdentifier
_UpsTestIdfirst_Object = MibScalar
upsTestIdfirst = _UpsTestIdfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 1),
    _UpsTestIdfirst_Type()
)
upsTestIdfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdfirst.setStatus("current")
_UpsTestSpinLockfirst_Type = TestAndIncr
_UpsTestSpinLockfirst_Object = MibScalar
upsTestSpinLockfirst = _UpsTestSpinLockfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 2),
    _UpsTestSpinLockfirst_Type()
)
upsTestSpinLockfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLockfirst.setStatus("current")


class _UpsTestResultsSummaryfirst_Type(Integer32):
    """Custom type upsTestResultsSummaryfirst based on Integer32"""
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


_UpsTestResultsSummaryfirst_Type.__name__ = "Integer32"
_UpsTestResultsSummaryfirst_Object = MibScalar
upsTestResultsSummaryfirst = _UpsTestResultsSummaryfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 3),
    _UpsTestResultsSummaryfirst_Type()
)
upsTestResultsSummaryfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummaryfirst.setStatus("current")
_UpsTestResultsDetailfirst_Type = DisplayString
_UpsTestResultsDetailfirst_Object = MibScalar
upsTestResultsDetailfirst = _UpsTestResultsDetailfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 4),
    _UpsTestResultsDetailfirst_Type()
)
upsTestResultsDetailfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailfirst.setStatus("current")
_UpsTestStartTimefirst_Type = TimeStamp
_UpsTestStartTimefirst_Object = MibScalar
upsTestStartTimefirst = _UpsTestStartTimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 5),
    _UpsTestStartTimefirst_Type()
)
upsTestStartTimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimefirst.setStatus("current")
_UpsTestElapsedTimefirst_Type = TimeInterval
_UpsTestElapsedTimefirst_Object = MibScalar
upsTestElapsedTimefirst = _UpsTestElapsedTimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 6),
    _UpsTestElapsedTimefirst_Type()
)
upsTestElapsedTimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimefirst.setStatus("current")
_UpsWellKnownTestsfirst_ObjectIdentity = ObjectIdentity
upsWellKnownTestsfirst = _UpsWellKnownTestsfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 7)
)
_UpsTestNoTestsInitiatedfirst_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedfirst = _UpsTestNoTestsInitiatedfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedfirst.setStatus("current")
_UpsTestAbortTestInProgressfirst_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgressfirst = _UpsTestAbortTestInProgressfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgressfirst.setStatus("current")
_UpsTestGeneralSystemsTestfirst_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestfirst = _UpsTestGeneralSystemsTestfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestfirst.setStatus("current")
_UpsTestQuickBatteryTestfirst_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestfirst = _UpsTestQuickBatteryTestfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestfirst.setStatus("current")
_UpsTestDeepBatteryCalibrationfirst_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationfirst = _UpsTestDeepBatteryCalibrationfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationfirst.setStatus("current")
_UpsControlfirst_ObjectIdentity = ObjectIdentity
upsControlfirst = _UpsControlfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8)
)


class _UpsShutdownTypefirst_Type(Integer32):
    """Custom type upsShutdownTypefirst based on Integer32"""
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


_UpsShutdownTypefirst_Type.__name__ = "Integer32"
_UpsShutdownTypefirst_Object = MibScalar
upsShutdownTypefirst = _UpsShutdownTypefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 1),
    _UpsShutdownTypefirst_Type()
)
upsShutdownTypefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypefirst.setStatus("current")


class _UpsShutdownAfterDelayfirst_Type(Integer32):
    """Custom type upsShutdownAfterDelayfirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelayfirst_Type.__name__ = "Integer32"
_UpsShutdownAfterDelayfirst_Object = MibScalar
upsShutdownAfterDelayfirst = _UpsShutdownAfterDelayfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 2),
    _UpsShutdownAfterDelayfirst_Type()
)
upsShutdownAfterDelayfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayfirst.setUnits("seconds")


class _UpsStartupAfterDelayfirst_Type(Integer32):
    """Custom type upsStartupAfterDelayfirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelayfirst_Type.__name__ = "Integer32"
_UpsStartupAfterDelayfirst_Object = MibScalar
upsStartupAfterDelayfirst = _UpsStartupAfterDelayfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 3),
    _UpsStartupAfterDelayfirst_Type()
)
upsStartupAfterDelayfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelayfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelayfirst.setUnits("seconds")


class _UpsRebootWithDurationfirst_Type(Integer32):
    """Custom type upsRebootWithDurationfirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationfirst_Type.__name__ = "Integer32"
_UpsRebootWithDurationfirst_Object = MibScalar
upsRebootWithDurationfirst = _UpsRebootWithDurationfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 4),
    _UpsRebootWithDurationfirst_Type()
)
upsRebootWithDurationfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationfirst.setUnits("seconds")


class _UpsAutoRestartfirst_Type(Integer32):
    """Custom type upsAutoRestartfirst based on Integer32"""
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


_UpsAutoRestartfirst_Type.__name__ = "Integer32"
_UpsAutoRestartfirst_Object = MibScalar
upsAutoRestartfirst = _UpsAutoRestartfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 5),
    _UpsAutoRestartfirst_Type()
)
upsAutoRestartfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartfirst.setStatus("current")
_UpsReceptaclesNumfirst_Type = NonNegativeInteger32
_UpsReceptaclesNumfirst_Object = MibScalar
upsReceptaclesNumfirst = _UpsReceptaclesNumfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 6),
    _UpsReceptaclesNumfirst_Type()
)
upsReceptaclesNumfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumfirst.setStatus("current")
_UpsReceptacleFirstTable_Object = MibTable
upsReceptacleFirstTable = _UpsReceptacleFirstTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleFirstTable.setStatus("current")
_UpsReceptacleFirstEntry_Object = MibTableRow
upsReceptacleFirstEntry = _UpsReceptacleFirstEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 7, 1)
)
upsReceptacleFirstEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexfirst"),
)
if mibBuilder.loadTexts:
    upsReceptacleFirstEntry.setStatus("current")
_UpsReceptacleLineIndexfirst_Type = PositiveInteger32
_UpsReceptacleLineIndexfirst_Object = MibTableColumn
upsReceptacleLineIndexfirst = _UpsReceptacleLineIndexfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 7, 1, 1),
    _UpsReceptacleLineIndexfirst_Type()
)
upsReceptacleLineIndexfirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexfirst.setStatus("current")


class _UpsReceptacleOnOfffirst_Type(Integer32):
    """Custom type upsReceptacleOnOfffirst based on Integer32"""
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


_UpsReceptacleOnOfffirst_Type.__name__ = "Integer32"
_UpsReceptacleOnOfffirst_Object = MibTableColumn
upsReceptacleOnOfffirst = _UpsReceptacleOnOfffirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 7, 1, 2),
    _UpsReceptacleOnOfffirst_Type()
)
upsReceptacleOnOfffirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOfffirst.setStatus("current")


class _UpsUPSModefirst_Type(Integer32):
    """Custom type upsUPSModefirst based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModefirst_Type.__name__ = "Integer32"
_UpsUPSModefirst_Object = MibScalar
upsUPSModefirst = _UpsUPSModefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 8),
    _UpsUPSModefirst_Type()
)
upsUPSModefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModefirst.setStatus("current")


class _UpsRectifierOnOfffirst_Type(Integer32):
    """Custom type upsRectifierOnOfffirst based on Integer32"""
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


_UpsRectifierOnOfffirst_Type.__name__ = "Integer32"
_UpsRectifierOnOfffirst_Object = MibScalar
upsRectifierOnOfffirst = _UpsRectifierOnOfffirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 9),
    _UpsRectifierOnOfffirst_Type()
)
upsRectifierOnOfffirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOfffirst.setStatus("current")


class _UpsBatteryChargeMethodfirst_Type(Integer32):
    """Custom type upsBatteryChargeMethodfirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodfirst_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodfirst_Object = MibScalar
upsBatteryChargeMethodfirst = _UpsBatteryChargeMethodfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 10),
    _UpsBatteryChargeMethodfirst_Type()
)
upsBatteryChargeMethodfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodfirst.setStatus("current")


class _UpsInverterOnOfffirst_Type(Integer32):
    """Custom type upsInverterOnOfffirst based on Integer32"""
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


_UpsInverterOnOfffirst_Type.__name__ = "Integer32"
_UpsInverterOnOfffirst_Object = MibScalar
upsInverterOnOfffirst = _UpsInverterOnOfffirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 11),
    _UpsInverterOnOfffirst_Type()
)
upsInverterOnOfffirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOfffirst.setStatus("current")


class _UpsBypassOnOfffirst_Type(Integer32):
    """Custom type upsBypassOnOfffirst based on Integer32"""
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


_UpsBypassOnOfffirst_Type.__name__ = "Integer32"
_UpsBypassOnOfffirst_Object = MibScalar
upsBypassOnOfffirst = _UpsBypassOnOfffirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 12),
    _UpsBypassOnOfffirst_Type()
)
upsBypassOnOfffirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOfffirst.setStatus("current")


class _UpsLoadSourcefirst_Type(Integer32):
    """Custom type upsLoadSourcefirst based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourcefirst_Type.__name__ = "Integer32"
_UpsLoadSourcefirst_Object = MibScalar
upsLoadSourcefirst = _UpsLoadSourcefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 8, 13),
    _UpsLoadSourcefirst_Type()
)
upsLoadSourcefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourcefirst.setStatus("current")
_UpsConfigfirst_ObjectIdentity = ObjectIdentity
upsConfigfirst = _UpsConfigfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9)
)
_UpsConfigInputVoltagefirst_Type = NonNegativeInteger32
_UpsConfigInputVoltagefirst_Object = MibScalar
upsConfigInputVoltagefirst = _UpsConfigInputVoltagefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 1),
    _UpsConfigInputVoltagefirst_Type()
)
upsConfigInputVoltagefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltagefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltagefirst.setUnits("RMS Volts")
_UpsConfigInputFreqfirst_Type = NonNegativeInteger32
_UpsConfigInputFreqfirst_Object = MibScalar
upsConfigInputFreqfirst = _UpsConfigInputFreqfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 2),
    _UpsConfigInputFreqfirst_Type()
)
upsConfigInputFreqfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqfirst.setUnits("0.1 Hertz")
_UpsConfigOutputVoltagefirst_Type = NonNegativeInteger32
_UpsConfigOutputVoltagefirst_Object = MibScalar
upsConfigOutputVoltagefirst = _UpsConfigOutputVoltagefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 3),
    _UpsConfigOutputVoltagefirst_Type()
)
upsConfigOutputVoltagefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagefirst.setUnits("RMS Volts")
_UpsConfigOutputFreqfirst_Type = NonNegativeInteger32
_UpsConfigOutputFreqfirst_Object = MibScalar
upsConfigOutputFreqfirst = _UpsConfigOutputFreqfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 4),
    _UpsConfigOutputFreqfirst_Type()
)
upsConfigOutputFreqfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqfirst.setUnits("0.1 Hertz")
_UpsConfigOutputVAfirst_Type = NonNegativeInteger32
_UpsConfigOutputVAfirst_Object = MibScalar
upsConfigOutputVAfirst = _UpsConfigOutputVAfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 5),
    _UpsConfigOutputVAfirst_Type()
)
upsConfigOutputVAfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAfirst.setUnits("Volt-Amps")
_UpsConfigOutputPowerfirst_Type = NonNegativeInteger32
_UpsConfigOutputPowerfirst_Object = MibScalar
upsConfigOutputPowerfirst = _UpsConfigOutputPowerfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 6),
    _UpsConfigOutputPowerfirst_Type()
)
upsConfigOutputPowerfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowerfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowerfirst.setUnits("Watts")
_UpsConfigLowBattTimefirst_Type = NonNegativeInteger32
_UpsConfigLowBattTimefirst_Object = MibScalar
upsConfigLowBattTimefirst = _UpsConfigLowBattTimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 7),
    _UpsConfigLowBattTimefirst_Type()
)
upsConfigLowBattTimefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimefirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimefirst.setUnits("minutes")


class _UpsConfigAudibleStatusfirst_Type(Integer32):
    """Custom type upsConfigAudibleStatusfirst based on Integer32"""
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


_UpsConfigAudibleStatusfirst_Type.__name__ = "Integer32"
_UpsConfigAudibleStatusfirst_Object = MibScalar
upsConfigAudibleStatusfirst = _UpsConfigAudibleStatusfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 8),
    _UpsConfigAudibleStatusfirst_Type()
)
upsConfigAudibleStatusfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatusfirst.setStatus("current")
_UpsConfigLowVoltageTransferPointfirst_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointfirst_Object = MibScalar
upsConfigLowVoltageTransferPointfirst = _UpsConfigLowVoltageTransferPointfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 9),
    _UpsConfigLowVoltageTransferPointfirst_Type()
)
upsConfigLowVoltageTransferPointfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointfirst.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointfirst_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointfirst_Object = MibScalar
upsConfigHighVoltageTransferPointfirst = _UpsConfigHighVoltageTransferPointfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 10),
    _UpsConfigHighVoltageTransferPointfirst_Type()
)
upsConfigHighVoltageTransferPointfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointfirst.setUnits("RMS Volts")
_UpsConfigBatteryCapacityfirst_Type = NonNegativeInteger32
_UpsConfigBatteryCapacityfirst_Object = MibScalar
upsConfigBatteryCapacityfirst = _UpsConfigBatteryCapacityfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 11),
    _UpsConfigBatteryCapacityfirst_Type()
)
upsConfigBatteryCapacityfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityfirst.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentfirst_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentfirst_Object = MibScalar
upsConfigBatteryChargeCurrentfirst = _UpsConfigBatteryChargeCurrentfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 12),
    _UpsConfigBatteryChargeCurrentfirst_Type()
)
upsConfigBatteryChargeCurrentfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentfirst.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdownfirst_Type(Integer32):
    """Custom type upsConfigNoLoadShutdownfirst based on Integer32"""
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


_UpsConfigNoLoadShutdownfirst_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdownfirst_Object = MibScalar
upsConfigNoLoadShutdownfirst = _UpsConfigNoLoadShutdownfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 13),
    _UpsConfigNoLoadShutdownfirst_Type()
)
upsConfigNoLoadShutdownfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdownfirst.setStatus("current")
_UpsConfigStartDelayfirst_Type = PositiveInteger32
_UpsConfigStartDelayfirst_Object = MibScalar
upsConfigStartDelayfirst = _UpsConfigStartDelayfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 9, 14),
    _UpsConfigStartDelayfirst_Type()
)
upsConfigStartDelayfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelayfirst.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelayfirst.setUnits("minutes")
_UpsGetSetfirst_ObjectIdentity = ObjectIdentity
upsGetSetfirst = _UpsGetSetfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10)
)
_UpsEventGetNextfirst_Type = PositiveInteger32
_UpsEventGetNextfirst_Object = MibScalar
upsEventGetNextfirst = _UpsEventGetNextfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 1),
    _UpsEventGetNextfirst_Type()
)
upsEventGetNextfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextfirst.setStatus("current")
_UpsEventGetPreviousfirst_Type = PositiveInteger32
_UpsEventGetPreviousfirst_Object = MibScalar
upsEventGetPreviousfirst = _UpsEventGetPreviousfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 2),
    _UpsEventGetPreviousfirst_Type()
)
upsEventGetPreviousfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPreviousfirst.setStatus("current")
_UpsEventSetStartingTimeStampfirst_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampfirst_Object = MibScalar
upsEventSetStartingTimeStampfirst = _UpsEventSetStartingTimeStampfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 3),
    _UpsEventSetStartingTimeStampfirst_Type()
)
upsEventSetStartingTimeStampfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampfirst.setStatus("current")
_UpsEventRetreiveCurrentTimeStampfirst_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampfirst_Object = MibScalar
upsEventRetreiveCurrentTimeStampfirst = _UpsEventRetreiveCurrentTimeStampfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 4),
    _UpsEventRetreiveCurrentTimeStampfirst_Type()
)
upsEventRetreiveCurrentTimeStampfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampfirst.setStatus("current")
_UpsEventTableSizefirst_Type = NonNegativeInteger32
_UpsEventTableSizefirst_Object = MibScalar
upsEventTableSizefirst = _UpsEventTableSizefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 5),
    _UpsEventTableSizefirst_Type()
)
upsEventTableSizefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizefirst.setStatus("current")
_UpsEventFirstTable_Object = MibTable
upsEventFirstTable = _UpsEventFirstTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventFirstTable.setStatus("current")
_UpsEventFirstEntry_Object = MibTableRow
upsEventFirstEntry = _UpsEventFirstEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 6, 1)
)
upsEventFirstEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexfirst"),
)
if mibBuilder.loadTexts:
    upsEventFirstEntry.setStatus("current")
_UpsEventLineIndexfirst_Type = PositiveInteger32
_UpsEventLineIndexfirst_Object = MibTableColumn
upsEventLineIndexfirst = _UpsEventLineIndexfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 6, 1, 1),
    _UpsEventLineIndexfirst_Type()
)
upsEventLineIndexfirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexfirst.setStatus("current")
_UpsEventCodefirst_Type = Integer32
_UpsEventCodefirst_Object = MibTableColumn
upsEventCodefirst = _UpsEventCodefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 6, 1, 2),
    _UpsEventCodefirst_Type()
)
upsEventCodefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodefirst.setStatus("current")
_UpsEventStatusfirst_Type = NonNegativeInteger32
_UpsEventStatusfirst_Object = MibTableColumn
upsEventStatusfirst = _UpsEventStatusfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 6, 1, 3),
    _UpsEventStatusfirst_Type()
)
upsEventStatusfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatusfirst.setStatus("current")
_UpsEventTimefirst_Type = NonNegativeInteger32
_UpsEventTimefirst_Object = MibTableColumn
upsEventTimefirst = _UpsEventTimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 6, 1, 4),
    _UpsEventTimefirst_Type()
)
upsEventTimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimefirst.setStatus("current")
_UpsParametersReadfirst_Type = PositiveInteger32
_UpsParametersReadfirst_Object = MibScalar
upsParametersReadfirst = _UpsParametersReadfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 7),
    _UpsParametersReadfirst_Type()
)
upsParametersReadfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadfirst.setStatus("current")
_UpsParametersWritefirst_Type = PositiveInteger32
_UpsParametersWritefirst_Object = MibScalar
upsParametersWritefirst = _UpsParametersWritefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 8),
    _UpsParametersWritefirst_Type()
)
upsParametersWritefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWritefirst.setStatus("current")
_UpsParametersStartAddressfirst_Type = NonNegativeInteger32
_UpsParametersStartAddressfirst_Object = MibScalar
upsParametersStartAddressfirst = _UpsParametersStartAddressfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 9),
    _UpsParametersStartAddressfirst_Type()
)
upsParametersStartAddressfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddressfirst.setStatus("current")
_UpsParameterTableSizefirst_Type = NonNegativeInteger32
_UpsParameterTableSizefirst_Object = MibScalar
upsParameterTableSizefirst = _UpsParameterTableSizefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 10),
    _UpsParameterTableSizefirst_Type()
)
upsParameterTableSizefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizefirst.setStatus("current")
_UpsParameterFirstTable_Object = MibTable
upsParameterFirstTable = _UpsParameterFirstTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterFirstTable.setStatus("current")
_UpsParameterFirstEntry_Object = MibTableRow
upsParameterFirstEntry = _UpsParameterFirstEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 11, 1)
)
upsParameterFirstEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexfirst"),
)
if mibBuilder.loadTexts:
    upsParameterFirstEntry.setStatus("current")
_UpsParameterLineIndexfirst_Type = PositiveInteger32
_UpsParameterLineIndexfirst_Object = MibTableColumn
upsParameterLineIndexfirst = _UpsParameterLineIndexfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 11, 1, 1),
    _UpsParameterLineIndexfirst_Type()
)
upsParameterLineIndexfirst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexfirst.setStatus("current")
_UpsParameterValuefirst_Type = Integer32
_UpsParameterValuefirst_Object = MibTableColumn
upsParameterValuefirst = _UpsParameterValuefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 11, 1, 2),
    _UpsParameterValuefirst_Type()
)
upsParameterValuefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValuefirst.setStatus("current")
_UpsStatusfirst_Type = NonNegativeInteger32
_UpsStatusfirst_Object = MibScalar
upsStatusfirst = _UpsStatusfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 12),
    _UpsStatusfirst_Type()
)
upsStatusfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusfirst.setStatus("current")
_UpsMainsStatisticsMBfailfirst_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailfirst_Object = MibScalar
upsMainsStatisticsMBfailfirst = _UpsMainsStatisticsMBfailfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 13),
    _UpsMainsStatisticsMBfailfirst_Type()
)
upsMainsStatisticsMBfailfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailfirst.setStatus("current")
_UpsMainsStatisticsMRfailfirst_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailfirst_Object = MibScalar
upsMainsStatisticsMRfailfirst = _UpsMainsStatisticsMRfailfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 14),
    _UpsMainsStatisticsMRfailfirst_Type()
)
upsMainsStatisticsMRfailfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailfirst.setStatus("current")
_UpsMainsStatisticsB2first_Type = NonNegativeInteger32
_UpsMainsStatisticsB2first_Object = MibScalar
upsMainsStatisticsB2first = _UpsMainsStatisticsB2first_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 15),
    _UpsMainsStatisticsB2first_Type()
)
upsMainsStatisticsB2first.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2first.setStatus("current")
_UpsMainsStatisticsB5first_Type = NonNegativeInteger32
_UpsMainsStatisticsB5first_Object = MibScalar
upsMainsStatisticsB5first = _UpsMainsStatisticsB5first_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 16),
    _UpsMainsStatisticsB5first_Type()
)
upsMainsStatisticsB5first.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5first.setStatus("current")
_UpsMainsStatisticsB10first_Type = NonNegativeInteger32
_UpsMainsStatisticsB10first_Object = MibScalar
upsMainsStatisticsB10first = _UpsMainsStatisticsB10first_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 17),
    _UpsMainsStatisticsB10first_Type()
)
upsMainsStatisticsB10first.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10first.setStatus("current")
_UpsMainsStatisticsB200first_Type = NonNegativeInteger32
_UpsMainsStatisticsB200first_Object = MibScalar
upsMainsStatisticsB200first = _UpsMainsStatisticsB200first_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 18),
    _UpsMainsStatisticsB200first_Type()
)
upsMainsStatisticsB200first.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200first.setStatus("current")
_UpsMainsStatisticsBypRelfirst_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelfirst_Object = MibScalar
upsMainsStatisticsBypRelfirst = _UpsMainsStatisticsBypRelfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 19),
    _UpsMainsStatisticsBypRelfirst_Type()
)
upsMainsStatisticsBypRelfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelfirst.setStatus("current")
_UpsTimefirst_Type = NonNegativeInteger32
_UpsTimefirst_Object = MibScalar
upsTimefirst = _UpsTimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 20),
    _UpsTimefirst_Type()
)
upsTimefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimefirst.setStatus("current")
_UpsRequestPermissionfirst_Type = DisplayString
_UpsRequestPermissionfirst_Object = MibScalar
upsRequestPermissionfirst = _UpsRequestPermissionfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 21),
    _UpsRequestPermissionfirst_Type()
)
upsRequestPermissionfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissionfirst.setStatus("current")
_UpsEventGetCodefirst_Type = Integer32
_UpsEventGetCodefirst_Object = MibScalar
upsEventGetCodefirst = _UpsEventGetCodefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 22),
    _UpsEventGetCodefirst_Type()
)
upsEventGetCodefirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodefirst.setStatus("current")
_UpsEventSpinLockfirst_Type = TestAndIncr
_UpsEventSpinLockfirst_Object = MibScalar
upsEventSpinLockfirst = _UpsEventSpinLockfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 23),
    _UpsEventSpinLockfirst_Type()
)
upsEventSpinLockfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLockfirst.setStatus("current")
_UpsParameterSpinLockfirst_Type = TestAndIncr
_UpsParameterSpinLockfirst_Object = MibScalar
upsParameterSpinLockfirst = _UpsParameterSpinLockfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 10, 24),
    _UpsParameterSpinLockfirst_Type()
)
upsParameterSpinLockfirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLockfirst.setStatus("current")
_GeUPSTrapsfirst_ObjectIdentity = ObjectIdentity
geUPSTrapsfirst = _GeUPSTrapsfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11)
)
_UpsDiagnosticfirst_ObjectIdentity = ObjectIdentity
upsDiagnosticfirst = _UpsDiagnosticfirst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12)
)
_UpsDiagnosticBusJACommunicationStatusfirst_Type = Integer32
_UpsDiagnosticBusJACommunicationStatusfirst_Object = MibScalar
upsDiagnosticBusJACommunicationStatusfirst = _UpsDiagnosticBusJACommunicationStatusfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12, 1),
    _UpsDiagnosticBusJACommunicationStatusfirst_Type()
)
upsDiagnosticBusJACommunicationStatusfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatusfirst.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatusfirst_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatusfirst_Object = MibScalar
upsDiagnosticBusJBCommunicationStatusfirst = _UpsDiagnosticBusJBCommunicationStatusfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatusfirst_Type()
)
upsDiagnosticBusJBCommunicationStatusfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatusfirst.setStatus("current")
_UpsDiagnosticBatteryLifetimefirst_Type = Integer32
_UpsDiagnosticBatteryLifetimefirst_Object = MibScalar
upsDiagnosticBatteryLifetimefirst = _UpsDiagnosticBatteryLifetimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12, 3),
    _UpsDiagnosticBatteryLifetimefirst_Type()
)
upsDiagnosticBatteryLifetimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimefirst.setStatus("current")
_UpsDiagnosticFansLifetimefirst_Type = Integer32
_UpsDiagnosticFansLifetimefirst_Object = MibScalar
upsDiagnosticFansLifetimefirst = _UpsDiagnosticFansLifetimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12, 4),
    _UpsDiagnosticFansLifetimefirst_Type()
)
upsDiagnosticFansLifetimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimefirst.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimefirst_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimefirst_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimefirst = _UpsDiagnosticDCcapacitorsLifetimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimefirst_Type()
)
upsDiagnosticDCcapacitorsLifetimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimefirst.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimefirst_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimefirst_Object = MibScalar
upsDiagnosticACcapacitorsLifetimefirst = _UpsDiagnosticACcapacitorsLifetimefirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimefirst_Type()
)
upsDiagnosticACcapacitorsLifetimefirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimefirst.setStatus("current")
_UpsDiagnosticGlobalServiceCheckfirst_Type = Integer32
_UpsDiagnosticGlobalServiceCheckfirst_Object = MibScalar
upsDiagnosticGlobalServiceCheckfirst = _UpsDiagnosticGlobalServiceCheckfirst_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 12, 7),
    _UpsDiagnosticGlobalServiceCheckfirst_Type()
)
upsDiagnosticGlobalServiceCheckfirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheckfirst.setStatus("current")
_GeSecondUPS_ObjectIdentity = ObjectIdentity
geSecondUPS = _GeSecondUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12)
)
_UpsIdentsecond_ObjectIdentity = ObjectIdentity
upsIdentsecond = _UpsIdentsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1)
)
_UpsIdentManufacturersecond_Type = DisplayString
_UpsIdentManufacturersecond_Object = MibScalar
upsIdentManufacturersecond = _UpsIdentManufacturersecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 1),
    _UpsIdentManufacturersecond_Type()
)
upsIdentManufacturersecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturersecond.setStatus("current")
_UpsIdentModelsecond_Type = DisplayString
_UpsIdentModelsecond_Object = MibScalar
upsIdentModelsecond = _UpsIdentModelsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 2),
    _UpsIdentModelsecond_Type()
)
upsIdentModelsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelsecond.setStatus("current")
_UpsIdentUPSSoftwareVersionsecond_Type = DisplayString
_UpsIdentUPSSoftwareVersionsecond_Object = MibScalar
upsIdentUPSSoftwareVersionsecond = _UpsIdentUPSSoftwareVersionsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 3),
    _UpsIdentUPSSoftwareVersionsecond_Type()
)
upsIdentUPSSoftwareVersionsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersionsecond.setStatus("current")
_UpsIdentAgentSoftwareVersionsecond_Type = DisplayString
_UpsIdentAgentSoftwareVersionsecond_Object = MibScalar
upsIdentAgentSoftwareVersionsecond = _UpsIdentAgentSoftwareVersionsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 4),
    _UpsIdentAgentSoftwareVersionsecond_Type()
)
upsIdentAgentSoftwareVersionsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersionsecond.setStatus("current")
_UpsIdentNamesecond_Type = DisplayString
_UpsIdentNamesecond_Object = MibScalar
upsIdentNamesecond = _UpsIdentNamesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 5),
    _UpsIdentNamesecond_Type()
)
upsIdentNamesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNamesecond.setStatus("current")
_UpsIdentAttachedDevicessecond_Type = DisplayString
_UpsIdentAttachedDevicessecond_Object = MibScalar
upsIdentAttachedDevicessecond = _UpsIdentAttachedDevicessecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 6),
    _UpsIdentAttachedDevicessecond_Type()
)
upsIdentAttachedDevicessecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicessecond.setStatus("current")
_UpsIdentUPSSerialNumbersecond_Type = DisplayString
_UpsIdentUPSSerialNumbersecond_Object = MibScalar
upsIdentUPSSerialNumbersecond = _UpsIdentUPSSerialNumbersecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 7),
    _UpsIdentUPSSerialNumbersecond_Type()
)
upsIdentUPSSerialNumbersecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumbersecond.setStatus("current")
_UpsIdentComProtVersionsecond_Type = DisplayString
_UpsIdentComProtVersionsecond_Object = MibScalar
upsIdentComProtVersionsecond = _UpsIdentComProtVersionsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 8),
    _UpsIdentComProtVersionsecond_Type()
)
upsIdentComProtVersionsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersionsecond.setStatus("current")
_UpsIdentOperatingTimesecond_Type = NonNegativeInteger32
_UpsIdentOperatingTimesecond_Object = MibScalar
upsIdentOperatingTimesecond = _UpsIdentOperatingTimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 1, 9),
    _UpsIdentOperatingTimesecond_Type()
)
upsIdentOperatingTimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimesecond.setUnits("seconds")
_UpsBatterysecond_ObjectIdentity = ObjectIdentity
upsBatterysecond = _UpsBatterysecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2)
)


class _UpsBatteryStatussecond_Type(Integer32):
    """Custom type upsBatteryStatussecond based on Integer32"""
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


_UpsBatteryStatussecond_Type.__name__ = "Integer32"
_UpsBatteryStatussecond_Object = MibScalar
upsBatteryStatussecond = _UpsBatteryStatussecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 1),
    _UpsBatteryStatussecond_Type()
)
upsBatteryStatussecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatussecond.setStatus("current")
_UpsSecondsOnBatterysecond_Type = Integer32
_UpsSecondsOnBatterysecond_Object = MibScalar
upsSecondsOnBatterysecond = _UpsSecondsOnBatterysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 2),
    _UpsSecondsOnBatterysecond_Type()
)
upsSecondsOnBatterysecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatterysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatterysecond.setUnits("seconds")
_UpsEstimatedMinutesRemainingsecond_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingsecond_Object = MibScalar
upsEstimatedMinutesRemainingsecond = _UpsEstimatedMinutesRemainingsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 3),
    _UpsEstimatedMinutesRemainingsecond_Type()
)
upsEstimatedMinutesRemainingsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingsecond.setUnits("minutes")


class _UpsEstimatedChargeRemainingsecond_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingsecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingsecond_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingsecond_Object = MibScalar
upsEstimatedChargeRemainingsecond = _UpsEstimatedChargeRemainingsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 4),
    _UpsEstimatedChargeRemainingsecond_Type()
)
upsEstimatedChargeRemainingsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingsecond.setUnits("percent")
_UpsBatteryVoltagesecond_Type = NonNegativeInteger32
_UpsBatteryVoltagesecond_Object = MibScalar
upsBatteryVoltagesecond = _UpsBatteryVoltagesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 5),
    _UpsBatteryVoltagesecond_Type()
)
upsBatteryVoltagesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltagesecond.setUnits("0.1 Volt DC")
_UpsBatteryCurrentsecond_Type = Integer32
_UpsBatteryCurrentsecond_Object = MibScalar
upsBatteryCurrentsecond = _UpsBatteryCurrentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 6),
    _UpsBatteryCurrentsecond_Type()
)
upsBatteryCurrentsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentsecond.setUnits("0.1 Amp DC")
_UpsBatteryTemperaturesecond_Type = Integer32
_UpsBatteryTemperaturesecond_Object = MibScalar
upsBatteryTemperaturesecond = _UpsBatteryTemperaturesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 7),
    _UpsBatteryTemperaturesecond_Type()
)
upsBatteryTemperaturesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperaturesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperaturesecond.setUnits("degrees Centigrade")
_UpsBatteryRipplesecond_Type = Integer32
_UpsBatteryRipplesecond_Object = MibScalar
upsBatteryRipplesecond = _UpsBatteryRipplesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 2, 8),
    _UpsBatteryRipplesecond_Type()
)
upsBatteryRipplesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipplesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipplesecond.setUnits("0.1 Volt RMS")
_UpsInputsecond_ObjectIdentity = ObjectIdentity
upsInputsecond = _UpsInputsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3)
)
_UpsInputLineBadssecond_Type = Counter32
_UpsInputLineBadssecond_Object = MibScalar
upsInputLineBadssecond = _UpsInputLineBadssecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 1),
    _UpsInputLineBadssecond_Type()
)
upsInputLineBadssecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadssecond.setStatus("current")
_UpsInputNumLinessecond_Type = NonNegativeInteger32
_UpsInputNumLinessecond_Object = MibScalar
upsInputNumLinessecond = _UpsInputNumLinessecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 2),
    _UpsInputNumLinessecond_Type()
)
upsInputNumLinessecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinessecond.setStatus("current")
_UpsInputSecondTable_Object = MibTable
upsInputSecondTable = _UpsInputSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputSecondTable.setStatus("current")
_UpsInputSecondEntry_Object = MibTableRow
upsInputSecondEntry = _UpsInputSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1)
)
upsInputSecondEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexsecond"),
)
if mibBuilder.loadTexts:
    upsInputSecondEntry.setStatus("current")
_UpsInputLineIndexsecond_Type = PositiveInteger32
_UpsInputLineIndexsecond_Object = MibTableColumn
upsInputLineIndexsecond = _UpsInputLineIndexsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1, 1),
    _UpsInputLineIndexsecond_Type()
)
upsInputLineIndexsecond.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexsecond.setStatus("current")
_UpsInputFrequencysecond_Type = NonNegativeInteger32
_UpsInputFrequencysecond_Object = MibTableColumn
upsInputFrequencysecond = _UpsInputFrequencysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1, 2),
    _UpsInputFrequencysecond_Type()
)
upsInputFrequencysecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencysecond.setUnits("0.1 Hertz")
_UpsInputVoltagesecond_Type = NonNegativeInteger32
_UpsInputVoltagesecond_Object = MibTableColumn
upsInputVoltagesecond = _UpsInputVoltagesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1, 3),
    _UpsInputVoltagesecond_Type()
)
upsInputVoltagesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltagesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltagesecond.setUnits("RMS Volts")
_UpsInputCurrentsecond_Type = NonNegativeInteger32
_UpsInputCurrentsecond_Object = MibTableColumn
upsInputCurrentsecond = _UpsInputCurrentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1, 4),
    _UpsInputCurrentsecond_Type()
)
upsInputCurrentsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentsecond.setUnits("0.1 RMS Amp")
_UpsInputTruePowersecond_Type = NonNegativeInteger32
_UpsInputTruePowersecond_Object = MibTableColumn
upsInputTruePowersecond = _UpsInputTruePowersecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1, 5),
    _UpsInputTruePowersecond_Type()
)
upsInputTruePowersecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowersecond.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowersecond.setUnits("Watts")
_UpsInputVoltageMinsecond_Type = NonNegativeInteger32
_UpsInputVoltageMinsecond_Object = MibTableColumn
upsInputVoltageMinsecond = _UpsInputVoltageMinsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1, 6),
    _UpsInputVoltageMinsecond_Type()
)
upsInputVoltageMinsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMinsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMinsecond.setUnits("RMS Volts")
_UpsInputVoltageMaxsecond_Type = NonNegativeInteger32
_UpsInputVoltageMaxsecond_Object = MibTableColumn
upsInputVoltageMaxsecond = _UpsInputVoltageMaxsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 3, 3, 1, 7),
    _UpsInputVoltageMaxsecond_Type()
)
upsInputVoltageMaxsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxsecond.setUnits("RMS Volts")
_UpsOutputsecond_ObjectIdentity = ObjectIdentity
upsOutputsecond = _UpsOutputsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4)
)


class _UpsOutputSourcesecond_Type(Integer32):
    """Custom type upsOutputSourcesecond based on Integer32"""
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


_UpsOutputSourcesecond_Type.__name__ = "Integer32"
_UpsOutputSourcesecond_Object = MibScalar
upsOutputSourcesecond = _UpsOutputSourcesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 1),
    _UpsOutputSourcesecond_Type()
)
upsOutputSourcesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourcesecond.setStatus("current")
_UpsOutputFrequencysecond_Type = NonNegativeInteger32
_UpsOutputFrequencysecond_Object = MibScalar
upsOutputFrequencysecond = _UpsOutputFrequencysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 2),
    _UpsOutputFrequencysecond_Type()
)
upsOutputFrequencysecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencysecond.setUnits("0.1 Hertz")
_UpsOutputNumLinessecond_Type = NonNegativeInteger32
_UpsOutputNumLinessecond_Object = MibScalar
upsOutputNumLinessecond = _UpsOutputNumLinessecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 3),
    _UpsOutputNumLinessecond_Type()
)
upsOutputNumLinessecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinessecond.setStatus("current")
_UpsOutputSecondTable_Object = MibTable
upsOutputSecondTable = _UpsOutputSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputSecondTable.setStatus("current")
_UpsOutputSecondEntry_Object = MibTableRow
upsOutputSecondEntry = _UpsOutputSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1)
)
upsOutputSecondEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexsecond"),
)
if mibBuilder.loadTexts:
    upsOutputSecondEntry.setStatus("current")
_UpsOutputLineIndexsecond_Type = PositiveInteger32
_UpsOutputLineIndexsecond_Object = MibTableColumn
upsOutputLineIndexsecond = _UpsOutputLineIndexsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 1),
    _UpsOutputLineIndexsecond_Type()
)
upsOutputLineIndexsecond.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexsecond.setStatus("current")
_UpsOutputVoltagesecond_Type = NonNegativeInteger32
_UpsOutputVoltagesecond_Object = MibTableColumn
upsOutputVoltagesecond = _UpsOutputVoltagesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 2),
    _UpsOutputVoltagesecond_Type()
)
upsOutputVoltagesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltagesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltagesecond.setUnits("RMS Volts")
_UpsOutputCurrentsecond_Type = NonNegativeInteger32
_UpsOutputCurrentsecond_Object = MibTableColumn
upsOutputCurrentsecond = _UpsOutputCurrentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 3),
    _UpsOutputCurrentsecond_Type()
)
upsOutputCurrentsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentsecond.setUnits("0.1 RMS Amp")
_UpsOutputPowersecond_Type = NonNegativeInteger32
_UpsOutputPowersecond_Object = MibTableColumn
upsOutputPowersecond = _UpsOutputPowersecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 4),
    _UpsOutputPowersecond_Type()
)
upsOutputPowersecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowersecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowersecond.setUnits("Watts")


class _UpsOutputPercentLoadsecond_Type(Integer32):
    """Custom type upsOutputPercentLoadsecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadsecond_Type.__name__ = "Integer32"
_UpsOutputPercentLoadsecond_Object = MibTableColumn
upsOutputPercentLoadsecond = _UpsOutputPercentLoadsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 5),
    _UpsOutputPercentLoadsecond_Type()
)
upsOutputPercentLoadsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadsecond.setUnits("percent")


class _UpsOutputPowerFactorsecond_Type(Integer32):
    """Custom type upsOutputPowerFactorsecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorsecond_Type.__name__ = "Integer32"
_UpsOutputPowerFactorsecond_Object = MibTableColumn
upsOutputPowerFactorsecond = _UpsOutputPowerFactorsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 6),
    _UpsOutputPowerFactorsecond_Type()
)
upsOutputPowerFactorsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorsecond.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentsecond_Type = Integer32
_UpsOutputPeakCurrentsecond_Object = MibTableColumn
upsOutputPeakCurrentsecond = _UpsOutputPeakCurrentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 7),
    _UpsOutputPeakCurrentsecond_Type()
)
upsOutputPeakCurrentsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentsecond.setUnits("Amps")
_UpsOutputShareCurrentsecond_Type = Integer32
_UpsOutputShareCurrentsecond_Object = MibTableColumn
upsOutputShareCurrentsecond = _UpsOutputShareCurrentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 4, 4, 1, 8),
    _UpsOutputShareCurrentsecond_Type()
)
upsOutputShareCurrentsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentsecond.setUnits("Amps")
_UpsBypasssecond_ObjectIdentity = ObjectIdentity
upsBypasssecond = _UpsBypasssecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5)
)
_UpsBypassFrequencysecond_Type = NonNegativeInteger32
_UpsBypassFrequencysecond_Object = MibScalar
upsBypassFrequencysecond = _UpsBypassFrequencysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 1),
    _UpsBypassFrequencysecond_Type()
)
upsBypassFrequencysecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencysecond.setUnits("0.1 Hertz")
_UpsBypassNumLinessecond_Type = NonNegativeInteger32
_UpsBypassNumLinessecond_Object = MibScalar
upsBypassNumLinessecond = _UpsBypassNumLinessecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 2),
    _UpsBypassNumLinessecond_Type()
)
upsBypassNumLinessecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinessecond.setStatus("current")
_UpsBypassSecondTable_Object = MibTable
upsBypassSecondTable = _UpsBypassSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassSecondTable.setStatus("current")
_UpsBypassSecondEntry_Object = MibTableRow
upsBypassSecondEntry = _UpsBypassSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 3, 1)
)
upsBypassSecondEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexsecond"),
)
if mibBuilder.loadTexts:
    upsBypassSecondEntry.setStatus("current")
_UpsBypassLineIndexsecond_Type = PositiveInteger32
_UpsBypassLineIndexsecond_Object = MibTableColumn
upsBypassLineIndexsecond = _UpsBypassLineIndexsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 3, 1, 1),
    _UpsBypassLineIndexsecond_Type()
)
upsBypassLineIndexsecond.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexsecond.setStatus("current")
_UpsBypassVoltagesecond_Type = NonNegativeInteger32
_UpsBypassVoltagesecond_Object = MibTableColumn
upsBypassVoltagesecond = _UpsBypassVoltagesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 3, 1, 2),
    _UpsBypassVoltagesecond_Type()
)
upsBypassVoltagesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltagesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltagesecond.setUnits("RMS Volts")
_UpsBypassCurrentsecond_Type = NonNegativeInteger32
_UpsBypassCurrentsecond_Object = MibTableColumn
upsBypassCurrentsecond = _UpsBypassCurrentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 3, 1, 3),
    _UpsBypassCurrentsecond_Type()
)
upsBypassCurrentsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentsecond.setUnits("0.1 RMS Amp")
_UpsBypassPowersecond_Type = NonNegativeInteger32
_UpsBypassPowersecond_Object = MibTableColumn
upsBypassPowersecond = _UpsBypassPowersecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 5, 3, 1, 4),
    _UpsBypassPowersecond_Type()
)
upsBypassPowersecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowersecond.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowersecond.setUnits("Watts")
_UpsAlarmsecond_ObjectIdentity = ObjectIdentity
upsAlarmsecond = _UpsAlarmsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6)
)
_UpsAlarmsPresentsecond_Type = Gauge32
_UpsAlarmsPresentsecond_Object = MibScalar
upsAlarmsPresentsecond = _UpsAlarmsPresentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 1),
    _UpsAlarmsPresentsecond_Type()
)
upsAlarmsPresentsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentsecond.setStatus("current")
_UpsAlarmSecondTable_Object = MibTable
upsAlarmSecondTable = _UpsAlarmSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmSecondTable.setStatus("current")
_UpsAlarmSecondEntry_Object = MibTableRow
upsAlarmSecondEntry = _UpsAlarmSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 2, 1)
)
upsAlarmSecondEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdsecond"),
)
if mibBuilder.loadTexts:
    upsAlarmSecondEntry.setStatus("current")
_UpsAlarmIdsecond_Type = PositiveInteger32
_UpsAlarmIdsecond_Object = MibTableColumn
upsAlarmIdsecond = _UpsAlarmIdsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 2, 1, 1),
    _UpsAlarmIdsecond_Type()
)
upsAlarmIdsecond.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdsecond.setStatus("current")
_UpsAlarmDescrsecond_Type = AutonomousType
_UpsAlarmDescrsecond_Object = MibTableColumn
upsAlarmDescrsecond = _UpsAlarmDescrsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 2, 1, 2),
    _UpsAlarmDescrsecond_Type()
)
upsAlarmDescrsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrsecond.setStatus("current")
_UpsAlarmTimesecond_Type = TimeStamp
_UpsAlarmTimesecond_Object = MibTableColumn
upsAlarmTimesecond = _UpsAlarmTimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 2, 1, 3),
    _UpsAlarmTimesecond_Type()
)
upsAlarmTimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimesecond.setStatus("current")
_UpsWellKnownAlarmssecond_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmssecond = _UpsWellKnownAlarmssecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3)
)
_UpsAlarmBatteryBadsecond_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadsecond = _UpsAlarmBatteryBadsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadsecond.setStatus("current")
_UpsAlarmOnBatterysecond_ObjectIdentity = ObjectIdentity
upsAlarmOnBatterysecond = _UpsAlarmOnBatterysecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatterysecond.setStatus("current")
_UpsAlarmLowBatterysecond_ObjectIdentity = ObjectIdentity
upsAlarmLowBatterysecond = _UpsAlarmLowBatterysecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatterysecond.setStatus("current")
_UpsAlarmDepletedBatterysecond_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatterysecond = _UpsAlarmDepletedBatterysecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatterysecond.setStatus("current")
_UpsAlarmTempBadsecond_ObjectIdentity = ObjectIdentity
upsAlarmTempBadsecond = _UpsAlarmTempBadsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadsecond.setStatus("current")
_UpsAlarmInputBadsecond_ObjectIdentity = ObjectIdentity
upsAlarmInputBadsecond = _UpsAlarmInputBadsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadsecond.setStatus("current")
_UpsAlarmOutputBadsecond_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadsecond = _UpsAlarmOutputBadsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadsecond.setStatus("current")
_UpsAlarmOutputOverloadsecond_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadsecond = _UpsAlarmOutputOverloadsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadsecond.setStatus("current")
_UpsAlarmOnBypasssecond_ObjectIdentity = ObjectIdentity
upsAlarmOnBypasssecond = _UpsAlarmOnBypasssecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypasssecond.setStatus("current")
_UpsAlarmBypassBadsecond_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadsecond = _UpsAlarmBypassBadsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadsecond.setStatus("current")
_UpsAlarmOutputOffAsRequestedsecond_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedsecond = _UpsAlarmOutputOffAsRequestedsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedsecond.setStatus("current")
_UpsAlarmUpsOffAsRequestedsecond_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedsecond = _UpsAlarmUpsOffAsRequestedsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedsecond.setStatus("current")
_UpsAlarmChargerFailedsecond_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedsecond = _UpsAlarmChargerFailedsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedsecond.setStatus("current")
_UpsAlarmUpsOutputOffsecond_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOffsecond = _UpsAlarmUpsOutputOffsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOffsecond.setStatus("current")
_UpsAlarmUpsSystemOffsecond_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOffsecond = _UpsAlarmUpsSystemOffsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOffsecond.setStatus("current")
_UpsAlarmFanFailuresecond_ObjectIdentity = ObjectIdentity
upsAlarmFanFailuresecond = _UpsAlarmFanFailuresecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailuresecond.setStatus("current")
_UpsAlarmFuseFailuresecond_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailuresecond = _UpsAlarmFuseFailuresecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailuresecond.setStatus("current")
_UpsAlarmGeneralFaultsecond_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultsecond = _UpsAlarmGeneralFaultsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultsecond.setStatus("current")
_UpsAlarmDiagnosticTestFailedsecond_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedsecond = _UpsAlarmDiagnosticTestFailedsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedsecond.setStatus("current")
_UpsAlarmCommunicationsLostsecond_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostsecond = _UpsAlarmCommunicationsLostsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostsecond.setStatus("current")
_UpsAlarmAwaitingPowersecond_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowersecond = _UpsAlarmAwaitingPowersecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowersecond.setStatus("current")
_UpsAlarmShutdownPendingsecond_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingsecond = _UpsAlarmShutdownPendingsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingsecond.setStatus("current")
_UpsAlarmShutdownImminentsecond_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentsecond = _UpsAlarmShutdownImminentsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentsecond.setStatus("current")
_UpsAlarmTestInProgresssecond_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgresssecond = _UpsAlarmTestInProgresssecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgresssecond.setStatus("current")
_UpsAlarmReceptacleOffsecond_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOffsecond = _UpsAlarmReceptacleOffsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOffsecond.setStatus("current")
_UpsAlarmHighSpeedBusFailuresecond_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailuresecond = _UpsAlarmHighSpeedBusFailuresecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailuresecond.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailuresecond_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailuresecond = _UpsAlarmHighSpeedBusJACRCFailuresecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailuresecond.setStatus("current")
_UpsAlarmConnectivityBusFailuresecond_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailuresecond = _UpsAlarmConnectivityBusFailuresecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailuresecond.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailuresecond_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailuresecond = _UpsAlarmHighSpeedBusJBCRCFailuresecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailuresecond.setStatus("current")
_UpsAlarmCurrentSharingsecond_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingsecond = _UpsAlarmCurrentSharingsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingsecond.setStatus("current")
_UpsAlarmDCRipplesecond_ObjectIdentity = ObjectIdentity
upsAlarmDCRipplesecond = _UpsAlarmDCRipplesecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipplesecond.setStatus("current")
_UpsAlarmMaskAsecond_Type = Unsigned32
_UpsAlarmMaskAsecond_Object = MibScalar
upsAlarmMaskAsecond = _UpsAlarmMaskAsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 6, 4),
    _UpsAlarmMaskAsecond_Type()
)
upsAlarmMaskAsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAsecond.setStatus("current")
_UpsTestsecond_ObjectIdentity = ObjectIdentity
upsTestsecond = _UpsTestsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7)
)
_UpsTestIdsecond_Type = ObjectIdentifier
_UpsTestIdsecond_Object = MibScalar
upsTestIdsecond = _UpsTestIdsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 1),
    _UpsTestIdsecond_Type()
)
upsTestIdsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdsecond.setStatus("current")
_UpsTestSpinLocksecond_Type = TestAndIncr
_UpsTestSpinLocksecond_Object = MibScalar
upsTestSpinLocksecond = _UpsTestSpinLocksecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 2),
    _UpsTestSpinLocksecond_Type()
)
upsTestSpinLocksecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLocksecond.setStatus("current")


class _UpsTestResultsSummarysecond_Type(Integer32):
    """Custom type upsTestResultsSummarysecond based on Integer32"""
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


_UpsTestResultsSummarysecond_Type.__name__ = "Integer32"
_UpsTestResultsSummarysecond_Object = MibScalar
upsTestResultsSummarysecond = _UpsTestResultsSummarysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 3),
    _UpsTestResultsSummarysecond_Type()
)
upsTestResultsSummarysecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummarysecond.setStatus("current")
_UpsTestResultsDetailsecond_Type = DisplayString
_UpsTestResultsDetailsecond_Object = MibScalar
upsTestResultsDetailsecond = _UpsTestResultsDetailsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 4),
    _UpsTestResultsDetailsecond_Type()
)
upsTestResultsDetailsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailsecond.setStatus("current")
_UpsTestStartTimesecond_Type = TimeStamp
_UpsTestStartTimesecond_Object = MibScalar
upsTestStartTimesecond = _UpsTestStartTimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 5),
    _UpsTestStartTimesecond_Type()
)
upsTestStartTimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimesecond.setStatus("current")
_UpsTestElapsedTimesecond_Type = TimeInterval
_UpsTestElapsedTimesecond_Object = MibScalar
upsTestElapsedTimesecond = _UpsTestElapsedTimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 6),
    _UpsTestElapsedTimesecond_Type()
)
upsTestElapsedTimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimesecond.setStatus("current")
_UpsWellKnownTestssecond_ObjectIdentity = ObjectIdentity
upsWellKnownTestssecond = _UpsWellKnownTestssecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 7)
)
_UpsTestNoTestsInitiatedsecond_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedsecond = _UpsTestNoTestsInitiatedsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedsecond.setStatus("current")
_UpsTestAbortTestInProgresssecond_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgresssecond = _UpsTestAbortTestInProgresssecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgresssecond.setStatus("current")
_UpsTestGeneralSystemsTestsecond_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestsecond = _UpsTestGeneralSystemsTestsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestsecond.setStatus("current")
_UpsTestQuickBatteryTestsecond_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestsecond = _UpsTestQuickBatteryTestsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestsecond.setStatus("current")
_UpsTestDeepBatteryCalibrationsecond_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationsecond = _UpsTestDeepBatteryCalibrationsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationsecond.setStatus("current")
_UpsControlsecond_ObjectIdentity = ObjectIdentity
upsControlsecond = _UpsControlsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8)
)


class _UpsShutdownTypesecond_Type(Integer32):
    """Custom type upsShutdownTypesecond based on Integer32"""
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


_UpsShutdownTypesecond_Type.__name__ = "Integer32"
_UpsShutdownTypesecond_Object = MibScalar
upsShutdownTypesecond = _UpsShutdownTypesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 1),
    _UpsShutdownTypesecond_Type()
)
upsShutdownTypesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypesecond.setStatus("current")


class _UpsShutdownAfterDelaysecond_Type(Integer32):
    """Custom type upsShutdownAfterDelaysecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelaysecond_Type.__name__ = "Integer32"
_UpsShutdownAfterDelaysecond_Object = MibScalar
upsShutdownAfterDelaysecond = _UpsShutdownAfterDelaysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 2),
    _UpsShutdownAfterDelaysecond_Type()
)
upsShutdownAfterDelaysecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaysecond.setUnits("seconds")


class _UpsStartupAfterDelaysecond_Type(Integer32):
    """Custom type upsStartupAfterDelaysecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelaysecond_Type.__name__ = "Integer32"
_UpsStartupAfterDelaysecond_Object = MibScalar
upsStartupAfterDelaysecond = _UpsStartupAfterDelaysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 3),
    _UpsStartupAfterDelaysecond_Type()
)
upsStartupAfterDelaysecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelaysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelaysecond.setUnits("seconds")


class _UpsRebootWithDurationsecond_Type(Integer32):
    """Custom type upsRebootWithDurationsecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationsecond_Type.__name__ = "Integer32"
_UpsRebootWithDurationsecond_Object = MibScalar
upsRebootWithDurationsecond = _UpsRebootWithDurationsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 4),
    _UpsRebootWithDurationsecond_Type()
)
upsRebootWithDurationsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationsecond.setUnits("seconds")


class _UpsAutoRestartsecond_Type(Integer32):
    """Custom type upsAutoRestartsecond based on Integer32"""
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


_UpsAutoRestartsecond_Type.__name__ = "Integer32"
_UpsAutoRestartsecond_Object = MibScalar
upsAutoRestartsecond = _UpsAutoRestartsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 5),
    _UpsAutoRestartsecond_Type()
)
upsAutoRestartsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartsecond.setStatus("current")
_UpsReceptaclesNumsecond_Type = NonNegativeInteger32
_UpsReceptaclesNumsecond_Object = MibScalar
upsReceptaclesNumsecond = _UpsReceptaclesNumsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 6),
    _UpsReceptaclesNumsecond_Type()
)
upsReceptaclesNumsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumsecond.setStatus("current")
_UpsReceptacleSecondTable_Object = MibTable
upsReceptacleSecondTable = _UpsReceptacleSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleSecondTable.setStatus("current")
_UpsReceptacleSecondEntry_Object = MibTableRow
upsReceptacleSecondEntry = _UpsReceptacleSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 7, 1)
)
upsReceptacleSecondEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexsecond"),
)
if mibBuilder.loadTexts:
    upsReceptacleSecondEntry.setStatus("current")
_UpsReceptacleLineIndexsecond_Type = PositiveInteger32
_UpsReceptacleLineIndexsecond_Object = MibTableColumn
upsReceptacleLineIndexsecond = _UpsReceptacleLineIndexsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 7, 1, 1),
    _UpsReceptacleLineIndexsecond_Type()
)
upsReceptacleLineIndexsecond.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexsecond.setStatus("current")


class _UpsReceptacleOnOffsecond_Type(Integer32):
    """Custom type upsReceptacleOnOffsecond based on Integer32"""
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


_UpsReceptacleOnOffsecond_Type.__name__ = "Integer32"
_UpsReceptacleOnOffsecond_Object = MibTableColumn
upsReceptacleOnOffsecond = _UpsReceptacleOnOffsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 7, 1, 2),
    _UpsReceptacleOnOffsecond_Type()
)
upsReceptacleOnOffsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOffsecond.setStatus("current")


class _UpsUPSModesecond_Type(Integer32):
    """Custom type upsUPSModesecond based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModesecond_Type.__name__ = "Integer32"
_UpsUPSModesecond_Object = MibScalar
upsUPSModesecond = _UpsUPSModesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 8),
    _UpsUPSModesecond_Type()
)
upsUPSModesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModesecond.setStatus("current")


class _UpsRectifierOnOffsecond_Type(Integer32):
    """Custom type upsRectifierOnOffsecond based on Integer32"""
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


_UpsRectifierOnOffsecond_Type.__name__ = "Integer32"
_UpsRectifierOnOffsecond_Object = MibScalar
upsRectifierOnOffsecond = _UpsRectifierOnOffsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 9),
    _UpsRectifierOnOffsecond_Type()
)
upsRectifierOnOffsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOffsecond.setStatus("current")


class _UpsBatteryChargeMethodsecond_Type(Integer32):
    """Custom type upsBatteryChargeMethodsecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodsecond_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodsecond_Object = MibScalar
upsBatteryChargeMethodsecond = _UpsBatteryChargeMethodsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 10),
    _UpsBatteryChargeMethodsecond_Type()
)
upsBatteryChargeMethodsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodsecond.setStatus("current")


class _UpsInverterOnOffsecond_Type(Integer32):
    """Custom type upsInverterOnOffsecond based on Integer32"""
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


_UpsInverterOnOffsecond_Type.__name__ = "Integer32"
_UpsInverterOnOffsecond_Object = MibScalar
upsInverterOnOffsecond = _UpsInverterOnOffsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 11),
    _UpsInverterOnOffsecond_Type()
)
upsInverterOnOffsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOffsecond.setStatus("current")


class _UpsBypassOnOffsecond_Type(Integer32):
    """Custom type upsBypassOnOffsecond based on Integer32"""
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


_UpsBypassOnOffsecond_Type.__name__ = "Integer32"
_UpsBypassOnOffsecond_Object = MibScalar
upsBypassOnOffsecond = _UpsBypassOnOffsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 12),
    _UpsBypassOnOffsecond_Type()
)
upsBypassOnOffsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOffsecond.setStatus("current")


class _UpsLoadSourcesecond_Type(Integer32):
    """Custom type upsLoadSourcesecond based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourcesecond_Type.__name__ = "Integer32"
_UpsLoadSourcesecond_Object = MibScalar
upsLoadSourcesecond = _UpsLoadSourcesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 8, 13),
    _UpsLoadSourcesecond_Type()
)
upsLoadSourcesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourcesecond.setStatus("current")
_UpsConfigsecond_ObjectIdentity = ObjectIdentity
upsConfigsecond = _UpsConfigsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9)
)
_UpsConfigInputVoltagesecond_Type = NonNegativeInteger32
_UpsConfigInputVoltagesecond_Object = MibScalar
upsConfigInputVoltagesecond = _UpsConfigInputVoltagesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 1),
    _UpsConfigInputVoltagesecond_Type()
)
upsConfigInputVoltagesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltagesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltagesecond.setUnits("RMS Volts")
_UpsConfigInputFreqsecond_Type = NonNegativeInteger32
_UpsConfigInputFreqsecond_Object = MibScalar
upsConfigInputFreqsecond = _UpsConfigInputFreqsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 2),
    _UpsConfigInputFreqsecond_Type()
)
upsConfigInputFreqsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqsecond.setUnits("0.1 Hertz")
_UpsConfigOutputVoltagesecond_Type = NonNegativeInteger32
_UpsConfigOutputVoltagesecond_Object = MibScalar
upsConfigOutputVoltagesecond = _UpsConfigOutputVoltagesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 3),
    _UpsConfigOutputVoltagesecond_Type()
)
upsConfigOutputVoltagesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagesecond.setUnits("RMS Volts")
_UpsConfigOutputFreqsecond_Type = NonNegativeInteger32
_UpsConfigOutputFreqsecond_Object = MibScalar
upsConfigOutputFreqsecond = _UpsConfigOutputFreqsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 4),
    _UpsConfigOutputFreqsecond_Type()
)
upsConfigOutputFreqsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqsecond.setUnits("0.1 Hertz")
_UpsConfigOutputVAsecond_Type = NonNegativeInteger32
_UpsConfigOutputVAsecond_Object = MibScalar
upsConfigOutputVAsecond = _UpsConfigOutputVAsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 5),
    _UpsConfigOutputVAsecond_Type()
)
upsConfigOutputVAsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAsecond.setUnits("Volt-Amps")
_UpsConfigOutputPowersecond_Type = NonNegativeInteger32
_UpsConfigOutputPowersecond_Object = MibScalar
upsConfigOutputPowersecond = _UpsConfigOutputPowersecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 6),
    _UpsConfigOutputPowersecond_Type()
)
upsConfigOutputPowersecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowersecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowersecond.setUnits("Watts")
_UpsConfigLowBattTimesecond_Type = NonNegativeInteger32
_UpsConfigLowBattTimesecond_Object = MibScalar
upsConfigLowBattTimesecond = _UpsConfigLowBattTimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 7),
    _UpsConfigLowBattTimesecond_Type()
)
upsConfigLowBattTimesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimesecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimesecond.setUnits("minutes")


class _UpsConfigAudibleStatussecond_Type(Integer32):
    """Custom type upsConfigAudibleStatussecond based on Integer32"""
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


_UpsConfigAudibleStatussecond_Type.__name__ = "Integer32"
_UpsConfigAudibleStatussecond_Object = MibScalar
upsConfigAudibleStatussecond = _UpsConfigAudibleStatussecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 8),
    _UpsConfigAudibleStatussecond_Type()
)
upsConfigAudibleStatussecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatussecond.setStatus("current")
_UpsConfigLowVoltageTransferPointsecond_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointsecond_Object = MibScalar
upsConfigLowVoltageTransferPointsecond = _UpsConfigLowVoltageTransferPointsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 9),
    _UpsConfigLowVoltageTransferPointsecond_Type()
)
upsConfigLowVoltageTransferPointsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointsecond.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointsecond_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointsecond_Object = MibScalar
upsConfigHighVoltageTransferPointsecond = _UpsConfigHighVoltageTransferPointsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 10),
    _UpsConfigHighVoltageTransferPointsecond_Type()
)
upsConfigHighVoltageTransferPointsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointsecond.setUnits("RMS Volts")
_UpsConfigBatteryCapacitysecond_Type = NonNegativeInteger32
_UpsConfigBatteryCapacitysecond_Object = MibScalar
upsConfigBatteryCapacitysecond = _UpsConfigBatteryCapacitysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 11),
    _UpsConfigBatteryCapacitysecond_Type()
)
upsConfigBatteryCapacitysecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitysecond.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentsecond_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentsecond_Object = MibScalar
upsConfigBatteryChargeCurrentsecond = _UpsConfigBatteryChargeCurrentsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 12),
    _UpsConfigBatteryChargeCurrentsecond_Type()
)
upsConfigBatteryChargeCurrentsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentsecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentsecond.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdownsecond_Type(Integer32):
    """Custom type upsConfigNoLoadShutdownsecond based on Integer32"""
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


_UpsConfigNoLoadShutdownsecond_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdownsecond_Object = MibScalar
upsConfigNoLoadShutdownsecond = _UpsConfigNoLoadShutdownsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 13),
    _UpsConfigNoLoadShutdownsecond_Type()
)
upsConfigNoLoadShutdownsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdownsecond.setStatus("current")
_UpsConfigStartDelaysecond_Type = PositiveInteger32
_UpsConfigStartDelaysecond_Object = MibScalar
upsConfigStartDelaysecond = _UpsConfigStartDelaysecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 9, 14),
    _UpsConfigStartDelaysecond_Type()
)
upsConfigStartDelaysecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelaysecond.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelaysecond.setUnits("minutes")
_UpsGetSetsecond_ObjectIdentity = ObjectIdentity
upsGetSetsecond = _UpsGetSetsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10)
)
_UpsEventGetNextsecond_Type = PositiveInteger32
_UpsEventGetNextsecond_Object = MibScalar
upsEventGetNextsecond = _UpsEventGetNextsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 1),
    _UpsEventGetNextsecond_Type()
)
upsEventGetNextsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextsecond.setStatus("current")
_UpsEventGetPrevioussecond_Type = PositiveInteger32
_UpsEventGetPrevioussecond_Object = MibScalar
upsEventGetPrevioussecond = _UpsEventGetPrevioussecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 2),
    _UpsEventGetPrevioussecond_Type()
)
upsEventGetPrevioussecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPrevioussecond.setStatus("current")
_UpsEventSetStartingTimeStampsecond_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampsecond_Object = MibScalar
upsEventSetStartingTimeStampsecond = _UpsEventSetStartingTimeStampsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 3),
    _UpsEventSetStartingTimeStampsecond_Type()
)
upsEventSetStartingTimeStampsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampsecond.setStatus("current")
_UpsEventRetreiveCurrentTimeStampsecond_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampsecond_Object = MibScalar
upsEventRetreiveCurrentTimeStampsecond = _UpsEventRetreiveCurrentTimeStampsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 4),
    _UpsEventRetreiveCurrentTimeStampsecond_Type()
)
upsEventRetreiveCurrentTimeStampsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampsecond.setStatus("current")
_UpsEventTableSizesecond_Type = NonNegativeInteger32
_UpsEventTableSizesecond_Object = MibScalar
upsEventTableSizesecond = _UpsEventTableSizesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 5),
    _UpsEventTableSizesecond_Type()
)
upsEventTableSizesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizesecond.setStatus("current")
_UpsEventSecondTable_Object = MibTable
upsEventSecondTable = _UpsEventSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventSecondTable.setStatus("current")
_UpsEventSecondEntry_Object = MibTableRow
upsEventSecondEntry = _UpsEventSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 6, 1)
)
upsEventSecondEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexsecond"),
)
if mibBuilder.loadTexts:
    upsEventSecondEntry.setStatus("current")
_UpsEventLineIndexsecond_Type = PositiveInteger32
_UpsEventLineIndexsecond_Object = MibTableColumn
upsEventLineIndexsecond = _UpsEventLineIndexsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 6, 1, 1),
    _UpsEventLineIndexsecond_Type()
)
upsEventLineIndexsecond.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexsecond.setStatus("current")
_UpsEventCodesecond_Type = Integer32
_UpsEventCodesecond_Object = MibTableColumn
upsEventCodesecond = _UpsEventCodesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 6, 1, 2),
    _UpsEventCodesecond_Type()
)
upsEventCodesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodesecond.setStatus("current")
_UpsEventStatussecond_Type = NonNegativeInteger32
_UpsEventStatussecond_Object = MibTableColumn
upsEventStatussecond = _UpsEventStatussecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 6, 1, 3),
    _UpsEventStatussecond_Type()
)
upsEventStatussecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatussecond.setStatus("current")
_UpsEventTimesecond_Type = NonNegativeInteger32
_UpsEventTimesecond_Object = MibTableColumn
upsEventTimesecond = _UpsEventTimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 6, 1, 4),
    _UpsEventTimesecond_Type()
)
upsEventTimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimesecond.setStatus("current")
_UpsParametersReadsecond_Type = PositiveInteger32
_UpsParametersReadsecond_Object = MibScalar
upsParametersReadsecond = _UpsParametersReadsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 7),
    _UpsParametersReadsecond_Type()
)
upsParametersReadsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadsecond.setStatus("current")
_UpsParametersWritesecond_Type = PositiveInteger32
_UpsParametersWritesecond_Object = MibScalar
upsParametersWritesecond = _UpsParametersWritesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 8),
    _UpsParametersWritesecond_Type()
)
upsParametersWritesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWritesecond.setStatus("current")
_UpsParametersStartAddresssecond_Type = NonNegativeInteger32
_UpsParametersStartAddresssecond_Object = MibScalar
upsParametersStartAddresssecond = _UpsParametersStartAddresssecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 9),
    _UpsParametersStartAddresssecond_Type()
)
upsParametersStartAddresssecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddresssecond.setStatus("current")
_UpsParameterTableSizesecond_Type = NonNegativeInteger32
_UpsParameterTableSizesecond_Object = MibScalar
upsParameterTableSizesecond = _UpsParameterTableSizesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 10),
    _UpsParameterTableSizesecond_Type()
)
upsParameterTableSizesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizesecond.setStatus("current")
_UpsParameterSecondTable_Object = MibTable
upsParameterSecondTable = _UpsParameterSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterSecondTable.setStatus("current")
_UpsParameterSecondEntry_Object = MibTableRow
upsParameterSecondEntry = _UpsParameterSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 11, 1)
)
upsParameterSecondEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexsecond"),
)
if mibBuilder.loadTexts:
    upsParameterSecondEntry.setStatus("current")
_UpsParameterLineIndexsecond_Type = PositiveInteger32
_UpsParameterLineIndexsecond_Object = MibTableColumn
upsParameterLineIndexsecond = _UpsParameterLineIndexsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 11, 1, 1),
    _UpsParameterLineIndexsecond_Type()
)
upsParameterLineIndexsecond.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexsecond.setStatus("current")
_UpsParameterValuesecond_Type = Integer32
_UpsParameterValuesecond_Object = MibTableColumn
upsParameterValuesecond = _UpsParameterValuesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 11, 1, 2),
    _UpsParameterValuesecond_Type()
)
upsParameterValuesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValuesecond.setStatus("current")
_UpsStatussecond_Type = NonNegativeInteger32
_UpsStatussecond_Object = MibScalar
upsStatussecond = _UpsStatussecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 12),
    _UpsStatussecond_Type()
)
upsStatussecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatussecond.setStatus("current")
_UpsMainsStatisticsMBfailsecond_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailsecond_Object = MibScalar
upsMainsStatisticsMBfailsecond = _UpsMainsStatisticsMBfailsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 13),
    _UpsMainsStatisticsMBfailsecond_Type()
)
upsMainsStatisticsMBfailsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailsecond.setStatus("current")
_UpsMainsStatisticsMRfailsecond_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailsecond_Object = MibScalar
upsMainsStatisticsMRfailsecond = _UpsMainsStatisticsMRfailsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 14),
    _UpsMainsStatisticsMRfailsecond_Type()
)
upsMainsStatisticsMRfailsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailsecond.setStatus("current")
_UpsMainsStatisticsB2second_Type = NonNegativeInteger32
_UpsMainsStatisticsB2second_Object = MibScalar
upsMainsStatisticsB2second = _UpsMainsStatisticsB2second_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 15),
    _UpsMainsStatisticsB2second_Type()
)
upsMainsStatisticsB2second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2second.setStatus("current")
_UpsMainsStatisticsB5second_Type = NonNegativeInteger32
_UpsMainsStatisticsB5second_Object = MibScalar
upsMainsStatisticsB5second = _UpsMainsStatisticsB5second_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 16),
    _UpsMainsStatisticsB5second_Type()
)
upsMainsStatisticsB5second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5second.setStatus("current")
_UpsMainsStatisticsB10second_Type = NonNegativeInteger32
_UpsMainsStatisticsB10second_Object = MibScalar
upsMainsStatisticsB10second = _UpsMainsStatisticsB10second_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 17),
    _UpsMainsStatisticsB10second_Type()
)
upsMainsStatisticsB10second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10second.setStatus("current")
_UpsMainsStatisticsB200second_Type = NonNegativeInteger32
_UpsMainsStatisticsB200second_Object = MibScalar
upsMainsStatisticsB200second = _UpsMainsStatisticsB200second_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 18),
    _UpsMainsStatisticsB200second_Type()
)
upsMainsStatisticsB200second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200second.setStatus("current")
_UpsMainsStatisticsBypRelsecond_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelsecond_Object = MibScalar
upsMainsStatisticsBypRelsecond = _UpsMainsStatisticsBypRelsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 19),
    _UpsMainsStatisticsBypRelsecond_Type()
)
upsMainsStatisticsBypRelsecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelsecond.setStatus("current")
_UpsTimesecond_Type = NonNegativeInteger32
_UpsTimesecond_Object = MibScalar
upsTimesecond = _UpsTimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 20),
    _UpsTimesecond_Type()
)
upsTimesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimesecond.setStatus("current")
_UpsRequestPermissionsecond_Type = DisplayString
_UpsRequestPermissionsecond_Object = MibScalar
upsRequestPermissionsecond = _UpsRequestPermissionsecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 21),
    _UpsRequestPermissionsecond_Type()
)
upsRequestPermissionsecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissionsecond.setStatus("current")
_UpsEventGetCodesecond_Type = Integer32
_UpsEventGetCodesecond_Object = MibScalar
upsEventGetCodesecond = _UpsEventGetCodesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 22),
    _UpsEventGetCodesecond_Type()
)
upsEventGetCodesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodesecond.setStatus("current")
_UpsEventSpinLocksecond_Type = TestAndIncr
_UpsEventSpinLocksecond_Object = MibScalar
upsEventSpinLocksecond = _UpsEventSpinLocksecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 23),
    _UpsEventSpinLocksecond_Type()
)
upsEventSpinLocksecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLocksecond.setStatus("current")
_UpsParameterSpinLocksecond_Type = TestAndIncr
_UpsParameterSpinLocksecond_Object = MibScalar
upsParameterSpinLocksecond = _UpsParameterSpinLocksecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 10, 24),
    _UpsParameterSpinLocksecond_Type()
)
upsParameterSpinLocksecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLocksecond.setStatus("current")
_GeUPSTrapssecond_ObjectIdentity = ObjectIdentity
geUPSTrapssecond = _GeUPSTrapssecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11)
)
_UpsDiagnosticsecond_ObjectIdentity = ObjectIdentity
upsDiagnosticsecond = _UpsDiagnosticsecond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12)
)
_UpsDiagnosticBusJACommunicationStatussecond_Type = Integer32
_UpsDiagnosticBusJACommunicationStatussecond_Object = MibScalar
upsDiagnosticBusJACommunicationStatussecond = _UpsDiagnosticBusJACommunicationStatussecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12, 1),
    _UpsDiagnosticBusJACommunicationStatussecond_Type()
)
upsDiagnosticBusJACommunicationStatussecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatussecond.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatussecond_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatussecond_Object = MibScalar
upsDiagnosticBusJBCommunicationStatussecond = _UpsDiagnosticBusJBCommunicationStatussecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatussecond_Type()
)
upsDiagnosticBusJBCommunicationStatussecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatussecond.setStatus("current")
_UpsDiagnosticBatteryLifetimesecond_Type = Integer32
_UpsDiagnosticBatteryLifetimesecond_Object = MibScalar
upsDiagnosticBatteryLifetimesecond = _UpsDiagnosticBatteryLifetimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12, 3),
    _UpsDiagnosticBatteryLifetimesecond_Type()
)
upsDiagnosticBatteryLifetimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimesecond.setStatus("current")
_UpsDiagnosticFansLifetimesecond_Type = Integer32
_UpsDiagnosticFansLifetimesecond_Object = MibScalar
upsDiagnosticFansLifetimesecond = _UpsDiagnosticFansLifetimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12, 4),
    _UpsDiagnosticFansLifetimesecond_Type()
)
upsDiagnosticFansLifetimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimesecond.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimesecond_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimesecond_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimesecond = _UpsDiagnosticDCcapacitorsLifetimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimesecond_Type()
)
upsDiagnosticDCcapacitorsLifetimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimesecond.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimesecond_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimesecond_Object = MibScalar
upsDiagnosticACcapacitorsLifetimesecond = _UpsDiagnosticACcapacitorsLifetimesecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimesecond_Type()
)
upsDiagnosticACcapacitorsLifetimesecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimesecond.setStatus("current")
_UpsDiagnosticGlobalServiceChecksecond_Type = Integer32
_UpsDiagnosticGlobalServiceChecksecond_Object = MibScalar
upsDiagnosticGlobalServiceChecksecond = _UpsDiagnosticGlobalServiceChecksecond_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 12, 7),
    _UpsDiagnosticGlobalServiceChecksecond_Type()
)
upsDiagnosticGlobalServiceChecksecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceChecksecond.setStatus("current")
_GeThirdUPS_ObjectIdentity = ObjectIdentity
geThirdUPS = _GeThirdUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13)
)
_UpsIdentthird_ObjectIdentity = ObjectIdentity
upsIdentthird = _UpsIdentthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1)
)
_UpsIdentManufacturerthird_Type = DisplayString
_UpsIdentManufacturerthird_Object = MibScalar
upsIdentManufacturerthird = _UpsIdentManufacturerthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 1),
    _UpsIdentManufacturerthird_Type()
)
upsIdentManufacturerthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturerthird.setStatus("current")
_UpsIdentModelthird_Type = DisplayString
_UpsIdentModelthird_Object = MibScalar
upsIdentModelthird = _UpsIdentModelthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 2),
    _UpsIdentModelthird_Type()
)
upsIdentModelthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelthird.setStatus("current")
_UpsIdentUPSSoftwareVersionthird_Type = DisplayString
_UpsIdentUPSSoftwareVersionthird_Object = MibScalar
upsIdentUPSSoftwareVersionthird = _UpsIdentUPSSoftwareVersionthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 3),
    _UpsIdentUPSSoftwareVersionthird_Type()
)
upsIdentUPSSoftwareVersionthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersionthird.setStatus("current")
_UpsIdentAgentSoftwareVersionthird_Type = DisplayString
_UpsIdentAgentSoftwareVersionthird_Object = MibScalar
upsIdentAgentSoftwareVersionthird = _UpsIdentAgentSoftwareVersionthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 4),
    _UpsIdentAgentSoftwareVersionthird_Type()
)
upsIdentAgentSoftwareVersionthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersionthird.setStatus("current")
_UpsIdentNamethird_Type = DisplayString
_UpsIdentNamethird_Object = MibScalar
upsIdentNamethird = _UpsIdentNamethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 5),
    _UpsIdentNamethird_Type()
)
upsIdentNamethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNamethird.setStatus("current")
_UpsIdentAttachedDevicesthird_Type = DisplayString
_UpsIdentAttachedDevicesthird_Object = MibScalar
upsIdentAttachedDevicesthird = _UpsIdentAttachedDevicesthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 6),
    _UpsIdentAttachedDevicesthird_Type()
)
upsIdentAttachedDevicesthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicesthird.setStatus("current")
_UpsIdentUPSSerialNumberthird_Type = DisplayString
_UpsIdentUPSSerialNumberthird_Object = MibScalar
upsIdentUPSSerialNumberthird = _UpsIdentUPSSerialNumberthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 7),
    _UpsIdentUPSSerialNumberthird_Type()
)
upsIdentUPSSerialNumberthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumberthird.setStatus("current")
_UpsIdentComProtVersionthird_Type = DisplayString
_UpsIdentComProtVersionthird_Object = MibScalar
upsIdentComProtVersionthird = _UpsIdentComProtVersionthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 8),
    _UpsIdentComProtVersionthird_Type()
)
upsIdentComProtVersionthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersionthird.setStatus("current")
_UpsIdentOperatingTimethird_Type = NonNegativeInteger32
_UpsIdentOperatingTimethird_Object = MibScalar
upsIdentOperatingTimethird = _UpsIdentOperatingTimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 1, 9),
    _UpsIdentOperatingTimethird_Type()
)
upsIdentOperatingTimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimethird.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimethird.setUnits("Seconds")
_UpsBatterythird_ObjectIdentity = ObjectIdentity
upsBatterythird = _UpsBatterythird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2)
)


class _UpsBatteryStatusthird_Type(Integer32):
    """Custom type upsBatteryStatusthird based on Integer32"""
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


_UpsBatteryStatusthird_Type.__name__ = "Integer32"
_UpsBatteryStatusthird_Object = MibScalar
upsBatteryStatusthird = _UpsBatteryStatusthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 1),
    _UpsBatteryStatusthird_Type()
)
upsBatteryStatusthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatusthird.setStatus("current")
_UpsSecondsOnBatterythird_Type = Integer32
_UpsSecondsOnBatterythird_Object = MibScalar
upsSecondsOnBatterythird = _UpsSecondsOnBatterythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 2),
    _UpsSecondsOnBatterythird_Type()
)
upsSecondsOnBatterythird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatterythird.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatterythird.setUnits("Seconds")
_UpsEstimatedMinutesRemainingthird_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingthird_Object = MibScalar
upsEstimatedMinutesRemainingthird = _UpsEstimatedMinutesRemainingthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 3),
    _UpsEstimatedMinutesRemainingthird_Type()
)
upsEstimatedMinutesRemainingthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingthird.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingthird.setUnits("minutes")


class _UpsEstimatedChargeRemainingthird_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingthird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingthird_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingthird_Object = MibScalar
upsEstimatedChargeRemainingthird = _UpsEstimatedChargeRemainingthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 4),
    _UpsEstimatedChargeRemainingthird_Type()
)
upsEstimatedChargeRemainingthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingthird.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingthird.setUnits("percent")
_UpsBatteryVoltagethird_Type = NonNegativeInteger32
_UpsBatteryVoltagethird_Object = MibScalar
upsBatteryVoltagethird = _UpsBatteryVoltagethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 5),
    _UpsBatteryVoltagethird_Type()
)
upsBatteryVoltagethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagethird.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltagethird.setUnits("0.1 Volt DC")
_UpsBatteryCurrentthird_Type = Integer32
_UpsBatteryCurrentthird_Object = MibScalar
upsBatteryCurrentthird = _UpsBatteryCurrentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 6),
    _UpsBatteryCurrentthird_Type()
)
upsBatteryCurrentthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentthird.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentthird.setUnits("0.1 Amp DC")
_UpsBatteryTemperaturethird_Type = Integer32
_UpsBatteryTemperaturethird_Object = MibScalar
upsBatteryTemperaturethird = _UpsBatteryTemperaturethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 7),
    _UpsBatteryTemperaturethird_Type()
)
upsBatteryTemperaturethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperaturethird.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperaturethird.setUnits("degrees Centigrade")
_UpsBatteryRipplethird_Type = Integer32
_UpsBatteryRipplethird_Object = MibScalar
upsBatteryRipplethird = _UpsBatteryRipplethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 2, 8),
    _UpsBatteryRipplethird_Type()
)
upsBatteryRipplethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipplethird.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipplethird.setUnits("0.1 Volt RMS")
_UpsInputthird_ObjectIdentity = ObjectIdentity
upsInputthird = _UpsInputthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3)
)
_UpsInputLineBadsthird_Type = Counter32
_UpsInputLineBadsthird_Object = MibScalar
upsInputLineBadsthird = _UpsInputLineBadsthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 1),
    _UpsInputLineBadsthird_Type()
)
upsInputLineBadsthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadsthird.setStatus("current")
_UpsInputNumLinesthird_Type = NonNegativeInteger32
_UpsInputNumLinesthird_Object = MibScalar
upsInputNumLinesthird = _UpsInputNumLinesthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 2),
    _UpsInputNumLinesthird_Type()
)
upsInputNumLinesthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinesthird.setStatus("current")
_UpsInputThirdTable_Object = MibTable
upsInputThirdTable = _UpsInputThirdTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputThirdTable.setStatus("current")
_UpsInputThirdEntry_Object = MibTableRow
upsInputThirdEntry = _UpsInputThirdEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1)
)
upsInputThirdEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexthird"),
)
if mibBuilder.loadTexts:
    upsInputThirdEntry.setStatus("current")
_UpsInputLineIndexthird_Type = PositiveInteger32
_UpsInputLineIndexthird_Object = MibTableColumn
upsInputLineIndexthird = _UpsInputLineIndexthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1, 1),
    _UpsInputLineIndexthird_Type()
)
upsInputLineIndexthird.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexthird.setStatus("current")
_UpsInputFrequencythird_Type = NonNegativeInteger32
_UpsInputFrequencythird_Object = MibTableColumn
upsInputFrequencythird = _UpsInputFrequencythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1, 2),
    _UpsInputFrequencythird_Type()
)
upsInputFrequencythird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencythird.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencythird.setUnits("0.1 Hertz")
_UpsInputVoltagethird_Type = NonNegativeInteger32
_UpsInputVoltagethird_Object = MibTableColumn
upsInputVoltagethird = _UpsInputVoltagethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1, 3),
    _UpsInputVoltagethird_Type()
)
upsInputVoltagethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltagethird.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltagethird.setUnits("RMS Volts")
_UpsInputCurrentthird_Type = NonNegativeInteger32
_UpsInputCurrentthird_Object = MibTableColumn
upsInputCurrentthird = _UpsInputCurrentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1, 4),
    _UpsInputCurrentthird_Type()
)
upsInputCurrentthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentthird.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentthird.setUnits("0.1 RMS Amp")
_UpsInputTruePowerthird_Type = NonNegativeInteger32
_UpsInputTruePowerthird_Object = MibTableColumn
upsInputTruePowerthird = _UpsInputTruePowerthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1, 5),
    _UpsInputTruePowerthird_Type()
)
upsInputTruePowerthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowerthird.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowerthird.setUnits("Watts")
_UpsInputVoltageMinthird_Type = NonNegativeInteger32
_UpsInputVoltageMinthird_Object = MibTableColumn
upsInputVoltageMinthird = _UpsInputVoltageMinthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1, 6),
    _UpsInputVoltageMinthird_Type()
)
upsInputVoltageMinthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMinthird.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMinthird.setUnits("RMS Volts")
_UpsInputVoltageMaxthird_Type = NonNegativeInteger32
_UpsInputVoltageMaxthird_Object = MibTableColumn
upsInputVoltageMaxthird = _UpsInputVoltageMaxthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 3, 3, 1, 7),
    _UpsInputVoltageMaxthird_Type()
)
upsInputVoltageMaxthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxthird.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxthird.setUnits("RMS Volts")
_UpsOutputthird_ObjectIdentity = ObjectIdentity
upsOutputthird = _UpsOutputthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4)
)


class _UpsOutputSourcethird_Type(Integer32):
    """Custom type upsOutputSourcethird based on Integer32"""
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


_UpsOutputSourcethird_Type.__name__ = "Integer32"
_UpsOutputSourcethird_Object = MibScalar
upsOutputSourcethird = _UpsOutputSourcethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 1),
    _UpsOutputSourcethird_Type()
)
upsOutputSourcethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourcethird.setStatus("current")
_UpsOutputFrequencythird_Type = NonNegativeInteger32
_UpsOutputFrequencythird_Object = MibScalar
upsOutputFrequencythird = _UpsOutputFrequencythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 2),
    _UpsOutputFrequencythird_Type()
)
upsOutputFrequencythird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencythird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencythird.setUnits("0.1 Hertz")
_UpsOutputNumLinesthird_Type = NonNegativeInteger32
_UpsOutputNumLinesthird_Object = MibScalar
upsOutputNumLinesthird = _UpsOutputNumLinesthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 3),
    _UpsOutputNumLinesthird_Type()
)
upsOutputNumLinesthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinesthird.setStatus("current")
_UpsOutputThirdTable_Object = MibTable
upsOutputThirdTable = _UpsOutputThirdTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputThirdTable.setStatus("current")
_UpsOutputThirdEntry_Object = MibTableRow
upsOutputThirdEntry = _UpsOutputThirdEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1)
)
upsOutputThirdEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexthird"),
)
if mibBuilder.loadTexts:
    upsOutputThirdEntry.setStatus("current")
_UpsOutputLineIndexthird_Type = PositiveInteger32
_UpsOutputLineIndexthird_Object = MibTableColumn
upsOutputLineIndexthird = _UpsOutputLineIndexthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 1),
    _UpsOutputLineIndexthird_Type()
)
upsOutputLineIndexthird.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexthird.setStatus("current")
_UpsOutputVoltagethird_Type = NonNegativeInteger32
_UpsOutputVoltagethird_Object = MibTableColumn
upsOutputVoltagethird = _UpsOutputVoltagethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 2),
    _UpsOutputVoltagethird_Type()
)
upsOutputVoltagethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltagethird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltagethird.setUnits("RMS Volts")
_UpsOutputCurrentthird_Type = NonNegativeInteger32
_UpsOutputCurrentthird_Object = MibTableColumn
upsOutputCurrentthird = _UpsOutputCurrentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 3),
    _UpsOutputCurrentthird_Type()
)
upsOutputCurrentthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentthird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentthird.setUnits("0.1 RMS Amp")
_UpsOutputPowerthird_Type = NonNegativeInteger32
_UpsOutputPowerthird_Object = MibTableColumn
upsOutputPowerthird = _UpsOutputPowerthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 4),
    _UpsOutputPowerthird_Type()
)
upsOutputPowerthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerthird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerthird.setUnits("Watts")


class _UpsOutputPercentLoadthird_Type(Integer32):
    """Custom type upsOutputPercentLoadthird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadthird_Type.__name__ = "Integer32"
_UpsOutputPercentLoadthird_Object = MibTableColumn
upsOutputPercentLoadthird = _UpsOutputPercentLoadthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 5),
    _UpsOutputPercentLoadthird_Type()
)
upsOutputPercentLoadthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadthird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadthird.setUnits("percent")


class _UpsOutputPowerFactorthird_Type(Integer32):
    """Custom type upsOutputPowerFactorthird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorthird_Type.__name__ = "Integer32"
_UpsOutputPowerFactorthird_Object = MibTableColumn
upsOutputPowerFactorthird = _UpsOutputPowerFactorthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 6),
    _UpsOutputPowerFactorthird_Type()
)
upsOutputPowerFactorthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorthird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorthird.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentthird_Type = Integer32
_UpsOutputPeakCurrentthird_Object = MibTableColumn
upsOutputPeakCurrentthird = _UpsOutputPeakCurrentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 7),
    _UpsOutputPeakCurrentthird_Type()
)
upsOutputPeakCurrentthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentthird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentthird.setUnits("Amps")
_UpsOutputShareCurrentthird_Type = Integer32
_UpsOutputShareCurrentthird_Object = MibTableColumn
upsOutputShareCurrentthird = _UpsOutputShareCurrentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 4, 4, 1, 8),
    _UpsOutputShareCurrentthird_Type()
)
upsOutputShareCurrentthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentthird.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentthird.setUnits("Amps")
_UpsBypassthird_ObjectIdentity = ObjectIdentity
upsBypassthird = _UpsBypassthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5)
)
_UpsBypassFrequencythird_Type = NonNegativeInteger32
_UpsBypassFrequencythird_Object = MibScalar
upsBypassFrequencythird = _UpsBypassFrequencythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 1),
    _UpsBypassFrequencythird_Type()
)
upsBypassFrequencythird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencythird.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencythird.setUnits("0.1 Hertz")
_UpsBypassNumLinesthird_Type = NonNegativeInteger32
_UpsBypassNumLinesthird_Object = MibScalar
upsBypassNumLinesthird = _UpsBypassNumLinesthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 2),
    _UpsBypassNumLinesthird_Type()
)
upsBypassNumLinesthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinesthird.setStatus("current")
_UpsBypassThirdTable_Object = MibTable
upsBypassThirdTable = _UpsBypassThirdTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassThirdTable.setStatus("current")
_UpsBypassThirdEntry_Object = MibTableRow
upsBypassThirdEntry = _UpsBypassThirdEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 3, 1)
)
upsBypassThirdEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexthird"),
)
if mibBuilder.loadTexts:
    upsBypassThirdEntry.setStatus("current")
_UpsBypassLineIndexthird_Type = PositiveInteger32
_UpsBypassLineIndexthird_Object = MibTableColumn
upsBypassLineIndexthird = _UpsBypassLineIndexthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 3, 1, 1),
    _UpsBypassLineIndexthird_Type()
)
upsBypassLineIndexthird.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexthird.setStatus("current")
_UpsBypassVoltagethird_Type = NonNegativeInteger32
_UpsBypassVoltagethird_Object = MibTableColumn
upsBypassVoltagethird = _UpsBypassVoltagethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 3, 1, 2),
    _UpsBypassVoltagethird_Type()
)
upsBypassVoltagethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltagethird.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltagethird.setUnits("RMS Volts")
_UpsBypassCurrentthird_Type = NonNegativeInteger32
_UpsBypassCurrentthird_Object = MibTableColumn
upsBypassCurrentthird = _UpsBypassCurrentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 3, 1, 3),
    _UpsBypassCurrentthird_Type()
)
upsBypassCurrentthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentthird.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentthird.setUnits("0.1 RMS Amp")
_UpsBypassPowerthird_Type = NonNegativeInteger32
_UpsBypassPowerthird_Object = MibTableColumn
upsBypassPowerthird = _UpsBypassPowerthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 5, 3, 1, 4),
    _UpsBypassPowerthird_Type()
)
upsBypassPowerthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowerthird.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowerthird.setUnits("Watts")
_UpsAlarmthird_ObjectIdentity = ObjectIdentity
upsAlarmthird = _UpsAlarmthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6)
)
_UpsAlarmsPresentthird_Type = Gauge32
_UpsAlarmsPresentthird_Object = MibScalar
upsAlarmsPresentthird = _UpsAlarmsPresentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 1),
    _UpsAlarmsPresentthird_Type()
)
upsAlarmsPresentthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentthird.setStatus("current")
_UpsAlarmThirdTable_Object = MibTable
upsAlarmThirdTable = _UpsAlarmThirdTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmThirdTable.setStatus("current")
_UpsAlarmThirdEntry_Object = MibTableRow
upsAlarmThirdEntry = _UpsAlarmThirdEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 2, 1)
)
upsAlarmThirdEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdthird"),
)
if mibBuilder.loadTexts:
    upsAlarmThirdEntry.setStatus("current")
_UpsAlarmIdthird_Type = PositiveInteger32
_UpsAlarmIdthird_Object = MibTableColumn
upsAlarmIdthird = _UpsAlarmIdthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 2, 1, 1),
    _UpsAlarmIdthird_Type()
)
upsAlarmIdthird.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdthird.setStatus("current")
_UpsAlarmDescrthird_Type = AutonomousType
_UpsAlarmDescrthird_Object = MibTableColumn
upsAlarmDescrthird = _UpsAlarmDescrthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 2, 1, 2),
    _UpsAlarmDescrthird_Type()
)
upsAlarmDescrthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrthird.setStatus("current")
_UpsAlarmTimethird_Type = TimeStamp
_UpsAlarmTimethird_Object = MibTableColumn
upsAlarmTimethird = _UpsAlarmTimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 2, 1, 3),
    _UpsAlarmTimethird_Type()
)
upsAlarmTimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimethird.setStatus("current")
_UpsWellKnownAlarmsthird_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmsthird = _UpsWellKnownAlarmsthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3)
)
_UpsAlarmBatteryBadthird_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadthird = _UpsAlarmBatteryBadthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadthird.setStatus("current")
_UpsAlarmOnBatterythird_ObjectIdentity = ObjectIdentity
upsAlarmOnBatterythird = _UpsAlarmOnBatterythird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatterythird.setStatus("current")
_UpsAlarmLowBatterythird_ObjectIdentity = ObjectIdentity
upsAlarmLowBatterythird = _UpsAlarmLowBatterythird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatterythird.setStatus("current")
_UpsAlarmDepletedBatterythird_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatterythird = _UpsAlarmDepletedBatterythird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatterythird.setStatus("current")
_UpsAlarmTempBadthird_ObjectIdentity = ObjectIdentity
upsAlarmTempBadthird = _UpsAlarmTempBadthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadthird.setStatus("current")
_UpsAlarmInputBadthird_ObjectIdentity = ObjectIdentity
upsAlarmInputBadthird = _UpsAlarmInputBadthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadthird.setStatus("current")
_UpsAlarmOutputBadthird_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadthird = _UpsAlarmOutputBadthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadthird.setStatus("current")
_UpsAlarmOutputOverloadthird_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadthird = _UpsAlarmOutputOverloadthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadthird.setStatus("current")
_UpsAlarmOnBypassthird_ObjectIdentity = ObjectIdentity
upsAlarmOnBypassthird = _UpsAlarmOnBypassthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypassthird.setStatus("current")
_UpsAlarmBypassBadthird_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadthird = _UpsAlarmBypassBadthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadthird.setStatus("current")
_UpsAlarmOutputOffAsRequestedthird_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedthird = _UpsAlarmOutputOffAsRequestedthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedthird.setStatus("current")
_UpsAlarmUpsOffAsRequestedthird_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedthird = _UpsAlarmUpsOffAsRequestedthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedthird.setStatus("current")
_UpsAlarmChargerFailedthird_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedthird = _UpsAlarmChargerFailedthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedthird.setStatus("current")
_UpsAlarmUpsOutputOffthird_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOffthird = _UpsAlarmUpsOutputOffthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOffthird.setStatus("current")
_UpsAlarmUpsSystemOffthird_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOffthird = _UpsAlarmUpsSystemOffthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOffthird.setStatus("current")
_UpsAlarmFanFailurethird_ObjectIdentity = ObjectIdentity
upsAlarmFanFailurethird = _UpsAlarmFanFailurethird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailurethird.setStatus("current")
_UpsAlarmFuseFailurethird_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailurethird = _UpsAlarmFuseFailurethird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailurethird.setStatus("current")
_UpsAlarmGeneralFaultthird_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultthird = _UpsAlarmGeneralFaultthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultthird.setStatus("current")
_UpsAlarmDiagnosticTestFailedthird_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedthird = _UpsAlarmDiagnosticTestFailedthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedthird.setStatus("current")
_UpsAlarmCommunicationsLostthird_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostthird = _UpsAlarmCommunicationsLostthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostthird.setStatus("current")
_UpsAlarmAwaitingPowerthird_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowerthird = _UpsAlarmAwaitingPowerthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowerthird.setStatus("current")
_UpsAlarmShutdownPendingthird_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingthird = _UpsAlarmShutdownPendingthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingthird.setStatus("current")
_UpsAlarmShutdownImminentthird_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentthird = _UpsAlarmShutdownImminentthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentthird.setStatus("current")
_UpsAlarmTestInProgressthird_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgressthird = _UpsAlarmTestInProgressthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgressthird.setStatus("current")
_UpsAlarmReceptacleOffthird_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOffthird = _UpsAlarmReceptacleOffthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOffthird.setStatus("current")
_UpsAlarmHighSpeedBusFailurethird_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailurethird = _UpsAlarmHighSpeedBusFailurethird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailurethird.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailurethird_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailurethird = _UpsAlarmHighSpeedBusJACRCFailurethird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailurethird.setStatus("current")
_UpsAlarmConnectivityBusFailurethird_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailurethird = _UpsAlarmConnectivityBusFailurethird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailurethird.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailurethird_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailurethird = _UpsAlarmHighSpeedBusJBCRCFailurethird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailurethird.setStatus("current")
_UpsAlarmCurrentSharingthird_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingthird = _UpsAlarmCurrentSharingthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingthird.setStatus("current")
_UpsAlarmDCRipplethird_ObjectIdentity = ObjectIdentity
upsAlarmDCRipplethird = _UpsAlarmDCRipplethird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipplethird.setStatus("current")
_UpsAlarmMaskAthird_Type = Unsigned32
_UpsAlarmMaskAthird_Object = MibScalar
upsAlarmMaskAthird = _UpsAlarmMaskAthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 6, 4),
    _UpsAlarmMaskAthird_Type()
)
upsAlarmMaskAthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAthird.setStatus("current")
_UpsTestthird_ObjectIdentity = ObjectIdentity
upsTestthird = _UpsTestthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7)
)
_UpsTestIdthird_Type = ObjectIdentifier
_UpsTestIdthird_Object = MibScalar
upsTestIdthird = _UpsTestIdthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 1),
    _UpsTestIdthird_Type()
)
upsTestIdthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdthird.setStatus("current")
_UpsTestSpinLockthird_Type = TestAndIncr
_UpsTestSpinLockthird_Object = MibScalar
upsTestSpinLockthird = _UpsTestSpinLockthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 2),
    _UpsTestSpinLockthird_Type()
)
upsTestSpinLockthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLockthird.setStatus("current")


class _UpsTestResultsSummarythird_Type(Integer32):
    """Custom type upsTestResultsSummarythird based on Integer32"""
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


_UpsTestResultsSummarythird_Type.__name__ = "Integer32"
_UpsTestResultsSummarythird_Object = MibScalar
upsTestResultsSummarythird = _UpsTestResultsSummarythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 3),
    _UpsTestResultsSummarythird_Type()
)
upsTestResultsSummarythird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummarythird.setStatus("current")
_UpsTestResultsDetailthird_Type = DisplayString
_UpsTestResultsDetailthird_Object = MibScalar
upsTestResultsDetailthird = _UpsTestResultsDetailthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 4),
    _UpsTestResultsDetailthird_Type()
)
upsTestResultsDetailthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailthird.setStatus("current")
_UpsTestStartTimethird_Type = TimeStamp
_UpsTestStartTimethird_Object = MibScalar
upsTestStartTimethird = _UpsTestStartTimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 5),
    _UpsTestStartTimethird_Type()
)
upsTestStartTimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimethird.setStatus("current")
_UpsTestElapsedTimethird_Type = TimeInterval
_UpsTestElapsedTimethird_Object = MibScalar
upsTestElapsedTimethird = _UpsTestElapsedTimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 6),
    _UpsTestElapsedTimethird_Type()
)
upsTestElapsedTimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimethird.setStatus("current")
_UpsWellKnownTeststhird_ObjectIdentity = ObjectIdentity
upsWellKnownTeststhird = _UpsWellKnownTeststhird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 7)
)
_UpsTestNoTestsInitiatedthird_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedthird = _UpsTestNoTestsInitiatedthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedthird.setStatus("current")
_UpsTestAbortTestInProgressthird_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgressthird = _UpsTestAbortTestInProgressthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgressthird.setStatus("current")
_UpsTestGeneralSystemsTestthird_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestthird = _UpsTestGeneralSystemsTestthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestthird.setStatus("current")
_UpsTestQuickBatteryTestthird_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestthird = _UpsTestQuickBatteryTestthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestthird.setStatus("current")
_UpsTestDeepBatteryCalibrationthird_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationthird = _UpsTestDeepBatteryCalibrationthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationthird.setStatus("current")
_UpsControlthird_ObjectIdentity = ObjectIdentity
upsControlthird = _UpsControlthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8)
)


class _UpsShutdownTypethird_Type(Integer32):
    """Custom type upsShutdownTypethird based on Integer32"""
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


_UpsShutdownTypethird_Type.__name__ = "Integer32"
_UpsShutdownTypethird_Object = MibScalar
upsShutdownTypethird = _UpsShutdownTypethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 1),
    _UpsShutdownTypethird_Type()
)
upsShutdownTypethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypethird.setStatus("current")


class _UpsShutdownAfterDelaythird_Type(Integer32):
    """Custom type upsShutdownAfterDelaythird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelaythird_Type.__name__ = "Integer32"
_UpsShutdownAfterDelaythird_Object = MibScalar
upsShutdownAfterDelaythird = _UpsShutdownAfterDelaythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 2),
    _UpsShutdownAfterDelaythird_Type()
)
upsShutdownAfterDelaythird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaythird.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaythird.setUnits("Seconds")


class _UpsStartupAfterDelaythird_Type(Integer32):
    """Custom type upsStartupAfterDelaythird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelaythird_Type.__name__ = "Integer32"
_UpsStartupAfterDelaythird_Object = MibScalar
upsStartupAfterDelaythird = _UpsStartupAfterDelaythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 3),
    _UpsStartupAfterDelaythird_Type()
)
upsStartupAfterDelaythird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelaythird.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelaythird.setUnits("Seconds")


class _UpsRebootWithDurationthird_Type(Integer32):
    """Custom type upsRebootWithDurationthird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationthird_Type.__name__ = "Integer32"
_UpsRebootWithDurationthird_Object = MibScalar
upsRebootWithDurationthird = _UpsRebootWithDurationthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 4),
    _UpsRebootWithDurationthird_Type()
)
upsRebootWithDurationthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationthird.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationthird.setUnits("Seconds")


class _UpsAutoRestartthird_Type(Integer32):
    """Custom type upsAutoRestartthird based on Integer32"""
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


_UpsAutoRestartthird_Type.__name__ = "Integer32"
_UpsAutoRestartthird_Object = MibScalar
upsAutoRestartthird = _UpsAutoRestartthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 5),
    _UpsAutoRestartthird_Type()
)
upsAutoRestartthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartthird.setStatus("current")
_UpsReceptaclesNumthird_Type = NonNegativeInteger32
_UpsReceptaclesNumthird_Object = MibScalar
upsReceptaclesNumthird = _UpsReceptaclesNumthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 6),
    _UpsReceptaclesNumthird_Type()
)
upsReceptaclesNumthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumthird.setStatus("current")
_UpsReceptacleThirdTable_Object = MibTable
upsReceptacleThirdTable = _UpsReceptacleThirdTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleThirdTable.setStatus("current")
_UpsReceptacleThirdEntry_Object = MibTableRow
upsReceptacleThirdEntry = _UpsReceptacleThirdEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 7, 1)
)
upsReceptacleThirdEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexthird"),
)
if mibBuilder.loadTexts:
    upsReceptacleThirdEntry.setStatus("current")
_UpsReceptacleLineIndexthird_Type = PositiveInteger32
_UpsReceptacleLineIndexthird_Object = MibTableColumn
upsReceptacleLineIndexthird = _UpsReceptacleLineIndexthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 7, 1, 1),
    _UpsReceptacleLineIndexthird_Type()
)
upsReceptacleLineIndexthird.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexthird.setStatus("current")


class _UpsReceptacleOnOffthird_Type(Integer32):
    """Custom type upsReceptacleOnOffthird based on Integer32"""
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


_UpsReceptacleOnOffthird_Type.__name__ = "Integer32"
_UpsReceptacleOnOffthird_Object = MibTableColumn
upsReceptacleOnOffthird = _UpsReceptacleOnOffthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 7, 1, 2),
    _UpsReceptacleOnOffthird_Type()
)
upsReceptacleOnOffthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOffthird.setStatus("current")


class _UpsUPSModethird_Type(Integer32):
    """Custom type upsUPSModethird based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModethird_Type.__name__ = "Integer32"
_UpsUPSModethird_Object = MibScalar
upsUPSModethird = _UpsUPSModethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 8),
    _UpsUPSModethird_Type()
)
upsUPSModethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModethird.setStatus("current")


class _UpsRectifierOnOffthird_Type(Integer32):
    """Custom type upsRectifierOnOffthird based on Integer32"""
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


_UpsRectifierOnOffthird_Type.__name__ = "Integer32"
_UpsRectifierOnOffthird_Object = MibScalar
upsRectifierOnOffthird = _UpsRectifierOnOffthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 9),
    _UpsRectifierOnOffthird_Type()
)
upsRectifierOnOffthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOffthird.setStatus("current")


class _UpsBatteryChargeMethodthird_Type(Integer32):
    """Custom type upsBatteryChargeMethodthird based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodthird_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodthird_Object = MibScalar
upsBatteryChargeMethodthird = _UpsBatteryChargeMethodthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 10),
    _UpsBatteryChargeMethodthird_Type()
)
upsBatteryChargeMethodthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodthird.setStatus("current")


class _UpsInverterOnOffthird_Type(Integer32):
    """Custom type upsInverterOnOffthird based on Integer32"""
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


_UpsInverterOnOffthird_Type.__name__ = "Integer32"
_UpsInverterOnOffthird_Object = MibScalar
upsInverterOnOffthird = _UpsInverterOnOffthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 11),
    _UpsInverterOnOffthird_Type()
)
upsInverterOnOffthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOffthird.setStatus("current")


class _UpsBypassOnOffthird_Type(Integer32):
    """Custom type upsBypassOnOffthird based on Integer32"""
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


_UpsBypassOnOffthird_Type.__name__ = "Integer32"
_UpsBypassOnOffthird_Object = MibScalar
upsBypassOnOffthird = _UpsBypassOnOffthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 12),
    _UpsBypassOnOffthird_Type()
)
upsBypassOnOffthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOffthird.setStatus("current")


class _UpsLoadSourcethird_Type(Integer32):
    """Custom type upsLoadSourcethird based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourcethird_Type.__name__ = "Integer32"
_UpsLoadSourcethird_Object = MibScalar
upsLoadSourcethird = _UpsLoadSourcethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 8, 13),
    _UpsLoadSourcethird_Type()
)
upsLoadSourcethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourcethird.setStatus("current")
_UpsConfigthird_ObjectIdentity = ObjectIdentity
upsConfigthird = _UpsConfigthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9)
)
_UpsConfigInputVoltagethird_Type = NonNegativeInteger32
_UpsConfigInputVoltagethird_Object = MibScalar
upsConfigInputVoltagethird = _UpsConfigInputVoltagethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 1),
    _UpsConfigInputVoltagethird_Type()
)
upsConfigInputVoltagethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltagethird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltagethird.setUnits("RMS Volts")
_UpsConfigInputFreqthird_Type = NonNegativeInteger32
_UpsConfigInputFreqthird_Object = MibScalar
upsConfigInputFreqthird = _UpsConfigInputFreqthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 2),
    _UpsConfigInputFreqthird_Type()
)
upsConfigInputFreqthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqthird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqthird.setUnits("0.1 Hertz")
_UpsConfigOutputVoltagethird_Type = NonNegativeInteger32
_UpsConfigOutputVoltagethird_Object = MibScalar
upsConfigOutputVoltagethird = _UpsConfigOutputVoltagethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 3),
    _UpsConfigOutputVoltagethird_Type()
)
upsConfigOutputVoltagethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagethird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagethird.setUnits("RMS Volts")
_UpsConfigOutputFreqthird_Type = NonNegativeInteger32
_UpsConfigOutputFreqthird_Object = MibScalar
upsConfigOutputFreqthird = _UpsConfigOutputFreqthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 4),
    _UpsConfigOutputFreqthird_Type()
)
upsConfigOutputFreqthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqthird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqthird.setUnits("0.1 Hertz")
_UpsConfigOutputVAthird_Type = NonNegativeInteger32
_UpsConfigOutputVAthird_Object = MibScalar
upsConfigOutputVAthird = _UpsConfigOutputVAthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 5),
    _UpsConfigOutputVAthird_Type()
)
upsConfigOutputVAthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAthird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAthird.setUnits("Volt-Amps")
_UpsConfigOutputPowerthird_Type = NonNegativeInteger32
_UpsConfigOutputPowerthird_Object = MibScalar
upsConfigOutputPowerthird = _UpsConfigOutputPowerthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 6),
    _UpsConfigOutputPowerthird_Type()
)
upsConfigOutputPowerthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowerthird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowerthird.setUnits("Watts")
_UpsConfigLowBattTimethird_Type = NonNegativeInteger32
_UpsConfigLowBattTimethird_Object = MibScalar
upsConfigLowBattTimethird = _UpsConfigLowBattTimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 7),
    _UpsConfigLowBattTimethird_Type()
)
upsConfigLowBattTimethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimethird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimethird.setUnits("minutes")


class _UpsConfigAudibleStatusthird_Type(Integer32):
    """Custom type upsConfigAudibleStatusthird based on Integer32"""
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


_UpsConfigAudibleStatusthird_Type.__name__ = "Integer32"
_UpsConfigAudibleStatusthird_Object = MibScalar
upsConfigAudibleStatusthird = _UpsConfigAudibleStatusthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 8),
    _UpsConfigAudibleStatusthird_Type()
)
upsConfigAudibleStatusthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatusthird.setStatus("current")
_UpsConfigLowVoltageTransferPointthird_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointthird_Object = MibScalar
upsConfigLowVoltageTransferPointthird = _UpsConfigLowVoltageTransferPointthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 9),
    _UpsConfigLowVoltageTransferPointthird_Type()
)
upsConfigLowVoltageTransferPointthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointthird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointthird.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointthird_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointthird_Object = MibScalar
upsConfigHighVoltageTransferPointthird = _UpsConfigHighVoltageTransferPointthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 10),
    _UpsConfigHighVoltageTransferPointthird_Type()
)
upsConfigHighVoltageTransferPointthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointthird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointthird.setUnits("RMS Volts")
_UpsConfigBatteryCapacitythird_Type = NonNegativeInteger32
_UpsConfigBatteryCapacitythird_Object = MibScalar
upsConfigBatteryCapacitythird = _UpsConfigBatteryCapacitythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 11),
    _UpsConfigBatteryCapacitythird_Type()
)
upsConfigBatteryCapacitythird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitythird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitythird.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentthird_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentthird_Object = MibScalar
upsConfigBatteryChargeCurrentthird = _UpsConfigBatteryChargeCurrentthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 12),
    _UpsConfigBatteryChargeCurrentthird_Type()
)
upsConfigBatteryChargeCurrentthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentthird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentthird.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdownthird_Type(Integer32):
    """Custom type upsConfigNoLoadShutdownthird based on Integer32"""
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


_UpsConfigNoLoadShutdownthird_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdownthird_Object = MibScalar
upsConfigNoLoadShutdownthird = _UpsConfigNoLoadShutdownthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 13),
    _UpsConfigNoLoadShutdownthird_Type()
)
upsConfigNoLoadShutdownthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdownthird.setStatus("current")
_UpsConfigStartDelaythird_Type = PositiveInteger32
_UpsConfigStartDelaythird_Object = MibScalar
upsConfigStartDelaythird = _UpsConfigStartDelaythird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 9, 14),
    _UpsConfigStartDelaythird_Type()
)
upsConfigStartDelaythird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelaythird.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelaythird.setUnits("minutes")
_UpsGetSetthird_ObjectIdentity = ObjectIdentity
upsGetSetthird = _UpsGetSetthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10)
)
_UpsEventGetNextthird_Type = PositiveInteger32
_UpsEventGetNextthird_Object = MibScalar
upsEventGetNextthird = _UpsEventGetNextthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 1),
    _UpsEventGetNextthird_Type()
)
upsEventGetNextthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextthird.setStatus("current")
_UpsEventGetPreviousthird_Type = PositiveInteger32
_UpsEventGetPreviousthird_Object = MibScalar
upsEventGetPreviousthird = _UpsEventGetPreviousthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 2),
    _UpsEventGetPreviousthird_Type()
)
upsEventGetPreviousthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPreviousthird.setStatus("current")
_UpsEventSetStartingTimeStampthird_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampthird_Object = MibScalar
upsEventSetStartingTimeStampthird = _UpsEventSetStartingTimeStampthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 3),
    _UpsEventSetStartingTimeStampthird_Type()
)
upsEventSetStartingTimeStampthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampthird.setStatus("current")
_UpsEventRetreiveCurrentTimeStampthird_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampthird_Object = MibScalar
upsEventRetreiveCurrentTimeStampthird = _UpsEventRetreiveCurrentTimeStampthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 4),
    _UpsEventRetreiveCurrentTimeStampthird_Type()
)
upsEventRetreiveCurrentTimeStampthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampthird.setStatus("current")
_UpsEventTableSizethird_Type = NonNegativeInteger32
_UpsEventTableSizethird_Object = MibScalar
upsEventTableSizethird = _UpsEventTableSizethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 5),
    _UpsEventTableSizethird_Type()
)
upsEventTableSizethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizethird.setStatus("current")
_UpsEventThirdTable_Object = MibTable
upsEventThirdTable = _UpsEventThirdTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventThirdTable.setStatus("current")
_UpsEventThirdEntry_Object = MibTableRow
upsEventThirdEntry = _UpsEventThirdEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 6, 1)
)
upsEventThirdEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexthird"),
)
if mibBuilder.loadTexts:
    upsEventThirdEntry.setStatus("current")
_UpsEventLineIndexthird_Type = PositiveInteger32
_UpsEventLineIndexthird_Object = MibTableColumn
upsEventLineIndexthird = _UpsEventLineIndexthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 6, 1, 1),
    _UpsEventLineIndexthird_Type()
)
upsEventLineIndexthird.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexthird.setStatus("current")
_UpsEventCodethird_Type = Integer32
_UpsEventCodethird_Object = MibTableColumn
upsEventCodethird = _UpsEventCodethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 6, 1, 2),
    _UpsEventCodethird_Type()
)
upsEventCodethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodethird.setStatus("current")
_UpsEventStatusthird_Type = NonNegativeInteger32
_UpsEventStatusthird_Object = MibTableColumn
upsEventStatusthird = _UpsEventStatusthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 6, 1, 3),
    _UpsEventStatusthird_Type()
)
upsEventStatusthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatusthird.setStatus("current")
_UpsEventTimethird_Type = NonNegativeInteger32
_UpsEventTimethird_Object = MibTableColumn
upsEventTimethird = _UpsEventTimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 6, 1, 4),
    _UpsEventTimethird_Type()
)
upsEventTimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimethird.setStatus("current")
_UpsParametersReadthird_Type = PositiveInteger32
_UpsParametersReadthird_Object = MibScalar
upsParametersReadthird = _UpsParametersReadthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 7),
    _UpsParametersReadthird_Type()
)
upsParametersReadthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadthird.setStatus("current")
_UpsParametersWritethird_Type = PositiveInteger32
_UpsParametersWritethird_Object = MibScalar
upsParametersWritethird = _UpsParametersWritethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 8),
    _UpsParametersWritethird_Type()
)
upsParametersWritethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWritethird.setStatus("current")
_UpsParametersStartAddressthird_Type = NonNegativeInteger32
_UpsParametersStartAddressthird_Object = MibScalar
upsParametersStartAddressthird = _UpsParametersStartAddressthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 9),
    _UpsParametersStartAddressthird_Type()
)
upsParametersStartAddressthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddressthird.setStatus("current")
_UpsParameterTableSizethird_Type = NonNegativeInteger32
_UpsParameterTableSizethird_Object = MibScalar
upsParameterTableSizethird = _UpsParameterTableSizethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 10),
    _UpsParameterTableSizethird_Type()
)
upsParameterTableSizethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizethird.setStatus("current")
_UpsParameterThirdTable_Object = MibTable
upsParameterThirdTable = _UpsParameterThirdTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterThirdTable.setStatus("current")
_UpsParameterThirdEntry_Object = MibTableRow
upsParameterThirdEntry = _UpsParameterThirdEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 11, 1)
)
upsParameterThirdEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexthird"),
)
if mibBuilder.loadTexts:
    upsParameterThirdEntry.setStatus("current")
_UpsParameterLineIndexthird_Type = PositiveInteger32
_UpsParameterLineIndexthird_Object = MibTableColumn
upsParameterLineIndexthird = _UpsParameterLineIndexthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 11, 1, 1),
    _UpsParameterLineIndexthird_Type()
)
upsParameterLineIndexthird.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexthird.setStatus("current")
_UpsParameterValuethird_Type = Integer32
_UpsParameterValuethird_Object = MibTableColumn
upsParameterValuethird = _UpsParameterValuethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 11, 1, 2),
    _UpsParameterValuethird_Type()
)
upsParameterValuethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValuethird.setStatus("current")
_UpsStatusthird_Type = NonNegativeInteger32
_UpsStatusthird_Object = MibScalar
upsStatusthird = _UpsStatusthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 12),
    _UpsStatusthird_Type()
)
upsStatusthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusthird.setStatus("current")
_UpsMainsStatisticsMBfailthird_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailthird_Object = MibScalar
upsMainsStatisticsMBfailthird = _UpsMainsStatisticsMBfailthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 13),
    _UpsMainsStatisticsMBfailthird_Type()
)
upsMainsStatisticsMBfailthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailthird.setStatus("current")
_UpsMainsStatisticsMRfailthird_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailthird_Object = MibScalar
upsMainsStatisticsMRfailthird = _UpsMainsStatisticsMRfailthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 14),
    _UpsMainsStatisticsMRfailthird_Type()
)
upsMainsStatisticsMRfailthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailthird.setStatus("current")
_UpsMainsStatisticsB2third_Type = NonNegativeInteger32
_UpsMainsStatisticsB2third_Object = MibScalar
upsMainsStatisticsB2third = _UpsMainsStatisticsB2third_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 15),
    _UpsMainsStatisticsB2third_Type()
)
upsMainsStatisticsB2third.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2third.setStatus("current")
_UpsMainsStatisticsB5third_Type = NonNegativeInteger32
_UpsMainsStatisticsB5third_Object = MibScalar
upsMainsStatisticsB5third = _UpsMainsStatisticsB5third_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 16),
    _UpsMainsStatisticsB5third_Type()
)
upsMainsStatisticsB5third.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5third.setStatus("current")
_UpsMainsStatisticsB10third_Type = NonNegativeInteger32
_UpsMainsStatisticsB10third_Object = MibScalar
upsMainsStatisticsB10third = _UpsMainsStatisticsB10third_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 17),
    _UpsMainsStatisticsB10third_Type()
)
upsMainsStatisticsB10third.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10third.setStatus("current")
_UpsMainsStatisticsB200third_Type = NonNegativeInteger32
_UpsMainsStatisticsB200third_Object = MibScalar
upsMainsStatisticsB200third = _UpsMainsStatisticsB200third_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 18),
    _UpsMainsStatisticsB200third_Type()
)
upsMainsStatisticsB200third.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200third.setStatus("current")
_UpsMainsStatisticsBypRelthird_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelthird_Object = MibScalar
upsMainsStatisticsBypRelthird = _UpsMainsStatisticsBypRelthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 19),
    _UpsMainsStatisticsBypRelthird_Type()
)
upsMainsStatisticsBypRelthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelthird.setStatus("current")
_UpsTimethird_Type = NonNegativeInteger32
_UpsTimethird_Object = MibScalar
upsTimethird = _UpsTimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 20),
    _UpsTimethird_Type()
)
upsTimethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimethird.setStatus("current")
_UpsRequestPermissionthird_Type = DisplayString
_UpsRequestPermissionthird_Object = MibScalar
upsRequestPermissionthird = _UpsRequestPermissionthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 21),
    _UpsRequestPermissionthird_Type()
)
upsRequestPermissionthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissionthird.setStatus("current")
_UpsEventGetCodethird_Type = Integer32
_UpsEventGetCodethird_Object = MibScalar
upsEventGetCodethird = _UpsEventGetCodethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 22),
    _UpsEventGetCodethird_Type()
)
upsEventGetCodethird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodethird.setStatus("current")
_UpsEventSpinLockthird_Type = TestAndIncr
_UpsEventSpinLockthird_Object = MibScalar
upsEventSpinLockthird = _UpsEventSpinLockthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 23),
    _UpsEventSpinLockthird_Type()
)
upsEventSpinLockthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLockthird.setStatus("current")
_UpsParameterSpinLockthird_Type = TestAndIncr
_UpsParameterSpinLockthird_Object = MibScalar
upsParameterSpinLockthird = _UpsParameterSpinLockthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 10, 24),
    _UpsParameterSpinLockthird_Type()
)
upsParameterSpinLockthird.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLockthird.setStatus("current")
_GeUPSTrapsthird_ObjectIdentity = ObjectIdentity
geUPSTrapsthird = _GeUPSTrapsthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11)
)
_UpsDiagnosticthird_ObjectIdentity = ObjectIdentity
upsDiagnosticthird = _UpsDiagnosticthird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12)
)
_UpsDiagnosticBusJACommunicationStatusthird_Type = Integer32
_UpsDiagnosticBusJACommunicationStatusthird_Object = MibScalar
upsDiagnosticBusJACommunicationStatusthird = _UpsDiagnosticBusJACommunicationStatusthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12, 1),
    _UpsDiagnosticBusJACommunicationStatusthird_Type()
)
upsDiagnosticBusJACommunicationStatusthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatusthird.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatusthird_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatusthird_Object = MibScalar
upsDiagnosticBusJBCommunicationStatusthird = _UpsDiagnosticBusJBCommunicationStatusthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatusthird_Type()
)
upsDiagnosticBusJBCommunicationStatusthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatusthird.setStatus("current")
_UpsDiagnosticBatteryLifetimethird_Type = Integer32
_UpsDiagnosticBatteryLifetimethird_Object = MibScalar
upsDiagnosticBatteryLifetimethird = _UpsDiagnosticBatteryLifetimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12, 3),
    _UpsDiagnosticBatteryLifetimethird_Type()
)
upsDiagnosticBatteryLifetimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimethird.setStatus("current")
_UpsDiagnosticFansLifetimethird_Type = Integer32
_UpsDiagnosticFansLifetimethird_Object = MibScalar
upsDiagnosticFansLifetimethird = _UpsDiagnosticFansLifetimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12, 4),
    _UpsDiagnosticFansLifetimethird_Type()
)
upsDiagnosticFansLifetimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimethird.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimethird_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimethird_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimethird = _UpsDiagnosticDCcapacitorsLifetimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimethird_Type()
)
upsDiagnosticDCcapacitorsLifetimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimethird.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimethird_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimethird_Object = MibScalar
upsDiagnosticACcapacitorsLifetimethird = _UpsDiagnosticACcapacitorsLifetimethird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimethird_Type()
)
upsDiagnosticACcapacitorsLifetimethird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimethird.setStatus("current")
_UpsDiagnosticGlobalServiceCheckthird_Type = Integer32
_UpsDiagnosticGlobalServiceCheckthird_Object = MibScalar
upsDiagnosticGlobalServiceCheckthird = _UpsDiagnosticGlobalServiceCheckthird_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 12, 7),
    _UpsDiagnosticGlobalServiceCheckthird_Type()
)
upsDiagnosticGlobalServiceCheckthird.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheckthird.setStatus("current")
_GeFourthUPS_ObjectIdentity = ObjectIdentity
geFourthUPS = _GeFourthUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14)
)
_UpsIdentfourth_ObjectIdentity = ObjectIdentity
upsIdentfourth = _UpsIdentfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1)
)
_UpsIdentManufacturerfourth_Type = DisplayString
_UpsIdentManufacturerfourth_Object = MibScalar
upsIdentManufacturerfourth = _UpsIdentManufacturerfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 1),
    _UpsIdentManufacturerfourth_Type()
)
upsIdentManufacturerfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturerfourth.setStatus("current")
_UpsIdentModelfourth_Type = DisplayString
_UpsIdentModelfourth_Object = MibScalar
upsIdentModelfourth = _UpsIdentModelfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 2),
    _UpsIdentModelfourth_Type()
)
upsIdentModelfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelfourth.setStatus("current")
_UpsIdentUPSSoftwareVersionfourth_Type = DisplayString
_UpsIdentUPSSoftwareVersionfourth_Object = MibScalar
upsIdentUPSSoftwareVersionfourth = _UpsIdentUPSSoftwareVersionfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 3),
    _UpsIdentUPSSoftwareVersionfourth_Type()
)
upsIdentUPSSoftwareVersionfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersionfourth.setStatus("current")
_UpsIdentAgentSoftwareVersionfourth_Type = DisplayString
_UpsIdentAgentSoftwareVersionfourth_Object = MibScalar
upsIdentAgentSoftwareVersionfourth = _UpsIdentAgentSoftwareVersionfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 4),
    _UpsIdentAgentSoftwareVersionfourth_Type()
)
upsIdentAgentSoftwareVersionfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersionfourth.setStatus("current")
_UpsIdentNamefourth_Type = DisplayString
_UpsIdentNamefourth_Object = MibScalar
upsIdentNamefourth = _UpsIdentNamefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 5),
    _UpsIdentNamefourth_Type()
)
upsIdentNamefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNamefourth.setStatus("current")
_UpsIdentAttachedDevicesfourth_Type = DisplayString
_UpsIdentAttachedDevicesfourth_Object = MibScalar
upsIdentAttachedDevicesfourth = _UpsIdentAttachedDevicesfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 6),
    _UpsIdentAttachedDevicesfourth_Type()
)
upsIdentAttachedDevicesfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicesfourth.setStatus("current")
_UpsIdentUPSSerialNumberfourth_Type = DisplayString
_UpsIdentUPSSerialNumberfourth_Object = MibScalar
upsIdentUPSSerialNumberfourth = _UpsIdentUPSSerialNumberfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 7),
    _UpsIdentUPSSerialNumberfourth_Type()
)
upsIdentUPSSerialNumberfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumberfourth.setStatus("current")
_UpsIdentComProtVersionfourth_Type = DisplayString
_UpsIdentComProtVersionfourth_Object = MibScalar
upsIdentComProtVersionfourth = _UpsIdentComProtVersionfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 8),
    _UpsIdentComProtVersionfourth_Type()
)
upsIdentComProtVersionfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersionfourth.setStatus("current")
_UpsIdentOperatingTimefourth_Type = NonNegativeInteger32
_UpsIdentOperatingTimefourth_Object = MibScalar
upsIdentOperatingTimefourth = _UpsIdentOperatingTimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 1, 9),
    _UpsIdentOperatingTimefourth_Type()
)
upsIdentOperatingTimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimefourth.setUnits("fourths")
_UpsBatteryfourth_ObjectIdentity = ObjectIdentity
upsBatteryfourth = _UpsBatteryfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2)
)


class _UpsBatteryStatusfourth_Type(Integer32):
    """Custom type upsBatteryStatusfourth based on Integer32"""
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


_UpsBatteryStatusfourth_Type.__name__ = "Integer32"
_UpsBatteryStatusfourth_Object = MibScalar
upsBatteryStatusfourth = _UpsBatteryStatusfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 1),
    _UpsBatteryStatusfourth_Type()
)
upsBatteryStatusfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatusfourth.setStatus("current")
_UpsSecondsOnBatteryfourth_Type = Integer32
_UpsSecondsOnBatteryfourth_Object = MibScalar
upsSecondsOnBatteryfourth = _UpsSecondsOnBatteryfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 2),
    _UpsSecondsOnBatteryfourth_Type()
)
upsSecondsOnBatteryfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryfourth.setUnits("fourths")
_UpsEstimatedMinutesRemainingfourth_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingfourth_Object = MibScalar
upsEstimatedMinutesRemainingfourth = _UpsEstimatedMinutesRemainingfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 3),
    _UpsEstimatedMinutesRemainingfourth_Type()
)
upsEstimatedMinutesRemainingfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingfourth.setUnits("minutes")


class _UpsEstimatedChargeRemainingfourth_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingfourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingfourth_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingfourth_Object = MibScalar
upsEstimatedChargeRemainingfourth = _UpsEstimatedChargeRemainingfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 4),
    _UpsEstimatedChargeRemainingfourth_Type()
)
upsEstimatedChargeRemainingfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingfourth.setUnits("percent")
_UpsBatteryVoltagefourth_Type = NonNegativeInteger32
_UpsBatteryVoltagefourth_Object = MibScalar
upsBatteryVoltagefourth = _UpsBatteryVoltagefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 5),
    _UpsBatteryVoltagefourth_Type()
)
upsBatteryVoltagefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltagefourth.setUnits("0.1 Volt DC")
_UpsBatteryCurrentfourth_Type = Integer32
_UpsBatteryCurrentfourth_Object = MibScalar
upsBatteryCurrentfourth = _UpsBatteryCurrentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 6),
    _UpsBatteryCurrentfourth_Type()
)
upsBatteryCurrentfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentfourth.setUnits("0.1 Amp DC")
_UpsBatteryTemperaturefourth_Type = Integer32
_UpsBatteryTemperaturefourth_Object = MibScalar
upsBatteryTemperaturefourth = _UpsBatteryTemperaturefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 7),
    _UpsBatteryTemperaturefourth_Type()
)
upsBatteryTemperaturefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperaturefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperaturefourth.setUnits("degrees Centigrade")
_UpsBatteryRipplefourth_Type = Integer32
_UpsBatteryRipplefourth_Object = MibScalar
upsBatteryRipplefourth = _UpsBatteryRipplefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 2, 8),
    _UpsBatteryRipplefourth_Type()
)
upsBatteryRipplefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipplefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipplefourth.setUnits("0.1 Volt RMS")
_UpsInputfourth_ObjectIdentity = ObjectIdentity
upsInputfourth = _UpsInputfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3)
)
_UpsInputLineBadsfourth_Type = Counter32
_UpsInputLineBadsfourth_Object = MibScalar
upsInputLineBadsfourth = _UpsInputLineBadsfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 1),
    _UpsInputLineBadsfourth_Type()
)
upsInputLineBadsfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadsfourth.setStatus("current")
_UpsInputNumLinesfourth_Type = NonNegativeInteger32
_UpsInputNumLinesfourth_Object = MibScalar
upsInputNumLinesfourth = _UpsInputNumLinesfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 2),
    _UpsInputNumLinesfourth_Type()
)
upsInputNumLinesfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinesfourth.setStatus("current")
_UpsInputFourthTable_Object = MibTable
upsInputFourthTable = _UpsInputFourthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputFourthTable.setStatus("current")
_UpsInputFourthEntry_Object = MibTableRow
upsInputFourthEntry = _UpsInputFourthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1)
)
upsInputFourthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexfourth"),
)
if mibBuilder.loadTexts:
    upsInputFourthEntry.setStatus("current")
_UpsInputLineIndexfourth_Type = PositiveInteger32
_UpsInputLineIndexfourth_Object = MibTableColumn
upsInputLineIndexfourth = _UpsInputLineIndexfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1, 1),
    _UpsInputLineIndexfourth_Type()
)
upsInputLineIndexfourth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexfourth.setStatus("current")
_UpsInputFrequencyfourth_Type = NonNegativeInteger32
_UpsInputFrequencyfourth_Object = MibTableColumn
upsInputFrequencyfourth = _UpsInputFrequencyfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1, 2),
    _UpsInputFrequencyfourth_Type()
)
upsInputFrequencyfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyfourth.setUnits("0.1 Hertz")
_UpsInputVoltagefourth_Type = NonNegativeInteger32
_UpsInputVoltagefourth_Object = MibTableColumn
upsInputVoltagefourth = _UpsInputVoltagefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1, 3),
    _UpsInputVoltagefourth_Type()
)
upsInputVoltagefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltagefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltagefourth.setUnits("RMS Volts")
_UpsInputCurrentfourth_Type = NonNegativeInteger32
_UpsInputCurrentfourth_Object = MibTableColumn
upsInputCurrentfourth = _UpsInputCurrentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1, 4),
    _UpsInputCurrentfourth_Type()
)
upsInputCurrentfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentfourth.setUnits("0.1 RMS Amp")
_UpsInputTruePowerfourth_Type = NonNegativeInteger32
_UpsInputTruePowerfourth_Object = MibTableColumn
upsInputTruePowerfourth = _UpsInputTruePowerfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1, 5),
    _UpsInputTruePowerfourth_Type()
)
upsInputTruePowerfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowerfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowerfourth.setUnits("Watts")
_UpsInputVoltageMinfourth_Type = NonNegativeInteger32
_UpsInputVoltageMinfourth_Object = MibTableColumn
upsInputVoltageMinfourth = _UpsInputVoltageMinfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1, 6),
    _UpsInputVoltageMinfourth_Type()
)
upsInputVoltageMinfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMinfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMinfourth.setUnits("RMS Volts")
_UpsInputVoltageMaxfourth_Type = NonNegativeInteger32
_UpsInputVoltageMaxfourth_Object = MibTableColumn
upsInputVoltageMaxfourth = _UpsInputVoltageMaxfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 3, 3, 1, 7),
    _UpsInputVoltageMaxfourth_Type()
)
upsInputVoltageMaxfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxfourth.setUnits("RMS Volts")
_UpsOutputfourth_ObjectIdentity = ObjectIdentity
upsOutputfourth = _UpsOutputfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4)
)


class _UpsOutputSourcefourth_Type(Integer32):
    """Custom type upsOutputSourcefourth based on Integer32"""
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


_UpsOutputSourcefourth_Type.__name__ = "Integer32"
_UpsOutputSourcefourth_Object = MibScalar
upsOutputSourcefourth = _UpsOutputSourcefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 1),
    _UpsOutputSourcefourth_Type()
)
upsOutputSourcefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourcefourth.setStatus("current")
_UpsOutputFrequencyfourth_Type = NonNegativeInteger32
_UpsOutputFrequencyfourth_Object = MibScalar
upsOutputFrequencyfourth = _UpsOutputFrequencyfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 2),
    _UpsOutputFrequencyfourth_Type()
)
upsOutputFrequencyfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencyfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencyfourth.setUnits("0.1 Hertz")
_UpsOutputNumLinesfourth_Type = NonNegativeInteger32
_UpsOutputNumLinesfourth_Object = MibScalar
upsOutputNumLinesfourth = _UpsOutputNumLinesfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 3),
    _UpsOutputNumLinesfourth_Type()
)
upsOutputNumLinesfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinesfourth.setStatus("current")
_UpsOutputFourthTable_Object = MibTable
upsOutputFourthTable = _UpsOutputFourthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputFourthTable.setStatus("current")
_UpsOutputFourthEntry_Object = MibTableRow
upsOutputFourthEntry = _UpsOutputFourthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1)
)
upsOutputFourthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexfourth"),
)
if mibBuilder.loadTexts:
    upsOutputFourthEntry.setStatus("current")
_UpsOutputLineIndexfourth_Type = PositiveInteger32
_UpsOutputLineIndexfourth_Object = MibTableColumn
upsOutputLineIndexfourth = _UpsOutputLineIndexfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 1),
    _UpsOutputLineIndexfourth_Type()
)
upsOutputLineIndexfourth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexfourth.setStatus("current")
_UpsOutputVoltagefourth_Type = NonNegativeInteger32
_UpsOutputVoltagefourth_Object = MibTableColumn
upsOutputVoltagefourth = _UpsOutputVoltagefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 2),
    _UpsOutputVoltagefourth_Type()
)
upsOutputVoltagefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltagefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltagefourth.setUnits("RMS Volts")
_UpsOutputCurrentfourth_Type = NonNegativeInteger32
_UpsOutputCurrentfourth_Object = MibTableColumn
upsOutputCurrentfourth = _UpsOutputCurrentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 3),
    _UpsOutputCurrentfourth_Type()
)
upsOutputCurrentfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentfourth.setUnits("0.1 RMS Amp")
_UpsOutputPowerfourth_Type = NonNegativeInteger32
_UpsOutputPowerfourth_Object = MibTableColumn
upsOutputPowerfourth = _UpsOutputPowerfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 4),
    _UpsOutputPowerfourth_Type()
)
upsOutputPowerfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerfourth.setUnits("Watts")


class _UpsOutputPercentLoadfourth_Type(Integer32):
    """Custom type upsOutputPercentLoadfourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadfourth_Type.__name__ = "Integer32"
_UpsOutputPercentLoadfourth_Object = MibTableColumn
upsOutputPercentLoadfourth = _UpsOutputPercentLoadfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 5),
    _UpsOutputPercentLoadfourth_Type()
)
upsOutputPercentLoadfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadfourth.setUnits("percent")


class _UpsOutputPowerFactorfourth_Type(Integer32):
    """Custom type upsOutputPowerFactorfourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorfourth_Type.__name__ = "Integer32"
_UpsOutputPowerFactorfourth_Object = MibTableColumn
upsOutputPowerFactorfourth = _UpsOutputPowerFactorfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 6),
    _UpsOutputPowerFactorfourth_Type()
)
upsOutputPowerFactorfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorfourth.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentfourth_Type = Integer32
_UpsOutputPeakCurrentfourth_Object = MibTableColumn
upsOutputPeakCurrentfourth = _UpsOutputPeakCurrentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 7),
    _UpsOutputPeakCurrentfourth_Type()
)
upsOutputPeakCurrentfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentfourth.setUnits("Amps")
_UpsOutputShareCurrentfourth_Type = Integer32
_UpsOutputShareCurrentfourth_Object = MibTableColumn
upsOutputShareCurrentfourth = _UpsOutputShareCurrentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 4, 4, 1, 8),
    _UpsOutputShareCurrentfourth_Type()
)
upsOutputShareCurrentfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentfourth.setUnits("Amps")
_UpsBypassfourth_ObjectIdentity = ObjectIdentity
upsBypassfourth = _UpsBypassfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5)
)
_UpsBypassFrequencyfourth_Type = NonNegativeInteger32
_UpsBypassFrequencyfourth_Object = MibScalar
upsBypassFrequencyfourth = _UpsBypassFrequencyfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 1),
    _UpsBypassFrequencyfourth_Type()
)
upsBypassFrequencyfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencyfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencyfourth.setUnits("0.1 Hertz")
_UpsBypassNumLinesfourth_Type = NonNegativeInteger32
_UpsBypassNumLinesfourth_Object = MibScalar
upsBypassNumLinesfourth = _UpsBypassNumLinesfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 2),
    _UpsBypassNumLinesfourth_Type()
)
upsBypassNumLinesfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinesfourth.setStatus("current")
_UpsBypassFourthTable_Object = MibTable
upsBypassFourthTable = _UpsBypassFourthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassFourthTable.setStatus("current")
_UpsBypassFourthEntry_Object = MibTableRow
upsBypassFourthEntry = _UpsBypassFourthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 3, 1)
)
upsBypassFourthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexfourth"),
)
if mibBuilder.loadTexts:
    upsBypassFourthEntry.setStatus("current")
_UpsBypassLineIndexfourth_Type = PositiveInteger32
_UpsBypassLineIndexfourth_Object = MibTableColumn
upsBypassLineIndexfourth = _UpsBypassLineIndexfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 3, 1, 1),
    _UpsBypassLineIndexfourth_Type()
)
upsBypassLineIndexfourth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexfourth.setStatus("current")
_UpsBypassVoltagefourth_Type = NonNegativeInteger32
_UpsBypassVoltagefourth_Object = MibTableColumn
upsBypassVoltagefourth = _UpsBypassVoltagefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 3, 1, 2),
    _UpsBypassVoltagefourth_Type()
)
upsBypassVoltagefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltagefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltagefourth.setUnits("RMS Volts")
_UpsBypassCurrentfourth_Type = NonNegativeInteger32
_UpsBypassCurrentfourth_Object = MibTableColumn
upsBypassCurrentfourth = _UpsBypassCurrentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 3, 1, 3),
    _UpsBypassCurrentfourth_Type()
)
upsBypassCurrentfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentfourth.setUnits("0.1 RMS Amp")
_UpsBypassPowerfourth_Type = NonNegativeInteger32
_UpsBypassPowerfourth_Object = MibTableColumn
upsBypassPowerfourth = _UpsBypassPowerfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 5, 3, 1, 4),
    _UpsBypassPowerfourth_Type()
)
upsBypassPowerfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowerfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowerfourth.setUnits("Watts")
_UpsAlarmfourth_ObjectIdentity = ObjectIdentity
upsAlarmfourth = _UpsAlarmfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6)
)
_UpsAlarmsPresentfourth_Type = Gauge32
_UpsAlarmsPresentfourth_Object = MibScalar
upsAlarmsPresentfourth = _UpsAlarmsPresentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 1),
    _UpsAlarmsPresentfourth_Type()
)
upsAlarmsPresentfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentfourth.setStatus("current")
_UpsAlarmFourthTable_Object = MibTable
upsAlarmFourthTable = _UpsAlarmFourthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmFourthTable.setStatus("current")
_UpsAlarmFourthEntry_Object = MibTableRow
upsAlarmFourthEntry = _UpsAlarmFourthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 2, 1)
)
upsAlarmFourthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdfourth"),
)
if mibBuilder.loadTexts:
    upsAlarmFourthEntry.setStatus("current")
_UpsAlarmIdfourth_Type = PositiveInteger32
_UpsAlarmIdfourth_Object = MibTableColumn
upsAlarmIdfourth = _UpsAlarmIdfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 2, 1, 1),
    _UpsAlarmIdfourth_Type()
)
upsAlarmIdfourth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdfourth.setStatus("current")
_UpsAlarmDescrfourth_Type = AutonomousType
_UpsAlarmDescrfourth_Object = MibTableColumn
upsAlarmDescrfourth = _UpsAlarmDescrfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 2, 1, 2),
    _UpsAlarmDescrfourth_Type()
)
upsAlarmDescrfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrfourth.setStatus("current")
_UpsAlarmTimefourth_Type = TimeStamp
_UpsAlarmTimefourth_Object = MibTableColumn
upsAlarmTimefourth = _UpsAlarmTimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 2, 1, 3),
    _UpsAlarmTimefourth_Type()
)
upsAlarmTimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimefourth.setStatus("current")
_UpsWellKnownAlarmsfourth_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmsfourth = _UpsWellKnownAlarmsfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3)
)
_UpsAlarmBatteryBadfourth_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadfourth = _UpsAlarmBatteryBadfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadfourth.setStatus("current")
_UpsAlarmOnBatteryfourth_ObjectIdentity = ObjectIdentity
upsAlarmOnBatteryfourth = _UpsAlarmOnBatteryfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatteryfourth.setStatus("current")
_UpsAlarmLowBatteryfourth_ObjectIdentity = ObjectIdentity
upsAlarmLowBatteryfourth = _UpsAlarmLowBatteryfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatteryfourth.setStatus("current")
_UpsAlarmDepletedBatteryfourth_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatteryfourth = _UpsAlarmDepletedBatteryfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatteryfourth.setStatus("current")
_UpsAlarmTempBadfourth_ObjectIdentity = ObjectIdentity
upsAlarmTempBadfourth = _UpsAlarmTempBadfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadfourth.setStatus("current")
_UpsAlarmInputBadfourth_ObjectIdentity = ObjectIdentity
upsAlarmInputBadfourth = _UpsAlarmInputBadfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadfourth.setStatus("current")
_UpsAlarmOutputBadfourth_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadfourth = _UpsAlarmOutputBadfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadfourth.setStatus("current")
_UpsAlarmOutputOverloadfourth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadfourth = _UpsAlarmOutputOverloadfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadfourth.setStatus("current")
_UpsAlarmOnBypassfourth_ObjectIdentity = ObjectIdentity
upsAlarmOnBypassfourth = _UpsAlarmOnBypassfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypassfourth.setStatus("current")
_UpsAlarmBypassBadfourth_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadfourth = _UpsAlarmBypassBadfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadfourth.setStatus("current")
_UpsAlarmOutputOffAsRequestedfourth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedfourth = _UpsAlarmOutputOffAsRequestedfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedfourth.setStatus("current")
_UpsAlarmUpsOffAsRequestedfourth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedfourth = _UpsAlarmUpsOffAsRequestedfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedfourth.setStatus("current")
_UpsAlarmChargerFailedfourth_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedfourth = _UpsAlarmChargerFailedfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedfourth.setStatus("current")
_UpsAlarmUpsOutputOfffourth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOfffourth = _UpsAlarmUpsOutputOfffourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOfffourth.setStatus("current")
_UpsAlarmUpsSystemOfffourth_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOfffourth = _UpsAlarmUpsSystemOfffourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOfffourth.setStatus("current")
_UpsAlarmFanFailurefourth_ObjectIdentity = ObjectIdentity
upsAlarmFanFailurefourth = _UpsAlarmFanFailurefourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailurefourth.setStatus("current")
_UpsAlarmFuseFailurefourth_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailurefourth = _UpsAlarmFuseFailurefourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailurefourth.setStatus("current")
_UpsAlarmGeneralFaultfourth_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultfourth = _UpsAlarmGeneralFaultfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultfourth.setStatus("current")
_UpsAlarmDiagnosticTestFailedfourth_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedfourth = _UpsAlarmDiagnosticTestFailedfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedfourth.setStatus("current")
_UpsAlarmCommunicationsLostfourth_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostfourth = _UpsAlarmCommunicationsLostfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostfourth.setStatus("current")
_UpsAlarmAwaitingPowerfourth_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowerfourth = _UpsAlarmAwaitingPowerfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowerfourth.setStatus("current")
_UpsAlarmShutdownPendingfourth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingfourth = _UpsAlarmShutdownPendingfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingfourth.setStatus("current")
_UpsAlarmShutdownImminentfourth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentfourth = _UpsAlarmShutdownImminentfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentfourth.setStatus("current")
_UpsAlarmTestInProgressfourth_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgressfourth = _UpsAlarmTestInProgressfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgressfourth.setStatus("current")
_UpsAlarmReceptacleOfffourth_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOfffourth = _UpsAlarmReceptacleOfffourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOfffourth.setStatus("current")
_UpsAlarmHighSpeedBusFailurefourth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailurefourth = _UpsAlarmHighSpeedBusFailurefourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailurefourth.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailurefourth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailurefourth = _UpsAlarmHighSpeedBusJACRCFailurefourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailurefourth.setStatus("current")
_UpsAlarmConnectivityBusFailurefourth_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailurefourth = _UpsAlarmConnectivityBusFailurefourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailurefourth.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailurefourth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailurefourth = _UpsAlarmHighSpeedBusJBCRCFailurefourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailurefourth.setStatus("current")
_UpsAlarmCurrentSharingfourth_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingfourth = _UpsAlarmCurrentSharingfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingfourth.setStatus("current")
_UpsAlarmDCRipplefourth_ObjectIdentity = ObjectIdentity
upsAlarmDCRipplefourth = _UpsAlarmDCRipplefourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipplefourth.setStatus("current")
_UpsAlarmMaskAfourth_Type = Unsigned32
_UpsAlarmMaskAfourth_Object = MibScalar
upsAlarmMaskAfourth = _UpsAlarmMaskAfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 6, 4),
    _UpsAlarmMaskAfourth_Type()
)
upsAlarmMaskAfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAfourth.setStatus("current")
_UpsTestfourth_ObjectIdentity = ObjectIdentity
upsTestfourth = _UpsTestfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7)
)
_UpsTestIdfourth_Type = ObjectIdentifier
_UpsTestIdfourth_Object = MibScalar
upsTestIdfourth = _UpsTestIdfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 1),
    _UpsTestIdfourth_Type()
)
upsTestIdfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdfourth.setStatus("current")
_UpsTestSpinLockfourth_Type = TestAndIncr
_UpsTestSpinLockfourth_Object = MibScalar
upsTestSpinLockfourth = _UpsTestSpinLockfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 2),
    _UpsTestSpinLockfourth_Type()
)
upsTestSpinLockfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLockfourth.setStatus("current")


class _UpsTestResultsSummaryfourth_Type(Integer32):
    """Custom type upsTestResultsSummaryfourth based on Integer32"""
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


_UpsTestResultsSummaryfourth_Type.__name__ = "Integer32"
_UpsTestResultsSummaryfourth_Object = MibScalar
upsTestResultsSummaryfourth = _UpsTestResultsSummaryfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 3),
    _UpsTestResultsSummaryfourth_Type()
)
upsTestResultsSummaryfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummaryfourth.setStatus("current")
_UpsTestResultsDetailfourth_Type = DisplayString
_UpsTestResultsDetailfourth_Object = MibScalar
upsTestResultsDetailfourth = _UpsTestResultsDetailfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 4),
    _UpsTestResultsDetailfourth_Type()
)
upsTestResultsDetailfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailfourth.setStatus("current")
_UpsTestStartTimefourth_Type = TimeStamp
_UpsTestStartTimefourth_Object = MibScalar
upsTestStartTimefourth = _UpsTestStartTimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 5),
    _UpsTestStartTimefourth_Type()
)
upsTestStartTimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimefourth.setStatus("current")
_UpsTestElapsedTimefourth_Type = TimeInterval
_UpsTestElapsedTimefourth_Object = MibScalar
upsTestElapsedTimefourth = _UpsTestElapsedTimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 6),
    _UpsTestElapsedTimefourth_Type()
)
upsTestElapsedTimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimefourth.setStatus("current")
_UpsWellKnownTestsfourth_ObjectIdentity = ObjectIdentity
upsWellKnownTestsfourth = _UpsWellKnownTestsfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 7)
)
_UpsTestNoTestsInitiatedfourth_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedfourth = _UpsTestNoTestsInitiatedfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedfourth.setStatus("current")
_UpsTestAbortTestInProgressfourth_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgressfourth = _UpsTestAbortTestInProgressfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgressfourth.setStatus("current")
_UpsTestGeneralSystemsTestfourth_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestfourth = _UpsTestGeneralSystemsTestfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestfourth.setStatus("current")
_UpsTestQuickBatteryTestfourth_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestfourth = _UpsTestQuickBatteryTestfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestfourth.setStatus("current")
_UpsTestDeepBatteryCalibrationfourth_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationfourth = _UpsTestDeepBatteryCalibrationfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationfourth.setStatus("current")
_UpsControlfourth_ObjectIdentity = ObjectIdentity
upsControlfourth = _UpsControlfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8)
)


class _UpsShutdownTypefourth_Type(Integer32):
    """Custom type upsShutdownTypefourth based on Integer32"""
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


_UpsShutdownTypefourth_Type.__name__ = "Integer32"
_UpsShutdownTypefourth_Object = MibScalar
upsShutdownTypefourth = _UpsShutdownTypefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 1),
    _UpsShutdownTypefourth_Type()
)
upsShutdownTypefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypefourth.setStatus("current")


class _UpsShutdownAfterDelayfourth_Type(Integer32):
    """Custom type upsShutdownAfterDelayfourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelayfourth_Type.__name__ = "Integer32"
_UpsShutdownAfterDelayfourth_Object = MibScalar
upsShutdownAfterDelayfourth = _UpsShutdownAfterDelayfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 2),
    _UpsShutdownAfterDelayfourth_Type()
)
upsShutdownAfterDelayfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayfourth.setUnits("fourths")


class _UpsStartupAfterDelayfourth_Type(Integer32):
    """Custom type upsStartupAfterDelayfourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelayfourth_Type.__name__ = "Integer32"
_UpsStartupAfterDelayfourth_Object = MibScalar
upsStartupAfterDelayfourth = _UpsStartupAfterDelayfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 3),
    _UpsStartupAfterDelayfourth_Type()
)
upsStartupAfterDelayfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelayfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelayfourth.setUnits("fourths")


class _UpsRebootWithDurationfourth_Type(Integer32):
    """Custom type upsRebootWithDurationfourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationfourth_Type.__name__ = "Integer32"
_UpsRebootWithDurationfourth_Object = MibScalar
upsRebootWithDurationfourth = _UpsRebootWithDurationfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 4),
    _UpsRebootWithDurationfourth_Type()
)
upsRebootWithDurationfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationfourth.setUnits("fourths")


class _UpsAutoRestartfourth_Type(Integer32):
    """Custom type upsAutoRestartfourth based on Integer32"""
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


_UpsAutoRestartfourth_Type.__name__ = "Integer32"
_UpsAutoRestartfourth_Object = MibScalar
upsAutoRestartfourth = _UpsAutoRestartfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 5),
    _UpsAutoRestartfourth_Type()
)
upsAutoRestartfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartfourth.setStatus("current")
_UpsReceptaclesNumfourth_Type = NonNegativeInteger32
_UpsReceptaclesNumfourth_Object = MibScalar
upsReceptaclesNumfourth = _UpsReceptaclesNumfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 6),
    _UpsReceptaclesNumfourth_Type()
)
upsReceptaclesNumfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumfourth.setStatus("current")
_UpsReceptacleFourthTable_Object = MibTable
upsReceptacleFourthTable = _UpsReceptacleFourthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleFourthTable.setStatus("current")
_UpsReceptacleFourthEntry_Object = MibTableRow
upsReceptacleFourthEntry = _UpsReceptacleFourthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 7, 1)
)
upsReceptacleFourthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexfourth"),
)
if mibBuilder.loadTexts:
    upsReceptacleFourthEntry.setStatus("current")
_UpsReceptacleLineIndexfourth_Type = PositiveInteger32
_UpsReceptacleLineIndexfourth_Object = MibTableColumn
upsReceptacleLineIndexfourth = _UpsReceptacleLineIndexfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 7, 1, 1),
    _UpsReceptacleLineIndexfourth_Type()
)
upsReceptacleLineIndexfourth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexfourth.setStatus("current")


class _UpsReceptacleOnOfffourth_Type(Integer32):
    """Custom type upsReceptacleOnOfffourth based on Integer32"""
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


_UpsReceptacleOnOfffourth_Type.__name__ = "Integer32"
_UpsReceptacleOnOfffourth_Object = MibTableColumn
upsReceptacleOnOfffourth = _UpsReceptacleOnOfffourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 7, 1, 2),
    _UpsReceptacleOnOfffourth_Type()
)
upsReceptacleOnOfffourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOfffourth.setStatus("current")


class _UpsUPSModefourth_Type(Integer32):
    """Custom type upsUPSModefourth based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModefourth_Type.__name__ = "Integer32"
_UpsUPSModefourth_Object = MibScalar
upsUPSModefourth = _UpsUPSModefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 8),
    _UpsUPSModefourth_Type()
)
upsUPSModefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModefourth.setStatus("current")


class _UpsRectifierOnOfffourth_Type(Integer32):
    """Custom type upsRectifierOnOfffourth based on Integer32"""
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


_UpsRectifierOnOfffourth_Type.__name__ = "Integer32"
_UpsRectifierOnOfffourth_Object = MibScalar
upsRectifierOnOfffourth = _UpsRectifierOnOfffourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 9),
    _UpsRectifierOnOfffourth_Type()
)
upsRectifierOnOfffourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOfffourth.setStatus("current")


class _UpsBatteryChargeMethodfourth_Type(Integer32):
    """Custom type upsBatteryChargeMethodfourth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodfourth_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodfourth_Object = MibScalar
upsBatteryChargeMethodfourth = _UpsBatteryChargeMethodfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 10),
    _UpsBatteryChargeMethodfourth_Type()
)
upsBatteryChargeMethodfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodfourth.setStatus("current")


class _UpsInverterOnOfffourth_Type(Integer32):
    """Custom type upsInverterOnOfffourth based on Integer32"""
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


_UpsInverterOnOfffourth_Type.__name__ = "Integer32"
_UpsInverterOnOfffourth_Object = MibScalar
upsInverterOnOfffourth = _UpsInverterOnOfffourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 11),
    _UpsInverterOnOfffourth_Type()
)
upsInverterOnOfffourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOfffourth.setStatus("current")


class _UpsBypassOnOfffourth_Type(Integer32):
    """Custom type upsBypassOnOfffourth based on Integer32"""
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


_UpsBypassOnOfffourth_Type.__name__ = "Integer32"
_UpsBypassOnOfffourth_Object = MibScalar
upsBypassOnOfffourth = _UpsBypassOnOfffourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 12),
    _UpsBypassOnOfffourth_Type()
)
upsBypassOnOfffourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOfffourth.setStatus("current")


class _UpsLoadSourcefourth_Type(Integer32):
    """Custom type upsLoadSourcefourth based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourcefourth_Type.__name__ = "Integer32"
_UpsLoadSourcefourth_Object = MibScalar
upsLoadSourcefourth = _UpsLoadSourcefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 8, 13),
    _UpsLoadSourcefourth_Type()
)
upsLoadSourcefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourcefourth.setStatus("current")
_UpsConfigfourth_ObjectIdentity = ObjectIdentity
upsConfigfourth = _UpsConfigfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9)
)
_UpsConfigInputVoltagefourth_Type = NonNegativeInteger32
_UpsConfigInputVoltagefourth_Object = MibScalar
upsConfigInputVoltagefourth = _UpsConfigInputVoltagefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 1),
    _UpsConfigInputVoltagefourth_Type()
)
upsConfigInputVoltagefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltagefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltagefourth.setUnits("RMS Volts")
_UpsConfigInputFreqfourth_Type = NonNegativeInteger32
_UpsConfigInputFreqfourth_Object = MibScalar
upsConfigInputFreqfourth = _UpsConfigInputFreqfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 2),
    _UpsConfigInputFreqfourth_Type()
)
upsConfigInputFreqfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqfourth.setUnits("0.1 Hertz")
_UpsConfigOutputVoltagefourth_Type = NonNegativeInteger32
_UpsConfigOutputVoltagefourth_Object = MibScalar
upsConfigOutputVoltagefourth = _UpsConfigOutputVoltagefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 3),
    _UpsConfigOutputVoltagefourth_Type()
)
upsConfigOutputVoltagefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagefourth.setUnits("RMS Volts")
_UpsConfigOutputFreqfourth_Type = NonNegativeInteger32
_UpsConfigOutputFreqfourth_Object = MibScalar
upsConfigOutputFreqfourth = _UpsConfigOutputFreqfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 4),
    _UpsConfigOutputFreqfourth_Type()
)
upsConfigOutputFreqfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqfourth.setUnits("0.1 Hertz")
_UpsConfigOutputVAfourth_Type = NonNegativeInteger32
_UpsConfigOutputVAfourth_Object = MibScalar
upsConfigOutputVAfourth = _UpsConfigOutputVAfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 5),
    _UpsConfigOutputVAfourth_Type()
)
upsConfigOutputVAfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAfourth.setUnits("Volt-Amps")
_UpsConfigOutputPowerfourth_Type = NonNegativeInteger32
_UpsConfigOutputPowerfourth_Object = MibScalar
upsConfigOutputPowerfourth = _UpsConfigOutputPowerfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 6),
    _UpsConfigOutputPowerfourth_Type()
)
upsConfigOutputPowerfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowerfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowerfourth.setUnits("Watts")
_UpsConfigLowBattTimefourth_Type = NonNegativeInteger32
_UpsConfigLowBattTimefourth_Object = MibScalar
upsConfigLowBattTimefourth = _UpsConfigLowBattTimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 7),
    _UpsConfigLowBattTimefourth_Type()
)
upsConfigLowBattTimefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimefourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimefourth.setUnits("minutes")


class _UpsConfigAudibleStatusfourth_Type(Integer32):
    """Custom type upsConfigAudibleStatusfourth based on Integer32"""
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


_UpsConfigAudibleStatusfourth_Type.__name__ = "Integer32"
_UpsConfigAudibleStatusfourth_Object = MibScalar
upsConfigAudibleStatusfourth = _UpsConfigAudibleStatusfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 8),
    _UpsConfigAudibleStatusfourth_Type()
)
upsConfigAudibleStatusfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatusfourth.setStatus("current")
_UpsConfigLowVoltageTransferPointfourth_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointfourth_Object = MibScalar
upsConfigLowVoltageTransferPointfourth = _UpsConfigLowVoltageTransferPointfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 9),
    _UpsConfigLowVoltageTransferPointfourth_Type()
)
upsConfigLowVoltageTransferPointfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointfourth.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointfourth_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointfourth_Object = MibScalar
upsConfigHighVoltageTransferPointfourth = _UpsConfigHighVoltageTransferPointfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 10),
    _UpsConfigHighVoltageTransferPointfourth_Type()
)
upsConfigHighVoltageTransferPointfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointfourth.setUnits("RMS Volts")
_UpsConfigBatteryCapacityfourth_Type = NonNegativeInteger32
_UpsConfigBatteryCapacityfourth_Object = MibScalar
upsConfigBatteryCapacityfourth = _UpsConfigBatteryCapacityfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 11),
    _UpsConfigBatteryCapacityfourth_Type()
)
upsConfigBatteryCapacityfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityfourth.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentfourth_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentfourth_Object = MibScalar
upsConfigBatteryChargeCurrentfourth = _UpsConfigBatteryChargeCurrentfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 12),
    _UpsConfigBatteryChargeCurrentfourth_Type()
)
upsConfigBatteryChargeCurrentfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentfourth.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdownfourth_Type(Integer32):
    """Custom type upsConfigNoLoadShutdownfourth based on Integer32"""
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


_UpsConfigNoLoadShutdownfourth_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdownfourth_Object = MibScalar
upsConfigNoLoadShutdownfourth = _UpsConfigNoLoadShutdownfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 13),
    _UpsConfigNoLoadShutdownfourth_Type()
)
upsConfigNoLoadShutdownfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdownfourth.setStatus("current")
_UpsConfigStartDelayfourth_Type = PositiveInteger32
_UpsConfigStartDelayfourth_Object = MibScalar
upsConfigStartDelayfourth = _UpsConfigStartDelayfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 9, 14),
    _UpsConfigStartDelayfourth_Type()
)
upsConfigStartDelayfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelayfourth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelayfourth.setUnits("minutes")
_UpsGetSetfourth_ObjectIdentity = ObjectIdentity
upsGetSetfourth = _UpsGetSetfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10)
)
_UpsEventGetNextfourth_Type = PositiveInteger32
_UpsEventGetNextfourth_Object = MibScalar
upsEventGetNextfourth = _UpsEventGetNextfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 1),
    _UpsEventGetNextfourth_Type()
)
upsEventGetNextfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextfourth.setStatus("current")
_UpsEventGetPreviousfourth_Type = PositiveInteger32
_UpsEventGetPreviousfourth_Object = MibScalar
upsEventGetPreviousfourth = _UpsEventGetPreviousfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 2),
    _UpsEventGetPreviousfourth_Type()
)
upsEventGetPreviousfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPreviousfourth.setStatus("current")
_UpsEventSetStartingTimeStampfourth_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampfourth_Object = MibScalar
upsEventSetStartingTimeStampfourth = _UpsEventSetStartingTimeStampfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 3),
    _UpsEventSetStartingTimeStampfourth_Type()
)
upsEventSetStartingTimeStampfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampfourth.setStatus("current")
_UpsEventRetreiveCurrentTimeStampfourth_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampfourth_Object = MibScalar
upsEventRetreiveCurrentTimeStampfourth = _UpsEventRetreiveCurrentTimeStampfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 4),
    _UpsEventRetreiveCurrentTimeStampfourth_Type()
)
upsEventRetreiveCurrentTimeStampfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampfourth.setStatus("current")
_UpsEventTableSizefourth_Type = NonNegativeInteger32
_UpsEventTableSizefourth_Object = MibScalar
upsEventTableSizefourth = _UpsEventTableSizefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 5),
    _UpsEventTableSizefourth_Type()
)
upsEventTableSizefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizefourth.setStatus("current")
_UpsEventFourthTable_Object = MibTable
upsEventFourthTable = _UpsEventFourthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventFourthTable.setStatus("current")
_UpsEventFourthEntry_Object = MibTableRow
upsEventFourthEntry = _UpsEventFourthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 6, 1)
)
upsEventFourthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexfourth"),
)
if mibBuilder.loadTexts:
    upsEventFourthEntry.setStatus("current")
_UpsEventLineIndexfourth_Type = PositiveInteger32
_UpsEventLineIndexfourth_Object = MibTableColumn
upsEventLineIndexfourth = _UpsEventLineIndexfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 6, 1, 1),
    _UpsEventLineIndexfourth_Type()
)
upsEventLineIndexfourth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexfourth.setStatus("current")
_UpsEventCodefourth_Type = Integer32
_UpsEventCodefourth_Object = MibTableColumn
upsEventCodefourth = _UpsEventCodefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 6, 1, 2),
    _UpsEventCodefourth_Type()
)
upsEventCodefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodefourth.setStatus("current")
_UpsEventStatusfourth_Type = NonNegativeInteger32
_UpsEventStatusfourth_Object = MibTableColumn
upsEventStatusfourth = _UpsEventStatusfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 6, 1, 3),
    _UpsEventStatusfourth_Type()
)
upsEventStatusfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatusfourth.setStatus("current")
_UpsEventTimefourth_Type = NonNegativeInteger32
_UpsEventTimefourth_Object = MibTableColumn
upsEventTimefourth = _UpsEventTimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 6, 1, 4),
    _UpsEventTimefourth_Type()
)
upsEventTimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimefourth.setStatus("current")
_UpsParametersReadfourth_Type = PositiveInteger32
_UpsParametersReadfourth_Object = MibScalar
upsParametersReadfourth = _UpsParametersReadfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 7),
    _UpsParametersReadfourth_Type()
)
upsParametersReadfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadfourth.setStatus("current")
_UpsParametersWritefourth_Type = PositiveInteger32
_UpsParametersWritefourth_Object = MibScalar
upsParametersWritefourth = _UpsParametersWritefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 8),
    _UpsParametersWritefourth_Type()
)
upsParametersWritefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWritefourth.setStatus("current")
_UpsParametersStartAddressfourth_Type = NonNegativeInteger32
_UpsParametersStartAddressfourth_Object = MibScalar
upsParametersStartAddressfourth = _UpsParametersStartAddressfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 9),
    _UpsParametersStartAddressfourth_Type()
)
upsParametersStartAddressfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddressfourth.setStatus("current")
_UpsParameterTableSizefourth_Type = NonNegativeInteger32
_UpsParameterTableSizefourth_Object = MibScalar
upsParameterTableSizefourth = _UpsParameterTableSizefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 10),
    _UpsParameterTableSizefourth_Type()
)
upsParameterTableSizefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizefourth.setStatus("current")
_UpsParameterFourthTable_Object = MibTable
upsParameterFourthTable = _UpsParameterFourthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterFourthTable.setStatus("current")
_UpsParameterFourthEntry_Object = MibTableRow
upsParameterFourthEntry = _UpsParameterFourthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 11, 1)
)
upsParameterFourthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexfourth"),
)
if mibBuilder.loadTexts:
    upsParameterFourthEntry.setStatus("current")
_UpsParameterLineIndexfourth_Type = PositiveInteger32
_UpsParameterLineIndexfourth_Object = MibTableColumn
upsParameterLineIndexfourth = _UpsParameterLineIndexfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 11, 1, 1),
    _UpsParameterLineIndexfourth_Type()
)
upsParameterLineIndexfourth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexfourth.setStatus("current")
_UpsParameterValuefourth_Type = Integer32
_UpsParameterValuefourth_Object = MibTableColumn
upsParameterValuefourth = _UpsParameterValuefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 11, 1, 2),
    _UpsParameterValuefourth_Type()
)
upsParameterValuefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValuefourth.setStatus("current")
_UpsStatusfourth_Type = NonNegativeInteger32
_UpsStatusfourth_Object = MibScalar
upsStatusfourth = _UpsStatusfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 12),
    _UpsStatusfourth_Type()
)
upsStatusfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusfourth.setStatus("current")
_UpsMainsStatisticsMBfailfourth_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailfourth_Object = MibScalar
upsMainsStatisticsMBfailfourth = _UpsMainsStatisticsMBfailfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 13),
    _UpsMainsStatisticsMBfailfourth_Type()
)
upsMainsStatisticsMBfailfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailfourth.setStatus("current")
_UpsMainsStatisticsMRfailfourth_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailfourth_Object = MibScalar
upsMainsStatisticsMRfailfourth = _UpsMainsStatisticsMRfailfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 14),
    _UpsMainsStatisticsMRfailfourth_Type()
)
upsMainsStatisticsMRfailfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailfourth.setStatus("current")
_UpsMainsStatisticsB2fourth_Type = NonNegativeInteger32
_UpsMainsStatisticsB2fourth_Object = MibScalar
upsMainsStatisticsB2fourth = _UpsMainsStatisticsB2fourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 15),
    _UpsMainsStatisticsB2fourth_Type()
)
upsMainsStatisticsB2fourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2fourth.setStatus("current")
_UpsMainsStatisticsB5fourth_Type = NonNegativeInteger32
_UpsMainsStatisticsB5fourth_Object = MibScalar
upsMainsStatisticsB5fourth = _UpsMainsStatisticsB5fourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 16),
    _UpsMainsStatisticsB5fourth_Type()
)
upsMainsStatisticsB5fourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5fourth.setStatus("current")
_UpsMainsStatisticsB10fourth_Type = NonNegativeInteger32
_UpsMainsStatisticsB10fourth_Object = MibScalar
upsMainsStatisticsB10fourth = _UpsMainsStatisticsB10fourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 17),
    _UpsMainsStatisticsB10fourth_Type()
)
upsMainsStatisticsB10fourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10fourth.setStatus("current")
_UpsMainsStatisticsB200fourth_Type = NonNegativeInteger32
_UpsMainsStatisticsB200fourth_Object = MibScalar
upsMainsStatisticsB200fourth = _UpsMainsStatisticsB200fourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 18),
    _UpsMainsStatisticsB200fourth_Type()
)
upsMainsStatisticsB200fourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200fourth.setStatus("current")
_UpsMainsStatisticsBypRelfourth_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelfourth_Object = MibScalar
upsMainsStatisticsBypRelfourth = _UpsMainsStatisticsBypRelfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 19),
    _UpsMainsStatisticsBypRelfourth_Type()
)
upsMainsStatisticsBypRelfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelfourth.setStatus("current")
_UpsTimefourth_Type = NonNegativeInteger32
_UpsTimefourth_Object = MibScalar
upsTimefourth = _UpsTimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 20),
    _UpsTimefourth_Type()
)
upsTimefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimefourth.setStatus("current")
_UpsRequestPermissionfourth_Type = DisplayString
_UpsRequestPermissionfourth_Object = MibScalar
upsRequestPermissionfourth = _UpsRequestPermissionfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 21),
    _UpsRequestPermissionfourth_Type()
)
upsRequestPermissionfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissionfourth.setStatus("current")
_UpsEventGetCodefourth_Type = Integer32
_UpsEventGetCodefourth_Object = MibScalar
upsEventGetCodefourth = _UpsEventGetCodefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 22),
    _UpsEventGetCodefourth_Type()
)
upsEventGetCodefourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodefourth.setStatus("current")
_UpsEventSpinLockfourth_Type = TestAndIncr
_UpsEventSpinLockfourth_Object = MibScalar
upsEventSpinLockfourth = _UpsEventSpinLockfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 23),
    _UpsEventSpinLockfourth_Type()
)
upsEventSpinLockfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLockfourth.setStatus("current")
_UpsParameterSpinLockfourth_Type = TestAndIncr
_UpsParameterSpinLockfourth_Object = MibScalar
upsParameterSpinLockfourth = _UpsParameterSpinLockfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 10, 24),
    _UpsParameterSpinLockfourth_Type()
)
upsParameterSpinLockfourth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLockfourth.setStatus("current")
_GeUPSTrapsfourth_ObjectIdentity = ObjectIdentity
geUPSTrapsfourth = _GeUPSTrapsfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11)
)
_UpsDiagnosticfourth_ObjectIdentity = ObjectIdentity
upsDiagnosticfourth = _UpsDiagnosticfourth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12)
)
_UpsDiagnosticBusJACommunicationStatusfourth_Type = Integer32
_UpsDiagnosticBusJACommunicationStatusfourth_Object = MibScalar
upsDiagnosticBusJACommunicationStatusfourth = _UpsDiagnosticBusJACommunicationStatusfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12, 1),
    _UpsDiagnosticBusJACommunicationStatusfourth_Type()
)
upsDiagnosticBusJACommunicationStatusfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatusfourth.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatusfourth_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatusfourth_Object = MibScalar
upsDiagnosticBusJBCommunicationStatusfourth = _UpsDiagnosticBusJBCommunicationStatusfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatusfourth_Type()
)
upsDiagnosticBusJBCommunicationStatusfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatusfourth.setStatus("current")
_UpsDiagnosticBatteryLifetimefourth_Type = Integer32
_UpsDiagnosticBatteryLifetimefourth_Object = MibScalar
upsDiagnosticBatteryLifetimefourth = _UpsDiagnosticBatteryLifetimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12, 3),
    _UpsDiagnosticBatteryLifetimefourth_Type()
)
upsDiagnosticBatteryLifetimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimefourth.setStatus("current")
_UpsDiagnosticFansLifetimefourth_Type = Integer32
_UpsDiagnosticFansLifetimefourth_Object = MibScalar
upsDiagnosticFansLifetimefourth = _UpsDiagnosticFansLifetimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12, 4),
    _UpsDiagnosticFansLifetimefourth_Type()
)
upsDiagnosticFansLifetimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimefourth.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimefourth_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimefourth_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimefourth = _UpsDiagnosticDCcapacitorsLifetimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimefourth_Type()
)
upsDiagnosticDCcapacitorsLifetimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimefourth.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimefourth_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimefourth_Object = MibScalar
upsDiagnosticACcapacitorsLifetimefourth = _UpsDiagnosticACcapacitorsLifetimefourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimefourth_Type()
)
upsDiagnosticACcapacitorsLifetimefourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimefourth.setStatus("current")
_UpsDiagnosticGlobalServiceCheckfourth_Type = Integer32
_UpsDiagnosticGlobalServiceCheckfourth_Object = MibScalar
upsDiagnosticGlobalServiceCheckfourth = _UpsDiagnosticGlobalServiceCheckfourth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 12, 7),
    _UpsDiagnosticGlobalServiceCheckfourth_Type()
)
upsDiagnosticGlobalServiceCheckfourth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheckfourth.setStatus("current")
_GeFifthUPS_ObjectIdentity = ObjectIdentity
geFifthUPS = _GeFifthUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15)
)
_UpsIdentfifth_ObjectIdentity = ObjectIdentity
upsIdentfifth = _UpsIdentfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1)
)
_UpsIdentManufacturerfifth_Type = DisplayString
_UpsIdentManufacturerfifth_Object = MibScalar
upsIdentManufacturerfifth = _UpsIdentManufacturerfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 1),
    _UpsIdentManufacturerfifth_Type()
)
upsIdentManufacturerfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturerfifth.setStatus("current")
_UpsIdentModelfifth_Type = DisplayString
_UpsIdentModelfifth_Object = MibScalar
upsIdentModelfifth = _UpsIdentModelfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 2),
    _UpsIdentModelfifth_Type()
)
upsIdentModelfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelfifth.setStatus("current")
_UpsIdentUPSSoftwareVersionfifth_Type = DisplayString
_UpsIdentUPSSoftwareVersionfifth_Object = MibScalar
upsIdentUPSSoftwareVersionfifth = _UpsIdentUPSSoftwareVersionfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 3),
    _UpsIdentUPSSoftwareVersionfifth_Type()
)
upsIdentUPSSoftwareVersionfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersionfifth.setStatus("current")
_UpsIdentAgentSoftwareVersionfifth_Type = DisplayString
_UpsIdentAgentSoftwareVersionfifth_Object = MibScalar
upsIdentAgentSoftwareVersionfifth = _UpsIdentAgentSoftwareVersionfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 4),
    _UpsIdentAgentSoftwareVersionfifth_Type()
)
upsIdentAgentSoftwareVersionfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersionfifth.setStatus("current")
_UpsIdentNamefifth_Type = DisplayString
_UpsIdentNamefifth_Object = MibScalar
upsIdentNamefifth = _UpsIdentNamefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 5),
    _UpsIdentNamefifth_Type()
)
upsIdentNamefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNamefifth.setStatus("current")
_UpsIdentAttachedDevicesfifth_Type = DisplayString
_UpsIdentAttachedDevicesfifth_Object = MibScalar
upsIdentAttachedDevicesfifth = _UpsIdentAttachedDevicesfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 6),
    _UpsIdentAttachedDevicesfifth_Type()
)
upsIdentAttachedDevicesfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicesfifth.setStatus("current")
_UpsIdentUPSSerialNumberfifth_Type = DisplayString
_UpsIdentUPSSerialNumberfifth_Object = MibScalar
upsIdentUPSSerialNumberfifth = _UpsIdentUPSSerialNumberfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 7),
    _UpsIdentUPSSerialNumberfifth_Type()
)
upsIdentUPSSerialNumberfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumberfifth.setStatus("current")
_UpsIdentComProtVersionfifth_Type = DisplayString
_UpsIdentComProtVersionfifth_Object = MibScalar
upsIdentComProtVersionfifth = _UpsIdentComProtVersionfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 8),
    _UpsIdentComProtVersionfifth_Type()
)
upsIdentComProtVersionfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersionfifth.setStatus("current")
_UpsIdentOperatingTimefifth_Type = NonNegativeInteger32
_UpsIdentOperatingTimefifth_Object = MibScalar
upsIdentOperatingTimefifth = _UpsIdentOperatingTimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 1, 9),
    _UpsIdentOperatingTimefifth_Type()
)
upsIdentOperatingTimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimefifth.setUnits("fifths")
_UpsBatteryfifth_ObjectIdentity = ObjectIdentity
upsBatteryfifth = _UpsBatteryfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2)
)


class _UpsBatteryStatusfifth_Type(Integer32):
    """Custom type upsBatteryStatusfifth based on Integer32"""
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


_UpsBatteryStatusfifth_Type.__name__ = "Integer32"
_UpsBatteryStatusfifth_Object = MibScalar
upsBatteryStatusfifth = _UpsBatteryStatusfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 1),
    _UpsBatteryStatusfifth_Type()
)
upsBatteryStatusfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatusfifth.setStatus("current")
_UpsSecondsOnBatteryfifth_Type = Integer32
_UpsSecondsOnBatteryfifth_Object = MibScalar
upsSecondsOnBatteryfifth = _UpsSecondsOnBatteryfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 2),
    _UpsSecondsOnBatteryfifth_Type()
)
upsSecondsOnBatteryfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryfifth.setUnits("fifths")
_UpsEstimatedMinutesRemainingfifth_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingfifth_Object = MibScalar
upsEstimatedMinutesRemainingfifth = _UpsEstimatedMinutesRemainingfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 3),
    _UpsEstimatedMinutesRemainingfifth_Type()
)
upsEstimatedMinutesRemainingfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingfifth.setUnits("minutes")


class _UpsEstimatedChargeRemainingfifth_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingfifth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingfifth_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingfifth_Object = MibScalar
upsEstimatedChargeRemainingfifth = _UpsEstimatedChargeRemainingfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 4),
    _UpsEstimatedChargeRemainingfifth_Type()
)
upsEstimatedChargeRemainingfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingfifth.setUnits("percent")
_UpsBatteryVoltagefifth_Type = NonNegativeInteger32
_UpsBatteryVoltagefifth_Object = MibScalar
upsBatteryVoltagefifth = _UpsBatteryVoltagefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 5),
    _UpsBatteryVoltagefifth_Type()
)
upsBatteryVoltagefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltagefifth.setUnits("0.1 Volt DC")
_UpsBatteryCurrentfifth_Type = Integer32
_UpsBatteryCurrentfifth_Object = MibScalar
upsBatteryCurrentfifth = _UpsBatteryCurrentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 6),
    _UpsBatteryCurrentfifth_Type()
)
upsBatteryCurrentfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentfifth.setUnits("0.1 Amp DC")
_UpsBatteryTemperaturefifth_Type = Integer32
_UpsBatteryTemperaturefifth_Object = MibScalar
upsBatteryTemperaturefifth = _UpsBatteryTemperaturefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 7),
    _UpsBatteryTemperaturefifth_Type()
)
upsBatteryTemperaturefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperaturefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperaturefifth.setUnits("degrees Centigrade")
_UpsBatteryRipplefifth_Type = Integer32
_UpsBatteryRipplefifth_Object = MibScalar
upsBatteryRipplefifth = _UpsBatteryRipplefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 2, 8),
    _UpsBatteryRipplefifth_Type()
)
upsBatteryRipplefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipplefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipplefifth.setUnits("0.1 Volt RMS")
_UpsInputfifth_ObjectIdentity = ObjectIdentity
upsInputfifth = _UpsInputfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3)
)
_UpsInputLineBadsfifth_Type = Counter32
_UpsInputLineBadsfifth_Object = MibScalar
upsInputLineBadsfifth = _UpsInputLineBadsfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 1),
    _UpsInputLineBadsfifth_Type()
)
upsInputLineBadsfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadsfifth.setStatus("current")
_UpsInputNumLinesfifth_Type = NonNegativeInteger32
_UpsInputNumLinesfifth_Object = MibScalar
upsInputNumLinesfifth = _UpsInputNumLinesfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 2),
    _UpsInputNumLinesfifth_Type()
)
upsInputNumLinesfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinesfifth.setStatus("current")
_UpsInputFifthTable_Object = MibTable
upsInputFifthTable = _UpsInputFifthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputFifthTable.setStatus("current")
_UpsInputFifthEntry_Object = MibTableRow
upsInputFifthEntry = _UpsInputFifthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1)
)
upsInputFifthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexfifth"),
)
if mibBuilder.loadTexts:
    upsInputFifthEntry.setStatus("current")
_UpsInputLineIndexfifth_Type = PositiveInteger32
_UpsInputLineIndexfifth_Object = MibTableColumn
upsInputLineIndexfifth = _UpsInputLineIndexfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1, 1),
    _UpsInputLineIndexfifth_Type()
)
upsInputLineIndexfifth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexfifth.setStatus("current")
_UpsInputFrequencyfifth_Type = NonNegativeInteger32
_UpsInputFrequencyfifth_Object = MibTableColumn
upsInputFrequencyfifth = _UpsInputFrequencyfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1, 2),
    _UpsInputFrequencyfifth_Type()
)
upsInputFrequencyfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyfifth.setUnits("0.1 Hertz")
_UpsInputVoltagefifth_Type = NonNegativeInteger32
_UpsInputVoltagefifth_Object = MibTableColumn
upsInputVoltagefifth = _UpsInputVoltagefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1, 3),
    _UpsInputVoltagefifth_Type()
)
upsInputVoltagefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltagefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltagefifth.setUnits("RMS Volts")
_UpsInputCurrentfifth_Type = NonNegativeInteger32
_UpsInputCurrentfifth_Object = MibTableColumn
upsInputCurrentfifth = _UpsInputCurrentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1, 4),
    _UpsInputCurrentfifth_Type()
)
upsInputCurrentfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentfifth.setUnits("0.1 RMS Amp")
_UpsInputTruePowerfifth_Type = NonNegativeInteger32
_UpsInputTruePowerfifth_Object = MibTableColumn
upsInputTruePowerfifth = _UpsInputTruePowerfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1, 5),
    _UpsInputTruePowerfifth_Type()
)
upsInputTruePowerfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowerfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowerfifth.setUnits("Watts")
_UpsInputVoltageMinfifth_Type = NonNegativeInteger32
_UpsInputVoltageMinfifth_Object = MibTableColumn
upsInputVoltageMinfifth = _UpsInputVoltageMinfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1, 6),
    _UpsInputVoltageMinfifth_Type()
)
upsInputVoltageMinfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMinfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMinfifth.setUnits("RMS Volts")
_UpsInputVoltageMaxfifth_Type = NonNegativeInteger32
_UpsInputVoltageMaxfifth_Object = MibTableColumn
upsInputVoltageMaxfifth = _UpsInputVoltageMaxfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 3, 3, 1, 7),
    _UpsInputVoltageMaxfifth_Type()
)
upsInputVoltageMaxfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxfifth.setUnits("RMS Volts")
_UpsOutputfifth_ObjectIdentity = ObjectIdentity
upsOutputfifth = _UpsOutputfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4)
)


class _UpsOutputSourcefifth_Type(Integer32):
    """Custom type upsOutputSourcefifth based on Integer32"""
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


_UpsOutputSourcefifth_Type.__name__ = "Integer32"
_UpsOutputSourcefifth_Object = MibScalar
upsOutputSourcefifth = _UpsOutputSourcefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 1),
    _UpsOutputSourcefifth_Type()
)
upsOutputSourcefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourcefifth.setStatus("current")
_UpsOutputFrequencyfifth_Type = NonNegativeInteger32
_UpsOutputFrequencyfifth_Object = MibScalar
upsOutputFrequencyfifth = _UpsOutputFrequencyfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 2),
    _UpsOutputFrequencyfifth_Type()
)
upsOutputFrequencyfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencyfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencyfifth.setUnits("0.1 Hertz")
_UpsOutputNumLinesfifth_Type = NonNegativeInteger32
_UpsOutputNumLinesfifth_Object = MibScalar
upsOutputNumLinesfifth = _UpsOutputNumLinesfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 3),
    _UpsOutputNumLinesfifth_Type()
)
upsOutputNumLinesfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinesfifth.setStatus("current")
_UpsOutputFifthTable_Object = MibTable
upsOutputFifthTable = _UpsOutputFifthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputFifthTable.setStatus("current")
_UpsOutputFifthEntry_Object = MibTableRow
upsOutputFifthEntry = _UpsOutputFifthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1)
)
upsOutputFifthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexfifth"),
)
if mibBuilder.loadTexts:
    upsOutputFifthEntry.setStatus("current")
_UpsOutputLineIndexfifth_Type = PositiveInteger32
_UpsOutputLineIndexfifth_Object = MibTableColumn
upsOutputLineIndexfifth = _UpsOutputLineIndexfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 1),
    _UpsOutputLineIndexfifth_Type()
)
upsOutputLineIndexfifth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexfifth.setStatus("current")
_UpsOutputVoltagefifth_Type = NonNegativeInteger32
_UpsOutputVoltagefifth_Object = MibTableColumn
upsOutputVoltagefifth = _UpsOutputVoltagefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 2),
    _UpsOutputVoltagefifth_Type()
)
upsOutputVoltagefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltagefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltagefifth.setUnits("RMS Volts")
_UpsOutputCurrentfifth_Type = NonNegativeInteger32
_UpsOutputCurrentfifth_Object = MibTableColumn
upsOutputCurrentfifth = _UpsOutputCurrentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 3),
    _UpsOutputCurrentfifth_Type()
)
upsOutputCurrentfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentfifth.setUnits("0.1 RMS Amp")
_UpsOutputPowerfifth_Type = NonNegativeInteger32
_UpsOutputPowerfifth_Object = MibTableColumn
upsOutputPowerfifth = _UpsOutputPowerfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 4),
    _UpsOutputPowerfifth_Type()
)
upsOutputPowerfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerfifth.setUnits("Watts")


class _UpsOutputPercentLoadfifth_Type(Integer32):
    """Custom type upsOutputPercentLoadfifth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadfifth_Type.__name__ = "Integer32"
_UpsOutputPercentLoadfifth_Object = MibTableColumn
upsOutputPercentLoadfifth = _UpsOutputPercentLoadfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 5),
    _UpsOutputPercentLoadfifth_Type()
)
upsOutputPercentLoadfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadfifth.setUnits("percent")


class _UpsOutputPowerFactorfifth_Type(Integer32):
    """Custom type upsOutputPowerFactorfifth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorfifth_Type.__name__ = "Integer32"
_UpsOutputPowerFactorfifth_Object = MibTableColumn
upsOutputPowerFactorfifth = _UpsOutputPowerFactorfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 6),
    _UpsOutputPowerFactorfifth_Type()
)
upsOutputPowerFactorfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorfifth.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentfifth_Type = Integer32
_UpsOutputPeakCurrentfifth_Object = MibTableColumn
upsOutputPeakCurrentfifth = _UpsOutputPeakCurrentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 7),
    _UpsOutputPeakCurrentfifth_Type()
)
upsOutputPeakCurrentfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentfifth.setUnits("Amps")
_UpsOutputShareCurrentfifth_Type = Integer32
_UpsOutputShareCurrentfifth_Object = MibTableColumn
upsOutputShareCurrentfifth = _UpsOutputShareCurrentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 4, 4, 1, 8),
    _UpsOutputShareCurrentfifth_Type()
)
upsOutputShareCurrentfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentfifth.setUnits("Amps")
_UpsBypassfifth_ObjectIdentity = ObjectIdentity
upsBypassfifth = _UpsBypassfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5)
)
_UpsBypassFrequencyfifth_Type = NonNegativeInteger32
_UpsBypassFrequencyfifth_Object = MibScalar
upsBypassFrequencyfifth = _UpsBypassFrequencyfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 1),
    _UpsBypassFrequencyfifth_Type()
)
upsBypassFrequencyfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencyfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencyfifth.setUnits("0.1 Hertz")
_UpsBypassNumLinesfifth_Type = NonNegativeInteger32
_UpsBypassNumLinesfifth_Object = MibScalar
upsBypassNumLinesfifth = _UpsBypassNumLinesfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 2),
    _UpsBypassNumLinesfifth_Type()
)
upsBypassNumLinesfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinesfifth.setStatus("current")
_UpsBypassFifthTable_Object = MibTable
upsBypassFifthTable = _UpsBypassFifthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassFifthTable.setStatus("current")
_UpsBypassFifthEntry_Object = MibTableRow
upsBypassFifthEntry = _UpsBypassFifthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 3, 1)
)
upsBypassFifthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexfifth"),
)
if mibBuilder.loadTexts:
    upsBypassFifthEntry.setStatus("current")
_UpsBypassLineIndexfifth_Type = PositiveInteger32
_UpsBypassLineIndexfifth_Object = MibTableColumn
upsBypassLineIndexfifth = _UpsBypassLineIndexfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 3, 1, 1),
    _UpsBypassLineIndexfifth_Type()
)
upsBypassLineIndexfifth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexfifth.setStatus("current")
_UpsBypassVoltagefifth_Type = NonNegativeInteger32
_UpsBypassVoltagefifth_Object = MibTableColumn
upsBypassVoltagefifth = _UpsBypassVoltagefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 3, 1, 2),
    _UpsBypassVoltagefifth_Type()
)
upsBypassVoltagefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltagefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltagefifth.setUnits("RMS Volts")
_UpsBypassCurrentfifth_Type = NonNegativeInteger32
_UpsBypassCurrentfifth_Object = MibTableColumn
upsBypassCurrentfifth = _UpsBypassCurrentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 3, 1, 3),
    _UpsBypassCurrentfifth_Type()
)
upsBypassCurrentfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentfifth.setUnits("0.1 RMS Amp")
_UpsBypassPowerfifth_Type = NonNegativeInteger32
_UpsBypassPowerfifth_Object = MibTableColumn
upsBypassPowerfifth = _UpsBypassPowerfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 5, 3, 1, 4),
    _UpsBypassPowerfifth_Type()
)
upsBypassPowerfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowerfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowerfifth.setUnits("Watts")
_UpsAlarmfifth_ObjectIdentity = ObjectIdentity
upsAlarmfifth = _UpsAlarmfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6)
)
_UpsAlarmsPresentfifth_Type = Gauge32
_UpsAlarmsPresentfifth_Object = MibScalar
upsAlarmsPresentfifth = _UpsAlarmsPresentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 1),
    _UpsAlarmsPresentfifth_Type()
)
upsAlarmsPresentfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentfifth.setStatus("current")
_UpsAlarmFifthTable_Object = MibTable
upsAlarmFifthTable = _UpsAlarmFifthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmFifthTable.setStatus("current")
_UpsAlarmFifthEntry_Object = MibTableRow
upsAlarmFifthEntry = _UpsAlarmFifthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 2, 1)
)
upsAlarmFifthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdfifth"),
)
if mibBuilder.loadTexts:
    upsAlarmFifthEntry.setStatus("current")
_UpsAlarmIdfifth_Type = PositiveInteger32
_UpsAlarmIdfifth_Object = MibTableColumn
upsAlarmIdfifth = _UpsAlarmIdfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 2, 1, 1),
    _UpsAlarmIdfifth_Type()
)
upsAlarmIdfifth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdfifth.setStatus("current")
_UpsAlarmDescrfifth_Type = AutonomousType
_UpsAlarmDescrfifth_Object = MibTableColumn
upsAlarmDescrfifth = _UpsAlarmDescrfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 2, 1, 2),
    _UpsAlarmDescrfifth_Type()
)
upsAlarmDescrfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrfifth.setStatus("current")
_UpsAlarmTimefifth_Type = TimeStamp
_UpsAlarmTimefifth_Object = MibTableColumn
upsAlarmTimefifth = _UpsAlarmTimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 2, 1, 3),
    _UpsAlarmTimefifth_Type()
)
upsAlarmTimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimefifth.setStatus("current")
_UpsWellKnownAlarmsfifth_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmsfifth = _UpsWellKnownAlarmsfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3)
)
_UpsAlarmBatteryBadfifth_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadfifth = _UpsAlarmBatteryBadfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadfifth.setStatus("current")
_UpsAlarmOnBatteryfifth_ObjectIdentity = ObjectIdentity
upsAlarmOnBatteryfifth = _UpsAlarmOnBatteryfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatteryfifth.setStatus("current")
_UpsAlarmLowBatteryfifth_ObjectIdentity = ObjectIdentity
upsAlarmLowBatteryfifth = _UpsAlarmLowBatteryfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatteryfifth.setStatus("current")
_UpsAlarmDepletedBatteryfifth_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatteryfifth = _UpsAlarmDepletedBatteryfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatteryfifth.setStatus("current")
_UpsAlarmTempBadfifth_ObjectIdentity = ObjectIdentity
upsAlarmTempBadfifth = _UpsAlarmTempBadfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadfifth.setStatus("current")
_UpsAlarmInputBadfifth_ObjectIdentity = ObjectIdentity
upsAlarmInputBadfifth = _UpsAlarmInputBadfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadfifth.setStatus("current")
_UpsAlarmOutputBadfifth_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadfifth = _UpsAlarmOutputBadfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadfifth.setStatus("current")
_UpsAlarmOutputOverloadfifth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadfifth = _UpsAlarmOutputOverloadfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadfifth.setStatus("current")
_UpsAlarmOnBypassfifth_ObjectIdentity = ObjectIdentity
upsAlarmOnBypassfifth = _UpsAlarmOnBypassfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypassfifth.setStatus("current")
_UpsAlarmBypassBadfifth_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadfifth = _UpsAlarmBypassBadfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadfifth.setStatus("current")
_UpsAlarmOutputOffAsRequestedfifth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedfifth = _UpsAlarmOutputOffAsRequestedfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedfifth.setStatus("current")
_UpsAlarmUpsOffAsRequestedfifth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedfifth = _UpsAlarmUpsOffAsRequestedfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedfifth.setStatus("current")
_UpsAlarmChargerFailedfifth_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedfifth = _UpsAlarmChargerFailedfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedfifth.setStatus("current")
_UpsAlarmUpsOutputOfffifth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOfffifth = _UpsAlarmUpsOutputOfffifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOfffifth.setStatus("current")
_UpsAlarmUpsSystemOfffifth_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOfffifth = _UpsAlarmUpsSystemOfffifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOfffifth.setStatus("current")
_UpsAlarmFanFailurefifth_ObjectIdentity = ObjectIdentity
upsAlarmFanFailurefifth = _UpsAlarmFanFailurefifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailurefifth.setStatus("current")
_UpsAlarmFuseFailurefifth_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailurefifth = _UpsAlarmFuseFailurefifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailurefifth.setStatus("current")
_UpsAlarmGeneralFaultfifth_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultfifth = _UpsAlarmGeneralFaultfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultfifth.setStatus("current")
_UpsAlarmDiagnosticTestFailedfifth_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedfifth = _UpsAlarmDiagnosticTestFailedfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedfifth.setStatus("current")
_UpsAlarmCommunicationsLostfifth_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostfifth = _UpsAlarmCommunicationsLostfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostfifth.setStatus("current")
_UpsAlarmAwaitingPowerfifth_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowerfifth = _UpsAlarmAwaitingPowerfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowerfifth.setStatus("current")
_UpsAlarmShutdownPendingfifth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingfifth = _UpsAlarmShutdownPendingfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingfifth.setStatus("current")
_UpsAlarmShutdownImminentfifth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentfifth = _UpsAlarmShutdownImminentfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentfifth.setStatus("current")
_UpsAlarmTestInProgressfifth_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgressfifth = _UpsAlarmTestInProgressfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgressfifth.setStatus("current")
_UpsAlarmReceptacleOfffifth_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOfffifth = _UpsAlarmReceptacleOfffifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOfffifth.setStatus("current")
_UpsAlarmHighSpeedBusFailurefifth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailurefifth = _UpsAlarmHighSpeedBusFailurefifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailurefifth.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailurefifth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailurefifth = _UpsAlarmHighSpeedBusJACRCFailurefifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailurefifth.setStatus("current")
_UpsAlarmConnectivityBusFailurefifth_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailurefifth = _UpsAlarmConnectivityBusFailurefifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailurefifth.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailurefifth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailurefifth = _UpsAlarmHighSpeedBusJBCRCFailurefifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailurefifth.setStatus("current")
_UpsAlarmCurrentSharingfifth_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingfifth = _UpsAlarmCurrentSharingfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingfifth.setStatus("current")
_UpsAlarmDCRipplefifth_ObjectIdentity = ObjectIdentity
upsAlarmDCRipplefifth = _UpsAlarmDCRipplefifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipplefifth.setStatus("current")
_UpsAlarmMaskAfifth_Type = Unsigned32
_UpsAlarmMaskAfifth_Object = MibScalar
upsAlarmMaskAfifth = _UpsAlarmMaskAfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 6, 4),
    _UpsAlarmMaskAfifth_Type()
)
upsAlarmMaskAfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAfifth.setStatus("current")
_UpsTestfifth_ObjectIdentity = ObjectIdentity
upsTestfifth = _UpsTestfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7)
)
_UpsTestIdfifth_Type = ObjectIdentifier
_UpsTestIdfifth_Object = MibScalar
upsTestIdfifth = _UpsTestIdfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 1),
    _UpsTestIdfifth_Type()
)
upsTestIdfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdfifth.setStatus("current")
_UpsTestSpinLockfifth_Type = TestAndIncr
_UpsTestSpinLockfifth_Object = MibScalar
upsTestSpinLockfifth = _UpsTestSpinLockfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 2),
    _UpsTestSpinLockfifth_Type()
)
upsTestSpinLockfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLockfifth.setStatus("current")


class _UpsTestResultsSummaryfifth_Type(Integer32):
    """Custom type upsTestResultsSummaryfifth based on Integer32"""
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


_UpsTestResultsSummaryfifth_Type.__name__ = "Integer32"
_UpsTestResultsSummaryfifth_Object = MibScalar
upsTestResultsSummaryfifth = _UpsTestResultsSummaryfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 3),
    _UpsTestResultsSummaryfifth_Type()
)
upsTestResultsSummaryfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummaryfifth.setStatus("current")
_UpsTestResultsDetailfifth_Type = DisplayString
_UpsTestResultsDetailfifth_Object = MibScalar
upsTestResultsDetailfifth = _UpsTestResultsDetailfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 4),
    _UpsTestResultsDetailfifth_Type()
)
upsTestResultsDetailfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailfifth.setStatus("current")
_UpsTestStartTimefifth_Type = TimeStamp
_UpsTestStartTimefifth_Object = MibScalar
upsTestStartTimefifth = _UpsTestStartTimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 5),
    _UpsTestStartTimefifth_Type()
)
upsTestStartTimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimefifth.setStatus("current")
_UpsTestElapsedTimefifth_Type = TimeInterval
_UpsTestElapsedTimefifth_Object = MibScalar
upsTestElapsedTimefifth = _UpsTestElapsedTimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 6),
    _UpsTestElapsedTimefifth_Type()
)
upsTestElapsedTimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimefifth.setStatus("current")
_UpsWellKnownTestsfifth_ObjectIdentity = ObjectIdentity
upsWellKnownTestsfifth = _UpsWellKnownTestsfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 7)
)
_UpsTestNoTestsInitiatedfifth_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedfifth = _UpsTestNoTestsInitiatedfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedfifth.setStatus("current")
_UpsTestAbortTestInProgressfifth_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgressfifth = _UpsTestAbortTestInProgressfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgressfifth.setStatus("current")
_UpsTestGeneralSystemsTestfifth_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestfifth = _UpsTestGeneralSystemsTestfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestfifth.setStatus("current")
_UpsTestQuickBatteryTestfifth_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestfifth = _UpsTestQuickBatteryTestfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestfifth.setStatus("current")
_UpsTestDeepBatteryCalibrationfifth_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationfifth = _UpsTestDeepBatteryCalibrationfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationfifth.setStatus("current")
_UpsControlfifth_ObjectIdentity = ObjectIdentity
upsControlfifth = _UpsControlfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8)
)


class _UpsShutdownTypefifth_Type(Integer32):
    """Custom type upsShutdownTypefifth based on Integer32"""
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


_UpsShutdownTypefifth_Type.__name__ = "Integer32"
_UpsShutdownTypefifth_Object = MibScalar
upsShutdownTypefifth = _UpsShutdownTypefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 1),
    _UpsShutdownTypefifth_Type()
)
upsShutdownTypefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypefifth.setStatus("current")


class _UpsShutdownAfterDelayfifth_Type(Integer32):
    """Custom type upsShutdownAfterDelayfifth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelayfifth_Type.__name__ = "Integer32"
_UpsShutdownAfterDelayfifth_Object = MibScalar
upsShutdownAfterDelayfifth = _UpsShutdownAfterDelayfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 2),
    _UpsShutdownAfterDelayfifth_Type()
)
upsShutdownAfterDelayfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayfifth.setUnits("fifths")


class _UpsStartupAfterDelayfifth_Type(Integer32):
    """Custom type upsStartupAfterDelayfifth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelayfifth_Type.__name__ = "Integer32"
_UpsStartupAfterDelayfifth_Object = MibScalar
upsStartupAfterDelayfifth = _UpsStartupAfterDelayfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 3),
    _UpsStartupAfterDelayfifth_Type()
)
upsStartupAfterDelayfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelayfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelayfifth.setUnits("fifths")


class _UpsRebootWithDurationfifth_Type(Integer32):
    """Custom type upsRebootWithDurationfifth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationfifth_Type.__name__ = "Integer32"
_UpsRebootWithDurationfifth_Object = MibScalar
upsRebootWithDurationfifth = _UpsRebootWithDurationfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 4),
    _UpsRebootWithDurationfifth_Type()
)
upsRebootWithDurationfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationfifth.setUnits("fifths")


class _UpsAutoRestartfifth_Type(Integer32):
    """Custom type upsAutoRestartfifth based on Integer32"""
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


_UpsAutoRestartfifth_Type.__name__ = "Integer32"
_UpsAutoRestartfifth_Object = MibScalar
upsAutoRestartfifth = _UpsAutoRestartfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 5),
    _UpsAutoRestartfifth_Type()
)
upsAutoRestartfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartfifth.setStatus("current")
_UpsReceptaclesNumfifth_Type = NonNegativeInteger32
_UpsReceptaclesNumfifth_Object = MibScalar
upsReceptaclesNumfifth = _UpsReceptaclesNumfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 6),
    _UpsReceptaclesNumfifth_Type()
)
upsReceptaclesNumfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumfifth.setStatus("current")
_UpsReceptacleFifthTable_Object = MibTable
upsReceptacleFifthTable = _UpsReceptacleFifthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleFifthTable.setStatus("current")
_UpsReceptacleFifthEntry_Object = MibTableRow
upsReceptacleFifthEntry = _UpsReceptacleFifthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 7, 1)
)
upsReceptacleFifthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexfifth"),
)
if mibBuilder.loadTexts:
    upsReceptacleFifthEntry.setStatus("current")
_UpsReceptacleLineIndexfifth_Type = PositiveInteger32
_UpsReceptacleLineIndexfifth_Object = MibTableColumn
upsReceptacleLineIndexfifth = _UpsReceptacleLineIndexfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 7, 1, 1),
    _UpsReceptacleLineIndexfifth_Type()
)
upsReceptacleLineIndexfifth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexfifth.setStatus("current")


class _UpsReceptacleOnOfffifth_Type(Integer32):
    """Custom type upsReceptacleOnOfffifth based on Integer32"""
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


_UpsReceptacleOnOfffifth_Type.__name__ = "Integer32"
_UpsReceptacleOnOfffifth_Object = MibTableColumn
upsReceptacleOnOfffifth = _UpsReceptacleOnOfffifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 7, 1, 2),
    _UpsReceptacleOnOfffifth_Type()
)
upsReceptacleOnOfffifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOfffifth.setStatus("current")


class _UpsUPSModefifth_Type(Integer32):
    """Custom type upsUPSModefifth based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModefifth_Type.__name__ = "Integer32"
_UpsUPSModefifth_Object = MibScalar
upsUPSModefifth = _UpsUPSModefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 8),
    _UpsUPSModefifth_Type()
)
upsUPSModefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModefifth.setStatus("current")


class _UpsRectifierOnOfffifth_Type(Integer32):
    """Custom type upsRectifierOnOfffifth based on Integer32"""
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


_UpsRectifierOnOfffifth_Type.__name__ = "Integer32"
_UpsRectifierOnOfffifth_Object = MibScalar
upsRectifierOnOfffifth = _UpsRectifierOnOfffifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 9),
    _UpsRectifierOnOfffifth_Type()
)
upsRectifierOnOfffifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOfffifth.setStatus("current")


class _UpsBatteryChargeMethodfifth_Type(Integer32):
    """Custom type upsBatteryChargeMethodfifth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodfifth_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodfifth_Object = MibScalar
upsBatteryChargeMethodfifth = _UpsBatteryChargeMethodfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 10),
    _UpsBatteryChargeMethodfifth_Type()
)
upsBatteryChargeMethodfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodfifth.setStatus("current")


class _UpsInverterOnOfffifth_Type(Integer32):
    """Custom type upsInverterOnOfffifth based on Integer32"""
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


_UpsInverterOnOfffifth_Type.__name__ = "Integer32"
_UpsInverterOnOfffifth_Object = MibScalar
upsInverterOnOfffifth = _UpsInverterOnOfffifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 11),
    _UpsInverterOnOfffifth_Type()
)
upsInverterOnOfffifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOfffifth.setStatus("current")


class _UpsBypassOnOfffifth_Type(Integer32):
    """Custom type upsBypassOnOfffifth based on Integer32"""
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


_UpsBypassOnOfffifth_Type.__name__ = "Integer32"
_UpsBypassOnOfffifth_Object = MibScalar
upsBypassOnOfffifth = _UpsBypassOnOfffifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 12),
    _UpsBypassOnOfffifth_Type()
)
upsBypassOnOfffifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOfffifth.setStatus("current")


class _UpsLoadSourcefifth_Type(Integer32):
    """Custom type upsLoadSourcefifth based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourcefifth_Type.__name__ = "Integer32"
_UpsLoadSourcefifth_Object = MibScalar
upsLoadSourcefifth = _UpsLoadSourcefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 8, 13),
    _UpsLoadSourcefifth_Type()
)
upsLoadSourcefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourcefifth.setStatus("current")
_UpsConfigfifth_ObjectIdentity = ObjectIdentity
upsConfigfifth = _UpsConfigfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9)
)
_UpsConfigInputVoltagefifth_Type = NonNegativeInteger32
_UpsConfigInputVoltagefifth_Object = MibScalar
upsConfigInputVoltagefifth = _UpsConfigInputVoltagefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 1),
    _UpsConfigInputVoltagefifth_Type()
)
upsConfigInputVoltagefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltagefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltagefifth.setUnits("RMS Volts")
_UpsConfigInputFreqfifth_Type = NonNegativeInteger32
_UpsConfigInputFreqfifth_Object = MibScalar
upsConfigInputFreqfifth = _UpsConfigInputFreqfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 2),
    _UpsConfigInputFreqfifth_Type()
)
upsConfigInputFreqfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqfifth.setUnits("0.1 Hertz")
_UpsConfigOutputVoltagefifth_Type = NonNegativeInteger32
_UpsConfigOutputVoltagefifth_Object = MibScalar
upsConfigOutputVoltagefifth = _UpsConfigOutputVoltagefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 3),
    _UpsConfigOutputVoltagefifth_Type()
)
upsConfigOutputVoltagefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagefifth.setUnits("RMS Volts")
_UpsConfigOutputFreqfifth_Type = NonNegativeInteger32
_UpsConfigOutputFreqfifth_Object = MibScalar
upsConfigOutputFreqfifth = _UpsConfigOutputFreqfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 4),
    _UpsConfigOutputFreqfifth_Type()
)
upsConfigOutputFreqfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqfifth.setUnits("0.1 Hertz")
_UpsConfigOutputVAfifth_Type = NonNegativeInteger32
_UpsConfigOutputVAfifth_Object = MibScalar
upsConfigOutputVAfifth = _UpsConfigOutputVAfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 5),
    _UpsConfigOutputVAfifth_Type()
)
upsConfigOutputVAfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAfifth.setUnits("Volt-Amps")
_UpsConfigOutputPowerfifth_Type = NonNegativeInteger32
_UpsConfigOutputPowerfifth_Object = MibScalar
upsConfigOutputPowerfifth = _UpsConfigOutputPowerfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 6),
    _UpsConfigOutputPowerfifth_Type()
)
upsConfigOutputPowerfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowerfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowerfifth.setUnits("Watts")
_UpsConfigLowBattTimefifth_Type = NonNegativeInteger32
_UpsConfigLowBattTimefifth_Object = MibScalar
upsConfigLowBattTimefifth = _UpsConfigLowBattTimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 7),
    _UpsConfigLowBattTimefifth_Type()
)
upsConfigLowBattTimefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimefifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimefifth.setUnits("minutes")


class _UpsConfigAudibleStatusfifth_Type(Integer32):
    """Custom type upsConfigAudibleStatusfifth based on Integer32"""
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


_UpsConfigAudibleStatusfifth_Type.__name__ = "Integer32"
_UpsConfigAudibleStatusfifth_Object = MibScalar
upsConfigAudibleStatusfifth = _UpsConfigAudibleStatusfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 8),
    _UpsConfigAudibleStatusfifth_Type()
)
upsConfigAudibleStatusfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatusfifth.setStatus("current")
_UpsConfigLowVoltageTransferPointfifth_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointfifth_Object = MibScalar
upsConfigLowVoltageTransferPointfifth = _UpsConfigLowVoltageTransferPointfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 9),
    _UpsConfigLowVoltageTransferPointfifth_Type()
)
upsConfigLowVoltageTransferPointfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointfifth.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointfifth_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointfifth_Object = MibScalar
upsConfigHighVoltageTransferPointfifth = _UpsConfigHighVoltageTransferPointfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 10),
    _UpsConfigHighVoltageTransferPointfifth_Type()
)
upsConfigHighVoltageTransferPointfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointfifth.setUnits("RMS Volts")
_UpsConfigBatteryCapacityfifth_Type = NonNegativeInteger32
_UpsConfigBatteryCapacityfifth_Object = MibScalar
upsConfigBatteryCapacityfifth = _UpsConfigBatteryCapacityfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 11),
    _UpsConfigBatteryCapacityfifth_Type()
)
upsConfigBatteryCapacityfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityfifth.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentfifth_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentfifth_Object = MibScalar
upsConfigBatteryChargeCurrentfifth = _UpsConfigBatteryChargeCurrentfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 12),
    _UpsConfigBatteryChargeCurrentfifth_Type()
)
upsConfigBatteryChargeCurrentfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentfifth.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdownfifth_Type(Integer32):
    """Custom type upsConfigNoLoadShutdownfifth based on Integer32"""
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


_UpsConfigNoLoadShutdownfifth_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdownfifth_Object = MibScalar
upsConfigNoLoadShutdownfifth = _UpsConfigNoLoadShutdownfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 13),
    _UpsConfigNoLoadShutdownfifth_Type()
)
upsConfigNoLoadShutdownfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdownfifth.setStatus("current")
_UpsConfigStartDelayfifth_Type = PositiveInteger32
_UpsConfigStartDelayfifth_Object = MibScalar
upsConfigStartDelayfifth = _UpsConfigStartDelayfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 9, 14),
    _UpsConfigStartDelayfifth_Type()
)
upsConfigStartDelayfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelayfifth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelayfifth.setUnits("minutes")
_UpsGetSetfifth_ObjectIdentity = ObjectIdentity
upsGetSetfifth = _UpsGetSetfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10)
)
_UpsEventGetNextfifth_Type = PositiveInteger32
_UpsEventGetNextfifth_Object = MibScalar
upsEventGetNextfifth = _UpsEventGetNextfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 1),
    _UpsEventGetNextfifth_Type()
)
upsEventGetNextfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextfifth.setStatus("current")
_UpsEventGetPreviousfifth_Type = PositiveInteger32
_UpsEventGetPreviousfifth_Object = MibScalar
upsEventGetPreviousfifth = _UpsEventGetPreviousfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 2),
    _UpsEventGetPreviousfifth_Type()
)
upsEventGetPreviousfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPreviousfifth.setStatus("current")
_UpsEventSetStartingTimeStampfifth_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampfifth_Object = MibScalar
upsEventSetStartingTimeStampfifth = _UpsEventSetStartingTimeStampfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 3),
    _UpsEventSetStartingTimeStampfifth_Type()
)
upsEventSetStartingTimeStampfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampfifth.setStatus("current")
_UpsEventRetreiveCurrentTimeStampfifth_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampfifth_Object = MibScalar
upsEventRetreiveCurrentTimeStampfifth = _UpsEventRetreiveCurrentTimeStampfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 4),
    _UpsEventRetreiveCurrentTimeStampfifth_Type()
)
upsEventRetreiveCurrentTimeStampfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampfifth.setStatus("current")
_UpsEventTableSizefifth_Type = NonNegativeInteger32
_UpsEventTableSizefifth_Object = MibScalar
upsEventTableSizefifth = _UpsEventTableSizefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 5),
    _UpsEventTableSizefifth_Type()
)
upsEventTableSizefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizefifth.setStatus("current")
_UpsEventFifthTable_Object = MibTable
upsEventFifthTable = _UpsEventFifthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventFifthTable.setStatus("current")
_UpsEventFifthEntry_Object = MibTableRow
upsEventFifthEntry = _UpsEventFifthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 6, 1)
)
upsEventFifthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexfifth"),
)
if mibBuilder.loadTexts:
    upsEventFifthEntry.setStatus("current")
_UpsEventLineIndexfifth_Type = PositiveInteger32
_UpsEventLineIndexfifth_Object = MibTableColumn
upsEventLineIndexfifth = _UpsEventLineIndexfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 6, 1, 1),
    _UpsEventLineIndexfifth_Type()
)
upsEventLineIndexfifth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexfifth.setStatus("current")
_UpsEventCodefifth_Type = Integer32
_UpsEventCodefifth_Object = MibTableColumn
upsEventCodefifth = _UpsEventCodefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 6, 1, 2),
    _UpsEventCodefifth_Type()
)
upsEventCodefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodefifth.setStatus("current")
_UpsEventStatusfifth_Type = NonNegativeInteger32
_UpsEventStatusfifth_Object = MibTableColumn
upsEventStatusfifth = _UpsEventStatusfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 6, 1, 3),
    _UpsEventStatusfifth_Type()
)
upsEventStatusfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatusfifth.setStatus("current")
_UpsEventTimefifth_Type = NonNegativeInteger32
_UpsEventTimefifth_Object = MibTableColumn
upsEventTimefifth = _UpsEventTimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 6, 1, 4),
    _UpsEventTimefifth_Type()
)
upsEventTimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimefifth.setStatus("current")
_UpsParametersReadfifth_Type = PositiveInteger32
_UpsParametersReadfifth_Object = MibScalar
upsParametersReadfifth = _UpsParametersReadfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 7),
    _UpsParametersReadfifth_Type()
)
upsParametersReadfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadfifth.setStatus("current")
_UpsParametersWritefifth_Type = PositiveInteger32
_UpsParametersWritefifth_Object = MibScalar
upsParametersWritefifth = _UpsParametersWritefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 8),
    _UpsParametersWritefifth_Type()
)
upsParametersWritefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWritefifth.setStatus("current")
_UpsParametersStartAddressfifth_Type = NonNegativeInteger32
_UpsParametersStartAddressfifth_Object = MibScalar
upsParametersStartAddressfifth = _UpsParametersStartAddressfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 9),
    _UpsParametersStartAddressfifth_Type()
)
upsParametersStartAddressfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddressfifth.setStatus("current")
_UpsParameterTableSizefifth_Type = NonNegativeInteger32
_UpsParameterTableSizefifth_Object = MibScalar
upsParameterTableSizefifth = _UpsParameterTableSizefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 10),
    _UpsParameterTableSizefifth_Type()
)
upsParameterTableSizefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizefifth.setStatus("current")
_UpsParameterFifthTable_Object = MibTable
upsParameterFifthTable = _UpsParameterFifthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterFifthTable.setStatus("current")
_UpsParameterFifthEntry_Object = MibTableRow
upsParameterFifthEntry = _UpsParameterFifthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 11, 1)
)
upsParameterFifthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexfifth"),
)
if mibBuilder.loadTexts:
    upsParameterFifthEntry.setStatus("current")
_UpsParameterLineIndexfifth_Type = PositiveInteger32
_UpsParameterLineIndexfifth_Object = MibTableColumn
upsParameterLineIndexfifth = _UpsParameterLineIndexfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 11, 1, 1),
    _UpsParameterLineIndexfifth_Type()
)
upsParameterLineIndexfifth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexfifth.setStatus("current")
_UpsParameterValuefifth_Type = Integer32
_UpsParameterValuefifth_Object = MibTableColumn
upsParameterValuefifth = _UpsParameterValuefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 11, 1, 2),
    _UpsParameterValuefifth_Type()
)
upsParameterValuefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValuefifth.setStatus("current")
_UpsStatusfifth_Type = NonNegativeInteger32
_UpsStatusfifth_Object = MibScalar
upsStatusfifth = _UpsStatusfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 12),
    _UpsStatusfifth_Type()
)
upsStatusfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusfifth.setStatus("current")
_UpsMainsStatisticsMBfailfifth_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailfifth_Object = MibScalar
upsMainsStatisticsMBfailfifth = _UpsMainsStatisticsMBfailfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 13),
    _UpsMainsStatisticsMBfailfifth_Type()
)
upsMainsStatisticsMBfailfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailfifth.setStatus("current")
_UpsMainsStatisticsMRfailfifth_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailfifth_Object = MibScalar
upsMainsStatisticsMRfailfifth = _UpsMainsStatisticsMRfailfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 14),
    _UpsMainsStatisticsMRfailfifth_Type()
)
upsMainsStatisticsMRfailfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailfifth.setStatus("current")
_UpsMainsStatisticsB2fifth_Type = NonNegativeInteger32
_UpsMainsStatisticsB2fifth_Object = MibScalar
upsMainsStatisticsB2fifth = _UpsMainsStatisticsB2fifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 15),
    _UpsMainsStatisticsB2fifth_Type()
)
upsMainsStatisticsB2fifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2fifth.setStatus("current")
_UpsMainsStatisticsB5fifth_Type = NonNegativeInteger32
_UpsMainsStatisticsB5fifth_Object = MibScalar
upsMainsStatisticsB5fifth = _UpsMainsStatisticsB5fifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 16),
    _UpsMainsStatisticsB5fifth_Type()
)
upsMainsStatisticsB5fifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5fifth.setStatus("current")
_UpsMainsStatisticsB10fifth_Type = NonNegativeInteger32
_UpsMainsStatisticsB10fifth_Object = MibScalar
upsMainsStatisticsB10fifth = _UpsMainsStatisticsB10fifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 17),
    _UpsMainsStatisticsB10fifth_Type()
)
upsMainsStatisticsB10fifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10fifth.setStatus("current")
_UpsMainsStatisticsB200fifth_Type = NonNegativeInteger32
_UpsMainsStatisticsB200fifth_Object = MibScalar
upsMainsStatisticsB200fifth = _UpsMainsStatisticsB200fifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 18),
    _UpsMainsStatisticsB200fifth_Type()
)
upsMainsStatisticsB200fifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200fifth.setStatus("current")
_UpsMainsStatisticsBypRelfifth_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelfifth_Object = MibScalar
upsMainsStatisticsBypRelfifth = _UpsMainsStatisticsBypRelfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 19),
    _UpsMainsStatisticsBypRelfifth_Type()
)
upsMainsStatisticsBypRelfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelfifth.setStatus("current")
_UpsTimefifth_Type = NonNegativeInteger32
_UpsTimefifth_Object = MibScalar
upsTimefifth = _UpsTimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 20),
    _UpsTimefifth_Type()
)
upsTimefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimefifth.setStatus("current")
_UpsRequestPermissionfifth_Type = DisplayString
_UpsRequestPermissionfifth_Object = MibScalar
upsRequestPermissionfifth = _UpsRequestPermissionfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 21),
    _UpsRequestPermissionfifth_Type()
)
upsRequestPermissionfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissionfifth.setStatus("current")
_UpsEventGetCodefifth_Type = Integer32
_UpsEventGetCodefifth_Object = MibScalar
upsEventGetCodefifth = _UpsEventGetCodefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 22),
    _UpsEventGetCodefifth_Type()
)
upsEventGetCodefifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodefifth.setStatus("current")
_UpsEventSpinLockfifth_Type = TestAndIncr
_UpsEventSpinLockfifth_Object = MibScalar
upsEventSpinLockfifth = _UpsEventSpinLockfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 23),
    _UpsEventSpinLockfifth_Type()
)
upsEventSpinLockfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLockfifth.setStatus("current")
_UpsParameterSpinLockfifth_Type = TestAndIncr
_UpsParameterSpinLockfifth_Object = MibScalar
upsParameterSpinLockfifth = _UpsParameterSpinLockfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 10, 24),
    _UpsParameterSpinLockfifth_Type()
)
upsParameterSpinLockfifth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLockfifth.setStatus("current")
_GeUPSTrapsfifth_ObjectIdentity = ObjectIdentity
geUPSTrapsfifth = _GeUPSTrapsfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11)
)
_UpsDiagnosticfifth_ObjectIdentity = ObjectIdentity
upsDiagnosticfifth = _UpsDiagnosticfifth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12)
)
_UpsDiagnosticBusJACommunicationStatusfifth_Type = Integer32
_UpsDiagnosticBusJACommunicationStatusfifth_Object = MibScalar
upsDiagnosticBusJACommunicationStatusfifth = _UpsDiagnosticBusJACommunicationStatusfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12, 1),
    _UpsDiagnosticBusJACommunicationStatusfifth_Type()
)
upsDiagnosticBusJACommunicationStatusfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatusfifth.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatusfifth_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatusfifth_Object = MibScalar
upsDiagnosticBusJBCommunicationStatusfifth = _UpsDiagnosticBusJBCommunicationStatusfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatusfifth_Type()
)
upsDiagnosticBusJBCommunicationStatusfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatusfifth.setStatus("current")
_UpsDiagnosticBatteryLifetimefifth_Type = Integer32
_UpsDiagnosticBatteryLifetimefifth_Object = MibScalar
upsDiagnosticBatteryLifetimefifth = _UpsDiagnosticBatteryLifetimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12, 3),
    _UpsDiagnosticBatteryLifetimefifth_Type()
)
upsDiagnosticBatteryLifetimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimefifth.setStatus("current")
_UpsDiagnosticFansLifetimefifth_Type = Integer32
_UpsDiagnosticFansLifetimefifth_Object = MibScalar
upsDiagnosticFansLifetimefifth = _UpsDiagnosticFansLifetimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12, 4),
    _UpsDiagnosticFansLifetimefifth_Type()
)
upsDiagnosticFansLifetimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimefifth.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimefifth_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimefifth_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimefifth = _UpsDiagnosticDCcapacitorsLifetimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimefifth_Type()
)
upsDiagnosticDCcapacitorsLifetimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimefifth.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimefifth_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimefifth_Object = MibScalar
upsDiagnosticACcapacitorsLifetimefifth = _UpsDiagnosticACcapacitorsLifetimefifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimefifth_Type()
)
upsDiagnosticACcapacitorsLifetimefifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimefifth.setStatus("current")
_UpsDiagnosticGlobalServiceCheckfifth_Type = Integer32
_UpsDiagnosticGlobalServiceCheckfifth_Object = MibScalar
upsDiagnosticGlobalServiceCheckfifth = _UpsDiagnosticGlobalServiceCheckfifth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 12, 7),
    _UpsDiagnosticGlobalServiceCheckfifth_Type()
)
upsDiagnosticGlobalServiceCheckfifth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheckfifth.setStatus("current")
_GeSixthUPS_ObjectIdentity = ObjectIdentity
geSixthUPS = _GeSixthUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16)
)
_UpsIdentsixth_ObjectIdentity = ObjectIdentity
upsIdentsixth = _UpsIdentsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1)
)
_UpsIdentManufacturersixth_Type = DisplayString
_UpsIdentManufacturersixth_Object = MibScalar
upsIdentManufacturersixth = _UpsIdentManufacturersixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 1),
    _UpsIdentManufacturersixth_Type()
)
upsIdentManufacturersixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturersixth.setStatus("current")
_UpsIdentModelsixth_Type = DisplayString
_UpsIdentModelsixth_Object = MibScalar
upsIdentModelsixth = _UpsIdentModelsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 2),
    _UpsIdentModelsixth_Type()
)
upsIdentModelsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelsixth.setStatus("current")
_UpsIdentUPSSoftwareVersionsixth_Type = DisplayString
_UpsIdentUPSSoftwareVersionsixth_Object = MibScalar
upsIdentUPSSoftwareVersionsixth = _UpsIdentUPSSoftwareVersionsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 3),
    _UpsIdentUPSSoftwareVersionsixth_Type()
)
upsIdentUPSSoftwareVersionsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersionsixth.setStatus("current")
_UpsIdentAgentSoftwareVersionsixth_Type = DisplayString
_UpsIdentAgentSoftwareVersionsixth_Object = MibScalar
upsIdentAgentSoftwareVersionsixth = _UpsIdentAgentSoftwareVersionsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 4),
    _UpsIdentAgentSoftwareVersionsixth_Type()
)
upsIdentAgentSoftwareVersionsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersionsixth.setStatus("current")
_UpsIdentNamesixth_Type = DisplayString
_UpsIdentNamesixth_Object = MibScalar
upsIdentNamesixth = _UpsIdentNamesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 5),
    _UpsIdentNamesixth_Type()
)
upsIdentNamesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNamesixth.setStatus("current")
_UpsIdentAttachedDevicessixth_Type = DisplayString
_UpsIdentAttachedDevicessixth_Object = MibScalar
upsIdentAttachedDevicessixth = _UpsIdentAttachedDevicessixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 6),
    _UpsIdentAttachedDevicessixth_Type()
)
upsIdentAttachedDevicessixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicessixth.setStatus("current")
_UpsIdentUPSSerialNumbersixth_Type = DisplayString
_UpsIdentUPSSerialNumbersixth_Object = MibScalar
upsIdentUPSSerialNumbersixth = _UpsIdentUPSSerialNumbersixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 7),
    _UpsIdentUPSSerialNumbersixth_Type()
)
upsIdentUPSSerialNumbersixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumbersixth.setStatus("current")
_UpsIdentComProtVersionsixth_Type = DisplayString
_UpsIdentComProtVersionsixth_Object = MibScalar
upsIdentComProtVersionsixth = _UpsIdentComProtVersionsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 8),
    _UpsIdentComProtVersionsixth_Type()
)
upsIdentComProtVersionsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersionsixth.setStatus("current")
_UpsIdentOperatingTimesixth_Type = NonNegativeInteger32
_UpsIdentOperatingTimesixth_Object = MibScalar
upsIdentOperatingTimesixth = _UpsIdentOperatingTimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 1, 9),
    _UpsIdentOperatingTimesixth_Type()
)
upsIdentOperatingTimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimesixth.setUnits("sixths")
_UpsBatterysixth_ObjectIdentity = ObjectIdentity
upsBatterysixth = _UpsBatterysixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2)
)


class _UpsBatteryStatussixth_Type(Integer32):
    """Custom type upsBatteryStatussixth based on Integer32"""
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


_UpsBatteryStatussixth_Type.__name__ = "Integer32"
_UpsBatteryStatussixth_Object = MibScalar
upsBatteryStatussixth = _UpsBatteryStatussixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 1),
    _UpsBatteryStatussixth_Type()
)
upsBatteryStatussixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatussixth.setStatus("current")
_UpsSecondsOnBatterysixth_Type = NonNegativeInteger32
_UpsSecondsOnBatterysixth_Object = MibScalar
upsSecondsOnBatterysixth = _UpsSecondsOnBatterysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 2),
    _UpsSecondsOnBatterysixth_Type()
)
upsSecondsOnBatterysixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatterysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatterysixth.setUnits("sixths")
_UpsEstimatedMinutesRemainingsixth_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingsixth_Object = MibScalar
upsEstimatedMinutesRemainingsixth = _UpsEstimatedMinutesRemainingsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 3),
    _UpsEstimatedMinutesRemainingsixth_Type()
)
upsEstimatedMinutesRemainingsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingsixth.setUnits("minutes")


class _UpsEstimatedChargeRemainingsixth_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingsixth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingsixth_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingsixth_Object = MibScalar
upsEstimatedChargeRemainingsixth = _UpsEstimatedChargeRemainingsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 4),
    _UpsEstimatedChargeRemainingsixth_Type()
)
upsEstimatedChargeRemainingsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingsixth.setUnits("percent")
_UpsBatteryVoltagesixth_Type = NonNegativeInteger32
_UpsBatteryVoltagesixth_Object = MibScalar
upsBatteryVoltagesixth = _UpsBatteryVoltagesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 5),
    _UpsBatteryVoltagesixth_Type()
)
upsBatteryVoltagesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltagesixth.setUnits("0.1 Volt DC")
_UpsBatteryCurrentsixth_Type = Integer32
_UpsBatteryCurrentsixth_Object = MibScalar
upsBatteryCurrentsixth = _UpsBatteryCurrentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 6),
    _UpsBatteryCurrentsixth_Type()
)
upsBatteryCurrentsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentsixth.setUnits("0.1 Amp DC")
_UpsBatteryTemperaturesixth_Type = Integer32
_UpsBatteryTemperaturesixth_Object = MibScalar
upsBatteryTemperaturesixth = _UpsBatteryTemperaturesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 7),
    _UpsBatteryTemperaturesixth_Type()
)
upsBatteryTemperaturesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperaturesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperaturesixth.setUnits("degrees Centigrade")
_UpsBatteryRipplesixth_Type = Integer32
_UpsBatteryRipplesixth_Object = MibScalar
upsBatteryRipplesixth = _UpsBatteryRipplesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 2, 8),
    _UpsBatteryRipplesixth_Type()
)
upsBatteryRipplesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipplesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipplesixth.setUnits("0.1 Volt RMS")
_UpsInputsixth_ObjectIdentity = ObjectIdentity
upsInputsixth = _UpsInputsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3)
)
_UpsInputLineBadssixth_Type = Counter32
_UpsInputLineBadssixth_Object = MibScalar
upsInputLineBadssixth = _UpsInputLineBadssixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 1),
    _UpsInputLineBadssixth_Type()
)
upsInputLineBadssixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadssixth.setStatus("current")
_UpsInputNumLinessixth_Type = NonNegativeInteger32
_UpsInputNumLinessixth_Object = MibScalar
upsInputNumLinessixth = _UpsInputNumLinessixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 2),
    _UpsInputNumLinessixth_Type()
)
upsInputNumLinessixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinessixth.setStatus("current")
_UpsInputSixthTable_Object = MibTable
upsInputSixthTable = _UpsInputSixthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputSixthTable.setStatus("current")
_UpsInputSixthEntry_Object = MibTableRow
upsInputSixthEntry = _UpsInputSixthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1)
)
upsInputSixthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexsixth"),
)
if mibBuilder.loadTexts:
    upsInputSixthEntry.setStatus("current")
_UpsInputLineIndexsixth_Type = PositiveInteger32
_UpsInputLineIndexsixth_Object = MibTableColumn
upsInputLineIndexsixth = _UpsInputLineIndexsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1, 1),
    _UpsInputLineIndexsixth_Type()
)
upsInputLineIndexsixth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexsixth.setStatus("current")
_UpsInputFrequencysixth_Type = NonNegativeInteger32
_UpsInputFrequencysixth_Object = MibTableColumn
upsInputFrequencysixth = _UpsInputFrequencysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1, 2),
    _UpsInputFrequencysixth_Type()
)
upsInputFrequencysixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencysixth.setUnits("0.1 Hertz")
_UpsInputVoltagesixth_Type = NonNegativeInteger32
_UpsInputVoltagesixth_Object = MibTableColumn
upsInputVoltagesixth = _UpsInputVoltagesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1, 3),
    _UpsInputVoltagesixth_Type()
)
upsInputVoltagesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltagesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltagesixth.setUnits("RMS Volts")
_UpsInputCurrentsixth_Type = NonNegativeInteger32
_UpsInputCurrentsixth_Object = MibTableColumn
upsInputCurrentsixth = _UpsInputCurrentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1, 4),
    _UpsInputCurrentsixth_Type()
)
upsInputCurrentsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentsixth.setUnits("0.1 RMS Amp")
_UpsInputTruePowersixth_Type = NonNegativeInteger32
_UpsInputTruePowersixth_Object = MibTableColumn
upsInputTruePowersixth = _UpsInputTruePowersixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1, 5),
    _UpsInputTruePowersixth_Type()
)
upsInputTruePowersixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowersixth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowersixth.setUnits("Watts")
_UpsInputVoltageMinsixth_Type = NonNegativeInteger32
_UpsInputVoltageMinsixth_Object = MibTableColumn
upsInputVoltageMinsixth = _UpsInputVoltageMinsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1, 6),
    _UpsInputVoltageMinsixth_Type()
)
upsInputVoltageMinsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMinsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMinsixth.setUnits("RMS Volts")
_UpsInputVoltageMaxsixth_Type = NonNegativeInteger32
_UpsInputVoltageMaxsixth_Object = MibTableColumn
upsInputVoltageMaxsixth = _UpsInputVoltageMaxsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 3, 3, 1, 7),
    _UpsInputVoltageMaxsixth_Type()
)
upsInputVoltageMaxsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxsixth.setUnits("RMS Volts")
_UpsOutputsixth_ObjectIdentity = ObjectIdentity
upsOutputsixth = _UpsOutputsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4)
)


class _UpsOutputSourcesixth_Type(Integer32):
    """Custom type upsOutputSourcesixth based on Integer32"""
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


_UpsOutputSourcesixth_Type.__name__ = "Integer32"
_UpsOutputSourcesixth_Object = MibScalar
upsOutputSourcesixth = _UpsOutputSourcesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 1),
    _UpsOutputSourcesixth_Type()
)
upsOutputSourcesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourcesixth.setStatus("current")
_UpsOutputFrequencysixth_Type = NonNegativeInteger32
_UpsOutputFrequencysixth_Object = MibScalar
upsOutputFrequencysixth = _UpsOutputFrequencysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 2),
    _UpsOutputFrequencysixth_Type()
)
upsOutputFrequencysixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencysixth.setUnits("0.1 Hertz")
_UpsOutputNumLinessixth_Type = NonNegativeInteger32
_UpsOutputNumLinessixth_Object = MibScalar
upsOutputNumLinessixth = _UpsOutputNumLinessixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 3),
    _UpsOutputNumLinessixth_Type()
)
upsOutputNumLinessixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinessixth.setStatus("current")
_UpsOutputSixthTable_Object = MibTable
upsOutputSixthTable = _UpsOutputSixthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputSixthTable.setStatus("current")
_UpsOutputSixthEntry_Object = MibTableRow
upsOutputSixthEntry = _UpsOutputSixthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1)
)
upsOutputSixthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexsixth"),
)
if mibBuilder.loadTexts:
    upsOutputSixthEntry.setStatus("current")
_UpsOutputLineIndexsixth_Type = PositiveInteger32
_UpsOutputLineIndexsixth_Object = MibTableColumn
upsOutputLineIndexsixth = _UpsOutputLineIndexsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 1),
    _UpsOutputLineIndexsixth_Type()
)
upsOutputLineIndexsixth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexsixth.setStatus("current")
_UpsOutputVoltagesixth_Type = NonNegativeInteger32
_UpsOutputVoltagesixth_Object = MibTableColumn
upsOutputVoltagesixth = _UpsOutputVoltagesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 2),
    _UpsOutputVoltagesixth_Type()
)
upsOutputVoltagesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltagesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltagesixth.setUnits("RMS Volts")
_UpsOutputCurrentsixth_Type = NonNegativeInteger32
_UpsOutputCurrentsixth_Object = MibTableColumn
upsOutputCurrentsixth = _UpsOutputCurrentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 3),
    _UpsOutputCurrentsixth_Type()
)
upsOutputCurrentsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentsixth.setUnits("0.1 RMS Amp")
_UpsOutputPowersixth_Type = NonNegativeInteger32
_UpsOutputPowersixth_Object = MibTableColumn
upsOutputPowersixth = _UpsOutputPowersixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 4),
    _UpsOutputPowersixth_Type()
)
upsOutputPowersixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowersixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowersixth.setUnits("Watts")


class _UpsOutputPercentLoadsixth_Type(Integer32):
    """Custom type upsOutputPercentLoadsixth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadsixth_Type.__name__ = "Integer32"
_UpsOutputPercentLoadsixth_Object = MibTableColumn
upsOutputPercentLoadsixth = _UpsOutputPercentLoadsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 5),
    _UpsOutputPercentLoadsixth_Type()
)
upsOutputPercentLoadsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadsixth.setUnits("percent")


class _UpsOutputPowerFactorsixth_Type(Integer32):
    """Custom type upsOutputPowerFactorsixth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorsixth_Type.__name__ = "Integer32"
_UpsOutputPowerFactorsixth_Object = MibTableColumn
upsOutputPowerFactorsixth = _UpsOutputPowerFactorsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 6),
    _UpsOutputPowerFactorsixth_Type()
)
upsOutputPowerFactorsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorsixth.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentsixth_Type = Integer32
_UpsOutputPeakCurrentsixth_Object = MibTableColumn
upsOutputPeakCurrentsixth = _UpsOutputPeakCurrentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 7),
    _UpsOutputPeakCurrentsixth_Type()
)
upsOutputPeakCurrentsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentsixth.setUnits("Amps")
_UpsOutputShareCurrentsixth_Type = Integer32
_UpsOutputShareCurrentsixth_Object = MibTableColumn
upsOutputShareCurrentsixth = _UpsOutputShareCurrentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 4, 4, 1, 8),
    _UpsOutputShareCurrentsixth_Type()
)
upsOutputShareCurrentsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentsixth.setUnits("Amps")
_UpsBypasssixth_ObjectIdentity = ObjectIdentity
upsBypasssixth = _UpsBypasssixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5)
)
_UpsBypassFrequencysixth_Type = NonNegativeInteger32
_UpsBypassFrequencysixth_Object = MibScalar
upsBypassFrequencysixth = _UpsBypassFrequencysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 1),
    _UpsBypassFrequencysixth_Type()
)
upsBypassFrequencysixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencysixth.setUnits("0.1 Hertz")
_UpsBypassNumLinessixth_Type = NonNegativeInteger32
_UpsBypassNumLinessixth_Object = MibScalar
upsBypassNumLinessixth = _UpsBypassNumLinessixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 2),
    _UpsBypassNumLinessixth_Type()
)
upsBypassNumLinessixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinessixth.setStatus("current")
_UpsBypassSixthTable_Object = MibTable
upsBypassSixthTable = _UpsBypassSixthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassSixthTable.setStatus("current")
_UpsBypassSixthEntry_Object = MibTableRow
upsBypassSixthEntry = _UpsBypassSixthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 3, 1)
)
upsBypassSixthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexsixth"),
)
if mibBuilder.loadTexts:
    upsBypassSixthEntry.setStatus("current")
_UpsBypassLineIndexsixth_Type = PositiveInteger32
_UpsBypassLineIndexsixth_Object = MibTableColumn
upsBypassLineIndexsixth = _UpsBypassLineIndexsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 3, 1, 1),
    _UpsBypassLineIndexsixth_Type()
)
upsBypassLineIndexsixth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexsixth.setStatus("current")
_UpsBypassVoltagesixth_Type = NonNegativeInteger32
_UpsBypassVoltagesixth_Object = MibTableColumn
upsBypassVoltagesixth = _UpsBypassVoltagesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 3, 1, 2),
    _UpsBypassVoltagesixth_Type()
)
upsBypassVoltagesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltagesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltagesixth.setUnits("RMS Volts")
_UpsBypassCurrentsixth_Type = NonNegativeInteger32
_UpsBypassCurrentsixth_Object = MibTableColumn
upsBypassCurrentsixth = _UpsBypassCurrentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 3, 1, 3),
    _UpsBypassCurrentsixth_Type()
)
upsBypassCurrentsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentsixth.setUnits("0.1 RMS Amp")
_UpsBypassPowersixth_Type = NonNegativeInteger32
_UpsBypassPowersixth_Object = MibTableColumn
upsBypassPowersixth = _UpsBypassPowersixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 5, 3, 1, 4),
    _UpsBypassPowersixth_Type()
)
upsBypassPowersixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowersixth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowersixth.setUnits("Watts")
_UpsAlarmsixth_ObjectIdentity = ObjectIdentity
upsAlarmsixth = _UpsAlarmsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6)
)
_UpsAlarmsPresentsixth_Type = Gauge32
_UpsAlarmsPresentsixth_Object = MibScalar
upsAlarmsPresentsixth = _UpsAlarmsPresentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 1),
    _UpsAlarmsPresentsixth_Type()
)
upsAlarmsPresentsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentsixth.setStatus("current")
_UpsAlarmSixthTable_Object = MibTable
upsAlarmSixthTable = _UpsAlarmSixthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmSixthTable.setStatus("current")
_UpsAlarmSixthEntry_Object = MibTableRow
upsAlarmSixthEntry = _UpsAlarmSixthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 2, 1)
)
upsAlarmSixthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdsixth"),
)
if mibBuilder.loadTexts:
    upsAlarmSixthEntry.setStatus("current")
_UpsAlarmIdsixth_Type = PositiveInteger32
_UpsAlarmIdsixth_Object = MibTableColumn
upsAlarmIdsixth = _UpsAlarmIdsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 2, 1, 1),
    _UpsAlarmIdsixth_Type()
)
upsAlarmIdsixth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdsixth.setStatus("current")
_UpsAlarmDescrsixth_Type = AutonomousType
_UpsAlarmDescrsixth_Object = MibTableColumn
upsAlarmDescrsixth = _UpsAlarmDescrsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 2, 1, 2),
    _UpsAlarmDescrsixth_Type()
)
upsAlarmDescrsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrsixth.setStatus("current")
_UpsAlarmTimesixth_Type = TimeStamp
_UpsAlarmTimesixth_Object = MibTableColumn
upsAlarmTimesixth = _UpsAlarmTimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 2, 1, 3),
    _UpsAlarmTimesixth_Type()
)
upsAlarmTimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimesixth.setStatus("current")
_UpsWellKnownAlarmssixth_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmssixth = _UpsWellKnownAlarmssixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3)
)
_UpsAlarmBatteryBadsixth_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadsixth = _UpsAlarmBatteryBadsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadsixth.setStatus("current")
_UpsAlarmOnBatterysixth_ObjectIdentity = ObjectIdentity
upsAlarmOnBatterysixth = _UpsAlarmOnBatterysixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatterysixth.setStatus("current")
_UpsAlarmLowBatterysixth_ObjectIdentity = ObjectIdentity
upsAlarmLowBatterysixth = _UpsAlarmLowBatterysixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatterysixth.setStatus("current")
_UpsAlarmDepletedBatterysixth_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatterysixth = _UpsAlarmDepletedBatterysixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatterysixth.setStatus("current")
_UpsAlarmTempBadsixth_ObjectIdentity = ObjectIdentity
upsAlarmTempBadsixth = _UpsAlarmTempBadsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadsixth.setStatus("current")
_UpsAlarmInputBadsixth_ObjectIdentity = ObjectIdentity
upsAlarmInputBadsixth = _UpsAlarmInputBadsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadsixth.setStatus("current")
_UpsAlarmOutputBadsixth_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadsixth = _UpsAlarmOutputBadsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadsixth.setStatus("current")
_UpsAlarmOutputOverloadsixth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadsixth = _UpsAlarmOutputOverloadsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadsixth.setStatus("current")
_UpsAlarmOnBypasssixth_ObjectIdentity = ObjectIdentity
upsAlarmOnBypasssixth = _UpsAlarmOnBypasssixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypasssixth.setStatus("current")
_UpsAlarmBypassBadsixth_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadsixth = _UpsAlarmBypassBadsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadsixth.setStatus("current")
_UpsAlarmOutputOffAsRequestedsixth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedsixth = _UpsAlarmOutputOffAsRequestedsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedsixth.setStatus("current")
_UpsAlarmUpsOffAsRequestedsixth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedsixth = _UpsAlarmUpsOffAsRequestedsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedsixth.setStatus("current")
_UpsAlarmChargerFailedsixth_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedsixth = _UpsAlarmChargerFailedsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedsixth.setStatus("current")
_UpsAlarmUpsOutputOffsixth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOffsixth = _UpsAlarmUpsOutputOffsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOffsixth.setStatus("current")
_UpsAlarmUpsSystemOffsixth_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOffsixth = _UpsAlarmUpsSystemOffsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOffsixth.setStatus("current")
_UpsAlarmFanFailuresixth_ObjectIdentity = ObjectIdentity
upsAlarmFanFailuresixth = _UpsAlarmFanFailuresixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailuresixth.setStatus("current")
_UpsAlarmFuseFailuresixth_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailuresixth = _UpsAlarmFuseFailuresixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailuresixth.setStatus("current")
_UpsAlarmGeneralFaultsixth_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultsixth = _UpsAlarmGeneralFaultsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultsixth.setStatus("current")
_UpsAlarmDiagnosticTestFailedsixth_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedsixth = _UpsAlarmDiagnosticTestFailedsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedsixth.setStatus("current")
_UpsAlarmCommunicationsLostsixth_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostsixth = _UpsAlarmCommunicationsLostsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostsixth.setStatus("current")
_UpsAlarmAwaitingPowersixth_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowersixth = _UpsAlarmAwaitingPowersixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowersixth.setStatus("current")
_UpsAlarmShutdownPendingsixth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingsixth = _UpsAlarmShutdownPendingsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingsixth.setStatus("current")
_UpsAlarmShutdownImminentsixth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentsixth = _UpsAlarmShutdownImminentsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentsixth.setStatus("current")
_UpsAlarmTestInProgresssixth_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgresssixth = _UpsAlarmTestInProgresssixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgresssixth.setStatus("current")
_UpsAlarmReceptacleOffsixth_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOffsixth = _UpsAlarmReceptacleOffsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOffsixth.setStatus("current")
_UpsAlarmHighSpeedBusFailuresixth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailuresixth = _UpsAlarmHighSpeedBusFailuresixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailuresixth.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailuresixth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailuresixth = _UpsAlarmHighSpeedBusJACRCFailuresixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailuresixth.setStatus("current")
_UpsAlarmConnectivityBusFailuresixth_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailuresixth = _UpsAlarmConnectivityBusFailuresixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailuresixth.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailuresixth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailuresixth = _UpsAlarmHighSpeedBusJBCRCFailuresixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailuresixth.setStatus("current")
_UpsAlarmCurrentSharingsixth_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingsixth = _UpsAlarmCurrentSharingsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingsixth.setStatus("current")
_UpsAlarmDCRipplesixth_ObjectIdentity = ObjectIdentity
upsAlarmDCRipplesixth = _UpsAlarmDCRipplesixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipplesixth.setStatus("current")
_UpsAlarmMaskAsixth_Type = Unsigned32
_UpsAlarmMaskAsixth_Object = MibScalar
upsAlarmMaskAsixth = _UpsAlarmMaskAsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 6, 4),
    _UpsAlarmMaskAsixth_Type()
)
upsAlarmMaskAsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAsixth.setStatus("current")
_UpsTestsixth_ObjectIdentity = ObjectIdentity
upsTestsixth = _UpsTestsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7)
)
_UpsTestIdsixth_Type = ObjectIdentifier
_UpsTestIdsixth_Object = MibScalar
upsTestIdsixth = _UpsTestIdsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 1),
    _UpsTestIdsixth_Type()
)
upsTestIdsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdsixth.setStatus("current")
_UpsTestSpinLocksixth_Type = TestAndIncr
_UpsTestSpinLocksixth_Object = MibScalar
upsTestSpinLocksixth = _UpsTestSpinLocksixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 2),
    _UpsTestSpinLocksixth_Type()
)
upsTestSpinLocksixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLocksixth.setStatus("current")


class _UpsTestResultsSummarysixth_Type(Integer32):
    """Custom type upsTestResultsSummarysixth based on Integer32"""
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


_UpsTestResultsSummarysixth_Type.__name__ = "Integer32"
_UpsTestResultsSummarysixth_Object = MibScalar
upsTestResultsSummarysixth = _UpsTestResultsSummarysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 3),
    _UpsTestResultsSummarysixth_Type()
)
upsTestResultsSummarysixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummarysixth.setStatus("current")
_UpsTestResultsDetailsixth_Type = DisplayString
_UpsTestResultsDetailsixth_Object = MibScalar
upsTestResultsDetailsixth = _UpsTestResultsDetailsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 4),
    _UpsTestResultsDetailsixth_Type()
)
upsTestResultsDetailsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailsixth.setStatus("current")
_UpsTestStartTimesixth_Type = TimeStamp
_UpsTestStartTimesixth_Object = MibScalar
upsTestStartTimesixth = _UpsTestStartTimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 5),
    _UpsTestStartTimesixth_Type()
)
upsTestStartTimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimesixth.setStatus("current")
_UpsTestElapsedTimesixth_Type = TimeInterval
_UpsTestElapsedTimesixth_Object = MibScalar
upsTestElapsedTimesixth = _UpsTestElapsedTimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 6),
    _UpsTestElapsedTimesixth_Type()
)
upsTestElapsedTimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimesixth.setStatus("current")
_UpsWellKnownTestssixth_ObjectIdentity = ObjectIdentity
upsWellKnownTestssixth = _UpsWellKnownTestssixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 7)
)
_UpsTestNoTestsInitiatedsixth_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedsixth = _UpsTestNoTestsInitiatedsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedsixth.setStatus("current")
_UpsTestAbortTestInProgresssixth_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgresssixth = _UpsTestAbortTestInProgresssixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgresssixth.setStatus("current")
_UpsTestGeneralSystemsTestsixth_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestsixth = _UpsTestGeneralSystemsTestsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestsixth.setStatus("current")
_UpsTestQuickBatteryTestsixth_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestsixth = _UpsTestQuickBatteryTestsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestsixth.setStatus("current")
_UpsTestDeepBatteryCalibrationsixth_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationsixth = _UpsTestDeepBatteryCalibrationsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationsixth.setStatus("current")
_UpsControlsixth_ObjectIdentity = ObjectIdentity
upsControlsixth = _UpsControlsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8)
)


class _UpsShutdownTypesixth_Type(Integer32):
    """Custom type upsShutdownTypesixth based on Integer32"""
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


_UpsShutdownTypesixth_Type.__name__ = "Integer32"
_UpsShutdownTypesixth_Object = MibScalar
upsShutdownTypesixth = _UpsShutdownTypesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 1),
    _UpsShutdownTypesixth_Type()
)
upsShutdownTypesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypesixth.setStatus("current")


class _UpsShutdownAfterDelaysixth_Type(Integer32):
    """Custom type upsShutdownAfterDelaysixth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelaysixth_Type.__name__ = "Integer32"
_UpsShutdownAfterDelaysixth_Object = MibScalar
upsShutdownAfterDelaysixth = _UpsShutdownAfterDelaysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 2),
    _UpsShutdownAfterDelaysixth_Type()
)
upsShutdownAfterDelaysixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaysixth.setUnits("sixths")


class _UpsStartupAfterDelaysixth_Type(Integer32):
    """Custom type upsStartupAfterDelaysixth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelaysixth_Type.__name__ = "Integer32"
_UpsStartupAfterDelaysixth_Object = MibScalar
upsStartupAfterDelaysixth = _UpsStartupAfterDelaysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 3),
    _UpsStartupAfterDelaysixth_Type()
)
upsStartupAfterDelaysixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelaysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelaysixth.setUnits("sixths")


class _UpsRebootWithDurationsixth_Type(Integer32):
    """Custom type upsRebootWithDurationsixth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationsixth_Type.__name__ = "Integer32"
_UpsRebootWithDurationsixth_Object = MibScalar
upsRebootWithDurationsixth = _UpsRebootWithDurationsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 4),
    _UpsRebootWithDurationsixth_Type()
)
upsRebootWithDurationsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationsixth.setUnits("sixths")


class _UpsAutoRestartsixth_Type(Integer32):
    """Custom type upsAutoRestartsixth based on Integer32"""
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


_UpsAutoRestartsixth_Type.__name__ = "Integer32"
_UpsAutoRestartsixth_Object = MibScalar
upsAutoRestartsixth = _UpsAutoRestartsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 5),
    _UpsAutoRestartsixth_Type()
)
upsAutoRestartsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartsixth.setStatus("current")
_UpsReceptaclesNumsixth_Type = NonNegativeInteger32
_UpsReceptaclesNumsixth_Object = MibScalar
upsReceptaclesNumsixth = _UpsReceptaclesNumsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 6),
    _UpsReceptaclesNumsixth_Type()
)
upsReceptaclesNumsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumsixth.setStatus("current")
_UpsReceptacleSixthTable_Object = MibTable
upsReceptacleSixthTable = _UpsReceptacleSixthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleSixthTable.setStatus("current")
_UpsReceptacleSixthEntry_Object = MibTableRow
upsReceptacleSixthEntry = _UpsReceptacleSixthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 7, 1)
)
upsReceptacleSixthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexsixth"),
)
if mibBuilder.loadTexts:
    upsReceptacleSixthEntry.setStatus("current")
_UpsReceptacleLineIndexsixth_Type = PositiveInteger32
_UpsReceptacleLineIndexsixth_Object = MibTableColumn
upsReceptacleLineIndexsixth = _UpsReceptacleLineIndexsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 7, 1, 1),
    _UpsReceptacleLineIndexsixth_Type()
)
upsReceptacleLineIndexsixth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexsixth.setStatus("current")


class _UpsReceptacleOnOffsixth_Type(Integer32):
    """Custom type upsReceptacleOnOffsixth based on Integer32"""
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


_UpsReceptacleOnOffsixth_Type.__name__ = "Integer32"
_UpsReceptacleOnOffsixth_Object = MibTableColumn
upsReceptacleOnOffsixth = _UpsReceptacleOnOffsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 7, 1, 2),
    _UpsReceptacleOnOffsixth_Type()
)
upsReceptacleOnOffsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOffsixth.setStatus("current")


class _UpsUPSModesixth_Type(Integer32):
    """Custom type upsUPSModesixth based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModesixth_Type.__name__ = "Integer32"
_UpsUPSModesixth_Object = MibScalar
upsUPSModesixth = _UpsUPSModesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 8),
    _UpsUPSModesixth_Type()
)
upsUPSModesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModesixth.setStatus("current")


class _UpsRectifierOnOffsixth_Type(Integer32):
    """Custom type upsRectifierOnOffsixth based on Integer32"""
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


_UpsRectifierOnOffsixth_Type.__name__ = "Integer32"
_UpsRectifierOnOffsixth_Object = MibScalar
upsRectifierOnOffsixth = _UpsRectifierOnOffsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 9),
    _UpsRectifierOnOffsixth_Type()
)
upsRectifierOnOffsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOffsixth.setStatus("current")


class _UpsBatteryChargeMethodsixth_Type(Integer32):
    """Custom type upsBatteryChargeMethodsixth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodsixth_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodsixth_Object = MibScalar
upsBatteryChargeMethodsixth = _UpsBatteryChargeMethodsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 10),
    _UpsBatteryChargeMethodsixth_Type()
)
upsBatteryChargeMethodsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodsixth.setStatus("current")


class _UpsInverterOnOffsixth_Type(Integer32):
    """Custom type upsInverterOnOffsixth based on Integer32"""
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


_UpsInverterOnOffsixth_Type.__name__ = "Integer32"
_UpsInverterOnOffsixth_Object = MibScalar
upsInverterOnOffsixth = _UpsInverterOnOffsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 11),
    _UpsInverterOnOffsixth_Type()
)
upsInverterOnOffsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOffsixth.setStatus("current")


class _UpsBypassOnOffsixth_Type(Integer32):
    """Custom type upsBypassOnOffsixth based on Integer32"""
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


_UpsBypassOnOffsixth_Type.__name__ = "Integer32"
_UpsBypassOnOffsixth_Object = MibScalar
upsBypassOnOffsixth = _UpsBypassOnOffsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 12),
    _UpsBypassOnOffsixth_Type()
)
upsBypassOnOffsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOffsixth.setStatus("current")


class _UpsLoadSourcesixth_Type(Integer32):
    """Custom type upsLoadSourcesixth based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourcesixth_Type.__name__ = "Integer32"
_UpsLoadSourcesixth_Object = MibScalar
upsLoadSourcesixth = _UpsLoadSourcesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 8, 13),
    _UpsLoadSourcesixth_Type()
)
upsLoadSourcesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourcesixth.setStatus("current")
_UpsConfigsixth_ObjectIdentity = ObjectIdentity
upsConfigsixth = _UpsConfigsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9)
)
_UpsConfigInputVoltagesixth_Type = NonNegativeInteger32
_UpsConfigInputVoltagesixth_Object = MibScalar
upsConfigInputVoltagesixth = _UpsConfigInputVoltagesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 1),
    _UpsConfigInputVoltagesixth_Type()
)
upsConfigInputVoltagesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltagesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltagesixth.setUnits("RMS Volts")
_UpsConfigInputFreqsixth_Type = NonNegativeInteger32
_UpsConfigInputFreqsixth_Object = MibScalar
upsConfigInputFreqsixth = _UpsConfigInputFreqsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 2),
    _UpsConfigInputFreqsixth_Type()
)
upsConfigInputFreqsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqsixth.setUnits("0.1 Hertz")
_UpsConfigOutputVoltagesixth_Type = NonNegativeInteger32
_UpsConfigOutputVoltagesixth_Object = MibScalar
upsConfigOutputVoltagesixth = _UpsConfigOutputVoltagesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 3),
    _UpsConfigOutputVoltagesixth_Type()
)
upsConfigOutputVoltagesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagesixth.setUnits("RMS Volts")
_UpsConfigOutputFreqsixth_Type = NonNegativeInteger32
_UpsConfigOutputFreqsixth_Object = MibScalar
upsConfigOutputFreqsixth = _UpsConfigOutputFreqsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 4),
    _UpsConfigOutputFreqsixth_Type()
)
upsConfigOutputFreqsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqsixth.setUnits("0.1 Hertz")
_UpsConfigOutputVAsixth_Type = NonNegativeInteger32
_UpsConfigOutputVAsixth_Object = MibScalar
upsConfigOutputVAsixth = _UpsConfigOutputVAsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 5),
    _UpsConfigOutputVAsixth_Type()
)
upsConfigOutputVAsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAsixth.setUnits("Volt-Amps")
_UpsConfigOutputPowersixth_Type = NonNegativeInteger32
_UpsConfigOutputPowersixth_Object = MibScalar
upsConfigOutputPowersixth = _UpsConfigOutputPowersixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 6),
    _UpsConfigOutputPowersixth_Type()
)
upsConfigOutputPowersixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowersixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowersixth.setUnits("Watts")
_UpsConfigLowBattTimesixth_Type = NonNegativeInteger32
_UpsConfigLowBattTimesixth_Object = MibScalar
upsConfigLowBattTimesixth = _UpsConfigLowBattTimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 7),
    _UpsConfigLowBattTimesixth_Type()
)
upsConfigLowBattTimesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimesixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimesixth.setUnits("minutes")


class _UpsConfigAudibleStatussixth_Type(Integer32):
    """Custom type upsConfigAudibleStatussixth based on Integer32"""
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


_UpsConfigAudibleStatussixth_Type.__name__ = "Integer32"
_UpsConfigAudibleStatussixth_Object = MibScalar
upsConfigAudibleStatussixth = _UpsConfigAudibleStatussixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 8),
    _UpsConfigAudibleStatussixth_Type()
)
upsConfigAudibleStatussixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatussixth.setStatus("current")
_UpsConfigLowVoltageTransferPointsixth_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointsixth_Object = MibScalar
upsConfigLowVoltageTransferPointsixth = _UpsConfigLowVoltageTransferPointsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 9),
    _UpsConfigLowVoltageTransferPointsixth_Type()
)
upsConfigLowVoltageTransferPointsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointsixth.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointsixth_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointsixth_Object = MibScalar
upsConfigHighVoltageTransferPointsixth = _UpsConfigHighVoltageTransferPointsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 10),
    _UpsConfigHighVoltageTransferPointsixth_Type()
)
upsConfigHighVoltageTransferPointsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointsixth.setUnits("RMS Volts")
_UpsConfigBatteryCapacitysixth_Type = NonNegativeInteger32
_UpsConfigBatteryCapacitysixth_Object = MibScalar
upsConfigBatteryCapacitysixth = _UpsConfigBatteryCapacitysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 11),
    _UpsConfigBatteryCapacitysixth_Type()
)
upsConfigBatteryCapacitysixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitysixth.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentsixth_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentsixth_Object = MibScalar
upsConfigBatteryChargeCurrentsixth = _UpsConfigBatteryChargeCurrentsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 12),
    _UpsConfigBatteryChargeCurrentsixth_Type()
)
upsConfigBatteryChargeCurrentsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentsixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentsixth.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdownsixth_Type(Integer32):
    """Custom type upsConfigNoLoadShutdownsixth based on Integer32"""
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


_UpsConfigNoLoadShutdownsixth_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdownsixth_Object = MibScalar
upsConfigNoLoadShutdownsixth = _UpsConfigNoLoadShutdownsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 13),
    _UpsConfigNoLoadShutdownsixth_Type()
)
upsConfigNoLoadShutdownsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdownsixth.setStatus("current")
_UpsConfigStartDelaysixth_Type = PositiveInteger32
_UpsConfigStartDelaysixth_Object = MibScalar
upsConfigStartDelaysixth = _UpsConfigStartDelaysixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 9, 14),
    _UpsConfigStartDelaysixth_Type()
)
upsConfigStartDelaysixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelaysixth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelaysixth.setUnits("minutes")
_UpsGetSetsixth_ObjectIdentity = ObjectIdentity
upsGetSetsixth = _UpsGetSetsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10)
)
_UpsEventGetNextsixth_Type = PositiveInteger32
_UpsEventGetNextsixth_Object = MibScalar
upsEventGetNextsixth = _UpsEventGetNextsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 1),
    _UpsEventGetNextsixth_Type()
)
upsEventGetNextsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextsixth.setStatus("current")
_UpsEventGetPrevioussixth_Type = PositiveInteger32
_UpsEventGetPrevioussixth_Object = MibScalar
upsEventGetPrevioussixth = _UpsEventGetPrevioussixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 2),
    _UpsEventGetPrevioussixth_Type()
)
upsEventGetPrevioussixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPrevioussixth.setStatus("current")
_UpsEventSetStartingTimeStampsixth_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampsixth_Object = MibScalar
upsEventSetStartingTimeStampsixth = _UpsEventSetStartingTimeStampsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 3),
    _UpsEventSetStartingTimeStampsixth_Type()
)
upsEventSetStartingTimeStampsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampsixth.setStatus("current")
_UpsEventRetreiveCurrentTimeStampsixth_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampsixth_Object = MibScalar
upsEventRetreiveCurrentTimeStampsixth = _UpsEventRetreiveCurrentTimeStampsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 4),
    _UpsEventRetreiveCurrentTimeStampsixth_Type()
)
upsEventRetreiveCurrentTimeStampsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampsixth.setStatus("current")
_UpsEventTableSizesixth_Type = NonNegativeInteger32
_UpsEventTableSizesixth_Object = MibScalar
upsEventTableSizesixth = _UpsEventTableSizesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 5),
    _UpsEventTableSizesixth_Type()
)
upsEventTableSizesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizesixth.setStatus("current")
_UpsEventSixthTable_Object = MibTable
upsEventSixthTable = _UpsEventSixthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventSixthTable.setStatus("current")
_UpsEventSixthEntry_Object = MibTableRow
upsEventSixthEntry = _UpsEventSixthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 6, 1)
)
upsEventSixthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexsixth"),
)
if mibBuilder.loadTexts:
    upsEventSixthEntry.setStatus("current")
_UpsEventLineIndexsixth_Type = PositiveInteger32
_UpsEventLineIndexsixth_Object = MibTableColumn
upsEventLineIndexsixth = _UpsEventLineIndexsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 6, 1, 1),
    _UpsEventLineIndexsixth_Type()
)
upsEventLineIndexsixth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexsixth.setStatus("current")
_UpsEventCodesixth_Type = Integer32
_UpsEventCodesixth_Object = MibTableColumn
upsEventCodesixth = _UpsEventCodesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 6, 1, 2),
    _UpsEventCodesixth_Type()
)
upsEventCodesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodesixth.setStatus("current")
_UpsEventStatussixth_Type = NonNegativeInteger32
_UpsEventStatussixth_Object = MibTableColumn
upsEventStatussixth = _UpsEventStatussixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 6, 1, 3),
    _UpsEventStatussixth_Type()
)
upsEventStatussixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatussixth.setStatus("current")
_UpsEventTimesixth_Type = NonNegativeInteger32
_UpsEventTimesixth_Object = MibTableColumn
upsEventTimesixth = _UpsEventTimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 6, 1, 4),
    _UpsEventTimesixth_Type()
)
upsEventTimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimesixth.setStatus("current")
_UpsParametersReadsixth_Type = PositiveInteger32
_UpsParametersReadsixth_Object = MibScalar
upsParametersReadsixth = _UpsParametersReadsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 7),
    _UpsParametersReadsixth_Type()
)
upsParametersReadsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadsixth.setStatus("current")
_UpsParametersWritesixth_Type = PositiveInteger32
_UpsParametersWritesixth_Object = MibScalar
upsParametersWritesixth = _UpsParametersWritesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 8),
    _UpsParametersWritesixth_Type()
)
upsParametersWritesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWritesixth.setStatus("current")
_UpsParametersStartAddresssixth_Type = NonNegativeInteger32
_UpsParametersStartAddresssixth_Object = MibScalar
upsParametersStartAddresssixth = _UpsParametersStartAddresssixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 9),
    _UpsParametersStartAddresssixth_Type()
)
upsParametersStartAddresssixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddresssixth.setStatus("current")
_UpsParameterTableSizesixth_Type = NonNegativeInteger32
_UpsParameterTableSizesixth_Object = MibScalar
upsParameterTableSizesixth = _UpsParameterTableSizesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 10),
    _UpsParameterTableSizesixth_Type()
)
upsParameterTableSizesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizesixth.setStatus("current")
_UpsParameterSixthTable_Object = MibTable
upsParameterSixthTable = _UpsParameterSixthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterSixthTable.setStatus("current")
_UpsParameterSixthEntry_Object = MibTableRow
upsParameterSixthEntry = _UpsParameterSixthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 11, 1)
)
upsParameterSixthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexsixth"),
)
if mibBuilder.loadTexts:
    upsParameterSixthEntry.setStatus("current")
_UpsParameterLineIndexsixth_Type = PositiveInteger32
_UpsParameterLineIndexsixth_Object = MibTableColumn
upsParameterLineIndexsixth = _UpsParameterLineIndexsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 11, 1, 1),
    _UpsParameterLineIndexsixth_Type()
)
upsParameterLineIndexsixth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexsixth.setStatus("current")
_UpsParameterValuesixth_Type = Integer32
_UpsParameterValuesixth_Object = MibTableColumn
upsParameterValuesixth = _UpsParameterValuesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 11, 1, 2),
    _UpsParameterValuesixth_Type()
)
upsParameterValuesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValuesixth.setStatus("current")
_UpsStatussixth_Type = NonNegativeInteger32
_UpsStatussixth_Object = MibScalar
upsStatussixth = _UpsStatussixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 12),
    _UpsStatussixth_Type()
)
upsStatussixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatussixth.setStatus("current")
_UpsMainsStatisticsMBfailsixth_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailsixth_Object = MibScalar
upsMainsStatisticsMBfailsixth = _UpsMainsStatisticsMBfailsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 13),
    _UpsMainsStatisticsMBfailsixth_Type()
)
upsMainsStatisticsMBfailsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailsixth.setStatus("current")
_UpsMainsStatisticsMRfailsixth_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailsixth_Object = MibScalar
upsMainsStatisticsMRfailsixth = _UpsMainsStatisticsMRfailsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 14),
    _UpsMainsStatisticsMRfailsixth_Type()
)
upsMainsStatisticsMRfailsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailsixth.setStatus("current")
_UpsMainsStatisticsB2sixth_Type = NonNegativeInteger32
_UpsMainsStatisticsB2sixth_Object = MibScalar
upsMainsStatisticsB2sixth = _UpsMainsStatisticsB2sixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 15),
    _UpsMainsStatisticsB2sixth_Type()
)
upsMainsStatisticsB2sixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2sixth.setStatus("current")
_UpsMainsStatisticsB5sixth_Type = NonNegativeInteger32
_UpsMainsStatisticsB5sixth_Object = MibScalar
upsMainsStatisticsB5sixth = _UpsMainsStatisticsB5sixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 16),
    _UpsMainsStatisticsB5sixth_Type()
)
upsMainsStatisticsB5sixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5sixth.setStatus("current")
_UpsMainsStatisticsB10sixth_Type = NonNegativeInteger32
_UpsMainsStatisticsB10sixth_Object = MibScalar
upsMainsStatisticsB10sixth = _UpsMainsStatisticsB10sixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 17),
    _UpsMainsStatisticsB10sixth_Type()
)
upsMainsStatisticsB10sixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10sixth.setStatus("current")
_UpsMainsStatisticsB200sixth_Type = NonNegativeInteger32
_UpsMainsStatisticsB200sixth_Object = MibScalar
upsMainsStatisticsB200sixth = _UpsMainsStatisticsB200sixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 18),
    _UpsMainsStatisticsB200sixth_Type()
)
upsMainsStatisticsB200sixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200sixth.setStatus("current")
_UpsMainsStatisticsBypRelsixth_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelsixth_Object = MibScalar
upsMainsStatisticsBypRelsixth = _UpsMainsStatisticsBypRelsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 19),
    _UpsMainsStatisticsBypRelsixth_Type()
)
upsMainsStatisticsBypRelsixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelsixth.setStatus("current")
_UpsTimesixth_Type = NonNegativeInteger32
_UpsTimesixth_Object = MibScalar
upsTimesixth = _UpsTimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 20),
    _UpsTimesixth_Type()
)
upsTimesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimesixth.setStatus("current")
_UpsRequestPermissionsixth_Type = DisplayString
_UpsRequestPermissionsixth_Object = MibScalar
upsRequestPermissionsixth = _UpsRequestPermissionsixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 21),
    _UpsRequestPermissionsixth_Type()
)
upsRequestPermissionsixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissionsixth.setStatus("current")
_UpsEventGetCodesixth_Type = Integer32
_UpsEventGetCodesixth_Object = MibScalar
upsEventGetCodesixth = _UpsEventGetCodesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 22),
    _UpsEventGetCodesixth_Type()
)
upsEventGetCodesixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodesixth.setStatus("current")
_UpsEventSpinLocksixth_Type = TestAndIncr
_UpsEventSpinLocksixth_Object = MibScalar
upsEventSpinLocksixth = _UpsEventSpinLocksixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 23),
    _UpsEventSpinLocksixth_Type()
)
upsEventSpinLocksixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLocksixth.setStatus("current")
_UpsParameterSpinLocksixth_Type = TestAndIncr
_UpsParameterSpinLocksixth_Object = MibScalar
upsParameterSpinLocksixth = _UpsParameterSpinLocksixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 10, 24),
    _UpsParameterSpinLocksixth_Type()
)
upsParameterSpinLocksixth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLocksixth.setStatus("current")
_GeUPSTrapssixth_ObjectIdentity = ObjectIdentity
geUPSTrapssixth = _GeUPSTrapssixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11)
)
_UpsDiagnosticsixth_ObjectIdentity = ObjectIdentity
upsDiagnosticsixth = _UpsDiagnosticsixth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12)
)
_UpsDiagnosticBusJACommunicationStatussixth_Type = Integer32
_UpsDiagnosticBusJACommunicationStatussixth_Object = MibScalar
upsDiagnosticBusJACommunicationStatussixth = _UpsDiagnosticBusJACommunicationStatussixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12, 1),
    _UpsDiagnosticBusJACommunicationStatussixth_Type()
)
upsDiagnosticBusJACommunicationStatussixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatussixth.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatussixth_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatussixth_Object = MibScalar
upsDiagnosticBusJBCommunicationStatussixth = _UpsDiagnosticBusJBCommunicationStatussixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatussixth_Type()
)
upsDiagnosticBusJBCommunicationStatussixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatussixth.setStatus("current")
_UpsDiagnosticBatteryLifetimesixth_Type = Integer32
_UpsDiagnosticBatteryLifetimesixth_Object = MibScalar
upsDiagnosticBatteryLifetimesixth = _UpsDiagnosticBatteryLifetimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12, 3),
    _UpsDiagnosticBatteryLifetimesixth_Type()
)
upsDiagnosticBatteryLifetimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimesixth.setStatus("current")
_UpsDiagnosticFansLifetimesixth_Type = Integer32
_UpsDiagnosticFansLifetimesixth_Object = MibScalar
upsDiagnosticFansLifetimesixth = _UpsDiagnosticFansLifetimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12, 4),
    _UpsDiagnosticFansLifetimesixth_Type()
)
upsDiagnosticFansLifetimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimesixth.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimesixth_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimesixth_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimesixth = _UpsDiagnosticDCcapacitorsLifetimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimesixth_Type()
)
upsDiagnosticDCcapacitorsLifetimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimesixth.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimesixth_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimesixth_Object = MibScalar
upsDiagnosticACcapacitorsLifetimesixth = _UpsDiagnosticACcapacitorsLifetimesixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimesixth_Type()
)
upsDiagnosticACcapacitorsLifetimesixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimesixth.setStatus("current")
_UpsDiagnosticGlobalServiceChecksixth_Type = Integer32
_UpsDiagnosticGlobalServiceChecksixth_Object = MibScalar
upsDiagnosticGlobalServiceChecksixth = _UpsDiagnosticGlobalServiceChecksixth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 12, 7),
    _UpsDiagnosticGlobalServiceChecksixth_Type()
)
upsDiagnosticGlobalServiceChecksixth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceChecksixth.setStatus("current")
_GeSeventhUPS_ObjectIdentity = ObjectIdentity
geSeventhUPS = _GeSeventhUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17)
)
_UpsIdentseventh_ObjectIdentity = ObjectIdentity
upsIdentseventh = _UpsIdentseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1)
)
_UpsIdentManufacturerseventh_Type = DisplayString
_UpsIdentManufacturerseventh_Object = MibScalar
upsIdentManufacturerseventh = _UpsIdentManufacturerseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 1),
    _UpsIdentManufacturerseventh_Type()
)
upsIdentManufacturerseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturerseventh.setStatus("current")
_UpsIdentModelseventh_Type = DisplayString
_UpsIdentModelseventh_Object = MibScalar
upsIdentModelseventh = _UpsIdentModelseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 2),
    _UpsIdentModelseventh_Type()
)
upsIdentModelseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelseventh.setStatus("current")
_UpsIdentUPSSoftwareVersionseventh_Type = DisplayString
_UpsIdentUPSSoftwareVersionseventh_Object = MibScalar
upsIdentUPSSoftwareVersionseventh = _UpsIdentUPSSoftwareVersionseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 3),
    _UpsIdentUPSSoftwareVersionseventh_Type()
)
upsIdentUPSSoftwareVersionseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersionseventh.setStatus("current")
_UpsIdentAgentSoftwareVersionseventh_Type = DisplayString
_UpsIdentAgentSoftwareVersionseventh_Object = MibScalar
upsIdentAgentSoftwareVersionseventh = _UpsIdentAgentSoftwareVersionseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 4),
    _UpsIdentAgentSoftwareVersionseventh_Type()
)
upsIdentAgentSoftwareVersionseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersionseventh.setStatus("current")
_UpsIdentNameseventh_Type = DisplayString
_UpsIdentNameseventh_Object = MibScalar
upsIdentNameseventh = _UpsIdentNameseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 5),
    _UpsIdentNameseventh_Type()
)
upsIdentNameseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNameseventh.setStatus("current")
_UpsIdentAttachedDevicesseventh_Type = DisplayString
_UpsIdentAttachedDevicesseventh_Object = MibScalar
upsIdentAttachedDevicesseventh = _UpsIdentAttachedDevicesseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 6),
    _UpsIdentAttachedDevicesseventh_Type()
)
upsIdentAttachedDevicesseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicesseventh.setStatus("current")
_UpsIdentUPSSerialNumberseventh_Type = DisplayString
_UpsIdentUPSSerialNumberseventh_Object = MibScalar
upsIdentUPSSerialNumberseventh = _UpsIdentUPSSerialNumberseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 7),
    _UpsIdentUPSSerialNumberseventh_Type()
)
upsIdentUPSSerialNumberseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumberseventh.setStatus("current")
_UpsIdentComProtVersionseventh_Type = DisplayString
_UpsIdentComProtVersionseventh_Object = MibScalar
upsIdentComProtVersionseventh = _UpsIdentComProtVersionseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 8),
    _UpsIdentComProtVersionseventh_Type()
)
upsIdentComProtVersionseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersionseventh.setStatus("current")
_UpsIdentOperatingTimeseventh_Type = NonNegativeInteger32
_UpsIdentOperatingTimeseventh_Object = MibScalar
upsIdentOperatingTimeseventh = _UpsIdentOperatingTimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 1, 9),
    _UpsIdentOperatingTimeseventh_Type()
)
upsIdentOperatingTimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimeseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimeseventh.setUnits("sevenths")
_UpsBatteryseventh_ObjectIdentity = ObjectIdentity
upsBatteryseventh = _UpsBatteryseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2)
)


class _UpsBatteryStatusseventh_Type(Integer32):
    """Custom type upsBatteryStatusseventh based on Integer32"""
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


_UpsBatteryStatusseventh_Type.__name__ = "Integer32"
_UpsBatteryStatusseventh_Object = MibScalar
upsBatteryStatusseventh = _UpsBatteryStatusseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 1),
    _UpsBatteryStatusseventh_Type()
)
upsBatteryStatusseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatusseventh.setStatus("current")
_UpsSecondsOnBatteryseventh_Type = NonNegativeInteger32
_UpsSecondsOnBatteryseventh_Object = MibScalar
upsSecondsOnBatteryseventh = _UpsSecondsOnBatteryseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 2),
    _UpsSecondsOnBatteryseventh_Type()
)
upsSecondsOnBatteryseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryseventh.setUnits("sevenths")
_UpsEstimatedMinutesRemainingseventh_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingseventh_Object = MibScalar
upsEstimatedMinutesRemainingseventh = _UpsEstimatedMinutesRemainingseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 3),
    _UpsEstimatedMinutesRemainingseventh_Type()
)
upsEstimatedMinutesRemainingseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingseventh.setUnits("minutes")


class _UpsEstimatedChargeRemainingseventh_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingseventh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingseventh_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingseventh_Object = MibScalar
upsEstimatedChargeRemainingseventh = _UpsEstimatedChargeRemainingseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 4),
    _UpsEstimatedChargeRemainingseventh_Type()
)
upsEstimatedChargeRemainingseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingseventh.setUnits("percent")
_UpsBatteryVoltageseventh_Type = NonNegativeInteger32
_UpsBatteryVoltageseventh_Object = MibScalar
upsBatteryVoltageseventh = _UpsBatteryVoltageseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 5),
    _UpsBatteryVoltageseventh_Type()
)
upsBatteryVoltageseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltageseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltageseventh.setUnits("0.1 Volt DC")
_UpsBatteryCurrentseventh_Type = Integer32
_UpsBatteryCurrentseventh_Object = MibScalar
upsBatteryCurrentseventh = _UpsBatteryCurrentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 6),
    _UpsBatteryCurrentseventh_Type()
)
upsBatteryCurrentseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentseventh.setUnits("0.1 Amp DC")
_UpsBatteryTemperatureseventh_Type = Integer32
_UpsBatteryTemperatureseventh_Object = MibScalar
upsBatteryTemperatureseventh = _UpsBatteryTemperatureseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 7),
    _UpsBatteryTemperatureseventh_Type()
)
upsBatteryTemperatureseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperatureseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperatureseventh.setUnits("degrees Centigrade")
_UpsBatteryRippleseventh_Type = Integer32
_UpsBatteryRippleseventh_Object = MibScalar
upsBatteryRippleseventh = _UpsBatteryRippleseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 2, 8),
    _UpsBatteryRippleseventh_Type()
)
upsBatteryRippleseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRippleseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRippleseventh.setUnits("0.1 Volt RMS")
_UpsInputseventh_ObjectIdentity = ObjectIdentity
upsInputseventh = _UpsInputseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3)
)
_UpsInputLineBadsseventh_Type = Counter32
_UpsInputLineBadsseventh_Object = MibScalar
upsInputLineBadsseventh = _UpsInputLineBadsseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 1),
    _UpsInputLineBadsseventh_Type()
)
upsInputLineBadsseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadsseventh.setStatus("current")
_UpsInputNumLinesseventh_Type = NonNegativeInteger32
_UpsInputNumLinesseventh_Object = MibScalar
upsInputNumLinesseventh = _UpsInputNumLinesseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 2),
    _UpsInputNumLinesseventh_Type()
)
upsInputNumLinesseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinesseventh.setStatus("current")
_UpsInputSeventhTable_Object = MibTable
upsInputSeventhTable = _UpsInputSeventhTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputSeventhTable.setStatus("current")
_UpsInputSeventhEntry_Object = MibTableRow
upsInputSeventhEntry = _UpsInputSeventhEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1)
)
upsInputSeventhEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexseventh"),
)
if mibBuilder.loadTexts:
    upsInputSeventhEntry.setStatus("current")
_UpsInputLineIndexseventh_Type = PositiveInteger32
_UpsInputLineIndexseventh_Object = MibTableColumn
upsInputLineIndexseventh = _UpsInputLineIndexseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1, 1),
    _UpsInputLineIndexseventh_Type()
)
upsInputLineIndexseventh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexseventh.setStatus("current")
_UpsInputFrequencyseventh_Type = NonNegativeInteger32
_UpsInputFrequencyseventh_Object = MibTableColumn
upsInputFrequencyseventh = _UpsInputFrequencyseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1, 2),
    _UpsInputFrequencyseventh_Type()
)
upsInputFrequencyseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyseventh.setUnits("0.1 Hertz")
_UpsInputVoltageseventh_Type = NonNegativeInteger32
_UpsInputVoltageseventh_Object = MibTableColumn
upsInputVoltageseventh = _UpsInputVoltageseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1, 3),
    _UpsInputVoltageseventh_Type()
)
upsInputVoltageseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageseventh.setUnits("RMS Volts")
_UpsInputCurrentseventh_Type = NonNegativeInteger32
_UpsInputCurrentseventh_Object = MibTableColumn
upsInputCurrentseventh = _UpsInputCurrentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1, 4),
    _UpsInputCurrentseventh_Type()
)
upsInputCurrentseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentseventh.setUnits("0.1 RMS Amp")
_UpsInputTruePowerseventh_Type = NonNegativeInteger32
_UpsInputTruePowerseventh_Object = MibTableColumn
upsInputTruePowerseventh = _UpsInputTruePowerseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1, 5),
    _UpsInputTruePowerseventh_Type()
)
upsInputTruePowerseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowerseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowerseventh.setUnits("Watts")
_UpsInputVoltageMinseventh_Type = NonNegativeInteger32
_UpsInputVoltageMinseventh_Object = MibTableColumn
upsInputVoltageMinseventh = _UpsInputVoltageMinseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1, 6),
    _UpsInputVoltageMinseventh_Type()
)
upsInputVoltageMinseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMinseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMinseventh.setUnits("RMS Volts")
_UpsInputVoltageMaxseventh_Type = NonNegativeInteger32
_UpsInputVoltageMaxseventh_Object = MibTableColumn
upsInputVoltageMaxseventh = _UpsInputVoltageMaxseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 3, 3, 1, 7),
    _UpsInputVoltageMaxseventh_Type()
)
upsInputVoltageMaxseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxseventh.setUnits("RMS Volts")
_UpsOutputseventh_ObjectIdentity = ObjectIdentity
upsOutputseventh = _UpsOutputseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4)
)


class _UpsOutputSourceseventh_Type(Integer32):
    """Custom type upsOutputSourceseventh based on Integer32"""
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


_UpsOutputSourceseventh_Type.__name__ = "Integer32"
_UpsOutputSourceseventh_Object = MibScalar
upsOutputSourceseventh = _UpsOutputSourceseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 1),
    _UpsOutputSourceseventh_Type()
)
upsOutputSourceseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourceseventh.setStatus("current")
_UpsOutputFrequencyseventh_Type = NonNegativeInteger32
_UpsOutputFrequencyseventh_Object = MibScalar
upsOutputFrequencyseventh = _UpsOutputFrequencyseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 2),
    _UpsOutputFrequencyseventh_Type()
)
upsOutputFrequencyseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencyseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencyseventh.setUnits("0.1 Hertz")
_UpsOutputNumLinesseventh_Type = NonNegativeInteger32
_UpsOutputNumLinesseventh_Object = MibScalar
upsOutputNumLinesseventh = _UpsOutputNumLinesseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 3),
    _UpsOutputNumLinesseventh_Type()
)
upsOutputNumLinesseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinesseventh.setStatus("current")
_UpsOutputSeventhTable_Object = MibTable
upsOutputSeventhTable = _UpsOutputSeventhTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputSeventhTable.setStatus("current")
_UpsOutputSeventhEntry_Object = MibTableRow
upsOutputSeventhEntry = _UpsOutputSeventhEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1)
)
upsOutputSeventhEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexseventh"),
)
if mibBuilder.loadTexts:
    upsOutputSeventhEntry.setStatus("current")
_UpsOutputLineIndexseventh_Type = PositiveInteger32
_UpsOutputLineIndexseventh_Object = MibTableColumn
upsOutputLineIndexseventh = _UpsOutputLineIndexseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 1),
    _UpsOutputLineIndexseventh_Type()
)
upsOutputLineIndexseventh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexseventh.setStatus("current")
_UpsOutputVoltageseventh_Type = NonNegativeInteger32
_UpsOutputVoltageseventh_Object = MibTableColumn
upsOutputVoltageseventh = _UpsOutputVoltageseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 2),
    _UpsOutputVoltageseventh_Type()
)
upsOutputVoltageseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltageseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltageseventh.setUnits("RMS Volts")
_UpsOutputCurrentseventh_Type = NonNegativeInteger32
_UpsOutputCurrentseventh_Object = MibTableColumn
upsOutputCurrentseventh = _UpsOutputCurrentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 3),
    _UpsOutputCurrentseventh_Type()
)
upsOutputCurrentseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentseventh.setUnits("0.1 RMS Amp")
_UpsOutputPowerseventh_Type = NonNegativeInteger32
_UpsOutputPowerseventh_Object = MibTableColumn
upsOutputPowerseventh = _UpsOutputPowerseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 4),
    _UpsOutputPowerseventh_Type()
)
upsOutputPowerseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerseventh.setUnits("Watts")


class _UpsOutputPercentLoadseventh_Type(Integer32):
    """Custom type upsOutputPercentLoadseventh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadseventh_Type.__name__ = "Integer32"
_UpsOutputPercentLoadseventh_Object = MibTableColumn
upsOutputPercentLoadseventh = _UpsOutputPercentLoadseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 5),
    _UpsOutputPercentLoadseventh_Type()
)
upsOutputPercentLoadseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadseventh.setUnits("percent")


class _UpsOutputPowerFactorseventh_Type(Integer32):
    """Custom type upsOutputPowerFactorseventh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorseventh_Type.__name__ = "Integer32"
_UpsOutputPowerFactorseventh_Object = MibTableColumn
upsOutputPowerFactorseventh = _UpsOutputPowerFactorseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 6),
    _UpsOutputPowerFactorseventh_Type()
)
upsOutputPowerFactorseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorseventh.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentseventh_Type = Integer32
_UpsOutputPeakCurrentseventh_Object = MibTableColumn
upsOutputPeakCurrentseventh = _UpsOutputPeakCurrentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 7),
    _UpsOutputPeakCurrentseventh_Type()
)
upsOutputPeakCurrentseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentseventh.setUnits("Amps")
_UpsOutputShareCurrentseventh_Type = Integer32
_UpsOutputShareCurrentseventh_Object = MibTableColumn
upsOutputShareCurrentseventh = _UpsOutputShareCurrentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 4, 4, 1, 8),
    _UpsOutputShareCurrentseventh_Type()
)
upsOutputShareCurrentseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentseventh.setUnits("Amps")
_UpsBypassseventh_ObjectIdentity = ObjectIdentity
upsBypassseventh = _UpsBypassseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5)
)
_UpsBypassFrequencyseventh_Type = NonNegativeInteger32
_UpsBypassFrequencyseventh_Object = MibScalar
upsBypassFrequencyseventh = _UpsBypassFrequencyseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 1),
    _UpsBypassFrequencyseventh_Type()
)
upsBypassFrequencyseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencyseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencyseventh.setUnits("0.1 Hertz")
_UpsBypassNumLinesseventh_Type = NonNegativeInteger32
_UpsBypassNumLinesseventh_Object = MibScalar
upsBypassNumLinesseventh = _UpsBypassNumLinesseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 2),
    _UpsBypassNumLinesseventh_Type()
)
upsBypassNumLinesseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinesseventh.setStatus("current")
_UpsBypassSeventhTable_Object = MibTable
upsBypassSeventhTable = _UpsBypassSeventhTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassSeventhTable.setStatus("current")
_UpsBypassSeventhEntry_Object = MibTableRow
upsBypassSeventhEntry = _UpsBypassSeventhEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 3, 1)
)
upsBypassSeventhEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexseventh"),
)
if mibBuilder.loadTexts:
    upsBypassSeventhEntry.setStatus("current")
_UpsBypassLineIndexseventh_Type = PositiveInteger32
_UpsBypassLineIndexseventh_Object = MibTableColumn
upsBypassLineIndexseventh = _UpsBypassLineIndexseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 3, 1, 1),
    _UpsBypassLineIndexseventh_Type()
)
upsBypassLineIndexseventh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexseventh.setStatus("current")
_UpsBypassVoltageseventh_Type = NonNegativeInteger32
_UpsBypassVoltageseventh_Object = MibTableColumn
upsBypassVoltageseventh = _UpsBypassVoltageseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 3, 1, 2),
    _UpsBypassVoltageseventh_Type()
)
upsBypassVoltageseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltageseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltageseventh.setUnits("RMS Volts")
_UpsBypassCurrentseventh_Type = NonNegativeInteger32
_UpsBypassCurrentseventh_Object = MibTableColumn
upsBypassCurrentseventh = _UpsBypassCurrentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 3, 1, 3),
    _UpsBypassCurrentseventh_Type()
)
upsBypassCurrentseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentseventh.setUnits("0.1 RMS Amp")
_UpsBypassPowerseventh_Type = NonNegativeInteger32
_UpsBypassPowerseventh_Object = MibTableColumn
upsBypassPowerseventh = _UpsBypassPowerseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 5, 3, 1, 4),
    _UpsBypassPowerseventh_Type()
)
upsBypassPowerseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowerseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowerseventh.setUnits("Watts")
_UpsAlarmseventh_ObjectIdentity = ObjectIdentity
upsAlarmseventh = _UpsAlarmseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6)
)
_UpsAlarmsPresentseventh_Type = Gauge32
_UpsAlarmsPresentseventh_Object = MibScalar
upsAlarmsPresentseventh = _UpsAlarmsPresentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 1),
    _UpsAlarmsPresentseventh_Type()
)
upsAlarmsPresentseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentseventh.setStatus("current")
_UpsAlarmSeventhTable_Object = MibTable
upsAlarmSeventhTable = _UpsAlarmSeventhTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmSeventhTable.setStatus("current")
_UpsAlarmSeventhEntry_Object = MibTableRow
upsAlarmSeventhEntry = _UpsAlarmSeventhEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 2, 1)
)
upsAlarmSeventhEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdseventh"),
)
if mibBuilder.loadTexts:
    upsAlarmSeventhEntry.setStatus("current")
_UpsAlarmIdseventh_Type = PositiveInteger32
_UpsAlarmIdseventh_Object = MibTableColumn
upsAlarmIdseventh = _UpsAlarmIdseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 2, 1, 1),
    _UpsAlarmIdseventh_Type()
)
upsAlarmIdseventh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdseventh.setStatus("current")
_UpsAlarmDescrseventh_Type = AutonomousType
_UpsAlarmDescrseventh_Object = MibTableColumn
upsAlarmDescrseventh = _UpsAlarmDescrseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 2, 1, 2),
    _UpsAlarmDescrseventh_Type()
)
upsAlarmDescrseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrseventh.setStatus("current")
_UpsAlarmTimeseventh_Type = TimeStamp
_UpsAlarmTimeseventh_Object = MibTableColumn
upsAlarmTimeseventh = _UpsAlarmTimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 2, 1, 3),
    _UpsAlarmTimeseventh_Type()
)
upsAlarmTimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimeseventh.setStatus("current")
_UpsWellKnownAlarmsseventh_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmsseventh = _UpsWellKnownAlarmsseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3)
)
_UpsAlarmBatteryBadseventh_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadseventh = _UpsAlarmBatteryBadseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadseventh.setStatus("current")
_UpsAlarmOnBatteryseventh_ObjectIdentity = ObjectIdentity
upsAlarmOnBatteryseventh = _UpsAlarmOnBatteryseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatteryseventh.setStatus("current")
_UpsAlarmLowBatteryseventh_ObjectIdentity = ObjectIdentity
upsAlarmLowBatteryseventh = _UpsAlarmLowBatteryseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatteryseventh.setStatus("current")
_UpsAlarmDepletedBatteryseventh_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatteryseventh = _UpsAlarmDepletedBatteryseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatteryseventh.setStatus("current")
_UpsAlarmTempBadseventh_ObjectIdentity = ObjectIdentity
upsAlarmTempBadseventh = _UpsAlarmTempBadseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadseventh.setStatus("current")
_UpsAlarmInputBadseventh_ObjectIdentity = ObjectIdentity
upsAlarmInputBadseventh = _UpsAlarmInputBadseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadseventh.setStatus("current")
_UpsAlarmOutputBadseventh_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadseventh = _UpsAlarmOutputBadseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadseventh.setStatus("current")
_UpsAlarmOutputOverloadseventh_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadseventh = _UpsAlarmOutputOverloadseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadseventh.setStatus("current")
_UpsAlarmOnBypassseventh_ObjectIdentity = ObjectIdentity
upsAlarmOnBypassseventh = _UpsAlarmOnBypassseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypassseventh.setStatus("current")
_UpsAlarmBypassBadseventh_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadseventh = _UpsAlarmBypassBadseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadseventh.setStatus("current")
_UpsAlarmOutputOffAsRequestedseventh_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedseventh = _UpsAlarmOutputOffAsRequestedseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedseventh.setStatus("current")
_UpsAlarmUpsOffAsRequestedseventh_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedseventh = _UpsAlarmUpsOffAsRequestedseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedseventh.setStatus("current")
_UpsAlarmChargerFailedseventh_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedseventh = _UpsAlarmChargerFailedseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedseventh.setStatus("current")
_UpsAlarmUpsOutputOffseventh_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOffseventh = _UpsAlarmUpsOutputOffseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOffseventh.setStatus("current")
_UpsAlarmUpsSystemOffseventh_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOffseventh = _UpsAlarmUpsSystemOffseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOffseventh.setStatus("current")
_UpsAlarmFanFailureseventh_ObjectIdentity = ObjectIdentity
upsAlarmFanFailureseventh = _UpsAlarmFanFailureseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailureseventh.setStatus("current")
_UpsAlarmFuseFailureseventh_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailureseventh = _UpsAlarmFuseFailureseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailureseventh.setStatus("current")
_UpsAlarmGeneralFaultseventh_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultseventh = _UpsAlarmGeneralFaultseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultseventh.setStatus("current")
_UpsAlarmDiagnosticTestFailedseventh_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedseventh = _UpsAlarmDiagnosticTestFailedseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedseventh.setStatus("current")
_UpsAlarmCommunicationsLostseventh_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostseventh = _UpsAlarmCommunicationsLostseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostseventh.setStatus("current")
_UpsAlarmAwaitingPowerseventh_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowerseventh = _UpsAlarmAwaitingPowerseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowerseventh.setStatus("current")
_UpsAlarmShutdownPendingseventh_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingseventh = _UpsAlarmShutdownPendingseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingseventh.setStatus("current")
_UpsAlarmShutdownImminentseventh_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentseventh = _UpsAlarmShutdownImminentseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentseventh.setStatus("current")
_UpsAlarmTestInProgressseventh_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgressseventh = _UpsAlarmTestInProgressseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgressseventh.setStatus("current")
_UpsAlarmReceptacleOffseventh_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOffseventh = _UpsAlarmReceptacleOffseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOffseventh.setStatus("current")
_UpsAlarmHighSpeedBusFailureseventh_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailureseventh = _UpsAlarmHighSpeedBusFailureseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailureseventh.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailureseventh_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailureseventh = _UpsAlarmHighSpeedBusJACRCFailureseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailureseventh.setStatus("current")
_UpsAlarmConnectivityBusFailureseventh_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailureseventh = _UpsAlarmConnectivityBusFailureseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailureseventh.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailureseventh_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailureseventh = _UpsAlarmHighSpeedBusJBCRCFailureseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailureseventh.setStatus("current")
_UpsAlarmCurrentSharingseventh_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingseventh = _UpsAlarmCurrentSharingseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingseventh.setStatus("current")
_UpsAlarmDCRippleseventh_ObjectIdentity = ObjectIdentity
upsAlarmDCRippleseventh = _UpsAlarmDCRippleseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRippleseventh.setStatus("current")
_UpsAlarmMaskAseventh_Type = Unsigned32
_UpsAlarmMaskAseventh_Object = MibScalar
upsAlarmMaskAseventh = _UpsAlarmMaskAseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 6, 4),
    _UpsAlarmMaskAseventh_Type()
)
upsAlarmMaskAseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAseventh.setStatus("current")
_UpsTestseventh_ObjectIdentity = ObjectIdentity
upsTestseventh = _UpsTestseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7)
)
_UpsTestIdseventh_Type = ObjectIdentifier
_UpsTestIdseventh_Object = MibScalar
upsTestIdseventh = _UpsTestIdseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 1),
    _UpsTestIdseventh_Type()
)
upsTestIdseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdseventh.setStatus("current")
_UpsTestSpinLockseventh_Type = TestAndIncr
_UpsTestSpinLockseventh_Object = MibScalar
upsTestSpinLockseventh = _UpsTestSpinLockseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 2),
    _UpsTestSpinLockseventh_Type()
)
upsTestSpinLockseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLockseventh.setStatus("current")


class _UpsTestResultsSummaryseventh_Type(Integer32):
    """Custom type upsTestResultsSummaryseventh based on Integer32"""
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


_UpsTestResultsSummaryseventh_Type.__name__ = "Integer32"
_UpsTestResultsSummaryseventh_Object = MibScalar
upsTestResultsSummaryseventh = _UpsTestResultsSummaryseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 3),
    _UpsTestResultsSummaryseventh_Type()
)
upsTestResultsSummaryseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummaryseventh.setStatus("current")
_UpsTestResultsDetailseventh_Type = DisplayString
_UpsTestResultsDetailseventh_Object = MibScalar
upsTestResultsDetailseventh = _UpsTestResultsDetailseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 4),
    _UpsTestResultsDetailseventh_Type()
)
upsTestResultsDetailseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailseventh.setStatus("current")
_UpsTestStartTimeseventh_Type = TimeStamp
_UpsTestStartTimeseventh_Object = MibScalar
upsTestStartTimeseventh = _UpsTestStartTimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 5),
    _UpsTestStartTimeseventh_Type()
)
upsTestStartTimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimeseventh.setStatus("current")
_UpsTestElapsedTimeseventh_Type = TimeInterval
_UpsTestElapsedTimeseventh_Object = MibScalar
upsTestElapsedTimeseventh = _UpsTestElapsedTimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 6),
    _UpsTestElapsedTimeseventh_Type()
)
upsTestElapsedTimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimeseventh.setStatus("current")
_UpsWellKnownTestsseventh_ObjectIdentity = ObjectIdentity
upsWellKnownTestsseventh = _UpsWellKnownTestsseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 7)
)
_UpsTestNoTestsInitiatedseventh_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedseventh = _UpsTestNoTestsInitiatedseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedseventh.setStatus("current")
_UpsTestAbortTestInProgressseventh_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgressseventh = _UpsTestAbortTestInProgressseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgressseventh.setStatus("current")
_UpsTestGeneralSystemsTestseventh_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestseventh = _UpsTestGeneralSystemsTestseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestseventh.setStatus("current")
_UpsTestQuickBatteryTestseventh_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestseventh = _UpsTestQuickBatteryTestseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestseventh.setStatus("current")
_UpsTestDeepBatteryCalibrationseventh_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationseventh = _UpsTestDeepBatteryCalibrationseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationseventh.setStatus("current")
_UpsControlseventh_ObjectIdentity = ObjectIdentity
upsControlseventh = _UpsControlseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8)
)


class _UpsShutdownTypeseventh_Type(Integer32):
    """Custom type upsShutdownTypeseventh based on Integer32"""
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


_UpsShutdownTypeseventh_Type.__name__ = "Integer32"
_UpsShutdownTypeseventh_Object = MibScalar
upsShutdownTypeseventh = _UpsShutdownTypeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 1),
    _UpsShutdownTypeseventh_Type()
)
upsShutdownTypeseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypeseventh.setStatus("current")


class _UpsShutdownAfterDelayseventh_Type(Integer32):
    """Custom type upsShutdownAfterDelayseventh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelayseventh_Type.__name__ = "Integer32"
_UpsShutdownAfterDelayseventh_Object = MibScalar
upsShutdownAfterDelayseventh = _UpsShutdownAfterDelayseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 2),
    _UpsShutdownAfterDelayseventh_Type()
)
upsShutdownAfterDelayseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayseventh.setUnits("sevenths")


class _UpsStartupAfterDelayseventh_Type(Integer32):
    """Custom type upsStartupAfterDelayseventh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelayseventh_Type.__name__ = "Integer32"
_UpsStartupAfterDelayseventh_Object = MibScalar
upsStartupAfterDelayseventh = _UpsStartupAfterDelayseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 3),
    _UpsStartupAfterDelayseventh_Type()
)
upsStartupAfterDelayseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelayseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelayseventh.setUnits("sevenths")


class _UpsRebootWithDurationseventh_Type(Integer32):
    """Custom type upsRebootWithDurationseventh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationseventh_Type.__name__ = "Integer32"
_UpsRebootWithDurationseventh_Object = MibScalar
upsRebootWithDurationseventh = _UpsRebootWithDurationseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 4),
    _UpsRebootWithDurationseventh_Type()
)
upsRebootWithDurationseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationseventh.setUnits("sevenths")


class _UpsAutoRestartseventh_Type(Integer32):
    """Custom type upsAutoRestartseventh based on Integer32"""
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


_UpsAutoRestartseventh_Type.__name__ = "Integer32"
_UpsAutoRestartseventh_Object = MibScalar
upsAutoRestartseventh = _UpsAutoRestartseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 5),
    _UpsAutoRestartseventh_Type()
)
upsAutoRestartseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartseventh.setStatus("current")
_UpsReceptaclesNumseventh_Type = NonNegativeInteger32
_UpsReceptaclesNumseventh_Object = MibScalar
upsReceptaclesNumseventh = _UpsReceptaclesNumseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 6),
    _UpsReceptaclesNumseventh_Type()
)
upsReceptaclesNumseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumseventh.setStatus("current")
_UpsReceptacleSeventhTable_Object = MibTable
upsReceptacleSeventhTable = _UpsReceptacleSeventhTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleSeventhTable.setStatus("current")
_UpsReceptacleSeventhEntry_Object = MibTableRow
upsReceptacleSeventhEntry = _UpsReceptacleSeventhEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 7, 1)
)
upsReceptacleSeventhEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexseventh"),
)
if mibBuilder.loadTexts:
    upsReceptacleSeventhEntry.setStatus("current")
_UpsReceptacleLineIndexseventh_Type = PositiveInteger32
_UpsReceptacleLineIndexseventh_Object = MibTableColumn
upsReceptacleLineIndexseventh = _UpsReceptacleLineIndexseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 7, 1, 1),
    _UpsReceptacleLineIndexseventh_Type()
)
upsReceptacleLineIndexseventh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexseventh.setStatus("current")


class _UpsReceptacleOnOffseventh_Type(Integer32):
    """Custom type upsReceptacleOnOffseventh based on Integer32"""
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


_UpsReceptacleOnOffseventh_Type.__name__ = "Integer32"
_UpsReceptacleOnOffseventh_Object = MibTableColumn
upsReceptacleOnOffseventh = _UpsReceptacleOnOffseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 7, 1, 2),
    _UpsReceptacleOnOffseventh_Type()
)
upsReceptacleOnOffseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOffseventh.setStatus("current")


class _UpsUPSModeseventh_Type(Integer32):
    """Custom type upsUPSModeseventh based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModeseventh_Type.__name__ = "Integer32"
_UpsUPSModeseventh_Object = MibScalar
upsUPSModeseventh = _UpsUPSModeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 8),
    _UpsUPSModeseventh_Type()
)
upsUPSModeseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModeseventh.setStatus("current")


class _UpsRectifierOnOffseventh_Type(Integer32):
    """Custom type upsRectifierOnOffseventh based on Integer32"""
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


_UpsRectifierOnOffseventh_Type.__name__ = "Integer32"
_UpsRectifierOnOffseventh_Object = MibScalar
upsRectifierOnOffseventh = _UpsRectifierOnOffseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 9),
    _UpsRectifierOnOffseventh_Type()
)
upsRectifierOnOffseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOffseventh.setStatus("current")


class _UpsBatteryChargeMethodseventh_Type(Integer32):
    """Custom type upsBatteryChargeMethodseventh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodseventh_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodseventh_Object = MibScalar
upsBatteryChargeMethodseventh = _UpsBatteryChargeMethodseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 10),
    _UpsBatteryChargeMethodseventh_Type()
)
upsBatteryChargeMethodseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodseventh.setStatus("current")


class _UpsInverterOnOffseventh_Type(Integer32):
    """Custom type upsInverterOnOffseventh based on Integer32"""
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


_UpsInverterOnOffseventh_Type.__name__ = "Integer32"
_UpsInverterOnOffseventh_Object = MibScalar
upsInverterOnOffseventh = _UpsInverterOnOffseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 11),
    _UpsInverterOnOffseventh_Type()
)
upsInverterOnOffseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOffseventh.setStatus("current")


class _UpsBypassOnOffseventh_Type(Integer32):
    """Custom type upsBypassOnOffseventh based on Integer32"""
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


_UpsBypassOnOffseventh_Type.__name__ = "Integer32"
_UpsBypassOnOffseventh_Object = MibScalar
upsBypassOnOffseventh = _UpsBypassOnOffseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 12),
    _UpsBypassOnOffseventh_Type()
)
upsBypassOnOffseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOffseventh.setStatus("current")


class _UpsLoadSourceseventh_Type(Integer32):
    """Custom type upsLoadSourceseventh based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourceseventh_Type.__name__ = "Integer32"
_UpsLoadSourceseventh_Object = MibScalar
upsLoadSourceseventh = _UpsLoadSourceseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 8, 13),
    _UpsLoadSourceseventh_Type()
)
upsLoadSourceseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourceseventh.setStatus("current")
_UpsConfigseventh_ObjectIdentity = ObjectIdentity
upsConfigseventh = _UpsConfigseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9)
)
_UpsConfigInputVoltageseventh_Type = NonNegativeInteger32
_UpsConfigInputVoltageseventh_Object = MibScalar
upsConfigInputVoltageseventh = _UpsConfigInputVoltageseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 1),
    _UpsConfigInputVoltageseventh_Type()
)
upsConfigInputVoltageseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltageseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltageseventh.setUnits("RMS Volts")
_UpsConfigInputFreqseventh_Type = NonNegativeInteger32
_UpsConfigInputFreqseventh_Object = MibScalar
upsConfigInputFreqseventh = _UpsConfigInputFreqseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 2),
    _UpsConfigInputFreqseventh_Type()
)
upsConfigInputFreqseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqseventh.setUnits("0.1 Hertz")
_UpsConfigOutputVoltageseventh_Type = NonNegativeInteger32
_UpsConfigOutputVoltageseventh_Object = MibScalar
upsConfigOutputVoltageseventh = _UpsConfigOutputVoltageseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 3),
    _UpsConfigOutputVoltageseventh_Type()
)
upsConfigOutputVoltageseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltageseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltageseventh.setUnits("RMS Volts")
_UpsConfigOutputFreqseventh_Type = NonNegativeInteger32
_UpsConfigOutputFreqseventh_Object = MibScalar
upsConfigOutputFreqseventh = _UpsConfigOutputFreqseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 4),
    _UpsConfigOutputFreqseventh_Type()
)
upsConfigOutputFreqseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqseventh.setUnits("0.1 Hertz")
_UpsConfigOutputVAseventh_Type = NonNegativeInteger32
_UpsConfigOutputVAseventh_Object = MibScalar
upsConfigOutputVAseventh = _UpsConfigOutputVAseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 5),
    _UpsConfigOutputVAseventh_Type()
)
upsConfigOutputVAseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAseventh.setUnits("Volt-Amps")
_UpsConfigOutputPowerseventh_Type = NonNegativeInteger32
_UpsConfigOutputPowerseventh_Object = MibScalar
upsConfigOutputPowerseventh = _UpsConfigOutputPowerseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 6),
    _UpsConfigOutputPowerseventh_Type()
)
upsConfigOutputPowerseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowerseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowerseventh.setUnits("Watts")
_UpsConfigLowBattTimeseventh_Type = NonNegativeInteger32
_UpsConfigLowBattTimeseventh_Object = MibScalar
upsConfigLowBattTimeseventh = _UpsConfigLowBattTimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 7),
    _UpsConfigLowBattTimeseventh_Type()
)
upsConfigLowBattTimeseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimeseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimeseventh.setUnits("minutes")


class _UpsConfigAudibleStatusseventh_Type(Integer32):
    """Custom type upsConfigAudibleStatusseventh based on Integer32"""
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


_UpsConfigAudibleStatusseventh_Type.__name__ = "Integer32"
_UpsConfigAudibleStatusseventh_Object = MibScalar
upsConfigAudibleStatusseventh = _UpsConfigAudibleStatusseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 8),
    _UpsConfigAudibleStatusseventh_Type()
)
upsConfigAudibleStatusseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatusseventh.setStatus("current")
_UpsConfigLowVoltageTransferPointseventh_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointseventh_Object = MibScalar
upsConfigLowVoltageTransferPointseventh = _UpsConfigLowVoltageTransferPointseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 9),
    _UpsConfigLowVoltageTransferPointseventh_Type()
)
upsConfigLowVoltageTransferPointseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointseventh.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointseventh_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointseventh_Object = MibScalar
upsConfigHighVoltageTransferPointseventh = _UpsConfigHighVoltageTransferPointseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 10),
    _UpsConfigHighVoltageTransferPointseventh_Type()
)
upsConfigHighVoltageTransferPointseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointseventh.setUnits("RMS Volts")
_UpsConfigBatteryCapacityseventh_Type = NonNegativeInteger32
_UpsConfigBatteryCapacityseventh_Object = MibScalar
upsConfigBatteryCapacityseventh = _UpsConfigBatteryCapacityseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 11),
    _UpsConfigBatteryCapacityseventh_Type()
)
upsConfigBatteryCapacityseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityseventh.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentseventh_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentseventh_Object = MibScalar
upsConfigBatteryChargeCurrentseventh = _UpsConfigBatteryChargeCurrentseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 12),
    _UpsConfigBatteryChargeCurrentseventh_Type()
)
upsConfigBatteryChargeCurrentseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentseventh.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdownseventh_Type(Integer32):
    """Custom type upsConfigNoLoadShutdownseventh based on Integer32"""
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


_UpsConfigNoLoadShutdownseventh_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdownseventh_Object = MibScalar
upsConfigNoLoadShutdownseventh = _UpsConfigNoLoadShutdownseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 13),
    _UpsConfigNoLoadShutdownseventh_Type()
)
upsConfigNoLoadShutdownseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdownseventh.setStatus("current")
_UpsConfigStartDelayseventh_Type = PositiveInteger32
_UpsConfigStartDelayseventh_Object = MibScalar
upsConfigStartDelayseventh = _UpsConfigStartDelayseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 9, 14),
    _UpsConfigStartDelayseventh_Type()
)
upsConfigStartDelayseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelayseventh.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelayseventh.setUnits("minutes")
_UpsGetSetseventh_ObjectIdentity = ObjectIdentity
upsGetSetseventh = _UpsGetSetseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10)
)
_UpsEventGetNextseventh_Type = PositiveInteger32
_UpsEventGetNextseventh_Object = MibScalar
upsEventGetNextseventh = _UpsEventGetNextseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 1),
    _UpsEventGetNextseventh_Type()
)
upsEventGetNextseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextseventh.setStatus("current")
_UpsEventGetPreviousseventh_Type = PositiveInteger32
_UpsEventGetPreviousseventh_Object = MibScalar
upsEventGetPreviousseventh = _UpsEventGetPreviousseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 2),
    _UpsEventGetPreviousseventh_Type()
)
upsEventGetPreviousseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPreviousseventh.setStatus("current")
_UpsEventSetStartingTimeStampseventh_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampseventh_Object = MibScalar
upsEventSetStartingTimeStampseventh = _UpsEventSetStartingTimeStampseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 3),
    _UpsEventSetStartingTimeStampseventh_Type()
)
upsEventSetStartingTimeStampseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampseventh.setStatus("current")
_UpsEventRetreiveCurrentTimeStampseventh_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampseventh_Object = MibScalar
upsEventRetreiveCurrentTimeStampseventh = _UpsEventRetreiveCurrentTimeStampseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 4),
    _UpsEventRetreiveCurrentTimeStampseventh_Type()
)
upsEventRetreiveCurrentTimeStampseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampseventh.setStatus("current")
_UpsEventTableSizeseventh_Type = NonNegativeInteger32
_UpsEventTableSizeseventh_Object = MibScalar
upsEventTableSizeseventh = _UpsEventTableSizeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 5),
    _UpsEventTableSizeseventh_Type()
)
upsEventTableSizeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizeseventh.setStatus("current")
_UpsEventSeventhTable_Object = MibTable
upsEventSeventhTable = _UpsEventSeventhTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventSeventhTable.setStatus("current")
_UpsEventSeventhEntry_Object = MibTableRow
upsEventSeventhEntry = _UpsEventSeventhEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 6, 1)
)
upsEventSeventhEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexseventh"),
)
if mibBuilder.loadTexts:
    upsEventSeventhEntry.setStatus("current")
_UpsEventLineIndexseventh_Type = PositiveInteger32
_UpsEventLineIndexseventh_Object = MibTableColumn
upsEventLineIndexseventh = _UpsEventLineIndexseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 6, 1, 1),
    _UpsEventLineIndexseventh_Type()
)
upsEventLineIndexseventh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexseventh.setStatus("current")
_UpsEventCodeseventh_Type = Integer32
_UpsEventCodeseventh_Object = MibTableColumn
upsEventCodeseventh = _UpsEventCodeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 6, 1, 2),
    _UpsEventCodeseventh_Type()
)
upsEventCodeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodeseventh.setStatus("current")
_UpsEventStatusseventh_Type = NonNegativeInteger32
_UpsEventStatusseventh_Object = MibTableColumn
upsEventStatusseventh = _UpsEventStatusseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 6, 1, 3),
    _UpsEventStatusseventh_Type()
)
upsEventStatusseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatusseventh.setStatus("current")
_UpsEventTimeseventh_Type = NonNegativeInteger32
_UpsEventTimeseventh_Object = MibTableColumn
upsEventTimeseventh = _UpsEventTimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 6, 1, 4),
    _UpsEventTimeseventh_Type()
)
upsEventTimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimeseventh.setStatus("current")
_UpsParametersReadseventh_Type = PositiveInteger32
_UpsParametersReadseventh_Object = MibScalar
upsParametersReadseventh = _UpsParametersReadseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 7),
    _UpsParametersReadseventh_Type()
)
upsParametersReadseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadseventh.setStatus("current")
_UpsParametersWriteseventh_Type = PositiveInteger32
_UpsParametersWriteseventh_Object = MibScalar
upsParametersWriteseventh = _UpsParametersWriteseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 8),
    _UpsParametersWriteseventh_Type()
)
upsParametersWriteseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWriteseventh.setStatus("current")
_UpsParametersStartAddressseventh_Type = NonNegativeInteger32
_UpsParametersStartAddressseventh_Object = MibScalar
upsParametersStartAddressseventh = _UpsParametersStartAddressseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 9),
    _UpsParametersStartAddressseventh_Type()
)
upsParametersStartAddressseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddressseventh.setStatus("current")
_UpsParameterTableSizeseventh_Type = NonNegativeInteger32
_UpsParameterTableSizeseventh_Object = MibScalar
upsParameterTableSizeseventh = _UpsParameterTableSizeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 10),
    _UpsParameterTableSizeseventh_Type()
)
upsParameterTableSizeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizeseventh.setStatus("current")
_UpsParameterSeventhTable_Object = MibTable
upsParameterSeventhTable = _UpsParameterSeventhTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterSeventhTable.setStatus("current")
_UpsParameterSeventhEntry_Object = MibTableRow
upsParameterSeventhEntry = _UpsParameterSeventhEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 11, 1)
)
upsParameterSeventhEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexseventh"),
)
if mibBuilder.loadTexts:
    upsParameterSeventhEntry.setStatus("current")
_UpsParameterLineIndexseventh_Type = PositiveInteger32
_UpsParameterLineIndexseventh_Object = MibTableColumn
upsParameterLineIndexseventh = _UpsParameterLineIndexseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 11, 1, 1),
    _UpsParameterLineIndexseventh_Type()
)
upsParameterLineIndexseventh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexseventh.setStatus("current")
_UpsParameterValueseventh_Type = Integer32
_UpsParameterValueseventh_Object = MibTableColumn
upsParameterValueseventh = _UpsParameterValueseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 11, 1, 2),
    _UpsParameterValueseventh_Type()
)
upsParameterValueseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValueseventh.setStatus("current")
_UpsStatusseventh_Type = NonNegativeInteger32
_UpsStatusseventh_Object = MibScalar
upsStatusseventh = _UpsStatusseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 12),
    _UpsStatusseventh_Type()
)
upsStatusseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusseventh.setStatus("current")
_UpsMainsStatisticsMBfailseventh_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailseventh_Object = MibScalar
upsMainsStatisticsMBfailseventh = _UpsMainsStatisticsMBfailseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 13),
    _UpsMainsStatisticsMBfailseventh_Type()
)
upsMainsStatisticsMBfailseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailseventh.setStatus("current")
_UpsMainsStatisticsMRfailseventh_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailseventh_Object = MibScalar
upsMainsStatisticsMRfailseventh = _UpsMainsStatisticsMRfailseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 14),
    _UpsMainsStatisticsMRfailseventh_Type()
)
upsMainsStatisticsMRfailseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailseventh.setStatus("current")
_UpsMainsStatisticsB2seventh_Type = NonNegativeInteger32
_UpsMainsStatisticsB2seventh_Object = MibScalar
upsMainsStatisticsB2seventh = _UpsMainsStatisticsB2seventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 15),
    _UpsMainsStatisticsB2seventh_Type()
)
upsMainsStatisticsB2seventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2seventh.setStatus("current")
_UpsMainsStatisticsB5seventh_Type = NonNegativeInteger32
_UpsMainsStatisticsB5seventh_Object = MibScalar
upsMainsStatisticsB5seventh = _UpsMainsStatisticsB5seventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 16),
    _UpsMainsStatisticsB5seventh_Type()
)
upsMainsStatisticsB5seventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5seventh.setStatus("current")
_UpsMainsStatisticsB10seventh_Type = NonNegativeInteger32
_UpsMainsStatisticsB10seventh_Object = MibScalar
upsMainsStatisticsB10seventh = _UpsMainsStatisticsB10seventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 17),
    _UpsMainsStatisticsB10seventh_Type()
)
upsMainsStatisticsB10seventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10seventh.setStatus("current")
_UpsMainsStatisticsB200seventh_Type = NonNegativeInteger32
_UpsMainsStatisticsB200seventh_Object = MibScalar
upsMainsStatisticsB200seventh = _UpsMainsStatisticsB200seventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 18),
    _UpsMainsStatisticsB200seventh_Type()
)
upsMainsStatisticsB200seventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200seventh.setStatus("current")
_UpsMainsStatisticsBypRelseventh_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelseventh_Object = MibScalar
upsMainsStatisticsBypRelseventh = _UpsMainsStatisticsBypRelseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 19),
    _UpsMainsStatisticsBypRelseventh_Type()
)
upsMainsStatisticsBypRelseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelseventh.setStatus("current")
_UpsTimeseventh_Type = NonNegativeInteger32
_UpsTimeseventh_Object = MibScalar
upsTimeseventh = _UpsTimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 20),
    _UpsTimeseventh_Type()
)
upsTimeseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimeseventh.setStatus("current")
_UpsRequestPermissionseventh_Type = DisplayString
_UpsRequestPermissionseventh_Object = MibScalar
upsRequestPermissionseventh = _UpsRequestPermissionseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 21),
    _UpsRequestPermissionseventh_Type()
)
upsRequestPermissionseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissionseventh.setStatus("current")
_UpsEventGetCodeseventh_Type = Integer32
_UpsEventGetCodeseventh_Object = MibScalar
upsEventGetCodeseventh = _UpsEventGetCodeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 22),
    _UpsEventGetCodeseventh_Type()
)
upsEventGetCodeseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodeseventh.setStatus("current")
_UpsEventSpinLockseventh_Type = TestAndIncr
_UpsEventSpinLockseventh_Object = MibScalar
upsEventSpinLockseventh = _UpsEventSpinLockseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 23),
    _UpsEventSpinLockseventh_Type()
)
upsEventSpinLockseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLockseventh.setStatus("current")
_UpsParameterSpinLockseventh_Type = TestAndIncr
_UpsParameterSpinLockseventh_Object = MibScalar
upsParameterSpinLockseventh = _UpsParameterSpinLockseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 10, 24),
    _UpsParameterSpinLockseventh_Type()
)
upsParameterSpinLockseventh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLockseventh.setStatus("current")
_GeUPSTrapsseventh_ObjectIdentity = ObjectIdentity
geUPSTrapsseventh = _GeUPSTrapsseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11)
)
_UpsDiagnosticseventh_ObjectIdentity = ObjectIdentity
upsDiagnosticseventh = _UpsDiagnosticseventh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12)
)
_UpsDiagnosticBusJACommunicationStatusseventh_Type = Integer32
_UpsDiagnosticBusJACommunicationStatusseventh_Object = MibScalar
upsDiagnosticBusJACommunicationStatusseventh = _UpsDiagnosticBusJACommunicationStatusseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12, 1),
    _UpsDiagnosticBusJACommunicationStatusseventh_Type()
)
upsDiagnosticBusJACommunicationStatusseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatusseventh.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatusseventh_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatusseventh_Object = MibScalar
upsDiagnosticBusJBCommunicationStatusseventh = _UpsDiagnosticBusJBCommunicationStatusseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatusseventh_Type()
)
upsDiagnosticBusJBCommunicationStatusseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatusseventh.setStatus("current")
_UpsDiagnosticBatteryLifetimeseventh_Type = Integer32
_UpsDiagnosticBatteryLifetimeseventh_Object = MibScalar
upsDiagnosticBatteryLifetimeseventh = _UpsDiagnosticBatteryLifetimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12, 3),
    _UpsDiagnosticBatteryLifetimeseventh_Type()
)
upsDiagnosticBatteryLifetimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimeseventh.setStatus("current")
_UpsDiagnosticFansLifetimeseventh_Type = Integer32
_UpsDiagnosticFansLifetimeseventh_Object = MibScalar
upsDiagnosticFansLifetimeseventh = _UpsDiagnosticFansLifetimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12, 4),
    _UpsDiagnosticFansLifetimeseventh_Type()
)
upsDiagnosticFansLifetimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimeseventh.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimeseventh_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimeseventh_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimeseventh = _UpsDiagnosticDCcapacitorsLifetimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimeseventh_Type()
)
upsDiagnosticDCcapacitorsLifetimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimeseventh.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimeseventh_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimeseventh_Object = MibScalar
upsDiagnosticACcapacitorsLifetimeseventh = _UpsDiagnosticACcapacitorsLifetimeseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimeseventh_Type()
)
upsDiagnosticACcapacitorsLifetimeseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimeseventh.setStatus("current")
_UpsDiagnosticGlobalServiceCheckseventh_Type = Integer32
_UpsDiagnosticGlobalServiceCheckseventh_Object = MibScalar
upsDiagnosticGlobalServiceCheckseventh = _UpsDiagnosticGlobalServiceCheckseventh_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 12, 7),
    _UpsDiagnosticGlobalServiceCheckseventh_Type()
)
upsDiagnosticGlobalServiceCheckseventh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheckseventh.setStatus("current")
_GeEighthUPS_ObjectIdentity = ObjectIdentity
geEighthUPS = _GeEighthUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18)
)
_UpsIdenteighth_ObjectIdentity = ObjectIdentity
upsIdenteighth = _UpsIdenteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1)
)
_UpsIdentManufacturereighth_Type = DisplayString
_UpsIdentManufacturereighth_Object = MibScalar
upsIdentManufacturereighth = _UpsIdentManufacturereighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 1),
    _UpsIdentManufacturereighth_Type()
)
upsIdentManufacturereighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturereighth.setStatus("current")
_UpsIdentModeleighth_Type = DisplayString
_UpsIdentModeleighth_Object = MibScalar
upsIdentModeleighth = _UpsIdentModeleighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 2),
    _UpsIdentModeleighth_Type()
)
upsIdentModeleighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModeleighth.setStatus("current")
_UpsIdentUPSSoftwareVersioneighth_Type = DisplayString
_UpsIdentUPSSoftwareVersioneighth_Object = MibScalar
upsIdentUPSSoftwareVersioneighth = _UpsIdentUPSSoftwareVersioneighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 3),
    _UpsIdentUPSSoftwareVersioneighth_Type()
)
upsIdentUPSSoftwareVersioneighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersioneighth.setStatus("current")
_UpsIdentAgentSoftwareVersioneighth_Type = DisplayString
_UpsIdentAgentSoftwareVersioneighth_Object = MibScalar
upsIdentAgentSoftwareVersioneighth = _UpsIdentAgentSoftwareVersioneighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 4),
    _UpsIdentAgentSoftwareVersioneighth_Type()
)
upsIdentAgentSoftwareVersioneighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersioneighth.setStatus("current")
_UpsIdentNameeighth_Type = DisplayString
_UpsIdentNameeighth_Object = MibScalar
upsIdentNameeighth = _UpsIdentNameeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 5),
    _UpsIdentNameeighth_Type()
)
upsIdentNameeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNameeighth.setStatus("current")
_UpsIdentAttachedDeviceseighth_Type = DisplayString
_UpsIdentAttachedDeviceseighth_Object = MibScalar
upsIdentAttachedDeviceseighth = _UpsIdentAttachedDeviceseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 6),
    _UpsIdentAttachedDeviceseighth_Type()
)
upsIdentAttachedDeviceseighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDeviceseighth.setStatus("current")
_UpsIdentUPSSerialNumbereighth_Type = DisplayString
_UpsIdentUPSSerialNumbereighth_Object = MibScalar
upsIdentUPSSerialNumbereighth = _UpsIdentUPSSerialNumbereighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 7),
    _UpsIdentUPSSerialNumbereighth_Type()
)
upsIdentUPSSerialNumbereighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumbereighth.setStatus("current")
_UpsIdentComProtVersioneighth_Type = DisplayString
_UpsIdentComProtVersioneighth_Object = MibScalar
upsIdentComProtVersioneighth = _UpsIdentComProtVersioneighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 8),
    _UpsIdentComProtVersioneighth_Type()
)
upsIdentComProtVersioneighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersioneighth.setStatus("current")
_UpsIdentOperatingTimeeighth_Type = NonNegativeInteger32
_UpsIdentOperatingTimeeighth_Object = MibScalar
upsIdentOperatingTimeeighth = _UpsIdentOperatingTimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 1, 9),
    _UpsIdentOperatingTimeeighth_Type()
)
upsIdentOperatingTimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimeeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimeeighth.setUnits("eighths")
_UpsBatteryeighth_ObjectIdentity = ObjectIdentity
upsBatteryeighth = _UpsBatteryeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2)
)


class _UpsBatteryStatuseighth_Type(Integer32):
    """Custom type upsBatteryStatuseighth based on Integer32"""
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


_UpsBatteryStatuseighth_Type.__name__ = "Integer32"
_UpsBatteryStatuseighth_Object = MibScalar
upsBatteryStatuseighth = _UpsBatteryStatuseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 1),
    _UpsBatteryStatuseighth_Type()
)
upsBatteryStatuseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatuseighth.setStatus("current")
_UpsSecondsOnBatteryeighth_Type = NonNegativeInteger32
_UpsSecondsOnBatteryeighth_Object = MibScalar
upsSecondsOnBatteryeighth = _UpsSecondsOnBatteryeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 2),
    _UpsSecondsOnBatteryeighth_Type()
)
upsSecondsOnBatteryeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatteryeighth.setUnits("eighths")
_UpsEstimatedMinutesRemainingeighth_Type = PositiveInteger32
_UpsEstimatedMinutesRemainingeighth_Object = MibScalar
upsEstimatedMinutesRemainingeighth = _UpsEstimatedMinutesRemainingeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 3),
    _UpsEstimatedMinutesRemainingeighth_Type()
)
upsEstimatedMinutesRemainingeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemainingeighth.setUnits("minutes")


class _UpsEstimatedChargeRemainingeighth_Type(Integer32):
    """Custom type upsEstimatedChargeRemainingeighth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemainingeighth_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemainingeighth_Object = MibScalar
upsEstimatedChargeRemainingeighth = _UpsEstimatedChargeRemainingeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 4),
    _UpsEstimatedChargeRemainingeighth_Type()
)
upsEstimatedChargeRemainingeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemainingeighth.setUnits("percent")
_UpsBatteryVoltageeighth_Type = NonNegativeInteger32
_UpsBatteryVoltageeighth_Object = MibScalar
upsBatteryVoltageeighth = _UpsBatteryVoltageeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 5),
    _UpsBatteryVoltageeighth_Type()
)
upsBatteryVoltageeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltageeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltageeighth.setUnits("0.1 Volt DC")
_UpsBatteryCurrenteighth_Type = Integer32
_UpsBatteryCurrenteighth_Object = MibScalar
upsBatteryCurrenteighth = _UpsBatteryCurrenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 6),
    _UpsBatteryCurrenteighth_Type()
)
upsBatteryCurrenteighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrenteighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrenteighth.setUnits("0.1 Amp DC")
_UpsBatteryTemperatureeighth_Type = Integer32
_UpsBatteryTemperatureeighth_Object = MibScalar
upsBatteryTemperatureeighth = _UpsBatteryTemperatureeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 7),
    _UpsBatteryTemperatureeighth_Type()
)
upsBatteryTemperatureeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperatureeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperatureeighth.setUnits("degrees Centigrade")
_UpsBatteryRippleeighth_Type = Integer32
_UpsBatteryRippleeighth_Object = MibScalar
upsBatteryRippleeighth = _UpsBatteryRippleeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 2, 8),
    _UpsBatteryRippleeighth_Type()
)
upsBatteryRippleeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRippleeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRippleeighth.setUnits("0.1 Volt RMS")
_UpsInputeighth_ObjectIdentity = ObjectIdentity
upsInputeighth = _UpsInputeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3)
)
_UpsInputLineBadseighth_Type = Counter32
_UpsInputLineBadseighth_Object = MibScalar
upsInputLineBadseighth = _UpsInputLineBadseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 1),
    _UpsInputLineBadseighth_Type()
)
upsInputLineBadseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadseighth.setStatus("current")
_UpsInputNumLineseighth_Type = NonNegativeInteger32
_UpsInputNumLineseighth_Object = MibScalar
upsInputNumLineseighth = _UpsInputNumLineseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 2),
    _UpsInputNumLineseighth_Type()
)
upsInputNumLineseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLineseighth.setStatus("current")
_UpsInputEighthTable_Object = MibTable
upsInputEighthTable = _UpsInputEighthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputEighthTable.setStatus("current")
_UpsInputEighthEntry_Object = MibTableRow
upsInputEighthEntry = _UpsInputEighthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1)
)
upsInputEighthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsInputLineIndexeighth"),
)
if mibBuilder.loadTexts:
    upsInputEighthEntry.setStatus("current")
_UpsInputLineIndexeighth_Type = PositiveInteger32
_UpsInputLineIndexeighth_Object = MibTableColumn
upsInputLineIndexeighth = _UpsInputLineIndexeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1, 1),
    _UpsInputLineIndexeighth_Type()
)
upsInputLineIndexeighth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexeighth.setStatus("current")
_UpsInputFrequencyeighth_Type = NonNegativeInteger32
_UpsInputFrequencyeighth_Object = MibTableColumn
upsInputFrequencyeighth = _UpsInputFrequencyeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1, 2),
    _UpsInputFrequencyeighth_Type()
)
upsInputFrequencyeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyeighth.setUnits("0.1 Hertz")
_UpsInputVoltageeighth_Type = NonNegativeInteger32
_UpsInputVoltageeighth_Object = MibTableColumn
upsInputVoltageeighth = _UpsInputVoltageeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1, 3),
    _UpsInputVoltageeighth_Type()
)
upsInputVoltageeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageeighth.setUnits("RMS Volts")
_UpsInputCurrenteighth_Type = NonNegativeInteger32
_UpsInputCurrenteighth_Object = MibTableColumn
upsInputCurrenteighth = _UpsInputCurrenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1, 4),
    _UpsInputCurrenteighth_Type()
)
upsInputCurrenteighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrenteighth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrenteighth.setUnits("0.1 RMS Amp")
_UpsInputTruePowereighth_Type = NonNegativeInteger32
_UpsInputTruePowereighth_Object = MibTableColumn
upsInputTruePowereighth = _UpsInputTruePowereighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1, 5),
    _UpsInputTruePowereighth_Type()
)
upsInputTruePowereighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowereighth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowereighth.setUnits("Watts")
_UpsInputVoltageMineighth_Type = NonNegativeInteger32
_UpsInputVoltageMineighth_Object = MibTableColumn
upsInputVoltageMineighth = _UpsInputVoltageMineighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1, 6),
    _UpsInputVoltageMineighth_Type()
)
upsInputVoltageMineighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMineighth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMineighth.setUnits("RMS Volts")
_UpsInputVoltageMaxeighth_Type = NonNegativeInteger32
_UpsInputVoltageMaxeighth_Object = MibTableColumn
upsInputVoltageMaxeighth = _UpsInputVoltageMaxeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 3, 3, 1, 7),
    _UpsInputVoltageMaxeighth_Type()
)
upsInputVoltageMaxeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxeighth.setUnits("RMS Volts")
_UpsOutputeighth_ObjectIdentity = ObjectIdentity
upsOutputeighth = _UpsOutputeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4)
)


class _UpsOutputSourceeighth_Type(Integer32):
    """Custom type upsOutputSourceeighth based on Integer32"""
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


_UpsOutputSourceeighth_Type.__name__ = "Integer32"
_UpsOutputSourceeighth_Object = MibScalar
upsOutputSourceeighth = _UpsOutputSourceeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 1),
    _UpsOutputSourceeighth_Type()
)
upsOutputSourceeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourceeighth.setStatus("current")
_UpsOutputFrequencyeighth_Type = NonNegativeInteger32
_UpsOutputFrequencyeighth_Object = MibScalar
upsOutputFrequencyeighth = _UpsOutputFrequencyeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 2),
    _UpsOutputFrequencyeighth_Type()
)
upsOutputFrequencyeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencyeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencyeighth.setUnits("0.1 Hertz")
_UpsOutputNumLineseighth_Type = NonNegativeInteger32
_UpsOutputNumLineseighth_Object = MibScalar
upsOutputNumLineseighth = _UpsOutputNumLineseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 3),
    _UpsOutputNumLineseighth_Type()
)
upsOutputNumLineseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLineseighth.setStatus("current")
_UpsOutputEighthTable_Object = MibTable
upsOutputEighthTable = _UpsOutputEighthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputEighthTable.setStatus("current")
_UpsOutputEighthEntry_Object = MibTableRow
upsOutputEighthEntry = _UpsOutputEighthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1)
)
upsOutputEighthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsOutputLineIndexeighth"),
)
if mibBuilder.loadTexts:
    upsOutputEighthEntry.setStatus("current")
_UpsOutputLineIndexeighth_Type = PositiveInteger32
_UpsOutputLineIndexeighth_Object = MibTableColumn
upsOutputLineIndexeighth = _UpsOutputLineIndexeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 1),
    _UpsOutputLineIndexeighth_Type()
)
upsOutputLineIndexeighth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexeighth.setStatus("current")
_UpsOutputVoltageeighth_Type = NonNegativeInteger32
_UpsOutputVoltageeighth_Object = MibTableColumn
upsOutputVoltageeighth = _UpsOutputVoltageeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 2),
    _UpsOutputVoltageeighth_Type()
)
upsOutputVoltageeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltageeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltageeighth.setUnits("RMS Volts")
_UpsOutputCurrenteighth_Type = NonNegativeInteger32
_UpsOutputCurrenteighth_Object = MibTableColumn
upsOutputCurrenteighth = _UpsOutputCurrenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 3),
    _UpsOutputCurrenteighth_Type()
)
upsOutputCurrenteighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrenteighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrenteighth.setUnits("0.1 RMS Amp")
_UpsOutputPowereighth_Type = NonNegativeInteger32
_UpsOutputPowereighth_Object = MibTableColumn
upsOutputPowereighth = _UpsOutputPowereighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 4),
    _UpsOutputPowereighth_Type()
)
upsOutputPowereighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowereighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowereighth.setUnits("Watts")


class _UpsOutputPercentLoadeighth_Type(Integer32):
    """Custom type upsOutputPercentLoadeighth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadeighth_Type.__name__ = "Integer32"
_UpsOutputPercentLoadeighth_Object = MibTableColumn
upsOutputPercentLoadeighth = _UpsOutputPercentLoadeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 5),
    _UpsOutputPercentLoadeighth_Type()
)
upsOutputPercentLoadeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadeighth.setUnits("percent")


class _UpsOutputPowerFactoreighth_Type(Integer32):
    """Custom type upsOutputPowerFactoreighth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactoreighth_Type.__name__ = "Integer32"
_UpsOutputPowerFactoreighth_Object = MibTableColumn
upsOutputPowerFactoreighth = _UpsOutputPowerFactoreighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 6),
    _UpsOutputPowerFactoreighth_Type()
)
upsOutputPowerFactoreighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactoreighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactoreighth.setUnits("0.01 cos phi")
_UpsOutputPeakCurrenteighth_Type = Integer32
_UpsOutputPeakCurrenteighth_Object = MibTableColumn
upsOutputPeakCurrenteighth = _UpsOutputPeakCurrenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 7),
    _UpsOutputPeakCurrenteighth_Type()
)
upsOutputPeakCurrenteighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrenteighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrenteighth.setUnits("Amps")
_UpsOutputShareCurrenteighth_Type = Integer32
_UpsOutputShareCurrenteighth_Object = MibTableColumn
upsOutputShareCurrenteighth = _UpsOutputShareCurrenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 4, 4, 1, 8),
    _UpsOutputShareCurrenteighth_Type()
)
upsOutputShareCurrenteighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrenteighth.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrenteighth.setUnits("Amps")
_UpsBypasseighth_ObjectIdentity = ObjectIdentity
upsBypasseighth = _UpsBypasseighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5)
)
_UpsBypassFrequencyeighth_Type = NonNegativeInteger32
_UpsBypassFrequencyeighth_Object = MibScalar
upsBypassFrequencyeighth = _UpsBypassFrequencyeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 1),
    _UpsBypassFrequencyeighth_Type()
)
upsBypassFrequencyeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencyeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencyeighth.setUnits("0.1 Hertz")
_UpsBypassNumLineseighth_Type = NonNegativeInteger32
_UpsBypassNumLineseighth_Object = MibScalar
upsBypassNumLineseighth = _UpsBypassNumLineseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 2),
    _UpsBypassNumLineseighth_Type()
)
upsBypassNumLineseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLineseighth.setStatus("current")
_UpsBypassEighthTable_Object = MibTable
upsBypassEighthTable = _UpsBypassEighthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassEighthTable.setStatus("current")
_UpsBypassEighthEntry_Object = MibTableRow
upsBypassEighthEntry = _UpsBypassEighthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 3, 1)
)
upsBypassEighthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsBypassLineIndexeighth"),
)
if mibBuilder.loadTexts:
    upsBypassEighthEntry.setStatus("current")
_UpsBypassLineIndexeighth_Type = PositiveInteger32
_UpsBypassLineIndexeighth_Object = MibTableColumn
upsBypassLineIndexeighth = _UpsBypassLineIndexeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 3, 1, 1),
    _UpsBypassLineIndexeighth_Type()
)
upsBypassLineIndexeighth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexeighth.setStatus("current")
_UpsBypassVoltageeighth_Type = NonNegativeInteger32
_UpsBypassVoltageeighth_Object = MibTableColumn
upsBypassVoltageeighth = _UpsBypassVoltageeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 3, 1, 2),
    _UpsBypassVoltageeighth_Type()
)
upsBypassVoltageeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltageeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltageeighth.setUnits("RMS Volts")
_UpsBypassCurrenteighth_Type = NonNegativeInteger32
_UpsBypassCurrenteighth_Object = MibTableColumn
upsBypassCurrenteighth = _UpsBypassCurrenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 3, 1, 3),
    _UpsBypassCurrenteighth_Type()
)
upsBypassCurrenteighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrenteighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrenteighth.setUnits("0.1 RMS Amp")
_UpsBypassPowereighth_Type = NonNegativeInteger32
_UpsBypassPowereighth_Object = MibTableColumn
upsBypassPowereighth = _UpsBypassPowereighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 5, 3, 1, 4),
    _UpsBypassPowereighth_Type()
)
upsBypassPowereighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowereighth.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowereighth.setUnits("Watts")
_UpsAlarmeighth_ObjectIdentity = ObjectIdentity
upsAlarmeighth = _UpsAlarmeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6)
)
_UpsAlarmsPresenteighth_Type = Gauge32
_UpsAlarmsPresenteighth_Object = MibScalar
upsAlarmsPresenteighth = _UpsAlarmsPresenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 1),
    _UpsAlarmsPresenteighth_Type()
)
upsAlarmsPresenteighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresenteighth.setStatus("current")
_UpsAlarmEighthTable_Object = MibTable
upsAlarmEighthTable = _UpsAlarmEighthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmEighthTable.setStatus("current")
_UpsAlarmEighthEntry_Object = MibTableRow
upsAlarmEighthEntry = _UpsAlarmEighthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 2, 1)
)
upsAlarmEighthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsAlarmIdeighth"),
)
if mibBuilder.loadTexts:
    upsAlarmEighthEntry.setStatus("current")
_UpsAlarmIdeighth_Type = PositiveInteger32
_UpsAlarmIdeighth_Object = MibTableColumn
upsAlarmIdeighth = _UpsAlarmIdeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 2, 1, 1),
    _UpsAlarmIdeighth_Type()
)
upsAlarmIdeighth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdeighth.setStatus("current")
_UpsAlarmDescreighth_Type = AutonomousType
_UpsAlarmDescreighth_Object = MibTableColumn
upsAlarmDescreighth = _UpsAlarmDescreighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 2, 1, 2),
    _UpsAlarmDescreighth_Type()
)
upsAlarmDescreighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescreighth.setStatus("current")
_UpsAlarmTimeeighth_Type = TimeStamp
_UpsAlarmTimeeighth_Object = MibTableColumn
upsAlarmTimeeighth = _UpsAlarmTimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 2, 1, 3),
    _UpsAlarmTimeeighth_Type()
)
upsAlarmTimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimeeighth.setStatus("current")
_UpsWellKnownAlarmseighth_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmseighth = _UpsWellKnownAlarmseighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3)
)
_UpsAlarmBatteryBadeighth_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadeighth = _UpsAlarmBatteryBadeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadeighth.setStatus("current")
_UpsAlarmOnBatteryeighth_ObjectIdentity = ObjectIdentity
upsAlarmOnBatteryeighth = _UpsAlarmOnBatteryeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatteryeighth.setStatus("current")
_UpsAlarmLowBatteryeighth_ObjectIdentity = ObjectIdentity
upsAlarmLowBatteryeighth = _UpsAlarmLowBatteryeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatteryeighth.setStatus("current")
_UpsAlarmDepletedBatteryeighth_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatteryeighth = _UpsAlarmDepletedBatteryeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatteryeighth.setStatus("current")
_UpsAlarmTempBadeighth_ObjectIdentity = ObjectIdentity
upsAlarmTempBadeighth = _UpsAlarmTempBadeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadeighth.setStatus("current")
_UpsAlarmInputBadeighth_ObjectIdentity = ObjectIdentity
upsAlarmInputBadeighth = _UpsAlarmInputBadeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadeighth.setStatus("current")
_UpsAlarmOutputBadeighth_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadeighth = _UpsAlarmOutputBadeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadeighth.setStatus("current")
_UpsAlarmOutputOverloadeighth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadeighth = _UpsAlarmOutputOverloadeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadeighth.setStatus("current")
_UpsAlarmOnBypasseighth_ObjectIdentity = ObjectIdentity
upsAlarmOnBypasseighth = _UpsAlarmOnBypasseighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypasseighth.setStatus("current")
_UpsAlarmBypassBadeighth_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadeighth = _UpsAlarmBypassBadeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadeighth.setStatus("current")
_UpsAlarmOutputOffAsRequestedeighth_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedeighth = _UpsAlarmOutputOffAsRequestedeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedeighth.setStatus("current")
_UpsAlarmUpsOffAsRequestedeighth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedeighth = _UpsAlarmUpsOffAsRequestedeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedeighth.setStatus("current")
_UpsAlarmChargerFailedeighth_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedeighth = _UpsAlarmChargerFailedeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedeighth.setStatus("current")
_UpsAlarmUpsOutputOffeighth_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOffeighth = _UpsAlarmUpsOutputOffeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOffeighth.setStatus("current")
_UpsAlarmUpsSystemOffeighth_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOffeighth = _UpsAlarmUpsSystemOffeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOffeighth.setStatus("current")
_UpsAlarmFanFailureeighth_ObjectIdentity = ObjectIdentity
upsAlarmFanFailureeighth = _UpsAlarmFanFailureeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailureeighth.setStatus("current")
_UpsAlarmFuseFailureeighth_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailureeighth = _UpsAlarmFuseFailureeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailureeighth.setStatus("current")
_UpsAlarmGeneralFaulteighth_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaulteighth = _UpsAlarmGeneralFaulteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaulteighth.setStatus("current")
_UpsAlarmDiagnosticTestFailedeighth_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedeighth = _UpsAlarmDiagnosticTestFailedeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedeighth.setStatus("current")
_UpsAlarmCommunicationsLosteighth_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLosteighth = _UpsAlarmCommunicationsLosteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLosteighth.setStatus("current")
_UpsAlarmAwaitingPowereighth_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowereighth = _UpsAlarmAwaitingPowereighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowereighth.setStatus("current")
_UpsAlarmShutdownPendingeighth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendingeighth = _UpsAlarmShutdownPendingeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendingeighth.setStatus("current")
_UpsAlarmShutdownImminenteighth_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminenteighth = _UpsAlarmShutdownImminenteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminenteighth.setStatus("current")
_UpsAlarmTestInProgresseighth_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgresseighth = _UpsAlarmTestInProgresseighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgresseighth.setStatus("current")
_UpsAlarmReceptacleOffeighth_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOffeighth = _UpsAlarmReceptacleOffeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOffeighth.setStatus("current")
_UpsAlarmHighSpeedBusFailureeighth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailureeighth = _UpsAlarmHighSpeedBusFailureeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailureeighth.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailureeighth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailureeighth = _UpsAlarmHighSpeedBusJACRCFailureeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailureeighth.setStatus("current")
_UpsAlarmConnectivityBusFailureeighth_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailureeighth = _UpsAlarmConnectivityBusFailureeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailureeighth.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailureeighth_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailureeighth = _UpsAlarmHighSpeedBusJBCRCFailureeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailureeighth.setStatus("current")
_UpsAlarmCurrentSharingeighth_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharingeighth = _UpsAlarmCurrentSharingeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharingeighth.setStatus("current")
_UpsAlarmDCRippleeighth_ObjectIdentity = ObjectIdentity
upsAlarmDCRippleeighth = _UpsAlarmDCRippleeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRippleeighth.setStatus("current")
_UpsAlarmMaskAeighth_Type = Unsigned32
_UpsAlarmMaskAeighth_Object = MibScalar
upsAlarmMaskAeighth = _UpsAlarmMaskAeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 6, 4),
    _UpsAlarmMaskAeighth_Type()
)
upsAlarmMaskAeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAeighth.setStatus("current")
_UpsTesteighth_ObjectIdentity = ObjectIdentity
upsTesteighth = _UpsTesteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7)
)
_UpsTestIdeighth_Type = ObjectIdentifier
_UpsTestIdeighth_Object = MibScalar
upsTestIdeighth = _UpsTestIdeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 1),
    _UpsTestIdeighth_Type()
)
upsTestIdeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdeighth.setStatus("current")
_UpsTestSpinLockeighth_Type = TestAndIncr
_UpsTestSpinLockeighth_Object = MibScalar
upsTestSpinLockeighth = _UpsTestSpinLockeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 2),
    _UpsTestSpinLockeighth_Type()
)
upsTestSpinLockeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLockeighth.setStatus("current")


class _UpsTestResultsSummaryeighth_Type(Integer32):
    """Custom type upsTestResultsSummaryeighth based on Integer32"""
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


_UpsTestResultsSummaryeighth_Type.__name__ = "Integer32"
_UpsTestResultsSummaryeighth_Object = MibScalar
upsTestResultsSummaryeighth = _UpsTestResultsSummaryeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 3),
    _UpsTestResultsSummaryeighth_Type()
)
upsTestResultsSummaryeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummaryeighth.setStatus("current")
_UpsTestResultsDetaileighth_Type = DisplayString
_UpsTestResultsDetaileighth_Object = MibScalar
upsTestResultsDetaileighth = _UpsTestResultsDetaileighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 4),
    _UpsTestResultsDetaileighth_Type()
)
upsTestResultsDetaileighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetaileighth.setStatus("current")
_UpsTestStartTimeeighth_Type = TimeStamp
_UpsTestStartTimeeighth_Object = MibScalar
upsTestStartTimeeighth = _UpsTestStartTimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 5),
    _UpsTestStartTimeeighth_Type()
)
upsTestStartTimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimeeighth.setStatus("current")
_UpsTestElapsedTimeeighth_Type = TimeInterval
_UpsTestElapsedTimeeighth_Object = MibScalar
upsTestElapsedTimeeighth = _UpsTestElapsedTimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 6),
    _UpsTestElapsedTimeeighth_Type()
)
upsTestElapsedTimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimeeighth.setStatus("current")
_UpsWellKnownTestseighth_ObjectIdentity = ObjectIdentity
upsWellKnownTestseighth = _UpsWellKnownTestseighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 7)
)
_UpsTestNoTestsInitiatedeighth_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedeighth = _UpsTestNoTestsInitiatedeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedeighth.setStatus("current")
_UpsTestAbortTestInProgresseighth_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgresseighth = _UpsTestAbortTestInProgresseighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgresseighth.setStatus("current")
_UpsTestGeneralSystemsTesteighth_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTesteighth = _UpsTestGeneralSystemsTesteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTesteighth.setStatus("current")
_UpsTestQuickBatteryTesteighth_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTesteighth = _UpsTestQuickBatteryTesteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTesteighth.setStatus("current")
_UpsTestDeepBatteryCalibrationeighth_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationeighth = _UpsTestDeepBatteryCalibrationeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationeighth.setStatus("current")
_UpsControleighth_ObjectIdentity = ObjectIdentity
upsControleighth = _UpsControleighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8)
)


class _UpsShutdownTypeeighth_Type(Integer32):
    """Custom type upsShutdownTypeeighth based on Integer32"""
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


_UpsShutdownTypeeighth_Type.__name__ = "Integer32"
_UpsShutdownTypeeighth_Object = MibScalar
upsShutdownTypeeighth = _UpsShutdownTypeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 1),
    _UpsShutdownTypeeighth_Type()
)
upsShutdownTypeeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypeeighth.setStatus("current")


class _UpsShutdownAfterDelayeighth_Type(Integer32):
    """Custom type upsShutdownAfterDelayeighth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelayeighth_Type.__name__ = "Integer32"
_UpsShutdownAfterDelayeighth_Object = MibScalar
upsShutdownAfterDelayeighth = _UpsShutdownAfterDelayeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 2),
    _UpsShutdownAfterDelayeighth_Type()
)
upsShutdownAfterDelayeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelayeighth.setUnits("eighths")


class _UpsStartupAfterDelayeighth_Type(Integer32):
    """Custom type upsStartupAfterDelayeighth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelayeighth_Type.__name__ = "Integer32"
_UpsStartupAfterDelayeighth_Object = MibScalar
upsStartupAfterDelayeighth = _UpsStartupAfterDelayeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 3),
    _UpsStartupAfterDelayeighth_Type()
)
upsStartupAfterDelayeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelayeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelayeighth.setUnits("eighths")


class _UpsRebootWithDurationeighth_Type(Integer32):
    """Custom type upsRebootWithDurationeighth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationeighth_Type.__name__ = "Integer32"
_UpsRebootWithDurationeighth_Object = MibScalar
upsRebootWithDurationeighth = _UpsRebootWithDurationeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 4),
    _UpsRebootWithDurationeighth_Type()
)
upsRebootWithDurationeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationeighth.setUnits("eighths")


class _UpsAutoRestarteighth_Type(Integer32):
    """Custom type upsAutoRestarteighth based on Integer32"""
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


_UpsAutoRestarteighth_Type.__name__ = "Integer32"
_UpsAutoRestarteighth_Object = MibScalar
upsAutoRestarteighth = _UpsAutoRestarteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 5),
    _UpsAutoRestarteighth_Type()
)
upsAutoRestarteighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestarteighth.setStatus("current")
_UpsReceptaclesNumeighth_Type = NonNegativeInteger32
_UpsReceptaclesNumeighth_Object = MibScalar
upsReceptaclesNumeighth = _UpsReceptaclesNumeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 6),
    _UpsReceptaclesNumeighth_Type()
)
upsReceptaclesNumeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumeighth.setStatus("current")
_UpsReceptacleEighthTable_Object = MibTable
upsReceptacleEighthTable = _UpsReceptacleEighthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleEighthTable.setStatus("current")
_UpsReceptacleEighthEntry_Object = MibTableRow
upsReceptacleEighthEntry = _UpsReceptacleEighthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 7, 1)
)
upsReceptacleEighthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsReceptacleLineIndexeighth"),
)
if mibBuilder.loadTexts:
    upsReceptacleEighthEntry.setStatus("current")
_UpsReceptacleLineIndexeighth_Type = PositiveInteger32
_UpsReceptacleLineIndexeighth_Object = MibTableColumn
upsReceptacleLineIndexeighth = _UpsReceptacleLineIndexeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 7, 1, 1),
    _UpsReceptacleLineIndexeighth_Type()
)
upsReceptacleLineIndexeighth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexeighth.setStatus("current")


class _UpsReceptacleOnOffeighth_Type(Integer32):
    """Custom type upsReceptacleOnOffeighth based on Integer32"""
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


_UpsReceptacleOnOffeighth_Type.__name__ = "Integer32"
_UpsReceptacleOnOffeighth_Object = MibTableColumn
upsReceptacleOnOffeighth = _UpsReceptacleOnOffeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 7, 1, 2),
    _UpsReceptacleOnOffeighth_Type()
)
upsReceptacleOnOffeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOffeighth.setStatus("current")


class _UpsUPSModeeighth_Type(Integer32):
    """Custom type upsUPSModeeighth based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModeeighth_Type.__name__ = "Integer32"
_UpsUPSModeeighth_Object = MibScalar
upsUPSModeeighth = _UpsUPSModeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 8),
    _UpsUPSModeeighth_Type()
)
upsUPSModeeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModeeighth.setStatus("current")


class _UpsRectifierOnOffeighth_Type(Integer32):
    """Custom type upsRectifierOnOffeighth based on Integer32"""
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


_UpsRectifierOnOffeighth_Type.__name__ = "Integer32"
_UpsRectifierOnOffeighth_Object = MibScalar
upsRectifierOnOffeighth = _UpsRectifierOnOffeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 9),
    _UpsRectifierOnOffeighth_Type()
)
upsRectifierOnOffeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOffeighth.setStatus("current")


class _UpsBatteryChargeMethodeighth_Type(Integer32):
    """Custom type upsBatteryChargeMethodeighth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodeighth_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodeighth_Object = MibScalar
upsBatteryChargeMethodeighth = _UpsBatteryChargeMethodeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 10),
    _UpsBatteryChargeMethodeighth_Type()
)
upsBatteryChargeMethodeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodeighth.setStatus("current")


class _UpsInverterOnOffeighth_Type(Integer32):
    """Custom type upsInverterOnOffeighth based on Integer32"""
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


_UpsInverterOnOffeighth_Type.__name__ = "Integer32"
_UpsInverterOnOffeighth_Object = MibScalar
upsInverterOnOffeighth = _UpsInverterOnOffeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 11),
    _UpsInverterOnOffeighth_Type()
)
upsInverterOnOffeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOffeighth.setStatus("current")


class _UpsBypassOnOffeighth_Type(Integer32):
    """Custom type upsBypassOnOffeighth based on Integer32"""
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


_UpsBypassOnOffeighth_Type.__name__ = "Integer32"
_UpsBypassOnOffeighth_Object = MibScalar
upsBypassOnOffeighth = _UpsBypassOnOffeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 12),
    _UpsBypassOnOffeighth_Type()
)
upsBypassOnOffeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOffeighth.setStatus("current")


class _UpsLoadSourceeighth_Type(Integer32):
    """Custom type upsLoadSourceeighth based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourceeighth_Type.__name__ = "Integer32"
_UpsLoadSourceeighth_Object = MibScalar
upsLoadSourceeighth = _UpsLoadSourceeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 8, 13),
    _UpsLoadSourceeighth_Type()
)
upsLoadSourceeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourceeighth.setStatus("current")
_UpsConfigeighth_ObjectIdentity = ObjectIdentity
upsConfigeighth = _UpsConfigeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9)
)
_UpsConfigInputVoltageeighth_Type = NonNegativeInteger32
_UpsConfigInputVoltageeighth_Object = MibScalar
upsConfigInputVoltageeighth = _UpsConfigInputVoltageeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 1),
    _UpsConfigInputVoltageeighth_Type()
)
upsConfigInputVoltageeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltageeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltageeighth.setUnits("RMS Volts")
_UpsConfigInputFreqeighth_Type = NonNegativeInteger32
_UpsConfigInputFreqeighth_Object = MibScalar
upsConfigInputFreqeighth = _UpsConfigInputFreqeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 2),
    _UpsConfigInputFreqeighth_Type()
)
upsConfigInputFreqeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqeighth.setUnits("0.1 Hertz")
_UpsConfigOutputVoltageeighth_Type = NonNegativeInteger32
_UpsConfigOutputVoltageeighth_Object = MibScalar
upsConfigOutputVoltageeighth = _UpsConfigOutputVoltageeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 3),
    _UpsConfigOutputVoltageeighth_Type()
)
upsConfigOutputVoltageeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltageeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltageeighth.setUnits("RMS Volts")
_UpsConfigOutputFreqeighth_Type = NonNegativeInteger32
_UpsConfigOutputFreqeighth_Object = MibScalar
upsConfigOutputFreqeighth = _UpsConfigOutputFreqeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 4),
    _UpsConfigOutputFreqeighth_Type()
)
upsConfigOutputFreqeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqeighth.setUnits("0.1 Hertz")
_UpsConfigOutputVAeighth_Type = NonNegativeInteger32
_UpsConfigOutputVAeighth_Object = MibScalar
upsConfigOutputVAeighth = _UpsConfigOutputVAeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 5),
    _UpsConfigOutputVAeighth_Type()
)
upsConfigOutputVAeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAeighth.setUnits("Volt-Amps")
_UpsConfigOutputPowereighth_Type = NonNegativeInteger32
_UpsConfigOutputPowereighth_Object = MibScalar
upsConfigOutputPowereighth = _UpsConfigOutputPowereighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 6),
    _UpsConfigOutputPowereighth_Type()
)
upsConfigOutputPowereighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowereighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowereighth.setUnits("Watts")
_UpsConfigLowBattTimeeighth_Type = NonNegativeInteger32
_UpsConfigLowBattTimeeighth_Object = MibScalar
upsConfigLowBattTimeeighth = _UpsConfigLowBattTimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 7),
    _UpsConfigLowBattTimeeighth_Type()
)
upsConfigLowBattTimeeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimeeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimeeighth.setUnits("minutes")


class _UpsConfigAudibleStatuseighth_Type(Integer32):
    """Custom type upsConfigAudibleStatuseighth based on Integer32"""
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


_UpsConfigAudibleStatuseighth_Type.__name__ = "Integer32"
_UpsConfigAudibleStatuseighth_Object = MibScalar
upsConfigAudibleStatuseighth = _UpsConfigAudibleStatuseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 8),
    _UpsConfigAudibleStatuseighth_Type()
)
upsConfigAudibleStatuseighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatuseighth.setStatus("current")
_UpsConfigLowVoltageTransferPointeighth_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointeighth_Object = MibScalar
upsConfigLowVoltageTransferPointeighth = _UpsConfigLowVoltageTransferPointeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 9),
    _UpsConfigLowVoltageTransferPointeighth_Type()
)
upsConfigLowVoltageTransferPointeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointeighth.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointeighth_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointeighth_Object = MibScalar
upsConfigHighVoltageTransferPointeighth = _UpsConfigHighVoltageTransferPointeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 10),
    _UpsConfigHighVoltageTransferPointeighth_Type()
)
upsConfigHighVoltageTransferPointeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointeighth.setUnits("RMS Volts")
_UpsConfigBatteryCapacityeighth_Type = NonNegativeInteger32
_UpsConfigBatteryCapacityeighth_Object = MibScalar
upsConfigBatteryCapacityeighth = _UpsConfigBatteryCapacityeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 11),
    _UpsConfigBatteryCapacityeighth_Type()
)
upsConfigBatteryCapacityeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacityeighth.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrenteighth_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrenteighth_Object = MibScalar
upsConfigBatteryChargeCurrenteighth = _UpsConfigBatteryChargeCurrenteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 12),
    _UpsConfigBatteryChargeCurrenteighth_Type()
)
upsConfigBatteryChargeCurrenteighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrenteighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrenteighth.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdowneighth_Type(Integer32):
    """Custom type upsConfigNoLoadShutdowneighth based on Integer32"""
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


_UpsConfigNoLoadShutdowneighth_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdowneighth_Object = MibScalar
upsConfigNoLoadShutdowneighth = _UpsConfigNoLoadShutdowneighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 13),
    _UpsConfigNoLoadShutdowneighth_Type()
)
upsConfigNoLoadShutdowneighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdowneighth.setStatus("current")
_UpsConfigStartDelayeighth_Type = PositiveInteger32
_UpsConfigStartDelayeighth_Object = MibScalar
upsConfigStartDelayeighth = _UpsConfigStartDelayeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 9, 14),
    _UpsConfigStartDelayeighth_Type()
)
upsConfigStartDelayeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelayeighth.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelayeighth.setUnits("minutes")
_UpsGetSeteighth_ObjectIdentity = ObjectIdentity
upsGetSeteighth = _UpsGetSeteighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10)
)
_UpsEventGetNexteighth_Type = PositiveInteger32
_UpsEventGetNexteighth_Object = MibScalar
upsEventGetNexteighth = _UpsEventGetNexteighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 1),
    _UpsEventGetNexteighth_Type()
)
upsEventGetNexteighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNexteighth.setStatus("current")
_UpsEventGetPreviouseighth_Type = PositiveInteger32
_UpsEventGetPreviouseighth_Object = MibScalar
upsEventGetPreviouseighth = _UpsEventGetPreviouseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 2),
    _UpsEventGetPreviouseighth_Type()
)
upsEventGetPreviouseighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPreviouseighth.setStatus("current")
_UpsEventSetStartingTimeStampeighth_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampeighth_Object = MibScalar
upsEventSetStartingTimeStampeighth = _UpsEventSetStartingTimeStampeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 3),
    _UpsEventSetStartingTimeStampeighth_Type()
)
upsEventSetStartingTimeStampeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampeighth.setStatus("current")
_UpsEventRetreiveCurrentTimeStampeighth_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampeighth_Object = MibScalar
upsEventRetreiveCurrentTimeStampeighth = _UpsEventRetreiveCurrentTimeStampeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 4),
    _UpsEventRetreiveCurrentTimeStampeighth_Type()
)
upsEventRetreiveCurrentTimeStampeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampeighth.setStatus("current")
_UpsEventTableSizeeighth_Type = NonNegativeInteger32
_UpsEventTableSizeeighth_Object = MibScalar
upsEventTableSizeeighth = _UpsEventTableSizeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 5),
    _UpsEventTableSizeeighth_Type()
)
upsEventTableSizeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizeeighth.setStatus("current")
_UpsEventEighthTable_Object = MibTable
upsEventEighthTable = _UpsEventEighthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventEighthTable.setStatus("current")
_UpsEventEighthEntry_Object = MibTableRow
upsEventEighthEntry = _UpsEventEighthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 6, 1)
)
upsEventEighthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsEventLineIndexeighth"),
)
if mibBuilder.loadTexts:
    upsEventEighthEntry.setStatus("current")
_UpsEventLineIndexeighth_Type = PositiveInteger32
_UpsEventLineIndexeighth_Object = MibTableColumn
upsEventLineIndexeighth = _UpsEventLineIndexeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 6, 1, 1),
    _UpsEventLineIndexeighth_Type()
)
upsEventLineIndexeighth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexeighth.setStatus("current")
_UpsEventCodeeighth_Type = Integer32
_UpsEventCodeeighth_Object = MibTableColumn
upsEventCodeeighth = _UpsEventCodeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 6, 1, 2),
    _UpsEventCodeeighth_Type()
)
upsEventCodeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodeeighth.setStatus("current")
_UpsEventStatuseighth_Type = NonNegativeInteger32
_UpsEventStatuseighth_Object = MibTableColumn
upsEventStatuseighth = _UpsEventStatuseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 6, 1, 3),
    _UpsEventStatuseighth_Type()
)
upsEventStatuseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatuseighth.setStatus("current")
_UpsEventTimeeighth_Type = NonNegativeInteger32
_UpsEventTimeeighth_Object = MibTableColumn
upsEventTimeeighth = _UpsEventTimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 6, 1, 4),
    _UpsEventTimeeighth_Type()
)
upsEventTimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimeeighth.setStatus("current")
_UpsParametersReadeighth_Type = PositiveInteger32
_UpsParametersReadeighth_Object = MibScalar
upsParametersReadeighth = _UpsParametersReadeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 7),
    _UpsParametersReadeighth_Type()
)
upsParametersReadeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadeighth.setStatus("current")
_UpsParametersWriteeighth_Type = PositiveInteger32
_UpsParametersWriteeighth_Object = MibScalar
upsParametersWriteeighth = _UpsParametersWriteeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 8),
    _UpsParametersWriteeighth_Type()
)
upsParametersWriteeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWriteeighth.setStatus("current")
_UpsParametersStartAddresseighth_Type = NonNegativeInteger32
_UpsParametersStartAddresseighth_Object = MibScalar
upsParametersStartAddresseighth = _UpsParametersStartAddresseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 9),
    _UpsParametersStartAddresseighth_Type()
)
upsParametersStartAddresseighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddresseighth.setStatus("current")
_UpsParameterTableSizeeighth_Type = NonNegativeInteger32
_UpsParameterTableSizeeighth_Object = MibScalar
upsParameterTableSizeeighth = _UpsParameterTableSizeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 10),
    _UpsParameterTableSizeeighth_Type()
)
upsParameterTableSizeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizeeighth.setStatus("current")
_UpsParameterEighthTable_Object = MibTable
upsParameterEighthTable = _UpsParameterEighthTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterEighthTable.setStatus("current")
_UpsParameterEighthEntry_Object = MibTableRow
upsParameterEighthEntry = _UpsParameterEighthEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 11, 1)
)
upsParameterEighthEntry.setIndexNames(
    (0, "GEPARALLELUPS-MIB", "upsParameterLineIndexeighth"),
)
if mibBuilder.loadTexts:
    upsParameterEighthEntry.setStatus("current")
_UpsParameterLineIndexeighth_Type = PositiveInteger32
_UpsParameterLineIndexeighth_Object = MibTableColumn
upsParameterLineIndexeighth = _UpsParameterLineIndexeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 11, 1, 1),
    _UpsParameterLineIndexeighth_Type()
)
upsParameterLineIndexeighth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexeighth.setStatus("current")
_UpsParameterValueeighth_Type = Integer32
_UpsParameterValueeighth_Object = MibTableColumn
upsParameterValueeighth = _UpsParameterValueeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 11, 1, 2),
    _UpsParameterValueeighth_Type()
)
upsParameterValueeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValueeighth.setStatus("current")
_UpsStatuseighth_Type = NonNegativeInteger32
_UpsStatuseighth_Object = MibScalar
upsStatuseighth = _UpsStatuseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 12),
    _UpsStatuseighth_Type()
)
upsStatuseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatuseighth.setStatus("current")
_UpsMainsStatisticsMBfaileighth_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfaileighth_Object = MibScalar
upsMainsStatisticsMBfaileighth = _UpsMainsStatisticsMBfaileighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 13),
    _UpsMainsStatisticsMBfaileighth_Type()
)
upsMainsStatisticsMBfaileighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfaileighth.setStatus("current")
_UpsMainsStatisticsMRfaileighth_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfaileighth_Object = MibScalar
upsMainsStatisticsMRfaileighth = _UpsMainsStatisticsMRfaileighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 14),
    _UpsMainsStatisticsMRfaileighth_Type()
)
upsMainsStatisticsMRfaileighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfaileighth.setStatus("current")
_UpsMainsStatisticsB2eighth_Type = NonNegativeInteger32
_UpsMainsStatisticsB2eighth_Object = MibScalar
upsMainsStatisticsB2eighth = _UpsMainsStatisticsB2eighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 15),
    _UpsMainsStatisticsB2eighth_Type()
)
upsMainsStatisticsB2eighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2eighth.setStatus("current")
_UpsMainsStatisticsB5eighth_Type = NonNegativeInteger32
_UpsMainsStatisticsB5eighth_Object = MibScalar
upsMainsStatisticsB5eighth = _UpsMainsStatisticsB5eighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 16),
    _UpsMainsStatisticsB5eighth_Type()
)
upsMainsStatisticsB5eighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5eighth.setStatus("current")
_UpsMainsStatisticsB10eighth_Type = NonNegativeInteger32
_UpsMainsStatisticsB10eighth_Object = MibScalar
upsMainsStatisticsB10eighth = _UpsMainsStatisticsB10eighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 17),
    _UpsMainsStatisticsB10eighth_Type()
)
upsMainsStatisticsB10eighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10eighth.setStatus("current")
_UpsMainsStatisticsB200eighth_Type = NonNegativeInteger32
_UpsMainsStatisticsB200eighth_Object = MibScalar
upsMainsStatisticsB200eighth = _UpsMainsStatisticsB200eighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 18),
    _UpsMainsStatisticsB200eighth_Type()
)
upsMainsStatisticsB200eighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200eighth.setStatus("current")
_UpsMainsStatisticsBypReleighth_Type = NonNegativeInteger32
_UpsMainsStatisticsBypReleighth_Object = MibScalar
upsMainsStatisticsBypReleighth = _UpsMainsStatisticsBypReleighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 19),
    _UpsMainsStatisticsBypReleighth_Type()
)
upsMainsStatisticsBypReleighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypReleighth.setStatus("current")
_UpsTimeeighth_Type = NonNegativeInteger32
_UpsTimeeighth_Object = MibScalar
upsTimeeighth = _UpsTimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 20),
    _UpsTimeeighth_Type()
)
upsTimeeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimeeighth.setStatus("current")
_UpsRequestPermissioneighth_Type = DisplayString
_UpsRequestPermissioneighth_Object = MibScalar
upsRequestPermissioneighth = _UpsRequestPermissioneighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 21),
    _UpsRequestPermissioneighth_Type()
)
upsRequestPermissioneighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissioneighth.setStatus("current")
_UpsEventGetCodeeighth_Type = Integer32
_UpsEventGetCodeeighth_Object = MibScalar
upsEventGetCodeeighth = _UpsEventGetCodeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 22),
    _UpsEventGetCodeeighth_Type()
)
upsEventGetCodeeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodeeighth.setStatus("current")
_UpsEventSpinLockeighth_Type = TestAndIncr
_UpsEventSpinLockeighth_Object = MibScalar
upsEventSpinLockeighth = _UpsEventSpinLockeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 23),
    _UpsEventSpinLockeighth_Type()
)
upsEventSpinLockeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLockeighth.setStatus("current")
_UpsParameterSpinLockeighth_Type = TestAndIncr
_UpsParameterSpinLockeighth_Object = MibScalar
upsParameterSpinLockeighth = _UpsParameterSpinLockeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 10, 24),
    _UpsParameterSpinLockeighth_Type()
)
upsParameterSpinLockeighth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLockeighth.setStatus("current")
_GeUPSTrapseighth_ObjectIdentity = ObjectIdentity
geUPSTrapseighth = _GeUPSTrapseighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11)
)
_UpsDiagnosticeighth_ObjectIdentity = ObjectIdentity
upsDiagnosticeighth = _UpsDiagnosticeighth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12)
)
_UpsDiagnosticBusJACommunicationStatuseighth_Type = Integer32
_UpsDiagnosticBusJACommunicationStatuseighth_Object = MibScalar
upsDiagnosticBusJACommunicationStatuseighth = _UpsDiagnosticBusJACommunicationStatuseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12, 1),
    _UpsDiagnosticBusJACommunicationStatuseighth_Type()
)
upsDiagnosticBusJACommunicationStatuseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatuseighth.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatuseighth_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatuseighth_Object = MibScalar
upsDiagnosticBusJBCommunicationStatuseighth = _UpsDiagnosticBusJBCommunicationStatuseighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatuseighth_Type()
)
upsDiagnosticBusJBCommunicationStatuseighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatuseighth.setStatus("current")
_UpsDiagnosticBatteryLifetimeeighth_Type = Integer32
_UpsDiagnosticBatteryLifetimeeighth_Object = MibScalar
upsDiagnosticBatteryLifetimeeighth = _UpsDiagnosticBatteryLifetimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12, 3),
    _UpsDiagnosticBatteryLifetimeeighth_Type()
)
upsDiagnosticBatteryLifetimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimeeighth.setStatus("current")
_UpsDiagnosticFansLifetimeeighth_Type = Integer32
_UpsDiagnosticFansLifetimeeighth_Object = MibScalar
upsDiagnosticFansLifetimeeighth = _UpsDiagnosticFansLifetimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12, 4),
    _UpsDiagnosticFansLifetimeeighth_Type()
)
upsDiagnosticFansLifetimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimeeighth.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimeeighth_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimeeighth_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimeeighth = _UpsDiagnosticDCcapacitorsLifetimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimeeighth_Type()
)
upsDiagnosticDCcapacitorsLifetimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimeeighth.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimeeighth_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimeeighth_Object = MibScalar
upsDiagnosticACcapacitorsLifetimeeighth = _UpsDiagnosticACcapacitorsLifetimeeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimeeighth_Type()
)
upsDiagnosticACcapacitorsLifetimeeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimeeighth.setStatus("current")
_UpsDiagnosticGlobalServiceCheckeighth_Type = Integer32
_UpsDiagnosticGlobalServiceCheckeighth_Object = MibScalar
upsDiagnosticGlobalServiceCheckeighth = _UpsDiagnosticGlobalServiceCheckeighth_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 12, 7),
    _UpsDiagnosticGlobalServiceCheckeighth_Type()
)
upsDiagnosticGlobalServiceCheckeighth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheckeighth.setStatus("current")
_GeDevices_ObjectIdentity = ObjectIdentity
geDevices = _GeDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100)
)
_GeDevicesDescriptions_ObjectIdentity = ObjectIdentity
geDevicesDescriptions = _GeDevicesDescriptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1)
)
_AdvSNMPWebIntCard_ObjectIdentity = ObjectIdentity
advSNMPWebIntCard = _AdvSNMPWebIntCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1, 1)
)
_SnmpWebIntCard_ObjectIdentity = ObjectIdentity
snmpWebIntCard = _SnmpWebIntCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1, 2)
)
_SnmpWebIntBox_ObjectIdentity = ObjectIdentity
snmpWebIntBox = _SnmpWebIntBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1, 3)
)

# Managed Objects groups


# Notification objects

upsTrapAlarmBatteryBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBad.setStatus(
        "current"
    )

upsTrapAlarmOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 2)
)
upsTrapAlarmOnBattery.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBattery")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBattery.setStatus(
        "current"
    )

upsTrapAlarmLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBattery.setStatus(
        "current"
    )

upsTrapAlarmDepletedBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBattery.setStatus(
        "current"
    )

upsTrapAlarmTempBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 5)
)
upsTrapAlarmTempBad.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBad.setStatus(
        "current"
    )

upsTrapAlarmInputBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBad.setStatus(
        "current"
    )

upsTrapAlarmOutputBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBad.setStatus(
        "current"
    )

upsTrapAlarmOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 8)
)
upsTrapAlarmOutputOverload.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLines"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoad"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverload.setStatus(
        "current"
    )

upsTrapAlarmOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypass.setStatus(
        "current"
    )

upsTrapAlarmBypassBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBad.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequested.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequested = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequested.setStatus(
        "current"
    )

upsTrapAlarmChargerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailed.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOff.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOff.setStatus(
        "current"
    )

upsTrapAlarmFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailure.setStatus(
        "current"
    )

upsTrapAlarmFuseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailure.setStatus(
        "current"
    )

upsTrapAlarmGeneralFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFault.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailed.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLost.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPower.setStatus(
        "current"
    )

upsTrapAlarmShutdownPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 22)
)
upsTrapAlarmShutdownPending.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelay")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPending.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminent = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminent.setStatus(
        "current"
    )

upsTrapAlarmTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 24)
)
upsTrapAlarmTestInProgress.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestId")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgress.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOff.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailure.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailure.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailure.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailure.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailure.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailure.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestored.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestored.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestored.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestored.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestored.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestored.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestored.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestored.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestored.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestored.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestored.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestored.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestored.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOn.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOn.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestored.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestored.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestored.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestored.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestored.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestored.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 54)
)
upsTrapAlarmShutdownPendingRestored.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelay")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestored.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestored.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 56)
)
upsTrapAlarmTestInProgressRestored.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestId")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestored.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOn.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestored.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestored.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestored.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestored.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestored.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestored.setStatus(
        "current"
    )

upsTrapAlarmValueLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLow.setStatus(
        "current"
    )

upsTrapAlarmValueHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHigh.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestored.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestored.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadfirst.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 2)
)
upsTrapAlarmOnBatteryfirst.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatteryfirst")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryfirst.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryfirst.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryfirst.setStatus(
        "current"
    )

upsTrapAlarmTempBadfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 5)
)
upsTrapAlarmTempBadfirst.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadfirst.setStatus(
        "current"
    )

upsTrapAlarmInputBadfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadfirst.setStatus(
        "current"
    )

upsTrapAlarmOutputBadfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadfirst.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 8)
)
upsTrapAlarmOutputOverloadfirst.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLinesfirst"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadfirst"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadfirst.setStatus(
        "current"
    )

upsTrapAlarmOnBypassfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassfirst.setStatus(
        "current"
    )

upsTrapAlarmBypassBadfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadfirst.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedfirst.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedfirst.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedfirst.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOfffirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOfffirst.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOfffirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOfffirst.setStatus(
        "current"
    )

upsTrapAlarmFanFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmFuseFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultfirst.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedfirst.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostfirst.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerfirst.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 22)
)
upsTrapAlarmShutdownPendingfirst.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayfirst")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingfirst.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentfirst.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 24)
)
upsTrapAlarmTestInProgressfirst.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdfirst")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressfirst.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOfffirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOfffirst.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailurefirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailurefirst.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOnfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOnfirst.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOnfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOnfirst.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredfirst.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayfirst")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 56)
)
upsTrapAlarmTestInProgressRestoredfirst.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdfirst")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOnfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOnfirst.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmValueLowfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowfirst.setStatus(
        "current"
    )

upsTrapAlarmValueHighfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighfirst.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredfirst = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 11, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredfirst.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadsecond.setStatus(
        "current"
    )

upsTrapAlarmOnBatterysecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 2)
)
upsTrapAlarmOnBatterysecond.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatterysecond")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatterysecond.setStatus(
        "current"
    )

upsTrapAlarmLowBatterysecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatterysecond.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatterysecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatterysecond.setStatus(
        "current"
    )

upsTrapAlarmTempBadsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 5)
)
upsTrapAlarmTempBadsecond.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadsecond.setStatus(
        "current"
    )

upsTrapAlarmInputBadsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadsecond.setStatus(
        "current"
    )

upsTrapAlarmOutputBadsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadsecond.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 8)
)
upsTrapAlarmOutputOverloadsecond.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLinessecond"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadsecond"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadsecond.setStatus(
        "current"
    )

upsTrapAlarmOnBypasssecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypasssecond.setStatus(
        "current"
    )

upsTrapAlarmBypassBadsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadsecond.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedsecond.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedsecond.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedsecond.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOffsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOffsecond.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOffsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOffsecond.setStatus(
        "current"
    )

upsTrapAlarmFanFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmFuseFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultsecond.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedsecond.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostsecond.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowersecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowersecond.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 22)
)
upsTrapAlarmShutdownPendingsecond.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelaysecond")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingsecond.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentsecond.setStatus(
        "current"
    )

upsTrapAlarmTestInProgresssecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 24)
)
upsTrapAlarmTestInProgresssecond.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdsecond")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgresssecond.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOffsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOffsecond.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailuresecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailuresecond.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOnsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOnsecond.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOnsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOnsecond.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredsecond.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelaysecond")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 56)
)
upsTrapAlarmTestInProgressRestoredsecond.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdsecond")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOnsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOnsecond.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmValueLowsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowsecond.setStatus(
        "current"
    )

upsTrapAlarmValueHighsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighsecond.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredsecond = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 12, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredsecond.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadthird.setStatus(
        "current"
    )

upsTrapAlarmOnBatterythird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 2)
)
upsTrapAlarmOnBatterythird.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatterythird")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatterythird.setStatus(
        "current"
    )

upsTrapAlarmLowBatterythird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatterythird.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatterythird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatterythird.setStatus(
        "current"
    )

upsTrapAlarmTempBadthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 5)
)
upsTrapAlarmTempBadthird.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadthird.setStatus(
        "current"
    )

upsTrapAlarmInputBadthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadthird.setStatus(
        "current"
    )

upsTrapAlarmOutputBadthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadthird.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 8)
)
upsTrapAlarmOutputOverloadthird.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLinesthird"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadthird"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadthird.setStatus(
        "current"
    )

upsTrapAlarmOnBypassthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassthird.setStatus(
        "current"
    )

upsTrapAlarmBypassBadthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadthird.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedthird.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedthird.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedthird.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOffthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOffthird.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOffthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOffthird.setStatus(
        "current"
    )

upsTrapAlarmFanFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailurethird.setStatus(
        "current"
    )

upsTrapAlarmFuseFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailurethird.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultthird.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedthird.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostthird.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerthird.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 22)
)
upsTrapAlarmShutdownPendingthird.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelaythird")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingthird.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentthird.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 24)
)
upsTrapAlarmTestInProgressthird.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdthird")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressthird.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOffthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOffthird.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailurethird.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailurethird.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailurethird.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailurethird.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailurethird.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailurethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailurethird.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOnthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOnthird.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOnthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOnthird.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredthird.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelaythird")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 56)
)
upsTrapAlarmTestInProgressRestoredthird.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdthird")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOnthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOnthird.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestorethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestorethird.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestorethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestorethird.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestorethird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestorethird.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmValueLowthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowthird.setStatus(
        "current"
    )

upsTrapAlarmValueHighthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighthird.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredthird = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 13, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredthird.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadfourth.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 2)
)
upsTrapAlarmOnBatteryfourth.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatteryfourth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryfourth.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryfourth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryfourth.setStatus(
        "current"
    )

upsTrapAlarmTempBadfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 5)
)
upsTrapAlarmTempBadfourth.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadfourth.setStatus(
        "current"
    )

upsTrapAlarmInputBadfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadfourth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadfourth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 8)
)
upsTrapAlarmOutputOverloadfourth.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLinesfourth"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadfourth"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadfourth.setStatus(
        "current"
    )

upsTrapAlarmOnBypassfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassfourth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadfourth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedfourth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedfourth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedfourth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOfffourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOfffourth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOfffourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOfffourth.setStatus(
        "current"
    )

upsTrapAlarmFanFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultfourth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedfourth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostfourth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerfourth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 22)
)
upsTrapAlarmShutdownPendingfourth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayfourth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingfourth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentfourth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 24)
)
upsTrapAlarmTestInProgressfourth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdfourth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressfourth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOfffourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOfffourth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailurefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailurefourth.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOnfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOnfourth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOnfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOnfourth.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredfourth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayfourth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 56)
)
upsTrapAlarmTestInProgressRestoredfourth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdfourth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOnfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOnfourth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestorefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestorefourth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestorefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestorefourth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestorefourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestorefourth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmValueLowfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowfourth.setStatus(
        "current"
    )

upsTrapAlarmValueHighfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighfourth.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredfourth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 14, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredfourth.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadfifth.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 2)
)
upsTrapAlarmOnBatteryfifth.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatteryfifth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryfifth.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryfifth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryfifth.setStatus(
        "current"
    )

upsTrapAlarmTempBadfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 5)
)
upsTrapAlarmTempBadfifth.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadfifth.setStatus(
        "current"
    )

upsTrapAlarmInputBadfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadfifth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadfifth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 8)
)
upsTrapAlarmOutputOverloadfifth.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLinesfifth"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadfifth"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadfifth.setStatus(
        "current"
    )

upsTrapAlarmOnBypassfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassfifth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadfifth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedfifth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedfifth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedfifth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOfffifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOfffifth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOfffifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOfffifth.setStatus(
        "current"
    )

upsTrapAlarmFanFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultfifth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedfifth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostfifth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerfifth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 22)
)
upsTrapAlarmShutdownPendingfifth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayfifth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingfifth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentfifth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 24)
)
upsTrapAlarmTestInProgressfifth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdfifth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressfifth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOfffifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOfffifth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailurefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailurefifth.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOnfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOnfifth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOnfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOnfifth.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredfifth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayfifth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 56)
)
upsTrapAlarmTestInProgressRestoredfifth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdfifth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOnfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOnfifth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestorefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestorefifth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestorefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestorefifth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestorefifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestorefifth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmValueLowfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowfifth.setStatus(
        "current"
    )

upsTrapAlarmValueHighfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighfifth.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredfifth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 15, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredfifth.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadsixth.setStatus(
        "current"
    )

upsTrapAlarmOnBatterysixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 2)
)
upsTrapAlarmOnBatterysixth.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatterysixth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatterysixth.setStatus(
        "current"
    )

upsTrapAlarmLowBatterysixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatterysixth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatterysixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatterysixth.setStatus(
        "current"
    )

upsTrapAlarmTempBadsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 5)
)
upsTrapAlarmTempBadsixth.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadsixth.setStatus(
        "current"
    )

upsTrapAlarmInputBadsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadsixth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadsixth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 8)
)
upsTrapAlarmOutputOverloadsixth.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLinessixth"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadsixth"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadsixth.setStatus(
        "current"
    )

upsTrapAlarmOnBypasssixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypasssixth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadsixth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedsixth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedsixth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedsixth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOffsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOffsixth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOffsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOffsixth.setStatus(
        "current"
    )

upsTrapAlarmFanFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultsixth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedsixth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostsixth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowersixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowersixth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 22)
)
upsTrapAlarmShutdownPendingsixth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelaysixth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingsixth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentsixth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgresssixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 24)
)
upsTrapAlarmTestInProgresssixth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdsixth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgresssixth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOffsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOffsixth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailuresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailuresixth.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOnsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOnsixth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOnsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOnsixth.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredsixth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelaysixth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 56)
)
upsTrapAlarmTestInProgressRestoredsixth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdsixth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOnsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOnsixth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestoresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestoresixth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestoresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestoresixth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestoresixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestoresixth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmValueLowsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowsixth.setStatus(
        "current"
    )

upsTrapAlarmValueHighsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighsixth.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredsixth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 16, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredsixth.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadseventh.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 2)
)
upsTrapAlarmOnBatteryseventh.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatteryseventh")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryseventh.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryseventh.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryseventh.setStatus(
        "current"
    )

upsTrapAlarmTempBadseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 5)
)
upsTrapAlarmTempBadseventh.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadseventh.setStatus(
        "current"
    )

upsTrapAlarmInputBadseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadseventh.setStatus(
        "current"
    )

upsTrapAlarmOutputBadseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadseventh.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 8)
)
upsTrapAlarmOutputOverloadseventh.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLinesseventh"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadseventh"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadseventh.setStatus(
        "current"
    )

upsTrapAlarmOnBypassseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassseventh.setStatus(
        "current"
    )

upsTrapAlarmBypassBadseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadseventh.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedseventh.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedseventh.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedseventh.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOffseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOffseventh.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOffseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOffseventh.setStatus(
        "current"
    )

upsTrapAlarmFanFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultseventh.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedseventh.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostseventh.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerseventh.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 22)
)
upsTrapAlarmShutdownPendingseventh.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayseventh")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingseventh.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentseventh.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 24)
)
upsTrapAlarmTestInProgressseventh.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdseventh")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressseventh.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOffseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOffseventh.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailureseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailureseventh.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOnseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOnseventh.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOnseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOnseventh.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredseventh.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayseventh")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 56)
)
upsTrapAlarmTestInProgressRestoredseventh.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdseventh")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOnseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOnseventh.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestoreseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestoreseventh.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestoreseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestoreseventh.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestoreseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestoreseventh.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmValueLowseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowseventh.setStatus(
        "current"
    )

upsTrapAlarmValueHighseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighseventh.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredseventh = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 17, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredseventh.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadeighth.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 2)
)
upsTrapAlarmOnBatteryeighth.setObjects(
    ("GEPARALLELUPS-MIB", "upsSecondsOnBatteryeighth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryeighth.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryeighth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryeighth.setStatus(
        "current"
    )

upsTrapAlarmTempBadeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 5)
)
upsTrapAlarmTempBadeighth.setObjects(
    ("GEPARALLELUPS-MIB", "upsBatteryTemperature")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadeighth.setStatus(
        "current"
    )

upsTrapAlarmInputBadeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadeighth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadeighth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 8)
)
upsTrapAlarmOutputOverloadeighth.setObjects(
      *(("GEPARALLELUPS-MIB", "upsOutputNumLineseighth"),
        ("GEPARALLELUPS-MIB", "upsOutputPercentLoadeighth"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadeighth.setStatus(
        "current"
    )

upsTrapAlarmOnBypasseighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypasseighth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadeighth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedeighth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedeighth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedeighth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOffeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOffeighth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOffeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOffeighth.setStatus(
        "current"
    )

upsTrapAlarmFanFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaulteighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaulteighth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedeighth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLosteighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLosteighth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowereighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowereighth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 22)
)
upsTrapAlarmShutdownPendingeighth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayeighth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingeighth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminenteighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminenteighth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgresseighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 24)
)
upsTrapAlarmTestInProgresseighth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdeighth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgresseighth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOffeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOffeighth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailureeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailureeighth.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOneighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOneighth.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOneighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOneighth.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredeighth.setObjects(
    ("GEPARALLELUPS-MIB", "upsShutdownAfterDelayeighth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 56)
)
upsTrapAlarmTestInProgressRestoredeighth.setObjects(
    ("GEPARALLELUPS-MIB", "upsTestIdeighth")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOneighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOneighth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestoreeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestoreeighth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestoreeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestoreeighth.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestoreeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestoreeighth.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmValueLoweighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLoweighth.setStatus(
        "current"
    )

upsTrapAlarmValueHigheighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHigheighth.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredeighth.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredeighth = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 18, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredeighth.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEPARALLELUPS-MIB",
    **{"PositiveInteger32": PositiveInteger32,
       "NonNegativeInteger32": NonNegativeInteger32,
       "imv": imv,
       "geHardware": geHardware,
       "geUPS": geUPS,
       "geDiscoveredUPSsMask": geDiscoveredUPSsMask,
       "geRequestPacket": geRequestPacket,
       "geReplyPacket": geReplyPacket,
       "geGenericUPS": geGenericUPS,
       "upsIdent": upsIdent,
       "upsIdentManufacturer": upsIdentManufacturer,
       "upsIdentModel": upsIdentModel,
       "upsIdentUPSSoftwareVersion": upsIdentUPSSoftwareVersion,
       "upsIdentAgentSoftwareVersion": upsIdentAgentSoftwareVersion,
       "upsIdentName": upsIdentName,
       "upsIdentAttachedDevices": upsIdentAttachedDevices,
       "upsIdentUPSSerialNumber": upsIdentUPSSerialNumber,
       "upsIdentComProtVersion": upsIdentComProtVersion,
       "upsIdentOperatingTime": upsIdentOperatingTime,
       "upsBattery": upsBattery,
       "upsBatteryStatus": upsBatteryStatus,
       "upsSecondsOnBattery": upsSecondsOnBattery,
       "upsEstimatedMinutesRemaining": upsEstimatedMinutesRemaining,
       "upsEstimatedChargeRemaining": upsEstimatedChargeRemaining,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryCurrent": upsBatteryCurrent,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsBatteryRipple": upsBatteryRipple,
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
       "upsInputVoltageMin": upsInputVoltageMin,
       "upsInputVoltageMax": upsInputVoltageMax,
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
       "upsOutputPowerFactor": upsOutputPowerFactor,
       "upsOutputPeakCurrent": upsOutputPeakCurrent,
       "upsOutputShareCurrent": upsOutputShareCurrent,
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
       "upsAlarmReceptacleOff": upsAlarmReceptacleOff,
       "upsAlarmHighSpeedBusFailure": upsAlarmHighSpeedBusFailure,
       "upsAlarmHighSpeedBusJACRCFailure": upsAlarmHighSpeedBusJACRCFailure,
       "upsAlarmConnectivityBusFailure": upsAlarmConnectivityBusFailure,
       "upsAlarmHighSpeedBusJBCRCFailure": upsAlarmHighSpeedBusJBCRCFailure,
       "upsAlarmCurrentSharing": upsAlarmCurrentSharing,
       "upsAlarmDCRipple": upsAlarmDCRipple,
       "upsAlarmMaskA": upsAlarmMaskA,
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
       "upsReceptaclesNum": upsReceptaclesNum,
       "upsReceptacleTable": upsReceptacleTable,
       "upsReceptacleEntry": upsReceptacleEntry,
       "upsReceptacleLineIndex": upsReceptacleLineIndex,
       "upsReceptacleOnOff": upsReceptacleOnOff,
       "upsUPSMode": upsUPSMode,
       "upsRectifierOnOff": upsRectifierOnOff,
       "upsBatteryChargeMethod": upsBatteryChargeMethod,
       "upsInverterOnOff": upsInverterOnOff,
       "upsBypassOnOff": upsBypassOnOff,
       "upsLoadSource": upsLoadSource,
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
       "upsConfigBatteryCapacity": upsConfigBatteryCapacity,
       "upsConfigBatteryChargeCurrent": upsConfigBatteryChargeCurrent,
       "upsConfigNoLoadShutdown": upsConfigNoLoadShutdown,
       "upsConfigStartDelay": upsConfigStartDelay,
       "upsGetSet": upsGetSet,
       "upsEventGetNext": upsEventGetNext,
       "upsEventGetPrevious": upsEventGetPrevious,
       "upsEventSetStartingTimeStamp": upsEventSetStartingTimeStamp,
       "upsEventRetreiveCurrentTimeStamp": upsEventRetreiveCurrentTimeStamp,
       "upsEventTableSize": upsEventTableSize,
       "upsEventTable": upsEventTable,
       "upsEventEntry": upsEventEntry,
       "upsEventLineIndex": upsEventLineIndex,
       "upsEventCode": upsEventCode,
       "upsEventStatus": upsEventStatus,
       "upsEventTime": upsEventTime,
       "upsParametersRead": upsParametersRead,
       "upsParametersWrite": upsParametersWrite,
       "upsParametersStartAddress": upsParametersStartAddress,
       "upsParameterTableSize": upsParameterTableSize,
       "upsParameterTable": upsParameterTable,
       "upsParameterEntry": upsParameterEntry,
       "upsParameterLineIndex": upsParameterLineIndex,
       "upsParameterValue": upsParameterValue,
       "upsStatus": upsStatus,
       "upsMainsStatisticsMBfail": upsMainsStatisticsMBfail,
       "upsMainsStatisticsMRfail": upsMainsStatisticsMRfail,
       "upsMainsStatisticsB2": upsMainsStatisticsB2,
       "upsMainsStatisticsB5": upsMainsStatisticsB5,
       "upsMainsStatisticsB10": upsMainsStatisticsB10,
       "upsMainsStatisticsB200": upsMainsStatisticsB200,
       "upsMainsStatisticsBypRel": upsMainsStatisticsBypRel,
       "upsTimegen": upsTimegen,
       "upsRequestPermission": upsRequestPermission,
       "upsEventGetCode": upsEventGetCode,
       "upsEventSpinLock": upsEventSpinLock,
       "upsParameterSpinLock": upsParameterSpinLock,
       "geUPSTraps": geUPSTraps,
       "upsTrapAlarmBatteryBad": upsTrapAlarmBatteryBad,
       "upsTrapAlarmOnBattery": upsTrapAlarmOnBattery,
       "upsTrapAlarmLowBattery": upsTrapAlarmLowBattery,
       "upsTrapAlarmDepletedBattery": upsTrapAlarmDepletedBattery,
       "upsTrapAlarmTempBad": upsTrapAlarmTempBad,
       "upsTrapAlarmInputBad": upsTrapAlarmInputBad,
       "upsTrapAlarmOutputBad": upsTrapAlarmOutputBad,
       "upsTrapAlarmOutputOverload": upsTrapAlarmOutputOverload,
       "upsTrapAlarmOnBypass": upsTrapAlarmOnBypass,
       "upsTrapAlarmBypassBad": upsTrapAlarmBypassBad,
       "upsTrapAlarmOutputOffAsRequested": upsTrapAlarmOutputOffAsRequested,
       "upsTrapAlarmUpsOffAsRequested": upsTrapAlarmUpsOffAsRequested,
       "upsTrapAlarmChargerFailed": upsTrapAlarmChargerFailed,
       "upsTrapAlarmUpsOutputOff": upsTrapAlarmUpsOutputOff,
       "upsTrapAlarmUpsSystemOff": upsTrapAlarmUpsSystemOff,
       "upsTrapAlarmFanFailure": upsTrapAlarmFanFailure,
       "upsTrapAlarmFuseFailure": upsTrapAlarmFuseFailure,
       "upsTrapAlarmGeneralFault": upsTrapAlarmGeneralFault,
       "upsTrapAlarmDiagnosticTestFailed": upsTrapAlarmDiagnosticTestFailed,
       "upsTrapAlarmCommunicationsLost": upsTrapAlarmCommunicationsLost,
       "upsTrapAlarmAwaitingPower": upsTrapAlarmAwaitingPower,
       "upsTrapAlarmShutdownPending": upsTrapAlarmShutdownPending,
       "upsTrapAlarmShutdownImminent": upsTrapAlarmShutdownImminent,
       "upsTrapAlarmTestInProgress": upsTrapAlarmTestInProgress,
       "upsTrapAlarmReceptacleOff": upsTrapAlarmReceptacleOff,
       "upsTrapAlarmHighspeedBusFailure": upsTrapAlarmHighspeedBusFailure,
       "upsTrapAlarmHighspeedBusJACRCFailure": upsTrapAlarmHighspeedBusJACRCFailure,
       "upsTrapAlarmConnectivityBusFailure": upsTrapAlarmConnectivityBusFailure,
       "upsTrapAlarmHighspeedBusJBCRCFailure": upsTrapAlarmHighspeedBusJBCRCFailure,
       "upsTrapAlarmCurrentSharingFailure": upsTrapAlarmCurrentSharingFailure,
       "upsTrapAlarmDCRippleFailure": upsTrapAlarmDCRippleFailure,
       "upsTrapAlarmBatteryBadRestored": upsTrapAlarmBatteryBadRestored,
       "upsTrapAlarmOnBatteryRestored": upsTrapAlarmOnBatteryRestored,
       "upsTrapAlarmLowBatteryRestored": upsTrapAlarmLowBatteryRestored,
       "upsTrapAlarmDepletedBatteryRestored": upsTrapAlarmDepletedBatteryRestored,
       "upsTrapAlarmTempBadRestored": upsTrapAlarmTempBadRestored,
       "upsTrapAlarmInputBadRestored": upsTrapAlarmInputBadRestored,
       "upsTrapAlarmOutputBadRestored": upsTrapAlarmOutputBadRestored,
       "upsTrapAlarmOutputOverloadRestored": upsTrapAlarmOutputOverloadRestored,
       "upsTrapAlarmOnBypassRestored": upsTrapAlarmOnBypassRestored,
       "upsTrapAlarmBypassBadRestored": upsTrapAlarmBypassBadRestored,
       "upsTrapAlarmOutputOffAsRequestedRestored": upsTrapAlarmOutputOffAsRequestedRestored,
       "upsTrapAlarmUpsOffAsRequestedRestored": upsTrapAlarmUpsOffAsRequestedRestored,
       "upsTrapAlarmChargerFailedRestored": upsTrapAlarmChargerFailedRestored,
       "upsTrapAlarmUpsOutputOn": upsTrapAlarmUpsOutputOn,
       "upsTrapAlarmUpsSystemOn": upsTrapAlarmUpsSystemOn,
       "upsTrapAlarmFanFailureRestored": upsTrapAlarmFanFailureRestored,
       "upsTrapAlarmFuseFailureRestored": upsTrapAlarmFuseFailureRestored,
       "upsTrapAlarmGeneralFaultRestored": upsTrapAlarmGeneralFaultRestored,
       "upsTrapAlarmDiagnosticTestFailedRestored": upsTrapAlarmDiagnosticTestFailedRestored,
       "upsTrapAlarmCommunicationsLostRestored": upsTrapAlarmCommunicationsLostRestored,
       "upsTrapAlarmAwaitingPowerRestored": upsTrapAlarmAwaitingPowerRestored,
       "upsTrapAlarmShutdownPendingRestored": upsTrapAlarmShutdownPendingRestored,
       "upsTrapAlarmShutdownImminentRestored": upsTrapAlarmShutdownImminentRestored,
       "upsTrapAlarmTestInProgressRestored": upsTrapAlarmTestInProgressRestored,
       "upsTrapAlarmReceptacleOn": upsTrapAlarmReceptacleOn,
       "upsTrapAlarmHighspeedBusRestored": upsTrapAlarmHighspeedBusRestored,
       "upsTrapAlarmHighspeedBusJACRCRestored": upsTrapAlarmHighspeedBusJACRCRestored,
       "upsTrapAlarmConnectivityBusRestored": upsTrapAlarmConnectivityBusRestored,
       "upsTrapAlarmHighspeedBusJBCRCRestored": upsTrapAlarmHighspeedBusJBCRCRestored,
       "upsTrapAlarmCurrentSharingRestored": upsTrapAlarmCurrentSharingRestored,
       "upsTrapAlarmDCRippleRestored": upsTrapAlarmDCRippleRestored,
       "upsTrapAlarmValueLow": upsTrapAlarmValueLow,
       "upsTrapAlarmValueHigh": upsTrapAlarmValueHigh,
       "upsTrapAlarmValueLowRestored": upsTrapAlarmValueLowRestored,
       "upsTrapAlarmValueHighRestored": upsTrapAlarmValueHighRestored,
       "upsDiagnostic": upsDiagnostic,
       "upsDiagnosticBusJACommunicationStatus": upsDiagnosticBusJACommunicationStatus,
       "upsDiagnosticBusJBCommunicationStatus": upsDiagnosticBusJBCommunicationStatus,
       "upsDiagnosticBatteryLifetime": upsDiagnosticBatteryLifetime,
       "upsDiagnosticFansLifetime": upsDiagnosticFansLifetime,
       "upsDiagnosticDCcapacitorsLifetime": upsDiagnosticDCcapacitorsLifetime,
       "upsDiagnosticACcapacitorsLifetime": upsDiagnosticACcapacitorsLifetime,
       "upsDiagnosticGlobalServiceCheck": upsDiagnosticGlobalServiceCheck,
       "geFirstUPS": geFirstUPS,
       "upsIdentfirst": upsIdentfirst,
       "upsIdentManufacturerfirst": upsIdentManufacturerfirst,
       "upsIdentModelfirst": upsIdentModelfirst,
       "upsIdentUPSSoftwareVersionfirst": upsIdentUPSSoftwareVersionfirst,
       "upsIdentAgentSoftwareVersionfirst": upsIdentAgentSoftwareVersionfirst,
       "upsIdentNamefirst": upsIdentNamefirst,
       "upsIdentAttachedDevicesfirst": upsIdentAttachedDevicesfirst,
       "upsIdentUPSSerialNumberfirst": upsIdentUPSSerialNumberfirst,
       "upsIdentComProtVersionfirst": upsIdentComProtVersionfirst,
       "upsIdentOperatingTimefirst": upsIdentOperatingTimefirst,
       "upsBatteryfirst": upsBatteryfirst,
       "upsBatteryStatusfirst": upsBatteryStatusfirst,
       "upsSecondsOnBatteryfirst": upsSecondsOnBatteryfirst,
       "upsEstimatedMinutesRemainingfirst": upsEstimatedMinutesRemainingfirst,
       "upsEstimatedChargeRemainingfirst": upsEstimatedChargeRemainingfirst,
       "upsBatteryVoltagefirst": upsBatteryVoltagefirst,
       "upsBatteryCurrentfirst": upsBatteryCurrentfirst,
       "upsBatteryTemperaturefirst": upsBatteryTemperaturefirst,
       "upsBatteryRipplefirst": upsBatteryRipplefirst,
       "upsInputfirst": upsInputfirst,
       "upsInputLineBadsfirst": upsInputLineBadsfirst,
       "upsInputNumLinesfirst": upsInputNumLinesfirst,
       "upsInputFirstTable": upsInputFirstTable,
       "upsInputFirstEntry": upsInputFirstEntry,
       "upsInputLineIndexfirst": upsInputLineIndexfirst,
       "upsInputFrequencyfirst": upsInputFrequencyfirst,
       "upsInputVoltagefirst": upsInputVoltagefirst,
       "upsInputCurrentfirst": upsInputCurrentfirst,
       "upsInputTruePowerfirst": upsInputTruePowerfirst,
       "upsInputVoltageMinfirst": upsInputVoltageMinfirst,
       "upsInputVoltageMaxfirst": upsInputVoltageMaxfirst,
       "upsOutputfirst": upsOutputfirst,
       "upsOutputSourcefirst": upsOutputSourcefirst,
       "upsOutputFrequencyfirst": upsOutputFrequencyfirst,
       "upsOutputNumLinesfirst": upsOutputNumLinesfirst,
       "upsOutputFirstTable": upsOutputFirstTable,
       "upsOutputFirstEntry": upsOutputFirstEntry,
       "upsOutputLineIndexfirst": upsOutputLineIndexfirst,
       "upsOutputVoltagefirst": upsOutputVoltagefirst,
       "upsOutputCurrentfirst": upsOutputCurrentfirst,
       "upsOutputPowerfirst": upsOutputPowerfirst,
       "upsOutputPercentLoadfirst": upsOutputPercentLoadfirst,
       "upsOutputPowerFactorfirst": upsOutputPowerFactorfirst,
       "upsOutputPeakCurrentfirst": upsOutputPeakCurrentfirst,
       "upsOutputShareCurrentfirst": upsOutputShareCurrentfirst,
       "upsBypassfirst": upsBypassfirst,
       "upsBypassFrequencyfirst": upsBypassFrequencyfirst,
       "upsBypassNumLinesfirst": upsBypassNumLinesfirst,
       "upsBypassFirstTable": upsBypassFirstTable,
       "upsBypassFirstEntry": upsBypassFirstEntry,
       "upsBypassLineIndexfirst": upsBypassLineIndexfirst,
       "upsBypassVoltagefirst": upsBypassVoltagefirst,
       "upsBypassCurrentfirst": upsBypassCurrentfirst,
       "upsBypassPowerfirst": upsBypassPowerfirst,
       "upsAlarmfirst": upsAlarmfirst,
       "upsAlarmsPresentfirst": upsAlarmsPresentfirst,
       "upsAlarmFirstTable": upsAlarmFirstTable,
       "upsAlarmFirstEntry": upsAlarmFirstEntry,
       "upsAlarmIdfirst": upsAlarmIdfirst,
       "upsAlarmDescrfirst": upsAlarmDescrfirst,
       "upsAlarmTimefirst": upsAlarmTimefirst,
       "upsWellKnownAlarmsfirst": upsWellKnownAlarmsfirst,
       "upsAlarmBatteryBadfirst": upsAlarmBatteryBadfirst,
       "upsAlarmOnBatteryfirst": upsAlarmOnBatteryfirst,
       "upsAlarmLowBatteryfirst": upsAlarmLowBatteryfirst,
       "upsAlarmDepletedBatteryfirst": upsAlarmDepletedBatteryfirst,
       "upsAlarmTempBadfirst": upsAlarmTempBadfirst,
       "upsAlarmInputBadfirst": upsAlarmInputBadfirst,
       "upsAlarmOutputBadfirst": upsAlarmOutputBadfirst,
       "upsAlarmOutputOverloadfirst": upsAlarmOutputOverloadfirst,
       "upsAlarmOnBypassfirst": upsAlarmOnBypassfirst,
       "upsAlarmBypassBadfirst": upsAlarmBypassBadfirst,
       "upsAlarmOutputOffAsRequestedfirst": upsAlarmOutputOffAsRequestedfirst,
       "upsAlarmUpsOffAsRequestedfirst": upsAlarmUpsOffAsRequestedfirst,
       "upsAlarmChargerFailedfirst": upsAlarmChargerFailedfirst,
       "upsAlarmUpsOutputOfffirst": upsAlarmUpsOutputOfffirst,
       "upsAlarmUpsSystemOfffirst": upsAlarmUpsSystemOfffirst,
       "upsAlarmFanFailurefirst": upsAlarmFanFailurefirst,
       "upsAlarmFuseFailurefirst": upsAlarmFuseFailurefirst,
       "upsAlarmGeneralFaultfirst": upsAlarmGeneralFaultfirst,
       "upsAlarmDiagnosticTestFailedfirst": upsAlarmDiagnosticTestFailedfirst,
       "upsAlarmCommunicationsLostfirst": upsAlarmCommunicationsLostfirst,
       "upsAlarmAwaitingPowerfirst": upsAlarmAwaitingPowerfirst,
       "upsAlarmShutdownPendingfirst": upsAlarmShutdownPendingfirst,
       "upsAlarmShutdownImminentfirst": upsAlarmShutdownImminentfirst,
       "upsAlarmTestInProgressfirst": upsAlarmTestInProgressfirst,
       "upsAlarmReceptacleOfffirst": upsAlarmReceptacleOfffirst,
       "upsAlarmHighSpeedBusFailurefirst": upsAlarmHighSpeedBusFailurefirst,
       "upsAlarmHighSpeedBusJACRCFailurefirst": upsAlarmHighSpeedBusJACRCFailurefirst,
       "upsAlarmConnectivityBusFailurefirst": upsAlarmConnectivityBusFailurefirst,
       "upsAlarmHighSpeedBusJBCRCFailurefirst": upsAlarmHighSpeedBusJBCRCFailurefirst,
       "upsAlarmCurrentSharingfirst": upsAlarmCurrentSharingfirst,
       "upsAlarmDCRipplefirst": upsAlarmDCRipplefirst,
       "upsAlarmMaskAfirst": upsAlarmMaskAfirst,
       "upsTestfirst": upsTestfirst,
       "upsTestIdfirst": upsTestIdfirst,
       "upsTestSpinLockfirst": upsTestSpinLockfirst,
       "upsTestResultsSummaryfirst": upsTestResultsSummaryfirst,
       "upsTestResultsDetailfirst": upsTestResultsDetailfirst,
       "upsTestStartTimefirst": upsTestStartTimefirst,
       "upsTestElapsedTimefirst": upsTestElapsedTimefirst,
       "upsWellKnownTestsfirst": upsWellKnownTestsfirst,
       "upsTestNoTestsInitiatedfirst": upsTestNoTestsInitiatedfirst,
       "upsTestAbortTestInProgressfirst": upsTestAbortTestInProgressfirst,
       "upsTestGeneralSystemsTestfirst": upsTestGeneralSystemsTestfirst,
       "upsTestQuickBatteryTestfirst": upsTestQuickBatteryTestfirst,
       "upsTestDeepBatteryCalibrationfirst": upsTestDeepBatteryCalibrationfirst,
       "upsControlfirst": upsControlfirst,
       "upsShutdownTypefirst": upsShutdownTypefirst,
       "upsShutdownAfterDelayfirst": upsShutdownAfterDelayfirst,
       "upsStartupAfterDelayfirst": upsStartupAfterDelayfirst,
       "upsRebootWithDurationfirst": upsRebootWithDurationfirst,
       "upsAutoRestartfirst": upsAutoRestartfirst,
       "upsReceptaclesNumfirst": upsReceptaclesNumfirst,
       "upsReceptacleFirstTable": upsReceptacleFirstTable,
       "upsReceptacleFirstEntry": upsReceptacleFirstEntry,
       "upsReceptacleLineIndexfirst": upsReceptacleLineIndexfirst,
       "upsReceptacleOnOfffirst": upsReceptacleOnOfffirst,
       "upsUPSModefirst": upsUPSModefirst,
       "upsRectifierOnOfffirst": upsRectifierOnOfffirst,
       "upsBatteryChargeMethodfirst": upsBatteryChargeMethodfirst,
       "upsInverterOnOfffirst": upsInverterOnOfffirst,
       "upsBypassOnOfffirst": upsBypassOnOfffirst,
       "upsLoadSourcefirst": upsLoadSourcefirst,
       "upsConfigfirst": upsConfigfirst,
       "upsConfigInputVoltagefirst": upsConfigInputVoltagefirst,
       "upsConfigInputFreqfirst": upsConfigInputFreqfirst,
       "upsConfigOutputVoltagefirst": upsConfigOutputVoltagefirst,
       "upsConfigOutputFreqfirst": upsConfigOutputFreqfirst,
       "upsConfigOutputVAfirst": upsConfigOutputVAfirst,
       "upsConfigOutputPowerfirst": upsConfigOutputPowerfirst,
       "upsConfigLowBattTimefirst": upsConfigLowBattTimefirst,
       "upsConfigAudibleStatusfirst": upsConfigAudibleStatusfirst,
       "upsConfigLowVoltageTransferPointfirst": upsConfigLowVoltageTransferPointfirst,
       "upsConfigHighVoltageTransferPointfirst": upsConfigHighVoltageTransferPointfirst,
       "upsConfigBatteryCapacityfirst": upsConfigBatteryCapacityfirst,
       "upsConfigBatteryChargeCurrentfirst": upsConfigBatteryChargeCurrentfirst,
       "upsConfigNoLoadShutdownfirst": upsConfigNoLoadShutdownfirst,
       "upsConfigStartDelayfirst": upsConfigStartDelayfirst,
       "upsGetSetfirst": upsGetSetfirst,
       "upsEventGetNextfirst": upsEventGetNextfirst,
       "upsEventGetPreviousfirst": upsEventGetPreviousfirst,
       "upsEventSetStartingTimeStampfirst": upsEventSetStartingTimeStampfirst,
       "upsEventRetreiveCurrentTimeStampfirst": upsEventRetreiveCurrentTimeStampfirst,
       "upsEventTableSizefirst": upsEventTableSizefirst,
       "upsEventFirstTable": upsEventFirstTable,
       "upsEventFirstEntry": upsEventFirstEntry,
       "upsEventLineIndexfirst": upsEventLineIndexfirst,
       "upsEventCodefirst": upsEventCodefirst,
       "upsEventStatusfirst": upsEventStatusfirst,
       "upsEventTimefirst": upsEventTimefirst,
       "upsParametersReadfirst": upsParametersReadfirst,
       "upsParametersWritefirst": upsParametersWritefirst,
       "upsParametersStartAddressfirst": upsParametersStartAddressfirst,
       "upsParameterTableSizefirst": upsParameterTableSizefirst,
       "upsParameterFirstTable": upsParameterFirstTable,
       "upsParameterFirstEntry": upsParameterFirstEntry,
       "upsParameterLineIndexfirst": upsParameterLineIndexfirst,
       "upsParameterValuefirst": upsParameterValuefirst,
       "upsStatusfirst": upsStatusfirst,
       "upsMainsStatisticsMBfailfirst": upsMainsStatisticsMBfailfirst,
       "upsMainsStatisticsMRfailfirst": upsMainsStatisticsMRfailfirst,
       "upsMainsStatisticsB2first": upsMainsStatisticsB2first,
       "upsMainsStatisticsB5first": upsMainsStatisticsB5first,
       "upsMainsStatisticsB10first": upsMainsStatisticsB10first,
       "upsMainsStatisticsB200first": upsMainsStatisticsB200first,
       "upsMainsStatisticsBypRelfirst": upsMainsStatisticsBypRelfirst,
       "upsTimefirst": upsTimefirst,
       "upsRequestPermissionfirst": upsRequestPermissionfirst,
       "upsEventGetCodefirst": upsEventGetCodefirst,
       "upsEventSpinLockfirst": upsEventSpinLockfirst,
       "upsParameterSpinLockfirst": upsParameterSpinLockfirst,
       "geUPSTrapsfirst": geUPSTrapsfirst,
       "upsTrapAlarmBatteryBadfirst": upsTrapAlarmBatteryBadfirst,
       "upsTrapAlarmOnBatteryfirst": upsTrapAlarmOnBatteryfirst,
       "upsTrapAlarmLowBatteryfirst": upsTrapAlarmLowBatteryfirst,
       "upsTrapAlarmDepletedBatteryfirst": upsTrapAlarmDepletedBatteryfirst,
       "upsTrapAlarmTempBadfirst": upsTrapAlarmTempBadfirst,
       "upsTrapAlarmInputBadfirst": upsTrapAlarmInputBadfirst,
       "upsTrapAlarmOutputBadfirst": upsTrapAlarmOutputBadfirst,
       "upsTrapAlarmOutputOverloadfirst": upsTrapAlarmOutputOverloadfirst,
       "upsTrapAlarmOnBypassfirst": upsTrapAlarmOnBypassfirst,
       "upsTrapAlarmBypassBadfirst": upsTrapAlarmBypassBadfirst,
       "upsTrapAlarmOutputOffAsRequestedfirst": upsTrapAlarmOutputOffAsRequestedfirst,
       "upsTrapAlarmUpsOffAsRequestedfirst": upsTrapAlarmUpsOffAsRequestedfirst,
       "upsTrapAlarmChargerFailedfirst": upsTrapAlarmChargerFailedfirst,
       "upsTrapAlarmUpsOutputOfffirst": upsTrapAlarmUpsOutputOfffirst,
       "upsTrapAlarmUpsSystemOfffirst": upsTrapAlarmUpsSystemOfffirst,
       "upsTrapAlarmFanFailurefirst": upsTrapAlarmFanFailurefirst,
       "upsTrapAlarmFuseFailurefirst": upsTrapAlarmFuseFailurefirst,
       "upsTrapAlarmGeneralFaultfirst": upsTrapAlarmGeneralFaultfirst,
       "upsTrapAlarmDiagnosticTestFailedfirst": upsTrapAlarmDiagnosticTestFailedfirst,
       "upsTrapAlarmCommunicationsLostfirst": upsTrapAlarmCommunicationsLostfirst,
       "upsTrapAlarmAwaitingPowerfirst": upsTrapAlarmAwaitingPowerfirst,
       "upsTrapAlarmShutdownPendingfirst": upsTrapAlarmShutdownPendingfirst,
       "upsTrapAlarmShutdownImminentfirst": upsTrapAlarmShutdownImminentfirst,
       "upsTrapAlarmTestInProgressfirst": upsTrapAlarmTestInProgressfirst,
       "upsTrapAlarmReceptacleOfffirst": upsTrapAlarmReceptacleOfffirst,
       "upsTrapAlarmHighspeedBusFailurefirst": upsTrapAlarmHighspeedBusFailurefirst,
       "upsTrapAlarmHighspeedBusJACRCFailurefirst": upsTrapAlarmHighspeedBusJACRCFailurefirst,
       "upsTrapAlarmConnectivityBusFailurefirst": upsTrapAlarmConnectivityBusFailurefirst,
       "upsTrapAlarmHighspeedBusJBCRCFailurefirst": upsTrapAlarmHighspeedBusJBCRCFailurefirst,
       "upsTrapAlarmCurrentSharingFailurefirst": upsTrapAlarmCurrentSharingFailurefirst,
       "upsTrapAlarmDCRippleFailurefirst": upsTrapAlarmDCRippleFailurefirst,
       "upsTrapAlarmBatteryBadRestoredfirst": upsTrapAlarmBatteryBadRestoredfirst,
       "upsTrapAlarmOnBatteryRestoredfirst": upsTrapAlarmOnBatteryRestoredfirst,
       "upsTrapAlarmLowBatteryRestoredfirst": upsTrapAlarmLowBatteryRestoredfirst,
       "upsTrapAlarmDepletedBatteryRestoredfirst": upsTrapAlarmDepletedBatteryRestoredfirst,
       "upsTrapAlarmTempBadRestoredfirst": upsTrapAlarmTempBadRestoredfirst,
       "upsTrapAlarmInputBadRestoredfirst": upsTrapAlarmInputBadRestoredfirst,
       "upsTrapAlarmOutputBadRestoredfirst": upsTrapAlarmOutputBadRestoredfirst,
       "upsTrapAlarmOutputOverloadRestoredfirst": upsTrapAlarmOutputOverloadRestoredfirst,
       "upsTrapAlarmOnBypassRestoredfirst": upsTrapAlarmOnBypassRestoredfirst,
       "upsTrapAlarmBypassBadRestoredfirst": upsTrapAlarmBypassBadRestoredfirst,
       "upsTrapAlarmOutputOffAsRequestedRestoredfirst": upsTrapAlarmOutputOffAsRequestedRestoredfirst,
       "upsTrapAlarmUpsOffAsRequestedRestoredfirst": upsTrapAlarmUpsOffAsRequestedRestoredfirst,
       "upsTrapAlarmChargerFailedRestoredfirst": upsTrapAlarmChargerFailedRestoredfirst,
       "upsTrapAlarmUpsOutputOnfirst": upsTrapAlarmUpsOutputOnfirst,
       "upsTrapAlarmUpsSystemOnfirst": upsTrapAlarmUpsSystemOnfirst,
       "upsTrapAlarmFanFailureRestoredfirst": upsTrapAlarmFanFailureRestoredfirst,
       "upsTrapAlarmFuseFailureRestoredfirst": upsTrapAlarmFuseFailureRestoredfirst,
       "upsTrapAlarmGeneralFaultRestoredfirst": upsTrapAlarmGeneralFaultRestoredfirst,
       "upsTrapAlarmDiagnosticTestFailedRestoredfirst": upsTrapAlarmDiagnosticTestFailedRestoredfirst,
       "upsTrapAlarmCommunicationsLostRestoredfirst": upsTrapAlarmCommunicationsLostRestoredfirst,
       "upsTrapAlarmAwaitingPowerRestoredfirst": upsTrapAlarmAwaitingPowerRestoredfirst,
       "upsTrapAlarmShutdownPendingRestoredfirst": upsTrapAlarmShutdownPendingRestoredfirst,
       "upsTrapAlarmShutdownImminentRestoredfirst": upsTrapAlarmShutdownImminentRestoredfirst,
       "upsTrapAlarmTestInProgressRestoredfirst": upsTrapAlarmTestInProgressRestoredfirst,
       "upsTrapAlarmReceptacleOnfirst": upsTrapAlarmReceptacleOnfirst,
       "upsTrapAlarmHighspeedBusRestoredfirst": upsTrapAlarmHighspeedBusRestoredfirst,
       "upsTrapAlarmHighspeedBusJACRCRestoredfirst": upsTrapAlarmHighspeedBusJACRCRestoredfirst,
       "upsTrapAlarmConnectivityBusRestoredfirst": upsTrapAlarmConnectivityBusRestoredfirst,
       "upsTrapAlarmHighspeedBusJBCRCRestoredfirst": upsTrapAlarmHighspeedBusJBCRCRestoredfirst,
       "upsTrapAlarmCurrentSharingRestoredfirst": upsTrapAlarmCurrentSharingRestoredfirst,
       "upsTrapAlarmDCRippleRestoredfirst": upsTrapAlarmDCRippleRestoredfirst,
       "upsTrapAlarmValueLowfirst": upsTrapAlarmValueLowfirst,
       "upsTrapAlarmValueHighfirst": upsTrapAlarmValueHighfirst,
       "upsTrapAlarmValueLowRestoredfirst": upsTrapAlarmValueLowRestoredfirst,
       "upsTrapAlarmValueHighRestoredfirst": upsTrapAlarmValueHighRestoredfirst,
       "upsDiagnosticfirst": upsDiagnosticfirst,
       "upsDiagnosticBusJACommunicationStatusfirst": upsDiagnosticBusJACommunicationStatusfirst,
       "upsDiagnosticBusJBCommunicationStatusfirst": upsDiagnosticBusJBCommunicationStatusfirst,
       "upsDiagnosticBatteryLifetimefirst": upsDiagnosticBatteryLifetimefirst,
       "upsDiagnosticFansLifetimefirst": upsDiagnosticFansLifetimefirst,
       "upsDiagnosticDCcapacitorsLifetimefirst": upsDiagnosticDCcapacitorsLifetimefirst,
       "upsDiagnosticACcapacitorsLifetimefirst": upsDiagnosticACcapacitorsLifetimefirst,
       "upsDiagnosticGlobalServiceCheckfirst": upsDiagnosticGlobalServiceCheckfirst,
       "geSecondUPS": geSecondUPS,
       "upsIdentsecond": upsIdentsecond,
       "upsIdentManufacturersecond": upsIdentManufacturersecond,
       "upsIdentModelsecond": upsIdentModelsecond,
       "upsIdentUPSSoftwareVersionsecond": upsIdentUPSSoftwareVersionsecond,
       "upsIdentAgentSoftwareVersionsecond": upsIdentAgentSoftwareVersionsecond,
       "upsIdentNamesecond": upsIdentNamesecond,
       "upsIdentAttachedDevicessecond": upsIdentAttachedDevicessecond,
       "upsIdentUPSSerialNumbersecond": upsIdentUPSSerialNumbersecond,
       "upsIdentComProtVersionsecond": upsIdentComProtVersionsecond,
       "upsIdentOperatingTimesecond": upsIdentOperatingTimesecond,
       "upsBatterysecond": upsBatterysecond,
       "upsBatteryStatussecond": upsBatteryStatussecond,
       "upsSecondsOnBatterysecond": upsSecondsOnBatterysecond,
       "upsEstimatedMinutesRemainingsecond": upsEstimatedMinutesRemainingsecond,
       "upsEstimatedChargeRemainingsecond": upsEstimatedChargeRemainingsecond,
       "upsBatteryVoltagesecond": upsBatteryVoltagesecond,
       "upsBatteryCurrentsecond": upsBatteryCurrentsecond,
       "upsBatteryTemperaturesecond": upsBatteryTemperaturesecond,
       "upsBatteryRipplesecond": upsBatteryRipplesecond,
       "upsInputsecond": upsInputsecond,
       "upsInputLineBadssecond": upsInputLineBadssecond,
       "upsInputNumLinessecond": upsInputNumLinessecond,
       "upsInputSecondTable": upsInputSecondTable,
       "upsInputSecondEntry": upsInputSecondEntry,
       "upsInputLineIndexsecond": upsInputLineIndexsecond,
       "upsInputFrequencysecond": upsInputFrequencysecond,
       "upsInputVoltagesecond": upsInputVoltagesecond,
       "upsInputCurrentsecond": upsInputCurrentsecond,
       "upsInputTruePowersecond": upsInputTruePowersecond,
       "upsInputVoltageMinsecond": upsInputVoltageMinsecond,
       "upsInputVoltageMaxsecond": upsInputVoltageMaxsecond,
       "upsOutputsecond": upsOutputsecond,
       "upsOutputSourcesecond": upsOutputSourcesecond,
       "upsOutputFrequencysecond": upsOutputFrequencysecond,
       "upsOutputNumLinessecond": upsOutputNumLinessecond,
       "upsOutputSecondTable": upsOutputSecondTable,
       "upsOutputSecondEntry": upsOutputSecondEntry,
       "upsOutputLineIndexsecond": upsOutputLineIndexsecond,
       "upsOutputVoltagesecond": upsOutputVoltagesecond,
       "upsOutputCurrentsecond": upsOutputCurrentsecond,
       "upsOutputPowersecond": upsOutputPowersecond,
       "upsOutputPercentLoadsecond": upsOutputPercentLoadsecond,
       "upsOutputPowerFactorsecond": upsOutputPowerFactorsecond,
       "upsOutputPeakCurrentsecond": upsOutputPeakCurrentsecond,
       "upsOutputShareCurrentsecond": upsOutputShareCurrentsecond,
       "upsBypasssecond": upsBypasssecond,
       "upsBypassFrequencysecond": upsBypassFrequencysecond,
       "upsBypassNumLinessecond": upsBypassNumLinessecond,
       "upsBypassSecondTable": upsBypassSecondTable,
       "upsBypassSecondEntry": upsBypassSecondEntry,
       "upsBypassLineIndexsecond": upsBypassLineIndexsecond,
       "upsBypassVoltagesecond": upsBypassVoltagesecond,
       "upsBypassCurrentsecond": upsBypassCurrentsecond,
       "upsBypassPowersecond": upsBypassPowersecond,
       "upsAlarmsecond": upsAlarmsecond,
       "upsAlarmsPresentsecond": upsAlarmsPresentsecond,
       "upsAlarmSecondTable": upsAlarmSecondTable,
       "upsAlarmSecondEntry": upsAlarmSecondEntry,
       "upsAlarmIdsecond": upsAlarmIdsecond,
       "upsAlarmDescrsecond": upsAlarmDescrsecond,
       "upsAlarmTimesecond": upsAlarmTimesecond,
       "upsWellKnownAlarmssecond": upsWellKnownAlarmssecond,
       "upsAlarmBatteryBadsecond": upsAlarmBatteryBadsecond,
       "upsAlarmOnBatterysecond": upsAlarmOnBatterysecond,
       "upsAlarmLowBatterysecond": upsAlarmLowBatterysecond,
       "upsAlarmDepletedBatterysecond": upsAlarmDepletedBatterysecond,
       "upsAlarmTempBadsecond": upsAlarmTempBadsecond,
       "upsAlarmInputBadsecond": upsAlarmInputBadsecond,
       "upsAlarmOutputBadsecond": upsAlarmOutputBadsecond,
       "upsAlarmOutputOverloadsecond": upsAlarmOutputOverloadsecond,
       "upsAlarmOnBypasssecond": upsAlarmOnBypasssecond,
       "upsAlarmBypassBadsecond": upsAlarmBypassBadsecond,
       "upsAlarmOutputOffAsRequestedsecond": upsAlarmOutputOffAsRequestedsecond,
       "upsAlarmUpsOffAsRequestedsecond": upsAlarmUpsOffAsRequestedsecond,
       "upsAlarmChargerFailedsecond": upsAlarmChargerFailedsecond,
       "upsAlarmUpsOutputOffsecond": upsAlarmUpsOutputOffsecond,
       "upsAlarmUpsSystemOffsecond": upsAlarmUpsSystemOffsecond,
       "upsAlarmFanFailuresecond": upsAlarmFanFailuresecond,
       "upsAlarmFuseFailuresecond": upsAlarmFuseFailuresecond,
       "upsAlarmGeneralFaultsecond": upsAlarmGeneralFaultsecond,
       "upsAlarmDiagnosticTestFailedsecond": upsAlarmDiagnosticTestFailedsecond,
       "upsAlarmCommunicationsLostsecond": upsAlarmCommunicationsLostsecond,
       "upsAlarmAwaitingPowersecond": upsAlarmAwaitingPowersecond,
       "upsAlarmShutdownPendingsecond": upsAlarmShutdownPendingsecond,
       "upsAlarmShutdownImminentsecond": upsAlarmShutdownImminentsecond,
       "upsAlarmTestInProgresssecond": upsAlarmTestInProgresssecond,
       "upsAlarmReceptacleOffsecond": upsAlarmReceptacleOffsecond,
       "upsAlarmHighSpeedBusFailuresecond": upsAlarmHighSpeedBusFailuresecond,
       "upsAlarmHighSpeedBusJACRCFailuresecond": upsAlarmHighSpeedBusJACRCFailuresecond,
       "upsAlarmConnectivityBusFailuresecond": upsAlarmConnectivityBusFailuresecond,
       "upsAlarmHighSpeedBusJBCRCFailuresecond": upsAlarmHighSpeedBusJBCRCFailuresecond,
       "upsAlarmCurrentSharingsecond": upsAlarmCurrentSharingsecond,
       "upsAlarmDCRipplesecond": upsAlarmDCRipplesecond,
       "upsAlarmMaskAsecond": upsAlarmMaskAsecond,
       "upsTestsecond": upsTestsecond,
       "upsTestIdsecond": upsTestIdsecond,
       "upsTestSpinLocksecond": upsTestSpinLocksecond,
       "upsTestResultsSummarysecond": upsTestResultsSummarysecond,
       "upsTestResultsDetailsecond": upsTestResultsDetailsecond,
       "upsTestStartTimesecond": upsTestStartTimesecond,
       "upsTestElapsedTimesecond": upsTestElapsedTimesecond,
       "upsWellKnownTestssecond": upsWellKnownTestssecond,
       "upsTestNoTestsInitiatedsecond": upsTestNoTestsInitiatedsecond,
       "upsTestAbortTestInProgresssecond": upsTestAbortTestInProgresssecond,
       "upsTestGeneralSystemsTestsecond": upsTestGeneralSystemsTestsecond,
       "upsTestQuickBatteryTestsecond": upsTestQuickBatteryTestsecond,
       "upsTestDeepBatteryCalibrationsecond": upsTestDeepBatteryCalibrationsecond,
       "upsControlsecond": upsControlsecond,
       "upsShutdownTypesecond": upsShutdownTypesecond,
       "upsShutdownAfterDelaysecond": upsShutdownAfterDelaysecond,
       "upsStartupAfterDelaysecond": upsStartupAfterDelaysecond,
       "upsRebootWithDurationsecond": upsRebootWithDurationsecond,
       "upsAutoRestartsecond": upsAutoRestartsecond,
       "upsReceptaclesNumsecond": upsReceptaclesNumsecond,
       "upsReceptacleSecondTable": upsReceptacleSecondTable,
       "upsReceptacleSecondEntry": upsReceptacleSecondEntry,
       "upsReceptacleLineIndexsecond": upsReceptacleLineIndexsecond,
       "upsReceptacleOnOffsecond": upsReceptacleOnOffsecond,
       "upsUPSModesecond": upsUPSModesecond,
       "upsRectifierOnOffsecond": upsRectifierOnOffsecond,
       "upsBatteryChargeMethodsecond": upsBatteryChargeMethodsecond,
       "upsInverterOnOffsecond": upsInverterOnOffsecond,
       "upsBypassOnOffsecond": upsBypassOnOffsecond,
       "upsLoadSourcesecond": upsLoadSourcesecond,
       "upsConfigsecond": upsConfigsecond,
       "upsConfigInputVoltagesecond": upsConfigInputVoltagesecond,
       "upsConfigInputFreqsecond": upsConfigInputFreqsecond,
       "upsConfigOutputVoltagesecond": upsConfigOutputVoltagesecond,
       "upsConfigOutputFreqsecond": upsConfigOutputFreqsecond,
       "upsConfigOutputVAsecond": upsConfigOutputVAsecond,
       "upsConfigOutputPowersecond": upsConfigOutputPowersecond,
       "upsConfigLowBattTimesecond": upsConfigLowBattTimesecond,
       "upsConfigAudibleStatussecond": upsConfigAudibleStatussecond,
       "upsConfigLowVoltageTransferPointsecond": upsConfigLowVoltageTransferPointsecond,
       "upsConfigHighVoltageTransferPointsecond": upsConfigHighVoltageTransferPointsecond,
       "upsConfigBatteryCapacitysecond": upsConfigBatteryCapacitysecond,
       "upsConfigBatteryChargeCurrentsecond": upsConfigBatteryChargeCurrentsecond,
       "upsConfigNoLoadShutdownsecond": upsConfigNoLoadShutdownsecond,
       "upsConfigStartDelaysecond": upsConfigStartDelaysecond,
       "upsGetSetsecond": upsGetSetsecond,
       "upsEventGetNextsecond": upsEventGetNextsecond,
       "upsEventGetPrevioussecond": upsEventGetPrevioussecond,
       "upsEventSetStartingTimeStampsecond": upsEventSetStartingTimeStampsecond,
       "upsEventRetreiveCurrentTimeStampsecond": upsEventRetreiveCurrentTimeStampsecond,
       "upsEventTableSizesecond": upsEventTableSizesecond,
       "upsEventSecondTable": upsEventSecondTable,
       "upsEventSecondEntry": upsEventSecondEntry,
       "upsEventLineIndexsecond": upsEventLineIndexsecond,
       "upsEventCodesecond": upsEventCodesecond,
       "upsEventStatussecond": upsEventStatussecond,
       "upsEventTimesecond": upsEventTimesecond,
       "upsParametersReadsecond": upsParametersReadsecond,
       "upsParametersWritesecond": upsParametersWritesecond,
       "upsParametersStartAddresssecond": upsParametersStartAddresssecond,
       "upsParameterTableSizesecond": upsParameterTableSizesecond,
       "upsParameterSecondTable": upsParameterSecondTable,
       "upsParameterSecondEntry": upsParameterSecondEntry,
       "upsParameterLineIndexsecond": upsParameterLineIndexsecond,
       "upsParameterValuesecond": upsParameterValuesecond,
       "upsStatussecond": upsStatussecond,
       "upsMainsStatisticsMBfailsecond": upsMainsStatisticsMBfailsecond,
       "upsMainsStatisticsMRfailsecond": upsMainsStatisticsMRfailsecond,
       "upsMainsStatisticsB2second": upsMainsStatisticsB2second,
       "upsMainsStatisticsB5second": upsMainsStatisticsB5second,
       "upsMainsStatisticsB10second": upsMainsStatisticsB10second,
       "upsMainsStatisticsB200second": upsMainsStatisticsB200second,
       "upsMainsStatisticsBypRelsecond": upsMainsStatisticsBypRelsecond,
       "upsTimesecond": upsTimesecond,
       "upsRequestPermissionsecond": upsRequestPermissionsecond,
       "upsEventGetCodesecond": upsEventGetCodesecond,
       "upsEventSpinLocksecond": upsEventSpinLocksecond,
       "upsParameterSpinLocksecond": upsParameterSpinLocksecond,
       "geUPSTrapssecond": geUPSTrapssecond,
       "upsTrapAlarmBatteryBadsecond": upsTrapAlarmBatteryBadsecond,
       "upsTrapAlarmOnBatterysecond": upsTrapAlarmOnBatterysecond,
       "upsTrapAlarmLowBatterysecond": upsTrapAlarmLowBatterysecond,
       "upsTrapAlarmDepletedBatterysecond": upsTrapAlarmDepletedBatterysecond,
       "upsTrapAlarmTempBadsecond": upsTrapAlarmTempBadsecond,
       "upsTrapAlarmInputBadsecond": upsTrapAlarmInputBadsecond,
       "upsTrapAlarmOutputBadsecond": upsTrapAlarmOutputBadsecond,
       "upsTrapAlarmOutputOverloadsecond": upsTrapAlarmOutputOverloadsecond,
       "upsTrapAlarmOnBypasssecond": upsTrapAlarmOnBypasssecond,
       "upsTrapAlarmBypassBadsecond": upsTrapAlarmBypassBadsecond,
       "upsTrapAlarmOutputOffAsRequestedsecond": upsTrapAlarmOutputOffAsRequestedsecond,
       "upsTrapAlarmUpsOffAsRequestedsecond": upsTrapAlarmUpsOffAsRequestedsecond,
       "upsTrapAlarmChargerFailedsecond": upsTrapAlarmChargerFailedsecond,
       "upsTrapAlarmUpsOutputOffsecond": upsTrapAlarmUpsOutputOffsecond,
       "upsTrapAlarmUpsSystemOffsecond": upsTrapAlarmUpsSystemOffsecond,
       "upsTrapAlarmFanFailuresecond": upsTrapAlarmFanFailuresecond,
       "upsTrapAlarmFuseFailuresecond": upsTrapAlarmFuseFailuresecond,
       "upsTrapAlarmGeneralFaultsecond": upsTrapAlarmGeneralFaultsecond,
       "upsTrapAlarmDiagnosticTestFailedsecond": upsTrapAlarmDiagnosticTestFailedsecond,
       "upsTrapAlarmCommunicationsLostsecond": upsTrapAlarmCommunicationsLostsecond,
       "upsTrapAlarmAwaitingPowersecond": upsTrapAlarmAwaitingPowersecond,
       "upsTrapAlarmShutdownPendingsecond": upsTrapAlarmShutdownPendingsecond,
       "upsTrapAlarmShutdownImminentsecond": upsTrapAlarmShutdownImminentsecond,
       "upsTrapAlarmTestInProgresssecond": upsTrapAlarmTestInProgresssecond,
       "upsTrapAlarmReceptacleOffsecond": upsTrapAlarmReceptacleOffsecond,
       "upsTrapAlarmHighspeedBusFailuresecond": upsTrapAlarmHighspeedBusFailuresecond,
       "upsTrapAlarmHighspeedBusJACRCFailuresecond": upsTrapAlarmHighspeedBusJACRCFailuresecond,
       "upsTrapAlarmConnectivityBusFailuresecond": upsTrapAlarmConnectivityBusFailuresecond,
       "upsTrapAlarmHighspeedBusJBCRCFailuresecond": upsTrapAlarmHighspeedBusJBCRCFailuresecond,
       "upsTrapAlarmCurrentSharingFailuresecond": upsTrapAlarmCurrentSharingFailuresecond,
       "upsTrapAlarmDCRippleFailuresecond": upsTrapAlarmDCRippleFailuresecond,
       "upsTrapAlarmBatteryBadRestoredsecond": upsTrapAlarmBatteryBadRestoredsecond,
       "upsTrapAlarmOnBatteryRestoredsecond": upsTrapAlarmOnBatteryRestoredsecond,
       "upsTrapAlarmLowBatteryRestoredsecond": upsTrapAlarmLowBatteryRestoredsecond,
       "upsTrapAlarmDepletedBatteryRestoredsecond": upsTrapAlarmDepletedBatteryRestoredsecond,
       "upsTrapAlarmTempBadRestoredsecond": upsTrapAlarmTempBadRestoredsecond,
       "upsTrapAlarmInputBadRestoredsecond": upsTrapAlarmInputBadRestoredsecond,
       "upsTrapAlarmOutputBadRestoredsecond": upsTrapAlarmOutputBadRestoredsecond,
       "upsTrapAlarmOutputOverloadRestoredsecond": upsTrapAlarmOutputOverloadRestoredsecond,
       "upsTrapAlarmOnBypassRestoredsecond": upsTrapAlarmOnBypassRestoredsecond,
       "upsTrapAlarmBypassBadRestoredsecond": upsTrapAlarmBypassBadRestoredsecond,
       "upsTrapAlarmOutputOffAsRequestedRestoredsecond": upsTrapAlarmOutputOffAsRequestedRestoredsecond,
       "upsTrapAlarmUpsOffAsRequestedRestoredsecond": upsTrapAlarmUpsOffAsRequestedRestoredsecond,
       "upsTrapAlarmChargerFailedRestoredsecond": upsTrapAlarmChargerFailedRestoredsecond,
       "upsTrapAlarmUpsOutputOnsecond": upsTrapAlarmUpsOutputOnsecond,
       "upsTrapAlarmUpsSystemOnsecond": upsTrapAlarmUpsSystemOnsecond,
       "upsTrapAlarmFanFailureRestoredsecond": upsTrapAlarmFanFailureRestoredsecond,
       "upsTrapAlarmFuseFailureRestoredsecond": upsTrapAlarmFuseFailureRestoredsecond,
       "upsTrapAlarmGeneralFaultRestoredsecond": upsTrapAlarmGeneralFaultRestoredsecond,
       "upsTrapAlarmDiagnosticTestFailedRestoredsecond": upsTrapAlarmDiagnosticTestFailedRestoredsecond,
       "upsTrapAlarmCommunicationsLostRestoredsecond": upsTrapAlarmCommunicationsLostRestoredsecond,
       "upsTrapAlarmAwaitingPowerRestoredsecond": upsTrapAlarmAwaitingPowerRestoredsecond,
       "upsTrapAlarmShutdownPendingRestoredsecond": upsTrapAlarmShutdownPendingRestoredsecond,
       "upsTrapAlarmShutdownImminentRestoredsecond": upsTrapAlarmShutdownImminentRestoredsecond,
       "upsTrapAlarmTestInProgressRestoredsecond": upsTrapAlarmTestInProgressRestoredsecond,
       "upsTrapAlarmReceptacleOnsecond": upsTrapAlarmReceptacleOnsecond,
       "upsTrapAlarmHighspeedBusRestoredsecond": upsTrapAlarmHighspeedBusRestoredsecond,
       "upsTrapAlarmHighspeedBusJACRCRestoredsecond": upsTrapAlarmHighspeedBusJACRCRestoredsecond,
       "upsTrapAlarmConnectivityBusRestoredsecond": upsTrapAlarmConnectivityBusRestoredsecond,
       "upsTrapAlarmHighspeedBusJBCRCRestoredsecond": upsTrapAlarmHighspeedBusJBCRCRestoredsecond,
       "upsTrapAlarmCurrentSharingRestoredsecond": upsTrapAlarmCurrentSharingRestoredsecond,
       "upsTrapAlarmDCRippleRestoredsecond": upsTrapAlarmDCRippleRestoredsecond,
       "upsTrapAlarmValueLowsecond": upsTrapAlarmValueLowsecond,
       "upsTrapAlarmValueHighsecond": upsTrapAlarmValueHighsecond,
       "upsTrapAlarmValueLowRestoredsecond": upsTrapAlarmValueLowRestoredsecond,
       "upsTrapAlarmValueHighRestoredsecond": upsTrapAlarmValueHighRestoredsecond,
       "upsDiagnosticsecond": upsDiagnosticsecond,
       "upsDiagnosticBusJACommunicationStatussecond": upsDiagnosticBusJACommunicationStatussecond,
       "upsDiagnosticBusJBCommunicationStatussecond": upsDiagnosticBusJBCommunicationStatussecond,
       "upsDiagnosticBatteryLifetimesecond": upsDiagnosticBatteryLifetimesecond,
       "upsDiagnosticFansLifetimesecond": upsDiagnosticFansLifetimesecond,
       "upsDiagnosticDCcapacitorsLifetimesecond": upsDiagnosticDCcapacitorsLifetimesecond,
       "upsDiagnosticACcapacitorsLifetimesecond": upsDiagnosticACcapacitorsLifetimesecond,
       "upsDiagnosticGlobalServiceChecksecond": upsDiagnosticGlobalServiceChecksecond,
       "geThirdUPS": geThirdUPS,
       "upsIdentthird": upsIdentthird,
       "upsIdentManufacturerthird": upsIdentManufacturerthird,
       "upsIdentModelthird": upsIdentModelthird,
       "upsIdentUPSSoftwareVersionthird": upsIdentUPSSoftwareVersionthird,
       "upsIdentAgentSoftwareVersionthird": upsIdentAgentSoftwareVersionthird,
       "upsIdentNamethird": upsIdentNamethird,
       "upsIdentAttachedDevicesthird": upsIdentAttachedDevicesthird,
       "upsIdentUPSSerialNumberthird": upsIdentUPSSerialNumberthird,
       "upsIdentComProtVersionthird": upsIdentComProtVersionthird,
       "upsIdentOperatingTimethird": upsIdentOperatingTimethird,
       "upsBatterythird": upsBatterythird,
       "upsBatteryStatusthird": upsBatteryStatusthird,
       "upsSecondsOnBatterythird": upsSecondsOnBatterythird,
       "upsEstimatedMinutesRemainingthird": upsEstimatedMinutesRemainingthird,
       "upsEstimatedChargeRemainingthird": upsEstimatedChargeRemainingthird,
       "upsBatteryVoltagethird": upsBatteryVoltagethird,
       "upsBatteryCurrentthird": upsBatteryCurrentthird,
       "upsBatteryTemperaturethird": upsBatteryTemperaturethird,
       "upsBatteryRipplethird": upsBatteryRipplethird,
       "upsInputthird": upsInputthird,
       "upsInputLineBadsthird": upsInputLineBadsthird,
       "upsInputNumLinesthird": upsInputNumLinesthird,
       "upsInputThirdTable": upsInputThirdTable,
       "upsInputThirdEntry": upsInputThirdEntry,
       "upsInputLineIndexthird": upsInputLineIndexthird,
       "upsInputFrequencythird": upsInputFrequencythird,
       "upsInputVoltagethird": upsInputVoltagethird,
       "upsInputCurrentthird": upsInputCurrentthird,
       "upsInputTruePowerthird": upsInputTruePowerthird,
       "upsInputVoltageMinthird": upsInputVoltageMinthird,
       "upsInputVoltageMaxthird": upsInputVoltageMaxthird,
       "upsOutputthird": upsOutputthird,
       "upsOutputSourcethird": upsOutputSourcethird,
       "upsOutputFrequencythird": upsOutputFrequencythird,
       "upsOutputNumLinesthird": upsOutputNumLinesthird,
       "upsOutputThirdTable": upsOutputThirdTable,
       "upsOutputThirdEntry": upsOutputThirdEntry,
       "upsOutputLineIndexthird": upsOutputLineIndexthird,
       "upsOutputVoltagethird": upsOutputVoltagethird,
       "upsOutputCurrentthird": upsOutputCurrentthird,
       "upsOutputPowerthird": upsOutputPowerthird,
       "upsOutputPercentLoadthird": upsOutputPercentLoadthird,
       "upsOutputPowerFactorthird": upsOutputPowerFactorthird,
       "upsOutputPeakCurrentthird": upsOutputPeakCurrentthird,
       "upsOutputShareCurrentthird": upsOutputShareCurrentthird,
       "upsBypassthird": upsBypassthird,
       "upsBypassFrequencythird": upsBypassFrequencythird,
       "upsBypassNumLinesthird": upsBypassNumLinesthird,
       "upsBypassThirdTable": upsBypassThirdTable,
       "upsBypassThirdEntry": upsBypassThirdEntry,
       "upsBypassLineIndexthird": upsBypassLineIndexthird,
       "upsBypassVoltagethird": upsBypassVoltagethird,
       "upsBypassCurrentthird": upsBypassCurrentthird,
       "upsBypassPowerthird": upsBypassPowerthird,
       "upsAlarmthird": upsAlarmthird,
       "upsAlarmsPresentthird": upsAlarmsPresentthird,
       "upsAlarmThirdTable": upsAlarmThirdTable,
       "upsAlarmThirdEntry": upsAlarmThirdEntry,
       "upsAlarmIdthird": upsAlarmIdthird,
       "upsAlarmDescrthird": upsAlarmDescrthird,
       "upsAlarmTimethird": upsAlarmTimethird,
       "upsWellKnownAlarmsthird": upsWellKnownAlarmsthird,
       "upsAlarmBatteryBadthird": upsAlarmBatteryBadthird,
       "upsAlarmOnBatterythird": upsAlarmOnBatterythird,
       "upsAlarmLowBatterythird": upsAlarmLowBatterythird,
       "upsAlarmDepletedBatterythird": upsAlarmDepletedBatterythird,
       "upsAlarmTempBadthird": upsAlarmTempBadthird,
       "upsAlarmInputBadthird": upsAlarmInputBadthird,
       "upsAlarmOutputBadthird": upsAlarmOutputBadthird,
       "upsAlarmOutputOverloadthird": upsAlarmOutputOverloadthird,
       "upsAlarmOnBypassthird": upsAlarmOnBypassthird,
       "upsAlarmBypassBadthird": upsAlarmBypassBadthird,
       "upsAlarmOutputOffAsRequestedthird": upsAlarmOutputOffAsRequestedthird,
       "upsAlarmUpsOffAsRequestedthird": upsAlarmUpsOffAsRequestedthird,
       "upsAlarmChargerFailedthird": upsAlarmChargerFailedthird,
       "upsAlarmUpsOutputOffthird": upsAlarmUpsOutputOffthird,
       "upsAlarmUpsSystemOffthird": upsAlarmUpsSystemOffthird,
       "upsAlarmFanFailurethird": upsAlarmFanFailurethird,
       "upsAlarmFuseFailurethird": upsAlarmFuseFailurethird,
       "upsAlarmGeneralFaultthird": upsAlarmGeneralFaultthird,
       "upsAlarmDiagnosticTestFailedthird": upsAlarmDiagnosticTestFailedthird,
       "upsAlarmCommunicationsLostthird": upsAlarmCommunicationsLostthird,
       "upsAlarmAwaitingPowerthird": upsAlarmAwaitingPowerthird,
       "upsAlarmShutdownPendingthird": upsAlarmShutdownPendingthird,
       "upsAlarmShutdownImminentthird": upsAlarmShutdownImminentthird,
       "upsAlarmTestInProgressthird": upsAlarmTestInProgressthird,
       "upsAlarmReceptacleOffthird": upsAlarmReceptacleOffthird,
       "upsAlarmHighSpeedBusFailurethird": upsAlarmHighSpeedBusFailurethird,
       "upsAlarmHighSpeedBusJACRCFailurethird": upsAlarmHighSpeedBusJACRCFailurethird,
       "upsAlarmConnectivityBusFailurethird": upsAlarmConnectivityBusFailurethird,
       "upsAlarmHighSpeedBusJBCRCFailurethird": upsAlarmHighSpeedBusJBCRCFailurethird,
       "upsAlarmCurrentSharingthird": upsAlarmCurrentSharingthird,
       "upsAlarmDCRipplethird": upsAlarmDCRipplethird,
       "upsAlarmMaskAthird": upsAlarmMaskAthird,
       "upsTestthird": upsTestthird,
       "upsTestIdthird": upsTestIdthird,
       "upsTestSpinLockthird": upsTestSpinLockthird,
       "upsTestResultsSummarythird": upsTestResultsSummarythird,
       "upsTestResultsDetailthird": upsTestResultsDetailthird,
       "upsTestStartTimethird": upsTestStartTimethird,
       "upsTestElapsedTimethird": upsTestElapsedTimethird,
       "upsWellKnownTeststhird": upsWellKnownTeststhird,
       "upsTestNoTestsInitiatedthird": upsTestNoTestsInitiatedthird,
       "upsTestAbortTestInProgressthird": upsTestAbortTestInProgressthird,
       "upsTestGeneralSystemsTestthird": upsTestGeneralSystemsTestthird,
       "upsTestQuickBatteryTestthird": upsTestQuickBatteryTestthird,
       "upsTestDeepBatteryCalibrationthird": upsTestDeepBatteryCalibrationthird,
       "upsControlthird": upsControlthird,
       "upsShutdownTypethird": upsShutdownTypethird,
       "upsShutdownAfterDelaythird": upsShutdownAfterDelaythird,
       "upsStartupAfterDelaythird": upsStartupAfterDelaythird,
       "upsRebootWithDurationthird": upsRebootWithDurationthird,
       "upsAutoRestartthird": upsAutoRestartthird,
       "upsReceptaclesNumthird": upsReceptaclesNumthird,
       "upsReceptacleThirdTable": upsReceptacleThirdTable,
       "upsReceptacleThirdEntry": upsReceptacleThirdEntry,
       "upsReceptacleLineIndexthird": upsReceptacleLineIndexthird,
       "upsReceptacleOnOffthird": upsReceptacleOnOffthird,
       "upsUPSModethird": upsUPSModethird,
       "upsRectifierOnOffthird": upsRectifierOnOffthird,
       "upsBatteryChargeMethodthird": upsBatteryChargeMethodthird,
       "upsInverterOnOffthird": upsInverterOnOffthird,
       "upsBypassOnOffthird": upsBypassOnOffthird,
       "upsLoadSourcethird": upsLoadSourcethird,
       "upsConfigthird": upsConfigthird,
       "upsConfigInputVoltagethird": upsConfigInputVoltagethird,
       "upsConfigInputFreqthird": upsConfigInputFreqthird,
       "upsConfigOutputVoltagethird": upsConfigOutputVoltagethird,
       "upsConfigOutputFreqthird": upsConfigOutputFreqthird,
       "upsConfigOutputVAthird": upsConfigOutputVAthird,
       "upsConfigOutputPowerthird": upsConfigOutputPowerthird,
       "upsConfigLowBattTimethird": upsConfigLowBattTimethird,
       "upsConfigAudibleStatusthird": upsConfigAudibleStatusthird,
       "upsConfigLowVoltageTransferPointthird": upsConfigLowVoltageTransferPointthird,
       "upsConfigHighVoltageTransferPointthird": upsConfigHighVoltageTransferPointthird,
       "upsConfigBatteryCapacitythird": upsConfigBatteryCapacitythird,
       "upsConfigBatteryChargeCurrentthird": upsConfigBatteryChargeCurrentthird,
       "upsConfigNoLoadShutdownthird": upsConfigNoLoadShutdownthird,
       "upsConfigStartDelaythird": upsConfigStartDelaythird,
       "upsGetSetthird": upsGetSetthird,
       "upsEventGetNextthird": upsEventGetNextthird,
       "upsEventGetPreviousthird": upsEventGetPreviousthird,
       "upsEventSetStartingTimeStampthird": upsEventSetStartingTimeStampthird,
       "upsEventRetreiveCurrentTimeStampthird": upsEventRetreiveCurrentTimeStampthird,
       "upsEventTableSizethird": upsEventTableSizethird,
       "upsEventThirdTable": upsEventThirdTable,
       "upsEventThirdEntry": upsEventThirdEntry,
       "upsEventLineIndexthird": upsEventLineIndexthird,
       "upsEventCodethird": upsEventCodethird,
       "upsEventStatusthird": upsEventStatusthird,
       "upsEventTimethird": upsEventTimethird,
       "upsParametersReadthird": upsParametersReadthird,
       "upsParametersWritethird": upsParametersWritethird,
       "upsParametersStartAddressthird": upsParametersStartAddressthird,
       "upsParameterTableSizethird": upsParameterTableSizethird,
       "upsParameterThirdTable": upsParameterThirdTable,
       "upsParameterThirdEntry": upsParameterThirdEntry,
       "upsParameterLineIndexthird": upsParameterLineIndexthird,
       "upsParameterValuethird": upsParameterValuethird,
       "upsStatusthird": upsStatusthird,
       "upsMainsStatisticsMBfailthird": upsMainsStatisticsMBfailthird,
       "upsMainsStatisticsMRfailthird": upsMainsStatisticsMRfailthird,
       "upsMainsStatisticsB2third": upsMainsStatisticsB2third,
       "upsMainsStatisticsB5third": upsMainsStatisticsB5third,
       "upsMainsStatisticsB10third": upsMainsStatisticsB10third,
       "upsMainsStatisticsB200third": upsMainsStatisticsB200third,
       "upsMainsStatisticsBypRelthird": upsMainsStatisticsBypRelthird,
       "upsTimethird": upsTimethird,
       "upsRequestPermissionthird": upsRequestPermissionthird,
       "upsEventGetCodethird": upsEventGetCodethird,
       "upsEventSpinLockthird": upsEventSpinLockthird,
       "upsParameterSpinLockthird": upsParameterSpinLockthird,
       "geUPSTrapsthird": geUPSTrapsthird,
       "upsTrapAlarmBatteryBadthird": upsTrapAlarmBatteryBadthird,
       "upsTrapAlarmOnBatterythird": upsTrapAlarmOnBatterythird,
       "upsTrapAlarmLowBatterythird": upsTrapAlarmLowBatterythird,
       "upsTrapAlarmDepletedBatterythird": upsTrapAlarmDepletedBatterythird,
       "upsTrapAlarmTempBadthird": upsTrapAlarmTempBadthird,
       "upsTrapAlarmInputBadthird": upsTrapAlarmInputBadthird,
       "upsTrapAlarmOutputBadthird": upsTrapAlarmOutputBadthird,
       "upsTrapAlarmOutputOverloadthird": upsTrapAlarmOutputOverloadthird,
       "upsTrapAlarmOnBypassthird": upsTrapAlarmOnBypassthird,
       "upsTrapAlarmBypassBadthird": upsTrapAlarmBypassBadthird,
       "upsTrapAlarmOutputOffAsRequestedthird": upsTrapAlarmOutputOffAsRequestedthird,
       "upsTrapAlarmUpsOffAsRequestedthird": upsTrapAlarmUpsOffAsRequestedthird,
       "upsTrapAlarmChargerFailedthird": upsTrapAlarmChargerFailedthird,
       "upsTrapAlarmUpsOutputOffthird": upsTrapAlarmUpsOutputOffthird,
       "upsTrapAlarmUpsSystemOffthird": upsTrapAlarmUpsSystemOffthird,
       "upsTrapAlarmFanFailurethird": upsTrapAlarmFanFailurethird,
       "upsTrapAlarmFuseFailurethird": upsTrapAlarmFuseFailurethird,
       "upsTrapAlarmGeneralFaultthird": upsTrapAlarmGeneralFaultthird,
       "upsTrapAlarmDiagnosticTestFailedthird": upsTrapAlarmDiagnosticTestFailedthird,
       "upsTrapAlarmCommunicationsLostthird": upsTrapAlarmCommunicationsLostthird,
       "upsTrapAlarmAwaitingPowerthird": upsTrapAlarmAwaitingPowerthird,
       "upsTrapAlarmShutdownPendingthird": upsTrapAlarmShutdownPendingthird,
       "upsTrapAlarmShutdownImminentthird": upsTrapAlarmShutdownImminentthird,
       "upsTrapAlarmTestInProgressthird": upsTrapAlarmTestInProgressthird,
       "upsTrapAlarmReceptacleOffthird": upsTrapAlarmReceptacleOffthird,
       "upsTrapAlarmHighspeedBusFailurethird": upsTrapAlarmHighspeedBusFailurethird,
       "upsTrapAlarmHighspeedBusJACRCFailurethird": upsTrapAlarmHighspeedBusJACRCFailurethird,
       "upsTrapAlarmConnectivityBusFailurethird": upsTrapAlarmConnectivityBusFailurethird,
       "upsTrapAlarmHighspeedBusJBCRCFailurethird": upsTrapAlarmHighspeedBusJBCRCFailurethird,
       "upsTrapAlarmCurrentSharingFailurethird": upsTrapAlarmCurrentSharingFailurethird,
       "upsTrapAlarmDCRippleFailurethird": upsTrapAlarmDCRippleFailurethird,
       "upsTrapAlarmBatteryBadRestoredthird": upsTrapAlarmBatteryBadRestoredthird,
       "upsTrapAlarmOnBatteryRestoredthird": upsTrapAlarmOnBatteryRestoredthird,
       "upsTrapAlarmLowBatteryRestoredthird": upsTrapAlarmLowBatteryRestoredthird,
       "upsTrapAlarmDepletedBatteryRestoredthird": upsTrapAlarmDepletedBatteryRestoredthird,
       "upsTrapAlarmTempBadRestoredthird": upsTrapAlarmTempBadRestoredthird,
       "upsTrapAlarmInputBadRestoredthird": upsTrapAlarmInputBadRestoredthird,
       "upsTrapAlarmOutputBadRestoredthird": upsTrapAlarmOutputBadRestoredthird,
       "upsTrapAlarmOutputOverloadRestoredthird": upsTrapAlarmOutputOverloadRestoredthird,
       "upsTrapAlarmOnBypassRestoredthird": upsTrapAlarmOnBypassRestoredthird,
       "upsTrapAlarmBypassBadRestoredthird": upsTrapAlarmBypassBadRestoredthird,
       "upsTrapAlarmOutputOffAsRequestedRestoredthird": upsTrapAlarmOutputOffAsRequestedRestoredthird,
       "upsTrapAlarmUpsOffAsRequestedRestoredthird": upsTrapAlarmUpsOffAsRequestedRestoredthird,
       "upsTrapAlarmChargerFailedRestoredthird": upsTrapAlarmChargerFailedRestoredthird,
       "upsTrapAlarmUpsOutputOnthird": upsTrapAlarmUpsOutputOnthird,
       "upsTrapAlarmUpsSystemOnthird": upsTrapAlarmUpsSystemOnthird,
       "upsTrapAlarmFanFailureRestoredthird": upsTrapAlarmFanFailureRestoredthird,
       "upsTrapAlarmFuseFailureRestoredthird": upsTrapAlarmFuseFailureRestoredthird,
       "upsTrapAlarmGeneralFaultRestoredthird": upsTrapAlarmGeneralFaultRestoredthird,
       "upsTrapAlarmDiagnosticTestFailedRestoredthird": upsTrapAlarmDiagnosticTestFailedRestoredthird,
       "upsTrapAlarmCommunicationsLostRestoredthird": upsTrapAlarmCommunicationsLostRestoredthird,
       "upsTrapAlarmAwaitingPowerRestoredthird": upsTrapAlarmAwaitingPowerRestoredthird,
       "upsTrapAlarmShutdownPendingRestoredthird": upsTrapAlarmShutdownPendingRestoredthird,
       "upsTrapAlarmShutdownImminentRestoredthird": upsTrapAlarmShutdownImminentRestoredthird,
       "upsTrapAlarmTestInProgressRestoredthird": upsTrapAlarmTestInProgressRestoredthird,
       "upsTrapAlarmReceptacleOnthird": upsTrapAlarmReceptacleOnthird,
       "upsTrapAlarmHighspeedBusRestorethird": upsTrapAlarmHighspeedBusRestorethird,
       "upsTrapAlarmHighspeedBusJACRCRestorethird": upsTrapAlarmHighspeedBusJACRCRestorethird,
       "upsTrapAlarmConnectivityBusRestorethird": upsTrapAlarmConnectivityBusRestorethird,
       "upsTrapAlarmHighspeedBusJBCRCRestoredthird": upsTrapAlarmHighspeedBusJBCRCRestoredthird,
       "upsTrapAlarmCurrentSharingRestoredthird": upsTrapAlarmCurrentSharingRestoredthird,
       "upsTrapAlarmDCRippleRestoredthird": upsTrapAlarmDCRippleRestoredthird,
       "upsTrapAlarmValueLowthird": upsTrapAlarmValueLowthird,
       "upsTrapAlarmValueHighthird": upsTrapAlarmValueHighthird,
       "upsTrapAlarmValueLowRestoredthird": upsTrapAlarmValueLowRestoredthird,
       "upsTrapAlarmValueHighRestoredthird": upsTrapAlarmValueHighRestoredthird,
       "upsDiagnosticthird": upsDiagnosticthird,
       "upsDiagnosticBusJACommunicationStatusthird": upsDiagnosticBusJACommunicationStatusthird,
       "upsDiagnosticBusJBCommunicationStatusthird": upsDiagnosticBusJBCommunicationStatusthird,
       "upsDiagnosticBatteryLifetimethird": upsDiagnosticBatteryLifetimethird,
       "upsDiagnosticFansLifetimethird": upsDiagnosticFansLifetimethird,
       "upsDiagnosticDCcapacitorsLifetimethird": upsDiagnosticDCcapacitorsLifetimethird,
       "upsDiagnosticACcapacitorsLifetimethird": upsDiagnosticACcapacitorsLifetimethird,
       "upsDiagnosticGlobalServiceCheckthird": upsDiagnosticGlobalServiceCheckthird,
       "geFourthUPS": geFourthUPS,
       "upsIdentfourth": upsIdentfourth,
       "upsIdentManufacturerfourth": upsIdentManufacturerfourth,
       "upsIdentModelfourth": upsIdentModelfourth,
       "upsIdentUPSSoftwareVersionfourth": upsIdentUPSSoftwareVersionfourth,
       "upsIdentAgentSoftwareVersionfourth": upsIdentAgentSoftwareVersionfourth,
       "upsIdentNamefourth": upsIdentNamefourth,
       "upsIdentAttachedDevicesfourth": upsIdentAttachedDevicesfourth,
       "upsIdentUPSSerialNumberfourth": upsIdentUPSSerialNumberfourth,
       "upsIdentComProtVersionfourth": upsIdentComProtVersionfourth,
       "upsIdentOperatingTimefourth": upsIdentOperatingTimefourth,
       "upsBatteryfourth": upsBatteryfourth,
       "upsBatteryStatusfourth": upsBatteryStatusfourth,
       "upsSecondsOnBatteryfourth": upsSecondsOnBatteryfourth,
       "upsEstimatedMinutesRemainingfourth": upsEstimatedMinutesRemainingfourth,
       "upsEstimatedChargeRemainingfourth": upsEstimatedChargeRemainingfourth,
       "upsBatteryVoltagefourth": upsBatteryVoltagefourth,
       "upsBatteryCurrentfourth": upsBatteryCurrentfourth,
       "upsBatteryTemperaturefourth": upsBatteryTemperaturefourth,
       "upsBatteryRipplefourth": upsBatteryRipplefourth,
       "upsInputfourth": upsInputfourth,
       "upsInputLineBadsfourth": upsInputLineBadsfourth,
       "upsInputNumLinesfourth": upsInputNumLinesfourth,
       "upsInputFourthTable": upsInputFourthTable,
       "upsInputFourthEntry": upsInputFourthEntry,
       "upsInputLineIndexfourth": upsInputLineIndexfourth,
       "upsInputFrequencyfourth": upsInputFrequencyfourth,
       "upsInputVoltagefourth": upsInputVoltagefourth,
       "upsInputCurrentfourth": upsInputCurrentfourth,
       "upsInputTruePowerfourth": upsInputTruePowerfourth,
       "upsInputVoltageMinfourth": upsInputVoltageMinfourth,
       "upsInputVoltageMaxfourth": upsInputVoltageMaxfourth,
       "upsOutputfourth": upsOutputfourth,
       "upsOutputSourcefourth": upsOutputSourcefourth,
       "upsOutputFrequencyfourth": upsOutputFrequencyfourth,
       "upsOutputNumLinesfourth": upsOutputNumLinesfourth,
       "upsOutputFourthTable": upsOutputFourthTable,
       "upsOutputFourthEntry": upsOutputFourthEntry,
       "upsOutputLineIndexfourth": upsOutputLineIndexfourth,
       "upsOutputVoltagefourth": upsOutputVoltagefourth,
       "upsOutputCurrentfourth": upsOutputCurrentfourth,
       "upsOutputPowerfourth": upsOutputPowerfourth,
       "upsOutputPercentLoadfourth": upsOutputPercentLoadfourth,
       "upsOutputPowerFactorfourth": upsOutputPowerFactorfourth,
       "upsOutputPeakCurrentfourth": upsOutputPeakCurrentfourth,
       "upsOutputShareCurrentfourth": upsOutputShareCurrentfourth,
       "upsBypassfourth": upsBypassfourth,
       "upsBypassFrequencyfourth": upsBypassFrequencyfourth,
       "upsBypassNumLinesfourth": upsBypassNumLinesfourth,
       "upsBypassFourthTable": upsBypassFourthTable,
       "upsBypassFourthEntry": upsBypassFourthEntry,
       "upsBypassLineIndexfourth": upsBypassLineIndexfourth,
       "upsBypassVoltagefourth": upsBypassVoltagefourth,
       "upsBypassCurrentfourth": upsBypassCurrentfourth,
       "upsBypassPowerfourth": upsBypassPowerfourth,
       "upsAlarmfourth": upsAlarmfourth,
       "upsAlarmsPresentfourth": upsAlarmsPresentfourth,
       "upsAlarmFourthTable": upsAlarmFourthTable,
       "upsAlarmFourthEntry": upsAlarmFourthEntry,
       "upsAlarmIdfourth": upsAlarmIdfourth,
       "upsAlarmDescrfourth": upsAlarmDescrfourth,
       "upsAlarmTimefourth": upsAlarmTimefourth,
       "upsWellKnownAlarmsfourth": upsWellKnownAlarmsfourth,
       "upsAlarmBatteryBadfourth": upsAlarmBatteryBadfourth,
       "upsAlarmOnBatteryfourth": upsAlarmOnBatteryfourth,
       "upsAlarmLowBatteryfourth": upsAlarmLowBatteryfourth,
       "upsAlarmDepletedBatteryfourth": upsAlarmDepletedBatteryfourth,
       "upsAlarmTempBadfourth": upsAlarmTempBadfourth,
       "upsAlarmInputBadfourth": upsAlarmInputBadfourth,
       "upsAlarmOutputBadfourth": upsAlarmOutputBadfourth,
       "upsAlarmOutputOverloadfourth": upsAlarmOutputOverloadfourth,
       "upsAlarmOnBypassfourth": upsAlarmOnBypassfourth,
       "upsAlarmBypassBadfourth": upsAlarmBypassBadfourth,
       "upsAlarmOutputOffAsRequestedfourth": upsAlarmOutputOffAsRequestedfourth,
       "upsAlarmUpsOffAsRequestedfourth": upsAlarmUpsOffAsRequestedfourth,
       "upsAlarmChargerFailedfourth": upsAlarmChargerFailedfourth,
       "upsAlarmUpsOutputOfffourth": upsAlarmUpsOutputOfffourth,
       "upsAlarmUpsSystemOfffourth": upsAlarmUpsSystemOfffourth,
       "upsAlarmFanFailurefourth": upsAlarmFanFailurefourth,
       "upsAlarmFuseFailurefourth": upsAlarmFuseFailurefourth,
       "upsAlarmGeneralFaultfourth": upsAlarmGeneralFaultfourth,
       "upsAlarmDiagnosticTestFailedfourth": upsAlarmDiagnosticTestFailedfourth,
       "upsAlarmCommunicationsLostfourth": upsAlarmCommunicationsLostfourth,
       "upsAlarmAwaitingPowerfourth": upsAlarmAwaitingPowerfourth,
       "upsAlarmShutdownPendingfourth": upsAlarmShutdownPendingfourth,
       "upsAlarmShutdownImminentfourth": upsAlarmShutdownImminentfourth,
       "upsAlarmTestInProgressfourth": upsAlarmTestInProgressfourth,
       "upsAlarmReceptacleOfffourth": upsAlarmReceptacleOfffourth,
       "upsAlarmHighSpeedBusFailurefourth": upsAlarmHighSpeedBusFailurefourth,
       "upsAlarmHighSpeedBusJACRCFailurefourth": upsAlarmHighSpeedBusJACRCFailurefourth,
       "upsAlarmConnectivityBusFailurefourth": upsAlarmConnectivityBusFailurefourth,
       "upsAlarmHighSpeedBusJBCRCFailurefourth": upsAlarmHighSpeedBusJBCRCFailurefourth,
       "upsAlarmCurrentSharingfourth": upsAlarmCurrentSharingfourth,
       "upsAlarmDCRipplefourth": upsAlarmDCRipplefourth,
       "upsAlarmMaskAfourth": upsAlarmMaskAfourth,
       "upsTestfourth": upsTestfourth,
       "upsTestIdfourth": upsTestIdfourth,
       "upsTestSpinLockfourth": upsTestSpinLockfourth,
       "upsTestResultsSummaryfourth": upsTestResultsSummaryfourth,
       "upsTestResultsDetailfourth": upsTestResultsDetailfourth,
       "upsTestStartTimefourth": upsTestStartTimefourth,
       "upsTestElapsedTimefourth": upsTestElapsedTimefourth,
       "upsWellKnownTestsfourth": upsWellKnownTestsfourth,
       "upsTestNoTestsInitiatedfourth": upsTestNoTestsInitiatedfourth,
       "upsTestAbortTestInProgressfourth": upsTestAbortTestInProgressfourth,
       "upsTestGeneralSystemsTestfourth": upsTestGeneralSystemsTestfourth,
       "upsTestQuickBatteryTestfourth": upsTestQuickBatteryTestfourth,
       "upsTestDeepBatteryCalibrationfourth": upsTestDeepBatteryCalibrationfourth,
       "upsControlfourth": upsControlfourth,
       "upsShutdownTypefourth": upsShutdownTypefourth,
       "upsShutdownAfterDelayfourth": upsShutdownAfterDelayfourth,
       "upsStartupAfterDelayfourth": upsStartupAfterDelayfourth,
       "upsRebootWithDurationfourth": upsRebootWithDurationfourth,
       "upsAutoRestartfourth": upsAutoRestartfourth,
       "upsReceptaclesNumfourth": upsReceptaclesNumfourth,
       "upsReceptacleFourthTable": upsReceptacleFourthTable,
       "upsReceptacleFourthEntry": upsReceptacleFourthEntry,
       "upsReceptacleLineIndexfourth": upsReceptacleLineIndexfourth,
       "upsReceptacleOnOfffourth": upsReceptacleOnOfffourth,
       "upsUPSModefourth": upsUPSModefourth,
       "upsRectifierOnOfffourth": upsRectifierOnOfffourth,
       "upsBatteryChargeMethodfourth": upsBatteryChargeMethodfourth,
       "upsInverterOnOfffourth": upsInverterOnOfffourth,
       "upsBypassOnOfffourth": upsBypassOnOfffourth,
       "upsLoadSourcefourth": upsLoadSourcefourth,
       "upsConfigfourth": upsConfigfourth,
       "upsConfigInputVoltagefourth": upsConfigInputVoltagefourth,
       "upsConfigInputFreqfourth": upsConfigInputFreqfourth,
       "upsConfigOutputVoltagefourth": upsConfigOutputVoltagefourth,
       "upsConfigOutputFreqfourth": upsConfigOutputFreqfourth,
       "upsConfigOutputVAfourth": upsConfigOutputVAfourth,
       "upsConfigOutputPowerfourth": upsConfigOutputPowerfourth,
       "upsConfigLowBattTimefourth": upsConfigLowBattTimefourth,
       "upsConfigAudibleStatusfourth": upsConfigAudibleStatusfourth,
       "upsConfigLowVoltageTransferPointfourth": upsConfigLowVoltageTransferPointfourth,
       "upsConfigHighVoltageTransferPointfourth": upsConfigHighVoltageTransferPointfourth,
       "upsConfigBatteryCapacityfourth": upsConfigBatteryCapacityfourth,
       "upsConfigBatteryChargeCurrentfourth": upsConfigBatteryChargeCurrentfourth,
       "upsConfigNoLoadShutdownfourth": upsConfigNoLoadShutdownfourth,
       "upsConfigStartDelayfourth": upsConfigStartDelayfourth,
       "upsGetSetfourth": upsGetSetfourth,
       "upsEventGetNextfourth": upsEventGetNextfourth,
       "upsEventGetPreviousfourth": upsEventGetPreviousfourth,
       "upsEventSetStartingTimeStampfourth": upsEventSetStartingTimeStampfourth,
       "upsEventRetreiveCurrentTimeStampfourth": upsEventRetreiveCurrentTimeStampfourth,
       "upsEventTableSizefourth": upsEventTableSizefourth,
       "upsEventFourthTable": upsEventFourthTable,
       "upsEventFourthEntry": upsEventFourthEntry,
       "upsEventLineIndexfourth": upsEventLineIndexfourth,
       "upsEventCodefourth": upsEventCodefourth,
       "upsEventStatusfourth": upsEventStatusfourth,
       "upsEventTimefourth": upsEventTimefourth,
       "upsParametersReadfourth": upsParametersReadfourth,
       "upsParametersWritefourth": upsParametersWritefourth,
       "upsParametersStartAddressfourth": upsParametersStartAddressfourth,
       "upsParameterTableSizefourth": upsParameterTableSizefourth,
       "upsParameterFourthTable": upsParameterFourthTable,
       "upsParameterFourthEntry": upsParameterFourthEntry,
       "upsParameterLineIndexfourth": upsParameterLineIndexfourth,
       "upsParameterValuefourth": upsParameterValuefourth,
       "upsStatusfourth": upsStatusfourth,
       "upsMainsStatisticsMBfailfourth": upsMainsStatisticsMBfailfourth,
       "upsMainsStatisticsMRfailfourth": upsMainsStatisticsMRfailfourth,
       "upsMainsStatisticsB2fourth": upsMainsStatisticsB2fourth,
       "upsMainsStatisticsB5fourth": upsMainsStatisticsB5fourth,
       "upsMainsStatisticsB10fourth": upsMainsStatisticsB10fourth,
       "upsMainsStatisticsB200fourth": upsMainsStatisticsB200fourth,
       "upsMainsStatisticsBypRelfourth": upsMainsStatisticsBypRelfourth,
       "upsTimefourth": upsTimefourth,
       "upsRequestPermissionfourth": upsRequestPermissionfourth,
       "upsEventGetCodefourth": upsEventGetCodefourth,
       "upsEventSpinLockfourth": upsEventSpinLockfourth,
       "upsParameterSpinLockfourth": upsParameterSpinLockfourth,
       "geUPSTrapsfourth": geUPSTrapsfourth,
       "upsTrapAlarmBatteryBadfourth": upsTrapAlarmBatteryBadfourth,
       "upsTrapAlarmOnBatteryfourth": upsTrapAlarmOnBatteryfourth,
       "upsTrapAlarmLowBatteryfourth": upsTrapAlarmLowBatteryfourth,
       "upsTrapAlarmDepletedBatteryfourth": upsTrapAlarmDepletedBatteryfourth,
       "upsTrapAlarmTempBadfourth": upsTrapAlarmTempBadfourth,
       "upsTrapAlarmInputBadfourth": upsTrapAlarmInputBadfourth,
       "upsTrapAlarmOutputBadfourth": upsTrapAlarmOutputBadfourth,
       "upsTrapAlarmOutputOverloadfourth": upsTrapAlarmOutputOverloadfourth,
       "upsTrapAlarmOnBypassfourth": upsTrapAlarmOnBypassfourth,
       "upsTrapAlarmBypassBadfourth": upsTrapAlarmBypassBadfourth,
       "upsTrapAlarmOutputOffAsRequestedfourth": upsTrapAlarmOutputOffAsRequestedfourth,
       "upsTrapAlarmUpsOffAsRequestedfourth": upsTrapAlarmUpsOffAsRequestedfourth,
       "upsTrapAlarmChargerFailedfourth": upsTrapAlarmChargerFailedfourth,
       "upsTrapAlarmUpsOutputOfffourth": upsTrapAlarmUpsOutputOfffourth,
       "upsTrapAlarmUpsSystemOfffourth": upsTrapAlarmUpsSystemOfffourth,
       "upsTrapAlarmFanFailurefourth": upsTrapAlarmFanFailurefourth,
       "upsTrapAlarmFuseFailurefourth": upsTrapAlarmFuseFailurefourth,
       "upsTrapAlarmGeneralFaultfourth": upsTrapAlarmGeneralFaultfourth,
       "upsTrapAlarmDiagnosticTestFailedfourth": upsTrapAlarmDiagnosticTestFailedfourth,
       "upsTrapAlarmCommunicationsLostfourth": upsTrapAlarmCommunicationsLostfourth,
       "upsTrapAlarmAwaitingPowerfourth": upsTrapAlarmAwaitingPowerfourth,
       "upsTrapAlarmShutdownPendingfourth": upsTrapAlarmShutdownPendingfourth,
       "upsTrapAlarmShutdownImminentfourth": upsTrapAlarmShutdownImminentfourth,
       "upsTrapAlarmTestInProgressfourth": upsTrapAlarmTestInProgressfourth,
       "upsTrapAlarmReceptacleOfffourth": upsTrapAlarmReceptacleOfffourth,
       "upsTrapAlarmHighspeedBusFailurefourth": upsTrapAlarmHighspeedBusFailurefourth,
       "upsTrapAlarmHighspeedBusJACRCFailurefourth": upsTrapAlarmHighspeedBusJACRCFailurefourth,
       "upsTrapAlarmConnectivityBusFailurefourth": upsTrapAlarmConnectivityBusFailurefourth,
       "upsTrapAlarmHighspeedBusJBCRCFailurefourth": upsTrapAlarmHighspeedBusJBCRCFailurefourth,
       "upsTrapAlarmCurrentSharingFailurefourth": upsTrapAlarmCurrentSharingFailurefourth,
       "upsTrapAlarmDCRippleFailurefourth": upsTrapAlarmDCRippleFailurefourth,
       "upsTrapAlarmBatteryBadRestoredfourth": upsTrapAlarmBatteryBadRestoredfourth,
       "upsTrapAlarmOnBatteryRestoredfourth": upsTrapAlarmOnBatteryRestoredfourth,
       "upsTrapAlarmLowBatteryRestoredfourth": upsTrapAlarmLowBatteryRestoredfourth,
       "upsTrapAlarmDepletedBatteryRestoredfourth": upsTrapAlarmDepletedBatteryRestoredfourth,
       "upsTrapAlarmTempBadRestoredfourth": upsTrapAlarmTempBadRestoredfourth,
       "upsTrapAlarmInputBadRestoredfourth": upsTrapAlarmInputBadRestoredfourth,
       "upsTrapAlarmOutputBadRestoredfourth": upsTrapAlarmOutputBadRestoredfourth,
       "upsTrapAlarmOutputOverloadRestoredfourth": upsTrapAlarmOutputOverloadRestoredfourth,
       "upsTrapAlarmOnBypassRestoredfourth": upsTrapAlarmOnBypassRestoredfourth,
       "upsTrapAlarmBypassBadRestoredfourth": upsTrapAlarmBypassBadRestoredfourth,
       "upsTrapAlarmOutputOffAsRequestedRestoredfourth": upsTrapAlarmOutputOffAsRequestedRestoredfourth,
       "upsTrapAlarmUpsOffAsRequestedRestoredfourth": upsTrapAlarmUpsOffAsRequestedRestoredfourth,
       "upsTrapAlarmChargerFailedRestoredfourth": upsTrapAlarmChargerFailedRestoredfourth,
       "upsTrapAlarmUpsOutputOnfourth": upsTrapAlarmUpsOutputOnfourth,
       "upsTrapAlarmUpsSystemOnfourth": upsTrapAlarmUpsSystemOnfourth,
       "upsTrapAlarmFanFailureRestoredfourth": upsTrapAlarmFanFailureRestoredfourth,
       "upsTrapAlarmFuseFailureRestoredfourth": upsTrapAlarmFuseFailureRestoredfourth,
       "upsTrapAlarmGeneralFaultRestoredfourth": upsTrapAlarmGeneralFaultRestoredfourth,
       "upsTrapAlarmDiagnosticTestFailedRestoredfourth": upsTrapAlarmDiagnosticTestFailedRestoredfourth,
       "upsTrapAlarmCommunicationsLostRestoredfourth": upsTrapAlarmCommunicationsLostRestoredfourth,
       "upsTrapAlarmAwaitingPowerRestoredfourth": upsTrapAlarmAwaitingPowerRestoredfourth,
       "upsTrapAlarmShutdownPendingRestoredfourth": upsTrapAlarmShutdownPendingRestoredfourth,
       "upsTrapAlarmShutdownImminentRestoredfourth": upsTrapAlarmShutdownImminentRestoredfourth,
       "upsTrapAlarmTestInProgressRestoredfourth": upsTrapAlarmTestInProgressRestoredfourth,
       "upsTrapAlarmReceptacleOnfourth": upsTrapAlarmReceptacleOnfourth,
       "upsTrapAlarmHighspeedBusRestorefourth": upsTrapAlarmHighspeedBusRestorefourth,
       "upsTrapAlarmHighspeedBusJACRCRestorefourth": upsTrapAlarmHighspeedBusJACRCRestorefourth,
       "upsTrapAlarmConnectivityBusRestorefourth": upsTrapAlarmConnectivityBusRestorefourth,
       "upsTrapAlarmHighspeedBusJBCRCRestoredfourth": upsTrapAlarmHighspeedBusJBCRCRestoredfourth,
       "upsTrapAlarmCurrentSharingRestoredfourth": upsTrapAlarmCurrentSharingRestoredfourth,
       "upsTrapAlarmDCRippleRestoredfourth": upsTrapAlarmDCRippleRestoredfourth,
       "upsTrapAlarmValueLowfourth": upsTrapAlarmValueLowfourth,
       "upsTrapAlarmValueHighfourth": upsTrapAlarmValueHighfourth,
       "upsTrapAlarmValueLowRestoredfourth": upsTrapAlarmValueLowRestoredfourth,
       "upsTrapAlarmValueHighRestoredfourth": upsTrapAlarmValueHighRestoredfourth,
       "upsDiagnosticfourth": upsDiagnosticfourth,
       "upsDiagnosticBusJACommunicationStatusfourth": upsDiagnosticBusJACommunicationStatusfourth,
       "upsDiagnosticBusJBCommunicationStatusfourth": upsDiagnosticBusJBCommunicationStatusfourth,
       "upsDiagnosticBatteryLifetimefourth": upsDiagnosticBatteryLifetimefourth,
       "upsDiagnosticFansLifetimefourth": upsDiagnosticFansLifetimefourth,
       "upsDiagnosticDCcapacitorsLifetimefourth": upsDiagnosticDCcapacitorsLifetimefourth,
       "upsDiagnosticACcapacitorsLifetimefourth": upsDiagnosticACcapacitorsLifetimefourth,
       "upsDiagnosticGlobalServiceCheckfourth": upsDiagnosticGlobalServiceCheckfourth,
       "geFifthUPS": geFifthUPS,
       "upsIdentfifth": upsIdentfifth,
       "upsIdentManufacturerfifth": upsIdentManufacturerfifth,
       "upsIdentModelfifth": upsIdentModelfifth,
       "upsIdentUPSSoftwareVersionfifth": upsIdentUPSSoftwareVersionfifth,
       "upsIdentAgentSoftwareVersionfifth": upsIdentAgentSoftwareVersionfifth,
       "upsIdentNamefifth": upsIdentNamefifth,
       "upsIdentAttachedDevicesfifth": upsIdentAttachedDevicesfifth,
       "upsIdentUPSSerialNumberfifth": upsIdentUPSSerialNumberfifth,
       "upsIdentComProtVersionfifth": upsIdentComProtVersionfifth,
       "upsIdentOperatingTimefifth": upsIdentOperatingTimefifth,
       "upsBatteryfifth": upsBatteryfifth,
       "upsBatteryStatusfifth": upsBatteryStatusfifth,
       "upsSecondsOnBatteryfifth": upsSecondsOnBatteryfifth,
       "upsEstimatedMinutesRemainingfifth": upsEstimatedMinutesRemainingfifth,
       "upsEstimatedChargeRemainingfifth": upsEstimatedChargeRemainingfifth,
       "upsBatteryVoltagefifth": upsBatteryVoltagefifth,
       "upsBatteryCurrentfifth": upsBatteryCurrentfifth,
       "upsBatteryTemperaturefifth": upsBatteryTemperaturefifth,
       "upsBatteryRipplefifth": upsBatteryRipplefifth,
       "upsInputfifth": upsInputfifth,
       "upsInputLineBadsfifth": upsInputLineBadsfifth,
       "upsInputNumLinesfifth": upsInputNumLinesfifth,
       "upsInputFifthTable": upsInputFifthTable,
       "upsInputFifthEntry": upsInputFifthEntry,
       "upsInputLineIndexfifth": upsInputLineIndexfifth,
       "upsInputFrequencyfifth": upsInputFrequencyfifth,
       "upsInputVoltagefifth": upsInputVoltagefifth,
       "upsInputCurrentfifth": upsInputCurrentfifth,
       "upsInputTruePowerfifth": upsInputTruePowerfifth,
       "upsInputVoltageMinfifth": upsInputVoltageMinfifth,
       "upsInputVoltageMaxfifth": upsInputVoltageMaxfifth,
       "upsOutputfifth": upsOutputfifth,
       "upsOutputSourcefifth": upsOutputSourcefifth,
       "upsOutputFrequencyfifth": upsOutputFrequencyfifth,
       "upsOutputNumLinesfifth": upsOutputNumLinesfifth,
       "upsOutputFifthTable": upsOutputFifthTable,
       "upsOutputFifthEntry": upsOutputFifthEntry,
       "upsOutputLineIndexfifth": upsOutputLineIndexfifth,
       "upsOutputVoltagefifth": upsOutputVoltagefifth,
       "upsOutputCurrentfifth": upsOutputCurrentfifth,
       "upsOutputPowerfifth": upsOutputPowerfifth,
       "upsOutputPercentLoadfifth": upsOutputPercentLoadfifth,
       "upsOutputPowerFactorfifth": upsOutputPowerFactorfifth,
       "upsOutputPeakCurrentfifth": upsOutputPeakCurrentfifth,
       "upsOutputShareCurrentfifth": upsOutputShareCurrentfifth,
       "upsBypassfifth": upsBypassfifth,
       "upsBypassFrequencyfifth": upsBypassFrequencyfifth,
       "upsBypassNumLinesfifth": upsBypassNumLinesfifth,
       "upsBypassFifthTable": upsBypassFifthTable,
       "upsBypassFifthEntry": upsBypassFifthEntry,
       "upsBypassLineIndexfifth": upsBypassLineIndexfifth,
       "upsBypassVoltagefifth": upsBypassVoltagefifth,
       "upsBypassCurrentfifth": upsBypassCurrentfifth,
       "upsBypassPowerfifth": upsBypassPowerfifth,
       "upsAlarmfifth": upsAlarmfifth,
       "upsAlarmsPresentfifth": upsAlarmsPresentfifth,
       "upsAlarmFifthTable": upsAlarmFifthTable,
       "upsAlarmFifthEntry": upsAlarmFifthEntry,
       "upsAlarmIdfifth": upsAlarmIdfifth,
       "upsAlarmDescrfifth": upsAlarmDescrfifth,
       "upsAlarmTimefifth": upsAlarmTimefifth,
       "upsWellKnownAlarmsfifth": upsWellKnownAlarmsfifth,
       "upsAlarmBatteryBadfifth": upsAlarmBatteryBadfifth,
       "upsAlarmOnBatteryfifth": upsAlarmOnBatteryfifth,
       "upsAlarmLowBatteryfifth": upsAlarmLowBatteryfifth,
       "upsAlarmDepletedBatteryfifth": upsAlarmDepletedBatteryfifth,
       "upsAlarmTempBadfifth": upsAlarmTempBadfifth,
       "upsAlarmInputBadfifth": upsAlarmInputBadfifth,
       "upsAlarmOutputBadfifth": upsAlarmOutputBadfifth,
       "upsAlarmOutputOverloadfifth": upsAlarmOutputOverloadfifth,
       "upsAlarmOnBypassfifth": upsAlarmOnBypassfifth,
       "upsAlarmBypassBadfifth": upsAlarmBypassBadfifth,
       "upsAlarmOutputOffAsRequestedfifth": upsAlarmOutputOffAsRequestedfifth,
       "upsAlarmUpsOffAsRequestedfifth": upsAlarmUpsOffAsRequestedfifth,
       "upsAlarmChargerFailedfifth": upsAlarmChargerFailedfifth,
       "upsAlarmUpsOutputOfffifth": upsAlarmUpsOutputOfffifth,
       "upsAlarmUpsSystemOfffifth": upsAlarmUpsSystemOfffifth,
       "upsAlarmFanFailurefifth": upsAlarmFanFailurefifth,
       "upsAlarmFuseFailurefifth": upsAlarmFuseFailurefifth,
       "upsAlarmGeneralFaultfifth": upsAlarmGeneralFaultfifth,
       "upsAlarmDiagnosticTestFailedfifth": upsAlarmDiagnosticTestFailedfifth,
       "upsAlarmCommunicationsLostfifth": upsAlarmCommunicationsLostfifth,
       "upsAlarmAwaitingPowerfifth": upsAlarmAwaitingPowerfifth,
       "upsAlarmShutdownPendingfifth": upsAlarmShutdownPendingfifth,
       "upsAlarmShutdownImminentfifth": upsAlarmShutdownImminentfifth,
       "upsAlarmTestInProgressfifth": upsAlarmTestInProgressfifth,
       "upsAlarmReceptacleOfffifth": upsAlarmReceptacleOfffifth,
       "upsAlarmHighSpeedBusFailurefifth": upsAlarmHighSpeedBusFailurefifth,
       "upsAlarmHighSpeedBusJACRCFailurefifth": upsAlarmHighSpeedBusJACRCFailurefifth,
       "upsAlarmConnectivityBusFailurefifth": upsAlarmConnectivityBusFailurefifth,
       "upsAlarmHighSpeedBusJBCRCFailurefifth": upsAlarmHighSpeedBusJBCRCFailurefifth,
       "upsAlarmCurrentSharingfifth": upsAlarmCurrentSharingfifth,
       "upsAlarmDCRipplefifth": upsAlarmDCRipplefifth,
       "upsAlarmMaskAfifth": upsAlarmMaskAfifth,
       "upsTestfifth": upsTestfifth,
       "upsTestIdfifth": upsTestIdfifth,
       "upsTestSpinLockfifth": upsTestSpinLockfifth,
       "upsTestResultsSummaryfifth": upsTestResultsSummaryfifth,
       "upsTestResultsDetailfifth": upsTestResultsDetailfifth,
       "upsTestStartTimefifth": upsTestStartTimefifth,
       "upsTestElapsedTimefifth": upsTestElapsedTimefifth,
       "upsWellKnownTestsfifth": upsWellKnownTestsfifth,
       "upsTestNoTestsInitiatedfifth": upsTestNoTestsInitiatedfifth,
       "upsTestAbortTestInProgressfifth": upsTestAbortTestInProgressfifth,
       "upsTestGeneralSystemsTestfifth": upsTestGeneralSystemsTestfifth,
       "upsTestQuickBatteryTestfifth": upsTestQuickBatteryTestfifth,
       "upsTestDeepBatteryCalibrationfifth": upsTestDeepBatteryCalibrationfifth,
       "upsControlfifth": upsControlfifth,
       "upsShutdownTypefifth": upsShutdownTypefifth,
       "upsShutdownAfterDelayfifth": upsShutdownAfterDelayfifth,
       "upsStartupAfterDelayfifth": upsStartupAfterDelayfifth,
       "upsRebootWithDurationfifth": upsRebootWithDurationfifth,
       "upsAutoRestartfifth": upsAutoRestartfifth,
       "upsReceptaclesNumfifth": upsReceptaclesNumfifth,
       "upsReceptacleFifthTable": upsReceptacleFifthTable,
       "upsReceptacleFifthEntry": upsReceptacleFifthEntry,
       "upsReceptacleLineIndexfifth": upsReceptacleLineIndexfifth,
       "upsReceptacleOnOfffifth": upsReceptacleOnOfffifth,
       "upsUPSModefifth": upsUPSModefifth,
       "upsRectifierOnOfffifth": upsRectifierOnOfffifth,
       "upsBatteryChargeMethodfifth": upsBatteryChargeMethodfifth,
       "upsInverterOnOfffifth": upsInverterOnOfffifth,
       "upsBypassOnOfffifth": upsBypassOnOfffifth,
       "upsLoadSourcefifth": upsLoadSourcefifth,
       "upsConfigfifth": upsConfigfifth,
       "upsConfigInputVoltagefifth": upsConfigInputVoltagefifth,
       "upsConfigInputFreqfifth": upsConfigInputFreqfifth,
       "upsConfigOutputVoltagefifth": upsConfigOutputVoltagefifth,
       "upsConfigOutputFreqfifth": upsConfigOutputFreqfifth,
       "upsConfigOutputVAfifth": upsConfigOutputVAfifth,
       "upsConfigOutputPowerfifth": upsConfigOutputPowerfifth,
       "upsConfigLowBattTimefifth": upsConfigLowBattTimefifth,
       "upsConfigAudibleStatusfifth": upsConfigAudibleStatusfifth,
       "upsConfigLowVoltageTransferPointfifth": upsConfigLowVoltageTransferPointfifth,
       "upsConfigHighVoltageTransferPointfifth": upsConfigHighVoltageTransferPointfifth,
       "upsConfigBatteryCapacityfifth": upsConfigBatteryCapacityfifth,
       "upsConfigBatteryChargeCurrentfifth": upsConfigBatteryChargeCurrentfifth,
       "upsConfigNoLoadShutdownfifth": upsConfigNoLoadShutdownfifth,
       "upsConfigStartDelayfifth": upsConfigStartDelayfifth,
       "upsGetSetfifth": upsGetSetfifth,
       "upsEventGetNextfifth": upsEventGetNextfifth,
       "upsEventGetPreviousfifth": upsEventGetPreviousfifth,
       "upsEventSetStartingTimeStampfifth": upsEventSetStartingTimeStampfifth,
       "upsEventRetreiveCurrentTimeStampfifth": upsEventRetreiveCurrentTimeStampfifth,
       "upsEventTableSizefifth": upsEventTableSizefifth,
       "upsEventFifthTable": upsEventFifthTable,
       "upsEventFifthEntry": upsEventFifthEntry,
       "upsEventLineIndexfifth": upsEventLineIndexfifth,
       "upsEventCodefifth": upsEventCodefifth,
       "upsEventStatusfifth": upsEventStatusfifth,
       "upsEventTimefifth": upsEventTimefifth,
       "upsParametersReadfifth": upsParametersReadfifth,
       "upsParametersWritefifth": upsParametersWritefifth,
       "upsParametersStartAddressfifth": upsParametersStartAddressfifth,
       "upsParameterTableSizefifth": upsParameterTableSizefifth,
       "upsParameterFifthTable": upsParameterFifthTable,
       "upsParameterFifthEntry": upsParameterFifthEntry,
       "upsParameterLineIndexfifth": upsParameterLineIndexfifth,
       "upsParameterValuefifth": upsParameterValuefifth,
       "upsStatusfifth": upsStatusfifth,
       "upsMainsStatisticsMBfailfifth": upsMainsStatisticsMBfailfifth,
       "upsMainsStatisticsMRfailfifth": upsMainsStatisticsMRfailfifth,
       "upsMainsStatisticsB2fifth": upsMainsStatisticsB2fifth,
       "upsMainsStatisticsB5fifth": upsMainsStatisticsB5fifth,
       "upsMainsStatisticsB10fifth": upsMainsStatisticsB10fifth,
       "upsMainsStatisticsB200fifth": upsMainsStatisticsB200fifth,
       "upsMainsStatisticsBypRelfifth": upsMainsStatisticsBypRelfifth,
       "upsTimefifth": upsTimefifth,
       "upsRequestPermissionfifth": upsRequestPermissionfifth,
       "upsEventGetCodefifth": upsEventGetCodefifth,
       "upsEventSpinLockfifth": upsEventSpinLockfifth,
       "upsParameterSpinLockfifth": upsParameterSpinLockfifth,
       "geUPSTrapsfifth": geUPSTrapsfifth,
       "upsTrapAlarmBatteryBadfifth": upsTrapAlarmBatteryBadfifth,
       "upsTrapAlarmOnBatteryfifth": upsTrapAlarmOnBatteryfifth,
       "upsTrapAlarmLowBatteryfifth": upsTrapAlarmLowBatteryfifth,
       "upsTrapAlarmDepletedBatteryfifth": upsTrapAlarmDepletedBatteryfifth,
       "upsTrapAlarmTempBadfifth": upsTrapAlarmTempBadfifth,
       "upsTrapAlarmInputBadfifth": upsTrapAlarmInputBadfifth,
       "upsTrapAlarmOutputBadfifth": upsTrapAlarmOutputBadfifth,
       "upsTrapAlarmOutputOverloadfifth": upsTrapAlarmOutputOverloadfifth,
       "upsTrapAlarmOnBypassfifth": upsTrapAlarmOnBypassfifth,
       "upsTrapAlarmBypassBadfifth": upsTrapAlarmBypassBadfifth,
       "upsTrapAlarmOutputOffAsRequestedfifth": upsTrapAlarmOutputOffAsRequestedfifth,
       "upsTrapAlarmUpsOffAsRequestedfifth": upsTrapAlarmUpsOffAsRequestedfifth,
       "upsTrapAlarmChargerFailedfifth": upsTrapAlarmChargerFailedfifth,
       "upsTrapAlarmUpsOutputOfffifth": upsTrapAlarmUpsOutputOfffifth,
       "upsTrapAlarmUpsSystemOfffifth": upsTrapAlarmUpsSystemOfffifth,
       "upsTrapAlarmFanFailurefifth": upsTrapAlarmFanFailurefifth,
       "upsTrapAlarmFuseFailurefifth": upsTrapAlarmFuseFailurefifth,
       "upsTrapAlarmGeneralFaultfifth": upsTrapAlarmGeneralFaultfifth,
       "upsTrapAlarmDiagnosticTestFailedfifth": upsTrapAlarmDiagnosticTestFailedfifth,
       "upsTrapAlarmCommunicationsLostfifth": upsTrapAlarmCommunicationsLostfifth,
       "upsTrapAlarmAwaitingPowerfifth": upsTrapAlarmAwaitingPowerfifth,
       "upsTrapAlarmShutdownPendingfifth": upsTrapAlarmShutdownPendingfifth,
       "upsTrapAlarmShutdownImminentfifth": upsTrapAlarmShutdownImminentfifth,
       "upsTrapAlarmTestInProgressfifth": upsTrapAlarmTestInProgressfifth,
       "upsTrapAlarmReceptacleOfffifth": upsTrapAlarmReceptacleOfffifth,
       "upsTrapAlarmHighspeedBusFailurefifth": upsTrapAlarmHighspeedBusFailurefifth,
       "upsTrapAlarmHighspeedBusJACRCFailurefifth": upsTrapAlarmHighspeedBusJACRCFailurefifth,
       "upsTrapAlarmConnectivityBusFailurefifth": upsTrapAlarmConnectivityBusFailurefifth,
       "upsTrapAlarmHighspeedBusJBCRCFailurefifth": upsTrapAlarmHighspeedBusJBCRCFailurefifth,
       "upsTrapAlarmCurrentSharingFailurefifth": upsTrapAlarmCurrentSharingFailurefifth,
       "upsTrapAlarmDCRippleFailurefifth": upsTrapAlarmDCRippleFailurefifth,
       "upsTrapAlarmBatteryBadRestoredfifth": upsTrapAlarmBatteryBadRestoredfifth,
       "upsTrapAlarmOnBatteryRestoredfifth": upsTrapAlarmOnBatteryRestoredfifth,
       "upsTrapAlarmLowBatteryRestoredfifth": upsTrapAlarmLowBatteryRestoredfifth,
       "upsTrapAlarmDepletedBatteryRestoredfifth": upsTrapAlarmDepletedBatteryRestoredfifth,
       "upsTrapAlarmTempBadRestoredfifth": upsTrapAlarmTempBadRestoredfifth,
       "upsTrapAlarmInputBadRestoredfifth": upsTrapAlarmInputBadRestoredfifth,
       "upsTrapAlarmOutputBadRestoredfifth": upsTrapAlarmOutputBadRestoredfifth,
       "upsTrapAlarmOutputOverloadRestoredfifth": upsTrapAlarmOutputOverloadRestoredfifth,
       "upsTrapAlarmOnBypassRestoredfifth": upsTrapAlarmOnBypassRestoredfifth,
       "upsTrapAlarmBypassBadRestoredfifth": upsTrapAlarmBypassBadRestoredfifth,
       "upsTrapAlarmOutputOffAsRequestedRestoredfifth": upsTrapAlarmOutputOffAsRequestedRestoredfifth,
       "upsTrapAlarmUpsOffAsRequestedRestoredfifth": upsTrapAlarmUpsOffAsRequestedRestoredfifth,
       "upsTrapAlarmChargerFailedRestoredfifth": upsTrapAlarmChargerFailedRestoredfifth,
       "upsTrapAlarmUpsOutputOnfifth": upsTrapAlarmUpsOutputOnfifth,
       "upsTrapAlarmUpsSystemOnfifth": upsTrapAlarmUpsSystemOnfifth,
       "upsTrapAlarmFanFailureRestoredfifth": upsTrapAlarmFanFailureRestoredfifth,
       "upsTrapAlarmFuseFailureRestoredfifth": upsTrapAlarmFuseFailureRestoredfifth,
       "upsTrapAlarmGeneralFaultRestoredfifth": upsTrapAlarmGeneralFaultRestoredfifth,
       "upsTrapAlarmDiagnosticTestFailedRestoredfifth": upsTrapAlarmDiagnosticTestFailedRestoredfifth,
       "upsTrapAlarmCommunicationsLostRestoredfifth": upsTrapAlarmCommunicationsLostRestoredfifth,
       "upsTrapAlarmAwaitingPowerRestoredfifth": upsTrapAlarmAwaitingPowerRestoredfifth,
       "upsTrapAlarmShutdownPendingRestoredfifth": upsTrapAlarmShutdownPendingRestoredfifth,
       "upsTrapAlarmShutdownImminentRestoredfifth": upsTrapAlarmShutdownImminentRestoredfifth,
       "upsTrapAlarmTestInProgressRestoredfifth": upsTrapAlarmTestInProgressRestoredfifth,
       "upsTrapAlarmReceptacleOnfifth": upsTrapAlarmReceptacleOnfifth,
       "upsTrapAlarmHighspeedBusRestorefifth": upsTrapAlarmHighspeedBusRestorefifth,
       "upsTrapAlarmHighspeedBusJACRCRestorefifth": upsTrapAlarmHighspeedBusJACRCRestorefifth,
       "upsTrapAlarmConnectivityBusRestorefifth": upsTrapAlarmConnectivityBusRestorefifth,
       "upsTrapAlarmHighspeedBusJBCRCRestoredfifth": upsTrapAlarmHighspeedBusJBCRCRestoredfifth,
       "upsTrapAlarmCurrentSharingRestoredfifth": upsTrapAlarmCurrentSharingRestoredfifth,
       "upsTrapAlarmDCRippleRestoredfifth": upsTrapAlarmDCRippleRestoredfifth,
       "upsTrapAlarmValueLowfifth": upsTrapAlarmValueLowfifth,
       "upsTrapAlarmValueHighfifth": upsTrapAlarmValueHighfifth,
       "upsTrapAlarmValueLowRestoredfifth": upsTrapAlarmValueLowRestoredfifth,
       "upsTrapAlarmValueHighRestoredfifth": upsTrapAlarmValueHighRestoredfifth,
       "upsDiagnosticfifth": upsDiagnosticfifth,
       "upsDiagnosticBusJACommunicationStatusfifth": upsDiagnosticBusJACommunicationStatusfifth,
       "upsDiagnosticBusJBCommunicationStatusfifth": upsDiagnosticBusJBCommunicationStatusfifth,
       "upsDiagnosticBatteryLifetimefifth": upsDiagnosticBatteryLifetimefifth,
       "upsDiagnosticFansLifetimefifth": upsDiagnosticFansLifetimefifth,
       "upsDiagnosticDCcapacitorsLifetimefifth": upsDiagnosticDCcapacitorsLifetimefifth,
       "upsDiagnosticACcapacitorsLifetimefifth": upsDiagnosticACcapacitorsLifetimefifth,
       "upsDiagnosticGlobalServiceCheckfifth": upsDiagnosticGlobalServiceCheckfifth,
       "geSixthUPS": geSixthUPS,
       "upsIdentsixth": upsIdentsixth,
       "upsIdentManufacturersixth": upsIdentManufacturersixth,
       "upsIdentModelsixth": upsIdentModelsixth,
       "upsIdentUPSSoftwareVersionsixth": upsIdentUPSSoftwareVersionsixth,
       "upsIdentAgentSoftwareVersionsixth": upsIdentAgentSoftwareVersionsixth,
       "upsIdentNamesixth": upsIdentNamesixth,
       "upsIdentAttachedDevicessixth": upsIdentAttachedDevicessixth,
       "upsIdentUPSSerialNumbersixth": upsIdentUPSSerialNumbersixth,
       "upsIdentComProtVersionsixth": upsIdentComProtVersionsixth,
       "upsIdentOperatingTimesixth": upsIdentOperatingTimesixth,
       "upsBatterysixth": upsBatterysixth,
       "upsBatteryStatussixth": upsBatteryStatussixth,
       "upsSecondsOnBatterysixth": upsSecondsOnBatterysixth,
       "upsEstimatedMinutesRemainingsixth": upsEstimatedMinutesRemainingsixth,
       "upsEstimatedChargeRemainingsixth": upsEstimatedChargeRemainingsixth,
       "upsBatteryVoltagesixth": upsBatteryVoltagesixth,
       "upsBatteryCurrentsixth": upsBatteryCurrentsixth,
       "upsBatteryTemperaturesixth": upsBatteryTemperaturesixth,
       "upsBatteryRipplesixth": upsBatteryRipplesixth,
       "upsInputsixth": upsInputsixth,
       "upsInputLineBadssixth": upsInputLineBadssixth,
       "upsInputNumLinessixth": upsInputNumLinessixth,
       "upsInputSixthTable": upsInputSixthTable,
       "upsInputSixthEntry": upsInputSixthEntry,
       "upsInputLineIndexsixth": upsInputLineIndexsixth,
       "upsInputFrequencysixth": upsInputFrequencysixth,
       "upsInputVoltagesixth": upsInputVoltagesixth,
       "upsInputCurrentsixth": upsInputCurrentsixth,
       "upsInputTruePowersixth": upsInputTruePowersixth,
       "upsInputVoltageMinsixth": upsInputVoltageMinsixth,
       "upsInputVoltageMaxsixth": upsInputVoltageMaxsixth,
       "upsOutputsixth": upsOutputsixth,
       "upsOutputSourcesixth": upsOutputSourcesixth,
       "upsOutputFrequencysixth": upsOutputFrequencysixth,
       "upsOutputNumLinessixth": upsOutputNumLinessixth,
       "upsOutputSixthTable": upsOutputSixthTable,
       "upsOutputSixthEntry": upsOutputSixthEntry,
       "upsOutputLineIndexsixth": upsOutputLineIndexsixth,
       "upsOutputVoltagesixth": upsOutputVoltagesixth,
       "upsOutputCurrentsixth": upsOutputCurrentsixth,
       "upsOutputPowersixth": upsOutputPowersixth,
       "upsOutputPercentLoadsixth": upsOutputPercentLoadsixth,
       "upsOutputPowerFactorsixth": upsOutputPowerFactorsixth,
       "upsOutputPeakCurrentsixth": upsOutputPeakCurrentsixth,
       "upsOutputShareCurrentsixth": upsOutputShareCurrentsixth,
       "upsBypasssixth": upsBypasssixth,
       "upsBypassFrequencysixth": upsBypassFrequencysixth,
       "upsBypassNumLinessixth": upsBypassNumLinessixth,
       "upsBypassSixthTable": upsBypassSixthTable,
       "upsBypassSixthEntry": upsBypassSixthEntry,
       "upsBypassLineIndexsixth": upsBypassLineIndexsixth,
       "upsBypassVoltagesixth": upsBypassVoltagesixth,
       "upsBypassCurrentsixth": upsBypassCurrentsixth,
       "upsBypassPowersixth": upsBypassPowersixth,
       "upsAlarmsixth": upsAlarmsixth,
       "upsAlarmsPresentsixth": upsAlarmsPresentsixth,
       "upsAlarmSixthTable": upsAlarmSixthTable,
       "upsAlarmSixthEntry": upsAlarmSixthEntry,
       "upsAlarmIdsixth": upsAlarmIdsixth,
       "upsAlarmDescrsixth": upsAlarmDescrsixth,
       "upsAlarmTimesixth": upsAlarmTimesixth,
       "upsWellKnownAlarmssixth": upsWellKnownAlarmssixth,
       "upsAlarmBatteryBadsixth": upsAlarmBatteryBadsixth,
       "upsAlarmOnBatterysixth": upsAlarmOnBatterysixth,
       "upsAlarmLowBatterysixth": upsAlarmLowBatterysixth,
       "upsAlarmDepletedBatterysixth": upsAlarmDepletedBatterysixth,
       "upsAlarmTempBadsixth": upsAlarmTempBadsixth,
       "upsAlarmInputBadsixth": upsAlarmInputBadsixth,
       "upsAlarmOutputBadsixth": upsAlarmOutputBadsixth,
       "upsAlarmOutputOverloadsixth": upsAlarmOutputOverloadsixth,
       "upsAlarmOnBypasssixth": upsAlarmOnBypasssixth,
       "upsAlarmBypassBadsixth": upsAlarmBypassBadsixth,
       "upsAlarmOutputOffAsRequestedsixth": upsAlarmOutputOffAsRequestedsixth,
       "upsAlarmUpsOffAsRequestedsixth": upsAlarmUpsOffAsRequestedsixth,
       "upsAlarmChargerFailedsixth": upsAlarmChargerFailedsixth,
       "upsAlarmUpsOutputOffsixth": upsAlarmUpsOutputOffsixth,
       "upsAlarmUpsSystemOffsixth": upsAlarmUpsSystemOffsixth,
       "upsAlarmFanFailuresixth": upsAlarmFanFailuresixth,
       "upsAlarmFuseFailuresixth": upsAlarmFuseFailuresixth,
       "upsAlarmGeneralFaultsixth": upsAlarmGeneralFaultsixth,
       "upsAlarmDiagnosticTestFailedsixth": upsAlarmDiagnosticTestFailedsixth,
       "upsAlarmCommunicationsLostsixth": upsAlarmCommunicationsLostsixth,
       "upsAlarmAwaitingPowersixth": upsAlarmAwaitingPowersixth,
       "upsAlarmShutdownPendingsixth": upsAlarmShutdownPendingsixth,
       "upsAlarmShutdownImminentsixth": upsAlarmShutdownImminentsixth,
       "upsAlarmTestInProgresssixth": upsAlarmTestInProgresssixth,
       "upsAlarmReceptacleOffsixth": upsAlarmReceptacleOffsixth,
       "upsAlarmHighSpeedBusFailuresixth": upsAlarmHighSpeedBusFailuresixth,
       "upsAlarmHighSpeedBusJACRCFailuresixth": upsAlarmHighSpeedBusJACRCFailuresixth,
       "upsAlarmConnectivityBusFailuresixth": upsAlarmConnectivityBusFailuresixth,
       "upsAlarmHighSpeedBusJBCRCFailuresixth": upsAlarmHighSpeedBusJBCRCFailuresixth,
       "upsAlarmCurrentSharingsixth": upsAlarmCurrentSharingsixth,
       "upsAlarmDCRipplesixth": upsAlarmDCRipplesixth,
       "upsAlarmMaskAsixth": upsAlarmMaskAsixth,
       "upsTestsixth": upsTestsixth,
       "upsTestIdsixth": upsTestIdsixth,
       "upsTestSpinLocksixth": upsTestSpinLocksixth,
       "upsTestResultsSummarysixth": upsTestResultsSummarysixth,
       "upsTestResultsDetailsixth": upsTestResultsDetailsixth,
       "upsTestStartTimesixth": upsTestStartTimesixth,
       "upsTestElapsedTimesixth": upsTestElapsedTimesixth,
       "upsWellKnownTestssixth": upsWellKnownTestssixth,
       "upsTestNoTestsInitiatedsixth": upsTestNoTestsInitiatedsixth,
       "upsTestAbortTestInProgresssixth": upsTestAbortTestInProgresssixth,
       "upsTestGeneralSystemsTestsixth": upsTestGeneralSystemsTestsixth,
       "upsTestQuickBatteryTestsixth": upsTestQuickBatteryTestsixth,
       "upsTestDeepBatteryCalibrationsixth": upsTestDeepBatteryCalibrationsixth,
       "upsControlsixth": upsControlsixth,
       "upsShutdownTypesixth": upsShutdownTypesixth,
       "upsShutdownAfterDelaysixth": upsShutdownAfterDelaysixth,
       "upsStartupAfterDelaysixth": upsStartupAfterDelaysixth,
       "upsRebootWithDurationsixth": upsRebootWithDurationsixth,
       "upsAutoRestartsixth": upsAutoRestartsixth,
       "upsReceptaclesNumsixth": upsReceptaclesNumsixth,
       "upsReceptacleSixthTable": upsReceptacleSixthTable,
       "upsReceptacleSixthEntry": upsReceptacleSixthEntry,
       "upsReceptacleLineIndexsixth": upsReceptacleLineIndexsixth,
       "upsReceptacleOnOffsixth": upsReceptacleOnOffsixth,
       "upsUPSModesixth": upsUPSModesixth,
       "upsRectifierOnOffsixth": upsRectifierOnOffsixth,
       "upsBatteryChargeMethodsixth": upsBatteryChargeMethodsixth,
       "upsInverterOnOffsixth": upsInverterOnOffsixth,
       "upsBypassOnOffsixth": upsBypassOnOffsixth,
       "upsLoadSourcesixth": upsLoadSourcesixth,
       "upsConfigsixth": upsConfigsixth,
       "upsConfigInputVoltagesixth": upsConfigInputVoltagesixth,
       "upsConfigInputFreqsixth": upsConfigInputFreqsixth,
       "upsConfigOutputVoltagesixth": upsConfigOutputVoltagesixth,
       "upsConfigOutputFreqsixth": upsConfigOutputFreqsixth,
       "upsConfigOutputVAsixth": upsConfigOutputVAsixth,
       "upsConfigOutputPowersixth": upsConfigOutputPowersixth,
       "upsConfigLowBattTimesixth": upsConfigLowBattTimesixth,
       "upsConfigAudibleStatussixth": upsConfigAudibleStatussixth,
       "upsConfigLowVoltageTransferPointsixth": upsConfigLowVoltageTransferPointsixth,
       "upsConfigHighVoltageTransferPointsixth": upsConfigHighVoltageTransferPointsixth,
       "upsConfigBatteryCapacitysixth": upsConfigBatteryCapacitysixth,
       "upsConfigBatteryChargeCurrentsixth": upsConfigBatteryChargeCurrentsixth,
       "upsConfigNoLoadShutdownsixth": upsConfigNoLoadShutdownsixth,
       "upsConfigStartDelaysixth": upsConfigStartDelaysixth,
       "upsGetSetsixth": upsGetSetsixth,
       "upsEventGetNextsixth": upsEventGetNextsixth,
       "upsEventGetPrevioussixth": upsEventGetPrevioussixth,
       "upsEventSetStartingTimeStampsixth": upsEventSetStartingTimeStampsixth,
       "upsEventRetreiveCurrentTimeStampsixth": upsEventRetreiveCurrentTimeStampsixth,
       "upsEventTableSizesixth": upsEventTableSizesixth,
       "upsEventSixthTable": upsEventSixthTable,
       "upsEventSixthEntry": upsEventSixthEntry,
       "upsEventLineIndexsixth": upsEventLineIndexsixth,
       "upsEventCodesixth": upsEventCodesixth,
       "upsEventStatussixth": upsEventStatussixth,
       "upsEventTimesixth": upsEventTimesixth,
       "upsParametersReadsixth": upsParametersReadsixth,
       "upsParametersWritesixth": upsParametersWritesixth,
       "upsParametersStartAddresssixth": upsParametersStartAddresssixth,
       "upsParameterTableSizesixth": upsParameterTableSizesixth,
       "upsParameterSixthTable": upsParameterSixthTable,
       "upsParameterSixthEntry": upsParameterSixthEntry,
       "upsParameterLineIndexsixth": upsParameterLineIndexsixth,
       "upsParameterValuesixth": upsParameterValuesixth,
       "upsStatussixth": upsStatussixth,
       "upsMainsStatisticsMBfailsixth": upsMainsStatisticsMBfailsixth,
       "upsMainsStatisticsMRfailsixth": upsMainsStatisticsMRfailsixth,
       "upsMainsStatisticsB2sixth": upsMainsStatisticsB2sixth,
       "upsMainsStatisticsB5sixth": upsMainsStatisticsB5sixth,
       "upsMainsStatisticsB10sixth": upsMainsStatisticsB10sixth,
       "upsMainsStatisticsB200sixth": upsMainsStatisticsB200sixth,
       "upsMainsStatisticsBypRelsixth": upsMainsStatisticsBypRelsixth,
       "upsTimesixth": upsTimesixth,
       "upsRequestPermissionsixth": upsRequestPermissionsixth,
       "upsEventGetCodesixth": upsEventGetCodesixth,
       "upsEventSpinLocksixth": upsEventSpinLocksixth,
       "upsParameterSpinLocksixth": upsParameterSpinLocksixth,
       "geUPSTrapssixth": geUPSTrapssixth,
       "upsTrapAlarmBatteryBadsixth": upsTrapAlarmBatteryBadsixth,
       "upsTrapAlarmOnBatterysixth": upsTrapAlarmOnBatterysixth,
       "upsTrapAlarmLowBatterysixth": upsTrapAlarmLowBatterysixth,
       "upsTrapAlarmDepletedBatterysixth": upsTrapAlarmDepletedBatterysixth,
       "upsTrapAlarmTempBadsixth": upsTrapAlarmTempBadsixth,
       "upsTrapAlarmInputBadsixth": upsTrapAlarmInputBadsixth,
       "upsTrapAlarmOutputBadsixth": upsTrapAlarmOutputBadsixth,
       "upsTrapAlarmOutputOverloadsixth": upsTrapAlarmOutputOverloadsixth,
       "upsTrapAlarmOnBypasssixth": upsTrapAlarmOnBypasssixth,
       "upsTrapAlarmBypassBadsixth": upsTrapAlarmBypassBadsixth,
       "upsTrapAlarmOutputOffAsRequestedsixth": upsTrapAlarmOutputOffAsRequestedsixth,
       "upsTrapAlarmUpsOffAsRequestedsixth": upsTrapAlarmUpsOffAsRequestedsixth,
       "upsTrapAlarmChargerFailedsixth": upsTrapAlarmChargerFailedsixth,
       "upsTrapAlarmUpsOutputOffsixth": upsTrapAlarmUpsOutputOffsixth,
       "upsTrapAlarmUpsSystemOffsixth": upsTrapAlarmUpsSystemOffsixth,
       "upsTrapAlarmFanFailuresixth": upsTrapAlarmFanFailuresixth,
       "upsTrapAlarmFuseFailuresixth": upsTrapAlarmFuseFailuresixth,
       "upsTrapAlarmGeneralFaultsixth": upsTrapAlarmGeneralFaultsixth,
       "upsTrapAlarmDiagnosticTestFailedsixth": upsTrapAlarmDiagnosticTestFailedsixth,
       "upsTrapAlarmCommunicationsLostsixth": upsTrapAlarmCommunicationsLostsixth,
       "upsTrapAlarmAwaitingPowersixth": upsTrapAlarmAwaitingPowersixth,
       "upsTrapAlarmShutdownPendingsixth": upsTrapAlarmShutdownPendingsixth,
       "upsTrapAlarmShutdownImminentsixth": upsTrapAlarmShutdownImminentsixth,
       "upsTrapAlarmTestInProgresssixth": upsTrapAlarmTestInProgresssixth,
       "upsTrapAlarmReceptacleOffsixth": upsTrapAlarmReceptacleOffsixth,
       "upsTrapAlarmHighspeedBusFailuresixth": upsTrapAlarmHighspeedBusFailuresixth,
       "upsTrapAlarmHighspeedBusJACRCFailuresixth": upsTrapAlarmHighspeedBusJACRCFailuresixth,
       "upsTrapAlarmConnectivityBusFailuresixth": upsTrapAlarmConnectivityBusFailuresixth,
       "upsTrapAlarmHighspeedBusJBCRCFailuresixth": upsTrapAlarmHighspeedBusJBCRCFailuresixth,
       "upsTrapAlarmCurrentSharingFailuresixth": upsTrapAlarmCurrentSharingFailuresixth,
       "upsTrapAlarmDCRippleFailuresixth": upsTrapAlarmDCRippleFailuresixth,
       "upsTrapAlarmBatteryBadRestoredsixth": upsTrapAlarmBatteryBadRestoredsixth,
       "upsTrapAlarmOnBatteryRestoredsixth": upsTrapAlarmOnBatteryRestoredsixth,
       "upsTrapAlarmLowBatteryRestoredsixth": upsTrapAlarmLowBatteryRestoredsixth,
       "upsTrapAlarmDepletedBatteryRestoredsixth": upsTrapAlarmDepletedBatteryRestoredsixth,
       "upsTrapAlarmTempBadRestoredsixth": upsTrapAlarmTempBadRestoredsixth,
       "upsTrapAlarmInputBadRestoredsixth": upsTrapAlarmInputBadRestoredsixth,
       "upsTrapAlarmOutputBadRestoredsixth": upsTrapAlarmOutputBadRestoredsixth,
       "upsTrapAlarmOutputOverloadRestoredsixth": upsTrapAlarmOutputOverloadRestoredsixth,
       "upsTrapAlarmOnBypassRestoredsixth": upsTrapAlarmOnBypassRestoredsixth,
       "upsTrapAlarmBypassBadRestoredsixth": upsTrapAlarmBypassBadRestoredsixth,
       "upsTrapAlarmOutputOffAsRequestedRestoredsixth": upsTrapAlarmOutputOffAsRequestedRestoredsixth,
       "upsTrapAlarmUpsOffAsRequestedRestoredsixth": upsTrapAlarmUpsOffAsRequestedRestoredsixth,
       "upsTrapAlarmChargerFailedRestoredsixth": upsTrapAlarmChargerFailedRestoredsixth,
       "upsTrapAlarmUpsOutputOnsixth": upsTrapAlarmUpsOutputOnsixth,
       "upsTrapAlarmUpsSystemOnsixth": upsTrapAlarmUpsSystemOnsixth,
       "upsTrapAlarmFanFailureRestoredsixth": upsTrapAlarmFanFailureRestoredsixth,
       "upsTrapAlarmFuseFailureRestoredsixth": upsTrapAlarmFuseFailureRestoredsixth,
       "upsTrapAlarmGeneralFaultRestoredsixth": upsTrapAlarmGeneralFaultRestoredsixth,
       "upsTrapAlarmDiagnosticTestFailedRestoredsixth": upsTrapAlarmDiagnosticTestFailedRestoredsixth,
       "upsTrapAlarmCommunicationsLostRestoredsixth": upsTrapAlarmCommunicationsLostRestoredsixth,
       "upsTrapAlarmAwaitingPowerRestoredsixth": upsTrapAlarmAwaitingPowerRestoredsixth,
       "upsTrapAlarmShutdownPendingRestoredsixth": upsTrapAlarmShutdownPendingRestoredsixth,
       "upsTrapAlarmShutdownImminentRestoredsixth": upsTrapAlarmShutdownImminentRestoredsixth,
       "upsTrapAlarmTestInProgressRestoredsixth": upsTrapAlarmTestInProgressRestoredsixth,
       "upsTrapAlarmReceptacleOnsixth": upsTrapAlarmReceptacleOnsixth,
       "upsTrapAlarmHighspeedBusRestoresixth": upsTrapAlarmHighspeedBusRestoresixth,
       "upsTrapAlarmHighspeedBusJACRCRestoresixth": upsTrapAlarmHighspeedBusJACRCRestoresixth,
       "upsTrapAlarmConnectivityBusRestoresixth": upsTrapAlarmConnectivityBusRestoresixth,
       "upsTrapAlarmHighspeedBusJBCRCRestoredsixth": upsTrapAlarmHighspeedBusJBCRCRestoredsixth,
       "upsTrapAlarmCurrentSharingRestoredsixth": upsTrapAlarmCurrentSharingRestoredsixth,
       "upsTrapAlarmDCRippleRestoredsixth": upsTrapAlarmDCRippleRestoredsixth,
       "upsTrapAlarmValueLowsixth": upsTrapAlarmValueLowsixth,
       "upsTrapAlarmValueHighsixth": upsTrapAlarmValueHighsixth,
       "upsTrapAlarmValueLowRestoredsixth": upsTrapAlarmValueLowRestoredsixth,
       "upsTrapAlarmValueHighRestoredsixth": upsTrapAlarmValueHighRestoredsixth,
       "upsDiagnosticsixth": upsDiagnosticsixth,
       "upsDiagnosticBusJACommunicationStatussixth": upsDiagnosticBusJACommunicationStatussixth,
       "upsDiagnosticBusJBCommunicationStatussixth": upsDiagnosticBusJBCommunicationStatussixth,
       "upsDiagnosticBatteryLifetimesixth": upsDiagnosticBatteryLifetimesixth,
       "upsDiagnosticFansLifetimesixth": upsDiagnosticFansLifetimesixth,
       "upsDiagnosticDCcapacitorsLifetimesixth": upsDiagnosticDCcapacitorsLifetimesixth,
       "upsDiagnosticACcapacitorsLifetimesixth": upsDiagnosticACcapacitorsLifetimesixth,
       "upsDiagnosticGlobalServiceChecksixth": upsDiagnosticGlobalServiceChecksixth,
       "geSeventhUPS": geSeventhUPS,
       "upsIdentseventh": upsIdentseventh,
       "upsIdentManufacturerseventh": upsIdentManufacturerseventh,
       "upsIdentModelseventh": upsIdentModelseventh,
       "upsIdentUPSSoftwareVersionseventh": upsIdentUPSSoftwareVersionseventh,
       "upsIdentAgentSoftwareVersionseventh": upsIdentAgentSoftwareVersionseventh,
       "upsIdentNameseventh": upsIdentNameseventh,
       "upsIdentAttachedDevicesseventh": upsIdentAttachedDevicesseventh,
       "upsIdentUPSSerialNumberseventh": upsIdentUPSSerialNumberseventh,
       "upsIdentComProtVersionseventh": upsIdentComProtVersionseventh,
       "upsIdentOperatingTimeseventh": upsIdentOperatingTimeseventh,
       "upsBatteryseventh": upsBatteryseventh,
       "upsBatteryStatusseventh": upsBatteryStatusseventh,
       "upsSecondsOnBatteryseventh": upsSecondsOnBatteryseventh,
       "upsEstimatedMinutesRemainingseventh": upsEstimatedMinutesRemainingseventh,
       "upsEstimatedChargeRemainingseventh": upsEstimatedChargeRemainingseventh,
       "upsBatteryVoltageseventh": upsBatteryVoltageseventh,
       "upsBatteryCurrentseventh": upsBatteryCurrentseventh,
       "upsBatteryTemperatureseventh": upsBatteryTemperatureseventh,
       "upsBatteryRippleseventh": upsBatteryRippleseventh,
       "upsInputseventh": upsInputseventh,
       "upsInputLineBadsseventh": upsInputLineBadsseventh,
       "upsInputNumLinesseventh": upsInputNumLinesseventh,
       "upsInputSeventhTable": upsInputSeventhTable,
       "upsInputSeventhEntry": upsInputSeventhEntry,
       "upsInputLineIndexseventh": upsInputLineIndexseventh,
       "upsInputFrequencyseventh": upsInputFrequencyseventh,
       "upsInputVoltageseventh": upsInputVoltageseventh,
       "upsInputCurrentseventh": upsInputCurrentseventh,
       "upsInputTruePowerseventh": upsInputTruePowerseventh,
       "upsInputVoltageMinseventh": upsInputVoltageMinseventh,
       "upsInputVoltageMaxseventh": upsInputVoltageMaxseventh,
       "upsOutputseventh": upsOutputseventh,
       "upsOutputSourceseventh": upsOutputSourceseventh,
       "upsOutputFrequencyseventh": upsOutputFrequencyseventh,
       "upsOutputNumLinesseventh": upsOutputNumLinesseventh,
       "upsOutputSeventhTable": upsOutputSeventhTable,
       "upsOutputSeventhEntry": upsOutputSeventhEntry,
       "upsOutputLineIndexseventh": upsOutputLineIndexseventh,
       "upsOutputVoltageseventh": upsOutputVoltageseventh,
       "upsOutputCurrentseventh": upsOutputCurrentseventh,
       "upsOutputPowerseventh": upsOutputPowerseventh,
       "upsOutputPercentLoadseventh": upsOutputPercentLoadseventh,
       "upsOutputPowerFactorseventh": upsOutputPowerFactorseventh,
       "upsOutputPeakCurrentseventh": upsOutputPeakCurrentseventh,
       "upsOutputShareCurrentseventh": upsOutputShareCurrentseventh,
       "upsBypassseventh": upsBypassseventh,
       "upsBypassFrequencyseventh": upsBypassFrequencyseventh,
       "upsBypassNumLinesseventh": upsBypassNumLinesseventh,
       "upsBypassSeventhTable": upsBypassSeventhTable,
       "upsBypassSeventhEntry": upsBypassSeventhEntry,
       "upsBypassLineIndexseventh": upsBypassLineIndexseventh,
       "upsBypassVoltageseventh": upsBypassVoltageseventh,
       "upsBypassCurrentseventh": upsBypassCurrentseventh,
       "upsBypassPowerseventh": upsBypassPowerseventh,
       "upsAlarmseventh": upsAlarmseventh,
       "upsAlarmsPresentseventh": upsAlarmsPresentseventh,
       "upsAlarmSeventhTable": upsAlarmSeventhTable,
       "upsAlarmSeventhEntry": upsAlarmSeventhEntry,
       "upsAlarmIdseventh": upsAlarmIdseventh,
       "upsAlarmDescrseventh": upsAlarmDescrseventh,
       "upsAlarmTimeseventh": upsAlarmTimeseventh,
       "upsWellKnownAlarmsseventh": upsWellKnownAlarmsseventh,
       "upsAlarmBatteryBadseventh": upsAlarmBatteryBadseventh,
       "upsAlarmOnBatteryseventh": upsAlarmOnBatteryseventh,
       "upsAlarmLowBatteryseventh": upsAlarmLowBatteryseventh,
       "upsAlarmDepletedBatteryseventh": upsAlarmDepletedBatteryseventh,
       "upsAlarmTempBadseventh": upsAlarmTempBadseventh,
       "upsAlarmInputBadseventh": upsAlarmInputBadseventh,
       "upsAlarmOutputBadseventh": upsAlarmOutputBadseventh,
       "upsAlarmOutputOverloadseventh": upsAlarmOutputOverloadseventh,
       "upsAlarmOnBypassseventh": upsAlarmOnBypassseventh,
       "upsAlarmBypassBadseventh": upsAlarmBypassBadseventh,
       "upsAlarmOutputOffAsRequestedseventh": upsAlarmOutputOffAsRequestedseventh,
       "upsAlarmUpsOffAsRequestedseventh": upsAlarmUpsOffAsRequestedseventh,
       "upsAlarmChargerFailedseventh": upsAlarmChargerFailedseventh,
       "upsAlarmUpsOutputOffseventh": upsAlarmUpsOutputOffseventh,
       "upsAlarmUpsSystemOffseventh": upsAlarmUpsSystemOffseventh,
       "upsAlarmFanFailureseventh": upsAlarmFanFailureseventh,
       "upsAlarmFuseFailureseventh": upsAlarmFuseFailureseventh,
       "upsAlarmGeneralFaultseventh": upsAlarmGeneralFaultseventh,
       "upsAlarmDiagnosticTestFailedseventh": upsAlarmDiagnosticTestFailedseventh,
       "upsAlarmCommunicationsLostseventh": upsAlarmCommunicationsLostseventh,
       "upsAlarmAwaitingPowerseventh": upsAlarmAwaitingPowerseventh,
       "upsAlarmShutdownPendingseventh": upsAlarmShutdownPendingseventh,
       "upsAlarmShutdownImminentseventh": upsAlarmShutdownImminentseventh,
       "upsAlarmTestInProgressseventh": upsAlarmTestInProgressseventh,
       "upsAlarmReceptacleOffseventh": upsAlarmReceptacleOffseventh,
       "upsAlarmHighSpeedBusFailureseventh": upsAlarmHighSpeedBusFailureseventh,
       "upsAlarmHighSpeedBusJACRCFailureseventh": upsAlarmHighSpeedBusJACRCFailureseventh,
       "upsAlarmConnectivityBusFailureseventh": upsAlarmConnectivityBusFailureseventh,
       "upsAlarmHighSpeedBusJBCRCFailureseventh": upsAlarmHighSpeedBusJBCRCFailureseventh,
       "upsAlarmCurrentSharingseventh": upsAlarmCurrentSharingseventh,
       "upsAlarmDCRippleseventh": upsAlarmDCRippleseventh,
       "upsAlarmMaskAseventh": upsAlarmMaskAseventh,
       "upsTestseventh": upsTestseventh,
       "upsTestIdseventh": upsTestIdseventh,
       "upsTestSpinLockseventh": upsTestSpinLockseventh,
       "upsTestResultsSummaryseventh": upsTestResultsSummaryseventh,
       "upsTestResultsDetailseventh": upsTestResultsDetailseventh,
       "upsTestStartTimeseventh": upsTestStartTimeseventh,
       "upsTestElapsedTimeseventh": upsTestElapsedTimeseventh,
       "upsWellKnownTestsseventh": upsWellKnownTestsseventh,
       "upsTestNoTestsInitiatedseventh": upsTestNoTestsInitiatedseventh,
       "upsTestAbortTestInProgressseventh": upsTestAbortTestInProgressseventh,
       "upsTestGeneralSystemsTestseventh": upsTestGeneralSystemsTestseventh,
       "upsTestQuickBatteryTestseventh": upsTestQuickBatteryTestseventh,
       "upsTestDeepBatteryCalibrationseventh": upsTestDeepBatteryCalibrationseventh,
       "upsControlseventh": upsControlseventh,
       "upsShutdownTypeseventh": upsShutdownTypeseventh,
       "upsShutdownAfterDelayseventh": upsShutdownAfterDelayseventh,
       "upsStartupAfterDelayseventh": upsStartupAfterDelayseventh,
       "upsRebootWithDurationseventh": upsRebootWithDurationseventh,
       "upsAutoRestartseventh": upsAutoRestartseventh,
       "upsReceptaclesNumseventh": upsReceptaclesNumseventh,
       "upsReceptacleSeventhTable": upsReceptacleSeventhTable,
       "upsReceptacleSeventhEntry": upsReceptacleSeventhEntry,
       "upsReceptacleLineIndexseventh": upsReceptacleLineIndexseventh,
       "upsReceptacleOnOffseventh": upsReceptacleOnOffseventh,
       "upsUPSModeseventh": upsUPSModeseventh,
       "upsRectifierOnOffseventh": upsRectifierOnOffseventh,
       "upsBatteryChargeMethodseventh": upsBatteryChargeMethodseventh,
       "upsInverterOnOffseventh": upsInverterOnOffseventh,
       "upsBypassOnOffseventh": upsBypassOnOffseventh,
       "upsLoadSourceseventh": upsLoadSourceseventh,
       "upsConfigseventh": upsConfigseventh,
       "upsConfigInputVoltageseventh": upsConfigInputVoltageseventh,
       "upsConfigInputFreqseventh": upsConfigInputFreqseventh,
       "upsConfigOutputVoltageseventh": upsConfigOutputVoltageseventh,
       "upsConfigOutputFreqseventh": upsConfigOutputFreqseventh,
       "upsConfigOutputVAseventh": upsConfigOutputVAseventh,
       "upsConfigOutputPowerseventh": upsConfigOutputPowerseventh,
       "upsConfigLowBattTimeseventh": upsConfigLowBattTimeseventh,
       "upsConfigAudibleStatusseventh": upsConfigAudibleStatusseventh,
       "upsConfigLowVoltageTransferPointseventh": upsConfigLowVoltageTransferPointseventh,
       "upsConfigHighVoltageTransferPointseventh": upsConfigHighVoltageTransferPointseventh,
       "upsConfigBatteryCapacityseventh": upsConfigBatteryCapacityseventh,
       "upsConfigBatteryChargeCurrentseventh": upsConfigBatteryChargeCurrentseventh,
       "upsConfigNoLoadShutdownseventh": upsConfigNoLoadShutdownseventh,
       "upsConfigStartDelayseventh": upsConfigStartDelayseventh,
       "upsGetSetseventh": upsGetSetseventh,
       "upsEventGetNextseventh": upsEventGetNextseventh,
       "upsEventGetPreviousseventh": upsEventGetPreviousseventh,
       "upsEventSetStartingTimeStampseventh": upsEventSetStartingTimeStampseventh,
       "upsEventRetreiveCurrentTimeStampseventh": upsEventRetreiveCurrentTimeStampseventh,
       "upsEventTableSizeseventh": upsEventTableSizeseventh,
       "upsEventSeventhTable": upsEventSeventhTable,
       "upsEventSeventhEntry": upsEventSeventhEntry,
       "upsEventLineIndexseventh": upsEventLineIndexseventh,
       "upsEventCodeseventh": upsEventCodeseventh,
       "upsEventStatusseventh": upsEventStatusseventh,
       "upsEventTimeseventh": upsEventTimeseventh,
       "upsParametersReadseventh": upsParametersReadseventh,
       "upsParametersWriteseventh": upsParametersWriteseventh,
       "upsParametersStartAddressseventh": upsParametersStartAddressseventh,
       "upsParameterTableSizeseventh": upsParameterTableSizeseventh,
       "upsParameterSeventhTable": upsParameterSeventhTable,
       "upsParameterSeventhEntry": upsParameterSeventhEntry,
       "upsParameterLineIndexseventh": upsParameterLineIndexseventh,
       "upsParameterValueseventh": upsParameterValueseventh,
       "upsStatusseventh": upsStatusseventh,
       "upsMainsStatisticsMBfailseventh": upsMainsStatisticsMBfailseventh,
       "upsMainsStatisticsMRfailseventh": upsMainsStatisticsMRfailseventh,
       "upsMainsStatisticsB2seventh": upsMainsStatisticsB2seventh,
       "upsMainsStatisticsB5seventh": upsMainsStatisticsB5seventh,
       "upsMainsStatisticsB10seventh": upsMainsStatisticsB10seventh,
       "upsMainsStatisticsB200seventh": upsMainsStatisticsB200seventh,
       "upsMainsStatisticsBypRelseventh": upsMainsStatisticsBypRelseventh,
       "upsTimeseventh": upsTimeseventh,
       "upsRequestPermissionseventh": upsRequestPermissionseventh,
       "upsEventGetCodeseventh": upsEventGetCodeseventh,
       "upsEventSpinLockseventh": upsEventSpinLockseventh,
       "upsParameterSpinLockseventh": upsParameterSpinLockseventh,
       "geUPSTrapsseventh": geUPSTrapsseventh,
       "upsTrapAlarmBatteryBadseventh": upsTrapAlarmBatteryBadseventh,
       "upsTrapAlarmOnBatteryseventh": upsTrapAlarmOnBatteryseventh,
       "upsTrapAlarmLowBatteryseventh": upsTrapAlarmLowBatteryseventh,
       "upsTrapAlarmDepletedBatteryseventh": upsTrapAlarmDepletedBatteryseventh,
       "upsTrapAlarmTempBadseventh": upsTrapAlarmTempBadseventh,
       "upsTrapAlarmInputBadseventh": upsTrapAlarmInputBadseventh,
       "upsTrapAlarmOutputBadseventh": upsTrapAlarmOutputBadseventh,
       "upsTrapAlarmOutputOverloadseventh": upsTrapAlarmOutputOverloadseventh,
       "upsTrapAlarmOnBypassseventh": upsTrapAlarmOnBypassseventh,
       "upsTrapAlarmBypassBadseventh": upsTrapAlarmBypassBadseventh,
       "upsTrapAlarmOutputOffAsRequestedseventh": upsTrapAlarmOutputOffAsRequestedseventh,
       "upsTrapAlarmUpsOffAsRequestedseventh": upsTrapAlarmUpsOffAsRequestedseventh,
       "upsTrapAlarmChargerFailedseventh": upsTrapAlarmChargerFailedseventh,
       "upsTrapAlarmUpsOutputOffseventh": upsTrapAlarmUpsOutputOffseventh,
       "upsTrapAlarmUpsSystemOffseventh": upsTrapAlarmUpsSystemOffseventh,
       "upsTrapAlarmFanFailureseventh": upsTrapAlarmFanFailureseventh,
       "upsTrapAlarmFuseFailureseventh": upsTrapAlarmFuseFailureseventh,
       "upsTrapAlarmGeneralFaultseventh": upsTrapAlarmGeneralFaultseventh,
       "upsTrapAlarmDiagnosticTestFailedseventh": upsTrapAlarmDiagnosticTestFailedseventh,
       "upsTrapAlarmCommunicationsLostseventh": upsTrapAlarmCommunicationsLostseventh,
       "upsTrapAlarmAwaitingPowerseventh": upsTrapAlarmAwaitingPowerseventh,
       "upsTrapAlarmShutdownPendingseventh": upsTrapAlarmShutdownPendingseventh,
       "upsTrapAlarmShutdownImminentseventh": upsTrapAlarmShutdownImminentseventh,
       "upsTrapAlarmTestInProgressseventh": upsTrapAlarmTestInProgressseventh,
       "upsTrapAlarmReceptacleOffseventh": upsTrapAlarmReceptacleOffseventh,
       "upsTrapAlarmHighspeedBusFailureseventh": upsTrapAlarmHighspeedBusFailureseventh,
       "upsTrapAlarmHighspeedBusJACRCFailureseventh": upsTrapAlarmHighspeedBusJACRCFailureseventh,
       "upsTrapAlarmConnectivityBusFailureseventh": upsTrapAlarmConnectivityBusFailureseventh,
       "upsTrapAlarmHighspeedBusJBCRCFailureseventh": upsTrapAlarmHighspeedBusJBCRCFailureseventh,
       "upsTrapAlarmCurrentSharingFailureseventh": upsTrapAlarmCurrentSharingFailureseventh,
       "upsTrapAlarmDCRippleFailureseventh": upsTrapAlarmDCRippleFailureseventh,
       "upsTrapAlarmBatteryBadRestoredseventh": upsTrapAlarmBatteryBadRestoredseventh,
       "upsTrapAlarmOnBatteryRestoredseventh": upsTrapAlarmOnBatteryRestoredseventh,
       "upsTrapAlarmLowBatteryRestoredseventh": upsTrapAlarmLowBatteryRestoredseventh,
       "upsTrapAlarmDepletedBatteryRestoredseventh": upsTrapAlarmDepletedBatteryRestoredseventh,
       "upsTrapAlarmTempBadRestoredseventh": upsTrapAlarmTempBadRestoredseventh,
       "upsTrapAlarmInputBadRestoredseventh": upsTrapAlarmInputBadRestoredseventh,
       "upsTrapAlarmOutputBadRestoredseventh": upsTrapAlarmOutputBadRestoredseventh,
       "upsTrapAlarmOutputOverloadRestoredseventh": upsTrapAlarmOutputOverloadRestoredseventh,
       "upsTrapAlarmOnBypassRestoredseventh": upsTrapAlarmOnBypassRestoredseventh,
       "upsTrapAlarmBypassBadRestoredseventh": upsTrapAlarmBypassBadRestoredseventh,
       "upsTrapAlarmOutputOffAsRequestedRestoredseventh": upsTrapAlarmOutputOffAsRequestedRestoredseventh,
       "upsTrapAlarmUpsOffAsRequestedRestoredseventh": upsTrapAlarmUpsOffAsRequestedRestoredseventh,
       "upsTrapAlarmChargerFailedRestoredseventh": upsTrapAlarmChargerFailedRestoredseventh,
       "upsTrapAlarmUpsOutputOnseventh": upsTrapAlarmUpsOutputOnseventh,
       "upsTrapAlarmUpsSystemOnseventh": upsTrapAlarmUpsSystemOnseventh,
       "upsTrapAlarmFanFailureRestoredseventh": upsTrapAlarmFanFailureRestoredseventh,
       "upsTrapAlarmFuseFailureRestoredseventh": upsTrapAlarmFuseFailureRestoredseventh,
       "upsTrapAlarmGeneralFaultRestoredseventh": upsTrapAlarmGeneralFaultRestoredseventh,
       "upsTrapAlarmDiagnosticTestFailedRestoredseventh": upsTrapAlarmDiagnosticTestFailedRestoredseventh,
       "upsTrapAlarmCommunicationsLostRestoredseventh": upsTrapAlarmCommunicationsLostRestoredseventh,
       "upsTrapAlarmAwaitingPowerRestoredseventh": upsTrapAlarmAwaitingPowerRestoredseventh,
       "upsTrapAlarmShutdownPendingRestoredseventh": upsTrapAlarmShutdownPendingRestoredseventh,
       "upsTrapAlarmShutdownImminentRestoredseventh": upsTrapAlarmShutdownImminentRestoredseventh,
       "upsTrapAlarmTestInProgressRestoredseventh": upsTrapAlarmTestInProgressRestoredseventh,
       "upsTrapAlarmReceptacleOnseventh": upsTrapAlarmReceptacleOnseventh,
       "upsTrapAlarmHighspeedBusRestoreseventh": upsTrapAlarmHighspeedBusRestoreseventh,
       "upsTrapAlarmHighspeedBusJACRCRestoreseventh": upsTrapAlarmHighspeedBusJACRCRestoreseventh,
       "upsTrapAlarmConnectivityBusRestoreseventh": upsTrapAlarmConnectivityBusRestoreseventh,
       "upsTrapAlarmHighspeedBusJBCRCRestoredseventh": upsTrapAlarmHighspeedBusJBCRCRestoredseventh,
       "upsTrapAlarmCurrentSharingRestoredseventh": upsTrapAlarmCurrentSharingRestoredseventh,
       "upsTrapAlarmDCRippleRestoredseventh": upsTrapAlarmDCRippleRestoredseventh,
       "upsTrapAlarmValueLowseventh": upsTrapAlarmValueLowseventh,
       "upsTrapAlarmValueHighseventh": upsTrapAlarmValueHighseventh,
       "upsTrapAlarmValueLowRestoredseventh": upsTrapAlarmValueLowRestoredseventh,
       "upsTrapAlarmValueHighRestoredseventh": upsTrapAlarmValueHighRestoredseventh,
       "upsDiagnosticseventh": upsDiagnosticseventh,
       "upsDiagnosticBusJACommunicationStatusseventh": upsDiagnosticBusJACommunicationStatusseventh,
       "upsDiagnosticBusJBCommunicationStatusseventh": upsDiagnosticBusJBCommunicationStatusseventh,
       "upsDiagnosticBatteryLifetimeseventh": upsDiagnosticBatteryLifetimeseventh,
       "upsDiagnosticFansLifetimeseventh": upsDiagnosticFansLifetimeseventh,
       "upsDiagnosticDCcapacitorsLifetimeseventh": upsDiagnosticDCcapacitorsLifetimeseventh,
       "upsDiagnosticACcapacitorsLifetimeseventh": upsDiagnosticACcapacitorsLifetimeseventh,
       "upsDiagnosticGlobalServiceCheckseventh": upsDiagnosticGlobalServiceCheckseventh,
       "geEighthUPS": geEighthUPS,
       "upsIdenteighth": upsIdenteighth,
       "upsIdentManufacturereighth": upsIdentManufacturereighth,
       "upsIdentModeleighth": upsIdentModeleighth,
       "upsIdentUPSSoftwareVersioneighth": upsIdentUPSSoftwareVersioneighth,
       "upsIdentAgentSoftwareVersioneighth": upsIdentAgentSoftwareVersioneighth,
       "upsIdentNameeighth": upsIdentNameeighth,
       "upsIdentAttachedDeviceseighth": upsIdentAttachedDeviceseighth,
       "upsIdentUPSSerialNumbereighth": upsIdentUPSSerialNumbereighth,
       "upsIdentComProtVersioneighth": upsIdentComProtVersioneighth,
       "upsIdentOperatingTimeeighth": upsIdentOperatingTimeeighth,
       "upsBatteryeighth": upsBatteryeighth,
       "upsBatteryStatuseighth": upsBatteryStatuseighth,
       "upsSecondsOnBatteryeighth": upsSecondsOnBatteryeighth,
       "upsEstimatedMinutesRemainingeighth": upsEstimatedMinutesRemainingeighth,
       "upsEstimatedChargeRemainingeighth": upsEstimatedChargeRemainingeighth,
       "upsBatteryVoltageeighth": upsBatteryVoltageeighth,
       "upsBatteryCurrenteighth": upsBatteryCurrenteighth,
       "upsBatteryTemperatureeighth": upsBatteryTemperatureeighth,
       "upsBatteryRippleeighth": upsBatteryRippleeighth,
       "upsInputeighth": upsInputeighth,
       "upsInputLineBadseighth": upsInputLineBadseighth,
       "upsInputNumLineseighth": upsInputNumLineseighth,
       "upsInputEighthTable": upsInputEighthTable,
       "upsInputEighthEntry": upsInputEighthEntry,
       "upsInputLineIndexeighth": upsInputLineIndexeighth,
       "upsInputFrequencyeighth": upsInputFrequencyeighth,
       "upsInputVoltageeighth": upsInputVoltageeighth,
       "upsInputCurrenteighth": upsInputCurrenteighth,
       "upsInputTruePowereighth": upsInputTruePowereighth,
       "upsInputVoltageMineighth": upsInputVoltageMineighth,
       "upsInputVoltageMaxeighth": upsInputVoltageMaxeighth,
       "upsOutputeighth": upsOutputeighth,
       "upsOutputSourceeighth": upsOutputSourceeighth,
       "upsOutputFrequencyeighth": upsOutputFrequencyeighth,
       "upsOutputNumLineseighth": upsOutputNumLineseighth,
       "upsOutputEighthTable": upsOutputEighthTable,
       "upsOutputEighthEntry": upsOutputEighthEntry,
       "upsOutputLineIndexeighth": upsOutputLineIndexeighth,
       "upsOutputVoltageeighth": upsOutputVoltageeighth,
       "upsOutputCurrenteighth": upsOutputCurrenteighth,
       "upsOutputPowereighth": upsOutputPowereighth,
       "upsOutputPercentLoadeighth": upsOutputPercentLoadeighth,
       "upsOutputPowerFactoreighth": upsOutputPowerFactoreighth,
       "upsOutputPeakCurrenteighth": upsOutputPeakCurrenteighth,
       "upsOutputShareCurrenteighth": upsOutputShareCurrenteighth,
       "upsBypasseighth": upsBypasseighth,
       "upsBypassFrequencyeighth": upsBypassFrequencyeighth,
       "upsBypassNumLineseighth": upsBypassNumLineseighth,
       "upsBypassEighthTable": upsBypassEighthTable,
       "upsBypassEighthEntry": upsBypassEighthEntry,
       "upsBypassLineIndexeighth": upsBypassLineIndexeighth,
       "upsBypassVoltageeighth": upsBypassVoltageeighth,
       "upsBypassCurrenteighth": upsBypassCurrenteighth,
       "upsBypassPowereighth": upsBypassPowereighth,
       "upsAlarmeighth": upsAlarmeighth,
       "upsAlarmsPresenteighth": upsAlarmsPresenteighth,
       "upsAlarmEighthTable": upsAlarmEighthTable,
       "upsAlarmEighthEntry": upsAlarmEighthEntry,
       "upsAlarmIdeighth": upsAlarmIdeighth,
       "upsAlarmDescreighth": upsAlarmDescreighth,
       "upsAlarmTimeeighth": upsAlarmTimeeighth,
       "upsWellKnownAlarmseighth": upsWellKnownAlarmseighth,
       "upsAlarmBatteryBadeighth": upsAlarmBatteryBadeighth,
       "upsAlarmOnBatteryeighth": upsAlarmOnBatteryeighth,
       "upsAlarmLowBatteryeighth": upsAlarmLowBatteryeighth,
       "upsAlarmDepletedBatteryeighth": upsAlarmDepletedBatteryeighth,
       "upsAlarmTempBadeighth": upsAlarmTempBadeighth,
       "upsAlarmInputBadeighth": upsAlarmInputBadeighth,
       "upsAlarmOutputBadeighth": upsAlarmOutputBadeighth,
       "upsAlarmOutputOverloadeighth": upsAlarmOutputOverloadeighth,
       "upsAlarmOnBypasseighth": upsAlarmOnBypasseighth,
       "upsAlarmBypassBadeighth": upsAlarmBypassBadeighth,
       "upsAlarmOutputOffAsRequestedeighth": upsAlarmOutputOffAsRequestedeighth,
       "upsAlarmUpsOffAsRequestedeighth": upsAlarmUpsOffAsRequestedeighth,
       "upsAlarmChargerFailedeighth": upsAlarmChargerFailedeighth,
       "upsAlarmUpsOutputOffeighth": upsAlarmUpsOutputOffeighth,
       "upsAlarmUpsSystemOffeighth": upsAlarmUpsSystemOffeighth,
       "upsAlarmFanFailureeighth": upsAlarmFanFailureeighth,
       "upsAlarmFuseFailureeighth": upsAlarmFuseFailureeighth,
       "upsAlarmGeneralFaulteighth": upsAlarmGeneralFaulteighth,
       "upsAlarmDiagnosticTestFailedeighth": upsAlarmDiagnosticTestFailedeighth,
       "upsAlarmCommunicationsLosteighth": upsAlarmCommunicationsLosteighth,
       "upsAlarmAwaitingPowereighth": upsAlarmAwaitingPowereighth,
       "upsAlarmShutdownPendingeighth": upsAlarmShutdownPendingeighth,
       "upsAlarmShutdownImminenteighth": upsAlarmShutdownImminenteighth,
       "upsAlarmTestInProgresseighth": upsAlarmTestInProgresseighth,
       "upsAlarmReceptacleOffeighth": upsAlarmReceptacleOffeighth,
       "upsAlarmHighSpeedBusFailureeighth": upsAlarmHighSpeedBusFailureeighth,
       "upsAlarmHighSpeedBusJACRCFailureeighth": upsAlarmHighSpeedBusJACRCFailureeighth,
       "upsAlarmConnectivityBusFailureeighth": upsAlarmConnectivityBusFailureeighth,
       "upsAlarmHighSpeedBusJBCRCFailureeighth": upsAlarmHighSpeedBusJBCRCFailureeighth,
       "upsAlarmCurrentSharingeighth": upsAlarmCurrentSharingeighth,
       "upsAlarmDCRippleeighth": upsAlarmDCRippleeighth,
       "upsAlarmMaskAeighth": upsAlarmMaskAeighth,
       "upsTesteighth": upsTesteighth,
       "upsTestIdeighth": upsTestIdeighth,
       "upsTestSpinLockeighth": upsTestSpinLockeighth,
       "upsTestResultsSummaryeighth": upsTestResultsSummaryeighth,
       "upsTestResultsDetaileighth": upsTestResultsDetaileighth,
       "upsTestStartTimeeighth": upsTestStartTimeeighth,
       "upsTestElapsedTimeeighth": upsTestElapsedTimeeighth,
       "upsWellKnownTestseighth": upsWellKnownTestseighth,
       "upsTestNoTestsInitiatedeighth": upsTestNoTestsInitiatedeighth,
       "upsTestAbortTestInProgresseighth": upsTestAbortTestInProgresseighth,
       "upsTestGeneralSystemsTesteighth": upsTestGeneralSystemsTesteighth,
       "upsTestQuickBatteryTesteighth": upsTestQuickBatteryTesteighth,
       "upsTestDeepBatteryCalibrationeighth": upsTestDeepBatteryCalibrationeighth,
       "upsControleighth": upsControleighth,
       "upsShutdownTypeeighth": upsShutdownTypeeighth,
       "upsShutdownAfterDelayeighth": upsShutdownAfterDelayeighth,
       "upsStartupAfterDelayeighth": upsStartupAfterDelayeighth,
       "upsRebootWithDurationeighth": upsRebootWithDurationeighth,
       "upsAutoRestarteighth": upsAutoRestarteighth,
       "upsReceptaclesNumeighth": upsReceptaclesNumeighth,
       "upsReceptacleEighthTable": upsReceptacleEighthTable,
       "upsReceptacleEighthEntry": upsReceptacleEighthEntry,
       "upsReceptacleLineIndexeighth": upsReceptacleLineIndexeighth,
       "upsReceptacleOnOffeighth": upsReceptacleOnOffeighth,
       "upsUPSModeeighth": upsUPSModeeighth,
       "upsRectifierOnOffeighth": upsRectifierOnOffeighth,
       "upsBatteryChargeMethodeighth": upsBatteryChargeMethodeighth,
       "upsInverterOnOffeighth": upsInverterOnOffeighth,
       "upsBypassOnOffeighth": upsBypassOnOffeighth,
       "upsLoadSourceeighth": upsLoadSourceeighth,
       "upsConfigeighth": upsConfigeighth,
       "upsConfigInputVoltageeighth": upsConfigInputVoltageeighth,
       "upsConfigInputFreqeighth": upsConfigInputFreqeighth,
       "upsConfigOutputVoltageeighth": upsConfigOutputVoltageeighth,
       "upsConfigOutputFreqeighth": upsConfigOutputFreqeighth,
       "upsConfigOutputVAeighth": upsConfigOutputVAeighth,
       "upsConfigOutputPowereighth": upsConfigOutputPowereighth,
       "upsConfigLowBattTimeeighth": upsConfigLowBattTimeeighth,
       "upsConfigAudibleStatuseighth": upsConfigAudibleStatuseighth,
       "upsConfigLowVoltageTransferPointeighth": upsConfigLowVoltageTransferPointeighth,
       "upsConfigHighVoltageTransferPointeighth": upsConfigHighVoltageTransferPointeighth,
       "upsConfigBatteryCapacityeighth": upsConfigBatteryCapacityeighth,
       "upsConfigBatteryChargeCurrenteighth": upsConfigBatteryChargeCurrenteighth,
       "upsConfigNoLoadShutdowneighth": upsConfigNoLoadShutdowneighth,
       "upsConfigStartDelayeighth": upsConfigStartDelayeighth,
       "upsGetSeteighth": upsGetSeteighth,
       "upsEventGetNexteighth": upsEventGetNexteighth,
       "upsEventGetPreviouseighth": upsEventGetPreviouseighth,
       "upsEventSetStartingTimeStampeighth": upsEventSetStartingTimeStampeighth,
       "upsEventRetreiveCurrentTimeStampeighth": upsEventRetreiveCurrentTimeStampeighth,
       "upsEventTableSizeeighth": upsEventTableSizeeighth,
       "upsEventEighthTable": upsEventEighthTable,
       "upsEventEighthEntry": upsEventEighthEntry,
       "upsEventLineIndexeighth": upsEventLineIndexeighth,
       "upsEventCodeeighth": upsEventCodeeighth,
       "upsEventStatuseighth": upsEventStatuseighth,
       "upsEventTimeeighth": upsEventTimeeighth,
       "upsParametersReadeighth": upsParametersReadeighth,
       "upsParametersWriteeighth": upsParametersWriteeighth,
       "upsParametersStartAddresseighth": upsParametersStartAddresseighth,
       "upsParameterTableSizeeighth": upsParameterTableSizeeighth,
       "upsParameterEighthTable": upsParameterEighthTable,
       "upsParameterEighthEntry": upsParameterEighthEntry,
       "upsParameterLineIndexeighth": upsParameterLineIndexeighth,
       "upsParameterValueeighth": upsParameterValueeighth,
       "upsStatuseighth": upsStatuseighth,
       "upsMainsStatisticsMBfaileighth": upsMainsStatisticsMBfaileighth,
       "upsMainsStatisticsMRfaileighth": upsMainsStatisticsMRfaileighth,
       "upsMainsStatisticsB2eighth": upsMainsStatisticsB2eighth,
       "upsMainsStatisticsB5eighth": upsMainsStatisticsB5eighth,
       "upsMainsStatisticsB10eighth": upsMainsStatisticsB10eighth,
       "upsMainsStatisticsB200eighth": upsMainsStatisticsB200eighth,
       "upsMainsStatisticsBypReleighth": upsMainsStatisticsBypReleighth,
       "upsTimeeighth": upsTimeeighth,
       "upsRequestPermissioneighth": upsRequestPermissioneighth,
       "upsEventGetCodeeighth": upsEventGetCodeeighth,
       "upsEventSpinLockeighth": upsEventSpinLockeighth,
       "upsParameterSpinLockeighth": upsParameterSpinLockeighth,
       "geUPSTrapseighth": geUPSTrapseighth,
       "upsTrapAlarmBatteryBadeighth": upsTrapAlarmBatteryBadeighth,
       "upsTrapAlarmOnBatteryeighth": upsTrapAlarmOnBatteryeighth,
       "upsTrapAlarmLowBatteryeighth": upsTrapAlarmLowBatteryeighth,
       "upsTrapAlarmDepletedBatteryeighth": upsTrapAlarmDepletedBatteryeighth,
       "upsTrapAlarmTempBadeighth": upsTrapAlarmTempBadeighth,
       "upsTrapAlarmInputBadeighth": upsTrapAlarmInputBadeighth,
       "upsTrapAlarmOutputBadeighth": upsTrapAlarmOutputBadeighth,
       "upsTrapAlarmOutputOverloadeighth": upsTrapAlarmOutputOverloadeighth,
       "upsTrapAlarmOnBypasseighth": upsTrapAlarmOnBypasseighth,
       "upsTrapAlarmBypassBadeighth": upsTrapAlarmBypassBadeighth,
       "upsTrapAlarmOutputOffAsRequestedeighth": upsTrapAlarmOutputOffAsRequestedeighth,
       "upsTrapAlarmUpsOffAsRequestedeighth": upsTrapAlarmUpsOffAsRequestedeighth,
       "upsTrapAlarmChargerFailedeighth": upsTrapAlarmChargerFailedeighth,
       "upsTrapAlarmUpsOutputOffeighth": upsTrapAlarmUpsOutputOffeighth,
       "upsTrapAlarmUpsSystemOffeighth": upsTrapAlarmUpsSystemOffeighth,
       "upsTrapAlarmFanFailureeighth": upsTrapAlarmFanFailureeighth,
       "upsTrapAlarmFuseFailureeighth": upsTrapAlarmFuseFailureeighth,
       "upsTrapAlarmGeneralFaulteighth": upsTrapAlarmGeneralFaulteighth,
       "upsTrapAlarmDiagnosticTestFailedeighth": upsTrapAlarmDiagnosticTestFailedeighth,
       "upsTrapAlarmCommunicationsLosteighth": upsTrapAlarmCommunicationsLosteighth,
       "upsTrapAlarmAwaitingPowereighth": upsTrapAlarmAwaitingPowereighth,
       "upsTrapAlarmShutdownPendingeighth": upsTrapAlarmShutdownPendingeighth,
       "upsTrapAlarmShutdownImminenteighth": upsTrapAlarmShutdownImminenteighth,
       "upsTrapAlarmTestInProgresseighth": upsTrapAlarmTestInProgresseighth,
       "upsTrapAlarmReceptacleOffeighth": upsTrapAlarmReceptacleOffeighth,
       "upsTrapAlarmHighspeedBusFailureeighth": upsTrapAlarmHighspeedBusFailureeighth,
       "upsTrapAlarmHighspeedBusJACRCFailureeighth": upsTrapAlarmHighspeedBusJACRCFailureeighth,
       "upsTrapAlarmConnectivityBusFailureeighth": upsTrapAlarmConnectivityBusFailureeighth,
       "upsTrapAlarmHighspeedBusJBCRCFailureeighth": upsTrapAlarmHighspeedBusJBCRCFailureeighth,
       "upsTrapAlarmCurrentSharingFailureeighth": upsTrapAlarmCurrentSharingFailureeighth,
       "upsTrapAlarmDCRippleFailureeighth": upsTrapAlarmDCRippleFailureeighth,
       "upsTrapAlarmBatteryBadRestoredeighth": upsTrapAlarmBatteryBadRestoredeighth,
       "upsTrapAlarmOnBatteryRestoredeighth": upsTrapAlarmOnBatteryRestoredeighth,
       "upsTrapAlarmLowBatteryRestoredeighth": upsTrapAlarmLowBatteryRestoredeighth,
       "upsTrapAlarmDepletedBatteryRestoredeighth": upsTrapAlarmDepletedBatteryRestoredeighth,
       "upsTrapAlarmTempBadRestoredeighth": upsTrapAlarmTempBadRestoredeighth,
       "upsTrapAlarmInputBadRestoredeighth": upsTrapAlarmInputBadRestoredeighth,
       "upsTrapAlarmOutputBadRestoredeighth": upsTrapAlarmOutputBadRestoredeighth,
       "upsTrapAlarmOutputOverloadRestoredeighth": upsTrapAlarmOutputOverloadRestoredeighth,
       "upsTrapAlarmOnBypassRestoredeighth": upsTrapAlarmOnBypassRestoredeighth,
       "upsTrapAlarmBypassBadRestoredeighth": upsTrapAlarmBypassBadRestoredeighth,
       "upsTrapAlarmOutputOffAsRequestedRestoredeighth": upsTrapAlarmOutputOffAsRequestedRestoredeighth,
       "upsTrapAlarmUpsOffAsRequestedRestoredeighth": upsTrapAlarmUpsOffAsRequestedRestoredeighth,
       "upsTrapAlarmChargerFailedRestoredeighth": upsTrapAlarmChargerFailedRestoredeighth,
       "upsTrapAlarmUpsOutputOneighth": upsTrapAlarmUpsOutputOneighth,
       "upsTrapAlarmUpsSystemOneighth": upsTrapAlarmUpsSystemOneighth,
       "upsTrapAlarmFanFailureRestoredeighth": upsTrapAlarmFanFailureRestoredeighth,
       "upsTrapAlarmFuseFailureRestoredeighth": upsTrapAlarmFuseFailureRestoredeighth,
       "upsTrapAlarmGeneralFaultRestoredeighth": upsTrapAlarmGeneralFaultRestoredeighth,
       "upsTrapAlarmDiagnosticTestFailedRestoredeighth": upsTrapAlarmDiagnosticTestFailedRestoredeighth,
       "upsTrapAlarmCommunicationsLostRestoredeighth": upsTrapAlarmCommunicationsLostRestoredeighth,
       "upsTrapAlarmAwaitingPowerRestoredeighth": upsTrapAlarmAwaitingPowerRestoredeighth,
       "upsTrapAlarmShutdownPendingRestoredeighth": upsTrapAlarmShutdownPendingRestoredeighth,
       "upsTrapAlarmShutdownImminentRestoredeighth": upsTrapAlarmShutdownImminentRestoredeighth,
       "upsTrapAlarmTestInProgressRestoredeighth": upsTrapAlarmTestInProgressRestoredeighth,
       "upsTrapAlarmReceptacleOneighth": upsTrapAlarmReceptacleOneighth,
       "upsTrapAlarmHighspeedBusRestoreeighth": upsTrapAlarmHighspeedBusRestoreeighth,
       "upsTrapAlarmHighspeedBusJACRCRestoreeighth": upsTrapAlarmHighspeedBusJACRCRestoreeighth,
       "upsTrapAlarmConnectivityBusRestoreeighth": upsTrapAlarmConnectivityBusRestoreeighth,
       "upsTrapAlarmHighspeedBusJBCRCRestoredeighth": upsTrapAlarmHighspeedBusJBCRCRestoredeighth,
       "upsTrapAlarmCurrentSharingRestoredeighth": upsTrapAlarmCurrentSharingRestoredeighth,
       "upsTrapAlarmDCRippleRestoredeighth": upsTrapAlarmDCRippleRestoredeighth,
       "upsTrapAlarmValueLoweighth": upsTrapAlarmValueLoweighth,
       "upsTrapAlarmValueHigheighth": upsTrapAlarmValueHigheighth,
       "upsTrapAlarmValueLowRestoredeighth": upsTrapAlarmValueLowRestoredeighth,
       "upsTrapAlarmValueHighRestoredeighth": upsTrapAlarmValueHighRestoredeighth,
       "upsDiagnosticeighth": upsDiagnosticeighth,
       "upsDiagnosticBusJACommunicationStatuseighth": upsDiagnosticBusJACommunicationStatuseighth,
       "upsDiagnosticBusJBCommunicationStatuseighth": upsDiagnosticBusJBCommunicationStatuseighth,
       "upsDiagnosticBatteryLifetimeeighth": upsDiagnosticBatteryLifetimeeighth,
       "upsDiagnosticFansLifetimeeighth": upsDiagnosticFansLifetimeeighth,
       "upsDiagnosticDCcapacitorsLifetimeeighth": upsDiagnosticDCcapacitorsLifetimeeighth,
       "upsDiagnosticACcapacitorsLifetimeeighth": upsDiagnosticACcapacitorsLifetimeeighth,
       "upsDiagnosticGlobalServiceCheckeighth": upsDiagnosticGlobalServiceCheckeighth,
       "geDevices": geDevices,
       "geDevicesDescriptions": geDevicesDescriptions,
       "advSNMPWebIntCard": advSNMPWebIntCard,
       "snmpWebIntCard": snmpWebIntCard,
       "snmpWebIntBox": snmpWebIntBox}
)
