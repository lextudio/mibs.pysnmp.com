# SNMP MIB module (SDEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SDEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:11 2024
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

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

schleifenbauer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31034)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DeciAmps(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class DeciCelsius(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class DeciPowerFactor(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class DeciValue(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class DeciVolts(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class KiloWattHour(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class MilliSeconds(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class Seconds(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_Device0_ObjectIdentity = ObjectIdentity
device0 = _Device0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 2)
)
_Identification_ObjectIdentity = ObjectIdentity
identification = _Identification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3)
)


class _SpdmVersion_Type(Integer32):
    """Custom type spdmVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_SpdmVersion_Type.__name__ = "Integer32"
_SpdmVersion_Object = MibTableColumn
spdmVersion = _SpdmVersion_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 1),
    _SpdmVersion_Type()
)
spdmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spdmVersion.setStatus("current")


class _FirmwareVersion_Type(Integer32):
    """Custom type firmwareVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_FirmwareVersion_Type.__name__ = "Integer32"
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 2),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_BuildNumber_Type = DisplayString
_BuildNumber_Object = MibScalar
buildNumber = _BuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 3),
    _BuildNumber_Type()
)
buildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildNumber.setStatus("current")
_SalesOrderNumber_Type = DisplayString
_SalesOrderNumber_Object = MibTableColumn
salesOrderNumber = _SalesOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 4),
    _SalesOrderNumber_Type()
)
salesOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salesOrderNumber.setStatus("current")
_ProductId_Type = DisplayString
_ProductId_Object = MibTableColumn
productId = _ProductId_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 5),
    _ProductId_Type()
)
productId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productId.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 6),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_HardwareAddress_Type = DisplayString
_HardwareAddress_Object = MibTableColumn
hardwareAddress = _HardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 7),
    _HardwareAddress_Type()
)
hardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareAddress.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 8),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _UnitAddress_Type(Integer32):
    """Custom type unitAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UnitAddress_Type.__name__ = "Integer32"
_UnitAddress_Object = MibTableColumn
unitAddress = _UnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 9),
    _UnitAddress_Type()
)
unitAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitAddress.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 10),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceLocation_Type = DisplayString
_DeviceLocation_Object = MibScalar
deviceLocation = _DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 11),
    _DeviceLocation_Type()
)
deviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceLocation.setStatus("current")
_VanityTag_Type = DisplayString
_VanityTag_Object = MibScalar
vanityTag = _VanityTag_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 3, 12),
    _VanityTag_Type()
)
vanityTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vanityTag.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 2, 4)
)


class _NoPhases_Type(Integer32):
    """Custom type noPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NoPhases_Type.__name__ = "Integer32"
_NoPhases_Object = MibTableColumn
noPhases = _NoPhases_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 4, 1),
    _NoPhases_Type()
)
noPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noPhases.setStatus("current")


class _NoOutletsTotal_Type(Integer32):
    """Custom type noOutletsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_NoOutletsTotal_Type.__name__ = "Integer32"
_NoOutletsTotal_Object = MibTableColumn
noOutletsTotal = _NoOutletsTotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 4, 2),
    _NoOutletsTotal_Type()
)
noOutletsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noOutletsTotal.setStatus("current")


class _NoSwitchedOutlets_Type(Integer32):
    """Custom type noSwitchedOutlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_NoSwitchedOutlets_Type.__name__ = "Integer32"
_NoSwitchedOutlets_Object = MibTableColumn
noSwitchedOutlets = _NoSwitchedOutlets_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 4, 3),
    _NoSwitchedOutlets_Type()
)
noSwitchedOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noSwitchedOutlets.setStatus("current")


class _NoMeasuredOutlets_Type(Integer32):
    """Custom type noMeasuredOutlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_NoMeasuredOutlets_Type.__name__ = "Integer32"
_NoMeasuredOutlets_Object = MibTableColumn
noMeasuredOutlets = _NoMeasuredOutlets_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 4, 4),
    _NoMeasuredOutlets_Type()
)
noMeasuredOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noMeasuredOutlets.setStatus("current")


class _NoSensors_Type(Integer32):
    """Custom type noSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_NoSensors_Type.__name__ = "Integer32"
