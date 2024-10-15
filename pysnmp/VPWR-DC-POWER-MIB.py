# SNMP MIB module (VPWR-DC-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPWR-DC-POWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:17 2024
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

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

valereDcPowerMgt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13858)
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

_VpwrDcPowerProducts_ObjectIdentity = ObjectIdentity
vpwrDcPowerProducts = _VpwrDcPowerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 1)
)
_VpwrDcPowerSystem_ObjectIdentity = ObjectIdentity
vpwrDcPowerSystem = _VpwrDcPowerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2)
)
_VpwrSystemIdentGroup_ObjectIdentity = ObjectIdentity
vpwrSystemIdentGroup = _VpwrSystemIdentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1)
)


class _VpwrIdentManufacturer_Type(DisplayString):
    """Custom type vpwrIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VpwrIdentManufacturer_Type.__name__ = "DisplayString"
_VpwrIdentManufacturer_Object = MibScalar
vpwrIdentManufacturer = _VpwrIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 1),
    _VpwrIdentManufacturer_Type()
)
vpwrIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentManufacturer.setStatus("current")


class _VpwrIdentModel_Type(DisplayString):
    """Custom type vpwrIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VpwrIdentModel_Type.__name__ = "DisplayString"
_VpwrIdentModel_Object = MibScalar
vpwrIdentModel = _VpwrIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 2),
    _VpwrIdentModel_Type()
)
vpwrIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentModel.setStatus("current")


class _VpwrIdentControllerVersion_Type(DisplayString):
    """Custom type vpwrIdentControllerVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VpwrIdentControllerVersion_Type.__name__ = "DisplayString"
_VpwrIdentControllerVersion_Object = MibScalar
vpwrIdentControllerVersion = _VpwrIdentControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 3),
    _VpwrIdentControllerVersion_Type()
)
vpwrIdentControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentControllerVersion.setStatus("current")


class _VpwrIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type vpwrIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VpwrIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_VpwrIdentAgentSoftwareVersion_Object = MibScalar
vpwrIdentAgentSoftwareVersion = _VpwrIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 4),
    _VpwrIdentAgentSoftwareVersion_Type()
)
vpwrIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrIdentAgentSoftwareVersion.setStatus("current")


class _VpwrIdentName_Type(DisplayString):
    """Custom type vpwrIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VpwrIdentName_Type.__name__ = "DisplayString"
_VpwrIdentName_Object = MibScalar
vpwrIdentName = _VpwrIdentName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 5),
    _VpwrIdentName_Type()
)
vpwrIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrIdentName.setStatus("current")
_VpwrSystemIdentTable_Object = MibTable
vpwrSystemIdentTable = _VpwrSystemIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6)
)
if mibBuilder.loadTexts:
    vpwrSystemIdentTable.setStatus("current")
_VpwrSystemIdentEntry_Object = MibTableRow
vpwrSystemIdentEntry = _VpwrSystemIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1)
)
vpwrSystemIdentEntry.setIndexNames(
    (0, "VPWR-DC-POWER-MIB", "vpwrShelfIndex"),
    (0, "VPWR-DC-POWER-MIB", "vpwrModuleIndex"),
)
if mibBuilder.loadTexts:
    vpwrSystemIdentEntry.setStatus("current")
_VpwrShelfIndex_Type = PositiveInteger
_VpwrShelfIndex_Object = MibTableColumn
vpwrShelfIndex = _VpwrShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 1),
    _VpwrShelfIndex_Type()
)
vpwrShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrShelfIndex.setStatus("current")
_VpwrModuleIndex_Type = PositiveInteger
_VpwrModuleIndex_Object = MibTableColumn
vpwrModuleIndex = _VpwrModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 2),
    _VpwrModuleIndex_Type()
)
vpwrModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleIndex.setStatus("current")
_VpwrModuleOID_Type = ObjectIdentifier
_VpwrModuleOID_Object = MibTableColumn
vpwrModuleOID = _VpwrModuleOID_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 3),
    _VpwrModuleOID_Type()
)
vpwrModuleOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleOID.setStatus("current")
_VpwrModuleParameter_Type = Integer32
_VpwrModuleParameter_Object = MibTableColumn
vpwrModuleParameter = _VpwrModuleParameter_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 4),
    _VpwrModuleParameter_Type()
)
vpwrModuleParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleParameter.setStatus("current")


class _VpwrModuleOperStatus_Type(Integer32):
    """Custom type vpwrModuleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("moduleStatusAlarm", 1),
          ("moduleStatusOK", 0))
    )


_VpwrModuleOperStatus_Type.__name__ = "Integer32"
_VpwrModuleOperStatus_Object = MibTableColumn
vpwrModuleOperStatus = _VpwrModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 5),
    _VpwrModuleOperStatus_Type()
)
vpwrModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleOperStatus.setStatus("current")
_VpwrModuleCapacity_Type = Integer32
_VpwrModuleCapacity_Object = MibTableColumn
vpwrModuleCapacity = _VpwrModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 6),
    _VpwrModuleCapacity_Type()
)
vpwrModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleCapacity.setStatus("current")
_VpwrSystemConfigGroup_ObjectIdentity = ObjectIdentity
vpwrSystemConfigGroup = _VpwrSystemConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2)
)


class _VpwrSystemTempCompensation_Type(Integer32):
    """Custom type vpwrSystemTempCompensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tempCompDisabled", 0),
          ("tempCompEnabled", 1))
    )


_VpwrSystemTempCompensation_Type.__name__ = "Integer32"
_VpwrSystemTempCompensation_Object = MibScalar
vpwrSystemTempCompensation = _VpwrSystemTempCompensation_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 1),
    _VpwrSystemTempCompensation_Type()
)
vpwrSystemTempCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensation.setStatus("current")


