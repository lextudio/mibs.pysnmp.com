# SNMP MIB module (SYNOLOGY-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOLOGY-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:00 2024
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

(Float,) = mibBuilder.importSymbols(
    "NET-SNMP-TC",
    "Float")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

synoUPS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4)
)
synoUPS.setRevisions(
        ("2013-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NonNegativeInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_UpsDevice_ObjectIdentity = ObjectIdentity
upsDevice = _UpsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1)
)


class _UpsDeviceModel_Type(DisplayString):
    """Custom type upsDeviceModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDeviceModel_Type.__name__ = "DisplayString"
_UpsDeviceModel_Object = MibScalar
upsDeviceModel = _UpsDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 1),
    _UpsDeviceModel_Type()
)
upsDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceModel.setStatus("current")


class _UpsDeviceManufacturer_Type(DisplayString):
    """Custom type upsDeviceManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsDeviceManufacturer_Type.__name__ = "DisplayString"
_UpsDeviceManufacturer_Object = MibScalar
upsDeviceManufacturer = _UpsDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 2),
    _UpsDeviceManufacturer_Type()
)
upsDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceManufacturer.setStatus("current")


class _UpsDeviceSerial_Type(DisplayString):
    """Custom type upsDeviceSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDeviceSerial_Type.__name__ = "DisplayString"
_UpsDeviceSerial_Object = MibScalar
upsDeviceSerial = _UpsDeviceSerial_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 3),
    _UpsDeviceSerial_Type()
)
upsDeviceSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceSerial.setStatus("current")


class _UpsDeviceType_Type(DisplayString):
    """Custom type upsDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDeviceType_Type.__name__ = "DisplayString"
_UpsDeviceType_Object = MibScalar
upsDeviceType = _UpsDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 4),
    _UpsDeviceType_Type()
)
upsDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceType.setStatus("current")


class _UpsDeviceDescription_Type(DisplayString):
    """Custom type upsDeviceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDeviceDescription_Type.__name__ = "DisplayString"
_UpsDeviceDescription_Object = MibScalar
upsDeviceDescription = _UpsDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 5),
    _UpsDeviceDescription_Type()
)
upsDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceDescription.setStatus("current")


class _UpsDeviceContact_Type(DisplayString):
    """Custom type upsDeviceContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDeviceContact_Type.__name__ = "DisplayString"
_UpsDeviceContact_Object = MibScalar
upsDeviceContact = _UpsDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 6),
    _UpsDeviceContact_Type()
)
upsDeviceContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceContact.setStatus("current")


class _UpsDeviceLocation_Type(DisplayString):
    """Custom type upsDeviceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDeviceLocation_Type.__name__ = "DisplayString"
_UpsDeviceLocation_Object = MibScalar
upsDeviceLocation = _UpsDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 7),
    _UpsDeviceLocation_Type()
)
upsDeviceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceLocation.setStatus("current")


class _UpsDevicePart_Type(DisplayString):
    """Custom type upsDevicePart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDevicePart_Type.__name__ = "DisplayString"
_UpsDevicePart_Object = MibScalar
upsDevicePart = _UpsDevicePart_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 8),
    _UpsDevicePart_Type()
)
upsDevicePart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDevicePart.setStatus("current")


class _UpsDeviceMACAddr_Type(DisplayString):
    """Custom type upsDeviceMACAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDeviceMACAddr_Type.__name__ = "DisplayString"
_UpsDeviceMACAddr_Object = MibScalar
upsDeviceMACAddr = _UpsDeviceMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 1, 9),
    _UpsDeviceMACAddr_Type()
)
upsDeviceMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDeviceMACAddr.setStatus("current")
_UpsInfo_ObjectIdentity = ObjectIdentity
upsInfo = _UpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2)
)


class _UpsInfoStatus_Type(DisplayString):
    """Custom type upsInfoStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoStatus_Type.__name__ = "DisplayString"
_UpsInfoStatus_Object = MibScalar
upsInfoStatus = _UpsInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 1),
    _UpsInfoStatus_Type()
)
upsInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoStatus.setStatus("current")


class _UpsInfoAlarm_Type(DisplayString):
    """Custom type upsInfoAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoAlarm_Type.__name__ = "DisplayString"
_UpsInfoAlarm_Object = MibScalar
upsInfoAlarm = _UpsInfoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 2),
    _UpsInfoAlarm_Type()
)
upsInfoAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoAlarm.setStatus("current")


class _UpsInfoTime_Type(DisplayString):
    """Custom type upsInfoTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoTime_Type.__name__ = "DisplayString"
_UpsInfoTime_Object = MibScalar
upsInfoTime = _UpsInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 3),
    _UpsInfoTime_Type()
)
upsInfoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoTime.setStatus("current")


class _UpsInfoDate_Type(DisplayString):
    """Custom type upsInfoDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoDate_Type.__name__ = "DisplayString"
_UpsInfoDate_Object = MibScalar
upsInfoDate = _UpsInfoDate_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 4),
    _UpsInfoDate_Type()
)
upsInfoDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoDate.setStatus("current")


class _UpsInfoModel_Type(DisplayString):
    """Custom type upsInfoModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoModel_Type.__name__ = "DisplayString"
_UpsInfoModel_Object = MibScalar
upsInfoModel = _UpsInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 5),
    _UpsInfoModel_Type()
)
upsInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoModel.setStatus("current")
_UpsInfoMfr_ObjectIdentity = ObjectIdentity
upsInfoMfr = _UpsInfoMfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 6)
)


class _UpsInfoMfrName_Type(DisplayString):
    """Custom type upsInfoMfrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoMfrName_Type.__name__ = "DisplayString"
_UpsInfoMfrName_Object = MibScalar
upsInfoMfrName = _UpsInfoMfrName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 6, 1),
    _UpsInfoMfrName_Type()
)
upsInfoMfrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoMfrName.setStatus("current")


class _UpsInfoMfrDate_Type(DisplayString):
    """Custom type upsInfoMfrDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoMfrDate_Type.__name__ = "DisplayString"
_UpsInfoMfrDate_Object = MibScalar
upsInfoMfrDate = _UpsInfoMfrDate_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 6, 2),
    _UpsInfoMfrDate_Type()
)
upsInfoMfrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoMfrDate.setStatus("current")


class _UpsInfoSerial_Type(DisplayString):
    """Custom type upsInfoSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoSerial_Type.__name__ = "DisplayString"
_UpsInfoSerial_Object = MibScalar
upsInfoSerial = _UpsInfoSerial_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 7),
    _UpsInfoSerial_Type()
)
upsInfoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoSerial.setStatus("current")


class _UpsInfoVendorID_Type(DisplayString):
    """Custom type upsInfoVendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoVendorID_Type.__name__ = "DisplayString"
_UpsInfoVendorID_Object = MibScalar
upsInfoVendorID = _UpsInfoVendorID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 8),
    _UpsInfoVendorID_Type()
)
upsInfoVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoVendorID.setStatus("current")


class _UpsInfoProductID_Type(DisplayString):
    """Custom type upsInfoProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoProductID_Type.__name__ = "DisplayString"
_UpsInfoProductID_Object = MibScalar
upsInfoProductID = _UpsInfoProductID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 9),
    _UpsInfoProductID_Type()
)
upsInfoProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoProductID.setStatus("current")
_UpsInfoFirmware_ObjectIdentity = ObjectIdentity
upsInfoFirmware = _UpsInfoFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 10)
)


class _UpsInfoFirmwareName_Type(DisplayString):
    """Custom type upsInfoFirmwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoFirmwareName_Type.__name__ = "DisplayString"
_UpsInfoFirmwareName_Object = MibScalar
upsInfoFirmwareName = _UpsInfoFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 10, 1),
    _UpsInfoFirmwareName_Type()
)
upsInfoFirmwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoFirmwareName.setStatus("current")


