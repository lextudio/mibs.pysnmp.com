# SNMP MIB module (STN-IPROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-IPROUTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:04 2024
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(stnSystems,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnSystems")

(stnCpuIpRouteLimit,
 stnEngineCpu,
 stnEngineSlot,
 stnEngineType) = mibBuilder.importSymbols(
    "STN-CHASSIS-MIB",
    "stnCpuIpRouteLimit",
    "stnEngineCpu",
    "stnEngineSlot",
    "stnEngineType")

(stnRouterIndex,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterIndex")


# MODULE-IDENTITY

stnIpRouting = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnIp_ObjectIdentity = ObjectIdentity
stnIp = _StnIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1)
)
_StnIpRtCache_ObjectIdentity = ObjectIdentity
stnIpRtCache = _StnIpRtCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1)
)
_StnIpRtCacheEntries_Type = Gauge32
_StnIpRtCacheEntries_Object = MibScalar
stnIpRtCacheEntries = _StnIpRtCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 1),
    _StnIpRtCacheEntries_Type()
)
stnIpRtCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheEntries.setStatus("current")
_StnIpRtCacheMisses_Type = Counter32
_StnIpRtCacheMisses_Object = MibScalar
stnIpRtCacheMisses = _StnIpRtCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 2),
    _StnIpRtCacheMisses_Type()
)
stnIpRtCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheMisses.setStatus("current")
_StnIpRtCacheHits_Type = Counter32
_StnIpRtCacheHits_Object = MibScalar
stnIpRtCacheHits = _StnIpRtCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 3),
    _StnIpRtCacheHits_Type()
)
stnIpRtCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheHits.setStatus("current")
_StnIpRtCacheRemovals_Type = Counter32
_StnIpRtCacheRemovals_Object = MibScalar
stnIpRtCacheRemovals = _StnIpRtCacheRemovals_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 4),
    _StnIpRtCacheRemovals_Type()
)
stnIpRtCacheRemovals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheRemovals.setStatus("current")
_StnIpRoutingCacheTable_Object = MibTable
stnIpRoutingCacheTable = _StnIpRoutingCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5)
)
if mibBuilder.loadTexts:
    stnIpRoutingCacheTable.setStatus("current")
_StnIpRtCacheEntry_Object = MibTableRow
stnIpRtCacheEntry = _StnIpRtCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5, 1)
)
stnIpRtCacheEntry.setIndexNames(
    (0, "STN-IPROUTING-MIB", "stnIpRtCacheIpAddress"),
    (0, "STN-IPROUTING-MIB", "stnIpRtCacheIpMask"),
)
if mibBuilder.loadTexts:
    stnIpRtCacheEntry.setStatus("current")
_StnIpRtCacheIpAddress_Type = IpAddress
_StnIpRtCacheIpAddress_Object = MibTableColumn
stnIpRtCacheIpAddress = _StnIpRtCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5, 1, 1),
    _StnIpRtCacheIpAddress_Type()
)
stnIpRtCacheIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheIpAddress.setStatus("current")
_StnIpRtCacheIpMask_Type = IpAddress
_StnIpRtCacheIpMask_Object = MibTableColumn
stnIpRtCacheIpMask = _StnIpRtCacheIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5, 1, 2),
    _StnIpRtCacheIpMask_Type()
)
stnIpRtCacheIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheIpMask.setStatus("current")
_StnIpRtCacheNextHop_Type = IpAddress
_StnIpRtCacheNextHop_Object = MibTableColumn
stnIpRtCacheNextHop = _StnIpRtCacheNextHop_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5, 1, 3),
    _StnIpRtCacheNextHop_Type()
)
stnIpRtCacheNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheNextHop.setStatus("current")
_StnIpRtCacheIfIndex_Type = Integer32
_StnIpRtCacheIfIndex_Object = MibTableColumn
stnIpRtCacheIfIndex = _StnIpRtCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5, 1, 4),
    _StnIpRtCacheIfIndex_Type()
)
stnIpRtCacheIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheIfIndex.setStatus("current")


class _StnIpRtCacheRouteType_Type(Integer32):
    """Custom type stnIpRtCacheRouteType based on Integer32"""
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
        *(("local", 3),
          ("other", 1),
          ("reject", 2),
          ("remote", 4))
    )


