# SNMP MIB module (SYMBIOSDMI20MIFDEFINITIONID22-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMBIOSDMI20MIFDEFINITIONID22-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:34 2024
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
 NotificationType,
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
    "NotificationType",
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

_Symbios_ObjectIdentity = ObjectIdentity
symbios = _Symbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123)
)
_Cosprings_ObjectIdentity = ObjectIdentity
cosprings = _Cosprings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3)
)
_Scsi_ObjectIdentity = ObjectIdentity
scsi = _Scsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1)
)
_Fam8xx_ObjectIdentity = ObjectIdentity
fam8xx = _Fam8xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2)
)
_Id22_ObjectIdentity = ObjectIdentity
id22 = _Id22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1, 1, 5),
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
          ("vTheVerifyIsNotSupported", 2),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TSubcomponentSoftware_Object = MibTable
tSubcomponentSoftware = _TSubcomponentSoftware_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2)
)
if mibBuilder.loadTexts:
    tSubcomponentSoftware.setStatus("mandatory")
_ESubcomponentSoftware_Object = MibTableRow
eSubcomponentSoftware = _ESubcomponentSoftware_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1)
)
eSubcomponentSoftware.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a2SoftwareIndex"),
)
if mibBuilder.loadTexts:
    eSubcomponentSoftware.setStatus("mandatory")
_A2SoftwareIndex_Type = DmiInteger
_A2SoftwareIndex_Object = MibTableColumn
a2SoftwareIndex = _A2SoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 1),
    _A2SoftwareIndex_Type()
)
a2SoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SoftwareIndex.setStatus("mandatory")
_A2Type_Type = DmiDisplaystring
_A2Type_Object = MibTableColumn
a2Type = _A2Type_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 2),
    _A2Type_Type()
)
a2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Type.setStatus("mandatory")
_A2Vendor_Type = DmiDisplaystring
_A2Vendor_Object = MibTableColumn
a2Vendor = _A2Vendor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 3),
    _A2Vendor_Type()
)
a2Vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Vendor.setStatus("mandatory")
_A2Version_Type = DmiDisplaystring
_A2Version_Object = MibTableColumn
a2Version = _A2Version_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 4),
    _A2Version_Type()
)
a2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Version.setStatus("mandatory")
_A2Description_Type = DmiDisplaystring
_A2Description_Object = MibTableColumn
a2Description = _A2Description_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 5),
    _A2Description_Type()
)
a2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Description.setStatus("mandatory")
_A2IdentificationCode_Type = DmiDisplaystring
_A2IdentificationCode_Object = MibTableColumn
a2IdentificationCode = _A2IdentificationCode_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 6),
    _A2IdentificationCode_Type()
)
a2IdentificationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2IdentificationCode.setStatus("mandatory")
_A2LanguageEdition_Type = DmiDisplaystring
_A2LanguageEdition_Object = MibTableColumn
a2LanguageEdition = _A2LanguageEdition_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 7),
    _A2LanguageEdition_Type()
)
a2LanguageEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LanguageEdition.setStatus("mandatory")
_A2InterfaceDescription_Type = DmiDisplaystring
_A2InterfaceDescription_Object = MibTableColumn
a2InterfaceDescription = _A2InterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 8),
    _A2InterfaceDescription_Type()
)
a2InterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2InterfaceDescription.setStatus("mandatory")
_A2InterfaceVersion_Type = DmiDisplaystring
_A2InterfaceVersion_Object = MibTableColumn
a2InterfaceVersion = _A2InterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 2, 1, 9),
    _A2InterfaceVersion_Type()
)
a2InterfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2InterfaceVersion.setStatus("mandatory")
_TWorldwideIdentifer_Object = MibTable
tWorldwideIdentifer = _TWorldwideIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 3)
)
if mibBuilder.loadTexts:
    tWorldwideIdentifer.setStatus("mandatory")
_EWorldwideIdentifer_Object = MibTableRow
eWorldwideIdentifer = _EWorldwideIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 3, 1)
)
eWorldwideIdentifer.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a3WorldwideIdentifierIndex"),
)
if mibBuilder.loadTexts:
    eWorldwideIdentifer.setStatus("mandatory")
_A3WorldwideIdentifierIndex_Type = DmiInteger
_A3WorldwideIdentifierIndex_Object = MibTableColumn
a3WorldwideIdentifierIndex = _A3WorldwideIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 3, 1, 1),
    _A3WorldwideIdentifierIndex_Type()
)
a3WorldwideIdentifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3WorldwideIdentifierIndex.setStatus("mandatory")


class _A3WorldwideIdentifierType_Type(Integer32):
    """Custom type a3WorldwideIdentifierType based on Integer32"""
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
          ("vFc-ph64-bitName-identifier", 6),
          ("vIeeeExtendedUniqueIdentifier64-bit", 5),
          ("vLanMacAddress", 9),
          ("vNone", 3),
          ("vOther", 1),
          ("vUnicode", 8),
          ("vUnknown", 2),
          ("vVendorIdProductIdSerialNumber", 4),
          ("vWanAccessAddress", 10))
    )


_A3WorldwideIdentifierType_Type.__name__ = "Integer32"
_A3WorldwideIdentifierType_Object = MibTableColumn
a3WorldwideIdentifierType = _A3WorldwideIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 3, 1, 2),
    _A3WorldwideIdentifierType_Type()
)
a3WorldwideIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3WorldwideIdentifierType.setStatus("mandatory")
_A3WorldwideIdentifier_Type = DmiDisplaystring
_A3WorldwideIdentifier_Object = MibTableColumn
a3WorldwideIdentifier = _A3WorldwideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 3, 1, 3),
    _A3WorldwideIdentifier_Type()
)
a3WorldwideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3WorldwideIdentifier.setStatus("mandatory")
_TFieldReplaceableUnit_Object = MibTable
tFieldReplaceableUnit = _TFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4)
)
if mibBuilder.loadTexts:
    tFieldReplaceableUnit.setStatus("mandatory")
_EFieldReplaceableUnit_Object = MibTableRow
eFieldReplaceableUnit = _EFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1)
)
eFieldReplaceableUnit.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a4FruIndex"),
)
if mibBuilder.loadTexts:
    eFieldReplaceableUnit.setStatus("mandatory")
_A4FruIndex_Type = DmiInteger
_A4FruIndex_Object = MibTableColumn
a4FruIndex = _A4FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 1),
    _A4FruIndex_Type()
)
a4FruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4FruIndex.setStatus("mandatory")
_A4DeviceGroupIndex_Type = DmiInteger
_A4DeviceGroupIndex_Object = MibTableColumn
a4DeviceGroupIndex = _A4DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 2),
    _A4DeviceGroupIndex_Type()
)
a4DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4DeviceGroupIndex.setStatus("mandatory")
_A4Description_Type = DmiDisplaystring
_A4Description_Object = MibTableColumn
a4Description = _A4Description_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 3),
    _A4Description_Type()
)
a4Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Description.setStatus("mandatory")
_A4Manufacturer_Type = DmiDisplaystring
_A4Manufacturer_Object = MibTableColumn
a4Manufacturer = _A4Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 4),
    _A4Manufacturer_Type()
)
a4Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Manufacturer.setStatus("mandatory")
_A4Model_Type = DmiDisplaystring
_A4Model_Object = MibTableColumn
a4Model = _A4Model_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 5),
    _A4Model_Type()
)
a4Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Model.setStatus("mandatory")
_A4PartNumber_Type = DmiDisplaystring
_A4PartNumber_Object = MibTableColumn
a4PartNumber = _A4PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 6),
    _A4PartNumber_Type()
)
a4PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4PartNumber.setStatus("mandatory")
_A4FruSerialNumber_Type = DmiDisplaystring
_A4FruSerialNumber_Object = MibTableColumn
a4FruSerialNumber = _A4FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 7),
    _A4FruSerialNumber_Type()
)
a4FruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4FruSerialNumber.setStatus("mandatory")
_A4RevisionLevel_Type = DmiDisplaystring
_A4RevisionLevel_Object = MibTableColumn
a4RevisionLevel = _A4RevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 8),
    _A4RevisionLevel_Type()
)
a4RevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4RevisionLevel.setStatus("mandatory")
_A4WarrantyStartDate_Type = DmiDateX
_A4WarrantyStartDate_Object = MibTableColumn
a4WarrantyStartDate = _A4WarrantyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 9),
    _A4WarrantyStartDate_Type()
)
a4WarrantyStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4WarrantyStartDate.setStatus("mandatory")
_A4WarrantyDuration_Type = DmiInteger
_A4WarrantyDuration_Object = MibTableColumn
a4WarrantyDuration = _A4WarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 10),
    _A4WarrantyDuration_Type()
)
a4WarrantyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4WarrantyDuration.setStatus("mandatory")
_A4SupportPhoneNumber_Type = DmiDisplaystring
_A4SupportPhoneNumber_Object = MibTableColumn
a4SupportPhoneNumber = _A4SupportPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 11),
    _A4SupportPhoneNumber_Type()
)
a4SupportPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4SupportPhoneNumber.setStatus("mandatory")
_A4FruInternetUniformResourceLocator_Type = DmiDisplaystring
_A4FruInternetUniformResourceLocator_Object = MibTableColumn
a4FruInternetUniformResourceLocator = _A4FruInternetUniformResourceLocator_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 4, 1, 12),
    _A4FruInternetUniformResourceLocator_Type()
)
a4FruInternetUniformResourceLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4FruInternetUniformResourceLocator.setStatus("mandatory")
_TStorageDevices_Object = MibTable
tStorageDevices = _TStorageDevices_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5)
)
if mibBuilder.loadTexts:
    tStorageDevices.setStatus("mandatory")
_EStorageDevices_Object = MibTableRow
eStorageDevices = _EStorageDevices_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1)
)
eStorageDevices.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a5StorageDeviceIndex"),
)
if mibBuilder.loadTexts:
    eStorageDevices.setStatus("mandatory")
_A5StorageDeviceIndex_Type = DmiInteger
_A5StorageDeviceIndex_Object = MibTableColumn
a5StorageDeviceIndex = _A5StorageDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 1),
    _A5StorageDeviceIndex_Type()
)
a5StorageDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5StorageDeviceIndex.setStatus("mandatory")


class _A5Type_Type(Integer32):
    """Custom type a5Type based on Integer32"""
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
          ("vDigitalVersatileDiskDvdramRamDrive", 16),
          ("vFlashDisk", 9),
          ("vFlexibleDisketteDrive", 4),
          ("vMagneto-opticalDrive", 7),
          ("vMediaChanger", 13),
          ("vOpticalFloppyDiskDrive", 11),
          ("vOpticalWrite-onceread-manyWormDrive", 6),
          ("vOther", 1),
          ("vRigidDiskDrive", 3),
          ("vSolidState", 14),
          ("vTapeDrive", 12),
          ("vUnknown", 2))
    )


_A5Type_Type.__name__ = "Integer32"
_A5Type_Object = MibTableColumn
a5Type = _A5Type_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 2),
    _A5Type_Type()
)
a5Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Type.setStatus("mandatory")
_A5TypeDescription_Type = DmiDisplaystring
_A5TypeDescription_Object = MibTableColumn
a5TypeDescription = _A5TypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 3),
    _A5TypeDescription_Type()
)
a5TypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5TypeDescription.setStatus("mandatory")
_A5Sub_identifier_Type = DmiDisplaystring
_A5Sub_identifier_Object = MibScalar
a5Sub_identifier = _A5Sub_identifier_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 4),
    _A5Sub_identifier_Type()
)
a5Sub_identifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Sub_identifier.setStatus("mandatory")
_A5MediaDataBlockSize_Type = DmiInteger
_A5MediaDataBlockSize_Object = MibTableColumn
a5MediaDataBlockSize = _A5MediaDataBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 5),
    _A5MediaDataBlockSize_Type()
)
a5MediaDataBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5MediaDataBlockSize.setStatus("mandatory")
_A5FormattedMediaCapacity_Type = DmiInteger64X
_A5FormattedMediaCapacity_Object = MibTableColumn
a5FormattedMediaCapacity = _A5FormattedMediaCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 6),
    _A5FormattedMediaCapacity_Type()
)
a5FormattedMediaCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5FormattedMediaCapacity.setStatus("mandatory")


class _A5RemovableDevice_Type(Integer32):
    """Custom type a5RemovableDevice based on Integer32"""
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


_A5RemovableDevice_Type.__name__ = "Integer32"
_A5RemovableDevice_Object = MibTableColumn
a5RemovableDevice = _A5RemovableDevice_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 7),
    _A5RemovableDevice_Type()
)
a5RemovableDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5RemovableDevice.setStatus("mandatory")


class _A5DeviceLoaded_Type(Integer32):
    """Custom type a5DeviceLoaded based on Integer32"""
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


_A5DeviceLoaded_Type.__name__ = "Integer32"
_A5DeviceLoaded_Object = MibTableColumn
a5DeviceLoaded = _A5DeviceLoaded_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 8),
    _A5DeviceLoaded_Type()
)
a5DeviceLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5DeviceLoaded.setStatus("mandatory")


class _A5RemovableMedia_Type(Integer32):
    """Custom type a5RemovableMedia based on Integer32"""
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


_A5RemovableMedia_Type.__name__ = "Integer32"
_A5RemovableMedia_Object = MibTableColumn
a5RemovableMedia = _A5RemovableMedia_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 9),
    _A5RemovableMedia_Type()
)
a5RemovableMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5RemovableMedia.setStatus("mandatory")


class _A5MediaLoaded_Type(Integer32):
    """Custom type a5MediaLoaded based on Integer32"""
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


_A5MediaLoaded_Type.__name__ = "Integer32"
_A5MediaLoaded_Object = MibTableColumn
a5MediaLoaded = _A5MediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 10),
    _A5MediaLoaded_Type()
)
a5MediaLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5MediaLoaded.setStatus("mandatory")


class _A5Compression_Type(Integer32):
    """Custom type a5Compression based on Integer32"""
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


_A5Compression_Type.__name__ = "Integer32"
_A5Compression_Object = MibTableColumn
a5Compression = _A5Compression_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 11),
    _A5Compression_Type()
)
a5Compression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Compression.setStatus("mandatory")


class _A5Encryption_Type(Integer32):
    """Custom type a5Encryption based on Integer32"""
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


_A5Encryption_Type.__name__ = "Integer32"
_A5Encryption_Object = MibTableColumn
a5Encryption = _A5Encryption_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 5, 1, 12),
    _A5Encryption_Type()
)
a5Encryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Encryption.setStatus("mandatory")
_TStorageDevicesEvents_Object = MibTable
tStorageDevicesEvents = _TStorageDevicesEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6)
)
if mibBuilder.loadTexts:
    tStorageDevicesEvents.setStatus("mandatory")
