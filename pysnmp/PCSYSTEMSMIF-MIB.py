# SNMP MIB module (PCSYSTEMSMIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCSYSTEMSMIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:10 2024
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



class DmiCounter(Integer32):
    """Custom type DmiCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiInteger64(Integer32):
    """Custom type DmiInteger64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18446744073709551615, 18446744073709551615),
    )





class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDate(OctetString):
    """Custom type DmiDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NetFinity_ObjectIdentity = ObjectIdentity
netFinity = _NetFinity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71)
)
_DmiMibs_ObjectIdentity = ObjectIdentity
dmiMibs = _DmiMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200)
)
_NetFinitySystemsMIB_ObjectIdentity = ObjectIdentity
netFinitySystemsMIB = _NetFinitySystemsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1)
)
_DmtfGroups1_ObjectIdentity = ObjectIdentity
dmtfGroups1 = _DmtfGroups1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1)
)
_TComponentid1_Object = MibTable
tComponentid1 = _TComponentid1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid1.setStatus("mandatory")
_EComponentid1_Object = MibTableRow
eComponentid1 = _EComponentid1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 1, 1)
)
eComponentid1.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid1.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_TGeneralInformation_Object = MibTable
tGeneralInformation = _TGeneralInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tGeneralInformation.setStatus("mandatory")
_EGeneralInformation_Object = MibTableRow
eGeneralInformation = _EGeneralInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2, 1)
)
eGeneralInformation.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eGeneralInformation.setStatus("mandatory")
_A2SystemName_Type = DmiDisplaystring
_A2SystemName_Object = MibTableColumn
a2SystemName = _A2SystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2, 1, 1),
    _A2SystemName_Type()
)
a2SystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemName.setStatus("mandatory")
_A2SystemLocation_Type = DmiDisplaystring
_A2SystemLocation_Object = MibTableColumn
a2SystemLocation = _A2SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2, 1, 2),
    _A2SystemLocation_Type()
)
a2SystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemLocation.setStatus("mandatory")
_A2SystemPrimaryUserName_Type = DmiDisplaystring
_A2SystemPrimaryUserName_Object = MibTableColumn
a2SystemPrimaryUserName = _A2SystemPrimaryUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2, 1, 3),
    _A2SystemPrimaryUserName_Type()
)
a2SystemPrimaryUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemPrimaryUserName.setStatus("mandatory")
_A2SystemPrimaryUserPhone_Type = DmiDisplaystring
_A2SystemPrimaryUserPhone_Object = MibTableColumn
a2SystemPrimaryUserPhone = _A2SystemPrimaryUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2, 1, 4),
    _A2SystemPrimaryUserPhone_Type()
)
a2SystemPrimaryUserPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemPrimaryUserPhone.setStatus("mandatory")
_A2SystemBootUpTime_Type = DmiDate
_A2SystemBootUpTime_Object = MibTableColumn
a2SystemBootUpTime = _A2SystemBootUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2, 1, 5),
    _A2SystemBootUpTime_Type()
)
a2SystemBootUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SystemBootUpTime.setStatus("mandatory")
_A2SystemDateTime_Type = DmiDate
_A2SystemDateTime_Object = MibTableColumn
a2SystemDateTime = _A2SystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 2, 1, 6),
    _A2SystemDateTime_Type()
)
a2SystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemDateTime.setStatus("mandatory")
_TOperatingSystem_Object = MibTable
tOperatingSystem = _TOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tOperatingSystem.setStatus("mandatory")
_EOperatingSystem_Object = MibTableRow
eOperatingSystem = _EOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1)
)
eOperatingSystem.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a3OperatingSystemIndex"),
)
if mibBuilder.loadTexts:
    eOperatingSystem.setStatus("mandatory")
_A3OperatingSystemIndex_Type = DmiInteger
_A3OperatingSystemIndex_Object = MibTableColumn
a3OperatingSystemIndex = _A3OperatingSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 1),
    _A3OperatingSystemIndex_Type()
)
a3OperatingSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperatingSystemIndex.setStatus("mandatory")
_A3OperatingSystemName_Type = DmiDisplaystring
_A3OperatingSystemName_Object = MibTableColumn
a3OperatingSystemName = _A3OperatingSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 2),
    _A3OperatingSystemName_Type()
)
a3OperatingSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperatingSystemName.setStatus("mandatory")
_A3OperatingSystemVersion_Type = DmiDisplaystring
_A3OperatingSystemVersion_Object = MibTableColumn
a3OperatingSystemVersion = _A3OperatingSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 3),
    _A3OperatingSystemVersion_Type()
)
a3OperatingSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperatingSystemVersion.setStatus("mandatory")


class _A3PrimaryOperatingSystem_Type(Integer32):
    """Custom type a3PrimaryOperatingSystem based on Integer32"""
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


_A3PrimaryOperatingSystem_Type.__name__ = "Integer32"
_A3PrimaryOperatingSystem_Object = MibTableColumn
a3PrimaryOperatingSystem = _A3PrimaryOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 4),
    _A3PrimaryOperatingSystem_Type()
)
a3PrimaryOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3PrimaryOperatingSystem.setStatus("mandatory")


class _A3OperatingSystemBootDeviceStorageType_Type(Integer32):
    """Custom type a3OperatingSystemBootDeviceStorageType based on Integer32"""
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
        *(("vBernoulli", 10),
          ("vCompact-disk", 8),
          ("vFlash-disk", 9),
          ("vFloppy-disk", 4),
          ("vHard-disk", 3),
          ("vOptical-rom", 5),
          ("vOptical-rw", 7),
          ("vOptical-worm", 6),
          ("vOpticalFloppyDisk", 11),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A3OperatingSystemBootDeviceStorageType_Type.__name__ = "Integer32"
_A3OperatingSystemBootDeviceStorageType_Object = MibTableColumn
a3OperatingSystemBootDeviceStorageType = _A3OperatingSystemBootDeviceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 5),
    _A3OperatingSystemBootDeviceStorageType_Type()
)
a3OperatingSystemBootDeviceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperatingSystemBootDeviceStorageType.setStatus("mandatory")
_A3OperatingSystemBootDeviceIndex_Type = DmiInteger
_A3OperatingSystemBootDeviceIndex_Object = MibTableColumn
a3OperatingSystemBootDeviceIndex = _A3OperatingSystemBootDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 6),
    _A3OperatingSystemBootDeviceIndex_Type()
)
a3OperatingSystemBootDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperatingSystemBootDeviceIndex.setStatus("mandatory")
_A3OperatingSystemBootPartitionIndex_Type = DmiInteger
_A3OperatingSystemBootPartitionIndex_Object = MibTableColumn
a3OperatingSystemBootPartitionIndex = _A3OperatingSystemBootPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 7),
    _A3OperatingSystemBootPartitionIndex_Type()
)
a3OperatingSystemBootPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperatingSystemBootPartitionIndex.setStatus("mandatory")
_A3OperatingSystemDescription_Type = DmiDisplaystring
_A3OperatingSystemDescription_Object = MibTableColumn
a3OperatingSystemDescription = _A3OperatingSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 3, 1, 8),
    _A3OperatingSystemDescription_Type()
)
a3OperatingSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperatingSystemDescription.setStatus("mandatory")
_TSystemBios_Object = MibTable
tSystemBios = _TSystemBios_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tSystemBios.setStatus("mandatory")
_ESystemBios_Object = MibTableRow
eSystemBios = _ESystemBios_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1)
)
eSystemBios.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a4BiosIndex"),
)
if mibBuilder.loadTexts:
    eSystemBios.setStatus("mandatory")
_A4BiosIndex_Type = DmiInteger
_A4BiosIndex_Object = MibTableColumn
a4BiosIndex = _A4BiosIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 1),
    _A4BiosIndex_Type()
)
a4BiosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosIndex.setStatus("mandatory")
_A4Manufacturer_Type = DmiDisplaystring
_A4Manufacturer_Object = MibTableColumn
a4Manufacturer = _A4Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 2),
    _A4Manufacturer_Type()
)
a4Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Manufacturer.setStatus("mandatory")
_A4Version_Type = DmiDisplaystring
_A4Version_Object = MibTableColumn
a4Version = _A4Version_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 3),
    _A4Version_Type()
)
a4Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Version.setStatus("mandatory")
_A4BiosRomSize_Type = DmiInteger
_A4BiosRomSize_Object = MibTableColumn
a4BiosRomSize = _A4BiosRomSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 4),
    _A4BiosRomSize_Type()
)
a4BiosRomSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosRomSize.setStatus("mandatory")
_A4StartingAddress_Type = DmiInteger64
_A4StartingAddress_Object = MibTableColumn
a4StartingAddress = _A4StartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 5),
    _A4StartingAddress_Type()
)
a4StartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4StartingAddress.setStatus("mandatory")
_A4EndingAddress_Type = DmiInteger64
_A4EndingAddress_Object = MibTableColumn
a4EndingAddress = _A4EndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 6),
    _A4EndingAddress_Type()
)
a4EndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4EndingAddress.setStatus("mandatory")
_A4LoaderVersion_Type = DmiDisplaystring
_A4LoaderVersion_Object = MibTableColumn
a4LoaderVersion = _A4LoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 7),
    _A4LoaderVersion_Type()
)
a4LoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4LoaderVersion.setStatus("mandatory")
_A4BiosReleaseDate_Type = DmiDate
_A4BiosReleaseDate_Object = MibTableColumn
a4BiosReleaseDate = _A4BiosReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 8),
    _A4BiosReleaseDate_Type()
)
a4BiosReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosReleaseDate.setStatus("mandatory")


class _A4PrimaryBios_Type(Integer32):
    """Custom type a4PrimaryBios based on Integer32"""
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


_A4PrimaryBios_Type.__name__ = "Integer32"
_A4PrimaryBios_Object = MibTableColumn
a4PrimaryBios = _A4PrimaryBios_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 4, 1, 9),
    _A4PrimaryBios_Type()
)
a4PrimaryBios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4PrimaryBios.setStatus("mandatory")
_TSystemBiosCharacteristic_Object = MibTable
tSystemBiosCharacteristic = _TSystemBiosCharacteristic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tSystemBiosCharacteristic.setStatus("mandatory")
_ESystemBiosCharacteristic_Object = MibTableRow
eSystemBiosCharacteristic = _ESystemBiosCharacteristic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 5, 1)
)
eSystemBiosCharacteristic.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a5BiosCharacteristicsIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a5BiosNumber"),
)
if mibBuilder.loadTexts:
    eSystemBiosCharacteristic.setStatus("mandatory")
_A5BiosCharacteristicsIndex_Type = DmiInteger
_A5BiosCharacteristicsIndex_Object = MibTableColumn
a5BiosCharacteristicsIndex = _A5BiosCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 5, 1, 1),
    _A5BiosCharacteristicsIndex_Type()
)
a5BiosCharacteristicsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosCharacteristicsIndex.setStatus("mandatory")
_A5BiosNumber_Type = DmiInteger
_A5BiosNumber_Object = MibTableColumn
a5BiosNumber = _A5BiosNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 5, 1, 2),
    _A5BiosNumber_Type()
)
a5BiosNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosNumber.setStatus("mandatory")


class _A5BiosCharacteristics_Type(Integer32):
    """Custom type a5BiosCharacteristics based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("vApmSupport", 10),
          ("vBios-shadowing-allowed", 12),
          ("vEisa-support", 6),
          ("vEscdSupport", 14),
          ("vIsa-support", 4),
          ("vMca-support", 5),
          ("vOther", 1),
          ("vPci-support", 7),
          ("vPcmcia-support", 8),
          ("vPnp-support", 9),
          ("vUnknown", 2),
          ("vUnsupported", 3),
          ("vUpgradeable-bios", 11),
          ("vVl-vesa-support", 13))
    )


_A5BiosCharacteristics_Type.__name__ = "Integer32"
_A5BiosCharacteristics_Object = MibTableColumn
a5BiosCharacteristics = _A5BiosCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 5, 1, 3),
    _A5BiosCharacteristics_Type()
)
a5BiosCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosCharacteristics.setStatus("mandatory")
_A5BiosCharacteristicsDescription_Type = DmiDisplaystring
_A5BiosCharacteristicsDescription_Object = MibTableColumn
a5BiosCharacteristicsDescription = _A5BiosCharacteristicsDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 5, 1, 4),
    _A5BiosCharacteristicsDescription_Type()
)
a5BiosCharacteristicsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosCharacteristicsDescription.setStatus("mandatory")
_TProcessor_Object = MibTable
tProcessor = _TProcessor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tProcessor.setStatus("mandatory")
_EProcessor_Object = MibTableRow
eProcessor = _EProcessor_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1)
)
eProcessor.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a6ProcessorIndex"),
)
if mibBuilder.loadTexts:
    eProcessor.setStatus("mandatory")
_A6ProcessorIndex_Type = DmiInteger
_A6ProcessorIndex_Object = MibTableColumn
a6ProcessorIndex = _A6ProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 1),
    _A6ProcessorIndex_Type()
)
a6ProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorIndex.setStatus("mandatory")


class _A6Type_Type(Integer32):
    """Custom type a6Type based on Integer32"""
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
        *(("vCentralProcessor", 3),
          ("vDsp-processor", 5),
          ("vMath-processor", 4),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vVideo-processor", 6))
    )


_A6Type_Type.__name__ = "Integer32"
_A6Type_Object = MibTableColumn
a6Type = _A6Type_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 2),
    _A6Type_Type()
)
a6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Type.setStatus("mandatory")


class _A6ProcessorFamily_Type(Integer32):
    """Custom type a6ProcessorFamily based on Integer32"""
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
              32,
              48,
              64,
              80,
              96,
              112,
              128,
              144)
        )
    )
    namedValues = NamedValues(
        *(("v68040Family", 96),
          ("v80286", 4),
          ("v80287", 8),
          ("v80386", 5),
          ("v80387", 9),
          ("v80486", 6),
          ("v80487", 10),
          ("v8086", 3),
          ("v8087", 7),
          ("vAlphaFamily", 48),
          ("vHobbitFamily", 112),
          ("vMipsFamily", 64),
          ("vOther", 1),
          ("vPa-riscFamily", 144),
          ("vPentiumFamily", 11),
          ("vPowerPcFamily", 32),
          ("vSparcFamily", 80),
          ("vUnknown", 2),
          ("vWeitek", 128))
    )


_A6ProcessorFamily_Type.__name__ = "Integer32"
_A6ProcessorFamily_Object = MibTableColumn
a6ProcessorFamily = _A6ProcessorFamily_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 3),
    _A6ProcessorFamily_Type()
)
a6ProcessorFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorFamily.setStatus("mandatory")
_A6VersionInformation_Type = DmiDisplaystring
_A6VersionInformation_Object = MibTableColumn
a6VersionInformation = _A6VersionInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 4),
    _A6VersionInformation_Type()
)
a6VersionInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6VersionInformation.setStatus("mandatory")
_A6MaximumSpeed_Type = DmiInteger
_A6MaximumSpeed_Object = MibTableColumn
a6MaximumSpeed = _A6MaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 5),
    _A6MaximumSpeed_Type()
)
a6MaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6MaximumSpeed.setStatus("mandatory")
_A6CurrentSpeed_Type = DmiInteger
_A6CurrentSpeed_Object = MibTableColumn
a6CurrentSpeed = _A6CurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 6),
    _A6CurrentSpeed_Type()
)
a6CurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6CurrentSpeed.setStatus("mandatory")


class _A6ProcessorUpgrade_Type(Integer32):
    """Custom type a6ProcessorUpgrade based on Integer32"""
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
        *(("vDaughterBoard", 3),
          ("vNone", 6),
          ("vOther", 1),
          ("vReplacementpiggyBack", 5),
          ("vUnknown", 2),
          ("vZifSocket", 4))
    )