class _UpsInfoFirmwareAux_Type(DisplayString):
    """Custom type upsInfoFirmwareAux based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoFirmwareAux_Type.__name__ = "DisplayString"
_UpsInfoFirmwareAux_Object = MibScalar
upsInfoFirmwareAux = _UpsInfoFirmwareAux_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 10, 2),
    _UpsInfoFirmwareAux_Type()
)
upsInfoFirmwareAux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoFirmwareAux.setStatus("current")
_UpsInfoTemperature_Type = Float
_UpsInfoTemperature_Object = MibScalar
upsInfoTemperature = _UpsInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 11),
    _UpsInfoTemperature_Type()
)
upsInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoTemperature.setUnits("degree C")
_UpsInfoLoad_ObjectIdentity = ObjectIdentity
upsInfoLoad = _UpsInfoLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 12)
)
_UpsInfoLoadValue_Type = Float
_UpsInfoLoadValue_Object = MibScalar
upsInfoLoadValue = _UpsInfoLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 12, 1),
    _UpsInfoLoadValue_Type()
)
upsInfoLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoLoadValue.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoLoadValue.setUnits("percentage")
_UpsInfoLoadHigh_Type = Float
_UpsInfoLoadHigh_Object = MibScalar
upsInfoLoadHigh = _UpsInfoLoadHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 12, 2),
    _UpsInfoLoadHigh_Type()
)
upsInfoLoadHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoLoadHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoLoadHigh.setUnits("percentage")


class _UpsInfoID_Type(DisplayString):
    """Custom type upsInfoID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoID_Type.__name__ = "DisplayString"
_UpsInfoID_Object = MibScalar
upsInfoID = _UpsInfoID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 13),
    _UpsInfoID_Type()
)
upsInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoID.setStatus("current")
_UpsInfoDelay_ObjectIdentity = ObjectIdentity
upsInfoDelay = _UpsInfoDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 14)
)
_UpsInfoDelayStart_Type = NonNegativeInteger
_UpsInfoDelayStart_Object = MibScalar
upsInfoDelayStart = _UpsInfoDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 14, 1),
    _UpsInfoDelayStart_Type()
)
upsInfoDelayStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoDelayStart.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoDelayStart.setUnits("seconds")
_UpsInfoDelayReboot_Type = NonNegativeInteger
_UpsInfoDelayReboot_Object = MibScalar
upsInfoDelayReboot = _UpsInfoDelayReboot_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 14, 2),
    _UpsInfoDelayReboot_Type()
)
upsInfoDelayReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoDelayReboot.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoDelayReboot.setUnits("seconds")
_UpsInfoDelayShutdown_Type = NonNegativeInteger
_UpsInfoDelayShutdown_Object = MibScalar
upsInfoDelayShutdown = _UpsInfoDelayShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 14, 3),
    _UpsInfoDelayShutdown_Type()
)
upsInfoDelayShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoDelayShutdown.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoDelayShutdown.setUnits("seconds")
_UpsInfoTimer_ObjectIdentity = ObjectIdentity
upsInfoTimer = _UpsInfoTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 15)
)
_UpsInfoTimerStart_Type = NonNegativeInteger
_UpsInfoTimerStart_Object = MibScalar
upsInfoTimerStart = _UpsInfoTimerStart_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 15, 1),
    _UpsInfoTimerStart_Type()
)
upsInfoTimerStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoTimerStart.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoTimerStart.setUnits("seconds")
_UpsInfoTimerReboot_Type = NonNegativeInteger
_UpsInfoTimerReboot_Object = MibScalar
upsInfoTimerReboot = _UpsInfoTimerReboot_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 15, 2),
    _UpsInfoTimerReboot_Type()
)
upsInfoTimerReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoTimerReboot.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoTimerReboot.setUnits("seconds")
_UpsInfoTimerShutdown_Type = NonNegativeInteger
_UpsInfoTimerShutdown_Object = MibScalar
upsInfoTimerShutdown = _UpsInfoTimerShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 15, 3),
    _UpsInfoTimerShutdown_Type()
)
upsInfoTimerShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoTimerShutdown.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoTimerShutdown.setUnits("seconds")
_UpsInfoTest_ObjectIdentity = ObjectIdentity
upsInfoTest = _UpsInfoTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 16)
)
_UpsInfoTestInterval_Type = NonNegativeInteger
_UpsInfoTestInterval_Object = MibScalar
upsInfoTestInterval = _UpsInfoTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 16, 1),
    _UpsInfoTestInterval_Type()
)
upsInfoTestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoTestInterval.setUnits("seconds")


class _UpsInfoTestResult_Type(DisplayString):
    """Custom type upsInfoTestResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoTestResult_Type.__name__ = "DisplayString"
_UpsInfoTestResult_Object = MibScalar
upsInfoTestResult = _UpsInfoTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 16, 2),
    _UpsInfoTestResult_Type()
)
upsInfoTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoTestResult.setStatus("current")


class _UpsInfoDisplayLanguage_Type(DisplayString):
    """Custom type upsInfoDisplayLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoDisplayLanguage_Type.__name__ = "DisplayString"
_UpsInfoDisplayLanguage_Object = MibScalar
upsInfoDisplayLanguage = _UpsInfoDisplayLanguage_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 17),
    _UpsInfoDisplayLanguage_Type()
)
upsInfoDisplayLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoDisplayLanguage.setStatus("current")


class _UpsInfoContacts_Type(DisplayString):
    """Custom type upsInfoContacts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoContacts_Type.__name__ = "DisplayString"
_UpsInfoContacts_Object = MibScalar
upsInfoContacts = _UpsInfoContacts_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 18),
    _UpsInfoContacts_Type()
)
upsInfoContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoContacts.setStatus("current")
_UpsInfoEffciency_Type = NonNegativeInteger
_UpsInfoEffciency_Object = MibScalar
upsInfoEffciency = _UpsInfoEffciency_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 19),
    _UpsInfoEffciency_Type()
)
upsInfoEffciency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoEffciency.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoEffciency.setUnits("percent")
_UpsInfoPower_ObjectIdentity = ObjectIdentity
upsInfoPower = _UpsInfoPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 20)
)
_UpsInfoPowerValue_Type = Float
_UpsInfoPowerValue_Object = MibScalar
upsInfoPowerValue = _UpsInfoPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 20, 1),
    _UpsInfoPowerValue_Type()
)
upsInfoPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoPowerValue.setUnits("Volt-Amps")
_UpsInfoPowerNominal_Type = Float
_UpsInfoPowerNominal_Object = MibScalar
upsInfoPowerNominal = _UpsInfoPowerNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 20, 2),
    _UpsInfoPowerNominal_Type()
)
upsInfoPowerNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoPowerNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoPowerNominal.setUnits("Volt-Amps")
_UpsInfoRealPower_ObjectIdentity = ObjectIdentity
upsInfoRealPower = _UpsInfoRealPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 21)
)
_UpsInfoRealPowerValue_Type = Float
_UpsInfoRealPowerValue_Object = MibScalar
upsInfoRealPowerValue = _UpsInfoRealPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 21, 1),
    _UpsInfoRealPowerValue_Type()
)
upsInfoRealPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoRealPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoRealPowerValue.setUnits("Watts")
_UpsInfoRealPowerNominal_Type = Float
_UpsInfoRealPowerNominal_Object = MibScalar
upsInfoRealPowerNominal = _UpsInfoRealPowerNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 21, 2),
    _UpsInfoRealPowerNominal_Type()
)
upsInfoRealPowerNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoRealPowerNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsInfoRealPowerNominal.setUnits("Watts")


class _UpsInfoBeeperStatus_Type(DisplayString):
    """Custom type upsInfoBeeperStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoBeeperStatus_Type.__name__ = "DisplayString"
_UpsInfoBeeperStatus_Object = MibScalar
upsInfoBeeperStatus = _UpsInfoBeeperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 22),
    _UpsInfoBeeperStatus_Type()
)
upsInfoBeeperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoBeeperStatus.setStatus("current")


