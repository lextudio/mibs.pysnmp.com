# SNMP MIB module (DELL-NETWORKING-FIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-FIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:52 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

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

dellNetIpForwardMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9)
)
dellNetIpForwardMib.setRevisions(
        ("2011-07-08 12:00",
         "2007-09-14 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetIpForwardMibObjects_ObjectIdentity = ObjectIdentity
dellNetIpForwardMibObjects = _DellNetIpForwardMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1)
)
_DellNetIpForwardVersionTable_Object = MibTable
dellNetIpForwardVersionTable = _DellNetIpForwardVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetIpForwardVersionTable.setStatus("current")
_DellNetIpForwardVersionEntry_Object = MibTableRow
dellNetIpForwardVersionEntry = _DellNetIpForwardVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1)
)
dellNetIpForwardVersionEntry.setIndexNames(
    (0, "DELL-NETWORKING-FIB-MIB", "chSysCardNumber"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpForwardAddrFamily"),
)
if mibBuilder.loadTexts:
    dellNetIpForwardVersionEntry.setStatus("current")
_DellNetIpForwardAddrFamily_Type = InetAddressType
_DellNetIpForwardAddrFamily_Object = MibTableColumn
dellNetIpForwardAddrFamily = _DellNetIpForwardAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1, 1),
    _DellNetIpForwardAddrFamily_Type()
)
dellNetIpForwardAddrFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetIpForwardAddrFamily.setStatus("current")
_DellNetIpForwardVersion_Type = Counter64
_DellNetIpForwardVersion_Object = MibTableColumn
dellNetIpForwardVersion = _DellNetIpForwardVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 1, 1, 2),
    _DellNetIpForwardVersion_Type()
)
dellNetIpForwardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpForwardVersion.setStatus("current")
_DellNetIpForwardTable_Object = MibTable
dellNetIpForwardTable = _DellNetIpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2)
)
if mibBuilder.loadTexts:
    dellNetIpForwardTable.setStatus("deprecated")
_DellNetIpForwardEntry_Object = MibTableRow
dellNetIpForwardEntry = _DellNetIpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1)
)
dellNetIpForwardEntry.setIndexNames(
    (0, "DELL-NETWORKING-FIB-MIB", "chSysCardNumber"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardDest"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardMask"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardNextHop"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetIpforwardFirstHop"),
)
if mibBuilder.loadTexts:
    dellNetIpForwardEntry.setStatus("deprecated")
_DellNetIpforwardDest_Type = IpAddress
_DellNetIpforwardDest_Object = MibTableColumn
dellNetIpforwardDest = _DellNetIpforwardDest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 1),
    _DellNetIpforwardDest_Type()
)
dellNetIpforwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardDest.setStatus("deprecated")
_DellNetIpforwardMask_Type = IpAddress
_DellNetIpforwardMask_Object = MibTableColumn
dellNetIpforwardMask = _DellNetIpforwardMask_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 2),
    _DellNetIpforwardMask_Type()
)
dellNetIpforwardMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardMask.setStatus("deprecated")
_DellNetIpforwardNextHop_Type = IpAddress
_DellNetIpforwardNextHop_Object = MibTableColumn
dellNetIpforwardNextHop = _DellNetIpforwardNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 3),
    _DellNetIpforwardNextHop_Type()
)
dellNetIpforwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardNextHop.setStatus("deprecated")
_DellNetIpforwardFirstHop_Type = IpAddress
_DellNetIpforwardFirstHop_Object = MibTableColumn
dellNetIpforwardFirstHop = _DellNetIpforwardFirstHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 4),
    _DellNetIpforwardFirstHop_Type()
)
dellNetIpforwardFirstHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardFirstHop.setStatus("deprecated")
_DellNetIpforwardIfIndex_Type = Integer32
_DellNetIpforwardIfIndex_Object = MibTableColumn
dellNetIpforwardIfIndex = _DellNetIpforwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 5),
    _DellNetIpforwardIfIndex_Type()
)
dellNetIpforwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardIfIndex.setStatus("deprecated")
_DellNetIpforwardMacAddress_Type = MacAddress
_DellNetIpforwardMacAddress_Object = MibTableColumn
dellNetIpforwardMacAddress = _DellNetIpforwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 6),
    _DellNetIpforwardMacAddress_Type()
)
dellNetIpforwardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardMacAddress.setStatus("deprecated")


