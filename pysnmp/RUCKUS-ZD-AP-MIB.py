# SNMP MIB module (RUCKUS-ZD-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ZD-AP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:53 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusZDWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusZDWLANModule")

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
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusZDAPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDAPObjects_ObjectIdentity = ObjectIdentity
ruckusZDAPObjects = _RuckusZDAPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1)
)
_RuckusZDAPConfig_ObjectIdentity = ObjectIdentity
ruckusZDAPConfig = _RuckusZDAPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1)
)
_RuckusZDAPConfigTable_Object = MibTable
ruckusZDAPConfigTable = _RuckusZDAPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusZDAPConfigTable.setStatus("current")
_RuckusZDAPConfigEntry_Object = MibTableRow
ruckusZDAPConfigEntry = _RuckusZDAPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1)
)
ruckusZDAPConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-AP-MIB", "ruckusZDAPConfigID"),
)
if mibBuilder.loadTexts:
    ruckusZDAPConfigEntry.setStatus("current")


class _RuckusZDAPConfigID_Type(Integer32):
    """Custom type ruckusZDAPConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_RuckusZDAPConfigID_Type.__name__ = "Integer32"
_RuckusZDAPConfigID_Object = MibTableColumn
ruckusZDAPConfigID = _RuckusZDAPConfigID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 1),
    _RuckusZDAPConfigID_Type()
)
ruckusZDAPConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDAPConfigID.setStatus("current")
_RuckusZDAPConfigMacAddress_Type = MacAddress
_RuckusZDAPConfigMacAddress_Object = MibTableColumn
ruckusZDAPConfigMacAddress = _RuckusZDAPConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 2),
    _RuckusZDAPConfigMacAddress_Type()
)
ruckusZDAPConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDAPConfigMacAddress.setStatus("current")


class _RuckusZDAPConfigAPModel_Type(OctetString):
    """Custom type ruckusZDAPConfigAPModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDAPConfigAPModel_Type.__name__ = "OctetString"
_RuckusZDAPConfigAPModel_Object = MibTableColumn
ruckusZDAPConfigAPModel = _RuckusZDAPConfigAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 4),
    _RuckusZDAPConfigAPModel_Type()
)
ruckusZDAPConfigAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDAPConfigAPModel.setStatus("current")


class _RuckusZDAPConfigDeviceName_Type(OctetString):
    """Custom type ruckusZDAPConfigDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDAPConfigDeviceName_Type.__name__ = "OctetString"
_RuckusZDAPConfigDeviceName_Object = MibTableColumn
ruckusZDAPConfigDeviceName = _RuckusZDAPConfigDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 5),
    _RuckusZDAPConfigDeviceName_Type()
)
ruckusZDAPConfigDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigDeviceName.setStatus("current")


class _RuckusZDAPConfigDescription_Type(OctetString):
    """Custom type ruckusZDAPConfigDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDAPConfigDescription_Type.__name__ = "OctetString"
_RuckusZDAPConfigDescription_Object = MibTableColumn
ruckusZDAPConfigDescription = _RuckusZDAPConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 6),
    _RuckusZDAPConfigDescription_Type()
)
ruckusZDAPConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigDescription.setStatus("current")


class _RuckusZDAPConfigLocation_Type(OctetString):
    """Custom type ruckusZDAPConfigLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDAPConfigLocation_Type.__name__ = "OctetString"
_RuckusZDAPConfigLocation_Object = MibTableColumn
ruckusZDAPConfigLocation = _RuckusZDAPConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 7),
    _RuckusZDAPConfigLocation_Type()
)
ruckusZDAPConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigLocation.setStatus("current")


class _RuckusZDAPConfigGpsLatitude_Type(OctetString):
    """Custom type ruckusZDAPConfigGpsLatitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RuckusZDAPConfigGpsLatitude_Type.__name__ = "OctetString"
_RuckusZDAPConfigGpsLatitude_Object = MibTableColumn
ruckusZDAPConfigGpsLatitude = _RuckusZDAPConfigGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 10),
    _RuckusZDAPConfigGpsLatitude_Type()
)
ruckusZDAPConfigGpsLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigGpsLatitude.setStatus("current")


