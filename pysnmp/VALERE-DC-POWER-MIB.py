# SNMP MIB module (VALERE-DC-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VALERE-DC-POWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:00 2024
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

vpwrDcPowerMgt = ModuleIdentity(
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
    (0, "VALERE-DC-POWER-MIB", "vpwrBayIndex"),
    (0, "VALERE-DC-POWER-MIB", "vpwrModuleIndex"),
)
if mibBuilder.loadTexts:
    vpwrSystemIdentEntry.setStatus("current")
_VpwrBayIndex_Type = PositiveInteger
_VpwrBayIndex_Object = MibTableColumn
vpwrBayIndex = _VpwrBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 1),
    _VpwrBayIndex_Type()
)
vpwrBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayIndex.setStatus("current")
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
_VpwrModuleCurrent_Type = Integer32
_VpwrModuleCurrent_Object = MibTableColumn
vpwrModuleCurrent = _VpwrModuleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 1, 6, 1, 4),
    _VpwrModuleCurrent_Type()
)
vpwrModuleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleCurrent.setStatus("current")


class _VpwrModuleOperStatus_Type(Integer32):
    """Custom type vpwrModuleOperStatus based on Integer32"""
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
        *(("moduleStatusAlarm", 1),
          ("moduleStatusDisabled", 2),
          ("moduleStatusOK", 0),
          ("moduleStatusRingerAOn", 3),
          ("moduleStatusRingerBOn", 4),
          ("moduleStatusUnknown", 5))
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
    vpwrSystemTempCompStopVoltage.setUnits(" *.01 Volts")


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
    vpwrSystemHVAlarmSetpoint.setUnits(" *.01 Volts")
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
    vpwrSystemBDAlarmSetpoint.setUnits(" *.01 Volts")
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
    vpwrSystemVoltage.setUnits(" *.01 Volts")
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
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sysType12V", 3),
          ("sysType24V", 2),
          ("sysType48V", 1),
          ("sysTypeUnknow", 0))
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
_VpwrSystemPanelIdentGroup_ObjectIdentity = ObjectIdentity
vpwrSystemPanelIdentGroup = _VpwrSystemPanelIdentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4)
)
_VpwrPanelIdentTable_Object = MibTable
vpwrPanelIdentTable = _VpwrPanelIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vpwrPanelIdentTable.setStatus("current")
_VpwrPanelIdentEntry_Object = MibTableRow
vpwrPanelIdentEntry = _VpwrPanelIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1)
)
vpwrPanelIdentEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "vpwrPanelBayIndex"),
    (0, "VALERE-DC-POWER-MIB", "vpwrPanelModuleIndex"),
)
if mibBuilder.loadTexts:
    vpwrPanelIdentEntry.setStatus("current")
_VpwrPanelBayIndex_Type = PositiveInteger
_VpwrPanelBayIndex_Object = MibTableColumn
vpwrPanelBayIndex = _VpwrPanelBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 1),
    _VpwrPanelBayIndex_Type()
)
vpwrPanelBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelBayIndex.setStatus("current")
_VpwrPanelModuleIndex_Type = PositiveInteger
_VpwrPanelModuleIndex_Object = MibTableColumn
vpwrPanelModuleIndex = _VpwrPanelModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 2),
    _VpwrPanelModuleIndex_Type()
)
vpwrPanelModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleIndex.setStatus("current")
_VpwrPanelModuleOID_Type = ObjectIdentifier
_VpwrPanelModuleOID_Object = MibTableColumn
vpwrPanelModuleOID = _VpwrPanelModuleOID_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 3),
    _VpwrPanelModuleOID_Type()
)
vpwrPanelModuleOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleOID.setStatus("current")
_VpwrPanelModuleCurrent_Type = Integer32
_VpwrPanelModuleCurrent_Object = MibTableColumn
vpwrPanelModuleCurrent = _VpwrPanelModuleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 4),
    _VpwrPanelModuleCurrent_Type()
)
vpwrPanelModuleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleCurrent.setStatus("current")


class _VpwrPanelModuleOperStatus_Type(Integer32):
    """Custom type vpwrPanelModuleOperStatus based on Integer32"""
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


_VpwrPanelModuleOperStatus_Type.__name__ = "Integer32"
_VpwrPanelModuleOperStatus_Object = MibTableColumn
vpwrPanelModuleOperStatus = _VpwrPanelModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 5),
    _VpwrPanelModuleOperStatus_Type()
)
vpwrPanelModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleOperStatus.setStatus("current")
_VpwrPanelModuleCapacity_Type = Integer32
_VpwrPanelModuleCapacity_Object = MibTableColumn
vpwrPanelModuleCapacity = _VpwrPanelModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 4, 1, 1, 6),
    _VpwrPanelModuleCapacity_Type()
)
vpwrPanelModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleCapacity.setStatus("current")
_VpwrSystemBayctrlIdentGroup_ObjectIdentity = ObjectIdentity
vpwrSystemBayctrlIdentGroup = _VpwrSystemBayctrlIdentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5)
)
_VpwrBayctrlIdentTable_Object = MibTable
vpwrBayctrlIdentTable = _VpwrBayctrlIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vpwrBayctrlIdentTable.setStatus("current")
_VpwrBayctrlIdentEntry_Object = MibTableRow
vpwrBayctrlIdentEntry = _VpwrBayctrlIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1)
)
vpwrBayctrlIdentEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "vpwrBayctrlIndex"),
)
if mibBuilder.loadTexts:
    vpwrBayctrlIdentEntry.setStatus("current")
_VpwrBayctrlIndex_Type = PositiveInteger
_VpwrBayctrlIndex_Object = MibTableColumn
vpwrBayctrlIndex = _VpwrBayctrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1, 1),
    _VpwrBayctrlIndex_Type()
)
vpwrBayctrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlIndex.setStatus("current")
_VpwrBayctrlOID_Type = ObjectIdentifier
_VpwrBayctrlOID_Object = MibTableColumn
vpwrBayctrlOID = _VpwrBayctrlOID_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1, 2),
    _VpwrBayctrlOID_Type()
)
vpwrBayctrlOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlOID.setStatus("current")
_VpwrBayctrlCurrent_Type = Integer32
_VpwrBayctrlCurrent_Object = MibTableColumn
vpwrBayctrlCurrent = _VpwrBayctrlCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1, 3),
    _VpwrBayctrlCurrent_Type()
)
vpwrBayctrlCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlCurrent.setStatus("current")


class _VpwrBayctrlOperStatus_Type(Integer32):
    """Custom type vpwrBayctrlOperStatus based on Integer32"""
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


_VpwrBayctrlOperStatus_Type.__name__ = "Integer32"
_VpwrBayctrlOperStatus_Object = MibTableColumn
vpwrBayctrlOperStatus = _VpwrBayctrlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1, 4),
    _VpwrBayctrlOperStatus_Type()
)
vpwrBayctrlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlOperStatus.setStatus("current")
_VpwrBayctrlCapacity_Type = Integer32
_VpwrBayctrlCapacity_Object = MibTableColumn
vpwrBayctrlCapacity = _VpwrBayctrlCapacity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 2, 5, 1, 1, 5),
    _VpwrBayctrlCapacity_Type()
)
vpwrBayctrlCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlCapacity.setStatus("current")
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
    vpwrRectifierFVSetpoint.setUnits(" *.01 Volts")
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
    vpwrRectifierHVSDSetpoint.setUnits(" *.01 Volts")


class _VpwrRectifierCurrentLimitAdminState_Type(Integer32):
    """Custom type vpwrRectifierCurrentLimitAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rectCurrentLimitDisabled", 0),
          ("rectCurrentLimitEnabled", 1))
    )


_VpwrRectifierCurrentLimitAdminState_Type.__name__ = "Integer32"
_VpwrRectifierCurrentLimitAdminState_Object = MibScalar
vpwrRectifierCurrentLimitAdminState = _VpwrRectifierCurrentLimitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 3),
    _VpwrRectifierCurrentLimitAdminState_Type()
)
vpwrRectifierCurrentLimitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierCurrentLimitAdminState.setStatus("current")


class _VpwrRectifierCurrentLimit_Type(Integer32):
    """Custom type vpwrRectifierCurrentLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_VpwrRectifierCurrentLimit_Type.__name__ = "Integer32"
_VpwrRectifierCurrentLimit_Object = MibScalar
vpwrRectifierCurrentLimit = _VpwrRectifierCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 13858, 3, 1, 4),
    _VpwrRectifierCurrentLimit_Type()
)
vpwrRectifierCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRectifierCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRectifierCurrentLimit.setUnits("Amperes")
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
    vpwrLvdWarningSetpoint.setUnits(" * .01 Volts")
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
    vpwrLvdDisconnectSetpoint.setUnits(" *.01 Volts")
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
    vpwrLvdReconnectSetpoint.setUnits(" *.01 Volts")


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
_VpwrLvdContactorConfigTable_Object = MibTable
vpwrLvdContactorConfigTable = _VpwrLvdContactorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5)
)
if mibBuilder.loadTexts:
    vpwrLvdContactorConfigTable.setStatus("current")
_VpwrLvdContactorConfigEntry_Object = MibTableRow
vpwrLvdContactorConfigEntry = _VpwrLvdContactorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5, 1)
)
vpwrLvdContactorConfigEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "vpwrBayIndex"),
    (0, "VALERE-DC-POWER-MIB", "vpwrModuleIndex"),
    (0, "VALERE-DC-POWER-MIB", "vpwrLvdContactorIndex"),
)
if mibBuilder.loadTexts:
    vpwrLvdContactorConfigEntry.setStatus("current")
