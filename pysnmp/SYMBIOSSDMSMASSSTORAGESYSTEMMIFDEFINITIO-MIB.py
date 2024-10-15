# SNMP MIB module (SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:35 2024
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
_Scsitype_ObjectIdentity = ObjectIdentity
scsitype = _Scsitype_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1)
)
_Type8xx_ObjectIdentity = ObjectIdentity
type8xx = _Type8xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2)
)
_Id_ObjectIdentity = ObjectIdentity
id = _Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TSoftwareComponentInformation_Object = MibTable
tSoftwareComponentInformation = _TSoftwareComponentInformation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tSoftwareComponentInformation.setStatus("mandatory")
_ESoftwareComponentInformation_Object = MibTableRow
eSoftwareComponentInformation = _ESoftwareComponentInformation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1)
)
eSoftwareComponentInformation.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSoftwareComponentInformation.setStatus("mandatory")
_A2MajorVersion_Type = DmiDisplaystring
_A2MajorVersion_Object = MibTableColumn
a2MajorVersion = _A2MajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 1),
    _A2MajorVersion_Type()
)
a2MajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MajorVersion.setStatus("mandatory")
_A2MinorVersion_Type = DmiDisplaystring
_A2MinorVersion_Object = MibTableColumn
a2MinorVersion = _A2MinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 2),
    _A2MinorVersion_Type()
)
a2MinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2MinorVersion.setStatus("mandatory")
_A2Revision_Type = DmiDisplaystring
_A2Revision_Object = MibTableColumn
a2Revision = _A2Revision_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 3),
    _A2Revision_Type()
)
a2Revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Revision.setStatus("mandatory")
_A2Build_Type = DmiDisplaystring
_A2Build_Object = MibTableColumn
a2Build = _A2Build_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 4),
    _A2Build_Type()
)
a2Build.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Build.setStatus("mandatory")


class _A2TargetOperatingSystem_Type(Integer32):
    """Custom type a2TargetOperatingSystem based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("vDos", 1),
          ("vMacos", 2),
          ("vNetware", 8),
          ("vOpenvms", 7),
          ("vOs2", 3),
          ("vOther", 0),
          ("vUnix", 4),
          ("vWin16", 5),
          ("vWin32", 6),
          ("vWin9x", 9),
          ("vWinnt", 10))
    )


_A2TargetOperatingSystem_Type.__name__ = "Integer32"
_A2TargetOperatingSystem_Object = MibTableColumn
a2TargetOperatingSystem = _A2TargetOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 5),
    _A2TargetOperatingSystem_Type()
)
a2TargetOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2TargetOperatingSystem.setStatus("mandatory")
_A2LanguageEdition_Type = DmiDisplaystring
_A2LanguageEdition_Object = MibTableColumn
a2LanguageEdition = _A2LanguageEdition_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 6),
    _A2LanguageEdition_Type()
)
a2LanguageEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2LanguageEdition.setStatus("mandatory")
_A2IdentificationCode_Type = DmiDisplaystring
_A2IdentificationCode_Object = MibTableColumn
a2IdentificationCode = _A2IdentificationCode_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 7),
    _A2IdentificationCode_Type()
)
a2IdentificationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2IdentificationCode.setStatus("mandatory")


class _A2InstallableState_Type(Integer32):
    """Custom type a2InstallableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vInstallable", 2),
          ("vNotInstallable", 3),
          ("vUnknown", 1))
    )


_A2InstallableState_Type.__name__ = "Integer32"
_A2InstallableState_Object = MibTableColumn
a2InstallableState = _A2InstallableState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 8),
    _A2InstallableState_Type()
)
a2InstallableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2InstallableState.setStatus("mandatory")


