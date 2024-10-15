# SNMP MIB module (INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:21 2024
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




class DmiCounter64X(Integer32):
    """Custom type DmiCounter64X based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18446744073709551615),
    )





class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




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
_Nic_ObjectIdentity = ObjectIdentity
nic = _Nic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4)
)
_E100b_ObjectIdentity = ObjectIdentity
e100b = _E100b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TSystemResourcesDescription_Object = MibTable
tSystemResourcesDescription = _TSystemResourcesDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tSystemResourcesDescription.setStatus("mandatory")
_ESystemResourcesDescription_Object = MibTableRow
eSystemResourcesDescription = _ESystemResourcesDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 2, 1)
)
eSystemResourcesDescription.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSystemResourcesDescription.setStatus("mandatory")
_A2DeviceCount_Type = DmiInteger
_A2DeviceCount_Object = MibTableColumn
a2DeviceCount = _A2DeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 2, 1, 1),
    _A2DeviceCount_Type()
)
a2DeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2DeviceCount.setStatus("mandatory")
_A2SystemResourceCount_Type = DmiInteger
_A2SystemResourceCount_Object = MibTableColumn
a2SystemResourceCount = _A2SystemResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 2, 1, 2),
    _A2SystemResourceCount_Type()
)
a2SystemResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SystemResourceCount.setStatus("mandatory")
_TSystemResources_Object = MibTable
tSystemResources = _TSystemResources_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tSystemResources.setStatus("mandatory")
_ESystemResources_Object = MibTableRow
eSystemResources = _ESystemResources_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1)
)
eSystemResources.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a3DeviceId"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a3ResourceNumber"),
)
if mibBuilder.loadTexts:
    eSystemResources.setStatus("mandatory")
_A3DeviceId_Type = DmiInteger
_A3DeviceId_Object = MibTableColumn
a3DeviceId = _A3DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1, 1),
    _A3DeviceId_Type()
)
a3DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3DeviceId.setStatus("mandatory")
_A3ResourceNumber_Type = DmiInteger
_A3ResourceNumber_Object = MibTableColumn
a3ResourceNumber = _A3ResourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1, 2),
    _A3ResourceNumber_Type()
)
a3ResourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ResourceNumber.setStatus("mandatory")


class _A3ResourceType_Type(Integer32):
    """Custom type a3ResourceType based on Integer32"""
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


_A3ResourceType_Type.__name__ = "Integer32"
_A3ResourceType_Object = MibTableColumn
a3ResourceType = _A3ResourceType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1, 3),
    _A3ResourceType_Type()
)
a3ResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ResourceType.setStatus("mandatory")
_A3ResourceBase_Type = DmiInteger
_A3ResourceBase_Object = MibTableColumn
a3ResourceBase = _A3ResourceBase_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1, 4),
    _A3ResourceBase_Type()
)
a3ResourceBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ResourceBase.setStatus("mandatory")
_A3ResourceSize_Type = DmiInteger
_A3ResourceSize_Object = MibTableColumn
a3ResourceSize = _A3ResourceSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1, 5),
    _A3ResourceSize_Type()
)
a3ResourceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ResourceSize.setStatus("mandatory")
_A3ResourceFlags_Type = DmiInteger
_A3ResourceFlags_Object = MibTableColumn
a3ResourceFlags = _A3ResourceFlags_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1, 6),
    _A3ResourceFlags_Type()
)
a3ResourceFlags.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ResourceFlags.setStatus("mandatory")
_A3GroupId_Type = DmiInteger
_A3GroupId_Object = MibTableColumn
a3GroupId = _A3GroupId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 3, 1, 7),
    _A3GroupId_Type()
)
a3GroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3GroupId.setStatus("mandatory")
_TNetworkAdapter802PortGroup_Object = MibTable
tNetworkAdapter802PortGroup = _TNetworkAdapter802PortGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tNetworkAdapter802PortGroup.setStatus("mandatory")
_ENetworkAdapter802PortGroup_Object = MibTableRow
eNetworkAdapter802PortGroup = _ENetworkAdapter802PortGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1)
)
eNetworkAdapter802PortGroup.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a4PortIndex"),
)
if mibBuilder.loadTexts:
    eNetworkAdapter802PortGroup.setStatus("mandatory")
_A4PortIndex_Type = DmiInteger
_A4PortIndex_Object = MibTableColumn
a4PortIndex = _A4PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 1),
    _A4PortIndex_Type()
)
a4PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4PortIndex.setStatus("mandatory")
_A4PermanentNetworkAddress_Type = DmiDisplaystring
_A4PermanentNetworkAddress_Object = MibTableColumn
a4PermanentNetworkAddress = _A4PermanentNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 2),
    _A4PermanentNetworkAddress_Type()
)
a4PermanentNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4PermanentNetworkAddress.setStatus("mandatory")
_A4CurrentNetworkAddress_Type = DmiDisplaystring
_A4CurrentNetworkAddress_Object = MibTableColumn
a4CurrentNetworkAddress = _A4CurrentNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 3),
    _A4CurrentNetworkAddress_Type()
)
a4CurrentNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4CurrentNetworkAddress.setStatus("mandatory")


class _A4ConnectorType_Type(Integer32):
    """Custom type a4ConnectorType based on Integer32"""
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


_A4ConnectorType_Type.__name__ = "Integer32"
_A4ConnectorType_Object = MibTableColumn
a4ConnectorType = _A4ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 4),
    _A4ConnectorType_Type()
)
a4ConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ConnectorType.setStatus("mandatory")
_A4DataRate_Type = DmiInteger
_A4DataRate_Object = MibTableColumn
a4DataRate = _A4DataRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 5),
    _A4DataRate_Type()
)
a4DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4DataRate.setStatus("mandatory")
_A4TotalPacketsTransmitted_Type = DmiCounter64X
_A4TotalPacketsTransmitted_Object = MibTableColumn
a4TotalPacketsTransmitted = _A4TotalPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 6),
    _A4TotalPacketsTransmitted_Type()
)
a4TotalPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalPacketsTransmitted.setStatus("mandatory")
_A4TotalBytesTransmitted_Type = DmiCounter64X
_A4TotalBytesTransmitted_Object = MibTableColumn
a4TotalBytesTransmitted = _A4TotalBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 7),
    _A4TotalBytesTransmitted_Type()
)
a4TotalBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalBytesTransmitted.setStatus("mandatory")
_A4TotalPacketsReceived_Type = DmiCounter64X
_A4TotalPacketsReceived_Object = MibTableColumn
a4TotalPacketsReceived = _A4TotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 8),
    _A4TotalPacketsReceived_Type()
)
a4TotalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalPacketsReceived.setStatus("mandatory")
_A4TotalBytesReceived_Type = DmiCounter64X
_A4TotalBytesReceived_Object = MibTableColumn
a4TotalBytesReceived = _A4TotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 9),
    _A4TotalBytesReceived_Type()
)
a4TotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalBytesReceived.setStatus("mandatory")
_A4TotalTransmitErrors_Type = DmiCounter64X
_A4TotalTransmitErrors_Object = MibTableColumn
a4TotalTransmitErrors = _A4TotalTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 10),
    _A4TotalTransmitErrors_Type()
)
a4TotalTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalTransmitErrors.setStatus("mandatory")
_A4TotalReceiveErrors_Type = DmiCounter64X
_A4TotalReceiveErrors_Object = MibTableColumn
a4TotalReceiveErrors = _A4TotalReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 11),
    _A4TotalReceiveErrors_Type()
)
a4TotalReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalReceiveErrors.setStatus("mandatory")
_A4TotalHostErrors_Type = DmiCounter64X
_A4TotalHostErrors_Object = MibTableColumn
a4TotalHostErrors = _A4TotalHostErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 12),
    _A4TotalHostErrors_Type()
)
a4TotalHostErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalHostErrors.setStatus("mandatory")
_A4TotalWireErrors_Type = DmiCounter64X
_A4TotalWireErrors_Object = MibTableColumn
a4TotalWireErrors = _A4TotalWireErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 4, 1, 13),
    _A4TotalWireErrors_Type()
)
a4TotalWireErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4TotalWireErrors.setStatus("mandatory")
_T802AlternateAddressGroup_Object = MibTable
t802AlternateAddressGroup = _T802AlternateAddressGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    t802AlternateAddressGroup.setStatus("mandatory")
_E802AlternateAddressGroup_Object = MibTableRow
e802AlternateAddressGroup = _E802AlternateAddressGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 5, 1)
)
e802AlternateAddressGroup.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a5AlternateAddressIndex"),
)
if mibBuilder.loadTexts:
    e802AlternateAddressGroup.setStatus("mandatory")
_A5AlternateAddressIndex_Type = DmiInteger
_A5AlternateAddressIndex_Object = MibTableColumn
a5AlternateAddressIndex = _A5AlternateAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 5, 1, 1),
    _A5AlternateAddressIndex_Type()
)
a5AlternateAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a5AlternateAddressIndex.setStatus("mandatory")
_A5PortIndex_Type = DmiInteger
_A5PortIndex_Object = MibTableColumn
a5PortIndex = _A5PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 5, 1, 2),
    _A5PortIndex_Type()
)
a5PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a5PortIndex.setStatus("mandatory")


class _A5AddressType_Type(Integer32):
    """Custom type a5AddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vFunctional", 2),
          ("vGroup", 3),
          ("vMulticast", 1))
    )


