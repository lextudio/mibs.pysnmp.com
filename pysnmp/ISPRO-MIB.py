# SNMP MIB module (ISPRO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISPRO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:00 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class IsproEnuEnable(Integer32):
    """Custom type IsproEnuEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )





class IsproEnuReset(Integer32):
    """Custom type IsproEnuReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("reset", 1))
    )





class IsproEnuRestart(Integer32):
    """Custom type IsproEnuRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("restart", 1))
    )





class IsproEnuSeverity(Integer32):
    """Custom type IsproEnuSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("information", 1),
          ("severe", 3),
          ("warning", 2))
    )





class IsproEnuAccess(Integer32):
    """Custom type IsproEnuAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("readonly", 2),
          ("readwrite", 3))
    )





class IsproEnuTempUnit(Integer32):
    """Custom type IsproEnuTempUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )





class IsproEnuDateFormat(Integer32):
    """Custom type IsproEnuDateFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dd-mm-yyyy", 1),
          ("mm-dd-yyyy", 2))
    )





class IsproEnuTimeZone(Integer32):
    """Custom type IsproEnuTimeZone based on Integer32"""
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
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("gMT-0000", 14),
          ("gMT-0100", 13),
          ("gMT-0200", 12),
          ("gMT-0300", 11),
          ("gMT-0330", 10),
          ("gMT-0400", 9),
          ("gMT-0500", 8),
          ("gMT-0600", 7),
          ("gMT-0700", 6),
          ("gMT-0800", 5),
          ("gMT-0900", 4),
          ("gMT-1000", 3),
          ("gMT-1100", 2),
          ("gMT-1200", 1),
          ("gMT0100", 15),
          ("gMT0200", 16),
          ("gMT0300", 17),
          ("gMT0330", 18),
          ("gMT0400", 19),
          ("gMT0500", 20),
          ("gMT0530", 21),
          ("gMT0600", 22),
          ("gMT0700", 23),
          ("gMT0800", 24),
          ("gMT0900", 25),
          ("gMT1000", 26),
          ("gMT1100", 27),
          ("gMT1200", 28))
    )





class IsproEnuSensorType(Integer32):
    """Custom type IsproEnuSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sensorHT", 2),
          ("unknown", 1))
    )





class IsproEnuThresholdStatus(Integer32):
    """Custom type IsproEnuThresholdStatus based on Integer32"""
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
        *(("above-high-critical", 7),
          ("above-high-warning", 6),
          ("below-low-critical", 5),
          ("below-low-warning", 4),
          ("disable", 2),
          ("normal", 3),
          ("unknown", 1))
    )





class IsproEnuDigitalStatus(Integer32):
    """Custom type IsproEnuDigitalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )





class IsproTriggerStatus(Integer32):
    """Custom type IsproTriggerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("triggered", 2))
    )





class IsproEnuSensorState(Integer32):
    """Custom type IsproEnuSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disable", 2))
    )





class IsproEnuTempCalibration(Integer32):
    """Custom type IsproEnuTempCalibration based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("temperatureDecrease0Point5", 8),
          ("temperatureDecrease1Point0", 9),
          ("temperatureDecrease1Point5", 10),
          ("temperatureDecrease2Point0", 11),
          ("temperatureDecrease2Point5", 12),
          ("temperatureDecrease3Point0", 13),
          ("temperatureIncrease0Point0", 1),
          ("temperatureIncrease0Point5", 2),
          ("temperatureIncrease1Point0", 3),
          ("temperatureIncrease1Point5", 4),
          ("temperatureIncrease2Point0", 5),
          ("temperatureIncrease2Point5", 6),
          ("temperatureIncrease3Point0", 7))
    )





class IsproEnuHumidityCalibration(Integer32):
    """Custom type IsproEnuHumidityCalibration based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("humidityDecrease0Point5", 8),
          ("humidityDecrease1Point0", 9),
          ("humidityDecrease1Point5", 10),
          ("humidityDecrease2Point0", 11),
          ("humidityDecrease2Point5", 12),
          ("humidityDecrease3Point0", 13),
          ("humidityIncrease0Point0", 1),
          ("humidityIncrease0Point5", 2),
          ("humidityIncrease1Point0", 3),
          ("humidityIncrease1Point5", 4),
          ("humidityIncrease2Point0", 5),
          ("humidityIncrease2Point5", 6),
          ("humidityIncrease3Point0", 7))
    )





class IsproEnuAlarmState(Integer32):
    """Custom type IsproEnuAlarmState based on Integer32"""
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
          ("normalClose", 3),
          ("normalOpen", 2))
    )





class IsproEnuOnOff(Integer32):
    """Custom type IsproEnuOnOff based on Integer32"""
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





class IsproEnuTurnOnOff(Integer32):
    """Custom type IsproEnuTurnOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("turnOff", 2),
          ("turnOn", 1))
    )





class IsproEnuPresent(Integer32):
    """Custom type IsproEnuPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("present", 1))
    )





class IsproEnuDO(Integer32):
    """Custom type IsproEnuDO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("digitalOutput1", 2),
          ("digitalOutput2", 3),
          ("none", 1))
    )





class IsproEnuHighLow(Integer32):
    """Custom type IsproEnuHighLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )





class IsproLogType(Integer32):
    """Custom type IsproLogType based on Integer32"""
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
        *(("deviceEventLog", 3),
          ("extendedLog", 2),
          ("historyLog", 1),
          ("systemEventLog", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Jacarta_ObjectIdentity = ObjectIdentity
jacarta = _Jacarta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1)
)
_WebAppliance_ObjectIdentity = ObjectIdentity
webAppliance = _WebAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3)
)
_Ispro_ObjectIdentity = ObjectIdentity
ispro = _Ispro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2)
)
_IsObjects_ObjectIdentity = ObjectIdentity
isObjects = _IsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1)
)
_IsIdent_ObjectIdentity = ObjectIdentity
isIdent = _IsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 1)
)


class _IsIdentManufacturer_Type(DisplayString):
    """Custom type isIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IsIdentManufacturer_Type.__name__ = "DisplayString"
_IsIdentManufacturer_Object = MibScalar
isIdentManufacturer = _IsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 1, 1),
    _IsIdentManufacturer_Type()
)
isIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isIdentManufacturer.setStatus("mandatory")


class _IsIdentModel_Type(DisplayString):
    """Custom type isIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IsIdentModel_Type.__name__ = "DisplayString"
_IsIdentModel_Object = MibScalar
isIdentModel = _IsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 1, 2),
    _IsIdentModel_Type()
)
isIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isIdentModel.setStatus("mandatory")


class _IsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type isIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_IsIdentAgentSoftwareVersion_Object = MibScalar
isIdentAgentSoftwareVersion = _IsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 1, 3),
    _IsIdentAgentSoftwareVersion_Type()
)
isIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isIdentAgentSoftwareVersion.setStatus("mandatory")


class _IsIdentName_Type(DisplayString):
    """Custom type isIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IsIdentName_Type.__name__ = "DisplayString"
_IsIdentName_Object = MibScalar
isIdentName = _IsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 1, 4),
    _IsIdentName_Type()
)
isIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isIdentName.setStatus("mandatory")
_IsConfig_ObjectIdentity = ObjectIdentity
isConfig = _IsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2)
)


class _IsConfigMibVersion_Type(DisplayString):
    """Custom type isConfigMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IsConfigMibVersion_Type.__name__ = "DisplayString"
_IsConfigMibVersion_Object = MibScalar
isConfigMibVersion = _IsConfigMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 1),
    _IsConfigMibVersion_Type()
)
isConfigMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isConfigMibVersion.setStatus("mandatory")
_IsConfigNetwork_ObjectIdentity = ObjectIdentity
isConfigNetwork = _IsConfigNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 2)
)
_IsConfigIpAddress_Type = IpAddress
_IsConfigIpAddress_Object = MibScalar
isConfigIpAddress = _IsConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 2, 1),
    _IsConfigIpAddress_Type()
)
isConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigIpAddress.setStatus("mandatory")
_IsConfigGateway_Type = IpAddress
_IsConfigGateway_Object = MibScalar
isConfigGateway = _IsConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 2, 2),
    _IsConfigGateway_Type()
)
isConfigGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigGateway.setStatus("mandatory")
_IsConfigSubnetMask_Type = IpAddress
_IsConfigSubnetMask_Object = MibScalar
isConfigSubnetMask = _IsConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 2, 3),
    _IsConfigSubnetMask_Type()
)
isConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigSubnetMask.setStatus("mandatory")
_IsConfigDateTime_ObjectIdentity = ObjectIdentity
isConfigDateTime = _IsConfigDateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 3)
)


class _IsConfigDate_Type(DisplayString):
    """Custom type isConfigDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IsConfigDate_Type.__name__ = "DisplayString"
