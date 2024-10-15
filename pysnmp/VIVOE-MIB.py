# SNMP MIB module (VIVOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIVOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:43 2024
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

vivoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1)
)
vivoeMIB.setRevisions(
        ("2012-02-16 13:24",
         "2010-11-04 15:53")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString16(OctetString, TextualConvention):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class DisplayString32(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class DisplayString64(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_Desle_ObjectIdentity = ObjectIdentity
desle = _Desle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35990)
)
_DesleProducts_ObjectIdentity = ObjectIdentity
desleProducts = _DesleProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35990, 3)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1)
)
_DeviceDesc_Type = DisplayString32
_DeviceDesc_Object = MibScalar
deviceDesc = _DeviceDesc_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 1),
    _DeviceDesc_Type()
)
deviceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDesc.setStatus("current")
_DeviceManufacturer_Type = DisplayString64
_DeviceManufacturer_Object = MibScalar
deviceManufacturer = _DeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 2),
    _DeviceManufacturer_Type()
)
deviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceManufacturer.setStatus("current")
_DevicePartNumber_Type = DisplayString32
_DevicePartNumber_Object = MibScalar
devicePartNumber = _DevicePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 3),
    _DevicePartNumber_Type()
)
devicePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePartNumber.setStatus("current")
_DeviceSerialNumber_Type = DisplayString32
_DeviceSerialNumber_Object = MibScalar
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 4),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("current")
_DeviceHardwareVersion_Type = DisplayString16
_DeviceHardwareVersion_Object = MibScalar
deviceHardwareVersion = _DeviceHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 5),
    _DeviceHardwareVersion_Type()
)
deviceHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardwareVersion.setStatus("current")
_DeviceSoftwareVersion_Type = DisplayString16
_DeviceSoftwareVersion_Object = MibScalar
deviceSoftwareVersion = _DeviceSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 6),
    _DeviceSoftwareVersion_Type()
)
deviceSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSoftwareVersion.setStatus("current")
_DeviceFirmwareVersion_Type = DisplayString16
_DeviceFirmwareVersion_Object = MibScalar
deviceFirmwareVersion = _DeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 7),
    _DeviceFirmwareVersion_Type()
)
deviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmwareVersion.setStatus("current")
_DeviceMibVersion_Type = DisplayString16
_DeviceMibVersion_Object = MibScalar
deviceMibVersion = _DeviceMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 8),
    _DeviceMibVersion_Type()
)
deviceMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMibVersion.setStatus("current")


class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("serviceProvider", 1),
          ("serviceUser", 2))
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 9),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_DeviceUserDesc_Type = DisplayString64
_DeviceUserDesc_Object = MibScalar
deviceUserDesc = _DeviceUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 10),
    _DeviceUserDesc_Type()
)
deviceUserDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceUserDesc.setStatus("current")


class _EthernetIfNumber_Type(Integer32):
    """Custom type ethernetIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthernetIfNumber_Type.__name__ = "Integer32"
_EthernetIfNumber_Object = MibScalar
ethernetIfNumber = _EthernetIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 11),
    _EthernetIfNumber_Type()
)
ethernetIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfNumber.setStatus("current")
_EthernetIfTable_Object = MibTable
ethernetIfTable = _EthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    ethernetIfTable.setStatus("current")
_EthernetIfEntry_Object = MibTableRow
ethernetIfEntry = _EthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12, 1)
)
ethernetIfEntry.setIndexNames(
    (0, "VIVOE-MIB", "ethernetIfIndex"),
)
if mibBuilder.loadTexts:
    ethernetIfEntry.setStatus("current")


class _EthernetIfIndex_Type(Integer32):
    """Custom type ethernetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthernetIfIndex_Type.__name__ = "Integer32"
_EthernetIfIndex_Object = MibTableColumn
ethernetIfIndex = _EthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12, 1, 1),
    _EthernetIfIndex_Type()
)
ethernetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetIfIndex.setStatus("current")
_EthernetIfSpeed_Type = Integer32
_EthernetIfSpeed_Object = MibTableColumn
ethernetIfSpeed = _EthernetIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12, 1, 2),
    _EthernetIfSpeed_Type()
)
ethernetIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfSpeed.setStatus("current")
if mibBuilder.loadTexts:
    ethernetIfSpeed.setUnits("Mbps")
