# SNMP MIB module (HUAWEI-MGMD-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MGMD-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:59 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwMgmdStdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3)
)
hwMgmdStdMib.setRevisions(
        ("2014-07-09 00:00",
         "2014-07-01 00:00",
         "2014-06-20 00:00",
         "2013-08-28 00:00",
         "2007-04-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWMgmdCtlMsgState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("invalid", 2),
          ("valid", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwMcast_ObjectIdentity = ObjectIdentity
hwMcast = _HwMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149)
)
_HwMgmdMibObjects_ObjectIdentity = ObjectIdentity
hwMgmdMibObjects = _HwMgmdMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1)
)
_HwMgmdRouterInterfaceTable_Object = MibTable
hwMgmdRouterInterfaceTable = _HwMgmdRouterInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceTable.setStatus("current")
_HwMgmdRouterInterfaceEntry_Object = MibTableRow
hwMgmdRouterInterfaceEntry = _HwMgmdRouterInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1)
)
hwMgmdRouterInterfaceEntry.setIndexNames(
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceIfIndex"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceQuerierType"),
)
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceEntry.setStatus("current")
_HwMgmdRouterInterfaceIfIndex_Type = InterfaceIndex
_HwMgmdRouterInterfaceIfIndex_Object = MibTableColumn
hwMgmdRouterInterfaceIfIndex = _HwMgmdRouterInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 1),
    _HwMgmdRouterInterfaceIfIndex_Type()
)
hwMgmdRouterInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceIfIndex.setStatus("current")
_HwMgmdRouterInterfaceQuerierType_Type = InetAddressType
_HwMgmdRouterInterfaceQuerierType_Object = MibTableColumn
hwMgmdRouterInterfaceQuerierType = _HwMgmdRouterInterfaceQuerierType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 2),
    _HwMgmdRouterInterfaceQuerierType_Type()
)
hwMgmdRouterInterfaceQuerierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQuerierType.setStatus("current")


class _HwMgmdRouterInterfaceQuerier_Type(InetAddress):
    """Custom type hwMgmdRouterInterfaceQuerier based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HwMgmdRouterInterfaceQuerier_Type.__name__ = "InetAddress"
_HwMgmdRouterInterfaceQuerier_Object = MibTableColumn
hwMgmdRouterInterfaceQuerier = _HwMgmdRouterInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 3),
    _HwMgmdRouterInterfaceQuerier_Type()
)
hwMgmdRouterInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQuerier.setStatus("current")


class _HwMgmdRouterInterfaceQueryInterval_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_HwMgmdRouterInterfaceQueryInterval_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceQueryInterval_Object = MibTableColumn
hwMgmdRouterInterfaceQueryInterval = _HwMgmdRouterInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 4),
    _HwMgmdRouterInterfaceQueryInterval_Type()
)
hwMgmdRouterInterfaceQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQueryInterval.setUnits("seconds")
_HwMgmdRouterInterfaceStatus_Type = RowStatus
_HwMgmdRouterInterfaceStatus_Object = MibTableColumn
hwMgmdRouterInterfaceStatus = _HwMgmdRouterInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 5),
    _HwMgmdRouterInterfaceStatus_Type()
)
hwMgmdRouterInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceStatus.setStatus("current")


class _HwMgmdRouterInterfaceVersion_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceVersion based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HwMgmdRouterInterfaceVersion_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceVersion_Object = MibTableColumn
hwMgmdRouterInterfaceVersion = _HwMgmdRouterInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 6),
    _HwMgmdRouterInterfaceVersion_Type()
)
hwMgmdRouterInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceVersion.setStatus("current")


class _HwMgmdRouterInterfaceQueryMaxResponseTime_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_HwMgmdRouterInterfaceQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceQueryMaxResponseTime_Object = MibTableColumn
hwMgmdRouterInterfaceQueryMaxResponseTime = _HwMgmdRouterInterfaceQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 7),
    _HwMgmdRouterInterfaceQueryMaxResponseTime_Type()
)
hwMgmdRouterInterfaceQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQueryMaxResponseTime.setUnits("tenths of seconds")
_HwMgmdRouterInterfaceQuerierUpTime_Type = TimeTicks
_HwMgmdRouterInterfaceQuerierUpTime_Object = MibTableColumn
hwMgmdRouterInterfaceQuerierUpTime = _HwMgmdRouterInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 8),
    _HwMgmdRouterInterfaceQuerierUpTime_Type()
)
hwMgmdRouterInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQuerierUpTime.setStatus("current")
_HwMgmdRouterInterfaceQuerierExpiryTime_Type = TimeTicks
_HwMgmdRouterInterfaceQuerierExpiryTime_Object = MibTableColumn
hwMgmdRouterInterfaceQuerierExpiryTime = _HwMgmdRouterInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 9),
    _HwMgmdRouterInterfaceQuerierExpiryTime_Type()
)
hwMgmdRouterInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceQuerierExpiryTime.setStatus("current")
_HwMgmdRouterInterfaceWrongVersionQueries_Type = Counter32
_HwMgmdRouterInterfaceWrongVersionQueries_Object = MibTableColumn
hwMgmdRouterInterfaceWrongVersionQueries = _HwMgmdRouterInterfaceWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 10),
    _HwMgmdRouterInterfaceWrongVersionQueries_Type()
)
hwMgmdRouterInterfaceWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceWrongVersionQueries.setStatus("current")
_HwMgmdRouterInterfaceJoins_Type = Counter32
_HwMgmdRouterInterfaceJoins_Object = MibTableColumn
hwMgmdRouterInterfaceJoins = _HwMgmdRouterInterfaceJoins_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 11),
    _HwMgmdRouterInterfaceJoins_Type()
)
hwMgmdRouterInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceJoins.setStatus("current")


class _HwMgmdRouterInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type hwMgmdRouterInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_HwMgmdRouterInterfaceProxyIfIndex_Object = MibTableColumn
hwMgmdRouterInterfaceProxyIfIndex = _HwMgmdRouterInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 12),
    _HwMgmdRouterInterfaceProxyIfIndex_Type()
)
hwMgmdRouterInterfaceProxyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceProxyIfIndex.setStatus("current")
_HwMgmdRouterInterfaceGroups_Type = Gauge32
_HwMgmdRouterInterfaceGroups_Object = MibTableColumn
hwMgmdRouterInterfaceGroups = _HwMgmdRouterInterfaceGroups_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 13),
    _HwMgmdRouterInterfaceGroups_Type()
)
hwMgmdRouterInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceGroups.setStatus("current")


class _HwMgmdRouterInterfaceRobustness_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMgmdRouterInterfaceRobustness_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceRobustness_Object = MibTableColumn
hwMgmdRouterInterfaceRobustness = _HwMgmdRouterInterfaceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 14),
    _HwMgmdRouterInterfaceRobustness_Type()
)
hwMgmdRouterInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceRobustness.setStatus("current")


class _HwMgmdRouterInterfaceLastMembQueryIntvl_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceLastMembQueryIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_HwMgmdRouterInterfaceLastMembQueryIntvl_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceLastMembQueryIntvl_Object = MibTableColumn
hwMgmdRouterInterfaceLastMembQueryIntvl = _HwMgmdRouterInterfaceLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 15),
    _HwMgmdRouterInterfaceLastMembQueryIntvl_Type()
)
hwMgmdRouterInterfaceLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceLastMembQueryIntvl.setUnits("tenths of seconds")


class _HwMgmdRouterInterfaceLastMembQueryCount_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceLastMembQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMgmdRouterInterfaceLastMembQueryCount_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceLastMembQueryCount_Object = MibTableColumn
hwMgmdRouterInterfaceLastMembQueryCount = _HwMgmdRouterInterfaceLastMembQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 16),
    _HwMgmdRouterInterfaceLastMembQueryCount_Type()
)
hwMgmdRouterInterfaceLastMembQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceLastMembQueryCount.setStatus("current")


class _HwMgmdRouterInterfaceStartupQueryCount_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceStartupQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMgmdRouterInterfaceStartupQueryCount_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceStartupQueryCount_Object = MibTableColumn
hwMgmdRouterInterfaceStartupQueryCount = _HwMgmdRouterInterfaceStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 17),
    _HwMgmdRouterInterfaceStartupQueryCount_Type()
)
hwMgmdRouterInterfaceStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceStartupQueryCount.setStatus("current")


class _HwMgmdRouterInterfaceStartupQueryInterval_Type(Unsigned32):
    """Custom type hwMgmdRouterInterfaceStartupQueryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744),
    )