_A5AddressType_Type.__name__ = "Integer32"
_A5AddressType_Object = MibTableColumn
a5AddressType = _A5AddressType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 5, 1, 3),
    _A5AddressType_Type()
)
a5AddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a5AddressType.setStatus("mandatory")
_A5AlternateAddress_Type = DmiDisplaystring
_A5AlternateAddress_Object = MibTableColumn
a5AlternateAddress = _A5AlternateAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 5, 1, 4),
    _A5AlternateAddress_Type()
)
a5AlternateAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a5AlternateAddress.setStatus("mandatory")
_TNetworkAdapterDriverGroup_Object = MibTable
tNetworkAdapterDriverGroup = _TNetworkAdapterDriverGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tNetworkAdapterDriverGroup.setStatus("mandatory")
_ENetworkAdapterDriverGroup_Object = MibTableRow
eNetworkAdapterDriverGroup = _ENetworkAdapterDriverGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1)
)
eNetworkAdapterDriverGroup.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a6DriverIndex"),
)
if mibBuilder.loadTexts:
    eNetworkAdapterDriverGroup.setStatus("mandatory")
_A6DriverIndex_Type = DmiInteger
_A6DriverIndex_Object = MibTableColumn
a6DriverIndex = _A6DriverIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 1),
    _A6DriverIndex_Type()
)
a6DriverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverIndex.setStatus("mandatory")
_A6DriverSoftwareName_Type = DmiDisplaystring
_A6DriverSoftwareName_Object = MibTableColumn
a6DriverSoftwareName = _A6DriverSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 2),
    _A6DriverSoftwareName_Type()
)
a6DriverSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverSoftwareName.setStatus("mandatory")
_A6DriverSoftwareVersion_Type = DmiDisplaystring
_A6DriverSoftwareVersion_Object = MibTableColumn
a6DriverSoftwareVersion = _A6DriverSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 3),
    _A6DriverSoftwareVersion_Type()
)
a6DriverSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverSoftwareVersion.setStatus("mandatory")
_A6DriverSoftwareDescription_Type = DmiDisplaystring
_A6DriverSoftwareDescription_Object = MibTableColumn
a6DriverSoftwareDescription = _A6DriverSoftwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 4),
    _A6DriverSoftwareDescription_Type()
)
a6DriverSoftwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverSoftwareDescription.setStatus("mandatory")
_A6DriverSize_Type = DmiInteger
_A6DriverSize_Object = MibTableColumn
a6DriverSize = _A6DriverSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 5),
    _A6DriverSize_Type()
)
a6DriverSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverSize.setStatus("mandatory")