_StnIpRtCacheRouteType_Type.__name__ = "Integer32"
_StnIpRtCacheRouteType_Object = MibTableColumn
stnIpRtCacheRouteType = _StnIpRtCacheRouteType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5, 1, 5),
    _StnIpRtCacheRouteType_Type()
)
stnIpRtCacheRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpRtCacheRouteType.setStatus("current")
_StnIpRtCacheStatus_Type = RowStatus
_StnIpRtCacheStatus_Object = MibTableColumn
stnIpRtCacheStatus = _StnIpRtCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 1, 5, 1, 6),
    _StnIpRtCacheStatus_Type()
)
stnIpRtCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnIpRtCacheStatus.setStatus("current")
_StnIpCircExtTable_Object = MibTable
stnIpCircExtTable = _StnIpCircExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2)
)
if mibBuilder.loadTexts:
    stnIpCircExtTable.setStatus("current")
_StnIpCircExtEntry_Object = MibTableRow
stnIpCircExtEntry = _StnIpCircExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1)
)
stnIpCircExtEntry.setIndexNames(
    (0, "STN-IPROUTING-MIB", "stnIpCircExtIfIndex"),
)
if mibBuilder.loadTexts:
    stnIpCircExtEntry.setStatus("current")
_StnIpCircExtIfIndex_Type = Integer32
_StnIpCircExtIfIndex_Object = MibTableColumn
stnIpCircExtIfIndex = _StnIpCircExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 1),
    _StnIpCircExtIfIndex_Type()
)
stnIpCircExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCircExtIfIndex.setStatus("current")


class _StnIpCircExtAdminState_Type(Integer32):
    """Custom type stnIpCircExtAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnIpCircExtAdminState_Type.__name__ = "Integer32"
_StnIpCircExtAdminState_Object = MibTableColumn
stnIpCircExtAdminState = _StnIpCircExtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 2),
    _StnIpCircExtAdminState_Type()
)
stnIpCircExtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnIpCircExtAdminState.setStatus("current")


class _StnIpCircExtOperState_Type(Integer32):
    """Custom type stnIpCircExtOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_StnIpCircExtOperState_Type.__name__ = "Integer32"
_StnIpCircExtOperState_Object = MibTableColumn
stnIpCircExtOperState = _StnIpCircExtOperState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 3),
    _StnIpCircExtOperState_Type()
)
stnIpCircExtOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCircExtOperState.setStatus("current")
_StnIpCircExtIpAddress_Type = IpAddress
_StnIpCircExtIpAddress_Object = MibTableColumn
stnIpCircExtIpAddress = _StnIpCircExtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 4),
    _StnIpCircExtIpAddress_Type()
)
stnIpCircExtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCircExtIpAddress.setStatus("current")
_StnIpCircExtIpMask_Type = IpAddress
_StnIpCircExtIpMask_Object = MibTableColumn
stnIpCircExtIpMask = _StnIpCircExtIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 5),
    _StnIpCircExtIpMask_Type()
)
stnIpCircExtIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCircExtIpMask.setStatus("current")


class _StnIpCircExtMaxReasm_Type(Integer32):
    """Custom type stnIpCircExtMaxReasm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnIpCircExtMaxReasm_Type.__name__ = "Integer32"
_StnIpCircExtMaxReasm_Object = MibTableColumn
stnIpCircExtMaxReasm = _StnIpCircExtMaxReasm_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 6),
    _StnIpCircExtMaxReasm_Type()
)
stnIpCircExtMaxReasm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCircExtMaxReasm.setStatus("current")
_StnIpCircExtMaxMtu_Type = Integer32
_StnIpCircExtMaxMtu_Object = MibTableColumn
stnIpCircExtMaxMtu = _StnIpCircExtMaxMtu_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 7),
    _StnIpCircExtMaxMtu_Type()
)
stnIpCircExtMaxMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCircExtMaxMtu.setStatus("current")
_StnIpCircExtBcastAddr_Type = IpAddress
_StnIpCircExtBcastAddr_Object = MibTableColumn
stnIpCircExtBcastAddr = _StnIpCircExtBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 2, 1, 8),
    _StnIpCircExtBcastAddr_Type()
)
stnIpCircExtBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCircExtBcastAddr.setStatus("current")
_StnIpDetailsTable_Object = MibTable
stnIpDetailsTable = _StnIpDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3)
)
if mibBuilder.loadTexts:
    stnIpDetailsTable.setStatus("current")
_StnIpDetailsEntry_Object = MibTableRow
stnIpDetailsEntry = _StnIpDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3, 1)
)
stnIpDetailsEntry.setIndexNames(
    (0, "STN-IPROUTING-MIB", "stnIpDetailsIndex"),
)
if mibBuilder.loadTexts:
    stnIpDetailsEntry.setStatus("current")
_StnIpDetailsIndex_Type = Integer32
_StnIpDetailsIndex_Object = MibTableColumn
stnIpDetailsIndex = _StnIpDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3, 1, 1),
    _StnIpDetailsIndex_Type()
)
stnIpDetailsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnIpDetailsIndex.setStatus("current")
_StnIpDetailsSource_Type = IpAddress
_StnIpDetailsSource_Object = MibTableColumn
stnIpDetailsSource = _StnIpDetailsSource_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3, 1, 2),
    _StnIpDetailsSource_Type()
)
stnIpDetailsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpDetailsSource.setStatus("current")
_StnIpDetailsDest_Type = IpAddress
_StnIpDetailsDest_Object = MibTableColumn
stnIpDetailsDest = _StnIpDetailsDest_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3, 1, 3),
    _StnIpDetailsDest_Type()
)
stnIpDetailsDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpDetailsDest.setStatus("current")


class _StnIpDetailsType_Type(Integer32):
    """Custom type stnIpDetailsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("header-error", 1),
          ("no-route", 3),
          ("param-problem", 5),
          ("redirect", 6),
          ("ttl-exceed", 4),
          ("unknown-proto", 2))
    )


