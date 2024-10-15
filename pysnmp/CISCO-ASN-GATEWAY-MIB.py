# SNMP MIB module (CISCO-ASN-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ASN-GATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:42 2024
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

(CiscoAlarmSeverity,
 EntPhysicalIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "EntPhysicalIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAgwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638)
)
ciscoAgwMIB.setRevisions(
        ("2009-05-26 00:00",
         "2008-04-22 00:00",
         "2008-03-24 00:00",
         "2007-09-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAgwMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoAgwMIBNotifs = _CiscoAgwMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 0)
)
_CiscoAgwMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAgwMIBObjects = _CiscoAgwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1)
)
_CagwInstances_ObjectIdentity = ObjectIdentity
cagwInstances = _CagwInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1)
)
_CagwInstanceTable_Object = MibTable
cagwInstanceTable = _CagwInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cagwInstanceTable.setStatus("current")
_CagwInstanceEntry_Object = MibTableRow
cagwInstanceEntry = _CagwInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1, 1)
)
cagwInstanceEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
)
if mibBuilder.loadTexts:
    cagwInstanceEntry.setStatus("current")
_CagwInstanceIndex_Type = Unsigned32
_CagwInstanceIndex_Object = MibTableColumn
cagwInstanceIndex = _CagwInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1, 1, 1),
    _CagwInstanceIndex_Type()
)
cagwInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwInstanceIndex.setStatus("current")
_CagwInstancePhysicalIndex_Type = EntPhysicalIndexOrZero
_CagwInstancePhysicalIndex_Object = MibTableColumn
cagwInstancePhysicalIndex = _CagwInstancePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1, 1, 2),
    _CagwInstancePhysicalIndex_Type()
)
cagwInstancePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwInstancePhysicalIndex.setStatus("current")
_CagwInstanceDescription_Type = SnmpAdminString
_CagwInstanceDescription_Object = MibTableColumn
cagwInstanceDescription = _CagwInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1, 1, 3),
    _CagwInstanceDescription_Type()
)
cagwInstanceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwInstanceDescription.setStatus("current")
_CagwInstanceVersion_Type = SnmpAdminString
_CagwInstanceVersion_Object = MibTableColumn
cagwInstanceVersion = _CagwInstanceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1, 1, 4),
    _CagwInstanceVersion_Type()
)
cagwInstanceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwInstanceVersion.setStatus("current")