class _A6DriverInterfaceType_Type(Integer32):
    """Custom type a6DriverInterfaceType based on Integer32"""
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
        *(("vAppletalk", 8),
          ("vIbmLanSupportProgram", 9),
          ("vIpx", 2),
          ("vLantastic", 6),
          ("vLlc", 10),
          ("vNdis", 4),
          ("vNetbios", 11),
          ("vOdi", 3),
          ("vOther", 1),
          ("vPacketDriver", 5),
          ("vPathworksDll", 12),
          ("vUnix", 7))
    )


_A6DriverInterfaceType_Type.__name__ = "Integer32"
_A6DriverInterfaceType_Object = MibTableColumn
a6DriverInterfaceType = _A6DriverInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 6),
    _A6DriverInterfaceType_Type()
)
a6DriverInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverInterfaceType.setStatus("mandatory")
_A6DriverInterfaceVersion_Type = DmiDisplaystring
_A6DriverInterfaceVersion_Object = MibTableColumn
a6DriverInterfaceVersion = _A6DriverInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 7),
    _A6DriverInterfaceVersion_Type()
)
a6DriverInterfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverInterfaceVersion.setStatus("mandatory")
_A6DriverInterfaceDescription_Type = DmiDisplaystring
_A6DriverInterfaceDescription_Object = MibTableColumn
a6DriverInterfaceDescription = _A6DriverInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 6, 1, 8),
    _A6DriverInterfaceDescription_Type()
)
a6DriverInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DriverInterfaceDescription.setStatus("mandatory")
_TNetworkAdapterHardwareGroup_Object = MibTable
tNetworkAdapterHardwareGroup = _TNetworkAdapterHardwareGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tNetworkAdapterHardwareGroup.setStatus("mandatory")
_ENetworkAdapterHardwareGroup_Object = MibTableRow
eNetworkAdapterHardwareGroup = _ENetworkAdapterHardwareGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 7, 1)
)
eNetworkAdapterHardwareGroup.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eNetworkAdapterHardwareGroup.setStatus("mandatory")


class _A7NetworkTopology_Type(Integer32):
    """Custom type a7NetworkTopology based on Integer32"""
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
        *(("v10010MbpsEthernet", 4),
          ("v100MbpsEthernet", 3),
          ("v100MbpsVgAnylan", 5),
          ("v10MbpsEthernet", 2),
          ("v164MbpsToken-ring", 8),
          ("v16MbpsToken-ring", 7),
          ("v20MbpsArcnet", 10),
          ("v2MbpsArcnet", 9),
          ("v4MbpsToken-ring", 6),
          ("vAppletalk1", 13),
          ("vAtm", 12),
          ("vFddi", 11),
          ("vOther", 1))
    )


_A7NetworkTopology_Type.__name__ = "Integer32"
_A7NetworkTopology_Object = MibTableColumn
a7NetworkTopology = _A7NetworkTopology_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 7, 1, 1),
    _A7NetworkTopology_Type()
)
a7NetworkTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7NetworkTopology.setStatus("mandatory")


class _A7TransmissionCapability_Type(Integer32):
    """Custom type a7TransmissionCapability based on Integer32"""
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


_A7TransmissionCapability_Type.__name__ = "Integer32"
_A7TransmissionCapability_Object = MibTableColumn
a7TransmissionCapability = _A7TransmissionCapability_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 7, 1, 2),
    _A7TransmissionCapability_Type()
)
a7TransmissionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7TransmissionCapability.setStatus("mandatory")
_A7NetworkAdapterRamSize_Type = DmiInteger
_A7NetworkAdapterRamSize_Object = MibTableColumn
a7NetworkAdapterRamSize = _A7NetworkAdapterRamSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 7, 1, 3),
    _A7NetworkAdapterRamSize_Type()
)
a7NetworkAdapterRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7NetworkAdapterRamSize.setStatus("mandatory")


class _A7BusType_Type(Integer32):
    """Custom type a7BusType based on Integer32"""
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


_A7BusType_Type.__name__ = "Integer32"
_A7BusType_Object = MibTableColumn
a7BusType = _A7BusType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 7, 1, 4),
    _A7BusType_Type()
)
a7BusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7BusType.setStatus("mandatory")


class _A7BusWidth_Type(Integer32):
    """Custom type a7BusWidth based on Integer32"""
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


_A7BusWidth_Type.__name__ = "Integer32"
_A7BusWidth_Object = MibTableColumn
a7BusWidth = _A7BusWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 7, 1, 5),
    _A7BusWidth_Type()
)
a7BusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7BusWidth.setStatus("mandatory")
_TOperationalState_Object = MibTable
tOperationalState = _TOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tOperationalState.setStatus("mandatory")
_EOperationalState_Object = MibTableRow
eOperationalState = _EOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1)
)
eOperationalState.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a8OperationalStateInstanceIndex"),
)
if mibBuilder.loadTexts:
    eOperationalState.setStatus("mandatory")
_A8OperationalStateInstanceIndex_Type = DmiInteger
_A8OperationalStateInstanceIndex_Object = MibTableColumn
a8OperationalStateInstanceIndex = _A8OperationalStateInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 1),
    _A8OperationalStateInstanceIndex_Type()
)
a8OperationalStateInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8OperationalStateInstanceIndex.setStatus("mandatory")
_A8DeviceGroupIndex_Type = DmiInteger
_A8DeviceGroupIndex_Object = MibTableColumn
a8DeviceGroupIndex = _A8DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 2),
    _A8DeviceGroupIndex_Type()
)
a8DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8DeviceGroupIndex.setStatus("mandatory")


class _A8OperationalStatus_Type(Integer32):
    """Custom type a8OperationalStatus based on Integer32"""
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


_A8OperationalStatus_Type.__name__ = "Integer32"
_A8OperationalStatus_Object = MibTableColumn
a8OperationalStatus = _A8OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 3),
    _A8OperationalStatus_Type()
)
a8OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8OperationalStatus.setStatus("mandatory")


class _A8UsageState_Type(Integer32):
    """Custom type a8UsageState based on Integer32"""
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


_A8UsageState_Type.__name__ = "Integer32"
_A8UsageState_Object = MibTableColumn
a8UsageState = _A8UsageState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 4),
    _A8UsageState_Type()
)
a8UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8UsageState.setStatus("mandatory")


