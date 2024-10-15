# SNMP MIB module (Argus-Power-System-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Argus-Power-System-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:07 2024
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

argus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309)
)
argus.setRevisions(
        ("2016-12-09 00:00",)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



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

_UpsPower_ObjectIdentity = ObjectIdentity
upsPower = _UpsPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6)
)
_UpsDevice_ObjectIdentity = ObjectIdentity
upsDevice = _UpsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1)
)


class _UpsIdentManufacturer_Type(DisplayString):
    """Custom type upsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentManufacturer_Type.__name__ = "DisplayString"
_UpsIdentManufacturer_Object = MibScalar
upsIdentManufacturer = _UpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 1),
    _UpsIdentManufacturer_Type()
)
upsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturer.setStatus("current")


class _UpsIdentProductCode_Type(DisplayString):
    """Custom type upsIdentProductCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentProductCode_Type.__name__ = "DisplayString"
_UpsIdentProductCode_Object = MibScalar
upsIdentProductCode = _UpsIdentProductCode_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 2),
    _UpsIdentProductCode_Type()
)
upsIdentProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentProductCode.setStatus("current")


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 3),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("current")


class _UpsIdentUPSSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentUPSSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentUPSSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentUPSSoftwareVersion_Object = MibScalar
upsIdentUPSSoftwareVersion = _UpsIdentUPSSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 4),
    _UpsIdentUPSSoftwareVersion_Type()
)
upsIdentUPSSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersion.setStatus("current")


class _UpsIdentAgentSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentAgentSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentAgentSoftwareVersion_Object = MibScalar
upsIdentAgentSoftwareVersion = _UpsIdentAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 5),
    _UpsIdentAgentSoftwareVersion_Type()
)
upsIdentAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersion.setStatus("current")


class _UpsIdentName_Type(DisplayString):
    """Custom type upsIdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentName_Type.__name__ = "DisplayString"
_UpsIdentName_Object = MibScalar
upsIdentName = _UpsIdentName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 6),
    _UpsIdentName_Type()
)
upsIdentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentName.setStatus("current")


class _UpsIdentAttachedDevices_Type(DisplayString):
    """Custom type upsIdentAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentAttachedDevices_Type.__name__ = "DisplayString"
_UpsIdentAttachedDevices_Object = MibScalar
upsIdentAttachedDevices = _UpsIdentAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 7),
    _UpsIdentAttachedDevices_Type()
)
upsIdentAttachedDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAttachedDevices.setStatus("current")


class _UpsIdentSiteName_Type(DisplayString):
    """Custom type upsIdentSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentSiteName_Type.__name__ = "DisplayString"
_UpsIdentSiteName_Object = MibScalar
upsIdentSiteName = _UpsIdentSiteName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 8),
    _UpsIdentSiteName_Type()
)
upsIdentSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentSiteName.setStatus("current")


class _UpsIdentSiteCity_Type(DisplayString):
    """Custom type upsIdentSiteCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentSiteCity_Type.__name__ = "DisplayString"
_UpsIdentSiteCity_Object = MibScalar
upsIdentSiteCity = _UpsIdentSiteCity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 9),
    _UpsIdentSiteCity_Type()
)
upsIdentSiteCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentSiteCity.setStatus("current")


class _UpsIdentSiteRegion_Type(DisplayString):
    """Custom type upsIdentSiteRegion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentSiteRegion_Type.__name__ = "DisplayString"
_UpsIdentSiteRegion_Object = MibScalar
upsIdentSiteRegion = _UpsIdentSiteRegion_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 10),
    _UpsIdentSiteRegion_Type()
)
upsIdentSiteRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentSiteRegion.setStatus("current")


class _UpsIdentSiteCountry_Type(DisplayString):
    """Custom type upsIdentSiteCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentSiteCountry_Type.__name__ = "DisplayString"
_UpsIdentSiteCountry_Object = MibScalar
upsIdentSiteCountry = _UpsIdentSiteCountry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 11),
    _UpsIdentSiteCountry_Type()
)
upsIdentSiteCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentSiteCountry.setStatus("current")