class _VpwrSystemTempCompStartTemperature_Type(Integer32):
    """Custom type vpwrSystemTempCompStartTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 60),
    )


_VpwrSystemTempCompStartTemperature_Type.__name__ = "Integer32"
_VpwrSystemTempCompStartTemperature_Object = MibScalar
vpwrSystemTempCompStartTemperature = _VpwrSystemTempCompStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 2),
    _VpwrSystemTempCompStartTemperature_Type()
)
vpwrSystemTempCompStartTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStartTemperature.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStartTemperature.setUnits("degrees Centigrade")
_VpwrSystemTempCompStopVoltage_Type = Integer32
_VpwrSystemTempCompStopVoltage_Object = MibScalar
vpwrSystemTempCompStopVoltage = _VpwrSystemTempCompStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 3),
    _VpwrSystemTempCompStopVoltage_Type()
)
vpwrSystemTempCompStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemTempCompStopVoltage.setUnits(" vpwrSystemTempCompStopVoltage *.01 Volts")


class _VpwrSystemTempCompensationSlope_Type(Integer32):
    """Custom type vpwrSystemTempCompensationSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_VpwrSystemTempCompensationSlope_Type.__name__ = "Integer32"
_VpwrSystemTempCompensationSlope_Object = MibScalar
vpwrSystemTempCompensationSlope = _VpwrSystemTempCompensationSlope_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 4),
    _VpwrSystemTempCompensationSlope_Type()
)
vpwrSystemTempCompensationSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensationSlope.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensationSlope.setUnits(" milli-Volts per degrees Centigrade")


class _VpwrSystemThermalSenseType_Type(Integer32):
    """Custom type vpwrSystemThermalSenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 0),
          ("internal", 1))
    )


_VpwrSystemThermalSenseType_Type.__name__ = "Integer32"
_VpwrSystemThermalSenseType_Object = MibScalar
vpwrSystemThermalSenseType = _VpwrSystemThermalSenseType_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 5),
    _VpwrSystemThermalSenseType_Type()
)
vpwrSystemThermalSenseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemThermalSenseType.setStatus("current")
_VpwrSystemHVAlarmSetpoint_Type = Integer32
_VpwrSystemHVAlarmSetpoint_Object = MibScalar
vpwrSystemHVAlarmSetpoint = _VpwrSystemHVAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 6),
    _VpwrSystemHVAlarmSetpoint_Type()
)
vpwrSystemHVAlarmSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemHVAlarmSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemHVAlarmSetpoint.setUnits(" vpwrSystemHVAlarmSetpoint *.01 Volts")
_VpwrSystemBDAlarmSetpoint_Type = Integer32
_VpwrSystemBDAlarmSetpoint_Object = MibScalar
vpwrSystemBDAlarmSetpoint = _VpwrSystemBDAlarmSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 7),
    _VpwrSystemBDAlarmSetpoint_Type()
)
vpwrSystemBDAlarmSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemBDAlarmSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemBDAlarmSetpoint.setUnits(" vpwrSystemBDAlarmSetpoint *.01 Volts")
_VpwrSystemInternalTempLThreshold_Type = Integer32
_VpwrSystemInternalTempLThreshold_Object = MibScalar
vpwrSystemInternalTempLThreshold = _VpwrSystemInternalTempLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 8),
    _VpwrSystemInternalTempLThreshold_Type()
)
vpwrSystemInternalTempLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempLThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempLThreshold.setUnits("degrees Centigrade")
_VpwrSystemInternalTempUThreshold_Type = Integer32
_VpwrSystemInternalTempUThreshold_Object = MibScalar
vpwrSystemInternalTempUThreshold = _VpwrSystemInternalTempUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 2, 9),
    _VpwrSystemInternalTempUThreshold_Type()
)
vpwrSystemInternalTempUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempUThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemInternalTempUThreshold.setUnits("degrees Centigrade")
_VpwrSystemParameterGroup_ObjectIdentity = ObjectIdentity
vpwrSystemParameterGroup = _VpwrSystemParameterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3)
)


class _VpwrSystemShelfCapacity_Type(Integer32):
    """Custom type vpwrSystemShelfCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VpwrSystemShelfCapacity_Type.__name__ = "Integer32"
_VpwrSystemShelfCapacity_Object = MibScalar
vpwrSystemShelfCapacity = _VpwrSystemShelfCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 1),
    _VpwrSystemShelfCapacity_Type()
)
vpwrSystemShelfCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemShelfCapacity.setStatus("current")
_VpwrSystemVoltage_Type = Integer32
_VpwrSystemVoltage_Object = MibScalar
vpwrSystemVoltage = _VpwrSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 2),
    _VpwrSystemVoltage_Type()
)
vpwrSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemVoltage.setUnits(" vpwrSystemVoltage *.01 Volts")
_VpwrSystemCurrent_Type = Integer32
_VpwrSystemCurrent_Object = MibScalar
vpwrSystemCurrent = _VpwrSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 3),
    _VpwrSystemCurrent_Type()
)
vpwrSystemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemCurrent.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemCurrent.setUnits(" Amperes")


class _VpwrSystemControllerState_Type(Integer32):
    """Custom type vpwrSystemControllerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("systemControllerStateAlarm", 3),
          ("systemControllerStateChange", 2),
          ("systemControllerStateIrActive", 5),
          ("systemControllerStateMenu", 4),
          ("systemControllerStateNormal", 1),
          ("systemControllerStateUnknown", 0))
    )


_VpwrSystemControllerState_Type.__name__ = "Integer32"
_VpwrSystemControllerState_Object = MibScalar
vpwrSystemControllerState = _VpwrSystemControllerState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 4),
    _VpwrSystemControllerState_Type()
)
vpwrSystemControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemControllerState.setStatus("current")
_VpwrSystemInternalTemperature_Type = Integer32
_VpwrSystemInternalTemperature_Object = MibScalar
vpwrSystemInternalTemperature = _VpwrSystemInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 5),
    _VpwrSystemInternalTemperature_Type()
)
vpwrSystemInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemInternalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    vpwrSystemInternalTemperature.setUnits("degrees Centigrade")


class _VpwrSystemTempCompensationState_Type(Integer32):
    """Custom type vpwrSystemTempCompensationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("systemTempCompActive", 1),
          ("systemTempCompInactive", 0))
    )


