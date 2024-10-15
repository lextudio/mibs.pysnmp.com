# SNMP MIB module (BAY-STACK-IPV6-MLD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-IPV6-MLD-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:02 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(PortSet,) = mibBuilder.importSymbols(
    "RAPID-CITY",
    "PortSet")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackIpv6MldSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 44)
)
bayStackIpv6MldSnoopingMib.setRevisions(
        ("2015-05-29 00:00",
         "2015-01-22 00:00",
         "2014-10-23 00:00",
         "2014-08-11 00:00",
         "2014-01-16 00:00",
         "2013-01-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsIpv6MldSnoopingNotifications_ObjectIdentity = ObjectIdentity
bsIpv6MldSnoopingNotifications = _BsIpv6MldSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 0)
)
_BsIpv6MldSnoopingObjects_ObjectIdentity = ObjectIdentity
bsIpv6MldSnoopingObjects = _BsIpv6MldSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1)
)
_BsIpv6MldSnoopingInterfaceTable_Object = MibTable
bsIpv6MldSnoopingInterfaceTable = _BsIpv6MldSnoopingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1)
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceTable.setStatus("current")
_BsIpv6MldSnoopingInterfaceEntry_Object = MibTableRow
bsIpv6MldSnoopingInterfaceEntry = _BsIpv6MldSnoopingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1)
)
bsIpv6MldSnoopingInterfaceEntry.setIndexNames(
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceEntry.setStatus("current")
_BsIpv6MldSnoopingInterfaceIfIndex_Type = InterfaceIndex
_BsIpv6MldSnoopingInterfaceIfIndex_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceIfIndex = _BsIpv6MldSnoopingInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 1),
    _BsIpv6MldSnoopingInterfaceIfIndex_Type()
)
bsIpv6MldSnoopingInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceIfIndex.setStatus("current")


class _BsIpv6MldSnoopingInterfaceQueryInterval_Type(Unsigned32):
    """Custom type bsIpv6MldSnoopingInterfaceQueryInterval based on Unsigned32"""
    defaultValue = 125


_BsIpv6MldSnoopingInterfaceQueryInterval_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceQueryInterval = _BsIpv6MldSnoopingInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 2),
    _BsIpv6MldSnoopingInterfaceQueryInterval_Type()
)
bsIpv6MldSnoopingInterfaceQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceQueryInterval.setUnits("seconds")
_BsIpv6MldSnoopingInterfaceStatus_Type = RowStatus
_BsIpv6MldSnoopingInterfaceStatus_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceStatus = _BsIpv6MldSnoopingInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 3),
    _BsIpv6MldSnoopingInterfaceStatus_Type()
)
bsIpv6MldSnoopingInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceStatus.setStatus("current")


class _BsIpv6MldSnoopingInterfaceVersion_Type(Unsigned32):
    """Custom type bsIpv6MldSnoopingInterfaceVersion based on Unsigned32"""
    defaultValue = 1


_BsIpv6MldSnoopingInterfaceVersion_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceVersion = _BsIpv6MldSnoopingInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 4),
    _BsIpv6MldSnoopingInterfaceVersion_Type()
)
bsIpv6MldSnoopingInterfaceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceVersion.setStatus("current")


class _BsIpv6MldSnoopingInterfaceQuerier_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingInterfaceQuerier based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingInterfaceQuerier_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingInterfaceQuerier_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceQuerier = _BsIpv6MldSnoopingInterfaceQuerier_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 5),
    _BsIpv6MldSnoopingInterfaceQuerier_Type()
)
bsIpv6MldSnoopingInterfaceQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceQuerier.setStatus("current")


class _BsIpv6MldSnoopingInterfaceQueryMaxResponseDelay_Type(Unsigned32):
    """Custom type bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay based on Unsigned32"""
    defaultValue = 10


