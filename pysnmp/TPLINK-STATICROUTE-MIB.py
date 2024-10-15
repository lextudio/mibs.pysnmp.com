# SNMP MIB module (TPLINK-STATICROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-STATICROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:45 2024
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

tplinkStaticRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36)
)
tplinkStaticRouteMIB.setRevisions(
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

_TplinkStaticRouteMIBObjects_ObjectIdentity = ObjectIdentity
tplinkStaticRouteMIBObjects = _TplinkStaticRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1)
)
_TpStaticRouteConfig_ObjectIdentity = ObjectIdentity
tpStaticRouteConfig = _TpStaticRouteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1)
)
_TpStaticRouteConfigTable_Object = MibTable
tpStaticRouteConfigTable = _TpStaticRouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpStaticRouteConfigTable.setStatus("current")
_TpStaticRouteConfigEntry_Object = MibTableRow
tpStaticRouteConfigEntry = _TpStaticRouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1)
)
tpStaticRouteConfigEntry.setIndexNames(
    (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemDesIp"),
    (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemMask"),
    (0, "TPLINK-STATICROUTE-MIB", "tpStaticRouteItemNextIp"),
)
if mibBuilder.loadTexts:
    tpStaticRouteConfigEntry.setStatus("current")
_TpStaticRouteItemDesIp_Type = IpAddress
_TpStaticRouteItemDesIp_Object = MibTableColumn
tpStaticRouteItemDesIp = _TpStaticRouteItemDesIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 1),
    _TpStaticRouteItemDesIp_Type()
)
tpStaticRouteItemDesIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticRouteItemDesIp.setStatus("current")
_TpStaticRouteItemMask_Type = IpAddress
_TpStaticRouteItemMask_Object = MibTableColumn
tpStaticRouteItemMask = _TpStaticRouteItemMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 2),
    _TpStaticRouteItemMask_Type()
)
tpStaticRouteItemMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticRouteItemMask.setStatus("current")
_TpStaticRouteItemNextIp_Type = IpAddress
_TpStaticRouteItemNextIp_Object = MibTableColumn
tpStaticRouteItemNextIp = _TpStaticRouteItemNextIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 3),
    _TpStaticRouteItemNextIp_Type()
)
tpStaticRouteItemNextIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticRouteItemNextIp.setStatus("current")


class _TpStaticRouteItemInterfaceName_Type(OctetString):
    """Custom type tpStaticRouteItemInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStaticRouteItemInterfaceName_Type.__name__ = "OctetString"
_TpStaticRouteItemInterfaceName_Object = MibTableColumn
tpStaticRouteItemInterfaceName = _TpStaticRouteItemInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 4),
    _TpStaticRouteItemInterfaceName_Type()
)
tpStaticRouteItemInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStaticRouteItemInterfaceName.setStatus("current")
_TpStaticRouteItemStatus_Type = TPRowStatus
_TpStaticRouteItemStatus_Object = MibTableColumn
tpStaticRouteItemStatus = _TpStaticRouteItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 1, 1, 1, 1, 5),
    _TpStaticRouteItemStatus_Type()
)
tpStaticRouteItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpStaticRouteItemStatus.setStatus("current")
_TplinkStaticRouteNotifications_ObjectIdentity = ObjectIdentity
tplinkStaticRouteNotifications = _TplinkStaticRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 36, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-STATICROUTE-MIB",
    **{"MacAddress": MacAddress,
       "tplinkStaticRouteMIB": tplinkStaticRouteMIB,
       "tplinkStaticRouteMIBObjects": tplinkStaticRouteMIBObjects,
       "tpStaticRouteConfig": tpStaticRouteConfig,
       "tpStaticRouteConfigTable": tpStaticRouteConfigTable,
       "tpStaticRouteConfigEntry": tpStaticRouteConfigEntry,
       "tpStaticRouteItemDesIp": tpStaticRouteItemDesIp,
       "tpStaticRouteItemMask": tpStaticRouteItemMask,
       "tpStaticRouteItemNextIp": tpStaticRouteItemNextIp,
       "tpStaticRouteItemInterfaceName": tpStaticRouteItemInterfaceName,
       "tpStaticRouteItemStatus": tpStaticRouteItemStatus,
       "tplinkStaticRouteNotifications": tplinkStaticRouteNotifications}
)
