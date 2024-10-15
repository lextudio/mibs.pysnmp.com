# SNMP MIB module (LHX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LHX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:51 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raritan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
raritan.setRevisions(
        ("2015-01-05 00:00",
         "2013-07-24 00:00",
         "2012-08-13 00:00",
         "2011-05-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OperationalStateEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("offline", 1),
          ("online", 2))
    )



class GwSensorTypeEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("airTemperature", 0),
          ("doorContact", 3),
          ("fanSpeed", 2),
          ("valvePosition", 4),
          ("waterTemperature", 1))
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("amp", 2),
          ("cm", 17),
          ("degreeC", 7),
          ("degreeF", 14),
          ("feet", 15),
          ("g", 13),
          ("hertz", 8),
          ("inches", 16),
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
          ("watt", 3),
          ("wattHour", 5))
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



# MIB Managed Objects in the order of their OIDs

_Lhxgw_ObjectIdentity = ObjectIdentity
lhxgw = _Lhxgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0)
)
_TrapInformation_ObjectIdentity = ObjectIdentity
trapInformation = _TrapInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0)
)
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceInetAddressType_Type = InetAddressType
_DeviceInetAddressType_Object = MibScalar
deviceInetAddressType = _DeviceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 2),
    _DeviceInetAddressType_Type()
)
deviceInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceInetAddressType.setStatus("current")
_DeviceInetIPAddress_Type = InetAddress
_DeviceInetIPAddress_Object = MibScalar
deviceInetIPAddress = _DeviceInetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 3),
    _DeviceInetIPAddress_Type()
)
deviceInetIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceInetIPAddress.setStatus("current")
_LhxErrorCode_Type = DisplayString
_LhxErrorCode_Object = MibScalar
lhxErrorCode = _LhxErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 4),
    _LhxErrorCode_Type()
)
lhxErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lhxErrorCode.setStatus("current")


class _PortId_Type(Integer32):
    """Custom type portId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PortId_Type.__name__ = "Integer32"
_PortId_Object = MibScalar
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 5),
    _PortId_Type()
)
portId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portId.setStatus("current")
_ProbeId_Type = DisplayString
_ProbeId_Object = MibScalar
probeId = _ProbeId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 6),
    _ProbeId_Type()
)
probeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    probeId.setStatus("current")
_FanId_Type = DisplayString
_FanId_Object = MibScalar
fanId = _FanId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 7),
    _FanId_Type()
)
fanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fanId.setStatus("current")
_PowerSupplyId_Type = DisplayString
_PowerSupplyId_Object = MibScalar
powerSupplyId = _PowerSupplyId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 8),
    _PowerSupplyId_Type()
)
powerSupplyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    powerSupplyId.setStatus("current")
_OldSensorState_Type = SensorStateEnumeration
_OldSensorState_Object = MibScalar
oldSensorState = _OldSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 9),
    _OldSensorState_Type()
)
oldSensorState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oldSensorState.setStatus("current")
_SensorTypeId_Type = GwSensorTypeEnumeration
_SensorTypeId_Object = MibScalar
sensorTypeId = _SensorTypeId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 10),
    _SensorTypeId_Type()
)
sensorTypeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sensorTypeId.setStatus("current")


class _SensorId_Type(Integer32):
    """Custom type sensorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SensorId_Type.__name__ = "Integer32"
_SensorId_Object = MibScalar
sensorId = _SensorId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 11),
    _SensorId_Type()
)
sensorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sensorId.setStatus("current")


class _OldOperationalState_Type(OperationalStateEnumeration):
    """Custom type oldOperationalState based on OperationalStateEnumeration"""
    defaultValue = 0


_OldOperationalState_Object = MibScalar
oldOperationalState = _OldOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 12),
    _OldOperationalState_Type()
)
oldOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldOperationalState.setStatus("current")
_AgentInetPortNumber_Type = InetPortNumber
_AgentInetPortNumber_Object = MibScalar
agentInetPortNumber = _AgentInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 0, 13),
    _AgentInetPortNumber_Type()
)
agentInetPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentInetPortNumber.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1)
)