_BsIpv6MldSnoopingInterfaceQueryMaxResponseDelay_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay = _BsIpv6MldSnoopingInterfaceQueryMaxResponseDelay_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 6),
    _BsIpv6MldSnoopingInterfaceQueryMaxResponseDelay_Type()
)
bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay.setStatus("current")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay.setUnits("seconds")
_BsIpv6MldSnoopingInterfaceJoins_Type = Counter32
_BsIpv6MldSnoopingInterfaceJoins_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceJoins = _BsIpv6MldSnoopingInterfaceJoins_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 7),
    _BsIpv6MldSnoopingInterfaceJoins_Type()
)
bsIpv6MldSnoopingInterfaceJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceJoins.setStatus("current")
_BsIpv6MldSnoopingInterfaceGroups_Type = Gauge32
_BsIpv6MldSnoopingInterfaceGroups_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceGroups = _BsIpv6MldSnoopingInterfaceGroups_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 8),
    _BsIpv6MldSnoopingInterfaceGroups_Type()
)
bsIpv6MldSnoopingInterfaceGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceGroups.setStatus("current")


class _BsIpv6MldSnoopingInterfaceRobustness_Type(Unsigned32):
    """Custom type bsIpv6MldSnoopingInterfaceRobustness based on Unsigned32"""
    defaultValue = 2


_BsIpv6MldSnoopingInterfaceRobustness_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceRobustness = _BsIpv6MldSnoopingInterfaceRobustness_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 9),
    _BsIpv6MldSnoopingInterfaceRobustness_Type()
)
bsIpv6MldSnoopingInterfaceRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceRobustness.setStatus("current")


class _BsIpv6MldSnoopingInterfaceLastListenQueryIntvl_Type(Unsigned32):
    """Custom type bsIpv6MldSnoopingInterfaceLastListenQueryIntvl based on Unsigned32"""
    defaultValue = 1


_BsIpv6MldSnoopingInterfaceLastListenQueryIntvl_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceLastListenQueryIntvl = _BsIpv6MldSnoopingInterfaceLastListenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 10),
    _BsIpv6MldSnoopingInterfaceLastListenQueryIntvl_Type()
)
bsIpv6MldSnoopingInterfaceLastListenQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceLastListenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceLastListenQueryIntvl.setUnits("seconds")


class _BsIpv6MldSnoopingInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type bsIpv6MldSnoopingInterfaceProxyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_BsIpv6MldSnoopingInterfaceProxyIfIndex_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceProxyIfIndex = _BsIpv6MldSnoopingInterfaceProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 11),
    _BsIpv6MldSnoopingInterfaceProxyIfIndex_Type()
)
bsIpv6MldSnoopingInterfaceProxyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceProxyIfIndex.setStatus("current")
_BsIpv6MldSnoopingInterfaceQuerierUpTime_Type = TimeTicks
_BsIpv6MldSnoopingInterfaceQuerierUpTime_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceQuerierUpTime = _BsIpv6MldSnoopingInterfaceQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 12),
    _BsIpv6MldSnoopingInterfaceQuerierUpTime_Type()
)
bsIpv6MldSnoopingInterfaceQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceQuerierUpTime.setStatus("current")
_BsIpv6MldSnoopingInterfaceQuerierExpiryTime_Type = TimeTicks
_BsIpv6MldSnoopingInterfaceQuerierExpiryTime_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceQuerierExpiryTime = _BsIpv6MldSnoopingInterfaceQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 13),
    _BsIpv6MldSnoopingInterfaceQuerierExpiryTime_Type()
)
bsIpv6MldSnoopingInterfaceQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceQuerierExpiryTime.setStatus("current")


class _BsIpv6MldSnoopingInterfaceEnabled_Type(TruthValue):
    """Custom type bsIpv6MldSnoopingInterfaceEnabled based on TruthValue"""


