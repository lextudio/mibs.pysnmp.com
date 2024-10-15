# SNMP MIB module (ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:42 2024
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



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiInteger64X(Integer32):
    """Custom type DmiInteger64X based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18446744073709551615, 18446744073709551615),
    )





class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Thirdparty_ObjectIdentity = ObjectIdentity
thirdparty = _Thirdparty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 50)
)
_Isc20_ObjectIdentity = ObjectIdentity
isc20 = _Isc20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 50, 10)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
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
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4),
          ("vVerificationIsNotSupported", 2))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")
_TStorageDevices_Object = MibTable
tStorageDevices = _TStorageDevices_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001)
)
if mibBuilder.loadTexts:
    tStorageDevices.setStatus("mandatory")
_EStorageDevices_Object = MibTableRow
eStorageDevices = _EStorageDevices_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1)
)
eStorageDevices.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7001StorageDeviceIndex"),
)
if mibBuilder.loadTexts:
    eStorageDevices.setStatus("mandatory")
_A7001StorageDeviceIndex_Type = DmiInteger
_A7001StorageDeviceIndex_Object = MibTableColumn
a7001StorageDeviceIndex = _A7001StorageDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 1),
    _A7001StorageDeviceIndex_Type()
)
a7001StorageDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001StorageDeviceIndex.setStatus("mandatory")


class _A7001Type_Type(Integer32):
    """Custom type a7001Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("vCartridgeRigidDiskDrive", 10),
          ("vCompactDiskDrive", 8),
          ("vDigitalVersatileDiskDvdDrive", 15),
          ("vDigitalVersatileDiskDvdRamDrive", 16),
          ("vFlashDisk", 9),
          ("vFlexibleDisketteDrive", 4),
          ("vMagneto-opticalDrive", 7),
          ("vMediaChanger", 14),
          ("vOpticalFloppyDrive", 11),
          ("vOpticalWrite-onceread-manyWormDrive", 6),
          ("vOther", 1),
          ("vRigidDiskDrive", 3),
          ("vSolidState", 13),
          ("vTapeDrive", 12),
          ("vUnknown", 2))
    )


_A7001Type_Type.__name__ = "Integer32"
_A7001Type_Object = MibTableColumn
a7001Type = _A7001Type_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 2),
    _A7001Type_Type()
)
a7001Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001Type.setStatus("mandatory")
_A7001TypeDescription_Type = DmiDisplaystring
_A7001TypeDescription_Object = MibTableColumn
a7001TypeDescription = _A7001TypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 3),
    _A7001TypeDescription_Type()
)
a7001TypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001TypeDescription.setStatus("mandatory")
_A7001Sub_identifier_Type = DmiDisplaystring
_A7001Sub_identifier_Object = MibScalar
a7001Sub_identifier = _A7001Sub_identifier_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 4),
    _A7001Sub_identifier_Type()
)
a7001Sub_identifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001Sub_identifier.setStatus("mandatory")
_A7001MediaDataBlockSize_Type = DmiInteger
_A7001MediaDataBlockSize_Object = MibTableColumn
a7001MediaDataBlockSize = _A7001MediaDataBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 5),
    _A7001MediaDataBlockSize_Type()
)
a7001MediaDataBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001MediaDataBlockSize.setStatus("mandatory")
_A7001FormattedMediaCapacity_Type = DmiInteger64X
_A7001FormattedMediaCapacity_Object = MibTableColumn
a7001FormattedMediaCapacity = _A7001FormattedMediaCapacity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 6),
    _A7001FormattedMediaCapacity_Type()
)
a7001FormattedMediaCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001FormattedMediaCapacity.setStatus("mandatory")


class _A7001RemovableDevice_Type(Integer32):
    """Custom type a7001RemovableDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A7001RemovableDevice_Type.__name__ = "Integer32"
_A7001RemovableDevice_Object = MibTableColumn
a7001RemovableDevice = _A7001RemovableDevice_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 7),
    _A7001RemovableDevice_Type()
)
a7001RemovableDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001RemovableDevice.setStatus("mandatory")


class _A7001DeviceLoaded_Type(Integer32):
    """Custom type a7001DeviceLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A7001DeviceLoaded_Type.__name__ = "Integer32"
_A7001DeviceLoaded_Object = MibTableColumn
a7001DeviceLoaded = _A7001DeviceLoaded_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 8),
    _A7001DeviceLoaded_Type()
)
a7001DeviceLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001DeviceLoaded.setStatus("mandatory")


class _A7001RemovableMedia_Type(Integer32):
    """Custom type a7001RemovableMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A7001RemovableMedia_Type.__name__ = "Integer32"
_A7001RemovableMedia_Object = MibTableColumn
a7001RemovableMedia = _A7001RemovableMedia_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 9),
    _A7001RemovableMedia_Type()
)
a7001RemovableMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001RemovableMedia.setStatus("mandatory")


class _A7001MediaLoaded_Type(Integer32):
    """Custom type a7001MediaLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A7001MediaLoaded_Type.__name__ = "Integer32"
_A7001MediaLoaded_Object = MibTableColumn
a7001MediaLoaded = _A7001MediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 10),
    _A7001MediaLoaded_Type()
)
a7001MediaLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001MediaLoaded.setStatus("mandatory")


class _A7001Compression_Type(Integer32):
    """Custom type a7001Compression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A7001Compression_Type.__name__ = "Integer32"
_A7001Compression_Object = MibTableColumn
a7001Compression = _A7001Compression_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 11),
    _A7001Compression_Type()
)
a7001Compression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001Compression.setStatus("mandatory")


class _A7001Encryption_Type(Integer32):
    """Custom type a7001Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A7001Encryption_Type.__name__ = "Integer32"
_A7001Encryption_Object = MibTableColumn
a7001Encryption = _A7001Encryption_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7001, 1, 12),
    _A7001Encryption_Type()
)
a7001Encryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7001Encryption.setStatus("mandatory")
_TStorageDevicesEvents_Object = MibTable
tStorageDevicesEvents = _TStorageDevicesEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002)
)
if mibBuilder.loadTexts:
    tStorageDevicesEvents.setStatus("mandatory")
_EStorageDevicesEvents_Object = MibTableRow
eStorageDevicesEvents = _EStorageDevicesEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1)
)
eStorageDevicesEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eStorageDevicesEvents.setStatus("mandatory")


class _A7002StorageDevicesEventType_Type(Integer32):
    """Custom type a7002StorageDevicesEventType based on Integer32"""
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
        *(("vCioEvent", 5),
          ("vRebuildInProgress", 1),
          ("vSelf-monitoringWarning", 4),
          ("vStorageDeviceError", 3),
          ("vStorageDeviceReadying", 2))
    )


_A7002StorageDevicesEventType_Type.__name__ = "Integer32"
_A7002StorageDevicesEventType_Object = MibTableColumn
a7002StorageDevicesEventType = _A7002StorageDevicesEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 1),
    _A7002StorageDevicesEventType_Type()
)
a7002StorageDevicesEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002StorageDevicesEventType.setStatus("mandatory")


class _A7002EventSeverity_Type(Integer32):
    """Custom type a7002EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7002EventSeverity_Type.__name__ = "Integer32"
_A7002EventSeverity_Object = MibTableColumn
a7002EventSeverity = _A7002EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 2),
    _A7002EventSeverity_Type()
)
a7002EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002EventSeverity.setStatus("mandatory")


class _A7002EventIsStateBased_Type(Integer32):
    """Custom type a7002EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7002EventIsStateBased_Type.__name__ = "Integer32"
_A7002EventIsStateBased_Object = MibTableColumn
a7002EventIsStateBased = _A7002EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 3),
    _A7002EventIsStateBased_Type()
)
a7002EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002EventIsStateBased.setStatus("mandatory")
_A7002EventStateKey_Type = DmiInteger
_A7002EventStateKey_Object = MibTableColumn
a7002EventStateKey = _A7002EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 4),
    _A7002EventStateKey_Type()
)
a7002EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002EventStateKey.setStatus("mandatory")
_A7002AssociatedGroup_Type = DmiDisplaystring
_A7002AssociatedGroup_Object = MibTableColumn
a7002AssociatedGroup = _A7002AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 5),
    _A7002AssociatedGroup_Type()
)
a7002AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002AssociatedGroup.setStatus("mandatory")


class _A7002EventSystem_Type(Integer32):
    """Custom type a7002EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7002EventSystem_Type.__name__ = "Integer32"
_A7002EventSystem_Object = MibTableColumn
a7002EventSystem = _A7002EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 6),
    _A7002EventSystem_Type()
)
a7002EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002EventSystem.setStatus("mandatory")


class _A7002EventSubsystem_Type(Integer32):
    """Custom type a7002EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7002EventSubsystem_Type.__name__ = "Integer32"
_A7002EventSubsystem_Object = MibTableColumn
a7002EventSubsystem = _A7002EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 7),
    _A7002EventSubsystem_Type()
)
a7002EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002EventSubsystem.setStatus("mandatory")


class _A7002EventSolution_Type(Integer32):
    """Custom type a7002EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7002EventSolution_Type.__name__ = "Integer32"
_A7002EventSolution_Object = MibTableColumn
a7002EventSolution = _A7002EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 8),
    _A7002EventSolution_Type()
)
a7002EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002EventSolution.setStatus("mandatory")


class _A7002InstanceDataPresent_Type(Integer32):
    """Custom type a7002InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7002InstanceDataPresent_Type.__name__ = "Integer32"
_A7002InstanceDataPresent_Object = MibTableColumn
a7002InstanceDataPresent = _A7002InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 9),
    _A7002InstanceDataPresent_Type()
)
a7002InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002InstanceDataPresent.setStatus("mandatory")
_A7002EventMessage_Type = DmiDisplaystring
_A7002EventMessage_Object = MibTableColumn
a7002EventMessage = _A7002EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 10),
    _A7002EventMessage_Type()
)
a7002EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002EventMessage.setStatus("mandatory")
_A7002VendorSpecificData_Type = DmiOctetstring
_A7002VendorSpecificData_Object = MibTableColumn
a7002VendorSpecificData = _A7002VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 11),
    _A7002VendorSpecificData_Type()
)
a7002VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7002VendorSpecificData.setStatus("mandatory")
_TStorageController_Object = MibTable
tStorageController = _TStorageController_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7003)
)
if mibBuilder.loadTexts:
    tStorageController.setStatus("mandatory")
_EStorageController_Object = MibTableRow
eStorageController = _EStorageController_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7003, 1)
)
eStorageController.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7003ControllerIndex"),
)
if mibBuilder.loadTexts:
    eStorageController.setStatus("mandatory")
_A7003ControllerIndex_Type = DmiInteger
_A7003ControllerIndex_Object = MibTableColumn
a7003ControllerIndex = _A7003ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7003, 1, 1),
    _A7003ControllerIndex_Type()
)
a7003ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7003ControllerIndex.setStatus("mandatory")
_A7003Identification_Type = DmiDisplaystring
_A7003Identification_Object = MibTableColumn
a7003Identification = _A7003Identification_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7003, 1, 2),
    _A7003Identification_Type()
)
a7003Identification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7003Identification.setStatus("mandatory")


class _A7003ProtectionManagement_Type(Integer32):
    """Custom type a7003ProtectionManagement based on Integer32"""
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
        *(("vOther", 1),
          ("vProtected", 4),
          ("vProtectedThroughScsi-3ControllerComman1", 6),
          ("vProtectedThroughScsi-3ControllerCommand", 5),
          ("vUnknown", 2),
          ("vUnprotected", 3))
    )


_A7003ProtectionManagement_Type.__name__ = "Integer32"
_A7003ProtectionManagement_Object = MibTableColumn
a7003ProtectionManagement = _A7003ProtectionManagement_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7003, 1, 3),
    _A7003ProtectionManagement_Type()
)
a7003ProtectionManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7003ProtectionManagement.setStatus("mandatory")


class _A7003BusMaster_Type(Integer32):
    """Custom type a7003BusMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A7003BusMaster_Type.__name__ = "Integer32"
_A7003BusMaster_Object = MibTableColumn
a7003BusMaster = _A7003BusMaster_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7003, 1, 4),
    _A7003BusMaster_Type()
)
a7003BusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7003BusMaster.setStatus("mandatory")
_A7003SecondsSinceLastPower_up_Type = DmiInteger
_A7003SecondsSinceLastPower_up_Object = MibScalar
a7003SecondsSinceLastPower_up = _A7003SecondsSinceLastPower_up_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7003, 1, 5),
    _A7003SecondsSinceLastPower_up_Type()
)
a7003SecondsSinceLastPower_up.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7003SecondsSinceLastPower_up.setStatus("mandatory")
_TStorageControllerEvents_Object = MibTable
tStorageControllerEvents = _TStorageControllerEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004)
)
if mibBuilder.loadTexts:
    tStorageControllerEvents.setStatus("mandatory")
_EStorageControllerEvents_Object = MibTableRow
eStorageControllerEvents = _EStorageControllerEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1)
)
eStorageControllerEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eStorageControllerEvents.setStatus("mandatory")


class _A7004StorageControllerEventType_Type(Integer32):
    """Custom type a7004StorageControllerEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vCioEvent", 3),
          ("vSelf-monitoringWarning1", 2),
          ("vStorageControllerError", 1))
    )


_A7004StorageControllerEventType_Type.__name__ = "Integer32"
_A7004StorageControllerEventType_Object = MibTableColumn
a7004StorageControllerEventType = _A7004StorageControllerEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 1),
    _A7004StorageControllerEventType_Type()
)
a7004StorageControllerEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004StorageControllerEventType.setStatus("mandatory")


class _A7004EventSeverity_Type(Integer32):
    """Custom type a7004EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7004EventSeverity_Type.__name__ = "Integer32"
_A7004EventSeverity_Object = MibTableColumn
a7004EventSeverity = _A7004EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 2),
    _A7004EventSeverity_Type()
)
a7004EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004EventSeverity.setStatus("mandatory")


class _A7004EventIsStateBased_Type(Integer32):
    """Custom type a7004EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7004EventIsStateBased_Type.__name__ = "Integer32"
