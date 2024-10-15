# SNMP MIB module (INTELCORPORATIONBASEBOARD2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATIONBASEBOARD2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:14 2024
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

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Server_products_ObjectIdentity = ObjectIdentity
server_products = _Server_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6)
)
_Platforms_ObjectIdentity = ObjectIdentity
platforms = _Platforms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2)
)
_Basebrd2_ObjectIdentity = ObjectIdentity
basebrd2 = _Basebrd2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TGeneralInformation_Object = MibTable
tGeneralInformation = _TGeneralInformation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tGeneralInformation.setStatus("mandatory")
_EGeneralInformation_Object = MibTableRow
eGeneralInformation = _EGeneralInformation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2, 1)
)
eGeneralInformation.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eGeneralInformation.setStatus("mandatory")
_A2SystemName_Type = DmiDisplaystring
_A2SystemName_Object = MibTableColumn
a2SystemName = _A2SystemName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2, 1, 1),
    _A2SystemName_Type()
)
a2SystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemName.setStatus("mandatory")
_A2SystemLocation_Type = DmiDisplaystring
_A2SystemLocation_Object = MibTableColumn
a2SystemLocation = _A2SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2, 1, 2),
    _A2SystemLocation_Type()
)
a2SystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemLocation.setStatus("mandatory")
_A2SystemPrimaryUserName_Type = DmiDisplaystring
_A2SystemPrimaryUserName_Object = MibTableColumn
a2SystemPrimaryUserName = _A2SystemPrimaryUserName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2, 1, 3),
    _A2SystemPrimaryUserName_Type()
)
a2SystemPrimaryUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemPrimaryUserName.setStatus("mandatory")
_A2SystemPrimaryUserPhone_Type = DmiDisplaystring
_A2SystemPrimaryUserPhone_Object = MibTableColumn
a2SystemPrimaryUserPhone = _A2SystemPrimaryUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2, 1, 4),
    _A2SystemPrimaryUserPhone_Type()
)
a2SystemPrimaryUserPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemPrimaryUserPhone.setStatus("mandatory")
_A2SystemBootupTime_Type = DmiDateX
_A2SystemBootupTime_Object = MibTableColumn
a2SystemBootupTime = _A2SystemBootupTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2, 1, 5),
    _A2SystemBootupTime_Type()
)
a2SystemBootupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SystemBootupTime.setStatus("mandatory")
_A2SystemDateTime_Type = DmiDateX
_A2SystemDateTime_Object = MibTableColumn
a2SystemDateTime = _A2SystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 2, 1, 6),
    _A2SystemDateTime_Type()
)
a2SystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2SystemDateTime.setStatus("mandatory")
_TSystemBios_Object = MibTable
tSystemBios = _TSystemBios_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tSystemBios.setStatus("mandatory")
_ESystemBios_Object = MibTableRow
eSystemBios = _ESystemBios_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1)
)
eSystemBios.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a4BiosIndex"),
)
if mibBuilder.loadTexts:
    eSystemBios.setStatus("mandatory")
_A4BiosIndex_Type = DmiInteger
_A4BiosIndex_Object = MibTableColumn
a4BiosIndex = _A4BiosIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 1),
    _A4BiosIndex_Type()
)
a4BiosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosIndex.setStatus("mandatory")
_A4BiosManufacturer_Type = DmiDisplaystring
_A4BiosManufacturer_Object = MibTableColumn
a4BiosManufacturer = _A4BiosManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 2),
    _A4BiosManufacturer_Type()
)
a4BiosManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosManufacturer.setStatus("mandatory")
_A4BiosVersion_Type = DmiDisplaystring
_A4BiosVersion_Object = MibTableColumn
a4BiosVersion = _A4BiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 3),
    _A4BiosVersion_Type()
)
a4BiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosVersion.setStatus("mandatory")
_A4BiosRomSize_Type = DmiInteger
_A4BiosRomSize_Object = MibTableColumn
a4BiosRomSize = _A4BiosRomSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 4),
    _A4BiosRomSize_Type()
)
a4BiosRomSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosRomSize.setStatus("mandatory")
_A4BiosStartingAddress_Type = DmiInteger64X
_A4BiosStartingAddress_Object = MibTableColumn
a4BiosStartingAddress = _A4BiosStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 5),
    _A4BiosStartingAddress_Type()
)
a4BiosStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosStartingAddress.setStatus("mandatory")
_A4BiosEndingAddress_Type = DmiInteger64X
_A4BiosEndingAddress_Object = MibTableColumn
a4BiosEndingAddress = _A4BiosEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 6),
    _A4BiosEndingAddress_Type()
)
a4BiosEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosEndingAddress.setStatus("mandatory")
_A4BiosLoaderVersion_Type = DmiDisplaystring
_A4BiosLoaderVersion_Object = MibTableColumn
a4BiosLoaderVersion = _A4BiosLoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 7),
    _A4BiosLoaderVersion_Type()
)
a4BiosLoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4BiosLoaderVersion.setStatus("mandatory")
_A4BiosReleaseDate_Type = DmiDateX
_A4BiosReleaseDate_Object = MibTableColumn
a4BiosReleaseDate = _A4BiosReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 4, 1, 9),
    _A4PrimaryBios_Type()
)
a4PrimaryBios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4PrimaryBios.setStatus("mandatory")
_TSystemBiosCharacteristics_Object = MibTable
tSystemBiosCharacteristics = _TSystemBiosCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tSystemBiosCharacteristics.setStatus("mandatory")
_ESystemBiosCharacteristics_Object = MibTableRow
eSystemBiosCharacteristics = _ESystemBiosCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 5, 1)
)
eSystemBiosCharacteristics.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a5BiosCharacteristicIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a5BiosNumber"),
)
if mibBuilder.loadTexts:
    eSystemBiosCharacteristics.setStatus("mandatory")
_A5BiosCharacteristicIndex_Type = DmiInteger
_A5BiosCharacteristicIndex_Object = MibTableColumn
a5BiosCharacteristicIndex = _A5BiosCharacteristicIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 5, 1, 1),
    _A5BiosCharacteristicIndex_Type()
)
a5BiosCharacteristicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosCharacteristicIndex.setStatus("mandatory")
_A5BiosNumber_Type = DmiInteger
_A5BiosNumber_Object = MibTableColumn
a5BiosNumber = _A5BiosNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 5, 1, 2),
    _A5BiosNumber_Type()
)
a5BiosNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosNumber.setStatus("mandatory")


class _A5BiosCharacteristic_Type(Integer32):
    """Custom type a5BiosCharacteristic based on Integer32"""
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
              160)
        )
    )
    namedValues = NamedValues(
        *(("vApmSupport", 10),
          ("vBiosShadowingAllowed", 12),
          ("vEisaSupport", 6),
          ("vEscdSupport", 14),
          ("vIsaSupport", 4),
          ("vMcaSupport", 5),
          ("vOther", 1),
          ("vPc-98", 160),
          ("vPciSupport", 7),
          ("vPcmciaSupport", 8),
          ("vPnpSupport", 9),
          ("vUnknown", 2),
          ("vUnsupported", 3),
          ("vUpgradeableBios", 11),
          ("vVlVesaSupport", 13))
    )


_A5BiosCharacteristic_Type.__name__ = "Integer32"
_A5BiosCharacteristic_Object = MibTableColumn
a5BiosCharacteristic = _A5BiosCharacteristic_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 5, 1, 3),
    _A5BiosCharacteristic_Type()
)
a5BiosCharacteristic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosCharacteristic.setStatus("mandatory")
_A5BiosCharacteristicDescription_Type = DmiDisplaystring
_A5BiosCharacteristicDescription_Object = MibTableColumn
a5BiosCharacteristicDescription = _A5BiosCharacteristicDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 5, 1, 4),
    _A5BiosCharacteristicDescription_Type()
)
a5BiosCharacteristicDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5BiosCharacteristicDescription.setStatus("mandatory")
_TProcessor_Object = MibTable
tProcessor = _TProcessor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tProcessor.setStatus("mandatory")
_EProcessor_Object = MibTableRow
eProcessor = _EProcessor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1)
)
eProcessor.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a6ProcessorIndex"),
)
if mibBuilder.loadTexts:
    eProcessor.setStatus("mandatory")
_A6ProcessorIndex_Type = DmiInteger
_A6ProcessorIndex_Object = MibTableColumn
a6ProcessorIndex = _A6ProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 1),
    _A6ProcessorIndex_Type()
)
a6ProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorIndex.setStatus("mandatory")


class _A6ProcessorType_Type(Integer32):
    """Custom type a6ProcessorType based on Integer32"""
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
          ("vDspProcessor", 5),
          ("vMathProcessor", 4),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vVideoProcessor", 6))
    )


_A6ProcessorType_Type.__name__ = "Integer32"
_A6ProcessorType_Object = MibTableColumn
a6ProcessorType = _A6ProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 2),
    _A6ProcessorType_Type()
)
a6ProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorType.setStatus("mandatory")


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
              12,
              18,
              25,
              32,
              33,
              34,
              35,
              36,
              48,
              64,
              80,
              96,
              97,
              98,
              99,
              100,
              101,
              112,
              128,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("v68000", 98),
          ("v68010", 99),
          ("v68020", 100),
          ("v68030", 101),
          ("v68040", 96),
          ("v68xxxFamily", 97),
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
          ("vK5Family", 25),
          ("vM1Family", 18),
          ("vMipsFamily", 64),
          ("vOther", 1),
          ("vPa-riscFamily", 144),
          ("vPentiumFamily", 11),
          ("vPentiumPro", 12),
          ("vPowerPc601", 33),
          ("vPowerPc603", 34),
          ("vPowerPc603plus", 35),
          ("vPowerPc604", 36),
          ("vPowerPcFamily", 32),
          ("vSparcFamily", 80),
          ("vUnknown", 2),
          ("vV30Family", 160),
          ("vWeitek", 128))
    )


_A6ProcessorFamily_Type.__name__ = "Integer32"
_A6ProcessorFamily_Object = MibTableColumn
a6ProcessorFamily = _A6ProcessorFamily_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 3),
    _A6ProcessorFamily_Type()
)
a6ProcessorFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorFamily.setStatus("mandatory")
_A6ProcessorVersionInformation_Type = DmiDisplaystring
_A6ProcessorVersionInformation_Object = MibTableColumn
a6ProcessorVersionInformation = _A6ProcessorVersionInformation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 4),
    _A6ProcessorVersionInformation_Type()
)
a6ProcessorVersionInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorVersionInformation.setStatus("mandatory")
_A6MaximumSpeed_Type = DmiInteger
_A6MaximumSpeed_Object = MibTableColumn
a6MaximumSpeed = _A6MaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 5),
    _A6MaximumSpeed_Type()
)
a6MaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6MaximumSpeed.setStatus("mandatory")
_A6CurrentSpeed_Type = DmiInteger
_A6CurrentSpeed_Object = MibTableColumn
a6CurrentSpeed = _A6CurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 6),
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vDaughterBoard", 3),
          ("vLifSocket", 7),
          ("vNone", 6),
          ("vOther", 1),
          ("vReplacementpiggyBack", 5),
          ("vUnknown", 2),
          ("vZifSocket", 4))
    )


_A6ProcessorUpgrade_Type.__name__ = "Integer32"
_A6ProcessorUpgrade_Object = MibTableColumn
a6ProcessorUpgrade = _A6ProcessorUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 7),
    _A6ProcessorUpgrade_Type()
)
a6ProcessorUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6ProcessorUpgrade.setStatus("mandatory")
_A6FruGroupIndex_Type = DmiInteger
_A6FruGroupIndex_Object = MibTableColumn
a6FruGroupIndex = _A6FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 8),
    _A6FruGroupIndex_Type()
)
a6FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6FruGroupIndex.setStatus("mandatory")
_A6OperationalGroupIndex_Type = DmiInteger
_A6OperationalGroupIndex_Object = MibTableColumn
a6OperationalGroupIndex = _A6OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 9),
    _A6OperationalGroupIndex_Type()
)
a6OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6OperationalGroupIndex.setStatus("mandatory")
_A6Level1CacheIndex_Type = DmiInteger
_A6Level1CacheIndex_Object = MibTableColumn
a6Level1CacheIndex = _A6Level1CacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 10),
    _A6Level1CacheIndex_Type()
)
a6Level1CacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Level1CacheIndex.setStatus("mandatory")
_A6Level2CacheIndex_Type = DmiInteger
_A6Level2CacheIndex_Object = MibTableColumn
a6Level2CacheIndex = _A6Level2CacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 11),
    _A6Level2CacheIndex_Type()
)
a6Level2CacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Level2CacheIndex.setStatus("mandatory")
_A6Level3CacheIndex_Type = DmiInteger
_A6Level3CacheIndex_Object = MibTableColumn
a6Level3CacheIndex = _A6Level3CacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 6, 1, 12),
    _A6Level3CacheIndex_Type()
)
a6Level3CacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Level3CacheIndex.setStatus("mandatory")
_TMotherboard_Object = MibTable
tMotherboard = _TMotherboard_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tMotherboard.setStatus("mandatory")
_EMotherboard_Object = MibTableRow
eMotherboard = _EMotherboard_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 7, 1)
)
eMotherboard.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMotherboard.setStatus("mandatory")
_A7NumberOfExpansionSlots_Type = DmiInteger
_A7NumberOfExpansionSlots_Object = MibTableColumn
a7NumberOfExpansionSlots = _A7NumberOfExpansionSlots_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 7, 1, 1),
    _A7NumberOfExpansionSlots_Type()
)
a7NumberOfExpansionSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7NumberOfExpansionSlots.setStatus("mandatory")
_A7FruGroupIndex_Type = DmiInteger
_A7FruGroupIndex_Object = MibTableColumn
a7FruGroupIndex = _A7FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 7, 1, 2),
    _A7FruGroupIndex_Type()
)
a7FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7FruGroupIndex.setStatus("mandatory")
_A7OperationalGroupIndex_Type = DmiInteger
_A7OperationalGroupIndex_Object = MibTableColumn
a7OperationalGroupIndex = _A7OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 7, 1, 3),
    _A7OperationalGroupIndex_Type()
)
a7OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7OperationalGroupIndex.setStatus("mandatory")
_TSystemCache_Object = MibTable
tSystemCache = _TSystemCache_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tSystemCache.setStatus("mandatory")
_ESystemCache_Object = MibTableRow
eSystemCache = _ESystemCache_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1)
)
eSystemCache.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a10SystemCacheIndex"),
)
if mibBuilder.loadTexts:
    eSystemCache.setStatus("mandatory")
_A10SystemCacheIndex_Type = DmiInteger
_A10SystemCacheIndex_Object = MibTableColumn
a10SystemCacheIndex = _A10SystemCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 2),
    _A10SystemCacheLevel_Type()
)
a10SystemCacheLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheLevel.setStatus("mandatory")
_A10SystemCacheSpeed_Type = DmiInteger
_A10SystemCacheSpeed_Object = MibTableColumn
a10SystemCacheSpeed = _A10SystemCacheSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 3),
    _A10SystemCacheSpeed_Type()
)
a10SystemCacheSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheSpeed.setStatus("mandatory")
_A10SystemCacheSize_Type = DmiInteger
_A10SystemCacheSize_Object = MibTableColumn
a10SystemCacheSize = _A10SystemCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 6),
    _A10SystemCacheErrorCorrection_Type()
)
a10SystemCacheErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheErrorCorrection.setStatus("mandatory")
_A10FruGroupIndex_Type = DmiInteger
_A10FruGroupIndex_Object = MibTableColumn
a10FruGroupIndex = _A10FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 7),
    _A10FruGroupIndex_Type()
)
a10FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10FruGroupIndex.setStatus("mandatory")
_A10OperationalGroupIndex_Type = DmiInteger
_A10OperationalGroupIndex_Object = MibTableColumn
a10OperationalGroupIndex = _A10OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 8),
    _A10OperationalGroupIndex_Type()
)
a10OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10OperationalGroupIndex.setStatus("mandatory")


class _A10SystemCacheType_Type(Integer32):
    """Custom type a10SystemCacheType based on Integer32"""
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
        *(("vData", 4),
          ("vInstruction", 3),
          ("vOther", 1),
          ("vUnified", 5),
          ("vUnknown", 2))
    )


_A10SystemCacheType_Type.__name__ = "Integer32"
_A10SystemCacheType_Object = MibTableColumn
a10SystemCacheType = _A10SystemCacheType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 10, 1, 9),
    _A10SystemCacheType_Type()
)
a10SystemCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10SystemCacheType.setStatus("mandatory")
_TPowerSupply_Object = MibTable
tPowerSupply = _TPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17)
)
if mibBuilder.loadTexts:
    tPowerSupply.setStatus("mandatory")
_EPowerSupply_Object = MibTableRow
ePowerSupply = _EPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1)
)
ePowerSupply.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a17PowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    ePowerSupply.setStatus("mandatory")
_A17PowerSupplyIndex_Type = DmiInteger
_A17PowerSupplyIndex_Object = MibTableColumn
a17PowerSupplyIndex = _A17PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 1),
    _A17PowerSupplyIndex_Type()
)
a17PowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17PowerSupplyIndex.setStatus("mandatory")
_A17FruGroupIndex_Type = DmiInteger
_A17FruGroupIndex_Object = MibTableColumn
a17FruGroupIndex = _A17FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 2),
    _A17FruGroupIndex_Type()
)
a17FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17FruGroupIndex.setStatus("mandatory")
_A17OperationalGroupIndex_Type = DmiInteger
_A17OperationalGroupIndex_Object = MibTableColumn
a17OperationalGroupIndex = _A17OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 3),
    _A17OperationalGroupIndex_Type()
)
a17OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17OperationalGroupIndex.setStatus("mandatory")
_A17PowerUnitIndex_Type = DmiInteger
_A17PowerUnitIndex_Object = MibTableColumn
a17PowerUnitIndex = _A17PowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 4),
    _A17PowerUnitIndex_Type()
)
a17PowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17PowerUnitIndex.setStatus("mandatory")


class _A17PowerSupplyType_Type(Integer32):
    """Custom type a17PowerSupplyType based on Integer32"""
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
        *(("vBattery", 5),
          ("vConverter", 7),
          ("vLinear", 3),
          ("vOther", 1),
          ("vRegulator", 8),
          ("vSwitching", 4),
          ("vUnknown", 2),
          ("vUps", 6))
    )


_A17PowerSupplyType_Type.__name__ = "Integer32"
_A17PowerSupplyType_Object = MibTableColumn
a17PowerSupplyType = _A17PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 5),
    _A17PowerSupplyType_Type()
)
a17PowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17PowerSupplyType.setStatus("mandatory")
_A17InputVoltageCapabilityDescription_Type = DmiDisplaystring
_A17InputVoltageCapabilityDescription_Object = MibTableColumn
a17InputVoltageCapabilityDescription = _A17InputVoltageCapabilityDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 6),
    _A17InputVoltageCapabilityDescription_Type()
)
a17InputVoltageCapabilityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17InputVoltageCapabilityDescription.setStatus("mandatory")
_A17Range1InputVoltageLow_Type = DmiInteger
_A17Range1InputVoltageLow_Object = MibTableColumn
a17Range1InputVoltageLow = _A17Range1InputVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 7),
    _A17Range1InputVoltageLow_Type()
)
a17Range1InputVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range1InputVoltageLow.setStatus("mandatory")
_A17Range1InputVoltageHigh_Type = DmiInteger
_A17Range1InputVoltageHigh_Object = MibTableColumn
a17Range1InputVoltageHigh = _A17Range1InputVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 8),
    _A17Range1InputVoltageHigh_Type()
)
a17Range1InputVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range1InputVoltageHigh.setStatus("mandatory")
_A17Range1VoltageProbeIndex_Type = DmiInteger
_A17Range1VoltageProbeIndex_Object = MibTableColumn
a17Range1VoltageProbeIndex = _A17Range1VoltageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 9),
    _A17Range1VoltageProbeIndex_Type()
)
a17Range1VoltageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range1VoltageProbeIndex.setStatus("mandatory")
_A17Range1ElectricalCurrentProbeIndex_Type = DmiInteger
_A17Range1ElectricalCurrentProbeIndex_Object = MibTableColumn
a17Range1ElectricalCurrentProbeIndex = _A17Range1ElectricalCurrentProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 10),
    _A17Range1ElectricalCurrentProbeIndex_Type()
)
a17Range1ElectricalCurrentProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range1ElectricalCurrentProbeIndex.setStatus("mandatory")
_A17Range2InputVoltageLow_Type = DmiInteger
_A17Range2InputVoltageLow_Object = MibTableColumn
a17Range2InputVoltageLow = _A17Range2InputVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 11),
    _A17Range2InputVoltageLow_Type()
)
a17Range2InputVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range2InputVoltageLow.setStatus("mandatory")
_A17Range2InputVoltageHigh_Type = DmiInteger
_A17Range2InputVoltageHigh_Object = MibTableColumn
a17Range2InputVoltageHigh = _A17Range2InputVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 12),
    _A17Range2InputVoltageHigh_Type()
)
a17Range2InputVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range2InputVoltageHigh.setStatus("mandatory")
_A17Range2VoltageProbeIndex_Type = DmiInteger
_A17Range2VoltageProbeIndex_Object = MibTableColumn
a17Range2VoltageProbeIndex = _A17Range2VoltageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 13),
    _A17Range2VoltageProbeIndex_Type()
)
a17Range2VoltageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range2VoltageProbeIndex.setStatus("mandatory")
_A17Range2CurrentProbeIndex_Type = DmiInteger
_A17Range2CurrentProbeIndex_Object = MibTableColumn
a17Range2CurrentProbeIndex = _A17Range2CurrentProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 14),
    _A17Range2CurrentProbeIndex_Type()
)
a17Range2CurrentProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range2CurrentProbeIndex.setStatus("mandatory")


class _A17ActiveInputVoltageRange_Type(Integer32):
    """Custom type a17ActiveInputVoltageRange based on Integer32"""
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
        *(("vBoth", 5),
          ("vOther", 1),
          ("vRange1", 3),
          ("vRange2", 4),
          ("vUnknown", 2))
    )


_A17ActiveInputVoltageRange_Type.__name__ = "Integer32"
_A17ActiveInputVoltageRange_Object = MibTableColumn
a17ActiveInputVoltageRange = _A17ActiveInputVoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 15),
    _A17ActiveInputVoltageRange_Type()
)
a17ActiveInputVoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17ActiveInputVoltageRange.setStatus("mandatory")


class _A17InputVoltageRangeSwitching_Type(Integer32):
    """Custom type a17InputVoltageRangeSwitching based on Integer32"""
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
        *(("vAutoswitch", 4),
          ("vManual", 3),
          ("vNotApplicable", 6),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vWideRange", 5))
    )


_A17InputVoltageRangeSwitching_Type.__name__ = "Integer32"
_A17InputVoltageRangeSwitching_Object = MibTableColumn
a17InputVoltageRangeSwitching = _A17InputVoltageRangeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 16),
    _A17InputVoltageRangeSwitching_Type()
)
a17InputVoltageRangeSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17InputVoltageRangeSwitching.setStatus("mandatory")
_A17Range1InputFrequencyLow_Type = DmiInteger
_A17Range1InputFrequencyLow_Object = MibTableColumn
a17Range1InputFrequencyLow = _A17Range1InputFrequencyLow_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 17),
    _A17Range1InputFrequencyLow_Type()
)
a17Range1InputFrequencyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range1InputFrequencyLow.setStatus("mandatory")
_A17Range1InputFrequencyHigh_Type = DmiInteger
_A17Range1InputFrequencyHigh_Object = MibTableColumn
a17Range1InputFrequencyHigh = _A17Range1InputFrequencyHigh_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 18),
    _A17Range1InputFrequencyHigh_Type()
)
a17Range1InputFrequencyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range1InputFrequencyHigh.setStatus("mandatory")
_A17Range2InputFrequencyLow_Type = DmiInteger
_A17Range2InputFrequencyLow_Object = MibTableColumn
a17Range2InputFrequencyLow = _A17Range2InputFrequencyLow_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 19),
    _A17Range2InputFrequencyLow_Type()
)
a17Range2InputFrequencyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range2InputFrequencyLow.setStatus("mandatory")
_A17Range2InputFrequencyHigh_Type = DmiInteger
_A17Range2InputFrequencyHigh_Object = MibTableColumn
a17Range2InputFrequencyHigh = _A17Range2InputFrequencyHigh_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 20),
    _A17Range2InputFrequencyHigh_Type()
)
a17Range2InputFrequencyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17Range2InputFrequencyHigh.setStatus("mandatory")
_A17TotalOutputPower_Type = DmiInteger
_A17TotalOutputPower_Object = MibTableColumn
a17TotalOutputPower = _A17TotalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 17, 1, 21),
    _A17TotalOutputPower_Type()
)
a17TotalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a17TotalOutputPower.setStatus("mandatory")
_TSystemSlots_Object = MibTable
tSystemSlots = _TSystemSlots_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19)
)
if mibBuilder.loadTexts:
    tSystemSlots.setStatus("mandatory")
_ESystemSlots_Object = MibTableRow
eSystemSlots = _ESystemSlots_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1)
)
eSystemSlots.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a19SlotIndex"),
)
if mibBuilder.loadTexts:
    eSystemSlots.setStatus("mandatory")
_A19SlotIndex_Type = DmiInteger
_A19SlotIndex_Object = MibTableColumn
a19SlotIndex = _A19SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 1),
    _A19SlotIndex_Type()
)
a19SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19SlotIndex.setStatus("mandatory")
_A19SlotType_Type = DmiInteger64X
_A19SlotType_Object = MibTableColumn
a19SlotType = _A19SlotType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 3),
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
          ("vInUse", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A19CurrentUsage_Type.__name__ = "Integer32"
_A19CurrentUsage_Object = MibTableColumn
a19CurrentUsage = _A19CurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 4),
    _A19CurrentUsage_Type()
)
a19CurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19CurrentUsage.setStatus("mandatory")
_A19SlotDescription_Type = DmiDisplaystring
_A19SlotDescription_Object = MibTableColumn
a19SlotDescription = _A19SlotDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 5),
    _A19SlotDescription_Type()
)
a19SlotDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19SlotDescription.setStatus("mandatory")


class _A19SlotCategory_Type(Integer32):
    """Custom type a19SlotCategory based on Integer32"""
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
        *(("vBusConnector", 3),
          ("vMotherboard", 5),
          ("vOther", 1),
          ("vPcmciaSlot", 4),
          ("vUnknown", 2))
    )


_A19SlotCategory_Type.__name__ = "Integer32"
_A19SlotCategory_Object = MibTableColumn
a19SlotCategory = _A19SlotCategory_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 6),
    _A19SlotCategory_Type()
)
a19SlotCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19SlotCategory.setStatus("mandatory")


class _A19VirtualSlot_Type(Integer32):
    """Custom type a19VirtualSlot based on Integer32"""
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


