# SNMP MIB module (IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:49 2024
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
 experimental,
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
    "experimental",
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

igmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 59)
)
igmpMIB.setRevisions(
        ("1995-08-15 00:00",
         "1997-01-06 00:00",
         "1997-12-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IgmpMIBObjects_ObjectIdentity = ObjectIdentity
igmpMIBObjects = _IgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 59, 1)
)
_Igmp_ObjectIdentity = ObjectIdentity
igmp = _Igmp_ObjectIdentity(
    (1, 3, 6, 1, 3, 59, 1, 1)
)
_IgmpInterfaceTable_Object = MibTable
igmpInterfaceTable = _IgmpInterfaceTable_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1)
)
if mibBuilder.loadTexts:
    igmpInterfaceTable.setStatus("current")
_IgmpInterfaceEntry_Object = MibTableRow
igmpInterfaceEntry = _IgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1)
)
igmpInterfaceEntry.setIndexNames(
    (0, "IGMP-MIB", "igmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    igmpInterfaceEntry.setStatus("current")


class _IgmpInterfaceIfIndex_Type(Integer32):
    """Custom type igmpInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IgmpInterfaceIfIndex_Type.__name__ = "Integer32"
_IgmpInterfaceIfIndex_Object = MibTableColumn
igmpInterfaceIfIndex = _IgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 1),
    _IgmpInterfaceIfIndex_Type()
)
igmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpInterfaceIfIndex.setStatus("current")


class _IgmpInterfaceQueryInterval_Type(Integer32):
    """Custom type igmpInterfaceQueryInterval based on Integer32"""
    defaultValue = 60


_IgmpInterfaceQueryInterval_Object = MibTableColumn
igmpInterfaceQueryInterval = _IgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 3),
    _IgmpInterfaceStatus_Type()
)
igmpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceStatus.setStatus("current")


class _IgmpInterfaceVersion_Type(Integer32):
    """Custom type igmpInterfaceVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_IgmpInterfaceVersion_Type.__name__ = "Integer32"
_IgmpInterfaceVersion_Object = MibTableColumn
igmpInterfaceVersion = _IgmpInterfaceVersion_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 4),
    _IgmpInterfaceVersion_Type()
)
igmpInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceVersion.setStatus("current")
_IgmpInterfaceQuerier_Type = IpAddress
_IgmpInterfaceQuerier_Object = MibTableColumn
igmpInterfaceQuerier = _IgmpInterfaceQuerier_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 5),
    _IgmpInterfaceQuerier_Type()
)
igmpInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceQuerier.setStatus("current")


class _IgmpInterfaceQueryMaxResponseTime_Type(Integer32):
    """Custom type igmpInterfaceQueryMaxResponseTime based on Integer32"""
    defaultValue = 10


_IgmpInterfaceQueryMaxResponseTime_Object = MibTableColumn
igmpInterfaceQueryMaxResponseTime = _IgmpInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 6),
    _IgmpInterfaceQueryMaxResponseTime_Type()
)
igmpInterfaceQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    igmpInterfaceQueryMaxResponseTime.setUnits("seconds")


class _IgmpInterfaceQuerierPresentTimeout_Type(Integer32):
    """Custom type igmpInterfaceQuerierPresentTimeout based on Integer32"""
    defaultValue = 255


_IgmpInterfaceQuerierPresentTimeout_Object = MibTableColumn
igmpInterfaceQuerierPresentTimeout = _IgmpInterfaceQuerierPresentTimeout_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 7),
    _IgmpInterfaceQuerierPresentTimeout_Type()
)
igmpInterfaceQuerierPresentTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceQuerierPresentTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    igmpInterfaceQuerierPresentTimeout.setUnits("seconds")


class _IgmpInterfaceLeaveEnabled_Type(TruthValue):
    """Custom type igmpInterfaceLeaveEnabled based on TruthValue"""


_IgmpInterfaceLeaveEnabled_Object = MibTableColumn
igmpInterfaceLeaveEnabled = _IgmpInterfaceLeaveEnabled_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 8),
    _IgmpInterfaceLeaveEnabled_Type()
)
igmpInterfaceLeaveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceLeaveEnabled.setStatus("deprecated")
_IgmpInterfaceVersion1QuerierTimer_Type = Integer32
_IgmpInterfaceVersion1QuerierTimer_Object = MibTableColumn
igmpInterfaceVersion1QuerierTimer = _IgmpInterfaceVersion1QuerierTimer_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 9),
    _IgmpInterfaceVersion1QuerierTimer_Type()
)
igmpInterfaceVersion1QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceVersion1QuerierTimer.setStatus("current")
if mibBuilder.loadTexts:
    igmpInterfaceVersion1QuerierTimer.setUnits("seconds")