_BsIpv6MldSnoopingInterfaceEnabled_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceEnabled = _BsIpv6MldSnoopingInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 14),
    _BsIpv6MldSnoopingInterfaceEnabled_Type()
)
bsIpv6MldSnoopingInterfaceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceEnabled.setStatus("current")
_BsIpv6MldSnoopingInterfaceIgmpMRouterPorts_Type = PortSet
_BsIpv6MldSnoopingInterfaceIgmpMRouterPorts_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceIgmpMRouterPorts = _BsIpv6MldSnoopingInterfaceIgmpMRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 15),
    _BsIpv6MldSnoopingInterfaceIgmpMRouterPorts_Type()
)
bsIpv6MldSnoopingInterfaceIgmpMRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceIgmpMRouterPorts.setStatus("current")
_BsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts_Type = PortSet
_BsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts = _BsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 16),
    _BsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts_Type()
)
bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts.setStatus("current")
_BsIpv6MldSnoopingInterfaceIgmpMRouterExpiration_Type = Integer32
_BsIpv6MldSnoopingInterfaceIgmpMRouterExpiration_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration = _BsIpv6MldSnoopingInterfaceIgmpMRouterExpiration_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 17),
    _BsIpv6MldSnoopingInterfaceIgmpMRouterExpiration_Type()
)
bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration.setStatus("current")
_BsIpv6MldSnoopingInterfaceOperationalVersion_Type = Unsigned32
_BsIpv6MldSnoopingInterfaceOperationalVersion_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceOperationalVersion = _BsIpv6MldSnoopingInterfaceOperationalVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 18),
    _BsIpv6MldSnoopingInterfaceOperationalVersion_Type()
)
bsIpv6MldSnoopingInterfaceOperationalVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceOperationalVersion.setStatus("current")
_BsIpv6MldSnoopingInterfaceSendQuery_Type = TruthValue
_BsIpv6MldSnoopingInterfaceSendQuery_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceSendQuery = _BsIpv6MldSnoopingInterfaceSendQuery_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 19),
    _BsIpv6MldSnoopingInterfaceSendQuery_Type()
)
bsIpv6MldSnoopingInterfaceSendQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceSendQuery.setStatus("current")
_BsIpv6MldSnoopingInterfaceProxy_Type = TruthValue
_BsIpv6MldSnoopingInterfaceProxy_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceProxy = _BsIpv6MldSnoopingInterfaceProxy_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 20),
    _BsIpv6MldSnoopingInterfaceProxy_Type()
)
bsIpv6MldSnoopingInterfaceProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceProxy.setStatus("current")


class _BsIpv6MldSnoopingInterfaceFlush_Type(Integer32):
    """Custom type bsIpv6MldSnoopingInterfaceFlush based on Integer32"""
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
        *(("all", 4),
          ("groups", 2),
          ("mrouters", 3),
          ("noAction", 1))
    )


_BsIpv6MldSnoopingInterfaceFlush_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingInterfaceFlush_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceFlush = _BsIpv6MldSnoopingInterfaceFlush_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 21),
    _BsIpv6MldSnoopingInterfaceFlush_Type()
)
bsIpv6MldSnoopingInterfaceFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceFlush.setStatus("current")
_BsIpv6MldSnoopingInterfaceFlushPorts_Type = PortSet
_BsIpv6MldSnoopingInterfaceFlushPorts_Object = MibTableColumn
bsIpv6MldSnoopingInterfaceFlushPorts = _BsIpv6MldSnoopingInterfaceFlushPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 1, 1, 22),
    _BsIpv6MldSnoopingInterfaceFlushPorts_Type()
)
bsIpv6MldSnoopingInterfaceFlushPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingInterfaceFlushPorts.setStatus("current")
_BsIpv6MldSnoopingCacheTable_Object = MibTable
bsIpv6MldSnoopingCacheTable = _BsIpv6MldSnoopingCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2)
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheTable.setStatus("current")
_BsIpv6MldSnoopingCacheEntry_Object = MibTableRow
bsIpv6MldSnoopingCacheEntry = _BsIpv6MldSnoopingCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1)
)
bsIpv6MldSnoopingCacheEntry.setIndexNames(
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingCacheAddress"),
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingCacheIfIndex"),
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheEntry.setStatus("current")


class _BsIpv6MldSnoopingCacheAddress_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingCacheAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingCacheAddress_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingCacheAddress_Object = MibTableColumn
bsIpv6MldSnoopingCacheAddress = _BsIpv6MldSnoopingCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 1),
    _BsIpv6MldSnoopingCacheAddress_Type()
)
bsIpv6MldSnoopingCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheAddress.setStatus("current")
_BsIpv6MldSnoopingCacheIfIndex_Type = InterfaceIndex
_BsIpv6MldSnoopingCacheIfIndex_Object = MibTableColumn
bsIpv6MldSnoopingCacheIfIndex = _BsIpv6MldSnoopingCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 2),
    _BsIpv6MldSnoopingCacheIfIndex_Type()
)
bsIpv6MldSnoopingCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheIfIndex.setStatus("current")


