# SNMP MIB module (EATON-EPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-EPDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:19 2024
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

(pduAgent,) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "pduAgent")

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
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eatonEpdu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7)
)
eatonEpdu.setRevisions(
        ("2014-09-29 12:00",
         "2013-12-18 12:00",
         "2013-09-02 12:00",
         "2013-05-29 12:00",
         "2013-02-21 12:00",
         "2011-11-21 12:00",
         "2011-10-24 12:00",
         "2011-02-07 15:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UnixTimeStamp(Counter32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0)
)
_Units_ObjectIdentity = ObjectIdentity
units = _Units_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1)
)
_UnitsPresent_Type = DisplayString
_UnitsPresent_Object = MibScalar
unitsPresent = _UnitsPresent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 1),
    _UnitsPresent_Type()
)
unitsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitsPresent.setStatus("current")
_UnitTable_Object = MibTable
unitTable = _UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2)
)
if mibBuilder.loadTexts:
    unitTable.setStatus("current")
_UnitEntry_Object = MibTableRow
unitEntry = _UnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1)
)
unitEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
)
if mibBuilder.loadTexts:
    unitEntry.setStatus("current")


class _StrappingIndex_Type(Integer32):
    """Custom type strappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_StrappingIndex_Type.__name__ = "Integer32"
_StrappingIndex_Object = MibTableColumn
strappingIndex = _StrappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 1),
    _StrappingIndex_Type()
)
strappingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    strappingIndex.setStatus("current")


class _ProductName_Type(OctetString):
    """Custom type productName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_ProductName_Type.__name__ = "OctetString"
_ProductName_Object = MibTableColumn
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 2),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_PartNumber_Type = OctetString
_PartNumber_Object = MibTableColumn
partNumber = _PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 3),
    _PartNumber_Type()
)
partNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNumber.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FirmwareVersion_Type = OctetString
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 5),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _UnitName_Type(OctetString):
    """Custom type unitName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_UnitName_Type.__name__ = "OctetString"
_UnitName_Object = MibTableColumn
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 6),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")


class _LcdControl_Type(Integer32):
    """Custom type lcdControl based on Integer32"""
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
        *(("lcdKeyLock", 2),
          ("lcdScreenOff", 1),
          ("lcdScreenOffAndKeyLock", 3),
          ("notApplicable", 0))
    )


_LcdControl_Type.__name__ = "Integer32"
_LcdControl_Object = MibTableColumn
lcdControl = _LcdControl_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 7),
    _LcdControl_Type()
)
lcdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcdControl.setStatus("current")
_ClockValue_Type = DateAndTime
_ClockValue_Object = MibTableColumn
clockValue = _ClockValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 8),
    _ClockValue_Type()
)
clockValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockValue.setStatus("current")


class _TemperatureScale_Type(Integer32):
    """Custom type temperatureScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 0),
          ("fahrenheit", 1))
    )


_TemperatureScale_Type.__name__ = "Integer32"
_TemperatureScale_Object = MibTableColumn
temperatureScale = _TemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 9),
    _TemperatureScale_Type()
)
temperatureScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureScale.setStatus("current")


class _UnitType_Type(Integer32):
    """Custom type unitType based on Integer32"""
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
        *(("advancedMonitored", 2),
          ("managed", 3),
          ("monitored", 4),
          ("switched", 1),
          ("unknown", 0))
    )


_UnitType_Type.__name__ = "Integer32"
_UnitType_Object = MibTableColumn
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 10),
    _UnitType_Type()
)
unitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitType.setStatus("current")
_InputCount_Type = Integer32
_InputCount_Object = MibTableColumn
inputCount = _InputCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 20),
    _InputCount_Type()
)
inputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCount.setStatus("current")
_GroupCount_Type = Integer32
_GroupCount_Object = MibTableColumn
groupCount = _GroupCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 21),
    _GroupCount_Type()
)
groupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCount.setStatus("current")
_OutletCount_Type = Integer32
_OutletCount_Object = MibTableColumn
outletCount = _OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 22),
    _OutletCount_Type()
)
outletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCount.setStatus("current")
_TemperatureCount_Type = Integer32
_TemperatureCount_Object = MibTableColumn
temperatureCount = _TemperatureCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 23),
    _TemperatureCount_Type()
)
temperatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCount.setStatus("current")
_HumidityCount_Type = Integer32
_HumidityCount_Object = MibTableColumn
humidityCount = _HumidityCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 24),
    _HumidityCount_Type()
)
humidityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityCount.setStatus("current")
_ContactCount_Type = Integer32
_ContactCount_Object = MibTableColumn
contactCount = _ContactCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 25),
    _ContactCount_Type()
)
contactCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactCount.setStatus("current")


class _CommunicationStatus_Type(Integer32):
    """Custom type communicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("communicationLost", 1),
          ("good", 0))
    )


_CommunicationStatus_Type.__name__ = "Integer32"
_CommunicationStatus_Object = MibTableColumn
communicationStatus = _CommunicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 30),
    _CommunicationStatus_Type()
)
communicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communicationStatus.setStatus("current")


class _InternalStatus_Type(Integer32):
    """Custom type internalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("internalFailure", 1))
    )


_InternalStatus_Type.__name__ = "Integer32"
_InternalStatus_Object = MibTableColumn
internalStatus = _InternalStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 31),
    _InternalStatus_Type()
)
internalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalStatus.setStatus("current")


class _StrappingStatus_Type(Integer32):
    """Custom type strappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("communicationLost", 1),
          ("good", 0))
    )


_StrappingStatus_Type.__name__ = "Integer32"
_StrappingStatus_Object = MibTableColumn
strappingStatus = _StrappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 32),
    _StrappingStatus_Type()
)
strappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strappingStatus.setStatus("current")


class _UserName_Type(OctetString):
    """Custom type userName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UserName_Type.__name__ = "OctetString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 40),
    _UserName_Type()
)
userName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _CommInterface_Type(Integer32):
    """Custom type commInterface based on Integer32"""
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
        *(("ftp", 4),
          ("serial", 0),
          ("telnet", 2),
          ("usb", 1),
          ("web", 3),
          ("xml", 5))
    )


_CommInterface_Type.__name__ = "Integer32"
_CommInterface_Object = MibTableColumn
commInterface = _CommInterface_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 2, 1, 41),
    _CommInterface_Type()
)
commInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    commInterface.setStatus("current")
_UnitControlTable_Object = MibTable
unitControlTable = _UnitControlTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 3)
)
if mibBuilder.loadTexts:
    unitControlTable.setStatus("current")
_UnitControlEntry_Object = MibTableRow
unitControlEntry = _UnitControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 3, 1)
)
unitControlEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
)
if mibBuilder.loadTexts:
    unitControlEntry.setStatus("current")


class _UnitControlOffCmd_Type(Integer32):
    """Custom type unitControlOffCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_UnitControlOffCmd_Type.__name__ = "Integer32"
_UnitControlOffCmd_Object = MibTableColumn
unitControlOffCmd = _UnitControlOffCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 3, 1, 2),
    _UnitControlOffCmd_Type()
)
unitControlOffCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitControlOffCmd.setStatus("current")


class _UnitControlOnCmd_Type(Integer32):
    """Custom type unitControlOnCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_UnitControlOnCmd_Type.__name__ = "Integer32"
_UnitControlOnCmd_Object = MibTableColumn
unitControlOnCmd = _UnitControlOnCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 1, 3, 1, 3),
    _UnitControlOnCmd_Type()
)
unitControlOnCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitControlOnCmd.setStatus("current")
_Inputs_ObjectIdentity = ObjectIdentity
inputs = _Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3)
)
_InputTable_Object = MibTable
inputTable = _InputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1)
)
if mibBuilder.loadTexts:
    inputTable.setStatus("current")
_InputEntry_Object = MibTableRow
inputEntry = _InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1)
)
inputEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "inputIndex"),
)
if mibBuilder.loadTexts:
    inputEntry.setStatus("current")


class _InputIndex_Type(Integer32):
    """Custom type inputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_InputIndex_Type.__name__ = "Integer32"
_InputIndex_Object = MibTableColumn
inputIndex = _InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 1),
    _InputIndex_Type()
)
inputIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inputIndex.setStatus("current")


class _InputType_Type(Integer32):
    """Custom type inputType based on Integer32"""
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
        *(("singlePhase", 1),
          ("splitPhase", 2),
          ("threePhaseDelta", 3),
          ("threePhaseWye", 4))
    )


_InputType_Type.__name__ = "Integer32"
_InputType_Object = MibTableColumn
inputType = _InputType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 2),
    _InputType_Type()
)
inputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputType.setStatus("current")
_InputFrequency_Type = Integer32
_InputFrequency_Object = MibTableColumn
inputFrequency = _InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 3),
    _InputFrequency_Type()
)
inputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputFrequency.setStatus("current")


class _InputFrequencyStatus_Type(Integer32):
    """Custom type inputFrequencyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("outOfRange", 1))
    )


_InputFrequencyStatus_Type.__name__ = "Integer32"
_InputFrequencyStatus_Object = MibTableColumn
inputFrequencyStatus = _InputFrequencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 4),
    _InputFrequencyStatus_Type()
)
inputFrequencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputFrequencyStatus.setStatus("current")
_InputVoltageCount_Type = Integer32
_InputVoltageCount_Object = MibTableColumn
inputVoltageCount = _InputVoltageCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 5),
    _InputVoltageCount_Type()
)
inputVoltageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageCount.setStatus("current")
_InputCurrentCount_Type = Integer32
_InputCurrentCount_Object = MibTableColumn
inputCurrentCount = _InputCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 6),
    _InputCurrentCount_Type()
)
inputCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentCount.setStatus("current")
_InputPowerCount_Type = Integer32
_InputPowerCount_Object = MibTableColumn
inputPowerCount = _InputPowerCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 7),
    _InputPowerCount_Type()
)
inputPowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPowerCount.setStatus("current")


class _InputPlugType_Type(Integer32):
    """Custom type inputPlugType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              150,
              151,
              152,
              200,
              201,
              202,
              300,
              301,
              302,
              303,
              304,
              306,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              350,
              351)
        )
    )
    namedValues = NamedValues(
        *(("bladeUps208V", 350),
          ("bladeUps400V", 351),
          ("cs8265", 130),
          ("cs8365", 324),
          ("french", 150),
          ("iec316P6", 103),
          ("iec332P6", 104),
          ("iec360P6", 105),
          ("iec460P9", 302),
          ("iec516P6", 301),
          ("iec532P6", 304),
          ("iec560P9", 303),
          ("iec563P6", 306),
          ("iecC14Inlet", 101),
          ("iecC14Plug", 106),
          ("iecC20Inlet", 102),
          ("iecC20Plug", 107),
          ("nema515", 120),
          ("nema520", 122),
          ("nema615", 124),
          ("nema620", 127),
          ("nemaL1420", 201),
          ("nemaL1430", 202),
          ("nemaL1520", 320),
          ("nemaL1530", 322),
          ("nemaL2120", 321),
          ("nemaL2130", 323),
          ("nemaL2220", 325),
          ("nemaL2230", 326),
          ("nemaL515", 121),
          ("nemaL520", 123),
          ("nemaL530", 126),
          ("nemaL615", 125),
          ("nemaL620", 128),
          ("nemaL630", 129),
          ("other1Phase", 100),
          ("other2Phase", 200),
          ("other3Phase", 300),
          ("schuko", 151),
          ("uk", 152))
    )


_InputPlugType_Type.__name__ = "Integer32"
_InputPlugType_Object = MibTableColumn
inputPlugType = _InputPlugType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 1, 1, 8),
    _InputPlugType_Type()
)
inputPlugType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPlugType.setStatus("current")
_InputVoltageTable_Object = MibTable
inputVoltageTable = _InputVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2)
)
if mibBuilder.loadTexts:
    inputVoltageTable.setStatus("current")
_InputVoltageEntry_Object = MibTableRow
inputVoltageEntry = _InputVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1)
)
inputVoltageEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "inputIndex"),
    (0, "EATON-EPDU-MIB", "inputVoltageIndex"),
)
if mibBuilder.loadTexts:
    inputVoltageEntry.setStatus("current")


class _InputVoltageIndex_Type(Integer32):
    """Custom type inputVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_InputVoltageIndex_Type.__name__ = "Integer32"
