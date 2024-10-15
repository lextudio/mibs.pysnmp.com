# SNMP MIB module (CISCO-IPMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPMROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:50 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ipMRouteEntry,
 ipMRouteInterfaceEntry,
 ipMRouteNextHopEntry) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "ipMRouteEntry",
    "ipMRouteInterfaceEntry",
    "ipMRouteNextHopEntry")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpMRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2)
)
ciscoIpMRouteMIB.setRevisions(
        ("2005-03-07 00:00",
         "2000-12-22 00:00",
         "2000-05-15 00:00",
         "1999-02-08 00:00",
         "1996-10-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpMRouteMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpMRouteMIBObjects = _CiscoIpMRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1)
)
_CiscoIpMRoute_ObjectIdentity = ObjectIdentity
ciscoIpMRoute = _CiscoIpMRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1)
)
_CiscoIpMRouteNumberOfEntries_Type = Gauge32
_CiscoIpMRouteNumberOfEntries_Object = MibScalar
ciscoIpMRouteNumberOfEntries = _CiscoIpMRouteNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 1),
    _CiscoIpMRouteNumberOfEntries_Type()
)
ciscoIpMRouteNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteNumberOfEntries.setStatus("current")
_CiscoIpMRouteTable_Object = MibTable
ciscoIpMRouteTable = _CiscoIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteTable.setStatus("current")
_CiscoIpMRouteEntry_Object = MibTableRow
ciscoIpMRouteEntry = _CiscoIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteEntry.setStatus("current")
_CiscoIpMRoutePruneFlag_Type = TruthValue
_CiscoIpMRoutePruneFlag_Object = MibTableColumn
ciscoIpMRoutePruneFlag = _CiscoIpMRoutePruneFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 12),
    _CiscoIpMRoutePruneFlag_Type()
)
ciscoIpMRoutePruneFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRoutePruneFlag.setStatus("current")
_CiscoIpMRouteSparseFlag_Type = TruthValue
_CiscoIpMRouteSparseFlag_Object = MibTableColumn
ciscoIpMRouteSparseFlag = _CiscoIpMRouteSparseFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 13),
    _CiscoIpMRouteSparseFlag_Type()
)
ciscoIpMRouteSparseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteSparseFlag.setStatus("current")
_CiscoIpMRouteConnectedFlag_Type = TruthValue
_CiscoIpMRouteConnectedFlag_Object = MibTableColumn
ciscoIpMRouteConnectedFlag = _CiscoIpMRouteConnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 14),
    _CiscoIpMRouteConnectedFlag_Type()
)
ciscoIpMRouteConnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteConnectedFlag.setStatus("current")
_CiscoIpMRouteLocalFlag_Type = TruthValue
_CiscoIpMRouteLocalFlag_Object = MibTableColumn
ciscoIpMRouteLocalFlag = _CiscoIpMRouteLocalFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 15),
    _CiscoIpMRouteLocalFlag_Type()
)
ciscoIpMRouteLocalFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteLocalFlag.setStatus("current")
_CiscoIpMRouteRegisterFlag_Type = TruthValue
_CiscoIpMRouteRegisterFlag_Object = MibTableColumn
ciscoIpMRouteRegisterFlag = _CiscoIpMRouteRegisterFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 16),
    _CiscoIpMRouteRegisterFlag_Type()
)
ciscoIpMRouteRegisterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteRegisterFlag.setStatus("current")
_CiscoIpMRouteRpFlag_Type = TruthValue
_CiscoIpMRouteRpFlag_Object = MibTableColumn
ciscoIpMRouteRpFlag = _CiscoIpMRouteRpFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 17),
    _CiscoIpMRouteRpFlag_Type()
)
ciscoIpMRouteRpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteRpFlag.setStatus("current")
_CiscoIpMRouteSptFlag_Type = TruthValue
_CiscoIpMRouteSptFlag_Object = MibTableColumn
ciscoIpMRouteSptFlag = _CiscoIpMRouteSptFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 18),
    _CiscoIpMRouteSptFlag_Type()
)
ciscoIpMRouteSptFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteSptFlag.setStatus("current")
_CiscoIpMRouteBps_Type = Gauge32
_CiscoIpMRouteBps_Object = MibTableColumn
ciscoIpMRouteBps = _CiscoIpMRouteBps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 19),
    _CiscoIpMRouteBps_Type()
)
ciscoIpMRouteBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteBps.setStatus("deprecated")


