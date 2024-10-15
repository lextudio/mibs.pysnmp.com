# SNMP MIB module (ALCATEL-IND1-IPRMV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IPRMV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:17 2024
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

(routingIND1Iprm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Iprm")

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(Ipv6Address,
 Ipv6IfIndex) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1IPRMV6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2)
)
alcatelIND1IPRMV6MIB.setRevisions(
        ("2010-02-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaIprmV6RtPrefType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgpExternal", 5),
          ("bgpInternal", 6),
          ("isisl1", 7),
          ("isisl2", 8),
          ("local", 1),
          ("ospf", 3),
          ("rip", 4),
          ("static", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPRMV6MIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMV6MIBObjects = _AlcatelIND1IPRMV6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1)
)
_AlaIprmV6Config_ObjectIdentity = ObjectIdentity
alaIprmV6Config = _AlaIprmV6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1)
)
_AlaIprmV6RouteTable_Object = MibTable
alaIprmV6RouteTable = _AlaIprmV6RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaIprmV6RouteTable.setStatus("current")
_AlaIprmV6RouteEntry_Object = MibTableRow
alaIprmV6RouteEntry = _AlaIprmV6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1)
)
alaIprmV6RouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RouteDest"),
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RoutePfxLength"),
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RouteNextHop"),
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RouteProtocol"),
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RouteIfIndex"),
)
if mibBuilder.loadTexts:
    alaIprmV6RouteEntry.setStatus("current")
_AlaIprmV6RouteDest_Type = Ipv6Address
_AlaIprmV6RouteDest_Object = MibTableColumn
alaIprmV6RouteDest = _AlaIprmV6RouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1, 1),
    _AlaIprmV6RouteDest_Type()
)
alaIprmV6RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6RouteDest.setStatus("current")


class _AlaIprmV6RoutePfxLength_Type(Integer32):
    """Custom type alaIprmV6RoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaIprmV6RoutePfxLength_Type.__name__ = "Integer32"
_AlaIprmV6RoutePfxLength_Object = MibTableColumn
alaIprmV6RoutePfxLength = _AlaIprmV6RoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1, 2),
    _AlaIprmV6RoutePfxLength_Type()
)
alaIprmV6RoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6RoutePfxLength.setStatus("current")
if mibBuilder.loadTexts:
    alaIprmV6RoutePfxLength.setUnits("bits")
_AlaIprmV6RouteNextHop_Type = Ipv6Address
_AlaIprmV6RouteNextHop_Object = MibTableColumn
alaIprmV6RouteNextHop = _AlaIprmV6RouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1, 3),
    _AlaIprmV6RouteNextHop_Type()
)
alaIprmV6RouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6RouteNextHop.setStatus("current")
_AlaIprmV6RouteProtocol_Type = IANAipRouteProtocol
_AlaIprmV6RouteProtocol_Object = MibTableColumn
alaIprmV6RouteProtocol = _AlaIprmV6RouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1, 4),
    _AlaIprmV6RouteProtocol_Type()
)
alaIprmV6RouteProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6RouteProtocol.setStatus("current")
_AlaIprmV6RouteIfIndex_Type = Ipv6IfIndex
_AlaIprmV6RouteIfIndex_Object = MibTableColumn
alaIprmV6RouteIfIndex = _AlaIprmV6RouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1, 5),
    _AlaIprmV6RouteIfIndex_Type()
)
alaIprmV6RouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6RouteIfIndex.setStatus("current")
_AlaIprmV6RouteMetric_Type = Unsigned32
_AlaIprmV6RouteMetric_Object = MibTableColumn
alaIprmV6RouteMetric = _AlaIprmV6RouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1, 6),
    _AlaIprmV6RouteMetric_Type()
)
alaIprmV6RouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmV6RouteMetric.setStatus("current")
_AlaIprmV6RouteValid_Type = TruthValue
_AlaIprmV6RouteValid_Object = MibTableColumn
alaIprmV6RouteValid = _AlaIprmV6RouteValid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 1, 1, 7),
    _AlaIprmV6RouteValid_Type()
)
alaIprmV6RouteValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIprmV6RouteValid.setStatus("current")
_AlaIprmV6StaticRouteTable_Object = MibTable
alaIprmV6StaticRouteTable = _AlaIprmV6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteTable.setStatus("current")
_AlaIprmV6StaticRouteEntry_Object = MibTableRow
alaIprmV6StaticRouteEntry = _AlaIprmV6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1)
)
alaIprmV6StaticRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRouteDest"),
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRoutePfxLength"),
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRouteNextHop"),
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRouteIfIndex"),
)
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteEntry.setStatus("current")
_AlaIprmV6StaticRouteDest_Type = Ipv6Address
_AlaIprmV6StaticRouteDest_Object = MibTableColumn
alaIprmV6StaticRouteDest = _AlaIprmV6StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 1),
    _AlaIprmV6StaticRouteDest_Type()
)
alaIprmV6StaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteDest.setStatus("current")


class _AlaIprmV6StaticRoutePfxLength_Type(Integer32):
    """Custom type alaIprmV6StaticRoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaIprmV6StaticRoutePfxLength_Type.__name__ = "Integer32"