_IsConfigDate_Object = MibScalar
isConfigDate = _IsConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 3, 1),
    _IsConfigDate_Type()
)
isConfigDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigDate.setStatus("mandatory")


class _IsConfigTime_Type(DisplayString):
    """Custom type isConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IsConfigTime_Type.__name__ = "DisplayString"
_IsConfigTime_Object = MibScalar
isConfigTime = _IsConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 3, 2),
    _IsConfigTime_Type()
)
isConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTime.setStatus("mandatory")
_IsConfigTimeFromNtp_Type = IsproEnuEnable
_IsConfigTimeFromNtp_Object = MibScalar
isConfigTimeFromNtp = _IsConfigTimeFromNtp_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 3, 3),
    _IsConfigTimeFromNtp_Type()
)
isConfigTimeFromNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTimeFromNtp.setStatus("mandatory")


class _IsConfigNtpIpAddress_Type(DisplayString):
    """Custom type isConfigNtpIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IsConfigNtpIpAddress_Type.__name__ = "DisplayString"
_IsConfigNtpIpAddress_Object = MibScalar
isConfigNtpIpAddress = _IsConfigNtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 3, 4),
    _IsConfigNtpIpAddress_Type()
)
isConfigNtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigNtpIpAddress.setStatus("mandatory")
_IsConfigNtpTimeZone_Type = IsproEnuTimeZone
_IsConfigNtpTimeZone_Object = MibScalar
isConfigNtpTimeZone = _IsConfigNtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 3, 5),
    _IsConfigNtpTimeZone_Type()
)
isConfigNtpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigNtpTimeZone.setStatus("mandatory")
_IsConfigDayLightSaving_Type = IsproEnuEnable
_IsConfigDayLightSaving_Object = MibScalar
isConfigDayLightSaving = _IsConfigDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 3, 6),
    _IsConfigDayLightSaving_Type()
)
isConfigDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigDayLightSaving.setStatus("mandatory")
_IsConfigLog_ObjectIdentity = ObjectIdentity
isConfigLog = _IsConfigLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 4)
)


class _IsConfigHistoryLogFrequency_Type(Integer32):
    """Custom type isConfigHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_IsConfigHistoryLogFrequency_Type.__name__ = "Integer32"
_IsConfigHistoryLogFrequency_Object = MibScalar
isConfigHistoryLogFrequency = _IsConfigHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 4, 1),
    _IsConfigHistoryLogFrequency_Type()
)
isConfigHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigHistoryLogFrequency.setStatus("mandatory")


class _IsConfigExtHistoryLogFrequency_Type(Integer32):
    """Custom type isConfigExtHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 720),
    )


_IsConfigExtHistoryLogFrequency_Type.__name__ = "Integer32"
_IsConfigExtHistoryLogFrequency_Object = MibScalar
isConfigExtHistoryLogFrequency = _IsConfigExtHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 4, 2),
    _IsConfigExtHistoryLogFrequency_Type()
)
isConfigExtHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigExtHistoryLogFrequency.setStatus("mandatory")
_IsConfigConfigurationLog_Type = IsproEnuEnable
_IsConfigConfigurationLog_Object = MibScalar
isConfigConfigurationLog = _IsConfigConfigurationLog_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 4, 3),
    _IsConfigConfigurationLog_Type()
)
isConfigConfigurationLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigConfigurationLog.setStatus("mandatory")
_IsConfigLogType_Type = IsproLogType
_IsConfigLogType_Object = MibScalar
isConfigLogType = _IsConfigLogType_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 4, 4),
    _IsConfigLogType_Type()
)
isConfigLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isConfigLogType.setStatus("mandatory")
_IsConfigDhcpState_Type = IsproEnuEnable
_IsConfigDhcpState_Object = MibScalar
isConfigDhcpState = _IsConfigDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 5),
    _IsConfigDhcpState_Type()
)
isConfigDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigDhcpState.setStatus("mandatory")
_IsConfigPingState_Type = IsproEnuEnable
_IsConfigPingState_Object = MibScalar
isConfigPingState = _IsConfigPingState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 6),
    _IsConfigPingState_Type()
)
isConfigPingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigPingState.setStatus("mandatory")
_IsConfigTftpState_Type = IsproEnuEnable
_IsConfigTftpState_Object = MibScalar
isConfigTftpState = _IsConfigTftpState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 7),
    _IsConfigTftpState_Type()
)
isConfigTftpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTftpState.setStatus("mandatory")
_IsConfigTelnet_ObjectIdentity = ObjectIdentity
isConfigTelnet = _IsConfigTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 8)
)
_IsConfigTelnetState_Type = IsproEnuEnable
_IsConfigTelnetState_Object = MibScalar
isConfigTelnetState = _IsConfigTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 8, 1),
    _IsConfigTelnetState_Type()
)
isConfigTelnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTelnetState.setStatus("mandatory")


class _IsConfigTelnetPortNumber_Type(Integer32):
    """Custom type isConfigTelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsConfigTelnetPortNumber_Type.__name__ = "Integer32"
_IsConfigTelnetPortNumber_Object = MibScalar
isConfigTelnetPortNumber = _IsConfigTelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 8, 2),
    _IsConfigTelnetPortNumber_Type()
)
isConfigTelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTelnetPortNumber.setStatus("mandatory")
_IsConfigHttp_ObjectIdentity = ObjectIdentity
isConfigHttp = _IsConfigHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 9)
)
_IsConfigHttpState_Type = IsproEnuEnable
_IsConfigHttpState_Object = MibScalar
isConfigHttpState = _IsConfigHttpState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 9, 1),
    _IsConfigHttpState_Type()
)
isConfigHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigHttpState.setStatus("mandatory")


class _IsConfigHttpPortNumber_Type(Integer32):
    """Custom type isConfigHttpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsConfigHttpPortNumber_Type.__name__ = "Integer32"
_IsConfigHttpPortNumber_Object = MibScalar
isConfigHttpPortNumber = _IsConfigHttpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 9, 2),
    _IsConfigHttpPortNumber_Type()
)
isConfigHttpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigHttpPortNumber.setStatus("mandatory")
_IsConfigHttpSecurity_Type = IsproEnuEnable
_IsConfigHttpSecurity_Object = MibScalar
isConfigHttpSecurity = _IsConfigHttpSecurity_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 9, 3),
    _IsConfigHttpSecurity_Type()
)
isConfigHttpSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigHttpSecurity.setStatus("mandatory")
_IsConfigSnmp_ObjectIdentity = ObjectIdentity
isConfigSnmp = _IsConfigSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 10)
)
_IsConfigSnmpState_Type = IsproEnuEnable
_IsConfigSnmpState_Object = MibScalar
isConfigSnmpState = _IsConfigSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 10, 1),
    _IsConfigSnmpState_Type()
)
isConfigSnmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigSnmpState.setStatus("mandatory")