_A7004EventIsStateBased_Object = MibTableColumn
a7004EventIsStateBased = _A7004EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 3),
    _A7004EventIsStateBased_Type()
)
a7004EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004EventIsStateBased.setStatus("mandatory")
_A7004EventStateKey_Type = DmiInteger
_A7004EventStateKey_Object = MibTableColumn
a7004EventStateKey = _A7004EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 4),
    _A7004EventStateKey_Type()
)
a7004EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004EventStateKey.setStatus("mandatory")
_A7004AssociatedGroup_Type = DmiDisplaystring
_A7004AssociatedGroup_Object = MibTableColumn
a7004AssociatedGroup = _A7004AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 5),
    _A7004AssociatedGroup_Type()
)
a7004AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004AssociatedGroup.setStatus("mandatory")


class _A7004EventSystem_Type(Integer32):
    """Custom type a7004EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7004EventSystem_Type.__name__ = "Integer32"
_A7004EventSystem_Object = MibTableColumn
a7004EventSystem = _A7004EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 6),
    _A7004EventSystem_Type()
)
a7004EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004EventSystem.setStatus("mandatory")


class _A7004EventSubsystem_Type(Integer32):
    """Custom type a7004EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7004EventSubsystem_Type.__name__ = "Integer32"
_A7004EventSubsystem_Object = MibTableColumn
a7004EventSubsystem = _A7004EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 7),
    _A7004EventSubsystem_Type()
)
a7004EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004EventSubsystem.setStatus("mandatory")


class _A7004EventSolution_Type(Integer32):
    """Custom type a7004EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7004EventSolution_Type.__name__ = "Integer32"
_A7004EventSolution_Object = MibTableColumn
a7004EventSolution = _A7004EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 8),
    _A7004EventSolution_Type()
)
a7004EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004EventSolution.setStatus("mandatory")


class _A7004InstanceDataPresent_Type(Integer32):
    """Custom type a7004InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7004InstanceDataPresent_Type.__name__ = "Integer32"
_A7004InstanceDataPresent_Object = MibTableColumn
a7004InstanceDataPresent = _A7004InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 9),
    _A7004InstanceDataPresent_Type()
)
a7004InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004InstanceDataPresent.setStatus("mandatory")
_A7004EventMessage_Type = DmiDisplaystring
_A7004EventMessage_Object = MibTableColumn
a7004EventMessage = _A7004EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 10),
    _A7004EventMessage_Type()
)
a7004EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004EventMessage.setStatus("mandatory")
_A7004VendorSpecificData_Type = DmiOctetstring
_A7004VendorSpecificData_Object = MibTableColumn
a7004VendorSpecificData = _A7004VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 11),
    _A7004VendorSpecificData_Type()
)
a7004VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7004VendorSpecificData.setStatus("mandatory")
_TEnclosure_Object = MibTable
tEnclosure = _TEnclosure_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7005)
)
if mibBuilder.loadTexts:
    tEnclosure.setStatus("mandatory")
_EEnclosure_Object = MibTableRow
eEnclosure = _EEnclosure_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7005, 1)
)
eEnclosure.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7005EnclosureIndex"),
)
if mibBuilder.loadTexts:
    eEnclosure.setStatus("mandatory")
_A7005EnclosureIndex_Type = DmiInteger
_A7005EnclosureIndex_Object = MibTableColumn
a7005EnclosureIndex = _A7005EnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7005, 1, 1),
    _A7005EnclosureIndex_Type()
)
a7005EnclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7005EnclosureIndex.setStatus("mandatory")


class _A7005Type_Type(Integer32):
    """Custom type a7005Type based on Integer32"""
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
        *(("vAemi", 6),
          ("vDecfault", 3),
          ("vOther", 1),
          ("vSaf-te", 4),
          ("vSes", 5),
          ("vUnknown", 2))
    )


_A7005Type_Type.__name__ = "Integer32"
_A7005Type_Object = MibTableColumn
a7005Type = _A7005Type_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7005, 1, 2),
    _A7005Type_Type()
)
a7005Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7005Type.setStatus("mandatory")
_A7005Description_Type = DmiDisplaystring
_A7005Description_Object = MibTableColumn
a7005Description = _A7005Description_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7005, 1, 3),
    _A7005Description_Type()
)
a7005Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7005Description.setStatus("mandatory")
_TEnclosureEvents_Object = MibTable
tEnclosureEvents = _TEnclosureEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006)
)
if mibBuilder.loadTexts:
    tEnclosureEvents.setStatus("mandatory")
_EEnclosureEvents_Object = MibTableRow
eEnclosureEvents = _EEnclosureEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1)
)
eEnclosureEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEnclosureEvents.setStatus("mandatory")


class _A7006EnclosureEventType_Type(Integer32):
    """Custom type a7006EnclosureEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vCioEvent", 1)
    )


_A7006EnclosureEventType_Type.__name__ = "Integer32"
_A7006EnclosureEventType_Object = MibTableColumn
a7006EnclosureEventType = _A7006EnclosureEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 1),
    _A7006EnclosureEventType_Type()
)
a7006EnclosureEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EnclosureEventType.setStatus("mandatory")


class _A7006EventSeverity_Type(Integer32):
    """Custom type a7006EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7006EventSeverity_Type.__name__ = "Integer32"
_A7006EventSeverity_Object = MibTableColumn
a7006EventSeverity = _A7006EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 2),
    _A7006EventSeverity_Type()
)
a7006EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EventSeverity.setStatus("mandatory")


class _A7006EventIsStateBased_Type(Integer32):
    """Custom type a7006EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7006EventIsStateBased_Type.__name__ = "Integer32"
_A7006EventIsStateBased_Object = MibTableColumn
a7006EventIsStateBased = _A7006EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 3),
    _A7006EventIsStateBased_Type()
)
a7006EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EventIsStateBased.setStatus("mandatory")
_A7006EventStateKey_Type = DmiInteger
_A7006EventStateKey_Object = MibTableColumn
a7006EventStateKey = _A7006EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 4),
    _A7006EventStateKey_Type()
)
a7006EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EventStateKey.setStatus("mandatory")
_A7006AssociatedGroup_Type = DmiDisplaystring
_A7006AssociatedGroup_Object = MibTableColumn
a7006AssociatedGroup = _A7006AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 5),
    _A7006AssociatedGroup_Type()
)
a7006AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006AssociatedGroup.setStatus("mandatory")


class _A7006EventSystem_Type(Integer32):
    """Custom type a7006EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7006EventSystem_Type.__name__ = "Integer32"
_A7006EventSystem_Object = MibTableColumn
a7006EventSystem = _A7006EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 6),
    _A7006EventSystem_Type()
)
a7006EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EventSystem.setStatus("mandatory")


class _A7006EventSubsystem_Type(Integer32):
    """Custom type a7006EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7006EventSubsystem_Type.__name__ = "Integer32"
_A7006EventSubsystem_Object = MibTableColumn
a7006EventSubsystem = _A7006EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 7),
    _A7006EventSubsystem_Type()
)
a7006EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EventSubsystem.setStatus("mandatory")


class _A7006EventSolution_Type(Integer32):
    """Custom type a7006EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7006EventSolution_Type.__name__ = "Integer32"
_A7006EventSolution_Object = MibTableColumn
a7006EventSolution = _A7006EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 8),
    _A7006EventSolution_Type()
)
a7006EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EventSolution.setStatus("mandatory")


class _A7006InstanceDataPresent_Type(Integer32):
    """Custom type a7006InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7006InstanceDataPresent_Type.__name__ = "Integer32"
_A7006InstanceDataPresent_Object = MibTableColumn
a7006InstanceDataPresent = _A7006InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 9),
    _A7006InstanceDataPresent_Type()
)
a7006InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006InstanceDataPresent.setStatus("mandatory")
_A7006EventMessage_Type = DmiDisplaystring
_A7006EventMessage_Object = MibTableColumn
a7006EventMessage = _A7006EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 10),
    _A7006EventMessage_Type()
)
a7006EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006EventMessage.setStatus("mandatory")
_A7006VendorSpecificData_Type = DmiOctetstring
_A7006VendorSpecificData_Object = MibTableColumn
a7006VendorSpecificData = _A7006VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 11),
    _A7006VendorSpecificData_Type()
)
a7006VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7006VendorSpecificData.setStatus("mandatory")
_TBusPort_Object = MibTable
tBusPort = _TBusPort_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007)
)
if mibBuilder.loadTexts:
    tBusPort.setStatus("mandatory")
_EBusPort_Object = MibTableRow
eBusPort = _EBusPort_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1)
)
eBusPort.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7007BusPortIndex"),
)
if mibBuilder.loadTexts:
    eBusPort.setStatus("mandatory")
_A7007BusPortIndex_Type = DmiInteger
_A7007BusPortIndex_Object = MibTableColumn
a7007BusPortIndex = _A7007BusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 1),
    _A7007BusPortIndex_Type()
)
a7007BusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007BusPortIndex.setStatus("mandatory")


class _A7007Protocol_Type(Integer32):
    """Custom type a7007Protocol based on Integer32"""
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
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("v1496", 8),
          ("vAnsiX3t95Fddi", 34),
          ("vAtaatapi", 6),
          ("vDiagnostic", 19),
          ("vEisa", 3),
          ("vEscon", 18),
          ("vFlexibleDiskette", 7),
          ("vHippi", 22),
          ("vI2c", 20),
          ("vIeee-488", 26),
          ("vIeee8023100basevg", 32),
          ("vIeee802310base2", 29),
          ("vIeee802310base5", 28),
          ("vIeee802310broad36", 31),
          ("vIeee80231base5", 30),
          ("vIeee8025Token-ring", 33),
          ("vIpi", 25),
          ("vIsa", 4),
          ("vMca", 35),
          ("vMultibus", 23),
          ("vOther", 1),
          ("vParallelPort", 17),
          ("vPci", 5),
          ("vPcmcia", 15),
          ("vPower", 21),
          ("vRs232", 27),
          ("vScsiFibreChannelProtocol", 10),
          ("vScsiParallelInterface", 9),
          ("vScsiSerialBusProtocol", 11),
          ("vScsiSerialBusProtocol-21394", 12),
          ("vScsiSerialStorageArchitecture", 13),
          ("vUniversalSerialBus", 16),
          ("vUnknown", 2),
          ("vVesa", 14),
          ("vVme", 24))
    )


_A7007Protocol_Type.__name__ = "Integer32"
_A7007Protocol_Object = MibTableColumn
a7007Protocol = _A7007Protocol_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 2),
    _A7007Protocol_Type()
)
a7007Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007Protocol.setStatus("mandatory")
_A7007ProtocolDescription_Type = DmiDisplaystring
_A7007ProtocolDescription_Object = MibTableColumn
a7007ProtocolDescription = _A7007ProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 3),
    _A7007ProtocolDescription_Type()
)
a7007ProtocolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007ProtocolDescription.setStatus("mandatory")


class _A7007SignalCharacteristics_Type(Integer32):
    """Custom type a7007SignalCharacteristics based on Integer32"""
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
        *(("vDifferential", 4),
          ("vLowVoltageDifferential", 5),
          ("vOptical", 6),
          ("vOther", 1),
          ("vSingleEnded", 3),
          ("vUnknown", 2))
    )


_A7007SignalCharacteristics_Type.__name__ = "Integer32"
_A7007SignalCharacteristics_Object = MibTableColumn
a7007SignalCharacteristics = _A7007SignalCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 4),
    _A7007SignalCharacteristics_Type()
)
a7007SignalCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007SignalCharacteristics.setStatus("mandatory")
_A7007AddressDescriptor_Type = DmiDisplaystring
_A7007AddressDescriptor_Object = MibTableColumn
a7007AddressDescriptor = _A7007AddressDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 5),
    _A7007AddressDescriptor_Type()
)
a7007AddressDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007AddressDescriptor.setStatus("mandatory")


class _A7007Isochronous_Type(Integer32):
    """Custom type a7007Isochronous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7007Isochronous_Type.__name__ = "Integer32"
_A7007Isochronous_Object = MibTableColumn
a7007Isochronous = _A7007Isochronous_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 6),
    _A7007Isochronous_Type()
)
a7007Isochronous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007Isochronous.setStatus("mandatory")
_A7007MaximumWidth_Type = DmiInteger
_A7007MaximumWidth_Object = MibTableColumn
a7007MaximumWidth = _A7007MaximumWidth_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 7),
    _A7007MaximumWidth_Type()
)
a7007MaximumWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007MaximumWidth.setStatus("mandatory")
_A7007MaximumTransferRate_Type = DmiInteger
_A7007MaximumTransferRate_Object = MibTableColumn
a7007MaximumTransferRate = _A7007MaximumTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 8),
    _A7007MaximumTransferRate_Type()
)
a7007MaximumTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007MaximumTransferRate.setStatus("mandatory")
_A7007MaximumNumberOfAttachments_Type = DmiInteger
_A7007MaximumNumberOfAttachments_Object = MibTableColumn
a7007MaximumNumberOfAttachments = _A7007MaximumNumberOfAttachments_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 9),
    _A7007MaximumNumberOfAttachments_Type()
)
a7007MaximumNumberOfAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007MaximumNumberOfAttachments.setStatus("mandatory")


class _A7007ConnectorType_Type(Integer32):
    """Custom type a7007ConnectorType based on Integer32"""
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
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("v13946Pins", 44),
          ("vAppleAui", 33),
          ("vAta2-12Inch44Pins", 18),
          ("vAta3-12Inch40Pins", 17),
          ("vAui", 24),
          ("vBnc", 28),
          ("vEisaSlot", 36),
          ("vFiberMic", 32),
          ("vFloppyDiskette3-12Inch", 41),
          ("vFloppyDiskette5-14Inch", 40),
          ("vGbicSocket", 43),
          ("vHssdc6Pins", 42),
          ("vIeee-488", 23),
          ("vIsaSlot", 35),
          ("vNone", 3),
          ("vOther", 1),
          ("vPcCardSlot", 39),
          ("vPciSlot", 34),
          ("vPcmciaSlot", 38),
          ("vRs23225Pin", 21),
          ("vRs422", 22),
          ("vScsiAHigh-densityShielded50Pins", 4),
          ("vScsiAHigh-densityUnshielded50Pins", 5),
          ("vScsiALow-densityShielded50Pins", 6),
          ("vScsiALow-densityUnshielded50Pins", 7),
          ("vScsiFibreChannelBnc", 16),
          ("vScsiFibreChannelDb9Copper", 12),
          ("vScsiFibreChannelFibre", 13),
          ("vScsiFibreChannelSca-ii20Pins", 15),
          ("vScsiFibreChannelSca-ii40Pins", 14),
          ("vScsiPHigh-densityShielded68Pins", 8),
          ("vScsiPHigh-densityUnshielded68Pins", 9),
          ("vScsiSca-i80Pins", 10),
          ("vScsiSca-ii80Pins", 11),
          ("vScsiVhdciShielded68Pins", 45),
          ("vSerial25Pin", 20),
          ("vSerial9Pin", 19),
          ("vStpDb9", 31),
          ("vStpRj11", 29),
          ("vStpRj45", 30),
          ("vUnknown", 2),
          ("vUptCategory3", 25),
          ("vUptCategory4", 26),
          ("vUptCategory5", 27),
          ("vVesaSlot", 37))
    )


