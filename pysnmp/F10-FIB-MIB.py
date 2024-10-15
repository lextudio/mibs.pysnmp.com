# SNMP MIB module (F10-FIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-FIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:21 2024
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

(chSysCardNumber,) = mibBuilder.importSymbols(
    "F10-CHASSIS-MIB",
    "chSysCardNumber")

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

f10IpForwardMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9)
)
f10IpForwardMib.setRevisions(
        ("2011-07-08 12:00",
         "2007-09-14 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10IpForwardMibObjects_ObjectIdentity = ObjectIdentity
f10IpForwardMibObjects = _F10IpForwardMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1)
)
_F10IpForwardVersionTable_Object = MibTable
f10IpForwardVersionTable = _F10IpForwardVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    f10IpForwardVersionTable.setStatus("current")
_F10IpForwardVersionEntry_Object = MibTableRow
f10IpForwardVersionEntry = _F10IpForwardVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1)
)
f10IpForwardVersionEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysCardNumber"),
    (0, "F10-FIB-MIB", "f10IpForwardAddrFamily"),
)
if mibBuilder.loadTexts:
    f10IpForwardVersionEntry.setStatus("current")
_F10IpForwardAddrFamily_Type = InetAddressType
_F10IpForwardAddrFamily_Object = MibTableColumn
f10IpForwardAddrFamily = _F10IpForwardAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1, 1),
    _F10IpForwardAddrFamily_Type()
)
f10IpForwardAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10IpForwardAddrFamily.setStatus("current")
_F10IpForwardVersion_Type = Counter64
_F10IpForwardVersion_Object = MibTableColumn
f10IpForwardVersion = _F10IpForwardVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1, 2),
    _F10IpForwardVersion_Type()
)
f10IpForwardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpForwardVersion.setStatus("current")
_F10IpForwardTable_Object = MibTable
f10IpForwardTable = _F10IpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2)
)
if mibBuilder.loadTexts:
    f10IpForwardTable.setStatus("deprecated")
_F10IpForwardEntry_Object = MibTableRow
f10IpForwardEntry = _F10IpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1)
)
f10IpForwardEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysCardNumber"),
    (0, "F10-FIB-MIB", "f10IpforwardDest"),
    (0, "F10-FIB-MIB", "f10IpforwardMask"),
    (0, "F10-FIB-MIB", "f10IpforwardNextHop"),
    (0, "F10-FIB-MIB", "f10IpforwardFirstHop"),
)
if mibBuilder.loadTexts:
    f10IpForwardEntry.setStatus("deprecated")
_F10IpforwardDest_Type = IpAddress
_F10IpforwardDest_Object = MibTableColumn
f10IpforwardDest = _F10IpforwardDest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 1),
    _F10IpforwardDest_Type()
)
f10IpforwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardDest.setStatus("deprecated")
_F10IpforwardMask_Type = IpAddress
_F10IpforwardMask_Object = MibTableColumn
f10IpforwardMask = _F10IpforwardMask_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 2),
    _F10IpforwardMask_Type()
)
f10IpforwardMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardMask.setStatus("deprecated")
_F10IpforwardNextHop_Type = IpAddress
_F10IpforwardNextHop_Object = MibTableColumn
f10IpforwardNextHop = _F10IpforwardNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 3),
    _F10IpforwardNextHop_Type()
)
f10IpforwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardNextHop.setStatus("deprecated")
_F10IpforwardFirstHop_Type = IpAddress
_F10IpforwardFirstHop_Object = MibTableColumn
f10IpforwardFirstHop = _F10IpforwardFirstHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 4),
    _F10IpforwardFirstHop_Type()
)
f10IpforwardFirstHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardFirstHop.setStatus("deprecated")
_F10IpforwardIfIndex_Type = Integer32
_F10IpforwardIfIndex_Object = MibTableColumn
f10IpforwardIfIndex = _F10IpforwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 5),
    _F10IpforwardIfIndex_Type()
)
f10IpforwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardIfIndex.setStatus("deprecated")
_F10IpforwardMacAddress_Type = MacAddress
_F10IpforwardMacAddress_Object = MibTableColumn
f10IpforwardMacAddress = _F10IpforwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 6),
    _F10IpforwardMacAddress_Type()
)
f10IpforwardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardMacAddress.setStatus("deprecated")