_A6ProcessorUpgrade_Type.__name__ = "Integer32"
_A6ProcessorUpgrade_Object = MibTableColumn
a6ProcessorUpgrade = _A6ProcessorUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 7),
    _A6ProcessorUpgrade_Type()
)
a6ProcessorUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorUpgrade.setStatus("mandatory")
_A6FruGroupIndex_Type = DmiInteger
_A6FruGroupIndex_Object = MibTableColumn
a6FruGroupIndex = _A6FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 8),
    _A6FruGroupIndex_Type()
)
a6FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6FruGroupIndex.setStatus("mandatory")
_A6OperationalGroupIndex_Type = DmiInteger
_A6OperationalGroupIndex_Object = MibTableColumn
a6OperationalGroupIndex = _A6OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 6, 1, 9),
    _A6OperationalGroupIndex_Type()
)
a6OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6OperationalGroupIndex.setStatus("mandatory")
_TMotherboard_Object = MibTable
tMotherboard = _TMotherboard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tMotherboard.setStatus("mandatory")
_EMotherboard_Object = MibTableRow
eMotherboard = _EMotherboard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 7, 1)
)
eMotherboard.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMotherboard.setStatus("mandatory")
_A7NumberOfExpansionSlots_Type = DmiInteger
_A7NumberOfExpansionSlots_Object = MibTableColumn
a7NumberOfExpansionSlots = _A7NumberOfExpansionSlots_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 7, 1, 1),
    _A7NumberOfExpansionSlots_Type()
)
a7NumberOfExpansionSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7NumberOfExpansionSlots.setStatus("mandatory")
_A7FruGroupIndex_Type = DmiInteger
_A7FruGroupIndex_Object = MibTableColumn
a7FruGroupIndex = _A7FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 7, 1, 2),
    _A7FruGroupIndex_Type()
)
a7FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7FruGroupIndex.setStatus("mandatory")
_A7OperationalGroupIndex_Type = DmiInteger
_A7OperationalGroupIndex_Object = MibTableColumn
a7OperationalGroupIndex = _A7OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 7, 1, 3),
    _A7OperationalGroupIndex_Type()
)
a7OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7OperationalGroupIndex.setStatus("mandatory")
_TPhysicalMemory_Object = MibTable
tPhysicalMemory = _TPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tPhysicalMemory.setStatus("mandatory")
_EPhysicalMemory_Object = MibTableRow
ePhysicalMemory = _EPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1)
)
ePhysicalMemory.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a8PhysicalMemoryIndex"),
)
if mibBuilder.loadTexts:
    ePhysicalMemory.setStatus("mandatory")
_A8PhysicalMemoryIndex_Type = DmiInteger
_A8PhysicalMemoryIndex_Object = MibTableColumn
a8PhysicalMemoryIndex = _A8PhysicalMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 1),
    _A8PhysicalMemoryIndex_Type()
)
a8PhysicalMemoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8PhysicalMemoryIndex.setStatus("mandatory")


class _A8PhysicalMemoryLocation_Type(Integer32):
    """Custom type a8PhysicalMemoryLocation based on Integer32"""
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
        *(("vEisaAddOnCard", 5),
          ("vIsaAddOnCard", 4),
          ("vMcaAddOnCard", 7),
          ("vOther", 1),
          ("vPciAddOnCard", 6),
          ("vPcmciaAddOnCard", 8),
          ("vProprietaryAddOnCard", 9),
          ("vSystemBoardOrMotherBoard", 3),
          ("vUnknown", 2))
    )


_A8PhysicalMemoryLocation_Type.__name__ = "Integer32"
_A8PhysicalMemoryLocation_Object = MibTableColumn
a8PhysicalMemoryLocation = _A8PhysicalMemoryLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 2),
    _A8PhysicalMemoryLocation_Type()
)
a8PhysicalMemoryLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8PhysicalMemoryLocation.setStatus("mandatory")
_A8MemoryStartingAddress_Type = DmiInteger64
_A8MemoryStartingAddress_Object = MibTableColumn
a8MemoryStartingAddress = _A8MemoryStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 3),
    _A8MemoryStartingAddress_Type()
)
a8MemoryStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8MemoryStartingAddress.setStatus("mandatory")
_A8MemoryEndingAddress_Type = DmiInteger64
_A8MemoryEndingAddress_Object = MibTableColumn
a8MemoryEndingAddress = _A8MemoryEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 4),
    _A8MemoryEndingAddress_Type()
)
a8MemoryEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8MemoryEndingAddress.setStatus("mandatory")


class _A8MemoryUsage_Type(Integer32):
    """Custom type a8MemoryUsage based on Integer32"""
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
        *(("vFlashMemory", 5),
          ("vNonVolatileRam", 6),
          ("vOther", 1),
          ("vSystemMemory", 3),
          ("vUnknown", 2),
          ("vVideoMemory", 4))
    )


_A8MemoryUsage_Type.__name__ = "Integer32"
_A8MemoryUsage_Object = MibTableColumn
a8MemoryUsage = _A8MemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 5),
    _A8MemoryUsage_Type()
)
a8MemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8MemoryUsage.setStatus("mandatory")
_A8MaximumMemoryCapacity_Type = DmiInteger
_A8MaximumMemoryCapacity_Object = MibTableColumn
a8MaximumMemoryCapacity = _A8MaximumMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 6),
    _A8MaximumMemoryCapacity_Type()
)
a8MaximumMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8MaximumMemoryCapacity.setStatus("mandatory")
_A8NumberOfSimmSlots_Type = DmiInteger
_A8NumberOfSimmSlots_Object = MibTableColumn
a8NumberOfSimmSlots = _A8NumberOfSimmSlots_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 7),
    _A8NumberOfSimmSlots_Type()
)
a8NumberOfSimmSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfSimmSlots.setStatus("mandatory")
_A8NumberOfSimmSlotsUsed_Type = DmiInteger
_A8NumberOfSimmSlotsUsed_Object = MibTableColumn
a8NumberOfSimmSlotsUsed = _A8NumberOfSimmSlotsUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 8),
    _A8NumberOfSimmSlotsUsed_Type()
)
a8NumberOfSimmSlotsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfSimmSlotsUsed.setStatus("mandatory")
_A8MemorySpeed_Type = DmiInteger
_A8MemorySpeed_Object = MibTableColumn
a8MemorySpeed = _A8MemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 9),
    _A8MemorySpeed_Type()
)
a8MemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8MemorySpeed.setStatus("mandatory")


class _A8MemoryErrorCorrection_Type(Integer32):
    """Custom type a8MemoryErrorCorrection based on Integer32"""
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
        *(("vMultibitEcc", 6),
          ("vNone", 3),
          ("vOther", 1),
          ("vParity", 4),
          ("vSingleBitEcc", 5),
          ("vUnknown", 2))
    )


_A8MemoryErrorCorrection_Type.__name__ = "Integer32"
_A8MemoryErrorCorrection_Object = MibTableColumn
a8MemoryErrorCorrection = _A8MemoryErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 10),
    _A8MemoryErrorCorrection_Type()
)
a8MemoryErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8MemoryErrorCorrection.setStatus("mandatory")
_A8FruGroupIndex_Type = DmiInteger
_A8FruGroupIndex_Object = MibTableColumn
a8FruGroupIndex = _A8FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 11),
    _A8FruGroupIndex_Type()
)
a8FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8FruGroupIndex.setStatus("mandatory")
_A8OperationalGroupIndex_Type = DmiInteger
_A8OperationalGroupIndex_Object = MibTableColumn
a8OperationalGroupIndex = _A8OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 8, 1, 12),
    _A8OperationalGroupIndex_Type()
)
a8OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8OperationalGroupIndex.setStatus("mandatory")
_TLogicalMemory_Object = MibTable
tLogicalMemory = _TLogicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tLogicalMemory.setStatus("mandatory")
_ELogicalMemory_Object = MibTableRow
eLogicalMemory = _ELogicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1)
)
eLogicalMemory.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eLogicalMemory.setStatus("mandatory")
_A9BaseMemorySize_Type = DmiInteger
_A9BaseMemorySize_Object = MibTableColumn
a9BaseMemorySize = _A9BaseMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 1),
    _A9BaseMemorySize_Type()
)
a9BaseMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9BaseMemorySize.setStatus("mandatory")
_A9FreeBaseMemorySize_Type = DmiInteger
_A9FreeBaseMemorySize_Object = MibTableColumn
a9FreeBaseMemorySize = _A9FreeBaseMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 2),
    _A9FreeBaseMemorySize_Type()
)
a9FreeBaseMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9FreeBaseMemorySize.setStatus("mandatory")
_A9ExtendedMemorySize_Type = DmiInteger
_A9ExtendedMemorySize_Object = MibTableColumn
a9ExtendedMemorySize = _A9ExtendedMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 3),
    _A9ExtendedMemorySize_Type()
)
a9ExtendedMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExtendedMemorySize.setStatus("mandatory")
_A9FreeExtendedMemorySize_Type = DmiInteger
_A9FreeExtendedMemorySize_Object = MibTableColumn
a9FreeExtendedMemorySize = _A9FreeExtendedMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 4),
    _A9FreeExtendedMemorySize_Type()
)
a9FreeExtendedMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9FreeExtendedMemorySize.setStatus("mandatory")
_A9ExtendedMemoryManagerName_Type = DmiDisplaystring
_A9ExtendedMemoryManagerName_Object = MibTableColumn
a9ExtendedMemoryManagerName = _A9ExtendedMemoryManagerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 5),
    _A9ExtendedMemoryManagerName_Type()
)
a9ExtendedMemoryManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExtendedMemoryManagerName.setStatus("mandatory")
_A9ExtendedMemoryManagerVersion_Type = DmiDisplaystring
_A9ExtendedMemoryManagerVersion_Object = MibTableColumn
a9ExtendedMemoryManagerVersion = _A9ExtendedMemoryManagerVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 6),
    _A9ExtendedMemoryManagerVersion_Type()
)
a9ExtendedMemoryManagerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExtendedMemoryManagerVersion.setStatus("mandatory")
_A9ExpandedMemorySize_Type = DmiInteger
_A9ExpandedMemorySize_Object = MibTableColumn
a9ExpandedMemorySize = _A9ExpandedMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 7),
    _A9ExpandedMemorySize_Type()
)
a9ExpandedMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExpandedMemorySize.setStatus("mandatory")
_A9FreeExpandedMemorySize_Type = DmiInteger
_A9FreeExpandedMemorySize_Object = MibTableColumn
a9FreeExpandedMemorySize = _A9FreeExpandedMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 8),
    _A9FreeExpandedMemorySize_Type()
)
a9FreeExpandedMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9FreeExpandedMemorySize.setStatus("mandatory")
_A9ExpandedMemoryManagerName_Type = DmiDisplaystring
_A9ExpandedMemoryManagerName_Object = MibTableColumn
a9ExpandedMemoryManagerName = _A9ExpandedMemoryManagerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 9),
    _A9ExpandedMemoryManagerName_Type()
)
a9ExpandedMemoryManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExpandedMemoryManagerName.setStatus("mandatory")
_A9ExpandedMemoryManagerVersion_Type = DmiDisplaystring
_A9ExpandedMemoryManagerVersion_Object = MibTableColumn
a9ExpandedMemoryManagerVersion = _A9ExpandedMemoryManagerVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 10),
    _A9ExpandedMemoryManagerVersion_Type()
)
a9ExpandedMemoryManagerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExpandedMemoryManagerVersion.setStatus("mandatory")
_A9ExpandedMemoryPageFrameAddress_Type = DmiInteger64
_A9ExpandedMemoryPageFrameAddress_Object = MibTableColumn
a9ExpandedMemoryPageFrameAddress = _A9ExpandedMemoryPageFrameAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 11),
    _A9ExpandedMemoryPageFrameAddress_Type()
)
a9ExpandedMemoryPageFrameAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExpandedMemoryPageFrameAddress.setStatus("mandatory")
_A9ExpandedMemoryPageFrameSize_Type = DmiInteger
_A9ExpandedMemoryPageFrameSize_Object = MibTableColumn
a9ExpandedMemoryPageFrameSize = _A9ExpandedMemoryPageFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 12),
    _A9ExpandedMemoryPageFrameSize_Type()
)
a9ExpandedMemoryPageFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExpandedMemoryPageFrameSize.setStatus("mandatory")
_A9ExpandedMemoryPageSize_Type = DmiInteger
_A9ExpandedMemoryPageSize_Object = MibTableColumn
a9ExpandedMemoryPageSize = _A9ExpandedMemoryPageSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 9, 1, 13),
    _A9ExpandedMemoryPageSize_Type()
)
a9ExpandedMemoryPageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ExpandedMemoryPageSize.setStatus("mandatory")
_TSystemCache_Object = MibTable
tSystemCache = _TSystemCache_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tSystemCache.setStatus("mandatory")
_ESystemCache_Object = MibTableRow
eSystemCache = _ESystemCache_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1)
)
eSystemCache.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a10SystemCacheIndex"),
)
if mibBuilder.loadTexts:
    eSystemCache.setStatus("mandatory")
_A10SystemCacheIndex_Type = DmiInteger
_A10SystemCacheIndex_Object = MibTableColumn
a10SystemCacheIndex = _A10SystemCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 1),
    _A10SystemCacheIndex_Type()
)
a10SystemCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheIndex.setStatus("mandatory")


class _A10SystemCacheLevel_Type(Integer32):
    """Custom type a10SystemCacheLevel based on Integer32"""
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
        *(("vOther", 1),
          ("vPrimary", 3),
          ("vSecondary", 4),
          ("vTertiary", 5),
          ("vUnknown", 2))
    )


_A10SystemCacheLevel_Type.__name__ = "Integer32"
_A10SystemCacheLevel_Object = MibTableColumn
a10SystemCacheLevel = _A10SystemCacheLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 2),
    _A10SystemCacheLevel_Type()
)
a10SystemCacheLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheLevel.setStatus("mandatory")
_A10SystemCacheSpeed_Type = DmiInteger
_A10SystemCacheSpeed_Object = MibTableColumn
a10SystemCacheSpeed = _A10SystemCacheSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 3),
    _A10SystemCacheSpeed_Type()
)
a10SystemCacheSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheSpeed.setStatus("mandatory")
_A10SystemCacheSize_Type = DmiInteger
_A10SystemCacheSize_Object = MibTableColumn
a10SystemCacheSize = _A10SystemCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 4),
    _A10SystemCacheSize_Type()
)
a10SystemCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheSize.setStatus("mandatory")


class _A10SystemCacheWritePolicy_Type(Integer32):
    """Custom type a10SystemCacheWritePolicy based on Integer32"""
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
        *(("vOther", 1),
          ("vUnknown", 2),
          ("vWriteBack", 3),
          ("vWriteThrough", 4))
    )


_A10SystemCacheWritePolicy_Type.__name__ = "Integer32"
_A10SystemCacheWritePolicy_Object = MibTableColumn
a10SystemCacheWritePolicy = _A10SystemCacheWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 5),
    _A10SystemCacheWritePolicy_Type()
)
a10SystemCacheWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheWritePolicy.setStatus("mandatory")


class _A10SystemCacheErrorCorrection_Type(Integer32):
    """Custom type a10SystemCacheErrorCorrection based on Integer32"""
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
        *(("vMultibitEcc", 6),
          ("vNone", 3),
          ("vOther", 1),
          ("vParity", 4),
          ("vSingleBitEcc", 5),
          ("vUnknown", 2))
    )


_A10SystemCacheErrorCorrection_Type.__name__ = "Integer32"
_A10SystemCacheErrorCorrection_Object = MibTableColumn
a10SystemCacheErrorCorrection = _A10SystemCacheErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 6),
    _A10SystemCacheErrorCorrection_Type()
)
a10SystemCacheErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheErrorCorrection.setStatus("mandatory")
_A10FruGroupIndex_Type = DmiInteger
_A10FruGroupIndex_Object = MibTableColumn
a10FruGroupIndex = _A10FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 7),
    _A10FruGroupIndex_Type()
)
a10FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10FruGroupIndex.setStatus("mandatory")
_A10OperationalGroupIndex_Type = DmiInteger
_A10OperationalGroupIndex_Object = MibTableColumn
a10OperationalGroupIndex = _A10OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 10, 1, 8),
    _A10OperationalGroupIndex_Type()
)
a10OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10OperationalGroupIndex.setStatus("mandatory")
_TParallelPorts_Object = MibTable
tParallelPorts = _TParallelPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tParallelPorts.setStatus("mandatory")
_EParallelPorts_Object = MibTableRow
eParallelPorts = _EParallelPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1)
)
eParallelPorts.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a11ParallelPortIndex"),
)
if mibBuilder.loadTexts:
    eParallelPorts.setStatus("mandatory")
_A11ParallelPortIndex_Type = DmiInteger
_A11ParallelPortIndex_Object = MibTableColumn
a11ParallelPortIndex = _A11ParallelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 1),
    _A11ParallelPortIndex_Type()
)
a11ParallelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ParallelPortIndex.setStatus("mandatory")
_A11ParallelBaseIoAddress_Type = DmiInteger64
_A11ParallelBaseIoAddress_Object = MibTableColumn
a11ParallelBaseIoAddress = _A11ParallelBaseIoAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 2),
    _A11ParallelBaseIoAddress_Type()
)
a11ParallelBaseIoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ParallelBaseIoAddress.setStatus("mandatory")
_A11IrqUsed_Type = DmiInteger
_A11IrqUsed_Object = MibTableColumn
a11IrqUsed = _A11IrqUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 3),
    _A11IrqUsed_Type()
)
a11IrqUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11IrqUsed.setStatus("mandatory")
_A11LogicalName_Type = DmiDisplaystring
_A11LogicalName_Object = MibTableColumn
a11LogicalName = _A11LogicalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 4),
    _A11LogicalName_Type()
)
a11LogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11LogicalName.setStatus("mandatory")


