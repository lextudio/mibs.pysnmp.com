# SNMP MIB module (IPV6-STATIC-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV6-STATIC-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:28 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swIPv6StaticRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_SwIPv6StaticRouteCtrl_ObjectIdentity = ObjectIdentity
swIPv6StaticRouteCtrl = _SwIPv6StaticRouteCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 1)
)
_SwIPv6StaticRouteInfo_ObjectIdentity = ObjectIdentity
swIPv6StaticRouteInfo = _SwIPv6StaticRouteInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 2)
)
_SwIPv6StaticRouteMgmt_ObjectIdentity = ObjectIdentity
swIPv6StaticRouteMgmt = _SwIPv6StaticRouteMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3)
)
_SwIPv6StaticRouteTable_Object = MibTable
swIPv6StaticRouteTable = _SwIPv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1)
)
if mibBuilder.loadTexts:
    swIPv6StaticRouteTable.setStatus("current")
_SwIPv6StaticRouteEntry_Object = MibTableRow
swIPv6StaticRouteEntry = _SwIPv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1)
)
swIPv6StaticRouteEntry.setIndexNames(
    (0, "IPV6-STATIC-ROUTE-MIB", "swIPv6StaticRouteDest"),
    (0, "IPV6-STATIC-ROUTE-MIB", "swIPv6StaticRoutePrefixLen"),
    (0, "IPV6-STATIC-ROUTE-MIB", "swIPv6StaticRouteInterfaceName"),
    (0, "IPV6-STATIC-ROUTE-MIB", "swIPv6StaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    swIPv6StaticRouteEntry.setStatus("current")
_SwIPv6StaticRouteDest_Type = Ipv6Address
_SwIPv6StaticRouteDest_Object = MibTableColumn
swIPv6StaticRouteDest = _SwIPv6StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 1),
    _SwIPv6StaticRouteDest_Type()
)
swIPv6StaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6StaticRouteDest.setStatus("current")


class _SwIPv6StaticRoutePrefixLen_Type(Integer32):
    """Custom type swIPv6StaticRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SwIPv6StaticRoutePrefixLen_Type.__name__ = "Integer32"
_SwIPv6StaticRoutePrefixLen_Object = MibTableColumn
swIPv6StaticRoutePrefixLen = _SwIPv6StaticRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 2),
    _SwIPv6StaticRoutePrefixLen_Type()
)
swIPv6StaticRoutePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6StaticRoutePrefixLen.setStatus("current")


class _SwIPv6StaticRouteInterfaceName_Type(DisplayString):
    """Custom type swIPv6StaticRouteInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwIPv6StaticRouteInterfaceName_Type.__name__ = "DisplayString"
_SwIPv6StaticRouteInterfaceName_Object = MibTableColumn
swIPv6StaticRouteInterfaceName = _SwIPv6StaticRouteInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 3),
    _SwIPv6StaticRouteInterfaceName_Type()
)
swIPv6StaticRouteInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6StaticRouteInterfaceName.setStatus("current")
_SwIPv6StaticRouteNextHop_Type = Ipv6Address
_SwIPv6StaticRouteNextHop_Object = MibTableColumn
swIPv6StaticRouteNextHop = _SwIPv6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 4),
    _SwIPv6StaticRouteNextHop_Type()
)
swIPv6StaticRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6StaticRouteNextHop.setStatus("current")


class _SwIPv6StaticRouteMetric_Type(Integer32):
    """Custom type swIPv6StaticRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwIPv6StaticRouteMetric_Type.__name__ = "Integer32"
_SwIPv6StaticRouteMetric_Object = MibTableColumn
swIPv6StaticRouteMetric = _SwIPv6StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 5),
    _SwIPv6StaticRouteMetric_Type()
)
swIPv6StaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIPv6StaticRouteMetric.setStatus("current")


class _SwIPv6StaticRouteWeight_Type(Integer32):
    """Custom type swIPv6StaticRouteWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SwIPv6StaticRouteWeight_Type.__name__ = "Integer32"