class _IsConfigSnmpPortNumber_Type(Integer32):
    """Custom type isConfigSnmpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsConfigSnmpPortNumber_Type.__name__ = "Integer32"
_IsConfigSnmpPortNumber_Object = MibScalar
isConfigSnmpPortNumber = _IsConfigSnmpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 10, 2),
    _IsConfigSnmpPortNumber_Type()
)
isConfigSnmpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigSnmpPortNumber.setStatus("mandatory")
_IsConfigControl_ObjectIdentity = ObjectIdentity
isConfigControl = _IsConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 11)
)
_IsConfigResetToDefault_Type = IsproEnuReset
_IsConfigResetToDefault_Object = MibScalar
isConfigResetToDefault = _IsConfigResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 11, 1),
    _IsConfigResetToDefault_Type()
)
isConfigResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigResetToDefault.setStatus("mandatory")
_IsConfigRestart_Type = IsproEnuRestart
_IsConfigRestart_Object = MibScalar
isConfigRestart = _IsConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 11, 2),
    _IsConfigRestart_Type()
)
isConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigRestart.setStatus("mandatory")
_IsConfigTrap_ObjectIdentity = ObjectIdentity
isConfigTrap = _IsConfigTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 12)
)


class _IsConfigTrapRetryCount_Type(Integer32):
    """Custom type isConfigTrapRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsConfigTrapRetryCount_Type.__name__ = "Integer32"
_IsConfigTrapRetryCount_Object = MibScalar
isConfigTrapRetryCount = _IsConfigTrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 12, 1),
    _IsConfigTrapRetryCount_Type()
)
isConfigTrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTrapRetryCount.setStatus("mandatory")


class _IsConfigTrapRetryTime_Type(Integer32):
    """Custom type isConfigTrapRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsConfigTrapRetryTime_Type.__name__ = "Integer32"
_IsConfigTrapRetryTime_Object = MibScalar
isConfigTrapRetryTime = _IsConfigTrapRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 12, 2),
    _IsConfigTrapRetryTime_Type()
)
isConfigTrapRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTrapRetryTime.setStatus("mandatory")


class _IsConfigTrapAckSignature_Type(Integer32):
    """Custom type isConfigTrapAckSignature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsConfigTrapAckSignature_Type.__name__ = "Integer32"
_IsConfigTrapAckSignature_Object = MibScalar
isConfigTrapAckSignature = _IsConfigTrapAckSignature_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 12, 3),
    _IsConfigTrapAckSignature_Type()
)
isConfigTrapAckSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTrapAckSignature.setStatus("mandatory")


class _IsConfigRefreshRate_Type(Integer32):
    """Custom type isConfigRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IsConfigRefreshRate_Type.__name__ = "Integer32"
_IsConfigRefreshRate_Object = MibScalar
isConfigRefreshRate = _IsConfigRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 13),
    _IsConfigRefreshRate_Type()
)
isConfigRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigRefreshRate.setStatus("mandatory")
_IsConfigTrapReceiverTable_Object = MibTable
isConfigTrapReceiverTable = _IsConfigTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    isConfigTrapReceiverTable.setStatus("mandatory")
_IsConfigTrapReceiverEntry_Object = MibTableRow
isConfigTrapReceiverEntry = _IsConfigTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 14, 1)
)
isConfigTrapReceiverEntry.setIndexNames(
    (0, "ISPRO-MIB", "isReceiverIndex"),
)
if mibBuilder.loadTexts:
    isConfigTrapReceiverEntry.setStatus("mandatory")


class _IsReceiverIndex_Type(Integer32):
    """Custom type isReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IsReceiverIndex_Type.__name__ = "Integer32"
_IsReceiverIndex_Object = MibTableColumn
isReceiverIndex = _IsReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 14, 1, 1),
    _IsReceiverIndex_Type()
)
isReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isReceiverIndex.setStatus("mandatory")
_IsReceiverAddr_Type = IpAddress
_IsReceiverAddr_Object = MibTableColumn
isReceiverAddr = _IsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 14, 1, 2),
    _IsReceiverAddr_Type()
)
isReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isReceiverAddr.setStatus("mandatory")


class _IsReceiverCommunityString_Type(DisplayString):
    """Custom type isReceiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_IsReceiverCommunityString_Type.__name__ = "DisplayString"
_IsReceiverCommunityString_Object = MibTableColumn
isReceiverCommunityString = _IsReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 14, 1, 3),
    _IsReceiverCommunityString_Type()
)
isReceiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isReceiverCommunityString.setStatus("mandatory")
_IsReceiverSeverityLevel_Type = IsproEnuSeverity
_IsReceiverSeverityLevel_Object = MibTableColumn
isReceiverSeverityLevel = _IsReceiverSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 14, 1, 4),
    _IsReceiverSeverityLevel_Type()
)
isReceiverSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isReceiverSeverityLevel.setStatus("mandatory")


class _IsReceiverDescription_Type(DisplayString):
    """Custom type isReceiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_IsReceiverDescription_Type.__name__ = "DisplayString"
_IsReceiverDescription_Object = MibTableColumn
isReceiverDescription = _IsReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 14, 1, 5),
    _IsReceiverDescription_Type()
)
isReceiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isReceiverDescription.setStatus("mandatory")
_IsConfigAccessControlTable_Object = MibTable
isConfigAccessControlTable = _IsConfigAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    isConfigAccessControlTable.setStatus("mandatory")
_IsConfigAccessControlEntry_Object = MibTableRow
isConfigAccessControlEntry = _IsConfigAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 15, 1)
)
isConfigAccessControlEntry.setIndexNames(
    (0, "ISPRO-MIB", "isAccessIndex"),
)
if mibBuilder.loadTexts:
    isConfigAccessControlEntry.setStatus("mandatory")


class _IsAccessIndex_Type(Integer32):
    """Custom type isAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IsAccessIndex_Type.__name__ = "Integer32"
_IsAccessIndex_Object = MibTableColumn
isAccessIndex = _IsAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 15, 1, 1),
    _IsAccessIndex_Type()
)
isAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isAccessIndex.setStatus("mandatory")
_IsAccessControlAddr_Type = IpAddress
_IsAccessControlAddr_Object = MibTableColumn
isAccessControlAddr = _IsAccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 15, 1, 2),
    _IsAccessControlAddr_Type()
)
isAccessControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isAccessControlAddr.setStatus("mandatory")


class _IsAccessCommunityString_Type(DisplayString):
    """Custom type isAccessCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsAccessCommunityString_Type.__name__ = "DisplayString"
_IsAccessCommunityString_Object = MibTableColumn
isAccessCommunityString = _IsAccessCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 15, 1, 3),
    _IsAccessCommunityString_Type()
)
isAccessCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isAccessCommunityString.setStatus("mandatory")
_IsAccessControlMode_Type = IsproEnuAccess
_IsAccessControlMode_Object = MibTableColumn
isAccessControlMode = _IsAccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 15, 1, 4),
    _IsAccessControlMode_Type()
)
isAccessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isAccessControlMode.setStatus("mandatory")


class _IsAccessAccount_Type(DisplayString):
    """Custom type isAccessAccount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IsAccessAccount_Type.__name__ = "DisplayString"
_IsAccessAccount_Object = MibTableColumn
isAccessAccount = _IsAccessAccount_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 15, 1, 5),
    _IsAccessAccount_Type()
)
isAccessAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isAccessAccount.setStatus("mandatory")
_IsConfigTemperatureUnit_Type = IsproEnuTempUnit
_IsConfigTemperatureUnit_Object = MibScalar
isConfigTemperatureUnit = _IsConfigTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 16),
    _IsConfigTemperatureUnit_Type()
)
isConfigTemperatureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigTemperatureUnit.setStatus("mandatory")
_IsConfigDateFormat_Type = IsproEnuDateFormat
_IsConfigDateFormat_Object = MibScalar
isConfigDateFormat = _IsConfigDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 2, 17),
    _IsConfigDateFormat_Type()
)
isConfigDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isConfigDateFormat.setStatus("mandatory")
_IsDevice_ObjectIdentity = ObjectIdentity
isDevice = _IsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3)
)
_IsDeviceMonitor_ObjectIdentity = ObjectIdentity
isDeviceMonitor = _IsDeviceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1)
)
_IsDeviceMonitorTemperatureTable_Object = MibTable
isDeviceMonitorTemperatureTable = _IsDeviceMonitorTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    isDeviceMonitorTemperatureTable.setStatus("mandatory")
_IsDeviceMonitorTemperatureEntry_Object = MibTableRow
isDeviceMonitorTemperatureEntry = _IsDeviceMonitorTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 1, 1)
)
isDeviceMonitorTemperatureEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceMonitorTemperatureIndex"),
)
if mibBuilder.loadTexts:
    isDeviceMonitorTemperatureEntry.setStatus("mandatory")


class _IsDeviceMonitorTemperatureIndex_Type(Integer32):
    """Custom type isDeviceMonitorTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IsDeviceMonitorTemperatureIndex_Type.__name__ = "Integer32"