class _A11ConnectorType_Type(Integer32):
    """Custom type a11ConnectorType based on Integer32"""
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
        *(("vCentronics", 5),
          ("vDb-25Female", 3),
          ("vDb-25Male", 4),
          ("vMini-centronics", 6),
          ("vOther", 1),
          ("vProprietary", 7),
          ("vUnknown", 2))
    )


_A11ConnectorType_Type.__name__ = "Integer32"
_A11ConnectorType_Object = MibTableColumn
a11ConnectorType = _A11ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 5),
    _A11ConnectorType_Type()
)
a11ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ConnectorType.setStatus("mandatory")


class _A11ConnectorPinout_Type(Integer32):
    """Custom type a11ConnectorPinout based on Integer32"""
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
        *(("vIeee1284", 5),
          ("vOther", 1),
          ("vProprietary", 6),
          ("vPs2", 4),
          ("vUnknown", 2),
          ("vXtat", 3))
    )


_A11ConnectorPinout_Type.__name__ = "Integer32"
_A11ConnectorPinout_Object = MibTableColumn
a11ConnectorPinout = _A11ConnectorPinout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 6),
    _A11ConnectorPinout_Type()
)
a11ConnectorPinout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ConnectorPinout.setStatus("mandatory")


class _A11DmaSupport_Type(Integer32):
    """Custom type a11DmaSupport based on Integer32"""
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


_A11DmaSupport_Type.__name__ = "Integer32"
_A11DmaSupport_Object = MibTableColumn
a11DmaSupport = _A11DmaSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 7),
    _A11DmaSupport_Type()
)
a11DmaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11DmaSupport.setStatus("mandatory")
_A11ParallelPortCapabilities_Type = DmiInteger
_A11ParallelPortCapabilities_Object = MibTableColumn
a11ParallelPortCapabilities = _A11ParallelPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 8),
    _A11ParallelPortCapabilities_Type()
)
a11ParallelPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ParallelPortCapabilities.setStatus("mandatory")
_A11OperationalGroupIndex_Type = DmiInteger
_A11OperationalGroupIndex_Object = MibTableColumn
a11OperationalGroupIndex = _A11OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 11, 1, 9),
    _A11OperationalGroupIndex_Type()
)
a11OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11OperationalGroupIndex.setStatus("mandatory")
_TSerialPorts_Object = MibTable
tSerialPorts = _TSerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tSerialPorts.setStatus("mandatory")
_ESerialPorts_Object = MibTableRow
eSerialPorts = _ESerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1)
)
eSerialPorts.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a12SerialPortIndex"),
)
if mibBuilder.loadTexts:
    eSerialPorts.setStatus("mandatory")
_A12SerialPortIndex_Type = DmiInteger
_A12SerialPortIndex_Object = MibTableColumn
a12SerialPortIndex = _A12SerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 1),
    _A12SerialPortIndex_Type()
)
a12SerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SerialPortIndex.setStatus("mandatory")
_A12SerialBaseIo_Type = DmiInteger64
_A12SerialBaseIo_Object = MibTableColumn
a12SerialBaseIo = _A12SerialBaseIo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 2),
    _A12SerialBaseIo_Type()
)
a12SerialBaseIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SerialBaseIo.setStatus("mandatory")
_A12IrqUsed_Type = DmiInteger
_A12IrqUsed_Object = MibTableColumn
a12IrqUsed = _A12IrqUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 3),
    _A12IrqUsed_Type()
)
a12IrqUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12IrqUsed.setStatus("mandatory")
_A12LogicalName_Type = DmiDisplaystring
_A12LogicalName_Object = MibTableColumn
a12LogicalName = _A12LogicalName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 4),
    _A12LogicalName_Type()
)
a12LogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12LogicalName.setStatus("mandatory")


class _A12ConnectorType_Type(Integer32):
    """Custom type a12ConnectorType based on Integer32"""
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
        *(("vDb-25PinFemale", 6),
          ("vDb-25PinMale", 5),
          ("vDb-9PinFemale", 4),
          ("vDb-9PinMale", 3),
          ("vOther", 1),
          ("vProprietary", 9),
          ("vRj-11", 7),
          ("vRj-45", 8),
          ("vUnknown", 2))
    )


_A12ConnectorType_Type.__name__ = "Integer32"
_A12ConnectorType_Object = MibTableColumn
a12ConnectorType = _A12ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 5),
    _A12ConnectorType_Type()
)
a12ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12ConnectorType.setStatus("mandatory")
_A12MaximumSpeed_Type = DmiInteger
_A12MaximumSpeed_Object = MibTableColumn
a12MaximumSpeed = _A12MaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 6),
    _A12MaximumSpeed_Type()
)
a12MaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12MaximumSpeed.setStatus("mandatory")


class _A12SerialPortCapabilities_Type(Integer32):
    """Custom type a12SerialPortCapabilities based on Integer32"""
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
        *(("v16450Compatible", 4),
          ("v16550Compatible", 5),
          ("v16550aCompatible", 6),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vXtatCcompatible", 3))
    )


_A12SerialPortCapabilities_Type.__name__ = "Integer32"
_A12SerialPortCapabilities_Object = MibTableColumn
a12SerialPortCapabilities = _A12SerialPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 7),
    _A12SerialPortCapabilities_Type()
)
a12SerialPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SerialPortCapabilities.setStatus("mandatory")
_A12OperationalGroupIndex_Type = DmiInteger
_A12OperationalGroupIndex_Object = MibTableColumn
a12OperationalGroupIndex = _A12OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 12, 1, 8),
    _A12OperationalGroupIndex_Type()
)
a12OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12OperationalGroupIndex.setStatus("mandatory")
_TIrq_Object = MibTable
tIrq = _TIrq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 13)
)
if mibBuilder.loadTexts:
    tIrq.setStatus("mandatory")
_EIrq_Object = MibTableRow
eIrq = _EIrq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 13, 1)
)
eIrq.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a13IrqNumber"),
)
if mibBuilder.loadTexts:
    eIrq.setStatus("mandatory")
_A13IrqNumber_Type = DmiInteger
_A13IrqNumber_Object = MibTableColumn
a13IrqNumber = _A13IrqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 13, 1, 1),
    _A13IrqNumber_Type()
)
a13IrqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13IrqNumber.setStatus("mandatory")


class _A13AvailabilityOfIrq_Type(Integer32):
    """Custom type a13AvailabilityOfIrq based on Integer32"""
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
        *(("vAvailable", 3),
          ("vInUse", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A13AvailabilityOfIrq_Type.__name__ = "Integer32"
_A13AvailabilityOfIrq_Object = MibTableColumn
a13AvailabilityOfIrq = _A13AvailabilityOfIrq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 13, 1, 2),
    _A13AvailabilityOfIrq_Type()
)
a13AvailabilityOfIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13AvailabilityOfIrq.setStatus("mandatory")


class _A13IrqTriggerType_Type(Integer32):
    """Custom type a13IrqTriggerType based on Integer32"""
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
        *(("vEdge", 4),
          ("vLevel", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A13IrqTriggerType_Type.__name__ = "Integer32"
_A13IrqTriggerType_Object = MibTableColumn
a13IrqTriggerType = _A13IrqTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 13, 1, 3),
    _A13IrqTriggerType_Type()
)
a13IrqTriggerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13IrqTriggerType.setStatus("mandatory")


class _A13IrqShareable_Type(Integer32):
    """Custom type a13IrqShareable based on Integer32"""
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


_A13IrqShareable_Type.__name__ = "Integer32"
_A13IrqShareable_Object = MibTableColumn
a13IrqShareable = _A13IrqShareable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 13, 1, 4),
    _A13IrqShareable_Type()
)
a13IrqShareable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13IrqShareable.setStatus("mandatory")
_A13IrqDescription_Type = DmiDisplaystring
_A13IrqDescription_Object = MibTableColumn
a13IrqDescription = _A13IrqDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 13, 1, 5),
    _A13IrqDescription_Type()
)
a13IrqDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13IrqDescription.setStatus("mandatory")
_TDma_Object = MibTable
tDma = _TDma_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tDma.setStatus("mandatory")
_EDma_Object = MibTableRow
eDma = _EDma_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 14, 1)
)
eDma.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a14DmaNumber"),
)
if mibBuilder.loadTexts:
    eDma.setStatus("mandatory")
_A14DmaNumber_Type = DmiInteger
_A14DmaNumber_Object = MibTableColumn
a14DmaNumber = _A14DmaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 14, 1, 1),
    _A14DmaNumber_Type()
)
a14DmaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14DmaNumber.setStatus("mandatory")


class _A14AvailabilityOfDma_Type(Integer32):
    """Custom type a14AvailabilityOfDma based on Integer32"""
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


_A14AvailabilityOfDma_Type.__name__ = "Integer32"
_A14AvailabilityOfDma_Object = MibTableColumn
a14AvailabilityOfDma = _A14AvailabilityOfDma_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 14, 1, 2),
    _A14AvailabilityOfDma_Type()
)
a14AvailabilityOfDma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14AvailabilityOfDma.setStatus("mandatory")


class _A14DmaBurstMode_Type(Integer32):
    """Custom type a14DmaBurstMode based on Integer32"""
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


_A14DmaBurstMode_Type.__name__ = "Integer32"
_A14DmaBurstMode_Object = MibTableColumn
a14DmaBurstMode = _A14DmaBurstMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 14, 1, 3),
    _A14DmaBurstMode_Type()
)
a14DmaBurstMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14DmaBurstMode.setStatus("mandatory")
_A14DmaDescription_Type = DmiDisplaystring
_A14DmaDescription_Object = MibTableColumn
a14DmaDescription = _A14DmaDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 14, 1, 4),
    _A14DmaDescription_Type()
)
a14DmaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14DmaDescription.setStatus("mandatory")
_TMemoryMappedIo_Object = MibTable
tMemoryMappedIo = _TMemoryMappedIo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 15)
)
if mibBuilder.loadTexts:
    tMemoryMappedIo.setStatus("mandatory")
_EMemoryMappedIo_Object = MibTableRow
eMemoryMappedIo = _EMemoryMappedIo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 15, 1)
)
eMemoryMappedIo.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a15MemoryMappedIoStartingAddress"),
)
if mibBuilder.loadTexts:
    eMemoryMappedIo.setStatus("mandatory")
_A15MemoryMappedIoStartingAddress_Type = DmiInteger64
_A15MemoryMappedIoStartingAddress_Object = MibTableColumn
a15MemoryMappedIoStartingAddress = _A15MemoryMappedIoStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 15, 1, 1),
    _A15MemoryMappedIoStartingAddress_Type()
)
a15MemoryMappedIoStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15MemoryMappedIoStartingAddress.setStatus("mandatory")
_A15MemoryMappedIoEndingAddress_Type = DmiInteger64
_A15MemoryMappedIoEndingAddress_Object = MibTableColumn
a15MemoryMappedIoEndingAddress = _A15MemoryMappedIoEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 15, 1, 2),
    _A15MemoryMappedIoEndingAddress_Type()
)
a15MemoryMappedIoEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15MemoryMappedIoEndingAddress.setStatus("mandatory")
_A15MemoryMappedIoDescription_Type = DmiDisplaystring
_A15MemoryMappedIoDescription_Object = MibTableColumn
a15MemoryMappedIoDescription = _A15MemoryMappedIoDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 15, 1, 3),
    _A15MemoryMappedIoDescription_Type()
)
a15MemoryMappedIoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15MemoryMappedIoDescription.setStatus("mandatory")
_TSystemEnclosure_Object = MibTable
tSystemEnclosure = _TSystemEnclosure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16)
)
if mibBuilder.loadTexts:
    tSystemEnclosure.setStatus("mandatory")
_ESystemEnclosure_Object = MibTableRow
eSystemEnclosure = _ESystemEnclosure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1)
)
eSystemEnclosure.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSystemEnclosure.setStatus("mandatory")


class _A16EnclosureOrChassis_Type(Integer32):
    """Custom type a16EnclosureOrChassis based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("vDesktop", 3),
          ("vDockingStation", 12),
          ("vHandHeld", 11),
          ("vLaptop", 9),
          ("vLowProfileDesktop", 4),
          ("vMiniTower", 6),
          ("vNotebook", 10),
          ("vOther", 1),
          ("vPizzaBox", 5),
          ("vPortable", 8),
          ("vTower", 7),
          ("vUnknown", 2))
    )


_A16EnclosureOrChassis_Type.__name__ = "Integer32"
_A16EnclosureOrChassis_Object = MibTableColumn
a16EnclosureOrChassis = _A16EnclosureOrChassis_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 1),
    _A16EnclosureOrChassis_Type()
)
a16EnclosureOrChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16EnclosureOrChassis.setStatus("mandatory")
_A16AssetTag_Type = DmiDisplaystring
_A16AssetTag_Object = MibTableColumn
a16AssetTag = _A16AssetTag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 2),
    _A16AssetTag_Type()
)
a16AssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a16AssetTag.setStatus("mandatory")


class _A16ChassisLockPresent_Type(Integer32):
    """Custom type a16ChassisLockPresent based on Integer32"""
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


_A16ChassisLockPresent_Type.__name__ = "Integer32"
_A16ChassisLockPresent_Object = MibTableColumn
a16ChassisLockPresent = _A16ChassisLockPresent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 3),
    _A16ChassisLockPresent_Type()
)
a16ChassisLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16ChassisLockPresent.setStatus("mandatory")


class _A16BootUpState_Type(Integer32):
    """Custom type a16BootUpState based on Integer32"""
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
        *(("vCritical", 5),
          ("vOther", 1),
          ("vSafe", 3),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A16BootUpState_Type.__name__ = "Integer32"
_A16BootUpState_Object = MibTableColumn
a16BootUpState = _A16BootUpState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 4),
    _A16BootUpState_Type()
)
a16BootUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16BootUpState.setStatus("mandatory")


class _A16PowerState_Type(Integer32):
    """Custom type a16PowerState based on Integer32"""
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
        *(("vCritical", 5),
          ("vOther", 1),
          ("vSafe", 3),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A16PowerState_Type.__name__ = "Integer32"
_A16PowerState_Object = MibTableColumn
a16PowerState = _A16PowerState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 5),
    _A16PowerState_Type()
)
a16PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16PowerState.setStatus("mandatory")


class _A16ThermalState_Type(Integer32):
    """Custom type a16ThermalState based on Integer32"""
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
        *(("vCritical", 5),
          ("vOther", 1),
          ("vSafe", 3),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A16ThermalState_Type.__name__ = "Integer32"
_A16ThermalState_Object = MibTableColumn
a16ThermalState = _A16ThermalState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 6),
    _A16ThermalState_Type()
)
a16ThermalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16ThermalState.setStatus("mandatory")
_A16FruGroupIndex_Type = DmiInteger
_A16FruGroupIndex_Object = MibTableColumn
a16FruGroupIndex = _A16FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 7),
    _A16FruGroupIndex_Type()
)
a16FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16FruGroupIndex.setStatus("mandatory")
_A16OperationalGroupIndex_Type = DmiInteger
_A16OperationalGroupIndex_Object = MibTableColumn
a16OperationalGroupIndex = _A16OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 16, 1, 8),
    _A16OperationalGroupIndex_Type()
)
a16OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a16OperationalGroupIndex.setStatus("mandatory")
_TPowerSupply_Object = MibTable
tPowerSupply = _TPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 17)
)
if mibBuilder.loadTexts:
    tPowerSupply.setStatus("mandatory")
_EPowerSupply_Object = MibTableRow
ePowerSupply = _EPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 17, 1)
)
ePowerSupply.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a17PowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    ePowerSupply.setStatus("mandatory")
_A17PowerSupplyIndex_Type = DmiInteger
_A17PowerSupplyIndex_Object = MibTableColumn
a17PowerSupplyIndex = _A17PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 17, 1, 1),
    _A17PowerSupplyIndex_Type()
)
a17PowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17PowerSupplyIndex.setStatus("mandatory")
_A17FruGroupIndex_Type = DmiInteger
_A17FruGroupIndex_Object = MibTableColumn
a17FruGroupIndex = _A17FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 17, 1, 2),
    _A17FruGroupIndex_Type()
)
a17FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17FruGroupIndex.setStatus("mandatory")
_A17OperationalGroupIndex_Type = DmiInteger
_A17OperationalGroupIndex_Object = MibTableColumn
a17OperationalGroupIndex = _A17OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 17, 1, 3),
    _A17OperationalGroupIndex_Type()
)
a17OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17OperationalGroupIndex.setStatus("mandatory")
_TCoolingDevice_Object = MibTable
tCoolingDevice = _TCoolingDevice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 18)
)
if mibBuilder.loadTexts:
    tCoolingDevice.setStatus("mandatory")
_ECoolingDevice_Object = MibTableRow
eCoolingDevice = _ECoolingDevice_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 18, 1)
)
eCoolingDevice.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a18CoolingDeviceIndex"),
)
if mibBuilder.loadTexts:
    eCoolingDevice.setStatus("mandatory")
_A18CoolingDeviceIndex_Type = DmiInteger
_A18CoolingDeviceIndex_Object = MibTableColumn
a18CoolingDeviceIndex = _A18CoolingDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 18, 1, 1),
    _A18CoolingDeviceIndex_Type()
)
a18CoolingDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a18CoolingDeviceIndex.setStatus("mandatory")
_A18FruGroupIndex_Type = DmiInteger
_A18FruGroupIndex_Object = MibTableColumn
a18FruGroupIndex = _A18FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 18, 1, 2),
    _A18FruGroupIndex_Type()
)
a18FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a18FruGroupIndex.setStatus("mandatory")
_A18OperationalGroupIndex_Type = DmiInteger
_A18OperationalGroupIndex_Object = MibTableColumn
a18OperationalGroupIndex = _A18OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 18, 1, 3),
    _A18OperationalGroupIndex_Type()
)
a18OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a18OperationalGroupIndex.setStatus("mandatory")
_TSystemSlots_Object = MibTable
tSystemSlots = _TSystemSlots_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 19)
)
if mibBuilder.loadTexts:
    tSystemSlots.setStatus("mandatory")
_ESystemSlots_Object = MibTableRow
eSystemSlots = _ESystemSlots_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 19, 1)
)
eSystemSlots.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a19SlotIndex"),
)
if mibBuilder.loadTexts:
    eSystemSlots.setStatus("mandatory")
_A19SlotIndex_Type = DmiInteger
_A19SlotIndex_Object = MibTableColumn
a19SlotIndex = _A19SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 19, 1, 1),
    _A19SlotIndex_Type()
)
a19SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19SlotIndex.setStatus("mandatory")


class _A19SlotType_Type(Integer32):
    """Custom type a19SlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              18,
              20,
              24)
        )
    )
    namedValues = NamedValues(
        *(("vEisa", 4),
          ("vIsa", 2),
          ("vMca", 8),
          ("vPci", 16),
          ("vPciEisa", 20),
          ("vPciIsa", 18),
          ("vPciMca", 24),
          ("vUnknown", 1))
    )