_NoSensors_Object = MibScalar
noSensors = _NoSensors_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 4, 5),
    _NoSensors_Type()
)
noSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noSensors.setStatus("current")


class _MaximumLoad_Type(Integer32):
    """Custom type maximumLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MaximumLoad_Type.__name__ = "Integer32"
_MaximumLoad_Object = MibTableColumn
maximumLoad = _MaximumLoad_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 4, 6),
    _MaximumLoad_Type()
)
maximumLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumLoad.setStatus("current")
_Systemstatus_ObjectIdentity = ObjectIdentity
systemstatus = _Systemstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5)
)


class _DeviceStatusCode_Type(Integer32):
    """Custom type deviceStatusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DeviceStatusCode_Type.__name__ = "Integer32"
_DeviceStatusCode_Object = MibTableColumn
deviceStatusCode = _DeviceStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5, 1),
    _DeviceStatusCode_Type()
)
deviceStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceStatusCode.setStatus("current")


class _TemperatureAlert_Type(Integer32):
    """Custom type temperatureAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TemperatureAlert_Type.__name__ = "Integer32"
_TemperatureAlert_Object = MibTableColumn
temperatureAlert = _TemperatureAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5, 2),
    _TemperatureAlert_Type()
)
temperatureAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAlert.setStatus("current")


class _InputCurrentAlert_Type(Integer32):
    """Custom type inputCurrentAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_InputCurrentAlert_Type.__name__ = "Integer32"
_InputCurrentAlert_Object = MibTableColumn
inputCurrentAlert = _InputCurrentAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5, 3),
    _InputCurrentAlert_Type()
)
inputCurrentAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentAlert.setStatus("current")


class _OutputCurrentAlert_Type(Integer32):
    """Custom type outputCurrentAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_OutputCurrentAlert_Type.__name__ = "Integer32"
_OutputCurrentAlert_Object = MibTableColumn
outputCurrentAlert = _OutputCurrentAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5, 4),
    _OutputCurrentAlert_Type()
)
outputCurrentAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrentAlert.setStatus("current")


class _InputVoltageAlert_Type(Integer32):
    """Custom type inputVoltageAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_InputVoltageAlert_Type.__name__ = "Integer32"
_InputVoltageAlert_Object = MibTableColumn
inputVoltageAlert = _InputVoltageAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5, 5),
    _InputVoltageAlert_Type()
)
inputVoltageAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageAlert.setStatus("current")


class _OCurrentDropAlert_Type(Integer32):
    """Custom type oCurrentDropAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 103),
    )


_OCurrentDropAlert_Type.__name__ = "Integer32"
_OCurrentDropAlert_Object = MibTableColumn
oCurrentDropAlert = _OCurrentDropAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5, 6),
    _OCurrentDropAlert_Type()
)
oCurrentDropAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCurrentDropAlert.setStatus("current")


class _ICurrentDropAlert_Type(Integer32):
    """Custom type iCurrentDropAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ICurrentDropAlert_Type.__name__ = "Integer32"
