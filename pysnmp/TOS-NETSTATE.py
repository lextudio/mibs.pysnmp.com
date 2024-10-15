# SNMP MIB module (TOS-NETSTATE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOS-NETSTATE
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:38 2024
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
 Gauge,
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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge",
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(tosMib,) = mibBuilder.importSymbols(
    "TOS-SMI",
    "tosMib")


# MODULE-IDENTITY

tosMACTable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 6)
)
tosMACTable.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00")
)

tosVLANTable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 7)
)
tosVLANTable.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00")
)

tosRouteTable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8)
)
tosRouteTable.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00")
)

tosARPTable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 9)
)
tosARPTable.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00")
)

tosARPProxyTable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 10)
)
tosARPProxyTable.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TosMACEntry_Object = MibTableRow
tosMACEntry = _TosMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 6, 1)
)
tosMACEntry.setIndexNames(
    (0, "TOS-NETSTATE", "macIndex"),
)
if mibBuilder.loadTexts:
    tosMACEntry.setStatus("current")
_MacIndex_Type = Integer32
_MacIndex_Object = MibTableColumn
macIndex = _MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 6, 1, 1),
    _MacIndex_Type()
)
macIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macIndex.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 6, 1, 2),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_MacVlanID_Type = Integer32
_MacVlanID_Object = MibTableColumn
macVlanID = _MacVlanID_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 6, 1, 3),
    _MacVlanID_Type()
)
macVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVlanID.setStatus("current")
_MacDevName_Type = DisplayString
_MacDevName_Object = MibTableColumn
macDevName = _MacDevName_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 6, 1, 4),
    _MacDevName_Type()
)
macDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macDevName.setStatus("current")
_TosVLANEntry_Object = MibTableRow
tosVLANEntry = _TosVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 7, 1)
)
tosVLANEntry.setIndexNames(
    (0, "TOS-NETSTATE", "vlanIndex"),
)
if mibBuilder.loadTexts:
    tosVLANEntry.setStatus("current")
_VlanIndex_Type = Integer32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 7, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")
_VlanId_Type = Integer32
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 7, 1, 2),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_VlanStatus_Type = DisplayString
_VlanStatus_Object = MibTableColumn
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 7, 1, 3),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("current")
_VlanPorts_Type = DisplayString
_VlanPorts_Object = MibTableColumn
vlanPorts = _VlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 7, 1, 4),
    _VlanPorts_Type()
)
vlanPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPorts.setStatus("current")
_TosRouteEntry_Object = MibTableRow
tosRouteEntry = _TosRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1)
)
tosRouteEntry.setIndexNames(
    (0, "TOS-NETSTATE", "routeIndex"),
)
if mibBuilder.loadTexts:
    tosRouteEntry.setStatus("current")


class _RouteIndex_Type(Integer32):
    """Custom type routeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RouteIndex_Type.__name__ = "Integer32"
_RouteIndex_Object = MibTableColumn
routeIndex = _RouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 1),
    _RouteIndex_Type()
)
routeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeIndex.setStatus("current")
_RouteId_Type = Integer32
_RouteId_Object = MibTableColumn
routeId = _RouteId_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 2),
    _RouteId_Type()
)
routeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeId.setStatus("current")
_RouteNetSrc_Type = DisplayString
_RouteNetSrc_Object = MibTableColumn
routeNetSrc = _RouteNetSrc_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 3),
    _RouteNetSrc_Type()
)
routeNetSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeNetSrc.setStatus("current")
_RouteNetDst_Type = DisplayString
_RouteNetDst_Object = MibTableColumn
routeNetDst = _RouteNetDst_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 4),
    _RouteNetDst_Type()
)
routeNetDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeNetDst.setStatus("current")
_RouteGateway_Type = DisplayString
_RouteGateway_Object = MibTableColumn
routeGateway = _RouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 5),
    _RouteGateway_Type()
)
routeGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeGateway.setStatus("current")
_RouteFlags_Type = DisplayString
_RouteFlags_Object = MibTableColumn
routeFlags = _RouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 6),
    _RouteFlags_Type()
)
routeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeFlags.setStatus("current")
_RouteMetric_Type = Integer32
_RouteMetric_Object = MibTableColumn
routeMetric = _RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 7),
    _RouteMetric_Type()
)
routeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeMetric.setStatus("current")
_RouteIface_Type = DisplayString
_RouteIface_Object = MibTableColumn
routeIface = _RouteIface_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 8, 1, 8),
    _RouteIface_Type()
)
routeIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeIface.setStatus("current")
_TosARPEntry_Object = MibTableRow
tosARPEntry = _TosARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 9, 1)
)
tosARPEntry.setIndexNames(
    (0, "TOS-NETSTATE", "arpIndex"),
)
if mibBuilder.loadTexts:
    tosARPEntry.setStatus("current")


class _ArpIndex_Type(Integer32):
    """Custom type arpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ArpIndex_Type.__name__ = "Integer32"
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 9, 1, 1),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("current")


