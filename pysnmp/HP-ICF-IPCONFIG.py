# SNMP MIB module (HP-ICF-IPCONFIG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-IPCONFIG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:36 2024
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

(hpicfCommon,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(IpAddressOriginTC,
 IpAddressStatusTC,
 ipNetToPhysicalEntry,
 ipv4InterfaceEntry,
 ipv6InterfaceEntry) = mibBuilder.importSymbols(
    "IP-MIB",
    "IpAddressOriginTC",
    "IpAddressStatusTC",
    "ipNetToPhysicalEntry",
    "ipv4InterfaceEntry",
    "ipv6InterfaceEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tunnelInetConfigEntry,) = mibBuilder.importSymbols(
    "TUNNEL-MIB",
    "tunnelInetConfigEntry")


# MODULE-IDENTITY

hpicfIpConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10)
)
hpicfIpConfig.setRevisions(
        ("2017-06-07 21:40",
         "2016-08-04 21:40",
         "2010-06-10 21:40",
         "2009-10-02 00:00",
         "2009-09-10 00:00",
         "2009-09-04 00:00",
         "2009-07-21 00:00",
         "2008-12-09 00:00",
         "2008-10-01 00:00",
         "2007-06-06 00:00",
         "2007-05-30 00:00",
         "2007-02-02 00:00",
         "2006-12-03 00:00",
         "2006-07-07 00:00",
         "2005-08-08 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfIpConfigObjects_ObjectIdentity = ObjectIdentity
hpicfIpConfigObjects = _HpicfIpConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1)
)
_HpicfIpAddressObjects_ObjectIdentity = ObjectIdentity
hpicfIpAddressObjects = _HpicfIpAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1)
)
_HpicfIpAddressTable_Object = MibTable
hpicfIpAddressTable = _HpicfIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfIpAddressTable.setStatus("current")
_HpicfIpAddressEntry_Object = MibTableRow
hpicfIpAddressEntry = _HpicfIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1, 1)
)
hpicfIpAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-IPCONFIG", "hpicfIpAddressAddrType"),
    (0, "HP-ICF-IPCONFIG", "hpicfIpAddressAddr"),
)
if mibBuilder.loadTexts:
    hpicfIpAddressEntry.setStatus("current")
_HpicfIpAddressAddrType_Type = InetAddressType
_HpicfIpAddressAddrType_Object = MibTableColumn
hpicfIpAddressAddrType = _HpicfIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1, 1, 1),
    _HpicfIpAddressAddrType_Type()
)
hpicfIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpAddressAddrType.setStatus("current")
_HpicfIpAddressAddr_Type = InetAddress
_HpicfIpAddressAddr_Object = MibTableColumn
hpicfIpAddressAddr = _HpicfIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1, 1, 2),
    _HpicfIpAddressAddr_Type()
)
hpicfIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpAddressAddr.setStatus("current")
_HpicfIpAddressPrefixLength_Type = InetAddressPrefixLength
_HpicfIpAddressPrefixLength_Object = MibTableColumn
hpicfIpAddressPrefixLength = _HpicfIpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1, 1, 3),
    _HpicfIpAddressPrefixLength_Type()
)
hpicfIpAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpAddressPrefixLength.setStatus("current")


class _HpicfIpAddressType_Type(Integer32):
    """Custom type hpicfIpAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 2),
          ("unicast", 1))
    )


_HpicfIpAddressType_Type.__name__ = "Integer32"
_HpicfIpAddressType_Object = MibTableColumn
hpicfIpAddressType = _HpicfIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1, 1, 4),
    _HpicfIpAddressType_Type()
)
hpicfIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpAddressType.setStatus("current")
_HpicfIpAddressRowStatus_Type = RowStatus
_HpicfIpAddressRowStatus_Object = MibTableColumn
hpicfIpAddressRowStatus = _HpicfIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1, 1, 5),
    _HpicfIpAddressRowStatus_Type()
)
hpicfIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpAddressRowStatus.setStatus("current")


class _HpicfIpAddressExtendedType_Type(Integer32):
    """Custom type hpicfIpAddressExtendedType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eui64", 1),
          ("linkLocal", 2),
          ("none", 0))
    )


_HpicfIpAddressExtendedType_Type.__name__ = "Integer32"
_HpicfIpAddressExtendedType_Object = MibTableColumn
hpicfIpAddressExtendedType = _HpicfIpAddressExtendedType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 1, 1, 6),
    _HpicfIpAddressExtendedType_Type()
)
hpicfIpAddressExtendedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpAddressExtendedType.setStatus("current")
_HpicfSwitchIpAddressTable_Object = MibTable
hpicfSwitchIpAddressTable = _HpicfSwitchIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressTable.setStatus("current")
_HpicfSwitchIpAddressEntry_Object = MibTableRow
hpicfSwitchIpAddressEntry = _HpicfSwitchIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1)
)
hpicfSwitchIpAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-IPCONFIG", "hpicfSwitchIpAddressAddrType"),
    (0, "HP-ICF-IPCONFIG", "hpicfSwitchIpAddressAddr"),
)
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressEntry.setStatus("current")
_HpicfSwitchIpAddressAddrType_Type = InetAddressType
_HpicfSwitchIpAddressAddrType_Object = MibTableColumn
hpicfSwitchIpAddressAddrType = _HpicfSwitchIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 1),
    _HpicfSwitchIpAddressAddrType_Type()
)
hpicfSwitchIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressAddrType.setStatus("current")
_HpicfSwitchIpAddressAddr_Type = InetAddress
_HpicfSwitchIpAddressAddr_Object = MibTableColumn
hpicfSwitchIpAddressAddr = _HpicfSwitchIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 2),
    _HpicfSwitchIpAddressAddr_Type()
)
hpicfSwitchIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressAddr.setStatus("current")
_HpicfSwitchIpAddressPrefixLength_Type = InetAddressPrefixLength
_HpicfSwitchIpAddressPrefixLength_Object = MibTableColumn
hpicfSwitchIpAddressPrefixLength = _HpicfSwitchIpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 3),
    _HpicfSwitchIpAddressPrefixLength_Type()
)
hpicfSwitchIpAddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressPrefixLength.setStatus("current")