_ICurrentDropAlert_Object = MibTableColumn
iCurrentDropAlert = _ICurrentDropAlert_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 5, 7),
    _ICurrentDropAlert_Type()
)
iCurrentDropAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iCurrentDropAlert.setStatus("current")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 2, 6)
)
_RebootDevice_Type = Integer32
_RebootDevice_Object = MibScalar
rebootDevice = _RebootDevice_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 6, 1),
    _RebootDevice_Type()
)
rebootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootDevice.setStatus("current")
_ResetAlerts_Type = Integer32
_ResetAlerts_Object = MibScalar
resetAlerts = _ResetAlerts_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 6, 2),
    _ResetAlerts_Type()
)
resetAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAlerts.setStatus("current")
_ZeroInputKWhSubtotal_Type = Integer32
_ZeroInputKWhSubtotal_Object = MibScalar
zeroInputKWhSubtotal = _ZeroInputKWhSubtotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 6, 3),
    _ZeroInputKWhSubtotal_Type()
)
zeroInputKWhSubtotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zeroInputKWhSubtotal.setStatus("current")
_ZeroOutKWhSubtotal_Type = Integer32
_ZeroOutKWhSubtotal_Object = MibScalar
zeroOutKWhSubtotal = _ZeroOutKWhSubtotal_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 6, 4),
    _ZeroOutKWhSubtotal_Type()
)
zeroOutKWhSubtotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zeroOutKWhSubtotal.setStatus("current")
_ResetPeakValues_Type = Integer32
_ResetPeakValues_Object = MibScalar
resetPeakValues = _ResetPeakValues_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 6, 5),
    _ResetPeakValues_Type()
)
resetPeakValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetPeakValues.setStatus("current")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1)
)
_PeakDuration_Type = MilliSeconds
_PeakDuration_Object = MibScalar
peakDuration = _PeakDuration_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 4),
    _PeakDuration_Type()
)
peakDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakDuration.setStatus("current")
_FixedOutletDelay_Type = MilliSeconds
_FixedOutletDelay_Object = MibScalar
fixedOutletDelay = _FixedOutletDelay_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 5),
    _FixedOutletDelay_Type()
)
fixedOutletDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fixedOutletDelay.setStatus("current")
_PowerSaverMode_Type = Seconds
_PowerSaverMode_Object = MibScalar
powerSaverMode = _PowerSaverMode_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 6),
    _PowerSaverMode_Type()
)
powerSaverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSaverMode.setStatus("current")


class _OutletPowerupMode_Type(Integer32):
    """Custom type outletPowerupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OutletPowerupMode_Type.__name__ = "Integer32"
_OutletPowerupMode_Object = MibScalar
outletPowerupMode = _OutletPowerupMode_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 7),
    _OutletPowerupMode_Type()
)
outletPowerupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPowerupMode.setStatus("current")


class _MaximumTemperature_Type(Integer32):
    """Custom type maximumTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MaximumTemperature_Type.__name__ = "Integer32"
_MaximumTemperature_Object = MibScalar
maximumTemperature = _MaximumTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 8),
    _MaximumTemperature_Type()
)
maximumTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maximumTemperature.setStatus("current")


class _DisplayOrientation_Type(Integer32):
    """Custom type displayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DisplayOrientation_Type.__name__ = "Integer32"
_DisplayOrientation_Object = MibScalar
displayOrientation = _DisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 9),
    _DisplayOrientation_Type()
)
displayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    displayOrientation.setStatus("current")
_LocalAlertReset_Type = Integer32
_LocalAlertReset_Object = MibScalar
localAlertReset = _LocalAlertReset_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 10),
    _LocalAlertReset_Type()
)
localAlertReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localAlertReset.setStatus("current")


class _CurrentDropDetection_Type(Integer32):
    """Custom type currentDropDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CurrentDropDetection_Type.__name__ = "Integer32"
_CurrentDropDetection_Object = MibScalar
currentDropDetection = _CurrentDropDetection_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 11),
    _CurrentDropDetection_Type()
)
currentDropDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentDropDetection.setStatus("current")
_WirelessDisplayPower_Type = Integer32
_WirelessDisplayPower_Object = MibScalar
wirelessDisplayPower = _WirelessDisplayPower_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 7, 1, 12),
    _WirelessDisplayPower_Type()
)
wirelessDisplayPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDisplayPower.setStatus("current")
_InputmeasuresTable_Object = MibTable
inputmeasuresTable = _InputmeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8)
)
if mibBuilder.loadTexts:
    inputmeasuresTable.setStatus("current")
_InputmeasuresEntry_Object = MibTableRow
inputmeasuresEntry = _InputmeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1)
)
inputmeasuresEntry.setIndexNames(
    (0, "SDEVICE-MIB", "channelIndex6"),
)
if mibBuilder.loadTexts:
    inputmeasuresEntry.setStatus("current")