_IsDeviceMonitorTemperatureIndex_Object = MibTableColumn
isDeviceMonitorTemperatureIndex = _IsDeviceMonitorTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 1, 1, 1),
    _IsDeviceMonitorTemperatureIndex_Type()
)
isDeviceMonitorTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorTemperatureIndex.setStatus("mandatory")


class _IsDeviceMonitorTemperatureName_Type(DisplayString):
    """Custom type isDeviceMonitorTemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsDeviceMonitorTemperatureName_Type.__name__ = "DisplayString"
_IsDeviceMonitorTemperatureName_Object = MibTableColumn
isDeviceMonitorTemperatureName = _IsDeviceMonitorTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 1, 1, 2),
    _IsDeviceMonitorTemperatureName_Type()
)
isDeviceMonitorTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorTemperatureName.setStatus("mandatory")
_IsDeviceMonitorTemperature_Type = Integer32
_IsDeviceMonitorTemperature_Object = MibTableColumn
isDeviceMonitorTemperature = _IsDeviceMonitorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 1, 1, 3),
    _IsDeviceMonitorTemperature_Type()
)
isDeviceMonitorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorTemperature.setStatus("mandatory")
_IsDeviceMonitorTemperatureAlarm_Type = IsproEnuThresholdStatus
_IsDeviceMonitorTemperatureAlarm_Object = MibTableColumn
isDeviceMonitorTemperatureAlarm = _IsDeviceMonitorTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 1, 1, 4),
    _IsDeviceMonitorTemperatureAlarm_Type()
)
isDeviceMonitorTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorTemperatureAlarm.setStatus("mandatory")
_IsDeviceMonitorHumidityTable_Object = MibTable
isDeviceMonitorHumidityTable = _IsDeviceMonitorHumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    isDeviceMonitorHumidityTable.setStatus("mandatory")
_IsDeviceMonitorHumidityEntry_Object = MibTableRow
isDeviceMonitorHumidityEntry = _IsDeviceMonitorHumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 2, 1)
)
isDeviceMonitorHumidityEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceMonitorHumidityIndex"),
)
if mibBuilder.loadTexts:
    isDeviceMonitorHumidityEntry.setStatus("mandatory")


class _IsDeviceMonitorHumidityIndex_Type(Integer32):
    """Custom type isDeviceMonitorHumidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IsDeviceMonitorHumidityIndex_Type.__name__ = "Integer32"
_IsDeviceMonitorHumidityIndex_Object = MibTableColumn
isDeviceMonitorHumidityIndex = _IsDeviceMonitorHumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 2, 1, 1),
    _IsDeviceMonitorHumidityIndex_Type()
)
isDeviceMonitorHumidityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorHumidityIndex.setStatus("mandatory")


class _IsDeviceMonitorHumidityName_Type(DisplayString):
    """Custom type isDeviceMonitorHumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsDeviceMonitorHumidityName_Type.__name__ = "DisplayString"
_IsDeviceMonitorHumidityName_Object = MibTableColumn
isDeviceMonitorHumidityName = _IsDeviceMonitorHumidityName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 2, 1, 2),
    _IsDeviceMonitorHumidityName_Type()
)
isDeviceMonitorHumidityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorHumidityName.setStatus("mandatory")
_IsDeviceMonitorHumidity_Type = Integer32
_IsDeviceMonitorHumidity_Object = MibTableColumn
isDeviceMonitorHumidity = _IsDeviceMonitorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 2, 1, 3),
    _IsDeviceMonitorHumidity_Type()
)
isDeviceMonitorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorHumidity.setStatus("mandatory")
_IsDeviceMonitorHumidityAlarm_Type = IsproEnuThresholdStatus
_IsDeviceMonitorHumidityAlarm_Object = MibTableColumn
isDeviceMonitorHumidityAlarm = _IsDeviceMonitorHumidityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 2, 1, 4),
    _IsDeviceMonitorHumidityAlarm_Type()
)
isDeviceMonitorHumidityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorHumidityAlarm.setStatus("mandatory")
_IsDeviceMonitorDigitalInTable_Object = MibTable
isDeviceMonitorDigitalInTable = _IsDeviceMonitorDigitalInTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    isDeviceMonitorDigitalInTable.setStatus("mandatory")
_IsDeviceMonitorDigitalInEntry_Object = MibTableRow
isDeviceMonitorDigitalInEntry = _IsDeviceMonitorDigitalInEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 3, 1)
)
isDeviceMonitorDigitalInEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceMonitorDigitalInIndex"),
)
if mibBuilder.loadTexts:
    isDeviceMonitorDigitalInEntry.setStatus("mandatory")


class _IsDeviceMonitorDigitalInIndex_Type(Integer32):
    """Custom type isDeviceMonitorDigitalInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IsDeviceMonitorDigitalInIndex_Type.__name__ = "Integer32"
_IsDeviceMonitorDigitalInIndex_Object = MibTableColumn
isDeviceMonitorDigitalInIndex = _IsDeviceMonitorDigitalInIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 3, 1, 1),
    _IsDeviceMonitorDigitalInIndex_Type()
)
isDeviceMonitorDigitalInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorDigitalInIndex.setStatus("mandatory")


class _IsDeviceMonitorDigitalInName_Type(DisplayString):
    """Custom type isDeviceMonitorDigitalInName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsDeviceMonitorDigitalInName_Type.__name__ = "DisplayString"
_IsDeviceMonitorDigitalInName_Object = MibTableColumn
isDeviceMonitorDigitalInName = _IsDeviceMonitorDigitalInName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 3, 1, 2),
    _IsDeviceMonitorDigitalInName_Type()
)
isDeviceMonitorDigitalInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorDigitalInName.setStatus("mandatory")
_IsDeviceMonitorDigitalIn_Type = IsproEnuDigitalStatus
_IsDeviceMonitorDigitalIn_Object = MibTableColumn
isDeviceMonitorDigitalIn = _IsDeviceMonitorDigitalIn_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 3, 1, 3),
    _IsDeviceMonitorDigitalIn_Type()
)
isDeviceMonitorDigitalIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorDigitalIn.setStatus("mandatory")
_IsDeviceMonitorDigitalInAlarm_Type = IsproTriggerStatus
_IsDeviceMonitorDigitalInAlarm_Object = MibTableColumn
isDeviceMonitorDigitalInAlarm = _IsDeviceMonitorDigitalInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 1, 3, 1, 4),
    _IsDeviceMonitorDigitalInAlarm_Type()
)
isDeviceMonitorDigitalInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceMonitorDigitalInAlarm.setStatus("mandatory")
_IsDeviceConfig_ObjectIdentity = ObjectIdentity
isDeviceConfig = _IsDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2)
)
_IsDeviceConfigTable_Object = MibTable
isDeviceConfigTable = _IsDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    isDeviceConfigTable.setStatus("mandatory")
_IsDeviceConfigEntry_Object = MibTableRow
isDeviceConfigEntry = _IsDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 1, 1)
)
isDeviceConfigEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceConfigIndex"),
)
if mibBuilder.loadTexts:
    isDeviceConfigEntry.setStatus("mandatory")


class _IsDeviceConfigIndex_Type(Integer32):
    """Custom type isDeviceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IsDeviceConfigIndex_Type.__name__ = "Integer32"
_IsDeviceConfigIndex_Object = MibTableColumn
isDeviceConfigIndex = _IsDeviceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 1, 1, 1),
    _IsDeviceConfigIndex_Type()
)
isDeviceConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceConfigIndex.setStatus("mandatory")