_A19VirtualSlot_Type.__name__ = "Integer32"
_A19VirtualSlot_Object = MibTableColumn
a19VirtualSlot = _A19VirtualSlot_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 7),
    _A19VirtualSlot_Type()
)
a19VirtualSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19VirtualSlot.setStatus("mandatory")
_A19ResourceUserId_Type = DmiInteger
_A19ResourceUserId_Object = MibTableColumn
a19ResourceUserId = _A19ResourceUserId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 19, 1, 8),
    _A19ResourceUserId_Type()
)
a19ResourceUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a19ResourceUserId.setStatus("mandatory")
_TFieldReplaceableUnit_Object = MibTable
tFieldReplaceableUnit = _TFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30)
)
if mibBuilder.loadTexts:
    tFieldReplaceableUnit.setStatus("mandatory")
_EFieldReplaceableUnit_Object = MibTableRow
eFieldReplaceableUnit = _EFieldReplaceableUnit_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1)
)
eFieldReplaceableUnit.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a30FruIndex"),
)
if mibBuilder.loadTexts:
    eFieldReplaceableUnit.setStatus("mandatory")
_A30FruIndex_Type = DmiInteger
_A30FruIndex_Object = MibTableColumn
a30FruIndex = _A30FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 1),
    _A30FruIndex_Type()
)
a30FruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30FruIndex.setStatus("mandatory")
_A30DeviceGroupIndex_Type = DmiInteger
_A30DeviceGroupIndex_Object = MibTableColumn
a30DeviceGroupIndex = _A30DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 2),
    _A30DeviceGroupIndex_Type()
)
a30DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30DeviceGroupIndex.setStatus("mandatory")
_A30Description_Type = DmiDisplaystring
_A30Description_Object = MibTableColumn
a30Description = _A30Description_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 3),
    _A30Description_Type()
)
a30Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30Description.setStatus("mandatory")
_A30Manufacturer_Type = DmiDisplaystring
_A30Manufacturer_Object = MibTableColumn
a30Manufacturer = _A30Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 4),
    _A30Manufacturer_Type()
)
a30Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30Manufacturer.setStatus("mandatory")
_A30Model_Type = DmiDisplaystring
_A30Model_Object = MibTableColumn
a30Model = _A30Model_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 5),
    _A30Model_Type()
)
a30Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30Model.setStatus("mandatory")
_A30PartNumber_Type = DmiDisplaystring
_A30PartNumber_Object = MibTableColumn
a30PartNumber = _A30PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 6),
    _A30PartNumber_Type()
)
a30PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30PartNumber.setStatus("mandatory")
_A30FruSerialNumber_Type = DmiDisplaystring
_A30FruSerialNumber_Object = MibTableColumn
a30FruSerialNumber = _A30FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 7),
    _A30FruSerialNumber_Type()
)
a30FruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30FruSerialNumber.setStatus("mandatory")
_A30RevisionLevel_Type = DmiDisplaystring
_A30RevisionLevel_Object = MibTableColumn
a30RevisionLevel = _A30RevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 8),
    _A30RevisionLevel_Type()
)
a30RevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30RevisionLevel.setStatus("mandatory")
_A30WarrantyStartDate_Type = DmiDateX
_A30WarrantyStartDate_Object = MibTableColumn
a30WarrantyStartDate = _A30WarrantyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 9),
    _A30WarrantyStartDate_Type()
)
a30WarrantyStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30WarrantyStartDate.setStatus("mandatory")
_A30WarrantyDuration_Type = DmiInteger
_A30WarrantyDuration_Object = MibTableColumn
a30WarrantyDuration = _A30WarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 10),
    _A30WarrantyDuration_Type()
)
a30WarrantyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30WarrantyDuration.setStatus("mandatory")
_A30SupportPhoneNumber_Type = DmiDisplaystring
_A30SupportPhoneNumber_Object = MibTableColumn
a30SupportPhoneNumber = _A30SupportPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 11),
    _A30SupportPhoneNumber_Type()
)
a30SupportPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30SupportPhoneNumber.setStatus("mandatory")
_A30FruInternetUniformResourceLocator_Type = DmiDisplaystring
_A30FruInternetUniformResourceLocator_Object = MibTableColumn
a30FruInternetUniformResourceLocator = _A30FruInternetUniformResourceLocator_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 30, 1, 12),
    _A30FruInternetUniformResourceLocator_Type()
)
a30FruInternetUniformResourceLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a30FruInternetUniformResourceLocator.setStatus("mandatory")
_TOperationalState_Object = MibTable
tOperationalState = _TOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31)
)
if mibBuilder.loadTexts:
    tOperationalState.setStatus("mandatory")
_EOperationalState_Object = MibTableRow
eOperationalState = _EOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1)
)
eOperationalState.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a31OperationalStateInstanceIndex"),
)
if mibBuilder.loadTexts:
    eOperationalState.setStatus("mandatory")
_A31OperationalStateInstanceIndex_Type = DmiInteger
_A31OperationalStateInstanceIndex_Object = MibTableColumn
a31OperationalStateInstanceIndex = _A31OperationalStateInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 1),
    _A31OperationalStateInstanceIndex_Type()
)
a31OperationalStateInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31OperationalStateInstanceIndex.setStatus("mandatory")
_A31DeviceGroupIndex_Type = DmiInteger
_A31DeviceGroupIndex_Object = MibTableColumn
a31DeviceGroupIndex = _A31DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 3),
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
          ("vNotApplicable", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A31UsageState_Type.__name__ = "Integer32"
_A31UsageState_Object = MibTableColumn
a31UsageState = _A31UsageState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 6),
    _A31AdministrativeState_Type()
)
a31AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31AdministrativeState.setStatus("mandatory")
_A31FatalErrorCount_Type = DmiCounter
_A31FatalErrorCount_Object = MibTableColumn
a31FatalErrorCount = _A31FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 7),
    _A31FatalErrorCount_Type()
)
a31FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31FatalErrorCount.setStatus("mandatory")
_A31MajorErrorCount_Type = DmiCounter
_A31MajorErrorCount_Object = MibTableColumn
a31MajorErrorCount = _A31MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 8),
    _A31MajorErrorCount_Type()
)
a31MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31MajorErrorCount.setStatus("mandatory")
_A31WarningErrorCount_Type = DmiCounter
_A31WarningErrorCount_Object = MibTableColumn
a31WarningErrorCount = _A31WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 9),
    _A31WarningErrorCount_Type()
)
a31WarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31WarningErrorCount.setStatus("mandatory")


class _A31CurrentErrorStatus_Type(Integer32):
    """Custom type a31CurrentErrorStatus based on Integer32"""
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
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A31CurrentErrorStatus_Type.__name__ = "Integer32"
_A31CurrentErrorStatus_Object = MibTableColumn
a31CurrentErrorStatus = _A31CurrentErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 31, 1, 10),
    _A31CurrentErrorStatus_Type()
)
a31CurrentErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a31CurrentErrorStatus.setStatus("mandatory")
_TPhysicalMemoryArray_Object = MibTable
tPhysicalMemoryArray = _TPhysicalMemoryArray_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34)
)
if mibBuilder.loadTexts:
    tPhysicalMemoryArray.setStatus("mandatory")
_EPhysicalMemoryArray_Object = MibTableRow
ePhysicalMemoryArray = _EPhysicalMemoryArray_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1)
)
ePhysicalMemoryArray.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a34MemoryArrayTableIndex"),
)
if mibBuilder.loadTexts:
    ePhysicalMemoryArray.setStatus("mandatory")
_A34MemoryArrayTableIndex_Type = DmiInteger
_A34MemoryArrayTableIndex_Object = MibTableColumn
a34MemoryArrayTableIndex = _A34MemoryArrayTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 1),
    _A34MemoryArrayTableIndex_Type()
)
a34MemoryArrayTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34MemoryArrayTableIndex.setStatus("mandatory")


class _A34MemoryArrayLocation_Type(Integer32):
    """Custom type a34MemoryArrayLocation based on Integer32"""
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
              16,
              160,
              161,
              162,
              163,
              164)
        )
    )
    namedValues = NamedValues(
        *(("vEisaAdd-onCard", 5),
          ("vIsaAdd-onCard", 4),
          ("vMcaAdd-onCard", 7),
          ("vNubus", 16),
          ("vOther", 1),
          ("vPc-98c20Add-onCard", 160),
          ("vPc-98c24Add-onCard", 161),
          ("vPc-98cardSlotAdd-onCard", 164),
          ("vPc-98eAdd-onCard", 162),
          ("vPc-98localBusAdd-onCard", 163),
          ("vPciAdd-onCard", 6),
          ("vPcmciaAdd-onCard", 8),
          ("vProprietaryAdd-onCard", 9),
          ("vSystemBoardOrMotherboard", 3),
          ("vUnknown", 2))
    )


_A34MemoryArrayLocation_Type.__name__ = "Integer32"
_A34MemoryArrayLocation_Object = MibTableColumn
a34MemoryArrayLocation = _A34MemoryArrayLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 2),
    _A34MemoryArrayLocation_Type()
)
a34MemoryArrayLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34MemoryArrayLocation.setStatus("mandatory")


class _A34MemoryArrayUse_Type(Integer32):
    """Custom type a34MemoryArrayUse based on Integer32"""
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
        *(("vCacheMemory", 7),
          ("vFlashMemory", 5),
          ("vNonVolatileRam", 6),
          ("vOther", 1),
          ("vSystemMemory", 3),
          ("vUnknown", 2),
          ("vVideoMemory", 4))
    )


_A34MemoryArrayUse_Type.__name__ = "Integer32"
_A34MemoryArrayUse_Object = MibTableColumn
a34MemoryArrayUse = _A34MemoryArrayUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 3),
    _A34MemoryArrayUse_Type()
)
a34MemoryArrayUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34MemoryArrayUse.setStatus("mandatory")
_A34MaximumMemoryCapacity_Type = DmiInteger
_A34MaximumMemoryCapacity_Object = MibTableColumn
a34MaximumMemoryCapacity = _A34MaximumMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 4),
    _A34MaximumMemoryCapacity_Type()
)
a34MaximumMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34MaximumMemoryCapacity.setStatus("mandatory")
_A34NumberOfMemoryDeviceSockets_Type = DmiInteger
_A34NumberOfMemoryDeviceSockets_Object = MibTableColumn
a34NumberOfMemoryDeviceSockets = _A34NumberOfMemoryDeviceSockets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 5),
    _A34NumberOfMemoryDeviceSockets_Type()
)
a34NumberOfMemoryDeviceSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34NumberOfMemoryDeviceSockets.setStatus("mandatory")
_A34NumberOfMemoryDeviceSocketsUsed_Type = DmiInteger
_A34NumberOfMemoryDeviceSocketsUsed_Object = MibTableColumn
a34NumberOfMemoryDeviceSocketsUsed = _A34NumberOfMemoryDeviceSocketsUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 6),
    _A34NumberOfMemoryDeviceSocketsUsed_Type()
)
a34NumberOfMemoryDeviceSocketsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34NumberOfMemoryDeviceSocketsUsed.setStatus("mandatory")


class _A34MemoryErrorCorrection_Type(Integer32):
    """Custom type a34MemoryErrorCorrection based on Integer32"""
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
        *(("vCrc", 7),
          ("vMultibitEcc", 6),
          ("vNone", 3),
          ("vOther", 1),
          ("vParity", 4),
          ("vSingleBitEcc", 5),
          ("vUnknown", 2))
    )


_A34MemoryErrorCorrection_Type.__name__ = "Integer32"
_A34MemoryErrorCorrection_Object = MibTableColumn
a34MemoryErrorCorrection = _A34MemoryErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 7),
    _A34MemoryErrorCorrection_Type()
)
a34MemoryErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34MemoryErrorCorrection.setStatus("mandatory")


class _A34ArrayErrorType_Type(Integer32):
    """Custom type a34ArrayErrorType based on Integer32"""
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
        *(("vBadRead", 4),
          ("vChecksumError", 10),
          ("vCorrectedError", 13),
          ("vCorrectedSingle-bitError", 12),
          ("vCrcError", 11),
          ("vDouble-bitError", 7),
          ("vMulti-bitError", 8),
          ("vNibbleError", 9),
          ("vOk", 3),
          ("vOther", 1),
          ("vParityError", 5),
          ("vSingle-bitError", 6),
          ("vUncorrectableError", 14),
          ("vUnknown", 2))
    )


_A34ArrayErrorType_Type.__name__ = "Integer32"
_A34ArrayErrorType_Object = MibTableColumn
a34ArrayErrorType = _A34ArrayErrorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 8),
    _A34ArrayErrorType_Type()
)
a34ArrayErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34ArrayErrorType.setStatus("mandatory")


class _A34LastErrorUpdate_Type(Integer32):
    """Custom type a34LastErrorUpdate based on Integer32"""
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
        *(("vNoUpdateSinceLastInstrumentationStart", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vUpdatedDuringInstrumentationRun-time", 5),
          ("vUpdatedFromInformationObtainedPriorToIn", 4))
    )


_A34LastErrorUpdate_Type.__name__ = "Integer32"
_A34LastErrorUpdate_Object = MibTableColumn
a34LastErrorUpdate = _A34LastErrorUpdate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 9),
    _A34LastErrorUpdate_Type()
)
a34LastErrorUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34LastErrorUpdate.setStatus("mandatory")


class _A34ErrorOperation_Type(Integer32):
    """Custom type a34ErrorOperation based on Integer32"""
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
          ("vPartialWrite", 5),
          ("vRead", 3),
          ("vUnknown", 2),
          ("vWrite", 4))
    )


_A34ErrorOperation_Type.__name__ = "Integer32"
_A34ErrorOperation_Object = MibTableColumn
a34ErrorOperation = _A34ErrorOperation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 10),
    _A34ErrorOperation_Type()
)
a34ErrorOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34ErrorOperation.setStatus("mandatory")
_A34ErrorDataSize_Type = DmiInteger
_A34ErrorDataSize_Object = MibTableColumn
a34ErrorDataSize = _A34ErrorDataSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 11),
    _A34ErrorDataSize_Type()
)
a34ErrorDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34ErrorDataSize.setStatus("mandatory")
_A34ErrorData_Type = DmiOctetstring
_A34ErrorData_Object = MibTableColumn
a34ErrorData = _A34ErrorData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 12),
    _A34ErrorData_Type()
)
a34ErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34ErrorData.setStatus("mandatory")
_A34VendorSyndrome_Type = DmiOctetstring
_A34VendorSyndrome_Object = MibTableColumn
a34VendorSyndrome = _A34VendorSyndrome_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 13),
    _A34VendorSyndrome_Type()
)
a34VendorSyndrome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34VendorSyndrome.setStatus("mandatory")
_A34ErrorAddress_Type = DmiInteger64X
_A34ErrorAddress_Object = MibTableColumn
a34ErrorAddress = _A34ErrorAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 14),
    _A34ErrorAddress_Type()
)
a34ErrorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34ErrorAddress.setStatus("mandatory")
_A34ErrorResolution_Type = DmiInteger
_A34ErrorResolution_Object = MibTableColumn
a34ErrorResolution = _A34ErrorResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 15),
    _A34ErrorResolution_Type()
)
a34ErrorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34ErrorResolution.setStatus("mandatory")
_A34FruGroupIndex_Type = DmiInteger
_A34FruGroupIndex_Object = MibTableColumn
a34FruGroupIndex = _A34FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 16),
    _A34FruGroupIndex_Type()
)
a34FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34FruGroupIndex.setStatus("mandatory")
_A34OperationalGroupIndex_Type = DmiInteger
_A34OperationalGroupIndex_Object = MibTableColumn
a34OperationalGroupIndex = _A34OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 34, 1, 17),
    _A34OperationalGroupIndex_Type()
)
a34OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a34OperationalGroupIndex.setStatus("mandatory")
_TMemoryArrayMappedAddresses_Object = MibTable
tMemoryArrayMappedAddresses = _TMemoryArrayMappedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35)
)
if mibBuilder.loadTexts:
    tMemoryArrayMappedAddresses.setStatus("mandatory")
_EMemoryArrayMappedAddresses_Object = MibTableRow
eMemoryArrayMappedAddresses = _EMemoryArrayMappedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1)
)
eMemoryArrayMappedAddresses.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a35MemoryArrayMappedAddressesTableIndex"),
)
if mibBuilder.loadTexts:
    eMemoryArrayMappedAddresses.setStatus("mandatory")
_A35MemoryArrayMappedAddressesTableIndex_Type = DmiInteger
_A35MemoryArrayMappedAddressesTableIndex_Object = MibTableColumn
a35MemoryArrayMappedAddressesTableIndex = _A35MemoryArrayMappedAddressesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1, 1),
    _A35MemoryArrayMappedAddressesTableIndex_Type()
)
a35MemoryArrayMappedAddressesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35MemoryArrayMappedAddressesTableIndex.setStatus("mandatory")
_A35MemoryArrayIndex_Type = DmiInteger
_A35MemoryArrayIndex_Object = MibTableColumn
a35MemoryArrayIndex = _A35MemoryArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1, 2),
    _A35MemoryArrayIndex_Type()
)
a35MemoryArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35MemoryArrayIndex.setStatus("mandatory")
_A35MappedRangeStartingAddress_Type = DmiInteger
_A35MappedRangeStartingAddress_Object = MibTableColumn
a35MappedRangeStartingAddress = _A35MappedRangeStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1, 3),
    _A35MappedRangeStartingAddress_Type()
)
a35MappedRangeStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35MappedRangeStartingAddress.setStatus("mandatory")
_A35MappedRangeEndingAddress_Type = DmiInteger
_A35MappedRangeEndingAddress_Object = MibTableColumn
a35MappedRangeEndingAddress = _A35MappedRangeEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1, 4),
    _A35MappedRangeEndingAddress_Type()
)
a35MappedRangeEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35MappedRangeEndingAddress.setStatus("mandatory")
_A35PartitionId_Type = DmiInteger
_A35PartitionId_Object = MibTableColumn
a35PartitionId = _A35PartitionId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1, 5),
    _A35PartitionId_Type()
)
a35PartitionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35PartitionId.setStatus("mandatory")
_A35PartitionWidth_Type = DmiInteger
_A35PartitionWidth_Object = MibTableColumn
a35PartitionWidth = _A35PartitionWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1, 6),
    _A35PartitionWidth_Type()
)
a35PartitionWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35PartitionWidth.setStatus("mandatory")
_A35OperationalGroupIndex_Type = DmiInteger
_A35OperationalGroupIndex_Object = MibTableColumn
a35OperationalGroupIndex = _A35OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 35, 1, 7),
    _A35OperationalGroupIndex_Type()
)
a35OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a35OperationalGroupIndex.setStatus("mandatory")
_TMemoryDevice_Object = MibTable
tMemoryDevice = _TMemoryDevice_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36)
)
if mibBuilder.loadTexts:
    tMemoryDevice.setStatus("mandatory")
_EMemoryDevice_Object = MibTableRow
eMemoryDevice = _EMemoryDevice_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1)
)
eMemoryDevice.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a36MemoryDeviceTableIndex"),
)
if mibBuilder.loadTexts:
    eMemoryDevice.setStatus("mandatory")
_A36MemoryDeviceTableIndex_Type = DmiInteger
_A36MemoryDeviceTableIndex_Object = MibTableColumn
a36MemoryDeviceTableIndex = _A36MemoryDeviceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 1),
    _A36MemoryDeviceTableIndex_Type()
)
a36MemoryDeviceTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36MemoryDeviceTableIndex.setStatus("mandatory")
_A36MemoryArrayIndex_Type = DmiInteger
_A36MemoryArrayIndex_Object = MibTableColumn
a36MemoryArrayIndex = _A36MemoryArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 2),
    _A36MemoryArrayIndex_Type()
)
a36MemoryArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36MemoryArrayIndex.setStatus("mandatory")
_A36DeviceLocator_Type = DmiDisplaystring
_A36DeviceLocator_Object = MibTableColumn
a36DeviceLocator = _A36DeviceLocator_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 3),
    _A36DeviceLocator_Type()
)
a36DeviceLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DeviceLocator.setStatus("mandatory")
_A36BankLocator_Type = DmiDisplaystring
_A36BankLocator_Object = MibTableColumn
a36BankLocator = _A36BankLocator_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 4),
    _A36BankLocator_Type()
)
a36BankLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36BankLocator.setStatus("mandatory")
_A36Size_Type = DmiInteger
_A36Size_Object = MibTableColumn
a36Size = _A36Size_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 5),
    _A36Size_Type()
)
a36Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36Size.setStatus("mandatory")


class _A36FormFactor_Type(Integer32):
    """Custom type a36FormFactor based on Integer32"""
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
        *(("vChip", 5),
          ("vDimm", 9),
          ("vDip", 6),
          ("vOther", 1),
          ("vProprietaryCard", 8),
          ("vRowOfChips", 11),
          ("vSimm", 3),
          ("vSip", 4),
          ("vTsop", 10),
          ("vUnknown", 2),
          ("vZip", 7))
    )


_A36FormFactor_Type.__name__ = "Integer32"
_A36FormFactor_Object = MibTableColumn
a36FormFactor = _A36FormFactor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 6),
    _A36FormFactor_Type()
)
a36FormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36FormFactor.setStatus("mandatory")
_A36TotalWidth_Type = DmiInteger
_A36TotalWidth_Object = MibTableColumn
a36TotalWidth = _A36TotalWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 7),
    _A36TotalWidth_Type()
)
a36TotalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36TotalWidth.setStatus("mandatory")
_A36DataWidth_Type = DmiInteger
_A36DataWidth_Object = MibTableColumn
a36DataWidth = _A36DataWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 8),
    _A36DataWidth_Type()
)
a36DataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DataWidth.setStatus("mandatory")


class _A36MemoryType_Type(Integer32):
    """Custom type a36MemoryType based on Integer32"""
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
        *(("vDram", 3),
          ("vEdram", 4),
          ("vEeprom", 10),
          ("vEprom", 12),
          ("vFeprom", 11),
          ("vFlash", 9),
          ("vOther", 1),
          ("vRam", 7),
          ("vRom", 8),
          ("vSram", 6),
          ("vUnknown", 2),
          ("vVram", 5))
    )


_A36MemoryType_Type.__name__ = "Integer32"
_A36MemoryType_Object = MibTableColumn
a36MemoryType = _A36MemoryType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 9),
    _A36MemoryType_Type()
)
a36MemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36MemoryType.setStatus("mandatory")


class _A36TypeDetail_Type(Integer32):
    """Custom type a36TypeDetail based on Integer32"""
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
        *(("vCacheDram", 11),
          ("vCmos", 8),
          ("vEdo", 9),
          ("vFastPaged", 3),
          ("vNon-volatile", 12),
          ("vOther", 1),
          ("vPseudo-static", 5),
          ("vRambus", 6),
          ("vStaticColumn", 4),
          ("vSynchronous", 7),
          ("vUnknown", 2),
          ("vWindowDram", 10))
    )


_A36TypeDetail_Type.__name__ = "Integer32"
_A36TypeDetail_Object = MibTableColumn
a36TypeDetail = _A36TypeDetail_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 10),
    _A36TypeDetail_Type()
)
a36TypeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36TypeDetail.setStatus("mandatory")
_A36DeviceSet_Type = DmiInteger
_A36DeviceSet_Object = MibTableColumn
a36DeviceSet = _A36DeviceSet_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 11),
    _A36DeviceSet_Type()
)
a36DeviceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DeviceSet.setStatus("mandatory")


class _A36DeviceErrorType_Type(Integer32):
    """Custom type a36DeviceErrorType based on Integer32"""
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
        *(("vBadRead", 4),
          ("vChecksumError", 10),
          ("vCorrectedError", 13),
          ("vCorrectedSingle-bitError", 12),
          ("vCrcError", 11),
          ("vDouble-bitError", 7),
          ("vMulti-bitError", 8),
          ("vNibbleError", 9),
          ("vOk", 3),
          ("vOther", 1),
          ("vParityError", 5),
          ("vSingle-bitError", 6),
          ("vUncorrectableError", 14),
          ("vUnknown", 2))
    )


_A36DeviceErrorType_Type.__name__ = "Integer32"
_A36DeviceErrorType_Object = MibTableColumn
a36DeviceErrorType = _A36DeviceErrorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 12),
    _A36DeviceErrorType_Type()
)
a36DeviceErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DeviceErrorType.setStatus("mandatory")


class _A36ErrorGranularity_Type(Integer32):
    """Custom type a36ErrorGranularity based on Integer32"""
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
        *(("vDeviceLevel", 3),
          ("vMemoryPartitionLevel", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A36ErrorGranularity_Type.__name__ = "Integer32"
_A36ErrorGranularity_Object = MibTableColumn
a36ErrorGranularity = _A36ErrorGranularity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 13),
    _A36ErrorGranularity_Type()
)
a36ErrorGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36ErrorGranularity.setStatus("mandatory")


class _A36LastErrorUpdate_Type(Integer32):
    """Custom type a36LastErrorUpdate based on Integer32"""
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
        *(("vNoUpdateSinceLastInstrumentationStart", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vUpdatedDuringInstrumentationRun-time", 5),
          ("vUpdatedFromInformationObtainedPriorToIn", 4))
    )


_A36LastErrorUpdate_Type.__name__ = "Integer32"
_A36LastErrorUpdate_Object = MibTableColumn
a36LastErrorUpdate = _A36LastErrorUpdate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 14),
    _A36LastErrorUpdate_Type()
)
a36LastErrorUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36LastErrorUpdate.setStatus("mandatory")


class _A36ErrorOperation_Type(Integer32):
    """Custom type a36ErrorOperation based on Integer32"""
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
          ("vPartialWrite", 5),
          ("vRead", 3),
          ("vUnknown", 2),
          ("vWrite", 4))
    )


_A36ErrorOperation_Type.__name__ = "Integer32"
_A36ErrorOperation_Object = MibTableColumn
a36ErrorOperation = _A36ErrorOperation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 15),
    _A36ErrorOperation_Type()
)
a36ErrorOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36ErrorOperation.setStatus("mandatory")
_A36ErrorDataSize_Type = DmiInteger
_A36ErrorDataSize_Object = MibTableColumn
a36ErrorDataSize = _A36ErrorDataSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 16),
    _A36ErrorDataSize_Type()
)
a36ErrorDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36ErrorDataSize.setStatus("mandatory")
_A36ErrorData_Type = DmiOctetstring
_A36ErrorData_Object = MibTableColumn
a36ErrorData = _A36ErrorData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 17),
    _A36ErrorData_Type()
)
a36ErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36ErrorData.setStatus("mandatory")
_A36VendorSyndrome_Type = DmiOctetstring
_A36VendorSyndrome_Object = MibTableColumn
a36VendorSyndrome = _A36VendorSyndrome_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 18),
    _A36VendorSyndrome_Type()
)
a36VendorSyndrome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36VendorSyndrome.setStatus("mandatory")
_A36DeviceErrorAddress_Type = DmiInteger
_A36DeviceErrorAddress_Object = MibTableColumn
a36DeviceErrorAddress = _A36DeviceErrorAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 19),
    _A36DeviceErrorAddress_Type()
)
a36DeviceErrorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36DeviceErrorAddress.setStatus("mandatory")
_A36ArrayErrorAddress_Type = DmiInteger
_A36ArrayErrorAddress_Object = MibTableColumn
a36ArrayErrorAddress = _A36ArrayErrorAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 20),
    _A36ArrayErrorAddress_Type()
)
a36ArrayErrorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36ArrayErrorAddress.setStatus("mandatory")
_A36ErrorResolution_Type = DmiInteger
_A36ErrorResolution_Object = MibTableColumn
a36ErrorResolution = _A36ErrorResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 21),
    _A36ErrorResolution_Type()
)
a36ErrorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36ErrorResolution.setStatus("mandatory")
_A36FruGroupIndex_Type = DmiInteger
_A36FruGroupIndex_Object = MibTableColumn
a36FruGroupIndex = _A36FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 22),
    _A36FruGroupIndex_Type()
)
a36FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36FruGroupIndex.setStatus("mandatory")
_A36OperationalGroupIndex_Type = DmiInteger
_A36OperationalGroupIndex_Object = MibTableColumn
a36OperationalGroupIndex = _A36OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 36, 1, 23),
    _A36OperationalGroupIndex_Type()
)
a36OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a36OperationalGroupIndex.setStatus("mandatory")
_TMemoryDeviceMappedAddresses_Object = MibTable
tMemoryDeviceMappedAddresses = _TMemoryDeviceMappedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37)
)
if mibBuilder.loadTexts:
    tMemoryDeviceMappedAddresses.setStatus("mandatory")
