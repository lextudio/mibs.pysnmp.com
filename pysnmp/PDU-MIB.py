# SNMP MIB module (PDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:16 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raritan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
raritan.setRevisions(
        ("2016-02-22 00:00",
         "2016-02-03 00:00",
         "2015-11-02 00:00",
         "2015-10-26 00:00",
         "2015-10-16 00:00",
         "2015-10-02 00:00",
         "2015-06-19 00:00",
         "2015-03-11 00:00",
         "2014-04-03 00:00",
         "2012-03-22 00:00",
         "2012-03-15 00:00",
         "2012-03-14 00:00",
         "2011-11-30 00:00",
         "2011-11-07 00:00",
         "2011-10-06 00:00",
         "2011-05-17 00:00",
         "2011-05-11 00:00",
         "2011-04-18 00:00",
         "2011-02-14 00:00",
         "2011-01-24 00:00",
         "2010-11-30 00:00",
         "2010-11-04 00:00",
         "2010-07-21 00:00",
         "2010-07-19 00:00",
         "2010-07-15 00:00",
         "2010-07-13 00:00",
         "2010-06-29 00:00",
         "2010-06-07 00:00",
         "2010-05-27 00:00",
         "2010-05-20 00:00",
         "2010-05-17 00:00",
         "2009-06-09 00:00",
         "2009-04-20 00:00",
         "2009-02-13 00:00",
         "2009-02-12 00:00",
         "2008-12-01 00:00",
         "2008-10-24 00:00",
         "2008-09-25 00:00",
         "2008-09-05 00:00",
         "2008-06-05 00:00",
         "2007-11-28 00:00",
         "2007-06-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliAmps(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class MilliVolts(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class Watts(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class VoltAmps(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class DegreesCelsius(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class TenthDegreesCelsius(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class Hertz(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class RelativeHumidity(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class PowerFactorPercentage(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class Percentage(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class SensorTypeEnumeration(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              200,
              201,
              202,
              203,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              550,
              551,
              552,
              600,
              601,
              602)
        )
    )
    namedValues = NamedValues(
        *(("environmentalHumidity1", 400),
          ("environmentalHumidity2", 401),
          ("environmentalHumidity3", 402),
          ("environmentalHumidity4", 403),
          ("environmentalHumidity5", 404),
          ("environmentalHumidity6", 405),
          ("environmentalHumidity7", 406),
          ("environmentalHumidity8", 407),
          ("environmentalTemp1", 300),
          ("environmentalTemp2", 301),
          ("environmentalTemp3", 302),
          ("environmentalTemp4", 303),
          ("environmentalTemp5", 304),
          ("environmentalTemp6", 305),
          ("environmentalTemp7", 306),
          ("environmentalTemp8", 307),
          ("outletActivePower", 3),
          ("outletApparentPower", 4),
          ("outletAverageActivePower", 6),
          ("outletCurrent", 0),
          ("outletMaxActivePower", 5),
          ("outletMaxCurrent", 1),
          ("outletPowerFactor", 7),
          ("outletVoltage", 2),
          ("powerBranchCurrent", 203),
          ("powerBranchFrequency", 201),
          ("powerBranchTemperature", 202),
          ("powerBranchVoltage", 200),
          ("unitActivePower", 504),
          ("unitApparentPower", 505),
          ("unitCircuitBreak0Current", 600),
          ("unitCircuitBreak0State", 550),
          ("unitCircuitBreak1Current", 601),
          ("unitCircuitBreak1State", 551),
          ("unitCircuitBreak2Current", 602),
          ("unitCircuitBreak2State", 552),
          ("unitCpuTemp", 503),
          ("unitFrequency", 506),
          ("unitMaxRmsCurrent", 501),
          ("unitRmsCurrent", 500),
          ("unitVoltage", 502))
    )



class SensorStateEnumeration(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aboveUpperCritical", 4),
          ("aboveUpperWarning", 2),
          ("belowLowerCritical", 3),
          ("belowLowerWarning", 1),
          ("ok", 0),
          ("unavailable", -1))
    )



class StateOfSensorEnumeration(Integer32, TextualConvention):
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



class TypeOfSensorEnumeration(Integer32, TextualConvention):
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
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("activeEnergy", 8),
          ("activePower", 5),
          ("airFlow", 12),
          ("airPressure", 13),
          ("apparentEnergy", 9),
          ("apparentPower", 6),
          ("binary", 19),
          ("contact", 20),
          ("humidity", 11),
          ("none", 31),
          ("onOff", 14),
          ("other", 30),
          ("peakCurrent", 2),
          ("powerFactor", 7),
          ("rmsCurrent", 1),
          ("rmsVoltage", 4),
          ("smokeDetection", 18),
          ("temperature", 10),
          ("trip", 15),
          ("unbalancedCurrent", 3),
          ("vibration", 16),
          ("waterDetection", 17))
    )



class WattHours(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


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
              18)
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
          ("volt", 1),
          ("voltamp", 4),
          ("voltampHour", 6),
          ("watt", 3),
          ("wattHour", 5))
    )



class PowerCIMStatusEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class EnabledDisabledEnumeration(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class SensorClassEnumeration(Integer32, TextualConvention):
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
        *(("externalAirFlow", 2),
          ("externalAirPressure", 3),
          ("externalHumidity", 1),
          ("externalTemperature", 0))
    )



class EventTypeEnumeration(Integer32, TextualConvention):
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
        *(("aboveUpperCritical", 0),
          ("aboveUpperNonCritical", 1),
          ("belowLowerCritical", 3),
          ("belowLowerNonCritical", 2))
    )



class EventDirectionEnumeration(Integer32, TextualConvention):
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
        *(("asserted", 0),
          ("both", 2),
          ("deasserted", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0)
)
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1)
)
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 1),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 3),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_Netmask_Type = IpAddress
_Netmask_Object = MibScalar
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 4),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 5),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_Mac_Type = MacAddress
_Mac_Object = MibScalar
mac = _Mac_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 6),
    _Mac_Type()
)
mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mac.setStatus("current")


class _HardwareRev_Type(Integer32):
    """Custom type hardwareRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HardwareRev_Type.__name__ = "Integer32"
_HardwareRev_Object = MibScalar
hardwareRev = _HardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 7),
    _HardwareRev_Type()
)
hardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRev.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 10),
    _UserName_Type()
)
userName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_ObjectName_Type = DisplayString
_ObjectName_Object = MibScalar
objectName = _ObjectName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 12),
    _ObjectName_Type()
)
objectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    objectName.setStatus("current")
_ObjectInstance_Type = DisplayString
_ObjectInstance_Object = MibScalar
objectInstance = _ObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 13),
    _ObjectInstance_Type()
)
objectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    objectInstance.setStatus("current")
_TargetUser_Type = DisplayString
_TargetUser_Object = MibScalar
targetUser = _TargetUser_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 14),
    _TargetUser_Type()
)
targetUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    targetUser.setStatus("current")
_GroupName_Type = DisplayString
_GroupName_Object = MibScalar
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 15),
    _GroupName_Type()
)
groupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    groupName.setStatus("current")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibScalar
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 18),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imageVersion.setStatus("current")
_SensorDescr_Type = DisplayString
_SensorDescr_Object = MibScalar
sensorDescr = _SensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 19),
    _SensorDescr_Type()
)
sensorDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sensorDescr.setStatus("current")
_ThresholdDescr_Type = DisplayString
_ThresholdDescr_Object = MibScalar
thresholdDescr = _ThresholdDescr_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 20),
    _ThresholdDescr_Type()
)
thresholdDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdDescr.setStatus("current")
_ThresholdSeverity_Type = DisplayString
_ThresholdSeverity_Object = MibScalar
thresholdSeverity = _ThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 21),
    _ThresholdSeverity_Type()
)
thresholdSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdSeverity.setStatus("current")
_ThresholdEventType_Type = DisplayString
_ThresholdEventType_Object = MibScalar
thresholdEventType = _ThresholdEventType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 22),
    _ThresholdEventType_Type()
)
thresholdEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdEventType.setStatus("current")
_Status_Type = DisplayString
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 23),
    _Status_Type()
)
status.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    status.setStatus("current")
_SlaveIpAddress_Type = IpAddress
_SlaveIpAddress_Object = MibScalar
slaveIpAddress = _SlaveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 24),
    _SlaveIpAddress_Type()
)
slaveIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaveIpAddress.setStatus("current")
_InputCurrentRating_Type = MilliAmps
_InputCurrentRating_Object = MibScalar
inputCurrentRating = _InputCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 25),
    _InputCurrentRating_Type()
)
inputCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentRating.setStatus("current")
_RatedVoltage_Type = DisplayString
_RatedVoltage_Object = MibScalar
ratedVoltage = _RatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 26),
    _RatedVoltage_Type()
)
ratedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratedVoltage.setStatus("current")
_RatedPower_Type = DisplayString
_RatedPower_Object = MibScalar
ratedPower = _RatedPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 27),
    _RatedPower_Type()
)
ratedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ratedPower.setStatus("current")
_OutletSwitching_Type = DisplayString
_OutletSwitching_Object = MibScalar
outletSwitching = _OutletSwitching_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 28),
    _OutletSwitching_Type()
)
outletSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSwitching.setStatus("current")
_DataLogging_Type = DisplayString
_DataLogging_Object = MibScalar
dataLogging = _DataLogging_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 29),
    _DataLogging_Type()
)
dataLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataLogging.setStatus("current")
_DataLoggingInterval_Type = Integer32
_DataLoggingInterval_Object = MibScalar
dataLoggingInterval = _DataLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 30),
    _DataLoggingInterval_Type()
)
dataLoggingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataLoggingInterval.setStatus("deprecated")
_DataCollectionInterval_Type = Integer32
_DataCollectionInterval_Object = MibScalar
dataCollectionInterval = _DataCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 31),
    _DataCollectionInterval_Type()
)
dataCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCollectionInterval.setStatus("current")
_OutletEnergySupport_Type = DisplayString
_OutletEnergySupport_Object = MibScalar
outletEnergySupport = _OutletEnergySupport_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 32),
    _OutletEnergySupport_Type()
)
outletEnergySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletEnergySupport.setStatus("current")
_CurrentUnbalanceSupport_Type = DisplayString
_CurrentUnbalanceSupport_Object = MibScalar
currentUnbalanceSupport = _CurrentUnbalanceSupport_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 33),
    _CurrentUnbalanceSupport_Type()
)
currentUnbalanceSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentUnbalanceSupport.setStatus("current")
_ExternalSensorsZCoordinateUnits_Type = DisplayString
_ExternalSensorsZCoordinateUnits_Object = MibScalar
externalSensorsZCoordinateUnits = _ExternalSensorsZCoordinateUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 34),
    _ExternalSensorsZCoordinateUnits_Type()
)
externalSensorsZCoordinateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorsZCoordinateUnits.setStatus("current")
_InlineMeter_Type = DisplayString
_InlineMeter_Object = MibScalar
inlineMeter = _InlineMeter_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 35),
    _InlineMeter_Type()
)
inlineMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlineMeter.setStatus("current")
_OldSensorState_Type = StateOfSensorEnumeration
_OldSensorState_Object = MibScalar
oldSensorState = _OldSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 36),
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
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 37),
    _ExternalSensorNumber_Type()
)
externalSensorNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalSensorNumber.setStatus("current")
_SensorIdentificationString_Type = DisplayString
_SensorIdentificationString_Object = MibScalar
sensorIdentificationString = _SensorIdentificationString_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 38),
    _SensorIdentificationString_Type()
)
sensorIdentificationString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sensorIdentificationString.setStatus("current")


class _LastUpgradeStatus_Type(Bits):
    """Custom type lastUpgradeStatus based on Bits"""
    namedValues = NamedValues(
        *(("mainController", 0),
          ("psoc1", 1),
          ("psoc2", 2),
          ("psoc3", 3),
          ("psoc4", 4),
          ("psoc5", 5),
          ("psoc6", 6))
    )

_LastUpgradeStatus_Type.__name__ = "Bits"
_LastUpgradeStatus_Object = MibScalar
lastUpgradeStatus = _LastUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 39),
    _LastUpgradeStatus_Type()
)
lastUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastUpgradeStatus.setStatus("current")
_LastUpgradeTimestamp_Type = DateAndTime
_LastUpgradeTimestamp_Object = MibScalar
lastUpgradeTimestamp = _LastUpgradeTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 40),
    _LastUpgradeTimestamp_Type()
)
lastUpgradeTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastUpgradeTimestamp.setStatus("current")
_LastUpgradeErrorDescription_Type = DisplayString
_LastUpgradeErrorDescription_Object = MibScalar
lastUpgradeErrorDescription = _LastUpgradeErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 41),
    _LastUpgradeErrorDescription_Type()
)
lastUpgradeErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastUpgradeErrorDescription.setStatus("current")
_PowerCIMStatus_Type = PowerCIMStatusEnumeration
_PowerCIMStatus_Object = MibScalar
powerCIMStatus = _PowerCIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 42),
    _PowerCIMStatus_Type()
)
powerCIMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerCIMStatus.setStatus("current")
_MeasurementsPerLogEntry_Type = Integer32
_MeasurementsPerLogEntry_Object = MibScalar
measurementsPerLogEntry = _MeasurementsPerLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 43),
    _MeasurementsPerLogEntry_Type()
)
measurementsPerLogEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measurementsPerLogEntry.setStatus("current")
_PsocNumber_Type = Integer32
_PsocNumber_Object = MibScalar
psocNumber = _PsocNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 44),
    _PsocNumber_Type()
)
psocNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    psocNumber.setStatus("current")


class _Altitude_Type(Integer32):
    """Custom type altitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_Altitude_Type.__name__ = "Integer32"
_Altitude_Object = MibScalar
altitude = _Altitude_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 45),
    _Altitude_Type()
)
altitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altitude.setStatus("current")
_ConfigureAlerts_Type = DisplayString
_ConfigureAlerts_Object = MibScalar
configureAlerts = _ConfigureAlerts_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 46),
    _ConfigureAlerts_Type()
)
configureAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configureAlerts.setStatus("current")
_FipsMode_Type = EnabledDisabledEnumeration
_FipsMode_Object = MibScalar
fipsMode = _FipsMode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 47),
    _FipsMode_Type()
)
fipsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fipsMode.setStatus("current")
_SynchronizeWithNTPServer_Type = EnabledDisabledEnumeration
_SynchronizeWithNTPServer_Object = MibScalar
synchronizeWithNTPServer = _SynchronizeWithNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 48),
    _SynchronizeWithNTPServer_Type()
)
synchronizeWithNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synchronizeWithNTPServer.setStatus("current")
_UseDHCPProvidedNTPServer_Type = EnabledDisabledEnumeration
_UseDHCPProvidedNTPServer_Object = MibScalar
useDHCPProvidedNTPServer = _UseDHCPProvidedNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 49),
    _UseDHCPProvidedNTPServer_Type()
)
useDHCPProvidedNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDHCPProvidedNTPServer.setStatus("current")


class _PrimaryNTPServerAddressType_Type(InetAddressType):
    """Custom type primaryNTPServerAddressType based on InetAddressType"""


_PrimaryNTPServerAddressType_Object = MibScalar
primaryNTPServerAddressType = _PrimaryNTPServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 50),
    _PrimaryNTPServerAddressType_Type()
)
primaryNTPServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryNTPServerAddressType.setStatus("current")
_PrimaryNTPServerAddress_Type = InetAddress
_PrimaryNTPServerAddress_Object = MibScalar
primaryNTPServerAddress = _PrimaryNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 51),
    _PrimaryNTPServerAddress_Type()
)
primaryNTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryNTPServerAddress.setStatus("current")
_SecondaryNTPServerAddressType_Type = InetAddressType
_SecondaryNTPServerAddressType_Object = MibScalar
secondaryNTPServerAddressType = _SecondaryNTPServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 52),
    _SecondaryNTPServerAddressType_Type()
)
secondaryNTPServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryNTPServerAddressType.setStatus("current")
_SecondaryNTPServerAddress_Type = InetAddress
_SecondaryNTPServerAddress_Object = MibScalar
secondaryNTPServerAddress = _SecondaryNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 53),
    _SecondaryNTPServerAddress_Type()
)
secondaryNTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryNTPServerAddress.setStatus("current")
_DaylightSavingsTime_Type = EnabledDisabledEnumeration
_DaylightSavingsTime_Object = MibScalar
daylightSavingsTime = _DaylightSavingsTime_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 55),
    _DaylightSavingsTime_Type()
)
daylightSavingsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSavingsTime.setStatus("current")
_ThresholdValue_Type = DisplayString
_ThresholdValue_Object = MibScalar
thresholdValue = _ThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 56),
    _ThresholdValue_Type()
)
thresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    thresholdValue.setStatus("current")
_SensorValue_Type = DisplayString
_SensorValue_Object = MibScalar
sensorValue = _SensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 57),
    _SensorValue_Type()
)
sensorValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sensorValue.setStatus("current")
_IpmiOverLAN_Type = EnabledDisabledEnumeration
_IpmiOverLAN_Object = MibScalar
ipmiOverLAN = _IpmiOverLAN_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 1, 58),
    _IpmiOverLAN_Type()
)
ipmiOverLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmiOverLAN.setStatus("current")
_Outlets_ObjectIdentity = ObjectIdentity
outlets = _Outlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2)
)
_OutletCount_Type = Integer32
_OutletCount_Object = MibScalar
outletCount = _OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 1),
    _OutletCount_Type()
)
outletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCount.setStatus("current")
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1)
)
outletEntry.setIndexNames(
    (0, "PDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")
_OutletLabel_Type = DisplayString
_OutletLabel_Object = MibTableColumn
outletLabel = _OutletLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 2),
    _OutletLabel_Type()
)
outletLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletLabel.setStatus("current")