class _HpicfSwitchIpAddressType_Type(Integer32):
    """Custom type hpicfSwitchIpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 2),
          ("unicast", 1))
    )


_HpicfSwitchIpAddressType_Type.__name__ = "Integer32"
_HpicfSwitchIpAddressType_Object = MibTableColumn
hpicfSwitchIpAddressType = _HpicfSwitchIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 4),
    _HpicfSwitchIpAddressType_Type()
)
hpicfSwitchIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressType.setStatus("current")
_HpicfSwitchIpAddressOrigin_Type = IpAddressOriginTC
_HpicfSwitchIpAddressOrigin_Object = MibTableColumn
hpicfSwitchIpAddressOrigin = _HpicfSwitchIpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 5),
    _HpicfSwitchIpAddressOrigin_Type()
)
hpicfSwitchIpAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressOrigin.setStatus("current")


class _HpicfSwitchIpAddressStatus_Type(IpAddressStatusTC):
    """Custom type hpicfSwitchIpAddressStatus based on IpAddressStatusTC"""


_HpicfSwitchIpAddressStatus_Object = MibTableColumn
hpicfSwitchIpAddressStatus = _HpicfSwitchIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 6),
    _HpicfSwitchIpAddressStatus_Type()
)
hpicfSwitchIpAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressStatus.setStatus("current")
_HpicfSwitchIpAddressPreferredLifetime_Type = Unsigned32
_HpicfSwitchIpAddressPreferredLifetime_Object = MibTableColumn
hpicfSwitchIpAddressPreferredLifetime = _HpicfSwitchIpAddressPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 7),
    _HpicfSwitchIpAddressPreferredLifetime_Type()
)
hpicfSwitchIpAddressPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressPreferredLifetime.setUnits("seconds")
_HpicfSwitchIpAddressValidLifetime_Type = Unsigned32
_HpicfSwitchIpAddressValidLifetime_Object = MibTableColumn
hpicfSwitchIpAddressValidLifetime = _HpicfSwitchIpAddressValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 8),
    _HpicfSwitchIpAddressValidLifetime_Type()
)
hpicfSwitchIpAddressValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressValidLifetime.setUnits("seconds")


class _HpicfSwitchIpAddressExtendedType_Type(Integer32):
    """Custom type hpicfSwitchIpAddressExtendedType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eui64", 1),
          ("linkLocal", 2),
          ("none", 0))
    )


_HpicfSwitchIpAddressExtendedType_Type.__name__ = "Integer32"
_HpicfSwitchIpAddressExtendedType_Object = MibTableColumn
hpicfSwitchIpAddressExtendedType = _HpicfSwitchIpAddressExtendedType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 2, 1, 9),
    _HpicfSwitchIpAddressExtendedType_Type()
)
hpicfSwitchIpAddressExtendedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressExtendedType.setStatus("current")
_HpicfIpNetToPhysicalTable_Object = MibTable
hpicfIpNetToPhysicalTable = _HpicfIpNetToPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfIpNetToPhysicalTable.setStatus("current")
_HpicfIpNetToPhysicalEntry_Object = MibTableRow
hpicfIpNetToPhysicalEntry = _HpicfIpNetToPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfIpNetToPhysicalEntry.setStatus("current")
_HpicfIpNetToPhysicalPort_Type = Integer32
_HpicfIpNetToPhysicalPort_Object = MibTableColumn
hpicfIpNetToPhysicalPort = _HpicfIpNetToPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 3, 1, 1),
    _HpicfIpNetToPhysicalPort_Type()
)
hpicfIpNetToPhysicalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpNetToPhysicalPort.setStatus("current")


class _HpicfIpNetToPhysicalTableClear_Type(Integer32):
    """Custom type hpicfIpNetToPhysicalTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 2),
          ("ipv6", 3),
          ("unknown", 1))
    )


_HpicfIpNetToPhysicalTableClear_Type.__name__ = "Integer32"
_HpicfIpNetToPhysicalTableClear_Object = MibScalar
hpicfIpNetToPhysicalTableClear = _HpicfIpNetToPhysicalTableClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 1, 4),
    _HpicfIpNetToPhysicalTableClear_Type()
)
hpicfIpNetToPhysicalTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpNetToPhysicalTableClear.setStatus("current")
_HpicfIpv4InterfaceObjects_ObjectIdentity = ObjectIdentity
hpicfIpv4InterfaceObjects = _HpicfIpv4InterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2)
)
_HpicfIpv4InterfaceTable_Object = MibTable
hpicfIpv4InterfaceTable = _HpicfIpv4InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceTable.setStatus("current")
_HpicfIpv4InterfaceEntry_Object = MibTableRow
hpicfIpv4InterfaceEntry = _HpicfIpv4InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceEntry.setStatus("current")


class _HpicfIpv4InterfaceDhcpEnable_Type(Integer32):
    """Custom type hpicfIpv4InterfaceDhcpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("inform", 3),
          ("off", 2))
    )