_IgmpInterfaceWrongVersionQueries_Type = Counter32
_IgmpInterfaceWrongVersionQueries_Object = MibTableColumn
igmpInterfaceWrongVersionQueries = _IgmpInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 10),
    _IgmpInterfaceWrongVersionQueries_Type()
)
igmpInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceWrongVersionQueries.setStatus("current")
_IgmpInterfaceJoins_Type = Counter32
_IgmpInterfaceJoins_Object = MibTableColumn
igmpInterfaceJoins = _IgmpInterfaceJoins_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 11),
    _IgmpInterfaceJoins_Type()
)
igmpInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceJoins.setStatus("current")
_IgmpInterfaceLeaves_Type = Counter32
_IgmpInterfaceLeaves_Object = MibTableColumn
igmpInterfaceLeaves = _IgmpInterfaceLeaves_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 12),
    _IgmpInterfaceLeaves_Type()
)
igmpInterfaceLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceLeaves.setStatus("deprecated")
_IgmpInterfaceGroups_Type = Gauge32
_IgmpInterfaceGroups_Object = MibTableColumn
igmpInterfaceGroups = _IgmpInterfaceGroups_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 13),
    _IgmpInterfaceGroups_Type()
)
igmpInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceGroups.setStatus("current")


class _IgmpInterfaceRobustness_Type(Integer32):
    """Custom type igmpInterfaceRobustness based on Integer32"""
    defaultValue = 2


_IgmpInterfaceRobustness_Object = MibTableColumn
igmpInterfaceRobustness = _IgmpInterfaceRobustness_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 1, 1, 14),
    _IgmpInterfaceRobustness_Type()
)
igmpInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpInterfaceRobustness.setStatus("current")
_IgmpCacheTable_Object = MibTable
igmpCacheTable = _IgmpCacheTable_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2)
)
if mibBuilder.loadTexts:
    igmpCacheTable.setStatus("current")
_IgmpCacheEntry_Object = MibTableRow
igmpCacheEntry = _IgmpCacheEntry_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1)
)
igmpCacheEntry.setIndexNames(
    (0, "IGMP-MIB", "igmpCacheAddress"),
    (0, "IGMP-MIB", "igmpCacheIfIndex"),
)
if mibBuilder.loadTexts:
    igmpCacheEntry.setStatus("current")
_IgmpCacheAddress_Type = IpAddress
_IgmpCacheAddress_Object = MibTableColumn
igmpCacheAddress = _IgmpCacheAddress_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 1),
    _IgmpCacheAddress_Type()
)
igmpCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCacheAddress.setStatus("current")