_InputVoltageIndex_Object = MibTableColumn
inputVoltageIndex = _InputVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 1),
    _InputVoltageIndex_Type()
)
inputVoltageIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inputVoltageIndex.setStatus("current")


class _InputVoltageMeasType_Type(Integer32):
    """Custom type inputVoltageMeasType based on Integer32"""
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
        *(("phase1to2", 5),
          ("phase1toN", 2),
          ("phase2to3", 6),
          ("phase2toN", 3),
          ("phase3to1", 7),
          ("phase3toN", 4),
          ("singlePhase", 1))
    )


_InputVoltageMeasType_Type.__name__ = "Integer32"
_InputVoltageMeasType_Object = MibTableColumn
inputVoltageMeasType = _InputVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 2),
    _InputVoltageMeasType_Type()
)
inputVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageMeasType.setStatus("current")
_InputVoltage_Type = Integer32
_InputVoltage_Object = MibTableColumn
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 3),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("current")


class _InputVoltageThStatus_Type(Integer32):
    """Custom type inputVoltageThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_InputVoltageThStatus_Type.__name__ = "Integer32"
_InputVoltageThStatus_Object = MibTableColumn
inputVoltageThStatus = _InputVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 4),
    _InputVoltageThStatus_Type()
)
inputVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltageThStatus.setStatus("current")


class _InputVoltageThLowerWarning_Type(Integer32):
    """Custom type inputVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_InputVoltageThLowerWarning_Type.__name__ = "Integer32"
_InputVoltageThLowerWarning_Object = MibTableColumn
inputVoltageThLowerWarning = _InputVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 5),
    _InputVoltageThLowerWarning_Type()
)
inputVoltageThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputVoltageThLowerWarning.setStatus("current")


class _InputVoltageThLowerCritical_Type(Integer32):
    """Custom type inputVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_InputVoltageThLowerCritical_Type.__name__ = "Integer32"
_InputVoltageThLowerCritical_Object = MibTableColumn
inputVoltageThLowerCritical = _InputVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 6),
    _InputVoltageThLowerCritical_Type()
)
inputVoltageThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputVoltageThLowerCritical.setStatus("current")


class _InputVoltageThUpperWarning_Type(Integer32):
    """Custom type inputVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_InputVoltageThUpperWarning_Type.__name__ = "Integer32"
_InputVoltageThUpperWarning_Object = MibTableColumn
inputVoltageThUpperWarning = _InputVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 7),
    _InputVoltageThUpperWarning_Type()
)
inputVoltageThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputVoltageThUpperWarning.setStatus("current")


class _InputVoltageThUpperCritical_Type(Integer32):
    """Custom type inputVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_InputVoltageThUpperCritical_Type.__name__ = "Integer32"
_InputVoltageThUpperCritical_Object = MibTableColumn
inputVoltageThUpperCritical = _InputVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 2, 1, 8),
    _InputVoltageThUpperCritical_Type()
)
inputVoltageThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputVoltageThUpperCritical.setStatus("current")
_InputCurrentTable_Object = MibTable
inputCurrentTable = _InputCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3)
)
if mibBuilder.loadTexts:
    inputCurrentTable.setStatus("current")
_InputCurrentEntry_Object = MibTableRow
inputCurrentEntry = _InputCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1)
)
inputCurrentEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "inputIndex"),
    (0, "EATON-EPDU-MIB", "inputCurrentIndex"),
)
if mibBuilder.loadTexts:
    inputCurrentEntry.setStatus("current")


class _InputCurrentIndex_Type(Integer32):
    """Custom type inputCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_InputCurrentIndex_Type.__name__ = "Integer32"
_InputCurrentIndex_Object = MibTableColumn
inputCurrentIndex = _InputCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 1),
    _InputCurrentIndex_Type()
)
inputCurrentIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inputCurrentIndex.setStatus("current")


class _InputCurrentMeasType_Type(Integer32):
    """Custom type inputCurrentMeasType based on Integer32"""
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
        *(("neutral", 2),
          ("phase1", 3),
          ("phase2", 4),
          ("phase3", 5),
          ("singlePhase", 1))
    )


_InputCurrentMeasType_Type.__name__ = "Integer32"
_InputCurrentMeasType_Object = MibTableColumn
inputCurrentMeasType = _InputCurrentMeasType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 2),
    _InputCurrentMeasType_Type()
)
inputCurrentMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentMeasType.setStatus("current")
_InputCurrentCapacity_Type = Integer32
_InputCurrentCapacity_Object = MibTableColumn
inputCurrentCapacity = _InputCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 3),
    _InputCurrentCapacity_Type()
)
inputCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentCapacity.setStatus("current")
_InputCurrent_Type = Integer32
_InputCurrent_Object = MibTableColumn
inputCurrent = _InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 4),
    _InputCurrent_Type()
)
inputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrent.setStatus("current")


class _InputCurrentThStatus_Type(Integer32):
    """Custom type inputCurrentThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_InputCurrentThStatus_Type.__name__ = "Integer32"
_InputCurrentThStatus_Object = MibTableColumn
inputCurrentThStatus = _InputCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 5),
    _InputCurrentThStatus_Type()
)
inputCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentThStatus.setStatus("current")


class _InputCurrentThLowerWarning_Type(Integer32):
    """Custom type inputCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_InputCurrentThLowerWarning_Type.__name__ = "Integer32"
_InputCurrentThLowerWarning_Object = MibTableColumn
inputCurrentThLowerWarning = _InputCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 6),
    _InputCurrentThLowerWarning_Type()
)
inputCurrentThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputCurrentThLowerWarning.setStatus("current")


class _InputCurrentThLowerCritical_Type(Integer32):
    """Custom type inputCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_InputCurrentThLowerCritical_Type.__name__ = "Integer32"
_InputCurrentThLowerCritical_Object = MibTableColumn
inputCurrentThLowerCritical = _InputCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 7),
    _InputCurrentThLowerCritical_Type()
)
inputCurrentThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputCurrentThLowerCritical.setStatus("current")


class _InputCurrentThUpperWarning_Type(Integer32):
    """Custom type inputCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_InputCurrentThUpperWarning_Type.__name__ = "Integer32"
_InputCurrentThUpperWarning_Object = MibTableColumn
inputCurrentThUpperWarning = _InputCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 8),
    _InputCurrentThUpperWarning_Type()
)
inputCurrentThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputCurrentThUpperWarning.setStatus("current")


class _InputCurrentThUpperCritical_Type(Integer32):
    """Custom type inputCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_InputCurrentThUpperCritical_Type.__name__ = "Integer32"
_InputCurrentThUpperCritical_Object = MibTableColumn
inputCurrentThUpperCritical = _InputCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 9),
    _InputCurrentThUpperCritical_Type()
)
inputCurrentThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputCurrentThUpperCritical.setStatus("current")
_InputCurrentCrestFactor_Type = Integer32
_InputCurrentCrestFactor_Object = MibTableColumn
inputCurrentCrestFactor = _InputCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 10),
    _InputCurrentCrestFactor_Type()
)
inputCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentCrestFactor.setStatus("current")
_InputCurrentPercentLoad_Type = Integer32
_InputCurrentPercentLoad_Object = MibTableColumn
inputCurrentPercentLoad = _InputCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 3, 1, 11),
    _InputCurrentPercentLoad_Type()
)
inputCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrentPercentLoad.setStatus("current")
_InputPowerTable_Object = MibTable
inputPowerTable = _InputPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4)
)
if mibBuilder.loadTexts:
    inputPowerTable.setStatus("current")
_InputPowerEntry_Object = MibTableRow
inputPowerEntry = _InputPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1)
)
inputPowerEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "inputIndex"),
    (0, "EATON-EPDU-MIB", "inputPowerIndex"),
)
if mibBuilder.loadTexts:
    inputPowerEntry.setStatus("current")


class _InputPowerIndex_Type(Integer32):
    """Custom type inputPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_InputPowerIndex_Type.__name__ = "Integer32"
_InputPowerIndex_Object = MibTableColumn
inputPowerIndex = _InputPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 1),
    _InputPowerIndex_Type()
)
inputPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputPowerIndex.setStatus("current")


class _InputPowerMeasType_Type(Integer32):
    """Custom type inputPowerMeasType based on Integer32"""
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
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3),
          ("total", 4),
          ("unknown", 0))
    )


_InputPowerMeasType_Type.__name__ = "Integer32"
_InputPowerMeasType_Object = MibTableColumn
inputPowerMeasType = _InputPowerMeasType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 2),
    _InputPowerMeasType_Type()
)
inputPowerMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPowerMeasType.setStatus("current")
_InputVA_Type = Integer32
_InputVA_Object = MibTableColumn
inputVA = _InputVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 3),
    _InputVA_Type()
)
inputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVA.setStatus("current")
_InputWatts_Type = Integer32
_InputWatts_Object = MibTableColumn
inputWatts = _InputWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 4),
    _InputWatts_Type()
)
inputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputWatts.setStatus("current")


class _InputWh_Type(Unsigned32):
    """Custom type inputWh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_InputWh_Type.__name__ = "Unsigned32"
_InputWh_Object = MibTableColumn
inputWh = _InputWh_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 5),
    _InputWh_Type()
)
inputWh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputWh.setStatus("current")
_InputWhTimer_Type = UnixTimeStamp
_InputWhTimer_Object = MibTableColumn
inputWhTimer = _InputWhTimer_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 6),
    _InputWhTimer_Type()
)
inputWhTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputWhTimer.setStatus("current")
_InputPowerFactor_Type = Integer32
_InputPowerFactor_Object = MibTableColumn
inputPowerFactor = _InputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 7),
    _InputPowerFactor_Type()
)
inputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPowerFactor.setStatus("current")
_InputVAR_Type = Integer32
_InputVAR_Object = MibTableColumn
inputVAR = _InputVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 4, 1, 8),
    _InputVAR_Type()
)
inputVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVAR.setStatus("current")
_InputTotalPowerTable_Object = MibTable
inputTotalPowerTable = _InputTotalPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5)
)
if mibBuilder.loadTexts:
    inputTotalPowerTable.setStatus("current")
_InputTotalPowerEntry_Object = MibTableRow
inputTotalPowerEntry = _InputTotalPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5, 1)
)
inputTotalPowerEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "inputIndex"),
)
if mibBuilder.loadTexts:
    inputTotalPowerEntry.setStatus("current")
_InputTotalVA_Type = Integer32
_InputTotalVA_Object = MibTableColumn
inputTotalVA = _InputTotalVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5, 1, 3),
    _InputTotalVA_Type()
)
inputTotalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalVA.setStatus("current")
_InputTotalWatts_Type = Integer32
_InputTotalWatts_Object = MibTableColumn
inputTotalWatts = _InputTotalWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5, 1, 4),
    _InputTotalWatts_Type()
)
inputTotalWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalWatts.setStatus("current")


class _InputTotalWh_Type(Unsigned32):
    """Custom type inputTotalWh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_InputTotalWh_Type.__name__ = "Unsigned32"
