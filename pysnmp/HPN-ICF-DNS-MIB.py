# SNMP MIB module (HPN-ICF-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:46 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfDns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97)
)
hpnicfDns.setRevisions(
        ("2009-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDnsObjects_ObjectIdentity = ObjectIdentity
hpnicfDnsObjects = _HpnicfDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1)
)
_HpnicfDnsStaticSrvIpTable_Object = MibTable
hpnicfDnsStaticSrvIpTable = _HpnicfDnsStaticSrvIpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDnsStaticSrvIpTable.setStatus("current")
_HpnicfDnsStaticSrvIpEntry_Object = MibTableRow
hpnicfDnsStaticSrvIpEntry = _HpnicfDnsStaticSrvIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 1, 1)
)
hpnicfDnsStaticSrvIpEntry.setIndexNames(
    (0, "HPN-ICF-DNS-MIB", "hpnicfDnsStaticSrvIpType"),
    (0, "HPN-ICF-DNS-MIB", "hpnicfDnsStaticSrvIpAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDnsStaticSrvIpEntry.setStatus("current")
_HpnicfDnsStaticSrvIpType_Type = InetAddressType
_HpnicfDnsStaticSrvIpType_Object = MibTableColumn
hpnicfDnsStaticSrvIpType = _HpnicfDnsStaticSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 1, 1, 1),
    _HpnicfDnsStaticSrvIpType_Type()
)
hpnicfDnsStaticSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDnsStaticSrvIpType.setStatus("current")


class _HpnicfDnsStaticSrvIpAddr_Type(InetAddress):
    """Custom type hpnicfDnsStaticSrvIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfDnsStaticSrvIpAddr_Type.__name__ = "InetAddress"
_HpnicfDnsStaticSrvIpAddr_Object = MibTableColumn
hpnicfDnsStaticSrvIpAddr = _HpnicfDnsStaticSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 1, 1, 2),
    _HpnicfDnsStaticSrvIpAddr_Type()
)
hpnicfDnsStaticSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDnsStaticSrvIpAddr.setStatus("current")


class _HpnicfDnsStaticSrvIpPriority_Type(Integer32):
    """Custom type hpnicfDnsStaticSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDnsStaticSrvIpPriority_Type.__name__ = "Integer32"
_HpnicfDnsStaticSrvIpPriority_Object = MibTableColumn
hpnicfDnsStaticSrvIpPriority = _HpnicfDnsStaticSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 1, 1, 3),
    _HpnicfDnsStaticSrvIpPriority_Type()
)
hpnicfDnsStaticSrvIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDnsStaticSrvIpPriority.setStatus("current")
_HpnicfDnsStaticSrvIpRowStatus_Type = RowStatus
_HpnicfDnsStaticSrvIpRowStatus_Object = MibTableColumn
hpnicfDnsStaticSrvIpRowStatus = _HpnicfDnsStaticSrvIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 1, 1, 4),
    _HpnicfDnsStaticSrvIpRowStatus_Type()
)
hpnicfDnsStaticSrvIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDnsStaticSrvIpRowStatus.setStatus("current")
_HpnicfDnsDynamicSrvIpTable_Object = MibTable
hpnicfDnsDynamicSrvIpTable = _HpnicfDnsDynamicSrvIpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDnsDynamicSrvIpTable.setStatus("current")
_HpnicfDnsDynamicSrvIpEntry_Object = MibTableRow
hpnicfDnsDynamicSrvIpEntry = _HpnicfDnsDynamicSrvIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 2, 1)
)
hpnicfDnsDynamicSrvIpEntry.setIndexNames(
    (0, "HPN-ICF-DNS-MIB", "hpnicfDnsDynamicSrvIpType"),
    (0, "HPN-ICF-DNS-MIB", "hpnicfDnsDynamicSrvIpAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDnsDynamicSrvIpEntry.setStatus("current")
_HpnicfDnsDynamicSrvIpType_Type = InetAddressType
_HpnicfDnsDynamicSrvIpType_Object = MibTableColumn
hpnicfDnsDynamicSrvIpType = _HpnicfDnsDynamicSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 2, 1, 1),
    _HpnicfDnsDynamicSrvIpType_Type()
)
hpnicfDnsDynamicSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDnsDynamicSrvIpType.setStatus("current")