_HwMgmdRouterInterfaceStartupQueryInterval_Type.__name__ = "Unsigned32"
_HwMgmdRouterInterfaceStartupQueryInterval_Object = MibTableColumn
hwMgmdRouterInterfaceStartupQueryInterval = _HwMgmdRouterInterfaceStartupQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 4, 1, 18),
    _HwMgmdRouterInterfaceStartupQueryInterval_Type()
)
hwMgmdRouterInterfaceStartupQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceStartupQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwMgmdRouterInterfaceStartupQueryInterval.setUnits("seconds")
_HwMgmdRouterCacheTable_Object = MibTable
hwMgmdRouterCacheTable = _HwMgmdRouterCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6)
)
if mibBuilder.loadTexts:
    hwMgmdRouterCacheTable.setStatus("current")
_HwMgmdRouterCacheEntry_Object = MibTableRow
hwMgmdRouterCacheEntry = _HwMgmdRouterCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1)
)
hwMgmdRouterCacheEntry.setIndexNames(
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheAddressType"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheAddress"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheIfIndex"),
)
if mibBuilder.loadTexts:
    hwMgmdRouterCacheEntry.setStatus("current")
_HwMgmdRouterCacheAddressType_Type = InetAddressType
_HwMgmdRouterCacheAddressType_Object = MibTableColumn
hwMgmdRouterCacheAddressType = _HwMgmdRouterCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 1),
    _HwMgmdRouterCacheAddressType_Type()
)
hwMgmdRouterCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheAddressType.setStatus("current")


class _HwMgmdRouterCacheAddress_Type(InetAddress):
    """Custom type hwMgmdRouterCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HwMgmdRouterCacheAddress_Type.__name__ = "InetAddress"
_HwMgmdRouterCacheAddress_Object = MibTableColumn
hwMgmdRouterCacheAddress = _HwMgmdRouterCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 2),
    _HwMgmdRouterCacheAddress_Type()
)
hwMgmdRouterCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheAddress.setStatus("current")
_HwMgmdRouterCacheIfIndex_Type = InterfaceIndex
_HwMgmdRouterCacheIfIndex_Object = MibTableColumn
hwMgmdRouterCacheIfIndex = _HwMgmdRouterCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 3),
    _HwMgmdRouterCacheIfIndex_Type()
)
hwMgmdRouterCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheIfIndex.setStatus("current")
_HwMgmdRouterCacheLastReporter_Type = InetAddress
_HwMgmdRouterCacheLastReporter_Object = MibTableColumn
hwMgmdRouterCacheLastReporter = _HwMgmdRouterCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 4),
    _HwMgmdRouterCacheLastReporter_Type()
)
hwMgmdRouterCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheLastReporter.setStatus("current")
_HwMgmdRouterCacheUpTime_Type = TimeTicks
_HwMgmdRouterCacheUpTime_Object = MibTableColumn
hwMgmdRouterCacheUpTime = _HwMgmdRouterCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 5),
    _HwMgmdRouterCacheUpTime_Type()
)
hwMgmdRouterCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheUpTime.setStatus("current")
_HwMgmdRouterCacheExpiryTime_Type = TimeTicks
_HwMgmdRouterCacheExpiryTime_Object = MibTableColumn
hwMgmdRouterCacheExpiryTime = _HwMgmdRouterCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 6),
    _HwMgmdRouterCacheExpiryTime_Type()
)
hwMgmdRouterCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheExpiryTime.setStatus("current")
_HwMgmdRouterCacheExcludeModeExpiryTimer_Type = TimeTicks
_HwMgmdRouterCacheExcludeModeExpiryTimer_Object = MibTableColumn
hwMgmdRouterCacheExcludeModeExpiryTimer = _HwMgmdRouterCacheExcludeModeExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 7),
    _HwMgmdRouterCacheExcludeModeExpiryTimer_Type()
)
hwMgmdRouterCacheExcludeModeExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheExcludeModeExpiryTimer.setStatus("current")
_HwMgmdRouterCacheVersion1HostTimer_Type = TimeTicks
_HwMgmdRouterCacheVersion1HostTimer_Object = MibTableColumn
hwMgmdRouterCacheVersion1HostTimer = _HwMgmdRouterCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 8),
    _HwMgmdRouterCacheVersion1HostTimer_Type()
)
hwMgmdRouterCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheVersion1HostTimer.setStatus("current")
_HwMgmdRouterCacheVersion2HostTimer_Type = TimeTicks
_HwMgmdRouterCacheVersion2HostTimer_Object = MibTableColumn
hwMgmdRouterCacheVersion2HostTimer = _HwMgmdRouterCacheVersion2HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 9),
    _HwMgmdRouterCacheVersion2HostTimer_Type()
)
hwMgmdRouterCacheVersion2HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheVersion2HostTimer.setStatus("current")


class _HwMgmdRouterCacheSourceFilterMode_Type(Integer32):
    """Custom type hwMgmdRouterCacheSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_HwMgmdRouterCacheSourceFilterMode_Type.__name__ = "Integer32"
_HwMgmdRouterCacheSourceFilterMode_Object = MibTableColumn
hwMgmdRouterCacheSourceFilterMode = _HwMgmdRouterCacheSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 6, 1, 10),
    _HwMgmdRouterCacheSourceFilterMode_Type()
)
hwMgmdRouterCacheSourceFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterCacheSourceFilterMode.setStatus("current")
_HwMgmdInverseRouterCacheTable_Object = MibTable
hwMgmdInverseRouterCacheTable = _HwMgmdInverseRouterCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 8)
)
if mibBuilder.loadTexts:
    hwMgmdInverseRouterCacheTable.setStatus("current")
_HwMgmdInverseRouterCacheEntry_Object = MibTableRow
hwMgmdInverseRouterCacheEntry = _HwMgmdInverseRouterCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 8, 1)
)
hwMgmdInverseRouterCacheEntry.setIndexNames(
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdInverseRouterCacheIfIndex"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdInverseRouterCacheAddressType"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdInverseRouterCacheAddress"),
)
if mibBuilder.loadTexts:
    hwMgmdInverseRouterCacheEntry.setStatus("current")
_HwMgmdInverseRouterCacheIfIndex_Type = InterfaceIndex
_HwMgmdInverseRouterCacheIfIndex_Object = MibTableColumn
hwMgmdInverseRouterCacheIfIndex = _HwMgmdInverseRouterCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 8, 1, 1),
    _HwMgmdInverseRouterCacheIfIndex_Type()
)
hwMgmdInverseRouterCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdInverseRouterCacheIfIndex.setStatus("current")
_HwMgmdInverseRouterCacheAddressType_Type = InetAddressType
_HwMgmdInverseRouterCacheAddressType_Object = MibTableColumn
hwMgmdInverseRouterCacheAddressType = _HwMgmdInverseRouterCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 8, 1, 2),
    _HwMgmdInverseRouterCacheAddressType_Type()
)
hwMgmdInverseRouterCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdInverseRouterCacheAddressType.setStatus("current")


