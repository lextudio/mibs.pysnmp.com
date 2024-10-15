# SNMP MIB module (QUANTA-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QUANTA-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:05 2024
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

(switch,) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "switch")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

quantaBGP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentBGPQueueGroup_ObjectIdentity = ObjectIdentity
agentBGPQueueGroup = _AgentBGPQueueGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1)
)
_AgentBGPQueueTable_Object = MibTable
agentBGPQueueTable = _AgentBGPQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    agentBGPQueueTable.setStatus("current")
_AgentBGPQueueEntry_Object = MibTableRow
agentBGPQueueEntry = _AgentBGPQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1, 1)
)
agentBGPQueueEntry.setIndexNames(
    (0, "QUANTA-BGP-MIB", "agentBGPQueueIndex"),
)
if mibBuilder.loadTexts:
    agentBGPQueueEntry.setStatus("current")
_AgentBGPQueueIndex_Type = Unsigned32
_AgentBGPQueueIndex_Object = MibTableColumn
agentBGPQueueIndex = _AgentBGPQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1, 1, 1),
    _AgentBGPQueueIndex_Type()
)
agentBGPQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentBGPQueueIndex.setStatus("current")
_AgentBGPQueueName_Type = DisplayString
_AgentBGPQueueName_Object = MibTableColumn
agentBGPQueueName = _AgentBGPQueueName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1, 1, 2),
    _AgentBGPQueueName_Type()
)
agentBGPQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPQueueName.setStatus("current")
_AgentBGPQueueLength_Type = Gauge32
_AgentBGPQueueLength_Object = MibTableColumn
agentBGPQueueLength = _AgentBGPQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1, 1, 3),
    _AgentBGPQueueLength_Type()
)
agentBGPQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPQueueLength.setStatus("current")
_AgentBGPQueueHigh_Type = Gauge32
_AgentBGPQueueHigh_Object = MibTableColumn
agentBGPQueueHigh = _AgentBGPQueueHigh_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1, 1, 4),
    _AgentBGPQueueHigh_Type()
)
agentBGPQueueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPQueueHigh.setStatus("current")
_AgentBGPQueueDrops_Type = Counter32
_AgentBGPQueueDrops_Object = MibTableColumn
agentBGPQueueDrops = _AgentBGPQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1, 1, 5),
    _AgentBGPQueueDrops_Type()
)
agentBGPQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPQueueDrops.setStatus("current")
_AgentBGPQueueLimit_Type = Unsigned32
_AgentBGPQueueLimit_Object = MibTableColumn
agentBGPQueueLimit = _AgentBGPQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 1, 1, 1, 6),
    _AgentBGPQueueLimit_Type()
)
agentBGPQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPQueueLimit.setStatus("current")
_AgentBGPMessageStatsGroup_ObjectIdentity = ObjectIdentity
agentBGPMessageStatsGroup = _AgentBGPMessageStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2)
)
_AgentBGPCountersCleared_Type = TimeTicks
_AgentBGPCountersCleared_Object = MibScalar
agentBGPCountersCleared = _AgentBGPCountersCleared_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 1),
    _AgentBGPCountersCleared_Type()
)
agentBGPCountersCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPCountersCleared.setStatus("current")
_AgentBGPInOpens_Type = Counter32
_AgentBGPInOpens_Object = MibScalar
agentBGPInOpens = _AgentBGPInOpens_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 2),
    _AgentBGPInOpens_Type()
)
agentBGPInOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPInOpens.setStatus("current")
_AgentBGPOutOpens_Type = Counter32
_AgentBGPOutOpens_Object = MibScalar
agentBGPOutOpens = _AgentBGPOutOpens_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 3),
    _AgentBGPOutOpens_Type()
)
agentBGPOutOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPOutOpens.setStatus("current")
_AgentBGPInUpdates_Type = Counter32
_AgentBGPInUpdates_Object = MibScalar
agentBGPInUpdates = _AgentBGPInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 4),
    _AgentBGPInUpdates_Type()
)
agentBGPInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPInUpdates.setStatus("current")
_AgentBGPOutUpdates_Type = Counter32
_AgentBGPOutUpdates_Object = MibScalar
agentBGPOutUpdates = _AgentBGPOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 5),
    _AgentBGPOutUpdates_Type()
)
agentBGPOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPOutUpdates.setStatus("current")
_AgentBGPInNotifications_Type = Counter32
_AgentBGPInNotifications_Object = MibScalar
agentBGPInNotifications = _AgentBGPInNotifications_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 6),
    _AgentBGPInNotifications_Type()
)
agentBGPInNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPInNotifications.setStatus("current")
_AgentBGPOutNotifications_Type = Counter32
_AgentBGPOutNotifications_Object = MibScalar
agentBGPOutNotifications = _AgentBGPOutNotifications_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 7),
    _AgentBGPOutNotifications_Type()
)
agentBGPOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPOutNotifications.setStatus("current")
_AgentBGPInKeepalives_Type = Counter32
_AgentBGPInKeepalives_Object = MibScalar
agentBGPInKeepalives = _AgentBGPInKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 8),
    _AgentBGPInKeepalives_Type()
)
agentBGPInKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPInKeepalives.setStatus("current")
_AgentBGPOutKeepalives_Type = Counter32
_AgentBGPOutKeepalives_Object = MibScalar
agentBGPOutKeepalives = _AgentBGPOutKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 9),
    _AgentBGPOutKeepalives_Type()
)
agentBGPOutKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPOutKeepalives.setStatus("current")
_AgentBGPInRouteRefreshes_Type = Counter32
_AgentBGPInRouteRefreshes_Object = MibScalar
agentBGPInRouteRefreshes = _AgentBGPInRouteRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 10),
    _AgentBGPInRouteRefreshes_Type()
)
agentBGPInRouteRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPInRouteRefreshes.setStatus("current")
_AgentBGPOutRouteRefreshes_Type = Counter32
_AgentBGPOutRouteRefreshes_Object = MibScalar
agentBGPOutRouteRefreshes = _AgentBGPOutRouteRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 11),
    _AgentBGPOutRouteRefreshes_Type()
)
agentBGPOutRouteRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPOutRouteRefreshes.setStatus("current")
_AgentBGPInUpdatesMax_Type = Gauge32
_AgentBGPInUpdatesMax_Object = MibScalar
agentBGPInUpdatesMax = _AgentBGPInUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 12),
    _AgentBGPInUpdatesMax_Type()
)
agentBGPInUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPInUpdatesMax.setStatus("current")
_AgentBGPOutUpdatesMax_Type = Gauge32
_AgentBGPOutUpdatesMax_Object = MibScalar
agentBGPOutUpdatesMax = _AgentBGPOutUpdatesMax_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 2, 13),
    _AgentBGPOutUpdatesMax_Type()
)
agentBGPOutUpdatesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPOutUpdatesMax.setStatus("current")
_AgentBGPDecProcTable_Object = MibTable
agentBGPDecProcTable = _AgentBGPDecProcTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3)
)
if mibBuilder.loadTexts:
    agentBGPDecProcTable.setStatus("current")