_EStorageDevicesEvents_Object = MibTableRow
eStorageDevicesEvents = _EStorageDevicesEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1)
)
eStorageDevicesEvents.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eStorageDevicesEvents.setStatus("mandatory")


class _A6StorageDevicesEventType_Type(Integer32):
    """Custom type a6StorageDevicesEventType based on Integer32"""
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
        *(("vRebuildInProgress", 1),
          ("vSelf-monitoringWarning", 4),
          ("vStorageDeviceError", 3),
          ("vStorageDeviceReadying", 2))
    )


_A6StorageDevicesEventType_Type.__name__ = "Integer32"
_A6StorageDevicesEventType_Object = MibTableColumn
a6StorageDevicesEventType = _A6StorageDevicesEventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 1),
    _A6StorageDevicesEventType_Type()
)
a6StorageDevicesEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6StorageDevicesEventType.setStatus("mandatory")


class _A6EventSeverity_Type(Integer32):
    """Custom type a6EventSeverity based on Integer32"""
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


_A6EventSeverity_Type.__name__ = "Integer32"
_A6EventSeverity_Object = MibTableColumn
a6EventSeverity = _A6EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 2),
    _A6EventSeverity_Type()
)
a6EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventSeverity.setStatus("mandatory")


class _A6EventIsStateBased_Type(Integer32):
    """Custom type a6EventIsStateBased based on Integer32"""
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


_A6EventIsStateBased_Type.__name__ = "Integer32"
_A6EventIsStateBased_Object = MibTableColumn
a6EventIsStateBased = _A6EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 3),
    _A6EventIsStateBased_Type()
)
a6EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventIsStateBased.setStatus("mandatory")
_A6EventStateKey_Type = DmiInteger
_A6EventStateKey_Object = MibTableColumn
a6EventStateKey = _A6EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 4),
    _A6EventStateKey_Type()
)
a6EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventStateKey.setStatus("mandatory")
_A6AssociatedGroup_Type = DmiDisplaystring
_A6AssociatedGroup_Object = MibTableColumn
a6AssociatedGroup = _A6AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 5),
    _A6AssociatedGroup_Type()
)
a6AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6AssociatedGroup.setStatus("mandatory")


class _A6EventSystem_Type(Integer32):
    """Custom type a6EventSystem based on Integer32"""
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
        *(("vDeviceScan", 4),
          ("vDomainValidation", 3),
          ("vOther", 1),
          ("vSmart", 5),
          ("vUnknown", 2))
    )


_A6EventSystem_Type.__name__ = "Integer32"
_A6EventSystem_Object = MibTableColumn
a6EventSystem = _A6EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 6),
    _A6EventSystem_Type()
)
a6EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventSystem.setStatus("mandatory")


class _A6EventSubsystem_Type(Integer32):
    """Custom type a6EventSubsystem based on Integer32"""
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


_A6EventSubsystem_Type.__name__ = "Integer32"
_A6EventSubsystem_Object = MibTableColumn
a6EventSubsystem = _A6EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 7),
    _A6EventSubsystem_Type()
)
a6EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventSubsystem.setStatus("mandatory")


class _A6EventSolution_Type(Integer32):
    """Custom type a6EventSolution based on Integer32"""
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
        *(("v1stCheckCabling2ndPowerCycleDeviceLas", 3),
          ("vBackupDataFromFailingDeviceAndReplaceTh", 4),
          ("vNoActionRequired", 6),
          ("vOther", 1),
          ("vRunDiskAdministrator", 5),
          ("vUnknown", 2))
    )


_A6EventSolution_Type.__name__ = "Integer32"
_A6EventSolution_Object = MibTableColumn
a6EventSolution = _A6EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 8),
    _A6EventSolution_Type()
)
a6EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventSolution.setStatus("mandatory")


class _A6InstanceDataPresent_Type(Integer32):
    """Custom type a6InstanceDataPresent based on Integer32"""
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


_A6InstanceDataPresent_Type.__name__ = "Integer32"
_A6InstanceDataPresent_Object = MibTableColumn
a6InstanceDataPresent = _A6InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 9),
    _A6InstanceDataPresent_Type()
)
a6InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6InstanceDataPresent.setStatus("mandatory")
_A6EventMessage_Type = DmiDisplaystring
_A6EventMessage_Object = MibTableColumn
a6EventMessage = _A6EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 10),
    _A6EventMessage_Type()
)
a6EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventMessage.setStatus("mandatory")
_TStorageController_Object = MibTable
tStorageController = _TStorageController_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 7)
)
if mibBuilder.loadTexts:
    tStorageController.setStatus("mandatory")
_EStorageController_Object = MibTableRow
eStorageController = _EStorageController_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 7, 1)
)
eStorageController.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a7ControllerIndex"),
)
if mibBuilder.loadTexts:
    eStorageController.setStatus("mandatory")
_A7ControllerIndex_Type = DmiInteger
_A7ControllerIndex_Object = MibTableColumn
a7ControllerIndex = _A7ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 7, 1, 1),
    _A7ControllerIndex_Type()
)
a7ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ControllerIndex.setStatus("mandatory")
_A7Identification_Type = DmiDisplaystring
_A7Identification_Object = MibTableColumn
a7Identification = _A7Identification_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 7, 1, 2),
    _A7Identification_Type()
)
a7Identification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Identification.setStatus("mandatory")


class _A7ProtectionManagement_Type(Integer32):
    """Custom type a7ProtectionManagement based on Integer32"""
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


_A7ProtectionManagement_Type.__name__ = "Integer32"
_A7ProtectionManagement_Object = MibTableColumn
a7ProtectionManagement = _A7ProtectionManagement_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 7, 1, 3),
    _A7ProtectionManagement_Type()
)
a7ProtectionManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ProtectionManagement.setStatus("mandatory")


class _A7BusMaster_Type(Integer32):
    """Custom type a7BusMaster based on Integer32"""
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


_A7BusMaster_Type.__name__ = "Integer32"
_A7BusMaster_Object = MibTableColumn
a7BusMaster = _A7BusMaster_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 7, 1, 4),
    _A7BusMaster_Type()
)
a7BusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7BusMaster.setStatus("mandatory")
_A7SecondsSinceLastPower_up_Type = DmiInteger
_A7SecondsSinceLastPower_up_Object = MibScalar
a7SecondsSinceLastPower_up = _A7SecondsSinceLastPower_up_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 7, 1, 5),
    _A7SecondsSinceLastPower_up_Type()
)
a7SecondsSinceLastPower_up.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7SecondsSinceLastPower_up.setStatus("mandatory")
_TStorageControllerEvents_Object = MibTable
tStorageControllerEvents = _TStorageControllerEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8)
)
if mibBuilder.loadTexts:
    tStorageControllerEvents.setStatus("mandatory")
_EStorageControllerEvents_Object = MibTableRow
eStorageControllerEvents = _EStorageControllerEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1)
)
eStorageControllerEvents.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eStorageControllerEvents.setStatus("mandatory")


class _A8StorageControllerEventType_Type(Integer32):
    """Custom type a8StorageControllerEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vSelf-monitoringWarning1", 2),
          ("vStorageControllerError", 1))
    )


_A8StorageControllerEventType_Type.__name__ = "Integer32"
_A8StorageControllerEventType_Object = MibTableColumn
a8StorageControllerEventType = _A8StorageControllerEventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 1),
    _A8StorageControllerEventType_Type()
)
a8StorageControllerEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8StorageControllerEventType.setStatus("mandatory")


class _A8EventSeverity_Type(Integer32):
    """Custom type a8EventSeverity based on Integer32"""
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


_A8EventSeverity_Type.__name__ = "Integer32"
_A8EventSeverity_Object = MibTableColumn
a8EventSeverity = _A8EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 2),
    _A8EventSeverity_Type()
)
a8EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventSeverity.setStatus("mandatory")


class _A8EventIsStateBased_Type(Integer32):
    """Custom type a8EventIsStateBased based on Integer32"""
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


_A8EventIsStateBased_Type.__name__ = "Integer32"
_A8EventIsStateBased_Object = MibTableColumn
a8EventIsStateBased = _A8EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 3),
    _A8EventIsStateBased_Type()
)
a8EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventIsStateBased.setStatus("mandatory")
_A8EventStateKey_Type = DmiInteger
_A8EventStateKey_Object = MibTableColumn
a8EventStateKey = _A8EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 4),
    _A8EventStateKey_Type()
)
a8EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventStateKey.setStatus("mandatory")
_A8AssociatedGroup_Type = DmiDisplaystring
_A8AssociatedGroup_Object = MibTableColumn
a8AssociatedGroup = _A8AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 5),
    _A8AssociatedGroup_Type()
)
a8AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8AssociatedGroup.setStatus("mandatory")


class _A8EventSystem_Type(Integer32):
    """Custom type a8EventSystem based on Integer32"""
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
        *(("vControllerScan", 4),
          ("vDomainValidation", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A8EventSystem_Type.__name__ = "Integer32"
_A8EventSystem_Object = MibTableColumn
a8EventSystem = _A8EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 6),
    _A8EventSystem_Type()
)
a8EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventSystem.setStatus("mandatory")


class _A8EventSubsystem_Type(Integer32):
    """Custom type a8EventSubsystem based on Integer32"""
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


_A8EventSubsystem_Type.__name__ = "Integer32"
_A8EventSubsystem_Object = MibTableColumn
a8EventSubsystem = _A8EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 7),
    _A8EventSubsystem_Type()
)
a8EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventSubsystem.setStatus("mandatory")


class _A8EventSolution_Type(Integer32):
    """Custom type a8EventSolution based on Integer32"""
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
        *(("v1stCheckCabling2ndPowerCycleSystemLas", 3),
          ("vOther", 1),
          ("vRunDomainValidationOnThisController", 4),
          ("vUnknown", 2))
    )


_A8EventSolution_Type.__name__ = "Integer32"
_A8EventSolution_Object = MibTableColumn
a8EventSolution = _A8EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 8),
    _A8EventSolution_Type()
)
a8EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventSolution.setStatus("mandatory")


class _A8InstanceDataPresent_Type(Integer32):
    """Custom type a8InstanceDataPresent based on Integer32"""
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


_A8InstanceDataPresent_Type.__name__ = "Integer32"
_A8InstanceDataPresent_Object = MibTableColumn
a8InstanceDataPresent = _A8InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 9),
    _A8InstanceDataPresent_Type()
)
a8InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8InstanceDataPresent.setStatus("mandatory")
_A8EventMessage_Type = DmiDisplaystring
_A8EventMessage_Object = MibTableColumn
a8EventMessage = _A8EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 10),
    _A8EventMessage_Type()
)
a8EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventMessage.setStatus("mandatory")
_TBusPort_Object = MibTable
tBusPort = _TBusPort_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9)
)
if mibBuilder.loadTexts:
    tBusPort.setStatus("mandatory")
_EBusPort_Object = MibTableRow
eBusPort = _EBusPort_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1)
)
eBusPort.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a9BusPortIndex"),
)
if mibBuilder.loadTexts:
    eBusPort.setStatus("mandatory")
_A9BusPortIndex_Type = DmiInteger
_A9BusPortIndex_Object = MibTableColumn
a9BusPortIndex = _A9BusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 1),
    _A9BusPortIndex_Type()
)
a9BusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9BusPortIndex.setStatus("mandatory")


class _A9Protocol_Type(Integer32):
    """Custom type a9Protocol based on Integer32"""
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


_A9Protocol_Type.__name__ = "Integer32"
_A9Protocol_Object = MibTableColumn
a9Protocol = _A9Protocol_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 2),
    _A9Protocol_Type()
)
a9Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Protocol.setStatus("mandatory")
_A9ProtocolDescription_Type = DmiDisplaystring
_A9ProtocolDescription_Object = MibTableColumn
a9ProtocolDescription = _A9ProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 3),
    _A9ProtocolDescription_Type()
)
a9ProtocolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ProtocolDescription.setStatus("mandatory")


class _A9SignalCharacteristics_Type(Integer32):
    """Custom type a9SignalCharacteristics based on Integer32"""
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


_A9SignalCharacteristics_Type.__name__ = "Integer32"
_A9SignalCharacteristics_Object = MibTableColumn
a9SignalCharacteristics = _A9SignalCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 4),
    _A9SignalCharacteristics_Type()
)
a9SignalCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9SignalCharacteristics.setStatus("mandatory")
_A9AddressDescriptor_Type = DmiDisplaystring
_A9AddressDescriptor_Object = MibTableColumn
a9AddressDescriptor = _A9AddressDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 5),
    _A9AddressDescriptor_Type()
)
a9AddressDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9AddressDescriptor.setStatus("mandatory")


class _A9Isochronous_Type(Integer32):
    """Custom type a9Isochronous based on Integer32"""
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


_A9Isochronous_Type.__name__ = "Integer32"
_A9Isochronous_Object = MibTableColumn
a9Isochronous = _A9Isochronous_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 6),
    _A9Isochronous_Type()
)
a9Isochronous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Isochronous.setStatus("mandatory")
_A9MaximumWidth_Type = DmiInteger
_A9MaximumWidth_Object = MibTableColumn
a9MaximumWidth = _A9MaximumWidth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 7),
    _A9MaximumWidth_Type()
)
a9MaximumWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9MaximumWidth.setStatus("mandatory")
_A9MaximumTransferRate_Type = DmiInteger
_A9MaximumTransferRate_Object = MibTableColumn
a9MaximumTransferRate = _A9MaximumTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 8),
    _A9MaximumTransferRate_Type()
)
a9MaximumTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9MaximumTransferRate.setStatus("mandatory")
_A9MaximumNumberOfAttachments_Type = DmiInteger
_A9MaximumNumberOfAttachments_Object = MibTableColumn
a9MaximumNumberOfAttachments = _A9MaximumNumberOfAttachments_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 9),
    _A9MaximumNumberOfAttachments_Type()
)
a9MaximumNumberOfAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9MaximumNumberOfAttachments.setStatus("mandatory")


class _A9ConnectorType_Type(Integer32):
    """Custom type a9ConnectorType based on Integer32"""
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


_A9ConnectorType_Type.__name__ = "Integer32"
_A9ConnectorType_Object = MibTableColumn
a9ConnectorType = _A9ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 10),
    _A9ConnectorType_Type()
)
a9ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ConnectorType.setStatus("mandatory")
_A9ConnectorTypeDescription_Type = DmiDisplaystring
_A9ConnectorTypeDescription_Object = MibTableColumn
a9ConnectorTypeDescription = _A9ConnectorTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 11),
    _A9ConnectorTypeDescription_Type()
)
a9ConnectorTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ConnectorTypeDescription.setStatus("mandatory")


class _A9ConnectorGender_Type(Integer32):
    """Custom type a9ConnectorGender based on Integer32"""
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


_A9ConnectorGender_Type.__name__ = "Integer32"
_A9ConnectorGender_Object = MibTableColumn
a9ConnectorGender = _A9ConnectorGender_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 9, 1, 12),
    _A9ConnectorGender_Type()
)
a9ConnectorGender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ConnectorGender.setStatus("mandatory")
_TFibreChannelBusPortExtensions_Object = MibTable
tFibreChannelBusPortExtensions = _TFibreChannelBusPortExtensions_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10)
)
if mibBuilder.loadTexts:
    tFibreChannelBusPortExtensions.setStatus("mandatory")
_EFibreChannelBusPortExtensions_Object = MibTableRow
eFibreChannelBusPortExtensions = _EFibreChannelBusPortExtensions_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1)
)
eFibreChannelBusPortExtensions.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a10BusPortIndex"),
)
if mibBuilder.loadTexts:
    eFibreChannelBusPortExtensions.setStatus("mandatory")
_A10BusPortIndex_Type = DmiInteger
_A10BusPortIndex_Object = MibTableColumn
a10BusPortIndex = _A10BusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1, 1),
    _A10BusPortIndex_Type()
)
a10BusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10BusPortIndex.setStatus("mandatory")
_A10EndToEndCredit_Type = DmiInteger
_A10EndToEndCredit_Object = MibTableColumn
a10EndToEndCredit = _A10EndToEndCredit_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1, 2),
    _A10EndToEndCredit_Type()
)
a10EndToEndCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EndToEndCredit.setStatus("mandatory")
_A10BufferToBufferCredit_Type = DmiInteger
_A10BufferToBufferCredit_Object = MibTableColumn
a10BufferToBufferCredit = _A10BufferToBufferCredit_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1, 3),
    _A10BufferToBufferCredit_Type()
)
a10BufferToBufferCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10BufferToBufferCredit.setStatus("mandatory")


class _A10LinkType_Type(Integer32):
    """Custom type a10LinkType based on Integer32"""
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
        *(("vCopper", 3),
          ("vFibre-Multimode50-Laser", 6),
          ("vFibre-Multimode50-Led", 7),
          ("vFibre-Multimode625-Laser", 8),
          ("vFibre-Multimode625-Led", 9),
          ("vFibre-SingleMode1300Nanometers", 4),
          ("vFibre-SingleMode1500Nanometers", 5),
          ("vFibreLongWave", 10),
          ("vFibreShortWave", 11),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A10LinkType_Type.__name__ = "Integer32"
_A10LinkType_Object = MibTableColumn
a10LinkType = _A10LinkType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1, 4),
    _A10LinkType_Type()
)
a10LinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10LinkType.setStatus("mandatory")


class _A10FlowControlClassType_Type(Integer32):
    """Custom type a10FlowControlClassType based on Integer32"""
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
        *(("vClass-1", 3),
          ("vClass-1class-2", 6),
          ("vClass-2", 4),
          ("vClass-3", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A10FlowControlClassType_Type.__name__ = "Integer32"
_A10FlowControlClassType_Object = MibTableColumn
a10FlowControlClassType = _A10FlowControlClassType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1, 5),
    _A10FlowControlClassType_Type()
)
a10FlowControlClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10FlowControlClassType.setStatus("mandatory")


class _A10FlowControlAcknowledgmentType_Type(Integer32):
    """Custom type a10FlowControlAcknowledgmentType based on Integer32"""
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
        *(("vAck-0", 3),
          ("vAck-1", 4),
          ("vAck-n", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A10FlowControlAcknowledgmentType_Type.__name__ = "Integer32"
_A10FlowControlAcknowledgmentType_Object = MibTableColumn
a10FlowControlAcknowledgmentType = _A10FlowControlAcknowledgmentType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1, 6),
    _A10FlowControlAcknowledgmentType_Type()
)
a10FlowControlAcknowledgmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10FlowControlAcknowledgmentType.setStatus("mandatory")


class _A10FabricTopology_Type(Integer32):
    """Custom type a10FabricTopology based on Integer32"""
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


_A10FabricTopology_Type.__name__ = "Integer32"
_A10FabricTopology_Object = MibTableColumn
a10FabricTopology = _A10FabricTopology_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 10, 1, 7),
    _A10FabricTopology_Type()
)
a10FabricTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10FabricTopology.setStatus("mandatory")
_TMassStorageAssociation_Object = MibTable
tMassStorageAssociation = _TMassStorageAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 11)
)
if mibBuilder.loadTexts:
    tMassStorageAssociation.setStatus("mandatory")
_EMassStorageAssociation_Object = MibTableRow
eMassStorageAssociation = _EMassStorageAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 11, 1)
)
eMassStorageAssociation.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a11AssociationIndex"),
)
if mibBuilder.loadTexts:
    eMassStorageAssociation.setStatus("mandatory")
_A11AssociationIndex_Type = DmiInteger
_A11AssociationIndex_Object = MibTableColumn
a11AssociationIndex = _A11AssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 11, 1, 1),
    _A11AssociationIndex_Type()
)
a11AssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11AssociationIndex.setStatus("mandatory")
_A11Type_Type = DmiDisplaystring
_A11Type_Object = MibTableColumn
a11Type = _A11Type_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 11, 1, 2),
    _A11Type_Type()
)
a11Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Type.setStatus("mandatory")
_A11Reference1_Type = DmiDisplaystring
_A11Reference1_Object = MibTableColumn
a11Reference1 = _A11Reference1_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 11, 1, 3),
    _A11Reference1_Type()
)
a11Reference1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Reference1.setStatus("mandatory")
_A11Reference2_Type = DmiDisplaystring
_A11Reference2_Object = MibTableColumn
a11Reference2 = _A11Reference2_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 11, 1, 4),
    _A11Reference2_Type()
)
a11Reference2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Reference2.setStatus("mandatory")
_TMassStorageAssociationEvents_Object = MibTable
tMassStorageAssociationEvents = _TMassStorageAssociationEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12)
)
if mibBuilder.loadTexts:
    tMassStorageAssociationEvents.setStatus("mandatory")
_EMassStorageAssociationEvents_Object = MibTableRow
eMassStorageAssociationEvents = _EMassStorageAssociationEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1)
)
eMassStorageAssociationEvents.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eMassStorageAssociationEvents.setStatus("mandatory")


class _A12MassStorageAssociationEventType_Type(Integer32):
    """Custom type a12MassStorageAssociationEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vExistingObjectGone", 3),
          ("vExistingObjectReplaced", 2),
          ("vNewObjectDetected", 1))
    )