class _A8AvailabilityStatus_Type(Integer32):
    """Custom type a8AvailabilityStatus based on Integer32"""
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


_A8AvailabilityStatus_Type.__name__ = "Integer32"
_A8AvailabilityStatus_Object = MibTableColumn
a8AvailabilityStatus = _A8AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 5),
    _A8AvailabilityStatus_Type()
)
a8AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8AvailabilityStatus.setStatus("mandatory")


class _A8AdministrativeState_Type(Integer32):
    """Custom type a8AdministrativeState based on Integer32"""
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


_A8AdministrativeState_Type.__name__ = "Integer32"
_A8AdministrativeState_Object = MibTableColumn
a8AdministrativeState = _A8AdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 6),
    _A8AdministrativeState_Type()
)
a8AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8AdministrativeState.setStatus("mandatory")
_A8FatalErrorCount_Type = DmiCounter
_A8FatalErrorCount_Object = MibTableColumn
a8FatalErrorCount = _A8FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 7),
    _A8FatalErrorCount_Type()
)
a8FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8FatalErrorCount.setStatus("mandatory")
_A8MajorErrorCount_Type = DmiCounter
_A8MajorErrorCount_Object = MibTableColumn
a8MajorErrorCount = _A8MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 8),
    _A8MajorErrorCount_Type()
)
a8MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8MajorErrorCount.setStatus("mandatory")
_A8WarningErrorCount_Type = DmiCounter
_A8WarningErrorCount_Object = MibTableColumn
a8WarningErrorCount = _A8WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 8, 1, 9),
    _A8WarningErrorCount_Type()
)
a8WarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8WarningErrorCount.setStatus("mandatory")
_TFruTable_Object = MibTable
tFruTable = _TFruTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tFruTable.setStatus("mandatory")
_EFruTable_Object = MibTableRow
eFruTable = _EFruTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1)
)
eFruTable.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9FruIndex"),
)
if mibBuilder.loadTexts:
    eFruTable.setStatus("mandatory")
_A9FruIndex_Type = DmiInteger
_A9FruIndex_Object = MibTableColumn
a9FruIndex = _A9FruIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 1),
    _A9FruIndex_Type()
)
a9FruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9FruIndex.setStatus("mandatory")
_A9DeviceGroupIndex_Type = DmiInteger
_A9DeviceGroupIndex_Object = MibTableColumn
a9DeviceGroupIndex = _A9DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 2),
    _A9DeviceGroupIndex_Type()
)
a9DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9DeviceGroupIndex.setStatus("mandatory")
_A9Description_Type = DmiDisplaystring
_A9Description_Object = MibTableColumn
a9Description = _A9Description_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 3),
    _A9Description_Type()
)
a9Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Description.setStatus("mandatory")
_A9Manufacturer_Type = DmiDisplaystring
_A9Manufacturer_Object = MibTableColumn
a9Manufacturer = _A9Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 4),
    _A9Manufacturer_Type()
)
a9Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Manufacturer.setStatus("mandatory")
_A9Model_Type = DmiDisplaystring
_A9Model_Object = MibTableColumn
a9Model = _A9Model_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 5),
    _A9Model_Type()
)
a9Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9Model.setStatus("mandatory")
_A9PartNumber_Type = DmiDisplaystring
_A9PartNumber_Object = MibTableColumn
a9PartNumber = _A9PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 6),
    _A9PartNumber_Type()
)
a9PartNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a9PartNumber.setStatus("mandatory")
_A9FruSerialNumber_Type = DmiDisplaystring
_A9FruSerialNumber_Object = MibTableColumn
a9FruSerialNumber = _A9FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 7),
    _A9FruSerialNumber_Type()
)
a9FruSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a9FruSerialNumber.setStatus("mandatory")
_A9RevisionLevel_Type = DmiDisplaystring
_A9RevisionLevel_Object = MibTableColumn
a9RevisionLevel = _A9RevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 8),
    _A9RevisionLevel_Type()
)
a9RevisionLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a9RevisionLevel.setStatus("mandatory")
_A9WarrantyStartDate_Type = DmiDateX
_A9WarrantyStartDate_Object = MibTableColumn
a9WarrantyStartDate = _A9WarrantyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 9),
    _A9WarrantyStartDate_Type()
)
a9WarrantyStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9WarrantyStartDate.setStatus("mandatory")
_A9WarrantyDuration_Type = DmiInteger
_A9WarrantyDuration_Object = MibTableColumn
a9WarrantyDuration = _A9WarrantyDuration_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 10),
    _A9WarrantyDuration_Type()
)
a9WarrantyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9WarrantyDuration.setStatus("mandatory")
_A9SupportPhoneNumber_Type = DmiDisplaystring
_A9SupportPhoneNumber_Object = MibTableColumn
a9SupportPhoneNumber = _A9SupportPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9, 1, 11),
    _A9SupportPhoneNumber_Type()
)
a9SupportPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9SupportPhoneNumber.setStatus("mandatory")
_TBootRomConfiguration_Object = MibTable
tBootRomConfiguration = _TBootRomConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tBootRomConfiguration.setStatus("mandatory")
_EBootRomConfiguration_Object = MibTableRow
eBootRomConfiguration = _EBootRomConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 10, 1)
)
eBootRomConfiguration.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eBootRomConfiguration.setStatus("mandatory")
_A10BootRomDescription_Type = DmiDisplaystring
_A10BootRomDescription_Object = MibTableColumn
a10BootRomDescription = _A10BootRomDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 10, 1, 1),
    _A10BootRomDescription_Type()
)
a10BootRomDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10BootRomDescription.setStatus("mandatory")
_A10BootRomVersion_Type = DmiDisplaystring
_A10BootRomVersion_Object = MibTableColumn
a10BootRomVersion = _A10BootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 10, 1, 2),
    _A10BootRomVersion_Type()
)
a10BootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10BootRomVersion.setStatus("mandatory")


class _A10RemoteBootProtocolType_Type(Integer32):
    """Custom type a10RemoteBootProtocolType based on Integer32"""
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
        *(("vBootp", 4),
          ("vDecMop", 5),
          ("vNativeNetware", 6),
          ("vNone", 2),
          ("vOther", 1),
          ("vRpl", 3))
    )