class _A2ExecutableState_Type(Integer32):
    """Custom type a2ExecutableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vExecutable", 2),
          ("vNotExecutable", 3),
          ("vUnknown", 1))
    )


_A2ExecutableState_Type.__name__ = "Integer32"
_A2ExecutableState_Object = MibTableColumn
a2ExecutableState = _A2ExecutableState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 2, 1, 9),
    _A2ExecutableState_Type()
)
a2ExecutableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2ExecutableState.setStatus("mandatory")
_TComponentid1_Object = MibTable
tComponentid1 = _TComponentid1_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tComponentid1.setStatus("mandatory")
_EComponentid1_Object = MibTableRow
eComponentid1 = _EComponentid1_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1)
)
eComponentid1.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a3FileName"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a3FileLocation"),
)
if mibBuilder.loadTexts:
    eComponentid1.setStatus("mandatory")
_A3FileName_Type = DmiDisplaystring
_A3FileName_Object = MibTableColumn
a3FileName = _A3FileName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1, 1),
    _A3FileName_Type()
)
a3FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FileName.setStatus("mandatory")
_A3FileSize_Type = DmiInteger
_A3FileSize_Object = MibTableColumn
a3FileSize = _A3FileSize_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1, 2),
    _A3FileSize_Type()
)
a3FileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FileSize.setStatus("mandatory")
_A3FileDateAndTime_Type = DmiDateX
_A3FileDateAndTime_Object = MibTableColumn
a3FileDateAndTime = _A3FileDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1, 3),
    _A3FileDateAndTime_Type()
)
a3FileDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FileDateAndTime.setStatus("mandatory")
_A3FileChecksum_Type = DmiInteger
_A3FileChecksum_Object = MibTableColumn
a3FileChecksum = _A3FileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1, 4),
    _A3FileChecksum_Type()
)
a3FileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FileChecksum.setStatus("mandatory")
_A3FileCrc1_Type = DmiInteger
_A3FileCrc1_Object = MibTableColumn
a3FileCrc1 = _A3FileCrc1_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1, 5),
    _A3FileCrc1_Type()
)
a3FileCrc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FileCrc1.setStatus("mandatory")
_A3FileCrc2_Type = DmiInteger
_A3FileCrc2_Object = MibTableColumn
a3FileCrc2 = _A3FileCrc2_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1, 6),
    _A3FileCrc2_Type()
)
a3FileCrc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FileCrc2.setStatus("mandatory")
_A3FileLocation_Type = DmiInteger
_A3FileLocation_Object = MibTableColumn
a3FileLocation = _A3FileLocation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 3, 1, 7),
    _A3FileLocation_Type()
)
a3FileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FileLocation.setStatus("mandatory")
_TFieldReplaceableUnit_Object = MibTable
tFieldReplaceableUnit = _TFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tFieldReplaceableUnit.setStatus("mandatory")
_EFieldReplaceableUnit_Object = MibTableRow
eFieldReplaceableUnit = _EFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1)
)
eFieldReplaceableUnit.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a4FruIndex"),
)
if mibBuilder.loadTexts:
    eFieldReplaceableUnit.setStatus("mandatory")
_A4FruIndex_Type = DmiInteger
_A4FruIndex_Object = MibTableColumn
a4FruIndex = _A4FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 1),
    _A4FruIndex_Type()
)
a4FruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4FruIndex.setStatus("mandatory")
_A4DeviceGroupIndex_Type = DmiInteger
_A4DeviceGroupIndex_Object = MibTableColumn
a4DeviceGroupIndex = _A4DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 2),
    _A4DeviceGroupIndex_Type()
)
a4DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4DeviceGroupIndex.setStatus("mandatory")
_A4Description_Type = DmiDisplaystring
_A4Description_Object = MibTableColumn
a4Description = _A4Description_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 3),
    _A4Description_Type()
)
a4Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Description.setStatus("mandatory")
_A4Manufacturer_Type = DmiDisplaystring
_A4Manufacturer_Object = MibTableColumn
a4Manufacturer = _A4Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 4),
    _A4Manufacturer_Type()
)
a4Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Manufacturer.setStatus("mandatory")
_A4Model_Type = DmiDisplaystring
_A4Model_Object = MibTableColumn
a4Model = _A4Model_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 5),
    _A4Model_Type()
)
a4Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Model.setStatus("mandatory")
_A4PartNumber_Type = DmiDisplaystring
_A4PartNumber_Object = MibTableColumn
a4PartNumber = _A4PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 6),
    _A4PartNumber_Type()
)
a4PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4PartNumber.setStatus("mandatory")
_A4FruSerialNumber_Type = DmiDisplaystring
_A4FruSerialNumber_Object = MibTableColumn
a4FruSerialNumber = _A4FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 7),
    _A4FruSerialNumber_Type()
)
a4FruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4FruSerialNumber.setStatus("mandatory")
_A4RevisionLevel_Type = DmiDisplaystring
_A4RevisionLevel_Object = MibTableColumn
a4RevisionLevel = _A4RevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 8),
    _A4RevisionLevel_Type()
)
a4RevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4RevisionLevel.setStatus("mandatory")
_A4WarrantyStartDate_Type = DmiDateX
_A4WarrantyStartDate_Object = MibTableColumn
a4WarrantyStartDate = _A4WarrantyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 9),
    _A4WarrantyStartDate_Type()
)
a4WarrantyStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4WarrantyStartDate.setStatus("mandatory")
_A4WarrantyDuration_Type = DmiInteger
_A4WarrantyDuration_Object = MibTableColumn
a4WarrantyDuration = _A4WarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 10),
    _A4WarrantyDuration_Type()
)
a4WarrantyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4WarrantyDuration.setStatus("mandatory")
_A4SupportPhoneNumber_Type = DmiDisplaystring
_A4SupportPhoneNumber_Object = MibTableColumn
a4SupportPhoneNumber = _A4SupportPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 4, 1, 11),
    _A4SupportPhoneNumber_Type()
)
a4SupportPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4SupportPhoneNumber.setStatus("mandatory")
_TStorageDevices_Object = MibTable
tStorageDevices = _TStorageDevices_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tStorageDevices.setStatus("mandatory")
_EStorageDevices_Object = MibTableRow
eStorageDevices = _EStorageDevices_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1)
)
eStorageDevices.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a5StorageDeviceIndex"),
)
if mibBuilder.loadTexts:
    eStorageDevices.setStatus("mandatory")
_A5StorageDeviceIndex_Type = DmiInteger
_A5StorageDeviceIndex_Object = MibTableColumn
a5StorageDeviceIndex = _A5StorageDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 1),
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
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("vCartridgeRigidDiskDrive", 4),
          ("vCompactDiskDrive", 6),
          ("vFlexibleDisketteDrive", 5),
          ("vMagneto-opticalDrive", 8),
          ("vMediaChanger", 10),
          ("vOpticalWrite-onceread-manyWormDrive", 7),
          ("vOther", 1),
          ("vRigidDiskDrive", 3),
          ("vTapeDrive", 9),
          ("vUnknown", 2))
    )


_A5Type_Type.__name__ = "Integer32"
_A5Type_Object = MibTableColumn
a5Type = _A5Type_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 2),
    _A5Type_Type()
)
a5Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Type.setStatus("mandatory")
_A5TypeDescription_Type = DmiDisplaystring
_A5TypeDescription_Object = MibTableColumn
a5TypeDescription = _A5TypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 3),
    _A5TypeDescription_Type()
)
a5TypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5TypeDescription.setStatus("mandatory")


class _A5WorldwideIdentifierType_Type(Integer32):
    """Custom type a5WorldwideIdentifierType based on Integer32"""
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


_A5WorldwideIdentifierType_Type.__name__ = "Integer32"
_A5WorldwideIdentifierType_Object = MibTableColumn
a5WorldwideIdentifierType = _A5WorldwideIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 4),
    _A5WorldwideIdentifierType_Type()
)
a5WorldwideIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5WorldwideIdentifierType.setStatus("mandatory")
_A5WorldwideIdentifier_Type = DmiDisplaystring
_A5WorldwideIdentifier_Object = MibTableColumn
a5WorldwideIdentifier = _A5WorldwideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 5),
    _A5WorldwideIdentifier_Type()
)
a5WorldwideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5WorldwideIdentifier.setStatus("mandatory")
_A5Sub_identifier_Type = DmiDisplaystring
_A5Sub_identifier_Object = MibScalar
a5Sub_identifier = _A5Sub_identifier_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 6),
    _A5Sub_identifier_Type()
)
a5Sub_identifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Sub_identifier.setStatus("mandatory")
_A5MediaDataBlockSize_Type = DmiInteger
_A5MediaDataBlockSize_Object = MibTableColumn
a5MediaDataBlockSize = _A5MediaDataBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 7),
    _A5MediaDataBlockSize_Type()
)
a5MediaDataBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5MediaDataBlockSize.setStatus("mandatory")
_A5FormattedMediaCapacity_Type = DmiInteger64X
_A5FormattedMediaCapacity_Object = MibTableColumn
a5FormattedMediaCapacity = _A5FormattedMediaCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 14),
    _A5Encryption_Type()
)
a5Encryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Encryption.setStatus("mandatory")
_A5FruGroupIndex_Type = DmiInteger
_A5FruGroupIndex_Object = MibTableColumn
a5FruGroupIndex = _A5FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 15),
    _A5FruGroupIndex_Type()
)
a5FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5FruGroupIndex.setStatus("mandatory")
_A5OperationalGroupIndex_Type = DmiInteger
_A5OperationalGroupIndex_Object = MibTableColumn
a5OperationalGroupIndex = _A5OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 5, 1, 16),
    _A5OperationalGroupIndex_Type()
)
a5OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5OperationalGroupIndex.setStatus("mandatory")
_TStorageDevicesEvents_Object = MibTable
tStorageDevicesEvents = _TStorageDevicesEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tStorageDevicesEvents.setStatus("mandatory")
_EStorageDevicesEvents_Object = MibTableRow
eStorageDevicesEvents = _EStorageDevicesEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1)
)
eStorageDevicesEvents.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a6AssociatedGroup"),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1, 1),
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
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A6EventSeverity_Type.__name__ = "Integer32"
_A6EventSeverity_Object = MibTableColumn
a6EventSeverity = _A6EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1, 3),
    _A6EventIsStateBased_Type()
)
a6EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventIsStateBased.setStatus("mandatory")
_A6EventStateKey_Type = DmiInteger
_A6EventStateKey_Object = MibTableColumn
a6EventStateKey = _A6EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1, 4),
    _A6EventStateKey_Type()
)
a6EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventStateKey.setStatus("mandatory")
_A6AssociatedGroup_Type = DmiDisplaystring
_A6AssociatedGroup_Object = MibTableColumn
a6AssociatedGroup = _A6AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1, 5),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A6EventSystem_Type.__name__ = "Integer32"
_A6EventSystem_Object = MibTableColumn
a6EventSystem = _A6EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 6, 1, 7),
    _A6EventSubsystem_Type()
)
a6EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6EventSubsystem.setStatus("mandatory")
_TStorageController_Object = MibTable
tStorageController = _TStorageController_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tStorageController.setStatus("mandatory")
_EStorageController_Object = MibTableRow
eStorageController = _EStorageController_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1)
)
eStorageController.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a7ControllerIndex"),
)
if mibBuilder.loadTexts:
    eStorageController.setStatus("mandatory")
_A7ControllerIndex_Type = DmiInteger
_A7ControllerIndex_Object = MibTableColumn
a7ControllerIndex = _A7ControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 1),
    _A7ControllerIndex_Type()
)
a7ControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7ControllerIndex.setStatus("mandatory")
_A7Identification_Type = DmiDisplaystring
_A7Identification_Object = MibTableColumn
a7Identification = _A7Identification_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 2),
    _A7Identification_Type()
)
a7Identification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Identification.setStatus("mandatory")


class _A7WorldwideIdentifierType_Type(Integer32):
    """Custom type a7WorldwideIdentifierType based on Integer32"""
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


_A7WorldwideIdentifierType_Type.__name__ = "Integer32"
_A7WorldwideIdentifierType_Object = MibTableColumn
a7WorldwideIdentifierType = _A7WorldwideIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 3),
    _A7WorldwideIdentifierType_Type()
)
a7WorldwideIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7WorldwideIdentifierType.setStatus("mandatory")
_A7WorldwideIdentifier_Type = DmiDisplaystring
_A7WorldwideIdentifier_Object = MibTableColumn
a7WorldwideIdentifier = _A7WorldwideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 4),
    _A7WorldwideIdentifier_Type()
)
a7WorldwideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7WorldwideIdentifier.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 6),
    _A7BusMaster_Type()
)
a7BusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7BusMaster.setStatus("mandatory")
_A7SecondsSinceLastPower_up_Type = DmiInteger
_A7SecondsSinceLastPower_up_Object = MibScalar
a7SecondsSinceLastPower_up = _A7SecondsSinceLastPower_up_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 7),
    _A7SecondsSinceLastPower_up_Type()
)
a7SecondsSinceLastPower_up.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7SecondsSinceLastPower_up.setStatus("mandatory")
_A7FruGroupIndex_Type = DmiInteger
_A7FruGroupIndex_Object = MibTableColumn
a7FruGroupIndex = _A7FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 8),
    _A7FruGroupIndex_Type()
)
a7FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7FruGroupIndex.setStatus("mandatory")
_A7OperationalGroupIndex_Type = DmiInteger
_A7OperationalGroupIndex_Object = MibTableColumn
a7OperationalGroupIndex = _A7OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 7, 1, 9),
    _A7OperationalGroupIndex_Type()
)
a7OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7OperationalGroupIndex.setStatus("mandatory")
_TStorageControllerEvents_Object = MibTable
tStorageControllerEvents = _TStorageControllerEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tStorageControllerEvents.setStatus("mandatory")
_EStorageControllerEvents_Object = MibTableRow
eStorageControllerEvents = _EStorageControllerEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1)
)
eStorageControllerEvents.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a8AssociatedGroup"),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1, 1),
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
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A8EventSeverity_Type.__name__ = "Integer32"
_A8EventSeverity_Object = MibTableColumn
a8EventSeverity = _A8EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1, 3),
    _A8EventIsStateBased_Type()
)
a8EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventIsStateBased.setStatus("mandatory")
_A8EventStateKey_Type = DmiInteger
_A8EventStateKey_Object = MibTableColumn
a8EventStateKey = _A8EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1, 4),
    _A8EventStateKey_Type()
)
a8EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventStateKey.setStatus("mandatory")
_A8AssociatedGroup_Type = DmiDisplaystring
_A8AssociatedGroup_Object = MibTableColumn
a8AssociatedGroup = _A8AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1, 5),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A8EventSystem_Type.__name__ = "Integer32"
_A8EventSystem_Object = MibTableColumn
a8EventSystem = _A8EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 8, 1, 7),
    _A8EventSubsystem_Type()
)
a8EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8EventSubsystem.setStatus("mandatory")
_TBusPort_Object = MibTable
tBusPort = _TBusPort_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tBusPort.setStatus("mandatory")
_EBusPort_Object = MibTableRow
eBusPort = _EBusPort_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1)
)
eBusPort.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a9BusPortIndex"),
)
if mibBuilder.loadTexts:
    eBusPort.setStatus("mandatory")
_A9BusPortIndex_Type = DmiInteger
_A9BusPortIndex_Object = MibTableColumn
a9BusPortIndex = _A9BusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 2),
    _A9Protocol_Type()
)
a9Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Protocol.setStatus("mandatory")
_A9ProtocolDescription_Type = DmiDisplaystring
_A9ProtocolDescription_Object = MibTableColumn
a9ProtocolDescription = _A9ProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 4),
    _A9SignalCharacteristics_Type()
)
a9SignalCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9SignalCharacteristics.setStatus("mandatory")


class _A9WorldwideIdentifierType_Type(Integer32):
    """Custom type a9WorldwideIdentifierType based on Integer32"""
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


_A9WorldwideIdentifierType_Type.__name__ = "Integer32"
_A9WorldwideIdentifierType_Object = MibTableColumn
a9WorldwideIdentifierType = _A9WorldwideIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 5),
    _A9WorldwideIdentifierType_Type()
)
a9WorldwideIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9WorldwideIdentifierType.setStatus("mandatory")
_A9WorldwideIdentifier_Type = DmiDisplaystring
_A9WorldwideIdentifier_Object = MibTableColumn
a9WorldwideIdentifier = _A9WorldwideIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 6),
    _A9WorldwideIdentifier_Type()
)
a9WorldwideIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9WorldwideIdentifier.setStatus("mandatory")
_A9AddressDescriptor_Type = DmiDisplaystring
_A9AddressDescriptor_Object = MibTableColumn
a9AddressDescriptor = _A9AddressDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 8),
    _A9Isochronous_Type()
)
a9Isochronous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Isochronous.setStatus("mandatory")
_A9MaximumWidth_Type = DmiInteger
_A9MaximumWidth_Object = MibTableColumn
a9MaximumWidth = _A9MaximumWidth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 9),
    _A9MaximumWidth_Type()
)
a9MaximumWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9MaximumWidth.setStatus("mandatory")
_A9MaximumTransferRate_Type = DmiInteger
_A9MaximumTransferRate_Object = MibTableColumn
a9MaximumTransferRate = _A9MaximumTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 10),
    _A9MaximumTransferRate_Type()
)
a9MaximumTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9MaximumTransferRate.setStatus("mandatory")
_A9MaximumNumberOfAttachments_Type = DmiInteger
_A9MaximumNumberOfAttachments_Object = MibTableColumn
a9MaximumNumberOfAttachments = _A9MaximumNumberOfAttachments_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 11),
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
              43)
        )
    )
    namedValues = NamedValues(
        *(("vAppleAui", 33),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 12),
    _A9ConnectorType_Type()
)
a9ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ConnectorType.setStatus("mandatory")
_A9ConnectorTypeDescription_Type = DmiDisplaystring
_A9ConnectorTypeDescription_Object = MibTableColumn
a9ConnectorTypeDescription = _A9ConnectorTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 14),
    _A9ConnectorGender_Type()
)
a9ConnectorGender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ConnectorGender.setStatus("mandatory")
_A9OperationalGroupIndex_Type = DmiInteger
_A9OperationalGroupIndex_Object = MibTableColumn
a9OperationalGroupIndex = _A9OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 15),
    _A9OperationalGroupIndex_Type()
)
a9OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9OperationalGroupIndex.setStatus("mandatory")
_A9MassStorageStatisticsGroupIndex_Type = DmiInteger
_A9MassStorageStatisticsGroupIndex_Object = MibTableColumn
a9MassStorageStatisticsGroupIndex = _A9MassStorageStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 9, 1, 16),
    _A9MassStorageStatisticsGroupIndex_Type()
)
a9MassStorageStatisticsGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9MassStorageStatisticsGroupIndex.setStatus("mandatory")
_TBusPortEvents_Object = MibTable
tBusPortEvents = _TBusPortEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tBusPortEvents.setStatus("mandatory")
_EBusPortEvents_Object = MibTableRow
eBusPortEvents = _EBusPortEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1)
)
eBusPortEvents.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a10AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eBusPortEvents.setStatus("mandatory")


class _A10BusPortEventType_Type(Integer32):
    """Custom type a10BusPortEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vBusPortError", 1)
    )