class _BsIpv6MldSnoopingCacheSelf_Type(TruthValue):
    """Custom type bsIpv6MldSnoopingCacheSelf based on TruthValue"""


_BsIpv6MldSnoopingCacheSelf_Object = MibTableColumn
bsIpv6MldSnoopingCacheSelf = _BsIpv6MldSnoopingCacheSelf_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 3),
    _BsIpv6MldSnoopingCacheSelf_Type()
)
bsIpv6MldSnoopingCacheSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheSelf.setStatus("current")


class _BsIpv6MldSnoopingCacheLastReporter_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingCacheLastReporter based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingCacheLastReporter_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingCacheLastReporter_Object = MibTableColumn
bsIpv6MldSnoopingCacheLastReporter = _BsIpv6MldSnoopingCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 4),
    _BsIpv6MldSnoopingCacheLastReporter_Type()
)
bsIpv6MldSnoopingCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheLastReporter.setStatus("current")
_BsIpv6MldSnoopingCacheUpTime_Type = TimeTicks
_BsIpv6MldSnoopingCacheUpTime_Object = MibTableColumn
bsIpv6MldSnoopingCacheUpTime = _BsIpv6MldSnoopingCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 5),
    _BsIpv6MldSnoopingCacheUpTime_Type()
)
bsIpv6MldSnoopingCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheUpTime.setStatus("current")
_BsIpv6MldSnoopingCacheExpiryTime_Type = TimeTicks
_BsIpv6MldSnoopingCacheExpiryTime_Object = MibTableColumn
bsIpv6MldSnoopingCacheExpiryTime = _BsIpv6MldSnoopingCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 6),
    _BsIpv6MldSnoopingCacheExpiryTime_Type()
)
bsIpv6MldSnoopingCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheExpiryTime.setStatus("current")
_BsIpv6MldSnoopingCacheStatus_Type = RowStatus
_BsIpv6MldSnoopingCacheStatus_Object = MibTableColumn
bsIpv6MldSnoopingCacheStatus = _BsIpv6MldSnoopingCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 7),
    _BsIpv6MldSnoopingCacheStatus_Type()
)
bsIpv6MldSnoopingCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheStatus.setStatus("current")


