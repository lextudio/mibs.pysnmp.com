# SNMP MIB module (CISCO-SERVICE-CONTROL-TP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SERVICE-CONTROL-TP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:09 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoServiceControlTpStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 634)
)
ciscoServiceControlTpStatsMIB.setRevisions(
        ("2007-07-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSCTpStatsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSCTpStatsMIBNotifs = _CiscoSCTpStatsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 0)
)
_CiscoSCTpStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSCTpStatsMIBObjects = _CiscoSCTpStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1)
)
_CscTpTable_Object = MibTable
cscTpTable = _CscTpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1)
)
if mibBuilder.loadTexts:
    cscTpTable.setStatus("current")
_CscTpEntry_Object = MibTableRow
cscTpEntry = _CscTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1)
)
cscTpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cscTpEntry.setStatus("current")
_CscTpTotalHandledPackets_Type = Counter64
_CscTpTotalHandledPackets_Object = MibTableColumn
cscTpTotalHandledPackets = _CscTpTotalHandledPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 1),
    _CscTpTotalHandledPackets_Type()
)
cscTpTotalHandledPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalHandledPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalHandledPackets.setUnits("packets")
_CscTpTotalHandledFlows_Type = Counter64
_CscTpTotalHandledFlows_Object = MibTableColumn
cscTpTotalHandledFlows = _CscTpTotalHandledFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 2),
    _CscTpTotalHandledFlows_Type()
)
cscTpTotalHandledFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalHandledFlows.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalHandledFlows.setUnits("flows")
_CscTpActiveFlows_Type = Gauge32
_CscTpActiveFlows_Object = MibTableColumn
cscTpActiveFlows = _CscTpActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 3),
    _CscTpActiveFlows_Type()
)
cscTpActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpActiveFlows.setStatus("current")
if mibBuilder.loadTexts:
    cscTpActiveFlows.setUnits("flows")
_CscTpTcpActiveFlows_Type = Gauge32
_CscTpTcpActiveFlows_Object = MibTableColumn
cscTpTcpActiveFlows = _CscTpTcpActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 4),
    _CscTpTcpActiveFlows_Type()
)
cscTpTcpActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTcpActiveFlows.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTcpActiveFlows.setUnits("flows")
_CscTpUdpActiveFlows_Type = Gauge32
_CscTpUdpActiveFlows_Object = MibTableColumn
cscTpUdpActiveFlows = _CscTpUdpActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 5),
    _CscTpUdpActiveFlows_Type()
)
cscTpUdpActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpUdpActiveFlows.setStatus("current")
if mibBuilder.loadTexts:
    cscTpUdpActiveFlows.setUnits("flows")