_A12MassStorageAssociationEventType_Type.__name__ = "Integer32"
_A12MassStorageAssociationEventType_Object = MibTableColumn
a12MassStorageAssociationEventType = _A12MassStorageAssociationEventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 1),
    _A12MassStorageAssociationEventType_Type()
)
a12MassStorageAssociationEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12MassStorageAssociationEventType.setStatus("mandatory")


class _A12EventSeverity_Type(Integer32):
    """Custom type a12EventSeverity based on Integer32"""
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


_A12EventSeverity_Type.__name__ = "Integer32"
_A12EventSeverity_Object = MibTableColumn
a12EventSeverity = _A12EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 2),
    _A12EventSeverity_Type()
)
a12EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventSeverity.setStatus("mandatory")


class _A12EventIsStateBased_Type(Integer32):
    """Custom type a12EventIsStateBased based on Integer32"""
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


_A12EventIsStateBased_Type.__name__ = "Integer32"
_A12EventIsStateBased_Object = MibTableColumn
a12EventIsStateBased = _A12EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 3),
    _A12EventIsStateBased_Type()
)
a12EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventIsStateBased.setStatus("mandatory")
_A12EventStateKey_Type = DmiInteger
_A12EventStateKey_Object = MibTableColumn
a12EventStateKey = _A12EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 4),
    _A12EventStateKey_Type()
)
a12EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventStateKey.setStatus("mandatory")
_A12AssociatedGroup_Type = DmiDisplaystring
_A12AssociatedGroup_Object = MibTableColumn
a12AssociatedGroup = _A12AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 5),
    _A12AssociatedGroup_Type()
)
a12AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12AssociatedGroup.setStatus("mandatory")


class _A12EventSystem_Type(Integer32):
    """Custom type a12EventSystem based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("vAggregatePhysicalExtent", 9),
          ("vAggregateProtectedSpaceExtent", 7),
          ("vBusPort", 4),
          ("vCache", 11),
          ("vOther", 0),
          ("vPhysicalExtent", 8),
          ("vProtectedSpaceExtent", 6),
          ("vRedundancyGroup", 10),
          ("vSoftwareSubcomponent", 12),
          ("vStorageController", 2),
          ("vStorageDevice", 3),
          ("vUnknown", 1),
          ("vVolumeSet", 5))
    )


_A12EventSystem_Type.__name__ = "Integer32"
_A12EventSystem_Object = MibTableColumn
a12EventSystem = _A12EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 6),
    _A12EventSystem_Type()
)
a12EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventSystem.setStatus("mandatory")


class _A12EventSubsystem_Type(Integer32):
    """Custom type a12EventSubsystem based on Integer32"""
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


_A12EventSubsystem_Type.__name__ = "Integer32"
_A12EventSubsystem_Object = MibTableColumn
a12EventSubsystem = _A12EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 7),
    _A12EventSubsystem_Type()
)
a12EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventSubsystem.setStatus("mandatory")


class _A12EventSolution_Type(Integer32):
    """Custom type a12EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vNoActionIsRequired", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A12EventSolution_Type.__name__ = "Integer32"
_A12EventSolution_Object = MibTableColumn
a12EventSolution = _A12EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 8),
    _A12EventSolution_Type()
)
a12EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventSolution.setStatus("mandatory")


class _A12InstanceDataPresent_Type(Integer32):
    """Custom type a12InstanceDataPresent based on Integer32"""
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


_A12InstanceDataPresent_Type.__name__ = "Integer32"
_A12InstanceDataPresent_Object = MibTableColumn
a12InstanceDataPresent = _A12InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 9),
    _A12InstanceDataPresent_Type()
)
a12InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12InstanceDataPresent.setStatus("mandatory")
_A12EventMessage_Type = DmiDisplaystring
_A12EventMessage_Object = MibTableColumn
a12EventMessage = _A12EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 10),
    _A12EventMessage_Type()
)
a12EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventMessage.setStatus("mandatory")
_TBusPortAssociation_Object = MibTable
tBusPortAssociation = _TBusPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 13)
)
if mibBuilder.loadTexts:
    tBusPortAssociation.setStatus("mandatory")
_EBusPortAssociation_Object = MibTableRow
eBusPortAssociation = _EBusPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 13, 1)
)
eBusPortAssociation.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a13BusPortAssociationIndex"),
)
if mibBuilder.loadTexts:
    eBusPortAssociation.setStatus("mandatory")
_A13BusPortAssociationIndex_Type = DmiInteger
_A13BusPortAssociationIndex_Object = MibTableColumn
a13BusPortAssociationIndex = _A13BusPortAssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 13, 1, 1),
    _A13BusPortAssociationIndex_Type()
)
a13BusPortAssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13BusPortAssociationIndex.setStatus("mandatory")
_A13NegotiatedSpeed_Type = DmiInteger
_A13NegotiatedSpeed_Object = MibTableColumn
a13NegotiatedSpeed = _A13NegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 13, 1, 2),
    _A13NegotiatedSpeed_Type()
)
a13NegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13NegotiatedSpeed.setStatus("mandatory")
_A13NegotiatedWidth_Type = DmiInteger
_A13NegotiatedWidth_Object = MibTableColumn
a13NegotiatedWidth = _A13NegotiatedWidth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 13, 1, 3),
    _A13NegotiatedWidth_Type()
)
a13NegotiatedWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13NegotiatedWidth.setStatus("mandatory")
_TOperationalState_Object = MibTable
tOperationalState = _TOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14)
)
if mibBuilder.loadTexts:
    tOperationalState.setStatus("mandatory")
_EOperationalState_Object = MibTableRow
eOperationalState = _EOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1)
)
eOperationalState.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a14OperationalStateInstanceIndex"),
)
if mibBuilder.loadTexts:
    eOperationalState.setStatus("mandatory")
_A14OperationalStateInstanceIndex_Type = DmiInteger
_A14OperationalStateInstanceIndex_Object = MibTableColumn
a14OperationalStateInstanceIndex = _A14OperationalStateInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 1),
    _A14OperationalStateInstanceIndex_Type()
)
a14OperationalStateInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14OperationalStateInstanceIndex.setStatus("mandatory")
_A14DeviceGroupIndex_Type = DmiInteger
_A14DeviceGroupIndex_Object = MibTableColumn
a14DeviceGroupIndex = _A14DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 2),
    _A14DeviceGroupIndex_Type()
)
a14DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14DeviceGroupIndex.setStatus("mandatory")


class _A14OperationalStatus_Type(Integer32):
    """Custom type a14OperationalStatus based on Integer32"""
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


_A14OperationalStatus_Type.__name__ = "Integer32"
_A14OperationalStatus_Object = MibTableColumn
a14OperationalStatus = _A14OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 3),
    _A14OperationalStatus_Type()
)
a14OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14OperationalStatus.setStatus("mandatory")


class _A14UsageState_Type(Integer32):
    """Custom type a14UsageState based on Integer32"""
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


_A14UsageState_Type.__name__ = "Integer32"
_A14UsageState_Object = MibTableColumn
a14UsageState = _A14UsageState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 4),
    _A14UsageState_Type()
)
a14UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14UsageState.setStatus("mandatory")


class _A14AvailabilityStatus_Type(Integer32):
    """Custom type a14AvailabilityStatus based on Integer32"""
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


_A14AvailabilityStatus_Type.__name__ = "Integer32"
_A14AvailabilityStatus_Object = MibTableColumn
a14AvailabilityStatus = _A14AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 5),
    _A14AvailabilityStatus_Type()
)
a14AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14AvailabilityStatus.setStatus("mandatory")


class _A14AdministrativeState_Type(Integer32):
    """Custom type a14AdministrativeState based on Integer32"""
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