_A19SlotType_Type.__name__ = "Integer32"
_A19SlotType_Object = MibTableColumn
a19SlotType = _A19SlotType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 19, 1, 2),
    _A19SlotType_Type()
)
a19SlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19SlotType.setStatus("mandatory")


class _A19SlotWidth_Type(Integer32):
    """Custom type a19SlotWidth based on Integer32"""
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


_A19SlotWidth_Type.__name__ = "Integer32"
_A19SlotWidth_Object = MibTableColumn
a19SlotWidth = _A19SlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 19, 1, 3),
    _A19SlotWidth_Type()
)
a19SlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19SlotWidth.setStatus("mandatory")


class _A19CurrentUsage_Type(Integer32):
    """Custom type a19CurrentUsage based on Integer32"""
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
        *(("vAvailable", 3),
          ("vInUse1", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A19CurrentUsage_Type.__name__ = "Integer32"
_A19CurrentUsage_Object = MibTableColumn
a19CurrentUsage = _A19CurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 19, 1, 4),
    _A19CurrentUsage_Type()
)
a19CurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19CurrentUsage.setStatus("mandatory")
_A19SlotDescription_Type = DmiDisplaystring
_A19SlotDescription_Object = MibTableColumn
a19SlotDescription = _A19SlotDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 19, 1, 5),
    _A19SlotDescription_Type()
)
a19SlotDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19SlotDescription.setStatus("mandatory")
_TVideo_Object = MibTable
tVideo = _TVideo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20)
)
if mibBuilder.loadTexts:
    tVideo.setStatus("mandatory")
_EVideo_Object = MibTableRow
eVideo = _EVideo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1)
)
eVideo.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a20VideoIndex"),
)
if mibBuilder.loadTexts:
    eVideo.setStatus("mandatory")
_A20VideoIndex_Type = DmiInteger
_A20VideoIndex_Object = MibTableColumn
a20VideoIndex = _A20VideoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 1),
    _A20VideoIndex_Type()
)
a20VideoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20VideoIndex.setStatus("mandatory")


class _A20VideoType_Type(Integer32):
    """Custom type a20VideoType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("v8514a", 10),
          ("vCga", 3),
          ("vEga", 4),
          ("vHgc", 8),
          ("vLinearFrameBuffer", 12),
          ("vMcga", 9),
          ("vMda", 7),
          ("vOther", 1),
          ("vSvga", 6),
          ("vUnknown", 2),
          ("vVga", 5),
          ("vXga", 11))
    )


_A20VideoType_Type.__name__ = "Integer32"
_A20VideoType_Object = MibTableColumn
a20VideoType = _A20VideoType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 2),
    _A20VideoType_Type()
)
a20VideoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20VideoType.setStatus("mandatory")
_A20CurrentVideoMode_Type = DmiInteger
_A20CurrentVideoMode_Object = MibTableColumn
a20CurrentVideoMode = _A20CurrentVideoMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 3),
    _A20CurrentVideoMode_Type()
)
a20CurrentVideoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20CurrentVideoMode.setStatus("mandatory")
_A20MinimumRefreshRate_Type = DmiInteger
_A20MinimumRefreshRate_Object = MibTableColumn
a20MinimumRefreshRate = _A20MinimumRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 4),
    _A20MinimumRefreshRate_Type()
)
a20MinimumRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20MinimumRefreshRate.setStatus("mandatory")
_A20MaximumRefreshRate_Type = DmiInteger
_A20MaximumRefreshRate_Object = MibTableColumn
a20MaximumRefreshRate = _A20MaximumRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 5),
    _A20MaximumRefreshRate_Type()
)
a20MaximumRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20MaximumRefreshRate.setStatus("mandatory")


class _A20VideoMemoryType_Type(Integer32):
    """Custom type a20VideoMemoryType based on Integer32"""
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
        *(("vDram", 4),
          ("vOther", 1),
          ("vSram", 5),
          ("vUnknown", 2),
          ("vVram", 3))
    )


_A20VideoMemoryType_Type.__name__ = "Integer32"
_A20VideoMemoryType_Object = MibTableColumn
a20VideoMemoryType = _A20VideoMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 6),
    _A20VideoMemoryType_Type()
)
a20VideoMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20VideoMemoryType.setStatus("mandatory")
_A20VideoRamMemorySize_Type = DmiInteger
_A20VideoRamMemorySize_Object = MibTableColumn
a20VideoRamMemorySize = _A20VideoRamMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 7),
    _A20VideoRamMemorySize_Type()
)
a20VideoRamMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20VideoRamMemorySize.setStatus("mandatory")


class _A20ScanMode_Type(Integer32):
    """Custom type a20ScanMode based on Integer32"""
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
        *(("vInterlaced", 3),
          ("vNonInterlaced", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A20ScanMode_Type.__name__ = "Integer32"
_A20ScanMode_Object = MibTableColumn
a20ScanMode = _A20ScanMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 8),
    _A20ScanMode_Type()
)
a20ScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20ScanMode.setStatus("mandatory")


class _A20VideoPhysicalLocation_Type(Integer32):
    """Custom type a20VideoPhysicalLocation based on Integer32"""
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
        *(("vAddOnCard", 4),
          ("vIntegrated", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A20VideoPhysicalLocation_Type.__name__ = "Integer32"
_A20VideoPhysicalLocation_Object = MibTableColumn
a20VideoPhysicalLocation = _A20VideoPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 9),
    _A20VideoPhysicalLocation_Type()
)
a20VideoPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20VideoPhysicalLocation.setStatus("mandatory")
_A20CurrentVerticalResolution_Type = DmiInteger
_A20CurrentVerticalResolution_Object = MibTableColumn
a20CurrentVerticalResolution = _A20CurrentVerticalResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 10),
    _A20CurrentVerticalResolution_Type()
)
a20CurrentVerticalResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20CurrentVerticalResolution.setStatus("mandatory")
_A20CurrentHorizontalResolution_Type = DmiInteger
_A20CurrentHorizontalResolution_Object = MibTableColumn
a20CurrentHorizontalResolution = _A20CurrentHorizontalResolution_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 11),
    _A20CurrentHorizontalResolution_Type()
)
a20CurrentHorizontalResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20CurrentHorizontalResolution.setStatus("mandatory")
_A20CurrentNumberOfBitsPerPixel_Type = DmiInteger
_A20CurrentNumberOfBitsPerPixel_Object = MibTableColumn
a20CurrentNumberOfBitsPerPixel = _A20CurrentNumberOfBitsPerPixel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 12),
    _A20CurrentNumberOfBitsPerPixel_Type()
)
a20CurrentNumberOfBitsPerPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20CurrentNumberOfBitsPerPixel.setStatus("mandatory")
_A20CurrentNumberOfRows_Type = DmiInteger
_A20CurrentNumberOfRows_Object = MibTableColumn
a20CurrentNumberOfRows = _A20CurrentNumberOfRows_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 13),
    _A20CurrentNumberOfRows_Type()
)
a20CurrentNumberOfRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20CurrentNumberOfRows.setStatus("mandatory")
_A20CurrentNumberOfColumns_Type = DmiInteger
_A20CurrentNumberOfColumns_Object = MibTableColumn
a20CurrentNumberOfColumns = _A20CurrentNumberOfColumns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 14),
    _A20CurrentNumberOfColumns_Type()
)
a20CurrentNumberOfColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20CurrentNumberOfColumns.setStatus("mandatory")
_A20CurrentRefreshRate_Type = DmiInteger
_A20CurrentRefreshRate_Object = MibTableColumn
a20CurrentRefreshRate = _A20CurrentRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 15),
    _A20CurrentRefreshRate_Type()
)
a20CurrentRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20CurrentRefreshRate.setStatus("mandatory")
_A20FruGroupIndex_Type = DmiInteger
_A20FruGroupIndex_Object = MibTableColumn
a20FruGroupIndex = _A20FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 16),
    _A20FruGroupIndex_Type()
)
a20FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20FruGroupIndex.setStatus("mandatory")
_A20OperationalGroupIndex_Type = DmiInteger
_A20OperationalGroupIndex_Object = MibTableColumn
a20OperationalGroupIndex = _A20OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 20, 1, 17),
    _A20OperationalGroupIndex_Type()
)
a20OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a20OperationalGroupIndex.setStatus("mandatory")
_TVideoBios_Object = MibTable
tVideoBios = _TVideoBios_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 21)
)
if mibBuilder.loadTexts:
    tVideoBios.setStatus("mandatory")
_EVideoBios_Object = MibTableRow
eVideoBios = _EVideoBios_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 21, 1)
)
eVideoBios.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a21VideoBiosIndex"),
)
if mibBuilder.loadTexts:
    eVideoBios.setStatus("mandatory")
_A21VideoBiosIndex_Type = DmiInteger
_A21VideoBiosIndex_Object = MibTableColumn
a21VideoBiosIndex = _A21VideoBiosIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 21, 1, 1),
    _A21VideoBiosIndex_Type()
)
a21VideoBiosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21VideoBiosIndex.setStatus("mandatory")
_A21VideoBiosManufacturer_Type = DmiDisplaystring
_A21VideoBiosManufacturer_Object = MibTableColumn
a21VideoBiosManufacturer = _A21VideoBiosManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 21, 1, 2),
    _A21VideoBiosManufacturer_Type()
)
a21VideoBiosManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21VideoBiosManufacturer.setStatus("mandatory")
_A21VideoBiosVersion_Type = DmiDisplaystring
_A21VideoBiosVersion_Object = MibTableColumn
a21VideoBiosVersion = _A21VideoBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 21, 1, 3),
    _A21VideoBiosVersion_Type()
)
a21VideoBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21VideoBiosVersion.setStatus("mandatory")
_A21VideoBiosReleaseDate_Type = DmiDate
_A21VideoBiosReleaseDate_Object = MibTableColumn
a21VideoBiosReleaseDate = _A21VideoBiosReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 21, 1, 4),
    _A21VideoBiosReleaseDate_Type()
)
a21VideoBiosReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21VideoBiosReleaseDate.setStatus("mandatory")


class _A21VideoBiosShadowingState_Type(Integer32):
    """Custom type a21VideoBiosShadowingState based on Integer32"""
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


_A21VideoBiosShadowingState_Type.__name__ = "Integer32"
_A21VideoBiosShadowingState_Object = MibTableColumn
a21VideoBiosShadowingState = _A21VideoBiosShadowingState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 21, 1, 5),
    _A21VideoBiosShadowingState_Type()
)
a21VideoBiosShadowingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a21VideoBiosShadowingState.setStatus("mandatory")
_TVideoBiosCharacteristic_Object = MibTable
tVideoBiosCharacteristic = _TVideoBiosCharacteristic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 22)
)
if mibBuilder.loadTexts:
    tVideoBiosCharacteristic.setStatus("mandatory")
_EVideoBiosCharacteristic_Object = MibTableRow
eVideoBiosCharacteristic = _EVideoBiosCharacteristic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 22, 1)
)
eVideoBiosCharacteristic.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a22VideoBiosCharacteristicsIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a22VideoBiosNumber"),
)
if mibBuilder.loadTexts:
    eVideoBiosCharacteristic.setStatus("mandatory")
_A22VideoBiosCharacteristicsIndex_Type = DmiInteger
_A22VideoBiosCharacteristicsIndex_Object = MibTableColumn
a22VideoBiosCharacteristicsIndex = _A22VideoBiosCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 22, 1, 1),
    _A22VideoBiosCharacteristicsIndex_Type()
)
a22VideoBiosCharacteristicsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22VideoBiosCharacteristicsIndex.setStatus("mandatory")
_A22VideoBiosNumber_Type = DmiInteger
_A22VideoBiosNumber_Object = MibTableColumn
a22VideoBiosNumber = _A22VideoBiosNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 22, 1, 2),
    _A22VideoBiosNumber_Type()
)
a22VideoBiosNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22VideoBiosNumber.setStatus("mandatory")


class _A22VideoBiosCharacteristics_Type(Integer32):
    """Custom type a22VideoBiosCharacteristics based on Integer32"""
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
        *(("vOther", 1),
          ("vStandardVideoBios", 4),
          ("vUnknown", 2),
          ("vUnsupported", 3),
          ("vVesaBiosExtensionsSupported", 5),
          ("vVesaDisplayDataChannelSupported", 7),
          ("vVesaPowerManagementSupported", 6),
          ("vVideoBios-shadowing-allowed", 8),
          ("vVideoBiosUpgradable", 9))
    )


_A22VideoBiosCharacteristics_Type.__name__ = "Integer32"
_A22VideoBiosCharacteristics_Object = MibTableColumn
a22VideoBiosCharacteristics = _A22VideoBiosCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 22, 1, 3),
    _A22VideoBiosCharacteristics_Type()
)
a22VideoBiosCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22VideoBiosCharacteristics.setStatus("mandatory")
_A22VideoBiosCharacteristicsDescription_Type = DmiDisplaystring
_A22VideoBiosCharacteristicsDescription_Object = MibTableColumn
a22VideoBiosCharacteristicsDescription = _A22VideoBiosCharacteristicsDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 22, 1, 4),
    _A22VideoBiosCharacteristicsDescription_Type()
)
a22VideoBiosCharacteristicsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a22VideoBiosCharacteristicsDescription.setStatus("mandatory")
_TDiskDrives_Object = MibTable
tDiskDrives = _TDiskDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23)
)
if mibBuilder.loadTexts:
    tDiskDrives.setStatus("mandatory")
_EDiskDrives_Object = MibTableRow
eDiskDrives = _EDiskDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1)
)
eDiskDrives.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a23StorageType"),
    (0, "PCSYSTEMSMIF-MIB", "a23DiskIndex"),
)
if mibBuilder.loadTexts:
    eDiskDrives.setStatus("mandatory")


class _A23StorageType_Type(Integer32):
    """Custom type a23StorageType based on Integer32"""
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
        *(("vBernoulli", 10),
          ("vCompact-disk", 8),
          ("vFlash-disk", 9),
          ("vFloppy-disk", 4),
          ("vHard-disk", 3),
          ("vOptical-rom", 5),
          ("vOptical-rw", 7),
          ("vOptical-worm", 6),
          ("vOpticalFloppyDisk", 11),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A23StorageType_Type.__name__ = "Integer32"
_A23StorageType_Object = MibTableColumn
a23StorageType = _A23StorageType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 1),
    _A23StorageType_Type()
)
a23StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23StorageType.setStatus("mandatory")
_A23DiskIndex_Type = DmiInteger
_A23DiskIndex_Object = MibTableColumn
a23DiskIndex = _A23DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 2),
    _A23DiskIndex_Type()
)
a23DiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23DiskIndex.setStatus("mandatory")


class _A23StorageInterfaceType_Type(Integer32):
    """Custom type a23StorageInterfaceType based on Integer32"""
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
        *(("vCmd", 6),
          ("vDssi", 9),
          ("vEnhancedAtaide", 15),
          ("vEsdi", 4),
          ("vFloppy-disk-interface", 13),
          ("vHippi", 11),
          ("vIde", 5),
          ("vIpi", 7),
          ("vOther", 1),
          ("vParallel-port", 10),
          ("vPcmcia", 14),
          ("vQic2", 12),
          ("vScsi", 3),
          ("vSt506", 8),
          ("vUnknown", 2))
    )


_A23StorageInterfaceType_Type.__name__ = "Integer32"
_A23StorageInterfaceType_Object = MibTableColumn
a23StorageInterfaceType = _A23StorageInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 3),
    _A23StorageInterfaceType_Type()
)
a23StorageInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23StorageInterfaceType.setStatus("mandatory")
_A23InterfaceDescription_Type = DmiDisplaystring
_A23InterfaceDescription_Object = MibTableColumn
a23InterfaceDescription = _A23InterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 4),
    _A23InterfaceDescription_Type()
)
a23InterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23InterfaceDescription.setStatus("mandatory")


class _A23MediaLoaded_Type(Integer32):
    """Custom type a23MediaLoaded based on Integer32"""
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


_A23MediaLoaded_Type.__name__ = "Integer32"
_A23MediaLoaded_Object = MibTableColumn
a23MediaLoaded = _A23MediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 5),
    _A23MediaLoaded_Type()
)
a23MediaLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23MediaLoaded.setStatus("mandatory")


class _A23RemovableMedia_Type(Integer32):
    """Custom type a23RemovableMedia based on Integer32"""
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


_A23RemovableMedia_Type.__name__ = "Integer32"
_A23RemovableMedia_Object = MibTableColumn
a23RemovableMedia = _A23RemovableMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 6),
    _A23RemovableMedia_Type()
)
a23RemovableMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23RemovableMedia.setStatus("mandatory")
_A23DeviceId_Type = DmiInteger
_A23DeviceId_Object = MibTableColumn
a23DeviceId = _A23DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 7),
    _A23DeviceId_Type()
)
a23DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23DeviceId.setStatus("mandatory")
_A23LogicalUnitNumber_Type = DmiInteger
_A23LogicalUnitNumber_Object = MibTableColumn
a23LogicalUnitNumber = _A23LogicalUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 8),
    _A23LogicalUnitNumber_Type()
)
a23LogicalUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23LogicalUnitNumber.setStatus("mandatory")
_A23NumberOfPhysicalCylinders_Type = DmiInteger
_A23NumberOfPhysicalCylinders_Object = MibTableColumn
a23NumberOfPhysicalCylinders = _A23NumberOfPhysicalCylinders_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 9),
    _A23NumberOfPhysicalCylinders_Type()
)
a23NumberOfPhysicalCylinders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23NumberOfPhysicalCylinders.setStatus("mandatory")
_A23NumberOfPhysicalSectorsPerTrack_Type = DmiInteger
_A23NumberOfPhysicalSectorsPerTrack_Object = MibTableColumn
a23NumberOfPhysicalSectorsPerTrack = _A23NumberOfPhysicalSectorsPerTrack_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 10),
    _A23NumberOfPhysicalSectorsPerTrack_Type()
)
a23NumberOfPhysicalSectorsPerTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23NumberOfPhysicalSectorsPerTrack.setStatus("mandatory")
_A23NumberOfPhysicalHeads_Type = DmiInteger
_A23NumberOfPhysicalHeads_Object = MibTableColumn
a23NumberOfPhysicalHeads = _A23NumberOfPhysicalHeads_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 11),
    _A23NumberOfPhysicalHeads_Type()
)
a23NumberOfPhysicalHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23NumberOfPhysicalHeads.setStatus("mandatory")
_A23SectorSize_Type = DmiInteger
_A23SectorSize_Object = MibTableColumn
a23SectorSize = _A23SectorSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 12),
    _A23SectorSize_Type()
)
a23SectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23SectorSize.setStatus("mandatory")
_A23TotalPhysicalSize_Type = DmiInteger
_A23TotalPhysicalSize_Object = MibTableColumn
a23TotalPhysicalSize = _A23TotalPhysicalSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 13),
    _A23TotalPhysicalSize_Type()
)
a23TotalPhysicalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23TotalPhysicalSize.setStatus("mandatory")
_A23Partitions_Type = DmiInteger
_A23Partitions_Object = MibTableColumn
a23Partitions = _A23Partitions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 14),
    _A23Partitions_Type()
)
a23Partitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23Partitions.setStatus("mandatory")
_A23FruGroupIndex_Type = DmiInteger
_A23FruGroupIndex_Object = MibTableColumn
a23FruGroupIndex = _A23FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 23, 1, 15),
    _A23FruGroupIndex_Type()
)
a23FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a23FruGroupIndex.setStatus("mandatory")
_TDiskMappingTable_Object = MibTable
tDiskMappingTable = _TDiskMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 24)
)
if mibBuilder.loadTexts:
    tDiskMappingTable.setStatus("mandatory")
_EDiskMappingTable_Object = MibTableRow
eDiskMappingTable = _EDiskMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 24, 1)
)
eDiskMappingTable.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a24StorageType"),
    (0, "PCSYSTEMSMIF-MIB", "a24DiskIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a24PartitionIndex"),
)
if mibBuilder.loadTexts:
    eDiskMappingTable.setStatus("mandatory")


class _A24StorageType_Type(Integer32):
    """Custom type a24StorageType based on Integer32"""
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
        *(("vBernoulli", 10),
          ("vCompact-disk", 8),
          ("vFlash-disk", 9),
          ("vFloppy-disk", 4),
          ("vHard-disk", 3),
          ("vOptical-rom", 5),
          ("vOptical-rw", 7),
          ("vOptical-worm", 6),
          ("vOpticalFloppyDisk", 11),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A24StorageType_Type.__name__ = "Integer32"
_A24StorageType_Object = MibTableColumn
a24StorageType = _A24StorageType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 24, 1, 1),
    _A24StorageType_Type()
)
a24StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24StorageType.setStatus("mandatory")
_A24DiskIndex_Type = DmiInteger
_A24DiskIndex_Object = MibTableColumn
a24DiskIndex = _A24DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 24, 1, 2),
    _A24DiskIndex_Type()
)
a24DiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24DiskIndex.setStatus("mandatory")
_A24PartitionIndex_Type = DmiInteger
_A24PartitionIndex_Object = MibTableColumn
a24PartitionIndex = _A24PartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 24, 1, 3),
    _A24PartitionIndex_Type()
)
a24PartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a24PartitionIndex.setStatus("mandatory")
_TPartition_Object = MibTable
tPartition = _TPartition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25)
)
if mibBuilder.loadTexts:
    tPartition.setStatus("mandatory")
_EPartition_Object = MibTableRow
ePartition = _EPartition_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1)
)
ePartition.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a25PartitionIndex"),
)
if mibBuilder.loadTexts:
    ePartition.setStatus("mandatory")
_A25PartitionIndex_Type = DmiInteger
_A25PartitionIndex_Object = MibTableColumn
a25PartitionIndex = _A25PartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 1),
    _A25PartitionIndex_Type()
)
a25PartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25PartitionIndex.setStatus("mandatory")
_A25PartitionName_Type = DmiDisplaystring
_A25PartitionName_Object = MibTableColumn
a25PartitionName = _A25PartitionName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 2),
    _A25PartitionName_Type()
)
a25PartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25PartitionName.setStatus("mandatory")
_A25PartitionSize_Type = DmiInteger64
_A25PartitionSize_Object = MibTableColumn
a25PartitionSize = _A25PartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 3),
    _A25PartitionSize_Type()
)
a25PartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25PartitionSize.setStatus("mandatory")
_A25FreeSpace_Type = DmiInteger64
_A25FreeSpace_Object = MibTableColumn
a25FreeSpace = _A25FreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 4),
    _A25FreeSpace_Type()
)
a25FreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25FreeSpace.setStatus("mandatory")
_A25PartitionLabel_Type = DmiOctetstring
_A25PartitionLabel_Object = MibTableColumn
a25PartitionLabel = _A25PartitionLabel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 5),
    _A25PartitionLabel_Type()
)
a25PartitionLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25PartitionLabel.setStatus("mandatory")


class _A25FileSystem_Type(Integer32):
    """Custom type a25FileSystem based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("vFat", 3),
          ("vFfs", 14),
          ("vHfs", 8),
          ("vHpfs", 4),
          ("vMfs", 7),
          ("vNetware286", 15),
          ("vNetware386", 16),
          ("vNtfs", 5),
          ("vOfs", 6),
          ("vOther", 1),
          ("vS5", 11),
          ("vS52k", 12),
          ("vSfs", 10),
          ("vUfs", 13),
          ("vUnknown", 2),
          ("vVxfs", 9))
    )