class _UpsIdentContactName_Type(DisplayString):
    """Custom type upsIdentContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentContactName_Type.__name__ = "DisplayString"
_UpsIdentContactName_Object = MibScalar
upsIdentContactName = _UpsIdentContactName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 12),
    _UpsIdentContactName_Type()
)
upsIdentContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentContactName.setStatus("current")


class _UpsIdentPhoneNumber_Type(DisplayString):
    """Custom type upsIdentPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentPhoneNumber_Type.__name__ = "DisplayString"
_UpsIdentPhoneNumber_Object = MibScalar
upsIdentPhoneNumber = _UpsIdentPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 13),
    _UpsIdentPhoneNumber_Type()
)
upsIdentPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentPhoneNumber.setStatus("current")


class _UpsIdentDate_Type(DisplayString):
    """Custom type upsIdentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentDate_Type.__name__ = "DisplayString"
_UpsIdentDate_Object = MibScalar
upsIdentDate = _UpsIdentDate_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 14),
    _UpsIdentDate_Type()
)
upsIdentDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentDate.setStatus("current")


class _UpsIdentTime_Type(DisplayString):
    """Custom type upsIdentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsIdentTime_Type.__name__ = "DisplayString"
_UpsIdentTime_Object = MibScalar
upsIdentTime = _UpsIdentTime_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 1, 15),
    _UpsIdentTime_Type()
)
upsIdentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentTime.setStatus("current")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2)
)


class _UpsBatteryStatus_Type(Integer32):
    """Custom type upsBatteryStatus based on Integer32"""
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
        *(("batteryDepleted", 4),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_UpsBatteryStatus_Type.__name__ = "Integer32"
_UpsBatteryStatus_Object = MibScalar
upsBatteryStatus = _UpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("current")
_UpsMinutesOnBattery_Type = Integer32
_UpsMinutesOnBattery_Object = MibScalar
upsMinutesOnBattery = _UpsMinutesOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 2),
    _UpsMinutesOnBattery_Type()
)
upsMinutesOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMinutesOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    upsMinutesOnBattery.setUnits("minutes")
_UpsBatteryVoltage_Type = Integer32
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 3),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setUnits("0.1 Volt DC")
_UpsBatteryChargingCurrent_Type = Integer32
_UpsBatteryChargingCurrent_Object = MibScalar
upsBatteryChargingCurrent = _UpsBatteryChargingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 4),
    _UpsBatteryChargingCurrent_Type()
)
upsBatteryChargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryChargingCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryChargingCurrent.setUnits("0.1 Amp DC")
_UpsBatteryCapacity_Type = Integer32
_UpsBatteryCapacity_Object = MibScalar
upsBatteryCapacity = _UpsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 5),
    _UpsBatteryCapacity_Type()
)
upsBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCapacity.setUnits("0.1 Amp DC")
_UpsBatteryTemperature_Type = Integer32
_UpsBatteryTemperature_Object = MibScalar
upsBatteryTemperature = _UpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 6),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setUnits("degrees Centigrade")
_UpsBatteryLowWarning_Type = Integer32
_UpsBatteryLowWarning_Object = MibScalar
upsBatteryLowWarning = _UpsBatteryLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 2, 7),
    _UpsBatteryLowWarning_Type()
)
upsBatteryLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryLowWarning.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryLowWarning.setUnits("percentage")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 3)
)
_UpsInputNumLines_Type = Integer32
_UpsInputNumLines_Object = MibScalar
upsInputNumLines = _UpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 1),
    _UpsInputNumLines_Type()
)
upsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLines.setStatus("current")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("current")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1)
)
upsInputEntry.setIndexNames(
    (0, "Argus-Power-System-MIB", "upsInputLineIndex"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("current")
_UpsInputLineIndex_Type = Integer32
_UpsInputLineIndex_Object = MibTableColumn
upsInputLineIndex = _UpsInputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 1),
    _UpsInputLineIndex_Type()
)
upsInputLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndex.setStatus("current")
_UpsInputFrequency_Type = Integer32
_UpsInputFrequency_Object = MibTableColumn
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 2),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequency.setUnits("Hertz")
_UpsInputVoltage_Type = Integer32
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 3, 2, 1, 3),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltage.setUnits("0.1 RMS Volts")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4)
)


