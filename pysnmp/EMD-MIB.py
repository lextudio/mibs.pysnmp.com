# SNMP MIB module (EMD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:25 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raritan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
raritan.setRevisions(
        ("2015-10-26 00:00",
         "2014-09-29 00:00",
         "2014-02-21 00:00",
         "2013-12-17 00:00",
         "2012-10-01 00:00",
         "2012-07-11 00:00",
         "2012-05-25 00:00",
         "2012-01-25 00:00",
         "2011-12-14 00:00",
         "2011-12-12 00:00",
         "2011-11-04 00:00",
         "2011-08-26 00:00",
         "2011-08-05 00:00",
         "2011-06-30 00:00",
         "2011-03-30 00:00",
         "2011-03-10 00:00",
         "2011-02-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorTypeEnumeration(Integer32, TextualConvention):
    status = "current"
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
              28,
              30,
              31,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("absoluteHumidity", 28),
          ("activeEnergy", 8),
          ("activePower", 5),
          ("airFlow", 12),
          ("airPressure", 13),
          ("apparentEnergy", 9),
          ("apparentPower", 6),
          ("binary", 19),
          ("contact", 20),
          ("doorContact", 43),
          ("fanSpeed", 21),
          ("humidity", 11),
          ("illuminance", 42),
          ("motionDetection", 45),
          ("none", 31),
          ("onOff", 14),
          ("other", 30),
          ("peakCurrent", 2),
          ("powerFactor", 7),
          ("rmsCurrent", 1),
          ("rmsVoltage", 4),
          ("smokeDetection", 18),
          ("tamperDetection", 44),
          ("temperature", 10),
          ("trip", 15),
          ("unbalancedCurrent", 3),
          ("vibration", 16),
          ("waterDetection", 17))
    )



class SensorStateEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("aboveUpperCritical", 6),
          ("aboveUpperWarning", 5),
          ("alarmed", 11),
          ("belowLowerCritical", 2),
          ("belowLowerWarning", 3),
          ("closed", 1),
          ("detected", 9),
          ("normal", 4),
          ("notDetected", 10),
          ("off", 8),
          ("on", 7),
          ("open", 0),
          ("unavailable", -1))
    )



class SensorUnitsEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("amp", 2),
          ("cm", 17),
          ("degreeC", 7),
          ("degreeF", 14),
          ("degrees", 20),
          ("feet", 15),
          ("g", 13),
          ("grampercubicmeter", 22),
          ("hertz", 8),
          ("inches", 16),
          ("lux", 21),
          ("meterpersec", 10),
          ("meters", 18),
          ("none", -1),
          ("other", 0),
          ("pascal", 11),
          ("percent", 9),
          ("psi", 12),
          ("rpm", 19),
          ("volt", 1),
          ("voltamp", 4),
          ("voltampHour", 6),
          ("voltampReactive", 23),
          ("watt", 3),
          ("wattHour", 5))
    )



class ExternalSensorsZCoordinateUnitsEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rackUnits", 0),
          ("text", 1))
    )



class HundredthsOfAPercentage(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class DeviceIdentificationParameterEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deviceName", 0),
          ("sysContact", 1),
          ("sysLocation", 3),
          ("sysName", 2))
    )



class PeripheralDeviceFirmwareUpdateStateEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("started", 1),
          ("successful", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Emd_ObjectIdentity = ObjectIdentity
emd = _Emd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0)
)
_TrapInformation_ObjectIdentity = ObjectIdentity
trapInformation = _TrapInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0)
)
_UserName_Type = DisplayString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_TargetUser_Type = DisplayString
_TargetUser_Object = MibScalar
targetUser = _TargetUser_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 2),
    _TargetUser_Type()
)
targetUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetUser.setStatus("current")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibScalar
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 3),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageVersion.setStatus("current")
_RoleName_Type = DisplayString
_RoleName_Object = MibScalar
roleName = _RoleName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 4),
    _RoleName_Type()
)
roleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roleName.setStatus("current")
_SmtpMessageRecipients_Type = DisplayString
_SmtpMessageRecipients_Object = MibScalar
smtpMessageRecipients = _SmtpMessageRecipients_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 5),
    _SmtpMessageRecipients_Type()
)
smtpMessageRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpMessageRecipients.setStatus("current")
_SmtpServer_Type = DisplayString
_SmtpServer_Object = MibScalar
smtpServer = _SmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 6),
    _SmtpServer_Type()
)
smtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServer.setStatus("current")
_OldSensorState_Type = SensorStateEnumeration
_OldSensorState_Object = MibScalar
oldSensorState = _OldSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 7),
    _OldSensorState_Type()
)
oldSensorState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oldSensorState.setStatus("current")


class _ExternalSensorNumber_Type(Integer32):
    """Custom type externalSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExternalSensorNumber_Type.__name__ = "Integer32"
_ExternalSensorNumber_Object = MibScalar
externalSensorNumber = _ExternalSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 8),
    _ExternalSensorNumber_Type()
)
externalSensorNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalSensorNumber.setStatus("current")
_TypeOfSensor_Type = SensorTypeEnumeration
_TypeOfSensor_Object = MibScalar
typeOfSensor = _TypeOfSensor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 9),
    _TypeOfSensor_Type()
)
typeOfSensor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    typeOfSensor.setStatus("current")
_ErrorDescription_Type = DisplayString
_ErrorDescription_Object = MibScalar
errorDescription = _ErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 10),
    _ErrorDescription_Type()
)
errorDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorDescription.setStatus("current")
_DeviceChangedParameter_Type = DeviceIdentificationParameterEnumeration
_DeviceChangedParameter_Object = MibScalar
deviceChangedParameter = _DeviceChangedParameter_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 11),
    _DeviceChangedParameter_Type()
)
deviceChangedParameter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceChangedParameter.setStatus("current")
_ChangedParameterNewValue_Type = DisplayString
_ChangedParameterNewValue_Object = MibScalar
changedParameterNewValue = _ChangedParameterNewValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 12),
    _ChangedParameterNewValue_Type()
)
changedParameterNewValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    changedParameterNewValue.setStatus("current")
_LhxSupportEnabled_Type = TruthValue
_LhxSupportEnabled_Object = MibScalar
lhxSupportEnabled = _LhxSupportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 13),
    _LhxSupportEnabled_Type()
)
lhxSupportEnabled.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lhxSupportEnabled.setStatus("current")
_WebcamModel_Type = DisplayString
_WebcamModel_Object = MibScalar
webcamModel = _WebcamModel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 14),
    _WebcamModel_Type()
)
webcamModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    webcamModel.setStatus("current")
_WebcamConnectionPort_Type = DisplayString
_WebcamConnectionPort_Object = MibScalar
webcamConnectionPort = _WebcamConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 15),
    _WebcamConnectionPort_Type()
)
webcamConnectionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    webcamConnectionPort.setStatus("current")
_PeripheralDeviceRomcode_Type = DisplayString
_PeripheralDeviceRomcode_Object = MibScalar
peripheralDeviceRomcode = _PeripheralDeviceRomcode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 16),
    _PeripheralDeviceRomcode_Type()
)
peripheralDeviceRomcode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    peripheralDeviceRomcode.setStatus("current")
_PeripheralDeviceFirmwareUpdateState_Type = PeripheralDeviceFirmwareUpdateStateEnumeration
_PeripheralDeviceFirmwareUpdateState_Object = MibScalar
peripheralDeviceFirmwareUpdateState = _PeripheralDeviceFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 17),
    _PeripheralDeviceFirmwareUpdateState_Type()
)
peripheralDeviceFirmwareUpdateState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    peripheralDeviceFirmwareUpdateState.setStatus("current")
_AgentInetPortNumber_Type = InetPortNumber
_AgentInetPortNumber_Object = MibScalar
agentInetPortNumber = _AgentInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 18),
    _AgentInetPortNumber_Type()
)
agentInetPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentInetPortNumber.setStatus("current")
_PhoneNumber_Type = DisplayString
_PhoneNumber_Object = MibScalar
phoneNumber = _PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 0, 19),
    _PhoneNumber_Type()
)
phoneNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    phoneNumber.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1)
)
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1)
)
_UnitConfiguration_ObjectIdentity = ObjectIdentity
unitConfiguration = _UnitConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1)
)
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_HardwareVersion_Type = DisplayString
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 2),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 3),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_UtcOffset_Type = DisplayString
_UtcOffset_Object = MibScalar
utcOffset = _UtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 4),
    _UtcOffset_Type()
)
utcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utcOffset.setStatus("current")


class _ExternalSensorCount_Type(Integer32):
    """Custom type externalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExternalSensorCount_Type.__name__ = "Integer32"