_A10RemoteBootProtocolType_Type.__name__ = "Integer32"
_A10RemoteBootProtocolType_Object = MibTableColumn
a10RemoteBootProtocolType = _A10RemoteBootProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 10, 1, 3),
    _A10RemoteBootProtocolType_Type()
)
a10RemoteBootProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10RemoteBootProtocolType.setStatus("mandatory")
_A10RemoteBootProtocolVersion_Type = DmiDisplaystring
_A10RemoteBootProtocolVersion_Object = MibTableColumn
a10RemoteBootProtocolVersion = _A10RemoteBootProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 10, 1, 4),
    _A10RemoteBootProtocolVersion_Type()
)
a10RemoteBootProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10RemoteBootProtocolVersion.setStatus("mandatory")
_TBootRomCapabilities_Object = MibTable
tBootRomCapabilities = _TBootRomCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tBootRomCapabilities.setStatus("mandatory")
_EBootRomCapabilities_Object = MibTableRow
eBootRomCapabilities = _EBootRomCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 11, 1)
)
eBootRomCapabilities.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a11CapabilityIndex"),
)
if mibBuilder.loadTexts:
    eBootRomCapabilities.setStatus("mandatory")
_A11CapabilityIndex_Type = DmiInteger
_A11CapabilityIndex_Object = MibTableColumn
a11CapabilityIndex = _A11CapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 11, 1, 1),
    _A11CapabilityIndex_Type()
)
a11CapabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11CapabilityIndex.setStatus("mandatory")
_A11CapabilityDescription_Type = DmiDisplaystring
_A11CapabilityDescription_Object = MibTableColumn
a11CapabilityDescription = _A11CapabilityDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 11, 1, 2),
    _A11CapabilityDescription_Type()
)
a11CapabilityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11CapabilityDescription.setStatus("mandatory")
_A11CapabilityStatus_Type = DmiDisplaystring
_A11CapabilityStatus_Object = MibTableColumn
a11CapabilityStatus = _A11CapabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 11, 1, 3),
    _A11CapabilityStatus_Type()
)
a11CapabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11CapabilityStatus.setStatus("mandatory")
_TIntellanadapterextensionsgroup_Object = MibTable
tIntellanadapterextensionsgroup = _TIntellanadapterextensionsgroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tIntellanadapterextensionsgroup.setStatus("mandatory")
_EIntellanadapterextensionsgroup_Object = MibTableRow
eIntellanadapterextensionsgroup = _EIntellanadapterextensionsgroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 12, 1)
)
eIntellanadapterextensionsgroup.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eIntellanadapterextensionsgroup.setStatus("mandatory")
_A12DriverFilename_Type = DmiDisplaystring
_A12DriverFilename_Object = MibTableColumn
a12DriverFilename = _A12DriverFilename_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 12, 1, 1),
    _A12DriverFilename_Type()
)
a12DriverFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12DriverFilename.setStatus("mandatory")
_A12DriverDate_Type = DmiDateX
_A12DriverDate_Object = MibTableColumn
a12DriverDate = _A12DriverDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 12, 1, 2),
    _A12DriverDate_Type()
)
a12DriverDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12DriverDate.setStatus("mandatory")
_A12MifAndInstrumentationFilename_Type = DmiDisplaystring
_A12MifAndInstrumentationFilename_Object = MibTableColumn
a12MifAndInstrumentationFilename = _A12MifAndInstrumentationFilename_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 12, 1, 3),
    _A12MifAndInstrumentationFilename_Type()
)
a12MifAndInstrumentationFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12MifAndInstrumentationFilename.setStatus("mandatory")
_A12InstrumentationVersion_Type = DmiDisplaystring
_A12InstrumentationVersion_Object = MibTableColumn
a12InstrumentationVersion = _A12InstrumentationVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 12, 1, 4),
    _A12InstrumentationVersion_Type()
)
a12InstrumentationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12InstrumentationVersion.setStatus("mandatory")
_A12MifVersion_Type = DmiDisplaystring
_A12MifVersion_Object = MibTableColumn
a12MifVersion = _A12MifVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 12, 1, 5),
    _A12MifVersion_Type()
)
a12MifVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12MifVersion.setStatus("mandatory")
_TIndication_control_group_Object = MibTable
tIndication_control_group = _TIndication_control_group_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151)
)
if mibBuilder.loadTexts:
    tIndication_control_group.setStatus("mandatory")
_EIndication_control_group_Object = MibTableRow
eIndication_control_group = _EIndication_control_group_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1)
)
eIndication_control_group.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a151PortIndex"),
)
if mibBuilder.loadTexts:
    eIndication_control_group.setStatus("mandatory")
_A151PortIndex_Type = DmiInteger
_A151PortIndex_Object = MibTableColumn
a151PortIndex = _A151PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 1),
    _A151PortIndex_Type()
)
a151PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a151PortIndex.setStatus("mandatory")


class _A151IndicationEnable_Type(Integer32):
    """Custom type a151IndicationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A151IndicationEnable_Type.__name__ = "Integer32"
_A151IndicationEnable_Object = MibTableColumn
a151IndicationEnable = _A151IndicationEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 2),
    _A151IndicationEnable_Type()
)
a151IndicationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151IndicationEnable.setStatus("mandatory")


class _A151TotalTransmitIndicationEnable_Type(Integer32):
    """Custom type a151TotalTransmitIndicationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A151TotalTransmitIndicationEnable_Type.__name__ = "Integer32"
_A151TotalTransmitIndicationEnable_Object = MibTableColumn
a151TotalTransmitIndicationEnable = _A151TotalTransmitIndicationEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 3),
    _A151TotalTransmitIndicationEnable_Type()
)
a151TotalTransmitIndicationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalTransmitIndicationEnable.setStatus("mandatory")
_A151TotalTransmitErrorsThreshold_Type = DmiCounter64X
_A151TotalTransmitErrorsThreshold_Object = MibTableColumn
a151TotalTransmitErrorsThreshold = _A151TotalTransmitErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 4),
    _A151TotalTransmitErrorsThreshold_Type()
)
a151TotalTransmitErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalTransmitErrorsThreshold.setStatus("mandatory")