class _CiscoIpMRouteMetric_Type(Integer32):
    """Custom type ciscoIpMRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoIpMRouteMetric_Type.__name__ = "Integer32"
_CiscoIpMRouteMetric_Object = MibTableColumn
ciscoIpMRouteMetric = _CiscoIpMRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 20),
    _CiscoIpMRouteMetric_Type()
)
ciscoIpMRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteMetric.setStatus("deprecated")


class _CiscoIpMRouteMetricPreference_Type(Integer32):
    """Custom type ciscoIpMRouteMetricPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoIpMRouteMetricPreference_Type.__name__ = "Integer32"
_CiscoIpMRouteMetricPreference_Object = MibTableColumn
ciscoIpMRouteMetricPreference = _CiscoIpMRouteMetricPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 21),
    _CiscoIpMRouteMetricPreference_Type()
)
ciscoIpMRouteMetricPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteMetricPreference.setStatus("current")


class _CiscoIpMRouteInLimit_Type(Integer32):
    """Custom type ciscoIpMRouteInLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoIpMRouteInLimit_Type.__name__ = "Integer32"
_CiscoIpMRouteInLimit_Object = MibTableColumn
ciscoIpMRouteInLimit = _CiscoIpMRouteInLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 22),
    _CiscoIpMRouteInLimit_Type()
)
ciscoIpMRouteInLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteInLimit.setStatus("obsolete")
if mibBuilder.loadTexts:
    ciscoIpMRouteInLimit.setUnits("Kbits/second")
_CiscoIpMRouteLastUsed_Type = TimeTicks
_CiscoIpMRouteLastUsed_Object = MibTableColumn
ciscoIpMRouteLastUsed = _CiscoIpMRouteLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 23),
    _CiscoIpMRouteLastUsed_Type()
)
ciscoIpMRouteLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteLastUsed.setStatus("current")
_CiscoIpMRouteInLimit2_Type = Gauge32
_CiscoIpMRouteInLimit2_Object = MibTableColumn
ciscoIpMRouteInLimit2 = _CiscoIpMRouteInLimit2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 24),
    _CiscoIpMRouteInLimit2_Type()
)
ciscoIpMRouteInLimit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteInLimit2.setStatus("current")
if mibBuilder.loadTexts:
    ciscoIpMRouteInLimit2.setUnits("Kbits/second")
_CiscoIpMRouteJoinFlag_Type = TruthValue
_CiscoIpMRouteJoinFlag_Object = MibTableColumn
ciscoIpMRouteJoinFlag = _CiscoIpMRouteJoinFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 25),
    _CiscoIpMRouteJoinFlag_Type()
)
ciscoIpMRouteJoinFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteJoinFlag.setStatus("current")
_CiscoIpMRouteMsdpFlag_Type = TruthValue
_CiscoIpMRouteMsdpFlag_Object = MibTableColumn
ciscoIpMRouteMsdpFlag = _CiscoIpMRouteMsdpFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 26),
    _CiscoIpMRouteMsdpFlag_Type()
)
ciscoIpMRouteMsdpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteMsdpFlag.setStatus("current")
_CiscoIpMRouteProxyJoinFlag_Type = TruthValue
_CiscoIpMRouteProxyJoinFlag_Object = MibTableColumn
ciscoIpMRouteProxyJoinFlag = _CiscoIpMRouteProxyJoinFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 27),
    _CiscoIpMRouteProxyJoinFlag_Type()
)
ciscoIpMRouteProxyJoinFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteProxyJoinFlag.setStatus("current")
_CiscoIpMRoutePkts_Type = Counter64
_CiscoIpMRoutePkts_Object = MibTableColumn
ciscoIpMRoutePkts = _CiscoIpMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 28),
    _CiscoIpMRoutePkts_Type()
)
ciscoIpMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRoutePkts.setStatus("current")
_CiscoIpMRouteDifferentInIfPkts_Type = Counter64
_CiscoIpMRouteDifferentInIfPkts_Object = MibTableColumn
ciscoIpMRouteDifferentInIfPkts = _CiscoIpMRouteDifferentInIfPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 29),
    _CiscoIpMRouteDifferentInIfPkts_Type()
)
ciscoIpMRouteDifferentInIfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteDifferentInIfPkts.setStatus("current")
_CiscoIpMRouteOctets_Type = Counter64
_CiscoIpMRouteOctets_Object = MibTableColumn
ciscoIpMRouteOctets = _CiscoIpMRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 30),
    _CiscoIpMRouteOctets_Type()
)
ciscoIpMRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteOctets.setStatus("current")
_CiscoIpMRouteBps2_Type = CounterBasedGauge64
_CiscoIpMRouteBps2_Object = MibTableColumn
ciscoIpMRouteBps2 = _CiscoIpMRouteBps2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 31),
    _CiscoIpMRouteBps2_Type()
)
ciscoIpMRouteBps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteBps2.setStatus("current")
_CiscoIpMRouteMetric2_Type = Unsigned32
_CiscoIpMRouteMetric2_Object = MibTableColumn
ciscoIpMRouteMetric2 = _CiscoIpMRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 2, 1, 32),
    _CiscoIpMRouteMetric2_Type()
)
ciscoIpMRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteMetric2.setStatus("current")
_CiscoIpMRouteNextHopTable_Object = MibTable
ciscoIpMRouteNextHopTable = _CiscoIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteNextHopTable.setStatus("current")
_CiscoIpMRouteNextHopEntry_Object = MibTableRow
ciscoIpMRouteNextHopEntry = _CiscoIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteNextHopEntry.setStatus("current")
_CiscoIpMRouteNextHopOutLimit_Type = Gauge32
_CiscoIpMRouteNextHopOutLimit_Object = MibTableColumn
ciscoIpMRouteNextHopOutLimit = _CiscoIpMRouteNextHopOutLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1, 9),
    _CiscoIpMRouteNextHopOutLimit_Type()
)
ciscoIpMRouteNextHopOutLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteNextHopOutLimit.setStatus("current")
if mibBuilder.loadTexts:
    ciscoIpMRouteNextHopOutLimit.setUnits("Kbits/second")
_CiscoIpMRouteNextHopMacHdr_Type = OctetString
_CiscoIpMRouteNextHopMacHdr_Object = MibTableColumn
ciscoIpMRouteNextHopMacHdr = _CiscoIpMRouteNextHopMacHdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1, 10),
    _CiscoIpMRouteNextHopMacHdr_Type()
)
ciscoIpMRouteNextHopMacHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteNextHopMacHdr.setStatus("current")
_CiscoIpMRouteNextHopPkts_Type = Counter64
_CiscoIpMRouteNextHopPkts_Object = MibTableColumn
ciscoIpMRouteNextHopPkts = _CiscoIpMRouteNextHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 3, 1, 11),
    _CiscoIpMRouteNextHopPkts_Type()
)
ciscoIpMRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteNextHopPkts.setStatus("current")
_CiscoIpMRouteHeartBeatTable_Object = MibTable
ciscoIpMRouteHeartBeatTable = _CiscoIpMRouteHeartBeatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatTable.setStatus("current")
_CiscoIpMRouteHeartBeatEntry_Object = MibTableRow
ciscoIpMRouteHeartBeatEntry = _CiscoIpMRouteHeartBeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1)
)
ciscoIpMRouteHeartBeatEntry.setIndexNames(
    (0, "CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatGroupAddr"),
)
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatEntry.setStatus("current")
_CiscoIpMRouteHeartBeatGroupAddr_Type = IpAddress
_CiscoIpMRouteHeartBeatGroupAddr_Object = MibTableColumn
ciscoIpMRouteHeartBeatGroupAddr = _CiscoIpMRouteHeartBeatGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 1),
    _CiscoIpMRouteHeartBeatGroupAddr_Type()
)
ciscoIpMRouteHeartBeatGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatGroupAddr.setStatus("current")
_CiscoIpMRouteHeartBeatSourceAddr_Type = IpAddress
_CiscoIpMRouteHeartBeatSourceAddr_Object = MibTableColumn
ciscoIpMRouteHeartBeatSourceAddr = _CiscoIpMRouteHeartBeatSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 2),
    _CiscoIpMRouteHeartBeatSourceAddr_Type()
)
ciscoIpMRouteHeartBeatSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatSourceAddr.setStatus("current")


class _CiscoIpMRouteHeartBeatInterval_Type(Integer32):
    """Custom type ciscoIpMRouteHeartBeatInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_CiscoIpMRouteHeartBeatInterval_Type.__name__ = "Integer32"