_A7007ConnectorType_Type.__name__ = "Integer32"
_A7007ConnectorType_Object = MibTableColumn
a7007ConnectorType = _A7007ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 10),
    _A7007ConnectorType_Type()
)
a7007ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007ConnectorType.setStatus("mandatory")
_A7007ConnectorTypeDescription_Type = DmiDisplaystring
_A7007ConnectorTypeDescription_Object = MibTableColumn
a7007ConnectorTypeDescription = _A7007ConnectorTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 11),
    _A7007ConnectorTypeDescription_Type()
)
a7007ConnectorTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007ConnectorTypeDescription.setStatus("mandatory")


class _A7007ConnectorGender_Type(Integer32):
    """Custom type a7007ConnectorGender based on Integer32"""
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
        *(("vFemale", 3),
          ("vMale", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A7007ConnectorGender_Type.__name__ = "Integer32"
_A7007ConnectorGender_Object = MibTableColumn
a7007ConnectorGender = _A7007ConnectorGender_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7007, 1, 12),
    _A7007ConnectorGender_Type()
)
a7007ConnectorGender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7007ConnectorGender.setStatus("mandatory")
_TBusPortEvents_Object = MibTable
tBusPortEvents = _TBusPortEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008)
)
if mibBuilder.loadTexts:
    tBusPortEvents.setStatus("mandatory")
_EBusPortEvents_Object = MibTableRow
eBusPortEvents = _EBusPortEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1)
)
eBusPortEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eBusPortEvents.setStatus("mandatory")


class _A7008BusPortEventType_Type(Integer32):
    """Custom type a7008BusPortEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vBusPortError", 1)
    )


_A7008BusPortEventType_Type.__name__ = "Integer32"
_A7008BusPortEventType_Object = MibTableColumn
a7008BusPortEventType = _A7008BusPortEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 1),
    _A7008BusPortEventType_Type()
)
a7008BusPortEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008BusPortEventType.setStatus("mandatory")


class _A7008EventSeverity_Type(Integer32):
    """Custom type a7008EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7008EventSeverity_Type.__name__ = "Integer32"
_A7008EventSeverity_Object = MibTableColumn
a7008EventSeverity = _A7008EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 2),
    _A7008EventSeverity_Type()
)
a7008EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008EventSeverity.setStatus("mandatory")


class _A7008EventIsStateBased_Type(Integer32):
    """Custom type a7008EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7008EventIsStateBased_Type.__name__ = "Integer32"
_A7008EventIsStateBased_Object = MibTableColumn
a7008EventIsStateBased = _A7008EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 3),
    _A7008EventIsStateBased_Type()
)
a7008EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008EventIsStateBased.setStatus("mandatory")
_A7008EventStateKey_Type = DmiInteger
_A7008EventStateKey_Object = MibTableColumn
a7008EventStateKey = _A7008EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 4),
    _A7008EventStateKey_Type()
)
a7008EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008EventStateKey.setStatus("mandatory")
_A7008AssociatedGroup_Type = DmiDisplaystring
_A7008AssociatedGroup_Object = MibTableColumn
a7008AssociatedGroup = _A7008AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 5),
    _A7008AssociatedGroup_Type()
)
a7008AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008AssociatedGroup.setStatus("mandatory")


class _A7008EventSystem_Type(Integer32):
    """Custom type a7008EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7008EventSystem_Type.__name__ = "Integer32"
_A7008EventSystem_Object = MibTableColumn
a7008EventSystem = _A7008EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 6),
    _A7008EventSystem_Type()
)
a7008EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008EventSystem.setStatus("mandatory")


class _A7008EventSubsystem_Type(Integer32):
    """Custom type a7008EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7008EventSubsystem_Type.__name__ = "Integer32"
_A7008EventSubsystem_Object = MibTableColumn
a7008EventSubsystem = _A7008EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 7),
    _A7008EventSubsystem_Type()
)
a7008EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008EventSubsystem.setStatus("mandatory")


class _A7008EventSolution_Type(Integer32):
    """Custom type a7008EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7008EventSolution_Type.__name__ = "Integer32"
_A7008EventSolution_Object = MibTableColumn
a7008EventSolution = _A7008EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 8),
    _A7008EventSolution_Type()
)
a7008EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008EventSolution.setStatus("mandatory")


class _A7008InstanceDataPresent_Type(Integer32):
    """Custom type a7008InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7008InstanceDataPresent_Type.__name__ = "Integer32"
_A7008InstanceDataPresent_Object = MibTableColumn
a7008InstanceDataPresent = _A7008InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 9),
    _A7008InstanceDataPresent_Type()
)
a7008InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008InstanceDataPresent.setStatus("mandatory")
_A7008EventMessage_Type = DmiDisplaystring
_A7008EventMessage_Object = MibTableColumn
a7008EventMessage = _A7008EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 10),
    _A7008EventMessage_Type()
)
a7008EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008EventMessage.setStatus("mandatory")
_A7008VendorSpecificData_Type = DmiOctetstring
_A7008VendorSpecificData_Object = MibTableColumn
a7008VendorSpecificData = _A7008VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 11),
    _A7008VendorSpecificData_Type()
)
a7008VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7008VendorSpecificData.setStatus("mandatory")
_TAggregatePhysicalExtent_Object = MibTable
tAggregatePhysicalExtent = _TAggregatePhysicalExtent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7009)
)
if mibBuilder.loadTexts:
    tAggregatePhysicalExtent.setStatus("mandatory")
_EAggregatePhysicalExtent_Object = MibTableRow
eAggregatePhysicalExtent = _EAggregatePhysicalExtent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7009, 1)
)
eAggregatePhysicalExtent.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7009AggregatePhysicalExtentIndex"),
)
if mibBuilder.loadTexts:
    eAggregatePhysicalExtent.setStatus("mandatory")
_A7009AggregatePhysicalExtentIndex_Type = DmiInteger
_A7009AggregatePhysicalExtentIndex_Object = MibTableColumn
a7009AggregatePhysicalExtentIndex = _A7009AggregatePhysicalExtentIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7009, 1, 1),
    _A7009AggregatePhysicalExtentIndex_Type()
)
a7009AggregatePhysicalExtentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7009AggregatePhysicalExtentIndex.setStatus("mandatory")
_A7009NumberOfBlocks_Type = DmiInteger64X
_A7009NumberOfBlocks_Object = MibTableColumn
a7009NumberOfBlocks = _A7009NumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7009, 1, 2),
    _A7009NumberOfBlocks_Type()
)
a7009NumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7009NumberOfBlocks.setStatus("mandatory")
_A7009NumberOfBlocksOfCheckData_Type = DmiInteger64X
_A7009NumberOfBlocksOfCheckData_Object = MibTableColumn
a7009NumberOfBlocksOfCheckData = _A7009NumberOfBlocksOfCheckData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7009, 1, 3),
    _A7009NumberOfBlocksOfCheckData_Type()
)
a7009NumberOfBlocksOfCheckData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7009NumberOfBlocksOfCheckData.setStatus("mandatory")
_TAggregateProtectedSpaceExtent_Object = MibTable
tAggregateProtectedSpaceExtent = _TAggregateProtectedSpaceExtent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7010)
)
if mibBuilder.loadTexts:
    tAggregateProtectedSpaceExtent.setStatus("mandatory")
_EAggregateProtectedSpaceExtent_Object = MibTableRow
eAggregateProtectedSpaceExtent = _EAggregateProtectedSpaceExtent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7010, 1)
)
eAggregateProtectedSpaceExtent.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7010AggregateProtectedSpaceExtentIndex"),
)
if mibBuilder.loadTexts:
    eAggregateProtectedSpaceExtent.setStatus("mandatory")
_A7010AggregateProtectedSpaceExtentIndex_Type = DmiInteger
_A7010AggregateProtectedSpaceExtentIndex_Object = MibTableColumn
a7010AggregateProtectedSpaceExtentIndex = _A7010AggregateProtectedSpaceExtentIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7010, 1, 1),
    _A7010AggregateProtectedSpaceExtentIndex_Type()
)
a7010AggregateProtectedSpaceExtentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7010AggregateProtectedSpaceExtentIndex.setStatus("mandatory")
_A7010NumberOfBlocks_Type = DmiInteger64X
_A7010NumberOfBlocks_Object = MibTableColumn
a7010NumberOfBlocks = _A7010NumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7010, 1, 2),
    _A7010NumberOfBlocks_Type()
)
a7010NumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7010NumberOfBlocks.setStatus("mandatory")
_TVolumeSet_Object = MibTable
tVolumeSet = _TVolumeSet_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7011)
)
if mibBuilder.loadTexts:
    tVolumeSet.setStatus("mandatory")
_EVolumeSet_Object = MibTableRow
eVolumeSet = _EVolumeSet_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7011, 1)
)
eVolumeSet.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"),
)
if mibBuilder.loadTexts:
    eVolumeSet.setStatus("mandatory")
_A7011VolumeSetIndex_Type = DmiInteger
_A7011VolumeSetIndex_Object = MibTableColumn
a7011VolumeSetIndex = _A7011VolumeSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7011, 1, 1),
    _A7011VolumeSetIndex_Type()
)
a7011VolumeSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7011VolumeSetIndex.setStatus("mandatory")
_A7011Name_Type = DmiDisplaystring
_A7011Name_Object = MibTableColumn
a7011Name = _A7011Name_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7011, 1, 2),
    _A7011Name_Type()
)
a7011Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7011Name.setStatus("mandatory")
_A7011TotalStorageCapacity_Type = DmiInteger64X
_A7011TotalStorageCapacity_Object = MibTableColumn
a7011TotalStorageCapacity = _A7011TotalStorageCapacity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7011, 1, 3),
    _A7011TotalStorageCapacity_Type()
)
a7011TotalStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7011TotalStorageCapacity.setStatus("mandatory")
_A7011ProtectedSpaceStripeLength_Type = DmiInteger64X
_A7011ProtectedSpaceStripeLength_Object = MibTableColumn
a7011ProtectedSpaceStripeLength = _A7011ProtectedSpaceStripeLength_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7011, 1, 4),
    _A7011ProtectedSpaceStripeLength_Type()
)
a7011ProtectedSpaceStripeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7011ProtectedSpaceStripeLength.setStatus("mandatory")
_A7011ProtectedSpaceExtentInterleaveDepth_Type = DmiInteger64X
_A7011ProtectedSpaceExtentInterleaveDepth_Object = MibTableColumn
a7011ProtectedSpaceExtentInterleaveDepth = _A7011ProtectedSpaceExtentInterleaveDepth_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7011, 1, 5),
    _A7011ProtectedSpaceExtentInterleaveDepth_Type()
)
a7011ProtectedSpaceExtentInterleaveDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7011ProtectedSpaceExtentInterleaveDepth.setStatus("mandatory")
_TVolumeSetEvents_Object = MibTable
tVolumeSetEvents = _TVolumeSetEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012)
)
if mibBuilder.loadTexts:
    tVolumeSetEvents.setStatus("mandatory")
_EVolumeSetEvents_Object = MibTableRow
eVolumeSetEvents = _EVolumeSetEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1)
)
eVolumeSetEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eVolumeSetEvents.setStatus("mandatory")


class _A7012VolumeSetEventType_Type(Integer32):
    """Custom type a7012VolumeSetEventType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("vCioEvent", 9),
          ("vProtectionDisabled", 3),
          ("vRebuildInProgress", 2),
          ("vRecalculateActive", 5),
          ("vSpareInUse", 6),
          ("vVerifyInProgress", 7),
          ("vVolumeSetBroken", 8),
          ("vVolumeSetExposed", 1),
          ("vVolumeSetReadying", 4))
    )


_A7012VolumeSetEventType_Type.__name__ = "Integer32"
_A7012VolumeSetEventType_Object = MibTableColumn
a7012VolumeSetEventType = _A7012VolumeSetEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 1),
    _A7012VolumeSetEventType_Type()
)
a7012VolumeSetEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012VolumeSetEventType.setStatus("mandatory")


class _A7012EventSeverity_Type(Integer32):
    """Custom type a7012EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7012EventSeverity_Type.__name__ = "Integer32"
_A7012EventSeverity_Object = MibTableColumn
a7012EventSeverity = _A7012EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 2),
    _A7012EventSeverity_Type()
)
a7012EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012EventSeverity.setStatus("mandatory")


class _A7012EventIsStateBased_Type(Integer32):
    """Custom type a7012EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7012EventIsStateBased_Type.__name__ = "Integer32"
_A7012EventIsStateBased_Object = MibTableColumn
a7012EventIsStateBased = _A7012EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 3),
    _A7012EventIsStateBased_Type()
)
a7012EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012EventIsStateBased.setStatus("mandatory")
_A7012EventStateKey_Type = DmiInteger
_A7012EventStateKey_Object = MibTableColumn
a7012EventStateKey = _A7012EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 4),
    _A7012EventStateKey_Type()
)
a7012EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012EventStateKey.setStatus("mandatory")
_A7012AssociatedGroup_Type = DmiDisplaystring
_A7012AssociatedGroup_Object = MibTableColumn
a7012AssociatedGroup = _A7012AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 5),
    _A7012AssociatedGroup_Type()
)
a7012AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012AssociatedGroup.setStatus("mandatory")


class _A7012EventSystem_Type(Integer32):
    """Custom type a7012EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7012EventSystem_Type.__name__ = "Integer32"
_A7012EventSystem_Object = MibTableColumn
a7012EventSystem = _A7012EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 6),
    _A7012EventSystem_Type()
)
a7012EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012EventSystem.setStatus("mandatory")


class _A7012EventSubsystem_Type(Integer32):
    """Custom type a7012EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7012EventSubsystem_Type.__name__ = "Integer32"
_A7012EventSubsystem_Object = MibTableColumn
a7012EventSubsystem = _A7012EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 7),
    _A7012EventSubsystem_Type()
)
a7012EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012EventSubsystem.setStatus("mandatory")