_InputTotalWh_Object = MibTableColumn
inputTotalWh = _InputTotalWh_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5, 1, 5),
    _InputTotalWh_Type()
)
inputTotalWh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputTotalWh.setStatus("current")
_InputTotalWhTimer_Type = UnixTimeStamp
_InputTotalWhTimer_Object = MibTableColumn
inputTotalWhTimer = _InputTotalWhTimer_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5, 1, 6),
    _InputTotalWhTimer_Type()
)
inputTotalWhTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalWhTimer.setStatus("current")
_InputTotalPowerFactor_Type = Integer32
_InputTotalPowerFactor_Object = MibTableColumn
inputTotalPowerFactor = _InputTotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5, 1, 7),
    _InputTotalPowerFactor_Type()
)
inputTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalPowerFactor.setStatus("current")
_InputTotalVAR_Type = Integer32
_InputTotalVAR_Object = MibTableColumn
inputTotalVAR = _InputTotalVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 3, 5, 1, 8),
    _InputTotalVAR_Type()
)
inputTotalVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputTotalVAR.setStatus("current")
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5)
)
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("current")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1, 1)
)
groupEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("current")


class _GroupIndex_Type(Integer32):
    """Custom type groupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_GroupIndex_Type.__name__ = "Integer32"
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    groupIndex.setStatus("current")


class _GroupID_Type(DisplayString):
    """Custom type groupID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_GroupID_Type.__name__ = "DisplayString"
_GroupID_Object = MibTableColumn
groupID = _GroupID_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1, 1, 2),
    _GroupID_Type()
)
groupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupID.setStatus("current")


class _GroupName_Type(OctetString):
    """Custom type groupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_GroupName_Type.__name__ = "OctetString"
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1, 1, 3),
    _GroupName_Type()
)
groupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupName.setStatus("current")


class _GroupType_Type(Integer32):
    """Custom type groupType based on Integer32"""
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
        *(("breaker1pole", 1),
          ("breaker2pole", 2),
          ("breaker3pole", 3),
          ("outletSection", 4),
          ("unknown", 0),
          ("userDefined", 5))
    )


_GroupType_Type.__name__ = "Integer32"
_GroupType_Object = MibTableColumn
groupType = _GroupType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1, 1, 4),
    _GroupType_Type()
)
groupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupType.setStatus("current")


class _GroupBreakerStatus_Type(Integer32):
    """Custom type groupBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("breakerOff", 2),
          ("breakerOn", 1),
          ("notApplicable", 0))
    )


_GroupBreakerStatus_Type.__name__ = "Integer32"
_GroupBreakerStatus_Object = MibTableColumn
groupBreakerStatus = _GroupBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1, 1, 5),
    _GroupBreakerStatus_Type()
)
groupBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupBreakerStatus.setStatus("current")
_GroupChildCount_Type = Integer32
_GroupChildCount_Object = MibTableColumn
groupChildCount = _GroupChildCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 1, 1, 6),
    _GroupChildCount_Type()
)
groupChildCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupChildCount.setStatus("current")
_GroupChildTable_Object = MibTable
groupChildTable = _GroupChildTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 2)
)
if mibBuilder.loadTexts:
    groupChildTable.setStatus("current")
_GroupChildEntry_Object = MibTableRow
groupChildEntry = _GroupChildEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 2, 1)
)
groupChildEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "groupIndex"),
    (0, "EATON-EPDU-MIB", "groupChildIndex"),
)
if mibBuilder.loadTexts:
    groupChildEntry.setStatus("current")


class _GroupChildIndex_Type(Integer32):
    """Custom type groupChildIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_GroupChildIndex_Type.__name__ = "Integer32"
_GroupChildIndex_Object = MibTableColumn
groupChildIndex = _GroupChildIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 2, 1, 1),
    _GroupChildIndex_Type()
)
groupChildIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupChildIndex.setStatus("current")


class _GroupChildType_Type(Integer32):
    """Custom type groupChildType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("custom", 3),
          ("outlet", 4),
          ("section", 2),
          ("unknown", 0))
    )


_GroupChildType_Type.__name__ = "Integer32"
_GroupChildType_Object = MibTableColumn
groupChildType = _GroupChildType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 2, 1, 2),
    _GroupChildType_Type()
)
groupChildType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupChildType.setStatus("current")
_GroupChildOID_Type = ObjectIdentifier
_GroupChildOID_Object = MibTableColumn
groupChildOID = _GroupChildOID_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 2, 1, 3),
    _GroupChildOID_Type()
)
groupChildOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupChildOID.setStatus("current")
_GroupVoltageTable_Object = MibTable
groupVoltageTable = _GroupVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3)
)
if mibBuilder.loadTexts:
    groupVoltageTable.setStatus("current")
_GroupVoltageEntry_Object = MibTableRow
groupVoltageEntry = _GroupVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1)
)
groupVoltageEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupVoltageEntry.setStatus("current")


class _GroupVoltageMeasType_Type(Integer32):
    """Custom type groupVoltageMeasType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("phase1to2", 5),
          ("phase1toN", 2),
          ("phase2to3", 6),
          ("phase2toN", 3),
          ("phase3to1", 7),
          ("phase3toN", 4),
          ("singlePhase", 1),
          ("unknown", 0))
    )


_GroupVoltageMeasType_Type.__name__ = "Integer32"
_GroupVoltageMeasType_Object = MibTableColumn
groupVoltageMeasType = _GroupVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1, 2),
    _GroupVoltageMeasType_Type()
)
groupVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupVoltageMeasType.setStatus("current")
_GroupVoltage_Type = Integer32
_GroupVoltage_Object = MibTableColumn
groupVoltage = _GroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1, 3),
    _GroupVoltage_Type()
)
groupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupVoltage.setStatus("current")


class _GroupVoltageThStatus_Type(Integer32):
    """Custom type groupVoltageThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_GroupVoltageThStatus_Type.__name__ = "Integer32"
_GroupVoltageThStatus_Object = MibTableColumn
groupVoltageThStatus = _GroupVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1, 4),
    _GroupVoltageThStatus_Type()
)
groupVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupVoltageThStatus.setStatus("current")


class _GroupVoltageThLowerWarning_Type(Integer32):
    """Custom type groupVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_GroupVoltageThLowerWarning_Type.__name__ = "Integer32"
_GroupVoltageThLowerWarning_Object = MibTableColumn
groupVoltageThLowerWarning = _GroupVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1, 5),
    _GroupVoltageThLowerWarning_Type()
)
groupVoltageThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupVoltageThLowerWarning.setStatus("current")


class _GroupVoltageThLowerCritical_Type(Integer32):
    """Custom type groupVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_GroupVoltageThLowerCritical_Type.__name__ = "Integer32"
_GroupVoltageThLowerCritical_Object = MibTableColumn
groupVoltageThLowerCritical = _GroupVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1, 6),
    _GroupVoltageThLowerCritical_Type()
)
groupVoltageThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupVoltageThLowerCritical.setStatus("current")


class _GroupVoltageThUpperWarning_Type(Integer32):
    """Custom type groupVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_GroupVoltageThUpperWarning_Type.__name__ = "Integer32"
_GroupVoltageThUpperWarning_Object = MibTableColumn
groupVoltageThUpperWarning = _GroupVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1, 7),
    _GroupVoltageThUpperWarning_Type()
)
groupVoltageThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupVoltageThUpperWarning.setStatus("current")


class _GroupVoltageThUpperCritical_Type(Integer32):
    """Custom type groupVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_GroupVoltageThUpperCritical_Type.__name__ = "Integer32"
_GroupVoltageThUpperCritical_Object = MibTableColumn
groupVoltageThUpperCritical = _GroupVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 3, 1, 8),
    _GroupVoltageThUpperCritical_Type()
)
groupVoltageThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupVoltageThUpperCritical.setStatus("current")
_GroupCurrentTable_Object = MibTable
groupCurrentTable = _GroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4)
)
if mibBuilder.loadTexts:
    groupCurrentTable.setStatus("current")
_GroupCurrentEntry_Object = MibTableRow
groupCurrentEntry = _GroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1)
)
groupCurrentEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupCurrentEntry.setStatus("current")
_GroupCurrentCapacity_Type = Integer32
_GroupCurrentCapacity_Object = MibTableColumn
groupCurrentCapacity = _GroupCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 2),
    _GroupCurrentCapacity_Type()
)
groupCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrentCapacity.setStatus("current")
_GroupCurrent_Type = Integer32
_GroupCurrent_Object = MibTableColumn
groupCurrent = _GroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 3),
    _GroupCurrent_Type()
)
groupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrent.setStatus("current")


class _GroupCurrentThStatus_Type(Integer32):
    """Custom type groupCurrentThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_GroupCurrentThStatus_Type.__name__ = "Integer32"
_GroupCurrentThStatus_Object = MibTableColumn
groupCurrentThStatus = _GroupCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 4),
    _GroupCurrentThStatus_Type()
)
groupCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrentThStatus.setStatus("current")


class _GroupCurrentThLowerWarning_Type(Integer32):
    """Custom type groupCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_GroupCurrentThLowerWarning_Type.__name__ = "Integer32"
_GroupCurrentThLowerWarning_Object = MibTableColumn
groupCurrentThLowerWarning = _GroupCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 5),
    _GroupCurrentThLowerWarning_Type()
)
groupCurrentThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupCurrentThLowerWarning.setStatus("current")


class _GroupCurrentThLowerCritical_Type(Integer32):
    """Custom type groupCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_GroupCurrentThLowerCritical_Type.__name__ = "Integer32"
_GroupCurrentThLowerCritical_Object = MibTableColumn
groupCurrentThLowerCritical = _GroupCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 6),
    _GroupCurrentThLowerCritical_Type()
)
groupCurrentThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupCurrentThLowerCritical.setStatus("current")


class _GroupCurrentThUpperWarning_Type(Integer32):
    """Custom type groupCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_GroupCurrentThUpperWarning_Type.__name__ = "Integer32"
_GroupCurrentThUpperWarning_Object = MibTableColumn
groupCurrentThUpperWarning = _GroupCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 7),
    _GroupCurrentThUpperWarning_Type()
)
groupCurrentThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupCurrentThUpperWarning.setStatus("current")


class _GroupCurrentThUpperCritical_Type(Integer32):
    """Custom type groupCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_GroupCurrentThUpperCritical_Type.__name__ = "Integer32"
_GroupCurrentThUpperCritical_Object = MibTableColumn
groupCurrentThUpperCritical = _GroupCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 8),
    _GroupCurrentThUpperCritical_Type()
)
groupCurrentThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupCurrentThUpperCritical.setStatus("current")
_GroupCurrentCrestFactor_Type = Integer32
_GroupCurrentCrestFactor_Object = MibTableColumn
groupCurrentCrestFactor = _GroupCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 9),
    _GroupCurrentCrestFactor_Type()
)
groupCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrentCrestFactor.setStatus("current")
_GroupCurrentPercentLoad_Type = Integer32
_GroupCurrentPercentLoad_Object = MibTableColumn
groupCurrentPercentLoad = _GroupCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 4, 1, 10),
    _GroupCurrentPercentLoad_Type()
)
groupCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupCurrentPercentLoad.setStatus("current")
_GroupPowerTable_Object = MibTable
groupPowerTable = _GroupPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5)
)
if mibBuilder.loadTexts:
    groupPowerTable.setStatus("current")
_GroupPowerEntry_Object = MibTableRow
groupPowerEntry = _GroupPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5, 1)
)
groupPowerEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupPowerEntry.setStatus("current")
_GroupVA_Type = Integer32
_GroupVA_Object = MibTableColumn
groupVA = _GroupVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5, 1, 2),
    _GroupVA_Type()
)
groupVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupVA.setStatus("current")
_GroupWatts_Type = Integer32
_GroupWatts_Object = MibTableColumn
groupWatts = _GroupWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5, 1, 3),
    _GroupWatts_Type()
)
groupWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupWatts.setStatus("current")


class _GroupWh_Type(Unsigned32):
    """Custom type groupWh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GroupWh_Type.__name__ = "Unsigned32"