_VpwrLvdContactorIndex_Type = PositiveInteger
_VpwrLvdContactorIndex_Object = MibTableColumn
vpwrLvdContactorIndex = _VpwrLvdContactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5, 1, 1),
    _VpwrLvdContactorIndex_Type()
)
vpwrLvdContactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrLvdContactorIndex.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdContactorIndex.setUnits(" None")
_VpwrLvdContactorWarningSetpoint_Type = PositiveInteger
_VpwrLvdContactorWarningSetpoint_Object = MibTableColumn
vpwrLvdContactorWarningSetpoint = _VpwrLvdContactorWarningSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5, 1, 2),
    _VpwrLvdContactorWarningSetpoint_Type()
)
vpwrLvdContactorWarningSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdContactorWarningSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdContactorWarningSetpoint.setUnits(" * .01 Volts")
_VpwrLvdContactorDisconnectSetpoint_Type = PositiveInteger
_VpwrLvdContactorDisconnectSetpoint_Object = MibTableColumn
vpwrLvdContactorDisconnectSetpoint = _VpwrLvdContactorDisconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5, 1, 3),
    _VpwrLvdContactorDisconnectSetpoint_Type()
)
vpwrLvdContactorDisconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdContactorDisconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdContactorDisconnectSetpoint.setUnits(" *.01 Volts")
_VpwrLvdContactorReconnectSetpoint_Type = PositiveInteger
_VpwrLvdContactorReconnectSetpoint_Object = MibTableColumn
vpwrLvdContactorReconnectSetpoint = _VpwrLvdContactorReconnectSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5, 1, 4),
    _VpwrLvdContactorReconnectSetpoint_Type()
)
vpwrLvdContactorReconnectSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdContactorReconnectSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdContactorReconnectSetpoint.setUnits(" *.01 Volts")


class _VpwrLvdContactorReconnectDelayTimer_Type(PositiveInteger):
    """Custom type vpwrLvdContactorReconnectDelayTimer based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_VpwrLvdContactorReconnectDelayTimer_Type.__name__ = "PositiveInteger"
_VpwrLvdContactorReconnectDelayTimer_Object = MibTableColumn
vpwrLvdContactorReconnectDelayTimer = _VpwrLvdContactorReconnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5, 1, 5),
    _VpwrLvdContactorReconnectDelayTimer_Type()
)
vpwrLvdContactorReconnectDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdContactorReconnectDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    vpwrLvdContactorReconnectDelayTimer.setUnits(" Seconds")


class _VpwrLvdContactorState_Type(Integer32):
    """Custom type vpwrLvdContactorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("contactorClose", 1),
          ("contactorOpen", 0))
    )


_VpwrLvdContactorState_Type.__name__ = "Integer32"
_VpwrLvdContactorState_Object = MibTableColumn
vpwrLvdContactorState = _VpwrLvdContactorState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 4, 1, 5, 1, 6),
    _VpwrLvdContactorState_Type()
)
vpwrLvdContactorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrLvdContactorState.setStatus("current")
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
_VpwrModuleIdentTable_Object = MibTable
vpwrModuleIdentTable = _VpwrModuleIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1)
)
if mibBuilder.loadTexts:
    vpwrModuleIdentTable.setStatus("current")
_VpwrModuleIdentEntry_Object = MibTableRow
vpwrModuleIdentEntry = _VpwrModuleIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1)
)
if mibBuilder.loadTexts:
    vpwrModuleIdentEntry.setStatus("current")
_VpwrModuleSerialNumber_Type = DisplayString
_VpwrModuleSerialNumber_Object = MibTableColumn
vpwrModuleSerialNumber = _VpwrModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 1),
    _VpwrModuleSerialNumber_Type()
)
vpwrModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleSerialNumber.setStatus("current")
_VpwrModuleModelNumber_Type = DisplayString
_VpwrModuleModelNumber_Object = MibTableColumn
vpwrModuleModelNumber = _VpwrModuleModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 2),
    _VpwrModuleModelNumber_Type()
)
vpwrModuleModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleModelNumber.setStatus("current")
_VpwrModuleFwVersion_Type = DisplayString
_VpwrModuleFwVersion_Object = MibTableColumn
vpwrModuleFwVersion = _VpwrModuleFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 3),
    _VpwrModuleFwVersion_Type()
)
vpwrModuleFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleFwVersion.setStatus("current")
_VpwrModuleTestDate_Type = DisplayString
_VpwrModuleTestDate_Object = MibTableColumn
vpwrModuleTestDate = _VpwrModuleTestDate_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 4),
    _VpwrModuleTestDate_Type()
)
vpwrModuleTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleTestDate.setStatus("current")
_VpwrModuleOperHours_Type = Counter32
_VpwrModuleOperHours_Object = MibTableColumn
vpwrModuleOperHours = _VpwrModuleOperHours_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 1, 1, 5),
    _VpwrModuleOperHours_Type()
)
vpwrModuleOperHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrModuleOperHours.setStatus("current")
_VpwrPanelModuleIdentTable_Object = MibTable
vpwrPanelModuleIdentTable = _VpwrPanelModuleIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 2)
)
if mibBuilder.loadTexts:
    vpwrPanelModuleIdentTable.setStatus("current")
_VpwrPanelModuleIdentEntry_Object = MibTableRow
vpwrPanelModuleIdentEntry = _VpwrPanelModuleIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vpwrPanelModuleIdentEntry.setStatus("current")
_VpwrPanelModuleSerialNumber_Type = DisplayString
_VpwrPanelModuleSerialNumber_Object = MibTableColumn
vpwrPanelModuleSerialNumber = _VpwrPanelModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 2, 1, 1),
    _VpwrPanelModuleSerialNumber_Type()
)
vpwrPanelModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleSerialNumber.setStatus("current")
_VpwrPanelModuleModelNumber_Type = DisplayString
_VpwrPanelModuleModelNumber_Object = MibTableColumn
vpwrPanelModuleModelNumber = _VpwrPanelModuleModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 2, 1, 2),
    _VpwrPanelModuleModelNumber_Type()
)
vpwrPanelModuleModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleModelNumber.setStatus("current")
_VpwrPanelModuleFwVersion_Type = DisplayString
_VpwrPanelModuleFwVersion_Object = MibTableColumn
vpwrPanelModuleFwVersion = _VpwrPanelModuleFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 2, 1, 3),
    _VpwrPanelModuleFwVersion_Type()
)
vpwrPanelModuleFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleFwVersion.setStatus("current")
_VpwrPanelModuleTestDate_Type = DisplayString
_VpwrPanelModuleTestDate_Object = MibTableColumn
vpwrPanelModuleTestDate = _VpwrPanelModuleTestDate_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 2, 1, 4),
    _VpwrPanelModuleTestDate_Type()
)
vpwrPanelModuleTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleTestDate.setStatus("current")
_VpwrPanelModuleOperHours_Type = Counter32
_VpwrPanelModuleOperHours_Object = MibTableColumn
vpwrPanelModuleOperHours = _VpwrPanelModuleOperHours_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 2, 1, 5),
    _VpwrPanelModuleOperHours_Type()
)
vpwrPanelModuleOperHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrPanelModuleOperHours.setStatus("current")
_VpwrBayctrlModuleIdentTable_Object = MibTable
vpwrBayctrlModuleIdentTable = _VpwrBayctrlModuleIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 3)
)
if mibBuilder.loadTexts:
    vpwrBayctrlModuleIdentTable.setStatus("current")
_VpwrBayctrlModuleIdentEntry_Object = MibTableRow
vpwrBayctrlModuleIdentEntry = _VpwrBayctrlModuleIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 3, 1)
)
if mibBuilder.loadTexts:
    vpwrBayctrlModuleIdentEntry.setStatus("current")
_VpwrBayctrlSerialNumber_Type = DisplayString
_VpwrBayctrlSerialNumber_Object = MibTableColumn
vpwrBayctrlSerialNumber = _VpwrBayctrlSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 3, 1, 1),
    _VpwrBayctrlSerialNumber_Type()
)
vpwrBayctrlSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlSerialNumber.setStatus("current")
_VpwrBayctrlModelNumber_Type = DisplayString
_VpwrBayctrlModelNumber_Object = MibTableColumn
vpwrBayctrlModelNumber = _VpwrBayctrlModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 3, 1, 2),
    _VpwrBayctrlModelNumber_Type()
)
vpwrBayctrlModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlModelNumber.setStatus("current")
_VpwrBayctrlFwVersion_Type = DisplayString
_VpwrBayctrlFwVersion_Object = MibTableColumn
vpwrBayctrlFwVersion = _VpwrBayctrlFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 3, 1, 3),
    _VpwrBayctrlFwVersion_Type()
)
vpwrBayctrlFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlFwVersion.setStatus("current")
_VpwrBayctrlTestDate_Type = DisplayString
_VpwrBayctrlTestDate_Object = MibTableColumn
vpwrBayctrlTestDate = _VpwrBayctrlTestDate_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 3, 1, 4),
    _VpwrBayctrlTestDate_Type()
)
vpwrBayctrlTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlTestDate.setStatus("current")
_VpwrBayctrlOperHours_Type = Counter32
_VpwrBayctrlOperHours_Object = MibTableColumn
vpwrBayctrlOperHours = _VpwrBayctrlOperHours_Object(
    (1, 3, 6, 1, 4, 1, 13858, 6, 3, 1, 5),
    _VpwrBayctrlOperHours_Type()
)
vpwrBayctrlOperHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBayctrlOperHours.setStatus("current")
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
_VpwrBatteryTempEntry_Object = MibTableRow
vpwrBatteryTempEntry = _VpwrBatteryTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 1, 1)
)
vpwrBatteryTempEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "vpwrBatteryTempIndex"),
)
if mibBuilder.loadTexts:
    vpwrBatteryTempEntry.setStatus("current")
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