_EthernetIfMacAddress_Type = MacAddress
_EthernetIfMacAddress_Object = MibTableColumn
ethernetIfMacAddress = _EthernetIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12, 1, 3),
    _EthernetIfMacAddress_Type()
)
ethernetIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfMacAddress.setStatus("current")
_EthernetIfIpAddress_Type = IpAddress
_EthernetIfIpAddress_Object = MibTableColumn
ethernetIfIpAddress = _EthernetIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12, 1, 4),
    _EthernetIfIpAddress_Type()
)
ethernetIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetIfIpAddress.setStatus("current")
_EthernetIfSubnetMask_Type = IpAddress
_EthernetIfSubnetMask_Object = MibTableColumn
ethernetIfSubnetMask = _EthernetIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12, 1, 5),
    _EthernetIfSubnetMask_Type()
)
ethernetIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetIfSubnetMask.setStatus("current")
_EthernetIfIpAddressConflict_Type = IpAddress
_EthernetIfIpAddressConflict_Object = MibTableColumn
ethernetIfIpAddressConflict = _EthernetIfIpAddressConflict_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 12, 1, 6),
    _EthernetIfIpAddressConflict_Type()
)
ethernetIfIpAddressConflict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetIfIpAddressConflict.setStatus("current")
_DeviceNatoStockNumber_Type = DisplayString32
_DeviceNatoStockNumber_Object = MibScalar
deviceNatoStockNumber = _DeviceNatoStockNumber_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 13),
    _DeviceNatoStockNumber_Type()
)
deviceNatoStockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceNatoStockNumber.setStatus("current")


class _DeviceMode_Type(Integer32):
    """Custom type deviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defaultStartUp", 2),
          ("maintenanceMode", 3),
          ("normal", 1))
    )


_DeviceMode_Type.__name__ = "Integer32"
_DeviceMode_Object = MibScalar
deviceMode = _DeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 14),
    _DeviceMode_Type()
)
deviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMode.setStatus("current")


class _DeviceReset_Type(Integer32):
    """Custom type deviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_DeviceReset_Type.__name__ = "Integer32"
_DeviceReset_Object = MibScalar
deviceReset = _DeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 1, 15),
    _DeviceReset_Type()
)
deviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceReset.setStatus("current")
_VideoFormatInfo_ObjectIdentity = ObjectIdentity
videoFormatInfo = _VideoFormatInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2)
)


class _VideoFormatNumber_Type(Integer32):
    """Custom type videoFormatNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VideoFormatNumber_Type.__name__ = "Integer32"
_VideoFormatNumber_Object = MibScalar
videoFormatNumber = _VideoFormatNumber_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 1),
    _VideoFormatNumber_Type()
)
videoFormatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatNumber.setStatus("current")
_VideoFormatTable_Object = MibTable
videoFormatTable = _VideoFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    videoFormatTable.setStatus("current")
_VideoFormatEntry_Object = MibTableRow
videoFormatEntry = _VideoFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1)
)
videoFormatEntry.setIndexNames(
    (0, "VIVOE-MIB", "videoFormatIndex"),
)
if mibBuilder.loadTexts:
    videoFormatEntry.setStatus("current")


class _VideoFormatIndex_Type(Integer32):
    """Custom type videoFormatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VideoFormatIndex_Type.__name__ = "Integer32"
_VideoFormatIndex_Object = MibTableColumn
videoFormatIndex = _VideoFormatIndex_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 1),
    _VideoFormatIndex_Type()
)
videoFormatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    videoFormatIndex.setStatus("current")


class _VideoFormatType_Type(Integer32):
    """Custom type videoFormatType based on Integer32"""
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
        *(("other", 5),
          ("rawData", 4),
          ("roi", 2),
          ("serviceUser", 3),
          ("videoChannel", 1))
    )


_VideoFormatType_Type.__name__ = "Integer32"
_VideoFormatType_Object = MibTableColumn
videoFormatType = _VideoFormatType_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 2),
    _VideoFormatType_Type()
)
videoFormatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatType.setStatus("current")


class _VideoFormatStatus_Type(Integer32):
    """Custom type videoFormatStatus based on Integer32"""
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


_VideoFormatStatus_Type.__name__ = "Integer32"
_VideoFormatStatus_Object = MibTableColumn
videoFormatStatus = _VideoFormatStatus_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 3),
    _VideoFormatStatus_Type()
)
videoFormatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatStatus.setStatus("current")
_VideoFormatBase_Type = DisplayString16
_VideoFormatBase_Object = MibTableColumn
videoFormatBase = _VideoFormatBase_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 4),
    _VideoFormatBase_Type()
)
videoFormatBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatBase.setStatus("current")
_VideoFormatSampling_Type = DisplayString16
_VideoFormatSampling_Object = MibTableColumn
videoFormatSampling = _VideoFormatSampling_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 5),
    _VideoFormatSampling_Type()
)
videoFormatSampling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatSampling.setStatus("current")


