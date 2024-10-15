# SNMP MIB module (IGMP-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IGMP-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:54 2024
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

igmpStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 85)
)
igmpStdMIB.setRevisions(
        ("2000-09-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IgmpMIBObjects_ObjectIdentity = ObjectIdentity
igmpMIBObjects = _IgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 85, 1)
)
_IgmpInterfaceTable_Object = MibTable
igmpInterfaceTable = _IgmpInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1)
)
if mibBuilder.loadTexts:
    igmpInterfaceTable.setStatus("current")
_IgmpInterfaceEntry_Object = MibTableRow
igmpInterfaceEntry = _IgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1)
)
igmpInterfaceEntry.setIndexNames(
    (0, "IGMP-STD-MIB", "igmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    igmpInterfaceEntry.setStatus("current")
_IgmpInterfaceIfIndex_Type = InterfaceIndex
_IgmpInterfaceIfIndex_Object = MibTableColumn
igmpInterfaceIfIndex = _IgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 1),
    _IgmpInterfaceIfIndex_Type()
)
igmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpInterfaceIfIndex.setStatus("current")


class _IgmpInterfaceQueryInterval_Type(Unsigned32):
    """Custom type igmpInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125


_IgmpInterfaceQueryInterval_Object = MibTableColumn
igmpInterfaceQueryInterval = _IgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 2),
    _IgmpInterfaceQueryInterval_Type()
)
igmpInterfaceQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    igmpInterfaceQueryInterval.setUnits("seconds")
_IgmpInterfaceStatus_Type = RowStatus
_IgmpInterfaceStatus_Object = MibTableColumn
igmpInterfaceStatus = _IgmpInterfaceStatus_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 3),
    _IgmpInterfaceStatus_Type()
)
igmpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceStatus.setStatus("current")


class _IgmpInterfaceVersion_Type(Unsigned32):
    """Custom type igmpInterfaceVersion based on Unsigned32"""
    defaultValue = 2


_IgmpInterfaceVersion_Object = MibTableColumn
igmpInterfaceVersion = _IgmpInterfaceVersion_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 4),
    _IgmpInterfaceVersion_Type()
)
igmpInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceVersion.setStatus("current")
_IgmpInterfaceQuerier_Type = IpAddress
_IgmpInterfaceQuerier_Object = MibTableColumn
igmpInterfaceQuerier = _IgmpInterfaceQuerier_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 5),
    _IgmpInterfaceQuerier_Type()
)
igmpInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceQuerier.setStatus("current")


class _IgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type igmpInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IgmpInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_IgmpInterfaceQueryMaxResponseTime_Object = MibTableColumn
igmpInterfaceQueryMaxResponseTime = _IgmpInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 6),
    _IgmpInterfaceQueryMaxResponseTime_Type()
)
igmpInterfaceQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    igmpInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_IgmpInterfaceQuerierUpTime_Type = TimeTicks
_IgmpInterfaceQuerierUpTime_Object = MibTableColumn
igmpInterfaceQuerierUpTime = _IgmpInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 7),
    _IgmpInterfaceQuerierUpTime_Type()
)
igmpInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceQuerierUpTime.setStatus("current")
_IgmpInterfaceQuerierExpiryTime_Type = TimeTicks
_IgmpInterfaceQuerierExpiryTime_Object = MibTableColumn
igmpInterfaceQuerierExpiryTime = _IgmpInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 8),
    _IgmpInterfaceQuerierExpiryTime_Type()
)
igmpInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceQuerierExpiryTime.setStatus("current")
_IgmpInterfaceVersion1QuerierTimer_Type = TimeTicks
_IgmpInterfaceVersion1QuerierTimer_Object = MibTableColumn
igmpInterfaceVersion1QuerierTimer = _IgmpInterfaceVersion1QuerierTimer_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 9),
    _IgmpInterfaceVersion1QuerierTimer_Type()
)
igmpInterfaceVersion1QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceVersion1QuerierTimer.setStatus("current")
_IgmpInterfaceWrongVersionQueries_Type = Counter32
_IgmpInterfaceWrongVersionQueries_Object = MibTableColumn
igmpInterfaceWrongVersionQueries = _IgmpInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 10),
    _IgmpInterfaceWrongVersionQueries_Type()
)
igmpInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceWrongVersionQueries.setStatus("current")
_IgmpInterfaceJoins_Type = Counter32
_IgmpInterfaceJoins_Object = MibTableColumn
igmpInterfaceJoins = _IgmpInterfaceJoins_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 11),
    _IgmpInterfaceJoins_Type()
)
igmpInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceJoins.setStatus("current")


class _IgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type igmpInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_IgmpInterfaceProxyIfIndex_Object = MibTableColumn
igmpInterfaceProxyIfIndex = _IgmpInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 12),
    _IgmpInterfaceProxyIfIndex_Type()
)
igmpInterfaceProxyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceProxyIfIndex.setStatus("current")
_IgmpInterfaceGroups_Type = Gauge32
_IgmpInterfaceGroups_Object = MibTableColumn
igmpInterfaceGroups = _IgmpInterfaceGroups_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 13),
    _IgmpInterfaceGroups_Type()
)
igmpInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceGroups.setStatus("current")


class _IgmpInterfaceRobustness_Type(Unsigned32):
    """Custom type igmpInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IgmpInterfaceRobustness_Type.__name__ = "Unsigned32"