_A14AdministrativeState_Type.__name__ = "Integer32"
_A14AdministrativeState_Object = MibTableColumn
a14AdministrativeState = _A14AdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 6),
    _A14AdministrativeState_Type()
)
a14AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14AdministrativeState.setStatus("mandatory")
_A14FatalErrorCount_Type = DmiCounter
_A14FatalErrorCount_Object = MibTableColumn
a14FatalErrorCount = _A14FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 7),
    _A14FatalErrorCount_Type()
)
a14FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14FatalErrorCount.setStatus("mandatory")
_A14MajorErrorCount_Type = DmiCounter
_A14MajorErrorCount_Object = MibTableColumn
a14MajorErrorCount = _A14MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 8),
    _A14MajorErrorCount_Type()
)
a14MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14MajorErrorCount.setStatus("mandatory")
_A14WarningErrorCount_Type = DmiCounter
_A14WarningErrorCount_Object = MibTableColumn
a14WarningErrorCount = _A14WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 9),
    _A14WarningErrorCount_Type()
)
a14WarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14WarningErrorCount.setStatus("mandatory")


class _A14CurrentErrorStatus_Type(Integer32):
    """Custom type a14CurrentErrorStatus based on Integer32"""
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


_A14CurrentErrorStatus_Type.__name__ = "Integer32"
_A14CurrentErrorStatus_Object = MibTableColumn
a14CurrentErrorStatus = _A14CurrentErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 10),
    _A14CurrentErrorStatus_Type()
)
a14CurrentErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14CurrentErrorStatus.setStatus("mandatory")


class _A14DevicePredictedFailureStatus_Type(Integer32):
    """Custom type a14DevicePredictedFailureStatus based on Integer32"""
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


_A14DevicePredictedFailureStatus_Type.__name__ = "Integer32"
_A14DevicePredictedFailureStatus_Object = MibTableColumn
a14DevicePredictedFailureStatus = _A14DevicePredictedFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 14, 1, 11),
    _A14DevicePredictedFailureStatus_Type()
)
a14DevicePredictedFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14DevicePredictedFailureStatus.setStatus("mandatory")
_TSymbiosEventPolling_Object = MibTable
tSymbiosEventPolling = _TSymbiosEventPolling_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15)
)
if mibBuilder.loadTexts:
    tSymbiosEventPolling.setStatus("mandatory")
_ESymbiosEventPolling_Object = MibTableRow
eSymbiosEventPolling = _ESymbiosEventPolling_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1)
)
eSymbiosEventPolling.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSymbiosEventPolling.setStatus("mandatory")
_A15SymbiosFlag_Type = DmiInteger
_A15SymbiosFlag_Object = MibTableColumn
a15SymbiosFlag = _A15SymbiosFlag_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1, 1),
    _A15SymbiosFlag_Type()
)
a15SymbiosFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15SymbiosFlag.setStatus("mandatory")


class _A15SmartEventPolling_Type(Integer32):
    """Custom type a15SmartEventPolling based on Integer32"""
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
        *(("vDisabled", 0),
          ("vEnabled", 1),
          ("vNotApplicable", 3),
          ("vUnknown", 2))
    )


_A15SmartEventPolling_Type.__name__ = "Integer32"
_A15SmartEventPolling_Object = MibTableColumn
a15SmartEventPolling = _A15SmartEventPolling_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1, 2),
    _A15SmartEventPolling_Type()
)
a15SmartEventPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15SmartEventPolling.setStatus("mandatory")


class _A15ScanEventPolling_Type(Integer32):
    """Custom type a15ScanEventPolling based on Integer32"""
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
        *(("vDisabled", 0),
          ("vEnabled", 1),
          ("vNotApplicable", 3),
          ("vUnknown", 2))
    )


_A15ScanEventPolling_Type.__name__ = "Integer32"
_A15ScanEventPolling_Object = MibTableColumn
a15ScanEventPolling = _A15ScanEventPolling_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1, 3),
    _A15ScanEventPolling_Type()
)
a15ScanEventPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15ScanEventPolling.setStatus("mandatory")


class _A15Saf_teEventPolling_Type(Integer32):
    """Custom type a15Saf_teEventPolling based on Integer32"""
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
        *(("vDisabled", 0),
          ("vEnabled", 1),
          ("vNotApplicable", 3),
          ("vUnknown", 2))
    )


_A15Saf_teEventPolling_Type.__name__ = "Integer32"
_A15Saf_teEventPolling_Object = MibScalar
a15Saf_teEventPolling = _A15Saf_teEventPolling_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1, 4),
    _A15Saf_teEventPolling_Type()
)
a15Saf_teEventPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15Saf_teEventPolling.setStatus("mandatory")
_A15EventPollingPeriod_Type = DmiInteger
_A15EventPollingPeriod_Object = MibTableColumn
a15EventPollingPeriod = _A15EventPollingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1, 5),
    _A15EventPollingPeriod_Type()
)
a15EventPollingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15EventPollingPeriod.setStatus("mandatory")


class _A15ControlLevelForDomainValidationErrorR_Type(Integer32):
    """Custom type a15ControlLevelForDomainValidationErrorR based on Integer32"""
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
        *(("vDisabled", 1),
          ("vNotSupported", 0),
          ("vReportIfDomainValidationRequired", 2),
          ("vWhenDomainValidationRequiredAutoRun", 3))
    )


_A15ControlLevelForDomainValidationErrorR_Type.__name__ = "Integer32"
_A15ControlLevelForDomainValidationErrorR_Object = MibTableColumn
a15ControlLevelForDomainValidationErrorR = _A15ControlLevelForDomainValidationErrorR_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1, 6),
    _A15ControlLevelForDomainValidationErrorR_Type()
)
a15ControlLevelForDomainValidationErrorR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15ControlLevelForDomainValidationErrorR.setStatus("mandatory")
_A15ControlLevelForDomainValidationSchedu_Type = DmiInteger
_A15ControlLevelForDomainValidationSchedu_Object = MibTableColumn
a15ControlLevelForDomainValidationSchedu = _A15ControlLevelForDomainValidationSchedu_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 15, 1, 7),
    _A15ControlLevelForDomainValidationSchedu_Type()
)
a15ControlLevelForDomainValidationSchedu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15ControlLevelForDomainValidationSchedu.setStatus("mandatory")
_TSymbiosDevice_Object = MibTable
tSymbiosDevice = _TSymbiosDevice_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16)
)
if mibBuilder.loadTexts:
    tSymbiosDevice.setStatus("mandatory")
_ESymbiosDevice_Object = MibTableRow
eSymbiosDevice = _ESymbiosDevice_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1)
)
eSymbiosDevice.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a16SymbiosDeviceIndex"),
)
if mibBuilder.loadTexts:
    eSymbiosDevice.setStatus("mandatory")
_A16SymbiosDeviceIndex_Type = DmiInteger
_A16SymbiosDeviceIndex_Object = MibTableColumn
a16SymbiosDeviceIndex = _A16SymbiosDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 1),
    _A16SymbiosDeviceIndex_Type()
)
a16SymbiosDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16SymbiosDeviceIndex.setStatus("mandatory")


class _A16SmartReportingCapability_Type(Integer32):
    """Custom type a16SmartReportingCapability based on Integer32"""
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
        *(("vDisabled", 0),
          ("vEnabled", 1),
          ("vNotSupported", 3),
          ("vUnknown", 2))
    )


_A16SmartReportingCapability_Type.__name__ = "Integer32"
_A16SmartReportingCapability_Object = MibTableColumn
a16SmartReportingCapability = _A16SmartReportingCapability_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 2),
    _A16SmartReportingCapability_Type()
)
a16SmartReportingCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a16SmartReportingCapability.setStatus("mandatory")


class _A16ControlLevelForDomainValidationMargin_Type(Integer32):
    """Custom type a16ControlLevelForDomainValidationMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vAll", 1),
          ("vNominal", 2),
          ("vNotSupported", 0))
    )


_A16ControlLevelForDomainValidationMargin_Type.__name__ = "Integer32"
_A16ControlLevelForDomainValidationMargin_Object = MibTableColumn
a16ControlLevelForDomainValidationMargin = _A16ControlLevelForDomainValidationMargin_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 3),
    _A16ControlLevelForDomainValidationMargin_Type()
)
a16ControlLevelForDomainValidationMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a16ControlLevelForDomainValidationMargin.setStatus("mandatory")


class _A16ControlLevelForDomainValidationSkewin_Type(Integer32):
    """Custom type a16ControlLevelForDomainValidationSkewin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vAll", 1),
          ("vNominal", 2),
          ("vNotSupported", 0))
    )


_A16ControlLevelForDomainValidationSkewin_Type.__name__ = "Integer32"
_A16ControlLevelForDomainValidationSkewin_Object = MibTableColumn
a16ControlLevelForDomainValidationSkewin = _A16ControlLevelForDomainValidationSkewin_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 4),
    _A16ControlLevelForDomainValidationSkewin_Type()
)
a16ControlLevelForDomainValidationSkewin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a16ControlLevelForDomainValidationSkewin.setStatus("mandatory")


class _A16MaximumAllowedNegotiatedSpeed_Type(Integer32):
    """Custom type a16MaximumAllowedNegotiatedSpeed based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("v10MillionBytesseconds", 6),
          ("v160MillionBytesseconds", 2),
          ("v20MillionBytesseconds", 5),
          ("v40MillionBytesseconds", 4),
          ("v5MillionBytesseconds", 7),
          ("v80MillionBytesseconds", 3),
          ("vAsynchronous", 8),
          ("vMaximumRate", 1),
          ("vNotApplicable", 0))
    )


_A16MaximumAllowedNegotiatedSpeed_Type.__name__ = "Integer32"
_A16MaximumAllowedNegotiatedSpeed_Object = MibTableColumn
a16MaximumAllowedNegotiatedSpeed = _A16MaximumAllowedNegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 5),
    _A16MaximumAllowedNegotiatedSpeed_Type()
)
a16MaximumAllowedNegotiatedSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a16MaximumAllowedNegotiatedSpeed.setStatus("mandatory")


class _A16MaximumAllowedNegotiatedWidth_Type(Integer32):
    """Custom type a16MaximumAllowedNegotiatedWidth based on Integer32"""
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
        *(("vMaximumWidth", 1),
          ("vNarrow8Bits", 3),
          ("vNotApplicable", 0),
          ("vWide16Bits", 2))
    )


_A16MaximumAllowedNegotiatedWidth_Type.__name__ = "Integer32"
_A16MaximumAllowedNegotiatedWidth_Object = MibTableColumn
a16MaximumAllowedNegotiatedWidth = _A16MaximumAllowedNegotiatedWidth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 6),
    _A16MaximumAllowedNegotiatedWidth_Type()
)
a16MaximumAllowedNegotiatedWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a16MaximumAllowedNegotiatedWidth.setStatus("mandatory")
_A16DomainValidationNegotiatedSpeed_Type = DmiInteger
_A16DomainValidationNegotiatedSpeed_Object = MibTableColumn
a16DomainValidationNegotiatedSpeed = _A16DomainValidationNegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 7),
    _A16DomainValidationNegotiatedSpeed_Type()
)
a16DomainValidationNegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16DomainValidationNegotiatedSpeed.setStatus("mandatory")
_A16DomainValidationNegotiatedWidth_Type = DmiInteger
_A16DomainValidationNegotiatedWidth_Object = MibTableColumn
a16DomainValidationNegotiatedWidth = _A16DomainValidationNegotiatedWidth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 16, 1, 8),
    _A16DomainValidationNegotiatedWidth_Type()
)
a16DomainValidationNegotiatedWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16DomainValidationNegotiatedWidth.setStatus("mandatory")
_TSaf_teProcessor_Object = MibTable
tSaf_teProcessor = _TSaf_teProcessor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17)
)
if mibBuilder.loadTexts:
    tSaf_teProcessor.setStatus("mandatory")
_ESaf_teProcessor_Object = MibTableRow
eSaf_teProcessor = _ESaf_teProcessor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1)
)
eSaf_teProcessor.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a17Saf-teProcessorIndex"),
)
if mibBuilder.loadTexts:
    eSaf_teProcessor.setStatus("mandatory")
_A17Saf_teProcessorIndex_Type = DmiInteger
_A17Saf_teProcessorIndex_Object = MibScalar
a17Saf_teProcessorIndex = _A17Saf_teProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 1),
    _A17Saf_teProcessorIndex_Type()
)
a17Saf_teProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Saf_teProcessorIndex.setStatus("mandatory")
_A17StorageControllerIndex_Type = DmiInteger
_A17StorageControllerIndex_Object = MibTableColumn
a17StorageControllerIndex = _A17StorageControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 2),
    _A17StorageControllerIndex_Type()
)
a17StorageControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17StorageControllerIndex.setStatus("mandatory")
_A17ScsiId_Type = DmiInteger64X
_A17ScsiId_Object = MibTableColumn
a17ScsiId = _A17ScsiId_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 3),
    _A17ScsiId_Type()
)
a17ScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17ScsiId.setStatus("mandatory")
_A17ScsiLun_Type = DmiInteger64X
_A17ScsiLun_Object = MibTableColumn
a17ScsiLun = _A17ScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 4),
    _A17ScsiLun_Type()
)
a17ScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17ScsiLun.setStatus("mandatory")
_A17VendorId_Type = DmiDisplaystring
_A17VendorId_Object = MibTableColumn
a17VendorId = _A17VendorId_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 5),
    _A17VendorId_Type()
)
a17VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17VendorId.setStatus("mandatory")
_A17ProductId_Type = DmiDisplaystring
_A17ProductId_Object = MibTableColumn
a17ProductId = _A17ProductId_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 6),
    _A17ProductId_Type()
)
a17ProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17ProductId.setStatus("mandatory")
_A17FirmwareRevisionLevel_Type = DmiDisplaystring
_A17FirmwareRevisionLevel_Object = MibTableColumn
a17FirmwareRevisionLevel = _A17FirmwareRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 7),
    _A17FirmwareRevisionLevel_Type()
)
a17FirmwareRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17FirmwareRevisionLevel.setStatus("mandatory")
_A17EnclosureUniqueIdentifier_Type = DmiDisplaystring
_A17EnclosureUniqueIdentifier_Object = MibTableColumn
a17EnclosureUniqueIdentifier = _A17EnclosureUniqueIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 8),
    _A17EnclosureUniqueIdentifier_Type()
)
a17EnclosureUniqueIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17EnclosureUniqueIdentifier.setStatus("mandatory")
_A17Saf_teSpecificationRevisionLevel_Type = DmiDisplaystring
_A17Saf_teSpecificationRevisionLevel_Object = MibScalar
a17Saf_teSpecificationRevisionLevel = _A17Saf_teSpecificationRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 9),
    _A17Saf_teSpecificationRevisionLevel_Type()
)
a17Saf_teSpecificationRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Saf_teSpecificationRevisionLevel.setStatus("mandatory")


class _A17HasLocks_Type(Integer32):
    """Custom type a17HasLocks based on Integer32"""
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


_A17HasLocks_Type.__name__ = "Integer32"
_A17HasLocks_Object = MibTableColumn
a17HasLocks = _A17HasLocks_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 10),
    _A17HasLocks_Type()
)
a17HasLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17HasLocks.setStatus("mandatory")


class _A17HasSpeakers_Type(Integer32):
    """Custom type a17HasSpeakers based on Integer32"""
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


_A17HasSpeakers_Type.__name__ = "Integer32"
_A17HasSpeakers_Object = MibTableColumn
a17HasSpeakers = _A17HasSpeakers_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 11),
    _A17HasSpeakers_Type()
)
a17HasSpeakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17HasSpeakers.setStatus("mandatory")


class _A17DoorLocked_Type(Integer32):
    """Custom type a17DoorLocked based on Integer32"""
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


_A17DoorLocked_Type.__name__ = "Integer32"
_A17DoorLocked_Object = MibTableColumn
a17DoorLocked = _A17DoorLocked_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 12),
    _A17DoorLocked_Type()
)
a17DoorLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17DoorLocked.setStatus("mandatory")


class _A17SpeakerStatus_Type(Integer32):
    """Custom type a17SpeakerStatus based on Integer32"""
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


_A17SpeakerStatus_Type.__name__ = "Integer32"
_A17SpeakerStatus_Object = MibTableColumn
a17SpeakerStatus = _A17SpeakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 13),
    _A17SpeakerStatus_Type()
)
a17SpeakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17SpeakerStatus.setStatus("mandatory")
_A17PowerOnMinutes_Type = DmiInteger
_A17PowerOnMinutes_Object = MibTableColumn
a17PowerOnMinutes = _A17PowerOnMinutes_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 14),
    _A17PowerOnMinutes_Type()
)
a17PowerOnMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17PowerOnMinutes.setStatus("mandatory")
_A17PowerOnCycles_Type = DmiInteger
_A17PowerOnCycles_Object = MibTableColumn
a17PowerOnCycles = _A17PowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 15),
    _A17PowerOnCycles_Type()
)
a17PowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17PowerOnCycles.setStatus("mandatory")


class _A17TemperatureOutOfRange_Type(Integer32):
    """Custom type a17TemperatureOutOfRange based on Integer32"""
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


_A17TemperatureOutOfRange_Type.__name__ = "Integer32"
_A17TemperatureOutOfRange_Object = MibTableColumn
a17TemperatureOutOfRange = _A17TemperatureOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 17, 1, 16),
    _A17TemperatureOutOfRange_Type()
)
a17TemperatureOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17TemperatureOutOfRange.setStatus("mandatory")
_TSaf_teControlledFan_Object = MibTable
tSaf_teControlledFan = _TSaf_teControlledFan_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 18)
)
if mibBuilder.loadTexts:
    tSaf_teControlledFan.setStatus("mandatory")
_ESaf_teControlledFan_Object = MibTableRow
eSaf_teControlledFan = _ESaf_teControlledFan_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 18, 1)
)
eSaf_teControlledFan.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a18Saf-teControlledFanIndex"),
)
if mibBuilder.loadTexts:
    eSaf_teControlledFan.setStatus("mandatory")
_A18Saf_teControlledFanIndex_Type = DmiInteger
_A18Saf_teControlledFanIndex_Object = MibScalar
a18Saf_teControlledFanIndex = _A18Saf_teControlledFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 18, 1, 1),
    _A18Saf_teControlledFanIndex_Type()
)
a18Saf_teControlledFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a18Saf_teControlledFanIndex.setStatus("mandatory")
_A18Saf_teProcessorIndex_Type = DmiInteger
_A18Saf_teProcessorIndex_Object = MibScalar
a18Saf_teProcessorIndex = _A18Saf_teProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 18, 1, 2),
    _A18Saf_teProcessorIndex_Type()
)
a18Saf_teProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a18Saf_teProcessorIndex.setStatus("mandatory")


class _A18Status_Type(Integer32):
    """Custom type a18Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("vFanIsMalfunctioning", 1),
          ("vFanIsNotInstalled", 2),
          ("vFanIsOperational", 0),
          ("vUnknownStatus", 128))
    )