class _UpsOutputSource_Type(Integer32):
    """Custom type upsOutputSource based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("boost1", 4),
          ("boost2", 3),
          ("buck1", 5),
          ("buck2", 6),
          ("bypass", 11),
          ("inverter", 7),
          ("line", 2),
          ("retransfer", 8),
          ("shutdown", 10),
          ("standby", 1),
          ("transfer", 9))
    )


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 1),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("current")
_UpsOutputFrequency_Type = Integer32
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequency.setUnits("0.1 Hertz")
_UpsOutputNumLines_Type = Integer32
_UpsOutputNumLines_Object = MibScalar
upsOutputNumLines = _UpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 3),
    _UpsOutputNumLines_Type()
)
upsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLines.setStatus("current")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("current")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1)
)
upsOutputEntry.setIndexNames(
    (0, "Argus-Power-System-MIB", "upsOutputLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("current")
_UpsOutputLineIndex_Type = Integer32
_UpsOutputLineIndex_Object = MibTableColumn
upsOutputLineIndex = _UpsOutputLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 1),
    _UpsOutputLineIndex_Type()
)
upsOutputLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndex.setStatus("current")
_UpsOutputVoltage_Type = Integer32
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltage.setUnits("0.1 RMS Volts")
_UpsOutputCurrent_Type = Integer32
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrent.setUnits("0.1 RMS Amp")
_UpsOutputPowerVA_Type = Integer32
_UpsOutputPowerVA_Object = MibTableColumn
upsOutputPowerVA = _UpsOutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 4),
    _UpsOutputPowerVA_Type()
)
upsOutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerVA.setUnits("VA")
_UpsOutputPowerWatt_Type = Integer32
_UpsOutputPowerWatt_Object = MibTableColumn
upsOutputPowerWatt = _UpsOutputPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 5),
    _UpsOutputPowerWatt_Type()
)
upsOutputPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerWatt.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerWatt.setUnits("Watts")
_UpsPowerFactor_Type = Integer32
_UpsPowerFactor_Object = MibTableColumn
upsPowerFactor = _UpsPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 6),
    _UpsPowerFactor_Type()
)
upsPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    upsPowerFactor.setUnits("percent")


class _UpsOutputPercentLoad_Type(Integer32):
    """Custom type upsOutputPercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoad_Type.__name__ = "Integer32"
_UpsOutputPercentLoad_Object = MibTableColumn
upsOutputPercentLoad = _UpsOutputPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 4, 4, 1, 7),
    _UpsOutputPercentLoad_Type()
)
upsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setUnits("percent")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 5)
)
_UpsAlarmsPresent_Type = Integer32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("current")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("current")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "Argus-Power-System-MIB", "upsAlarmId"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("current")
_UpsAlarmId_Type = Integer32
_UpsAlarmId_Object = MibTableColumn
upsAlarmId = _UpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 1),
    _UpsAlarmId_Type()
)
upsAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmId.setStatus("current")