_StnIpDetailsType_Type.__name__ = "Integer32"
_StnIpDetailsType_Object = MibTableColumn
stnIpDetailsType = _StnIpDetailsType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3, 1, 4),
    _StnIpDetailsType_Type()
)
stnIpDetailsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpDetailsType.setStatus("current")
_StnIpDetailsTimeStamp_Type = TimeStamp
_StnIpDetailsTimeStamp_Object = MibTableColumn
stnIpDetailsTimeStamp = _StnIpDetailsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3, 1, 5),
    _StnIpDetailsTimeStamp_Type()
)
stnIpDetailsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpDetailsTimeStamp.setStatus("current")


class _StnIpDetailsHeader_Type(OctetString):
    """Custom type stnIpDetailsHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_StnIpDetailsHeader_Type.__name__ = "OctetString"
_StnIpDetailsHeader_Object = MibTableColumn
stnIpDetailsHeader = _StnIpDetailsHeader_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 3, 1, 6),
    _StnIpDetailsHeader_Type()
)
stnIpDetailsHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpDetailsHeader.setStatus("current")
_StnIpRoutingVars_ObjectIdentity = ObjectIdentity
stnIpRoutingVars = _StnIpRoutingVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 4)
)
_StnIpMaxRoutingTableSize_Type = Integer32
_StnIpMaxRoutingTableSize_Object = MibScalar
stnIpMaxRoutingTableSize = _StnIpMaxRoutingTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 4, 1),
    _StnIpMaxRoutingTableSize_Type()
)
stnIpMaxRoutingTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpMaxRoutingTableSize.setStatus("current")
_StnIpCurrentRoutingTableSize_Type = Integer32
_StnIpCurrentRoutingTableSize_Object = MibScalar
stnIpCurrentRoutingTableSize = _StnIpCurrentRoutingTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 4, 2),
    _StnIpCurrentRoutingTableSize_Type()
)
stnIpCurrentRoutingTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIpCurrentRoutingTableSize.setStatus("current")
_StnIpTraps_ObjectIdentity = ObjectIdentity
stnIpTraps = _StnIpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 5)
)
_StnIpTrapVars_ObjectIdentity = ObjectIdentity
stnIpTrapVars = _StnIpTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 5, 1)
)
_StnIpNotificationPrefix_ObjectIdentity = ObjectIdentity
stnIpNotificationPrefix = _StnIpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 5, 2)
)
_StnIpNotification_ObjectIdentity = ObjectIdentity
stnIpNotification = _StnIpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 5, 2, 0)
)
_StnArp_ObjectIdentity = ObjectIdentity
stnArp = _StnArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2)
)
_StnArpExtTtl_Type = Integer32
_StnArpExtTtl_Object = MibScalar
stnArpExtTtl = _StnArpExtTtl_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 1),
    _StnArpExtTtl_Type()
)
stnArpExtTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnArpExtTtl.setStatus("current")
_StnArpExtRcvdRequests_Type = Counter32
_StnArpExtRcvdRequests_Object = MibScalar
stnArpExtRcvdRequests = _StnArpExtRcvdRequests_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 2),
    _StnArpExtRcvdRequests_Type()
)
stnArpExtRcvdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnArpExtRcvdRequests.setStatus("current")
_StnArpExtRcvdReplies_Type = Counter32
_StnArpExtRcvdReplies_Object = MibScalar
stnArpExtRcvdReplies = _StnArpExtRcvdReplies_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 3),
    _StnArpExtRcvdReplies_Type()
)
stnArpExtRcvdReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnArpExtRcvdReplies.setStatus("current")
_StnArpExtSendRequests_Type = Counter32
_StnArpExtSendRequests_Object = MibScalar
stnArpExtSendRequests = _StnArpExtSendRequests_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 4),
    _StnArpExtSendRequests_Type()
)
stnArpExtSendRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnArpExtSendRequests.setStatus("current")
_StnArpExtSendReplies_Type = Counter32
_StnArpExtSendReplies_Object = MibScalar
stnArpExtSendReplies = _StnArpExtSendReplies_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 5),
    _StnArpExtSendReplies_Type()
)
stnArpExtSendReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnArpExtSendReplies.setStatus("current")
_StnArpCircExtTable_Object = MibTable
stnArpCircExtTable = _StnArpCircExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 6)
)
if mibBuilder.loadTexts:
    stnArpCircExtTable.setStatus("current")
_StnArpCircExtEntry_Object = MibTableRow
stnArpCircExtEntry = _StnArpCircExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 6, 1)
)
stnArpCircExtEntry.setIndexNames(
    (0, "STN-IPROUTING-MIB", "stnArpCircExtIfIndex"),
)
if mibBuilder.loadTexts:
    stnArpCircExtEntry.setStatus("current")
_StnArpCircExtIfIndex_Type = Integer32
_StnArpCircExtIfIndex_Object = MibTableColumn
stnArpCircExtIfIndex = _StnArpCircExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 6, 1, 1),
    _StnArpCircExtIfIndex_Type()
)
stnArpCircExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnArpCircExtIfIndex.setStatus("current")


class _StnArpCircExtDoProxy_Type(Integer32):
    """Custom type stnArpCircExtDoProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnArpCircExtDoProxy_Type.__name__ = "Integer32"