class _ChannelIndex6_Type(Integer32):
    """Custom type channelIndex6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ChannelIndex6_Type.__name__ = "Integer32"
_ChannelIndex6_Object = MibTableColumn
channelIndex6 = _ChannelIndex6_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 1),
    _ChannelIndex6_Type()
)
channelIndex6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelIndex6.setStatus("current")
_KWhTotalI_Type = KiloWattHour
_KWhTotalI_Object = MibTableColumn
kWhTotalI = _KWhTotalI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 2),
    _KWhTotalI_Type()
)
kWhTotalI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kWhTotalI.setStatus("current")
_KWhSubtotalI_Type = KiloWattHour
_KWhSubtotalI_Object = MibTableColumn
kWhSubtotalI = _KWhSubtotalI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 3),
    _KWhSubtotalI_Type()
)
kWhSubtotalI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kWhSubtotalI.setStatus("current")
_PowerFactorI_Type = DeciPowerFactor
_PowerFactorI_Object = MibTableColumn
powerFactorI = _PowerFactorI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 4),
    _PowerFactorI_Type()
)
powerFactorI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFactorI.setStatus("current")
_ActualCurrentI_Type = DeciAmps
_ActualCurrentI_Object = MibTableColumn
actualCurrentI = _ActualCurrentI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 5),
    _ActualCurrentI_Type()
)
actualCurrentI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualCurrentI.setStatus("current")
_PeakCurrentI_Type = DeciAmps
_PeakCurrentI_Object = MibTableColumn
peakCurrentI = _PeakCurrentI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 6),
    _PeakCurrentI_Type()
)
peakCurrentI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakCurrentI.setStatus("current")
_ActualVoltageI_Type = DeciVolts
_ActualVoltageI_Object = MibTableColumn
actualVoltageI = _ActualVoltageI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 7),
    _ActualVoltageI_Type()
)
actualVoltageI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualVoltageI.setStatus("current")
_MinVoltageI_Type = DeciVolts
_MinVoltageI_Object = MibTableColumn
minVoltageI = _MinVoltageI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 8),
    _MinVoltageI_Type()
)
minVoltageI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minVoltageI.setStatus("current")
_PowerVAI_Type = Integer32
_PowerVAI_Object = MibTableColumn
powerVAI = _PowerVAI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 9),
    _PowerVAI_Type()
)
powerVAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerVAI.setStatus("current")
_PowerWattI_Type = Integer32
_PowerWattI_Object = MibTableColumn
powerWattI = _PowerWattI_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 10),
    _PowerWattI_Type()
)
powerWattI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerWattI.setStatus("current")
_MaxInletAmps_Type = DeciAmps
_MaxInletAmps_Object = MibTableColumn
maxInletAmps = _MaxInletAmps_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 11),
    _MaxInletAmps_Type()
)
maxInletAmps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxInletAmps.setStatus("current")
_InputCTratio_Type = Integer32
_InputCTratio_Object = MibTableColumn
inputCTratio = _InputCTratio_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 12),
    _InputCTratio_Type()
)
inputCTratio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputCTratio.setStatus("current")
_InputName_Type = DisplayString
_InputName_Object = MibTableColumn
inputName = _InputName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 8, 1, 13),
    _InputName_Type()
)
inputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputName.setStatus("current")
_OutletsTable_Object = MibTable
outletsTable = _OutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 9)
)
if mibBuilder.loadTexts:
    outletsTable.setStatus("current")
_OutletsEntry_Object = MibTableRow
outletsEntry = _OutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 9, 1)
)
outletsEntry.setIndexNames(
    (0, "SDEVICE-MIB", "channelIndex4"),
)
if mibBuilder.loadTexts:
    outletsEntry.setStatus("current")


class _ChannelIndex4_Type(Integer32):
    """Custom type channelIndex4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ChannelIndex4_Type.__name__ = "Integer32"
_ChannelIndex4_Object = MibTableColumn
channelIndex4 = _ChannelIndex4_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 9, 1, 1),
    _ChannelIndex4_Type()
)
channelIndex4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelIndex4.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 9, 1, 2),
    _OutletName_Type()
)
outletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletName.setStatus("current")
_OutputmeasuresTable_Object = MibTable
outputmeasuresTable = _OutputmeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10)
)
if mibBuilder.loadTexts:
    outputmeasuresTable.setStatus("current")