class _F10IpforwardEgressPort_Type(OctetString):
    """Custom type f10IpforwardEgressPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F10IpforwardEgressPort_Type.__name__ = "OctetString"
_F10IpforwardEgressPort_Object = MibTableColumn
f10IpforwardEgressPort = _F10IpforwardEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 7),
    _F10IpforwardEgressPort_Type()
)
f10IpforwardEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardEgressPort.setStatus("deprecated")
_F10IpforwardCamIndex_Type = Integer32
_F10IpforwardCamIndex_Object = MibTableColumn
f10IpforwardCamIndex = _F10IpforwardCamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 8),
    _F10IpforwardCamIndex_Type()
)
f10IpforwardCamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10IpforwardCamIndex.setStatus("deprecated")
_F10InetCidrIpv4RouteNumber_Type = Gauge32
_F10InetCidrIpv4RouteNumber_Object = MibScalar
f10InetCidrIpv4RouteNumber = _F10InetCidrIpv4RouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 3),
    _F10InetCidrIpv4RouteNumber_Type()
)
f10InetCidrIpv4RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InetCidrIpv4RouteNumber.setStatus("current")
_F10InetCidrIpv6RouteNumber_Type = Gauge32
_F10InetCidrIpv6RouteNumber_Object = MibScalar
f10InetCidrIpv6RouteNumber = _F10InetCidrIpv6RouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 4),
    _F10InetCidrIpv6RouteNumber_Type()
)
f10InetCidrIpv6RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InetCidrIpv6RouteNumber.setStatus("current")
_F10InetCidrRouteTable_Object = MibTable
f10InetCidrRouteTable = _F10InetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5)
)
if mibBuilder.loadTexts:
    f10InetCidrRouteTable.setStatus("current")
_F10InetCidrRouteTableEntry_Object = MibTableRow
f10InetCidrRouteTableEntry = _F10InetCidrRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1)
)
f10InetCidrRouteTableEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysCardNumber"),
    (0, "F10-FIB-MIB", "f10InetCidrRouteDestType"),
    (0, "F10-FIB-MIB", "f10InetCidrRouteDest"),
    (0, "F10-FIB-MIB", "f10InetCidrRoutePfxLen"),
    (0, "F10-FIB-MIB", "f10InetCidrRouteNextHopType"),
    (0, "F10-FIB-MIB", "f10InetCidrRouteNextHop"),
    (0, "F10-FIB-MIB", "f10InetCidrRouteFirstHopType"),
    (0, "F10-FIB-MIB", "f10InetCidrRouteFirstHop"),
)
if mibBuilder.loadTexts:
    f10InetCidrRouteTableEntry.setStatus("current")
_F10InetCidrRouteDestType_Type = InetAddressType
_F10InetCidrRouteDestType_Object = MibTableColumn
f10InetCidrRouteDestType = _F10InetCidrRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 1),
    _F10InetCidrRouteDestType_Type()
)
f10InetCidrRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10InetCidrRouteDestType.setStatus("current")
_F10InetCidrRouteDest_Type = InetAddress
_F10InetCidrRouteDest_Object = MibTableColumn
f10InetCidrRouteDest = _F10InetCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 2),
    _F10InetCidrRouteDest_Type()
)
f10InetCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10InetCidrRouteDest.setStatus("current")
_F10InetCidrRoutePfxLen_Type = InetAddressPrefixLength
_F10InetCidrRoutePfxLen_Object = MibTableColumn
f10InetCidrRoutePfxLen = _F10InetCidrRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 3),
    _F10InetCidrRoutePfxLen_Type()
)
f10InetCidrRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10InetCidrRoutePfxLen.setStatus("current")
_F10InetCidrRouteNextHopType_Type = InetAddressType
_F10InetCidrRouteNextHopType_Object = MibTableColumn
f10InetCidrRouteNextHopType = _F10InetCidrRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 4),
    _F10InetCidrRouteNextHopType_Type()
)
f10InetCidrRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10InetCidrRouteNextHopType.setStatus("current")
_F10InetCidrRouteNextHop_Type = InetAddress
_F10InetCidrRouteNextHop_Object = MibTableColumn
f10InetCidrRouteNextHop = _F10InetCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 5),
    _F10InetCidrRouteNextHop_Type()
)
f10InetCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10InetCidrRouteNextHop.setStatus("current")
_F10InetCidrRouteFirstHopType_Type = InetAddressType
_F10InetCidrRouteFirstHopType_Object = MibTableColumn
f10InetCidrRouteFirstHopType = _F10InetCidrRouteFirstHopType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 6),
    _F10InetCidrRouteFirstHopType_Type()
)
f10InetCidrRouteFirstHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10InetCidrRouteFirstHopType.setStatus("current")
_F10InetCidrRouteFirstHop_Type = InetAddress
_F10InetCidrRouteFirstHop_Object = MibTableColumn
f10InetCidrRouteFirstHop = _F10InetCidrRouteFirstHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 7),
    _F10InetCidrRouteFirstHop_Type()
)
f10InetCidrRouteFirstHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f10InetCidrRouteFirstHop.setStatus("current")
_F10InetCidrRouteIfIndex_Type = InterfaceIndexOrZero
_F10InetCidrRouteIfIndex_Object = MibTableColumn
f10InetCidrRouteIfIndex = _F10InetCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 8),
    _F10InetCidrRouteIfIndex_Type()
)
f10InetCidrRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InetCidrRouteIfIndex.setStatus("current")
_F10InetCidrRouteMacAddress_Type = MacAddress
_F10InetCidrRouteMacAddress_Object = MibTableColumn
f10InetCidrRouteMacAddress = _F10InetCidrRouteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 9),
    _F10InetCidrRouteMacAddress_Type()
)
f10InetCidrRouteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InetCidrRouteMacAddress.setStatus("current")


class _F10InetCidrRouteEgressPort_Type(OctetString):
    """Custom type f10InetCidrRouteEgressPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_F10InetCidrRouteEgressPort_Type.__name__ = "OctetString"