_HpicfIpv4InterfaceDhcpEnable_Type.__name__ = "Integer32"
_HpicfIpv4InterfaceDhcpEnable_Object = MibTableColumn
hpicfIpv4InterfaceDhcpEnable = _HpicfIpv4InterfaceDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1, 1, 1),
    _HpicfIpv4InterfaceDhcpEnable_Type()
)
hpicfIpv4InterfaceDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceDhcpEnable.setStatus("current")


class _HpicfIpv4InterfaceForwarding_Type(Integer32):
    """Custom type hpicfIpv4InterfaceForwarding based on Integer32"""
    defaultValue = 1

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


_HpicfIpv4InterfaceForwarding_Type.__name__ = "Integer32"
_HpicfIpv4InterfaceForwarding_Object = MibTableColumn
hpicfIpv4InterfaceForwarding = _HpicfIpv4InterfaceForwarding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1, 1, 2),
    _HpicfIpv4InterfaceForwarding_Type()
)
hpicfIpv4InterfaceForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceForwarding.setStatus("current")


class _HpicfIpv4InterfaceProxyArp_Type(Integer32):
    """Custom type hpicfIpv4InterfaceProxyArp based on Integer32"""
    defaultValue = 2

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


_HpicfIpv4InterfaceProxyArp_Type.__name__ = "Integer32"
_HpicfIpv4InterfaceProxyArp_Object = MibTableColumn
hpicfIpv4InterfaceProxyArp = _HpicfIpv4InterfaceProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1, 1, 3),
    _HpicfIpv4InterfaceProxyArp_Type()
)
hpicfIpv4InterfaceProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceProxyArp.setStatus("current")


class _HpicfIpv4InterfaceLocalProxyArp_Type(Integer32):
    """Custom type hpicfIpv4InterfaceLocalProxyArp based on Integer32"""
    defaultValue = 2

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


_HpicfIpv4InterfaceLocalProxyArp_Type.__name__ = "Integer32"
_HpicfIpv4InterfaceLocalProxyArp_Object = MibTableColumn
hpicfIpv4InterfaceLocalProxyArp = _HpicfIpv4InterfaceLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1, 1, 4),
    _HpicfIpv4InterfaceLocalProxyArp_Type()
)
hpicfIpv4InterfaceLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceLocalProxyArp.setStatus("current")
_HpicfIpv4InterfaceBootpGateway_Type = InetAddressIPv4
_HpicfIpv4InterfaceBootpGateway_Object = MibTableColumn
hpicfIpv4InterfaceBootpGateway = _HpicfIpv4InterfaceBootpGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1, 1, 5),
    _HpicfIpv4InterfaceBootpGateway_Type()
)
hpicfIpv4InterfaceBootpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceBootpGateway.setStatus("current")


class _HpicfIpv4InterfaceDirectedBcastFwd_Type(Integer32):
    """Custom type hpicfIpv4InterfaceDirectedBcastFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("enabled", 1))
    )


_HpicfIpv4InterfaceDirectedBcastFwd_Type.__name__ = "Integer32"
_HpicfIpv4InterfaceDirectedBcastFwd_Object = MibTableColumn
hpicfIpv4InterfaceDirectedBcastFwd = _HpicfIpv4InterfaceDirectedBcastFwd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 1, 1, 6),
    _HpicfIpv4InterfaceDirectedBcastFwd_Type()
)
hpicfIpv4InterfaceDirectedBcastFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceDirectedBcastFwd.setStatus("current")
_HpicfUdpTunnelTable_Object = MibTable
hpicfUdpTunnelTable = _HpicfUdpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfUdpTunnelTable.setStatus("current")
_HpicfUdpTunnelEntry_Object = MibTableRow
hpicfUdpTunnelEntry = _HpicfUdpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfUdpTunnelEntry.setStatus("current")


class _HpicfUdpTunnelSrcPort_Type(InetPortNumber):
    """Custom type hpicfUdpTunnelSrcPort based on InetPortNumber"""
    defaultValue = 0


_HpicfUdpTunnelSrcPort_Object = MibTableColumn
hpicfUdpTunnelSrcPort = _HpicfUdpTunnelSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 3, 1, 1),
    _HpicfUdpTunnelSrcPort_Type()
)
hpicfUdpTunnelSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUdpTunnelSrcPort.setStatus("current")


class _HpicfUdpTunnelMirrorSessionID_Type(Integer32):
    """Custom type hpicfUdpTunnelMirrorSessionID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_HpicfUdpTunnelMirrorSessionID_Type.__name__ = "Integer32"
_HpicfUdpTunnelMirrorSessionID_Object = MibTableColumn
hpicfUdpTunnelMirrorSessionID = _HpicfUdpTunnelMirrorSessionID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 3, 1, 2),
    _HpicfUdpTunnelMirrorSessionID_Type()
)
hpicfUdpTunnelMirrorSessionID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUdpTunnelMirrorSessionID.setStatus("current")


