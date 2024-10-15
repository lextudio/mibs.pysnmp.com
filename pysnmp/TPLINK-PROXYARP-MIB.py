# SNMP MIB module (TPLINK-PROXYARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PROXYARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:34 2024
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


# MODULE-IDENTITY

tplinkProxyArpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37)
)
tplinkProxyArpMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkProxyArpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkProxyArpMIBObjects = _TplinkProxyArpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1)
)
_TpProxyArpConfig_ObjectIdentity = ObjectIdentity
tpProxyArpConfig = _TpProxyArpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1)
)
_TpProxyArpTable_Object = MibTable
tpProxyArpTable = _TpProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1)
)
if mibBuilder.loadTexts:
    tpProxyArpTable.setStatus("current")
_TpProxyArpEntry_Object = MibTableRow
tpProxyArpEntry = _TpProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1)
)
tpProxyArpEntry.setIndexNames(
    (0, "TPLINK-PROXYARP-MIB", "tpProxyArpVlanId"),
)
if mibBuilder.loadTexts:
    tpProxyArpEntry.setStatus("current")


class _TpProxyArpVlanId_Type(Integer32):
    """Custom type tpProxyArpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpProxyArpVlanId_Type.__name__ = "Integer32"
_TpProxyArpVlanId_Object = MibTableColumn
tpProxyArpVlanId = _TpProxyArpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 1),
    _TpProxyArpVlanId_Type()
)
tpProxyArpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpProxyArpVlanId.setStatus("current")
_TpProxyArpIpAddr_Type = IpAddress
_TpProxyArpIpAddr_Object = MibTableColumn
tpProxyArpIpAddr = _TpProxyArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 2),
    _TpProxyArpIpAddr_Type()
)
tpProxyArpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpProxyArpIpAddr.setStatus("current")
_TpProxyArpIpMask_Type = IpAddress
_TpProxyArpIpMask_Object = MibTableColumn
tpProxyArpIpMask = _TpProxyArpIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 3),
    _TpProxyArpIpMask_Type()
)
tpProxyArpIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpProxyArpIpMask.setStatus("current")


class _TpProxyArpInterfaceName_Type(OctetString):
    """Custom type tpProxyArpInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TpProxyArpInterfaceName_Type.__name__ = "OctetString"
_TpProxyArpInterfaceName_Object = MibTableColumn
tpProxyArpInterfaceName = _TpProxyArpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 4),
    _TpProxyArpInterfaceName_Type()
)
tpProxyArpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpProxyArpInterfaceName.setStatus("current")


class _TpProxyArpEnable_Type(Integer32):
    """Custom type tpProxyArpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpProxyArpEnable_Type.__name__ = "Integer32"
_TpProxyArpEnable_Object = MibTableColumn
tpProxyArpEnable = _TpProxyArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 5),
    _TpProxyArpEnable_Type()
)
tpProxyArpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpProxyArpEnable.setStatus("current")
_TplinkProxyArpNotifications_ObjectIdentity = ObjectIdentity
tplinkProxyArpNotifications = _TplinkProxyArpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 37, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PROXYARP-MIB",
    **{"tplinkProxyArpMIB": tplinkProxyArpMIB,
       "tplinkProxyArpMIBObjects": tplinkProxyArpMIBObjects,
       "tpProxyArpConfig": tpProxyArpConfig,
       "tpProxyArpTable": tpProxyArpTable,
       "tpProxyArpEntry": tpProxyArpEntry,
       "tpProxyArpVlanId": tpProxyArpVlanId,
       "tpProxyArpIpAddr": tpProxyArpIpAddr,
       "tpProxyArpIpMask": tpProxyArpIpMask,
       "tpProxyArpInterfaceName": tpProxyArpInterfaceName,
       "tpProxyArpEnable": tpProxyArpEnable,
       "tplinkProxyArpNotifications": tplinkProxyArpNotifications}
)