_EMemoryDeviceMappedAddresses_Object = MibTableRow
eMemoryDeviceMappedAddresses = _EMemoryDeviceMappedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1)
)
eMemoryDeviceMappedAddresses.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a37MemoryDeviceMappedAddressesTableIndex"),
)
if mibBuilder.loadTexts:
    eMemoryDeviceMappedAddresses.setStatus("mandatory")
_A37MemoryDeviceMappedAddressesTableIndex_Type = DmiInteger
_A37MemoryDeviceMappedAddressesTableIndex_Object = MibTableColumn
a37MemoryDeviceMappedAddressesTableIndex = _A37MemoryDeviceMappedAddressesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 1),
    _A37MemoryDeviceMappedAddressesTableIndex_Type()
)
a37MemoryDeviceMappedAddressesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37MemoryDeviceMappedAddressesTableIndex.setStatus("mandatory")
_A37MemoryDeviceSetId_Type = DmiInteger
_A37MemoryDeviceSetId_Object = MibTableColumn
a37MemoryDeviceSetId = _A37MemoryDeviceSetId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 2),
    _A37MemoryDeviceSetId_Type()
)
a37MemoryDeviceSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37MemoryDeviceSetId.setStatus("mandatory")
_A37Partition_Type = DmiInteger
_A37Partition_Object = MibTableColumn
a37Partition = _A37Partition_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 3),
    _A37Partition_Type()
)
a37Partition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37Partition.setStatus("mandatory")
_A37MappedRangeStartingAddress_Type = DmiInteger
_A37MappedRangeStartingAddress_Object = MibTableColumn
a37MappedRangeStartingAddress = _A37MappedRangeStartingAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 4),
    _A37MappedRangeStartingAddress_Type()
)
a37MappedRangeStartingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37MappedRangeStartingAddress.setStatus("mandatory")
_A37MappedRangeEndingAddress_Type = DmiInteger
_A37MappedRangeEndingAddress_Object = MibTableColumn
a37MappedRangeEndingAddress = _A37MappedRangeEndingAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 5),
    _A37MappedRangeEndingAddress_Type()
)
a37MappedRangeEndingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37MappedRangeEndingAddress.setStatus("mandatory")
_A37PartitionRowPosition_Type = DmiInteger
_A37PartitionRowPosition_Object = MibTableColumn
a37PartitionRowPosition = _A37PartitionRowPosition_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 6),
    _A37PartitionRowPosition_Type()
)
a37PartitionRowPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37PartitionRowPosition.setStatus("mandatory")
_A37InterleavePosition_Type = DmiInteger
_A37InterleavePosition_Object = MibTableColumn
a37InterleavePosition = _A37InterleavePosition_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 7),
    _A37InterleavePosition_Type()
)
a37InterleavePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37InterleavePosition.setStatus("mandatory")
_A37DataDepth_Type = DmiInteger
_A37DataDepth_Object = MibTableColumn
a37DataDepth = _A37DataDepth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 37, 1, 8),
    _A37DataDepth_Type()
)
a37DataDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a37DataDepth.setStatus("mandatory")
_TSystemHardwareSecurity_Object = MibTable
tSystemHardwareSecurity = _TSystemHardwareSecurity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 50)
)
if mibBuilder.loadTexts:
    tSystemHardwareSecurity.setStatus("mandatory")
_ESystemHardwareSecurity_Object = MibTableRow
eSystemHardwareSecurity = _ESystemHardwareSecurity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 50, 1)
)
eSystemHardwareSecurity.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSystemHardwareSecurity.setStatus("mandatory")


class _A50Power_onPasswordStatus_Type(Integer32):
    """Custom type a50Power_onPasswordStatus based on Integer32"""
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
        *(("vDisabled", 3),
          ("vEnabled", 4),
          ("vNotImplemented", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A50Power_onPasswordStatus_Type.__name__ = "Integer32"
_A50Power_onPasswordStatus_Object = MibScalar
a50Power_onPasswordStatus = _A50Power_onPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 50, 1, 1),
    _A50Power_onPasswordStatus_Type()
)
a50Power_onPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a50Power_onPasswordStatus.setStatus("mandatory")


class _A50KeyboardPasswordStatus_Type(Integer32):
    """Custom type a50KeyboardPasswordStatus based on Integer32"""
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
        *(("vDisabled", 3),
          ("vEnabled", 4),
          ("vNotImplemented", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A50KeyboardPasswordStatus_Type.__name__ = "Integer32"
_A50KeyboardPasswordStatus_Object = MibTableColumn
a50KeyboardPasswordStatus = _A50KeyboardPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 50, 1, 2),
    _A50KeyboardPasswordStatus_Type()
)
a50KeyboardPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a50KeyboardPasswordStatus.setStatus("mandatory")


class _A50AdministratorPasswordStatus_Type(Integer32):
    """Custom type a50AdministratorPasswordStatus based on Integer32"""
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
        *(("vDisabled", 3),
          ("vEnabled", 4),
          ("vNotImplemented", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A50AdministratorPasswordStatus_Type.__name__ = "Integer32"
_A50AdministratorPasswordStatus_Object = MibTableColumn
a50AdministratorPasswordStatus = _A50AdministratorPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 50, 1, 3),
    _A50AdministratorPasswordStatus_Type()
)
a50AdministratorPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a50AdministratorPasswordStatus.setStatus("mandatory")


class _A50FrontPanelResetStatus_Type(Integer32):
    """Custom type a50FrontPanelResetStatus based on Integer32"""
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
        *(("vDisabled", 3),
          ("vEnabled", 4),
          ("vNotImplemented", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A50FrontPanelResetStatus_Type.__name__ = "Integer32"
_A50FrontPanelResetStatus_Object = MibTableColumn
a50FrontPanelResetStatus = _A50FrontPanelResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 50, 1, 4),
    _A50FrontPanelResetStatus_Type()
)
a50FrontPanelResetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a50FrontPanelResetStatus.setStatus("mandatory")
_TSystemPowerControls_Object = MibTable
tSystemPowerControls = _TSystemPowerControls_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 52)
)
if mibBuilder.loadTexts:
    tSystemPowerControls.setStatus("mandatory")
_ESystemPowerControls_Object = MibTableRow
eSystemPowerControls = _ESystemPowerControls_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 52, 1)
)
eSystemPowerControls.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSystemPowerControls.setStatus("mandatory")


class _A52PowerControlRequest_Type(Integer32):
    """Custom type a52PowerControlRequest based on Integer32"""
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
        *(("vEnterHibernationMode", 7),
          ("vEnterStandbyMode", 5),
          ("vEnterSuspendMode", 6),
          ("vOther", 1),
          ("vPowerOff", 3),
          ("vPowerOffThenOnAgain", 4),
          ("vUnknown", 2))
    )


_A52PowerControlRequest_Type.__name__ = "Integer32"
_A52PowerControlRequest_Object = MibTableColumn
a52PowerControlRequest = _A52PowerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 52, 1, 1),
    _A52PowerControlRequest_Type()
)
a52PowerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a52PowerControlRequest.setStatus("mandatory")


class _A52TimedPower_onAvailable_Type(Integer32):
    """Custom type a52TimedPower_onAvailable based on Integer32"""
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


_A52TimedPower_onAvailable_Type.__name__ = "Integer32"
_A52TimedPower_onAvailable_Object = MibScalar
a52TimedPower_onAvailable = _A52TimedPower_onAvailable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 52, 1, 2),
    _A52TimedPower_onAvailable_Type()
)
a52TimedPower_onAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a52TimedPower_onAvailable.setStatus("mandatory")
_A52TimeToNextScheduledPower_on_Type = DmiInteger
_A52TimeToNextScheduledPower_on_Object = MibScalar
a52TimeToNextScheduledPower_on = _A52TimeToNextScheduledPower_on_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 52, 1, 3),
    _A52TimeToNextScheduledPower_on_Type()
)
a52TimeToNextScheduledPower_on.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a52TimeToNextScheduledPower_on.setStatus("mandatory")
_TVoltageProbe_Object = MibTable
tVoltageProbe = _TVoltageProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54)
)
if mibBuilder.loadTexts:
    tVoltageProbe.setStatus("mandatory")
_EVoltageProbe_Object = MibTableRow
eVoltageProbe = _EVoltageProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1)
)
eVoltageProbe.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"),
)
if mibBuilder.loadTexts:
    eVoltageProbe.setStatus("mandatory")
_A54VoltageProbeIndex_Type = DmiInteger
_A54VoltageProbeIndex_Object = MibTableColumn
a54VoltageProbeIndex = _A54VoltageProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 1),
    _A54VoltageProbeIndex_Type()
)
a54VoltageProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54VoltageProbeIndex.setStatus("mandatory")


class _A54VoltageProbeLocation_Type(Integer32):
    """Custom type a54VoltageProbeLocation based on Integer32"""
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
        *(("vAdd-inCard", 11),
          ("vDisk", 4),
          ("vMemoryModule", 8),
          ("vMotherboard", 7),
          ("vOther", 1),
          ("vPeripheralBay", 5),
          ("vPowerUnit", 10),
          ("vProcessor", 3),
          ("vProcessorModule", 9),
          ("vSystemManagementModule", 6),
          ("vUnknown", 2))
    )


_A54VoltageProbeLocation_Type.__name__ = "Integer32"
_A54VoltageProbeLocation_Object = MibTableColumn
a54VoltageProbeLocation = _A54VoltageProbeLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 2),
    _A54VoltageProbeLocation_Type()
)
a54VoltageProbeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54VoltageProbeLocation.setStatus("mandatory")
_A54VoltageProbeDescription_Type = DmiDisplaystring
_A54VoltageProbeDescription_Object = MibTableColumn
a54VoltageProbeDescription = _A54VoltageProbeDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 3),
    _A54VoltageProbeDescription_Type()
)
a54VoltageProbeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54VoltageProbeDescription.setStatus("mandatory")


class _A54VoltageStatus_Type(Integer32):
    """Custom type a54VoltageStatus based on Integer32"""
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
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A54VoltageStatus_Type.__name__ = "Integer32"
_A54VoltageStatus_Object = MibTableColumn
a54VoltageStatus = _A54VoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 4),
    _A54VoltageStatus_Type()
)
a54VoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54VoltageStatus.setStatus("mandatory")
_A54VoltageProbeVoltageLevel_Type = DmiInteger
_A54VoltageProbeVoltageLevel_Object = MibTableColumn
a54VoltageProbeVoltageLevel = _A54VoltageProbeVoltageLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 5),
    _A54VoltageProbeVoltageLevel_Type()
)
a54VoltageProbeVoltageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54VoltageProbeVoltageLevel.setStatus("mandatory")
_A54MonitoredVoltageNominalLevel_Type = DmiInteger
_A54MonitoredVoltageNominalLevel_Object = MibTableColumn
a54MonitoredVoltageNominalLevel = _A54MonitoredVoltageNominalLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 6),
    _A54MonitoredVoltageNominalLevel_Type()
)
a54MonitoredVoltageNominalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54MonitoredVoltageNominalLevel.setStatus("mandatory")
_A54MonitoredVoltageNormalMaximum_Type = DmiInteger
_A54MonitoredVoltageNormalMaximum_Object = MibTableColumn
a54MonitoredVoltageNormalMaximum = _A54MonitoredVoltageNormalMaximum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 7),
    _A54MonitoredVoltageNormalMaximum_Type()
)
a54MonitoredVoltageNormalMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54MonitoredVoltageNormalMaximum.setStatus("mandatory")
_A54MonitoredVoltageNormalMinimum_Type = DmiInteger
_A54MonitoredVoltageNormalMinimum_Object = MibTableColumn
a54MonitoredVoltageNormalMinimum = _A54MonitoredVoltageNormalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 8),
    _A54MonitoredVoltageNormalMinimum_Type()
)
a54MonitoredVoltageNormalMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54MonitoredVoltageNormalMinimum.setStatus("mandatory")
_A54VoltageProbeMaximum_Type = DmiInteger
_A54VoltageProbeMaximum_Object = MibTableColumn
a54VoltageProbeMaximum = _A54VoltageProbeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 9),
    _A54VoltageProbeMaximum_Type()
)
a54VoltageProbeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54VoltageProbeMaximum.setStatus("mandatory")
_A54VoltageProbeMinimum_Type = DmiInteger
_A54VoltageProbeMinimum_Object = MibTableColumn
a54VoltageProbeMinimum = _A54VoltageProbeMinimum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 10),
    _A54VoltageProbeMinimum_Type()
)
a54VoltageProbeMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54VoltageProbeMinimum.setStatus("mandatory")
_A54VoltageLevelLowerThreshold_Non_critic_Type = DmiInteger
_A54VoltageLevelLowerThreshold_Non_critic_Object = MibScalar
a54VoltageLevelLowerThreshold_Non_critic = _A54VoltageLevelLowerThreshold_Non_critic_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 11),
    _A54VoltageLevelLowerThreshold_Non_critic_Type()
)
a54VoltageLevelLowerThreshold_Non_critic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageLevelLowerThreshold_Non_critic.setStatus("mandatory")
_A54VoltageLevelUpperThreshold_Non_critic_Type = DmiInteger
_A54VoltageLevelUpperThreshold_Non_critic_Object = MibScalar
a54VoltageLevelUpperThreshold_Non_critic = _A54VoltageLevelUpperThreshold_Non_critic_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 12),
    _A54VoltageLevelUpperThreshold_Non_critic_Type()
)
a54VoltageLevelUpperThreshold_Non_critic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageLevelUpperThreshold_Non_critic.setStatus("mandatory")
_A54VoltageLevelLowerThreshold_Critical_Type = DmiInteger
_A54VoltageLevelLowerThreshold_Critical_Object = MibScalar
a54VoltageLevelLowerThreshold_Critical = _A54VoltageLevelLowerThreshold_Critical_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 13),
    _A54VoltageLevelLowerThreshold_Critical_Type()
)
a54VoltageLevelLowerThreshold_Critical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageLevelLowerThreshold_Critical.setStatus("mandatory")
_A54VoltageLevelUpperThreshold_Critical_Type = DmiInteger
_A54VoltageLevelUpperThreshold_Critical_Object = MibScalar
a54VoltageLevelUpperThreshold_Critical = _A54VoltageLevelUpperThreshold_Critical_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 14),
    _A54VoltageLevelUpperThreshold_Critical_Type()
)
a54VoltageLevelUpperThreshold_Critical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageLevelUpperThreshold_Critical.setStatus("mandatory")
_A54VoltageLevelLowerThreshold_Non_recove_Type = DmiInteger
_A54VoltageLevelLowerThreshold_Non_recove_Object = MibScalar
a54VoltageLevelLowerThreshold_Non_recove = _A54VoltageLevelLowerThreshold_Non_recove_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 15),
    _A54VoltageLevelLowerThreshold_Non_recove_Type()
)
a54VoltageLevelLowerThreshold_Non_recove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageLevelLowerThreshold_Non_recove.setStatus("mandatory")
_A54VoltageLevelUpperThreshold_Non_recove_Type = DmiInteger
_A54VoltageLevelUpperThreshold_Non_recove_Object = MibScalar
a54VoltageLevelUpperThreshold_Non_recove = _A54VoltageLevelUpperThreshold_Non_recove_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 16),
    _A54VoltageLevelUpperThreshold_Non_recove_Type()
)
a54VoltageLevelUpperThreshold_Non_recove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageLevelUpperThreshold_Non_recove.setStatus("mandatory")
_A54VoltageProbeResolution_Type = DmiInteger
_A54VoltageProbeResolution_Object = MibTableColumn
a54VoltageProbeResolution = _A54VoltageProbeResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 17),
    _A54VoltageProbeResolution_Type()
)
a54VoltageProbeResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageProbeResolution.setStatus("mandatory")
_A54VoltageProbeTolerance_Type = DmiInteger
_A54VoltageProbeTolerance_Object = MibTableColumn
a54VoltageProbeTolerance = _A54VoltageProbeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 18),
    _A54VoltageProbeTolerance_Type()
)
a54VoltageProbeTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageProbeTolerance.setStatus("mandatory")
_A54VoltageProbeAccuracy_Type = DmiInteger
_A54VoltageProbeAccuracy_Object = MibTableColumn
a54VoltageProbeAccuracy = _A54VoltageProbeAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 19),
    _A54VoltageProbeAccuracy_Type()
)
a54VoltageProbeAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a54VoltageProbeAccuracy.setStatus("mandatory")
_A54FruGroupIndex_Type = DmiInteger
_A54FruGroupIndex_Object = MibScalar
a54FruGroupIndex = _A54FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 20),
    _A54FruGroupIndex_Type()
)
a54FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54FruGroupIndex.setStatus("mandatory")
_A54OperationalGroupIndex_Type = DmiInteger
_A54OperationalGroupIndex_Object = MibScalar
a54OperationalGroupIndex = _A54OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 54, 1, 21),
    _A54OperationalGroupIndex_Type()
)
a54OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a54OperationalGroupIndex.setStatus("mandatory")
_TTemperatureProbe_Object = MibTable
tTemperatureProbe = _TTemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55)
)
if mibBuilder.loadTexts:
    tTemperatureProbe.setStatus("mandatory")
_ETemperatureProbe_Object = MibTableRow
eTemperatureProbe = _ETemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1)
)
eTemperatureProbe.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"),
)
if mibBuilder.loadTexts:
    eTemperatureProbe.setStatus("mandatory")
_A55TemperatureProbeTableIndex_Type = DmiInteger
_A55TemperatureProbeTableIndex_Object = MibTableColumn
a55TemperatureProbeTableIndex = _A55TemperatureProbeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 1),
    _A55TemperatureProbeTableIndex_Type()
)
a55TemperatureProbeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55TemperatureProbeTableIndex.setStatus("mandatory")


class _A55TemperatureProbeLocation_Type(Integer32):
    """Custom type a55TemperatureProbeLocation based on Integer32"""
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
        *(("vAdd-inCard", 11),
          ("vDisk", 4),
          ("vMemoryModule", 8),
          ("vMotherboard", 7),
          ("vOther", 1),
          ("vPeripheralBay", 5),
          ("vPowerUnit", 10),
          ("vProcessor", 3),
          ("vProcessorModule", 9),
          ("vSmbMaster", 6),
          ("vUnknown", 2))
    )


_A55TemperatureProbeLocation_Type.__name__ = "Integer32"
_A55TemperatureProbeLocation_Object = MibTableColumn
a55TemperatureProbeLocation = _A55TemperatureProbeLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 2),
    _A55TemperatureProbeLocation_Type()
)
a55TemperatureProbeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55TemperatureProbeLocation.setStatus("mandatory")
_A55TemperatureProbeDescription_Type = DmiDisplaystring
_A55TemperatureProbeDescription_Object = MibTableColumn
a55TemperatureProbeDescription = _A55TemperatureProbeDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 3),
    _A55TemperatureProbeDescription_Type()
)
a55TemperatureProbeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55TemperatureProbeDescription.setStatus("mandatory")


class _A55TemperatureStatus_Type(Integer32):
    """Custom type a55TemperatureStatus based on Integer32"""
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
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A55TemperatureStatus_Type.__name__ = "Integer32"
_A55TemperatureStatus_Object = MibTableColumn
a55TemperatureStatus = _A55TemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 4),
    _A55TemperatureStatus_Type()
)
a55TemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55TemperatureStatus.setStatus("mandatory")
_A55TemperatureProbeTemperatureReading_Type = DmiInteger
_A55TemperatureProbeTemperatureReading_Object = MibTableColumn
a55TemperatureProbeTemperatureReading = _A55TemperatureProbeTemperatureReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 5),
    _A55TemperatureProbeTemperatureReading_Type()
)
a55TemperatureProbeTemperatureReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55TemperatureProbeTemperatureReading.setStatus("mandatory")
_A55MonitoredTemperatureNominalReading_Type = DmiInteger
_A55MonitoredTemperatureNominalReading_Object = MibTableColumn
a55MonitoredTemperatureNominalReading = _A55MonitoredTemperatureNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 6),
    _A55MonitoredTemperatureNominalReading_Type()
)
a55MonitoredTemperatureNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55MonitoredTemperatureNominalReading.setStatus("mandatory")
_A55MonitoredTemperatureNormalMaximum_Type = DmiInteger
_A55MonitoredTemperatureNormalMaximum_Object = MibTableColumn
a55MonitoredTemperatureNormalMaximum = _A55MonitoredTemperatureNormalMaximum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 7),
    _A55MonitoredTemperatureNormalMaximum_Type()
)
a55MonitoredTemperatureNormalMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55MonitoredTemperatureNormalMaximum.setStatus("mandatory")
_A55MonitoredTemperatureNormalMinimum_Type = DmiInteger
_A55MonitoredTemperatureNormalMinimum_Object = MibTableColumn
a55MonitoredTemperatureNormalMinimum = _A55MonitoredTemperatureNormalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 8),
    _A55MonitoredTemperatureNormalMinimum_Type()
)
a55MonitoredTemperatureNormalMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55MonitoredTemperatureNormalMinimum.setStatus("mandatory")
_A55TemperatureProbeMaximum_Type = DmiInteger
_A55TemperatureProbeMaximum_Object = MibTableColumn
a55TemperatureProbeMaximum = _A55TemperatureProbeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 9),
    _A55TemperatureProbeMaximum_Type()
)
a55TemperatureProbeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55TemperatureProbeMaximum.setStatus("mandatory")
_A55TemperatureProbeMinimum_Type = DmiInteger
_A55TemperatureProbeMinimum_Object = MibTableColumn
a55TemperatureProbeMinimum = _A55TemperatureProbeMinimum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 10),
    _A55TemperatureProbeMinimum_Type()
)
a55TemperatureProbeMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55TemperatureProbeMinimum.setStatus("mandatory")
_A55TemperatureLowerThreshold_Non_critica_Type = DmiInteger
_A55TemperatureLowerThreshold_Non_critica_Object = MibScalar
a55TemperatureLowerThreshold_Non_critica = _A55TemperatureLowerThreshold_Non_critica_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 11),
    _A55TemperatureLowerThreshold_Non_critica_Type()
)
a55TemperatureLowerThreshold_Non_critica.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureLowerThreshold_Non_critica.setStatus("mandatory")
_A55TemperatureUpperThreshold_Non_critica_Type = DmiInteger
_A55TemperatureUpperThreshold_Non_critica_Object = MibScalar
a55TemperatureUpperThreshold_Non_critica = _A55TemperatureUpperThreshold_Non_critica_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 12),
    _A55TemperatureUpperThreshold_Non_critica_Type()
)
a55TemperatureUpperThreshold_Non_critica.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureUpperThreshold_Non_critica.setStatus("mandatory")
_A55TemperatureLowerThreshold_Critical_Type = DmiInteger
_A55TemperatureLowerThreshold_Critical_Object = MibScalar
a55TemperatureLowerThreshold_Critical = _A55TemperatureLowerThreshold_Critical_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 13),
    _A55TemperatureLowerThreshold_Critical_Type()
)
a55TemperatureLowerThreshold_Critical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureLowerThreshold_Critical.setStatus("mandatory")
_A55TemperatureUpperThreshold_Critical_Type = DmiInteger
_A55TemperatureUpperThreshold_Critical_Object = MibScalar
a55TemperatureUpperThreshold_Critical = _A55TemperatureUpperThreshold_Critical_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 14),
    _A55TemperatureUpperThreshold_Critical_Type()
)
a55TemperatureUpperThreshold_Critical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureUpperThreshold_Critical.setStatus("mandatory")
_A55TemperatureLowerThreshold_Non_recover_Type = DmiInteger
_A55TemperatureLowerThreshold_Non_recover_Object = MibScalar
a55TemperatureLowerThreshold_Non_recover = _A55TemperatureLowerThreshold_Non_recover_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 15),
    _A55TemperatureLowerThreshold_Non_recover_Type()
)
a55TemperatureLowerThreshold_Non_recover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureLowerThreshold_Non_recover.setStatus("mandatory")
_A55TemperatureUpperThreshold_Non_recover_Type = DmiInteger
_A55TemperatureUpperThreshold_Non_recover_Object = MibScalar
a55TemperatureUpperThreshold_Non_recover = _A55TemperatureUpperThreshold_Non_recover_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 16),
    _A55TemperatureUpperThreshold_Non_recover_Type()
)
a55TemperatureUpperThreshold_Non_recover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureUpperThreshold_Non_recover.setStatus("mandatory")
_A55TemperatureProbeResolution_Type = DmiInteger
_A55TemperatureProbeResolution_Object = MibTableColumn
a55TemperatureProbeResolution = _A55TemperatureProbeResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 17),
    _A55TemperatureProbeResolution_Type()
)
a55TemperatureProbeResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureProbeResolution.setStatus("mandatory")
_A55TemperatureProbeTolerance_Type = DmiInteger
_A55TemperatureProbeTolerance_Object = MibTableColumn
a55TemperatureProbeTolerance = _A55TemperatureProbeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 18),
    _A55TemperatureProbeTolerance_Type()
)
a55TemperatureProbeTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureProbeTolerance.setStatus("mandatory")
_A55TemperatureProbeAccuracy_Type = DmiInteger
_A55TemperatureProbeAccuracy_Object = MibTableColumn
a55TemperatureProbeAccuracy = _A55TemperatureProbeAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 19),
    _A55TemperatureProbeAccuracy_Type()
)
a55TemperatureProbeAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a55TemperatureProbeAccuracy.setStatus("mandatory")
_A55FruGroupIndex_Type = DmiInteger
_A55FruGroupIndex_Object = MibTableColumn
a55FruGroupIndex = _A55FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 20),
    _A55FruGroupIndex_Type()
)
a55FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55FruGroupIndex.setStatus("mandatory")
_A55OperationalGroupIndex_Type = DmiInteger
_A55OperationalGroupIndex_Object = MibTableColumn
a55OperationalGroupIndex = _A55OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 55, 1, 21),
    _A55OperationalGroupIndex_Type()
)
a55OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a55OperationalGroupIndex.setStatus("mandatory")
_TPhysicalContainerGlobalTable_Object = MibTable
tPhysicalContainerGlobalTable = _TPhysicalContainerGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64)
)
if mibBuilder.loadTexts:
    tPhysicalContainerGlobalTable.setStatus("mandatory")