class _DellNetIpforwardEgressPort_Type(OctetString):
    """Custom type dellNetIpforwardEgressPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DellNetIpforwardEgressPort_Type.__name__ = "OctetString"
_DellNetIpforwardEgressPort_Object = MibTableColumn
dellNetIpforwardEgressPort = _DellNetIpforwardEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 7),
    _DellNetIpforwardEgressPort_Type()
)
dellNetIpforwardEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardEgressPort.setStatus("deprecated")
_DellNetIpforwardCamIndex_Type = Integer32
_DellNetIpforwardCamIndex_Object = MibTableColumn
dellNetIpforwardCamIndex = _DellNetIpforwardCamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 2, 1, 8),
    _DellNetIpforwardCamIndex_Type()
)
dellNetIpforwardCamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetIpforwardCamIndex.setStatus("deprecated")
_DellNetInetCidrIpv4RouteNumber_Type = Gauge32
_DellNetInetCidrIpv4RouteNumber_Object = MibScalar
dellNetInetCidrIpv4RouteNumber = _DellNetInetCidrIpv4RouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 3),
    _DellNetInetCidrIpv4RouteNumber_Type()
)
dellNetInetCidrIpv4RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetInetCidrIpv4RouteNumber.setStatus("current")
_DellNetInetCidrIpv6RouteNumber_Type = Gauge32
_DellNetInetCidrIpv6RouteNumber_Object = MibScalar
dellNetInetCidrIpv6RouteNumber = _DellNetInetCidrIpv6RouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 4),
    _DellNetInetCidrIpv6RouteNumber_Type()
)
dellNetInetCidrIpv6RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetInetCidrIpv6RouteNumber.setStatus("current")
_DellNetInetCidrRouteTable_Object = MibTable
dellNetInetCidrRouteTable = _DellNetInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5)
)
if mibBuilder.loadTexts:
    dellNetInetCidrRouteTable.setStatus("current")
_DellNetInetCidrRouteTableEntry_Object = MibTableRow
dellNetInetCidrRouteTableEntry = _DellNetInetCidrRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1)
)
dellNetInetCidrRouteTableEntry.setIndexNames(
    (0, "DELL-NETWORKING-FIB-MIB", "chSysCardNumber"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteDestType"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteDest"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRoutePfxLen"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteNextHopType"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteNextHop"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteFirstHopType"),
    (0, "DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteFirstHop"),
)
if mibBuilder.loadTexts:
    dellNetInetCidrRouteTableEntry.setStatus("current")
_DellNetInetCidrRouteDestType_Type = InetAddressType
_DellNetInetCidrRouteDestType_Object = MibTableColumn
dellNetInetCidrRouteDestType = _DellNetInetCidrRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 1),
    _DellNetInetCidrRouteDestType_Type()
)
dellNetInetCidrRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteDestType.setStatus("current")
_DellNetInetCidrRouteDest_Type = InetAddress
_DellNetInetCidrRouteDest_Object = MibTableColumn
dellNetInetCidrRouteDest = _DellNetInetCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 2),
    _DellNetInetCidrRouteDest_Type()
)
dellNetInetCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteDest.setStatus("current")
_DellNetInetCidrRoutePfxLen_Type = InetAddressPrefixLength
_DellNetInetCidrRoutePfxLen_Object = MibTableColumn
dellNetInetCidrRoutePfxLen = _DellNetInetCidrRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 3),
    _DellNetInetCidrRoutePfxLen_Type()
)
dellNetInetCidrRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetInetCidrRoutePfxLen.setStatus("current")
_DellNetInetCidrRouteNextHopType_Type = InetAddressType
_DellNetInetCidrRouteNextHopType_Object = MibTableColumn
dellNetInetCidrRouteNextHopType = _DellNetInetCidrRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 4),
    _DellNetInetCidrRouteNextHopType_Type()
)
dellNetInetCidrRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteNextHopType.setStatus("current")
_DellNetInetCidrRouteNextHop_Type = InetAddress
_DellNetInetCidrRouteNextHop_Object = MibTableColumn
dellNetInetCidrRouteNextHop = _DellNetInetCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 5),
    _DellNetInetCidrRouteNextHop_Type()
)
dellNetInetCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteNextHop.setStatus("current")
_DellNetInetCidrRouteFirstHopType_Type = InetAddressType
_DellNetInetCidrRouteFirstHopType_Object = MibTableColumn
dellNetInetCidrRouteFirstHopType = _DellNetInetCidrRouteFirstHopType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 6),
    _DellNetInetCidrRouteFirstHopType_Type()
)
dellNetInetCidrRouteFirstHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteFirstHopType.setStatus("current")
_DellNetInetCidrRouteFirstHop_Type = InetAddress
_DellNetInetCidrRouteFirstHop_Object = MibTableColumn
dellNetInetCidrRouteFirstHop = _DellNetInetCidrRouteFirstHop_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 7),
    _DellNetInetCidrRouteFirstHop_Type()
)
dellNetInetCidrRouteFirstHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteFirstHop.setStatus("current")
_DellNetInetCidrRouteIfIndex_Type = InterfaceIndexOrZero
_DellNetInetCidrRouteIfIndex_Object = MibTableColumn
dellNetInetCidrRouteIfIndex = _DellNetInetCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 8),
    _DellNetInetCidrRouteIfIndex_Type()
)
dellNetInetCidrRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteIfIndex.setStatus("current")
_DellNetInetCidrRouteMacAddress_Type = MacAddress
_DellNetInetCidrRouteMacAddress_Object = MibTableColumn
dellNetInetCidrRouteMacAddress = _DellNetInetCidrRouteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 9),
    _DellNetInetCidrRouteMacAddress_Type()
)
dellNetInetCidrRouteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteMacAddress.setStatus("current")


class _DellNetInetCidrRouteEgressPort_Type(OctetString):
    """Custom type dellNetInetCidrRouteEgressPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DellNetInetCidrRouteEgressPort_Type.__name__ = "OctetString"