class _PortCount_Type(Integer32):
    """Custom type portCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortCount_Type.__name__ = "Integer32"
_PortCount_Object = MibScalar
portCount = _PortCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 1),
    _PortCount_Type()
)
portCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCount.setStatus("current")
_SensorCountTable_Object = MibTable
sensorCountTable = _SensorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 2)
)
if mibBuilder.loadTexts:
    sensorCountTable.setStatus("current")
_SensorCountEntry_Object = MibTableRow
sensorCountEntry = _SensorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 2, 1)
)
sensorCountEntry.setIndexNames(
    (0, "LHX-MIB", "portIdx"),
    (0, "LHX-MIB", "sensorTypeIdx"),
)
if mibBuilder.loadTexts:
    sensorCountEntry.setStatus("current")
_SensorCount_Type = Integer32
_SensorCount_Object = MibTableColumn
sensorCount = _SensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 2, 1, 1),
    _SensorCount_Type()
)
sensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCount.setStatus("current")
_Lhx_ObjectIdentity = ObjectIdentity
lhx = _Lhx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3)
)
_LhxConfigurationTable_Object = MibTable
lhxConfigurationTable = _LhxConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lhxConfigurationTable.setStatus("current")
_LhxConfigurationEntry_Object = MibTableRow
lhxConfigurationEntry = _LhxConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1)
)
lhxConfigurationEntry.setIndexNames(
    (0, "LHX-MIB", "portIdx"),
)
if mibBuilder.loadTexts:
    lhxConfigurationEntry.setStatus("current")


class _OperationalState_Type(OperationalStateEnumeration):
    """Custom type operationalState based on OperationalStateEnumeration"""
    defaultValue = 0


_OperationalState_Object = MibTableColumn
operationalState = _OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 1),
    _OperationalState_Type()
)
operationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationalState.setStatus("current")


class _SetpointVentilators_Type(Integer32):
    """Custom type setpointVentilators based on Integer32"""
    defaultValue = 0


_SetpointVentilators_Object = MibTableColumn
setpointVentilators = _SetpointVentilators_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 2),
    _SetpointVentilators_Type()
)
setpointVentilators.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpointVentilators.setStatus("current")


class _SetpointWaterValve_Type(Integer32):
    """Custom type setpointWaterValve based on Integer32"""
    defaultValue = 0


_SetpointWaterValve_Object = MibTableColumn
setpointWaterValve = _SetpointWaterValve_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 3),
    _SetpointWaterValve_Type()
)
setpointWaterValve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setpointWaterValve.setStatus("current")


class _DefaultFanSpeed_Type(Integer32):
    """Custom type defaultFanSpeed based on Integer32"""
    defaultValue = 0


_DefaultFanSpeed_Object = MibTableColumn
defaultFanSpeed = _DefaultFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 4),
    _DefaultFanSpeed_Type()
)
defaultFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultFanSpeed.setStatus("current")


class _MaximumCoolingState_Type(TruthValue):
    """Custom type maximumCoolingState based on TruthValue"""
    defaultValue = 2


_MaximumCoolingState_Object = MibTableColumn
maximumCoolingState = _MaximumCoolingState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 5),
    _MaximumCoolingState_Type()
)
maximumCoolingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maximumCoolingState.setStatus("current")


class _AlertState_Type(TruthValue):
    """Custom type alertState based on TruthValue"""
    defaultValue = 2


_AlertState_Object = MibTableColumn
alertState = _AlertState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 6),
    _AlertState_Type()
)
alertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertState.setStatus("current")
_Model_Type = DisplayString
_Model_Object = MibTableColumn
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 7),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_FwVersion_Type = DisplayString
_FwVersion_Object = MibTableColumn
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 3, 1, 1, 8),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")
_GwSensors_ObjectIdentity = ObjectIdentity
gwSensors = _GwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4)
)
_SensorConfigurationTable_Object = MibTable
sensorConfigurationTable = _SensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sensorConfigurationTable.setStatus("current")
_SensorConfigurationEntry_Object = MibTableRow
sensorConfigurationEntry = _SensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1)
)
sensorConfigurationEntry.setIndexNames(
    (0, "LHX-MIB", "portIdx"),
    (0, "LHX-MIB", "sensorTypeIdx"),
    (0, "LHX-MIB", "sensorIdx"),
)
if mibBuilder.loadTexts:
    sensorConfigurationEntry.setStatus("current")


class _PortIdx_Type(Integer32):
    """Custom type portIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PortIdx_Type.__name__ = "Integer32"