class _CagwInstanceOperState_Type(Integer32):
    """Custom type cagwInstanceOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CagwInstanceOperState_Type.__name__ = "Integer32"
_CagwInstanceOperState_Object = MibTableColumn
cagwInstanceOperState = _CagwInstanceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1, 1, 5),
    _CagwInstanceOperState_Type()
)
cagwInstanceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwInstanceOperState.setStatus("current")


class _CagwInstanceSessionRedundancyAdmin_Type(Integer32):
    """Custom type cagwInstanceSessionRedundancyAdmin based on Integer32"""
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


_CagwInstanceSessionRedundancyAdmin_Type.__name__ = "Integer32"
_CagwInstanceSessionRedundancyAdmin_Object = MibTableColumn
cagwInstanceSessionRedundancyAdmin = _CagwInstanceSessionRedundancyAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 1, 1, 1, 6),
    _CagwInstanceSessionRedundancyAdmin_Type()
)
cagwInstanceSessionRedundancyAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwInstanceSessionRedundancyAdmin.setStatus("current")
_CagwState_ObjectIdentity = ObjectIdentity
cagwState = _CagwState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2)
)
_CagwStateTable_Object = MibTable
cagwStateTable = _CagwStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cagwStateTable.setStatus("current")
_CagwStateEntry_Object = MibTableRow
cagwStateEntry = _CagwStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1)
)
cagwStateEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
)
if mibBuilder.loadTexts:
    cagwStateEntry.setStatus("current")
_CagwMaximumBaseStations_Type = Integer32
_CagwMaximumBaseStations_Object = MibTableColumn
cagwMaximumBaseStations = _CagwMaximumBaseStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 1),
    _CagwMaximumBaseStations_Type()
)
cagwMaximumBaseStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaximumBaseStations.setStatus("current")
if mibBuilder.loadTexts:
    cagwMaximumBaseStations.setUnits("base stations")
_CagwMaximumSubscribers_Type = Integer32
_CagwMaximumSubscribers_Object = MibTableColumn
cagwMaximumSubscribers = _CagwMaximumSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 2),
    _CagwMaximumSubscribers_Type()
)
cagwMaximumSubscribers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaximumSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    cagwMaximumSubscribers.setUnits("subscribers")
_CagwMaximumFlowsPerSession_Type = Integer32
_CagwMaximumFlowsPerSession_Object = MibTableColumn
cagwMaximumFlowsPerSession = _CagwMaximumFlowsPerSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 3),
    _CagwMaximumFlowsPerSession_Type()
)
cagwMaximumFlowsPerSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaximumFlowsPerSession.setStatus("current")
if mibBuilder.loadTexts:
    cagwMaximumFlowsPerSession.setUnits("flows")
_CagwCurrentBaseStations_Type = Gauge32
_CagwCurrentBaseStations_Object = MibTableColumn
cagwCurrentBaseStations = _CagwCurrentBaseStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 4),
    _CagwCurrentBaseStations_Type()
)
cagwCurrentBaseStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentBaseStations.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentBaseStations.setUnits("paths")
_CagwCurrentDataPaths_Type = Gauge32
_CagwCurrentDataPaths_Object = MibTableColumn
cagwCurrentDataPaths = _CagwCurrentDataPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 5),
    _CagwCurrentDataPaths_Type()
)
cagwCurrentDataPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentDataPaths.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentDataPaths.setUnits("paths")
_CagwCurrentSubscribers_Type = Gauge32
_CagwCurrentSubscribers_Object = MibTableColumn
cagwCurrentSubscribers = _CagwCurrentSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 6),
    _CagwCurrentSubscribers_Type()
)
cagwCurrentSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentSubscribers.setUnits("subscribers")
_CagwCurrentSessions_Type = Gauge32
_CagwCurrentSessions_Object = MibTableColumn
cagwCurrentSessions = _CagwCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 7),
    _CagwCurrentSessions_Type()
)
cagwCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentSessions.setUnits("sessions")
_CagwCurrentFlows_Type = Gauge32
_CagwCurrentFlows_Object = MibTableColumn
cagwCurrentFlows = _CagwCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 8),
    _CagwCurrentFlows_Type()
)
cagwCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentFlows.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentFlows.setUnits("flows")
_CagwCurrentHosts_Type = Gauge32
_CagwCurrentHosts_Object = MibTableColumn
cagwCurrentHosts = _CagwCurrentHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 9),
    _CagwCurrentHosts_Type()
)
cagwCurrentHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentHosts.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentHosts.setUnits("hosts")
_CagwNetworkBehindMs_Type = Gauge32
_CagwNetworkBehindMs_Object = MibTableColumn
cagwNetworkBehindMs = _CagwNetworkBehindMs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 10),
    _CagwNetworkBehindMs_Type()
)
cagwNetworkBehindMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwNetworkBehindMs.setStatus("current")
if mibBuilder.loadTexts:
    cagwNetworkBehindMs.setUnits("mobile stations")
_CagwPendingSignalingPkts_Type = Gauge32
_CagwPendingSignalingPkts_Object = MibTableColumn
cagwPendingSignalingPkts = _CagwPendingSignalingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 11),
    _CagwPendingSignalingPkts_Type()
)
cagwPendingSignalingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPendingSignalingPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwPendingSignalingPkts.setUnits("packets")
_CagwCurrentFramedRoutes_Type = Gauge32
_CagwCurrentFramedRoutes_Object = MibTableColumn
cagwCurrentFramedRoutes = _CagwCurrentFramedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 12),
    _CagwCurrentFramedRoutes_Type()
)
cagwCurrentFramedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentFramedRoutes.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentFramedRoutes.setUnits("routes")
_CagwCurrentFramedRouteSubs_Type = Gauge32
_CagwCurrentFramedRouteSubs_Object = MibTableColumn
cagwCurrentFramedRouteSubs = _CagwCurrentFramedRouteSubs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 13),
    _CagwCurrentFramedRouteSubs_Type()
)
cagwCurrentFramedRouteSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentFramedRouteSubs.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentFramedRouteSubs.setUnits("subscribers")
_CagwCurrentAutoProvSessions_Type = Gauge32
_CagwCurrentAutoProvSessions_Object = MibTableColumn
cagwCurrentAutoProvSessions = _CagwCurrentAutoProvSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 14),
    _CagwCurrentAutoProvSessions_Type()
)
cagwCurrentAutoProvSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentAutoProvSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentAutoProvSessions.setUnits("Sessions")
_CagwCurrentSessionsWithIpPktsRedir_Type = Gauge32
_CagwCurrentSessionsWithIpPktsRedir_Object = MibTableColumn
cagwCurrentSessionsWithIpPktsRedir = _CagwCurrentSessionsWithIpPktsRedir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 15),
    _CagwCurrentSessionsWithIpPktsRedir_Type()
)
cagwCurrentSessionsWithIpPktsRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentSessionsWithIpPktsRedir.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentSessionsWithIpPktsRedir.setUnits("Sessions")
_CagwCurrentPmipEnabledSubs_Type = Gauge32
_CagwCurrentPmipEnabledSubs_Object = MibTableColumn
cagwCurrentPmipEnabledSubs = _CagwCurrentPmipEnabledSubs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 2, 1, 1, 16),
    _CagwCurrentPmipEnabledSubs_Type()
)
cagwCurrentPmipEnabledSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCurrentPmipEnabledSubs.setStatus("current")
if mibBuilder.loadTexts:
    cagwCurrentPmipEnabledSubs.setUnits("subscribers")
_CagwStatistics_ObjectIdentity = ObjectIdentity
cagwStatistics = _CagwStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3)
)
_CagwGlobalStatistics_ObjectIdentity = ObjectIdentity
cagwGlobalStatistics = _CagwGlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1)
)
_CagwGlobalStatisticsTable_Object = MibTable
cagwGlobalStatisticsTable = _CagwGlobalStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cagwGlobalStatisticsTable.setStatus("current")
_CagwGlobalStatisticsEntry_Object = MibTableRow
cagwGlobalStatisticsEntry = _CagwGlobalStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1)
)
cagwGlobalStatisticsEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
)
if mibBuilder.loadTexts:
    cagwGlobalStatisticsEntry.setStatus("current")
_CagwCreatedSubscribers_Type = Counter32
_CagwCreatedSubscribers_Object = MibTableColumn
cagwCreatedSubscribers = _CagwCreatedSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 1),
    _CagwCreatedSubscribers_Type()
)
cagwCreatedSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCreatedSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    cagwCreatedSubscribers.setUnits("subscribers")
_CagwDeletedSubscribers_Type = Counter32
_CagwDeletedSubscribers_Object = MibTableColumn
cagwDeletedSubscribers = _CagwDeletedSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 2),
    _CagwDeletedSubscribers_Type()
)
cagwDeletedSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDeletedSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    cagwDeletedSubscribers.setUnits("subscribers")
_CagwCreatedSessions_Type = Counter32
_CagwCreatedSessions_Object = MibTableColumn
cagwCreatedSessions = _CagwCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 3),
    _CagwCreatedSessions_Type()
)
cagwCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCreatedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwCreatedSessions.setUnits("sessions")
_CagwDeletedSessions_Type = Counter32
_CagwDeletedSessions_Object = MibTableColumn
cagwDeletedSessions = _CagwDeletedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 4),
    _CagwDeletedSessions_Type()
)
cagwDeletedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDeletedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwDeletedSessions.setUnits("sessions")
_CagwCreatedFlows_Type = Counter32
_CagwCreatedFlows_Object = MibTableColumn
cagwCreatedFlows = _CagwCreatedFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 5),
    _CagwCreatedFlows_Type()
)
cagwCreatedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCreatedFlows.setStatus("current")
if mibBuilder.loadTexts:
    cagwCreatedFlows.setUnits("flows")
_CagwDeletedFlows_Type = Counter32
_CagwDeletedFlows_Object = MibTableColumn
cagwDeletedFlows = _CagwDeletedFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 6),
    _CagwDeletedFlows_Type()
)
cagwDeletedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDeletedFlows.setStatus("current")
if mibBuilder.loadTexts:
    cagwDeletedFlows.setUnits("flows")
_CagwCreatedHosts_Type = Counter32
_CagwCreatedHosts_Object = MibTableColumn
cagwCreatedHosts = _CagwCreatedHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 7),
    _CagwCreatedHosts_Type()
)
cagwCreatedHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCreatedHosts.setStatus("current")
if mibBuilder.loadTexts:
    cagwCreatedHosts.setUnits("hosts")
_CagwDeletedHosts_Type = Counter32
_CagwDeletedHosts_Object = MibTableColumn
cagwDeletedHosts = _CagwDeletedHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 8),
    _CagwDeletedHosts_Type()
)
cagwDeletedHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDeletedHosts.setStatus("current")
if mibBuilder.loadTexts:
    cagwDeletedHosts.setUnits("hosts")
_CagwCreatedBaseStations_Type = Counter32
_CagwCreatedBaseStations_Object = MibTableColumn
cagwCreatedBaseStations = _CagwCreatedBaseStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 9),
    _CagwCreatedBaseStations_Type()
)
cagwCreatedBaseStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCreatedBaseStations.setStatus("current")
if mibBuilder.loadTexts:
    cagwCreatedBaseStations.setUnits("paths")
_CagwDeletedBaseStations_Type = Counter32
_CagwDeletedBaseStations_Object = MibTableColumn
cagwDeletedBaseStations = _CagwDeletedBaseStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 10),
    _CagwDeletedBaseStations_Type()
)
cagwDeletedBaseStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDeletedBaseStations.setStatus("current")
if mibBuilder.loadTexts:
    cagwDeletedBaseStations.setUnits("paths")
_CagwCreatedDataPaths_Type = Counter32
_CagwCreatedDataPaths_Object = MibTableColumn
cagwCreatedDataPaths = _CagwCreatedDataPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 11),
    _CagwCreatedDataPaths_Type()
)
cagwCreatedDataPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCreatedDataPaths.setStatus("current")
if mibBuilder.loadTexts:
    cagwCreatedDataPaths.setUnits("paths")
_CagwDeletedDataPaths_Type = Counter32
_CagwDeletedDataPaths_Object = MibTableColumn
cagwDeletedDataPaths = _CagwDeletedDataPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 12),
    _CagwDeletedDataPaths_Type()
)
cagwDeletedDataPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDeletedDataPaths.setStatus("current")
if mibBuilder.loadTexts:
    cagwDeletedDataPaths.setUnits("paths")
_CagwProcessedSignalingPkts_Type = Counter32
_CagwProcessedSignalingPkts_Object = MibTableColumn
cagwProcessedSignalingPkts = _CagwProcessedSignalingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 13),
    _CagwProcessedSignalingPkts_Type()
)
cagwProcessedSignalingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwProcessedSignalingPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwProcessedSignalingPkts.setUnits("packets")
_CagwRequeuedSignalingPkts_Type = Counter32
_CagwRequeuedSignalingPkts_Object = MibTableColumn
cagwRequeuedSignalingPkts = _CagwRequeuedSignalingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 14),
    _CagwRequeuedSignalingPkts_Type()
)
cagwRequeuedSignalingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwRequeuedSignalingPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwRequeuedSignalingPkts.setUnits("packets")
_CagwCongestionSignalingPktsDrops_Type = Counter32
_CagwCongestionSignalingPktsDrops_Object = MibTableColumn
cagwCongestionSignalingPktsDrops = _CagwCongestionSignalingPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 15),
    _CagwCongestionSignalingPktsDrops_Type()
)
cagwCongestionSignalingPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCongestionSignalingPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwCongestionSignalingPktsDrops.setUnits("packets")
_CagwServiceDisabledSignalingPktsDrops_Type = Counter32
_CagwServiceDisabledSignalingPktsDrops_Object = MibTableColumn
cagwServiceDisabledSignalingPktsDrops = _CagwServiceDisabledSignalingPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 16),
    _CagwServiceDisabledSignalingPktsDrops_Type()
)
cagwServiceDisabledSignalingPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwServiceDisabledSignalingPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwServiceDisabledSignalingPktsDrops.setUnits("packets")
_CagwServiceNotReadySignalingPktsDrops_Type = Counter32
_CagwServiceNotReadySignalingPktsDrops_Object = MibTableColumn
cagwServiceNotReadySignalingPktsDrops = _CagwServiceNotReadySignalingPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 17),
    _CagwServiceNotReadySignalingPktsDrops_Type()
)
cagwServiceNotReadySignalingPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwServiceNotReadySignalingPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwServiceNotReadySignalingPktsDrops.setUnits("packets")
_CagwEncapErrorSignalingPktsDrops_Type = Counter32
_CagwEncapErrorSignalingPktsDrops_Object = MibTableColumn
cagwEncapErrorSignalingPktsDrops = _CagwEncapErrorSignalingPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 18),
    _CagwEncapErrorSignalingPktsDrops_Type()
)
cagwEncapErrorSignalingPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEncapErrorSignalingPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwEncapErrorSignalingPktsDrops.setUnits("packets")
_CagwDisposedSignalingPktsDrops_Type = Counter32
_CagwDisposedSignalingPktsDrops_Object = MibTableColumn
cagwDisposedSignalingPktsDrops = _CagwDisposedSignalingPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 19),
    _CagwDisposedSignalingPktsDrops_Type()
)
cagwDisposedSignalingPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDisposedSignalingPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwDisposedSignalingPktsDrops.setUnits("packets")
_CagwEncapErrorDataPktsDrops_Type = Counter32
_CagwEncapErrorDataPktsDrops_Object = MibTableColumn
cagwEncapErrorDataPktsDrops = _CagwEncapErrorDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 41),
    _CagwEncapErrorDataPktsDrops_Type()
)
cagwEncapErrorDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEncapErrorDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwEncapErrorDataPktsDrops.setUnits("packets")
_CagwInvalidAddressDataPktsDrops_Type = Counter32
_CagwInvalidAddressDataPktsDrops_Object = MibTableColumn
cagwInvalidAddressDataPktsDrops = _CagwInvalidAddressDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 42),
    _CagwInvalidAddressDataPktsDrops_Type()
)
cagwInvalidAddressDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwInvalidAddressDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwInvalidAddressDataPktsDrops.setUnits("packets")
_CagwServiceDisabledDataPktsDrops_Type = Counter32
_CagwServiceDisabledDataPktsDrops_Object = MibTableColumn
cagwServiceDisabledDataPktsDrops = _CagwServiceDisabledDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 43),
    _CagwServiceDisabledDataPktsDrops_Type()
)
cagwServiceDisabledDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwServiceDisabledDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwServiceDisabledDataPktsDrops.setUnits("packets")
_CagwInvalidProtocolTypeDataPktsDrops_Type = Counter32
_CagwInvalidProtocolTypeDataPktsDrops_Object = MibTableColumn
cagwInvalidProtocolTypeDataPktsDrops = _CagwInvalidProtocolTypeDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 44),
    _CagwInvalidProtocolTypeDataPktsDrops_Type()
)
cagwInvalidProtocolTypeDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwInvalidProtocolTypeDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwInvalidProtocolTypeDataPktsDrops.setUnits("packets")
_CagwLengthErrorDataPktsDrops_Type = Counter32
_CagwLengthErrorDataPktsDrops_Object = MibTableColumn
cagwLengthErrorDataPktsDrops = _CagwLengthErrorDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 45),
    _CagwLengthErrorDataPktsDrops_Type()
)
cagwLengthErrorDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwLengthErrorDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwLengthErrorDataPktsDrops.setUnits("packets")
_CagwAbsentKeyDataPktsDrops_Type = Counter32
_CagwAbsentKeyDataPktsDrops_Object = MibTableColumn
cagwAbsentKeyDataPktsDrops = _CagwAbsentKeyDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 46),
    _CagwAbsentKeyDataPktsDrops_Type()
)
cagwAbsentKeyDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwAbsentKeyDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwAbsentKeyDataPktsDrops.setUnits("packets")
_CagwFlowNotFoundDataPktsDrops_Type = Counter32
_CagwFlowNotFoundDataPktsDrops_Object = MibTableColumn
cagwFlowNotFoundDataPktsDrops = _CagwFlowNotFoundDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 47),
    _CagwFlowNotFoundDataPktsDrops_Type()
)
cagwFlowNotFoundDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFlowNotFoundDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwFlowNotFoundDataPktsDrops.setUnits("packets")
_CagwFlowPathNotFoundDataPktsDrops_Type = Counter32
_CagwFlowPathNotFoundDataPktsDrops_Object = MibTableColumn
cagwFlowPathNotFoundDataPktsDrops = _CagwFlowPathNotFoundDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 48),
    _CagwFlowPathNotFoundDataPktsDrops_Type()
)
cagwFlowPathNotFoundDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFlowPathNotFoundDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwFlowPathNotFoundDataPktsDrops.setUnits("packets")
_CagwFlowPathInvalidSourceDataPktsDrops_Type = Counter32
_CagwFlowPathInvalidSourceDataPktsDrops_Object = MibTableColumn
cagwFlowPathInvalidSourceDataPktsDrops = _CagwFlowPathInvalidSourceDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 49),
    _CagwFlowPathInvalidSourceDataPktsDrops_Type()
)
cagwFlowPathInvalidSourceDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFlowPathInvalidSourceDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwFlowPathInvalidSourceDataPktsDrops.setUnits("packets")
_CagwSessionNotFoundDataPktsDrops_Type = Counter32
_CagwSessionNotFoundDataPktsDrops_Object = MibTableColumn
cagwSessionNotFoundDataPktsDrops = _CagwSessionNotFoundDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 50),
    _CagwSessionNotFoundDataPktsDrops_Type()
)
cagwSessionNotFoundDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSessionNotFoundDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwSessionNotFoundDataPktsDrops.setUnits("packets")
_CagwSubscriberNotFoundDataPktsDrops_Type = Counter32
_CagwSubscriberNotFoundDataPktsDrops_Object = MibTableColumn
cagwSubscriberNotFoundDataPktsDrops = _CagwSubscriberNotFoundDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 51),
    _CagwSubscriberNotFoundDataPktsDrops_Type()
)
cagwSubscriberNotFoundDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSubscriberNotFoundDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwSubscriberNotFoundDataPktsDrops.setUnits("packets")
_CagwChecksumErrorDataPktsDrops_Type = Counter32
_CagwChecksumErrorDataPktsDrops_Object = MibTableColumn
cagwChecksumErrorDataPktsDrops = _CagwChecksumErrorDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 52),
    _CagwChecksumErrorDataPktsDrops_Type()
)
cagwChecksumErrorDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwChecksumErrorDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwChecksumErrorDataPktsDrops.setUnits("packets")
_CagwIngressFilteringDataPktsDrops_Type = Counter32
_CagwIngressFilteringDataPktsDrops_Object = MibTableColumn
cagwIngressFilteringDataPktsDrops = _CagwIngressFilteringDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 53),
    _CagwIngressFilteringDataPktsDrops_Type()
)
cagwIngressFilteringDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIngressFilteringDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwIngressFilteringDataPktsDrops.setUnits("packets")
_CagwSequenceNumberErrorDataPktsDrops_Type = Counter32
_CagwSequenceNumberErrorDataPktsDrops_Object = MibTableColumn
cagwSequenceNumberErrorDataPktsDrops = _CagwSequenceNumberErrorDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 54),
    _CagwSequenceNumberErrorDataPktsDrops_Type()
)
cagwSequenceNumberErrorDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSequenceNumberErrorDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwSequenceNumberErrorDataPktsDrops.setUnits("packets")
_CagwFragmentedDataPktsDrops_Type = Counter32
_CagwFragmentedDataPktsDrops_Object = MibTableColumn
cagwFragmentedDataPktsDrops = _CagwFragmentedDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 55),
    _CagwFragmentedDataPktsDrops_Type()
)
cagwFragmentedDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFragmentedDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwFragmentedDataPktsDrops.setUnits("packets")
_CagwFramedRouteInserted_Type = Counter32
_CagwFramedRouteInserted_Object = MibTableColumn
cagwFramedRouteInserted = _CagwFramedRouteInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 56),
    _CagwFramedRouteInserted_Type()
)
cagwFramedRouteInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFramedRouteInserted.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwFramedRouteInserted.setUnits("routes")
_CagwFramedRouteInsertFailed_Type = Counter32
_CagwFramedRouteInsertFailed_Object = MibTableColumn
cagwFramedRouteInsertFailed = _CagwFramedRouteInsertFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 57),
    _CagwFramedRouteInsertFailed_Type()
)
cagwFramedRouteInsertFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFramedRouteInsertFailed.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwFramedRouteInsertFailed.setUnits("routes")
_CagwFramedRouteDeleted_Type = Counter32
_CagwFramedRouteDeleted_Object = MibTableColumn
cagwFramedRouteDeleted = _CagwFramedRouteDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 58),
    _CagwFramedRouteDeleted_Type()
)
cagwFramedRouteDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFramedRouteDeleted.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwFramedRouteDeleted.setUnits("routes")
_CagwServiceFlowProfileNotFound_Type = Counter32
_CagwServiceFlowProfileNotFound_Object = MibTableColumn
cagwServiceFlowProfileNotFound = _CagwServiceFlowProfileNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 59),
    _CagwServiceFlowProfileNotFound_Type()
)
cagwServiceFlowProfileNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwServiceFlowProfileNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cagwServiceFlowProfileNotFound.setUnits("service flow profiles")
_CagwQosProfileNotFound_Type = Counter32
_CagwQosProfileNotFound_Object = MibTableColumn
cagwQosProfileNotFound = _CagwQosProfileNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 60),
    _CagwQosProfileNotFound_Type()
)
cagwQosProfileNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwQosProfileNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cagwQosProfileNotFound.setUnits("qos profiles")
_CagwClassifierProfileNotFound_Type = Counter32
_CagwClassifierProfileNotFound_Object = MibTableColumn
cagwClassifierProfileNotFound = _CagwClassifierProfileNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 61),
    _CagwClassifierProfileNotFound_Type()
)
cagwClassifierProfileNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwClassifierProfileNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cagwClassifierProfileNotFound.setUnits("classifier profiles")
_CagwReceivedDataPkts_Type = Counter64
_CagwReceivedDataPkts_Object = MibTableColumn
cagwReceivedDataPkts = _CagwReceivedDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 62),
    _CagwReceivedDataPkts_Type()
)
cagwReceivedDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwReceivedDataPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwReceivedDataPkts.setUnits("packets")
_CagwReceivedDataBytes_Type = Counter64
_CagwReceivedDataBytes_Object = MibTableColumn
cagwReceivedDataBytes = _CagwReceivedDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 63),
    _CagwReceivedDataBytes_Type()
)
cagwReceivedDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwReceivedDataBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwReceivedDataBytes.setUnits("bytes")
_CagwSentDataPkts_Type = Counter64
_CagwSentDataPkts_Object = MibTableColumn
cagwSentDataPkts = _CagwSentDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 64),
    _CagwSentDataPkts_Type()
)
cagwSentDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSentDataPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwSentDataPkts.setUnits("packets")
_CagwSentDataBytes_Type = Counter64
_CagwSentDataBytes_Object = MibTableColumn
cagwSentDataBytes = _CagwSentDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 65),
    _CagwSentDataBytes_Type()
)
cagwSentDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSentDataBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwSentDataBytes.setUnits("bytes")
_CagwRejectedSessions_Type = Counter32
_CagwRejectedSessions_Object = MibTableColumn
cagwRejectedSessions = _CagwRejectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 66),
    _CagwRejectedSessions_Type()
)
cagwRejectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwRejectedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwRejectedSessions.setUnits("sessions")
_CagwRejectedFlows_Type = Counter32
_CagwRejectedFlows_Object = MibTableColumn
cagwRejectedFlows = _CagwRejectedFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 67),
    _CagwRejectedFlows_Type()
)
cagwRejectedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwRejectedFlows.setStatus("current")
if mibBuilder.loadTexts:
    cagwRejectedFlows.setUnits("flows")
_CagwRejectedBaseStations_Type = Counter32
_CagwRejectedBaseStations_Object = MibTableColumn
cagwRejectedBaseStations = _CagwRejectedBaseStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 68),
    _CagwRejectedBaseStations_Type()
)
cagwRejectedBaseStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwRejectedBaseStations.setStatus("current")
if mibBuilder.loadTexts:
    cagwRejectedBaseStations.setUnits("paths")
_CagwSessionsDeletedByAgw_Type = Counter32
_CagwSessionsDeletedByAgw_Object = MibTableColumn
cagwSessionsDeletedByAgw = _CagwSessionsDeletedByAgw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 69),
    _CagwSessionsDeletedByAgw_Type()
)
cagwSessionsDeletedByAgw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSessionsDeletedByAgw.setStatus("current")
if mibBuilder.loadTexts:
    cagwSessionsDeletedByAgw.setUnits("sessions")
_CagwIpGreReceivedDataPkts_Type = Counter64
_CagwIpGreReceivedDataPkts_Object = MibTableColumn
cagwIpGreReceivedDataPkts = _CagwIpGreReceivedDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 70),
    _CagwIpGreReceivedDataPkts_Type()
)
cagwIpGreReceivedDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIpGreReceivedDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwIpGreReceivedDataPkts.setUnits("packets")
_CagwIpGreReceivedDataBytes_Type = Counter64
_CagwIpGreReceivedDataBytes_Object = MibTableColumn
cagwIpGreReceivedDataBytes = _CagwIpGreReceivedDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 71),
    _CagwIpGreReceivedDataBytes_Type()
)
cagwIpGreReceivedDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIpGreReceivedDataBytes.setStatus("current")
if mibBuilder.loadTexts:
    cagwIpGreReceivedDataBytes.setUnits("bytes")
_CagwIpGreSentDataPkts_Type = Counter64
_CagwIpGreSentDataPkts_Object = MibTableColumn
cagwIpGreSentDataPkts = _CagwIpGreSentDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 72),
    _CagwIpGreSentDataPkts_Type()
)
cagwIpGreSentDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIpGreSentDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwIpGreSentDataPkts.setUnits("packets")
_CagwIpGreSentDataBytes_Type = Counter64
_CagwIpGreSentDataBytes_Object = MibTableColumn
cagwIpGreSentDataBytes = _CagwIpGreSentDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 73),
    _CagwIpGreSentDataBytes_Type()
)
cagwIpGreSentDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIpGreSentDataBytes.setStatus("current")
if mibBuilder.loadTexts:
    cagwIpGreSentDataBytes.setUnits("bytes")
_CagwEthGreReceivedDataPkts_Type = Counter64
_CagwEthGreReceivedDataPkts_Object = MibTableColumn
cagwEthGreReceivedDataPkts = _CagwEthGreReceivedDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 74),
    _CagwEthGreReceivedDataPkts_Type()
)
cagwEthGreReceivedDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEthGreReceivedDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwEthGreReceivedDataPkts.setUnits("packets")
_CagwEthGreReceivedDataBytes_Type = Counter64
_CagwEthGreReceivedDataBytes_Object = MibTableColumn
cagwEthGreReceivedDataBytes = _CagwEthGreReceivedDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 75),
    _CagwEthGreReceivedDataBytes_Type()
)
cagwEthGreReceivedDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEthGreReceivedDataBytes.setStatus("current")
if mibBuilder.loadTexts:
    cagwEthGreReceivedDataBytes.setUnits("bytes")
_CagwEthGreSentDataPkts_Type = Counter64
_CagwEthGreSentDataPkts_Object = MibTableColumn
cagwEthGreSentDataPkts = _CagwEthGreSentDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 76),
    _CagwEthGreSentDataPkts_Type()
)
cagwEthGreSentDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEthGreSentDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwEthGreSentDataPkts.setUnits("packets")
_CagwEthGreSentDataBytes_Type = Counter64
_CagwEthGreSentDataBytes_Object = MibTableColumn
cagwEthGreSentDataBytes = _CagwEthGreSentDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 77),
    _CagwEthGreSentDataBytes_Type()
)
cagwEthGreSentDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEthGreSentDataBytes.setStatus("current")
if mibBuilder.loadTexts:
    cagwEthGreSentDataBytes.setUnits("bytes")
_CagwRejectedHosts_Type = Counter32
_CagwRejectedHosts_Object = MibTableColumn
cagwRejectedHosts = _CagwRejectedHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 78),
    _CagwRejectedHosts_Type()
)
cagwRejectedHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwRejectedHosts.setStatus("current")
if mibBuilder.loadTexts:
    cagwRejectedHosts.setUnits("hosts")
_CagwAgedOutStaticHosts_Type = Counter32
_CagwAgedOutStaticHosts_Object = MibTableColumn
cagwAgedOutStaticHosts = _CagwAgedOutStaticHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 79),
    _CagwAgedOutStaticHosts_Type()
)
cagwAgedOutStaticHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwAgedOutStaticHosts.setStatus("current")
if mibBuilder.loadTexts:
    cagwAgedOutStaticHosts.setUnits("hosts")
_CagwSuccessfulHandoff_Type = Counter32
_CagwSuccessfulHandoff_Object = MibTableColumn
cagwSuccessfulHandoff = _CagwSuccessfulHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 80),
    _CagwSuccessfulHandoff_Type()
)
cagwSuccessfulHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSuccessfulHandoff.setStatus("current")
if mibBuilder.loadTexts:
    cagwSuccessfulHandoff.setUnits("sessions")
_CagwFailedHandoff_Type = Counter32
_CagwFailedHandoff_Object = MibTableColumn
cagwFailedHandoff = _CagwFailedHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 81),
    _CagwFailedHandoff_Type()
)
cagwFailedHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFailedHandoff.setStatus("current")
if mibBuilder.loadTexts:
    cagwFailedHandoff.setUnits("sessions")
_CagwSuccessfulCMACKeyUpdate_Type = Counter32
_CagwSuccessfulCMACKeyUpdate_Object = MibTableColumn
cagwSuccessfulCMACKeyUpdate = _CagwSuccessfulCMACKeyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 82),
    _CagwSuccessfulCMACKeyUpdate_Type()
)
cagwSuccessfulCMACKeyUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSuccessfulCMACKeyUpdate.setStatus("current")
if mibBuilder.loadTexts:
    cagwSuccessfulCMACKeyUpdate.setUnits("CMACKeyUpdates")
_CagwFailedCMACKeyUpdate_Type = Counter32
_CagwFailedCMACKeyUpdate_Object = MibTableColumn
cagwFailedCMACKeyUpdate = _CagwFailedCMACKeyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 83),
    _CagwFailedCMACKeyUpdate_Type()
)
cagwFailedCMACKeyUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFailedCMACKeyUpdate.setStatus("current")
if mibBuilder.loadTexts:
    cagwFailedCMACKeyUpdate.setUnits("CMACKeyUpdates")
_CagwSuccessfulSecurityKeyExchange_Type = Counter32
_CagwSuccessfulSecurityKeyExchange_Object = MibTableColumn
cagwSuccessfulSecurityKeyExchange = _CagwSuccessfulSecurityKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 84),
    _CagwSuccessfulSecurityKeyExchange_Type()
)
cagwSuccessfulSecurityKeyExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSuccessfulSecurityKeyExchange.setStatus("current")
if mibBuilder.loadTexts:
    cagwSuccessfulSecurityKeyExchange.setUnits("SecurityKeyExchange")
_CagwFailedSecurityKeyExchange_Type = Counter32
_CagwFailedSecurityKeyExchange_Object = MibTableColumn
cagwFailedSecurityKeyExchange = _CagwFailedSecurityKeyExchange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 85),
    _CagwFailedSecurityKeyExchange_Type()
)
cagwFailedSecurityKeyExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwFailedSecurityKeyExchange.setStatus("current")
if mibBuilder.loadTexts:
    cagwFailedSecurityKeyExchange.setUnits("SecurityKeyExchange")
_CagwIpGreReceivedRedirectedPkts_Type = Counter64
_CagwIpGreReceivedRedirectedPkts_Object = MibTableColumn
cagwIpGreReceivedRedirectedPkts = _CagwIpGreReceivedRedirectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 86),
    _CagwIpGreReceivedRedirectedPkts_Type()
)
cagwIpGreReceivedRedirectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIpGreReceivedRedirectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwIpGreReceivedRedirectedPkts.setUnits("IpDataPktsRedirected")
_CagwIpGreReceivedRedirectedBytes_Type = Counter64
_CagwIpGreReceivedRedirectedBytes_Object = MibTableColumn
cagwIpGreReceivedRedirectedBytes = _CagwIpGreReceivedRedirectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 87),
    _CagwIpGreReceivedRedirectedBytes_Type()
)
cagwIpGreReceivedRedirectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIpGreReceivedRedirectedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cagwIpGreReceivedRedirectedBytes.setUnits("IpDataBytesRedirected")
_CagwEthGreReceivedRedirectedPkts_Type = Counter64
_CagwEthGreReceivedRedirectedPkts_Object = MibTableColumn
cagwEthGreReceivedRedirectedPkts = _CagwEthGreReceivedRedirectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 88),
    _CagwEthGreReceivedRedirectedPkts_Type()
)
cagwEthGreReceivedRedirectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEthGreReceivedRedirectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwEthGreReceivedRedirectedPkts.setUnits("EthDataPktsRedirected")
_CagwEthGreReceivedRedirectedBytes_Type = Counter64
_CagwEthGreReceivedRedirectedBytes_Object = MibTableColumn
cagwEthGreReceivedRedirectedBytes = _CagwEthGreReceivedRedirectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 89),
    _CagwEthGreReceivedRedirectedBytes_Type()
)
cagwEthGreReceivedRedirectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwEthGreReceivedRedirectedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cagwEthGreReceivedRedirectedBytes.setUnits("EthDataBytesRedirected")
_CagwThrottlingOfPuntsDataPktsDrops_Type = Counter32
_CagwThrottlingOfPuntsDataPktsDrops_Object = MibTableColumn
cagwThrottlingOfPuntsDataPktsDrops = _CagwThrottlingOfPuntsDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 90),
    _CagwThrottlingOfPuntsDataPktsDrops_Type()
)
cagwThrottlingOfPuntsDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwThrottlingOfPuntsDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwThrottlingOfPuntsDataPktsDrops.setUnits("packets")
_CagwLearningUpstreamDataPktsDrops_Type = Counter32
_CagwLearningUpstreamDataPktsDrops_Object = MibTableColumn
cagwLearningUpstreamDataPktsDrops = _CagwLearningUpstreamDataPktsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 91),
    _CagwLearningUpstreamDataPktsDrops_Type()
)
cagwLearningUpstreamDataPktsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwLearningUpstreamDataPktsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwLearningUpstreamDataPktsDrops.setUnits("packets")
_CagwPuntedDataPkts_Type = Counter32
_CagwPuntedDataPkts_Object = MibTableColumn
cagwPuntedDataPkts = _CagwPuntedDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 92),
    _CagwPuntedDataPkts_Type()
)
cagwPuntedDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPuntedDataPkts.setStatus("current")
if mibBuilder.loadTexts:
    cagwPuntedDataPkts.setUnits("packets")
_CagwRejectedSessionUnapprovedBs_Type = Counter32
_CagwRejectedSessionUnapprovedBs_Object = MibTableColumn
cagwRejectedSessionUnapprovedBs = _CagwRejectedSessionUnapprovedBs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 93),
    _CagwRejectedSessionUnapprovedBs_Type()
)
cagwRejectedSessionUnapprovedBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwRejectedSessionUnapprovedBs.setStatus("current")
if mibBuilder.loadTexts:
    cagwRejectedSessionUnapprovedBs.setUnits("sessions")
_CagwPktsDroppedStaticIpHostNotAllowed_Type = Counter32
_CagwPktsDroppedStaticIpHostNotAllowed_Object = MibTableColumn
cagwPktsDroppedStaticIpHostNotAllowed = _CagwPktsDroppedStaticIpHostNotAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 94),
    _CagwPktsDroppedStaticIpHostNotAllowed_Type()
)
cagwPktsDroppedStaticIpHostNotAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPktsDroppedStaticIpHostNotAllowed.setStatus("current")
if mibBuilder.loadTexts:
    cagwPktsDroppedStaticIpHostNotAllowed.setUnits("packets")
_CagwPktsDroppedMulticastBroadcast_Type = Counter32
_CagwPktsDroppedMulticastBroadcast_Object = MibTableColumn
cagwPktsDroppedMulticastBroadcast = _CagwPktsDroppedMulticastBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 95),
    _CagwPktsDroppedMulticastBroadcast_Type()
)
cagwPktsDroppedMulticastBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPktsDroppedMulticastBroadcast.setStatus("current")
if mibBuilder.loadTexts:
    cagwPktsDroppedMulticastBroadcast.setUnits("packets")
_CagwSlaProfileNotFound_Type = Counter32
_CagwSlaProfileNotFound_Object = MibTableColumn
cagwSlaProfileNotFound = _CagwSlaProfileNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 96),
    _CagwSlaProfileNotFound_Type()
)
cagwSlaProfileNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwSlaProfileNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cagwSlaProfileNotFound.setUnits("SLA profile")
_CagwPktsDroppedMipIncomplete_Type = Counter32
_CagwPktsDroppedMipIncomplete_Object = MibTableColumn
cagwPktsDroppedMipIncomplete = _CagwPktsDroppedMipIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 97),
    _CagwPktsDroppedMipIncomplete_Type()
)
cagwPktsDroppedMipIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPktsDroppedMipIncomplete.setStatus("current")
if mibBuilder.loadTexts:
    cagwPktsDroppedMipIncomplete.setUnits("packets")
_CagwCreatedPmipEnabledSubs_Type = Counter32
_CagwCreatedPmipEnabledSubs_Object = MibTableColumn
cagwCreatedPmipEnabledSubs = _CagwCreatedPmipEnabledSubs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 98),
    _CagwCreatedPmipEnabledSubs_Type()
)
cagwCreatedPmipEnabledSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCreatedPmipEnabledSubs.setStatus("current")
if mibBuilder.loadTexts:
    cagwCreatedPmipEnabledSubs.setUnits("subscribers")
_CagwDeletedPmipEnabledSubs_Type = Counter32
_CagwDeletedPmipEnabledSubs_Object = MibTableColumn
cagwDeletedPmipEnabledSubs = _CagwDeletedPmipEnabledSubs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 99),
    _CagwDeletedPmipEnabledSubs_Type()
)
cagwDeletedPmipEnabledSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDeletedPmipEnabledSubs.setStatus("current")
if mibBuilder.loadTexts:
    cagwDeletedPmipEnabledSubs.setUnits("subscribers")
_CagwPktsDropPmipStaticIpHost_Type = Counter32
_CagwPktsDropPmipStaticIpHost_Object = MibTableColumn
cagwPktsDropPmipStaticIpHost = _CagwPktsDropPmipStaticIpHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 100),
    _CagwPktsDropPmipStaticIpHost_Type()
)
cagwPktsDropPmipStaticIpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPktsDropPmipStaticIpHost.setStatus("current")
if mibBuilder.loadTexts:
    cagwPktsDropPmipStaticIpHost.setUnits("packets")
_CagwIdleModeEntryMsBsInitiated_Type = Counter32
_CagwIdleModeEntryMsBsInitiated_Object = MibTableColumn
cagwIdleModeEntryMsBsInitiated = _CagwIdleModeEntryMsBsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 101),
    _CagwIdleModeEntryMsBsInitiated_Type()
)
cagwIdleModeEntryMsBsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeEntryMsBsInitiated.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeEntryMsBsInitiated.setUnits("messages")
_CagwIdleModeEntryBwgInitiated_Type = Counter32
_CagwIdleModeEntryBwgInitiated_Object = MibTableColumn
cagwIdleModeEntryBwgInitiated = _CagwIdleModeEntryBwgInitiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 102),
    _CagwIdleModeEntryBwgInitiated_Type()
)
cagwIdleModeEntryBwgInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeEntryBwgInitiated.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeEntryBwgInitiated.setUnits("messages")
_CagwIdleModeEntryFailures_Type = Counter32
_CagwIdleModeEntryFailures_Object = MibTableColumn
cagwIdleModeEntryFailures = _CagwIdleModeEntryFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 103),
    _CagwIdleModeEntryFailures_Type()
)
cagwIdleModeEntryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeEntryFailures.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeEntryFailures.setUnits("messages")
_CagwIdleModeExitMsBsInitiated_Type = Counter32
_CagwIdleModeExitMsBsInitiated_Object = MibTableColumn
cagwIdleModeExitMsBsInitiated = _CagwIdleModeExitMsBsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 104),
    _CagwIdleModeExitMsBsInitiated_Type()
)
cagwIdleModeExitMsBsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeExitMsBsInitiated.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeExitMsBsInitiated.setUnits("messages")
_CagwIdleModeExitBwgInitiated_Type = Counter32
_CagwIdleModeExitBwgInitiated_Object = MibTableColumn
cagwIdleModeExitBwgInitiated = _CagwIdleModeExitBwgInitiated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 105),
    _CagwIdleModeExitBwgInitiated_Type()
)
cagwIdleModeExitBwgInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeExitBwgInitiated.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeExitBwgInitiated.setUnits("messages")
_CagwIdleModeExitFailures_Type = Counter32
_CagwIdleModeExitFailures_Object = MibTableColumn
cagwIdleModeExitFailures = _CagwIdleModeExitFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 106),
    _CagwIdleModeExitFailures_Type()
)
cagwIdleModeExitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeExitFailures.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeExitFailures.setUnits("messages")
_CagwIdleModeLocUpdtPgidChange_Type = Counter32
_CagwIdleModeLocUpdtPgidChange_Object = MibTableColumn
cagwIdleModeLocUpdtPgidChange = _CagwIdleModeLocUpdtPgidChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 107),
    _CagwIdleModeLocUpdtPgidChange_Type()
)
cagwIdleModeLocUpdtPgidChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtPgidChange.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtPgidChange.setUnits("messages")
_CagwIdleModeLocUpdtPowerDown_Type = Counter32
_CagwIdleModeLocUpdtPowerDown_Object = MibTableColumn
cagwIdleModeLocUpdtPowerDown = _CagwIdleModeLocUpdtPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 108),
    _CagwIdleModeLocUpdtPowerDown_Type()
)
cagwIdleModeLocUpdtPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtPowerDown.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtPowerDown.setUnits("messages")
_CagwIdleModeLocUpdtPeriodic_Type = Counter32
_CagwIdleModeLocUpdtPeriodic_Object = MibTableColumn
cagwIdleModeLocUpdtPeriodic = _CagwIdleModeLocUpdtPeriodic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 109),
    _CagwIdleModeLocUpdtPeriodic_Type()
)
cagwIdleModeLocUpdtPeriodic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtPeriodic.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtPeriodic.setUnits("messages")
_CagwIdleModeLocUpdtFailures_Type = Counter32
_CagwIdleModeLocUpdtFailures_Object = MibTableColumn
cagwIdleModeLocUpdtFailures = _CagwIdleModeLocUpdtFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 110),
    _CagwIdleModeLocUpdtFailures_Type()
)
cagwIdleModeLocUpdtFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtFailures.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModeLocUpdtFailures.setUnits("messages")
_CagwIdleModePageAttemptsDwnlnkData_Type = Counter32
_CagwIdleModePageAttemptsDwnlnkData_Object = MibTableColumn
cagwIdleModePageAttemptsDwnlnkData = _CagwIdleModePageAttemptsDwnlnkData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 111),
    _CagwIdleModePageAttemptsDwnlnkData_Type()
)
cagwIdleModePageAttemptsDwnlnkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModePageAttemptsDwnlnkData.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModePageAttemptsDwnlnkData.setUnits("messages")
_CagwIdleModePageFailuresDwnlnkData_Type = Counter32
_CagwIdleModePageFailuresDwnlnkData_Object = MibTableColumn
cagwIdleModePageFailuresDwnlnkData = _CagwIdleModePageFailuresDwnlnkData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 112),
    _CagwIdleModePageFailuresDwnlnkData_Type()
)
cagwIdleModePageFailuresDwnlnkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModePageFailuresDwnlnkData.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModePageFailuresDwnlnkData.setUnits("messages")
_CagwIdleModePageAttemptsLocUpdt_Type = Counter32
_CagwIdleModePageAttemptsLocUpdt_Object = MibTableColumn
cagwIdleModePageAttemptsLocUpdt = _CagwIdleModePageAttemptsLocUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 113),
    _CagwIdleModePageAttemptsLocUpdt_Type()
)
cagwIdleModePageAttemptsLocUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModePageAttemptsLocUpdt.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModePageAttemptsLocUpdt.setUnits("messages")
_CagwIdleModePageFailuresLocUpdt_Type = Counter32
_CagwIdleModePageFailuresLocUpdt_Object = MibTableColumn
cagwIdleModePageFailuresLocUpdt = _CagwIdleModePageFailuresLocUpdt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 114),
    _CagwIdleModePageFailuresLocUpdt_Type()
)
cagwIdleModePageFailuresLocUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModePageFailuresLocUpdt.setStatus("current")
if mibBuilder.loadTexts:
    cagwIdleModePageFailuresLocUpdt.setUnits("messages")
_CagwIdleModeDirectedPagingSuccess_Type = Counter32
_CagwIdleModeDirectedPagingSuccess_Object = MibTableColumn
cagwIdleModeDirectedPagingSuccess = _CagwIdleModeDirectedPagingSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 115),
    _CagwIdleModeDirectedPagingSuccess_Type()
)
cagwIdleModeDirectedPagingSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeDirectedPagingSuccess.setStatus("current")
_CagwIdleModeDirectedPagingRetries_Type = Counter32
_CagwIdleModeDirectedPagingRetries_Object = MibTableColumn
cagwIdleModeDirectedPagingRetries = _CagwIdleModeDirectedPagingRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 116),
    _CagwIdleModeDirectedPagingRetries_Type()
)
cagwIdleModeDirectedPagingRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeDirectedPagingRetries.setStatus("current")
_CagwIdleModeFloodPagingSuccess_Type = Counter32
_CagwIdleModeFloodPagingSuccess_Object = MibTableColumn
cagwIdleModeFloodPagingSuccess = _CagwIdleModeFloodPagingSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 117),
    _CagwIdleModeFloodPagingSuccess_Type()
)
cagwIdleModeFloodPagingSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeFloodPagingSuccess.setStatus("current")
_CagwIdleModeFloodPagingRetries_Type = Counter32
_CagwIdleModeFloodPagingRetries_Object = MibTableColumn
cagwIdleModeFloodPagingRetries = _CagwIdleModeFloodPagingRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 118),
    _CagwIdleModeFloodPagingRetries_Type()
)
cagwIdleModeFloodPagingRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIdleModeFloodPagingRetries.setStatus("current")
_CagwPodRequestsRecv_Type = Counter32
_CagwPodRequestsRecv_Object = MibTableColumn
cagwPodRequestsRecv = _CagwPodRequestsRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 119),
    _CagwPodRequestsRecv_Type()
)
cagwPodRequestsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPodRequestsRecv.setStatus("current")
if mibBuilder.loadTexts:
    cagwPodRequestsRecv.setUnits("requests")
_CagwPodSuccessNotifsSent_Type = Counter32
_CagwPodSuccessNotifsSent_Object = MibTableColumn
cagwPodSuccessNotifsSent = _CagwPodSuccessNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 120),
    _CagwPodSuccessNotifsSent_Type()
)
cagwPodSuccessNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPodSuccessNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwPodSuccessNotifsSent.setUnits("notifications")
_CagwPodFailureNotifsSent_Type = Counter32
_CagwPodFailureNotifsSent_Object = MibTableColumn
cagwPodFailureNotifsSent = _CagwPodFailureNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 121),
    _CagwPodFailureNotifsSent_Type()
)
cagwPodFailureNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPodFailureNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwPodFailureNotifsSent.setUnits("notifications")
_CagwCoaReqRecv_Type = Counter32
_CagwCoaReqRecv_Object = MibTableColumn
cagwCoaReqRecv = _CagwCoaReqRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 122),
    _CagwCoaReqRecv_Type()
)
cagwCoaReqRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCoaReqRecv.setStatus("current")
if mibBuilder.loadTexts:
    cagwCoaReqRecv.setUnits("requests")
_CagwCoaSuccessNotifsSent_Type = Counter32
_CagwCoaSuccessNotifsSent_Object = MibTableColumn
cagwCoaSuccessNotifsSent = _CagwCoaSuccessNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 123),
    _CagwCoaSuccessNotifsSent_Type()
)
cagwCoaSuccessNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCoaSuccessNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwCoaSuccessNotifsSent.setUnits("notifications")
_CagwCoaFailureNotifsSent_Type = Counter32
_CagwCoaFailureNotifsSent_Object = MibTableColumn
cagwCoaFailureNotifsSent = _CagwCoaFailureNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 124),
    _CagwCoaFailureNotifsSent_Type()
)
cagwCoaFailureNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwCoaFailureNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwCoaFailureNotifsSent.setUnits("notifications")
_CagwHotlineUplinkPktDropAclDeny_Type = Counter32
_CagwHotlineUplinkPktDropAclDeny_Object = MibTableColumn
cagwHotlineUplinkPktDropAclDeny = _CagwHotlineUplinkPktDropAclDeny_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 125),
    _CagwHotlineUplinkPktDropAclDeny_Type()
)
cagwHotlineUplinkPktDropAclDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwHotlineUplinkPktDropAclDeny.setStatus("current")
if mibBuilder.loadTexts:
    cagwHotlineUplinkPktDropAclDeny.setUnits("packets")
_CagwHotlineDownlinkPktDropAclDeny_Type = Counter32
_CagwHotlineDownlinkPktDropAclDeny_Object = MibTableColumn
cagwHotlineDownlinkPktDropAclDeny = _CagwHotlineDownlinkPktDropAclDeny_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 126),
    _CagwHotlineDownlinkPktDropAclDeny_Type()
)
cagwHotlineDownlinkPktDropAclDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwHotlineDownlinkPktDropAclDeny.setStatus("current")
if mibBuilder.loadTexts:
    cagwHotlineDownlinkPktDropAclDeny.setUnits("packets")
_CagwUplinkPktDropUsrgrpAclDeny_Type = Counter32
_CagwUplinkPktDropUsrgrpAclDeny_Object = MibTableColumn
cagwUplinkPktDropUsrgrpAclDeny = _CagwUplinkPktDropUsrgrpAclDeny_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 127),
    _CagwUplinkPktDropUsrgrpAclDeny_Type()
)
cagwUplinkPktDropUsrgrpAclDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUplinkPktDropUsrgrpAclDeny.setStatus("current")
if mibBuilder.loadTexts:
    cagwUplinkPktDropUsrgrpAclDeny.setUnits("packets")
_CagwDownlinkPktDropUsrgrpAclDeny_Type = Counter32
_CagwDownlinkPktDropUsrgrpAclDeny_Object = MibTableColumn
cagwDownlinkPktDropUsrgrpAclDeny = _CagwDownlinkPktDropUsrgrpAclDeny_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 128),
    _CagwDownlinkPktDropUsrgrpAclDeny_Type()
)
cagwDownlinkPktDropUsrgrpAclDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDownlinkPktDropUsrgrpAclDeny.setStatus("current")
if mibBuilder.loadTexts:
    cagwDownlinkPktDropUsrgrpAclDeny.setUnits("packets")
_CagwDownlinkPktDropPagingAclDeny_Type = Counter32
_CagwDownlinkPktDropPagingAclDeny_Object = MibTableColumn
cagwDownlinkPktDropPagingAclDeny = _CagwDownlinkPktDropPagingAclDeny_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 1, 1, 1, 129),
    _CagwDownlinkPktDropPagingAclDeny_Type()
)
cagwDownlinkPktDropPagingAclDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDownlinkPktDropPagingAclDeny.setStatus("current")
if mibBuilder.loadTexts:
    cagwDownlinkPktDropPagingAclDeny.setUnits("packets")
_CagwDhcpStatistics_ObjectIdentity = ObjectIdentity
cagwDhcpStatistics = _CagwDhcpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2)
)
_CagwDhcpStatisticsTable_Object = MibTable
cagwDhcpStatisticsTable = _CagwDhcpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cagwDhcpStatisticsTable.setStatus("current")
_CagwDhcpStatisticsEntry_Object = MibTableRow
cagwDhcpStatisticsEntry = _CagwDhcpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1)
)
cagwDhcpStatisticsEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
)
if mibBuilder.loadTexts:
    cagwDhcpStatisticsEntry.setStatus("current")
_CagwDhcpDiscoverPackets_Type = Counter32
_CagwDhcpDiscoverPackets_Object = MibTableColumn
cagwDhcpDiscoverPackets = _CagwDhcpDiscoverPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 1),
    _CagwDhcpDiscoverPackets_Type()
)
cagwDhcpDiscoverPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpDiscoverPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpDiscoverPackets.setUnits("packets")
_CagwDhcpOfferPackets_Type = Counter32
_CagwDhcpOfferPackets_Object = MibTableColumn
cagwDhcpOfferPackets = _CagwDhcpOfferPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 2),
    _CagwDhcpOfferPackets_Type()
)
cagwDhcpOfferPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpOfferPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpOfferPackets.setUnits("packets")
_CagwDhcpRequestPackets_Type = Counter32
_CagwDhcpRequestPackets_Object = MibTableColumn
cagwDhcpRequestPackets = _CagwDhcpRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 3),
    _CagwDhcpRequestPackets_Type()
)
cagwDhcpRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpRequestPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpRequestPackets.setUnits("packets")
_CagwDhcpDeclinePackets_Type = Counter32
_CagwDhcpDeclinePackets_Object = MibTableColumn
cagwDhcpDeclinePackets = _CagwDhcpDeclinePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 4),
    _CagwDhcpDeclinePackets_Type()
)
cagwDhcpDeclinePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpDeclinePackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpDeclinePackets.setUnits("packets")
_CagwDhcpAckPackets_Type = Counter32
_CagwDhcpAckPackets_Object = MibTableColumn
cagwDhcpAckPackets = _CagwDhcpAckPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 5),
    _CagwDhcpAckPackets_Type()
)
cagwDhcpAckPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpAckPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpAckPackets.setUnits("packets")
_CagwDhcpNakPackets_Type = Counter32
_CagwDhcpNakPackets_Object = MibTableColumn
cagwDhcpNakPackets = _CagwDhcpNakPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 6),
    _CagwDhcpNakPackets_Type()
)
cagwDhcpNakPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpNakPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpNakPackets.setUnits("packets")
_CagwDhcpReleasePackets_Type = Counter32
_CagwDhcpReleasePackets_Object = MibTableColumn
cagwDhcpReleasePackets = _CagwDhcpReleasePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 7),
    _CagwDhcpReleasePackets_Type()
)
cagwDhcpReleasePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpReleasePackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpReleasePackets.setUnits("packets")
_CagwDhcpInformPackets_Type = Counter32
_CagwDhcpInformPackets_Object = MibTableColumn
cagwDhcpInformPackets = _CagwDhcpInformPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 8),
    _CagwDhcpInformPackets_Type()
)
cagwDhcpInformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpInformPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpInformPackets.setUnits("packets")
_CagwDhcpLeaseQueryPackets_Type = Counter32
_CagwDhcpLeaseQueryPackets_Object = MibTableColumn
cagwDhcpLeaseQueryPackets = _CagwDhcpLeaseQueryPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 9),
    _CagwDhcpLeaseQueryPackets_Type()
)
cagwDhcpLeaseQueryPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpLeaseQueryPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpLeaseQueryPackets.setUnits("packets")
_CagwDhcpUnknownPackets_Type = Counter32
_CagwDhcpUnknownPackets_Object = MibTableColumn
cagwDhcpUnknownPackets = _CagwDhcpUnknownPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 10),
    _CagwDhcpUnknownPackets_Type()
)
cagwDhcpUnknownPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpUnknownPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpUnknownPackets.setUnits("packets")
_CagwDhcpProxyDiscoverPackets_Type = Counter32
_CagwDhcpProxyDiscoverPackets_Object = MibTableColumn
cagwDhcpProxyDiscoverPackets = _CagwDhcpProxyDiscoverPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 11),
    _CagwDhcpProxyDiscoverPackets_Type()
)
cagwDhcpProxyDiscoverPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyDiscoverPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyDiscoverPackets.setUnits("packets")
_CagwDhcpProxyOfferPackets_Type = Counter32
_CagwDhcpProxyOfferPackets_Object = MibTableColumn
cagwDhcpProxyOfferPackets = _CagwDhcpProxyOfferPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 12),
    _CagwDhcpProxyOfferPackets_Type()
)
cagwDhcpProxyOfferPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyOfferPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyOfferPackets.setUnits("packets")
_CagwDhcpProxyRequestPackets_Type = Counter32
_CagwDhcpProxyRequestPackets_Object = MibTableColumn
cagwDhcpProxyRequestPackets = _CagwDhcpProxyRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 13),
    _CagwDhcpProxyRequestPackets_Type()
)
cagwDhcpProxyRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyRequestPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyRequestPackets.setUnits("packets")
_CagwDhcpProxyDeclinePackets_Type = Counter32
_CagwDhcpProxyDeclinePackets_Object = MibTableColumn
cagwDhcpProxyDeclinePackets = _CagwDhcpProxyDeclinePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 14),
    _CagwDhcpProxyDeclinePackets_Type()
)
cagwDhcpProxyDeclinePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyDeclinePackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyDeclinePackets.setUnits("packets")
_CagwDhcpProxyAckPackets_Type = Counter32
_CagwDhcpProxyAckPackets_Object = MibTableColumn
cagwDhcpProxyAckPackets = _CagwDhcpProxyAckPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 15),
    _CagwDhcpProxyAckPackets_Type()
)
cagwDhcpProxyAckPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyAckPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyAckPackets.setUnits("packets")
_CagwDhcpProxyNakPackets_Type = Counter32
_CagwDhcpProxyNakPackets_Object = MibTableColumn
cagwDhcpProxyNakPackets = _CagwDhcpProxyNakPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 16),
    _CagwDhcpProxyNakPackets_Type()
)
cagwDhcpProxyNakPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyNakPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyNakPackets.setUnits("packets")
_CagwDhcpProxyReleasePackets_Type = Counter32
_CagwDhcpProxyReleasePackets_Object = MibTableColumn
cagwDhcpProxyReleasePackets = _CagwDhcpProxyReleasePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 17),
    _CagwDhcpProxyReleasePackets_Type()
)
cagwDhcpProxyReleasePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyReleasePackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyReleasePackets.setUnits("packets")
_CagwDhcpProxyInformPackets_Type = Counter32
_CagwDhcpProxyInformPackets_Object = MibTableColumn
cagwDhcpProxyInformPackets = _CagwDhcpProxyInformPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 18),
    _CagwDhcpProxyInformPackets_Type()
)
cagwDhcpProxyInformPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyInformPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyInformPackets.setUnits("packets")
_CagwDhcpProxyLeaseQueryPackets_Type = Counter32
_CagwDhcpProxyLeaseQueryPackets_Object = MibTableColumn
cagwDhcpProxyLeaseQueryPackets = _CagwDhcpProxyLeaseQueryPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 19),
    _CagwDhcpProxyLeaseQueryPackets_Type()
)
cagwDhcpProxyLeaseQueryPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyLeaseQueryPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyLeaseQueryPackets.setUnits("packets")
_CagwDhcpProxyUnknownPackets_Type = Counter32
_CagwDhcpProxyUnknownPackets_Object = MibTableColumn
cagwDhcpProxyUnknownPackets = _CagwDhcpProxyUnknownPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 2, 1, 1, 20),
    _CagwDhcpProxyUnknownPackets_Type()
)
cagwDhcpProxyUnknownPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwDhcpProxyUnknownPackets.setStatus("current")
if mibBuilder.loadTexts:
    cagwDhcpProxyUnknownPackets.setUnits("packets")
_CagwMessageStatistics_ObjectIdentity = ObjectIdentity
cagwMessageStatistics = _CagwMessageStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 3)
)
_CagwMsgTable_Object = MibTable
cagwMsgTable = _CagwMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cagwMsgTable.setStatus("current")
_CagwMsgEntry_Object = MibTableRow
cagwMsgEntry = _CagwMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 3, 1, 1)
)
cagwMsgEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwMsgType"),
)
if mibBuilder.loadTexts:
    cagwMsgEntry.setStatus("current")


class _CagwMsgType_Type(Integer32):
    """Custom type cagwMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              21,
              22,
              23,
              31,
              32,
              33,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              51,
              52,
              53,
              61,
              62,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("attachmentAck", 33),
          ("attachmentRequest", 31),
          ("attachmentResponse", 32),
          ("authRelayEapStart", 11),
          ("authRelayEapTransfer", 12),
          ("contextDeliveryAck", 53),
          ("contextDeliveryReport", 52),
          ("contextDeliveryRequest", 51),
          ("datapathDeregAck", 49),
          ("datapathDeregRequest", 47),
          ("datapathDeregResponse", 48),
          ("datapathModifyAck", 46),
          ("datapathModifyRequest", 44),
          ("datapathModifyResponse", 45),
          ("datapathRegAck", 43),
          ("datapathRegRequest", 41),
          ("datapathRegResponse", 42),
          ("handoffDeregAck", 76),
          ("handoffDeregRequest", 74),
          ("handoffDeregResponse", 75),
          ("handoffRegAck", 73),
          ("handoffRegRequest", 71),
          ("handoffRegResponse", 72),
          ("handoffSuccessful", 77),
          ("keepaliveRequest", 61),
          ("keepaliveResponse", 62),
          ("keyChangeAck", 23),
          ("keyChangeConfirm", 22),
          ("keyChangeDirective", 21),
          ("preAttachmentAck", 3),
          ("preAttachmentRequest", 1),
          ("preAttachmentResponse", 2))
    )


