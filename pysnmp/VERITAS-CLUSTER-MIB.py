# SNMP MIB module (VERITAS-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERITAS-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:20 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

veritasCluster = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Veritassoftware_ObjectIdentity = ObjectIdentity
veritassoftware = _Veritassoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3)
)
_Clustertraps_ObjectIdentity = ObjectIdentity
clustertraps = _Clustertraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10)
)
_Clustertrapvars_ObjectIdentity = ObjectIdentity
clustertrapvars = _Clustertrapvars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1)
)


class _TrapOrigin_Type(DisplayString):
    """Custom type trapOrigin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TrapOrigin_Type.__name__ = "DisplayString"
_TrapOrigin_Object = MibScalar
trapOrigin = _TrapOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 1),
    _TrapOrigin_Type()
)
trapOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOrigin.setStatus("mandatory")


class _EntityType_Type(DisplayString):
    """Custom type entityType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EntityType_Type.__name__ = "DisplayString"
_EntityType_Object = MibScalar
entityType = _EntityType_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 2),
    _EntityType_Type()
)
entityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityType.setStatus("mandatory")


class _EntitySubType_Type(DisplayString):
    """Custom type entitySubType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EntitySubType_Type.__name__ = "DisplayString"
_EntitySubType_Object = MibScalar
entitySubType = _EntitySubType_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 3),
    _EntitySubType_Type()
)
entitySubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entitySubType.setStatus("mandatory")


class _EntityName_Type(DisplayString):
    """Custom type entityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EntityName_Type.__name__ = "DisplayString"
_EntityName_Object = MibScalar
entityName = _EntityName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 4),
    _EntityName_Type()
)
entityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityName.setStatus("mandatory")


class _EntityOwner_Type(DisplayString):
    """Custom type entityOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EntityOwner_Type.__name__ = "DisplayString"
_EntityOwner_Object = MibScalar
entityOwner = _EntityOwner_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 5),
    _EntityOwner_Type()
)
entityOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityOwner.setStatus("mandatory")


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 6),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("mandatory")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 7),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLocation.setStatus("mandatory")


class _EntityState_Type(DisplayString):
    """Custom type entityState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EntityState_Type.__name__ = "DisplayString"
_EntityState_Object = MibScalar
entityState = _EntityState_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 8),
    _EntityState_Type()
)
entityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityState.setStatus("mandatory")


class _EntityContainerType_Type(DisplayString):
    """Custom type entityContainerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EntityContainerType_Type.__name__ = "DisplayString"
_EntityContainerType_Object = MibScalar
entityContainerType = _EntityContainerType_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 9),
    _EntityContainerType_Type()
)
entityContainerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityContainerType.setStatus("mandatory")


class _EntityContainerName_Type(DisplayString):
    """Custom type entityContainerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EntityContainerName_Type.__name__ = "DisplayString"
_EntityContainerName_Object = MibScalar
entityContainerName = _EntityContainerName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 10),
    _EntityContainerName_Type()
)
entityContainerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityContainerName.setStatus("mandatory")


class _PeerSystemName_Type(DisplayString):
    """Custom type peerSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PeerSystemName_Type.__name__ = "DisplayString"
_PeerSystemName_Object = MibScalar
peerSystemName = _PeerSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 11),
    _PeerSystemName_Type()
)
peerSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerSystemName.setStatus("mandatory")


class _PeerSystemLocation_Type(DisplayString):
    """Custom type peerSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PeerSystemLocation_Type.__name__ = "DisplayString"
_PeerSystemLocation_Object = MibScalar
peerSystemLocation = _PeerSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 12),
    _PeerSystemLocation_Type()
)
peerSystemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerSystemLocation.setStatus("mandatory")


class _Message_Type(DisplayString):
    """Custom type message based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Message_Type.__name__ = "DisplayString"
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 13),
    _Message_Type()
)
message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    message.setStatus("mandatory")


class _EventTime_Type(DisplayString):
    """Custom type eventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_EventTime_Type.__name__ = "DisplayString"
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 14),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("mandatory")