class _IsDeviceConfigName_Type(DisplayString):
    """Custom type isDeviceConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsDeviceConfigName_Type.__name__ = "DisplayString"
_IsDeviceConfigName_Object = MibTableColumn
isDeviceConfigName = _IsDeviceConfigName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 1, 1, 2),
    _IsDeviceConfigName_Type()
)
isDeviceConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigName.setStatus("mandatory")
_IsDeviceConfigState_Type = IsproEnuSensorState
_IsDeviceConfigState_Object = MibTableColumn
isDeviceConfigState = _IsDeviceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 1, 1, 3),
    _IsDeviceConfigState_Type()
)
isDeviceConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigState.setStatus("mandatory")
_IsDeviceConfigDisplay_Type = IsproEnuEnable
_IsDeviceConfigDisplay_Object = MibTableColumn
isDeviceConfigDisplay = _IsDeviceConfigDisplay_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 1, 1, 4),
    _IsDeviceConfigDisplay_Type()
)
isDeviceConfigDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigDisplay.setStatus("mandatory")
_IsDeviceConfigTemperatureTable_Object = MibTable
isDeviceConfigTemperatureTable = _IsDeviceConfigTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureTable.setStatus("mandatory")
_IsDeviceConfigTemperatureEntry_Object = MibTableRow
isDeviceConfigTemperatureEntry = _IsDeviceConfigTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1)
)
isDeviceConfigTemperatureEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceConfigTemperatureIndex"),
)
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureEntry.setStatus("mandatory")


class _IsDeviceConfigTemperatureIndex_Type(Integer32):
    """Custom type isDeviceConfigTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IsDeviceConfigTemperatureIndex_Type.__name__ = "Integer32"
_IsDeviceConfigTemperatureIndex_Object = MibTableColumn
isDeviceConfigTemperatureIndex = _IsDeviceConfigTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 1),
    _IsDeviceConfigTemperatureIndex_Type()
)
isDeviceConfigTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureIndex.setStatus("mandatory")


class _IsDeviceConfigTemperatureName_Type(DisplayString):
    """Custom type isDeviceConfigTemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsDeviceConfigTemperatureName_Type.__name__ = "DisplayString"
_IsDeviceConfigTemperatureName_Object = MibTableColumn
isDeviceConfigTemperatureName = _IsDeviceConfigTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 2),
    _IsDeviceConfigTemperatureName_Type()
)
isDeviceConfigTemperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureName.setStatus("mandatory")


class _IsDeviceConfigTemperatureLowWarning_Type(Integer32):
    """Custom type isDeviceConfigTemperatureLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1500, 6500),
    )


_IsDeviceConfigTemperatureLowWarning_Type.__name__ = "Integer32"
_IsDeviceConfigTemperatureLowWarning_Object = MibTableColumn
isDeviceConfigTemperatureLowWarning = _IsDeviceConfigTemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 3),
    _IsDeviceConfigTemperatureLowWarning_Type()
)
isDeviceConfigTemperatureLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureLowWarning.setStatus("mandatory")


class _IsDeviceConfigTemperatureLowCritical_Type(Integer32):
    """Custom type isDeviceConfigTemperatureLowCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1500, 6500),
    )


_IsDeviceConfigTemperatureLowCritical_Type.__name__ = "Integer32"
_IsDeviceConfigTemperatureLowCritical_Object = MibTableColumn
isDeviceConfigTemperatureLowCritical = _IsDeviceConfigTemperatureLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 4),
    _IsDeviceConfigTemperatureLowCritical_Type()
)
isDeviceConfigTemperatureLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureLowCritical.setStatus("mandatory")


class _IsDeviceConfigTemperatureHighWarning_Type(Integer32):
    """Custom type isDeviceConfigTemperatureHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1500, 6500),
    )


_IsDeviceConfigTemperatureHighWarning_Type.__name__ = "Integer32"
_IsDeviceConfigTemperatureHighWarning_Object = MibTableColumn
isDeviceConfigTemperatureHighWarning = _IsDeviceConfigTemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 5),
    _IsDeviceConfigTemperatureHighWarning_Type()
)
isDeviceConfigTemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureHighWarning.setStatus("mandatory")


class _IsDeviceConfigTemperatureHighCritical_Type(Integer32):
    """Custom type isDeviceConfigTemperatureHighCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1500, 6500),
    )


_IsDeviceConfigTemperatureHighCritical_Type.__name__ = "Integer32"
_IsDeviceConfigTemperatureHighCritical_Object = MibTableColumn
isDeviceConfigTemperatureHighCritical = _IsDeviceConfigTemperatureHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 6),
    _IsDeviceConfigTemperatureHighCritical_Type()
)
isDeviceConfigTemperatureHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureHighCritical.setStatus("mandatory")
_IsDeviceConfigTemperatureHysteresis_Type = Integer32
_IsDeviceConfigTemperatureHysteresis_Object = MibTableColumn
isDeviceConfigTemperatureHysteresis = _IsDeviceConfigTemperatureHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 7),
    _IsDeviceConfigTemperatureHysteresis_Type()
)
isDeviceConfigTemperatureHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureHysteresis.setStatus("mandatory")
_IsDeviceConfigTemperatureCalibration_Type = IsproEnuTempCalibration
_IsDeviceConfigTemperatureCalibration_Object = MibTableColumn
isDeviceConfigTemperatureCalibration = _IsDeviceConfigTemperatureCalibration_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 8),
    _IsDeviceConfigTemperatureCalibration_Type()
)
isDeviceConfigTemperatureCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureCalibration.setStatus("mandatory")
_IsDeviceConfigTemperatureLowWarningState_Type = IsproEnuEnable
_IsDeviceConfigTemperatureLowWarningState_Object = MibTableColumn
isDeviceConfigTemperatureLowWarningState = _IsDeviceConfigTemperatureLowWarningState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 9),
    _IsDeviceConfigTemperatureLowWarningState_Type()
)
isDeviceConfigTemperatureLowWarningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureLowWarningState.setStatus("mandatory")
_IsDeviceConfigTemperatureLowCriticalState_Type = IsproEnuEnable
_IsDeviceConfigTemperatureLowCriticalState_Object = MibTableColumn
isDeviceConfigTemperatureLowCriticalState = _IsDeviceConfigTemperatureLowCriticalState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 10),
    _IsDeviceConfigTemperatureLowCriticalState_Type()
)
isDeviceConfigTemperatureLowCriticalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureLowCriticalState.setStatus("mandatory")
_IsDeviceConfigTemperatureHighWarningState_Type = IsproEnuEnable
_IsDeviceConfigTemperatureHighWarningState_Object = MibTableColumn
isDeviceConfigTemperatureHighWarningState = _IsDeviceConfigTemperatureHighWarningState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 11),
    _IsDeviceConfigTemperatureHighWarningState_Type()
)
isDeviceConfigTemperatureHighWarningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureHighWarningState.setStatus("mandatory")
_IsDeviceConfigTemperatureHighCriticalState_Type = IsproEnuEnable
_IsDeviceConfigTemperatureHighCriticalState_Object = MibTableColumn
isDeviceConfigTemperatureHighCriticalState = _IsDeviceConfigTemperatureHighCriticalState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 12),
    _IsDeviceConfigTemperatureHighCriticalState_Type()
)
isDeviceConfigTemperatureHighCriticalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureHighCriticalState.setStatus("mandatory")
_IsDeviceConfigTemperatureEventDO_Type = IsproEnuDO
_IsDeviceConfigTemperatureEventDO_Object = MibTableColumn
isDeviceConfigTemperatureEventDO = _IsDeviceConfigTemperatureEventDO_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 2, 1, 13),
    _IsDeviceConfigTemperatureEventDO_Type()
)
isDeviceConfigTemperatureEventDO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigTemperatureEventDO.setStatus("mandatory")
_IsDeviceConfigHumidityTable_Object = MibTable
isDeviceConfigHumidityTable = _IsDeviceConfigHumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    isDeviceConfigHumidityTable.setStatus("mandatory")
_IsDeviceConfigHumidityEntry_Object = MibTableRow
isDeviceConfigHumidityEntry = _IsDeviceConfigHumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1)
)
isDeviceConfigHumidityEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceConfigHumidityIndex"),
)
if mibBuilder.loadTexts:
    isDeviceConfigHumidityEntry.setStatus("mandatory")


class _IsDeviceConfigHumidityIndex_Type(Integer32):
    """Custom type isDeviceConfigHumidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IsDeviceConfigHumidityIndex_Type.__name__ = "Integer32"