class _OutletOperationalState_Type(Integer32):
    """Custom type outletOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cycling", 2),
          ("error", -1),
          ("off", 0),
          ("on", 1))
    )


_OutletOperationalState_Type.__name__ = "Integer32"
_OutletOperationalState_Object = MibTableColumn
outletOperationalState = _OutletOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 3),
    _OutletOperationalState_Type()
)
outletOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletOperationalState.setStatus("current")
_OutletCurrent_Type = MilliAmps
_OutletCurrent_Object = MibTableColumn
outletCurrent = _OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 4),
    _OutletCurrent_Type()
)
outletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrent.setStatus("current")
_OutletMaxCurrent_Type = MilliAmps
_OutletMaxCurrent_Object = MibTableColumn
outletMaxCurrent = _OutletMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 5),
    _OutletMaxCurrent_Type()
)
outletMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletMaxCurrent.setStatus("current")
_OutletVoltage_Type = MilliVolts
_OutletVoltage_Object = MibTableColumn
outletVoltage = _OutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 6),
    _OutletVoltage_Type()
)
outletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVoltage.setStatus("current")
_OutletActivePower_Type = Watts
_OutletActivePower_Object = MibTableColumn
outletActivePower = _OutletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 7),
    _OutletActivePower_Type()
)
outletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletActivePower.setStatus("current")
_OutletApparentPower_Type = VoltAmps
_OutletApparentPower_Object = MibTableColumn
outletApparentPower = _OutletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 8),
    _OutletApparentPower_Type()
)
outletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletApparentPower.setStatus("current")
_OutletPowerFactor_Type = PowerFactorPercentage
_OutletPowerFactor_Object = MibTableColumn
outletPowerFactor = _OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 9),
    _OutletPowerFactor_Type()
)
outletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPowerFactor.setStatus("current")
_OutletCurrentUpperWarning_Type = MilliAmps
_OutletCurrentUpperWarning_Object = MibTableColumn
outletCurrentUpperWarning = _OutletCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 20),
    _OutletCurrentUpperWarning_Type()
)
outletCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentUpperWarning.setStatus("current")
_OutletCurrentUpperCritical_Type = MilliAmps
_OutletCurrentUpperCritical_Object = MibTableColumn
outletCurrentUpperCritical = _OutletCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 21),
    _OutletCurrentUpperCritical_Type()
)
outletCurrentUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentUpperCritical.setStatus("current")
_OutletCurrentLowerWarning_Type = MilliAmps
_OutletCurrentLowerWarning_Object = MibTableColumn
outletCurrentLowerWarning = _OutletCurrentLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 22),
    _OutletCurrentLowerWarning_Type()
)
outletCurrentLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentLowerWarning.setStatus("current")
_OutletCurrentLowerCritical_Type = MilliAmps
_OutletCurrentLowerCritical_Object = MibTableColumn
outletCurrentLowerCritical = _OutletCurrentLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 23),
    _OutletCurrentLowerCritical_Type()
)
outletCurrentLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentLowerCritical.setStatus("current")
_OutletCurrentHysteresis_Type = Unsigned32
_OutletCurrentHysteresis_Object = MibTableColumn
outletCurrentHysteresis = _OutletCurrentHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 24),
    _OutletCurrentHysteresis_Type()
)
outletCurrentHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentHysteresis.setStatus("current")
_OutletCurrentRating_Type = MilliAmps
_OutletCurrentRating_Object = MibTableColumn
outletCurrentRating = _OutletCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 30),
    _OutletCurrentRating_Type()
)
outletCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrentRating.setStatus("current")
_OutletWattHours_Type = WattHours
_OutletWattHours_Object = MibTableColumn
outletWattHours = _OutletWattHours_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 2, 2, 1, 31),
    _OutletWattHours_Type()
)
outletWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletWattHours.setStatus("current")
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3)
)
_UnitReadings_ObjectIdentity = ObjectIdentity
unitReadings = _UnitReadings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1)
)
_UnitCurrent_Type = MilliAmps
_UnitCurrent_Object = MibScalar
unitCurrent = _UnitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 1),
    _UnitCurrent_Type()
)
unitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCurrent.setStatus("deprecated")
_UnitVoltage_Type = MilliVolts
_UnitVoltage_Object = MibScalar
unitVoltage = _UnitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 2),
    _UnitVoltage_Type()
)
unitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitVoltage.setStatus("deprecated")
_UnitActivePower_Type = Watts
_UnitActivePower_Object = MibScalar
unitActivePower = _UnitActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 3),
    _UnitActivePower_Type()
)
unitActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitActivePower.setStatus("deprecated")
_UnitApparentPower_Type = VoltAmps
_UnitApparentPower_Object = MibScalar
unitApparentPower = _UnitApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 4),
    _UnitApparentPower_Type()
)
unitApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitApparentPower.setStatus("deprecated")
_UnitCpuTemp_Type = TenthDegreesCelsius
_UnitCpuTemp_Object = MibScalar
unitCpuTemp = _UnitCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 5),
    _UnitCpuTemp_Type()
)
unitCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCpuTemp.setStatus("current")
_UnitVoltageLowerWarning_Type = MilliVolts
_UnitVoltageLowerWarning_Object = MibScalar
unitVoltageLowerWarning = _UnitVoltageLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 60),
    _UnitVoltageLowerWarning_Type()
)
unitVoltageLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageLowerWarning.setStatus("deprecated")
_UnitVoltageLowerCritical_Type = MilliVolts
_UnitVoltageLowerCritical_Object = MibScalar
unitVoltageLowerCritical = _UnitVoltageLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 61),
    _UnitVoltageLowerCritical_Type()
)
unitVoltageLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageLowerCritical.setStatus("deprecated")
_UnitVoltageUpperWarning_Type = MilliVolts
_UnitVoltageUpperWarning_Object = MibScalar
unitVoltageUpperWarning = _UnitVoltageUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 62),
    _UnitVoltageUpperWarning_Type()
)
unitVoltageUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageUpperWarning.setStatus("deprecated")
_UnitVoltageUpperCritical_Type = MilliVolts
_UnitVoltageUpperCritical_Object = MibScalar
unitVoltageUpperCritical = _UnitVoltageUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 63),
    _UnitVoltageUpperCritical_Type()
)
unitVoltageUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitVoltageUpperCritical.setStatus("deprecated")
_UnitCurrentUpperWarning_Type = MilliAmps
_UnitCurrentUpperWarning_Object = MibScalar
unitCurrentUpperWarning = _UnitCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 70),
    _UnitCurrentUpperWarning_Type()
)
unitCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitCurrentUpperWarning.setStatus("deprecated")
_UnitCurrentUpperCritical_Type = MilliAmps
_UnitCurrentUpperCritical_Object = MibScalar
unitCurrentUpperCritical = _UnitCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 71),
    _UnitCurrentUpperCritical_Type()
)
unitCurrentUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitCurrentUpperCritical.setStatus("deprecated")
_UnitTempLowerWarning_Type = DegreesCelsius
_UnitTempLowerWarning_Object = MibScalar
unitTempLowerWarning = _UnitTempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 80),
    _UnitTempLowerWarning_Type()
)
unitTempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempLowerWarning.setStatus("current")
_UnitTempLowerCritical_Type = DegreesCelsius
_UnitTempLowerCritical_Object = MibScalar
unitTempLowerCritical = _UnitTempLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 81),
    _UnitTempLowerCritical_Type()
)
unitTempLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempLowerCritical.setStatus("current")
_UnitTempUpperWarning_Type = DegreesCelsius
_UnitTempUpperWarning_Object = MibScalar
unitTempUpperWarning = _UnitTempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 82),
    _UnitTempUpperWarning_Type()
)
unitTempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempUpperWarning.setStatus("current")
_UnitTempUpperCritical_Type = DegreesCelsius
_UnitTempUpperCritical_Object = MibScalar
unitTempUpperCritical = _UnitTempUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 83),
    _UnitTempUpperCritical_Type()
)
unitTempUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempUpperCritical.setStatus("current")
_CurrentUnbalance_Type = DisplayString
_CurrentUnbalance_Object = MibScalar
currentUnbalance = _CurrentUnbalance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 84),
    _CurrentUnbalance_Type()
)
currentUnbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUnbalance.setStatus("current")
_CurrentUnbalanceUpperWarning_Type = Percentage
_CurrentUnbalanceUpperWarning_Object = MibScalar
currentUnbalanceUpperWarning = _CurrentUnbalanceUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 85),
    _CurrentUnbalanceUpperWarning_Type()
)
currentUnbalanceUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentUnbalanceUpperWarning.setStatus("current")
_CurrentUnbalanceUpperCritical_Type = Percentage
_CurrentUnbalanceUpperCritical_Object = MibScalar
currentUnbalanceUpperCritical = _CurrentUnbalanceUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 86),
    _CurrentUnbalanceUpperCritical_Type()
)
currentUnbalanceUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentUnbalanceUpperCritical.setStatus("current")
_UnitOrLineVoltageLowerWarning_Type = MilliVolts
_UnitOrLineVoltageLowerWarning_Object = MibScalar
unitOrLineVoltageLowerWarning = _UnitOrLineVoltageLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 90),
    _UnitOrLineVoltageLowerWarning_Type()
)
unitOrLineVoltageLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineVoltageLowerWarning.setStatus("current")
_UnitOrLineVoltageLowerCritical_Type = MilliVolts
_UnitOrLineVoltageLowerCritical_Object = MibScalar
unitOrLineVoltageLowerCritical = _UnitOrLineVoltageLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 91),
    _UnitOrLineVoltageLowerCritical_Type()
)
unitOrLineVoltageLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineVoltageLowerCritical.setStatus("current")
_UnitOrLineVoltageUpperWarning_Type = MilliVolts
_UnitOrLineVoltageUpperWarning_Object = MibScalar
unitOrLineVoltageUpperWarning = _UnitOrLineVoltageUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 92),
    _UnitOrLineVoltageUpperWarning_Type()
)
unitOrLineVoltageUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineVoltageUpperWarning.setStatus("current")
_UnitOrLineVoltageUpperCritical_Type = MilliVolts
_UnitOrLineVoltageUpperCritical_Object = MibScalar
unitOrLineVoltageUpperCritical = _UnitOrLineVoltageUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 93),
    _UnitOrLineVoltageUpperCritical_Type()
)
unitOrLineVoltageUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineVoltageUpperCritical.setStatus("current")
_UnitOrLineCurrentUpperWarning_Type = MilliAmps
_UnitOrLineCurrentUpperWarning_Object = MibScalar
unitOrLineCurrentUpperWarning = _UnitOrLineCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 94),
    _UnitOrLineCurrentUpperWarning_Type()
)
unitOrLineCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineCurrentUpperWarning.setStatus("current")
_UnitOrLineCurrentUpperCritical_Type = MilliAmps
_UnitOrLineCurrentUpperCritical_Object = MibScalar
unitOrLineCurrentUpperCritical = _UnitOrLineCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 95),
    _UnitOrLineCurrentUpperCritical_Type()
)
unitOrLineCurrentUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineCurrentUpperCritical.setStatus("current")
_NeutralCurrentUpperWarning_Type = MilliAmps
_NeutralCurrentUpperWarning_Object = MibScalar
neutralCurrentUpperWarning = _NeutralCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 96),
    _NeutralCurrentUpperWarning_Type()
)
neutralCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neutralCurrentUpperWarning.setStatus("current")
_NeutralCurrentUpperCritical_Type = MilliAmps
_NeutralCurrentUpperCritical_Object = MibScalar
neutralCurrentUpperCritical = _NeutralCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 97),
    _NeutralCurrentUpperCritical_Type()
)
neutralCurrentUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neutralCurrentUpperCritical.setStatus("current")
_UnitOrLineCurrentHysteresis_Type = Unsigned32
_UnitOrLineCurrentHysteresis_Object = MibScalar
unitOrLineCurrentHysteresis = _UnitOrLineCurrentHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 98),
    _UnitOrLineCurrentHysteresis_Type()
)
unitOrLineCurrentHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineCurrentHysteresis.setStatus("current")
_UnitOrLineVoltageHysteresis_Type = Unsigned32
_UnitOrLineVoltageHysteresis_Object = MibScalar
unitOrLineVoltageHysteresis = _UnitOrLineVoltageHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 99),
    _UnitOrLineVoltageHysteresis_Type()
)
unitOrLineVoltageHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOrLineVoltageHysteresis.setStatus("current")
_UnitTempHysteresis_Type = Unsigned32
_UnitTempHysteresis_Object = MibScalar
unitTempHysteresis = _UnitTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 100),
    _UnitTempHysteresis_Type()
)
unitTempHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTempHysteresis.setStatus("current")
_CurrentUnbalanceHysteresis_Type = Unsigned32
_CurrentUnbalanceHysteresis_Object = MibScalar
currentUnbalanceHysteresis = _CurrentUnbalanceHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 3, 1, 101),
    _CurrentUnbalanceHysteresis_Type()
)
currentUnbalanceHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentUnbalanceHysteresis.setStatus("current")
_LineCurrents_ObjectIdentity = ObjectIdentity
lineCurrents = _LineCurrents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 4)
)
_LineCurrentCount_Type = Integer32
_LineCurrentCount_Object = MibScalar
lineCurrentCount = _LineCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 4, 1),
    _LineCurrentCount_Type()
)
lineCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCurrentCount.setStatus("deprecated")
_LineCurrentTable_Object = MibTable
lineCurrentTable = _LineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    lineCurrentTable.setStatus("deprecated")
_LineCurrentEntry_Object = MibTableRow
lineCurrentEntry = _LineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 4, 2, 1)
)
lineCurrentEntry.setIndexNames(
    (0, "PDU-MIB", "lineCurrentIndex"),
)
if mibBuilder.loadTexts:
    lineCurrentEntry.setStatus("deprecated")


class _LineCurrentIndex_Type(Integer32):
    """Custom type lineCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LineCurrentIndex_Type.__name__ = "Integer32"
_LineCurrentIndex_Object = MibTableColumn
lineCurrentIndex = _LineCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 4, 2, 1, 1),
    _LineCurrentIndex_Type()
)
lineCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineCurrentIndex.setStatus("deprecated")
_LineCurrentLabel_Type = DisplayString
_LineCurrentLabel_Object = MibTableColumn
lineCurrentLabel = _LineCurrentLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 4, 2, 1, 2),
    _LineCurrentLabel_Type()
)
lineCurrentLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCurrentLabel.setStatus("deprecated")
_LineCurrent_Type = MilliAmps
_LineCurrent_Object = MibTableColumn
lineCurrent = _LineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 4, 2, 1, 3),
    _LineCurrent_Type()
)
lineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCurrent.setStatus("deprecated")
_CircuitBreaker_ObjectIdentity = ObjectIdentity
circuitBreaker = _CircuitBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5)
)
_CircuitBreakerCount_Type = Integer32
_CircuitBreakerCount_Object = MibScalar
circuitBreakerCount = _CircuitBreakerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 1),
    _CircuitBreakerCount_Type()
)
circuitBreakerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitBreakerCount.setStatus("current")
_CircuitBreakerTable_Object = MibTable
circuitBreakerTable = _CircuitBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    circuitBreakerTable.setStatus("current")
_CircuitBreakerEntry_Object = MibTableRow
circuitBreakerEntry = _CircuitBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1)
)
circuitBreakerEntry.setIndexNames(
    (0, "PDU-MIB", "circuitBreakerIndex"),
)
if mibBuilder.loadTexts:
    circuitBreakerEntry.setStatus("current")


class _CircuitBreakerIndex_Type(Integer32):
    """Custom type circuitBreakerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CircuitBreakerIndex_Type.__name__ = "Integer32"
_CircuitBreakerIndex_Object = MibTableColumn
circuitBreakerIndex = _CircuitBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 1),
    _CircuitBreakerIndex_Type()
)
circuitBreakerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    circuitBreakerIndex.setStatus("current")
_CircuitBreakerLabel_Type = DisplayString
_CircuitBreakerLabel_Object = MibTableColumn
circuitBreakerLabel = _CircuitBreakerLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 2),
    _CircuitBreakerLabel_Type()
)
circuitBreakerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitBreakerLabel.setStatus("current")


class _CircuitBreakerState_Type(Integer32):
    """Custom type circuitBreakerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("tripped", 1))
    )


_CircuitBreakerState_Type.__name__ = "Integer32"
_CircuitBreakerState_Object = MibTableColumn
circuitBreakerState = _CircuitBreakerState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 3),
    _CircuitBreakerState_Type()
)
circuitBreakerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitBreakerState.setStatus("current")
_CircuitBreakerCurrentRating_Type = MilliAmps
_CircuitBreakerCurrentRating_Object = MibTableColumn
circuitBreakerCurrentRating = _CircuitBreakerCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 4),
    _CircuitBreakerCurrentRating_Type()
)
circuitBreakerCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitBreakerCurrentRating.setStatus("current")
_CircuitBreakerCurrent_Type = MilliAmps
_CircuitBreakerCurrent_Object = MibTableColumn
circuitBreakerCurrent = _CircuitBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 5),
    _CircuitBreakerCurrent_Type()
)
circuitBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitBreakerCurrent.setStatus("current")
_CircuitBreakerCurrentUpperWarning_Type = MilliAmps
_CircuitBreakerCurrentUpperWarning_Object = MibTableColumn
circuitBreakerCurrentUpperWarning = _CircuitBreakerCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 7),
    _CircuitBreakerCurrentUpperWarning_Type()
)
circuitBreakerCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBreakerCurrentUpperWarning.setStatus("current")
_CircuitBreakerCurrentUpperCritical_Type = MilliAmps
_CircuitBreakerCurrentUpperCritical_Object = MibTableColumn
circuitBreakerCurrentUpperCritical = _CircuitBreakerCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 9),
    _CircuitBreakerCurrentUpperCritical_Type()
)
circuitBreakerCurrentUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBreakerCurrentUpperCritical.setStatus("current")
_CircuitBreakerCurrentHysteresis_Type = Unsigned32
_CircuitBreakerCurrentHysteresis_Object = MibTableColumn
circuitBreakerCurrentHysteresis = _CircuitBreakerCurrentHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 5, 2, 1, 10),
    _CircuitBreakerCurrentHysteresis_Type()
)
circuitBreakerCurrentHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBreakerCurrentHysteresis.setStatus("current")
_LineVoltages_ObjectIdentity = ObjectIdentity
lineVoltages = _LineVoltages_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 6)
)
_LineVoltageCount_Type = Integer32
_LineVoltageCount_Object = MibScalar
lineVoltageCount = _LineVoltageCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 6, 1),
    _LineVoltageCount_Type()
)
lineVoltageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineVoltageCount.setStatus("deprecated")
_LineVoltageTable_Object = MibTable
lineVoltageTable = _LineVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    lineVoltageTable.setStatus("deprecated")
_LineVoltageEntry_Object = MibTableRow
lineVoltageEntry = _LineVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 6, 2, 1)
)
lineVoltageEntry.setIndexNames(
    (0, "PDU-MIB", "lineVoltageIndex"),
)
if mibBuilder.loadTexts:
    lineVoltageEntry.setStatus("deprecated")


