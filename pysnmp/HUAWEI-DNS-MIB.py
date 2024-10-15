# SNMP MIB module (HUAWEI-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:36 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(EnabledStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus",
    "TextualConvention")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDnsObjects_ObjectIdentity = ObjectIdentity
hwDnsObjects = _HwDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1)
)
_HwDnsHostsDynamicTable_Object = MibTable
hwDnsHostsDynamicTable = _HwDnsHostsDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 1)
)
if mibBuilder.loadTexts:
    hwDnsHostsDynamicTable.setStatus("current")
_HwDnsHostsDynamicEntry_Object = MibTableRow
hwDnsHostsDynamicEntry = _HwDnsHostsDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 1, 1)
)
hwDnsHostsDynamicEntry.setIndexNames(
    (0, "HUAWEI-DNS-MIB", "hwDnsDomainName"),
)
if mibBuilder.loadTexts:
    hwDnsHostsDynamicEntry.setStatus("current")
_HwDnsDomainName_Type = DisplayString
_HwDnsDomainName_Object = MibTableColumn
hwDnsDomainName = _HwDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 1, 1, 1),
    _HwDnsDomainName_Type()
)
hwDnsDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDnsDomainName.setStatus("current")
_HwDnsIpAddress_Type = IpAddress
_HwDnsIpAddress_Object = MibTableColumn
hwDnsIpAddress = _HwDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 1, 1, 2),
    _HwDnsIpAddress_Type()
)
hwDnsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDnsIpAddress.setStatus("current")
_HwDnsTtl_Type = Integer32
_HwDnsTtl_Object = MibTableColumn
hwDnsTtl = _HwDnsTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 1, 1, 3),
    _HwDnsTtl_Type()
)
hwDnsTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDnsTtl.setStatus("current")
_HwDnsAlias_Type = DisplayString
_HwDnsAlias_Object = MibTableColumn
hwDnsAlias = _HwDnsAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 1, 1, 4),
    _HwDnsAlias_Type()
)
hwDnsAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDnsAlias.setStatus("current")
_HwDns6HostsDynamicTable_Object = MibTable
hwDns6HostsDynamicTable = _HwDns6HostsDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 2)
)
if mibBuilder.loadTexts:
    hwDns6HostsDynamicTable.setStatus("current")
_HwDns6HostsDynamicEntry_Object = MibTableRow
hwDns6HostsDynamicEntry = _HwDns6HostsDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 2, 1)
)
hwDns6HostsDynamicEntry.setIndexNames(
    (0, "HUAWEI-DNS-MIB", "hwDns6DomainName"),
)
if mibBuilder.loadTexts:
    hwDns6HostsDynamicEntry.setStatus("current")
_HwDns6DomainName_Type = DisplayString
_HwDns6DomainName_Object = MibTableColumn
hwDns6DomainName = _HwDns6DomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 2, 1, 1),
    _HwDns6DomainName_Type()
)
hwDns6DomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDns6DomainName.setStatus("current")
_HwDns6Ipv6Address_Type = DisplayString
_HwDns6Ipv6Address_Object = MibTableColumn
hwDns6Ipv6Address = _HwDns6Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 2, 1, 2),
    _HwDns6Ipv6Address_Type()
)
hwDns6Ipv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDns6Ipv6Address.setStatus("current")
_HwDns6Ttl_Type = Integer32
_HwDns6Ttl_Object = MibTableColumn
hwDns6Ttl = _HwDns6Ttl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 2, 1, 3),
    _HwDns6Ttl_Type()
)
hwDns6Ttl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDns6Ttl.setStatus("current")
_HwDns6Alias_Type = DisplayString
_HwDns6Alias_Object = MibTableColumn
hwDns6Alias = _HwDns6Alias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 2, 1, 4),
    _HwDns6Alias_Type()
)
hwDns6Alias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDns6Alias.setStatus("current")
_HwDdnsConfigTable_Object = MibTable
hwDdnsConfigTable = _HwDdnsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 3)
)
if mibBuilder.loadTexts:
    hwDdnsConfigTable.setStatus("current")
