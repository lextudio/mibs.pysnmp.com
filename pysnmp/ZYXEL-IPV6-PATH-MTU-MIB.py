# SNMP MIB module (ZYXEL-IPV6-PATH-MTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-IPV6-PATH-MTU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:07 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpv6PathMtu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPathMtuDiscoveryStatus_ObjectIdentity = ObjectIdentity
zyxelPathMtuDiscoveryStatus = _ZyxelPathMtuDiscoveryStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1)
)
_ZyxelPathMtuDiscoveryTable_Object = MibTable
zyxelPathMtuDiscoveryTable = _ZyxelPathMtuDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelPathMtuDiscoveryTable.setStatus("current")
_ZyxelPathMtuDiscoveryEntry_Object = MibTableRow
zyxelPathMtuDiscoveryEntry = _ZyxelPathMtuDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1)
)
zyxelPathMtuDiscoveryEntry.setIndexNames(
    (0, "ZYXEL-IPV6-PATH-MTU-MIB", "zyPathMtuDiscoveryDestinationIpAddressType"),
    (0, "ZYXEL-IPV6-PATH-MTU-MIB", "zyPathMtuDiscoveryDestinationIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelPathMtuDiscoveryEntry.setStatus("current")
_ZyPathMtuDiscoveryDestinationIpAddressType_Type = InetAddressType
_ZyPathMtuDiscoveryDestinationIpAddressType_Object = MibTableColumn
zyPathMtuDiscoveryDestinationIpAddressType = _ZyPathMtuDiscoveryDestinationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 1),
    _ZyPathMtuDiscoveryDestinationIpAddressType_Type()
)
zyPathMtuDiscoveryDestinationIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPathMtuDiscoveryDestinationIpAddressType.setStatus("current")
_ZyPathMtuDiscoveryDestinationIpAddress_Type = InetAddress
_ZyPathMtuDiscoveryDestinationIpAddress_Object = MibTableColumn
zyPathMtuDiscoveryDestinationIpAddress = _ZyPathMtuDiscoveryDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 2),
    _ZyPathMtuDiscoveryDestinationIpAddress_Type()
)
zyPathMtuDiscoveryDestinationIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPathMtuDiscoveryDestinationIpAddress.setStatus("current")
_ZyPathMtuDiscoveryMtu_Type = Integer32
_ZyPathMtuDiscoveryMtu_Object = MibTableColumn
zyPathMtuDiscoveryMtu = _ZyPathMtuDiscoveryMtu_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 3),
    _ZyPathMtuDiscoveryMtu_Type()
)
zyPathMtuDiscoveryMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPathMtuDiscoveryMtu.setStatus("current")
_ZyPathMtuDiscoveryExpiredTime_Type = Gauge32
_ZyPathMtuDiscoveryExpiredTime_Object = MibTableColumn
zyPathMtuDiscoveryExpiredTime = _ZyPathMtuDiscoveryExpiredTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 36, 1, 1, 1, 4),
    _ZyPathMtuDiscoveryExpiredTime_Type()
)
zyPathMtuDiscoveryExpiredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPathMtuDiscoveryExpiredTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IPV6-PATH-MTU-MIB",
    **{"zyxelIpv6PathMtu": zyxelIpv6PathMtu,
       "zyxelPathMtuDiscoveryStatus": zyxelPathMtuDiscoveryStatus,
       "zyxelPathMtuDiscoveryTable": zyxelPathMtuDiscoveryTable,
       "zyxelPathMtuDiscoveryEntry": zyxelPathMtuDiscoveryEntry,
       "zyPathMtuDiscoveryDestinationIpAddressType": zyPathMtuDiscoveryDestinationIpAddressType,
       "zyPathMtuDiscoveryDestinationIpAddress": zyPathMtuDiscoveryDestinationIpAddress,
       "zyPathMtuDiscoveryMtu": zyPathMtuDiscoveryMtu,
       "zyPathMtuDiscoveryExpiredTime": zyPathMtuDiscoveryExpiredTime}
)
