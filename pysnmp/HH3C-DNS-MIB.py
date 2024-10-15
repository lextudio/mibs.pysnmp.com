# SNMP MIB module (HH3C-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:47 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cDns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97)
)
hh3cDns.setRevisions(
        ("2009-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDnsObjects_ObjectIdentity = ObjectIdentity
hh3cDnsObjects = _Hh3cDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1)
)
_Hh3cDnsStaticSrvIpTable_Object = MibTable
hh3cDnsStaticSrvIpTable = _Hh3cDnsStaticSrvIpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDnsStaticSrvIpTable.setStatus("current")
_Hh3cDnsStaticSrvIpEntry_Object = MibTableRow
hh3cDnsStaticSrvIpEntry = _Hh3cDnsStaticSrvIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1)
)
hh3cDnsStaticSrvIpEntry.setIndexNames(
    (0, "HH3C-DNS-MIB", "hh3cDnsStaticSrvIpType"),
    (0, "HH3C-DNS-MIB", "hh3cDnsStaticSrvIpAddr"),
)
if mibBuilder.loadTexts:
    hh3cDnsStaticSrvIpEntry.setStatus("current")
_Hh3cDnsStaticSrvIpType_Type = InetAddressType
_Hh3cDnsStaticSrvIpType_Object = MibTableColumn
hh3cDnsStaticSrvIpType = _Hh3cDnsStaticSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 1),
    _Hh3cDnsStaticSrvIpType_Type()
)
hh3cDnsStaticSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDnsStaticSrvIpType.setStatus("current")


class _Hh3cDnsStaticSrvIpAddr_Type(InetAddress):
    """Custom type hh3cDnsStaticSrvIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDnsStaticSrvIpAddr_Type.__name__ = "InetAddress"
_Hh3cDnsStaticSrvIpAddr_Object = MibTableColumn
hh3cDnsStaticSrvIpAddr = _Hh3cDnsStaticSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 2),
    _Hh3cDnsStaticSrvIpAddr_Type()
)
hh3cDnsStaticSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDnsStaticSrvIpAddr.setStatus("current")


class _Hh3cDnsStaticSrvIpPriority_Type(Integer32):
    """Custom type hh3cDnsStaticSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDnsStaticSrvIpPriority_Type.__name__ = "Integer32"
_Hh3cDnsStaticSrvIpPriority_Object = MibTableColumn
hh3cDnsStaticSrvIpPriority = _Hh3cDnsStaticSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 3),
    _Hh3cDnsStaticSrvIpPriority_Type()
)
hh3cDnsStaticSrvIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDnsStaticSrvIpPriority.setStatus("current")
_Hh3cDnsStaticSrvIpRowStatus_Type = RowStatus
_Hh3cDnsStaticSrvIpRowStatus_Object = MibTableColumn
hh3cDnsStaticSrvIpRowStatus = _Hh3cDnsStaticSrvIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 1, 1, 4),
    _Hh3cDnsStaticSrvIpRowStatus_Type()
)
hh3cDnsStaticSrvIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDnsStaticSrvIpRowStatus.setStatus("current")
_Hh3cDnsDynamicSrvIpTable_Object = MibTable
hh3cDnsDynamicSrvIpTable = _Hh3cDnsDynamicSrvIpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDnsDynamicSrvIpTable.setStatus("current")
_Hh3cDnsDynamicSrvIpEntry_Object = MibTableRow
hh3cDnsDynamicSrvIpEntry = _Hh3cDnsDynamicSrvIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1)
)
hh3cDnsDynamicSrvIpEntry.setIndexNames(
    (0, "HH3C-DNS-MIB", "hh3cDnsDynamicSrvIpType"),
    (0, "HH3C-DNS-MIB", "hh3cDnsDynamicSrvIpAddr"),
)
if mibBuilder.loadTexts:
    hh3cDnsDynamicSrvIpEntry.setStatus("current")
_Hh3cDnsDynamicSrvIpType_Type = InetAddressType
_Hh3cDnsDynamicSrvIpType_Object = MibTableColumn
hh3cDnsDynamicSrvIpType = _Hh3cDnsDynamicSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1, 1),
    _Hh3cDnsDynamicSrvIpType_Type()
)
hh3cDnsDynamicSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDnsDynamicSrvIpType.setStatus("current")