_IgmpInterfaceRobustness_Object = MibTableColumn
igmpInterfaceRobustness = _IgmpInterfaceRobustness_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 14),
    _IgmpInterfaceRobustness_Type()
)
igmpInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceRobustness.setStatus("current")


class _IgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type igmpInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IgmpInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_IgmpInterfaceLastMembQueryIntvl_Object = MibTableColumn
igmpInterfaceLastMembQueryIntvl = _IgmpInterfaceLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 1, 1, 15),
    _IgmpInterfaceLastMembQueryIntvl_Type()
)
igmpInterfaceLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    igmpInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")
_IgmpCacheTable_Object = MibTable
igmpCacheTable = _IgmpCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2)
)
if mibBuilder.loadTexts:
    igmpCacheTable.setStatus("current")
_IgmpCacheEntry_Object = MibTableRow
igmpCacheEntry = _IgmpCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1)
)
igmpCacheEntry.setIndexNames(
    (0, "IGMP-STD-MIB", "igmpCacheAddress"),
    (0, "IGMP-STD-MIB", "igmpCacheIfIndex"),
)
if mibBuilder.loadTexts:
    igmpCacheEntry.setStatus("current")
_IgmpCacheAddress_Type = IpAddress
_IgmpCacheAddress_Object = MibTableColumn
igmpCacheAddress = _IgmpCacheAddress_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 1),
    _IgmpCacheAddress_Type()
)
igmpCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCacheAddress.setStatus("current")
_IgmpCacheIfIndex_Type = InterfaceIndex
_IgmpCacheIfIndex_Object = MibTableColumn
igmpCacheIfIndex = _IgmpCacheIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 2),
    _IgmpCacheIfIndex_Type()
)
igmpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCacheIfIndex.setStatus("current")


class _IgmpCacheSelf_Type(TruthValue):
    """Custom type igmpCacheSelf based on TruthValue"""