_OutputmeasuresEntry_Object = MibTableRow
outputmeasuresEntry = _OutputmeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1)
)
outputmeasuresEntry.setIndexNames(
    (0, "SDEVICE-MIB", "channelIndex7"),
)
if mibBuilder.loadTexts:
    outputmeasuresEntry.setStatus("current")


class _ChannelIndex7_Type(Integer32):
    """Custom type channelIndex7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ChannelIndex7_Type.__name__ = "Integer32"
_ChannelIndex7_Object = MibTableColumn
channelIndex7 = _ChannelIndex7_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 1),
    _ChannelIndex7_Type()
)
channelIndex7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelIndex7.setStatus("current")
_KWhTotalO_Type = KiloWattHour
_KWhTotalO_Object = MibTableColumn
kWhTotalO = _KWhTotalO_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 2),
    _KWhTotalO_Type()
)
kWhTotalO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kWhTotalO.setStatus("current")
_KWhSubtotalO_Type = KiloWattHour
_KWhSubtotalO_Object = MibTableColumn
kWhSubtotalO = _KWhSubtotalO_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 3),
    _KWhSubtotalO_Type()
)
kWhSubtotalO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kWhSubtotalO.setStatus("current")
_PowerFactorO_Type = DeciPowerFactor
_PowerFactorO_Object = MibTableColumn
powerFactorO = _PowerFactorO_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 4),
    _PowerFactorO_Type()
)
powerFactorO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFactorO.setStatus("current")
_ActualCurrentO_Type = DeciAmps
_ActualCurrentO_Object = MibTableColumn
actualCurrentO = _ActualCurrentO_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 5),
    _ActualCurrentO_Type()
)
actualCurrentO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualCurrentO.setStatus("current")
_PeakCurrentO_Type = DeciAmps
_PeakCurrentO_Object = MibTableColumn
peakCurrentO = _PeakCurrentO_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 6),
    _PeakCurrentO_Type()
)
peakCurrentO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakCurrentO.setStatus("current")
_ActualVoltageO_Type = DeciVolts
_ActualVoltageO_Object = MibTableColumn
actualVoltageO = _ActualVoltageO_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 7),
    _ActualVoltageO_Type()
)
actualVoltageO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualVoltageO.setStatus("current")
_MaxOutletAmps_Type = DeciAmps
_MaxOutletAmps_Object = MibTableColumn
maxOutletAmps = _MaxOutletAmps_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 8),
    _MaxOutletAmps_Type()
)
maxOutletAmps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxOutletAmps.setStatus("current")
_OutputCTratio_Type = Integer32
_OutputCTratio_Object = MibTableColumn
outputCTratio = _OutputCTratio_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 10, 1, 9),
    _OutputCTratio_Type()
)
outputCTratio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputCTratio.setStatus("current")
_SwitchedoutletsTable_Object = MibTable
switchedoutletsTable = _SwitchedoutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 11)
)
if mibBuilder.loadTexts:
    switchedoutletsTable.setStatus("current")
_SwitchedoutletsEntry_Object = MibTableRow
switchedoutletsEntry = _SwitchedoutletsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 11, 1)
)
switchedoutletsEntry.setIndexNames(
    (0, "SDEVICE-MIB", "channelIndex5"),
)
if mibBuilder.loadTexts:
    switchedoutletsEntry.setStatus("current")


class _ChannelIndex5_Type(Integer32):
    """Custom type channelIndex5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ChannelIndex5_Type.__name__ = "Integer32"
_ChannelIndex5_Object = MibTableColumn
channelIndex5 = _ChannelIndex5_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 11, 1, 1),
    _ChannelIndex5_Type()
)
channelIndex5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelIndex5.setStatus("current")


class _CurrentState_Type(Integer32):
    """Custom type currentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CurrentState_Type.__name__ = "Integer32"
_CurrentState_Object = MibTableColumn
currentState = _CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 11, 1, 2),
    _CurrentState_Type()
)
currentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentState.setStatus("current")


class _Scheduled_Type(Integer32):
    """Custom type scheduled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Scheduled_Type.__name__ = "Integer32"