_EPhysicalContainerGlobalTable_Object = MibTableRow
ePhysicalContainerGlobalTable = _EPhysicalContainerGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1)
)
ePhysicalContainerGlobalTable.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a64ContainerIndex"),
)
if mibBuilder.loadTexts:
    ePhysicalContainerGlobalTable.setStatus("mandatory")


class _A64ContainerOrChassisType_Type(Integer32):
    """Custom type a64ContainerOrChassisType based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("vAllInOne", 13),
          ("vBusExpansionChassis", 20),
          ("vDesktop", 3),
          ("vDockingStation", 12),
          ("vExpansionChassis", 18),
          ("vHandHeld", 11),
          ("vLaptop", 9),
          ("vLowProfileDesktop", 4),
          ("vLunchBox", 16),
          ("vMainSystemChassis", 17),
          ("vMiniTower", 6),
          ("vNotebook", 10),
          ("vOther", 1),
          ("vPeripheralChassis", 21),
          ("vPizzaBox", 5),
          ("vPortable", 8),
          ("vRackMountChassis", 23),
          ("vRaidChassis", 22),
          ("vSpace-saving", 15),
          ("vSubNotebook", 14),
          ("vSubchassis", 19),
          ("vTower", 7),
          ("vUnknown", 2))
    )


_A64ContainerOrChassisType_Type.__name__ = "Integer32"
_A64ContainerOrChassisType_Object = MibTableColumn
a64ContainerOrChassisType = _A64ContainerOrChassisType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 1),
    _A64ContainerOrChassisType_Type()
)
a64ContainerOrChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64ContainerOrChassisType.setStatus("mandatory")
_A64AssetTag_Type = DmiDisplaystring
_A64AssetTag_Object = MibTableColumn
a64AssetTag = _A64AssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 2),
    _A64AssetTag_Type()
)
a64AssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a64AssetTag.setStatus("mandatory")


class _A64ChassisLockPresent_Type(Integer32):
    """Custom type a64ChassisLockPresent based on Integer32"""
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


_A64ChassisLockPresent_Type.__name__ = "Integer32"
_A64ChassisLockPresent_Object = MibTableColumn
a64ChassisLockPresent = _A64ChassisLockPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 3),
    _A64ChassisLockPresent_Type()
)
a64ChassisLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64ChassisLockPresent.setStatus("mandatory")


class _A64BootupState_Type(Integer32):
    """Custom type a64BootupState based on Integer32"""
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
          ("vNon-recoverable1", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A64BootupState_Type.__name__ = "Integer32"
_A64BootupState_Object = MibTableColumn
a64BootupState = _A64BootupState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 4),
    _A64BootupState_Type()
)
a64BootupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64BootupState.setStatus("mandatory")


class _A64PowerState_Type(Integer32):
    """Custom type a64PowerState based on Integer32"""
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
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A64PowerState_Type.__name__ = "Integer32"
_A64PowerState_Object = MibTableColumn
a64PowerState = _A64PowerState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 5),
    _A64PowerState_Type()
)
a64PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64PowerState.setStatus("mandatory")


class _A64ThermalState_Type(Integer32):
    """Custom type a64ThermalState based on Integer32"""
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
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A64ThermalState_Type.__name__ = "Integer32"
_A64ThermalState_Object = MibTableColumn
a64ThermalState = _A64ThermalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 6),
    _A64ThermalState_Type()
)
a64ThermalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64ThermalState.setStatus("mandatory")
_A64FruGroupIndex_Type = DmiInteger
_A64FruGroupIndex_Object = MibTableColumn
a64FruGroupIndex = _A64FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 7),
    _A64FruGroupIndex_Type()
)
a64FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64FruGroupIndex.setStatus("mandatory")
_A64OperationalGroupIndex_Type = DmiInteger
_A64OperationalGroupIndex_Object = MibTableColumn
a64OperationalGroupIndex = _A64OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 8),
    _A64OperationalGroupIndex_Type()
)
a64OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64OperationalGroupIndex.setStatus("mandatory")
_A64ContainerIndex_Type = DmiInteger
_A64ContainerIndex_Object = MibTableColumn
a64ContainerIndex = _A64ContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 9),
    _A64ContainerIndex_Type()
)
a64ContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64ContainerIndex.setStatus("mandatory")
_A64ContainerName_Type = DmiDisplaystring
_A64ContainerName_Object = MibTableColumn
a64ContainerName = _A64ContainerName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 10),
    _A64ContainerName_Type()
)
a64ContainerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a64ContainerName.setStatus("mandatory")
_A64ContainerLocation_Type = DmiDisplaystring
_A64ContainerLocation_Object = MibTableColumn
a64ContainerLocation = _A64ContainerLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 11),
    _A64ContainerLocation_Type()
)
a64ContainerLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a64ContainerLocation.setStatus("mandatory")


class _A64ContainerSecurityStatus_Type(Integer32):
    """Custom type a64ContainerSecurityStatus based on Integer32"""
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
        *(("vContainerSecurityBreachAttempted", 4),
          ("vContainerSecurityBreached", 5),
          ("vNoSecurityBreachDetected", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A64ContainerSecurityStatus_Type.__name__ = "Integer32"
_A64ContainerSecurityStatus_Object = MibTableColumn
a64ContainerSecurityStatus = _A64ContainerSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 64, 1, 12),
    _A64ContainerSecurityStatus_Type()
)
a64ContainerSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a64ContainerSecurityStatus.setStatus("mandatory")
_TOperatingSystem_Object = MibTable
tOperatingSystem = _TOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66)
)
if mibBuilder.loadTexts:
    tOperatingSystem.setStatus("mandatory")
_EOperatingSystem_Object = MibTableRow
eOperatingSystem = _EOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1)
)
eOperatingSystem.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a66OperatingSystemIndex"),
)
if mibBuilder.loadTexts:
    eOperatingSystem.setStatus("mandatory")
_A66OperatingSystemIndex_Type = DmiInteger
_A66OperatingSystemIndex_Object = MibTableColumn
a66OperatingSystemIndex = _A66OperatingSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 1),
    _A66OperatingSystemIndex_Type()
)
a66OperatingSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66OperatingSystemIndex.setStatus("mandatory")
_A66OperatingSystemName_Type = DmiDisplaystring
_A66OperatingSystemName_Object = MibTableColumn
a66OperatingSystemName = _A66OperatingSystemName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 2),
    _A66OperatingSystemName_Type()
)
a66OperatingSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66OperatingSystemName.setStatus("mandatory")
_A66OperatingSystemVersion_Type = DmiDisplaystring
_A66OperatingSystemVersion_Object = MibTableColumn
a66OperatingSystemVersion = _A66OperatingSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 3),
    _A66OperatingSystemVersion_Type()
)
a66OperatingSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66OperatingSystemVersion.setStatus("mandatory")


class _A66PrimaryOperatingSystem_Type(Integer32):
    """Custom type a66PrimaryOperatingSystem based on Integer32"""
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


_A66PrimaryOperatingSystem_Type.__name__ = "Integer32"
_A66PrimaryOperatingSystem_Object = MibTableColumn
a66PrimaryOperatingSystem = _A66PrimaryOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 4),
    _A66PrimaryOperatingSystem_Type()
)
a66PrimaryOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66PrimaryOperatingSystem.setStatus("mandatory")


class _A66OperatingSystemBootDeviceStorageType_Type(Integer32):
    """Custom type a66OperatingSystemBootDeviceStorageType based on Integer32"""
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
          ("vCompactDisk", 8),
          ("vFlashDisk", 9),
          ("vFloppyDisk", 4),
          ("vHardDisk", 3),
          ("vOpticalFloppyDisk", 11),
          ("vOpticalRom", 5),
          ("vOpticalRw", 7),
          ("vOpticalWorm", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A66OperatingSystemBootDeviceStorageType_Type.__name__ = "Integer32"
_A66OperatingSystemBootDeviceStorageType_Object = MibTableColumn
a66OperatingSystemBootDeviceStorageType = _A66OperatingSystemBootDeviceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 5),
    _A66OperatingSystemBootDeviceStorageType_Type()
)
a66OperatingSystemBootDeviceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66OperatingSystemBootDeviceStorageType.setStatus("mandatory")
_A66OperatingSystemBootDeviceIndex_Type = DmiInteger
_A66OperatingSystemBootDeviceIndex_Object = MibTableColumn
a66OperatingSystemBootDeviceIndex = _A66OperatingSystemBootDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 6),
    _A66OperatingSystemBootDeviceIndex_Type()
)
a66OperatingSystemBootDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66OperatingSystemBootDeviceIndex.setStatus("mandatory")
_A66OperatingSystemBootPartitionIndex_Type = DmiInteger
_A66OperatingSystemBootPartitionIndex_Object = MibTableColumn
a66OperatingSystemBootPartitionIndex = _A66OperatingSystemBootPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 7),
    _A66OperatingSystemBootPartitionIndex_Type()
)
a66OperatingSystemBootPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66OperatingSystemBootPartitionIndex.setStatus("mandatory")
_A66OperatingSystemDescription_Type = DmiDisplaystring
_A66OperatingSystemDescription_Object = MibTableColumn
a66OperatingSystemDescription = _A66OperatingSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 66, 1, 8),
    _A66OperatingSystemDescription_Type()
)
a66OperatingSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a66OperatingSystemDescription.setStatus("mandatory")
_TPowerUnitGlobalTable_Object = MibTable
tPowerUnitGlobalTable = _TPowerUnitGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 67)
)
if mibBuilder.loadTexts:
    tPowerUnitGlobalTable.setStatus("mandatory")
_EPowerUnitGlobalTable_Object = MibTableRow
ePowerUnitGlobalTable = _EPowerUnitGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 67, 1)
)
ePowerUnitGlobalTable.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a67PowerUnitIndex"),
)
if mibBuilder.loadTexts:
    ePowerUnitGlobalTable.setStatus("mandatory")
_A67PowerUnitIndex_Type = DmiInteger
_A67PowerUnitIndex_Object = MibTableColumn
a67PowerUnitIndex = _A67PowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 67, 1, 1),
    _A67PowerUnitIndex_Type()
)
a67PowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a67PowerUnitIndex.setStatus("mandatory")


class _A67PowerUnitRedundancyStatus_Type(Integer32):
    """Custom type a67PowerUnitRedundancyStatus based on Integer32"""
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
        *(("vDegradedRedundancy", 6),
          ("vFullyRedundant", 5),
          ("vNotApplicableUnitNotRedundant", 3),
          ("vOffline", 4),
          ("vOther", 1),
          ("vRedundancyLost", 7),
          ("vUnknown", 2))
    )


_A67PowerUnitRedundancyStatus_Type.__name__ = "Integer32"
_A67PowerUnitRedundancyStatus_Object = MibTableColumn
a67PowerUnitRedundancyStatus = _A67PowerUnitRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 67, 1, 2),
    _A67PowerUnitRedundancyStatus_Type()
)
a67PowerUnitRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a67PowerUnitRedundancyStatus.setStatus("mandatory")
_TParallelPorts_Object = MibTable
tParallelPorts = _TParallelPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74)
)
if mibBuilder.loadTexts:
    tParallelPorts.setStatus("mandatory")
_EParallelPorts_Object = MibTableRow
eParallelPorts = _EParallelPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1)
)
eParallelPorts.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a74ParallelPortIndex"),
)
if mibBuilder.loadTexts:
    eParallelPorts.setStatus("mandatory")
_A74ParallelPortIndex_Type = DmiInteger
_A74ParallelPortIndex_Object = MibTableColumn
a74ParallelPortIndex = _A74ParallelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 1),
    _A74ParallelPortIndex_Type()
)
a74ParallelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74ParallelPortIndex.setStatus("mandatory")
_A74ParallelBaseIoAddress_Type = DmiInteger64X
_A74ParallelBaseIoAddress_Object = MibTableColumn
a74ParallelBaseIoAddress = _A74ParallelBaseIoAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 2),
    _A74ParallelBaseIoAddress_Type()
)
a74ParallelBaseIoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74ParallelBaseIoAddress.setStatus("mandatory")
_A74IrqUsed_Type = DmiInteger
_A74IrqUsed_Object = MibTableColumn
a74IrqUsed = _A74IrqUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 3),
    _A74IrqUsed_Type()
)
a74IrqUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74IrqUsed.setStatus("mandatory")
_A74LogicalName_Type = DmiDisplaystring
_A74LogicalName_Object = MibTableColumn
a74LogicalName = _A74LogicalName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 4),
    _A74LogicalName_Type()
)
a74LogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74LogicalName.setStatus("mandatory")


class _A74ConnectorType_Type(Integer32):
    """Custom type a74ConnectorType based on Integer32"""
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
              160,
              161,
              162)
        )
    )
    namedValues = NamedValues(
        *(("vCentronics", 5),
          ("vCentronics-14", 160),
          ("vDb-25Female", 3),
          ("vDb-25Male", 4),
          ("vDb-36Female", 161),
          ("vMini-centronics", 6),
          ("vMini-centronics-20", 162),
          ("vOther", 1),
          ("vProprietary", 7),
          ("vUnknown", 2))
    )


_A74ConnectorType_Type.__name__ = "Integer32"
_A74ConnectorType_Object = MibTableColumn
a74ConnectorType = _A74ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 5),
    _A74ConnectorType_Type()
)
a74ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74ConnectorType.setStatus("mandatory")


class _A74ConnectorPinout_Type(Integer32):
    """Custom type a74ConnectorPinout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              160,
              161,
              162,
              163,
              164)
        )
    )
    namedValues = NamedValues(
        *(("vIeee1284", 5),
          ("vOther", 1),
          ("vPc-98", 160),
          ("vPc-98-hireso", 161),
          ("vPc-98full", 164),
          ("vPc-98note", 163),
          ("vPc-h98", 162),
          ("vProprietary", 6),
          ("vPs2", 4),
          ("vUnknown", 2),
          ("vXtat", 3))
    )


_A74ConnectorPinout_Type.__name__ = "Integer32"
_A74ConnectorPinout_Object = MibTableColumn
a74ConnectorPinout = _A74ConnectorPinout_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 6),
    _A74ConnectorPinout_Type()
)
a74ConnectorPinout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74ConnectorPinout.setStatus("mandatory")


class _A74DmaSupport_Type(Integer32):
    """Custom type a74DmaSupport based on Integer32"""
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


_A74DmaSupport_Type.__name__ = "Integer32"
_A74DmaSupport_Object = MibTableColumn
a74DmaSupport = _A74DmaSupport_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 7),
    _A74DmaSupport_Type()
)
a74DmaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74DmaSupport.setStatus("mandatory")
_A74ParallelPortCapabilities_Type = DmiInteger
_A74ParallelPortCapabilities_Object = MibTableColumn
a74ParallelPortCapabilities = _A74ParallelPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 8),
    _A74ParallelPortCapabilities_Type()
)
a74ParallelPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74ParallelPortCapabilities.setStatus("mandatory")
_A74OperationalGroupIndex_Type = DmiInteger
_A74OperationalGroupIndex_Object = MibTableColumn
a74OperationalGroupIndex = _A74OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 9),
    _A74OperationalGroupIndex_Type()
)
a74OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74OperationalGroupIndex.setStatus("mandatory")


class _A74ParallelPortSecuritySettings_Type(Integer32):
    """Custom type a74ParallelPortSecuritySettings based on Integer32"""
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
        *(("vBoot-bypass", 6),
          ("vExternalInterfaceEnabled", 5),
          ("vExternalInterfaceLockedOut", 4),
          ("vNone", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A74ParallelPortSecuritySettings_Type.__name__ = "Integer32"
_A74ParallelPortSecuritySettings_Object = MibTableColumn
a74ParallelPortSecuritySettings = _A74ParallelPortSecuritySettings_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 74, 1, 10),
    _A74ParallelPortSecuritySettings_Type()
)
a74ParallelPortSecuritySettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a74ParallelPortSecuritySettings.setStatus("mandatory")
_TSerialPorts_Object = MibTable
tSerialPorts = _TSerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75)
)
if mibBuilder.loadTexts:
    tSerialPorts.setStatus("mandatory")
_ESerialPorts_Object = MibTableRow
eSerialPorts = _ESerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1)
)
eSerialPorts.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a75SerialPortIndex"),
)
if mibBuilder.loadTexts:
    eSerialPorts.setStatus("mandatory")
_A75SerialPortIndex_Type = DmiInteger
_A75SerialPortIndex_Object = MibTableColumn
a75SerialPortIndex = _A75SerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 1),
    _A75SerialPortIndex_Type()
)
a75SerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75SerialPortIndex.setStatus("mandatory")
_A75SerialBaseIoAddress_Type = DmiInteger64X
_A75SerialBaseIoAddress_Object = MibTableColumn
a75SerialBaseIoAddress = _A75SerialBaseIoAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 2),
    _A75SerialBaseIoAddress_Type()
)
a75SerialBaseIoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75SerialBaseIoAddress.setStatus("mandatory")
_A75IrqUsed_Type = DmiInteger
_A75IrqUsed_Object = MibTableColumn
a75IrqUsed = _A75IrqUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 3),
    _A75IrqUsed_Type()
)
a75IrqUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75IrqUsed.setStatus("mandatory")
_A75LogicalName_Type = DmiDisplaystring
_A75LogicalName_Object = MibTableColumn
a75LogicalName = _A75LogicalName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 4),
    _A75LogicalName_Type()
)
a75LogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75LogicalName.setStatus("mandatory")


class _A75ConnectorType_Type(Integer32):
    """Custom type a75ConnectorType based on Integer32"""
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
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("vCircularDin-8Female", 11),
          ("vCircularDin-8Male", 10),
          ("vDb-25PinFemale", 6),
          ("vDb-25PinMale", 5),
          ("vDb-9PinFemale", 4),
          ("vDb-9PinMale", 3),
          ("vMini-centronicsType-14", 160),
          ("vMini-centronicsType-26", 161),
          ("vOther", 1),
          ("vProprietary", 9),
          ("vRj-11", 7),
          ("vRj-45", 8),
          ("vUnknown", 2))
    )


_A75ConnectorType_Type.__name__ = "Integer32"
_A75ConnectorType_Object = MibTableColumn
a75ConnectorType = _A75ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 5),
    _A75ConnectorType_Type()
)
a75ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75ConnectorType.setStatus("mandatory")
_A75MaximumSpeed_Type = DmiInteger
_A75MaximumSpeed_Object = MibTableColumn
a75MaximumSpeed = _A75MaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 6),
    _A75MaximumSpeed_Type()
)
a75MaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75MaximumSpeed.setStatus("mandatory")