class _HwMgmdInverseRouterCacheAddress_Type(InetAddress):
    """Custom type hwMgmdInverseRouterCacheAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HwMgmdInverseRouterCacheAddress_Type.__name__ = "InetAddress"
_HwMgmdInverseRouterCacheAddress_Object = MibTableColumn
hwMgmdInverseRouterCacheAddress = _HwMgmdInverseRouterCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 8, 1, 3),
    _HwMgmdInverseRouterCacheAddress_Type()
)
hwMgmdInverseRouterCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdInverseRouterCacheAddress.setStatus("current")
_HwMgmdRouterSrcListTable_Object = MibTable
hwMgmdRouterSrcListTable = _HwMgmdRouterSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hwMgmdRouterSrcListTable.setStatus("current")
_HwMgmdRouterSrcListEntry_Object = MibTableRow
hwMgmdRouterSrcListEntry = _HwMgmdRouterSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 10, 1)
)
hwMgmdRouterSrcListEntry.setIndexNames(
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterSrcListAddressType"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterSrcListAddress"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterSrcListIfIndex"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdRouterSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    hwMgmdRouterSrcListEntry.setStatus("current")
_HwMgmdRouterSrcListAddressType_Type = InetAddressType
_HwMgmdRouterSrcListAddressType_Object = MibTableColumn
hwMgmdRouterSrcListAddressType = _HwMgmdRouterSrcListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 10, 1, 1),
    _HwMgmdRouterSrcListAddressType_Type()
)
hwMgmdRouterSrcListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterSrcListAddressType.setStatus("current")


class _HwMgmdRouterSrcListAddress_Type(InetAddress):
    """Custom type hwMgmdRouterSrcListAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HwMgmdRouterSrcListAddress_Type.__name__ = "InetAddress"
_HwMgmdRouterSrcListAddress_Object = MibTableColumn
hwMgmdRouterSrcListAddress = _HwMgmdRouterSrcListAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 10, 1, 2),
    _HwMgmdRouterSrcListAddress_Type()
)
hwMgmdRouterSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterSrcListAddress.setStatus("current")
_HwMgmdRouterSrcListIfIndex_Type = InterfaceIndex
_HwMgmdRouterSrcListIfIndex_Object = MibTableColumn
hwMgmdRouterSrcListIfIndex = _HwMgmdRouterSrcListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 10, 1, 3),
    _HwMgmdRouterSrcListIfIndex_Type()
)
hwMgmdRouterSrcListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdRouterSrcListIfIndex.setStatus("current")


class _HwMgmdRouterSrcListHostAddress_Type(InetAddress):
    """Custom type hwMgmdRouterSrcListHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HwMgmdRouterSrcListHostAddress_Type.__name__ = "InetAddress"
_HwMgmdRouterSrcListHostAddress_Object = MibTableColumn
hwMgmdRouterSrcListHostAddress = _HwMgmdRouterSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 10, 1, 4),
    _HwMgmdRouterSrcListHostAddress_Type()
)
hwMgmdRouterSrcListHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterSrcListHostAddress.setStatus("current")
_HwMgmdRouterSrcListExpire_Type = TimeTicks
_HwMgmdRouterSrcListExpire_Object = MibTableColumn
hwMgmdRouterSrcListExpire = _HwMgmdRouterSrcListExpire_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 10, 1, 5),
    _HwMgmdRouterSrcListExpire_Type()
)
hwMgmdRouterSrcListExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdRouterSrcListExpire.setStatus("current")
_HwMgmdCtlMsgCountTable_Object = MibTable
hwMgmdCtlMsgCountTable = _HwMgmdCtlMsgCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11)
)
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountTable.setStatus("current")
_HwMgmdCtlMsgCountEntry_Object = MibTableRow
hwMgmdCtlMsgCountEntry = _HwMgmdCtlMsgCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1)
)
hwMgmdCtlMsgCountEntry.setIndexNames(
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdCtlMsgCountIfIndex"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdCtlMsgCountQuerierType"),
    (0, "HUAWEI-MGMD-STD-MIB", "hwMgmdCtlMsgCountState"),
)
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountEntry.setStatus("current")
_HwMgmdCtlMsgCountIfIndex_Type = InterfaceIndex
_HwMgmdCtlMsgCountIfIndex_Object = MibTableColumn
hwMgmdCtlMsgCountIfIndex = _HwMgmdCtlMsgCountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 1),
    _HwMgmdCtlMsgCountIfIndex_Type()
)
hwMgmdCtlMsgCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountIfIndex.setStatus("current")
_HwMgmdCtlMsgCountQuerierType_Type = InetAddressType
_HwMgmdCtlMsgCountQuerierType_Object = MibTableColumn
hwMgmdCtlMsgCountQuerierType = _HwMgmdCtlMsgCountQuerierType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 2),
    _HwMgmdCtlMsgCountQuerierType_Type()
)
hwMgmdCtlMsgCountQuerierType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountQuerierType.setStatus("current")
_HwMgmdCtlMsgCountState_Type = HWMgmdCtlMsgState
_HwMgmdCtlMsgCountState_Object = MibTableColumn
hwMgmdCtlMsgCountState = _HwMgmdCtlMsgCountState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 3),
    _HwMgmdCtlMsgCountState_Type()
)
hwMgmdCtlMsgCountState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountState.setStatus("current")
_HwMgmdCtlMsgCountQuery_Type = Unsigned32
_HwMgmdCtlMsgCountQuery_Object = MibTableColumn
hwMgmdCtlMsgCountQuery = _HwMgmdCtlMsgCountQuery_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 4),
    _HwMgmdCtlMsgCountQuery_Type()
)
hwMgmdCtlMsgCountQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountQuery.setStatus("current")
_HwMgmdCtlMsgCountReportASM_Type = Unsigned32
_HwMgmdCtlMsgCountReportASM_Object = MibTableColumn
hwMgmdCtlMsgCountReportASM = _HwMgmdCtlMsgCountReportASM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 5),
    _HwMgmdCtlMsgCountReportASM_Type()
)
hwMgmdCtlMsgCountReportASM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountReportASM.setStatus("current")
_HwMgmdCtlMsgCountReportSSM_Type = Unsigned32
_HwMgmdCtlMsgCountReportSSM_Object = MibTableColumn
hwMgmdCtlMsgCountReportSSM = _HwMgmdCtlMsgCountReportSSM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 6),
    _HwMgmdCtlMsgCountReportSSM_Type()
)
hwMgmdCtlMsgCountReportSSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountReportSSM.setStatus("current")
_HwMgmdCtlMsgCountLeaveASM_Type = Unsigned32
_HwMgmdCtlMsgCountLeaveASM_Object = MibTableColumn
hwMgmdCtlMsgCountLeaveASM = _HwMgmdCtlMsgCountLeaveASM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 7),
    _HwMgmdCtlMsgCountLeaveASM_Type()
)
hwMgmdCtlMsgCountLeaveASM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountLeaveASM.setStatus("current")
_HwMgmdCtlMsgCountLeaveSSM_Type = Unsigned32
_HwMgmdCtlMsgCountLeaveSSM_Object = MibTableColumn
hwMgmdCtlMsgCountLeaveSSM = _HwMgmdCtlMsgCountLeaveSSM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 8),
    _HwMgmdCtlMsgCountLeaveSSM_Type()
)
hwMgmdCtlMsgCountLeaveSSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountLeaveSSM.setStatus("current")
_HwMgmdCtlMsgCountISIN_Type = Unsigned32
_HwMgmdCtlMsgCountISIN_Object = MibTableColumn
hwMgmdCtlMsgCountISIN = _HwMgmdCtlMsgCountISIN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 9),
    _HwMgmdCtlMsgCountISIN_Type()
)
hwMgmdCtlMsgCountISIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountISIN.setStatus("current")
_HwMgmdCtlMsgCountISEX_Type = Unsigned32
_HwMgmdCtlMsgCountISEX_Object = MibTableColumn
hwMgmdCtlMsgCountISEX = _HwMgmdCtlMsgCountISEX_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 10),
    _HwMgmdCtlMsgCountISEX_Type()
)
hwMgmdCtlMsgCountISEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountISEX.setStatus("current")
_HwMgmdCtlMsgCountTOIN_Type = Unsigned32
_HwMgmdCtlMsgCountTOIN_Object = MibTableColumn
hwMgmdCtlMsgCountTOIN = _HwMgmdCtlMsgCountTOIN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 11),
    _HwMgmdCtlMsgCountTOIN_Type()
)
hwMgmdCtlMsgCountTOIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountTOIN.setStatus("current")
_HwMgmdCtlMsgCountTOEX_Type = Unsigned32
_HwMgmdCtlMsgCountTOEX_Object = MibTableColumn
hwMgmdCtlMsgCountTOEX = _HwMgmdCtlMsgCountTOEX_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 12),
    _HwMgmdCtlMsgCountTOEX_Type()
)
hwMgmdCtlMsgCountTOEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountTOEX.setStatus("current")
_HwMgmdCtlMsgCountALLOW_Type = Unsigned32
_HwMgmdCtlMsgCountALLOW_Object = MibTableColumn
hwMgmdCtlMsgCountALLOW = _HwMgmdCtlMsgCountALLOW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 13),
    _HwMgmdCtlMsgCountALLOW_Type()
)
hwMgmdCtlMsgCountALLOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountALLOW.setStatus("current")
_HwMgmdCtlMsgCountBLOCK_Type = Unsigned32
_HwMgmdCtlMsgCountBLOCK_Object = MibTableColumn
hwMgmdCtlMsgCountBLOCK = _HwMgmdCtlMsgCountBLOCK_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 14),
    _HwMgmdCtlMsgCountBLOCK_Type()
)
hwMgmdCtlMsgCountBLOCK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountBLOCK.setStatus("current")
_HwMgmdCtlMsgCountSrcRecTotal_Type = Unsigned32
_HwMgmdCtlMsgCountSrcRecTotal_Object = MibTableColumn
hwMgmdCtlMsgCountSrcRecTotal = _HwMgmdCtlMsgCountSrcRecTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 15),
    _HwMgmdCtlMsgCountSrcRecTotal_Type()
)
hwMgmdCtlMsgCountSrcRecTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountSrcRecTotal.setStatus("current")
_HwMgmdCtlMsgCountOthers_Type = Unsigned32
_HwMgmdCtlMsgCountOthers_Object = MibTableColumn
hwMgmdCtlMsgCountOthers = _HwMgmdCtlMsgCountOthers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 1, 11, 1, 16),
    _HwMgmdCtlMsgCountOthers_Type()
)
hwMgmdCtlMsgCountOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdCtlMsgCountOthers.setStatus("current")
_HwMgmdMibGeneralObjects_ObjectIdentity = ObjectIdentity
hwMgmdMibGeneralObjects = _HwMgmdMibGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2)
)
_HwMgmdGroup_Type = IpAddress
_HwMgmdGroup_Object = MibScalar
hwMgmdGroup = _HwMgmdGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 1),
    _HwMgmdGroup_Type()
)
hwMgmdGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdGroup.setStatus("obsolete")
_HwMgmdSource_Type = IpAddress
_HwMgmdSource_Object = MibScalar
hwMgmdSource = _HwMgmdSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 2),
    _HwMgmdSource_Type()
)
hwMgmdSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdSource.setStatus("obsolete")
_HwMgmdLimitInterfaceIfIndex_Type = InterfaceIndexOrZero
_HwMgmdLimitInterfaceIfIndex_Object = MibScalar
hwMgmdLimitInterfaceIfIndex = _HwMgmdLimitInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 3),
    _HwMgmdLimitInterfaceIfIndex_Type()
)
hwMgmdLimitInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdLimitInterfaceIfIndex.setStatus("current")


class _HwMgmdGlobalEntries_Type(Unsigned32):
    """Custom type hwMgmdGlobalEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdGlobalEntries_Type.__name__ = "Unsigned32"
