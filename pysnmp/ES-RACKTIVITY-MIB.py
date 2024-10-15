# SNMP MIB module (ES-RACKTIVITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ES-RACKTIVITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:40 2024
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

esRACKTIVITYMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9)
)
esRACKTIVITYMIB.setRevisions(
        ("2014-04-23 03:33",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Version(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class Utenth(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class Uhundredth(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class Uthousandth(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-3"


class Stenth(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class Shundredth(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class Sthousandth(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"


class EVENTFLAGS(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sNMPTrapOff", 0),
          ("sNMPTrapOn", 1))
    )



class CURPORTSTATE(Integer32, TextualConvention):
    status = "current"
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
        *(("portOff", 0),
          ("portOff1", 2),
          ("portOff2", 4),
          ("portOff3", 6),
          ("portOffWithDelayOn", 16),
          ("portOffWithDelayOn1", 18),
          ("portOffWithDelayOn2", 20),
          ("portOffWithDelayOn3", 22),
          ("portOffWithError", 8),
          ("portOffWithError1", 10),
          ("portOffWithError2", 12),
          ("portOffWithError3", 14),
          ("portOnNoWarning", 1),
          ("portOnNoWarning1", 9),
          ("portOnNoWarning2", 17),
          ("portOnWithWarnCurrentAndPower1", 15),
          ("portOnWithWarnCurrentAndPower2", 23),
          ("portOnWithWarningCurrent", 3),
          ("portOnWithWarningCurrent1", 11),
          ("portOnWithWarningCurrent2", 19),
          ("portOnWithWarningCurrentAndPower", 7),
          ("portOnWithWarningPower", 5),
          ("portOnWithWarningPower1", 13),
          ("portOnWithWarningPower2", 21))
    )



# MIB Managed Objects in the order of their OIDs

_Racktivity_ObjectIdentity = ObjectIdentity
racktivity = _Racktivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097)
)
_RacktivityNotif_ObjectIdentity = ObjectIdentity
racktivityNotif = _RacktivityNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0)
)
_EsRacktivityConformance_ObjectIdentity = ObjectIdentity
esRacktivityConformance = _EsRacktivityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 2)
)
_EsRacktivityMIBGroups_ObjectIdentity = ObjectIdentity
esRacktivityMIBGroups = _EsRacktivityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 2, 1)
)
_EsRacktivityMIBCompliances_ObjectIdentity = ObjectIdentity
esRacktivityMIBCompliances = _EsRacktivityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 2, 2)
)
_EsnModule_ObjectIdentity = ObjectIdentity
esnModule = _EsnModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65)
)
_EESNTable_Object = MibTable
eESNTable = _EESNTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1)
)
if mibBuilder.loadTexts:
    eESNTable.setStatus("current")
_EESNEntry_Object = MibTableRow
eESNEntry = _EESNEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1)
)
eESNEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "esnModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "esnIndex"),
)
if mibBuilder.loadTexts:
    eESNEntry.setStatus("current")
_AGeneralModuleStatus_Type = Unsigned32
_AGeneralModuleStatus_Object = MibTableColumn
aGeneralModuleStatus = _AGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 1),
    _AGeneralModuleStatus_Type()
)
aGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aGeneralModuleStatus.setStatus("current")
_ASpecificModuleStatus_Type = Unsigned32
_ASpecificModuleStatus_Object = MibTableColumn
aSpecificModuleStatus = _ASpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 2),
    _ASpecificModuleStatus_Type()
)
aSpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aSpecificModuleStatus.setStatus("current")
_ACurrentTime_Type = TimeTicks
_ACurrentTime_Object = MibTableColumn
aCurrentTime = _ACurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 3),
    _ACurrentTime_Type()
)
aCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    aCurrentTime.setUnits("UNIX")
_AVoltage_Type = Uhundredth
_AVoltage_Object = MibTableColumn
aVoltage = _AVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 4),
    _AVoltage_Type()
)
aVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aVoltage.setStatus("current")
if mibBuilder.loadTexts:
    aVoltage.setUnits("V")
_AStatePortCur_Type = CURPORTSTATE
_AStatePortCur_Object = MibTableColumn
aStatePortCur = _AStatePortCur_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 8),
    _AStatePortCur_Type()
)
aStatePortCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aStatePortCur.setStatus("current")
_ATemperature_Type = Utenth
_ATemperature_Object = MibTableColumn
aTemperature = _ATemperature_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 11),
    _ATemperature_Type()
)
aTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aTemperature.setStatus("current")
if mibBuilder.loadTexts:
    aTemperature.setUnits("K")
_AHumidity_Type = Utenth
_AHumidity_Object = MibTableColumn
aHumidity = _AHumidity_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 12),
    _AHumidity_Type()
)
aHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aHumidity.setStatus("current")
if mibBuilder.loadTexts:
    aHumidity.setUnits("RH")
_AAirflow_Type = Utenth
_AAirflow_Object = MibTableColumn
aAirflow = _AAirflow_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 23),
    _AAirflow_Type()
)
aAirflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aAirflow.setStatus("current")
if mibBuilder.loadTexts:
    aAirflow.setUnits("m/s")


class _ADewPoint_Type(Utenth):
    """Custom type aDewPoint based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ADewPoint_Type.__name__ = "Utenth"
_ADewPoint_Object = MibTableColumn
aDewPoint = _ADewPoint_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 25),
    _ADewPoint_Type()
)
aDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    aDewPoint.setUnits("K")
_APressure_Type = Utenth
_APressure_Object = MibTableColumn
aPressure = _APressure_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 26),
    _APressure_Type()
)
aPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aPressure.setStatus("current")
if mibBuilder.loadTexts:
    aPressure.setUnits("hPa")
_AAnalogueInput_Type = Unsigned32
_AAnalogueInput_Object = MibTableColumn
aAnalogueInput = _AAnalogueInput_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 27),
    _AAnalogueInput_Type()
)
aAnalogueInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aAnalogueInput.setStatus("current")
if mibBuilder.loadTexts:
    aAnalogueInput.setUnits("mV")
_AWaterleak_Type = Unsigned32
_AWaterleak_Object = MibTableColumn
aWaterleak = _AWaterleak_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 28),
    _AWaterleak_Type()
)
aWaterleak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aWaterleak.setStatus("current")
_AMotionDetected_Type = Unsigned32
_AMotionDetected_Object = MibTableColumn
aMotionDetected = _AMotionDetected_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 29),
    _AMotionDetected_Type()
)
aMotionDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMotionDetected.setStatus("current")


class _AIOPort_Type(Unsigned32):
    """Custom type aIOPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AIOPort_Type.__name__ = "Unsigned32"
_AIOPort_Object = MibTableColumn
aIOPort = _AIOPort_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 30),
    _AIOPort_Type()
)
aIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aIOPort.setStatus("current")


class _AHighCurrent_Type(Stenth):
    """Custom type aHighCurrent based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_AHighCurrent_Type.__name__ = "Stenth"
_AHighCurrent_Object = MibTableColumn
aHighCurrent = _AHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 41),
    _AHighCurrent_Type()
)
aHighCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aHighCurrent.setStatus("current")
if mibBuilder.loadTexts:
    aHighCurrent.setUnits("A")


class _AHighPower_Type(Shundredth):
    """Custom type aHighPower based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_AHighPower_Type.__name__ = "Shundredth"
_AHighPower_Object = MibTableColumn
aHighPower = _AHighPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 43),
    _AHighPower_Type()
)
aHighPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aHighPower.setStatus("current")
if mibBuilder.loadTexts:
    aHighPower.setUnits("kW")
_AModuleName_Type = DisplayString
_AModuleName_Object = MibTableColumn
aModuleName = _AModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10001),
    _AModuleName_Type()
)
aModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aModuleName.setStatus("current")
_AFirmwareVersion_Type = Version
_AFirmwareVersion_Object = MibTableColumn
aFirmwareVersion = _AFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10002),
    _AFirmwareVersion_Type()
)
aFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFirmwareVersion.setStatus("current")
_AHardwareVersion_Type = Version
_AHardwareVersion_Object = MibTableColumn
aHardwareVersion = _AHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10003),
    _AHardwareVersion_Type()
)
aHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aHardwareVersion.setStatus("current")
_AFirmwareID_Type = DisplayString
_AFirmwareID_Object = MibTableColumn
aFirmwareID = _AFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10004),
    _AFirmwareID_Type()
)
aFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aFirmwareID.setStatus("current")
_AHardwareID_Type = DisplayString
_AHardwareID_Object = MibTableColumn
aHardwareID = _AHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10005),
    _AHardwareID_Type()
)
aHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aHardwareID.setStatus("current")


class _ADisplayTimeOn_Type(Unsigned32):
    """Custom type aDisplayTimeOn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ADisplayTimeOn_Type.__name__ = "Unsigned32"
_ADisplayTimeOn_Object = MibTableColumn
aDisplayTimeOn = _ADisplayTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10032),
    _ADisplayTimeOn_Type()
)
aDisplayTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aDisplayTimeOn.setStatus("current")
if mibBuilder.loadTexts:
    aDisplayTimeOn.setUnits("min")


class _AMaxVoltageWarning_Type(Uhundredth):
    """Custom type aMaxVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMaxVoltageWarning_Type.__name__ = "Uhundredth"
_AMaxVoltageWarning_Object = MibTableColumn
aMaxVoltageWarning = _AMaxVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10047),
    _AMaxVoltageWarning_Type()
)
aMaxVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMaxVoltageWarning.setUnits("V")


class _AMinVoltageWarning_Type(Uhundredth):
    """Custom type aMinVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMinVoltageWarning_Type.__name__ = "Uhundredth"
_AMinVoltageWarning_Object = MibTableColumn
aMinVoltageWarning = _AMinVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10049),
    _AMinVoltageWarning_Type()
)
aMinVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMinVoltageWarning.setUnits("V")


class _AMinTemperatureWarning_Type(Utenth):
    """Custom type aMinTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_AMinTemperatureWarning_Type.__name__ = "Utenth"
_AMinTemperatureWarning_Object = MibTableColumn
aMinTemperatureWarning = _AMinTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10052),
    _AMinTemperatureWarning_Type()
)
aMinTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMinTemperatureWarning.setUnits("K")


class _AMaxTemperatureWarning_Type(Utenth):
    """Custom type aMaxTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_AMaxTemperatureWarning_Type.__name__ = "Utenth"
_AMaxTemperatureWarning_Object = MibTableColumn
aMaxTemperatureWarning = _AMaxTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10053),
    _AMaxTemperatureWarning_Type()
)
aMaxTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMaxTemperatureWarning.setUnits("K")


class _AMinHumidityWarning_Type(Utenth):
    """Custom type aMinHumidityWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AMinHumidityWarning_Type.__name__ = "Utenth"
_AMinHumidityWarning_Object = MibTableColumn
aMinHumidityWarning = _AMinHumidityWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10054),
    _AMinHumidityWarning_Type()
)
aMinHumidityWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinHumidityWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMinHumidityWarning.setUnits("RH")


class _AMaxHumidityWarning_Type(Utenth):
    """Custom type aMaxHumidityWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AMaxHumidityWarning_Type.__name__ = "Utenth"
_AMaxHumidityWarning_Object = MibTableColumn
aMaxHumidityWarning = _AMaxHumidityWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10055),
    _AMaxHumidityWarning_Type()
)
aMaxHumidityWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxHumidityWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMaxHumidityWarning.setUnits("RH")
_ACurrentWarningEvent_Type = EVENTFLAGS
_ACurrentWarningEvent_Object = MibTableColumn
aCurrentWarningEvent = _ACurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10078),
    _ACurrentWarningEvent_Type()
)
aCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aCurrentWarningEvent.setStatus("current")
_APowerWarningEvent_Type = EVENTFLAGS
_APowerWarningEvent_Object = MibTableColumn
aPowerWarningEvent = _APowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10080),
    _APowerWarningEvent_Type()
)
aPowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aPowerWarningEvent.setStatus("current")
_AVoltageWarningEvent_Type = EVENTFLAGS
_AVoltageWarningEvent_Object = MibTableColumn
aVoltageWarningEvent = _AVoltageWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10086),
    _AVoltageWarningEvent_Type()
)
aVoltageWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aVoltageWarningEvent.setStatus("current")
_ATemperatureWarningEvent_Type = EVENTFLAGS
_ATemperatureWarningEvent_Object = MibTableColumn
aTemperatureWarningEvent = _ATemperatureWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10087),
    _ATemperatureWarningEvent_Type()
)
aTemperatureWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aTemperatureWarningEvent.setStatus("current")
_AHumidityWarningEvent_Type = EVENTFLAGS
_AHumidityWarningEvent_Object = MibTableColumn
aHumidityWarningEvent = _AHumidityWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10088),
    _AHumidityWarningEvent_Type()
)
aHumidityWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aHumidityWarningEvent.setStatus("current")


class _ADewPointWarning_Type(Utenth):
    """Custom type aDewPointWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ADewPointWarning_Type.__name__ = "Utenth"
_ADewPointWarning_Object = MibTableColumn
aDewPointWarning = _ADewPointWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10092),
    _ADewPointWarning_Type()
)
aDewPointWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aDewPointWarning.setStatus("current")
if mibBuilder.loadTexts:
    aDewPointWarning.setUnits("K")
_ADewPointWarningEvent_Type = EVENTFLAGS
_ADewPointWarningEvent_Object = MibTableColumn
aDewPointWarningEvent = _ADewPointWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10093),
    _ADewPointWarningEvent_Type()
)
aDewPointWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aDewPointWarningEvent.setStatus("current")
_ADewPointViolationEvent_Type = EVENTFLAGS
_ADewPointViolationEvent_Object = MibTableColumn
aDewPointViolationEvent = _ADewPointViolationEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10094),
    _ADewPointViolationEvent_Type()
)
aDewPointViolationEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aDewPointViolationEvent.setStatus("current")
_APressureWarningEvent_Type = EVENTFLAGS
_APressureWarningEvent_Object = MibTableColumn
aPressureWarningEvent = _APressureWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10095),
    _APressureWarningEvent_Type()
)
aPressureWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aPressureWarningEvent.setStatus("current")


class _AMinPressureWarning_Type(Utenth):
    """Custom type aMinPressureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMinPressureWarning_Type.__name__ = "Utenth"
_AMinPressureWarning_Object = MibTableColumn
aMinPressureWarning = _AMinPressureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10096),
    _AMinPressureWarning_Type()
)
aMinPressureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinPressureWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMinPressureWarning.setUnits("hPa")


class _AMaxPressureWarning_Type(Utenth):
    """Custom type aMaxPressureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMaxPressureWarning_Type.__name__ = "Utenth"
_AMaxPressureWarning_Object = MibTableColumn
aMaxPressureWarning = _AMaxPressureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10097),
    _AMaxPressureWarning_Type()
)
aMaxPressureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxPressureWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMaxPressureWarning.setUnits("hPa")


class _ADisplayBrightness_Type(Unsigned32):
    """Custom type aDisplayBrightness based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ADisplayBrightness_Type.__name__ = "Unsigned32"
_ADisplayBrightness_Object = MibTableColumn
aDisplayBrightness = _ADisplayBrightness_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10098),
    _ADisplayBrightness_Type()
)
aDisplayBrightness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aDisplayBrightness.setStatus("current")


class _AMotionSensitivity_Type(Unsigned32):
    """Custom type aMotionSensitivity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AMotionSensitivity_Type.__name__ = "Unsigned32"
_AMotionSensitivity_Object = MibTableColumn
aMotionSensitivity = _AMotionSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10107),
    _AMotionSensitivity_Type()
)
aMotionSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMotionSensitivity.setStatus("current")
_AExternalSensorLabel_Type = DisplayString
_AExternalSensorLabel_Object = MibTableColumn
aExternalSensorLabel = _AExternalSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10109),
    _AExternalSensorLabel_Type()
)
aExternalSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aExternalSensorLabel.setStatus("current")
_ARelayLabel_Type = DisplayString
_ARelayLabel_Object = MibTableColumn
aRelayLabel = _ARelayLabel_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10110),
    _ARelayLabel_Type()
)
aRelayLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRelayLabel.setStatus("current")


class _AMinAnalogueInputWarning_Type(Unsigned32):
    """Custom type aMinAnalogueInputWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMinAnalogueInputWarning_Type.__name__ = "Unsigned32"
_AMinAnalogueInputWarning_Object = MibTableColumn
aMinAnalogueInputWarning = _AMinAnalogueInputWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10111),
    _AMinAnalogueInputWarning_Type()
)
aMinAnalogueInputWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinAnalogueInputWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMinAnalogueInputWarning.setUnits("mV")


class _AMaxAnalogueInputWarning_Type(Unsigned32):
    """Custom type aMaxAnalogueInputWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMaxAnalogueInputWarning_Type.__name__ = "Unsigned32"
_AMaxAnalogueInputWarning_Object = MibTableColumn
aMaxAnalogueInputWarning = _AMaxAnalogueInputWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10112),
    _AMaxAnalogueInputWarning_Type()
)
aMaxAnalogueInputWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxAnalogueInputWarning.setStatus("current")


class _AWaterleakWarning_Type(Unsigned32):
    """Custom type aWaterleakWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AWaterleakWarning_Type.__name__ = "Unsigned32"
_AWaterleakWarning_Object = MibTableColumn
aWaterleakWarning = _AWaterleakWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10113),
    _AWaterleakWarning_Type()
)
aWaterleakWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aWaterleakWarning.setStatus("current")


class _AMinAirflowWarning_Type(Unsigned32):
    """Custom type aMinAirflowWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMinAirflowWarning_Type.__name__ = "Unsigned32"
_AMinAirflowWarning_Object = MibTableColumn
aMinAirflowWarning = _AMinAirflowWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10114),
    _AMinAirflowWarning_Type()
)
aMinAirflowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinAirflowWarning.setStatus("current")


class _AMaxAirflowWarning_Type(Unsigned32):
    """Custom type aMaxAirflowWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AMaxAirflowWarning_Type.__name__ = "Unsigned32"
_AMaxAirflowWarning_Object = MibTableColumn
aMaxAirflowWarning = _AMaxAirflowWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10115),
    _AMaxAirflowWarning_Type()
)
aMaxAirflowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxAirflowWarning.setStatus("current")
_AAnalogueInputWarningEvent_Type = EVENTFLAGS
_AAnalogueInputWarningEvent_Object = MibTableColumn
aAnalogueInputWarningEvent = _AAnalogueInputWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10116),
    _AAnalogueInputWarningEvent_Type()
)
aAnalogueInputWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aAnalogueInputWarningEvent.setStatus("current")
_AWaterleakWarningEvent_Type = EVENTFLAGS
_AWaterleakWarningEvent_Object = MibTableColumn
aWaterleakWarningEvent = _AWaterleakWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10117),
    _AWaterleakWarningEvent_Type()
)
aWaterleakWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aWaterleakWarningEvent.setStatus("current")
_AAirflowWarningEvent_Type = EVENTFLAGS
_AAirflowWarningEvent_Object = MibTableColumn
aAirflowWarningEvent = _AAirflowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10118),
    _AAirflowWarningEvent_Type()
)
aAirflowWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aAirflowWarningEvent.setStatus("current")
_ARelayAssertActionEvent_Type = EVENTFLAGS
_ARelayAssertActionEvent_Object = MibTableColumn
aRelayAssertActionEvent = _ARelayAssertActionEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10119),
    _ARelayAssertActionEvent_Type()
)
aRelayAssertActionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRelayAssertActionEvent.setStatus("current")
_ARelayDeassertActionEvent_Type = EVENTFLAGS
_ARelayDeassertActionEvent_Object = MibTableColumn
aRelayDeassertActionEvent = _ARelayDeassertActionEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10120),
    _ARelayDeassertActionEvent_Type()
)
aRelayDeassertActionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aRelayDeassertActionEvent.setStatus("current")


class _AMotionWarning_Type(Unsigned32):
    """Custom type aMotionWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AMotionWarning_Type.__name__ = "Unsigned32"
_AMotionWarning_Object = MibTableColumn
aMotionWarning = _AMotionWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10141),
    _AMotionWarning_Type()
)
aMotionWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMotionWarning.setStatus("current")
_AMotionWarningEvent_Type = EVENTFLAGS
_AMotionWarningEvent_Object = MibTableColumn
aMotionWarningEvent = _AMotionWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10149),
    _AMotionWarningEvent_Type()
)
aMotionWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMotionWarningEvent.setStatus("current")
_ADeviceID_Type = DisplayString
_ADeviceID_Object = MibTableColumn
aDeviceID = _ADeviceID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10150),
    _ADeviceID_Type()
)
aDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aDeviceID.setStatus("current")
_ADeviceVersion_Type = Version
_ADeviceVersion_Object = MibTableColumn
aDeviceVersion = _ADeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10151),
    _ADeviceVersion_Type()
)
aDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aDeviceVersion.setStatus("current")
_ASysName_Type = DisplayString
_ASysName_Object = MibTableColumn
aSysName = _ASysName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10152),
    _ASysName_Type()
)
aSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aSysName.setStatus("current")


class _AMaxHighCurrentWarning_Type(Stenth):
    """Custom type aMaxHighCurrentWarning based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_AMaxHighCurrentWarning_Type.__name__ = "Stenth"
_AMaxHighCurrentWarning_Object = MibTableColumn
aMaxHighCurrentWarning = _AMaxHighCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10165),
    _AMaxHighCurrentWarning_Type()
)
aMaxHighCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxHighCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMaxHighCurrentWarning.setUnits("A")


class _AMinHighCurrentWarning_Type(Stenth):
    """Custom type aMinHighCurrentWarning based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_AMinHighCurrentWarning_Type.__name__ = "Stenth"
_AMinHighCurrentWarning_Object = MibTableColumn
aMinHighCurrentWarning = _AMinHighCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10176),
    _AMinHighCurrentWarning_Type()
)
aMinHighCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinHighCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMinHighCurrentWarning.setUnits("A")


class _AMinHighPowerWarning_Type(Shundredth):
    """Custom type aMinHighPowerWarning based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_AMinHighPowerWarning_Type.__name__ = "Shundredth"
_AMinHighPowerWarning_Object = MibTableColumn
aMinHighPowerWarning = _AMinHighPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10177),
    _AMinHighPowerWarning_Type()
)
aMinHighPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMinHighPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMinHighPowerWarning.setUnits("kW")


class _AMaxHighPowerWarning_Type(Shundredth):
    """Custom type aMaxHighPowerWarning based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_AMaxHighPowerWarning_Type.__name__ = "Shundredth"
_AMaxHighPowerWarning_Object = MibTableColumn
aMaxHighPowerWarning = _AMaxHighPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10178),
    _AMaxHighPowerWarning_Type()
)
aMaxHighPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMaxHighPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    aMaxHighPowerWarning.setUnits("kW")
_AIOPortWarningEvent_Type = EVENTFLAGS
_AIOPortWarningEvent_Object = MibTableColumn
aIOPortWarningEvent = _AIOPortWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 10192),
    _AIOPortWarningEvent_Type()
)
aIOPortWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aIOPortWarningEvent.setStatus("current")


class _EsnIndex_Type(Integer32):
    """Custom type esnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EsnIndex_Type.__name__ = "Integer32"
_EsnIndex_Object = MibTableColumn
esnIndex = _EsnIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 65537),
    _EsnIndex_Type()
)
esnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esnIndex.setStatus("current")


class _EsnModuleIndex_Type(Integer32):
    """Custom type esnModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EsnModuleIndex_Type.__name__ = "Integer32"
_EsnModuleIndex_Object = MibTableColumn
esnModuleIndex = _EsnModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 65, 1, 1, 65538),
    _EsnModuleIndex_Type()
)
esnModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esnModuleIndex.setStatus("current")
_ThreephasepowerModule_ObjectIdentity = ObjectIdentity
threephasepowerModule = _ThreephasepowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 66)
)
_EThreePhasePowerTable_Object = MibTable
eThreePhasePowerTable = _EThreePhasePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 66, 1)
)
if mibBuilder.loadTexts:
    eThreePhasePowerTable.setStatus("current")
_EThreePhasePowerEntry_Object = MibTableRow
eThreePhasePowerEntry = _EThreePhasePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 66, 1, 1)
)
eThreePhasePowerEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "threephasepowerModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "threephasepowerIndex"),
)
if mibBuilder.loadTexts:
    eThreePhasePowerEntry.setStatus("current")


class _ThreephasepowerIndex_Type(Integer32):
    """Custom type threephasepowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ThreephasepowerIndex_Type.__name__ = "Integer32"
_ThreephasepowerIndex_Object = MibTableColumn
threephasepowerIndex = _ThreephasepowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 66, 1, 1, 65537),
    _ThreephasepowerIndex_Type()
)
threephasepowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    threephasepowerIndex.setStatus("current")


class _ThreephasepowerModuleIndex_Type(Integer32):
    """Custom type threephasepowerModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ThreephasepowerModuleIndex_Type.__name__ = "Integer32"