_PortIdx_Object = MibTableColumn
portIdx = _PortIdx_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 1),
    _PortIdx_Type()
)
portIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIdx.setStatus("current")


class _SensorTypeIdx_Type(Integer32):
    """Custom type sensorTypeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SensorTypeIdx_Type.__name__ = "Integer32"
_SensorTypeIdx_Object = MibTableColumn
sensorTypeIdx = _SensorTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 2),
    _SensorTypeIdx_Type()
)
sensorTypeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorTypeIdx.setStatus("current")


class _SensorIdx_Type(Integer32):
    """Custom type sensorIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SensorIdx_Type.__name__ = "Integer32"
_SensorIdx_Object = MibTableColumn
sensorIdx = _SensorIdx_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 3),
    _SensorIdx_Type()
)
sensorIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorIdx.setStatus("current")
_SensorLabel_Type = DisplayString
_SensorLabel_Object = MibTableColumn
sensorLabel = _SensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 4),
    _SensorLabel_Type()
)
sensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorLabel.setStatus("current")
_SensorUnit_Type = SensorUnitsEnumeration
_SensorUnit_Object = MibTableColumn
sensorUnit = _SensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 5),
    _SensorUnit_Type()
)
sensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorUnit.setStatus("current")
_SensorDecimalDigits_Type = Unsigned32
_SensorDecimalDigits_Object = MibTableColumn
sensorDecimalDigits = _SensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 6),
    _SensorDecimalDigits_Type()
)
sensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDecimalDigits.setStatus("current")
_SensorMaximum_Type = Integer32
_SensorMaximum_Object = MibTableColumn
sensorMaximum = _SensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 7),
    _SensorMaximum_Type()
)
sensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorMaximum.setStatus("current")
_SensorMinimum_Type = Integer32
_SensorMinimum_Object = MibTableColumn
sensorMinimum = _SensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 8),
    _SensorMinimum_Type()
)
sensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorMinimum.setStatus("current")
_SensorHysteresis_Type = Unsigned32
_SensorHysteresis_Object = MibTableColumn
sensorHysteresis = _SensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 9),
    _SensorHysteresis_Type()
)
sensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorHysteresis.setStatus("current")
_SensorLowerCriticalThreshold_Type = Integer32
_SensorLowerCriticalThreshold_Object = MibTableColumn
sensorLowerCriticalThreshold = _SensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 10),
    _SensorLowerCriticalThreshold_Type()
)
sensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorLowerCriticalThreshold.setStatus("current")
_SensorLowerWarningThreshold_Type = Integer32
_SensorLowerWarningThreshold_Object = MibTableColumn
sensorLowerWarningThreshold = _SensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 11),
    _SensorLowerWarningThreshold_Type()
)
sensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorLowerWarningThreshold.setStatus("current")
_SensorUpperCriticalThreshold_Type = Integer32
_SensorUpperCriticalThreshold_Object = MibTableColumn
sensorUpperCriticalThreshold = _SensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 12),
    _SensorUpperCriticalThreshold_Type()
)
sensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorUpperCriticalThreshold.setStatus("current")
_SensorUpperWarningThreshold_Type = Integer32
_SensorUpperWarningThreshold_Object = MibTableColumn
sensorUpperWarningThreshold = _SensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 13),
    _SensorUpperWarningThreshold_Type()
)
sensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorUpperWarningThreshold.setStatus("current")