class _A75SerialPortCapabilities_Type(Integer32):
    """Custom type a75SerialPortCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("v16450Compatible", 4),
          ("v16550Compatible", 5),
          ("v16550aCompatible", 6),
          ("v8251Compatible", 160),
          ("v8251fifoCompatible", 161),
          ("vOther", 1),
          ("vUnknown", 2),
          ("vXtatCompatible", 3))
    )


_A75SerialPortCapabilities_Type.__name__ = "Integer32"
_A75SerialPortCapabilities_Object = MibTableColumn
a75SerialPortCapabilities = _A75SerialPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 7),
    _A75SerialPortCapabilities_Type()
)
a75SerialPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75SerialPortCapabilities.setStatus("mandatory")
_A75OperationalGroupIndex_Type = DmiInteger
_A75OperationalGroupIndex_Object = MibTableColumn
a75OperationalGroupIndex = _A75OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 8),
    _A75OperationalGroupIndex_Type()
)
a75OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75OperationalGroupIndex.setStatus("mandatory")


class _A75SerialPortSecuritySettings_Type(Integer32):
    """Custom type a75SerialPortSecuritySettings based on Integer32"""
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
        *(("vBoot-bypass", 6),
          ("vExternalInterfaceEnabled", 5),
          ("vExternalInterfaceLockedOut", 4),
          ("vNone", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A75SerialPortSecuritySettings_Type.__name__ = "Integer32"
_A75SerialPortSecuritySettings_Object = MibTableColumn
a75SerialPortSecuritySettings = _A75SerialPortSecuritySettings_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 75, 1, 9),
    _A75SerialPortSecuritySettings_Type()
)
a75SerialPortSecuritySettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a75SerialPortSecuritySettings.setStatus("mandatory")
_TCoolingDevice_Object = MibTable
tCoolingDevice = _TCoolingDevice_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81)
)
if mibBuilder.loadTexts:
    tCoolingDevice.setStatus("mandatory")
_ECoolingDevice_Object = MibTableRow
eCoolingDevice = _ECoolingDevice_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81, 1)
)
eCoolingDevice.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a81CoolingDeviceTableIndex"),
)
if mibBuilder.loadTexts:
    eCoolingDevice.setStatus("mandatory")
_A81CoolingDeviceTableIndex_Type = DmiInteger
_A81CoolingDeviceTableIndex_Object = MibTableColumn
a81CoolingDeviceTableIndex = _A81CoolingDeviceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81, 1, 1),
    _A81CoolingDeviceTableIndex_Type()
)
a81CoolingDeviceTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a81CoolingDeviceTableIndex.setStatus("mandatory")
_A81FruGroupIndex_Type = DmiInteger
_A81FruGroupIndex_Object = MibTableColumn
a81FruGroupIndex = _A81FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81, 1, 2),
    _A81FruGroupIndex_Type()
)
a81FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a81FruGroupIndex.setStatus("mandatory")
_A81OperationalGroupIndex_Type = DmiInteger
_A81OperationalGroupIndex_Object = MibTableColumn
a81OperationalGroupIndex = _A81OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81, 1, 3),
    _A81OperationalGroupIndex_Type()
)
a81OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a81OperationalGroupIndex.setStatus("mandatory")
_A81CoolingUnitIndex_Type = DmiInteger
_A81CoolingUnitIndex_Object = MibTableColumn
a81CoolingUnitIndex = _A81CoolingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81, 1, 4),
    _A81CoolingUnitIndex_Type()
)
a81CoolingUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a81CoolingUnitIndex.setStatus("mandatory")


class _A81CoolingDeviceType_Type(Integer32):
    """Custom type a81CoolingDeviceType based on Integer32"""
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("vActiveCooling", 32),
          ("vCabinetFan", 6),
          ("vCentrifugalBlower", 4),
          ("vChipFan", 5),
          ("vFan", 3),
          ("vHeatPipe", 8),
          ("vIntegratedRefrigeration", 9),
          ("vOther", 1),
          ("vPassiveCooling", 33),
          ("vPowerSupplyFan", 7),
          ("vUnknown", 2))
    )


_A81CoolingDeviceType_Type.__name__ = "Integer32"
_A81CoolingDeviceType_Object = MibTableColumn
a81CoolingDeviceType = _A81CoolingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81, 1, 5),
    _A81CoolingDeviceType_Type()
)
a81CoolingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a81CoolingDeviceType.setStatus("mandatory")
_A81TemperatureProbeIndex_Type = DmiInteger
_A81TemperatureProbeIndex_Object = MibTableColumn
a81TemperatureProbeIndex = _A81TemperatureProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 81, 1, 6),
    _A81TemperatureProbeIndex_Type()
)
a81TemperatureProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a81TemperatureProbeIndex.setStatus("mandatory")
_TVideo_Object = MibTable
tVideo = _TVideo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83)
)
if mibBuilder.loadTexts:
    tVideo.setStatus("mandatory")
_EVideo_Object = MibTableRow
eVideo = _EVideo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1)
)
eVideo.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a83VideoIndex"),
)
if mibBuilder.loadTexts:
    eVideo.setStatus("mandatory")
_A83VideoIndex_Type = DmiInteger
_A83VideoIndex_Object = MibTableColumn
a83VideoIndex = _A83VideoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 1),
    _A83VideoIndex_Type()
)
a83VideoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83VideoIndex.setStatus("mandatory")


class _A83VideoType_Type(Integer32):
    """Custom type a83VideoType based on Integer32"""
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
              160)
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
          ("vPc-98", 160),
          ("vSvga", 6),
          ("vUnknown", 2),
          ("vVga", 5),
          ("vXga", 11))
    )


_A83VideoType_Type.__name__ = "Integer32"
_A83VideoType_Object = MibTableColumn
a83VideoType = _A83VideoType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 2),
    _A83VideoType_Type()
)
a83VideoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83VideoType.setStatus("mandatory")
_A83CurrentVideoMode_Type = DmiInteger
_A83CurrentVideoMode_Object = MibTableColumn
a83CurrentVideoMode = _A83CurrentVideoMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 3),
    _A83CurrentVideoMode_Type()
)
a83CurrentVideoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83CurrentVideoMode.setStatus("mandatory")
_A83MinimumRefreshRate_Type = DmiInteger
_A83MinimumRefreshRate_Object = MibTableColumn
a83MinimumRefreshRate = _A83MinimumRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 4),
    _A83MinimumRefreshRate_Type()
)
a83MinimumRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83MinimumRefreshRate.setStatus("mandatory")
_A83MaximumRefreshRate_Type = DmiInteger
_A83MaximumRefreshRate_Object = MibTableColumn
a83MaximumRefreshRate = _A83MaximumRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 5),
    _A83MaximumRefreshRate_Type()
)
a83MaximumRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83MaximumRefreshRate.setStatus("mandatory")


class _A83VideoMemoryType_Type(Integer32):
    """Custom type a83VideoMemoryType based on Integer32"""
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
        *(("vBurstSynchronousDram", 8),
          ("vDram", 4),
          ("vEdoRam", 7),
          ("vOther", 1),
          ("vPipelinedBurstSram", 9),
          ("vSram", 5),
          ("vUnknown", 2),
          ("vVram", 3),
          ("vWram", 6))
    )


_A83VideoMemoryType_Type.__name__ = "Integer32"
_A83VideoMemoryType_Object = MibTableColumn
a83VideoMemoryType = _A83VideoMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 6),
    _A83VideoMemoryType_Type()
)
a83VideoMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83VideoMemoryType.setStatus("mandatory")
_A83VideoRamMemorySize_Type = DmiInteger
_A83VideoRamMemorySize_Object = MibTableColumn
a83VideoRamMemorySize = _A83VideoRamMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 7),
    _A83VideoRamMemorySize_Type()
)
a83VideoRamMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83VideoRamMemorySize.setStatus("mandatory")


class _A83ScanMode_Type(Integer32):
    """Custom type a83ScanMode based on Integer32"""
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


_A83ScanMode_Type.__name__ = "Integer32"
_A83ScanMode_Object = MibTableColumn
a83ScanMode = _A83ScanMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 8),
    _A83ScanMode_Type()
)
a83ScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83ScanMode.setStatus("mandatory")


class _A83VideoPhysicalLocation_Type(Integer32):
    """Custom type a83VideoPhysicalLocation based on Integer32"""
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
        *(("vAdd-onCard", 4),
          ("vIntegrated", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A83VideoPhysicalLocation_Type.__name__ = "Integer32"
_A83VideoPhysicalLocation_Object = MibTableColumn
a83VideoPhysicalLocation = _A83VideoPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 9),
    _A83VideoPhysicalLocation_Type()
)
a83VideoPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83VideoPhysicalLocation.setStatus("mandatory")
_A83CurrentVerticalResolution_Type = DmiInteger
_A83CurrentVerticalResolution_Object = MibTableColumn
a83CurrentVerticalResolution = _A83CurrentVerticalResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 10),
    _A83CurrentVerticalResolution_Type()
)
a83CurrentVerticalResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83CurrentVerticalResolution.setStatus("mandatory")
_A83CurrentHorizontalResolution_Type = DmiInteger
_A83CurrentHorizontalResolution_Object = MibTableColumn
a83CurrentHorizontalResolution = _A83CurrentHorizontalResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 11),
    _A83CurrentHorizontalResolution_Type()
)
a83CurrentHorizontalResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83CurrentHorizontalResolution.setStatus("mandatory")
_A83CurrentNumberOfBitsPerPixel_Type = DmiInteger
_A83CurrentNumberOfBitsPerPixel_Object = MibTableColumn
a83CurrentNumberOfBitsPerPixel = _A83CurrentNumberOfBitsPerPixel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 12),
    _A83CurrentNumberOfBitsPerPixel_Type()
)
a83CurrentNumberOfBitsPerPixel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83CurrentNumberOfBitsPerPixel.setStatus("mandatory")
_A83CurrentNumberOfRows_Type = DmiInteger
_A83CurrentNumberOfRows_Object = MibTableColumn
a83CurrentNumberOfRows = _A83CurrentNumberOfRows_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 13),
    _A83CurrentNumberOfRows_Type()
)
a83CurrentNumberOfRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83CurrentNumberOfRows.setStatus("mandatory")
_A83CurrentNumberOfColumns_Type = DmiInteger
_A83CurrentNumberOfColumns_Object = MibTableColumn
a83CurrentNumberOfColumns = _A83CurrentNumberOfColumns_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 14),
    _A83CurrentNumberOfColumns_Type()
)
a83CurrentNumberOfColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83CurrentNumberOfColumns.setStatus("mandatory")
_A83CurrentRefreshRate_Type = DmiInteger
_A83CurrentRefreshRate_Object = MibTableColumn
a83CurrentRefreshRate = _A83CurrentRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 15),
    _A83CurrentRefreshRate_Type()
)
a83CurrentRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83CurrentRefreshRate.setStatus("mandatory")
_A83FruGroupIndex_Type = DmiInteger
_A83FruGroupIndex_Object = MibTableColumn
a83FruGroupIndex = _A83FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 16),
    _A83FruGroupIndex_Type()
)
a83FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83FruGroupIndex.setStatus("mandatory")
_A83OperationalGroupIndex_Type = DmiInteger
_A83OperationalGroupIndex_Object = MibTableColumn
a83OperationalGroupIndex = _A83OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 83, 1, 17),
    _A83OperationalGroupIndex_Type()
)
a83OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a83OperationalGroupIndex.setStatus("mandatory")
_TVideoBios_Object = MibTable
tVideoBios = _TVideoBios_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 84)
)
if mibBuilder.loadTexts:
    tVideoBios.setStatus("mandatory")
_EVideoBios_Object = MibTableRow
eVideoBios = _EVideoBios_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 84, 1)
)
eVideoBios.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a84VideoBiosIndex"),
)
if mibBuilder.loadTexts:
    eVideoBios.setStatus("mandatory")
_A84VideoBiosIndex_Type = DmiInteger
_A84VideoBiosIndex_Object = MibTableColumn
a84VideoBiosIndex = _A84VideoBiosIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 84, 1, 1),
    _A84VideoBiosIndex_Type()
)
a84VideoBiosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a84VideoBiosIndex.setStatus("mandatory")
_A84VideoBiosManufacturer_Type = DmiDisplaystring
_A84VideoBiosManufacturer_Object = MibTableColumn
a84VideoBiosManufacturer = _A84VideoBiosManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 84, 1, 2),
    _A84VideoBiosManufacturer_Type()
)
a84VideoBiosManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a84VideoBiosManufacturer.setStatus("mandatory")
_A84VideoBiosVersion_Type = DmiDisplaystring
_A84VideoBiosVersion_Object = MibTableColumn
a84VideoBiosVersion = _A84VideoBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 84, 1, 3),
    _A84VideoBiosVersion_Type()
)
a84VideoBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a84VideoBiosVersion.setStatus("mandatory")
_A84VideoBiosReleaseDate_Type = DmiDateX
_A84VideoBiosReleaseDate_Object = MibTableColumn
a84VideoBiosReleaseDate = _A84VideoBiosReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 84, 1, 4),
    _A84VideoBiosReleaseDate_Type()
)
a84VideoBiosReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a84VideoBiosReleaseDate.setStatus("mandatory")


class _A84VideoBiosShadowingState_Type(Integer32):
    """Custom type a84VideoBiosShadowingState based on Integer32"""
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


_A84VideoBiosShadowingState_Type.__name__ = "Integer32"
_A84VideoBiosShadowingState_Object = MibTableColumn
a84VideoBiosShadowingState = _A84VideoBiosShadowingState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 84, 1, 5),
    _A84VideoBiosShadowingState_Type()
)
a84VideoBiosShadowingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a84VideoBiosShadowingState.setStatus("mandatory")
_TMouse_Object = MibTable
tMouse = _TMouse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91)
)
if mibBuilder.loadTexts:
    tMouse.setStatus("mandatory")
_EMouse_Object = MibTableRow
eMouse = _EMouse_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1)
)
eMouse.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMouse.setStatus("mandatory")


class _A91MouseInterface_Type(Integer32):
    """Custom type a91MouseInterface based on Integer32"""
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
              160,
              161)
        )
    )
    namedValues = NamedValues(
        *(("vAdb", 8),
          ("vBusMouse", 7),
          ("vBusMouseDb-9", 160),
          ("vBusMouseMicro-din", 161),
          ("vHp-hil", 6),
          ("vInfrared", 5),
          ("vOther", 1),
          ("vPs2", 4),
          ("vSerial", 3),
          ("vUnknown", 2))
    )


_A91MouseInterface_Type.__name__ = "Integer32"
_A91MouseInterface_Object = MibTableColumn
a91MouseInterface = _A91MouseInterface_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 1),
    _A91MouseInterface_Type()
)
a91MouseInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91MouseInterface.setStatus("mandatory")
_A91MouseIrq_Type = DmiInteger
_A91MouseIrq_Object = MibTableColumn
a91MouseIrq = _A91MouseIrq_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 2),
    _A91MouseIrq_Type()
)
a91MouseIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91MouseIrq.setStatus("mandatory")
_A91MouseButtons_Type = DmiInteger
_A91MouseButtons_Object = MibTableColumn
a91MouseButtons = _A91MouseButtons_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 3),
    _A91MouseButtons_Type()
)
a91MouseButtons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91MouseButtons.setStatus("mandatory")
_A91MousePortName_Type = DmiDisplaystring
_A91MousePortName_Object = MibTableColumn
a91MousePortName = _A91MousePortName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 4),
    _A91MousePortName_Type()
)
a91MousePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91MousePortName.setStatus("mandatory")
_A91MouseDriverName_Type = DmiDisplaystring
_A91MouseDriverName_Object = MibTableColumn
a91MouseDriverName = _A91MouseDriverName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 5),
    _A91MouseDriverName_Type()
)
a91MouseDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91MouseDriverName.setStatus("mandatory")
_A91MouseDriverVersion_Type = DmiDisplaystring
_A91MouseDriverVersion_Object = MibTableColumn
a91MouseDriverVersion = _A91MouseDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 6),
    _A91MouseDriverVersion_Type()
)
a91MouseDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91MouseDriverVersion.setStatus("mandatory")
_A91FruGroupIndex_Type = DmiInteger
_A91FruGroupIndex_Object = MibTableColumn
a91FruGroupIndex = _A91FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 7),
    _A91FruGroupIndex_Type()
)
a91FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91FruGroupIndex.setStatus("mandatory")
_A91OperationalGroupIndex_Type = DmiInteger
_A91OperationalGroupIndex_Object = MibTableColumn
a91OperationalGroupIndex = _A91OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 8),
    _A91OperationalGroupIndex_Type()
)
a91OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91OperationalGroupIndex.setStatus("mandatory")


class _A91SecuritySettings_Type(Integer32):
    """Custom type a91SecuritySettings based on Integer32"""
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
        *(("vExternalInterfaceEnabled", 5),
          ("vExternalInterfaceLockedOut", 4),
          ("vNone", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A91SecuritySettings_Type.__name__ = "Integer32"
_A91SecuritySettings_Object = MibTableColumn
a91SecuritySettings = _A91SecuritySettings_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 91, 1, 9),
    _A91SecuritySettings_Type()
)
a91SecuritySettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a91SecuritySettings.setStatus("mandatory")
_TKeyboard_Object = MibTable
tKeyboard = _TKeyboard_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92)
)
if mibBuilder.loadTexts:
    tKeyboard.setStatus("mandatory")
_EKeyboard_Object = MibTableRow
eKeyboard = _EKeyboard_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92, 1)
)
eKeyboard.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eKeyboard.setStatus("mandatory")
_A92KeyboardLayout_Type = DmiDisplaystring
_A92KeyboardLayout_Object = MibTableColumn
a92KeyboardLayout = _A92KeyboardLayout_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92, 1, 1),
    _A92KeyboardLayout_Type()
)
a92KeyboardLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a92KeyboardLayout.setStatus("mandatory")
_A92KeyboardType_Type = DmiDisplaystring
_A92KeyboardType_Object = MibTableColumn
a92KeyboardType = _A92KeyboardType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92, 1, 2),
    _A92KeyboardType_Type()
)
a92KeyboardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a92KeyboardType.setStatus("mandatory")


class _A92KeyboardConnectorType_Type(Integer32):
    """Custom type a92KeyboardConnectorType based on Integer32"""
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
              160)
        )
    )
    namedValues = NamedValues(
        *(("vAccessBus", 9),
          ("vDb-9", 8),
          ("vHp-hil", 7),
          ("vInfrared", 6),
          ("vMicro-din", 4),
          ("vMini-din", 3),
          ("vOther", 1),
          ("vPc-98", 160),
          ("vPs2", 5),
          ("vUnknown", 2))
    )


_A92KeyboardConnectorType_Type.__name__ = "Integer32"
_A92KeyboardConnectorType_Object = MibTableColumn
a92KeyboardConnectorType = _A92KeyboardConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92, 1, 3),
    _A92KeyboardConnectorType_Type()
)
a92KeyboardConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a92KeyboardConnectorType.setStatus("mandatory")
_A92FruGroupIndex_Type = DmiInteger
_A92FruGroupIndex_Object = MibTableColumn
a92FruGroupIndex = _A92FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92, 1, 4),
    _A92FruGroupIndex_Type()
)
a92FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a92FruGroupIndex.setStatus("mandatory")
_A92OperationalGroupIndex_Type = DmiInteger
_A92OperationalGroupIndex_Object = MibTableColumn
a92OperationalGroupIndex = _A92OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92, 1, 5),
    _A92OperationalGroupIndex_Type()
)
a92OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a92OperationalGroupIndex.setStatus("mandatory")


class _A92SecuritySettings_Type(Integer32):
    """Custom type a92SecuritySettings based on Integer32"""
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
        *(("vExternalInterfaceEnabled", 5),
          ("vExternalInterfaceLockedOut", 4),
          ("vNone", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A92SecuritySettings_Type.__name__ = "Integer32"
_A92SecuritySettings_Object = MibTableColumn
a92SecuritySettings = _A92SecuritySettings_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 92, 1, 6),
    _A92SecuritySettings_Type()
)
a92SecuritySettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a92SecuritySettings.setStatus("mandatory")
_TEventGenerationForProcessor_Object = MibTable
tEventGenerationForProcessor = _TEventGenerationForProcessor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100)
)
if mibBuilder.loadTexts:
    tEventGenerationForProcessor.setStatus("mandatory")
_EEventGenerationForProcessor_Object = MibTableRow
eEventGenerationForProcessor = _EEventGenerationForProcessor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1)
)
eEventGenerationForProcessor.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a100AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForProcessor.setStatus("mandatory")


class _A100EventType_Type(Integer32):
    """Custom type a100EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              257,
              258)
        )
    )
    namedValues = NamedValues(
        *(("vProcessorFrb-3Failure", 258),
          ("vProcessorInternalError", 256),
          ("vProcessorThermalTrip", 257))
    )


_A100EventType_Type.__name__ = "Integer32"
_A100EventType_Object = MibTableColumn
a100EventType = _A100EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 1),
    _A100EventType_Type()
)
a100EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventType.setStatus("mandatory")


class _A100EventSeverity_Type(Integer32):
    """Custom type a100EventSeverity based on Integer32"""
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
          ("vNon-critical1", 8),
          ("vNon-recoverable", 32),
          ("vOk", 4))
    )


_A100EventSeverity_Type.__name__ = "Integer32"
_A100EventSeverity_Object = MibTableColumn
a100EventSeverity = _A100EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 2),
    _A100EventSeverity_Type()
)
a100EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventSeverity.setStatus("mandatory")


class _A100IsEventState_based_Type(Integer32):
    """Custom type a100IsEventState_based based on Integer32"""
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


_A100IsEventState_based_Type.__name__ = "Integer32"
_A100IsEventState_based_Object = MibScalar
a100IsEventState_based = _A100IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 3),
    _A100IsEventState_based_Type()
)
a100IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100IsEventState_based.setStatus("mandatory")
_A100EventStateKey_Type = DmiInteger
_A100EventStateKey_Object = MibTableColumn
a100EventStateKey = _A100EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 4),
    _A100EventStateKey_Type()
)
a100EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventStateKey.setStatus("mandatory")
_A100AssociatedGroup_Type = DmiDisplaystring
_A100AssociatedGroup_Object = MibTableColumn
a100AssociatedGroup = _A100AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 5),
    _A100AssociatedGroup_Type()
)
a100AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100AssociatedGroup.setStatus("mandatory")


class _A100EventSystem_Type(Integer32):
    """Custom type a100EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A100EventSystem_Type.__name__ = "Integer32"
_A100EventSystem_Object = MibTableColumn
a100EventSystem = _A100EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 6),
    _A100EventSystem_Type()
)
a100EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventSystem.setStatus("mandatory")


class _A100EventSubsystem_Type(Integer32):
    """Custom type a100EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A100EventSubsystem_Type.__name__ = "Integer32"
_A100EventSubsystem_Object = MibTableColumn
a100EventSubsystem = _A100EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 7),
    _A100EventSubsystem_Type()
)
a100EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventSubsystem.setStatus("mandatory")


class _A100IsInstanceDataPresent_Type(Integer32):
    """Custom type a100IsInstanceDataPresent based on Integer32"""
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


_A100IsInstanceDataPresent_Type.__name__ = "Integer32"
_A100IsInstanceDataPresent_Object = MibTableColumn
a100IsInstanceDataPresent = _A100IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 9),
    _A100IsInstanceDataPresent_Type()
)
a100IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100IsInstanceDataPresent.setStatus("mandatory")
_A100EventMessage_Type = DmiDisplaystring
_A100EventMessage_Object = MibTableColumn
a100EventMessage = _A100EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 10),
    _A100EventMessage_Type()
)
a100EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a100EventMessage.setStatus("mandatory")
_TEventGenerationForPowerSupply_Object = MibTable
tEventGenerationForPowerSupply = _TEventGenerationForPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104)
)
if mibBuilder.loadTexts:
    tEventGenerationForPowerSupply.setStatus("mandatory")
_EEventGenerationForPowerSupply_Object = MibTableRow
eEventGenerationForPowerSupply = _EEventGenerationForPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1)
)
eEventGenerationForPowerSupply.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a104AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForPowerSupply.setStatus("mandatory")


class _A104EventType_Type(Integer32):
    """Custom type a104EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              257,
              258)
        )
    )
    namedValues = NamedValues(
        *(("vPowerSupplyFailed", 256),
          ("vPowerSupplyLikelyToFail", 258),
          ("vPowerSupplyOk", 257))
    )


_A104EventType_Type.__name__ = "Integer32"
_A104EventType_Object = MibTableColumn
a104EventType = _A104EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 1),
    _A104EventType_Type()
)
a104EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventType.setStatus("mandatory")


class _A104EventSeverity_Type(Integer32):
    """Custom type a104EventSeverity based on Integer32"""
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


_A104EventSeverity_Type.__name__ = "Integer32"
_A104EventSeverity_Object = MibTableColumn
a104EventSeverity = _A104EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 2),
    _A104EventSeverity_Type()
)
a104EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSeverity.setStatus("mandatory")


class _A104IsEventState_based_Type(Integer32):
    """Custom type a104IsEventState_based based on Integer32"""
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


_A104IsEventState_based_Type.__name__ = "Integer32"
_A104IsEventState_based_Object = MibScalar
a104IsEventState_based = _A104IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 3),
    _A104IsEventState_based_Type()
)
a104IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104IsEventState_based.setStatus("mandatory")
_A104EventStateKey_Type = DmiInteger
_A104EventStateKey_Object = MibTableColumn
a104EventStateKey = _A104EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 4),
    _A104EventStateKey_Type()
)
a104EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventStateKey.setStatus("mandatory")
_A104AssociatedGroup_Type = DmiDisplaystring
_A104AssociatedGroup_Object = MibTableColumn
a104AssociatedGroup = _A104AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 5),
    _A104AssociatedGroup_Type()
)
a104AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104AssociatedGroup.setStatus("mandatory")


class _A104EventSystem_Type(Integer32):
    """Custom type a104EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A104EventSystem_Type.__name__ = "Integer32"
_A104EventSystem_Object = MibTableColumn
a104EventSystem = _A104EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 6),
    _A104EventSystem_Type()
)
a104EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSystem.setStatus("mandatory")


class _A104EventSubsystem_Type(Integer32):
    """Custom type a104EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A104EventSubsystem_Type.__name__ = "Integer32"
_A104EventSubsystem_Object = MibTableColumn
a104EventSubsystem = _A104EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 7),
    _A104EventSubsystem_Type()
)
a104EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSubsystem.setStatus("mandatory")


class _A104IsInstanceDataPresent_Type(Integer32):
    """Custom type a104IsInstanceDataPresent based on Integer32"""
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


_A104IsInstanceDataPresent_Type.__name__ = "Integer32"
_A104IsInstanceDataPresent_Object = MibTableColumn
a104IsInstanceDataPresent = _A104IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 9),
    _A104IsInstanceDataPresent_Type()
)
a104IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104IsInstanceDataPresent.setStatus("mandatory")
_A104EventMessage_Type = DmiDisplaystring
_A104EventMessage_Object = MibTableColumn
a104EventMessage = _A104EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 10),
    _A104EventMessage_Type()
)
a104EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventMessage.setStatus("mandatory")
_TEventGenerationForPhysicalMemory_Object = MibTable
tEventGenerationForPhysicalMemory = _TEventGenerationForPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108)
)
if mibBuilder.loadTexts:
    tEventGenerationForPhysicalMemory.setStatus("mandatory")
_EEventGenerationForPhysicalMemory_Object = MibTableRow
eEventGenerationForPhysicalMemory = _EEventGenerationForPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1)
)
eEventGenerationForPhysicalMemory.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a108AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForPhysicalMemory.setStatus("mandatory")


class _A108EventType_Type(Integer32):
    """Custom type a108EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              257)
        )
    )
    namedValues = NamedValues(
        *(("vMulti-bitMemoryErrorFromPreviousBoot", 257),
          ("vSingle-bitMemoryError", 256))
    )


_A108EventType_Type.__name__ = "Integer32"
_A108EventType_Object = MibTableColumn
a108EventType = _A108EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 1),
    _A108EventType_Type()
)
a108EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventType.setStatus("mandatory")


class _A108EventSeverity_Type(Integer32):
    """Custom type a108EventSeverity based on Integer32"""
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


_A108EventSeverity_Type.__name__ = "Integer32"
_A108EventSeverity_Object = MibTableColumn
a108EventSeverity = _A108EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 2),
    _A108EventSeverity_Type()
)
a108EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventSeverity.setStatus("mandatory")


class _A108IsEventState_based_Type(Integer32):
    """Custom type a108IsEventState_based based on Integer32"""
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


_A108IsEventState_based_Type.__name__ = "Integer32"
_A108IsEventState_based_Object = MibScalar
a108IsEventState_based = _A108IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 3),
    _A108IsEventState_based_Type()
)
a108IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108IsEventState_based.setStatus("mandatory")
_A108EventStateKey_Type = DmiInteger
_A108EventStateKey_Object = MibTableColumn
a108EventStateKey = _A108EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 4),
    _A108EventStateKey_Type()
)
a108EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventStateKey.setStatus("mandatory")
_A108AssociatedGroup_Type = DmiDisplaystring
_A108AssociatedGroup_Object = MibTableColumn
a108AssociatedGroup = _A108AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 5),
    _A108AssociatedGroup_Type()
)
a108AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108AssociatedGroup.setStatus("mandatory")


class _A108EventSystem_Type(Integer32):
    """Custom type a108EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A108EventSystem_Type.__name__ = "Integer32"
_A108EventSystem_Object = MibTableColumn
a108EventSystem = _A108EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 6),
    _A108EventSystem_Type()
)
a108EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventSystem.setStatus("mandatory")


class _A108EventSubsystem_Type(Integer32):
    """Custom type a108EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A108EventSubsystem_Type.__name__ = "Integer32"
_A108EventSubsystem_Object = MibTableColumn
a108EventSubsystem = _A108EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 7),
    _A108EventSubsystem_Type()
)
a108EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventSubsystem.setStatus("mandatory")


class _A108IsInstanceDataPresent_Type(Integer32):
    """Custom type a108IsInstanceDataPresent based on Integer32"""
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


_A108IsInstanceDataPresent_Type.__name__ = "Integer32"
_A108IsInstanceDataPresent_Object = MibTableColumn
a108IsInstanceDataPresent = _A108IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 9),
    _A108IsInstanceDataPresent_Type()
)
a108IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108IsInstanceDataPresent.setStatus("mandatory")
_A108EventMessage_Type = DmiDisplaystring
_A108EventMessage_Object = MibTableColumn
a108EventMessage = _A108EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 10),
    _A108EventMessage_Type()
)
a108EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventMessage.setStatus("mandatory")
_TEventGenerationForVoltageProbe_Object = MibTable
tEventGenerationForVoltageProbe = _TEventGenerationForVoltageProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113)
)
if mibBuilder.loadTexts:
    tEventGenerationForVoltageProbe.setStatus("mandatory")
_EEventGenerationForVoltageProbe_Object = MibTableRow
eEventGenerationForVoltageProbe = _EEventGenerationForVoltageProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1)
)
eEventGenerationForVoltageProbe.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForVoltageProbe.setStatus("mandatory")


class _A113EventType_Type(Integer32):
    """Custom type a113EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              257,
              258,
              259,
              260,
              261,
              262)
        )
    )
    namedValues = NamedValues(
        *(("vStatusChangedFromLowerCriticalToLowerNo", 262),
          ("vStatusChangedFromOkToLowerNon-critical", 260),
          ("vStatusChangedFromOkToUpperNon-critical", 259),
          ("vStatusChangedFromUpperCriticalToUpperNo", 261),
          ("vStatusChangedToLowerCritical", 258),
          ("vStatusChangedToOk", 256),
          ("vStatusChangedToUpperCritical", 257))
    )


_A113EventType_Type.__name__ = "Integer32"
_A113EventType_Object = MibTableColumn
a113EventType = _A113EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 1),
    _A113EventType_Type()
)
a113EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113EventType.setStatus("mandatory")


class _A113EventSeverity_Type(Integer32):
    """Custom type a113EventSeverity based on Integer32"""
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


_A113EventSeverity_Type.__name__ = "Integer32"
_A113EventSeverity_Object = MibTableColumn
a113EventSeverity = _A113EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 2),
    _A113EventSeverity_Type()
)
a113EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113EventSeverity.setStatus("mandatory")


class _A113IsEventState_based_Type(Integer32):
    """Custom type a113IsEventState_based based on Integer32"""
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


_A113IsEventState_based_Type.__name__ = "Integer32"
_A113IsEventState_based_Object = MibScalar
a113IsEventState_based = _A113IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 3),
    _A113IsEventState_based_Type()
)
a113IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113IsEventState_based.setStatus("mandatory")
_A113EventStateKey_Type = DmiInteger
_A113EventStateKey_Object = MibTableColumn
a113EventStateKey = _A113EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 4),
    _A113EventStateKey_Type()
)
a113EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113EventStateKey.setStatus("mandatory")
_A113AssociatedGroup_Type = DmiDisplaystring
_A113AssociatedGroup_Object = MibTableColumn
a113AssociatedGroup = _A113AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 5),
    _A113AssociatedGroup_Type()
)
a113AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113AssociatedGroup.setStatus("mandatory")


class _A113EventSystem_Type(Integer32):
    """Custom type a113EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A113EventSystem_Type.__name__ = "Integer32"
_A113EventSystem_Object = MibTableColumn
a113EventSystem = _A113EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 6),
    _A113EventSystem_Type()
)
a113EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113EventSystem.setStatus("mandatory")


class _A113EventSubsystem_Type(Integer32):
    """Custom type a113EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A113EventSubsystem_Type.__name__ = "Integer32"
_A113EventSubsystem_Object = MibTableColumn
a113EventSubsystem = _A113EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 7),
    _A113EventSubsystem_Type()
)
a113EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113EventSubsystem.setStatus("mandatory")


class _A113IsInstanceDataPresent_Type(Integer32):
    """Custom type a113IsInstanceDataPresent based on Integer32"""
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


_A113IsInstanceDataPresent_Type.__name__ = "Integer32"
_A113IsInstanceDataPresent_Object = MibTableColumn
a113IsInstanceDataPresent = _A113IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 9),
    _A113IsInstanceDataPresent_Type()
)
a113IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113IsInstanceDataPresent.setStatus("mandatory")
_A113EventMessage_Type = DmiDisplaystring
_A113EventMessage_Object = MibTableColumn
a113EventMessage = _A113EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 10),
    _A113EventMessage_Type()
)
a113EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a113EventMessage.setStatus("mandatory")
_TEventGenerationForTemperatureProbe_Object = MibTable
tEventGenerationForTemperatureProbe = _TEventGenerationForTemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114)
)
if mibBuilder.loadTexts:
    tEventGenerationForTemperatureProbe.setStatus("mandatory")
_EEventGenerationForTemperatureProbe_Object = MibTableRow
eEventGenerationForTemperatureProbe = _EEventGenerationForTemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1)
)
eEventGenerationForTemperatureProbe.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForTemperatureProbe.setStatus("mandatory")


class _A114EventType_Type(Integer32):
    """Custom type a114EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              257,
              258,
              259,
              260,
              261,
              262)
        )
    )
    namedValues = NamedValues(
        *(("vStatusChangedFromLowerCriticalToLowerNo", 262),
          ("vStatusChangedFromOkToLowerNon-critical", 260),
          ("vStatusChangedFromOkToUpperNon-critical", 259),
          ("vStatusChangedFromUpperCriticalToUpperNo", 261),
          ("vStatusChangedToLowerCritical", 258),
          ("vStatusChangedToOk", 256),
          ("vStatusChangedToUpperCritical", 257))
    )