_ThreephasepowerModuleIndex_Object = MibTableColumn
threephasepowerModuleIndex = _ThreephasepowerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 66, 1, 1, 65538),
    _ThreephasepowerModuleIndex_Type()
)
threephasepowerModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    threephasepowerModuleIndex.setStatus("current")
_DisplaymoduleModule_ObjectIdentity = ObjectIdentity
displaymoduleModule = _DisplaymoduleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68)
)
_EDisplayModuleTable_Object = MibTable
eDisplayModuleTable = _EDisplayModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1)
)
if mibBuilder.loadTexts:
    eDisplayModuleTable.setStatus("current")
_EDisplayModuleEntry_Object = MibTableRow
eDisplayModuleEntry = _EDisplayModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1)
)
eDisplayModuleEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "displaymoduleModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "displaymoduleIndex"),
)
if mibBuilder.loadTexts:
    eDisplayModuleEntry.setStatus("current")
_DGeneralModuleStatus_Type = Unsigned32
_DGeneralModuleStatus_Object = MibTableColumn
dGeneralModuleStatus = _DGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 1),
    _DGeneralModuleStatus_Type()
)
dGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dGeneralModuleStatus.setStatus("current")
_DSpecificModuleStatus_Type = Unsigned32
_DSpecificModuleStatus_Object = MibTableColumn
dSpecificModuleStatus = _DSpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 2),
    _DSpecificModuleStatus_Type()
)
dSpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSpecificModuleStatus.setStatus("current")
_DCurrentTime_Type = TimeTicks
_DCurrentTime_Object = MibTableColumn
dCurrentTime = _DCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 3),
    _DCurrentTime_Type()
)
dCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    dCurrentTime.setUnits("UNIX")
_DTemperature_Type = Utenth
_DTemperature_Object = MibTableColumn
dTemperature = _DTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 11),
    _DTemperature_Type()
)
dTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dTemperature.setUnits("K")
_DTimeOnline_Type = Unsigned32
_DTimeOnline_Object = MibTableColumn
dTimeOnline = _DTimeOnline_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 24),
    _DTimeOnline_Type()
)
dTimeOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTimeOnline.setStatus("current")
if mibBuilder.loadTexts:
    dTimeOnline.setUnits("s")
_DModuleName_Type = DisplayString
_DModuleName_Object = MibTableColumn
dModuleName = _DModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10001),
    _DModuleName_Type()
)
dModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dModuleName.setStatus("current")
_DFirmwareVersion_Type = Version
_DFirmwareVersion_Object = MibTableColumn
dFirmwareVersion = _DFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10002),
    _DFirmwareVersion_Type()
)
dFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFirmwareVersion.setStatus("current")
_DHardwareVersion_Type = Version
_DHardwareVersion_Object = MibTableColumn
dHardwareVersion = _DHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10003),
    _DHardwareVersion_Type()
)
dHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dHardwareVersion.setStatus("current")
_DFirmwareID_Type = DisplayString
_DFirmwareID_Object = MibTableColumn
dFirmwareID = _DFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10004),
    _DFirmwareID_Type()
)
dFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dFirmwareID.setStatus("current")
_DHardwareID_Type = DisplayString
_DHardwareID_Object = MibTableColumn
dHardwareID = _DHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10005),
    _DHardwareID_Type()
)
dHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dHardwareID.setStatus("current")


class _DMinTemperatureWarning_Type(Utenth):
    """Custom type dMinTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_DMinTemperatureWarning_Type.__name__ = "Utenth"
_DMinTemperatureWarning_Object = MibTableColumn
dMinTemperatureWarning = _DMinTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10052),
    _DMinTemperatureWarning_Type()
)
dMinTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMinTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    dMinTemperatureWarning.setUnits("K")


class _DMaxTemperatureWarning_Type(Utenth):
    """Custom type dMaxTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_DMaxTemperatureWarning_Type.__name__ = "Utenth"
_DMaxTemperatureWarning_Object = MibTableColumn
dMaxTemperatureWarning = _DMaxTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10053),
    _DMaxTemperatureWarning_Type()
)
dMaxTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dMaxTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    dMaxTemperatureWarning.setUnits("K")


class _DDisplayAllDevices_Type(Unsigned32):
    """Custom type dDisplayAllDevices based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DDisplayAllDevices_Type.__name__ = "Unsigned32"
_DDisplayAllDevices_Object = MibTableColumn
dDisplayAllDevices = _DDisplayAllDevices_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 10237),
    _DDisplayAllDevices_Type()
)
dDisplayAllDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDisplayAllDevices.setStatus("current")


class _DisplaymoduleIndex_Type(Integer32):
    """Custom type displaymoduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DisplaymoduleIndex_Type.__name__ = "Integer32"
_DisplaymoduleIndex_Object = MibTableColumn
displaymoduleIndex = _DisplaymoduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 65537),
    _DisplaymoduleIndex_Type()
)
displaymoduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    displaymoduleIndex.setStatus("current")


class _DisplaymoduleModuleIndex_Type(Integer32):
    """Custom type displaymoduleModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DisplaymoduleModuleIndex_Type.__name__ = "Integer32"
_DisplaymoduleModuleIndex_Object = MibTableColumn
displaymoduleModuleIndex = _DisplaymoduleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 68, 1, 1, 65538),
    _DisplaymoduleModuleIndex_Type()
)
displaymoduleModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    displaymoduleModuleIndex.setStatus("current")
_EnergymonitorModule_ObjectIdentity = ObjectIdentity
energymonitorModule = _EnergymonitorModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69)
)
_EEnergyMonitorTable_Object = MibTable
eEnergyMonitorTable = _EEnergyMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1)
)
if mibBuilder.loadTexts:
    eEnergyMonitorTable.setStatus("current")
_EEnergyMonitorEntry_Object = MibTableRow
eEnergyMonitorEntry = _EEnergyMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1)
)
eEnergyMonitorEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "energymonitorModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "energymonitorIndex"),
)
if mibBuilder.loadTexts:
    eEnergyMonitorEntry.setStatus("current")
_EGeneralModuleStatus_Type = Unsigned32
_EGeneralModuleStatus_Object = MibTableColumn
eGeneralModuleStatus = _EGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 1),
    _EGeneralModuleStatus_Type()
)
eGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGeneralModuleStatus.setStatus("current")
_ESpecificModuleStatus_Type = Unsigned32
_ESpecificModuleStatus_Object = MibTableColumn
eSpecificModuleStatus = _ESpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 2),
    _ESpecificModuleStatus_Type()
)
eSpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpecificModuleStatus.setStatus("current")
_ECurrentTime_Type = TimeTicks
_ECurrentTime_Object = MibTableColumn
eCurrentTime = _ECurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 3),
    _ECurrentTime_Type()
)
eCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    eCurrentTime.setUnits("UNIX")
_EVoltage_Type = Uhundredth
_EVoltage_Object = MibTableColumn
eVoltage = _EVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 4),
    _EVoltage_Type()
)
eVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVoltage.setStatus("current")
if mibBuilder.loadTexts:
    eVoltage.setUnits("V")
_EFrequency_Type = Uthousandth
_EFrequency_Object = MibTableColumn
eFrequency = _EFrequency_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 5),
    _EFrequency_Type()
)
eFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFrequency.setStatus("current")
if mibBuilder.loadTexts:
    eFrequency.setUnits("Hz")
_ECurrent_Type = Uthousandth
_ECurrent_Object = MibTableColumn
eCurrent = _ECurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 6),
    _ECurrent_Type()
)
eCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eCurrent.setUnits("A")
_EPower_Type = Unsigned32
_EPower_Object = MibTableColumn
ePower = _EPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 7),
    _EPower_Type()
)
ePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePower.setStatus("current")
if mibBuilder.loadTexts:
    ePower.setUnits("W")
_EActiveEnergy_Type = Uthousandth
_EActiveEnergy_Object = MibTableColumn
eActiveEnergy = _EActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 9),
    _EActiveEnergy_Type()
)
eActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eActiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    eActiveEnergy.setUnits("kWh")
_EApparentEnergy_Type = Uthousandth
_EApparentEnergy_Object = MibTableColumn
eApparentEnergy = _EApparentEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10),
    _EApparentEnergy_Type()
)
eApparentEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eApparentEnergy.setStatus("current")
if mibBuilder.loadTexts:
    eApparentEnergy.setUnits("kVAh")
_ETemperature_Type = Utenth
_ETemperature_Object = MibTableColumn
eTemperature = _ETemperature_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 11),
    _ETemperature_Type()
)
eTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTemperature.setStatus("current")
if mibBuilder.loadTexts:
    eTemperature.setUnits("K")
_EApparentPower_Type = Unsigned32
_EApparentPower_Object = MibTableColumn
eApparentPower = _EApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 15),
    _EApparentPower_Type()
)
eApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    eApparentPower.setUnits("VA")
_EPowerFactor_Type = Unsigned32
_EPowerFactor_Object = MibTableColumn
ePowerFactor = _EPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 16),
    _EPowerFactor_Type()
)
ePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    ePowerFactor.setUnits("%")
_ETotalCurrent_Type = Uthousandth
_ETotalCurrent_Object = MibTableColumn
eTotalCurrent = _ETotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 17),
    _ETotalCurrent_Type()
)
eTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    eTotalCurrent.setUnits("A")
_ETotalRealPower_Type = Unsigned32
_ETotalRealPower_Object = MibTableColumn
eTotalRealPower = _ETotalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 18),
    _ETotalRealPower_Type()
)
eTotalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTotalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    eTotalRealPower.setUnits("W")
_ETotalApparentPower_Type = Unsigned32
_ETotalApparentPower_Object = MibTableColumn
eTotalApparentPower = _ETotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 19),
    _ETotalApparentPower_Type()
)
eTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTotalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    eTotalApparentPower.setUnits("VA")
_ETotalActiveEnergy_Type = Uthousandth
_ETotalActiveEnergy_Object = MibTableColumn
eTotalActiveEnergy = _ETotalActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 20),
    _ETotalActiveEnergy_Type()
)
eTotalActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTotalActiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    eTotalActiveEnergy.setUnits("kWh")
_ETotalApparentEnergy_Type = Uthousandth
_ETotalApparentEnergy_Object = MibTableColumn
eTotalApparentEnergy = _ETotalApparentEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 21),
    _ETotalApparentEnergy_Type()
)
eTotalApparentEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTotalApparentEnergy.setStatus("current")
if mibBuilder.loadTexts:
    eTotalApparentEnergy.setUnits("kVAh")
_ETotalPowerFactor_Type = Unsigned32
_ETotalPowerFactor_Object = MibTableColumn
eTotalPowerFactor = _ETotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 22),
    _ETotalPowerFactor_Type()
)
eTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTotalPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    eTotalPowerFactor.setUnits("%")
_ETimeOnline_Type = Unsigned32
_ETimeOnline_Object = MibTableColumn
eTimeOnline = _ETimeOnline_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 24),
    _ETimeOnline_Type()
)
eTimeOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTimeOnline.setStatus("current")
if mibBuilder.loadTexts:
    eTimeOnline.setUnits("s")


class _ETotalHarmonicDistortion_Type(Utenth):
    """Custom type eTotalHarmonicDistortion based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ETotalHarmonicDistortion_Type.__name__ = "Utenth"
_ETotalHarmonicDistortion_Object = MibTableColumn
eTotalHarmonicDistortion = _ETotalHarmonicDistortion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 50),
    _ETotalHarmonicDistortion_Type()
)
eTotalHarmonicDistortion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTotalHarmonicDistortion.setStatus("current")
if mibBuilder.loadTexts:
    eTotalHarmonicDistortion.setUnits("%")
_EModuleName_Type = DisplayString
_EModuleName_Object = MibTableColumn
eModuleName = _EModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10001),
    _EModuleName_Type()
)
eModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eModuleName.setStatus("current")
_EFirmwareVersion_Type = Version
_EFirmwareVersion_Object = MibTableColumn
eFirmwareVersion = _EFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10002),
    _EFirmwareVersion_Type()
)
eFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFirmwareVersion.setStatus("current")
_EHardwareVersion_Type = Version
_EHardwareVersion_Object = MibTableColumn
eHardwareVersion = _EHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10003),
    _EHardwareVersion_Type()
)
eHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHardwareVersion.setStatus("current")
_EFirmwareID_Type = DisplayString
_EFirmwareID_Object = MibTableColumn
eFirmwareID = _EFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10004),
    _EFirmwareID_Type()
)
eFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFirmwareID.setStatus("current")
_EHardwareID_Type = DisplayString
_EHardwareID_Object = MibTableColumn
eHardwareID = _EHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10005),
    _EHardwareID_Type()
)
eHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHardwareID.setStatus("current")


class _EMaxCurrentWarning_Type(Uthousandth):
    """Custom type eMaxCurrentWarning based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8000),
    )


_EMaxCurrentWarning_Type.__name__ = "Uthousandth"
_EMaxCurrentWarning_Object = MibTableColumn
eMaxCurrentWarning = _EMaxCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10039),
    _EMaxCurrentWarning_Type()
)
eMaxCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMaxCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMaxCurrentWarning.setUnits("A")


class _EMaxPowerWarning_Type(Unsigned32):
    """Custom type eMaxPowerWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_EMaxPowerWarning_Type.__name__ = "Unsigned32"
_EMaxPowerWarning_Object = MibTableColumn
eMaxPowerWarning = _EMaxPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10041),
    _EMaxPowerWarning_Type()
)
eMaxPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMaxPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMaxPowerWarning.setUnits("W")


class _EMaxTotalCurrentWarning_Type(Uthousandth):
    """Custom type eMaxTotalCurrentWarning based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 16000),
    )


_EMaxTotalCurrentWarning_Type.__name__ = "Uthousandth"
_EMaxTotalCurrentWarning_Object = MibTableColumn
eMaxTotalCurrentWarning = _EMaxTotalCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10043),
    _EMaxTotalCurrentWarning_Type()
)
eMaxTotalCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMaxTotalCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMaxTotalCurrentWarning.setUnits("A")


class _EMaxTotalPowerWarning_Type(Unsigned32):
    """Custom type eMaxTotalPowerWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4000),
    )


_EMaxTotalPowerWarning_Type.__name__ = "Unsigned32"
_EMaxTotalPowerWarning_Object = MibTableColumn
eMaxTotalPowerWarning = _EMaxTotalPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10045),
    _EMaxTotalPowerWarning_Type()
)
eMaxTotalPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMaxTotalPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMaxTotalPowerWarning.setUnits("W")


class _EMaxVoltageWarning_Type(Uhundredth):
    """Custom type eMaxVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 30000),
    )


_EMaxVoltageWarning_Type.__name__ = "Uhundredth"
_EMaxVoltageWarning_Object = MibTableColumn
eMaxVoltageWarning = _EMaxVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10047),
    _EMaxVoltageWarning_Type()
)
eMaxVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMaxVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMaxVoltageWarning.setUnits("V")


class _EMinVoltageWarning_Type(Uhundredth):
    """Custom type eMinVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 30000),
    )


_EMinVoltageWarning_Type.__name__ = "Uhundredth"
_EMinVoltageWarning_Object = MibTableColumn
eMinVoltageWarning = _EMinVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10049),
    _EMinVoltageWarning_Type()
)
eMinVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMinVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMinVoltageWarning.setUnits("V")


class _EMinTemperatureWarning_Type(Utenth):
    """Custom type eMinTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_EMinTemperatureWarning_Type.__name__ = "Utenth"
_EMinTemperatureWarning_Object = MibTableColumn
eMinTemperatureWarning = _EMinTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10052),
    _EMinTemperatureWarning_Type()
)
eMinTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMinTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMinTemperatureWarning.setUnits("K")


class _EMaxTemperatureWarning_Type(Utenth):
    """Custom type eMaxTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_EMaxTemperatureWarning_Type.__name__ = "Utenth"
_EMaxTemperatureWarning_Object = MibTableColumn
eMaxTemperatureWarning = _EMaxTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10053),
    _EMaxTemperatureWarning_Type()
)
eMaxTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMaxTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    eMaxTemperatureWarning.setUnits("K")
_ECurrentWarningEvent_Type = EVENTFLAGS
_ECurrentWarningEvent_Object = MibTableColumn
eCurrentWarningEvent = _ECurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10078),
    _ECurrentWarningEvent_Type()
)
eCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eCurrentWarningEvent.setStatus("current")
_EPowerWarningEvent_Type = EVENTFLAGS
_EPowerWarningEvent_Object = MibTableColumn
ePowerWarningEvent = _EPowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10080),
    _EPowerWarningEvent_Type()
)
ePowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePowerWarningEvent.setStatus("current")
_ETotalCurrentWarningEvent_Type = EVENTFLAGS
_ETotalCurrentWarningEvent_Object = MibTableColumn
eTotalCurrentWarningEvent = _ETotalCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10082),
    _ETotalCurrentWarningEvent_Type()
)
eTotalCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTotalCurrentWarningEvent.setStatus("current")
_ETotalPowerWarningEvent_Type = EVENTFLAGS
_ETotalPowerWarningEvent_Object = MibTableColumn
eTotalPowerWarningEvent = _ETotalPowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10084),
    _ETotalPowerWarningEvent_Type()
)
eTotalPowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTotalPowerWarningEvent.setStatus("current")
_EVoltageWarningEvent_Type = EVENTFLAGS
_EVoltageWarningEvent_Object = MibTableColumn
eVoltageWarningEvent = _EVoltageWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10086),
    _EVoltageWarningEvent_Type()
)
eVoltageWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eVoltageWarningEvent.setStatus("current")
_ETemperatureWarningEvent_Type = EVENTFLAGS
_ETemperatureWarningEvent_Object = MibTableColumn
eTemperatureWarningEvent = _ETemperatureWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10087),
    _ETemperatureWarningEvent_Type()
)
eTemperatureWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTemperatureWarningEvent.setStatus("current")


class _EMicroIntTimeThreshold_Type(Utenth):
    """Custom type eMicroIntTimeThreshold based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_EMicroIntTimeThreshold_Type.__name__ = "Utenth"
_EMicroIntTimeThreshold_Object = MibTableColumn
eMicroIntTimeThreshold = _EMicroIntTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10135),
    _EMicroIntTimeThreshold_Type()
)
eMicroIntTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMicroIntTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    eMicroIntTimeThreshold.setUnits("ms")
_EMicroIntEvent_Type = EVENTFLAGS
_EMicroIntEvent_Object = MibTableColumn
eMicroIntEvent = _EMicroIntEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 10136),
    _EMicroIntEvent_Type()
)
eMicroIntEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMicroIntEvent.setStatus("current")


class _EnergymonitorIndex_Type(Integer32):
    """Custom type energymonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EnergymonitorIndex_Type.__name__ = "Integer32"
_EnergymonitorIndex_Object = MibTableColumn
energymonitorIndex = _EnergymonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 65537),
    _EnergymonitorIndex_Type()
)
energymonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    energymonitorIndex.setStatus("current")


class _EnergymonitorModuleIndex_Type(Integer32):
    """Custom type energymonitorModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EnergymonitorModuleIndex_Type.__name__ = "Integer32"
_EnergymonitorModuleIndex_Object = MibTableColumn
energymonitorModuleIndex = _EnergymonitorModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 69, 1, 1, 65538),
    _EnergymonitorModuleIndex_Type()
)
energymonitorModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    energymonitorModuleIndex.setStatus("current")
_MasterModule_ObjectIdentity = ObjectIdentity
masterModule = _MasterModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77)
)
_EMasterTable_Object = MibTable
eMasterTable = _EMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1)
)
if mibBuilder.loadTexts:
    eMasterTable.setStatus("current")
_EMasterEntry_Object = MibTableRow
eMasterEntry = _EMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1)
)
eMasterEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "masterModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "masterIndex"),
)
if mibBuilder.loadTexts:
    eMasterEntry.setStatus("current")
_MGeneralModuleStatus_Type = Unsigned32
_MGeneralModuleStatus_Object = MibTableColumn
mGeneralModuleStatus = _MGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 1),
    _MGeneralModuleStatus_Type()
)
mGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mGeneralModuleStatus.setStatus("current")
_MSpecificModuleStatus_Type = Unsigned32
_MSpecificModuleStatus_Object = MibTableColumn
mSpecificModuleStatus = _MSpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 2),
    _MSpecificModuleStatus_Type()
)
mSpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSpecificModuleStatus.setStatus("current")
_MCurrentTime_Type = TimeTicks
_MCurrentTime_Object = MibTableColumn
mCurrentTime = _MCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 3),
    _MCurrentTime_Type()
)
mCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    mCurrentTime.setUnits("UNIX")
_MVoltage_Type = Uhundredth
_MVoltage_Object = MibTableColumn
mVoltage = _MVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 4),
    _MVoltage_Type()
)
mVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mVoltage.setStatus("current")
if mibBuilder.loadTexts:
    mVoltage.setUnits("V")
_MTemperature_Type = Utenth
_MTemperature_Object = MibTableColumn
mTemperature = _MTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 11),
    _MTemperature_Type()
)
mTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTemperature.setStatus("current")
if mibBuilder.loadTexts:
    mTemperature.setUnits("K")
_MCurrentIP_Type = IpAddress
_MCurrentIP_Object = MibTableColumn
mCurrentIP = _MCurrentIP_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 14),
    _MCurrentIP_Type()
)
mCurrentIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCurrentIP.setStatus("current")
_MTotalCurrent_Type = Uthousandth
_MTotalCurrent_Object = MibTableColumn
mTotalCurrent = _MTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 17),
    _MTotalCurrent_Type()
)
mTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mTotalCurrent.setUnits("A")
_MTotalRealPower_Type = Unsigned32
_MTotalRealPower_Object = MibTableColumn
mTotalRealPower = _MTotalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 18),
    _MTotalRealPower_Type()
)
mTotalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTotalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    mTotalRealPower.setUnits("W")
_MTotalActiveEnergy_Type = Uthousandth
_MTotalActiveEnergy_Object = MibTableColumn
mTotalActiveEnergy = _MTotalActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 20),
    _MTotalActiveEnergy_Type()
)
mTotalActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTotalActiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    mTotalActiveEnergy.setUnits("kWh")


class _MLineCurrent_Type(Uthousandth):
    """Custom type mLineCurrent based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MLineCurrent_Type.__name__ = "Uthousandth"
_MLineCurrent_Object = MibTableColumn
mLineCurrent = _MLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 32),
    _MLineCurrent_Type()
)
mLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mLineCurrent.setUnits("A")


class _MFuseCurrent_Type(Uthousandth):
    """Custom type mFuseCurrent based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MFuseCurrent_Type.__name__ = "Uthousandth"
_MFuseCurrent_Object = MibTableColumn
mFuseCurrent = _MFuseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 33),
    _MFuseCurrent_Type()
)
mFuseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mFuseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mFuseCurrent.setUnits("A")
_MCurrentSubNetMask_Type = IpAddress
_MCurrentSubNetMask_Object = MibTableColumn
mCurrentSubNetMask = _MCurrentSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 34),
    _MCurrentSubNetMask_Type()
)
mCurrentSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCurrentSubNetMask.setStatus("current")
_MCurrentDNSServer_Type = IpAddress
_MCurrentDNSServer_Object = MibTableColumn
mCurrentDNSServer = _MCurrentDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 35),
    _MCurrentDNSServer_Type()
)
mCurrentDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCurrentDNSServer.setStatus("current")
_MCurrentStdGateway_Type = IpAddress
_MCurrentStdGateway_Object = MibTableColumn
mCurrentStdGateway = _MCurrentStdGateway_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 36),
    _MCurrentStdGateway_Type()
)
mCurrentStdGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCurrentStdGateway.setStatus("current")


class _MUPSPresent_Type(Unsigned32):
    """Custom type mUPSPresent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MUPSPresent_Type.__name__ = "Unsigned32"
_MUPSPresent_Object = MibTableColumn
mUPSPresent = _MUPSPresent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 37),
    _MUPSPresent_Type()
)
mUPSPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mUPSPresent.setStatus("current")
_MUPSStatus_Type = Unsigned32
_MUPSStatus_Object = MibTableColumn
mUPSStatus = _MUPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 38),
    _MUPSStatus_Type()
)
mUPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mUPSStatus.setStatus("current")


class _MUPSEstimatedRunTime_Type(Unsigned32):
    """Custom type mUPSEstimatedRunTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MUPSEstimatedRunTime_Type.__name__ = "Unsigned32"
_MUPSEstimatedRunTime_Object = MibTableColumn
mUPSEstimatedRunTime = _MUPSEstimatedRunTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 39),
    _MUPSEstimatedRunTime_Type()
)
mUPSEstimatedRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mUPSEstimatedRunTime.setStatus("current")
if mibBuilder.loadTexts:
    mUPSEstimatedRunTime.setUnits("min")


class _MUPSBatteryLevel_Type(Utenth):
    """Custom type mUPSBatteryLevel based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MUPSBatteryLevel_Type.__name__ = "Utenth"