class _A7012EventSolution_Type(Integer32):
    """Custom type a7012EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7012EventSolution_Type.__name__ = "Integer32"
_A7012EventSolution_Object = MibTableColumn
a7012EventSolution = _A7012EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 8),
    _A7012EventSolution_Type()
)
a7012EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012EventSolution.setStatus("mandatory")


class _A7012InstanceDataPresent_Type(Integer32):
    """Custom type a7012InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7012InstanceDataPresent_Type.__name__ = "Integer32"
_A7012InstanceDataPresent_Object = MibTableColumn
a7012InstanceDataPresent = _A7012InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 9),
    _A7012InstanceDataPresent_Type()
)
a7012InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012InstanceDataPresent.setStatus("mandatory")
_A7012EventMessage_Type = DmiDisplaystring
_A7012EventMessage_Object = MibTableColumn
a7012EventMessage = _A7012EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 10),
    _A7012EventMessage_Type()
)
a7012EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012EventMessage.setStatus("mandatory")
_A7012VendorSpecificData_Type = DmiOctetstring
_A7012VendorSpecificData_Object = MibTableColumn
a7012VendorSpecificData = _A7012VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 11),
    _A7012VendorSpecificData_Type()
)
a7012VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7012VendorSpecificData.setStatus("mandatory")
_TVolumeSetActivityEvents_Object = MibTable
tVolumeSetActivityEvents = _TVolumeSetActivityEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013)
)
if mibBuilder.loadTexts:
    tVolumeSetActivityEvents.setStatus("mandatory")
_EVolumeSetActivityEvents_Object = MibTableRow
eVolumeSetActivityEvents = _EVolumeSetActivityEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1)
)
eVolumeSetActivityEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eVolumeSetActivityEvents.setStatus("mandatory")


class _A7013VolumeSetEventType_Type(Integer32):
    """Custom type a7013VolumeSetEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vCioEvent", 1)
    )


_A7013VolumeSetEventType_Type.__name__ = "Integer32"
_A7013VolumeSetEventType_Object = MibTableColumn
a7013VolumeSetEventType = _A7013VolumeSetEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 1),
    _A7013VolumeSetEventType_Type()
)
a7013VolumeSetEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013VolumeSetEventType.setStatus("mandatory")


class _A7013EventSeverity_Type(Integer32):
    """Custom type a7013EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7013EventSeverity_Type.__name__ = "Integer32"
_A7013EventSeverity_Object = MibTableColumn
a7013EventSeverity = _A7013EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 2),
    _A7013EventSeverity_Type()
)
a7013EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013EventSeverity.setStatus("mandatory")


class _A7013EventIsStateBased_Type(Integer32):
    """Custom type a7013EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7013EventIsStateBased_Type.__name__ = "Integer32"
_A7013EventIsStateBased_Object = MibTableColumn
a7013EventIsStateBased = _A7013EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 3),
    _A7013EventIsStateBased_Type()
)
a7013EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013EventIsStateBased.setStatus("mandatory")
_A7013EventStateKey_Type = DmiInteger
_A7013EventStateKey_Object = MibTableColumn
a7013EventStateKey = _A7013EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 4),
    _A7013EventStateKey_Type()
)
a7013EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013EventStateKey.setStatus("mandatory")
_A7013AssociatedGroup_Type = DmiDisplaystring
_A7013AssociatedGroup_Object = MibTableColumn
a7013AssociatedGroup = _A7013AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 5),
    _A7013AssociatedGroup_Type()
)
a7013AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013AssociatedGroup.setStatus("mandatory")


class _A7013EventSystem_Type(Integer32):
    """Custom type a7013EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7013EventSystem_Type.__name__ = "Integer32"
_A7013EventSystem_Object = MibTableColumn
a7013EventSystem = _A7013EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 6),
    _A7013EventSystem_Type()
)
a7013EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013EventSystem.setStatus("mandatory")


class _A7013EventSubsystem_Type(Integer32):
    """Custom type a7013EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7013EventSubsystem_Type.__name__ = "Integer32"
_A7013EventSubsystem_Object = MibTableColumn
a7013EventSubsystem = _A7013EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 7),
    _A7013EventSubsystem_Type()
)
a7013EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013EventSubsystem.setStatus("mandatory")


class _A7013EventSolution_Type(Integer32):
    """Custom type a7013EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7013EventSolution_Type.__name__ = "Integer32"
_A7013EventSolution_Object = MibTableColumn
a7013EventSolution = _A7013EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 8),
    _A7013EventSolution_Type()
)
a7013EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013EventSolution.setStatus("mandatory")


class _A7013InstanceDataPresent_Type(Integer32):
    """Custom type a7013InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7013InstanceDataPresent_Type.__name__ = "Integer32"
_A7013InstanceDataPresent_Object = MibTableColumn
a7013InstanceDataPresent = _A7013InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 9),
    _A7013InstanceDataPresent_Type()
)
a7013InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013InstanceDataPresent.setStatus("mandatory")
_A7013EventMessage_Type = DmiDisplaystring
_A7013EventMessage_Object = MibTableColumn
a7013EventMessage = _A7013EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 10),
    _A7013EventMessage_Type()
)
a7013EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013EventMessage.setStatus("mandatory")
_A7013VendorSpecificData_Type = DmiOctetstring
_A7013VendorSpecificData_Object = MibTableColumn
a7013VendorSpecificData = _A7013VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 11),
    _A7013VendorSpecificData_Type()
)
a7013VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7013VendorSpecificData.setStatus("mandatory")
_TRedundancyGroup_Object = MibTable
tRedundancyGroup = _TRedundancyGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7014)
)
if mibBuilder.loadTexts:
    tRedundancyGroup.setStatus("mandatory")
_ERedundancyGroup_Object = MibTableRow
eRedundancyGroup = _ERedundancyGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7014, 1)
)
eRedundancyGroup.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7014RedundancyGroupIndex"),
)
if mibBuilder.loadTexts:
    eRedundancyGroup.setStatus("mandatory")
_A7014RedundancyGroupIndex_Type = DmiInteger
_A7014RedundancyGroupIndex_Object = MibTableColumn
a7014RedundancyGroupIndex = _A7014RedundancyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7014, 1, 1),
    _A7014RedundancyGroupIndex_Type()
)
a7014RedundancyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7014RedundancyGroupIndex.setStatus("mandatory")


class _A7014RedundancyType_Type(Integer32):
    """Custom type a7014RedundancyType based on Integer32"""
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
        *(("vCopy", 3),
          ("vNone", 0),
          ("vOther", 1),
          ("vPplusq", 5),
          ("vPpluss", 7),
          ("vS", 6),
          ("vUnknown", 2),
          ("vXor", 4))
    )


_A7014RedundancyType_Type.__name__ = "Integer32"
_A7014RedundancyType_Object = MibTableColumn
a7014RedundancyType = _A7014RedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7014, 1, 2),
    _A7014RedundancyType_Type()
)
a7014RedundancyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7014RedundancyType.setStatus("mandatory")
_TRedundancyGroupEvents_Object = MibTable
tRedundancyGroupEvents = _TRedundancyGroupEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015)
)
if mibBuilder.loadTexts:
    tRedundancyGroupEvents.setStatus("mandatory")
_ERedundancyGroupEvents_Object = MibTableRow
eRedundancyGroupEvents = _ERedundancyGroupEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1)
)
eRedundancyGroupEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eRedundancyGroupEvents.setStatus("mandatory")


class _A7015RedundancyGroupEventType_Type(Integer32):
    """Custom type a7015RedundancyGroupEventType based on Integer32"""
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
        *(("vProtectionDisabled", 3),
          ("vRebuildInProgress", 2),
          ("vRecalculationActive", 4),
          ("vRedundancyGroupExposed", 1),
          ("vVerifyInProgress", 5))
    )


_A7015RedundancyGroupEventType_Type.__name__ = "Integer32"
_A7015RedundancyGroupEventType_Object = MibTableColumn
a7015RedundancyGroupEventType = _A7015RedundancyGroupEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 1),
    _A7015RedundancyGroupEventType_Type()
)
a7015RedundancyGroupEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015RedundancyGroupEventType.setStatus("mandatory")


class _A7015EventSeverity_Type(Integer32):
    """Custom type a7015EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7015EventSeverity_Type.__name__ = "Integer32"
_A7015EventSeverity_Object = MibTableColumn
a7015EventSeverity = _A7015EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 2),
    _A7015EventSeverity_Type()
)
a7015EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015EventSeverity.setStatus("mandatory")


class _A7015EventIsStateBased_Type(Integer32):
    """Custom type a7015EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7015EventIsStateBased_Type.__name__ = "Integer32"
_A7015EventIsStateBased_Object = MibTableColumn
a7015EventIsStateBased = _A7015EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 3),
    _A7015EventIsStateBased_Type()
)
a7015EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015EventIsStateBased.setStatus("mandatory")
_A7015EventStateKey_Type = DmiInteger
_A7015EventStateKey_Object = MibTableColumn
a7015EventStateKey = _A7015EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 4),
    _A7015EventStateKey_Type()
)
a7015EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015EventStateKey.setStatus("mandatory")
_A7015AssociatedGroup_Type = DmiDisplaystring
_A7015AssociatedGroup_Object = MibTableColumn
a7015AssociatedGroup = _A7015AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 5),
    _A7015AssociatedGroup_Type()
)
a7015AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015AssociatedGroup.setStatus("mandatory")


class _A7015EventSystem_Type(Integer32):
    """Custom type a7015EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7015EventSystem_Type.__name__ = "Integer32"
_A7015EventSystem_Object = MibTableColumn
a7015EventSystem = _A7015EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 6),
    _A7015EventSystem_Type()
)
a7015EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015EventSystem.setStatus("mandatory")


class _A7015EventSubsystem_Type(Integer32):
    """Custom type a7015EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7015EventSubsystem_Type.__name__ = "Integer32"
_A7015EventSubsystem_Object = MibTableColumn
a7015EventSubsystem = _A7015EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 7),
    _A7015EventSubsystem_Type()
)
a7015EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015EventSubsystem.setStatus("mandatory")


class _A7015EventSolution_Type(Integer32):
    """Custom type a7015EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7015EventSolution_Type.__name__ = "Integer32"
_A7015EventSolution_Object = MibTableColumn
a7015EventSolution = _A7015EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 8),
    _A7015EventSolution_Type()
)
a7015EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015EventSolution.setStatus("mandatory")


class _A7015InstanceDataPresent_Type(Integer32):
    """Custom type a7015InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7015InstanceDataPresent_Type.__name__ = "Integer32"
_A7015InstanceDataPresent_Object = MibTableColumn
a7015InstanceDataPresent = _A7015InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 9),
    _A7015InstanceDataPresent_Type()
)
a7015InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015InstanceDataPresent.setStatus("mandatory")
_A7015EventMessage_Type = DmiDisplaystring
_A7015EventMessage_Object = MibTableColumn
a7015EventMessage = _A7015EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 10),
    _A7015EventMessage_Type()
)
a7015EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015EventMessage.setStatus("mandatory")
_A7015VendorSpecificData_Type = DmiOctetstring
_A7015VendorSpecificData_Object = MibTableColumn
a7015VendorSpecificData = _A7015VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 11),
    _A7015VendorSpecificData_Type()
)
a7015VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7015VendorSpecificData.setStatus("mandatory")
_TSpareEvents_Object = MibTable
tSpareEvents = _TSpareEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016)
)
if mibBuilder.loadTexts:
    tSpareEvents.setStatus("mandatory")
_ESpareEvents_Object = MibTableRow
eSpareEvents = _ESpareEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1)
)
eSpareEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eSpareEvents.setStatus("mandatory")


class _A7016SpareEventType_Type(Integer32):
    """Custom type a7016SpareEventType based on Integer32"""
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
        *(("vCioEvent", 4),
          ("vComponentSpareBroken", 1),
          ("vComponentSpareInUse", 2),
          ("vComponentSpareReadying", 3))
    )


_A7016SpareEventType_Type.__name__ = "Integer32"
_A7016SpareEventType_Object = MibTableColumn
a7016SpareEventType = _A7016SpareEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 1),
    _A7016SpareEventType_Type()
)
a7016SpareEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016SpareEventType.setStatus("mandatory")


class _A7016EventSeverity_Type(Integer32):
    """Custom type a7016EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7016EventSeverity_Type.__name__ = "Integer32"
_A7016EventSeverity_Object = MibTableColumn
a7016EventSeverity = _A7016EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 2),
    _A7016EventSeverity_Type()
)
a7016EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016EventSeverity.setStatus("mandatory")


class _A7016EventIsStateBased_Type(Integer32):
    """Custom type a7016EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7016EventIsStateBased_Type.__name__ = "Integer32"
_A7016EventIsStateBased_Object = MibTableColumn
a7016EventIsStateBased = _A7016EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 3),
    _A7016EventIsStateBased_Type()
)
a7016EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016EventIsStateBased.setStatus("mandatory")
_A7016EventStateKey_Type = DmiInteger
_A7016EventStateKey_Object = MibTableColumn
a7016EventStateKey = _A7016EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 4),
    _A7016EventStateKey_Type()
)
a7016EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016EventStateKey.setStatus("mandatory")
_A7016AssociatedGroup_Type = DmiDisplaystring
_A7016AssociatedGroup_Object = MibTableColumn
a7016AssociatedGroup = _A7016AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 5),
    _A7016AssociatedGroup_Type()
)
a7016AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016AssociatedGroup.setStatus("mandatory")


class _A7016EventSystem_Type(Integer32):
    """Custom type a7016EventSystem based on Integer32"""
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
        *(("vComponentSpare", 4),
          ("vDataSpare", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A7016EventSystem_Type.__name__ = "Integer32"
_A7016EventSystem_Object = MibTableColumn
a7016EventSystem = _A7016EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 6),
    _A7016EventSystem_Type()
)
a7016EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016EventSystem.setStatus("mandatory")


class _A7016EventSubsystem_Type(Integer32):
    """Custom type a7016EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7016EventSubsystem_Type.__name__ = "Integer32"
_A7016EventSubsystem_Object = MibTableColumn
a7016EventSubsystem = _A7016EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 7),
    _A7016EventSubsystem_Type()
)
a7016EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016EventSubsystem.setStatus("mandatory")