class _RuckusZDAPConfigGpsLongitude_Type(OctetString):
    """Custom type ruckusZDAPConfigGpsLongitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RuckusZDAPConfigGpsLongitude_Type.__name__ = "OctetString"
_RuckusZDAPConfigGpsLongitude_Object = MibTableColumn
ruckusZDAPConfigGpsLongitude = _RuckusZDAPConfigGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 11),
    _RuckusZDAPConfigGpsLongitude_Type()
)
ruckusZDAPConfigGpsLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigGpsLongitude.setStatus("current")


class _RuckusZDAPConfigIPVersion_Type(Integer32):
    """Custom type ruckusZDAPConfigIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualstack", 3),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_RuckusZDAPConfigIPVersion_Type.__name__ = "Integer32"
_RuckusZDAPConfigIPVersion_Object = MibTableColumn
ruckusZDAPConfigIPVersion = _RuckusZDAPConfigIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 14),
    _RuckusZDAPConfigIPVersion_Type()
)
ruckusZDAPConfigIPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigIPVersion.setStatus("current")


class _RuckusZDAPConfigIpAddressSettingMode_Type(Integer32):
    """Custom type ruckusZDAPConfigIpAddressSettingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin-by-ap", 3),
          ("admin-by-dhcp", 2),
          ("admin-by-zd", 1))
    )


_RuckusZDAPConfigIpAddressSettingMode_Type.__name__ = "Integer32"
_RuckusZDAPConfigIpAddressSettingMode_Object = MibTableColumn
ruckusZDAPConfigIpAddressSettingMode = _RuckusZDAPConfigIpAddressSettingMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 15),
    _RuckusZDAPConfigIpAddressSettingMode_Type()
)
ruckusZDAPConfigIpAddressSettingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigIpAddressSettingMode.setStatus("current")
_RuckusZDAPConfigIpAddress_Type = IpAddress
_RuckusZDAPConfigIpAddress_Object = MibTableColumn
ruckusZDAPConfigIpAddress = _RuckusZDAPConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 16),
    _RuckusZDAPConfigIpAddress_Type()
)
ruckusZDAPConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigIpAddress.setStatus("current")
_RuckusZDAPConfigIpAddressMask_Type = IpAddress
_RuckusZDAPConfigIpAddressMask_Object = MibTableColumn
ruckusZDAPConfigIpAddressMask = _RuckusZDAPConfigIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 17),
    _RuckusZDAPConfigIpAddressMask_Type()
)
ruckusZDAPConfigIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigIpAddressMask.setStatus("current")
_RuckusZDAPConfigGatewayIpAddress_Type = IpAddress
_RuckusZDAPConfigGatewayIpAddress_Object = MibTableColumn
ruckusZDAPConfigGatewayIpAddress = _RuckusZDAPConfigGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 20),
    _RuckusZDAPConfigGatewayIpAddress_Type()
)
ruckusZDAPConfigGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigGatewayIpAddress.setStatus("current")


class _RuckusZDAPConfigIpV6AddressSettingMode_Type(Integer32):
    """Custom type ruckusZDAPConfigIpV6AddressSettingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin-by-ap", 3),
          ("admin-by-autoconfig", 2),
          ("admin-by-zd", 1))
    )


_RuckusZDAPConfigIpV6AddressSettingMode_Type.__name__ = "Integer32"
_RuckusZDAPConfigIpV6AddressSettingMode_Object = MibTableColumn
ruckusZDAPConfigIpV6AddressSettingMode = _RuckusZDAPConfigIpV6AddressSettingMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 21),
    _RuckusZDAPConfigIpV6AddressSettingMode_Type()
)
ruckusZDAPConfigIpV6AddressSettingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigIpV6AddressSettingMode.setStatus("current")


class _RuckusZDAPConfigIpV6Address_Type(OctetString):
    """Custom type ruckusZDAPConfigIpV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDAPConfigIpV6Address_Type.__name__ = "OctetString"
_RuckusZDAPConfigIpV6Address_Object = MibTableColumn
ruckusZDAPConfigIpV6Address = _RuckusZDAPConfigIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 22),
    _RuckusZDAPConfigIpV6Address_Type()
)
ruckusZDAPConfigIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigIpV6Address.setStatus("current")


class _RuckusZDAPConfigIpV6PrefixLen_Type(Integer32):
    """Custom type ruckusZDAPConfigIpV6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_RuckusZDAPConfigIpV6PrefixLen_Type.__name__ = "Integer32"