_ExternalSensorCount_Object = MibScalar
externalSensorCount = _ExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 5),
    _ExternalSensorCount_Type()
)
externalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorCount.setStatus("current")


class _ManagedExternalSensorCount_Type(Integer32):
    """Custom type managedExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ManagedExternalSensorCount_Type.__name__ = "Integer32"
_ManagedExternalSensorCount_Object = MibScalar
managedExternalSensorCount = _ManagedExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 6),
    _ManagedExternalSensorCount_Type()
)
managedExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedExternalSensorCount.setStatus("current")
_ExternalSensorsZCoordinateUnits_Type = ExternalSensorsZCoordinateUnitsEnumeration
_ExternalSensorsZCoordinateUnits_Object = MibScalar
externalSensorsZCoordinateUnits = _ExternalSensorsZCoordinateUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 7),
    _ExternalSensorsZCoordinateUnits_Type()
)
externalSensorsZCoordinateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorsZCoordinateUnits.setStatus("current")
_DeviceMACAddress_Type = MacAddress
_DeviceMACAddress_Object = MibScalar
deviceMACAddress = _DeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 8),
    _DeviceMACAddress_Type()
)
deviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMACAddress.setStatus("current")
_DeviceInetAddressType_Type = InetAddressType
_DeviceInetAddressType_Object = MibScalar
deviceInetAddressType = _DeviceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 9),
    _DeviceInetAddressType_Type()
)
deviceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInetAddressType.setStatus("current")
_DeviceInetIPAddress_Type = InetAddress
_DeviceInetIPAddress_Object = MibScalar
deviceInetIPAddress = _DeviceInetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 10),
    _DeviceInetIPAddress_Type()
)
deviceInetIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInetIPAddress.setStatus("current")
_DeviceInetNetmask_Type = InetAddress
_DeviceInetNetmask_Object = MibScalar
deviceInetNetmask = _DeviceInetNetmask_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 11),
    _DeviceInetNetmask_Type()
)
deviceInetNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInetNetmask.setStatus("current")
_DeviceInetGateway_Type = InetAddress
_DeviceInetGateway_Object = MibScalar
deviceInetGateway = _DeviceInetGateway_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 12),
    _DeviceInetGateway_Type()
)
deviceInetGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInetGateway.setStatus("current")


class _ServerCount_Type(Integer32):
    """Custom type serverCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ServerCount_Type.__name__ = "Integer32"
_ServerCount_Object = MibScalar
serverCount = _ServerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 13),
    _ServerCount_Type()
)
serverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCount.setStatus("current")
_Model_Type = DisplayString
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 14),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_CascadedDeviceConnected_Type = TruthValue
_CascadedDeviceConnected_Object = MibScalar
cascadedDeviceConnected = _CascadedDeviceConnected_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 15),
    _CascadedDeviceConnected_Type()
)
cascadedDeviceConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cascadedDeviceConnected.setStatus("current")
_PeripheralDevicesAutoManagement_Type = TruthValue
_PeripheralDevicesAutoManagement_Object = MibScalar
peripheralDevicesAutoManagement = _PeripheralDevicesAutoManagement_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 16),
    _PeripheralDevicesAutoManagement_Type()
)
peripheralDevicesAutoManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peripheralDevicesAutoManagement.setStatus("current")
_SynchronizeWithNTPServer_Type = TruthValue
_SynchronizeWithNTPServer_Object = MibScalar
synchronizeWithNTPServer = _SynchronizeWithNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 17),
    _SynchronizeWithNTPServer_Type()
)
synchronizeWithNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synchronizeWithNTPServer.setStatus("current")
_UseDHCPProvidedNTPServer_Type = TruthValue
_UseDHCPProvidedNTPServer_Object = MibScalar
useDHCPProvidedNTPServer = _UseDHCPProvidedNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 18),
    _UseDHCPProvidedNTPServer_Type()
)
useDHCPProvidedNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDHCPProvidedNTPServer.setStatus("current")


class _FirstNTPServerAddressType_Type(InetAddressType):
    """Custom type firstNTPServerAddressType based on InetAddressType"""


_FirstNTPServerAddressType_Object = MibScalar
firstNTPServerAddressType = _FirstNTPServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 19),
    _FirstNTPServerAddressType_Type()
)
firstNTPServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstNTPServerAddressType.setStatus("current")
_FirstNTPServerAddress_Type = InetAddress
_FirstNTPServerAddress_Object = MibScalar
firstNTPServerAddress = _FirstNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 20),
    _FirstNTPServerAddress_Type()
)
firstNTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstNTPServerAddress.setStatus("current")


class _SecondNTPServerAddressType_Type(InetAddressType):
    """Custom type secondNTPServerAddressType based on InetAddressType"""