class _IgmpCacheIfIndex_Type(Integer32):
    """Custom type igmpCacheIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IgmpCacheIfIndex_Type.__name__ = "Integer32"
_IgmpCacheIfIndex_Object = MibTableColumn
igmpCacheIfIndex = _IgmpCacheIfIndex_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 2),
    _IgmpCacheIfIndex_Type()
)
igmpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCacheIfIndex.setStatus("current")


class _IgmpCacheSelf_Type(TruthValue):
    """Custom type igmpCacheSelf based on TruthValue"""


_IgmpCacheSelf_Object = MibTableColumn
igmpCacheSelf = _IgmpCacheSelf_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 3),
    _IgmpCacheSelf_Type()
)
igmpCacheSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpCacheSelf.setStatus("current")
_IgmpCacheLastReporter_Type = IpAddress
_IgmpCacheLastReporter_Object = MibTableColumn
igmpCacheLastReporter = _IgmpCacheLastReporter_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 4),
    _IgmpCacheLastReporter_Type()
)
igmpCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheLastReporter.setStatus("current")
_IgmpCacheUpTime_Type = TimeTicks
_IgmpCacheUpTime_Object = MibTableColumn
igmpCacheUpTime = _IgmpCacheUpTime_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 5),
    _IgmpCacheUpTime_Type()
)
igmpCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheUpTime.setStatus("current")
_IgmpCacheExpiryTime_Type = TimeTicks
_IgmpCacheExpiryTime_Object = MibTableColumn
igmpCacheExpiryTime = _IgmpCacheExpiryTime_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 6),
    _IgmpCacheExpiryTime_Type()
)
igmpCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheExpiryTime.setStatus("current")
_IgmpCacheStatus_Type = RowStatus
_IgmpCacheStatus_Object = MibTableColumn
igmpCacheStatus = _IgmpCacheStatus_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 7),
    _IgmpCacheStatus_Type()
)
igmpCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpCacheStatus.setStatus("current")
_IgmpCacheVersion1HostTimer_Type = Integer32
_IgmpCacheVersion1HostTimer_Object = MibTableColumn
igmpCacheVersion1HostTimer = _IgmpCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 3, 59, 1, 1, 2, 1, 8),
    _IgmpCacheVersion1HostTimer_Type()
)
igmpCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheVersion1HostTimer.setStatus("current")
if mibBuilder.loadTexts:
    igmpCacheVersion1HostTimer.setUnits("seconds")
_IgmpMIBConformance_ObjectIdentity = ObjectIdentity
igmpMIBConformance = _IgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 59, 2)
)
_IgmpMIBCompliances_ObjectIdentity = ObjectIdentity
igmpMIBCompliances = _IgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 59, 2, 1)
)
_IgmpMIBGroups_ObjectIdentity = ObjectIdentity
igmpMIBGroups = _IgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 59, 2, 2)
)

# Managed Objects groups

igmpBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 59, 2, 2, 1)
)
igmpBaseMIBGroup.setObjects(
      *(("IGMP-MIB", "igmpCacheSelf"),
        ("IGMP-MIB", "igmpCacheLastReporter"),
        ("IGMP-MIB", "igmpCacheStatus"),
        ("IGMP-MIB", "igmpInterfaceStatus"))
)
if mibBuilder.loadTexts:
    igmpBaseMIBGroup.setStatus("current")

igmpRouterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 59, 2, 2, 2)
)
igmpRouterMIBGroup.setObjects(
      *(("IGMP-MIB", "igmpCacheUpTime"),
        ("IGMP-MIB", "igmpCacheExpiryTime"),
        ("IGMP-MIB", "igmpInterfaceQueryInterval"))
)
if mibBuilder.loadTexts:
    igmpRouterMIBGroup.setStatus("current")

igmpV2HostMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 59, 2, 2, 3)
)
igmpV2HostMIBGroup.setObjects(
      *(("IGMP-MIB", "igmpInterfaceQuerier"),
        ("IGMP-MIB", "igmpInterfaceVersion1QuerierTimer"))
)
if mibBuilder.loadTexts:
    igmpV2HostMIBGroup.setStatus("current")

igmpRouterVersion2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 59, 2, 2, 4)
)
igmpRouterVersion2MIBGroup.setObjects(
      *(("IGMP-MIB", "igmpInterfaceVersion"),
        ("IGMP-MIB", "igmpInterfaceQueryMaxResponseTime"),
        ("IGMP-MIB", "igmpInterfaceQuerierPresentTimeout"),
        ("IGMP-MIB", "igmpInterfaceLeaveEnabled"),
        ("IGMP-MIB", "igmpInterfaceWrongVersionQueries"),
        ("IGMP-MIB", "igmpInterfaceJoins"),
        ("IGMP-MIB", "igmpInterfaceLeaves"),
        ("IGMP-MIB", "igmpCacheVersion1HostTimer"))
)
if mibBuilder.loadTexts:
    igmpRouterVersion2MIBGroup.setStatus("deprecated")

igmpV2RouterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 59, 2, 2, 5)
)
igmpV2RouterMIBGroup.setObjects(
      *(("IGMP-MIB", "igmpInterfaceVersion"),
        ("IGMP-MIB", "igmpInterfaceQuerier"),
        ("IGMP-MIB", "igmpInterfaceQueryMaxResponseTime"),
        ("IGMP-MIB", "igmpInterfaceRobustness"),
        ("IGMP-MIB", "igmpInterfaceWrongVersionQueries"),
        ("IGMP-MIB", "igmpInterfaceJoins"),
        ("IGMP-MIB", "igmpInterfaceGroups"),
        ("IGMP-MIB", "igmpCacheVersion1HostTimer"))
)
if mibBuilder.loadTexts:
    igmpV2RouterMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

igmpV1HostMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 59, 2, 1, 1)
)
if mibBuilder.loadTexts:
    igmpV1HostMIBCompliance.setStatus(
        "current"
    )

igmpV1RouterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 59, 2, 1, 2)
)
if mibBuilder.loadTexts:
    igmpV1RouterMIBCompliance.setStatus(
        "current"
    )

igmpV2HostMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 59, 2, 1, 3)
)
if mibBuilder.loadTexts:
    igmpV2HostMIBCompliance.setStatus(
        "current"
    )

igmpV2RouterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 59, 2, 1, 4)
)
if mibBuilder.loadTexts:
    igmpV2RouterMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IGMP-MIB",
    **{"igmpMIB": igmpMIB,
       "igmpMIBObjects": igmpMIBObjects,
       "igmp": igmp,
       "igmpInterfaceTable": igmpInterfaceTable,
       "igmpInterfaceEntry": igmpInterfaceEntry,
       "igmpInterfaceIfIndex": igmpInterfaceIfIndex,
       "igmpInterfaceQueryInterval": igmpInterfaceQueryInterval,
       "igmpInterfaceStatus": igmpInterfaceStatus,
       "igmpInterfaceVersion": igmpInterfaceVersion,
       "igmpInterfaceQuerier": igmpInterfaceQuerier,
       "igmpInterfaceQueryMaxResponseTime": igmpInterfaceQueryMaxResponseTime,
       "igmpInterfaceQuerierPresentTimeout": igmpInterfaceQuerierPresentTimeout,
       "igmpInterfaceLeaveEnabled": igmpInterfaceLeaveEnabled,
       "igmpInterfaceVersion1QuerierTimer": igmpInterfaceVersion1QuerierTimer,
       "igmpInterfaceWrongVersionQueries": igmpInterfaceWrongVersionQueries,
       "igmpInterfaceJoins": igmpInterfaceJoins,
       "igmpInterfaceLeaves": igmpInterfaceLeaves,
       "igmpInterfaceGroups": igmpInterfaceGroups,
       "igmpInterfaceRobustness": igmpInterfaceRobustness,
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
       "igmpRouterVersion2MIBGroup": igmpRouterVersion2MIBGroup,
       "igmpV2RouterMIBGroup": igmpV2RouterMIBGroup}
)