class _BatteryTempCompensation_Type(Integer32):
    """Custom type batteryTempCompensation based on Integer32"""
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


_BatteryTempCompensation_Type.__name__ = "Integer32"
_BatteryTempCompensation_Object = MibScalar
batteryTempCompensation = _BatteryTempCompensation_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 4),
    _BatteryTempCompensation_Type()
)
batteryTempCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompensation.setStatus("current")


class _BatteryTempCompHighStartTemperature_Type(Integer32):
    """Custom type batteryTempCompHighStartTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 60),
    )


_BatteryTempCompHighStartTemperature_Type.__name__ = "Integer32"
_BatteryTempCompHighStartTemperature_Object = MibScalar
batteryTempCompHighStartTemperature = _BatteryTempCompHighStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 5),
    _BatteryTempCompHighStartTemperature_Type()
)
batteryTempCompHighStartTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompHighStartTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompHighStartTemperature.setUnits("degrees Centigrade")
_BatteryTempCompHighStopVoltage_Type = Integer32
_BatteryTempCompHighStopVoltage_Object = MibScalar
batteryTempCompHighStopVoltage = _BatteryTempCompHighStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 6),
    _BatteryTempCompHighStopVoltage_Type()
)
batteryTempCompHighStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompHighStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompHighStopVoltage.setUnits(" *.01 Volts")


class _BatteryTempCompHighSlope_Type(Integer32):
    """Custom type batteryTempCompHighSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BatteryTempCompHighSlope_Type.__name__ = "Integer32"
_BatteryTempCompHighSlope_Object = MibScalar
batteryTempCompHighSlope = _BatteryTempCompHighSlope_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 7),
    _BatteryTempCompHighSlope_Type()
)
batteryTempCompHighSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompHighSlope.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompHighSlope.setUnits(" milli-Volts per degrees Centigrade")
_BatteryTempCompLowStartTemperature_Type = Integer32
_BatteryTempCompLowStartTemperature_Object = MibScalar
batteryTempCompLowStartTemperature = _BatteryTempCompLowStartTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 8),
    _BatteryTempCompLowStartTemperature_Type()
)
batteryTempCompLowStartTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompLowStartTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompLowStartTemperature.setUnits("degrees Centigrade")
_BatteryTempCompLowStopVoltage_Type = Integer32
_BatteryTempCompLowStopVoltage_Object = MibScalar
batteryTempCompLowStopVoltage = _BatteryTempCompLowStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 9),
    _BatteryTempCompLowStopVoltage_Type()
)
batteryTempCompLowStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompLowStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompLowStopVoltage.setUnits(" *.01 Volts")


class _BatteryTempCompLowSlope_Type(Integer32):
    """Custom type batteryTempCompLowSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BatteryTempCompLowSlope_Type.__name__ = "Integer32"
_BatteryTempCompLowSlope_Object = MibScalar
batteryTempCompLowSlope = _BatteryTempCompLowSlope_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 10),
    _BatteryTempCompLowSlope_Type()
)
batteryTempCompLowSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompLowSlope.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompLowSlope.setUnits(" milli-Volts per degrees Centigrade")


class _BatteryTempCompRunawayTemperature_Type(Integer32):
    """Custom type batteryTempCompRunawayTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 60),
    )


_BatteryTempCompRunawayTemperature_Type.__name__ = "Integer32"
_BatteryTempCompRunawayTemperature_Object = MibScalar
batteryTempCompRunawayTemperature = _BatteryTempCompRunawayTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 11),
    _BatteryTempCompRunawayTemperature_Type()
)
batteryTempCompRunawayTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompRunawayTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompRunawayTemperature.setUnits("degrees Centigrade")
_BatteryTempCompRunawayStopVoltage_Type = Integer32
_BatteryTempCompRunawayStopVoltage_Object = MibScalar
batteryTempCompRunawayStopVoltage = _BatteryTempCompRunawayStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 12),
    _BatteryTempCompRunawayStopVoltage_Type()
)
batteryTempCompRunawayStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompRunawayStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTempCompRunawayStopVoltage.setUnits(" *.01 Volts")


class _BatteryTempCompSenseSource_Type(Integer32):
    """Custom type batteryTempCompSenseSource based on Integer32"""
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


_BatteryTempCompSenseSource_Type.__name__ = "Integer32"
_BatteryTempCompSenseSource_Object = MibScalar
batteryTempCompSenseSource = _BatteryTempCompSenseSource_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 13),
    _BatteryTempCompSenseSource_Type()
)
batteryTempCompSenseSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompSenseSource.setStatus("current")


class _BatteryTempCompRunawayState_Type(Integer32):
    """Custom type batteryTempCompRunawayState based on Integer32"""
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


_BatteryTempCompRunawayState_Type.__name__ = "Integer32"
_BatteryTempCompRunawayState_Object = MibScalar
batteryTempCompRunawayState = _BatteryTempCompRunawayState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 14),
    _BatteryTempCompRunawayState_Type()
)
batteryTempCompRunawayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTempCompRunawayState.setStatus("current")
_ThermalProbeTable_Object = MibTable
thermalProbeTable = _ThermalProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 15)
)
if mibBuilder.loadTexts:
    thermalProbeTable.setStatus("current")
_ThermalProbeEntry_Object = MibTableRow
thermalProbeEntry = _ThermalProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 15, 1)
)
if mibBuilder.loadTexts:
    thermalProbeEntry.setStatus("current")


class _ThermalProbeState_Type(Integer32):
    """Custom type thermalProbeState based on Integer32"""
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
        *(("notPresent", 0),
          ("present", 1),
          ("removed", 2),
          ("shorted", 3))
    )


_ThermalProbeState_Type.__name__ = "Integer32"
_ThermalProbeState_Object = MibTableColumn
thermalProbeState = _ThermalProbeState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 1, 15, 1, 1),
    _ThermalProbeState_Type()
)
thermalProbeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thermalProbeState.setStatus("current")
_VpwrBatteryCurrentGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryCurrentGroup = _VpwrBatteryCurrentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2)
)


class _VpwrBatteryCurrentLimitAdminState_Type(Integer32):
    """Custom type vpwrBatteryCurrentLimitAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("battetyCurrentLimitDisabled", 0),
          ("battetyCurrentLimitEnabled", 1))
    )


_VpwrBatteryCurrentLimitAdminState_Type.__name__ = "Integer32"
_VpwrBatteryCurrentLimitAdminState_Object = MibScalar
vpwrBatteryCurrentLimitAdminState = _VpwrBatteryCurrentLimitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2, 1),
    _VpwrBatteryCurrentLimitAdminState_Type()
)
vpwrBatteryCurrentLimitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBatteryCurrentLimitAdminState.setStatus("current")


class _VpwrBattetyCurrentLimitValue_Type(Integer32):
    """Custom type vpwrBattetyCurrentLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_VpwrBattetyCurrentLimitValue_Type.__name__ = "Integer32"
_VpwrBattetyCurrentLimitValue_Object = MibScalar
vpwrBattetyCurrentLimitValue = _VpwrBattetyCurrentLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2, 2),
    _VpwrBattetyCurrentLimitValue_Type()
)
vpwrBattetyCurrentLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBattetyCurrentLimitValue.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBattetyCurrentLimitValue.setUnits("Ampere")


class _VpwrBattetyCurrentValue_Type(Integer32):
    """Custom type vpwrBattetyCurrentValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_VpwrBattetyCurrentValue_Type.__name__ = "Integer32"
_VpwrBattetyCurrentValue_Object = MibScalar
vpwrBattetyCurrentValue = _VpwrBattetyCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 2, 3),
    _VpwrBattetyCurrentValue_Type()
)
vpwrBattetyCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrBattetyCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBattetyCurrentValue.setUnits("Ampere")
_VpwrBatteryBoostGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryBoostGroup = _VpwrBatteryBoostGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3)
)


class _VpwrBoostAdminState_Type(Integer32):
    """Custom type vpwrBoostAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("boostDisabled", 0),
          ("boostEnabled", 1))
    )


_VpwrBoostAdminState_Type.__name__ = "Integer32"
_VpwrBoostAdminState_Object = MibScalar
vpwrBoostAdminState = _VpwrBoostAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 1),
    _VpwrBoostAdminState_Type()
)
vpwrBoostAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostAdminState.setStatus("current")


class _VpwrBoostVoltage_Type(Integer32):
    """Custom type vpwrBoostVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7000, 11000),
    )


_VpwrBoostVoltage_Type.__name__ = "Integer32"
_VpwrBoostVoltage_Object = MibScalar
vpwrBoostVoltage = _VpwrBoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 2),
    _VpwrBoostVoltage_Type()
)
vpwrBoostVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBoostVoltage.setUnits(" *.01 Volts")


class _VpwrBoostDuration_Type(Integer32):
    """Custom type vpwrBoostDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VpwrBoostDuration_Type.__name__ = "Integer32"