_IgmpCacheSelf_Object = MibTableColumn
igmpCacheSelf = _IgmpCacheSelf_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 3),
    _IgmpCacheSelf_Type()
)
igmpCacheSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpCacheSelf.setStatus("current")
_IgmpCacheLastReporter_Type = IpAddress
_IgmpCacheLastReporter_Object = MibTableColumn
igmpCacheLastReporter = _IgmpCacheLastReporter_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 4),
    _IgmpCacheLastReporter_Type()
)
igmpCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheLastReporter.setStatus("current")
_IgmpCacheUpTime_Type = TimeTicks
_IgmpCacheUpTime_Object = MibTableColumn
igmpCacheUpTime = _IgmpCacheUpTime_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 5),
    _IgmpCacheUpTime_Type()
)
igmpCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheUpTime.setStatus("current")
_IgmpCacheExpiryTime_Type = TimeTicks
_IgmpCacheExpiryTime_Object = MibTableColumn
igmpCacheExpiryTime = _IgmpCacheExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 6),
    _IgmpCacheExpiryTime_Type()
)
igmpCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheExpiryTime.setStatus("current")
_IgmpCacheStatus_Type = RowStatus
_IgmpCacheStatus_Object = MibTableColumn
igmpCacheStatus = _IgmpCacheStatus_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 7),
    _IgmpCacheStatus_Type()
)
igmpCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpCacheStatus.setStatus("current")
_IgmpCacheVersion1HostTimer_Type = TimeTicks
_IgmpCacheVersion1HostTimer_Object = MibTableColumn
igmpCacheVersion1HostTimer = _IgmpCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 2, 1, 85, 1, 2, 1, 8),
    _IgmpCacheVersion1HostTimer_Type()
)
igmpCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheVersion1HostTimer.setStatus("current")
_IgmpMIBConformance_ObjectIdentity = ObjectIdentity
igmpMIBConformance = _IgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 85, 2)
)
_IgmpMIBCompliances_ObjectIdentity = ObjectIdentity
igmpMIBCompliances = _IgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 85, 2, 1)
)
_IgmpMIBGroups_ObjectIdentity = ObjectIdentity
igmpMIBGroups = _IgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 85, 2, 2)
)

# Managed Objects groups

igmpBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 85, 2, 2, 1)
)
igmpBaseMIBGroup.setObjects(
      *(("IGMP-STD-MIB", "igmpCacheSelf"),
        ("IGMP-STD-MIB", "igmpCacheStatus"),
        ("IGMP-STD-MIB", "igmpInterfaceStatus"))
)
if mibBuilder.loadTexts:
    igmpBaseMIBGroup.setStatus("current")

igmpRouterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 85, 2, 2, 2)
)
igmpRouterMIBGroup.setObjects(
      *(("IGMP-STD-MIB", "igmpCacheUpTime"),
        ("IGMP-STD-MIB", "igmpCacheExpiryTime"),
        ("IGMP-STD-MIB", "igmpInterfaceJoins"),
        ("IGMP-STD-MIB", "igmpInterfaceGroups"),
        ("IGMP-STD-MIB", "igmpCacheLastReporter"),
        ("IGMP-STD-MIB", "igmpInterfaceQuerierUpTime"),
        ("IGMP-STD-MIB", "igmpInterfaceQuerierExpiryTime"),
        ("IGMP-STD-MIB", "igmpInterfaceQueryInterval"))
)
if mibBuilder.loadTexts:
    igmpRouterMIBGroup.setStatus("current")

igmpV2HostMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 85, 2, 2, 3)
)
igmpV2HostMIBGroup.setObjects(
    ("IGMP-STD-MIB", "igmpInterfaceVersion1QuerierTimer")
)
if mibBuilder.loadTexts:
    igmpV2HostMIBGroup.setStatus("current")

igmpHostOptMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 85, 2, 2, 4)
)
igmpHostOptMIBGroup.setObjects(
      *(("IGMP-STD-MIB", "igmpCacheLastReporter"),
        ("IGMP-STD-MIB", "igmpInterfaceQuerier"))
)
if mibBuilder.loadTexts:
    igmpHostOptMIBGroup.setStatus("current")

igmpV2RouterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 85, 2, 2, 5)
)
igmpV2RouterMIBGroup.setObjects(
      *(("IGMP-STD-MIB", "igmpInterfaceVersion"),
        ("IGMP-STD-MIB", "igmpInterfaceQuerier"),
        ("IGMP-STD-MIB", "igmpInterfaceQueryMaxResponseTime"),
        ("IGMP-STD-MIB", "igmpInterfaceRobustness"),
        ("IGMP-STD-MIB", "igmpInterfaceWrongVersionQueries"),
        ("IGMP-STD-MIB", "igmpInterfaceLastMembQueryIntvl"),
        ("IGMP-STD-MIB", "igmpCacheVersion1HostTimer"))
)
if mibBuilder.loadTexts:
    igmpV2RouterMIBGroup.setStatus("current")