_A18Status_Type.__name__ = "Integer32"
_A18Status_Object = MibTableColumn
a18Status = _A18Status_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 18, 1, 3),
    _A18Status_Type()
)
a18Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a18Status.setStatus("mandatory")
_TSaf_teControlledPowerSupply_Object = MibTable
tSaf_teControlledPowerSupply = _TSaf_teControlledPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 19)
)
if mibBuilder.loadTexts:
    tSaf_teControlledPowerSupply.setStatus("mandatory")
_ESaf_teControlledPowerSupply_Object = MibTableRow
eSaf_teControlledPowerSupply = _ESaf_teControlledPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 19, 1)
)
eSaf_teControlledPowerSupply.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a19Saf-teControlledPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    eSaf_teControlledPowerSupply.setStatus("mandatory")
_A19Saf_teControlledPowerSupplyIndex_Type = DmiInteger
_A19Saf_teControlledPowerSupplyIndex_Object = MibScalar
a19Saf_teControlledPowerSupplyIndex = _A19Saf_teControlledPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 19, 1, 1),
    _A19Saf_teControlledPowerSupplyIndex_Type()
)
a19Saf_teControlledPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19Saf_teControlledPowerSupplyIndex.setStatus("mandatory")
_A19Saf_teProcessorIndex_Type = DmiInteger
_A19Saf_teProcessorIndex_Object = MibScalar
a19Saf_teProcessorIndex = _A19Saf_teProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 19, 1, 2),
    _A19Saf_teProcessorIndex_Type()
)
a19Saf_teProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19Saf_teProcessorIndex.setStatus("mandatory")


class _A19Status_Type(Integer32):
    """Custom type a19Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              16,
              17,
              32,
              33,
              128)
        )
    )
    namedValues = NamedValues(
        *(("vPowerSupplyIsMalfunctioningAndCommande1", 17),
          ("vPowerSupplyIsMalfunctioningAndCommanded", 16),
          ("vPowerSupplyIsNotPresent", 32),
          ("vPowerSupplyIsOperationalAndOff", 1),
          ("vPowerSupplyIsOperationalAndOn", 0),
          ("vPowerSupplyIsPresent", 33),
          ("vUnknownStatus", 128))
    )


_A19Status_Type.__name__ = "Integer32"
_A19Status_Object = MibTableColumn
a19Status = _A19Status_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 19, 1, 3),
    _A19Status_Type()
)
a19Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19Status.setStatus("mandatory")
_TSaf_teControlledSlot_Object = MibTable
tSaf_teControlledSlot = _TSaf_teControlledSlot_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20)
)
if mibBuilder.loadTexts:
    tSaf_teControlledSlot.setStatus("mandatory")
_ESaf_teControlledSlot_Object = MibTableRow
eSaf_teControlledSlot = _ESaf_teControlledSlot_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1)
)
eSaf_teControlledSlot.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a20Saf-teControlledSlotIndex"),
)
if mibBuilder.loadTexts:
    eSaf_teControlledSlot.setStatus("mandatory")
_A20Saf_teControlledSlotIndex_Type = DmiInteger
_A20Saf_teControlledSlotIndex_Object = MibScalar
a20Saf_teControlledSlotIndex = _A20Saf_teControlledSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 1),
    _A20Saf_teControlledSlotIndex_Type()
)
a20Saf_teControlledSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20Saf_teControlledSlotIndex.setStatus("mandatory")
_A20Saf_teProcessorIndex_Type = DmiInteger
_A20Saf_teProcessorIndex_Object = MibScalar
a20Saf_teProcessorIndex = _A20Saf_teProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 2),
    _A20Saf_teProcessorIndex_Type()
)
a20Saf_teProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20Saf_teProcessorIndex.setStatus("mandatory")
_A20ScsiId_Type = DmiInteger64X
_A20ScsiId_Object = MibTableColumn
a20ScsiId = _A20ScsiId_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 3),
    _A20ScsiId_Type()
)
a20ScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20ScsiId.setStatus("mandatory")
_A20NumberOfInsertions_Type = DmiInteger
_A20NumberOfInsertions_Object = MibTableColumn
a20NumberOfInsertions = _A20NumberOfInsertions_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 4),
    _A20NumberOfInsertions_Type()
)
a20NumberOfInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20NumberOfInsertions.setStatus("mandatory")


class _A20State_Type(Integer32):
    """Custom type a20State based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("vDeviceNotPresent", 5),
          ("vDeviceNotPresent-ReadyForInsertion", 6),
          ("vDevicePresent-HotSpare", 3),
          ("vDevicePresent-NotReady", 2),
          ("vDevicePresent-Ready", 1),
          ("vDevicePresent-ReadyForRemoval", 4),
          ("vUnconfigured", 7),
          ("vUnknownState", 8))
    )


_A20State_Type.__name__ = "Integer32"
_A20State_Object = MibTableColumn
a20State = _A20State_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 5),
    _A20State_Type()
)
a20State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20State.setStatus("mandatory")


class _A20Rebuild_Type(Integer32):
    """Custom type a20Rebuild based on Integer32"""
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
        *(("vNotRebuilding", 0),
          ("vRebuildInProcess", 1),
          ("vRebuildStopped", 2),
          ("vUnknownStatus", 3))
    )


_A20Rebuild_Type.__name__ = "Integer32"
_A20Rebuild_Object = MibTableColumn
a20Rebuild = _A20Rebuild_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 6),
    _A20Rebuild_Type()
)
a20Rebuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20Rebuild.setStatus("mandatory")


class _A20DeviceFault_Type(Integer32):
    """Custom type a20DeviceFault based on Integer32"""
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


_A20DeviceFault_Type.__name__ = "Integer32"
_A20DeviceFault_Object = MibTableColumn
a20DeviceFault = _A20DeviceFault_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 7),
    _A20DeviceFault_Type()
)
a20DeviceFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20DeviceFault.setStatus("mandatory")


class _A20InFailedArray_Type(Integer32):
    """Custom type a20InFailedArray based on Integer32"""
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


_A20InFailedArray_Type.__name__ = "Integer32"
_A20InFailedArray_Object = MibTableColumn
a20InFailedArray = _A20InFailedArray_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 8),
    _A20InFailedArray_Type()
)
a20InFailedArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20InFailedArray.setStatus("mandatory")


class _A20InCriticalArray_Type(Integer32):
    """Custom type a20InCriticalArray based on Integer32"""
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


_A20InCriticalArray_Type.__name__ = "Integer32"
_A20InCriticalArray_Object = MibTableColumn
a20InCriticalArray = _A20InCriticalArray_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 9),
    _A20InCriticalArray_Type()
)
a20InCriticalArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20InCriticalArray.setStatus("mandatory")


class _A20ParityCheck_Type(Integer32):
    """Custom type a20ParityCheck based on Integer32"""
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


_A20ParityCheck_Type.__name__ = "Integer32"
_A20ParityCheck_Object = MibTableColumn
a20ParityCheck = _A20ParityCheck_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 10),
    _A20ParityCheck_Type()
)
a20ParityCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20ParityCheck.setStatus("mandatory")


class _A20PredictedFault_Type(Integer32):
    """Custom type a20PredictedFault based on Integer32"""
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


_A20PredictedFault_Type.__name__ = "Integer32"
_A20PredictedFault_Object = MibTableColumn
a20PredictedFault = _A20PredictedFault_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 20, 1, 11),
    _A20PredictedFault_Type()
)
a20PredictedFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20PredictedFault.setStatus("mandatory")
_TSaf_teControlledTemperatureSensor_Object = MibTable
tSaf_teControlledTemperatureSensor = _TSaf_teControlledTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 21)
)
if mibBuilder.loadTexts:
    tSaf_teControlledTemperatureSensor.setStatus("mandatory")
_ESaf_teControlledTemperatureSensor_Object = MibTableRow
eSaf_teControlledTemperatureSensor = _ESaf_teControlledTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 21, 1)
)
eSaf_teControlledTemperatureSensor.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a21Saf-teControlledTemperatureSensorInde"),
)
if mibBuilder.loadTexts:
    eSaf_teControlledTemperatureSensor.setStatus("mandatory")
_A21Saf_teControlledTemperatureSensorInde_Type = DmiInteger
_A21Saf_teControlledTemperatureSensorInde_Object = MibScalar
a21Saf_teControlledTemperatureSensorInde = _A21Saf_teControlledTemperatureSensorInde_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 21, 1, 1),
    _A21Saf_teControlledTemperatureSensorInde_Type()
)
a21Saf_teControlledTemperatureSensorInde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21Saf_teControlledTemperatureSensorInde.setStatus("mandatory")
_A21Saf_teProcessorIndex_Type = DmiInteger
_A21Saf_teProcessorIndex_Object = MibScalar
a21Saf_teProcessorIndex = _A21Saf_teProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 21, 1, 2),
    _A21Saf_teProcessorIndex_Type()
)
a21Saf_teProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21Saf_teProcessorIndex.setStatus("mandatory")
_A21Temperature_Type = DmiInteger
_A21Temperature_Object = MibTableColumn
a21Temperature = _A21Temperature_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 21, 1, 3),
    _A21Temperature_Type()
)
a21Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21Temperature.setStatus("mandatory")
_TNetworkAdapter802PortGroup_Object = MibTable
tNetworkAdapter802PortGroup = _TNetworkAdapter802PortGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 22)
)
if mibBuilder.loadTexts:
    tNetworkAdapter802PortGroup.setStatus("mandatory")
_ENetworkAdapter802PortGroup_Object = MibTableRow
eNetworkAdapter802PortGroup = _ENetworkAdapter802PortGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 22, 1)
)
eNetworkAdapter802PortGroup.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a22PortIndex"),
)
if mibBuilder.loadTexts:
    eNetworkAdapter802PortGroup.setStatus("mandatory")
_A22PortIndex_Type = DmiInteger
_A22PortIndex_Object = MibTableColumn
a22PortIndex = _A22PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 22, 1, 1),
    _A22PortIndex_Type()
)
a22PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22PortIndex.setStatus("mandatory")
_A22PermanentNetworkAddress_Type = DmiDisplaystring
_A22PermanentNetworkAddress_Object = MibTableColumn
a22PermanentNetworkAddress = _A22PermanentNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 22, 1, 2),
    _A22PermanentNetworkAddress_Type()
)
a22PermanentNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22PermanentNetworkAddress.setStatus("mandatory")
_A22CurrentNetworkAddress_Type = DmiDisplaystring
_A22CurrentNetworkAddress_Object = MibTableColumn
a22CurrentNetworkAddress = _A22CurrentNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 22, 1, 3),
    _A22CurrentNetworkAddress_Type()
)
a22CurrentNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22CurrentNetworkAddress.setStatus("mandatory")