_IsDeviceConfigHumidityIndex_Object = MibTableColumn
isDeviceConfigHumidityIndex = _IsDeviceConfigHumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 1),
    _IsDeviceConfigHumidityIndex_Type()
)
isDeviceConfigHumidityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityIndex.setStatus("mandatory")


class _IsDeviceConfigHumidityName_Type(DisplayString):
    """Custom type isDeviceConfigHumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsDeviceConfigHumidityName_Type.__name__ = "DisplayString"
_IsDeviceConfigHumidityName_Object = MibTableColumn
isDeviceConfigHumidityName = _IsDeviceConfigHumidityName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 2),
    _IsDeviceConfigHumidityName_Type()
)
isDeviceConfigHumidityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityName.setStatus("mandatory")


class _IsDeviceConfigHumidityLowWarning_Type(Integer32):
    """Custom type isDeviceConfigHumidityLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 9500),
    )


_IsDeviceConfigHumidityLowWarning_Type.__name__ = "Integer32"
_IsDeviceConfigHumidityLowWarning_Object = MibTableColumn
isDeviceConfigHumidityLowWarning = _IsDeviceConfigHumidityLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 3),
    _IsDeviceConfigHumidityLowWarning_Type()
)
isDeviceConfigHumidityLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityLowWarning.setStatus("mandatory")


class _IsDeviceConfigHumidityLowCritical_Type(Integer32):
    """Custom type isDeviceConfigHumidityLowCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 9500),
    )


_IsDeviceConfigHumidityLowCritical_Type.__name__ = "Integer32"
_IsDeviceConfigHumidityLowCritical_Object = MibTableColumn
isDeviceConfigHumidityLowCritical = _IsDeviceConfigHumidityLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 4),
    _IsDeviceConfigHumidityLowCritical_Type()
)
isDeviceConfigHumidityLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityLowCritical.setStatus("mandatory")


class _IsDeviceConfigHumidityHighWarning_Type(Integer32):
    """Custom type isDeviceConfigHumidityHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 9500),
    )


_IsDeviceConfigHumidityHighWarning_Type.__name__ = "Integer32"
_IsDeviceConfigHumidityHighWarning_Object = MibTableColumn
isDeviceConfigHumidityHighWarning = _IsDeviceConfigHumidityHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 5),
    _IsDeviceConfigHumidityHighWarning_Type()
)
isDeviceConfigHumidityHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityHighWarning.setStatus("mandatory")


class _IsDeviceConfigHumidityHighCritical_Type(Integer32):
    """Custom type isDeviceConfigHumidityHighCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 9500),
    )


_IsDeviceConfigHumidityHighCritical_Type.__name__ = "Integer32"
_IsDeviceConfigHumidityHighCritical_Object = MibTableColumn
isDeviceConfigHumidityHighCritical = _IsDeviceConfigHumidityHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 6),
    _IsDeviceConfigHumidityHighCritical_Type()
)
isDeviceConfigHumidityHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityHighCritical.setStatus("mandatory")
_IsDeviceConfigHumidityHysteresis_Type = Integer32
_IsDeviceConfigHumidityHysteresis_Object = MibTableColumn
isDeviceConfigHumidityHysteresis = _IsDeviceConfigHumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 7),
    _IsDeviceConfigHumidityHysteresis_Type()
)
isDeviceConfigHumidityHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityHysteresis.setStatus("mandatory")
_IsDeviceConfigHumidityCalibration_Type = IsproEnuHumidityCalibration
_IsDeviceConfigHumidityCalibration_Object = MibTableColumn
isDeviceConfigHumidityCalibration = _IsDeviceConfigHumidityCalibration_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 8),
    _IsDeviceConfigHumidityCalibration_Type()
)
isDeviceConfigHumidityCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityCalibration.setStatus("mandatory")
_IsDeviceConfigHumidityLowWarningState_Type = IsproEnuEnable
_IsDeviceConfigHumidityLowWarningState_Object = MibTableColumn
isDeviceConfigHumidityLowWarningState = _IsDeviceConfigHumidityLowWarningState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 9),
    _IsDeviceConfigHumidityLowWarningState_Type()
)
isDeviceConfigHumidityLowWarningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityLowWarningState.setStatus("mandatory")
_IsDeviceConfigHumidityLowCriticalState_Type = IsproEnuEnable
_IsDeviceConfigHumidityLowCriticalState_Object = MibTableColumn
isDeviceConfigHumidityLowCriticalState = _IsDeviceConfigHumidityLowCriticalState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 10),
    _IsDeviceConfigHumidityLowCriticalState_Type()
)
isDeviceConfigHumidityLowCriticalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityLowCriticalState.setStatus("mandatory")
_IsDeviceConfigHumidityHighWarningState_Type = IsproEnuEnable
_IsDeviceConfigHumidityHighWarningState_Object = MibTableColumn
isDeviceConfigHumidityHighWarningState = _IsDeviceConfigHumidityHighWarningState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 11),
    _IsDeviceConfigHumidityHighWarningState_Type()
)
isDeviceConfigHumidityHighWarningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityHighWarningState.setStatus("mandatory")
_IsDeviceConfigHumidityHighCriticalState_Type = IsproEnuEnable
_IsDeviceConfigHumidityHighCriticalState_Object = MibTableColumn
isDeviceConfigHumidityHighCriticalState = _IsDeviceConfigHumidityHighCriticalState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 12),
    _IsDeviceConfigHumidityHighCriticalState_Type()
)
isDeviceConfigHumidityHighCriticalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityHighCriticalState.setStatus("mandatory")
_IsDeviceConfigHumidityEventDO_Type = IsproEnuDO
_IsDeviceConfigHumidityEventDO_Object = MibTableColumn
isDeviceConfigHumidityEventDO = _IsDeviceConfigHumidityEventDO_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 3, 1, 13),
    _IsDeviceConfigHumidityEventDO_Type()
)
isDeviceConfigHumidityEventDO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigHumidityEventDO.setStatus("mandatory")
_IsDeviceConfigDigitalInTable_Object = MibTable
isDeviceConfigDigitalInTable = _IsDeviceConfigDigitalInTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    isDeviceConfigDigitalInTable.setStatus("mandatory")
_IsDeviceConfigDigitalInEntry_Object = MibTableRow
isDeviceConfigDigitalInEntry = _IsDeviceConfigDigitalInEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 4, 1)
)
isDeviceConfigDigitalInEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceConfigDigitalInIndex"),
)
if mibBuilder.loadTexts:
    isDeviceConfigDigitalInEntry.setStatus("mandatory")


class _IsDeviceConfigDigitalInIndex_Type(Integer32):
    """Custom type isDeviceConfigDigitalInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IsDeviceConfigDigitalInIndex_Type.__name__ = "Integer32"
_IsDeviceConfigDigitalInIndex_Object = MibTableColumn
isDeviceConfigDigitalInIndex = _IsDeviceConfigDigitalInIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 4, 1, 1),
    _IsDeviceConfigDigitalInIndex_Type()
)
isDeviceConfigDigitalInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceConfigDigitalInIndex.setStatus("mandatory")


