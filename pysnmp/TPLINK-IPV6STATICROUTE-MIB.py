# SNMP MIB module (TPLINK-IPV6STATICROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-IPV6STATICROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:13 2024
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkIPv6StaticRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53)
)
tplinkIPv6StaticRouteMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIPv6StaticRouteMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIPv6StaticRouteMIBObjects = _TplinkIPv6StaticRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1)
)
_TpIPv6StaticRouteConfig_ObjectIdentity = ObjectIdentity
tpIPv6StaticRouteConfig = _TpIPv6StaticRouteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1)
)
_TpIPv6StaticRouteConfigTable_Object = MibTable
tpIPv6StaticRouteConfigTable = _TpIPv6StaticRouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpIPv6StaticRouteConfigTable.setStatus("current")
_TpIPv6StaticRouteConfigEntry_Object = MibTableRow
tpIPv6StaticRouteConfigEntry = _TpIPv6StaticRouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1)
)
tpIPv6StaticRouteConfigEntry.setIndexNames(
    (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemDesIp"),
    (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemPrefixLen"),
    (0, "TPLINK-IPV6STATICROUTE-MIB", "tpIPv6StaticRouteItemNexthop"),
)
if mibBuilder.loadTexts:
    tpIPv6StaticRouteConfigEntry.setStatus("current")
_TpIPv6StaticRouteItemDesIp_Type = InetAddress
_TpIPv6StaticRouteItemDesIp_Object = MibTableColumn
tpIPv6StaticRouteItemDesIp = _TpIPv6StaticRouteItemDesIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 1),
    _TpIPv6StaticRouteItemDesIp_Type()
)
tpIPv6StaticRouteItemDesIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIPv6StaticRouteItemDesIp.setStatus("current")


class _TpIPv6StaticRouteItemPrefixLen_Type(Integer32):
    """Custom type tpIPv6StaticRouteItemPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TpIPv6StaticRouteItemPrefixLen_Type.__name__ = "Integer32"
_TpIPv6StaticRouteItemPrefixLen_Object = MibTableColumn
tpIPv6StaticRouteItemPrefixLen = _TpIPv6StaticRouteItemPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 2),
    _TpIPv6StaticRouteItemPrefixLen_Type()
)
tpIPv6StaticRouteItemPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIPv6StaticRouteItemPrefixLen.setStatus("current")
_TpIPv6StaticRouteItemNexthop_Type = InetAddress
_TpIPv6StaticRouteItemNexthop_Object = MibTableColumn
tpIPv6StaticRouteItemNexthop = _TpIPv6StaticRouteItemNexthop_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 3),
    _TpIPv6StaticRouteItemNexthop_Type()
)
tpIPv6StaticRouteItemNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6StaticRouteItemNexthop.setStatus("current")


class _TpIPv6StaticRouteItemInterfaceName_Type(OctetString):
    """Custom type tpIPv6StaticRouteItemInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpIPv6StaticRouteItemInterfaceName_Type.__name__ = "OctetString"
_TpIPv6StaticRouteItemInterfaceName_Object = MibTableColumn
tpIPv6StaticRouteItemInterfaceName = _TpIPv6StaticRouteItemInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 4),
    _TpIPv6StaticRouteItemInterfaceName_Type()
)
tpIPv6StaticRouteItemInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpIPv6StaticRouteItemInterfaceName.setStatus("current")
_TpIPv6StaticRouteItemStatus_Type = TPRowStatus
_TpIPv6StaticRouteItemStatus_Object = MibTableColumn
tpIPv6StaticRouteItemStatus = _TpIPv6StaticRouteItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 1, 1, 1, 1, 5),
    _TpIPv6StaticRouteItemStatus_Type()
)
tpIPv6StaticRouteItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIPv6StaticRouteItemStatus.setStatus("current")
_TplinkIPv6StaticRouteNotifications_ObjectIdentity = ObjectIdentity
tplinkIPv6StaticRouteNotifications = _TplinkIPv6StaticRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 53, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPV6STATICROUTE-MIB",
    **{"MacAddress": MacAddress,
       "tplinkIPv6StaticRouteMIB": tplinkIPv6StaticRouteMIB,
       "tplinkIPv6StaticRouteMIBObjects": tplinkIPv6StaticRouteMIBObjects,
       "tpIPv6StaticRouteConfig": tpIPv6StaticRouteConfig,
       "tpIPv6StaticRouteConfigTable": tpIPv6StaticRouteConfigTable,
       "tpIPv6StaticRouteConfigEntry": tpIPv6StaticRouteConfigEntry,
       "tpIPv6StaticRouteItemDesIp": tpIPv6StaticRouteItemDesIp,
       "tpIPv6StaticRouteItemPrefixLen": tpIPv6StaticRouteItemPrefixLen,
       "tpIPv6StaticRouteItemNexthop": tpIPv6StaticRouteItemNexthop,
       "tpIPv6StaticRouteItemInterfaceName": tpIPv6StaticRouteItemInterfaceName,
       "tpIPv6StaticRouteItemStatus": tpIPv6StaticRouteItemStatus,
       "tplinkIPv6StaticRouteNotifications": tplinkIPv6StaticRouteNotifications}
)