class _UpsAlarmDescr_Type(DisplayString):
    """Custom type upsAlarmDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsAlarmDescr_Type.__name__ = "DisplayString"
_UpsAlarmDescr_Object = MibTableColumn
upsAlarmDescr = _UpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 2),
    _UpsAlarmDescr_Type()
)
upsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescr.setStatus("current")
_UpsAlarmStatus_Type = Integer32
_UpsAlarmStatus_Object = MibTableColumn
upsAlarmStatus = _UpsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 5, 2, 1, 3),
    _UpsAlarmStatus_Type()
)
upsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmStatus.setStatus("current")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6)
)
_UpsConfigLineQualifyTime_Type = Integer32
_UpsConfigLineQualifyTime_Object = MibScalar
upsConfigLineQualifyTime = _UpsConfigLineQualifyTime_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 1),
    _UpsConfigLineQualifyTime_Type()
)
upsConfigLineQualifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigLineQualifyTime.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLineQualifyTime.setUnits("seconds")
_UpsConfigLineOutputVoltageHighLimit_Type = Integer32
_UpsConfigLineOutputVoltageHighLimit_Object = MibScalar
upsConfigLineOutputVoltageHighLimit = _UpsConfigLineOutputVoltageHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 2),
    _UpsConfigLineOutputVoltageHighLimit_Type()
)
upsConfigLineOutputVoltageHighLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigLineOutputVoltageHighLimit.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLineOutputVoltageHighLimit.setUnits("volttenth")
_UpsConfigLineOutputVoltageLowLimit_Type = Integer32
_UpsConfigLineOutputVoltageLowLimit_Object = MibScalar
upsConfigLineOutputVoltageLowLimit = _UpsConfigLineOutputVoltageLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 3),
    _UpsConfigLineOutputVoltageLowLimit_Type()
)
upsConfigLineOutputVoltageLowLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigLineOutputVoltageLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLineOutputVoltageLowLimit.setUnits("volttenth")
_UpsConfigFanOnTemperature_Type = Integer32
_UpsConfigFanOnTemperature_Object = MibScalar
upsConfigFanOnTemperature = _UpsConfigFanOnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 4),
    _UpsConfigFanOnTemperature_Type()
)
upsConfigFanOnTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigFanOnTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigFanOnTemperature.setUnits("degreeC")
_UpsShutdownStatus_Type = Integer32
_UpsShutdownStatus_Object = MibScalar
upsShutdownStatus = _UpsShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 5),
    _UpsShutdownStatus_Type()
)
upsShutdownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownStatus.setStatus("current")
_UpsInverterOffDelayTime_Type = Integer32
_UpsInverterOffDelayTime_Object = MibScalar
upsInverterOffDelayTime = _UpsInverterOffDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 6),
    _UpsInverterOffDelayTime_Type()
)
upsInverterOffDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOffDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    upsInverterOffDelayTime.setUnits("seconds")


class _UpsConfigIPAddress_Type(DisplayString):
    """Custom type upsConfigIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsConfigIPAddress_Type.__name__ = "DisplayString"
_UpsConfigIPAddress_Object = MibScalar
upsConfigIPAddress = _UpsConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 7),
    _UpsConfigIPAddress_Type()
)
upsConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigIPAddress.setStatus("current")


class _UpsConfigNetMask_Type(DisplayString):
    """Custom type upsConfigNetMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsConfigNetMask_Type.__name__ = "DisplayString"
_UpsConfigNetMask_Object = MibScalar
upsConfigNetMask = _UpsConfigNetMask_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 8),
    _UpsConfigNetMask_Type()
)
upsConfigNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNetMask.setStatus("current")


class _UpsConfigGateway_Type(DisplayString):
    """Custom type upsConfigGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsConfigGateway_Type.__name__ = "DisplayString"
_UpsConfigGateway_Object = MibScalar
upsConfigGateway = _UpsConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 9),
    _UpsConfigGateway_Type()
)
upsConfigGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigGateway.setStatus("current")


class _UpsConfigSnmpCommunity_Type(DisplayString):
    """Custom type upsConfigSnmpCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsConfigSnmpCommunity_Type.__name__ = "DisplayString"
_UpsConfigSnmpCommunity_Object = MibScalar
upsConfigSnmpCommunity = _UpsConfigSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 10),
    _UpsConfigSnmpCommunity_Type()
)
upsConfigSnmpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigSnmpCommunity.setStatus("current")


class _UpsConfigSnmpTrapIPDestination_Type(DisplayString):
    """Custom type upsConfigSnmpTrapIPDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsConfigSnmpTrapIPDestination_Type.__name__ = "DisplayString"
_UpsConfigSnmpTrapIPDestination_Object = MibScalar
upsConfigSnmpTrapIPDestination = _UpsConfigSnmpTrapIPDestination_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 6, 11),
    _UpsConfigSnmpTrapIPDestination_Type()
)
upsConfigSnmpTrapIPDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigSnmpTrapIPDestination.setStatus("current")
_UpsTraps_ObjectIdentity = ObjectIdentity
upsTraps = _UpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 7)
)
_UpsTrap_ObjectIdentity = ObjectIdentity
upsTrap = _UpsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0)
)
_UpsExtra_ObjectIdentity = ObjectIdentity
upsExtra = _UpsExtra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8)
)