_CagwMsgType_Type.__name__ = "Integer32"
_CagwMsgType_Object = MibTableColumn
cagwMsgType = _CagwMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 3, 1, 1, 1),
    _CagwMsgType_Type()
)
cagwMsgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwMsgType.setStatus("current")
_CagwMsgSent_Type = Counter32
_CagwMsgSent_Object = MibTableColumn
cagwMsgSent = _CagwMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 3, 1, 1, 2),
    _CagwMsgSent_Type()
)
cagwMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwMsgSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwMsgSent.setUnits("messages")
_CagwMsgReceived_Type = Counter32
_CagwMsgReceived_Object = MibTableColumn
cagwMsgReceived = _CagwMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 3, 1, 1, 3),
    _CagwMsgReceived_Type()
)
cagwMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    cagwMsgReceived.setUnits("messages")
_CagwMsgResent_Type = Counter32
_CagwMsgResent_Object = MibTableColumn
cagwMsgResent = _CagwMsgResent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 3, 1, 1, 4),
    _CagwMsgResent_Type()
)
cagwMsgResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwMsgResent.setStatus("current")
if mibBuilder.loadTexts:
    cagwMsgResent.setUnits("messages")
_CagwUserGrpStatistics_ObjectIdentity = ObjectIdentity
cagwUserGrpStatistics = _CagwUserGrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4)
)
_CagwUserGrpTable_Object = MibTable
cagwUserGrpTable = _CagwUserGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cagwUserGrpTable.setStatus("current")
_CagwUserGrpEntry_Object = MibTableRow
cagwUserGrpEntry = _CagwUserGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1)
)
cagwUserGrpEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwUserGrpDomainName"),
)
if mibBuilder.loadTexts:
    cagwUserGrpEntry.setStatus("current")