class _Hh3cDnsDynamicSrvIpAddr_Type(InetAddress):
    """Custom type hh3cDnsDynamicSrvIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDnsDynamicSrvIpAddr_Type.__name__ = "InetAddress"
_Hh3cDnsDynamicSrvIpAddr_Object = MibTableColumn
hh3cDnsDynamicSrvIpAddr = _Hh3cDnsDynamicSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1, 2),
    _Hh3cDnsDynamicSrvIpAddr_Type()
)
hh3cDnsDynamicSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDnsDynamicSrvIpAddr.setStatus("current")


class _Hh3cDnsDynamicSrvIpPriority_Type(Integer32):
    """Custom type hh3cDnsDynamicSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDnsDynamicSrvIpPriority_Type.__name__ = "Integer32"
_Hh3cDnsDynamicSrvIpPriority_Object = MibTableColumn
hh3cDnsDynamicSrvIpPriority = _Hh3cDnsDynamicSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 1, 2, 1, 3),
    _Hh3cDnsDynamicSrvIpPriority_Type()
)
hh3cDnsDynamicSrvIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDnsDynamicSrvIpPriority.setStatus("current")
_Hh3cDnsMIBConformance_ObjectIdentity = ObjectIdentity
hh3cDnsMIBConformance = _Hh3cDnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 2)
)
_Hh3cDnsMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cDnsMIBCompliances = _Hh3cDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 1)
)
_Hh3cDnsMIBGroups_ObjectIdentity = ObjectIdentity
hh3cDnsMIBGroups = _Hh3cDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 2)
)

# Managed Objects groups

hh3cDnsStaticSrvIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 2, 1)
)
hh3cDnsStaticSrvIpGroup.setObjects(
      *(("HH3C-DNS-MIB", "hh3cDnsStaticSrvIpPriority"),
        ("HH3C-DNS-MIB", "hh3cDnsStaticSrvIpRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cDnsStaticSrvIpGroup.setStatus("current")

hh3cDnsDynamicSrvIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 2, 2)
)
hh3cDnsDynamicSrvIpGroup.setObjects(
    ("HH3C-DNS-MIB", "hh3cDnsDynamicSrvIpPriority")
)
if mibBuilder.loadTexts:
    hh3cDnsDynamicSrvIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DNS-MIB",
    **{"hh3cDns": hh3cDns,
       "hh3cDnsObjects": hh3cDnsObjects,
       "hh3cDnsStaticSrvIpTable": hh3cDnsStaticSrvIpTable,
       "hh3cDnsStaticSrvIpEntry": hh3cDnsStaticSrvIpEntry,
       "hh3cDnsStaticSrvIpType": hh3cDnsStaticSrvIpType,
       "hh3cDnsStaticSrvIpAddr": hh3cDnsStaticSrvIpAddr,
       "hh3cDnsStaticSrvIpPriority": hh3cDnsStaticSrvIpPriority,
       "hh3cDnsStaticSrvIpRowStatus": hh3cDnsStaticSrvIpRowStatus,
       "hh3cDnsDynamicSrvIpTable": hh3cDnsDynamicSrvIpTable,
       "hh3cDnsDynamicSrvIpEntry": hh3cDnsDynamicSrvIpEntry,
       "hh3cDnsDynamicSrvIpType": hh3cDnsDynamicSrvIpType,
       "hh3cDnsDynamicSrvIpAddr": hh3cDnsDynamicSrvIpAddr,
       "hh3cDnsDynamicSrvIpPriority": hh3cDnsDynamicSrvIpPriority,
       "hh3cDnsMIBConformance": hh3cDnsMIBConformance,
       "hh3cDnsMIBCompliances": hh3cDnsMIBCompliances,
       "hh3cDnsMIBCompliance": hh3cDnsMIBCompliance,
       "hh3cDnsMIBGroups": hh3cDnsMIBGroups,
       "hh3cDnsStaticSrvIpGroup": hh3cDnsStaticSrvIpGroup,
       "hh3cDnsDynamicSrvIpGroup": hh3cDnsDynamicSrvIpGroup}
)