_RuckusZDAPConfigIpV6PrefixLen_Object = MibTableColumn
ruckusZDAPConfigIpV6PrefixLen = _RuckusZDAPConfigIpV6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 23),
    _RuckusZDAPConfigIpV6PrefixLen_Type()
)
ruckusZDAPConfigIpV6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigIpV6PrefixLen.setStatus("current")


class _RuckusZDAPConfigGatewayIpV6Address_Type(OctetString):
    """Custom type ruckusZDAPConfigGatewayIpV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDAPConfigGatewayIpV6Address_Type.__name__ = "OctetString"
_RuckusZDAPConfigGatewayIpV6Address_Object = MibTableColumn
ruckusZDAPConfigGatewayIpV6Address = _RuckusZDAPConfigGatewayIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 24),
    _RuckusZDAPConfigGatewayIpV6Address_Type()
)
ruckusZDAPConfigGatewayIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigGatewayIpV6Address.setStatus("current")
_RuckusZDAPConfigPrimaryDnsIpAddress_Type = IpAddress
_RuckusZDAPConfigPrimaryDnsIpAddress_Object = MibTableColumn
ruckusZDAPConfigPrimaryDnsIpAddress = _RuckusZDAPConfigPrimaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 25),
    _RuckusZDAPConfigPrimaryDnsIpAddress_Type()
)
ruckusZDAPConfigPrimaryDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigPrimaryDnsIpAddress.setStatus("current")
_RuckusZDAPConfigSecondaryDnsIpAddress_Type = IpAddress
_RuckusZDAPConfigSecondaryDnsIpAddress_Object = MibTableColumn
ruckusZDAPConfigSecondaryDnsIpAddress = _RuckusZDAPConfigSecondaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 26),
    _RuckusZDAPConfigSecondaryDnsIpAddress_Type()
)
ruckusZDAPConfigSecondaryDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigSecondaryDnsIpAddress.setStatus("current")


class _RuckusZDAPConfigPrimaryDnsIpV6Address_Type(OctetString):
    """Custom type ruckusZDAPConfigPrimaryDnsIpV6Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDAPConfigPrimaryDnsIpV6Address_Type.__name__ = "OctetString"
_RuckusZDAPConfigPrimaryDnsIpV6Address_Object = MibTableColumn
ruckusZDAPConfigPrimaryDnsIpV6Address = _RuckusZDAPConfigPrimaryDnsIpV6Address_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 27),
    _RuckusZDAPConfigPrimaryDnsIpV6Address_Type()
)
ruckusZDAPConfigPrimaryDnsIpV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigPrimaryDnsIpV6Address.setStatus("current")


class _RuckusZDAPConfigSecondaryDnsV6IpAddress_Type(OctetString):
    """Custom type ruckusZDAPConfigSecondaryDnsV6IpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusZDAPConfigSecondaryDnsV6IpAddress_Type.__name__ = "OctetString"
_RuckusZDAPConfigSecondaryDnsV6IpAddress_Object = MibTableColumn
ruckusZDAPConfigSecondaryDnsV6IpAddress = _RuckusZDAPConfigSecondaryDnsV6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 28),
    _RuckusZDAPConfigSecondaryDnsV6IpAddress_Type()
)
ruckusZDAPConfigSecondaryDnsV6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigSecondaryDnsV6IpAddress.setStatus("current")


class _RuckusZDAPConfigRadioType_Type(Integer32):
    """Custom type ruckusZDAPConfigRadioType based on Integer32"""
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
        *(("ieee80211a", 3),
          ("ieee80211bg", 1),
          ("ieee80211n", 4),
          ("ieee80211na", 2),
          ("ieee80211ng", 5))
    )


_RuckusZDAPConfigRadioType_Type.__name__ = "Integer32"
_RuckusZDAPConfigRadioType_Object = MibTableColumn
ruckusZDAPConfigRadioType = _RuckusZDAPConfigRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 30),
    _RuckusZDAPConfigRadioType_Type()
)
ruckusZDAPConfigRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioType.setStatus("current")


class _RuckusZDAPConfigRadioChannel24_Type(Integer32):
    """Custom type ruckusZDAPConfigRadioChannel24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_RuckusZDAPConfigRadioChannel24_Type.__name__ = "Integer32"