_DellNetInetCidrRouteEgressPort_Object = MibTableColumn
dellNetInetCidrRouteEgressPort = _DellNetInetCidrRouteEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 10),
    _DellNetInetCidrRouteEgressPort_Type()
)
dellNetInetCidrRouteEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteEgressPort.setStatus("current")
_DellNetInetCidrRouteCamIndex_Type = Unsigned32
_DellNetInetCidrRouteCamIndex_Object = MibTableColumn
dellNetInetCidrRouteCamIndex = _DellNetInetCidrRouteCamIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 1, 5, 1, 11),
    _DellNetInetCidrRouteCamIndex_Type()
)
dellNetInetCidrRouteCamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetInetCidrRouteCamIndex.setStatus("current")
_DellNetIpForwardMibConformance_ObjectIdentity = ObjectIdentity
dellNetIpForwardMibConformance = _DellNetIpForwardMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2)
)
_DellNetIpForwardMibCompliances_ObjectIdentity = ObjectIdentity
dellNetIpForwardMibCompliances = _DellNetIpForwardMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1)
)
_DellNetIpForwardMibGroups_ObjectIdentity = ObjectIdentity
dellNetIpForwardMibGroups = _DellNetIpForwardMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2)
)
_DellNetIpForwardVariable_ObjectIdentity = ObjectIdentity
dellNetIpForwardVariable = _DellNetIpForwardVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 3)
)
_ChSysCardNumber_Type = Integer32
_ChSysCardNumber_Object = MibScalar
chSysCardNumber = _ChSysCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 3, 1),
    _ChSysCardNumber_Type()
)
chSysCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardNumber.setStatus("current")