class _HpicfUdpTunnelMirrorTruncate_Type(Integer32):
    """Custom type hpicfUdpTunnelMirrorTruncate based on Integer32"""
    defaultValue = 2

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


_HpicfUdpTunnelMirrorTruncate_Type.__name__ = "Integer32"
_HpicfUdpTunnelMirrorTruncate_Object = MibTableColumn
hpicfUdpTunnelMirrorTruncate = _HpicfUdpTunnelMirrorTruncate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 2, 3, 1, 3),
    _HpicfUdpTunnelMirrorTruncate_Type()
)
hpicfUdpTunnelMirrorTruncate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpTunnelMirrorTruncate.setStatus("current")
_HpicfIpClientTrackerObjects_ObjectIdentity = ObjectIdentity
hpicfIpClientTrackerObjects = _HpicfIpClientTrackerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 3)
)


class _HpicfIpClientTrackerEnable_Type(TruthValue):
    """Custom type hpicfIpClientTrackerEnable based on TruthValue"""


_HpicfIpClientTrackerEnable_Object = MibScalar
hpicfIpClientTrackerEnable = _HpicfIpClientTrackerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 3, 1),
    _HpicfIpClientTrackerEnable_Type()
)
hpicfIpClientTrackerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpClientTrackerEnable.setStatus("current")


class _HpicfIpClientTrackerTrusted_Type(TruthValue):
    """Custom type hpicfIpClientTrackerTrusted based on TruthValue"""


_HpicfIpClientTrackerTrusted_Object = MibScalar
hpicfIpClientTrackerTrusted = _HpicfIpClientTrackerTrusted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 3, 2),
    _HpicfIpClientTrackerTrusted_Type()
)
hpicfIpClientTrackerTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpClientTrackerTrusted.setStatus("current")


class _HpicfIpClientTrackerUntrusted_Type(TruthValue):
    """Custom type hpicfIpClientTrackerUntrusted based on TruthValue"""


_HpicfIpClientTrackerUntrusted_Object = MibScalar
hpicfIpClientTrackerUntrusted = _HpicfIpClientTrackerUntrusted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 1, 3, 3),
    _HpicfIpClientTrackerUntrusted_Type()
)
hpicfIpClientTrackerUntrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpClientTrackerUntrusted.setStatus("current")
_HpicfIpConfigConformance_ObjectIdentity = ObjectIdentity
hpicfIpConfigConformance = _HpicfIpConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2)
)
_HpicfIpConfigCompliances_ObjectIdentity = ObjectIdentity
hpicfIpConfigCompliances = _HpicfIpConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1)
)
_HpicfIpConfigGroups_ObjectIdentity = ObjectIdentity
hpicfIpConfigGroups = _HpicfIpConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2)
)
_HpicfIpv6ConfigObjects_ObjectIdentity = ObjectIdentity
hpicfIpv6ConfigObjects = _HpicfIpv6ConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3)
)
_HpicfIpv6GlobalConfigObjects_ObjectIdentity = ObjectIdentity
hpicfIpv6GlobalConfigObjects = _HpicfIpv6GlobalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 1)
)
_HpicfIpv6NDObjects_ObjectIdentity = ObjectIdentity
hpicfIpv6NDObjects = _HpicfIpv6NDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 1, 1)
)
_HpicfIpv6NDDadAttempts_Type = Integer32
_HpicfIpv6NDDadAttempts_Object = MibScalar
hpicfIpv6NDDadAttempts = _HpicfIpv6NDDadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 1, 1, 1),
    _HpicfIpv6NDDadAttempts_Type()
)
hpicfIpv6NDDadAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6NDDadAttempts.setStatus("current")
_HpicfIpv6IcmpObjects_ObjectIdentity = ObjectIdentity
hpicfIpv6IcmpObjects = _HpicfIpv6IcmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 1, 2)
)
_HpicfIpv6IcmpErrorInterval_Type = Integer32
_HpicfIpv6IcmpErrorInterval_Object = MibScalar
hpicfIpv6IcmpErrorInterval = _HpicfIpv6IcmpErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 1, 2, 1),
    _HpicfIpv6IcmpErrorInterval_Type()
)
hpicfIpv6IcmpErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6IcmpErrorInterval.setStatus("current")
_HpicfIpv6IcmpBucketsize_Type = Integer32
_HpicfIpv6IcmpBucketsize_Object = MibScalar
hpicfIpv6IcmpBucketsize = _HpicfIpv6IcmpBucketsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 1, 2, 2),
    _HpicfIpv6IcmpBucketsize_Type()
)
hpicfIpv6IcmpBucketsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6IcmpBucketsize.setStatus("current")
_HpicfIpv6InterfaceObjects_ObjectIdentity = ObjectIdentity
hpicfIpv6InterfaceObjects = _HpicfIpv6InterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2)
)
_HpicfIpv6InterfaceTable_Object = MibTable
hpicfIpv6InterfaceTable = _HpicfIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceTable.setStatus("current")
_HpicfIpv6InterfaceEntry_Object = MibTableRow
hpicfIpv6InterfaceEntry = _HpicfIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceEntry.setStatus("current")