_VpwrSystemTempCompensationState_Type.__name__ = "Integer32"
_VpwrSystemTempCompensationState_Object = MibScalar
vpwrSystemTempCompensationState = _VpwrSystemTempCompensationState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 6),
    _VpwrSystemTempCompensationState_Type()
)
vpwrSystemTempCompensationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemTempCompensationState.setStatus("current")


class _VpwrSystemType_Type(Integer32):
    """Custom type vpwrSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sysType24V", 1),
          ("sysType48V", 0))
    )


_VpwrSystemType_Type.__name__ = "Integer32"
_VpwrSystemType_Object = MibScalar
vpwrSystemType = _VpwrSystemType_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 3, 7),
    _VpwrSystemType_Type()
)
vpwrSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrSystemType.setStatus("current")
_VpwrDcPowerRectifier_ObjectIdentity = ObjectIdentity
vpwrDcPowerRectifier = _VpwrDcPowerRectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3)
)
_VpwrRectifierConfigGroup_ObjectIdentity = ObjectIdentity
vpwrRectifierConfigGroup = _VpwrRectifierConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1)
)
_VpwrRectifierFVSetpoint_Type = Integer32
_VpwrRectifierFVSetpoint_Object = MibScalar
vpwrRectifierFVSetpoint = _VpwrRectifierFVSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 1),
    _VpwrRectifierFVSetpoint_Type()
)
vpwrRectifierFVSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierFVSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRectifierFVSetpoint.setUnits(" vpwrRectifierFVSetpoint *.01 Volts")
_VpwrRectifierHVSDSetpoint_Type = Integer32
_VpwrRectifierHVSDSetpoint_Object = MibScalar
vpwrRectifierHVSDSetpoint = _VpwrRectifierHVSDSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 2),
    _VpwrRectifierHVSDSetpoint_Type()
)
vpwrRectifierHVSDSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierHVSDSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRectifierHVSDSetpoint.setUnits(" vpwrRectifierHVSDSetpoint *.01 Volts")
_VpwrRectifierAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrRectifierAlarmGroup = _VpwrRectifierAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2)
)
_VpwrRectAlarmDCFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmDCFail = _VpwrRectAlarmDCFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmDCFail.setStatus("current")
_VpwrRectAlarmBoostFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmBoostFail = _VpwrRectAlarmBoostFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 2)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmBoostFail.setStatus("current")
_VpwrRectAlarmACFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmACFail = _VpwrRectAlarmACFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 3)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmACFail.setStatus("current")
_VpwrRectAlarmHVSD_ObjectIdentity = ObjectIdentity
vpwrRectAlarmHVSD = _VpwrRectAlarmHVSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmHVSD.setStatus("current")
_VpwrRectAlarmFanFail_ObjectIdentity = ObjectIdentity
vpwrRectAlarmFanFail = _VpwrRectAlarmFanFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 5)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmFanFail.setStatus("current")
_VpwrRectAlarmAmbTemp_ObjectIdentity = ObjectIdentity
vpwrRectAlarmAmbTemp = _VpwrRectAlarmAmbTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 6)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmAmbTemp.setStatus("current")
_VpwrRectAlarmIntTemp_ObjectIdentity = ObjectIdentity
vpwrRectAlarmIntTemp = _VpwrRectAlarmIntTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 7)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmIntTemp.setStatus("current")
_VpwrRectAlarmIShare_ObjectIdentity = ObjectIdentity
vpwrRectAlarmIShare = _VpwrRectAlarmIShare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 8)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmIShare.setStatus("current")
_VpwrRectAlarmUV_ObjectIdentity = ObjectIdentity
vpwrRectAlarmUV = _VpwrRectAlarmUV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 9)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmUV.setStatus("current")
_VpwrRectAlarmLowVoltage_ObjectIdentity = ObjectIdentity
vpwrRectAlarmLowVoltage = _VpwrRectAlarmLowVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmLowVoltage.setStatus("current")
_VpwrRectAlarmReserved_ObjectIdentity = ObjectIdentity
vpwrRectAlarmReserved = _VpwrRectAlarmReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 11)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmReserved.setStatus("current")
_VpwrRectAlarmDCEnable_ObjectIdentity = ObjectIdentity
vpwrRectAlarmDCEnable = _VpwrRectAlarmDCEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 12)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmDCEnable.setStatus("current")
_VpwrRectAlarmRemoteShutdown_ObjectIdentity = ObjectIdentity
vpwrRectAlarmRemoteShutdown = _VpwrRectAlarmRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 13)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmRemoteShutdown.setStatus("current")
_VpwrRectAlarmModDisableShutdown_ObjectIdentity = ObjectIdentity
vpwrRectAlarmModDisableShutdown = _VpwrRectAlarmModDisableShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 14)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmModDisableShutdown.setStatus("current")
_VpwrRectAlarmShortPinShutdown_ObjectIdentity = ObjectIdentity
vpwrRectAlarmShortPinShutdown = _VpwrRectAlarmShortPinShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 15)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmShortPinShutdown.setStatus("current")
_VpwrRectAlarmBoostComm_ObjectIdentity = ObjectIdentity
vpwrRectAlarmBoostComm = _VpwrRectAlarmBoostComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 2, 16)
)
if mibBuilder.loadTexts:
    vpwrRectAlarmBoostComm.setStatus("current")
_VpwrRectifierTestGroup_ObjectIdentity = ObjectIdentity
vpwrRectifierTestGroup = _VpwrRectifierTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 3, 3)
)
_VpwrDcPowerLvd_ObjectIdentity = ObjectIdentity
vpwrDcPowerLvd = _VpwrDcPowerLvd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4)
)
_VpwrLvdConfigGroup_ObjectIdentity = ObjectIdentity
vpwrLvdConfigGroup = _VpwrLvdConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1)
)
_VpwrLvdWarningSetpoint_Type = Integer32
_VpwrLvdWarningSetpoint_Object = MibScalar
vpwrLvdWarningSetpoint = _VpwrLvdWarningSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 1),
    _VpwrLvdWarningSetpoint_Type()
)
vpwrLvdWarningSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdWarningSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdWarningSetpoint.setUnits(" vpwrLvdWarningSetpoint * .01 Volts")
_VpwrLvdDisconnectSetpoint_Type = Integer32
_VpwrLvdDisconnectSetpoint_Object = MibScalar
vpwrLvdDisconnectSetpoint = _VpwrLvdDisconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 2),
    _VpwrLvdDisconnectSetpoint_Type()
)
vpwrLvdDisconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdDisconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdDisconnectSetpoint.setUnits(" vpwrLvdDisconnectSetpoint *.01 Volts")
_VpwrLvdReconnectSetpoint_Type = Integer32
_VpwrLvdReconnectSetpoint_Object = MibScalar
vpwrLvdReconnectSetpoint = _VpwrLvdReconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 3),
    _VpwrLvdReconnectSetpoint_Type()
)
vpwrLvdReconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdReconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdReconnectSetpoint.setUnits(" vpwrLvdReconnectSetpoint *.01 Volts")


class _VpwrLvdReconnectDelayTimer_Type(Integer32):
    """Custom type vpwrLvdReconnectDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 240),
    )