_StnArpCircExtDoProxy_Object = MibTableColumn
stnArpCircExtDoProxy = _StnArpCircExtDoProxy_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 6, 1, 2),
    _StnArpCircExtDoProxy_Type()
)
stnArpCircExtDoProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnArpCircExtDoProxy.setStatus("current")


class _StnArpCircExtDoResp_Type(Integer32):
    """Custom type stnArpCircExtDoResp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnArpCircExtDoResp_Type.__name__ = "Integer32"
_StnArpCircExtDoResp_Object = MibTableColumn
stnArpCircExtDoResp = _StnArpCircExtDoResp_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 6, 1, 3),
    _StnArpCircExtDoResp_Type()
)
stnArpCircExtDoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnArpCircExtDoResp.setStatus("current")


class _StnArpCircExtWanProxy_Type(Integer32):
    """Custom type stnArpCircExtWanProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnArpCircExtWanProxy_Type.__name__ = "Integer32"
_StnArpCircExtWanProxy_Object = MibTableColumn
stnArpCircExtWanProxy = _StnArpCircExtWanProxy_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 2, 6, 1, 4),
    _StnArpCircExtWanProxy_Type()
)
stnArpCircExtWanProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnArpCircExtWanProxy.setStatus("current")
_StnRip_ObjectIdentity = ObjectIdentity
stnRip = _StnRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3)
)


class _StnRipExtAdminState_Type(Integer32):
    """Custom type stnRipExtAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnRipExtAdminState_Type.__name__ = "Integer32"
_StnRipExtAdminState_Object = MibScalar
stnRipExtAdminState = _StnRipExtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 1),
    _StnRipExtAdminState_Type()
)
stnRipExtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnRipExtAdminState.setStatus("current")
_StnRipExtUpdateTime_Type = Integer32
_StnRipExtUpdateTime_Object = MibScalar
stnRipExtUpdateTime = _StnRipExtUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 2),
    _StnRipExtUpdateTime_Type()
)
stnRipExtUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnRipExtUpdateTime.setStatus("current")
_StnRipCircExtTable_Object = MibTable
stnRipCircExtTable = _StnRipCircExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 3)
)
if mibBuilder.loadTexts:
    stnRipCircExtTable.setStatus("current")
_StnRipCircExtEntry_Object = MibTableRow
stnRipCircExtEntry = _StnRipCircExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 3, 1)
)
stnRipCircExtEntry.setIndexNames(
    (0, "STN-IPROUTING-MIB", "stnRipCircExtIfIndex"),
)
if mibBuilder.loadTexts:
    stnRipCircExtEntry.setStatus("current")
_StnRipCircExtIfIndex_Type = Integer32
_StnRipCircExtIfIndex_Object = MibTableColumn
stnRipCircExtIfIndex = _StnRipCircExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 3, 1, 1),
    _StnRipCircExtIfIndex_Type()
)
stnRipCircExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRipCircExtIfIndex.setStatus("current")


class _StnRipCircExtTalk_Type(Integer32):
    """Custom type stnRipCircExtTalk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnRipCircExtTalk_Type.__name__ = "Integer32"