_RuckusZDAPConfigRadioChannel24_Object = MibTableColumn
ruckusZDAPConfigRadioChannel24 = _RuckusZDAPConfigRadioChannel24_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 31),
    _RuckusZDAPConfigRadioChannel24_Type()
)
ruckusZDAPConfigRadioChannel24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioChannel24.setStatus("current")


class _RuckusZDAPConfigRadioTxPowerLevel24_Type(Integer32):
    """Custom type ruckusZDAPConfigRadioTxPowerLevel24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_RuckusZDAPConfigRadioTxPowerLevel24_Type.__name__ = "Integer32"
_RuckusZDAPConfigRadioTxPowerLevel24_Object = MibTableColumn
ruckusZDAPConfigRadioTxPowerLevel24 = _RuckusZDAPConfigRadioTxPowerLevel24_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 32),
    _RuckusZDAPConfigRadioTxPowerLevel24_Type()
)
ruckusZDAPConfigRadioTxPowerLevel24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioTxPowerLevel24.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioTxPowerLevel24.setUnits("dB")


class _RuckusZDAPConfigRadioWlanGroup24_Type(OctetString):
    """Custom type ruckusZDAPConfigRadioWlanGroup24 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuckusZDAPConfigRadioWlanGroup24_Type.__name__ = "OctetString"
_RuckusZDAPConfigRadioWlanGroup24_Object = MibTableColumn
ruckusZDAPConfigRadioWlanGroup24 = _RuckusZDAPConfigRadioWlanGroup24_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 33),
    _RuckusZDAPConfigRadioWlanGroup24_Type()
)
ruckusZDAPConfigRadioWlanGroup24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioWlanGroup24.setStatus("current")


class _RuckusZDAPConfigRadioEnableWlanService24_Type(Integer32):
    """Custom type ruckusZDAPConfigRadioEnableWlanService24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RuckusZDAPConfigRadioEnableWlanService24_Type.__name__ = "Integer32"
_RuckusZDAPConfigRadioEnableWlanService24_Object = MibTableColumn
ruckusZDAPConfigRadioEnableWlanService24 = _RuckusZDAPConfigRadioEnableWlanService24_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 34),
    _RuckusZDAPConfigRadioEnableWlanService24_Type()
)
ruckusZDAPConfigRadioEnableWlanService24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioEnableWlanService24.setStatus("current")


class _RuckusZDAPConfigRadioChannel5_Type(Integer32):
    """Custom type ruckusZDAPConfigRadioChannel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(36, 165),
    )


_RuckusZDAPConfigRadioChannel5_Type.__name__ = "Integer32"
_RuckusZDAPConfigRadioChannel5_Object = MibTableColumn
ruckusZDAPConfigRadioChannel5 = _RuckusZDAPConfigRadioChannel5_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 40),
    _RuckusZDAPConfigRadioChannel5_Type()
)
ruckusZDAPConfigRadioChannel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioChannel5.setStatus("current")


class _RuckusZDAPConfigRadioTxPowerLevel5_Type(Integer32):
    """Custom type ruckusZDAPConfigRadioTxPowerLevel5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_RuckusZDAPConfigRadioTxPowerLevel5_Type.__name__ = "Integer32"
_RuckusZDAPConfigRadioTxPowerLevel5_Object = MibTableColumn
ruckusZDAPConfigRadioTxPowerLevel5 = _RuckusZDAPConfigRadioTxPowerLevel5_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 41),
    _RuckusZDAPConfigRadioTxPowerLevel5_Type()
)
ruckusZDAPConfigRadioTxPowerLevel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioTxPowerLevel5.setStatus("current")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioTxPowerLevel5.setUnits("dB")


class _RuckusZDAPConfigRadioWlanGroup5_Type(OctetString):
    """Custom type ruckusZDAPConfigRadioWlanGroup5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RuckusZDAPConfigRadioWlanGroup5_Type.__name__ = "OctetString"