class _VideoFormatBitDepth_Type(Integer32):
    """Custom type videoFormatBitDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VideoFormatBitDepth_Type.__name__ = "Integer32"
_VideoFormatBitDepth_Object = MibTableColumn
videoFormatBitDepth = _VideoFormatBitDepth_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 6),
    _VideoFormatBitDepth_Type()
)
videoFormatBitDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatBitDepth.setStatus("current")


class _VideoFormatFps_Type(Integer32):
    """Custom type videoFormatFps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VideoFormatFps_Type.__name__ = "Integer32"
_VideoFormatFps_Object = MibTableColumn
videoFormatFps = _VideoFormatFps_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 7),
    _VideoFormatFps_Type()
)
videoFormatFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatFps.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatFps.setUnits("Frame per Second")
_VideoFormatColorimetry_Type = DisplayString16
_VideoFormatColorimetry_Object = MibTableColumn
videoFormatColorimetry = _VideoFormatColorimetry_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 8),
    _VideoFormatColorimetry_Type()
)
videoFormatColorimetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatColorimetry.setStatus("current")


class _VideoFormatInterlaced_Type(Integer32):
    """Custom type videoFormatInterlaced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interlaced", 1),
          ("none", 3),
          ("progressive", 2))
    )


_VideoFormatInterlaced_Type.__name__ = "Integer32"
_VideoFormatInterlaced_Object = MibTableColumn
videoFormatInterlaced = _VideoFormatInterlaced_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 9),
    _VideoFormatInterlaced_Type()
)
videoFormatInterlaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatInterlaced.setStatus("current")


class _VideoFormatCompressionFactor_Type(Integer32):
    """Custom type videoFormatCompressionFactor based on Integer32"""
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
        *(("lossless", 3),
          ("none", 4),
          ("targetQuality", 2),
          ("targetRate", 1))
    )


_VideoFormatCompressionFactor_Type.__name__ = "Integer32"
_VideoFormatCompressionFactor_Object = MibTableColumn
videoFormatCompressionFactor = _VideoFormatCompressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 10),
    _VideoFormatCompressionFactor_Type()
)
videoFormatCompressionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatCompressionFactor.setStatus("current")
_VideoFormatCompressionRate_Type = Integer32
_VideoFormatCompressionRate_Object = MibTableColumn
videoFormatCompressionRate = _VideoFormatCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 11),
    _VideoFormatCompressionRate_Type()
)
videoFormatCompressionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatCompressionRate.setStatus("current")
_VideoFormatMaxHorzRes_Type = Integer32
_VideoFormatMaxHorzRes_Object = MibTableColumn
videoFormatMaxHorzRes = _VideoFormatMaxHorzRes_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 12),
    _VideoFormatMaxHorzRes_Type()
)
videoFormatMaxHorzRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatMaxHorzRes.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatMaxHorzRes.setUnits("pixels")
_VideoFormatMaxVertRes_Type = Integer32
_VideoFormatMaxVertRes_Object = MibTableColumn
videoFormatMaxVertRes = _VideoFormatMaxVertRes_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 13),
    _VideoFormatMaxVertRes_Type()
)
videoFormatMaxVertRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFormatMaxVertRes.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatMaxVertRes.setUnits("pixels")
_VideoFormatRoiHorzRes_Type = Integer32
_VideoFormatRoiHorzRes_Object = MibTableColumn
videoFormatRoiHorzRes = _VideoFormatRoiHorzRes_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 14),
    _VideoFormatRoiHorzRes_Type()
)
videoFormatRoiHorzRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatRoiHorzRes.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatRoiHorzRes.setUnits("pixels")
_VideoFormatRoiVertRes_Type = Integer32
_VideoFormatRoiVertRes_Object = MibTableColumn
videoFormatRoiVertRes = _VideoFormatRoiVertRes_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 15),
    _VideoFormatRoiVertRes_Type()
)
videoFormatRoiVertRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatRoiVertRes.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatRoiVertRes.setUnits("pixels")
_VideoFormatRoiOriginTop_Type = Integer32
_VideoFormatRoiOriginTop_Object = MibTableColumn
videoFormatRoiOriginTop = _VideoFormatRoiOriginTop_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 16),
    _VideoFormatRoiOriginTop_Type()
)
videoFormatRoiOriginTop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatRoiOriginTop.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatRoiOriginTop.setUnits("pixels")
_VideoFormatRoiOriginLeft_Type = Integer32
_VideoFormatRoiOriginLeft_Object = MibTableColumn
videoFormatRoiOriginLeft = _VideoFormatRoiOriginLeft_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 17),
    _VideoFormatRoiOriginLeft_Type()
)
videoFormatRoiOriginLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatRoiOriginLeft.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatRoiOriginLeft.setUnits("pixels")
_VideoFormatRoiExtentBottom_Type = Integer32
_VideoFormatRoiExtentBottom_Object = MibTableColumn
videoFormatRoiExtentBottom = _VideoFormatRoiExtentBottom_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 18),
    _VideoFormatRoiExtentBottom_Type()
)
videoFormatRoiExtentBottom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatRoiExtentBottom.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatRoiExtentBottom.setUnits("pixels")
_VideoFormatRoiExtentRight_Type = Integer32
_VideoFormatRoiExtentRight_Object = MibTableColumn
videoFormatRoiExtentRight = _VideoFormatRoiExtentRight_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 19),
    _VideoFormatRoiExtentRight_Type()
)
videoFormatRoiExtentRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatRoiExtentRight.setStatus("current")
if mibBuilder.loadTexts:
    videoFormatRoiExtentRight.setUnits("pixels")


class _VideoFormatRtpPt_Type(Integer32):
    """Custom type videoFormatRtpPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VideoFormatRtpPt_Type.__name__ = "Integer32"