_VpwrLvdReconnectDelayTimer_Type.__name__ = "Integer32"
_VpwrLvdReconnectDelayTimer_Object = MibScalar
vpwrLvdReconnectDelayTimer = _VpwrLvdReconnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 4),
    _VpwrLvdReconnectDelayTimer_Type()
)
vpwrLvdReconnectDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdReconnectDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdReconnectDelayTimer.setUnits(" Seconds")
_VpwrLvdAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrLvdAlarmGroup = _VpwrLvdAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 2)
)
_VpwrLvdAlarmContactorOpen_ObjectIdentity = ObjectIdentity
vpwrLvdAlarmContactorOpen = _VpwrLvdAlarmContactorOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vpwrLvdAlarmContactorOpen.setStatus("current")
_VpwrLvdAlarmCBOpen_ObjectIdentity = ObjectIdentity
vpwrLvdAlarmCBOpen = _VpwrLvdAlarmCBOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 2, 2)
)
if mibBuilder.loadTexts:
    vpwrLvdAlarmCBOpen.setStatus("current")
_VpwrTrapLvdFuseOpen_ObjectIdentity = ObjectIdentity
vpwrTrapLvdFuseOpen = _VpwrTrapLvdFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 2, 3)
)
if mibBuilder.loadTexts:
    vpwrTrapLvdFuseOpen.setStatus("current")
_VpwrLvdAlarmWarning_ObjectIdentity = ObjectIdentity
vpwrLvdAlarmWarning = _VpwrLvdAlarmWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 2, 4)
)
if mibBuilder.loadTexts:
    vpwrLvdAlarmWarning.setStatus("current")
_VpwrLvdTestGroup_ObjectIdentity = ObjectIdentity
vpwrLvdTestGroup = _VpwrLvdTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 4, 3)
)
_VpwrDcPowerTest_ObjectIdentity = ObjectIdentity
vpwrDcPowerTest = _VpwrDcPowerTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 5)
)
_VpwrDcPowerModuleIdent_ObjectIdentity = ObjectIdentity
vpwrDcPowerModuleIdent = _VpwrDcPowerModuleIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 6)
)
_VpwrDcPowerBatteryGroup_ObjectIdentity = ObjectIdentity
vpwrDcPowerBatteryGroup = _VpwrDcPowerBatteryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7)
)
_VpwrBatteryTempGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryTempGroup = _VpwrBatteryTempGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1)
)
_VpwrBatteryTempTable_Object = MibTable
vpwrBatteryTempTable = _VpwrBatteryTempTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1)
)
if mibBuilder.loadTexts:
    vpwrBatteryTempTable.setStatus("current")
_VpwrBatteryTempTableEntry_Object = MibTableRow
vpwrBatteryTempTableEntry = _VpwrBatteryTempTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1)
)
vpwrBatteryTempTableEntry.setIndexNames(
    (0, "VPWR-DC-POWER-MIB", "vpwrBatteryTempIndex"),
)
if mibBuilder.loadTexts:
    vpwrBatteryTempTableEntry.setStatus("current")
_VpwrBatteryTempIndex_Type = Integer32
_VpwrBatteryTempIndex_Object = MibTableColumn
vpwrBatteryTempIndex = _VpwrBatteryTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1, 1),
    _VpwrBatteryTempIndex_Type()
)
vpwrBatteryTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBatteryTempIndex.setStatus("current")