_AgentBGPDecProcEntry_Object = MibTableRow
agentBGPDecProcEntry = _AgentBGPDecProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1)
)
agentBGPDecProcEntry.setIndexNames(
    (0, "QUANTA-BGP-MIB", "agentBGPDecProcIndex"),
)
if mibBuilder.loadTexts:
    agentBGPDecProcEntry.setStatus("current")
_AgentBGPDecProcIndex_Type = Counter32
_AgentBGPDecProcIndex_Object = MibTableColumn
agentBGPDecProcIndex = _AgentBGPDecProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 1),
    _AgentBGPDecProcIndex_Type()
)
agentBGPDecProcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentBGPDecProcIndex.setStatus("current")
_AgentBGPDecProcDeltaT_Type = Unsigned32
_AgentBGPDecProcDeltaT_Object = MibTableColumn
agentBGPDecProcDeltaT = _AgentBGPDecProcDeltaT_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 2),
    _AgentBGPDecProcDeltaT_Type()
)
agentBGPDecProcDeltaT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcDeltaT.setStatus("current")


class _AgentBGPDecProcPhase_Type(Unsigned32):
    """Custom type agentBGPDecProcPhase based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AgentBGPDecProcPhase_Type.__name__ = "Unsigned32"
_AgentBGPDecProcPhase_Object = MibTableColumn
agentBGPDecProcPhase = _AgentBGPDecProcPhase_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 3),
    _AgentBGPDecProcPhase_Type()
)
agentBGPDecProcPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcPhase.setStatus("current")
_AgentBGPDecProcUpdateGroup_Type = Unsigned32
_AgentBGPDecProcUpdateGroup_Object = MibTableColumn
agentBGPDecProcUpdateGroup = _AgentBGPDecProcUpdateGroup_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 4),
    _AgentBGPDecProcUpdateGroup_Type()
)
agentBGPDecProcUpdateGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcUpdateGroup.setStatus("current")
_AgentBGPDecProcGenId_Type = Unsigned32
_AgentBGPDecProcGenId_Object = MibTableColumn
agentBGPDecProcGenId = _AgentBGPDecProcGenId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 5),
    _AgentBGPDecProcGenId_Type()
)
agentBGPDecProcGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcGenId.setStatus("current")
_AgentBGPDecProcReason_Type = DisplayString
_AgentBGPDecProcReason_Object = MibTableColumn
agentBGPDecProcReason = _AgentBGPDecProcReason_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 6),
    _AgentBGPDecProcReason_Type()
)
agentBGPDecProcReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcReason.setStatus("current")
_AgentBGPDecProcPeer_Type = IpAddress
_AgentBGPDecProcPeer_Object = MibTableColumn
agentBGPDecProcPeer = _AgentBGPDecProcPeer_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 7),
    _AgentBGPDecProcPeer_Type()
)
agentBGPDecProcPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcPeer.setStatus("current")
_AgentBGPDecProcDuration_Type = Gauge32
_AgentBGPDecProcDuration_Object = MibTableColumn
agentBGPDecProcDuration = _AgentBGPDecProcDuration_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 8),
    _AgentBGPDecProcDuration_Type()
)
agentBGPDecProcDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcDuration.setStatus("current")
_AgentBGPDecProcAdds_Type = Gauge32
_AgentBGPDecProcAdds_Object = MibTableColumn
agentBGPDecProcAdds = _AgentBGPDecProcAdds_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 9),
    _AgentBGPDecProcAdds_Type()
)
agentBGPDecProcAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcAdds.setStatus("current")
_AgentBGPDecProcMods_Type = Gauge32
_AgentBGPDecProcMods_Object = MibTableColumn
agentBGPDecProcMods = _AgentBGPDecProcMods_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 10),
    _AgentBGPDecProcMods_Type()
)
agentBGPDecProcMods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcMods.setStatus("current")
_AgentBGPDecProcDels_Type = Gauge32
_AgentBGPDecProcDels_Object = MibTableColumn
agentBGPDecProcDels = _AgentBGPDecProcDels_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 3, 1, 11),
    _AgentBGPDecProcDels_Type()
)
agentBGPDecProcDels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPDecProcDels.setStatus("current")
_AgentBGPPeerTable_Object = MibTable
agentBGPPeerTable = _AgentBGPPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4)
)
if mibBuilder.loadTexts:
    agentBGPPeerTable.setStatus("current")
_AgentBGPPeerEntry_Object = MibTableRow
agentBGPPeerEntry = _AgentBGPPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1)
)
agentBGPPeerEntry.setIndexNames(
    (0, "QUANTA-BGP-MIB", "agentBGPPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    agentBGPPeerEntry.setStatus("current")
_AgentBGPPeerRemoteAddr_Type = IpAddress
_AgentBGPPeerRemoteAddr_Object = MibTableColumn
agentBGPPeerRemoteAddr = _AgentBGPPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 1),
    _AgentBGPPeerRemoteAddr_Type()
)
agentBGPPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerRemoteAddr.setStatus("current")
_AgentBGPPeerInOpens_Type = Counter32
_AgentBGPPeerInOpens_Object = MibTableColumn
agentBGPPeerInOpens = _AgentBGPPeerInOpens_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 2),
    _AgentBGPPeerInOpens_Type()
)
agentBGPPeerInOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInOpens.setStatus("current")
_AgentBGPPeerOutOpens_Type = Counter32
_AgentBGPPeerOutOpens_Object = MibTableColumn
agentBGPPeerOutOpens = _AgentBGPPeerOutOpens_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 3),
    _AgentBGPPeerOutOpens_Type()
)
agentBGPPeerOutOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutOpens.setStatus("current")
_AgentBGPPeerInUpdates_Type = Counter32
_AgentBGPPeerInUpdates_Object = MibTableColumn
agentBGPPeerInUpdates = _AgentBGPPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 4),
    _AgentBGPPeerInUpdates_Type()
)
agentBGPPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInUpdates.setStatus("current")
_AgentBGPPeerOutUpdates_Type = Counter32
_AgentBGPPeerOutUpdates_Object = MibTableColumn
agentBGPPeerOutUpdates = _AgentBGPPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 5),
    _AgentBGPPeerOutUpdates_Type()
)
agentBGPPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutUpdates.setStatus("current")
_AgentBGPPeerInNotifications_Type = Counter32
_AgentBGPPeerInNotifications_Object = MibTableColumn
agentBGPPeerInNotifications = _AgentBGPPeerInNotifications_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 6),
    _AgentBGPPeerInNotifications_Type()
)
agentBGPPeerInNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInNotifications.setStatus("current")
_AgentBGPPeerOutNotifications_Type = Counter32
_AgentBGPPeerOutNotifications_Object = MibTableColumn
agentBGPPeerOutNotifications = _AgentBGPPeerOutNotifications_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 7),
    _AgentBGPPeerOutNotifications_Type()
)
agentBGPPeerOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutNotifications.setStatus("current")
_AgentBGPPeerInKeepalives_Type = Counter32
_AgentBGPPeerInKeepalives_Object = MibTableColumn
agentBGPPeerInKeepalives = _AgentBGPPeerInKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 8),
    _AgentBGPPeerInKeepalives_Type()
)
agentBGPPeerInKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInKeepalives.setStatus("current")
_AgentBGPPeerOutKeepalives_Type = Counter32
_AgentBGPPeerOutKeepalives_Object = MibTableColumn
agentBGPPeerOutKeepalives = _AgentBGPPeerOutKeepalives_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 9),
    _AgentBGPPeerOutKeepalives_Type()
)
agentBGPPeerOutKeepalives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutKeepalives.setStatus("current")
_AgentBGPPeerInRouteRefreshes_Type = Counter32
_AgentBGPPeerInRouteRefreshes_Object = MibTableColumn
agentBGPPeerInRouteRefreshes = _AgentBGPPeerInRouteRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 10),
    _AgentBGPPeerInRouteRefreshes_Type()
)
agentBGPPeerInRouteRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInRouteRefreshes.setStatus("current")
_AgentBGPPeerOutRouteRefreshes_Type = Counter32
_AgentBGPPeerOutRouteRefreshes_Object = MibTableColumn
agentBGPPeerOutRouteRefreshes = _AgentBGPPeerOutRouteRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 11),
    _AgentBGPPeerOutRouteRefreshes_Type()
)
agentBGPPeerOutRouteRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutRouteRefreshes.setStatus("current")
_AgentBGPPeerInTotalMessages_Type = Counter32
_AgentBGPPeerInTotalMessages_Object = MibTableColumn
agentBGPPeerInTotalMessages = _AgentBGPPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 12),
    _AgentBGPPeerInTotalMessages_Type()
)
agentBGPPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInTotalMessages.setStatus("current")
_AgentBGPPeerOutTotalMessages_Type = Counter32
_AgentBGPPeerOutTotalMessages_Object = MibTableColumn
agentBGPPeerOutTotalMessages = _AgentBGPPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 13),
    _AgentBGPPeerOutTotalMessages_Type()
)
agentBGPPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutTotalMessages.setStatus("current")
_AgentBGPPeerUpdateQueueLen_Type = Gauge32
_AgentBGPPeerUpdateQueueLen_Object = MibTableColumn
agentBGPPeerUpdateQueueLen = _AgentBGPPeerUpdateQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 14),
    _AgentBGPPeerUpdateQueueLen_Type()
)
agentBGPPeerUpdateQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerUpdateQueueLen.setStatus("current")
_AgentBGPPeerUpdateQueueHigh_Type = Gauge32
_AgentBGPPeerUpdateQueueHigh_Object = MibTableColumn
agentBGPPeerUpdateQueueHigh = _AgentBGPPeerUpdateQueueHigh_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 15),
    _AgentBGPPeerUpdateQueueHigh_Type()
)
agentBGPPeerUpdateQueueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerUpdateQueueHigh.setStatus("current")
_AgentBGPPeerUpdateQueueLimit_Type = Unsigned32
_AgentBGPPeerUpdateQueueLimit_Object = MibTableColumn
agentBGPPeerUpdateQueueLimit = _AgentBGPPeerUpdateQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 16),
    _AgentBGPPeerUpdateQueueLimit_Type()
)
agentBGPPeerUpdateQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerUpdateQueueLimit.setStatus("current")
_AgentBGPPeerUpdateQueueDrops_Type = Counter32
_AgentBGPPeerUpdateQueueDrops_Object = MibTableColumn
agentBGPPeerUpdateQueueDrops = _AgentBGPPeerUpdateQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 17),
    _AgentBGPPeerUpdateQueueDrops_Type()
)
agentBGPPeerUpdateQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerUpdateQueueDrops.setStatus("current")
_AgentBGPPeerInPfxAdv_Type = Counter32
_AgentBGPPeerInPfxAdv_Object = MibTableColumn
agentBGPPeerInPfxAdv = _AgentBGPPeerInPfxAdv_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 18),
    _AgentBGPPeerInPfxAdv_Type()
)
agentBGPPeerInPfxAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInPfxAdv.setStatus("current")
_AgentBGPPeerOutPfxAdv_Type = Counter32
_AgentBGPPeerOutPfxAdv_Object = MibTableColumn
agentBGPPeerOutPfxAdv = _AgentBGPPeerOutPfxAdv_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 19),
    _AgentBGPPeerOutPfxAdv_Type()
)
agentBGPPeerOutPfxAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutPfxAdv.setStatus("current")
_AgentBGPPeerInPfxWithdrawn_Type = Counter32
_AgentBGPPeerInPfxWithdrawn_Object = MibTableColumn
agentBGPPeerInPfxWithdrawn = _AgentBGPPeerInPfxWithdrawn_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 20),
    _AgentBGPPeerInPfxWithdrawn_Type()
)
agentBGPPeerInPfxWithdrawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInPfxWithdrawn.setStatus("current")
_AgentBGPPeerOutPfxWithdrawn_Type = Counter32
_AgentBGPPeerOutPfxWithdrawn_Object = MibTableColumn
agentBGPPeerOutPfxWithdrawn = _AgentBGPPeerOutPfxWithdrawn_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 21),
    _AgentBGPPeerOutPfxWithdrawn_Type()
)
agentBGPPeerOutPfxWithdrawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutPfxWithdrawn.setStatus("current")
_AgentBGPPeerInPfxCurrent_Type = Gauge32
_AgentBGPPeerInPfxCurrent_Object = MibTableColumn
agentBGPPeerInPfxCurrent = _AgentBGPPeerInPfxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 22),
    _AgentBGPPeerInPfxCurrent_Type()
)
agentBGPPeerInPfxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInPfxCurrent.setStatus("current")
_AgentBGPPeerOutPfxCurrent_Type = Gauge32
_AgentBGPPeerOutPfxCurrent_Object = MibTableColumn
agentBGPPeerOutPfxCurrent = _AgentBGPPeerOutPfxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 23),
    _AgentBGPPeerOutPfxCurrent_Type()
)
agentBGPPeerOutPfxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutPfxCurrent.setStatus("current")
_AgentBGPPeerInPfxAccepted_Type = Gauge32
_AgentBGPPeerInPfxAccepted_Object = MibTableColumn
agentBGPPeerInPfxAccepted = _AgentBGPPeerInPfxAccepted_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 24),
    _AgentBGPPeerInPfxAccepted_Type()
)
agentBGPPeerInPfxAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInPfxAccepted.setStatus("current")
_AgentBGPPeerInPfxRejected_Type = Gauge32
_AgentBGPPeerInPfxRejected_Object = MibTableColumn
agentBGPPeerInPfxRejected = _AgentBGPPeerInPfxRejected_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 25),
    _AgentBGPPeerInPfxRejected_Type()
)
agentBGPPeerInPfxRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInPfxRejected.setStatus("current")
_AgentBGPPeerInMaxNlriPerUpdate_Type = Gauge32
_AgentBGPPeerInMaxNlriPerUpdate_Object = MibTableColumn
agentBGPPeerInMaxNlriPerUpdate = _AgentBGPPeerInMaxNlriPerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 26),
    _AgentBGPPeerInMaxNlriPerUpdate_Type()
)
agentBGPPeerInMaxNlriPerUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInMaxNlriPerUpdate.setStatus("current")
_AgentBGPPeerOutMaxNlriPerUpdate_Type = Gauge32
_AgentBGPPeerOutMaxNlriPerUpdate_Object = MibTableColumn
agentBGPPeerOutMaxNlriPerUpdate = _AgentBGPPeerOutMaxNlriPerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 27),
    _AgentBGPPeerOutMaxNlriPerUpdate_Type()
)
agentBGPPeerOutMaxNlriPerUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutMaxNlriPerUpdate.setStatus("current")
_AgentBGPPeerInMinNlriPerUpdate_Type = Gauge32
_AgentBGPPeerInMinNlriPerUpdate_Object = MibTableColumn
agentBGPPeerInMinNlriPerUpdate = _AgentBGPPeerInMinNlriPerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 28),
    _AgentBGPPeerInMinNlriPerUpdate_Type()
)
agentBGPPeerInMinNlriPerUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerInMinNlriPerUpdate.setStatus("current")
_AgentBGPPeerOutMinNlriPerUpdate_Type = Gauge32
_AgentBGPPeerOutMinNlriPerUpdate_Object = MibTableColumn
agentBGPPeerOutMinNlriPerUpdate = _AgentBGPPeerOutMinNlriPerUpdate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 5, 4, 1, 29),
    _AgentBGPPeerOutMinNlriPerUpdate_Type()
)
agentBGPPeerOutMinNlriPerUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBGPPeerOutMinNlriPerUpdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QUANTA-BGP-MIB",
    **{"quantaBGP": quantaBGP,
       "agentBGPQueueGroup": agentBGPQueueGroup,
       "agentBGPQueueTable": agentBGPQueueTable,
       "agentBGPQueueEntry": agentBGPQueueEntry,
       "agentBGPQueueIndex": agentBGPQueueIndex,
       "agentBGPQueueName": agentBGPQueueName,
       "agentBGPQueueLength": agentBGPQueueLength,
       "agentBGPQueueHigh": agentBGPQueueHigh,
       "agentBGPQueueDrops": agentBGPQueueDrops,
       "agentBGPQueueLimit": agentBGPQueueLimit,
       "agentBGPMessageStatsGroup": agentBGPMessageStatsGroup,
       "agentBGPCountersCleared": agentBGPCountersCleared,
       "agentBGPInOpens": agentBGPInOpens,
       "agentBGPOutOpens": agentBGPOutOpens,
       "agentBGPInUpdates": agentBGPInUpdates,
       "agentBGPOutUpdates": agentBGPOutUpdates,
       "agentBGPInNotifications": agentBGPInNotifications,
       "agentBGPOutNotifications": agentBGPOutNotifications,
       "agentBGPInKeepalives": agentBGPInKeepalives,
       "agentBGPOutKeepalives": agentBGPOutKeepalives,
       "agentBGPInRouteRefreshes": agentBGPInRouteRefreshes,
       "agentBGPOutRouteRefreshes": agentBGPOutRouteRefreshes,
       "agentBGPInUpdatesMax": agentBGPInUpdatesMax,
       "agentBGPOutUpdatesMax": agentBGPOutUpdatesMax,
       "agentBGPDecProcTable": agentBGPDecProcTable,
       "agentBGPDecProcEntry": agentBGPDecProcEntry,
       "agentBGPDecProcIndex": agentBGPDecProcIndex,
       "agentBGPDecProcDeltaT": agentBGPDecProcDeltaT,
       "agentBGPDecProcPhase": agentBGPDecProcPhase,
       "agentBGPDecProcUpdateGroup": agentBGPDecProcUpdateGroup,
       "agentBGPDecProcGenId": agentBGPDecProcGenId,
       "agentBGPDecProcReason": agentBGPDecProcReason,
       "agentBGPDecProcPeer": agentBGPDecProcPeer,
       "agentBGPDecProcDuration": agentBGPDecProcDuration,
       "agentBGPDecProcAdds": agentBGPDecProcAdds,
       "agentBGPDecProcMods": agentBGPDecProcMods,
       "agentBGPDecProcDels": agentBGPDecProcDels,
       "agentBGPPeerTable": agentBGPPeerTable,
       "agentBGPPeerEntry": agentBGPPeerEntry,
       "agentBGPPeerRemoteAddr": agentBGPPeerRemoteAddr,
       "agentBGPPeerInOpens": agentBGPPeerInOpens,
       "agentBGPPeerOutOpens": agentBGPPeerOutOpens,
       "agentBGPPeerInUpdates": agentBGPPeerInUpdates,
       "agentBGPPeerOutUpdates": agentBGPPeerOutUpdates,
       "agentBGPPeerInNotifications": agentBGPPeerInNotifications,
       "agentBGPPeerOutNotifications": agentBGPPeerOutNotifications,
       "agentBGPPeerInKeepalives": agentBGPPeerInKeepalives,
       "agentBGPPeerOutKeepalives": agentBGPPeerOutKeepalives,
       "agentBGPPeerInRouteRefreshes": agentBGPPeerInRouteRefreshes,
       "agentBGPPeerOutRouteRefreshes": agentBGPPeerOutRouteRefreshes,
       "agentBGPPeerInTotalMessages": agentBGPPeerInTotalMessages,
       "agentBGPPeerOutTotalMessages": agentBGPPeerOutTotalMessages,
       "agentBGPPeerUpdateQueueLen": agentBGPPeerUpdateQueueLen,
       "agentBGPPeerUpdateQueueHigh": agentBGPPeerUpdateQueueHigh,
       "agentBGPPeerUpdateQueueLimit": agentBGPPeerUpdateQueueLimit,
       "agentBGPPeerUpdateQueueDrops": agentBGPPeerUpdateQueueDrops,
       "agentBGPPeerInPfxAdv": agentBGPPeerInPfxAdv,
       "agentBGPPeerOutPfxAdv": agentBGPPeerOutPfxAdv,
       "agentBGPPeerInPfxWithdrawn": agentBGPPeerInPfxWithdrawn,
       "agentBGPPeerOutPfxWithdrawn": agentBGPPeerOutPfxWithdrawn,
       "agentBGPPeerInPfxCurrent": agentBGPPeerInPfxCurrent,
       "agentBGPPeerOutPfxCurrent": agentBGPPeerOutPfxCurrent,
       "agentBGPPeerInPfxAccepted": agentBGPPeerInPfxAccepted,
       "agentBGPPeerInPfxRejected": agentBGPPeerInPfxRejected,
       "agentBGPPeerInMaxNlriPerUpdate": agentBGPPeerInMaxNlriPerUpdate,
       "agentBGPPeerOutMaxNlriPerUpdate": agentBGPPeerOutMaxNlriPerUpdate,
       "agentBGPPeerInMinNlriPerUpdate": agentBGPPeerInMinNlriPerUpdate,
       "agentBGPPeerOutMinNlriPerUpdate": agentBGPPeerOutMinNlriPerUpdate}
)