_A25FileSystem_Type.__name__ = "Integer32"
_A25FileSystem_Object = MibTableColumn
a25FileSystem = _A25FileSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 6),
    _A25FileSystem_Type()
)
a25FileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25FileSystem.setStatus("mandatory")


class _A25Compressed_Type(Integer32):
    """Custom type a25Compressed based on Integer32"""
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


_A25Compressed_Type.__name__ = "Integer32"
_A25Compressed_Object = MibTableColumn
a25Compressed = _A25Compressed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 7),
    _A25Compressed_Type()
)
a25Compressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25Compressed.setStatus("mandatory")


class _A25Encrypted_Type(Integer32):
    """Custom type a25Encrypted based on Integer32"""
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


_A25Encrypted_Type.__name__ = "Integer32"
_A25Encrypted_Object = MibTableColumn
a25Encrypted = _A25Encrypted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 8),
    _A25Encrypted_Type()
)
a25Encrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25Encrypted.setStatus("mandatory")
_A25NumberOfDisksOccupied_Type = DmiInteger
_A25NumberOfDisksOccupied_Object = MibTableColumn
a25NumberOfDisksOccupied = _A25NumberOfDisksOccupied_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 25, 1, 9),
    _A25NumberOfDisksOccupied_Type()
)
a25NumberOfDisksOccupied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a25NumberOfDisksOccupied.setStatus("mandatory")
_TDiskController_Object = MibTable
tDiskController = _TDiskController_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 26)
)
if mibBuilder.loadTexts:
    tDiskController.setStatus("mandatory")
_EDiskController_Object = MibTableRow
eDiskController = _EDiskController_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 26, 1)
)
eDiskController.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a26DiskControllerIndex"),
)
if mibBuilder.loadTexts:
    eDiskController.setStatus("mandatory")
_A26DiskControllerIndex_Type = DmiInteger
_A26DiskControllerIndex_Object = MibTableColumn
a26DiskControllerIndex = _A26DiskControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 26, 1, 1),
    _A26DiskControllerIndex_Type()
)
a26DiskControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26DiskControllerIndex.setStatus("mandatory")
_A26FruGroupIndex_Type = DmiInteger
_A26FruGroupIndex_Object = MibTableColumn
a26FruGroupIndex = _A26FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 26, 1, 2),
    _A26FruGroupIndex_Type()
)
a26FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26FruGroupIndex.setStatus("mandatory")
_A26OperationalGroupIndex_Type = DmiInteger
_A26OperationalGroupIndex_Object = MibTableColumn
a26OperationalGroupIndex = _A26OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 26, 1, 3),
    _A26OperationalGroupIndex_Type()
)
a26OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a26OperationalGroupIndex.setStatus("mandatory")
_TLogicalDrives_Object = MibTable
tLogicalDrives = _TLogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27)
)
if mibBuilder.loadTexts:
    tLogicalDrives.setStatus("mandatory")
_ELogicalDrives_Object = MibTableRow
eLogicalDrives = _ELogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27, 1)
)
eLogicalDrives.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a27LogicalDriveIndex"),
)
if mibBuilder.loadTexts:
    eLogicalDrives.setStatus("mandatory")
_A27LogicalDriveIndex_Type = DmiInteger
_A27LogicalDriveIndex_Object = MibTableColumn
a27LogicalDriveIndex = _A27LogicalDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27, 1, 1),
    _A27LogicalDriveIndex_Type()
)
a27LogicalDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27LogicalDriveIndex.setStatus("mandatory")
_A27LogicalDriveName_Type = DmiDisplaystring
_A27LogicalDriveName_Object = MibTableColumn
a27LogicalDriveName = _A27LogicalDriveName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27, 1, 2),
    _A27LogicalDriveName_Type()
)
a27LogicalDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27LogicalDriveName.setStatus("mandatory")


class _A27LogicalDriveType_Type(Integer32):
    """Custom type a27LogicalDriveType based on Integer32"""
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
        *(("vCdrom", 6),
          ("vDriveArray", 9),
          ("vFixedDrive", 3),
          ("vFloppyDrive", 7),
          ("vOther", 1),
          ("vRamDrive", 8),
          ("vRemoteDrive", 5),
          ("vRemovableDrive", 4),
          ("vUnknown", 2))
    )


_A27LogicalDriveType_Type.__name__ = "Integer32"
_A27LogicalDriveType_Object = MibTableColumn
a27LogicalDriveType = _A27LogicalDriveType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27, 1, 3),
    _A27LogicalDriveType_Type()
)
a27LogicalDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27LogicalDriveType.setStatus("mandatory")
_A27LogicalDriveSize_Type = DmiInteger
_A27LogicalDriveSize_Object = MibTableColumn
a27LogicalDriveSize = _A27LogicalDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27, 1, 4),
    _A27LogicalDriveSize_Type()
)
a27LogicalDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27LogicalDriveSize.setStatus("mandatory")
_A27FreeLogicalDriveSize_Type = DmiInteger
_A27FreeLogicalDriveSize_Object = MibTableColumn
a27FreeLogicalDriveSize = _A27FreeLogicalDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27, 1, 5),
    _A27FreeLogicalDriveSize_Type()
)
a27FreeLogicalDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27FreeLogicalDriveSize.setStatus("mandatory")
_A27LogicalDrivePath_Type = DmiDisplaystring
_A27LogicalDrivePath_Object = MibTableColumn
a27LogicalDrivePath = _A27LogicalDrivePath_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 27, 1, 6),
    _A27LogicalDrivePath_Type()
)
a27LogicalDrivePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a27LogicalDrivePath.setStatus("mandatory")
_TMouse_Object = MibTable
tMouse = _TMouse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28)
)
if mibBuilder.loadTexts:
    tMouse.setStatus("mandatory")
_EMouse_Object = MibTableRow
eMouse = _EMouse_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1)
)
eMouse.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMouse.setStatus("mandatory")


class _A28MouseInterface_Type(Integer32):
    """Custom type a28MouseInterface based on Integer32"""
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
        *(("vBusMouse", 7),
          ("vHp-hil", 6),
          ("vInfrared", 5),
          ("vOther", 1),
          ("vPs2", 4),
          ("vSerial", 3),
          ("vUnknown", 2))
    )


_A28MouseInterface_Type.__name__ = "Integer32"
_A28MouseInterface_Object = MibTableColumn
a28MouseInterface = _A28MouseInterface_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 1),
    _A28MouseInterface_Type()
)
a28MouseInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28MouseInterface.setStatus("mandatory")
_A28MouseIrq_Type = DmiInteger
_A28MouseIrq_Object = MibTableColumn
a28MouseIrq = _A28MouseIrq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 2),
    _A28MouseIrq_Type()
)
a28MouseIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28MouseIrq.setStatus("mandatory")
_A28MouseButtons_Type = DmiInteger
_A28MouseButtons_Object = MibTableColumn
a28MouseButtons = _A28MouseButtons_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 3),
    _A28MouseButtons_Type()
)
a28MouseButtons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28MouseButtons.setStatus("mandatory")
_A28MousePortName_Type = DmiDisplaystring
_A28MousePortName_Object = MibTableColumn
a28MousePortName = _A28MousePortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 4),
    _A28MousePortName_Type()
)
a28MousePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28MousePortName.setStatus("mandatory")
_A28MouseDriverName_Type = DmiDisplaystring
_A28MouseDriverName_Object = MibTableColumn
a28MouseDriverName = _A28MouseDriverName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 5),
    _A28MouseDriverName_Type()
)
a28MouseDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28MouseDriverName.setStatus("mandatory")
_A28MouseDriverVersion_Type = DmiDisplaystring
_A28MouseDriverVersion_Object = MibTableColumn
a28MouseDriverVersion = _A28MouseDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 6),
    _A28MouseDriverVersion_Type()
)
a28MouseDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28MouseDriverVersion.setStatus("mandatory")
_A28FruGroupIndex_Type = DmiInteger
_A28FruGroupIndex_Object = MibTableColumn
a28FruGroupIndex = _A28FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 7),
    _A28FruGroupIndex_Type()
)
a28FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28FruGroupIndex.setStatus("mandatory")
_A28OperationalGroupIndex_Type = DmiInteger
_A28OperationalGroupIndex_Object = MibTableColumn
a28OperationalGroupIndex = _A28OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 28, 1, 8),
    _A28OperationalGroupIndex_Type()
)
a28OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a28OperationalGroupIndex.setStatus("mandatory")
_TKeyboard_Object = MibTable
tKeyboard = _TKeyboard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 29)
)
if mibBuilder.loadTexts:
    tKeyboard.setStatus("mandatory")
