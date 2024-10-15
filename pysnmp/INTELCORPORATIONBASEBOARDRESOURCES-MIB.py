# SNMP MIB module (INTELCORPORATIONBASEBOARDRESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATIONBASEBOARDRESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:16 2024
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
_Resources_ObjectIdentity = ObjectIdentity
resources = _Resources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TSystemResources2_Object = MibTable
tSystemResources2 = _TSystemResources2_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41)
)
if mibBuilder.loadTexts:
    tSystemResources2.setStatus("mandatory")
_ESystemResources2_Object = MibTableRow
eSystemResources2 = _ESystemResources2_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1)
)
eSystemResources2.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a41SystemResourcesIndex"),
)
if mibBuilder.loadTexts:
    eSystemResources2.setStatus("mandatory")
_A41SystemResourcesIndex_Type = DmiInteger
_A41SystemResourcesIndex_Object = MibTableColumn
a41SystemResourcesIndex = _A41SystemResourcesIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 1),
    _A41SystemResourcesIndex_Type()
)
a41SystemResourcesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41SystemResourcesIndex.setStatus("mandatory")
_A41ResourceUser_Type = DmiInteger
_A41ResourceUser_Object = MibTableColumn
a41ResourceUser = _A41ResourceUser_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 2),
    _A41ResourceUser_Type()
)
a41ResourceUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41ResourceUser.setStatus("mandatory")
_A41ResourceSet_Type = DmiInteger
_A41ResourceSet_Object = MibTableColumn
a41ResourceSet = _A41ResourceSet_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 3),
    _A41ResourceSet_Type()
)
a41ResourceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41ResourceSet.setStatus("mandatory")


class _A41ResourceAssignment_Type(Integer32):
    """Custom type a41ResourceAssignment based on Integer32"""
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
        *(("vAllocated", 3),
          ("vAssignable", 4),
          ("vOther", 1),
          ("vTemporaryAssignment", 5),
          ("vUnknown", 2))
    )


_A41ResourceAssignment_Type.__name__ = "Integer32"
_A41ResourceAssignment_Object = MibTableColumn
a41ResourceAssignment = _A41ResourceAssignment_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 4),
    _A41ResourceAssignment_Type()
)
a41ResourceAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41ResourceAssignment.setStatus("mandatory")


class _A41ResourceType_Type(Integer32):
    """Custom type a41ResourceType based on Integer32"""
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
          ("vIo", 4),
          ("vIrq", 5),
          ("vMemory", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A41ResourceType_Type.__name__ = "Integer32"
_A41ResourceType_Object = MibTableColumn
a41ResourceType = _A41ResourceType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 5),
    _A41ResourceType_Type()
)
a41ResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41ResourceType.setStatus("mandatory")
_A41ResourceNumber_Type = DmiInteger
_A41ResourceNumber_Object = MibTableColumn
a41ResourceNumber = _A41ResourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 6),
    _A41ResourceNumber_Type()
)
a41ResourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41ResourceNumber.setStatus("mandatory")
_A41ResourceInfoId_Type = DmiInteger
_A41ResourceInfoId_Object = MibTableColumn
a41ResourceInfoId = _A41ResourceInfoId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 7),
    _A41ResourceInfoId_Type()
)
a41ResourceInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41ResourceInfoId.setStatus("mandatory")
_A41StartAddress_Type = DmiInteger64X
_A41StartAddress_Object = MibTableColumn
a41StartAddress = _A41StartAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 8),
    _A41StartAddress_Type()
)
a41StartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41StartAddress.setStatus("mandatory")
_A41EndAddress_Type = DmiInteger64X
_A41EndAddress_Object = MibTableColumn
a41EndAddress = _A41EndAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 9),
    _A41EndAddress_Type()
)
a41EndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41EndAddress.setStatus("mandatory")
_A41ResourceSize_Type = DmiInteger
_A41ResourceSize_Object = MibTableColumn
a41ResourceSize = _A41ResourceSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 10),
    _A41ResourceSize_Type()
)
a41ResourceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41ResourceSize.setStatus("mandatory")
_A41BaseAlignment_Type = DmiInteger
_A41BaseAlignment_Object = MibTableColumn
a41BaseAlignment = _A41BaseAlignment_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 11),
    _A41BaseAlignment_Type()
)
a41BaseAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41BaseAlignment.setStatus("mandatory")


class _A41Shareable_Type(Integer32):
    """Custom type a41Shareable based on Integer32"""
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