_Scheduled_Object = MibTableColumn
scheduled = _Scheduled_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 11, 1, 3),
    _Scheduled_Type()
)
scheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scheduled.setStatus("current")
_Unlock_Type = Integer32
_Unlock_Object = MibTableColumn
unlock = _Unlock_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 11, 1, 4),
    _Unlock_Type()
)
unlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unlock.setStatus("current")
_IndividualOutletDelay_Type = Seconds
_IndividualOutletDelay_Object = MibTableColumn
individualOutletDelay = _IndividualOutletDelay_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 11, 1, 5),
    _IndividualOutletDelay_Type()
)
individualOutletDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    individualOutletDelay.setStatus("current")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 12)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 12, 1)
)
sensorEntry.setIndexNames(
    (0, "SDEVICE-MIB", "channelIndex8"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _ChannelIndex8_Type(Integer32):
    """Custom type channelIndex8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ChannelIndex8_Type.__name__ = "Integer32"
_ChannelIndex8_Object = MibTableColumn
channelIndex8 = _ChannelIndex8_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 12, 1, 1),
    _ChannelIndex8_Type()
)
channelIndex8.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelIndex8.setStatus("current")
_SensorType_Type = DisplayString
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 12, 1, 2),
    _SensorType_Type()
)
sensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_SensorValue_Type = DeciValue
_SensorValue_Object = MibTableColumn
sensorValue = _SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 12, 1, 3),
    _SensorValue_Type()
)
sensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorValue.setStatus("current")
_SensorName_Type = DisplayString
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 31034, 2, 12, 1, 4),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 99)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 99, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2)
)

# Managed Objects groups

identificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 1)
)
identificationGroup.setObjects(
      *(("SDEVICE-MIB", "spdmVersion"),
        ("SDEVICE-MIB", "firmwareVersion"),
        ("SDEVICE-MIB", "salesOrderNumber"),
        ("SDEVICE-MIB", "productId"),
        ("SDEVICE-MIB", "serialNumber"),
        ("SDEVICE-MIB", "hardwareAddress"),
        ("SDEVICE-MIB", "unitAddress"),
        ("SDEVICE-MIB", "deviceName"),
        ("SDEVICE-MIB", "deviceLocation"),
        ("SDEVICE-MIB", "vanityTag"),
        ("SDEVICE-MIB", "macAddress"),
        ("SDEVICE-MIB", "buildNumber"))
)
if mibBuilder.loadTexts:
    identificationGroup.setStatus("current")

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 2)
)
configurationGroup.setObjects(
      *(("SDEVICE-MIB", "noPhases"),
        ("SDEVICE-MIB", "noOutletsTotal"),
        ("SDEVICE-MIB", "noSwitchedOutlets"),
        ("SDEVICE-MIB", "noMeasuredOutlets"),
        ("SDEVICE-MIB", "maximumLoad"),
        ("SDEVICE-MIB", "noSensors"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

systemStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 3)
)
systemStatusGroup.setObjects(
      *(("SDEVICE-MIB", "deviceStatusCode"),
        ("SDEVICE-MIB", "temperatureAlert"),
        ("SDEVICE-MIB", "inputCurrentAlert"),
        ("SDEVICE-MIB", "outputCurrentAlert"),
        ("SDEVICE-MIB", "inputVoltageAlert"),
        ("SDEVICE-MIB", "oCurrentDropAlert"),
        ("SDEVICE-MIB", "iCurrentDropAlert"))
)
if mibBuilder.loadTexts:
    systemStatusGroup.setStatus("current")

resetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 4)
)
resetGroup.setObjects(
      *(("SDEVICE-MIB", "resetAlerts"),
        ("SDEVICE-MIB", "resetPeakValues"),
        ("SDEVICE-MIB", "rebootDevice"),
        ("SDEVICE-MIB", "zeroInputKWhSubtotal"),
        ("SDEVICE-MIB", "zeroOutKWhSubtotal"))
)
if mibBuilder.loadTexts:
    resetGroup.setStatus("current")

settingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 5)
)
settingsGroup.setObjects(
      *(("SDEVICE-MIB", "peakDuration"),
        ("SDEVICE-MIB", "localAlertReset"),
        ("SDEVICE-MIB", "fixedOutletDelay"),
        ("SDEVICE-MIB", "powerSaverMode"),
        ("SDEVICE-MIB", "outletPowerupMode"),
        ("SDEVICE-MIB", "maximumTemperature"),
        ("SDEVICE-MIB", "displayOrientation"),
        ("SDEVICE-MIB", "maxInletAmps"),
        ("SDEVICE-MIB", "maxOutletAmps"),
        ("SDEVICE-MIB", "outputCTratio"),
        ("SDEVICE-MIB", "inputCTratio"),
        ("SDEVICE-MIB", "inputName"),
        ("SDEVICE-MIB", "outletName"),
        ("SDEVICE-MIB", "individualOutletDelay"),
        ("SDEVICE-MIB", "currentDropDetection"),
        ("SDEVICE-MIB", "wirelessDisplayPower"))
)
if mibBuilder.loadTexts:
    settingsGroup.setStatus("current")

switchedOutletsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 6)
)
switchedOutletsGroup.setObjects(
      *(("SDEVICE-MIB", "currentState"),
        ("SDEVICE-MIB", "scheduled"),
        ("SDEVICE-MIB", "individualOutletDelay"),
        ("SDEVICE-MIB", "unlock"))
)
if mibBuilder.loadTexts:
    switchedOutletsGroup.setStatus("current")

inputMeasuresGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 7)
)
inputMeasuresGroup.setObjects(
      *(("SDEVICE-MIB", "kWhTotalI"),
        ("SDEVICE-MIB", "kWhSubtotalI"),
        ("SDEVICE-MIB", "powerFactorI"),
        ("SDEVICE-MIB", "actualCurrentI"),
        ("SDEVICE-MIB", "peakCurrentI"),
        ("SDEVICE-MIB", "actualVoltageI"),
        ("SDEVICE-MIB", "minVoltageI"),
        ("SDEVICE-MIB", "powerWattI"),
        ("SDEVICE-MIB", "powerVAI"),
        ("SDEVICE-MIB", "maxInletAmps"),
        ("SDEVICE-MIB", "inputCTratio"),
        ("SDEVICE-MIB", "inputName"))
)
if mibBuilder.loadTexts:
    inputMeasuresGroup.setStatus("current")

outputMeasuresGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 8)
)
outputMeasuresGroup.setObjects(
      *(("SDEVICE-MIB", "kWhTotalO"),
        ("SDEVICE-MIB", "kWhSubtotalO"),
        ("SDEVICE-MIB", "powerFactorO"),
        ("SDEVICE-MIB", "actualCurrentO"),
        ("SDEVICE-MIB", "peakCurrentO"),
        ("SDEVICE-MIB", "actualVoltageO"),
        ("SDEVICE-MIB", "maxOutletAmps"),
        ("SDEVICE-MIB", "outputCTratio"))
)
if mibBuilder.loadTexts:
    outputMeasuresGroup.setStatus("current")

sensorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31034, 99, 2, 9)
)
sensorsGroup.setObjects(
      *(("SDEVICE-MIB", "sensorType"),
        ("SDEVICE-MIB", "sensorValue"),
        ("SDEVICE-MIB", "sensorName"))
)
if mibBuilder.loadTexts:
    sensorsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31034, 99, 1, 1)
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SDEVICE-MIB",
    **{"DeciAmps": DeciAmps,
       "DeciCelsius": DeciCelsius,
       "DeciPowerFactor": DeciPowerFactor,
       "DeciValue": DeciValue,
       "DeciVolts": DeciVolts,
       "KiloWattHour": KiloWattHour,
       "MilliSeconds": MilliSeconds,
       "Seconds": Seconds,
       "schleifenbauer": schleifenbauer,
       "device0": device0,
       "identification": identification,
       "spdmVersion": spdmVersion,
       "firmwareVersion": firmwareVersion,
       "buildNumber": buildNumber,
       "salesOrderNumber": salesOrderNumber,
       "productId": productId,
       "serialNumber": serialNumber,
       "hardwareAddress": hardwareAddress,
       "macAddress": macAddress,
       "unitAddress": unitAddress,
       "deviceName": deviceName,
       "deviceLocation": deviceLocation,
       "vanityTag": vanityTag,
       "configuration": configuration,
       "noPhases": noPhases,
       "noOutletsTotal": noOutletsTotal,
       "noSwitchedOutlets": noSwitchedOutlets,
       "noMeasuredOutlets": noMeasuredOutlets,
       "noSensors": noSensors,
       "maximumLoad": maximumLoad,
       "systemstatus": systemstatus,
       "deviceStatusCode": deviceStatusCode,
       "temperatureAlert": temperatureAlert,
       "inputCurrentAlert": inputCurrentAlert,
       "outputCurrentAlert": outputCurrentAlert,
       "inputVoltageAlert": inputVoltageAlert,
       "oCurrentDropAlert": oCurrentDropAlert,
       "iCurrentDropAlert": iCurrentDropAlert,
       "reset": reset,
       "rebootDevice": rebootDevice,
       "resetAlerts": resetAlerts,
       "zeroInputKWhSubtotal": zeroInputKWhSubtotal,
       "zeroOutKWhSubtotal": zeroOutKWhSubtotal,
       "resetPeakValues": resetPeakValues,
       "settings": settings,
       "general": general,
       "peakDuration": peakDuration,
       "fixedOutletDelay": fixedOutletDelay,
       "powerSaverMode": powerSaverMode,
       "outletPowerupMode": outletPowerupMode,
       "maximumTemperature": maximumTemperature,
       "displayOrientation": displayOrientation,
       "localAlertReset": localAlertReset,
       "currentDropDetection": currentDropDetection,
       "wirelessDisplayPower": wirelessDisplayPower,
       "inputmeasuresTable": inputmeasuresTable,
       "inputmeasuresEntry": inputmeasuresEntry,
       "channelIndex6": channelIndex6,
       "kWhTotalI": kWhTotalI,
       "kWhSubtotalI": kWhSubtotalI,
       "powerFactorI": powerFactorI,
       "actualCurrentI": actualCurrentI,
       "peakCurrentI": peakCurrentI,
       "actualVoltageI": actualVoltageI,
       "minVoltageI": minVoltageI,
       "powerVAI": powerVAI,
       "powerWattI": powerWattI,
       "maxInletAmps": maxInletAmps,
       "inputCTratio": inputCTratio,
       "inputName": inputName,
       "outletsTable": outletsTable,
       "outletsEntry": outletsEntry,
       "channelIndex4": channelIndex4,
       "outletName": outletName,
       "outputmeasuresTable": outputmeasuresTable,
       "outputmeasuresEntry": outputmeasuresEntry,
       "channelIndex7": channelIndex7,
       "kWhTotalO": kWhTotalO,
       "kWhSubtotalO": kWhSubtotalO,
       "powerFactorO": powerFactorO,
       "actualCurrentO": actualCurrentO,
       "peakCurrentO": peakCurrentO,
       "actualVoltageO": actualVoltageO,
       "maxOutletAmps": maxOutletAmps,
       "outputCTratio": outputCTratio,
       "switchedoutletsTable": switchedoutletsTable,
       "switchedoutletsEntry": switchedoutletsEntry,
       "channelIndex5": channelIndex5,
       "currentState": currentState,
       "scheduled": scheduled,
       "unlock": unlock,
       "individualOutletDelay": individualOutletDelay,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "channelIndex8": channelIndex8,
       "sensorType": sensorType,
       "sensorValue": sensorValue,
       "sensorName": sensorName,
       "conformance": conformance,
       "compliances": compliances,
       "compliance": compliance,
       "groups": groups,
       "identificationGroup": identificationGroup,
       "configurationGroup": configurationGroup,
       "systemStatusGroup": systemStatusGroup,
       "resetGroup": resetGroup,
       "settingsGroup": settingsGroup,
       "switchedOutletsGroup": switchedOutletsGroup,
       "inputMeasuresGroup": inputMeasuresGroup,
       "outputMeasuresGroup": outputMeasuresGroup,
       "sensorsGroup": sensorsGroup}
)