class _LineVoltageIndex_Type(Integer32):
    """Custom type lineVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LineVoltageIndex_Type.__name__ = "Integer32"
_LineVoltageIndex_Object = MibTableColumn
lineVoltageIndex = _LineVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 6, 2, 1, 1),
    _LineVoltageIndex_Type()
)
lineVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lineVoltageIndex.setStatus("deprecated")
_LineVoltageLabel_Type = DisplayString
_LineVoltageLabel_Object = MibTableColumn
lineVoltageLabel = _LineVoltageLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 6, 2, 1, 2),
    _LineVoltageLabel_Type()
)
lineVoltageLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineVoltageLabel.setStatus("deprecated")
_LineVoltage_Type = MilliVolts
_LineVoltage_Object = MibTableColumn
lineVoltage = _LineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 6, 2, 1, 3),
    _LineVoltage_Type()
)
lineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineVoltage.setStatus("deprecated")
_DataLog_ObjectIdentity = ObjectIdentity
dataLog = _DataLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7)
)
_DataLogCount_Type = Integer32
_DataLogCount_Object = MibScalar
dataLogCount = _DataLogCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 1),
    _DataLogCount_Type()
)
dataLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogCount.setStatus("current")


class _DataLogLatestIndex_Type(Integer32):
    """Custom type dataLogLatestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogLatestIndex_Type.__name__ = "Integer32"
_DataLogLatestIndex_Object = MibScalar
dataLogLatestIndex = _DataLogLatestIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 2),
    _DataLogLatestIndex_Type()
)
dataLogLatestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogLatestIndex.setStatus("current")
_DataLogTable_Object = MibTable
dataLogTable = _DataLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3)
)
if mibBuilder.loadTexts:
    dataLogTable.setStatus("current")
_DataLogEntry_Object = MibTableRow
dataLogEntry = _DataLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1)
)
dataLogEntry.setIndexNames(
    (0, "PDU-MIB", "dataLogIndex"),
)
if mibBuilder.loadTexts:
    dataLogEntry.setStatus("current")


class _DataLogIndex_Type(Integer32):
    """Custom type dataLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogIndex_Type.__name__ = "Integer32"
_DataLogIndex_Object = MibTableColumn
dataLogIndex = _DataLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 1),
    _DataLogIndex_Type()
)
dataLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataLogIndex.setStatus("current")
_DataLogTimeStamp_Type = Unsigned32
_DataLogTimeStamp_Object = MibTableColumn
dataLogTimeStamp = _DataLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 2),
    _DataLogTimeStamp_Type()
)
dataLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogTimeStamp.setStatus("current")
_DataLogActivePower_Type = Watts
_DataLogActivePower_Object = MibTableColumn
dataLogActivePower = _DataLogActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 3),
    _DataLogActivePower_Type()
)
dataLogActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogActivePower.setStatus("deprecated")
_DataLogApparentPower_Type = VoltAmps
_DataLogApparentPower_Object = MibTableColumn
dataLogApparentPower = _DataLogApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 4),
    _DataLogApparentPower_Type()
)
dataLogApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogApparentPower.setStatus("deprecated")
_DataLogAvgActivePower_Type = Watts
_DataLogAvgActivePower_Object = MibTableColumn
dataLogAvgActivePower = _DataLogAvgActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 5),
    _DataLogAvgActivePower_Type()
)
dataLogAvgActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgActivePower.setStatus("current")
_DataLogMaxActivePower_Type = Watts
_DataLogMaxActivePower_Object = MibTableColumn
dataLogMaxActivePower = _DataLogMaxActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 6),
    _DataLogMaxActivePower_Type()
)
dataLogMaxActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxActivePower.setStatus("current")
_DataLogMinActivePower_Type = Watts
_DataLogMinActivePower_Object = MibTableColumn
dataLogMinActivePower = _DataLogMinActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 7),
    _DataLogMinActivePower_Type()
)
dataLogMinActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinActivePower.setStatus("current")
_DataLogAvgApparentPower_Type = VoltAmps
_DataLogAvgApparentPower_Object = MibTableColumn
dataLogAvgApparentPower = _DataLogAvgApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 8),
    _DataLogAvgApparentPower_Type()
)
dataLogAvgApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgApparentPower.setStatus("current")
_DataLogMaxApparentPower_Type = VoltAmps
_DataLogMaxApparentPower_Object = MibTableColumn
dataLogMaxApparentPower = _DataLogMaxApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 9),
    _DataLogMaxApparentPower_Type()
)
dataLogMaxApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxApparentPower.setStatus("current")
_DataLogMinApparentPower_Type = VoltAmps
_DataLogMinApparentPower_Object = MibTableColumn
dataLogMinApparentPower = _DataLogMinApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 7, 3, 1, 10),
    _DataLogMinApparentPower_Type()
)
dataLogMinApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinApparentPower.setStatus("current")
_DataLogOutlet_ObjectIdentity = ObjectIdentity
dataLogOutlet = _DataLogOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10)
)
_DataLogOutletTable_Object = MibTable
dataLogOutletTable = _DataLogOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    dataLogOutletTable.setStatus("current")
_DataLogOutletEntry_Object = MibTableRow
dataLogOutletEntry = _DataLogOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1)
)
dataLogOutletEntry.setIndexNames(
    (0, "PDU-MIB", "dataLogIndex"),
    (0, "PDU-MIB", "dataLogOutletIndex"),
)
if mibBuilder.loadTexts:
    dataLogOutletEntry.setStatus("current")


class _DataLogOutletIndex_Type(Integer32):
    """Custom type dataLogOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogOutletIndex_Type.__name__ = "Integer32"
_DataLogOutletIndex_Object = MibTableColumn
dataLogOutletIndex = _DataLogOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 1),
    _DataLogOutletIndex_Type()
)
dataLogOutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataLogOutletIndex.setStatus("current")
_DataLogOutletCurrent_Type = MilliAmps
_DataLogOutletCurrent_Object = MibTableColumn
dataLogOutletCurrent = _DataLogOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 2),
    _DataLogOutletCurrent_Type()
)
dataLogOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogOutletCurrent.setStatus("deprecated")
_DataLogOutletVoltage_Type = MilliVolts
_DataLogOutletVoltage_Object = MibTableColumn
dataLogOutletVoltage = _DataLogOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 3),
    _DataLogOutletVoltage_Type()
)
dataLogOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogOutletVoltage.setStatus("deprecated")
_DataLogOutletPowerFactor_Type = PowerFactorPercentage
_DataLogOutletPowerFactor_Object = MibTableColumn
dataLogOutletPowerFactor = _DataLogOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 4),
    _DataLogOutletPowerFactor_Type()
)
dataLogOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogOutletPowerFactor.setStatus("deprecated")
_DataLogOutletOnTime_Type = Unsigned32
_DataLogOutletOnTime_Object = MibTableColumn
dataLogOutletOnTime = _DataLogOutletOnTime_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 5),
    _DataLogOutletOnTime_Type()
)
dataLogOutletOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogOutletOnTime.setStatus("current")
_DataLogOutletWattHours_Type = WattHours
_DataLogOutletWattHours_Object = MibTableColumn
dataLogOutletWattHours = _DataLogOutletWattHours_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 6),
    _DataLogOutletWattHours_Type()
)
dataLogOutletWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogOutletWattHours.setStatus("deprecated")
_DataLogAvgOutletCurrent_Type = MilliAmps
_DataLogAvgOutletCurrent_Object = MibTableColumn
dataLogAvgOutletCurrent = _DataLogAvgOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 7),
    _DataLogAvgOutletCurrent_Type()
)
dataLogAvgOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgOutletCurrent.setStatus("current")
_DataLogMaxOutletCurrent_Type = MilliAmps
_DataLogMaxOutletCurrent_Object = MibTableColumn
dataLogMaxOutletCurrent = _DataLogMaxOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 8),
    _DataLogMaxOutletCurrent_Type()
)
dataLogMaxOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxOutletCurrent.setStatus("current")
_DataLogMinOutletCurrent_Type = MilliAmps
_DataLogMinOutletCurrent_Object = MibTableColumn
dataLogMinOutletCurrent = _DataLogMinOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 9),
    _DataLogMinOutletCurrent_Type()
)
dataLogMinOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinOutletCurrent.setStatus("current")
_DataLogAvgOutletVoltage_Type = MilliVolts
_DataLogAvgOutletVoltage_Object = MibTableColumn
dataLogAvgOutletVoltage = _DataLogAvgOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 10),
    _DataLogAvgOutletVoltage_Type()
)
dataLogAvgOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgOutletVoltage.setStatus("current")
_DataLogMaxOutletVoltage_Type = MilliVolts
_DataLogMaxOutletVoltage_Object = MibTableColumn
dataLogMaxOutletVoltage = _DataLogMaxOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 11),
    _DataLogMaxOutletVoltage_Type()
)
dataLogMaxOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxOutletVoltage.setStatus("current")
_DataLogMinOutletVoltage_Type = MilliVolts
_DataLogMinOutletVoltage_Object = MibTableColumn
dataLogMinOutletVoltage = _DataLogMinOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 12),
    _DataLogMinOutletVoltage_Type()
)
dataLogMinOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinOutletVoltage.setStatus("current")
_DataLogAvgOutletPowerFactor_Type = PowerFactorPercentage
_DataLogAvgOutletPowerFactor_Object = MibTableColumn
dataLogAvgOutletPowerFactor = _DataLogAvgOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 13),
    _DataLogAvgOutletPowerFactor_Type()
)
dataLogAvgOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgOutletPowerFactor.setStatus("current")
_DataLogMaxOutletPowerFactor_Type = PowerFactorPercentage
_DataLogMaxOutletPowerFactor_Object = MibTableColumn
dataLogMaxOutletPowerFactor = _DataLogMaxOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 14),
    _DataLogMaxOutletPowerFactor_Type()
)
dataLogMaxOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxOutletPowerFactor.setStatus("current")
_DataLogMinOutletPowerFactor_Type = PowerFactorPercentage
_DataLogMinOutletPowerFactor_Object = MibTableColumn
dataLogMinOutletPowerFactor = _DataLogMinOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 15),
    _DataLogMinOutletPowerFactor_Type()
)
dataLogMinOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinOutletPowerFactor.setStatus("current")
_DataLogAvgOutletWattHours_Type = WattHours
_DataLogAvgOutletWattHours_Object = MibTableColumn
dataLogAvgOutletWattHours = _DataLogAvgOutletWattHours_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 16),
    _DataLogAvgOutletWattHours_Type()
)
dataLogAvgOutletWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgOutletWattHours.setStatus("current")
_DataLogMaxOutletWattHours_Type = WattHours
_DataLogMaxOutletWattHours_Object = MibTableColumn
dataLogMaxOutletWattHours = _DataLogMaxOutletWattHours_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 17),
    _DataLogMaxOutletWattHours_Type()
)
dataLogMaxOutletWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxOutletWattHours.setStatus("current")
_DataLogMinOutletWattHours_Type = WattHours
_DataLogMinOutletWattHours_Object = MibTableColumn
dataLogMinOutletWattHours = _DataLogMinOutletWattHours_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 10, 1, 1, 18),
    _DataLogMinOutletWattHours_Type()
)
dataLogMinOutletWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinOutletWattHours.setStatus("current")
_DataLogInlet_ObjectIdentity = ObjectIdentity
dataLogInlet = _DataLogInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12)
)
_DataLogInletTable_Object = MibTable
dataLogInletTable = _DataLogInletTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2)
)
if mibBuilder.loadTexts:
    dataLogInletTable.setStatus("current")
_DataLogInletEntry_Object = MibTableRow
dataLogInletEntry = _DataLogInletEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1)
)
dataLogInletEntry.setIndexNames(
    (0, "PDU-MIB", "dataLogIndex"),
    (0, "PDU-MIB", "dataLogInletIndex"),
)
if mibBuilder.loadTexts:
    dataLogInletEntry.setStatus("current")


class _DataLogInletIndex_Type(Integer32):
    """Custom type dataLogInletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogInletIndex_Type.__name__ = "Integer32"
_DataLogInletIndex_Object = MibTableColumn
dataLogInletIndex = _DataLogInletIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 1),
    _DataLogInletIndex_Type()
)
dataLogInletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataLogInletIndex.setStatus("current")
_DataLogInletCurrentUnbalance_Type = DisplayString
_DataLogInletCurrentUnbalance_Object = MibTableColumn
dataLogInletCurrentUnbalance = _DataLogInletCurrentUnbalance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 10),
    _DataLogInletCurrentUnbalance_Type()
)
dataLogInletCurrentUnbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInletCurrentUnbalance.setStatus("deprecated")
_DataLogInletActivePower_Type = Watts
_DataLogInletActivePower_Object = MibTableColumn
dataLogInletActivePower = _DataLogInletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 11),
    _DataLogInletActivePower_Type()
)
dataLogInletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInletActivePower.setStatus("deprecated")
_DataLogInletApparentPower_Type = VoltAmps
_DataLogInletApparentPower_Object = MibTableColumn
dataLogInletApparentPower = _DataLogInletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 12),
    _DataLogInletApparentPower_Type()
)
dataLogInletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInletApparentPower.setStatus("deprecated")
_DataLogInletActiveEnergy_Type = WattHours
_DataLogInletActiveEnergy_Object = MibTableColumn
dataLogInletActiveEnergy = _DataLogInletActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 13),
    _DataLogInletActiveEnergy_Type()
)
dataLogInletActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInletActiveEnergy.setStatus("deprecated")
_DataLogAvgInletCurrentUnbalance_Type = DisplayString
_DataLogAvgInletCurrentUnbalance_Object = MibTableColumn
dataLogAvgInletCurrentUnbalance = _DataLogAvgInletCurrentUnbalance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 14),
    _DataLogAvgInletCurrentUnbalance_Type()
)
dataLogAvgInletCurrentUnbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletCurrentUnbalance.setStatus("current")
_DataLogMaxInletCurrentUnbalance_Type = DisplayString
_DataLogMaxInletCurrentUnbalance_Object = MibTableColumn
dataLogMaxInletCurrentUnbalance = _DataLogMaxInletCurrentUnbalance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 15),
    _DataLogMaxInletCurrentUnbalance_Type()
)
dataLogMaxInletCurrentUnbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletCurrentUnbalance.setStatus("current")
_DataLogMinInletCurrentUnbalance_Type = DisplayString
_DataLogMinInletCurrentUnbalance_Object = MibTableColumn
dataLogMinInletCurrentUnbalance = _DataLogMinInletCurrentUnbalance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 16),
    _DataLogMinInletCurrentUnbalance_Type()
)
dataLogMinInletCurrentUnbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletCurrentUnbalance.setStatus("current")
_DataLogAvgInletActivePower_Type = Watts
_DataLogAvgInletActivePower_Object = MibTableColumn
dataLogAvgInletActivePower = _DataLogAvgInletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 17),
    _DataLogAvgInletActivePower_Type()
)
dataLogAvgInletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletActivePower.setStatus("current")
_DataLogMaxInletActivePower_Type = Watts
_DataLogMaxInletActivePower_Object = MibTableColumn
dataLogMaxInletActivePower = _DataLogMaxInletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 18),
    _DataLogMaxInletActivePower_Type()
)
dataLogMaxInletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletActivePower.setStatus("current")
_DataLogMinInletActivePower_Type = Watts
_DataLogMinInletActivePower_Object = MibTableColumn
dataLogMinInletActivePower = _DataLogMinInletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 19),
    _DataLogMinInletActivePower_Type()
)
dataLogMinInletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletActivePower.setStatus("current")
_DataLogAvgInletApparentPower_Type = VoltAmps
_DataLogAvgInletApparentPower_Object = MibTableColumn
dataLogAvgInletApparentPower = _DataLogAvgInletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 20),
    _DataLogAvgInletApparentPower_Type()
)
dataLogAvgInletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletApparentPower.setStatus("current")
_DataLogMaxInletApparentPower_Type = VoltAmps
_DataLogMaxInletApparentPower_Object = MibTableColumn
dataLogMaxInletApparentPower = _DataLogMaxInletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 21),
    _DataLogMaxInletApparentPower_Type()
)
dataLogMaxInletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletApparentPower.setStatus("current")
_DataLogMinInletApparentPower_Type = VoltAmps
_DataLogMinInletApparentPower_Object = MibTableColumn
dataLogMinInletApparentPower = _DataLogMinInletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 22),
    _DataLogMinInletApparentPower_Type()
)
dataLogMinInletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletApparentPower.setStatus("current")
_DataLogAvgInletActiveEnergy_Type = WattHours
_DataLogAvgInletActiveEnergy_Object = MibTableColumn
dataLogAvgInletActiveEnergy = _DataLogAvgInletActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 23),
    _DataLogAvgInletActiveEnergy_Type()
)
dataLogAvgInletActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletActiveEnergy.setStatus("current")
_DataLogMaxInletActiveEnergy_Type = WattHours
_DataLogMaxInletActiveEnergy_Object = MibTableColumn
dataLogMaxInletActiveEnergy = _DataLogMaxInletActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 24),
    _DataLogMaxInletActiveEnergy_Type()
)
dataLogMaxInletActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletActiveEnergy.setStatus("current")
_DataLogMinInletActiveEnergy_Type = WattHours
_DataLogMinInletActiveEnergy_Object = MibTableColumn
dataLogMinInletActiveEnergy = _DataLogMinInletActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 12, 2, 1, 25),
    _DataLogMinInletActiveEnergy_Type()
)
dataLogMinInletActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletActiveEnergy.setStatus("current")
_DataLogInletPole_ObjectIdentity = ObjectIdentity
dataLogInletPole = _DataLogInletPole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13)
)
_DataLogInletPoleTable_Object = MibTable
dataLogInletPoleTable = _DataLogInletPoleTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    dataLogInletPoleTable.setStatus("current")
_DataLogInletPoleEntry_Object = MibTableRow
dataLogInletPoleEntry = _DataLogInletPoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1)
)
dataLogInletPoleEntry.setIndexNames(
    (0, "PDU-MIB", "dataLogIndex"),
    (0, "PDU-MIB", "dataLogInletIndex"),
    (0, "PDU-MIB", "dataLogInletPoleIndex"),
)
if mibBuilder.loadTexts:
    dataLogInletPoleEntry.setStatus("current")


class _DataLogInletPoleIndex_Type(Integer32):
    """Custom type dataLogInletPoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogInletPoleIndex_Type.__name__ = "Integer32"