class _A7016EventSolution_Type(Integer32):
    """Custom type a7016EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7016EventSolution_Type.__name__ = "Integer32"
_A7016EventSolution_Object = MibTableColumn
a7016EventSolution = _A7016EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 8),
    _A7016EventSolution_Type()
)
a7016EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016EventSolution.setStatus("mandatory")


class _A7016InstanceDataPresent_Type(Integer32):
    """Custom type a7016InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7016InstanceDataPresent_Type.__name__ = "Integer32"
_A7016InstanceDataPresent_Object = MibTableColumn
a7016InstanceDataPresent = _A7016InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 9),
    _A7016InstanceDataPresent_Type()
)
a7016InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016InstanceDataPresent.setStatus("mandatory")
_A7016EventMessage_Type = DmiDisplaystring
_A7016EventMessage_Object = MibTableColumn
a7016EventMessage = _A7016EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 10),
    _A7016EventMessage_Type()
)
a7016EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016EventMessage.setStatus("mandatory")
_A7016VendorSpecificData_Type = DmiOctetstring
_A7016VendorSpecificData_Object = MibTableColumn
a7016VendorSpecificData = _A7016VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 11),
    _A7016VendorSpecificData_Type()
)
a7016VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7016VendorSpecificData.setStatus("mandatory")
_TMassStorageAssociation_Object = MibTable
tMassStorageAssociation = _TMassStorageAssociation_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7017)
)
if mibBuilder.loadTexts:
    tMassStorageAssociation.setStatus("mandatory")
_EMassStorageAssociation_Object = MibTableRow
eMassStorageAssociation = _EMassStorageAssociation_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7017, 1)
)
eMassStorageAssociation.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7017AssociationIndex"),
)
if mibBuilder.loadTexts:
    eMassStorageAssociation.setStatus("mandatory")
_A7017AssociationIndex_Type = DmiInteger
_A7017AssociationIndex_Object = MibTableColumn
a7017AssociationIndex = _A7017AssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7017, 1, 1),
    _A7017AssociationIndex_Type()
)
a7017AssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7017AssociationIndex.setStatus("mandatory")
_A7017Type_Type = DmiDisplaystring
_A7017Type_Object = MibTableColumn
a7017Type = _A7017Type_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7017, 1, 2),
    _A7017Type_Type()
)
a7017Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7017Type.setStatus("mandatory")
_A7017Reference1_Type = DmiDisplaystring
_A7017Reference1_Object = MibTableColumn
a7017Reference1 = _A7017Reference1_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7017, 1, 3),
    _A7017Reference1_Type()
)
a7017Reference1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7017Reference1.setStatus("mandatory")
_A7017Reference2_Type = DmiDisplaystring
_A7017Reference2_Object = MibTableColumn
a7017Reference2 = _A7017Reference2_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7017, 1, 4),
    _A7017Reference2_Type()
)
a7017Reference2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7017Reference2.setStatus("mandatory")
_TAssociationEvents_Object = MibTable
tAssociationEvents = _TAssociationEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018)
)
if mibBuilder.loadTexts:
    tAssociationEvents.setStatus("mandatory")
_EAssociationEvents_Object = MibTableRow
eAssociationEvents = _EAssociationEvents_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1)
)
eAssociationEvents.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eAssociationEvents.setStatus("mandatory")


class _A7018AssociationEventType_Type(Integer32):
    """Custom type a7018AssociationEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vExistingObjectIsGone", 3),
          ("vExistingObjectReplaced", 2),
          ("vNewObjectDetected", 1))
    )


_A7018AssociationEventType_Type.__name__ = "Integer32"
_A7018AssociationEventType_Object = MibTableColumn
a7018AssociationEventType = _A7018AssociationEventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 1),
    _A7018AssociationEventType_Type()
)
a7018AssociationEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018AssociationEventType.setStatus("mandatory")


class _A7018EventSeverity_Type(Integer32):
    """Custom type a7018EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7018EventSeverity_Type.__name__ = "Integer32"
_A7018EventSeverity_Object = MibTableColumn
a7018EventSeverity = _A7018EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 2),
    _A7018EventSeverity_Type()
)
a7018EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018EventSeverity.setStatus("mandatory")


class _A7018EventIsStateBased_Type(Integer32):
    """Custom type a7018EventIsStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7018EventIsStateBased_Type.__name__ = "Integer32"
_A7018EventIsStateBased_Object = MibTableColumn
a7018EventIsStateBased = _A7018EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 3),
    _A7018EventIsStateBased_Type()
)
a7018EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018EventIsStateBased.setStatus("mandatory")
_A7018EventStateKey_Type = DmiInteger
_A7018EventStateKey_Object = MibTableColumn
a7018EventStateKey = _A7018EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 4),
    _A7018EventStateKey_Type()
)
a7018EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018EventStateKey.setStatus("mandatory")
_A7018AssociatedGroup_Type = DmiDisplaystring
_A7018AssociatedGroup_Object = MibTableColumn
a7018AssociatedGroup = _A7018AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 5),
    _A7018AssociatedGroup_Type()
)
a7018AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018AssociatedGroup.setStatus("mandatory")


class _A7018EventSystem_Type(Integer32):
    """Custom type a7018EventSystem based on Integer32"""
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
        *(("vAggregatePhysicalExtent", 7),
          ("vAggregateProtectedSpaceExtent", 5),
          ("vBusPort", 2),
          ("vCache", 9),
          ("vPhysicalExtent", 6),
          ("vProtectedSpaceExtent", 4),
          ("vRedundancyGroup", 8),
          ("vSoftwareComponent", 10),
          ("vSoftwareSignature", 11),
          ("vStorageController", 0),
          ("vStorageDevice", 1),
          ("vVolumeSet", 3))
    )


_A7018EventSystem_Type.__name__ = "Integer32"
_A7018EventSystem_Object = MibTableColumn
a7018EventSystem = _A7018EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 6),
    _A7018EventSystem_Type()
)
a7018EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018EventSystem.setStatus("mandatory")


class _A7018EventSubsystem_Type(Integer32):
    """Custom type a7018EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A7018EventSubsystem_Type.__name__ = "Integer32"
_A7018EventSubsystem_Object = MibTableColumn
a7018EventSubsystem = _A7018EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 7),
    _A7018EventSubsystem_Type()
)
a7018EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018EventSubsystem.setStatus("mandatory")


class _A7018EventSolution_Type(Integer32):
    """Custom type a7018EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vNotProvided", 1)
    )


_A7018EventSolution_Type.__name__ = "Integer32"
_A7018EventSolution_Object = MibTableColumn
a7018EventSolution = _A7018EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 8),
    _A7018EventSolution_Type()
)
a7018EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018EventSolution.setStatus("mandatory")


class _A7018InstanceDataPresent_Type(Integer32):
    """Custom type a7018InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7018InstanceDataPresent_Type.__name__ = "Integer32"
_A7018InstanceDataPresent_Object = MibTableColumn
a7018InstanceDataPresent = _A7018InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 9),
    _A7018InstanceDataPresent_Type()
)
a7018InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018InstanceDataPresent.setStatus("mandatory")
_A7018EventMessage_Type = DmiDisplaystring
_A7018EventMessage_Object = MibTableColumn
a7018EventMessage = _A7018EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 10),
    _A7018EventMessage_Type()
)
a7018EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018EventMessage.setStatus("mandatory")
_A7018VendorSpecificData_Type = DmiOctetstring
_A7018VendorSpecificData_Object = MibTableColumn
a7018VendorSpecificData = _A7018VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 11),
    _A7018VendorSpecificData_Type()
)
a7018VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7018VendorSpecificData.setStatus("mandatory")
_TBusPortAssociation_Object = MibTable
tBusPortAssociation = _TBusPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7019)
)
if mibBuilder.loadTexts:
    tBusPortAssociation.setStatus("mandatory")
_EBusPortAssociation_Object = MibTableRow
eBusPortAssociation = _EBusPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7019, 1)
)
eBusPortAssociation.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7019BusPortAssociationIndex"),
)
if mibBuilder.loadTexts:
    eBusPortAssociation.setStatus("mandatory")
_A7019BusPortAssociationIndex_Type = DmiInteger
_A7019BusPortAssociationIndex_Object = MibTableColumn
a7019BusPortAssociationIndex = _A7019BusPortAssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7019, 1, 1),
    _A7019BusPortAssociationIndex_Type()
)
a7019BusPortAssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7019BusPortAssociationIndex.setStatus("mandatory")
_A7019NegotiatedSpeed_Type = DmiInteger
_A7019NegotiatedSpeed_Object = MibTableColumn
a7019NegotiatedSpeed = _A7019NegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7019, 1, 2),
    _A7019NegotiatedSpeed_Type()
)
a7019NegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7019NegotiatedSpeed.setStatus("mandatory")
_A7019NegotiatedWidth_Type = DmiInteger
_A7019NegotiatedWidth_Object = MibTableColumn
a7019NegotiatedWidth = _A7019NegotiatedWidth_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7019, 1, 3),
    _A7019NegotiatedWidth_Type()
)
a7019NegotiatedWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7019NegotiatedWidth.setStatus("mandatory")
_TComponentSpareAssociation_Object = MibTable
tComponentSpareAssociation = _TComponentSpareAssociation_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7020)
)
if mibBuilder.loadTexts:
    tComponentSpareAssociation.setStatus("mandatory")
_EComponentSpareAssociation_Object = MibTableRow
eComponentSpareAssociation = _EComponentSpareAssociation_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7020, 1)
)
eComponentSpareAssociation.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7020ComponentSpareIndex"),
)
if mibBuilder.loadTexts:
    eComponentSpareAssociation.setStatus("mandatory")
_A7020ComponentSpareIndex_Type = DmiInteger
_A7020ComponentSpareIndex_Object = MibTableColumn
a7020ComponentSpareIndex = _A7020ComponentSpareIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7020, 1, 1),
    _A7020ComponentSpareIndex_Type()
)
a7020ComponentSpareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7020ComponentSpareIndex.setStatus("mandatory")


class _A7020SpareFunctioningState_Type(Integer32):
    """Custom type a7020SpareFunctioningState based on Integer32"""
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
        *(("vActivestandby", 4),
          ("vActivestandbyThatInAdditionLoadBalances", 5),
          ("vInactivestandby", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A7020SpareFunctioningState_Type.__name__ = "Integer32"
_A7020SpareFunctioningState_Object = MibTableColumn
a7020SpareFunctioningState = _A7020SpareFunctioningState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7020, 1, 2),
    _A7020SpareFunctioningState_Type()
)
a7020SpareFunctioningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7020SpareFunctioningState.setStatus("mandatory")
_TWorldwideIdentifer_Object = MibTable
tWorldwideIdentifer = _TWorldwideIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7021)
)
if mibBuilder.loadTexts:
    tWorldwideIdentifer.setStatus("mandatory")
_EWorldwideIdentifer_Object = MibTableRow
eWorldwideIdentifer = _EWorldwideIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7021, 1)
)
eWorldwideIdentifer.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7021WorldwideIdentifierIndex"),
)
if mibBuilder.loadTexts:
    eWorldwideIdentifer.setStatus("mandatory")
_A7021WorldwideIdentifierIndex_Type = DmiInteger
_A7021WorldwideIdentifierIndex_Object = MibTableColumn
a7021WorldwideIdentifierIndex = _A7021WorldwideIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7021, 1, 1),
    _A7021WorldwideIdentifierIndex_Type()
)
a7021WorldwideIdentifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7021WorldwideIdentifierIndex.setStatus("mandatory")