_AlaIprmV6StaticRoutePfxLength_Object = MibTableColumn
alaIprmV6StaticRoutePfxLength = _AlaIprmV6StaticRoutePfxLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 2),
    _AlaIprmV6StaticRoutePfxLength_Type()
)
alaIprmV6StaticRoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6StaticRoutePfxLength.setStatus("current")
_AlaIprmV6StaticRouteNextHop_Type = Ipv6Address
_AlaIprmV6StaticRouteNextHop_Object = MibTableColumn
alaIprmV6StaticRouteNextHop = _AlaIprmV6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 3),
    _AlaIprmV6StaticRouteNextHop_Type()
)
alaIprmV6StaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteNextHop.setStatus("current")
_AlaIprmV6StaticRouteIfIndex_Type = Ipv6IfIndex
_AlaIprmV6StaticRouteIfIndex_Object = MibTableColumn
alaIprmV6StaticRouteIfIndex = _AlaIprmV6StaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 4),
    _AlaIprmV6StaticRouteIfIndex_Type()
)
alaIprmV6StaticRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteIfIndex.setStatus("current")


class _AlaIprmV6StaticRouteMetric_Type(Unsigned32):
    """Custom type alaIprmV6StaticRouteMetric based on Unsigned32"""
    defaultValue = 1


_AlaIprmV6StaticRouteMetric_Object = MibTableColumn
alaIprmV6StaticRouteMetric = _AlaIprmV6StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 5),
    _AlaIprmV6StaticRouteMetric_Type()
)
alaIprmV6StaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteMetric.setStatus("current")
_AlaIprmV6StaticRouteStatus_Type = RowStatus
_AlaIprmV6StaticRouteStatus_Object = MibTableColumn
alaIprmV6StaticRouteStatus = _AlaIprmV6StaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 6),
    _AlaIprmV6StaticRouteStatus_Type()
)
alaIprmV6StaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteStatus.setStatus("current")
_AlaIprmV6StaticRouteTag_Type = Unsigned32
_AlaIprmV6StaticRouteTag_Object = MibTableColumn
alaIprmV6StaticRouteTag = _AlaIprmV6StaticRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 7),
    _AlaIprmV6StaticRouteTag_Type()
)
alaIprmV6StaticRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteTag.setStatus("current")


class _AlaIprmV6StaticRouteName_Type(SnmpAdminString):
    """Custom type alaIprmV6StaticRouteName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaIprmV6StaticRouteName_Type.__name__ = "SnmpAdminString"
_AlaIprmV6StaticRouteName_Object = MibTableColumn
alaIprmV6StaticRouteName = _AlaIprmV6StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 2, 1, 8),
    _AlaIprmV6StaticRouteName_Type()
)
alaIprmV6StaticRouteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIprmV6StaticRouteName.setStatus("current")
_AlaIprmV6RtPrefTable_Object = MibTable
alaIprmV6RtPrefTable = _AlaIprmV6RtPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaIprmV6RtPrefTable.setStatus("current")
_AlaIprmV6RtPrefTableEntry_Object = MibTableRow
alaIprmV6RtPrefTableEntry = _AlaIprmV6RtPrefTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 3, 1)
)
alaIprmV6RtPrefTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RtPrefEntryType"),
)
if mibBuilder.loadTexts:
    alaIprmV6RtPrefTableEntry.setStatus("current")
_AlaIprmV6RtPrefEntryType_Type = AlaIprmV6RtPrefType
_AlaIprmV6RtPrefEntryType_Object = MibTableColumn
alaIprmV6RtPrefEntryType = _AlaIprmV6RtPrefEntryType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 3, 1, 1),
    _AlaIprmV6RtPrefEntryType_Type()
)
alaIprmV6RtPrefEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIprmV6RtPrefEntryType.setStatus("current")


class _AlaIprmV6RtPrefEntryValue_Type(Integer32):
    """Custom type alaIprmV6RtPrefEntryValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaIprmV6RtPrefEntryValue_Type.__name__ = "Integer32"
