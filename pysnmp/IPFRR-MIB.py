# SNMP MIB module (IPFRR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPFRR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:52 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(inetCidrRouteDest,
 inetCidrRouteDestType,
 inetCidrRouteNextHop,
 inetCidrRouteNextHopType,
 inetCidrRoutePfxLen,
 inetCidrRoutePolicy) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "inetCidrRouteDest",
    "inetCidrRouteDestType",
    "inetCidrRouteNextHop",
    "inetCidrRouteNextHopType",
    "inetCidrRoutePfxLen",
    "inetCidrRoutePolicy")

(ip,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ip")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ipFrrMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 4, 999)
)
ipFrrMIB.setRevisions(
        ("2005-02-18 12:00",
         "2005-02-13 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpFrrMIBObjects_ObjectIdentity = ObjectIdentity
ipFrrMIBObjects = _IpFrrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 999, 1)
)
_IpFrrProtectStats_ObjectIdentity = ObjectIdentity
ipFrrProtectStats = _IpFrrProtectStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 1)
)
_IpFrrTotalRoutes_Type = Gauge32
_IpFrrTotalRoutes_Object = MibScalar
ipFrrTotalRoutes = _IpFrrTotalRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 1),
    _IpFrrTotalRoutes_Type()
)
ipFrrTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFrrTotalRoutes.setStatus("current")
_IpFrrUnprotectedRoutes_Type = Gauge32
_IpFrrUnprotectedRoutes_Object = MibScalar
ipFrrUnprotectedRoutes = _IpFrrUnprotectedRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 2),
    _IpFrrUnprotectedRoutes_Type()
)
ipFrrUnprotectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFrrUnprotectedRoutes.setStatus("current")
_IpFrrProtectedRoutes_Type = Gauge32
_IpFrrProtectedRoutes_Object = MibScalar
ipFrrProtectedRoutes = _IpFrrProtectedRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 3),
    _IpFrrProtectedRoutes_Type()
)
ipFrrProtectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFrrProtectedRoutes.setStatus("current")
_IpFrrLinkProtectedRoutes_Type = Gauge32
_IpFrrLinkProtectedRoutes_Object = MibScalar
ipFrrLinkProtectedRoutes = _IpFrrLinkProtectedRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 4),
    _IpFrrLinkProtectedRoutes_Type()
)
ipFrrLinkProtectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFrrLinkProtectedRoutes.setStatus("current")
_IpFrrNodeProtectedRoutes_Type = Gauge32
_IpFrrNodeProtectedRoutes_Object = MibScalar
ipFrrNodeProtectedRoutes = _IpFrrNodeProtectedRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 1, 5),
    _IpFrrNodeProtectedRoutes_Type()
)
ipFrrNodeProtectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFrrNodeProtectedRoutes.setStatus("current")
_IpFrrAltTable_Object = MibTable
ipFrrAltTable = _IpFrrAltTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2)
)
if mibBuilder.loadTexts:
    ipFrrAltTable.setStatus("current")
_IpFrrAltEntry_Object = MibTableRow
ipFrrAltEntry = _IpFrrAltEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1)
)
ipFrrAltEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "inetCidrRouteDestType"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteDest"),
    (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"),
    (0, "IP-FORWARD-MIB", "inetCidrRoutePolicy"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteNextHopType"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteNextHop"),
    (0, "IPFRR-MIB", "ipFrrAltNextHopType"),
    (0, "IPFRR-MIB", "ipFrrAltNextHop"),
)
if mibBuilder.loadTexts:
    ipFrrAltEntry.setStatus("current")
_IpFrrAltNextHopType_Type = InetAddressType
_IpFrrAltNextHopType_Object = MibTableColumn
ipFrrAltNextHopType = _IpFrrAltNextHopType_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 1),
    _IpFrrAltNextHopType_Type()
)
ipFrrAltNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFrrAltNextHopType.setStatus("current")
_IpFrrAltNextHop_Type = InetAddress
_IpFrrAltNextHop_Object = MibTableColumn
ipFrrAltNextHop = _IpFrrAltNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 2),
    _IpFrrAltNextHop_Type()
)
ipFrrAltNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFrrAltNextHop.setStatus("current")
_IpFrrAltIfIndex_Type = InterfaceIndex
_IpFrrAltIfIndex_Object = MibTableColumn
ipFrrAltIfIndex = _IpFrrAltIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 3),
    _IpFrrAltIfIndex_Type()
)
ipFrrAltIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFrrAltIfIndex.setStatus("current")


class _IpFrrAltType_Type(Integer32):
    """Custom type ipFrrAltType based on Integer32"""
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
        *(("equalCost", 2),
          ("loopFree", 3),
          ("other", 1),
          ("uTurn", 4))
    )


_IpFrrAltType_Type.__name__ = "Integer32"
_IpFrrAltType_Object = MibTableColumn
ipFrrAltType = _IpFrrAltType_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 4),
    _IpFrrAltType_Type()
)
ipFrrAltType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFrrAltType.setStatus("current")


class _IpFrrAltProtectionAvailable_Type(Bits):
    """Custom type ipFrrAltProtectionAvailable based on Bits"""
    namedValues = NamedValues(
        *(("linkProtect", 1),
          ("nodeProtect", 0),
          ("unknownProtection", 2))
    )