_HwDdnsConfigEntry_Object = MibTableRow
hwDdnsConfigEntry = _HwDdnsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 3, 1)
)
hwDdnsConfigEntry.setIndexNames(
    (0, "HUAWEI-DNS-MIB", "hwDdnsPolicyName"),
    (0, "HUAWEI-DNS-MIB", "hwDdnsIfindex"),
)
if mibBuilder.loadTexts:
    hwDdnsConfigEntry.setStatus("current")
_HwDdnsPolicyName_Type = DisplayString
_HwDdnsPolicyName_Object = MibTableColumn
hwDdnsPolicyName = _HwDdnsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 3, 1, 1),
    _HwDdnsPolicyName_Type()
)
hwDdnsPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDdnsPolicyName.setStatus("current")
_HwDdnsIfindex_Type = Integer32
_HwDdnsIfindex_Object = MibTableColumn
hwDdnsIfindex = _HwDdnsIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 3, 1, 2),
    _HwDdnsIfindex_Type()
)
hwDdnsIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDdnsIfindex.setStatus("current")
_HwService_Type = Integer32
_HwService_Object = MibTableColumn
hwService = _HwService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 3, 1, 3),
    _HwService_Type()
)
hwService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwService.setStatus("current")
_HwDdnsUserName_Type = DisplayString
_HwDdnsUserName_Object = MibTableColumn
hwDdnsUserName = _HwDdnsUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 3, 1, 4),
    _HwDdnsUserName_Type()
)
hwDdnsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDdnsUserName.setStatus("current")
_HwDdnsFqdn_Type = DisplayString
_HwDdnsFqdn_Object = MibTableColumn
hwDdnsFqdn = _HwDdnsFqdn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 3, 1, 5),
    _HwDdnsFqdn_Type()
)
hwDdnsFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDdnsFqdn.setStatus("current")
_HwDnsServerAddrTable_Object = MibTable
hwDnsServerAddrTable = _HwDnsServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 4)
)
if mibBuilder.loadTexts:
    hwDnsServerAddrTable.setStatus("current")
_HwDnsServerAddrEntry_Object = MibTableRow
hwDnsServerAddrEntry = _HwDnsServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 4, 1)
)
hwDnsServerAddrEntry.setIndexNames(
    (0, "HUAWEI-DNS-MIB", "hwServerAddr"),
)
if mibBuilder.loadTexts:
    hwDnsServerAddrEntry.setStatus("current")
_HwServerAddr_Type = IpAddress
_HwServerAddr_Object = MibTableColumn
hwServerAddr = _HwServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 4, 1, 1),
    _HwServerAddr_Type()
)
hwServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwServerAddr.setStatus("current")
_HwServerStatus_Type = Integer32
_HwServerStatus_Object = MibTableColumn
hwServerStatus = _HwServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 4, 1, 2),
    _HwServerStatus_Type()
)
hwServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServerStatus.setStatus("current")
_HwDnsDomainSuffixTable_Object = MibTable
hwDnsDomainSuffixTable = _HwDnsDomainSuffixTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 5)
)
if mibBuilder.loadTexts:
    hwDnsDomainSuffixTable.setStatus("current")
_HwDnsDomainSuffixEntry_Object = MibTableRow
hwDnsDomainSuffixEntry = _HwDnsDomainSuffixEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 5, 1)
)
hwDnsDomainSuffixEntry.setIndexNames(
    (0, "HUAWEI-DNS-MIB", "hwDomainSuffix"),
)
if mibBuilder.loadTexts:
    hwDnsDomainSuffixEntry.setStatus("current")
_HwDomainSuffix_Type = DisplayString
_HwDomainSuffix_Object = MibTableColumn
hwDomainSuffix = _HwDomainSuffix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 5, 1, 1),
    _HwDomainSuffix_Type()
)
hwDomainSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDomainSuffix.setStatus("current")
_HwDnsProxyEnable_Type = EnabledStatus
_HwDnsProxyEnable_Object = MibScalar
hwDnsProxyEnable = _HwDnsProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 1, 6),
    _HwDnsProxyEnable_Type()
)
hwDnsProxyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDnsProxyEnable.setStatus("current")
_HwDnsConformance_ObjectIdentity = ObjectIdentity
hwDnsConformance = _HwDnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 3)
)
_HwDnsGroups_ObjectIdentity = ObjectIdentity
hwDnsGroups = _HwDnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 3, 1)
)
_HwDnsCompliances_ObjectIdentity = ObjectIdentity
hwDnsCompliances = _HwDnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 3, 2)
)