_EKeyboard_Object = MibTableRow
eKeyboard = _EKeyboard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 29, 1)
)
eKeyboard.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eKeyboard.setStatus("mandatory")
_A29KeyboardLayout_Type = DmiDisplaystring
_A29KeyboardLayout_Object = MibTableColumn
a29KeyboardLayout = _A29KeyboardLayout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 29, 1, 1),
    _A29KeyboardLayout_Type()
)
a29KeyboardLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a29KeyboardLayout.setStatus("mandatory")
_A29KeyboardType_Type = DmiDisplaystring
_A29KeyboardType_Object = MibTableColumn
a29KeyboardType = _A29KeyboardType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 29, 1, 2),
    _A29KeyboardType_Type()
)
a29KeyboardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a29KeyboardType.setStatus("mandatory")


class _A29KeyboardConnectorType_Type(Integer32):
    """Custom type a29KeyboardConnectorType based on Integer32"""
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
        *(("vAccessbus", 9),
          ("vDb-9", 8),
          ("vHp-hil", 7),
          ("vInfrared", 6),
          ("vMicro-din", 4),
          ("vMini-din", 3),
          ("vOther", 1),
          ("vPs2", 5),
          ("vUnknown", 2))
    )


_A29KeyboardConnectorType_Type.__name__ = "Integer32"
_A29KeyboardConnectorType_Object = MibTableColumn
a29KeyboardConnectorType = _A29KeyboardConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 29, 1, 3),
    _A29KeyboardConnectorType_Type()
)
a29KeyboardConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a29KeyboardConnectorType.setStatus("mandatory")
_A29FruGroupIndex_Type = DmiInteger
_A29FruGroupIndex_Object = MibTableColumn
a29FruGroupIndex = _A29FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 29, 1, 4),
    _A29FruGroupIndex_Type()
)
a29FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a29FruGroupIndex.setStatus("mandatory")
_A29OperationalGroupIndex_Type = DmiInteger
_A29OperationalGroupIndex_Object = MibTableColumn
a29OperationalGroupIndex = _A29OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 29, 1, 5),
    _A29OperationalGroupIndex_Type()
)
a29OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a29OperationalGroupIndex.setStatus("mandatory")
_TFieldReplacableUnit_Object = MibTable
tFieldReplacableUnit = _TFieldReplacableUnit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30)
)
if mibBuilder.loadTexts:
    tFieldReplacableUnit.setStatus("mandatory")
_EFieldReplacableUnit_Object = MibTableRow
eFieldReplacableUnit = _EFieldReplacableUnit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1)
)
eFieldReplacableUnit.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a30FruIndex"),
)
if mibBuilder.loadTexts:
    eFieldReplacableUnit.setStatus("mandatory")
_A30FruIndex_Type = DmiInteger
_A30FruIndex_Object = MibTableColumn
a30FruIndex = _A30FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 1),
    _A30FruIndex_Type()
)
a30FruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30FruIndex.setStatus("mandatory")
_A30DeviceGroupIndex_Type = DmiInteger
_A30DeviceGroupIndex_Object = MibTableColumn
a30DeviceGroupIndex = _A30DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 2),
    _A30DeviceGroupIndex_Type()
)
a30DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30DeviceGroupIndex.setStatus("mandatory")
_A30Description_Type = DmiDisplaystring
_A30Description_Object = MibTableColumn
a30Description = _A30Description_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 3),
    _A30Description_Type()
)
a30Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a30Description.setStatus("mandatory")
_A30Manufacturer_Type = DmiDisplaystring
_A30Manufacturer_Object = MibTableColumn
a30Manufacturer = _A30Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 4),
    _A30Manufacturer_Type()
)
a30Manufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a30Manufacturer.setStatus("mandatory")
_A30Model_Type = DmiDisplaystring
_A30Model_Object = MibTableColumn
a30Model = _A30Model_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 5),
    _A30Model_Type()
)
a30Model.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a30Model.setStatus("mandatory")
_A30PartNumber_Type = DmiDisplaystring
_A30PartNumber_Object = MibTableColumn
a30PartNumber = _A30PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 6),
    _A30PartNumber_Type()
)
a30PartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a30PartNumber.setStatus("mandatory")
_A30FruSerialNumber_Type = DmiDisplaystring
_A30FruSerialNumber_Object = MibTableColumn
a30FruSerialNumber = _A30FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 7),
    _A30FruSerialNumber_Type()
)
a30FruSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a30FruSerialNumber.setStatus("mandatory")
_A30RevisionLevel_Type = DmiDisplaystring
_A30RevisionLevel_Object = MibTableColumn
a30RevisionLevel = _A30RevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 30, 1, 8),
    _A30RevisionLevel_Type()
)
a30RevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a30RevisionLevel.setStatus("mandatory")
_TOperationalState_Object = MibTable
tOperationalState = _TOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31)
)
if mibBuilder.loadTexts:
    tOperationalState.setStatus("mandatory")
_EOperationalState_Object = MibTableRow
eOperationalState = _EOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1)
)
eOperationalState.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a31OperationalStateInstanceIndex"),
)
if mibBuilder.loadTexts:
    eOperationalState.setStatus("mandatory")
_A31OperationalStateInstanceIndex_Type = DmiInteger
_A31OperationalStateInstanceIndex_Object = MibTableColumn
a31OperationalStateInstanceIndex = _A31OperationalStateInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 1),
    _A31OperationalStateInstanceIndex_Type()
)
a31OperationalStateInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31OperationalStateInstanceIndex.setStatus("mandatory")
_A31DeviceGroupIndex_Type = DmiInteger
_A31DeviceGroupIndex_Object = MibTableColumn
a31DeviceGroupIndex = _A31DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 2),
    _A31DeviceGroupIndex_Type()
)
a31DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31DeviceGroupIndex.setStatus("mandatory")


class _A31OperationalStatus_Type(Integer32):
    """Custom type a31OperationalStatus based on Integer32"""
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


_A31OperationalStatus_Type.__name__ = "Integer32"
_A31OperationalStatus_Object = MibTableColumn
a31OperationalStatus = _A31OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 3),
    _A31OperationalStatus_Type()
)
a31OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31OperationalStatus.setStatus("mandatory")


class _A31UsageState_Type(Integer32):
    """Custom type a31UsageState based on Integer32"""
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
          ("vNotApplicable1", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A31UsageState_Type.__name__ = "Integer32"
_A31UsageState_Object = MibTableColumn
a31UsageState = _A31UsageState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 4),
    _A31UsageState_Type()
)
a31UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31UsageState.setStatus("mandatory")


class _A31AvailabilityStatus_Type(Integer32):
    """Custom type a31AvailabilityStatus based on Integer32"""
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


_A31AvailabilityStatus_Type.__name__ = "Integer32"
_A31AvailabilityStatus_Object = MibTableColumn
a31AvailabilityStatus = _A31AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 5),
    _A31AvailabilityStatus_Type()
)
a31AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31AvailabilityStatus.setStatus("mandatory")


class _A31AdministrativeState_Type(Integer32):
    """Custom type a31AdministrativeState based on Integer32"""
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


_A31AdministrativeState_Type.__name__ = "Integer32"
_A31AdministrativeState_Object = MibTableColumn
a31AdministrativeState = _A31AdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 6),
    _A31AdministrativeState_Type()
)
a31AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31AdministrativeState.setStatus("mandatory")
_A31FatalErrorCount_Type = DmiCounter
_A31FatalErrorCount_Object = MibTableColumn
a31FatalErrorCount = _A31FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 7),
    _A31FatalErrorCount_Type()
)
a31FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31FatalErrorCount.setStatus("mandatory")
_A31MajorErrorCount_Type = DmiCounter
_A31MajorErrorCount_Object = MibTableColumn
a31MajorErrorCount = _A31MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 8),
    _A31MajorErrorCount_Type()
)
a31MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31MajorErrorCount.setStatus("mandatory")
_A31WarningErrorCount_Type = DmiCounter
_A31WarningErrorCount_Object = MibTableColumn
a31WarningErrorCount = _A31WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 31, 1, 9),
    _A31WarningErrorCount_Type()
)
a31WarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31WarningErrorCount.setStatus("mandatory")
_TSystemResourcesDescription_Object = MibTable
tSystemResourcesDescription = _TSystemResourcesDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 32)
)
if mibBuilder.loadTexts:
    tSystemResourcesDescription.setStatus("mandatory")
_ESystemResourcesDescription_Object = MibTableRow
eSystemResourcesDescription = _ESystemResourcesDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 32, 1)
)
eSystemResourcesDescription.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a32DeviceCount"),
)
if mibBuilder.loadTexts:
    eSystemResourcesDescription.setStatus("mandatory")
_A32DeviceCount_Type = DmiInteger
_A32DeviceCount_Object = MibTableColumn
a32DeviceCount = _A32DeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 32, 1, 1),
    _A32DeviceCount_Type()
)
a32DeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a32DeviceCount.setStatus("mandatory")
_A32SystemResourceCount_Type = DmiInteger
_A32SystemResourceCount_Object = MibTableColumn
a32SystemResourceCount = _A32SystemResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 32, 1, 2),
    _A32SystemResourceCount_Type()
)
a32SystemResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a32SystemResourceCount.setStatus("mandatory")
_TSystemResources_Object = MibTable
tSystemResources = _TSystemResources_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33)
)
if mibBuilder.loadTexts:
    tSystemResources.setStatus("mandatory")
_ESystemResources_Object = MibTableRow
eSystemResources = _ESystemResources_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33, 1)
)
eSystemResources.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a33ResourceInstance"),
    (0, "PCSYSTEMSMIF-MIB", "a33ResourceParentGroupIndex"),
)
if mibBuilder.loadTexts:
    eSystemResources.setStatus("mandatory")
_A33ResourceInstance_Type = DmiInteger
_A33ResourceInstance_Object = MibTableColumn
a33ResourceInstance = _A33ResourceInstance_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33, 1, 1),
    _A33ResourceInstance_Type()
)
a33ResourceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a33ResourceInstance.setStatus("mandatory")
_A33ResourceParentGroupIndex_Type = DmiInteger
_A33ResourceParentGroupIndex_Object = MibTableColumn
a33ResourceParentGroupIndex = _A33ResourceParentGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33, 1, 2),
    _A33ResourceParentGroupIndex_Type()
)
a33ResourceParentGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a33ResourceParentGroupIndex.setStatus("mandatory")


class _A33ResourceType_Type(Integer32):
    """Custom type a33ResourceType based on Integer32"""
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
        *(("vDma", 6),
          ("vIoPort", 4),
          ("vIrq", 5),
          ("vMemoryRange", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A33ResourceType_Type.__name__ = "Integer32"
_A33ResourceType_Object = MibTableColumn
a33ResourceType = _A33ResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33, 1, 3),
    _A33ResourceType_Type()
)
a33ResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a33ResourceType.setStatus("mandatory")
_A33ResourceBase_Type = DmiInteger
_A33ResourceBase_Object = MibTableColumn
a33ResourceBase = _A33ResourceBase_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33, 1, 4),
    _A33ResourceBase_Type()
)
a33ResourceBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a33ResourceBase.setStatus("mandatory")
_A33ResourceSize_Type = DmiInteger
_A33ResourceSize_Object = MibTableColumn
a33ResourceSize = _A33ResourceSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33, 1, 5),
    _A33ResourceSize_Type()
)
a33ResourceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a33ResourceSize.setStatus("mandatory")
_A33ResourceFlags_Type = DmiInteger
_A33ResourceFlags_Object = MibTableColumn
a33ResourceFlags = _A33ResourceFlags_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 33, 1, 6),
    _A33ResourceFlags_Type()
)
a33ResourceFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a33ResourceFlags.setStatus("mandatory")
_TNetfinityDmiInstall_Object = MibTable
tNetfinityDmiInstall = _TNetfinityDmiInstall_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 34)
)
if mibBuilder.loadTexts:
    tNetfinityDmiInstall.setStatus("mandatory")
_ENetfinityDmiInstall_Object = MibTableRow
eNetfinityDmiInstall = _ENetfinityDmiInstall_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 34, 1)
)
eNetfinityDmiInstall.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eNetfinityDmiInstall.setStatus("mandatory")
_A34ProductName_Type = DmiDisplaystring
_A34ProductName_Object = MibTableColumn
a34ProductName = _A34ProductName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 34, 1, 1),
    _A34ProductName_Type()
)
a34ProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34ProductName.setStatus("mandatory")
_TMicrochannelAdapterInformation_Object = MibTable
tMicrochannelAdapterInformation = _TMicrochannelAdapterInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 35)
)
if mibBuilder.loadTexts:
    tMicrochannelAdapterInformation.setStatus("mandatory")
_EMicrochannelAdapterInformation_Object = MibTableRow
eMicrochannelAdapterInformation = _EMicrochannelAdapterInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 35, 1)
)
eMicrochannelAdapterInformation.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a35AdapterIndex"),
)
if mibBuilder.loadTexts:
    eMicrochannelAdapterInformation.setStatus("mandatory")
_A35AdapterIndex_Type = DmiInteger
_A35AdapterIndex_Object = MibTableColumn
a35AdapterIndex = _A35AdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 35, 1, 1),
    _A35AdapterIndex_Type()
)
a35AdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35AdapterIndex.setStatus("mandatory")
_A35SlotNumber_Type = DmiInteger
_A35SlotNumber_Object = MibTableColumn
a35SlotNumber = _A35SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 35, 1, 2),
    _A35SlotNumber_Type()
)
a35SlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35SlotNumber.setStatus("mandatory")
_A35AdapterId_Type = DmiDisplaystring
_A35AdapterId_Object = MibTableColumn
a35AdapterId = _A35AdapterId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 35, 1, 3),
    _A35AdapterId_Type()
)
a35AdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35AdapterId.setStatus("mandatory")
_A35PosData_Type = DmiDisplaystring
_A35PosData_Object = MibTableColumn
a35PosData = _A35PosData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 35, 1, 4),
    _A35PosData_Type()
)
a35PosData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35PosData.setStatus("mandatory")
_A35AdapterName_Type = DmiDisplaystring
_A35AdapterName_Object = MibTableColumn
a35AdapterName = _A35AdapterName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 35, 1, 5),
    _A35AdapterName_Type()
)
a35AdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35AdapterName.setStatus("mandatory")
_TPciDeviceInformation_Object = MibTable
tPciDeviceInformation = _TPciDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36)
)
if mibBuilder.loadTexts:
    tPciDeviceInformation.setStatus("mandatory")
_EPciDeviceInformation_Object = MibTableRow
ePciDeviceInformation = _EPciDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1)
)
ePciDeviceInformation.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a36DeviceIndex"),
)
if mibBuilder.loadTexts:
    ePciDeviceInformation.setStatus("mandatory")