_VideoFormatRtpPt_Object = MibTableColumn
videoFormatRtpPt = _VideoFormatRtpPt_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 2, 2, 1, 20),
    _VideoFormatRtpPt_Type()
)
videoFormatRtpPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFormatRtpPt.setStatus("current")
_ChannelControl_ObjectIdentity = ObjectIdentity
channelControl = _ChannelControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3)
)


class _ChannelReset_Type(Integer32):
    """Custom type channelReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelReset_Type.__name__ = "Integer32"
_ChannelReset_Object = MibScalar
channelReset = _ChannelReset_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 1),
    _ChannelReset_Type()
)
channelReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelReset.setStatus("current")


class _ChannelNumber_Type(Integer32):
    """Custom type channelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ChannelNumber_Type.__name__ = "Integer32"
_ChannelNumber_Object = MibScalar
channelNumber = _ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 2),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumber.setStatus("current")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("current")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1)
)
channelEntry.setIndexNames(
    (0, "VIVOE-MIB", "channelIndex"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")


class _ChannelIndex_Type(Integer32):
    """Custom type channelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ChannelIndex_Type.__name__ = "Integer32"
_ChannelIndex_Object = MibTableColumn
channelIndex = _ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 1),
    _ChannelIndex_Type()
)
channelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelIndex.setStatus("current")


class _ChannelType_Type(Integer32):
    """Custom type channelType based on Integer32"""
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
        *(("other", 5),
          ("rawData", 4),
          ("roi", 2),
          ("serviceUser", 3),
          ("videoChannel", 1))
    )


_ChannelType_Type.__name__ = "Integer32"
_ChannelType_Object = MibTableColumn
channelType = _ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 2),
    _ChannelType_Type()
)
channelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelType.setStatus("current")
_ChannelUserDesc_Type = DisplayString64
_ChannelUserDesc_Object = MibTableColumn
channelUserDesc = _ChannelUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 3),
    _ChannelUserDesc_Type()
)
channelUserDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelUserDesc.setStatus("current")


class _ChannelStatus_Type(Integer32):
    """Custom type channelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singleFrame", 3),
          ("start", 1),
          ("stop", 2))
    )


_ChannelStatus_Type.__name__ = "Integer32"
_ChannelStatus_Object = MibTableColumn
channelStatus = _ChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 4),
    _ChannelStatus_Type()
)
channelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelStatus.setStatus("current")


class _ChannelVideoFormatIndex_Type(Integer32):
    """Custom type channelVideoFormatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelVideoFormatIndex_Type.__name__ = "Integer32"
_ChannelVideoFormatIndex_Object = MibTableColumn
channelVideoFormatIndex = _ChannelVideoFormatIndex_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 5),
    _ChannelVideoFormatIndex_Type()
)
channelVideoFormatIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelVideoFormatIndex.setStatus("current")
_ChannelVideoFormat_Type = DisplayString16
_ChannelVideoFormat_Object = MibTableColumn
channelVideoFormat = _ChannelVideoFormat_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 6),
    _ChannelVideoFormat_Type()
)
channelVideoFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelVideoFormat.setStatus("current")
_ChannelVideoSampling_Type = DisplayString16
_ChannelVideoSampling_Object = MibTableColumn
channelVideoSampling = _ChannelVideoSampling_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 7),
    _ChannelVideoSampling_Type()
)
channelVideoSampling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelVideoSampling.setStatus("current")


class _ChannelVideoBitDepth_Type(Integer32):
    """Custom type channelVideoBitDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelVideoBitDepth_Type.__name__ = "Integer32"
_ChannelVideoBitDepth_Object = MibTableColumn
channelVideoBitDepth = _ChannelVideoBitDepth_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 8),
    _ChannelVideoBitDepth_Type()
)
channelVideoBitDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelVideoBitDepth.setStatus("current")