class _BsIpv6MldSnoopingCacheType_Type(Integer32):
    """Custom type bsIpv6MldSnoopingCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("other", 1),
          ("static", 3))
    )


_BsIpv6MldSnoopingCacheType_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingCacheType_Object = MibTableColumn
bsIpv6MldSnoopingCacheType = _BsIpv6MldSnoopingCacheType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 2, 1, 8),
    _BsIpv6MldSnoopingCacheType_Type()
)
bsIpv6MldSnoopingCacheType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingCacheType.setStatus("current")
_BsIpv6MldSnoopingIgmpGroupTable_Object = MibTable
bsIpv6MldSnoopingIgmpGroupTable = _BsIpv6MldSnoopingIgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3)
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupTable.setStatus("current")
_BsIpv6MldSnoopingIgmpGroupEntry_Object = MibTableRow
bsIpv6MldSnoopingIgmpGroupEntry = _BsIpv6MldSnoopingIgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1)
)
bsIpv6MldSnoopingIgmpGroupEntry.setIndexNames(
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupIpv6Address"),
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupMembers"),
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupSourceAddress"),
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingIgmpGroupIfIndex"),
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupEntry.setStatus("current")


class _BsIpv6MldSnoopingIgmpGroupIpv6Address_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingIgmpGroupIpv6Address based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingIgmpGroupIpv6Address_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingIgmpGroupIpv6Address_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupIpv6Address = _BsIpv6MldSnoopingIgmpGroupIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 1),
    _BsIpv6MldSnoopingIgmpGroupIpv6Address_Type()
)
bsIpv6MldSnoopingIgmpGroupIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupIpv6Address.setStatus("current")


class _BsIpv6MldSnoopingIgmpGroupMembers_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingIgmpGroupMembers based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingIgmpGroupMembers_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingIgmpGroupMembers_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupMembers = _BsIpv6MldSnoopingIgmpGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 2),
    _BsIpv6MldSnoopingIgmpGroupMembers_Type()
)
bsIpv6MldSnoopingIgmpGroupMembers.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupMembers.setStatus("current")


class _BsIpv6MldSnoopingIgmpGroupSourceAddress_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingIgmpGroupSourceAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingIgmpGroupSourceAddress_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingIgmpGroupSourceAddress_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupSourceAddress = _BsIpv6MldSnoopingIgmpGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 3),
    _BsIpv6MldSnoopingIgmpGroupSourceAddress_Type()
)
bsIpv6MldSnoopingIgmpGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupSourceAddress.setStatus("current")
_BsIpv6MldSnoopingIgmpGroupIfIndex_Type = InterfaceIndex
_BsIpv6MldSnoopingIgmpGroupIfIndex_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupIfIndex = _BsIpv6MldSnoopingIgmpGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 4),
    _BsIpv6MldSnoopingIgmpGroupIfIndex_Type()
)
bsIpv6MldSnoopingIgmpGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupIfIndex.setStatus("current")
_BsIpv6MldSnoopingIgmpGroupInPort_Type = PortList
_BsIpv6MldSnoopingIgmpGroupInPort_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupInPort = _BsIpv6MldSnoopingIgmpGroupInPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 5),
    _BsIpv6MldSnoopingIgmpGroupInPort_Type()
)
bsIpv6MldSnoopingIgmpGroupInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupInPort.setStatus("current")
_BsIpv6MldSnoopingIgmpGroupExpiration_Type = Integer32
_BsIpv6MldSnoopingIgmpGroupExpiration_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupExpiration = _BsIpv6MldSnoopingIgmpGroupExpiration_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 6),
    _BsIpv6MldSnoopingIgmpGroupExpiration_Type()
)
bsIpv6MldSnoopingIgmpGroupExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupExpiration.setStatus("current")


class _BsIpv6MldSnoopingIgmpGroupUserId_Type(DisplayString):
    """Custom type bsIpv6MldSnoopingIgmpGroupUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BsIpv6MldSnoopingIgmpGroupUserId_Type.__name__ = "DisplayString"
_BsIpv6MldSnoopingIgmpGroupUserId_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupUserId = _BsIpv6MldSnoopingIgmpGroupUserId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 7),
    _BsIpv6MldSnoopingIgmpGroupUserId_Type()
)
bsIpv6MldSnoopingIgmpGroupUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupUserId.setStatus("current")


class _BsIpv6MldSnoopingIgmpGroupType_Type(Integer32):
    """Custom type bsIpv6MldSnoopingIgmpGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("other", 1),
          ("static", 3))
    )


_BsIpv6MldSnoopingIgmpGroupType_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingIgmpGroupType_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupType = _BsIpv6MldSnoopingIgmpGroupType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 8),
    _BsIpv6MldSnoopingIgmpGroupType_Type()
)
bsIpv6MldSnoopingIgmpGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupType.setStatus("current")


class _BsIpv6MldSnoopingIgmpGroupMode_Type(Integer32):
    """Custom type bsIpv6MldSnoopingIgmpGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 3),
          ("include", 2),
          ("received", 1))
    )


_BsIpv6MldSnoopingIgmpGroupMode_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingIgmpGroupMode_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupMode = _BsIpv6MldSnoopingIgmpGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 9),
    _BsIpv6MldSnoopingIgmpGroupMode_Type()
)
bsIpv6MldSnoopingIgmpGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupMode.setStatus("current")


class _BsIpv6MldSnoopingIgmpGroupVersion_Type(Integer32):
    """Custom type bsIpv6MldSnoopingIgmpGroupVersion based on Integer32"""
    defaultValue = 1

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