_A10BusPortEventType_Type.__name__ = "Integer32"
_A10BusPortEventType_Object = MibTableColumn
a10BusPortEventType = _A10BusPortEventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1, 1),
    _A10BusPortEventType_Type()
)
a10BusPortEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10BusPortEventType.setStatus("mandatory")


class _A10EventSeverity_Type(Integer32):
    """Custom type a10EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A10EventSeverity_Type.__name__ = "Integer32"
_A10EventSeverity_Object = MibTableColumn
a10EventSeverity = _A10EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1, 2),
    _A10EventSeverity_Type()
)
a10EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventSeverity.setStatus("mandatory")


class _A10EventIsStateBased_Type(Integer32):
    """Custom type a10EventIsStateBased based on Integer32"""
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


_A10EventIsStateBased_Type.__name__ = "Integer32"
_A10EventIsStateBased_Object = MibTableColumn
a10EventIsStateBased = _A10EventIsStateBased_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1, 3),
    _A10EventIsStateBased_Type()
)
a10EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventIsStateBased.setStatus("mandatory")
_A10EventStateKey_Type = DmiInteger
_A10EventStateKey_Object = MibTableColumn
a10EventStateKey = _A10EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1, 4),
    _A10EventStateKey_Type()
)
a10EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventStateKey.setStatus("mandatory")
_A10AssociatedGroup_Type = DmiDisplaystring
_A10AssociatedGroup_Object = MibTableColumn
a10AssociatedGroup = _A10AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1, 5),
    _A10AssociatedGroup_Type()
)
a10AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10AssociatedGroup.setStatus("mandatory")


class _A10EventSystem_Type(Integer32):
    """Custom type a10EventSystem based on Integer32"""
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


_A10EventSystem_Type.__name__ = "Integer32"
_A10EventSystem_Object = MibTableColumn
a10EventSystem = _A10EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1, 6),
    _A10EventSystem_Type()
)
a10EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventSystem.setStatus("mandatory")


class _A10EventSubsystem_Type(Integer32):
    """Custom type a10EventSubsystem based on Integer32"""
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


_A10EventSubsystem_Type.__name__ = "Integer32"
_A10EventSubsystem_Object = MibTableColumn
a10EventSubsystem = _A10EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 10, 1, 7),
    _A10EventSubsystem_Type()
)
a10EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10EventSubsystem.setStatus("mandatory")
_TMassStorageAssociation_Object = MibTable
tMassStorageAssociation = _TMassStorageAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tMassStorageAssociation.setStatus("mandatory")
_EMassStorageAssociation_Object = MibTableRow
eMassStorageAssociation = _EMassStorageAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11, 1)
)
eMassStorageAssociation.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a11AssociationIndex"),
)
if mibBuilder.loadTexts:
    eMassStorageAssociation.setStatus("mandatory")
_A11AssociationIndex_Type = DmiInteger
_A11AssociationIndex_Object = MibTableColumn
a11AssociationIndex = _A11AssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11, 1, 1),
    _A11AssociationIndex_Type()
)
a11AssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11AssociationIndex.setStatus("mandatory")


class _A11Type_Type(Integer32):
    """Custom type a11Type based on Integer32"""
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
        *(("vCacheOrganization", 5),
          ("vLogicalOrganization", 1),
          ("vLogicalToPhysicalOrganization", 2),
          ("vPhysicalOrganization", 0),
          ("vRedundancyOrganization", 3),
          ("vSoftwareOrganization", 6),
          ("vSpareOrganization", 4))
    )


_A11Type_Type.__name__ = "Integer32"
_A11Type_Object = MibTableColumn
a11Type = _A11Type_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11, 1, 2),
    _A11Type_Type()
)
a11Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Type.setStatus("mandatory")


class _A11Object1Type_Type(Integer32):
    """Custom type a11Object1Type based on Integer32"""
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


_A11Object1Type_Type.__name__ = "Integer32"
_A11Object1Type_Object = MibTableColumn
a11Object1Type = _A11Object1Type_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11, 1, 3),
    _A11Object1Type_Type()
)
a11Object1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Object1Type.setStatus("mandatory")
_A11Object1Index_Type = DmiInteger
_A11Object1Index_Object = MibTableColumn
a11Object1Index = _A11Object1Index_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11, 1, 4),
    _A11Object1Index_Type()
)
a11Object1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Object1Index.setStatus("mandatory")


class _A11Object2Type_Type(Integer32):
    """Custom type a11Object2Type based on Integer32"""
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


_A11Object2Type_Type.__name__ = "Integer32"
_A11Object2Type_Object = MibTableColumn
a11Object2Type = _A11Object2Type_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11, 1, 5),
    _A11Object2Type_Type()
)
a11Object2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Object2Type.setStatus("mandatory")
_A11Object2Index_Type = DmiInteger
_A11Object2Index_Object = MibTableColumn
a11Object2Index = _A11Object2Index_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 11, 1, 6),
    _A11Object2Index_Type()
)
a11Object2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Object2Index.setStatus("mandatory")
_TMassStorageAssociationEvents_Object = MibTable
tMassStorageAssociationEvents = _TMassStorageAssociationEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tMassStorageAssociationEvents.setStatus("mandatory")
_EMassStorageAssociationEvents_Object = MibTableRow
eMassStorageAssociationEvents = _EMassStorageAssociationEvents_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1)
)
eMassStorageAssociationEvents.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a12AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eMassStorageAssociationEvents.setStatus("mandatory")


class _A12MassStorageAssociationEventType_Type(Integer32):
    """Custom type a12MassStorageAssociationEventType based on Integer32"""
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
        *(("vCacheOrganization", 5),
          ("vLogicalOrganization", 1),
          ("vLogicalToPhysicalOrganization", 2),
          ("vPhysicalOrganization", 0),
          ("vRedundancyOrganization", 3),
          ("vSoftwareOrganization", 6),
          ("vSpareOrganization", 4))
    )


_A12MassStorageAssociationEventType_Type.__name__ = "Integer32"
_A12MassStorageAssociationEventType_Object = MibTableColumn
a12MassStorageAssociationEventType = _A12MassStorageAssociationEventType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1, 1),
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
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A12EventSeverity_Type.__name__ = "Integer32"
_A12EventSeverity_Object = MibTableColumn
a12EventSeverity = _A12EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1, 3),
    _A12EventIsStateBased_Type()
)
a12EventIsStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventIsStateBased.setStatus("mandatory")
_A12EventStateKey_Type = DmiInteger
_A12EventStateKey_Object = MibTableColumn
a12EventStateKey = _A12EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1, 4),
    _A12EventStateKey_Type()
)
a12EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventStateKey.setStatus("mandatory")
_A12AssociatedGroup_Type = DmiDisplaystring
_A12AssociatedGroup_Object = MibTableColumn
a12AssociatedGroup = _A12AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1, 5),
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


_A12EventSystem_Type.__name__ = "Integer32"
_A12EventSystem_Object = MibTableColumn
a12EventSystem = _A12EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 12, 1, 7),
    _A12EventSubsystem_Type()
)
a12EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12EventSubsystem.setStatus("mandatory")
_TBusPortAssociation_Object = MibTable
tBusPortAssociation = _TBusPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    tBusPortAssociation.setStatus("mandatory")
_EBusPortAssociation_Object = MibTableRow
eBusPortAssociation = _EBusPortAssociation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 13, 1)
)
eBusPortAssociation.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a13BusPortAssociationIndex"),
)
if mibBuilder.loadTexts:
    eBusPortAssociation.setStatus("mandatory")
_A13BusPortAssociationIndex_Type = DmiInteger
_A13BusPortAssociationIndex_Object = MibTableColumn
a13BusPortAssociationIndex = _A13BusPortAssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 13, 1, 1),
    _A13BusPortAssociationIndex_Type()
)
a13BusPortAssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13BusPortAssociationIndex.setStatus("mandatory")
_A13NegotiatedSpeed_Type = DmiInteger
_A13NegotiatedSpeed_Object = MibTableColumn
a13NegotiatedSpeed = _A13NegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 13, 1, 2),
    _A13NegotiatedSpeed_Type()
)
a13NegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13NegotiatedSpeed.setStatus("mandatory")
_A13NegotiatedWidth_Type = DmiInteger
_A13NegotiatedWidth_Object = MibTableColumn
a13NegotiatedWidth = _A13NegotiatedWidth_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 13, 1, 3),
    _A13NegotiatedWidth_Type()
)
a13NegotiatedWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13NegotiatedWidth.setStatus("mandatory")
_TOperationalState_Object = MibTable
tOperationalState = _TOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tOperationalState.setStatus("mandatory")
_EOperationalState_Object = MibTableRow
eOperationalState = _EOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1)
)
eOperationalState.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a14OperationalStateInstanceIndex"),
)
if mibBuilder.loadTexts:
    eOperationalState.setStatus("mandatory")
_A14OperationalStateInstanceIndex_Type = DmiInteger
_A14OperationalStateInstanceIndex_Object = MibTableColumn
a14OperationalStateInstanceIndex = _A14OperationalStateInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 1),
    _A14OperationalStateInstanceIndex_Type()
)
a14OperationalStateInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14OperationalStateInstanceIndex.setStatus("mandatory")
_A14DeviceGroupIndex_Type = DmiInteger
_A14DeviceGroupIndex_Object = MibTableColumn
a14DeviceGroupIndex = _A14DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 6),
    _A14AdministrativeState_Type()
)
a14AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14AdministrativeState.setStatus("mandatory")
_A14FatalErrorCount_Type = DmiCounter
_A14FatalErrorCount_Object = MibTableColumn
a14FatalErrorCount = _A14FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 7),
    _A14FatalErrorCount_Type()
)
a14FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14FatalErrorCount.setStatus("mandatory")
_A14MajorErrorCount_Type = DmiCounter
_A14MajorErrorCount_Object = MibTableColumn
a14MajorErrorCount = _A14MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 8),
    _A14MajorErrorCount_Type()
)
a14MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14MajorErrorCount.setStatus("mandatory")
_A14WarningErrorCount_Type = DmiCounter
_A14WarningErrorCount_Object = MibTableColumn
a14WarningErrorCount = _A14WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 14, 1, 11),
    _A14DevicePredictedFailureStatus_Type()
)
a14DevicePredictedFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14DevicePredictedFailureStatus.setStatus("mandatory")
_TSymi2omassstoragesystem_Object = MibTable
tSymi2omassstoragesystem = _TSymi2omassstoragesystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    tSymi2omassstoragesystem.setStatus("mandatory")
_ESymi2omassstoragesystem_Object = MibTableRow
eSymi2omassstoragesystem = _ESymi2omassstoragesystem_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 15, 1)
)
eSymi2omassstoragesystem.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "a15SymDeviceIndex"),
)
if mibBuilder.loadTexts:
    eSymi2omassstoragesystem.setStatus("mandatory")
_A15SymDeviceIndex_Type = DmiInteger
_A15SymDeviceIndex_Object = MibTableColumn
a15SymDeviceIndex = _A15SymDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 15, 1, 1),
    _A15SymDeviceIndex_Type()
)
a15SymDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15SymDeviceIndex.setStatus("mandatory")
_A15SymDeviceIndex2_Type = DmiInteger
_A15SymDeviceIndex2_Object = MibTableColumn
a15SymDeviceIndex2 = _A15SymDeviceIndex2_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 15, 1, 2),
    _A15SymDeviceIndex2_Type()
)
a15SymDeviceIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15SymDeviceIndex2.setStatus("mandatory")


class _A15SmartReportingCapability_Type(Integer32):
    """Custom type a15SmartReportingCapability based on Integer32"""
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


_A15SmartReportingCapability_Type.__name__ = "Integer32"
_A15SmartReportingCapability_Object = MibTableColumn
a15SmartReportingCapability = _A15SmartReportingCapability_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 15, 1, 3),
    _A15SmartReportingCapability_Type()
)
a15SmartReportingCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15SmartReportingCapability.setStatus("mandatory")
_A15SmartPollingPeriod_Type = DmiInteger
_A15SmartPollingPeriod_Object = MibTableColumn
a15SmartPollingPeriod = _A15SmartPollingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 15, 1, 4),
    _A15SmartPollingPeriod_Type()
)
a15SmartPollingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15SmartPollingPeriod.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 1, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMBIOSSDMSMASSSTORAGESYSTEMMIFDEFINITIO-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiInteger64X": DmiInteger64X,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "symbios": symbios,
       "cosprings": cosprings,
       "scsitype": scsitype,
       "type8xx": type8xx,
       "id": id,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tSoftwareComponentInformation": tSoftwareComponentInformation,
       "eSoftwareComponentInformation": eSoftwareComponentInformation,
       "a2MajorVersion": a2MajorVersion,
       "a2MinorVersion": a2MinorVersion,
       "a2Revision": a2Revision,
       "a2Build": a2Build,
       "a2TargetOperatingSystem": a2TargetOperatingSystem,
       "a2LanguageEdition": a2LanguageEdition,
       "a2IdentificationCode": a2IdentificationCode,
       "a2InstallableState": a2InstallableState,
       "a2ExecutableState": a2ExecutableState,
       "tComponentid1": tComponentid1,
       "eComponentid1": eComponentid1,
       "a3FileName": a3FileName,
       "a3FileSize": a3FileSize,
       "a3FileDateAndTime": a3FileDateAndTime,
       "a3FileChecksum": a3FileChecksum,
       "a3FileCrc1": a3FileCrc1,
       "a3FileCrc2": a3FileCrc2,
       "a3FileLocation": a3FileLocation,
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
       "tStorageDevices": tStorageDevices,
       "eStorageDevices": eStorageDevices,
       "a5StorageDeviceIndex": a5StorageDeviceIndex,
       "a5Type": a5Type,
       "a5TypeDescription": a5TypeDescription,
       "a5WorldwideIdentifierType": a5WorldwideIdentifierType,
       "a5WorldwideIdentifier": a5WorldwideIdentifier,
       "a5Sub-identifier": a5Sub_identifier,
       "a5MediaDataBlockSize": a5MediaDataBlockSize,
       "a5FormattedMediaCapacity": a5FormattedMediaCapacity,
       "a5RemovableDevice": a5RemovableDevice,
       "a5DeviceLoaded": a5DeviceLoaded,
       "a5RemovableMedia": a5RemovableMedia,
       "a5MediaLoaded": a5MediaLoaded,
       "a5Compression": a5Compression,
       "a5Encryption": a5Encryption,
       "a5FruGroupIndex": a5FruGroupIndex,
       "a5OperationalGroupIndex": a5OperationalGroupIndex,
       "tStorageDevicesEvents": tStorageDevicesEvents,
       "eStorageDevicesEvents": eStorageDevicesEvents,
       "a6StorageDevicesEventType": a6StorageDevicesEventType,
       "a6EventSeverity": a6EventSeverity,
       "a6EventIsStateBased": a6EventIsStateBased,
       "a6EventStateKey": a6EventStateKey,
       "a6AssociatedGroup": a6AssociatedGroup,
       "a6EventSystem": a6EventSystem,
       "a6EventSubsystem": a6EventSubsystem,
       "tStorageController": tStorageController,
       "eStorageController": eStorageController,
       "a7ControllerIndex": a7ControllerIndex,
       "a7Identification": a7Identification,
       "a7WorldwideIdentifierType": a7WorldwideIdentifierType,
       "a7WorldwideIdentifier": a7WorldwideIdentifier,
       "a7ProtectionManagement": a7ProtectionManagement,
       "a7BusMaster": a7BusMaster,
       "a7SecondsSinceLastPower-up": a7SecondsSinceLastPower_up,
       "a7FruGroupIndex": a7FruGroupIndex,
       "a7OperationalGroupIndex": a7OperationalGroupIndex,
       "tStorageControllerEvents": tStorageControllerEvents,
       "eStorageControllerEvents": eStorageControllerEvents,
       "a8StorageControllerEventType": a8StorageControllerEventType,
       "a8EventSeverity": a8EventSeverity,
       "a8EventIsStateBased": a8EventIsStateBased,
       "a8EventStateKey": a8EventStateKey,
       "a8AssociatedGroup": a8AssociatedGroup,
       "a8EventSystem": a8EventSystem,
       "a8EventSubsystem": a8EventSubsystem,
       "tBusPort": tBusPort,
       "eBusPort": eBusPort,
       "a9BusPortIndex": a9BusPortIndex,
       "a9Protocol": a9Protocol,
       "a9ProtocolDescription": a9ProtocolDescription,
       "a9SignalCharacteristics": a9SignalCharacteristics,
       "a9WorldwideIdentifierType": a9WorldwideIdentifierType,
       "a9WorldwideIdentifier": a9WorldwideIdentifier,
       "a9AddressDescriptor": a9AddressDescriptor,
       "a9Isochronous": a9Isochronous,
       "a9MaximumWidth": a9MaximumWidth,
       "a9MaximumTransferRate": a9MaximumTransferRate,
       "a9MaximumNumberOfAttachments": a9MaximumNumberOfAttachments,
       "a9ConnectorType": a9ConnectorType,
       "a9ConnectorTypeDescription": a9ConnectorTypeDescription,
       "a9ConnectorGender": a9ConnectorGender,
       "a9OperationalGroupIndex": a9OperationalGroupIndex,
       "a9MassStorageStatisticsGroupIndex": a9MassStorageStatisticsGroupIndex,
       "tBusPortEvents": tBusPortEvents,
       "eBusPortEvents": eBusPortEvents,
       "a10BusPortEventType": a10BusPortEventType,
       "a10EventSeverity": a10EventSeverity,
       "a10EventIsStateBased": a10EventIsStateBased,
       "a10EventStateKey": a10EventStateKey,
       "a10AssociatedGroup": a10AssociatedGroup,
       "a10EventSystem": a10EventSystem,
       "a10EventSubsystem": a10EventSubsystem,
       "tMassStorageAssociation": tMassStorageAssociation,
       "eMassStorageAssociation": eMassStorageAssociation,
       "a11AssociationIndex": a11AssociationIndex,
       "a11Type": a11Type,
       "a11Object1Type": a11Object1Type,
       "a11Object1Index": a11Object1Index,
       "a11Object2Type": a11Object2Type,
       "a11Object2Index": a11Object2Index,
       "tMassStorageAssociationEvents": tMassStorageAssociationEvents,
       "eMassStorageAssociationEvents": eMassStorageAssociationEvents,
       "a12MassStorageAssociationEventType": a12MassStorageAssociationEventType,
       "a12EventSeverity": a12EventSeverity,
       "a12EventIsStateBased": a12EventIsStateBased,
       "a12EventStateKey": a12EventStateKey,
       "a12AssociatedGroup": a12AssociatedGroup,
       "a12EventSystem": a12EventSystem,
       "a12EventSubsystem": a12EventSubsystem,
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
       "tSymi2omassstoragesystem": tSymi2omassstoragesystem,
       "eSymi2omassstoragesystem": eSymi2omassstoragesystem,
       "a15SymDeviceIndex": a15SymDeviceIndex,
       "a15SymDeviceIndex2": a15SymDeviceIndex2,
       "a15SmartReportingCapability": a15SmartReportingCapability,
       "a15SmartPollingPeriod": a15SmartPollingPeriod,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap}
)