class _VpwrBatteryTempName_Type(DisplayString):
    """Custom type vpwrBatteryTempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_VpwrBatteryTempName_Type.__name__ = "DisplayString"
_VpwrBatteryTempName_Object = MibTableColumn
vpwrBatteryTempName = _VpwrBatteryTempName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1, 2),
    _VpwrBatteryTempName_Type()
)
vpwrBatteryTempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryTempName.setStatus("current")
_VpwrBatteryTemp_Type = Integer32
_VpwrBatteryTemp_Object = MibTableColumn
vpwrBatteryTemp = _VpwrBatteryTemp_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1, 3),
    _VpwrBatteryTemp_Type()
)
vpwrBatteryTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBatteryTemp.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryTemp.setUnits("degrees Centigrade")
_VpwrBatteryTempLThreshold_Type = Integer32
_VpwrBatteryTempLThreshold_Object = MibScalar
vpwrBatteryTempLThreshold = _VpwrBatteryTempLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 2),
    _VpwrBatteryTempLThreshold_Type()
)
vpwrBatteryTempLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryTempLThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryTempLThreshold.setUnits("degrees Centigrade")
_VpwrBatteryTempUThreshold_Type = Integer32
_VpwrBatteryTempUThreshold_Object = MibScalar
vpwrBatteryTempUThreshold = _VpwrBatteryTempUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 3),
    _VpwrBatteryTempUThreshold_Type()
)
vpwrBatteryTempUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryTempUThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBatteryTempUThreshold.setUnits("degrees Centigrade")
_VpwrDcPowerAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrDcPowerAlarmGroup = _VpwrDcPowerAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 8)
)
_VpwrAlarmsPresent_Type = Gauge32
_VpwrAlarmsPresent_Object = MibScalar
vpwrAlarmsPresent = _VpwrAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 1),
    _VpwrAlarmsPresent_Type()
)
vpwrAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmsPresent.setStatus("current")
_VpwrAlarmTable_Object = MibTable
vpwrAlarmTable = _VpwrAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2)
)
if mibBuilder.loadTexts:
    vpwrAlarmTable.setStatus("current")
_VpwrAlarmEntry_Object = MibTableRow
vpwrAlarmEntry = _VpwrAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1)
)
vpwrAlarmEntry.setIndexNames(
    (0, "VPWR-DC-POWER-MIB", "vpwrShelfIndex"),
    (0, "VPWR-DC-POWER-MIB", "vpwrModuleIndex"),
    (0, "VPWR-DC-POWER-MIB", "vpwrAlarmIndex"),
)
if mibBuilder.loadTexts:
    vpwrAlarmEntry.setStatus("current")
_VpwrAlarmIndex_Type = PositiveInteger
_VpwrAlarmIndex_Object = MibTableColumn
vpwrAlarmIndex = _VpwrAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1, 1),
    _VpwrAlarmIndex_Type()
)
vpwrAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmIndex.setStatus("current")
_VpwrAlarmDescr_Type = AutonomousType
_VpwrAlarmDescr_Object = MibTableColumn
vpwrAlarmDescr = _VpwrAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1, 2),
    _VpwrAlarmDescr_Type()
)
vpwrAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmDescr.setStatus("current")
_VpwrAlarmTime_Type = TimeStamp
_VpwrAlarmTime_Object = MibTableColumn
vpwrAlarmTime = _VpwrAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 2, 1, 3),
    _VpwrAlarmTime_Type()
)
vpwrAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrAlarmTime.setStatus("current")
_SysAlarmConfigTable_Object = MibTable
sysAlarmConfigTable = _SysAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4)
)
if mibBuilder.loadTexts:
    sysAlarmConfigTable.setStatus("current")
_SysAlarmConfigEntry_Object = MibTableRow
sysAlarmConfigEntry = _SysAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4, 1)
)
sysAlarmConfigEntry.setIndexNames(
    (0, "VPWR-DC-POWER-MIB", "sysAlarmIndex"),
)
if mibBuilder.loadTexts:
    sysAlarmConfigEntry.setStatus("current")
_SysAlarmIndex_Type = Integer32
_SysAlarmIndex_Object = MibTableColumn
sysAlarmIndex = _SysAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4, 1, 1),
    _SysAlarmIndex_Type()
)
sysAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmIndex.setStatus("current")


class _SysAlarmDefaultName_Type(DisplayString):
    """Custom type sysAlarmDefaultName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAlarmDefaultName_Type.__name__ = "DisplayString"
_SysAlarmDefaultName_Object = MibTableColumn
sysAlarmDefaultName = _SysAlarmDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4, 1, 2),
    _SysAlarmDefaultName_Type()
)
sysAlarmDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmDefaultName.setStatus("current")


class _SysAlarmCustomName_Type(DisplayString):
    """Custom type sysAlarmCustomName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAlarmCustomName_Type.__name__ = "DisplayString"
_SysAlarmCustomName_Object = MibTableColumn
sysAlarmCustomName = _SysAlarmCustomName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4, 1, 3),
    _SysAlarmCustomName_Type()
)
sysAlarmCustomName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmCustomName.setStatus("current")


class _SysAlarmSeverity_Type(Integer32):
    """Custom type sysAlarmSeverity based on Integer32"""
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
        *(("major", 1),
          ("majorAndMinor", 3),
          ("minor", 2),
          ("none", 0))
    )


_SysAlarmSeverity_Type.__name__ = "Integer32"
_SysAlarmSeverity_Object = MibTableColumn
sysAlarmSeverity = _SysAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4, 1, 4),
    _SysAlarmSeverity_Type()
)
sysAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmSeverity.setStatus("current")


class _SysAlarmToRelayMapping_Type(DisplayString):
    """Custom type sysAlarmToRelayMapping based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAlarmToRelayMapping_Type.__name__ = "DisplayString"
_SysAlarmToRelayMapping_Object = MibTableColumn
sysAlarmToRelayMapping = _SysAlarmToRelayMapping_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4, 1, 5),
    _SysAlarmToRelayMapping_Type()
)
sysAlarmToRelayMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmToRelayMapping.setStatus("current")