_A36DeviceIndex_Type = DmiInteger
_A36DeviceIndex_Object = MibTableColumn
a36DeviceIndex = _A36DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 1),
    _A36DeviceIndex_Type()
)
a36DeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DeviceIndex.setStatus("mandatory")
_A36ClassCode_Type = DmiDisplaystring
_A36ClassCode_Object = MibTableColumn
a36ClassCode = _A36ClassCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 2),
    _A36ClassCode_Type()
)
a36ClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36ClassCode.setStatus("mandatory")
_A36PciDeviceName_Type = DmiDisplaystring
_A36PciDeviceName_Object = MibTableColumn
a36PciDeviceName = _A36PciDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 3),
    _A36PciDeviceName_Type()
)
a36PciDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36PciDeviceName.setStatus("mandatory")
_A36VendorId_Type = DmiDisplaystring
_A36VendorId_Object = MibTableColumn
a36VendorId = _A36VendorId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 4),
    _A36VendorId_Type()
)
a36VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36VendorId.setStatus("mandatory")
_A36DeviceId_Type = DmiDisplaystring
_A36DeviceId_Object = MibTableColumn
a36DeviceId = _A36DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 5),
    _A36DeviceId_Type()
)
a36DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DeviceId.setStatus("mandatory")
_A36BusNumber_Type = DmiInteger
_A36BusNumber_Object = MibTableColumn
a36BusNumber = _A36BusNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 6),
    _A36BusNumber_Type()
)
a36BusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36BusNumber.setStatus("mandatory")
_A36DeviceNumber_Type = DmiDisplaystring
_A36DeviceNumber_Object = MibTableColumn
a36DeviceNumber = _A36DeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 7),
    _A36DeviceNumber_Type()
)
a36DeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DeviceNumber.setStatus("mandatory")
_A36RevisionId_Type = DmiDisplaystring
_A36RevisionId_Object = MibTableColumn
a36RevisionId = _A36RevisionId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 36, 1, 8),
    _A36RevisionId_Type()
)
a36RevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36RevisionId.setStatus("mandatory")
_TEisaDeviceInformation_Object = MibTable
tEisaDeviceInformation = _TEisaDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37)
)
if mibBuilder.loadTexts:
    tEisaDeviceInformation.setStatus("mandatory")
_EEisaDeviceInformation_Object = MibTableRow
eEisaDeviceInformation = _EEisaDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1)
)
eEisaDeviceInformation.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a37DeviceIndex"),
)
if mibBuilder.loadTexts:
    eEisaDeviceInformation.setStatus("mandatory")
_A37DeviceIndex_Type = DmiInteger
_A37DeviceIndex_Object = MibTableColumn
a37DeviceIndex = _A37DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 1),
    _A37DeviceIndex_Type()
)
a37DeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37DeviceIndex.setStatus("mandatory")
_A37ProductId_Type = DmiDisplaystring
_A37ProductId_Object = MibTableColumn
a37ProductId = _A37ProductId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 2),
    _A37ProductId_Type()
)
a37ProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37ProductId.setStatus("mandatory")
_A37EisaDeviceName_Type = DmiDisplaystring
_A37EisaDeviceName_Object = MibTableColumn
a37EisaDeviceName = _A37EisaDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 3),
    _A37EisaDeviceName_Type()
)
a37EisaDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37EisaDeviceName.setStatus("mandatory")
_A37Manufacturer_Type = DmiDisplaystring
_A37Manufacturer_Object = MibTableColumn
a37Manufacturer = _A37Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 4),
    _A37Manufacturer_Type()
)
a37Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37Manufacturer.setStatus("mandatory")
_A37SlotLocation_Type = DmiInteger
_A37SlotLocation_Object = MibTableColumn
a37SlotLocation = _A37SlotLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 5),
    _A37SlotLocation_Type()
)
a37SlotLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37SlotLocation.setStatus("mandatory")


class _A37SlotType_Type(Integer32):
    """Custom type a37SlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vEmbeddedDevice", 1),
          ("vExpansionSlot", 0),
          ("vVirtual", 2))
    )


_A37SlotType_Type.__name__ = "Integer32"
_A37SlotType_Object = MibTableColumn
a37SlotType = _A37SlotType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 6),
    _A37SlotType_Type()
)
a37SlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37SlotType.setStatus("mandatory")
_A37NumberOfDeviceFunctions_Type = DmiInteger
_A37NumberOfDeviceFunctions_Object = MibTableColumn
a37NumberOfDeviceFunctions = _A37NumberOfDeviceFunctions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 7),
    _A37NumberOfDeviceFunctions_Type()
)
a37NumberOfDeviceFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37NumberOfDeviceFunctions.setStatus("mandatory")


class _A37IdType_Type(Integer32):
    """Custom type a37IdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vNotReadable", 1),
          ("vReadable", 0))
    )


_A37IdType_Type.__name__ = "Integer32"
_A37IdType_Object = MibTableColumn
a37IdType = _A37IdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 37, 1, 8),
    _A37IdType_Type()
)
a37IdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37IdType.setStatus("mandatory")
_TRaidAdapterInformation_Object = MibTable
tRaidAdapterInformation = _TRaidAdapterInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38)
)
if mibBuilder.loadTexts:
    tRaidAdapterInformation.setStatus("mandatory")
_ERaidAdapterInformation_Object = MibTableRow
eRaidAdapterInformation = _ERaidAdapterInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38, 1)
)
eRaidAdapterInformation.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a38RaidAdapterIndex"),
)
if mibBuilder.loadTexts:
    eRaidAdapterInformation.setStatus("mandatory")
_A38RaidAdapterIndex_Type = DmiInteger
_A38RaidAdapterIndex_Object = MibTableColumn
a38RaidAdapterIndex = _A38RaidAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38, 1, 1),
    _A38RaidAdapterIndex_Type()
)
a38RaidAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a38RaidAdapterIndex.setStatus("mandatory")
_A38NumberOfLogicalVolumes_Type = DmiInteger
_A38NumberOfLogicalVolumes_Object = MibTableColumn
a38NumberOfLogicalVolumes = _A38NumberOfLogicalVolumes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38, 1, 2),
    _A38NumberOfLogicalVolumes_Type()
)
a38NumberOfLogicalVolumes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a38NumberOfLogicalVolumes.setStatus("mandatory")
_A38NumberOfPhysicalDevices_Type = DmiInteger
_A38NumberOfPhysicalDevices_Object = MibTableColumn
a38NumberOfPhysicalDevices = _A38NumberOfPhysicalDevices_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38, 1, 3),
    _A38NumberOfPhysicalDevices_Type()
)
a38NumberOfPhysicalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a38NumberOfPhysicalDevices.setStatus("mandatory")
_A38NumberOfPhysicalDrivesOffline_Type = DmiInteger
_A38NumberOfPhysicalDrivesOffline_Object = MibTableColumn
a38NumberOfPhysicalDrivesOffline = _A38NumberOfPhysicalDrivesOffline_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38, 1, 4),
    _A38NumberOfPhysicalDrivesOffline_Type()
)
a38NumberOfPhysicalDrivesOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a38NumberOfPhysicalDrivesOffline.setStatus("mandatory")
_A38NumberOfCriticalVirtualDrives_Type = DmiInteger
_A38NumberOfCriticalVirtualDrives_Object = MibTableColumn
a38NumberOfCriticalVirtualDrives = _A38NumberOfCriticalVirtualDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38, 1, 5),
    _A38NumberOfCriticalVirtualDrives_Type()
)
a38NumberOfCriticalVirtualDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a38NumberOfCriticalVirtualDrives.setStatus("mandatory")
_A38NumberOfDefunctPhysicalDrives_Type = DmiInteger
_A38NumberOfDefunctPhysicalDrives_Object = MibTableColumn
a38NumberOfDefunctPhysicalDrives = _A38NumberOfDefunctPhysicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 38, 1, 6),
    _A38NumberOfDefunctPhysicalDrives_Type()
)
a38NumberOfDefunctPhysicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a38NumberOfDefunctPhysicalDrives.setStatus("mandatory")
_TRaidVirtualDrivesInformation_Object = MibTable
tRaidVirtualDrivesInformation = _TRaidVirtualDrivesInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 39)
)
if mibBuilder.loadTexts:
    tRaidVirtualDrivesInformation.setStatus("mandatory")
_ERaidVirtualDrivesInformation_Object = MibTableRow
eRaidVirtualDrivesInformation = _ERaidVirtualDrivesInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 39, 1)
)
eRaidVirtualDrivesInformation.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a39RaidVirtualDriveIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a39RaidAdapterIndex"),
)
if mibBuilder.loadTexts:
    eRaidVirtualDrivesInformation.setStatus("mandatory")
_A39RaidVirtualDriveIndex_Type = DmiInteger
_A39RaidVirtualDriveIndex_Object = MibTableColumn
a39RaidVirtualDriveIndex = _A39RaidVirtualDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 39, 1, 1),
    _A39RaidVirtualDriveIndex_Type()
)
a39RaidVirtualDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a39RaidVirtualDriveIndex.setStatus("mandatory")
_A39RaidAdapterIndex_Type = DmiInteger
_A39RaidAdapterIndex_Object = MibTableColumn
a39RaidAdapterIndex = _A39RaidAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 39, 1, 2),
    _A39RaidAdapterIndex_Type()
)
a39RaidAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a39RaidAdapterIndex.setStatus("mandatory")