_IpFrrAltProtectionAvailable_Type.__name__ = "Bits"
_IpFrrAltProtectionAvailable_Object = MibTableColumn
ipFrrAltProtectionAvailable = _IpFrrAltProtectionAvailable_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 5),
    _IpFrrAltProtectionAvailable_Type()
)
ipFrrAltProtectionAvailable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFrrAltProtectionAvailable.setStatus("current")
_IpFrrAltMetric1_Type = Integer32
_IpFrrAltMetric1_Object = MibTableColumn
ipFrrAltMetric1 = _IpFrrAltMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 6),
    _IpFrrAltMetric1_Type()
)
ipFrrAltMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFrrAltMetric1.setStatus("current")
_IpFrrAltStatus_Type = RowStatus
_IpFrrAltStatus_Object = MibTableColumn
ipFrrAltStatus = _IpFrrAltStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 2, 1, 7),
    _IpFrrAltStatus_Type()
)
ipFrrAltStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFrrAltStatus.setStatus("current")
_IpFrrNoAltTable_Object = MibTable
ipFrrNoAltTable = _IpFrrNoAltTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 3)
)
if mibBuilder.loadTexts:
    ipFrrNoAltTable.setStatus("current")
_IpFrrNoAltEntry_Object = MibTableRow
ipFrrNoAltEntry = _IpFrrNoAltEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 3, 1)
)
ipFrrNoAltEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "inetCidrRouteDestType"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteDest"),
    (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"),
)
if mibBuilder.loadTexts:
    ipFrrNoAltEntry.setStatus("current")


class _IpFrrNoAltCause_Type(Integer32):
    """Custom type ipFrrNoAltCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ipFrrDisabled", 3),
          ("ipFrrUnavailable", 1),
          ("ipFrrUturnDisabled", 4),
          ("localAddress", 2),
          ("other", 5))
    )


_IpFrrNoAltCause_Type.__name__ = "Integer32"
_IpFrrNoAltCause_Object = MibTableColumn
ipFrrNoAltCause = _IpFrrNoAltCause_Object(
    (1, 3, 6, 1, 2, 1, 4, 999, 1, 3, 1, 1),
    _IpFrrNoAltCause_Type()
)
ipFrrNoAltCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFrrNoAltCause.setStatus("current")
_IpFrrMIBConformance_ObjectIdentity = ObjectIdentity
ipFrrMIBConformance = _IpFrrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 999, 2)
)
_IpFrrMIBCompliances_ObjectIdentity = ObjectIdentity
ipFrrMIBCompliances = _IpFrrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 999, 2, 1)
)
_IpFrrMIBGroups_ObjectIdentity = ObjectIdentity
ipFrrMIBGroups = _IpFrrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 999, 2, 2)
)

# Managed Objects groups

ipFrrBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 999, 2, 2, 1)
)
ipFrrBasicGroup.setObjects(
      *(("IPFRR-MIB", "ipFrrTotalRoutes"),
        ("IPFRR-MIB", "ipFrrUnprotectedRoutes"),
        ("IPFRR-MIB", "ipFrrProtectedRoutes"),
        ("IPFRR-MIB", "ipFrrLinkProtectedRoutes"),
        ("IPFRR-MIB", "ipFrrNodeProtectedRoutes"),
        ("IPFRR-MIB", "ipFrrAltIfIndex"),
        ("IPFRR-MIB", "ipFrrAltType"),
        ("IPFRR-MIB", "ipFrrAltProtectionAvailable"),
        ("IPFRR-MIB", "ipFrrAltMetric1"),
        ("IPFRR-MIB", "ipFrrAltStatus"),
        ("IPFRR-MIB", "ipFrrNoAltCause"))
)
if mibBuilder.loadTexts:
    ipFrrBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipFrrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipFrrMIBCompliance.setStatus(
        "deprecated"
    )

ipFrrMIBInetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 999, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ipFrrMIBInetCompliance.setStatus(
        "current"
    )

ipFrrReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 999, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ipFrrReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFRR-MIB",
    **{"ipFrrMIB": ipFrrMIB,
       "ipFrrMIBObjects": ipFrrMIBObjects,
       "ipFrrProtectStats": ipFrrProtectStats,
       "ipFrrTotalRoutes": ipFrrTotalRoutes,
       "ipFrrUnprotectedRoutes": ipFrrUnprotectedRoutes,
       "ipFrrProtectedRoutes": ipFrrProtectedRoutes,
       "ipFrrLinkProtectedRoutes": ipFrrLinkProtectedRoutes,
       "ipFrrNodeProtectedRoutes": ipFrrNodeProtectedRoutes,
       "ipFrrAltTable": ipFrrAltTable,
       "ipFrrAltEntry": ipFrrAltEntry,
       "ipFrrAltNextHopType": ipFrrAltNextHopType,
       "ipFrrAltNextHop": ipFrrAltNextHop,
       "ipFrrAltIfIndex": ipFrrAltIfIndex,
       "ipFrrAltType": ipFrrAltType,
       "ipFrrAltProtectionAvailable": ipFrrAltProtectionAvailable,
       "ipFrrAltMetric1": ipFrrAltMetric1,
       "ipFrrAltStatus": ipFrrAltStatus,
       "ipFrrNoAltTable": ipFrrNoAltTable,
       "ipFrrNoAltEntry": ipFrrNoAltEntry,
       "ipFrrNoAltCause": ipFrrNoAltCause,
       "ipFrrMIBConformance": ipFrrMIBConformance,
       "ipFrrMIBCompliances": ipFrrMIBCompliances,
       "ipFrrMIBCompliance": ipFrrMIBCompliance,
       "ipFrrMIBInetCompliance": ipFrrMIBInetCompliance,
       "ipFrrReadOnlyCompliance": ipFrrReadOnlyCompliance,
       "ipFrrMIBGroups": ipFrrMIBGroups,
       "ipFrrBasicGroup": ipFrrBasicGroup}
)
