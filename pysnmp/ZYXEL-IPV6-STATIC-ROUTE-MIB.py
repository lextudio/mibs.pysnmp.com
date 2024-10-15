# SNMP MIB module (ZYXEL-IPV6-STATIC-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-IPV6-STATIC-ROUTE-MIB
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpv6StaticRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIpv6StaticRouteSetup_ObjectIdentity = ObjectIdentity
zyxelIpv6StaticRouteSetup = _ZyxelIpv6StaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1)
)
_ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Type = Integer32
_ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Object = MibScalar
zyIpv6StaticRouteMaxNumberOfStaticRoutes = _ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 1),
    _ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Type()
)
zyIpv6StaticRouteMaxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteMaxNumberOfStaticRoutes.setStatus("current")
_ZyxelIpv6StaticRouteTable_Object = MibTable
zyxelIpv6StaticRouteTable = _ZyxelIpv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelIpv6StaticRouteTable.setStatus("current")
_ZyxelIpv6StaticRouteEntry_Object = MibTableRow
zyxelIpv6StaticRouteEntry = _ZyxelIpv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1)
)
zyxelIpv6StaticRouteEntry.setIndexNames(
    (0, "ZYXEL-IPV6-STATIC-ROUTE-MIB", "zyIpv6StaticRouteDestinationIpAddressType"),
    (0, "ZYXEL-IPV6-STATIC-ROUTE-MIB", "zyIpv6StaticRouteDestinationIpAddress"),
    (0, "ZYXEL-IPV6-STATIC-ROUTE-MIB", "zyIpv6StaticRouteDestinationAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    zyxelIpv6StaticRouteEntry.setStatus("current")
_ZyIpv6StaticRouteDestinationIpAddressType_Type = InetAddressType
_ZyIpv6StaticRouteDestinationIpAddressType_Object = MibTableColumn
zyIpv6StaticRouteDestinationIpAddressType = _ZyIpv6StaticRouteDestinationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 1),
    _ZyIpv6StaticRouteDestinationIpAddressType_Type()
)
zyIpv6StaticRouteDestinationIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteDestinationIpAddressType.setStatus("current")
_ZyIpv6StaticRouteDestinationIpAddress_Type = InetAddress
_ZyIpv6StaticRouteDestinationIpAddress_Object = MibTableColumn
zyIpv6StaticRouteDestinationIpAddress = _ZyIpv6StaticRouteDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 2),
    _ZyIpv6StaticRouteDestinationIpAddress_Type()
)
zyIpv6StaticRouteDestinationIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteDestinationIpAddress.setStatus("current")
_ZyIpv6StaticRouteDestinationAddressPrefixLength_Type = Integer32
_ZyIpv6StaticRouteDestinationAddressPrefixLength_Object = MibTableColumn
zyIpv6StaticRouteDestinationAddressPrefixLength = _ZyIpv6StaticRouteDestinationAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 3),
    _ZyIpv6StaticRouteDestinationAddressPrefixLength_Type()
)
zyIpv6StaticRouteDestinationAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteDestinationAddressPrefixLength.setStatus("current")
_ZyIpv6StaticRouteNextHopIpAddressType_Type = InetAddressType
_ZyIpv6StaticRouteNextHopIpAddressType_Object = MibTableColumn
zyIpv6StaticRouteNextHopIpAddressType = _ZyIpv6StaticRouteNextHopIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 4),
    _ZyIpv6StaticRouteNextHopIpAddressType_Type()
)
zyIpv6StaticRouteNextHopIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteNextHopIpAddressType.setStatus("current")
_ZyIpv6StaticRouteNextHopIpAddress_Type = InetAddress
_ZyIpv6StaticRouteNextHopIpAddress_Object = MibTableColumn
zyIpv6StaticRouteNextHopIpAddress = _ZyIpv6StaticRouteNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 5),
    _ZyIpv6StaticRouteNextHopIpAddress_Type()
)
zyIpv6StaticRouteNextHopIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteNextHopIpAddress.setStatus("current")
_ZyIpv6StaticRouteIfIndex_Type = Integer32
_ZyIpv6StaticRouteIfIndex_Object = MibTableColumn
zyIpv6StaticRouteIfIndex = _ZyIpv6StaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 6),
    _ZyIpv6StaticRouteIfIndex_Type()
)
zyIpv6StaticRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteIfIndex.setStatus("current")
_ZyIpv6StaticRouteRowStatus_Type = RowStatus
_ZyIpv6StaticRouteRowStatus_Object = MibTableColumn
zyIpv6StaticRouteRowStatus = _ZyIpv6StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 37, 1, 2, 1, 7),
    _ZyIpv6StaticRouteRowStatus_Type()
)
zyIpv6StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyIpv6StaticRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IPV6-STATIC-ROUTE-MIB",
    **{"zyxelIpv6StaticRoute": zyxelIpv6StaticRoute,
       "zyxelIpv6StaticRouteSetup": zyxelIpv6StaticRouteSetup,
       "zyIpv6StaticRouteMaxNumberOfStaticRoutes": zyIpv6StaticRouteMaxNumberOfStaticRoutes,
       "zyxelIpv6StaticRouteTable": zyxelIpv6StaticRouteTable,
       "zyxelIpv6StaticRouteEntry": zyxelIpv6StaticRouteEntry,
       "zyIpv6StaticRouteDestinationIpAddressType": zyIpv6StaticRouteDestinationIpAddressType,
       "zyIpv6StaticRouteDestinationIpAddress": zyIpv6StaticRouteDestinationIpAddress,
       "zyIpv6StaticRouteDestinationAddressPrefixLength": zyIpv6StaticRouteDestinationAddressPrefixLength,
       "zyIpv6StaticRouteNextHopIpAddressType": zyIpv6StaticRouteNextHopIpAddressType,
       "zyIpv6StaticRouteNextHopIpAddress": zyIpv6StaticRouteNextHopIpAddress,
       "zyIpv6StaticRouteIfIndex": zyIpv6StaticRouteIfIndex,
       "zyIpv6StaticRouteRowStatus": zyIpv6StaticRouteRowStatus}
)