_BsIpv6MldSnoopingIgmpGroupVersion_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingIgmpGroupVersion_Object = MibTableColumn
bsIpv6MldSnoopingIgmpGroupVersion = _BsIpv6MldSnoopingIgmpGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 3, 1, 10),
    _BsIpv6MldSnoopingIgmpGroupVersion_Type()
)
bsIpv6MldSnoopingIgmpGroupVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingIgmpGroupVersion.setStatus("current")
_BsIpv6MldSnoopingProxyCacheTable_Object = MibTable
bsIpv6MldSnoopingProxyCacheTable = _BsIpv6MldSnoopingProxyCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4)
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheTable.setStatus("current")
_BsIpv6MldSnoopingProxyCacheEntry_Object = MibTableRow
bsIpv6MldSnoopingProxyCacheEntry = _BsIpv6MldSnoopingProxyCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1)
)
bsIpv6MldSnoopingProxyCacheEntry.setIndexNames(
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingProxyCacheIfIndex"),
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingProxyCacheGroupAddress"),
    (0, "BAY-STACK-IPV6-MLD-SNOOPING-MIB", "bsIpv6MldSnoopingProxyCacheSourceAddress"),
)
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheEntry.setStatus("current")
_BsIpv6MldSnoopingProxyCacheIfIndex_Type = InterfaceIndex
_BsIpv6MldSnoopingProxyCacheIfIndex_Object = MibTableColumn
bsIpv6MldSnoopingProxyCacheIfIndex = _BsIpv6MldSnoopingProxyCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 1),
    _BsIpv6MldSnoopingProxyCacheIfIndex_Type()
)
bsIpv6MldSnoopingProxyCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheIfIndex.setStatus("current")


class _BsIpv6MldSnoopingProxyCacheGroupAddress_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingProxyCacheGroupAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingProxyCacheGroupAddress_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingProxyCacheGroupAddress_Object = MibTableColumn
bsIpv6MldSnoopingProxyCacheGroupAddress = _BsIpv6MldSnoopingProxyCacheGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 2),
    _BsIpv6MldSnoopingProxyCacheGroupAddress_Type()
)
bsIpv6MldSnoopingProxyCacheGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheGroupAddress.setStatus("current")


class _BsIpv6MldSnoopingProxyCacheSourceAddress_Type(InetAddressIPv6):
    """Custom type bsIpv6MldSnoopingProxyCacheSourceAddress based on InetAddressIPv6"""
    subtypeSpec = InetAddressIPv6.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BsIpv6MldSnoopingProxyCacheSourceAddress_Type.__name__ = "InetAddressIPv6"
_BsIpv6MldSnoopingProxyCacheSourceAddress_Object = MibTableColumn
bsIpv6MldSnoopingProxyCacheSourceAddress = _BsIpv6MldSnoopingProxyCacheSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 3),
    _BsIpv6MldSnoopingProxyCacheSourceAddress_Type()
)
bsIpv6MldSnoopingProxyCacheSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheSourceAddress.setStatus("current")


class _BsIpv6MldSnoopingProxyCacheVersion_Type(Integer32):
    """Custom type bsIpv6MldSnoopingProxyCacheVersion based on Integer32"""
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


_BsIpv6MldSnoopingProxyCacheVersion_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingProxyCacheVersion_Object = MibTableColumn
bsIpv6MldSnoopingProxyCacheVersion = _BsIpv6MldSnoopingProxyCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 4),
    _BsIpv6MldSnoopingProxyCacheVersion_Type()
)
bsIpv6MldSnoopingProxyCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheVersion.setStatus("current")


class _BsIpv6MldSnoopingProxyCacheType_Type(Integer32):
    """Custom type bsIpv6MldSnoopingProxyCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_BsIpv6MldSnoopingProxyCacheType_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingProxyCacheType_Object = MibTableColumn
bsIpv6MldSnoopingProxyCacheType = _BsIpv6MldSnoopingProxyCacheType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 5),
    _BsIpv6MldSnoopingProxyCacheType_Type()
)
bsIpv6MldSnoopingProxyCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheType.setStatus("current")


class _BsIpv6MldSnoopingProxyCacheMode_Type(Integer32):
    """Custom type bsIpv6MldSnoopingProxyCacheMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 3),
          ("include", 2),
          ("version1", 1))
    )


_BsIpv6MldSnoopingProxyCacheMode_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingProxyCacheMode_Object = MibTableColumn
bsIpv6MldSnoopingProxyCacheMode = _BsIpv6MldSnoopingProxyCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 1, 4, 1, 6),
    _BsIpv6MldSnoopingProxyCacheMode_Type()
)
bsIpv6MldSnoopingProxyCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingProxyCacheMode.setStatus("current")
_BsIpv6MldSnoopingScalars_ObjectIdentity = ObjectIdentity
bsIpv6MldSnoopingScalars = _BsIpv6MldSnoopingScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 2)
)