class _CagwUserGrpDomainName_Type(SnmpAdminString):
    """Custom type cagwUserGrpDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CagwUserGrpDomainName_Type.__name__ = "SnmpAdminString"
_CagwUserGrpDomainName_Object = MibTableColumn
cagwUserGrpDomainName = _CagwUserGrpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 1),
    _CagwUserGrpDomainName_Type()
)
cagwUserGrpDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwUserGrpDomainName.setStatus("current")


class _CagwUserGrpServiceMode_Type(Integer32):
    """Custom type cagwUserGrpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("maintenance", 2),
          ("operational", 0))
    )


_CagwUserGrpServiceMode_Type.__name__ = "Integer32"
_CagwUserGrpServiceMode_Object = MibTableColumn
cagwUserGrpServiceMode = _CagwUserGrpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 2),
    _CagwUserGrpServiceMode_Type()
)
cagwUserGrpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpServiceMode.setStatus("current")
_CagwUserGrpCreatedSessions_Type = Counter32
_CagwUserGrpCreatedSessions_Object = MibTableColumn
cagwUserGrpCreatedSessions = _CagwUserGrpCreatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 3),
    _CagwUserGrpCreatedSessions_Type()
)
cagwUserGrpCreatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpCreatedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpCreatedSessions.setUnits("sessions")
_CagwUserGrpDeletedSessions_Type = Counter32
_CagwUserGrpDeletedSessions_Object = MibTableColumn
cagwUserGrpDeletedSessions = _CagwUserGrpDeletedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 4),
    _CagwUserGrpDeletedSessions_Type()
)
cagwUserGrpDeletedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpDeletedSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpDeletedSessions.setUnits("sessions")
_CagwUserGrpCurrentSessions_Type = Gauge32
_CagwUserGrpCurrentSessions_Object = MibTableColumn
cagwUserGrpCurrentSessions = _CagwUserGrpCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 5),
    _CagwUserGrpCurrentSessions_Type()
)
cagwUserGrpCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpCurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpCurrentSessions.setUnits("sessions")
_CagwUserGrpCreatedFlows_Type = Counter32
_CagwUserGrpCreatedFlows_Object = MibTableColumn
cagwUserGrpCreatedFlows = _CagwUserGrpCreatedFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 6),
    _CagwUserGrpCreatedFlows_Type()
)
cagwUserGrpCreatedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpCreatedFlows.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpCreatedFlows.setUnits("flows")
_CagwUserGrpDeletedFlows_Type = Counter32
_CagwUserGrpDeletedFlows_Object = MibTableColumn
cagwUserGrpDeletedFlows = _CagwUserGrpDeletedFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 7),
    _CagwUserGrpDeletedFlows_Type()
)
cagwUserGrpDeletedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpDeletedFlows.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpDeletedFlows.setUnits("flows")
_CagwUserGrpCurrentFlows_Type = Gauge32
_CagwUserGrpCurrentFlows_Object = MibTableColumn
cagwUserGrpCurrentFlows = _CagwUserGrpCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 8),
    _CagwUserGrpCurrentFlows_Type()
)
cagwUserGrpCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpCurrentFlows.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpCurrentFlows.setUnits("flows")
_CagwUserGrpPacketsSent_Type = Counter32
_CagwUserGrpPacketsSent_Object = MibTableColumn
cagwUserGrpPacketsSent = _CagwUserGrpPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 9),
    _CagwUserGrpPacketsSent_Type()
)
cagwUserGrpPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpPacketsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwUserGrpPacketsSent.setUnits("packets")
_CagwUserGrpBytesSent_Type = Counter64
_CagwUserGrpBytesSent_Object = MibTableColumn
cagwUserGrpBytesSent = _CagwUserGrpBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 10),
    _CagwUserGrpBytesSent_Type()
)
cagwUserGrpBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpBytesSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwUserGrpBytesSent.setUnits("bytes")
_CagwUserGrpPacketsReceived_Type = Counter32
_CagwUserGrpPacketsReceived_Object = MibTableColumn
cagwUserGrpPacketsReceived = _CagwUserGrpPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 11),
    _CagwUserGrpPacketsReceived_Type()
)
cagwUserGrpPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpPacketsReceived.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwUserGrpPacketsReceived.setUnits("packets")
_CagwUserGrpBytesReceived_Type = Counter64
_CagwUserGrpBytesReceived_Object = MibTableColumn
cagwUserGrpBytesReceived = _CagwUserGrpBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 12),
    _CagwUserGrpBytesReceived_Type()
)
cagwUserGrpBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpBytesReceived.setStatus("deprecated")
if mibBuilder.loadTexts:
    cagwUserGrpBytesReceived.setUnits("bytes")