class _ChannelFps_Type(Integer32):
    """Custom type channelFps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelFps_Type.__name__ = "Integer32"
_ChannelFps_Object = MibTableColumn
channelFps = _ChannelFps_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 9),
    _ChannelFps_Type()
)
channelFps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelFps.setStatus("current")
if mibBuilder.loadTexts:
    channelFps.setUnits("Frames per second")
_ChannelColorimetry_Type = DisplayString16
_ChannelColorimetry_Object = MibTableColumn
channelColorimetry = _ChannelColorimetry_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 10),
    _ChannelColorimetry_Type()
)
channelColorimetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelColorimetry.setStatus("current")


class _ChannelInterlaced_Type(Integer32):
    """Custom type channelInterlaced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interlaced", 1),
          ("none", 3),
          ("progressive", 2))
    )


_ChannelInterlaced_Type.__name__ = "Integer32"
_ChannelInterlaced_Object = MibTableColumn
channelInterlaced = _ChannelInterlaced_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 11),
    _ChannelInterlaced_Type()
)
channelInterlaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelInterlaced.setStatus("current")


class _ChannelCompressionFactor_Type(Integer32):
    """Custom type channelCompressionFactor based on Integer32"""
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
        *(("lossless", 3),
          ("none", 4),
          ("targetQuality", 2),
          ("targetRate", 1))
    )


_ChannelCompressionFactor_Type.__name__ = "Integer32"
_ChannelCompressionFactor_Object = MibTableColumn
channelCompressionFactor = _ChannelCompressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 12),
    _ChannelCompressionFactor_Type()
)
channelCompressionFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCompressionFactor.setStatus("current")
_ChannelCompressionRate_Type = Integer32
_ChannelCompressionRate_Object = MibTableColumn
channelCompressionRate = _ChannelCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 13),
    _ChannelCompressionRate_Type()
)
channelCompressionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCompressionRate.setStatus("current")
_ChannelHorzRes_Type = Integer32
_ChannelHorzRes_Object = MibTableColumn
channelHorzRes = _ChannelHorzRes_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 14),
    _ChannelHorzRes_Type()
)
channelHorzRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelHorzRes.setStatus("current")
if mibBuilder.loadTexts:
    channelHorzRes.setUnits("pixels")
_ChannelVertRes_Type = Integer32
_ChannelVertRes_Object = MibTableColumn
channelVertRes = _ChannelVertRes_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 15),
    _ChannelVertRes_Type()
)
channelVertRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelVertRes.setStatus("current")
if mibBuilder.loadTexts:
    channelVertRes.setUnits("pixels")
_ChannelRoiOriginTop_Type = Integer32
_ChannelRoiOriginTop_Object = MibTableColumn
channelRoiOriginTop = _ChannelRoiOriginTop_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 16),
    _ChannelRoiOriginTop_Type()
)
channelRoiOriginTop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelRoiOriginTop.setStatus("current")
if mibBuilder.loadTexts:
    channelRoiOriginTop.setUnits("pixels")
_ChannelRoiOriginLeft_Type = Integer32
_ChannelRoiOriginLeft_Object = MibTableColumn
channelRoiOriginLeft = _ChannelRoiOriginLeft_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 17),
    _ChannelRoiOriginLeft_Type()
)
channelRoiOriginLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelRoiOriginLeft.setStatus("current")
if mibBuilder.loadTexts:
    channelRoiOriginLeft.setUnits("pixels")
_ChannelRoiExtentBottom_Type = Integer32
_ChannelRoiExtentBottom_Object = MibTableColumn
channelRoiExtentBottom = _ChannelRoiExtentBottom_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 18),
    _ChannelRoiExtentBottom_Type()
)
channelRoiExtentBottom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelRoiExtentBottom.setStatus("current")
if mibBuilder.loadTexts:
    channelRoiExtentBottom.setUnits("pixels")
_ChannelRoiExtentRight_Type = Integer32
_ChannelRoiExtentRight_Object = MibTableColumn
channelRoiExtentRight = _ChannelRoiExtentRight_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 19),
    _ChannelRoiExtentRight_Type()
)
channelRoiExtentRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelRoiExtentRight.setStatus("current")
if mibBuilder.loadTexts:
    channelRoiExtentRight.setUnits("pixels")