class _UpsInfoType_Type(DisplayString):
    """Custom type upsInfoType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoType_Type.__name__ = "DisplayString"
_UpsInfoType_Object = MibScalar
upsInfoType = _UpsInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 23),
    _UpsInfoType_Type()
)
upsInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoType.setStatus("current")


class _UpsInfoWatchdogStatus_Type(DisplayString):
    """Custom type upsInfoWatchdogStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoWatchdogStatus_Type.__name__ = "DisplayString"
_UpsInfoWatchdogStatus_Object = MibScalar
upsInfoWatchdogStatus = _UpsInfoWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 24),
    _UpsInfoWatchdogStatus_Type()
)
upsInfoWatchdogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoWatchdogStatus.setStatus("current")
_UpsInfoStart_ObjectIdentity = ObjectIdentity
upsInfoStart = _UpsInfoStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 25)
)


class _UpsInfoStartAuto_Type(DisplayString):
    """Custom type upsInfoStartAuto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoStartAuto_Type.__name__ = "DisplayString"
_UpsInfoStartAuto_Object = MibScalar
upsInfoStartAuto = _UpsInfoStartAuto_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 25, 1),
    _UpsInfoStartAuto_Type()
)
upsInfoStartAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoStartAuto.setStatus("current")


class _UpsInfoStartBattery_Type(DisplayString):
    """Custom type upsInfoStartBattery based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoStartBattery_Type.__name__ = "DisplayString"
_UpsInfoStartBattery_Object = MibScalar
upsInfoStartBattery = _UpsInfoStartBattery_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 25, 2),
    _UpsInfoStartBattery_Type()
)
upsInfoStartBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoStartBattery.setStatus("current")


class _UpsInfoStartReboot_Type(DisplayString):
    """Custom type upsInfoStartReboot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsInfoStartReboot_Type.__name__ = "DisplayString"
_UpsInfoStartReboot_Object = MibScalar
upsInfoStartReboot = _UpsInfoStartReboot_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 2, 25, 3),
    _UpsInfoStartReboot_Type()
)
upsInfoStartReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInfoStartReboot.setStatus("current")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3)
)
_UpsBatteryCharge_ObjectIdentity = ObjectIdentity
upsBatteryCharge = _UpsBatteryCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 1)
)
_UpsBatteryChargeValue_Type = Float
_UpsBatteryChargeValue_Object = MibScalar
upsBatteryChargeValue = _UpsBatteryChargeValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 1, 1),
    _UpsBatteryChargeValue_Type()
)
upsBatteryChargeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryChargeValue.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryChargeValue.setUnits("Percent")
_UpsBatteryChargeLow_Type = Float
_UpsBatteryChargeLow_Object = MibScalar
upsBatteryChargeLow = _UpsBatteryChargeLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 1, 2),
    _UpsBatteryChargeLow_Type()
)
upsBatteryChargeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryChargeLow.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryChargeLow.setUnits("Percent")
_UpsBatteryChargeRestart_Type = Float
_UpsBatteryChargeRestart_Object = MibScalar
upsBatteryChargeRestart = _UpsBatteryChargeRestart_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 1, 3),
    _UpsBatteryChargeRestart_Type()
)
upsBatteryChargeRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryChargeRestart.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryChargeRestart.setUnits("Percent")
_UpsBatteryChargeWarning_Type = Float
_UpsBatteryChargeWarning_Object = MibScalar
upsBatteryChargeWarning = _UpsBatteryChargeWarning_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 1, 4),
    _UpsBatteryChargeWarning_Type()
)
upsBatteryChargeWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryChargeWarning.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryChargeWarning.setUnits("Percent")
_UpsBatteryVoltage_ObjectIdentity = ObjectIdentity
upsBatteryVoltage = _UpsBatteryVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 2)
)
_UpsBatteryVoltageValue_Type = Float
_UpsBatteryVoltageValue_Object = MibScalar
upsBatteryVoltageValue = _UpsBatteryVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 2, 1),
    _UpsBatteryVoltageValue_Type()
)
upsBatteryVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltageValue.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltageValue.setUnits("Volt DC")
_UpsBatteryVoltageNominal_Type = Float
_UpsBatteryVoltageNominal_Object = MibScalar
upsBatteryVoltageNominal = _UpsBatteryVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 2, 2),
    _UpsBatteryVoltageNominal_Type()
)
upsBatteryVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltageNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltageNominal.setUnits("Volt DC")
_UpsBatteryVoltageLow_Type = Float
_UpsBatteryVoltageLow_Object = MibScalar
upsBatteryVoltageLow = _UpsBatteryVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 2, 3),
    _UpsBatteryVoltageLow_Type()
)
upsBatteryVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltageLow.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltageLow.setUnits("Volt DC")
_UpsBatteryVoltageHigh_Type = Float
_UpsBatteryVoltageHigh_Object = MibScalar
upsBatteryVoltageHigh = _UpsBatteryVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 2, 4),
    _UpsBatteryVoltageHigh_Type()
)
upsBatteryVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltageHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltageHigh.setUnits("Volt DC")
_UpsBatteryCapacity_Type = Float
_UpsBatteryCapacity_Object = MibScalar
upsBatteryCapacity = _UpsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 3),
    _UpsBatteryCapacity_Type()
)
upsBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCapacity.setUnits("A")
_UpsBatteryCurrent_Type = Float
_UpsBatteryCurrent_Object = MibScalar
upsBatteryCurrent = _UpsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 4),
    _UpsBatteryCurrent_Type()
)
upsBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrent.setUnits("Amp DC")
_UpsBatteryTemperature_Type = Float
_UpsBatteryTemperature_Object = MibScalar
upsBatteryTemperature = _UpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 5),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setUnits("degrees Centigrade")
_UpsBatteryRuntime_ObjectIdentity = ObjectIdentity
upsBatteryRuntime = _UpsBatteryRuntime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 6)
)
_UpsBatteryRuntimeValue_Type = NonNegativeInteger
_UpsBatteryRuntimeValue_Object = MibScalar
upsBatteryRuntimeValue = _UpsBatteryRuntimeValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 6, 1),
    _UpsBatteryRuntimeValue_Type()
)
upsBatteryRuntimeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRuntimeValue.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRuntimeValue.setUnits("Seconds")
_UpsBatteryRuntimeLow_Type = NonNegativeInteger
_UpsBatteryRuntimeLow_Object = MibScalar
upsBatteryRuntimeLow = _UpsBatteryRuntimeLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 6, 2),
    _UpsBatteryRuntimeLow_Type()
)
upsBatteryRuntimeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRuntimeLow.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRuntimeLow.setUnits("Seconds")
_UpsBatteryRuntimeRestart_Type = NonNegativeInteger
_UpsBatteryRuntimeRestart_Object = MibScalar
upsBatteryRuntimeRestart = _UpsBatteryRuntimeRestart_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 6, 3),
    _UpsBatteryRuntimeRestart_Type()
)
upsBatteryRuntimeRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRuntimeRestart.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRuntimeRestart.setUnits("Seconds")


class _UpsBatteryAlarmThreshold_Type(DisplayString):
    """Custom type upsBatteryAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsBatteryAlarmThreshold_Type.__name__ = "DisplayString"
_UpsBatteryAlarmThreshold_Object = MibScalar
upsBatteryAlarmThreshold = _UpsBatteryAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 7),
    _UpsBatteryAlarmThreshold_Type()
)
upsBatteryAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryAlarmThreshold.setStatus("current")


class _UpsBatteryDate_Type(DisplayString):
    """Custom type upsBatteryDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsBatteryDate_Type.__name__ = "DisplayString"
_UpsBatteryDate_Object = MibScalar
upsBatteryDate = _UpsBatteryDate_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 8),
    _UpsBatteryDate_Type()
)
upsBatteryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryDate.setStatus("current")


class _UpsBatteryMfrDate_Type(DisplayString):
    """Custom type upsBatteryMfrDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsBatteryMfrDate_Type.__name__ = "DisplayString"