_SecondNTPServerAddressType_Object = MibScalar
secondNTPServerAddressType = _SecondNTPServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 21),
    _SecondNTPServerAddressType_Type()
)
secondNTPServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondNTPServerAddressType.setStatus("current")
_SecondNTPServerAddress_Type = InetAddress
_SecondNTPServerAddress_Object = MibScalar
secondNTPServerAddress = _SecondNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 1, 22),
    _SecondNTPServerAddress_Type()
)
secondNTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondNTPServerAddress.setStatus("current")
_LogConfiguration_ObjectIdentity = ObjectIdentity
logConfiguration = _LogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 2)
)
_DataLogging_Type = TruthValue
_DataLogging_Object = MibScalar
dataLogging = _DataLogging_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 2, 1),
    _DataLogging_Type()
)
dataLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataLogging.setStatus("current")
_MeasurementPeriod_Type = Integer32
_MeasurementPeriod_Object = MibScalar
measurementPeriod = _MeasurementPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 2, 2),
    _MeasurementPeriod_Type()
)
measurementPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementPeriod.setStatus("current")
_MeasurementsPerLogEntry_Type = Integer32
_MeasurementsPerLogEntry_Object = MibScalar
measurementsPerLogEntry = _MeasurementsPerLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 2, 3),
    _MeasurementsPerLogEntry_Type()
)
measurementsPerLogEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measurementsPerLogEntry.setStatus("current")
_LogSize_Type = Integer32
_LogSize_Object = MibScalar
logSize = _LogSize_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 2, 4),
    _LogSize_Type()
)
logSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSize.setStatus("current")
_DataLoggingEnableForAllSensors_Type = TruthValue
_DataLoggingEnableForAllSensors_Object = MibScalar
dataLoggingEnableForAllSensors = _DataLoggingEnableForAllSensors_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 1, 2, 5),
    _DataLoggingEnableForAllSensors_Type()
)
dataLoggingEnableForAllSensors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataLoggingEnableForAllSensors.setStatus("current")
_ExternalSensors_ObjectIdentity = ObjectIdentity
externalSensors = _ExternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2)
)
_ExternalSensorConfigurationTable_Object = MibTable
externalSensorConfigurationTable = _ExternalSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    externalSensorConfigurationTable.setStatus("current")
_ExternalSensorConfigurationEntry_Object = MibTableRow
externalSensorConfigurationEntry = _ExternalSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1)
)
externalSensorConfigurationEntry.setIndexNames(
    (0, "EMD-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    externalSensorConfigurationEntry.setStatus("current")


class _SensorID_Type(Integer32):
    """Custom type sensorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SensorID_Type.__name__ = "Integer32"
_SensorID_Object = MibTableColumn
sensorID = _SensorID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 1),
    _SensorID_Type()
)
sensorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorID.setStatus("current")
_ExternalSensorType_Type = SensorTypeEnumeration
_ExternalSensorType_Object = MibTableColumn
externalSensorType = _ExternalSensorType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 2),
    _ExternalSensorType_Type()
)
externalSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorType.setStatus("current")
_ExternalSensorSerialNumber_Type = DisplayString
_ExternalSensorSerialNumber_Object = MibTableColumn
externalSensorSerialNumber = _ExternalSensorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 3),
    _ExternalSensorSerialNumber_Type()
)
externalSensorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorSerialNumber.setStatus("current")
_ExternalSensorName_Type = DisplayString
_ExternalSensorName_Object = MibTableColumn
externalSensorName = _ExternalSensorName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 4),
    _ExternalSensorName_Type()
)
externalSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorName.setStatus("current")
_ExternalSensorDescription_Type = DisplayString
_ExternalSensorDescription_Object = MibTableColumn
externalSensorDescription = _ExternalSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 5),
    _ExternalSensorDescription_Type()
)
externalSensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorDescription.setStatus("current")
_ExternalSensorXCoordinate_Type = DisplayString
_ExternalSensorXCoordinate_Object = MibTableColumn
externalSensorXCoordinate = _ExternalSensorXCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 6),
    _ExternalSensorXCoordinate_Type()
)
externalSensorXCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorXCoordinate.setStatus("current")
_ExternalSensorYCoordinate_Type = DisplayString
_ExternalSensorYCoordinate_Object = MibTableColumn
externalSensorYCoordinate = _ExternalSensorYCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 7),
    _ExternalSensorYCoordinate_Type()
)
externalSensorYCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorYCoordinate.setStatus("current")
_ExternalSensorZCoordinate_Type = DisplayString
_ExternalSensorZCoordinate_Object = MibTableColumn
externalSensorZCoordinate = _ExternalSensorZCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 8),
    _ExternalSensorZCoordinate_Type()
)
externalSensorZCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorZCoordinate.setStatus("current")
_ExternalSensorChannelNumber_Type = Integer32
_ExternalSensorChannelNumber_Object = MibTableColumn
externalSensorChannelNumber = _ExternalSensorChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 9),
    _ExternalSensorChannelNumber_Type()
)
externalSensorChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorChannelNumber.setStatus("current")
_ExternalOnOffSensorSubtype_Type = SensorTypeEnumeration
_ExternalOnOffSensorSubtype_Object = MibTableColumn
externalOnOffSensorSubtype = _ExternalOnOffSensorSubtype_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 10),
    _ExternalOnOffSensorSubtype_Type()
)
externalOnOffSensorSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalOnOffSensorSubtype.setStatus("current")
_ExternalSensorUnits_Type = SensorUnitsEnumeration
_ExternalSensorUnits_Object = MibTableColumn
externalSensorUnits = _ExternalSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 11),
    _ExternalSensorUnits_Type()
)
externalSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorUnits.setStatus("current")
_ExternalSensorDecimalDigits_Type = Unsigned32
_ExternalSensorDecimalDigits_Object = MibTableColumn
externalSensorDecimalDigits = _ExternalSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 12),
    _ExternalSensorDecimalDigits_Type()
)
externalSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorDecimalDigits.setStatus("current")
_ExternalSensorAccuracy_Type = HundredthsOfAPercentage
_ExternalSensorAccuracy_Object = MibTableColumn
externalSensorAccuracy = _ExternalSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 13),
    _ExternalSensorAccuracy_Type()
)
externalSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorAccuracy.setStatus("current")
_ExternalSensorResolution_Type = Unsigned32
_ExternalSensorResolution_Object = MibTableColumn
externalSensorResolution = _ExternalSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 14),
    _ExternalSensorResolution_Type()
)
externalSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorResolution.setStatus("current")
_ExternalSensorTolerance_Type = Unsigned32
_ExternalSensorTolerance_Object = MibTableColumn
externalSensorTolerance = _ExternalSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 15),
    _ExternalSensorTolerance_Type()
)
externalSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorTolerance.setStatus("current")
_ExternalSensorMaximum_Type = Integer32
_ExternalSensorMaximum_Object = MibTableColumn
externalSensorMaximum = _ExternalSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 16),
    _ExternalSensorMaximum_Type()
)
externalSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorMaximum.setStatus("current")
_ExternalSensorMinimum_Type = Integer32
_ExternalSensorMinimum_Object = MibTableColumn
externalSensorMinimum = _ExternalSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 17),
    _ExternalSensorMinimum_Type()
)
externalSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorMinimum.setStatus("current")
_ExternalSensorHysteresis_Type = Unsigned32
_ExternalSensorHysteresis_Object = MibTableColumn
externalSensorHysteresis = _ExternalSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 18),
    _ExternalSensorHysteresis_Type()
)
externalSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorHysteresis.setStatus("current")
_ExternalSensorStateChangeDelay_Type = Unsigned32
_ExternalSensorStateChangeDelay_Object = MibTableColumn
externalSensorStateChangeDelay = _ExternalSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 19),
    _ExternalSensorStateChangeDelay_Type()
)
externalSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorStateChangeDelay.setStatus("current")
_ExternalSensorLowerCriticalThreshold_Type = Integer32
_ExternalSensorLowerCriticalThreshold_Object = MibTableColumn
externalSensorLowerCriticalThreshold = _ExternalSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 20),
    _ExternalSensorLowerCriticalThreshold_Type()
)
externalSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorLowerCriticalThreshold.setStatus("current")
_ExternalSensorLowerWarningThreshold_Type = Integer32
_ExternalSensorLowerWarningThreshold_Object = MibTableColumn
externalSensorLowerWarningThreshold = _ExternalSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 21),
    _ExternalSensorLowerWarningThreshold_Type()
)
externalSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorLowerWarningThreshold.setStatus("current")
_ExternalSensorUpperCriticalThreshold_Type = Integer32
_ExternalSensorUpperCriticalThreshold_Object = MibTableColumn
externalSensorUpperCriticalThreshold = _ExternalSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 22),
    _ExternalSensorUpperCriticalThreshold_Type()
)
externalSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUpperCriticalThreshold.setStatus("current")
_ExternalSensorUpperWarningThreshold_Type = Integer32
_ExternalSensorUpperWarningThreshold_Object = MibTableColumn
externalSensorUpperWarningThreshold = _ExternalSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 23),
    _ExternalSensorUpperWarningThreshold_Type()
)
externalSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUpperWarningThreshold.setStatus("current")


class _ExternalSensorEnabledThresholds_Type(Bits):
    """Custom type externalSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_ExternalSensorEnabledThresholds_Type.__name__ = "Bits"
_ExternalSensorEnabledThresholds_Object = MibTableColumn
externalSensorEnabledThresholds = _ExternalSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 24),
    _ExternalSensorEnabledThresholds_Type()
)
externalSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorEnabledThresholds.setStatus("current")
_ExternalSensorPort_Type = DisplayString
_ExternalSensorPort_Object = MibTableColumn
externalSensorPort = _ExternalSensorPort_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 25),
    _ExternalSensorPort_Type()
)
externalSensorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorPort.setStatus("current")
_ExternalSensorIsActuator_Type = TruthValue
_ExternalSensorIsActuator_Object = MibTableColumn
externalSensorIsActuator = _ExternalSensorIsActuator_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 26),
    _ExternalSensorIsActuator_Type()
)
externalSensorIsActuator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorIsActuator.setStatus("current")
_ExternalSensorAlarmedToNormalDelay_Type = Integer32
_ExternalSensorAlarmedToNormalDelay_Object = MibTableColumn
externalSensorAlarmedToNormalDelay = _ExternalSensorAlarmedToNormalDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 27),
    _ExternalSensorAlarmedToNormalDelay_Type()
)
externalSensorAlarmedToNormalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorAlarmedToNormalDelay.setStatus("current")
_ExternalSensorUseDefaultThresholds_Type = TruthValue
_ExternalSensorUseDefaultThresholds_Object = MibTableColumn
externalSensorUseDefaultThresholds = _ExternalSensorUseDefaultThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 1, 1, 28),
    _ExternalSensorUseDefaultThresholds_Type()
)
externalSensorUseDefaultThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUseDefaultThresholds.setStatus("current")
_ExternalSensorTypeDefaultThresholdsTable_Object = MibTable
externalSensorTypeDefaultThresholdsTable = _ExternalSensorTypeDefaultThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    externalSensorTypeDefaultThresholdsTable.setStatus("current")
_ExternalSensorTypeDefaultThresholdsEntry_Object = MibTableRow
externalSensorTypeDefaultThresholdsEntry = _ExternalSensorTypeDefaultThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1)
)
externalSensorTypeDefaultThresholdsEntry.setIndexNames(
    (0, "EMD-MIB", "externalSensorType"),
)
if mibBuilder.loadTexts:
    externalSensorTypeDefaultThresholdsEntry.setStatus("current")