class _IsDeviceConfigDigitalInName_Type(DisplayString):
    """Custom type isDeviceConfigDigitalInName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsDeviceConfigDigitalInName_Type.__name__ = "DisplayString"
_IsDeviceConfigDigitalInName_Object = MibTableColumn
isDeviceConfigDigitalInName = _IsDeviceConfigDigitalInName_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 4, 1, 2),
    _IsDeviceConfigDigitalInName_Type()
)
isDeviceConfigDigitalInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigDigitalInName.setStatus("mandatory")
_IsDeviceConfigDigitalInState_Type = IsproEnuAlarmState
_IsDeviceConfigDigitalInState_Object = MibTableColumn
isDeviceConfigDigitalInState = _IsDeviceConfigDigitalInState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 4, 1, 3),
    _IsDeviceConfigDigitalInState_Type()
)
isDeviceConfigDigitalInState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigDigitalInState.setStatus("mandatory")
_IsDeviceConfigDigitalInHysteresis_Type = Integer32
_IsDeviceConfigDigitalInHysteresis_Object = MibTableColumn
isDeviceConfigDigitalInHysteresis = _IsDeviceConfigDigitalInHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 4, 1, 4),
    _IsDeviceConfigDigitalInHysteresis_Type()
)
isDeviceConfigDigitalInHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigDigitalInHysteresis.setStatus("mandatory")
_IsDeviceConfigDigitalInEventDO_Type = IsproEnuDO
_IsDeviceConfigDigitalInEventDO_Object = MibTableColumn
isDeviceConfigDigitalInEventDO = _IsDeviceConfigDigitalInEventDO_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 4, 1, 5),
    _IsDeviceConfigDigitalInEventDO_Type()
)
isDeviceConfigDigitalInEventDO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceConfigDigitalInEventDO.setStatus("mandatory")
_IsDeviceDigitalOutTable_Object = MibTable
isDeviceDigitalOutTable = _IsDeviceDigitalOutTable_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    isDeviceDigitalOutTable.setStatus("mandatory")
_IsDeviceDigitalOutEntry_Object = MibTableRow
isDeviceDigitalOutEntry = _IsDeviceDigitalOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 5, 1)
)
isDeviceDigitalOutEntry.setIndexNames(
    (0, "ISPRO-MIB", "isDeviceDigitalOutIndex"),
)
if mibBuilder.loadTexts:
    isDeviceDigitalOutEntry.setStatus("mandatory")


class _IsDeviceDigitalOutIndex_Type(Integer32):
    """Custom type isDeviceDigitalOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_IsDeviceDigitalOutIndex_Type.__name__ = "Integer32"
_IsDeviceDigitalOutIndex_Object = MibTableColumn
isDeviceDigitalOutIndex = _IsDeviceDigitalOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 5, 1, 1),
    _IsDeviceDigitalOutIndex_Type()
)
isDeviceDigitalOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceDigitalOutIndex.setStatus("mandatory")
_IsDeviceDigitalOutStartState_Type = IsproEnuOnOff
_IsDeviceDigitalOutStartState_Object = MibTableColumn
isDeviceDigitalOutStartState = _IsDeviceDigitalOutStartState_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 5, 1, 2),
    _IsDeviceDigitalOutStartState_Type()
)
isDeviceDigitalOutStartState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceDigitalOutStartState.setStatus("mandatory")
_IsDeviceDigitalOutEventAction_Type = IsproEnuEnable
_IsDeviceDigitalOutEventAction_Object = MibTableColumn
isDeviceDigitalOutEventAction = _IsDeviceDigitalOutEventAction_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 5, 1, 3),
    _IsDeviceDigitalOutEventAction_Type()
)
isDeviceDigitalOutEventAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceDigitalOutEventAction.setStatus("mandatory")
_IsDeviceDigitalOutManualControl_Type = IsproEnuTurnOnOff
_IsDeviceDigitalOutManualControl_Object = MibTableColumn
isDeviceDigitalOutManualControl = _IsDeviceDigitalOutManualControl_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 2, 5, 1, 4),
    _IsDeviceDigitalOutManualControl_Type()
)
isDeviceDigitalOutManualControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isDeviceDigitalOutManualControl.setStatus("mandatory")


class _IsDeviceID_Type(Integer32):
    """Custom type isDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IsDeviceID_Type.__name__ = "Integer32"
_IsDeviceID_Object = MibScalar
isDeviceID = _IsDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 1, 3, 3),
    _IsDeviceID_Type()
)
isDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isDeviceID.setStatus("mandatory")
_IsTraps_ObjectIdentity = ObjectIdentity
isTraps = _IsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 2)
)


class _IsTrapsDescription_Type(DisplayString):
    """Custom type isTrapsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IsTrapsDescription_Type.__name__ = "DisplayString"