_HwMgmdGlobalEntries_Object = MibScalar
hwMgmdGlobalEntries = _HwMgmdGlobalEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 4),
    _HwMgmdGlobalEntries_Type()
)
hwMgmdGlobalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdGlobalEntries.setStatus("current")


class _HwMgmdInterfaceEntries_Type(Unsigned32):
    """Custom type hwMgmdInterfaceEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdInterfaceEntries_Type.__name__ = "Unsigned32"
_HwMgmdInterfaceEntries_Object = MibScalar
hwMgmdInterfaceEntries = _HwMgmdInterfaceEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 5),
    _HwMgmdInterfaceEntries_Type()
)
hwMgmdInterfaceEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdInterfaceEntries.setStatus("current")


class _HwMgmdTotalEntries_Type(Unsigned32):
    """Custom type hwMgmdTotalEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdTotalEntries_Type.__name__ = "Unsigned32"
_HwMgmdTotalEntries_Object = MibScalar
hwMgmdTotalEntries = _HwMgmdTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 6),
    _HwMgmdTotalEntries_Type()
)
hwMgmdTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdTotalEntries.setStatus("current")


class _HwMgmdGmpJoinGrpAddr_Type(DisplayString):
    """Custom type hwMgmdGmpJoinGrpAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwMgmdGmpJoinGrpAddr_Type.__name__ = "DisplayString"
_HwMgmdGmpJoinGrpAddr_Object = MibScalar
hwMgmdGmpJoinGrpAddr = _HwMgmdGmpJoinGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 7),
    _HwMgmdGmpJoinGrpAddr_Type()
)
hwMgmdGmpJoinGrpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpJoinGrpAddr.setStatus("current")


class _HwMgmdGmpJoinSrcAddr_Type(DisplayString):
    """Custom type hwMgmdGmpJoinSrcAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwMgmdGmpJoinSrcAddr_Type.__name__ = "DisplayString"
_HwMgmdGmpJoinSrcAddr_Object = MibScalar
hwMgmdGmpJoinSrcAddr = _HwMgmdGmpJoinSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 8),
    _HwMgmdGmpJoinSrcAddr_Type()
)
hwMgmdGmpJoinSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpJoinSrcAddr.setStatus("current")


class _HwMgmdGmpJoinSenderIp_Type(DisplayString):
    """Custom type hwMgmdGmpJoinSenderIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwMgmdGmpJoinSenderIp_Type.__name__ = "DisplayString"
_HwMgmdGmpJoinSenderIp_Object = MibScalar
hwMgmdGmpJoinSenderIp = _HwMgmdGmpJoinSenderIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 9),
    _HwMgmdGmpJoinSenderIp_Type()
)
hwMgmdGmpJoinSenderIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpJoinSenderIp.setStatus("current")


class _HwMgmdGmpJoinVersion_Type(Unsigned32):
    """Custom type hwMgmdGmpJoinVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HwMgmdGmpJoinVersion_Type.__name__ = "Unsigned32"
