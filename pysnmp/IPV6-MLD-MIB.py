# SNMP MIB module (IPV6-MLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV6-MLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:49 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

mldMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 91)
)
mldMIB.setRevisions(
        ("2001-01-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MldMIBObjects_ObjectIdentity = ObjectIdentity
mldMIBObjects = _MldMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 91, 1)
)
_MldInterfaceTable_Object = MibTable
mldInterfaceTable = _MldInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1)
)
if mibBuilder.loadTexts:
    mldInterfaceTable.setStatus("current")
_MldInterfaceEntry_Object = MibTableRow
mldInterfaceEntry = _MldInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1)
)
mldInterfaceEntry.setIndexNames(
    (0, "IPV6-MLD-MIB", "mldInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    mldInterfaceEntry.setStatus("current")
_MldInterfaceIfIndex_Type = InterfaceIndex
_MldInterfaceIfIndex_Object = MibTableColumn
mldInterfaceIfIndex = _MldInterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 1),
    _MldInterfaceIfIndex_Type()
)
mldInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldInterfaceIfIndex.setStatus("current")


class _MldInterfaceQueryInterval_Type(Unsigned32):
    """Custom type mldInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125


_MldInterfaceQueryInterval_Object = MibTableColumn
mldInterfaceQueryInterval = _MldInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 2),
    _MldInterfaceQueryInterval_Type()
)
mldInterfaceQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    mldInterfaceQueryInterval.setUnits("seconds")
_MldInterfaceStatus_Type = RowStatus
_MldInterfaceStatus_Object = MibTableColumn
mldInterfaceStatus = _MldInterfaceStatus_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 3),
    _MldInterfaceStatus_Type()
)
mldInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldInterfaceStatus.setStatus("current")


class _MldInterfaceVersion_Type(Unsigned32):
    """Custom type mldInterfaceVersion based on Unsigned32"""
    defaultValue = 1


_MldInterfaceVersion_Object = MibTableColumn
mldInterfaceVersion = _MldInterfaceVersion_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 4),
    _MldInterfaceVersion_Type()
)
mldInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldInterfaceVersion.setStatus("current")


class _MldInterfaceQuerier_Type(InetAddressIPv6):
    """Custom type mldInterfaceQuerier based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MldInterfaceQuerier_Type.__name__ = "InetAddressIPv6"
_MldInterfaceQuerier_Object = MibTableColumn
mldInterfaceQuerier = _MldInterfaceQuerier_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 5),
    _MldInterfaceQuerier_Type()
)
mldInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldInterfaceQuerier.setStatus("current")


class _MldInterfaceQueryMaxResponseDelay_Type(Unsigned32):
    """Custom type mldInterfaceQueryMaxResponseDelay based on Unsigned32"""
    defaultValue = 10


_MldInterfaceQueryMaxResponseDelay_Object = MibTableColumn
mldInterfaceQueryMaxResponseDelay = _MldInterfaceQueryMaxResponseDelay_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 6),
    _MldInterfaceQueryMaxResponseDelay_Type()
)
mldInterfaceQueryMaxResponseDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldInterfaceQueryMaxResponseDelay.setStatus("current")
if mibBuilder.loadTexts:
    mldInterfaceQueryMaxResponseDelay.setUnits("seconds")
_MldInterfaceJoins_Type = Counter32
_MldInterfaceJoins_Object = MibTableColumn
mldInterfaceJoins = _MldInterfaceJoins_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 7),
    _MldInterfaceJoins_Type()
)
mldInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldInterfaceJoins.setStatus("current")
_MldInterfaceGroups_Type = Gauge32
_MldInterfaceGroups_Object = MibTableColumn
mldInterfaceGroups = _MldInterfaceGroups_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 8),
    _MldInterfaceGroups_Type()
)
mldInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldInterfaceGroups.setStatus("current")


class _MldInterfaceRobustness_Type(Unsigned32):
    """Custom type mldInterfaceRobustness based on Unsigned32"""
    defaultValue = 2


_MldInterfaceRobustness_Object = MibTableColumn
mldInterfaceRobustness = _MldInterfaceRobustness_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 9),
    _MldInterfaceRobustness_Type()
)
mldInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldInterfaceRobustness.setStatus("current")


class _MldInterfaceLastListenQueryIntvl_Type(Unsigned32):
    """Custom type mldInterfaceLastListenQueryIntvl based on Unsigned32"""
    defaultValue = 1