class _SeverityId_Type(Integer32):
    """Custom type severityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("information", 0),
          ("severeError", 3),
          ("warning", 1))
    )


_SeverityId_Type.__name__ = "Integer32"
_SeverityId_Object = MibScalar
severityId = _SeverityId_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 1, 15),
    _SeverityId_Type()
)
severityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityId.setStatus("mandatory")
_ClustertrapsGroups_ObjectIdentity = ObjectIdentity
clustertrapsGroups = _ClustertrapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2)
)
_ResourcesTraps_ObjectIdentity = ObjectIdentity
resourcesTraps = _ResourcesTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 1)
)
_GroupsTraps_ObjectIdentity = ObjectIdentity
groupsTraps = _GroupsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2)
)
_SystemsTraps_ObjectIdentity = ObjectIdentity
systemsTraps = _SystemsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3)
)
_VcsHeartbeatTraps_ObjectIdentity = ObjectIdentity
vcsHeartbeatTraps = _VcsHeartbeatTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 4)
)
_GcmHeartbeatTraps_ObjectIdentity = ObjectIdentity
gcmHeartbeatTraps = _GcmHeartbeatTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 5)
)
_VcsTraps_ObjectIdentity = ObjectIdentity
vcsTraps = _VcsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 6)
)
_GcmSiteTraps_ObjectIdentity = ObjectIdentity
gcmSiteTraps = _GcmSiteTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 7)
)
_AgentsTraps_ObjectIdentity = ObjectIdentity
agentsTraps = _AgentsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 8)
)
_ExternalTraps_ObjectIdentity = ObjectIdentity
externalTraps = _ExternalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 9)
)
_RdcTraps_ObjectIdentity = ObjectIdentity
rdcTraps = _RdcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10)
)

# Managed Objects groups


# Notification objects

clusterResourceStateUnknownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 1, 0, 1)
)
clusterResourceStateUnknownTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterResourceStateUnknownTrap.setStatus(
        ""
    )

clusterResourceMonitorTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 1, 0, 2)
)
clusterResourceMonitorTimeoutTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterResourceMonitorTimeoutTrap.setStatus(
        ""
    )

clusterResourceNotGoingOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 1, 0, 3)
)
clusterResourceNotGoingOfflineTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterResourceNotGoingOfflineTrap.setStatus(
        ""
    )

clusterResourceRestartingByAgentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 1, 0, 4)
)
clusterResourceRestartingByAgentTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterResourceRestartingByAgentTrap.setStatus(
        ""
    )

clusterResourceWentOnlineByItselfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 1, 0, 5)
)
clusterResourceWentOnlineByItselfTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterResourceWentOnlineByItselfTrap.setStatus(
        ""
    )

clusterResourceFaultedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 1, 0, 6)
)
clusterResourceFaultedTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterResourceFaultedTrap.setStatus(
        ""
    )

clusterGroupOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 1)
)
clusterGroupOnlineTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupOnlineTrap.setStatus(
        ""
    )

clusterGroupOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 2)
)
clusterGroupOfflineTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupOfflineTrap.setStatus(
        ""
    )

clusterGroupAutoDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 3)
)
clusterGroupAutoDisabledTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupAutoDisabledTrap.setStatus(
        ""
    )

clusterGroupFaultedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 4)
)
clusterGroupFaultedTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupFaultedTrap.setStatus(
        ""
    )

clusterGroupFaultedAndNowhereToFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 5)
)
clusterGroupFaultedAndNowhereToFailoverTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupFaultedAndNowhereToFailoverTrap.setStatus(
        ""
    )

clusterGroupRestartingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 6)
)
clusterGroupRestartingTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupRestartingTrap.setStatus(
        ""
    )

clusterGroupInitiatingForSwitchingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 7)
)
clusterGroupInitiatingForSwitchingTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupInitiatingForSwitchingTrap.setStatus(
        ""
    )

clusterGroupConcurencyViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 8)
)
clusterGroupConcurencyViolationTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupConcurencyViolationTrap.setStatus(
        ""
    )

clusterGroupRestInRspnToPerstResGoOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 2, 0, 9)
)
clusterGroupRestInRspnToPerstResGoOnlineTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGroupRestInRspnToPerstResGoOnlineTrap.setStatus(
        ""
    )

clusterFirstSystemUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 1)
)
clusterFirstSystemUpTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterFirstSystemUpTrap.setStatus(
        ""
    )

clusterSystemRestartingByHashadowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 2)
)
clusterSystemRestartingByHashadowTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterSystemRestartingByHashadowTrap.setStatus(
        ""
    )

clusterSystemInJeopardyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 3)
)
clusterSystemInJeopardyTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterSystemInJeopardyTrap.setStatus(
        ""
    )

clusterSystemFaultedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 4)
)
clusterSystemFaultedTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterSystemFaultedTrap.setStatus(
        ""
    )

clusterSystemJoinedClusterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 5)
)
clusterSystemJoinedClusterTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterSystemJoinedClusterTrap.setStatus(
        ""
    )

clusterSystemExitedManuallyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 6)
)
clusterSystemExitedManuallyTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterSystemExitedManuallyTrap.setStatus(
        ""
    )

clusterSystemUpButNotInClusterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 7)
)
clusterSystemUpButNotInClusterTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterSystemUpButNotInClusterTrap.setStatus(
        ""
    )

clusterSystemUsageExceededThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 3, 0, 8)
)
clusterSystemUsageExceededThresholdTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterSystemUsageExceededThresholdTrap.setStatus(
        ""
    )

clusterGUIUserLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 6, 0, 2)
)
clusterGUIUserLoginTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterGUIUserLoginTrap.setStatus(
        ""
    )

clusterAgentRestartingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 8, 0, 1)
)
clusterAgentRestartingTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterAgentRestartingTrap.setStatus(
        ""
    )

clusterAgentFaultedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 8, 0, 2)
)
clusterAgentFaultedTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterAgentFaultedTrap.setStatus(
        ""
    )

clusterRDCRlinkInconsistentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 1)
)
clusterRDCRlinkInconsistentTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCRlinkInconsistentTrap.setStatus(
        ""
    )

clusterRDCRlinkNotUpToDateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 2)
)
clusterRDCRlinkNotUpToDateTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCRlinkNotUpToDateTrap.setStatus(
        ""
    )

clusterRDCTakeoverFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 3)
)
clusterRDCTakeoverFailedTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCTakeoverFailedTrap.setStatus(
        ""
    )

clusterRDCMigrateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 4)
)
clusterRDCMigrateFailedTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCMigrateFailedTrap.setStatus(
        ""
    )

clusterRDCTakeoverSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 5)
)
clusterRDCTakeoverSuccessTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCTakeoverSuccessTrap.setStatus(
        ""
    )

clusterRDCMigrateSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 6)
)
clusterRDCMigrateSuccessTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCMigrateSuccessTrap.setStatus(
        ""
    )

clusterRDCActingSecondaryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 7)
)
clusterRDCActingSecondaryTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCActingSecondaryTrap.setStatus(
        ""
    )

clusterRDCResyncFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 8)
)
clusterRDCResyncFailedTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCResyncFailedTrap.setStatus(
        ""
    )

clusterRDCResyncSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 9)
)
clusterRDCResyncSuccessTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCResyncSuccessTrap.setStatus(
        ""
    )

clusterRDCGroupOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 8, 10, 2, 10, 0, 10)
)
clusterRDCGroupOfflineTrap.setObjects(
      *(("VERITAS-CLUSTER-MIB", "severityId"),
        ("VERITAS-CLUSTER-MIB", "eventTime"),
        ("VERITAS-CLUSTER-MIB", "entityName"),
        ("VERITAS-CLUSTER-MIB", "entityType"),
        ("VERITAS-CLUSTER-MIB", "entitySubType"),
        ("VERITAS-CLUSTER-MIB", "entityState"),
        ("VERITAS-CLUSTER-MIB", "trapOrigin"),
        ("VERITAS-CLUSTER-MIB", "systemName"),
        ("VERITAS-CLUSTER-MIB", "systemLocation"),
        ("VERITAS-CLUSTER-MIB", "entityContainerName"),
        ("VERITAS-CLUSTER-MIB", "entityContainerType"),
        ("VERITAS-CLUSTER-MIB", "entityOwner"),
        ("VERITAS-CLUSTER-MIB", "message"))
)
if mibBuilder.loadTexts:
    clusterRDCGroupOfflineTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERITAS-CLUSTER-MIB",
    **{"veritassoftware": veritassoftware,
       "products": products,
       "veritasCluster": veritasCluster,
       "clustertraps": clustertraps,
       "clustertrapvars": clustertrapvars,
       "trapOrigin": trapOrigin,
       "entityType": entityType,
       "entitySubType": entitySubType,
       "entityName": entityName,
       "entityOwner": entityOwner,
       "systemName": systemName,
       "systemLocation": systemLocation,
       "entityState": entityState,
       "entityContainerType": entityContainerType,
       "entityContainerName": entityContainerName,
       "peerSystemName": peerSystemName,
       "peerSystemLocation": peerSystemLocation,
       "message": message,
       "eventTime": eventTime,
       "severityId": severityId,
       "clustertrapsGroups": clustertrapsGroups,
       "resourcesTraps": resourcesTraps,
       "clusterResourceStateUnknownTrap": clusterResourceStateUnknownTrap,
       "clusterResourceMonitorTimeoutTrap": clusterResourceMonitorTimeoutTrap,
       "clusterResourceNotGoingOfflineTrap": clusterResourceNotGoingOfflineTrap,
       "clusterResourceRestartingByAgentTrap": clusterResourceRestartingByAgentTrap,
       "clusterResourceWentOnlineByItselfTrap": clusterResourceWentOnlineByItselfTrap,
       "clusterResourceFaultedTrap": clusterResourceFaultedTrap,
       "groupsTraps": groupsTraps,
       "clusterGroupOnlineTrap": clusterGroupOnlineTrap,
       "clusterGroupOfflineTrap": clusterGroupOfflineTrap,
       "clusterGroupAutoDisabledTrap": clusterGroupAutoDisabledTrap,
       "clusterGroupFaultedTrap": clusterGroupFaultedTrap,
       "clusterGroupFaultedAndNowhereToFailoverTrap": clusterGroupFaultedAndNowhereToFailoverTrap,
       "clusterGroupRestartingTrap": clusterGroupRestartingTrap,
       "clusterGroupInitiatingForSwitchingTrap": clusterGroupInitiatingForSwitchingTrap,
       "clusterGroupConcurencyViolationTrap": clusterGroupConcurencyViolationTrap,
       "clusterGroupRestInRspnToPerstResGoOnlineTrap": clusterGroupRestInRspnToPerstResGoOnlineTrap,
       "systemsTraps": systemsTraps,
       "clusterFirstSystemUpTrap": clusterFirstSystemUpTrap,
       "clusterSystemRestartingByHashadowTrap": clusterSystemRestartingByHashadowTrap,
       "clusterSystemInJeopardyTrap": clusterSystemInJeopardyTrap,
       "clusterSystemFaultedTrap": clusterSystemFaultedTrap,
       "clusterSystemJoinedClusterTrap": clusterSystemJoinedClusterTrap,
       "clusterSystemExitedManuallyTrap": clusterSystemExitedManuallyTrap,
       "clusterSystemUpButNotInClusterTrap": clusterSystemUpButNotInClusterTrap,
       "clusterSystemUsageExceededThresholdTrap": clusterSystemUsageExceededThresholdTrap,
       "vcsHeartbeatTraps": vcsHeartbeatTraps,
       "gcmHeartbeatTraps": gcmHeartbeatTraps,
       "vcsTraps": vcsTraps,
       "clusterGUIUserLoginTrap": clusterGUIUserLoginTrap,
       "gcmSiteTraps": gcmSiteTraps,
       "agentsTraps": agentsTraps,
       "clusterAgentRestartingTrap": clusterAgentRestartingTrap,
       "clusterAgentFaultedTrap": clusterAgentFaultedTrap,
       "externalTraps": externalTraps,
       "rdcTraps": rdcTraps,
       "clusterRDCRlinkInconsistentTrap": clusterRDCRlinkInconsistentTrap,
       "clusterRDCRlinkNotUpToDateTrap": clusterRDCRlinkNotUpToDateTrap,
       "clusterRDCTakeoverFailedTrap": clusterRDCTakeoverFailedTrap,
       "clusterRDCMigrateFailedTrap": clusterRDCMigrateFailedTrap,
       "clusterRDCTakeoverSuccessTrap": clusterRDCTakeoverSuccessTrap,
       "clusterRDCMigrateSuccessTrap": clusterRDCMigrateSuccessTrap,
       "clusterRDCActingSecondaryTrap": clusterRDCActingSecondaryTrap,
       "clusterRDCResyncFailedTrap": clusterRDCResyncFailedTrap,
       "clusterRDCResyncSuccessTrap": clusterRDCResyncSuccessTrap,
       "clusterRDCGroupOfflineTrap": clusterRDCGroupOfflineTrap}
)