class _A151TotalReceiveIndicationEnable_Type(Integer32):
    """Custom type a151TotalReceiveIndicationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A151TotalReceiveIndicationEnable_Type.__name__ = "Integer32"
_A151TotalReceiveIndicationEnable_Object = MibTableColumn
a151TotalReceiveIndicationEnable = _A151TotalReceiveIndicationEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 5),
    _A151TotalReceiveIndicationEnable_Type()
)
a151TotalReceiveIndicationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalReceiveIndicationEnable.setStatus("mandatory")
_A151TotalReceiveErrorsThreshold_Type = DmiCounter64X
_A151TotalReceiveErrorsThreshold_Object = MibTableColumn
a151TotalReceiveErrorsThreshold = _A151TotalReceiveErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 6),
    _A151TotalReceiveErrorsThreshold_Type()
)
a151TotalReceiveErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalReceiveErrorsThreshold.setStatus("mandatory")


class _A151TotalHostIndicationEnable_Type(Integer32):
    """Custom type a151TotalHostIndicationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A151TotalHostIndicationEnable_Type.__name__ = "Integer32"
_A151TotalHostIndicationEnable_Object = MibTableColumn
a151TotalHostIndicationEnable = _A151TotalHostIndicationEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 7),
    _A151TotalHostIndicationEnable_Type()
)
a151TotalHostIndicationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalHostIndicationEnable.setStatus("mandatory")
_A151TotalHostErrorsThreshold_Type = DmiCounter64X
_A151TotalHostErrorsThreshold_Object = MibTableColumn
a151TotalHostErrorsThreshold = _A151TotalHostErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 8),
    _A151TotalHostErrorsThreshold_Type()
)
a151TotalHostErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalHostErrorsThreshold.setStatus("mandatory")


class _A151TotalWireIndicationEnable_Type(Integer32):
    """Custom type a151TotalWireIndicationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A151TotalWireIndicationEnable_Type.__name__ = "Integer32"
_A151TotalWireIndicationEnable_Object = MibTableColumn
a151TotalWireIndicationEnable = _A151TotalWireIndicationEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 9),
    _A151TotalWireIndicationEnable_Type()
)
a151TotalWireIndicationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalWireIndicationEnable.setStatus("mandatory")
_A151TotalWireErrorsThreshold_Type = DmiCounter64X
_A151TotalWireErrorsThreshold_Object = MibTableColumn
a151TotalWireErrorsThreshold = _A151TotalWireErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 151, 1, 10),
    _A151TotalWireErrorsThreshold_Type()
)
a151TotalWireErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a151TotalWireErrorsThreshold.setStatus("mandatory")
_TErrorcontrol_Object = MibTable
tErrorcontrol = _TErrorcontrol_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152)
)
if mibBuilder.loadTexts:
    tErrorcontrol.setStatus("mandatory")
_EErrorcontrol_Object = MibTableRow
eErrorcontrol = _EErrorcontrol_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152, 1)
)
eErrorcontrol.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a152Selfid"),
)
if mibBuilder.loadTexts:
    eErrorcontrol.setStatus("mandatory")
_A152Selfid_Type = DmiInteger
_A152Selfid_Object = MibTableColumn
a152Selfid = _A152Selfid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152, 1, 1),
    _A152Selfid_Type()
)
a152Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a152Selfid.setStatus("mandatory")
_A152Fatalcount_Type = DmiCounter
_A152Fatalcount_Object = MibTableColumn
a152Fatalcount = _A152Fatalcount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152, 1, 2),
    _A152Fatalcount_Type()
)
a152Fatalcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a152Fatalcount.setStatus("mandatory")
_A152Majorcount_Type = DmiCounter
_A152Majorcount_Object = MibTableColumn
a152Majorcount = _A152Majorcount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152, 1, 3),
    _A152Majorcount_Type()
)
a152Majorcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a152Majorcount.setStatus("mandatory")
_A152Warningcount_Type = DmiCounter
_A152Warningcount_Object = MibTableColumn
a152Warningcount = _A152Warningcount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152, 1, 4),
    _A152Warningcount_Type()
)
a152Warningcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a152Warningcount.setStatus("mandatory")


class _A152Errstatus_Type(Integer32):
    """Custom type a152Errstatus based on Integer32"""
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
        *(("vFatal", 3),
          ("vMajor", 2),
          ("vOk", 0),
          ("vUnknown", 4),
          ("vWarning1", 1))
    )


_A152Errstatus_Type.__name__ = "Integer32"
_A152Errstatus_Object = MibTableColumn
a152Errstatus = _A152Errstatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152, 1, 5),
    _A152Errstatus_Type()
)
a152Errstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a152Errstatus.setStatus("mandatory")


class _A152Errstatustype_Type(Integer32):
    """Custom type a152Errstatustype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDiagnosticTest", 2),
          ("vPost", 0),
          ("vRuntime", 1))
    )


_A152Errstatustype_Type.__name__ = "Integer32"
_A152Errstatustype_Object = MibTableColumn
a152Errstatustype = _A152Errstatustype_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 152, 1, 6),
    _A152Errstatustype_Type()
)
a152Errstatustype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a152Errstatustype.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 153)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 153, 1)
)
eMiftomib.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A153MibName_Type = DmiDisplaystring
_A153MibName_Object = MibTableColumn
a153MibName = _A153MibName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 153, 1, 1),
    _A153MibName_Type()
)
a153MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a153MibName.setStatus("mandatory")
_A153MibOid_Type = DmiDisplaystring
_A153MibOid_Object = MibTableColumn
a153MibOid = _A153MibOid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 153, 1, 2),
    _A153MibOid_Type()
)
a153MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a153MibOid.setStatus("mandatory")
_A153DisableTrap_Type = DmiInteger
_A153DisableTrap_Object = MibTableColumn
a153DisableTrap = _A153DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 153, 1, 3),
    _A153DisableTrap_Type()
)
a153DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a153DisableTrap.setStatus("mandatory")
_TTrapGroup_Object = MibTable
tTrapGroup = _TTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999)
)
if mibBuilder.loadTexts:
    tTrapGroup.setStatus("mandatory")