_StnRipCircExtTalk_Object = MibTableColumn
stnRipCircExtTalk = _StnRipCircExtTalk_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 3, 1, 2),
    _StnRipCircExtTalk_Type()
)
stnRipCircExtTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnRipCircExtTalk.setStatus("current")


class _StnRipCircExtListen_Type(Integer32):
    """Custom type stnRipCircExtListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnRipCircExtListen_Type.__name__ = "Integer32"
_StnRipCircExtListen_Object = MibTableColumn
stnRipCircExtListen = _StnRipCircExtListen_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 3, 1, 3),
    _StnRipCircExtListen_Type()
)
stnRipCircExtListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnRipCircExtListen.setStatus("current")


class _StnRipCircExtPoison_Type(Integer32):
    """Custom type stnRipCircExtPoison based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_StnRipCircExtPoison_Type.__name__ = "Integer32"
_StnRipCircExtPoison_Object = MibTableColumn
stnRipCircExtPoison = _StnRipCircExtPoison_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 3, 1, 4),
    _StnRipCircExtPoison_Type()
)
stnRipCircExtPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnRipCircExtPoison.setStatus("current")
_StnRipDetailsTable_Object = MibTable
stnRipDetailsTable = _StnRipDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4)
)
if mibBuilder.loadTexts:
    stnRipDetailsTable.setStatus("current")
_StnRipDetailsEntry_Object = MibTableRow
stnRipDetailsEntry = _StnRipDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4, 1)
)
stnRipDetailsEntry.setIndexNames(
    (0, "STN-IPROUTING-MIB", "stnRipDetailsIndex"),
)
if mibBuilder.loadTexts:
    stnRipDetailsEntry.setStatus("current")
_StnRipDetailsIndex_Type = Integer32
_StnRipDetailsIndex_Object = MibTableColumn
stnRipDetailsIndex = _StnRipDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4, 1, 1),
    _StnRipDetailsIndex_Type()
)
stnRipDetailsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnRipDetailsIndex.setStatus("current")
_StnRipDetailsSource_Type = IpAddress
_StnRipDetailsSource_Object = MibTableColumn
stnRipDetailsSource = _StnRipDetailsSource_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4, 1, 2),
    _StnRipDetailsSource_Type()
)
stnRipDetailsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRipDetailsSource.setStatus("current")
_StnRipDetailsDest_Type = IpAddress
_StnRipDetailsDest_Object = MibTableColumn
stnRipDetailsDest = _StnRipDetailsDest_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4, 1, 3),
    _StnRipDetailsDest_Type()
)
stnRipDetailsDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRipDetailsDest.setStatus("current")


class _StnRipDetailsType_Type(Integer32):
    """Custom type stnRipDetailsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bad-packet", 1)
    )


_StnRipDetailsType_Type.__name__ = "Integer32"
_StnRipDetailsType_Object = MibTableColumn
stnRipDetailsType = _StnRipDetailsType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4, 1, 4),
    _StnRipDetailsType_Type()
)
stnRipDetailsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRipDetailsType.setStatus("current")
_StnRipDetailsTimeStamp_Type = TimeStamp
_StnRipDetailsTimeStamp_Object = MibTableColumn
stnRipDetailsTimeStamp = _StnRipDetailsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4, 1, 5),
    _StnRipDetailsTimeStamp_Type()
)
stnRipDetailsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRipDetailsTimeStamp.setStatus("current")


class _StnRipDetailsHeader_Type(OctetString):
    """Custom type stnRipDetailsHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_StnRipDetailsHeader_Type.__name__ = "OctetString"