_SwIPv6StaticRouteWeight_Object = MibTableColumn
swIPv6StaticRouteWeight = _SwIPv6StaticRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 6),
    _SwIPv6StaticRouteWeight_Type()
)
swIPv6StaticRouteWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIPv6StaticRouteWeight.setStatus("current")
_SwIPv6StaticProtocol_Type = DisplayString
_SwIPv6StaticProtocol_Object = MibTableColumn
swIPv6StaticProtocol = _SwIPv6StaticProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 7),
    _SwIPv6StaticProtocol_Type()
)
swIPv6StaticProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6StaticProtocol.setStatus("current")
_SwIPv6StaticRouteStatus_Type = RowStatus
_SwIPv6StaticRouteStatus_Object = MibTableColumn
swIPv6StaticRouteStatus = _SwIPv6StaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 8),
    _SwIPv6StaticRouteStatus_Type()
)
swIPv6StaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIPv6StaticRouteStatus.setStatus("current")


class _SwIPv6StaticRouteBkupState_Type(Integer32):
    """Custom type swIPv6StaticRouteBkupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("none", 3),
          ("primary", 1))
    )


_SwIPv6StaticRouteBkupState_Type.__name__ = "Integer32"
_SwIPv6StaticRouteBkupState_Object = MibTableColumn
swIPv6StaticRouteBkupState = _SwIPv6StaticRouteBkupState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 3, 1, 1, 9),
    _SwIPv6StaticRouteBkupState_Type()
)
swIPv6StaticRouteBkupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIPv6StaticRouteBkupState.setStatus("current")
_SwIPv6NeighborCacheMgmt_ObjectIdentity = ObjectIdentity
swIPv6NeighborCacheMgmt = _SwIPv6NeighborCacheMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4)
)
_SwIPv6NeighborCacheTable_Object = MibTable
swIPv6NeighborCacheTable = _SwIPv6NeighborCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 1)
)
if mibBuilder.loadTexts:
    swIPv6NeighborCacheTable.setStatus("current")
_SwIPv6NeighborCacheEntry_Object = MibTableRow
swIPv6NeighborCacheEntry = _SwIPv6NeighborCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 1, 1)
)
swIPv6NeighborCacheEntry.setIndexNames(
    (0, "IPV6-STATIC-ROUTE-MIB", "swIPv6NeighborCacheIPv6Address"),
    (0, "IPV6-STATIC-ROUTE-MIB", "swIPv6NeighborCacheMacAddress"),
    (0, "IPV6-STATIC-ROUTE-MIB", "swIPv6NeighborCacheInterfaceName"),
)
if mibBuilder.loadTexts:
    swIPv6NeighborCacheEntry.setStatus("current")
_SwIPv6NeighborCacheIPv6Address_Type = Ipv6Address
_SwIPv6NeighborCacheIPv6Address_Object = MibTableColumn
swIPv6NeighborCacheIPv6Address = _SwIPv6NeighborCacheIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 1, 1, 1),
    _SwIPv6NeighborCacheIPv6Address_Type()
)
swIPv6NeighborCacheIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6NeighborCacheIPv6Address.setStatus("current")
_SwIPv6NeighborCacheMacAddress_Type = MacAddress
_SwIPv6NeighborCacheMacAddress_Object = MibTableColumn
swIPv6NeighborCacheMacAddress = _SwIPv6NeighborCacheMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 1, 1, 2),
    _SwIPv6NeighborCacheMacAddress_Type()
)
swIPv6NeighborCacheMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6NeighborCacheMacAddress.setStatus("current")


class _SwIPv6NeighborCacheInterfaceName_Type(DisplayString):
    """Custom type swIPv6NeighborCacheInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwIPv6NeighborCacheInterfaceName_Type.__name__ = "DisplayString"
_SwIPv6NeighborCacheInterfaceName_Object = MibTableColumn
swIPv6NeighborCacheInterfaceName = _SwIPv6NeighborCacheInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 1, 1, 3),
    _SwIPv6NeighborCacheInterfaceName_Type()
)
swIPv6NeighborCacheInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6NeighborCacheInterfaceName.setStatus("current")