class _SysAlarmOperStatus_Type(Integer32):
    """Custom type sysAlarmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_SysAlarmOperStatus_Type.__name__ = "Integer32"
_SysAlarmOperStatus_Object = MibTableColumn
sysAlarmOperStatus = _SysAlarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 4, 1, 6),
    _SysAlarmOperStatus_Type()
)
sysAlarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmOperStatus.setStatus("current")
_VpwrDcPowerSnmpConfig_ObjectIdentity = ObjectIdentity
vpwrDcPowerSnmpConfig = _VpwrDcPowerSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 9)
)
_VpwrTrapTable_Object = MibTable
vpwrTrapTable = _VpwrTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1)
)
if mibBuilder.loadTexts:
    vpwrTrapTable.setStatus("current")
_VpwrTrapTableEntry_Object = MibTableRow
vpwrTrapTableEntry = _VpwrTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1)
)
vpwrTrapTableEntry.setIndexNames(
    (0, "VPWR-DC-POWER-MIB", "vpwrTrapIpIndex"),
)
if mibBuilder.loadTexts:
    vpwrTrapTableEntry.setStatus("current")
_VpwrTrapIpIndex_Type = Integer32
_VpwrTrapIpIndex_Object = MibTableColumn
vpwrTrapIpIndex = _VpwrTrapIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1, 1),
    _VpwrTrapIpIndex_Type()
)
vpwrTrapIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrTrapIpIndex.setStatus("current")
_VpwrTrapIpAddress_Type = IpAddress
_VpwrTrapIpAddress_Object = MibTableColumn
vpwrTrapIpAddress = _VpwrTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1, 2),
    _VpwrTrapIpAddress_Type()
)
vpwrTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrTrapIpAddress.setStatus("current")
_VpwrTrapCriticality_Type = Integer32
_VpwrTrapCriticality_Object = MibTableColumn
vpwrTrapCriticality = _VpwrTrapCriticality_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1, 3),
    _VpwrTrapCriticality_Type()
)
vpwrTrapCriticality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrTrapCriticality.setStatus("current")


class _VpwrReadCommunityString_Type(DisplayString):
    """Custom type vpwrReadCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 8),
    )


_VpwrReadCommunityString_Type.__name__ = "DisplayString"
_VpwrReadCommunityString_Object = MibScalar
vpwrReadCommunityString = _VpwrReadCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 2),
    _VpwrReadCommunityString_Type()
)
vpwrReadCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrReadCommunityString.setStatus("current")


class _VpwrWriteCommunityString_Type(DisplayString):
    """Custom type vpwrWriteCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 8),
    )


_VpwrWriteCommunityString_Type.__name__ = "DisplayString"
_VpwrWriteCommunityString_Object = MibScalar
vpwrWriteCommunityString = _VpwrWriteCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 3),
    _VpwrWriteCommunityString_Type()
)
vpwrWriteCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrWriteCommunityString.setStatus("current")


class _VpwrTrapCommunityString_Type(DisplayString):
    """Custom type vpwrTrapCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 8),
    )


_VpwrTrapCommunityString_Type.__name__ = "DisplayString"
_VpwrTrapCommunityString_Object = MibScalar
vpwrTrapCommunityString = _VpwrTrapCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 4),
    _VpwrTrapCommunityString_Type()
)
vpwrTrapCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrTrapCommunityString.setStatus("current")
_VpwrDcPowerTraps_ObjectIdentity = ObjectIdentity
vpwrDcPowerTraps = _VpwrDcPowerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 10)
)
_VpwrDcPowerTrapsMsgString_ObjectIdentity = ObjectIdentity
vpwrDcPowerTrapsMsgString = _VpwrDcPowerTrapsMsgString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 11)
)