_A41Shareable_Type.__name__ = "Integer32"
_A41Shareable_Object = MibTableColumn
a41Shareable = _A41Shareable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 12),
    _A41Shareable_Type()
)
a41Shareable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41Shareable.setStatus("mandatory")


class _A41Shared_Type(Integer32):
    """Custom type a41Shared based on Integer32"""
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


_A41Shared_Type.__name__ = "Integer32"
_A41Shared_Object = MibTableColumn
a41Shared = _A41Shared_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 41, 1, 13),
    _A41Shared_Type()
)
a41Shared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a41Shared.setStatus("mandatory")
_TSystemResourceDeviceInfo_Object = MibTable
tSystemResourceDeviceInfo = _TSystemResourceDeviceInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42)
)
if mibBuilder.loadTexts:
    tSystemResourceDeviceInfo.setStatus("mandatory")
_ESystemResourceDeviceInfo_Object = MibTableRow
eSystemResourceDeviceInfo = _ESystemResourceDeviceInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1)
)
eSystemResourceDeviceInfo.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a42ResourceUser"),
)
if mibBuilder.loadTexts:
    eSystemResourceDeviceInfo.setStatus("mandatory")
_A42ResourceUser_Type = DmiInteger
_A42ResourceUser_Object = MibTableColumn
a42ResourceUser = _A42ResourceUser_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 1),
    _A42ResourceUser_Type()
)
a42ResourceUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42ResourceUser.setStatus("mandatory")
_A42DeviceId_Type = DmiInteger
_A42DeviceId_Object = MibTableColumn
a42DeviceId = _A42DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 2),
    _A42DeviceId_Type()
)
a42DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42DeviceId.setStatus("mandatory")
_A42DeviceSerialNumber_Type = DmiInteger
_A42DeviceSerialNumber_Object = MibTableColumn
a42DeviceSerialNumber = _A42DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 3),
    _A42DeviceSerialNumber_Type()
)
a42DeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42DeviceSerialNumber.setStatus("mandatory")
_A42LogicalDeviceId_ClassCode_Type = DmiInteger
_A42LogicalDeviceId_ClassCode_Object = MibScalar
a42LogicalDeviceId_ClassCode = _A42LogicalDeviceId_ClassCode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 4),
    _A42LogicalDeviceId_ClassCode_Type()
)
a42LogicalDeviceId_ClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42LogicalDeviceId_ClassCode.setStatus("mandatory")
_A42DeviceFlags_Type = DmiInteger
_A42DeviceFlags_Object = MibTableColumn
a42DeviceFlags = _A42DeviceFlags_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 5),
    _A42DeviceFlags_Type()
)
a42DeviceFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42DeviceFlags.setStatus("mandatory")
_A42DeviceNumber_Type = DmiInteger
_A42DeviceNumber_Object = MibTableColumn
a42DeviceNumber = _A42DeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 6),
    _A42DeviceNumber_Type()
)
a42DeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42DeviceNumber.setStatus("mandatory")
_A42FunctionNumber_Type = DmiInteger
_A42FunctionNumber_Object = MibTableColumn
a42FunctionNumber = _A42FunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 7),
    _A42FunctionNumber_Type()
)
a42FunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42FunctionNumber.setStatus("mandatory")
_A42BusType_Type = DmiInteger
_A42BusType_Object = MibTableColumn
a42BusType = _A42BusType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 8),
    _A42BusType_Type()
)
a42BusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42BusType.setStatus("mandatory")
_A42CmReserved_Type = DmiInteger
_A42CmReserved_Object = MibTableColumn
a42CmReserved = _A42CmReserved_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 42, 1, 9),
    _A42CmReserved_Type()
)
a42CmReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a42CmReserved.setStatus("mandatory")
_TSystemResourceMemoryInfo_Object = MibTable
tSystemResourceMemoryInfo = _TSystemResourceMemoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43)
)
if mibBuilder.loadTexts:
    tSystemResourceMemoryInfo.setStatus("mandatory")
_ESystemResourceMemoryInfo_Object = MibTableRow
eSystemResourceMemoryInfo = _ESystemResourceMemoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1)
)
eSystemResourceMemoryInfo.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a43SystemResourceMemoryInfoIndex"),
)
if mibBuilder.loadTexts:
    eSystemResourceMemoryInfo.setStatus("mandatory")