_UpsBatteryMfrDate_Object = MibScalar
upsBatteryMfrDate = _UpsBatteryMfrDate_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 9),
    _UpsBatteryMfrDate_Type()
)
upsBatteryMfrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryMfrDate.setStatus("current")
_UpsBatteryPacks_Type = NonNegativeInteger
_UpsBatteryPacks_Object = MibScalar
upsBatteryPacks = _UpsBatteryPacks_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 10),
    _UpsBatteryPacks_Type()
)
upsBatteryPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryPacks.setStatus("current")
_UpsBatteryPacksBad_Type = NonNegativeInteger
_UpsBatteryPacksBad_Object = MibScalar
upsBatteryPacksBad = _UpsBatteryPacksBad_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 11),
    _UpsBatteryPacksBad_Type()
)
upsBatteryPacksBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryPacksBad.setStatus("current")


class _UpsBatteryType_Type(DisplayString):
    """Custom type upsBatteryType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsBatteryType_Type.__name__ = "DisplayString"
_UpsBatteryType_Object = MibScalar
upsBatteryType = _UpsBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 12),
    _UpsBatteryType_Type()
)
upsBatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryType.setStatus("current")


class _UpsBatteryProtection_Type(DisplayString):
    """Custom type upsBatteryProtection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsBatteryProtection_Type.__name__ = "DisplayString"
_UpsBatteryProtection_Object = MibScalar
upsBatteryProtection = _UpsBatteryProtection_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 13),
    _UpsBatteryProtection_Type()
)
upsBatteryProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryProtection.setStatus("current")


class _UpsBatteryEnergySave_Type(DisplayString):
    """Custom type upsBatteryEnergySave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsBatteryEnergySave_Type.__name__ = "DisplayString"
_UpsBatteryEnergySave_Object = MibScalar
upsBatteryEnergySave = _UpsBatteryEnergySave_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 3, 14),
    _UpsBatteryEnergySave_Type()
)
upsBatteryEnergySave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryEnergySave.setStatus("current")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4)
)
_UpsInputVoltage_ObjectIdentity = ObjectIdentity
upsInputVoltage = _UpsInputVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 1)
)
_UpsInputVoltageValue_Type = Float
_UpsInputVoltageValue_Object = MibScalar
upsInputVoltageValue = _UpsInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 1, 1),
    _UpsInputVoltageValue_Type()
)
upsInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageValue.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageValue.setUnits("Volts")
_UpsInputVoltageMax_Type = Float
_UpsInputVoltageMax_Object = MibScalar
upsInputVoltageMax = _UpsInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 1, 2),
    _UpsInputVoltageMax_Type()
)
upsInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMax.setUnits("Volts")
_UpsInputVoltageMin_Type = Float
_UpsInputVoltageMin_Object = MibScalar
upsInputVoltageMin = _UpsInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 1, 3),
    _UpsInputVoltageMin_Type()
)
upsInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMin.setUnits("Volts")
_UpsInputVoltageNominal_Type = Float
_UpsInputVoltageNominal_Object = MibScalar
upsInputVoltageNominal = _UpsInputVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 1, 4),
    _UpsInputVoltageNominal_Type()
)
upsInputVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageNominal.setUnits("Volts")


class _UpsInputVoltageExtend_Type(DisplayString):
    """Custom type upsInputVoltageExtend based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsInputVoltageExtend_Type.__name__ = "DisplayString"
_UpsInputVoltageExtend_Object = MibScalar
upsInputVoltageExtend = _UpsInputVoltageExtend_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 1, 5),
    _UpsInputVoltageExtend_Type()
)
upsInputVoltageExtend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageExtend.setStatus("current")
_UpsInputVoltageFault_Type = Float
_UpsInputVoltageFault_Object = MibScalar
upsInputVoltageFault = _UpsInputVoltageFault_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 1, 6),
    _UpsInputVoltageFault_Type()
)
upsInputVoltageFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageFault.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageFault.setUnits("Volts")
_UpsInputTransfer_ObjectIdentity = ObjectIdentity
upsInputTransfer = _UpsInputTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2)
)


class _UpsInputTransferReason_Type(DisplayString):
    """Custom type upsInputTransferReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsInputTransferReason_Type.__name__ = "DisplayString"
_UpsInputTransferReason_Object = MibScalar
upsInputTransferReason = _UpsInputTransferReason_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 1),
    _UpsInputTransferReason_Type()
)
upsInputTransferReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferReason.setStatus("current")
_UpsInputTransferLow_Type = Float
_UpsInputTransferLow_Object = MibScalar
upsInputTransferLow = _UpsInputTransferLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 2),
    _UpsInputTransferLow_Type()
)
upsInputTransferLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferLow.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferLow.setUnits("Volts")
_UpsInputTransferHigh_Type = Float
_UpsInputTransferHigh_Object = MibScalar
upsInputTransferHigh = _UpsInputTransferHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 3),
    _UpsInputTransferHigh_Type()
)
upsInputTransferHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferHigh.setUnits("Volts")
_UpsInputTransferLowMin_Type = Float
_UpsInputTransferLowMin_Object = MibScalar
upsInputTransferLowMin = _UpsInputTransferLowMin_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 4),
    _UpsInputTransferLowMin_Type()
)
upsInputTransferLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferLowMin.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferLowMin.setUnits("Volts")
_UpsInputTransferLowMax_Type = Float
_UpsInputTransferLowMax_Object = MibScalar
upsInputTransferLowMax = _UpsInputTransferLowMax_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 5),
    _UpsInputTransferLowMax_Type()
)
upsInputTransferLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferLowMax.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferLowMax.setUnits("Volts")
_UpsInputTransferHighMin_Type = Float
_UpsInputTransferHighMin_Object = MibScalar
upsInputTransferHighMin = _UpsInputTransferHighMin_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 6),
    _UpsInputTransferHighMin_Type()
)
upsInputTransferHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferHighMin.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferHighMin.setUnits("Volts")
_UpsInputTransferHighMax_Type = Float
_UpsInputTransferHighMax_Object = MibScalar
upsInputTransferHighMax = _UpsInputTransferHighMax_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 7),
    _UpsInputTransferHighMax_Type()
)
upsInputTransferHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferHighMax.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferHighMax.setUnits("Volts")
_UpsInputTransferBoostLow_Type = Float
_UpsInputTransferBoostLow_Object = MibScalar
upsInputTransferBoostLow = _UpsInputTransferBoostLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 8),
    _UpsInputTransferBoostLow_Type()
)
upsInputTransferBoostLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferBoostLow.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferBoostLow.setUnits("Volts")
_UpsInputTransferBoostHigh_Type = Float
_UpsInputTransferBoostHigh_Object = MibScalar
upsInputTransferBoostHigh = _UpsInputTransferBoostHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 9),
    _UpsInputTransferBoostHigh_Type()
)
upsInputTransferBoostHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferBoostHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferBoostHigh.setUnits("Volts")
_UpsInputTransferTrimLow_Type = Float
_UpsInputTransferTrimLow_Object = MibScalar
upsInputTransferTrimLow = _UpsInputTransferTrimLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 10),
    _UpsInputTransferTrimLow_Type()
)
upsInputTransferTrimLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferTrimLow.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferTrimLow.setUnits("Volts")
_UpsInputTransferTrimHigh_Type = Float
_UpsInputTransferTrimHigh_Object = MibScalar
upsInputTransferTrimHigh = _UpsInputTransferTrimHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 2, 11),
    _UpsInputTransferTrimHigh_Type()
)
upsInputTransferTrimHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTransferTrimHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTransferTrimHigh.setUnits("Volts")


class _UpsInputSensitivity_Type(DisplayString):
    """Custom type upsInputSensitivity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsInputSensitivity_Type.__name__ = "DisplayString"
_UpsInputSensitivity_Object = MibScalar
upsInputSensitivity = _UpsInputSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 3),
    _UpsInputSensitivity_Type()
)
upsInputSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputSensitivity.setStatus("current")