_RuckusZDAPConfigRadioWlanGroup5_Object = MibTableColumn
ruckusZDAPConfigRadioWlanGroup5 = _RuckusZDAPConfigRadioWlanGroup5_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 42),
    _RuckusZDAPConfigRadioWlanGroup5_Type()
)
ruckusZDAPConfigRadioWlanGroup5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioWlanGroup5.setStatus("current")


class _RuckusZDAPConfigRadioEnableWlanService5_Type(Integer32):
    """Custom type ruckusZDAPConfigRadioEnableWlanService5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RuckusZDAPConfigRadioEnableWlanService5_Type.__name__ = "Integer32"
_RuckusZDAPConfigRadioEnableWlanService5_Object = MibTableColumn
ruckusZDAPConfigRadioEnableWlanService5 = _RuckusZDAPConfigRadioEnableWlanService5_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 43),
    _RuckusZDAPConfigRadioEnableWlanService5_Type()
)
ruckusZDAPConfigRadioEnableWlanService5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRadioEnableWlanService5.setStatus("current")


class _RuckusZDAPConfigMeshConfigurationMode_Type(Integer32):
    """Custom type ruckusZDAPConfigMeshConfigurationMode based on Integer32"""
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
        *(("auto", 1),
          ("disabled", 4),
          ("mesh-ap", 3),
          ("root-ap", 2))
    )


_RuckusZDAPConfigMeshConfigurationMode_Type.__name__ = "Integer32"
_RuckusZDAPConfigMeshConfigurationMode_Object = MibTableColumn
ruckusZDAPConfigMeshConfigurationMode = _RuckusZDAPConfigMeshConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 50),
    _RuckusZDAPConfigMeshConfigurationMode_Type()
)
ruckusZDAPConfigMeshConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigMeshConfigurationMode.setStatus("current")


class _RuckusZDAPConfigUplinkSelectionMode_Type(Integer32):
    """Custom type ruckusZDAPConfigUplinkSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("smart", 1))
    )


_RuckusZDAPConfigUplinkSelectionMode_Type.__name__ = "Integer32"
_RuckusZDAPConfigUplinkSelectionMode_Object = MibTableColumn
ruckusZDAPConfigUplinkSelectionMode = _RuckusZDAPConfigUplinkSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 51),
    _RuckusZDAPConfigUplinkSelectionMode_Type()
)
ruckusZDAPConfigUplinkSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigUplinkSelectionMode.setStatus("current")


class _RuckusZDAPConfigApproveMode_Type(Integer32):
    """Custom type ruckusZDAPConfigApproveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("approved", 1),
          ("not-approved", 2))
    )


_RuckusZDAPConfigApproveMode_Type.__name__ = "Integer32"
_RuckusZDAPConfigApproveMode_Object = MibTableColumn
ruckusZDAPConfigApproveMode = _RuckusZDAPConfigApproveMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 52),
    _RuckusZDAPConfigApproveMode_Type()
)
ruckusZDAPConfigApproveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigApproveMode.setStatus("current")


class _RuckusZDAPConfigManagementAdmin_Type(Integer32):
    """Custom type ruckusZDAPConfigManagementAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("associated", 2),
          ("delete", 1))
    )


_RuckusZDAPConfigManagementAdmin_Type.__name__ = "Integer32"
_RuckusZDAPConfigManagementAdmin_Object = MibTableColumn
ruckusZDAPConfigManagementAdmin = _RuckusZDAPConfigManagementAdmin_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 60),
    _RuckusZDAPConfigManagementAdmin_Type()
)
ruckusZDAPConfigManagementAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigManagementAdmin.setStatus("current")