_A43SystemResourceMemoryInfoIndex_Type = DmiInteger
_A43SystemResourceMemoryInfoIndex_Object = MibTableColumn
a43SystemResourceMemoryInfoIndex = _A43SystemResourceMemoryInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 1),
    _A43SystemResourceMemoryInfoIndex_Type()
)
a43SystemResourceMemoryInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a43SystemResourceMemoryInfoIndex.setStatus("mandatory")


class _A43IsapcmciaRangeDescriptor_Type(Integer32):
    """Custom type a43IsapcmciaRangeDescriptor based on Integer32"""
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
        *(("v16-bitMemoryOnly", 4),
          ("v32-bitMemoryOnly", 6),
          ("v8-And16-bitMemorySupported", 5),
          ("v8-bitMemoryOnly", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A43IsapcmciaRangeDescriptor_Type.__name__ = "Integer32"
_A43IsapcmciaRangeDescriptor_Object = MibTableColumn
a43IsapcmciaRangeDescriptor = _A43IsapcmciaRangeDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 2),
    _A43IsapcmciaRangeDescriptor_Type()
)
a43IsapcmciaRangeDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a43IsapcmciaRangeDescriptor.setStatus("mandatory")


class _A43EisaRangeDescriptor_Type(Integer32):
    """Custom type a43EisaRangeDescriptor based on Integer32"""
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
        *(("v16-bitMemoryOnly", 4),
          ("v32-bitMemoryOnly", 6),
          ("v8-And16-bitMemorySupported", 5),
          ("v8-bitMemoryOnly", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A43EisaRangeDescriptor_Type.__name__ = "Integer32"
_A43EisaRangeDescriptor_Object = MibTableColumn
a43EisaRangeDescriptor = _A43EisaRangeDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 3),
    _A43EisaRangeDescriptor_Type()
)
a43EisaRangeDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a43EisaRangeDescriptor.setStatus("mandatory")


class _A43DecodeSupport_Type(Integer32):
    """Custom type a43DecodeSupport based on Integer32"""
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
        *(("vDecodeSupportsHighAddress", 3),
          ("vDecodeSupportsRangeLength", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A43DecodeSupport_Type.__name__ = "Integer32"
_A43DecodeSupport_Object = MibTableColumn
a43DecodeSupport = _A43DecodeSupport_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 4),
    _A43DecodeSupport_Type()
)
a43DecodeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a43DecodeSupport.setStatus("mandatory")


class _A43Cacheable_Type(Integer32):
    """Custom type a43Cacheable based on Integer32"""
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


_A43Cacheable_Type.__name__ = "Integer32"
_A43Cacheable_Object = MibTableColumn
a43Cacheable = _A43Cacheable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 5),
    _A43Cacheable_Type()
)
a43Cacheable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a43Cacheable.setStatus("mandatory")


class _A43CacheType_Type(Integer32):
    """Custom type a43CacheType based on Integer32"""
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
          ("vWrite-back", 3),
          ("vWrite-through", 4))
    )


_A43CacheType_Type.__name__ = "Integer32"
_A43CacheType_Object = MibTableColumn
a43CacheType = _A43CacheType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 6),
    _A43CacheType_Type()
)
a43CacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a43CacheType.setStatus("mandatory")


class _A43Read_write_Type(Integer32):
    """Custom type a43Read_write based on Integer32"""
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
          ("vRamReadwrite", 4),
          ("vRomReadOnly", 3),
          ("vUnknown", 2))
    )


_A43Read_write_Type.__name__ = "Integer32"
_A43Read_write_Object = MibScalar
a43Read_write = _A43Read_write_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 43, 1, 7),
    _A43Read_write_Type()
)
a43Read_write.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a43Read_write.setStatus("mandatory")
_TSystemResourceIoInfo_Object = MibTable
tSystemResourceIoInfo = _TSystemResourceIoInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44)
)
if mibBuilder.loadTexts:
    tSystemResourceIoInfo.setStatus("mandatory")
_ESystemResourceIoInfo_Object = MibTableRow
eSystemResourceIoInfo = _ESystemResourceIoInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44, 1)
)
eSystemResourceIoInfo.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a44SystemResourceIoInfoIndex"),
)
if mibBuilder.loadTexts:
    eSystemResourceIoInfo.setStatus("mandatory")