_A114EventType_Type.__name__ = "Integer32"
_A114EventType_Object = MibTableColumn
a114EventType = _A114EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 1),
    _A114EventType_Type()
)
a114EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114EventType.setStatus("mandatory")


class _A114EventSeverity_Type(Integer32):
    """Custom type a114EventSeverity based on Integer32"""
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


_A114EventSeverity_Type.__name__ = "Integer32"
_A114EventSeverity_Object = MibTableColumn
a114EventSeverity = _A114EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 2),
    _A114EventSeverity_Type()
)
a114EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114EventSeverity.setStatus("mandatory")


class _A114IsEventState_based_Type(Integer32):
    """Custom type a114IsEventState_based based on Integer32"""
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


_A114IsEventState_based_Type.__name__ = "Integer32"
_A114IsEventState_based_Object = MibScalar
a114IsEventState_based = _A114IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 3),
    _A114IsEventState_based_Type()
)
a114IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114IsEventState_based.setStatus("mandatory")
_A114EventStateKey_Type = DmiInteger
_A114EventStateKey_Object = MibTableColumn
a114EventStateKey = _A114EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 4),
    _A114EventStateKey_Type()
)
a114EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114EventStateKey.setStatus("mandatory")
_A114AssociatedGroup_Type = DmiDisplaystring
_A114AssociatedGroup_Object = MibTableColumn
a114AssociatedGroup = _A114AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 5),
    _A114AssociatedGroup_Type()
)
a114AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114AssociatedGroup.setStatus("mandatory")


class _A114EventSystem_Type(Integer32):
    """Custom type a114EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A114EventSystem_Type.__name__ = "Integer32"
_A114EventSystem_Object = MibTableColumn
a114EventSystem = _A114EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 6),
    _A114EventSystem_Type()
)
a114EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114EventSystem.setStatus("mandatory")


class _A114EventSubsystem_Type(Integer32):
    """Custom type a114EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A114EventSubsystem_Type.__name__ = "Integer32"
_A114EventSubsystem_Object = MibTableColumn
a114EventSubsystem = _A114EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 7),
    _A114EventSubsystem_Type()
)
a114EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114EventSubsystem.setStatus("mandatory")


class _A114IsInstanceDataPresent_Type(Integer32):
    """Custom type a114IsInstanceDataPresent based on Integer32"""
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


_A114IsInstanceDataPresent_Type.__name__ = "Integer32"
_A114IsInstanceDataPresent_Object = MibTableColumn
a114IsInstanceDataPresent = _A114IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 9),
    _A114IsInstanceDataPresent_Type()
)
a114IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114IsInstanceDataPresent.setStatus("mandatory")
_A114EventMessage_Type = DmiDisplaystring
_A114EventMessage_Object = MibTableColumn
a114EventMessage = _A114EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 10),
    _A114EventMessage_Type()
)
a114EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a114EventMessage.setStatus("mandatory")
_TEventGenerationForPhysicalContainer_Object = MibTable
tEventGenerationForPhysicalContainer = _TEventGenerationForPhysicalContainer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116)
)
if mibBuilder.loadTexts:
    tEventGenerationForPhysicalContainer.setStatus("mandatory")
_EEventGenerationForPhysicalContainer_Object = MibTableRow
eEventGenerationForPhysicalContainer = _EEventGenerationForPhysicalContainer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1)
)
eEventGenerationForPhysicalContainer.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a116AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForPhysicalContainer.setStatus("mandatory")


class _A116EventType_Type(Integer32):
    """Custom type a116EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              256)
        )
    )
    namedValues = NamedValues(
        *(("vContainerSecurityBreach", 6),
          ("vContainerSecurityStatusOk", 256))
    )


_A116EventType_Type.__name__ = "Integer32"
_A116EventType_Object = MibTableColumn
a116EventType = _A116EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 1),
    _A116EventType_Type()
)
a116EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventType.setStatus("mandatory")


class _A116EventSeverity_Type(Integer32):
    """Custom type a116EventSeverity based on Integer32"""
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


_A116EventSeverity_Type.__name__ = "Integer32"
_A116EventSeverity_Object = MibTableColumn
a116EventSeverity = _A116EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 2),
    _A116EventSeverity_Type()
)
a116EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventSeverity.setStatus("mandatory")


class _A116IsEventState_based_Type(Integer32):
    """Custom type a116IsEventState_based based on Integer32"""
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


_A116IsEventState_based_Type.__name__ = "Integer32"
_A116IsEventState_based_Object = MibScalar
a116IsEventState_based = _A116IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 3),
    _A116IsEventState_based_Type()
)
a116IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116IsEventState_based.setStatus("mandatory")
_A116EventStateKey_Type = DmiInteger
_A116EventStateKey_Object = MibTableColumn
a116EventStateKey = _A116EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 4),
    _A116EventStateKey_Type()
)
a116EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventStateKey.setStatus("mandatory")
_A116AssociatedGroup_Type = DmiDisplaystring
_A116AssociatedGroup_Object = MibTableColumn
a116AssociatedGroup = _A116AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 5),
    _A116AssociatedGroup_Type()
)
a116AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116AssociatedGroup.setStatus("mandatory")


class _A116EventSystem_Type(Integer32):
    """Custom type a116EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A116EventSystem_Type.__name__ = "Integer32"
_A116EventSystem_Object = MibTableColumn
a116EventSystem = _A116EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 6),
    _A116EventSystem_Type()
)
a116EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventSystem.setStatus("mandatory")


class _A116EventSubsystem_Type(Integer32):
    """Custom type a116EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A116EventSubsystem_Type.__name__ = "Integer32"
_A116EventSubsystem_Object = MibTableColumn
a116EventSubsystem = _A116EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 7),
    _A116EventSubsystem_Type()
)
a116EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventSubsystem.setStatus("mandatory")


class _A116IsInstanceDataPresent_Type(Integer32):
    """Custom type a116IsInstanceDataPresent based on Integer32"""
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


_A116IsInstanceDataPresent_Type.__name__ = "Integer32"
_A116IsInstanceDataPresent_Object = MibTableColumn
a116IsInstanceDataPresent = _A116IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 9),
    _A116IsInstanceDataPresent_Type()
)
a116IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116IsInstanceDataPresent.setStatus("mandatory")
_A116EventMessage_Type = DmiDisplaystring
_A116EventMessage_Object = MibTableColumn
a116EventMessage = _A116EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 10),
    _A116EventMessage_Type()
)
a116EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a116EventMessage.setStatus("mandatory")
_TBusGlobalTable_Object = MibTable
tBusGlobalTable = _TBusGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 128)
)
if mibBuilder.loadTexts:
    tBusGlobalTable.setStatus("mandatory")
_EBusGlobalTable_Object = MibTableRow
eBusGlobalTable = _EBusGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 128, 1)
)
eBusGlobalTable.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a128BusId"),
)
if mibBuilder.loadTexts:
    eBusGlobalTable.setStatus("mandatory")
_A128BusId_Type = DmiInteger
_A128BusId_Object = MibTableColumn
a128BusId = _A128BusId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 128, 1, 1),
    _A128BusId_Type()
)
a128BusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a128BusId.setStatus("mandatory")


class _A128BusType_Type(Integer32):
    """Custom type a128BusType based on Integer32"""
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
        *(("vDiagnostic", 8),
          ("vEisa", 3),
          ("vI2c", 9),
          ("vIde", 7),
          ("vIsa", 4),
          ("vOther", 1),
          ("vPci", 5),
          ("vPower", 10),
          ("vScsi", 6),
          ("vUnknown", 2))
    )


_A128BusType_Type.__name__ = "Integer32"
_A128BusType_Object = MibTableColumn
a128BusType = _A128BusType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 128, 1, 2),
    _A128BusType_Type()
)
a128BusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a128BusType.setStatus("mandatory")
_TPhysicalExpansionSitesTable_Object = MibTable
tPhysicalExpansionSitesTable = _TPhysicalExpansionSitesTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129)
)
if mibBuilder.loadTexts:
    tPhysicalExpansionSitesTable.setStatus("mandatory")
_EPhysicalExpansionSitesTable_Object = MibTableRow
ePhysicalExpansionSitesTable = _EPhysicalExpansionSitesTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129, 1)
)
ePhysicalExpansionSitesTable.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a129ExpansionSiteIndex"),
)
if mibBuilder.loadTexts:
    ePhysicalExpansionSitesTable.setStatus("mandatory")
_A129ExpansionSiteIndex_Type = DmiInteger
_A129ExpansionSiteIndex_Object = MibTableColumn
a129ExpansionSiteIndex = _A129ExpansionSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129, 1, 1),
    _A129ExpansionSiteIndex_Type()
)
a129ExpansionSiteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a129ExpansionSiteIndex.setStatus("mandatory")


class _A129ExpansionSiteType_Type(Integer32):
    """Custom type a129ExpansionSiteType based on Integer32"""
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
        *(("vBusSlot", 3),
          ("vDriveBay", 4),
          ("vOther", 1),
          ("vPcmciaSlot", 7),
          ("vPowerUnitBay", 5),
          ("vSubchassisSlot", 6),
          ("vUnknown", 2))
    )


_A129ExpansionSiteType_Type.__name__ = "Integer32"
_A129ExpansionSiteType_Object = MibTableColumn
a129ExpansionSiteType = _A129ExpansionSiteType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129, 1, 2),
    _A129ExpansionSiteType_Type()
)
a129ExpansionSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a129ExpansionSiteType.setStatus("mandatory")


class _A129VirtualExpansionSite_Type(Integer32):
    """Custom type a129VirtualExpansionSite based on Integer32"""
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


_A129VirtualExpansionSite_Type.__name__ = "Integer32"
_A129VirtualExpansionSite_Object = MibTableColumn
a129VirtualExpansionSite = _A129VirtualExpansionSite_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129, 1, 3),
    _A129VirtualExpansionSite_Type()
)
a129VirtualExpansionSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a129VirtualExpansionSite.setStatus("mandatory")
_A129ExpansionSiteName_Type = DmiDisplaystring
_A129ExpansionSiteName_Object = MibTableColumn
a129ExpansionSiteName = _A129ExpansionSiteName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129, 1, 4),
    _A129ExpansionSiteName_Type()
)
a129ExpansionSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a129ExpansionSiteName.setStatus("mandatory")
_A129ExpansionSiteDescription_Type = DmiDisplaystring
_A129ExpansionSiteDescription_Object = MibTableColumn
a129ExpansionSiteDescription = _A129ExpansionSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129, 1, 5),
    _A129ExpansionSiteDescription_Type()
)
a129ExpansionSiteDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a129ExpansionSiteDescription.setStatus("mandatory")


class _A129ExpansionSiteCurrentlyOccupied_Type(Integer32):
    """Custom type a129ExpansionSiteCurrentlyOccupied based on Integer32"""
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


_A129ExpansionSiteCurrentlyOccupied_Type.__name__ = "Integer32"
_A129ExpansionSiteCurrentlyOccupied_Object = MibTableColumn
a129ExpansionSiteCurrentlyOccupied = _A129ExpansionSiteCurrentlyOccupied_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 129, 1, 6),
    _A129ExpansionSiteCurrentlyOccupied_Type()
)
a129ExpansionSiteCurrentlyOccupied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a129ExpansionSiteCurrentlyOccupied.setStatus("mandatory")
_TEventGenerationForCoolingDevice_Object = MibTable
tEventGenerationForCoolingDevice = _TEventGenerationForCoolingDevice_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140)
)
if mibBuilder.loadTexts:
    tEventGenerationForCoolingDevice.setStatus("mandatory")
_EEventGenerationForCoolingDevice_Object = MibTableRow
eEventGenerationForCoolingDevice = _EEventGenerationForCoolingDevice_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1)
)
eEventGenerationForCoolingDevice.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a140AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForCoolingDevice.setStatus("mandatory")


class _A140EventType_Type(Integer32):
    """Custom type a140EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vCoolingDeviceStatusChange", 1),
          ("vTemperatureFault", 2))
    )


_A140EventType_Type.__name__ = "Integer32"
_A140EventType_Object = MibTableColumn
a140EventType = _A140EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1, 1),
    _A140EventType_Type()
)
a140EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a140EventType.setStatus("mandatory")


class _A140EventSeverity_Type(Integer32):
    """Custom type a140EventSeverity based on Integer32"""
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


_A140EventSeverity_Type.__name__ = "Integer32"
_A140EventSeverity_Object = MibTableColumn
a140EventSeverity = _A140EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1, 2),
    _A140EventSeverity_Type()
)
a140EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a140EventSeverity.setStatus("mandatory")


class _A140IsEventState_based_Type(Integer32):
    """Custom type a140IsEventState_based based on Integer32"""
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


_A140IsEventState_based_Type.__name__ = "Integer32"
_A140IsEventState_based_Object = MibScalar
a140IsEventState_based = _A140IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1, 3),
    _A140IsEventState_based_Type()
)
a140IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a140IsEventState_based.setStatus("mandatory")
_A140EventStateKey_Type = DmiInteger
_A140EventStateKey_Object = MibTableColumn
a140EventStateKey = _A140EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1, 4),
    _A140EventStateKey_Type()
)
a140EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a140EventStateKey.setStatus("mandatory")
_A140AssociatedGroup_Type = DmiDisplaystring
_A140AssociatedGroup_Object = MibTableColumn
a140AssociatedGroup = _A140AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1, 5),
    _A140AssociatedGroup_Type()
)
a140AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a140AssociatedGroup.setStatus("mandatory")


class _A140EventSystem_Type(Integer32):
    """Custom type a140EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A140EventSystem_Type.__name__ = "Integer32"
_A140EventSystem_Object = MibTableColumn
a140EventSystem = _A140EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1, 6),
    _A140EventSystem_Type()
)
a140EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a140EventSystem.setStatus("mandatory")


class _A140EventSubsystem_Type(Integer32):
    """Custom type a140EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A140EventSubsystem_Type.__name__ = "Integer32"
_A140EventSubsystem_Object = MibTableColumn
a140EventSubsystem = _A140EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 140, 1, 7),
    _A140EventSubsystem_Type()
)
a140EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a140EventSubsystem.setStatus("mandatory")
_TEventGenerationForPowerUnit_Object = MibTable
tEventGenerationForPowerUnit = _TEventGenerationForPowerUnit_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201)
)
if mibBuilder.loadTexts:
    tEventGenerationForPowerUnit.setStatus("mandatory")
_EEventGenerationForPowerUnit_Object = MibTableRow
eEventGenerationForPowerUnit = _EEventGenerationForPowerUnit_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1)
)
eEventGenerationForPowerUnit.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a201AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForPowerUnit.setStatus("mandatory")


class _A201EventType_Type(Integer32):
    """Custom type a201EventType based on Integer32"""
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
        *(("vPowerUnitRedundancyDegraded", 3),
          ("vPowerUnitRedundancyLost", 1),
          ("vPowerUnitRedundancyRegained", 2),
          ("vPowerUnitVaShutdownConditionCleared", 4),
          ("vPowerUnitVaShutdownLimitExceeded", 5))
    )


_A201EventType_Type.__name__ = "Integer32"
_A201EventType_Object = MibTableColumn
a201EventType = _A201EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 1),
    _A201EventType_Type()
)
a201EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201EventType.setStatus("mandatory")


class _A201EventSeverity_Type(Integer32):
    """Custom type a201EventSeverity based on Integer32"""
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


_A201EventSeverity_Type.__name__ = "Integer32"
_A201EventSeverity_Object = MibTableColumn
a201EventSeverity = _A201EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 2),
    _A201EventSeverity_Type()
)
a201EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201EventSeverity.setStatus("mandatory")


class _A201IsEventState_based_Type(Integer32):
    """Custom type a201IsEventState_based based on Integer32"""
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


_A201IsEventState_based_Type.__name__ = "Integer32"
_A201IsEventState_based_Object = MibScalar
a201IsEventState_based = _A201IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 3),
    _A201IsEventState_based_Type()
)
a201IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201IsEventState_based.setStatus("mandatory")
_A201EventStateKey_Type = DmiInteger
_A201EventStateKey_Object = MibTableColumn
a201EventStateKey = _A201EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 4),
    _A201EventStateKey_Type()
)
a201EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201EventStateKey.setStatus("mandatory")
_A201AssociatedGroup_Type = DmiDisplaystring
_A201AssociatedGroup_Object = MibTableColumn
a201AssociatedGroup = _A201AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 5),
    _A201AssociatedGroup_Type()
)
a201AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201AssociatedGroup.setStatus("mandatory")


class _A201EventSystem_Type(Integer32):
    """Custom type a201EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A201EventSystem_Type.__name__ = "Integer32"
_A201EventSystem_Object = MibTableColumn
a201EventSystem = _A201EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 6),
    _A201EventSystem_Type()
)
a201EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201EventSystem.setStatus("mandatory")


class _A201EventSubsystem_Type(Integer32):
    """Custom type a201EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A201EventSubsystem_Type.__name__ = "Integer32"
_A201EventSubsystem_Object = MibTableColumn
a201EventSubsystem = _A201EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 7),
    _A201EventSubsystem_Type()
)
a201EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201EventSubsystem.setStatus("mandatory")


class _A201IsInstanceDataPresent_Type(Integer32):
    """Custom type a201IsInstanceDataPresent based on Integer32"""
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


_A201IsInstanceDataPresent_Type.__name__ = "Integer32"
_A201IsInstanceDataPresent_Object = MibTableColumn
a201IsInstanceDataPresent = _A201IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 9),
    _A201IsInstanceDataPresent_Type()
)
a201IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201IsInstanceDataPresent.setStatus("mandatory")
_A201EventMessage_Type = DmiDisplaystring
_A201EventMessage_Object = MibTableColumn
a201EventMessage = _A201EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 10),
    _A201EventMessage_Type()
)
a201EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a201EventMessage.setStatus("mandatory")
_TEventGenerationForCoolingSensors_Object = MibTable
tEventGenerationForCoolingSensors = _TEventGenerationForCoolingSensors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202)
)
if mibBuilder.loadTexts:
    tEventGenerationForCoolingSensors.setStatus("mandatory")
_EEventGenerationForCoolingSensors_Object = MibTableRow
eEventGenerationForCoolingSensors = _EEventGenerationForCoolingSensors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1)
)
eEventGenerationForCoolingSensors.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a202AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eEventGenerationForCoolingSensors.setStatus("mandatory")


class _A202EventType_Type(Integer32):
    """Custom type a202EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              257)
        )
    )
    namedValues = NamedValues(
        *(("vCoolingDeviceFailure", 256),
          ("vCoolingDeviceOk", 257))
    )


_A202EventType_Type.__name__ = "Integer32"
_A202EventType_Object = MibTableColumn
a202EventType = _A202EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 1),
    _A202EventType_Type()
)
a202EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202EventType.setStatus("mandatory")


class _A202EventSeverity_Type(Integer32):
    """Custom type a202EventSeverity based on Integer32"""
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


_A202EventSeverity_Type.__name__ = "Integer32"
_A202EventSeverity_Object = MibTableColumn
a202EventSeverity = _A202EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 2),
    _A202EventSeverity_Type()
)
a202EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202EventSeverity.setStatus("mandatory")


class _A202IsEventState_based_Type(Integer32):
    """Custom type a202IsEventState_based based on Integer32"""
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


_A202IsEventState_based_Type.__name__ = "Integer32"
_A202IsEventState_based_Object = MibScalar
a202IsEventState_based = _A202IsEventState_based_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 3),
    _A202IsEventState_based_Type()
)
a202IsEventState_based.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202IsEventState_based.setStatus("mandatory")
_A202EventStateKey_Type = DmiInteger
_A202EventStateKey_Object = MibTableColumn
a202EventStateKey = _A202EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 4),
    _A202EventStateKey_Type()
)
a202EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202EventStateKey.setStatus("mandatory")
_A202AssociatedGroup_Type = DmiDisplaystring
_A202AssociatedGroup_Object = MibTableColumn
a202AssociatedGroup = _A202AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 5),
    _A202AssociatedGroup_Type()
)
a202AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202AssociatedGroup.setStatus("mandatory")


class _A202EventSystem_Type(Integer32):
    """Custom type a202EventSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A202EventSystem_Type.__name__ = "Integer32"
_A202EventSystem_Object = MibTableColumn
a202EventSystem = _A202EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 6),
    _A202EventSystem_Type()
)
a202EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202EventSystem.setStatus("mandatory")


class _A202EventSubsystem_Type(Integer32):
    """Custom type a202EventSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 0),
          ("vUnknown", 1))
    )


_A202EventSubsystem_Type.__name__ = "Integer32"
_A202EventSubsystem_Object = MibTableColumn
a202EventSubsystem = _A202EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 7),
    _A202EventSubsystem_Type()
)
a202EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202EventSubsystem.setStatus("mandatory")


class _A202IsInstanceDataPresent_Type(Integer32):
    """Custom type a202IsInstanceDataPresent based on Integer32"""
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


_A202IsInstanceDataPresent_Type.__name__ = "Integer32"
_A202IsInstanceDataPresent_Object = MibTableColumn
a202IsInstanceDataPresent = _A202IsInstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 9),
    _A202IsInstanceDataPresent_Type()
)
a202IsInstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202IsInstanceDataPresent.setStatus("mandatory")
_A202EventMessage_Type = DmiDisplaystring
_A202EventMessage_Object = MibTableColumn
a202EventMessage = _A202EventMessage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 10),
    _A202EventMessage_Type()
)
a202EventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a202EventMessage.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1001)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1001, 1)
)
eMiftomib.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A1001MibName_Type = DmiDisplaystring
_A1001MibName_Object = MibTableColumn
a1001MibName = _A1001MibName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1001, 1, 1),
    _A1001MibName_Type()
)
a1001MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibName.setStatus("mandatory")
_A1001MibOid_Type = DmiDisplaystring
_A1001MibOid_Object = MibTableColumn
a1001MibOid = _A1001MibOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1001, 1, 2),
    _A1001MibOid_Type()
)
a1001MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibOid.setStatus("mandatory")
_A1001DisableTrap_Type = DmiInteger
_A1001DisableTrap_Object = MibTableColumn
a1001DisableTrap = _A1001DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1001, 1, 3),
    _A1001DisableTrap_Type()
)
a1001DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1001DisableTrap.setStatus("mandatory")
_TSystemControl_Object = MibTable
tSystemControl = _TSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004)
)
if mibBuilder.loadTexts:
    tSystemControl.setStatus("mandatory")
_ESystemControl_Object = MibTableRow
eSystemControl = _ESystemControl_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1)
)
eSystemControl.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a1004Selfid"),
)
if mibBuilder.loadTexts:
    eSystemControl.setStatus("mandatory")
_A1004Selfid_Type = DmiInteger
_A1004Selfid_Object = MibTableColumn
a1004Selfid = _A1004Selfid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 1),
    _A1004Selfid_Type()
)
a1004Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004Selfid.setStatus("mandatory")


class _A1004ResetSystem_Type(Integer32):
    """Custom type a1004ResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotReset", 0),
          ("vInitiateReset", 1),
          ("vUnsupported", 2))
    )


_A1004ResetSystem_Type.__name__ = "Integer32"
_A1004ResetSystem_Object = MibTableColumn
a1004ResetSystem = _A1004ResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 2),
    _A1004ResetSystem_Type()
)
a1004ResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ResetSystem.setStatus("mandatory")
_A1004TimedResetIncrement_Type = DmiInteger
_A1004TimedResetIncrement_Object = MibTableColumn
a1004TimedResetIncrement = _A1004TimedResetIncrement_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 3),
    _A1004TimedResetIncrement_Type()
)
a1004TimedResetIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004TimedResetIncrement.setStatus("mandatory")
_A1004TimedResetResolution_Type = DmiInteger
_A1004TimedResetResolution_Object = MibTableColumn
a1004TimedResetResolution = _A1004TimedResetResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 4),
    _A1004TimedResetResolution_Type()
)
a1004TimedResetResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004TimedResetResolution.setStatus("mandatory")
_A1004TimeUntilSystemReset_Type = DmiInteger
_A1004TimeUntilSystemReset_Object = MibTableColumn
a1004TimeUntilSystemReset = _A1004TimeUntilSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 5),
    _A1004TimeUntilSystemReset_Type()
)
a1004TimeUntilSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004TimeUntilSystemReset.setStatus("mandatory")


class _A1004SystemPowerCapabilities_Type(Integer32):
    """Custom type a1004SystemPowerCapabilities based on Integer32"""
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
        *(("vOffOnly", 3),
          ("vOnAndOff", 2),
          ("vOnOnly", 4),
          ("vUnknown", 0),
          ("vUnsupported", 1))
    )


_A1004SystemPowerCapabilities_Type.__name__ = "Integer32"
_A1004SystemPowerCapabilities_Object = MibTableColumn
a1004SystemPowerCapabilities = _A1004SystemPowerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 6),
    _A1004SystemPowerCapabilities_Type()
)
a1004SystemPowerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004SystemPowerCapabilities.setStatus("mandatory")


class _A1004SystemPowerStatus_Type(Integer32):
    """Custom type a1004SystemPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1),
          ("vUnsupported", 2))
    )


_A1004SystemPowerStatus_Type.__name__ = "Integer32"
_A1004SystemPowerStatus_Object = MibTableColumn
a1004SystemPowerStatus = _A1004SystemPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 7),
    _A1004SystemPowerStatus_Type()
)
a1004SystemPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004SystemPowerStatus.setStatus("mandatory")


class _A1004EventLoggingCapability_Type(Integer32):
    """Custom type a1004EventLoggingCapability based on Integer32"""
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
        *(("vActive", 2),
          ("vInactive", 3),
          ("vUnknown", 0),
          ("vUnsupported", 1))
    )


_A1004EventLoggingCapability_Type.__name__ = "Integer32"
_A1004EventLoggingCapability_Object = MibTableColumn
a1004EventLoggingCapability = _A1004EventLoggingCapability_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 8),
    _A1004EventLoggingCapability_Type()
)
a1004EventLoggingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004EventLoggingCapability.setStatus("mandatory")
_A1004WatchdogTimerIncrement_Type = DmiInteger
_A1004WatchdogTimerIncrement_Object = MibTableColumn
a1004WatchdogTimerIncrement = _A1004WatchdogTimerIncrement_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 9),
    _A1004WatchdogTimerIncrement_Type()
)
a1004WatchdogTimerIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004WatchdogTimerIncrement.setStatus("mandatory")
_A1004WatchdogTimerResolution_Type = DmiInteger
_A1004WatchdogTimerResolution_Object = MibTableColumn
a1004WatchdogTimerResolution = _A1004WatchdogTimerResolution_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 10),
    _A1004WatchdogTimerResolution_Type()
)
a1004WatchdogTimerResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1004WatchdogTimerResolution.setStatus("mandatory")
_A1004WatchdogUpdateInterval_Type = DmiInteger
_A1004WatchdogUpdateInterval_Object = MibTableColumn
a1004WatchdogUpdateInterval = _A1004WatchdogUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 11),
    _A1004WatchdogUpdateInterval_Type()
)
a1004WatchdogUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004WatchdogUpdateInterval.setStatus("mandatory")


class _A1004UseSystemWatchdogFeature_Type(Integer32):
    """Custom type a1004UseSystemWatchdogFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1),
          ("vUnsupported", 2))
    )