class _A22ConnectorType_Type(Integer32):
    """Custom type a22ConnectorType based on Integer32"""
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
        *(("vAppleAui", 10),
          ("vAui", 2),
          ("vBnc", 6),
          ("vFiberMic", 9),
          ("vStpDb9", 8),
          ("vStpRj45", 7),
          ("vUnknown", 1),
          ("vUtpCategory3", 3),
          ("vUtpCategory4", 4),
          ("vUtpCategory5", 5))
    )


_A22ConnectorType_Type.__name__ = "Integer32"
_A22ConnectorType_Object = MibTableColumn
a22ConnectorType = _A22ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 22, 1, 4),
    _A22ConnectorType_Type()
)
a22ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22ConnectorType.setStatus("mandatory")
_A22DataRate_Type = DmiInteger
_A22DataRate_Object = MibTableColumn
a22DataRate = _A22DataRate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 22, 1, 5),
    _A22DataRate_Type()
)
a22DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22DataRate.setStatus("mandatory")
_TNetworkAdapterHardwareGroup_Object = MibTable
tNetworkAdapterHardwareGroup = _TNetworkAdapterHardwareGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23)
)
if mibBuilder.loadTexts:
    tNetworkAdapterHardwareGroup.setStatus("mandatory")
_ENetworkAdapterHardwareGroup_Object = MibTableRow
eNetworkAdapterHardwareGroup = _ENetworkAdapterHardwareGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23, 1)
)
eNetworkAdapterHardwareGroup.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a23AdapterHardwareIndex"),
)
if mibBuilder.loadTexts:
    eNetworkAdapterHardwareGroup.setStatus("mandatory")


class _A23NetworkTopology_Type(Integer32):
    """Custom type a23NetworkTopology based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("v10010MbpsEthernet", 4),
          ("v100MbpsEthernet", 3),
          ("v100MbpsVgAnylan", 5),
          ("v100mbpsTokenRing", 14),
          ("v10MbpsEthernet", 2),
          ("v164MbpsToken-ring", 8),
          ("v16MbpsToken-ring", 7),
          ("v1gbpsEthernet", 15),
          ("v20MbpsArcnet", 10),
          ("v2MbpsArcnet", 9),
          ("v4MbpsToken-ring", 6),
          ("vAppletalk", 13),
          ("vAtm", 12),
          ("vFddi", 11),
          ("vOther", 1))
    )


_A23NetworkTopology_Type.__name__ = "Integer32"
_A23NetworkTopology_Object = MibTableColumn
a23NetworkTopology = _A23NetworkTopology_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23, 1, 1),
    _A23NetworkTopology_Type()
)
a23NetworkTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23NetworkTopology.setStatus("mandatory")


class _A23TransmissionCapability_Type(Integer32):
    """Custom type a23TransmissionCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFullDuplex", 2),
          ("vNormal", 1))
    )


_A23TransmissionCapability_Type.__name__ = "Integer32"
_A23TransmissionCapability_Object = MibTableColumn
a23TransmissionCapability = _A23TransmissionCapability_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23, 1, 2),
    _A23TransmissionCapability_Type()
)
a23TransmissionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23TransmissionCapability.setStatus("mandatory")
_A23NetworkAdapterRamSize_Type = DmiInteger
_A23NetworkAdapterRamSize_Object = MibTableColumn
a23NetworkAdapterRamSize = _A23NetworkAdapterRamSize_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23, 1, 3),
    _A23NetworkAdapterRamSize_Type()
)
a23NetworkAdapterRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23NetworkAdapterRamSize.setStatus("mandatory")


class _A23BusType_Type(Integer32):
    """Custom type a23BusType based on Integer32"""
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
              256)
        )
    )
    namedValues = NamedValues(
        *(("vEisa", 3),
          ("vIsa", 2),
          ("vMca", 4),
          ("vMotherboard", 256),
          ("vNec98", 9),
          ("vOther", 1),
          ("vParallel", 8),
          ("vPci", 5),
          ("vPcmcia", 7),
          ("vVl", 6))
    )


_A23BusType_Type.__name__ = "Integer32"
_A23BusType_Object = MibTableColumn
a23BusType = _A23BusType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23, 1, 4),
    _A23BusType_Type()
)
a23BusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23BusType.setStatus("mandatory")


class _A23BusWidth_Type(Integer32):
    """Custom type a23BusWidth based on Integer32"""
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
        *(("v128BitCard", 7),
          ("v16BitCard", 4),
          ("v32BitCard", 5),
          ("v64BitCard", 6),
          ("v8BitCard", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A23BusWidth_Type.__name__ = "Integer32"
_A23BusWidth_Object = MibTableColumn
a23BusWidth = _A23BusWidth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23, 1, 5),
    _A23BusWidth_Type()
)
a23BusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23BusWidth.setStatus("mandatory")
_A23AdapterHardwareIndex_Type = DmiInteger
_A23AdapterHardwareIndex_Object = MibTableColumn
a23AdapterHardwareIndex = _A23AdapterHardwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 23, 1, 6),
    _A23AdapterHardwareIndex_Type()
)
a23AdapterHardwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23AdapterHardwareIndex.setStatus("mandatory")
_TEventGenerationForPowerSupply_Object = MibTable
tEventGenerationForPowerSupply = _TEventGenerationForPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24)
)
if mibBuilder.loadTexts:
    tEventGenerationForPowerSupply.setStatus("mandatory")
_EEventGenerationForPowerSupply_Object = MibTableRow
eEventGenerationForPowerSupply = _EEventGenerationForPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1)
)
eEventGenerationForPowerSupply.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a24AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForPowerSupply.setStatus("mandatory")


class _A24EventType_Type(Integer32):
    """Custom type a24EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              256,
              257,
              258)
        )
    )
    namedValues = NamedValues(
        *(("vPowerControlRequest", 2),
          ("vPowerSupplyFailed", 256),
          ("vPowerSupplyLikelyToFail", 258),
          ("vPowerSupplyOk", 257),
          ("vPowerSupplyStatusChange", 1))
    )


_A24EventType_Type.__name__ = "Integer32"
_A24EventType_Object = MibTableColumn
a24EventType = _A24EventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 1),
    _A24EventType_Type()
)
a24EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24EventType.setStatus("mandatory")


class _A24EventSeverity_Type(Integer32):
    """Custom type a24EventSeverity based on Integer32"""
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


_A24EventSeverity_Type.__name__ = "Integer32"
_A24EventSeverity_Object = MibTableColumn
a24EventSeverity = _A24EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 2),
    _A24EventSeverity_Type()
)
a24EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24EventSeverity.setStatus("mandatory")


class _A24IsEventState_based_Type(Integer32):
    """Custom type a24IsEventState_based based on Integer32"""
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


_A24IsEventState_based_Type.__name__ = "Integer32"
_A24IsEventState_based_Object = MibScalar
a24IsEventState_based = _A24IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 3),
    _A24IsEventState_based_Type()
)
a24IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24IsEventState_based.setStatus("mandatory")
_A24EventStateKey_Type = DmiInteger
_A24EventStateKey_Object = MibTableColumn
a24EventStateKey = _A24EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 4),
    _A24EventStateKey_Type()
)
a24EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24EventStateKey.setStatus("mandatory")
_A24AssociatedGroup_Type = DmiDisplaystring
_A24AssociatedGroup_Object = MibTableColumn
a24AssociatedGroup = _A24AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 5),
    _A24AssociatedGroup_Type()
)
a24AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24AssociatedGroup.setStatus("mandatory")


class _A24EventSystem_Type(Integer32):
    """Custom type a24EventSystem based on Integer32"""
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


_A24EventSystem_Type.__name__ = "Integer32"
_A24EventSystem_Object = MibTableColumn
a24EventSystem = _A24EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 6),
    _A24EventSystem_Type()
)
a24EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24EventSystem.setStatus("mandatory")


class _A24EventSubsystem_Type(Integer32):
    """Custom type a24EventSubsystem based on Integer32"""
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


_A24EventSubsystem_Type.__name__ = "Integer32"
_A24EventSubsystem_Object = MibScalar
a24EventSubsystem = _A24EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 7),
    _A24EventSubsystem_Type()
)
a24EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24EventSubsystem.setStatus("mandatory")


class _A24IsInstanceDataPresent_Type(Integer32):
    """Custom type a24IsInstanceDataPresent based on Integer32"""
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


_A24IsInstanceDataPresent_Type.__name__ = "Integer32"
_A24IsInstanceDataPresent_Object = MibTableColumn
a24IsInstanceDataPresent = _A24IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 8),
    _A24IsInstanceDataPresent_Type()
)
a24IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24IsInstanceDataPresent.setStatus("mandatory")
_A24EventMessage_Type = DmiDisplaystring
_A24EventMessage_Object = MibTableColumn
a24EventMessage = _A24EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 24, 1, 9),
    _A24EventMessage_Type()
)
a24EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24EventMessage.setStatus("mandatory")
_TEventGenerationForTemperatureProbe_Object = MibTable
tEventGenerationForTemperatureProbe = _TEventGenerationForTemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25)
)
if mibBuilder.loadTexts:
    tEventGenerationForTemperatureProbe.setStatus("mandatory")
_EEventGenerationForTemperatureProbe_Object = MibTableRow
eEventGenerationForTemperatureProbe = _EEventGenerationForTemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1)
)
eEventGenerationForTemperatureProbe.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a25AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForTemperatureProbe.setStatus("mandatory")


class _A25EventType_Type(Integer32):
    """Custom type a25EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vTemperatureOutOfRange", 1)
    )


_A25EventType_Type.__name__ = "Integer32"
_A25EventType_Object = MibTableColumn
a25EventType = _A25EventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 1),
    _A25EventType_Type()
)
a25EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25EventType.setStatus("mandatory")


class _A25EventSeverity_Type(Integer32):
    """Custom type a25EventSeverity based on Integer32"""
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


_A25EventSeverity_Type.__name__ = "Integer32"
_A25EventSeverity_Object = MibTableColumn
a25EventSeverity = _A25EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 2),
    _A25EventSeverity_Type()
)
a25EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25EventSeverity.setStatus("mandatory")


class _A25IsEventState_based_Type(Integer32):
    """Custom type a25IsEventState_based based on Integer32"""
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


_A25IsEventState_based_Type.__name__ = "Integer32"
_A25IsEventState_based_Object = MibScalar
a25IsEventState_based = _A25IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 3),
    _A25IsEventState_based_Type()
)
a25IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25IsEventState_based.setStatus("mandatory")
_A25EventStateKey_Type = DmiInteger
_A25EventStateKey_Object = MibTableColumn
a25EventStateKey = _A25EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 4),
    _A25EventStateKey_Type()
)
a25EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25EventStateKey.setStatus("mandatory")
_A25AssociatedGroup_Type = DmiDisplaystring
_A25AssociatedGroup_Object = MibTableColumn
a25AssociatedGroup = _A25AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 5),
    _A25AssociatedGroup_Type()
)
a25AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25AssociatedGroup.setStatus("mandatory")


class _A25EventSystem_Type(Integer32):
    """Custom type a25EventSystem based on Integer32"""
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


_A25EventSystem_Type.__name__ = "Integer32"
_A25EventSystem_Object = MibTableColumn
a25EventSystem = _A25EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 6),
    _A25EventSystem_Type()
)
a25EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25EventSystem.setStatus("mandatory")


class _A25EventSubsystem_Type(Integer32):
    """Custom type a25EventSubsystem based on Integer32"""
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


_A25EventSubsystem_Type.__name__ = "Integer32"
_A25EventSubsystem_Object = MibTableColumn
a25EventSubsystem = _A25EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 7),
    _A25EventSubsystem_Type()
)
a25EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25EventSubsystem.setStatus("mandatory")


class _A25IsInstanceDataPresent_Type(Integer32):
    """Custom type a25IsInstanceDataPresent based on Integer32"""
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


_A25IsInstanceDataPresent_Type.__name__ = "Integer32"
_A25IsInstanceDataPresent_Object = MibTableColumn
a25IsInstanceDataPresent = _A25IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 8),
    _A25IsInstanceDataPresent_Type()
)
a25IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25IsInstanceDataPresent.setStatus("mandatory")
_A25EventMessage_Type = DmiDisplaystring
_A25EventMessage_Object = MibTableColumn
a25EventMessage = _A25EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 25, 1, 9),
    _A25EventMessage_Type()
)
a25EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25EventMessage.setStatus("mandatory")
_TEventGenerationForFans_Object = MibTable
tEventGenerationForFans = _TEventGenerationForFans_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26)
)
if mibBuilder.loadTexts:
    tEventGenerationForFans.setStatus("mandatory")
_EEventGenerationForFans_Object = MibTableRow
eEventGenerationForFans = _EEventGenerationForFans_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1)
)
eEventGenerationForFans.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a26AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForFans.setStatus("mandatory")


