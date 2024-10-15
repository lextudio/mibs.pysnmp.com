# SNMP MIB module (A3COM-HUAWEI-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:34 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cDns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97)
)
h3cDns.setRevisions(
        ("2009-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDnsObjects_ObjectIdentity = ObjectIdentity
h3cDnsObjects = _H3cDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1)
)
_H3cDnsStaticSrvIpTable_Object = MibTable
h3cDnsStaticSrvIpTable = _H3cDnsStaticSrvIpTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDnsStaticSrvIpTable.setStatus("current")
_H3cDnsStaticSrvIpEntry_Object = MibTableRow
h3cDnsStaticSrvIpEntry = _H3cDnsStaticSrvIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1)
)
h3cDnsStaticSrvIpEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpType"),
    (0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpAddr"),
)
if mibBuilder.loadTexts:
    h3cDnsStaticSrvIpEntry.setStatus("current")
_H3cDnsStaticSrvIpType_Type = InetAddressType
_H3cDnsStaticSrvIpType_Object = MibTableColumn
h3cDnsStaticSrvIpType = _H3cDnsStaticSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 1),
    _H3cDnsStaticSrvIpType_Type()
)
h3cDnsStaticSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDnsStaticSrvIpType.setStatus("current")


class _H3cDnsStaticSrvIpAddr_Type(InetAddress):
    """Custom type h3cDnsStaticSrvIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDnsStaticSrvIpAddr_Type.__name__ = "InetAddress"
_H3cDnsStaticSrvIpAddr_Object = MibTableColumn
h3cDnsStaticSrvIpAddr = _H3cDnsStaticSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 2),
    _H3cDnsStaticSrvIpAddr_Type()
)
h3cDnsStaticSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDnsStaticSrvIpAddr.setStatus("current")


class _H3cDnsStaticSrvIpPriority_Type(Integer32):
    """Custom type h3cDnsStaticSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDnsStaticSrvIpPriority_Type.__name__ = "Integer32"
_H3cDnsStaticSrvIpPriority_Object = MibTableColumn
h3cDnsStaticSrvIpPriority = _H3cDnsStaticSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 3),
    _H3cDnsStaticSrvIpPriority_Type()
)
h3cDnsStaticSrvIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDnsStaticSrvIpPriority.setStatus("current")
_H3cDnsStaticSrvIpRowStatus_Type = RowStatus
_H3cDnsStaticSrvIpRowStatus_Object = MibTableColumn
h3cDnsStaticSrvIpRowStatus = _H3cDnsStaticSrvIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 1, 1, 4),
    _H3cDnsStaticSrvIpRowStatus_Type()
)
h3cDnsStaticSrvIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDnsStaticSrvIpRowStatus.setStatus("current")
_H3cDnsDynamicSrvIpTable_Object = MibTable
h3cDnsDynamicSrvIpTable = _H3cDnsDynamicSrvIpTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDnsDynamicSrvIpTable.setStatus("current")
_H3cDnsDynamicSrvIpEntry_Object = MibTableRow
h3cDnsDynamicSrvIpEntry = _H3cDnsDynamicSrvIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1)
)
h3cDnsDynamicSrvIpEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsDynamicSrvIpType"),
    (0, "A3COM-HUAWEI-DNS-MIB", "h3cDnsDynamicSrvIpAddr"),
)
if mibBuilder.loadTexts:
    h3cDnsDynamicSrvIpEntry.setStatus("current")
_H3cDnsDynamicSrvIpType_Type = InetAddressType
_H3cDnsDynamicSrvIpType_Object = MibTableColumn
h3cDnsDynamicSrvIpType = _H3cDnsDynamicSrvIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1, 1),
    _H3cDnsDynamicSrvIpType_Type()
)
h3cDnsDynamicSrvIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDnsDynamicSrvIpType.setStatus("current")