_VpwrBoostDuration_Object = MibScalar
vpwrBoostDuration = _VpwrBoostDuration_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 3),
    _VpwrBoostDuration_Type()
)
vpwrBoostDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostDuration.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBoostDuration.setUnits("Hours")


class _VpwrBoostOperState_Type(Integer32):
    """Custom type vpwrBoostOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("boostActive", 1),
          ("boostInactive", 0))
    )


_VpwrBoostOperState_Type.__name__ = "Integer32"
_VpwrBoostOperState_Object = MibScalar
vpwrBoostOperState = _VpwrBoostOperState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 3, 4),
    _VpwrBoostOperState_Type()
)
vpwrBoostOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBoostOperState.setStatus("current")
_VpwrBatteryDischargeTestGroup_ObjectIdentity = ObjectIdentity
vpwrBatteryDischargeTestGroup = _VpwrBatteryDischargeTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4)
)


class _VpwrBDTAdminState_Type(Integer32):
    """Custom type vpwrBDTAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bdtDisabled", 0),
          ("bdtEnabled", 1))
    )


_VpwrBDTAdminState_Type.__name__ = "Integer32"
_VpwrBDTAdminState_Object = MibScalar
vpwrBDTAdminState = _VpwrBDTAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 1),
    _VpwrBDTAdminState_Type()
)
vpwrBDTAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAdminState.setStatus("current")


class _VpwrBDTDuration_Type(Integer32):
    """Custom type vpwrBDTDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 50),
    )


_VpwrBDTDuration_Type.__name__ = "Integer32"
_VpwrBDTDuration_Object = MibScalar
vpwrBDTDuration = _VpwrBDTDuration_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 2),
    _VpwrBDTDuration_Type()
)
vpwrBDTDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTDuration.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTDuration.setUnits("Minutes")


class _VpwrBDTAlarmVoltage_Type(Integer32):
    """Custom type vpwrBDTAlarmVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7000, 11000),
    )


_VpwrBDTAlarmVoltage_Type.__name__ = "Integer32"
_VpwrBDTAlarmVoltage_Object = MibScalar
vpwrBDTAlarmVoltage = _VpwrBDTAlarmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 3),
    _VpwrBDTAlarmVoltage_Type()
)
vpwrBDTAlarmVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAlarmVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTAlarmVoltage.setUnits(" *.01 Volts")


class _VpwrBDTAbortVoltage_Type(Integer32):
    """Custom type vpwrBDTAbortVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5600),
    )


_VpwrBDTAbortVoltage_Type.__name__ = "Integer32"
_VpwrBDTAbortVoltage_Object = MibScalar
vpwrBDTAbortVoltage = _VpwrBDTAbortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 4),
    _VpwrBDTAbortVoltage_Type()
)
vpwrBDTAbortVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAbortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTAbortVoltage.setUnits(" *.01 Volts")


class _VpwrBDTAlarmCoefficient_Type(Integer32):
    """Custom type vpwrBDTAlarmCoefficient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VpwrBDTAlarmCoefficient_Type.__name__ = "Integer32"
_VpwrBDTAlarmCoefficient_Object = MibScalar
vpwrBDTAlarmCoefficient = _VpwrBDTAlarmCoefficient_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 5),
    _VpwrBDTAlarmCoefficient_Type()
)
vpwrBDTAlarmCoefficient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTAlarmCoefficient.setStatus("current")
if mibBuilder.loadTexts:
    vpwrBDTAlarmCoefficient.setUnits("None")


class _VpwrBDTOperState_Type(Integer32):
    """Custom type vpwrBDTOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bdtActive", 1),
          ("bdtInactive", 0))
    )


_VpwrBDTOperState_Type.__name__ = "Integer32"
_VpwrBDTOperState_Object = MibScalar
vpwrBDTOperState = _VpwrBDTOperState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 6),
    _VpwrBDTOperState_Type()
)
vpwrBDTOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTOperState.setStatus("current")


class _VpwrBDTClearAlarm_Type(Integer32):
    """Custom type vpwrBDTClearAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bdtAlarmPresent", 1),
          ("bdtNoAlarm", 0))
    )


_VpwrBDTClearAlarm_Type.__name__ = "Integer32"
_VpwrBDTClearAlarm_Object = MibScalar
vpwrBDTClearAlarm = _VpwrBDTClearAlarm_Object(
    (1, 3, 6, 1, 4, 1, 13858, 7, 4, 7),
    _VpwrBDTClearAlarm_Type()
)
vpwrBDTClearAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrBDTClearAlarm.setStatus("current")
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
    (0, "VALERE-DC-POWER-MIB", "vpwrAlarmIndex"),
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
_SysRelayConfigTable_Object = MibTable
sysRelayConfigTable = _SysRelayConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3)
)
if mibBuilder.loadTexts:
    sysRelayConfigTable.setStatus("current")
_SysRelayConfigEntry_Object = MibTableRow
sysRelayConfigEntry = _SysRelayConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1)
)
sysRelayConfigEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "sysRelayIndex"),
)
if mibBuilder.loadTexts:
    sysRelayConfigEntry.setStatus("current")
_SysRelayIndex_Type = Integer32
_SysRelayIndex_Object = MibTableColumn
sysRelayIndex = _SysRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 1),
    _SysRelayIndex_Type()
)
sysRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRelayIndex.setStatus("current")


class _SysRelayDefaultName_Type(DisplayString):
    """Custom type sysRelayDefaultName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysRelayDefaultName_Type.__name__ = "DisplayString"
_SysRelayDefaultName_Object = MibTableColumn
sysRelayDefaultName = _SysRelayDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 2),
    _SysRelayDefaultName_Type()
)
sysRelayDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRelayDefaultName.setStatus("current")


class _SysRelayCustomName_Type(DisplayString):
    """Custom type sysRelayCustomName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysRelayCustomName_Type.__name__ = "DisplayString"
_SysRelayCustomName_Object = MibTableColumn
sysRelayCustomName = _SysRelayCustomName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 3),
    _SysRelayCustomName_Type()
)
sysRelayCustomName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRelayCustomName.setStatus("current")


class _SysRelayAlarmSeverity_Type(Integer32):
    """Custom type sysRelayAlarmSeverity based on Integer32"""
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
        *(("alarmMajor", 1),
          ("alarmMajorAndMinor", 3),
          ("alarmMinor", 2),
          ("alarmNone", 0))
    )


_SysRelayAlarmSeverity_Type.__name__ = "Integer32"
_SysRelayAlarmSeverity_Object = MibTableColumn
sysRelayAlarmSeverity = _SysRelayAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 3, 1, 4),
    _SysRelayAlarmSeverity_Type()
)
sysRelayAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRelayAlarmSeverity.setStatus("current")
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
    (0, "VALERE-DC-POWER-MIB", "sysAlarmIndex"),
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
_SysAuxAlarmConfigTable_Object = MibTable
sysAuxAlarmConfigTable = _SysAuxAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5)
)
if mibBuilder.loadTexts:
    sysAuxAlarmConfigTable.setStatus("current")
_SysAuxAlarmConfigEntry_Object = MibTableRow
sysAuxAlarmConfigEntry = _SysAuxAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1)
)
sysAuxAlarmConfigEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "sysAuxAlarmIndex"),
)
if mibBuilder.loadTexts:
    sysAuxAlarmConfigEntry.setStatus("current")
_SysAuxAlarmIndex_Type = Integer32
_SysAuxAlarmIndex_Object = MibTableColumn
sysAuxAlarmIndex = _SysAuxAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1, 1),
    _SysAuxAlarmIndex_Type()
)
sysAuxAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAuxAlarmIndex.setStatus("current")


class _SysAuxAlarmDefaultName_Type(DisplayString):
    """Custom type sysAuxAlarmDefaultName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAuxAlarmDefaultName_Type.__name__ = "DisplayString"
_SysAuxAlarmDefaultName_Object = MibTableColumn
sysAuxAlarmDefaultName = _SysAuxAlarmDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1, 2),
    _SysAuxAlarmDefaultName_Type()
)
sysAuxAlarmDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAuxAlarmDefaultName.setStatus("current")


class _SysAuxAlarmCustomName_Type(DisplayString):
    """Custom type sysAuxAlarmCustomName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAuxAlarmCustomName_Type.__name__ = "DisplayString"
_SysAuxAlarmCustomName_Object = MibTableColumn
sysAuxAlarmCustomName = _SysAuxAlarmCustomName_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1, 3),
    _SysAuxAlarmCustomName_Type()
)
sysAuxAlarmCustomName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAuxAlarmCustomName.setStatus("current")


class _SysAuxAlarmSeverity_Type(Integer32):
    """Custom type sysAuxAlarmSeverity based on Integer32"""
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


_SysAuxAlarmSeverity_Type.__name__ = "Integer32"
_SysAuxAlarmSeverity_Object = MibTableColumn
sysAuxAlarmSeverity = _SysAuxAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1, 4),
    _SysAuxAlarmSeverity_Type()
)
sysAuxAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAuxAlarmSeverity.setStatus("current")