_GroupWh_Object = MibTableColumn
groupWh = _GroupWh_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5, 1, 4),
    _GroupWh_Type()
)
groupWh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupWh.setStatus("current")
_GroupWhTimer_Type = UnixTimeStamp
_GroupWhTimer_Object = MibTableColumn
groupWhTimer = _GroupWhTimer_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5, 1, 5),
    _GroupWhTimer_Type()
)
groupWhTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupWhTimer.setStatus("current")
_GroupPowerFactor_Type = Integer32
_GroupPowerFactor_Object = MibTableColumn
groupPowerFactor = _GroupPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5, 1, 6),
    _GroupPowerFactor_Type()
)
groupPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPowerFactor.setStatus("current")
_GroupVAR_Type = Integer32
_GroupVAR_Object = MibTableColumn
groupVAR = _GroupVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 5, 1, 7),
    _GroupVAR_Type()
)
groupVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupVAR.setStatus("current")
_GroupControlTable_Object = MibTable
groupControlTable = _GroupControlTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 6)
)
if mibBuilder.loadTexts:
    groupControlTable.setStatus("current")
_GroupControlEntry_Object = MibTableRow
groupControlEntry = _GroupControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 6, 1)
)
groupControlEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupControlEntry.setStatus("current")


class _GroupControlStatus_Type(Integer32):
    """Custom type groupControlStatus based on Integer32"""
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
        *(("mixed", 3),
          ("off", 0),
          ("on", 1),
          ("rebooting", 2))
    )


_GroupControlStatus_Type.__name__ = "Integer32"
_GroupControlStatus_Object = MibTableColumn
groupControlStatus = _GroupControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 6, 1, 2),
    _GroupControlStatus_Type()
)
groupControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupControlStatus.setStatus("current")


class _GroupControlOffCmd_Type(Integer32):
    """Custom type groupControlOffCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_GroupControlOffCmd_Type.__name__ = "Integer32"
_GroupControlOffCmd_Object = MibTableColumn
groupControlOffCmd = _GroupControlOffCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 6, 1, 3),
    _GroupControlOffCmd_Type()
)
groupControlOffCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupControlOffCmd.setStatus("current")


class _GroupControl0nCmd_Type(Integer32):
    """Custom type groupControl0nCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_GroupControl0nCmd_Type.__name__ = "Integer32"
_GroupControl0nCmd_Object = MibTableColumn
groupControl0nCmd = _GroupControl0nCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 6, 1, 4),
    _GroupControl0nCmd_Type()
)
groupControl0nCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupControl0nCmd.setStatus("current")


class _GroupControlRebootCmd_Type(Integer32):
    """Custom type groupControlRebootCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 0),
    )


_GroupControlRebootCmd_Type.__name__ = "Integer32"
_GroupControlRebootCmd_Object = MibTableColumn
groupControlRebootCmd = _GroupControlRebootCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 5, 6, 1, 5),
    _GroupControlRebootCmd_Type()
)
groupControlRebootCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupControlRebootCmd.setStatus("current")
_Outlets_ObjectIdentity = ObjectIdentity
outlets = _Outlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6)
)
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 1)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 1, 1)
)
outletEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 1, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")


class _OutletID_Type(DisplayString):
    """Custom type outletID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_OutletID_Type.__name__ = "DisplayString"
_OutletID_Object = MibTableColumn
outletID = _OutletID_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 1, 1, 2),
    _OutletID_Type()
)
outletID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletID.setStatus("current")


class _OutletName_Type(OctetString):
    """Custom type outletName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_OutletName_Type.__name__ = "OctetString"
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 1, 1, 3),
    _OutletName_Type()
)
outletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletName.setStatus("current")
_OutletParentCount_Type = Integer32
_OutletParentCount_Object = MibTableColumn
outletParentCount = _OutletParentCount_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 1, 1, 4),
    _OutletParentCount_Type()
)
outletParentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletParentCount.setStatus("current")


class _OutletType_Type(Integer32):
    """Custom type outletType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10,
              11,
              12,
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("french", 11),
          ("iecC13", 1),
          ("iecC19", 2),
          ("nema515", 20),
          ("nema51520", 21),
          ("nema520", 22),
          ("nema615", 25),
          ("nema620", 26),
          ("nemaL520", 23),
          ("nemaL530", 24),
          ("nemaL620", 27),
          ("nemaL630", 28),
          ("nemaL715", 29),
          ("rf203p277", 30),
          ("schuko", 12),
          ("uk", 10),
          ("unknown", 0))
    )


_OutletType_Type.__name__ = "Integer32"
_OutletType_Object = MibTableColumn
outletType = _OutletType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 1, 1, 5),
    _OutletType_Type()
)
outletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletType.setStatus("current")
_OutletParentTable_Object = MibTable
outletParentTable = _OutletParentTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 2)
)
if mibBuilder.loadTexts:
    outletParentTable.setStatus("current")
_OutletParentEntry_Object = MibTableRow
outletParentEntry = _OutletParentEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 2, 1)
)
outletParentEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "outletIndex"),
    (0, "EATON-EPDU-MIB", "outletParentIndex"),
)
if mibBuilder.loadTexts:
    outletParentEntry.setStatus("current")


class _OutletParentIndex_Type(Integer32):
    """Custom type outletParentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_OutletParentIndex_Type.__name__ = "Integer32"
_OutletParentIndex_Object = MibTableColumn
outletParentIndex = _OutletParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 2, 1, 1),
    _OutletParentIndex_Type()
)
outletParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletParentIndex.setStatus("current")


class _OutletParentType_Type(Integer32):
    """Custom type outletParentType based on Integer32"""
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
        *(("breaker", 1),
          ("custom", 3),
          ("section", 2),
          ("unknown", 0))
    )


_OutletParentType_Type.__name__ = "Integer32"
_OutletParentType_Object = MibTableColumn
outletParentType = _OutletParentType_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 2, 1, 2),
    _OutletParentType_Type()
)
outletParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletParentType.setStatus("current")
_OutletParentOID_Type = ObjectIdentifier
_OutletParentOID_Object = MibTableColumn
outletParentOID = _OutletParentOID_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 2, 1, 3),
    _OutletParentOID_Type()
)
outletParentOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletParentOID.setStatus("current")
_OutletVoltageTable_Object = MibTable
outletVoltageTable = _OutletVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3)
)
if mibBuilder.loadTexts:
    outletVoltageTable.setStatus("current")
_OutletVoltageEntry_Object = MibTableRow
outletVoltageEntry = _OutletVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3, 1)
)
outletVoltageEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletVoltageEntry.setStatus("current")
_OutletVoltage_Type = Integer32
_OutletVoltage_Object = MibTableColumn
outletVoltage = _OutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3, 1, 2),
    _OutletVoltage_Type()
)
outletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVoltage.setStatus("current")


class _OutletVoltageThStatus_Type(Integer32):
    """Custom type outletVoltageThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_OutletVoltageThStatus_Type.__name__ = "Integer32"
_OutletVoltageThStatus_Object = MibTableColumn
outletVoltageThStatus = _OutletVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3, 1, 3),
    _OutletVoltageThStatus_Type()
)
outletVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVoltageThStatus.setStatus("current")


class _OutletVoltageThLowerWarning_Type(Integer32):
    """Custom type outletVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_OutletVoltageThLowerWarning_Type.__name__ = "Integer32"
_OutletVoltageThLowerWarning_Object = MibTableColumn
outletVoltageThLowerWarning = _OutletVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3, 1, 4),
    _OutletVoltageThLowerWarning_Type()
)
outletVoltageThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletVoltageThLowerWarning.setStatus("current")


class _OutletVoltageThLowerCritical_Type(Integer32):
    """Custom type outletVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_OutletVoltageThLowerCritical_Type.__name__ = "Integer32"
_OutletVoltageThLowerCritical_Object = MibTableColumn
outletVoltageThLowerCritical = _OutletVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3, 1, 5),
    _OutletVoltageThLowerCritical_Type()
)
outletVoltageThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletVoltageThLowerCritical.setStatus("current")


class _OutletVoltageThUpperWarning_Type(Integer32):
    """Custom type outletVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_OutletVoltageThUpperWarning_Type.__name__ = "Integer32"
_OutletVoltageThUpperWarning_Object = MibTableColumn
outletVoltageThUpperWarning = _OutletVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3, 1, 6),
    _OutletVoltageThUpperWarning_Type()
)
outletVoltageThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletVoltageThUpperWarning.setStatus("current")


class _OutletVoltageThUpperCritical_Type(Integer32):
    """Custom type outletVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_OutletVoltageThUpperCritical_Type.__name__ = "Integer32"
_OutletVoltageThUpperCritical_Object = MibTableColumn
outletVoltageThUpperCritical = _OutletVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 3, 1, 7),
    _OutletVoltageThUpperCritical_Type()
)
outletVoltageThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletVoltageThUpperCritical.setStatus("current")
_OutletCurrentTable_Object = MibTable
outletCurrentTable = _OutletCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4)
)
if mibBuilder.loadTexts:
    outletCurrentTable.setStatus("current")
_OutletCurrentEntry_Object = MibTableRow
outletCurrentEntry = _OutletCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1)
)
outletCurrentEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletCurrentEntry.setStatus("current")
_OutletCurrentCapacity_Type = Integer32
_OutletCurrentCapacity_Object = MibTableColumn
outletCurrentCapacity = _OutletCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 2),
    _OutletCurrentCapacity_Type()
)
outletCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrentCapacity.setStatus("current")
_OutletCurrent_Type = Integer32
_OutletCurrent_Object = MibTableColumn
outletCurrent = _OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 3),
    _OutletCurrent_Type()
)
outletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrent.setStatus("current")


class _OutletCurrentThStatus_Type(Integer32):
    """Custom type outletCurrentThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_OutletCurrentThStatus_Type.__name__ = "Integer32"
_OutletCurrentThStatus_Object = MibTableColumn
outletCurrentThStatus = _OutletCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 4),
    _OutletCurrentThStatus_Type()
)
outletCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrentThStatus.setStatus("current")


class _OutletCurrentThLowerWarning_Type(Integer32):
    """Custom type outletCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_OutletCurrentThLowerWarning_Type.__name__ = "Integer32"
_OutletCurrentThLowerWarning_Object = MibTableColumn
outletCurrentThLowerWarning = _OutletCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 5),
    _OutletCurrentThLowerWarning_Type()
)
outletCurrentThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentThLowerWarning.setStatus("current")


class _OutletCurrentThLowerCritical_Type(Integer32):
    """Custom type outletCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_OutletCurrentThLowerCritical_Type.__name__ = "Integer32"
_OutletCurrentThLowerCritical_Object = MibTableColumn
outletCurrentThLowerCritical = _OutletCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 6),
    _OutletCurrentThLowerCritical_Type()
)
outletCurrentThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentThLowerCritical.setStatus("current")


class _OutletCurrentThUpperWarning_Type(Integer32):
    """Custom type outletCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_OutletCurrentThUpperWarning_Type.__name__ = "Integer32"
_OutletCurrentThUpperWarning_Object = MibTableColumn
outletCurrentThUpperWarning = _OutletCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 7),
    _OutletCurrentThUpperWarning_Type()
)
outletCurrentThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentThUpperWarning.setStatus("current")