_ETrapGroup_Object = MibTableRow
eTrapGroup = _ETrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1)
)
eTrapGroup.setIndexNames(
    (0, "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eTrapGroup.setStatus("mandatory")
_A9999ErrorTime_Type = DisplayString
_A9999ErrorTime_Object = MibTableColumn
a9999ErrorTime = _A9999ErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 1),
    _A9999ErrorTime_Type()
)
a9999ErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorTime.setStatus("mandatory")
_A9999ErrorStatus_Type = DmiInteger
_A9999ErrorStatus_Object = MibTableColumn
a9999ErrorStatus = _A9999ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 2),
    _A9999ErrorStatus_Type()
)
a9999ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorStatus.setStatus("mandatory")
_A9999ErrorGroupId_Type = DmiInteger
_A9999ErrorGroupId_Object = MibTableColumn
a9999ErrorGroupId = _A9999ErrorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 3),
    _A9999ErrorGroupId_Type()
)
a9999ErrorGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorGroupId.setStatus("mandatory")
_A9999ErrorInstanceId_Type = DmiInteger
_A9999ErrorInstanceId_Object = MibTableColumn
a9999ErrorInstanceId = _A9999ErrorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 4),
    _A9999ErrorInstanceId_Type()
)
a9999ErrorInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorInstanceId.setStatus("mandatory")
_A9999ComponentId_Type = DmiInteger
_A9999ComponentId_Object = MibTableColumn
a9999ComponentId = _A9999ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 5),
    _A9999ComponentId_Type()
)
a9999ComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ComponentId.setStatus("mandatory")
_A9999GroupId_Type = DmiInteger
_A9999GroupId_Object = MibTableColumn
a9999GroupId = _A9999GroupId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 6),
    _A9999GroupId_Type()
)
a9999GroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999GroupId.setStatus("mandatory")
_A9999InstanceId_Type = DmiInteger
_A9999InstanceId_Object = MibTableColumn
a9999InstanceId = _A9999InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 7),
    _A9999InstanceId_Type()
)
a9999InstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999InstanceId.setStatus("mandatory")
_A9999VendorCode1_Type = DmiInteger
_A9999VendorCode1_Object = MibTableColumn
a9999VendorCode1 = _A9999VendorCode1_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 8),
    _A9999VendorCode1_Type()
)
a9999VendorCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode1.setStatus("mandatory")
_A9999VendorCode2_Type = DmiInteger
_A9999VendorCode2_Object = MibTableColumn
a9999VendorCode2 = _A9999VendorCode2_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 9),
    _A9999VendorCode2_Type()
)
a9999VendorCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode2.setStatus("mandatory")
_A9999VendorText_Type = OctetString
_A9999VendorText_Object = MibTableColumn
a9999VendorText = _A9999VendorText_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 10),
    _A9999VendorText_Type()
)
a9999VendorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorText.setStatus("mandatory")
_A9999ParentGroupId_Type = DmiInteger
_A9999ParentGroupId_Object = MibTableColumn
a9999ParentGroupId = _A9999ParentGroupId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 11),
    _A9999ParentGroupId_Type()
)
a9999ParentGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentGroupId.setStatus("mandatory")
_A9999ParentInstanceId_Type = DmiInteger
_A9999ParentInstanceId_Object = MibTableColumn
a9999ParentInstanceId = _A9999ParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 12),
    _A9999ParentInstanceId_Type()
)
a9999ParentInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentInstanceId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