_AlaIprmV6RtPrefEntryValue_Object = MibTableColumn
alaIprmV6RtPrefEntryValue = _AlaIprmV6RtPrefEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 1, 1, 3, 1, 2),
    _AlaIprmV6RtPrefEntryValue_Type()
)
alaIprmV6RtPrefEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIprmV6RtPrefEntryValue.setStatus("current")
_AlcatelIND1IPRMV6MIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMV6MIBConformance = _AlcatelIND1IPRMV6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 2)
)
_AlcatelIND1IPRMV6MIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMV6MIBCompliances = _AlcatelIND1IPRMV6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 2, 1)
)
_AlcatelIND1IPRMV6MIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPRMV6MIBGroups = _AlcatelIND1IPRMV6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 2, 2)
)

# Managed Objects groups

alaIprmV6ConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 2, 2, 1)
)
alaIprmV6ConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RouteMetric"),
        ("ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RouteValid"),
        ("ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRouteMetric"),
        ("ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRouteStatus"),
        ("ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRouteTag"),
        ("ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6StaticRouteName"),
        ("ALCATEL-IND1-IPRMV6-MIB", "alaIprmV6RtPrefEntryValue"))
)
if mibBuilder.loadTexts:
    alaIprmV6ConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIprmV6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaIprmV6Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPRMV6-MIB",
    **{"AlaIprmV6RtPrefType": AlaIprmV6RtPrefType,
       "alcatelIND1IPRMV6MIB": alcatelIND1IPRMV6MIB,
       "alcatelIND1IPRMV6MIBObjects": alcatelIND1IPRMV6MIBObjects,
       "alaIprmV6Config": alaIprmV6Config,
       "alaIprmV6RouteTable": alaIprmV6RouteTable,
       "alaIprmV6RouteEntry": alaIprmV6RouteEntry,
       "alaIprmV6RouteDest": alaIprmV6RouteDest,
       "alaIprmV6RoutePfxLength": alaIprmV6RoutePfxLength,
       "alaIprmV6RouteNextHop": alaIprmV6RouteNextHop,
       "alaIprmV6RouteProtocol": alaIprmV6RouteProtocol,
       "alaIprmV6RouteIfIndex": alaIprmV6RouteIfIndex,
       "alaIprmV6RouteMetric": alaIprmV6RouteMetric,
       "alaIprmV6RouteValid": alaIprmV6RouteValid,
       "alaIprmV6StaticRouteTable": alaIprmV6StaticRouteTable,
       "alaIprmV6StaticRouteEntry": alaIprmV6StaticRouteEntry,
       "alaIprmV6StaticRouteDest": alaIprmV6StaticRouteDest,
       "alaIprmV6StaticRoutePfxLength": alaIprmV6StaticRoutePfxLength,
       "alaIprmV6StaticRouteNextHop": alaIprmV6StaticRouteNextHop,
       "alaIprmV6StaticRouteIfIndex": alaIprmV6StaticRouteIfIndex,
       "alaIprmV6StaticRouteMetric": alaIprmV6StaticRouteMetric,
       "alaIprmV6StaticRouteStatus": alaIprmV6StaticRouteStatus,
       "alaIprmV6StaticRouteTag": alaIprmV6StaticRouteTag,
       "alaIprmV6StaticRouteName": alaIprmV6StaticRouteName,
       "alaIprmV6RtPrefTable": alaIprmV6RtPrefTable,
       "alaIprmV6RtPrefTableEntry": alaIprmV6RtPrefTableEntry,
       "alaIprmV6RtPrefEntryType": alaIprmV6RtPrefEntryType,
       "alaIprmV6RtPrefEntryValue": alaIprmV6RtPrefEntryValue,
       "alcatelIND1IPRMV6MIBConformance": alcatelIND1IPRMV6MIBConformance,
       "alcatelIND1IPRMV6MIBCompliances": alcatelIND1IPRMV6MIBCompliances,
       "alaIprmV6Compliance": alaIprmV6Compliance,
       "alcatelIND1IPRMV6MIBGroups": alcatelIND1IPRMV6MIBGroups,
       "alaIprmV6ConfigMIBGroup": alaIprmV6ConfigMIBGroup}
)