_StnRipDetailsHeader_Object = MibTableColumn
stnRipDetailsHeader = _StnRipDetailsHeader_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 3, 4, 1, 6),
    _StnRipDetailsHeader_Type()
)
stnRipDetailsHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRipDetailsHeader.setStatus("current")
_StnOspf_ObjectIdentity = ObjectIdentity
stnOspf = _StnOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4)
)
_StnOspfRouterLsaCount_Type = Gauge32
_StnOspfRouterLsaCount_Object = MibScalar
stnOspfRouterLsaCount = _StnOspfRouterLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 1),
    _StnOspfRouterLsaCount_Type()
)
stnOspfRouterLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfRouterLsaCount.setStatus("current")
_StnOspfNetworkLsaCount_Type = Gauge32
_StnOspfNetworkLsaCount_Object = MibScalar
stnOspfNetworkLsaCount = _StnOspfNetworkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 2),
    _StnOspfNetworkLsaCount_Type()
)
stnOspfNetworkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfNetworkLsaCount.setStatus("current")
_StnOspfSummaryLsaCount_Type = Gauge32
_StnOspfSummaryLsaCount_Object = MibScalar
stnOspfSummaryLsaCount = _StnOspfSummaryLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 3),
    _StnOspfSummaryLsaCount_Type()
)
stnOspfSummaryLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfSummaryLsaCount.setStatus("current")
_StnOspfASBRSummaryLsaCount_Type = Gauge32
_StnOspfASBRSummaryLsaCount_Object = MibScalar
stnOspfASBRSummaryLsaCount = _StnOspfASBRSummaryLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 4),
    _StnOspfASBRSummaryLsaCount_Type()
)
stnOspfASBRSummaryLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfASBRSummaryLsaCount.setStatus("current")
_StnOspfExternLsaCount_Type = Gauge32
_StnOspfExternLsaCount_Object = MibScalar
stnOspfExternLsaCount = _StnOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 5),
    _StnOspfExternLsaCount_Type()
)
stnOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfExternLsaCount.setStatus("current")
_StnOspfMcastGroupLsaCount_Type = Gauge32
_StnOspfMcastGroupLsaCount_Object = MibScalar
stnOspfMcastGroupLsaCount = _StnOspfMcastGroupLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 6),
    _StnOspfMcastGroupLsaCount_Type()
)
stnOspfMcastGroupLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfMcastGroupLsaCount.setStatus("current")
_StnOspfExternT7LsaCount_Type = Gauge32
_StnOspfExternT7LsaCount_Object = MibScalar
stnOspfExternT7LsaCount = _StnOspfExternT7LsaCount_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 7),
    _StnOspfExternT7LsaCount_Type()
)
stnOspfExternT7LsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfExternT7LsaCount.setStatus("current")
_StnOspfTraps_ObjectIdentity = ObjectIdentity
stnOspfTraps = _StnOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 8)
)
_StnOspfDetailsTable_Object = MibTable
stnOspfDetailsTable = _StnOspfDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9)
)
if mibBuilder.loadTexts:
    stnOspfDetailsTable.setStatus("current")
_StnOspfDetailsEntry_Object = MibTableRow
stnOspfDetailsEntry = _StnOspfDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1)
)
stnOspfDetailsEntry.setIndexNames(
    (0, "STN-IPROUTING-MIB", "stnOspfDetailsIndex"),
)
if mibBuilder.loadTexts:
    stnOspfDetailsEntry.setStatus("current")
_StnOspfDetailsIndex_Type = Integer32
_StnOspfDetailsIndex_Object = MibTableColumn
stnOspfDetailsIndex = _StnOspfDetailsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1, 1),
    _StnOspfDetailsIndex_Type()
)
stnOspfDetailsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnOspfDetailsIndex.setStatus("current")
_StnOspfDetailsPacketType_Type = Integer32
_StnOspfDetailsPacketType_Object = MibTableColumn
stnOspfDetailsPacketType = _StnOspfDetailsPacketType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1, 2),
    _StnOspfDetailsPacketType_Type()
)
stnOspfDetailsPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfDetailsPacketType.setStatus("current")
_StnOspfDetailsRouterId_Type = Integer32
_StnOspfDetailsRouterId_Object = MibTableColumn
stnOspfDetailsRouterId = _StnOspfDetailsRouterId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1, 3),
    _StnOspfDetailsRouterId_Type()
)
stnOspfDetailsRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfDetailsRouterId.setStatus("current")
_StnOspfDetailsAreaId_Type = Integer32
_StnOspfDetailsAreaId_Object = MibTableColumn
stnOspfDetailsAreaId = _StnOspfDetailsAreaId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1, 4),
    _StnOspfDetailsAreaId_Type()
)
stnOspfDetailsAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfDetailsAreaId.setStatus("current")