_ExternalSensorTypeDefaultHysteresis_Type = Unsigned32
_ExternalSensorTypeDefaultHysteresis_Object = MibTableColumn
externalSensorTypeDefaultHysteresis = _ExternalSensorTypeDefaultHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1, 3),
    _ExternalSensorTypeDefaultHysteresis_Type()
)
externalSensorTypeDefaultHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultHysteresis.setStatus("current")
_ExternalSensorTypeDefaultStateChangeDelay_Type = Unsigned32
_ExternalSensorTypeDefaultStateChangeDelay_Object = MibTableColumn
externalSensorTypeDefaultStateChangeDelay = _ExternalSensorTypeDefaultStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1, 4),
    _ExternalSensorTypeDefaultStateChangeDelay_Type()
)
externalSensorTypeDefaultStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultStateChangeDelay.setStatus("current")
_ExternalSensorTypeDefaultLowerCriticalThreshold_Type = Integer32
_ExternalSensorTypeDefaultLowerCriticalThreshold_Object = MibTableColumn
externalSensorTypeDefaultLowerCriticalThreshold = _ExternalSensorTypeDefaultLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1, 5),
    _ExternalSensorTypeDefaultLowerCriticalThreshold_Type()
)
externalSensorTypeDefaultLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultLowerCriticalThreshold.setStatus("current")
_ExternalSensorTypeDefaultLowerWarningThreshold_Type = Integer32
_ExternalSensorTypeDefaultLowerWarningThreshold_Object = MibTableColumn
externalSensorTypeDefaultLowerWarningThreshold = _ExternalSensorTypeDefaultLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1, 6),
    _ExternalSensorTypeDefaultLowerWarningThreshold_Type()
)
externalSensorTypeDefaultLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultLowerWarningThreshold.setStatus("current")
_ExternalSensorTypeDefaultUpperCriticalThreshold_Type = Integer32
_ExternalSensorTypeDefaultUpperCriticalThreshold_Object = MibTableColumn
externalSensorTypeDefaultUpperCriticalThreshold = _ExternalSensorTypeDefaultUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1, 7),
    _ExternalSensorTypeDefaultUpperCriticalThreshold_Type()
)
externalSensorTypeDefaultUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultUpperCriticalThreshold.setStatus("current")
_ExternalSensorTypeDefaultUpperWarningThreshold_Type = Integer32
_ExternalSensorTypeDefaultUpperWarningThreshold_Object = MibTableColumn
externalSensorTypeDefaultUpperWarningThreshold = _ExternalSensorTypeDefaultUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1, 8),
    _ExternalSensorTypeDefaultUpperWarningThreshold_Type()
)
externalSensorTypeDefaultUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultUpperWarningThreshold.setStatus("current")


class _ExternalSensorTypeDefaultEnabledThresholds_Type(Bits):
    """Custom type externalSensorTypeDefaultEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_ExternalSensorTypeDefaultEnabledThresholds_Type.__name__ = "Bits"
_ExternalSensorTypeDefaultEnabledThresholds_Object = MibTableColumn
externalSensorTypeDefaultEnabledThresholds = _ExternalSensorTypeDefaultEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 4, 1, 9),
    _ExternalSensorTypeDefaultEnabledThresholds_Type()
)
externalSensorTypeDefaultEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultEnabledThresholds.setStatus("current")
_PeripheralDevicePackageTable_Object = MibTable
peripheralDevicePackageTable = _PeripheralDevicePackageTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    peripheralDevicePackageTable.setStatus("current")
_PeripheralDevicePackageEntry_Object = MibTableRow
peripheralDevicePackageEntry = _PeripheralDevicePackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1)
)
peripheralDevicePackageEntry.setIndexNames(
    (0, "EMD-MIB", "peripheralDevicePackageId"),
)
if mibBuilder.loadTexts:
    peripheralDevicePackageEntry.setStatus("current")


class _PeripheralDevicePackageId_Type(Integer32):
    """Custom type peripheralDevicePackageId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PeripheralDevicePackageId_Type.__name__ = "Integer32"
_PeripheralDevicePackageId_Object = MibTableColumn
peripheralDevicePackageId = _PeripheralDevicePackageId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 1),
    _PeripheralDevicePackageId_Type()
)
peripheralDevicePackageId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peripheralDevicePackageId.setStatus("current")
_PeripheralDevicePackageSerialNumber_Type = DisplayString
_PeripheralDevicePackageSerialNumber_Object = MibTableColumn
peripheralDevicePackageSerialNumber = _PeripheralDevicePackageSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 3),
    _PeripheralDevicePackageSerialNumber_Type()
)
peripheralDevicePackageSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageSerialNumber.setStatus("current")
_PeripheralDevicePackageModel_Type = DisplayString
_PeripheralDevicePackageModel_Object = MibTableColumn
peripheralDevicePackageModel = _PeripheralDevicePackageModel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 4),
    _PeripheralDevicePackageModel_Type()
)
peripheralDevicePackageModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageModel.setStatus("current")
_PeripheralDevicePackageFirmwareVersion_Type = DisplayString
_PeripheralDevicePackageFirmwareVersion_Object = MibTableColumn
peripheralDevicePackageFirmwareVersion = _PeripheralDevicePackageFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 5),
    _PeripheralDevicePackageFirmwareVersion_Type()
)
peripheralDevicePackageFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageFirmwareVersion.setStatus("current")
_PeripheralDevicePackageMinFirmwareVersion_Type = DisplayString
_PeripheralDevicePackageMinFirmwareVersion_Object = MibTableColumn
peripheralDevicePackageMinFirmwareVersion = _PeripheralDevicePackageMinFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 6),
    _PeripheralDevicePackageMinFirmwareVersion_Type()
)
peripheralDevicePackageMinFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageMinFirmwareVersion.setStatus("current")
_PeripheralDevicePackageFirmwareTimeStamp_Type = Unsigned32
_PeripheralDevicePackageFirmwareTimeStamp_Object = MibTableColumn
peripheralDevicePackageFirmwareTimeStamp = _PeripheralDevicePackageFirmwareTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 7),
    _PeripheralDevicePackageFirmwareTimeStamp_Type()
)
peripheralDevicePackageFirmwareTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageFirmwareTimeStamp.setStatus("current")
_PeripheralDevicePackagePosition_Type = DisplayString
_PeripheralDevicePackagePosition_Object = MibTableColumn
peripheralDevicePackagePosition = _PeripheralDevicePackagePosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 8),
    _PeripheralDevicePackagePosition_Type()
)
peripheralDevicePackagePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackagePosition.setStatus("current")
_PeripheralDevicePackageState_Type = DisplayString
_PeripheralDevicePackageState_Object = MibTableColumn
peripheralDevicePackageState = _PeripheralDevicePackageState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 2, 5, 1, 9),
    _PeripheralDevicePackageState_Type()
)
peripheralDevicePackageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageState.setStatus("current")
_ServerReachability_ObjectIdentity = ObjectIdentity
serverReachability = _ServerReachability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 3)
)
_ServerReachabilityTable_Object = MibTable
serverReachabilityTable = _ServerReachabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    serverReachabilityTable.setStatus("current")
_ServerReachabilityEntry_Object = MibTableRow
serverReachabilityEntry = _ServerReachabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 3, 1, 1)
)
serverReachabilityEntry.setIndexNames(
    (0, "EMD-MIB", "serverID"),
)
if mibBuilder.loadTexts:
    serverReachabilityEntry.setStatus("current")