_A44SystemResourceIoInfoIndex_Type = DmiInteger
_A44SystemResourceIoInfoIndex_Object = MibTableColumn
a44SystemResourceIoInfoIndex = _A44SystemResourceIoInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44, 1, 1),
    _A44SystemResourceIoInfoIndex_Type()
)
a44SystemResourceIoInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a44SystemResourceIoInfoIndex.setStatus("mandatory")


class _A44IoDecode_Type(Integer32):
    """Custom type a44IoDecode based on Integer32"""
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
        *(("v10Bits", 3),
          ("v16Bits", 4),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A44IoDecode_Type.__name__ = "Integer32"
_A44IoDecode_Object = MibTableColumn
a44IoDecode = _A44IoDecode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 44, 1, 2),
    _A44IoDecode_Type()
)
a44IoDecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a44IoDecode.setStatus("mandatory")
_TSystemResourceIrqInfo_Object = MibTable
tSystemResourceIrqInfo = _TSystemResourceIrqInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45)
)
if mibBuilder.loadTexts:
    tSystemResourceIrqInfo.setStatus("mandatory")
_ESystemResourceIrqInfo_Object = MibTableRow
eSystemResourceIrqInfo = _ESystemResourceIrqInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1)
)
eSystemResourceIrqInfo.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a45SystemResourceIrqInfoIndex"),
)
if mibBuilder.loadTexts:
    eSystemResourceIrqInfo.setStatus("mandatory")
_A45SystemResourceIrqInfoIndex_Type = DmiInteger
_A45SystemResourceIrqInfoIndex_Object = MibTableColumn
a45SystemResourceIrqInfoIndex = _A45SystemResourceIrqInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1, 1),
    _A45SystemResourceIrqInfoIndex_Type()
)
a45SystemResourceIrqInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45SystemResourceIrqInfoIndex.setStatus("mandatory")


class _A45TriggerType_Type(Integer32):
    """Custom type a45TriggerType based on Integer32"""
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


_A45TriggerType_Type.__name__ = "Integer32"
_A45TriggerType_Object = MibTableColumn
a45TriggerType = _A45TriggerType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1, 2),
    _A45TriggerType_Type()
)
a45TriggerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45TriggerType.setStatus("mandatory")


class _A45TriggerLevel_Type(Integer32):
    """Custom type a45TriggerLevel based on Integer32"""
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
        *(("vActiveHigh", 4),
          ("vActiveLow", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A45TriggerLevel_Type.__name__ = "Integer32"
_A45TriggerLevel_Object = MibTableColumn
a45TriggerLevel = _A45TriggerLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 45, 1, 3),
    _A45TriggerLevel_Type()
)
a45TriggerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a45TriggerLevel.setStatus("mandatory")
_TSystemResourceDmaInfo_Object = MibTable
tSystemResourceDmaInfo = _TSystemResourceDmaInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46)
)
if mibBuilder.loadTexts:
    tSystemResourceDmaInfo.setStatus("mandatory")
_ESystemResourceDmaInfo_Object = MibTableRow
eSystemResourceDmaInfo = _ESystemResourceDmaInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1)
)
eSystemResourceDmaInfo.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "a46SystemResourceDmaInfoIndex"),
)
if mibBuilder.loadTexts:
    eSystemResourceDmaInfo.setStatus("mandatory")
_A46SystemResourceDmaInfoIndex_Type = DmiInteger
_A46SystemResourceDmaInfoIndex_Object = MibTableColumn
a46SystemResourceDmaInfoIndex = _A46SystemResourceDmaInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 1),
    _A46SystemResourceDmaInfoIndex_Type()
)
a46SystemResourceDmaInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46SystemResourceDmaInfoIndex.setStatus("mandatory")


class _A46DmaTransferWidth_Type(Integer32):
    """Custom type a46DmaTransferWidth based on Integer32"""
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
        *(("v128-bit", 8),
          ("v16-bit", 5),
          ("v32-bit", 6),
          ("v64-bit", 7),
          ("v8-And16-bit", 4),
          ("v8-bit", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A46DmaTransferWidth_Type.__name__ = "Integer32"
_A46DmaTransferWidth_Object = MibTableColumn
a46DmaTransferWidth = _A46DmaTransferWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 2),
    _A46DmaTransferWidth_Type()
)
a46DmaTransferWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46DmaTransferWidth.setStatus("mandatory")