class _A26EventType_Type(Integer32):
    """Custom type a26EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vFanFailure", 1)
    )


_A26EventType_Type.__name__ = "Integer32"
_A26EventType_Object = MibTableColumn
a26EventType = _A26EventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 1),
    _A26EventType_Type()
)
a26EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26EventType.setStatus("mandatory")


class _A26EventSeverity_Type(Integer32):
    """Custom type a26EventSeverity based on Integer32"""
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


_A26EventSeverity_Type.__name__ = "Integer32"
_A26EventSeverity_Object = MibTableColumn
a26EventSeverity = _A26EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 2),
    _A26EventSeverity_Type()
)
a26EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26EventSeverity.setStatus("mandatory")


class _A26IsEventState_based_Type(Integer32):
    """Custom type a26IsEventState_based based on Integer32"""
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


_A26IsEventState_based_Type.__name__ = "Integer32"
_A26IsEventState_based_Object = MibScalar
a26IsEventState_based = _A26IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 3),
    _A26IsEventState_based_Type()
)
a26IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26IsEventState_based.setStatus("mandatory")
_A26EventStateKey_Type = DmiInteger
_A26EventStateKey_Object = MibTableColumn
a26EventStateKey = _A26EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 4),
    _A26EventStateKey_Type()
)
a26EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26EventStateKey.setStatus("mandatory")
_A26AssociatedGroup_Type = DmiDisplaystring
_A26AssociatedGroup_Object = MibTableColumn
a26AssociatedGroup = _A26AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 5),
    _A26AssociatedGroup_Type()
)
a26AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26AssociatedGroup.setStatus("mandatory")


class _A26EventSystem_Type(Integer32):
    """Custom type a26EventSystem based on Integer32"""
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


_A26EventSystem_Type.__name__ = "Integer32"
_A26EventSystem_Object = MibTableColumn
a26EventSystem = _A26EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 6),
    _A26EventSystem_Type()
)
a26EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26EventSystem.setStatus("mandatory")


class _A26EventSubsystem_Type(Integer32):
    """Custom type a26EventSubsystem based on Integer32"""
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


_A26EventSubsystem_Type.__name__ = "Integer32"
_A26EventSubsystem_Object = MibTableColumn
a26EventSubsystem = _A26EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 7),
    _A26EventSubsystem_Type()
)
a26EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26EventSubsystem.setStatus("mandatory")


class _A26IsInstanceDataPresent_Type(Integer32):
    """Custom type a26IsInstanceDataPresent based on Integer32"""
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


_A26IsInstanceDataPresent_Type.__name__ = "Integer32"
_A26IsInstanceDataPresent_Object = MibTableColumn
a26IsInstanceDataPresent = _A26IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 8),
    _A26IsInstanceDataPresent_Type()
)
a26IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26IsInstanceDataPresent.setStatus("mandatory")
_A26EventMessage_Type = DmiDisplaystring
_A26EventMessage_Object = MibTableColumn
a26EventMessage = _A26EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 26, 1, 9),
    _A26EventMessage_Type()
)
a26EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26EventMessage.setStatus("mandatory")
_TSymbiosHealth_Object = MibTable
tSymbiosHealth = _TSymbiosHealth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27)
)
if mibBuilder.loadTexts:
    tSymbiosHealth.setStatus("mandatory")
_ESymbiosHealth_Object = MibTableRow
eSymbiosHealth = _ESymbiosHealth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1)
)
eSymbiosHealth.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSymbiosHealth.setStatus("mandatory")


class _A27OverallHealthStatus_Type(Integer32):
    """Custom type a27OverallHealthStatus based on Integer32"""
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
        *(("vDegraded", 4),
          ("vNon-recoverable", 5),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A27OverallHealthStatus_Type.__name__ = "Integer32"
_A27OverallHealthStatus_Object = MibTableColumn
a27OverallHealthStatus = _A27OverallHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 1),
    _A27OverallHealthStatus_Type()
)
a27OverallHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27OverallHealthStatus.setStatus("mandatory")


class _A27OverallControllerHealthStatus_Type(Integer32):
    """Custom type a27OverallControllerHealthStatus based on Integer32"""
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
        *(("vDegraded", 4),
          ("vNon-recoverable", 5),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A27OverallControllerHealthStatus_Type.__name__ = "Integer32"
_A27OverallControllerHealthStatus_Object = MibTableColumn
a27OverallControllerHealthStatus = _A27OverallControllerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 2),
    _A27OverallControllerHealthStatus_Type()
)
a27OverallControllerHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27OverallControllerHealthStatus.setStatus("mandatory")
_A27Non_recoverableControllers_Type = DmiInteger
_A27Non_recoverableControllers_Object = MibScalar
a27Non_recoverableControllers = _A27Non_recoverableControllers_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 3),
    _A27Non_recoverableControllers_Type()
)
a27Non_recoverableControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27Non_recoverableControllers.setStatus("mandatory")
_A27DegradedControllers_Type = DmiInteger
_A27DegradedControllers_Object = MibTableColumn
a27DegradedControllers = _A27DegradedControllers_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 4),
    _A27DegradedControllers_Type()
)
a27DegradedControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27DegradedControllers.setStatus("mandatory")


class _A27OverallDeviceHealthStatus_Type(Integer32):
    """Custom type a27OverallDeviceHealthStatus based on Integer32"""
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
        *(("vDegraded", 4),
          ("vNon-recoverable", 5),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A27OverallDeviceHealthStatus_Type.__name__ = "Integer32"
_A27OverallDeviceHealthStatus_Object = MibTableColumn
a27OverallDeviceHealthStatus = _A27OverallDeviceHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 5),
    _A27OverallDeviceHealthStatus_Type()
)
a27OverallDeviceHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27OverallDeviceHealthStatus.setStatus("mandatory")
_A27Non_recoverableDevices_Type = DmiInteger
_A27Non_recoverableDevices_Object = MibScalar
a27Non_recoverableDevices = _A27Non_recoverableDevices_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 6),
    _A27Non_recoverableDevices_Type()
)
a27Non_recoverableDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27Non_recoverableDevices.setStatus("mandatory")
_A27DegradedDevices_Type = DmiInteger
_A27DegradedDevices_Object = MibTableColumn
a27DegradedDevices = _A27DegradedDevices_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 7),
    _A27DegradedDevices_Type()
)
a27DegradedDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27DegradedDevices.setStatus("mandatory")
_A27DataValuesTimeStamp_Type = DmiDateX
_A27DataValuesTimeStamp_Object = MibTableColumn
a27DataValuesTimeStamp = _A27DataValuesTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 8),
    _A27DataValuesTimeStamp_Type()
)
a27DataValuesTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27DataValuesTimeStamp.setStatus("mandatory")
_A27HardwareTimeStamp_Type = DmiDateX
_A27HardwareTimeStamp_Object = MibTableColumn
a27HardwareTimeStamp = _A27HardwareTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 27, 1, 9),
    _A27HardwareTimeStamp_Type()
)
a27HardwareTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27HardwareTimeStamp.setStatus("mandatory")
_TSymbiosController_Object = MibTable
tSymbiosController = _TSymbiosController_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28)
)
if mibBuilder.loadTexts:
    tSymbiosController.setStatus("mandatory")
_ESymbiosController_Object = MibTableRow
eSymbiosController = _ESymbiosController_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28, 1)
)
eSymbiosController.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a28SymbiosControllerIndex"),
)
if mibBuilder.loadTexts:
    eSymbiosController.setStatus("mandatory")
_A28SymbiosControllerIndex_Type = DmiInteger
_A28SymbiosControllerIndex_Object = MibTableColumn
a28SymbiosControllerIndex = _A28SymbiosControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28, 1, 1),
    _A28SymbiosControllerIndex_Type()
)
a28SymbiosControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28SymbiosControllerIndex.setStatus("mandatory")
_A28LastRunDateForDv_Type = DmiDateX
_A28LastRunDateForDv_Object = MibTableColumn
a28LastRunDateForDv = _A28LastRunDateForDv_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28, 1, 2),
    _A28LastRunDateForDv_Type()
)
a28LastRunDateForDv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28LastRunDateForDv.setStatus("mandatory")
_A28IoFactorForDvErrorRate_Type = DmiInteger
_A28IoFactorForDvErrorRate_Object = MibTableColumn
a28IoFactorForDvErrorRate = _A28IoFactorForDvErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28, 1, 3),
    _A28IoFactorForDvErrorRate_Type()
)
a28IoFactorForDvErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a28IoFactorForDvErrorRate.setStatus("mandatory")
_A28TimeFactorForDvErrorRate_Type = DmiInteger
_A28TimeFactorForDvErrorRate_Object = MibTableColumn
a28TimeFactorForDvErrorRate = _A28TimeFactorForDvErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28, 1, 4),
    _A28TimeFactorForDvErrorRate_Type()
)
a28TimeFactorForDvErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a28TimeFactorForDvErrorRate.setStatus("mandatory")
_A28ErrorCountFactorForDvErrorRate_Type = DmiInteger
_A28ErrorCountFactorForDvErrorRate_Object = MibTableColumn
a28ErrorCountFactorForDvErrorRate = _A28ErrorCountFactorForDvErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28, 1, 5),
    _A28ErrorCountFactorForDvErrorRate_Type()
)
a28ErrorCountFactorForDvErrorRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a28ErrorCountFactorForDvErrorRate.setStatus("mandatory")


class _A28DvStatus_Type(Integer32):
    """Custom type a28DvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vDomainValidationCompletedByTheDriver", 1),
          ("vDomainValidationCompletedWithChanges", 3),
          ("vDomainValidationCompletedWithNoChanges", 2),
          ("vDomainValidationCurrentlyRunning", 4),
          ("vDomainValidationNeedsToBeRun", 6),
          ("vDomainValidationTerminated", 5),
          ("vNotApplicable", 0))
    )


_A28DvStatus_Type.__name__ = "Integer32"
_A28DvStatus_Object = MibTableColumn
a28DvStatus = _A28DvStatus_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 28, 1, 6),
    _A28DvStatus_Type()
)
a28DvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a28DvStatus.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "SYMBIOSDMI20MIFDEFINITIONID22-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trap1forStorageDevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 0, 1)
)
trap1forStorageDevices.setObjects(
      *(("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6StorageDevicesEventType"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSeverity"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventIsStateBased"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventStateKey"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6AssociatedGroup"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSubsystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSolution"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6InstanceDataPresent"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventMessage"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a5StorageDeviceIndex"))
)
if mibBuilder.loadTexts:
    trap1forStorageDevices.setStatus(
        ""
    )

trap2forStorageDevices = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 6, 1, 0, 2)
)
trap2forStorageDevices.setObjects(
      *(("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6StorageDevicesEventType"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSeverity"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventIsStateBased"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventStateKey"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6AssociatedGroup"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSubsystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventSolution"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6InstanceDataPresent"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a6EventMessage"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a5StorageDeviceIndex"))
)
if mibBuilder.loadTexts:
    trap2forStorageDevices.setStatus(
        ""
    )

trap3forStorageController = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 8, 1, 0, 3)
)
trap3forStorageController.setObjects(
      *(("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8StorageControllerEventType"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8EventSeverity"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8EventIsStateBased"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8EventStateKey"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8AssociatedGroup"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8EventSystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8EventSubsystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8EventSolution"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8InstanceDataPresent"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a8EventMessage"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a7ControllerIndex"))
)
if mibBuilder.loadTexts:
    trap3forStorageController.setStatus(
        ""
    )

trap4forMassStorageAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 0, 4)
)
trap4forMassStorageAssociation.setObjects(
      *(("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12MassStorageAssociationEventType"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSeverity"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventIsStateBased"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventStateKey"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12AssociatedGroup"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSubsystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSolution"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12InstanceDataPresent"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventMessage"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a11AssociationIndex"))
)
if mibBuilder.loadTexts:
    trap4forMassStorageAssociation.setStatus(
        ""
    )

trap5forMassStorageAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 0, 5)
)
trap5forMassStorageAssociation.setObjects(
      *(("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12MassStorageAssociationEventType"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSeverity"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventIsStateBased"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventStateKey"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12AssociatedGroup"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSubsystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSolution"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12InstanceDataPresent"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventMessage"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a11AssociationIndex"))
)
if mibBuilder.loadTexts:
    trap5forMassStorageAssociation.setStatus(
        ""
    )

trap6forMassStorageAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 0, 6)
)
trap6forMassStorageAssociation.setObjects(
      *(("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12MassStorageAssociationEventType"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSeverity"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventIsStateBased"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventStateKey"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12AssociatedGroup"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSubsystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSolution"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12InstanceDataPresent"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventMessage"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a11AssociationIndex"))
)
if mibBuilder.loadTexts:
    trap6forMassStorageAssociation.setStatus(
        ""
    )