_A1004UseSystemWatchdogFeature_Type.__name__ = "Integer32"
_A1004UseSystemWatchdogFeature_Object = MibTableColumn
a1004UseSystemWatchdogFeature = _A1004UseSystemWatchdogFeature_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 12),
    _A1004UseSystemWatchdogFeature_Type()
)
a1004UseSystemWatchdogFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004UseSystemWatchdogFeature.setStatus("mandatory")


class _A1004ResetSystemAfterDelay_Type(Integer32):
    """Custom type a1004ResetSystemAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1),
          ("vUnsupported", 2))
    )


_A1004ResetSystemAfterDelay_Type.__name__ = "Integer32"
_A1004ResetSystemAfterDelay_Object = MibTableColumn
a1004ResetSystemAfterDelay = _A1004ResetSystemAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 13),
    _A1004ResetSystemAfterDelay_Type()
)
a1004ResetSystemAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ResetSystemAfterDelay.setStatus("mandatory")


class _A1004SavePersistentData_Type(Integer32):
    """Custom type a1004SavePersistentData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1),
          ("vUnsupported", 2))
    )


_A1004SavePersistentData_Type.__name__ = "Integer32"
_A1004SavePersistentData_Object = MibTableColumn
a1004SavePersistentData = _A1004SavePersistentData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 15),
    _A1004SavePersistentData_Type()
)
a1004SavePersistentData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004SavePersistentData.setStatus("mandatory")


class _A1004RestoreFactoryDefaults_Type(Integer32):
    """Custom type a1004RestoreFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1),
          ("vUnsupported", 2))
    )


_A1004RestoreFactoryDefaults_Type.__name__ = "Integer32"
_A1004RestoreFactoryDefaults_Object = MibTableColumn
a1004RestoreFactoryDefaults = _A1004RestoreFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 16),
    _A1004RestoreFactoryDefaults_Type()
)
a1004RestoreFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004RestoreFactoryDefaults.setStatus("mandatory")


class _A1004ShutdownOs_Type(Integer32):
    """Custom type a1004ShutdownOs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotShutdown", 0),
          ("vShutdownOs", 1),
          ("vUnsupported", 2))
    )


_A1004ShutdownOs_Type.__name__ = "Integer32"
_A1004ShutdownOs_Object = MibTableColumn
a1004ShutdownOs = _A1004ShutdownOs_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 17),
    _A1004ShutdownOs_Type()
)
a1004ShutdownOs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ShutdownOs.setStatus("mandatory")


class _A1004ShutdownOsAndPowerOff_Type(Integer32):
    """Custom type a1004ShutdownOsAndPowerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotShutdownAndPowerOff", 0),
          ("vShutdownAndPowerOff", 1),
          ("vUnsupported", 2))
    )


_A1004ShutdownOsAndPowerOff_Type.__name__ = "Integer32"
_A1004ShutdownOsAndPowerOff_Object = MibTableColumn
a1004ShutdownOsAndPowerOff = _A1004ShutdownOsAndPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 18),
    _A1004ShutdownOsAndPowerOff_Type()
)
a1004ShutdownOsAndPowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ShutdownOsAndPowerOff.setStatus("mandatory")


class _A1004ShutdownOsAndHardwareReset_Type(Integer32):
    """Custom type a1004ShutdownOsAndHardwareReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotShutdownAndHardwareReset", 0),
          ("vShutdownAndHardwareReset", 1),
          ("vUnsupported", 2))
    )


_A1004ShutdownOsAndHardwareReset_Type.__name__ = "Integer32"
_A1004ShutdownOsAndHardwareReset_Object = MibTableColumn
a1004ShutdownOsAndHardwareReset = _A1004ShutdownOsAndHardwareReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 19),
    _A1004ShutdownOsAndHardwareReset_Type()
)
a1004ShutdownOsAndHardwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004ShutdownOsAndHardwareReset.setStatus("mandatory")


class _A1004IssueAHardwareNmi_Type(Integer32):
    """Custom type a1004IssueAHardwareNmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDoNotIssueAnNmi", 0),
          ("vIssueAnNmi", 1),
          ("vUnsupported", 2))
    )


_A1004IssueAHardwareNmi_Type.__name__ = "Integer32"
_A1004IssueAHardwareNmi_Object = MibTableColumn
a1004IssueAHardwareNmi = _A1004IssueAHardwareNmi_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1004, 1, 20),
    _A1004IssueAHardwareNmi_Type()
)
a1004IssueAHardwareNmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1004IssueAHardwareNmi.setStatus("mandatory")
_TCoolingSensors_Object = MibTable
tCoolingSensors = _TCoolingSensors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005)
)
if mibBuilder.loadTexts:
    tCoolingSensors.setStatus("mandatory")
_ECoolingSensors_Object = MibTableRow
eCoolingSensors = _ECoolingSensors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1)
)
eCoolingSensors.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a1005Selfid"),
)
if mibBuilder.loadTexts:
    eCoolingSensors.setStatus("mandatory")
_A1005Selfid_Type = DmiInteger
_A1005Selfid_Object = MibTableColumn
a1005Selfid = _A1005Selfid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 1),
    _A1005Selfid_Type()
)
a1005Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005Selfid.setStatus("mandatory")
_A1005FruGroupIndex_Type = DmiInteger
_A1005FruGroupIndex_Object = MibTableColumn
a1005FruGroupIndex = _A1005FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 2),
    _A1005FruGroupIndex_Type()
)
a1005FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005FruGroupIndex.setStatus("mandatory")
_A1005OperationalGroupIndex_Type = DmiInteger
_A1005OperationalGroupIndex_Object = MibTableColumn
a1005OperationalGroupIndex = _A1005OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 3),
    _A1005OperationalGroupIndex_Type()
)
a1005OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005OperationalGroupIndex.setStatus("mandatory")


class _A1005CoolingDeviceType_Type(Integer32):
    """Custom type a1005CoolingDeviceType based on Integer32"""
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("vActiveCooling", 32),
          ("vCabinetFan", 6),
          ("vCentrifugalBlower", 4),
          ("vChipFan", 5),
          ("vFan", 3),
          ("vHeatPipe", 8),
          ("vIntegratedRefrigeration", 9),
          ("vOther", 1),
          ("vPassiveCooling", 33),
          ("vPowerSupplyFan", 7),
          ("vUnknown", 2))
    )


_A1005CoolingDeviceType_Type.__name__ = "Integer32"
_A1005CoolingDeviceType_Object = MibTableColumn
a1005CoolingDeviceType = _A1005CoolingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 6),
    _A1005CoolingDeviceType_Type()
)
a1005CoolingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005CoolingDeviceType.setStatus("mandatory")
_A1005CfmRating_Type = DmiInteger
_A1005CfmRating_Object = MibTableColumn
a1005CfmRating = _A1005CfmRating_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 7),
    _A1005CfmRating_Type()
)
a1005CfmRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005CfmRating.setStatus("mandatory")


class _A1005FanUnits_Type(Integer32):
    """Custom type a1005FanUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vCfm", 1),
          ("vOkfatal", 2),
          ("vRpm", 0))
    )


_A1005FanUnits_Type.__name__ = "Integer32"
_A1005FanUnits_Object = MibTableColumn
a1005FanUnits = _A1005FanUnits_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 8),
    _A1005FanUnits_Type()
)
a1005FanUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005FanUnits.setStatus("mandatory")
_A1005MaximumReading_Type = DmiInteger
_A1005MaximumReading_Object = MibTableColumn
a1005MaximumReading = _A1005MaximumReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 9),
    _A1005MaximumReading_Type()
)
a1005MaximumReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005MaximumReading.setStatus("mandatory")
_A1005MinimumReading_Type = DmiInteger
_A1005MinimumReading_Object = MibTableColumn
a1005MinimumReading = _A1005MinimumReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 10),
    _A1005MinimumReading_Type()
)
a1005MinimumReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005MinimumReading.setStatus("mandatory")
_A1005CurrentReading_Type = DmiInteger
_A1005CurrentReading_Object = MibTableColumn
a1005CurrentReading = _A1005CurrentReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 11),
    _A1005CurrentReading_Type()
)
a1005CurrentReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005CurrentReading.setStatus("mandatory")
_A1005SensorAccuracy_Type = DmiInteger
_A1005SensorAccuracy_Object = MibTableColumn
a1005SensorAccuracy = _A1005SensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 13),
    _A1005SensorAccuracy_Type()
)
a1005SensorAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1005SensorAccuracy.setStatus("mandatory")
_A1005SensorTolerancePlus_Type = DmiInteger
_A1005SensorTolerancePlus_Object = MibTableColumn
a1005SensorTolerancePlus = _A1005SensorTolerancePlus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 14),
    _A1005SensorTolerancePlus_Type()
)
a1005SensorTolerancePlus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1005SensorTolerancePlus.setStatus("mandatory")
_A1005SensorToleranceMinus_Type = DmiInteger
_A1005SensorToleranceMinus_Object = MibTableColumn
a1005SensorToleranceMinus = _A1005SensorToleranceMinus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 15),
    _A1005SensorToleranceMinus_Type()
)
a1005SensorToleranceMinus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1005SensorToleranceMinus.setStatus("mandatory")
_A1005Non_criticalThreshold_Type = DmiInteger
_A1005Non_criticalThreshold_Object = MibScalar
a1005Non_criticalThreshold = _A1005Non_criticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 16),
    _A1005Non_criticalThreshold_Type()
)
a1005Non_criticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1005Non_criticalThreshold.setStatus("mandatory")
_A1005CriticalThreshold_Type = DmiInteger
_A1005CriticalThreshold_Object = MibTableColumn
a1005CriticalThreshold = _A1005CriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 17),
    _A1005CriticalThreshold_Type()
)
a1005CriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1005CriticalThreshold.setStatus("mandatory")
_A1005Non_recoverableThreshold_Type = DmiInteger
_A1005Non_recoverableThreshold_Object = MibScalar
a1005Non_recoverableThreshold = _A1005Non_recoverableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 18),
    _A1005Non_recoverableThreshold_Type()
)
a1005Non_recoverableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1005Non_recoverableThreshold.setStatus("mandatory")
_A1005CoolingSensorDescription_Type = DmiDisplaystring
_A1005CoolingSensorDescription_Object = MibTableColumn
a1005CoolingSensorDescription = _A1005CoolingSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 19),
    _A1005CoolingSensorDescription_Type()
)
a1005CoolingSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005CoolingSensorDescription.setStatus("mandatory")
_A1005NominalReading_Type = DmiInteger
_A1005NominalReading_Object = MibTableColumn
a1005NominalReading = _A1005NominalReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 21),
    _A1005NominalReading_Type()
)
a1005NominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005NominalReading.setStatus("mandatory")
_A1005LowestNormalReading_Type = DmiInteger
_A1005LowestNormalReading_Object = MibTableColumn
a1005LowestNormalReading = _A1005LowestNormalReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 22),
    _A1005LowestNormalReading_Type()
)
a1005LowestNormalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005LowestNormalReading.setStatus("mandatory")
_A1005HighestNormalReading_Type = DmiInteger
_A1005HighestNormalReading_Object = MibTableColumn
a1005HighestNormalReading = _A1005HighestNormalReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1005, 1, 23),
    _A1005HighestNormalReading_Type()
)
a1005HighestNormalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1005HighestNormalReading.setStatus("mandatory")
_TSystemEventLog_Object = MibTable
tSystemEventLog = _TSystemEventLog_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1006)
)
if mibBuilder.loadTexts:
    tSystemEventLog.setStatus("mandatory")
_ESystemEventLog_Object = MibTableRow
eSystemEventLog = _ESystemEventLog_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1006, 1)
)
eSystemEventLog.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARD2-MIB", "a1006Selfid"),
)
if mibBuilder.loadTexts:
    eSystemEventLog.setStatus("mandatory")
_A1006Selfid_Type = DmiInteger
_A1006Selfid_Object = MibTableColumn
a1006Selfid = _A1006Selfid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1006, 1, 1),
    _A1006Selfid_Type()
)
a1006Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006Selfid.setStatus("mandatory")
_A1006Timestamp_Type = DmiDateX
_A1006Timestamp_Object = MibTableColumn
a1006Timestamp = _A1006Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1006, 1, 2),
    _A1006Timestamp_Type()
)
a1006Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006Timestamp.setStatus("mandatory")
_A1006RecordType_Type = DmiInteger
_A1006RecordType_Object = MibTableColumn
a1006RecordType = _A1006RecordType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1006, 1, 3),
    _A1006RecordType_Type()
)
a1006RecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006RecordType.setStatus("mandatory")
_A1006RecordLength_Type = DmiInteger
_A1006RecordLength_Object = MibTableColumn
a1006RecordLength = _A1006RecordLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1006, 1, 4),
    _A1006RecordLength_Type()
)
a1006RecordLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006RecordLength.setStatus("mandatory")
_A1006RecordData_Type = DmiOctetstring
_A1006RecordData_Object = MibTableColumn
a1006RecordData = _A1006RecordData_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 1006, 1, 5),
    _A1006RecordData_Type()
)
a1006RecordData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1006RecordData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trap1ForProcessor = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 0, 256)
)
trap1ForProcessor.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a100EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventMessage"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a6ProcessorIndex"))
)
if mibBuilder.loadTexts:
    trap1ForProcessor.setStatus(
        ""
    )

trap2ForProcessor = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 0, 257)
)
trap2ForProcessor.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a100EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventMessage"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a6ProcessorIndex"))
)
if mibBuilder.loadTexts:
    trap2ForProcessor.setStatus(
        ""
    )

trap3ForProcessor = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 100, 1, 0, 258)
)
trap3ForProcessor.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a100EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a100EventMessage"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a6ProcessorIndex"))
)
if mibBuilder.loadTexts:
    trap3ForProcessor.setStatus(
        ""
    )

trap1ForPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 0, 256)
)
trap1ForPowerSupply.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a104EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a17PowerSupplyIndex"))
)
if mibBuilder.loadTexts:
    trap1ForPowerSupply.setStatus(
        ""
    )

trap2ForPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 0, 257)
)
trap2ForPowerSupply.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a104EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a17PowerSupplyIndex"))
)
if mibBuilder.loadTexts:
    trap2ForPowerSupply.setStatus(
        ""
    )

trap3ForPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 104, 1, 0, 258)
)
trap3ForPowerSupply.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a104EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a104IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a17PowerSupplyIndex"))
)
if mibBuilder.loadTexts:
    trap3ForPowerSupply.setStatus(
        ""
    )

trap1ForPhysicalMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 0, 256)
)
trap1ForPhysicalMemory.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a108EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a34MemoryArrayTableIndex"))
)
if mibBuilder.loadTexts:
    trap1ForPhysicalMemory.setStatus(
        ""
    )

trap2ForPhysicalMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 108, 1, 0, 257)
)
trap2ForPhysicalMemory.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a108EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a108IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a34MemoryArrayTableIndex"))
)
if mibBuilder.loadTexts:
    trap2ForPhysicalMemory.setStatus(
        ""
    )

trap1ForVoltageProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 0, 256)
)
trap1ForVoltageProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a113EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"))
)
if mibBuilder.loadTexts:
    trap1ForVoltageProbe.setStatus(
        ""
    )

trap2ForVoltageProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 0, 257)
)
trap2ForVoltageProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a113EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"))
)
if mibBuilder.loadTexts:
    trap2ForVoltageProbe.setStatus(
        ""
    )

trap3ForVoltageProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 0, 258)
)
trap3ForVoltageProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a113EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"))
)
if mibBuilder.loadTexts:
    trap3ForVoltageProbe.setStatus(
        ""
    )

trap4ForVoltageProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 0, 259)
)
trap4ForVoltageProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a113EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"))
)
if mibBuilder.loadTexts:
    trap4ForVoltageProbe.setStatus(
        ""
    )

trap5ForVoltageProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 0, 260)
)
trap5ForVoltageProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a113EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"))
)
if mibBuilder.loadTexts:
    trap5ForVoltageProbe.setStatus(
        ""
    )

trap6ForVoltageProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 0, 261)
)
trap6ForVoltageProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a113EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"))
)
if mibBuilder.loadTexts:
    trap6ForVoltageProbe.setStatus(
        ""
    )

trap7ForVoltageProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 113, 1, 0, 262)
)
trap7ForVoltageProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a113EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a113IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a54VoltageProbeIndex"))
)
if mibBuilder.loadTexts:
    trap7ForVoltageProbe.setStatus(
        ""
    )

trap1ForTemperatureProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 0, 256)
)
trap1ForTemperatureProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a114EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"))
)
if mibBuilder.loadTexts:
    trap1ForTemperatureProbe.setStatus(
        ""
    )

trap2ForTemperatureProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 0, 257)
)
trap2ForTemperatureProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a114EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"))
)
if mibBuilder.loadTexts:
    trap2ForTemperatureProbe.setStatus(
        ""
    )

trap3ForTemperatureProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 0, 258)
)
trap3ForTemperatureProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a114EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"))
)
if mibBuilder.loadTexts:
    trap3ForTemperatureProbe.setStatus(
        ""
    )

trap4ForTemperatureProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 0, 259)
)
trap4ForTemperatureProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a114EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"))
)
if mibBuilder.loadTexts:
    trap4ForTemperatureProbe.setStatus(
        ""
    )

trap5ForTemperatureProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 0, 260)
)
trap5ForTemperatureProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a114EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"))
)
if mibBuilder.loadTexts:
    trap5ForTemperatureProbe.setStatus(
        ""
    )

trap6ForTemperatureProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 0, 261)
)
trap6ForTemperatureProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a114EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"))
)
if mibBuilder.loadTexts:
    trap6ForTemperatureProbe.setStatus(
        ""
    )

trap7ForTemperatureProbe = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 114, 1, 0, 262)
)
trap7ForTemperatureProbe.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a114EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a114IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a55TemperatureProbeTableIndex"))
)
if mibBuilder.loadTexts:
    trap7ForTemperatureProbe.setStatus(
        ""
    )

trap1ForPhysicalContainer = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 0, 6)
)
trap1ForPhysicalContainer.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a116EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a64ContainerIndex"))
)
if mibBuilder.loadTexts:
    trap1ForPhysicalContainer.setStatus(
        ""
    )

trap2ForPhysicalContainer = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 116, 1, 0, 256)
)
trap2ForPhysicalContainer.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a116EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a116IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a64ContainerIndex"))
)
if mibBuilder.loadTexts:
    trap2ForPhysicalContainer.setStatus(
        ""
    )

trap1ForPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 0, 1)
)
trap1ForPowerUnit.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a201EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a67PowerUnitIndex"))
)
if mibBuilder.loadTexts:
    trap1ForPowerUnit.setStatus(
        ""
    )

trap2ForPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 0, 2)
)
trap2ForPowerUnit.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a201EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a67PowerUnitIndex"))
)
if mibBuilder.loadTexts:
    trap2ForPowerUnit.setStatus(
        ""
    )

trap3ForPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 0, 3)
)
trap3ForPowerUnit.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a201EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a67PowerUnitIndex"))
)
if mibBuilder.loadTexts:
    trap3ForPowerUnit.setStatus(
        ""
    )

trap4ForPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 0, 4)
)
trap4ForPowerUnit.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a201EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a67PowerUnitIndex"))
)
if mibBuilder.loadTexts:
    trap4ForPowerUnit.setStatus(
        ""
    )

trap5ForPowerUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 201, 1, 0, 5)
)
trap5ForPowerUnit.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a201EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a201IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a67PowerUnitIndex"))
)
if mibBuilder.loadTexts:
    trap5ForPowerUnit.setStatus(
        ""
    )

trap1ForCoolingSensors = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 0, 256)
)
trap1ForCoolingSensors.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a202EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a1005Selfid"))
)
if mibBuilder.loadTexts:
    trap1ForCoolingSensors.setStatus(
        ""
    )