class _A39VirtualDriveState_Type(Integer32):
    """Custom type a39VirtualDriveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 2),
          ("vOffline", 1),
          ("vOnline", 0))
    )


_A39VirtualDriveState_Type.__name__ = "Integer32"
_A39VirtualDriveState_Object = MibTableColumn
a39VirtualDriveState = _A39VirtualDriveState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 39, 1, 3),
    _A39VirtualDriveState_Type()
)
a39VirtualDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a39VirtualDriveState.setStatus("mandatory")
_A39VirtualDriveSize_Type = DmiInteger
_A39VirtualDriveSize_Object = MibTableColumn
a39VirtualDriveSize = _A39VirtualDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 39, 1, 4),
    _A39VirtualDriveSize_Type()
)
a39VirtualDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a39VirtualDriveSize.setStatus("mandatory")
_TRaidPhysicalDriveInformation_Object = MibTable
tRaidPhysicalDriveInformation = _TRaidPhysicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40)
)
if mibBuilder.loadTexts:
    tRaidPhysicalDriveInformation.setStatus("mandatory")
_ERaidPhysicalDriveInformation_Object = MibTableRow
eRaidPhysicalDriveInformation = _ERaidPhysicalDriveInformation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40, 1)
)
eRaidPhysicalDriveInformation.setIndexNames(
    (0, "PCSYSTEMSMIF-MIB", "DmiComponentIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a40RaidPhysicalDriveIndex"),
    (0, "PCSYSTEMSMIF-MIB", "a40RaidAdapterIndex"),
)
if mibBuilder.loadTexts:
    eRaidPhysicalDriveInformation.setStatus("mandatory")
_A40RaidPhysicalDriveIndex_Type = DmiInteger
_A40RaidPhysicalDriveIndex_Object = MibTableColumn
a40RaidPhysicalDriveIndex = _A40RaidPhysicalDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40, 1, 1),
    _A40RaidPhysicalDriveIndex_Type()
)
a40RaidPhysicalDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a40RaidPhysicalDriveIndex.setStatus("mandatory")
_A40RaidAdapterIndex_Type = DmiInteger
_A40RaidAdapterIndex_Object = MibTableColumn
a40RaidAdapterIndex = _A40RaidAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40, 1, 2),
    _A40RaidAdapterIndex_Type()
)
a40RaidAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a40RaidAdapterIndex.setStatus("mandatory")
_A40PhysicalDriveSize_Type = DmiInteger
_A40PhysicalDriveSize_Object = MibTableColumn
a40PhysicalDriveSize = _A40PhysicalDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40, 1, 3),
    _A40PhysicalDriveSize_Type()
)
a40PhysicalDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a40PhysicalDriveSize.setStatus("mandatory")
_A40ChannelNumber_Type = DmiInteger
_A40ChannelNumber_Object = MibTableColumn
a40ChannelNumber = _A40ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40, 1, 4),
    _A40ChannelNumber_Type()
)
a40ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a40ChannelNumber.setStatus("mandatory")
_A40TargetNumber_Type = DmiInteger
_A40TargetNumber_Object = MibTableColumn
a40TargetNumber = _A40TargetNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40, 1, 5),
    _A40TargetNumber_Type()
)
a40TargetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a40TargetNumber.setStatus("mandatory")


class _A40RaidPhysicalDeviceState_Type(Integer32):
    """Custom type a40RaidPhysicalDeviceState based on Integer32"""
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
        *(("vDeadHotspare", 5),
          ("vDefunct", 2),
          ("vHotspare", 3),
          ("vOffline", 1),
          ("vOnline", 0),
          ("vReady", 6),
          ("vRebuild", 7),
          ("vStandby", 8),
          ("vStandbyHotspare", 4))
    )


_A40RaidPhysicalDeviceState_Type.__name__ = "Integer32"
_A40RaidPhysicalDeviceState_Object = MibTableColumn
a40RaidPhysicalDeviceState = _A40RaidPhysicalDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 1, 1, 40, 1, 6),
    _A40RaidPhysicalDeviceState_Type()
)
a40RaidPhysicalDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a40RaidPhysicalDeviceState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCSYSTEMSMIF-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiInteger64": DmiInteger64,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDate": DmiDate,
       "DmiComponentIndex": DmiComponentIndex,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "netFinity": netFinity,
       "dmiMibs": dmiMibs,
       "netFinitySystemsMIB": netFinitySystemsMIB,
       "dmtfGroups1": dmtfGroups1,
       "tComponentid1": tComponentid1,
       "eComponentid1": eComponentid1,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "tGeneralInformation": tGeneralInformation,
       "eGeneralInformation": eGeneralInformation,
       "a2SystemName": a2SystemName,
       "a2SystemLocation": a2SystemLocation,
       "a2SystemPrimaryUserName": a2SystemPrimaryUserName,
       "a2SystemPrimaryUserPhone": a2SystemPrimaryUserPhone,
       "a2SystemBootUpTime": a2SystemBootUpTime,
       "a2SystemDateTime": a2SystemDateTime,
       "tOperatingSystem": tOperatingSystem,
       "eOperatingSystem": eOperatingSystem,
       "a3OperatingSystemIndex": a3OperatingSystemIndex,
       "a3OperatingSystemName": a3OperatingSystemName,
       "a3OperatingSystemVersion": a3OperatingSystemVersion,
       "a3PrimaryOperatingSystem": a3PrimaryOperatingSystem,
       "a3OperatingSystemBootDeviceStorageType": a3OperatingSystemBootDeviceStorageType,
       "a3OperatingSystemBootDeviceIndex": a3OperatingSystemBootDeviceIndex,
       "a3OperatingSystemBootPartitionIndex": a3OperatingSystemBootPartitionIndex,
       "a3OperatingSystemDescription": a3OperatingSystemDescription,
       "tSystemBios": tSystemBios,
       "eSystemBios": eSystemBios,
       "a4BiosIndex": a4BiosIndex,
       "a4Manufacturer": a4Manufacturer,
       "a4Version": a4Version,
       "a4BiosRomSize": a4BiosRomSize,
       "a4StartingAddress": a4StartingAddress,
       "a4EndingAddress": a4EndingAddress,
       "a4LoaderVersion": a4LoaderVersion,
       "a4BiosReleaseDate": a4BiosReleaseDate,
       "a4PrimaryBios": a4PrimaryBios,
       "tSystemBiosCharacteristic": tSystemBiosCharacteristic,
       "eSystemBiosCharacteristic": eSystemBiosCharacteristic,
       "a5BiosCharacteristicsIndex": a5BiosCharacteristicsIndex,
       "a5BiosNumber": a5BiosNumber,
       "a5BiosCharacteristics": a5BiosCharacteristics,
       "a5BiosCharacteristicsDescription": a5BiosCharacteristicsDescription,
       "tProcessor": tProcessor,
       "eProcessor": eProcessor,
       "a6ProcessorIndex": a6ProcessorIndex,
       "a6Type": a6Type,
       "a6ProcessorFamily": a6ProcessorFamily,
       "a6VersionInformation": a6VersionInformation,
       "a6MaximumSpeed": a6MaximumSpeed,
       "a6CurrentSpeed": a6CurrentSpeed,
       "a6ProcessorUpgrade": a6ProcessorUpgrade,
       "a6FruGroupIndex": a6FruGroupIndex,
       "a6OperationalGroupIndex": a6OperationalGroupIndex,
       "tMotherboard": tMotherboard,
       "eMotherboard": eMotherboard,
       "a7NumberOfExpansionSlots": a7NumberOfExpansionSlots,
       "a7FruGroupIndex": a7FruGroupIndex,
       "a7OperationalGroupIndex": a7OperationalGroupIndex,
       "tPhysicalMemory": tPhysicalMemory,
       "ePhysicalMemory": ePhysicalMemory,
       "a8PhysicalMemoryIndex": a8PhysicalMemoryIndex,
       "a8PhysicalMemoryLocation": a8PhysicalMemoryLocation,
       "a8MemoryStartingAddress": a8MemoryStartingAddress,
       "a8MemoryEndingAddress": a8MemoryEndingAddress,
       "a8MemoryUsage": a8MemoryUsage,
       "a8MaximumMemoryCapacity": a8MaximumMemoryCapacity,
       "a8NumberOfSimmSlots": a8NumberOfSimmSlots,
       "a8NumberOfSimmSlotsUsed": a8NumberOfSimmSlotsUsed,
       "a8MemorySpeed": a8MemorySpeed,
       "a8MemoryErrorCorrection": a8MemoryErrorCorrection,
       "a8FruGroupIndex": a8FruGroupIndex,
       "a8OperationalGroupIndex": a8OperationalGroupIndex,
       "tLogicalMemory": tLogicalMemory,
       "eLogicalMemory": eLogicalMemory,
       "a9BaseMemorySize": a9BaseMemorySize,
       "a9FreeBaseMemorySize": a9FreeBaseMemorySize,
       "a9ExtendedMemorySize": a9ExtendedMemorySize,
       "a9FreeExtendedMemorySize": a9FreeExtendedMemorySize,
       "a9ExtendedMemoryManagerName": a9ExtendedMemoryManagerName,
       "a9ExtendedMemoryManagerVersion": a9ExtendedMemoryManagerVersion,
       "a9ExpandedMemorySize": a9ExpandedMemorySize,
       "a9FreeExpandedMemorySize": a9FreeExpandedMemorySize,
       "a9ExpandedMemoryManagerName": a9ExpandedMemoryManagerName,
       "a9ExpandedMemoryManagerVersion": a9ExpandedMemoryManagerVersion,
       "a9ExpandedMemoryPageFrameAddress": a9ExpandedMemoryPageFrameAddress,
       "a9ExpandedMemoryPageFrameSize": a9ExpandedMemoryPageFrameSize,
       "a9ExpandedMemoryPageSize": a9ExpandedMemoryPageSize,
       "tSystemCache": tSystemCache,
       "eSystemCache": eSystemCache,
       "a10SystemCacheIndex": a10SystemCacheIndex,
       "a10SystemCacheLevel": a10SystemCacheLevel,
       "a10SystemCacheSpeed": a10SystemCacheSpeed,
       "a10SystemCacheSize": a10SystemCacheSize,
       "a10SystemCacheWritePolicy": a10SystemCacheWritePolicy,
       "a10SystemCacheErrorCorrection": a10SystemCacheErrorCorrection,
       "a10FruGroupIndex": a10FruGroupIndex,
       "a10OperationalGroupIndex": a10OperationalGroupIndex,
       "tParallelPorts": tParallelPorts,
       "eParallelPorts": eParallelPorts,
       "a11ParallelPortIndex": a11ParallelPortIndex,
       "a11ParallelBaseIoAddress": a11ParallelBaseIoAddress,
       "a11IrqUsed": a11IrqUsed,
       "a11LogicalName": a11LogicalName,
       "a11ConnectorType": a11ConnectorType,
       "a11ConnectorPinout": a11ConnectorPinout,
       "a11DmaSupport": a11DmaSupport,
       "a11ParallelPortCapabilities": a11ParallelPortCapabilities,
       "a11OperationalGroupIndex": a11OperationalGroupIndex,
       "tSerialPorts": tSerialPorts,
       "eSerialPorts": eSerialPorts,
       "a12SerialPortIndex": a12SerialPortIndex,
       "a12SerialBaseIo": a12SerialBaseIo,
       "a12IrqUsed": a12IrqUsed,
       "a12LogicalName": a12LogicalName,
       "a12ConnectorType": a12ConnectorType,
       "a12MaximumSpeed": a12MaximumSpeed,
       "a12SerialPortCapabilities": a12SerialPortCapabilities,
       "a12OperationalGroupIndex": a12OperationalGroupIndex,
       "tIrq": tIrq,
       "eIrq": eIrq,
       "a13IrqNumber": a13IrqNumber,
       "a13AvailabilityOfIrq": a13AvailabilityOfIrq,
       "a13IrqTriggerType": a13IrqTriggerType,
       "a13IrqShareable": a13IrqShareable,
       "a13IrqDescription": a13IrqDescription,
       "tDma": tDma,
       "eDma": eDma,
       "a14DmaNumber": a14DmaNumber,
       "a14AvailabilityOfDma": a14AvailabilityOfDma,
       "a14DmaBurstMode": a14DmaBurstMode,
       "a14DmaDescription": a14DmaDescription,
       "tMemoryMappedIo": tMemoryMappedIo,
       "eMemoryMappedIo": eMemoryMappedIo,
       "a15MemoryMappedIoStartingAddress": a15MemoryMappedIoStartingAddress,
       "a15MemoryMappedIoEndingAddress": a15MemoryMappedIoEndingAddress,
       "a15MemoryMappedIoDescription": a15MemoryMappedIoDescription,
       "tSystemEnclosure": tSystemEnclosure,
       "eSystemEnclosure": eSystemEnclosure,
       "a16EnclosureOrChassis": a16EnclosureOrChassis,
       "a16AssetTag": a16AssetTag,
       "a16ChassisLockPresent": a16ChassisLockPresent,
       "a16BootUpState": a16BootUpState,
       "a16PowerState": a16PowerState,
       "a16ThermalState": a16ThermalState,
       "a16FruGroupIndex": a16FruGroupIndex,
       "a16OperationalGroupIndex": a16OperationalGroupIndex,
       "tPowerSupply": tPowerSupply,
       "ePowerSupply": ePowerSupply,
       "a17PowerSupplyIndex": a17PowerSupplyIndex,
       "a17FruGroupIndex": a17FruGroupIndex,
       "a17OperationalGroupIndex": a17OperationalGroupIndex,
       "tCoolingDevice": tCoolingDevice,
       "eCoolingDevice": eCoolingDevice,
       "a18CoolingDeviceIndex": a18CoolingDeviceIndex,
       "a18FruGroupIndex": a18FruGroupIndex,
       "a18OperationalGroupIndex": a18OperationalGroupIndex,
       "tSystemSlots": tSystemSlots,
       "eSystemSlots": eSystemSlots,
       "a19SlotIndex": a19SlotIndex,
       "a19SlotType": a19SlotType,
       "a19SlotWidth": a19SlotWidth,
       "a19CurrentUsage": a19CurrentUsage,
       "a19SlotDescription": a19SlotDescription,
       "tVideo": tVideo,
       "eVideo": eVideo,
       "a20VideoIndex": a20VideoIndex,
       "a20VideoType": a20VideoType,
       "a20CurrentVideoMode": a20CurrentVideoMode,
       "a20MinimumRefreshRate": a20MinimumRefreshRate,
       "a20MaximumRefreshRate": a20MaximumRefreshRate,
       "a20VideoMemoryType": a20VideoMemoryType,
       "a20VideoRamMemorySize": a20VideoRamMemorySize,
       "a20ScanMode": a20ScanMode,
       "a20VideoPhysicalLocation": a20VideoPhysicalLocation,
       "a20CurrentVerticalResolution": a20CurrentVerticalResolution,
       "a20CurrentHorizontalResolution": a20CurrentHorizontalResolution,
       "a20CurrentNumberOfBitsPerPixel": a20CurrentNumberOfBitsPerPixel,
       "a20CurrentNumberOfRows": a20CurrentNumberOfRows,
       "a20CurrentNumberOfColumns": a20CurrentNumberOfColumns,
       "a20CurrentRefreshRate": a20CurrentRefreshRate,
       "a20FruGroupIndex": a20FruGroupIndex,
       "a20OperationalGroupIndex": a20OperationalGroupIndex,
       "tVideoBios": tVideoBios,
       "eVideoBios": eVideoBios,
       "a21VideoBiosIndex": a21VideoBiosIndex,
       "a21VideoBiosManufacturer": a21VideoBiosManufacturer,
       "a21VideoBiosVersion": a21VideoBiosVersion,
       "a21VideoBiosReleaseDate": a21VideoBiosReleaseDate,
       "a21VideoBiosShadowingState": a21VideoBiosShadowingState,
       "tVideoBiosCharacteristic": tVideoBiosCharacteristic,
       "eVideoBiosCharacteristic": eVideoBiosCharacteristic,
       "a22VideoBiosCharacteristicsIndex": a22VideoBiosCharacteristicsIndex,
       "a22VideoBiosNumber": a22VideoBiosNumber,
       "a22VideoBiosCharacteristics": a22VideoBiosCharacteristics,
       "a22VideoBiosCharacteristicsDescription": a22VideoBiosCharacteristicsDescription,
       "tDiskDrives": tDiskDrives,
       "eDiskDrives": eDiskDrives,
       "a23StorageType": a23StorageType,
       "a23DiskIndex": a23DiskIndex,
       "a23StorageInterfaceType": a23StorageInterfaceType,
       "a23InterfaceDescription": a23InterfaceDescription,
       "a23MediaLoaded": a23MediaLoaded,
       "a23RemovableMedia": a23RemovableMedia,
       "a23DeviceId": a23DeviceId,
       "a23LogicalUnitNumber": a23LogicalUnitNumber,
       "a23NumberOfPhysicalCylinders": a23NumberOfPhysicalCylinders,
       "a23NumberOfPhysicalSectorsPerTrack": a23NumberOfPhysicalSectorsPerTrack,
       "a23NumberOfPhysicalHeads": a23NumberOfPhysicalHeads,
       "a23SectorSize": a23SectorSize,
       "a23TotalPhysicalSize": a23TotalPhysicalSize,
       "a23Partitions": a23Partitions,
       "a23FruGroupIndex": a23FruGroupIndex,
       "tDiskMappingTable": tDiskMappingTable,
       "eDiskMappingTable": eDiskMappingTable,
       "a24StorageType": a24StorageType,
       "a24DiskIndex": a24DiskIndex,
       "a24PartitionIndex": a24PartitionIndex,
       "tPartition": tPartition,
       "ePartition": ePartition,
       "a25PartitionIndex": a25PartitionIndex,
       "a25PartitionName": a25PartitionName,
       "a25PartitionSize": a25PartitionSize,
       "a25FreeSpace": a25FreeSpace,
       "a25PartitionLabel": a25PartitionLabel,
       "a25FileSystem": a25FileSystem,
       "a25Compressed": a25Compressed,
       "a25Encrypted": a25Encrypted,
       "a25NumberOfDisksOccupied": a25NumberOfDisksOccupied,
       "tDiskController": tDiskController,
       "eDiskController": eDiskController,
       "a26DiskControllerIndex": a26DiskControllerIndex,
       "a26FruGroupIndex": a26FruGroupIndex,
       "a26OperationalGroupIndex": a26OperationalGroupIndex,
       "tLogicalDrives": tLogicalDrives,
       "eLogicalDrives": eLogicalDrives,
       "a27LogicalDriveIndex": a27LogicalDriveIndex,
       "a27LogicalDriveName": a27LogicalDriveName,
       "a27LogicalDriveType": a27LogicalDriveType,
       "a27LogicalDriveSize": a27LogicalDriveSize,
       "a27FreeLogicalDriveSize": a27FreeLogicalDriveSize,
       "a27LogicalDrivePath": a27LogicalDrivePath,
       "tMouse": tMouse,
       "eMouse": eMouse,
       "a28MouseInterface": a28MouseInterface,
       "a28MouseIrq": a28MouseIrq,
       "a28MouseButtons": a28MouseButtons,
       "a28MousePortName": a28MousePortName,
       "a28MouseDriverName": a28MouseDriverName,
       "a28MouseDriverVersion": a28MouseDriverVersion,
       "a28FruGroupIndex": a28FruGroupIndex,
       "a28OperationalGroupIndex": a28OperationalGroupIndex,
       "tKeyboard": tKeyboard,
       "eKeyboard": eKeyboard,
       "a29KeyboardLayout": a29KeyboardLayout,
       "a29KeyboardType": a29KeyboardType,
       "a29KeyboardConnectorType": a29KeyboardConnectorType,
       "a29FruGroupIndex": a29FruGroupIndex,
       "a29OperationalGroupIndex": a29OperationalGroupIndex,
       "tFieldReplacableUnit": tFieldReplacableUnit,
       "eFieldReplacableUnit": eFieldReplacableUnit,
       "a30FruIndex": a30FruIndex,
       "a30DeviceGroupIndex": a30DeviceGroupIndex,
       "a30Description": a30Description,
       "a30Manufacturer": a30Manufacturer,
       "a30Model": a30Model,
       "a30PartNumber": a30PartNumber,
       "a30FruSerialNumber": a30FruSerialNumber,
       "a30RevisionLevel": a30RevisionLevel,
       "tOperationalState": tOperationalState,
       "eOperationalState": eOperationalState,
       "a31OperationalStateInstanceIndex": a31OperationalStateInstanceIndex,
       "a31DeviceGroupIndex": a31DeviceGroupIndex,
       "a31OperationalStatus": a31OperationalStatus,
       "a31UsageState": a31UsageState,
       "a31AvailabilityStatus": a31AvailabilityStatus,
       "a31AdministrativeState": a31AdministrativeState,
       "a31FatalErrorCount": a31FatalErrorCount,
       "a31MajorErrorCount": a31MajorErrorCount,
       "a31WarningErrorCount": a31WarningErrorCount,
       "tSystemResourcesDescription": tSystemResourcesDescription,
       "eSystemResourcesDescription": eSystemResourcesDescription,
       "a32DeviceCount": a32DeviceCount,
       "a32SystemResourceCount": a32SystemResourceCount,
       "tSystemResources": tSystemResources,
       "eSystemResources": eSystemResources,
       "a33ResourceInstance": a33ResourceInstance,
       "a33ResourceParentGroupIndex": a33ResourceParentGroupIndex,
       "a33ResourceType": a33ResourceType,
       "a33ResourceBase": a33ResourceBase,
       "a33ResourceSize": a33ResourceSize,
       "a33ResourceFlags": a33ResourceFlags,
       "tNetfinityDmiInstall": tNetfinityDmiInstall,
       "eNetfinityDmiInstall": eNetfinityDmiInstall,
       "a34ProductName": a34ProductName,
       "tMicrochannelAdapterInformation": tMicrochannelAdapterInformation,
       "eMicrochannelAdapterInformation": eMicrochannelAdapterInformation,
       "a35AdapterIndex": a35AdapterIndex,
       "a35SlotNumber": a35SlotNumber,
       "a35AdapterId": a35AdapterId,
       "a35PosData": a35PosData,
       "a35AdapterName": a35AdapterName,
       "tPciDeviceInformation": tPciDeviceInformation,
       "ePciDeviceInformation": ePciDeviceInformation,
       "a36DeviceIndex": a36DeviceIndex,
       "a36ClassCode": a36ClassCode,
       "a36PciDeviceName": a36PciDeviceName,
       "a36VendorId": a36VendorId,
       "a36DeviceId": a36DeviceId,
       "a36BusNumber": a36BusNumber,
       "a36DeviceNumber": a36DeviceNumber,
       "a36RevisionId": a36RevisionId,
       "tEisaDeviceInformation": tEisaDeviceInformation,
       "eEisaDeviceInformation": eEisaDeviceInformation,
       "a37DeviceIndex": a37DeviceIndex,
       "a37ProductId": a37ProductId,
       "a37EisaDeviceName": a37EisaDeviceName,
       "a37Manufacturer": a37Manufacturer,
       "a37SlotLocation": a37SlotLocation,
       "a37SlotType": a37SlotType,
       "a37NumberOfDeviceFunctions": a37NumberOfDeviceFunctions,
       "a37IdType": a37IdType,
       "tRaidAdapterInformation": tRaidAdapterInformation,
       "eRaidAdapterInformation": eRaidAdapterInformation,
       "a38RaidAdapterIndex": a38RaidAdapterIndex,
       "a38NumberOfLogicalVolumes": a38NumberOfLogicalVolumes,
       "a38NumberOfPhysicalDevices": a38NumberOfPhysicalDevices,
       "a38NumberOfPhysicalDrivesOffline": a38NumberOfPhysicalDrivesOffline,
       "a38NumberOfCriticalVirtualDrives": a38NumberOfCriticalVirtualDrives,
       "a38NumberOfDefunctPhysicalDrives": a38NumberOfDefunctPhysicalDrives,
       "tRaidVirtualDrivesInformation": tRaidVirtualDrivesInformation,
       "eRaidVirtualDrivesInformation": eRaidVirtualDrivesInformation,
       "a39RaidVirtualDriveIndex": a39RaidVirtualDriveIndex,
       "a39RaidAdapterIndex": a39RaidAdapterIndex,
       "a39VirtualDriveState": a39VirtualDriveState,
       "a39VirtualDriveSize": a39VirtualDriveSize,
       "tRaidPhysicalDriveInformation": tRaidPhysicalDriveInformation,
       "eRaidPhysicalDriveInformation": eRaidPhysicalDriveInformation,
       "a40RaidPhysicalDriveIndex": a40RaidPhysicalDriveIndex,
       "a40RaidAdapterIndex": a40RaidAdapterIndex,
       "a40PhysicalDriveSize": a40PhysicalDriveSize,
       "a40ChannelNumber": a40ChannelNumber,
       "a40TargetNumber": a40TargetNumber,
       "a40RaidPhysicalDeviceState": a40RaidPhysicalDeviceState}
)