class _HpnicfDnsDynamicSrvIpAddr_Type(InetAddress):
    """Custom type hpnicfDnsDynamicSrvIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfDnsDynamicSrvIpAddr_Type.__name__ = "InetAddress"
_HpnicfDnsDynamicSrvIpAddr_Object = MibTableColumn
hpnicfDnsDynamicSrvIpAddr = _HpnicfDnsDynamicSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 2, 1, 2),
    _HpnicfDnsDynamicSrvIpAddr_Type()
)
hpnicfDnsDynamicSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDnsDynamicSrvIpAddr.setStatus("current")


class _HpnicfDnsDynamicSrvIpPriority_Type(Integer32):
    """Custom type hpnicfDnsDynamicSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDnsDynamicSrvIpPriority_Type.__name__ = "Integer32"
_HpnicfDnsDynamicSrvIpPriority_Object = MibTableColumn
hpnicfDnsDynamicSrvIpPriority = _HpnicfDnsDynamicSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 1, 2, 1, 3),
    _HpnicfDnsDynamicSrvIpPriority_Type()
)
hpnicfDnsDynamicSrvIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDnsDynamicSrvIpPriority.setStatus("current")
_HpnicfDnsMIBConformance_ObjectIdentity = ObjectIdentity
hpnicfDnsMIBConformance = _HpnicfDnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 2)
)
_HpnicfDnsMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfDnsMIBCompliances = _HpnicfDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 2, 1)
)
_HpnicfDnsMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfDnsMIBGroups = _HpnicfDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 2, 2)
)

# Managed Objects groups

hpnicfDnsStaticSrvIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 2, 2, 1)
)
hpnicfDnsStaticSrvIpGroup.setObjects(
      *(("HPN-ICF-DNS-MIB", "hpnicfDnsStaticSrvIpPriority"),
        ("HPN-ICF-DNS-MIB", "hpnicfDnsStaticSrvIpRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfDnsStaticSrvIpGroup.setStatus("current")

hpnicfDnsDynamicSrvIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 2, 2, 2)
)
hpnicfDnsDynamicSrvIpGroup.setObjects(
    ("HPN-ICF-DNS-MIB", "hpnicfDnsDynamicSrvIpPriority")
)
if mibBuilder.loadTexts:
    hpnicfDnsDynamicSrvIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DNS-MIB",
    **{"hpnicfDns": hpnicfDns,
       "hpnicfDnsObjects": hpnicfDnsObjects,
       "hpnicfDnsStaticSrvIpTable": hpnicfDnsStaticSrvIpTable,
       "hpnicfDnsStaticSrvIpEntry": hpnicfDnsStaticSrvIpEntry,
       "hpnicfDnsStaticSrvIpType": hpnicfDnsStaticSrvIpType,
       "hpnicfDnsStaticSrvIpAddr": hpnicfDnsStaticSrvIpAddr,
       "hpnicfDnsStaticSrvIpPriority": hpnicfDnsStaticSrvIpPriority,
       "hpnicfDnsStaticSrvIpRowStatus": hpnicfDnsStaticSrvIpRowStatus,
       "hpnicfDnsDynamicSrvIpTable": hpnicfDnsDynamicSrvIpTable,
       "hpnicfDnsDynamicSrvIpEntry": hpnicfDnsDynamicSrvIpEntry,
       "hpnicfDnsDynamicSrvIpType": hpnicfDnsDynamicSrvIpType,
       "hpnicfDnsDynamicSrvIpAddr": hpnicfDnsDynamicSrvIpAddr,
       "hpnicfDnsDynamicSrvIpPriority": hpnicfDnsDynamicSrvIpPriority,
       "hpnicfDnsMIBConformance": hpnicfDnsMIBConformance,
       "hpnicfDnsMIBCompliances": hpnicfDnsMIBCompliances,
       "hpnicfDnsMIBCompliance": hpnicfDnsMIBCompliance,
       "hpnicfDnsMIBGroups": hpnicfDnsMIBGroups,
       "hpnicfDnsStaticSrvIpGroup": hpnicfDnsStaticSrvIpGroup,
       "hpnicfDnsDynamicSrvIpGroup": hpnicfDnsDynamicSrvIpGroup}
)