_HwMgmdGmpJoinVersion_Object = MibScalar
hwMgmdGmpJoinVersion = _HwMgmdGmpJoinVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 10),
    _HwMgmdGmpJoinVersion_Type()
)
hwMgmdGmpJoinVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpJoinVersion.setStatus("current")
_HwMgmdGmpInterfaceIfIndex_Type = InterfaceIndex
_HwMgmdGmpInterfaceIfIndex_Object = MibScalar
hwMgmdGmpInterfaceIfIndex = _HwMgmdGmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 11),
    _HwMgmdGmpInterfaceIfIndex_Type()
)
hwMgmdGmpInterfaceIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpInterfaceIfIndex.setStatus("current")


class _HwMgmdGmpInterfaceName_Type(DisplayString):
    """Custom type hwMgmdGmpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwMgmdGmpInterfaceName_Type.__name__ = "DisplayString"
_HwMgmdGmpInterfaceName_Object = MibScalar
hwMgmdGmpInterfaceName = _HwMgmdGmpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 12),
    _HwMgmdGmpInterfaceName_Type()
)
hwMgmdGmpInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpInterfaceName.setStatus("current")
_HwMgmdGmpLimitGroupAddressType_Type = InetAddressType
_HwMgmdGmpLimitGroupAddressType_Object = MibScalar
hwMgmdGmpLimitGroupAddressType = _HwMgmdGmpLimitGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 13),
    _HwMgmdGmpLimitGroupAddressType_Type()
)
hwMgmdGmpLimitGroupAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpLimitGroupAddressType.setStatus("current")


class _HwMgmdGmpLimitGroup_Type(InetAddress):
    """Custom type hwMgmdGmpLimitGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwMgmdGmpLimitGroup_Type.__name__ = "InetAddress"
_HwMgmdGmpLimitGroup_Object = MibScalar
hwMgmdGmpLimitGroup = _HwMgmdGmpLimitGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 14),
    _HwMgmdGmpLimitGroup_Type()
)
hwMgmdGmpLimitGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpLimitGroup.setStatus("current")


class _HwMgmdGmpLimitSource_Type(InetAddress):
    """Custom type hwMgmdGmpLimitSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwMgmdGmpLimitSource_Type.__name__ = "InetAddress"
_HwMgmdGmpLimitSource_Object = MibScalar
hwMgmdGmpLimitSource = _HwMgmdGmpLimitSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 15),
    _HwMgmdGmpLimitSource_Type()
)
hwMgmdGmpLimitSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdGmpLimitSource.setStatus("current")
_HwMgmdInstanceName_Type = DisplayString
_HwMgmdInstanceName_Object = MibScalar
hwMgmdInstanceName = _HwMgmdInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 16),
    _HwMgmdInstanceName_Type()
)
hwMgmdInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdInstanceName.setStatus("current")
_HwMgmdNotificationAddressType_Type = InetAddressType
_HwMgmdNotificationAddressType_Object = MibScalar
hwMgmdNotificationAddressType = _HwMgmdNotificationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 17),
    _HwMgmdNotificationAddressType_Type()
)
hwMgmdNotificationAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdNotificationAddressType.setStatus("current")


class _HwMgmdTotalLimitCurrentCount_Type(Unsigned32):
    """Custom type hwMgmdTotalLimitCurrentCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdTotalLimitCurrentCount_Type.__name__ = "Unsigned32"
_HwMgmdTotalLimitCurrentCount_Object = MibScalar
hwMgmdTotalLimitCurrentCount = _HwMgmdTotalLimitCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 18),
    _HwMgmdTotalLimitCurrentCount_Type()
)
hwMgmdTotalLimitCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMgmdTotalLimitCurrentCount.setStatus("current")


class _HwMgmdTotalLimitThreshold_Type(Unsigned32):
    """Custom type hwMgmdTotalLimitThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwMgmdTotalLimitThreshold_Type.__name__ = "Unsigned32"
_HwMgmdTotalLimitThreshold_Object = MibScalar
hwMgmdTotalLimitThreshold = _HwMgmdTotalLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 19),
    _HwMgmdTotalLimitThreshold_Type()
)
hwMgmdTotalLimitThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdTotalLimitThreshold.setStatus("current")


class _HwMgmdHostStarGCurrentCount_Type(Unsigned32):
    """Custom type hwMgmdHostStarGCurrentCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdHostStarGCurrentCount_Type.__name__ = "Unsigned32"
_HwMgmdHostStarGCurrentCount_Object = MibScalar
hwMgmdHostStarGCurrentCount = _HwMgmdHostStarGCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 20),
    _HwMgmdHostStarGCurrentCount_Type()
)
hwMgmdHostStarGCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostStarGCurrentCount.setStatus("current")


class _HwMgmdHostStarGThreshold_Type(Unsigned32):
    """Custom type hwMgmdHostStarGThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwMgmdHostStarGThreshold_Type.__name__ = "Unsigned32"
_HwMgmdHostStarGThreshold_Object = MibScalar
hwMgmdHostStarGThreshold = _HwMgmdHostStarGThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 21),
    _HwMgmdHostStarGThreshold_Type()
)
hwMgmdHostStarGThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostStarGThreshold.setStatus("current")


class _HwMgmdHostStarGTotalCount_Type(Unsigned32):
    """Custom type hwMgmdHostStarGTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdHostStarGTotalCount_Type.__name__ = "Unsigned32"
_HwMgmdHostStarGTotalCount_Object = MibScalar
hwMgmdHostStarGTotalCount = _HwMgmdHostStarGTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 22),
    _HwMgmdHostStarGTotalCount_Type()
)
hwMgmdHostStarGTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostStarGTotalCount.setStatus("current")


class _HwMgmdHostNotificationSrcAddr_Type(InetAddress):
    """Custom type hwMgmdHostNotificationSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwMgmdHostNotificationSrcAddr_Type.__name__ = "InetAddress"
_HwMgmdHostNotificationSrcAddr_Object = MibScalar
hwMgmdHostNotificationSrcAddr = _HwMgmdHostNotificationSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 23),
    _HwMgmdHostNotificationSrcAddr_Type()
)
hwMgmdHostNotificationSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostNotificationSrcAddr.setStatus("current")


class _HwMgmdHostNotificationGrpAddr_Type(InetAddress):
    """Custom type hwMgmdHostNotificationGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwMgmdHostNotificationGrpAddr_Type.__name__ = "InetAddress"
_HwMgmdHostNotificationGrpAddr_Object = MibScalar
hwMgmdHostNotificationGrpAddr = _HwMgmdHostNotificationGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 24),
    _HwMgmdHostNotificationGrpAddr_Type()
)
hwMgmdHostNotificationGrpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostNotificationGrpAddr.setStatus("current")


class _HwMgmdHostSGCurrentCount_Type(Unsigned32):
    """Custom type hwMgmdHostSGCurrentCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdHostSGCurrentCount_Type.__name__ = "Unsigned32"
_HwMgmdHostSGCurrentCount_Object = MibScalar
hwMgmdHostSGCurrentCount = _HwMgmdHostSGCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 25),
    _HwMgmdHostSGCurrentCount_Type()
)
hwMgmdHostSGCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostSGCurrentCount.setStatus("current")


class _HwMgmdHostSGThreshold_Type(Unsigned32):
    """Custom type hwMgmdHostSGThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwMgmdHostSGThreshold_Type.__name__ = "Unsigned32"
_HwMgmdHostSGThreshold_Object = MibScalar
hwMgmdHostSGThreshold = _HwMgmdHostSGThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 26),
    _HwMgmdHostSGThreshold_Type()
)
hwMgmdHostSGThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostSGThreshold.setStatus("current")