_CscTpTotalBlockedPackets_Type = Counter32
_CscTpTotalBlockedPackets_Object = MibTableColumn
cscTpTotalBlockedPackets = _CscTpTotalBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 6),
    _CscTpTotalBlockedPackets_Type()
)
cscTpTotalBlockedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalBlockedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalBlockedPackets.setUnits("packets")
_CscTpTotalBlockedFlows_Type = Counter32
_CscTpTotalBlockedFlows_Object = MibTableColumn
cscTpTotalBlockedFlows = _CscTpTotalBlockedFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 7),
    _CscTpTotalBlockedFlows_Type()
)
cscTpTotalBlockedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalBlockedFlows.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalBlockedFlows.setUnits("flows")
_CscTpTotalBandwidthDiscardedPackets_Type = Counter32
_CscTpTotalBandwidthDiscardedPackets_Object = MibTableColumn
cscTpTotalBandwidthDiscardedPackets = _CscTpTotalBandwidthDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 8),
    _CscTpTotalBandwidthDiscardedPackets_Type()
)
cscTpTotalBandwidthDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalBandwidthDiscardedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalBandwidthDiscardedPackets.setUnits("packets")
_CscTpTotalWredDiscardedPackets_Type = Counter32
_CscTpTotalWredDiscardedPackets_Object = MibTableColumn
cscTpTotalWredDiscardedPackets = _CscTpTotalWredDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 9),
    _CscTpTotalWredDiscardedPackets_Type()
)
cscTpTotalWredDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalWredDiscardedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalWredDiscardedPackets.setUnits("packets")
_CscTpTotalFragments_Type = Counter64
_CscTpTotalFragments_Object = MibTableColumn
cscTpTotalFragments = _CscTpTotalFragments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 10),
    _CscTpTotalFragments_Type()
)
cscTpTotalFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalFragments.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalFragments.setUnits("packets")
_CscTpTotalNonIpPackets_Type = Counter64
_CscTpTotalNonIpPackets_Object = MibTableColumn
cscTpTotalNonIpPackets = _CscTpTotalNonIpPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 11),
    _CscTpTotalNonIpPackets_Type()
)
cscTpTotalNonIpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalNonIpPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalNonIpPackets.setUnits("packets")
_CscTpTotalIpChecksumErrPackets_Type = Counter32
_CscTpTotalIpChecksumErrPackets_Object = MibTableColumn
cscTpTotalIpChecksumErrPackets = _CscTpTotalIpChecksumErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 12),
    _CscTpTotalIpChecksumErrPackets_Type()
)
cscTpTotalIpChecksumErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalIpChecksumErrPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalIpChecksumErrPackets.setUnits("num-of-packets")
_CscTpTotalIpLengthErrPackets_Type = Counter32
_CscTpTotalIpLengthErrPackets_Object = MibTableColumn
cscTpTotalIpLengthErrPackets = _CscTpTotalIpLengthErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 13),
    _CscTpTotalIpLengthErrPackets_Type()
)
cscTpTotalIpLengthErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalIpLengthErrPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalIpLengthErrPackets.setUnits("packets")
_CscTpTotalIpBroadcastPackets_Type = Counter64
_CscTpTotalIpBroadcastPackets_Object = MibTableColumn
cscTpTotalIpBroadcastPackets = _CscTpTotalIpBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 14),
    _CscTpTotalIpBroadcastPackets_Type()
)
cscTpTotalIpBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalIpBroadcastPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalIpBroadcastPackets.setUnits("packets")
_CscTpTotalTTLErrPackets_Type = Counter32
_CscTpTotalTTLErrPackets_Object = MibTableColumn
cscTpTotalTTLErrPackets = _CscTpTotalTTLErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 15),
    _CscTpTotalTTLErrPackets_Type()
)
cscTpTotalTTLErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalTTLErrPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalTTLErrPackets.setUnits("packets")
_CscTpTotalTcpUdpChksumErrPackets_Type = Counter32
_CscTpTotalTcpUdpChksumErrPackets_Object = MibTableColumn
cscTpTotalTcpUdpChksumErrPackets = _CscTpTotalTcpUdpChksumErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 16),
    _CscTpTotalTcpUdpChksumErrPackets_Type()
)
cscTpTotalTcpUdpChksumErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpTotalTcpUdpChksumErrPackets.setStatus("current")
if mibBuilder.loadTexts:
    cscTpTotalTcpUdpChksumErrPackets.setUnits("packets")
_CscTpHandledPacketsRate_Type = Gauge32
_CscTpHandledPacketsRate_Object = MibTableColumn
cscTpHandledPacketsRate = _CscTpHandledPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 17),
    _CscTpHandledPacketsRate_Type()
)
cscTpHandledPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpHandledPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    cscTpHandledPacketsRate.setUnits("packets per second")
_CscTpHandledFlowsRate_Type = Gauge32
_CscTpHandledFlowsRate_Object = MibTableColumn
cscTpHandledFlowsRate = _CscTpHandledFlowsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 18),
    _CscTpHandledFlowsRate_Type()
)
cscTpHandledFlowsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpHandledFlowsRate.setStatus("current")
if mibBuilder.loadTexts:
    cscTpHandledFlowsRate.setUnits("flows per second")


class _CscTpFlowsCapacityUtilization_Type(Unsigned32):
    """Custom type cscTpFlowsCapacityUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CscTpFlowsCapacityUtilization_Type.__name__ = "Unsigned32"
_CscTpFlowsCapacityUtilization_Object = MibTableColumn
cscTpFlowsCapacityUtilization = _CscTpFlowsCapacityUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 19),
    _CscTpFlowsCapacityUtilization_Type()
)
cscTpFlowsCapacityUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpFlowsCapacityUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cscTpFlowsCapacityUtilization.setUnits("percent")


class _CscTpServiceLoss_Type(Unsigned32):
    """Custom type cscTpServiceLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CscTpServiceLoss_Type.__name__ = "Unsigned32"