class _SysAuxAlarmToRelayMapping_Type(DisplayString):
    """Custom type sysAuxAlarmToRelayMapping based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SysAuxAlarmToRelayMapping_Type.__name__ = "DisplayString"
_SysAuxAlarmToRelayMapping_Object = MibTableColumn
sysAuxAlarmToRelayMapping = _SysAuxAlarmToRelayMapping_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1, 5),
    _SysAuxAlarmToRelayMapping_Type()
)
sysAuxAlarmToRelayMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAuxAlarmToRelayMapping.setStatus("current")


class _SysAuxAlarmPolarity_Type(Integer32):
    """Custom type sysAuxAlarmPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnClose", 1),
          ("alarmOnOpen", 0))
    )


_SysAuxAlarmPolarity_Type.__name__ = "Integer32"
_SysAuxAlarmPolarity_Object = MibTableColumn
sysAuxAlarmPolarity = _SysAuxAlarmPolarity_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1, 6),
    _SysAuxAlarmPolarity_Type()
)
sysAuxAlarmPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAuxAlarmPolarity.setStatus("current")


class _SysAuxAlarmOperStatus_Type(Integer32):
    """Custom type sysAuxAlarmOperStatus based on Integer32"""
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


_SysAuxAlarmOperStatus_Type.__name__ = "Integer32"
_SysAuxAlarmOperStatus_Object = MibTableColumn
sysAuxAlarmOperStatus = _SysAuxAlarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 5, 1, 7),
    _SysAuxAlarmOperStatus_Type()
)
sysAuxAlarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAuxAlarmOperStatus.setStatus("current")


class _SysAlarmComFailState_Type(Integer32):
    """Custom type sysAlarmComFailState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("other", 2))
    )


_SysAlarmComFailState_Type.__name__ = "Integer32"
_SysAlarmComFailState_Object = MibScalar
sysAlarmComFailState = _SysAlarmComFailState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 6),
    _SysAlarmComFailState_Type()
)
sysAlarmComFailState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmComFailState.setStatus("current")


class _SysAlarmIShareState_Type(Integer32):
    """Custom type sysAlarmIShareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("other", 2))
    )


_SysAlarmIShareState_Type.__name__ = "Integer32"
_SysAlarmIShareState_Object = MibScalar
sysAlarmIShareState = _SysAlarmIShareState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 7),
    _SysAlarmIShareState_Type()
)
sysAlarmIShareState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmIShareState.setStatus("current")


class _SysAlarmRedundancyState_Type(Integer32):
    """Custom type sysAlarmRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("nPlus1", 1),
          ("nPlus2", 2))
    )


_SysAlarmRedundancyState_Type.__name__ = "Integer32"
_SysAlarmRedundancyState_Object = MibScalar
sysAlarmRedundancyState = _SysAlarmRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 8, 8),
    _SysAlarmRedundancyState_Type()
)
sysAlarmRedundancyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAlarmRedundancyState.setStatus("current")
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
_VpwrTrapEntry_Object = MibTableRow
vpwrTrapEntry = _VpwrTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 9, 1, 1)
)
vpwrTrapEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "vpwrTrapIpIndex"),
)
if mibBuilder.loadTexts:
    vpwrTrapEntry.setStatus("current")
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
_VpwrTrapUserIpAddress_Type = IpAddress
_VpwrTrapUserIpAddress_Object = MibScalar
vpwrTrapUserIpAddress = _VpwrTrapUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 2),
    _VpwrTrapUserIpAddress_Type()
)
vpwrTrapUserIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpwrTrapUserIpAddress.setStatus("current")
_VpwrTrapEventTimeStamp_Type = IpAddress
_VpwrTrapEventTimeStamp_Object = MibScalar
vpwrTrapEventTimeStamp = _VpwrTrapEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13858, 11, 3),
    _VpwrTrapEventTimeStamp_Type()
)
vpwrTrapEventTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpwrTrapEventTimeStamp.setStatus("current")
_VpwrDcPowerRinger_ObjectIdentity = ObjectIdentity
vpwrDcPowerRinger = _VpwrDcPowerRinger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12)
)
_VpwrRingerConfigGroup_ObjectIdentity = ObjectIdentity
vpwrRingerConfigGroup = _VpwrRingerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1)
)
_VpwrRingerParameterTable_Object = MibTable
vpwrRingerParameterTable = _VpwrRingerParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1)
)
if mibBuilder.loadTexts:
    vpwrRingerParameterTable.setStatus("current")
_VpwrRingerParameterEntry_Object = MibTableRow
vpwrRingerParameterEntry = _VpwrRingerParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1, 1)
)
vpwrRingerParameterEntry.setIndexNames(
    (0, "VALERE-DC-POWER-MIB", "vpwrModuleIndex"),
    (0, "VALERE-DC-POWER-MIB", "vpwrRingerIndex"),
)
if mibBuilder.loadTexts:
    vpwrRingerParameterEntry.setStatus("current")
_VpwrRingerIndex_Type = Integer32
_VpwrRingerIndex_Object = MibTableColumn
vpwrRingerIndex = _VpwrRingerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1, 1, 1),
    _VpwrRingerIndex_Type()
)
vpwrRingerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrRingerIndex.setStatus("current")


class _VpwrRingerParameterAdminState_Type(Integer32):
    """Custom type vpwrRingerParameterAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringerAOn", 1),
          ("ringerBOn", 2),
          ("ringerDisabled", 0))
    )


_VpwrRingerParameterAdminState_Type.__name__ = "Integer32"
_VpwrRingerParameterAdminState_Object = MibTableColumn
vpwrRingerParameterAdminState = _VpwrRingerParameterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1, 1, 2),
    _VpwrRingerParameterAdminState_Type()
)
vpwrRingerParameterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterAdminState.setStatus("current")


class _VpwrRingerParameterAcVoltage_Type(Integer32):
    """Custom type vpwrRingerParameterAcVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7000, 11000),
    )


_VpwrRingerParameterAcVoltage_Type.__name__ = "Integer32"
_VpwrRingerParameterAcVoltage_Object = MibTableColumn
vpwrRingerParameterAcVoltage = _VpwrRingerParameterAcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1, 1, 3),
    _VpwrRingerParameterAcVoltage_Type()
)
vpwrRingerParameterAcVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterAcVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRingerParameterAcVoltage.setUnits(" *.01 Volts")


class _VpwrRingerParameterDcVoltage_Type(Integer32):
    """Custom type vpwrRingerParameterDcVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5600),
    )


_VpwrRingerParameterDcVoltage_Type.__name__ = "Integer32"
_VpwrRingerParameterDcVoltage_Object = MibTableColumn
vpwrRingerParameterDcVoltage = _VpwrRingerParameterDcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1, 1, 4),
    _VpwrRingerParameterDcVoltage_Type()
)
vpwrRingerParameterDcVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterDcVoltage.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRingerParameterDcVoltage.setUnits(" *.01 Volts")