class _OutletCurrentThUpperCritical_Type(Integer32):
    """Custom type outletCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_OutletCurrentThUpperCritical_Type.__name__ = "Integer32"
_OutletCurrentThUpperCritical_Object = MibTableColumn
outletCurrentThUpperCritical = _OutletCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 8),
    _OutletCurrentThUpperCritical_Type()
)
outletCurrentThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletCurrentThUpperCritical.setStatus("current")
_OutletCurrentCrestFactor_Type = Integer32
_OutletCurrentCrestFactor_Object = MibTableColumn
outletCurrentCrestFactor = _OutletCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 9),
    _OutletCurrentCrestFactor_Type()
)
outletCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrentCrestFactor.setStatus("current")
_OutletCurrentPercentLoad_Type = Integer32
_OutletCurrentPercentLoad_Object = MibTableColumn
outletCurrentPercentLoad = _OutletCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 4, 1, 10),
    _OutletCurrentPercentLoad_Type()
)
outletCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCurrentPercentLoad.setStatus("current")
_OutletPowerTable_Object = MibTable
outletPowerTable = _OutletPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5)
)
if mibBuilder.loadTexts:
    outletPowerTable.setStatus("current")
_OutletPowerEntry_Object = MibTableRow
outletPowerEntry = _OutletPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5, 1)
)
outletPowerEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletPowerEntry.setStatus("current")
_OutletVA_Type = Integer32
_OutletVA_Object = MibTableColumn
outletVA = _OutletVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5, 1, 2),
    _OutletVA_Type()
)
outletVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVA.setStatus("current")
_OutletWatts_Type = Integer32
_OutletWatts_Object = MibTableColumn
outletWatts = _OutletWatts_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5, 1, 3),
    _OutletWatts_Type()
)
outletWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletWatts.setStatus("current")


class _OutletWh_Type(Unsigned32):
    """Custom type outletWh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OutletWh_Type.__name__ = "Unsigned32"
_OutletWh_Object = MibTableColumn
outletWh = _OutletWh_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5, 1, 4),
    _OutletWh_Type()
)
outletWh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletWh.setStatus("current")
_OutletWhTimer_Type = UnixTimeStamp
_OutletWhTimer_Object = MibTableColumn
outletWhTimer = _OutletWhTimer_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5, 1, 5),
    _OutletWhTimer_Type()
)
outletWhTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletWhTimer.setStatus("current")
_OutletPowerFactor_Type = Integer32
_OutletPowerFactor_Object = MibTableColumn
outletPowerFactor = _OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5, 1, 6),
    _OutletPowerFactor_Type()
)
outletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPowerFactor.setStatus("current")
_OutletVAR_Type = Integer32
_OutletVAR_Object = MibTableColumn
outletVAR = _OutletVAR_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 5, 1, 7),
    _OutletVAR_Type()
)
outletVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletVAR.setStatus("current")
_OutletControlTable_Object = MibTable
outletControlTable = _OutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6)
)
if mibBuilder.loadTexts:
    outletControlTable.setStatus("current")
_OutletControlEntry_Object = MibTableRow
outletControlEntry = _OutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1)
)
outletControlEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletControlEntry.setStatus("current")


class _OutletControlStatus_Type(Integer32):
    """Custom type outletControlStatus based on Integer32"""
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
        *(("off", 0),
          ("on", 1),
          ("pendingOff", 2),
          ("pendingOn", 3))
    )


_OutletControlStatus_Type.__name__ = "Integer32"
_OutletControlStatus_Object = MibTableColumn
outletControlStatus = _OutletControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 2),
    _OutletControlStatus_Type()
)
outletControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletControlStatus.setStatus("current")


class _OutletControlOffCmd_Type(Integer32):
    """Custom type outletControlOffCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_OutletControlOffCmd_Type.__name__ = "Integer32"
_OutletControlOffCmd_Object = MibTableColumn
outletControlOffCmd = _OutletControlOffCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 3),
    _OutletControlOffCmd_Type()
)
outletControlOffCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlOffCmd.setStatus("current")


class _OutletControlOnCmd_Type(Integer32):
    """Custom type outletControlOnCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_OutletControlOnCmd_Type.__name__ = "Integer32"
_OutletControlOnCmd_Object = MibTableColumn
outletControlOnCmd = _OutletControlOnCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 4),
    _OutletControlOnCmd_Type()
)
outletControlOnCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlOnCmd.setStatus("current")


class _OutletControlRebootCmd_Type(Integer32):
    """Custom type outletControlRebootCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_OutletControlRebootCmd_Type.__name__ = "Integer32"
_OutletControlRebootCmd_Object = MibTableColumn
outletControlRebootCmd = _OutletControlRebootCmd_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 5),
    _OutletControlRebootCmd_Type()
)
outletControlRebootCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlRebootCmd.setStatus("current")


class _OutletControlPowerOnState_Type(Integer32):
    """Custom type outletControlPowerOnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lastState", 2),
          ("off", 0),
          ("on", 1))
    )


_OutletControlPowerOnState_Type.__name__ = "Integer32"
_OutletControlPowerOnState_Object = MibTableColumn
outletControlPowerOnState = _OutletControlPowerOnState_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 6),
    _OutletControlPowerOnState_Type()
)
outletControlPowerOnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlPowerOnState.setStatus("current")


class _OutletControlSequenceDelay_Type(Integer32):
    """Custom type outletControlSequenceDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_OutletControlSequenceDelay_Type.__name__ = "Integer32"
_OutletControlSequenceDelay_Object = MibTableColumn
outletControlSequenceDelay = _OutletControlSequenceDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 7),
    _OutletControlSequenceDelay_Type()
)
outletControlSequenceDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlSequenceDelay.setStatus("current")


class _OutletControlRebootOffTime_Type(Integer32):
    """Custom type outletControlRebootOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_OutletControlRebootOffTime_Type.__name__ = "Integer32"
_OutletControlRebootOffTime_Object = MibTableColumn
outletControlRebootOffTime = _OutletControlRebootOffTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 8),
    _OutletControlRebootOffTime_Type()
)
outletControlRebootOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlRebootOffTime.setStatus("current")


class _OutletControlSwitchable_Type(Integer32):
    """Custom type outletControlSwitchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSwitchable", 2),
          ("switchable", 1))
    )


_OutletControlSwitchable_Type.__name__ = "Integer32"
_OutletControlSwitchable_Object = MibTableColumn
outletControlSwitchable = _OutletControlSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 9),
    _OutletControlSwitchable_Type()
)
outletControlSwitchable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlSwitchable.setStatus("current")


class _OutletControlShutoffDelay_Type(Integer32):
    """Custom type outletControlShutoffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_OutletControlShutoffDelay_Type.__name__ = "Integer32"
_OutletControlShutoffDelay_Object = MibTableColumn
outletControlShutoffDelay = _OutletControlShutoffDelay_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 6, 6, 1, 10),
    _OutletControlShutoffDelay_Type()
)
outletControlShutoffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletControlShutoffDelay.setStatus("current")
_Environmental_ObjectIdentity = ObjectIdentity
environmental = _Environmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7)
)
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("current")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1)
)
temperatureEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("current")


class _TemperatureIndex_Type(Integer32):
    """Custom type temperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TemperatureIndex_Type.__name__ = "Integer32"
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("current")


class _TemperatureName_Type(OctetString):
    """Custom type temperatureName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TemperatureName_Type.__name__ = "OctetString"
_TemperatureName_Object = MibTableColumn
temperatureName = _TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 2),
    _TemperatureName_Type()
)
temperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureName.setStatus("current")


class _TemperatureProbeStatus_Type(Integer32):
    """Custom type temperatureProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", -1),
          ("connected", 1),
          ("disconnected", 0))
    )


_TemperatureProbeStatus_Type.__name__ = "Integer32"
_TemperatureProbeStatus_Object = MibTableColumn
temperatureProbeStatus = _TemperatureProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 3),
    _TemperatureProbeStatus_Type()
)
temperatureProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureProbeStatus.setStatus("current")
_TemperatureValue_Type = Integer32
_TemperatureValue_Object = MibTableColumn
temperatureValue = _TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 4),
    _TemperatureValue_Type()
)
temperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureValue.setStatus("current")


class _TemperatureThStatus_Type(Integer32):
    """Custom type temperatureThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_TemperatureThStatus_Type.__name__ = "Integer32"
_TemperatureThStatus_Object = MibTableColumn
temperatureThStatus = _TemperatureThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 5),
    _TemperatureThStatus_Type()
)
temperatureThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureThStatus.setStatus("current")


class _TemperatureThLowerWarning_Type(Integer32):
    """Custom type temperatureThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_TemperatureThLowerWarning_Type.__name__ = "Integer32"
_TemperatureThLowerWarning_Object = MibTableColumn
temperatureThLowerWarning = _TemperatureThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 6),
    _TemperatureThLowerWarning_Type()
)
temperatureThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThLowerWarning.setStatus("current")


class _TemperatureThLowerCritical_Type(Integer32):
    """Custom type temperatureThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_TemperatureThLowerCritical_Type.__name__ = "Integer32"
_TemperatureThLowerCritical_Object = MibTableColumn
temperatureThLowerCritical = _TemperatureThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 7),
    _TemperatureThLowerCritical_Type()
)
temperatureThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThLowerCritical.setStatus("current")


class _TemperatureThUpperWarning_Type(Integer32):
    """Custom type temperatureThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_TemperatureThUpperWarning_Type.__name__ = "Integer32"
_TemperatureThUpperWarning_Object = MibTableColumn
temperatureThUpperWarning = _TemperatureThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 8),
    _TemperatureThUpperWarning_Type()
)
temperatureThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThUpperWarning.setStatus("current")


class _TemperatureThUpperCritical_Type(Integer32):
    """Custom type temperatureThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_TemperatureThUpperCritical_Type.__name__ = "Integer32"
_TemperatureThUpperCritical_Object = MibTableColumn
temperatureThUpperCritical = _TemperatureThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 1, 1, 9),
    _TemperatureThUpperCritical_Type()
)
temperatureThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureThUpperCritical.setStatus("current")
_HumidityTable_Object = MibTable
humidityTable = _HumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2)
)
if mibBuilder.loadTexts:
    humidityTable.setStatus("current")
_HumidityEntry_Object = MibTableRow
humidityEntry = _HumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1)
)
humidityEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "humidityIndex"),
)
if mibBuilder.loadTexts:
    humidityEntry.setStatus("current")


class _HumidityIndex_Type(Integer32):
    """Custom type humidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HumidityIndex_Type.__name__ = "Integer32"
_HumidityIndex_Object = MibTableColumn
humidityIndex = _HumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 1),
    _HumidityIndex_Type()
)
humidityIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    humidityIndex.setStatus("current")


class _HumidityName_Type(OctetString):
    """Custom type humidityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HumidityName_Type.__name__ = "OctetString"
_HumidityName_Object = MibTableColumn
humidityName = _HumidityName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 2),
    _HumidityName_Type()
)
humidityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityName.setStatus("current")


class _HumidityProbeStatus_Type(Integer32):
    """Custom type humidityProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", -1),
          ("connected", 1),
          ("disconnected", 0))
    )


_HumidityProbeStatus_Type.__name__ = "Integer32"
_HumidityProbeStatus_Object = MibTableColumn
humidityProbeStatus = _HumidityProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 3),
    _HumidityProbeStatus_Type()
)
humidityProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityProbeStatus.setStatus("current")
_HumidityValue_Type = Integer32
_HumidityValue_Object = MibTableColumn
humidityValue = _HumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 4),
    _HumidityValue_Type()
)
humidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityValue.setStatus("current")


class _HumidityThStatus_Type(Integer32):
    """Custom type humidityThStatus based on Integer32"""
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
        *(("good", 0),
          ("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 2),
          ("lowWarning", 1))
    )


_HumidityThStatus_Type.__name__ = "Integer32"
_HumidityThStatus_Object = MibTableColumn
humidityThStatus = _HumidityThStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 5),
    _HumidityThStatus_Type()
)
humidityThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityThStatus.setStatus("current")


class _HumidityThLowerWarning_Type(Integer32):
    """Custom type humidityThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_HumidityThLowerWarning_Type.__name__ = "Integer32"