class _UpsInputQuality_Type(DisplayString):
    """Custom type upsInputQuality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsInputQuality_Type.__name__ = "DisplayString"
_UpsInputQuality_Object = MibScalar
upsInputQuality = _UpsInputQuality_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 4),
    _UpsInputQuality_Type()
)
upsInputQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputQuality.setStatus("current")
_UpsInputCurrent_ObjectIdentity = ObjectIdentity
upsInputCurrent = _UpsInputCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 5)
)
_UpsInputCurrentValue_Type = Float
_UpsInputCurrentValue_Object = MibScalar
upsInputCurrentValue = _UpsInputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 5, 1),
    _UpsInputCurrentValue_Type()
)
upsInputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentValue.setUnits("Amp")
_UpsInputCurrentNominal_Type = Float
_UpsInputCurrentNominal_Object = MibScalar
upsInputCurrentNominal = _UpsInputCurrentNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 5, 2),
    _UpsInputCurrentNominal_Type()
)
upsInputCurrentNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentNominal.setUnits("Amp")
_UpsInputFrequency_ObjectIdentity = ObjectIdentity
upsInputFrequency = _UpsInputFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 6)
)
_UpsInputFrequencyValue_Type = Float
_UpsInputFrequencyValue_Object = MibScalar
upsInputFrequencyValue = _UpsInputFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 6, 1),
    _UpsInputFrequencyValue_Type()
)
upsInputFrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyValue.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyValue.setUnits("Hz")
_UpsInputFrequencyNominal_Type = Float
_UpsInputFrequencyNominal_Object = MibScalar
upsInputFrequencyNominal = _UpsInputFrequencyNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 6, 2),
    _UpsInputFrequencyNominal_Type()
)
upsInputFrequencyNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyNominal.setUnits("Hz")
_UpsInputFrequencyLow_Type = Float
_UpsInputFrequencyLow_Object = MibScalar
upsInputFrequencyLow = _UpsInputFrequencyLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 6, 3),
    _UpsInputFrequencyLow_Type()
)
upsInputFrequencyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyLow.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyLow.setUnits("Hz")
_UpsInputFrequencyHigh_Type = Float
_UpsInputFrequencyHigh_Object = MibScalar
upsInputFrequencyHigh = _UpsInputFrequencyHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 6, 4),
    _UpsInputFrequencyHigh_Type()
)
upsInputFrequencyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencyHigh.setUnits("Hz")


class _UpsInputFrequencyExtend_Type(DisplayString):
    """Custom type upsInputFrequencyExtend based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsInputFrequencyExtend_Type.__name__ = "DisplayString"
_UpsInputFrequencyExtend_Object = MibScalar
upsInputFrequencyExtend = _UpsInputFrequencyExtend_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 4, 6, 5),
    _UpsInputFrequencyExtend_Type()
)
upsInputFrequencyExtend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencyExtend.setStatus("current")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5)
)
_UpsOutputVoltage_ObjectIdentity = ObjectIdentity
upsOutputVoltage = _UpsOutputVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 1)
)
_UpsOutputVoltageValue_Type = Float
_UpsOutputVoltageValue_Object = MibScalar
upsOutputVoltageValue = _UpsOutputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 1, 1),
    _UpsOutputVoltageValue_Type()
)
upsOutputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltageValue.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltageValue.setUnits("Volts")
_UpsOutputVoltageNominal_Type = Float
_UpsOutputVoltageNominal_Object = MibScalar
upsOutputVoltageNominal = _UpsOutputVoltageNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 1, 2),
    _UpsOutputVoltageNominal_Type()
)
upsOutputVoltageNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltageNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltageNominal.setUnits("Volts")
_UpsOutputFrequency_ObjectIdentity = ObjectIdentity
upsOutputFrequency = _UpsOutputFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 2)
)
_UpsOutputFrequencyValue_Type = Float
_UpsOutputFrequencyValue_Object = MibScalar
upsOutputFrequencyValue = _UpsOutputFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 2, 1),
    _UpsOutputFrequencyValue_Type()
)
upsOutputFrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencyValue.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencyValue.setUnits("Hz")
_UpsOutputFrequencyNominal_Type = Float
_UpsOutputFrequencyNominal_Object = MibScalar
upsOutputFrequencyNominal = _UpsOutputFrequencyNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 2, 2),
    _UpsOutputFrequencyNominal_Type()
)
upsOutputFrequencyNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencyNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencyNominal.setUnits("Hz")
_UpsOutputCurrent_ObjectIdentity = ObjectIdentity
upsOutputCurrent = _UpsOutputCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 3)
)
_UpsOutputCurrentValue_Type = Float
_UpsOutputCurrentValue_Object = MibScalar
upsOutputCurrentValue = _UpsOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 3, 1),
    _UpsOutputCurrentValue_Type()
)
upsOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentValue.setUnits("Amp")
_UpsOutputCurrentNominal_Type = Float
_UpsOutputCurrentNominal_Object = MibScalar
upsOutputCurrentNominal = _UpsOutputCurrentNominal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 5, 3, 2),
    _UpsOutputCurrentNominal_Type()
)
upsOutputCurrentNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentNominal.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentNominal.setUnits("Amp")
_UpsAmbient_ObjectIdentity = ObjectIdentity
upsAmbient = _UpsAmbient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6)
)
_UpsAmbientTemperature_ObjectIdentity = ObjectIdentity
upsAmbientTemperature = _UpsAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 1)
)
_UpsAmbientTemperatureValue_Type = Float
_UpsAmbientTemperatureValue_Object = MibScalar
upsAmbientTemperatureValue = _UpsAmbientTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 1, 1),
    _UpsAmbientTemperatureValue_Type()
)
upsAmbientTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientTemperatureValue.setUnits("degrees Centigrade")


class _UpsAmbientTemperatureAlarm_Type(DisplayString):
    """Custom type upsAmbientTemperatureAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsAmbientTemperatureAlarm_Type.__name__ = "DisplayString"
_UpsAmbientTemperatureAlarm_Object = MibScalar
upsAmbientTemperatureAlarm = _UpsAmbientTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 1, 2),
    _UpsAmbientTemperatureAlarm_Type()
)
upsAmbientTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientTemperatureAlarm.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientTemperatureAlarm.setUnits("enabled/disabled")
_UpsAmbientTemperatureHigh_Type = Float
_UpsAmbientTemperatureHigh_Object = MibScalar
upsAmbientTemperatureHigh = _UpsAmbientTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 1, 3),
    _UpsAmbientTemperatureHigh_Type()
)
upsAmbientTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientTemperatureHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientTemperatureHigh.setUnits("degrees Centigrade")
_UpsAmbientTemperatureLow_Type = Float
_UpsAmbientTemperatureLow_Object = MibScalar
upsAmbientTemperatureLow = _UpsAmbientTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 1, 4),
    _UpsAmbientTemperatureLow_Type()
)
upsAmbientTemperatureLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientTemperatureLow.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientTemperatureLow.setUnits("degrees Centigrade")
_UpsAmbientTemperatureMax_Type = Float
_UpsAmbientTemperatureMax_Object = MibScalar
upsAmbientTemperatureMax = _UpsAmbientTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 1, 5),
    _UpsAmbientTemperatureMax_Type()
)
upsAmbientTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientTemperatureMax.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientTemperatureMax.setUnits("degrees Centigrade")
_UpsAmbientTemperatureMin_Type = Float
_UpsAmbientTemperatureMin_Object = MibScalar
upsAmbientTemperatureMin = _UpsAmbientTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 1, 6),
    _UpsAmbientTemperatureMin_Type()
)
upsAmbientTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientTemperatureMin.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientTemperatureMin.setUnits("degrees Centigrade")
_UpsAmbientHumidity_ObjectIdentity = ObjectIdentity
upsAmbientHumidity = _UpsAmbientHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 2)
)
_UpsAmbientHumidityValue_Type = Float
_UpsAmbientHumidityValue_Object = MibScalar
upsAmbientHumidityValue = _UpsAmbientHumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 2, 1),
    _UpsAmbientHumidityValue_Type()
)
upsAmbientHumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientHumidityValue.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientHumidityValue.setUnits("percent")


class _UpsAmbientHumidityAlarm_Type(DisplayString):
    """Custom type upsAmbientHumidityAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsAmbientHumidityAlarm_Type.__name__ = "DisplayString"