_CagwUserGrpInvalidSourcePacketsDrops_Type = Counter32
_CagwUserGrpInvalidSourcePacketsDrops_Object = MibTableColumn
cagwUserGrpInvalidSourcePacketsDrops = _CagwUserGrpInvalidSourcePacketsDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 13),
    _CagwUserGrpInvalidSourcePacketsDrops_Type()
)
cagwUserGrpInvalidSourcePacketsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpInvalidSourcePacketsDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpInvalidSourcePacketsDrops.setUnits("packets")
_CagwUserGrpInvalidSourceBytesDrops_Type = Counter32
_CagwUserGrpInvalidSourceBytesDrops_Object = MibTableColumn
cagwUserGrpInvalidSourceBytesDrops = _CagwUserGrpInvalidSourceBytesDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 14),
    _CagwUserGrpInvalidSourceBytesDrops_Type()
)
cagwUserGrpInvalidSourceBytesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpInvalidSourceBytesDrops.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpInvalidSourceBytesDrops.setUnits("bytes")
_CagwUserGrpIpGrePacketsSent_Type = Counter32
_CagwUserGrpIpGrePacketsSent_Object = MibTableColumn
cagwUserGrpIpGrePacketsSent = _CagwUserGrpIpGrePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 15),
    _CagwUserGrpIpGrePacketsSent_Type()
)
cagwUserGrpIpGrePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpIpGrePacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpIpGrePacketsSent.setUnits("packets")
_CagwUserGrpIpGreBytesSent_Type = Counter64
_CagwUserGrpIpGreBytesSent_Object = MibTableColumn
cagwUserGrpIpGreBytesSent = _CagwUserGrpIpGreBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 16),
    _CagwUserGrpIpGreBytesSent_Type()
)
cagwUserGrpIpGreBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpIpGreBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpIpGreBytesSent.setUnits("bytes")
_CagwUserGrpIpGrePacketsReceived_Type = Counter32
_CagwUserGrpIpGrePacketsReceived_Object = MibTableColumn
cagwUserGrpIpGrePacketsReceived = _CagwUserGrpIpGrePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 17),
    _CagwUserGrpIpGrePacketsReceived_Type()
)
cagwUserGrpIpGrePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpIpGrePacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpIpGrePacketsReceived.setUnits("packets")
_CagwUserGrpIpGreBytesReceived_Type = Counter64
_CagwUserGrpIpGreBytesReceived_Object = MibTableColumn
cagwUserGrpIpGreBytesReceived = _CagwUserGrpIpGreBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 18),
    _CagwUserGrpIpGreBytesReceived_Type()
)
cagwUserGrpIpGreBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpIpGreBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpIpGreBytesReceived.setUnits("bytes")
_CagwUserGrpEthGrePacketsSent_Type = Counter32
_CagwUserGrpEthGrePacketsSent_Object = MibTableColumn
cagwUserGrpEthGrePacketsSent = _CagwUserGrpEthGrePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 19),
    _CagwUserGrpEthGrePacketsSent_Type()
)
cagwUserGrpEthGrePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpEthGrePacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpEthGrePacketsSent.setUnits("packets")
_CagwUserGrpEthGreBytesSent_Type = Counter64
_CagwUserGrpEthGreBytesSent_Object = MibTableColumn
cagwUserGrpEthGreBytesSent = _CagwUserGrpEthGreBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 20),
    _CagwUserGrpEthGreBytesSent_Type()
)
cagwUserGrpEthGreBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpEthGreBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpEthGreBytesSent.setUnits("bytes")
_CagwUserGrpEthGrePacketsReceived_Type = Counter32
_CagwUserGrpEthGrePacketsReceived_Object = MibTableColumn
cagwUserGrpEthGrePacketsReceived = _CagwUserGrpEthGrePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 21),
    _CagwUserGrpEthGrePacketsReceived_Type()
)
cagwUserGrpEthGrePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpEthGrePacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpEthGrePacketsReceived.setUnits("packets")
_CagwUserGrpEthGreBytesReceived_Type = Counter64
_CagwUserGrpEthGreBytesReceived_Object = MibTableColumn
cagwUserGrpEthGreBytesReceived = _CagwUserGrpEthGreBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 22),
    _CagwUserGrpEthGreBytesReceived_Type()
)
cagwUserGrpEthGreBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpEthGreBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpEthGreBytesReceived.setUnits("bytes")
_CagwUserGrpOverwritten_Type = Counter32
_CagwUserGrpOverwritten_Object = MibTableColumn
cagwUserGrpOverwritten = _CagwUserGrpOverwritten_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 23),
    _CagwUserGrpOverwritten_Type()
)
cagwUserGrpOverwritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpOverwritten.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpOverwritten.setUnits("number")
_CagwUserGrpPodReqRecv_Type = Counter32
_CagwUserGrpPodReqRecv_Object = MibTableColumn
cagwUserGrpPodReqRecv = _CagwUserGrpPodReqRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 24),
    _CagwUserGrpPodReqRecv_Type()
)
cagwUserGrpPodReqRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpPodReqRecv.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpPodReqRecv.setUnits("requests")
_CagwUserGrpPodSuccessNotifsSent_Type = Counter32
_CagwUserGrpPodSuccessNotifsSent_Object = MibTableColumn
cagwUserGrpPodSuccessNotifsSent = _CagwUserGrpPodSuccessNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 25),
    _CagwUserGrpPodSuccessNotifsSent_Type()
)
cagwUserGrpPodSuccessNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpPodSuccessNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpPodSuccessNotifsSent.setUnits("notifications")
_CagwUserGrpPodFailureNotifsSent_Type = Counter32
_CagwUserGrpPodFailureNotifsSent_Object = MibTableColumn
cagwUserGrpPodFailureNotifsSent = _CagwUserGrpPodFailureNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 26),
    _CagwUserGrpPodFailureNotifsSent_Type()
)
cagwUserGrpPodFailureNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpPodFailureNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpPodFailureNotifsSent.setUnits("notifications")
_CagwUserGrpCoaReqRecv_Type = Counter32
_CagwUserGrpCoaReqRecv_Object = MibTableColumn
cagwUserGrpCoaReqRecv = _CagwUserGrpCoaReqRecv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 27),
    _CagwUserGrpCoaReqRecv_Type()
)
cagwUserGrpCoaReqRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpCoaReqRecv.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpCoaReqRecv.setUnits("requests")
_CagwUserGrpCoaSuccessNotifsSent_Type = Counter32
_CagwUserGrpCoaSuccessNotifsSent_Object = MibTableColumn
cagwUserGrpCoaSuccessNotifsSent = _CagwUserGrpCoaSuccessNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 28),
    _CagwUserGrpCoaSuccessNotifsSent_Type()
)
cagwUserGrpCoaSuccessNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpCoaSuccessNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpCoaSuccessNotifsSent.setUnits("notifications")
_CagwUserGrpCoaFailureNotifsSent_Type = Counter32
_CagwUserGrpCoaFailureNotifsSent_Object = MibTableColumn
cagwUserGrpCoaFailureNotifsSent = _CagwUserGrpCoaFailureNotifsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 29),
    _CagwUserGrpCoaFailureNotifsSent_Type()
)
cagwUserGrpCoaFailureNotifsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpCoaFailureNotifsSent.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpCoaFailureNotifsSent.setUnits("notifications")
_CagwUserGrpRejSession_Type = Counter32
_CagwUserGrpRejSession_Object = MibTableColumn
cagwUserGrpRejSession = _CagwUserGrpRejSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 4, 1, 1, 30),
    _CagwUserGrpRejSession_Type()
)
cagwUserGrpRejSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwUserGrpRejSession.setStatus("current")
if mibBuilder.loadTexts:
    cagwUserGrpRejSession.setUnits("sessions")
_CagwPathStatistics_ObjectIdentity = ObjectIdentity
cagwPathStatistics = _CagwPathStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5)
)
_CagwPathTable_Object = MibTable
cagwPathTable = _CagwPathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cagwPathTable.setStatus("obsolete")
_CagwPathEntry_Object = MibTableRow
cagwPathEntry = _CagwPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1)
)
cagwPathEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwPathRemoteIpType"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwPathRemoteIp"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwPathType"),
)
if mibBuilder.loadTexts:
    cagwPathEntry.setStatus("obsolete")
_CagwPathRemoteIpType_Type = InetAddressType
_CagwPathRemoteIpType_Object = MibTableColumn
cagwPathRemoteIpType = _CagwPathRemoteIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 1),
    _CagwPathRemoteIpType_Type()
)
cagwPathRemoteIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwPathRemoteIpType.setStatus("obsolete")


class _CagwPathRemoteIp_Type(InetAddress):
    """Custom type cagwPathRemoteIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CagwPathRemoteIp_Type.__name__ = "InetAddress"
_CagwPathRemoteIp_Object = MibTableColumn
cagwPathRemoteIp = _CagwPathRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 2),
    _CagwPathRemoteIp_Type()
)
cagwPathRemoteIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwPathRemoteIp.setStatus("obsolete")


class _CagwPathType_Type(Integer32):
    """Custom type cagwPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("signaling", 1))
    )


_CagwPathType_Type.__name__ = "Integer32"
_CagwPathType_Object = MibTableColumn
cagwPathType = _CagwPathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 3),
    _CagwPathType_Type()
)
cagwPathType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwPathType.setStatus("obsolete")
_CagwPathLocalIpType_Type = InetAddressType
_CagwPathLocalIpType_Object = MibTableColumn
cagwPathLocalIpType = _CagwPathLocalIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 4),
    _CagwPathLocalIpType_Type()
)
cagwPathLocalIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathLocalIpType.setStatus("obsolete")
_CagwPathLocalIp_Type = InetAddress
_CagwPathLocalIp_Object = MibTableColumn
cagwPathLocalIp = _CagwPathLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 5),
    _CagwPathLocalIp_Type()
)
cagwPathLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathLocalIp.setStatus("obsolete")
_CagwPathCurrentSessions_Type = Gauge32
_CagwPathCurrentSessions_Object = MibTableColumn
cagwPathCurrentSessions = _CagwPathCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 6),
    _CagwPathCurrentSessions_Type()
)
cagwPathCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathCurrentSessions.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwPathCurrentSessions.setUnits("sessions")
_CagwPathCurrentFlows_Type = Gauge32
_CagwPathCurrentFlows_Object = MibTableColumn
cagwPathCurrentFlows = _CagwPathCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 7),
    _CagwPathCurrentFlows_Type()
)
cagwPathCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathCurrentFlows.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwPathCurrentFlows.setUnits("flows")
_CagwPathPacketsSent_Type = Counter32
_CagwPathPacketsSent_Object = MibTableColumn
cagwPathPacketsSent = _CagwPathPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 8),
    _CagwPathPacketsSent_Type()
)
cagwPathPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathPacketsSent.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwPathPacketsSent.setUnits("packets")
_CagwPathBytesSent_Type = Counter64
_CagwPathBytesSent_Object = MibTableColumn
cagwPathBytesSent = _CagwPathBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 9),
    _CagwPathBytesSent_Type()
)
cagwPathBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathBytesSent.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwPathBytesSent.setUnits("bytes")
_CagwPathPacketsReceived_Type = Counter32
_CagwPathPacketsReceived_Object = MibTableColumn
cagwPathPacketsReceived = _CagwPathPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 10),
    _CagwPathPacketsReceived_Type()
)
cagwPathPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathPacketsReceived.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwPathPacketsReceived.setUnits("packets")
_CagwPathBytesReceived_Type = Counter64
_CagwPathBytesReceived_Object = MibTableColumn
cagwPathBytesReceived = _CagwPathBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 1, 1, 11),
    _CagwPathBytesReceived_Type()
)
cagwPathBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathBytesReceived.setStatus("obsolete")
if mibBuilder.loadTexts:
    cagwPathBytesReceived.setUnits("bytes")
_CagwPathRev1Table_Object = MibTable
cagwPathRev1Table = _CagwPathRev1Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    cagwPathRev1Table.setStatus("current")
_CagwPathRev1Entry_Object = MibTableRow
cagwPathRev1Entry = _CagwPathRev1Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1)
)
cagwPathRev1Entry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwPathTypeRev1"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwPathRemoteIpTypeRev1"),
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwPathRemoteIpRev1"),
)
if mibBuilder.loadTexts:
    cagwPathRev1Entry.setStatus("current")


class _CagwPathTypeRev1_Type(Integer32):
    """Custom type cagwPathTypeRev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("signaling", 1))
    )


_CagwPathTypeRev1_Type.__name__ = "Integer32"
_CagwPathTypeRev1_Object = MibTableColumn
cagwPathTypeRev1 = _CagwPathTypeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 1),
    _CagwPathTypeRev1_Type()
)
cagwPathTypeRev1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwPathTypeRev1.setStatus("current")
_CagwPathRemoteIpTypeRev1_Type = InetAddressType
_CagwPathRemoteIpTypeRev1_Object = MibTableColumn
cagwPathRemoteIpTypeRev1 = _CagwPathRemoteIpTypeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 2),
    _CagwPathRemoteIpTypeRev1_Type()
)
cagwPathRemoteIpTypeRev1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwPathRemoteIpTypeRev1.setStatus("current")


class _CagwPathRemoteIpRev1_Type(InetAddress):
    """Custom type cagwPathRemoteIpRev1 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_CagwPathRemoteIpRev1_Type.__name__ = "InetAddress"
_CagwPathRemoteIpRev1_Object = MibTableColumn
cagwPathRemoteIpRev1 = _CagwPathRemoteIpRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 3),
    _CagwPathRemoteIpRev1_Type()
)
cagwPathRemoteIpRev1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cagwPathRemoteIpRev1.setStatus("current")
_CagwPathLocalIpTypeRev1_Type = InetAddressType
_CagwPathLocalIpTypeRev1_Object = MibTableColumn
cagwPathLocalIpTypeRev1 = _CagwPathLocalIpTypeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 4),
    _CagwPathLocalIpTypeRev1_Type()
)
cagwPathLocalIpTypeRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathLocalIpTypeRev1.setStatus("current")
_CagwPathLocalIpRev1_Type = InetAddress
_CagwPathLocalIpRev1_Object = MibTableColumn
cagwPathLocalIpRev1 = _CagwPathLocalIpRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 5),
    _CagwPathLocalIpRev1_Type()
)
cagwPathLocalIpRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathLocalIpRev1.setStatus("current")
_CagwPathCurrentSessionsRev1_Type = Gauge32
_CagwPathCurrentSessionsRev1_Object = MibTableColumn
cagwPathCurrentSessionsRev1 = _CagwPathCurrentSessionsRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 6),
    _CagwPathCurrentSessionsRev1_Type()
)
cagwPathCurrentSessionsRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathCurrentSessionsRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathCurrentSessionsRev1.setUnits("sessions")
_CagwPathCurrentFlowsRev1_Type = Gauge32
_CagwPathCurrentFlowsRev1_Object = MibTableColumn
cagwPathCurrentFlowsRev1 = _CagwPathCurrentFlowsRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 7),
    _CagwPathCurrentFlowsRev1_Type()
)
cagwPathCurrentFlowsRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathCurrentFlowsRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathCurrentFlowsRev1.setUnits("flows")
_CagwPathIpGrePacketsSentRev1_Type = Counter32
_CagwPathIpGrePacketsSentRev1_Object = MibTableColumn
cagwPathIpGrePacketsSentRev1 = _CagwPathIpGrePacketsSentRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 8),
    _CagwPathIpGrePacketsSentRev1_Type()
)
cagwPathIpGrePacketsSentRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathIpGrePacketsSentRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathIpGrePacketsSentRev1.setUnits("packets")
_CagwPathIpGreBytesSentRev1_Type = Counter64
_CagwPathIpGreBytesSentRev1_Object = MibTableColumn
cagwPathIpGreBytesSentRev1 = _CagwPathIpGreBytesSentRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 9),
    _CagwPathIpGreBytesSentRev1_Type()
)
cagwPathIpGreBytesSentRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathIpGreBytesSentRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathIpGreBytesSentRev1.setUnits("bytes")
_CagwPathIpGrePacketsReceivedRev1_Type = Counter32
_CagwPathIpGrePacketsReceivedRev1_Object = MibTableColumn
cagwPathIpGrePacketsReceivedRev1 = _CagwPathIpGrePacketsReceivedRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 10),
    _CagwPathIpGrePacketsReceivedRev1_Type()
)
cagwPathIpGrePacketsReceivedRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathIpGrePacketsReceivedRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathIpGrePacketsReceivedRev1.setUnits("packets")
_CagwPathIpGreBytesReceivedRev1_Type = Counter64
_CagwPathIpGreBytesReceivedRev1_Object = MibTableColumn
cagwPathIpGreBytesReceivedRev1 = _CagwPathIpGreBytesReceivedRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 11),
    _CagwPathIpGreBytesReceivedRev1_Type()
)
cagwPathIpGreBytesReceivedRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathIpGreBytesReceivedRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathIpGreBytesReceivedRev1.setUnits("bytes")
_CagwPathEthGrePacketsSentRev1_Type = Counter32
_CagwPathEthGrePacketsSentRev1_Object = MibTableColumn
cagwPathEthGrePacketsSentRev1 = _CagwPathEthGrePacketsSentRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 12),
    _CagwPathEthGrePacketsSentRev1_Type()
)
cagwPathEthGrePacketsSentRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathEthGrePacketsSentRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathEthGrePacketsSentRev1.setUnits("packets")
_CagwPathEthGreBytesSentRev1_Type = Counter64
_CagwPathEthGreBytesSentRev1_Object = MibTableColumn
cagwPathEthGreBytesSentRev1 = _CagwPathEthGreBytesSentRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 13),
    _CagwPathEthGreBytesSentRev1_Type()
)
cagwPathEthGreBytesSentRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathEthGreBytesSentRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathEthGreBytesSentRev1.setUnits("bytes")
_CagwPathEthGrePacketsReceivedRev1_Type = Counter32
_CagwPathEthGrePacketsReceivedRev1_Object = MibTableColumn
cagwPathEthGrePacketsReceivedRev1 = _CagwPathEthGrePacketsReceivedRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 14),
    _CagwPathEthGrePacketsReceivedRev1_Type()
)
cagwPathEthGrePacketsReceivedRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathEthGrePacketsReceivedRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathEthGrePacketsReceivedRev1.setUnits("packets")
_CagwPathEthGreBytesReceivedRev1_Type = Counter64
_CagwPathEthGreBytesReceivedRev1_Object = MibTableColumn
cagwPathEthGreBytesReceivedRev1 = _CagwPathEthGreBytesReceivedRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 5, 2, 1, 15),
    _CagwPathEthGreBytesReceivedRev1_Type()
)
cagwPathEthGreBytesReceivedRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwPathEthGreBytesReceivedRev1.setStatus("current")
if mibBuilder.loadTexts:
    cagwPathEthGreBytesReceivedRev1.setUnits("bytes")