_MUPSBatteryLevel_Object = MibTableColumn
mUPSBatteryLevel = _MUPSBatteryLevel_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 40),
    _MUPSBatteryLevel_Type()
)
mUPSBatteryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mUPSBatteryLevel.setStatus("current")
if mibBuilder.loadTexts:
    mUPSBatteryLevel.setUnits("%")
_MHighCurrent_Type = Stenth
_MHighCurrent_Object = MibTableColumn
mHighCurrent = _MHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 41),
    _MHighCurrent_Type()
)
mHighCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mHighCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mHighCurrent.setUnits("A")


class _MUpsCommunicationStatus_Type(Unsigned32):
    """Custom type mUpsCommunicationStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MUpsCommunicationStatus_Type.__name__ = "Unsigned32"
_MUpsCommunicationStatus_Object = MibTableColumn
mUpsCommunicationStatus = _MUpsCommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 42),
    _MUpsCommunicationStatus_Type()
)
mUpsCommunicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mUpsCommunicationStatus.setStatus("current")


class _MHighPower_Type(Shundredth):
    """Custom type mHighPower based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MHighPower_Type.__name__ = "Shundredth"
_MHighPower_Object = MibTableColumn
mHighPower = _MHighPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 43),
    _MHighPower_Type()
)
mHighPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mHighPower.setStatus("current")
if mibBuilder.loadTexts:
    mHighPower.setUnits("kW")


class _MTotalHighCurrent_Type(Stenth):
    """Custom type mTotalHighCurrent based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MTotalHighCurrent_Type.__name__ = "Stenth"
_MTotalHighCurrent_Object = MibTableColumn
mTotalHighCurrent = _MTotalHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 44),
    _MTotalHighCurrent_Type()
)
mTotalHighCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTotalHighCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mTotalHighCurrent.setUnits("A")


class _MTotalHighPower_Type(Shundredth):
    """Custom type mTotalHighPower based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MTotalHighPower_Type.__name__ = "Shundredth"
_MTotalHighPower_Object = MibTableColumn
mTotalHighPower = _MTotalHighPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 45),
    _MTotalHighPower_Type()
)
mTotalHighPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTotalHighPower.setStatus("current")
if mibBuilder.loadTexts:
    mTotalHighPower.setUnits("kW")


class _MPositiveEnergy_Type(Uthousandth):
    """Custom type mPositiveEnergy based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MPositiveEnergy_Type.__name__ = "Uthousandth"
_MPositiveEnergy_Object = MibTableColumn
mPositiveEnergy = _MPositiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 46),
    _MPositiveEnergy_Type()
)
mPositiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPositiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    mPositiveEnergy.setUnits("kWh")


class _MNegativeEnergy_Type(Uthousandth):
    """Custom type mNegativeEnergy based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MNegativeEnergy_Type.__name__ = "Uthousandth"
_MNegativeEnergy_Object = MibTableColumn
mNegativeEnergy = _MNegativeEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 47),
    _MNegativeEnergy_Type()
)
mNegativeEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mNegativeEnergy.setStatus("current")
if mibBuilder.loadTexts:
    mNegativeEnergy.setUnits("kWh")


class _MTotalPositiveEnergy_Type(Uthousandth):
    """Custom type mTotalPositiveEnergy based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MTotalPositiveEnergy_Type.__name__ = "Uthousandth"
_MTotalPositiveEnergy_Object = MibTableColumn
mTotalPositiveEnergy = _MTotalPositiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 48),
    _MTotalPositiveEnergy_Type()
)
mTotalPositiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTotalPositiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    mTotalPositiveEnergy.setUnits("kWh")


class _MTotalNegativeEnergy_Type(Uthousandth):
    """Custom type mTotalNegativeEnergy based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MTotalNegativeEnergy_Type.__name__ = "Uthousandth"
_MTotalNegativeEnergy_Object = MibTableColumn
mTotalNegativeEnergy = _MTotalNegativeEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 49),
    _MTotalNegativeEnergy_Type()
)
mTotalNegativeEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTotalNegativeEnergy.setStatus("current")
if mibBuilder.loadTexts:
    mTotalNegativeEnergy.setUnits("kWh")


class _MCloudStatus_Type(Unsigned32):
    """Custom type mCloudStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MCloudStatus_Type.__name__ = "Unsigned32"
_MCloudStatus_Object = MibTableColumn
mCloudStatus = _MCloudStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 56),
    _MCloudStatus_Type()
)
mCloudStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCloudStatus.setStatus("current")


class _MStatus_Type(Unsigned32):
    """Custom type mStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MStatus_Type.__name__ = "Unsigned32"
_MStatus_Object = MibTableColumn
mStatus = _MStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 1000),
    _MStatus_Type()
)
mStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mStatus.setStatus("current")
_MModuleName_Type = DisplayString
_MModuleName_Object = MibTableColumn
mModuleName = _MModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10001),
    _MModuleName_Type()
)
mModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mModuleName.setStatus("current")
_MFirmwareVersion_Type = Version
_MFirmwareVersion_Object = MibTableColumn
mFirmwareVersion = _MFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10002),
    _MFirmwareVersion_Type()
)
mFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mFirmwareVersion.setStatus("current")
_MHardwareVersion_Type = Version
_MHardwareVersion_Object = MibTableColumn
mHardwareVersion = _MHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10003),
    _MHardwareVersion_Type()
)
mHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mHardwareVersion.setStatus("current")
_MFirmwareID_Type = DisplayString
_MFirmwareID_Object = MibTableColumn
mFirmwareID = _MFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10004),
    _MFirmwareID_Type()
)
mFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mFirmwareID.setStatus("current")
_MHardwareID_Type = DisplayString
_MHardwareID_Object = MibTableColumn
mHardwareID = _MHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10005),
    _MHardwareID_Type()
)
mHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mHardwareID.setStatus("current")
_MRackName_Type = DisplayString
_MRackName_Object = MibTableColumn
mRackName = _MRackName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10006),
    _MRackName_Type()
)
mRackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mRackName.setStatus("current")
_MRackPosition_Type = DisplayString
_MRackPosition_Object = MibTableColumn
mRackPosition = _MRackPosition_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10007),
    _MRackPosition_Type()
)
mRackPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mRackPosition.setStatus("current")
_MIPAddress_Type = IpAddress
_MIPAddress_Object = MibTableColumn
mIPAddress = _MIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10011),
    _MIPAddress_Type()
)
mIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mIPAddress.setStatus("current")
_MSubNetMask_Type = IpAddress
_MSubNetMask_Object = MibTableColumn
mSubNetMask = _MSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10012),
    _MSubNetMask_Type()
)
mSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSubNetMask.setStatus("current")
_MStdGateWay_Type = IpAddress
_MStdGateWay_Object = MibTableColumn
mStdGateWay = _MStdGateWay_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10013),
    _MStdGateWay_Type()
)
mStdGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mStdGateWay.setStatus("current")
_MDnsServer_Type = IpAddress
_MDnsServer_Object = MibTableColumn
mDnsServer = _MDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10014),
    _MDnsServer_Type()
)
mDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mDnsServer.setStatus("current")
_MMAC_Type = MacAddress
_MMAC_Object = MibTableColumn
mMAC = _MMAC_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10015),
    _MMAC_Type()
)
mMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mMAC.setStatus("current")


class _MDHCPEnable_Type(Unsigned32):
    """Custom type mDHCPEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MDHCPEnable_Type.__name__ = "Unsigned32"
_MDHCPEnable_Object = MibTableColumn
mDHCPEnable = _MDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10016),
    _MDHCPEnable_Type()
)
mDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mDHCPEnable.setStatus("current")
_MNTPServer_Type = IpAddress
_MNTPServer_Object = MibTableColumn
mNTPServer = _MNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10017),
    _MNTPServer_Type()
)
mNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mNTPServer.setStatus("current")


class _MUseDefaultNTPServer_Type(Unsigned32):
    """Custom type mUseDefaultNTPServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MUseDefaultNTPServer_Type.__name__ = "Unsigned32"
_MUseDefaultNTPServer_Object = MibTableColumn
mUseDefaultNTPServer = _MUseDefaultNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10018),
    _MUseDefaultNTPServer_Type()
)
mUseDefaultNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUseDefaultNTPServer.setStatus("current")


class _MUseNTP_Type(Unsigned32):
    """Custom type mUseNTP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MUseNTP_Type.__name__ = "Unsigned32"
_MUseNTP_Object = MibTableColumn
mUseNTP = _MUseNTP_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10019),
    _MUseNTP_Type()
)
mUseNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUseNTP.setStatus("current")
_MSNMPTrapRecvIP_Type = IpAddress
_MSNMPTrapRecvIP_Object = MibTableColumn
mSNMPTrapRecvIP = _MSNMPTrapRecvIP_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10020),
    _MSNMPTrapRecvIP_Type()
)
mSNMPTrapRecvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPTrapRecvIP.setStatus("current")


class _MSNMPTrapRecvPort_Type(Unsigned32):
    """Custom type mSNMPTrapRecvPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MSNMPTrapRecvPort_Type.__name__ = "Unsigned32"
_MSNMPTrapRecvPort_Object = MibTableColumn
mSNMPTrapRecvPort = _MSNMPTrapRecvPort_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10021),
    _MSNMPTrapRecvPort_Type()
)
mSNMPTrapRecvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPTrapRecvPort.setStatus("current")


class _MSNMPControl_Type(Unsigned32):
    """Custom type mSNMPControl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MSNMPControl_Type.__name__ = "Unsigned32"
_MSNMPControl_Object = MibTableColumn
mSNMPControl = _MSNMPControl_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10024),
    _MSNMPControl_Type()
)
mSNMPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPControl.setStatus("current")
_MECSServer_Type = IpAddress
_MECSServer_Object = MibTableColumn
mECSServer = _MECSServer_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10028),
    _MECSServer_Type()
)
mECSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mECSServer.setStatus("current")


class _MUseECSServer_Type(Unsigned32):
    """Custom type mUseECSServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MUseECSServer_Type.__name__ = "Unsigned32"
_MUseECSServer_Object = MibTableColumn
mUseECSServer = _MUseECSServer_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10029),
    _MUseECSServer_Type()
)
mUseECSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUseECSServer.setStatus("current")


class _MDisplayLock_Type(Unsigned32):
    """Custom type mDisplayLock based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MDisplayLock_Type.__name__ = "Unsigned32"
_MDisplayLock_Object = MibTableColumn
mDisplayLock = _MDisplayLock_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10031),
    _MDisplayLock_Type()
)
mDisplayLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mDisplayLock.setStatus("current")


class _MDisplayTimeOn_Type(Unsigned32):
    """Custom type mDisplayTimeOn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MDisplayTimeOn_Type.__name__ = "Unsigned32"
_MDisplayTimeOn_Object = MibTableColumn
mDisplayTimeOn = _MDisplayTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10032),
    _MDisplayTimeOn_Type()
)
mDisplayTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mDisplayTimeOn.setStatus("current")
if mibBuilder.loadTexts:
    mDisplayTimeOn.setUnits("min")


class _MMaxVoltageWarning_Type(Uhundredth):
    """Custom type mMaxVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MMaxVoltageWarning_Type.__name__ = "Uhundredth"
_MMaxVoltageWarning_Object = MibTableColumn
mMaxVoltageWarning = _MMaxVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10047),
    _MMaxVoltageWarning_Type()
)
mMaxVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMaxVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMaxVoltageWarning.setUnits("V")


class _MMinVoltageWarning_Type(Uhundredth):
    """Custom type mMinVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MMinVoltageWarning_Type.__name__ = "Uhundredth"
_MMinVoltageWarning_Object = MibTableColumn
mMinVoltageWarning = _MMinVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10049),
    _MMinVoltageWarning_Type()
)
mMinVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMinVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMinVoltageWarning.setUnits("V")


class _MMinTemperatureWarning_Type(Utenth):
    """Custom type mMinTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_MMinTemperatureWarning_Type.__name__ = "Utenth"
_MMinTemperatureWarning_Object = MibTableColumn
mMinTemperatureWarning = _MMinTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10052),
    _MMinTemperatureWarning_Type()
)
mMinTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMinTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMinTemperatureWarning.setUnits("K")


class _MMaxTemperatureWarning_Type(Utenth):
    """Custom type mMaxTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_MMaxTemperatureWarning_Type.__name__ = "Utenth"
_MMaxTemperatureWarning_Object = MibTableColumn
mMaxTemperatureWarning = _MMaxTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10053),
    _MMaxTemperatureWarning_Type()
)
mMaxTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMaxTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMaxTemperatureWarning.setUnits("K")
_MGeneralEventEnable_Type = EVENTFLAGS
_MGeneralEventEnable_Object = MibTableColumn
mGeneralEventEnable = _MGeneralEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10074),
    _MGeneralEventEnable_Type()
)
mGeneralEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGeneralEventEnable.setStatus("current")
_MSNMPSysContact_Type = DisplayString
_MSNMPSysContact_Object = MibTableColumn
mSNMPSysContact = _MSNMPSysContact_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10075),
    _MSNMPSysContact_Type()
)
mSNMPSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPSysContact.setStatus("current")
_MCurrentWarningEvent_Type = EVENTFLAGS
_MCurrentWarningEvent_Object = MibTableColumn
mCurrentWarningEvent = _MCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10078),
    _MCurrentWarningEvent_Type()
)
mCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mCurrentWarningEvent.setStatus("current")
_MPowerWarningEvent_Type = EVENTFLAGS
_MPowerWarningEvent_Object = MibTableColumn
mPowerWarningEvent = _MPowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10080),
    _MPowerWarningEvent_Type()
)
mPowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mPowerWarningEvent.setStatus("current")
_MTotalCurrentWarningEvent_Type = EVENTFLAGS
_MTotalCurrentWarningEvent_Object = MibTableColumn
mTotalCurrentWarningEvent = _MTotalCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10082),
    _MTotalCurrentWarningEvent_Type()
)
mTotalCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mTotalCurrentWarningEvent.setStatus("current")
_MTotalPowerWarningEvent_Type = EVENTFLAGS
_MTotalPowerWarningEvent_Object = MibTableColumn
mTotalPowerWarningEvent = _MTotalPowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10084),
    _MTotalPowerWarningEvent_Type()
)
mTotalPowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mTotalPowerWarningEvent.setStatus("current")
_MVoltageWarningEvent_Type = EVENTFLAGS
_MVoltageWarningEvent_Object = MibTableColumn
mVoltageWarningEvent = _MVoltageWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10086),
    _MVoltageWarningEvent_Type()
)
mVoltageWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mVoltageWarningEvent.setStatus("current")
_MTemperatureWarningEvent_Type = EVENTFLAGS
_MTemperatureWarningEvent_Object = MibTableColumn
mTemperatureWarningEvent = _MTemperatureWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10087),
    _MTemperatureWarningEvent_Type()
)
mTemperatureWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mTemperatureWarningEvent.setStatus("current")


class _MDisplayBrightness_Type(Unsigned32):
    """Custom type mDisplayBrightness based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MDisplayBrightness_Type.__name__ = "Unsigned32"
_MDisplayBrightness_Object = MibTableColumn
mDisplayBrightness = _MDisplayBrightness_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10098),
    _MDisplayBrightness_Type()
)
mDisplayBrightness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mDisplayBrightness.setStatus("current")


class _MECSServerPort_Type(Unsigned32):
    """Custom type mECSServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MECSServerPort_Type.__name__ = "Unsigned32"
_MECSServerPort_Object = MibTableColumn
mECSServerPort = _MECSServerPort_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10106),
    _MECSServerPort_Type()
)
mECSServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mECSServerPort.setStatus("current")
_MExternalSensorLabel_Type = DisplayString
_MExternalSensorLabel_Object = MibTableColumn
mExternalSensorLabel = _MExternalSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10109),
    _MExternalSensorLabel_Type()
)
mExternalSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mExternalSensorLabel.setStatus("current")


class _MHttpsOnly_Type(Unsigned32):
    """Custom type mHttpsOnly based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MHttpsOnly_Type.__name__ = "Unsigned32"
_MHttpsOnly_Object = MibTableColumn
mHttpsOnly = _MHttpsOnly_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10127),
    _MHttpsOnly_Type()
)
mHttpsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mHttpsOnly.setStatus("current")


class _MTelnetSsl_Type(Unsigned32):
    """Custom type mTelnetSsl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MTelnetSsl_Type.__name__ = "Unsigned32"
_MTelnetSsl_Object = MibTableColumn
mTelnetSsl = _MTelnetSsl_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10128),
    _MTelnetSsl_Type()
)
mTelnetSsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mTelnetSsl.setStatus("current")


class _MCookieTimeToLive_Type(Unsigned32):
    """Custom type mCookieTimeToLive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MCookieTimeToLive_Type.__name__ = "Unsigned32"
_MCookieTimeToLive_Object = MibTableColumn
mCookieTimeToLive = _MCookieTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10130),
    _MCookieTimeToLive_Type()
)
mCookieTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mCookieTimeToLive.setStatus("current")
if mibBuilder.loadTexts:
    mCookieTimeToLive.setUnits("min")


class _MLineCurrentWarningThreshold_Type(Uthousandth):
    """Custom type mLineCurrentWarningThreshold based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MLineCurrentWarningThreshold_Type.__name__ = "Uthousandth"
_MLineCurrentWarningThreshold_Object = MibTableColumn
mLineCurrentWarningThreshold = _MLineCurrentWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10131),
    _MLineCurrentWarningThreshold_Type()
)
mLineCurrentWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLineCurrentWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mLineCurrentWarningThreshold.setUnits("A")


class _MLineCurrentOffThreshold_Type(Uthousandth):
    """Custom type mLineCurrentOffThreshold based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MLineCurrentOffThreshold_Type.__name__ = "Uthousandth"
_MLineCurrentOffThreshold_Object = MibTableColumn
mLineCurrentOffThreshold = _MLineCurrentOffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10132),
    _MLineCurrentOffThreshold_Type()
)
mLineCurrentOffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLineCurrentOffThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mLineCurrentOffThreshold.setUnits("A")
_MLineCurrentWarningEvent_Type = EVENTFLAGS
_MLineCurrentWarningEvent_Object = MibTableColumn
mLineCurrentWarningEvent = _MLineCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10133),
    _MLineCurrentWarningEvent_Type()
)
mLineCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLineCurrentWarningEvent.setStatus("current")
_MLineCurrentOffEvent_Type = EVENTFLAGS
_MLineCurrentOffEvent_Object = MibTableColumn
mLineCurrentOffEvent = _MLineCurrentOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10134),
    _MLineCurrentOffEvent_Type()
)
mLineCurrentOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLineCurrentOffEvent.setStatus("current")


class _MFuseCurrentWarningThreshold_Type(Uthousandth):
    """Custom type mFuseCurrentWarningThreshold based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MFuseCurrentWarningThreshold_Type.__name__ = "Uthousandth"
_MFuseCurrentWarningThreshold_Object = MibTableColumn
mFuseCurrentWarningThreshold = _MFuseCurrentWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10142),
    _MFuseCurrentWarningThreshold_Type()
)
mFuseCurrentWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mFuseCurrentWarningThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mFuseCurrentWarningThreshold.setUnits("A")


class _MFuseCurrentOffThreshold_Type(Uthousandth):
    """Custom type mFuseCurrentOffThreshold based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_MFuseCurrentOffThreshold_Type.__name__ = "Uthousandth"
_MFuseCurrentOffThreshold_Object = MibTableColumn
mFuseCurrentOffThreshold = _MFuseCurrentOffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10143),
    _MFuseCurrentOffThreshold_Type()
)
mFuseCurrentOffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mFuseCurrentOffThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mFuseCurrentOffThreshold.setUnits("A")
_MFuseCurrentWarningEvent_Type = EVENTFLAGS
_MFuseCurrentWarningEvent_Object = MibTableColumn
mFuseCurrentWarningEvent = _MFuseCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10144),
    _MFuseCurrentWarningEvent_Type()
)
mFuseCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mFuseCurrentWarningEvent.setStatus("current")
_MFuseCurrentOffEvent_Type = EVENTFLAGS
_MFuseCurrentOffEvent_Object = MibTableColumn
mFuseCurrentOffEvent = _MFuseCurrentOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10145),
    _MFuseCurrentOffEvent_Type()
)
mFuseCurrentOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mFuseCurrentOffEvent.setStatus("current")
_MDeviceID_Type = DisplayString
_MDeviceID_Object = MibTableColumn
mDeviceID = _MDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10150),
    _MDeviceID_Type()
)
mDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mDeviceID.setStatus("current")
_MDeviceVersion_Type = Version
_MDeviceVersion_Object = MibTableColumn
mDeviceVersion = _MDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10151),
    _MDeviceVersion_Type()
)
mDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mDeviceVersion.setStatus("current")
_MSysName_Type = DisplayString
_MSysName_Object = MibTableColumn
mSysName = _MSysName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10152),
    _MSysName_Type()
)
mSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSysName.setStatus("current")


class _MElectricalTopology_Type(Unsigned32):
    """Custom type mElectricalTopology based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MElectricalTopology_Type.__name__ = "Unsigned32"
_MElectricalTopology_Object = MibTableColumn
mElectricalTopology = _MElectricalTopology_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10153),
    _MElectricalTopology_Type()
)
mElectricalTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mElectricalTopology.setStatus("current")


class _MFusePortTopology_Type(Unsigned32):
    """Custom type mFusePortTopology based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_MFusePortTopology_Type.__name__ = "Unsigned32"
_MFusePortTopology_Object = MibTableColumn
mFusePortTopology = _MFusePortTopology_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10154),
    _MFusePortTopology_Type()
)
mFusePortTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mFusePortTopology.setStatus("current")


class _MLineFuseTopology_Type(Unsigned32):
    """Custom type mLineFuseTopology based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MLineFuseTopology_Type.__name__ = "Unsigned32"
_MLineFuseTopology_Object = MibTableColumn
mLineFuseTopology = _MLineFuseTopology_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10155),
    _MLineFuseTopology_Type()
)
mLineFuseTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLineFuseTopology.setStatus("current")
_MSSOIPAddress_Type = IpAddress
_MSSOIPAddress_Object = MibTableColumn
mSSOIPAddress = _MSSOIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10156),
    _MSSOIPAddress_Type()
)
mSSOIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSSOIPAddress.setStatus("current")
_MSSOLoginCredentials_Type = DisplayString
_MSSOLoginCredentials_Object = MibTableColumn
mSSOLoginCredentials = _MSSOLoginCredentials_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10157),
    _MSSOLoginCredentials_Type()
)
mSSOLoginCredentials.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSSOLoginCredentials.setStatus("current")
_MSSOGracefullShutdown_Type = DisplayString
_MSSOGracefullShutdown_Object = MibTableColumn
mSSOGracefullShutdown = _MSSOGracefullShutdown_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10158),
    _MSSOGracefullShutdown_Type()
)
mSSOGracefullShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSSOGracefullShutdown.setStatus("current")


class _MUPSWarningLevel_Type(Utenth):
    """Custom type mUPSWarningLevel based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MUPSWarningLevel_Type.__name__ = "Utenth"
_MUPSWarningLevel_Object = MibTableColumn
mUPSWarningLevel = _MUPSWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10159),
    _MUPSWarningLevel_Type()
)
mUPSWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUPSWarningLevel.setStatus("current")


class _MUPSOffLevel_Type(Utenth):
    """Custom type mUPSOffLevel based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MUPSOffLevel_Type.__name__ = "Utenth"
_MUPSOffLevel_Object = MibTableColumn
mUPSOffLevel = _MUPSOffLevel_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10160),
    _MUPSOffLevel_Type()
)
mUPSOffLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUPSOffLevel.setStatus("current")


class _MMaxHighCurrentWarning_Type(Stenth):
    """Custom type mMaxHighCurrentWarning based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMaxHighCurrentWarning_Type.__name__ = "Stenth"
_MMaxHighCurrentWarning_Object = MibTableColumn
mMaxHighCurrentWarning = _MMaxHighCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10165),
    _MMaxHighCurrentWarning_Type()
)
mMaxHighCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMaxHighCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMaxHighCurrentWarning.setUnits("A")


class _MUpsMonitoringProtocol_Type(Unsigned32):
    """Custom type mUpsMonitoringProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MUpsMonitoringProtocol_Type.__name__ = "Unsigned32"
_MUpsMonitoringProtocol_Object = MibTableColumn
mUpsMonitoringProtocol = _MUpsMonitoringProtocol_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10167),
    _MUpsMonitoringProtocol_Type()
)
mUpsMonitoringProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUpsMonitoringProtocol.setStatus("current")


class _MUpsEmergencyThreshold_Type(Utenth):
    """Custom type mUpsEmergencyThreshold based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MUpsEmergencyThreshold_Type.__name__ = "Utenth"
_MUpsEmergencyThreshold_Object = MibTableColumn
mUpsEmergencyThreshold = _MUpsEmergencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10168),
    _MUpsEmergencyThreshold_Type()
)
mUpsEmergencyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUpsEmergencyThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mUpsEmergencyThreshold.setUnits("%")


class _MUpsRecoveryThreshold_Type(Utenth):
    """Custom type mUpsRecoveryThreshold based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MUpsRecoveryThreshold_Type.__name__ = "Utenth"