_MldInterfaceLastListenQueryIntvl_Object = MibTableColumn
mldInterfaceLastListenQueryIntvl = _MldInterfaceLastListenQueryIntvl_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 10),
    _MldInterfaceLastListenQueryIntvl_Type()
)
mldInterfaceLastListenQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldInterfaceLastListenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    mldInterfaceLastListenQueryIntvl.setUnits("seconds")


class _MldInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mldInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MldInterfaceProxyIfIndex_Object = MibTableColumn
mldInterfaceProxyIfIndex = _MldInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 11),
    _MldInterfaceProxyIfIndex_Type()
)
mldInterfaceProxyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldInterfaceProxyIfIndex.setStatus("current")
_MldInterfaceQuerierUpTime_Type = TimeTicks
_MldInterfaceQuerierUpTime_Object = MibTableColumn
mldInterfaceQuerierUpTime = _MldInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 12),
    _MldInterfaceQuerierUpTime_Type()
)
mldInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldInterfaceQuerierUpTime.setStatus("current")
_MldInterfaceQuerierExpiryTime_Type = TimeTicks
_MldInterfaceQuerierExpiryTime_Object = MibTableColumn
mldInterfaceQuerierExpiryTime = _MldInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 1, 1, 13),
    _MldInterfaceQuerierExpiryTime_Type()
)
mldInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldInterfaceQuerierExpiryTime.setStatus("current")
_MldCacheTable_Object = MibTable
mldCacheTable = _MldCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2)
)
if mibBuilder.loadTexts:
    mldCacheTable.setStatus("current")
_MldCacheEntry_Object = MibTableRow
mldCacheEntry = _MldCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1)
)
mldCacheEntry.setIndexNames(
    (0, "IPV6-MLD-MIB", "mldCacheAddress"),
    (0, "IPV6-MLD-MIB", "mldCacheIfIndex"),
)
if mibBuilder.loadTexts:
    mldCacheEntry.setStatus("current")


class _MldCacheAddress_Type(InetAddressIPv6):
    """Custom type mldCacheAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MldCacheAddress_Type.__name__ = "InetAddressIPv6"
_MldCacheAddress_Object = MibTableColumn
mldCacheAddress = _MldCacheAddress_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 1),
    _MldCacheAddress_Type()
)
mldCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldCacheAddress.setStatus("current")
_MldCacheIfIndex_Type = InterfaceIndex
_MldCacheIfIndex_Object = MibTableColumn
mldCacheIfIndex = _MldCacheIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 2),
    _MldCacheIfIndex_Type()
)
mldCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldCacheIfIndex.setStatus("current")


class _MldCacheSelf_Type(TruthValue):
    """Custom type mldCacheSelf based on TruthValue"""


_MldCacheSelf_Object = MibTableColumn
mldCacheSelf = _MldCacheSelf_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 3),
    _MldCacheSelf_Type()
)
mldCacheSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldCacheSelf.setStatus("current")


class _MldCacheLastReporter_Type(InetAddressIPv6):
    """Custom type mldCacheLastReporter based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MldCacheLastReporter_Type.__name__ = "InetAddressIPv6"
_MldCacheLastReporter_Object = MibTableColumn
mldCacheLastReporter = _MldCacheLastReporter_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 4),
    _MldCacheLastReporter_Type()
)
mldCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldCacheLastReporter.setStatus("current")
_MldCacheUpTime_Type = TimeTicks
_MldCacheUpTime_Object = MibTableColumn
mldCacheUpTime = _MldCacheUpTime_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 5),
    _MldCacheUpTime_Type()
)
mldCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldCacheUpTime.setStatus("current")
_MldCacheExpiryTime_Type = TimeTicks
_MldCacheExpiryTime_Object = MibTableColumn
mldCacheExpiryTime = _MldCacheExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 6),
    _MldCacheExpiryTime_Type()
)
mldCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldCacheExpiryTime.setStatus("current")
_MldCacheStatus_Type = RowStatus
_MldCacheStatus_Object = MibTableColumn
mldCacheStatus = _MldCacheStatus_Object(
    (1, 3, 6, 1, 2, 1, 91, 1, 2, 1, 7),
    _MldCacheStatus_Type()
)
mldCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldCacheStatus.setStatus("current")
_MldMIBConformance_ObjectIdentity = ObjectIdentity
mldMIBConformance = _MldMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 91, 2)
)
_MldMIBCompliances_ObjectIdentity = ObjectIdentity
mldMIBCompliances = _MldMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 91, 2, 1)
)
_MldMIBGroups_ObjectIdentity = ObjectIdentity
mldMIBGroups = _MldMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 91, 2, 2)
)

# Managed Objects groups

mldBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 91, 2, 2, 1)
)
mldBaseMIBGroup.setObjects(
      *(("IPV6-MLD-MIB", "mldCacheSelf"),
        ("IPV6-MLD-MIB", "mldCacheStatus"),
        ("IPV6-MLD-MIB", "mldInterfaceStatus"))
)
if mibBuilder.loadTexts:
    mldBaseMIBGroup.setStatus("current")

mldRouterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 91, 2, 2, 2)
)
mldRouterMIBGroup.setObjects(
      *(("IPV6-MLD-MIB", "mldCacheUpTime"),
        ("IPV6-MLD-MIB", "mldCacheExpiryTime"),
        ("IPV6-MLD-MIB", "mldInterfaceQueryInterval"),
        ("IPV6-MLD-MIB", "mldInterfaceJoins"),
        ("IPV6-MLD-MIB", "mldInterfaceGroups"),
        ("IPV6-MLD-MIB", "mldCacheLastReporter"),
        ("IPV6-MLD-MIB", "mldInterfaceQuerierUpTime"),
        ("IPV6-MLD-MIB", "mldInterfaceQuerierExpiryTime"),
        ("IPV6-MLD-MIB", "mldInterfaceQuerier"),
        ("IPV6-MLD-MIB", "mldInterfaceVersion"),
        ("IPV6-MLD-MIB", "mldInterfaceQueryMaxResponseDelay"),
        ("IPV6-MLD-MIB", "mldInterfaceRobustness"),
        ("IPV6-MLD-MIB", "mldInterfaceLastListenQueryIntvl"))
)
if mibBuilder.loadTexts:
    mldRouterMIBGroup.setStatus("current")

mldHostMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 91, 2, 2, 3)
)
mldHostMIBGroup.setObjects(
    ("IPV6-MLD-MIB", "mldInterfaceQuerier")
)
if mibBuilder.loadTexts:
    mldHostMIBGroup.setStatus("current")

mldProxyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 91, 2, 2, 4)
)
mldProxyMIBGroup.setObjects(
    ("IPV6-MLD-MIB", "mldInterfaceProxyIfIndex")
)
if mibBuilder.loadTexts:
    mldProxyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mldHostMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 91, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mldHostMIBCompliance.setStatus(
        "current"
    )

mldRouterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 91, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mldRouterMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV6-MLD-MIB",
    **{"mldMIB": mldMIB,
       "mldMIBObjects": mldMIBObjects,
       "mldInterfaceTable": mldInterfaceTable,
       "mldInterfaceEntry": mldInterfaceEntry,
       "mldInterfaceIfIndex": mldInterfaceIfIndex,
       "mldInterfaceQueryInterval": mldInterfaceQueryInterval,
       "mldInterfaceStatus": mldInterfaceStatus,
       "mldInterfaceVersion": mldInterfaceVersion,
       "mldInterfaceQuerier": mldInterfaceQuerier,
       "mldInterfaceQueryMaxResponseDelay": mldInterfaceQueryMaxResponseDelay,
       "mldInterfaceJoins": mldInterfaceJoins,
       "mldInterfaceGroups": mldInterfaceGroups,
       "mldInterfaceRobustness": mldInterfaceRobustness,
       "mldInterfaceLastListenQueryIntvl": mldInterfaceLastListenQueryIntvl,
       "mldInterfaceProxyIfIndex": mldInterfaceProxyIfIndex,
       "mldInterfaceQuerierUpTime": mldInterfaceQuerierUpTime,
       "mldInterfaceQuerierExpiryTime": mldInterfaceQuerierExpiryTime,
       "mldCacheTable": mldCacheTable,
       "mldCacheEntry": mldCacheEntry,
       "mldCacheAddress": mldCacheAddress,
       "mldCacheIfIndex": mldCacheIfIndex,
       "mldCacheSelf": mldCacheSelf,
       "mldCacheLastReporter": mldCacheLastReporter,
       "mldCacheUpTime": mldCacheUpTime,
       "mldCacheExpiryTime": mldCacheExpiryTime,
       "mldCacheStatus": mldCacheStatus,
       "mldMIBConformance": mldMIBConformance,
       "mldMIBCompliances": mldMIBCompliances,
       "mldHostMIBCompliance": mldHostMIBCompliance,
       "mldRouterMIBCompliance": mldRouterMIBCompliance,
       "mldMIBGroups": mldMIBGroups,
       "mldBaseMIBGroup": mldBaseMIBGroup,
       "mldRouterMIBGroup": mldRouterMIBGroup,
       "mldHostMIBGroup": mldHostMIBGroup,
       "mldProxyMIBGroup": mldProxyMIBGroup}
)