_HumidityThLowerWarning_Object = MibTableColumn
humidityThLowerWarning = _HumidityThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 6),
    _HumidityThLowerWarning_Type()
)
humidityThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThLowerWarning.setStatus("current")


class _HumidityThLowerCritical_Type(Integer32):
    """Custom type humidityThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_HumidityThLowerCritical_Type.__name__ = "Integer32"
_HumidityThLowerCritical_Object = MibTableColumn
humidityThLowerCritical = _HumidityThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 7),
    _HumidityThLowerCritical_Type()
)
humidityThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThLowerCritical.setStatus("current")


class _HumidityThUpperWarning_Type(Integer32):
    """Custom type humidityThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_HumidityThUpperWarning_Type.__name__ = "Integer32"
_HumidityThUpperWarning_Object = MibTableColumn
humidityThUpperWarning = _HumidityThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 8),
    _HumidityThUpperWarning_Type()
)
humidityThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThUpperWarning.setStatus("current")


class _HumidityThUpperCritical_Type(Integer32):
    """Custom type humidityThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_HumidityThUpperCritical_Type.__name__ = "Integer32"
_HumidityThUpperCritical_Object = MibTableColumn
humidityThUpperCritical = _HumidityThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 2, 1, 9),
    _HumidityThUpperCritical_Type()
)
humidityThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityThUpperCritical.setStatus("current")
_ContactTable_Object = MibTable
contactTable = _ContactTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 3)
)
if mibBuilder.loadTexts:
    contactTable.setStatus("current")
_ContactEntry_Object = MibTableRow
contactEntry = _ContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 3, 1)
)
contactEntry.setIndexNames(
    (0, "EATON-EPDU-MIB", "strappingIndex"),
    (0, "EATON-EPDU-MIB", "contactIndex"),
)
if mibBuilder.loadTexts:
    contactEntry.setStatus("current")


class _ContactIndex_Type(Integer32):
    """Custom type contactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ContactIndex_Type.__name__ = "Integer32"
_ContactIndex_Object = MibTableColumn
contactIndex = _ContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 3, 1, 1),
    _ContactIndex_Type()
)
contactIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    contactIndex.setStatus("current")


class _ContactName_Type(OctetString):
    """Custom type contactName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ContactName_Type.__name__ = "OctetString"
_ContactName_Object = MibTableColumn
contactName = _ContactName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 3, 1, 2),
    _ContactName_Type()
)
contactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactName.setStatus("current")


class _ContactProbeStatus_Type(Integer32):
    """Custom type contactProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", -1),
          ("connected", 1),
          ("disconnected", 0))
    )


_ContactProbeStatus_Type.__name__ = "Integer32"
_ContactProbeStatus_Object = MibTableColumn
contactProbeStatus = _ContactProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 3, 1, 3),
    _ContactProbeStatus_Type()
)
contactProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactProbeStatus.setStatus("current")