_MUpsRecoveryThreshold_Object = MibTableColumn
mUpsRecoveryThreshold = _MUpsRecoveryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10169),
    _MUpsRecoveryThreshold_Type()
)
mUpsRecoveryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUpsRecoveryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mUpsRecoveryThreshold.setUnits("%")
_MUpsEventFlags_Type = EVENTFLAGS
_MUpsEventFlags_Object = MibTableColumn
mUpsEventFlags = _MUpsEventFlags_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10170),
    _MUpsEventFlags_Type()
)
mUpsEventFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUpsEventFlags.setStatus("current")


class _MRecoveryPowerThreshold_Type(Unsigned32):
    """Custom type mRecoveryPowerThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4000),
    )


_MRecoveryPowerThreshold_Type.__name__ = "Unsigned32"
_MRecoveryPowerThreshold_Object = MibTableColumn
mRecoveryPowerThreshold = _MRecoveryPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10171),
    _MRecoveryPowerThreshold_Type()
)
mRecoveryPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mRecoveryPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mRecoveryPowerThreshold.setUnits("W")


class _MMinHighCurrentWarning_Type(Stenth):
    """Custom type mMinHighCurrentWarning based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMinHighCurrentWarning_Type.__name__ = "Stenth"
_MMinHighCurrentWarning_Object = MibTableColumn
mMinHighCurrentWarning = _MMinHighCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10176),
    _MMinHighCurrentWarning_Type()
)
mMinHighCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMinHighCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMinHighCurrentWarning.setUnits("A")


class _MMinHighPowerWarning_Type(Shundredth):
    """Custom type mMinHighPowerWarning based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMinHighPowerWarning_Type.__name__ = "Shundredth"
_MMinHighPowerWarning_Object = MibTableColumn
mMinHighPowerWarning = _MMinHighPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10177),
    _MMinHighPowerWarning_Type()
)
mMinHighPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMinHighPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMinHighPowerWarning.setUnits("kW")


class _MMaxHighPowerWarning_Type(Shundredth):
    """Custom type mMaxHighPowerWarning based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMaxHighPowerWarning_Type.__name__ = "Shundredth"
_MMaxHighPowerWarning_Object = MibTableColumn
mMaxHighPowerWarning = _MMaxHighPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10178),
    _MMaxHighPowerWarning_Type()
)
mMaxHighPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMaxHighPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMaxHighPowerWarning.setUnits("kW")


class _MHeartbeatInterval_Type(Unsigned32):
    """Custom type mHeartbeatInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MHeartbeatInterval_Type.__name__ = "Unsigned32"
_MHeartbeatInterval_Object = MibTableColumn
mHeartbeatInterval = _MHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10179),
    _MHeartbeatInterval_Type()
)
mHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mHeartbeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    mHeartbeatInterval.setUnits("s")


class _MMinTotalHighCurrentWarning_Type(Stenth):
    """Custom type mMinTotalHighCurrentWarning based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMinTotalHighCurrentWarning_Type.__name__ = "Stenth"
_MMinTotalHighCurrentWarning_Object = MibTableColumn
mMinTotalHighCurrentWarning = _MMinTotalHighCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10180),
    _MMinTotalHighCurrentWarning_Type()
)
mMinTotalHighCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMinTotalHighCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMinTotalHighCurrentWarning.setUnits("A")


class _MMaxTotalHighCurrentWarning_Type(Stenth):
    """Custom type mMaxTotalHighCurrentWarning based on Stenth"""
    subtypeSpec = Stenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMaxTotalHighCurrentWarning_Type.__name__ = "Stenth"
_MMaxTotalHighCurrentWarning_Object = MibTableColumn
mMaxTotalHighCurrentWarning = _MMaxTotalHighCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10181),
    _MMaxTotalHighCurrentWarning_Type()
)
mMaxTotalHighCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMaxTotalHighCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMaxTotalHighCurrentWarning.setUnits("A")


class _MMinTotalHighPowerWarning_Type(Shundredth):
    """Custom type mMinTotalHighPowerWarning based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMinTotalHighPowerWarning_Type.__name__ = "Shundredth"
_MMinTotalHighPowerWarning_Object = MibTableColumn
mMinTotalHighPowerWarning = _MMinTotalHighPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10182),
    _MMinTotalHighPowerWarning_Type()
)
mMinTotalHighPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMinTotalHighPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMinTotalHighPowerWarning.setUnits("kW")


class _MMaxTotalHighPowerWarning_Type(Shundredth):
    """Custom type mMaxTotalHighPowerWarning based on Shundredth"""
    subtypeSpec = Shundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MMaxTotalHighPowerWarning_Type.__name__ = "Shundredth"
_MMaxTotalHighPowerWarning_Object = MibTableColumn
mMaxTotalHighPowerWarning = _MMaxTotalHighPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10183),
    _MMaxTotalHighPowerWarning_Type()
)
mMaxTotalHighPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mMaxTotalHighPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    mMaxTotalHighPowerWarning.setUnits("kW")


class _MCloudState_Type(Unsigned32):
    """Custom type mCloudState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MCloudState_Type.__name__ = "Unsigned32"
_MCloudState_Object = MibTableColumn
mCloudState = _MCloudState_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10208),
    _MCloudState_Type()
)
mCloudState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mCloudState.setStatus("current")


class _MSensorBias_Type(Integer32):
    """Custom type mSensorBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MSensorBias_Type.__name__ = "Integer32"
_MSensorBias_Object = MibTableColumn
mSensorBias = _MSensorBias_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10210),
    _MSensorBias_Type()
)
mSensorBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSensorBias.setStatus("current")
if mibBuilder.loadTexts:
    mSensorBias.setUnits("mV")


class _MDaisyChainDeviceMode_Type(Unsigned32):
    """Custom type mDaisyChainDeviceMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MDaisyChainDeviceMode_Type.__name__ = "Unsigned32"
_MDaisyChainDeviceMode_Object = MibTableColumn
mDaisyChainDeviceMode = _MDaisyChainDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10211),
    _MDaisyChainDeviceMode_Type()
)
mDaisyChainDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mDaisyChainDeviceMode.setStatus("current")


class _MSNMPTrapUser_Type(Unsigned32):
    """Custom type mSNMPTrapUser based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MSNMPTrapUser_Type.__name__ = "Unsigned32"
_MSNMPTrapUser_Object = MibTableColumn
mSNMPTrapUser = _MSNMPTrapUser_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10212),
    _MSNMPTrapUser_Type()
)
mSNMPTrapUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPTrapUser.setStatus("current")
_MUSMUser_Type = DisplayString
_MUSMUser_Object = MibTableColumn
mUSMUser = _MUSMUser_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10213),
    _MUSMUser_Type()
)
mUSMUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUSMUser.setStatus("current")
_MUSMAuthPassphrase_Type = DisplayString
_MUSMAuthPassphrase_Object = MibTableColumn
mUSMAuthPassphrase = _MUSMAuthPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10214),
    _MUSMAuthPassphrase_Type()
)
mUSMAuthPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUSMAuthPassphrase.setStatus("current")
_MUSMPrivPassphrase_Type = DisplayString
_MUSMPrivPassphrase_Object = MibTableColumn
mUSMPrivPassphrase = _MUSMPrivPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10215),
    _MUSMPrivPassphrase_Type()
)
mUSMPrivPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUSMPrivPassphrase.setStatus("current")


class _MSNMPV2GetSetEnable_Type(Unsigned32):
    """Custom type mSNMPV2GetSetEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MSNMPV2GetSetEnable_Type.__name__ = "Unsigned32"
_MSNMPV2GetSetEnable_Object = MibTableColumn
mSNMPV2GetSetEnable = _MSNMPV2GetSetEnable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10216),
    _MSNMPV2GetSetEnable_Type()
)
mSNMPV2GetSetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPV2GetSetEnable.setStatus("current")


class _MSNMPV3GetSetEnable_Type(Unsigned32):
    """Custom type mSNMPV3GetSetEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MSNMPV3GetSetEnable_Type.__name__ = "Unsigned32"
_MSNMPV3GetSetEnable_Object = MibTableColumn
mSNMPV3GetSetEnable = _MSNMPV3GetSetEnable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10217),
    _MSNMPV3GetSetEnable_Type()
)
mSNMPV3GetSetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPV3GetSetEnable.setStatus("current")


class _MUSMAuthPassphraseLength_Type(Unsigned32):
    """Custom type mUSMAuthPassphraseLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MUSMAuthPassphraseLength_Type.__name__ = "Unsigned32"
_MUSMAuthPassphraseLength_Object = MibTableColumn
mUSMAuthPassphraseLength = _MUSMAuthPassphraseLength_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10218),
    _MUSMAuthPassphraseLength_Type()
)
mUSMAuthPassphraseLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUSMAuthPassphraseLength.setStatus("current")


class _MUSMPrivPassphraseLength_Type(Unsigned32):
    """Custom type mUSMPrivPassphraseLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MUSMPrivPassphraseLength_Type.__name__ = "Unsigned32"
_MUSMPrivPassphraseLength_Object = MibTableColumn
mUSMPrivPassphraseLength = _MUSMPrivPassphraseLength_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10219),
    _MUSMPrivPassphraseLength_Type()
)
mUSMPrivPassphraseLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mUSMPrivPassphraseLength.setStatus("current")


class _MSNMPTrapEnable_Type(Unsigned32):
    """Custom type mSNMPTrapEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MSNMPTrapEnable_Type.__name__ = "Unsigned32"
_MSNMPTrapEnable_Object = MibTableColumn
mSNMPTrapEnable = _MSNMPTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10222),
    _MSNMPTrapEnable_Type()
)
mSNMPTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSNMPTrapEnable.setStatus("current")
_MLDAPAttribute_Type = DisplayString
_MLDAPAttribute_Object = MibTableColumn
mLDAPAttribute = _MLDAPAttribute_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10227),
    _MLDAPAttribute_Type()
)
mLDAPAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPAttribute.setStatus("current")
_MLDAPPath_Type = DisplayString
_MLDAPPath_Object = MibTableColumn
mLDAPPath = _MLDAPPath_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10228),
    _MLDAPPath_Type()
)
mLDAPPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPPath.setStatus("current")
_MLDAPAdminGroupName_Type = DisplayString
_MLDAPAdminGroupName_Object = MibTableColumn
mLDAPAdminGroupName = _MLDAPAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10229),
    _MLDAPAdminGroupName_Type()
)
mLDAPAdminGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPAdminGroupName.setStatus("current")
_MLDAPRestrictedGroupName_Type = DisplayString
_MLDAPRestrictedGroupName_Object = MibTableColumn
mLDAPRestrictedGroupName = _MLDAPRestrictedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10230),
    _MLDAPRestrictedGroupName_Type()
)
mLDAPRestrictedGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPRestrictedGroupName.setStatus("current")
_MLDAPGuestGroupName_Type = DisplayString
_MLDAPGuestGroupName_Object = MibTableColumn
mLDAPGuestGroupName = _MLDAPGuestGroupName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10231),
    _MLDAPGuestGroupName_Type()
)
mLDAPGuestGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPGuestGroupName.setStatus("current")


class _MLDAPEnable_Type(Unsigned32):
    """Custom type mLDAPEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MLDAPEnable_Type.__name__ = "Unsigned32"
_MLDAPEnable_Object = MibTableColumn
mLDAPEnable = _MLDAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10232),
    _MLDAPEnable_Type()
)
mLDAPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPEnable.setStatus("current")
_MLDAPLoginWrapper_Type = DisplayString
_MLDAPLoginWrapper_Object = MibTableColumn
mLDAPLoginWrapper = _MLDAPLoginWrapper_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10233),
    _MLDAPLoginWrapper_Type()
)
mLDAPLoginWrapper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPLoginWrapper.setStatus("current")
_MLDAPServer_Type = DisplayString
_MLDAPServer_Object = MibTableColumn
mLDAPServer = _MLDAPServer_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10235),
    _MLDAPServer_Type()
)
mLDAPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLDAPServer.setStatus("current")


class _MLocalAuthEnable_Type(Unsigned32):
    """Custom type mLocalAuthEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MLocalAuthEnable_Type.__name__ = "Unsigned32"
_MLocalAuthEnable_Object = MibTableColumn
mLocalAuthEnable = _MLocalAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 10236),
    _MLocalAuthEnable_Type()
)
mLocalAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLocalAuthEnable.setStatus("current")


class _MasterIndex_Type(Integer32):
    """Custom type masterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MasterIndex_Type.__name__ = "Integer32"
_MasterIndex_Object = MibTableColumn
masterIndex = _MasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 65537),
    _MasterIndex_Type()
)
masterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    masterIndex.setStatus("current")


class _MasterModuleIndex_Type(Integer32):
    """Custom type masterModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MasterModuleIndex_Type.__name__ = "Integer32"
_MasterModuleIndex_Object = MibTableColumn
masterModuleIndex = _MasterModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 77, 1, 1, 65538),
    _MasterModuleIndex_Type()
)
masterModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    masterModuleIndex.setStatus("current")
_PowerModule_ObjectIdentity = ObjectIdentity
powerModule = _PowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80)
)
_EPowerTable_Object = MibTable
ePowerTable = _EPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1)
)
if mibBuilder.loadTexts:
    ePowerTable.setStatus("current")
_EPowerEntry_Object = MibTableRow
ePowerEntry = _EPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1)
)
ePowerEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "powerModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    ePowerEntry.setStatus("current")
_PGeneralModuleStatus_Type = Unsigned32
_PGeneralModuleStatus_Object = MibTableColumn
pGeneralModuleStatus = _PGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 1),
    _PGeneralModuleStatus_Type()
)
pGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pGeneralModuleStatus.setStatus("current")
_PSpecificModuleStatus_Type = Unsigned32
_PSpecificModuleStatus_Object = MibTableColumn
pSpecificModuleStatus = _PSpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 2),
    _PSpecificModuleStatus_Type()
)
pSpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSpecificModuleStatus.setStatus("current")
_PCurrentTime_Type = TimeTicks
_PCurrentTime_Object = MibTableColumn
pCurrentTime = _PCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 3),
    _PCurrentTime_Type()
)
pCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    pCurrentTime.setUnits("UNIX")
_PVoltage_Type = Uhundredth
_PVoltage_Object = MibTableColumn
pVoltage = _PVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 4),
    _PVoltage_Type()
)
pVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pVoltage.setUnits("V")
_PFrequency_Type = Uthousandth
_PFrequency_Object = MibTableColumn
pFrequency = _PFrequency_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 5),
    _PFrequency_Type()
)
pFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pFrequency.setUnits("Hz")
_PCurrent_Type = Uthousandth
_PCurrent_Object = MibTableColumn
pCurrent = _PCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 6),
    _PCurrent_Type()
)
pCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pCurrent.setUnits("A")
_PPower_Type = Unsigned32
_PPower_Object = MibTableColumn
pPower = _PPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 7),
    _PPower_Type()
)
pPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPower.setStatus("current")
if mibBuilder.loadTexts:
    pPower.setUnits("W")
_PStatePortCur_Type = CURPORTSTATE
_PStatePortCur_Object = MibTableColumn
pStatePortCur = _PStatePortCur_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 8),
    _PStatePortCur_Type()
)
pStatePortCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pStatePortCur.setStatus("current")
_PActiveEnergy_Type = Uthousandth
_PActiveEnergy_Object = MibTableColumn
pActiveEnergy = _PActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 9),
    _PActiveEnergy_Type()
)
pActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pActiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pActiveEnergy.setUnits("kWh")
_PApparentEnergy_Type = Uthousandth
_PApparentEnergy_Object = MibTableColumn
pApparentEnergy = _PApparentEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10),
    _PApparentEnergy_Type()
)
pApparentEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pApparentEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pApparentEnergy.setUnits("kVAh")
_PTemperature_Type = Utenth
_PTemperature_Object = MibTableColumn
pTemperature = _PTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 11),
    _PTemperature_Type()
)
pTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTemperature.setStatus("current")
if mibBuilder.loadTexts:
    pTemperature.setUnits("K")
_PApparentPower_Type = Unsigned32
_PApparentPower_Object = MibTableColumn
pApparentPower = _PApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 15),
    _PApparentPower_Type()
)
pApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pApparentPower.setUnits("VA")
_PPowerFactor_Type = Unsigned32
_PPowerFactor_Object = MibTableColumn
pPowerFactor = _PPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 16),
    _PPowerFactor_Type()
)
pPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pPowerFactor.setUnits("%")
_PTotalCurrent_Type = Uthousandth
_PTotalCurrent_Object = MibTableColumn
pTotalCurrent = _PTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 17),
    _PTotalCurrent_Type()
)
pTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pTotalCurrent.setUnits("A")
_PTotalRealPower_Type = Unsigned32
_PTotalRealPower_Object = MibTableColumn
pTotalRealPower = _PTotalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 18),
    _PTotalRealPower_Type()
)
pTotalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    pTotalRealPower.setUnits("W")
_PTotalApparentPower_Type = Unsigned32
_PTotalApparentPower_Object = MibTableColumn
pTotalApparentPower = _PTotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 19),
    _PTotalApparentPower_Type()
)
pTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pTotalApparentPower.setUnits("VA")
_PTotalActiveEnergy_Type = Uthousandth
_PTotalActiveEnergy_Object = MibTableColumn
pTotalActiveEnergy = _PTotalActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 20),
    _PTotalActiveEnergy_Type()
)
pTotalActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalActiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pTotalActiveEnergy.setUnits("kWh")
_PTotalApparentEnergy_Type = Uthousandth
_PTotalApparentEnergy_Object = MibTableColumn
pTotalApparentEnergy = _PTotalApparentEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 21),
    _PTotalApparentEnergy_Type()
)
pTotalApparentEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalApparentEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pTotalApparentEnergy.setUnits("kVAh")
_PTotalPowerFactor_Type = Unsigned32
_PTotalPowerFactor_Object = MibTableColumn
pTotalPowerFactor = _PTotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 22),
    _PTotalPowerFactor_Type()
)
pTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pTotalPowerFactor.setUnits("%")
_PTimeOnline_Type = Unsigned32
_PTimeOnline_Object = MibTableColumn
pTimeOnline = _PTimeOnline_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 24),
    _PTimeOnline_Type()
)
pTimeOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTimeOnline.setStatus("current")
if mibBuilder.loadTexts:
    pTimeOnline.setUnits("s")


class _PTotalHarmonicDistortion_Type(Utenth):
    """Custom type pTotalHarmonicDistortion based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PTotalHarmonicDistortion_Type.__name__ = "Utenth"
_PTotalHarmonicDistortion_Object = MibTableColumn
pTotalHarmonicDistortion = _PTotalHarmonicDistortion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 50),
    _PTotalHarmonicDistortion_Type()
)
pTotalHarmonicDistortion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalHarmonicDistortion.setStatus("current")
if mibBuilder.loadTexts:
    pTotalHarmonicDistortion.setUnits("%")


class _PPhase_Type(Unsigned32):
    """Custom type pPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PPhase_Type.__name__ = "Unsigned32"
_PPhase_Object = MibTableColumn
pPhase = _PPhase_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 51),
    _PPhase_Type()
)
pPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPhase.setStatus("current")
if mibBuilder.loadTexts:
    pPhase.setUnits("degr")
_PBigCurrent_Type = Unsigned32
_PBigCurrent_Object = MibTableColumn
pBigCurrent = _PBigCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 52),
    _PBigCurrent_Type()
)
pBigCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBigCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pBigCurrent.setUnits("A")
_PBigPower_Type = Uthousandth
_PBigPower_Object = MibTableColumn
pBigPower = _PBigPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 53),
    _PBigPower_Type()
)
pBigPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBigPower.setStatus("current")
if mibBuilder.loadTexts:
    pBigPower.setUnits("W")
_PBigApparentPower_Type = Uthousandth
_PBigApparentPower_Object = MibTableColumn
pBigApparentPower = _PBigApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 54),
    _PBigApparentPower_Type()
)
pBigApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBigApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pBigApparentPower.setUnits("VA")


class _PDetectedPhase_Type(Unsigned32):
    """Custom type pDetectedPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PDetectedPhase_Type.__name__ = "Unsigned32"
_PDetectedPhase_Object = MibTableColumn
pDetectedPhase = _PDetectedPhase_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 55),
    _PDetectedPhase_Type()
)
pDetectedPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDetectedPhase.setStatus("current")
_PModuleName_Type = DisplayString
_PModuleName_Object = MibTableColumn
pModuleName = _PModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10001),
    _PModuleName_Type()
)
pModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pModuleName.setStatus("current")
_PFirmwareVersion_Type = Version
_PFirmwareVersion_Object = MibTableColumn
pFirmwareVersion = _PFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10002),
    _PFirmwareVersion_Type()
)
pFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFirmwareVersion.setStatus("current")
_PHardwareVersion_Type = Version
_PHardwareVersion_Object = MibTableColumn
pHardwareVersion = _PHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10003),
    _PHardwareVersion_Type()
)
pHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pHardwareVersion.setStatus("current")
_PFirmwareID_Type = DisplayString
_PFirmwareID_Object = MibTableColumn
pFirmwareID = _PFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10004),
    _PFirmwareID_Type()
)
pFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFirmwareID.setStatus("current")
_PHardwareID_Type = DisplayString
_PHardwareID_Object = MibTableColumn
pHardwareID = _PHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10005),
    _PHardwareID_Type()
)
pHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pHardwareID.setStatus("current")
_PPortName_Type = DisplayString
_PPortName_Object = MibTableColumn
pPortName = _PPortName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10034),
    _PPortName_Type()
)
pPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortName.setStatus("current")


class _PPortState_Type(Unsigned32):
    """Custom type pPortState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PPortState_Type.__name__ = "Unsigned32"
_PPortState_Object = MibTableColumn
pPortState = _PPortState_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10035),
    _PPortState_Type()
)
pPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortState.setStatus("current")


class _PCurrentPriorOff_Type(Unsigned32):
    """Custom type pCurrentPriorOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PCurrentPriorOff_Type.__name__ = "Unsigned32"
_PCurrentPriorOff_Object = MibTableColumn
pCurrentPriorOff = _PCurrentPriorOff_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10036),
    _PCurrentPriorOff_Type()
)
pCurrentPriorOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCurrentPriorOff.setStatus("current")


class _PDelayOn_Type(Unsigned32):
    """Custom type pDelayOn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PDelayOn_Type.__name__ = "Unsigned32"
_PDelayOn_Object = MibTableColumn
pDelayOn = _PDelayOn_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10037),
    _PDelayOn_Type()
)
pDelayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDelayOn.setStatus("current")
if mibBuilder.loadTexts:
    pDelayOn.setUnits("s")


class _PMaxCurrentOff_Type(Uthousandth):
    """Custom type pMaxCurrentOff based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8000),
    )


_PMaxCurrentOff_Type.__name__ = "Uthousandth"
_PMaxCurrentOff_Object = MibTableColumn
pMaxCurrentOff = _PMaxCurrentOff_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10038),
    _PMaxCurrentOff_Type()
)
pMaxCurrentOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxCurrentOff.setStatus("current")
if mibBuilder.loadTexts:
    pMaxCurrentOff.setUnits("A")


class _PMaxCurrentWarning_Type(Uthousandth):
    """Custom type pMaxCurrentWarning based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 8000),
    )


_PMaxCurrentWarning_Type.__name__ = "Uthousandth"
_PMaxCurrentWarning_Object = MibTableColumn
pMaxCurrentWarning = _PMaxCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10039),
    _PMaxCurrentWarning_Type()
)
pMaxCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxCurrentWarning.setUnits("A")


class _PMaxPowerOff_Type(Unsigned32):
    """Custom type pMaxPowerOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_PMaxPowerOff_Type.__name__ = "Unsigned32"
_PMaxPowerOff_Object = MibTableColumn
pMaxPowerOff = _PMaxPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10040),
    _PMaxPowerOff_Type()
)
pMaxPowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxPowerOff.setStatus("current")
if mibBuilder.loadTexts:
    pMaxPowerOff.setUnits("W")


class _PMaxPowerWarning_Type(Unsigned32):
    """Custom type pMaxPowerWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_PMaxPowerWarning_Type.__name__ = "Unsigned32"
_PMaxPowerWarning_Object = MibTableColumn
pMaxPowerWarning = _PMaxPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10041),
    _PMaxPowerWarning_Type()
)
pMaxPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxPowerWarning.setUnits("W")