class _ChannelRtpPt_Type(Integer32):
    """Custom type channelRtpPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ChannelRtpPt_Type.__name__ = "Integer32"
_ChannelRtpPt_Object = MibTableColumn
channelRtpPt = _ChannelRtpPt_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 20),
    _ChannelRtpPt_Type()
)
channelRtpPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelRtpPt.setStatus("current")
_ChannelReceiveIpAddress_Type = IpAddress
_ChannelReceiveIpAddress_Object = MibTableColumn
channelReceiveIpAddress = _ChannelReceiveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 21),
    _ChannelReceiveIpAddress_Type()
)
channelReceiveIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelReceiveIpAddress.setStatus("current")
_ChannelInterPacketDelay_Type = Integer32
_ChannelInterPacketDelay_Object = MibTableColumn
channelInterPacketDelay = _ChannelInterPacketDelay_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 22),
    _ChannelInterPacketDelay_Type()
)
channelInterPacketDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInterPacketDelay.setStatus("current")
if mibBuilder.loadTexts:
    channelInterPacketDelay.setUnits("microseconds")


class _ChannelSapMessageInterval_Type(Integer32):
    """Custom type channelSapMessageInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ChannelSapMessageInterval_Type.__name__ = "Integer32"
_ChannelSapMessageInterval_Object = MibTableColumn
channelSapMessageInterval = _ChannelSapMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 23),
    _ChannelSapMessageInterval_Type()
)
channelSapMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelSapMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    channelSapMessageInterval.setUnits("milliseconds")