_CagwArpStatistics_ObjectIdentity = ObjectIdentity
cagwArpStatistics = _CagwArpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 6)
)
_CagwArpStatisticsTable_Object = MibTable
cagwArpStatisticsTable = _CagwArpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    cagwArpStatisticsTable.setStatus("current")
_CagwArpStatisticsEntry_Object = MibTableRow
cagwArpStatisticsEntry = _CagwArpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 6, 1, 1)
)
cagwArpStatisticsEntry.setIndexNames(
    (0, "CISCO-ASN-GATEWAY-MIB", "cagwInstanceIndex"),
)
if mibBuilder.loadTexts:
    cagwArpStatisticsEntry.setStatus("current")
_CagwArpReqReceived_Type = Counter32
_CagwArpReqReceived_Object = MibTableColumn
cagwArpReqReceived = _CagwArpReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 6, 1, 1, 1),
    _CagwArpReqReceived_Type()
)
cagwArpReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwArpReqReceived.setStatus("current")
if mibBuilder.loadTexts:
    cagwArpReqReceived.setUnits("packets")
_CagwArpReplySent_Type = Counter32
_CagwArpReplySent_Object = MibTableColumn
cagwArpReplySent = _CagwArpReplySent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 6, 1, 1, 2),
    _CagwArpReplySent_Type()
)
cagwArpReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwArpReplySent.setStatus("current")
if mibBuilder.loadTexts:
    cagwArpReplySent.setUnits("packets")
_CagwArpPacketsDropped_Type = Counter32
_CagwArpPacketsDropped_Object = MibTableColumn
cagwArpPacketsDropped = _CagwArpPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 3, 6, 1, 1, 3),
    _CagwArpPacketsDropped_Type()
)
cagwArpPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwArpPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    cagwArpPacketsDropped.setUnits("packets")
_CagwNotifMgmt_ObjectIdentity = ObjectIdentity
cagwNotifMgmt = _CagwNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4)
)


class _CagwNotifEnabled_Type(TruthValue):
    """Custom type cagwNotifEnabled based on TruthValue"""


_CagwNotifEnabled_Object = MibScalar
cagwNotifEnabled = _CagwNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 1),
    _CagwNotifEnabled_Type()
)
cagwNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwNotifEnabled.setStatus("current")


class _CagwNotifSeverityLevel_Type(CiscoAlarmSeverity):
    """Custom type cagwNotifSeverityLevel based on CiscoAlarmSeverity"""


_CagwNotifSeverityLevel_Object = MibScalar
cagwNotifSeverityLevel = _CagwNotifSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 2),
    _CagwNotifSeverityLevel_Type()
)
cagwNotifSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwNotifSeverityLevel.setStatus("current")


class _CagwRepeatNotifInterval_Type(Integer32):
    """Custom type cagwRepeatNotifInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_CagwRepeatNotifInterval_Type.__name__ = "Integer32"
_CagwRepeatNotifInterval_Object = MibScalar
cagwRepeatNotifInterval = _CagwRepeatNotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 3),
    _CagwRepeatNotifInterval_Type()
)
cagwRepeatNotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwRepeatNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    cagwRepeatNotifInterval.setUnits("seconds")
_CagwGeneratedNotifs_Type = Counter32
_CagwGeneratedNotifs_Object = MibScalar
cagwGeneratedNotifs = _CagwGeneratedNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 4),
    _CagwGeneratedNotifs_Type()
)
cagwGeneratedNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwGeneratedNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwGeneratedNotifs.setUnits("notifications")
_CagwIgnoredNotifs_Type = Counter32
_CagwIgnoredNotifs_Object = MibScalar
cagwIgnoredNotifs = _CagwIgnoredNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 5),
    _CagwIgnoredNotifs_Type()
)
cagwIgnoredNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIgnoredNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwIgnoredNotifs.setUnits("notifications")


class _CagwServiceNotifEnabled_Type(TruthValue):
    """Custom type cagwServiceNotifEnabled based on TruthValue"""


_CagwServiceNotifEnabled_Object = MibScalar
cagwServiceNotifEnabled = _CagwServiceNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 11),
    _CagwServiceNotifEnabled_Type()
)
cagwServiceNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwServiceNotifEnabled.setStatus("current")


class _CagwServiceNotifSeverity_Type(CiscoAlarmSeverity):
    """Custom type cagwServiceNotifSeverity based on CiscoAlarmSeverity"""


_CagwServiceNotifSeverity_Object = MibScalar
cagwServiceNotifSeverity = _CagwServiceNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 12),
    _CagwServiceNotifSeverity_Type()
)
cagwServiceNotifSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwServiceNotifSeverity.setStatus("current")
_CagwGeneratedServiceNotifs_Type = Counter32
_CagwGeneratedServiceNotifs_Object = MibScalar
cagwGeneratedServiceNotifs = _CagwGeneratedServiceNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 13),
    _CagwGeneratedServiceNotifs_Type()
)
cagwGeneratedServiceNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwGeneratedServiceNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwGeneratedServiceNotifs.setUnits("notifications")
_CagwIgnoredServiceNotifs_Type = Counter32
_CagwIgnoredServiceNotifs_Object = MibScalar
cagwIgnoredServiceNotifs = _CagwIgnoredServiceNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 14),
    _CagwIgnoredServiceNotifs_Type()
)
cagwIgnoredServiceNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIgnoredServiceNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwIgnoredServiceNotifs.setUnits("notifications")


class _CagwMaxBaseStationExceededNotifEnabled_Type(TruthValue):
    """Custom type cagwMaxBaseStationExceededNotifEnabled based on TruthValue"""


_CagwMaxBaseStationExceededNotifEnabled_Object = MibScalar
cagwMaxBaseStationExceededNotifEnabled = _CagwMaxBaseStationExceededNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 21),
    _CagwMaxBaseStationExceededNotifEnabled_Type()
)
cagwMaxBaseStationExceededNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaxBaseStationExceededNotifEnabled.setStatus("current")


class _CagwMaxBaseStationExceededNotifSeverity_Type(CiscoAlarmSeverity):
    """Custom type cagwMaxBaseStationExceededNotifSeverity based on CiscoAlarmSeverity"""


_CagwMaxBaseStationExceededNotifSeverity_Object = MibScalar
cagwMaxBaseStationExceededNotifSeverity = _CagwMaxBaseStationExceededNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 22),
    _CagwMaxBaseStationExceededNotifSeverity_Type()
)
cagwMaxBaseStationExceededNotifSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaxBaseStationExceededNotifSeverity.setStatus("current")


class _CagwMaxBaseStationExceededNotifThreshold_Type(Integer32):
    """Custom type cagwMaxBaseStationExceededNotifThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )


_CagwMaxBaseStationExceededNotifThreshold_Type.__name__ = "Integer32"
_CagwMaxBaseStationExceededNotifThreshold_Object = MibScalar
cagwMaxBaseStationExceededNotifThreshold = _CagwMaxBaseStationExceededNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 23),
    _CagwMaxBaseStationExceededNotifThreshold_Type()
)
cagwMaxBaseStationExceededNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaxBaseStationExceededNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cagwMaxBaseStationExceededNotifThreshold.setUnits("percent")
_CagwGeneratedMaxBsNotifs_Type = Counter32
_CagwGeneratedMaxBsNotifs_Object = MibScalar
cagwGeneratedMaxBsNotifs = _CagwGeneratedMaxBsNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 24),
    _CagwGeneratedMaxBsNotifs_Type()
)
cagwGeneratedMaxBsNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwGeneratedMaxBsNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwGeneratedMaxBsNotifs.setUnits("notifications")
_CagwIgnoredMaxBsNotifs_Type = Counter32
_CagwIgnoredMaxBsNotifs_Object = MibScalar
cagwIgnoredMaxBsNotifs = _CagwIgnoredMaxBsNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 25),
    _CagwIgnoredMaxBsNotifs_Type()
)
cagwIgnoredMaxBsNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIgnoredMaxBsNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwIgnoredMaxBsNotifs.setUnits("notifications")


class _CagwMaxSubscribersExceededNotifEnabled_Type(TruthValue):
    """Custom type cagwMaxSubscribersExceededNotifEnabled based on TruthValue"""


_CagwMaxSubscribersExceededNotifEnabled_Object = MibScalar
cagwMaxSubscribersExceededNotifEnabled = _CagwMaxSubscribersExceededNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 31),
    _CagwMaxSubscribersExceededNotifEnabled_Type()
)
cagwMaxSubscribersExceededNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaxSubscribersExceededNotifEnabled.setStatus("current")


class _CagwMaxSubscribersExceededNotifSeverity_Type(CiscoAlarmSeverity):
    """Custom type cagwMaxSubscribersExceededNotifSeverity based on CiscoAlarmSeverity"""


_CagwMaxSubscribersExceededNotifSeverity_Object = MibScalar
cagwMaxSubscribersExceededNotifSeverity = _CagwMaxSubscribersExceededNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 32),
    _CagwMaxSubscribersExceededNotifSeverity_Type()
)
cagwMaxSubscribersExceededNotifSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaxSubscribersExceededNotifSeverity.setStatus("current")


class _CagwMaxSubscribersExceededNotifThreshold_Type(Integer32):
    """Custom type cagwMaxSubscribersExceededNotifThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )


_CagwMaxSubscribersExceededNotifThreshold_Type.__name__ = "Integer32"
_CagwMaxSubscribersExceededNotifThreshold_Object = MibScalar
cagwMaxSubscribersExceededNotifThreshold = _CagwMaxSubscribersExceededNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 33),
    _CagwMaxSubscribersExceededNotifThreshold_Type()
)
cagwMaxSubscribersExceededNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cagwMaxSubscribersExceededNotifThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cagwMaxSubscribersExceededNotifThreshold.setUnits("percent")
_CagwGeneratedMaxSubscNotifs_Type = Counter32
_CagwGeneratedMaxSubscNotifs_Object = MibScalar
cagwGeneratedMaxSubscNotifs = _CagwGeneratedMaxSubscNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 34),
    _CagwGeneratedMaxSubscNotifs_Type()
)
cagwGeneratedMaxSubscNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwGeneratedMaxSubscNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwGeneratedMaxSubscNotifs.setUnits("notifications")
_CagwIgnoredMaxSubscNotifs_Type = Counter32
_CagwIgnoredMaxSubscNotifs_Object = MibScalar
cagwIgnoredMaxSubscNotifs = _CagwIgnoredMaxSubscNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 4, 35),
    _CagwIgnoredMaxSubscNotifs_Type()
)
cagwIgnoredMaxSubscNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwIgnoredMaxSubscNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cagwIgnoredMaxSubscNotifs.setUnits("notifications")
_CagwNotifInfo_ObjectIdentity = ObjectIdentity
cagwNotifInfo = _CagwNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 5)
)
_CagwImpactedIpType_Type = InetAddressType
_CagwImpactedIpType_Object = MibScalar
cagwImpactedIpType = _CagwImpactedIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 5, 1),
    _CagwImpactedIpType_Type()
)
cagwImpactedIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwImpactedIpType.setStatus("current")
_CagwImpactedIp_Type = InetAddress
_CagwImpactedIp_Object = MibScalar
cagwImpactedIp = _CagwImpactedIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 5, 2),
    _CagwImpactedIp_Type()
)
cagwImpactedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwImpactedIp.setStatus("current")


class _CagwImpactedReason_Type(Integer32):
    """Custom type cagwImpactedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("limit", 1),
          ("unknown", 0))
    )


_CagwImpactedReason_Type.__name__ = "Integer32"
_CagwImpactedReason_Object = MibScalar
cagwImpactedReason = _CagwImpactedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 5, 3),
    _CagwImpactedReason_Type()
)
cagwImpactedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwImpactedReason.setStatus("current")
_CagwImpactedInfo_Type = SnmpAdminString
_CagwImpactedInfo_Object = MibScalar
cagwImpactedInfo = _CagwImpactedInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 1, 5, 4),
    _CagwImpactedInfo_Type()
)
cagwImpactedInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cagwImpactedInfo.setStatus("current")
_CiscoAgwMIBConform_ObjectIdentity = ObjectIdentity
ciscoAgwMIBConform = _CiscoAgwMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2)
)
_CiscoAgwMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAgwMIBCompliances = _CiscoAgwMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 1)
)
_CiscoAgwMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAgwMIBGroups = _CiscoAgwMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2)
)

# Managed Objects groups

cagwInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 1)
)
cagwInstanceGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwInstancePhysicalIndex"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInstanceDescription"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInstanceVersion"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInstanceOperState"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInstanceSessionRedundancyAdmin"))
)
if mibBuilder.loadTexts:
    cagwInstanceGroup.setStatus("current")

cagwStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 2)
)
cagwStateGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwMaximumBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaximumSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaximumFlowsPerSession"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentDataPaths"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwNetworkBehindMs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPendingSignalingPkts"))
)
if mibBuilder.loadTexts:
    cagwStateGroup.setStatus("current")

cagwGlobalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 3)
)
cagwGlobalStatisticsGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwCreatedSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedDataPaths"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedDataPaths"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwProcessedSignalingPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRequeuedSignalingPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCongestionSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceDisabledSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceNotReadySignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEncapErrorSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDisposedSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEncapErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInvalidAddressDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceDisabledDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInvalidProtocolTypeDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwLengthErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwAbsentKeyDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowPathNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowPathInvalidSourceDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSessionNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSubscriberNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwChecksumErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIngressFilteringDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSequenceNumberErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFragmentedDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFramedRouteInserted"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFramedRouteInsertFailed"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFramedRouteDeleted"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceFlowProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwQosProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwClassifierProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwReceivedDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwReceivedDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSentDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSentDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSessionsDeletedByAgw"))
)
if mibBuilder.loadTexts:
    cagwGlobalStatisticsGroup.setStatus("obsolete")

cagwDhcpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 4)
)
cagwDhcpStatisticsGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwDhcpDiscoverPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpOfferPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpRequestPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpDeclinePackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpAckPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpNakPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpReleasePackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpInformPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpLeaseQueryPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpUnknownPackets"))
)
if mibBuilder.loadTexts:
    cagwDhcpStatisticsGroup.setStatus("current")

cagwMessageStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 5)
)
cagwMessageStatisticsGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwMsgSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMsgReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMsgResent"))
)
if mibBuilder.loadTexts:
    cagwMessageStatisticsGroup.setStatus("current")

cagwUserGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 6)
)
cagwUserGrpGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpServiceMode"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCreatedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpDeletedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCurrentSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCreatedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpDeletedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCurrentFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpPacketsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpBytesSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpPacketsReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpBytesReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpInvalidSourcePacketsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpInvalidSourceBytesDrops"))
)
if mibBuilder.loadTexts:
    cagwUserGrpGroup.setStatus("deprecated")

cagwPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 7)
)
cagwPathGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwPathLocalIpType"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathLocalIp"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathCurrentSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathCurrentFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathPacketsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathBytesSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathPacketsReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathBytesReceived"))
)
if mibBuilder.loadTexts:
    cagwPathGroup.setStatus("obsolete")

cagwNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 8)
)
cagwNotifInfoGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwImpactedIpType"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedIp"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedReason"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedInfo"))
)
if mibBuilder.loadTexts:
    cagwNotifInfoGroup.setStatus("current")

cagwNotifMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 9)
)
cagwNotifMgmtGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwNotifEnabled"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwNotifSeverityLevel"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRepeatNotifInterval"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwGeneratedNotifs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIgnoredNotifs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceNotifEnabled"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceNotifSeverity"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwGeneratedServiceNotifs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIgnoredServiceNotifs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxBaseStationExceededNotifEnabled"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxBaseStationExceededNotifSeverity"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxBaseStationExceededNotifThreshold"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwGeneratedMaxBsNotifs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIgnoredMaxBsNotifs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxSubscribersExceededNotifEnabled"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxSubscribersExceededNotifSeverity"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxSubscribersExceededNotifThreshold"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwGeneratedMaxSubscNotifs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIgnoredMaxSubscNotifs"))
)
if mibBuilder.loadTexts:
    cagwNotifMgmtGroup.setStatus("current")

cagwGlobalStatisticsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 11)
)
cagwGlobalStatisticsGroupRev1.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwCreatedSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedDataPaths"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedDataPaths"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwProcessedSignalingPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRequeuedSignalingPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCongestionSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceDisabledSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceNotReadySignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEncapErrorSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDisposedSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEncapErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInvalidAddressDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceDisabledDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInvalidProtocolTypeDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwLengthErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwAbsentKeyDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowPathNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowPathInvalidSourceDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSessionNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSubscriberNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwChecksumErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIngressFilteringDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSequenceNumberErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFragmentedDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFramedRouteInserted"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFramedRouteInsertFailed"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFramedRouteDeleted"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceFlowProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwQosProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwClassifierProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSessionsDeletedByAgw"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreSentDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreSentDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreSentDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreSentDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwAgedOutStaticHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSuccessfulHandoff"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFailedHandoff"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSuccessfulCMACKeyUpdate"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFailedCMACKeyUpdate"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSuccessfulSecurityKeyExchange"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFailedSecurityKeyExchange"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedRedirectedPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedRedirectedBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedRedirectedPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedRedirectedBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwThrottlingOfPuntsDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwLearningUpstreamDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPuntedDataPkts"))
)
if mibBuilder.loadTexts:
    cagwGlobalStatisticsGroupRev1.setStatus("obsolete")

cagwUserGrpGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 12)
)
cagwUserGrpGroupRev1.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpServiceMode"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCreatedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpDeletedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCurrentSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCreatedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpDeletedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCurrentFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpInvalidSourcePacketsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpInvalidSourceBytesDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpIpGrePacketsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpIpGreBytesSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpIpGrePacketsReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpIpGreBytesReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpEthGrePacketsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpEthGreBytesSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpEthGrePacketsReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpEthGreBytesReceived"))
)
if mibBuilder.loadTexts:
    cagwUserGrpGroupRev1.setStatus("current")

cagwPathGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 13)
)
cagwPathGroupRev1.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwPathLocalIpTypeRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathLocalIpRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathCurrentSessionsRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathCurrentFlowsRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathIpGrePacketsSentRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathIpGreBytesSentRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathIpGrePacketsReceivedRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathIpGreBytesReceivedRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathEthGrePacketsSentRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathEthGreBytesSentRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathEthGrePacketsReceivedRev1"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPathEthGreBytesReceivedRev1"))
)
if mibBuilder.loadTexts:
    cagwPathGroupRev1.setStatus("current")

cagwArpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 14)
)
cagwArpStatisticsGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwArpReqReceived"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwArpReplySent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwArpPacketsDropped"))
)
if mibBuilder.loadTexts:
    cagwArpStatisticsGroup.setStatus("current")

cagwStateGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 15)
)
cagwStateGroupSup1.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwCurrentFramedRoutes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentFramedRouteSubs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentAutoProvSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentSessionsWithIpPktsRedir"))
)
if mibBuilder.loadTexts:
    cagwStateGroupSup1.setStatus("current")

cagwGlobalStatisticsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 16)
)
cagwGlobalStatisticsGroupRev2.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwCreatedSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedDataPaths"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedDataPaths"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwProcessedSignalingPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRequeuedSignalingPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCongestionSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceDisabledSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceNotReadySignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEncapErrorSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDisposedSignalingPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEncapErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInvalidAddressDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceDisabledDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwInvalidProtocolTypeDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwLengthErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwAbsentKeyDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowPathNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFlowPathInvalidSourceDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSessionNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSubscriberNotFoundDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwChecksumErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIngressFilteringDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSequenceNumberErrorDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFragmentedDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceFlowProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwQosProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwClassifierProfileNotFound"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedFlows"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSessionsDeletedByAgw"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreSentDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreSentDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreSentDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreSentDataBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwAgedOutStaticHosts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSuccessfulHandoff"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFailedHandoff"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSuccessfulCMACKeyUpdate"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFailedCMACKeyUpdate"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSuccessfulSecurityKeyExchange"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwFailedSecurityKeyExchange"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedRedirectedPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIpGreReceivedRedirectedBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedRedirectedPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwEthGreReceivedRedirectedBytes"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwThrottlingOfPuntsDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwLearningUpstreamDataPktsDrops"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPuntedDataPkts"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedSessionUnapprovedBs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPktsDroppedStaticIpHostNotAllowed"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPktsDroppedMulticastBroadcast"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwSlaProfileNotFound"))
)
if mibBuilder.loadTexts:
    cagwGlobalStatisticsGroupRev2.setStatus("current")

cagwUserGrpGroupRev1Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 17)
)
cagwUserGrpGroupRev1Sup1.setObjects(
    ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpOverwritten")
)
if mibBuilder.loadTexts:
    cagwUserGrpGroupRev1Sup1.setStatus("current")

cagwStateGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 18)
)
cagwStateGroupSup2.setObjects(
    ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentPmipEnabledSubs")
)
if mibBuilder.loadTexts:
    cagwStateGroupSup2.setStatus("current")

cagwUserGrpGroupRev1Sup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 19)
)
cagwUserGrpGroupRev1Sup2.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpPodReqRecv"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpPodSuccessNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpPodFailureNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCoaReqRecv"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCoaSuccessNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpCoaFailureNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUserGrpRejSession"))
)
if mibBuilder.loadTexts:
    cagwUserGrpGroupRev1Sup2.setStatus("current")

cagwGlobalStatisticsGroupRev2Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 20)
)
cagwGlobalStatisticsGroupRev2Sup1.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwPktsDroppedMipIncomplete"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCreatedPmipEnabledSubs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDeletedPmipEnabledSubs"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPktsDropPmipStaticIpHost"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeEntryMsBsInitiated"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeEntryBwgInitiated"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeEntryFailures"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeExitMsBsInitiated"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeExitBwgInitiated"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeExitFailures"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeLocUpdtPgidChange"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeLocUpdtPowerDown"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeLocUpdtPeriodic"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeLocUpdtFailures"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModePageAttemptsDwnlnkData"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModePageFailuresDwnlnkData"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModePageAttemptsLocUpdt"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModePageFailuresLocUpdt"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeDirectedPagingSuccess"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeDirectedPagingRetries"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeFloodPagingSuccess"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwIdleModeFloodPagingRetries"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPodRequestsRecv"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPodSuccessNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwPodFailureNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCoaReqRecv"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCoaSuccessNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCoaFailureNotifsSent"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwHotlineUplinkPktDropAclDeny"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwHotlineDownlinkPktDropAclDeny"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwUplinkPktDropUsrgrpAclDeny"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDownlinkPktDropUsrgrpAclDeny"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDownlinkPktDropPagingAclDeny"))
)
if mibBuilder.loadTexts:
    cagwGlobalStatisticsGroupRev2Sup1.setStatus("current")

cagwDhcpProxyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 21)
)
cagwDhcpProxyStatsGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyDiscoverPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyOfferPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyRequestPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyDeclinePackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyAckPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyNakPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyReleasePackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyInformPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyLeaseQueryPackets"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwDhcpProxyUnknownPackets"))
)
if mibBuilder.loadTexts:
    cagwDhcpProxyStatsGroup.setStatus("current")


# Notification objects

ciscoAgwServiceDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 0, 1)
)
ciscoAgwServiceDownNotif.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwInstanceDescription"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceNotifSeverity"))
)
if mibBuilder.loadTexts:
    ciscoAgwServiceDownNotif.setStatus(
        "current"
    )

ciscoAgwServiceUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 0, 2)
)
ciscoAgwServiceUpNotif.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwInstanceDescription"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwServiceNotifSeverity"))
)
if mibBuilder.loadTexts:
    ciscoAgwServiceUpNotif.setStatus(
        "current"
    )

ciscoAgwMaxBaseStationExceededOnsetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 0, 3)
)
ciscoAgwMaxBaseStationExceededOnsetNotif.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwInstanceDescription"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxBaseStationExceededNotifSeverity"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaximumBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedIpType"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedIp"))
)
if mibBuilder.loadTexts:
    ciscoAgwMaxBaseStationExceededOnsetNotif.setStatus(
        "current"
    )

ciscoAgwMaxBaseStationExceededAbateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 0, 4)
)
ciscoAgwMaxBaseStationExceededAbateNotif.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwInstanceDescription"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxBaseStationExceededNotifSeverity"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaximumBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentBaseStations"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedBaseStations"))
)
if mibBuilder.loadTexts:
    ciscoAgwMaxBaseStationExceededAbateNotif.setStatus(
        "current"
    )

ciscoAgwMaxSubscribersExceededOnsetNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 0, 5)
)
ciscoAgwMaxSubscribersExceededOnsetNotif.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwInstanceDescription"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxSubscribersExceededNotifSeverity"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaximumSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedSessions"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedIpType"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedIp"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwImpactedInfo"))
)
if mibBuilder.loadTexts:
    ciscoAgwMaxSubscribersExceededOnsetNotif.setStatus(
        "current"
    )

ciscoAgwMaxSubscribersExceededAbateNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 0, 6)
)
ciscoAgwMaxSubscribersExceededAbateNotif.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "cagwInstanceDescription"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaxSubscribersExceededNotifSeverity"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwMaximumSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwCurrentSubscribers"),
        ("CISCO-ASN-GATEWAY-MIB", "cagwRejectedSessions"))
)
if mibBuilder.loadTexts:
    ciscoAgwMaxSubscribersExceededAbateNotif.setStatus(
        "current"
    )


# Notifications groups

cagwNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 2, 10)
)
cagwNotifGroup.setObjects(
      *(("CISCO-ASN-GATEWAY-MIB", "ciscoAgwServiceDownNotif"),
        ("CISCO-ASN-GATEWAY-MIB", "ciscoAgwServiceUpNotif"),
        ("CISCO-ASN-GATEWAY-MIB", "ciscoAgwMaxBaseStationExceededOnsetNotif"),
        ("CISCO-ASN-GATEWAY-MIB", "ciscoAgwMaxBaseStationExceededAbateNotif"),
        ("CISCO-ASN-GATEWAY-MIB", "ciscoAgwMaxSubscribersExceededOnsetNotif"),
        ("CISCO-ASN-GATEWAY-MIB", "ciscoAgwMaxSubscribersExceededAbateNotif"))
)
if mibBuilder.loadTexts:
    cagwNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoAgwMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAgwMIBCompliance.setStatus(
        "obsolete"
    )

ciscoAgwMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAgwMIBComplianceRev1.setStatus(
        "obsolete"
    )

ciscoAgwMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAgwMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoAgwMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 638, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoAgwMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ASN-GATEWAY-MIB",
    **{"ciscoAgwMIB": ciscoAgwMIB,
       "ciscoAgwMIBNotifs": ciscoAgwMIBNotifs,
       "ciscoAgwServiceDownNotif": ciscoAgwServiceDownNotif,
       "ciscoAgwServiceUpNotif": ciscoAgwServiceUpNotif,
       "ciscoAgwMaxBaseStationExceededOnsetNotif": ciscoAgwMaxBaseStationExceededOnsetNotif,
       "ciscoAgwMaxBaseStationExceededAbateNotif": ciscoAgwMaxBaseStationExceededAbateNotif,
       "ciscoAgwMaxSubscribersExceededOnsetNotif": ciscoAgwMaxSubscribersExceededOnsetNotif,
       "ciscoAgwMaxSubscribersExceededAbateNotif": ciscoAgwMaxSubscribersExceededAbateNotif,
       "ciscoAgwMIBObjects": ciscoAgwMIBObjects,
       "cagwInstances": cagwInstances,
       "cagwInstanceTable": cagwInstanceTable,
       "cagwInstanceEntry": cagwInstanceEntry,
       "cagwInstanceIndex": cagwInstanceIndex,
       "cagwInstancePhysicalIndex": cagwInstancePhysicalIndex,
       "cagwInstanceDescription": cagwInstanceDescription,
       "cagwInstanceVersion": cagwInstanceVersion,
       "cagwInstanceOperState": cagwInstanceOperState,
       "cagwInstanceSessionRedundancyAdmin": cagwInstanceSessionRedundancyAdmin,
       "cagwState": cagwState,
       "cagwStateTable": cagwStateTable,
       "cagwStateEntry": cagwStateEntry,
       "cagwMaximumBaseStations": cagwMaximumBaseStations,
       "cagwMaximumSubscribers": cagwMaximumSubscribers,
       "cagwMaximumFlowsPerSession": cagwMaximumFlowsPerSession,
       "cagwCurrentBaseStations": cagwCurrentBaseStations,
       "cagwCurrentDataPaths": cagwCurrentDataPaths,
       "cagwCurrentSubscribers": cagwCurrentSubscribers,
       "cagwCurrentSessions": cagwCurrentSessions,
       "cagwCurrentFlows": cagwCurrentFlows,
       "cagwCurrentHosts": cagwCurrentHosts,
       "cagwNetworkBehindMs": cagwNetworkBehindMs,
       "cagwPendingSignalingPkts": cagwPendingSignalingPkts,
       "cagwCurrentFramedRoutes": cagwCurrentFramedRoutes,
       "cagwCurrentFramedRouteSubs": cagwCurrentFramedRouteSubs,
       "cagwCurrentAutoProvSessions": cagwCurrentAutoProvSessions,
       "cagwCurrentSessionsWithIpPktsRedir": cagwCurrentSessionsWithIpPktsRedir,
       "cagwCurrentPmipEnabledSubs": cagwCurrentPmipEnabledSubs,
       "cagwStatistics": cagwStatistics,
       "cagwGlobalStatistics": cagwGlobalStatistics,
       "cagwGlobalStatisticsTable": cagwGlobalStatisticsTable,
       "cagwGlobalStatisticsEntry": cagwGlobalStatisticsEntry,
       "cagwCreatedSubscribers": cagwCreatedSubscribers,
       "cagwDeletedSubscribers": cagwDeletedSubscribers,
       "cagwCreatedSessions": cagwCreatedSessions,
       "cagwDeletedSessions": cagwDeletedSessions,
       "cagwCreatedFlows": cagwCreatedFlows,
       "cagwDeletedFlows": cagwDeletedFlows,
       "cagwCreatedHosts": cagwCreatedHosts,
       "cagwDeletedHosts": cagwDeletedHosts,
       "cagwCreatedBaseStations": cagwCreatedBaseStations,
       "cagwDeletedBaseStations": cagwDeletedBaseStations,
       "cagwCreatedDataPaths": cagwCreatedDataPaths,
       "cagwDeletedDataPaths": cagwDeletedDataPaths,
       "cagwProcessedSignalingPkts": cagwProcessedSignalingPkts,
       "cagwRequeuedSignalingPkts": cagwRequeuedSignalingPkts,
       "cagwCongestionSignalingPktsDrops": cagwCongestionSignalingPktsDrops,
       "cagwServiceDisabledSignalingPktsDrops": cagwServiceDisabledSignalingPktsDrops,
       "cagwServiceNotReadySignalingPktsDrops": cagwServiceNotReadySignalingPktsDrops,
       "cagwEncapErrorSignalingPktsDrops": cagwEncapErrorSignalingPktsDrops,
       "cagwDisposedSignalingPktsDrops": cagwDisposedSignalingPktsDrops,
       "cagwEncapErrorDataPktsDrops": cagwEncapErrorDataPktsDrops,
       "cagwInvalidAddressDataPktsDrops": cagwInvalidAddressDataPktsDrops,
       "cagwServiceDisabledDataPktsDrops": cagwServiceDisabledDataPktsDrops,
       "cagwInvalidProtocolTypeDataPktsDrops": cagwInvalidProtocolTypeDataPktsDrops,
       "cagwLengthErrorDataPktsDrops": cagwLengthErrorDataPktsDrops,
       "cagwAbsentKeyDataPktsDrops": cagwAbsentKeyDataPktsDrops,
       "cagwFlowNotFoundDataPktsDrops": cagwFlowNotFoundDataPktsDrops,
       "cagwFlowPathNotFoundDataPktsDrops": cagwFlowPathNotFoundDataPktsDrops,
       "cagwFlowPathInvalidSourceDataPktsDrops": cagwFlowPathInvalidSourceDataPktsDrops,
       "cagwSessionNotFoundDataPktsDrops": cagwSessionNotFoundDataPktsDrops,
       "cagwSubscriberNotFoundDataPktsDrops": cagwSubscriberNotFoundDataPktsDrops,
       "cagwChecksumErrorDataPktsDrops": cagwChecksumErrorDataPktsDrops,
       "cagwIngressFilteringDataPktsDrops": cagwIngressFilteringDataPktsDrops,
       "cagwSequenceNumberErrorDataPktsDrops": cagwSequenceNumberErrorDataPktsDrops,
       "cagwFragmentedDataPktsDrops": cagwFragmentedDataPktsDrops,
       "cagwFramedRouteInserted": cagwFramedRouteInserted,
       "cagwFramedRouteInsertFailed": cagwFramedRouteInsertFailed,
       "cagwFramedRouteDeleted": cagwFramedRouteDeleted,
       "cagwServiceFlowProfileNotFound": cagwServiceFlowProfileNotFound,
       "cagwQosProfileNotFound": cagwQosProfileNotFound,
       "cagwClassifierProfileNotFound": cagwClassifierProfileNotFound,
       "cagwReceivedDataPkts": cagwReceivedDataPkts,
       "cagwReceivedDataBytes": cagwReceivedDataBytes,
       "cagwSentDataPkts": cagwSentDataPkts,
       "cagwSentDataBytes": cagwSentDataBytes,
       "cagwRejectedSessions": cagwRejectedSessions,
       "cagwRejectedFlows": cagwRejectedFlows,
       "cagwRejectedBaseStations": cagwRejectedBaseStations,
       "cagwSessionsDeletedByAgw": cagwSessionsDeletedByAgw,
       "cagwIpGreReceivedDataPkts": cagwIpGreReceivedDataPkts,
       "cagwIpGreReceivedDataBytes": cagwIpGreReceivedDataBytes,
       "cagwIpGreSentDataPkts": cagwIpGreSentDataPkts,
       "cagwIpGreSentDataBytes": cagwIpGreSentDataBytes,
       "cagwEthGreReceivedDataPkts": cagwEthGreReceivedDataPkts,
       "cagwEthGreReceivedDataBytes": cagwEthGreReceivedDataBytes,
       "cagwEthGreSentDataPkts": cagwEthGreSentDataPkts,
       "cagwEthGreSentDataBytes": cagwEthGreSentDataBytes,
       "cagwRejectedHosts": cagwRejectedHosts,
       "cagwAgedOutStaticHosts": cagwAgedOutStaticHosts,
       "cagwSuccessfulHandoff": cagwSuccessfulHandoff,
       "cagwFailedHandoff": cagwFailedHandoff,
       "cagwSuccessfulCMACKeyUpdate": cagwSuccessfulCMACKeyUpdate,
       "cagwFailedCMACKeyUpdate": cagwFailedCMACKeyUpdate,
       "cagwSuccessfulSecurityKeyExchange": cagwSuccessfulSecurityKeyExchange,
       "cagwFailedSecurityKeyExchange": cagwFailedSecurityKeyExchange,
       "cagwIpGreReceivedRedirectedPkts": cagwIpGreReceivedRedirectedPkts,
       "cagwIpGreReceivedRedirectedBytes": cagwIpGreReceivedRedirectedBytes,
       "cagwEthGreReceivedRedirectedPkts": cagwEthGreReceivedRedirectedPkts,
       "cagwEthGreReceivedRedirectedBytes": cagwEthGreReceivedRedirectedBytes,
       "cagwThrottlingOfPuntsDataPktsDrops": cagwThrottlingOfPuntsDataPktsDrops,
       "cagwLearningUpstreamDataPktsDrops": cagwLearningUpstreamDataPktsDrops,
       "cagwPuntedDataPkts": cagwPuntedDataPkts,
       "cagwRejectedSessionUnapprovedBs": cagwRejectedSessionUnapprovedBs,
       "cagwPktsDroppedStaticIpHostNotAllowed": cagwPktsDroppedStaticIpHostNotAllowed,
       "cagwPktsDroppedMulticastBroadcast": cagwPktsDroppedMulticastBroadcast,
       "cagwSlaProfileNotFound": cagwSlaProfileNotFound,
       "cagwPktsDroppedMipIncomplete": cagwPktsDroppedMipIncomplete,
       "cagwCreatedPmipEnabledSubs": cagwCreatedPmipEnabledSubs,
       "cagwDeletedPmipEnabledSubs": cagwDeletedPmipEnabledSubs,
       "cagwPktsDropPmipStaticIpHost": cagwPktsDropPmipStaticIpHost,
       "cagwIdleModeEntryMsBsInitiated": cagwIdleModeEntryMsBsInitiated,
       "cagwIdleModeEntryBwgInitiated": cagwIdleModeEntryBwgInitiated,
       "cagwIdleModeEntryFailures": cagwIdleModeEntryFailures,
       "cagwIdleModeExitMsBsInitiated": cagwIdleModeExitMsBsInitiated,
       "cagwIdleModeExitBwgInitiated": cagwIdleModeExitBwgInitiated,
       "cagwIdleModeExitFailures": cagwIdleModeExitFailures,
       "cagwIdleModeLocUpdtPgidChange": cagwIdleModeLocUpdtPgidChange,
       "cagwIdleModeLocUpdtPowerDown": cagwIdleModeLocUpdtPowerDown,
       "cagwIdleModeLocUpdtPeriodic": cagwIdleModeLocUpdtPeriodic,
       "cagwIdleModeLocUpdtFailures": cagwIdleModeLocUpdtFailures,
       "cagwIdleModePageAttemptsDwnlnkData": cagwIdleModePageAttemptsDwnlnkData,
       "cagwIdleModePageFailuresDwnlnkData": cagwIdleModePageFailuresDwnlnkData,
       "cagwIdleModePageAttemptsLocUpdt": cagwIdleModePageAttemptsLocUpdt,
       "cagwIdleModePageFailuresLocUpdt": cagwIdleModePageFailuresLocUpdt,
       "cagwIdleModeDirectedPagingSuccess": cagwIdleModeDirectedPagingSuccess,
       "cagwIdleModeDirectedPagingRetries": cagwIdleModeDirectedPagingRetries,
       "cagwIdleModeFloodPagingSuccess": cagwIdleModeFloodPagingSuccess,
       "cagwIdleModeFloodPagingRetries": cagwIdleModeFloodPagingRetries,
       "cagwPodRequestsRecv": cagwPodRequestsRecv,
       "cagwPodSuccessNotifsSent": cagwPodSuccessNotifsSent,
       "cagwPodFailureNotifsSent": cagwPodFailureNotifsSent,
       "cagwCoaReqRecv": cagwCoaReqRecv,
       "cagwCoaSuccessNotifsSent": cagwCoaSuccessNotifsSent,
       "cagwCoaFailureNotifsSent": cagwCoaFailureNotifsSent,
       "cagwHotlineUplinkPktDropAclDeny": cagwHotlineUplinkPktDropAclDeny,
       "cagwHotlineDownlinkPktDropAclDeny": cagwHotlineDownlinkPktDropAclDeny,
       "cagwUplinkPktDropUsrgrpAclDeny": cagwUplinkPktDropUsrgrpAclDeny,
       "cagwDownlinkPktDropUsrgrpAclDeny": cagwDownlinkPktDropUsrgrpAclDeny,
       "cagwDownlinkPktDropPagingAclDeny": cagwDownlinkPktDropPagingAclDeny,
       "cagwDhcpStatistics": cagwDhcpStatistics,
       "cagwDhcpStatisticsTable": cagwDhcpStatisticsTable,
       "cagwDhcpStatisticsEntry": cagwDhcpStatisticsEntry,
       "cagwDhcpDiscoverPackets": cagwDhcpDiscoverPackets,
       "cagwDhcpOfferPackets": cagwDhcpOfferPackets,
       "cagwDhcpRequestPackets": cagwDhcpRequestPackets,
       "cagwDhcpDeclinePackets": cagwDhcpDeclinePackets,
       "cagwDhcpAckPackets": cagwDhcpAckPackets,
       "cagwDhcpNakPackets": cagwDhcpNakPackets,
       "cagwDhcpReleasePackets": cagwDhcpReleasePackets,
       "cagwDhcpInformPackets": cagwDhcpInformPackets,
       "cagwDhcpLeaseQueryPackets": cagwDhcpLeaseQueryPackets,
       "cagwDhcpUnknownPackets": cagwDhcpUnknownPackets,
       "cagwDhcpProxyDiscoverPackets": cagwDhcpProxyDiscoverPackets,
       "cagwDhcpProxyOfferPackets": cagwDhcpProxyOfferPackets,
       "cagwDhcpProxyRequestPackets": cagwDhcpProxyRequestPackets,
       "cagwDhcpProxyDeclinePackets": cagwDhcpProxyDeclinePackets,
       "cagwDhcpProxyAckPackets": cagwDhcpProxyAckPackets,
       "cagwDhcpProxyNakPackets": cagwDhcpProxyNakPackets,
       "cagwDhcpProxyReleasePackets": cagwDhcpProxyReleasePackets,
       "cagwDhcpProxyInformPackets": cagwDhcpProxyInformPackets,
       "cagwDhcpProxyLeaseQueryPackets": cagwDhcpProxyLeaseQueryPackets,
       "cagwDhcpProxyUnknownPackets": cagwDhcpProxyUnknownPackets,
       "cagwMessageStatistics": cagwMessageStatistics,
       "cagwMsgTable": cagwMsgTable,
       "cagwMsgEntry": cagwMsgEntry,
       "cagwMsgType": cagwMsgType,
       "cagwMsgSent": cagwMsgSent,
       "cagwMsgReceived": cagwMsgReceived,
       "cagwMsgResent": cagwMsgResent,
       "cagwUserGrpStatistics": cagwUserGrpStatistics,
       "cagwUserGrpTable": cagwUserGrpTable,
       "cagwUserGrpEntry": cagwUserGrpEntry,
       "cagwUserGrpDomainName": cagwUserGrpDomainName,
       "cagwUserGrpServiceMode": cagwUserGrpServiceMode,
       "cagwUserGrpCreatedSessions": cagwUserGrpCreatedSessions,
       "cagwUserGrpDeletedSessions": cagwUserGrpDeletedSessions,
       "cagwUserGrpCurrentSessions": cagwUserGrpCurrentSessions,
       "cagwUserGrpCreatedFlows": cagwUserGrpCreatedFlows,
       "cagwUserGrpDeletedFlows": cagwUserGrpDeletedFlows,
       "cagwUserGrpCurrentFlows": cagwUserGrpCurrentFlows,
       "cagwUserGrpPacketsSent": cagwUserGrpPacketsSent,
       "cagwUserGrpBytesSent": cagwUserGrpBytesSent,
       "cagwUserGrpPacketsReceived": cagwUserGrpPacketsReceived,
       "cagwUserGrpBytesReceived": cagwUserGrpBytesReceived,
       "cagwUserGrpInvalidSourcePacketsDrops": cagwUserGrpInvalidSourcePacketsDrops,
       "cagwUserGrpInvalidSourceBytesDrops": cagwUserGrpInvalidSourceBytesDrops,
       "cagwUserGrpIpGrePacketsSent": cagwUserGrpIpGrePacketsSent,
       "cagwUserGrpIpGreBytesSent": cagwUserGrpIpGreBytesSent,
       "cagwUserGrpIpGrePacketsReceived": cagwUserGrpIpGrePacketsReceived,
       "cagwUserGrpIpGreBytesReceived": cagwUserGrpIpGreBytesReceived,
       "cagwUserGrpEthGrePacketsSent": cagwUserGrpEthGrePacketsSent,
       "cagwUserGrpEthGreBytesSent": cagwUserGrpEthGreBytesSent,
       "cagwUserGrpEthGrePacketsReceived": cagwUserGrpEthGrePacketsReceived,
       "cagwUserGrpEthGreBytesReceived": cagwUserGrpEthGreBytesReceived,
       "cagwUserGrpOverwritten": cagwUserGrpOverwritten,
       "cagwUserGrpPodReqRecv": cagwUserGrpPodReqRecv,
       "cagwUserGrpPodSuccessNotifsSent": cagwUserGrpPodSuccessNotifsSent,
       "cagwUserGrpPodFailureNotifsSent": cagwUserGrpPodFailureNotifsSent,
       "cagwUserGrpCoaReqRecv": cagwUserGrpCoaReqRecv,
       "cagwUserGrpCoaSuccessNotifsSent": cagwUserGrpCoaSuccessNotifsSent,
       "cagwUserGrpCoaFailureNotifsSent": cagwUserGrpCoaFailureNotifsSent,
       "cagwUserGrpRejSession": cagwUserGrpRejSession,
       "cagwPathStatistics": cagwPathStatistics,
       "cagwPathTable": cagwPathTable,
       "cagwPathEntry": cagwPathEntry,
       "cagwPathRemoteIpType": cagwPathRemoteIpType,
       "cagwPathRemoteIp": cagwPathRemoteIp,
       "cagwPathType": cagwPathType,
       "cagwPathLocalIpType": cagwPathLocalIpType,
       "cagwPathLocalIp": cagwPathLocalIp,
       "cagwPathCurrentSessions": cagwPathCurrentSessions,
       "cagwPathCurrentFlows": cagwPathCurrentFlows,
       "cagwPathPacketsSent": cagwPathPacketsSent,
       "cagwPathBytesSent": cagwPathBytesSent,
       "cagwPathPacketsReceived": cagwPathPacketsReceived,
       "cagwPathBytesReceived": cagwPathBytesReceived,
       "cagwPathRev1Table": cagwPathRev1Table,
       "cagwPathRev1Entry": cagwPathRev1Entry,
       "cagwPathTypeRev1": cagwPathTypeRev1,
       "cagwPathRemoteIpTypeRev1": cagwPathRemoteIpTypeRev1,
       "cagwPathRemoteIpRev1": cagwPathRemoteIpRev1,
       "cagwPathLocalIpTypeRev1": cagwPathLocalIpTypeRev1,
       "cagwPathLocalIpRev1": cagwPathLocalIpRev1,
       "cagwPathCurrentSessionsRev1": cagwPathCurrentSessionsRev1,
       "cagwPathCurrentFlowsRev1": cagwPathCurrentFlowsRev1,
       "cagwPathIpGrePacketsSentRev1": cagwPathIpGrePacketsSentRev1,
       "cagwPathIpGreBytesSentRev1": cagwPathIpGreBytesSentRev1,
       "cagwPathIpGrePacketsReceivedRev1": cagwPathIpGrePacketsReceivedRev1,
       "cagwPathIpGreBytesReceivedRev1": cagwPathIpGreBytesReceivedRev1,
       "cagwPathEthGrePacketsSentRev1": cagwPathEthGrePacketsSentRev1,
       "cagwPathEthGreBytesSentRev1": cagwPathEthGreBytesSentRev1,
       "cagwPathEthGrePacketsReceivedRev1": cagwPathEthGrePacketsReceivedRev1,
       "cagwPathEthGreBytesReceivedRev1": cagwPathEthGreBytesReceivedRev1,
       "cagwArpStatistics": cagwArpStatistics,
       "cagwArpStatisticsTable": cagwArpStatisticsTable,
       "cagwArpStatisticsEntry": cagwArpStatisticsEntry,
       "cagwArpReqReceived": cagwArpReqReceived,
       "cagwArpReplySent": cagwArpReplySent,
       "cagwArpPacketsDropped": cagwArpPacketsDropped,
       "cagwNotifMgmt": cagwNotifMgmt,
       "cagwNotifEnabled": cagwNotifEnabled,
       "cagwNotifSeverityLevel": cagwNotifSeverityLevel,
       "cagwRepeatNotifInterval": cagwRepeatNotifInterval,
       "cagwGeneratedNotifs": cagwGeneratedNotifs,
       "cagwIgnoredNotifs": cagwIgnoredNotifs,
       "cagwServiceNotifEnabled": cagwServiceNotifEnabled,
       "cagwServiceNotifSeverity": cagwServiceNotifSeverity,
       "cagwGeneratedServiceNotifs": cagwGeneratedServiceNotifs,
       "cagwIgnoredServiceNotifs": cagwIgnoredServiceNotifs,
       "cagwMaxBaseStationExceededNotifEnabled": cagwMaxBaseStationExceededNotifEnabled,
       "cagwMaxBaseStationExceededNotifSeverity": cagwMaxBaseStationExceededNotifSeverity,
       "cagwMaxBaseStationExceededNotifThreshold": cagwMaxBaseStationExceededNotifThreshold,
       "cagwGeneratedMaxBsNotifs": cagwGeneratedMaxBsNotifs,
       "cagwIgnoredMaxBsNotifs": cagwIgnoredMaxBsNotifs,
       "cagwMaxSubscribersExceededNotifEnabled": cagwMaxSubscribersExceededNotifEnabled,
       "cagwMaxSubscribersExceededNotifSeverity": cagwMaxSubscribersExceededNotifSeverity,
       "cagwMaxSubscribersExceededNotifThreshold": cagwMaxSubscribersExceededNotifThreshold,
       "cagwGeneratedMaxSubscNotifs": cagwGeneratedMaxSubscNotifs,
       "cagwIgnoredMaxSubscNotifs": cagwIgnoredMaxSubscNotifs,
       "cagwNotifInfo": cagwNotifInfo,
       "cagwImpactedIpType": cagwImpactedIpType,
       "cagwImpactedIp": cagwImpactedIp,
       "cagwImpactedReason": cagwImpactedReason,
       "cagwImpactedInfo": cagwImpactedInfo,
       "ciscoAgwMIBConform": ciscoAgwMIBConform,
       "ciscoAgwMIBCompliances": ciscoAgwMIBCompliances,
       "ciscoAgwMIBCompliance": ciscoAgwMIBCompliance,
       "ciscoAgwMIBComplianceRev1": ciscoAgwMIBComplianceRev1,
       "ciscoAgwMIBComplianceRev2": ciscoAgwMIBComplianceRev2,
       "ciscoAgwMIBComplianceRev3": ciscoAgwMIBComplianceRev3,
       "ciscoAgwMIBGroups": ciscoAgwMIBGroups,
       "cagwInstanceGroup": cagwInstanceGroup,
       "cagwStateGroup": cagwStateGroup,
       "cagwGlobalStatisticsGroup": cagwGlobalStatisticsGroup,
       "cagwDhcpStatisticsGroup": cagwDhcpStatisticsGroup,
       "cagwMessageStatisticsGroup": cagwMessageStatisticsGroup,
       "cagwUserGrpGroup": cagwUserGrpGroup,
       "cagwPathGroup": cagwPathGroup,
       "cagwNotifInfoGroup": cagwNotifInfoGroup,
       "cagwNotifMgmtGroup": cagwNotifMgmtGroup,
       "cagwNotifGroup": cagwNotifGroup,
       "cagwGlobalStatisticsGroupRev1": cagwGlobalStatisticsGroupRev1,
       "cagwUserGrpGroupRev1": cagwUserGrpGroupRev1,
       "cagwPathGroupRev1": cagwPathGroupRev1,
       "cagwArpStatisticsGroup": cagwArpStatisticsGroup,
       "cagwStateGroupSup1": cagwStateGroupSup1,
       "cagwGlobalStatisticsGroupRev2": cagwGlobalStatisticsGroupRev2,
       "cagwUserGrpGroupRev1Sup1": cagwUserGrpGroupRev1Sup1,
       "cagwStateGroupSup2": cagwStateGroupSup2,
       "cagwUserGrpGroupRev1Sup2": cagwUserGrpGroupRev1Sup2,
       "cagwGlobalStatisticsGroupRev2Sup1": cagwGlobalStatisticsGroupRev2Sup1,
       "cagwDhcpProxyStatsGroup": cagwDhcpProxyStatsGroup}
)