_DataLogInletPoleIndex_Object = MibTableColumn
dataLogInletPoleIndex = _DataLogInletPoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 1),
    _DataLogInletPoleIndex_Type()
)
dataLogInletPoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataLogInletPoleIndex.setStatus("current")
_DataLogInletPoleCurrent_Type = MilliAmps
_DataLogInletPoleCurrent_Object = MibTableColumn
dataLogInletPoleCurrent = _DataLogInletPoleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 2),
    _DataLogInletPoleCurrent_Type()
)
dataLogInletPoleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInletPoleCurrent.setStatus("deprecated")
_DataLogInletPoleVoltage_Type = MilliVolts
_DataLogInletPoleVoltage_Object = MibTableColumn
dataLogInletPoleVoltage = _DataLogInletPoleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 3),
    _DataLogInletPoleVoltage_Type()
)
dataLogInletPoleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInletPoleVoltage.setStatus("deprecated")
_DataLogAvgInletPoleCurrent_Type = MilliAmps
_DataLogAvgInletPoleCurrent_Object = MibTableColumn
dataLogAvgInletPoleCurrent = _DataLogAvgInletPoleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 4),
    _DataLogAvgInletPoleCurrent_Type()
)
dataLogAvgInletPoleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletPoleCurrent.setStatus("current")
_DataLogMaxInletPoleCurrent_Type = MilliAmps
_DataLogMaxInletPoleCurrent_Object = MibTableColumn
dataLogMaxInletPoleCurrent = _DataLogMaxInletPoleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 5),
    _DataLogMaxInletPoleCurrent_Type()
)
dataLogMaxInletPoleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletPoleCurrent.setStatus("current")
_DataLogMinInletPoleCurrent_Type = MilliAmps
_DataLogMinInletPoleCurrent_Object = MibTableColumn
dataLogMinInletPoleCurrent = _DataLogMinInletPoleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 6),
    _DataLogMinInletPoleCurrent_Type()
)
dataLogMinInletPoleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletPoleCurrent.setStatus("current")
_DataLogAvgInletPoleVoltage_Type = MilliVolts
_DataLogAvgInletPoleVoltage_Object = MibTableColumn
dataLogAvgInletPoleVoltage = _DataLogAvgInletPoleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 7),
    _DataLogAvgInletPoleVoltage_Type()
)
dataLogAvgInletPoleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletPoleVoltage.setStatus("current")
_DataLogMaxInletPoleVoltage_Type = MilliVolts
_DataLogMaxInletPoleVoltage_Object = MibTableColumn
dataLogMaxInletPoleVoltage = _DataLogMaxInletPoleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 8),
    _DataLogMaxInletPoleVoltage_Type()
)
dataLogMaxInletPoleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletPoleVoltage.setStatus("current")
_DataLogMinInletPoleVoltage_Type = MilliVolts
_DataLogMinInletPoleVoltage_Object = MibTableColumn
dataLogMinInletPoleVoltage = _DataLogMinInletPoleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 9),
    _DataLogMinInletPoleVoltage_Type()
)
dataLogMinInletPoleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletPoleVoltage.setStatus("current")
_DataLogAvgInletPoleActivePower_Type = Watts
_DataLogAvgInletPoleActivePower_Object = MibTableColumn
dataLogAvgInletPoleActivePower = _DataLogAvgInletPoleActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 10),
    _DataLogAvgInletPoleActivePower_Type()
)
dataLogAvgInletPoleActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletPoleActivePower.setStatus("current")
_DataLogMaxInletPoleActivePower_Type = Watts
_DataLogMaxInletPoleActivePower_Object = MibTableColumn
dataLogMaxInletPoleActivePower = _DataLogMaxInletPoleActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 11),
    _DataLogMaxInletPoleActivePower_Type()
)
dataLogMaxInletPoleActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletPoleActivePower.setStatus("current")
_DataLogMinInletPoleActivePower_Type = Watts
_DataLogMinInletPoleActivePower_Object = MibTableColumn
dataLogMinInletPoleActivePower = _DataLogMinInletPoleActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 12),
    _DataLogMinInletPoleActivePower_Type()
)
dataLogMinInletPoleActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletPoleActivePower.setStatus("current")
_DataLogAvgInletPoleApparentPower_Type = VoltAmps
_DataLogAvgInletPoleApparentPower_Object = MibTableColumn
dataLogAvgInletPoleApparentPower = _DataLogAvgInletPoleApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 13),
    _DataLogAvgInletPoleApparentPower_Type()
)
dataLogAvgInletPoleApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletPoleApparentPower.setStatus("current")
_DataLogMaxInletPoleApparentPower_Type = VoltAmps
_DataLogMaxInletPoleApparentPower_Object = MibTableColumn
dataLogMaxInletPoleApparentPower = _DataLogMaxInletPoleApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 14),
    _DataLogMaxInletPoleApparentPower_Type()
)
dataLogMaxInletPoleApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletPoleApparentPower.setStatus("current")
_DataLogMinInletPoleApparentPower_Type = VoltAmps
_DataLogMinInletPoleApparentPower_Object = MibTableColumn
dataLogMinInletPoleApparentPower = _DataLogMinInletPoleApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 15),
    _DataLogMinInletPoleApparentPower_Type()
)
dataLogMinInletPoleApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletPoleApparentPower.setStatus("current")
_DataLogAvgInletPoleActiveEnergy_Type = WattHours
_DataLogAvgInletPoleActiveEnergy_Object = MibTableColumn
dataLogAvgInletPoleActiveEnergy = _DataLogAvgInletPoleActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 16),
    _DataLogAvgInletPoleActiveEnergy_Type()
)
dataLogAvgInletPoleActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgInletPoleActiveEnergy.setStatus("current")
_DataLogMaxInletPoleActiveEnergy_Type = WattHours
_DataLogMaxInletPoleActiveEnergy_Object = MibTableColumn
dataLogMaxInletPoleActiveEnergy = _DataLogMaxInletPoleActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 17),
    _DataLogMaxInletPoleActiveEnergy_Type()
)
dataLogMaxInletPoleActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxInletPoleActiveEnergy.setStatus("current")
_DataLogMinInletPoleActiveEnergy_Type = WattHours
_DataLogMinInletPoleActiveEnergy_Object = MibTableColumn
dataLogMinInletPoleActiveEnergy = _DataLogMinInletPoleActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 13, 1, 1, 18),
    _DataLogMinInletPoleActiveEnergy_Type()
)
dataLogMinInletPoleActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinInletPoleActiveEnergy.setStatus("current")
_DataLogInputLine_ObjectIdentity = ObjectIdentity
dataLogInputLine = _DataLogInputLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 14)
)
_DataLogInputLineTable_Object = MibTable
dataLogInputLineTable = _DataLogInputLineTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 14, 1)
)
if mibBuilder.loadTexts:
    dataLogInputLineTable.setStatus("deprecated")
_DataLogInputLineEntry_Object = MibTableRow
dataLogInputLineEntry = _DataLogInputLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 14, 1, 1)
)
dataLogInputLineEntry.setIndexNames(
    (0, "PDU-MIB", "dataLogIndex"),
    (0, "PDU-MIB", "dataLogInputLineIndex"),
)
if mibBuilder.loadTexts:
    dataLogInputLineEntry.setStatus("deprecated")


class _DataLogInputLineIndex_Type(Integer32):
    """Custom type dataLogInputLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogInputLineIndex_Type.__name__ = "Integer32"
_DataLogInputLineIndex_Object = MibTableColumn
dataLogInputLineIndex = _DataLogInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 14, 1, 1, 1),
    _DataLogInputLineIndex_Type()
)
dataLogInputLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataLogInputLineIndex.setStatus("deprecated")
_DataLogInputLineCurrent_Type = MilliAmps
_DataLogInputLineCurrent_Object = MibTableColumn
dataLogInputLineCurrent = _DataLogInputLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 14, 1, 1, 2),
    _DataLogInputLineCurrent_Type()
)
dataLogInputLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInputLineCurrent.setStatus("deprecated")
_DataLogInputLineVoltage_Type = MilliVolts
_DataLogInputLineVoltage_Object = MibTableColumn
dataLogInputLineVoltage = _DataLogInputLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 14, 1, 1, 3),
    _DataLogInputLineVoltage_Type()
)
dataLogInputLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogInputLineVoltage.setStatus("deprecated")
_DataLogCircuitBreaker_ObjectIdentity = ObjectIdentity
dataLogCircuitBreaker = _DataLogCircuitBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15)
)
_DataLogCircuitBreakerTable_Object = MibTable
dataLogCircuitBreakerTable = _DataLogCircuitBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    dataLogCircuitBreakerTable.setStatus("current")
_DataLogCircuitBreakerEntry_Object = MibTableRow
dataLogCircuitBreakerEntry = _DataLogCircuitBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15, 1, 1)
)
dataLogCircuitBreakerEntry.setIndexNames(
    (0, "PDU-MIB", "dataLogIndex"),
    (0, "PDU-MIB", "dataLogCircuitBreakerIndex"),
)
if mibBuilder.loadTexts:
    dataLogCircuitBreakerEntry.setStatus("current")


class _DataLogCircuitBreakerIndex_Type(Integer32):
    """Custom type dataLogCircuitBreakerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogCircuitBreakerIndex_Type.__name__ = "Integer32"
_DataLogCircuitBreakerIndex_Object = MibTableColumn
dataLogCircuitBreakerIndex = _DataLogCircuitBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15, 1, 1, 1),
    _DataLogCircuitBreakerIndex_Type()
)
dataLogCircuitBreakerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataLogCircuitBreakerIndex.setStatus("current")
_DataLogCircuitBreakerCurrent_Type = MilliAmps
_DataLogCircuitBreakerCurrent_Object = MibTableColumn
dataLogCircuitBreakerCurrent = _DataLogCircuitBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15, 1, 1, 2),
    _DataLogCircuitBreakerCurrent_Type()
)
dataLogCircuitBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogCircuitBreakerCurrent.setStatus("deprecated")
_DataLogAvgCircuitBreakerCurrent_Type = MilliAmps
_DataLogAvgCircuitBreakerCurrent_Object = MibTableColumn
dataLogAvgCircuitBreakerCurrent = _DataLogAvgCircuitBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15, 1, 1, 3),
    _DataLogAvgCircuitBreakerCurrent_Type()
)
dataLogAvgCircuitBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgCircuitBreakerCurrent.setStatus("current")
_DataLogMaxCircuitBreakerCurrent_Type = MilliAmps
_DataLogMaxCircuitBreakerCurrent_Object = MibTableColumn
dataLogMaxCircuitBreakerCurrent = _DataLogMaxCircuitBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15, 1, 1, 4),
    _DataLogMaxCircuitBreakerCurrent_Type()
)
dataLogMaxCircuitBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxCircuitBreakerCurrent.setStatus("current")
_DataLogMinCircuitBreakerCurrent_Type = MilliAmps
_DataLogMinCircuitBreakerCurrent_Object = MibTableColumn
dataLogMinCircuitBreakerCurrent = _DataLogMinCircuitBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 15, 1, 1, 5),
    _DataLogMinCircuitBreakerCurrent_Type()
)
dataLogMinCircuitBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinCircuitBreakerCurrent.setStatus("current")
_DataLogExternalSensor_ObjectIdentity = ObjectIdentity
dataLogExternalSensor = _DataLogExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16)
)
_DataLogExternalSensorTable_Object = MibTable
dataLogExternalSensorTable = _DataLogExternalSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    dataLogExternalSensorTable.setStatus("current")
_DataLogExternalSensorEntry_Object = MibTableRow
dataLogExternalSensorEntry = _DataLogExternalSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1, 1)
)
dataLogExternalSensorEntry.setIndexNames(
    (0, "PDU-MIB", "dataLogIndex"),
    (0, "PDU-MIB", "dataLogExternalSensorIndex"),
)
if mibBuilder.loadTexts:
    dataLogExternalSensorEntry.setStatus("current")


class _DataLogExternalSensorIndex_Type(Integer32):
    """Custom type dataLogExternalSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DataLogExternalSensorIndex_Type.__name__ = "Integer32"
_DataLogExternalSensorIndex_Object = MibTableColumn
dataLogExternalSensorIndex = _DataLogExternalSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1, 1, 1),
    _DataLogExternalSensorIndex_Type()
)
dataLogExternalSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataLogExternalSensorIndex.setStatus("current")
_DataLogExternalSensorChanged_Type = DisplayString
_DataLogExternalSensorChanged_Object = MibTableColumn
dataLogExternalSensorChanged = _DataLogExternalSensorChanged_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1, 1, 2),
    _DataLogExternalSensorChanged_Type()
)
dataLogExternalSensorChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogExternalSensorChanged.setStatus("current")
_DataLogExternalSensorState_Type = StateOfSensorEnumeration
_DataLogExternalSensorState_Object = MibTableColumn
dataLogExternalSensorState = _DataLogExternalSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1, 1, 3),
    _DataLogExternalSensorState_Type()
)
dataLogExternalSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogExternalSensorState.setStatus("current")
_DataLogAvgExternalSensorValue_Type = Integer32
_DataLogAvgExternalSensorValue_Object = MibTableColumn
dataLogAvgExternalSensorValue = _DataLogAvgExternalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1, 1, 4),
    _DataLogAvgExternalSensorValue_Type()
)
dataLogAvgExternalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogAvgExternalSensorValue.setStatus("current")
_DataLogMaxExternalSensorValue_Type = Integer32
_DataLogMaxExternalSensorValue_Object = MibTableColumn
dataLogMaxExternalSensorValue = _DataLogMaxExternalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1, 1, 5),
    _DataLogMaxExternalSensorValue_Type()
)
dataLogMaxExternalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMaxExternalSensorValue.setStatus("current")
_DataLogMinExternalSensorValue_Type = Integer32
_DataLogMinExternalSensorValue_Object = MibTableColumn
dataLogMinExternalSensorValue = _DataLogMinExternalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 16, 1, 1, 6),
    _DataLogMinExternalSensorValue_Type()
)
dataLogMinExternalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataLogMinExternalSensorValue.setStatus("current")
_Inlets_ObjectIdentity = ObjectIdentity
inlets = _Inlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20)
)
_InletCount_Type = Integer32
_InletCount_Object = MibScalar
inletCount = _InletCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 1),
    _InletCount_Type()
)
inletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCount.setStatus("current")
_InletTable_Object = MibTable
inletTable = _InletTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2)
)
if mibBuilder.loadTexts:
    inletTable.setStatus("current")
_InletEntry_Object = MibTableRow
inletEntry = _InletEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1)
)
inletEntry.setIndexNames(
    (0, "PDU-MIB", "inletIndex"),
)
if mibBuilder.loadTexts:
    inletEntry.setStatus("current")


class _InletIndex_Type(Integer32):
    """Custom type inletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_InletIndex_Type.__name__ = "Integer32"
_InletIndex_Object = MibTableColumn
inletIndex = _InletIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 1),
    _InletIndex_Type()
)
inletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inletIndex.setStatus("current")
_InletPoleCount_Type = Integer32
_InletPoleCount_Object = MibTableColumn
inletPoleCount = _InletPoleCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 3),
    _InletPoleCount_Type()
)
inletPoleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleCount.setStatus("current")
_InletCurrentRating_Type = MilliAmps
_InletCurrentRating_Object = MibTableColumn
inletCurrentRating = _InletCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 4),
    _InletCurrentRating_Type()
)
inletCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrentRating.setStatus("current")
_InletCurrent_Type = MilliAmps
_InletCurrent_Object = MibTableColumn
inletCurrent = _InletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 7),
    _InletCurrent_Type()
)
inletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrent.setStatus("current")
_InletVoltage_Type = MilliVolts
_InletVoltage_Object = MibTableColumn
inletVoltage = _InletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 8),
    _InletVoltage_Type()
)
inletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletVoltage.setStatus("current")
_InletActivePower_Type = Watts
_InletActivePower_Object = MibTableColumn
inletActivePower = _InletActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 9),
    _InletActivePower_Type()
)
inletActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletActivePower.setStatus("current")
_InletApparentPower_Type = VoltAmps
_InletApparentPower_Object = MibTableColumn
inletApparentPower = _InletApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 10),
    _InletApparentPower_Type()
)
inletApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletApparentPower.setStatus("current")
_InletPowerFactor_Type = PowerFactorPercentage
_InletPowerFactor_Object = MibTableColumn
inletPowerFactor = _InletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 11),
    _InletPowerFactor_Type()
)
inletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPowerFactor.setStatus("current")
_InletActiveEnergy_Type = WattHours
_InletActiveEnergy_Object = MibTableColumn
inletActiveEnergy = _InletActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 12),
    _InletActiveEnergy_Type()
)
inletActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletActiveEnergy.setStatus("current")
_InletCurrentUnbalance_Type = DisplayString
_InletCurrentUnbalance_Object = MibTableColumn
inletCurrentUnbalance = _InletCurrentUnbalance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 15),
    _InletCurrentUnbalance_Type()
)
inletCurrentUnbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCurrentUnbalance.setStatus("current")
_InletCurrentUpperWarning_Type = MilliAmps
_InletCurrentUpperWarning_Object = MibTableColumn
inletCurrentUpperWarning = _InletCurrentUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 20),
    _InletCurrentUpperWarning_Type()
)
inletCurrentUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentUpperWarning.setStatus("current")
_InletCurrentUpperCritical_Type = MilliAmps
_InletCurrentUpperCritical_Object = MibTableColumn
inletCurrentUpperCritical = _InletCurrentUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 21),
    _InletCurrentUpperCritical_Type()
)
inletCurrentUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentUpperCritical.setStatus("current")
_InletCurrentLowerWarning_Type = MilliAmps
_InletCurrentLowerWarning_Object = MibTableColumn
inletCurrentLowerWarning = _InletCurrentLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 22),
    _InletCurrentLowerWarning_Type()
)
inletCurrentLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentLowerWarning.setStatus("current")
_InletCurrentLowerCritical_Type = MilliAmps
_InletCurrentLowerCritical_Object = MibTableColumn
inletCurrentLowerCritical = _InletCurrentLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 23),
    _InletCurrentLowerCritical_Type()
)
inletCurrentLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentLowerCritical.setStatus("current")
_InletVoltageUpperWarning_Type = MilliVolts
_InletVoltageUpperWarning_Object = MibTableColumn
inletVoltageUpperWarning = _InletVoltageUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 24),
    _InletVoltageUpperWarning_Type()
)
inletVoltageUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletVoltageUpperWarning.setStatus("current")
_InletVoltageUpperCritical_Type = MilliVolts
_InletVoltageUpperCritical_Object = MibTableColumn
inletVoltageUpperCritical = _InletVoltageUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 25),
    _InletVoltageUpperCritical_Type()
)
inletVoltageUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletVoltageUpperCritical.setStatus("current")
_InletVoltageLowerWarning_Type = MilliVolts
_InletVoltageLowerWarning_Object = MibTableColumn
inletVoltageLowerWarning = _InletVoltageLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 26),
    _InletVoltageLowerWarning_Type()
)
inletVoltageLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletVoltageLowerWarning.setStatus("current")
_InletVoltageLowerCritical_Type = MilliVolts
_InletVoltageLowerCritical_Object = MibTableColumn
inletVoltageLowerCritical = _InletVoltageLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 27),
    _InletVoltageLowerCritical_Type()
)
inletVoltageLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletVoltageLowerCritical.setStatus("current")
_InletCurrentUnbalanceUpperCritical_Type = Percentage
_InletCurrentUnbalanceUpperCritical_Object = MibTableColumn
inletCurrentUnbalanceUpperCritical = _InletCurrentUnbalanceUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 28),
    _InletCurrentUnbalanceUpperCritical_Type()
)
inletCurrentUnbalanceUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentUnbalanceUpperCritical.setStatus("current")
_InletCurrentUnbalanceUpperWarning_Type = Percentage
_InletCurrentUnbalanceUpperWarning_Object = MibTableColumn
inletCurrentUnbalanceUpperWarning = _InletCurrentUnbalanceUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 29),
    _InletCurrentUnbalanceUpperWarning_Type()
)
inletCurrentUnbalanceUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentUnbalanceUpperWarning.setStatus("current")
_InletCurrentHysteresis_Type = Unsigned32
_InletCurrentHysteresis_Object = MibTableColumn
inletCurrentHysteresis = _InletCurrentHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 30),
    _InletCurrentHysteresis_Type()
)
inletCurrentHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentHysteresis.setStatus("current")
_InletVoltageHysteresis_Type = Unsigned32
_InletVoltageHysteresis_Object = MibTableColumn
inletVoltageHysteresis = _InletVoltageHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 31),
    _InletVoltageHysteresis_Type()
)
inletVoltageHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletVoltageHysteresis.setStatus("current")
_InletCurrentUnbalanceHysteresis_Type = Unsigned32
_InletCurrentUnbalanceHysteresis_Object = MibTableColumn
inletCurrentUnbalanceHysteresis = _InletCurrentUnbalanceHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 20, 2, 1, 32),
    _InletCurrentUnbalanceHysteresis_Type()
)
inletCurrentUnbalanceHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletCurrentUnbalanceHysteresis.setStatus("current")
_InletPole_ObjectIdentity = ObjectIdentity
inletPole = _InletPole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21)
)
_InletPoleTable_Object = MibTable
inletPoleTable = _InletPoleTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2)
)
if mibBuilder.loadTexts:
    inletPoleTable.setStatus("current")