class _ChannelDefaultVideoFormatIndex_Type(Integer32):
    """Custom type channelDefaultVideoFormatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelDefaultVideoFormatIndex_Type.__name__ = "Integer32"
_ChannelDefaultVideoFormatIndex_Object = MibTableColumn
channelDefaultVideoFormatIndex = _ChannelDefaultVideoFormatIndex_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 24),
    _ChannelDefaultVideoFormatIndex_Type()
)
channelDefaultVideoFormatIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelDefaultVideoFormatIndex.setStatus("current")
_ChannelDefaultReceiveIpAddress_Type = IpAddress
_ChannelDefaultReceiveIpAddress_Object = MibTableColumn
channelDefaultReceiveIpAddress = _ChannelDefaultReceiveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 3, 3, 1, 25),
    _ChannelDefaultReceiveIpAddress_Type()
)
channelDefaultReceiveIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelDefaultReceiveIpAddress.setStatus("current")
_VivoeNotifications_ObjectIdentity = ObjectIdentity
vivoeNotifications = _VivoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 4)
)
_VivoeGroups_ObjectIdentity = ObjectIdentity
vivoeGroups = _VivoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 5)
)

# Managed Objects groups

presetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 5, 1)
)
presetGroup.setObjects(
      *(("VIVOE-MIB", "deviceDesc"),
        ("VIVOE-MIB", "deviceManufacturer"),
        ("VIVOE-MIB", "devicePartNumber"),
        ("VIVOE-MIB", "deviceSerialNumber"),
        ("VIVOE-MIB", "deviceHardwareVersion"),
        ("VIVOE-MIB", "deviceSoftwareVersion"),
        ("VIVOE-MIB", "deviceFirmwareVersion"),
        ("VIVOE-MIB", "deviceMibVersion"),
        ("VIVOE-MIB", "deviceType"),
        ("VIVOE-MIB", "ethernetIfNumber"),
        ("VIVOE-MIB", "ethernetIfSpeed"),
        ("VIVOE-MIB", "ethernetIfMacAddress"),
        ("VIVOE-MIB", "deviceNatoStockNumber"),
        ("VIVOE-MIB", "videoFormatNumber"),
        ("VIVOE-MIB", "videoFormatType"),
        ("VIVOE-MIB", "videoFormatStatus"),
        ("VIVOE-MIB", "videoFormatBase"),
        ("VIVOE-MIB", "videoFormatSampling"),
        ("VIVOE-MIB", "videoFormatBitDepth"),
        ("VIVOE-MIB", "videoFormatFps"),
        ("VIVOE-MIB", "videoFormatColorimetry"),
        ("VIVOE-MIB", "videoFormatInterlaced"),
        ("VIVOE-MIB", "videoFormatCompressionFactor"),
        ("VIVOE-MIB", "videoFormatMaxHorzRes"),
        ("VIVOE-MIB", "videoFormatMaxVertRes"),
        ("VIVOE-MIB", "channelNumber"))
)
if mibBuilder.loadTexts:
    presetGroup.setStatus("current")

setChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 5, 2)
)
setChannelGroup.setObjects(
      *(("VIVOE-MIB", "channelType"),
        ("VIVOE-MIB", "channelVideoFormat"),
        ("VIVOE-MIB", "channelVideoSampling"),
        ("VIVOE-MIB", "channelVideoBitDepth"),
        ("VIVOE-MIB", "channelFps"),
        ("VIVOE-MIB", "channelColorimetry"),
        ("VIVOE-MIB", "channelInterlaced"),
        ("VIVOE-MIB", "channelCompressionFactor"),
        ("VIVOE-MIB", "channelCompressionRate"),
        ("VIVOE-MIB", "channelHorzRes"),
        ("VIVOE-MIB", "channelVertRes"),
        ("VIVOE-MIB", "channelRoiOriginTop"),
        ("VIVOE-MIB", "channelRoiOriginLeft"),
        ("VIVOE-MIB", "channelRoiExtentBottom"),
        ("VIVOE-MIB", "channelRoiExtentRight"),
        ("VIVOE-MIB", "channelRtpPt"))
)
if mibBuilder.loadTexts:
    setChannelGroup.setStatus("current")

maintenanceModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 5, 3)
)
maintenanceModeGroup.setObjects(
      *(("VIVOE-MIB", "deviceUserDesc"),
        ("VIVOE-MIB", "ethernetIfIpAddress"),
        ("VIVOE-MIB", "ethernetIfSubnetMask"),
        ("VIVOE-MIB", "ethernetIfIpAddressConflict"),
        ("VIVOE-MIB", "deviceReset"),
        ("VIVOE-MIB", "videoFormatCompressionRate"),
        ("VIVOE-MIB", "videoFormatRoiHorzRes"),
        ("VIVOE-MIB", "videoFormatRoiVertRes"),
        ("VIVOE-MIB", "videoFormatRoiOriginTop"),
        ("VIVOE-MIB", "videoFormatRoiOriginLeft"),
        ("VIVOE-MIB", "videoFormatRoiExtentBottom"),
        ("VIVOE-MIB", "videoFormatRoiExtentRight"),
        ("VIVOE-MIB", "videoFormatRtpPt"),
        ("VIVOE-MIB", "channelReset"),
        ("VIVOE-MIB", "channelUserDesc"),
        ("VIVOE-MIB", "channelInterPacketDelay"),
        ("VIVOE-MIB", "channelSapMessageInterval"),
        ("VIVOE-MIB", "channelDefaultVideoFormatIndex"),
        ("VIVOE-MIB", "channelDefaultReceiveIpAddress"))
)
if mibBuilder.loadTexts:
    maintenanceModeGroup.setStatus("current")

volatileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 5, 4)
)
volatileGroup.setObjects(
      *(("VIVOE-MIB", "deviceMode"),
        ("VIVOE-MIB", "deviceReset"),
        ("VIVOE-MIB", "channelReset"),
        ("VIVOE-MIB", "channelType"),
        ("VIVOE-MIB", "channelStatus"),
        ("VIVOE-MIB", "channelVideoFormatIndex"),
        ("VIVOE-MIB", "channelVideoFormat"),
        ("VIVOE-MIB", "channelVideoSampling"),
        ("VIVOE-MIB", "channelVideoBitDepth"),
        ("VIVOE-MIB", "channelFps"),
        ("VIVOE-MIB", "channelColorimetry"),
        ("VIVOE-MIB", "channelInterlaced"),
        ("VIVOE-MIB", "channelCompressionFactor"),
        ("VIVOE-MIB", "channelCompressionRate"),
        ("VIVOE-MIB", "channelHorzRes"),
        ("VIVOE-MIB", "channelVertRes"),
        ("VIVOE-MIB", "channelRoiOriginTop"),
        ("VIVOE-MIB", "channelRoiOriginLeft"),
        ("VIVOE-MIB", "channelRoiExtentBottom"),
        ("VIVOE-MIB", "channelRoiExtentRight"),
        ("VIVOE-MIB", "channelRtpPt"),
        ("VIVOE-MIB", "channelReceiveIpAddress"))
)
if mibBuilder.loadTexts:
    volatileGroup.setStatus("current")


# Notification objects

deviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 4, 1)
)
deviceError.setObjects(
      *(("VIVOE-MIB", "deviceUserDesc"),
        ("VIVOE-MIB", "deviceMode"))
)
if mibBuilder.loadTexts:
    deviceError.setStatus(
        "current"
    )

ipAddressConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 4, 2)
)
ipAddressConflict.setObjects(
      *(("VIVOE-MIB", "ethernetIfIpAddress"),
        ("VIVOE-MIB", "ethernetIfIpAddressConflict"))
)
if mibBuilder.loadTexts:
    ipAddressConflict.setStatus(
        "current"
    )


# Notifications groups

notificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35990, 3, 1, 5, 5)
)
notificationGroup.setObjects(
      *(("VIVOE-MIB", "deviceError"),
        ("VIVOE-MIB", "ipAddressConflict"))
)
if mibBuilder.loadTexts:
    notificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIVOE-MIB",
    **{"DisplayString16": DisplayString16,
       "DisplayString32": DisplayString32,
       "DisplayString64": DisplayString64,
       "desle": desle,
       "desleProducts": desleProducts,
       "vivoeMIB": vivoeMIB,
       "deviceInfo": deviceInfo,
       "deviceDesc": deviceDesc,
       "deviceManufacturer": deviceManufacturer,
       "devicePartNumber": devicePartNumber,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceHardwareVersion": deviceHardwareVersion,
       "deviceSoftwareVersion": deviceSoftwareVersion,
       "deviceFirmwareVersion": deviceFirmwareVersion,
       "deviceMibVersion": deviceMibVersion,
       "deviceType": deviceType,
       "deviceUserDesc": deviceUserDesc,
       "ethernetIfNumber": ethernetIfNumber,
       "ethernetIfTable": ethernetIfTable,
       "ethernetIfEntry": ethernetIfEntry,
       "ethernetIfIndex": ethernetIfIndex,
       "ethernetIfSpeed": ethernetIfSpeed,
       "ethernetIfMacAddress": ethernetIfMacAddress,
       "ethernetIfIpAddress": ethernetIfIpAddress,
       "ethernetIfSubnetMask": ethernetIfSubnetMask,
       "ethernetIfIpAddressConflict": ethernetIfIpAddressConflict,
       "deviceNatoStockNumber": deviceNatoStockNumber,
       "deviceMode": deviceMode,
       "deviceReset": deviceReset,
       "videoFormatInfo": videoFormatInfo,
       "videoFormatNumber": videoFormatNumber,
       "videoFormatTable": videoFormatTable,
       "videoFormatEntry": videoFormatEntry,
       "videoFormatIndex": videoFormatIndex,
       "videoFormatType": videoFormatType,
       "videoFormatStatus": videoFormatStatus,
       "videoFormatBase": videoFormatBase,
       "videoFormatSampling": videoFormatSampling,
       "videoFormatBitDepth": videoFormatBitDepth,
       "videoFormatFps": videoFormatFps,
       "videoFormatColorimetry": videoFormatColorimetry,
       "videoFormatInterlaced": videoFormatInterlaced,
       "videoFormatCompressionFactor": videoFormatCompressionFactor,
       "videoFormatCompressionRate": videoFormatCompressionRate,
       "videoFormatMaxHorzRes": videoFormatMaxHorzRes,
       "videoFormatMaxVertRes": videoFormatMaxVertRes,
       "videoFormatRoiHorzRes": videoFormatRoiHorzRes,
       "videoFormatRoiVertRes": videoFormatRoiVertRes,
       "videoFormatRoiOriginTop": videoFormatRoiOriginTop,
       "videoFormatRoiOriginLeft": videoFormatRoiOriginLeft,
       "videoFormatRoiExtentBottom": videoFormatRoiExtentBottom,
       "videoFormatRoiExtentRight": videoFormatRoiExtentRight,
       "videoFormatRtpPt": videoFormatRtpPt,
       "channelControl": channelControl,
       "channelReset": channelReset,
       "channelNumber": channelNumber,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channelIndex": channelIndex,
       "channelType": channelType,
       "channelUserDesc": channelUserDesc,
       "channelStatus": channelStatus,
       "channelVideoFormatIndex": channelVideoFormatIndex,
       "channelVideoFormat": channelVideoFormat,
       "channelVideoSampling": channelVideoSampling,
       "channelVideoBitDepth": channelVideoBitDepth,
       "channelFps": channelFps,
       "channelColorimetry": channelColorimetry,
       "channelInterlaced": channelInterlaced,
       "channelCompressionFactor": channelCompressionFactor,
       "channelCompressionRate": channelCompressionRate,
       "channelHorzRes": channelHorzRes,
       "channelVertRes": channelVertRes,
       "channelRoiOriginTop": channelRoiOriginTop,
       "channelRoiOriginLeft": channelRoiOriginLeft,
       "channelRoiExtentBottom": channelRoiExtentBottom,
       "channelRoiExtentRight": channelRoiExtentRight,
       "channelRtpPt": channelRtpPt,
       "channelReceiveIpAddress": channelReceiveIpAddress,
       "channelInterPacketDelay": channelInterPacketDelay,
       "channelSapMessageInterval": channelSapMessageInterval,
       "channelDefaultVideoFormatIndex": channelDefaultVideoFormatIndex,
       "channelDefaultReceiveIpAddress": channelDefaultReceiveIpAddress,
       "vivoeNotifications": vivoeNotifications,
       "deviceError": deviceError,
       "ipAddressConflict": ipAddressConflict,
       "vivoeGroups": vivoeGroups,
       "presetGroup": presetGroup,
       "setChannelGroup": setChannelGroup,
       "maintenanceModeGroup": maintenanceModeGroup,
       "volatileGroup": volatileGroup,
       "notificationGroup": notificationGroup}
)