class _UpsExtraCount_Type(Integer32):
    """Custom type upsExtraCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsExtraCount_Type.__name__ = "Integer32"
_UpsExtraCount_Object = MibScalar
upsExtraCount = _UpsExtraCount_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 1),
    _UpsExtraCount_Type()
)
upsExtraCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtraCount.setStatus("current")
_UpsExtraTable_Object = MibTable
upsExtraTable = _UpsExtraTable_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2)
)
if mibBuilder.loadTexts:
    upsExtraTable.setStatus("current")
_UpsExtraEntry_Object = MibTableRow
upsExtraEntry = _UpsExtraEntry_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1)
)
upsExtraEntry.setIndexNames(
    (0, "Argus-Power-System-MIB", "upsExtraIndex"),
)
if mibBuilder.loadTexts:
    upsExtraEntry.setStatus("current")


class _UpsExtraIndex_Type(Integer32):
    """Custom type upsExtraIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsExtraIndex_Type.__name__ = "Integer32"
_UpsExtraIndex_Object = MibTableColumn
upsExtraIndex = _UpsExtraIndex_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 1),
    _UpsExtraIndex_Type()
)
upsExtraIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtraIndex.setStatus("current")


class _UpsExtraName_Type(DisplayString):
    """Custom type upsExtraName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_UpsExtraName_Type.__name__ = "DisplayString"
_UpsExtraName_Object = MibTableColumn
upsExtraName = _UpsExtraName_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 2),
    _UpsExtraName_Type()
)
upsExtraName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtraName.setStatus("current")


class _UpsExtraIntegerValue_Type(Integer32):
    """Custom type upsExtraIntegerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )


_UpsExtraIntegerValue_Type.__name__ = "Integer32"
_UpsExtraIntegerValue_Object = MibTableColumn
upsExtraIntegerValue = _UpsExtraIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 3),
    _UpsExtraIntegerValue_Type()
)
upsExtraIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtraIntegerValue.setStatus("current")