# Managed Objects groups

dellNetIpForwardObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 2, 1)
)
dellNetIpForwardObjectGroup.setObjects(
      *(("DELL-NETWORKING-FIB-MIB", "dellNetIpForwardVersion"),
        ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteIfIndex"),
        ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteMacAddress"),
        ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteEgressPort"),
        ("DELL-NETWORKING-FIB-MIB", "dellNetInetCidrRouteCamIndex"))
)
if mibBuilder.loadTexts:
    dellNetIpForwardObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dellNetIpForwardMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetIpForwardMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-FIB-MIB",
    **{"dellNetIpForwardMib": dellNetIpForwardMib,
       "dellNetIpForwardMibObjects": dellNetIpForwardMibObjects,
       "dellNetIpForwardVersionTable": dellNetIpForwardVersionTable,
       "dellNetIpForwardVersionEntry": dellNetIpForwardVersionEntry,
       "dellNetIpForwardAddrFamily": dellNetIpForwardAddrFamily,
       "dellNetIpForwardVersion": dellNetIpForwardVersion,
       "dellNetIpForwardTable": dellNetIpForwardTable,
       "dellNetIpForwardEntry": dellNetIpForwardEntry,
       "dellNetIpforwardDest": dellNetIpforwardDest,
       "dellNetIpforwardMask": dellNetIpforwardMask,
       "dellNetIpforwardNextHop": dellNetIpforwardNextHop,
       "dellNetIpforwardFirstHop": dellNetIpforwardFirstHop,
       "dellNetIpforwardIfIndex": dellNetIpforwardIfIndex,
       "dellNetIpforwardMacAddress": dellNetIpforwardMacAddress,
       "dellNetIpforwardEgressPort": dellNetIpforwardEgressPort,
       "dellNetIpforwardCamIndex": dellNetIpforwardCamIndex,
       "dellNetInetCidrIpv4RouteNumber": dellNetInetCidrIpv4RouteNumber,
       "dellNetInetCidrIpv6RouteNumber": dellNetInetCidrIpv6RouteNumber,
       "dellNetInetCidrRouteTable": dellNetInetCidrRouteTable,
       "dellNetInetCidrRouteTableEntry": dellNetInetCidrRouteTableEntry,
       "dellNetInetCidrRouteDestType": dellNetInetCidrRouteDestType,
       "dellNetInetCidrRouteDest": dellNetInetCidrRouteDest,
       "dellNetInetCidrRoutePfxLen": dellNetInetCidrRoutePfxLen,
       "dellNetInetCidrRouteNextHopType": dellNetInetCidrRouteNextHopType,
       "dellNetInetCidrRouteNextHop": dellNetInetCidrRouteNextHop,
       "dellNetInetCidrRouteFirstHopType": dellNetInetCidrRouteFirstHopType,
       "dellNetInetCidrRouteFirstHop": dellNetInetCidrRouteFirstHop,
       "dellNetInetCidrRouteIfIndex": dellNetInetCidrRouteIfIndex,
       "dellNetInetCidrRouteMacAddress": dellNetInetCidrRouteMacAddress,
       "dellNetInetCidrRouteEgressPort": dellNetInetCidrRouteEgressPort,
       "dellNetInetCidrRouteCamIndex": dellNetInetCidrRouteCamIndex,
       "dellNetIpForwardMibConformance": dellNetIpForwardMibConformance,
       "dellNetIpForwardMibCompliances": dellNetIpForwardMibCompliances,
       "dellNetIpForwardMibCompliance": dellNetIpForwardMibCompliance,
       "dellNetIpForwardMibGroups": dellNetIpForwardMibGroups,
       "dellNetIpForwardObjectGroup": dellNetIpForwardObjectGroup,
       "dellNetIpForwardVariable": dellNetIpForwardVariable,
       "chSysCardNumber": chSysCardNumber}
)