e100bEventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 6, 4, 1, 1, 9999, 1, 0, 1)
)
e100bEventError.setObjects(
      *(("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999ErrorTime"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999ErrorStatus"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999ErrorGroupId"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999ErrorInstanceId"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999ComponentId"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999GroupId"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999InstanceId"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999VendorCode1"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999VendorCode2"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999VendorText"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999ParentGroupId"),
        ("INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB", "a9999ParentInstanceId"))
)
if mibBuilder.loadTexts:
    e100bEventError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELETHEREXPRESSTMPRO100BLANADAPTER-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiCounter64X": DmiCounter64X,
       "DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "intel": intel,
       "products": products,
       "server-products": server_products,
       "nic": nic,
       "e100b": e100b,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tSystemResourcesDescription": tSystemResourcesDescription,
       "eSystemResourcesDescription": eSystemResourcesDescription,
       "a2DeviceCount": a2DeviceCount,
       "a2SystemResourceCount": a2SystemResourceCount,
       "tSystemResources": tSystemResources,
       "eSystemResources": eSystemResources,
       "a3DeviceId": a3DeviceId,
       "a3ResourceNumber": a3ResourceNumber,
       "a3ResourceType": a3ResourceType,
       "a3ResourceBase": a3ResourceBase,
       "a3ResourceSize": a3ResourceSize,
       "a3ResourceFlags": a3ResourceFlags,
       "a3GroupId": a3GroupId,
       "tNetworkAdapter802PortGroup": tNetworkAdapter802PortGroup,
       "eNetworkAdapter802PortGroup": eNetworkAdapter802PortGroup,
       "a4PortIndex": a4PortIndex,
       "a4PermanentNetworkAddress": a4PermanentNetworkAddress,
       "a4CurrentNetworkAddress": a4CurrentNetworkAddress,
       "a4ConnectorType": a4ConnectorType,
       "a4DataRate": a4DataRate,
       "a4TotalPacketsTransmitted": a4TotalPacketsTransmitted,
       "a4TotalBytesTransmitted": a4TotalBytesTransmitted,
       "a4TotalPacketsReceived": a4TotalPacketsReceived,
       "a4TotalBytesReceived": a4TotalBytesReceived,
       "a4TotalTransmitErrors": a4TotalTransmitErrors,
       "a4TotalReceiveErrors": a4TotalReceiveErrors,
       "a4TotalHostErrors": a4TotalHostErrors,
       "a4TotalWireErrors": a4TotalWireErrors,
       "t802AlternateAddressGroup": t802AlternateAddressGroup,
       "e802AlternateAddressGroup": e802AlternateAddressGroup,
       "a5AlternateAddressIndex": a5AlternateAddressIndex,
       "a5PortIndex": a5PortIndex,
       "a5AddressType": a5AddressType,
       "a5AlternateAddress": a5AlternateAddress,
       "tNetworkAdapterDriverGroup": tNetworkAdapterDriverGroup,
       "eNetworkAdapterDriverGroup": eNetworkAdapterDriverGroup,
       "a6DriverIndex": a6DriverIndex,
       "a6DriverSoftwareName": a6DriverSoftwareName,
       "a6DriverSoftwareVersion": a6DriverSoftwareVersion,
       "a6DriverSoftwareDescription": a6DriverSoftwareDescription,
       "a6DriverSize": a6DriverSize,
       "a6DriverInterfaceType": a6DriverInterfaceType,
       "a6DriverInterfaceVersion": a6DriverInterfaceVersion,
       "a6DriverInterfaceDescription": a6DriverInterfaceDescription,
       "tNetworkAdapterHardwareGroup": tNetworkAdapterHardwareGroup,
       "eNetworkAdapterHardwareGroup": eNetworkAdapterHardwareGroup,
       "a7NetworkTopology": a7NetworkTopology,
       "a7TransmissionCapability": a7TransmissionCapability,
       "a7NetworkAdapterRamSize": a7NetworkAdapterRamSize,
       "a7BusType": a7BusType,
       "a7BusWidth": a7BusWidth,
       "tOperationalState": tOperationalState,
       "eOperationalState": eOperationalState,
       "a8OperationalStateInstanceIndex": a8OperationalStateInstanceIndex,
       "a8DeviceGroupIndex": a8DeviceGroupIndex,
       "a8OperationalStatus": a8OperationalStatus,
       "a8UsageState": a8UsageState,
       "a8AvailabilityStatus": a8AvailabilityStatus,
       "a8AdministrativeState": a8AdministrativeState,
       "a8FatalErrorCount": a8FatalErrorCount,
       "a8MajorErrorCount": a8MajorErrorCount,
       "a8WarningErrorCount": a8WarningErrorCount,
       "tFruTable": tFruTable,
       "eFruTable": eFruTable,
       "a9FruIndex": a9FruIndex,
       "a9DeviceGroupIndex": a9DeviceGroupIndex,
       "a9Description": a9Description,
       "a9Manufacturer": a9Manufacturer,
       "a9Model": a9Model,
       "a9PartNumber": a9PartNumber,
       "a9FruSerialNumber": a9FruSerialNumber,
       "a9RevisionLevel": a9RevisionLevel,
       "a9WarrantyStartDate": a9WarrantyStartDate,
       "a9WarrantyDuration": a9WarrantyDuration,
       "a9SupportPhoneNumber": a9SupportPhoneNumber,
       "tBootRomConfiguration": tBootRomConfiguration,
       "eBootRomConfiguration": eBootRomConfiguration,
       "a10BootRomDescription": a10BootRomDescription,
       "a10BootRomVersion": a10BootRomVersion,
       "a10RemoteBootProtocolType": a10RemoteBootProtocolType,
       "a10RemoteBootProtocolVersion": a10RemoteBootProtocolVersion,
       "tBootRomCapabilities": tBootRomCapabilities,
       "eBootRomCapabilities": eBootRomCapabilities,
       "a11CapabilityIndex": a11CapabilityIndex,
       "a11CapabilityDescription": a11CapabilityDescription,
       "a11CapabilityStatus": a11CapabilityStatus,
       "tIntellanadapterextensionsgroup": tIntellanadapterextensionsgroup,
       "eIntellanadapterextensionsgroup": eIntellanadapterextensionsgroup,
       "a12DriverFilename": a12DriverFilename,
       "a12DriverDate": a12DriverDate,
       "a12MifAndInstrumentationFilename": a12MifAndInstrumentationFilename,
       "a12InstrumentationVersion": a12InstrumentationVersion,
       "a12MifVersion": a12MifVersion,
       "tIndication_control_group": tIndication_control_group,
       "eIndication_control_group": eIndication_control_group,
       "a151PortIndex": a151PortIndex,
       "a151IndicationEnable": a151IndicationEnable,
       "a151TotalTransmitIndicationEnable": a151TotalTransmitIndicationEnable,
       "a151TotalTransmitErrorsThreshold": a151TotalTransmitErrorsThreshold,
       "a151TotalReceiveIndicationEnable": a151TotalReceiveIndicationEnable,
       "a151TotalReceiveErrorsThreshold": a151TotalReceiveErrorsThreshold,
       "a151TotalHostIndicationEnable": a151TotalHostIndicationEnable,
       "a151TotalHostErrorsThreshold": a151TotalHostErrorsThreshold,
       "a151TotalWireIndicationEnable": a151TotalWireIndicationEnable,
       "a151TotalWireErrorsThreshold": a151TotalWireErrorsThreshold,
       "tErrorcontrol": tErrorcontrol,
       "eErrorcontrol": eErrorcontrol,
       "a152Selfid": a152Selfid,
       "a152Fatalcount": a152Fatalcount,
       "a152Majorcount": a152Majorcount,
       "a152Warningcount": a152Warningcount,
       "a152Errstatus": a152Errstatus,
       "a152Errstatustype": a152Errstatustype,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a153MibName": a153MibName,
       "a153MibOid": a153MibOid,
       "a153DisableTrap": a153DisableTrap,
       "tTrapGroup": tTrapGroup,
       "eTrapGroup": eTrapGroup,
       "e100bEventError": e100bEventError,
       "a9999ErrorTime": a9999ErrorTime,
       "a9999ErrorStatus": a9999ErrorStatus,
       "a9999ErrorGroupId": a9999ErrorGroupId,
       "a9999ErrorInstanceId": a9999ErrorInstanceId,
       "a9999ComponentId": a9999ComponentId,
       "a9999GroupId": a9999GroupId,
       "a9999InstanceId": a9999InstanceId,
       "a9999VendorCode1": a9999VendorCode1,
       "a9999VendorCode2": a9999VendorCode2,
       "a9999VendorText": a9999VendorText,
       "a9999ParentGroupId": a9999ParentGroupId,
       "a9999ParentInstanceId": a9999ParentInstanceId}
)