igmpV2ProxyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 85, 2, 2, 6)
)
igmpV2ProxyMIBGroup.setObjects(
    ("IGMP-STD-MIB", "igmpInterfaceProxyIfIndex")
)
if mibBuilder.loadTexts:
    igmpV2ProxyMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

igmpV1HostMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 85, 2, 1, 1)
)
if mibBuilder.loadTexts:
    igmpV1HostMIBCompliance.setStatus(
        "current"
    )

igmpV1RouterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 85, 2, 1, 2)
)
if mibBuilder.loadTexts:
    igmpV1RouterMIBCompliance.setStatus(
        "current"
    )

igmpV2HostMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 85, 2, 1, 3)
)
if mibBuilder.loadTexts:
    igmpV2HostMIBCompliance.setStatus(
        "current"
    )

igmpV2RouterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 85, 2, 1, 4)
)
if mibBuilder.loadTexts:
    igmpV2RouterMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IGMP-STD-MIB",
    **{"igmpStdMIB": igmpStdMIB,
       "igmpMIBObjects": igmpMIBObjects,
       "igmpInterfaceTable": igmpInterfaceTable,
       "igmpInterfaceEntry": igmpInterfaceEntry,
       "igmpInterfaceIfIndex": igmpInterfaceIfIndex,
       "igmpInterfaceQueryInterval": igmpInterfaceQueryInterval,
       "igmpInterfaceStatus": igmpInterfaceStatus,
       "igmpInterfaceVersion": igmpInterfaceVersion,
       "igmpInterfaceQuerier": igmpInterfaceQuerier,
       "igmpInterfaceQueryMaxResponseTime": igmpInterfaceQueryMaxResponseTime,
       "igmpInterfaceQuerierUpTime": igmpInterfaceQuerierUpTime,
       "igmpInterfaceQuerierExpiryTime": igmpInterfaceQuerierExpiryTime,
       "igmpInterfaceVersion1QuerierTimer": igmpInterfaceVersion1QuerierTimer,
       "igmpInterfaceWrongVersionQueries": igmpInterfaceWrongVersionQueries,
       "igmpInterfaceJoins": igmpInterfaceJoins,
       "igmpInterfaceProxyIfIndex": igmpInterfaceProxyIfIndex,
       "igmpInterfaceGroups": igmpInterfaceGroups,
       "igmpInterfaceRobustness": igmpInterfaceRobustness,
       "igmpInterfaceLastMembQueryIntvl": igmpInterfaceLastMembQueryIntvl,
       "igmpCacheTable": igmpCacheTable,
       "igmpCacheEntry": igmpCacheEntry,
       "igmpCacheAddress": igmpCacheAddress,
       "igmpCacheIfIndex": igmpCacheIfIndex,
       "igmpCacheSelf": igmpCacheSelf,
       "igmpCacheLastReporter": igmpCacheLastReporter,
       "igmpCacheUpTime": igmpCacheUpTime,
       "igmpCacheExpiryTime": igmpCacheExpiryTime,
       "igmpCacheStatus": igmpCacheStatus,
       "igmpCacheVersion1HostTimer": igmpCacheVersion1HostTimer,
       "igmpMIBConformance": igmpMIBConformance,
       "igmpMIBCompliances": igmpMIBCompliances,
       "igmpV1HostMIBCompliance": igmpV1HostMIBCompliance,
       "igmpV1RouterMIBCompliance": igmpV1RouterMIBCompliance,
       "igmpV2HostMIBCompliance": igmpV2HostMIBCompliance,
       "igmpV2RouterMIBCompliance": igmpV2RouterMIBCompliance,
       "igmpMIBGroups": igmpMIBGroups,
       "igmpBaseMIBGroup": igmpBaseMIBGroup,
       "igmpRouterMIBGroup": igmpRouterMIBGroup,
       "igmpV2HostMIBGroup": igmpV2HostMIBGroup,
       "igmpHostOptMIBGroup": igmpHostOptMIBGroup,
       "igmpV2RouterMIBGroup": igmpV2RouterMIBGroup,
       "igmpV2ProxyMIBGroup": igmpV2ProxyMIBGroup}
)