class _RuckusZDAPConfigRebootNow_Type(Integer32):
    """Custom type ruckusZDAPConfigRebootNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_RuckusZDAPConfigRebootNow_Type.__name__ = "Integer32"
_RuckusZDAPConfigRebootNow_Object = MibTableColumn
ruckusZDAPConfigRebootNow = _RuckusZDAPConfigRebootNow_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 64),
    _RuckusZDAPConfigRebootNow_Type()
)
ruckusZDAPConfigRebootNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDAPConfigRebootNow.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-AP-MIB",
    **{"ruckusZDAPMIB": ruckusZDAPMIB,
       "ruckusZDAPObjects": ruckusZDAPObjects,
       "ruckusZDAPConfig": ruckusZDAPConfig,
       "ruckusZDAPConfigTable": ruckusZDAPConfigTable,
       "ruckusZDAPConfigEntry": ruckusZDAPConfigEntry,
       "ruckusZDAPConfigID": ruckusZDAPConfigID,
       "ruckusZDAPConfigMacAddress": ruckusZDAPConfigMacAddress,
       "ruckusZDAPConfigAPModel": ruckusZDAPConfigAPModel,
       "ruckusZDAPConfigDeviceName": ruckusZDAPConfigDeviceName,
       "ruckusZDAPConfigDescription": ruckusZDAPConfigDescription,
       "ruckusZDAPConfigLocation": ruckusZDAPConfigLocation,
       "ruckusZDAPConfigGpsLatitude": ruckusZDAPConfigGpsLatitude,
       "ruckusZDAPConfigGpsLongitude": ruckusZDAPConfigGpsLongitude,
       "ruckusZDAPConfigIPVersion": ruckusZDAPConfigIPVersion,
       "ruckusZDAPConfigIpAddressSettingMode": ruckusZDAPConfigIpAddressSettingMode,
       "ruckusZDAPConfigIpAddress": ruckusZDAPConfigIpAddress,
       "ruckusZDAPConfigIpAddressMask": ruckusZDAPConfigIpAddressMask,
       "ruckusZDAPConfigGatewayIpAddress": ruckusZDAPConfigGatewayIpAddress,
       "ruckusZDAPConfigIpV6AddressSettingMode": ruckusZDAPConfigIpV6AddressSettingMode,
       "ruckusZDAPConfigIpV6Address": ruckusZDAPConfigIpV6Address,
       "ruckusZDAPConfigIpV6PrefixLen": ruckusZDAPConfigIpV6PrefixLen,
       "ruckusZDAPConfigGatewayIpV6Address": ruckusZDAPConfigGatewayIpV6Address,
       "ruckusZDAPConfigPrimaryDnsIpAddress": ruckusZDAPConfigPrimaryDnsIpAddress,
       "ruckusZDAPConfigSecondaryDnsIpAddress": ruckusZDAPConfigSecondaryDnsIpAddress,
       "ruckusZDAPConfigPrimaryDnsIpV6Address": ruckusZDAPConfigPrimaryDnsIpV6Address,
       "ruckusZDAPConfigSecondaryDnsV6IpAddress": ruckusZDAPConfigSecondaryDnsV6IpAddress,
       "ruckusZDAPConfigRadioType": ruckusZDAPConfigRadioType,
       "ruckusZDAPConfigRadioChannel24": ruckusZDAPConfigRadioChannel24,
       "ruckusZDAPConfigRadioTxPowerLevel24": ruckusZDAPConfigRadioTxPowerLevel24,
       "ruckusZDAPConfigRadioWlanGroup24": ruckusZDAPConfigRadioWlanGroup24,
       "ruckusZDAPConfigRadioEnableWlanService24": ruckusZDAPConfigRadioEnableWlanService24,
       "ruckusZDAPConfigRadioChannel5": ruckusZDAPConfigRadioChannel5,
       "ruckusZDAPConfigRadioTxPowerLevel5": ruckusZDAPConfigRadioTxPowerLevel5,
       "ruckusZDAPConfigRadioWlanGroup5": ruckusZDAPConfigRadioWlanGroup5,
       "ruckusZDAPConfigRadioEnableWlanService5": ruckusZDAPConfigRadioEnableWlanService5,
       "ruckusZDAPConfigMeshConfigurationMode": ruckusZDAPConfigMeshConfigurationMode,
       "ruckusZDAPConfigUplinkSelectionMode": ruckusZDAPConfigUplinkSelectionMode,
       "ruckusZDAPConfigApproveMode": ruckusZDAPConfigApproveMode,
       "ruckusZDAPConfigManagementAdmin": ruckusZDAPConfigManagementAdmin,
       "ruckusZDAPConfigRebootNow": ruckusZDAPConfigRebootNow}
)