_CiscoIpMRouteHeartBeatInterval_Object = MibTableColumn
ciscoIpMRouteHeartBeatInterval = _CiscoIpMRouteHeartBeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 3),
    _CiscoIpMRouteHeartBeatInterval_Type()
)
ciscoIpMRouteHeartBeatInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatInterval.setUnits("seconds")


class _CiscoIpMRouteHeartBeatWindowSize_Type(Integer32):
    """Custom type ciscoIpMRouteHeartBeatWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoIpMRouteHeartBeatWindowSize_Type.__name__ = "Integer32"
_CiscoIpMRouteHeartBeatWindowSize_Object = MibTableColumn
ciscoIpMRouteHeartBeatWindowSize = _CiscoIpMRouteHeartBeatWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 4),
    _CiscoIpMRouteHeartBeatWindowSize_Type()
)
ciscoIpMRouteHeartBeatWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatWindowSize.setStatus("current")
_CiscoIpMRouteHeartBeatCount_Type = Gauge32
_CiscoIpMRouteHeartBeatCount_Object = MibTableColumn
ciscoIpMRouteHeartBeatCount = _CiscoIpMRouteHeartBeatCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 5),
    _CiscoIpMRouteHeartBeatCount_Type()
)
ciscoIpMRouteHeartBeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatCount.setStatus("current")


class _CiscoIpMRouteHeartBeatMinimum_Type(Integer32):
    """Custom type ciscoIpMRouteHeartBeatMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoIpMRouteHeartBeatMinimum_Type.__name__ = "Integer32"