class _UpsExtraStringValue_Type(DisplayString):
    """Custom type upsExtraStringValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpsExtraStringValue_Type.__name__ = "DisplayString"
_UpsExtraStringValue_Object = MibTableColumn
upsExtraStringValue = _UpsExtraStringValue_Object(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 8, 2, 1, 4),
    _UpsExtraStringValue_Type()
)
upsExtraStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsExtraStringValue.setStatus("current")

# Managed Objects groups


# Notification objects

upsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 1)
)
upsAlarmTrap.setObjects(
      *(("Argus-Power-System-MIB", "upsExtraIntegerValue"),
        ("Argus-Power-System-MIB", "upsExtraStringValue"),
        ("Argus-Power-System-MIB", "upsExtraIndex"),
        ("Argus-Power-System-MIB", "upsExtraName"))
)
if mibBuilder.loadTexts:
    upsAlarmTrap.setStatus(
        "current"
    )

upsAgentStartupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 2)
)
upsAgentStartupTrap.setObjects(
    ("Argus-Power-System-MIB", "upsIdentSiteName")
)
if mibBuilder.loadTexts:
    upsAgentStartupTrap.setStatus(
        "current"
    )

upsAgentShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 3)
)
upsAgentShutdownTrap.setObjects(
    ("Argus-Power-System-MIB", "upsIdentSiteName")
)
if mibBuilder.loadTexts:
    upsAgentShutdownTrap.setStatus(
        "current"
    )

upsAgentFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 4)
)
upsAgentFaultTrap.setObjects(
      *(("Argus-Power-System-MIB", "upsExtraIntegerValue"),
        ("Argus-Power-System-MIB", "upsExtraStringValue"),
        ("Argus-Power-System-MIB", "upsExtraIndex"),
        ("Argus-Power-System-MIB", "upsExtraName"))
)
if mibBuilder.loadTexts:
    upsAgentFaultTrap.setStatus(
        "current"
    )

upsAgentEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7309, 6, 1, 7, 0, 5)
)
upsAgentEventTrap.setObjects(
      *(("Argus-Power-System-MIB", "upsExtraIntegerValue"),
        ("Argus-Power-System-MIB", "upsExtraStringValue"),
        ("Argus-Power-System-MIB", "upsExtraIndex"),
        ("Argus-Power-System-MIB", "upsExtraName"))
)
if mibBuilder.loadTexts:
    upsAgentEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Argus-Power-System-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "argus": argus,
       "upsPower": upsPower,
       "upsDevice": upsDevice,
       "upsIdent": upsIdent,
       "upsIdentManufacturer": upsIdentManufacturer,
       "upsIdentProductCode": upsIdentProductCode,
       "upsIdentModel": upsIdentModel,
       "upsIdentUPSSoftwareVersion": upsIdentUPSSoftwareVersion,
       "upsIdentAgentSoftwareVersion": upsIdentAgentSoftwareVersion,
       "upsIdentName": upsIdentName,
       "upsIdentAttachedDevices": upsIdentAttachedDevices,
       "upsIdentSiteName": upsIdentSiteName,
       "upsIdentSiteCity": upsIdentSiteCity,
       "upsIdentSiteRegion": upsIdentSiteRegion,
       "upsIdentSiteCountry": upsIdentSiteCountry,
       "upsIdentContactName": upsIdentContactName,
       "upsIdentPhoneNumber": upsIdentPhoneNumber,
       "upsIdentDate": upsIdentDate,
       "upsIdentTime": upsIdentTime,
       "upsBattery": upsBattery,
       "upsBatteryStatus": upsBatteryStatus,
       "upsMinutesOnBattery": upsMinutesOnBattery,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryChargingCurrent": upsBatteryChargingCurrent,
       "upsBatteryCapacity": upsBatteryCapacity,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsBatteryLowWarning": upsBatteryLowWarning,
       "upsInput": upsInput,
       "upsInputNumLines": upsInputNumLines,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputLineIndex": upsInputLineIndex,
       "upsInputFrequency": upsInputFrequency,
       "upsInputVoltage": upsInputVoltage,
       "upsOutput": upsOutput,
       "upsOutputSource": upsOutputSource,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputNumLines": upsOutputNumLines,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputLineIndex": upsOutputLineIndex,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputPowerVA": upsOutputPowerVA,
       "upsOutputPowerWatt": upsOutputPowerWatt,
       "upsPowerFactor": upsPowerFactor,
       "upsOutputPercentLoad": upsOutputPercentLoad,
       "upsAlarm": upsAlarm,
       "upsAlarmsPresent": upsAlarmsPresent,
       "upsAlarmTable": upsAlarmTable,
       "upsAlarmEntry": upsAlarmEntry,
       "upsAlarmId": upsAlarmId,
       "upsAlarmDescr": upsAlarmDescr,
       "upsAlarmStatus": upsAlarmStatus,
       "upsConfig": upsConfig,
       "upsConfigLineQualifyTime": upsConfigLineQualifyTime,
       "upsConfigLineOutputVoltageHighLimit": upsConfigLineOutputVoltageHighLimit,
       "upsConfigLineOutputVoltageLowLimit": upsConfigLineOutputVoltageLowLimit,
       "upsConfigFanOnTemperature": upsConfigFanOnTemperature,
       "upsShutdownStatus": upsShutdownStatus,
       "upsInverterOffDelayTime": upsInverterOffDelayTime,
       "upsConfigIPAddress": upsConfigIPAddress,
       "upsConfigNetMask": upsConfigNetMask,
       "upsConfigGateway": upsConfigGateway,
       "upsConfigSnmpCommunity": upsConfigSnmpCommunity,
       "upsConfigSnmpTrapIPDestination": upsConfigSnmpTrapIPDestination,
       "upsTraps": upsTraps,
       "upsTrap": upsTrap,
       "upsAlarmTrap": upsAlarmTrap,
       "upsAgentStartupTrap": upsAgentStartupTrap,
       "upsAgentShutdownTrap": upsAgentShutdownTrap,
       "upsAgentFaultTrap": upsAgentFaultTrap,
       "upsAgentEventTrap": upsAgentEventTrap,
       "upsExtra": upsExtra,
       "upsExtraCount": upsExtraCount,
       "upsExtraTable": upsExtraTable,
       "upsExtraEntry": upsExtraEntry,
       "upsExtraIndex": upsExtraIndex,
       "upsExtraName": upsExtraName,
       "upsExtraIntegerValue": upsExtraIntegerValue,
       "upsExtraStringValue": upsExtraStringValue}
)