class _HpicfIpv6InterfaceDhcpMode_Type(Integer32):
    """Custom type hpicfIpv6InterfaceDhcpMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpFull", 1),
          ("dhcpInform", 2),
          ("disabled", 0))
    )


_HpicfIpv6InterfaceDhcpMode_Type.__name__ = "Integer32"
_HpicfIpv6InterfaceDhcpMode_Object = MibTableColumn
hpicfIpv6InterfaceDhcpMode = _HpicfIpv6InterfaceDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 1),
    _HpicfIpv6InterfaceDhcpMode_Type()
)
hpicfIpv6InterfaceDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceDhcpMode.setStatus("current")


class _HpicfIpv6InterfaceManual_Type(Integer32):
    """Custom type hpicfIpv6InterfaceManual based on Integer32"""
    defaultValue = 2

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


_HpicfIpv6InterfaceManual_Type.__name__ = "Integer32"
_HpicfIpv6InterfaceManual_Object = MibTableColumn
hpicfIpv6InterfaceManual = _HpicfIpv6InterfaceManual_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 2),
    _HpicfIpv6InterfaceManual_Type()
)
hpicfIpv6InterfaceManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceManual.setStatus("current")


class _HpicfIpv6InterfaceAutoConfig_Type(Integer32):
    """Custom type hpicfIpv6InterfaceAutoConfig based on Integer32"""
    defaultValue = 2

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


_HpicfIpv6InterfaceAutoConfig_Type.__name__ = "Integer32"
_HpicfIpv6InterfaceAutoConfig_Object = MibTableColumn
hpicfIpv6InterfaceAutoConfig = _HpicfIpv6InterfaceAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 3),
    _HpicfIpv6InterfaceAutoConfig_Type()
)
hpicfIpv6InterfaceAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceAutoConfig.setStatus("current")


class _HpicfIpv6InterfaceDhcpRapidCommit_Type(Integer32):
    """Custom type hpicfIpv6InterfaceDhcpRapidCommit based on Integer32"""
    defaultValue = 2

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


_HpicfIpv6InterfaceDhcpRapidCommit_Type.__name__ = "Integer32"
_HpicfIpv6InterfaceDhcpRapidCommit_Object = MibTableColumn
hpicfIpv6InterfaceDhcpRapidCommit = _HpicfIpv6InterfaceDhcpRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 4),
    _HpicfIpv6InterfaceDhcpRapidCommit_Type()
)
hpicfIpv6InterfaceDhcpRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceDhcpRapidCommit.setStatus("current")


class _HpicfIpv6InterfaceDhcpRelay_Type(Integer32):
    """Custom type hpicfIpv6InterfaceDhcpRelay based on Integer32"""
    defaultValue = 1

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


_HpicfIpv6InterfaceDhcpRelay_Type.__name__ = "Integer32"
_HpicfIpv6InterfaceDhcpRelay_Object = MibTableColumn
hpicfIpv6InterfaceDhcpRelay = _HpicfIpv6InterfaceDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 5),
    _HpicfIpv6InterfaceDhcpRelay_Type()
)
hpicfIpv6InterfaceDhcpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceDhcpRelay.setStatus("current")


class _HpicfIpv6InterfaceCfgEnableStatus_Type(Integer32):
    """Custom type hpicfIpv6InterfaceCfgEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HpicfIpv6InterfaceCfgEnableStatus_Type.__name__ = "Integer32"
_HpicfIpv6InterfaceCfgEnableStatus_Object = MibTableColumn
hpicfIpv6InterfaceCfgEnableStatus = _HpicfIpv6InterfaceCfgEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 6),
    _HpicfIpv6InterfaceCfgEnableStatus_Type()
)
hpicfIpv6InterfaceCfgEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceCfgEnableStatus.setStatus("current")
_HpicfIpv6InterfaceDadAttempts_Type = Integer32
_HpicfIpv6InterfaceDadAttempts_Object = MibTableColumn
hpicfIpv6InterfaceDadAttempts = _HpicfIpv6InterfaceDadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 7),
    _HpicfIpv6InterfaceDadAttempts_Type()
)
hpicfIpv6InterfaceDadAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceDadAttempts.setStatus("current")


