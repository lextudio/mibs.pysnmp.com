# SNMP MIB module (ZHONE-COM-IP-STATIC-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-STATIC-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:20 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(rdIndex,) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "rdIndex")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comIpStaticRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 63)
)
comIpStaticRoute.setRevisions(
        ("2006-07-14 15:50",
         "2005-04-29 14:10",
         "2000-09-12 10:23",
         "2000-09-29 16:34")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StaticRoute_ObjectIdentity = ObjectIdentity
staticRoute = _StaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13)
)
if mibBuilder.loadTexts:
    staticRoute.setStatus("current")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1)
)
staticRouteEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteDest"),
    (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteNetMask"),
    (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteNextHop"),
    (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteIfNumber"),
    (0, "ZHONE-COM-IP-STATIC-ROUTE-MIB", "staticRouteType"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")
_StaticRouteDest_Type = IpAddress
_StaticRouteDest_Object = MibTableColumn
staticRouteDest = _StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 1),
    _StaticRouteDest_Type()
)
staticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteDest.setStatus("current")
_StaticRouteNetMask_Type = IpAddress
_StaticRouteNetMask_Object = MibTableColumn
staticRouteNetMask = _StaticRouteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 2),
    _StaticRouteNetMask_Type()
)
staticRouteNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteNetMask.setStatus("current")
_StaticRouteNextHop_Type = IpAddress
_StaticRouteNextHop_Object = MibTableColumn
staticRouteNextHop = _StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 3),
    _StaticRouteNextHop_Type()
)
staticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteNextHop.setStatus("current")
_StaticRouteIfNumber_Type = InterfaceIndexOrZero
_StaticRouteIfNumber_Object = MibTableColumn
staticRouteIfNumber = _StaticRouteIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 4),
    _StaticRouteIfNumber_Type()
)
staticRouteIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteIfNumber.setStatus("current")


class _StaticRouteMetric_Type(Unsigned32):
    """Custom type staticRouteMetric based on Unsigned32"""
    defaultValue = 2147483647


_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("current")


class _StaticRouteEnable_Type(Integer32):
    """Custom type staticRouteEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_StaticRouteEnable_Type.__name__ = "Integer32"
_StaticRouteEnable_Object = MibTableColumn
staticRouteEnable = _StaticRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 6),
    _StaticRouteEnable_Type()
)
staticRouteEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteEnable.setStatus("current")
_StaticRouteRowStatus_Type = ZhoneRowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 7),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("current")


class _StaticRouteType_Type(Integer32):
    """Custom type staticRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destinationRoute", 1),
          ("sourceRoute", 2))
    )


_StaticRouteType_Type.__name__ = "Integer32"
_StaticRouteType_Object = MibTableColumn
staticRouteType = _StaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 8),
    _StaticRouteType_Type()
)
staticRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteType.setStatus("current")


class _StaticRouteFallbackMetric_Type(Integer32):
    """Custom type staticRouteFallbackMetric based on Integer32"""
    defaultBinValue = 0


_StaticRouteFallbackMetric_Object = MibTableColumn
staticRouteFallbackMetric = _StaticRouteFallbackMetric_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 9),
    _StaticRouteFallbackMetric_Type()
)
staticRouteFallbackMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteFallbackMetric.setStatus("current")


class _StaticRoutePingInterval_Type(Unsigned32):
    """Custom type staticRoutePingInterval based on Unsigned32"""
    defaultValue = 0


_StaticRoutePingInterval_Object = MibTableColumn
staticRoutePingInterval = _StaticRoutePingInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 10),
    _StaticRoutePingInterval_Type()
)
staticRoutePingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRoutePingInterval.setStatus("current")


class _StaticRoutePingFailMax_Type(Integer32):
    """Custom type staticRoutePingFailMax based on Integer32"""
    defaultValue = 0


_StaticRoutePingFailMax_Object = MibTableColumn
staticRoutePingFailMax = _StaticRoutePingFailMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 13, 1, 1, 11),
    _StaticRoutePingFailMax_Type()
)
staticRoutePingFailMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRoutePingFailMax.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-STATIC-ROUTE-MIB",
    **{"staticRoute": staticRoute,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteDest": staticRouteDest,
       "staticRouteNetMask": staticRouteNetMask,
       "staticRouteNextHop": staticRouteNextHop,
       "staticRouteIfNumber": staticRouteIfNumber,
       "staticRouteMetric": staticRouteMetric,
       "staticRouteEnable": staticRouteEnable,
       "staticRouteRowStatus": staticRouteRowStatus,
       "staticRouteType": staticRouteType,
       "staticRouteFallbackMetric": staticRouteFallbackMetric,
       "staticRoutePingInterval": staticRoutePingInterval,
       "staticRoutePingFailMax": staticRoutePingFailMax,
       "comIpStaticRoute": comIpStaticRoute}
)