class _A46DmaAddressSize_Type(Integer32):
    """Custom type a46DmaAddressSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("v16-bit", 5),
          ("v32-bit", 6),
          ("v64-bit", 7),
          ("v8-bit", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A46DmaAddressSize_Type.__name__ = "Integer32"
_A46DmaAddressSize_Object = MibTableColumn
a46DmaAddressSize = _A46DmaAddressSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 3),
    _A46DmaAddressSize_Type()
)
a46DmaAddressSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46DmaAddressSize.setStatus("mandatory")
_A46DmaMaximumTransferSize_Type = DmiInteger
_A46DmaMaximumTransferSize_Object = MibTableColumn
a46DmaMaximumTransferSize = _A46DmaMaximumTransferSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 4),
    _A46DmaMaximumTransferSize_Type()
)
a46DmaMaximumTransferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46DmaMaximumTransferSize.setStatus("mandatory")


class _A46DmaTransferPreference_Type(Integer32):
    """Custom type a46DmaTransferPreference based on Integer32"""
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
        *(("v16-bit", 5),
          ("v32-bit", 6),
          ("v64-bit", 7),
          ("v8-And16-bit", 4),
          ("v8-bit", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A46DmaTransferPreference_Type.__name__ = "Integer32"
_A46DmaTransferPreference_Object = MibTableColumn
a46DmaTransferPreference = _A46DmaTransferPreference_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 5),
    _A46DmaTransferPreference_Type()
)
a46DmaTransferPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46DmaTransferPreference.setStatus("mandatory")


class _A46BusMaster_Type(Integer32):
    """Custom type a46BusMaster based on Integer32"""
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
        *(("vLogicalDeviceIsABusMaster", 4),
          ("vLogicalDeviceIsNotABusMaster", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A46BusMaster_Type.__name__ = "Integer32"
_A46BusMaster_Object = MibTableColumn
a46BusMaster = _A46BusMaster_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 6),
    _A46BusMaster_Type()
)
a46BusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46BusMaster.setStatus("mandatory")


class _A46ByteMode_Type(Integer32):
    """Custom type a46ByteMode based on Integer32"""
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
        *(("vDmaMayExecuteInCountByByteMode", 4),
          ("vDmaMayNotExecuteInCountByByteMode", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A46ByteMode_Type.__name__ = "Integer32"
_A46ByteMode_Object = MibTableColumn
a46ByteMode = _A46ByteMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 7),
    _A46ByteMode_Type()
)
a46ByteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46ByteMode.setStatus("mandatory")


class _A46WordMode_Type(Integer32):
    """Custom type a46WordMode based on Integer32"""
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
        *(("vDmaMayExecuteInCountByWordMode", 4),
          ("vDmaMayNotExecuteInCountByWordMode", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A46WordMode_Type.__name__ = "Integer32"
_A46WordMode_Object = MibTableColumn
a46WordMode = _A46WordMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 8),
    _A46WordMode_Type()
)
a46WordMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46WordMode.setStatus("mandatory")


class _A46ChannelTiming_Type(Integer32):
    """Custom type a46ChannelTiming based on Integer32"""
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
        *(("vIsaCompatible", 3),
          ("vOther", 1),
          ("vTypeA", 4),
          ("vTypeB", 5),
          ("vTypeF", 6),
          ("vUnknown", 2))
    )


_A46ChannelTiming_Type.__name__ = "Integer32"
_A46ChannelTiming_Object = MibTableColumn
a46ChannelTiming = _A46ChannelTiming_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 9),
    _A46ChannelTiming_Type()
)
a46ChannelTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46ChannelTiming.setStatus("mandatory")


class _A46Type_cTiming_Type(Integer32):
    """Custom type a46Type_cTiming based on Integer32"""
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
        *(("vCTypeTimingIsNotSupported", 4),
          ("vCTypeTimingIsSupported", 5),
          ("vIsaCompatible", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A46Type_cTiming_Type.__name__ = "Integer32"
_A46Type_cTiming_Object = MibScalar
a46Type_cTiming = _A46Type_cTiming_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 46, 1, 10),
    _A46Type_cTiming_Type()
)
a46Type_cTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a46Type_cTiming.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1)
)
eMiftomib.setIndexNames(
    (0, "INTELCORPORATIONBASEBOARDRESOURCES-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A1001MibName_Type = DmiDisplaystring
_A1001MibName_Object = MibTableColumn
a1001MibName = _A1001MibName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1, 1),
    _A1001MibName_Type()
)
a1001MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibName.setStatus("mandatory")
_A1001MibOid_Type = DmiDisplaystring
_A1001MibOid_Object = MibTableColumn
a1001MibOid = _A1001MibOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1, 2),
    _A1001MibOid_Type()
)
a1001MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1001MibOid.setStatus("mandatory")
_A1001DisableTrap_Type = DmiInteger
_A1001DisableTrap_Object = MibTableColumn
a1001DisableTrap = _A1001DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 2, 3, 1, 1001, 1, 3),
    _A1001DisableTrap_Type()
)
a1001DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a1001DisableTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATIONBASEBOARDRESOURCES-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiInteger64X": DmiInteger64X,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "intel": intel,
       "products": products,
       "server-products": server_products,
       "platforms": platforms,
       "resources": resources,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tSystemResources2": tSystemResources2,
       "eSystemResources2": eSystemResources2,
       "a41SystemResourcesIndex": a41SystemResourcesIndex,
       "a41ResourceUser": a41ResourceUser,
       "a41ResourceSet": a41ResourceSet,
       "a41ResourceAssignment": a41ResourceAssignment,
       "a41ResourceType": a41ResourceType,
       "a41ResourceNumber": a41ResourceNumber,
       "a41ResourceInfoId": a41ResourceInfoId,
       "a41StartAddress": a41StartAddress,
       "a41EndAddress": a41EndAddress,
       "a41ResourceSize": a41ResourceSize,
       "a41BaseAlignment": a41BaseAlignment,
       "a41Shareable": a41Shareable,
       "a41Shared": a41Shared,
       "tSystemResourceDeviceInfo": tSystemResourceDeviceInfo,
       "eSystemResourceDeviceInfo": eSystemResourceDeviceInfo,
       "a42ResourceUser": a42ResourceUser,
       "a42DeviceId": a42DeviceId,
       "a42DeviceSerialNumber": a42DeviceSerialNumber,
       "a42LogicalDeviceId-ClassCode": a42LogicalDeviceId_ClassCode,
       "a42DeviceFlags": a42DeviceFlags,
       "a42DeviceNumber": a42DeviceNumber,
       "a42FunctionNumber": a42FunctionNumber,
       "a42BusType": a42BusType,
       "a42CmReserved": a42CmReserved,
       "tSystemResourceMemoryInfo": tSystemResourceMemoryInfo,
       "eSystemResourceMemoryInfo": eSystemResourceMemoryInfo,
       "a43SystemResourceMemoryInfoIndex": a43SystemResourceMemoryInfoIndex,
       "a43IsapcmciaRangeDescriptor": a43IsapcmciaRangeDescriptor,
       "a43EisaRangeDescriptor": a43EisaRangeDescriptor,
       "a43DecodeSupport": a43DecodeSupport,
       "a43Cacheable": a43Cacheable,
       "a43CacheType": a43CacheType,
       "a43Read-write": a43Read_write,
       "tSystemResourceIoInfo": tSystemResourceIoInfo,
       "eSystemResourceIoInfo": eSystemResourceIoInfo,
       "a44SystemResourceIoInfoIndex": a44SystemResourceIoInfoIndex,
       "a44IoDecode": a44IoDecode,
       "tSystemResourceIrqInfo": tSystemResourceIrqInfo,
       "eSystemResourceIrqInfo": eSystemResourceIrqInfo,
       "a45SystemResourceIrqInfoIndex": a45SystemResourceIrqInfoIndex,
       "a45TriggerType": a45TriggerType,
       "a45TriggerLevel": a45TriggerLevel,
       "tSystemResourceDmaInfo": tSystemResourceDmaInfo,
       "eSystemResourceDmaInfo": eSystemResourceDmaInfo,
       "a46SystemResourceDmaInfoIndex": a46SystemResourceDmaInfoIndex,
       "a46DmaTransferWidth": a46DmaTransferWidth,
       "a46DmaAddressSize": a46DmaAddressSize,
       "a46DmaMaximumTransferSize": a46DmaMaximumTransferSize,
       "a46DmaTransferPreference": a46DmaTransferPreference,
       "a46BusMaster": a46BusMaster,
       "a46ByteMode": a46ByteMode,
       "a46WordMode": a46WordMode,
       "a46ChannelTiming": a46ChannelTiming,
       "a46Type-cTiming": a46Type_cTiming,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a1001MibName": a1001MibName,
       "a1001MibOid": a1001MibOid,
       "a1001DisableTrap": a1001DisableTrap}
)