_UpsAmbientHumidityAlarm_Object = MibScalar
upsAmbientHumidityAlarm = _UpsAmbientHumidityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 2, 2),
    _UpsAmbientHumidityAlarm_Type()
)
upsAmbientHumidityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientHumidityAlarm.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientHumidityAlarm.setUnits("enabled/disabled")
_UpsAmbientHumidityHigh_Type = Float
_UpsAmbientHumidityHigh_Object = MibScalar
upsAmbientHumidityHigh = _UpsAmbientHumidityHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 2, 3),
    _UpsAmbientHumidityHigh_Type()
)
upsAmbientHumidityHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientHumidityHigh.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientHumidityHigh.setUnits("percent")
_UpsAmbientHumidityLow_Type = Float
_UpsAmbientHumidityLow_Object = MibScalar
upsAmbientHumidityLow = _UpsAmbientHumidityLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 2, 4),
    _UpsAmbientHumidityLow_Type()
)
upsAmbientHumidityLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientHumidityLow.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientHumidityLow.setUnits("percent")
_UpsAmbientHumidityMax_Type = Float
_UpsAmbientHumidityMax_Object = MibScalar
upsAmbientHumidityMax = _UpsAmbientHumidityMax_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 2, 5),
    _UpsAmbientHumidityMax_Type()
)
upsAmbientHumidityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientHumidityMax.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientHumidityMax.setUnits("percent")
_UpsAmbientHumidityMin_Type = Float
_UpsAmbientHumidityMin_Object = MibScalar
upsAmbientHumidityMin = _UpsAmbientHumidityMin_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 6, 2, 6),
    _UpsAmbientHumidityMin_Type()
)
upsAmbientHumidityMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAmbientHumidityMin.setStatus("current")
if mibBuilder.loadTexts:
    upsAmbientHumidityMin.setUnits("percent")
_UpsDriver_ObjectIdentity = ObjectIdentity
upsDriver = _UpsDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7)
)


class _UpsDriverName_Type(DisplayString):
    """Custom type upsDriverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDriverName_Type.__name__ = "DisplayString"
_UpsDriverName_Object = MibScalar
upsDriverName = _UpsDriverName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 1),
    _UpsDriverName_Type()
)
upsDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverName.setStatus("current")


class _UpsDriverVersion_Type(DisplayString):
    """Custom type upsDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDriverVersion_Type.__name__ = "DisplayString"
_UpsDriverVersion_Object = MibScalar
upsDriverVersion = _UpsDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 2),
    _UpsDriverVersion_Type()
)
upsDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverVersion.setStatus("current")


class _UpsDriverVersionData_Type(DisplayString):
    """Custom type upsDriverVersionData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDriverVersionData_Type.__name__ = "DisplayString"
_UpsDriverVersionData_Object = MibScalar
upsDriverVersionData = _UpsDriverVersionData_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 3),
    _UpsDriverVersionData_Type()
)
upsDriverVersionData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverVersionData.setStatus("current")


class _UpsDriverVersionInternal_Type(DisplayString):
    """Custom type upsDriverVersionInternal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDriverVersionInternal_Type.__name__ = "DisplayString"
_UpsDriverVersionInternal_Object = MibScalar
upsDriverVersionInternal = _UpsDriverVersionInternal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 4),
    _UpsDriverVersionInternal_Type()
)
upsDriverVersionInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverVersionInternal.setStatus("current")
_UpsDriverPollInterval_Type = Integer32
_UpsDriverPollInterval_Object = MibScalar
upsDriverPollInterval = _UpsDriverPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 5),
    _UpsDriverPollInterval_Type()
)
upsDriverPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    upsDriverPollInterval.setUnits("second")


class _UpsDriverPort_Type(DisplayString):
    """Custom type upsDriverPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDriverPort_Type.__name__ = "DisplayString"
_UpsDriverPort_Object = MibScalar
upsDriverPort = _UpsDriverPort_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 6),
    _UpsDriverPort_Type()
)
upsDriverPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverPort.setStatus("current")
_UpsDriverPollFrequency_Type = Integer32
_UpsDriverPollFrequency_Object = MibScalar
upsDriverPollFrequency = _UpsDriverPollFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 7),
    _UpsDriverPollFrequency_Type()
)
upsDriverPollFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverPollFrequency.setStatus("current")


class _UpsDriverProductID_Type(DisplayString):
    """Custom type upsDriverProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDriverProductID_Type.__name__ = "DisplayString"
_UpsDriverProductID_Object = MibScalar
upsDriverProductID = _UpsDriverProductID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 8),
    _UpsDriverProductID_Type()
)
upsDriverProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverProductID.setStatus("current")


class _UpsDriverSnmpVersion_Type(DisplayString):
    """Custom type upsDriverSnmpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsDriverSnmpVersion_Type.__name__ = "DisplayString"
_UpsDriverSnmpVersion_Object = MibScalar
upsDriverSnmpVersion = _UpsDriverSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 7, 9),
    _UpsDriverSnmpVersion_Type()
)
upsDriverSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDriverSnmpVersion.setStatus("current")
_UpsServer_ObjectIdentity = ObjectIdentity
upsServer = _UpsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 8)
)


class _UpsServerInfo_Type(DisplayString):
    """Custom type upsServerInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsServerInfo_Type.__name__ = "DisplayString"
_UpsServerInfo_Object = MibScalar
upsServerInfo = _UpsServerInfo_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 8, 1),
    _UpsServerInfo_Type()
)
upsServerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsServerInfo.setStatus("current")