class _PMaxTotalCurrentOff_Type(Uthousandth):
    """Custom type pMaxTotalCurrentOff based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 16000),
    )


_PMaxTotalCurrentOff_Type.__name__ = "Uthousandth"
_PMaxTotalCurrentOff_Object = MibTableColumn
pMaxTotalCurrentOff = _PMaxTotalCurrentOff_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10042),
    _PMaxTotalCurrentOff_Type()
)
pMaxTotalCurrentOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxTotalCurrentOff.setStatus("current")
if mibBuilder.loadTexts:
    pMaxTotalCurrentOff.setUnits("A")


class _PMaxTotalCurrentWarning_Type(Uthousandth):
    """Custom type pMaxTotalCurrentWarning based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 16000),
    )


_PMaxTotalCurrentWarning_Type.__name__ = "Uthousandth"
_PMaxTotalCurrentWarning_Object = MibTableColumn
pMaxTotalCurrentWarning = _PMaxTotalCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10043),
    _PMaxTotalCurrentWarning_Type()
)
pMaxTotalCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxTotalCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxTotalCurrentWarning.setUnits("A")


class _PMaxTotalPowerOff_Type(Unsigned32):
    """Custom type pMaxTotalPowerOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4000),
    )


_PMaxTotalPowerOff_Type.__name__ = "Unsigned32"
_PMaxTotalPowerOff_Object = MibTableColumn
pMaxTotalPowerOff = _PMaxTotalPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10044),
    _PMaxTotalPowerOff_Type()
)
pMaxTotalPowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxTotalPowerOff.setStatus("current")
if mibBuilder.loadTexts:
    pMaxTotalPowerOff.setUnits("W")


class _PMaxTotalPowerWarning_Type(Unsigned32):
    """Custom type pMaxTotalPowerWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4000),
    )


_PMaxTotalPowerWarning_Type.__name__ = "Unsigned32"
_PMaxTotalPowerWarning_Object = MibTableColumn
pMaxTotalPowerWarning = _PMaxTotalPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10045),
    _PMaxTotalPowerWarning_Type()
)
pMaxTotalPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxTotalPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxTotalPowerWarning.setUnits("W")


class _PMaxVoltageWarning_Type(Uhundredth):
    """Custom type pMaxVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 30000),
    )


_PMaxVoltageWarning_Type.__name__ = "Uhundredth"
_PMaxVoltageWarning_Object = MibTableColumn
pMaxVoltageWarning = _PMaxVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10047),
    _PMaxVoltageWarning_Type()
)
pMaxVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxVoltageWarning.setUnits("V")


class _PMinVoltageWarning_Type(Uhundredth):
    """Custom type pMinVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 30000),
    )


_PMinVoltageWarning_Type.__name__ = "Uhundredth"
_PMinVoltageWarning_Object = MibTableColumn
pMinVoltageWarning = _PMinVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10049),
    _PMinVoltageWarning_Type()
)
pMinVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMinVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMinVoltageWarning.setUnits("V")


class _PMinTemperatureWarning_Type(Utenth):
    """Custom type pMinTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_PMinTemperatureWarning_Type.__name__ = "Utenth"
_PMinTemperatureWarning_Object = MibTableColumn
pMinTemperatureWarning = _PMinTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10052),
    _PMinTemperatureWarning_Type()
)
pMinTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMinTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMinTemperatureWarning.setUnits("K")


class _PMaxTemperatureWarning_Type(Utenth):
    """Custom type pMaxTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_PMaxTemperatureWarning_Type.__name__ = "Utenth"
_PMaxTemperatureWarning_Object = MibTableColumn
pMaxTemperatureWarning = _PMaxTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10053),
    _PMaxTemperatureWarning_Type()
)
pMaxTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxTemperatureWarning.setUnits("K")
_PPortStateEvent_Type = EVENTFLAGS
_PPortStateEvent_Object = MibTableColumn
pPortStateEvent = _PPortStateEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10076),
    _PPortStateEvent_Type()
)
pPortStateEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPortStateEvent.setStatus("current")
_PCurrentOffEvent_Type = EVENTFLAGS
_PCurrentOffEvent_Object = MibTableColumn
pCurrentOffEvent = _PCurrentOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10077),
    _PCurrentOffEvent_Type()
)
pCurrentOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCurrentOffEvent.setStatus("current")
_PCurrentWarningEvent_Type = EVENTFLAGS
_PCurrentWarningEvent_Object = MibTableColumn
pCurrentWarningEvent = _PCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10078),
    _PCurrentWarningEvent_Type()
)
pCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCurrentWarningEvent.setStatus("current")
_PPowerOffEvent_Type = EVENTFLAGS
_PPowerOffEvent_Object = MibTableColumn
pPowerOffEvent = _PPowerOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10079),
    _PPowerOffEvent_Type()
)
pPowerOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPowerOffEvent.setStatus("current")
_PPowerWarningEvent_Type = EVENTFLAGS
_PPowerWarningEvent_Object = MibTableColumn
pPowerWarningEvent = _PPowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10080),
    _PPowerWarningEvent_Type()
)
pPowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPowerWarningEvent.setStatus("current")
_PTotalCurrentOffEvent_Type = EVENTFLAGS
_PTotalCurrentOffEvent_Object = MibTableColumn
pTotalCurrentOffEvent = _PTotalCurrentOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10081),
    _PTotalCurrentOffEvent_Type()
)
pTotalCurrentOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTotalCurrentOffEvent.setStatus("current")
_PTotalCurrentWarningEvent_Type = EVENTFLAGS
_PTotalCurrentWarningEvent_Object = MibTableColumn
pTotalCurrentWarningEvent = _PTotalCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10082),
    _PTotalCurrentWarningEvent_Type()
)
pTotalCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTotalCurrentWarningEvent.setStatus("current")
_PTotalPowerOffEvent_Type = EVENTFLAGS
_PTotalPowerOffEvent_Object = MibTableColumn
pTotalPowerOffEvent = _PTotalPowerOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10083),
    _PTotalPowerOffEvent_Type()
)
pTotalPowerOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTotalPowerOffEvent.setStatus("current")
_PTotalPowerWarningEvent_Type = EVENTFLAGS
_PTotalPowerWarningEvent_Object = MibTableColumn
pTotalPowerWarningEvent = _PTotalPowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10084),
    _PTotalPowerWarningEvent_Type()
)
pTotalPowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTotalPowerWarningEvent.setStatus("current")
_PVoltageWarningEvent_Type = EVENTFLAGS
_PVoltageWarningEvent_Object = MibTableColumn
pVoltageWarningEvent = _PVoltageWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10086),
    _PVoltageWarningEvent_Type()
)
pVoltageWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pVoltageWarningEvent.setStatus("current")
_PTemperatureWarningEvent_Type = EVENTFLAGS
_PTemperatureWarningEvent_Object = MibTableColumn
pTemperatureWarningEvent = _PTemperatureWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10087),
    _PTemperatureWarningEvent_Type()
)
pTemperatureWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTemperatureWarningEvent.setStatus("current")


class _PMaxOverheatingOff_Type(Utenth):
    """Custom type pMaxOverheatingOff based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_PMaxOverheatingOff_Type.__name__ = "Utenth"
_PMaxOverheatingOff_Object = MibTableColumn
pMaxOverheatingOff = _PMaxOverheatingOff_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10090),
    _PMaxOverheatingOff_Type()
)
pMaxOverheatingOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxOverheatingOff.setStatus("current")
if mibBuilder.loadTexts:
    pMaxOverheatingOff.setUnits("K")
_POverheatingOffEvent_Type = EVENTFLAGS
_POverheatingOffEvent_Object = MibTableColumn
pOverheatingOffEvent = _POverheatingOffEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10091),
    _POverheatingOffEvent_Type()
)
pOverheatingOffEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOverheatingOffEvent.setStatus("current")


class _PPowerCycleTime_Type(Unsigned32):
    """Custom type pPowerCycleTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PPowerCycleTime_Type.__name__ = "Unsigned32"
_PPowerCycleTime_Object = MibTableColumn
pPowerCycleTime = _PPowerCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10099),
    _PPowerCycleTime_Type()
)
pPowerCycleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPowerCycleTime.setStatus("current")
if mibBuilder.loadTexts:
    pPowerCycleTime.setUnits("s")
_PExternalSensorLabel_Type = DisplayString
_PExternalSensorLabel_Object = MibTableColumn
pExternalSensorLabel = _PExternalSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10109),
    _PExternalSensorLabel_Type()
)
pExternalSensorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pExternalSensorLabel.setStatus("current")


class _PMaxOverheatingWarning_Type(Utenth):
    """Custom type pMaxOverheatingWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_PMaxOverheatingWarning_Type.__name__ = "Utenth"
_PMaxOverheatingWarning_Object = MibTableColumn
pMaxOverheatingWarning = _PMaxOverheatingWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10121),
    _PMaxOverheatingWarning_Type()
)
pMaxOverheatingWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxOverheatingWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxOverheatingWarning.setUnits("K")
_POverheatingWarningEvent_Type = EVENTFLAGS
_POverheatingWarningEvent_Object = MibTableColumn
pOverheatingWarningEvent = _POverheatingWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10122),
    _POverheatingWarningEvent_Type()
)
pOverheatingWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOverheatingWarningEvent.setStatus("current")


class _PMicroIntTimeThreshold_Type(Utenth):
    """Custom type pMicroIntTimeThreshold based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_PMicroIntTimeThreshold_Type.__name__ = "Utenth"
_PMicroIntTimeThreshold_Object = MibTableColumn
pMicroIntTimeThreshold = _PMicroIntTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10135),
    _PMicroIntTimeThreshold_Type()
)
pMicroIntTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMicroIntTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pMicroIntTimeThreshold.setUnits("ms")
_PMicroIntEvent_Type = EVENTFLAGS
_PMicroIntEvent_Object = MibTableColumn
pMicroIntEvent = _PMicroIntEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10136),
    _PMicroIntEvent_Type()
)
pMicroIntEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMicroIntEvent.setStatus("current")


class _PSoftFuseCurrentThreshold_Type(Unsigned32):
    """Custom type pSoftFuseCurrentThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PSoftFuseCurrentThreshold_Type.__name__ = "Unsigned32"
_PSoftFuseCurrentThreshold_Object = MibTableColumn
pSoftFuseCurrentThreshold = _PSoftFuseCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10137),
    _PSoftFuseCurrentThreshold_Type()
)
pSoftFuseCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSoftFuseCurrentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pSoftFuseCurrentThreshold.setUnits("A")


class _PSoftFuseDelay_Type(Unsigned32):
    """Custom type pSoftFuseDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PSoftFuseDelay_Type.__name__ = "Unsigned32"
_PSoftFuseDelay_Object = MibTableColumn
pSoftFuseDelay = _PSoftFuseDelay_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10138),
    _PSoftFuseDelay_Type()
)
pSoftFuseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSoftFuseDelay.setStatus("current")
if mibBuilder.loadTexts:
    pSoftFuseDelay.setUnits("ms")
_PSoftFuseEvent_Type = EVENTFLAGS
_PSoftFuseEvent_Object = MibTableColumn
pSoftFuseEvent = _PSoftFuseEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10139),
    _PSoftFuseEvent_Type()
)
pSoftFuseEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSoftFuseEvent.setStatus("current")
_PPhaseShiftEvent_Type = EVENTFLAGS
_PPhaseShiftEvent_Object = MibTableColumn
pPhaseShiftEvent = _PPhaseShiftEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10140),
    _PPhaseShiftEvent_Type()
)
pPhaseShiftEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPhaseShiftEvent.setStatus("current")


class _PSchedulePortOnTime_Type(Unsigned32):
    """Custom type pSchedulePortOnTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_PSchedulePortOnTime_Type.__name__ = "Unsigned32"
_PSchedulePortOnTime_Object = MibTableColumn
pSchedulePortOnTime = _PSchedulePortOnTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10146),
    _PSchedulePortOnTime_Type()
)
pSchedulePortOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSchedulePortOnTime.setStatus("current")
if mibBuilder.loadTexts:
    pSchedulePortOnTime.setUnits("min")


class _PSchedulePortOffTime_Type(Unsigned32):
    """Custom type pSchedulePortOffTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_PSchedulePortOffTime_Type.__name__ = "Unsigned32"
_PSchedulePortOffTime_Object = MibTableColumn
pSchedulePortOffTime = _PSchedulePortOffTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10147),
    _PSchedulePortOffTime_Type()
)
pSchedulePortOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSchedulePortOffTime.setStatus("current")
if mibBuilder.loadTexts:
    pSchedulePortOffTime.setUnits("min")


class _PEnableSchedulePort_Type(Unsigned32):
    """Custom type pEnableSchedulePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PEnableSchedulePort_Type.__name__ = "Unsigned32"
_PEnableSchedulePort_Object = MibTableColumn
pEnableSchedulePort = _PEnableSchedulePort_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10148),
    _PEnableSchedulePort_Type()
)
pEnableSchedulePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pEnableSchedulePort.setStatus("current")


class _PBlockSetPortOff_Type(Unsigned32):
    """Custom type pBlockSetPortOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PBlockSetPortOff_Type.__name__ = "Unsigned32"
_PBlockSetPortOff_Object = MibTableColumn
pBlockSetPortOff = _PBlockSetPortOff_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10161),
    _PBlockSetPortOff_Type()
)
pBlockSetPortOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBlockSetPortOff.setStatus("current")
_PSchedulePortChangeEvent_Type = EVENTFLAGS
_PSchedulePortChangeEvent_Object = MibTableColumn
pSchedulePortChangeEvent = _PSchedulePortChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10166),
    _PSchedulePortChangeEvent_Type()
)
pSchedulePortChangeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSchedulePortChangeEvent.setStatus("current")
_PAgentIP_Type = IpAddress
_PAgentIP_Object = MibTableColumn
pAgentIP = _PAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10172),
    _PAgentIP_Type()
)
pAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAgentIP.setStatus("current")


class _PAgentPort_Type(Unsigned32):
    """Custom type pAgentPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PAgentPort_Type.__name__ = "Unsigned32"
_PAgentPort_Object = MibTableColumn
pAgentPort = _PAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10173),
    _PAgentPort_Type()
)
pAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAgentPort.setStatus("current")
_PAgentCommunicationEventFlags_Type = EVENTFLAGS
_PAgentCommunicationEventFlags_Object = MibTableColumn
pAgentCommunicationEventFlags = _PAgentCommunicationEventFlags_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10174),
    _PAgentCommunicationEventFlags_Type()
)
pAgentCommunicationEventFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAgentCommunicationEventFlags.setStatus("current")


class _PAlwaysOn_Type(Unsigned32):
    """Custom type pAlwaysOn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PAlwaysOn_Type.__name__ = "Unsigned32"
_PAlwaysOn_Object = MibTableColumn
pAlwaysOn = _PAlwaysOn_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10175),
    _PAlwaysOn_Type()
)
pAlwaysOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAlwaysOn.setStatus("current")


class _PGenericTransducerParameters_Type(Integer32):
    """Custom type pGenericTransducerParameters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2000000000),
    )


_PGenericTransducerParameters_Type.__name__ = "Integer32"
_PGenericTransducerParameters_Object = MibTableColumn
pGenericTransducerParameters = _PGenericTransducerParameters_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10190),
    _PGenericTransducerParameters_Type()
)
pGenericTransducerParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pGenericTransducerParameters.setStatus("current")
if mibBuilder.loadTexts:
    pGenericTransducerParameters.setUnits("mA/V")


class _PMaxBigCurrentWarning_Type(Unsigned32):
    """Custom type pMaxBigCurrentWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 400000000),
    )


_PMaxBigCurrentWarning_Type.__name__ = "Unsigned32"
_PMaxBigCurrentWarning_Object = MibTableColumn
pMaxBigCurrentWarning = _PMaxBigCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10193),
    _PMaxBigCurrentWarning_Type()
)
pMaxBigCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxBigCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxBigCurrentWarning.setUnits("A")


class _PMaxBigPowerWarning_Type(Uthousandth):
    """Custom type pMaxBigPowerWarning based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2000000000),
    )


_PMaxBigPowerWarning_Type.__name__ = "Uthousandth"
_PMaxBigPowerWarning_Object = MibTableColumn
pMaxBigPowerWarning = _PMaxBigPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10194),
    _PMaxBigPowerWarning_Type()
)
pMaxBigPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMaxBigPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMaxBigPowerWarning.setUnits("W")


class _PGroupNumber_Type(Unsigned32):
    """Custom type pGroupNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_PGroupNumber_Type.__name__ = "Unsigned32"
_PGroupNumber_Object = MibTableColumn
pGroupNumber = _PGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10195),
    _PGroupNumber_Type()
)
pGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pGroupNumber.setStatus("current")


class _PPhaseLink_Type(Unsigned32):
    """Custom type pPhaseLink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PPhaseLink_Type.__name__ = "Unsigned32"
_PPhaseLink_Object = MibTableColumn
pPhaseLink = _PPhaseLink_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10196),
    _PPhaseLink_Type()
)
pPhaseLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pPhaseLink.setStatus("current")


class _PCurrentSensorSelector_Type(Unsigned32):
    """Custom type pCurrentSensorSelector based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PCurrentSensorSelector_Type.__name__ = "Unsigned32"
_PCurrentSensorSelector_Object = MibTableColumn
pCurrentSensorSelector = _PCurrentSensorSelector_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10197),
    _PCurrentSensorSelector_Type()
)
pCurrentSensorSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCurrentSensorSelector.setStatus("current")


class _PMinBigCurrentWarning_Type(Unsigned32):
    """Custom type pMinBigCurrentWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400000000),
    )


_PMinBigCurrentWarning_Type.__name__ = "Unsigned32"
_PMinBigCurrentWarning_Object = MibTableColumn
pMinBigCurrentWarning = _PMinBigCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 10209),
    _PMinBigCurrentWarning_Type()
)
pMinBigCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMinBigCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    pMinBigCurrentWarning.setUnits("A")


class _PowerIndex_Type(Integer32):
    """Custom type powerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PowerIndex_Type.__name__ = "Integer32"
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 65537),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerIndex.setStatus("current")


class _PowerModuleIndex_Type(Integer32):
    """Custom type powerModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PowerModuleIndex_Type.__name__ = "Integer32"
_PowerModuleIndex_Object = MibTableColumn
powerModuleIndex = _PowerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 80, 1, 1, 65538),
    _PowerModuleIndex_Type()
)
powerModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerModuleIndex.setStatus("current")
_Measuring3phaseModule_ObjectIdentity = ObjectIdentity
measuring3phaseModule = _Measuring3phaseModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81)
)
_EMeasuring3PhaseTable_Object = MibTable
eMeasuring3PhaseTable = _EMeasuring3PhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1)
)
if mibBuilder.loadTexts:
    eMeasuring3PhaseTable.setStatus("current")
_EMeasuring3PhaseEntry_Object = MibTableRow
eMeasuring3PhaseEntry = _EMeasuring3PhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1)
)
eMeasuring3PhaseEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "measuring3phaseModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "measuring3phaseIndex"),
)
if mibBuilder.loadTexts:
    eMeasuring3PhaseEntry.setStatus("current")
_QGeneralModuleStatus_Type = Unsigned32
_QGeneralModuleStatus_Object = MibTableColumn
qGeneralModuleStatus = _QGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 1),
    _QGeneralModuleStatus_Type()
)
qGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qGeneralModuleStatus.setStatus("current")
_QSpecificModuleStatus_Type = Unsigned32
_QSpecificModuleStatus_Object = MibTableColumn
qSpecificModuleStatus = _QSpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 2),
    _QSpecificModuleStatus_Type()
)
qSpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qSpecificModuleStatus.setStatus("current")
_QCurrentTime_Type = TimeTicks
_QCurrentTime_Object = MibTableColumn
qCurrentTime = _QCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 3),
    _QCurrentTime_Type()
)
qCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    qCurrentTime.setUnits("UNIX")
_QVoltage_Type = Uhundredth
_QVoltage_Object = MibTableColumn
qVoltage = _QVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 4),
    _QVoltage_Type()
)
qVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qVoltage.setStatus("current")
if mibBuilder.loadTexts:
    qVoltage.setUnits("V")
_QFrequency_Type = Uthousandth
_QFrequency_Object = MibTableColumn
qFrequency = _QFrequency_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 5),
    _QFrequency_Type()
)
qFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qFrequency.setStatus("current")
if mibBuilder.loadTexts:
    qFrequency.setUnits("Hz")
_QActiveEnergy_Type = Uthousandth
_QActiveEnergy_Object = MibTableColumn
qActiveEnergy = _QActiveEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 9),
    _QActiveEnergy_Type()
)
qActiveEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qActiveEnergy.setStatus("current")
if mibBuilder.loadTexts:
    qActiveEnergy.setUnits("kWh")
_QApparentEnergy_Type = Uthousandth
_QApparentEnergy_Object = MibTableColumn
qApparentEnergy = _QApparentEnergy_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10),
    _QApparentEnergy_Type()
)
qApparentEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qApparentEnergy.setStatus("current")
if mibBuilder.loadTexts:
    qApparentEnergy.setUnits("kVAh")
_QTemperature_Type = Utenth
_QTemperature_Object = MibTableColumn
qTemperature = _QTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 11),
    _QTemperature_Type()
)
qTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qTemperature.setStatus("current")
if mibBuilder.loadTexts:
    qTemperature.setUnits("K")
_QPowerFactor_Type = Unsigned32
_QPowerFactor_Object = MibTableColumn
qPowerFactor = _QPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 16),
    _QPowerFactor_Type()
)
qPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    qPowerFactor.setUnits("%")
_QTimeOnline_Type = Unsigned32
_QTimeOnline_Object = MibTableColumn
qTimeOnline = _QTimeOnline_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 24),
    _QTimeOnline_Type()
)
qTimeOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qTimeOnline.setStatus("current")
if mibBuilder.loadTexts:
    qTimeOnline.setUnits("s")


class _QIOPort_Type(Unsigned32):
    """Custom type qIOPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QIOPort_Type.__name__ = "Unsigned32"
_QIOPort_Object = MibTableColumn
qIOPort = _QIOPort_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 30),
    _QIOPort_Type()
)
qIOPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qIOPort.setStatus("current")


class _QTotalHarmonicDistortion_Type(Utenth):
    """Custom type qTotalHarmonicDistortion based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_QTotalHarmonicDistortion_Type.__name__ = "Utenth"
_QTotalHarmonicDistortion_Object = MibTableColumn
qTotalHarmonicDistortion = _QTotalHarmonicDistortion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 50),
    _QTotalHarmonicDistortion_Type()
)
qTotalHarmonicDistortion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qTotalHarmonicDistortion.setStatus("current")
if mibBuilder.loadTexts:
    qTotalHarmonicDistortion.setUnits("%")


class _QPhase_Type(Unsigned32):
    """Custom type qPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QPhase_Type.__name__ = "Unsigned32"
_QPhase_Object = MibTableColumn
qPhase = _QPhase_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 51),
    _QPhase_Type()
)
qPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qPhase.setStatus("current")
if mibBuilder.loadTexts:
    qPhase.setUnits("degr")
_QBigCurrent_Type = Unsigned32
_QBigCurrent_Object = MibTableColumn
qBigCurrent = _QBigCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 52),
    _QBigCurrent_Type()
)
qBigCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qBigCurrent.setStatus("current")
if mibBuilder.loadTexts:
    qBigCurrent.setUnits("A")
_QBigPower_Type = Uthousandth
_QBigPower_Object = MibTableColumn
qBigPower = _QBigPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 53),
    _QBigPower_Type()
)
qBigPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qBigPower.setStatus("current")
if mibBuilder.loadTexts:
    qBigPower.setUnits("W")
_QBigApparentPower_Type = Uthousandth
_QBigApparentPower_Object = MibTableColumn
qBigApparentPower = _QBigApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 54),
    _QBigApparentPower_Type()
)
qBigApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qBigApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    qBigApparentPower.setUnits("VA")


class _QStatus_Type(Unsigned32):
    """Custom type qStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QStatus_Type.__name__ = "Unsigned32"
_QStatus_Object = MibTableColumn
qStatus = _QStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 1000),
    _QStatus_Type()
)
qStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qStatus.setStatus("current")
_QModuleName_Type = DisplayString
_QModuleName_Object = MibTableColumn
qModuleName = _QModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10001),
    _QModuleName_Type()
)
qModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qModuleName.setStatus("current")
_QFirmwareVersion_Type = Version
_QFirmwareVersion_Object = MibTableColumn
qFirmwareVersion = _QFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10002),
    _QFirmwareVersion_Type()
)
qFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qFirmwareVersion.setStatus("current")
_QHardwareVersion_Type = Version
_QHardwareVersion_Object = MibTableColumn
qHardwareVersion = _QHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10003),
    _QHardwareVersion_Type()
)
qHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qHardwareVersion.setStatus("current")
_QFirmwareID_Type = DisplayString
_QFirmwareID_Object = MibTableColumn
qFirmwareID = _QFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10004),
    _QFirmwareID_Type()
)
qFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qFirmwareID.setStatus("current")
_QHardwareID_Type = DisplayString
_QHardwareID_Object = MibTableColumn
qHardwareID = _QHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10005),
    _QHardwareID_Type()
)
qHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qHardwareID.setStatus("current")


class _QPortState_Type(Unsigned32):
    """Custom type qPortState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QPortState_Type.__name__ = "Unsigned32"