class _StnOspfDetailsErrorType_Type(Integer32):
    """Custom type stnOspfDetailsErrorType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("areaMismatch", 2),
          ("authFailure", 6),
          ("authTypeMismatch", 5),
          ("badVersion", 1),
          ("deadIntervalMismatch", 9),
          ("designatedRouterMismatch", 12),
          ("helloIntervalMismatch", 8),
          ("invalidLength", 14),
          ("lanSubnetMismatch", 11),
          ("md5SequenceError", 16),
          ("myRouterId", 13),
          ("neighborNotFound", 15),
          ("netMaskMismatch", 7),
          ("optionMismatch", 10),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4))
    )


_StnOspfDetailsErrorType_Type.__name__ = "Integer32"
_StnOspfDetailsErrorType_Object = MibTableColumn
stnOspfDetailsErrorType = _StnOspfDetailsErrorType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1, 5),
    _StnOspfDetailsErrorType_Type()
)
stnOspfDetailsErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfDetailsErrorType.setStatus("current")
_StnOspfDetailsTimeStamp_Type = TimeStamp
_StnOspfDetailsTimeStamp_Object = MibTableColumn
stnOspfDetailsTimeStamp = _StnOspfDetailsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1, 6),
    _StnOspfDetailsTimeStamp_Type()
)
stnOspfDetailsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfDetailsTimeStamp.setStatus("current")


class _StnOspfDetailsHeader_Type(OctetString):
    """Custom type stnOspfDetailsHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_StnOspfDetailsHeader_Type.__name__ = "OctetString"
_StnOspfDetailsHeader_Object = MibTableColumn
stnOspfDetailsHeader = _StnOspfDetailsHeader_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 4, 9, 1, 7),
    _StnOspfDetailsHeader_Type()
)
stnOspfDetailsHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnOspfDetailsHeader.setStatus("current")
_StnBgp_ObjectIdentity = ObjectIdentity
stnBgp = _StnBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 5)
)

# Managed Objects groups


# Notification objects

stnIpRouterRouteLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 5, 2, 0, 1)
)
stnIpRouterRouteLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-IPROUTING-MIB", "stnIpMaxRoutingTableSize"))
)
if mibBuilder.loadTexts:
    stnIpRouterRouteLimitExceeded.setStatus(
        "current"
    )

stnIpEngineRouteLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3551, 2, 12, 1, 5, 2, 0, 2)
)
stnIpEngineRouteLimitExceeded.setObjects(
      *(("STN-CHASSIS-MIB", "stnEngineSlot"),
        ("STN-CHASSIS-MIB", "stnEngineCpu"),
        ("STN-CHASSIS-MIB", "stnEngineType"),
        ("STN-ROUTER-MIB", "stnRouterIndex"),
        ("STN-CHASSIS-MIB", "stnCpuIpRouteLimit"))
)
if mibBuilder.loadTexts:
    stnIpEngineRouteLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-IPROUTING-MIB",
    **{"stnIpRouting": stnIpRouting,
       "stnIp": stnIp,
       "stnIpRtCache": stnIpRtCache,
       "stnIpRtCacheEntries": stnIpRtCacheEntries,
       "stnIpRtCacheMisses": stnIpRtCacheMisses,
       "stnIpRtCacheHits": stnIpRtCacheHits,
       "stnIpRtCacheRemovals": stnIpRtCacheRemovals,
       "stnIpRoutingCacheTable": stnIpRoutingCacheTable,
       "stnIpRtCacheEntry": stnIpRtCacheEntry,
       "stnIpRtCacheIpAddress": stnIpRtCacheIpAddress,
       "stnIpRtCacheIpMask": stnIpRtCacheIpMask,
       "stnIpRtCacheNextHop": stnIpRtCacheNextHop,
       "stnIpRtCacheIfIndex": stnIpRtCacheIfIndex,
       "stnIpRtCacheRouteType": stnIpRtCacheRouteType,
       "stnIpRtCacheStatus": stnIpRtCacheStatus,
       "stnIpCircExtTable": stnIpCircExtTable,
       "stnIpCircExtEntry": stnIpCircExtEntry,
       "stnIpCircExtIfIndex": stnIpCircExtIfIndex,
       "stnIpCircExtAdminState": stnIpCircExtAdminState,
       "stnIpCircExtOperState": stnIpCircExtOperState,
       "stnIpCircExtIpAddress": stnIpCircExtIpAddress,
       "stnIpCircExtIpMask": stnIpCircExtIpMask,
       "stnIpCircExtMaxReasm": stnIpCircExtMaxReasm,
       "stnIpCircExtMaxMtu": stnIpCircExtMaxMtu,
       "stnIpCircExtBcastAddr": stnIpCircExtBcastAddr,
       "stnIpDetailsTable": stnIpDetailsTable,
       "stnIpDetailsEntry": stnIpDetailsEntry,
       "stnIpDetailsIndex": stnIpDetailsIndex,
       "stnIpDetailsSource": stnIpDetailsSource,
       "stnIpDetailsDest": stnIpDetailsDest,
       "stnIpDetailsType": stnIpDetailsType,
       "stnIpDetailsTimeStamp": stnIpDetailsTimeStamp,
       "stnIpDetailsHeader": stnIpDetailsHeader,
       "stnIpRoutingVars": stnIpRoutingVars,
       "stnIpMaxRoutingTableSize": stnIpMaxRoutingTableSize,
       "stnIpCurrentRoutingTableSize": stnIpCurrentRoutingTableSize,
       "stnIpTraps": stnIpTraps,
       "stnIpTrapVars": stnIpTrapVars,
       "stnIpNotificationPrefix": stnIpNotificationPrefix,
       "stnIpNotification": stnIpNotification,
       "stnIpRouterRouteLimitExceeded": stnIpRouterRouteLimitExceeded,
       "stnIpEngineRouteLimitExceeded": stnIpEngineRouteLimitExceeded,
       "stnArp": stnArp,
       "stnArpExtTtl": stnArpExtTtl,
       "stnArpExtRcvdRequests": stnArpExtRcvdRequests,
       "stnArpExtRcvdReplies": stnArpExtRcvdReplies,
       "stnArpExtSendRequests": stnArpExtSendRequests,
       "stnArpExtSendReplies": stnArpExtSendReplies,
       "stnArpCircExtTable": stnArpCircExtTable,
       "stnArpCircExtEntry": stnArpCircExtEntry,
       "stnArpCircExtIfIndex": stnArpCircExtIfIndex,
       "stnArpCircExtDoProxy": stnArpCircExtDoProxy,
       "stnArpCircExtDoResp": stnArpCircExtDoResp,
       "stnArpCircExtWanProxy": stnArpCircExtWanProxy,
       "stnRip": stnRip,
       "stnRipExtAdminState": stnRipExtAdminState,
       "stnRipExtUpdateTime": stnRipExtUpdateTime,
       "stnRipCircExtTable": stnRipCircExtTable,
       "stnRipCircExtEntry": stnRipCircExtEntry,
       "stnRipCircExtIfIndex": stnRipCircExtIfIndex,
       "stnRipCircExtTalk": stnRipCircExtTalk,
       "stnRipCircExtListen": stnRipCircExtListen,
       "stnRipCircExtPoison": stnRipCircExtPoison,
       "stnRipDetailsTable": stnRipDetailsTable,
       "stnRipDetailsEntry": stnRipDetailsEntry,
       "stnRipDetailsIndex": stnRipDetailsIndex,
       "stnRipDetailsSource": stnRipDetailsSource,
       "stnRipDetailsDest": stnRipDetailsDest,
       "stnRipDetailsType": stnRipDetailsType,
       "stnRipDetailsTimeStamp": stnRipDetailsTimeStamp,
       "stnRipDetailsHeader": stnRipDetailsHeader,
       "stnOspf": stnOspf,
       "stnOspfRouterLsaCount": stnOspfRouterLsaCount,
       "stnOspfNetworkLsaCount": stnOspfNetworkLsaCount,
       "stnOspfSummaryLsaCount": stnOspfSummaryLsaCount,
       "stnOspfASBRSummaryLsaCount": stnOspfASBRSummaryLsaCount,
       "stnOspfExternLsaCount": stnOspfExternLsaCount,
       "stnOspfMcastGroupLsaCount": stnOspfMcastGroupLsaCount,
       "stnOspfExternT7LsaCount": stnOspfExternT7LsaCount,
       "stnOspfTraps": stnOspfTraps,
       "stnOspfDetailsTable": stnOspfDetailsTable,
       "stnOspfDetailsEntry": stnOspfDetailsEntry,
       "stnOspfDetailsIndex": stnOspfDetailsIndex,
       "stnOspfDetailsPacketType": stnOspfDetailsPacketType,
       "stnOspfDetailsRouterId": stnOspfDetailsRouterId,
       "stnOspfDetailsAreaId": stnOspfDetailsAreaId,
       "stnOspfDetailsErrorType": stnOspfDetailsErrorType,
       "stnOspfDetailsTimeStamp": stnOspfDetailsTimeStamp,
       "stnOspfDetailsHeader": stnOspfDetailsHeader,
       "stnBgp": stnBgp}
)