class _HpicfIpv6InterfaceDadAttemptsMode_Type(Integer32):
    """Custom type hpicfIpv6InterfaceDadAttemptsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("perInterface", 2))
    )


_HpicfIpv6InterfaceDadAttemptsMode_Type.__name__ = "Integer32"
_HpicfIpv6InterfaceDadAttemptsMode_Object = MibTableColumn
hpicfIpv6InterfaceDadAttemptsMode = _HpicfIpv6InterfaceDadAttemptsMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 8),
    _HpicfIpv6InterfaceDadAttemptsMode_Type()
)
hpicfIpv6InterfaceDadAttemptsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceDadAttemptsMode.setStatus("current")
_HpicfIpv6InterfaceReachableTime_Type = Unsigned32
_HpicfIpv6InterfaceReachableTime_Object = MibTableColumn
hpicfIpv6InterfaceReachableTime = _HpicfIpv6InterfaceReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 9),
    _HpicfIpv6InterfaceReachableTime_Type()
)
hpicfIpv6InterfaceReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceReachableTime.setUnits("milliseconds")
_HpicfIpv6InterfaceRetransmitTime_Type = Unsigned32
_HpicfIpv6InterfaceRetransmitTime_Object = MibTableColumn
hpicfIpv6InterfaceRetransmitTime = _HpicfIpv6InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 3, 2, 1, 1, 10),
    _HpicfIpv6InterfaceRetransmitTime_Type()
)
hpicfIpv6InterfaceRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceRetransmitTime.setUnits("milliseconds")
ipNetToPhysicalEntry.registerAugmentions(
    ("HP-ICF-IPCONFIG",
     "hpicfIpNetToPhysicalEntry")
)
hpicfIpNetToPhysicalEntry.setIndexNames(*ipNetToPhysicalEntry.getIndexNames())
ipv4InterfaceEntry.registerAugmentions(
    ("HP-ICF-IPCONFIG",
     "hpicfIpv4InterfaceEntry")
)
hpicfIpv4InterfaceEntry.setIndexNames(*ipv4InterfaceEntry.getIndexNames())
tunnelInetConfigEntry.registerAugmentions(
    ("HP-ICF-IPCONFIG",
     "hpicfUdpTunnelEntry")
)
hpicfUdpTunnelEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
ipv6InterfaceEntry.registerAugmentions(
    ("HP-ICF-IPCONFIG",
     "hpicfIpv6InterfaceEntry")
)
hpicfIpv6InterfaceEntry.setIndexNames(*ipv6InterfaceEntry.getIndexNames())

# Managed Objects groups

hpicfIpAddressTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 1)
)
hpicfIpAddressTableGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpAddressPrefixLength"),
        ("HP-ICF-IPCONFIG", "hpicfIpAddressType"),
        ("HP-ICF-IPCONFIG", "hpicfIpAddressRowStatus"),
        ("HP-ICF-IPCONFIG", "hpicfIpAddressExtendedType"))
)
if mibBuilder.loadTexts:
    hpicfIpAddressTableGroup.setStatus("current")

hpicfSwitchIpAddressTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 2)
)
hpicfSwitchIpAddressTableGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfSwitchIpAddressPrefixLength"),
        ("HP-ICF-IPCONFIG", "hpicfSwitchIpAddressType"),
        ("HP-ICF-IPCONFIG", "hpicfSwitchIpAddressOrigin"),
        ("HP-ICF-IPCONFIG", "hpicfSwitchIpAddressStatus"),
        ("HP-ICF-IPCONFIG", "hpicfSwitchIpAddressPreferredLifetime"),
        ("HP-ICF-IPCONFIG", "hpicfSwitchIpAddressValidLifetime"),
        ("HP-ICF-IPCONFIG", "hpicfSwitchIpAddressExtendedType"))
)
if mibBuilder.loadTexts:
    hpicfSwitchIpAddressTableGroup.setStatus("current")

hpicfIpv4InterfaceTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 3)
)
hpicfIpv4InterfaceTableGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceDhcpEnable"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceForwarding"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceProxyArp"))
)
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceTableGroup.setStatus("deprecated")

hpicfUdpTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 4)
)
hpicfUdpTunnelTableGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfUdpTunnelSrcPort"),
        ("HP-ICF-IPCONFIG", "hpicfUdpTunnelMirrorSessionID"))
)
if mibBuilder.loadTexts:
    hpicfUdpTunnelTableGroup.setStatus("current")

hpicfIpv6InterfaceTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 5)
)
hpicfIpv6InterfaceTableGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceDhcpMode"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceManual"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceAutoConfig"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceDhcpRapidCommit"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceDhcpRelay"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceCfgEnableStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpv6InterfaceTableGroup.setStatus("current")

hpicfIpv4InterfaceTableGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 6)
)
hpicfIpv4InterfaceTableGroup2.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceDhcpEnable"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceForwarding"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceProxyArp"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceLocalProxyArp"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceBootpGateway"))
)
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceTableGroup2.setStatus("current")

hpicfIpv6DadAttemptsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 7)
)
hpicfIpv6DadAttemptsGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpv6NDDadAttempts"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceDadAttempts"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceDadAttemptsMode"))
)
if mibBuilder.loadTexts:
    hpicfIpv6DadAttemptsGroup.setStatus("current")

hpicfIpv6IcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 8)
)
hpicfIpv6IcmpGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpv6IcmpErrorInterval"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6IcmpBucketsize"))
)
if mibBuilder.loadTexts:
    hpicfIpv6IcmpGroup.setStatus("current")

hpicfIpNetToPhysicalTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 9)
)
hpicfIpNetToPhysicalTableGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpNetToPhysicalPort"),
        ("HP-ICF-IPCONFIG", "hpicfIpNetToPhysicalTableClear"))
)
if mibBuilder.loadTexts:
    hpicfIpNetToPhysicalTableGroup.setStatus("current")

hpicfUdpTunnelMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 10)
)
hpicfUdpTunnelMirrorGroup.setObjects(
    ("HP-ICF-IPCONFIG", "hpicfUdpTunnelMirrorTruncate")
)
if mibBuilder.loadTexts:
    hpicfUdpTunnelMirrorGroup.setStatus("current")

hpicfIpv6NDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 11)
)
hpicfIpv6NDGroup.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceReachableTime"),
        ("HP-ICF-IPCONFIG", "hpicfIpv6InterfaceRetransmitTime"))
)
if mibBuilder.loadTexts:
    hpicfIpv6NDGroup.setStatus("current")

hpicfIpv4InterfaceTableGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 12)
)
hpicfIpv4InterfaceTableGroup3.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceDhcpEnable"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceForwarding"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceProxyArp"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceLocalProxyArp"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceBootpGateway"),
        ("HP-ICF-IPCONFIG", "hpicfIpv4InterfaceDirectedBcastFwd"))
)
if mibBuilder.loadTexts:
    hpicfIpv4InterfaceTableGroup3.setStatus("current")

hpicfIpClientTrackerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 13)
)
hpicfIpClientTrackerGroup.setObjects(
    ("HP-ICF-IPCONFIG", "hpicfIpClientTrackerEnable")
)
if mibBuilder.loadTexts:
    hpicfIpClientTrackerGroup.setStatus("deprecated")

hpicfIpClientTrackerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 2, 14)
)
hpicfIpClientTrackerGroup2.setObjects(
      *(("HP-ICF-IPCONFIG", "hpicfIpClientTrackerEnable"),
        ("HP-ICF-IPCONFIG", "hpicfIpClientTrackerTrusted"),
        ("HP-ICF-IPCONFIG", "hpicfIpClientTrackerUntrusted"))
)
if mibBuilder.loadTexts:
    hpicfIpClientTrackerGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfIpConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance.setStatus(
        "deprecated"
    )

hpicfIpConfigCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance2.setStatus(
        "current"
    )

hpicfIpConfigCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance4.setStatus(
        "current"
    )

hpicfIpConfigCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance5.setStatus(
        "current"
    )

hpicfIpConfigCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance6.setStatus(
        "current"
    )

hpicfIpConfigCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance7.setStatus(
        "current"
    )

hpicfIpConfigCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance8.setStatus(
        "current"
    )

hpicfIpConfigCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance9.setStatus(
        "current"
    )

hpicfIpConfigCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance10.setStatus(
        "deprecated"
    )

hpicfIpConfigCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 10, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hpicfIpConfigCompliance11.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-IPCONFIG",
    **{"hpicfIpConfig": hpicfIpConfig,
       "hpicfIpConfigObjects": hpicfIpConfigObjects,
       "hpicfIpAddressObjects": hpicfIpAddressObjects,
       "hpicfIpAddressTable": hpicfIpAddressTable,
       "hpicfIpAddressEntry": hpicfIpAddressEntry,
       "hpicfIpAddressAddrType": hpicfIpAddressAddrType,
       "hpicfIpAddressAddr": hpicfIpAddressAddr,
       "hpicfIpAddressPrefixLength": hpicfIpAddressPrefixLength,
       "hpicfIpAddressType": hpicfIpAddressType,
       "hpicfIpAddressRowStatus": hpicfIpAddressRowStatus,
       "hpicfIpAddressExtendedType": hpicfIpAddressExtendedType,
       "hpicfSwitchIpAddressTable": hpicfSwitchIpAddressTable,
       "hpicfSwitchIpAddressEntry": hpicfSwitchIpAddressEntry,
       "hpicfSwitchIpAddressAddrType": hpicfSwitchIpAddressAddrType,
       "hpicfSwitchIpAddressAddr": hpicfSwitchIpAddressAddr,
       "hpicfSwitchIpAddressPrefixLength": hpicfSwitchIpAddressPrefixLength,
       "hpicfSwitchIpAddressType": hpicfSwitchIpAddressType,
       "hpicfSwitchIpAddressOrigin": hpicfSwitchIpAddressOrigin,
       "hpicfSwitchIpAddressStatus": hpicfSwitchIpAddressStatus,
       "hpicfSwitchIpAddressPreferredLifetime": hpicfSwitchIpAddressPreferredLifetime,
       "hpicfSwitchIpAddressValidLifetime": hpicfSwitchIpAddressValidLifetime,
       "hpicfSwitchIpAddressExtendedType": hpicfSwitchIpAddressExtendedType,
       "hpicfIpNetToPhysicalTable": hpicfIpNetToPhysicalTable,
       "hpicfIpNetToPhysicalEntry": hpicfIpNetToPhysicalEntry,
       "hpicfIpNetToPhysicalPort": hpicfIpNetToPhysicalPort,
       "hpicfIpNetToPhysicalTableClear": hpicfIpNetToPhysicalTableClear,
       "hpicfIpv4InterfaceObjects": hpicfIpv4InterfaceObjects,
       "hpicfIpv4InterfaceTable": hpicfIpv4InterfaceTable,
       "hpicfIpv4InterfaceEntry": hpicfIpv4InterfaceEntry,
       "hpicfIpv4InterfaceDhcpEnable": hpicfIpv4InterfaceDhcpEnable,
       "hpicfIpv4InterfaceForwarding": hpicfIpv4InterfaceForwarding,
       "hpicfIpv4InterfaceProxyArp": hpicfIpv4InterfaceProxyArp,
       "hpicfIpv4InterfaceLocalProxyArp": hpicfIpv4InterfaceLocalProxyArp,
       "hpicfIpv4InterfaceBootpGateway": hpicfIpv4InterfaceBootpGateway,
       "hpicfIpv4InterfaceDirectedBcastFwd": hpicfIpv4InterfaceDirectedBcastFwd,
       "hpicfUdpTunnelTable": hpicfUdpTunnelTable,
       "hpicfUdpTunnelEntry": hpicfUdpTunnelEntry,
       "hpicfUdpTunnelSrcPort": hpicfUdpTunnelSrcPort,
       "hpicfUdpTunnelMirrorSessionID": hpicfUdpTunnelMirrorSessionID,
       "hpicfUdpTunnelMirrorTruncate": hpicfUdpTunnelMirrorTruncate,
       "hpicfIpClientTrackerObjects": hpicfIpClientTrackerObjects,
       "hpicfIpClientTrackerEnable": hpicfIpClientTrackerEnable,
       "hpicfIpClientTrackerTrusted": hpicfIpClientTrackerTrusted,
       "hpicfIpClientTrackerUntrusted": hpicfIpClientTrackerUntrusted,
       "hpicfIpConfigConformance": hpicfIpConfigConformance,
       "hpicfIpConfigCompliances": hpicfIpConfigCompliances,
       "hpicfIpConfigCompliance": hpicfIpConfigCompliance,
       "hpicfIpConfigCompliance2": hpicfIpConfigCompliance2,
       "hpicfIpConfigCompliance4": hpicfIpConfigCompliance4,
       "hpicfIpConfigCompliance5": hpicfIpConfigCompliance5,
       "hpicfIpConfigCompliance6": hpicfIpConfigCompliance6,
       "hpicfIpConfigCompliance7": hpicfIpConfigCompliance7,
       "hpicfIpConfigCompliance8": hpicfIpConfigCompliance8,
       "hpicfIpConfigCompliance9": hpicfIpConfigCompliance9,
       "hpicfIpConfigCompliance10": hpicfIpConfigCompliance10,
       "hpicfIpConfigCompliance11": hpicfIpConfigCompliance11,
       "hpicfIpConfigGroups": hpicfIpConfigGroups,
       "hpicfIpAddressTableGroup": hpicfIpAddressTableGroup,
       "hpicfSwitchIpAddressTableGroup": hpicfSwitchIpAddressTableGroup,
       "hpicfIpv4InterfaceTableGroup": hpicfIpv4InterfaceTableGroup,
       "hpicfUdpTunnelTableGroup": hpicfUdpTunnelTableGroup,
       "hpicfIpv6InterfaceTableGroup": hpicfIpv6InterfaceTableGroup,
       "hpicfIpv4InterfaceTableGroup2": hpicfIpv4InterfaceTableGroup2,
       "hpicfIpv6DadAttemptsGroup": hpicfIpv6DadAttemptsGroup,
       "hpicfIpv6IcmpGroup": hpicfIpv6IcmpGroup,
       "hpicfIpNetToPhysicalTableGroup": hpicfIpNetToPhysicalTableGroup,
       "hpicfUdpTunnelMirrorGroup": hpicfUdpTunnelMirrorGroup,
       "hpicfIpv6NDGroup": hpicfIpv6NDGroup,
       "hpicfIpv4InterfaceTableGroup3": hpicfIpv4InterfaceTableGroup3,
       "hpicfIpClientTrackerGroup": hpicfIpClientTrackerGroup,
       "hpicfIpClientTrackerGroup2": hpicfIpClientTrackerGroup2,
       "hpicfIpv6ConfigObjects": hpicfIpv6ConfigObjects,
       "hpicfIpv6GlobalConfigObjects": hpicfIpv6GlobalConfigObjects,
       "hpicfIpv6NDObjects": hpicfIpv6NDObjects,
       "hpicfIpv6NDDadAttempts": hpicfIpv6NDDadAttempts,
       "hpicfIpv6IcmpObjects": hpicfIpv6IcmpObjects,
       "hpicfIpv6IcmpErrorInterval": hpicfIpv6IcmpErrorInterval,
       "hpicfIpv6IcmpBucketsize": hpicfIpv6IcmpBucketsize,
       "hpicfIpv6InterfaceObjects": hpicfIpv6InterfaceObjects,
       "hpicfIpv6InterfaceTable": hpicfIpv6InterfaceTable,
       "hpicfIpv6InterfaceEntry": hpicfIpv6InterfaceEntry,
       "hpicfIpv6InterfaceDhcpMode": hpicfIpv6InterfaceDhcpMode,
       "hpicfIpv6InterfaceManual": hpicfIpv6InterfaceManual,
       "hpicfIpv6InterfaceAutoConfig": hpicfIpv6InterfaceAutoConfig,
       "hpicfIpv6InterfaceDhcpRapidCommit": hpicfIpv6InterfaceDhcpRapidCommit,
       "hpicfIpv6InterfaceDhcpRelay": hpicfIpv6InterfaceDhcpRelay,
       "hpicfIpv6InterfaceCfgEnableStatus": hpicfIpv6InterfaceCfgEnableStatus,
       "hpicfIpv6InterfaceDadAttempts": hpicfIpv6InterfaceDadAttempts,
       "hpicfIpv6InterfaceDadAttemptsMode": hpicfIpv6InterfaceDadAttemptsMode,
       "hpicfIpv6InterfaceReachableTime": hpicfIpv6InterfaceReachableTime,
       "hpicfIpv6InterfaceRetransmitTime": hpicfIpv6InterfaceRetransmitTime}
)