_F10InetCidrRouteEgressPort_Object = MibTableColumn
f10InetCidrRouteEgressPort = _F10InetCidrRouteEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 10),
    _F10InetCidrRouteEgressPort_Type()
)
f10InetCidrRouteEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InetCidrRouteEgressPort.setStatus("current")
_F10InetCidrRouteCamIndex_Type = Unsigned32
_F10InetCidrRouteCamIndex_Object = MibTableColumn
f10InetCidrRouteCamIndex = _F10InetCidrRouteCamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 11),
    _F10InetCidrRouteCamIndex_Type()
)
f10InetCidrRouteCamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f10InetCidrRouteCamIndex.setStatus("current")
_F10IpForwardMibConformance_ObjectIdentity = ObjectIdentity
f10IpForwardMibConformance = _F10IpForwardMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2)
)
_F10IpForwardMibCompliances_ObjectIdentity = ObjectIdentity
f10IpForwardMibCompliances = _F10IpForwardMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1)
)
_F10IpForwardMibGroups_ObjectIdentity = ObjectIdentity
f10IpForwardMibGroups = _F10IpForwardMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2)
)

# Managed Objects groups

f10IpForwardObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2, 1)
)
f10IpForwardObjectGroup.setObjects(
      *(("F10-FIB-MIB", "f10IpForwardVersion"),
        ("F10-FIB-MIB", "f10InetCidrRouteIfIndex"),
        ("F10-FIB-MIB", "f10InetCidrRouteMacAddress"),
        ("F10-FIB-MIB", "f10InetCidrRouteEgressPort"),
        ("F10-FIB-MIB", "f10InetCidrRouteCamIndex"))
)
if mibBuilder.loadTexts:
    f10IpForwardObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f10IpForwardMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f10IpForwardMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-FIB-MIB",
    **{"f10IpForwardMib": f10IpForwardMib,
       "f10IpForwardMibObjects": f10IpForwardMibObjects,
       "f10IpForwardVersionTable": f10IpForwardVersionTable,
       "f10IpForwardVersionEntry": f10IpForwardVersionEntry,
       "f10IpForwardAddrFamily": f10IpForwardAddrFamily,
       "f10IpForwardVersion": f10IpForwardVersion,
       "f10IpForwardTable": f10IpForwardTable,
       "f10IpForwardEntry": f10IpForwardEntry,
       "f10IpforwardDest": f10IpforwardDest,
       "f10IpforwardMask": f10IpforwardMask,
       "f10IpforwardNextHop": f10IpforwardNextHop,
       "f10IpforwardFirstHop": f10IpforwardFirstHop,
       "f10IpforwardIfIndex": f10IpforwardIfIndex,
       "f10IpforwardMacAddress": f10IpforwardMacAddress,
       "f10IpforwardEgressPort": f10IpforwardEgressPort,
       "f10IpforwardCamIndex": f10IpforwardCamIndex,
       "f10InetCidrIpv4RouteNumber": f10InetCidrIpv4RouteNumber,
       "f10InetCidrIpv6RouteNumber": f10InetCidrIpv6RouteNumber,
       "f10InetCidrRouteTable": f10InetCidrRouteTable,
       "f10InetCidrRouteTableEntry": f10InetCidrRouteTableEntry,
       "f10InetCidrRouteDestType": f10InetCidrRouteDestType,
       "f10InetCidrRouteDest": f10InetCidrRouteDest,
       "f10InetCidrRoutePfxLen": f10InetCidrRoutePfxLen,
       "f10InetCidrRouteNextHopType": f10InetCidrRouteNextHopType,
       "f10InetCidrRouteNextHop": f10InetCidrRouteNextHop,
       "f10InetCidrRouteFirstHopType": f10InetCidrRouteFirstHopType,
       "f10InetCidrRouteFirstHop": f10InetCidrRouteFirstHop,
       "f10InetCidrRouteIfIndex": f10InetCidrRouteIfIndex,
       "f10InetCidrRouteMacAddress": f10InetCidrRouteMacAddress,
       "f10InetCidrRouteEgressPort": f10InetCidrRouteEgressPort,
       "f10InetCidrRouteCamIndex": f10InetCidrRouteCamIndex,
       "f10IpForwardMibConformance": f10IpForwardMibConformance,
       "f10IpForwardMibCompliances": f10IpForwardMibCompliances,
       "f10IpForwardMibCompliance": f10IpForwardMibCompliance,
       "f10IpForwardMibGroups": f10IpForwardMibGroups,
       "f10IpForwardObjectGroup": f10IpForwardObjectGroup}
)