_QPortState_Object = MibTableColumn
qPortState = _QPortState_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10035),
    _QPortState_Type()
)
qPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortState.setStatus("current")


class _QMaxVoltageWarning_Type(Uhundredth):
    """Custom type qMaxVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 30000),
    )


_QMaxVoltageWarning_Type.__name__ = "Uhundredth"
_QMaxVoltageWarning_Object = MibTableColumn
qMaxVoltageWarning = _QMaxVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10047),
    _QMaxVoltageWarning_Type()
)
qMaxVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMaxVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    qMaxVoltageWarning.setUnits("V")


class _QMinVoltageWarning_Type(Uhundredth):
    """Custom type qMinVoltageWarning based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 30000),
    )


_QMinVoltageWarning_Type.__name__ = "Uhundredth"
_QMinVoltageWarning_Object = MibTableColumn
qMinVoltageWarning = _QMinVoltageWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10049),
    _QMinVoltageWarning_Type()
)
qMinVoltageWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMinVoltageWarning.setStatus("current")
if mibBuilder.loadTexts:
    qMinVoltageWarning.setUnits("V")


class _QMinTemperatureWarning_Type(Utenth):
    """Custom type qMinTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_QMinTemperatureWarning_Type.__name__ = "Utenth"
_QMinTemperatureWarning_Object = MibTableColumn
qMinTemperatureWarning = _QMinTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10052),
    _QMinTemperatureWarning_Type()
)
qMinTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMinTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    qMinTemperatureWarning.setUnits("K")


class _QMaxTemperatureWarning_Type(Utenth):
    """Custom type qMaxTemperatureWarning based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_QMaxTemperatureWarning_Type.__name__ = "Utenth"
_QMaxTemperatureWarning_Object = MibTableColumn
qMaxTemperatureWarning = _QMaxTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10053),
    _QMaxTemperatureWarning_Type()
)
qMaxTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMaxTemperatureWarning.setStatus("current")
if mibBuilder.loadTexts:
    qMaxTemperatureWarning.setUnits("K")
_QPortStateEvent_Type = EVENTFLAGS
_QPortStateEvent_Object = MibTableColumn
qPortStateEvent = _QPortStateEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10076),
    _QPortStateEvent_Type()
)
qPortStateEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortStateEvent.setStatus("current")
_QCurrentWarningEvent_Type = EVENTFLAGS
_QCurrentWarningEvent_Object = MibTableColumn
qCurrentWarningEvent = _QCurrentWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10078),
    _QCurrentWarningEvent_Type()
)
qCurrentWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qCurrentWarningEvent.setStatus("current")
_QPowerWarningEvent_Type = EVENTFLAGS
_QPowerWarningEvent_Object = MibTableColumn
qPowerWarningEvent = _QPowerWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10080),
    _QPowerWarningEvent_Type()
)
qPowerWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPowerWarningEvent.setStatus("current")
_QVoltageWarningEvent_Type = EVENTFLAGS
_QVoltageWarningEvent_Object = MibTableColumn
qVoltageWarningEvent = _QVoltageWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10086),
    _QVoltageWarningEvent_Type()
)
qVoltageWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qVoltageWarningEvent.setStatus("current")
_QTemperatureWarningEvent_Type = EVENTFLAGS
_QTemperatureWarningEvent_Object = MibTableColumn
qTemperatureWarningEvent = _QTemperatureWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10087),
    _QTemperatureWarningEvent_Type()
)
qTemperatureWarningEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qTemperatureWarningEvent.setStatus("current")


class _QMicroIntTimeThreshold_Type(Utenth):
    """Custom type qMicroIntTimeThreshold based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_QMicroIntTimeThreshold_Type.__name__ = "Utenth"
_QMicroIntTimeThreshold_Object = MibTableColumn
qMicroIntTimeThreshold = _QMicroIntTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10135),
    _QMicroIntTimeThreshold_Type()
)
qMicroIntTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMicroIntTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    qMicroIntTimeThreshold.setUnits("ms")
_QMicroIntEvent_Type = EVENTFLAGS
_QMicroIntEvent_Object = MibTableColumn
qMicroIntEvent = _QMicroIntEvent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10136),
    _QMicroIntEvent_Type()
)
qMicroIntEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMicroIntEvent.setStatus("current")
_QDeviceID_Type = DisplayString
_QDeviceID_Object = MibTableColumn
qDeviceID = _QDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10150),
    _QDeviceID_Type()
)
qDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qDeviceID.setStatus("current")
_QDeviceVersion_Type = Version
_QDeviceVersion_Object = MibTableColumn
qDeviceVersion = _QDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10151),
    _QDeviceVersion_Type()
)
qDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qDeviceVersion.setStatus("current")


class _QMaxBigCurrentWarning_Type(Unsigned32):
    """Custom type qMaxBigCurrentWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 400000000),
    )


_QMaxBigCurrentWarning_Type.__name__ = "Unsigned32"
_QMaxBigCurrentWarning_Object = MibTableColumn
qMaxBigCurrentWarning = _QMaxBigCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10193),
    _QMaxBigCurrentWarning_Type()
)
qMaxBigCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMaxBigCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    qMaxBigCurrentWarning.setUnits("A")


class _QMaxBigPowerWarning_Type(Uthousandth):
    """Custom type qMaxBigPowerWarning based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2000000000),
    )


_QMaxBigPowerWarning_Type.__name__ = "Uthousandth"
_QMaxBigPowerWarning_Object = MibTableColumn
qMaxBigPowerWarning = _QMaxBigPowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10194),
    _QMaxBigPowerWarning_Type()
)
qMaxBigPowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMaxBigPowerWarning.setStatus("current")
if mibBuilder.loadTexts:
    qMaxBigPowerWarning.setUnits("W")


class _QCurrentSensorSelector_Type(Unsigned32):
    """Custom type qCurrentSensorSelector based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QCurrentSensorSelector_Type.__name__ = "Unsigned32"
_QCurrentSensorSelector_Object = MibTableColumn
qCurrentSensorSelector = _QCurrentSensorSelector_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10197),
    _QCurrentSensorSelector_Type()
)
qCurrentSensorSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qCurrentSensorSelector.setStatus("current")


class _QMinBigCurrentWarning_Type(Unsigned32):
    """Custom type qMinBigCurrentWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400000000),
    )


_QMinBigCurrentWarning_Type.__name__ = "Unsigned32"
_QMinBigCurrentWarning_Object = MibTableColumn
qMinBigCurrentWarning = _QMinBigCurrentWarning_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10209),
    _QMinBigCurrentWarning_Type()
)
qMinBigCurrentWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qMinBigCurrentWarning.setStatus("current")
if mibBuilder.loadTexts:
    qMinBigCurrentWarning.setUnits("A")


class _QkWhMode_Type(Unsigned32):
    """Custom type qkWhMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_QkWhMode_Type.__name__ = "Unsigned32"
_QkWhMode_Object = MibTableColumn
qkWhMode = _QkWhMode_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 10234),
    _QkWhMode_Type()
)
qkWhMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qkWhMode.setStatus("current")


class _Measuring3phaseIndex_Type(Integer32):
    """Custom type measuring3phaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Measuring3phaseIndex_Type.__name__ = "Integer32"
_Measuring3phaseIndex_Object = MibTableColumn
measuring3phaseIndex = _Measuring3phaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 65537),
    _Measuring3phaseIndex_Type()
)
measuring3phaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measuring3phaseIndex.setStatus("current")


class _Measuring3phaseModuleIndex_Type(Integer32):
    """Custom type measuring3phaseModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Measuring3phaseModuleIndex_Type.__name__ = "Integer32"
_Measuring3phaseModuleIndex_Object = MibTableColumn
measuring3phaseModuleIndex = _Measuring3phaseModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 81, 1, 1, 65538),
    _Measuring3phaseModuleIndex_Type()
)
measuring3phaseModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measuring3phaseModuleIndex.setStatus("current")
_PcModule_ObjectIdentity = ObjectIdentity
pcModule = _PcModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85)
)
_EPCTable_Object = MibTable
ePCTable = _EPCTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1)
)
if mibBuilder.loadTexts:
    ePCTable.setStatus("current")
_EPCEntry_Object = MibTableRow
ePCEntry = _EPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1)
)
ePCEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "pcModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "pcIndex"),
)
if mibBuilder.loadTexts:
    ePCEntry.setStatus("current")
_UGeneralModuleStatus_Type = Unsigned32
_UGeneralModuleStatus_Object = MibTableColumn
uGeneralModuleStatus = _UGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 1),
    _UGeneralModuleStatus_Type()
)
uGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uGeneralModuleStatus.setStatus("current")
_USpecificModuleStatus_Type = Unsigned32
_USpecificModuleStatus_Object = MibTableColumn
uSpecificModuleStatus = _USpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 2),
    _USpecificModuleStatus_Type()
)
uSpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSpecificModuleStatus.setStatus("current")
_UCurrentTime_Type = TimeTicks
_UCurrentTime_Object = MibTableColumn
uCurrentTime = _UCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 3),
    _UCurrentTime_Type()
)
uCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    uCurrentTime.setUnits("UNIX")


class _UVoltage_Type(Uhundredth):
    """Custom type uVoltage based on Uhundredth"""
    subtypeSpec = Uhundredth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UVoltage_Type.__name__ = "Uhundredth"
_UVoltage_Object = MibTableColumn
uVoltage = _UVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 4),
    _UVoltage_Type()
)
uVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uVoltage.setStatus("current")
if mibBuilder.loadTexts:
    uVoltage.setUnits("V")


class _UCurrent_Type(Uthousandth):
    """Custom type uCurrent based on Uthousandth"""
    subtypeSpec = Uthousandth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UCurrent_Type.__name__ = "Uthousandth"
_UCurrent_Object = MibTableColumn
uCurrent = _UCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 6),
    _UCurrent_Type()
)
uCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uCurrent.setStatus("current")
if mibBuilder.loadTexts:
    uCurrent.setUnits("A")
_UStatePortCur_Type = CURPORTSTATE
_UStatePortCur_Object = MibTableColumn
uStatePortCur = _UStatePortCur_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 8),
    _UStatePortCur_Type()
)
uStatePortCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uStatePortCur.setStatus("current")


class _UTemperature_Type(Utenth):
    """Custom type uTemperature based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2232, 4732),
    )


_UTemperature_Type.__name__ = "Utenth"
_UTemperature_Object = MibTableColumn
uTemperature = _UTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 11),
    _UTemperature_Type()
)
uTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uTemperature.setStatus("current")
if mibBuilder.loadTexts:
    uTemperature.setUnits("K")


class _UHumidity_Type(Utenth):
    """Custom type uHumidity based on Utenth"""
    subtypeSpec = Utenth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_UHumidity_Type.__name__ = "Utenth"
_UHumidity_Object = MibTableColumn
uHumidity = _UHumidity_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 12),
    _UHumidity_Type()
)
uHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uHumidity.setStatus("current")
if mibBuilder.loadTexts:
    uHumidity.setUnits("RH")
_UModuleName_Type = DisplayString
_UModuleName_Object = MibTableColumn
uModuleName = _UModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 10001),
    _UModuleName_Type()
)
uModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uModuleName.setStatus("current")
_UFirmwareVersion_Type = Version
_UFirmwareVersion_Object = MibTableColumn
uFirmwareVersion = _UFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 10002),
    _UFirmwareVersion_Type()
)
uFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uFirmwareVersion.setStatus("current")
_UHardwareVersion_Type = Version
_UHardwareVersion_Object = MibTableColumn
uHardwareVersion = _UHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 10003),
    _UHardwareVersion_Type()
)
uHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uHardwareVersion.setStatus("current")
_UFirmwareID_Type = DisplayString
_UFirmwareID_Object = MibTableColumn
uFirmwareID = _UFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 10004),
    _UFirmwareID_Type()
)
uFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uFirmwareID.setStatus("current")
_UHardwareID_Type = DisplayString
_UHardwareID_Object = MibTableColumn
uHardwareID = _UHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 10005),
    _UHardwareID_Type()
)
uHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uHardwareID.setStatus("current")


class _UPortState_Type(Unsigned32):
    """Custom type uPortState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UPortState_Type.__name__ = "Unsigned32"
_UPortState_Object = MibTableColumn
uPortState = _UPortState_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 10035),
    _UPortState_Type()
)
uPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uPortState.setStatus("current")


class _PcIndex_Type(Integer32):
    """Custom type pcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PcIndex_Type.__name__ = "Integer32"
_PcIndex_Object = MibTableColumn
pcIndex = _PcIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 65537),
    _PcIndex_Type()
)
pcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcIndex.setStatus("current")


class _PcModuleIndex_Type(Integer32):
    """Custom type pcModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PcModuleIndex_Type.__name__ = "Integer32"
_PcModuleIndex_Object = MibTableColumn
pcModuleIndex = _PcModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 85, 1, 1, 65538),
    _PcModuleIndex_Type()
)
pcModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcModuleIndex.setStatus("current")
_TestmoduleModule_ObjectIdentity = ObjectIdentity
testmoduleModule = _TestmoduleModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89)
)
_ETestModuleTable_Object = MibTable
eTestModuleTable = _ETestModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1)
)
if mibBuilder.loadTexts:
    eTestModuleTable.setStatus("current")
_ETestModuleEntry_Object = MibTableRow
eTestModuleEntry = _ETestModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1)
)
eTestModuleEntry.setIndexNames(
    (0, "ES-RACKTIVITY-MIB", "testmoduleModuleIndex"),
    (0, "ES-RACKTIVITY-MIB", "testmoduleIndex"),
)
if mibBuilder.loadTexts:
    eTestModuleEntry.setStatus("current")
_YGeneralModuleStatus_Type = Unsigned32
_YGeneralModuleStatus_Object = MibTableColumn
yGeneralModuleStatus = _YGeneralModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 1),
    _YGeneralModuleStatus_Type()
)
yGeneralModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yGeneralModuleStatus.setStatus("current")
_YSpecificModuleStatus_Type = Unsigned32
_YSpecificModuleStatus_Object = MibTableColumn
ySpecificModuleStatus = _YSpecificModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 2),
    _YSpecificModuleStatus_Type()
)
ySpecificModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ySpecificModuleStatus.setStatus("current")
_YCurrentTime_Type = TimeTicks
_YCurrentTime_Object = MibTableColumn
yCurrentTime = _YCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 3),
    _YCurrentTime_Type()
)
yCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    yCurrentTime.setStatus("current")
if mibBuilder.loadTexts:
    yCurrentTime.setUnits("UNIX")
_YCurrent_Type = Uthousandth
_YCurrent_Object = MibTableColumn
yCurrent = _YCurrent_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 6),
    _YCurrent_Type()
)
yCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yCurrent.setStatus("current")
if mibBuilder.loadTexts:
    yCurrent.setUnits("A")
_YStatePortCur_Type = CURPORTSTATE
_YStatePortCur_Object = MibTableColumn
yStatePortCur = _YStatePortCur_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 8),
    _YStatePortCur_Type()
)
yStatePortCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yStatePortCur.setStatus("current")
_YAnalogueInput_Type = Unsigned32
_YAnalogueInput_Object = MibTableColumn
yAnalogueInput = _YAnalogueInput_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 27),
    _YAnalogueInput_Type()
)
yAnalogueInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yAnalogueInput.setStatus("current")
if mibBuilder.loadTexts:
    yAnalogueInput.setUnits("mV")
_YModuleName_Type = DisplayString
_YModuleName_Object = MibTableColumn
yModuleName = _YModuleName_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 10001),
    _YModuleName_Type()
)
yModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    yModuleName.setStatus("current")
_YFirmwareVersion_Type = Version
_YFirmwareVersion_Object = MibTableColumn
yFirmwareVersion = _YFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 10002),
    _YFirmwareVersion_Type()
)
yFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yFirmwareVersion.setStatus("current")
_YHardwareVersion_Type = Version
_YHardwareVersion_Object = MibTableColumn
yHardwareVersion = _YHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 10003),
    _YHardwareVersion_Type()
)
yHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yHardwareVersion.setStatus("current")
_YFirmwareID_Type = DisplayString
_YFirmwareID_Object = MibTableColumn
yFirmwareID = _YFirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 10004),
    _YFirmwareID_Type()
)
yFirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yFirmwareID.setStatus("current")
_YHardwareID_Type = DisplayString
_YHardwareID_Object = MibTableColumn
yHardwareID = _YHardwareID_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 10005),
    _YHardwareID_Type()
)
yHardwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    yHardwareID.setStatus("current")


class _TestmoduleIndex_Type(Integer32):
    """Custom type testmoduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TestmoduleIndex_Type.__name__ = "Integer32"
_TestmoduleIndex_Object = MibTableColumn
testmoduleIndex = _TestmoduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 65537),
    _TestmoduleIndex_Type()
)
testmoduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    testmoduleIndex.setStatus("current")


class _TestmoduleModuleIndex_Type(Integer32):
    """Custom type testmoduleModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TestmoduleModuleIndex_Type.__name__ = "Integer32"
_TestmoduleModuleIndex_Object = MibTableColumn
testmoduleModuleIndex = _TestmoduleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 34097, 9, 89, 1, 1, 65538),
    _TestmoduleModuleIndex_Type()
)
testmoduleModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    testmoduleModuleIndex.setStatus("current")

# Managed Objects groups

esRacktivityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34097, 9, 2, 1, 1)
)
esRacktivityMIBGroup.setObjects(
      *(("ES-RACKTIVITY-MIB", "mGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "mSpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "mCurrentTime"),
        ("ES-RACKTIVITY-MIB", "mVoltage"),
        ("ES-RACKTIVITY-MIB", "mTemperature"),
        ("ES-RACKTIVITY-MIB", "mCurrentIP"),
        ("ES-RACKTIVITY-MIB", "mTotalCurrent"),
        ("ES-RACKTIVITY-MIB", "mTotalRealPower"),
        ("ES-RACKTIVITY-MIB", "mTotalActiveEnergy"),
        ("ES-RACKTIVITY-MIB", "mLineCurrent"),
        ("ES-RACKTIVITY-MIB", "mFuseCurrent"),
        ("ES-RACKTIVITY-MIB", "mCurrentSubNetMask"),
        ("ES-RACKTIVITY-MIB", "mCurrentDNSServer"),
        ("ES-RACKTIVITY-MIB", "mCurrentStdGateway"),
        ("ES-RACKTIVITY-MIB", "mUPSPresent"),
        ("ES-RACKTIVITY-MIB", "mUPSStatus"),
        ("ES-RACKTIVITY-MIB", "mUPSEstimatedRunTime"),
        ("ES-RACKTIVITY-MIB", "mUPSBatteryLevel"),
        ("ES-RACKTIVITY-MIB", "mHighCurrent"),
        ("ES-RACKTIVITY-MIB", "mUpsCommunicationStatus"),
        ("ES-RACKTIVITY-MIB", "mHighPower"),
        ("ES-RACKTIVITY-MIB", "mTotalHighCurrent"),
        ("ES-RACKTIVITY-MIB", "mTotalHighPower"),
        ("ES-RACKTIVITY-MIB", "mPositiveEnergy"),
        ("ES-RACKTIVITY-MIB", "mNegativeEnergy"),
        ("ES-RACKTIVITY-MIB", "mTotalPositiveEnergy"),
        ("ES-RACKTIVITY-MIB", "mTotalNegativeEnergy"),
        ("ES-RACKTIVITY-MIB", "mCloudStatus"),
        ("ES-RACKTIVITY-MIB", "mStatus"),
        ("ES-RACKTIVITY-MIB", "mModuleName"),
        ("ES-RACKTIVITY-MIB", "mFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "mHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "mFirmwareID"),
        ("ES-RACKTIVITY-MIB", "mHardwareID"),
        ("ES-RACKTIVITY-MIB", "mRackName"),
        ("ES-RACKTIVITY-MIB", "mRackPosition"),
        ("ES-RACKTIVITY-MIB", "mIPAddress"),
        ("ES-RACKTIVITY-MIB", "mSubNetMask"),
        ("ES-RACKTIVITY-MIB", "mStdGateWay"),
        ("ES-RACKTIVITY-MIB", "mDnsServer"),
        ("ES-RACKTIVITY-MIB", "mMAC"),
        ("ES-RACKTIVITY-MIB", "mDHCPEnable"),
        ("ES-RACKTIVITY-MIB", "mNTPServer"),
        ("ES-RACKTIVITY-MIB", "mUseDefaultNTPServer"),
        ("ES-RACKTIVITY-MIB", "mUseNTP"),
        ("ES-RACKTIVITY-MIB", "mSNMPTrapRecvIP"),
        ("ES-RACKTIVITY-MIB", "mSNMPTrapRecvPort"),
        ("ES-RACKTIVITY-MIB", "mSNMPControl"),
        ("ES-RACKTIVITY-MIB", "mECSServer"),
        ("ES-RACKTIVITY-MIB", "mUseECSServer"),
        ("ES-RACKTIVITY-MIB", "mDisplayLock"),
        ("ES-RACKTIVITY-MIB", "mDisplayTimeOn"),
        ("ES-RACKTIVITY-MIB", "mMaxVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "mMinVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "mMinTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "mMaxTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "mGeneralEventEnable"),
        ("ES-RACKTIVITY-MIB", "mSNMPSysContact"),
        ("ES-RACKTIVITY-MIB", "mCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mPowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mTotalCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mTotalPowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mVoltageWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mTemperatureWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mDisplayBrightness"),
        ("ES-RACKTIVITY-MIB", "mECSServerPort"),
        ("ES-RACKTIVITY-MIB", "mExternalSensorLabel"),
        ("ES-RACKTIVITY-MIB", "mHttpsOnly"),
        ("ES-RACKTIVITY-MIB", "mTelnetSsl"),
        ("ES-RACKTIVITY-MIB", "mCookieTimeToLive"),
        ("ES-RACKTIVITY-MIB", "mLineCurrentWarningThreshold"),
        ("ES-RACKTIVITY-MIB", "mLineCurrentOffThreshold"),
        ("ES-RACKTIVITY-MIB", "mLineCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mLineCurrentOffEvent"),
        ("ES-RACKTIVITY-MIB", "mFuseCurrentWarningThreshold"),
        ("ES-RACKTIVITY-MIB", "mFuseCurrentOffThreshold"),
        ("ES-RACKTIVITY-MIB", "mFuseCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "mFuseCurrentOffEvent"),
        ("ES-RACKTIVITY-MIB", "mDeviceID"),
        ("ES-RACKTIVITY-MIB", "mDeviceVersion"),
        ("ES-RACKTIVITY-MIB", "mSysName"),
        ("ES-RACKTIVITY-MIB", "mElectricalTopology"),
        ("ES-RACKTIVITY-MIB", "mFusePortTopology"),
        ("ES-RACKTIVITY-MIB", "mLineFuseTopology"),
        ("ES-RACKTIVITY-MIB", "mSSOIPAddress"),
        ("ES-RACKTIVITY-MIB", "mSSOLoginCredentials"),
        ("ES-RACKTIVITY-MIB", "mSSOGracefullShutdown"),
        ("ES-RACKTIVITY-MIB", "mUPSWarningLevel"),
        ("ES-RACKTIVITY-MIB", "mUPSOffLevel"),
        ("ES-RACKTIVITY-MIB", "mMaxHighCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "mUpsMonitoringProtocol"),
        ("ES-RACKTIVITY-MIB", "mUpsEmergencyThreshold"),
        ("ES-RACKTIVITY-MIB", "mUpsRecoveryThreshold"),
        ("ES-RACKTIVITY-MIB", "mUpsEventFlags"),
        ("ES-RACKTIVITY-MIB", "mRecoveryPowerThreshold"),
        ("ES-RACKTIVITY-MIB", "mMinHighCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "mMinHighPowerWarning"),
        ("ES-RACKTIVITY-MIB", "mMaxHighPowerWarning"),
        ("ES-RACKTIVITY-MIB", "mHeartbeatInterval"),
        ("ES-RACKTIVITY-MIB", "mMinTotalHighCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "mMaxTotalHighCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "mMinTotalHighPowerWarning"),
        ("ES-RACKTIVITY-MIB", "mMaxTotalHighPowerWarning"),
        ("ES-RACKTIVITY-MIB", "mCloudState"),
        ("ES-RACKTIVITY-MIB", "mSensorBias"),
        ("ES-RACKTIVITY-MIB", "mDaisyChainDeviceMode"),
        ("ES-RACKTIVITY-MIB", "mSNMPTrapUser"),
        ("ES-RACKTIVITY-MIB", "mUSMUser"),
        ("ES-RACKTIVITY-MIB", "mUSMAuthPassphrase"),
        ("ES-RACKTIVITY-MIB", "mUSMPrivPassphrase"),
        ("ES-RACKTIVITY-MIB", "mSNMPV2GetSetEnable"),
        ("ES-RACKTIVITY-MIB", "mSNMPV3GetSetEnable"),
        ("ES-RACKTIVITY-MIB", "mUSMAuthPassphraseLength"),
        ("ES-RACKTIVITY-MIB", "mUSMPrivPassphraseLength"),
        ("ES-RACKTIVITY-MIB", "mSNMPTrapEnable"),
        ("ES-RACKTIVITY-MIB", "mLDAPAttribute"),
        ("ES-RACKTIVITY-MIB", "mLDAPPath"),
        ("ES-RACKTIVITY-MIB", "mLDAPAdminGroupName"),
        ("ES-RACKTIVITY-MIB", "mLDAPRestrictedGroupName"),
        ("ES-RACKTIVITY-MIB", "mLDAPGuestGroupName"),
        ("ES-RACKTIVITY-MIB", "mLDAPEnable"),
        ("ES-RACKTIVITY-MIB", "mLDAPLoginWrapper"),
        ("ES-RACKTIVITY-MIB", "mLDAPServer"),
        ("ES-RACKTIVITY-MIB", "mLocalAuthEnable"),
        ("ES-RACKTIVITY-MIB", "pGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "pSpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "pCurrentTime"),
        ("ES-RACKTIVITY-MIB", "pVoltage"),
        ("ES-RACKTIVITY-MIB", "pFrequency"),
        ("ES-RACKTIVITY-MIB", "pCurrent"),
        ("ES-RACKTIVITY-MIB", "pPower"),
        ("ES-RACKTIVITY-MIB", "pStatePortCur"),
        ("ES-RACKTIVITY-MIB", "pActiveEnergy"),
        ("ES-RACKTIVITY-MIB", "pApparentEnergy"),
        ("ES-RACKTIVITY-MIB", "pTemperature"),
        ("ES-RACKTIVITY-MIB", "pApparentPower"),
        ("ES-RACKTIVITY-MIB", "pPowerFactor"),
        ("ES-RACKTIVITY-MIB", "pTotalCurrent"),
        ("ES-RACKTIVITY-MIB", "pTotalRealPower"),
        ("ES-RACKTIVITY-MIB", "pTotalApparentPower"),
        ("ES-RACKTIVITY-MIB", "pTotalActiveEnergy"),
        ("ES-RACKTIVITY-MIB", "pTotalApparentEnergy"),
        ("ES-RACKTIVITY-MIB", "pTotalPowerFactor"),
        ("ES-RACKTIVITY-MIB", "pTimeOnline"),
        ("ES-RACKTIVITY-MIB", "pTotalHarmonicDistortion"),
        ("ES-RACKTIVITY-MIB", "pPhase"),
        ("ES-RACKTIVITY-MIB", "pBigCurrent"),
        ("ES-RACKTIVITY-MIB", "pBigPower"),
        ("ES-RACKTIVITY-MIB", "pBigApparentPower"),
        ("ES-RACKTIVITY-MIB", "pDetectedPhase"),
        ("ES-RACKTIVITY-MIB", "pModuleName"),
        ("ES-RACKTIVITY-MIB", "pFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "pHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "pFirmwareID"),
        ("ES-RACKTIVITY-MIB", "pHardwareID"),
        ("ES-RACKTIVITY-MIB", "pPortName"),
        ("ES-RACKTIVITY-MIB", "pPortState"),
        ("ES-RACKTIVITY-MIB", "pCurrentPriorOff"),
        ("ES-RACKTIVITY-MIB", "pDelayOn"),
        ("ES-RACKTIVITY-MIB", "pMaxCurrentOff"),
        ("ES-RACKTIVITY-MIB", "pMaxCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "pMaxPowerOff"),
        ("ES-RACKTIVITY-MIB", "pMaxPowerWarning"),
        ("ES-RACKTIVITY-MIB", "pMaxTotalCurrentOff"),
        ("ES-RACKTIVITY-MIB", "pMaxTotalCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "pMaxTotalPowerOff"),
        ("ES-RACKTIVITY-MIB", "pMaxTotalPowerWarning"),
        ("ES-RACKTIVITY-MIB", "pMaxVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "pMinVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "pMinTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "pMaxTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "pPortStateEvent"),
        ("ES-RACKTIVITY-MIB", "pCurrentOffEvent"),
        ("ES-RACKTIVITY-MIB", "pCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "pPowerOffEvent"),
        ("ES-RACKTIVITY-MIB", "pPowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "pTotalCurrentOffEvent"),
        ("ES-RACKTIVITY-MIB", "pTotalCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "pTotalPowerOffEvent"),
        ("ES-RACKTIVITY-MIB", "pTotalPowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "pVoltageWarningEvent"),
        ("ES-RACKTIVITY-MIB", "pTemperatureWarningEvent"),
        ("ES-RACKTIVITY-MIB", "pMaxOverheatingOff"),
        ("ES-RACKTIVITY-MIB", "pOverheatingOffEvent"),
        ("ES-RACKTIVITY-MIB", "pPowerCycleTime"),
        ("ES-RACKTIVITY-MIB", "pExternalSensorLabel"),
        ("ES-RACKTIVITY-MIB", "pMaxOverheatingWarning"),
        ("ES-RACKTIVITY-MIB", "pOverheatingWarningEvent"),
        ("ES-RACKTIVITY-MIB", "pMicroIntTimeThreshold"),
        ("ES-RACKTIVITY-MIB", "pMicroIntEvent"),
        ("ES-RACKTIVITY-MIB", "pSoftFuseCurrentThreshold"),
        ("ES-RACKTIVITY-MIB", "pSoftFuseDelay"),
        ("ES-RACKTIVITY-MIB", "pSoftFuseEvent"),
        ("ES-RACKTIVITY-MIB", "pPhaseShiftEvent"),
        ("ES-RACKTIVITY-MIB", "pSchedulePortOnTime"),
        ("ES-RACKTIVITY-MIB", "pSchedulePortOffTime"),
        ("ES-RACKTIVITY-MIB", "pEnableSchedulePort"),
        ("ES-RACKTIVITY-MIB", "pBlockSetPortOff"),
        ("ES-RACKTIVITY-MIB", "pSchedulePortChangeEvent"),
        ("ES-RACKTIVITY-MIB", "pAgentIP"),
        ("ES-RACKTIVITY-MIB", "pAgentPort"),
        ("ES-RACKTIVITY-MIB", "pAgentCommunicationEventFlags"),
        ("ES-RACKTIVITY-MIB", "pAlwaysOn"),
        ("ES-RACKTIVITY-MIB", "pGenericTransducerParameters"),
        ("ES-RACKTIVITY-MIB", "pMaxBigCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "pMaxBigPowerWarning"),
        ("ES-RACKTIVITY-MIB", "pGroupNumber"),
        ("ES-RACKTIVITY-MIB", "pPhaseLink"),
        ("ES-RACKTIVITY-MIB", "pCurrentSensorSelector"),
        ("ES-RACKTIVITY-MIB", "pMinBigCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "aGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "aSpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "aCurrentTime"),
        ("ES-RACKTIVITY-MIB", "aVoltage"),
        ("ES-RACKTIVITY-MIB", "aStatePortCur"),
        ("ES-RACKTIVITY-MIB", "aTemperature"),
        ("ES-RACKTIVITY-MIB", "aHumidity"),
        ("ES-RACKTIVITY-MIB", "aAirflow"),
        ("ES-RACKTIVITY-MIB", "aDewPoint"),
        ("ES-RACKTIVITY-MIB", "aPressure"),
        ("ES-RACKTIVITY-MIB", "aAnalogueInput"),
        ("ES-RACKTIVITY-MIB", "aWaterleak"),
        ("ES-RACKTIVITY-MIB", "aMotionDetected"),
        ("ES-RACKTIVITY-MIB", "aIOPort"),
        ("ES-RACKTIVITY-MIB", "aHighCurrent"),
        ("ES-RACKTIVITY-MIB", "aHighPower"),
        ("ES-RACKTIVITY-MIB", "aModuleName"),
        ("ES-RACKTIVITY-MIB", "aFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "aHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "aFirmwareID"),
        ("ES-RACKTIVITY-MIB", "aHardwareID"),
        ("ES-RACKTIVITY-MIB", "aDisplayTimeOn"),
        ("ES-RACKTIVITY-MIB", "aMaxVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "aMinVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "aMinTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "aMaxTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "aMinHumidityWarning"),
        ("ES-RACKTIVITY-MIB", "aMaxHumidityWarning"),
        ("ES-RACKTIVITY-MIB", "aCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aPowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aVoltageWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aTemperatureWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aHumidityWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aDewPointWarning"),
        ("ES-RACKTIVITY-MIB", "aDewPointWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aDewPointViolationEvent"),
        ("ES-RACKTIVITY-MIB", "aPressureWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aMinPressureWarning"),
        ("ES-RACKTIVITY-MIB", "aMaxPressureWarning"),
        ("ES-RACKTIVITY-MIB", "aDisplayBrightness"),
        ("ES-RACKTIVITY-MIB", "aMotionSensitivity"),
        ("ES-RACKTIVITY-MIB", "aExternalSensorLabel"),
        ("ES-RACKTIVITY-MIB", "aRelayLabel"),
        ("ES-RACKTIVITY-MIB", "aMinAnalogueInputWarning"),
        ("ES-RACKTIVITY-MIB", "aMaxAnalogueInputWarning"),
        ("ES-RACKTIVITY-MIB", "aWaterleakWarning"),
        ("ES-RACKTIVITY-MIB", "aMinAirflowWarning"),
        ("ES-RACKTIVITY-MIB", "aMaxAirflowWarning"),
        ("ES-RACKTIVITY-MIB", "aAnalogueInputWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aWaterleakWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aAirflowWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aRelayAssertActionEvent"),
        ("ES-RACKTIVITY-MIB", "aRelayDeassertActionEvent"),
        ("ES-RACKTIVITY-MIB", "aMotionWarning"),
        ("ES-RACKTIVITY-MIB", "aMotionWarningEvent"),
        ("ES-RACKTIVITY-MIB", "aDeviceID"),
        ("ES-RACKTIVITY-MIB", "aDeviceVersion"),
        ("ES-RACKTIVITY-MIB", "aSysName"),
        ("ES-RACKTIVITY-MIB", "aMaxHighCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "aMinHighCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "aMinHighPowerWarning"),
        ("ES-RACKTIVITY-MIB", "aMaxHighPowerWarning"),
        ("ES-RACKTIVITY-MIB", "aIOPortWarningEvent"),
        ("ES-RACKTIVITY-MIB", "yGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "ySpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "yCurrentTime"),
        ("ES-RACKTIVITY-MIB", "yCurrent"),
        ("ES-RACKTIVITY-MIB", "yStatePortCur"),
        ("ES-RACKTIVITY-MIB", "yAnalogueInput"),
        ("ES-RACKTIVITY-MIB", "yModuleName"),
        ("ES-RACKTIVITY-MIB", "yFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "yHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "yFirmwareID"),
        ("ES-RACKTIVITY-MIB", "yHardwareID"),
        ("ES-RACKTIVITY-MIB", "uGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "uSpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "uCurrentTime"),
        ("ES-RACKTIVITY-MIB", "uVoltage"),
        ("ES-RACKTIVITY-MIB", "uCurrent"),
        ("ES-RACKTIVITY-MIB", "uStatePortCur"),
        ("ES-RACKTIVITY-MIB", "uTemperature"),
        ("ES-RACKTIVITY-MIB", "uHumidity"),
        ("ES-RACKTIVITY-MIB", "uModuleName"),
        ("ES-RACKTIVITY-MIB", "uFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "uHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "uFirmwareID"),
        ("ES-RACKTIVITY-MIB", "uHardwareID"),
        ("ES-RACKTIVITY-MIB", "uPortState"),
        ("ES-RACKTIVITY-MIB", "eGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "eSpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "eCurrentTime"),
        ("ES-RACKTIVITY-MIB", "eVoltage"),
        ("ES-RACKTIVITY-MIB", "eFrequency"),
        ("ES-RACKTIVITY-MIB", "eCurrent"),
        ("ES-RACKTIVITY-MIB", "ePower"),
        ("ES-RACKTIVITY-MIB", "eActiveEnergy"),
        ("ES-RACKTIVITY-MIB", "eApparentEnergy"),
        ("ES-RACKTIVITY-MIB", "eTemperature"),
        ("ES-RACKTIVITY-MIB", "eApparentPower"),
        ("ES-RACKTIVITY-MIB", "ePowerFactor"),
        ("ES-RACKTIVITY-MIB", "eTotalCurrent"),
        ("ES-RACKTIVITY-MIB", "eTotalRealPower"),
        ("ES-RACKTIVITY-MIB", "eTotalApparentPower"),
        ("ES-RACKTIVITY-MIB", "eTotalActiveEnergy"),
        ("ES-RACKTIVITY-MIB", "eTotalApparentEnergy"),
        ("ES-RACKTIVITY-MIB", "eTotalPowerFactor"),
        ("ES-RACKTIVITY-MIB", "eTimeOnline"),
        ("ES-RACKTIVITY-MIB", "eTotalHarmonicDistortion"),
        ("ES-RACKTIVITY-MIB", "eModuleName"),
        ("ES-RACKTIVITY-MIB", "eFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "eHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "eFirmwareID"),
        ("ES-RACKTIVITY-MIB", "eHardwareID"),
        ("ES-RACKTIVITY-MIB", "eMaxCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "eMaxPowerWarning"),
        ("ES-RACKTIVITY-MIB", "eMaxTotalCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "eMaxTotalPowerWarning"),
        ("ES-RACKTIVITY-MIB", "eMaxVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "eMinVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "eMinTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "eMaxTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "eCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "ePowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "eTotalCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "eTotalPowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "eVoltageWarningEvent"),
        ("ES-RACKTIVITY-MIB", "eTemperatureWarningEvent"),
        ("ES-RACKTIVITY-MIB", "eMicroIntTimeThreshold"),
        ("ES-RACKTIVITY-MIB", "eMicroIntEvent"),
        ("ES-RACKTIVITY-MIB", "qGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "qSpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "qCurrentTime"),
        ("ES-RACKTIVITY-MIB", "qVoltage"),
        ("ES-RACKTIVITY-MIB", "qFrequency"),
        ("ES-RACKTIVITY-MIB", "qActiveEnergy"),
        ("ES-RACKTIVITY-MIB", "qApparentEnergy"),
        ("ES-RACKTIVITY-MIB", "qTemperature"),
        ("ES-RACKTIVITY-MIB", "qPowerFactor"),
        ("ES-RACKTIVITY-MIB", "qTimeOnline"),
        ("ES-RACKTIVITY-MIB", "qIOPort"),
        ("ES-RACKTIVITY-MIB", "qTotalHarmonicDistortion"),
        ("ES-RACKTIVITY-MIB", "qPhase"),
        ("ES-RACKTIVITY-MIB", "qBigCurrent"),
        ("ES-RACKTIVITY-MIB", "qBigPower"),
        ("ES-RACKTIVITY-MIB", "qBigApparentPower"),
        ("ES-RACKTIVITY-MIB", "qStatus"),
        ("ES-RACKTIVITY-MIB", "qModuleName"),
        ("ES-RACKTIVITY-MIB", "qFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "qHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "qFirmwareID"),
        ("ES-RACKTIVITY-MIB", "qHardwareID"),
        ("ES-RACKTIVITY-MIB", "qPortState"),
        ("ES-RACKTIVITY-MIB", "qMaxVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "qMinVoltageWarning"),
        ("ES-RACKTIVITY-MIB", "qMinTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "qMaxTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "qPortStateEvent"),
        ("ES-RACKTIVITY-MIB", "qCurrentWarningEvent"),
        ("ES-RACKTIVITY-MIB", "qPowerWarningEvent"),
        ("ES-RACKTIVITY-MIB", "qVoltageWarningEvent"),
        ("ES-RACKTIVITY-MIB", "qTemperatureWarningEvent"),
        ("ES-RACKTIVITY-MIB", "qMicroIntTimeThreshold"),
        ("ES-RACKTIVITY-MIB", "qMicroIntEvent"),
        ("ES-RACKTIVITY-MIB", "qDeviceID"),
        ("ES-RACKTIVITY-MIB", "qDeviceVersion"),
        ("ES-RACKTIVITY-MIB", "qMaxBigCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "qMaxBigPowerWarning"),
        ("ES-RACKTIVITY-MIB", "qCurrentSensorSelector"),
        ("ES-RACKTIVITY-MIB", "qMinBigCurrentWarning"),
        ("ES-RACKTIVITY-MIB", "qkWhMode"),
        ("ES-RACKTIVITY-MIB", "dGeneralModuleStatus"),
        ("ES-RACKTIVITY-MIB", "dSpecificModuleStatus"),
        ("ES-RACKTIVITY-MIB", "dCurrentTime"),
        ("ES-RACKTIVITY-MIB", "dTemperature"),
        ("ES-RACKTIVITY-MIB", "dTimeOnline"),
        ("ES-RACKTIVITY-MIB", "dModuleName"),
        ("ES-RACKTIVITY-MIB", "dFirmwareVersion"),
        ("ES-RACKTIVITY-MIB", "dHardwareVersion"),
        ("ES-RACKTIVITY-MIB", "dFirmwareID"),
        ("ES-RACKTIVITY-MIB", "dHardwareID"),
        ("ES-RACKTIVITY-MIB", "dMinTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "dMaxTemperatureWarning"),
        ("ES-RACKTIVITY-MIB", "dDisplayAllDevices"))
)
if mibBuilder.loadTexts:
    esRacktivityMIBGroup.setStatus("current")


# Notification objects

errorValueTooHighRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 16)
)
if mibBuilder.loadTexts:
    errorValueTooHighRaised.setStatus(
        "current"
    )

errorValueTooLowRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 17)
)
if mibBuilder.loadTexts:
    errorValueTooLowRaised.setStatus(
        "current"
    )

errorRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 18)
)
if mibBuilder.loadTexts:
    errorRaised.setStatus(
        "current"
    )

errorValueTooHighCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 19)
)
if mibBuilder.loadTexts:
    errorValueTooHighCleared.setStatus(
        "current"
    )

errorValueTooLowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 20)
)
if mibBuilder.loadTexts:
    errorValueTooLowCleared.setStatus(
        "current"
    )

errorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 21)
)
if mibBuilder.loadTexts:
    errorCleared.setStatus(
        "current"
    )

warningValueTooHighRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 48)
)
if mibBuilder.loadTexts:
    warningValueTooHighRaised.setStatus(
        "current"
    )

warningValueTooLowRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 49)
)
if mibBuilder.loadTexts:
    warningValueTooLowRaised.setStatus(
        "current"
    )

warningRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 50)
)
if mibBuilder.loadTexts:
    warningRaised.setStatus(
        "current"
    )

warningValueTooHighCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 51)
)
if mibBuilder.loadTexts:
    warningValueTooHighCleared.setStatus(
        "current"
    )

warningValueTooLowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 52)
)
if mibBuilder.loadTexts:
    warningValueTooLowCleared.setStatus(
        "current"
    )

warningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 53)
)
if mibBuilder.loadTexts:
    warningCleared.setStatus(
        "current"
    )

warningMicroInterruption = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 54)
)
if mibBuilder.loadTexts:
    warningMicroInterruption.setStatus(
        "current"
    )

warningPhaseShift = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 55)
)
if mibBuilder.loadTexts:
    warningPhaseShift.setStatus(
        "current"
    )

infoValueTooHighRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 80)
)
if mibBuilder.loadTexts:
    infoValueTooHighRaised.setStatus(
        "current"
    )

infoValueTooLowRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 81)
)
if mibBuilder.loadTexts:
    infoValueTooLowRaised.setStatus(
        "current"
    )

infoRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 82)
)
if mibBuilder.loadTexts:
    infoRaised.setStatus(
        "current"
    )

infoValueTooHighCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 83)
)
if mibBuilder.loadTexts:
    infoValueTooHighCleared.setStatus(
        "current"
    )

infoValueTooLowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 84)
)
if mibBuilder.loadTexts:
    infoValueTooLowCleared.setStatus(
        "current"
    )

infoCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 85)
)
if mibBuilder.loadTexts:
    infoCleared.setStatus(
        "current"
    )

infoPortStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 96)
)
if mibBuilder.loadTexts:
    infoPortStateChanged.setStatus(
        "current"
    )

infoReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 97)
)
if mibBuilder.loadTexts:
    infoReset.setStatus(
        "current"
    )

infoUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 98)
)
if mibBuilder.loadTexts:
    infoUpgrade.setStatus(
        "current"
    )

infoPortSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 99)
)
if mibBuilder.loadTexts:
    infoPortSchedule.setStatus(
        "current"
    )

infoHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 34097, 9, 0, 100)
)
if mibBuilder.loadTexts:
    infoHeartbeat.setStatus(
        "current"
    )


# Notifications groups

esRacktivityNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 34097, 9, 2, 1, 2)
)
esRacktivityNotificationGroup.setObjects(
      *(("ES-RACKTIVITY-MIB", "errorValueTooHighRaised"),
        ("ES-RACKTIVITY-MIB", "errorValueTooLowRaised"),
        ("ES-RACKTIVITY-MIB", "errorRaised"),
        ("ES-RACKTIVITY-MIB", "errorValueTooHighCleared"),
        ("ES-RACKTIVITY-MIB", "errorValueTooLowCleared"),
        ("ES-RACKTIVITY-MIB", "errorCleared"),
        ("ES-RACKTIVITY-MIB", "warningValueTooHighRaised"),
        ("ES-RACKTIVITY-MIB", "warningValueTooLowRaised"),
        ("ES-RACKTIVITY-MIB", "warningRaised"),
        ("ES-RACKTIVITY-MIB", "warningValueTooHighCleared"),
        ("ES-RACKTIVITY-MIB", "warningValueTooLowCleared"),
        ("ES-RACKTIVITY-MIB", "warningCleared"),
        ("ES-RACKTIVITY-MIB", "infoValueTooHighRaised"),
        ("ES-RACKTIVITY-MIB", "infoPortStateChanged"),
        ("ES-RACKTIVITY-MIB", "infoReset"),
        ("ES-RACKTIVITY-MIB", "infoValueTooLowRaised"),
        ("ES-RACKTIVITY-MIB", "infoRaised"),
        ("ES-RACKTIVITY-MIB", "infoValueTooHighCleared"),
        ("ES-RACKTIVITY-MIB", "infoValueTooLowCleared"),
        ("ES-RACKTIVITY-MIB", "infoCleared"),
        ("ES-RACKTIVITY-MIB", "infoUpgrade"),
        ("ES-RACKTIVITY-MIB", "warningMicroInterruption"),
        ("ES-RACKTIVITY-MIB", "warningPhaseShift"),
        ("ES-RACKTIVITY-MIB", "infoPortSchedule"),
        ("ES-RACKTIVITY-MIB", "infoHeartbeat"))
)
if mibBuilder.loadTexts:
    esRacktivityNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

esRacktivityConpliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34097, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    esRacktivityConpliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ES-RACKTIVITY-MIB",
    **{"Version": Version,
       "Utenth": Utenth,
       "Uhundredth": Uhundredth,
       "Uthousandth": Uthousandth,
       "Stenth": Stenth,
       "Shundredth": Shundredth,
       "Sthousandth": Sthousandth,
       "EVENTFLAGS": EVENTFLAGS,
       "CURPORTSTATE": CURPORTSTATE,
       "racktivity": racktivity,
       "esRACKTIVITYMIB": esRACKTIVITYMIB,
       "racktivityNotif": racktivityNotif,
       "errorValueTooHighRaised": errorValueTooHighRaised,
       "errorValueTooLowRaised": errorValueTooLowRaised,
       "errorRaised": errorRaised,
       "errorValueTooHighCleared": errorValueTooHighCleared,
       "errorValueTooLowCleared": errorValueTooLowCleared,
       "errorCleared": errorCleared,
       "warningValueTooHighRaised": warningValueTooHighRaised,
       "warningValueTooLowRaised": warningValueTooLowRaised,
       "warningRaised": warningRaised,
       "warningValueTooHighCleared": warningValueTooHighCleared,
       "warningValueTooLowCleared": warningValueTooLowCleared,
       "warningCleared": warningCleared,
       "warningMicroInterruption": warningMicroInterruption,
       "warningPhaseShift": warningPhaseShift,
       "infoValueTooHighRaised": infoValueTooHighRaised,
       "infoValueTooLowRaised": infoValueTooLowRaised,
       "infoRaised": infoRaised,
       "infoValueTooHighCleared": infoValueTooHighCleared,
       "infoValueTooLowCleared": infoValueTooLowCleared,
       "infoCleared": infoCleared,
       "infoPortStateChanged": infoPortStateChanged,
       "infoReset": infoReset,
       "infoUpgrade": infoUpgrade,
       "infoPortSchedule": infoPortSchedule,
       "infoHeartbeat": infoHeartbeat,
       "esRacktivityConformance": esRacktivityConformance,
       "esRacktivityMIBGroups": esRacktivityMIBGroups,
       "esRacktivityMIBGroup": esRacktivityMIBGroup,
       "esRacktivityNotificationGroup": esRacktivityNotificationGroup,
       "esRacktivityMIBCompliances": esRacktivityMIBCompliances,
       "esRacktivityConpliance": esRacktivityConpliance,
       "esnModule": esnModule,
       "eESNTable": eESNTable,
       "eESNEntry": eESNEntry,
       "aGeneralModuleStatus": aGeneralModuleStatus,
       "aSpecificModuleStatus": aSpecificModuleStatus,
       "aCurrentTime": aCurrentTime,
       "aVoltage": aVoltage,
       "aStatePortCur": aStatePortCur,
       "aTemperature": aTemperature,
       "aHumidity": aHumidity,
       "aAirflow": aAirflow,
       "aDewPoint": aDewPoint,
       "aPressure": aPressure,
       "aAnalogueInput": aAnalogueInput,
       "aWaterleak": aWaterleak,
       "aMotionDetected": aMotionDetected,
       "aIOPort": aIOPort,
       "aHighCurrent": aHighCurrent,
       "aHighPower": aHighPower,
       "aModuleName": aModuleName,
       "aFirmwareVersion": aFirmwareVersion,
       "aHardwareVersion": aHardwareVersion,
       "aFirmwareID": aFirmwareID,
       "aHardwareID": aHardwareID,
       "aDisplayTimeOn": aDisplayTimeOn,
       "aMaxVoltageWarning": aMaxVoltageWarning,
       "aMinVoltageWarning": aMinVoltageWarning,
       "aMinTemperatureWarning": aMinTemperatureWarning,
       "aMaxTemperatureWarning": aMaxTemperatureWarning,
       "aMinHumidityWarning": aMinHumidityWarning,
       "aMaxHumidityWarning": aMaxHumidityWarning,
       "aCurrentWarningEvent": aCurrentWarningEvent,
       "aPowerWarningEvent": aPowerWarningEvent,
       "aVoltageWarningEvent": aVoltageWarningEvent,
       "aTemperatureWarningEvent": aTemperatureWarningEvent,
       "aHumidityWarningEvent": aHumidityWarningEvent,
       "aDewPointWarning": aDewPointWarning,
       "aDewPointWarningEvent": aDewPointWarningEvent,
       "aDewPointViolationEvent": aDewPointViolationEvent,
       "aPressureWarningEvent": aPressureWarningEvent,
       "aMinPressureWarning": aMinPressureWarning,
       "aMaxPressureWarning": aMaxPressureWarning,
       "aDisplayBrightness": aDisplayBrightness,
       "aMotionSensitivity": aMotionSensitivity,
       "aExternalSensorLabel": aExternalSensorLabel,
       "aRelayLabel": aRelayLabel,
       "aMinAnalogueInputWarning": aMinAnalogueInputWarning,
       "aMaxAnalogueInputWarning": aMaxAnalogueInputWarning,
       "aWaterleakWarning": aWaterleakWarning,
       "aMinAirflowWarning": aMinAirflowWarning,
       "aMaxAirflowWarning": aMaxAirflowWarning,
       "aAnalogueInputWarningEvent": aAnalogueInputWarningEvent,
       "aWaterleakWarningEvent": aWaterleakWarningEvent,
       "aAirflowWarningEvent": aAirflowWarningEvent,
       "aRelayAssertActionEvent": aRelayAssertActionEvent,
       "aRelayDeassertActionEvent": aRelayDeassertActionEvent,
       "aMotionWarning": aMotionWarning,
       "aMotionWarningEvent": aMotionWarningEvent,
       "aDeviceID": aDeviceID,
       "aDeviceVersion": aDeviceVersion,
       "aSysName": aSysName,
       "aMaxHighCurrentWarning": aMaxHighCurrentWarning,
       "aMinHighCurrentWarning": aMinHighCurrentWarning,
       "aMinHighPowerWarning": aMinHighPowerWarning,
       "aMaxHighPowerWarning": aMaxHighPowerWarning,
       "aIOPortWarningEvent": aIOPortWarningEvent,
       "esnIndex": esnIndex,
       "esnModuleIndex": esnModuleIndex,
       "threephasepowerModule": threephasepowerModule,
       "eThreePhasePowerTable": eThreePhasePowerTable,
       "eThreePhasePowerEntry": eThreePhasePowerEntry,
       "threephasepowerIndex": threephasepowerIndex,
       "threephasepowerModuleIndex": threephasepowerModuleIndex,
       "displaymoduleModule": displaymoduleModule,
       "eDisplayModuleTable": eDisplayModuleTable,
       "eDisplayModuleEntry": eDisplayModuleEntry,
       "dGeneralModuleStatus": dGeneralModuleStatus,
       "dSpecificModuleStatus": dSpecificModuleStatus,
       "dCurrentTime": dCurrentTime,
       "dTemperature": dTemperature,
       "dTimeOnline": dTimeOnline,
       "dModuleName": dModuleName,
       "dFirmwareVersion": dFirmwareVersion,
       "dHardwareVersion": dHardwareVersion,
       "dFirmwareID": dFirmwareID,
       "dHardwareID": dHardwareID,
       "dMinTemperatureWarning": dMinTemperatureWarning,
       "dMaxTemperatureWarning": dMaxTemperatureWarning,
       "dDisplayAllDevices": dDisplayAllDevices,
       "displaymoduleIndex": displaymoduleIndex,
       "displaymoduleModuleIndex": displaymoduleModuleIndex,
       "energymonitorModule": energymonitorModule,
       "eEnergyMonitorTable": eEnergyMonitorTable,
       "eEnergyMonitorEntry": eEnergyMonitorEntry,
       "eGeneralModuleStatus": eGeneralModuleStatus,
       "eSpecificModuleStatus": eSpecificModuleStatus,
       "eCurrentTime": eCurrentTime,
       "eVoltage": eVoltage,
       "eFrequency": eFrequency,
       "eCurrent": eCurrent,
       "ePower": ePower,
       "eActiveEnergy": eActiveEnergy,
       "eApparentEnergy": eApparentEnergy,
       "eTemperature": eTemperature,
       "eApparentPower": eApparentPower,
       "ePowerFactor": ePowerFactor,
       "eTotalCurrent": eTotalCurrent,
       "eTotalRealPower": eTotalRealPower,
       "eTotalApparentPower": eTotalApparentPower,
       "eTotalActiveEnergy": eTotalActiveEnergy,
       "eTotalApparentEnergy": eTotalApparentEnergy,
       "eTotalPowerFactor": eTotalPowerFactor,
       "eTimeOnline": eTimeOnline,
       "eTotalHarmonicDistortion": eTotalHarmonicDistortion,
       "eModuleName": eModuleName,
       "eFirmwareVersion": eFirmwareVersion,
       "eHardwareVersion": eHardwareVersion,
       "eFirmwareID": eFirmwareID,
       "eHardwareID": eHardwareID,
       "eMaxCurrentWarning": eMaxCurrentWarning,
       "eMaxPowerWarning": eMaxPowerWarning,
       "eMaxTotalCurrentWarning": eMaxTotalCurrentWarning,
       "eMaxTotalPowerWarning": eMaxTotalPowerWarning,
       "eMaxVoltageWarning": eMaxVoltageWarning,
       "eMinVoltageWarning": eMinVoltageWarning,
       "eMinTemperatureWarning": eMinTemperatureWarning,
       "eMaxTemperatureWarning": eMaxTemperatureWarning,
       "eCurrentWarningEvent": eCurrentWarningEvent,
       "ePowerWarningEvent": ePowerWarningEvent,
       "eTotalCurrentWarningEvent": eTotalCurrentWarningEvent,
       "eTotalPowerWarningEvent": eTotalPowerWarningEvent,
       "eVoltageWarningEvent": eVoltageWarningEvent,
       "eTemperatureWarningEvent": eTemperatureWarningEvent,
       "eMicroIntTimeThreshold": eMicroIntTimeThreshold,
       "eMicroIntEvent": eMicroIntEvent,
       "energymonitorIndex": energymonitorIndex,
       "energymonitorModuleIndex": energymonitorModuleIndex,
       "masterModule": masterModule,
       "eMasterTable": eMasterTable,
       "eMasterEntry": eMasterEntry,
       "mGeneralModuleStatus": mGeneralModuleStatus,
       "mSpecificModuleStatus": mSpecificModuleStatus,
       "mCurrentTime": mCurrentTime,
       "mVoltage": mVoltage,
       "mTemperature": mTemperature,
       "mCurrentIP": mCurrentIP,
       "mTotalCurrent": mTotalCurrent,
       "mTotalRealPower": mTotalRealPower,
       "mTotalActiveEnergy": mTotalActiveEnergy,
       "mLineCurrent": mLineCurrent,
       "mFuseCurrent": mFuseCurrent,
       "mCurrentSubNetMask": mCurrentSubNetMask,
       "mCurrentDNSServer": mCurrentDNSServer,
       "mCurrentStdGateway": mCurrentStdGateway,
       "mUPSPresent": mUPSPresent,
       "mUPSStatus": mUPSStatus,
       "mUPSEstimatedRunTime": mUPSEstimatedRunTime,
       "mUPSBatteryLevel": mUPSBatteryLevel,
       "mHighCurrent": mHighCurrent,
       "mUpsCommunicationStatus": mUpsCommunicationStatus,
       "mHighPower": mHighPower,
       "mTotalHighCurrent": mTotalHighCurrent,
       "mTotalHighPower": mTotalHighPower,
       "mPositiveEnergy": mPositiveEnergy,
       "mNegativeEnergy": mNegativeEnergy,
       "mTotalPositiveEnergy": mTotalPositiveEnergy,
       "mTotalNegativeEnergy": mTotalNegativeEnergy,
       "mCloudStatus": mCloudStatus,
       "mStatus": mStatus,
       "mModuleName": mModuleName,
       "mFirmwareVersion": mFirmwareVersion,
       "mHardwareVersion": mHardwareVersion,
       "mFirmwareID": mFirmwareID,
       "mHardwareID": mHardwareID,
       "mRackName": mRackName,
       "mRackPosition": mRackPosition,
       "mIPAddress": mIPAddress,
       "mSubNetMask": mSubNetMask,
       "mStdGateWay": mStdGateWay,
       "mDnsServer": mDnsServer,
       "mMAC": mMAC,
       "mDHCPEnable": mDHCPEnable,
       "mNTPServer": mNTPServer,
       "mUseDefaultNTPServer": mUseDefaultNTPServer,
       "mUseNTP": mUseNTP,
       "mSNMPTrapRecvIP": mSNMPTrapRecvIP,
       "mSNMPTrapRecvPort": mSNMPTrapRecvPort,
       "mSNMPControl": mSNMPControl,
       "mECSServer": mECSServer,
       "mUseECSServer": mUseECSServer,
       "mDisplayLock": mDisplayLock,
       "mDisplayTimeOn": mDisplayTimeOn,
       "mMaxVoltageWarning": mMaxVoltageWarning,
       "mMinVoltageWarning": mMinVoltageWarning,
       "mMinTemperatureWarning": mMinTemperatureWarning,
       "mMaxTemperatureWarning": mMaxTemperatureWarning,
       "mGeneralEventEnable": mGeneralEventEnable,
       "mSNMPSysContact": mSNMPSysContact,
       "mCurrentWarningEvent": mCurrentWarningEvent,
       "mPowerWarningEvent": mPowerWarningEvent,
       "mTotalCurrentWarningEvent": mTotalCurrentWarningEvent,
       "mTotalPowerWarningEvent": mTotalPowerWarningEvent,
       "mVoltageWarningEvent": mVoltageWarningEvent,
       "mTemperatureWarningEvent": mTemperatureWarningEvent,
       "mDisplayBrightness": mDisplayBrightness,
       "mECSServerPort": mECSServerPort,
       "mExternalSensorLabel": mExternalSensorLabel,
       "mHttpsOnly": mHttpsOnly,
       "mTelnetSsl": mTelnetSsl,
       "mCookieTimeToLive": mCookieTimeToLive,
       "mLineCurrentWarningThreshold": mLineCurrentWarningThreshold,
       "mLineCurrentOffThreshold": mLineCurrentOffThreshold,
       "mLineCurrentWarningEvent": mLineCurrentWarningEvent,
       "mLineCurrentOffEvent": mLineCurrentOffEvent,
       "mFuseCurrentWarningThreshold": mFuseCurrentWarningThreshold,
       "mFuseCurrentOffThreshold": mFuseCurrentOffThreshold,
       "mFuseCurrentWarningEvent": mFuseCurrentWarningEvent,
       "mFuseCurrentOffEvent": mFuseCurrentOffEvent,
       "mDeviceID": mDeviceID,
       "mDeviceVersion": mDeviceVersion,
       "mSysName": mSysName,
       "mElectricalTopology": mElectricalTopology,
       "mFusePortTopology": mFusePortTopology,
       "mLineFuseTopology": mLineFuseTopology,
       "mSSOIPAddress": mSSOIPAddress,
       "mSSOLoginCredentials": mSSOLoginCredentials,
       "mSSOGracefullShutdown": mSSOGracefullShutdown,
       "mUPSWarningLevel": mUPSWarningLevel,
       "mUPSOffLevel": mUPSOffLevel,
       "mMaxHighCurrentWarning": mMaxHighCurrentWarning,
       "mUpsMonitoringProtocol": mUpsMonitoringProtocol,
       "mUpsEmergencyThreshold": mUpsEmergencyThreshold,
       "mUpsRecoveryThreshold": mUpsRecoveryThreshold,
       "mUpsEventFlags": mUpsEventFlags,
       "mRecoveryPowerThreshold": mRecoveryPowerThreshold,
       "mMinHighCurrentWarning": mMinHighCurrentWarning,
       "mMinHighPowerWarning": mMinHighPowerWarning,
       "mMaxHighPowerWarning": mMaxHighPowerWarning,
       "mHeartbeatInterval": mHeartbeatInterval,
       "mMinTotalHighCurrentWarning": mMinTotalHighCurrentWarning,
       "mMaxTotalHighCurrentWarning": mMaxTotalHighCurrentWarning,
       "mMinTotalHighPowerWarning": mMinTotalHighPowerWarning,
       "mMaxTotalHighPowerWarning": mMaxTotalHighPowerWarning,
       "mCloudState": mCloudState,
       "mSensorBias": mSensorBias,
       "mDaisyChainDeviceMode": mDaisyChainDeviceMode,
       "mSNMPTrapUser": mSNMPTrapUser,
       "mUSMUser": mUSMUser,
       "mUSMAuthPassphrase": mUSMAuthPassphrase,
       "mUSMPrivPassphrase": mUSMPrivPassphrase,
       "mSNMPV2GetSetEnable": mSNMPV2GetSetEnable,
       "mSNMPV3GetSetEnable": mSNMPV3GetSetEnable,
       "mUSMAuthPassphraseLength": mUSMAuthPassphraseLength,
       "mUSMPrivPassphraseLength": mUSMPrivPassphraseLength,
       "mSNMPTrapEnable": mSNMPTrapEnable,
       "mLDAPAttribute": mLDAPAttribute,
       "mLDAPPath": mLDAPPath,
       "mLDAPAdminGroupName": mLDAPAdminGroupName,
       "mLDAPRestrictedGroupName": mLDAPRestrictedGroupName,
       "mLDAPGuestGroupName": mLDAPGuestGroupName,
       "mLDAPEnable": mLDAPEnable,
       "mLDAPLoginWrapper": mLDAPLoginWrapper,
       "mLDAPServer": mLDAPServer,
       "mLocalAuthEnable": mLocalAuthEnable,
       "masterIndex": masterIndex,
       "masterModuleIndex": masterModuleIndex,
       "powerModule": powerModule,
       "ePowerTable": ePowerTable,
       "ePowerEntry": ePowerEntry,
       "pGeneralModuleStatus": pGeneralModuleStatus,
       "pSpecificModuleStatus": pSpecificModuleStatus,
       "pCurrentTime": pCurrentTime,
       "pVoltage": pVoltage,
       "pFrequency": pFrequency,
       "pCurrent": pCurrent,
       "pPower": pPower,
       "pStatePortCur": pStatePortCur,
       "pActiveEnergy": pActiveEnergy,
       "pApparentEnergy": pApparentEnergy,
       "pTemperature": pTemperature,
       "pApparentPower": pApparentPower,
       "pPowerFactor": pPowerFactor,
       "pTotalCurrent": pTotalCurrent,
       "pTotalRealPower": pTotalRealPower,
       "pTotalApparentPower": pTotalApparentPower,
       "pTotalActiveEnergy": pTotalActiveEnergy,
       "pTotalApparentEnergy": pTotalApparentEnergy,
       "pTotalPowerFactor": pTotalPowerFactor,
       "pTimeOnline": pTimeOnline,
       "pTotalHarmonicDistortion": pTotalHarmonicDistortion,
       "pPhase": pPhase,
       "pBigCurrent": pBigCurrent,
       "pBigPower": pBigPower,
       "pBigApparentPower": pBigApparentPower,
       "pDetectedPhase": pDetectedPhase,
       "pModuleName": pModuleName,
       "pFirmwareVersion": pFirmwareVersion,
       "pHardwareVersion": pHardwareVersion,
       "pFirmwareID": pFirmwareID,
       "pHardwareID": pHardwareID,
       "pPortName": pPortName,
       "pPortState": pPortState,
       "pCurrentPriorOff": pCurrentPriorOff,
       "pDelayOn": pDelayOn,
       "pMaxCurrentOff": pMaxCurrentOff,
       "pMaxCurrentWarning": pMaxCurrentWarning,
       "pMaxPowerOff": pMaxPowerOff,
       "pMaxPowerWarning": pMaxPowerWarning,
       "pMaxTotalCurrentOff": pMaxTotalCurrentOff,
       "pMaxTotalCurrentWarning": pMaxTotalCurrentWarning,
       "pMaxTotalPowerOff": pMaxTotalPowerOff,
       "pMaxTotalPowerWarning": pMaxTotalPowerWarning,
       "pMaxVoltageWarning": pMaxVoltageWarning,
       "pMinVoltageWarning": pMinVoltageWarning,
       "pMinTemperatureWarning": pMinTemperatureWarning,
       "pMaxTemperatureWarning": pMaxTemperatureWarning,
       "pPortStateEvent": pPortStateEvent,
       "pCurrentOffEvent": pCurrentOffEvent,
       "pCurrentWarningEvent": pCurrentWarningEvent,
       "pPowerOffEvent": pPowerOffEvent,
       "pPowerWarningEvent": pPowerWarningEvent,
       "pTotalCurrentOffEvent": pTotalCurrentOffEvent,
       "pTotalCurrentWarningEvent": pTotalCurrentWarningEvent,
       "pTotalPowerOffEvent": pTotalPowerOffEvent,
       "pTotalPowerWarningEvent": pTotalPowerWarningEvent,
       "pVoltageWarningEvent": pVoltageWarningEvent,
       "pTemperatureWarningEvent": pTemperatureWarningEvent,
       "pMaxOverheatingOff": pMaxOverheatingOff,
       "pOverheatingOffEvent": pOverheatingOffEvent,
       "pPowerCycleTime": pPowerCycleTime,
       "pExternalSensorLabel": pExternalSensorLabel,
       "pMaxOverheatingWarning": pMaxOverheatingWarning,
       "pOverheatingWarningEvent": pOverheatingWarningEvent,
       "pMicroIntTimeThreshold": pMicroIntTimeThreshold,
       "pMicroIntEvent": pMicroIntEvent,
       "pSoftFuseCurrentThreshold": pSoftFuseCurrentThreshold,
       "pSoftFuseDelay": pSoftFuseDelay,
       "pSoftFuseEvent": pSoftFuseEvent,
       "pPhaseShiftEvent": pPhaseShiftEvent,
       "pSchedulePortOnTime": pSchedulePortOnTime,
       "pSchedulePortOffTime": pSchedulePortOffTime,
       "pEnableSchedulePort": pEnableSchedulePort,
       "pBlockSetPortOff": pBlockSetPortOff,
       "pSchedulePortChangeEvent": pSchedulePortChangeEvent,
       "pAgentIP": pAgentIP,
       "pAgentPort": pAgentPort,
       "pAgentCommunicationEventFlags": pAgentCommunicationEventFlags,
       "pAlwaysOn": pAlwaysOn,
       "pGenericTransducerParameters": pGenericTransducerParameters,
       "pMaxBigCurrentWarning": pMaxBigCurrentWarning,
       "pMaxBigPowerWarning": pMaxBigPowerWarning,
       "pGroupNumber": pGroupNumber,
       "pPhaseLink": pPhaseLink,
       "pCurrentSensorSelector": pCurrentSensorSelector,
       "pMinBigCurrentWarning": pMinBigCurrentWarning,
       "powerIndex": powerIndex,
       "powerModuleIndex": powerModuleIndex,
       "measuring3phaseModule": measuring3phaseModule,
       "eMeasuring3PhaseTable": eMeasuring3PhaseTable,
       "eMeasuring3PhaseEntry": eMeasuring3PhaseEntry,
       "qGeneralModuleStatus": qGeneralModuleStatus,
       "qSpecificModuleStatus": qSpecificModuleStatus,
       "qCurrentTime": qCurrentTime,
       "qVoltage": qVoltage,
       "qFrequency": qFrequency,
       "qActiveEnergy": qActiveEnergy,
       "qApparentEnergy": qApparentEnergy,
       "qTemperature": qTemperature,
       "qPowerFactor": qPowerFactor,
       "qTimeOnline": qTimeOnline,
       "qIOPort": qIOPort,
       "qTotalHarmonicDistortion": qTotalHarmonicDistortion,
       "qPhase": qPhase,
       "qBigCurrent": qBigCurrent,
       "qBigPower": qBigPower,
       "qBigApparentPower": qBigApparentPower,
       "qStatus": qStatus,
       "qModuleName": qModuleName,
       "qFirmwareVersion": qFirmwareVersion,
       "qHardwareVersion": qHardwareVersion,
       "qFirmwareID": qFirmwareID,
       "qHardwareID": qHardwareID,
       "qPortState": qPortState,
       "qMaxVoltageWarning": qMaxVoltageWarning,
       "qMinVoltageWarning": qMinVoltageWarning,
       "qMinTemperatureWarning": qMinTemperatureWarning,
       "qMaxTemperatureWarning": qMaxTemperatureWarning,
       "qPortStateEvent": qPortStateEvent,
       "qCurrentWarningEvent": qCurrentWarningEvent,
       "qPowerWarningEvent": qPowerWarningEvent,
       "qVoltageWarningEvent": qVoltageWarningEvent,
       "qTemperatureWarningEvent": qTemperatureWarningEvent,
       "qMicroIntTimeThreshold": qMicroIntTimeThreshold,
       "qMicroIntEvent": qMicroIntEvent,
       "qDeviceID": qDeviceID,
       "qDeviceVersion": qDeviceVersion,
       "qMaxBigCurrentWarning": qMaxBigCurrentWarning,
       "qMaxBigPowerWarning": qMaxBigPowerWarning,
       "qCurrentSensorSelector": qCurrentSensorSelector,
       "qMinBigCurrentWarning": qMinBigCurrentWarning,
       "qkWhMode": qkWhMode,
       "measuring3phaseIndex": measuring3phaseIndex,
       "measuring3phaseModuleIndex": measuring3phaseModuleIndex,
       "pcModule": pcModule,
       "ePCTable": ePCTable,
       "ePCEntry": ePCEntry,
       "uGeneralModuleStatus": uGeneralModuleStatus,
       "uSpecificModuleStatus": uSpecificModuleStatus,
       "uCurrentTime": uCurrentTime,
       "uVoltage": uVoltage,
       "uCurrent": uCurrent,
       "uStatePortCur": uStatePortCur,
       "uTemperature": uTemperature,
       "uHumidity": uHumidity,
       "uModuleName": uModuleName,
       "uFirmwareVersion": uFirmwareVersion,
       "uHardwareVersion": uHardwareVersion,
       "uFirmwareID": uFirmwareID,
       "uHardwareID": uHardwareID,
       "uPortState": uPortState,
       "pcIndex": pcIndex,
       "pcModuleIndex": pcModuleIndex,
       "testmoduleModule": testmoduleModule,
       "eTestModuleTable": eTestModuleTable,
       "eTestModuleEntry": eTestModuleEntry,
       "yGeneralModuleStatus": yGeneralModuleStatus,
       "ySpecificModuleStatus": ySpecificModuleStatus,
       "yCurrentTime": yCurrentTime,
       "yCurrent": yCurrent,
       "yStatePortCur": yStatePortCur,
       "yAnalogueInput": yAnalogueInput,
       "yModuleName": yModuleName,
       "yFirmwareVersion": yFirmwareVersion,
       "yHardwareVersion": yHardwareVersion,
       "yFirmwareID": yFirmwareID,
       "yHardwareID": yHardwareID,
       "testmoduleIndex": testmoduleIndex,
       "testmoduleModuleIndex": testmoduleModuleIndex}
)