class _ContactState_Type(Integer32):
    """Custom type contactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("contactBad", -1),
          ("contactClosed", 1),
          ("contactOpen", 0))
    )


_ContactState_Type.__name__ = "Integer32"
_ContactState_Object = MibTableColumn
contactState = _ContactState_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 7, 3, 1, 4),
    _ContactState_Type()
)
contactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactState.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 25)
)
_ObjectGroups_ObjectIdentity = ObjectIdentity
objectGroups = _ObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 25, 5)
)

# Managed Objects groups

epduRequiredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 25, 5, 1)
)
epduRequiredGroup.setObjects(
      *(("EATON-EPDU-MIB", "unitName"),
        ("EATON-EPDU-MIB", "firmwareVersion"))
)
if mibBuilder.loadTexts:
    epduRequiredGroup.setStatus("current")

epduOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 25, 5, 2)
)
epduOptionalGroup.setObjects(
      *(("EATON-EPDU-MIB", "clockValue"),
        ("EATON-EPDU-MIB", "commInterface"),
        ("EATON-EPDU-MIB", "communicationStatus"),
        ("EATON-EPDU-MIB", "contactCount"),
        ("EATON-EPDU-MIB", "contactIndex"),
        ("EATON-EPDU-MIB", "contactName"),
        ("EATON-EPDU-MIB", "contactProbeStatus"),
        ("EATON-EPDU-MIB", "contactState"),
        ("EATON-EPDU-MIB", "groupChildCount"),
        ("EATON-EPDU-MIB", "groupChildOID"),
        ("EATON-EPDU-MIB", "groupChildType"),
        ("EATON-EPDU-MIB", "groupControl0nCmd"),
        ("EATON-EPDU-MIB", "groupControlOffCmd"),
        ("EATON-EPDU-MIB", "groupControlRebootCmd"),
        ("EATON-EPDU-MIB", "groupControlStatus"),
        ("EATON-EPDU-MIB", "groupCount"),
        ("EATON-EPDU-MIB", "groupCurrent"),
        ("EATON-EPDU-MIB", "groupCurrentCapacity"),
        ("EATON-EPDU-MIB", "groupCurrentCrestFactor"),
        ("EATON-EPDU-MIB", "groupCurrentPercentLoad"),
        ("EATON-EPDU-MIB", "groupCurrentThLowerCritical"),
        ("EATON-EPDU-MIB", "groupCurrentThLowerWarning"),
        ("EATON-EPDU-MIB", "groupCurrentThStatus"),
        ("EATON-EPDU-MIB", "groupCurrentThUpperCritical"),
        ("EATON-EPDU-MIB", "groupCurrentThUpperWarning"),
        ("EATON-EPDU-MIB", "groupID"),
        ("EATON-EPDU-MIB", "groupIndex"),
        ("EATON-EPDU-MIB", "groupName"),
        ("EATON-EPDU-MIB", "groupBreakerStatus"),
        ("EATON-EPDU-MIB", "groupPowerFactor"),
        ("EATON-EPDU-MIB", "groupType"),
        ("EATON-EPDU-MIB", "groupVA"),
        ("EATON-EPDU-MIB", "groupVAR"),
        ("EATON-EPDU-MIB", "groupVoltage"),
        ("EATON-EPDU-MIB", "groupVoltageMeasType"),
        ("EATON-EPDU-MIB", "groupVoltageThLowerCritical"),
        ("EATON-EPDU-MIB", "groupVoltageThLowerWarning"),
        ("EATON-EPDU-MIB", "groupVoltageThStatus"),
        ("EATON-EPDU-MIB", "groupVoltageThUpperCritical"),
        ("EATON-EPDU-MIB", "groupVoltageThUpperWarning"),
        ("EATON-EPDU-MIB", "groupWatts"),
        ("EATON-EPDU-MIB", "groupWh"),
        ("EATON-EPDU-MIB", "groupWhTimer"),
        ("EATON-EPDU-MIB", "humidityCount"),
        ("EATON-EPDU-MIB", "humidityIndex"),
        ("EATON-EPDU-MIB", "humidityName"),
        ("EATON-EPDU-MIB", "humidityProbeStatus"),
        ("EATON-EPDU-MIB", "humidityThLowerCritical"),
        ("EATON-EPDU-MIB", "humidityThLowerWarning"),
        ("EATON-EPDU-MIB", "humidityThStatus"),
        ("EATON-EPDU-MIB", "humidityThUpperCritical"),
        ("EATON-EPDU-MIB", "humidityThUpperWarning"),
        ("EATON-EPDU-MIB", "humidityValue"),
        ("EATON-EPDU-MIB", "inputCount"),
        ("EATON-EPDU-MIB", "inputCurrent"),
        ("EATON-EPDU-MIB", "inputCurrentCapacity"),
        ("EATON-EPDU-MIB", "inputCurrentCount"),
        ("EATON-EPDU-MIB", "inputCurrentCrestFactor"),
        ("EATON-EPDU-MIB", "inputCurrentIndex"),
        ("EATON-EPDU-MIB", "inputCurrentMeasType"),
        ("EATON-EPDU-MIB", "inputCurrentPercentLoad"),
        ("EATON-EPDU-MIB", "inputCurrentThLowerCritical"),
        ("EATON-EPDU-MIB", "inputCurrentThLowerWarning"),
        ("EATON-EPDU-MIB", "inputCurrentThStatus"),
        ("EATON-EPDU-MIB", "inputCurrentThUpperCritical"),
        ("EATON-EPDU-MIB", "inputCurrentThUpperWarning"),
        ("EATON-EPDU-MIB", "inputFrequency"),
        ("EATON-EPDU-MIB", "inputFrequencyStatus"),
        ("EATON-EPDU-MIB", "inputIndex"),
        ("EATON-EPDU-MIB", "inputPlugType"),
        ("EATON-EPDU-MIB", "inputPowerCount"),
        ("EATON-EPDU-MIB", "inputPowerFactor"),
        ("EATON-EPDU-MIB", "inputPowerMeasType"),
        ("EATON-EPDU-MIB", "inputType"),
        ("EATON-EPDU-MIB", "inputVA"),
        ("EATON-EPDU-MIB", "inputVAR"),
        ("EATON-EPDU-MIB", "inputVoltage"),
        ("EATON-EPDU-MIB", "inputVoltageCount"),
        ("EATON-EPDU-MIB", "inputVoltageIndex"),
        ("EATON-EPDU-MIB", "inputVoltageMeasType"),
        ("EATON-EPDU-MIB", "inputVoltageThLowerCritical"),
        ("EATON-EPDU-MIB", "inputVoltageThLowerWarning"),
        ("EATON-EPDU-MIB", "inputVoltageThStatus"),
        ("EATON-EPDU-MIB", "inputVoltageThUpperCritical"),
        ("EATON-EPDU-MIB", "inputVoltageThUpperWarning"),
        ("EATON-EPDU-MIB", "inputWatts"),
        ("EATON-EPDU-MIB", "inputWh"),
        ("EATON-EPDU-MIB", "inputWhTimer"),
        ("EATON-EPDU-MIB", "inputTotalVA"),
        ("EATON-EPDU-MIB", "inputTotalWatts"),
        ("EATON-EPDU-MIB", "inputTotalWh"),
        ("EATON-EPDU-MIB", "inputTotalWhTimer"),
        ("EATON-EPDU-MIB", "inputTotalPowerFactor"),
        ("EATON-EPDU-MIB", "inputTotalVAR"),
        ("EATON-EPDU-MIB", "internalStatus"),
        ("EATON-EPDU-MIB", "lcdControl"),
        ("EATON-EPDU-MIB", "outletControlSwitchable"),
        ("EATON-EPDU-MIB", "outletControlShutoffDelay"),
        ("EATON-EPDU-MIB", "outletControlOffCmd"),
        ("EATON-EPDU-MIB", "outletControlOnCmd"),
        ("EATON-EPDU-MIB", "outletControlPowerOnState"),
        ("EATON-EPDU-MIB", "outletControlRebootCmd"),
        ("EATON-EPDU-MIB", "outletControlRebootOffTime"),
        ("EATON-EPDU-MIB", "outletControlSequenceDelay"),
        ("EATON-EPDU-MIB", "outletControlStatus"),
        ("EATON-EPDU-MIB", "outletCount"),
        ("EATON-EPDU-MIB", "outletCurrent"),
        ("EATON-EPDU-MIB", "outletCurrentCapacity"),
        ("EATON-EPDU-MIB", "outletCurrentCrestFactor"),
        ("EATON-EPDU-MIB", "outletCurrentPercentLoad"),
        ("EATON-EPDU-MIB", "outletCurrentThLowerCritical"),
        ("EATON-EPDU-MIB", "outletCurrentThLowerWarning"),
        ("EATON-EPDU-MIB", "outletCurrentThStatus"),
        ("EATON-EPDU-MIB", "outletCurrentThUpperCritical"),
        ("EATON-EPDU-MIB", "outletCurrentThUpperWarning"),
        ("EATON-EPDU-MIB", "outletID"),
        ("EATON-EPDU-MIB", "outletIndex"),
        ("EATON-EPDU-MIB", "outletName"),
        ("EATON-EPDU-MIB", "outletParentCount"),
        ("EATON-EPDU-MIB", "outletParentOID"),
        ("EATON-EPDU-MIB", "outletParentType"),
        ("EATON-EPDU-MIB", "outletPowerFactor"),
        ("EATON-EPDU-MIB", "outletType"),
        ("EATON-EPDU-MIB", "outletVA"),
        ("EATON-EPDU-MIB", "outletVAR"),
        ("EATON-EPDU-MIB", "outletVoltage"),
        ("EATON-EPDU-MIB", "outletVoltageThLowerCritical"),
        ("EATON-EPDU-MIB", "outletVoltageThLowerWarning"),
        ("EATON-EPDU-MIB", "outletVoltageThStatus"),
        ("EATON-EPDU-MIB", "outletVoltageThUpperCritical"),
        ("EATON-EPDU-MIB", "outletVoltageThUpperWarning"),
        ("EATON-EPDU-MIB", "outletWatts"),
        ("EATON-EPDU-MIB", "outletWh"),
        ("EATON-EPDU-MIB", "outletWhTimer"),
        ("EATON-EPDU-MIB", "partNumber"),
        ("EATON-EPDU-MIB", "productName"),
        ("EATON-EPDU-MIB", "serialNumber"),
        ("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "strappingStatus"),
        ("EATON-EPDU-MIB", "temperatureCount"),
        ("EATON-EPDU-MIB", "temperatureIndex"),
        ("EATON-EPDU-MIB", "temperatureName"),
        ("EATON-EPDU-MIB", "temperatureProbeStatus"),
        ("EATON-EPDU-MIB", "temperatureScale"),
        ("EATON-EPDU-MIB", "unitType"),
        ("EATON-EPDU-MIB", "temperatureThLowerCritical"),
        ("EATON-EPDU-MIB", "temperatureThLowerWarning"),
        ("EATON-EPDU-MIB", "temperatureThStatus"),
        ("EATON-EPDU-MIB", "temperatureThUpperCritical"),
        ("EATON-EPDU-MIB", "temperatureThUpperWarning"),
        ("EATON-EPDU-MIB", "temperatureValue"),
        ("EATON-EPDU-MIB", "unitControlOffCmd"),
        ("EATON-EPDU-MIB", "unitControlOnCmd"),
        ("EATON-EPDU-MIB", "unitName"),
        ("EATON-EPDU-MIB", "unitsPresent"),
        ("EATON-EPDU-MIB", "userName"))
)
if mibBuilder.loadTexts:
    epduOptionalGroup.setStatus("current")


# Notification objects

notifyUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 1)
)
notifyUserLogin.setObjects(
      *(("EATON-EPDU-MIB", "userName"),
        ("EATON-EPDU-MIB", "commInterface"))
)
if mibBuilder.loadTexts:
    notifyUserLogin.setStatus(
        "current"
    )

notifyUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 2)
)
notifyUserLogout.setObjects(
      *(("EATON-EPDU-MIB", "userName"),
        ("EATON-EPDU-MIB", "commInterface"))
)
if mibBuilder.loadTexts:
    notifyUserLogout.setStatus(
        "current"
    )

notifyFailedLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 3)
)
notifyFailedLogin.setObjects(
      *(("EATON-EPDU-MIB", "userName"),
        ("EATON-EPDU-MIB", "commInterface"))
)
if mibBuilder.loadTexts:
    notifyFailedLogin.setStatus(
        "current"
    )

notifyBootUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 4)
)
notifyBootUp.setObjects(
    ("EATON-EPDU-MIB", "strappingIndex")
)
if mibBuilder.loadTexts:
    notifyBootUp.setStatus(
        "current"
    )

notifyInputVoltageThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 11)
)
notifyInputVoltageThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "inputIndex"),
        ("EATON-EPDU-MIB", "inputVoltageIndex"),
        ("EATON-EPDU-MIB", "inputVoltage"),
        ("EATON-EPDU-MIB", "inputVoltageThStatus"))
)
if mibBuilder.loadTexts:
    notifyInputVoltageThStatus.setStatus(
        "current"
    )

notifyInputCurrentThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 12)
)
notifyInputCurrentThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "inputIndex"),
        ("EATON-EPDU-MIB", "inputCurrentIndex"),
        ("EATON-EPDU-MIB", "inputCurrent"),
        ("EATON-EPDU-MIB", "inputCurrentThStatus"))
)
if mibBuilder.loadTexts:
    notifyInputCurrentThStatus.setStatus(
        "current"
    )

notifyInputFrequencyStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 13)
)
notifyInputFrequencyStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "inputIndex"),
        ("EATON-EPDU-MIB", "inputFrequency"),
        ("EATON-EPDU-MIB", "inputFrequencyStatus"))
)
if mibBuilder.loadTexts:
    notifyInputFrequencyStatus.setStatus(
        "current"
    )

notifyGroupVoltageThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 21)
)
notifyGroupVoltageThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "groupIndex"),
        ("EATON-EPDU-MIB", "groupVoltage"),
        ("EATON-EPDU-MIB", "groupVoltageThStatus"))
)
if mibBuilder.loadTexts:
    notifyGroupVoltageThStatus.setStatus(
        "current"
    )

notifyGroupCurrentThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 22)
)
notifyGroupCurrentThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "groupIndex"),
        ("EATON-EPDU-MIB", "groupCurrent"),
        ("EATON-EPDU-MIB", "groupCurrentThStatus"))
)
if mibBuilder.loadTexts:
    notifyGroupCurrentThStatus.setStatus(
        "current"
    )

notifyGroupBreakerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 23)
)
notifyGroupBreakerStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "groupIndex"),
        ("EATON-EPDU-MIB", "groupBreakerStatus"))
)
if mibBuilder.loadTexts:
    notifyGroupBreakerStatus.setStatus(
        "current"
    )

notifyOutletVoltageThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 31)
)
notifyOutletVoltageThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "outletIndex"),
        ("EATON-EPDU-MIB", "outletVoltage"),
        ("EATON-EPDU-MIB", "outletVoltageThStatus"))
)
if mibBuilder.loadTexts:
    notifyOutletVoltageThStatus.setStatus(
        "current"
    )

notifyOutletCurrentThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 32)
)
notifyOutletCurrentThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "outletIndex"),
        ("EATON-EPDU-MIB", "outletCurrent"),
        ("EATON-EPDU-MIB", "outletCurrentThStatus"))
)
if mibBuilder.loadTexts:
    notifyOutletCurrentThStatus.setStatus(
        "current"
    )

notifyOutletControlStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 33)
)
notifyOutletControlStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "outletIndex"),
        ("EATON-EPDU-MIB", "outletControlStatus"))
)
if mibBuilder.loadTexts:
    notifyOutletControlStatus.setStatus(
        "current"
    )

notifyTemperatureThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 41)
)
notifyTemperatureThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "temperatureIndex"),
        ("EATON-EPDU-MIB", "temperatureValue"),
        ("EATON-EPDU-MIB", "temperatureThStatus"))
)
if mibBuilder.loadTexts:
    notifyTemperatureThStatus.setStatus(
        "current"
    )

notifyHumidityThStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 42)
)
notifyHumidityThStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "humidityIndex"),
        ("EATON-EPDU-MIB", "humidityValue"),
        ("EATON-EPDU-MIB", "humidityThStatus"))
)
if mibBuilder.loadTexts:
    notifyHumidityThStatus.setStatus(
        "current"
    )

notifyContactState = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 43)
)
notifyContactState.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "contactIndex"),
        ("EATON-EPDU-MIB", "contactState"))
)
if mibBuilder.loadTexts:
    notifyContactState.setStatus(
        "current"
    )

notifyProbeStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 44)
)
notifyProbeStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "temperatureIndex"),
        ("EATON-EPDU-MIB", "temperatureProbeStatus"))
)
if mibBuilder.loadTexts:
    notifyProbeStatus.setStatus(
        "current"
    )

notifyCommunicationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 51)
)
notifyCommunicationStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "communicationStatus"))
)
if mibBuilder.loadTexts:
    notifyCommunicationStatus.setStatus(
        "current"
    )

notifyInternalStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 52)
)
notifyInternalStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "internalStatus"))
)
if mibBuilder.loadTexts:
    notifyInternalStatus.setStatus(
        "current"
    )

notifyTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 53)
)
if mibBuilder.loadTexts:
    notifyTest.setStatus(
        "current"
    )

notifyStrappingStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 0, 54)
)
notifyStrappingStatus.setObjects(
      *(("EATON-EPDU-MIB", "strappingIndex"),
        ("EATON-EPDU-MIB", "strappingStatus"))
)
if mibBuilder.loadTexts:
    notifyStrappingStatus.setStatus(
        "current"
    )


# Notifications groups

epduNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 25, 5, 3)
)
epduNotifyGroup.setObjects(
      *(("EATON-EPDU-MIB", "notifyBootUp"),
        ("EATON-EPDU-MIB", "notifyCommunicationStatus"),
        ("EATON-EPDU-MIB", "notifyContactState"),
        ("EATON-EPDU-MIB", "notifyFailedLogin"),
        ("EATON-EPDU-MIB", "notifyGroupCurrentThStatus"),
        ("EATON-EPDU-MIB", "notifyGroupVoltageThStatus"),
        ("EATON-EPDU-MIB", "notifyGroupBreakerStatus"),
        ("EATON-EPDU-MIB", "notifyHumidityThStatus"),
        ("EATON-EPDU-MIB", "notifyInputCurrentThStatus"),
        ("EATON-EPDU-MIB", "notifyInputFrequencyStatus"),
        ("EATON-EPDU-MIB", "notifyInputVoltageThStatus"),
        ("EATON-EPDU-MIB", "notifyInternalStatus"),
        ("EATON-EPDU-MIB", "notifyOutletControlStatus"),
        ("EATON-EPDU-MIB", "notifyOutletCurrentThStatus"),
        ("EATON-EPDU-MIB", "notifyOutletVoltageThStatus"),
        ("EATON-EPDU-MIB", "notifyProbeStatus"),
        ("EATON-EPDU-MIB", "notifyStrappingStatus"),
        ("EATON-EPDU-MIB", "notifyTemperatureThStatus"),
        ("EATON-EPDU-MIB", "notifyTest"),
        ("EATON-EPDU-MIB", "notifyUserLogin"),
        ("EATON-EPDU-MIB", "notifyUserLogout"))
)
if mibBuilder.loadTexts:
    epduNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eatonEpduCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 7, 25, 1)
)
if mibBuilder.loadTexts:
    eatonEpduCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-EPDU-MIB",
    **{"UnixTimeStamp": UnixTimeStamp,
       "eatonEpdu": eatonEpdu,
       "notifications": notifications,
       "notifyUserLogin": notifyUserLogin,
       "notifyUserLogout": notifyUserLogout,
       "notifyFailedLogin": notifyFailedLogin,
       "notifyBootUp": notifyBootUp,
       "notifyInputVoltageThStatus": notifyInputVoltageThStatus,
       "notifyInputCurrentThStatus": notifyInputCurrentThStatus,
       "notifyInputFrequencyStatus": notifyInputFrequencyStatus,
       "notifyGroupVoltageThStatus": notifyGroupVoltageThStatus,
       "notifyGroupCurrentThStatus": notifyGroupCurrentThStatus,
       "notifyGroupBreakerStatus": notifyGroupBreakerStatus,
       "notifyOutletVoltageThStatus": notifyOutletVoltageThStatus,
       "notifyOutletCurrentThStatus": notifyOutletCurrentThStatus,
       "notifyOutletControlStatus": notifyOutletControlStatus,
       "notifyTemperatureThStatus": notifyTemperatureThStatus,
       "notifyHumidityThStatus": notifyHumidityThStatus,
       "notifyContactState": notifyContactState,
       "notifyProbeStatus": notifyProbeStatus,
       "notifyCommunicationStatus": notifyCommunicationStatus,
       "notifyInternalStatus": notifyInternalStatus,
       "notifyTest": notifyTest,
       "notifyStrappingStatus": notifyStrappingStatus,
       "units": units,
       "unitsPresent": unitsPresent,
       "unitTable": unitTable,
       "unitEntry": unitEntry,
       "strappingIndex": strappingIndex,
       "productName": productName,
       "partNumber": partNumber,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "unitName": unitName,
       "lcdControl": lcdControl,
       "clockValue": clockValue,
       "temperatureScale": temperatureScale,
       "unitType": unitType,
       "inputCount": inputCount,
       "groupCount": groupCount,
       "outletCount": outletCount,
       "temperatureCount": temperatureCount,
       "humidityCount": humidityCount,
       "contactCount": contactCount,
       "communicationStatus": communicationStatus,
       "internalStatus": internalStatus,
       "strappingStatus": strappingStatus,
       "userName": userName,
       "commInterface": commInterface,
       "unitControlTable": unitControlTable,
       "unitControlEntry": unitControlEntry,
       "unitControlOffCmd": unitControlOffCmd,
       "unitControlOnCmd": unitControlOnCmd,
       "inputs": inputs,
       "inputTable": inputTable,
       "inputEntry": inputEntry,
       "inputIndex": inputIndex,
       "inputType": inputType,
       "inputFrequency": inputFrequency,
       "inputFrequencyStatus": inputFrequencyStatus,
       "inputVoltageCount": inputVoltageCount,
       "inputCurrentCount": inputCurrentCount,
       "inputPowerCount": inputPowerCount,
       "inputPlugType": inputPlugType,
       "inputVoltageTable": inputVoltageTable,
       "inputVoltageEntry": inputVoltageEntry,
       "inputVoltageIndex": inputVoltageIndex,
       "inputVoltageMeasType": inputVoltageMeasType,
       "inputVoltage": inputVoltage,
       "inputVoltageThStatus": inputVoltageThStatus,
       "inputVoltageThLowerWarning": inputVoltageThLowerWarning,
       "inputVoltageThLowerCritical": inputVoltageThLowerCritical,
       "inputVoltageThUpperWarning": inputVoltageThUpperWarning,
       "inputVoltageThUpperCritical": inputVoltageThUpperCritical,
       "inputCurrentTable": inputCurrentTable,
       "inputCurrentEntry": inputCurrentEntry,
       "inputCurrentIndex": inputCurrentIndex,
       "inputCurrentMeasType": inputCurrentMeasType,
       "inputCurrentCapacity": inputCurrentCapacity,
       "inputCurrent": inputCurrent,
       "inputCurrentThStatus": inputCurrentThStatus,
       "inputCurrentThLowerWarning": inputCurrentThLowerWarning,
       "inputCurrentThLowerCritical": inputCurrentThLowerCritical,
       "inputCurrentThUpperWarning": inputCurrentThUpperWarning,
       "inputCurrentThUpperCritical": inputCurrentThUpperCritical,
       "inputCurrentCrestFactor": inputCurrentCrestFactor,
       "inputCurrentPercentLoad": inputCurrentPercentLoad,
       "inputPowerTable": inputPowerTable,
       "inputPowerEntry": inputPowerEntry,
       "inputPowerIndex": inputPowerIndex,
       "inputPowerMeasType": inputPowerMeasType,
       "inputVA": inputVA,
       "inputWatts": inputWatts,
       "inputWh": inputWh,
       "inputWhTimer": inputWhTimer,
       "inputPowerFactor": inputPowerFactor,
       "inputVAR": inputVAR,
       "inputTotalPowerTable": inputTotalPowerTable,
       "inputTotalPowerEntry": inputTotalPowerEntry,
       "inputTotalVA": inputTotalVA,
       "inputTotalWatts": inputTotalWatts,
       "inputTotalWh": inputTotalWh,
       "inputTotalWhTimer": inputTotalWhTimer,
       "inputTotalPowerFactor": inputTotalPowerFactor,
       "inputTotalVAR": inputTotalVAR,
       "groups": groups,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupIndex": groupIndex,
       "groupID": groupID,
       "groupName": groupName,
       "groupType": groupType,
       "groupBreakerStatus": groupBreakerStatus,
       "groupChildCount": groupChildCount,
       "groupChildTable": groupChildTable,
       "groupChildEntry": groupChildEntry,
       "groupChildIndex": groupChildIndex,
       "groupChildType": groupChildType,
       "groupChildOID": groupChildOID,
       "groupVoltageTable": groupVoltageTable,
       "groupVoltageEntry": groupVoltageEntry,
       "groupVoltageMeasType": groupVoltageMeasType,
       "groupVoltage": groupVoltage,
       "groupVoltageThStatus": groupVoltageThStatus,
       "groupVoltageThLowerWarning": groupVoltageThLowerWarning,
       "groupVoltageThLowerCritical": groupVoltageThLowerCritical,
       "groupVoltageThUpperWarning": groupVoltageThUpperWarning,
       "groupVoltageThUpperCritical": groupVoltageThUpperCritical,
       "groupCurrentTable": groupCurrentTable,
       "groupCurrentEntry": groupCurrentEntry,
       "groupCurrentCapacity": groupCurrentCapacity,
       "groupCurrent": groupCurrent,
       "groupCurrentThStatus": groupCurrentThStatus,
       "groupCurrentThLowerWarning": groupCurrentThLowerWarning,
       "groupCurrentThLowerCritical": groupCurrentThLowerCritical,
       "groupCurrentThUpperWarning": groupCurrentThUpperWarning,
       "groupCurrentThUpperCritical": groupCurrentThUpperCritical,
       "groupCurrentCrestFactor": groupCurrentCrestFactor,
       "groupCurrentPercentLoad": groupCurrentPercentLoad,
       "groupPowerTable": groupPowerTable,
       "groupPowerEntry": groupPowerEntry,
       "groupVA": groupVA,
       "groupWatts": groupWatts,
       "groupWh": groupWh,
       "groupWhTimer": groupWhTimer,
       "groupPowerFactor": groupPowerFactor,
       "groupVAR": groupVAR,
       "groupControlTable": groupControlTable,
       "groupControlEntry": groupControlEntry,
       "groupControlStatus": groupControlStatus,
       "groupControlOffCmd": groupControlOffCmd,
       "groupControl0nCmd": groupControl0nCmd,
       "groupControlRebootCmd": groupControlRebootCmd,
       "outlets": outlets,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletID": outletID,
       "outletName": outletName,
       "outletParentCount": outletParentCount,
       "outletType": outletType,
       "outletParentTable": outletParentTable,
       "outletParentEntry": outletParentEntry,
       "outletParentIndex": outletParentIndex,
       "outletParentType": outletParentType,
       "outletParentOID": outletParentOID,
       "outletVoltageTable": outletVoltageTable,
       "outletVoltageEntry": outletVoltageEntry,
       "outletVoltage": outletVoltage,
       "outletVoltageThStatus": outletVoltageThStatus,
       "outletVoltageThLowerWarning": outletVoltageThLowerWarning,
       "outletVoltageThLowerCritical": outletVoltageThLowerCritical,
       "outletVoltageThUpperWarning": outletVoltageThUpperWarning,
       "outletVoltageThUpperCritical": outletVoltageThUpperCritical,
       "outletCurrentTable": outletCurrentTable,
       "outletCurrentEntry": outletCurrentEntry,
       "outletCurrentCapacity": outletCurrentCapacity,
       "outletCurrent": outletCurrent,
       "outletCurrentThStatus": outletCurrentThStatus,
       "outletCurrentThLowerWarning": outletCurrentThLowerWarning,
       "outletCurrentThLowerCritical": outletCurrentThLowerCritical,
       "outletCurrentThUpperWarning": outletCurrentThUpperWarning,
       "outletCurrentThUpperCritical": outletCurrentThUpperCritical,
       "outletCurrentCrestFactor": outletCurrentCrestFactor,
       "outletCurrentPercentLoad": outletCurrentPercentLoad,
       "outletPowerTable": outletPowerTable,
       "outletPowerEntry": outletPowerEntry,
       "outletVA": outletVA,
       "outletWatts": outletWatts,
       "outletWh": outletWh,
       "outletWhTimer": outletWhTimer,
       "outletPowerFactor": outletPowerFactor,
       "outletVAR": outletVAR,
       "outletControlTable": outletControlTable,
       "outletControlEntry": outletControlEntry,
       "outletControlStatus": outletControlStatus,
       "outletControlOffCmd": outletControlOffCmd,
       "outletControlOnCmd": outletControlOnCmd,
       "outletControlRebootCmd": outletControlRebootCmd,
       "outletControlPowerOnState": outletControlPowerOnState,
       "outletControlSequenceDelay": outletControlSequenceDelay,
       "outletControlRebootOffTime": outletControlRebootOffTime,
       "outletControlSwitchable": outletControlSwitchable,
       "outletControlShutoffDelay": outletControlShutoffDelay,
       "environmental": environmental,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureIndex": temperatureIndex,
       "temperatureName": temperatureName,
       "temperatureProbeStatus": temperatureProbeStatus,
       "temperatureValue": temperatureValue,
       "temperatureThStatus": temperatureThStatus,
       "temperatureThLowerWarning": temperatureThLowerWarning,
       "temperatureThLowerCritical": temperatureThLowerCritical,
       "temperatureThUpperWarning": temperatureThUpperWarning,
       "temperatureThUpperCritical": temperatureThUpperCritical,
       "humidityTable": humidityTable,
       "humidityEntry": humidityEntry,
       "humidityIndex": humidityIndex,
       "humidityName": humidityName,
       "humidityProbeStatus": humidityProbeStatus,
       "humidityValue": humidityValue,
       "humidityThStatus": humidityThStatus,
       "humidityThLowerWarning": humidityThLowerWarning,
       "humidityThLowerCritical": humidityThLowerCritical,
       "humidityThUpperWarning": humidityThUpperWarning,
       "humidityThUpperCritical": humidityThUpperCritical,
       "contactTable": contactTable,
       "contactEntry": contactEntry,
       "contactIndex": contactIndex,
       "contactName": contactName,
       "contactProbeStatus": contactProbeStatus,
       "contactState": contactState,
       "conformance": conformance,
       "eatonEpduCompliances": eatonEpduCompliances,
       "objectGroups": objectGroups,
       "epduRequiredGroup": epduRequiredGroup,
       "epduOptionalGroup": epduOptionalGroup,
       "epduNotifyGroup": epduNotifyGroup}
)