trap2ForCoolingSensors = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 2, 1, 202, 1, 0, 257)
)
trap2ForCoolingSensors.setObjects(
      *(("INTELCORPORATIONBASEBOARD2-MIB", "a202EventType"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventSeverity"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202IsEventState_based"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventStateKey"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202AssociatedGroup"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventSystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202EventSubsystem"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a202IsInstanceDataPresent"),
        ("INTELCORPORATIONBASEBOARD2-MIB", "a1005Selfid"))
)
if mibBuilder.loadTexts:
    trap2ForCoolingSensors.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATIONBASEBOARD2-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiInteger64X": DmiInteger64X,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "intel": intel,
       "products": products,
       "server-products": server_products,
       "platforms": platforms,
       "basebrd2": basebrd2,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tGeneralInformation": tGeneralInformation,
       "eGeneralInformation": eGeneralInformation,
       "a2SystemName": a2SystemName,
       "a2SystemLocation": a2SystemLocation,
       "a2SystemPrimaryUserName": a2SystemPrimaryUserName,
       "a2SystemPrimaryUserPhone": a2SystemPrimaryUserPhone,
       "a2SystemBootupTime": a2SystemBootupTime,
       "a2SystemDateTime": a2SystemDateTime,
       "tSystemBios": tSystemBios,
       "eSystemBios": eSystemBios,
       "a4BiosIndex": a4BiosIndex,
       "a4BiosManufacturer": a4BiosManufacturer,
       "a4BiosVersion": a4BiosVersion,
       "a4BiosRomSize": a4BiosRomSize,
       "a4BiosStartingAddress": a4BiosStartingAddress,
       "a4BiosEndingAddress": a4BiosEndingAddress,
       "a4BiosLoaderVersion": a4BiosLoaderVersion,
       "a4BiosReleaseDate": a4BiosReleaseDate,
       "a4PrimaryBios": a4PrimaryBios,
       "tSystemBiosCharacteristics": tSystemBiosCharacteristics,
       "eSystemBiosCharacteristics": eSystemBiosCharacteristics,
       "a5BiosCharacteristicIndex": a5BiosCharacteristicIndex,
       "a5BiosNumber": a5BiosNumber,
       "a5BiosCharacteristic": a5BiosCharacteristic,
       "a5BiosCharacteristicDescription": a5BiosCharacteristicDescription,
       "tProcessor": tProcessor,
       "eProcessor": eProcessor,
       "a6ProcessorIndex": a6ProcessorIndex,
       "a6ProcessorType": a6ProcessorType,
       "a6ProcessorFamily": a6ProcessorFamily,
       "a6ProcessorVersionInformation": a6ProcessorVersionInformation,
       "a6MaximumSpeed": a6MaximumSpeed,
       "a6CurrentSpeed": a6CurrentSpeed,
       "a6ProcessorUpgrade": a6ProcessorUpgrade,
       "a6FruGroupIndex": a6FruGroupIndex,
       "a6OperationalGroupIndex": a6OperationalGroupIndex,
       "a6Level1CacheIndex": a6Level1CacheIndex,
       "a6Level2CacheIndex": a6Level2CacheIndex,
       "a6Level3CacheIndex": a6Level3CacheIndex,
       "tMotherboard": tMotherboard,
       "eMotherboard": eMotherboard,
       "a7NumberOfExpansionSlots": a7NumberOfExpansionSlots,
       "a7FruGroupIndex": a7FruGroupIndex,
       "a7OperationalGroupIndex": a7OperationalGroupIndex,
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
       "a10SystemCacheType": a10SystemCacheType,
       "tPowerSupply": tPowerSupply,
       "ePowerSupply": ePowerSupply,
       "a17PowerSupplyIndex": a17PowerSupplyIndex,
       "a17FruGroupIndex": a17FruGroupIndex,
       "a17OperationalGroupIndex": a17OperationalGroupIndex,
       "a17PowerUnitIndex": a17PowerUnitIndex,
       "a17PowerSupplyType": a17PowerSupplyType,
       "a17InputVoltageCapabilityDescription": a17InputVoltageCapabilityDescription,
       "a17Range1InputVoltageLow": a17Range1InputVoltageLow,
       "a17Range1InputVoltageHigh": a17Range1InputVoltageHigh,
       "a17Range1VoltageProbeIndex": a17Range1VoltageProbeIndex,
       "a17Range1ElectricalCurrentProbeIndex": a17Range1ElectricalCurrentProbeIndex,
       "a17Range2InputVoltageLow": a17Range2InputVoltageLow,
       "a17Range2InputVoltageHigh": a17Range2InputVoltageHigh,
       "a17Range2VoltageProbeIndex": a17Range2VoltageProbeIndex,
       "a17Range2CurrentProbeIndex": a17Range2CurrentProbeIndex,
       "a17ActiveInputVoltageRange": a17ActiveInputVoltageRange,
       "a17InputVoltageRangeSwitching": a17InputVoltageRangeSwitching,
       "a17Range1InputFrequencyLow": a17Range1InputFrequencyLow,
       "a17Range1InputFrequencyHigh": a17Range1InputFrequencyHigh,
       "a17Range2InputFrequencyLow": a17Range2InputFrequencyLow,
       "a17Range2InputFrequencyHigh": a17Range2InputFrequencyHigh,
       "a17TotalOutputPower": a17TotalOutputPower,
       "tSystemSlots": tSystemSlots,
       "eSystemSlots": eSystemSlots,
       "a19SlotIndex": a19SlotIndex,
       "a19SlotType": a19SlotType,
       "a19SlotWidth": a19SlotWidth,
       "a19CurrentUsage": a19CurrentUsage,
       "a19SlotDescription": a19SlotDescription,
       "a19SlotCategory": a19SlotCategory,
       "a19VirtualSlot": a19VirtualSlot,
       "a19ResourceUserId": a19ResourceUserId,
       "tFieldReplaceableUnit": tFieldReplaceableUnit,
       "eFieldReplaceableUnit": eFieldReplaceableUnit,
       "a30FruIndex": a30FruIndex,
       "a30DeviceGroupIndex": a30DeviceGroupIndex,
       "a30Description": a30Description,
       "a30Manufacturer": a30Manufacturer,
       "a30Model": a30Model,
       "a30PartNumber": a30PartNumber,
       "a30FruSerialNumber": a30FruSerialNumber,
       "a30RevisionLevel": a30RevisionLevel,
       "a30WarrantyStartDate": a30WarrantyStartDate,
       "a30WarrantyDuration": a30WarrantyDuration,
       "a30SupportPhoneNumber": a30SupportPhoneNumber,
       "a30FruInternetUniformResourceLocator": a30FruInternetUniformResourceLocator,
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
       "a31CurrentErrorStatus": a31CurrentErrorStatus,
       "tPhysicalMemoryArray": tPhysicalMemoryArray,
       "ePhysicalMemoryArray": ePhysicalMemoryArray,
       "a34MemoryArrayTableIndex": a34MemoryArrayTableIndex,
       "a34MemoryArrayLocation": a34MemoryArrayLocation,
       "a34MemoryArrayUse": a34MemoryArrayUse,
       "a34MaximumMemoryCapacity": a34MaximumMemoryCapacity,
       "a34NumberOfMemoryDeviceSockets": a34NumberOfMemoryDeviceSockets,
       "a34NumberOfMemoryDeviceSocketsUsed": a34NumberOfMemoryDeviceSocketsUsed,
       "a34MemoryErrorCorrection": a34MemoryErrorCorrection,
       "a34ArrayErrorType": a34ArrayErrorType,
       "a34LastErrorUpdate": a34LastErrorUpdate,
       "a34ErrorOperation": a34ErrorOperation,
       "a34ErrorDataSize": a34ErrorDataSize,
       "a34ErrorData": a34ErrorData,
       "a34VendorSyndrome": a34VendorSyndrome,
       "a34ErrorAddress": a34ErrorAddress,
       "a34ErrorResolution": a34ErrorResolution,
       "a34FruGroupIndex": a34FruGroupIndex,
       "a34OperationalGroupIndex": a34OperationalGroupIndex,
       "tMemoryArrayMappedAddresses": tMemoryArrayMappedAddresses,
       "eMemoryArrayMappedAddresses": eMemoryArrayMappedAddresses,
       "a35MemoryArrayMappedAddressesTableIndex": a35MemoryArrayMappedAddressesTableIndex,
       "a35MemoryArrayIndex": a35MemoryArrayIndex,
       "a35MappedRangeStartingAddress": a35MappedRangeStartingAddress,
       "a35MappedRangeEndingAddress": a35MappedRangeEndingAddress,
       "a35PartitionId": a35PartitionId,
       "a35PartitionWidth": a35PartitionWidth,
       "a35OperationalGroupIndex": a35OperationalGroupIndex,
       "tMemoryDevice": tMemoryDevice,
       "eMemoryDevice": eMemoryDevice,
       "a36MemoryDeviceTableIndex": a36MemoryDeviceTableIndex,
       "a36MemoryArrayIndex": a36MemoryArrayIndex,
       "a36DeviceLocator": a36DeviceLocator,
       "a36BankLocator": a36BankLocator,
       "a36Size": a36Size,
       "a36FormFactor": a36FormFactor,
       "a36TotalWidth": a36TotalWidth,
       "a36DataWidth": a36DataWidth,
       "a36MemoryType": a36MemoryType,
       "a36TypeDetail": a36TypeDetail,
       "a36DeviceSet": a36DeviceSet,
       "a36DeviceErrorType": a36DeviceErrorType,
       "a36ErrorGranularity": a36ErrorGranularity,
       "a36LastErrorUpdate": a36LastErrorUpdate,
       "a36ErrorOperation": a36ErrorOperation,
       "a36ErrorDataSize": a36ErrorDataSize,
       "a36ErrorData": a36ErrorData,
       "a36VendorSyndrome": a36VendorSyndrome,
       "a36DeviceErrorAddress": a36DeviceErrorAddress,
       "a36ArrayErrorAddress": a36ArrayErrorAddress,
       "a36ErrorResolution": a36ErrorResolution,
       "a36FruGroupIndex": a36FruGroupIndex,
       "a36OperationalGroupIndex": a36OperationalGroupIndex,
       "tMemoryDeviceMappedAddresses": tMemoryDeviceMappedAddresses,
       "eMemoryDeviceMappedAddresses": eMemoryDeviceMappedAddresses,
       "a37MemoryDeviceMappedAddressesTableIndex": a37MemoryDeviceMappedAddressesTableIndex,
       "a37MemoryDeviceSetId": a37MemoryDeviceSetId,
       "a37Partition": a37Partition,
       "a37MappedRangeStartingAddress": a37MappedRangeStartingAddress,
       "a37MappedRangeEndingAddress": a37MappedRangeEndingAddress,
       "a37PartitionRowPosition": a37PartitionRowPosition,
       "a37InterleavePosition": a37InterleavePosition,
       "a37DataDepth": a37DataDepth,
       "tSystemHardwareSecurity": tSystemHardwareSecurity,
       "eSystemHardwareSecurity": eSystemHardwareSecurity,
       "a50Power-onPasswordStatus": a50Power_onPasswordStatus,
       "a50KeyboardPasswordStatus": a50KeyboardPasswordStatus,
       "a50AdministratorPasswordStatus": a50AdministratorPasswordStatus,
       "a50FrontPanelResetStatus": a50FrontPanelResetStatus,
       "tSystemPowerControls": tSystemPowerControls,
       "eSystemPowerControls": eSystemPowerControls,
       "a52PowerControlRequest": a52PowerControlRequest,
       "a52TimedPower-onAvailable": a52TimedPower_onAvailable,
       "a52TimeToNextScheduledPower-on": a52TimeToNextScheduledPower_on,
       "tVoltageProbe": tVoltageProbe,
       "eVoltageProbe": eVoltageProbe,
       "a54VoltageProbeIndex": a54VoltageProbeIndex,
       "a54VoltageProbeLocation": a54VoltageProbeLocation,
       "a54VoltageProbeDescription": a54VoltageProbeDescription,
       "a54VoltageStatus": a54VoltageStatus,
       "a54VoltageProbeVoltageLevel": a54VoltageProbeVoltageLevel,
       "a54MonitoredVoltageNominalLevel": a54MonitoredVoltageNominalLevel,
       "a54MonitoredVoltageNormalMaximum": a54MonitoredVoltageNormalMaximum,
       "a54MonitoredVoltageNormalMinimum": a54MonitoredVoltageNormalMinimum,
       "a54VoltageProbeMaximum": a54VoltageProbeMaximum,
       "a54VoltageProbeMinimum": a54VoltageProbeMinimum,
       "a54VoltageLevelLowerThreshold-Non-critic": a54VoltageLevelLowerThreshold_Non_critic,
       "a54VoltageLevelUpperThreshold-Non-critic": a54VoltageLevelUpperThreshold_Non_critic,
       "a54VoltageLevelLowerThreshold-Critical": a54VoltageLevelLowerThreshold_Critical,
       "a54VoltageLevelUpperThreshold-Critical": a54VoltageLevelUpperThreshold_Critical,
       "a54VoltageLevelLowerThreshold-Non-recove": a54VoltageLevelLowerThreshold_Non_recove,
       "a54VoltageLevelUpperThreshold-Non-recove": a54VoltageLevelUpperThreshold_Non_recove,
       "a54VoltageProbeResolution": a54VoltageProbeResolution,
       "a54VoltageProbeTolerance": a54VoltageProbeTolerance,
       "a54VoltageProbeAccuracy": a54VoltageProbeAccuracy,
       "a54FruGroupIndex": a54FruGroupIndex,
       "a54OperationalGroupIndex": a54OperationalGroupIndex,
       "tTemperatureProbe": tTemperatureProbe,
       "eTemperatureProbe": eTemperatureProbe,
       "a55TemperatureProbeTableIndex": a55TemperatureProbeTableIndex,
       "a55TemperatureProbeLocation": a55TemperatureProbeLocation,
       "a55TemperatureProbeDescription": a55TemperatureProbeDescription,
       "a55TemperatureStatus": a55TemperatureStatus,
       "a55TemperatureProbeTemperatureReading": a55TemperatureProbeTemperatureReading,
       "a55MonitoredTemperatureNominalReading": a55MonitoredTemperatureNominalReading,
       "a55MonitoredTemperatureNormalMaximum": a55MonitoredTemperatureNormalMaximum,
       "a55MonitoredTemperatureNormalMinimum": a55MonitoredTemperatureNormalMinimum,
       "a55TemperatureProbeMaximum": a55TemperatureProbeMaximum,
       "a55TemperatureProbeMinimum": a55TemperatureProbeMinimum,
       "a55TemperatureLowerThreshold-Non-critica": a55TemperatureLowerThreshold_Non_critica,
       "a55TemperatureUpperThreshold-Non-critica": a55TemperatureUpperThreshold_Non_critica,
       "a55TemperatureLowerThreshold-Critical": a55TemperatureLowerThreshold_Critical,
       "a55TemperatureUpperThreshold-Critical": a55TemperatureUpperThreshold_Critical,
       "a55TemperatureLowerThreshold-Non-recover": a55TemperatureLowerThreshold_Non_recover,
       "a55TemperatureUpperThreshold-Non-recover": a55TemperatureUpperThreshold_Non_recover,
       "a55TemperatureProbeResolution": a55TemperatureProbeResolution,
       "a55TemperatureProbeTolerance": a55TemperatureProbeTolerance,
       "a55TemperatureProbeAccuracy": a55TemperatureProbeAccuracy,
       "a55FruGroupIndex": a55FruGroupIndex,
       "a55OperationalGroupIndex": a55OperationalGroupIndex,
       "tPhysicalContainerGlobalTable": tPhysicalContainerGlobalTable,
       "ePhysicalContainerGlobalTable": ePhysicalContainerGlobalTable,
       "a64ContainerOrChassisType": a64ContainerOrChassisType,
       "a64AssetTag": a64AssetTag,
       "a64ChassisLockPresent": a64ChassisLockPresent,
       "a64BootupState": a64BootupState,
       "a64PowerState": a64PowerState,
       "a64ThermalState": a64ThermalState,
       "a64FruGroupIndex": a64FruGroupIndex,
       "a64OperationalGroupIndex": a64OperationalGroupIndex,
       "a64ContainerIndex": a64ContainerIndex,
       "a64ContainerName": a64ContainerName,
       "a64ContainerLocation": a64ContainerLocation,
       "a64ContainerSecurityStatus": a64ContainerSecurityStatus,
       "tOperatingSystem": tOperatingSystem,
       "eOperatingSystem": eOperatingSystem,
       "a66OperatingSystemIndex": a66OperatingSystemIndex,
       "a66OperatingSystemName": a66OperatingSystemName,
       "a66OperatingSystemVersion": a66OperatingSystemVersion,
       "a66PrimaryOperatingSystem": a66PrimaryOperatingSystem,
       "a66OperatingSystemBootDeviceStorageType": a66OperatingSystemBootDeviceStorageType,
       "a66OperatingSystemBootDeviceIndex": a66OperatingSystemBootDeviceIndex,
       "a66OperatingSystemBootPartitionIndex": a66OperatingSystemBootPartitionIndex,
       "a66OperatingSystemDescription": a66OperatingSystemDescription,
       "tPowerUnitGlobalTable": tPowerUnitGlobalTable,
       "ePowerUnitGlobalTable": ePowerUnitGlobalTable,
       "a67PowerUnitIndex": a67PowerUnitIndex,
       "a67PowerUnitRedundancyStatus": a67PowerUnitRedundancyStatus,
       "tParallelPorts": tParallelPorts,
       "eParallelPorts": eParallelPorts,
       "a74ParallelPortIndex": a74ParallelPortIndex,
       "a74ParallelBaseIoAddress": a74ParallelBaseIoAddress,
       "a74IrqUsed": a74IrqUsed,
       "a74LogicalName": a74LogicalName,
       "a74ConnectorType": a74ConnectorType,
       "a74ConnectorPinout": a74ConnectorPinout,
       "a74DmaSupport": a74DmaSupport,
       "a74ParallelPortCapabilities": a74ParallelPortCapabilities,
       "a74OperationalGroupIndex": a74OperationalGroupIndex,
       "a74ParallelPortSecuritySettings": a74ParallelPortSecuritySettings,
       "tSerialPorts": tSerialPorts,
       "eSerialPorts": eSerialPorts,
       "a75SerialPortIndex": a75SerialPortIndex,
       "a75SerialBaseIoAddress": a75SerialBaseIoAddress,
       "a75IrqUsed": a75IrqUsed,
       "a75LogicalName": a75LogicalName,
       "a75ConnectorType": a75ConnectorType,
       "a75MaximumSpeed": a75MaximumSpeed,
       "a75SerialPortCapabilities": a75SerialPortCapabilities,
       "a75OperationalGroupIndex": a75OperationalGroupIndex,
       "a75SerialPortSecuritySettings": a75SerialPortSecuritySettings,
       "tCoolingDevice": tCoolingDevice,
       "eCoolingDevice": eCoolingDevice,
       "a81CoolingDeviceTableIndex": a81CoolingDeviceTableIndex,
       "a81FruGroupIndex": a81FruGroupIndex,
       "a81OperationalGroupIndex": a81OperationalGroupIndex,
       "a81CoolingUnitIndex": a81CoolingUnitIndex,
       "a81CoolingDeviceType": a81CoolingDeviceType,
       "a81TemperatureProbeIndex": a81TemperatureProbeIndex,
       "tVideo": tVideo,
       "eVideo": eVideo,
       "a83VideoIndex": a83VideoIndex,
       "a83VideoType": a83VideoType,
       "a83CurrentVideoMode": a83CurrentVideoMode,
       "a83MinimumRefreshRate": a83MinimumRefreshRate,
       "a83MaximumRefreshRate": a83MaximumRefreshRate,
       "a83VideoMemoryType": a83VideoMemoryType,
       "a83VideoRamMemorySize": a83VideoRamMemorySize,
       "a83ScanMode": a83ScanMode,
       "a83VideoPhysicalLocation": a83VideoPhysicalLocation,
       "a83CurrentVerticalResolution": a83CurrentVerticalResolution,
       "a83CurrentHorizontalResolution": a83CurrentHorizontalResolution,
       "a83CurrentNumberOfBitsPerPixel": a83CurrentNumberOfBitsPerPixel,
       "a83CurrentNumberOfRows": a83CurrentNumberOfRows,
       "a83CurrentNumberOfColumns": a83CurrentNumberOfColumns,
       "a83CurrentRefreshRate": a83CurrentRefreshRate,
       "a83FruGroupIndex": a83FruGroupIndex,
       "a83OperationalGroupIndex": a83OperationalGroupIndex,
       "tVideoBios": tVideoBios,
       "eVideoBios": eVideoBios,
       "a84VideoBiosIndex": a84VideoBiosIndex,
       "a84VideoBiosManufacturer": a84VideoBiosManufacturer,
       "a84VideoBiosVersion": a84VideoBiosVersion,
       "a84VideoBiosReleaseDate": a84VideoBiosReleaseDate,
       "a84VideoBiosShadowingState": a84VideoBiosShadowingState,
       "tMouse": tMouse,
       "eMouse": eMouse,
       "a91MouseInterface": a91MouseInterface,
       "a91MouseIrq": a91MouseIrq,
       "a91MouseButtons": a91MouseButtons,
       "a91MousePortName": a91MousePortName,
       "a91MouseDriverName": a91MouseDriverName,
       "a91MouseDriverVersion": a91MouseDriverVersion,
       "a91FruGroupIndex": a91FruGroupIndex,
       "a91OperationalGroupIndex": a91OperationalGroupIndex,
       "a91SecuritySettings": a91SecuritySettings,
       "tKeyboard": tKeyboard,
       "eKeyboard": eKeyboard,
       "a92KeyboardLayout": a92KeyboardLayout,
       "a92KeyboardType": a92KeyboardType,
       "a92KeyboardConnectorType": a92KeyboardConnectorType,
       "a92FruGroupIndex": a92FruGroupIndex,
       "a92OperationalGroupIndex": a92OperationalGroupIndex,
       "a92SecuritySettings": a92SecuritySettings,
       "tEventGenerationForProcessor": tEventGenerationForProcessor,
       "eEventGenerationForProcessor": eEventGenerationForProcessor,
       "trap1ForProcessor": trap1ForProcessor,
       "trap2ForProcessor": trap2ForProcessor,
       "trap3ForProcessor": trap3ForProcessor,
       "a100EventType": a100EventType,
       "a100EventSeverity": a100EventSeverity,
       "a100IsEventState-based": a100IsEventState_based,
       "a100EventStateKey": a100EventStateKey,
       "a100AssociatedGroup": a100AssociatedGroup,
       "a100EventSystem": a100EventSystem,
       "a100EventSubsystem": a100EventSubsystem,
       "a100IsInstanceDataPresent": a100IsInstanceDataPresent,
       "a100EventMessage": a100EventMessage,
       "tEventGenerationForPowerSupply": tEventGenerationForPowerSupply,
       "eEventGenerationForPowerSupply": eEventGenerationForPowerSupply,
       "trap1ForPowerSupply": trap1ForPowerSupply,
       "trap2ForPowerSupply": trap2ForPowerSupply,
       "trap3ForPowerSupply": trap3ForPowerSupply,
       "a104EventType": a104EventType,
       "a104EventSeverity": a104EventSeverity,
       "a104IsEventState-based": a104IsEventState_based,
       "a104EventStateKey": a104EventStateKey,
       "a104AssociatedGroup": a104AssociatedGroup,
       "a104EventSystem": a104EventSystem,
       "a104EventSubsystem": a104EventSubsystem,
       "a104IsInstanceDataPresent": a104IsInstanceDataPresent,
       "a104EventMessage": a104EventMessage,
       "tEventGenerationForPhysicalMemory": tEventGenerationForPhysicalMemory,
       "eEventGenerationForPhysicalMemory": eEventGenerationForPhysicalMemory,
       "trap1ForPhysicalMemory": trap1ForPhysicalMemory,
       "trap2ForPhysicalMemory": trap2ForPhysicalMemory,
       "a108EventType": a108EventType,
       "a108EventSeverity": a108EventSeverity,
       "a108IsEventState-based": a108IsEventState_based,
       "a108EventStateKey": a108EventStateKey,
       "a108AssociatedGroup": a108AssociatedGroup,
       "a108EventSystem": a108EventSystem,
       "a108EventSubsystem": a108EventSubsystem,
       "a108IsInstanceDataPresent": a108IsInstanceDataPresent,
       "a108EventMessage": a108EventMessage,
       "tEventGenerationForVoltageProbe": tEventGenerationForVoltageProbe,
       "eEventGenerationForVoltageProbe": eEventGenerationForVoltageProbe,
       "trap1ForVoltageProbe": trap1ForVoltageProbe,
       "trap2ForVoltageProbe": trap2ForVoltageProbe,
       "trap3ForVoltageProbe": trap3ForVoltageProbe,
       "trap4ForVoltageProbe": trap4ForVoltageProbe,
       "trap5ForVoltageProbe": trap5ForVoltageProbe,
       "trap6ForVoltageProbe": trap6ForVoltageProbe,
       "trap7ForVoltageProbe": trap7ForVoltageProbe,
       "a113EventType": a113EventType,
       "a113EventSeverity": a113EventSeverity,
       "a113IsEventState-based": a113IsEventState_based,
       "a113EventStateKey": a113EventStateKey,
       "a113AssociatedGroup": a113AssociatedGroup,
       "a113EventSystem": a113EventSystem,
       "a113EventSubsystem": a113EventSubsystem,
       "a113IsInstanceDataPresent": a113IsInstanceDataPresent,
       "a113EventMessage": a113EventMessage,
       "tEventGenerationForTemperatureProbe": tEventGenerationForTemperatureProbe,
       "eEventGenerationForTemperatureProbe": eEventGenerationForTemperatureProbe,
       "trap1ForTemperatureProbe": trap1ForTemperatureProbe,
       "trap2ForTemperatureProbe": trap2ForTemperatureProbe,
       "trap3ForTemperatureProbe": trap3ForTemperatureProbe,
       "trap4ForTemperatureProbe": trap4ForTemperatureProbe,
       "trap5ForTemperatureProbe": trap5ForTemperatureProbe,
       "trap6ForTemperatureProbe": trap6ForTemperatureProbe,
       "trap7ForTemperatureProbe": trap7ForTemperatureProbe,
       "a114EventType": a114EventType,
       "a114EventSeverity": a114EventSeverity,
       "a114IsEventState-based": a114IsEventState_based,
       "a114EventStateKey": a114EventStateKey,
       "a114AssociatedGroup": a114AssociatedGroup,
       "a114EventSystem": a114EventSystem,
       "a114EventSubsystem": a114EventSubsystem,
       "a114IsInstanceDataPresent": a114IsInstanceDataPresent,
       "a114EventMessage": a114EventMessage,
       "tEventGenerationForPhysicalContainer": tEventGenerationForPhysicalContainer,
       "eEventGenerationForPhysicalContainer": eEventGenerationForPhysicalContainer,
       "trap1ForPhysicalContainer": trap1ForPhysicalContainer,
       "trap2ForPhysicalContainer": trap2ForPhysicalContainer,
       "a116EventType": a116EventType,
       "a116EventSeverity": a116EventSeverity,
       "a116IsEventState-based": a116IsEventState_based,
       "a116EventStateKey": a116EventStateKey,
       "a116AssociatedGroup": a116AssociatedGroup,
       "a116EventSystem": a116EventSystem,
       "a116EventSubsystem": a116EventSubsystem,
       "a116IsInstanceDataPresent": a116IsInstanceDataPresent,
       "a116EventMessage": a116EventMessage,
       "tBusGlobalTable": tBusGlobalTable,
       "eBusGlobalTable": eBusGlobalTable,
       "a128BusId": a128BusId,
       "a128BusType": a128BusType,
       "tPhysicalExpansionSitesTable": tPhysicalExpansionSitesTable,
       "ePhysicalExpansionSitesTable": ePhysicalExpansionSitesTable,
       "a129ExpansionSiteIndex": a129ExpansionSiteIndex,
       "a129ExpansionSiteType": a129ExpansionSiteType,
       "a129VirtualExpansionSite": a129VirtualExpansionSite,
       "a129ExpansionSiteName": a129ExpansionSiteName,
       "a129ExpansionSiteDescription": a129ExpansionSiteDescription,
       "a129ExpansionSiteCurrentlyOccupied": a129ExpansionSiteCurrentlyOccupied,
       "tEventGenerationForCoolingDevice": tEventGenerationForCoolingDevice,
       "eEventGenerationForCoolingDevice": eEventGenerationForCoolingDevice,
       "a140EventType": a140EventType,
       "a140EventSeverity": a140EventSeverity,
       "a140IsEventState-based": a140IsEventState_based,
       "a140EventStateKey": a140EventStateKey,
       "a140AssociatedGroup": a140AssociatedGroup,
       "a140EventSystem": a140EventSystem,
       "a140EventSubsystem": a140EventSubsystem,
       "tEventGenerationForPowerUnit": tEventGenerationForPowerUnit,
       "eEventGenerationForPowerUnit": eEventGenerationForPowerUnit,
       "trap1ForPowerUnit": trap1ForPowerUnit,
       "trap2ForPowerUnit": trap2ForPowerUnit,
       "trap3ForPowerUnit": trap3ForPowerUnit,
       "trap4ForPowerUnit": trap4ForPowerUnit,
       "trap5ForPowerUnit": trap5ForPowerUnit,
       "a201EventType": a201EventType,
       "a201EventSeverity": a201EventSeverity,
       "a201IsEventState-based": a201IsEventState_based,
       "a201EventStateKey": a201EventStateKey,
       "a201AssociatedGroup": a201AssociatedGroup,
       "a201EventSystem": a201EventSystem,
       "a201EventSubsystem": a201EventSubsystem,
       "a201IsInstanceDataPresent": a201IsInstanceDataPresent,
       "a201EventMessage": a201EventMessage,
       "tEventGenerationForCoolingSensors": tEventGenerationForCoolingSensors,
       "eEventGenerationForCoolingSensors": eEventGenerationForCoolingSensors,
       "trap1ForCoolingSensors": trap1ForCoolingSensors,
       "trap2ForCoolingSensors": trap2ForCoolingSensors,
       "a202EventType": a202EventType,
       "a202EventSeverity": a202EventSeverity,
       "a202IsEventState-based": a202IsEventState_based,
       "a202EventStateKey": a202EventStateKey,
       "a202AssociatedGroup": a202AssociatedGroup,
       "a202EventSystem": a202EventSystem,
       "a202EventSubsystem": a202EventSubsystem,
       "a202IsInstanceDataPresent": a202IsInstanceDataPresent,
       "a202EventMessage": a202EventMessage,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a1001MibName": a1001MibName,
       "a1001MibOid": a1001MibOid,
       "a1001DisableTrap": a1001DisableTrap,
       "tSystemControl": tSystemControl,
       "eSystemControl": eSystemControl,
       "a1004Selfid": a1004Selfid,
       "a1004ResetSystem": a1004ResetSystem,
       "a1004TimedResetIncrement": a1004TimedResetIncrement,
       "a1004TimedResetResolution": a1004TimedResetResolution,
       "a1004TimeUntilSystemReset": a1004TimeUntilSystemReset,
       "a1004SystemPowerCapabilities": a1004SystemPowerCapabilities,
       "a1004SystemPowerStatus": a1004SystemPowerStatus,
       "a1004EventLoggingCapability": a1004EventLoggingCapability,
       "a1004WatchdogTimerIncrement": a1004WatchdogTimerIncrement,
       "a1004WatchdogTimerResolution": a1004WatchdogTimerResolution,
       "a1004WatchdogUpdateInterval": a1004WatchdogUpdateInterval,
       "a1004UseSystemWatchdogFeature": a1004UseSystemWatchdogFeature,
       "a1004ResetSystemAfterDelay": a1004ResetSystemAfterDelay,
       "a1004SavePersistentData": a1004SavePersistentData,
       "a1004RestoreFactoryDefaults": a1004RestoreFactoryDefaults,
       "a1004ShutdownOs": a1004ShutdownOs,
       "a1004ShutdownOsAndPowerOff": a1004ShutdownOsAndPowerOff,
       "a1004ShutdownOsAndHardwareReset": a1004ShutdownOsAndHardwareReset,
       "a1004IssueAHardwareNmi": a1004IssueAHardwareNmi,
       "tCoolingSensors": tCoolingSensors,
       "eCoolingSensors": eCoolingSensors,
       "a1005Selfid": a1005Selfid,
       "a1005FruGroupIndex": a1005FruGroupIndex,
       "a1005OperationalGroupIndex": a1005OperationalGroupIndex,
       "a1005CoolingDeviceType": a1005CoolingDeviceType,
       "a1005CfmRating": a1005CfmRating,
       "a1005FanUnits": a1005FanUnits,
       "a1005MaximumReading": a1005MaximumReading,
       "a1005MinimumReading": a1005MinimumReading,
       "a1005CurrentReading": a1005CurrentReading,
       "a1005SensorAccuracy": a1005SensorAccuracy,
       "a1005SensorTolerancePlus": a1005SensorTolerancePlus,
       "a1005SensorToleranceMinus": a1005SensorToleranceMinus,
       "a1005Non-criticalThreshold": a1005Non_criticalThreshold,
       "a1005CriticalThreshold": a1005CriticalThreshold,
       "a1005Non-recoverableThreshold": a1005Non_recoverableThreshold,
       "a1005CoolingSensorDescription": a1005CoolingSensorDescription,
       "a1005NominalReading": a1005NominalReading,
       "a1005LowestNormalReading": a1005LowestNormalReading,
       "a1005HighestNormalReading": a1005HighestNormalReading,
       "tSystemEventLog": tSystemEventLog,
       "eSystemEventLog": eSystemEventLog,
       "a1006Selfid": a1006Selfid,
       "a1006Timestamp": a1006Timestamp,
       "a1006RecordType": a1006RecordType,
       "a1006RecordLength": a1006RecordLength,
       "a1006RecordData": a1006RecordData}
)