_CscTpServiceLoss_Object = MibTableColumn
cscTpServiceLoss = _CscTpServiceLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 1, 1, 20),
    _CscTpServiceLoss_Type()
)
cscTpServiceLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpServiceLoss.setStatus("current")
if mibBuilder.loadTexts:
    cscTpServiceLoss.setUnits("0.001 percent")
_CscTpStatsTrafficCountersTable_Object = MibTable
cscTpStatsTrafficCountersTable = _CscTpStatsTrafficCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 2)
)
if mibBuilder.loadTexts:
    cscTpStatsTrafficCountersTable.setStatus("current")
_CscTpStatsTrafficCountersEntry_Object = MibTableRow
cscTpStatsTrafficCountersEntry = _CscTpStatsTrafficCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 2, 1)
)
cscTpStatsTrafficCountersEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpStatsTrafficCounterIndex"),
)
if mibBuilder.loadTexts:
    cscTpStatsTrafficCountersEntry.setStatus("current")


class _CscTpStatsTrafficCounterIndex_Type(Unsigned32):
    """Custom type cscTpStatsTrafficCounterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CscTpStatsTrafficCounterIndex_Type.__name__ = "Unsigned32"
_CscTpStatsTrafficCounterIndex_Object = MibTableColumn
cscTpStatsTrafficCounterIndex = _CscTpStatsTrafficCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 2, 1, 1),
    _CscTpStatsTrafficCounterIndex_Type()
)
cscTpStatsTrafficCounterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cscTpStatsTrafficCounterIndex.setStatus("current")
_CscTpStatsTrafficCounterName_Type = SnmpAdminString
_CscTpStatsTrafficCounterName_Object = MibTableColumn
cscTpStatsTrafficCounterName = _CscTpStatsTrafficCounterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 2, 1, 2),
    _CscTpStatsTrafficCounterName_Type()
)
cscTpStatsTrafficCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpStatsTrafficCounterName.setStatus("current")
_CscTpStatsTrafficCounterValue_Type = Counter64
_CscTpStatsTrafficCounterValue_Object = MibTableColumn
cscTpStatsTrafficCounterValue = _CscTpStatsTrafficCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 2, 1, 3),
    _CscTpStatsTrafficCounterValue_Type()
)
cscTpStatsTrafficCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpStatsTrafficCounterValue.setStatus("current")


class _CscTpStatsTrafficCounterType_Type(Integer32):
    """Custom type cscTpStatsTrafficCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 2),
          ("other", 1),
          ("packets", 3))
    )


_CscTpStatsTrafficCounterType_Type.__name__ = "Integer32"
_CscTpStatsTrafficCounterType_Object = MibTableColumn
cscTpStatsTrafficCounterType = _CscTpStatsTrafficCounterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 2, 1, 4),
    _CscTpStatsTrafficCounterType_Type()
)
cscTpStatsTrafficCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpStatsTrafficCounterType.setStatus("current")
_CscTpCounterDiscontinuityTime_Type = TimeStamp
_CscTpCounterDiscontinuityTime_Object = MibScalar
cscTpCounterDiscontinuityTime = _CscTpCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 1, 3),
    _CscTpCounterDiscontinuityTime_Type()
)
cscTpCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscTpCounterDiscontinuityTime.setStatus("current")
_CiscoSCTpStatsMIBConform_ObjectIdentity = ObjectIdentity
ciscoSCTpStatsMIBConform = _CiscoSCTpStatsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 2)
)
_CscTpStatsMIBCompliances_ObjectIdentity = ObjectIdentity
cscTpStatsMIBCompliances = _CscTpStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 2, 1)
)
_CscTpStatsMIBGroups_ObjectIdentity = ObjectIdentity
cscTpStatsMIBGroups = _CscTpStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 2, 2)
)

# Managed Objects groups

cscTpStatsMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 2, 2, 1)
)
cscTpStatsMIBObjectGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalHandledPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalHandledFlows"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpActiveFlows"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTcpActiveFlows"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpUdpActiveFlows"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalBlockedPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalBlockedFlows"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalBandwidthDiscardedPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalWredDiscardedPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalFragments"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalNonIpPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalIpChecksumErrPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalIpLengthErrPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalIpBroadcastPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalTTLErrPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpTotalTcpUdpChksumErrPackets"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpHandledPacketsRate"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpHandledFlowsRate"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpFlowsCapacityUtilization"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpServiceLoss"))
)
if mibBuilder.loadTexts:
    cscTpStatsMIBObjectGroup.setStatus("current")

cscTpStatsMIBTrafficCntrsObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 2, 2, 2)
)
cscTpStatsMIBTrafficCntrsObjGroup.setObjects(
      *(("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpStatsTrafficCounterValue"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpStatsTrafficCounterName"),
        ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpStatsTrafficCounterType"))
)
if mibBuilder.loadTexts:
    cscTpStatsMIBTrafficCntrsObjGroup.setStatus("current")

cscTpCounterDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 2, 2, 3)
)
cscTpCounterDiscontinuityGroup.setObjects(
    ("CISCO-SERVICE-CONTROL-TP-STATS-MIB", "cscTpCounterDiscontinuityTime")
)
if mibBuilder.loadTexts:
    cscTpCounterDiscontinuityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cscTpStatsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 634, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cscTpStatsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SERVICE-CONTROL-TP-STATS-MIB",
    **{"ciscoServiceControlTpStatsMIB": ciscoServiceControlTpStatsMIB,
       "ciscoSCTpStatsMIBNotifs": ciscoSCTpStatsMIBNotifs,
       "ciscoSCTpStatsMIBObjects": ciscoSCTpStatsMIBObjects,
       "cscTpTable": cscTpTable,
       "cscTpEntry": cscTpEntry,
       "cscTpTotalHandledPackets": cscTpTotalHandledPackets,
       "cscTpTotalHandledFlows": cscTpTotalHandledFlows,
       "cscTpActiveFlows": cscTpActiveFlows,
       "cscTpTcpActiveFlows": cscTpTcpActiveFlows,
       "cscTpUdpActiveFlows": cscTpUdpActiveFlows,
       "cscTpTotalBlockedPackets": cscTpTotalBlockedPackets,
       "cscTpTotalBlockedFlows": cscTpTotalBlockedFlows,
       "cscTpTotalBandwidthDiscardedPackets": cscTpTotalBandwidthDiscardedPackets,
       "cscTpTotalWredDiscardedPackets": cscTpTotalWredDiscardedPackets,
       "cscTpTotalFragments": cscTpTotalFragments,
       "cscTpTotalNonIpPackets": cscTpTotalNonIpPackets,
       "cscTpTotalIpChecksumErrPackets": cscTpTotalIpChecksumErrPackets,
       "cscTpTotalIpLengthErrPackets": cscTpTotalIpLengthErrPackets,
       "cscTpTotalIpBroadcastPackets": cscTpTotalIpBroadcastPackets,
       "cscTpTotalTTLErrPackets": cscTpTotalTTLErrPackets,
       "cscTpTotalTcpUdpChksumErrPackets": cscTpTotalTcpUdpChksumErrPackets,
       "cscTpHandledPacketsRate": cscTpHandledPacketsRate,
       "cscTpHandledFlowsRate": cscTpHandledFlowsRate,
       "cscTpFlowsCapacityUtilization": cscTpFlowsCapacityUtilization,
       "cscTpServiceLoss": cscTpServiceLoss,
       "cscTpStatsTrafficCountersTable": cscTpStatsTrafficCountersTable,
       "cscTpStatsTrafficCountersEntry": cscTpStatsTrafficCountersEntry,
       "cscTpStatsTrafficCounterIndex": cscTpStatsTrafficCounterIndex,
       "cscTpStatsTrafficCounterName": cscTpStatsTrafficCounterName,
       "cscTpStatsTrafficCounterValue": cscTpStatsTrafficCounterValue,
       "cscTpStatsTrafficCounterType": cscTpStatsTrafficCounterType,
       "cscTpCounterDiscontinuityTime": cscTpCounterDiscontinuityTime,
       "ciscoSCTpStatsMIBConform": ciscoSCTpStatsMIBConform,
       "cscTpStatsMIBCompliances": cscTpStatsMIBCompliances,
       "cscTpStatsMIBCompliance": cscTpStatsMIBCompliance,
       "cscTpStatsMIBGroups": cscTpStatsMIBGroups,
       "cscTpStatsMIBObjectGroup": cscTpStatsMIBObjectGroup,
       "cscTpStatsMIBTrafficCntrsObjGroup": cscTpStatsMIBTrafficCntrsObjGroup,
       "cscTpCounterDiscontinuityGroup": cscTpCounterDiscontinuityGroup}
)