class _SensorEnabledThresholds_Type(Bits):
    """Custom type sensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_SensorEnabledThresholds_Type.__name__ = "Bits"
_SensorEnabledThresholds_Object = MibTableColumn
sensorEnabledThresholds = _SensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 14),
    _SensorEnabledThresholds_Type()
)
sensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorEnabledThresholds.setStatus("current")
_SensorThresholdMaximum_Type = Integer32
_SensorThresholdMaximum_Object = MibTableColumn
sensorThresholdMaximum = _SensorThresholdMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 15),
    _SensorThresholdMaximum_Type()
)
sensorThresholdMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorThresholdMaximum.setStatus("current")
_SensorThresholdMinimum_Type = Integer32
_SensorThresholdMinimum_Object = MibTableColumn
sensorThresholdMinimum = _SensorThresholdMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 16),
    _SensorThresholdMinimum_Type()
)
sensorThresholdMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorThresholdMinimum.setStatus("current")
_SensorName_Type = DisplayString
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 4, 1, 1, 17),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")
_Measurements_ObjectIdentity = ObjectIdentity
measurements = _Measurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2)
)
_SensorMeasurementsTable_Object = MibTable
sensorMeasurementsTable = _SensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1)
)
if mibBuilder.loadTexts:
    sensorMeasurementsTable.setStatus("current")
_SensorMeasurementsEntry_Object = MibTableRow
sensorMeasurementsEntry = _SensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1)
)
sensorMeasurementsEntry.setIndexNames(
    (0, "LHX-MIB", "portIdx"),
    (0, "LHX-MIB", "sensorTypeIdx"),
    (0, "LHX-MIB", "sensorIdx"),
)
if mibBuilder.loadTexts:
    sensorMeasurementsEntry.setStatus("current")
_MeasurementsSensorIsAvailable_Type = TruthValue
_MeasurementsSensorIsAvailable_Object = MibTableColumn
measurementsSensorIsAvailable = _MeasurementsSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 1),
    _MeasurementsSensorIsAvailable_Type()
)
measurementsSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsSensorIsAvailable.setStatus("current")
_MeasurementsSensorState_Type = SensorStateEnumeration
_MeasurementsSensorState_Object = MibTableColumn
measurementsSensorState = _MeasurementsSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 2),
    _MeasurementsSensorState_Type()
)
measurementsSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsSensorState.setStatus("current")
_MeasurementsSensorValue_Type = Integer32
_MeasurementsSensorValue_Object = MibTableColumn
measurementsSensorValue = _MeasurementsSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 3),
    _MeasurementsSensorValue_Type()
)
measurementsSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsSensorValue.setStatus("current")
_MeasurementsSensorTimeStamp_Type = Unsigned32
_MeasurementsSensorTimeStamp_Object = MibTableColumn
measurementsSensorTimeStamp = _MeasurementsSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1, 1, 4),
    _MeasurementsSensorTimeStamp_Type()
)
measurementsSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsSensorTimeStamp.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3, 2)
)

# Managed Objects groups

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 1)
)
configurationGroup.setObjects(
      *(("LHX-MIB", "portCount"),
        ("LHX-MIB", "portId"),
        ("LHX-MIB", "operationalState"),
        ("LHX-MIB", "sensorCount"),
        ("LHX-MIB", "sensorLabel"),
        ("LHX-MIB", "sensorUnit"),
        ("LHX-MIB", "sensorDecimalDigits"),
        ("LHX-MIB", "sensorMaximum"),
        ("LHX-MIB", "sensorMinimum"),
        ("LHX-MIB", "sensorHysteresis"),
        ("LHX-MIB", "sensorLowerCriticalThreshold"),
        ("LHX-MIB", "sensorLowerWarningThreshold"),
        ("LHX-MIB", "sensorUpperCriticalThreshold"),
        ("LHX-MIB", "sensorUpperWarningThreshold"),
        ("LHX-MIB", "sensorEnabledThresholds"),
        ("LHX-MIB", "setpointVentilators"),
        ("LHX-MIB", "setpointWaterValve"),
        ("LHX-MIB", "defaultFanSpeed"),
        ("LHX-MIB", "maximumCoolingState"),
        ("LHX-MIB", "alertState"),
        ("LHX-MIB", "sensorThresholdMaximum"),
        ("LHX-MIB", "sensorThresholdMinimum"),
        ("LHX-MIB", "model"),
        ("LHX-MIB", "fwVersion"),
        ("LHX-MIB", "sensorName"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

measurementsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 2)
)
measurementsGroup.setObjects(
      *(("LHX-MIB", "measurementsSensorIsAvailable"),
        ("LHX-MIB", "measurementsSensorState"),
        ("LHX-MIB", "measurementsSensorValue"),
        ("LHX-MIB", "measurementsSensorTimeStamp"))
)
if mibBuilder.loadTexts:
    measurementsGroup.setStatus("current")

trapInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 3)
)
trapInformationGroup.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"),
        ("LHX-MIB", "probeId"),
        ("LHX-MIB", "fanId"),
        ("LHX-MIB", "powerSupplyId"),
        ("LHX-MIB", "oldSensorState"),
        ("LHX-MIB", "sensorTypeId"),
        ("LHX-MIB", "sensorId"),
        ("LHX-MIB", "oldOperationalState"),
        ("LHX-MIB", "agentInetPortNumber"))
)
if mibBuilder.loadTexts:
    trapInformationGroup.setStatus("current")


# Notification objects

lhxSensorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 1)
)
lhxSensorFailure.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"),
        ("LHX-MIB", "probeId"))
)
if mibBuilder.loadTexts:
    lhxSensorFailure.setStatus(
        "current"
    )

lhxFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 2)
)
lhxFanFailure.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"),
        ("LHX-MIB", "fanId"))
)
if mibBuilder.loadTexts:
    lhxFanFailure.setStatus(
        "current"
    )

lhxPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 3)
)
lhxPowerSupplyFailure.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"),
        ("LHX-MIB", "powerSupplyId"))
)
if mibBuilder.loadTexts:
    lhxPowerSupplyFailure.setStatus(
        "current"
    )

lhxThresholdAirOutlet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 4)
)
lhxThresholdAirOutlet.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxThresholdAirOutlet.setStatus(
        "current"
    )

lhxThresholdAirInlet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 5)
)
lhxThresholdAirInlet.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxThresholdAirInlet.setStatus(
        "current"
    )

lhxThresholdWaterInlet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 6)
)
lhxThresholdWaterInlet.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxThresholdWaterInlet.setStatus(
        "current"
    )

lhxDoorOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 7)
)
lhxDoorOpened.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxDoorOpened.setStatus(
        "current"
    )

lhxMaximumCoolingRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 8)
)
lhxMaximumCoolingRequest.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxMaximumCoolingRequest.setStatus(
        "current"
    )

lhxEmergencyCooling = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 9)
)
lhxEmergencyCooling.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxEmergencyCooling.setStatus(
        "current"
    )

lhxWaterLeak = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 10)
)
lhxWaterLeak.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxWaterLeak.setStatus(
        "current"
    )

lhxThresholdHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 11)
)
lhxThresholdHumidity.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxThresholdHumidity.setStatus(
        "current"
    )

lhxExternalWaterCoolingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 12)
)
lhxExternalWaterCoolingFailure.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxExternalWaterCoolingFailure.setStatus(
        "current"
    )

lhxThresholdWaterOutlet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 13)
)
lhxThresholdWaterOutlet.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxThresholdWaterOutlet.setStatus(
        "current"
    )

lhxParameterDataLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 14)
)
lhxParameterDataLoss.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxParameterDataLoss.setStatus(
        "current"
    )

lhxStBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 15)
)
lhxStBusError.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxStBusError.setStatus(
        "current"
    )

lhxCollectiveFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 16)
)
lhxCollectiveFault.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxCollectiveFault.setStatus(
        "current"
    )

gwSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 17)
)
gwSensorStateChange.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "portId"),
        ("LHX-MIB", "sensorTypeId"),
        ("LHX-MIB", "sensorId"),
        ("LHX-MIB", "probeId"),
        ("LHX-MIB", "measurementsSensorTimeStamp"),
        ("LHX-MIB", "measurementsSensorValue"),
        ("LHX-MIB", "measurementsSensorState"),
        ("LHX-MIB", "oldSensorState"))
)
if mibBuilder.loadTexts:
    gwSensorStateChange.setStatus(
        "current"
    )

gwLhxOperationalStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 18)
)
gwLhxOperationalStateChange.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "portId"),
        ("LHX-MIB", "operationalState"),
        ("LHX-MIB", "oldOperationalState"))
)
if mibBuilder.loadTexts:
    gwLhxOperationalStateChange.setStatus(
        "current"
    )

lhxVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 19)
)
lhxVoltageLow.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxVoltageLow.setStatus(
        "current"
    )

lhxBaseElectronicsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 20)
)
lhxBaseElectronicsFailure.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxBaseElectronicsFailure.setStatus(
        "current"
    )

lhxCondenserPumpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 9, 0, 21)
)
lhxCondenserPumpFailure.setObjects(
      *(("LHX-MIB", "deviceName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("LHX-MIB", "deviceInetAddressType"),
        ("LHX-MIB", "deviceInetIPAddress"),
        ("LHX-MIB", "lhxErrorCode"),
        ("LHX-MIB", "agentInetPortNumber"),
        ("LHX-MIB", "portId"))
)
if mibBuilder.loadTexts:
    lhxCondenserPumpFailure.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3, 2, 4)
)
trapsGroup.setObjects(
      *(("LHX-MIB", "lhxSensorFailure"),
        ("LHX-MIB", "lhxFanFailure"),
        ("LHX-MIB", "lhxPowerSupplyFailure"),
        ("LHX-MIB", "lhxThresholdAirOutlet"),
        ("LHX-MIB", "lhxThresholdAirInlet"),
        ("LHX-MIB", "lhxThresholdWaterInlet"),
        ("LHX-MIB", "lhxDoorOpened"),
        ("LHX-MIB", "lhxMaximumCoolingRequest"),
        ("LHX-MIB", "lhxEmergencyCooling"),
        ("LHX-MIB", "lhxWaterLeak"),
        ("LHX-MIB", "lhxThresholdHumidity"),
        ("LHX-MIB", "lhxExternalWaterCoolingFailure"),
        ("LHX-MIB", "lhxThresholdWaterOutlet"),
        ("LHX-MIB", "lhxParameterDataLoss"),
        ("LHX-MIB", "lhxStBusError"),
        ("LHX-MIB", "lhxCondenserPumpFailure"),
        ("LHX-MIB", "gwSensorStateChange"),
        ("LHX-MIB", "gwLhxOperationalStateChange"),
        ("LHX-MIB", "lhxCollectiveFault"),
        ("LHX-MIB", "lhxVoltageLow"),
        ("LHX-MIB", "lhxBaseElectronicsFailure"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

complianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    complianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LHX-MIB",
    **{"OperationalStateEnumeration": OperationalStateEnumeration,
       "GwSensorTypeEnumeration": GwSensorTypeEnumeration,
       "SensorUnitsEnumeration": SensorUnitsEnumeration,
       "SensorStateEnumeration": SensorStateEnumeration,
       "raritan": raritan,
       "lhxgw": lhxgw,
       "traps": traps,
       "trapInformation": trapInformation,
       "deviceName": deviceName,
       "deviceInetAddressType": deviceInetAddressType,
       "deviceInetIPAddress": deviceInetIPAddress,
       "lhxErrorCode": lhxErrorCode,
       "portId": portId,
       "probeId": probeId,
       "fanId": fanId,
       "powerSupplyId": powerSupplyId,
       "oldSensorState": oldSensorState,
       "sensorTypeId": sensorTypeId,
       "sensorId": sensorId,
       "oldOperationalState": oldOperationalState,
       "agentInetPortNumber": agentInetPortNumber,
       "lhxSensorFailure": lhxSensorFailure,
       "lhxFanFailure": lhxFanFailure,
       "lhxPowerSupplyFailure": lhxPowerSupplyFailure,
       "lhxThresholdAirOutlet": lhxThresholdAirOutlet,
       "lhxThresholdAirInlet": lhxThresholdAirInlet,
       "lhxThresholdWaterInlet": lhxThresholdWaterInlet,
       "lhxDoorOpened": lhxDoorOpened,
       "lhxMaximumCoolingRequest": lhxMaximumCoolingRequest,
       "lhxEmergencyCooling": lhxEmergencyCooling,
       "lhxWaterLeak": lhxWaterLeak,
       "lhxThresholdHumidity": lhxThresholdHumidity,
       "lhxExternalWaterCoolingFailure": lhxExternalWaterCoolingFailure,
       "lhxThresholdWaterOutlet": lhxThresholdWaterOutlet,
       "lhxParameterDataLoss": lhxParameterDataLoss,
       "lhxStBusError": lhxStBusError,
       "lhxCollectiveFault": lhxCollectiveFault,
       "gwSensorStateChange": gwSensorStateChange,
       "gwLhxOperationalStateChange": gwLhxOperationalStateChange,
       "lhxVoltageLow": lhxVoltageLow,
       "lhxBaseElectronicsFailure": lhxBaseElectronicsFailure,
       "lhxCondenserPumpFailure": lhxCondenserPumpFailure,
       "configuration": configuration,
       "portCount": portCount,
       "sensorCountTable": sensorCountTable,
       "sensorCountEntry": sensorCountEntry,
       "sensorCount": sensorCount,
       "lhx": lhx,
       "lhxConfigurationTable": lhxConfigurationTable,
       "lhxConfigurationEntry": lhxConfigurationEntry,
       "operationalState": operationalState,
       "setpointVentilators": setpointVentilators,
       "setpointWaterValve": setpointWaterValve,
       "defaultFanSpeed": defaultFanSpeed,
       "maximumCoolingState": maximumCoolingState,
       "alertState": alertState,
       "model": model,
       "fwVersion": fwVersion,
       "gwSensors": gwSensors,
       "sensorConfigurationTable": sensorConfigurationTable,
       "sensorConfigurationEntry": sensorConfigurationEntry,
       "portIdx": portIdx,
       "sensorTypeIdx": sensorTypeIdx,
       "sensorIdx": sensorIdx,
       "sensorLabel": sensorLabel,
       "sensorUnit": sensorUnit,
       "sensorDecimalDigits": sensorDecimalDigits,
       "sensorMaximum": sensorMaximum,
       "sensorMinimum": sensorMinimum,
       "sensorHysteresis": sensorHysteresis,
       "sensorLowerCriticalThreshold": sensorLowerCriticalThreshold,
       "sensorLowerWarningThreshold": sensorLowerWarningThreshold,
       "sensorUpperCriticalThreshold": sensorUpperCriticalThreshold,
       "sensorUpperWarningThreshold": sensorUpperWarningThreshold,
       "sensorEnabledThresholds": sensorEnabledThresholds,
       "sensorThresholdMaximum": sensorThresholdMaximum,
       "sensorThresholdMinimum": sensorThresholdMinimum,
       "sensorName": sensorName,
       "measurements": measurements,
       "sensorMeasurementsTable": sensorMeasurementsTable,
       "sensorMeasurementsEntry": sensorMeasurementsEntry,
       "measurementsSensorIsAvailable": measurementsSensorIsAvailable,
       "measurementsSensorState": measurementsSensorState,
       "measurementsSensorValue": measurementsSensorValue,
       "measurementsSensorTimeStamp": measurementsSensorTimeStamp,
       "conformance": conformance,
       "compliances": compliances,
       "complianceRev1": complianceRev1,
       "groups": groups,
       "configurationGroup": configurationGroup,
       "measurementsGroup": measurementsGroup,
       "trapInformationGroup": trapInformationGroup,
       "trapsGroup": trapsGroup}
)