_InletPoleEntry_Object = MibTableRow
inletPoleEntry = _InletPoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1)
)
inletPoleEntry.setIndexNames(
    (0, "PDU-MIB", "inletIndex"),
    (0, "PDU-MIB", "inletPoleIndex"),
)
if mibBuilder.loadTexts:
    inletPoleEntry.setStatus("current")


class _InletPoleIndex_Type(Integer32):
    """Custom type inletPoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_InletPoleIndex_Type.__name__ = "Integer32"
_InletPoleIndex_Object = MibTableColumn
inletPoleIndex = _InletPoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 1),
    _InletPoleIndex_Type()
)
inletPoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inletPoleIndex.setStatus("current")
_InletPoleLabel_Type = DisplayString
_InletPoleLabel_Object = MibTableColumn
inletPoleLabel = _InletPoleLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 2),
    _InletPoleLabel_Type()
)
inletPoleLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleLabel.setStatus("current")
_InletPoleCurrent_Type = MilliAmps
_InletPoleCurrent_Object = MibTableColumn
inletPoleCurrent = _InletPoleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 3),
    _InletPoleCurrent_Type()
)
inletPoleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleCurrent.setStatus("current")
_InletPoleVoltage_Type = MilliVolts
_InletPoleVoltage_Object = MibTableColumn
inletPoleVoltage = _InletPoleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 4),
    _InletPoleVoltage_Type()
)
inletPoleVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleVoltage.setStatus("current")
_InletPoleMaxCurrent_Type = MilliAmps
_InletPoleMaxCurrent_Object = MibTableColumn
inletPoleMaxCurrent = _InletPoleMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 5),
    _InletPoleMaxCurrent_Type()
)
inletPoleMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleMaxCurrent.setStatus("current")
_InletPoleActivePower_Type = Watts
_InletPoleActivePower_Object = MibTableColumn
inletPoleActivePower = _InletPoleActivePower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 7),
    _InletPoleActivePower_Type()
)
inletPoleActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleActivePower.setStatus("current")
_InletPoleApparentPower_Type = VoltAmps
_InletPoleApparentPower_Object = MibTableColumn
inletPoleApparentPower = _InletPoleApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 8),
    _InletPoleApparentPower_Type()
)
inletPoleApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleApparentPower.setStatus("current")
_InletPolePowerFactor_Type = PowerFactorPercentage
_InletPolePowerFactor_Object = MibTableColumn
inletPolePowerFactor = _InletPolePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 9),
    _InletPolePowerFactor_Type()
)
inletPolePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPolePowerFactor.setStatus("current")
_InletPoleActiveEnergy_Type = WattHours
_InletPoleActiveEnergy_Object = MibTableColumn
inletPoleActiveEnergy = _InletPoleActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 1, 21, 2, 1, 11),
    _InletPoleActiveEnergy_Type()
)
inletPoleActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleActiveEnergy.setStatus("current")
_Environmental_ObjectIdentity = ObjectIdentity
environmental = _Environmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2)
)
_TempSensorCount_Type = Integer32
_TempSensorCount_Object = MibScalar
tempSensorCount = _TempSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 1),
    _TempSensorCount_Type()
)
tempSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorCount.setStatus("deprecated")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("deprecated")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1)
)
tempSensorEntry.setIndexNames(
    (0, "PDU-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("deprecated")


class _TempSensorIndex_Type(Integer32):
    """Custom type tempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TempSensorIndex_Type.__name__ = "Integer32"
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("deprecated")
_TempSensorLabel_Type = DisplayString
_TempSensorLabel_Object = MibTableColumn
tempSensorLabel = _TempSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 2),
    _TempSensorLabel_Type()
)
tempSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempSensorLabel.setStatus("deprecated")
_Temperature_Type = TenthDegreesCelsius
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 3),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("deprecated")
_TempLowerWarning_Type = DegreesCelsius
_TempLowerWarning_Object = MibTableColumn
tempLowerWarning = _TempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 4),
    _TempLowerWarning_Type()
)
tempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowerWarning.setStatus("deprecated")
_TempUpperWarning_Type = DegreesCelsius
_TempUpperWarning_Object = MibTableColumn
tempUpperWarning = _TempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 5),
    _TempUpperWarning_Type()
)
tempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempUpperWarning.setStatus("deprecated")
_TempLowerCritical_Type = DegreesCelsius
_TempLowerCritical_Object = MibTableColumn
tempLowerCritical = _TempLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 6),
    _TempLowerCritical_Type()
)
tempLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowerCritical.setStatus("deprecated")
_TempUpperCritical_Type = DegreesCelsius
_TempUpperCritical_Object = MibTableColumn
tempUpperCritical = _TempUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 7),
    _TempUpperCritical_Type()
)
tempUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempUpperCritical.setStatus("deprecated")
_TempXCoordinate_Type = DisplayString
_TempXCoordinate_Object = MibTableColumn
tempXCoordinate = _TempXCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 8),
    _TempXCoordinate_Type()
)
tempXCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempXCoordinate.setStatus("deprecated")
_TempYCoordinate_Type = DisplayString
_TempYCoordinate_Object = MibTableColumn
tempYCoordinate = _TempYCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 9),
    _TempYCoordinate_Type()
)
tempYCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempYCoordinate.setStatus("deprecated")
_TempZCoordinate_Type = DisplayString
_TempZCoordinate_Object = MibTableColumn
tempZCoordinate = _TempZCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 2, 1, 10),
    _TempZCoordinate_Type()
)
tempZCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempZCoordinate.setStatus("deprecated")
_HumiditySensorCount_Type = Integer32
_HumiditySensorCount_Object = MibScalar
humiditySensorCount = _HumiditySensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 3),
    _HumiditySensorCount_Type()
)
humiditySensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensorCount.setStatus("deprecated")
_HumiditySensorTable_Object = MibTable
humiditySensorTable = _HumiditySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4)
)
if mibBuilder.loadTexts:
    humiditySensorTable.setStatus("deprecated")
_HumiditySensorEntry_Object = MibTableRow
humiditySensorEntry = _HumiditySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1)
)
humiditySensorEntry.setIndexNames(
    (0, "PDU-MIB", "humiditySensorIndex"),
)
if mibBuilder.loadTexts:
    humiditySensorEntry.setStatus("deprecated")


class _HumiditySensorIndex_Type(Integer32):
    """Custom type humiditySensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HumiditySensorIndex_Type.__name__ = "Integer32"
_HumiditySensorIndex_Object = MibTableColumn
humiditySensorIndex = _HumiditySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 1),
    _HumiditySensorIndex_Type()
)
humiditySensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    humiditySensorIndex.setStatus("deprecated")
_HumiditySensorLabel_Type = DisplayString
_HumiditySensorLabel_Object = MibTableColumn
humiditySensorLabel = _HumiditySensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 2),
    _HumiditySensorLabel_Type()
)
humiditySensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensorLabel.setStatus("deprecated")
_Humidity_Type = RelativeHumidity
_Humidity_Object = MibTableColumn
humidity = _Humidity_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 3),
    _Humidity_Type()
)
humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity.setStatus("deprecated")
_HumidityLowerWarning_Type = RelativeHumidity
_HumidityLowerWarning_Object = MibTableColumn
humidityLowerWarning = _HumidityLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 4),
    _HumidityLowerWarning_Type()
)
humidityLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowerWarning.setStatus("deprecated")
_HumidityUpperWarning_Type = RelativeHumidity
_HumidityUpperWarning_Object = MibTableColumn
humidityUpperWarning = _HumidityUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 5),
    _HumidityUpperWarning_Type()
)
humidityUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityUpperWarning.setStatus("deprecated")
_HumidityLowerCritical_Type = RelativeHumidity
_HumidityLowerCritical_Object = MibTableColumn
humidityLowerCritical = _HumidityLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 6),
    _HumidityLowerCritical_Type()
)
humidityLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowerCritical.setStatus("deprecated")
_HumidityUpperCritical_Type = RelativeHumidity
_HumidityUpperCritical_Object = MibTableColumn
humidityUpperCritical = _HumidityUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 7),
    _HumidityUpperCritical_Type()
)
humidityUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityUpperCritical.setStatus("deprecated")
_HumidityXCoordinate_Type = DisplayString
_HumidityXCoordinate_Object = MibTableColumn
humidityXCoordinate = _HumidityXCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 8),
    _HumidityXCoordinate_Type()
)
humidityXCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityXCoordinate.setStatus("deprecated")
_HumidityYCoordinate_Type = DisplayString
_HumidityYCoordinate_Object = MibTableColumn
humidityYCoordinate = _HumidityYCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 9),
    _HumidityYCoordinate_Type()
)
humidityYCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityYCoordinate.setStatus("deprecated")
_HumidityZCoordinate_Type = DisplayString
_HumidityZCoordinate_Object = MibTableColumn
humidityZCoordinate = _HumidityZCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 2, 4, 1, 10),
    _HumidityZCoordinate_Type()
)
humidityZCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityZCoordinate.setStatus("deprecated")
_ExternalSensors_ObjectIdentity = ObjectIdentity
externalSensors = _ExternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3)
)


class _ExternalSensorCount_Type(Integer32):
    """Custom type externalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExternalSensorCount_Type.__name__ = "Integer32"
_ExternalSensorCount_Object = MibScalar
externalSensorCount = _ExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 1),
    _ExternalSensorCount_Type()
)
externalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorCount.setStatus("current")
_ReorderexternalSensorTableEntries_Type = DisplayString
_ReorderexternalSensorTableEntries_Object = MibScalar
reorderexternalSensorTableEntries = _ReorderexternalSensorTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 2),
    _ReorderexternalSensorTableEntries_Type()
)
reorderexternalSensorTableEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reorderexternalSensorTableEntries.setStatus("current")
_ExternalSensorTable_Object = MibTable
externalSensorTable = _ExternalSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3)
)
if mibBuilder.loadTexts:
    externalSensorTable.setStatus("current")