class _ArpDevName_Type(DisplayString):
    """Custom type arpDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArpDevName_Type.__name__ = "DisplayString"
_ArpDevName_Object = MibTableColumn
arpDevName = _ArpDevName_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 9, 1, 2),
    _ArpDevName_Type()
)
arpDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpDevName.setStatus("current")
_ArpIpAdrress_Type = DisplayString
_ArpIpAdrress_Object = MibTableColumn
arpIpAdrress = _ArpIpAdrress_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 9, 1, 3),
    _ArpIpAdrress_Type()
)
arpIpAdrress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAdrress.setStatus("current")


class _ArpMacAddress_Type(DisplayString):
    """Custom type arpMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArpMacAddress_Type.__name__ = "DisplayString"
_ArpMacAddress_Object = MibTableColumn
arpMacAddress = _ArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 9, 1, 4),
    _ArpMacAddress_Type()
)
arpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddress.setStatus("current")


class _ArpStatus_Type(DisplayString):
    """Custom type arpStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArpStatus_Type.__name__ = "DisplayString"
_ArpStatus_Object = MibTableColumn
arpStatus = _ArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 9, 1, 5),
    _ArpStatus_Type()
)
arpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatus.setStatus("current")
_TosARPProxyEntry_Object = MibTableRow
tosARPProxyEntry = _TosARPProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 10, 1)
)
tosARPProxyEntry.setIndexNames(
    (0, "TOS-NETSTATE", "arpProxyIndex"),
)
if mibBuilder.loadTexts:
    tosARPProxyEntry.setStatus("current")
_ArpProxyIndex_Type = Integer32
_ArpProxyIndex_Object = MibTableColumn
arpProxyIndex = _ArpProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 10, 1, 1),
    _ArpProxyIndex_Type()
)
arpProxyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpProxyIndex.setStatus("current")
_ArpProxyMaxIpAdrress_Type = IpAddress
_ArpProxyMaxIpAdrress_Object = MibScalar
arpProxyMaxIpAdrress = _ArpProxyMaxIpAdrress_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 10, 1, 2),
    _ArpProxyMaxIpAdrress_Type()
)
arpProxyMaxIpAdrress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpProxyMaxIpAdrress.setStatus("current")
_ArpProxyMinIpAddress_Type = IpAddress
_ArpProxyMinIpAddress_Object = MibTableColumn
arpProxyMinIpAddress = _ArpProxyMinIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 10, 1, 3),
    _ArpProxyMinIpAddress_Type()
)
arpProxyMinIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpProxyMinIpAddress.setStatus("current")


class _ArpProxyHWaddress_Type(DisplayString):
    """Custom type arpProxyHWaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArpProxyHWaddress_Type.__name__ = "DisplayString"
_ArpProxyHWaddress_Object = MibScalar
arpProxyHWaddress = _ArpProxyHWaddress_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 10, 1, 4),
    _ArpProxyHWaddress_Type()
)
arpProxyHWaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpProxyHWaddress.setStatus("current")


class _ArpProxyStat_Type(DisplayString):
    """Custom type arpProxyStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArpProxyStat_Type.__name__ = "DisplayString"
_ArpProxyStat_Object = MibTableColumn
arpProxyStat = _ArpProxyStat_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 10, 1, 5),
    _ArpProxyStat_Type()
)
arpProxyStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpProxyStat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOS-NETSTATE",
    **{"tosMACTable": tosMACTable,
       "tosMACEntry": tosMACEntry,
       "macIndex": macIndex,
       "macAddress": macAddress,
       "macVlanID": macVlanID,
       "macDevName": macDevName,
       "tosVLANTable": tosVLANTable,
       "tosVLANEntry": tosVLANEntry,
       "vlanIndex": vlanIndex,
       "vlanId": vlanId,
       "vlanStatus": vlanStatus,
       "vlanPorts": vlanPorts,
       "tosRouteTable": tosRouteTable,
       "tosRouteEntry": tosRouteEntry,
       "routeIndex": routeIndex,
       "routeId": routeId,
       "routeNetSrc": routeNetSrc,
       "routeNetDst": routeNetDst,
       "routeGateway": routeGateway,
       "routeFlags": routeFlags,
       "routeMetric": routeMetric,
       "routeIface": routeIface,
       "tosARPTable": tosARPTable,
       "tosARPEntry": tosARPEntry,
       "arpIndex": arpIndex,
       "arpDevName": arpDevName,
       "arpIpAdrress": arpIpAdrress,
       "arpMacAddress": arpMacAddress,
       "arpStatus": arpStatus,
       "tosARPProxyTable": tosARPProxyTable,
       "tosARPProxyEntry": tosARPProxyEntry,
       "arpProxyIndex": arpProxyIndex,
       "arpProxyMaxIpAdrress": arpProxyMaxIpAdrress,
       "arpProxyMinIpAddress": arpProxyMinIpAddress,
       "arpProxyHWaddress": arpProxyHWaddress,
       "arpProxyStat": arpProxyStat}
)