_CiscoIpMRouteHeartBeatMinimum_Object = MibTableColumn
ciscoIpMRouteHeartBeatMinimum = _CiscoIpMRouteHeartBeatMinimum_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 6),
    _CiscoIpMRouteHeartBeatMinimum_Type()
)
ciscoIpMRouteHeartBeatMinimum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatMinimum.setStatus("current")
_CiscoIpMRouteHeartBeatAlertTime_Type = TimeStamp
_CiscoIpMRouteHeartBeatAlertTime_Object = MibTableColumn
ciscoIpMRouteHeartBeatAlertTime = _CiscoIpMRouteHeartBeatAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 7),
    _CiscoIpMRouteHeartBeatAlertTime_Type()
)
ciscoIpMRouteHeartBeatAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatAlertTime.setStatus("current")
_CiscoIpMRouteHeartBeatStatus_Type = RowStatus
_CiscoIpMRouteHeartBeatStatus_Object = MibTableColumn
ciscoIpMRouteHeartBeatStatus = _CiscoIpMRouteHeartBeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 4, 1, 8),
    _CiscoIpMRouteHeartBeatStatus_Type()
)
ciscoIpMRouteHeartBeatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoIpMRouteHeartBeatStatus.setStatus("current")
_CiscoIpMRouteInterfaceTable_Object = MibTable
ciscoIpMRouteInterfaceTable = _CiscoIpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteInterfaceTable.setStatus("current")
_CiscoIpMRouteInterfaceEntry_Object = MibTableRow
ciscoIpMRouteInterfaceEntry = _CiscoIpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteInterfaceEntry.setStatus("current")
_CiscoIpMRouteIfInMcastOctets_Type = Counter64
_CiscoIpMRouteIfInMcastOctets_Object = MibTableColumn
ciscoIpMRouteIfInMcastOctets = _CiscoIpMRouteIfInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 1),
    _CiscoIpMRouteIfInMcastOctets_Type()
)
ciscoIpMRouteIfInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteIfInMcastOctets.setStatus("current")
_CiscoIpMRouteIfOutMcastOctets_Type = Counter64
_CiscoIpMRouteIfOutMcastOctets_Object = MibTableColumn
ciscoIpMRouteIfOutMcastOctets = _CiscoIpMRouteIfOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 2),
    _CiscoIpMRouteIfOutMcastOctets_Type()
)
ciscoIpMRouteIfOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteIfOutMcastOctets.setStatus("current")
_CiscoIpMRouteIfInMcastPkts_Type = Counter32
_CiscoIpMRouteIfInMcastPkts_Object = MibTableColumn
ciscoIpMRouteIfInMcastPkts = _CiscoIpMRouteIfInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 3),
    _CiscoIpMRouteIfInMcastPkts_Type()
)
ciscoIpMRouteIfInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteIfInMcastPkts.setStatus("current")
_CiscoIpMRouteIfHCInMcastPkts_Type = Counter64
_CiscoIpMRouteIfHCInMcastPkts_Object = MibTableColumn
ciscoIpMRouteIfHCInMcastPkts = _CiscoIpMRouteIfHCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 4),
    _CiscoIpMRouteIfHCInMcastPkts_Type()
)
ciscoIpMRouteIfHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteIfHCInMcastPkts.setStatus("current")
_CiscoIpMRouteIfOutMcastPkts_Type = Counter32
_CiscoIpMRouteIfOutMcastPkts_Object = MibTableColumn
ciscoIpMRouteIfOutMcastPkts = _CiscoIpMRouteIfOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 5),
    _CiscoIpMRouteIfOutMcastPkts_Type()
)
ciscoIpMRouteIfOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteIfOutMcastPkts.setStatus("current")
_CiscoIpMRouteIfHCOutMcastPkts_Type = Counter64
_CiscoIpMRouteIfHCOutMcastPkts_Object = MibTableColumn
ciscoIpMRouteIfHCOutMcastPkts = _CiscoIpMRouteIfHCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 1, 1, 5, 1, 6),
    _CiscoIpMRouteIfHCOutMcastPkts_Type()
)
ciscoIpMRouteIfHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIpMRouteIfHCOutMcastPkts.setStatus("current")
_CiscoIpMRouteMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIpMRouteMIBConformance = _CiscoIpMRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2)
)
_CiscoIpMRouteMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpMRouteMIBCompliances = _CiscoIpMRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1)
)
_CiscoIpMRouteMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpMRouteMIBGroups = _CiscoIpMRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2)
)
_CiscoIpMRouteNotifications_ObjectIdentity = ObjectIdentity
ciscoIpMRouteNotifications = _CiscoIpMRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 3)
)
_CiscoIpMRouteMissingHeartBeatsNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoIpMRouteMissingHeartBeatsNotificationPrefix = _CiscoIpMRouteMissingHeartBeatsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 3, 1)
)
_CiscoIpMRouteMissingHeartBeatsNotifications_ObjectIdentity = ObjectIdentity
ciscoIpMRouteMissingHeartBeatsNotifications = _CiscoIpMRouteMissingHeartBeatsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 3, 1, 0)
)
ipMRouteEntry.registerAugmentions(
    ("CISCO-IPMROUTE-MIB",
     "ciscoIpMRouteEntry")
)
ciscoIpMRouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())
ipMRouteNextHopEntry.registerAugmentions(
    ("CISCO-IPMROUTE-MIB",
     "ciscoIpMRouteNextHopEntry")
)
ciscoIpMRouteNextHopEntry.setIndexNames(*ipMRouteNextHopEntry.getIndexNames())
ipMRouteInterfaceEntry.registerAugmentions(
    ("CISCO-IPMROUTE-MIB",
     "ciscoIpMRouteInterfaceEntry")
)
ciscoIpMRouteInterfaceEntry.setIndexNames(*ipMRouteInterfaceEntry.getIndexNames())