class _BsIpv6MldSnoopingFlush_Type(Integer32):
    """Custom type bsIpv6MldSnoopingFlush based on Integer32"""
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
        *(("all", 4),
          ("groups", 2),
          ("mrouters", 3),
          ("noAction", 1))
    )


_BsIpv6MldSnoopingFlush_Type.__name__ = "Integer32"
_BsIpv6MldSnoopingFlush_Object = MibScalar
bsIpv6MldSnoopingFlush = _BsIpv6MldSnoopingFlush_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 2, 1),
    _BsIpv6MldSnoopingFlush_Type()
)
bsIpv6MldSnoopingFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingFlush.setStatus("current")
_BsIpv6MldSnoopingFlushPorts_Type = PortSet
_BsIpv6MldSnoopingFlushPorts_Object = MibScalar
bsIpv6MldSnoopingFlushPorts = _BsIpv6MldSnoopingFlushPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 44, 2, 2),
    _BsIpv6MldSnoopingFlushPorts_Type()
)
bsIpv6MldSnoopingFlushPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6MldSnoopingFlushPorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-IPV6-MLD-SNOOPING-MIB",
    **{"bayStackIpv6MldSnoopingMib": bayStackIpv6MldSnoopingMib,
       "bsIpv6MldSnoopingNotifications": bsIpv6MldSnoopingNotifications,
       "bsIpv6MldSnoopingObjects": bsIpv6MldSnoopingObjects,
       "bsIpv6MldSnoopingInterfaceTable": bsIpv6MldSnoopingInterfaceTable,
       "bsIpv6MldSnoopingInterfaceEntry": bsIpv6MldSnoopingInterfaceEntry,
       "bsIpv6MldSnoopingInterfaceIfIndex": bsIpv6MldSnoopingInterfaceIfIndex,
       "bsIpv6MldSnoopingInterfaceQueryInterval": bsIpv6MldSnoopingInterfaceQueryInterval,
       "bsIpv6MldSnoopingInterfaceStatus": bsIpv6MldSnoopingInterfaceStatus,
       "bsIpv6MldSnoopingInterfaceVersion": bsIpv6MldSnoopingInterfaceVersion,
       "bsIpv6MldSnoopingInterfaceQuerier": bsIpv6MldSnoopingInterfaceQuerier,
       "bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay": bsIpv6MldSnoopingInterfaceQueryMaxResponseDelay,
       "bsIpv6MldSnoopingInterfaceJoins": bsIpv6MldSnoopingInterfaceJoins,
       "bsIpv6MldSnoopingInterfaceGroups": bsIpv6MldSnoopingInterfaceGroups,
       "bsIpv6MldSnoopingInterfaceRobustness": bsIpv6MldSnoopingInterfaceRobustness,
       "bsIpv6MldSnoopingInterfaceLastListenQueryIntvl": bsIpv6MldSnoopingInterfaceLastListenQueryIntvl,
       "bsIpv6MldSnoopingInterfaceProxyIfIndex": bsIpv6MldSnoopingInterfaceProxyIfIndex,
       "bsIpv6MldSnoopingInterfaceQuerierUpTime": bsIpv6MldSnoopingInterfaceQuerierUpTime,
       "bsIpv6MldSnoopingInterfaceQuerierExpiryTime": bsIpv6MldSnoopingInterfaceQuerierExpiryTime,
       "bsIpv6MldSnoopingInterfaceEnabled": bsIpv6MldSnoopingInterfaceEnabled,
       "bsIpv6MldSnoopingInterfaceIgmpMRouterPorts": bsIpv6MldSnoopingInterfaceIgmpMRouterPorts,
       "bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts": bsIpv6MldSnoopingInterfaceIgmpActiveMRouterPorts,
       "bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration": bsIpv6MldSnoopingInterfaceIgmpMRouterExpiration,
       "bsIpv6MldSnoopingInterfaceOperationalVersion": bsIpv6MldSnoopingInterfaceOperationalVersion,
       "bsIpv6MldSnoopingInterfaceSendQuery": bsIpv6MldSnoopingInterfaceSendQuery,
       "bsIpv6MldSnoopingInterfaceProxy": bsIpv6MldSnoopingInterfaceProxy,
       "bsIpv6MldSnoopingInterfaceFlush": bsIpv6MldSnoopingInterfaceFlush,
       "bsIpv6MldSnoopingInterfaceFlushPorts": bsIpv6MldSnoopingInterfaceFlushPorts,
       "bsIpv6MldSnoopingCacheTable": bsIpv6MldSnoopingCacheTable,
       "bsIpv6MldSnoopingCacheEntry": bsIpv6MldSnoopingCacheEntry,
       "bsIpv6MldSnoopingCacheAddress": bsIpv6MldSnoopingCacheAddress,
       "bsIpv6MldSnoopingCacheIfIndex": bsIpv6MldSnoopingCacheIfIndex,
       "bsIpv6MldSnoopingCacheSelf": bsIpv6MldSnoopingCacheSelf,
       "bsIpv6MldSnoopingCacheLastReporter": bsIpv6MldSnoopingCacheLastReporter,
       "bsIpv6MldSnoopingCacheUpTime": bsIpv6MldSnoopingCacheUpTime,
       "bsIpv6MldSnoopingCacheExpiryTime": bsIpv6MldSnoopingCacheExpiryTime,
       "bsIpv6MldSnoopingCacheStatus": bsIpv6MldSnoopingCacheStatus,
       "bsIpv6MldSnoopingCacheType": bsIpv6MldSnoopingCacheType,
       "bsIpv6MldSnoopingIgmpGroupTable": bsIpv6MldSnoopingIgmpGroupTable,
       "bsIpv6MldSnoopingIgmpGroupEntry": bsIpv6MldSnoopingIgmpGroupEntry,
       "bsIpv6MldSnoopingIgmpGroupIpv6Address": bsIpv6MldSnoopingIgmpGroupIpv6Address,
       "bsIpv6MldSnoopingIgmpGroupMembers": bsIpv6MldSnoopingIgmpGroupMembers,
       "bsIpv6MldSnoopingIgmpGroupSourceAddress": bsIpv6MldSnoopingIgmpGroupSourceAddress,
       "bsIpv6MldSnoopingIgmpGroupIfIndex": bsIpv6MldSnoopingIgmpGroupIfIndex,
       "bsIpv6MldSnoopingIgmpGroupInPort": bsIpv6MldSnoopingIgmpGroupInPort,
       "bsIpv6MldSnoopingIgmpGroupExpiration": bsIpv6MldSnoopingIgmpGroupExpiration,
       "bsIpv6MldSnoopingIgmpGroupUserId": bsIpv6MldSnoopingIgmpGroupUserId,
       "bsIpv6MldSnoopingIgmpGroupType": bsIpv6MldSnoopingIgmpGroupType,
       "bsIpv6MldSnoopingIgmpGroupMode": bsIpv6MldSnoopingIgmpGroupMode,
       "bsIpv6MldSnoopingIgmpGroupVersion": bsIpv6MldSnoopingIgmpGroupVersion,
       "bsIpv6MldSnoopingProxyCacheTable": bsIpv6MldSnoopingProxyCacheTable,
       "bsIpv6MldSnoopingProxyCacheEntry": bsIpv6MldSnoopingProxyCacheEntry,
       "bsIpv6MldSnoopingProxyCacheIfIndex": bsIpv6MldSnoopingProxyCacheIfIndex,
       "bsIpv6MldSnoopingProxyCacheGroupAddress": bsIpv6MldSnoopingProxyCacheGroupAddress,
       "bsIpv6MldSnoopingProxyCacheSourceAddress": bsIpv6MldSnoopingProxyCacheSourceAddress,
       "bsIpv6MldSnoopingProxyCacheVersion": bsIpv6MldSnoopingProxyCacheVersion,
       "bsIpv6MldSnoopingProxyCacheType": bsIpv6MldSnoopingProxyCacheType,
       "bsIpv6MldSnoopingProxyCacheMode": bsIpv6MldSnoopingProxyCacheMode,
       "bsIpv6MldSnoopingScalars": bsIpv6MldSnoopingScalars,
       "bsIpv6MldSnoopingFlush": bsIpv6MldSnoopingFlush,
       "bsIpv6MldSnoopingFlushPorts": bsIpv6MldSnoopingFlushPorts}
)