class _VpwrTrapsMsgString_Type(DisplayString):
    """Custom type vpwrTrapsMsgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VpwrTrapsMsgString_Type.__name__ = "DisplayString"
_VpwrTrapsMsgString_Object = MibScalar
vpwrTrapsMsgString = _VpwrTrapsMsgString_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 1),
    _VpwrTrapsMsgString_Type()
)
vpwrTrapsMsgString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpwrTrapsMsgString.setStatus("current")

# Managed Objects groups


# Notification objects

vpwrTrapPowerMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 1)
)
vpwrTrapPowerMajorAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPowerMajorAlarm.setStatus(
        ""
    )

vpwrTrapPowerMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 2)
)
vpwrTrapPowerMinorAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPowerMinorAlarm.setStatus(
        ""
    )

vpwrTrapACFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 3)
)
vpwrTrapACFAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapACFAlarm.setStatus(
        ""
    )

vpwrTrapHVAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 4)
)
vpwrTrapHVAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapHVAlarm.setStatus(
        ""
    )

vpwrTrapHVSDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 5)
)
vpwrTrapHVSDAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapHVSDAlarm.setStatus(
        ""
    )

vpwrTrapBDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 6)
)
vpwrTrapBDAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBDAlarm.setStatus(
        ""
    )

vpwrTrapLVDWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 7)
)
vpwrTrapLVDWarningAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLVDWarningAlarm.setStatus(
        ""
    )

vpwrTrapLVDOpenAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 8)
)
vpwrTrapLVDOpenAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLVDOpenAlarm.setStatus(
        ""
    )

vpwrTrapDistAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 9)
)
vpwrTrapDistAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDistAlarm.setStatus(
        ""
    )

vpwrTrapAuxAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 10)
)
vpwrTrapAuxAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapAuxAlarm.setStatus(
        ""
    )

vpwrTrapSystemRedundancyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 11)
)
vpwrTrapSystemRedundancyAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemRedundancyAlarm.setStatus(
        ""
    )

vpwrTrapIShareAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 12)
)
vpwrTrapIShareAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapIShareAlarm.setStatus(
        ""
    )

vpwrTrapModuleFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 13)
)
vpwrTrapModuleFailAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleFailAlarm.setStatus(
        ""
    )

vpwrTrapMultipleModuleFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 14)
)
vpwrTrapMultipleModuleFailAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultipleModuleFailAlarm.setStatus(
        ""
    )

vpwrTrapModuleCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 15)
)
vpwrTrapModuleCommAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleCommAlarm.setStatus(
        ""
    )

vpwrTrapSystemOverTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 16)
)
vpwrTrapSystemOverTemperatureAlarm.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemOverTemperatureAlarm.setStatus(
        ""
    )

vpwrTrapSystemOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 17)
)
vpwrTrapSystemOK.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemOK.setStatus(
        ""
    )

vpwrTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 18)
)
vpwrTrapModuleInserted.setObjects(
      *(("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("VPWR-DC-POWER-MIB", "vpwrShelfIndex"),
        ("VPWR-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapModuleInserted.setStatus(
        ""
    )

vpwrTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 19)
)
vpwrTrapModuleRemoved.setObjects(
      *(("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("VPWR-DC-POWER-MIB", "vpwrShelfIndex"),
        ("VPWR-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapModuleRemoved.setStatus(
        ""
    )

vpwrTrapThermalCompActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 20)
)
vpwrTrapThermalCompActive.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalCompActive.setStatus(
        ""
    )

vpwrTrapThermalCompInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 21)
)
vpwrTrapThermalCompInactive.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalCompInactive.setStatus(
        ""
    )

vpwrTrapInternalTempAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 22)
)
vpwrTrapInternalTempAlarmSet.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapInternalTempAlarmSet.setStatus(
        ""
    )

vpwrTrapInternalTempAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 23)
)
vpwrTrapInternalTempAlarmCleared.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapInternalTempAlarmCleared.setStatus(
        ""
    )

vpwrTrapBatteryTempAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 24)
)
vpwrTrapBatteryTempAlarmSet.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryTempAlarmSet.setStatus(
        ""
    )

vpwrTrapBatteryTempAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 25)
)
vpwrTrapBatteryTempAlarmCleared.setObjects(
    ("VPWR-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryTempAlarmCleared.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPWR-DC-POWER-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "valereDcPowerMgt": valereDcPowerMgt,
       "vpwrDcPowerProducts": vpwrDcPowerProducts,
       "vpwrDcPowerSystem": vpwrDcPowerSystem,
       "vpwrSystemIdentGroup": vpwrSystemIdentGroup,
       "vpwrIdentManufacturer": vpwrIdentManufacturer,
       "vpwrIdentModel": vpwrIdentModel,
       "vpwrIdentControllerVersion": vpwrIdentControllerVersion,
       "vpwrIdentAgentSoftwareVersion": vpwrIdentAgentSoftwareVersion,
       "vpwrIdentName": vpwrIdentName,
       "vpwrSystemIdentTable": vpwrSystemIdentTable,
       "vpwrSystemIdentEntry": vpwrSystemIdentEntry,
       "vpwrShelfIndex": vpwrShelfIndex,
       "vpwrModuleIndex": vpwrModuleIndex,
       "vpwrModuleOID": vpwrModuleOID,
       "vpwrModuleParameter": vpwrModuleParameter,
       "vpwrModuleOperStatus": vpwrModuleOperStatus,
       "vpwrModuleCapacity": vpwrModuleCapacity,
       "vpwrSystemConfigGroup": vpwrSystemConfigGroup,
       "vpwrSystemTempCompensation": vpwrSystemTempCompensation,
       "vpwrSystemTempCompStartTemperature": vpwrSystemTempCompStartTemperature,
       "vpwrSystemTempCompStopVoltage": vpwrSystemTempCompStopVoltage,
       "vpwrSystemTempCompensationSlope": vpwrSystemTempCompensationSlope,
       "vpwrSystemThermalSenseType": vpwrSystemThermalSenseType,
       "vpwrSystemHVAlarmSetpoint": vpwrSystemHVAlarmSetpoint,
       "vpwrSystemBDAlarmSetpoint": vpwrSystemBDAlarmSetpoint,
       "vpwrSystemInternalTempLThreshold": vpwrSystemInternalTempLThreshold,
       "vpwrSystemInternalTempUThreshold": vpwrSystemInternalTempUThreshold,
       "vpwrSystemParameterGroup": vpwrSystemParameterGroup,
       "vpwrSystemShelfCapacity": vpwrSystemShelfCapacity,
       "vpwrSystemVoltage": vpwrSystemVoltage,
       "vpwrSystemCurrent": vpwrSystemCurrent,
       "vpwrSystemControllerState": vpwrSystemControllerState,
       "vpwrSystemInternalTemperature": vpwrSystemInternalTemperature,
       "vpwrSystemTempCompensationState": vpwrSystemTempCompensationState,
       "vpwrSystemType": vpwrSystemType,
       "vpwrDcPowerRectifier": vpwrDcPowerRectifier,
       "vpwrRectifierConfigGroup": vpwrRectifierConfigGroup,
       "vpwrRectifierFVSetpoint": vpwrRectifierFVSetpoint,
       "vpwrRectifierHVSDSetpoint": vpwrRectifierHVSDSetpoint,
       "vpwrRectifierAlarmGroup": vpwrRectifierAlarmGroup,
       "vpwrRectAlarmDCFail": vpwrRectAlarmDCFail,
       "vpwrRectAlarmBoostFail": vpwrRectAlarmBoostFail,
       "vpwrRectAlarmACFail": vpwrRectAlarmACFail,
       "vpwrRectAlarmHVSD": vpwrRectAlarmHVSD,
       "vpwrRectAlarmFanFail": vpwrRectAlarmFanFail,
       "vpwrRectAlarmAmbTemp": vpwrRectAlarmAmbTemp,
       "vpwrRectAlarmIntTemp": vpwrRectAlarmIntTemp,
       "vpwrRectAlarmIShare": vpwrRectAlarmIShare,
       "vpwrRectAlarmUV": vpwrRectAlarmUV,
       "vpwrRectAlarmLowVoltage": vpwrRectAlarmLowVoltage,
       "vpwrRectAlarmReserved": vpwrRectAlarmReserved,
       "vpwrRectAlarmDCEnable": vpwrRectAlarmDCEnable,
       "vpwrRectAlarmRemoteShutdown": vpwrRectAlarmRemoteShutdown,
       "vpwrRectAlarmModDisableShutdown": vpwrRectAlarmModDisableShutdown,
       "vpwrRectAlarmShortPinShutdown": vpwrRectAlarmShortPinShutdown,
       "vpwrRectAlarmBoostComm": vpwrRectAlarmBoostComm,
       "vpwrRectifierTestGroup": vpwrRectifierTestGroup,
       "vpwrDcPowerLvd": vpwrDcPowerLvd,
       "vpwrLvdConfigGroup": vpwrLvdConfigGroup,
       "vpwrLvdWarningSetpoint": vpwrLvdWarningSetpoint,
       "vpwrLvdDisconnectSetpoint": vpwrLvdDisconnectSetpoint,
       "vpwrLvdReconnectSetpoint": vpwrLvdReconnectSetpoint,
       "vpwrLvdReconnectDelayTimer": vpwrLvdReconnectDelayTimer,
       "vpwrLvdAlarmGroup": vpwrLvdAlarmGroup,
       "vpwrLvdAlarmContactorOpen": vpwrLvdAlarmContactorOpen,
       "vpwrLvdAlarmCBOpen": vpwrLvdAlarmCBOpen,
       "vpwrTrapLvdFuseOpen": vpwrTrapLvdFuseOpen,
       "vpwrLvdAlarmWarning": vpwrLvdAlarmWarning,
       "vpwrLvdTestGroup": vpwrLvdTestGroup,
       "vpwrDcPowerTest": vpwrDcPowerTest,
       "vpwrDcPowerModuleIdent": vpwrDcPowerModuleIdent,
       "vpwrDcPowerBatteryGroup": vpwrDcPowerBatteryGroup,
       "vpwrBatteryTempGroup": vpwrBatteryTempGroup,
       "vpwrBatteryTempTable": vpwrBatteryTempTable,
       "vpwrBatteryTempTableEntry": vpwrBatteryTempTableEntry,
       "vpwrBatteryTempIndex": vpwrBatteryTempIndex,
       "vpwrBatteryTempName": vpwrBatteryTempName,
       "vpwrBatteryTemp": vpwrBatteryTemp,
       "vpwrBatteryTempLThreshold": vpwrBatteryTempLThreshold,
       "vpwrBatteryTempUThreshold": vpwrBatteryTempUThreshold,
       "vpwrDcPowerAlarmGroup": vpwrDcPowerAlarmGroup,
       "vpwrAlarmsPresent": vpwrAlarmsPresent,
       "vpwrAlarmTable": vpwrAlarmTable,
       "vpwrAlarmEntry": vpwrAlarmEntry,
       "vpwrAlarmIndex": vpwrAlarmIndex,
       "vpwrAlarmDescr": vpwrAlarmDescr,
       "vpwrAlarmTime": vpwrAlarmTime,
       "sysAlarmConfigTable": sysAlarmConfigTable,
       "sysAlarmConfigEntry": sysAlarmConfigEntry,
       "sysAlarmIndex": sysAlarmIndex,
       "sysAlarmDefaultName": sysAlarmDefaultName,
       "sysAlarmCustomName": sysAlarmCustomName,
       "sysAlarmSeverity": sysAlarmSeverity,
       "sysAlarmToRelayMapping": sysAlarmToRelayMapping,
       "sysAlarmOperStatus": sysAlarmOperStatus,
       "vpwrDcPowerSnmpConfig": vpwrDcPowerSnmpConfig,
       "vpwrTrapTable": vpwrTrapTable,
       "vpwrTrapTableEntry": vpwrTrapTableEntry,
       "vpwrTrapIpIndex": vpwrTrapIpIndex,
       "vpwrTrapIpAddress": vpwrTrapIpAddress,
       "vpwrTrapCriticality": vpwrTrapCriticality,
       "vpwrReadCommunityString": vpwrReadCommunityString,
       "vpwrWriteCommunityString": vpwrWriteCommunityString,
       "vpwrTrapCommunityString": vpwrTrapCommunityString,
       "vpwrDcPowerTraps": vpwrDcPowerTraps,
       "vpwrTrapPowerMajorAlarm": vpwrTrapPowerMajorAlarm,
       "vpwrTrapPowerMinorAlarm": vpwrTrapPowerMinorAlarm,
       "vpwrTrapACFAlarm": vpwrTrapACFAlarm,
       "vpwrTrapHVAlarm": vpwrTrapHVAlarm,
       "vpwrTrapHVSDAlarm": vpwrTrapHVSDAlarm,
       "vpwrTrapBDAlarm": vpwrTrapBDAlarm,
       "vpwrTrapLVDWarningAlarm": vpwrTrapLVDWarningAlarm,
       "vpwrTrapLVDOpenAlarm": vpwrTrapLVDOpenAlarm,
       "vpwrTrapDistAlarm": vpwrTrapDistAlarm,
       "vpwrTrapAuxAlarm": vpwrTrapAuxAlarm,
       "vpwrTrapSystemRedundancyAlarm": vpwrTrapSystemRedundancyAlarm,
       "vpwrTrapIShareAlarm": vpwrTrapIShareAlarm,
       "vpwrTrapModuleFailAlarm": vpwrTrapModuleFailAlarm,
       "vpwrTrapMultipleModuleFailAlarm": vpwrTrapMultipleModuleFailAlarm,
       "vpwrTrapModuleCommAlarm": vpwrTrapModuleCommAlarm,
       "vpwrTrapSystemOverTemperatureAlarm": vpwrTrapSystemOverTemperatureAlarm,
       "vpwrTrapSystemOK": vpwrTrapSystemOK,
       "vpwrTrapModuleInserted": vpwrTrapModuleInserted,
       "vpwrTrapModuleRemoved": vpwrTrapModuleRemoved,
       "vpwrTrapThermalCompActive": vpwrTrapThermalCompActive,
       "vpwrTrapThermalCompInactive": vpwrTrapThermalCompInactive,
       "vpwrTrapInternalTempAlarmSet": vpwrTrapInternalTempAlarmSet,
       "vpwrTrapInternalTempAlarmCleared": vpwrTrapInternalTempAlarmCleared,
       "vpwrTrapBatteryTempAlarmSet": vpwrTrapBatteryTempAlarmSet,
       "vpwrTrapBatteryTempAlarmCleared": vpwrTrapBatteryTempAlarmCleared,
       "vpwrDcPowerTrapsMsgString": vpwrDcPowerTrapsMsgString,
       "vpwrTrapsMsgString": vpwrTrapsMsgString}
)
