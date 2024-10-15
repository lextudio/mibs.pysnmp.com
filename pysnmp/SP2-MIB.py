# SNMP MIB module (SP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:17 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eltek = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12148)
)
eltek.setRevisions(
        ("2011-11-25 09:58",
         "2011-10-17 13:34",
         "2011-08-19 09:16",
         "2011-08-19 09:47",
         "2011-09-05 11:28")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ENexus_ObjectIdentity = ObjectIdentity
eNexus = _ENexus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10)
)
_EltekTraps_ObjectIdentity = ObjectIdentity
eltekTraps = _EltekTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1)
)
_PowerAlarmVars_ObjectIdentity = ObjectIdentity
powerAlarmVars = _PowerAlarmVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1)
)


class _AlarmSubsysSourceDescr_Type(DisplayString):
    """Custom type alarmSubsysSourceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlarmSubsysSourceDescr_Type.__name__ = "DisplayString"
_AlarmSubsysSourceDescr_Object = MibScalar
alarmSubsysSourceDescr = _AlarmSubsysSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 1),
    _AlarmSubsysSourceDescr_Type()
)
alarmSubsysSourceDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysSourceDescr.setStatus("current")
_AlarmSubsysStatusOid_Type = ObjectIdentifier
_AlarmSubsysStatusOid_Object = MibScalar
alarmSubsysStatusOid = _AlarmSubsysStatusOid_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 2),
    _AlarmSubsysStatusOid_Type()
)
alarmSubsysStatusOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysStatusOid.setStatus("current")


class _AlarmSubsysStatusValue_Type(Integer32):
    """Custom type alarmSubsysStatusValue based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_AlarmSubsysStatusValue_Type.__name__ = "Integer32"
_AlarmSubsysStatusValue_Object = MibScalar
alarmSubsysStatusValue = _AlarmSubsysStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 3),
    _AlarmSubsysStatusValue_Type()
)
alarmSubsysStatusValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysStatusValue.setStatus("current")


class _AlarmSubsysStatusOnOff_Type(Integer32):
    """Custom type alarmSubsysStatusOnOff based on Integer32"""
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


_AlarmSubsysStatusOnOff_Type.__name__ = "Integer32"
_AlarmSubsysStatusOnOff_Object = MibScalar
alarmSubsysStatusOnOff = _AlarmSubsysStatusOnOff_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 4),
    _AlarmSubsysStatusOnOff_Type()
)
alarmSubsysStatusOnOff.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysStatusOnOff.setStatus("current")
_AlarmMeasuredVarOid_Type = ObjectIdentifier
_AlarmMeasuredVarOid_Object = MibScalar
alarmMeasuredVarOid = _AlarmMeasuredVarOid_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 5),
    _AlarmMeasuredVarOid_Type()
)
alarmMeasuredVarOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmMeasuredVarOid.setStatus("current")
_AlarmMeasuredVarValue_Type = Integer32
_AlarmMeasuredVarValue_Object = MibScalar
alarmMeasuredVarValue = _AlarmMeasuredVarValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 6),
    _AlarmMeasuredVarValue_Type()
)
alarmMeasuredVarValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmMeasuredVarValue.setStatus("current")
_AlarmTrapCounterVarValue_Type = Integer32
_AlarmTrapCounterVarValue_Object = MibScalar
alarmTrapCounterVarValue = _AlarmTrapCounterVarValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 7),
    _AlarmTrapCounterVarValue_Type()
)
alarmTrapCounterVarValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTrapCounterVarValue.setStatus("current")
_PowerSystemTraps_ObjectIdentity = ObjectIdentity
powerSystemTraps = _PowerSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2)
)
_PowerSystem_ObjectIdentity = ObjectIdentity
powerSystem = _PowerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2)
)


class _PowerSystemStatus_Type(Integer32):
    """Custom type powerSystemStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_PowerSystemStatus_Type.__name__ = "Integer32"
_PowerSystemStatus_Object = MibScalar
powerSystemStatus = _PowerSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 1),
    _PowerSystemStatus_Type()
)
powerSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemStatus.setStatus("current")


class _PowerSystemType_Type(Integer32):
    """Custom type powerSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compack", 3),
          ("smartpack2", 1),
          ("smartpackS", 2))
    )


_PowerSystemType_Type.__name__ = "Integer32"
_PowerSystemType_Object = MibScalar
powerSystemType = _PowerSystemType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 2),
    _PowerSystemType_Type()
)
powerSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemType.setStatus("current")


class _PowerSystemMode_Type(Integer32):
    """Custom type powerSystemMode based on Integer32"""
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
        *(("boost", 2),
          ("float", 3),
          ("off", 0),
          ("test", 1))
    )


_PowerSystemMode_Type.__name__ = "Integer32"
_PowerSystemMode_Object = MibScalar
powerSystemMode = _PowerSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 3),
    _PowerSystemMode_Type()
)
powerSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemMode.setStatus("current")


class _PowerSystemCompany_Type(DisplayString):
    """Custom type powerSystemCompany based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PowerSystemCompany_Type.__name__ = "DisplayString"
_PowerSystemCompany_Object = MibScalar
powerSystemCompany = _PowerSystemCompany_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 4),
    _PowerSystemCompany_Type()
)
powerSystemCompany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemCompany.setStatus("current")


class _PowerSystemSite_Type(DisplayString):
    """Custom type powerSystemSite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PowerSystemSite_Type.__name__ = "DisplayString"
_PowerSystemSite_Object = MibScalar
powerSystemSite = _PowerSystemSite_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 5),
    _PowerSystemSite_Type()
)
powerSystemSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemSite.setStatus("current")


class _PowerSystemModel_Type(DisplayString):
    """Custom type powerSystemModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PowerSystemModel_Type.__name__ = "DisplayString"
_PowerSystemModel_Object = MibScalar
powerSystemModel = _PowerSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 6),
    _PowerSystemModel_Type()
)
powerSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemModel.setStatus("current")


class _PowerSystemSerialNumber_Type(DisplayString):
    """Custom type powerSystemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PowerSystemSerialNumber_Type.__name__ = "DisplayString"
_PowerSystemSerialNumber_Object = MibScalar
powerSystemSerialNumber = _PowerSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 7),
    _PowerSystemSerialNumber_Type()
)
powerSystemSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemSerialNumber.setStatus("current")
_PowerSystemInstallDate_Type = DateAndTime
_PowerSystemInstallDate_Object = MibScalar
powerSystemInstallDate = _PowerSystemInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 8),
    _PowerSystemInstallDate_Type()
)
powerSystemInstallDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemInstallDate.setStatus("current")


class _PowerSystemNominalVoltage_Type(Integer32):
    """Custom type powerSystemNominalVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 250),
    )


_PowerSystemNominalVoltage_Type.__name__ = "Integer32"
_PowerSystemNominalVoltage_Object = MibScalar
powerSystemNominalVoltage = _PowerSystemNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 9),
    _PowerSystemNominalVoltage_Type()
)
powerSystemNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemNominalVoltage.setStatus("current")


class _PowerSystemLongitude_Type(Integer32):
    """Custom type powerSystemLongitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180, 180),
    )


_PowerSystemLongitude_Type.__name__ = "Integer32"
_PowerSystemLongitude_Object = MibScalar
powerSystemLongitude = _PowerSystemLongitude_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 10),
    _PowerSystemLongitude_Type()
)
powerSystemLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLongitude.setStatus("current")
_PowerSystemLongitudeDecimal_Type = Integer32
_PowerSystemLongitudeDecimal_Object = MibScalar
powerSystemLongitudeDecimal = _PowerSystemLongitudeDecimal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 11),
    _PowerSystemLongitudeDecimal_Type()
)
powerSystemLongitudeDecimal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLongitudeDecimal.setStatus("current")


class _PowerSystemLatitude_Type(Integer32):
    """Custom type powerSystemLatitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 90),
    )


_PowerSystemLatitude_Type.__name__ = "Integer32"
_PowerSystemLatitude_Object = MibScalar
powerSystemLatitude = _PowerSystemLatitude_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 12),
    _PowerSystemLatitude_Type()
)
powerSystemLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLatitude.setStatus("current")
_PowerSystemLatitudeDecimal_Type = Integer32
_PowerSystemLatitudeDecimal_Object = MibScalar
powerSystemLatitudeDecimal = _PowerSystemLatitudeDecimal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 13),
    _PowerSystemLatitudeDecimal_Type()
)
powerSystemLatitudeDecimal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLatitudeDecimal.setStatus("current")
_PowerSystemElevation_Type = Integer32
_PowerSystemElevation_Object = MibScalar
powerSystemElevation = _PowerSystemElevation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 14),
    _PowerSystemElevation_Type()
)
powerSystemElevation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemElevation.setStatus("current")


class _PowerSystemCurrentDecimalSetting_Type(Integer32):
    """Custom type powerSystemCurrentDecimalSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ampere", 0),
          ("deciAmpere", 1))
    )


_PowerSystemCurrentDecimalSetting_Type.__name__ = "Integer32"
_PowerSystemCurrentDecimalSetting_Object = MibScalar
powerSystemCurrentDecimalSetting = _PowerSystemCurrentDecimalSetting_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 15),
    _PowerSystemCurrentDecimalSetting_Type()
)
powerSystemCurrentDecimalSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemCurrentDecimalSetting.setStatus("current")


class _PowerSystemTemperatureScale_Type(Integer32):
    """Custom type powerSystemTemperatureScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celcius", 0),
          ("fahrenheit", 1))
    )


_PowerSystemTemperatureScale_Type.__name__ = "Integer32"
_PowerSystemTemperatureScale_Object = MibScalar
powerSystemTemperatureScale = _PowerSystemTemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 16),
    _PowerSystemTemperatureScale_Type()
)
powerSystemTemperatureScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemTemperatureScale.setStatus("current")


class _PowerSystemCapacityScale_Type(Integer32):
    """Custom type powerSystemCapacityScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ah", 0),
          ("percent", 1))
    )


_PowerSystemCapacityScale_Type.__name__ = "Integer32"
_PowerSystemCapacityScale_Object = MibScalar
powerSystemCapacityScale = _PowerSystemCapacityScale_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 17),
    _PowerSystemCapacityScale_Type()
)
powerSystemCapacityScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemCapacityScale.setStatus("current")
_Mains_ObjectIdentity = ObjectIdentity
mains = _Mains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3)
)


class _MainsStatus_Type(Integer32):
    """Custom type mainsStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_MainsStatus_Type.__name__ = "Integer32"
_MainsStatus_Object = MibScalar
mainsStatus = _MainsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 1),
    _MainsStatus_Type()
)
mainsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsStatus.setStatus("current")
_MainsMainsFailure_ObjectIdentity = ObjectIdentity
mainsMainsFailure = _MainsMainsFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2)
)


class _MainsMainsFailureStatus_Type(Integer32):
    """Custom type mainsMainsFailureStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_MainsMainsFailureStatus_Type.__name__ = "Integer32"
_MainsMainsFailureStatus_Object = MibScalar
mainsMainsFailureStatus = _MainsMainsFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 1),
    _MainsMainsFailureStatus_Type()
)
mainsMainsFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMainsFailureStatus.setStatus("current")


class _MainsMainsFailureDescription_Type(DisplayString):
    """Custom type mainsMainsFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsMainsFailureDescription_Type.__name__ = "DisplayString"
_MainsMainsFailureDescription_Object = MibScalar
mainsMainsFailureDescription = _MainsMainsFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 2),
    _MainsMainsFailureDescription_Type()
)
mainsMainsFailureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureDescription.setStatus("current")
_MainsMainsFailureTrapRepeatCounter_Type = Integer32
_MainsMainsFailureTrapRepeatCounter_Object = MibScalar
mainsMainsFailureTrapRepeatCounter = _MainsMainsFailureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 3),
    _MainsMainsFailureTrapRepeatCounter_Type()
)
mainsMainsFailureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMainsFailureTrapRepeatCounter.setStatus("current")


class _MainsMainsFailureAlarmEnable_Type(Integer32):
    """Custom type mainsMainsFailureAlarmEnable based on Integer32"""
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


_MainsMainsFailureAlarmEnable_Type.__name__ = "Integer32"
_MainsMainsFailureAlarmEnable_Object = MibScalar
mainsMainsFailureAlarmEnable = _MainsMainsFailureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 4),
    _MainsMainsFailureAlarmEnable_Type()
)
mainsMainsFailureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureAlarmEnable.setStatus("current")
_MainsMainsFailureValue_Type = Integer32
_MainsMainsFailureValue_Object = MibScalar
mainsMainsFailureValue = _MainsMainsFailureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 5),
    _MainsMainsFailureValue_Type()
)
mainsMainsFailureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMainsFailureValue.setStatus("current")
_MainsMainsFailureMajorAlarmLevel_Type = Integer32
_MainsMainsFailureMajorAlarmLevel_Object = MibScalar
mainsMainsFailureMajorAlarmLevel = _MainsMainsFailureMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 6),
    _MainsMainsFailureMajorAlarmLevel_Type()
)
mainsMainsFailureMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureMajorAlarmLevel.setStatus("current")
_MainsMainsFailureMinorAlarmLevel_Type = Integer32
_MainsMainsFailureMinorAlarmLevel_Object = MibScalar
mainsMainsFailureMinorAlarmLevel = _MainsMainsFailureMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 7),
    _MainsMainsFailureMinorAlarmLevel_Type()
)
mainsMainsFailureMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureMinorAlarmLevel.setStatus("current")
_MainsNumberOfPhases_Type = Integer32
_MainsNumberOfPhases_Object = MibScalar
mainsNumberOfPhases = _MainsNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 3),
    _MainsNumberOfPhases_Type()
)
mainsNumberOfPhases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsNumberOfPhases.setStatus("current")
_MainsVoltageTable_Object = MibTable
mainsVoltageTable = _MainsVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4)
)
if mibBuilder.loadTexts:
    mainsVoltageTable.setStatus("current")
_MainsVoltageEntry_Object = MibTableRow
mainsVoltageEntry = _MainsVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1)
)
mainsVoltageEntry.setIndexNames(
    (0, "SP2-MIB", "mainsVoltageIndex"),
)
if mibBuilder.loadTexts:
    mainsVoltageEntry.setStatus("current")


class _MainsVoltageIndex_Type(Integer32):
    """Custom type mainsVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MainsVoltageIndex_Type.__name__ = "Integer32"
_MainsVoltageIndex_Object = MibTableColumn
mainsVoltageIndex = _MainsVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 1),
    _MainsVoltageIndex_Type()
)
mainsVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsVoltageIndex.setStatus("current")


class _MainsVoltageStatus_Type(Integer32):
    """Custom type mainsVoltageStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_MainsVoltageStatus_Type.__name__ = "Integer32"
_MainsVoltageStatus_Object = MibTableColumn
mainsVoltageStatus = _MainsVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 2),
    _MainsVoltageStatus_Type()
)
mainsVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVoltageStatus.setStatus("current")


class _MainsVoltageDescription_Type(DisplayString):
    """Custom type mainsVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsVoltageDescription_Type.__name__ = "DisplayString"
_MainsVoltageDescription_Object = MibTableColumn
mainsVoltageDescription = _MainsVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 3),
    _MainsVoltageDescription_Type()
)
mainsVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageDescription.setStatus("current")
_MainsVoltageTrapRepeatCounter_Type = Counter32
_MainsVoltageTrapRepeatCounter_Object = MibTableColumn
mainsVoltageTrapRepeatCounter = _MainsVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 4),
    _MainsVoltageTrapRepeatCounter_Type()
)
mainsVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsVoltageTrapRepeatCounter.setStatus("current")


class _MainsVoltageAlarmEnable_Type(Integer32):
    """Custom type mainsVoltageAlarmEnable based on Integer32"""
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


_MainsVoltageAlarmEnable_Type.__name__ = "Integer32"
_MainsVoltageAlarmEnable_Object = MibTableColumn
mainsVoltageAlarmEnable = _MainsVoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 5),
    _MainsVoltageAlarmEnable_Type()
)
mainsVoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageAlarmEnable.setStatus("current")
_MainsVoltageValue_Type = Integer32
_MainsVoltageValue_Object = MibTableColumn
mainsVoltageValue = _MainsVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 6),
    _MainsVoltageValue_Type()
)
mainsVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVoltageValue.setStatus("current")
_MainsVoltageMajorHighLevel_Type = Integer32
_MainsVoltageMajorHighLevel_Object = MibTableColumn
mainsVoltageMajorHighLevel = _MainsVoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 7),
    _MainsVoltageMajorHighLevel_Type()
)
mainsVoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMajorHighLevel.setStatus("current")
_MainsVoltageMinorHighLevel_Type = Integer32
_MainsVoltageMinorHighLevel_Object = MibTableColumn
mainsVoltageMinorHighLevel = _MainsVoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 8),
    _MainsVoltageMinorHighLevel_Type()
)
mainsVoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMinorHighLevel.setStatus("current")
_MainsVoltageMinorLowLevel_Type = Integer32
_MainsVoltageMinorLowLevel_Object = MibTableColumn
mainsVoltageMinorLowLevel = _MainsVoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 9),
    _MainsVoltageMinorLowLevel_Type()
)
mainsVoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMinorLowLevel.setStatus("current")
_MainsVoltageMajorLowLevel_Type = Integer32
_MainsVoltageMajorLowLevel_Object = MibTableColumn
mainsVoltageMajorLowLevel = _MainsVoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 10),
    _MainsVoltageMajorLowLevel_Type()
)
mainsVoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMajorLowLevel.setStatus("current")
_MainsMonitors_ObjectIdentity = ObjectIdentity
mainsMonitors = _MainsMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5)
)


class _MainsMonitorsNumberOfUnits_Type(Integer32):
    """Custom type mainsMonitorsNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_MainsMonitorsNumberOfUnits_Type.__name__ = "Integer32"
_MainsMonitorsNumberOfUnits_Object = MibScalar
mainsMonitorsNumberOfUnits = _MainsMonitorsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 1),
    _MainsMonitorsNumberOfUnits_Type()
)
mainsMonitorsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorsNumberOfUnits.setStatus("current")
_MainsMonitorsTable_Object = MibTable
mainsMonitorsTable = _MainsMonitorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2)
)
if mibBuilder.loadTexts:
    mainsMonitorsTable.setStatus("current")
_MainsMonitorsEntry_Object = MibTableRow
mainsMonitorsEntry = _MainsMonitorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1)
)
mainsMonitorsEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorsEntry.setStatus("current")


class _MainsMonitorIndex_Type(Integer32):
    """Custom type mainsMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_MainsMonitorIndex_Type.__name__ = "Integer32"
_MainsMonitorIndex_Object = MibTableColumn
mainsMonitorIndex = _MainsMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 1),
    _MainsMonitorIndex_Type()
)
mainsMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorIndex.setStatus("current")


class _MainsMonitorNumberOfVoltages_Type(Integer32):
    """Custom type mainsMonitorNumberOfVoltages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MainsMonitorNumberOfVoltages_Type.__name__ = "Integer32"
_MainsMonitorNumberOfVoltages_Object = MibTableColumn
mainsMonitorNumberOfVoltages = _MainsMonitorNumberOfVoltages_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 2),
    _MainsMonitorNumberOfVoltages_Type()
)
mainsMonitorNumberOfVoltages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorNumberOfVoltages.setStatus("current")


class _MainsMonitorNumberOfCurrents_Type(Integer32):
    """Custom type mainsMonitorNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MainsMonitorNumberOfCurrents_Type.__name__ = "Integer32"
_MainsMonitorNumberOfCurrents_Object = MibTableColumn
mainsMonitorNumberOfCurrents = _MainsMonitorNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 3),
    _MainsMonitorNumberOfCurrents_Type()
)
mainsMonitorNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorNumberOfCurrents.setStatus("current")


class _MainsMonitorNumberOfFrequencies_Type(Integer32):
    """Custom type mainsMonitorNumberOfFrequencies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MainsMonitorNumberOfFrequencies_Type.__name__ = "Integer32"
_MainsMonitorNumberOfFrequencies_Object = MibTableColumn
mainsMonitorNumberOfFrequencies = _MainsMonitorNumberOfFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 4),
    _MainsMonitorNumberOfFrequencies_Type()
)
mainsMonitorNumberOfFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorNumberOfFrequencies.setStatus("current")
_MainsMonitorVoltageTable_Object = MibTable
mainsMonitorVoltageTable = _MainsMonitorVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3)
)
if mibBuilder.loadTexts:
    mainsMonitorVoltageTable.setStatus("current")
_MainsMonitorVoltageEntry_Object = MibTableRow
mainsMonitorVoltageEntry = _MainsMonitorVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1)
)
mainsMonitorVoltageEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorPhaseIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorVoltageEntry.setStatus("current")


class _MainsMonitorPhaseIndex_Type(Integer32):
    """Custom type mainsMonitorPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MainsMonitorPhaseIndex_Type.__name__ = "Integer32"
_MainsMonitorPhaseIndex_Object = MibTableColumn
mainsMonitorPhaseIndex = _MainsMonitorPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 1),
    _MainsMonitorPhaseIndex_Type()
)
mainsMonitorPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorPhaseIndex.setStatus("current")


class _MainsMonitorVoltageStatus_Type(Integer32):
    """Custom type mainsMonitorVoltageStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_MainsMonitorVoltageStatus_Type.__name__ = "Integer32"
_MainsMonitorVoltageStatus_Object = MibTableColumn
mainsMonitorVoltageStatus = _MainsMonitorVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 2),
    _MainsMonitorVoltageStatus_Type()
)
mainsMonitorVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorVoltageStatus.setStatus("current")


class _MainsMonitorVoltageDescription_Type(DisplayString):
    """Custom type mainsMonitorVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MainsMonitorVoltageDescription_Type.__name__ = "DisplayString"
_MainsMonitorVoltageDescription_Object = MibTableColumn
mainsMonitorVoltageDescription = _MainsMonitorVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 3),
    _MainsMonitorVoltageDescription_Type()
)
mainsMonitorVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageDescription.setStatus("current")
_MainsMonitorVoltageTrapRepeatCounter_Type = Counter32
_MainsMonitorVoltageTrapRepeatCounter_Object = MibTableColumn
mainsMonitorVoltageTrapRepeatCounter = _MainsMonitorVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 4),
    _MainsMonitorVoltageTrapRepeatCounter_Type()
)
mainsMonitorVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMonitorVoltageTrapRepeatCounter.setStatus("current")


class _MainsMonitorVoltageAlarmEnable_Type(Integer32):
    """Custom type mainsMonitorVoltageAlarmEnable based on Integer32"""
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


_MainsMonitorVoltageAlarmEnable_Type.__name__ = "Integer32"
_MainsMonitorVoltageAlarmEnable_Object = MibTableColumn
mainsMonitorVoltageAlarmEnable = _MainsMonitorVoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 5),
    _MainsMonitorVoltageAlarmEnable_Type()
)
mainsMonitorVoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageAlarmEnable.setStatus("current")
_MainsMonitorVoltageValue_Type = Integer32
_MainsMonitorVoltageValue_Object = MibTableColumn
mainsMonitorVoltageValue = _MainsMonitorVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 6),
    _MainsMonitorVoltageValue_Type()
)
mainsMonitorVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorVoltageValue.setStatus("current")
_MainsMonitorVoltageMajorHighLevel_Type = Integer32
_MainsMonitorVoltageMajorHighLevel_Object = MibTableColumn
mainsMonitorVoltageMajorHighLevel = _MainsMonitorVoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 7),
    _MainsMonitorVoltageMajorHighLevel_Type()
)
mainsMonitorVoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMajorHighLevel.setStatus("current")
_MainsMonitorVoltageMinorHighLevel_Type = Integer32
_MainsMonitorVoltageMinorHighLevel_Object = MibTableColumn
mainsMonitorVoltageMinorHighLevel = _MainsMonitorVoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 8),
    _MainsMonitorVoltageMinorHighLevel_Type()
)
mainsMonitorVoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMinorHighLevel.setStatus("current")
_MainsMonitorVoltageMinorLowLevel_Type = Integer32
_MainsMonitorVoltageMinorLowLevel_Object = MibTableColumn
mainsMonitorVoltageMinorLowLevel = _MainsMonitorVoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 9),
    _MainsMonitorVoltageMinorLowLevel_Type()
)
mainsMonitorVoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMinorLowLevel.setStatus("current")
_MainsMonitorVoltageMajorLowLevel_Type = Integer32
_MainsMonitorVoltageMajorLowLevel_Object = MibTableColumn
mainsMonitorVoltageMajorLowLevel = _MainsMonitorVoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 10),
    _MainsMonitorVoltageMajorLowLevel_Type()
)
mainsMonitorVoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMajorLowLevel.setStatus("current")
_MainsMonitorCurrentTable_Object = MibTable
mainsMonitorCurrentTable = _MainsMonitorCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4)
)
if mibBuilder.loadTexts:
    mainsMonitorCurrentTable.setStatus("current")
_MainsMonitorCurrentEntry_Object = MibTableRow
mainsMonitorCurrentEntry = _MainsMonitorCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1)
)
mainsMonitorCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorPhaseIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorCurrentEntry.setStatus("current")


class _MainsMonitorCurrentStatus_Type(Integer32):
    """Custom type mainsMonitorCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_MainsMonitorCurrentStatus_Type.__name__ = "Integer32"
_MainsMonitorCurrentStatus_Object = MibTableColumn
mainsMonitorCurrentStatus = _MainsMonitorCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 1),
    _MainsMonitorCurrentStatus_Type()
)
mainsMonitorCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorCurrentStatus.setStatus("current")


class _MainsMonitorCurrentDescription_Type(DisplayString):
    """Custom type mainsMonitorCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MainsMonitorCurrentDescription_Type.__name__ = "DisplayString"
_MainsMonitorCurrentDescription_Object = MibTableColumn
mainsMonitorCurrentDescription = _MainsMonitorCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 2),
    _MainsMonitorCurrentDescription_Type()
)
mainsMonitorCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentDescription.setStatus("current")
_MainsMonitorCurrentTrapRepeatCounter_Type = Counter32
_MainsMonitorCurrentTrapRepeatCounter_Object = MibTableColumn
mainsMonitorCurrentTrapRepeatCounter = _MainsMonitorCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 3),
    _MainsMonitorCurrentTrapRepeatCounter_Type()
)
mainsMonitorCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMonitorCurrentTrapRepeatCounter.setStatus("current")


class _MainsMonitorCurrentAlarmEnable_Type(Integer32):
    """Custom type mainsMonitorCurrentAlarmEnable based on Integer32"""
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


_MainsMonitorCurrentAlarmEnable_Type.__name__ = "Integer32"
_MainsMonitorCurrentAlarmEnable_Object = MibTableColumn
mainsMonitorCurrentAlarmEnable = _MainsMonitorCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 4),
    _MainsMonitorCurrentAlarmEnable_Type()
)
mainsMonitorCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentAlarmEnable.setStatus("current")
_MainsMonitorCurrentValue_Type = Integer32
_MainsMonitorCurrentValue_Object = MibTableColumn
mainsMonitorCurrentValue = _MainsMonitorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 5),
    _MainsMonitorCurrentValue_Type()
)
mainsMonitorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorCurrentValue.setStatus("current")
_MainsMonitorCurrentMajorHighLevel_Type = Integer32
_MainsMonitorCurrentMajorHighLevel_Object = MibTableColumn
mainsMonitorCurrentMajorHighLevel = _MainsMonitorCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 6),
    _MainsMonitorCurrentMajorHighLevel_Type()
)
mainsMonitorCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentMajorHighLevel.setStatus("current")
_MainsMonitorCurrentMinorHighLevel_Type = Integer32
_MainsMonitorCurrentMinorHighLevel_Object = MibTableColumn
mainsMonitorCurrentMinorHighLevel = _MainsMonitorCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 7),
    _MainsMonitorCurrentMinorHighLevel_Type()
)
mainsMonitorCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentMinorHighLevel.setStatus("current")
_MainsMonitorFrequencyTable_Object = MibTable
mainsMonitorFrequencyTable = _MainsMonitorFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5)
)
if mibBuilder.loadTexts:
    mainsMonitorFrequencyTable.setStatus("current")
_MainsMonitorFrequencyEntry_Object = MibTableRow
mainsMonitorFrequencyEntry = _MainsMonitorFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1)
)
mainsMonitorFrequencyEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorFrequencyEntry.setStatus("current")


class _MainsMonitorFrequencyStatus_Type(Integer32):
    """Custom type mainsMonitorFrequencyStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_MainsMonitorFrequencyStatus_Type.__name__ = "Integer32"
_MainsMonitorFrequencyStatus_Object = MibTableColumn
mainsMonitorFrequencyStatus = _MainsMonitorFrequencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 1),
    _MainsMonitorFrequencyStatus_Type()
)
mainsMonitorFrequencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyStatus.setStatus("current")


class _MainsMonitorFrequencyDescription_Type(DisplayString):
    """Custom type mainsMonitorFrequencyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsMonitorFrequencyDescription_Type.__name__ = "DisplayString"
_MainsMonitorFrequencyDescription_Object = MibTableColumn
mainsMonitorFrequencyDescription = _MainsMonitorFrequencyDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 2),
    _MainsMonitorFrequencyDescription_Type()
)
mainsMonitorFrequencyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyDescription.setStatus("current")
_MainsMonitorFrequencyTrapRepeatCounter_Type = Counter32
_MainsMonitorFrequencyTrapRepeatCounter_Object = MibTableColumn
mainsMonitorFrequencyTrapRepeatCounter = _MainsMonitorFrequencyTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 3),
    _MainsMonitorFrequencyTrapRepeatCounter_Type()
)
mainsMonitorFrequencyTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyTrapRepeatCounter.setStatus("current")


class _MainsMonitorFrequencyAlarmEnable_Type(Integer32):
    """Custom type mainsMonitorFrequencyAlarmEnable based on Integer32"""
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


_MainsMonitorFrequencyAlarmEnable_Type.__name__ = "Integer32"
_MainsMonitorFrequencyAlarmEnable_Object = MibTableColumn
mainsMonitorFrequencyAlarmEnable = _MainsMonitorFrequencyAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 4),
    _MainsMonitorFrequencyAlarmEnable_Type()
)
mainsMonitorFrequencyAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyAlarmEnable.setStatus("current")
_MainsMonitorFrequencyValue_Type = Integer32
_MainsMonitorFrequencyValue_Object = MibTableColumn
mainsMonitorFrequencyValue = _MainsMonitorFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 5),
    _MainsMonitorFrequencyValue_Type()
)
mainsMonitorFrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyValue.setStatus("current")
_MainsMonitorFrequencyMajorHighLevel_Type = Integer32
_MainsMonitorFrequencyMajorHighLevel_Object = MibTableColumn
mainsMonitorFrequencyMajorHighLevel = _MainsMonitorFrequencyMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 6),
    _MainsMonitorFrequencyMajorHighLevel_Type()
)
mainsMonitorFrequencyMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMajorHighLevel.setStatus("current")
_MainsMonitorFrequencyMinorHighLevel_Type = Integer32
_MainsMonitorFrequencyMinorHighLevel_Object = MibTableColumn
mainsMonitorFrequencyMinorHighLevel = _MainsMonitorFrequencyMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 7),
    _MainsMonitorFrequencyMinorHighLevel_Type()
)
mainsMonitorFrequencyMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMinorHighLevel.setStatus("current")
_MainsMonitorFrequencyMinorLowLevel_Type = Integer32
_MainsMonitorFrequencyMinorLowLevel_Object = MibTableColumn
mainsMonitorFrequencyMinorLowLevel = _MainsMonitorFrequencyMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 8),
    _MainsMonitorFrequencyMinorLowLevel_Type()
)
mainsMonitorFrequencyMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMinorLowLevel.setStatus("current")
_MainsMonitorFrequencyMajorLowLevel_Type = Integer32
_MainsMonitorFrequencyMajorLowLevel_Object = MibTableColumn
mainsMonitorFrequencyMajorLowLevel = _MainsMonitorFrequencyMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 9),
    _MainsMonitorFrequencyMajorLowLevel_Type()
)
mainsMonitorFrequencyMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMajorLowLevel.setStatus("current")
_MainsMonitorEnergyLogAccumulatedTable_Object = MibTable
mainsMonitorEnergyLogAccumulatedTable = _MainsMonitorEnergyLogAccumulatedTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 6)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogAccumulatedTable.setStatus("current")
_MainsMonitorEnergyLogAccumulatedEntry_Object = MibTableRow
mainsMonitorEnergyLogAccumulatedEntry = _MainsMonitorEnergyLogAccumulatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 6, 1)
)
mainsMonitorEnergyLogAccumulatedEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogAccumulatedEntry.setStatus("current")
_MainsMonitorEnergyLogAccumulated_Type = Integer32
_MainsMonitorEnergyLogAccumulated_Object = MibTableColumn
mainsMonitorEnergyLogAccumulated = _MainsMonitorEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 6, 1, 1),
    _MainsMonitorEnergyLogAccumulated_Type()
)
mainsMonitorEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogAccumulated.setStatus("current")


class _MainsMonitorEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsMonitorEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastHoursNumberOfEntries_Object = MibScalar
mainsMonitorEnergyLogLastHoursNumberOfEntries = _MainsMonitorEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 7),
    _MainsMonitorEnergyLogLastHoursNumberOfEntries_Type()
)
mainsMonitorEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursNumberOfEntries.setStatus("current")
_MainsMonitorEnergyLogLastHoursTable_Object = MibTable
mainsMonitorEnergyLogLastHoursTable = _MainsMonitorEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursTable.setStatus("current")
_MainsMonitorEnergyLogLastHoursEntry_Object = MibTableRow
mainsMonitorEnergyLogLastHoursEntry = _MainsMonitorEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8, 1)
)
mainsMonitorEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursEntry.setStatus("current")


class _MainsMonitorEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsMonitorEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastHoursIndex_Object = MibTableColumn
mainsMonitorEnergyLogLastHoursIndex = _MainsMonitorEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8, 1, 1),
    _MainsMonitorEnergyLogLastHoursIndex_Type()
)
mainsMonitorEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursIndex.setStatus("current")
_MainsMonitorEnergyLogLastHoursValue_Type = Integer32
_MainsMonitorEnergyLogLastHoursValue_Object = MibTableColumn
mainsMonitorEnergyLogLastHoursValue = _MainsMonitorEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8, 1, 2),
    _MainsMonitorEnergyLogLastHoursValue_Type()
)
mainsMonitorEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursValue.setStatus("current")


class _MainsMonitorEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsMonitorEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastDaysNumberOfEntries_Object = MibScalar
mainsMonitorEnergyLogLastDaysNumberOfEntries = _MainsMonitorEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 9),
    _MainsMonitorEnergyLogLastDaysNumberOfEntries_Type()
)
mainsMonitorEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysNumberOfEntries.setStatus("current")
_MainsMonitorEnergyLogLastDaysTable_Object = MibTable
mainsMonitorEnergyLogLastDaysTable = _MainsMonitorEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysTable.setStatus("current")
_MainsMonitorEnergyLogLastDaysEntry_Object = MibTableRow
mainsMonitorEnergyLogLastDaysEntry = _MainsMonitorEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10, 1)
)
mainsMonitorEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysEntry.setStatus("current")


class _MainsMonitorEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsMonitorEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastDaysIndex_Object = MibTableColumn
mainsMonitorEnergyLogLastDaysIndex = _MainsMonitorEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10, 1, 1),
    _MainsMonitorEnergyLogLastDaysIndex_Type()
)
mainsMonitorEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysIndex.setStatus("current")
_MainsMonitorEnergyLogLastDaysValue_Type = Integer32
_MainsMonitorEnergyLogLastDaysValue_Object = MibTableColumn
mainsMonitorEnergyLogLastDaysValue = _MainsMonitorEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10, 1, 2),
    _MainsMonitorEnergyLogLastDaysValue_Type()
)
mainsMonitorEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysValue.setStatus("current")


class _MainsMonitorEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsMonitorEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
mainsMonitorEnergyLogLastWeeksNumberOfEntries = _MainsMonitorEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 11),
    _MainsMonitorEnergyLogLastWeeksNumberOfEntries_Type()
)
mainsMonitorEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_MainsMonitorEnergyLogLastWeeksTable_Object = MibTable
mainsMonitorEnergyLogLastWeeksTable = _MainsMonitorEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksTable.setStatus("current")
_MainsMonitorEnergyLogLastWeeksEntry_Object = MibTableRow
mainsMonitorEnergyLogLastWeeksEntry = _MainsMonitorEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12, 1)
)
mainsMonitorEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksEntry.setStatus("current")


class _MainsMonitorEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsMonitorEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastWeeksIndex_Object = MibTableColumn
mainsMonitorEnergyLogLastWeeksIndex = _MainsMonitorEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12, 1, 1),
    _MainsMonitorEnergyLogLastWeeksIndex_Type()
)
mainsMonitorEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksIndex.setStatus("current")
_MainsMonitorEnergyLogLastWeeksValue_Type = Integer32
_MainsMonitorEnergyLogLastWeeksValue_Object = MibTableColumn
mainsMonitorEnergyLogLastWeeksValue = _MainsMonitorEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12, 1, 2),
    _MainsMonitorEnergyLogLastWeeksValue_Type()
)
mainsMonitorEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksValue.setStatus("current")
_MainsOutageLog_ObjectIdentity = ObjectIdentity
mainsOutageLog = _MainsOutageLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6)
)
_MainsOutageTotal_Type = Integer32
_MainsOutageTotal_Object = MibScalar
mainsOutageTotal = _MainsOutageTotal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 1),
    _MainsOutageTotal_Type()
)
mainsOutageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageTotal.setStatus("current")


class _MainsOutageLogDaysNumberOfEntries_Type(Integer32):
    """Custom type mainsOutageLogDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsOutageLogDaysNumberOfEntries_Type.__name__ = "Integer32"
_MainsOutageLogDaysNumberOfEntries_Object = MibScalar
mainsOutageLogDaysNumberOfEntries = _MainsOutageLogDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 2),
    _MainsOutageLogDaysNumberOfEntries_Type()
)
mainsOutageLogDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogDaysNumberOfEntries.setStatus("current")
_MainsOutageLogDaysTable_Object = MibTable
mainsOutageLogDaysTable = _MainsOutageLogDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3)
)
if mibBuilder.loadTexts:
    mainsOutageLogDaysTable.setStatus("current")
_MainsOutageLogDaysEntry_Object = MibTableRow
mainsOutageLogDaysEntry = _MainsOutageLogDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3, 1)
)
mainsOutageLogDaysEntry.setIndexNames(
    (0, "SP2-MIB", "mainsOutageLogDaysIndex"),
)
if mibBuilder.loadTexts:
    mainsOutageLogDaysEntry.setStatus("current")


class _MainsOutageLogDaysIndex_Type(Integer32):
    """Custom type mainsOutageLogDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsOutageLogDaysIndex_Type.__name__ = "Integer32"
_MainsOutageLogDaysIndex_Object = MibTableColumn
mainsOutageLogDaysIndex = _MainsOutageLogDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3, 1, 1),
    _MainsOutageLogDaysIndex_Type()
)
mainsOutageLogDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsOutageLogDaysIndex.setStatus("current")
_MainsOutageLogDaysValue_Type = Integer32
_MainsOutageLogDaysValue_Object = MibTableColumn
mainsOutageLogDaysValue = _MainsOutageLogDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3, 1, 2),
    _MainsOutageLogDaysValue_Type()
)
mainsOutageLogDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogDaysValue.setStatus("current")


class _MainsOutageLogWeeksNumberOfEntries_Type(Integer32):
    """Custom type mainsOutageLogWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsOutageLogWeeksNumberOfEntries_Type.__name__ = "Integer32"
_MainsOutageLogWeeksNumberOfEntries_Object = MibScalar
mainsOutageLogWeeksNumberOfEntries = _MainsOutageLogWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 4),
    _MainsOutageLogWeeksNumberOfEntries_Type()
)
mainsOutageLogWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogWeeksNumberOfEntries.setStatus("current")
_MainsOutageLogWeeksTable_Object = MibTable
mainsOutageLogWeeksTable = _MainsOutageLogWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5)
)
if mibBuilder.loadTexts:
    mainsOutageLogWeeksTable.setStatus("current")
_MainsOutageLogWeeksEntry_Object = MibTableRow
mainsOutageLogWeeksEntry = _MainsOutageLogWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5, 1)
)
mainsOutageLogWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "mainsOutageLogWeeksIndex"),
)
if mibBuilder.loadTexts:
    mainsOutageLogWeeksEntry.setStatus("current")


class _MainsOutageLogWeeksIndex_Type(Integer32):
    """Custom type mainsOutageLogWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsOutageLogWeeksIndex_Type.__name__ = "Integer32"
_MainsOutageLogWeeksIndex_Object = MibTableColumn
mainsOutageLogWeeksIndex = _MainsOutageLogWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5, 1, 1),
    _MainsOutageLogWeeksIndex_Type()
)
mainsOutageLogWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsOutageLogWeeksIndex.setStatus("current")
_MainsOutageLogWeeksValue_Type = Integer32
_MainsOutageLogWeeksValue_Object = MibTableColumn
mainsOutageLogWeeksValue = _MainsOutageLogWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5, 1, 2),
    _MainsOutageLogWeeksValue_Type()
)
mainsOutageLogWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogWeeksValue.setStatus("current")


class _MainsOutageLogMonthsNumberOfEntries_Type(Integer32):
    """Custom type mainsOutageLogMonthsNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsOutageLogMonthsNumberOfEntries_Type.__name__ = "Integer32"
_MainsOutageLogMonthsNumberOfEntries_Object = MibScalar
mainsOutageLogMonthsNumberOfEntries = _MainsOutageLogMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 6),
    _MainsOutageLogMonthsNumberOfEntries_Type()
)
mainsOutageLogMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogMonthsNumberOfEntries.setStatus("current")
_MainsOutageLogMonthsTable_Object = MibTable
mainsOutageLogMonthsTable = _MainsOutageLogMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7)
)
if mibBuilder.loadTexts:
    mainsOutageLogMonthsTable.setStatus("current")
_MainsOutageLogMonthsEntry_Object = MibTableRow
mainsOutageLogMonthsEntry = _MainsOutageLogMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7, 1)
)
mainsOutageLogMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "mainsOutageLogMonthsIndex"),
)
if mibBuilder.loadTexts:
    mainsOutageLogMonthsEntry.setStatus("current")


class _MainsOutageLogMonthsIndex_Type(Integer32):
    """Custom type mainsOutageLogMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsOutageLogMonthsIndex_Type.__name__ = "Integer32"
_MainsOutageLogMonthsIndex_Object = MibTableColumn
mainsOutageLogMonthsIndex = _MainsOutageLogMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7, 1, 1),
    _MainsOutageLogMonthsIndex_Type()
)
mainsOutageLogMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsOutageLogMonthsIndex.setStatus("current")
_MainsOutageLogMonthsValue_Type = Integer32
_MainsOutageLogMonthsValue_Object = MibTableColumn
mainsOutageLogMonthsValue = _MainsOutageLogMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7, 1, 2),
    _MainsOutageLogMonthsValue_Type()
)
mainsOutageLogMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogMonthsValue.setStatus("current")
_Generator_ObjectIdentity = ObjectIdentity
generator = _Generator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4)
)


class _GeneratorStatus_Type(Integer32):
    """Custom type generatorStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_GeneratorStatus_Type.__name__ = "Integer32"
_GeneratorStatus_Object = MibScalar
generatorStatus = _GeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 1),
    _GeneratorStatus_Type()
)
generatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorStatus.setStatus("current")


class _GeneratorFailStatus_Type(Integer32):
    """Custom type generatorFailStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_GeneratorFailStatus_Type.__name__ = "Integer32"
_GeneratorFailStatus_Object = MibScalar
generatorFailStatus = _GeneratorFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 2),
    _GeneratorFailStatus_Type()
)
generatorFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFailStatus.setStatus("current")
_GeneratorActivation_Type = Integer32
_GeneratorActivation_Object = MibScalar
generatorActivation = _GeneratorActivation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 3),
    _GeneratorActivation_Type()
)
generatorActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorActivation.setStatus("current")
_GeneratorDischargeValue_Type = Integer32
_GeneratorDischargeValue_Object = MibScalar
generatorDischargeValue = _GeneratorDischargeValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 4),
    _GeneratorDischargeValue_Type()
)
generatorDischargeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorDischargeValue.setStatus("current")
_GeneratorMainsDelay_Type = Integer32
_GeneratorMainsDelay_Object = MibScalar
generatorMainsDelay = _GeneratorMainsDelay_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 5),
    _GeneratorMainsDelay_Type()
)
generatorMainsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorMainsDelay.setStatus("current")
_GeneratorChargeTime_Type = Integer32
_GeneratorChargeTime_Object = MibScalar
generatorChargeTime = _GeneratorChargeTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 6),
    _GeneratorChargeTime_Type()
)
generatorChargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorChargeTime.setStatus("current")


class _GeneratorCapacityControlledStartStopEnable_Type(Integer32):
    """Custom type generatorCapacityControlledStartStopEnable based on Integer32"""
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


_GeneratorCapacityControlledStartStopEnable_Type.__name__ = "Integer32"
_GeneratorCapacityControlledStartStopEnable_Object = MibScalar
generatorCapacityControlledStartStopEnable = _GeneratorCapacityControlledStartStopEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 7),
    _GeneratorCapacityControlledStartStopEnable_Type()
)
generatorCapacityControlledStartStopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCapacityControlledStartStopEnable.setStatus("current")


class _GeneratorCapacityStartOnDischargeLimit_Type(Integer32):
    """Custom type generatorCapacityStartOnDischargeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeneratorCapacityStartOnDischargeLimit_Type.__name__ = "Integer32"
_GeneratorCapacityStartOnDischargeLimit_Object = MibScalar
generatorCapacityStartOnDischargeLimit = _GeneratorCapacityStartOnDischargeLimit_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 8),
    _GeneratorCapacityStartOnDischargeLimit_Type()
)
generatorCapacityStartOnDischargeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCapacityStartOnDischargeLimit.setStatus("current")


class _GeneratorCapacityStopOnChargeLimit_Type(Integer32):
    """Custom type generatorCapacityStopOnChargeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeneratorCapacityStopOnChargeLimit_Type.__name__ = "Integer32"
_GeneratorCapacityStopOnChargeLimit_Object = MibScalar
generatorCapacityStopOnChargeLimit = _GeneratorCapacityStopOnChargeLimit_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 9),
    _GeneratorCapacityStopOnChargeLimit_Type()
)
generatorCapacityStopOnChargeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCapacityStopOnChargeLimit.setStatus("current")


class _GeneratorCurrentLimitControlledStopEnable_Type(Integer32):
    """Custom type generatorCurrentLimitControlledStopEnable based on Integer32"""
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


_GeneratorCurrentLimitControlledStopEnable_Type.__name__ = "Integer32"
_GeneratorCurrentLimitControlledStopEnable_Object = MibScalar
generatorCurrentLimitControlledStopEnable = _GeneratorCurrentLimitControlledStopEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 10),
    _GeneratorCurrentLimitControlledStopEnable_Type()
)
generatorCurrentLimitControlledStopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCurrentLimitControlledStopEnable.setStatus("current")


class _GeneratorCurrentLimitControlledStopValue_Type(Integer32):
    """Custom type generatorCurrentLimitControlledStopValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeneratorCurrentLimitControlledStopValue_Type.__name__ = "Integer32"
_GeneratorCurrentLimitControlledStopValue_Object = MibScalar
generatorCurrentLimitControlledStopValue = _GeneratorCurrentLimitControlledStopValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 11),
    _GeneratorCurrentLimitControlledStopValue_Type()
)
generatorCurrentLimitControlledStopValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCurrentLimitControlledStopValue.setStatus("current")


class _GeneratorVoltageControlledStartEnable_Type(Integer32):
    """Custom type generatorVoltageControlledStartEnable based on Integer32"""
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


_GeneratorVoltageControlledStartEnable_Type.__name__ = "Integer32"
_GeneratorVoltageControlledStartEnable_Object = MibScalar
generatorVoltageControlledStartEnable = _GeneratorVoltageControlledStartEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 12),
    _GeneratorVoltageControlledStartEnable_Type()
)
generatorVoltageControlledStartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorVoltageControlledStartEnable.setStatus("current")
_GeneratorVoltageControlStartVoltage_Type = Integer32
_GeneratorVoltageControlStartVoltage_Object = MibScalar
generatorVoltageControlStartVoltage = _GeneratorVoltageControlStartVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 13),
    _GeneratorVoltageControlStartVoltage_Type()
)
generatorVoltageControlStartVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorVoltageControlStartVoltage.setStatus("current")
_GeneratorVoltageControlStopAfter_Type = Integer32
_GeneratorVoltageControlStopAfter_Object = MibScalar
generatorVoltageControlStopAfter = _GeneratorVoltageControlStopAfter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 14),
    _GeneratorVoltageControlStopAfter_Type()
)
generatorVoltageControlStopAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorVoltageControlStopAfter.setStatus("current")


class _GeneratorDailyRunEnable_Type(Integer32):
    """Custom type generatorDailyRunEnable based on Integer32"""
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


_GeneratorDailyRunEnable_Type.__name__ = "Integer32"
_GeneratorDailyRunEnable_Object = MibScalar
generatorDailyRunEnable = _GeneratorDailyRunEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 15),
    _GeneratorDailyRunEnable_Type()
)
generatorDailyRunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorDailyRunEnable.setStatus("current")
_GeneratorDailyRunSetupTable_Object = MibTable
generatorDailyRunSetupTable = _GeneratorDailyRunSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16)
)
if mibBuilder.loadTexts:
    generatorDailyRunSetupTable.setStatus("current")
_GeneratorDailyRunSetupEntry_Object = MibTableRow
generatorDailyRunSetupEntry = _GeneratorDailyRunSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1)
)
generatorDailyRunSetupEntry.setIndexNames(
    (0, "SP2-MIB", "generatorDailyRunDayIndex"),
)
if mibBuilder.loadTexts:
    generatorDailyRunSetupEntry.setStatus("current")


class _GeneratorDailyRunDayIndex_Type(Integer32):
    """Custom type generatorDailyRunDayIndex based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_GeneratorDailyRunDayIndex_Type.__name__ = "Integer32"
_GeneratorDailyRunDayIndex_Object = MibTableColumn
generatorDailyRunDayIndex = _GeneratorDailyRunDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1, 1),
    _GeneratorDailyRunDayIndex_Type()
)
generatorDailyRunDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorDailyRunDayIndex.setStatus("current")


class _GeneratorDailyRunStartHour_Type(Integer32):
    """Custom type generatorDailyRunStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GeneratorDailyRunStartHour_Type.__name__ = "Integer32"
_GeneratorDailyRunStartHour_Object = MibTableColumn
generatorDailyRunStartHour = _GeneratorDailyRunStartHour_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1, 2),
    _GeneratorDailyRunStartHour_Type()
)
generatorDailyRunStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorDailyRunStartHour.setStatus("current")


class _GeneratorDailyRunStopHour_Type(Integer32):
    """Custom type generatorDailyRunStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GeneratorDailyRunStopHour_Type.__name__ = "Integer32"
_GeneratorDailyRunStopHour_Object = MibTableColumn
generatorDailyRunStopHour = _GeneratorDailyRunStopHour_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1, 3),
    _GeneratorDailyRunStopHour_Type()
)
generatorDailyRunStopHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorDailyRunStopHour.setStatus("current")


class _GeneratorMonthlyRunEnable_Type(Integer32):
    """Custom type generatorMonthlyRunEnable based on Integer32"""
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


_GeneratorMonthlyRunEnable_Type.__name__ = "Integer32"
_GeneratorMonthlyRunEnable_Object = MibScalar
generatorMonthlyRunEnable = _GeneratorMonthlyRunEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 17),
    _GeneratorMonthlyRunEnable_Type()
)
generatorMonthlyRunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunEnable.setStatus("current")


class _GeneratorMonthlyRunStartTime_Type(Integer32):
    """Custom type generatorMonthlyRunStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GeneratorMonthlyRunStartTime_Type.__name__ = "Integer32"
_GeneratorMonthlyRunStartTime_Object = MibScalar
generatorMonthlyRunStartTime = _GeneratorMonthlyRunStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 18),
    _GeneratorMonthlyRunStartTime_Type()
)
generatorMonthlyRunStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunStartTime.setStatus("current")


class _GeneratorMonthlyRunStartDayinMonth1_Type(Integer32):
    """Custom type generatorMonthlyRunStartDayinMonth1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_GeneratorMonthlyRunStartDayinMonth1_Type.__name__ = "Integer32"
_GeneratorMonthlyRunStartDayinMonth1_Object = MibScalar
generatorMonthlyRunStartDayinMonth1 = _GeneratorMonthlyRunStartDayinMonth1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 19),
    _GeneratorMonthlyRunStartDayinMonth1_Type()
)
generatorMonthlyRunStartDayinMonth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunStartDayinMonth1.setStatus("current")


class _GeneratorMonthlyRunStartDayinMonth2_Type(Integer32):
    """Custom type generatorMonthlyRunStartDayinMonth2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_GeneratorMonthlyRunStartDayinMonth2_Type.__name__ = "Integer32"
_GeneratorMonthlyRunStartDayinMonth2_Object = MibScalar
generatorMonthlyRunStartDayinMonth2 = _GeneratorMonthlyRunStartDayinMonth2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 20),
    _GeneratorMonthlyRunStartDayinMonth2_Type()
)
generatorMonthlyRunStartDayinMonth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunStartDayinMonth2.setStatus("current")


class _GeneratorTankNumberOfTanks_Type(Integer32):
    """Custom type generatorTankNumberOfTanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeneratorTankNumberOfTanks_Type.__name__ = "Integer32"
_GeneratorTankNumberOfTanks_Object = MibScalar
generatorTankNumberOfTanks = _GeneratorTankNumberOfTanks_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 21),
    _GeneratorTankNumberOfTanks_Type()
)
generatorTankNumberOfTanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorTankNumberOfTanks.setStatus("current")
_GeneratorTankTable_Object = MibTable
generatorTankTable = _GeneratorTankTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22)
)
if mibBuilder.loadTexts:
    generatorTankTable.setStatus("current")
_GeneratorTankEntry_Object = MibTableRow
generatorTankEntry = _GeneratorTankEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1)
)
generatorTankEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
)
if mibBuilder.loadTexts:
    generatorTankEntry.setStatus("current")


class _GeneratorTankIndex_Type(Integer32):
    """Custom type generatorTankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GeneratorTankIndex_Type.__name__ = "Integer32"
_GeneratorTankIndex_Object = MibTableColumn
generatorTankIndex = _GeneratorTankIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 1),
    _GeneratorTankIndex_Type()
)
generatorTankIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorTankIndex.setStatus("current")


class _GeneratorTankStatus_Type(Integer32):
    """Custom type generatorTankStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_GeneratorTankStatus_Type.__name__ = "Integer32"
_GeneratorTankStatus_Object = MibTableColumn
generatorTankStatus = _GeneratorTankStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 2),
    _GeneratorTankStatus_Type()
)
generatorTankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorTankStatus.setStatus("current")


class _GeneratorTankDescription_Type(DisplayString):
    """Custom type generatorTankDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GeneratorTankDescription_Type.__name__ = "DisplayString"
_GeneratorTankDescription_Object = MibTableColumn
generatorTankDescription = _GeneratorTankDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 3),
    _GeneratorTankDescription_Type()
)
generatorTankDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankDescription.setStatus("current")
_GeneratorTankTrapRepeatCounter_Type = Counter32
_GeneratorTankTrapRepeatCounter_Object = MibTableColumn
generatorTankTrapRepeatCounter = _GeneratorTankTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 4),
    _GeneratorTankTrapRepeatCounter_Type()
)
generatorTankTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    generatorTankTrapRepeatCounter.setStatus("current")


class _GeneratorTankEnable_Type(Integer32):
    """Custom type generatorTankEnable based on Integer32"""
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


_GeneratorTankEnable_Type.__name__ = "Integer32"
_GeneratorTankEnable_Object = MibTableColumn
generatorTankEnable = _GeneratorTankEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 5),
    _GeneratorTankEnable_Type()
)
generatorTankEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankEnable.setStatus("current")
_GeneratorTankValue_Type = Integer32
_GeneratorTankValue_Object = MibTableColumn
generatorTankValue = _GeneratorTankValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 6),
    _GeneratorTankValue_Type()
)
generatorTankValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorTankValue.setStatus("current")
_GeneratorTankMajorHighLevel_Type = Integer32
_GeneratorTankMajorHighLevel_Object = MibTableColumn
generatorTankMajorHighLevel = _GeneratorTankMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 7),
    _GeneratorTankMajorHighLevel_Type()
)
generatorTankMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMajorHighLevel.setStatus("current")
_GeneratorTankMinorHighLevel_Type = Integer32
_GeneratorTankMinorHighLevel_Object = MibTableColumn
generatorTankMinorHighLevel = _GeneratorTankMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 8),
    _GeneratorTankMinorHighLevel_Type()
)
generatorTankMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMinorHighLevel.setStatus("current")
_GeneratorTankMinorLowLevel_Type = Integer32
_GeneratorTankMinorLowLevel_Object = MibTableColumn
generatorTankMinorLowLevel = _GeneratorTankMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 9),
    _GeneratorTankMinorLowLevel_Type()
)
generatorTankMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMinorLowLevel.setStatus("current")
_GeneratorTankMajorLowLevel_Type = Integer32
_GeneratorTankMajorLowLevel_Object = MibTableColumn
generatorTankMajorLowLevel = _GeneratorTankMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 10),
    _GeneratorTankMajorLowLevel_Type()
)
generatorTankMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMajorLowLevel.setStatus("current")
_GeneratorEnergyLog_ObjectIdentity = ObjectIdentity
generatorEnergyLog = _GeneratorEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23)
)
_GeneratorEnergyLogAccumulated_Type = Integer32
_GeneratorEnergyLogAccumulated_Object = MibScalar
generatorEnergyLogAccumulated = _GeneratorEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 1),
    _GeneratorEnergyLogAccumulated_Type()
)
generatorEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogAccumulated.setStatus("current")


class _GeneratorEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type generatorEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastHoursNumberOfEntries_Object = MibScalar
generatorEnergyLogLastHoursNumberOfEntries = _GeneratorEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 2),
    _GeneratorEnergyLogLastHoursNumberOfEntries_Type()
)
generatorEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursNumberOfEntries.setStatus("current")
_GeneratorEnergyLogLastHoursTable_Object = MibTable
generatorEnergyLogLastHoursTable = _GeneratorEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3)
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursTable.setStatus("current")
_GeneratorEnergyLogLastHoursEntry_Object = MibTableRow
generatorEnergyLogLastHoursEntry = _GeneratorEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3, 1)
)
generatorEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "generatorEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursEntry.setStatus("current")


class _GeneratorEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type generatorEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastHoursIndex_Object = MibTableColumn
generatorEnergyLogLastHoursIndex = _GeneratorEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3, 1, 1),
    _GeneratorEnergyLogLastHoursIndex_Type()
)
generatorEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursIndex.setStatus("current")
_GeneratorEnergyLogLastHoursValue_Type = Integer32
_GeneratorEnergyLogLastHoursValue_Object = MibTableColumn
generatorEnergyLogLastHoursValue = _GeneratorEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3, 1, 2),
    _GeneratorEnergyLogLastHoursValue_Type()
)
generatorEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursValue.setStatus("current")


class _GeneratorEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type generatorEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastDaysNumberOfEntries_Object = MibScalar
generatorEnergyLogLastDaysNumberOfEntries = _GeneratorEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 4),
    _GeneratorEnergyLogLastDaysNumberOfEntries_Type()
)
generatorEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysNumberOfEntries.setStatus("current")
_GeneratorEnergyLogLastDaysTable_Object = MibTable
generatorEnergyLogLastDaysTable = _GeneratorEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5)
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysTable.setStatus("current")
_GeneratorEnergyLogLastDaysEntry_Object = MibTableRow
generatorEnergyLogLastDaysEntry = _GeneratorEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5, 1)
)
generatorEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "generatorEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysEntry.setStatus("current")


class _GeneratorEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type generatorEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastDaysIndex_Object = MibTableColumn
generatorEnergyLogLastDaysIndex = _GeneratorEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5, 1, 1),
    _GeneratorEnergyLogLastDaysIndex_Type()
)
generatorEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysIndex.setStatus("current")
_GeneratorEnergyLogLastDaysValue_Type = Integer32
_GeneratorEnergyLogLastDaysValue_Object = MibTableColumn
generatorEnergyLogLastDaysValue = _GeneratorEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5, 1, 2),
    _GeneratorEnergyLogLastDaysValue_Type()
)
generatorEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysValue.setStatus("current")


class _GeneratorEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type generatorEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
generatorEnergyLogLastWeeksNumberOfEntries = _GeneratorEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 6),
    _GeneratorEnergyLogLastWeeksNumberOfEntries_Type()
)
generatorEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_GeneratorEnergyLogLastWeeksTable_Object = MibTable
generatorEnergyLogLastWeeksTable = _GeneratorEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7)
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksTable.setStatus("current")
_GeneratorEnergyLogLastWeeksEntry_Object = MibTableRow
generatorEnergyLogLastWeeksEntry = _GeneratorEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7, 1)
)
generatorEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "generatorEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksEntry.setStatus("current")


class _GeneratorEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type generatorEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastWeeksIndex_Object = MibTableColumn
generatorEnergyLogLastWeeksIndex = _GeneratorEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7, 1, 1),
    _GeneratorEnergyLogLastWeeksIndex_Type()
)
generatorEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksIndex.setStatus("current")
_GeneratorEnergyLogLastWeeksValue_Type = Integer32
_GeneratorEnergyLogLastWeeksValue_Object = MibTableColumn
generatorEnergyLogLastWeeksValue = _GeneratorEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7, 1, 2),
    _GeneratorEnergyLogLastWeeksValue_Type()
)
generatorEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksValue.setStatus("current")
_GeneratorRunHoursLog_ObjectIdentity = ObjectIdentity
generatorRunHoursLog = _GeneratorRunHoursLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24)
)
_GeneratorRunHoursTotalHours_Type = Integer32
_GeneratorRunHoursTotalHours_Object = MibScalar
generatorRunHoursTotalHours = _GeneratorRunHoursTotalHours_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 1),
    _GeneratorRunHoursTotalHours_Type()
)
generatorRunHoursTotalHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursTotalHours.setStatus("current")


class _GeneratorRunHoursLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type generatorRunHoursLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorRunHoursLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastDaysNumberOfEntries_Object = MibScalar
generatorRunHoursLogLastDaysNumberOfEntries = _GeneratorRunHoursLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 2),
    _GeneratorRunHoursLogLastDaysNumberOfEntries_Type()
)
generatorRunHoursLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysNumberOfEntries.setStatus("current")
_GeneratorRunHoursLogLastDaysTable_Object = MibTable
generatorRunHoursLogLastDaysTable = _GeneratorRunHoursLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3)
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysTable.setStatus("current")
_GeneratorRunHoursLogLastDaysEntry_Object = MibTableRow
generatorRunHoursLogLastDaysEntry = _GeneratorRunHoursLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3, 1)
)
generatorRunHoursLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "generatorRunHoursLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysEntry.setStatus("current")


class _GeneratorRunHoursLogLastDaysIndex_Type(Integer32):
    """Custom type generatorRunHoursLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorRunHoursLogLastDaysIndex_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastDaysIndex_Object = MibTableColumn
generatorRunHoursLogLastDaysIndex = _GeneratorRunHoursLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3, 1, 1),
    _GeneratorRunHoursLogLastDaysIndex_Type()
)
generatorRunHoursLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysIndex.setStatus("current")
_GeneratorRunHoursLogLastDaysValue_Type = Integer32
_GeneratorRunHoursLogLastDaysValue_Object = MibTableColumn
generatorRunHoursLogLastDaysValue = _GeneratorRunHoursLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3, 1, 2),
    _GeneratorRunHoursLogLastDaysValue_Type()
)
generatorRunHoursLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysValue.setStatus("current")


class _GeneratorRunHoursLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type generatorRunHoursLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorRunHoursLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastWeeksNumberOfEntries_Object = MibScalar
generatorRunHoursLogLastWeeksNumberOfEntries = _GeneratorRunHoursLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 4),
    _GeneratorRunHoursLogLastWeeksNumberOfEntries_Type()
)
generatorRunHoursLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksNumberOfEntries.setStatus("current")
_GeneratorRunHoursLogLastWeeksTable_Object = MibTable
generatorRunHoursLogLastWeeksTable = _GeneratorRunHoursLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5)
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksTable.setStatus("current")
_GeneratorRunHoursLogLastWeeksEntry_Object = MibTableRow
generatorRunHoursLogLastWeeksEntry = _GeneratorRunHoursLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5, 1)
)
generatorRunHoursLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "generatorRunHoursLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksEntry.setStatus("current")


class _GeneratorRunHoursLogLastWeeksIndex_Type(Integer32):
    """Custom type generatorRunHoursLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorRunHoursLogLastWeeksIndex_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastWeeksIndex_Object = MibTableColumn
generatorRunHoursLogLastWeeksIndex = _GeneratorRunHoursLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5, 1, 1),
    _GeneratorRunHoursLogLastWeeksIndex_Type()
)
generatorRunHoursLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksIndex.setStatus("current")
_GeneratorRunHoursLogLastWeeksValue_Type = Integer32
_GeneratorRunHoursLogLastWeeksValue_Object = MibTableColumn
generatorRunHoursLogLastWeeksValue = _GeneratorRunHoursLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5, 1, 2),
    _GeneratorRunHoursLogLastWeeksValue_Type()
)
generatorRunHoursLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksValue.setStatus("current")


class _GeneratorRunHoursLogLastMonthsNumberOfEntries_Type(Integer32):
    """Custom type generatorRunHoursLogLastMonthsNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorRunHoursLogLastMonthsNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastMonthsNumberOfEntries_Object = MibScalar
generatorRunHoursLogLastMonthsNumberOfEntries = _GeneratorRunHoursLogLastMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 6),
    _GeneratorRunHoursLogLastMonthsNumberOfEntries_Type()
)
generatorRunHoursLogLastMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsNumberOfEntries.setStatus("current")
_GeneratorRunHoursLogLastMonthsTable_Object = MibTable
generatorRunHoursLogLastMonthsTable = _GeneratorRunHoursLogLastMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7)
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsTable.setStatus("current")
_GeneratorRunHoursLogLastMonthsEntry_Object = MibTableRow
generatorRunHoursLogLastMonthsEntry = _GeneratorRunHoursLogLastMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7, 1)
)
generatorRunHoursLogLastMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "generatorRunHoursLogLastMonthsIndex"),
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsEntry.setStatus("current")


class _GeneratorRunHoursLogLastMonthsIndex_Type(Integer32):
    """Custom type generatorRunHoursLogLastMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorRunHoursLogLastMonthsIndex_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastMonthsIndex_Object = MibTableColumn
generatorRunHoursLogLastMonthsIndex = _GeneratorRunHoursLogLastMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7, 1, 1),
    _GeneratorRunHoursLogLastMonthsIndex_Type()
)
generatorRunHoursLogLastMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsIndex.setStatus("current")
_GeneratorRunHoursLogLastMonthsValue_Type = Integer32
_GeneratorRunHoursLogLastMonthsValue_Object = MibTableColumn
generatorRunHoursLogLastMonthsValue = _GeneratorRunHoursLogLastMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7, 1, 2),
    _GeneratorRunHoursLogLastMonthsValue_Type()
)
generatorRunHoursLogLastMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsValue.setStatus("current")
_GeneratorFuelConsumptionLog_ObjectIdentity = ObjectIdentity
generatorFuelConsumptionLog = _GeneratorFuelConsumptionLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25)
)
_GeneratorFuelConsumptionTotalUsedTable_Object = MibTable
generatorFuelConsumptionTotalUsedTable = _GeneratorFuelConsumptionTotalUsedTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 1)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionTotalUsedTable.setStatus("current")
_GeneratorFuelConsumptionTotalUsedEntry_Object = MibTableRow
generatorFuelConsumptionTotalUsedEntry = _GeneratorFuelConsumptionTotalUsedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 1, 1)
)
generatorFuelConsumptionTotalUsedEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionTotalUsedEntry.setStatus("current")
_GeneratorFuelConsumptionTotalUsed_Type = Integer32
_GeneratorFuelConsumptionTotalUsed_Object = MibTableColumn
generatorFuelConsumptionTotalUsed = _GeneratorFuelConsumptionTotalUsed_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 1, 1, 1),
    _GeneratorFuelConsumptionTotalUsed_Type()
)
generatorFuelConsumptionTotalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionTotalUsed.setStatus("current")


class _GeneratorFuelConsumptionLogLastHoursNoOfEntries_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastHoursNoOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorFuelConsumptionLogLastHoursNoOfEntries_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastHoursNoOfEntries_Object = MibScalar
generatorFuelConsumptionLogLastHoursNoOfEntries = _GeneratorFuelConsumptionLogLastHoursNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 2),
    _GeneratorFuelConsumptionLogLastHoursNoOfEntries_Type()
)
generatorFuelConsumptionLogLastHoursNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastHoursNoOfEntries.setStatus("current")
_GeneratorFuelConsumptionLogLastHoursTable_Object = MibTable
generatorFuelConsumptionLogLastHoursTable = _GeneratorFuelConsumptionLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastHoursTable.setStatus("current")
_GeneratorFuelConsumptionLogLastHoursEntry_Object = MibTableRow
generatorFuelConsumptionLogLastHoursEntry = _GeneratorFuelConsumptionLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3, 1)
)
generatorFuelConsumptionLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
    (0, "SP2-MIB", "generatorFuelConsumptionLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastHoursEntry.setStatus("current")


class _GeneratorFuelConsumptionLogLastHoursIndex_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorFuelConsumptionLogLastHoursIndex_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastHoursIndex_Object = MibTableColumn
generatorFuelConsumptionLogLastHoursIndex = _GeneratorFuelConsumptionLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3, 1, 1),
    _GeneratorFuelConsumptionLogLastHoursIndex_Type()
)
generatorFuelConsumptionLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastHoursIndex.setStatus("current")
_GeneratorFuelConsumptionLogLastHoursValue_Type = Integer32
_GeneratorFuelConsumptionLogLastHoursValue_Object = MibTableColumn
generatorFuelConsumptionLogLastHoursValue = _GeneratorFuelConsumptionLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3, 1, 2),
    _GeneratorFuelConsumptionLogLastHoursValue_Type()
)
generatorFuelConsumptionLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastHoursValue.setStatus("current")


class _GeneratorFuelConsumptionLogLastDaysNoOfEntries_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastDaysNoOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorFuelConsumptionLogLastDaysNoOfEntries_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastDaysNoOfEntries_Object = MibScalar
generatorFuelConsumptionLogLastDaysNoOfEntries = _GeneratorFuelConsumptionLogLastDaysNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 4),
    _GeneratorFuelConsumptionLogLastDaysNoOfEntries_Type()
)
generatorFuelConsumptionLogLastDaysNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysNoOfEntries.setStatus("current")
_GeneratorFuelConsumptionLogLastDaysTable_Object = MibTable
generatorFuelConsumptionLogLastDaysTable = _GeneratorFuelConsumptionLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysTable.setStatus("current")
_GeneratorFuelConsumptionLogLastDaysEntry_Object = MibTableRow
generatorFuelConsumptionLogLastDaysEntry = _GeneratorFuelConsumptionLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5, 1)
)
generatorFuelConsumptionLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
    (0, "SP2-MIB", "generatorFuelConsumptionLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysEntry.setStatus("current")


class _GeneratorFuelConsumptionLogLastDaysIndex_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorFuelConsumptionLogLastDaysIndex_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastDaysIndex_Object = MibTableColumn
generatorFuelConsumptionLogLastDaysIndex = _GeneratorFuelConsumptionLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5, 1, 1),
    _GeneratorFuelConsumptionLogLastDaysIndex_Type()
)
generatorFuelConsumptionLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysIndex.setStatus("current")
_GeneratorFuelConsumptionLogLastDaysValue_Type = Integer32
_GeneratorFuelConsumptionLogLastDaysValue_Object = MibTableColumn
generatorFuelConsumptionLogLastDaysValue = _GeneratorFuelConsumptionLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5, 1, 2),
    _GeneratorFuelConsumptionLogLastDaysValue_Type()
)
generatorFuelConsumptionLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysValue.setStatus("current")


class _GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastWeeksNoOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Object = MibScalar
generatorFuelConsumptionLogLastWeeksNoOfEntries = _GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 6),
    _GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Type()
)
generatorFuelConsumptionLogLastWeeksNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksNoOfEntries.setStatus("current")
_GeneratorFuelConsumptionLogLastWeeksTable_Object = MibTable
generatorFuelConsumptionLogLastWeeksTable = _GeneratorFuelConsumptionLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksTable.setStatus("current")
_GeneratorFuelConsumptionLogLastWeeksEntry_Object = MibTableRow
generatorFuelConsumptionLogLastWeeksEntry = _GeneratorFuelConsumptionLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7, 1)
)
generatorFuelConsumptionLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
    (0, "SP2-MIB", "generatorFuelConsumptionLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksEntry.setStatus("current")


class _GeneratorFuelConsumptionLogLastWeeksIndex_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorFuelConsumptionLogLastWeeksIndex_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastWeeksIndex_Object = MibTableColumn
generatorFuelConsumptionLogLastWeeksIndex = _GeneratorFuelConsumptionLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7, 1, 1),
    _GeneratorFuelConsumptionLogLastWeeksIndex_Type()
)
generatorFuelConsumptionLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksIndex.setStatus("current")
_GeneratorFuelConsumptionLogLastWeeksValue_Type = Integer32
_GeneratorFuelConsumptionLogLastWeeksValue_Object = MibTableColumn
generatorFuelConsumptionLogLastWeeksValue = _GeneratorFuelConsumptionLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7, 1, 2),
    _GeneratorFuelConsumptionLogLastWeeksValue_Type()
)
generatorFuelConsumptionLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksValue.setStatus("current")
_Rectifiers_ObjectIdentity = ObjectIdentity
rectifiers = _Rectifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5)
)


class _RectifiersStatus_Type(Integer32):
    """Custom type rectifiersStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_RectifiersStatus_Type.__name__ = "Integer32"
_RectifiersStatus_Object = MibScalar
rectifiersStatus = _RectifiersStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 1),
    _RectifiersStatus_Type()
)
rectifiersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersStatus.setStatus("current")
_RectifiersCurrent_ObjectIdentity = ObjectIdentity
rectifiersCurrent = _RectifiersCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2)
)


class _RectifiersCurrentStatus_Type(Integer32):
    """Custom type rectifiersCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_RectifiersCurrentStatus_Type.__name__ = "Integer32"
_RectifiersCurrentStatus_Object = MibScalar
rectifiersCurrentStatus = _RectifiersCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 1),
    _RectifiersCurrentStatus_Type()
)
rectifiersCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCurrentStatus.setStatus("current")


class _RectifiersCurrentDescription_Type(DisplayString):
    """Custom type rectifiersCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifiersCurrentDescription_Type.__name__ = "DisplayString"
_RectifiersCurrentDescription_Object = MibScalar
rectifiersCurrentDescription = _RectifiersCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 2),
    _RectifiersCurrentDescription_Type()
)
rectifiersCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentDescription.setStatus("current")
_RectifiersCurrentTrapRepeatCounter_Type = Counter32
_RectifiersCurrentTrapRepeatCounter_Object = MibScalar
rectifiersCurrentTrapRepeatCounter = _RectifiersCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 3),
    _RectifiersCurrentTrapRepeatCounter_Type()
)
rectifiersCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifiersCurrentTrapRepeatCounter.setStatus("current")


class _RectifiersCurrentAlarmEnable_Type(Integer32):
    """Custom type rectifiersCurrentAlarmEnable based on Integer32"""
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


_RectifiersCurrentAlarmEnable_Type.__name__ = "Integer32"
_RectifiersCurrentAlarmEnable_Object = MibScalar
rectifiersCurrentAlarmEnable = _RectifiersCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 4),
    _RectifiersCurrentAlarmEnable_Type()
)
rectifiersCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentAlarmEnable.setStatus("current")
_RectifiersCurrentValue_Type = Integer32
_RectifiersCurrentValue_Object = MibScalar
rectifiersCurrentValue = _RectifiersCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 5),
    _RectifiersCurrentValue_Type()
)
rectifiersCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCurrentValue.setStatus("current")
_RectifiersCurrentMajorAlarmLevel_Type = Integer32
_RectifiersCurrentMajorAlarmLevel_Object = MibScalar
rectifiersCurrentMajorAlarmLevel = _RectifiersCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 6),
    _RectifiersCurrentMajorAlarmLevel_Type()
)
rectifiersCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentMajorAlarmLevel.setStatus("current")
_RectifiersCurrentMinorAlarmLevel_Type = Integer32
_RectifiersCurrentMinorAlarmLevel_Object = MibScalar
rectifiersCurrentMinorAlarmLevel = _RectifiersCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 7),
    _RectifiersCurrentMinorAlarmLevel_Type()
)
rectifiersCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentMinorAlarmLevel.setStatus("current")
_RectifiersCapacity_ObjectIdentity = ObjectIdentity
rectifiersCapacity = _RectifiersCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3)
)


class _RectifiersCapacityStatus_Type(Integer32):
    """Custom type rectifiersCapacityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_RectifiersCapacityStatus_Type.__name__ = "Integer32"
_RectifiersCapacityStatus_Object = MibScalar
rectifiersCapacityStatus = _RectifiersCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 1),
    _RectifiersCapacityStatus_Type()
)
rectifiersCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCapacityStatus.setStatus("current")


class _RectifiersCapacityDescription_Type(DisplayString):
    """Custom type rectifiersCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifiersCapacityDescription_Type.__name__ = "DisplayString"
_RectifiersCapacityDescription_Object = MibScalar
rectifiersCapacityDescription = _RectifiersCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 2),
    _RectifiersCapacityDescription_Type()
)
rectifiersCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityDescription.setStatus("current")
_RectifiersCapacityTrapRepeatCounter_Type = Counter32
_RectifiersCapacityTrapRepeatCounter_Object = MibScalar
rectifiersCapacityTrapRepeatCounter = _RectifiersCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 3),
    _RectifiersCapacityTrapRepeatCounter_Type()
)
rectifiersCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifiersCapacityTrapRepeatCounter.setStatus("current")


class _RectifiersCapacityAlarmEnable_Type(Integer32):
    """Custom type rectifiersCapacityAlarmEnable based on Integer32"""
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


_RectifiersCapacityAlarmEnable_Type.__name__ = "Integer32"
_RectifiersCapacityAlarmEnable_Object = MibScalar
rectifiersCapacityAlarmEnable = _RectifiersCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 4),
    _RectifiersCapacityAlarmEnable_Type()
)
rectifiersCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityAlarmEnable.setStatus("current")
_RectifiersCapacityValue_Type = Integer32
_RectifiersCapacityValue_Object = MibScalar
rectifiersCapacityValue = _RectifiersCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 5),
    _RectifiersCapacityValue_Type()
)
rectifiersCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCapacityValue.setStatus("current")
_RectifiersCapacityMajorAlarmLevel_Type = Integer32
_RectifiersCapacityMajorAlarmLevel_Object = MibScalar
rectifiersCapacityMajorAlarmLevel = _RectifiersCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 6),
    _RectifiersCapacityMajorAlarmLevel_Type()
)
rectifiersCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityMajorAlarmLevel.setStatus("current")
_RectifiersCapacityMinorAlarmLevel_Type = Integer32
_RectifiersCapacityMinorAlarmLevel_Object = MibScalar
rectifiersCapacityMinorAlarmLevel = _RectifiersCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 7),
    _RectifiersCapacityMinorAlarmLevel_Type()
)
rectifiersCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityMinorAlarmLevel.setStatus("current")
_RectifiersError_ObjectIdentity = ObjectIdentity
rectifiersError = _RectifiersError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4)
)


class _RectifiersErrorStatus_Type(Integer32):
    """Custom type rectifiersErrorStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_RectifiersErrorStatus_Type.__name__ = "Integer32"
_RectifiersErrorStatus_Object = MibScalar
rectifiersErrorStatus = _RectifiersErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 1),
    _RectifiersErrorStatus_Type()
)
rectifiersErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersErrorStatus.setStatus("current")


class _RectifiersErrorDescription_Type(DisplayString):
    """Custom type rectifiersErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifiersErrorDescription_Type.__name__ = "DisplayString"
_RectifiersErrorDescription_Object = MibScalar
rectifiersErrorDescription = _RectifiersErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 2),
    _RectifiersErrorDescription_Type()
)
rectifiersErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorDescription.setStatus("current")
_RectifiersErrorTrapRepeatCounter_Type = Counter32
_RectifiersErrorTrapRepeatCounter_Object = MibScalar
rectifiersErrorTrapRepeatCounter = _RectifiersErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 3),
    _RectifiersErrorTrapRepeatCounter_Type()
)
rectifiersErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifiersErrorTrapRepeatCounter.setStatus("current")


class _RectifiersErrorEnable_Type(Integer32):
    """Custom type rectifiersErrorEnable based on Integer32"""
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


_RectifiersErrorEnable_Type.__name__ = "Integer32"
_RectifiersErrorEnable_Object = MibScalar
rectifiersErrorEnable = _RectifiersErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 4),
    _RectifiersErrorEnable_Type()
)
rectifiersErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorEnable.setStatus("current")
_RectifiersErrorValue_Type = Integer32
_RectifiersErrorValue_Object = MibScalar
rectifiersErrorValue = _RectifiersErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 5),
    _RectifiersErrorValue_Type()
)
rectifiersErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersErrorValue.setStatus("current")
_RectifiersErrorMajorAlarmLevel_Type = Integer32
_RectifiersErrorMajorAlarmLevel_Object = MibScalar
rectifiersErrorMajorAlarmLevel = _RectifiersErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 6),
    _RectifiersErrorMajorAlarmLevel_Type()
)
rectifiersErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorMajorAlarmLevel.setStatus("current")
_RectifiersErrorMinorAlarmLevel_Type = Integer32
_RectifiersErrorMinorAlarmLevel_Object = MibScalar
rectifiersErrorMinorAlarmLevel = _RectifiersErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 7),
    _RectifiersErrorMinorAlarmLevel_Type()
)
rectifiersErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorMinorAlarmLevel.setStatus("current")


class _RectifiersNumberOfRectifiers_Type(Integer32):
    """Custom type rectifiersNumberOfRectifiers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RectifiersNumberOfRectifiers_Type.__name__ = "Integer32"
_RectifiersNumberOfRectifiers_Object = MibScalar
rectifiersNumberOfRectifiers = _RectifiersNumberOfRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 5),
    _RectifiersNumberOfRectifiers_Type()
)
rectifiersNumberOfRectifiers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersNumberOfRectifiers.setStatus("current")
_RectifierTable_Object = MibTable
rectifierTable = _RectifierTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6)
)
if mibBuilder.loadTexts:
    rectifierTable.setStatus("current")
_RectifierEntry_Object = MibTableRow
rectifierEntry = _RectifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1)
)
rectifierEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierIndex"),
)
if mibBuilder.loadTexts:
    rectifierEntry.setStatus("current")


class _RectifierIndex_Type(Integer32):
    """Custom type rectifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RectifierIndex_Type.__name__ = "Integer32"
_RectifierIndex_Object = MibTableColumn
rectifierIndex = _RectifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 1),
    _RectifierIndex_Type()
)
rectifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifierIndex.setStatus("current")


class _RectifierStatus_Type(Integer32):
    """Custom type rectifierStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_RectifierStatus_Type.__name__ = "Integer32"
_RectifierStatus_Object = MibTableColumn
rectifierStatus = _RectifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 2),
    _RectifierStatus_Type()
)
rectifierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatus.setStatus("current")
_RectifierOutputCurrentValue_Type = Integer32
_RectifierOutputCurrentValue_Object = MibTableColumn
rectifierOutputCurrentValue = _RectifierOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 3),
    _RectifierOutputCurrentValue_Type()
)
rectifierOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierOutputCurrentValue.setStatus("current")
_RectifierInputVoltageValue_Type = Integer32
_RectifierInputVoltageValue_Object = MibTableColumn
rectifierInputVoltageValue = _RectifierInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 4),
    _RectifierInputVoltageValue_Type()
)
rectifierInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierInputVoltageValue.setStatus("current")


class _RectifierType_Type(DisplayString):
    """Custom type rectifierType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_RectifierType_Type.__name__ = "DisplayString"
_RectifierType_Object = MibTableColumn
rectifierType = _RectifierType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 5),
    _RectifierType_Type()
)
rectifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierType.setStatus("current")


class _RectifierHwPartNumber_Type(DisplayString):
    """Custom type rectifierHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RectifierHwPartNumber_Type.__name__ = "DisplayString"
_RectifierHwPartNumber_Object = MibTableColumn
rectifierHwPartNumber = _RectifierHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 6),
    _RectifierHwPartNumber_Type()
)
rectifierHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierHwPartNumber.setStatus("current")


class _RectifierHwVersion_Type(DisplayString):
    """Custom type rectifierHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RectifierHwVersion_Type.__name__ = "DisplayString"
_RectifierHwVersion_Object = MibTableColumn
rectifierHwVersion = _RectifierHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 7),
    _RectifierHwVersion_Type()
)
rectifierHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierHwVersion.setStatus("current")


class _RectifierSwPartNumber_Type(DisplayString):
    """Custom type rectifierSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RectifierSwPartNumber_Type.__name__ = "DisplayString"
_RectifierSwPartNumber_Object = MibTableColumn
rectifierSwPartNumber = _RectifierSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 8),
    _RectifierSwPartNumber_Type()
)
rectifierSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierSwPartNumber.setStatus("current")


class _RectifierSwVersion_Type(DisplayString):
    """Custom type rectifierSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RectifierSwVersion_Type.__name__ = "DisplayString"
_RectifierSwVersion_Object = MibTableColumn
rectifierSwVersion = _RectifierSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 9),
    _RectifierSwVersion_Type()
)
rectifierSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierSwVersion.setStatus("current")
_RectifiersEnergyLog_ObjectIdentity = ObjectIdentity
rectifiersEnergyLog = _RectifiersEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7)
)
_RectifiersEnergyLogAccumulated_Type = Integer32
_RectifiersEnergyLogAccumulated_Object = MibScalar
rectifiersEnergyLogAccumulated = _RectifiersEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 1),
    _RectifiersEnergyLogAccumulated_Type()
)
rectifiersEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogAccumulated.setStatus("current")


class _RectifiersEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type rectifiersEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_RectifiersEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastHoursNumberOfEntries_Object = MibScalar
rectifiersEnergyLogLastHoursNumberOfEntries = _RectifiersEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 2),
    _RectifiersEnergyLogLastHoursNumberOfEntries_Type()
)
rectifiersEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursNumberOfEntries.setStatus("current")
_RectifiersEnergyLogLastHoursTable_Object = MibTable
rectifiersEnergyLogLastHoursTable = _RectifiersEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3)
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursTable.setStatus("current")
_RectifiersEnergyLogLastHoursEntry_Object = MibTableRow
rectifiersEnergyLogLastHoursEntry = _RectifiersEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3, 1)
)
rectifiersEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "rectifiersEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursEntry.setStatus("current")


class _RectifiersEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type rectifiersEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifiersEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastHoursIndex_Object = MibTableColumn
rectifiersEnergyLogLastHoursIndex = _RectifiersEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3, 1, 1),
    _RectifiersEnergyLogLastHoursIndex_Type()
)
rectifiersEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursIndex.setStatus("current")
_RectifiersEnergyLogLastHoursValue_Type = Integer32
_RectifiersEnergyLogLastHoursValue_Object = MibTableColumn
rectifiersEnergyLogLastHoursValue = _RectifiersEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3, 1, 2),
    _RectifiersEnergyLogLastHoursValue_Type()
)
rectifiersEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursValue.setStatus("current")


class _RectifiersEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type rectifiersEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_RectifiersEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastDaysNumberOfEntries_Object = MibScalar
rectifiersEnergyLogLastDaysNumberOfEntries = _RectifiersEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 4),
    _RectifiersEnergyLogLastDaysNumberOfEntries_Type()
)
rectifiersEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysNumberOfEntries.setStatus("current")
_RectifiersEnergyLogLastDaysTable_Object = MibTable
rectifiersEnergyLogLastDaysTable = _RectifiersEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5)
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysTable.setStatus("current")
_RectifiersEnergyLogLastDaysEntry_Object = MibTableRow
rectifiersEnergyLogLastDaysEntry = _RectifiersEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5, 1)
)
rectifiersEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "rectifiersEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysEntry.setStatus("current")


class _RectifiersEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type rectifiersEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifiersEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastDaysIndex_Object = MibTableColumn
rectifiersEnergyLogLastDaysIndex = _RectifiersEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5, 1, 1),
    _RectifiersEnergyLogLastDaysIndex_Type()
)
rectifiersEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysIndex.setStatus("current")
_RectifiersEnergyLogLastDaysValue_Type = Integer32
_RectifiersEnergyLogLastDaysValue_Object = MibTableColumn
rectifiersEnergyLogLastDaysValue = _RectifiersEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5, 1, 2),
    _RectifiersEnergyLogLastDaysValue_Type()
)
rectifiersEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysValue.setStatus("current")


class _RectifiersEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type rectifiersEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_RectifiersEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
rectifiersEnergyLogLastWeeksNumberOfEntries = _RectifiersEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 6),
    _RectifiersEnergyLogLastWeeksNumberOfEntries_Type()
)
rectifiersEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_RectifiersEnergyLogLastWeeksTable_Object = MibTable
rectifiersEnergyLogLastWeeksTable = _RectifiersEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7)
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksTable.setStatus("current")
_RectifiersEnergyLogLastWeeksEntry_Object = MibTableRow
rectifiersEnergyLogLastWeeksEntry = _RectifiersEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7, 1)
)
rectifiersEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "rectifiersEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksEntry.setStatus("current")


class _RectifiersEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type rectifiersEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifiersEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastWeeksIndex_Object = MibTableColumn
rectifiersEnergyLogLastWeeksIndex = _RectifiersEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7, 1, 1),
    _RectifiersEnergyLogLastWeeksIndex_Type()
)
rectifiersEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksIndex.setStatus("current")
_RectifiersEnergyLogLastWeeksValue_Type = Integer32
_RectifiersEnergyLogLastWeeksValue_Object = MibTableColumn
rectifiersEnergyLogLastWeeksValue = _RectifiersEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7, 1, 2),
    _RectifiersEnergyLogLastWeeksValue_Type()
)
rectifiersEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksValue.setStatus("current")
_Dcdc_ObjectIdentity = ObjectIdentity
dcdc = _Dcdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6)
)


class _DcdcNumberOfGroups_Type(Integer32):
    """Custom type dcdcNumberOfGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfGroups_Type.__name__ = "Integer32"
_DcdcNumberOfGroups_Object = MibScalar
dcdcNumberOfGroups = _DcdcNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 1),
    _DcdcNumberOfGroups_Type()
)
dcdcNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfGroups.setStatus("current")
_DcdcGroupsTable_Object = MibTable
dcdcGroupsTable = _DcdcGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2)
)
if mibBuilder.loadTexts:
    dcdcGroupsTable.setStatus("current")
_DcdcGroupsEntry_Object = MibTableRow
dcdcGroupsEntry = _DcdcGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1)
)
dcdcGroupsEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcGroupsEntry.setStatus("current")


class _DcdcGroupIndex_Type(Integer32):
    """Custom type dcdcGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DcdcGroupIndex_Type.__name__ = "Integer32"
_DcdcGroupIndex_Object = MibTableColumn
dcdcGroupIndex = _DcdcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 1),
    _DcdcGroupIndex_Type()
)
dcdcGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcdcGroupIndex.setStatus("current")


class _DcdcGroupStatus_Type(Integer32):
    """Custom type dcdcGroupStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_DcdcGroupStatus_Type.__name__ = "Integer32"
_DcdcGroupStatus_Object = MibTableColumn
dcdcGroupStatus = _DcdcGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 2),
    _DcdcGroupStatus_Type()
)
dcdcGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcGroupStatus.setStatus("current")
_DcdcGroupNumberOfDcdcConverters_Type = Integer32
_DcdcGroupNumberOfDcdcConverters_Object = MibTableColumn
dcdcGroupNumberOfDcdcConverters = _DcdcGroupNumberOfDcdcConverters_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 3),
    _DcdcGroupNumberOfDcdcConverters_Type()
)
dcdcGroupNumberOfDcdcConverters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcGroupNumberOfDcdcConverters.setStatus("current")
_DcdcGroupOutputVoltage_Type = Integer32
_DcdcGroupOutputVoltage_Object = MibTableColumn
dcdcGroupOutputVoltage = _DcdcGroupOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 4),
    _DcdcGroupOutputVoltage_Type()
)
dcdcGroupOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcGroupOutputVoltage.setStatus("current")


class _DcdcNumberOfCurrents_Type(Integer32):
    """Custom type dcdcNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfCurrents_Type.__name__ = "Integer32"
_DcdcNumberOfCurrents_Object = MibTableColumn
dcdcNumberOfCurrents = _DcdcNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 5),
    _DcdcNumberOfCurrents_Type()
)
dcdcNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfCurrents.setStatus("current")


class _DcdcNumberOfCapacities_Type(Integer32):
    """Custom type dcdcNumberOfCapacities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfCapacities_Type.__name__ = "Integer32"
_DcdcNumberOfCapacities_Object = MibTableColumn
dcdcNumberOfCapacities = _DcdcNumberOfCapacities_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 6),
    _DcdcNumberOfCapacities_Type()
)
dcdcNumberOfCapacities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfCapacities.setStatus("current")


class _DcdcNumberOfAlarms_Type(Integer32):
    """Custom type dcdcNumberOfAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfAlarms_Type.__name__ = "Integer32"
_DcdcNumberOfAlarms_Object = MibTableColumn
dcdcNumberOfAlarms = _DcdcNumberOfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 7),
    _DcdcNumberOfAlarms_Type()
)
dcdcNumberOfAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfAlarms.setStatus("current")
_DcdcCurrentTable_Object = MibTable
dcdcCurrentTable = _DcdcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3)
)
if mibBuilder.loadTexts:
    dcdcCurrentTable.setStatus("current")
_DcdcCurrentEntry_Object = MibTableRow
dcdcCurrentEntry = _DcdcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1)
)
dcdcCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcCurrentEntry.setStatus("current")


class _DcdcCurrentStatus_Type(Integer32):
    """Custom type dcdcCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_DcdcCurrentStatus_Type.__name__ = "Integer32"
_DcdcCurrentStatus_Object = MibTableColumn
dcdcCurrentStatus = _DcdcCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 1),
    _DcdcCurrentStatus_Type()
)
dcdcCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCurrentStatus.setStatus("current")


class _DcdcCurrentDescription_Type(DisplayString):
    """Custom type dcdcCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcdcCurrentDescription_Type.__name__ = "DisplayString"
_DcdcCurrentDescription_Object = MibTableColumn
dcdcCurrentDescription = _DcdcCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 2),
    _DcdcCurrentDescription_Type()
)
dcdcCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentDescription.setStatus("current")
_DcdcCurrentTrapRepeatCounter_Type = Counter32
_DcdcCurrentTrapRepeatCounter_Object = MibTableColumn
dcdcCurrentTrapRepeatCounter = _DcdcCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 3),
    _DcdcCurrentTrapRepeatCounter_Type()
)
dcdcCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dcdcCurrentTrapRepeatCounter.setStatus("current")


class _DcdcCurrentAlarmEnable_Type(Integer32):
    """Custom type dcdcCurrentAlarmEnable based on Integer32"""
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


_DcdcCurrentAlarmEnable_Type.__name__ = "Integer32"
_DcdcCurrentAlarmEnable_Object = MibTableColumn
dcdcCurrentAlarmEnable = _DcdcCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 4),
    _DcdcCurrentAlarmEnable_Type()
)
dcdcCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentAlarmEnable.setStatus("current")
_DcdcCurrentValue_Type = Integer32
_DcdcCurrentValue_Object = MibTableColumn
dcdcCurrentValue = _DcdcCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 5),
    _DcdcCurrentValue_Type()
)
dcdcCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCurrentValue.setStatus("current")
_DcdcCurrentMajorAlarmLevel_Type = Integer32
_DcdcCurrentMajorAlarmLevel_Object = MibTableColumn
dcdcCurrentMajorAlarmLevel = _DcdcCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 6),
    _DcdcCurrentMajorAlarmLevel_Type()
)
dcdcCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentMajorAlarmLevel.setStatus("current")
_DcdcCurrentMinorAlarmLevel_Type = Integer32
_DcdcCurrentMinorAlarmLevel_Object = MibTableColumn
dcdcCurrentMinorAlarmLevel = _DcdcCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 7),
    _DcdcCurrentMinorAlarmLevel_Type()
)
dcdcCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentMinorAlarmLevel.setStatus("current")
_DcdcCapacityTable_Object = MibTable
dcdcCapacityTable = _DcdcCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4)
)
if mibBuilder.loadTexts:
    dcdcCapacityTable.setStatus("current")
_DcdcCapacityEntry_Object = MibTableRow
dcdcCapacityEntry = _DcdcCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1)
)
dcdcCapacityEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcCapacityEntry.setStatus("current")


class _DcdcCapacityStatus_Type(Integer32):
    """Custom type dcdcCapacityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_DcdcCapacityStatus_Type.__name__ = "Integer32"
_DcdcCapacityStatus_Object = MibTableColumn
dcdcCapacityStatus = _DcdcCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 1),
    _DcdcCapacityStatus_Type()
)
dcdcCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCapacityStatus.setStatus("current")


class _DcdcCapacityDescription_Type(DisplayString):
    """Custom type dcdcCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcdcCapacityDescription_Type.__name__ = "DisplayString"
_DcdcCapacityDescription_Object = MibTableColumn
dcdcCapacityDescription = _DcdcCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 2),
    _DcdcCapacityDescription_Type()
)
dcdcCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityDescription.setStatus("current")
_DcdcCapacityTrapRepeatCounter_Type = Counter32
_DcdcCapacityTrapRepeatCounter_Object = MibTableColumn
dcdcCapacityTrapRepeatCounter = _DcdcCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 3),
    _DcdcCapacityTrapRepeatCounter_Type()
)
dcdcCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dcdcCapacityTrapRepeatCounter.setStatus("current")


class _DcdcCapacityAlarmEnable_Type(Integer32):
    """Custom type dcdcCapacityAlarmEnable based on Integer32"""
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


_DcdcCapacityAlarmEnable_Type.__name__ = "Integer32"
_DcdcCapacityAlarmEnable_Object = MibTableColumn
dcdcCapacityAlarmEnable = _DcdcCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 4),
    _DcdcCapacityAlarmEnable_Type()
)
dcdcCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityAlarmEnable.setStatus("current")
_DcdcCapacityValue_Type = Integer32
_DcdcCapacityValue_Object = MibTableColumn
dcdcCapacityValue = _DcdcCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 5),
    _DcdcCapacityValue_Type()
)
dcdcCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCapacityValue.setStatus("current")
_DcdcCapacityMajorAlarmLevel_Type = Integer32
_DcdcCapacityMajorAlarmLevel_Object = MibTableColumn
dcdcCapacityMajorAlarmLevel = _DcdcCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 6),
    _DcdcCapacityMajorAlarmLevel_Type()
)
dcdcCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityMajorAlarmLevel.setStatus("current")
_DcdcCapacityMinorAlarmLevel_Type = Integer32
_DcdcCapacityMinorAlarmLevel_Object = MibTableColumn
dcdcCapacityMinorAlarmLevel = _DcdcCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 7),
    _DcdcCapacityMinorAlarmLevel_Type()
)
dcdcCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityMinorAlarmLevel.setStatus("current")
_DcdcTable_Object = MibTable
dcdcTable = _DcdcTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5)
)
if mibBuilder.loadTexts:
    dcdcTable.setStatus("current")
_DcdcEntry_Object = MibTableRow
dcdcEntry = _DcdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1)
)
dcdcEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
    (0, "SP2-MIB", "dcdcIndex"),
)
if mibBuilder.loadTexts:
    dcdcEntry.setStatus("current")


class _DcdcIndex_Type(Integer32):
    """Custom type dcdcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DcdcIndex_Type.__name__ = "Integer32"
_DcdcIndex_Object = MibTableColumn
dcdcIndex = _DcdcIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 1),
    _DcdcIndex_Type()
)
dcdcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcdcIndex.setStatus("current")


class _DcdcStatus_Type(Integer32):
    """Custom type dcdcStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_DcdcStatus_Type.__name__ = "Integer32"
_DcdcStatus_Object = MibTableColumn
dcdcStatus = _DcdcStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 2),
    _DcdcStatus_Type()
)
dcdcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcStatus.setStatus("current")
_DcdcOutputCurrentValue_Type = Integer32
_DcdcOutputCurrentValue_Object = MibTableColumn
dcdcOutputCurrentValue = _DcdcOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 3),
    _DcdcOutputCurrentValue_Type()
)
dcdcOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcOutputCurrentValue.setStatus("current")
_DcdcInputVoltageValue_Type = Integer32
_DcdcInputVoltageValue_Object = MibTableColumn
dcdcInputVoltageValue = _DcdcInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 4),
    _DcdcInputVoltageValue_Type()
)
dcdcInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcInputVoltageValue.setStatus("current")


class _DcdcType_Type(DisplayString):
    """Custom type dcdcType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_DcdcType_Type.__name__ = "DisplayString"
_DcdcType_Object = MibTableColumn
dcdcType = _DcdcType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 5),
    _DcdcType_Type()
)
dcdcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcType.setStatus("current")


class _DcdcHwPartNumber_Type(DisplayString):
    """Custom type dcdcHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DcdcHwPartNumber_Type.__name__ = "DisplayString"
_DcdcHwPartNumber_Object = MibTableColumn
dcdcHwPartNumber = _DcdcHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 6),
    _DcdcHwPartNumber_Type()
)
dcdcHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcHwPartNumber.setStatus("current")


class _DcdcHwVersion_Type(DisplayString):
    """Custom type dcdcHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_DcdcHwVersion_Type.__name__ = "DisplayString"
_DcdcHwVersion_Object = MibTableColumn
dcdcHwVersion = _DcdcHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 7),
    _DcdcHwVersion_Type()
)
dcdcHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcHwVersion.setStatus("current")


class _DcdcSwPartNumber_Type(DisplayString):
    """Custom type dcdcSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DcdcSwPartNumber_Type.__name__ = "DisplayString"
_DcdcSwPartNumber_Object = MibTableColumn
dcdcSwPartNumber = _DcdcSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 8),
    _DcdcSwPartNumber_Type()
)
dcdcSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcSwPartNumber.setStatus("current")


class _DcdcSwVersion_Type(DisplayString):
    """Custom type dcdcSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_DcdcSwVersion_Type.__name__ = "DisplayString"
_DcdcSwVersion_Object = MibTableColumn
dcdcSwVersion = _DcdcSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 9),
    _DcdcSwVersion_Type()
)
dcdcSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcSwVersion.setStatus("current")
_DcdcErrorTable_Object = MibTable
dcdcErrorTable = _DcdcErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6)
)
if mibBuilder.loadTexts:
    dcdcErrorTable.setStatus("current")
_DcdcErrorEntry_Object = MibTableRow
dcdcErrorEntry = _DcdcErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1)
)
dcdcErrorEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcErrorEntry.setStatus("current")


class _DcdcErrorStatus_Type(Integer32):
    """Custom type dcdcErrorStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_DcdcErrorStatus_Type.__name__ = "Integer32"
_DcdcErrorStatus_Object = MibTableColumn
dcdcErrorStatus = _DcdcErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 1),
    _DcdcErrorStatus_Type()
)
dcdcErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcErrorStatus.setStatus("current")


class _DcdcErrorDescription_Type(DisplayString):
    """Custom type dcdcErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcdcErrorDescription_Type.__name__ = "DisplayString"
_DcdcErrorDescription_Object = MibTableColumn
dcdcErrorDescription = _DcdcErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 2),
    _DcdcErrorDescription_Type()
)
dcdcErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorDescription.setStatus("current")
_DcdcErrorTrapRepeatCounter_Type = Counter32
_DcdcErrorTrapRepeatCounter_Object = MibTableColumn
dcdcErrorTrapRepeatCounter = _DcdcErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 3),
    _DcdcErrorTrapRepeatCounter_Type()
)
dcdcErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dcdcErrorTrapRepeatCounter.setStatus("current")


class _DcdcErrorEnable_Type(Integer32):
    """Custom type dcdcErrorEnable based on Integer32"""
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


_DcdcErrorEnable_Type.__name__ = "Integer32"
_DcdcErrorEnable_Object = MibTableColumn
dcdcErrorEnable = _DcdcErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 4),
    _DcdcErrorEnable_Type()
)
dcdcErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorEnable.setStatus("current")
_DcdcErrorValue_Type = Integer32
_DcdcErrorValue_Object = MibTableColumn
dcdcErrorValue = _DcdcErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 5),
    _DcdcErrorValue_Type()
)
dcdcErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcErrorValue.setStatus("current")
_DcdcErrorMajorAlarmLevel_Type = Integer32
_DcdcErrorMajorAlarmLevel_Object = MibTableColumn
dcdcErrorMajorAlarmLevel = _DcdcErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 6),
    _DcdcErrorMajorAlarmLevel_Type()
)
dcdcErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorMajorAlarmLevel.setStatus("current")
_DcdcErrorMinorAlarmLevel_Type = Integer32
_DcdcErrorMinorAlarmLevel_Object = MibTableColumn
dcdcErrorMinorAlarmLevel = _DcdcErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 7),
    _DcdcErrorMinorAlarmLevel_Type()
)
dcdcErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorMinorAlarmLevel.setStatus("current")
_DcdcEnergyLog_ObjectIdentity = ObjectIdentity
dcdcEnergyLog = _DcdcEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7)
)
_DcdcEnergyLogAccumulatedTable_Object = MibTable
dcdcEnergyLogAccumulatedTable = _DcdcEnergyLogAccumulatedTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 1)
)
if mibBuilder.loadTexts:
    dcdcEnergyLogAccumulatedTable.setStatus("current")
_DcdcEnergyLogAccumulatedEntry_Object = MibTableRow
dcdcEnergyLogAccumulatedEntry = _DcdcEnergyLogAccumulatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 1, 1)
)
dcdcEnergyLogAccumulatedEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcEnergyLogAccumulatedEntry.setStatus("current")
_DcdcEnergyLogAccumulated_Type = Integer32
_DcdcEnergyLogAccumulated_Object = MibTableColumn
dcdcEnergyLogAccumulated = _DcdcEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 1, 1, 1),
    _DcdcEnergyLogAccumulated_Type()
)
dcdcEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEnergyLogAccumulated.setStatus("current")


class _DcdcEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type dcdcEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_DcdcEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_DcdcEnergyLogLastHoursNumberOfEntries_Object = MibScalar
dcdcEnergyLogLastHoursNumberOfEntries = _DcdcEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 2),
    _DcdcEnergyLogLastHoursNumberOfEntries_Type()
)
dcdcEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastHoursNumberOfEntries.setStatus("current")
_DcdcEnergyLogLastHoursTable_Object = MibTable
dcdcEnergyLogLastHoursTable = _DcdcEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 3)
)
if mibBuilder.loadTexts:
    dcdcEnergyLogLastHoursTable.setStatus("current")
_DcdcEnergyLogLastHoursEntry_Object = MibTableRow
dcdcEnergyLogLastHoursEntry = _DcdcEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 3, 1)
)
dcdcEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
    (0, "SP2-MIB", "dcdcEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    dcdcEnergyLogLastHoursEntry.setStatus("current")


class _DcdcEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type dcdcEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_DcdcEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_DcdcEnergyLogLastHoursIndex_Object = MibTableColumn
dcdcEnergyLogLastHoursIndex = _DcdcEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 3, 1, 1),
    _DcdcEnergyLogLastHoursIndex_Type()
)
dcdcEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastHoursIndex.setStatus("current")
_DcdcEnergyLogLastHoursValue_Type = Integer32
_DcdcEnergyLogLastHoursValue_Object = MibTableColumn
dcdcEnergyLogLastHoursValue = _DcdcEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 3, 1, 2),
    _DcdcEnergyLogLastHoursValue_Type()
)
dcdcEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastHoursValue.setStatus("current")


class _DcdcEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type dcdcEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_DcdcEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_DcdcEnergyLogLastDaysNumberOfEntries_Object = MibScalar
dcdcEnergyLogLastDaysNumberOfEntries = _DcdcEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 4),
    _DcdcEnergyLogLastDaysNumberOfEntries_Type()
)
dcdcEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastDaysNumberOfEntries.setStatus("current")
_DcdcEnergyLogLastDaysTable_Object = MibTable
dcdcEnergyLogLastDaysTable = _DcdcEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 5)
)
if mibBuilder.loadTexts:
    dcdcEnergyLogLastDaysTable.setStatus("current")
_DcdcEnergyLogLastDaysEntry_Object = MibTableRow
dcdcEnergyLogLastDaysEntry = _DcdcEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 5, 1)
)
dcdcEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
    (0, "SP2-MIB", "dcdcEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    dcdcEnergyLogLastDaysEntry.setStatus("current")


class _DcdcEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type dcdcEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_DcdcEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_DcdcEnergyLogLastDaysIndex_Object = MibTableColumn
dcdcEnergyLogLastDaysIndex = _DcdcEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 5, 1, 1),
    _DcdcEnergyLogLastDaysIndex_Type()
)
dcdcEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastDaysIndex.setStatus("current")
_DcdcEnergyLogLastDaysValue_Type = Integer32
_DcdcEnergyLogLastDaysValue_Object = MibTableColumn
dcdcEnergyLogLastDaysValue = _DcdcEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 5, 1, 2),
    _DcdcEnergyLogLastDaysValue_Type()
)
dcdcEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastDaysValue.setStatus("current")


class _DcdcEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type dcdcEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_DcdcEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_DcdcEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
dcdcEnergyLogLastWeeksNumberOfEntries = _DcdcEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 6),
    _DcdcEnergyLogLastWeeksNumberOfEntries_Type()
)
dcdcEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_DcdcEnergyLogLastWeeksTable_Object = MibTable
dcdcEnergyLogLastWeeksTable = _DcdcEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 7)
)
if mibBuilder.loadTexts:
    dcdcEnergyLogLastWeeksTable.setStatus("current")
_DcdcEnergyLogLastWeeksEntry_Object = MibTableRow
dcdcEnergyLogLastWeeksEntry = _DcdcEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 7, 1)
)
dcdcEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
    (0, "SP2-MIB", "dcdcEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    dcdcEnergyLogLastWeeksEntry.setStatus("current")


class _DcdcEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type dcdcEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_DcdcEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_DcdcEnergyLogLastWeeksIndex_Object = MibTableColumn
dcdcEnergyLogLastWeeksIndex = _DcdcEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 7, 1, 1),
    _DcdcEnergyLogLastWeeksIndex_Type()
)
dcdcEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastWeeksIndex.setStatus("current")
_DcdcEnergyLogLastWeeksValue_Type = Integer32
_DcdcEnergyLogLastWeeksValue_Object = MibTableColumn
dcdcEnergyLogLastWeeksValue = _DcdcEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7, 7, 1, 2),
    _DcdcEnergyLogLastWeeksValue_Type()
)
dcdcEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcEnergyLogLastWeeksValue.setStatus("current")
_SolarChargers_ObjectIdentity = ObjectIdentity
solarChargers = _SolarChargers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7)
)


class _SolarChargersStatus_Type(Integer32):
    """Custom type solarChargersStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_SolarChargersStatus_Type.__name__ = "Integer32"
_SolarChargersStatus_Object = MibScalar
solarChargersStatus = _SolarChargersStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 1),
    _SolarChargersStatus_Type()
)
solarChargersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersStatus.setStatus("current")
_SolarChargersCurrent_ObjectIdentity = ObjectIdentity
solarChargersCurrent = _SolarChargersCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2)
)


class _SolarChargersCurrentStatus_Type(Integer32):
    """Custom type solarChargersCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_SolarChargersCurrentStatus_Type.__name__ = "Integer32"
_SolarChargersCurrentStatus_Object = MibScalar
solarChargersCurrentStatus = _SolarChargersCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 1),
    _SolarChargersCurrentStatus_Type()
)
solarChargersCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersCurrentStatus.setStatus("current")


class _SolarChargersCurrentDescription_Type(DisplayString):
    """Custom type solarChargersCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolarChargersCurrentDescription_Type.__name__ = "DisplayString"
_SolarChargersCurrentDescription_Object = MibScalar
solarChargersCurrentDescription = _SolarChargersCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 2),
    _SolarChargersCurrentDescription_Type()
)
solarChargersCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentDescription.setStatus("current")
_SolarChargersCurrentTrapRepeatCounter_Type = Counter32
_SolarChargersCurrentTrapRepeatCounter_Object = MibScalar
solarChargersCurrentTrapRepeatCounter = _SolarChargersCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 3),
    _SolarChargersCurrentTrapRepeatCounter_Type()
)
solarChargersCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    solarChargersCurrentTrapRepeatCounter.setStatus("current")


class _SolarChargersCurrentAlarmEnable_Type(Integer32):
    """Custom type solarChargersCurrentAlarmEnable based on Integer32"""
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


_SolarChargersCurrentAlarmEnable_Type.__name__ = "Integer32"
_SolarChargersCurrentAlarmEnable_Object = MibScalar
solarChargersCurrentAlarmEnable = _SolarChargersCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 4),
    _SolarChargersCurrentAlarmEnable_Type()
)
solarChargersCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentAlarmEnable.setStatus("current")
_SolarChargersCurrentValue_Type = Integer32
_SolarChargersCurrentValue_Object = MibScalar
solarChargersCurrentValue = _SolarChargersCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 5),
    _SolarChargersCurrentValue_Type()
)
solarChargersCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersCurrentValue.setStatus("current")
_SolarChargersCurrentMajorAlarmLevel_Type = Integer32
_SolarChargersCurrentMajorAlarmLevel_Object = MibScalar
solarChargersCurrentMajorAlarmLevel = _SolarChargersCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 6),
    _SolarChargersCurrentMajorAlarmLevel_Type()
)
solarChargersCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentMajorAlarmLevel.setStatus("current")
_SolarChargersCurrentMinorAlarmLevel_Type = Integer32
_SolarChargersCurrentMinorAlarmLevel_Object = MibScalar
solarChargersCurrentMinorAlarmLevel = _SolarChargersCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 7),
    _SolarChargersCurrentMinorAlarmLevel_Type()
)
solarChargersCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentMinorAlarmLevel.setStatus("current")
_SolarChargersCapacity_ObjectIdentity = ObjectIdentity
solarChargersCapacity = _SolarChargersCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3)
)


class _SolarChargersCapacityStatus_Type(Integer32):
    """Custom type solarChargersCapacityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_SolarChargersCapacityStatus_Type.__name__ = "Integer32"
_SolarChargersCapacityStatus_Object = MibScalar
solarChargersCapacityStatus = _SolarChargersCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3, 1),
    _SolarChargersCapacityStatus_Type()
)
solarChargersCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersCapacityStatus.setStatus("current")


class _SolarChargersCapacityDescription_Type(DisplayString):
    """Custom type solarChargersCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolarChargersCapacityDescription_Type.__name__ = "DisplayString"
_SolarChargersCapacityDescription_Object = MibScalar
solarChargersCapacityDescription = _SolarChargersCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3, 2),
    _SolarChargersCapacityDescription_Type()
)
solarChargersCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCapacityDescription.setStatus("current")
_SolarChargersCapacityTrapRepeatCounter_Type = Counter32
_SolarChargersCapacityTrapRepeatCounter_Object = MibScalar
solarChargersCapacityTrapRepeatCounter = _SolarChargersCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3, 3),
    _SolarChargersCapacityTrapRepeatCounter_Type()
)
solarChargersCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    solarChargersCapacityTrapRepeatCounter.setStatus("current")


class _SolarChargersCapacityAlarmEnable_Type(Integer32):
    """Custom type solarChargersCapacityAlarmEnable based on Integer32"""
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


_SolarChargersCapacityAlarmEnable_Type.__name__ = "Integer32"
_SolarChargersCapacityAlarmEnable_Object = MibScalar
solarChargersCapacityAlarmEnable = _SolarChargersCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3, 4),
    _SolarChargersCapacityAlarmEnable_Type()
)
solarChargersCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCapacityAlarmEnable.setStatus("current")
_SolarChargersCapacityValue_Type = Integer32
_SolarChargersCapacityValue_Object = MibScalar
solarChargersCapacityValue = _SolarChargersCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3, 5),
    _SolarChargersCapacityValue_Type()
)
solarChargersCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersCapacityValue.setStatus("current")
_SolarChargersCapacityMajorAlarmLevel_Type = Integer32
_SolarChargersCapacityMajorAlarmLevel_Object = MibScalar
solarChargersCapacityMajorAlarmLevel = _SolarChargersCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3, 6),
    _SolarChargersCapacityMajorAlarmLevel_Type()
)
solarChargersCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCapacityMajorAlarmLevel.setStatus("current")
_SolarChargersCapacityMinorAlarmLevel_Type = Integer32
_SolarChargersCapacityMinorAlarmLevel_Object = MibScalar
solarChargersCapacityMinorAlarmLevel = _SolarChargersCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3, 7),
    _SolarChargersCapacityMinorAlarmLevel_Type()
)
solarChargersCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCapacityMinorAlarmLevel.setStatus("current")
_SolarChargersError_ObjectIdentity = ObjectIdentity
solarChargersError = _SolarChargersError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4)
)


class _SolarChargersErrorStatus_Type(Integer32):
    """Custom type solarChargersErrorStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_SolarChargersErrorStatus_Type.__name__ = "Integer32"
_SolarChargersErrorStatus_Object = MibScalar
solarChargersErrorStatus = _SolarChargersErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 1),
    _SolarChargersErrorStatus_Type()
)
solarChargersErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersErrorStatus.setStatus("current")


class _SolarChargersErrorDescription_Type(DisplayString):
    """Custom type solarChargersErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolarChargersErrorDescription_Type.__name__ = "DisplayString"
_SolarChargersErrorDescription_Object = MibScalar
solarChargersErrorDescription = _SolarChargersErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 2),
    _SolarChargersErrorDescription_Type()
)
solarChargersErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorDescription.setStatus("current")
_SolarChargersErrorTrapRepeatCounter_Type = Counter32
_SolarChargersErrorTrapRepeatCounter_Object = MibScalar
solarChargersErrorTrapRepeatCounter = _SolarChargersErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 3),
    _SolarChargersErrorTrapRepeatCounter_Type()
)
solarChargersErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    solarChargersErrorTrapRepeatCounter.setStatus("current")


class _SolarChargersErrorEnable_Type(Integer32):
    """Custom type solarChargersErrorEnable based on Integer32"""
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


_SolarChargersErrorEnable_Type.__name__ = "Integer32"
_SolarChargersErrorEnable_Object = MibScalar
solarChargersErrorEnable = _SolarChargersErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 4),
    _SolarChargersErrorEnable_Type()
)
solarChargersErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorEnable.setStatus("current")
_SolarChargersErrorValue_Type = Integer32
_SolarChargersErrorValue_Object = MibScalar
solarChargersErrorValue = _SolarChargersErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 5),
    _SolarChargersErrorValue_Type()
)
solarChargersErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersErrorValue.setStatus("current")
_SolarChargersErrorMajorAlarmLevel_Type = Integer32
_SolarChargersErrorMajorAlarmLevel_Object = MibScalar
solarChargersErrorMajorAlarmLevel = _SolarChargersErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 6),
    _SolarChargersErrorMajorAlarmLevel_Type()
)
solarChargersErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorMajorAlarmLevel.setStatus("current")
_SolarChargersErrorMinorAlarmLevel_Type = Integer32
_SolarChargersErrorMinorAlarmLevel_Object = MibScalar
solarChargersErrorMinorAlarmLevel = _SolarChargersErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 7),
    _SolarChargersErrorMinorAlarmLevel_Type()
)
solarChargersErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorMinorAlarmLevel.setStatus("current")


class _SolarChargersNumberOfSolarChargers_Type(Integer32):
    """Custom type solarChargersNumberOfSolarChargers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SolarChargersNumberOfSolarChargers_Type.__name__ = "Integer32"
_SolarChargersNumberOfSolarChargers_Object = MibScalar
solarChargersNumberOfSolarChargers = _SolarChargersNumberOfSolarChargers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 5),
    _SolarChargersNumberOfSolarChargers_Type()
)
solarChargersNumberOfSolarChargers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersNumberOfSolarChargers.setStatus("current")
_SolarChargerTable_Object = MibTable
solarChargerTable = _SolarChargerTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6)
)
if mibBuilder.loadTexts:
    solarChargerTable.setStatus("current")
_SolarChargerEntry_Object = MibTableRow
solarChargerEntry = _SolarChargerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1)
)
solarChargerEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargerIndex"),
)
if mibBuilder.loadTexts:
    solarChargerEntry.setStatus("current")


class _SolarChargerIndex_Type(Integer32):
    """Custom type solarChargerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SolarChargerIndex_Type.__name__ = "Integer32"
_SolarChargerIndex_Object = MibTableColumn
solarChargerIndex = _SolarChargerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 1),
    _SolarChargerIndex_Type()
)
solarChargerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargerIndex.setStatus("current")


class _SolarChargerStatus_Type(Integer32):
    """Custom type solarChargerStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_SolarChargerStatus_Type.__name__ = "Integer32"
_SolarChargerStatus_Object = MibTableColumn
solarChargerStatus = _SolarChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 2),
    _SolarChargerStatus_Type()
)
solarChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerStatus.setStatus("current")
_SolarChargerOutputCurrentValue_Type = Integer32
_SolarChargerOutputCurrentValue_Object = MibTableColumn
solarChargerOutputCurrentValue = _SolarChargerOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 3),
    _SolarChargerOutputCurrentValue_Type()
)
solarChargerOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerOutputCurrentValue.setStatus("current")
_SolarChargerInputVoltageValue_Type = Integer32
_SolarChargerInputVoltageValue_Object = MibTableColumn
solarChargerInputVoltageValue = _SolarChargerInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 4),
    _SolarChargerInputVoltageValue_Type()
)
solarChargerInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerInputVoltageValue.setStatus("current")


class _SolarChargerType_Type(DisplayString):
    """Custom type solarChargerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_SolarChargerType_Type.__name__ = "DisplayString"
_SolarChargerType_Object = MibTableColumn
solarChargerType = _SolarChargerType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 5),
    _SolarChargerType_Type()
)
solarChargerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerType.setStatus("current")


class _SolarChargerHwPartNumber_Type(DisplayString):
    """Custom type solarChargerHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SolarChargerHwPartNumber_Type.__name__ = "DisplayString"
_SolarChargerHwPartNumber_Object = MibTableColumn
solarChargerHwPartNumber = _SolarChargerHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 6),
    _SolarChargerHwPartNumber_Type()
)
solarChargerHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerHwPartNumber.setStatus("current")


class _SolarChargerHwVersion_Type(DisplayString):
    """Custom type solarChargerHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SolarChargerHwVersion_Type.__name__ = "DisplayString"
_SolarChargerHwVersion_Object = MibTableColumn
solarChargerHwVersion = _SolarChargerHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 7),
    _SolarChargerHwVersion_Type()
)
solarChargerHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerHwVersion.setStatus("current")


class _SolarChargerSwPartNumber_Type(DisplayString):
    """Custom type solarChargerSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SolarChargerSwPartNumber_Type.__name__ = "DisplayString"
_SolarChargerSwPartNumber_Object = MibTableColumn
solarChargerSwPartNumber = _SolarChargerSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 8),
    _SolarChargerSwPartNumber_Type()
)
solarChargerSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerSwPartNumber.setStatus("current")


class _SolarChargerSwVersion_Type(DisplayString):
    """Custom type solarChargerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SolarChargerSwVersion_Type.__name__ = "DisplayString"
_SolarChargerSwVersion_Object = MibTableColumn
solarChargerSwVersion = _SolarChargerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 9),
    _SolarChargerSwVersion_Type()
)
solarChargerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerSwVersion.setStatus("current")
_SolarChargersEnergyLog_ObjectIdentity = ObjectIdentity
solarChargersEnergyLog = _SolarChargersEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7)
)
_SolarChargersEnergyLogAccumulated_Type = Integer32
_SolarChargersEnergyLogAccumulated_Object = MibScalar
solarChargersEnergyLogAccumulated = _SolarChargersEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 1),
    _SolarChargersEnergyLogAccumulated_Type()
)
solarChargersEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogAccumulated.setStatus("current")
_SolarChargersEnergyLogLastHoursNumberOfEntries_Type = Integer32
_SolarChargersEnergyLogLastHoursNumberOfEntries_Object = MibScalar
solarChargersEnergyLogLastHoursNumberOfEntries = _SolarChargersEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 2),
    _SolarChargersEnergyLogLastHoursNumberOfEntries_Type()
)
solarChargersEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursNumberOfEntries.setStatus("current")
_SolarChargersEnergyLogLastHoursTable_Object = MibTable
solarChargersEnergyLogLastHoursTable = _SolarChargersEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3)
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursTable.setStatus("current")
_SolarChargersEnergyLogLastHoursEntry_Object = MibTableRow
solarChargersEnergyLogLastHoursEntry = _SolarChargersEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3, 1)
)
solarChargersEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargersEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursEntry.setStatus("current")


class _SolarChargersEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type solarChargersEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_SolarChargersEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_SolarChargersEnergyLogLastHoursIndex_Object = MibTableColumn
solarChargersEnergyLogLastHoursIndex = _SolarChargersEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3, 1, 1),
    _SolarChargersEnergyLogLastHoursIndex_Type()
)
solarChargersEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursIndex.setStatus("current")
_SolarChargersEnergyLogLastHoursValue_Type = Integer32
_SolarChargersEnergyLogLastHoursValue_Object = MibTableColumn
solarChargersEnergyLogLastHoursValue = _SolarChargersEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3, 1, 2),
    _SolarChargersEnergyLogLastHoursValue_Type()
)
solarChargersEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursValue.setStatus("current")
_SolarChargersEnergyLogLastDaysNumberOfEntries_Type = Integer32
_SolarChargersEnergyLogLastDaysNumberOfEntries_Object = MibScalar
solarChargersEnergyLogLastDaysNumberOfEntries = _SolarChargersEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 4),
    _SolarChargersEnergyLogLastDaysNumberOfEntries_Type()
)
solarChargersEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysNumberOfEntries.setStatus("current")
_SolarChargersEnergyLogLastDaysTable_Object = MibTable
solarChargersEnergyLogLastDaysTable = _SolarChargersEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5)
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysTable.setStatus("current")
_SolarChargersEnergyLogLastDaysEntry_Object = MibTableRow
solarChargersEnergyLogLastDaysEntry = _SolarChargersEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5, 1)
)
solarChargersEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargersEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysEntry.setStatus("current")


class _SolarChargersEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type solarChargersEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_SolarChargersEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_SolarChargersEnergyLogLastDaysIndex_Object = MibTableColumn
solarChargersEnergyLogLastDaysIndex = _SolarChargersEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5, 1, 1),
    _SolarChargersEnergyLogLastDaysIndex_Type()
)
solarChargersEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysIndex.setStatus("current")
_SolarChargersEnergyLogLastDaysValue_Type = Integer32
_SolarChargersEnergyLogLastDaysValue_Object = MibTableColumn
solarChargersEnergyLogLastDaysValue = _SolarChargersEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5, 1, 2),
    _SolarChargersEnergyLogLastDaysValue_Type()
)
solarChargersEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysValue.setStatus("current")
_SolarChargersEnergyLogLastWeeksNumberOfEntries_Type = Integer32
_SolarChargersEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
solarChargersEnergyLogLastWeeksNumberOfEntries = _SolarChargersEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 6),
    _SolarChargersEnergyLogLastWeeksNumberOfEntries_Type()
)
solarChargersEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_SolarChargersEnergyLogLastWeeksTable_Object = MibTable
solarChargersEnergyLogLastWeeksTable = _SolarChargersEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7)
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksTable.setStatus("current")
_SolarChargersEnergyLogLastWeeksEntry_Object = MibTableRow
solarChargersEnergyLogLastWeeksEntry = _SolarChargersEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7, 1)
)
solarChargersEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargersEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksEntry.setStatus("current")


class _SolarChargersEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type solarChargersEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_SolarChargersEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_SolarChargersEnergyLogLastWeeksIndex_Object = MibTableColumn
solarChargersEnergyLogLastWeeksIndex = _SolarChargersEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7, 1, 1),
    _SolarChargersEnergyLogLastWeeksIndex_Type()
)
solarChargersEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksIndex.setStatus("current")
_SolarChargersEnergyLogLastWeeksValue_Type = Integer32
_SolarChargersEnergyLogLastWeeksValue_Object = MibTableColumn
solarChargersEnergyLogLastWeeksValue = _SolarChargersEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7, 1, 2),
    _SolarChargersEnergyLogLastWeeksValue_Type()
)
solarChargersEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksValue.setStatus("current")
_WindChargers_ObjectIdentity = ObjectIdentity
windChargers = _WindChargers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8)
)


class _WindChargersStatus_Type(Integer32):
    """Custom type windChargersStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_WindChargersStatus_Type.__name__ = "Integer32"
_WindChargersStatus_Object = MibScalar
windChargersStatus = _WindChargersStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 1),
    _WindChargersStatus_Type()
)
windChargersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersStatus.setStatus("current")
_WindChargersCurrent_ObjectIdentity = ObjectIdentity
windChargersCurrent = _WindChargersCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2)
)


class _WindChargersCurrentStatus_Type(Integer32):
    """Custom type windChargersCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_WindChargersCurrentStatus_Type.__name__ = "Integer32"
_WindChargersCurrentStatus_Object = MibScalar
windChargersCurrentStatus = _WindChargersCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 1),
    _WindChargersCurrentStatus_Type()
)
windChargersCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersCurrentStatus.setStatus("current")


class _WindChargersCurrentDescription_Type(DisplayString):
    """Custom type windChargersCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WindChargersCurrentDescription_Type.__name__ = "DisplayString"
_WindChargersCurrentDescription_Object = MibScalar
windChargersCurrentDescription = _WindChargersCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 2),
    _WindChargersCurrentDescription_Type()
)
windChargersCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentDescription.setStatus("current")
_WindChargersCurrentTrapRepeatCounter_Type = Counter32
_WindChargersCurrentTrapRepeatCounter_Object = MibScalar
windChargersCurrentTrapRepeatCounter = _WindChargersCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 3),
    _WindChargersCurrentTrapRepeatCounter_Type()
)
windChargersCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    windChargersCurrentTrapRepeatCounter.setStatus("current")


class _WindChargersCurrentAlarmEnable_Type(Integer32):
    """Custom type windChargersCurrentAlarmEnable based on Integer32"""
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


_WindChargersCurrentAlarmEnable_Type.__name__ = "Integer32"
_WindChargersCurrentAlarmEnable_Object = MibScalar
windChargersCurrentAlarmEnable = _WindChargersCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 4),
    _WindChargersCurrentAlarmEnable_Type()
)
windChargersCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentAlarmEnable.setStatus("current")
_WindChargersCurrentValue_Type = Integer32
_WindChargersCurrentValue_Object = MibScalar
windChargersCurrentValue = _WindChargersCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 5),
    _WindChargersCurrentValue_Type()
)
windChargersCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersCurrentValue.setStatus("current")
_WindChargersCurrentMajorAlarmLevel_Type = Integer32
_WindChargersCurrentMajorAlarmLevel_Object = MibScalar
windChargersCurrentMajorAlarmLevel = _WindChargersCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 6),
    _WindChargersCurrentMajorAlarmLevel_Type()
)
windChargersCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentMajorAlarmLevel.setStatus("current")
_WindChargersCurrentMinorAlarmLevel_Type = Integer32
_WindChargersCurrentMinorAlarmLevel_Object = MibScalar
windChargersCurrentMinorAlarmLevel = _WindChargersCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 7),
    _WindChargersCurrentMinorAlarmLevel_Type()
)
windChargersCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentMinorAlarmLevel.setStatus("current")
_WindChargersCapacity_ObjectIdentity = ObjectIdentity
windChargersCapacity = _WindChargersCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3)
)


class _WindChargersCapacityStatus_Type(Integer32):
    """Custom type windChargersCapacityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_WindChargersCapacityStatus_Type.__name__ = "Integer32"
_WindChargersCapacityStatus_Object = MibScalar
windChargersCapacityStatus = _WindChargersCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3, 1),
    _WindChargersCapacityStatus_Type()
)
windChargersCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersCapacityStatus.setStatus("current")


class _WindChargersCapacityDescription_Type(DisplayString):
    """Custom type windChargersCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WindChargersCapacityDescription_Type.__name__ = "DisplayString"
_WindChargersCapacityDescription_Object = MibScalar
windChargersCapacityDescription = _WindChargersCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3, 2),
    _WindChargersCapacityDescription_Type()
)
windChargersCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCapacityDescription.setStatus("current")
_WindChargersCapacityTrapRepeatCounter_Type = Counter32
_WindChargersCapacityTrapRepeatCounter_Object = MibScalar
windChargersCapacityTrapRepeatCounter = _WindChargersCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3, 3),
    _WindChargersCapacityTrapRepeatCounter_Type()
)
windChargersCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    windChargersCapacityTrapRepeatCounter.setStatus("current")


class _WindChargersCapacityAlarmEnable_Type(Integer32):
    """Custom type windChargersCapacityAlarmEnable based on Integer32"""
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


_WindChargersCapacityAlarmEnable_Type.__name__ = "Integer32"
_WindChargersCapacityAlarmEnable_Object = MibScalar
windChargersCapacityAlarmEnable = _WindChargersCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3, 4),
    _WindChargersCapacityAlarmEnable_Type()
)
windChargersCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCapacityAlarmEnable.setStatus("current")
_WindChargersCapacityValue_Type = Integer32
_WindChargersCapacityValue_Object = MibScalar
windChargersCapacityValue = _WindChargersCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3, 5),
    _WindChargersCapacityValue_Type()
)
windChargersCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersCapacityValue.setStatus("current")
_WindChargersCapacityMajorAlarmLevel_Type = Integer32
_WindChargersCapacityMajorAlarmLevel_Object = MibScalar
windChargersCapacityMajorAlarmLevel = _WindChargersCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3, 6),
    _WindChargersCapacityMajorAlarmLevel_Type()
)
windChargersCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCapacityMajorAlarmLevel.setStatus("current")
_WindChargersCapacityMinorAlarmLevel_Type = Integer32
_WindChargersCapacityMinorAlarmLevel_Object = MibScalar
windChargersCapacityMinorAlarmLevel = _WindChargersCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3, 7),
    _WindChargersCapacityMinorAlarmLevel_Type()
)
windChargersCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCapacityMinorAlarmLevel.setStatus("current")
_WindChargersError_ObjectIdentity = ObjectIdentity
windChargersError = _WindChargersError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4)
)


class _WindChargersErrorStatus_Type(Integer32):
    """Custom type windChargersErrorStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_WindChargersErrorStatus_Type.__name__ = "Integer32"
_WindChargersErrorStatus_Object = MibScalar
windChargersErrorStatus = _WindChargersErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 1),
    _WindChargersErrorStatus_Type()
)
windChargersErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersErrorStatus.setStatus("current")


class _WindChargersErrorDescription_Type(DisplayString):
    """Custom type windChargersErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WindChargersErrorDescription_Type.__name__ = "DisplayString"
_WindChargersErrorDescription_Object = MibScalar
windChargersErrorDescription = _WindChargersErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 2),
    _WindChargersErrorDescription_Type()
)
windChargersErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorDescription.setStatus("current")
_WindChargersErrorTrapRepeatCounter_Type = Counter32
_WindChargersErrorTrapRepeatCounter_Object = MibScalar
windChargersErrorTrapRepeatCounter = _WindChargersErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 3),
    _WindChargersErrorTrapRepeatCounter_Type()
)
windChargersErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    windChargersErrorTrapRepeatCounter.setStatus("current")


class _WindChargersErrorEnable_Type(Integer32):
    """Custom type windChargersErrorEnable based on Integer32"""
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


_WindChargersErrorEnable_Type.__name__ = "Integer32"
_WindChargersErrorEnable_Object = MibScalar
windChargersErrorEnable = _WindChargersErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 4),
    _WindChargersErrorEnable_Type()
)
windChargersErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorEnable.setStatus("current")
_WindChargersErrorValue_Type = Integer32
_WindChargersErrorValue_Object = MibScalar
windChargersErrorValue = _WindChargersErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 5),
    _WindChargersErrorValue_Type()
)
windChargersErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersErrorValue.setStatus("current")
_WindChargersErrorMajorAlarmLevel_Type = Integer32
_WindChargersErrorMajorAlarmLevel_Object = MibScalar
windChargersErrorMajorAlarmLevel = _WindChargersErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 6),
    _WindChargersErrorMajorAlarmLevel_Type()
)
windChargersErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorMajorAlarmLevel.setStatus("current")
_WindChargersErrorMinorAlarmLevel_Type = Integer32
_WindChargersErrorMinorAlarmLevel_Object = MibScalar
windChargersErrorMinorAlarmLevel = _WindChargersErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 7),
    _WindChargersErrorMinorAlarmLevel_Type()
)
windChargersErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorMinorAlarmLevel.setStatus("current")


class _WindChargersNumberOfWindChargers_Type(Integer32):
    """Custom type windChargersNumberOfWindChargers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_WindChargersNumberOfWindChargers_Type.__name__ = "Integer32"
_WindChargersNumberOfWindChargers_Object = MibScalar
windChargersNumberOfWindChargers = _WindChargersNumberOfWindChargers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 5),
    _WindChargersNumberOfWindChargers_Type()
)
windChargersNumberOfWindChargers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersNumberOfWindChargers.setStatus("current")
_WindChargerTable_Object = MibTable
windChargerTable = _WindChargerTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6)
)
if mibBuilder.loadTexts:
    windChargerTable.setStatus("current")
_WindChargerEntry_Object = MibTableRow
windChargerEntry = _WindChargerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1)
)
windChargerEntry.setIndexNames(
    (0, "SP2-MIB", "windChargerIndex"),
)
if mibBuilder.loadTexts:
    windChargerEntry.setStatus("current")


class _WindChargerIndex_Type(Integer32):
    """Custom type windChargerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WindChargerIndex_Type.__name__ = "Integer32"
_WindChargerIndex_Object = MibTableColumn
windChargerIndex = _WindChargerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 1),
    _WindChargerIndex_Type()
)
windChargerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargerIndex.setStatus("current")


class _WindChargerStatus_Type(Integer32):
    """Custom type windChargerStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_WindChargerStatus_Type.__name__ = "Integer32"
_WindChargerStatus_Object = MibTableColumn
windChargerStatus = _WindChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 2),
    _WindChargerStatus_Type()
)
windChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerStatus.setStatus("current")
_WindChargerOutputCurrentValue_Type = Integer32
_WindChargerOutputCurrentValue_Object = MibTableColumn
windChargerOutputCurrentValue = _WindChargerOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 3),
    _WindChargerOutputCurrentValue_Type()
)
windChargerOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerOutputCurrentValue.setStatus("current")
_WindChargerInputVoltageValue_Type = Integer32
_WindChargerInputVoltageValue_Object = MibTableColumn
windChargerInputVoltageValue = _WindChargerInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 4),
    _WindChargerInputVoltageValue_Type()
)
windChargerInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerInputVoltageValue.setStatus("current")


class _WindChargerType_Type(DisplayString):
    """Custom type windChargerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_WindChargerType_Type.__name__ = "DisplayString"
_WindChargerType_Object = MibTableColumn
windChargerType = _WindChargerType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 5),
    _WindChargerType_Type()
)
windChargerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerType.setStatus("current")


class _WindChargerHwPartNumber_Type(DisplayString):
    """Custom type windChargerHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WindChargerHwPartNumber_Type.__name__ = "DisplayString"
_WindChargerHwPartNumber_Object = MibTableColumn
windChargerHwPartNumber = _WindChargerHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 6),
    _WindChargerHwPartNumber_Type()
)
windChargerHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerHwPartNumber.setStatus("current")


class _WindChargerHwVersion_Type(DisplayString):
    """Custom type windChargerHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_WindChargerHwVersion_Type.__name__ = "DisplayString"
_WindChargerHwVersion_Object = MibTableColumn
windChargerHwVersion = _WindChargerHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 7),
    _WindChargerHwVersion_Type()
)
windChargerHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerHwVersion.setStatus("current")


class _WindChargerSwPartNumber_Type(DisplayString):
    """Custom type windChargerSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WindChargerSwPartNumber_Type.__name__ = "DisplayString"
_WindChargerSwPartNumber_Object = MibTableColumn
windChargerSwPartNumber = _WindChargerSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 8),
    _WindChargerSwPartNumber_Type()
)
windChargerSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerSwPartNumber.setStatus("current")


class _WindChargerSwVersion_Type(DisplayString):
    """Custom type windChargerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_WindChargerSwVersion_Type.__name__ = "DisplayString"
_WindChargerSwVersion_Object = MibTableColumn
windChargerSwVersion = _WindChargerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 9),
    _WindChargerSwVersion_Type()
)
windChargerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerSwVersion.setStatus("current")
_WindChargersEnergyLog_ObjectIdentity = ObjectIdentity
windChargersEnergyLog = _WindChargersEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7)
)
_WindChargersEnergyLogAccumulated_Type = Integer32
_WindChargersEnergyLogAccumulated_Object = MibScalar
windChargersEnergyLogAccumulated = _WindChargersEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 1),
    _WindChargersEnergyLogAccumulated_Type()
)
windChargersEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogAccumulated.setStatus("current")


class _WindChargersEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type windChargersEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_WindChargersEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastHoursNumberOfEntries_Object = MibScalar
windChargersEnergyLogLastHoursNumberOfEntries = _WindChargersEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 2),
    _WindChargersEnergyLogLastHoursNumberOfEntries_Type()
)
windChargersEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursNumberOfEntries.setStatus("current")
_WindChargersEnergyLogLastHoursTable_Object = MibTable
windChargersEnergyLogLastHoursTable = _WindChargersEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3)
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursTable.setStatus("current")
_WindChargersEnergyLogLastHoursEntry_Object = MibTableRow
windChargersEnergyLogLastHoursEntry = _WindChargersEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3, 1)
)
windChargersEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "windChargersEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursEntry.setStatus("current")


class _WindChargersEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type windChargersEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WindChargersEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastHoursIndex_Object = MibTableColumn
windChargersEnergyLogLastHoursIndex = _WindChargersEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3, 1, 1),
    _WindChargersEnergyLogLastHoursIndex_Type()
)
windChargersEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursIndex.setStatus("current")
_WindChargersEnergyLogLastHoursValue_Type = Integer32
_WindChargersEnergyLogLastHoursValue_Object = MibTableColumn
windChargersEnergyLogLastHoursValue = _WindChargersEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3, 1, 2),
    _WindChargersEnergyLogLastHoursValue_Type()
)
windChargersEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursValue.setStatus("current")


class _WindChargersEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type windChargersEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_WindChargersEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastDaysNumberOfEntries_Object = MibScalar
windChargersEnergyLogLastDaysNumberOfEntries = _WindChargersEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 4),
    _WindChargersEnergyLogLastDaysNumberOfEntries_Type()
)
windChargersEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysNumberOfEntries.setStatus("current")
_WindChargersEnergyLogLastDaysTable_Object = MibTable
windChargersEnergyLogLastDaysTable = _WindChargersEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5)
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysTable.setStatus("current")
_WindChargersEnergyLogLastDaysEntry_Object = MibTableRow
windChargersEnergyLogLastDaysEntry = _WindChargersEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5, 1)
)
windChargersEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "windChargersEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysEntry.setStatus("current")


class _WindChargersEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type windChargersEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WindChargersEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastDaysIndex_Object = MibTableColumn
windChargersEnergyLogLastDaysIndex = _WindChargersEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5, 1, 1),
    _WindChargersEnergyLogLastDaysIndex_Type()
)
windChargersEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysIndex.setStatus("current")
_WindChargersEnergyLogLastDaysValue_Type = Integer32
_WindChargersEnergyLogLastDaysValue_Object = MibTableColumn
windChargersEnergyLogLastDaysValue = _WindChargersEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5, 1, 2),
    _WindChargersEnergyLogLastDaysValue_Type()
)
windChargersEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysValue.setStatus("current")


class _WindChargersEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type windChargersEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_WindChargersEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
windChargersEnergyLogLastWeeksNumberOfEntries = _WindChargersEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 6),
    _WindChargersEnergyLogLastWeeksNumberOfEntries_Type()
)
windChargersEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_WindChargersEnergyLogLastWeeksTable_Object = MibTable
windChargersEnergyLogLastWeeksTable = _WindChargersEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7)
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksTable.setStatus("current")
_WindChargersEnergyLogLastWeeksEntry_Object = MibTableRow
windChargersEnergyLogLastWeeksEntry = _WindChargersEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7, 1)
)
windChargersEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "windChargersEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksEntry.setStatus("current")


class _WindChargersEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type windChargersEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WindChargersEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastWeeksIndex_Object = MibTableColumn
windChargersEnergyLogLastWeeksIndex = _WindChargersEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7, 1, 1),
    _WindChargersEnergyLogLastWeeksIndex_Type()
)
windChargersEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksIndex.setStatus("current")
_WindChargersEnergyLogLastWeeksValue_Type = Integer32
_WindChargersEnergyLogLastWeeksValue_Object = MibTableColumn
windChargersEnergyLogLastWeeksValue = _WindChargersEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7, 1, 2),
    _WindChargersEnergyLogLastWeeksValue_Type()
)
windChargersEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksValue.setStatus("current")
_Load_ObjectIdentity = ObjectIdentity
load = _Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9)
)


class _LoadStatus_Type(Integer32):
    """Custom type loadStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_LoadStatus_Type.__name__ = "Integer32"
_LoadStatus_Object = MibScalar
loadStatus = _LoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 1),
    _LoadStatus_Type()
)
loadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadStatus.setStatus("current")
_LoadCurrent_ObjectIdentity = ObjectIdentity
loadCurrent = _LoadCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2)
)


class _LoadCurrentStatus_Type(Integer32):
    """Custom type loadCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_LoadCurrentStatus_Type.__name__ = "Integer32"
_LoadCurrentStatus_Object = MibScalar
loadCurrentStatus = _LoadCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 1),
    _LoadCurrentStatus_Type()
)
loadCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrentStatus.setStatus("current")


class _LoadCurrentDescription_Type(DisplayString):
    """Custom type loadCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadCurrentDescription_Type.__name__ = "DisplayString"
_LoadCurrentDescription_Object = MibScalar
loadCurrentDescription = _LoadCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 2),
    _LoadCurrentDescription_Type()
)
loadCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentDescription.setStatus("current")
_LoadCurrentTrapRepeatCounter_Type = Counter32
_LoadCurrentTrapRepeatCounter_Object = MibScalar
loadCurrentTrapRepeatCounter = _LoadCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 3),
    _LoadCurrentTrapRepeatCounter_Type()
)
loadCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadCurrentTrapRepeatCounter.setStatus("current")


class _LoadCurrentAlarmEnable_Type(Integer32):
    """Custom type loadCurrentAlarmEnable based on Integer32"""
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


_LoadCurrentAlarmEnable_Type.__name__ = "Integer32"
_LoadCurrentAlarmEnable_Object = MibScalar
loadCurrentAlarmEnable = _LoadCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 4),
    _LoadCurrentAlarmEnable_Type()
)
loadCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentAlarmEnable.setStatus("current")
_LoadCurrentValue_Type = Integer32
_LoadCurrentValue_Object = MibScalar
loadCurrentValue = _LoadCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 5),
    _LoadCurrentValue_Type()
)
loadCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrentValue.setStatus("current")
_LoadCurrentMajorHighLevel_Type = Integer32
_LoadCurrentMajorHighLevel_Object = MibScalar
loadCurrentMajorHighLevel = _LoadCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 6),
    _LoadCurrentMajorHighLevel_Type()
)
loadCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentMajorHighLevel.setStatus("current")
_LoadCurrentMinorHighLevel_Type = Integer32
_LoadCurrentMinorHighLevel_Object = MibScalar
loadCurrentMinorHighLevel = _LoadCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 7),
    _LoadCurrentMinorHighLevel_Type()
)
loadCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentMinorHighLevel.setStatus("current")


class _LoadFusesStatus_Type(Integer32):
    """Custom type loadFusesStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_LoadFusesStatus_Type.__name__ = "Integer32"
_LoadFusesStatus_Object = MibScalar
loadFusesStatus = _LoadFusesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 3),
    _LoadFusesStatus_Type()
)
loadFusesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFusesStatus.setStatus("current")


class _LoadNumberOfGroups_Type(Integer32):
    """Custom type loadNumberOfGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LoadNumberOfGroups_Type.__name__ = "Integer32"
_LoadNumberOfGroups_Object = MibScalar
loadNumberOfGroups = _LoadNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 4),
    _LoadNumberOfGroups_Type()
)
loadNumberOfGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadNumberOfGroups.setStatus("current")
_LoadGroupTable_Object = MibTable
loadGroupTable = _LoadGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5)
)
if mibBuilder.loadTexts:
    loadGroupTable.setStatus("current")
_LoadGroupEntry_Object = MibTableRow
loadGroupEntry = _LoadGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1)
)
loadGroupEntry.setIndexNames(
    (0, "SP2-MIB", "loadGroupIndex"),
)
if mibBuilder.loadTexts:
    loadGroupEntry.setStatus("current")


class _LoadGroupIndex_Type(Integer32):
    """Custom type loadGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LoadGroupIndex_Type.__name__ = "Integer32"
_LoadGroupIndex_Object = MibTableColumn
loadGroupIndex = _LoadGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1, 1),
    _LoadGroupIndex_Type()
)
loadGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadGroupIndex.setStatus("current")


class _LoadGroupStatus_Type(Integer32):
    """Custom type loadGroupStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_LoadGroupStatus_Type.__name__ = "Integer32"
_LoadGroupStatus_Object = MibTableColumn
loadGroupStatus = _LoadGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1, 2),
    _LoadGroupStatus_Type()
)
loadGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadGroupStatus.setStatus("current")


class _LoadNumberOfLVLDs_Type(Integer32):
    """Custom type loadNumberOfLVLDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_LoadNumberOfLVLDs_Type.__name__ = "Integer32"
_LoadNumberOfLVLDs_Object = MibTableColumn
loadNumberOfLVLDs = _LoadNumberOfLVLDs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1, 3),
    _LoadNumberOfLVLDs_Type()
)
loadNumberOfLVLDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadNumberOfLVLDs.setStatus("current")
_LoadLVLDTable_Object = MibTable
loadLVLDTable = _LoadLVLDTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6)
)
if mibBuilder.loadTexts:
    loadLVLDTable.setStatus("current")
_LoadLVLDEntry_Object = MibTableRow
loadLVLDEntry = _LoadLVLDEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1)
)
loadLVLDEntry.setIndexNames(
    (0, "SP2-MIB", "loadGroupIndex"),
    (0, "SP2-MIB", "loadLVLDIndex"),
)
if mibBuilder.loadTexts:
    loadLVLDEntry.setStatus("current")


class _LoadLVLDIndex_Type(Integer32):
    """Custom type loadLVLDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LoadLVLDIndex_Type.__name__ = "Integer32"
_LoadLVLDIndex_Object = MibTableColumn
loadLVLDIndex = _LoadLVLDIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 1),
    _LoadLVLDIndex_Type()
)
loadLVLDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadLVLDIndex.setStatus("current")


class _LoadLVLDStatus_Type(Integer32):
    """Custom type loadLVLDStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_LoadLVLDStatus_Type.__name__ = "Integer32"
_LoadLVLDStatus_Object = MibTableColumn
loadLVLDStatus = _LoadLVLDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 2),
    _LoadLVLDStatus_Type()
)
loadLVLDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVLDStatus.setStatus("current")


class _LoadLVLDDescription_Type(DisplayString):
    """Custom type loadLVLDDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadLVLDDescription_Type.__name__ = "DisplayString"
_LoadLVLDDescription_Object = MibTableColumn
loadLVLDDescription = _LoadLVLDDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 3),
    _LoadLVLDDescription_Type()
)
loadLVLDDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDDescription.setStatus("current")
_LoadLVLDTrapRepeatCounter_Type = Counter32
_LoadLVLDTrapRepeatCounter_Object = MibTableColumn
loadLVLDTrapRepeatCounter = _LoadLVLDTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 4),
    _LoadLVLDTrapRepeatCounter_Type()
)
loadLVLDTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadLVLDTrapRepeatCounter.setStatus("current")


class _LoadLVLDEnable_Type(Integer32):
    """Custom type loadLVLDEnable based on Integer32"""
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


_LoadLVLDEnable_Type.__name__ = "Integer32"
_LoadLVLDEnable_Object = MibTableColumn
loadLVLDEnable = _LoadLVLDEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 5),
    _LoadLVLDEnable_Type()
)
loadLVLDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDEnable.setStatus("current")
_LoadLVLDValue_Type = Integer32
_LoadLVLDValue_Object = MibTableColumn
loadLVLDValue = _LoadLVLDValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 6),
    _LoadLVLDValue_Type()
)
loadLVLDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVLDValue.setStatus("current")
_LoadLVLDConnectVoltage_Type = Integer32
_LoadLVLDConnectVoltage_Object = MibTableColumn
loadLVLDConnectVoltage = _LoadLVLDConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 7),
    _LoadLVLDConnectVoltage_Type()
)
loadLVLDConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDConnectVoltage.setStatus("current")
_LoadLVLDDisconnectVoltage_Type = Integer32
_LoadLVLDDisconnectVoltage_Object = MibTableColumn
loadLVLDDisconnectVoltage = _LoadLVLDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 8),
    _LoadLVLDDisconnectVoltage_Type()
)
loadLVLDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDDisconnectVoltage.setStatus("current")
_LoadFuseTable_Object = MibTable
loadFuseTable = _LoadFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7)
)
if mibBuilder.loadTexts:
    loadFuseTable.setStatus("current")
_LoadFuseEntry_Object = MibTableRow
loadFuseEntry = _LoadFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1)
)
loadFuseEntry.setIndexNames(
    (0, "SP2-MIB", "loadGroupIndex"),
)
if mibBuilder.loadTexts:
    loadFuseEntry.setStatus("current")


class _LoadFuseStatus_Type(Integer32):
    """Custom type loadFuseStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6))
    )


_LoadFuseStatus_Type.__name__ = "Integer32"
_LoadFuseStatus_Object = MibTableColumn
loadFuseStatus = _LoadFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 1),
    _LoadFuseStatus_Type()
)
loadFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFuseStatus.setStatus("current")


class _LoadFuseDescription_Type(DisplayString):
    """Custom type loadFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadFuseDescription_Type.__name__ = "DisplayString"
_LoadFuseDescription_Object = MibTableColumn
loadFuseDescription = _LoadFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 2),
    _LoadFuseDescription_Type()
)
loadFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFuseDescription.setStatus("current")
_LoadFuseTrapRepeatCounter_Type = Counter32
_LoadFuseTrapRepeatCounter_Object = MibTableColumn
loadFuseTrapRepeatCounter = _LoadFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 3),
    _LoadFuseTrapRepeatCounter_Type()
)
loadFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadFuseTrapRepeatCounter.setStatus("current")


class _LoadFuseAlarmEnable_Type(Integer32):
    """Custom type loadFuseAlarmEnable based on Integer32"""
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


_LoadFuseAlarmEnable_Type.__name__ = "Integer32"
_LoadFuseAlarmEnable_Object = MibTableColumn
loadFuseAlarmEnable = _LoadFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 4),
    _LoadFuseAlarmEnable_Type()
)
loadFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFuseAlarmEnable.setStatus("current")
_LoadFuseValue_Type = Integer32
_LoadFuseValue_Object = MibTableColumn
loadFuseValue = _LoadFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 5),
    _LoadFuseValue_Type()
)
loadFuseValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFuseValue.setStatus("current")
_LoadEnergyLog_ObjectIdentity = ObjectIdentity
loadEnergyLog = _LoadEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8)
)
_LoadEnergyLogAccumulated_Type = Integer32
_LoadEnergyLogAccumulated_Object = MibScalar
loadEnergyLogAccumulated = _LoadEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 1),
    _LoadEnergyLogAccumulated_Type()
)
loadEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogAccumulated.setStatus("current")


class _LoadEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type loadEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_LoadEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_LoadEnergyLogLastHoursNumberOfEntries_Object = MibScalar
loadEnergyLogLastHoursNumberOfEntries = _LoadEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 2),
    _LoadEnergyLogLastHoursNumberOfEntries_Type()
)
loadEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursNumberOfEntries.setStatus("current")
_LoadEnergyLogLastHoursTable_Object = MibTable
loadEnergyLogLastHoursTable = _LoadEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3)
)
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursTable.setStatus("current")
_LoadEnergyLogLastHoursEntry_Object = MibTableRow
loadEnergyLogLastHoursEntry = _LoadEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3, 1)
)
loadEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "loadEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursEntry.setStatus("current")


class _LoadEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type loadEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_LoadEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_LoadEnergyLogLastHoursIndex_Object = MibTableColumn
loadEnergyLogLastHoursIndex = _LoadEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3, 1, 1),
    _LoadEnergyLogLastHoursIndex_Type()
)
loadEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursIndex.setStatus("current")
_LoadEnergyLogLastHoursValue_Type = Integer32
_LoadEnergyLogLastHoursValue_Object = MibTableColumn
loadEnergyLogLastHoursValue = _LoadEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3, 1, 2),
    _LoadEnergyLogLastHoursValue_Type()
)
loadEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursValue.setStatus("current")


class _LoadEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type loadEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_LoadEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_LoadEnergyLogLastDaysNumberOfEntries_Object = MibScalar
loadEnergyLogLastDaysNumberOfEntries = _LoadEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 4),
    _LoadEnergyLogLastDaysNumberOfEntries_Type()
)
loadEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysNumberOfEntries.setStatus("current")
_LoadEnergyLogLastDaysTable_Object = MibTable
loadEnergyLogLastDaysTable = _LoadEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5)
)
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysTable.setStatus("current")
_LoadEnergyLogLastDaysEntry_Object = MibTableRow
loadEnergyLogLastDaysEntry = _LoadEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5, 1)
)
loadEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "loadEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysEntry.setStatus("current")


class _LoadEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type loadEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_LoadEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_LoadEnergyLogLastDaysIndex_Object = MibTableColumn
loadEnergyLogLastDaysIndex = _LoadEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5, 1, 1),
    _LoadEnergyLogLastDaysIndex_Type()
)
loadEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysIndex.setStatus("current")
_LoadEnergyLogLastDaysValue_Type = Integer32
_LoadEnergyLogLastDaysValue_Object = MibTableColumn
loadEnergyLogLastDaysValue = _LoadEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5, 1, 2),
    _LoadEnergyLogLastDaysValue_Type()
)
loadEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysValue.setStatus("current")


class _LoadEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type loadEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_LoadEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_LoadEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
loadEnergyLogLastWeeksNumberOfEntries = _LoadEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 6),
    _LoadEnergyLogLastWeeksNumberOfEntries_Type()
)
loadEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_LoadEnergyLogLastWeeksTable_Object = MibTable
loadEnergyLogLastWeeksTable = _LoadEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7)
)
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksTable.setStatus("current")
_LoadEnergyLogLastWeeksEntry_Object = MibTableRow
loadEnergyLogLastWeeksEntry = _LoadEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7, 1)
)
loadEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "loadEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksEntry.setStatus("current")


class _LoadEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type loadEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_LoadEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_LoadEnergyLogLastWeeksIndex_Object = MibTableColumn
loadEnergyLogLastWeeksIndex = _LoadEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7, 1, 1),
    _LoadEnergyLogLastWeeksIndex_Type()
)
loadEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksIndex.setStatus("current")
_LoadEnergyLogLastWeeksValue_Type = Integer32
_LoadEnergyLogLastWeeksValue_Object = MibTableColumn
loadEnergyLogLastWeeksValue = _LoadEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7, 1, 2),
    _LoadEnergyLogLastWeeksValue_Type()
)
loadEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksValue.setStatus("current")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10)
)


class _BatteryStatus_Type(Integer32):
    """Custom type batteryStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryStatus_Type.__name__ = "Integer32"
_BatteryStatus_Object = MibScalar
batteryStatus = _BatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 1),
    _BatteryStatus_Type()
)
batteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStatus.setStatus("current")


class _BatteryDescription_Type(DisplayString):
    """Custom type batteryDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BatteryDescription_Type.__name__ = "DisplayString"
_BatteryDescription_Object = MibScalar
batteryDescription = _BatteryDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 2),
    _BatteryDescription_Type()
)
batteryDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryDescription.setStatus("current")


class _BatteryReferenceVoltage_Type(Integer32):
    """Custom type batteryReferenceVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(840, 60417),
    )


_BatteryReferenceVoltage_Type.__name__ = "Integer32"
_BatteryReferenceVoltage_Object = MibScalar
batteryReferenceVoltage = _BatteryReferenceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 3),
    _BatteryReferenceVoltage_Type()
)
batteryReferenceVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryReferenceVoltage.setStatus("current")


class _BatteryFusesStatus_Type(Integer32):
    """Custom type batteryFusesStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryFusesStatus_Type.__name__ = "Integer32"
_BatteryFusesStatus_Object = MibScalar
batteryFusesStatus = _BatteryFusesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 4),
    _BatteryFusesStatus_Type()
)
batteryFusesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFusesStatus.setStatus("current")
_BatteryVoltage_ObjectIdentity = ObjectIdentity
batteryVoltage = _BatteryVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5)
)


class _BatteryVoltageStatus_Type(Integer32):
    """Custom type batteryVoltageStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryVoltageStatus_Type.__name__ = "Integer32"
_BatteryVoltageStatus_Object = MibScalar
batteryVoltageStatus = _BatteryVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 1),
    _BatteryVoltageStatus_Type()
)
batteryVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageStatus.setStatus("current")


class _BatteryVoltageDescription_Type(DisplayString):
    """Custom type batteryVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryVoltageDescription_Type.__name__ = "DisplayString"
_BatteryVoltageDescription_Object = MibScalar
batteryVoltageDescription = _BatteryVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 2),
    _BatteryVoltageDescription_Type()
)
batteryVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageDescription.setStatus("current")
_BatteryVoltageTrapRepeatCounter_Type = Counter32
_BatteryVoltageTrapRepeatCounter_Object = MibScalar
batteryVoltageTrapRepeatCounter = _BatteryVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 3),
    _BatteryVoltageTrapRepeatCounter_Type()
)
batteryVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryVoltageTrapRepeatCounter.setStatus("current")


class _BatteryVoltageAlarmEnable_Type(Integer32):
    """Custom type batteryVoltageAlarmEnable based on Integer32"""
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


_BatteryVoltageAlarmEnable_Type.__name__ = "Integer32"
_BatteryVoltageAlarmEnable_Object = MibScalar
batteryVoltageAlarmEnable = _BatteryVoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 4),
    _BatteryVoltageAlarmEnable_Type()
)
batteryVoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageAlarmEnable.setStatus("current")


class _BatteryVoltageValue_Type(Integer32):
    """Custom type batteryVoltageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_BatteryVoltageValue_Type.__name__ = "Integer32"
_BatteryVoltageValue_Object = MibScalar
batteryVoltageValue = _BatteryVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 5),
    _BatteryVoltageValue_Type()
)
batteryVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageValue.setStatus("current")


class _BatteryVoltageMajorHighLevel_Type(Integer32):
    """Custom type batteryVoltageMajorHighLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4300, 6000),
    )


_BatteryVoltageMajorHighLevel_Type.__name__ = "Integer32"
_BatteryVoltageMajorHighLevel_Object = MibScalar
batteryVoltageMajorHighLevel = _BatteryVoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 6),
    _BatteryVoltageMajorHighLevel_Type()
)
batteryVoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMajorHighLevel.setStatus("current")
_BatteryVoltageMinorHighLevel_Type = Integer32
_BatteryVoltageMinorHighLevel_Object = MibScalar
batteryVoltageMinorHighLevel = _BatteryVoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 7),
    _BatteryVoltageMinorHighLevel_Type()
)
batteryVoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMinorHighLevel.setStatus("current")


class _BatteryVoltageMinorLowLevel_Type(Integer32):
    """Custom type batteryVoltageMinorLowLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4300, 6000),
    )


_BatteryVoltageMinorLowLevel_Type.__name__ = "Integer32"
_BatteryVoltageMinorLowLevel_Object = MibScalar
batteryVoltageMinorLowLevel = _BatteryVoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 8),
    _BatteryVoltageMinorLowLevel_Type()
)
batteryVoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMinorLowLevel.setStatus("current")


class _BatteryVoltageMajorLowLevel_Type(Integer32):
    """Custom type batteryVoltageMajorLowLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4300, 6000),
    )


_BatteryVoltageMajorLowLevel_Type.__name__ = "Integer32"
_BatteryVoltageMajorLowLevel_Object = MibScalar
batteryVoltageMajorLowLevel = _BatteryVoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 9),
    _BatteryVoltageMajorLowLevel_Type()
)
batteryVoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMajorLowLevel.setStatus("current")
_BatteryCurrents_ObjectIdentity = ObjectIdentity
batteryCurrents = _BatteryCurrents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6)
)


class _BatteryCurrentsStatus_Type(Integer32):
    """Custom type batteryCurrentsStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryCurrentsStatus_Type.__name__ = "Integer32"
_BatteryCurrentsStatus_Object = MibScalar
batteryCurrentsStatus = _BatteryCurrentsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 1),
    _BatteryCurrentsStatus_Type()
)
batteryCurrentsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentsStatus.setStatus("current")


class _BatteryCurrentsDescription_Type(DisplayString):
    """Custom type batteryCurrentsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryCurrentsDescription_Type.__name__ = "DisplayString"
_BatteryCurrentsDescription_Object = MibScalar
batteryCurrentsDescription = _BatteryCurrentsDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 2),
    _BatteryCurrentsDescription_Type()
)
batteryCurrentsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsDescription.setStatus("current")
_BatteryCurrentsTrapRepeatCounter_Type = Counter32
_BatteryCurrentsTrapRepeatCounter_Object = MibScalar
batteryCurrentsTrapRepeatCounter = _BatteryCurrentsTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 3),
    _BatteryCurrentsTrapRepeatCounter_Type()
)
batteryCurrentsTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryCurrentsTrapRepeatCounter.setStatus("current")


class _BatteryCurrentsAlarmEnable_Type(Integer32):
    """Custom type batteryCurrentsAlarmEnable based on Integer32"""
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


_BatteryCurrentsAlarmEnable_Type.__name__ = "Integer32"
_BatteryCurrentsAlarmEnable_Object = MibScalar
batteryCurrentsAlarmEnable = _BatteryCurrentsAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 4),
    _BatteryCurrentsAlarmEnable_Type()
)
batteryCurrentsAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsAlarmEnable.setStatus("current")
_BatteryCurrentsValue_Type = Integer32
_BatteryCurrentsValue_Object = MibScalar
batteryCurrentsValue = _BatteryCurrentsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 5),
    _BatteryCurrentsValue_Type()
)
batteryCurrentsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentsValue.setStatus("current")
_BatteryCurrentsMajorHighLevel_Type = Integer32
_BatteryCurrentsMajorHighLevel_Object = MibScalar
batteryCurrentsMajorHighLevel = _BatteryCurrentsMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 6),
    _BatteryCurrentsMajorHighLevel_Type()
)
batteryCurrentsMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMajorHighLevel.setStatus("current")
_BatteryCurrentsMinorHighLevel_Type = Integer32
_BatteryCurrentsMinorHighLevel_Object = MibScalar
batteryCurrentsMinorHighLevel = _BatteryCurrentsMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 7),
    _BatteryCurrentsMinorHighLevel_Type()
)
batteryCurrentsMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMinorHighLevel.setStatus("current")
_BatteryCurrentsMinorLowLevel_Type = Integer32
_BatteryCurrentsMinorLowLevel_Object = MibScalar
batteryCurrentsMinorLowLevel = _BatteryCurrentsMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 8),
    _BatteryCurrentsMinorLowLevel_Type()
)
batteryCurrentsMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMinorLowLevel.setStatus("current")
_BatteryCurrentsMajorLowLevel_Type = Integer32
_BatteryCurrentsMajorLowLevel_Object = MibScalar
batteryCurrentsMajorLowLevel = _BatteryCurrentsMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 9),
    _BatteryCurrentsMajorLowLevel_Type()
)
batteryCurrentsMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMajorLowLevel.setStatus("current")
_BatteryTemperatures_ObjectIdentity = ObjectIdentity
batteryTemperatures = _BatteryTemperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7)
)


class _BatteryTemperaturesStatus_Type(Integer32):
    """Custom type batteryTemperaturesStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryTemperaturesStatus_Type.__name__ = "Integer32"
_BatteryTemperaturesStatus_Object = MibScalar
batteryTemperaturesStatus = _BatteryTemperaturesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 1),
    _BatteryTemperaturesStatus_Type()
)
batteryTemperaturesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperaturesStatus.setStatus("current")


class _BatteryTemperaturesDescription_Type(DisplayString):
    """Custom type batteryTemperaturesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTemperaturesDescription_Type.__name__ = "DisplayString"
_BatteryTemperaturesDescription_Object = MibScalar
batteryTemperaturesDescription = _BatteryTemperaturesDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 2),
    _BatteryTemperaturesDescription_Type()
)
batteryTemperaturesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesDescription.setStatus("current")
_BatteryTemperaturesTrapRepeatCounter_Type = Counter32
_BatteryTemperaturesTrapRepeatCounter_Object = MibScalar
batteryTemperaturesTrapRepeatCounter = _BatteryTemperaturesTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 3),
    _BatteryTemperaturesTrapRepeatCounter_Type()
)
batteryTemperaturesTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTemperaturesTrapRepeatCounter.setStatus("current")


class _BatteryTemperaturesAlarmEnable_Type(Integer32):
    """Custom type batteryTemperaturesAlarmEnable based on Integer32"""
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


_BatteryTemperaturesAlarmEnable_Type.__name__ = "Integer32"
_BatteryTemperaturesAlarmEnable_Object = MibScalar
batteryTemperaturesAlarmEnable = _BatteryTemperaturesAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 4),
    _BatteryTemperaturesAlarmEnable_Type()
)
batteryTemperaturesAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesAlarmEnable.setStatus("current")


class _BatteryTemperaturesValue_Type(Integer32):
    """Custom type batteryTemperaturesValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BatteryTemperaturesValue_Type.__name__ = "Integer32"
_BatteryTemperaturesValue_Object = MibScalar
batteryTemperaturesValue = _BatteryTemperaturesValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 5),
    _BatteryTemperaturesValue_Type()
)
batteryTemperaturesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperaturesValue.setStatus("current")
_BatteryTemperaturesMajorHighLevel_Type = Integer32
_BatteryTemperaturesMajorHighLevel_Object = MibScalar
batteryTemperaturesMajorHighLevel = _BatteryTemperaturesMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 6),
    _BatteryTemperaturesMajorHighLevel_Type()
)
batteryTemperaturesMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMajorHighLevel.setStatus("current")
_BatteryTemperaturesMinorHighLevel_Type = Integer32
_BatteryTemperaturesMinorHighLevel_Object = MibScalar
batteryTemperaturesMinorHighLevel = _BatteryTemperaturesMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 7),
    _BatteryTemperaturesMinorHighLevel_Type()
)
batteryTemperaturesMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMinorHighLevel.setStatus("current")
_BatteryTemperaturesMinorLowLevel_Type = Integer32
_BatteryTemperaturesMinorLowLevel_Object = MibScalar
batteryTemperaturesMinorLowLevel = _BatteryTemperaturesMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 8),
    _BatteryTemperaturesMinorLowLevel_Type()
)
batteryTemperaturesMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMinorLowLevel.setStatus("current")
_BatteryTemperaturesMajorLowLevel_Type = Integer32
_BatteryTemperaturesMajorLowLevel_Object = MibScalar
batteryTemperaturesMajorLowLevel = _BatteryTemperaturesMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 9),
    _BatteryTemperaturesMajorLowLevel_Type()
)
batteryTemperaturesMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMajorLowLevel.setStatus("current")
_BatteryTimeLeft_ObjectIdentity = ObjectIdentity
batteryTimeLeft = _BatteryTimeLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8)
)


class _BatteryTimeLeftStatus_Type(Integer32):
    """Custom type batteryTimeLeftStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryTimeLeftStatus_Type.__name__ = "Integer32"
_BatteryTimeLeftStatus_Object = MibScalar
batteryTimeLeftStatus = _BatteryTimeLeftStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 1),
    _BatteryTimeLeftStatus_Type()
)
batteryTimeLeftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTimeLeftStatus.setStatus("current")


class _BatteryTimeLeftDescription_Type(DisplayString):
    """Custom type batteryTimeLeftDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTimeLeftDescription_Type.__name__ = "DisplayString"
_BatteryTimeLeftDescription_Object = MibScalar
batteryTimeLeftDescription = _BatteryTimeLeftDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 2),
    _BatteryTimeLeftDescription_Type()
)
batteryTimeLeftDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftDescription.setStatus("current")
_BatteryTimeLeftTrapRepeatCounter_Type = Counter32
_BatteryTimeLeftTrapRepeatCounter_Object = MibScalar
batteryTimeLeftTrapRepeatCounter = _BatteryTimeLeftTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 3),
    _BatteryTimeLeftTrapRepeatCounter_Type()
)
batteryTimeLeftTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTimeLeftTrapRepeatCounter.setStatus("current")


class _BatteryTimeLeftAlarmEnable_Type(Integer32):
    """Custom type batteryTimeLeftAlarmEnable based on Integer32"""
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


_BatteryTimeLeftAlarmEnable_Type.__name__ = "Integer32"
_BatteryTimeLeftAlarmEnable_Object = MibScalar
batteryTimeLeftAlarmEnable = _BatteryTimeLeftAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 4),
    _BatteryTimeLeftAlarmEnable_Type()
)
batteryTimeLeftAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftAlarmEnable.setStatus("current")
_BatteryTimeLeftValue_Type = Integer32
_BatteryTimeLeftValue_Object = MibScalar
batteryTimeLeftValue = _BatteryTimeLeftValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 5),
    _BatteryTimeLeftValue_Type()
)
batteryTimeLeftValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTimeLeftValue.setStatus("current")
_BatteryTimeLeftMinorAlarmLevel_Type = Integer32
_BatteryTimeLeftMinorAlarmLevel_Object = MibScalar
batteryTimeLeftMinorAlarmLevel = _BatteryTimeLeftMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 6),
    _BatteryTimeLeftMinorAlarmLevel_Type()
)
batteryTimeLeftMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftMinorAlarmLevel.setStatus("current")
_BatteryTimeLeftMajorAlarmLevel_Type = Integer32
_BatteryTimeLeftMajorAlarmLevel_Object = MibScalar
batteryTimeLeftMajorAlarmLevel = _BatteryTimeLeftMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 7),
    _BatteryTimeLeftMajorAlarmLevel_Type()
)
batteryTimeLeftMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftMajorAlarmLevel.setStatus("current")
_BatteryRemainingCapacity_ObjectIdentity = ObjectIdentity
batteryRemainingCapacity = _BatteryRemainingCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9)
)


class _BatteryRemainingCapacityStatus_Type(Integer32):
    """Custom type batteryRemainingCapacityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryRemainingCapacityStatus_Type.__name__ = "Integer32"
_BatteryRemainingCapacityStatus_Object = MibScalar
batteryRemainingCapacityStatus = _BatteryRemainingCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 1),
    _BatteryRemainingCapacityStatus_Type()
)
batteryRemainingCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRemainingCapacityStatus.setStatus("current")


class _BatteryRemainingCapacityDescription_Type(DisplayString):
    """Custom type batteryRemainingCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryRemainingCapacityDescription_Type.__name__ = "DisplayString"
_BatteryRemainingCapacityDescription_Object = MibScalar
batteryRemainingCapacityDescription = _BatteryRemainingCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 2),
    _BatteryRemainingCapacityDescription_Type()
)
batteryRemainingCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityDescription.setStatus("current")
_BatteryRemainingCapacityTrapRepeatCounter_Type = Counter32
_BatteryRemainingCapacityTrapRepeatCounter_Object = MibScalar
batteryRemainingCapacityTrapRepeatCounter = _BatteryRemainingCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 3),
    _BatteryRemainingCapacityTrapRepeatCounter_Type()
)
batteryRemainingCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryRemainingCapacityTrapRepeatCounter.setStatus("current")


class _BatteryRemainingCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryRemainingCapacityAlarmEnable based on Integer32"""
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


_BatteryRemainingCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryRemainingCapacityAlarmEnable_Object = MibScalar
batteryRemainingCapacityAlarmEnable = _BatteryRemainingCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 4),
    _BatteryRemainingCapacityAlarmEnable_Type()
)
batteryRemainingCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityAlarmEnable.setStatus("current")
_BatteryRemainingCapacityValue_Type = Integer32
_BatteryRemainingCapacityValue_Object = MibScalar
batteryRemainingCapacityValue = _BatteryRemainingCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 5),
    _BatteryRemainingCapacityValue_Type()
)
batteryRemainingCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRemainingCapacityValue.setStatus("current")
_BatteryRemainingCapacityMinorLowLevel_Type = Integer32
_BatteryRemainingCapacityMinorLowLevel_Object = MibScalar
batteryRemainingCapacityMinorLowLevel = _BatteryRemainingCapacityMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 6),
    _BatteryRemainingCapacityMinorLowLevel_Type()
)
batteryRemainingCapacityMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityMinorLowLevel.setStatus("current")
_BatteryRemainingCapacityMajorLowLevel_Type = Integer32
_BatteryRemainingCapacityMajorLowLevel_Object = MibScalar
batteryRemainingCapacityMajorLowLevel = _BatteryRemainingCapacityMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 7),
    _BatteryRemainingCapacityMajorLowLevel_Type()
)
batteryRemainingCapacityMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityMajorLowLevel.setStatus("current")
_BatteryUsedCapacity_ObjectIdentity = ObjectIdentity
batteryUsedCapacity = _BatteryUsedCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10)
)


class _BatteryUsedCapacityStatus_Type(Integer32):
    """Custom type batteryUsedCapacityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryUsedCapacityStatus_Type.__name__ = "Integer32"
_BatteryUsedCapacityStatus_Object = MibScalar
batteryUsedCapacityStatus = _BatteryUsedCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 1),
    _BatteryUsedCapacityStatus_Type()
)
batteryUsedCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryUsedCapacityStatus.setStatus("current")


class _BatteryUsedCapacityDescription_Type(DisplayString):
    """Custom type batteryUsedCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryUsedCapacityDescription_Type.__name__ = "DisplayString"
_BatteryUsedCapacityDescription_Object = MibScalar
batteryUsedCapacityDescription = _BatteryUsedCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 2),
    _BatteryUsedCapacityDescription_Type()
)
batteryUsedCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityDescription.setStatus("current")
_BatteryUsedCapacityTrapRepeatCounter_Type = Counter32
_BatteryUsedCapacityTrapRepeatCounter_Object = MibScalar
batteryUsedCapacityTrapRepeatCounter = _BatteryUsedCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 3),
    _BatteryUsedCapacityTrapRepeatCounter_Type()
)
batteryUsedCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryUsedCapacityTrapRepeatCounter.setStatus("current")


class _BatteryUsedCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryUsedCapacityAlarmEnable based on Integer32"""
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


_BatteryUsedCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryUsedCapacityAlarmEnable_Object = MibScalar
batteryUsedCapacityAlarmEnable = _BatteryUsedCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 4),
    _BatteryUsedCapacityAlarmEnable_Type()
)
batteryUsedCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityAlarmEnable.setStatus("current")
_BatteryUsedCapacityValue_Type = Integer32
_BatteryUsedCapacityValue_Object = MibScalar
batteryUsedCapacityValue = _BatteryUsedCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 5),
    _BatteryUsedCapacityValue_Type()
)
batteryUsedCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryUsedCapacityValue.setStatus("current")
_BatteryUsedCapacityMajorAlarmLevel_Type = Integer32
_BatteryUsedCapacityMajorAlarmLevel_Object = MibScalar
batteryUsedCapacityMajorAlarmLevel = _BatteryUsedCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 6),
    _BatteryUsedCapacityMajorAlarmLevel_Type()
)
batteryUsedCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityMajorAlarmLevel.setStatus("current")
_BatteryUsedCapacityMinorAlarmLevel_Type = Integer32
_BatteryUsedCapacityMinorAlarmLevel_Object = MibScalar
batteryUsedCapacityMinorAlarmLevel = _BatteryUsedCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 7),
    _BatteryUsedCapacityMinorAlarmLevel_Type()
)
batteryUsedCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityMinorAlarmLevel.setStatus("current")
_BatteryTotalCapacity_ObjectIdentity = ObjectIdentity
batteryTotalCapacity = _BatteryTotalCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11)
)


class _BatteryTotalCapacityStatus_Type(Integer32):
    """Custom type batteryTotalCapacityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryTotalCapacityStatus_Type.__name__ = "Integer32"
_BatteryTotalCapacityStatus_Object = MibScalar
batteryTotalCapacityStatus = _BatteryTotalCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 1),
    _BatteryTotalCapacityStatus_Type()
)
batteryTotalCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTotalCapacityStatus.setStatus("current")


class _BatteryTotalCapacityDescription_Type(DisplayString):
    """Custom type batteryTotalCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTotalCapacityDescription_Type.__name__ = "DisplayString"
_BatteryTotalCapacityDescription_Object = MibScalar
batteryTotalCapacityDescription = _BatteryTotalCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 2),
    _BatteryTotalCapacityDescription_Type()
)
batteryTotalCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityDescription.setStatus("current")
_BatteryTotalCapacityTrapRepeatCounter_Type = Counter32
_BatteryTotalCapacityTrapRepeatCounter_Object = MibScalar
batteryTotalCapacityTrapRepeatCounter = _BatteryTotalCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 3),
    _BatteryTotalCapacityTrapRepeatCounter_Type()
)
batteryTotalCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTotalCapacityTrapRepeatCounter.setStatus("current")


class _BatteryTotalCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryTotalCapacityAlarmEnable based on Integer32"""
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


_BatteryTotalCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryTotalCapacityAlarmEnable_Object = MibScalar
batteryTotalCapacityAlarmEnable = _BatteryTotalCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 4),
    _BatteryTotalCapacityAlarmEnable_Type()
)
batteryTotalCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityAlarmEnable.setStatus("current")
_BatteryTotalCapacityValue_Type = Integer32
_BatteryTotalCapacityValue_Object = MibScalar
batteryTotalCapacityValue = _BatteryTotalCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 5),
    _BatteryTotalCapacityValue_Type()
)
batteryTotalCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTotalCapacityValue.setStatus("current")
_BatteryTotalCapacityMinorLowLevel_Type = Integer32
_BatteryTotalCapacityMinorLowLevel_Object = MibScalar
batteryTotalCapacityMinorLowLevel = _BatteryTotalCapacityMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 6),
    _BatteryTotalCapacityMinorLowLevel_Type()
)
batteryTotalCapacityMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityMinorLowLevel.setStatus("current")
_BatteryTotalCapacityMajorLowLevel_Type = Integer32
_BatteryTotalCapacityMajorLowLevel_Object = MibScalar
batteryTotalCapacityMajorLowLevel = _BatteryTotalCapacityMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 7),
    _BatteryTotalCapacityMajorLowLevel_Type()
)
batteryTotalCapacityMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityMajorLowLevel.setStatus("current")
_BatteryQuality_ObjectIdentity = ObjectIdentity
batteryQuality = _BatteryQuality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12)
)


class _BatteryQualityStatus_Type(Integer32):
    """Custom type batteryQualityStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryQualityStatus_Type.__name__ = "Integer32"
_BatteryQualityStatus_Object = MibScalar
batteryQualityStatus = _BatteryQualityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 1),
    _BatteryQualityStatus_Type()
)
batteryQualityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryQualityStatus.setStatus("current")


class _BatteryQualityDescription_Type(DisplayString):
    """Custom type batteryQualityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryQualityDescription_Type.__name__ = "DisplayString"
_BatteryQualityDescription_Object = MibScalar
batteryQualityDescription = _BatteryQualityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 2),
    _BatteryQualityDescription_Type()
)
batteryQualityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityDescription.setStatus("current")
_BatteryQualityTrapRepeatCounter_Type = Counter32
_BatteryQualityTrapRepeatCounter_Object = MibScalar
batteryQualityTrapRepeatCounter = _BatteryQualityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 3),
    _BatteryQualityTrapRepeatCounter_Type()
)
batteryQualityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryQualityTrapRepeatCounter.setStatus("current")


class _BatteryQualityAlarmEnable_Type(Integer32):
    """Custom type batteryQualityAlarmEnable based on Integer32"""
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


_BatteryQualityAlarmEnable_Type.__name__ = "Integer32"
_BatteryQualityAlarmEnable_Object = MibScalar
batteryQualityAlarmEnable = _BatteryQualityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 4),
    _BatteryQualityAlarmEnable_Type()
)
batteryQualityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityAlarmEnable.setStatus("current")
_BatteryQualityValue_Type = Integer32
_BatteryQualityValue_Object = MibScalar
batteryQualityValue = _BatteryQualityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 5),
    _BatteryQualityValue_Type()
)
batteryQualityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryQualityValue.setStatus("current")
_BatteryQualityMinorAlarmLevel_Type = Integer32
_BatteryQualityMinorAlarmLevel_Object = MibScalar
batteryQualityMinorAlarmLevel = _BatteryQualityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 6),
    _BatteryQualityMinorAlarmLevel_Type()
)
batteryQualityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityMinorAlarmLevel.setStatus("current")
_BatteryQualityMajorAlarmLevel_Type = Integer32
_BatteryQualityMajorAlarmLevel_Object = MibScalar
batteryQualityMajorAlarmLevel = _BatteryQualityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 7),
    _BatteryQualityMajorAlarmLevel_Type()
)
batteryQualityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityMajorAlarmLevel.setStatus("current")
_BatteryLVBD_ObjectIdentity = ObjectIdentity
batteryLVBD = _BatteryLVBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13)
)


class _BatteryLVBDStatus_Type(Integer32):
    """Custom type batteryLVBDStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryLVBDStatus_Type.__name__ = "Integer32"
_BatteryLVBDStatus_Object = MibScalar
batteryLVBDStatus = _BatteryLVBDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 1),
    _BatteryLVBDStatus_Type()
)
batteryLVBDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLVBDStatus.setStatus("current")


class _BatteryLVBDDescription_Type(DisplayString):
    """Custom type batteryLVBDDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryLVBDDescription_Type.__name__ = "DisplayString"
_BatteryLVBDDescription_Object = MibScalar
batteryLVBDDescription = _BatteryLVBDDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 2),
    _BatteryLVBDDescription_Type()
)
batteryLVBDDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDDescription.setStatus("current")
_BatteryLVBDTrapRepeatCounter_Type = Counter32
_BatteryLVBDTrapRepeatCounter_Object = MibScalar
batteryLVBDTrapRepeatCounter = _BatteryLVBDTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 3),
    _BatteryLVBDTrapRepeatCounter_Type()
)
batteryLVBDTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryLVBDTrapRepeatCounter.setStatus("current")


class _BatteryLVBDEnable_Type(Integer32):
    """Custom type batteryLVBDEnable based on Integer32"""
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


_BatteryLVBDEnable_Type.__name__ = "Integer32"
_BatteryLVBDEnable_Object = MibScalar
batteryLVBDEnable = _BatteryLVBDEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 4),
    _BatteryLVBDEnable_Type()
)
batteryLVBDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDEnable.setStatus("current")
_BatteryLVBDValue_Type = Integer32
_BatteryLVBDValue_Object = MibScalar
batteryLVBDValue = _BatteryLVBDValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 5),
    _BatteryLVBDValue_Type()
)
batteryLVBDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLVBDValue.setStatus("current")
_BatteryLVBDConnectVoltage_Type = Integer32
_BatteryLVBDConnectVoltage_Object = MibScalar
batteryLVBDConnectVoltage = _BatteryLVBDConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 6),
    _BatteryLVBDConnectVoltage_Type()
)
batteryLVBDConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDConnectVoltage.setStatus("current")
_BatteryLVBDDisconnectVoltage_Type = Integer32
_BatteryLVBDDisconnectVoltage_Object = MibScalar
batteryLVBDDisconnectVoltage = _BatteryLVBDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 7),
    _BatteryLVBDDisconnectVoltage_Type()
)
batteryLVBDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDDisconnectVoltage.setStatus("current")
_BatteryChargeCurrentLimit_ObjectIdentity = ObjectIdentity
batteryChargeCurrentLimit = _BatteryChargeCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 14)
)


class _BatteryChargeCurrentLimitEnable_Type(Integer32):
    """Custom type batteryChargeCurrentLimitEnable based on Integer32"""
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


_BatteryChargeCurrentLimitEnable_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitEnable_Object = MibScalar
batteryChargeCurrentLimitEnable = _BatteryChargeCurrentLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 14, 1),
    _BatteryChargeCurrentLimitEnable_Type()
)
batteryChargeCurrentLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitEnable.setStatus("current")


class _BatteryChargeCurrentLimitValue_Type(Integer32):
    """Custom type batteryChargeCurrentLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BatteryChargeCurrentLimitValue_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitValue_Object = MibScalar
batteryChargeCurrentLimitValue = _BatteryChargeCurrentLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 14, 2),
    _BatteryChargeCurrentLimitValue_Type()
)
batteryChargeCurrentLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitValue.setStatus("current")
_BatteryBoost_ObjectIdentity = ObjectIdentity
batteryBoost = _BatteryBoost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15)
)


class _BatteryBoostVoltage_Type(Integer32):
    """Custom type batteryBoostVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(870, 60418),
    )


_BatteryBoostVoltage_Type.__name__ = "Integer32"
_BatteryBoostVoltage_Object = MibScalar
batteryBoostVoltage = _BatteryBoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 1),
    _BatteryBoostVoltage_Type()
)
batteryBoostVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostVoltage.setStatus("current")


class _BatteryBoostCommand_Type(Integer32):
    """Custom type batteryBoostCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("startboost", 1),
          ("stopboost", 2))
    )


_BatteryBoostCommand_Type.__name__ = "Integer32"
_BatteryBoostCommand_Object = MibScalar
batteryBoostCommand = _BatteryBoostCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 2),
    _BatteryBoostCommand_Type()
)
batteryBoostCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostCommand.setStatus("current")
_BatteryBoostCurrentThreshold_Type = Integer32
_BatteryBoostCurrentThreshold_Object = MibScalar
batteryBoostCurrentThreshold = _BatteryBoostCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 3),
    _BatteryBoostCurrentThreshold_Type()
)
batteryBoostCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostCurrentThreshold.setStatus("current")


class _BatteryBoostManualMaxDuration_Type(Integer32):
    """Custom type batteryBoostManualMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BatteryBoostManualMaxDuration_Type.__name__ = "Integer32"
_BatteryBoostManualMaxDuration_Object = MibScalar
batteryBoostManualMaxDuration = _BatteryBoostManualMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 4),
    _BatteryBoostManualMaxDuration_Type()
)
batteryBoostManualMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostManualMaxDuration.setStatus("current")
_BatteryTest_ObjectIdentity = ObjectIdentity
batteryTest = _BatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16)
)
_BatteryTestVoltage_Type = Integer32
_BatteryTestVoltage_Object = MibScalar
batteryTestVoltage = _BatteryTestVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 1),
    _BatteryTestVoltage_Type()
)
batteryTestVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestVoltage.setStatus("current")


class _BatteryTestCommand_Type(Integer32):
    """Custom type batteryTestCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("starttest", 1),
          ("stoptest", 2))
    )


_BatteryTestCommand_Type.__name__ = "Integer32"
_BatteryTestCommand_Object = MibScalar
batteryTestCommand = _BatteryTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 2),
    _BatteryTestCommand_Type()
)
batteryTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestCommand.setStatus("current")


class _BatteryTestNumberOfResults_Type(Integer32):
    """Custom type batteryTestNumberOfResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BatteryTestNumberOfResults_Type.__name__ = "Integer32"
_BatteryTestNumberOfResults_Object = MibScalar
batteryTestNumberOfResults = _BatteryTestNumberOfResults_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 3),
    _BatteryTestNumberOfResults_Type()
)
batteryTestNumberOfResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestNumberOfResults.setStatus("current")
_BatteryTestResultTable_Object = MibTable
batteryTestResultTable = _BatteryTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4)
)
if mibBuilder.loadTexts:
    batteryTestResultTable.setStatus("current")
_BatteryTestResultEntry_Object = MibTableRow
batteryTestResultEntry = _BatteryTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1)
)
batteryTestResultEntry.setIndexNames(
    (0, "SP2-MIB", "batteryTestResultIndex"),
)
if mibBuilder.loadTexts:
    batteryTestResultEntry.setStatus("current")


class _BatteryTestResultIndex_Type(Integer32):
    """Custom type batteryTestResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BatteryTestResultIndex_Type.__name__ = "Integer32"
_BatteryTestResultIndex_Object = MibTableColumn
batteryTestResultIndex = _BatteryTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 1),
    _BatteryTestResultIndex_Type()
)
batteryTestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryTestResultIndex.setStatus("current")
_BatteryTestResultStartDateTime_Type = DateAndTime
_BatteryTestResultStartDateTime_Object = MibTableColumn
batteryTestResultStartDateTime = _BatteryTestResultStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 2),
    _BatteryTestResultStartDateTime_Type()
)
batteryTestResultStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultStartDateTime.setStatus("current")
_BatteryTestResultDuration_Type = Integer32
_BatteryTestResultDuration_Object = MibTableColumn
batteryTestResultDuration = _BatteryTestResultDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 3),
    _BatteryTestResultDuration_Type()
)
batteryTestResultDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultDuration.setStatus("current")
_BatteryTestResultDischarged_Type = Integer32
_BatteryTestResultDischarged_Object = MibTableColumn
batteryTestResultDischarged = _BatteryTestResultDischarged_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 4),
    _BatteryTestResultDischarged_Type()
)
batteryTestResultDischarged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultDischarged.setStatus("current")
_BatteryTestResultQuality_Type = Integer32
_BatteryTestResultQuality_Object = MibTableColumn
batteryTestResultQuality = _BatteryTestResultQuality_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 5),
    _BatteryTestResultQuality_Type()
)
batteryTestResultQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultQuality.setStatus("current")
_BatteryTempComp_ObjectIdentity = ObjectIdentity
batteryTempComp = _BatteryTempComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 17)
)


class _BatteryTempCompEnable_Type(Integer32):
    """Custom type batteryTempCompEnable based on Integer32"""
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


_BatteryTempCompEnable_Type.__name__ = "Integer32"
_BatteryTempCompEnable_Object = MibScalar
batteryTempCompEnable = _BatteryTempCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 17, 1),
    _BatteryTempCompEnable_Type()
)
batteryTempCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompEnable.setStatus("current")
_BatteryBank_ObjectIdentity = ObjectIdentity
batteryBank = _BatteryBank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18)
)


class _BatteryBankNumberOfBanks_Type(Integer32):
    """Custom type batteryBankNumberOfBanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BatteryBankNumberOfBanks_Type.__name__ = "Integer32"
_BatteryBankNumberOfBanks_Object = MibScalar
batteryBankNumberOfBanks = _BatteryBankNumberOfBanks_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 1),
    _BatteryBankNumberOfBanks_Type()
)
batteryBankNumberOfBanks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBankNumberOfBanks.setStatus("current")
_BatteryBankTable_Object = MibTable
batteryBankTable = _BatteryBankTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2)
)
if mibBuilder.loadTexts:
    batteryBankTable.setStatus("current")
_BatteryBankEntry_Object = MibTableRow
batteryBankEntry = _BatteryBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1)
)
batteryBankEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
)
if mibBuilder.loadTexts:
    batteryBankEntry.setStatus("current")


class _BatteryBankIndex_Type(Integer32):
    """Custom type batteryBankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryBankIndex_Type.__name__ = "Integer32"
_BatteryBankIndex_Object = MibTableColumn
batteryBankIndex = _BatteryBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 1),
    _BatteryBankIndex_Type()
)
batteryBankIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryBankIndex.setStatus("current")


class _BatteryBankStatus_Type(Integer32):
    """Custom type batteryBankStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryBankStatus_Type.__name__ = "Integer32"
_BatteryBankStatus_Object = MibTableColumn
batteryBankStatus = _BatteryBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 2),
    _BatteryBankStatus_Type()
)
batteryBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankStatus.setStatus("current")


class _BatteryBankNumberOfTemperatures_Type(Integer32):
    """Custom type batteryBankNumberOfTemperatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryBankNumberOfTemperatures_Type.__name__ = "Integer32"
_BatteryBankNumberOfTemperatures_Object = MibTableColumn
batteryBankNumberOfTemperatures = _BatteryBankNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 3),
    _BatteryBankNumberOfTemperatures_Type()
)
batteryBankNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankNumberOfTemperatures.setStatus("current")


class _BatteryBankNumberOfCurrents_Type(Integer32):
    """Custom type batteryBankNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryBankNumberOfCurrents_Type.__name__ = "Integer32"
_BatteryBankNumberOfCurrents_Object = MibTableColumn
batteryBankNumberOfCurrents = _BatteryBankNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 4),
    _BatteryBankNumberOfCurrents_Type()
)
batteryBankNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankNumberOfCurrents.setStatus("current")


class _BatteryBankNumberOfFuses_Type(Integer32):
    """Custom type batteryBankNumberOfFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryBankNumberOfFuses_Type.__name__ = "Integer32"
_BatteryBankNumberOfFuses_Object = MibTableColumn
batteryBankNumberOfFuses = _BatteryBankNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 5),
    _BatteryBankNumberOfFuses_Type()
)
batteryBankNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankNumberOfFuses.setStatus("current")
_BatteryBankTemperatureTable_Object = MibTable
batteryBankTemperatureTable = _BatteryBankTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3)
)
if mibBuilder.loadTexts:
    batteryBankTemperatureTable.setStatus("current")
_BatteryBankTemperatureEntry_Object = MibTableRow
batteryBankTemperatureEntry = _BatteryBankTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1)
)
batteryBankTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
    (0, "SP2-MIB", "batteryTemperatureIndex"),
)
if mibBuilder.loadTexts:
    batteryBankTemperatureEntry.setStatus("current")


class _BatteryTemperatureIndex_Type(Integer32):
    """Custom type batteryTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryTemperatureIndex_Type.__name__ = "Integer32"
_BatteryTemperatureIndex_Object = MibTableColumn
batteryTemperatureIndex = _BatteryTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 1),
    _BatteryTemperatureIndex_Type()
)
batteryTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryTemperatureIndex.setStatus("current")


class _BatteryTemperatureStatus_Type(Integer32):
    """Custom type batteryTemperatureStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryTemperatureStatus_Type.__name__ = "Integer32"
_BatteryTemperatureStatus_Object = MibTableColumn
batteryTemperatureStatus = _BatteryTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 2),
    _BatteryTemperatureStatus_Type()
)
batteryTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperatureStatus.setStatus("current")


class _BatteryTemperatureDescription_Type(DisplayString):
    """Custom type batteryTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTemperatureDescription_Type.__name__ = "DisplayString"
_BatteryTemperatureDescription_Object = MibTableColumn
batteryTemperatureDescription = _BatteryTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 3),
    _BatteryTemperatureDescription_Type()
)
batteryTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureDescription.setStatus("current")
_BatteryTemperatureTrapRepeatCounter_Type = Counter32
_BatteryTemperatureTrapRepeatCounter_Object = MibTableColumn
batteryTemperatureTrapRepeatCounter = _BatteryTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 4),
    _BatteryTemperatureTrapRepeatCounter_Type()
)
batteryTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTemperatureTrapRepeatCounter.setStatus("current")


class _BatteryTemperatureAlarmEnable_Type(Integer32):
    """Custom type batteryTemperatureAlarmEnable based on Integer32"""
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


_BatteryTemperatureAlarmEnable_Type.__name__ = "Integer32"
_BatteryTemperatureAlarmEnable_Object = MibTableColumn
batteryTemperatureAlarmEnable = _BatteryTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 5),
    _BatteryTemperatureAlarmEnable_Type()
)
batteryTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureAlarmEnable.setStatus("current")
_BatteryTemperatureValue_Type = Integer32
_BatteryTemperatureValue_Object = MibTableColumn
batteryTemperatureValue = _BatteryTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 6),
    _BatteryTemperatureValue_Type()
)
batteryTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperatureValue.setStatus("current")
_BatteryTemperatureMajorHighLevel_Type = Integer32
_BatteryTemperatureMajorHighLevel_Object = MibTableColumn
batteryTemperatureMajorHighLevel = _BatteryTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 7),
    _BatteryTemperatureMajorHighLevel_Type()
)
batteryTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMajorHighLevel.setStatus("current")
_BatteryTemperatureMinorHighLevel_Type = Integer32
_BatteryTemperatureMinorHighLevel_Object = MibTableColumn
batteryTemperatureMinorHighLevel = _BatteryTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 8),
    _BatteryTemperatureMinorHighLevel_Type()
)
batteryTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMinorHighLevel.setStatus("current")
_BatteryTemperatureMinorLowLevel_Type = Integer32
_BatteryTemperatureMinorLowLevel_Object = MibTableColumn
batteryTemperatureMinorLowLevel = _BatteryTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 9),
    _BatteryTemperatureMinorLowLevel_Type()
)
batteryTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMinorLowLevel.setStatus("current")
_BatteryTemperatureMajorLowLevel_Type = Integer32
_BatteryTemperatureMajorLowLevel_Object = MibTableColumn
batteryTemperatureMajorLowLevel = _BatteryTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 10),
    _BatteryTemperatureMajorLowLevel_Type()
)
batteryTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMajorLowLevel.setStatus("current")
_BatteryBankCurrentTable_Object = MibTable
batteryBankCurrentTable = _BatteryBankCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4)
)
if mibBuilder.loadTexts:
    batteryBankCurrentTable.setStatus("current")
_BatteryBankCurrentEntry_Object = MibTableRow
batteryBankCurrentEntry = _BatteryBankCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1)
)
batteryBankCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
    (0, "SP2-MIB", "batteryCurrentIndex"),
)
if mibBuilder.loadTexts:
    batteryBankCurrentEntry.setStatus("current")


class _BatteryCurrentIndex_Type(Integer32):
    """Custom type batteryCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryCurrentIndex_Type.__name__ = "Integer32"
_BatteryCurrentIndex_Object = MibTableColumn
batteryCurrentIndex = _BatteryCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 1),
    _BatteryCurrentIndex_Type()
)
batteryCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCurrentIndex.setStatus("current")


class _BatteryCurrentStatus_Type(Integer32):
    """Custom type batteryCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryCurrentStatus_Type.__name__ = "Integer32"
_BatteryCurrentStatus_Object = MibTableColumn
batteryCurrentStatus = _BatteryCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 2),
    _BatteryCurrentStatus_Type()
)
batteryCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentStatus.setStatus("current")


class _BatteryCurrentDescription_Type(DisplayString):
    """Custom type batteryCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryCurrentDescription_Type.__name__ = "DisplayString"
_BatteryCurrentDescription_Object = MibTableColumn
batteryCurrentDescription = _BatteryCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 3),
    _BatteryCurrentDescription_Type()
)
batteryCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentDescription.setStatus("current")
_BatteryCurrentTrapRepeatCounter_Type = Counter32
_BatteryCurrentTrapRepeatCounter_Object = MibTableColumn
batteryCurrentTrapRepeatCounter = _BatteryCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 4),
    _BatteryCurrentTrapRepeatCounter_Type()
)
batteryCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryCurrentTrapRepeatCounter.setStatus("current")


class _BatteryCurrentAlarmEnable_Type(Integer32):
    """Custom type batteryCurrentAlarmEnable based on Integer32"""
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


_BatteryCurrentAlarmEnable_Type.__name__ = "Integer32"
_BatteryCurrentAlarmEnable_Object = MibTableColumn
batteryCurrentAlarmEnable = _BatteryCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 5),
    _BatteryCurrentAlarmEnable_Type()
)
batteryCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentAlarmEnable.setStatus("current")
_BatteryCurrentValue_Type = Integer32
_BatteryCurrentValue_Object = MibTableColumn
batteryCurrentValue = _BatteryCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 6),
    _BatteryCurrentValue_Type()
)
batteryCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentValue.setStatus("current")
_BatteryCurrentMajorHighLevel_Type = Integer32
_BatteryCurrentMajorHighLevel_Object = MibTableColumn
batteryCurrentMajorHighLevel = _BatteryCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 7),
    _BatteryCurrentMajorHighLevel_Type()
)
batteryCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMajorHighLevel.setStatus("current")
_BatteryCurrentMinorHighLevel_Type = Integer32
_BatteryCurrentMinorHighLevel_Object = MibTableColumn
batteryCurrentMinorHighLevel = _BatteryCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 8),
    _BatteryCurrentMinorHighLevel_Type()
)
batteryCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMinorHighLevel.setStatus("current")
_BatteryCurrentMinorLowLevel_Type = Integer32
_BatteryCurrentMinorLowLevel_Object = MibTableColumn
batteryCurrentMinorLowLevel = _BatteryCurrentMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 9),
    _BatteryCurrentMinorLowLevel_Type()
)
batteryCurrentMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMinorLowLevel.setStatus("current")
_BatteryCurrentMajorLowLevel_Type = Integer32
_BatteryCurrentMajorLowLevel_Object = MibTableColumn
batteryCurrentMajorLowLevel = _BatteryCurrentMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 10),
    _BatteryCurrentMajorLowLevel_Type()
)
batteryCurrentMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMajorLowLevel.setStatus("current")
_BatteryBankFuseTable_Object = MibTable
batteryBankFuseTable = _BatteryBankFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5)
)
if mibBuilder.loadTexts:
    batteryBankFuseTable.setStatus("current")
_BatteryBankFuseEntry_Object = MibTableRow
batteryBankFuseEntry = _BatteryBankFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1)
)
batteryBankFuseEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
    (0, "SP2-MIB", "batteryFuseIndex"),
)
if mibBuilder.loadTexts:
    batteryBankFuseEntry.setStatus("current")


class _BatteryFuseIndex_Type(Integer32):
    """Custom type batteryFuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryFuseIndex_Type.__name__ = "Integer32"
_BatteryFuseIndex_Object = MibTableColumn
batteryFuseIndex = _BatteryFuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 1),
    _BatteryFuseIndex_Type()
)
batteryFuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryFuseIndex.setStatus("current")


class _BatteryFuseStatus_Type(Integer32):
    """Custom type batteryFuseStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryFuseStatus_Type.__name__ = "Integer32"
_BatteryFuseStatus_Object = MibTableColumn
batteryFuseStatus = _BatteryFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 2),
    _BatteryFuseStatus_Type()
)
batteryFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFuseStatus.setStatus("current")


class _BatteryFuseDescription_Type(DisplayString):
    """Custom type batteryFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryFuseDescription_Type.__name__ = "DisplayString"
_BatteryFuseDescription_Object = MibTableColumn
batteryFuseDescription = _BatteryFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 3),
    _BatteryFuseDescription_Type()
)
batteryFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryFuseDescription.setStatus("current")
_BatteryFuseTrapRepeatCounter_Type = Counter32
_BatteryFuseTrapRepeatCounter_Object = MibTableColumn
batteryFuseTrapRepeatCounter = _BatteryFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 4),
    _BatteryFuseTrapRepeatCounter_Type()
)
batteryFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryFuseTrapRepeatCounter.setStatus("current")


class _BatteryFuseAlarmEnable_Type(Integer32):
    """Custom type batteryFuseAlarmEnable based on Integer32"""
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


_BatteryFuseAlarmEnable_Type.__name__ = "Integer32"
_BatteryFuseAlarmEnable_Object = MibTableColumn
batteryFuseAlarmEnable = _BatteryFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 5),
    _BatteryFuseAlarmEnable_Type()
)
batteryFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryFuseAlarmEnable.setStatus("current")
_BatteryFuseValue_Type = Integer32
_BatteryFuseValue_Object = MibTableColumn
batteryFuseValue = _BatteryFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 6),
    _BatteryFuseValue_Type()
)
batteryFuseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFuseValue.setStatus("current")
_BatteryMonitors_ObjectIdentity = ObjectIdentity
batteryMonitors = _BatteryMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19)
)
_BatteryMonitorsNumberOfUnits_Type = Integer32
_BatteryMonitorsNumberOfUnits_Object = MibScalar
batteryMonitorsNumberOfUnits = _BatteryMonitorsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 1),
    _BatteryMonitorsNumberOfUnits_Type()
)
batteryMonitorsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorsNumberOfUnits.setStatus("current")
_BatteryMonitorsTable_Object = MibTable
batteryMonitorsTable = _BatteryMonitorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2)
)
if mibBuilder.loadTexts:
    batteryMonitorsTable.setStatus("current")
_BatteryMonitorsEntry_Object = MibTableRow
batteryMonitorsEntry = _BatteryMonitorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1)
)
batteryMonitorsEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorsEntry.setStatus("current")


class _BatteryMonitorIndex_Type(Integer32):
    """Custom type batteryMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryMonitorIndex_Type.__name__ = "Integer32"
_BatteryMonitorIndex_Object = MibTableColumn
batteryMonitorIndex = _BatteryMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 1),
    _BatteryMonitorIndex_Type()
)
batteryMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorIndex.setStatus("current")


class _BatteryMonitorNumberOfTemperatures_Type(Integer32):
    """Custom type batteryMonitorNumberOfTemperatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfTemperatures_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfTemperatures_Object = MibTableColumn
batteryMonitorNumberOfTemperatures = _BatteryMonitorNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 2),
    _BatteryMonitorNumberOfTemperatures_Type()
)
batteryMonitorNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfTemperatures.setStatus("current")


class _BatteryMonitorNumberOfCurrents_Type(Integer32):
    """Custom type batteryMonitorNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfCurrents_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfCurrents_Object = MibTableColumn
batteryMonitorNumberOfCurrents = _BatteryMonitorNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 3),
    _BatteryMonitorNumberOfCurrents_Type()
)
batteryMonitorNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfCurrents.setStatus("current")


class _BatteryMonitorNumberOfFuses_Type(Integer32):
    """Custom type batteryMonitorNumberOfFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfFuses_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfFuses_Object = MibTableColumn
batteryMonitorNumberOfFuses = _BatteryMonitorNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 4),
    _BatteryMonitorNumberOfFuses_Type()
)
batteryMonitorNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfFuses.setStatus("current")


class _BatteryMonitorNumberOfSymmetries_Type(Integer32):
    """Custom type batteryMonitorNumberOfSymmetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfSymmetries_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfSymmetries_Object = MibTableColumn
batteryMonitorNumberOfSymmetries = _BatteryMonitorNumberOfSymmetries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 5),
    _BatteryMonitorNumberOfSymmetries_Type()
)
batteryMonitorNumberOfSymmetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfSymmetries.setStatus("current")
_BatteryMonitorTemperatureTable_Object = MibTable
batteryMonitorTemperatureTable = _BatteryMonitorTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3)
)
if mibBuilder.loadTexts:
    batteryMonitorTemperatureTable.setStatus("current")
_BatteryMonitorTemperatureEntry_Object = MibTableRow
batteryMonitorTemperatureEntry = _BatteryMonitorTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1)
)
batteryMonitorTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorTemperatureIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorTemperatureEntry.setStatus("current")


class _BatteryMonitorTemperatureIndex_Type(Integer32):
    """Custom type batteryMonitorTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryMonitorTemperatureIndex_Type.__name__ = "Integer32"
_BatteryMonitorTemperatureIndex_Object = MibTableColumn
batteryMonitorTemperatureIndex = _BatteryMonitorTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 1),
    _BatteryMonitorTemperatureIndex_Type()
)
batteryMonitorTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureIndex.setStatus("current")


class _BatteryMonitorTemperatureStatus_Type(Integer32):
    """Custom type batteryMonitorTemperatureStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryMonitorTemperatureStatus_Type.__name__ = "Integer32"
_BatteryMonitorTemperatureStatus_Object = MibTableColumn
batteryMonitorTemperatureStatus = _BatteryMonitorTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 2),
    _BatteryMonitorTemperatureStatus_Type()
)
batteryMonitorTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureStatus.setStatus("current")


class _BatteryMonitorTemperatureDescription_Type(DisplayString):
    """Custom type batteryMonitorTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorTemperatureDescription_Type.__name__ = "DisplayString"
_BatteryMonitorTemperatureDescription_Object = MibTableColumn
batteryMonitorTemperatureDescription = _BatteryMonitorTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 3),
    _BatteryMonitorTemperatureDescription_Type()
)
batteryMonitorTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureDescription.setStatus("current")
_BatteryMonitorTemperatureTrapRepeatCounter_Type = Counter32
_BatteryMonitorTemperatureTrapRepeatCounter_Object = MibTableColumn
batteryMonitorTemperatureTrapRepeatCounter = _BatteryMonitorTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 4),
    _BatteryMonitorTemperatureTrapRepeatCounter_Type()
)
batteryMonitorTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureTrapRepeatCounter.setStatus("current")


class _BatteryMonitorTemperatureAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorTemperatureAlarmEnable based on Integer32"""
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


_BatteryMonitorTemperatureAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorTemperatureAlarmEnable_Object = MibTableColumn
batteryMonitorTemperatureAlarmEnable = _BatteryMonitorTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 5),
    _BatteryMonitorTemperatureAlarmEnable_Type()
)
batteryMonitorTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureAlarmEnable.setStatus("current")
_BatteryMonitorTemperatureValue_Type = Integer32
_BatteryMonitorTemperatureValue_Object = MibTableColumn
batteryMonitorTemperatureValue = _BatteryMonitorTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 6),
    _BatteryMonitorTemperatureValue_Type()
)
batteryMonitorTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureValue.setStatus("current")
_BatteryMonitorTemperatureMajorHighLevel_Type = Integer32
_BatteryMonitorTemperatureMajorHighLevel_Object = MibTableColumn
batteryMonitorTemperatureMajorHighLevel = _BatteryMonitorTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 7),
    _BatteryMonitorTemperatureMajorHighLevel_Type()
)
batteryMonitorTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMajorHighLevel.setStatus("current")
_BatteryMonitorTemperatureMinorHighLevel_Type = Integer32
_BatteryMonitorTemperatureMinorHighLevel_Object = MibTableColumn
batteryMonitorTemperatureMinorHighLevel = _BatteryMonitorTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 8),
    _BatteryMonitorTemperatureMinorHighLevel_Type()
)
batteryMonitorTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMinorHighLevel.setStatus("current")
_BatteryMonitorTemperatureMinorLowLevel_Type = Integer32
_BatteryMonitorTemperatureMinorLowLevel_Object = MibTableColumn
batteryMonitorTemperatureMinorLowLevel = _BatteryMonitorTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 9),
    _BatteryMonitorTemperatureMinorLowLevel_Type()
)
batteryMonitorTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMinorLowLevel.setStatus("current")
_BatteryMonitorTemperatureMajorLowLevel_Type = Integer32
_BatteryMonitorTemperatureMajorLowLevel_Object = MibTableColumn
batteryMonitorTemperatureMajorLowLevel = _BatteryMonitorTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 10),
    _BatteryMonitorTemperatureMajorLowLevel_Type()
)
batteryMonitorTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMajorLowLevel.setStatus("current")
_BatteryMonitorCurrentTable_Object = MibTable
batteryMonitorCurrentTable = _BatteryMonitorCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4)
)
if mibBuilder.loadTexts:
    batteryMonitorCurrentTable.setStatus("current")
_BatteryMonitorCurrentEntry_Object = MibTableRow
batteryMonitorCurrentEntry = _BatteryMonitorCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1)
)
batteryMonitorCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorCurrentIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorCurrentEntry.setStatus("current")


class _BatteryMonitorCurrentIndex_Type(Integer32):
    """Custom type batteryMonitorCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryMonitorCurrentIndex_Type.__name__ = "Integer32"
_BatteryMonitorCurrentIndex_Object = MibTableColumn
batteryMonitorCurrentIndex = _BatteryMonitorCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 1),
    _BatteryMonitorCurrentIndex_Type()
)
batteryMonitorCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorCurrentIndex.setStatus("current")


class _BatteryMonitorCurrentStatus_Type(Integer32):
    """Custom type batteryMonitorCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryMonitorCurrentStatus_Type.__name__ = "Integer32"
_BatteryMonitorCurrentStatus_Object = MibTableColumn
batteryMonitorCurrentStatus = _BatteryMonitorCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 2),
    _BatteryMonitorCurrentStatus_Type()
)
batteryMonitorCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorCurrentStatus.setStatus("current")


class _BatteryMonitorCurrentDescription_Type(DisplayString):
    """Custom type batteryMonitorCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorCurrentDescription_Type.__name__ = "DisplayString"
_BatteryMonitorCurrentDescription_Object = MibTableColumn
batteryMonitorCurrentDescription = _BatteryMonitorCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 3),
    _BatteryMonitorCurrentDescription_Type()
)
batteryMonitorCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentDescription.setStatus("current")
_BatteryMonitorCurrentTrapRepeatCounter_Type = Counter32
_BatteryMonitorCurrentTrapRepeatCounter_Object = MibTableColumn
batteryMonitorCurrentTrapRepeatCounter = _BatteryMonitorCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 4),
    _BatteryMonitorCurrentTrapRepeatCounter_Type()
)
batteryMonitorCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorCurrentTrapRepeatCounter.setStatus("current")


class _BatteryMonitorCurrentAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorCurrentAlarmEnable based on Integer32"""
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


_BatteryMonitorCurrentAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorCurrentAlarmEnable_Object = MibTableColumn
batteryMonitorCurrentAlarmEnable = _BatteryMonitorCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 5),
    _BatteryMonitorCurrentAlarmEnable_Type()
)
batteryMonitorCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentAlarmEnable.setStatus("current")
_BatteryMonitorCurrentValue_Type = Integer32
_BatteryMonitorCurrentValue_Object = MibTableColumn
batteryMonitorCurrentValue = _BatteryMonitorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 6),
    _BatteryMonitorCurrentValue_Type()
)
batteryMonitorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorCurrentValue.setStatus("current")
_BatteryMonitorCurrentMajorHighLevel_Type = Integer32
_BatteryMonitorCurrentMajorHighLevel_Object = MibTableColumn
batteryMonitorCurrentMajorHighLevel = _BatteryMonitorCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 7),
    _BatteryMonitorCurrentMajorHighLevel_Type()
)
batteryMonitorCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMajorHighLevel.setStatus("current")
_BatteryMonitorCurrentMinorHighLevel_Type = Integer32
_BatteryMonitorCurrentMinorHighLevel_Object = MibTableColumn
batteryMonitorCurrentMinorHighLevel = _BatteryMonitorCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 8),
    _BatteryMonitorCurrentMinorHighLevel_Type()
)
batteryMonitorCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMinorHighLevel.setStatus("current")
_BatteryMonitorCurrentMinorLowLevel_Type = Integer32
_BatteryMonitorCurrentMinorLowLevel_Object = MibTableColumn
batteryMonitorCurrentMinorLowLevel = _BatteryMonitorCurrentMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 9),
    _BatteryMonitorCurrentMinorLowLevel_Type()
)
batteryMonitorCurrentMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMinorLowLevel.setStatus("current")
_BatteryMonitorCurrentMajorLowLevel_Type = Integer32
_BatteryMonitorCurrentMajorLowLevel_Object = MibTableColumn
batteryMonitorCurrentMajorLowLevel = _BatteryMonitorCurrentMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 10),
    _BatteryMonitorCurrentMajorLowLevel_Type()
)
batteryMonitorCurrentMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMajorLowLevel.setStatus("current")
_BatteryMonitorFuseTable_Object = MibTable
batteryMonitorFuseTable = _BatteryMonitorFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5)
)
if mibBuilder.loadTexts:
    batteryMonitorFuseTable.setStatus("current")
_BatteryMonitorFuseEntry_Object = MibTableRow
batteryMonitorFuseEntry = _BatteryMonitorFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1)
)
batteryMonitorFuseEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorFuseIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorFuseEntry.setStatus("current")


class _BatteryMonitorFuseIndex_Type(Integer32):
    """Custom type batteryMonitorFuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryMonitorFuseIndex_Type.__name__ = "Integer32"
_BatteryMonitorFuseIndex_Object = MibTableColumn
batteryMonitorFuseIndex = _BatteryMonitorFuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 1),
    _BatteryMonitorFuseIndex_Type()
)
batteryMonitorFuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorFuseIndex.setStatus("current")


class _BatteryMonitorFuseStatus_Type(Integer32):
    """Custom type batteryMonitorFuseStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryMonitorFuseStatus_Type.__name__ = "Integer32"
_BatteryMonitorFuseStatus_Object = MibTableColumn
batteryMonitorFuseStatus = _BatteryMonitorFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 2),
    _BatteryMonitorFuseStatus_Type()
)
batteryMonitorFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorFuseStatus.setStatus("current")


class _BatteryMonitorFuseDescription_Type(DisplayString):
    """Custom type batteryMonitorFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorFuseDescription_Type.__name__ = "DisplayString"
_BatteryMonitorFuseDescription_Object = MibTableColumn
batteryMonitorFuseDescription = _BatteryMonitorFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 3),
    _BatteryMonitorFuseDescription_Type()
)
batteryMonitorFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorFuseDescription.setStatus("current")
_BatteryMonitorFuseTrapRepeatCounter_Type = Counter32
_BatteryMonitorFuseTrapRepeatCounter_Object = MibTableColumn
batteryMonitorFuseTrapRepeatCounter = _BatteryMonitorFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 4),
    _BatteryMonitorFuseTrapRepeatCounter_Type()
)
batteryMonitorFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorFuseTrapRepeatCounter.setStatus("current")


class _BatteryMonitorFuseAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorFuseAlarmEnable based on Integer32"""
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


_BatteryMonitorFuseAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorFuseAlarmEnable_Object = MibTableColumn
batteryMonitorFuseAlarmEnable = _BatteryMonitorFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 5),
    _BatteryMonitorFuseAlarmEnable_Type()
)
batteryMonitorFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorFuseAlarmEnable.setStatus("current")
_BatteryMonitorFuseValue_Type = Integer32
_BatteryMonitorFuseValue_Object = MibTableColumn
batteryMonitorFuseValue = _BatteryMonitorFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 6),
    _BatteryMonitorFuseValue_Type()
)
batteryMonitorFuseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorFuseValue.setStatus("current")
_BatteryMonitorSymmetryTable_Object = MibTable
batteryMonitorSymmetryTable = _BatteryMonitorSymmetryTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6)
)
if mibBuilder.loadTexts:
    batteryMonitorSymmetryTable.setStatus("current")
_BatteryMonitorSymmetryEntry_Object = MibTableRow
batteryMonitorSymmetryEntry = _BatteryMonitorSymmetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1)
)
batteryMonitorSymmetryEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorSymmetryIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorSymmetryEntry.setStatus("current")


class _BatteryMonitorSymmetryIndex_Type(Integer32):
    """Custom type batteryMonitorSymmetryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryMonitorSymmetryIndex_Type.__name__ = "Integer32"
_BatteryMonitorSymmetryIndex_Object = MibTableColumn
batteryMonitorSymmetryIndex = _BatteryMonitorSymmetryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 1),
    _BatteryMonitorSymmetryIndex_Type()
)
batteryMonitorSymmetryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryIndex.setStatus("current")


class _BatteryMonitorSymmetryStatus_Type(Integer32):
    """Custom type batteryMonitorSymmetryStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_BatteryMonitorSymmetryStatus_Type.__name__ = "Integer32"
_BatteryMonitorSymmetryStatus_Object = MibTableColumn
batteryMonitorSymmetryStatus = _BatteryMonitorSymmetryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 2),
    _BatteryMonitorSymmetryStatus_Type()
)
batteryMonitorSymmetryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryStatus.setStatus("current")


class _BatteryMonitorSymmetryDescription_Type(DisplayString):
    """Custom type batteryMonitorSymmetryDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorSymmetryDescription_Type.__name__ = "DisplayString"
_BatteryMonitorSymmetryDescription_Object = MibTableColumn
batteryMonitorSymmetryDescription = _BatteryMonitorSymmetryDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 3),
    _BatteryMonitorSymmetryDescription_Type()
)
batteryMonitorSymmetryDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryDescription.setStatus("current")
_BatteryMonitorSymmetryTrapRepeatCounter_Type = Counter32
_BatteryMonitorSymmetryTrapRepeatCounter_Object = MibTableColumn
batteryMonitorSymmetryTrapRepeatCounter = _BatteryMonitorSymmetryTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 4),
    _BatteryMonitorSymmetryTrapRepeatCounter_Type()
)
batteryMonitorSymmetryTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryTrapRepeatCounter.setStatus("current")


class _BatteryMonitorSymmetryAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorSymmetryAlarmEnable based on Integer32"""
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


_BatteryMonitorSymmetryAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorSymmetryAlarmEnable_Object = MibTableColumn
batteryMonitorSymmetryAlarmEnable = _BatteryMonitorSymmetryAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 5),
    _BatteryMonitorSymmetryAlarmEnable_Type()
)
batteryMonitorSymmetryAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryAlarmEnable.setStatus("current")
_BatteryMonitorSymmetryMeasureValue_Type = Integer32
_BatteryMonitorSymmetryMeasureValue_Object = MibTableColumn
batteryMonitorSymmetryMeasureValue = _BatteryMonitorSymmetryMeasureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 6),
    _BatteryMonitorSymmetryMeasureValue_Type()
)
batteryMonitorSymmetryMeasureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryMeasureValue.setStatus("current")
_BatteryMonitorSymmetryDeltaValue_Type = Integer32
_BatteryMonitorSymmetryDeltaValue_Object = MibTableColumn
batteryMonitorSymmetryDeltaValue = _BatteryMonitorSymmetryDeltaValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 7),
    _BatteryMonitorSymmetryDeltaValue_Type()
)
batteryMonitorSymmetryDeltaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryDeltaValue.setStatus("current")
_BatteryMonitorSymmetryMajorAlarmLevel_Type = Integer32
_BatteryMonitorSymmetryMajorAlarmLevel_Object = MibTableColumn
batteryMonitorSymmetryMajorAlarmLevel = _BatteryMonitorSymmetryMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 8),
    _BatteryMonitorSymmetryMajorAlarmLevel_Type()
)
batteryMonitorSymmetryMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryMajorAlarmLevel.setStatus("current")
_BatteryMonitorSymmetryMinorAlarmLevel_Type = Integer32
_BatteryMonitorSymmetryMinorAlarmLevel_Object = MibTableColumn
batteryMonitorSymmetryMinorAlarmLevel = _BatteryMonitorSymmetryMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 9),
    _BatteryMonitorSymmetryMinorAlarmLevel_Type()
)
batteryMonitorSymmetryMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryMinorAlarmLevel.setStatus("current")
_BatteryEnergyLog_ObjectIdentity = ObjectIdentity
batteryEnergyLog = _BatteryEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20)
)
_BatteryEnergyLogAccumulated_Type = Integer32
_BatteryEnergyLogAccumulated_Object = MibScalar
batteryEnergyLogAccumulated = _BatteryEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 1),
    _BatteryEnergyLogAccumulated_Type()
)
batteryEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogAccumulated.setStatus("current")


class _BatteryEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type batteryEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_BatteryEnergyLogLastHoursNumberOfEntries_Object = MibScalar
batteryEnergyLogLastHoursNumberOfEntries = _BatteryEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 2),
    _BatteryEnergyLogLastHoursNumberOfEntries_Type()
)
batteryEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursNumberOfEntries.setStatus("current")
_BatteryEnergyLogLastHoursTable_Object = MibTable
batteryEnergyLogLastHoursTable = _BatteryEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3)
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursTable.setStatus("current")
_BatteryEnergyLogLastHoursEntry_Object = MibTableRow
batteryEnergyLogLastHoursEntry = _BatteryEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3, 1)
)
batteryEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "batteryEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursEntry.setStatus("current")


class _BatteryEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type batteryEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_BatteryEnergyLogLastHoursIndex_Object = MibTableColumn
batteryEnergyLogLastHoursIndex = _BatteryEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3, 1, 1),
    _BatteryEnergyLogLastHoursIndex_Type()
)
batteryEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursIndex.setStatus("current")
_BatteryEnergyLogLastHoursValue_Type = Integer32
_BatteryEnergyLogLastHoursValue_Object = MibTableColumn
batteryEnergyLogLastHoursValue = _BatteryEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3, 1, 2),
    _BatteryEnergyLogLastHoursValue_Type()
)
batteryEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursValue.setStatus("current")


class _BatteryEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type batteryEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_BatteryEnergyLogLastDaysNumberOfEntries_Object = MibScalar
batteryEnergyLogLastDaysNumberOfEntries = _BatteryEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 4),
    _BatteryEnergyLogLastDaysNumberOfEntries_Type()
)
batteryEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysNumberOfEntries.setStatus("current")
_BatteryEnergyLogLastDaysTable_Object = MibTable
batteryEnergyLogLastDaysTable = _BatteryEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5)
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysTable.setStatus("current")
_BatteryEnergyLogLastDaysEntry_Object = MibTableRow
batteryEnergyLogLastDaysEntry = _BatteryEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5, 1)
)
batteryEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "batteryEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysEntry.setStatus("current")


class _BatteryEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type batteryEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_BatteryEnergyLogLastDaysIndex_Object = MibTableColumn
batteryEnergyLogLastDaysIndex = _BatteryEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5, 1, 1),
    _BatteryEnergyLogLastDaysIndex_Type()
)
batteryEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysIndex.setStatus("current")
_BatteryEnergyLogLastDaysValue_Type = Integer32
_BatteryEnergyLogLastDaysValue_Object = MibTableColumn
batteryEnergyLogLastDaysValue = _BatteryEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5, 1, 2),
    _BatteryEnergyLogLastDaysValue_Type()
)
batteryEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysValue.setStatus("current")


class _BatteryEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type batteryEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_BatteryEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
batteryEnergyLogLastWeeksNumberOfEntries = _BatteryEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 6),
    _BatteryEnergyLogLastWeeksNumberOfEntries_Type()
)
batteryEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_BatteryEnergyLogLastWeeksTable_Object = MibTable
batteryEnergyLogLastWeeksTable = _BatteryEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7)
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksTable.setStatus("current")
_BatteryEnergyLogLastWeeksEntry_Object = MibTableRow
batteryEnergyLogLastWeeksEntry = _BatteryEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7, 1)
)
batteryEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "batteryEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksEntry.setStatus("current")


class _BatteryEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type batteryEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_BatteryEnergyLogLastWeeksIndex_Object = MibTableColumn
batteryEnergyLogLastWeeksIndex = _BatteryEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7, 1, 1),
    _BatteryEnergyLogLastWeeksIndex_Type()
)
batteryEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksIndex.setStatus("current")
_BatteryEnergyLogLastWeeksValue_Type = Integer32
_BatteryEnergyLogLastWeeksValue_Object = MibTableColumn
batteryEnergyLogLastWeeksValue = _BatteryEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7, 1, 2),
    _BatteryEnergyLogLastWeeksValue_Type()
)
batteryEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksValue.setStatus("current")
_BatteryCycleLog_ObjectIdentity = ObjectIdentity
batteryCycleLog = _BatteryCycleLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21)
)
_BatteryCycleLogTotalCycles_Type = Integer32
_BatteryCycleLogTotalCycles_Object = MibScalar
batteryCycleLogTotalCycles = _BatteryCycleLogTotalCycles_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 1),
    _BatteryCycleLogTotalCycles_Type()
)
batteryCycleLogTotalCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogTotalCycles.setStatus("current")


class _BatteryCycleLogDaysNumberOfEntries_Type(Integer32):
    """Custom type batteryCycleLogDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryCycleLogDaysNumberOfEntries_Type.__name__ = "Integer32"
_BatteryCycleLogDaysNumberOfEntries_Object = MibScalar
batteryCycleLogDaysNumberOfEntries = _BatteryCycleLogDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 2),
    _BatteryCycleLogDaysNumberOfEntries_Type()
)
batteryCycleLogDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogDaysNumberOfEntries.setStatus("current")
_BatteryCycleLogDaysTable_Object = MibTable
batteryCycleLogDaysTable = _BatteryCycleLogDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3)
)
if mibBuilder.loadTexts:
    batteryCycleLogDaysTable.setStatus("current")
_BatteryCycleLogDaysEntry_Object = MibTableRow
batteryCycleLogDaysEntry = _BatteryCycleLogDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3, 1)
)
batteryCycleLogDaysEntry.setIndexNames(
    (0, "SP2-MIB", "batteryCycleLogDaysIndex"),
)
if mibBuilder.loadTexts:
    batteryCycleLogDaysEntry.setStatus("current")


class _BatteryCycleLogDaysIndex_Type(Integer32):
    """Custom type batteryCycleLogDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryCycleLogDaysIndex_Type.__name__ = "Integer32"
_BatteryCycleLogDaysIndex_Object = MibTableColumn
batteryCycleLogDaysIndex = _BatteryCycleLogDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3, 1, 1),
    _BatteryCycleLogDaysIndex_Type()
)
batteryCycleLogDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCycleLogDaysIndex.setStatus("current")
_BatteryCycleLogDaysValue_Type = Integer32
_BatteryCycleLogDaysValue_Object = MibTableColumn
batteryCycleLogDaysValue = _BatteryCycleLogDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3, 1, 2),
    _BatteryCycleLogDaysValue_Type()
)
batteryCycleLogDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogDaysValue.setStatus("current")


class _BatteryCycleLogWeeksNumberOfEntries_Type(Integer32):
    """Custom type batteryCycleLogWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryCycleLogWeeksNumberOfEntries_Type.__name__ = "Integer32"
_BatteryCycleLogWeeksNumberOfEntries_Object = MibScalar
batteryCycleLogWeeksNumberOfEntries = _BatteryCycleLogWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 4),
    _BatteryCycleLogWeeksNumberOfEntries_Type()
)
batteryCycleLogWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogWeeksNumberOfEntries.setStatus("current")
_BatteryCycleLogWeeksTable_Object = MibTable
batteryCycleLogWeeksTable = _BatteryCycleLogWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5)
)
if mibBuilder.loadTexts:
    batteryCycleLogWeeksTable.setStatus("current")
_BatteryCycleLogWeeksEntry_Object = MibTableRow
batteryCycleLogWeeksEntry = _BatteryCycleLogWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5, 1)
)
batteryCycleLogWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "batteryCycleLogWeeksIndex"),
)
if mibBuilder.loadTexts:
    batteryCycleLogWeeksEntry.setStatus("current")


class _BatteryCycleLogWeeksIndex_Type(Integer32):
    """Custom type batteryCycleLogWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryCycleLogWeeksIndex_Type.__name__ = "Integer32"
_BatteryCycleLogWeeksIndex_Object = MibTableColumn
batteryCycleLogWeeksIndex = _BatteryCycleLogWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5, 1, 1),
    _BatteryCycleLogWeeksIndex_Type()
)
batteryCycleLogWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCycleLogWeeksIndex.setStatus("current")
_BatteryCycleLogWeeksValue_Type = Integer32
_BatteryCycleLogWeeksValue_Object = MibTableColumn
batteryCycleLogWeeksValue = _BatteryCycleLogWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5, 1, 2),
    _BatteryCycleLogWeeksValue_Type()
)
batteryCycleLogWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogWeeksValue.setStatus("current")


class _BatteryCycleLogMonthsNumberOfEntries_Type(Integer32):
    """Custom type batteryCycleLogMonthsNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryCycleLogMonthsNumberOfEntries_Type.__name__ = "Integer32"
_BatteryCycleLogMonthsNumberOfEntries_Object = MibScalar
batteryCycleLogMonthsNumberOfEntries = _BatteryCycleLogMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 6),
    _BatteryCycleLogMonthsNumberOfEntries_Type()
)
batteryCycleLogMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogMonthsNumberOfEntries.setStatus("current")
_BatteryCycleLogMonthsTable_Object = MibTable
batteryCycleLogMonthsTable = _BatteryCycleLogMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7)
)
if mibBuilder.loadTexts:
    batteryCycleLogMonthsTable.setStatus("current")
_BatteryCycleLogMonthsEntry_Object = MibTableRow
batteryCycleLogMonthsEntry = _BatteryCycleLogMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7, 1)
)
batteryCycleLogMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "batteryCycleLogMonthsIndex"),
)
if mibBuilder.loadTexts:
    batteryCycleLogMonthsEntry.setStatus("current")


class _BatteryCycleLogMonthsIndex_Type(Integer32):
    """Custom type batteryCycleLogMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryCycleLogMonthsIndex_Type.__name__ = "Integer32"
_BatteryCycleLogMonthsIndex_Object = MibTableColumn
batteryCycleLogMonthsIndex = _BatteryCycleLogMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7, 1, 1),
    _BatteryCycleLogMonthsIndex_Type()
)
batteryCycleLogMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCycleLogMonthsIndex.setStatus("current")
_BatteryCycleLogMonthsValue_Type = Integer32
_BatteryCycleLogMonthsValue_Object = MibTableColumn
batteryCycleLogMonthsValue = _BatteryCycleLogMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7, 1, 2),
    _BatteryCycleLogMonthsValue_Type()
)
batteryCycleLogMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogMonthsValue.setStatus("current")
_Inputs_ObjectIdentity = ObjectIdentity
inputs = _Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11)
)
_InputControlUnitsTable_Object = MibTable
inputControlUnitsTable = _InputControlUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1)
)
if mibBuilder.loadTexts:
    inputControlUnitsTable.setStatus("current")
_InputControlUnitsEntry_Object = MibTableRow
inputControlUnitsEntry = _InputControlUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1, 1)
)
inputControlUnitsEntry.setIndexNames(
    (0, "SP2-MIB", "inputControlUnitIndex"),
)
if mibBuilder.loadTexts:
    inputControlUnitsEntry.setStatus("current")


class _InputControlUnitIndex_Type(Integer32):
    """Custom type inputControlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_InputControlUnitIndex_Type.__name__ = "Integer32"
_InputControlUnitIndex_Object = MibTableColumn
inputControlUnitIndex = _InputControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1, 1, 1),
    _InputControlUnitIndex_Type()
)
inputControlUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputControlUnitIndex.setStatus("current")


class _InputControlUnitNumberOfInputs_Type(Integer32):
    """Custom type inputControlUnitNumberOfInputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_InputControlUnitNumberOfInputs_Type.__name__ = "Integer32"
_InputControlUnitNumberOfInputs_Object = MibTableColumn
inputControlUnitNumberOfInputs = _InputControlUnitNumberOfInputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1, 1, 2),
    _InputControlUnitNumberOfInputs_Type()
)
inputControlUnitNumberOfInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputControlUnitNumberOfInputs.setStatus("current")
_InputControlUnitInputTable_Object = MibTable
inputControlUnitInputTable = _InputControlUnitInputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2)
)
if mibBuilder.loadTexts:
    inputControlUnitInputTable.setStatus("current")
_InputControlUnitInputEntry_Object = MibTableRow
inputControlUnitInputEntry = _InputControlUnitInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1)
)
inputControlUnitInputEntry.setIndexNames(
    (0, "SP2-MIB", "inputControlUnitIndex"),
    (0, "SP2-MIB", "inputControlUnitInputIndex"),
)
if mibBuilder.loadTexts:
    inputControlUnitInputEntry.setStatus("current")


class _InputControlUnitInputIndex_Type(Integer32):
    """Custom type inputControlUnitInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_InputControlUnitInputIndex_Type.__name__ = "Integer32"
_InputControlUnitInputIndex_Object = MibTableColumn
inputControlUnitInputIndex = _InputControlUnitInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 1),
    _InputControlUnitInputIndex_Type()
)
inputControlUnitInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputControlUnitInputIndex.setStatus("current")


class _InputControlUnitInputStatus_Type(Integer32):
    """Custom type inputControlUnitInputStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_InputControlUnitInputStatus_Type.__name__ = "Integer32"
_InputControlUnitInputStatus_Object = MibTableColumn
inputControlUnitInputStatus = _InputControlUnitInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 2),
    _InputControlUnitInputStatus_Type()
)
inputControlUnitInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputControlUnitInputStatus.setStatus("current")


class _InputControlUnitInputDescription_Type(DisplayString):
    """Custom type inputControlUnitInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputControlUnitInputDescription_Type.__name__ = "DisplayString"
_InputControlUnitInputDescription_Object = MibTableColumn
inputControlUnitInputDescription = _InputControlUnitInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 3),
    _InputControlUnitInputDescription_Type()
)
inputControlUnitInputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputDescription.setStatus("current")
_InputControlUnitInputTrapRepeatCounter_Type = Counter32
_InputControlUnitInputTrapRepeatCounter_Object = MibTableColumn
inputControlUnitInputTrapRepeatCounter = _InputControlUnitInputTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 4),
    _InputControlUnitInputTrapRepeatCounter_Type()
)
inputControlUnitInputTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inputControlUnitInputTrapRepeatCounter.setStatus("current")


class _InputControlUnitInputAlarmEnable_Type(Integer32):
    """Custom type inputControlUnitInputAlarmEnable based on Integer32"""
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


_InputControlUnitInputAlarmEnable_Type.__name__ = "Integer32"
_InputControlUnitInputAlarmEnable_Object = MibTableColumn
inputControlUnitInputAlarmEnable = _InputControlUnitInputAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 5),
    _InputControlUnitInputAlarmEnable_Type()
)
inputControlUnitInputAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputAlarmEnable.setStatus("current")
_InputControlUnitInputValue_Type = Integer32
_InputControlUnitInputValue_Object = MibTableColumn
inputControlUnitInputValue = _InputControlUnitInputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 6),
    _InputControlUnitInputValue_Type()
)
inputControlUnitInputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputValue.setStatus("current")


class _InputControlUnitInputConfiguration_Type(Integer32):
    """Custom type inputControlUnitInputConfiguration based on Integer32"""
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
        *(("clock", 5),
          ("diodeMatrix", 3),
          ("normallyClosed", 2),
          ("normallyOpen", 1),
          ("virtual", 6),
          ("voltage", 4))
    )


_InputControlUnitInputConfiguration_Type.__name__ = "Integer32"
_InputControlUnitInputConfiguration_Object = MibTableColumn
inputControlUnitInputConfiguration = _InputControlUnitInputConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 7),
    _InputControlUnitInputConfiguration_Type()
)
inputControlUnitInputConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputConfiguration.setStatus("current")
_InputIoUnitsTable_Object = MibTable
inputIoUnitsTable = _InputIoUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3)
)
if mibBuilder.loadTexts:
    inputIoUnitsTable.setStatus("current")
_InputIoUnitsEntry_Object = MibTableRow
inputIoUnitsEntry = _InputIoUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3, 1)
)
inputIoUnitsEntry.setIndexNames(
    (0, "SP2-MIB", "inputIoUnitIndex"),
)
if mibBuilder.loadTexts:
    inputIoUnitsEntry.setStatus("current")


class _InputIoUnitIndex_Type(Integer32):
    """Custom type inputIoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_InputIoUnitIndex_Type.__name__ = "Integer32"
_InputIoUnitIndex_Object = MibTableColumn
inputIoUnitIndex = _InputIoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3, 1, 1),
    _InputIoUnitIndex_Type()
)
inputIoUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputIoUnitIndex.setStatus("current")


class _InputIoUnitNumberOfInputs_Type(Integer32):
    """Custom type inputIoUnitNumberOfInputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_InputIoUnitNumberOfInputs_Type.__name__ = "Integer32"
_InputIoUnitNumberOfInputs_Object = MibTableColumn
inputIoUnitNumberOfInputs = _InputIoUnitNumberOfInputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3, 1, 2),
    _InputIoUnitNumberOfInputs_Type()
)
inputIoUnitNumberOfInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIoUnitNumberOfInputs.setStatus("current")
_InputIoUnitProgInputTable_Object = MibTable
inputIoUnitProgInputTable = _InputIoUnitProgInputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4)
)
if mibBuilder.loadTexts:
    inputIoUnitProgInputTable.setStatus("current")
_InputIoUnitProgInputEntry_Object = MibTableRow
inputIoUnitProgInputEntry = _InputIoUnitProgInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1)
)
inputIoUnitProgInputEntry.setIndexNames(
    (0, "SP2-MIB", "inputIoUnitIndex"),
    (0, "SP2-MIB", "inputIoUnitProgInputIndex"),
)
if mibBuilder.loadTexts:
    inputIoUnitProgInputEntry.setStatus("current")


class _InputIoUnitProgInputIndex_Type(Integer32):
    """Custom type inputIoUnitProgInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_InputIoUnitProgInputIndex_Type.__name__ = "Integer32"
_InputIoUnitProgInputIndex_Object = MibTableColumn
inputIoUnitProgInputIndex = _InputIoUnitProgInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 1),
    _InputIoUnitProgInputIndex_Type()
)
inputIoUnitProgInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputIoUnitProgInputIndex.setStatus("current")


class _InputIoUnitProgInputStatus_Type(Integer32):
    """Custom type inputIoUnitProgInputStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_InputIoUnitProgInputStatus_Type.__name__ = "Integer32"
_InputIoUnitProgInputStatus_Object = MibTableColumn
inputIoUnitProgInputStatus = _InputIoUnitProgInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 2),
    _InputIoUnitProgInputStatus_Type()
)
inputIoUnitProgInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIoUnitProgInputStatus.setStatus("current")


class _InputIoUnitProgInputDescription_Type(DisplayString):
    """Custom type inputIoUnitProgInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputIoUnitProgInputDescription_Type.__name__ = "DisplayString"
_InputIoUnitProgInputDescription_Object = MibTableColumn
inputIoUnitProgInputDescription = _InputIoUnitProgInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 3),
    _InputIoUnitProgInputDescription_Type()
)
inputIoUnitProgInputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIoUnitProgInputDescription.setStatus("current")
_InputIoUnitProgInputTrapRepeatCounter_Type = Counter32
_InputIoUnitProgInputTrapRepeatCounter_Object = MibTableColumn
inputIoUnitProgInputTrapRepeatCounter = _InputIoUnitProgInputTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 4),
    _InputIoUnitProgInputTrapRepeatCounter_Type()
)
inputIoUnitProgInputTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inputIoUnitProgInputTrapRepeatCounter.setStatus("current")


class _InputIoUnitProgInputAlarmEnable_Type(Integer32):
    """Custom type inputIoUnitProgInputAlarmEnable based on Integer32"""
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


_InputIoUnitProgInputAlarmEnable_Type.__name__ = "Integer32"
_InputIoUnitProgInputAlarmEnable_Object = MibTableColumn
inputIoUnitProgInputAlarmEnable = _InputIoUnitProgInputAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 5),
    _InputIoUnitProgInputAlarmEnable_Type()
)
inputIoUnitProgInputAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIoUnitProgInputAlarmEnable.setStatus("current")
_InputIoUnitProgInputValue_Type = Integer32
_InputIoUnitProgInputValue_Object = MibTableColumn
inputIoUnitProgInputValue = _InputIoUnitProgInputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 6),
    _InputIoUnitProgInputValue_Type()
)
inputIoUnitProgInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIoUnitProgInputValue.setStatus("current")


class _InputIoUnitProgInputConfiguration_Type(Integer32):
    """Custom type inputIoUnitProgInputConfiguration based on Integer32"""
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
        *(("diodeMatrix", 3),
          ("normallyClosed", 2),
          ("normallyOpen", 1),
          ("voltage", 4))
    )


_InputIoUnitProgInputConfiguration_Type.__name__ = "Integer32"
_InputIoUnitProgInputConfiguration_Object = MibTableColumn
inputIoUnitProgInputConfiguration = _InputIoUnitProgInputConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 7),
    _InputIoUnitProgInputConfiguration_Type()
)
inputIoUnitProgInputConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIoUnitProgInputConfiguration.setStatus("current")
_Outputs_ObjectIdentity = ObjectIdentity
outputs = _Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12)
)
_OutputControlUnitTable_Object = MibTable
outputControlUnitTable = _OutputControlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1)
)
if mibBuilder.loadTexts:
    outputControlUnitTable.setStatus("current")
_OutputControlUnitEntry_Object = MibTableRow
outputControlUnitEntry = _OutputControlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1, 1)
)
outputControlUnitEntry.setIndexNames(
    (0, "SP2-MIB", "outputControlUnitIndex"),
)
if mibBuilder.loadTexts:
    outputControlUnitEntry.setStatus("current")


class _OutputControlUnitIndex_Type(Integer32):
    """Custom type outputControlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OutputControlUnitIndex_Type.__name__ = "Integer32"
_OutputControlUnitIndex_Object = MibTableColumn
outputControlUnitIndex = _OutputControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1, 1, 1),
    _OutputControlUnitIndex_Type()
)
outputControlUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputControlUnitIndex.setStatus("current")


class _OutputControlUnitNumberOfOutputs_Type(Integer32):
    """Custom type outputControlUnitNumberOfOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_OutputControlUnitNumberOfOutputs_Type.__name__ = "Integer32"
_OutputControlUnitNumberOfOutputs_Object = MibTableColumn
outputControlUnitNumberOfOutputs = _OutputControlUnitNumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1, 1, 2),
    _OutputControlUnitNumberOfOutputs_Type()
)
outputControlUnitNumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputControlUnitNumberOfOutputs.setStatus("current")
_OutputControlUnitOutputTable_Object = MibTable
outputControlUnitOutputTable = _OutputControlUnitOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2)
)
if mibBuilder.loadTexts:
    outputControlUnitOutputTable.setStatus("current")
_OutputControlUnitOutputEntry_Object = MibTableRow
outputControlUnitOutputEntry = _OutputControlUnitOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1)
)
outputControlUnitOutputEntry.setIndexNames(
    (0, "SP2-MIB", "outputControlUnitIndex"),
    (0, "SP2-MIB", "outputControlUnitOutputIndex"),
)
if mibBuilder.loadTexts:
    outputControlUnitOutputEntry.setStatus("current")


class _OutputControlUnitOutputIndex_Type(Integer32):
    """Custom type outputControlUnitOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OutputControlUnitOutputIndex_Type.__name__ = "Integer32"
_OutputControlUnitOutputIndex_Object = MibTableColumn
outputControlUnitOutputIndex = _OutputControlUnitOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1, 1),
    _OutputControlUnitOutputIndex_Type()
)
outputControlUnitOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputControlUnitOutputIndex.setStatus("current")


class _OutputControlUnitOutputStatus_Type(Integer32):
    """Custom type outputControlUnitOutputStatus based on Integer32"""
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
        *(("connected", 3),
          ("disconnected", 2),
          ("energized", 1),
          ("notenergized", 0))
    )


_OutputControlUnitOutputStatus_Type.__name__ = "Integer32"
_OutputControlUnitOutputStatus_Object = MibTableColumn
outputControlUnitOutputStatus = _OutputControlUnitOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1, 2),
    _OutputControlUnitOutputStatus_Type()
)
outputControlUnitOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputControlUnitOutputStatus.setStatus("current")


class _OutputControlUnitOutputDescription_Type(DisplayString):
    """Custom type outputControlUnitOutputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OutputControlUnitOutputDescription_Type.__name__ = "DisplayString"
_OutputControlUnitOutputDescription_Object = MibTableColumn
outputControlUnitOutputDescription = _OutputControlUnitOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1, 3),
    _OutputControlUnitOutputDescription_Type()
)
outputControlUnitOutputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputControlUnitOutputDescription.setStatus("current")
_OutputIoUnitTable_Object = MibTable
outputIoUnitTable = _OutputIoUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3)
)
if mibBuilder.loadTexts:
    outputIoUnitTable.setStatus("current")
_OutputIoUnitEntry_Object = MibTableRow
outputIoUnitEntry = _OutputIoUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3, 1)
)
outputIoUnitEntry.setIndexNames(
    (0, "SP2-MIB", "outputIoUnitIndex"),
)
if mibBuilder.loadTexts:
    outputIoUnitEntry.setStatus("current")


class _OutputIoUnitIndex_Type(Integer32):
    """Custom type outputIoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OutputIoUnitIndex_Type.__name__ = "Integer32"
_OutputIoUnitIndex_Object = MibTableColumn
outputIoUnitIndex = _OutputIoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3, 1, 1),
    _OutputIoUnitIndex_Type()
)
outputIoUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputIoUnitIndex.setStatus("current")


class _OutputIoUnitNumberOfOutputs_Type(Integer32):
    """Custom type outputIoUnitNumberOfOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_OutputIoUnitNumberOfOutputs_Type.__name__ = "Integer32"
_OutputIoUnitNumberOfOutputs_Object = MibTableColumn
outputIoUnitNumberOfOutputs = _OutputIoUnitNumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3, 1, 2),
    _OutputIoUnitNumberOfOutputs_Type()
)
outputIoUnitNumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputIoUnitNumberOfOutputs.setStatus("current")
_OutputIoUnitOutputTable_Object = MibTable
outputIoUnitOutputTable = _OutputIoUnitOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4)
)
if mibBuilder.loadTexts:
    outputIoUnitOutputTable.setStatus("current")
_OutputIoUnitOutputEntry_Object = MibTableRow
outputIoUnitOutputEntry = _OutputIoUnitOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1)
)
outputIoUnitOutputEntry.setIndexNames(
    (0, "SP2-MIB", "outputIoUnitIndex"),
    (0, "SP2-MIB", "outputIoUnitOutputIndex"),
)
if mibBuilder.loadTexts:
    outputIoUnitOutputEntry.setStatus("current")


class _OutputIoUnitOutputIndex_Type(Integer32):
    """Custom type outputIoUnitOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OutputIoUnitOutputIndex_Type.__name__ = "Integer32"
_OutputIoUnitOutputIndex_Object = MibTableColumn
outputIoUnitOutputIndex = _OutputIoUnitOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1, 1),
    _OutputIoUnitOutputIndex_Type()
)
outputIoUnitOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputIoUnitOutputIndex.setStatus("current")


class _OutputIoUnitOutputStatus_Type(Integer32):
    """Custom type outputIoUnitOutputStatus based on Integer32"""
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
        *(("connected", 3),
          ("disconnected", 2),
          ("energized", 1),
          ("notenergized", 0))
    )


_OutputIoUnitOutputStatus_Type.__name__ = "Integer32"
_OutputIoUnitOutputStatus_Object = MibTableColumn
outputIoUnitOutputStatus = _OutputIoUnitOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1, 2),
    _OutputIoUnitOutputStatus_Type()
)
outputIoUnitOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputIoUnitOutputStatus.setStatus("current")


class _OutputIoUnitOutputDescription_Type(DisplayString):
    """Custom type outputIoUnitOutputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OutputIoUnitOutputDescription_Type.__name__ = "DisplayString"
_OutputIoUnitOutputDescription_Object = MibTableColumn
outputIoUnitOutputDescription = _OutputIoUnitOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1, 3),
    _OutputIoUnitOutputDescription_Type()
)
outputIoUnitOutputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputIoUnitOutputDescription.setStatus("current")
_ControlSystem_ObjectIdentity = ObjectIdentity
controlSystem = _ControlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13)
)


class _ControlSystemStatus_Type(Integer32):
    """Custom type controlSystemStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_ControlSystemStatus_Type.__name__ = "Integer32"
_ControlSystemStatus_Object = MibScalar
controlSystemStatus = _ControlSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 1),
    _ControlSystemStatus_Type()
)
controlSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemStatus.setStatus("current")


class _ControlSystemClock_Type(DateAndTime):
    """Custom type controlSystemClock based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 11),
    )


_ControlSystemClock_Type.__name__ = "DateAndTime"
_ControlSystemClock_Object = MibScalar
controlSystemClock = _ControlSystemClock_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 2),
    _ControlSystemClock_Type()
)
controlSystemClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemClock.setStatus("current")


class _ControlSystemNumberOfControlUnits_Type(Integer32):
    """Custom type controlSystemNumberOfControlUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ControlSystemNumberOfControlUnits_Type.__name__ = "Integer32"
_ControlSystemNumberOfControlUnits_Object = MibScalar
controlSystemNumberOfControlUnits = _ControlSystemNumberOfControlUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 3),
    _ControlSystemNumberOfControlUnits_Type()
)
controlSystemNumberOfControlUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemNumberOfControlUnits.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4)
)


class _SnmpSendOffTraps_Type(Integer32):
    """Custom type snmpSendOffTraps based on Integer32"""
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


_SnmpSendOffTraps_Type.__name__ = "Integer32"
_SnmpSendOffTraps_Object = MibScalar
snmpSendOffTraps = _SnmpSendOffTraps_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 1),
    _SnmpSendOffTraps_Type()
)
snmpSendOffTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSendOffTraps.setStatus("current")


class _SnmpTrapRepeatRate_Type(Integer32):
    """Custom type snmpTrapRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SnmpTrapRepeatRate_Type.__name__ = "Integer32"
_SnmpTrapRepeatRate_Object = MibScalar
snmpTrapRepeatRate = _SnmpTrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 2),
    _SnmpTrapRepeatRate_Type()
)
snmpTrapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRepeatRate.setStatus("current")


class _SnmpHeartBeatTrapRepeatRate_Type(Integer32):
    """Custom type snmpHeartBeatTrapRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SnmpHeartBeatTrapRepeatRate_Type.__name__ = "Integer32"
_SnmpHeartBeatTrapRepeatRate_Object = MibScalar
snmpHeartBeatTrapRepeatRate = _SnmpHeartBeatTrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 3),
    _SnmpHeartBeatTrapRepeatRate_Type()
)
snmpHeartBeatTrapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHeartBeatTrapRepeatRate.setStatus("current")


class _SnmpInhibitTraps_Type(Integer32):
    """Custom type snmpInhibitTraps based on Integer32"""
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


_SnmpInhibitTraps_Type.__name__ = "Integer32"
_SnmpInhibitTraps_Object = MibScalar
snmpInhibitTraps = _SnmpInhibitTraps_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 4),
    _SnmpInhibitTraps_Type()
)
snmpInhibitTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInhibitTraps.setStatus("current")


class _ControlSystemResetManualAlarms_Type(Integer32):
    """Custom type controlSystemResetManualAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("resetalarm", 1))
    )


_ControlSystemResetManualAlarms_Type.__name__ = "Integer32"
_ControlSystemResetManualAlarms_Object = MibScalar
controlSystemResetManualAlarms = _ControlSystemResetManualAlarms_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 5),
    _ControlSystemResetManualAlarms_Type()
)
controlSystemResetManualAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemResetManualAlarms.setStatus("current")


class _ControlSystemResetNumberOfModules_Type(Integer32):
    """Custom type controlSystemResetNumberOfModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("resetnumber", 1))
    )


_ControlSystemResetNumberOfModules_Type.__name__ = "Integer32"
_ControlSystemResetNumberOfModules_Object = MibScalar
controlSystemResetNumberOfModules = _ControlSystemResetNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 6),
    _ControlSystemResetNumberOfModules_Type()
)
controlSystemResetNumberOfModules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemResetNumberOfModules.setStatus("current")
_ControlSystemIoUnits_ObjectIdentity = ObjectIdentity
controlSystemIoUnits = _ControlSystemIoUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7)
)


class _ControlSystemIoUnitsNumberOfUnits_Type(Integer32):
    """Custom type controlSystemIoUnitsNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ControlSystemIoUnitsNumberOfUnits_Type.__name__ = "Integer32"
_ControlSystemIoUnitsNumberOfUnits_Object = MibScalar
controlSystemIoUnitsNumberOfUnits = _ControlSystemIoUnitsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 1),
    _ControlSystemIoUnitsNumberOfUnits_Type()
)
controlSystemIoUnitsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitsNumberOfUnits.setStatus("current")
_ControlSystemIoUnitsTable_Object = MibTable
controlSystemIoUnitsTable = _ControlSystemIoUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2)
)
if mibBuilder.loadTexts:
    controlSystemIoUnitsTable.setStatus("current")
_ControlSystemIoUnitsEntry_Object = MibTableRow
controlSystemIoUnitsEntry = _ControlSystemIoUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1)
)
controlSystemIoUnitsEntry.setIndexNames(
    (0, "SP2-MIB", "controlSystemIoUnitIndex"),
)
if mibBuilder.loadTexts:
    controlSystemIoUnitsEntry.setStatus("current")


class _ControlSystemIoUnitIndex_Type(Integer32):
    """Custom type controlSystemIoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ControlSystemIoUnitIndex_Type.__name__ = "Integer32"
_ControlSystemIoUnitIndex_Object = MibTableColumn
controlSystemIoUnitIndex = _ControlSystemIoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1, 1),
    _ControlSystemIoUnitIndex_Type()
)
controlSystemIoUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSystemIoUnitIndex.setStatus("current")


class _ControlSystemIoUnitNumberOfTemperatures_Type(Integer32):
    """Custom type controlSystemIoUnitNumberOfTemperatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ControlSystemIoUnitNumberOfTemperatures_Type.__name__ = "Integer32"
_ControlSystemIoUnitNumberOfTemperatures_Object = MibTableColumn
controlSystemIoUnitNumberOfTemperatures = _ControlSystemIoUnitNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1, 2),
    _ControlSystemIoUnitNumberOfTemperatures_Type()
)
controlSystemIoUnitNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitNumberOfTemperatures.setStatus("current")


class _ControlSystemIoUnitNumberOfFans_Type(Integer32):
    """Custom type controlSystemIoUnitNumberOfFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ControlSystemIoUnitNumberOfFans_Type.__name__ = "Integer32"
_ControlSystemIoUnitNumberOfFans_Object = MibTableColumn
controlSystemIoUnitNumberOfFans = _ControlSystemIoUnitNumberOfFans_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1, 3),
    _ControlSystemIoUnitNumberOfFans_Type()
)
controlSystemIoUnitNumberOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitNumberOfFans.setStatus("current")
_ControlSystemIoUnitTemperatureTable_Object = MibTable
controlSystemIoUnitTemperatureTable = _ControlSystemIoUnitTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3)
)
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureTable.setStatus("current")
_ControlSystemIoUnitTemperatureEntry_Object = MibTableRow
controlSystemIoUnitTemperatureEntry = _ControlSystemIoUnitTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1)
)
controlSystemIoUnitTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "controlSystemIoUnitIndex"),
    (0, "SP2-MIB", "controlSystemIoUnitTemperatureIndex"),
)
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureEntry.setStatus("current")


class _ControlSystemIoUnitTemperatureIndex_Type(Integer32):
    """Custom type controlSystemIoUnitTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ControlSystemIoUnitTemperatureIndex_Type.__name__ = "Integer32"
_ControlSystemIoUnitTemperatureIndex_Object = MibTableColumn
controlSystemIoUnitTemperatureIndex = _ControlSystemIoUnitTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 1),
    _ControlSystemIoUnitTemperatureIndex_Type()
)
controlSystemIoUnitTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureIndex.setStatus("current")


class _ControlSystemIoUnitTemperatureStatus_Type(Integer32):
    """Custom type controlSystemIoUnitTemperatureStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_ControlSystemIoUnitTemperatureStatus_Type.__name__ = "Integer32"
_ControlSystemIoUnitTemperatureStatus_Object = MibTableColumn
controlSystemIoUnitTemperatureStatus = _ControlSystemIoUnitTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 2),
    _ControlSystemIoUnitTemperatureStatus_Type()
)
controlSystemIoUnitTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureStatus.setStatus("current")


class _ControlSystemIoUnitTemperatureDescription_Type(DisplayString):
    """Custom type controlSystemIoUnitTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ControlSystemIoUnitTemperatureDescription_Type.__name__ = "DisplayString"
_ControlSystemIoUnitTemperatureDescription_Object = MibTableColumn
controlSystemIoUnitTemperatureDescription = _ControlSystemIoUnitTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 3),
    _ControlSystemIoUnitTemperatureDescription_Type()
)
controlSystemIoUnitTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureDescription.setStatus("current")
_ControlSystemIoUnitTemperatureTrapRepeatCounter_Type = Counter32
_ControlSystemIoUnitTemperatureTrapRepeatCounter_Object = MibTableColumn
controlSystemIoUnitTemperatureTrapRepeatCounter = _ControlSystemIoUnitTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 4),
    _ControlSystemIoUnitTemperatureTrapRepeatCounter_Type()
)
controlSystemIoUnitTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureTrapRepeatCounter.setStatus("current")


class _ControlSystemIoUnitTemperatureAlarmEnable_Type(Integer32):
    """Custom type controlSystemIoUnitTemperatureAlarmEnable based on Integer32"""
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


_ControlSystemIoUnitTemperatureAlarmEnable_Type.__name__ = "Integer32"
_ControlSystemIoUnitTemperatureAlarmEnable_Object = MibTableColumn
controlSystemIoUnitTemperatureAlarmEnable = _ControlSystemIoUnitTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 5),
    _ControlSystemIoUnitTemperatureAlarmEnable_Type()
)
controlSystemIoUnitTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureAlarmEnable.setStatus("current")
_ControlSystemIoUnitTemperatureValue_Type = Integer32
_ControlSystemIoUnitTemperatureValue_Object = MibTableColumn
controlSystemIoUnitTemperatureValue = _ControlSystemIoUnitTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 6),
    _ControlSystemIoUnitTemperatureValue_Type()
)
controlSystemIoUnitTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureValue.setStatus("current")
_ControlSystemIoUnitTemperatureMajorHighLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMajorHighLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMajorHighLevel = _ControlSystemIoUnitTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 7),
    _ControlSystemIoUnitTemperatureMajorHighLevel_Type()
)
controlSystemIoUnitTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMajorHighLevel.setStatus("current")
_ControlSystemIoUnitTemperatureMinorHighLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMinorHighLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMinorHighLevel = _ControlSystemIoUnitTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 8),
    _ControlSystemIoUnitTemperatureMinorHighLevel_Type()
)
controlSystemIoUnitTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMinorHighLevel.setStatus("current")
_ControlSystemIoUnitTemperatureMinorLowLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMinorLowLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMinorLowLevel = _ControlSystemIoUnitTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 9),
    _ControlSystemIoUnitTemperatureMinorLowLevel_Type()
)
controlSystemIoUnitTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMinorLowLevel.setStatus("current")
_ControlSystemIoUnitTemperatureMajorLowLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMajorLowLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMajorLowLevel = _ControlSystemIoUnitTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 10),
    _ControlSystemIoUnitTemperatureMajorLowLevel_Type()
)
controlSystemIoUnitTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMajorLowLevel.setStatus("current")
_ControlSystemIoUnitFanTable_Object = MibTable
controlSystemIoUnitFanTable = _ControlSystemIoUnitFanTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4)
)
if mibBuilder.loadTexts:
    controlSystemIoUnitFanTable.setStatus("current")
_ControlSystemIoUnitFanEntry_Object = MibTableRow
controlSystemIoUnitFanEntry = _ControlSystemIoUnitFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1)
)
controlSystemIoUnitFanEntry.setIndexNames(
    (0, "SP2-MIB", "controlSystemIoUnitIndex"),
    (0, "SP2-MIB", "controlSystemIoUnitFanIndex"),
)
if mibBuilder.loadTexts:
    controlSystemIoUnitFanEntry.setStatus("current")


class _ControlSystemIoUnitFanIndex_Type(Integer32):
    """Custom type controlSystemIoUnitFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ControlSystemIoUnitFanIndex_Type.__name__ = "Integer32"
_ControlSystemIoUnitFanIndex_Object = MibTableColumn
controlSystemIoUnitFanIndex = _ControlSystemIoUnitFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 1),
    _ControlSystemIoUnitFanIndex_Type()
)
controlSystemIoUnitFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanIndex.setStatus("current")
_ControlSystemIoUnitFanSpeedValue_Type = Integer32
_ControlSystemIoUnitFanSpeedValue_Object = MibTableColumn
controlSystemIoUnitFanSpeedValue = _ControlSystemIoUnitFanSpeedValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 2),
    _ControlSystemIoUnitFanSpeedValue_Type()
)
controlSystemIoUnitFanSpeedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanSpeedValue.setStatus("current")
_ControlSystemIoUnitFanSpeedDeviation_Type = Integer32
_ControlSystemIoUnitFanSpeedDeviation_Object = MibTableColumn
controlSystemIoUnitFanSpeedDeviation = _ControlSystemIoUnitFanSpeedDeviation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 3),
    _ControlSystemIoUnitFanSpeedDeviation_Type()
)
controlSystemIoUnitFanSpeedDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanSpeedDeviation.setStatus("current")
_ControlSystemIoUnitFanControl_Type = Integer32
_ControlSystemIoUnitFanControl_Object = MibTableColumn
controlSystemIoUnitFanControl = _ControlSystemIoUnitFanControl_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 4),
    _ControlSystemIoUnitFanControl_Type()
)
controlSystemIoUnitFanControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanControl.setStatus("current")
_ControlSystemInventory_ObjectIdentity = ObjectIdentity
controlSystemInventory = _ControlSystemInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8)
)


class _ControlUnitNumberOfUnits_Type(Integer32):
    """Custom type controlUnitNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ControlUnitNumberOfUnits_Type.__name__ = "Integer32"
_ControlUnitNumberOfUnits_Object = MibScalar
controlUnitNumberOfUnits = _ControlUnitNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 1),
    _ControlUnitNumberOfUnits_Type()
)
controlUnitNumberOfUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitNumberOfUnits.setStatus("current")
_ControlUnitTable_Object = MibTable
controlUnitTable = _ControlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2)
)
if mibBuilder.loadTexts:
    controlUnitTable.setStatus("current")
_ControlUnitEntry_Object = MibTableRow
controlUnitEntry = _ControlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1)
)
controlUnitEntry.setIndexNames(
    (0, "SP2-MIB", "controlUnitIndex"),
)
if mibBuilder.loadTexts:
    controlUnitEntry.setStatus("current")


class _ControlUnitIndex_Type(Integer32):
    """Custom type controlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ControlUnitIndex_Type.__name__ = "Integer32"
_ControlUnitIndex_Object = MibTableColumn
controlUnitIndex = _ControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 1),
    _ControlUnitIndex_Type()
)
controlUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlUnitIndex.setStatus("current")


class _ControlUnitDescription_Type(DisplayString):
    """Custom type controlUnitDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ControlUnitDescription_Type.__name__ = "DisplayString"
_ControlUnitDescription_Object = MibTableColumn
controlUnitDescription = _ControlUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 2),
    _ControlUnitDescription_Type()
)
controlUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitDescription.setStatus("current")


class _ControlUnitStatus_Type(Integer32):
    """Custom type controlUnitStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_ControlUnitStatus_Type.__name__ = "Integer32"
_ControlUnitStatus_Object = MibTableColumn
controlUnitStatus = _ControlUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 3),
    _ControlUnitStatus_Type()
)
controlUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitStatus.setStatus("current")


class _ControlUnitSerialNumber_Type(DisplayString):
    """Custom type controlUnitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ControlUnitSerialNumber_Type.__name__ = "DisplayString"
_ControlUnitSerialNumber_Object = MibTableColumn
controlUnitSerialNumber = _ControlUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 4),
    _ControlUnitSerialNumber_Type()
)
controlUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitSerialNumber.setStatus("current")


class _ControlUnitHwPartNumber_Type(DisplayString):
    """Custom type controlUnitHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ControlUnitHwPartNumber_Type.__name__ = "DisplayString"
_ControlUnitHwPartNumber_Object = MibTableColumn
controlUnitHwPartNumber = _ControlUnitHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 5),
    _ControlUnitHwPartNumber_Type()
)
controlUnitHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitHwPartNumber.setStatus("current")


class _ControlUnitHwVersion_Type(DisplayString):
    """Custom type controlUnitHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ControlUnitHwVersion_Type.__name__ = "DisplayString"
_ControlUnitHwVersion_Object = MibTableColumn
controlUnitHwVersion = _ControlUnitHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 6),
    _ControlUnitHwVersion_Type()
)
controlUnitHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitHwVersion.setStatus("current")


class _ControlUnitSwPartNumber_Type(DisplayString):
    """Custom type controlUnitSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ControlUnitSwPartNumber_Type.__name__ = "DisplayString"
_ControlUnitSwPartNumber_Object = MibTableColumn
controlUnitSwPartNumber = _ControlUnitSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 7),
    _ControlUnitSwPartNumber_Type()
)
controlUnitSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitSwPartNumber.setStatus("current")


class _ControlUnitSwVersion_Type(DisplayString):
    """Custom type controlUnitSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ControlUnitSwVersion_Type.__name__ = "DisplayString"
_ControlUnitSwVersion_Object = MibTableColumn
controlUnitSwVersion = _ControlUnitSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 8),
    _ControlUnitSwVersion_Type()
)
controlUnitSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitSwVersion.setStatus("current")
_CurrentMonitors_ObjectIdentity = ObjectIdentity
currentMonitors = _CurrentMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9)
)


class _CurrentMonitorsNumberOfUnits_Type(Integer32):
    """Custom type currentMonitorsNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CurrentMonitorsNumberOfUnits_Type.__name__ = "Integer32"
_CurrentMonitorsNumberOfUnits_Object = MibScalar
currentMonitorsNumberOfUnits = _CurrentMonitorsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 1),
    _CurrentMonitorsNumberOfUnits_Type()
)
currentMonitorsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorsNumberOfUnits.setStatus("current")
_CurrentMonitorsTable_Object = MibTable
currentMonitorsTable = _CurrentMonitorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2)
)
if mibBuilder.loadTexts:
    currentMonitorsTable.setStatus("current")
_CurrentMonitorsEntry_Object = MibTableRow
currentMonitorsEntry = _CurrentMonitorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1)
)
currentMonitorsEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorsEntry.setStatus("current")


class _CurrentMonitorIndex_Type(Integer32):
    """Custom type currentMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_CurrentMonitorIndex_Type.__name__ = "Integer32"
_CurrentMonitorIndex_Object = MibTableColumn
currentMonitorIndex = _CurrentMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 1),
    _CurrentMonitorIndex_Type()
)
currentMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorIndex.setStatus("current")


class _CurrentMonitorType_Type(Integer32):
    """Custom type currentMonitorType based on Integer32"""
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
        *(("dcdcCurrMonitor", 4),
          ("fuelcellCurrMonitor", 7),
          ("loadCurrMonitor", 2),
          ("rectCurrMonitor", 3),
          ("solarCurrMonitor", 5),
          ("stdLoadMonitor", 1),
          ("windCurrMonitor", 6))
    )


_CurrentMonitorType_Type.__name__ = "Integer32"
_CurrentMonitorType_Object = MibTableColumn
currentMonitorType = _CurrentMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 2),
    _CurrentMonitorType_Type()
)
currentMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorType.setStatus("current")
_CurrentMonitorId_Type = Integer32
_CurrentMonitorId_Object = MibTableColumn
currentMonitorId = _CurrentMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 3),
    _CurrentMonitorId_Type()
)
currentMonitorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorId.setStatus("current")


class _CurrentMonitorNumberOfFuses_Type(Integer32):
    """Custom type currentMonitorNumberOfFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CurrentMonitorNumberOfFuses_Type.__name__ = "Integer32"
_CurrentMonitorNumberOfFuses_Object = MibTableColumn
currentMonitorNumberOfFuses = _CurrentMonitorNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 4),
    _CurrentMonitorNumberOfFuses_Type()
)
currentMonitorNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorNumberOfFuses.setStatus("current")


class _CurrentMonitorNumberOfCurrents_Type(Integer32):
    """Custom type currentMonitorNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CurrentMonitorNumberOfCurrents_Type.__name__ = "Integer32"
_CurrentMonitorNumberOfCurrents_Object = MibTableColumn
currentMonitorNumberOfCurrents = _CurrentMonitorNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 5),
    _CurrentMonitorNumberOfCurrents_Type()
)
currentMonitorNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorNumberOfCurrents.setStatus("current")
_CurrentMonitorFuseTable_Object = MibTable
currentMonitorFuseTable = _CurrentMonitorFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3)
)
if mibBuilder.loadTexts:
    currentMonitorFuseTable.setStatus("current")
_CurrentMonitorFuseEntry_Object = MibTableRow
currentMonitorFuseEntry = _CurrentMonitorFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1)
)
currentMonitorFuseEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorFuseIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorFuseEntry.setStatus("current")


class _CurrentMonitorFuseIndex_Type(Integer32):
    """Custom type currentMonitorFuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CurrentMonitorFuseIndex_Type.__name__ = "Integer32"
_CurrentMonitorFuseIndex_Object = MibTableColumn
currentMonitorFuseIndex = _CurrentMonitorFuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 1),
    _CurrentMonitorFuseIndex_Type()
)
currentMonitorFuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorFuseIndex.setStatus("current")


class _CurrentMonitorFuseStatus_Type(Integer32):
    """Custom type currentMonitorFuseStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_CurrentMonitorFuseStatus_Type.__name__ = "Integer32"
_CurrentMonitorFuseStatus_Object = MibTableColumn
currentMonitorFuseStatus = _CurrentMonitorFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 2),
    _CurrentMonitorFuseStatus_Type()
)
currentMonitorFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorFuseStatus.setStatus("current")


class _CurrentMonitorFuseDescription_Type(DisplayString):
    """Custom type currentMonitorFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CurrentMonitorFuseDescription_Type.__name__ = "DisplayString"
_CurrentMonitorFuseDescription_Object = MibTableColumn
currentMonitorFuseDescription = _CurrentMonitorFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 3),
    _CurrentMonitorFuseDescription_Type()
)
currentMonitorFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorFuseDescription.setStatus("current")
_CurrentMonitorFuseTrapRepeatCounter_Type = Counter32
_CurrentMonitorFuseTrapRepeatCounter_Object = MibTableColumn
currentMonitorFuseTrapRepeatCounter = _CurrentMonitorFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 4),
    _CurrentMonitorFuseTrapRepeatCounter_Type()
)
currentMonitorFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentMonitorFuseTrapRepeatCounter.setStatus("current")


class _CurrentMonitorFuseAlarmEnable_Type(Integer32):
    """Custom type currentMonitorFuseAlarmEnable based on Integer32"""
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


_CurrentMonitorFuseAlarmEnable_Type.__name__ = "Integer32"
_CurrentMonitorFuseAlarmEnable_Object = MibTableColumn
currentMonitorFuseAlarmEnable = _CurrentMonitorFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 5),
    _CurrentMonitorFuseAlarmEnable_Type()
)
currentMonitorFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorFuseAlarmEnable.setStatus("current")
_CurrentMonitorFuseValue_Type = Integer32
_CurrentMonitorFuseValue_Object = MibTableColumn
currentMonitorFuseValue = _CurrentMonitorFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 6),
    _CurrentMonitorFuseValue_Type()
)
currentMonitorFuseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorFuseValue.setStatus("current")
_CurrentMonitorCurrentTable_Object = MibTable
currentMonitorCurrentTable = _CurrentMonitorCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4)
)
if mibBuilder.loadTexts:
    currentMonitorCurrentTable.setStatus("current")
_CurrentMonitorCurrentEntry_Object = MibTableRow
currentMonitorCurrentEntry = _CurrentMonitorCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1)
)
currentMonitorCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorCurrentEntry.setStatus("current")


class _CurrentMonitorCurrentIndex_Type(Integer32):
    """Custom type currentMonitorCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CurrentMonitorCurrentIndex_Type.__name__ = "Integer32"
_CurrentMonitorCurrentIndex_Object = MibTableColumn
currentMonitorCurrentIndex = _CurrentMonitorCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 1),
    _CurrentMonitorCurrentIndex_Type()
)
currentMonitorCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorCurrentIndex.setStatus("current")


class _CurrentMonitorCurrentStatus_Type(Integer32):
    """Custom type currentMonitorCurrentStatus based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("critical", 18),
          ("disabled", 4),
          ("disconnected", 5),
          ("error", 0),
          ("event", 12),
          ("majorAlarm", 3),
          ("majorHigh", 10),
          ("majorLow", 8),
          ("minorAlarm", 2),
          ("minorAndMajor", 7),
          ("minorHigh", 11),
          ("minorLow", 9),
          ("normal", 1),
          ("notPresent", 6),
          ("valueAmp", 14),
          ("valuePerCent", 17),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valueVolt", 13),
          ("warning", 19))
    )


_CurrentMonitorCurrentStatus_Type.__name__ = "Integer32"
_CurrentMonitorCurrentStatus_Object = MibTableColumn
currentMonitorCurrentStatus = _CurrentMonitorCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 2),
    _CurrentMonitorCurrentStatus_Type()
)
currentMonitorCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorCurrentStatus.setStatus("current")


class _CurrentMonitorCurrentDescription_Type(DisplayString):
    """Custom type currentMonitorCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CurrentMonitorCurrentDescription_Type.__name__ = "DisplayString"
_CurrentMonitorCurrentDescription_Object = MibTableColumn
currentMonitorCurrentDescription = _CurrentMonitorCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 3),
    _CurrentMonitorCurrentDescription_Type()
)
currentMonitorCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentDescription.setStatus("current")
_CurrentMonitorCurrentTrapRepeatCounter_Type = Counter32
_CurrentMonitorCurrentTrapRepeatCounter_Object = MibTableColumn
currentMonitorCurrentTrapRepeatCounter = _CurrentMonitorCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 4),
    _CurrentMonitorCurrentTrapRepeatCounter_Type()
)
currentMonitorCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentMonitorCurrentTrapRepeatCounter.setStatus("current")


class _CurrentMonitorCurrentAlarmEnable_Type(Integer32):
    """Custom type currentMonitorCurrentAlarmEnable based on Integer32"""
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


_CurrentMonitorCurrentAlarmEnable_Type.__name__ = "Integer32"
_CurrentMonitorCurrentAlarmEnable_Object = MibTableColumn
currentMonitorCurrentAlarmEnable = _CurrentMonitorCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 5),
    _CurrentMonitorCurrentAlarmEnable_Type()
)
currentMonitorCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentAlarmEnable.setStatus("current")
_CurrentMonitorCurrentValue_Type = Integer32
_CurrentMonitorCurrentValue_Object = MibTableColumn
currentMonitorCurrentValue = _CurrentMonitorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 6),
    _CurrentMonitorCurrentValue_Type()
)
currentMonitorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorCurrentValue.setStatus("current")
_CurrentMonitorCurrentMajorAlarmLevel_Type = Integer32
_CurrentMonitorCurrentMajorAlarmLevel_Object = MibTableColumn
currentMonitorCurrentMajorAlarmLevel = _CurrentMonitorCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 7),
    _CurrentMonitorCurrentMajorAlarmLevel_Type()
)
currentMonitorCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentMajorAlarmLevel.setStatus("current")
_CurrentMonitorCurrentMinorAlarmLevel_Type = Integer32
_CurrentMonitorCurrentMinorAlarmLevel_Object = MibTableColumn
currentMonitorCurrentMinorAlarmLevel = _CurrentMonitorCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 8),
    _CurrentMonitorCurrentMinorAlarmLevel_Type()
)
currentMonitorCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentMinorAlarmLevel.setStatus("current")
_CurrentMonitorEnergyLogAccumulatedTable_Object = MibTable
currentMonitorEnergyLogAccumulatedTable = _CurrentMonitorEnergyLogAccumulatedTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 5)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogAccumulatedTable.setStatus("current")
_CurrentMonitorEnergyLogAccumulatedEntry_Object = MibTableRow
currentMonitorEnergyLogAccumulatedEntry = _CurrentMonitorEnergyLogAccumulatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 5, 1)
)
currentMonitorEnergyLogAccumulatedEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogAccumulatedEntry.setStatus("current")
_CurrentMonitorEnergyLogAccumulated_Type = Integer32
_CurrentMonitorEnergyLogAccumulated_Object = MibTableColumn
currentMonitorEnergyLogAccumulated = _CurrentMonitorEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 5, 1, 1),
    _CurrentMonitorEnergyLogAccumulated_Type()
)
currentMonitorEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogAccumulated.setStatus("current")


class _CurrentMonitorEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CurrentMonitorEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastHoursNumberOfEntries_Object = MibScalar
currentMonitorEnergyLogLastHoursNumberOfEntries = _CurrentMonitorEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 6),
    _CurrentMonitorEnergyLogLastHoursNumberOfEntries_Type()
)
currentMonitorEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursNumberOfEntries.setStatus("current")
_CurrentMonitorEnergyLogLastHoursTable_Object = MibTable
currentMonitorEnergyLogLastHoursTable = _CurrentMonitorEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursTable.setStatus("current")
_CurrentMonitorEnergyLogLastHoursEntry_Object = MibTableRow
currentMonitorEnergyLogLastHoursEntry = _CurrentMonitorEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7, 1)
)
currentMonitorEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
    (0, "SP2-MIB", "currentMonitorEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursEntry.setStatus("current")


class _CurrentMonitorEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CurrentMonitorEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastHoursIndex_Object = MibTableColumn
currentMonitorEnergyLogLastHoursIndex = _CurrentMonitorEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7, 1, 1),
    _CurrentMonitorEnergyLogLastHoursIndex_Type()
)
currentMonitorEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursIndex.setStatus("current")
_CurrentMonitorEnergyLogLastHoursValue_Type = Integer32
_CurrentMonitorEnergyLogLastHoursValue_Object = MibTableColumn
currentMonitorEnergyLogLastHoursValue = _CurrentMonitorEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7, 1, 2),
    _CurrentMonitorEnergyLogLastHoursValue_Type()
)
currentMonitorEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursValue.setStatus("current")


class _CurrentMonitorEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CurrentMonitorEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastDaysNumberOfEntries_Object = MibScalar
currentMonitorEnergyLogLastDaysNumberOfEntries = _CurrentMonitorEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 8),
    _CurrentMonitorEnergyLogLastDaysNumberOfEntries_Type()
)
currentMonitorEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysNumberOfEntries.setStatus("current")
_CurrentMonitorEnergyLogLastDaysTable_Object = MibTable
currentMonitorEnergyLogLastDaysTable = _CurrentMonitorEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysTable.setStatus("current")
_CurrentMonitorEnergyLogLastDaysEntry_Object = MibTableRow
currentMonitorEnergyLogLastDaysEntry = _CurrentMonitorEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9, 1)
)
currentMonitorEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
    (0, "SP2-MIB", "currentMonitorEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysEntry.setStatus("current")


class _CurrentMonitorEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CurrentMonitorEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastDaysIndex_Object = MibTableColumn
currentMonitorEnergyLogLastDaysIndex = _CurrentMonitorEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9, 1, 1),
    _CurrentMonitorEnergyLogLastDaysIndex_Type()
)
currentMonitorEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysIndex.setStatus("current")
_CurrentMonitorEnergyLogLastDaysValue_Type = Integer32
_CurrentMonitorEnergyLogLastDaysValue_Object = MibTableColumn
currentMonitorEnergyLogLastDaysValue = _CurrentMonitorEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9, 1, 2),
    _CurrentMonitorEnergyLogLastDaysValue_Type()
)
currentMonitorEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysValue.setStatus("current")


class _CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
currentMonitorEnergyLogLastWeeksNumberOfEntries = _CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 10),
    _CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Type()
)
currentMonitorEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_CurrentMonitorEnergyLogLastWeeksTable_Object = MibTable
currentMonitorEnergyLogLastWeeksTable = _CurrentMonitorEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksTable.setStatus("current")
_CurrentMonitorEnergyLogLastWeeksEntry_Object = MibTableRow
currentMonitorEnergyLogLastWeeksEntry = _CurrentMonitorEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11, 1)
)
currentMonitorEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
    (0, "SP2-MIB", "currentMonitorEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksEntry.setStatus("current")


class _CurrentMonitorEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CurrentMonitorEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastWeeksIndex_Object = MibTableColumn
currentMonitorEnergyLogLastWeeksIndex = _CurrentMonitorEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11, 1, 1),
    _CurrentMonitorEnergyLogLastWeeksIndex_Type()
)
currentMonitorEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksIndex.setStatus("current")
_CurrentMonitorEnergyLogLastWeeksValue_Type = Integer32
_CurrentMonitorEnergyLogLastWeeksValue_Object = MibTableColumn
currentMonitorEnergyLogLastWeeksValue = _CurrentMonitorEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11, 1, 2),
    _CurrentMonitorEnergyLogLastWeeksValue_Type()
)
currentMonitorEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksValue.setStatus("current")
_AlarmGroups_ObjectIdentity = ObjectIdentity
alarmGroups = _AlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14)
)
_AlarmGroupTable_Object = MibTable
alarmGroupTable = _AlarmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1)
)
if mibBuilder.loadTexts:
    alarmGroupTable.setStatus("current")
_AlarmGroupEntry_Object = MibTableRow
alarmGroupEntry = _AlarmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1)
)
alarmGroupEntry.setIndexNames(
    (0, "SP2-MIB", "alarmGroupIndex"),
)
if mibBuilder.loadTexts:
    alarmGroupEntry.setStatus("current")


class _AlarmGroupIndex_Type(Integer32):
    """Custom type alarmGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49),
    )


_AlarmGroupIndex_Type.__name__ = "Integer32"
_AlarmGroupIndex_Object = MibTableColumn
alarmGroupIndex = _AlarmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1, 1),
    _AlarmGroupIndex_Type()
)
alarmGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmGroupIndex.setStatus("current")


class _AlarmGroupStatus_Type(Integer32):
    """Custom type alarmGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_AlarmGroupStatus_Type.__name__ = "Integer32"
_AlarmGroupStatus_Object = MibTableColumn
alarmGroupStatus = _AlarmGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1, 2),
    _AlarmGroupStatus_Type()
)
alarmGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGroupStatus.setStatus("current")


class _AlarmGroupDescription_Type(DisplayString):
    """Custom type alarmGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlarmGroupDescription_Type.__name__ = "DisplayString"
_AlarmGroupDescription_Object = MibTableColumn
alarmGroupDescription = _AlarmGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1, 3),
    _AlarmGroupDescription_Type()
)
alarmGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGroupDescription.setStatus("current")

# Managed Objects groups


# Notification objects

alarmPowerSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 1)
)
alarmPowerSystemTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmPowerSystemTrap.setStatus(
        "current"
    )

alarmBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 2)
)
alarmBatteryTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmBatteryTrap.setStatus(
        "current"
    )

alarmLoadGroupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 3)
)
alarmLoadGroupTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmLoadGroupTrap.setStatus(
        "current"
    )

alarmMainsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 4)
)
alarmMainsTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmMainsTrap.setStatus(
        "current"
    )

alarmRectifierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 5)
)
alarmRectifierTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmRectifierTrap.setStatus(
        "current"
    )

alarmControlSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 6)
)
alarmControlSystemTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmControlSystemTrap.setStatus(
        "current"
    )

alarmDcDcTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 7)
)
alarmDcDcTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmDcDcTrap.setStatus(
        "current"
    )

alarmInputsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 8)
)
alarmInputsTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmInputsTrap.setStatus(
        "current"
    )

alarmOutputsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 9)
)
alarmOutputsTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmOutputsTrap.setStatus(
        "current"
    )

alarmGeneratorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 10)
)
alarmGeneratorTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmGeneratorTrap.setStatus(
        "current"
    )

alarmSolarChargerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 11)
)
alarmSolarChargerTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmSolarChargerTrap.setStatus(
        "current"
    )

alarmWindChargerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 12)
)
alarmWindChargerTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmWindChargerTrap.setStatus(
        "current"
    )

infoHeartBeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 13)
)
infoHeartBeatTrap.setObjects(
    ("SP2-MIB", "alarmSubsysSourceDescr")
)
if mibBuilder.loadTexts:
    infoHeartBeatTrap.setStatus(
        "current"
    )


# Notifications groups

powerSystemTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 3)
)
powerSystemTrapsGroup.setObjects(
      *(("SP2-MIB", "alarmBatteryTrap"),
        ("SP2-MIB", "alarmControlSystemTrap"),
        ("SP2-MIB", "alarmDcDcTrap"),
        ("SP2-MIB", "alarmGeneratorTrap"),
        ("SP2-MIB", "alarmInputsTrap"),
        ("SP2-MIB", "alarmLoadGroupTrap"),
        ("SP2-MIB", "alarmMainsTrap"),
        ("SP2-MIB", "alarmOutputsTrap"),
        ("SP2-MIB", "alarmPowerSystemTrap"),
        ("SP2-MIB", "alarmRectifierTrap"),
        ("SP2-MIB", "alarmSolarChargerTrap"),
        ("SP2-MIB", "alarmWindChargerTrap"))
)
if mibBuilder.loadTexts:
    powerSystemTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SP2-MIB",
    **{"eltek": eltek,
       "eNexus": eNexus,
       "eltekTraps": eltekTraps,
       "powerAlarmVars": powerAlarmVars,
       "alarmSubsysSourceDescr": alarmSubsysSourceDescr,
       "alarmSubsysStatusOid": alarmSubsysStatusOid,
       "alarmSubsysStatusValue": alarmSubsysStatusValue,
       "alarmSubsysStatusOnOff": alarmSubsysStatusOnOff,
       "alarmMeasuredVarOid": alarmMeasuredVarOid,
       "alarmMeasuredVarValue": alarmMeasuredVarValue,
       "alarmTrapCounterVarValue": alarmTrapCounterVarValue,
       "powerSystemTraps": powerSystemTraps,
       "alarmPowerSystemTrap": alarmPowerSystemTrap,
       "alarmBatteryTrap": alarmBatteryTrap,
       "alarmLoadGroupTrap": alarmLoadGroupTrap,
       "alarmMainsTrap": alarmMainsTrap,
       "alarmRectifierTrap": alarmRectifierTrap,
       "alarmControlSystemTrap": alarmControlSystemTrap,
       "alarmDcDcTrap": alarmDcDcTrap,
       "alarmInputsTrap": alarmInputsTrap,
       "alarmOutputsTrap": alarmOutputsTrap,
       "alarmGeneratorTrap": alarmGeneratorTrap,
       "alarmSolarChargerTrap": alarmSolarChargerTrap,
       "alarmWindChargerTrap": alarmWindChargerTrap,
       "infoHeartBeatTrap": infoHeartBeatTrap,
       "powerSystemTrapsGroup": powerSystemTrapsGroup,
       "powerSystem": powerSystem,
       "powerSystemStatus": powerSystemStatus,
       "powerSystemType": powerSystemType,
       "powerSystemMode": powerSystemMode,
       "powerSystemCompany": powerSystemCompany,
       "powerSystemSite": powerSystemSite,
       "powerSystemModel": powerSystemModel,
       "powerSystemSerialNumber": powerSystemSerialNumber,
       "powerSystemInstallDate": powerSystemInstallDate,
       "powerSystemNominalVoltage": powerSystemNominalVoltage,
       "powerSystemLongitude": powerSystemLongitude,
       "powerSystemLongitudeDecimal": powerSystemLongitudeDecimal,
       "powerSystemLatitude": powerSystemLatitude,
       "powerSystemLatitudeDecimal": powerSystemLatitudeDecimal,
       "powerSystemElevation": powerSystemElevation,
       "powerSystemCurrentDecimalSetting": powerSystemCurrentDecimalSetting,
       "powerSystemTemperatureScale": powerSystemTemperatureScale,
       "powerSystemCapacityScale": powerSystemCapacityScale,
       "mains": mains,
       "mainsStatus": mainsStatus,
       "mainsMainsFailure": mainsMainsFailure,
       "mainsMainsFailureStatus": mainsMainsFailureStatus,
       "mainsMainsFailureDescription": mainsMainsFailureDescription,
       "mainsMainsFailureTrapRepeatCounter": mainsMainsFailureTrapRepeatCounter,
       "mainsMainsFailureAlarmEnable": mainsMainsFailureAlarmEnable,
       "mainsMainsFailureValue": mainsMainsFailureValue,
       "mainsMainsFailureMajorAlarmLevel": mainsMainsFailureMajorAlarmLevel,
       "mainsMainsFailureMinorAlarmLevel": mainsMainsFailureMinorAlarmLevel,
       "mainsNumberOfPhases": mainsNumberOfPhases,
       "mainsVoltageTable": mainsVoltageTable,
       "mainsVoltageEntry": mainsVoltageEntry,
       "mainsVoltageIndex": mainsVoltageIndex,
       "mainsVoltageStatus": mainsVoltageStatus,
       "mainsVoltageDescription": mainsVoltageDescription,
       "mainsVoltageTrapRepeatCounter": mainsVoltageTrapRepeatCounter,
       "mainsVoltageAlarmEnable": mainsVoltageAlarmEnable,
       "mainsVoltageValue": mainsVoltageValue,
       "mainsVoltageMajorHighLevel": mainsVoltageMajorHighLevel,
       "mainsVoltageMinorHighLevel": mainsVoltageMinorHighLevel,
       "mainsVoltageMinorLowLevel": mainsVoltageMinorLowLevel,
       "mainsVoltageMajorLowLevel": mainsVoltageMajorLowLevel,
       "mainsMonitors": mainsMonitors,
       "mainsMonitorsNumberOfUnits": mainsMonitorsNumberOfUnits,
       "mainsMonitorsTable": mainsMonitorsTable,
       "mainsMonitorsEntry": mainsMonitorsEntry,
       "mainsMonitorIndex": mainsMonitorIndex,
       "mainsMonitorNumberOfVoltages": mainsMonitorNumberOfVoltages,
       "mainsMonitorNumberOfCurrents": mainsMonitorNumberOfCurrents,
       "mainsMonitorNumberOfFrequencies": mainsMonitorNumberOfFrequencies,
       "mainsMonitorVoltageTable": mainsMonitorVoltageTable,
       "mainsMonitorVoltageEntry": mainsMonitorVoltageEntry,
       "mainsMonitorPhaseIndex": mainsMonitorPhaseIndex,
       "mainsMonitorVoltageStatus": mainsMonitorVoltageStatus,
       "mainsMonitorVoltageDescription": mainsMonitorVoltageDescription,
       "mainsMonitorVoltageTrapRepeatCounter": mainsMonitorVoltageTrapRepeatCounter,
       "mainsMonitorVoltageAlarmEnable": mainsMonitorVoltageAlarmEnable,
       "mainsMonitorVoltageValue": mainsMonitorVoltageValue,
       "mainsMonitorVoltageMajorHighLevel": mainsMonitorVoltageMajorHighLevel,
       "mainsMonitorVoltageMinorHighLevel": mainsMonitorVoltageMinorHighLevel,
       "mainsMonitorVoltageMinorLowLevel": mainsMonitorVoltageMinorLowLevel,
       "mainsMonitorVoltageMajorLowLevel": mainsMonitorVoltageMajorLowLevel,
       "mainsMonitorCurrentTable": mainsMonitorCurrentTable,
       "mainsMonitorCurrentEntry": mainsMonitorCurrentEntry,
       "mainsMonitorCurrentStatus": mainsMonitorCurrentStatus,
       "mainsMonitorCurrentDescription": mainsMonitorCurrentDescription,
       "mainsMonitorCurrentTrapRepeatCounter": mainsMonitorCurrentTrapRepeatCounter,
       "mainsMonitorCurrentAlarmEnable": mainsMonitorCurrentAlarmEnable,
       "mainsMonitorCurrentValue": mainsMonitorCurrentValue,
       "mainsMonitorCurrentMajorHighLevel": mainsMonitorCurrentMajorHighLevel,
       "mainsMonitorCurrentMinorHighLevel": mainsMonitorCurrentMinorHighLevel,
       "mainsMonitorFrequencyTable": mainsMonitorFrequencyTable,
       "mainsMonitorFrequencyEntry": mainsMonitorFrequencyEntry,
       "mainsMonitorFrequencyStatus": mainsMonitorFrequencyStatus,
       "mainsMonitorFrequencyDescription": mainsMonitorFrequencyDescription,
       "mainsMonitorFrequencyTrapRepeatCounter": mainsMonitorFrequencyTrapRepeatCounter,
       "mainsMonitorFrequencyAlarmEnable": mainsMonitorFrequencyAlarmEnable,
       "mainsMonitorFrequencyValue": mainsMonitorFrequencyValue,
       "mainsMonitorFrequencyMajorHighLevel": mainsMonitorFrequencyMajorHighLevel,
       "mainsMonitorFrequencyMinorHighLevel": mainsMonitorFrequencyMinorHighLevel,
       "mainsMonitorFrequencyMinorLowLevel": mainsMonitorFrequencyMinorLowLevel,
       "mainsMonitorFrequencyMajorLowLevel": mainsMonitorFrequencyMajorLowLevel,
       "mainsMonitorEnergyLogAccumulatedTable": mainsMonitorEnergyLogAccumulatedTable,
       "mainsMonitorEnergyLogAccumulatedEntry": mainsMonitorEnergyLogAccumulatedEntry,
       "mainsMonitorEnergyLogAccumulated": mainsMonitorEnergyLogAccumulated,
       "mainsMonitorEnergyLogLastHoursNumberOfEntries": mainsMonitorEnergyLogLastHoursNumberOfEntries,
       "mainsMonitorEnergyLogLastHoursTable": mainsMonitorEnergyLogLastHoursTable,
       "mainsMonitorEnergyLogLastHoursEntry": mainsMonitorEnergyLogLastHoursEntry,
       "mainsMonitorEnergyLogLastHoursIndex": mainsMonitorEnergyLogLastHoursIndex,
       "mainsMonitorEnergyLogLastHoursValue": mainsMonitorEnergyLogLastHoursValue,
       "mainsMonitorEnergyLogLastDaysNumberOfEntries": mainsMonitorEnergyLogLastDaysNumberOfEntries,
       "mainsMonitorEnergyLogLastDaysTable": mainsMonitorEnergyLogLastDaysTable,
       "mainsMonitorEnergyLogLastDaysEntry": mainsMonitorEnergyLogLastDaysEntry,
       "mainsMonitorEnergyLogLastDaysIndex": mainsMonitorEnergyLogLastDaysIndex,
       "mainsMonitorEnergyLogLastDaysValue": mainsMonitorEnergyLogLastDaysValue,
       "mainsMonitorEnergyLogLastWeeksNumberOfEntries": mainsMonitorEnergyLogLastWeeksNumberOfEntries,
       "mainsMonitorEnergyLogLastWeeksTable": mainsMonitorEnergyLogLastWeeksTable,
       "mainsMonitorEnergyLogLastWeeksEntry": mainsMonitorEnergyLogLastWeeksEntry,
       "mainsMonitorEnergyLogLastWeeksIndex": mainsMonitorEnergyLogLastWeeksIndex,
       "mainsMonitorEnergyLogLastWeeksValue": mainsMonitorEnergyLogLastWeeksValue,
       "mainsOutageLog": mainsOutageLog,
       "mainsOutageTotal": mainsOutageTotal,
       "mainsOutageLogDaysNumberOfEntries": mainsOutageLogDaysNumberOfEntries,
       "mainsOutageLogDaysTable": mainsOutageLogDaysTable,
       "mainsOutageLogDaysEntry": mainsOutageLogDaysEntry,
       "mainsOutageLogDaysIndex": mainsOutageLogDaysIndex,
       "mainsOutageLogDaysValue": mainsOutageLogDaysValue,
       "mainsOutageLogWeeksNumberOfEntries": mainsOutageLogWeeksNumberOfEntries,
       "mainsOutageLogWeeksTable": mainsOutageLogWeeksTable,
       "mainsOutageLogWeeksEntry": mainsOutageLogWeeksEntry,
       "mainsOutageLogWeeksIndex": mainsOutageLogWeeksIndex,
       "mainsOutageLogWeeksValue": mainsOutageLogWeeksValue,
       "mainsOutageLogMonthsNumberOfEntries": mainsOutageLogMonthsNumberOfEntries,
       "mainsOutageLogMonthsTable": mainsOutageLogMonthsTable,
       "mainsOutageLogMonthsEntry": mainsOutageLogMonthsEntry,
       "mainsOutageLogMonthsIndex": mainsOutageLogMonthsIndex,
       "mainsOutageLogMonthsValue": mainsOutageLogMonthsValue,
       "generator": generator,
       "generatorStatus": generatorStatus,
       "generatorFailStatus": generatorFailStatus,
       "generatorActivation": generatorActivation,
       "generatorDischargeValue": generatorDischargeValue,
       "generatorMainsDelay": generatorMainsDelay,
       "generatorChargeTime": generatorChargeTime,
       "generatorCapacityControlledStartStopEnable": generatorCapacityControlledStartStopEnable,
       "generatorCapacityStartOnDischargeLimit": generatorCapacityStartOnDischargeLimit,
       "generatorCapacityStopOnChargeLimit": generatorCapacityStopOnChargeLimit,
       "generatorCurrentLimitControlledStopEnable": generatorCurrentLimitControlledStopEnable,
       "generatorCurrentLimitControlledStopValue": generatorCurrentLimitControlledStopValue,
       "generatorVoltageControlledStartEnable": generatorVoltageControlledStartEnable,
       "generatorVoltageControlStartVoltage": generatorVoltageControlStartVoltage,
       "generatorVoltageControlStopAfter": generatorVoltageControlStopAfter,
       "generatorDailyRunEnable": generatorDailyRunEnable,
       "generatorDailyRunSetupTable": generatorDailyRunSetupTable,
       "generatorDailyRunSetupEntry": generatorDailyRunSetupEntry,
       "generatorDailyRunDayIndex": generatorDailyRunDayIndex,
       "generatorDailyRunStartHour": generatorDailyRunStartHour,
       "generatorDailyRunStopHour": generatorDailyRunStopHour,
       "generatorMonthlyRunEnable": generatorMonthlyRunEnable,
       "generatorMonthlyRunStartTime": generatorMonthlyRunStartTime,
       "generatorMonthlyRunStartDayinMonth1": generatorMonthlyRunStartDayinMonth1,
       "generatorMonthlyRunStartDayinMonth2": generatorMonthlyRunStartDayinMonth2,
       "generatorTankNumberOfTanks": generatorTankNumberOfTanks,
       "generatorTankTable": generatorTankTable,
       "generatorTankEntry": generatorTankEntry,
       "generatorTankIndex": generatorTankIndex,
       "generatorTankStatus": generatorTankStatus,
       "generatorTankDescription": generatorTankDescription,
       "generatorTankTrapRepeatCounter": generatorTankTrapRepeatCounter,
       "generatorTankEnable": generatorTankEnable,
       "generatorTankValue": generatorTankValue,
       "generatorTankMajorHighLevel": generatorTankMajorHighLevel,
       "generatorTankMinorHighLevel": generatorTankMinorHighLevel,
       "generatorTankMinorLowLevel": generatorTankMinorLowLevel,
       "generatorTankMajorLowLevel": generatorTankMajorLowLevel,
       "generatorEnergyLog": generatorEnergyLog,
       "generatorEnergyLogAccumulated": generatorEnergyLogAccumulated,
       "generatorEnergyLogLastHoursNumberOfEntries": generatorEnergyLogLastHoursNumberOfEntries,
       "generatorEnergyLogLastHoursTable": generatorEnergyLogLastHoursTable,
       "generatorEnergyLogLastHoursEntry": generatorEnergyLogLastHoursEntry,
       "generatorEnergyLogLastHoursIndex": generatorEnergyLogLastHoursIndex,
       "generatorEnergyLogLastHoursValue": generatorEnergyLogLastHoursValue,
       "generatorEnergyLogLastDaysNumberOfEntries": generatorEnergyLogLastDaysNumberOfEntries,
       "generatorEnergyLogLastDaysTable": generatorEnergyLogLastDaysTable,
       "generatorEnergyLogLastDaysEntry": generatorEnergyLogLastDaysEntry,
       "generatorEnergyLogLastDaysIndex": generatorEnergyLogLastDaysIndex,
       "generatorEnergyLogLastDaysValue": generatorEnergyLogLastDaysValue,
       "generatorEnergyLogLastWeeksNumberOfEntries": generatorEnergyLogLastWeeksNumberOfEntries,
       "generatorEnergyLogLastWeeksTable": generatorEnergyLogLastWeeksTable,
       "generatorEnergyLogLastWeeksEntry": generatorEnergyLogLastWeeksEntry,
       "generatorEnergyLogLastWeeksIndex": generatorEnergyLogLastWeeksIndex,
       "generatorEnergyLogLastWeeksValue": generatorEnergyLogLastWeeksValue,
       "generatorRunHoursLog": generatorRunHoursLog,
       "generatorRunHoursTotalHours": generatorRunHoursTotalHours,
       "generatorRunHoursLogLastDaysNumberOfEntries": generatorRunHoursLogLastDaysNumberOfEntries,
       "generatorRunHoursLogLastDaysTable": generatorRunHoursLogLastDaysTable,
       "generatorRunHoursLogLastDaysEntry": generatorRunHoursLogLastDaysEntry,
       "generatorRunHoursLogLastDaysIndex": generatorRunHoursLogLastDaysIndex,
       "generatorRunHoursLogLastDaysValue": generatorRunHoursLogLastDaysValue,
       "generatorRunHoursLogLastWeeksNumberOfEntries": generatorRunHoursLogLastWeeksNumberOfEntries,
       "generatorRunHoursLogLastWeeksTable": generatorRunHoursLogLastWeeksTable,
       "generatorRunHoursLogLastWeeksEntry": generatorRunHoursLogLastWeeksEntry,
       "generatorRunHoursLogLastWeeksIndex": generatorRunHoursLogLastWeeksIndex,
       "generatorRunHoursLogLastWeeksValue": generatorRunHoursLogLastWeeksValue,
       "generatorRunHoursLogLastMonthsNumberOfEntries": generatorRunHoursLogLastMonthsNumberOfEntries,
       "generatorRunHoursLogLastMonthsTable": generatorRunHoursLogLastMonthsTable,
       "generatorRunHoursLogLastMonthsEntry": generatorRunHoursLogLastMonthsEntry,
       "generatorRunHoursLogLastMonthsIndex": generatorRunHoursLogLastMonthsIndex,
       "generatorRunHoursLogLastMonthsValue": generatorRunHoursLogLastMonthsValue,
       "generatorFuelConsumptionLog": generatorFuelConsumptionLog,
       "generatorFuelConsumptionTotalUsedTable": generatorFuelConsumptionTotalUsedTable,
       "generatorFuelConsumptionTotalUsedEntry": generatorFuelConsumptionTotalUsedEntry,
       "generatorFuelConsumptionTotalUsed": generatorFuelConsumptionTotalUsed,
       "generatorFuelConsumptionLogLastHoursNoOfEntries": generatorFuelConsumptionLogLastHoursNoOfEntries,
       "generatorFuelConsumptionLogLastHoursTable": generatorFuelConsumptionLogLastHoursTable,
       "generatorFuelConsumptionLogLastHoursEntry": generatorFuelConsumptionLogLastHoursEntry,
       "generatorFuelConsumptionLogLastHoursIndex": generatorFuelConsumptionLogLastHoursIndex,
       "generatorFuelConsumptionLogLastHoursValue": generatorFuelConsumptionLogLastHoursValue,
       "generatorFuelConsumptionLogLastDaysNoOfEntries": generatorFuelConsumptionLogLastDaysNoOfEntries,
       "generatorFuelConsumptionLogLastDaysTable": generatorFuelConsumptionLogLastDaysTable,
       "generatorFuelConsumptionLogLastDaysEntry": generatorFuelConsumptionLogLastDaysEntry,
       "generatorFuelConsumptionLogLastDaysIndex": generatorFuelConsumptionLogLastDaysIndex,
       "generatorFuelConsumptionLogLastDaysValue": generatorFuelConsumptionLogLastDaysValue,
       "generatorFuelConsumptionLogLastWeeksNoOfEntries": generatorFuelConsumptionLogLastWeeksNoOfEntries,
       "generatorFuelConsumptionLogLastWeeksTable": generatorFuelConsumptionLogLastWeeksTable,
       "generatorFuelConsumptionLogLastWeeksEntry": generatorFuelConsumptionLogLastWeeksEntry,
       "generatorFuelConsumptionLogLastWeeksIndex": generatorFuelConsumptionLogLastWeeksIndex,
       "generatorFuelConsumptionLogLastWeeksValue": generatorFuelConsumptionLogLastWeeksValue,
       "rectifiers": rectifiers,
       "rectifiersStatus": rectifiersStatus,
       "rectifiersCurrent": rectifiersCurrent,
       "rectifiersCurrentStatus": rectifiersCurrentStatus,
       "rectifiersCurrentDescription": rectifiersCurrentDescription,
       "rectifiersCurrentTrapRepeatCounter": rectifiersCurrentTrapRepeatCounter,
       "rectifiersCurrentAlarmEnable": rectifiersCurrentAlarmEnable,
       "rectifiersCurrentValue": rectifiersCurrentValue,
       "rectifiersCurrentMajorAlarmLevel": rectifiersCurrentMajorAlarmLevel,
       "rectifiersCurrentMinorAlarmLevel": rectifiersCurrentMinorAlarmLevel,
       "rectifiersCapacity": rectifiersCapacity,
       "rectifiersCapacityStatus": rectifiersCapacityStatus,
       "rectifiersCapacityDescription": rectifiersCapacityDescription,
       "rectifiersCapacityTrapRepeatCounter": rectifiersCapacityTrapRepeatCounter,
       "rectifiersCapacityAlarmEnable": rectifiersCapacityAlarmEnable,
       "rectifiersCapacityValue": rectifiersCapacityValue,
       "rectifiersCapacityMajorAlarmLevel": rectifiersCapacityMajorAlarmLevel,
       "rectifiersCapacityMinorAlarmLevel": rectifiersCapacityMinorAlarmLevel,
       "rectifiersError": rectifiersError,
       "rectifiersErrorStatus": rectifiersErrorStatus,
       "rectifiersErrorDescription": rectifiersErrorDescription,
       "rectifiersErrorTrapRepeatCounter": rectifiersErrorTrapRepeatCounter,
       "rectifiersErrorEnable": rectifiersErrorEnable,
       "rectifiersErrorValue": rectifiersErrorValue,
       "rectifiersErrorMajorAlarmLevel": rectifiersErrorMajorAlarmLevel,
       "rectifiersErrorMinorAlarmLevel": rectifiersErrorMinorAlarmLevel,
       "rectifiersNumberOfRectifiers": rectifiersNumberOfRectifiers,
       "rectifierTable": rectifierTable,
       "rectifierEntry": rectifierEntry,
       "rectifierIndex": rectifierIndex,
       "rectifierStatus": rectifierStatus,
       "rectifierOutputCurrentValue": rectifierOutputCurrentValue,
       "rectifierInputVoltageValue": rectifierInputVoltageValue,
       "rectifierType": rectifierType,
       "rectifierHwPartNumber": rectifierHwPartNumber,
       "rectifierHwVersion": rectifierHwVersion,
       "rectifierSwPartNumber": rectifierSwPartNumber,
       "rectifierSwVersion": rectifierSwVersion,
       "rectifiersEnergyLog": rectifiersEnergyLog,
       "rectifiersEnergyLogAccumulated": rectifiersEnergyLogAccumulated,
       "rectifiersEnergyLogLastHoursNumberOfEntries": rectifiersEnergyLogLastHoursNumberOfEntries,
       "rectifiersEnergyLogLastHoursTable": rectifiersEnergyLogLastHoursTable,
       "rectifiersEnergyLogLastHoursEntry": rectifiersEnergyLogLastHoursEntry,
       "rectifiersEnergyLogLastHoursIndex": rectifiersEnergyLogLastHoursIndex,
       "rectifiersEnergyLogLastHoursValue": rectifiersEnergyLogLastHoursValue,
       "rectifiersEnergyLogLastDaysNumberOfEntries": rectifiersEnergyLogLastDaysNumberOfEntries,
       "rectifiersEnergyLogLastDaysTable": rectifiersEnergyLogLastDaysTable,
       "rectifiersEnergyLogLastDaysEntry": rectifiersEnergyLogLastDaysEntry,
       "rectifiersEnergyLogLastDaysIndex": rectifiersEnergyLogLastDaysIndex,
       "rectifiersEnergyLogLastDaysValue": rectifiersEnergyLogLastDaysValue,
       "rectifiersEnergyLogLastWeeksNumberOfEntries": rectifiersEnergyLogLastWeeksNumberOfEntries,
       "rectifiersEnergyLogLastWeeksTable": rectifiersEnergyLogLastWeeksTable,
       "rectifiersEnergyLogLastWeeksEntry": rectifiersEnergyLogLastWeeksEntry,
       "rectifiersEnergyLogLastWeeksIndex": rectifiersEnergyLogLastWeeksIndex,
       "rectifiersEnergyLogLastWeeksValue": rectifiersEnergyLogLastWeeksValue,
       "dcdc": dcdc,
       "dcdcNumberOfGroups": dcdcNumberOfGroups,
       "dcdcGroupsTable": dcdcGroupsTable,
       "dcdcGroupsEntry": dcdcGroupsEntry,
       "dcdcGroupIndex": dcdcGroupIndex,
       "dcdcGroupStatus": dcdcGroupStatus,
       "dcdcGroupNumberOfDcdcConverters": dcdcGroupNumberOfDcdcConverters,
       "dcdcGroupOutputVoltage": dcdcGroupOutputVoltage,
       "dcdcNumberOfCurrents": dcdcNumberOfCurrents,
       "dcdcNumberOfCapacities": dcdcNumberOfCapacities,
       "dcdcNumberOfAlarms": dcdcNumberOfAlarms,
       "dcdcCurrentTable": dcdcCurrentTable,
       "dcdcCurrentEntry": dcdcCurrentEntry,
       "dcdcCurrentStatus": dcdcCurrentStatus,
       "dcdcCurrentDescription": dcdcCurrentDescription,
       "dcdcCurrentTrapRepeatCounter": dcdcCurrentTrapRepeatCounter,
       "dcdcCurrentAlarmEnable": dcdcCurrentAlarmEnable,
       "dcdcCurrentValue": dcdcCurrentValue,
       "dcdcCurrentMajorAlarmLevel": dcdcCurrentMajorAlarmLevel,
       "dcdcCurrentMinorAlarmLevel": dcdcCurrentMinorAlarmLevel,
       "dcdcCapacityTable": dcdcCapacityTable,
       "dcdcCapacityEntry": dcdcCapacityEntry,
       "dcdcCapacityStatus": dcdcCapacityStatus,
       "dcdcCapacityDescription": dcdcCapacityDescription,
       "dcdcCapacityTrapRepeatCounter": dcdcCapacityTrapRepeatCounter,
       "dcdcCapacityAlarmEnable": dcdcCapacityAlarmEnable,
       "dcdcCapacityValue": dcdcCapacityValue,
       "dcdcCapacityMajorAlarmLevel": dcdcCapacityMajorAlarmLevel,
       "dcdcCapacityMinorAlarmLevel": dcdcCapacityMinorAlarmLevel,
       "dcdcTable": dcdcTable,
       "dcdcEntry": dcdcEntry,
       "dcdcIndex": dcdcIndex,
       "dcdcStatus": dcdcStatus,
       "dcdcOutputCurrentValue": dcdcOutputCurrentValue,
       "dcdcInputVoltageValue": dcdcInputVoltageValue,
       "dcdcType": dcdcType,
       "dcdcHwPartNumber": dcdcHwPartNumber,
       "dcdcHwVersion": dcdcHwVersion,
       "dcdcSwPartNumber": dcdcSwPartNumber,
       "dcdcSwVersion": dcdcSwVersion,
       "dcdcErrorTable": dcdcErrorTable,
       "dcdcErrorEntry": dcdcErrorEntry,
       "dcdcErrorStatus": dcdcErrorStatus,
       "dcdcErrorDescription": dcdcErrorDescription,
       "dcdcErrorTrapRepeatCounter": dcdcErrorTrapRepeatCounter,
       "dcdcErrorEnable": dcdcErrorEnable,
       "dcdcErrorValue": dcdcErrorValue,
       "dcdcErrorMajorAlarmLevel": dcdcErrorMajorAlarmLevel,
       "dcdcErrorMinorAlarmLevel": dcdcErrorMinorAlarmLevel,
       "dcdcEnergyLog": dcdcEnergyLog,
       "dcdcEnergyLogAccumulatedTable": dcdcEnergyLogAccumulatedTable,
       "dcdcEnergyLogAccumulatedEntry": dcdcEnergyLogAccumulatedEntry,
       "dcdcEnergyLogAccumulated": dcdcEnergyLogAccumulated,
       "dcdcEnergyLogLastHoursNumberOfEntries": dcdcEnergyLogLastHoursNumberOfEntries,
       "dcdcEnergyLogLastHoursTable": dcdcEnergyLogLastHoursTable,
       "dcdcEnergyLogLastHoursEntry": dcdcEnergyLogLastHoursEntry,
       "dcdcEnergyLogLastHoursIndex": dcdcEnergyLogLastHoursIndex,
       "dcdcEnergyLogLastHoursValue": dcdcEnergyLogLastHoursValue,
       "dcdcEnergyLogLastDaysNumberOfEntries": dcdcEnergyLogLastDaysNumberOfEntries,
       "dcdcEnergyLogLastDaysTable": dcdcEnergyLogLastDaysTable,
       "dcdcEnergyLogLastDaysEntry": dcdcEnergyLogLastDaysEntry,
       "dcdcEnergyLogLastDaysIndex": dcdcEnergyLogLastDaysIndex,
       "dcdcEnergyLogLastDaysValue": dcdcEnergyLogLastDaysValue,
       "dcdcEnergyLogLastWeeksNumberOfEntries": dcdcEnergyLogLastWeeksNumberOfEntries,
       "dcdcEnergyLogLastWeeksTable": dcdcEnergyLogLastWeeksTable,
       "dcdcEnergyLogLastWeeksEntry": dcdcEnergyLogLastWeeksEntry,
       "dcdcEnergyLogLastWeeksIndex": dcdcEnergyLogLastWeeksIndex,
       "dcdcEnergyLogLastWeeksValue": dcdcEnergyLogLastWeeksValue,
       "solarChargers": solarChargers,
       "solarChargersStatus": solarChargersStatus,
       "solarChargersCurrent": solarChargersCurrent,
       "solarChargersCurrentStatus": solarChargersCurrentStatus,
       "solarChargersCurrentDescription": solarChargersCurrentDescription,
       "solarChargersCurrentTrapRepeatCounter": solarChargersCurrentTrapRepeatCounter,
       "solarChargersCurrentAlarmEnable": solarChargersCurrentAlarmEnable,
       "solarChargersCurrentValue": solarChargersCurrentValue,
       "solarChargersCurrentMajorAlarmLevel": solarChargersCurrentMajorAlarmLevel,
       "solarChargersCurrentMinorAlarmLevel": solarChargersCurrentMinorAlarmLevel,
       "solarChargersCapacity": solarChargersCapacity,
       "solarChargersCapacityStatus": solarChargersCapacityStatus,
       "solarChargersCapacityDescription": solarChargersCapacityDescription,
       "solarChargersCapacityTrapRepeatCounter": solarChargersCapacityTrapRepeatCounter,
       "solarChargersCapacityAlarmEnable": solarChargersCapacityAlarmEnable,
       "solarChargersCapacityValue": solarChargersCapacityValue,
       "solarChargersCapacityMajorAlarmLevel": solarChargersCapacityMajorAlarmLevel,
       "solarChargersCapacityMinorAlarmLevel": solarChargersCapacityMinorAlarmLevel,
       "solarChargersError": solarChargersError,
       "solarChargersErrorStatus": solarChargersErrorStatus,
       "solarChargersErrorDescription": solarChargersErrorDescription,
       "solarChargersErrorTrapRepeatCounter": solarChargersErrorTrapRepeatCounter,
       "solarChargersErrorEnable": solarChargersErrorEnable,
       "solarChargersErrorValue": solarChargersErrorValue,
       "solarChargersErrorMajorAlarmLevel": solarChargersErrorMajorAlarmLevel,
       "solarChargersErrorMinorAlarmLevel": solarChargersErrorMinorAlarmLevel,
       "solarChargersNumberOfSolarChargers": solarChargersNumberOfSolarChargers,
       "solarChargerTable": solarChargerTable,
       "solarChargerEntry": solarChargerEntry,
       "solarChargerIndex": solarChargerIndex,
       "solarChargerStatus": solarChargerStatus,
       "solarChargerOutputCurrentValue": solarChargerOutputCurrentValue,
       "solarChargerInputVoltageValue": solarChargerInputVoltageValue,
       "solarChargerType": solarChargerType,
       "solarChargerHwPartNumber": solarChargerHwPartNumber,
       "solarChargerHwVersion": solarChargerHwVersion,
       "solarChargerSwPartNumber": solarChargerSwPartNumber,
       "solarChargerSwVersion": solarChargerSwVersion,
       "solarChargersEnergyLog": solarChargersEnergyLog,
       "solarChargersEnergyLogAccumulated": solarChargersEnergyLogAccumulated,
       "solarChargersEnergyLogLastHoursNumberOfEntries": solarChargersEnergyLogLastHoursNumberOfEntries,
       "solarChargersEnergyLogLastHoursTable": solarChargersEnergyLogLastHoursTable,
       "solarChargersEnergyLogLastHoursEntry": solarChargersEnergyLogLastHoursEntry,
       "solarChargersEnergyLogLastHoursIndex": solarChargersEnergyLogLastHoursIndex,
       "solarChargersEnergyLogLastHoursValue": solarChargersEnergyLogLastHoursValue,
       "solarChargersEnergyLogLastDaysNumberOfEntries": solarChargersEnergyLogLastDaysNumberOfEntries,
       "solarChargersEnergyLogLastDaysTable": solarChargersEnergyLogLastDaysTable,
       "solarChargersEnergyLogLastDaysEntry": solarChargersEnergyLogLastDaysEntry,
       "solarChargersEnergyLogLastDaysIndex": solarChargersEnergyLogLastDaysIndex,
       "solarChargersEnergyLogLastDaysValue": solarChargersEnergyLogLastDaysValue,
       "solarChargersEnergyLogLastWeeksNumberOfEntries": solarChargersEnergyLogLastWeeksNumberOfEntries,
       "solarChargersEnergyLogLastWeeksTable": solarChargersEnergyLogLastWeeksTable,
       "solarChargersEnergyLogLastWeeksEntry": solarChargersEnergyLogLastWeeksEntry,
       "solarChargersEnergyLogLastWeeksIndex": solarChargersEnergyLogLastWeeksIndex,
       "solarChargersEnergyLogLastWeeksValue": solarChargersEnergyLogLastWeeksValue,
       "windChargers": windChargers,
       "windChargersStatus": windChargersStatus,
       "windChargersCurrent": windChargersCurrent,
       "windChargersCurrentStatus": windChargersCurrentStatus,
       "windChargersCurrentDescription": windChargersCurrentDescription,
       "windChargersCurrentTrapRepeatCounter": windChargersCurrentTrapRepeatCounter,
       "windChargersCurrentAlarmEnable": windChargersCurrentAlarmEnable,
       "windChargersCurrentValue": windChargersCurrentValue,
       "windChargersCurrentMajorAlarmLevel": windChargersCurrentMajorAlarmLevel,
       "windChargersCurrentMinorAlarmLevel": windChargersCurrentMinorAlarmLevel,
       "windChargersCapacity": windChargersCapacity,
       "windChargersCapacityStatus": windChargersCapacityStatus,
       "windChargersCapacityDescription": windChargersCapacityDescription,
       "windChargersCapacityTrapRepeatCounter": windChargersCapacityTrapRepeatCounter,
       "windChargersCapacityAlarmEnable": windChargersCapacityAlarmEnable,
       "windChargersCapacityValue": windChargersCapacityValue,
       "windChargersCapacityMajorAlarmLevel": windChargersCapacityMajorAlarmLevel,
       "windChargersCapacityMinorAlarmLevel": windChargersCapacityMinorAlarmLevel,
       "windChargersError": windChargersError,
       "windChargersErrorStatus": windChargersErrorStatus,
       "windChargersErrorDescription": windChargersErrorDescription,
       "windChargersErrorTrapRepeatCounter": windChargersErrorTrapRepeatCounter,
       "windChargersErrorEnable": windChargersErrorEnable,
       "windChargersErrorValue": windChargersErrorValue,
       "windChargersErrorMajorAlarmLevel": windChargersErrorMajorAlarmLevel,
       "windChargersErrorMinorAlarmLevel": windChargersErrorMinorAlarmLevel,
       "windChargersNumberOfWindChargers": windChargersNumberOfWindChargers,
       "windChargerTable": windChargerTable,
       "windChargerEntry": windChargerEntry,
       "windChargerIndex": windChargerIndex,
       "windChargerStatus": windChargerStatus,
       "windChargerOutputCurrentValue": windChargerOutputCurrentValue,
       "windChargerInputVoltageValue": windChargerInputVoltageValue,
       "windChargerType": windChargerType,
       "windChargerHwPartNumber": windChargerHwPartNumber,
       "windChargerHwVersion": windChargerHwVersion,
       "windChargerSwPartNumber": windChargerSwPartNumber,
       "windChargerSwVersion": windChargerSwVersion,
       "windChargersEnergyLog": windChargersEnergyLog,
       "windChargersEnergyLogAccumulated": windChargersEnergyLogAccumulated,
       "windChargersEnergyLogLastHoursNumberOfEntries": windChargersEnergyLogLastHoursNumberOfEntries,
       "windChargersEnergyLogLastHoursTable": windChargersEnergyLogLastHoursTable,
       "windChargersEnergyLogLastHoursEntry": windChargersEnergyLogLastHoursEntry,
       "windChargersEnergyLogLastHoursIndex": windChargersEnergyLogLastHoursIndex,
       "windChargersEnergyLogLastHoursValue": windChargersEnergyLogLastHoursValue,
       "windChargersEnergyLogLastDaysNumberOfEntries": windChargersEnergyLogLastDaysNumberOfEntries,
       "windChargersEnergyLogLastDaysTable": windChargersEnergyLogLastDaysTable,
       "windChargersEnergyLogLastDaysEntry": windChargersEnergyLogLastDaysEntry,
       "windChargersEnergyLogLastDaysIndex": windChargersEnergyLogLastDaysIndex,
       "windChargersEnergyLogLastDaysValue": windChargersEnergyLogLastDaysValue,
       "windChargersEnergyLogLastWeeksNumberOfEntries": windChargersEnergyLogLastWeeksNumberOfEntries,
       "windChargersEnergyLogLastWeeksTable": windChargersEnergyLogLastWeeksTable,
       "windChargersEnergyLogLastWeeksEntry": windChargersEnergyLogLastWeeksEntry,
       "windChargersEnergyLogLastWeeksIndex": windChargersEnergyLogLastWeeksIndex,
       "windChargersEnergyLogLastWeeksValue": windChargersEnergyLogLastWeeksValue,
       "load": load,
       "loadStatus": loadStatus,
       "loadCurrent": loadCurrent,
       "loadCurrentStatus": loadCurrentStatus,
       "loadCurrentDescription": loadCurrentDescription,
       "loadCurrentTrapRepeatCounter": loadCurrentTrapRepeatCounter,
       "loadCurrentAlarmEnable": loadCurrentAlarmEnable,
       "loadCurrentValue": loadCurrentValue,
       "loadCurrentMajorHighLevel": loadCurrentMajorHighLevel,
       "loadCurrentMinorHighLevel": loadCurrentMinorHighLevel,
       "loadFusesStatus": loadFusesStatus,
       "loadNumberOfGroups": loadNumberOfGroups,
       "loadGroupTable": loadGroupTable,
       "loadGroupEntry": loadGroupEntry,
       "loadGroupIndex": loadGroupIndex,
       "loadGroupStatus": loadGroupStatus,
       "loadNumberOfLVLDs": loadNumberOfLVLDs,
       "loadLVLDTable": loadLVLDTable,
       "loadLVLDEntry": loadLVLDEntry,
       "loadLVLDIndex": loadLVLDIndex,
       "loadLVLDStatus": loadLVLDStatus,
       "loadLVLDDescription": loadLVLDDescription,
       "loadLVLDTrapRepeatCounter": loadLVLDTrapRepeatCounter,
       "loadLVLDEnable": loadLVLDEnable,
       "loadLVLDValue": loadLVLDValue,
       "loadLVLDConnectVoltage": loadLVLDConnectVoltage,
       "loadLVLDDisconnectVoltage": loadLVLDDisconnectVoltage,
       "loadFuseTable": loadFuseTable,
       "loadFuseEntry": loadFuseEntry,
       "loadFuseStatus": loadFuseStatus,
       "loadFuseDescription": loadFuseDescription,
       "loadFuseTrapRepeatCounter": loadFuseTrapRepeatCounter,
       "loadFuseAlarmEnable": loadFuseAlarmEnable,
       "loadFuseValue": loadFuseValue,
       "loadEnergyLog": loadEnergyLog,
       "loadEnergyLogAccumulated": loadEnergyLogAccumulated,
       "loadEnergyLogLastHoursNumberOfEntries": loadEnergyLogLastHoursNumberOfEntries,
       "loadEnergyLogLastHoursTable": loadEnergyLogLastHoursTable,
       "loadEnergyLogLastHoursEntry": loadEnergyLogLastHoursEntry,
       "loadEnergyLogLastHoursIndex": loadEnergyLogLastHoursIndex,
       "loadEnergyLogLastHoursValue": loadEnergyLogLastHoursValue,
       "loadEnergyLogLastDaysNumberOfEntries": loadEnergyLogLastDaysNumberOfEntries,
       "loadEnergyLogLastDaysTable": loadEnergyLogLastDaysTable,
       "loadEnergyLogLastDaysEntry": loadEnergyLogLastDaysEntry,
       "loadEnergyLogLastDaysIndex": loadEnergyLogLastDaysIndex,
       "loadEnergyLogLastDaysValue": loadEnergyLogLastDaysValue,
       "loadEnergyLogLastWeeksNumberOfEntries": loadEnergyLogLastWeeksNumberOfEntries,
       "loadEnergyLogLastWeeksTable": loadEnergyLogLastWeeksTable,
       "loadEnergyLogLastWeeksEntry": loadEnergyLogLastWeeksEntry,
       "loadEnergyLogLastWeeksIndex": loadEnergyLogLastWeeksIndex,
       "loadEnergyLogLastWeeksValue": loadEnergyLogLastWeeksValue,
       "battery": battery,
       "batteryStatus": batteryStatus,
       "batteryDescription": batteryDescription,
       "batteryReferenceVoltage": batteryReferenceVoltage,
       "batteryFusesStatus": batteryFusesStatus,
       "batteryVoltage": batteryVoltage,
       "batteryVoltageStatus": batteryVoltageStatus,
       "batteryVoltageDescription": batteryVoltageDescription,
       "batteryVoltageTrapRepeatCounter": batteryVoltageTrapRepeatCounter,
       "batteryVoltageAlarmEnable": batteryVoltageAlarmEnable,
       "batteryVoltageValue": batteryVoltageValue,
       "batteryVoltageMajorHighLevel": batteryVoltageMajorHighLevel,
       "batteryVoltageMinorHighLevel": batteryVoltageMinorHighLevel,
       "batteryVoltageMinorLowLevel": batteryVoltageMinorLowLevel,
       "batteryVoltageMajorLowLevel": batteryVoltageMajorLowLevel,
       "batteryCurrents": batteryCurrents,
       "batteryCurrentsStatus": batteryCurrentsStatus,
       "batteryCurrentsDescription": batteryCurrentsDescription,
       "batteryCurrentsTrapRepeatCounter": batteryCurrentsTrapRepeatCounter,
       "batteryCurrentsAlarmEnable": batteryCurrentsAlarmEnable,
       "batteryCurrentsValue": batteryCurrentsValue,
       "batteryCurrentsMajorHighLevel": batteryCurrentsMajorHighLevel,
       "batteryCurrentsMinorHighLevel": batteryCurrentsMinorHighLevel,
       "batteryCurrentsMinorLowLevel": batteryCurrentsMinorLowLevel,
       "batteryCurrentsMajorLowLevel": batteryCurrentsMajorLowLevel,
       "batteryTemperatures": batteryTemperatures,
       "batteryTemperaturesStatus": batteryTemperaturesStatus,
       "batteryTemperaturesDescription": batteryTemperaturesDescription,
       "batteryTemperaturesTrapRepeatCounter": batteryTemperaturesTrapRepeatCounter,
       "batteryTemperaturesAlarmEnable": batteryTemperaturesAlarmEnable,
       "batteryTemperaturesValue": batteryTemperaturesValue,
       "batteryTemperaturesMajorHighLevel": batteryTemperaturesMajorHighLevel,
       "batteryTemperaturesMinorHighLevel": batteryTemperaturesMinorHighLevel,
       "batteryTemperaturesMinorLowLevel": batteryTemperaturesMinorLowLevel,
       "batteryTemperaturesMajorLowLevel": batteryTemperaturesMajorLowLevel,
       "batteryTimeLeft": batteryTimeLeft,
       "batteryTimeLeftStatus": batteryTimeLeftStatus,
       "batteryTimeLeftDescription": batteryTimeLeftDescription,
       "batteryTimeLeftTrapRepeatCounter": batteryTimeLeftTrapRepeatCounter,
       "batteryTimeLeftAlarmEnable": batteryTimeLeftAlarmEnable,
       "batteryTimeLeftValue": batteryTimeLeftValue,
       "batteryTimeLeftMinorAlarmLevel": batteryTimeLeftMinorAlarmLevel,
       "batteryTimeLeftMajorAlarmLevel": batteryTimeLeftMajorAlarmLevel,
       "batteryRemainingCapacity": batteryRemainingCapacity,
       "batteryRemainingCapacityStatus": batteryRemainingCapacityStatus,
       "batteryRemainingCapacityDescription": batteryRemainingCapacityDescription,
       "batteryRemainingCapacityTrapRepeatCounter": batteryRemainingCapacityTrapRepeatCounter,
       "batteryRemainingCapacityAlarmEnable": batteryRemainingCapacityAlarmEnable,
       "batteryRemainingCapacityValue": batteryRemainingCapacityValue,
       "batteryRemainingCapacityMinorLowLevel": batteryRemainingCapacityMinorLowLevel,
       "batteryRemainingCapacityMajorLowLevel": batteryRemainingCapacityMajorLowLevel,
       "batteryUsedCapacity": batteryUsedCapacity,
       "batteryUsedCapacityStatus": batteryUsedCapacityStatus,
       "batteryUsedCapacityDescription": batteryUsedCapacityDescription,
       "batteryUsedCapacityTrapRepeatCounter": batteryUsedCapacityTrapRepeatCounter,
       "batteryUsedCapacityAlarmEnable": batteryUsedCapacityAlarmEnable,
       "batteryUsedCapacityValue": batteryUsedCapacityValue,
       "batteryUsedCapacityMajorAlarmLevel": batteryUsedCapacityMajorAlarmLevel,
       "batteryUsedCapacityMinorAlarmLevel": batteryUsedCapacityMinorAlarmLevel,
       "batteryTotalCapacity": batteryTotalCapacity,
       "batteryTotalCapacityStatus": batteryTotalCapacityStatus,
       "batteryTotalCapacityDescription": batteryTotalCapacityDescription,
       "batteryTotalCapacityTrapRepeatCounter": batteryTotalCapacityTrapRepeatCounter,
       "batteryTotalCapacityAlarmEnable": batteryTotalCapacityAlarmEnable,
       "batteryTotalCapacityValue": batteryTotalCapacityValue,
       "batteryTotalCapacityMinorLowLevel": batteryTotalCapacityMinorLowLevel,
       "batteryTotalCapacityMajorLowLevel": batteryTotalCapacityMajorLowLevel,
       "batteryQuality": batteryQuality,
       "batteryQualityStatus": batteryQualityStatus,
       "batteryQualityDescription": batteryQualityDescription,
       "batteryQualityTrapRepeatCounter": batteryQualityTrapRepeatCounter,
       "batteryQualityAlarmEnable": batteryQualityAlarmEnable,
       "batteryQualityValue": batteryQualityValue,
       "batteryQualityMinorAlarmLevel": batteryQualityMinorAlarmLevel,
       "batteryQualityMajorAlarmLevel": batteryQualityMajorAlarmLevel,
       "batteryLVBD": batteryLVBD,
       "batteryLVBDStatus": batteryLVBDStatus,
       "batteryLVBDDescription": batteryLVBDDescription,
       "batteryLVBDTrapRepeatCounter": batteryLVBDTrapRepeatCounter,
       "batteryLVBDEnable": batteryLVBDEnable,
       "batteryLVBDValue": batteryLVBDValue,
       "batteryLVBDConnectVoltage": batteryLVBDConnectVoltage,
       "batteryLVBDDisconnectVoltage": batteryLVBDDisconnectVoltage,
       "batteryChargeCurrentLimit": batteryChargeCurrentLimit,
       "batteryChargeCurrentLimitEnable": batteryChargeCurrentLimitEnable,
       "batteryChargeCurrentLimitValue": batteryChargeCurrentLimitValue,
       "batteryBoost": batteryBoost,
       "batteryBoostVoltage": batteryBoostVoltage,
       "batteryBoostCommand": batteryBoostCommand,
       "batteryBoostCurrentThreshold": batteryBoostCurrentThreshold,
       "batteryBoostManualMaxDuration": batteryBoostManualMaxDuration,
       "batteryTest": batteryTest,
       "batteryTestVoltage": batteryTestVoltage,
       "batteryTestCommand": batteryTestCommand,
       "batteryTestNumberOfResults": batteryTestNumberOfResults,
       "batteryTestResultTable": batteryTestResultTable,
       "batteryTestResultEntry": batteryTestResultEntry,
       "batteryTestResultIndex": batteryTestResultIndex,
       "batteryTestResultStartDateTime": batteryTestResultStartDateTime,
       "batteryTestResultDuration": batteryTestResultDuration,
       "batteryTestResultDischarged": batteryTestResultDischarged,
       "batteryTestResultQuality": batteryTestResultQuality,
       "batteryTempComp": batteryTempComp,
       "batteryTempCompEnable": batteryTempCompEnable,
       "batteryBank": batteryBank,
       "batteryBankNumberOfBanks": batteryBankNumberOfBanks,
       "batteryBankTable": batteryBankTable,
       "batteryBankEntry": batteryBankEntry,
       "batteryBankIndex": batteryBankIndex,
       "batteryBankStatus": batteryBankStatus,
       "batteryBankNumberOfTemperatures": batteryBankNumberOfTemperatures,
       "batteryBankNumberOfCurrents": batteryBankNumberOfCurrents,
       "batteryBankNumberOfFuses": batteryBankNumberOfFuses,
       "batteryBankTemperatureTable": batteryBankTemperatureTable,
       "batteryBankTemperatureEntry": batteryBankTemperatureEntry,
       "batteryTemperatureIndex": batteryTemperatureIndex,
       "batteryTemperatureStatus": batteryTemperatureStatus,
       "batteryTemperatureDescription": batteryTemperatureDescription,
       "batteryTemperatureTrapRepeatCounter": batteryTemperatureTrapRepeatCounter,
       "batteryTemperatureAlarmEnable": batteryTemperatureAlarmEnable,
       "batteryTemperatureValue": batteryTemperatureValue,
       "batteryTemperatureMajorHighLevel": batteryTemperatureMajorHighLevel,
       "batteryTemperatureMinorHighLevel": batteryTemperatureMinorHighLevel,
       "batteryTemperatureMinorLowLevel": batteryTemperatureMinorLowLevel,
       "batteryTemperatureMajorLowLevel": batteryTemperatureMajorLowLevel,
       "batteryBankCurrentTable": batteryBankCurrentTable,
       "batteryBankCurrentEntry": batteryBankCurrentEntry,
       "batteryCurrentIndex": batteryCurrentIndex,
       "batteryCurrentStatus": batteryCurrentStatus,
       "batteryCurrentDescription": batteryCurrentDescription,
       "batteryCurrentTrapRepeatCounter": batteryCurrentTrapRepeatCounter,
       "batteryCurrentAlarmEnable": batteryCurrentAlarmEnable,
       "batteryCurrentValue": batteryCurrentValue,
       "batteryCurrentMajorHighLevel": batteryCurrentMajorHighLevel,
       "batteryCurrentMinorHighLevel": batteryCurrentMinorHighLevel,
       "batteryCurrentMinorLowLevel": batteryCurrentMinorLowLevel,
       "batteryCurrentMajorLowLevel": batteryCurrentMajorLowLevel,
       "batteryBankFuseTable": batteryBankFuseTable,
       "batteryBankFuseEntry": batteryBankFuseEntry,
       "batteryFuseIndex": batteryFuseIndex,
       "batteryFuseStatus": batteryFuseStatus,
       "batteryFuseDescription": batteryFuseDescription,
       "batteryFuseTrapRepeatCounter": batteryFuseTrapRepeatCounter,
       "batteryFuseAlarmEnable": batteryFuseAlarmEnable,
       "batteryFuseValue": batteryFuseValue,
       "batteryMonitors": batteryMonitors,
       "batteryMonitorsNumberOfUnits": batteryMonitorsNumberOfUnits,
       "batteryMonitorsTable": batteryMonitorsTable,
       "batteryMonitorsEntry": batteryMonitorsEntry,
       "batteryMonitorIndex": batteryMonitorIndex,
       "batteryMonitorNumberOfTemperatures": batteryMonitorNumberOfTemperatures,
       "batteryMonitorNumberOfCurrents": batteryMonitorNumberOfCurrents,
       "batteryMonitorNumberOfFuses": batteryMonitorNumberOfFuses,
       "batteryMonitorNumberOfSymmetries": batteryMonitorNumberOfSymmetries,
       "batteryMonitorTemperatureTable": batteryMonitorTemperatureTable,
       "batteryMonitorTemperatureEntry": batteryMonitorTemperatureEntry,
       "batteryMonitorTemperatureIndex": batteryMonitorTemperatureIndex,
       "batteryMonitorTemperatureStatus": batteryMonitorTemperatureStatus,
       "batteryMonitorTemperatureDescription": batteryMonitorTemperatureDescription,
       "batteryMonitorTemperatureTrapRepeatCounter": batteryMonitorTemperatureTrapRepeatCounter,
       "batteryMonitorTemperatureAlarmEnable": batteryMonitorTemperatureAlarmEnable,
       "batteryMonitorTemperatureValue": batteryMonitorTemperatureValue,
       "batteryMonitorTemperatureMajorHighLevel": batteryMonitorTemperatureMajorHighLevel,
       "batteryMonitorTemperatureMinorHighLevel": batteryMonitorTemperatureMinorHighLevel,
       "batteryMonitorTemperatureMinorLowLevel": batteryMonitorTemperatureMinorLowLevel,
       "batteryMonitorTemperatureMajorLowLevel": batteryMonitorTemperatureMajorLowLevel,
       "batteryMonitorCurrentTable": batteryMonitorCurrentTable,
       "batteryMonitorCurrentEntry": batteryMonitorCurrentEntry,
       "batteryMonitorCurrentIndex": batteryMonitorCurrentIndex,
       "batteryMonitorCurrentStatus": batteryMonitorCurrentStatus,
       "batteryMonitorCurrentDescription": batteryMonitorCurrentDescription,
       "batteryMonitorCurrentTrapRepeatCounter": batteryMonitorCurrentTrapRepeatCounter,
       "batteryMonitorCurrentAlarmEnable": batteryMonitorCurrentAlarmEnable,
       "batteryMonitorCurrentValue": batteryMonitorCurrentValue,
       "batteryMonitorCurrentMajorHighLevel": batteryMonitorCurrentMajorHighLevel,
       "batteryMonitorCurrentMinorHighLevel": batteryMonitorCurrentMinorHighLevel,
       "batteryMonitorCurrentMinorLowLevel": batteryMonitorCurrentMinorLowLevel,
       "batteryMonitorCurrentMajorLowLevel": batteryMonitorCurrentMajorLowLevel,
       "batteryMonitorFuseTable": batteryMonitorFuseTable,
       "batteryMonitorFuseEntry": batteryMonitorFuseEntry,
       "batteryMonitorFuseIndex": batteryMonitorFuseIndex,
       "batteryMonitorFuseStatus": batteryMonitorFuseStatus,
       "batteryMonitorFuseDescription": batteryMonitorFuseDescription,
       "batteryMonitorFuseTrapRepeatCounter": batteryMonitorFuseTrapRepeatCounter,
       "batteryMonitorFuseAlarmEnable": batteryMonitorFuseAlarmEnable,
       "batteryMonitorFuseValue": batteryMonitorFuseValue,
       "batteryMonitorSymmetryTable": batteryMonitorSymmetryTable,
       "batteryMonitorSymmetryEntry": batteryMonitorSymmetryEntry,
       "batteryMonitorSymmetryIndex": batteryMonitorSymmetryIndex,
       "batteryMonitorSymmetryStatus": batteryMonitorSymmetryStatus,
       "batteryMonitorSymmetryDescription": batteryMonitorSymmetryDescription,
       "batteryMonitorSymmetryTrapRepeatCounter": batteryMonitorSymmetryTrapRepeatCounter,
       "batteryMonitorSymmetryAlarmEnable": batteryMonitorSymmetryAlarmEnable,
       "batteryMonitorSymmetryMeasureValue": batteryMonitorSymmetryMeasureValue,
       "batteryMonitorSymmetryDeltaValue": batteryMonitorSymmetryDeltaValue,
       "batteryMonitorSymmetryMajorAlarmLevel": batteryMonitorSymmetryMajorAlarmLevel,
       "batteryMonitorSymmetryMinorAlarmLevel": batteryMonitorSymmetryMinorAlarmLevel,
       "batteryEnergyLog": batteryEnergyLog,
       "batteryEnergyLogAccumulated": batteryEnergyLogAccumulated,
       "batteryEnergyLogLastHoursNumberOfEntries": batteryEnergyLogLastHoursNumberOfEntries,
       "batteryEnergyLogLastHoursTable": batteryEnergyLogLastHoursTable,
       "batteryEnergyLogLastHoursEntry": batteryEnergyLogLastHoursEntry,
       "batteryEnergyLogLastHoursIndex": batteryEnergyLogLastHoursIndex,
       "batteryEnergyLogLastHoursValue": batteryEnergyLogLastHoursValue,
       "batteryEnergyLogLastDaysNumberOfEntries": batteryEnergyLogLastDaysNumberOfEntries,
       "batteryEnergyLogLastDaysTable": batteryEnergyLogLastDaysTable,
       "batteryEnergyLogLastDaysEntry": batteryEnergyLogLastDaysEntry,
       "batteryEnergyLogLastDaysIndex": batteryEnergyLogLastDaysIndex,
       "batteryEnergyLogLastDaysValue": batteryEnergyLogLastDaysValue,
       "batteryEnergyLogLastWeeksNumberOfEntries": batteryEnergyLogLastWeeksNumberOfEntries,
       "batteryEnergyLogLastWeeksTable": batteryEnergyLogLastWeeksTable,
       "batteryEnergyLogLastWeeksEntry": batteryEnergyLogLastWeeksEntry,
       "batteryEnergyLogLastWeeksIndex": batteryEnergyLogLastWeeksIndex,
       "batteryEnergyLogLastWeeksValue": batteryEnergyLogLastWeeksValue,
       "batteryCycleLog": batteryCycleLog,
       "batteryCycleLogTotalCycles": batteryCycleLogTotalCycles,
       "batteryCycleLogDaysNumberOfEntries": batteryCycleLogDaysNumberOfEntries,
       "batteryCycleLogDaysTable": batteryCycleLogDaysTable,
       "batteryCycleLogDaysEntry": batteryCycleLogDaysEntry,
       "batteryCycleLogDaysIndex": batteryCycleLogDaysIndex,
       "batteryCycleLogDaysValue": batteryCycleLogDaysValue,
       "batteryCycleLogWeeksNumberOfEntries": batteryCycleLogWeeksNumberOfEntries,
       "batteryCycleLogWeeksTable": batteryCycleLogWeeksTable,
       "batteryCycleLogWeeksEntry": batteryCycleLogWeeksEntry,
       "batteryCycleLogWeeksIndex": batteryCycleLogWeeksIndex,
       "batteryCycleLogWeeksValue": batteryCycleLogWeeksValue,
       "batteryCycleLogMonthsNumberOfEntries": batteryCycleLogMonthsNumberOfEntries,
       "batteryCycleLogMonthsTable": batteryCycleLogMonthsTable,
       "batteryCycleLogMonthsEntry": batteryCycleLogMonthsEntry,
       "batteryCycleLogMonthsIndex": batteryCycleLogMonthsIndex,
       "batteryCycleLogMonthsValue": batteryCycleLogMonthsValue,
       "inputs": inputs,
       "inputControlUnitsTable": inputControlUnitsTable,
       "inputControlUnitsEntry": inputControlUnitsEntry,
       "inputControlUnitIndex": inputControlUnitIndex,
       "inputControlUnitNumberOfInputs": inputControlUnitNumberOfInputs,
       "inputControlUnitInputTable": inputControlUnitInputTable,
       "inputControlUnitInputEntry": inputControlUnitInputEntry,
       "inputControlUnitInputIndex": inputControlUnitInputIndex,
       "inputControlUnitInputStatus": inputControlUnitInputStatus,
       "inputControlUnitInputDescription": inputControlUnitInputDescription,
       "inputControlUnitInputTrapRepeatCounter": inputControlUnitInputTrapRepeatCounter,
       "inputControlUnitInputAlarmEnable": inputControlUnitInputAlarmEnable,
       "inputControlUnitInputValue": inputControlUnitInputValue,
       "inputControlUnitInputConfiguration": inputControlUnitInputConfiguration,
       "inputIoUnitsTable": inputIoUnitsTable,
       "inputIoUnitsEntry": inputIoUnitsEntry,
       "inputIoUnitIndex": inputIoUnitIndex,
       "inputIoUnitNumberOfInputs": inputIoUnitNumberOfInputs,
       "inputIoUnitProgInputTable": inputIoUnitProgInputTable,
       "inputIoUnitProgInputEntry": inputIoUnitProgInputEntry,
       "inputIoUnitProgInputIndex": inputIoUnitProgInputIndex,
       "inputIoUnitProgInputStatus": inputIoUnitProgInputStatus,
       "inputIoUnitProgInputDescription": inputIoUnitProgInputDescription,
       "inputIoUnitProgInputTrapRepeatCounter": inputIoUnitProgInputTrapRepeatCounter,
       "inputIoUnitProgInputAlarmEnable": inputIoUnitProgInputAlarmEnable,
       "inputIoUnitProgInputValue": inputIoUnitProgInputValue,
       "inputIoUnitProgInputConfiguration": inputIoUnitProgInputConfiguration,
       "outputs": outputs,
       "outputControlUnitTable": outputControlUnitTable,
       "outputControlUnitEntry": outputControlUnitEntry,
       "outputControlUnitIndex": outputControlUnitIndex,
       "outputControlUnitNumberOfOutputs": outputControlUnitNumberOfOutputs,
       "outputControlUnitOutputTable": outputControlUnitOutputTable,
       "outputControlUnitOutputEntry": outputControlUnitOutputEntry,
       "outputControlUnitOutputIndex": outputControlUnitOutputIndex,
       "outputControlUnitOutputStatus": outputControlUnitOutputStatus,
       "outputControlUnitOutputDescription": outputControlUnitOutputDescription,
       "outputIoUnitTable": outputIoUnitTable,
       "outputIoUnitEntry": outputIoUnitEntry,
       "outputIoUnitIndex": outputIoUnitIndex,
       "outputIoUnitNumberOfOutputs": outputIoUnitNumberOfOutputs,
       "outputIoUnitOutputTable": outputIoUnitOutputTable,
       "outputIoUnitOutputEntry": outputIoUnitOutputEntry,
       "outputIoUnitOutputIndex": outputIoUnitOutputIndex,
       "outputIoUnitOutputStatus": outputIoUnitOutputStatus,
       "outputIoUnitOutputDescription": outputIoUnitOutputDescription,
       "controlSystem": controlSystem,
       "controlSystemStatus": controlSystemStatus,
       "controlSystemClock": controlSystemClock,
       "controlSystemNumberOfControlUnits": controlSystemNumberOfControlUnits,
       "snmp": snmp,
       "snmpSendOffTraps": snmpSendOffTraps,
       "snmpTrapRepeatRate": snmpTrapRepeatRate,
       "snmpHeartBeatTrapRepeatRate": snmpHeartBeatTrapRepeatRate,
       "snmpInhibitTraps": snmpInhibitTraps,
       "controlSystemResetManualAlarms": controlSystemResetManualAlarms,
       "controlSystemResetNumberOfModules": controlSystemResetNumberOfModules,
       "controlSystemIoUnits": controlSystemIoUnits,
       "controlSystemIoUnitsNumberOfUnits": controlSystemIoUnitsNumberOfUnits,
       "controlSystemIoUnitsTable": controlSystemIoUnitsTable,
       "controlSystemIoUnitsEntry": controlSystemIoUnitsEntry,
       "controlSystemIoUnitIndex": controlSystemIoUnitIndex,
       "controlSystemIoUnitNumberOfTemperatures": controlSystemIoUnitNumberOfTemperatures,
       "controlSystemIoUnitNumberOfFans": controlSystemIoUnitNumberOfFans,
       "controlSystemIoUnitTemperatureTable": controlSystemIoUnitTemperatureTable,
       "controlSystemIoUnitTemperatureEntry": controlSystemIoUnitTemperatureEntry,
       "controlSystemIoUnitTemperatureIndex": controlSystemIoUnitTemperatureIndex,
       "controlSystemIoUnitTemperatureStatus": controlSystemIoUnitTemperatureStatus,
       "controlSystemIoUnitTemperatureDescription": controlSystemIoUnitTemperatureDescription,
       "controlSystemIoUnitTemperatureTrapRepeatCounter": controlSystemIoUnitTemperatureTrapRepeatCounter,
       "controlSystemIoUnitTemperatureAlarmEnable": controlSystemIoUnitTemperatureAlarmEnable,
       "controlSystemIoUnitTemperatureValue": controlSystemIoUnitTemperatureValue,
       "controlSystemIoUnitTemperatureMajorHighLevel": controlSystemIoUnitTemperatureMajorHighLevel,
       "controlSystemIoUnitTemperatureMinorHighLevel": controlSystemIoUnitTemperatureMinorHighLevel,
       "controlSystemIoUnitTemperatureMinorLowLevel": controlSystemIoUnitTemperatureMinorLowLevel,
       "controlSystemIoUnitTemperatureMajorLowLevel": controlSystemIoUnitTemperatureMajorLowLevel,
       "controlSystemIoUnitFanTable": controlSystemIoUnitFanTable,
       "controlSystemIoUnitFanEntry": controlSystemIoUnitFanEntry,
       "controlSystemIoUnitFanIndex": controlSystemIoUnitFanIndex,
       "controlSystemIoUnitFanSpeedValue": controlSystemIoUnitFanSpeedValue,
       "controlSystemIoUnitFanSpeedDeviation": controlSystemIoUnitFanSpeedDeviation,
       "controlSystemIoUnitFanControl": controlSystemIoUnitFanControl,
       "controlSystemInventory": controlSystemInventory,
       "controlUnitNumberOfUnits": controlUnitNumberOfUnits,
       "controlUnitTable": controlUnitTable,
       "controlUnitEntry": controlUnitEntry,
       "controlUnitIndex": controlUnitIndex,
       "controlUnitDescription": controlUnitDescription,
       "controlUnitStatus": controlUnitStatus,
       "controlUnitSerialNumber": controlUnitSerialNumber,
       "controlUnitHwPartNumber": controlUnitHwPartNumber,
       "controlUnitHwVersion": controlUnitHwVersion,
       "controlUnitSwPartNumber": controlUnitSwPartNumber,
       "controlUnitSwVersion": controlUnitSwVersion,
       "currentMonitors": currentMonitors,
       "currentMonitorsNumberOfUnits": currentMonitorsNumberOfUnits,
       "currentMonitorsTable": currentMonitorsTable,
       "currentMonitorsEntry": currentMonitorsEntry,
       "currentMonitorIndex": currentMonitorIndex,
       "currentMonitorType": currentMonitorType,
       "currentMonitorId": currentMonitorId,
       "currentMonitorNumberOfFuses": currentMonitorNumberOfFuses,
       "currentMonitorNumberOfCurrents": currentMonitorNumberOfCurrents,
       "currentMonitorFuseTable": currentMonitorFuseTable,
       "currentMonitorFuseEntry": currentMonitorFuseEntry,
       "currentMonitorFuseIndex": currentMonitorFuseIndex,
       "currentMonitorFuseStatus": currentMonitorFuseStatus,
       "currentMonitorFuseDescription": currentMonitorFuseDescription,
       "currentMonitorFuseTrapRepeatCounter": currentMonitorFuseTrapRepeatCounter,
       "currentMonitorFuseAlarmEnable": currentMonitorFuseAlarmEnable,
       "currentMonitorFuseValue": currentMonitorFuseValue,
       "currentMonitorCurrentTable": currentMonitorCurrentTable,
       "currentMonitorCurrentEntry": currentMonitorCurrentEntry,
       "currentMonitorCurrentIndex": currentMonitorCurrentIndex,
       "currentMonitorCurrentStatus": currentMonitorCurrentStatus,
       "currentMonitorCurrentDescription": currentMonitorCurrentDescription,
       "currentMonitorCurrentTrapRepeatCounter": currentMonitorCurrentTrapRepeatCounter,
       "currentMonitorCurrentAlarmEnable": currentMonitorCurrentAlarmEnable,
       "currentMonitorCurrentValue": currentMonitorCurrentValue,
       "currentMonitorCurrentMajorAlarmLevel": currentMonitorCurrentMajorAlarmLevel,
       "currentMonitorCurrentMinorAlarmLevel": currentMonitorCurrentMinorAlarmLevel,
       "currentMonitorEnergyLogAccumulatedTable": currentMonitorEnergyLogAccumulatedTable,
       "currentMonitorEnergyLogAccumulatedEntry": currentMonitorEnergyLogAccumulatedEntry,
       "currentMonitorEnergyLogAccumulated": currentMonitorEnergyLogAccumulated,
       "currentMonitorEnergyLogLastHoursNumberOfEntries": currentMonitorEnergyLogLastHoursNumberOfEntries,
       "currentMonitorEnergyLogLastHoursTable": currentMonitorEnergyLogLastHoursTable,
       "currentMonitorEnergyLogLastHoursEntry": currentMonitorEnergyLogLastHoursEntry,
       "currentMonitorEnergyLogLastHoursIndex": currentMonitorEnergyLogLastHoursIndex,
       "currentMonitorEnergyLogLastHoursValue": currentMonitorEnergyLogLastHoursValue,
       "currentMonitorEnergyLogLastDaysNumberOfEntries": currentMonitorEnergyLogLastDaysNumberOfEntries,
       "currentMonitorEnergyLogLastDaysTable": currentMonitorEnergyLogLastDaysTable,
       "currentMonitorEnergyLogLastDaysEntry": currentMonitorEnergyLogLastDaysEntry,
       "currentMonitorEnergyLogLastDaysIndex": currentMonitorEnergyLogLastDaysIndex,
       "currentMonitorEnergyLogLastDaysValue": currentMonitorEnergyLogLastDaysValue,
       "currentMonitorEnergyLogLastWeeksNumberOfEntries": currentMonitorEnergyLogLastWeeksNumberOfEntries,
       "currentMonitorEnergyLogLastWeeksTable": currentMonitorEnergyLogLastWeeksTable,
       "currentMonitorEnergyLogLastWeeksEntry": currentMonitorEnergyLogLastWeeksEntry,
       "currentMonitorEnergyLogLastWeeksIndex": currentMonitorEnergyLogLastWeeksIndex,
       "currentMonitorEnergyLogLastWeeksValue": currentMonitorEnergyLogLastWeeksValue,
       "alarmGroups": alarmGroups,
       "alarmGroupTable": alarmGroupTable,
       "alarmGroupEntry": alarmGroupEntry,
       "alarmGroupIndex": alarmGroupIndex,
       "alarmGroupStatus": alarmGroupStatus,
       "alarmGroupDescription": alarmGroupDescription}
)