# Managed Objects groups

ciscoIpMRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 1)
)
ciscoIpMRouteMIBGroup.setObjects(
      *(("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"))
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBGroup.setStatus("obsolete")

ciscoIpMRouteMIBGroupV11R01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 2)
)
ciscoIpMRouteMIBGroupV11R01.setObjects(
      *(("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit2"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteJoinFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMsdpFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteProxyJoinFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"))
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBGroupV11R01.setStatus("deprecated")

ciscoIpMRouteMIBHeartBeatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 3)
)
ciscoIpMRouteMIBHeartBeatGroup.setObjects(
      *(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatSourceAddr"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatInterval"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatWindowSize"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatCount"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatMinimum"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatAlertTime"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBHeartBeatGroup.setStatus("current")

ciscoIpMRouteMIBGroupV12R00S = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 4)
)
ciscoIpMRouteMIBGroupV12R00S.setObjects(
      *(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNumberOfEntries"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit2"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteJoinFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMsdpFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteProxyJoinFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteDifferentInIfPkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteOctets"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps2"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric2"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopPkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfInMcastOctets"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfOutMcastOctets"))
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBGroupV12R00S.setStatus("deprecated")

ciscoIpMRouteMIBGroupV12R28S = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 6)
)
ciscoIpMRouteMIBGroupV12R28S.setObjects(
      *(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNumberOfEntries"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePruneFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSparseFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteConnectedFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLocalFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRegisterFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteRpFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteSptFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetricPreference"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteLastUsed"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteInLimit2"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteJoinFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMsdpFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteProxyJoinFlag"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRoutePkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteDifferentInIfPkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteOctets"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteBps2"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMetric2"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopOutLimit"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopMacHdr"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteNextHopPkts"))
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBGroupV12R28S.setStatus("current")

ciscoIpMRouteMIBIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 7)
)
ciscoIpMRouteMIBIfGroup.setObjects(
      *(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfInMcastOctets"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfOutMcastOctets"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfInMcastPkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfHCInMcastPkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfOutMcastPkts"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteIfHCOutMcastPkts"))
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBIfGroup.setStatus("current")


# Notification objects

ciscoIpMRouteMissingHeartBeats = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 3, 1, 0, 1)
)
ciscoIpMRouteMissingHeartBeats.setObjects(
      *(("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatSourceAddr"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatInterval"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatWindowSize"),
        ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteHeartBeatCount"))
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMissingHeartBeats.setStatus(
        "current"
    )


# Notifications groups

ciscoIpMRouteMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 2, 5)
)
ciscoIpMRouteMIBNotifGroup.setObjects(
    ("CISCO-IPMROUTE-MIB", "ciscoIpMRouteMissingHeartBeats")
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIpMRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBCompliance.setStatus(
        "obsolete"
    )

ciscoIpMRouteMIBComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBComplianceV11R01.setStatus(
        "deprecated"
    )

ciscoIpMRouteMIBComplianceV12R00S = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBComplianceV12R00S.setStatus(
        "deprecated"
    )

ciscoIpMRouteMIBComplianceV12R28S = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoIpMRouteMIBComplianceV12R28S.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPMROUTE-MIB",
    **{"ciscoIpMRouteMIB": ciscoIpMRouteMIB,
       "ciscoIpMRouteMIBObjects": ciscoIpMRouteMIBObjects,
       "ciscoIpMRoute": ciscoIpMRoute,
       "ciscoIpMRouteNumberOfEntries": ciscoIpMRouteNumberOfEntries,
       "ciscoIpMRouteTable": ciscoIpMRouteTable,
       "ciscoIpMRouteEntry": ciscoIpMRouteEntry,
       "ciscoIpMRoutePruneFlag": ciscoIpMRoutePruneFlag,
       "ciscoIpMRouteSparseFlag": ciscoIpMRouteSparseFlag,
       "ciscoIpMRouteConnectedFlag": ciscoIpMRouteConnectedFlag,
       "ciscoIpMRouteLocalFlag": ciscoIpMRouteLocalFlag,
       "ciscoIpMRouteRegisterFlag": ciscoIpMRouteRegisterFlag,
       "ciscoIpMRouteRpFlag": ciscoIpMRouteRpFlag,
       "ciscoIpMRouteSptFlag": ciscoIpMRouteSptFlag,
       "ciscoIpMRouteBps": ciscoIpMRouteBps,
       "ciscoIpMRouteMetric": ciscoIpMRouteMetric,
       "ciscoIpMRouteMetricPreference": ciscoIpMRouteMetricPreference,
       "ciscoIpMRouteInLimit": ciscoIpMRouteInLimit,
       "ciscoIpMRouteLastUsed": ciscoIpMRouteLastUsed,
       "ciscoIpMRouteInLimit2": ciscoIpMRouteInLimit2,
       "ciscoIpMRouteJoinFlag": ciscoIpMRouteJoinFlag,
       "ciscoIpMRouteMsdpFlag": ciscoIpMRouteMsdpFlag,
       "ciscoIpMRouteProxyJoinFlag": ciscoIpMRouteProxyJoinFlag,
       "ciscoIpMRoutePkts": ciscoIpMRoutePkts,
       "ciscoIpMRouteDifferentInIfPkts": ciscoIpMRouteDifferentInIfPkts,
       "ciscoIpMRouteOctets": ciscoIpMRouteOctets,
       "ciscoIpMRouteBps2": ciscoIpMRouteBps2,
       "ciscoIpMRouteMetric2": ciscoIpMRouteMetric2,
       "ciscoIpMRouteNextHopTable": ciscoIpMRouteNextHopTable,
       "ciscoIpMRouteNextHopEntry": ciscoIpMRouteNextHopEntry,
       "ciscoIpMRouteNextHopOutLimit": ciscoIpMRouteNextHopOutLimit,
       "ciscoIpMRouteNextHopMacHdr": ciscoIpMRouteNextHopMacHdr,
       "ciscoIpMRouteNextHopPkts": ciscoIpMRouteNextHopPkts,
       "ciscoIpMRouteHeartBeatTable": ciscoIpMRouteHeartBeatTable,
       "ciscoIpMRouteHeartBeatEntry": ciscoIpMRouteHeartBeatEntry,
       "ciscoIpMRouteHeartBeatGroupAddr": ciscoIpMRouteHeartBeatGroupAddr,
       "ciscoIpMRouteHeartBeatSourceAddr": ciscoIpMRouteHeartBeatSourceAddr,
       "ciscoIpMRouteHeartBeatInterval": ciscoIpMRouteHeartBeatInterval,
       "ciscoIpMRouteHeartBeatWindowSize": ciscoIpMRouteHeartBeatWindowSize,
       "ciscoIpMRouteHeartBeatCount": ciscoIpMRouteHeartBeatCount,
       "ciscoIpMRouteHeartBeatMinimum": ciscoIpMRouteHeartBeatMinimum,
       "ciscoIpMRouteHeartBeatAlertTime": ciscoIpMRouteHeartBeatAlertTime,
       "ciscoIpMRouteHeartBeatStatus": ciscoIpMRouteHeartBeatStatus,
       "ciscoIpMRouteInterfaceTable": ciscoIpMRouteInterfaceTable,
       "ciscoIpMRouteInterfaceEntry": ciscoIpMRouteInterfaceEntry,
       "ciscoIpMRouteIfInMcastOctets": ciscoIpMRouteIfInMcastOctets,
       "ciscoIpMRouteIfOutMcastOctets": ciscoIpMRouteIfOutMcastOctets,
       "ciscoIpMRouteIfInMcastPkts": ciscoIpMRouteIfInMcastPkts,
       "ciscoIpMRouteIfHCInMcastPkts": ciscoIpMRouteIfHCInMcastPkts,
       "ciscoIpMRouteIfOutMcastPkts": ciscoIpMRouteIfOutMcastPkts,
       "ciscoIpMRouteIfHCOutMcastPkts": ciscoIpMRouteIfHCOutMcastPkts,
       "ciscoIpMRouteMIBConformance": ciscoIpMRouteMIBConformance,
       "ciscoIpMRouteMIBCompliances": ciscoIpMRouteMIBCompliances,
       "ciscoIpMRouteMIBCompliance": ciscoIpMRouteMIBCompliance,
       "ciscoIpMRouteMIBComplianceV11R01": ciscoIpMRouteMIBComplianceV11R01,
       "ciscoIpMRouteMIBComplianceV12R00S": ciscoIpMRouteMIBComplianceV12R00S,
       "ciscoIpMRouteMIBComplianceV12R28S": ciscoIpMRouteMIBComplianceV12R28S,
       "ciscoIpMRouteMIBGroups": ciscoIpMRouteMIBGroups,
       "ciscoIpMRouteMIBGroup": ciscoIpMRouteMIBGroup,
       "ciscoIpMRouteMIBGroupV11R01": ciscoIpMRouteMIBGroupV11R01,
       "ciscoIpMRouteMIBHeartBeatGroup": ciscoIpMRouteMIBHeartBeatGroup,
       "ciscoIpMRouteMIBGroupV12R00S": ciscoIpMRouteMIBGroupV12R00S,
       "ciscoIpMRouteMIBNotifGroup": ciscoIpMRouteMIBNotifGroup,
       "ciscoIpMRouteMIBGroupV12R28S": ciscoIpMRouteMIBGroupV12R28S,
       "ciscoIpMRouteMIBIfGroup": ciscoIpMRouteMIBIfGroup,
       "ciscoIpMRouteNotifications": ciscoIpMRouteNotifications,
       "ciscoIpMRouteMissingHeartBeatsNotificationPrefix": ciscoIpMRouteMissingHeartBeatsNotificationPrefix,
       "ciscoIpMRouteMissingHeartBeatsNotifications": ciscoIpMRouteMissingHeartBeatsNotifications,
       "ciscoIpMRouteMissingHeartBeats": ciscoIpMRouteMissingHeartBeats}
)