class _A7021WorldwideIdentifierType_Type(Integer32):
    """Custom type a7021WorldwideIdentifierType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("vBinary", 7),
          ("vFc-ph64-bitName_identifier", 6),
          ("vIeeeExtendedUniqueIdentifier64-bit", 5),
          ("vLanMacAddress", 9),
          ("vNone", 3),
          ("vOther", 1),
          ("vUnicode", 8),
          ("vUnknown", 2),
          ("vVendorIdProductIdSerialNumber", 4),
          ("vWanAccessAddress", 10))
    )


_A7021WorldwideIdentifierType_Type.__name__ = "Integer32"
_A7021WorldwideIdentifierType_Object = MibTableColumn
a7021WorldwideIdentifierType = _A7021WorldwideIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7021, 1, 2),
    _A7021WorldwideIdentifierType_Type()
)
a7021WorldwideIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7021WorldwideIdentifierType.setStatus("mandatory")
_A7021WorldwideIdentifier_Type = DmiDisplaystring
_A7021WorldwideIdentifier_Object = MibTableColumn
a7021WorldwideIdentifier = _A7021WorldwideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7021, 1, 3),
    _A7021WorldwideIdentifier_Type()
)
a7021WorldwideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7021WorldwideIdentifier.setStatus("mandatory")
_TMassStorageStatistics_Object = MibTable
tMassStorageStatistics = _TMassStorageStatistics_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022)
)
if mibBuilder.loadTexts:
    tMassStorageStatistics.setStatus("mandatory")
_EMassStorageStatistics_Object = MibTableRow
eMassStorageStatistics = _EMassStorageStatistics_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1)
)
eMassStorageStatistics.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7022StatisticsIndex"),
)
if mibBuilder.loadTexts:
    eMassStorageStatistics.setStatus("mandatory")
_A7022StatisticsIndex_Type = DmiInteger
_A7022StatisticsIndex_Object = MibTableColumn
a7022StatisticsIndex = _A7022StatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 1),
    _A7022StatisticsIndex_Type()
)
a7022StatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022StatisticsIndex.setStatus("mandatory")
_A7022BlocksRead_Type = DmiCounter
_A7022BlocksRead_Object = MibTableColumn
a7022BlocksRead = _A7022BlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 2),
    _A7022BlocksRead_Type()
)
a7022BlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022BlocksRead.setStatus("mandatory")
_A7022BlocksWritten_Type = DmiCounter
_A7022BlocksWritten_Object = MibTableColumn
a7022BlocksWritten = _A7022BlocksWritten_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 3),
    _A7022BlocksWritten_Type()
)
a7022BlocksWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022BlocksWritten.setStatus("mandatory")
_A7022ReadCommandsIssued_Type = DmiCounter
_A7022ReadCommandsIssued_Object = MibTableColumn
a7022ReadCommandsIssued = _A7022ReadCommandsIssued_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 4),
    _A7022ReadCommandsIssued_Type()
)
a7022ReadCommandsIssued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022ReadCommandsIssued.setStatus("mandatory")
_A7022WriteCommandsIssued_Type = DmiCounter
_A7022WriteCommandsIssued_Object = MibTableColumn
a7022WriteCommandsIssued = _A7022WriteCommandsIssued_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 5),
    _A7022WriteCommandsIssued_Type()
)
a7022WriteCommandsIssued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022WriteCommandsIssued.setStatus("mandatory")
_A7022IoRange0Read_Type = DmiCounter
_A7022IoRange0Read_Object = MibTableColumn
a7022IoRange0Read = _A7022IoRange0Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 6),
    _A7022IoRange0Read_Type()
)
a7022IoRange0Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange0Read.setStatus("mandatory")
_A7022IoRange1Read_Type = DmiCounter
_A7022IoRange1Read_Object = MibTableColumn
a7022IoRange1Read = _A7022IoRange1Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 7),
    _A7022IoRange1Read_Type()
)
a7022IoRange1Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange1Read.setStatus("mandatory")
_A7022IoRange2Read_Type = DmiCounter
_A7022IoRange2Read_Object = MibTableColumn
a7022IoRange2Read = _A7022IoRange2Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 8),
    _A7022IoRange2Read_Type()
)
a7022IoRange2Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange2Read.setStatus("mandatory")
_A7022IoRange3Read_Type = DmiCounter
_A7022IoRange3Read_Object = MibTableColumn
a7022IoRange3Read = _A7022IoRange3Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 9),
    _A7022IoRange3Read_Type()
)
a7022IoRange3Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange3Read.setStatus("mandatory")
_A7022IoRange4Read_Type = DmiCounter
_A7022IoRange4Read_Object = MibTableColumn
a7022IoRange4Read = _A7022IoRange4Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 10),
    _A7022IoRange4Read_Type()
)
a7022IoRange4Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange4Read.setStatus("mandatory")
_A7022IoRange5Read_Type = DmiCounter
_A7022IoRange5Read_Object = MibTableColumn
a7022IoRange5Read = _A7022IoRange5Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 11),
    _A7022IoRange5Read_Type()
)
a7022IoRange5Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange5Read.setStatus("mandatory")
_A7022IoRange6Read_Type = DmiCounter
_A7022IoRange6Read_Object = MibTableColumn
a7022IoRange6Read = _A7022IoRange6Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 12),
    _A7022IoRange6Read_Type()
)
a7022IoRange6Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange6Read.setStatus("mandatory")
_A7022IoRange7Read_Type = DmiCounter
_A7022IoRange7Read_Object = MibTableColumn
a7022IoRange7Read = _A7022IoRange7Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 13),
    _A7022IoRange7Read_Type()
)
a7022IoRange7Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange7Read.setStatus("mandatory")
_A7022IoRange8Read_Type = DmiCounter
_A7022IoRange8Read_Object = MibTableColumn
a7022IoRange8Read = _A7022IoRange8Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 14),
    _A7022IoRange8Read_Type()
)
a7022IoRange8Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange8Read.setStatus("mandatory")
_A7022IoRange9Read_Type = DmiCounter
_A7022IoRange9Read_Object = MibTableColumn
a7022IoRange9Read = _A7022IoRange9Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 15),
    _A7022IoRange9Read_Type()
)
a7022IoRange9Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange9Read.setStatus("mandatory")
_A7022IoRange10Read_Type = DmiCounter
_A7022IoRange10Read_Object = MibTableColumn
a7022IoRange10Read = _A7022IoRange10Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 16),
    _A7022IoRange10Read_Type()
)
a7022IoRange10Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange10Read.setStatus("mandatory")
_A7022IoRange11Read_Type = DmiCounter
_A7022IoRange11Read_Object = MibTableColumn
a7022IoRange11Read = _A7022IoRange11Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 17),
    _A7022IoRange11Read_Type()
)
a7022IoRange11Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange11Read.setStatus("mandatory")
_A7022IoRange12Read_Type = DmiCounter
_A7022IoRange12Read_Object = MibTableColumn
a7022IoRange12Read = _A7022IoRange12Read_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 18),
    _A7022IoRange12Read_Type()
)
a7022IoRange12Read.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange12Read.setStatus("mandatory")
_A7022IoRange0Written_Type = DmiCounter
_A7022IoRange0Written_Object = MibTableColumn
a7022IoRange0Written = _A7022IoRange0Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 19),
    _A7022IoRange0Written_Type()
)
a7022IoRange0Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange0Written.setStatus("mandatory")
_A7022IoRange1Written_Type = DmiCounter
_A7022IoRange1Written_Object = MibTableColumn
a7022IoRange1Written = _A7022IoRange1Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 20),
    _A7022IoRange1Written_Type()
)
a7022IoRange1Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange1Written.setStatus("mandatory")
_A7022IoRange2Written_Type = DmiCounter
_A7022IoRange2Written_Object = MibTableColumn
a7022IoRange2Written = _A7022IoRange2Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 21),
    _A7022IoRange2Written_Type()
)
a7022IoRange2Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange2Written.setStatus("mandatory")
_A7022IoRange3Written_Type = DmiCounter
_A7022IoRange3Written_Object = MibTableColumn
a7022IoRange3Written = _A7022IoRange3Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 22),
    _A7022IoRange3Written_Type()
)
a7022IoRange3Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange3Written.setStatus("mandatory")
_A7022IoRange4Written_Type = DmiCounter
_A7022IoRange4Written_Object = MibTableColumn
a7022IoRange4Written = _A7022IoRange4Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 23),
    _A7022IoRange4Written_Type()
)
a7022IoRange4Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange4Written.setStatus("mandatory")
_A7022IoRange5Written_Type = DmiCounter
_A7022IoRange5Written_Object = MibTableColumn
a7022IoRange5Written = _A7022IoRange5Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 24),
    _A7022IoRange5Written_Type()
)
a7022IoRange5Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange5Written.setStatus("mandatory")
_A7022IoRange6Written_Type = DmiCounter
_A7022IoRange6Written_Object = MibTableColumn
a7022IoRange6Written = _A7022IoRange6Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 25),
    _A7022IoRange6Written_Type()
)
a7022IoRange6Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange6Written.setStatus("mandatory")
_A7022IoRange7Written_Type = DmiCounter
_A7022IoRange7Written_Object = MibTableColumn
a7022IoRange7Written = _A7022IoRange7Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 26),
    _A7022IoRange7Written_Type()
)
a7022IoRange7Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange7Written.setStatus("mandatory")
_A7022IoRange8Written_Type = DmiCounter
_A7022IoRange8Written_Object = MibTableColumn
a7022IoRange8Written = _A7022IoRange8Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 27),
    _A7022IoRange8Written_Type()
)
a7022IoRange8Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange8Written.setStatus("mandatory")
_A7022IoRange9Written_Type = DmiCounter
_A7022IoRange9Written_Object = MibTableColumn
a7022IoRange9Written = _A7022IoRange9Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 28),
    _A7022IoRange9Written_Type()
)
a7022IoRange9Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange9Written.setStatus("mandatory")
_A7022IoRange10Written_Type = DmiCounter
_A7022IoRange10Written_Object = MibTableColumn
a7022IoRange10Written = _A7022IoRange10Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 29),
    _A7022IoRange10Written_Type()
)
a7022IoRange10Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange10Written.setStatus("mandatory")
_A7022IoRange11Written_Type = DmiCounter
_A7022IoRange11Written_Object = MibTableColumn
a7022IoRange11Written = _A7022IoRange11Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 30),
    _A7022IoRange11Written_Type()
)
a7022IoRange11Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange11Written.setStatus("mandatory")
_A7022IoRange12Written_Type = DmiCounter
_A7022IoRange12Written_Object = MibTableColumn
a7022IoRange12Written = _A7022IoRange12Written_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7022, 1, 31),
    _A7022IoRange12Written_Type()
)
a7022IoRange12Written.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7022IoRange12Written.setStatus("mandatory")
_TOverallStatus_Object = MibTable
tOverallStatus = _TOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7023)
)
if mibBuilder.loadTexts:
    tOverallStatus.setStatus("mandatory")
_EOverallStatus_Object = MibTableRow
eOverallStatus = _EOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7023, 1)
)
eOverallStatus.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eOverallStatus.setStatus("mandatory")


class _A7023OverallStatus_Type(Integer32):
    """Custom type a7023OverallStatus based on Integer32"""
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
        *(("vFailure", 3),
          ("vOk", 1),
          ("vOther", 5),
          ("vUnknown", 4),
          ("vWarning", 2))
    )


_A7023OverallStatus_Type.__name__ = "Integer32"
_A7023OverallStatus_Object = MibTableColumn
a7023OverallStatus = _A7023OverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7023, 1, 1),
    _A7023OverallStatus_Type()
)
a7023OverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7023OverallStatus.setStatus("mandatory")
_TOperationalState_Object = MibTable
tOperationalState = _TOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024)
)
if mibBuilder.loadTexts:
    tOperationalState.setStatus("mandatory")
_EOperationalState_Object = MibTableRow
eOperationalState = _EOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1)
)
eOperationalState.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7024OperationalStateIndex"),
)
if mibBuilder.loadTexts:
    eOperationalState.setStatus("mandatory")
_A7024OperationalStateIndex_Type = DmiInteger
_A7024OperationalStateIndex_Object = MibTableColumn
a7024OperationalStateIndex = _A7024OperationalStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 1),
    _A7024OperationalStateIndex_Type()
)
a7024OperationalStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024OperationalStateIndex.setStatus("mandatory")
_A7024DeviceGroupIndex_Type = DmiInteger
_A7024DeviceGroupIndex_Object = MibTableColumn
a7024DeviceGroupIndex = _A7024DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 2),
    _A7024DeviceGroupIndex_Type()
)
a7024DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024DeviceGroupIndex.setStatus("mandatory")


class _A7024OperationalStatus_Type(Integer32):
    """Custom type a7024OperationalStatus based on Integer32"""
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
        *(("vDisabled", 4),
          ("vEnabled", 3),
          ("vNotApplicable", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A7024OperationalStatus_Type.__name__ = "Integer32"
_A7024OperationalStatus_Object = MibTableColumn
a7024OperationalStatus = _A7024OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 3),
    _A7024OperationalStatus_Type()
)
a7024OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024OperationalStatus.setStatus("mandatory")


class _A7024UsageState_Type(Integer32):
    """Custom type a7024UsageState based on Integer32"""
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
        *(("vActive", 4),
          ("vBusy", 5),
          ("vIdle", 3),
          ("vNotApplicable", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A7024UsageState_Type.__name__ = "Integer32"
_A7024UsageState_Object = MibTableColumn
a7024UsageState = _A7024UsageState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 4),
    _A7024UsageState_Type()
)
a7024UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024UsageState.setStatus("mandatory")


class _A7024AvailabilityStatus_Type(Integer32):
    """Custom type a7024AvailabilityStatus based on Integer32"""
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
        *(("vDegraded", 10),
          ("vInTest", 5),
          ("vInstallError", 12),
          ("vNotApplicable", 6),
          ("vNotInstalled", 11),
          ("vOffDuty", 9),
          ("vOffLine", 8),
          ("vOther", 1),
          ("vPowerOff", 7),
          ("vPowerSave", 13),
          ("vRunning", 3),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A7024AvailabilityStatus_Type.__name__ = "Integer32"
_A7024AvailabilityStatus_Object = MibTableColumn
a7024AvailabilityStatus = _A7024AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 5),
    _A7024AvailabilityStatus_Type()
)
a7024AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024AvailabilityStatus.setStatus("mandatory")


class _A7024AdministrativeState_Type(Integer32):
    """Custom type a7024AdministrativeState based on Integer32"""
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
        *(("vLocked", 3),
          ("vNotApplicable", 5),
          ("vOther", 1),
          ("vShuttingDown", 6),
          ("vUnknown", 2),
          ("vUnlocked", 4))
    )


_A7024AdministrativeState_Type.__name__ = "Integer32"
_A7024AdministrativeState_Object = MibTableColumn
a7024AdministrativeState = _A7024AdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 6),
    _A7024AdministrativeState_Type()
)
a7024AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024AdministrativeState.setStatus("mandatory")
_A7024FatalErrorCount_Type = DmiCounter
_A7024FatalErrorCount_Object = MibTableColumn
a7024FatalErrorCount = _A7024FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 7),
    _A7024FatalErrorCount_Type()
)
a7024FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024FatalErrorCount.setStatus("mandatory")
_A7024MajorErrorCount_Type = DmiCounter
_A7024MajorErrorCount_Object = MibTableColumn
a7024MajorErrorCount = _A7024MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 8),
    _A7024MajorErrorCount_Type()
)
a7024MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024MajorErrorCount.setStatus("mandatory")
_A7024WarningErrorCount_Type = DmiCounter
_A7024WarningErrorCount_Object = MibTableColumn
a7024WarningErrorCount = _A7024WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 9),
    _A7024WarningErrorCount_Type()
)
a7024WarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024WarningErrorCount.setStatus("mandatory")


class _A7024CurrentErrorStatus_Type(Integer32):
    """Custom type a7024CurrentErrorStatus based on Integer32"""
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
        *(("vCritical", 5),
          ("vNon-critical1", 4),
          ("vNon-recoverable1", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A7024CurrentErrorStatus_Type.__name__ = "Integer32"
_A7024CurrentErrorStatus_Object = MibTableColumn
a7024CurrentErrorStatus = _A7024CurrentErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 10),
    _A7024CurrentErrorStatus_Type()
)
a7024CurrentErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024CurrentErrorStatus.setStatus("mandatory")


class _A7024DevicePredictedFailureStatus_Type(Integer32):
    """Custom type a7024DevicePredictedFailureStatus based on Integer32"""
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
        *(("vDeviceFailurePredictedByTheDevice", 5),
          ("vMediaFailurePredictedByTheDevice", 6),
          ("vNoFailurePredictedByTheDevice", 4),
          ("vNotSupportedByThisDevice", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A7024DevicePredictedFailureStatus_Type.__name__ = "Integer32"
_A7024DevicePredictedFailureStatus_Object = MibTableColumn
a7024DevicePredictedFailureStatus = _A7024DevicePredictedFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7024, 1, 11),
    _A7024DevicePredictedFailureStatus_Type()
)
a7024DevicePredictedFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7024DevicePredictedFailureStatus.setStatus("mandatory")
_TEventLogCount_Object = MibTable
tEventLogCount = _TEventLogCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7025)
)
if mibBuilder.loadTexts:
    tEventLogCount.setStatus("mandatory")
_EEventLogCount_Object = MibTableRow
eEventLogCount = _EEventLogCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7025, 1)
)
eEventLogCount.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eEventLogCount.setStatus("mandatory")
_A7025EventLogCount_Type = DmiInteger
_A7025EventLogCount_Object = MibTableColumn
a7025EventLogCount = _A7025EventLogCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7025, 1, 1),
    _A7025EventLogCount_Type()
)
a7025EventLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7025EventLogCount.setStatus("mandatory")
_TEventLog_Object = MibTable
tEventLog = _TEventLog_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7026)
)
if mibBuilder.loadTexts:
    tEventLog.setStatus("mandatory")
_EEventLog_Object = MibTableRow
eEventLog = _EEventLog_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7026, 1)
)
eEventLog.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7026EventLogIndex"),
)
if mibBuilder.loadTexts:
    eEventLog.setStatus("mandatory")
_A7026EventLogIndex_Type = DmiInteger
_A7026EventLogIndex_Object = MibTableColumn
a7026EventLogIndex = _A7026EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7026, 1, 1),
    _A7026EventLogIndex_Type()
)
a7026EventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7026EventLogIndex.setStatus("mandatory")
_A7026EventLogEntry_Type = DmiDisplaystring
_A7026EventLogEntry_Object = MibTableColumn
a7026EventLogEntry = _A7026EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7026, 1, 2),
    _A7026EventLogEntry_Type()
)
a7026EventLogEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7026EventLogEntry.setStatus("mandatory")
_A7026EventLogTimestamp_Type = DmiInteger
_A7026EventLogTimestamp_Object = MibTableColumn
a7026EventLogTimestamp = _A7026EventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7026, 1, 3),
    _A7026EventLogTimestamp_Type()
)
a7026EventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7026EventLogTimestamp.setStatus("mandatory")
_TEventState_Object = MibTable
tEventState = _TEventState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7027)
)
if mibBuilder.loadTexts:
    tEventState.setStatus("mandatory")
_EEventState_Object = MibTableRow
eEventState = _EEventState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7027, 1)
)
eEventState.setIndexNames(
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "DmiComponentIndex"),
    (0, "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7027EventStateIndex"),
)
if mibBuilder.loadTexts:
    eEventState.setStatus("mandatory")
_A7027EventStateIndex_Type = DmiInteger
_A7027EventStateIndex_Object = MibTableColumn
a7027EventStateIndex = _A7027EventStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7027, 1, 1),
    _A7027EventStateIndex_Type()
)
a7027EventStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7027EventStateIndex.setStatus("mandatory")
_A7027EventGenerationGroupClass_Type = DmiDisplaystring
_A7027EventGenerationGroupClass_Object = MibTableColumn
a7027EventGenerationGroupClass = _A7027EventGenerationGroupClass_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7027, 1, 2),
    _A7027EventGenerationGroupClass_Type()
)
a7027EventGenerationGroupClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7027EventGenerationGroupClass.setStatus("mandatory")
_A7027EventType_Type = DmiInteger
_A7027EventType_Object = MibTableColumn
a7027EventType = _A7027EventType_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7027, 1, 3),
    _A7027EventType_Type()
)
a7027EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7027EventType.setStatus("mandatory")


class _A7027CurrentState_Type(Integer32):
    """Custom type a7027CurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 16),
          ("vNon-critical", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A7027CurrentState_Type.__name__ = "Integer32"
_A7027CurrentState_Object = MibTableColumn
a7027CurrentState = _A7027CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7027, 1, 4),
    _A7027CurrentState_Type()
)
a7027CurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7027CurrentState.setStatus("mandatory")
_A7027AssociatedGroupObject_Type = DmiDisplaystring
_A7027AssociatedGroupObject_Object = MibTableColumn
a7027AssociatedGroupObject = _A7027AssociatedGroupObject_Object(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7027, 1, 5),
    _A7027AssociatedGroupObject_Type()
)
a7027AssociatedGroupObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7027AssociatedGroupObject.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trap1ForDevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 0, 1)
)
trap1ForDevices.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002StorageDevicesEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7001StorageDeviceIndex"))
)
if mibBuilder.loadTexts:
    trap1ForDevices.setStatus(
        ""
    )