class _VpwrRingerParameterFrequency_Type(Integer32):
    """Custom type vpwrRingerParameterFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 50),
    )


_VpwrRingerParameterFrequency_Type.__name__ = "Integer32"
_VpwrRingerParameterFrequency_Object = MibTableColumn
vpwrRingerParameterFrequency = _VpwrRingerParameterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 1, 1, 5),
    _VpwrRingerParameterFrequency_Type()
)
vpwrRingerParameterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpwrRingerParameterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    vpwrRingerParameterFrequency.setUnits(" Hz")
_VpwrRingerNumberPresent_Type = Gauge32
_VpwrRingerNumberPresent_Object = MibScalar
vpwrRingerNumberPresent = _VpwrRingerNumberPresent_Object(
    (1, 3, 6, 1, 4, 1, 13858, 12, 1, 2),
    _VpwrRingerNumberPresent_Type()
)
vpwrRingerNumberPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpwrRingerNumberPresent.setStatus("current")
_VpwrRingerAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmGroup = _VpwrRingerAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2)
)
_VpwrRingerAlarmaAFailed_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmaAFailed = _VpwrRingerAlarmaAFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 1)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmaAFailed.setStatus("current")
_VpwrRingerAlarmAOTemp_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmAOTemp = _VpwrRingerAlarmAOTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 2)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmAOTemp.setStatus("current")
_VpwrRingerAlarmAOCurrent_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmAOCurrent = _VpwrRingerAlarmAOCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 3)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmAOCurrent.setStatus("current")
_VpwrRingerAlarmaBFailed_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmaBFailed = _VpwrRingerAlarmaBFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 4)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmaBFailed.setStatus("current")
_VpwrRingerAlarmBOverTemp_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmBOverTemp = _VpwrRingerAlarmBOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 5)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmBOverTemp.setStatus("current")
_VpwrRingerAlarmBOverCurrent_ObjectIdentity = ObjectIdentity
vpwrRingerAlarmBOverCurrent = _VpwrRingerAlarmBOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 2, 6)
)
if mibBuilder.loadTexts:
    vpwrRingerAlarmBOverCurrent.setStatus("current")
_VpwrRingerTestGroup_ObjectIdentity = ObjectIdentity
vpwrRingerTestGroup = _VpwrRingerTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 12, 3)
)
_VpwrDcPowerDcDcConverter_ObjectIdentity = ObjectIdentity
vpwrDcPowerDcDcConverter = _VpwrDcPowerDcDcConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13)
)
_VpwrDcDcConverterConfigGroup_ObjectIdentity = ObjectIdentity
vpwrDcDcConverterConfigGroup = _VpwrDcDcConverterConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13, 1)
)
_VpwrDcDcConverterAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrDcDcConverterAlarmGroup = _VpwrDcDcConverterAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13, 2)
)
_VpwrDcDcConverterTestGroup_ObjectIdentity = ObjectIdentity
vpwrDcDcConverterTestGroup = _VpwrDcDcConverterTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 13, 3)
)
_VpwrDcPowerDcAcInverter_ObjectIdentity = ObjectIdentity
vpwrDcPowerDcAcInverter = _VpwrDcPowerDcAcInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14)
)
_VpwrDcAcInverterConfigGroup_ObjectIdentity = ObjectIdentity
vpwrDcAcInverterConfigGroup = _VpwrDcAcInverterConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14, 1)
)
_VpwrDcAcInverterAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrDcAcInverterAlarmGroup = _VpwrDcAcInverterAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14, 2)
)
_VpwrDcAcInverterTestGroup_ObjectIdentity = ObjectIdentity
vpwrDcAcInverterTestGroup = _VpwrDcAcInverterTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 14, 3)
)
_VpwrDcPowerBayController_ObjectIdentity = ObjectIdentity
vpwrDcPowerBayController = _VpwrDcPowerBayController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 15)
)
_VpwrDcPowerIoModule_ObjectIdentity = ObjectIdentity
vpwrDcPowerIoModule = _VpwrDcPowerIoModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16)
)
_VpwrIoModuleConfigGroup_ObjectIdentity = ObjectIdentity
vpwrIoModuleConfigGroup = _VpwrIoModuleConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16, 1)
)
_VpwrIoModuleAlarmGroup_ObjectIdentity = ObjectIdentity
vpwrIoModuleAlarmGroup = _VpwrIoModuleAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16, 2)
)
_VpwrIoModuleTestGroup_ObjectIdentity = ObjectIdentity
vpwrIoModuleTestGroup = _VpwrIoModuleTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 16, 3)
)
_VpwrDcPowerDist_ObjectIdentity = ObjectIdentity
vpwrDcPowerDist = _VpwrDcPowerDist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 17)
)
_VpwrDcPowerTrio_ObjectIdentity = ObjectIdentity
vpwrDcPowerTrio = _VpwrDcPowerTrio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13858, 18)
)
vpwrSystemIdentEntry.registerAugmentions(
    ("VALERE-DC-POWER-MIB",
     "vpwrModuleIdentEntry")
)
vpwrModuleIdentEntry.setIndexNames(*vpwrSystemIdentEntry.getIndexNames())
VpwrPanelIdentEntry.registerAugmentions(
    ("VALERE-DC-POWER-MIB",
     "vpwrPanelModuleIdentEntry")
)
vpwrPanelModuleIdentEntry.setIndexNames(*VpwrPanelIdentEntry.getIndexNames())
VpwrBayctrlIdentEntry.registerAugmentions(
    ("VALERE-DC-POWER-MIB",
     "vpwrBayctrlModuleIdentEntry")
)
vpwrBayctrlModuleIdentEntry.setIndexNames(*VpwrBayctrlIdentEntry.getIndexNames())
vpwrBatteryTempEntry.registerAugmentions(
    ("VALERE-DC-POWER-MIB",
     "thermalProbeEntry")
)
thermalProbeEntry.setIndexNames(*vpwrBatteryTempEntry.getIndexNames())

# Managed Objects groups


# Notification objects

vpwrTrapPowerMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 1)
)
vpwrTrapPowerMajorAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPowerMajorAlarm.setStatus(
        ""
    )

vpwrTrapPowerMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 2)
)
vpwrTrapPowerMinorAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapPowerMinorAlarm.setStatus(
        ""
    )

vpwrTrapACFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 3)
)
vpwrTrapACFAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapACFAlarm.setStatus(
        ""
    )

vpwrTrapHVAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 4)
)
vpwrTrapHVAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapHVAlarm.setStatus(
        ""
    )

vpwrTrapHVSDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 5)
)
vpwrTrapHVSDAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapHVSDAlarm.setStatus(
        ""
    )

vpwrTrapBDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 6)
)
vpwrTrapBDAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBDAlarm.setStatus(
        ""
    )

vpwrTrapLVDWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 7)
)
vpwrTrapLVDWarningAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLVDWarningAlarm.setStatus(
        ""
    )

vpwrTrapLVDOpenAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 8)
)
vpwrTrapLVDOpenAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLVDOpenAlarm.setStatus(
        ""
    )

vpwrTrapDistAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 9)
)
vpwrTrapDistAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDistAlarm.setStatus(
        ""
    )

vpwrTrapAuxAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 10)
)
vpwrTrapAuxAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapAuxAlarm.setStatus(
        ""
    )

vpwrTrapSystemRedundancyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 11)
)
vpwrTrapSystemRedundancyAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemRedundancyAlarm.setStatus(
        ""
    )

vpwrTrapIShareAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 12)
)
vpwrTrapIShareAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapIShareAlarm.setStatus(
        ""
    )

vpwrTrapModuleFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 13)
)
vpwrTrapModuleFailAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleFailAlarm.setStatus(
        ""
    )

vpwrTrapMultipleModuleFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 14)
)
vpwrTrapMultipleModuleFailAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultipleModuleFailAlarm.setStatus(
        ""
    )

vpwrTrapModuleCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 15)
)
vpwrTrapModuleCommAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleCommAlarm.setStatus(
        ""
    )

vpwrTrapSystemOverTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 16)
)
vpwrTrapSystemOverTemperatureAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemOverTemperatureAlarm.setStatus(
        ""
    )

vpwrTrapSystemOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 17)
)
vpwrTrapSystemOK.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemOK.setStatus(
        ""
    )

vpwrTrapModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 18)
)
vpwrTrapModuleInserted.setObjects(
      *(("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("VALERE-DC-POWER-MIB", "vpwrBayIndex"),
        ("VALERE-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapModuleInserted.setStatus(
        ""
    )

vpwrTrapModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 19)
)
vpwrTrapModuleRemoved.setObjects(
      *(("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString"),
        ("VALERE-DC-POWER-MIB", "vpwrBayIndex"),
        ("VALERE-DC-POWER-MIB", "vpwrModuleIndex"))
)
if mibBuilder.loadTexts:
    vpwrTrapModuleRemoved.setStatus(
        ""
    )

vpwrTrapThermalCompActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 20)
)
vpwrTrapThermalCompActive.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalCompActive.setStatus(
        ""
    )

vpwrTrapThermalCompInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 21)
)
vpwrTrapThermalCompInactive.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalCompInactive.setStatus(
        ""
    )

vpwrTrapInternalTempAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 22)
)
vpwrTrapInternalTempAlarmSet.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapInternalTempAlarmSet.setStatus(
        ""
    )

vpwrTrapInternalTempAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 23)
)
vpwrTrapInternalTempAlarmCleared.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapInternalTempAlarmCleared.setStatus(
        ""
    )

vpwrTrapBatteryTempAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 24)
)
vpwrTrapBatteryTempAlarmSet.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryTempAlarmSet.setStatus(
        ""
    )

vpwrTrapBatteryTempAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 25)
)
vpwrTrapBatteryTempAlarmCleared.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryTempAlarmCleared.setStatus(
        ""
    )

vpwrTrapLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 26)
)
vpwrTrapLoginFail.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLoginFail.setStatus(
        ""
    )

vpwrTrapLoginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 27)
)
vpwrTrapLoginSuccess.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLoginSuccess.setStatus(
        ""
    )

vpwrTrapLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 28)
)
vpwrTrapLogout.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapLogout.setStatus(
        ""
    )

vpwrTrapAdminPwdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 29)
)
vpwrTrapAdminPwdChange.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapAdminPwdChange.setStatus(
        ""
    )

vpwrTrapIllegalConfigSubmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 30)
)
vpwrTrapIllegalConfigSubmit.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapIllegalConfigSubmit.setStatus(
        ""
    )

vpwrTrapCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 31)
)
vpwrTrapCfgChange.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapCfgChange.setStatus(
        ""
    )

vpwrTrapClearEventHistory = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 32)
)
vpwrTrapClearEventHistory.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapClearEventHistory.setStatus(
        ""
    )

vpwrTrapSwDownloadNoReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 33)
)
vpwrTrapSwDownloadNoReboot.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSwDownloadNoReboot.setStatus(
        ""
    )

vpwrTrapSwDownloadAndReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 34)
)
vpwrTrapSwDownloadAndReboot.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSwDownloadAndReboot.setStatus(
        ""
    )

vpwrTrapSystemClockChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 35)
)
vpwrTrapSystemClockChange.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemClockChange.setStatus(
        ""
    )

vpwrTrapModuleAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 36)
)
vpwrTrapModuleAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapModuleAlarm.setStatus(
        ""
    )

vpwrTrapOIDChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 37)
)
vpwrTrapOIDChange.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapOIDChange.setStatus(
        ""
    )

vpwrTrapThermalRunaway = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 38)
)
vpwrTrapThermalRunaway.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalRunaway.setStatus(
        ""
    )

vpwrTrapBatteryDischargeTestAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 39)
)
vpwrTrapBatteryDischargeTestAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryDischargeTestAlarm.setStatus(
        ""
    )

vpwrTrapRingerAAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 40)
)
vpwrTrapRingerAAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapRingerAAlarm.setStatus(
        ""
    )

vpwrTrapRingerBAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 41)
)
vpwrTrapRingerBAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapRingerBAlarm.setStatus(
        ""
    )

vpwrTrapSingleRingerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 42)
)
vpwrTrapSingleRingerAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSingleRingerAlarm.setStatus(
        ""
    )

vpwrTrapMultipleRingerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 43)
)
vpwrTrapMultipleRingerAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultipleRingerAlarm.setStatus(
        ""
    )

vpwrTrapThermalProbeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 44)
)
vpwrTrapThermalProbeAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapThermalProbeAlarm.setStatus(
        ""
    )

vpwrTrapRingerCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 45)
)
vpwrTrapRingerCommAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapRingerCommAlarm.setStatus(
        ""
    )

vpwrTrapDistributionCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 46)
)
vpwrTrapDistributionCommAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDistributionCommAlarm.setStatus(
        ""
    )

vpwrTrapConverterAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 47)
)
vpwrTrapConverterAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapConverterAlarm.setStatus(
        ""
    )

vpwrTrapMultipleConvFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 48)
)
vpwrTrapMultipleConvFailAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapMultipleConvFailAlarm.setStatus(
        ""
    )

vpwrTrapUnmappedAddressAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 49)
)
vpwrTrapUnmappedAddressAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapUnmappedAddressAlarm.setStatus(
        ""
    )

vpwrTrapConfigErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 50)
)
vpwrTrapConfigErrorAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapConfigErrorAlarm.setStatus(
        ""
    )

vpwrTrapDisplayFirmwareMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 51)
)
vpwrTrapDisplayFirmwareMismatchAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapDisplayFirmwareMismatchAlarm.setStatus(
        ""
    )

vpwrTrapConverterInputFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 52)
)
vpwrTrapConverterInputFailAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapConverterInputFailAlarm.setStatus(
        ""
    )

vpwrTrapBatteryRechgIlimitFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 53)
)
vpwrTrapBatteryRechgIlimitFailAlarm.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapBatteryRechgIlimitFailAlarm.setStatus(
        ""
    )

vpwrTrapSystemAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13858, 10, 0, 54)
)
vpwrTrapSystemAlive.setObjects(
    ("VALERE-DC-POWER-MIB", "vpwrTrapsMsgString")
)
if mibBuilder.loadTexts:
    vpwrTrapSystemAlive.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VALERE-DC-POWER-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "vpwrDcPowerMgt": vpwrDcPowerMgt,
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
       "vpwrBayIndex": vpwrBayIndex,
       "vpwrModuleIndex": vpwrModuleIndex,
       "vpwrModuleOID": vpwrModuleOID,
       "vpwrModuleCurrent": vpwrModuleCurrent,
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
       "vpwrSystemPanelIdentGroup": vpwrSystemPanelIdentGroup,
       "vpwrPanelIdentTable": vpwrPanelIdentTable,
       "vpwrPanelIdentEntry": vpwrPanelIdentEntry,
       "vpwrPanelBayIndex": vpwrPanelBayIndex,
       "vpwrPanelModuleIndex": vpwrPanelModuleIndex,
       "vpwrPanelModuleOID": vpwrPanelModuleOID,
       "vpwrPanelModuleCurrent": vpwrPanelModuleCurrent,
       "vpwrPanelModuleOperStatus": vpwrPanelModuleOperStatus,
       "vpwrPanelModuleCapacity": vpwrPanelModuleCapacity,
       "vpwrSystemBayctrlIdentGroup": vpwrSystemBayctrlIdentGroup,
       "vpwrBayctrlIdentTable": vpwrBayctrlIdentTable,
       "vpwrBayctrlIdentEntry": vpwrBayctrlIdentEntry,
       "vpwrBayctrlIndex": vpwrBayctrlIndex,
       "vpwrBayctrlOID": vpwrBayctrlOID,
       "vpwrBayctrlCurrent": vpwrBayctrlCurrent,
       "vpwrBayctrlOperStatus": vpwrBayctrlOperStatus,
       "vpwrBayctrlCapacity": vpwrBayctrlCapacity,
       "vpwrDcPowerRectifier": vpwrDcPowerRectifier,
       "vpwrRectifierConfigGroup": vpwrRectifierConfigGroup,
       "vpwrRectifierFVSetpoint": vpwrRectifierFVSetpoint,
       "vpwrRectifierHVSDSetpoint": vpwrRectifierHVSDSetpoint,
       "vpwrRectifierCurrentLimitAdminState": vpwrRectifierCurrentLimitAdminState,
       "vpwrRectifierCurrentLimit": vpwrRectifierCurrentLimit,
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
       "vpwrLvdContactorConfigTable": vpwrLvdContactorConfigTable,
       "vpwrLvdContactorConfigEntry": vpwrLvdContactorConfigEntry,
       "vpwrLvdContactorIndex": vpwrLvdContactorIndex,
       "vpwrLvdContactorWarningSetpoint": vpwrLvdContactorWarningSetpoint,
       "vpwrLvdContactorDisconnectSetpoint": vpwrLvdContactorDisconnectSetpoint,
       "vpwrLvdContactorReconnectSetpoint": vpwrLvdContactorReconnectSetpoint,
       "vpwrLvdContactorReconnectDelayTimer": vpwrLvdContactorReconnectDelayTimer,
       "vpwrLvdContactorState": vpwrLvdContactorState,
       "vpwrLvdAlarmGroup": vpwrLvdAlarmGroup,
       "vpwrLvdAlarmContactorOpen": vpwrLvdAlarmContactorOpen,
       "vpwrLvdAlarmCBOpen": vpwrLvdAlarmCBOpen,
       "vpwrTrapLvdFuseOpen": vpwrTrapLvdFuseOpen,
       "vpwrLvdAlarmWarning": vpwrLvdAlarmWarning,
       "vpwrLvdTestGroup": vpwrLvdTestGroup,
       "vpwrDcPowerTest": vpwrDcPowerTest,
       "vpwrDcPowerModuleIdent": vpwrDcPowerModuleIdent,
       "vpwrModuleIdentTable": vpwrModuleIdentTable,
       "vpwrModuleIdentEntry": vpwrModuleIdentEntry,
       "vpwrModuleSerialNumber": vpwrModuleSerialNumber,
       "vpwrModuleModelNumber": vpwrModuleModelNumber,
       "vpwrModuleFwVersion": vpwrModuleFwVersion,
       "vpwrModuleTestDate": vpwrModuleTestDate,
       "vpwrModuleOperHours": vpwrModuleOperHours,
       "vpwrPanelModuleIdentTable": vpwrPanelModuleIdentTable,
       "vpwrPanelModuleIdentEntry": vpwrPanelModuleIdentEntry,
       "vpwrPanelModuleSerialNumber": vpwrPanelModuleSerialNumber,
       "vpwrPanelModuleModelNumber": vpwrPanelModuleModelNumber,
       "vpwrPanelModuleFwVersion": vpwrPanelModuleFwVersion,
       "vpwrPanelModuleTestDate": vpwrPanelModuleTestDate,
       "vpwrPanelModuleOperHours": vpwrPanelModuleOperHours,
       "vpwrBayctrlModuleIdentTable": vpwrBayctrlModuleIdentTable,
       "vpwrBayctrlModuleIdentEntry": vpwrBayctrlModuleIdentEntry,
       "vpwrBayctrlSerialNumber": vpwrBayctrlSerialNumber,
       "vpwrBayctrlModelNumber": vpwrBayctrlModelNumber,
       "vpwrBayctrlFwVersion": vpwrBayctrlFwVersion,
       "vpwrBayctrlTestDate": vpwrBayctrlTestDate,
       "vpwrBayctrlOperHours": vpwrBayctrlOperHours,
       "vpwrDcPowerBatteryGroup": vpwrDcPowerBatteryGroup,
       "vpwrBatteryTempGroup": vpwrBatteryTempGroup,
       "vpwrBatteryTempTable": vpwrBatteryTempTable,
       "vpwrBatteryTempEntry": vpwrBatteryTempEntry,
       "vpwrBatteryTempIndex": vpwrBatteryTempIndex,
       "vpwrBatteryTempName": vpwrBatteryTempName,
       "vpwrBatteryTemp": vpwrBatteryTemp,
       "vpwrBatteryTempLThreshold": vpwrBatteryTempLThreshold,
       "vpwrBatteryTempUThreshold": vpwrBatteryTempUThreshold,
       "batteryTempCompensation": batteryTempCompensation,
       "batteryTempCompHighStartTemperature": batteryTempCompHighStartTemperature,
       "batteryTempCompHighStopVoltage": batteryTempCompHighStopVoltage,
       "batteryTempCompHighSlope": batteryTempCompHighSlope,
       "batteryTempCompLowStartTemperature": batteryTempCompLowStartTemperature,
       "batteryTempCompLowStopVoltage": batteryTempCompLowStopVoltage,
       "batteryTempCompLowSlope": batteryTempCompLowSlope,
       "batteryTempCompRunawayTemperature": batteryTempCompRunawayTemperature,
       "batteryTempCompRunawayStopVoltage": batteryTempCompRunawayStopVoltage,
       "batteryTempCompSenseSource": batteryTempCompSenseSource,
       "batteryTempCompRunawayState": batteryTempCompRunawayState,
       "thermalProbeTable": thermalProbeTable,
       "thermalProbeEntry": thermalProbeEntry,
       "thermalProbeState": thermalProbeState,
       "vpwrBatteryCurrentGroup": vpwrBatteryCurrentGroup,
       "vpwrBatteryCurrentLimitAdminState": vpwrBatteryCurrentLimitAdminState,
       "vpwrBattetyCurrentLimitValue": vpwrBattetyCurrentLimitValue,
       "vpwrBattetyCurrentValue": vpwrBattetyCurrentValue,
       "vpwrBatteryBoostGroup": vpwrBatteryBoostGroup,
       "vpwrBoostAdminState": vpwrBoostAdminState,
       "vpwrBoostVoltage": vpwrBoostVoltage,
       "vpwrBoostDuration": vpwrBoostDuration,
       "vpwrBoostOperState": vpwrBoostOperState,
       "vpwrBatteryDischargeTestGroup": vpwrBatteryDischargeTestGroup,
       "vpwrBDTAdminState": vpwrBDTAdminState,
       "vpwrBDTDuration": vpwrBDTDuration,
       "vpwrBDTAlarmVoltage": vpwrBDTAlarmVoltage,
       "vpwrBDTAbortVoltage": vpwrBDTAbortVoltage,
       "vpwrBDTAlarmCoefficient": vpwrBDTAlarmCoefficient,
       "vpwrBDTOperState": vpwrBDTOperState,
       "vpwrBDTClearAlarm": vpwrBDTClearAlarm,
       "vpwrDcPowerAlarmGroup": vpwrDcPowerAlarmGroup,
       "vpwrAlarmsPresent": vpwrAlarmsPresent,
       "vpwrAlarmTable": vpwrAlarmTable,
       "vpwrAlarmEntry": vpwrAlarmEntry,
       "vpwrAlarmIndex": vpwrAlarmIndex,
       "vpwrAlarmDescr": vpwrAlarmDescr,
       "vpwrAlarmTime": vpwrAlarmTime,
       "sysRelayConfigTable": sysRelayConfigTable,
       "sysRelayConfigEntry": sysRelayConfigEntry,
       "sysRelayIndex": sysRelayIndex,
       "sysRelayDefaultName": sysRelayDefaultName,
       "sysRelayCustomName": sysRelayCustomName,
       "sysRelayAlarmSeverity": sysRelayAlarmSeverity,
       "sysAlarmConfigTable": sysAlarmConfigTable,
       "sysAlarmConfigEntry": sysAlarmConfigEntry,
       "sysAlarmIndex": sysAlarmIndex,
       "sysAlarmDefaultName": sysAlarmDefaultName,
       "sysAlarmCustomName": sysAlarmCustomName,
       "sysAlarmSeverity": sysAlarmSeverity,
       "sysAlarmToRelayMapping": sysAlarmToRelayMapping,
       "sysAlarmOperStatus": sysAlarmOperStatus,
       "sysAuxAlarmConfigTable": sysAuxAlarmConfigTable,
       "sysAuxAlarmConfigEntry": sysAuxAlarmConfigEntry,
       "sysAuxAlarmIndex": sysAuxAlarmIndex,
       "sysAuxAlarmDefaultName": sysAuxAlarmDefaultName,
       "sysAuxAlarmCustomName": sysAuxAlarmCustomName,
       "sysAuxAlarmSeverity": sysAuxAlarmSeverity,
       "sysAuxAlarmToRelayMapping": sysAuxAlarmToRelayMapping,
       "sysAuxAlarmPolarity": sysAuxAlarmPolarity,
       "sysAuxAlarmOperStatus": sysAuxAlarmOperStatus,
       "sysAlarmComFailState": sysAlarmComFailState,
       "sysAlarmIShareState": sysAlarmIShareState,
       "sysAlarmRedundancyState": sysAlarmRedundancyState,
       "vpwrDcPowerSnmpConfig": vpwrDcPowerSnmpConfig,
       "vpwrTrapTable": vpwrTrapTable,
       "vpwrTrapEntry": vpwrTrapEntry,
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
       "vpwrTrapLoginFail": vpwrTrapLoginFail,
       "vpwrTrapLoginSuccess": vpwrTrapLoginSuccess,
       "vpwrTrapLogout": vpwrTrapLogout,
       "vpwrTrapAdminPwdChange": vpwrTrapAdminPwdChange,
       "vpwrTrapIllegalConfigSubmit": vpwrTrapIllegalConfigSubmit,
       "vpwrTrapCfgChange": vpwrTrapCfgChange,
       "vpwrTrapClearEventHistory": vpwrTrapClearEventHistory,
       "vpwrTrapSwDownloadNoReboot": vpwrTrapSwDownloadNoReboot,
       "vpwrTrapSwDownloadAndReboot": vpwrTrapSwDownloadAndReboot,
       "vpwrTrapSystemClockChange": vpwrTrapSystemClockChange,
       "vpwrTrapModuleAlarm": vpwrTrapModuleAlarm,
       "vpwrTrapOIDChange": vpwrTrapOIDChange,
       "vpwrTrapThermalRunaway": vpwrTrapThermalRunaway,
       "vpwrTrapBatteryDischargeTestAlarm": vpwrTrapBatteryDischargeTestAlarm,
       "vpwrTrapRingerAAlarm": vpwrTrapRingerAAlarm,
       "vpwrTrapRingerBAlarm": vpwrTrapRingerBAlarm,
       "vpwrTrapSingleRingerAlarm": vpwrTrapSingleRingerAlarm,
       "vpwrTrapMultipleRingerAlarm": vpwrTrapMultipleRingerAlarm,
       "vpwrTrapThermalProbeAlarm": vpwrTrapThermalProbeAlarm,
       "vpwrTrapRingerCommAlarm": vpwrTrapRingerCommAlarm,
       "vpwrTrapDistributionCommAlarm": vpwrTrapDistributionCommAlarm,
       "vpwrTrapConverterAlarm": vpwrTrapConverterAlarm,
       "vpwrTrapMultipleConvFailAlarm": vpwrTrapMultipleConvFailAlarm,
       "vpwrTrapUnmappedAddressAlarm": vpwrTrapUnmappedAddressAlarm,
       "vpwrTrapConfigErrorAlarm": vpwrTrapConfigErrorAlarm,
       "vpwrTrapDisplayFirmwareMismatchAlarm": vpwrTrapDisplayFirmwareMismatchAlarm,
       "vpwrTrapConverterInputFailAlarm": vpwrTrapConverterInputFailAlarm,
       "vpwrTrapBatteryRechgIlimitFailAlarm": vpwrTrapBatteryRechgIlimitFailAlarm,
       "vpwrTrapSystemAlive": vpwrTrapSystemAlive,
       "vpwrDcPowerTrapsMsgString": vpwrDcPowerTrapsMsgString,
       "vpwrTrapsMsgString": vpwrTrapsMsgString,
       "vpwrTrapUserIpAddress": vpwrTrapUserIpAddress,
       "vpwrTrapEventTimeStamp": vpwrTrapEventTimeStamp,
       "vpwrDcPowerRinger": vpwrDcPowerRinger,
       "vpwrRingerConfigGroup": vpwrRingerConfigGroup,
       "vpwrRingerParameterTable": vpwrRingerParameterTable,
       "vpwrRingerParameterEntry": vpwrRingerParameterEntry,
       "vpwrRingerIndex": vpwrRingerIndex,
       "vpwrRingerParameterAdminState": vpwrRingerParameterAdminState,
       "vpwrRingerParameterAcVoltage": vpwrRingerParameterAcVoltage,
       "vpwrRingerParameterDcVoltage": vpwrRingerParameterDcVoltage,
       "vpwrRingerParameterFrequency": vpwrRingerParameterFrequency,
       "vpwrRingerNumberPresent": vpwrRingerNumberPresent,
       "vpwrRingerAlarmGroup": vpwrRingerAlarmGroup,
       "vpwrRingerAlarmaAFailed": vpwrRingerAlarmaAFailed,
       "vpwrRingerAlarmAOTemp": vpwrRingerAlarmAOTemp,
       "vpwrRingerAlarmAOCurrent": vpwrRingerAlarmAOCurrent,
       "vpwrRingerAlarmaBFailed": vpwrRingerAlarmaBFailed,
       "vpwrRingerAlarmBOverTemp": vpwrRingerAlarmBOverTemp,
       "vpwrRingerAlarmBOverCurrent": vpwrRingerAlarmBOverCurrent,
       "vpwrRingerTestGroup": vpwrRingerTestGroup,
       "vpwrDcPowerDcDcConverter": vpwrDcPowerDcDcConverter,
       "vpwrDcDcConverterConfigGroup": vpwrDcDcConverterConfigGroup,
       "vpwrDcDcConverterAlarmGroup": vpwrDcDcConverterAlarmGroup,
       "vpwrDcDcConverterTestGroup": vpwrDcDcConverterTestGroup,
       "vpwrDcPowerDcAcInverter": vpwrDcPowerDcAcInverter,
       "vpwrDcAcInverterConfigGroup": vpwrDcAcInverterConfigGroup,
       "vpwrDcAcInverterAlarmGroup": vpwrDcAcInverterAlarmGroup,
       "vpwrDcAcInverterTestGroup": vpwrDcAcInverterTestGroup,
       "vpwrDcPowerBayController": vpwrDcPowerBayController,
       "vpwrDcPowerIoModule": vpwrDcPowerIoModule,
       "vpwrIoModuleConfigGroup": vpwrIoModuleConfigGroup,
       "vpwrIoModuleAlarmGroup": vpwrIoModuleAlarmGroup,
       "vpwrIoModuleTestGroup": vpwrIoModuleTestGroup,
       "vpwrDcPowerDist": vpwrDcPowerDist,
       "vpwrDcPowerTrio": vpwrDcPowerTrio}
)