class _UpsServerVersion_Type(DisplayString):
    """Custom type upsServerVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsServerVersion_Type.__name__ = "DisplayString"
_UpsServerVersion_Object = MibScalar
upsServerVersion = _UpsServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6574, 4, 8, 2),
    _UpsServerVersion_Type()
)
upsServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsServerVersion.setStatus("current")
_UpsConformance_ObjectIdentity = ObjectIdentity
upsConformance = _UpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 9)
)
_UpsCompliances_ObjectIdentity = ObjectIdentity
upsCompliances = _UpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 9, 1)
)
_UpsGroups_ObjectIdentity = ObjectIdentity
upsGroups = _UpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 4, 9, 2)
)

# Managed Objects groups

upsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 4, 9, 2, 1)
)
upsGroup.setObjects(
      *(("SYNOLOGY-UPS-MIB", "upsDeviceModel"),
        ("SYNOLOGY-UPS-MIB", "upsDeviceManufacturer"),
        ("SYNOLOGY-UPS-MIB", "upsDeviceSerial"),
        ("SYNOLOGY-UPS-MIB", "upsDeviceType"),
        ("SYNOLOGY-UPS-MIB", "upsDeviceDescription"),
        ("SYNOLOGY-UPS-MIB", "upsDeviceContact"),
        ("SYNOLOGY-UPS-MIB", "upsDeviceLocation"),
        ("SYNOLOGY-UPS-MIB", "upsDevicePart"),
        ("SYNOLOGY-UPS-MIB", "upsDeviceMACAddr"),
        ("SYNOLOGY-UPS-MIB", "upsInfoStatus"),
        ("SYNOLOGY-UPS-MIB", "upsInfoAlarm"),
        ("SYNOLOGY-UPS-MIB", "upsInfoTime"),
        ("SYNOLOGY-UPS-MIB", "upsInfoDate"),
        ("SYNOLOGY-UPS-MIB", "upsInfoModel"),
        ("SYNOLOGY-UPS-MIB", "upsInfoMfrName"),
        ("SYNOLOGY-UPS-MIB", "upsInfoMfrDate"),
        ("SYNOLOGY-UPS-MIB", "upsInfoSerial"),
        ("SYNOLOGY-UPS-MIB", "upsInfoVendorID"),
        ("SYNOLOGY-UPS-MIB", "upsInfoProductID"),
        ("SYNOLOGY-UPS-MIB", "upsInfoFirmwareName"),
        ("SYNOLOGY-UPS-MIB", "upsInfoFirmwareAux"),
        ("SYNOLOGY-UPS-MIB", "upsInfoTemperature"),
        ("SYNOLOGY-UPS-MIB", "upsInfoLoadValue"),
        ("SYNOLOGY-UPS-MIB", "upsInfoLoadHigh"),
        ("SYNOLOGY-UPS-MIB", "upsInfoID"),
        ("SYNOLOGY-UPS-MIB", "upsInfoDelayStart"),
        ("SYNOLOGY-UPS-MIB", "upsInfoDelayReboot"),
        ("SYNOLOGY-UPS-MIB", "upsInfoDelayShutdown"),
        ("SYNOLOGY-UPS-MIB", "upsInfoTimerStart"),
        ("SYNOLOGY-UPS-MIB", "upsInfoTimerReboot"),
        ("SYNOLOGY-UPS-MIB", "upsInfoTimerShutdown"),
        ("SYNOLOGY-UPS-MIB", "upsInfoTestInterval"),
        ("SYNOLOGY-UPS-MIB", "upsInfoTestResult"),
        ("SYNOLOGY-UPS-MIB", "upsInfoDisplayLanguage"),
        ("SYNOLOGY-UPS-MIB", "upsInfoContacts"),
        ("SYNOLOGY-UPS-MIB", "upsInfoEffciency"),
        ("SYNOLOGY-UPS-MIB", "upsInfoPowerValue"),
        ("SYNOLOGY-UPS-MIB", "upsInfoPowerNominal"),
        ("SYNOLOGY-UPS-MIB", "upsInfoRealPowerValue"),
        ("SYNOLOGY-UPS-MIB", "upsInfoRealPowerNominal"),
        ("SYNOLOGY-UPS-MIB", "upsInfoBeeperStatus"),
        ("SYNOLOGY-UPS-MIB", "upsInfoType"),
        ("SYNOLOGY-UPS-MIB", "upsInfoWatchdogStatus"),
        ("SYNOLOGY-UPS-MIB", "upsInfoStartAuto"),
        ("SYNOLOGY-UPS-MIB", "upsInfoStartBattery"),
        ("SYNOLOGY-UPS-MIB", "upsInfoStartReboot"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryChargeValue"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryChargeLow"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryChargeRestart"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryChargeWarning"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryVoltageValue"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryVoltageNominal"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryVoltageLow"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryVoltageHigh"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryCapacity"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryCurrent"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryTemperature"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryRuntimeValue"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryRuntimeLow"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryRuntimeRestart"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryAlarmThreshold"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryDate"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryMfrDate"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryPacks"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryPacksBad"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryType"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryProtection"),
        ("SYNOLOGY-UPS-MIB", "upsBatteryEnergySave"),
        ("SYNOLOGY-UPS-MIB", "upsInputVoltageValue"),
        ("SYNOLOGY-UPS-MIB", "upsInputVoltageMax"),
        ("SYNOLOGY-UPS-MIB", "upsInputVoltageMin"),
        ("SYNOLOGY-UPS-MIB", "upsInputVoltageNominal"),
        ("SYNOLOGY-UPS-MIB", "upsInputVoltageExtend"),
        ("SYNOLOGY-UPS-MIB", "upsInputVoltageFault"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferReason"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferLow"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferHigh"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferLowMin"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferLowMax"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferHighMin"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferHighMax"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferBoostLow"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferBoostHigh"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferTrimLow"),
        ("SYNOLOGY-UPS-MIB", "upsInputTransferTrimHigh"),
        ("SYNOLOGY-UPS-MIB", "upsInputSensitivity"),
        ("SYNOLOGY-UPS-MIB", "upsInputQuality"),
        ("SYNOLOGY-UPS-MIB", "upsInputCurrentValue"),
        ("SYNOLOGY-UPS-MIB", "upsInputCurrentNominal"),
        ("SYNOLOGY-UPS-MIB", "upsInputFrequencyValue"),
        ("SYNOLOGY-UPS-MIB", "upsInputFrequencyNominal"),
        ("SYNOLOGY-UPS-MIB", "upsInputFrequencyLow"),
        ("SYNOLOGY-UPS-MIB", "upsInputFrequencyHigh"),
        ("SYNOLOGY-UPS-MIB", "upsInputFrequencyExtend"),
        ("SYNOLOGY-UPS-MIB", "upsOutputVoltageValue"),
        ("SYNOLOGY-UPS-MIB", "upsOutputVoltageNominal"),
        ("SYNOLOGY-UPS-MIB", "upsOutputFrequencyValue"),
        ("SYNOLOGY-UPS-MIB", "upsOutputFrequencyNominal"),
        ("SYNOLOGY-UPS-MIB", "upsOutputCurrentValue"),
        ("SYNOLOGY-UPS-MIB", "upsOutputCurrentNominal"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientTemperatureValue"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientTemperatureAlarm"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientTemperatureHigh"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientTemperatureLow"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientTemperatureMax"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientTemperatureMin"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientHumidityValue"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientHumidityAlarm"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientHumidityHigh"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientHumidityLow"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientHumidityMax"),
        ("SYNOLOGY-UPS-MIB", "upsAmbientHumidityMin"),
        ("SYNOLOGY-UPS-MIB", "upsDriverName"),
        ("SYNOLOGY-UPS-MIB", "upsDriverVersion"),
        ("SYNOLOGY-UPS-MIB", "upsDriverVersionData"),
        ("SYNOLOGY-UPS-MIB", "upsDriverVersionInternal"),
        ("SYNOLOGY-UPS-MIB", "upsDriverPollInterval"),
        ("SYNOLOGY-UPS-MIB", "upsDriverPort"),
        ("SYNOLOGY-UPS-MIB", "upsDriverPollFrequency"),
        ("SYNOLOGY-UPS-MIB", "upsDriverProductID"),
        ("SYNOLOGY-UPS-MIB", "upsDriverSnmpVersion"),
        ("SYNOLOGY-UPS-MIB", "upsServerInfo"),
        ("SYNOLOGY-UPS-MIB", "upsServerVersion"))
)
if mibBuilder.loadTexts:
    upsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

upsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 4, 9, 1, 1)
)
if mibBuilder.loadTexts:
    upsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-UPS-MIB",
    **{"NonNegativeInteger": NonNegativeInteger,
       "synology": synology,
       "synoUPS": synoUPS,
       "upsDevice": upsDevice,
       "upsDeviceModel": upsDeviceModel,
       "upsDeviceManufacturer": upsDeviceManufacturer,
       "upsDeviceSerial": upsDeviceSerial,
       "upsDeviceType": upsDeviceType,
       "upsDeviceDescription": upsDeviceDescription,
       "upsDeviceContact": upsDeviceContact,
       "upsDeviceLocation": upsDeviceLocation,
       "upsDevicePart": upsDevicePart,
       "upsDeviceMACAddr": upsDeviceMACAddr,
       "upsInfo": upsInfo,
       "upsInfoStatus": upsInfoStatus,
       "upsInfoAlarm": upsInfoAlarm,
       "upsInfoTime": upsInfoTime,
       "upsInfoDate": upsInfoDate,
       "upsInfoModel": upsInfoModel,
       "upsInfoMfr": upsInfoMfr,
       "upsInfoMfrName": upsInfoMfrName,
       "upsInfoMfrDate": upsInfoMfrDate,
       "upsInfoSerial": upsInfoSerial,
       "upsInfoVendorID": upsInfoVendorID,
       "upsInfoProductID": upsInfoProductID,
       "upsInfoFirmware": upsInfoFirmware,
       "upsInfoFirmwareName": upsInfoFirmwareName,
       "upsInfoFirmwareAux": upsInfoFirmwareAux,
       "upsInfoTemperature": upsInfoTemperature,
       "upsInfoLoad": upsInfoLoad,
       "upsInfoLoadValue": upsInfoLoadValue,
       "upsInfoLoadHigh": upsInfoLoadHigh,
       "upsInfoID": upsInfoID,
       "upsInfoDelay": upsInfoDelay,
       "upsInfoDelayStart": upsInfoDelayStart,
       "upsInfoDelayReboot": upsInfoDelayReboot,
       "upsInfoDelayShutdown": upsInfoDelayShutdown,
       "upsInfoTimer": upsInfoTimer,
       "upsInfoTimerStart": upsInfoTimerStart,
       "upsInfoTimerReboot": upsInfoTimerReboot,
       "upsInfoTimerShutdown": upsInfoTimerShutdown,
       "upsInfoTest": upsInfoTest,
       "upsInfoTestInterval": upsInfoTestInterval,
       "upsInfoTestResult": upsInfoTestResult,
       "upsInfoDisplayLanguage": upsInfoDisplayLanguage,
       "upsInfoContacts": upsInfoContacts,
       "upsInfoEffciency": upsInfoEffciency,
       "upsInfoPower": upsInfoPower,
       "upsInfoPowerValue": upsInfoPowerValue,
       "upsInfoPowerNominal": upsInfoPowerNominal,
       "upsInfoRealPower": upsInfoRealPower,
       "upsInfoRealPowerValue": upsInfoRealPowerValue,
       "upsInfoRealPowerNominal": upsInfoRealPowerNominal,
       "upsInfoBeeperStatus": upsInfoBeeperStatus,
       "upsInfoType": upsInfoType,
       "upsInfoWatchdogStatus": upsInfoWatchdogStatus,
       "upsInfoStart": upsInfoStart,
       "upsInfoStartAuto": upsInfoStartAuto,
       "upsInfoStartBattery": upsInfoStartBattery,
       "upsInfoStartReboot": upsInfoStartReboot,
       "upsBattery": upsBattery,
       "upsBatteryCharge": upsBatteryCharge,
       "upsBatteryChargeValue": upsBatteryChargeValue,
       "upsBatteryChargeLow": upsBatteryChargeLow,
       "upsBatteryChargeRestart": upsBatteryChargeRestart,
       "upsBatteryChargeWarning": upsBatteryChargeWarning,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryVoltageValue": upsBatteryVoltageValue,
       "upsBatteryVoltageNominal": upsBatteryVoltageNominal,
       "upsBatteryVoltageLow": upsBatteryVoltageLow,
       "upsBatteryVoltageHigh": upsBatteryVoltageHigh,
       "upsBatteryCapacity": upsBatteryCapacity,
       "upsBatteryCurrent": upsBatteryCurrent,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsBatteryRuntime": upsBatteryRuntime,
       "upsBatteryRuntimeValue": upsBatteryRuntimeValue,
       "upsBatteryRuntimeLow": upsBatteryRuntimeLow,
       "upsBatteryRuntimeRestart": upsBatteryRuntimeRestart,
       "upsBatteryAlarmThreshold": upsBatteryAlarmThreshold,
       "upsBatteryDate": upsBatteryDate,
       "upsBatteryMfrDate": upsBatteryMfrDate,
       "upsBatteryPacks": upsBatteryPacks,
       "upsBatteryPacksBad": upsBatteryPacksBad,
       "upsBatteryType": upsBatteryType,
       "upsBatteryProtection": upsBatteryProtection,
       "upsBatteryEnergySave": upsBatteryEnergySave,
       "upsInput": upsInput,
       "upsInputVoltage": upsInputVoltage,
       "upsInputVoltageValue": upsInputVoltageValue,
       "upsInputVoltageMax": upsInputVoltageMax,
       "upsInputVoltageMin": upsInputVoltageMin,
       "upsInputVoltageNominal": upsInputVoltageNominal,
       "upsInputVoltageExtend": upsInputVoltageExtend,
       "upsInputVoltageFault": upsInputVoltageFault,
       "upsInputTransfer": upsInputTransfer,
       "upsInputTransferReason": upsInputTransferReason,
       "upsInputTransferLow": upsInputTransferLow,
       "upsInputTransferHigh": upsInputTransferHigh,
       "upsInputTransferLowMin": upsInputTransferLowMin,
       "upsInputTransferLowMax": upsInputTransferLowMax,
       "upsInputTransferHighMin": upsInputTransferHighMin,
       "upsInputTransferHighMax": upsInputTransferHighMax,
       "upsInputTransferBoostLow": upsInputTransferBoostLow,
       "upsInputTransferBoostHigh": upsInputTransferBoostHigh,
       "upsInputTransferTrimLow": upsInputTransferTrimLow,
       "upsInputTransferTrimHigh": upsInputTransferTrimHigh,
       "upsInputSensitivity": upsInputSensitivity,
       "upsInputQuality": upsInputQuality,
       "upsInputCurrent": upsInputCurrent,
       "upsInputCurrentValue": upsInputCurrentValue,
       "upsInputCurrentNominal": upsInputCurrentNominal,
       "upsInputFrequency": upsInputFrequency,
       "upsInputFrequencyValue": upsInputFrequencyValue,
       "upsInputFrequencyNominal": upsInputFrequencyNominal,
       "upsInputFrequencyLow": upsInputFrequencyLow,
       "upsInputFrequencyHigh": upsInputFrequencyHigh,
       "upsInputFrequencyExtend": upsInputFrequencyExtend,
       "upsOutput": upsOutput,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputVoltageValue": upsOutputVoltageValue,
       "upsOutputVoltageNominal": upsOutputVoltageNominal,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputFrequencyValue": upsOutputFrequencyValue,
       "upsOutputFrequencyNominal": upsOutputFrequencyNominal,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputCurrentValue": upsOutputCurrentValue,
       "upsOutputCurrentNominal": upsOutputCurrentNominal,
       "upsAmbient": upsAmbient,
       "upsAmbientTemperature": upsAmbientTemperature,
       "upsAmbientTemperatureValue": upsAmbientTemperatureValue,
       "upsAmbientTemperatureAlarm": upsAmbientTemperatureAlarm,
       "upsAmbientTemperatureHigh": upsAmbientTemperatureHigh,
       "upsAmbientTemperatureLow": upsAmbientTemperatureLow,
       "upsAmbientTemperatureMax": upsAmbientTemperatureMax,
       "upsAmbientTemperatureMin": upsAmbientTemperatureMin,
       "upsAmbientHumidity": upsAmbientHumidity,
       "upsAmbientHumidityValue": upsAmbientHumidityValue,
       "upsAmbientHumidityAlarm": upsAmbientHumidityAlarm,
       "upsAmbientHumidityHigh": upsAmbientHumidityHigh,
       "upsAmbientHumidityLow": upsAmbientHumidityLow,
       "upsAmbientHumidityMax": upsAmbientHumidityMax,
       "upsAmbientHumidityMin": upsAmbientHumidityMin,
       "upsDriver": upsDriver,
       "upsDriverName": upsDriverName,
       "upsDriverVersion": upsDriverVersion,
       "upsDriverVersionData": upsDriverVersionData,
       "upsDriverVersionInternal": upsDriverVersionInternal,
       "upsDriverPollInterval": upsDriverPollInterval,
       "upsDriverPort": upsDriverPort,
       "upsDriverPollFrequency": upsDriverPollFrequency,
       "upsDriverProductID": upsDriverProductID,
       "upsDriverSnmpVersion": upsDriverSnmpVersion,
       "upsServer": upsServer,
       "upsServerInfo": upsServerInfo,
       "upsServerVersion": upsServerVersion,
       "upsConformance": upsConformance,
       "upsCompliances": upsCompliances,
       "upsCompliance": upsCompliance,
       "upsGroups": upsGroups,
       "upsGroup": upsGroup}
)