trap2ForDevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 0, 2)
)
trap2ForDevices.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002StorageDevicesEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7001StorageDeviceIndex"))
)
if mibBuilder.loadTexts:
    trap2ForDevices.setStatus(
        ""
    )

trap3ForDevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 0, 3)
)
trap3ForDevices.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002StorageDevicesEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7001StorageDeviceIndex"))
)
if mibBuilder.loadTexts:
    trap3ForDevices.setStatus(
        ""
    )

trap4ForDevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 0, 4)
)
trap4ForDevices.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002StorageDevicesEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7001StorageDeviceIndex"))
)
if mibBuilder.loadTexts:
    trap4ForDevices.setStatus(
        ""
    )

trap5ForDevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7002, 1, 0, 5)
)
trap5ForDevices.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002StorageDevicesEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7002VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7001StorageDeviceIndex"))
)
if mibBuilder.loadTexts:
    trap5ForDevices.setStatus(
        ""
    )

trap1ForController = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 0, 1)
)
trap1ForController.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004StorageControllerEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7003ControllerIndex"))
)
if mibBuilder.loadTexts:
    trap1ForController.setStatus(
        ""
    )

trap2ForController = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 0, 2)
)
trap2ForController.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004StorageControllerEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7003ControllerIndex"))
)
if mibBuilder.loadTexts:
    trap2ForController.setStatus(
        ""
    )

trap3ForController = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7004, 1, 0, 3)
)
trap3ForController.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004StorageControllerEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7004VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7003ControllerIndex"))
)
if mibBuilder.loadTexts:
    trap3ForController.setStatus(
        ""
    )

trap1ForEnclosure = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7006, 1, 0, 1)
)
trap1ForEnclosure.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EnclosureEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006InstanceDataPresentr"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7006VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7005EnclosureIndex"))
)
if mibBuilder.loadTexts:
    trap1ForEnclosure.setStatus(
        ""
    )

trap1ForBusPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7008, 1, 0, 1)
)
trap1ForBusPort.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008BusPortEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7008VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7007BusPortIndex"))
)
if mibBuilder.loadTexts:
    trap1ForBusPort.setStatus(
        ""
    )

trap1ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 1)
)
trap1ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap1ForVolumeSet.setStatus(
        ""
    )

trap2ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 2)
)
trap2ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap2ForVolumeSet.setStatus(
        ""
    )

trap3ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 3)
)
trap3ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap3ForVolumeSet.setStatus(
        ""
    )

trap4ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 4)
)
trap4ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap4ForVolumeSet.setStatus(
        ""
    )

trap5ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 5)
)
trap5ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap5ForVolumeSet.setStatus(
        ""
    )

trap6ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 6)
)
trap6ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap6ForVolumeSet.setStatus(
        ""
    )

trap7ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 7)
)
trap7ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap7ForVolumeSet.setStatus(
        ""
    )

trap8ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 8)
)
trap8ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap8ForVolumeSet.setStatus(
        ""
    )

trap9ForVolumeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7012, 1, 0, 9)
)
trap9ForVolumeSet.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7012VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap9ForVolumeSet.setStatus(
        ""
    )

trap1ForSetActivity = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7013, 1, 0, 1)
)
trap1ForSetActivity.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013VolumeSetEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7013VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7011VolumeSetIndex"))
)
if mibBuilder.loadTexts:
    trap1ForSetActivity.setStatus(
        ""
    )

trap1ForRedundancyGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 0, 1)
)
trap1ForRedundancyGroup.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015RedundancyGroupEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7014RedundancyGroupIndex"))
)
if mibBuilder.loadTexts:
    trap1ForRedundancyGroup.setStatus(
        ""
    )

trap2ForRedundancyGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 0, 2)
)
trap2ForRedundancyGroup.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015RedundancyGroupEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7014RedundancyGroupIndex"))
)
if mibBuilder.loadTexts:
    trap2ForRedundancyGroup.setStatus(
        ""
    )

trap3ForRedundancyGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 0, 3)
)
trap3ForRedundancyGroup.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015RedundancyGroupEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7014RedundancyGroupIndex"))
)
if mibBuilder.loadTexts:
    trap3ForRedundancyGroup.setStatus(
        ""
    )

trap4ForRedundancyGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 0, 4)
)
trap4ForRedundancyGroup.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015RedundancyGroupEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7014RedundancyGroupIndex"))
)
if mibBuilder.loadTexts:
    trap4ForRedundancyGroup.setStatus(
        ""
    )

trap5ForRedundancyGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7015, 1, 0, 5)
)
trap5ForRedundancyGroup.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015RedundancyGroupEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7015VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7014RedundancyGroupIndex"))
)
if mibBuilder.loadTexts:
    trap5ForRedundancyGroup.setStatus(
        ""
    )

trap1ForSpareEvents = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 0, 1)
)
trap1ForSpareEvents.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016SpareEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7020ComponentSpareIndex"))
)
if mibBuilder.loadTexts:
    trap1ForSpareEvents.setStatus(
        ""
    )

trap2ForSpareEvents = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 0, 2)
)
trap2ForSpareEvents.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016SpareEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7020ComponentSpareIndex"))
)
if mibBuilder.loadTexts:
    trap2ForSpareEvents.setStatus(
        ""
    )

trap3ForSpareEvents = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 0, 3)
)
trap3ForSpareEvents.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016SpareEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7020ComponentSpareIndex"))
)
if mibBuilder.loadTexts:
    trap3ForSpareEvents.setStatus(
        ""
    )

trap4ForSpareEvents = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7016, 1, 0, 4)
)
trap4ForSpareEvents.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016SpareEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7016VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7020ComponentSpareIndex"))
)
if mibBuilder.loadTexts:
    trap4ForSpareEvents.setStatus(
        ""
    )

trap1ForAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 0, 1)
)
trap1ForAssociation.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018AssociationEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7017AssociationIndex"))
)
if mibBuilder.loadTexts:
    trap1ForAssociation.setStatus(
        ""
    )

trap2ForAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 0, 2)
)
trap2ForAssociation.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018AssociationEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7017AssociationIndex"))
)
if mibBuilder.loadTexts:
    trap2ForAssociation.setStatus(
        ""
    )