# Managed Objects groups

hwDnsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 3, 1, 1)
)
hwDnsExtGroup.setObjects(
      *(("HUAWEI-DNS-MIB", "hwDnsDomainName"),
        ("HUAWEI-DNS-MIB", "hwDnsIpAddress"),
        ("HUAWEI-DNS-MIB", "hwDnsTtl"),
        ("HUAWEI-DNS-MIB", "hwDnsAlias"),
        ("HUAWEI-DNS-MIB", "hwDns6DomainName"),
        ("HUAWEI-DNS-MIB", "hwDns6Ipv6Address"),
        ("HUAWEI-DNS-MIB", "hwDns6Ttl"),
        ("HUAWEI-DNS-MIB", "hwDns6Alias"),
        ("HUAWEI-DNS-MIB", "hwDdnsPolicyName"),
        ("HUAWEI-DNS-MIB", "hwDdnsIfindex"),
        ("HUAWEI-DNS-MIB", "hwService"),
        ("HUAWEI-DNS-MIB", "hwDdnsUserName"),
        ("HUAWEI-DNS-MIB", "hwDdnsFqdn"),
        ("HUAWEI-DNS-MIB", "hwServerAddr"),
        ("HUAWEI-DNS-MIB", "hwServerStatus"),
        ("HUAWEI-DNS-MIB", "hwDomainSuffix"),
        ("HUAWEI-DNS-MIB", "hwDnsProxyEnable"))
)
if mibBuilder.loadTexts:
    hwDnsExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwDnsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 194, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwDnsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DNS-MIB",
    **{"hwDnsMIB": hwDnsMIB,
       "hwDnsObjects": hwDnsObjects,
       "hwDnsHostsDynamicTable": hwDnsHostsDynamicTable,
       "hwDnsHostsDynamicEntry": hwDnsHostsDynamicEntry,
       "hwDnsDomainName": hwDnsDomainName,
       "hwDnsIpAddress": hwDnsIpAddress,
       "hwDnsTtl": hwDnsTtl,
       "hwDnsAlias": hwDnsAlias,
       "hwDns6HostsDynamicTable": hwDns6HostsDynamicTable,
       "hwDns6HostsDynamicEntry": hwDns6HostsDynamicEntry,
       "hwDns6DomainName": hwDns6DomainName,
       "hwDns6Ipv6Address": hwDns6Ipv6Address,
       "hwDns6Ttl": hwDns6Ttl,
       "hwDns6Alias": hwDns6Alias,
       "hwDdnsConfigTable": hwDdnsConfigTable,
       "hwDdnsConfigEntry": hwDdnsConfigEntry,
       "hwDdnsPolicyName": hwDdnsPolicyName,
       "hwDdnsIfindex": hwDdnsIfindex,
       "hwService": hwService,
       "hwDdnsUserName": hwDdnsUserName,
       "hwDdnsFqdn": hwDdnsFqdn,
       "hwDnsServerAddrTable": hwDnsServerAddrTable,
       "hwDnsServerAddrEntry": hwDnsServerAddrEntry,
       "hwServerAddr": hwServerAddr,
       "hwServerStatus": hwServerStatus,
       "hwDnsDomainSuffixTable": hwDnsDomainSuffixTable,
       "hwDnsDomainSuffixEntry": hwDnsDomainSuffixEntry,
       "hwDomainSuffix": hwDomainSuffix,
       "hwDnsProxyEnable": hwDnsProxyEnable,
       "hwDnsConformance": hwDnsConformance,
       "hwDnsGroups": hwDnsGroups,
       "hwDnsExtGroup": hwDnsExtGroup,
       "hwDnsCompliances": hwDnsCompliances,
       "hwDnsCompliance": hwDnsCompliance}
)