_IsTrapsDescription_Object = MibScalar
isTrapsDescription = _IsTrapsDescription_Object(
    (1, 3, 6, 1, 4, 1, 19011, 1, 3, 2, 2, 1),
    _IsTrapsDescription_Type()
)
isTrapsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isTrapsDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISPRO-MIB",
    **{"IsproEnuEnable": IsproEnuEnable,
       "IsproEnuReset": IsproEnuReset,
       "IsproEnuRestart": IsproEnuRestart,
       "IsproEnuSeverity": IsproEnuSeverity,
       "IsproEnuAccess": IsproEnuAccess,
       "IsproEnuTempUnit": IsproEnuTempUnit,
       "IsproEnuDateFormat": IsproEnuDateFormat,
       "IsproEnuTimeZone": IsproEnuTimeZone,
       "IsproEnuSensorType": IsproEnuSensorType,
       "IsproEnuThresholdStatus": IsproEnuThresholdStatus,
       "IsproEnuDigitalStatus": IsproEnuDigitalStatus,
       "IsproTriggerStatus": IsproTriggerStatus,
       "IsproEnuSensorState": IsproEnuSensorState,
       "IsproEnuTempCalibration": IsproEnuTempCalibration,
       "IsproEnuHumidityCalibration": IsproEnuHumidityCalibration,
       "IsproEnuAlarmState": IsproEnuAlarmState,
       "IsproEnuOnOff": IsproEnuOnOff,
       "IsproEnuTurnOnOff": IsproEnuTurnOnOff,
       "IsproEnuPresent": IsproEnuPresent,
       "IsproEnuDO": IsproEnuDO,
       "IsproEnuHighLow": IsproEnuHighLow,
       "IsproLogType": IsproLogType,
       "jacarta": jacarta,
       "product": product,
       "webAppliance": webAppliance,
       "ispro": ispro,
       "isObjects": isObjects,
       "isIdent": isIdent,
       "isIdentManufacturer": isIdentManufacturer,
       "isIdentModel": isIdentModel,
       "isIdentAgentSoftwareVersion": isIdentAgentSoftwareVersion,
       "isIdentName": isIdentName,
       "isConfig": isConfig,
       "isConfigMibVersion": isConfigMibVersion,
       "isConfigNetwork": isConfigNetwork,
       "isConfigIpAddress": isConfigIpAddress,
       "isConfigGateway": isConfigGateway,
       "isConfigSubnetMask": isConfigSubnetMask,
       "isConfigDateTime": isConfigDateTime,
       "isConfigDate": isConfigDate,
       "isConfigTime": isConfigTime,
       "isConfigTimeFromNtp": isConfigTimeFromNtp,
       "isConfigNtpIpAddress": isConfigNtpIpAddress,
       "isConfigNtpTimeZone": isConfigNtpTimeZone,
       "isConfigDayLightSaving": isConfigDayLightSaving,
       "isConfigLog": isConfigLog,
       "isConfigHistoryLogFrequency": isConfigHistoryLogFrequency,
       "isConfigExtHistoryLogFrequency": isConfigExtHistoryLogFrequency,
       "isConfigConfigurationLog": isConfigConfigurationLog,
       "isConfigLogType": isConfigLogType,
       "isConfigDhcpState": isConfigDhcpState,
       "isConfigPingState": isConfigPingState,
       "isConfigTftpState": isConfigTftpState,
       "isConfigTelnet": isConfigTelnet,
       "isConfigTelnetState": isConfigTelnetState,
       "isConfigTelnetPortNumber": isConfigTelnetPortNumber,
       "isConfigHttp": isConfigHttp,
       "isConfigHttpState": isConfigHttpState,
       "isConfigHttpPortNumber": isConfigHttpPortNumber,
       "isConfigHttpSecurity": isConfigHttpSecurity,
       "isConfigSnmp": isConfigSnmp,
       "isConfigSnmpState": isConfigSnmpState,
       "isConfigSnmpPortNumber": isConfigSnmpPortNumber,
       "isConfigControl": isConfigControl,
       "isConfigResetToDefault": isConfigResetToDefault,
       "isConfigRestart": isConfigRestart,
       "isConfigTrap": isConfigTrap,
       "isConfigTrapRetryCount": isConfigTrapRetryCount,
       "isConfigTrapRetryTime": isConfigTrapRetryTime,
       "isConfigTrapAckSignature": isConfigTrapAckSignature,
       "isConfigRefreshRate": isConfigRefreshRate,
       "isConfigTrapReceiverTable": isConfigTrapReceiverTable,
       "isConfigTrapReceiverEntry": isConfigTrapReceiverEntry,
       "isReceiverIndex": isReceiverIndex,
       "isReceiverAddr": isReceiverAddr,
       "isReceiverCommunityString": isReceiverCommunityString,
       "isReceiverSeverityLevel": isReceiverSeverityLevel,
       "isReceiverDescription": isReceiverDescription,
       "isConfigAccessControlTable": isConfigAccessControlTable,
       "isConfigAccessControlEntry": isConfigAccessControlEntry,
       "isAccessIndex": isAccessIndex,
       "isAccessControlAddr": isAccessControlAddr,
       "isAccessCommunityString": isAccessCommunityString,
       "isAccessControlMode": isAccessControlMode,
       "isAccessAccount": isAccessAccount,
       "isConfigTemperatureUnit": isConfigTemperatureUnit,
       "isConfigDateFormat": isConfigDateFormat,
       "isDevice": isDevice,
       "isDeviceMonitor": isDeviceMonitor,
       "isDeviceMonitorTemperatureTable": isDeviceMonitorTemperatureTable,
       "isDeviceMonitorTemperatureEntry": isDeviceMonitorTemperatureEntry,
       "isDeviceMonitorTemperatureIndex": isDeviceMonitorTemperatureIndex,
       "isDeviceMonitorTemperatureName": isDeviceMonitorTemperatureName,
       "isDeviceMonitorTemperature": isDeviceMonitorTemperature,
       "isDeviceMonitorTemperatureAlarm": isDeviceMonitorTemperatureAlarm,
       "isDeviceMonitorHumidityTable": isDeviceMonitorHumidityTable,
       "isDeviceMonitorHumidityEntry": isDeviceMonitorHumidityEntry,
       "isDeviceMonitorHumidityIndex": isDeviceMonitorHumidityIndex,
       "isDeviceMonitorHumidityName": isDeviceMonitorHumidityName,
       "isDeviceMonitorHumidity": isDeviceMonitorHumidity,
       "isDeviceMonitorHumidityAlarm": isDeviceMonitorHumidityAlarm,
       "isDeviceMonitorDigitalInTable": isDeviceMonitorDigitalInTable,
       "isDeviceMonitorDigitalInEntry": isDeviceMonitorDigitalInEntry,
       "isDeviceMonitorDigitalInIndex": isDeviceMonitorDigitalInIndex,
       "isDeviceMonitorDigitalInName": isDeviceMonitorDigitalInName,
       "isDeviceMonitorDigitalIn": isDeviceMonitorDigitalIn,
       "isDeviceMonitorDigitalInAlarm": isDeviceMonitorDigitalInAlarm,
       "isDeviceConfig": isDeviceConfig,
       "isDeviceConfigTable": isDeviceConfigTable,
       "isDeviceConfigEntry": isDeviceConfigEntry,
       "isDeviceConfigIndex": isDeviceConfigIndex,
       "isDeviceConfigName": isDeviceConfigName,
       "isDeviceConfigState": isDeviceConfigState,
       "isDeviceConfigDisplay": isDeviceConfigDisplay,
       "isDeviceConfigTemperatureTable": isDeviceConfigTemperatureTable,
       "isDeviceConfigTemperatureEntry": isDeviceConfigTemperatureEntry,
       "isDeviceConfigTemperatureIndex": isDeviceConfigTemperatureIndex,
       "isDeviceConfigTemperatureName": isDeviceConfigTemperatureName,
       "isDeviceConfigTemperatureLowWarning": isDeviceConfigTemperatureLowWarning,
       "isDeviceConfigTemperatureLowCritical": isDeviceConfigTemperatureLowCritical,
       "isDeviceConfigTemperatureHighWarning": isDeviceConfigTemperatureHighWarning,
       "isDeviceConfigTemperatureHighCritical": isDeviceConfigTemperatureHighCritical,
       "isDeviceConfigTemperatureHysteresis": isDeviceConfigTemperatureHysteresis,
       "isDeviceConfigTemperatureCalibration": isDeviceConfigTemperatureCalibration,
       "isDeviceConfigTemperatureLowWarningState": isDeviceConfigTemperatureLowWarningState,
       "isDeviceConfigTemperatureLowCriticalState": isDeviceConfigTemperatureLowCriticalState,
       "isDeviceConfigTemperatureHighWarningState": isDeviceConfigTemperatureHighWarningState,
       "isDeviceConfigTemperatureHighCriticalState": isDeviceConfigTemperatureHighCriticalState,
       "isDeviceConfigTemperatureEventDO": isDeviceConfigTemperatureEventDO,
       "isDeviceConfigHumidityTable": isDeviceConfigHumidityTable,
       "isDeviceConfigHumidityEntry": isDeviceConfigHumidityEntry,
       "isDeviceConfigHumidityIndex": isDeviceConfigHumidityIndex,
       "isDeviceConfigHumidityName": isDeviceConfigHumidityName,
       "isDeviceConfigHumidityLowWarning": isDeviceConfigHumidityLowWarning,
       "isDeviceConfigHumidityLowCritical": isDeviceConfigHumidityLowCritical,
       "isDeviceConfigHumidityHighWarning": isDeviceConfigHumidityHighWarning,
       "isDeviceConfigHumidityHighCritical": isDeviceConfigHumidityHighCritical,
       "isDeviceConfigHumidityHysteresis": isDeviceConfigHumidityHysteresis,
       "isDeviceConfigHumidityCalibration": isDeviceConfigHumidityCalibration,
       "isDeviceConfigHumidityLowWarningState": isDeviceConfigHumidityLowWarningState,
       "isDeviceConfigHumidityLowCriticalState": isDeviceConfigHumidityLowCriticalState,
       "isDeviceConfigHumidityHighWarningState": isDeviceConfigHumidityHighWarningState,
       "isDeviceConfigHumidityHighCriticalState": isDeviceConfigHumidityHighCriticalState,
       "isDeviceConfigHumidityEventDO": isDeviceConfigHumidityEventDO,
       "isDeviceConfigDigitalInTable": isDeviceConfigDigitalInTable,
       "isDeviceConfigDigitalInEntry": isDeviceConfigDigitalInEntry,
       "isDeviceConfigDigitalInIndex": isDeviceConfigDigitalInIndex,
       "isDeviceConfigDigitalInName": isDeviceConfigDigitalInName,
       "isDeviceConfigDigitalInState": isDeviceConfigDigitalInState,
       "isDeviceConfigDigitalInHysteresis": isDeviceConfigDigitalInHysteresis,
       "isDeviceConfigDigitalInEventDO": isDeviceConfigDigitalInEventDO,
       "isDeviceDigitalOutTable": isDeviceDigitalOutTable,
       "isDeviceDigitalOutEntry": isDeviceDigitalOutEntry,
       "isDeviceDigitalOutIndex": isDeviceDigitalOutIndex,
       "isDeviceDigitalOutStartState": isDeviceDigitalOutStartState,
       "isDeviceDigitalOutEventAction": isDeviceDigitalOutEventAction,
       "isDeviceDigitalOutManualControl": isDeviceDigitalOutManualControl,
       "isDeviceID": isDeviceID,
       "isTraps": isTraps,
       "isTrapsDescription": isTrapsDescription}
)