class _H3cDnsDynamicSrvIpAddr_Type(InetAddress):
    """Custom type h3cDnsDynamicSrvIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDnsDynamicSrvIpAddr_Type.__name__ = "InetAddress"
_H3cDnsDynamicSrvIpAddr_Object = MibTableColumn
h3cDnsDynamicSrvIpAddr = _H3cDnsDynamicSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1, 2),
    _H3cDnsDynamicSrvIpAddr_Type()
)
h3cDnsDynamicSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDnsDynamicSrvIpAddr.setStatus("current")


class _H3cDnsDynamicSrvIpPriority_Type(Integer32):
    """Custom type h3cDnsDynamicSrvIpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDnsDynamicSrvIpPriority_Type.__name__ = "Integer32"
_H3cDnsDynamicSrvIpPriority_Object = MibTableColumn
h3cDnsDynamicSrvIpPriority = _H3cDnsDynamicSrvIpPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 1, 2, 1, 3),
    _H3cDnsDynamicSrvIpPriority_Type()
)
h3cDnsDynamicSrvIpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDnsDynamicSrvIpPriority.setStatus("current")
_H3cDnsMIBConformance_ObjectIdentity = ObjectIdentity
h3cDnsMIBConformance = _H3cDnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2)
)
_H3cDnsMIBCompliances_ObjectIdentity = ObjectIdentity
h3cDnsMIBCompliances = _H3cDnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 1)
)
_H3cDnsMIBGroups_ObjectIdentity = ObjectIdentity
h3cDnsMIBGroups = _H3cDnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 2)
)

# Managed Objects groups

h3cDnsStaticSrvIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 2, 1)
)
h3cDnsStaticSrvIpGroup.setObjects(
      *(("A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpPriority"),
        ("A3COM-HUAWEI-DNS-MIB", "h3cDnsStaticSrvIpRowStatus"))
)
if mibBuilder.loadTexts:
    h3cDnsStaticSrvIpGroup.setStatus("current")

h3cDnsDynamicSrvIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 2, 2)
)
h3cDnsDynamicSrvIpGroup.setObjects(
    ("A3COM-HUAWEI-DNS-MIB", "h3cDnsDynamicSrvIpPriority")
)
if mibBuilder.loadTexts:
    h3cDnsDynamicSrvIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cDnsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 97, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDnsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DNS-MIB",
    **{"h3cDns": h3cDns,
       "h3cDnsObjects": h3cDnsObjects,
       "h3cDnsStaticSrvIpTable": h3cDnsStaticSrvIpTable,
       "h3cDnsStaticSrvIpEntry": h3cDnsStaticSrvIpEntry,
       "h3cDnsStaticSrvIpType": h3cDnsStaticSrvIpType,
       "h3cDnsStaticSrvIpAddr": h3cDnsStaticSrvIpAddr,
       "h3cDnsStaticSrvIpPriority": h3cDnsStaticSrvIpPriority,
       "h3cDnsStaticSrvIpRowStatus": h3cDnsStaticSrvIpRowStatus,
       "h3cDnsDynamicSrvIpTable": h3cDnsDynamicSrvIpTable,
       "h3cDnsDynamicSrvIpEntry": h3cDnsDynamicSrvIpEntry,
       "h3cDnsDynamicSrvIpType": h3cDnsDynamicSrvIpType,
       "h3cDnsDynamicSrvIpAddr": h3cDnsDynamicSrvIpAddr,
       "h3cDnsDynamicSrvIpPriority": h3cDnsDynamicSrvIpPriority,
       "h3cDnsMIBConformance": h3cDnsMIBConformance,
       "h3cDnsMIBCompliances": h3cDnsMIBCompliances,
       "h3cDnsMIBCompliance": h3cDnsMIBCompliance,
       "h3cDnsMIBGroups": h3cDnsMIBGroups,
       "h3cDnsStaticSrvIpGroup": h3cDnsStaticSrvIpGroup,
       "h3cDnsDynamicSrvIpGroup": h3cDnsDynamicSrvIpGroup}
)