class _HwMgmdHostSGTotalCount_Type(Unsigned32):
    """Custom type hwMgmdHostSGTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMgmdHostSGTotalCount_Type.__name__ = "Unsigned32"
_HwMgmdHostSGTotalCount_Object = MibScalar
hwMgmdHostSGTotalCount = _HwMgmdHostSGTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 2, 27),
    _HwMgmdHostSGTotalCount_Type()
)
hwMgmdHostSGTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMgmdHostSGTotalCount.setStatus("current")
_HwMgmdMibNotifications_ObjectIdentity = ObjectIdentity
hwMgmdMibNotifications = _HwMgmdMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3)
)
_HwMgmdMibConformance_ObjectIdentity = ObjectIdentity
hwMgmdMibConformance = _HwMgmdMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4)
)
_HwMgmdMibCompliance_ObjectIdentity = ObjectIdentity
hwMgmdMibCompliance = _HwMgmdMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 3)
)
_HwMgmdMibGroups_ObjectIdentity = ObjectIdentity
hwMgmdMibGroups = _HwMgmdMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4)
)

# Managed Objects groups

hwMgmdRouterBaseMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 2)
)
hwMgmdRouterBaseMibGroup.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceStatus"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheUpTime"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheExpiryTime"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceJoins"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceGroups"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheLastReporter"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceQuerierUpTime"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceQuerierExpiryTime"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceQueryInterval"))
)
if mibBuilder.loadTexts:
    hwMgmdRouterBaseMibGroup.setStatus("current")

hwMgmdV2RouterBaseMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 6)
)
hwMgmdV2RouterBaseMibGroup.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceVersion"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceQuerier"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceQueryMaxResponseTime"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceRobustness"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceWrongVersionQueries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceLastMembQueryIntvl"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceLastMembQueryCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceStartupQueryCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceStartupQueryInterval"))
)
if mibBuilder.loadTexts:
    hwMgmdV2RouterBaseMibGroup.setStatus("current")

hwMgmdV2IgmpRouterMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 7)
)
hwMgmdV2IgmpRouterMibGroup.setObjects(
    ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheVersion1HostTimer")
)
if mibBuilder.loadTexts:
    hwMgmdV2IgmpRouterMibGroup.setStatus("current")

hwMgmdV2ProxyMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 8)
)
hwMgmdV2ProxyMibGroup.setObjects(
    ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterInterfaceProxyIfIndex")
)
if mibBuilder.loadTexts:
    hwMgmdV2ProxyMibGroup.setStatus("current")

hwMgmdV2RouterOptMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 9)
)
hwMgmdV2RouterOptMibGroup.setObjects(
    ("HUAWEI-MGMD-STD-MIB", "hwMgmdInverseRouterCacheAddress")
)
if mibBuilder.loadTexts:
    hwMgmdV2RouterOptMibGroup.setStatus("current")

hwMgmdV3RouterMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 11)
)
hwMgmdV3RouterMibGroup.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheSourceFilterMode"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheVersion2HostTimer"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterCacheExcludeModeExpiryTimer"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterSrcListHostAddress"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdRouterSrcListExpire"))
)
if mibBuilder.loadTexts:
    hwMgmdV3RouterMibGroup.setStatus("current")

hwMgmdMibNotificationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 12)
)
hwMgmdMibNotificationObjects.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdLimitInterfaceIfIndex"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGlobalEntries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInterfaceEntries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalEntries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinGrpAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinSrcAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinSenderIp"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinVersion"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceIfIndex"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceName"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroupAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGTotalCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostNotificationSrcAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostNotificationGrpAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwMgmdMibNotificationObjects.setStatus("current")


# Notification objects

hwMgmdGlobalLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 1)
)
hwMgmdGlobalLimit.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGlobalEntries"))
)
if mibBuilder.loadTexts:
    hwMgmdGlobalLimit.setStatus(
        "obsolete"
    )

hwMgmdInterfaceLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 2)
)
hwMgmdInterfaceLimit.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdLimitInterfaceIfIndex"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInterfaceEntries"))
)
if mibBuilder.loadTexts:
    hwMgmdInterfaceLimit.setStatus(
        "obsolete"
    )

hwMgmdTotalLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 3)
)
hwMgmdTotalLimit.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalEntries"))
)
if mibBuilder.loadTexts:
    hwMgmdTotalLimit.setStatus(
        "obsolete"
    )

hwMgmdGmpJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 4)
)
hwMgmdGmpJoin.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceName"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceIfIndex"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinVersion"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinSrcAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinGrpAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinSenderIp"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdGmpJoin.setStatus(
        "current"
    )

hwMgmdGmpLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 5)
)
hwMgmdGmpLeave.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceName"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceIfIndex"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinSrcAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoinGrpAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdGmpLeave.setStatus(
        "current"
    )

hwMgmdGMPGlobalLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 6)
)
hwMgmdGMPGlobalLimit.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroupAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGlobalEntries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdGMPGlobalLimit.setStatus(
        "current"
    )

hwMgmdGMPInterfaceLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 7)
)
hwMgmdGMPInterfaceLimit.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroupAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdLimitInterfaceIfIndex"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInterfaceEntries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceName"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdGMPInterfaceLimit.setStatus(
        "current"
    )

hwMgmdGMPTotalLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 8)
)
hwMgmdGMPTotalLimit.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroupAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalEntries"))
)
if mibBuilder.loadTexts:
    hwMgmdGMPTotalLimit.setStatus(
        "current"
    )

hwMgmdGMPInterfaceLimitClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 9)
)
hwMgmdGMPInterfaceLimitClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroupAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdLimitInterfaceIfIndex"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInterfaceEntries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpInterfaceName"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdGMPInterfaceLimitClear.setStatus(
        "current"
    )

hwMgmdGMPGlobalLimitClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 10)
)
hwMgmdGMPGlobalLimitClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroupAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGlobalEntries"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdGMPGlobalLimitClear.setStatus(
        "current"
    )

hwMgmdGMPTotalLimitClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 11)
)
hwMgmdGMPTotalLimitClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroupAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitSource"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLimitGroup"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalEntries"))
)
if mibBuilder.loadTexts:
    hwMgmdGMPTotalLimitClear.setStatus(
        "current"
    )

hwMgmdTotalLimitThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 12)
)
hwMgmdTotalLimitThresholdExceed.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalEntries"))
)
if mibBuilder.loadTexts:
    hwMgmdTotalLimitThresholdExceed.setStatus(
        "current"
    )

hwMgmdTotalLimitThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 13)
)
hwMgmdTotalLimitThresholdExceedClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalEntries"))
)
if mibBuilder.loadTexts:
    hwMgmdTotalLimitThresholdExceedClear.setStatus(
        "current"
    )

hwMgmdHostStarGThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 14)
)
hwMgmdHostStarGThresholdExceed.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGTotalCount"))
)
if mibBuilder.loadTexts:
    hwMgmdHostStarGThresholdExceed.setStatus(
        "current"
    )

hwMgmdHostStarGThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 15)
)
hwMgmdHostStarGThresholdExceedClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGTotalCount"))
)
if mibBuilder.loadTexts:
    hwMgmdHostStarGThresholdExceedClear.setStatus(
        "current"
    )

hwMgmdHostStarGExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 16)
)
hwMgmdHostStarGExceed.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostNotificationSrcAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostNotificationGrpAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGTotalCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdHostStarGExceed.setStatus(
        "current"
    )

hwMgmdHostStarGExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 17)
)
hwMgmdHostStarGExceedClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGTotalCount"))
)
if mibBuilder.loadTexts:
    hwMgmdHostStarGExceedClear.setStatus(
        "current"
    )

hwMgmdHostSGThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 18)
)
hwMgmdHostSGThresholdExceed.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwMgmdHostSGThresholdExceed.setStatus(
        "current"
    )

hwMgmdHostSGThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 19)
)
hwMgmdHostSGThresholdExceedClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGCurrentCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGThreshold"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwMgmdHostSGThresholdExceedClear.setStatus(
        "current"
    )

hwMgmdHostSGExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 20)
)
hwMgmdHostSGExceed.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostNotificationSrcAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostNotificationGrpAddr"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGTotalCount"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInstanceName"))
)
if mibBuilder.loadTexts:
    hwMgmdHostSGExceed.setStatus(
        "current"
    )

hwMgmdHostSGExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 3, 21)
)
hwMgmdHostSGExceedClear.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdNotificationAddressType"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwMgmdHostSGExceedClear.setStatus(
        "current"
    )


# Notifications groups

hwMgmdMibNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 4, 13)
)
hwMgmdMibNotificationGroup.setObjects(
      *(("HUAWEI-MGMD-STD-MIB", "hwMgmdGlobalLimit"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdInterfaceLimit"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimit"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpJoin"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGmpLeave"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGMPGlobalLimit"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGMPInterfaceLimit"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGMPTotalLimit"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGMPInterfaceLimitClear"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGMPGlobalLimitClear"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdGMPTotalLimitClear"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitThresholdExceed"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdTotalLimitThresholdExceedClear"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGThresholdExceed"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGThresholdExceedClear"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGExceed"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostStarGExceedClear"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGThresholdExceed"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGThresholdExceedClear"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGExceed"),
        ("HUAWEI-MGMD-STD-MIB", "hwMgmdHostSGExceedClear"))
)
if mibBuilder.loadTexts:
    hwMgmdMibNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMgmdIgmpV1RouterMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    hwMgmdIgmpV1RouterMibCompliance.setStatus(
        "current"
    )

hwMgmdIgmpV2RouterMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hwMgmdIgmpV2RouterMibCompliance.setStatus(
        "current"
    )

hwMgmdMldV1RouterMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 3, 6)
)
if mibBuilder.loadTexts:
    hwMgmdMldV1RouterMibCompliance.setStatus(
        "current"
    )

hwMgmdIgmpV3RouterMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 3, 8)
)
if mibBuilder.loadTexts:
    hwMgmdIgmpV3RouterMibCompliance.setStatus(
        "current"
    )

hwMgmdMldV2RouterMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 3, 4, 3, 10)
)
if mibBuilder.loadTexts:
    hwMgmdMldV2RouterMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MGMD-STD-MIB",
    **{"HWMgmdCtlMsgState": HWMgmdCtlMsgState,
       "hwMcast": hwMcast,
       "hwMgmdStdMib": hwMgmdStdMib,
       "hwMgmdMibObjects": hwMgmdMibObjects,
       "hwMgmdRouterInterfaceTable": hwMgmdRouterInterfaceTable,
       "hwMgmdRouterInterfaceEntry": hwMgmdRouterInterfaceEntry,
       "hwMgmdRouterInterfaceIfIndex": hwMgmdRouterInterfaceIfIndex,
       "hwMgmdRouterInterfaceQuerierType": hwMgmdRouterInterfaceQuerierType,
       "hwMgmdRouterInterfaceQuerier": hwMgmdRouterInterfaceQuerier,
       "hwMgmdRouterInterfaceQueryInterval": hwMgmdRouterInterfaceQueryInterval,
       "hwMgmdRouterInterfaceStatus": hwMgmdRouterInterfaceStatus,
       "hwMgmdRouterInterfaceVersion": hwMgmdRouterInterfaceVersion,
       "hwMgmdRouterInterfaceQueryMaxResponseTime": hwMgmdRouterInterfaceQueryMaxResponseTime,
       "hwMgmdRouterInterfaceQuerierUpTime": hwMgmdRouterInterfaceQuerierUpTime,
       "hwMgmdRouterInterfaceQuerierExpiryTime": hwMgmdRouterInterfaceQuerierExpiryTime,
       "hwMgmdRouterInterfaceWrongVersionQueries": hwMgmdRouterInterfaceWrongVersionQueries,
       "hwMgmdRouterInterfaceJoins": hwMgmdRouterInterfaceJoins,
       "hwMgmdRouterInterfaceProxyIfIndex": hwMgmdRouterInterfaceProxyIfIndex,
       "hwMgmdRouterInterfaceGroups": hwMgmdRouterInterfaceGroups,
       "hwMgmdRouterInterfaceRobustness": hwMgmdRouterInterfaceRobustness,
       "hwMgmdRouterInterfaceLastMembQueryIntvl": hwMgmdRouterInterfaceLastMembQueryIntvl,
       "hwMgmdRouterInterfaceLastMembQueryCount": hwMgmdRouterInterfaceLastMembQueryCount,
       "hwMgmdRouterInterfaceStartupQueryCount": hwMgmdRouterInterfaceStartupQueryCount,
       "hwMgmdRouterInterfaceStartupQueryInterval": hwMgmdRouterInterfaceStartupQueryInterval,
       "hwMgmdRouterCacheTable": hwMgmdRouterCacheTable,
       "hwMgmdRouterCacheEntry": hwMgmdRouterCacheEntry,
       "hwMgmdRouterCacheAddressType": hwMgmdRouterCacheAddressType,
       "hwMgmdRouterCacheAddress": hwMgmdRouterCacheAddress,
       "hwMgmdRouterCacheIfIndex": hwMgmdRouterCacheIfIndex,
       "hwMgmdRouterCacheLastReporter": hwMgmdRouterCacheLastReporter,
       "hwMgmdRouterCacheUpTime": hwMgmdRouterCacheUpTime,
       "hwMgmdRouterCacheExpiryTime": hwMgmdRouterCacheExpiryTime,
       "hwMgmdRouterCacheExcludeModeExpiryTimer": hwMgmdRouterCacheExcludeModeExpiryTimer,
       "hwMgmdRouterCacheVersion1HostTimer": hwMgmdRouterCacheVersion1HostTimer,
       "hwMgmdRouterCacheVersion2HostTimer": hwMgmdRouterCacheVersion2HostTimer,
       "hwMgmdRouterCacheSourceFilterMode": hwMgmdRouterCacheSourceFilterMode,
       "hwMgmdInverseRouterCacheTable": hwMgmdInverseRouterCacheTable,
       "hwMgmdInverseRouterCacheEntry": hwMgmdInverseRouterCacheEntry,
       "hwMgmdInverseRouterCacheIfIndex": hwMgmdInverseRouterCacheIfIndex,
       "hwMgmdInverseRouterCacheAddressType": hwMgmdInverseRouterCacheAddressType,
       "hwMgmdInverseRouterCacheAddress": hwMgmdInverseRouterCacheAddress,
       "hwMgmdRouterSrcListTable": hwMgmdRouterSrcListTable,
       "hwMgmdRouterSrcListEntry": hwMgmdRouterSrcListEntry,
       "hwMgmdRouterSrcListAddressType": hwMgmdRouterSrcListAddressType,
       "hwMgmdRouterSrcListAddress": hwMgmdRouterSrcListAddress,
       "hwMgmdRouterSrcListIfIndex": hwMgmdRouterSrcListIfIndex,
       "hwMgmdRouterSrcListHostAddress": hwMgmdRouterSrcListHostAddress,
       "hwMgmdRouterSrcListExpire": hwMgmdRouterSrcListExpire,
       "hwMgmdCtlMsgCountTable": hwMgmdCtlMsgCountTable,
       "hwMgmdCtlMsgCountEntry": hwMgmdCtlMsgCountEntry,
       "hwMgmdCtlMsgCountIfIndex": hwMgmdCtlMsgCountIfIndex,
       "hwMgmdCtlMsgCountQuerierType": hwMgmdCtlMsgCountQuerierType,
       "hwMgmdCtlMsgCountState": hwMgmdCtlMsgCountState,
       "hwMgmdCtlMsgCountQuery": hwMgmdCtlMsgCountQuery,
       "hwMgmdCtlMsgCountReportASM": hwMgmdCtlMsgCountReportASM,
       "hwMgmdCtlMsgCountReportSSM": hwMgmdCtlMsgCountReportSSM,
       "hwMgmdCtlMsgCountLeaveASM": hwMgmdCtlMsgCountLeaveASM,
       "hwMgmdCtlMsgCountLeaveSSM": hwMgmdCtlMsgCountLeaveSSM,
       "hwMgmdCtlMsgCountISIN": hwMgmdCtlMsgCountISIN,
       "hwMgmdCtlMsgCountISEX": hwMgmdCtlMsgCountISEX,
       "hwMgmdCtlMsgCountTOIN": hwMgmdCtlMsgCountTOIN,
       "hwMgmdCtlMsgCountTOEX": hwMgmdCtlMsgCountTOEX,
       "hwMgmdCtlMsgCountALLOW": hwMgmdCtlMsgCountALLOW,
       "hwMgmdCtlMsgCountBLOCK": hwMgmdCtlMsgCountBLOCK,
       "hwMgmdCtlMsgCountSrcRecTotal": hwMgmdCtlMsgCountSrcRecTotal,
       "hwMgmdCtlMsgCountOthers": hwMgmdCtlMsgCountOthers,
       "hwMgmdMibGeneralObjects": hwMgmdMibGeneralObjects,
       "hwMgmdGroup": hwMgmdGroup,
       "hwMgmdSource": hwMgmdSource,
       "hwMgmdLimitInterfaceIfIndex": hwMgmdLimitInterfaceIfIndex,
       "hwMgmdGlobalEntries": hwMgmdGlobalEntries,
       "hwMgmdInterfaceEntries": hwMgmdInterfaceEntries,
       "hwMgmdTotalEntries": hwMgmdTotalEntries,
       "hwMgmdGmpJoinGrpAddr": hwMgmdGmpJoinGrpAddr,
       "hwMgmdGmpJoinSrcAddr": hwMgmdGmpJoinSrcAddr,
       "hwMgmdGmpJoinSenderIp": hwMgmdGmpJoinSenderIp,
       "hwMgmdGmpJoinVersion": hwMgmdGmpJoinVersion,
       "hwMgmdGmpInterfaceIfIndex": hwMgmdGmpInterfaceIfIndex,
       "hwMgmdGmpInterfaceName": hwMgmdGmpInterfaceName,
       "hwMgmdGmpLimitGroupAddressType": hwMgmdGmpLimitGroupAddressType,
       "hwMgmdGmpLimitGroup": hwMgmdGmpLimitGroup,
       "hwMgmdGmpLimitSource": hwMgmdGmpLimitSource,
       "hwMgmdInstanceName": hwMgmdInstanceName,
       "hwMgmdNotificationAddressType": hwMgmdNotificationAddressType,
       "hwMgmdTotalLimitCurrentCount": hwMgmdTotalLimitCurrentCount,
       "hwMgmdTotalLimitThreshold": hwMgmdTotalLimitThreshold,
       "hwMgmdHostStarGCurrentCount": hwMgmdHostStarGCurrentCount,
       "hwMgmdHostStarGThreshold": hwMgmdHostStarGThreshold,
       "hwMgmdHostStarGTotalCount": hwMgmdHostStarGTotalCount,
       "hwMgmdHostNotificationSrcAddr": hwMgmdHostNotificationSrcAddr,
       "hwMgmdHostNotificationGrpAddr": hwMgmdHostNotificationGrpAddr,
       "hwMgmdHostSGCurrentCount": hwMgmdHostSGCurrentCount,
       "hwMgmdHostSGThreshold": hwMgmdHostSGThreshold,
       "hwMgmdHostSGTotalCount": hwMgmdHostSGTotalCount,
       "hwMgmdMibNotifications": hwMgmdMibNotifications,
       "hwMgmdGlobalLimit": hwMgmdGlobalLimit,
       "hwMgmdInterfaceLimit": hwMgmdInterfaceLimit,
       "hwMgmdTotalLimit": hwMgmdTotalLimit,
       "hwMgmdGmpJoin": hwMgmdGmpJoin,
       "hwMgmdGmpLeave": hwMgmdGmpLeave,
       "hwMgmdGMPGlobalLimit": hwMgmdGMPGlobalLimit,
       "hwMgmdGMPInterfaceLimit": hwMgmdGMPInterfaceLimit,
       "hwMgmdGMPTotalLimit": hwMgmdGMPTotalLimit,
       "hwMgmdGMPInterfaceLimitClear": hwMgmdGMPInterfaceLimitClear,
       "hwMgmdGMPGlobalLimitClear": hwMgmdGMPGlobalLimitClear,
       "hwMgmdGMPTotalLimitClear": hwMgmdGMPTotalLimitClear,
       "hwMgmdTotalLimitThresholdExceed": hwMgmdTotalLimitThresholdExceed,
       "hwMgmdTotalLimitThresholdExceedClear": hwMgmdTotalLimitThresholdExceedClear,
       "hwMgmdHostStarGThresholdExceed": hwMgmdHostStarGThresholdExceed,
       "hwMgmdHostStarGThresholdExceedClear": hwMgmdHostStarGThresholdExceedClear,
       "hwMgmdHostStarGExceed": hwMgmdHostStarGExceed,
       "hwMgmdHostStarGExceedClear": hwMgmdHostStarGExceedClear,
       "hwMgmdHostSGThresholdExceed": hwMgmdHostSGThresholdExceed,
       "hwMgmdHostSGThresholdExceedClear": hwMgmdHostSGThresholdExceedClear,
       "hwMgmdHostSGExceed": hwMgmdHostSGExceed,
       "hwMgmdHostSGExceedClear": hwMgmdHostSGExceedClear,
       "hwMgmdMibConformance": hwMgmdMibConformance,
       "hwMgmdMibCompliance": hwMgmdMibCompliance,
       "hwMgmdIgmpV1RouterMibCompliance": hwMgmdIgmpV1RouterMibCompliance,
       "hwMgmdIgmpV2RouterMibCompliance": hwMgmdIgmpV2RouterMibCompliance,
       "hwMgmdMldV1RouterMibCompliance": hwMgmdMldV1RouterMibCompliance,
       "hwMgmdIgmpV3RouterMibCompliance": hwMgmdIgmpV3RouterMibCompliance,
       "hwMgmdMldV2RouterMibCompliance": hwMgmdMldV2RouterMibCompliance,
       "hwMgmdMibGroups": hwMgmdMibGroups,
       "hwMgmdRouterBaseMibGroup": hwMgmdRouterBaseMibGroup,
       "hwMgmdV2RouterBaseMibGroup": hwMgmdV2RouterBaseMibGroup,
       "hwMgmdV2IgmpRouterMibGroup": hwMgmdV2IgmpRouterMibGroup,
       "hwMgmdV2ProxyMibGroup": hwMgmdV2ProxyMibGroup,
       "hwMgmdV2RouterOptMibGroup": hwMgmdV2RouterOptMibGroup,
       "hwMgmdV3RouterMibGroup": hwMgmdV3RouterMibGroup,
       "hwMgmdMibNotificationObjects": hwMgmdMibNotificationObjects,
       "hwMgmdMibNotificationGroup": hwMgmdMibNotificationGroup}
)