_ExternalSensorEntry_Object = MibTableRow
externalSensorEntry = _ExternalSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1)
)
externalSensorEntry.setIndexNames(
    (0, "PDU-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    externalSensorEntry.setStatus("current")


class _SensorID_Type(Integer32):
    """Custom type sensorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SensorID_Type.__name__ = "Integer32"
_SensorID_Object = MibTableColumn
sensorID = _SensorID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 1),
    _SensorID_Type()
)
sensorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorID.setStatus("current")
_ExternalSensorType_Type = TypeOfSensorEnumeration
_ExternalSensorType_Object = MibTableColumn
externalSensorType = _ExternalSensorType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 2),
    _ExternalSensorType_Type()
)
externalSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorType.setStatus("current")
_ExternalSensorSerialNumber_Type = DisplayString
_ExternalSensorSerialNumber_Object = MibTableColumn
externalSensorSerialNumber = _ExternalSensorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 3),
    _ExternalSensorSerialNumber_Type()
)
externalSensorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorSerialNumber.setStatus("current")
_ExternalSensorName_Type = DisplayString
_ExternalSensorName_Object = MibTableColumn
externalSensorName = _ExternalSensorName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 4),
    _ExternalSensorName_Type()
)
externalSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorName.setStatus("current")
_ExternalSensorChannelNumber_Type = Integer32
_ExternalSensorChannelNumber_Object = MibTableColumn
externalSensorChannelNumber = _ExternalSensorChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 5),
    _ExternalSensorChannelNumber_Type()
)
externalSensorChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorChannelNumber.setStatus("current")
_ExternalSensorXCoordinate_Type = DisplayString
_ExternalSensorXCoordinate_Object = MibTableColumn
externalSensorXCoordinate = _ExternalSensorXCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 6),
    _ExternalSensorXCoordinate_Type()
)
externalSensorXCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorXCoordinate.setStatus("current")
_ExternalSensorYCoordinate_Type = DisplayString
_ExternalSensorYCoordinate_Object = MibTableColumn
externalSensorYCoordinate = _ExternalSensorYCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 7),
    _ExternalSensorYCoordinate_Type()
)
externalSensorYCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorYCoordinate.setStatus("current")
_ExternalSensorZCoordinate_Type = DisplayString
_ExternalSensorZCoordinate_Object = MibTableColumn
externalSensorZCoordinate = _ExternalSensorZCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 8),
    _ExternalSensorZCoordinate_Type()
)
externalSensorZCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorZCoordinate.setStatus("current")
_ExternalBinarySensorSubtype_Type = TypeOfSensorEnumeration
_ExternalBinarySensorSubtype_Object = MibTableColumn
externalBinarySensorSubtype = _ExternalBinarySensorSubtype_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 9),
    _ExternalBinarySensorSubtype_Type()
)
externalBinarySensorSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBinarySensorSubtype.setStatus("current")
_ExternalSensorUnits_Type = SensorUnitsEnumeration
_ExternalSensorUnits_Object = MibTableColumn
externalSensorUnits = _ExternalSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 16),
    _ExternalSensorUnits_Type()
)
externalSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorUnits.setStatus("current")
_ExternalSensorDecimalDigits_Type = Unsigned32
_ExternalSensorDecimalDigits_Object = MibTableColumn
externalSensorDecimalDigits = _ExternalSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 17),
    _ExternalSensorDecimalDigits_Type()
)
externalSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorDecimalDigits.setStatus("current")
_ExternalSensorLowerCriticalThreshold_Type = Integer32
_ExternalSensorLowerCriticalThreshold_Object = MibTableColumn
externalSensorLowerCriticalThreshold = _ExternalSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 31),
    _ExternalSensorLowerCriticalThreshold_Type()
)
externalSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorLowerCriticalThreshold.setStatus("current")
_ExternalSensorLowerWarningThreshold_Type = Integer32
_ExternalSensorLowerWarningThreshold_Object = MibTableColumn
externalSensorLowerWarningThreshold = _ExternalSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 32),
    _ExternalSensorLowerWarningThreshold_Type()
)
externalSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorLowerWarningThreshold.setStatus("current")
_ExternalSensorUpperCriticalThreshold_Type = Integer32
_ExternalSensorUpperCriticalThreshold_Object = MibTableColumn
externalSensorUpperCriticalThreshold = _ExternalSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 33),
    _ExternalSensorUpperCriticalThreshold_Type()
)
externalSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUpperCriticalThreshold.setStatus("current")
_ExternalSensorUpperWarningThreshold_Type = Integer32
_ExternalSensorUpperWarningThreshold_Object = MibTableColumn
externalSensorUpperWarningThreshold = _ExternalSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 34),
    _ExternalSensorUpperWarningThreshold_Type()
)
externalSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUpperWarningThreshold.setStatus("current")
_ExternalSensorHysteresis_Type = Unsigned32
_ExternalSensorHysteresis_Object = MibTableColumn
externalSensorHysteresis = _ExternalSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 35),
    _ExternalSensorHysteresis_Type()
)
externalSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorHysteresis.setStatus("current")
_ExternalSensorState_Type = StateOfSensorEnumeration
_ExternalSensorState_Object = MibTableColumn
externalSensorState = _ExternalSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 40),
    _ExternalSensorState_Type()
)
externalSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorState.setStatus("current")
_ExternalSensorValue_Type = Integer32
_ExternalSensorValue_Object = MibTableColumn
externalSensorValue = _ExternalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 4, 3, 3, 1, 41),
    _ExternalSensorValue_Type()
)
externalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorValue.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2)
)

# Managed Objects groups

infoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 1)
)
infoGroup.setObjects(
    ("PDU-MIB", "dataLoggingInterval")
)
if mibBuilder.loadTexts:
    infoGroup.setStatus("deprecated")

outletsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 2)
)
outletsGroup.setObjects(
      *(("PDU-MIB", "outletCount"),
        ("PDU-MIB", "outletLabel"),
        ("PDU-MIB", "outletCurrentRating"),
        ("PDU-MIB", "outletOperationalState"),
        ("PDU-MIB", "outletCurrent"),
        ("PDU-MIB", "outletMaxCurrent"),
        ("PDU-MIB", "outletVoltage"),
        ("PDU-MIB", "outletActivePower"),
        ("PDU-MIB", "outletApparentPower"),
        ("PDU-MIB", "outletPowerFactor"),
        ("PDU-MIB", "outletCurrentUpperWarning"),
        ("PDU-MIB", "outletCurrentUpperCritical"),
        ("PDU-MIB", "outletCurrentLowerWarning"),
        ("PDU-MIB", "outletCurrentLowerCritical"),
        ("PDU-MIB", "outletCurrentHysteresis"),
        ("PDU-MIB", "outletWattHours"))
)
if mibBuilder.loadTexts:
    outletsGroup.setStatus("current")

unitSensorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 4)
)
unitSensorsGroup.setObjects(
      *(("PDU-MIB", "unitCurrent"),
        ("PDU-MIB", "unitVoltage"),
        ("PDU-MIB", "unitActivePower"),
        ("PDU-MIB", "unitApparentPower"),
        ("PDU-MIB", "unitCpuTemp"),
        ("PDU-MIB", "unitVoltageLowerWarning"),
        ("PDU-MIB", "unitVoltageUpperWarning"),
        ("PDU-MIB", "unitVoltageLowerCritical"),
        ("PDU-MIB", "unitVoltageUpperCritical"),
        ("PDU-MIB", "unitCurrentUpperWarning"),
        ("PDU-MIB", "unitCurrentUpperCritical"),
        ("PDU-MIB", "unitTempLowerWarning"),
        ("PDU-MIB", "unitTempUpperWarning"),
        ("PDU-MIB", "unitTempLowerCritical"),
        ("PDU-MIB", "unitTempUpperCritical"))
)
if mibBuilder.loadTexts:
    unitSensorsGroup.setStatus("deprecated")

externalTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 6)
)
externalTemperatureGroup.setObjects(
      *(("PDU-MIB", "tempSensorCount"),
        ("PDU-MIB", "tempSensorLabel"),
        ("PDU-MIB", "temperature"),
        ("PDU-MIB", "tempLowerWarning"),
        ("PDU-MIB", "tempUpperWarning"),
        ("PDU-MIB", "tempLowerCritical"),
        ("PDU-MIB", "tempUpperCritical"),
        ("PDU-MIB", "tempXCoordinate"),
        ("PDU-MIB", "tempYCoordinate"),
        ("PDU-MIB", "tempZCoordinate"))
)
if mibBuilder.loadTexts:
    externalTemperatureGroup.setStatus("deprecated")

externalHumidityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 7)
)
externalHumidityGroup.setObjects(
      *(("PDU-MIB", "humiditySensorCount"),
        ("PDU-MIB", "humiditySensorLabel"),
        ("PDU-MIB", "humidity"),
        ("PDU-MIB", "humidityLowerWarning"),
        ("PDU-MIB", "humidityUpperWarning"),
        ("PDU-MIB", "humidityLowerCritical"),
        ("PDU-MIB", "humidityUpperCritical"),
        ("PDU-MIB", "humidityXCoordinate"),
        ("PDU-MIB", "humidityYCoordinate"),
        ("PDU-MIB", "humidityZCoordinate"))
)
if mibBuilder.loadTexts:
    externalHumidityGroup.setStatus("deprecated")

lineCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 10)
)
lineCurrentGroup.setObjects(
      *(("PDU-MIB", "lineCurrentCount"),
        ("PDU-MIB", "lineCurrentLabel"),
        ("PDU-MIB", "lineCurrent"))
)
if mibBuilder.loadTexts:
    lineCurrentGroup.setStatus("deprecated")

circuitBreakerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 11)
)
circuitBreakerGroup.setObjects(
      *(("PDU-MIB", "circuitBreakerCount"),
        ("PDU-MIB", "circuitBreakerLabel"),
        ("PDU-MIB", "circuitBreakerCurrentRating"),
        ("PDU-MIB", "circuitBreakerState"),
        ("PDU-MIB", "circuitBreakerCurrent"),
        ("PDU-MIB", "circuitBreakerCurrentUpperWarning"),
        ("PDU-MIB", "circuitBreakerCurrentUpperCritical"),
        ("PDU-MIB", "circuitBreakerCurrentHysteresis"))
)
if mibBuilder.loadTexts:
    circuitBreakerGroup.setStatus("current")

lineVoltageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 12)
)
lineVoltageGroup.setObjects(
      *(("PDU-MIB", "lineVoltageCount"),
        ("PDU-MIB", "lineVoltageLabel"),
        ("PDU-MIB", "lineVoltage"))
)
if mibBuilder.loadTexts:
    lineVoltageGroup.setStatus("deprecated")

unitSensorsGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 13)
)
unitSensorsGroupRev.setObjects(
      *(("PDU-MIB", "unitActivePower"),
        ("PDU-MIB", "unitApparentPower"),
        ("PDU-MIB", "unitCpuTemp"),
        ("PDU-MIB", "unitOrLineVoltageLowerWarning"),
        ("PDU-MIB", "unitOrLineVoltageUpperWarning"),
        ("PDU-MIB", "unitOrLineVoltageLowerCritical"),
        ("PDU-MIB", "unitOrLineVoltageUpperCritical"),
        ("PDU-MIB", "unitOrLineCurrentUpperWarning"),
        ("PDU-MIB", "unitOrLineCurrentUpperCritical"),
        ("PDU-MIB", "neutralCurrentUpperWarning"),
        ("PDU-MIB", "neutralCurrentUpperCritical"),
        ("PDU-MIB", "unitTempLowerWarning"),
        ("PDU-MIB", "unitTempUpperWarning"),
        ("PDU-MIB", "unitTempLowerCritical"),
        ("PDU-MIB", "unitTempUpperCritical"),
        ("PDU-MIB", "currentUnbalance"),
        ("PDU-MIB", "currentUnbalanceUpperWarning"),
        ("PDU-MIB", "currentUnbalanceUpperCritical"))
)
if mibBuilder.loadTexts:
    unitSensorsGroupRev.setStatus("deprecated")

dataLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 14)
)
dataLogGroup.setObjects(
      *(("PDU-MIB", "dataLogCount"),
        ("PDU-MIB", "dataLogLatestIndex"),
        ("PDU-MIB", "dataLogTimeStamp"),
        ("PDU-MIB", "dataLogActivePower"),
        ("PDU-MIB", "dataLogApparentPower"),
        ("PDU-MIB", "dataLogOutletCurrent"),
        ("PDU-MIB", "dataLogOutletVoltage"),
        ("PDU-MIB", "dataLogOutletPowerFactor"),
        ("PDU-MIB", "dataLogOutletOnTime"),
        ("PDU-MIB", "dataLogCircuitBreakerCurrent"),
        ("PDU-MIB", "dataLogInputLineCurrent"),
        ("PDU-MIB", "dataLogInputLineVoltage"),
        ("PDU-MIB", "dataLogOutletWattHours"))
)
if mibBuilder.loadTexts:
    dataLogGroup.setStatus("deprecated")

inletPoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 15)
)
inletPoleGroup.setObjects(
      *(("PDU-MIB", "inletPoleCount"),
        ("PDU-MIB", "inletPoleLabel"),
        ("PDU-MIB", "inletPoleCurrent"),
        ("PDU-MIB", "inletPoleVoltage"),
        ("PDU-MIB", "inletPoleMaxCurrent"),
        ("PDU-MIB", "inletPoleActivePower"),
        ("PDU-MIB", "inletPoleApparentPower"),
        ("PDU-MIB", "inletPolePowerFactor"),
        ("PDU-MIB", "inletPoleActiveEnergy"))
)
if mibBuilder.loadTexts:
    inletPoleGroup.setStatus("current")

inletsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 16)
)
inletsGroup.setObjects(
      *(("PDU-MIB", "inletCount"),
        ("PDU-MIB", "inletCurrentRating"),
        ("PDU-MIB", "inletCurrentUnbalanceUpperCritical"),
        ("PDU-MIB", "inletCurrentUnbalanceUpperWarning"),
        ("PDU-MIB", "inletCurrentUnbalance"),
        ("PDU-MIB", "inletActivePower"),
        ("PDU-MIB", "inletApparentPower"),
        ("PDU-MIB", "inletPoleCount"),
        ("PDU-MIB", "inletCurrent"),
        ("PDU-MIB", "inletVoltage"),
        ("PDU-MIB", "inletPowerFactor"),
        ("PDU-MIB", "inletActiveEnergy"),
        ("PDU-MIB", "inletCurrentUpperWarning"),
        ("PDU-MIB", "inletCurrentUpperCritical"),
        ("PDU-MIB", "inletCurrentLowerWarning"),
        ("PDU-MIB", "inletCurrentLowerCritical"),
        ("PDU-MIB", "inletVoltageUpperWarning"),
        ("PDU-MIB", "inletVoltageUpperCritical"),
        ("PDU-MIB", "inletVoltageLowerWarning"),
        ("PDU-MIB", "inletVoltageLowerCritical"),
        ("PDU-MIB", "inletCurrentHysteresis"),
        ("PDU-MIB", "inletVoltageHysteresis"),
        ("PDU-MIB", "inletCurrentUnbalanceHysteresis"))
)
if mibBuilder.loadTexts:
    inletsGroup.setStatus("current")

dataLogGroupRev = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 17)
)
dataLogGroupRev.setObjects(
      *(("PDU-MIB", "dataLogCount"),
        ("PDU-MIB", "dataLogLatestIndex"),
        ("PDU-MIB", "dataLogTimeStamp"),
        ("PDU-MIB", "dataLogActivePower"),
        ("PDU-MIB", "dataLogApparentPower"),
        ("PDU-MIB", "dataLogOutletCurrent"),
        ("PDU-MIB", "dataLogOutletVoltage"),
        ("PDU-MIB", "dataLogOutletPowerFactor"),
        ("PDU-MIB", "dataLogOutletOnTime"),
        ("PDU-MIB", "dataLogCircuitBreakerCurrent"),
        ("PDU-MIB", "dataLogOutletWattHours"),
        ("PDU-MIB", "dataLogInletPoleCurrent"),
        ("PDU-MIB", "dataLogInletPoleVoltage"),
        ("PDU-MIB", "dataLogInletCurrentUnbalance"),
        ("PDU-MIB", "dataLogInletActivePower"),
        ("PDU-MIB", "dataLogInletApparentPower"),
        ("PDU-MIB", "dataLogInletActiveEnergy"))
)
if mibBuilder.loadTexts:
    dataLogGroupRev.setStatus("deprecated")

unitSensorsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 18)
)
unitSensorsGroupRev2.setObjects(
      *(("PDU-MIB", "unitCpuTemp"),
        ("PDU-MIB", "unitOrLineVoltageLowerWarning"),
        ("PDU-MIB", "unitOrLineVoltageUpperWarning"),
        ("PDU-MIB", "unitOrLineVoltageLowerCritical"),
        ("PDU-MIB", "unitOrLineVoltageUpperCritical"),
        ("PDU-MIB", "unitOrLineCurrentUpperWarning"),
        ("PDU-MIB", "unitOrLineCurrentUpperCritical"),
        ("PDU-MIB", "neutralCurrentUpperWarning"),
        ("PDU-MIB", "neutralCurrentUpperCritical"),
        ("PDU-MIB", "unitTempLowerWarning"),
        ("PDU-MIB", "unitTempUpperWarning"),
        ("PDU-MIB", "unitTempLowerCritical"),
        ("PDU-MIB", "unitTempUpperCritical"),
        ("PDU-MIB", "currentUnbalance"),
        ("PDU-MIB", "currentUnbalanceUpperWarning"),
        ("PDU-MIB", "currentUnbalanceUpperCritical"),
        ("PDU-MIB", "unitOrLineVoltageHysteresis"),
        ("PDU-MIB", "unitOrLineCurrentHysteresis"),
        ("PDU-MIB", "unitTempHysteresis"),
        ("PDU-MIB", "currentUnbalanceHysteresis"))
)
if mibBuilder.loadTexts:
    unitSensorsGroupRev2.setStatus("current")

externalSensorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 20)
)
externalSensorsGroup.setObjects(
      *(("PDU-MIB", "externalSensorCount"),
        ("PDU-MIB", "externalSensorType"),
        ("PDU-MIB", "externalSensorSerialNumber"),
        ("PDU-MIB", "externalSensorName"),
        ("PDU-MIB", "externalSensorChannelNumber"),
        ("PDU-MIB", "externalSensorXCoordinate"),
        ("PDU-MIB", "externalSensorYCoordinate"),
        ("PDU-MIB", "externalSensorZCoordinate"),
        ("PDU-MIB", "externalBinarySensorSubtype"),
        ("PDU-MIB", "externalSensorUnits"),
        ("PDU-MIB", "externalSensorDecimalDigits"),
        ("PDU-MIB", "externalSensorLowerCriticalThreshold"),
        ("PDU-MIB", "externalSensorLowerWarningThreshold"),
        ("PDU-MIB", "externalSensorUpperCriticalThreshold"),
        ("PDU-MIB", "externalSensorUpperWarningThreshold"),
        ("PDU-MIB", "externalSensorState"),
        ("PDU-MIB", "externalSensorValue"),
        ("PDU-MIB", "externalSensorHysteresis"),
        ("PDU-MIB", "reorderexternalSensorTableEntries"))
)
if mibBuilder.loadTexts:
    externalSensorsGroup.setStatus("current")

dataLogGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 21)
)
dataLogGroupRev2.setObjects(
      *(("PDU-MIB", "dataLogCount"),
        ("PDU-MIB", "dataLogLatestIndex"),
        ("PDU-MIB", "dataLogTimeStamp"),
        ("PDU-MIB", "dataLogAvgActivePower"),
        ("PDU-MIB", "dataLogMaxActivePower"),
        ("PDU-MIB", "dataLogMinActivePower"),
        ("PDU-MIB", "dataLogAvgApparentPower"),
        ("PDU-MIB", "dataLogMaxApparentPower"),
        ("PDU-MIB", "dataLogMinApparentPower"),
        ("PDU-MIB", "dataLogAvgOutletCurrent"),
        ("PDU-MIB", "dataLogMaxOutletCurrent"),
        ("PDU-MIB", "dataLogMinOutletCurrent"),
        ("PDU-MIB", "dataLogAvgOutletVoltage"),
        ("PDU-MIB", "dataLogMaxOutletVoltage"),
        ("PDU-MIB", "dataLogMinOutletVoltage"),
        ("PDU-MIB", "dataLogAvgOutletPowerFactor"),
        ("PDU-MIB", "dataLogMaxOutletPowerFactor"),
        ("PDU-MIB", "dataLogMinOutletPowerFactor"),
        ("PDU-MIB", "dataLogAvgOutletWattHours"),
        ("PDU-MIB", "dataLogMaxOutletWattHours"),
        ("PDU-MIB", "dataLogMinOutletWattHours"),
        ("PDU-MIB", "dataLogAvgCircuitBreakerCurrent"),
        ("PDU-MIB", "dataLogMaxCircuitBreakerCurrent"),
        ("PDU-MIB", "dataLogMinCircuitBreakerCurrent"),
        ("PDU-MIB", "dataLogAvgInletCurrentUnbalance"),
        ("PDU-MIB", "dataLogMaxInletCurrentUnbalance"),
        ("PDU-MIB", "dataLogMinInletCurrentUnbalance"),
        ("PDU-MIB", "dataLogAvgInletActivePower"),
        ("PDU-MIB", "dataLogMaxInletActivePower"),
        ("PDU-MIB", "dataLogMinInletActivePower"),
        ("PDU-MIB", "dataLogAvgInletApparentPower"),
        ("PDU-MIB", "dataLogMaxInletApparentPower"),
        ("PDU-MIB", "dataLogMinInletApparentPower"),
        ("PDU-MIB", "dataLogAvgInletActiveEnergy"),
        ("PDU-MIB", "dataLogMaxInletActiveEnergy"),
        ("PDU-MIB", "dataLogMinInletActiveEnergy"),
        ("PDU-MIB", "dataLogAvgInletPoleCurrent"),
        ("PDU-MIB", "dataLogMaxInletPoleCurrent"),
        ("PDU-MIB", "dataLogMinInletPoleCurrent"),
        ("PDU-MIB", "dataLogAvgInletPoleVoltage"),
        ("PDU-MIB", "dataLogMaxInletPoleVoltage"),
        ("PDU-MIB", "dataLogMinInletPoleVoltage"),
        ("PDU-MIB", "dataLogAvgInletPoleActivePower"),
        ("PDU-MIB", "dataLogMaxInletPoleActivePower"),
        ("PDU-MIB", "dataLogMinInletPoleActivePower"),
        ("PDU-MIB", "dataLogAvgInletPoleApparentPower"),
        ("PDU-MIB", "dataLogMaxInletPoleApparentPower"),
        ("PDU-MIB", "dataLogMinInletPoleApparentPower"),
        ("PDU-MIB", "dataLogAvgInletPoleActiveEnergy"),
        ("PDU-MIB", "dataLogMaxInletPoleActiveEnergy"),
        ("PDU-MIB", "dataLogMinInletPoleActiveEnergy"),
        ("PDU-MIB", "dataLogExternalSensorChanged"),
        ("PDU-MIB", "dataLogExternalSensorState"),
        ("PDU-MIB", "dataLogAvgExternalSensorValue"),
        ("PDU-MIB", "dataLogMaxExternalSensorValue"),
        ("PDU-MIB", "dataLogMinExternalSensorValue"))
)
if mibBuilder.loadTexts:
    dataLogGroupRev2.setStatus("current")

infoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 22)
)
infoGroupRev2.setObjects(
      *(("PDU-MIB", "firmwareVersion"),
        ("PDU-MIB", "serialNumber"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "netmask"),
        ("PDU-MIB", "gateway"),
        ("PDU-MIB", "mac"),
        ("PDU-MIB", "hardwareRev"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "targetUser"),
        ("PDU-MIB", "groupName"),
        ("PDU-MIB", "imageVersion"),
        ("PDU-MIB", "sensorDescr"),
        ("PDU-MIB", "thresholdDescr"),
        ("PDU-MIB", "thresholdSeverity"),
        ("PDU-MIB", "thresholdEventType"),
        ("PDU-MIB", "status"),
        ("PDU-MIB", "slaveIpAddress"),
        ("PDU-MIB", "inputCurrentRating"),
        ("PDU-MIB", "ratedVoltage"),
        ("PDU-MIB", "ratedPower"),
        ("PDU-MIB", "outletSwitching"),
        ("PDU-MIB", "dataLogging"),
        ("PDU-MIB", "dataCollectionInterval"),
        ("PDU-MIB", "outletEnergySupport"),
        ("PDU-MIB", "currentUnbalanceSupport"),
        ("PDU-MIB", "externalSensorsZCoordinateUnits"),
        ("PDU-MIB", "inlineMeter"),
        ("PDU-MIB", "oldSensorState"),
        ("PDU-MIB", "externalSensorNumber"),
        ("PDU-MIB", "sensorIdentificationString"),
        ("PDU-MIB", "lastUpgradeStatus"),
        ("PDU-MIB", "lastUpgradeTimestamp"),
        ("PDU-MIB", "lastUpgradeErrorDescription"),
        ("PDU-MIB", "powerCIMStatus"),
        ("PDU-MIB", "measurementsPerLogEntry"),
        ("PDU-MIB", "psocNumber"),
        ("PDU-MIB", "altitude"),
        ("PDU-MIB", "configureAlerts"),
        ("PDU-MIB", "fipsMode"),
        ("PDU-MIB", "synchronizeWithNTPServer"),
        ("PDU-MIB", "useDHCPProvidedNTPServer"),
        ("PDU-MIB", "primaryNTPServerAddressType"),
        ("PDU-MIB", "primaryNTPServerAddress"),
        ("PDU-MIB", "secondaryNTPServerAddressType"),
        ("PDU-MIB", "secondaryNTPServerAddress"),
        ("PDU-MIB", "daylightSavingsTime"),
        ("PDU-MIB", "thresholdValue"),
        ("PDU-MIB", "sensorValue"),
        ("PDU-MIB", "ipmiOverLAN"))
)
if mibBuilder.loadTexts:
    infoGroupRev2.setStatus("current")


# Notification objects

rebootStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 1)
)
rebootStarted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    rebootStarted.setStatus(
        "current"
    )

rebootCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 2)
)
rebootCompleted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"))
)
if mibBuilder.loadTexts:
    rebootCompleted.setStatus(
        "current"
    )

userLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 3)
)
userLogin.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userLogin.setStatus(
        "current"
    )

userLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 4)
)
userLogout.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userLogout.setStatus(
        "current"
    )

userAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 5)
)
userAuthenticationFailure.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userAuthenticationFailure.setStatus(
        "current"
    )

userSessionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 8)
)
userSessionTimeout.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userSessionTimeout.setStatus(
        "current"
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 11)
)
userAdded.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        "current"
    )

userModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 12)
)
userModified.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userModified.setStatus(
        "current"
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 13)
)
userDeleted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"))
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        "current"
    )

groupAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 14)
)
groupAdded.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupAdded.setStatus(
        "current"
    )

groupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 15)
)
groupModified.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupModified.setStatus(
        "current"
    )

groupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 16)
)
groupDeleted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "groupName"))
)
if mibBuilder.loadTexts:
    groupDeleted.setStatus(
        "current"
    )

deviceUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 20)
)
deviceUpdateStarted.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "imageVersion"))
)
if mibBuilder.loadTexts:
    deviceUpdateStarted.setStatus(
        "current"
    )

userBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 22)
)
userBlocked.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userBlocked.setStatus(
        "current"
    )

powerControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 23)
)
powerControl.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "outletLabel"),
        ("PDU-MIB", "outletOperationalState"))
)
if mibBuilder.loadTexts:
    powerControl.setStatus(
        "current"
    )

userPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 24)
)
userPasswordChanged.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "targetUser"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    userPasswordChanged.setStatus(
        "current"
    )

passwordSettingsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 28)
)
passwordSettingsChanged.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "status"))
)
if mibBuilder.loadTexts:
    passwordSettingsChanged.setStatus(
        "current"
    )

firmwareFileDiscarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 36)
)
firmwareFileDiscarded.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    firmwareFileDiscarded.setStatus(
        "current"
    )

firmwareValidationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 38)
)
firmwareValidationFailed.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    firmwareValidationFailed.setStatus(
        "current"
    )

securityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 39)
)
securityViolation.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    securityViolation.setStatus(
        "current"
    )

logFileCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 41)
)
logFileCleared.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    logFileCleared.setStatus(
        "current"
    )

thresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 45)
)
thresholdAlarm.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "sensorDescr"),
        ("PDU-MIB", "thresholdDescr"),
        ("PDU-MIB", "thresholdSeverity"),
        ("PDU-MIB", "thresholdEventType"),
        ("PDU-MIB", "sensorIdentificationString"),
        ("PDU-MIB", "thresholdValue"),
        ("PDU-MIB", "sensorValue"))
)
if mibBuilder.loadTexts:
    thresholdAlarm.setStatus(
        "current"
    )

outletGroupingConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 50)
)
outletGroupingConnectivityLost.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "slaveIpAddress"))
)
if mibBuilder.loadTexts:
    outletGroupingConnectivityLost.setStatus(
        "current"
    )

circuitBreakerTripped = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 51)
)
circuitBreakerTripped.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "circuitBreakerLabel"))
)
if mibBuilder.loadTexts:
    circuitBreakerTripped.setStatus(
        "current"
    )

circuitBreakerRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 52)
)
circuitBreakerRecovered.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "circuitBreakerLabel"))
)
if mibBuilder.loadTexts:
    circuitBreakerRecovered.setStatus(
        "current"
    )

bulkConfigurationSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 53)
)
bulkConfigurationSaved.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    bulkConfigurationSaved.setStatus(
        "current"
    )

bulkConfigurationCopied = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 54)
)
bulkConfigurationCopied.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"))
)
if mibBuilder.loadTexts:
    bulkConfigurationCopied.setStatus(
        "current"
    )

environmentalSensorsConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 55)
)
environmentalSensorsConnectivityLost.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "sensorDescr"),
        ("PDU-MIB", "externalSensorNumber"),
        ("PDU-MIB", "externalSensorType"),
        ("PDU-MIB", "externalSensorName"),
        ("PDU-MIB", "externalSensorChannelNumber"),
        ("PDU-MIB", "externalBinarySensorSubtype"),
        ("PDU-MIB", "externalSensorSerialNumber"))
)
if mibBuilder.loadTexts:
    environmentalSensorsConnectivityLost.setStatus(
        "current"
    )

externalOnOffSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 56)
)
externalOnOffSensorStateChange.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "externalSensorNumber"),
        ("PDU-MIB", "externalSensorType"),
        ("PDU-MIB", "externalSensorName"),
        ("PDU-MIB", "externalSensorChannelNumber"),
        ("PDU-MIB", "externalBinarySensorSubtype"),
        ("PDU-MIB", "externalSensorState"),
        ("PDU-MIB", "oldSensorState"),
        ("PDU-MIB", "externalSensorSerialNumber"))
)
if mibBuilder.loadTexts:
    externalOnOffSensorStateChange.setStatus(
        "current"
    )

environmentalSensorsConnectivityRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 57)
)
environmentalSensorsConnectivityRestored.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "externalSensorNumber"),
        ("PDU-MIB", "externalSensorType"),
        ("PDU-MIB", "externalSensorName"),
        ("PDU-MIB", "externalSensorChannelNumber"),
        ("PDU-MIB", "externalBinarySensorSubtype"),
        ("PDU-MIB", "externalSensorSerialNumber"))
)
if mibBuilder.loadTexts:
    environmentalSensorsConnectivityRestored.setStatus(
        "current"
    )

voltageMeasurementError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 58)
)
voltageMeasurementError.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "psocNumber"))
)
if mibBuilder.loadTexts:
    voltageMeasurementError.setStatus(
        "current"
    )

fipsModeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 59)
)
fipsModeEnabled.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    fipsModeEnabled.setStatus(
        "current"
    )

fipsModeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 60)
)
fipsModeDisabled.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    fipsModeDisabled.setStatus(
        "current"
    )

managingenvironmentalSensor = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 61)
)
managingenvironmentalSensor.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "sensorDescr"),
        ("PDU-MIB", "externalSensorNumber"),
        ("PDU-MIB", "externalSensorType"),
        ("PDU-MIB", "externalSensorName"),
        ("PDU-MIB", "externalSensorChannelNumber"),
        ("PDU-MIB", "externalBinarySensorSubtype"),
        ("PDU-MIB", "externalSensorSerialNumber"))
)
if mibBuilder.loadTexts:
    managingenvironmentalSensor.setStatus(
        "current"
    )

unmanagingenvironmentalSensor = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 62)
)
unmanagingenvironmentalSensor.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "ipAddress"),
        ("PDU-MIB", "sensorDescr"),
        ("PDU-MIB", "externalSensorNumber"),
        ("PDU-MIB", "externalSensorType"),
        ("PDU-MIB", "externalSensorName"),
        ("PDU-MIB", "externalSensorChannelNumber"),
        ("PDU-MIB", "externalBinarySensorSubtype"),
        ("PDU-MIB", "externalSensorSerialNumber"))
)
if mibBuilder.loadTexts:
    unmanagingenvironmentalSensor.setStatus(
        "current"
    )

ipmiOverLANEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 63)
)
ipmiOverLANEnabled.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    ipmiOverLANEnabled.setStatus(
        "current"
    )

ipmiOverLANDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 4, 0, 64)
)
ipmiOverLANDisabled.setObjects(
      *(("PDU-MIB", "objectName"),
        ("PDU-MIB", "objectInstance"),
        ("PDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    ipmiOverLANDisabled.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 2, 9)
)
trapsGroup.setObjects(
      *(("PDU-MIB", "rebootStarted"),
        ("PDU-MIB", "rebootCompleted"),
        ("PDU-MIB", "userLogin"),
        ("PDU-MIB", "userLogout"),
        ("PDU-MIB", "userAuthenticationFailure"),
        ("PDU-MIB", "userSessionTimeout"),
        ("PDU-MIB", "userAdded"),
        ("PDU-MIB", "userModified"),
        ("PDU-MIB", "userDeleted"),
        ("PDU-MIB", "groupAdded"),
        ("PDU-MIB", "groupModified"),
        ("PDU-MIB", "groupDeleted"),
        ("PDU-MIB", "deviceUpdateStarted"),
        ("PDU-MIB", "userBlocked"),
        ("PDU-MIB", "powerControl"),
        ("PDU-MIB", "userPasswordChanged"),
        ("PDU-MIB", "passwordSettingsChanged"),
        ("PDU-MIB", "firmwareFileDiscarded"),
        ("PDU-MIB", "firmwareValidationFailed"),
        ("PDU-MIB", "securityViolation"),
        ("PDU-MIB", "logFileCleared"),
        ("PDU-MIB", "thresholdAlarm"),
        ("PDU-MIB", "outletGroupingConnectivityLost"),
        ("PDU-MIB", "circuitBreakerTripped"),
        ("PDU-MIB", "circuitBreakerRecovered"),
        ("PDU-MIB", "bulkConfigurationSaved"),
        ("PDU-MIB", "bulkConfigurationCopied"),
        ("PDU-MIB", "environmentalSensorsConnectivityLost"),
        ("PDU-MIB", "externalOnOffSensorStateChange"),
        ("PDU-MIB", "environmentalSensorsConnectivityRestored"),
        ("PDU-MIB", "voltageMeasurementError"),
        ("PDU-MIB", "fipsModeEnabled"),
        ("PDU-MIB", "fipsModeDisabled"),
        ("PDU-MIB", "managingenvironmentalSensor"),
        ("PDU-MIB", "unmanagingenvironmentalSensor"),
        ("PDU-MIB", "ipmiOverLANEnabled"),
        ("PDU-MIB", "ipmiOverLANDisabled"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 1, 1)
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "deprecated"
    )

complianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 1, 2)
)
if mibBuilder.loadTexts:
    complianceRev1.setStatus(
        "deprecated"
    )

complianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 1, 3)
)
if mibBuilder.loadTexts:
    complianceRev2.setStatus(
        "deprecated"
    )

complianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 1, 4)
)
if mibBuilder.loadTexts:
    complianceRev3.setStatus(
        "deprecated"
    )

complianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 1, 5)
)
if mibBuilder.loadTexts:
    complianceRev4.setStatus(
        "deprecated"
    )

complianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 4, 9, 1, 6)
)
if mibBuilder.loadTexts:
    complianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDU-MIB",
    **{"MilliAmps": MilliAmps,
       "MilliVolts": MilliVolts,
       "Watts": Watts,
       "VoltAmps": VoltAmps,
       "DegreesCelsius": DegreesCelsius,
       "TenthDegreesCelsius": TenthDegreesCelsius,
       "Hertz": Hertz,
       "RelativeHumidity": RelativeHumidity,
       "PowerFactorPercentage": PowerFactorPercentage,
       "Percentage": Percentage,
       "SensorTypeEnumeration": SensorTypeEnumeration,
       "SensorStateEnumeration": SensorStateEnumeration,
       "StateOfSensorEnumeration": StateOfSensorEnumeration,
       "TypeOfSensorEnumeration": TypeOfSensorEnumeration,
       "WattHours": WattHours,
       "SensorUnitsEnumeration": SensorUnitsEnumeration,
       "PowerCIMStatusEnumeration": PowerCIMStatusEnumeration,
       "EnabledDisabledEnumeration": EnabledDisabledEnumeration,
       "SensorClassEnumeration": SensorClassEnumeration,
       "EventTypeEnumeration": EventTypeEnumeration,
       "EventDirectionEnumeration": EventDirectionEnumeration,
       "raritan": raritan,
       "pdu": pdu,
       "traps": traps,
       "rebootStarted": rebootStarted,
       "rebootCompleted": rebootCompleted,
       "userLogin": userLogin,
       "userLogout": userLogout,
       "userAuthenticationFailure": userAuthenticationFailure,
       "userSessionTimeout": userSessionTimeout,
       "userAdded": userAdded,
       "userModified": userModified,
       "userDeleted": userDeleted,
       "groupAdded": groupAdded,
       "groupModified": groupModified,
       "groupDeleted": groupDeleted,
       "deviceUpdateStarted": deviceUpdateStarted,
       "userBlocked": userBlocked,
       "powerControl": powerControl,
       "userPasswordChanged": userPasswordChanged,
       "passwordSettingsChanged": passwordSettingsChanged,
       "firmwareFileDiscarded": firmwareFileDiscarded,
       "firmwareValidationFailed": firmwareValidationFailed,
       "securityViolation": securityViolation,
       "logFileCleared": logFileCleared,
       "thresholdAlarm": thresholdAlarm,
       "outletGroupingConnectivityLost": outletGroupingConnectivityLost,
       "circuitBreakerTripped": circuitBreakerTripped,
       "circuitBreakerRecovered": circuitBreakerRecovered,
       "bulkConfigurationSaved": bulkConfigurationSaved,
       "bulkConfigurationCopied": bulkConfigurationCopied,
       "environmentalSensorsConnectivityLost": environmentalSensorsConnectivityLost,
       "externalOnOffSensorStateChange": externalOnOffSensorStateChange,
       "environmentalSensorsConnectivityRestored": environmentalSensorsConnectivityRestored,
       "voltageMeasurementError": voltageMeasurementError,
       "fipsModeEnabled": fipsModeEnabled,
       "fipsModeDisabled": fipsModeDisabled,
       "managingenvironmentalSensor": managingenvironmentalSensor,
       "unmanagingenvironmentalSensor": unmanagingenvironmentalSensor,
       "ipmiOverLANEnabled": ipmiOverLANEnabled,
       "ipmiOverLANDisabled": ipmiOverLANDisabled,
       "board": board,
       "info": info,
       "firmwareVersion": firmwareVersion,
       "serialNumber": serialNumber,
       "ipAddress": ipAddress,
       "netmask": netmask,
       "gateway": gateway,
       "mac": mac,
       "hardwareRev": hardwareRev,
       "userName": userName,
       "objectName": objectName,
       "objectInstance": objectInstance,
       "targetUser": targetUser,
       "groupName": groupName,
       "imageVersion": imageVersion,
       "sensorDescr": sensorDescr,
       "thresholdDescr": thresholdDescr,
       "thresholdSeverity": thresholdSeverity,
       "thresholdEventType": thresholdEventType,
       "status": status,
       "slaveIpAddress": slaveIpAddress,
       "inputCurrentRating": inputCurrentRating,
       "ratedVoltage": ratedVoltage,
       "ratedPower": ratedPower,
       "outletSwitching": outletSwitching,
       "dataLogging": dataLogging,
       "dataLoggingInterval": dataLoggingInterval,
       "dataCollectionInterval": dataCollectionInterval,
       "outletEnergySupport": outletEnergySupport,
       "currentUnbalanceSupport": currentUnbalanceSupport,
       "externalSensorsZCoordinateUnits": externalSensorsZCoordinateUnits,
       "inlineMeter": inlineMeter,
       "oldSensorState": oldSensorState,
       "externalSensorNumber": externalSensorNumber,
       "sensorIdentificationString": sensorIdentificationString,
       "lastUpgradeStatus": lastUpgradeStatus,
       "lastUpgradeTimestamp": lastUpgradeTimestamp,
       "lastUpgradeErrorDescription": lastUpgradeErrorDescription,
       "powerCIMStatus": powerCIMStatus,
       "measurementsPerLogEntry": measurementsPerLogEntry,
       "psocNumber": psocNumber,
       "altitude": altitude,
       "configureAlerts": configureAlerts,
       "fipsMode": fipsMode,
       "synchronizeWithNTPServer": synchronizeWithNTPServer,
       "useDHCPProvidedNTPServer": useDHCPProvidedNTPServer,
       "primaryNTPServerAddressType": primaryNTPServerAddressType,
       "primaryNTPServerAddress": primaryNTPServerAddress,
       "secondaryNTPServerAddressType": secondaryNTPServerAddressType,
       "secondaryNTPServerAddress": secondaryNTPServerAddress,
       "daylightSavingsTime": daylightSavingsTime,
       "thresholdValue": thresholdValue,
       "sensorValue": sensorValue,
       "ipmiOverLAN": ipmiOverLAN,
       "outlets": outlets,
       "outletCount": outletCount,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletLabel": outletLabel,
       "outletOperationalState": outletOperationalState,
       "outletCurrent": outletCurrent,
       "outletMaxCurrent": outletMaxCurrent,
       "outletVoltage": outletVoltage,
       "outletActivePower": outletActivePower,
       "outletApparentPower": outletApparentPower,
       "outletPowerFactor": outletPowerFactor,
       "outletCurrentUpperWarning": outletCurrentUpperWarning,
       "outletCurrentUpperCritical": outletCurrentUpperCritical,
       "outletCurrentLowerWarning": outletCurrentLowerWarning,
       "outletCurrentLowerCritical": outletCurrentLowerCritical,
       "outletCurrentHysteresis": outletCurrentHysteresis,
       "outletCurrentRating": outletCurrentRating,
       "outletWattHours": outletWattHours,
       "unit": unit,
       "unitReadings": unitReadings,
       "unitCurrent": unitCurrent,
       "unitVoltage": unitVoltage,
       "unitActivePower": unitActivePower,
       "unitApparentPower": unitApparentPower,
       "unitCpuTemp": unitCpuTemp,
       "unitVoltageLowerWarning": unitVoltageLowerWarning,
       "unitVoltageLowerCritical": unitVoltageLowerCritical,
       "unitVoltageUpperWarning": unitVoltageUpperWarning,
       "unitVoltageUpperCritical": unitVoltageUpperCritical,
       "unitCurrentUpperWarning": unitCurrentUpperWarning,
       "unitCurrentUpperCritical": unitCurrentUpperCritical,
       "unitTempLowerWarning": unitTempLowerWarning,
       "unitTempLowerCritical": unitTempLowerCritical,
       "unitTempUpperWarning": unitTempUpperWarning,
       "unitTempUpperCritical": unitTempUpperCritical,
       "currentUnbalance": currentUnbalance,
       "currentUnbalanceUpperWarning": currentUnbalanceUpperWarning,
       "currentUnbalanceUpperCritical": currentUnbalanceUpperCritical,
       "unitOrLineVoltageLowerWarning": unitOrLineVoltageLowerWarning,
       "unitOrLineVoltageLowerCritical": unitOrLineVoltageLowerCritical,
       "unitOrLineVoltageUpperWarning": unitOrLineVoltageUpperWarning,
       "unitOrLineVoltageUpperCritical": unitOrLineVoltageUpperCritical,
       "unitOrLineCurrentUpperWarning": unitOrLineCurrentUpperWarning,
       "unitOrLineCurrentUpperCritical": unitOrLineCurrentUpperCritical,
       "neutralCurrentUpperWarning": neutralCurrentUpperWarning,
       "neutralCurrentUpperCritical": neutralCurrentUpperCritical,
       "unitOrLineCurrentHysteresis": unitOrLineCurrentHysteresis,
       "unitOrLineVoltageHysteresis": unitOrLineVoltageHysteresis,
       "unitTempHysteresis": unitTempHysteresis,
       "currentUnbalanceHysteresis": currentUnbalanceHysteresis,
       "lineCurrents": lineCurrents,
       "lineCurrentCount": lineCurrentCount,
       "lineCurrentTable": lineCurrentTable,
       "lineCurrentEntry": lineCurrentEntry,
       "lineCurrentIndex": lineCurrentIndex,
       "lineCurrentLabel": lineCurrentLabel,
       "lineCurrent": lineCurrent,
       "circuitBreaker": circuitBreaker,
       "circuitBreakerCount": circuitBreakerCount,
       "circuitBreakerTable": circuitBreakerTable,
       "circuitBreakerEntry": circuitBreakerEntry,
       "circuitBreakerIndex": circuitBreakerIndex,
       "circuitBreakerLabel": circuitBreakerLabel,
       "circuitBreakerState": circuitBreakerState,
       "circuitBreakerCurrentRating": circuitBreakerCurrentRating,
       "circuitBreakerCurrent": circuitBreakerCurrent,
       "circuitBreakerCurrentUpperWarning": circuitBreakerCurrentUpperWarning,
       "circuitBreakerCurrentUpperCritical": circuitBreakerCurrentUpperCritical,
       "circuitBreakerCurrentHysteresis": circuitBreakerCurrentHysteresis,
       "lineVoltages": lineVoltages,
       "lineVoltageCount": lineVoltageCount,
       "lineVoltageTable": lineVoltageTable,
       "lineVoltageEntry": lineVoltageEntry,
       "lineVoltageIndex": lineVoltageIndex,
       "lineVoltageLabel": lineVoltageLabel,
       "lineVoltage": lineVoltage,
       "dataLog": dataLog,
       "dataLogCount": dataLogCount,
       "dataLogLatestIndex": dataLogLatestIndex,
       "dataLogTable": dataLogTable,
       "dataLogEntry": dataLogEntry,
       "dataLogIndex": dataLogIndex,
       "dataLogTimeStamp": dataLogTimeStamp,
       "dataLogActivePower": dataLogActivePower,
       "dataLogApparentPower": dataLogApparentPower,
       "dataLogAvgActivePower": dataLogAvgActivePower,
       "dataLogMaxActivePower": dataLogMaxActivePower,
       "dataLogMinActivePower": dataLogMinActivePower,
       "dataLogAvgApparentPower": dataLogAvgApparentPower,
       "dataLogMaxApparentPower": dataLogMaxApparentPower,
       "dataLogMinApparentPower": dataLogMinApparentPower,
       "dataLogOutlet": dataLogOutlet,
       "dataLogOutletTable": dataLogOutletTable,
       "dataLogOutletEntry": dataLogOutletEntry,
       "dataLogOutletIndex": dataLogOutletIndex,
       "dataLogOutletCurrent": dataLogOutletCurrent,
       "dataLogOutletVoltage": dataLogOutletVoltage,
       "dataLogOutletPowerFactor": dataLogOutletPowerFactor,
       "dataLogOutletOnTime": dataLogOutletOnTime,
       "dataLogOutletWattHours": dataLogOutletWattHours,
       "dataLogAvgOutletCurrent": dataLogAvgOutletCurrent,
       "dataLogMaxOutletCurrent": dataLogMaxOutletCurrent,
       "dataLogMinOutletCurrent": dataLogMinOutletCurrent,
       "dataLogAvgOutletVoltage": dataLogAvgOutletVoltage,
       "dataLogMaxOutletVoltage": dataLogMaxOutletVoltage,
       "dataLogMinOutletVoltage": dataLogMinOutletVoltage,
       "dataLogAvgOutletPowerFactor": dataLogAvgOutletPowerFactor,
       "dataLogMaxOutletPowerFactor": dataLogMaxOutletPowerFactor,
       "dataLogMinOutletPowerFactor": dataLogMinOutletPowerFactor,
       "dataLogAvgOutletWattHours": dataLogAvgOutletWattHours,
       "dataLogMaxOutletWattHours": dataLogMaxOutletWattHours,
       "dataLogMinOutletWattHours": dataLogMinOutletWattHours,
       "dataLogInlet": dataLogInlet,
       "dataLogInletTable": dataLogInletTable,
       "dataLogInletEntry": dataLogInletEntry,
       "dataLogInletIndex": dataLogInletIndex,
       "dataLogInletCurrentUnbalance": dataLogInletCurrentUnbalance,
       "dataLogInletActivePower": dataLogInletActivePower,
       "dataLogInletApparentPower": dataLogInletApparentPower,
       "dataLogInletActiveEnergy": dataLogInletActiveEnergy,
       "dataLogAvgInletCurrentUnbalance": dataLogAvgInletCurrentUnbalance,
       "dataLogMaxInletCurrentUnbalance": dataLogMaxInletCurrentUnbalance,
       "dataLogMinInletCurrentUnbalance": dataLogMinInletCurrentUnbalance,
       "dataLogAvgInletActivePower": dataLogAvgInletActivePower,
       "dataLogMaxInletActivePower": dataLogMaxInletActivePower,
       "dataLogMinInletActivePower": dataLogMinInletActivePower,
       "dataLogAvgInletApparentPower": dataLogAvgInletApparentPower,
       "dataLogMaxInletApparentPower": dataLogMaxInletApparentPower,
       "dataLogMinInletApparentPower": dataLogMinInletApparentPower,
       "dataLogAvgInletActiveEnergy": dataLogAvgInletActiveEnergy,
       "dataLogMaxInletActiveEnergy": dataLogMaxInletActiveEnergy,
       "dataLogMinInletActiveEnergy": dataLogMinInletActiveEnergy,
       "dataLogInletPole": dataLogInletPole,
       "dataLogInletPoleTable": dataLogInletPoleTable,
       "dataLogInletPoleEntry": dataLogInletPoleEntry,
       "dataLogInletPoleIndex": dataLogInletPoleIndex,
       "dataLogInletPoleCurrent": dataLogInletPoleCurrent,
       "dataLogInletPoleVoltage": dataLogInletPoleVoltage,
       "dataLogAvgInletPoleCurrent": dataLogAvgInletPoleCurrent,
       "dataLogMaxInletPoleCurrent": dataLogMaxInletPoleCurrent,
       "dataLogMinInletPoleCurrent": dataLogMinInletPoleCurrent,
       "dataLogAvgInletPoleVoltage": dataLogAvgInletPoleVoltage,
       "dataLogMaxInletPoleVoltage": dataLogMaxInletPoleVoltage,
       "dataLogMinInletPoleVoltage": dataLogMinInletPoleVoltage,
       "dataLogAvgInletPoleActivePower": dataLogAvgInletPoleActivePower,
       "dataLogMaxInletPoleActivePower": dataLogMaxInletPoleActivePower,
       "dataLogMinInletPoleActivePower": dataLogMinInletPoleActivePower,
       "dataLogAvgInletPoleApparentPower": dataLogAvgInletPoleApparentPower,
       "dataLogMaxInletPoleApparentPower": dataLogMaxInletPoleApparentPower,
       "dataLogMinInletPoleApparentPower": dataLogMinInletPoleApparentPower,
       "dataLogAvgInletPoleActiveEnergy": dataLogAvgInletPoleActiveEnergy,
       "dataLogMaxInletPoleActiveEnergy": dataLogMaxInletPoleActiveEnergy,
       "dataLogMinInletPoleActiveEnergy": dataLogMinInletPoleActiveEnergy,
       "dataLogInputLine": dataLogInputLine,
       "dataLogInputLineTable": dataLogInputLineTable,
       "dataLogInputLineEntry": dataLogInputLineEntry,
       "dataLogInputLineIndex": dataLogInputLineIndex,
       "dataLogInputLineCurrent": dataLogInputLineCurrent,
       "dataLogInputLineVoltage": dataLogInputLineVoltage,
       "dataLogCircuitBreaker": dataLogCircuitBreaker,
       "dataLogCircuitBreakerTable": dataLogCircuitBreakerTable,
       "dataLogCircuitBreakerEntry": dataLogCircuitBreakerEntry,
       "dataLogCircuitBreakerIndex": dataLogCircuitBreakerIndex,
       "dataLogCircuitBreakerCurrent": dataLogCircuitBreakerCurrent,
       "dataLogAvgCircuitBreakerCurrent": dataLogAvgCircuitBreakerCurrent,
       "dataLogMaxCircuitBreakerCurrent": dataLogMaxCircuitBreakerCurrent,
       "dataLogMinCircuitBreakerCurrent": dataLogMinCircuitBreakerCurrent,
       "dataLogExternalSensor": dataLogExternalSensor,
       "dataLogExternalSensorTable": dataLogExternalSensorTable,
       "dataLogExternalSensorEntry": dataLogExternalSensorEntry,
       "dataLogExternalSensorIndex": dataLogExternalSensorIndex,
       "dataLogExternalSensorChanged": dataLogExternalSensorChanged,
       "dataLogExternalSensorState": dataLogExternalSensorState,
       "dataLogAvgExternalSensorValue": dataLogAvgExternalSensorValue,
       "dataLogMaxExternalSensorValue": dataLogMaxExternalSensorValue,
       "dataLogMinExternalSensorValue": dataLogMinExternalSensorValue,
       "inlets": inlets,
       "inletCount": inletCount,
       "inletTable": inletTable,
       "inletEntry": inletEntry,
       "inletIndex": inletIndex,
       "inletPoleCount": inletPoleCount,
       "inletCurrentRating": inletCurrentRating,
       "inletCurrent": inletCurrent,
       "inletVoltage": inletVoltage,
       "inletActivePower": inletActivePower,
       "inletApparentPower": inletApparentPower,
       "inletPowerFactor": inletPowerFactor,
       "inletActiveEnergy": inletActiveEnergy,
       "inletCurrentUnbalance": inletCurrentUnbalance,
       "inletCurrentUpperWarning": inletCurrentUpperWarning,
       "inletCurrentUpperCritical": inletCurrentUpperCritical,
       "inletCurrentLowerWarning": inletCurrentLowerWarning,
       "inletCurrentLowerCritical": inletCurrentLowerCritical,
       "inletVoltageUpperWarning": inletVoltageUpperWarning,
       "inletVoltageUpperCritical": inletVoltageUpperCritical,
       "inletVoltageLowerWarning": inletVoltageLowerWarning,
       "inletVoltageLowerCritical": inletVoltageLowerCritical,
       "inletCurrentUnbalanceUpperCritical": inletCurrentUnbalanceUpperCritical,
       "inletCurrentUnbalanceUpperWarning": inletCurrentUnbalanceUpperWarning,
       "inletCurrentHysteresis": inletCurrentHysteresis,
       "inletVoltageHysteresis": inletVoltageHysteresis,
       "inletCurrentUnbalanceHysteresis": inletCurrentUnbalanceHysteresis,
       "inletPole": inletPole,
       "inletPoleTable": inletPoleTable,
       "inletPoleEntry": inletPoleEntry,
       "inletPoleIndex": inletPoleIndex,
       "inletPoleLabel": inletPoleLabel,
       "inletPoleCurrent": inletPoleCurrent,
       "inletPoleVoltage": inletPoleVoltage,
       "inletPoleMaxCurrent": inletPoleMaxCurrent,
       "inletPoleActivePower": inletPoleActivePower,
       "inletPoleApparentPower": inletPoleApparentPower,
       "inletPolePowerFactor": inletPolePowerFactor,
       "inletPoleActiveEnergy": inletPoleActiveEnergy,
       "environmental": environmental,
       "tempSensorCount": tempSensorCount,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorLabel": tempSensorLabel,
       "temperature": temperature,
       "tempLowerWarning": tempLowerWarning,
       "tempUpperWarning": tempUpperWarning,
       "tempLowerCritical": tempLowerCritical,
       "tempUpperCritical": tempUpperCritical,
       "tempXCoordinate": tempXCoordinate,
       "tempYCoordinate": tempYCoordinate,
       "tempZCoordinate": tempZCoordinate,
       "humiditySensorCount": humiditySensorCount,
       "humiditySensorTable": humiditySensorTable,
       "humiditySensorEntry": humiditySensorEntry,
       "humiditySensorIndex": humiditySensorIndex,
       "humiditySensorLabel": humiditySensorLabel,
       "humidity": humidity,
       "humidityLowerWarning": humidityLowerWarning,
       "humidityUpperWarning": humidityUpperWarning,
       "humidityLowerCritical": humidityLowerCritical,
       "humidityUpperCritical": humidityUpperCritical,
       "humidityXCoordinate": humidityXCoordinate,
       "humidityYCoordinate": humidityYCoordinate,
       "humidityZCoordinate": humidityZCoordinate,
       "externalSensors": externalSensors,
       "externalSensorCount": externalSensorCount,
       "reorderexternalSensorTableEntries": reorderexternalSensorTableEntries,
       "externalSensorTable": externalSensorTable,
       "externalSensorEntry": externalSensorEntry,
       "sensorID": sensorID,
       "externalSensorType": externalSensorType,
       "externalSensorSerialNumber": externalSensorSerialNumber,
       "externalSensorName": externalSensorName,
       "externalSensorChannelNumber": externalSensorChannelNumber,
       "externalSensorXCoordinate": externalSensorXCoordinate,
       "externalSensorYCoordinate": externalSensorYCoordinate,
       "externalSensorZCoordinate": externalSensorZCoordinate,
       "externalBinarySensorSubtype": externalBinarySensorSubtype,
       "externalSensorUnits": externalSensorUnits,
       "externalSensorDecimalDigits": externalSensorDecimalDigits,
       "externalSensorLowerCriticalThreshold": externalSensorLowerCriticalThreshold,
       "externalSensorLowerWarningThreshold": externalSensorLowerWarningThreshold,
       "externalSensorUpperCriticalThreshold": externalSensorUpperCriticalThreshold,
       "externalSensorUpperWarningThreshold": externalSensorUpperWarningThreshold,
       "externalSensorHysteresis": externalSensorHysteresis,
       "externalSensorState": externalSensorState,
       "externalSensorValue": externalSensorValue,
       "conformance": conformance,
       "compliances": compliances,
       "compliance": compliance,
       "complianceRev1": complianceRev1,
       "complianceRev2": complianceRev2,
       "complianceRev3": complianceRev3,
       "complianceRev4": complianceRev4,
       "complianceRev5": complianceRev5,
       "groups": groups,
       "infoGroup": infoGroup,
       "outletsGroup": outletsGroup,
       "unitSensorsGroup": unitSensorsGroup,
       "externalTemperatureGroup": externalTemperatureGroup,
       "externalHumidityGroup": externalHumidityGroup,
       "trapsGroup": trapsGroup,
       "lineCurrentGroup": lineCurrentGroup,
       "circuitBreakerGroup": circuitBreakerGroup,
       "lineVoltageGroup": lineVoltageGroup,
       "unitSensorsGroupRev": unitSensorsGroupRev,
       "dataLogGroup": dataLogGroup,
       "inletPoleGroup": inletPoleGroup,
       "inletsGroup": inletsGroup,
       "dataLogGroupRev": dataLogGroupRev,
       "unitSensorsGroupRev2": unitSensorsGroupRev2,
       "externalSensorsGroup": externalSensorsGroup,
       "dataLogGroupRev2": dataLogGroupRev2,
       "infoGroupRev2": infoGroupRev2}
)