class _SwIPv6NeighborCacheReachState_Type(Integer32):
    """Custom type swIPv6NeighborCacheReachState based on Integer32"""
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
        *(("delay", 4),
          ("incomplete", 1),
          ("probe", 5),
          ("reachable", 2),
          ("stale", 3),
          ("static", 6))
    )


_SwIPv6NeighborCacheReachState_Type.__name__ = "Integer32"
_SwIPv6NeighborCacheReachState_Object = MibTableColumn
swIPv6NeighborCacheReachState = _SwIPv6NeighborCacheReachState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 1, 1, 4),
    _SwIPv6NeighborCacheReachState_Type()
)
swIPv6NeighborCacheReachState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIPv6NeighborCacheReachState.setStatus("current")
_SwIPv6NeighborCacheRouteStatus_Type = RowStatus
_SwIPv6NeighborCacheRouteStatus_Object = MibTableColumn
swIPv6NeighborCacheRouteStatus = _SwIPv6NeighborCacheRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 1, 1, 5),
    _SwIPv6NeighborCacheRouteStatus_Type()
)
swIPv6NeighborCacheRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIPv6NeighborCacheRouteStatus.setStatus("current")


class _SwIPv6NeighborCacheDeleteAction_Type(Integer32):
    """Custom type swIPv6NeighborCacheDeleteAction based on Integer32"""
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
        *(("all", 1),
          ("dynamic", 3),
          ("other", 4),
          ("static", 2))
    )


_SwIPv6NeighborCacheDeleteAction_Type.__name__ = "Integer32"
_SwIPv6NeighborCacheDeleteAction_Object = MibScalar
swIPv6NeighborCacheDeleteAction = _SwIPv6NeighborCacheDeleteAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 26, 4, 2),
    _SwIPv6NeighborCacheDeleteAction_Type()
)
swIPv6NeighborCacheDeleteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIPv6NeighborCacheDeleteAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV6-STATIC-ROUTE-MIB",
    **{"Ipv6Address": Ipv6Address,
       "swIPv6StaticRouteMIB": swIPv6StaticRouteMIB,
       "swIPv6StaticRouteCtrl": swIPv6StaticRouteCtrl,
       "swIPv6StaticRouteInfo": swIPv6StaticRouteInfo,
       "swIPv6StaticRouteMgmt": swIPv6StaticRouteMgmt,
       "swIPv6StaticRouteTable": swIPv6StaticRouteTable,
       "swIPv6StaticRouteEntry": swIPv6StaticRouteEntry,
       "swIPv6StaticRouteDest": swIPv6StaticRouteDest,
       "swIPv6StaticRoutePrefixLen": swIPv6StaticRoutePrefixLen,
       "swIPv6StaticRouteInterfaceName": swIPv6StaticRouteInterfaceName,
       "swIPv6StaticRouteNextHop": swIPv6StaticRouteNextHop,
       "swIPv6StaticRouteMetric": swIPv6StaticRouteMetric,
       "swIPv6StaticRouteWeight": swIPv6StaticRouteWeight,
       "swIPv6StaticProtocol": swIPv6StaticProtocol,
       "swIPv6StaticRouteStatus": swIPv6StaticRouteStatus,
       "swIPv6StaticRouteBkupState": swIPv6StaticRouteBkupState,
       "swIPv6NeighborCacheMgmt": swIPv6NeighborCacheMgmt,
       "swIPv6NeighborCacheTable": swIPv6NeighborCacheTable,
       "swIPv6NeighborCacheEntry": swIPv6NeighborCacheEntry,
       "swIPv6NeighborCacheIPv6Address": swIPv6NeighborCacheIPv6Address,
       "swIPv6NeighborCacheMacAddress": swIPv6NeighborCacheMacAddress,
       "swIPv6NeighborCacheInterfaceName": swIPv6NeighborCacheInterfaceName,
       "swIPv6NeighborCacheReachState": swIPv6NeighborCacheReachState,
       "swIPv6NeighborCacheRouteStatus": swIPv6NeighborCacheRouteStatus,
       "swIPv6NeighborCacheDeleteAction": swIPv6NeighborCacheDeleteAction}
)