trap7forMassStorageAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 22, 1, 12, 1, 0, 7)
)
trap7forMassStorageAssociation.setObjects(
      *(("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12MassStorageAssociationEventType"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSeverity"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventIsStateBased"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventStateKey"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12AssociatedGroup"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSubsystem"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventSolution"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12InstanceDataPresent"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a12EventMessage"),
        ("SYMBIOSDMI20MIFDEFINITIONID22-MIB", "a11AssociationIndex"))
)
if mibBuilder.loadTexts:
    trap7forMassStorageAssociation.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMBIOSDMI20MIFDEFINITIONID22-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiInteger64X": DmiInteger64X,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "symbios": symbios,
       "cosprings": cosprings,
       "scsi": scsi,
       "fam8xx": fam8xx,
       "id22": id22,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tSubcomponentSoftware": tSubcomponentSoftware,
       "eSubcomponentSoftware": eSubcomponentSoftware,
       "a2SoftwareIndex": a2SoftwareIndex,
       "a2Type": a2Type,
       "a2Vendor": a2Vendor,
       "a2Version": a2Version,
       "a2Description": a2Description,
       "a2IdentificationCode": a2IdentificationCode,
       "a2LanguageEdition": a2LanguageEdition,
       "a2InterfaceDescription": a2InterfaceDescription,
       "a2InterfaceVersion": a2InterfaceVersion,
       "tWorldwideIdentifer": tWorldwideIdentifer,
       "eWorldwideIdentifer": eWorldwideIdentifer,
       "a3WorldwideIdentifierIndex": a3WorldwideIdentifierIndex,
       "a3WorldwideIdentifierType": a3WorldwideIdentifierType,
       "a3WorldwideIdentifier": a3WorldwideIdentifier,
       "tFieldReplaceableUnit": tFieldReplaceableUnit,
       "eFieldReplaceableUnit": eFieldReplaceableUnit,
       "a4FruIndex": a4FruIndex,
       "a4DeviceGroupIndex": a4DeviceGroupIndex,
       "a4Description": a4Description,
       "a4Manufacturer": a4Manufacturer,
       "a4Model": a4Model,
       "a4PartNumber": a4PartNumber,
       "a4FruSerialNumber": a4FruSerialNumber,
       "a4RevisionLevel": a4RevisionLevel,
       "a4WarrantyStartDate": a4WarrantyStartDate,
       "a4WarrantyDuration": a4WarrantyDuration,
       "a4SupportPhoneNumber": a4SupportPhoneNumber,
       "a4FruInternetUniformResourceLocator": a4FruInternetUniformResourceLocator,
       "tStorageDevices": tStorageDevices,
       "eStorageDevices": eStorageDevices,
       "a5StorageDeviceIndex": a5StorageDeviceIndex,
       "a5Type": a5Type,
       "a5TypeDescription": a5TypeDescription,
       "a5Sub-identifier": a5Sub_identifier,
       "a5MediaDataBlockSize": a5MediaDataBlockSize,
       "a5FormattedMediaCapacity": a5FormattedMediaCapacity,
       "a5RemovableDevice": a5RemovableDevice,
       "a5DeviceLoaded": a5DeviceLoaded,
       "a5RemovableMedia": a5RemovableMedia,
       "a5MediaLoaded": a5MediaLoaded,
       "a5Compression": a5Compression,
       "a5Encryption": a5Encryption,
       "tStorageDevicesEvents": tStorageDevicesEvents,
       "eStorageDevicesEvents": eStorageDevicesEvents,
       "trap1forStorageDevices": trap1forStorageDevices,
       "trap2forStorageDevices": trap2forStorageDevices,
       "a6StorageDevicesEventType": a6StorageDevicesEventType,
       "a6EventSeverity": a6EventSeverity,
       "a6EventIsStateBased": a6EventIsStateBased,
       "a6EventStateKey": a6EventStateKey,
       "a6AssociatedGroup": a6AssociatedGroup,
       "a6EventSystem": a6EventSystem,
       "a6EventSubsystem": a6EventSubsystem,
       "a6EventSolution": a6EventSolution,
       "a6InstanceDataPresent": a6InstanceDataPresent,
       "a6EventMessage": a6EventMessage,
       "tStorageController": tStorageController,
       "eStorageController": eStorageController,
       "a7ControllerIndex": a7ControllerIndex,
       "a7Identification": a7Identification,
       "a7ProtectionManagement": a7ProtectionManagement,
       "a7BusMaster": a7BusMaster,
       "a7SecondsSinceLastPower-up": a7SecondsSinceLastPower_up,
       "tStorageControllerEvents": tStorageControllerEvents,
       "eStorageControllerEvents": eStorageControllerEvents,
       "trap3forStorageController": trap3forStorageController,
       "a8StorageControllerEventType": a8StorageControllerEventType,
       "a8EventSeverity": a8EventSeverity,
       "a8EventIsStateBased": a8EventIsStateBased,
       "a8EventStateKey": a8EventStateKey,
       "a8AssociatedGroup": a8AssociatedGroup,
       "a8EventSystem": a8EventSystem,
       "a8EventSubsystem": a8EventSubsystem,
       "a8EventSolution": a8EventSolution,
       "a8InstanceDataPresent": a8InstanceDataPresent,
       "a8EventMessage": a8EventMessage,
       "tBusPort": tBusPort,
       "eBusPort": eBusPort,
       "a9BusPortIndex": a9BusPortIndex,
       "a9Protocol": a9Protocol,
       "a9ProtocolDescription": a9ProtocolDescription,
       "a9SignalCharacteristics": a9SignalCharacteristics,
       "a9AddressDescriptor": a9AddressDescriptor,
       "a9Isochronous": a9Isochronous,
       "a9MaximumWidth": a9MaximumWidth,
       "a9MaximumTransferRate": a9MaximumTransferRate,
       "a9MaximumNumberOfAttachments": a9MaximumNumberOfAttachments,
       "a9ConnectorType": a9ConnectorType,
       "a9ConnectorTypeDescription": a9ConnectorTypeDescription,
       "a9ConnectorGender": a9ConnectorGender,
       "tFibreChannelBusPortExtensions": tFibreChannelBusPortExtensions,
       "eFibreChannelBusPortExtensions": eFibreChannelBusPortExtensions,
       "a10BusPortIndex": a10BusPortIndex,
       "a10EndToEndCredit": a10EndToEndCredit,
       "a10BufferToBufferCredit": a10BufferToBufferCredit,
       "a10LinkType": a10LinkType,
       "a10FlowControlClassType": a10FlowControlClassType,
       "a10FlowControlAcknowledgmentType": a10FlowControlAcknowledgmentType,
       "a10FabricTopology": a10FabricTopology,
       "tMassStorageAssociation": tMassStorageAssociation,
       "eMassStorageAssociation": eMassStorageAssociation,
       "a11AssociationIndex": a11AssociationIndex,
       "a11Type": a11Type,
       "a11Reference1": a11Reference1,
       "a11Reference2": a11Reference2,
       "tMassStorageAssociationEvents": tMassStorageAssociationEvents,
       "eMassStorageAssociationEvents": eMassStorageAssociationEvents,
       "trap4forMassStorageAssociation": trap4forMassStorageAssociation,
       "trap5forMassStorageAssociation": trap5forMassStorageAssociation,
       "trap6forMassStorageAssociation": trap6forMassStorageAssociation,
       "trap7forMassStorageAssociation": trap7forMassStorageAssociation,
       "a12MassStorageAssociationEventType": a12MassStorageAssociationEventType,
       "a12EventSeverity": a12EventSeverity,
       "a12EventIsStateBased": a12EventIsStateBased,
       "a12EventStateKey": a12EventStateKey,
       "a12AssociatedGroup": a12AssociatedGroup,
       "a12EventSystem": a12EventSystem,
       "a12EventSubsystem": a12EventSubsystem,
       "a12EventSolution": a12EventSolution,
       "a12InstanceDataPresent": a12InstanceDataPresent,
       "a12EventMessage": a12EventMessage,
       "tBusPortAssociation": tBusPortAssociation,
       "eBusPortAssociation": eBusPortAssociation,
       "a13BusPortAssociationIndex": a13BusPortAssociationIndex,
       "a13NegotiatedSpeed": a13NegotiatedSpeed,
       "a13NegotiatedWidth": a13NegotiatedWidth,
       "tOperationalState": tOperationalState,
       "eOperationalState": eOperationalState,
       "a14OperationalStateInstanceIndex": a14OperationalStateInstanceIndex,
       "a14DeviceGroupIndex": a14DeviceGroupIndex,
       "a14OperationalStatus": a14OperationalStatus,
       "a14UsageState": a14UsageState,
       "a14AvailabilityStatus": a14AvailabilityStatus,
       "a14AdministrativeState": a14AdministrativeState,
       "a14FatalErrorCount": a14FatalErrorCount,
       "a14MajorErrorCount": a14MajorErrorCount,
       "a14WarningErrorCount": a14WarningErrorCount,
       "a14CurrentErrorStatus": a14CurrentErrorStatus,
       "a14DevicePredictedFailureStatus": a14DevicePredictedFailureStatus,
       "tSymbiosEventPolling": tSymbiosEventPolling,
       "eSymbiosEventPolling": eSymbiosEventPolling,
       "a15SymbiosFlag": a15SymbiosFlag,
       "a15SmartEventPolling": a15SmartEventPolling,
       "a15ScanEventPolling": a15ScanEventPolling,
       "a15Saf-teEventPolling": a15Saf_teEventPolling,
       "a15EventPollingPeriod": a15EventPollingPeriod,
       "a15ControlLevelForDomainValidationErrorR": a15ControlLevelForDomainValidationErrorR,
       "a15ControlLevelForDomainValidationSchedu": a15ControlLevelForDomainValidationSchedu,
       "tSymbiosDevice": tSymbiosDevice,
       "eSymbiosDevice": eSymbiosDevice,
       "a16SymbiosDeviceIndex": a16SymbiosDeviceIndex,
       "a16SmartReportingCapability": a16SmartReportingCapability,
       "a16ControlLevelForDomainValidationMargin": a16ControlLevelForDomainValidationMargin,
       "a16ControlLevelForDomainValidationSkewin": a16ControlLevelForDomainValidationSkewin,
       "a16MaximumAllowedNegotiatedSpeed": a16MaximumAllowedNegotiatedSpeed,
       "a16MaximumAllowedNegotiatedWidth": a16MaximumAllowedNegotiatedWidth,
       "a16DomainValidationNegotiatedSpeed": a16DomainValidationNegotiatedSpeed,
       "a16DomainValidationNegotiatedWidth": a16DomainValidationNegotiatedWidth,
       "tSaf-teProcessor": tSaf_teProcessor,
       "eSaf-teProcessor": eSaf_teProcessor,
       "a17Saf-teProcessorIndex": a17Saf_teProcessorIndex,
       "a17StorageControllerIndex": a17StorageControllerIndex,
       "a17ScsiId": a17ScsiId,
       "a17ScsiLun": a17ScsiLun,
       "a17VendorId": a17VendorId,
       "a17ProductId": a17ProductId,
       "a17FirmwareRevisionLevel": a17FirmwareRevisionLevel,
       "a17EnclosureUniqueIdentifier": a17EnclosureUniqueIdentifier,
       "a17Saf-teSpecificationRevisionLevel": a17Saf_teSpecificationRevisionLevel,
       "a17HasLocks": a17HasLocks,
       "a17HasSpeakers": a17HasSpeakers,
       "a17DoorLocked": a17DoorLocked,
       "a17SpeakerStatus": a17SpeakerStatus,
       "a17PowerOnMinutes": a17PowerOnMinutes,
       "a17PowerOnCycles": a17PowerOnCycles,
       "a17TemperatureOutOfRange": a17TemperatureOutOfRange,
       "tSaf-teControlledFan": tSaf_teControlledFan,
       "eSaf-teControlledFan": eSaf_teControlledFan,
       "a18Saf-teControlledFanIndex": a18Saf_teControlledFanIndex,
       "a18Saf-teProcessorIndex": a18Saf_teProcessorIndex,
       "a18Status": a18Status,
       "tSaf-teControlledPowerSupply": tSaf_teControlledPowerSupply,
       "eSaf-teControlledPowerSupply": eSaf_teControlledPowerSupply,
       "a19Saf-teControlledPowerSupplyIndex": a19Saf_teControlledPowerSupplyIndex,
       "a19Saf-teProcessorIndex": a19Saf_teProcessorIndex,
       "a19Status": a19Status,
       "tSaf-teControlledSlot": tSaf_teControlledSlot,
       "eSaf-teControlledSlot": eSaf_teControlledSlot,
       "a20Saf-teControlledSlotIndex": a20Saf_teControlledSlotIndex,
       "a20Saf-teProcessorIndex": a20Saf_teProcessorIndex,
       "a20ScsiId": a20ScsiId,
       "a20NumberOfInsertions": a20NumberOfInsertions,
       "a20State": a20State,
       "a20Rebuild": a20Rebuild,
       "a20DeviceFault": a20DeviceFault,
       "a20InFailedArray": a20InFailedArray,
       "a20InCriticalArray": a20InCriticalArray,
       "a20ParityCheck": a20ParityCheck,
       "a20PredictedFault": a20PredictedFault,
       "tSaf-teControlledTemperatureSensor": tSaf_teControlledTemperatureSensor,
       "eSaf-teControlledTemperatureSensor": eSaf_teControlledTemperatureSensor,
       "a21Saf-teControlledTemperatureSensorInde": a21Saf_teControlledTemperatureSensorInde,
       "a21Saf-teProcessorIndex": a21Saf_teProcessorIndex,
       "a21Temperature": a21Temperature,
       "tNetworkAdapter802PortGroup": tNetworkAdapter802PortGroup,
       "eNetworkAdapter802PortGroup": eNetworkAdapter802PortGroup,
       "a22PortIndex": a22PortIndex,
       "a22PermanentNetworkAddress": a22PermanentNetworkAddress,
       "a22CurrentNetworkAddress": a22CurrentNetworkAddress,
       "a22ConnectorType": a22ConnectorType,
       "a22DataRate": a22DataRate,
       "tNetworkAdapterHardwareGroup": tNetworkAdapterHardwareGroup,
       "eNetworkAdapterHardwareGroup": eNetworkAdapterHardwareGroup,
       "a23NetworkTopology": a23NetworkTopology,
       "a23TransmissionCapability": a23TransmissionCapability,
       "a23NetworkAdapterRamSize": a23NetworkAdapterRamSize,
       "a23BusType": a23BusType,
       "a23BusWidth": a23BusWidth,
       "a23AdapterHardwareIndex": a23AdapterHardwareIndex,
       "tEventGenerationForPowerSupply": tEventGenerationForPowerSupply,
       "eEventGenerationForPowerSupply": eEventGenerationForPowerSupply,
       "a24EventType": a24EventType,
       "a24EventSeverity": a24EventSeverity,
       "a24IsEventState-based": a24IsEventState_based,
       "a24EventStateKey": a24EventStateKey,
       "a24AssociatedGroup": a24AssociatedGroup,
       "a24EventSystem": a24EventSystem,
       "a24EventSubsystem": a24EventSubsystem,
       "a24IsInstanceDataPresent": a24IsInstanceDataPresent,
       "a24EventMessage": a24EventMessage,
       "tEventGenerationForTemperatureProbe": tEventGenerationForTemperatureProbe,
       "eEventGenerationForTemperatureProbe": eEventGenerationForTemperatureProbe,
       "a25EventType": a25EventType,
       "a25EventSeverity": a25EventSeverity,
       "a25IsEventState-based": a25IsEventState_based,
       "a25EventStateKey": a25EventStateKey,
       "a25AssociatedGroup": a25AssociatedGroup,
       "a25EventSystem": a25EventSystem,
       "a25EventSubsystem": a25EventSubsystem,
       "a25IsInstanceDataPresent": a25IsInstanceDataPresent,
       "a25EventMessage": a25EventMessage,
       "tEventGenerationForFans": tEventGenerationForFans,
       "eEventGenerationForFans": eEventGenerationForFans,
       "a26EventType": a26EventType,
       "a26EventSeverity": a26EventSeverity,
       "a26IsEventState-based": a26IsEventState_based,
       "a26EventStateKey": a26EventStateKey,
       "a26AssociatedGroup": a26AssociatedGroup,
       "a26EventSystem": a26EventSystem,
       "a26EventSubsystem": a26EventSubsystem,
       "a26IsInstanceDataPresent": a26IsInstanceDataPresent,
       "a26EventMessage": a26EventMessage,
       "tSymbiosHealth": tSymbiosHealth,
       "eSymbiosHealth": eSymbiosHealth,
       "a27OverallHealthStatus": a27OverallHealthStatus,
       "a27OverallControllerHealthStatus": a27OverallControllerHealthStatus,
       "a27Non-recoverableControllers": a27Non_recoverableControllers,
       "a27DegradedControllers": a27DegradedControllers,
       "a27OverallDeviceHealthStatus": a27OverallDeviceHealthStatus,
       "a27Non-recoverableDevices": a27Non_recoverableDevices,
       "a27DegradedDevices": a27DegradedDevices,
       "a27DataValuesTimeStamp": a27DataValuesTimeStamp,
       "a27HardwareTimeStamp": a27HardwareTimeStamp,
       "tSymbiosController": tSymbiosController,
       "eSymbiosController": eSymbiosController,
       "a28SymbiosControllerIndex": a28SymbiosControllerIndex,
       "a28LastRunDateForDv": a28LastRunDateForDv,
       "a28IoFactorForDvErrorRate": a28IoFactorForDvErrorRate,
       "a28TimeFactorForDvErrorRate": a28TimeFactorForDvErrorRate,
       "a28ErrorCountFactorForDvErrorRate": a28ErrorCountFactorForDvErrorRate,
       "a28DvStatus": a28DvStatus,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap}
)