trap3ForAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 50, 10, 1, 7018, 1, 0, 3)
)
trap3ForAssociation.setObjects(
      *(("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018AssociationEventType"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSeverity"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventIsStateBased"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventStateKey"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018AssociatedGroup"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSubsystem"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventSolution"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018InstanceDataPresent"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018EventMessage"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7018VendorSpecificData"),
        ("ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB", "a7017AssociationIndex"))
)
if mibBuilder.loadTexts:
    trap3ForAssociation.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADAPTECCIOSTANDARDGROUPMIFDEFINITION2-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiInteger64X": DmiInteger64X,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "adaptec": adaptec,
       "thirdparty": thirdparty,
       "isc20": isc20,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap,
       "tStorageDevices": tStorageDevices,
       "eStorageDevices": eStorageDevices,
       "a7001StorageDeviceIndex": a7001StorageDeviceIndex,
       "a7001Type": a7001Type,
       "a7001TypeDescription": a7001TypeDescription,
       "a7001Sub-identifier": a7001Sub_identifier,
       "a7001MediaDataBlockSize": a7001MediaDataBlockSize,
       "a7001FormattedMediaCapacity": a7001FormattedMediaCapacity,
       "a7001RemovableDevice": a7001RemovableDevice,
       "a7001DeviceLoaded": a7001DeviceLoaded,
       "a7001RemovableMedia": a7001RemovableMedia,
       "a7001MediaLoaded": a7001MediaLoaded,
       "a7001Compression": a7001Compression,
       "a7001Encryption": a7001Encryption,
       "tStorageDevicesEvents": tStorageDevicesEvents,
       "eStorageDevicesEvents": eStorageDevicesEvents,
       "trap1ForDevices": trap1ForDevices,
       "trap2ForDevices": trap2ForDevices,
       "trap3ForDevices": trap3ForDevices,
       "trap4ForDevices": trap4ForDevices,
       "trap5ForDevices": trap5ForDevices,
       "a7002StorageDevicesEventType": a7002StorageDevicesEventType,
       "a7002EventSeverity": a7002EventSeverity,
       "a7002EventIsStateBased": a7002EventIsStateBased,
       "a7002EventStateKey": a7002EventStateKey,
       "a7002AssociatedGroup": a7002AssociatedGroup,
       "a7002EventSystem": a7002EventSystem,
       "a7002EventSubsystem": a7002EventSubsystem,
       "a7002EventSolution": a7002EventSolution,
       "a7002InstanceDataPresent": a7002InstanceDataPresent,
       "a7002EventMessage": a7002EventMessage,
       "a7002VendorSpecificData": a7002VendorSpecificData,
       "tStorageController": tStorageController,
       "eStorageController": eStorageController,
       "a7003ControllerIndex": a7003ControllerIndex,
       "a7003Identification": a7003Identification,
       "a7003ProtectionManagement": a7003ProtectionManagement,
       "a7003BusMaster": a7003BusMaster,
       "a7003SecondsSinceLastPower-up": a7003SecondsSinceLastPower_up,
       "tStorageControllerEvents": tStorageControllerEvents,
       "eStorageControllerEvents": eStorageControllerEvents,
       "trap1ForController": trap1ForController,
       "trap2ForController": trap2ForController,
       "trap3ForController": trap3ForController,
       "a7004StorageControllerEventType": a7004StorageControllerEventType,
       "a7004EventSeverity": a7004EventSeverity,
       "a7004EventIsStateBased": a7004EventIsStateBased,
       "a7004EventStateKey": a7004EventStateKey,
       "a7004AssociatedGroup": a7004AssociatedGroup,
       "a7004EventSystem": a7004EventSystem,
       "a7004EventSubsystem": a7004EventSubsystem,
       "a7004EventSolution": a7004EventSolution,
       "a7004InstanceDataPresent": a7004InstanceDataPresent,
       "a7004EventMessage": a7004EventMessage,
       "a7004VendorSpecificData": a7004VendorSpecificData,
       "tEnclosure": tEnclosure,
       "eEnclosure": eEnclosure,
       "a7005EnclosureIndex": a7005EnclosureIndex,
       "a7005Type": a7005Type,
       "a7005Description": a7005Description,
       "tEnclosureEvents": tEnclosureEvents,
       "eEnclosureEvents": eEnclosureEvents,
       "trap1ForEnclosure": trap1ForEnclosure,
       "a7006EnclosureEventType": a7006EnclosureEventType,
       "a7006EventSeverity": a7006EventSeverity,
       "a7006EventIsStateBased": a7006EventIsStateBased,
       "a7006EventStateKey": a7006EventStateKey,
       "a7006AssociatedGroup": a7006AssociatedGroup,
       "a7006EventSystem": a7006EventSystem,
       "a7006EventSubsystem": a7006EventSubsystem,
       "a7006EventSolution": a7006EventSolution,
       "a7006InstanceDataPresent": a7006InstanceDataPresent,
       "a7006EventMessage": a7006EventMessage,
       "a7006VendorSpecificData": a7006VendorSpecificData,
       "tBusPort": tBusPort,
       "eBusPort": eBusPort,
       "a7007BusPortIndex": a7007BusPortIndex,
       "a7007Protocol": a7007Protocol,
       "a7007ProtocolDescription": a7007ProtocolDescription,
       "a7007SignalCharacteristics": a7007SignalCharacteristics,
       "a7007AddressDescriptor": a7007AddressDescriptor,
       "a7007Isochronous": a7007Isochronous,
       "a7007MaximumWidth": a7007MaximumWidth,
       "a7007MaximumTransferRate": a7007MaximumTransferRate,
       "a7007MaximumNumberOfAttachments": a7007MaximumNumberOfAttachments,
       "a7007ConnectorType": a7007ConnectorType,
       "a7007ConnectorTypeDescription": a7007ConnectorTypeDescription,
       "a7007ConnectorGender": a7007ConnectorGender,
       "tBusPortEvents": tBusPortEvents,
       "eBusPortEvents": eBusPortEvents,
       "trap1ForBusPort": trap1ForBusPort,
       "a7008BusPortEventType": a7008BusPortEventType,
       "a7008EventSeverity": a7008EventSeverity,
       "a7008EventIsStateBased": a7008EventIsStateBased,
       "a7008EventStateKey": a7008EventStateKey,
       "a7008AssociatedGroup": a7008AssociatedGroup,
       "a7008EventSystem": a7008EventSystem,
       "a7008EventSubsystem": a7008EventSubsystem,
       "a7008EventSolution": a7008EventSolution,
       "a7008InstanceDataPresent": a7008InstanceDataPresent,
       "a7008EventMessage": a7008EventMessage,
       "a7008VendorSpecificData": a7008VendorSpecificData,
       "tAggregatePhysicalExtent": tAggregatePhysicalExtent,
       "eAggregatePhysicalExtent": eAggregatePhysicalExtent,
       "a7009AggregatePhysicalExtentIndex": a7009AggregatePhysicalExtentIndex,
       "a7009NumberOfBlocks": a7009NumberOfBlocks,
       "a7009NumberOfBlocksOfCheckData": a7009NumberOfBlocksOfCheckData,
       "tAggregateProtectedSpaceExtent": tAggregateProtectedSpaceExtent,
       "eAggregateProtectedSpaceExtent": eAggregateProtectedSpaceExtent,
       "a7010AggregateProtectedSpaceExtentIndex": a7010AggregateProtectedSpaceExtentIndex,
       "a7010NumberOfBlocks": a7010NumberOfBlocks,
       "tVolumeSet": tVolumeSet,
       "eVolumeSet": eVolumeSet,
       "a7011VolumeSetIndex": a7011VolumeSetIndex,
       "a7011Name": a7011Name,
       "a7011TotalStorageCapacity": a7011TotalStorageCapacity,
       "a7011ProtectedSpaceStripeLength": a7011ProtectedSpaceStripeLength,
       "a7011ProtectedSpaceExtentInterleaveDepth": a7011ProtectedSpaceExtentInterleaveDepth,
       "tVolumeSetEvents": tVolumeSetEvents,
       "eVolumeSetEvents": eVolumeSetEvents,
       "trap1ForVolumeSet": trap1ForVolumeSet,
       "trap2ForVolumeSet": trap2ForVolumeSet,
       "trap3ForVolumeSet": trap3ForVolumeSet,
       "trap4ForVolumeSet": trap4ForVolumeSet,
       "trap5ForVolumeSet": trap5ForVolumeSet,
       "trap6ForVolumeSet": trap6ForVolumeSet,
       "trap7ForVolumeSet": trap7ForVolumeSet,
       "trap8ForVolumeSet": trap8ForVolumeSet,
       "trap9ForVolumeSet": trap9ForVolumeSet,
       "a7012VolumeSetEventType": a7012VolumeSetEventType,
       "a7012EventSeverity": a7012EventSeverity,
       "a7012EventIsStateBased": a7012EventIsStateBased,
       "a7012EventStateKey": a7012EventStateKey,
       "a7012AssociatedGroup": a7012AssociatedGroup,
       "a7012EventSystem": a7012EventSystem,
       "a7012EventSubsystem": a7012EventSubsystem,
       "a7012EventSolution": a7012EventSolution,
       "a7012InstanceDataPresent": a7012InstanceDataPresent,
       "a7012EventMessage": a7012EventMessage,
       "a7012VendorSpecificData": a7012VendorSpecificData,
       "tVolumeSetActivityEvents": tVolumeSetActivityEvents,
       "eVolumeSetActivityEvents": eVolumeSetActivityEvents,
       "trap1ForSetActivity": trap1ForSetActivity,
       "a7013VolumeSetEventType": a7013VolumeSetEventType,
       "a7013EventSeverity": a7013EventSeverity,
       "a7013EventIsStateBased": a7013EventIsStateBased,
       "a7013EventStateKey": a7013EventStateKey,
       "a7013AssociatedGroup": a7013AssociatedGroup,
       "a7013EventSystem": a7013EventSystem,
       "a7013EventSubsystem": a7013EventSubsystem,
       "a7013EventSolution": a7013EventSolution,
       "a7013InstanceDataPresent": a7013InstanceDataPresent,
       "a7013EventMessage": a7013EventMessage,
       "a7013VendorSpecificData": a7013VendorSpecificData,
       "tRedundancyGroup": tRedundancyGroup,
       "eRedundancyGroup": eRedundancyGroup,
       "a7014RedundancyGroupIndex": a7014RedundancyGroupIndex,
       "a7014RedundancyType": a7014RedundancyType,
       "tRedundancyGroupEvents": tRedundancyGroupEvents,
       "eRedundancyGroupEvents": eRedundancyGroupEvents,
       "trap1ForRedundancyGroup": trap1ForRedundancyGroup,
       "trap2ForRedundancyGroup": trap2ForRedundancyGroup,
       "trap3ForRedundancyGroup": trap3ForRedundancyGroup,
       "trap4ForRedundancyGroup": trap4ForRedundancyGroup,
       "trap5ForRedundancyGroup": trap5ForRedundancyGroup,
       "a7015RedundancyGroupEventType": a7015RedundancyGroupEventType,
       "a7015EventSeverity": a7015EventSeverity,
       "a7015EventIsStateBased": a7015EventIsStateBased,
       "a7015EventStateKey": a7015EventStateKey,
       "a7015AssociatedGroup": a7015AssociatedGroup,
       "a7015EventSystem": a7015EventSystem,
       "a7015EventSubsystem": a7015EventSubsystem,
       "a7015EventSolution": a7015EventSolution,
       "a7015InstanceDataPresent": a7015InstanceDataPresent,
       "a7015EventMessage": a7015EventMessage,
       "a7015VendorSpecificData": a7015VendorSpecificData,
       "tSpareEvents": tSpareEvents,
       "eSpareEvents": eSpareEvents,
       "trap1ForSpareEvents": trap1ForSpareEvents,
       "trap2ForSpareEvents": trap2ForSpareEvents,
       "trap3ForSpareEvents": trap3ForSpareEvents,
       "trap4ForSpareEvents": trap4ForSpareEvents,
       "a7016SpareEventType": a7016SpareEventType,
       "a7016EventSeverity": a7016EventSeverity,
       "a7016EventIsStateBased": a7016EventIsStateBased,
       "a7016EventStateKey": a7016EventStateKey,
       "a7016AssociatedGroup": a7016AssociatedGroup,
       "a7016EventSystem": a7016EventSystem,
       "a7016EventSubsystem": a7016EventSubsystem,
       "a7016EventSolution": a7016EventSolution,
       "a7016InstanceDataPresent": a7016InstanceDataPresent,
       "a7016EventMessage": a7016EventMessage,
       "a7016VendorSpecificData": a7016VendorSpecificData,
       "tMassStorageAssociation": tMassStorageAssociation,
       "eMassStorageAssociation": eMassStorageAssociation,
       "a7017AssociationIndex": a7017AssociationIndex,
       "a7017Type": a7017Type,
       "a7017Reference1": a7017Reference1,
       "a7017Reference2": a7017Reference2,
       "tAssociationEvents": tAssociationEvents,
       "eAssociationEvents": eAssociationEvents,
       "trap1ForAssociation": trap1ForAssociation,
       "trap2ForAssociation": trap2ForAssociation,
       "trap3ForAssociation": trap3ForAssociation,
       "a7018AssociationEventType": a7018AssociationEventType,
       "a7018EventSeverity": a7018EventSeverity,
       "a7018EventIsStateBased": a7018EventIsStateBased,
       "a7018EventStateKey": a7018EventStateKey,
       "a7018AssociatedGroup": a7018AssociatedGroup,
       "a7018EventSystem": a7018EventSystem,
       "a7018EventSubsystem": a7018EventSubsystem,
       "a7018EventSolution": a7018EventSolution,
       "a7018InstanceDataPresent": a7018InstanceDataPresent,
       "a7018EventMessage": a7018EventMessage,
       "a7018VendorSpecificData": a7018VendorSpecificData,
       "tBusPortAssociation": tBusPortAssociation,
       "eBusPortAssociation": eBusPortAssociation,
       "a7019BusPortAssociationIndex": a7019BusPortAssociationIndex,
       "a7019NegotiatedSpeed": a7019NegotiatedSpeed,
       "a7019NegotiatedWidth": a7019NegotiatedWidth,
       "tComponentSpareAssociation": tComponentSpareAssociation,
       "eComponentSpareAssociation": eComponentSpareAssociation,
       "a7020ComponentSpareIndex": a7020ComponentSpareIndex,
       "a7020SpareFunctioningState": a7020SpareFunctioningState,
       "tWorldwideIdentifer": tWorldwideIdentifer,
       "eWorldwideIdentifer": eWorldwideIdentifer,
       "a7021WorldwideIdentifierIndex": a7021WorldwideIdentifierIndex,
       "a7021WorldwideIdentifierType": a7021WorldwideIdentifierType,
       "a7021WorldwideIdentifier": a7021WorldwideIdentifier,
       "tMassStorageStatistics": tMassStorageStatistics,
       "eMassStorageStatistics": eMassStorageStatistics,
       "a7022StatisticsIndex": a7022StatisticsIndex,
       "a7022BlocksRead": a7022BlocksRead,
       "a7022BlocksWritten": a7022BlocksWritten,
       "a7022ReadCommandsIssued": a7022ReadCommandsIssued,
       "a7022WriteCommandsIssued": a7022WriteCommandsIssued,
       "a7022IoRange0Read": a7022IoRange0Read,
       "a7022IoRange1Read": a7022IoRange1Read,
       "a7022IoRange2Read": a7022IoRange2Read,
       "a7022IoRange3Read": a7022IoRange3Read,
       "a7022IoRange4Read": a7022IoRange4Read,
       "a7022IoRange5Read": a7022IoRange5Read,
       "a7022IoRange6Read": a7022IoRange6Read,
       "a7022IoRange7Read": a7022IoRange7Read,
       "a7022IoRange8Read": a7022IoRange8Read,
       "a7022IoRange9Read": a7022IoRange9Read,
       "a7022IoRange10Read": a7022IoRange10Read,
       "a7022IoRange11Read": a7022IoRange11Read,
       "a7022IoRange12Read": a7022IoRange12Read,
       "a7022IoRange0Written": a7022IoRange0Written,
       "a7022IoRange1Written": a7022IoRange1Written,
       "a7022IoRange2Written": a7022IoRange2Written,
       "a7022IoRange3Written": a7022IoRange3Written,
       "a7022IoRange4Written": a7022IoRange4Written,
       "a7022IoRange5Written": a7022IoRange5Written,
       "a7022IoRange6Written": a7022IoRange6Written,
       "a7022IoRange7Written": a7022IoRange7Written,
       "a7022IoRange8Written": a7022IoRange8Written,
       "a7022IoRange9Written": a7022IoRange9Written,
       "a7022IoRange10Written": a7022IoRange10Written,
       "a7022IoRange11Written": a7022IoRange11Written,
       "a7022IoRange12Written": a7022IoRange12Written,
       "tOverallStatus": tOverallStatus,
       "eOverallStatus": eOverallStatus,
       "a7023OverallStatus": a7023OverallStatus,
       "tOperationalState": tOperationalState,
       "eOperationalState": eOperationalState,
       "a7024OperationalStateIndex": a7024OperationalStateIndex,
       "a7024DeviceGroupIndex": a7024DeviceGroupIndex,
       "a7024OperationalStatus": a7024OperationalStatus,
       "a7024UsageState": a7024UsageState,
       "a7024AvailabilityStatus": a7024AvailabilityStatus,
       "a7024AdministrativeState": a7024AdministrativeState,
       "a7024FatalErrorCount": a7024FatalErrorCount,
       "a7024MajorErrorCount": a7024MajorErrorCount,
       "a7024WarningErrorCount": a7024WarningErrorCount,
       "a7024CurrentErrorStatus": a7024CurrentErrorStatus,
       "a7024DevicePredictedFailureStatus": a7024DevicePredictedFailureStatus,
       "tEventLogCount": tEventLogCount,
       "eEventLogCount": eEventLogCount,
       "a7025EventLogCount": a7025EventLogCount,
       "tEventLog": tEventLog,
       "eEventLog": eEventLog,
       "a7026EventLogIndex": a7026EventLogIndex,
       "a7026EventLogEntry": a7026EventLogEntry,
       "a7026EventLogTimestamp": a7026EventLogTimestamp,
       "tEventState": tEventState,
       "eEventState": eEventState,
       "a7027EventStateIndex": a7027EventStateIndex,
       "a7027EventGenerationGroupClass": a7027EventGenerationGroupClass,
       "a7027EventType": a7027EventType,
       "a7027CurrentState": a7027CurrentState,
       "a7027AssociatedGroupObject": a7027AssociatedGroupObject}
)