class _ServerID_Type(Integer32):
    """Custom type serverID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ServerID_Type.__name__ = "Integer32"
_ServerID_Object = MibTableColumn
serverID = _ServerID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 3, 1, 1, 1),
    _ServerID_Type()
)
serverID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverID.setStatus("current")
_ServerIPAddress_Type = DisplayString
_ServerIPAddress_Object = MibTableColumn
serverIPAddress = _ServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 3, 1, 1, 2),
    _ServerIPAddress_Type()
)
serverIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIPAddress.setStatus("current")
_ServerPingEnabled_Type = TruthValue
_ServerPingEnabled_Object = MibTableColumn
serverPingEnabled = _ServerPingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 1, 3, 1, 1, 3),
    _ServerPingEnabled_Type()
)
serverPingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverPingEnabled.setStatus("current")
_Measurements_ObjectIdentity = ObjectIdentity
measurements = _Measurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2)
)
_MeasurementsExternalSensor_ObjectIdentity = ObjectIdentity
measurementsExternalSensor = _MeasurementsExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2, 1)
)
_ExternalSensorMeasurementsTable_Object = MibTable
externalSensorMeasurementsTable = _ExternalSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    externalSensorMeasurementsTable.setStatus("current")
_ExternalSensorMeasurementsEntry_Object = MibTableRow
externalSensorMeasurementsEntry = _ExternalSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2, 1, 1, 1)
)
externalSensorMeasurementsEntry.setIndexNames(
    (0, "EMD-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    externalSensorMeasurementsEntry.setStatus("current")
_MeasurementsExternalSensorIsAvailable_Type = TruthValue
_MeasurementsExternalSensorIsAvailable_Object = MibTableColumn
measurementsExternalSensorIsAvailable = _MeasurementsExternalSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2, 1, 1, 1, 1),
    _MeasurementsExternalSensorIsAvailable_Type()
)
measurementsExternalSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorIsAvailable.setStatus("current")
_MeasurementsExternalSensorState_Type = SensorStateEnumeration
_MeasurementsExternalSensorState_Object = MibTableColumn
measurementsExternalSensorState = _MeasurementsExternalSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2, 1, 1, 1, 2),
    _MeasurementsExternalSensorState_Type()
)
measurementsExternalSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorState.setStatus("current")
_MeasurementsExternalSensorValue_Type = Integer32
_MeasurementsExternalSensorValue_Object = MibTableColumn
measurementsExternalSensorValue = _MeasurementsExternalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2, 1, 1, 1, 3),
    _MeasurementsExternalSensorValue_Type()
)
measurementsExternalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorValue.setStatus("current")
_MeasurementsExternalSensorTimeStamp_Type = Unsigned32
_MeasurementsExternalSensorTimeStamp_Object = MibTableColumn
measurementsExternalSensorTimeStamp = _MeasurementsExternalSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 2, 1, 1, 1, 4),
    _MeasurementsExternalSensorTimeStamp_Type()
)
measurementsExternalSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorTimeStamp.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 2)
)
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4)
)
_LogUnit_ObjectIdentity = ObjectIdentity
logUnit = _LogUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 1)
)
_OldestLogID_Type = Integer32
_OldestLogID_Object = MibScalar
oldestLogID = _OldestLogID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 1, 1),
    _OldestLogID_Type()
)
oldestLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldestLogID.setStatus("current")
_NewestLogID_Type = Integer32
_NewestLogID_Object = MibScalar
newestLogID = _NewestLogID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 1, 2),
    _NewestLogID_Type()
)
newestLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newestLogID.setStatus("current")
_LogTimeStampTable_Object = MibTable
logTimeStampTable = _LogTimeStampTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 1, 3)
)
if mibBuilder.loadTexts:
    logTimeStampTable.setStatus("current")
_LogTimeStampEntry_Object = MibTableRow
logTimeStampEntry = _LogTimeStampEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 1, 3, 1)
)
logTimeStampEntry.setIndexNames(
    (0, "EMD-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logTimeStampEntry.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 1, 3, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogTimeStamp_Type = Unsigned32
_LogTimeStamp_Object = MibTableColumn
logTimeStamp = _LogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 1, 3, 1, 2),
    _LogTimeStamp_Type()
)
logTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTimeStamp.setStatus("current")
_LogExternalSensor_ObjectIdentity = ObjectIdentity
logExternalSensor = _LogExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2)
)
_ExternalSensorLogTable_Object = MibTable
externalSensorLogTable = _ExternalSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    externalSensorLogTable.setStatus("current")
_ExternalSensorLogEntry_Object = MibTableRow
externalSensorLogEntry = _ExternalSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2, 1, 1)
)
externalSensorLogEntry.setIndexNames(
    (0, "EMD-MIB", "sensorID"),
    (0, "EMD-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    externalSensorLogEntry.setStatus("current")
_LogExternalSensorDataAvailable_Type = TruthValue
_LogExternalSensorDataAvailable_Object = MibTableColumn
logExternalSensorDataAvailable = _LogExternalSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2, 1, 1, 2),
    _LogExternalSensorDataAvailable_Type()
)
logExternalSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorDataAvailable.setStatus("current")
_LogExternalSensorState_Type = SensorStateEnumeration
_LogExternalSensorState_Object = MibTableColumn
logExternalSensorState = _LogExternalSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2, 1, 1, 3),
    _LogExternalSensorState_Type()
)
logExternalSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorState.setStatus("current")
_LogExternalSensorAvgValue_Type = Integer32
_LogExternalSensorAvgValue_Object = MibTableColumn
logExternalSensorAvgValue = _LogExternalSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2, 1, 1, 4),
    _LogExternalSensorAvgValue_Type()
)
logExternalSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorAvgValue.setStatus("current")
_LogExternalSensorMaxValue_Type = Integer32
_LogExternalSensorMaxValue_Object = MibTableColumn
logExternalSensorMaxValue = _LogExternalSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2, 1, 1, 5),
    _LogExternalSensorMaxValue_Type()
)
logExternalSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorMaxValue.setStatus("current")
_LogExternalSensorMinValue_Type = Integer32
_LogExternalSensorMinValue_Object = MibTableColumn
logExternalSensorMinValue = _LogExternalSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 4, 2, 1, 1, 6),
    _LogExternalSensorMinValue_Type()
)
logExternalSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorMinValue.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 5)
)
_ActuatorControl_ObjectIdentity = ObjectIdentity
actuatorControl = _ActuatorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 8, 5, 1)
)
_ActuatorControlTable_Object = MibTable
actuatorControlTable = _ActuatorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 5, 1, 1)
)
if mibBuilder.loadTexts:
    actuatorControlTable.setStatus("current")
_ActuatorControlEntry_Object = MibTableRow
actuatorControlEntry = _ActuatorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 5, 1, 1, 1)
)
actuatorControlEntry.setIndexNames(
    (0, "EMD-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    actuatorControlEntry.setStatus("current")
_ActuatorState_Type = SensorStateEnumeration
_ActuatorState_Object = MibTableColumn
actuatorState = _ActuatorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 8, 5, 1, 1, 1, 1),
    _ActuatorState_Type()
)
actuatorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actuatorState.setStatus("current")

# Managed Objects groups

configGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 2, 1)
)
configGroup.setObjects(
      *(("EMD-MIB", "externalSensorCount"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "deviceInetNetmask"),
        ("EMD-MIB", "deviceInetGateway"),
        ("EMD-MIB", "deviceMACAddress"),
        ("EMD-MIB", "utcOffset"),
        ("EMD-MIB", "model"),
        ("EMD-MIB", "deviceName"),
        ("EMD-MIB", "hardwareVersion"),
        ("EMD-MIB", "firmwareVersion"),
        ("EMD-MIB", "externalSensorType"),
        ("EMD-MIB", "externalSensorSerialNumber"),
        ("EMD-MIB", "externalSensorName"),
        ("EMD-MIB", "externalSensorDescription"),
        ("EMD-MIB", "externalSensorXCoordinate"),
        ("EMD-MIB", "externalSensorYCoordinate"),
        ("EMD-MIB", "externalSensorZCoordinate"),
        ("EMD-MIB", "externalSensorChannelNumber"),
        ("EMD-MIB", "externalOnOffSensorSubtype"),
        ("EMD-MIB", "externalSensorUnits"),
        ("EMD-MIB", "externalSensorDecimalDigits"),
        ("EMD-MIB", "externalSensorAccuracy"),
        ("EMD-MIB", "externalSensorResolution"),
        ("EMD-MIB", "externalSensorTolerance"),
        ("EMD-MIB", "externalSensorMaximum"),
        ("EMD-MIB", "externalSensorMinimum"),
        ("EMD-MIB", "externalSensorHysteresis"),
        ("EMD-MIB", "externalSensorStateChangeDelay"),
        ("EMD-MIB", "externalSensorLowerCriticalThreshold"),
        ("EMD-MIB", "externalSensorLowerWarningThreshold"),
        ("EMD-MIB", "externalSensorUpperCriticalThreshold"),
        ("EMD-MIB", "externalSensorUpperWarningThreshold"),
        ("EMD-MIB", "externalSensorEnabledThresholds"),
        ("EMD-MIB", "externalSensorPort"),
        ("EMD-MIB", "externalSensorsZCoordinateUnits"),
        ("EMD-MIB", "externalSensorIsActuator"),
        ("EMD-MIB", "externalSensorUseDefaultThresholds"),
        ("EMD-MIB", "externalSensorTypeDefaultHysteresis"),
        ("EMD-MIB", "externalSensorTypeDefaultStateChangeDelay"),
        ("EMD-MIB", "externalSensorTypeDefaultLowerCriticalThreshold"),
        ("EMD-MIB", "externalSensorTypeDefaultLowerWarningThreshold"),
        ("EMD-MIB", "externalSensorTypeDefaultUpperCriticalThreshold"),
        ("EMD-MIB", "externalSensorTypeDefaultUpperWarningThreshold"),
        ("EMD-MIB", "externalSensorTypeDefaultEnabledThresholds"),
        ("EMD-MIB", "managedExternalSensorCount"),
        ("EMD-MIB", "serverCount"),
        ("EMD-MIB", "serverIPAddress"),
        ("EMD-MIB", "serverPingEnabled"),
        ("EMD-MIB", "measurementPeriod"),
        ("EMD-MIB", "measurementsPerLogEntry"),
        ("EMD-MIB", "logSize"),
        ("EMD-MIB", "cascadedDeviceConnected"),
        ("EMD-MIB", "peripheralDevicePackageSerialNumber"),
        ("EMD-MIB", "peripheralDevicePackageModel"),
        ("EMD-MIB", "peripheralDevicePackageFirmwareVersion"),
        ("EMD-MIB", "peripheralDevicePackageMinFirmwareVersion"),
        ("EMD-MIB", "peripheralDevicePackageFirmwareTimeStamp"),
        ("EMD-MIB", "peripheralDevicePackagePosition"),
        ("EMD-MIB", "peripheralDevicePackageState"),
        ("EMD-MIB", "peripheralDevicesAutoManagement"),
        ("EMD-MIB", "externalSensorAlarmedToNormalDelay"),
        ("EMD-MIB", "synchronizeWithNTPServer"),
        ("EMD-MIB", "useDHCPProvidedNTPServer"),
        ("EMD-MIB", "firstNTPServerAddressType"),
        ("EMD-MIB", "firstNTPServerAddress"),
        ("EMD-MIB", "secondNTPServerAddressType"),
        ("EMD-MIB", "secondNTPServerAddress"))
)
if mibBuilder.loadTexts:
    configGroup.setStatus("current")

measurementsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 2, 2)
)
measurementsGroup.setObjects(
      *(("EMD-MIB", "measurementsExternalSensorIsAvailable"),
        ("EMD-MIB", "measurementsExternalSensorState"),
        ("EMD-MIB", "measurementsExternalSensorValue"),
        ("EMD-MIB", "measurementsExternalSensorTimeStamp"))
)
if mibBuilder.loadTexts:
    measurementsGroup.setStatus("current")

trapInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 2, 3)
)
trapInformationGroup.setObjects(
      *(("EMD-MIB", "userName"),
        ("EMD-MIB", "targetUser"),
        ("EMD-MIB", "imageVersion"),
        ("EMD-MIB", "roleName"),
        ("EMD-MIB", "oldSensorState"),
        ("EMD-MIB", "externalSensorNumber"),
        ("EMD-MIB", "typeOfSensor"),
        ("EMD-MIB", "smtpMessageRecipients"),
        ("EMD-MIB", "smtpServer"),
        ("EMD-MIB", "errorDescription"),
        ("EMD-MIB", "deviceChangedParameter"),
        ("EMD-MIB", "changedParameterNewValue"),
        ("EMD-MIB", "lhxSupportEnabled"),
        ("EMD-MIB", "webcamModel"),
        ("EMD-MIB", "webcamConnectionPort"),
        ("EMD-MIB", "peripheralDeviceRomcode"),
        ("EMD-MIB", "peripheralDeviceFirmwareUpdateState"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "phoneNumber"))
)
if mibBuilder.loadTexts:
    trapInformationGroup.setStatus("current")

logGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 2, 5)
)
logGroup.setObjects(
      *(("EMD-MIB", "dataLogging"),
        ("EMD-MIB", "oldestLogID"),
        ("EMD-MIB", "newestLogID"),
        ("EMD-MIB", "logTimeStamp"),
        ("EMD-MIB", "dataLoggingEnableForAllSensors"),
        ("EMD-MIB", "logExternalSensorDataAvailable"),
        ("EMD-MIB", "logExternalSensorState"),
        ("EMD-MIB", "logExternalSensorAvgValue"),
        ("EMD-MIB", "logExternalSensorMaxValue"),
        ("EMD-MIB", "logExternalSensorMinValue"))
)
if mibBuilder.loadTexts:
    logGroup.setStatus("current")

controlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 2, 6)
)
controlGroup.setObjects(
    ("EMD-MIB", "actuatorState")
)
if mibBuilder.loadTexts:
    controlGroup.setStatus("current")


# Notification objects

systemStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 1)
)
systemStarted.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    systemStarted.setStatus(
        "current"
    )

systemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 2)
)
systemReset.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    systemReset.setStatus(
        "current"
    )

userLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 3)
)
userLogin.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userLogin.setStatus(
        "current"
    )

userLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 4)
)
userLogout.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userLogout.setStatus(
        "current"
    )

userAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 5)
)
userAuthenticationFailure.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userAuthenticationFailure.setStatus(
        "current"
    )

userSessionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 6)
)
userSessionTimeout.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userSessionTimeout.setStatus(
        "current"
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 7)
)
userAdded.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "targetUser"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        "current"
    )

userModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 8)
)
userModified.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "targetUser"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userModified.setStatus(
        "current"
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 9)
)
userDeleted.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "targetUser"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        "current"
    )

roleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 10)
)
roleAdded.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "roleName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    roleAdded.setStatus(
        "current"
    )

roleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 11)
)
roleModified.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "roleName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    roleModified.setStatus(
        "current"
    )

roleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 12)
)
roleDeleted.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "roleName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    roleDeleted.setStatus(
        "current"
    )

deviceUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 13)
)
deviceUpdateStarted.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "imageVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    deviceUpdateStarted.setStatus(
        "current"
    )

deviceUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 14)
)
deviceUpdateCompleted.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "imageVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    deviceUpdateCompleted.setStatus(
        "current"
    )

userBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 15)
)
userBlocked.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userBlocked.setStatus(
        "current"
    )

userPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 16)
)
userPasswordChanged.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "targetUser"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userPasswordChanged.setStatus(
        "current"
    )

passwordSettingsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 17)
)
passwordSettingsChanged.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    passwordSettingsChanged.setStatus(
        "current"
    )

firmwareValidationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 18)
)
firmwareValidationFailed.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    firmwareValidationFailed.setStatus(
        "current"
    )

logFileCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 19)
)
logFileCleared.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    logFileCleared.setStatus(
        "current"
    )

bulkConfigurationSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 20)
)
bulkConfigurationSaved.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    bulkConfigurationSaved.setStatus(
        "current"
    )

bulkConfigurationCopied = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 21)
)
bulkConfigurationCopied.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    bulkConfigurationCopied.setStatus(
        "current"
    )

externalSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 22)
)
externalSensorStateChange.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "externalSensorNumber"),
        ("EMD-MIB", "typeOfSensor"),
        ("EMD-MIB", "measurementsExternalSensorTimeStamp"),
        ("EMD-MIB", "measurementsExternalSensorValue"),
        ("EMD-MIB", "measurementsExternalSensorState"),
        ("EMD-MIB", "oldSensorState"),
        ("EMD-MIB", "externalSensorSerialNumber"),
        ("EMD-MIB", "externalOnOffSensorSubtype"),
        ("EMD-MIB", "externalSensorChannelNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    externalSensorStateChange.setStatus(
        "current"
    )

smtpMessageTransmissionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 23)
)
smtpMessageTransmissionFailure.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "smtpMessageRecipients"),
        ("EMD-MIB", "smtpServer"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    smtpMessageTransmissionFailure.setStatus(
        "current"
    )

ldapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 24)
)
ldapError.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    ldapError.setStatus(
        "current"
    )

deviceUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 25)
)
deviceUpdateFailed.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "imageVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    deviceUpdateFailed.setStatus(
        "current"
    )

pingServerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 26)
)
pingServerEnabled.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pingServerEnabled.setStatus(
        "current"
    )

pingServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 27)
)
pingServerDisabled.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pingServerDisabled.setStatus(
        "current"
    )

serverNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 28)
)
serverNotReachable.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    serverNotReachable.setStatus(
        "current"
    )

serverReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 29)
)
serverReachable.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    serverReachable.setStatus(
        "current"
    )

deviceIdentificationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 30)
)
deviceIdentificationChanged.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceChangedParameter"),
        ("EMD-MIB", "changedParameterNewValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    deviceIdentificationChanged.setStatus(
        "current"
    )

usbSlaveConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 31)
)
usbSlaveConnected.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    usbSlaveConnected.setStatus(
        "current"
    )

usbSlaveDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 32)
)
usbSlaveDisconnected.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    usbSlaveDisconnected.setStatus(
        "current"
    )

lhxSupportChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 33)
)
lhxSupportChanged.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("EMD-MIB", "lhxSupportEnabled"))
)
if mibBuilder.loadTexts:
    lhxSupportChanged.setStatus(
        "current"
    )

userAcceptedRestrictedServiceAgreement = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 34)
)
userAcceptedRestrictedServiceAgreement.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userAcceptedRestrictedServiceAgreement.setStatus(
        "current"
    )

userDeclinedRestrictedServiceAgreement = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 35)
)
userDeclinedRestrictedServiceAgreement.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userDeclinedRestrictedServiceAgreement.setStatus(
        "current"
    )

deviceSettingsSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 36)
)
deviceSettingsSaved.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    deviceSettingsSaved.setStatus(
        "current"
    )

deviceSettingsRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 37)
)
deviceSettingsRestored.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "userName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    deviceSettingsRestored.setStatus(
        "current"
    )

webcamInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 38)
)
webcamInserted.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "webcamModel"),
        ("EMD-MIB", "webcamConnectionPort"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    webcamInserted.setStatus(
        "current"
    )

webcamRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 39)
)
webcamRemoved.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "webcamModel"),
        ("EMD-MIB", "webcamConnectionPort"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    webcamRemoved.setStatus(
        "current"
    )

serverConnectivityUnrecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 40)
)
serverConnectivityUnrecoverable.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    serverConnectivityUnrecoverable.setStatus(
        "current"
    )

radiusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 41)
)
radiusError.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    radiusError.setStatus(
        "current"
    )

serverReachabilityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 42)
)
serverReachabilityError.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "serverIPAddress"),
        ("EMD-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    serverReachabilityError.setStatus(
        "current"
    )

unknownPeripheralDeviceAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 43)
)
unknownPeripheralDeviceAttached.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "peripheralDeviceRomcode"),
        ("EMD-MIB", "peripheralDevicePackagePosition"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    unknownPeripheralDeviceAttached.setStatus(
        "current"
    )

peripheralDeviceFirmwareUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 44)
)
peripheralDeviceFirmwareUpdate.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "peripheralDevicePackageSerialNumber"),
        ("EMD-MIB", "peripheralDeviceFirmwareUpdateState"),
        ("EMD-MIB", "peripheralDevicePackageFirmwareVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    peripheralDeviceFirmwareUpdate.setStatus(
        "current"
    )

smsMessageTransmissionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 8, 0, 45)
)
smsMessageTransmissionFailure.setObjects(
      *(("EMD-MIB", "deviceName"),
        ("EMD-MIB", "deviceInetAddressType"),
        ("EMD-MIB", "deviceInetIPAddress"),
        ("EMD-MIB", "agentInetPortNumber"),
        ("EMD-MIB", "phoneNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    smsMessageTransmissionFailure.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 2, 4)
)
trapsGroup.setObjects(
      *(("EMD-MIB", "systemStarted"),
        ("EMD-MIB", "systemReset"),
        ("EMD-MIB", "userLogin"),
        ("EMD-MIB", "userLogout"),
        ("EMD-MIB", "userAuthenticationFailure"),
        ("EMD-MIB", "userSessionTimeout"),
        ("EMD-MIB", "userAdded"),
        ("EMD-MIB", "userModified"),
        ("EMD-MIB", "userDeleted"),
        ("EMD-MIB", "roleAdded"),
        ("EMD-MIB", "roleModified"),
        ("EMD-MIB", "roleDeleted"),
        ("EMD-MIB", "deviceUpdateStarted"),
        ("EMD-MIB", "deviceUpdateCompleted"),
        ("EMD-MIB", "userBlocked"),
        ("EMD-MIB", "userPasswordChanged"),
        ("EMD-MIB", "passwordSettingsChanged"),
        ("EMD-MIB", "firmwareValidationFailed"),
        ("EMD-MIB", "logFileCleared"),
        ("EMD-MIB", "bulkConfigurationSaved"),
        ("EMD-MIB", "bulkConfigurationCopied"),
        ("EMD-MIB", "externalSensorStateChange"),
        ("EMD-MIB", "smtpMessageTransmissionFailure"),
        ("EMD-MIB", "ldapError"),
        ("EMD-MIB", "deviceUpdateFailed"),
        ("EMD-MIB", "pingServerEnabled"),
        ("EMD-MIB", "pingServerDisabled"),
        ("EMD-MIB", "serverNotReachable"),
        ("EMD-MIB", "serverReachable"),
        ("EMD-MIB", "deviceIdentificationChanged"),
        ("EMD-MIB", "usbSlaveConnected"),
        ("EMD-MIB", "usbSlaveDisconnected"),
        ("EMD-MIB", "lhxSupportChanged"),
        ("EMD-MIB", "userAcceptedRestrictedServiceAgreement"),
        ("EMD-MIB", "userDeclinedRestrictedServiceAgreement"),
        ("EMD-MIB", "deviceSettingsSaved"),
        ("EMD-MIB", "deviceSettingsRestored"),
        ("EMD-MIB", "webcamInserted"),
        ("EMD-MIB", "webcamRemoved"),
        ("EMD-MIB", "serverConnectivityUnrecoverable"),
        ("EMD-MIB", "radiusError"),
        ("EMD-MIB", "serverReachabilityError"),
        ("EMD-MIB", "unknownPeripheralDeviceAttached"),
        ("EMD-MIB", "peripheralDeviceFirmwareUpdate"),
        ("EMD-MIB", "smsMessageTransmissionFailure"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

complianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    complianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMD-MIB",
    **{"SensorTypeEnumeration": SensorTypeEnumeration,
       "SensorStateEnumeration": SensorStateEnumeration,
       "SensorUnitsEnumeration": SensorUnitsEnumeration,
       "ExternalSensorsZCoordinateUnitsEnumeration": ExternalSensorsZCoordinateUnitsEnumeration,
       "HundredthsOfAPercentage": HundredthsOfAPercentage,
       "DeviceIdentificationParameterEnumeration": DeviceIdentificationParameterEnumeration,
       "PeripheralDeviceFirmwareUpdateStateEnumeration": PeripheralDeviceFirmwareUpdateStateEnumeration,
       "raritan": raritan,
       "emd": emd,
       "traps": traps,
       "trapInformation": trapInformation,
       "userName": userName,
       "targetUser": targetUser,
       "imageVersion": imageVersion,
       "roleName": roleName,
       "smtpMessageRecipients": smtpMessageRecipients,
       "smtpServer": smtpServer,
       "oldSensorState": oldSensorState,
       "externalSensorNumber": externalSensorNumber,
       "typeOfSensor": typeOfSensor,
       "errorDescription": errorDescription,
       "deviceChangedParameter": deviceChangedParameter,
       "changedParameterNewValue": changedParameterNewValue,
       "lhxSupportEnabled": lhxSupportEnabled,
       "webcamModel": webcamModel,
       "webcamConnectionPort": webcamConnectionPort,
       "peripheralDeviceRomcode": peripheralDeviceRomcode,
       "peripheralDeviceFirmwareUpdateState": peripheralDeviceFirmwareUpdateState,
       "agentInetPortNumber": agentInetPortNumber,
       "phoneNumber": phoneNumber,
       "systemStarted": systemStarted,
       "systemReset": systemReset,
       "userLogin": userLogin,
       "userLogout": userLogout,
       "userAuthenticationFailure": userAuthenticationFailure,
       "userSessionTimeout": userSessionTimeout,
       "userAdded": userAdded,
       "userModified": userModified,
       "userDeleted": userDeleted,
       "roleAdded": roleAdded,
       "roleModified": roleModified,
       "roleDeleted": roleDeleted,
       "deviceUpdateStarted": deviceUpdateStarted,
       "deviceUpdateCompleted": deviceUpdateCompleted,
       "userBlocked": userBlocked,
       "userPasswordChanged": userPasswordChanged,
       "passwordSettingsChanged": passwordSettingsChanged,
       "firmwareValidationFailed": firmwareValidationFailed,
       "logFileCleared": logFileCleared,
       "bulkConfigurationSaved": bulkConfigurationSaved,
       "bulkConfigurationCopied": bulkConfigurationCopied,
       "externalSensorStateChange": externalSensorStateChange,
       "smtpMessageTransmissionFailure": smtpMessageTransmissionFailure,
       "ldapError": ldapError,
       "deviceUpdateFailed": deviceUpdateFailed,
       "pingServerEnabled": pingServerEnabled,
       "pingServerDisabled": pingServerDisabled,
       "serverNotReachable": serverNotReachable,
       "serverReachable": serverReachable,
       "deviceIdentificationChanged": deviceIdentificationChanged,
       "usbSlaveConnected": usbSlaveConnected,
       "usbSlaveDisconnected": usbSlaveDisconnected,
       "lhxSupportChanged": lhxSupportChanged,
       "userAcceptedRestrictedServiceAgreement": userAcceptedRestrictedServiceAgreement,
       "userDeclinedRestrictedServiceAgreement": userDeclinedRestrictedServiceAgreement,
       "deviceSettingsSaved": deviceSettingsSaved,
       "deviceSettingsRestored": deviceSettingsRestored,
       "webcamInserted": webcamInserted,
       "webcamRemoved": webcamRemoved,
       "serverConnectivityUnrecoverable": serverConnectivityUnrecoverable,
       "radiusError": radiusError,
       "serverReachabilityError": serverReachabilityError,
       "unknownPeripheralDeviceAttached": unknownPeripheralDeviceAttached,
       "peripheralDeviceFirmwareUpdate": peripheralDeviceFirmwareUpdate,
       "smsMessageTransmissionFailure": smsMessageTransmissionFailure,
       "configuration": configuration,
       "unit": unit,
       "unitConfiguration": unitConfiguration,
       "deviceName": deviceName,
       "hardwareVersion": hardwareVersion,
       "firmwareVersion": firmwareVersion,
       "utcOffset": utcOffset,
       "externalSensorCount": externalSensorCount,
       "managedExternalSensorCount": managedExternalSensorCount,
       "externalSensorsZCoordinateUnits": externalSensorsZCoordinateUnits,
       "deviceMACAddress": deviceMACAddress,
       "deviceInetAddressType": deviceInetAddressType,
       "deviceInetIPAddress": deviceInetIPAddress,
       "deviceInetNetmask": deviceInetNetmask,
       "deviceInetGateway": deviceInetGateway,
       "serverCount": serverCount,
       "model": model,
       "cascadedDeviceConnected": cascadedDeviceConnected,
       "peripheralDevicesAutoManagement": peripheralDevicesAutoManagement,
       "synchronizeWithNTPServer": synchronizeWithNTPServer,
       "useDHCPProvidedNTPServer": useDHCPProvidedNTPServer,
       "firstNTPServerAddressType": firstNTPServerAddressType,
       "firstNTPServerAddress": firstNTPServerAddress,
       "secondNTPServerAddressType": secondNTPServerAddressType,
       "secondNTPServerAddress": secondNTPServerAddress,
       "logConfiguration": logConfiguration,
       "dataLogging": dataLogging,
       "measurementPeriod": measurementPeriod,
       "measurementsPerLogEntry": measurementsPerLogEntry,
       "logSize": logSize,
       "dataLoggingEnableForAllSensors": dataLoggingEnableForAllSensors,
       "externalSensors": externalSensors,
       "externalSensorConfigurationTable": externalSensorConfigurationTable,
       "externalSensorConfigurationEntry": externalSensorConfigurationEntry,
       "sensorID": sensorID,
       "externalSensorType": externalSensorType,
       "externalSensorSerialNumber": externalSensorSerialNumber,
       "externalSensorName": externalSensorName,
       "externalSensorDescription": externalSensorDescription,
       "externalSensorXCoordinate": externalSensorXCoordinate,
       "externalSensorYCoordinate": externalSensorYCoordinate,
       "externalSensorZCoordinate": externalSensorZCoordinate,
       "externalSensorChannelNumber": externalSensorChannelNumber,
       "externalOnOffSensorSubtype": externalOnOffSensorSubtype,
       "externalSensorUnits": externalSensorUnits,
       "externalSensorDecimalDigits": externalSensorDecimalDigits,
       "externalSensorAccuracy": externalSensorAccuracy,
       "externalSensorResolution": externalSensorResolution,
       "externalSensorTolerance": externalSensorTolerance,
       "externalSensorMaximum": externalSensorMaximum,
       "externalSensorMinimum": externalSensorMinimum,
       "externalSensorHysteresis": externalSensorHysteresis,
       "externalSensorStateChangeDelay": externalSensorStateChangeDelay,
       "externalSensorLowerCriticalThreshold": externalSensorLowerCriticalThreshold,
       "externalSensorLowerWarningThreshold": externalSensorLowerWarningThreshold,
       "externalSensorUpperCriticalThreshold": externalSensorUpperCriticalThreshold,
       "externalSensorUpperWarningThreshold": externalSensorUpperWarningThreshold,
       "externalSensorEnabledThresholds": externalSensorEnabledThresholds,
       "externalSensorPort": externalSensorPort,
       "externalSensorIsActuator": externalSensorIsActuator,
       "externalSensorAlarmedToNormalDelay": externalSensorAlarmedToNormalDelay,
       "externalSensorUseDefaultThresholds": externalSensorUseDefaultThresholds,
       "externalSensorTypeDefaultThresholdsTable": externalSensorTypeDefaultThresholdsTable,
       "externalSensorTypeDefaultThresholdsEntry": externalSensorTypeDefaultThresholdsEntry,
       "externalSensorTypeDefaultHysteresis": externalSensorTypeDefaultHysteresis,
       "externalSensorTypeDefaultStateChangeDelay": externalSensorTypeDefaultStateChangeDelay,
       "externalSensorTypeDefaultLowerCriticalThreshold": externalSensorTypeDefaultLowerCriticalThreshold,
       "externalSensorTypeDefaultLowerWarningThreshold": externalSensorTypeDefaultLowerWarningThreshold,
       "externalSensorTypeDefaultUpperCriticalThreshold": externalSensorTypeDefaultUpperCriticalThreshold,
       "externalSensorTypeDefaultUpperWarningThreshold": externalSensorTypeDefaultUpperWarningThreshold,
       "externalSensorTypeDefaultEnabledThresholds": externalSensorTypeDefaultEnabledThresholds,
       "peripheralDevicePackageTable": peripheralDevicePackageTable,
       "peripheralDevicePackageEntry": peripheralDevicePackageEntry,
       "peripheralDevicePackageId": peripheralDevicePackageId,
       "peripheralDevicePackageSerialNumber": peripheralDevicePackageSerialNumber,
       "peripheralDevicePackageModel": peripheralDevicePackageModel,
       "peripheralDevicePackageFirmwareVersion": peripheralDevicePackageFirmwareVersion,
       "peripheralDevicePackageMinFirmwareVersion": peripheralDevicePackageMinFirmwareVersion,
       "peripheralDevicePackageFirmwareTimeStamp": peripheralDevicePackageFirmwareTimeStamp,
       "peripheralDevicePackagePosition": peripheralDevicePackagePosition,
       "peripheralDevicePackageState": peripheralDevicePackageState,
       "serverReachability": serverReachability,
       "serverReachabilityTable": serverReachabilityTable,
       "serverReachabilityEntry": serverReachabilityEntry,
       "serverID": serverID,
       "serverIPAddress": serverIPAddress,
       "serverPingEnabled": serverPingEnabled,
       "measurements": measurements,
       "measurementsExternalSensor": measurementsExternalSensor,
       "externalSensorMeasurementsTable": externalSensorMeasurementsTable,
       "externalSensorMeasurementsEntry": externalSensorMeasurementsEntry,
       "measurementsExternalSensorIsAvailable": measurementsExternalSensorIsAvailable,
       "measurementsExternalSensorState": measurementsExternalSensorState,
       "measurementsExternalSensorValue": measurementsExternalSensorValue,
       "measurementsExternalSensorTimeStamp": measurementsExternalSensorTimeStamp,
       "conformance": conformance,
       "compliances": compliances,
       "complianceRev1": complianceRev1,
       "groups": groups,
       "configGroup": configGroup,
       "measurementsGroup": measurementsGroup,
       "trapInformationGroup": trapInformationGroup,
       "trapsGroup": trapsGroup,
       "logGroup": logGroup,
       "controlGroup": controlGroup,
       "log": log,
       "logUnit": logUnit,
       "oldestLogID": oldestLogID,
       "newestLogID": newestLogID,
       "logTimeStampTable": logTimeStampTable,
       "logTimeStampEntry": logTimeStampEntry,
       "logIndex": logIndex,
       "logTimeStamp": logTimeStamp,
       "logExternalSensor": logExternalSensor,
       "externalSensorLogTable": externalSensorLogTable,
       "externalSensorLogEntry": externalSensorLogEntry,
       "logExternalSensorDataAvailable": logExternalSensorDataAvailable,
       "logExternalSensorState": logExternalSensorState,
       "logExternalSensorAvgValue": logExternalSensorAvgValue,
       "logExternalSensorMaxValue": logExternalSensorMaxValue,
       "logExternalSensorMinValue": logExternalSensorMinValue,
       "control": control,
       "actuatorControl": actuatorControl,
       "actuatorControlTable": actuatorControlTable,
       "actuatorControlEntry": actuatorControlEntry,
       "actuatorState": actuatorState}
)
